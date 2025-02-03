from random import randint

def getRandom(iterable: list|tuple|str):
    return iterable[randint(0, len(iterable)-1)]

imagenes_durisimas = (
    "https://media.discordapp.net/attachments/1180299519355789423/1180299527756988507/IMG_0011.png?ex=657cea98&is=656a7598&hm=dbc5ccb63408e42b98c932c989f7f8be6a670eef1dd03243169862850093c111&=&format=webp&quality=lossless&width=706&height=670",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180299663111372830/Fg5rGTKWQAYATk8.png?ex=657ceab8&is=656a75b8&hm=5fa8d01214bcbbfde472eb063ec775be2ed811682bbaae9d6ed79248930f9ae3&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180299756308795462/image-203.png?ex=657ceace&is=656a75ce&hm=460116cd48cae1ad7bac87c4dd581c4eb90fd68c91b329fca290b2fdca99da46&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180300514559262771/338867359_766185765006688_4617840974261837499_n.png?ex=657ceb83&is=656a7683&hm=cc5570865d2e152454d85f59381bf1659cebd973d742b5354793c46dc353be41&",
    "https://media.discordapp.net/attachments/1180299519355789423/1180300640921079818/IMG_2746.png?ex=657ceba1&is=656a76a1&hm=6cc3f5f38a3d3ba308accd850acf898b8e0de37906660b3e5ff81e1e18ae095b&=&format=webp&quality=lossless&width=670&height=670",
    "https://media.discordapp.net/attachments/1180299519355789423/1180301029246517258/20230322_202001.png?ex=657cebfe&is=656a76fe&hm=fa71f06c2325815a55e4b30e4ec0bf89ac0d4fd3fa8ed739c1fd16872826a7dc&=&format=webp&quality=lossless&width=502&height=670",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180301217579147335/RDT_20230323_1049128331850639630935609.png?ex=657cec2b&is=656a772b&hm=774843de632b387099e054a128c9b9b2e0f5c4d1058b31a38e3fc56fe4b51bb7&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180301399075078214/337026772_1252261899021080_6904948111367055482_n.png?ex=657cec56&is=656a7756&hm=3666982bb0cf4faab3ba6cd52a88cb16aa642a711c0d99c032c8b6ae5f82363c&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180301627660435528/Screenshot_2023-03-28-17-21-42-17_1c337646f29875672b5a61192b9010f92.png?ex=657cec8c&is=656a778c&hm=6368422cc3645d5d8f29f767bc7325e0c8a76713a911b565901081b621fe1e5b&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180302011783192678/0cb.png?ex=657cece8&is=656a77e8&hm=519d28490fb4bbe295783f0395b565f2d2b48fad9f921dc5606a6dcfaa3f227b&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180303519497076807/20230319_211511.png?ex=657cee50&is=656a7950&hm=33ce06dcde7d88dd67f12cf2f6621427c256055f4776e1b2ec1704a133aa110a&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180303536064573481/Sin_titulo.png?ex=657cee53&is=656a7953&hm=3674ebb614db594f2d42cc8ead2c843d23715c56055fa6968d59f7ef2e343765&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180305535103418429/342395911_2324871534567563_4486820074193641343_n.png?ex=657cf030&is=656a7b30&hm=37abbd9bf63f4a1cf65ad42c4469cec1b139c270b2614b9244f80de089146d00&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180305542644760576/image.png?ex=657cf032&is=656a7b32&hm=e4dde014a9a0141b142af233ef32183c4ce0f4df80047c6155afdd599de8a5e6&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180305950779904091/Screenshot_20230502_203814.png?ex=657cf093&is=656a7b93&hm=2475192fcb8eba74603797af8c6db5249819ac1d5f59d51df45e9f45044e258b&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180306241394847795/8B68A6BF-22D8-4C56-A7BB-2585534F3B21.png?ex=657cf0d8&is=656a7bd8&hm=79a19da95e35d6af76b6c2213b6511bf20f95c5ecbf8980b302e3de1c94980e7&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180306341923926036/20230504_095833.png?ex=657cf0f0&is=656a7bf0&hm=5eb104613519383d68e296d74ca7edf4d711bc1f5d8c3b0cca31702aaacd85c4&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180306955307323432/352331743_9449105765131544_4645824813795425888_n.png?ex=657cf183&is=656a7c83&hm=5fdcd66b2fc7e6efab5ffda47098cf0016564f828308738ff526aea79e8d182a&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180307309147193404/358139393_233078416209193_3837355328395094221_n.png?ex=657cf1d7&is=656a7cd7&hm=f1eea0c04879fac5e1bc36404592f81ee0354401c408ee86a319c5aded4563a4&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180309120486756383/358586801_813391517011246_1902181881902437089_n.png?ex=657cf387&is=656a7e87&hm=5a5deab597d225ae03e0574d2fce73db87ed703d26bb4895b099039dba720d05&",
    "https://cdn.discordapp.com/attachments/1179960160828018750/1180535054896734208/IMG_9861.png?ex=657dc5f2&is=656b50f2&hm=f0593d1cc72bce01b6a16cfc78a7e7c15255266157da25bdcdf24f1a25d2585b&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180741638138642544/PHOTO-2023-08-04-11-33-29.png?ex=657e8657&is=656c1157&hm=00367788a3cb5fb5db8eb7850a3e83803060a19df6832005f8552d6f7e280311&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180742735863496754/133_sin_titulo_20230813230847.png?ex=657e875d&is=656c125d&hm=6111ae5fa327bb6ec6e85f1caab55c34b72753bef456c64c2bf86700e795afb0&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180742793228976238/366621221_3488671121384671_5486585821918176056_n.png?ex=657e876b&is=656c126b&hm=79f9c6db11e7018687b1e7cffe4698cc3a4648ecac24e07396c307d0ed61520a&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180743460987359333/20230824_131721.png?ex=657e880a&is=656c130a&hm=9b7e57f6fe244ea186908cc3030dafdf13e2edf0f500a719ccf37942c0d12a4f&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180743525910978580/20230824_131138.png?ex=657e8819&is=656c1319&hm=5a81fea6cb705b18c2e926d1aaeff06b4c201c4a1e5f05e89556212879befe10&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180743875434917968/Screenshot_20230912_114001.png?ex=657e886d&is=656c136d&hm=d01e0fd38684ae39cb5286122af897b12a690bf04337a80bd0c88358c9536bd3&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180743931118493787/375902460_153947441094083_5378325415317850092_n.png?ex=657e887a&is=656c137a&hm=e396b8dcfaf5c69e592041ba85f2d6cc6009855eadc8efdc737a2e1557458ba3&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180744080611885096/511741AF-BD2D-4B0E-868C-8601708F459E.png?ex=657e889d&is=656c139d&hm=e65cb7e4878ceef239011346e62e209eb98d0a6b796f4dad41c3bc0199f3aa03&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180744156428111962/IMG_20230916_191524590.png?ex=657e88b0&is=656c13b0&hm=1526e6b563540f25d8ab74b7619f0d4b7f1e982c78ad60d028094f0a91d39efd&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180744322577076306/378167703_315257771187097_3467771468842427541_n.png?ex=657e88d7&is=656c13d7&hm=3b9a31fb6f1444c53d93ca3139f698be986a53be1c257bdc9d1d5e27942cd34f&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180744466638843955/image0-16_1.png?ex=657e88fa&is=656c13fa&hm=45a87e6d6b44935bb715068813557435e1393ab24e4044554e4dd44dda300766&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180744760017821736/Screenshot_20231012_200716.png?ex=657e893f&is=656c143f&hm=83718ec36a216c375d46150c5ff87aa65b7668d94ba1c83c37d28e549e3df24b&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180744856109318234/Screenshot_20231016_112911.png?ex=657e8956&is=656c1456&hm=d05439a735c4688f310c74e9a5083ac8acad2d97d58c0997e31169c46ec5f0f0&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180745015237025792/Screenshot_20231023_090820.png?ex=657e897c&is=656c147c&hm=aa6400071fb92e6ebbff7ec05a2989638eff88d6817e76503e64705d7fb388f3&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180745064876605500/Screenshot_20231023_090805.png?ex=657e8988&is=656c1488&hm=c7a2678f3c7a654726dca9c9d81fea190325263e722d71ebb59e635203aea3b7&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1180745618650562630/Screenshot_20231120_174347.png?ex=657e8a0c&is=656c150c&hm=b5273f278fa9db5b613f980516c3fd028e3ded3d7ba1a1b4bab41ff58276c3c1&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1185302573247365150/image.png?ex=658f1e0b&is=657ca90b&hm=7a45ae9d80937c32204dfa7c5460143594be4553ae36b0141591bb832c25679d&",
    "https://cdn.discordapp.com/attachments/1180299519355789423/1193317649157988352/image.png?ex=65ac46aa&is=6599d1aa&hm=33ff187cde3a1a84ac10151284da13a89097448f089d406c3a4106bf5baa98e9&"
    )

imagenes_starboard = (
    ("Balacera", "https://cdn.discordapp.com/attachments/1186763825005994036/1186763863929135114/image.png?ex=65946efa&is=6581f9fa&hm=d7036eedce943a4dbf54cfdbc35014a306ad95fa3a325400c41a1e94c1fb9679&"),
    ("Starboard", "https://cdn.discordapp.com/attachments/1186763825005994036/1186764568379269311/image.png?ex=65946fa2&is=6581faa2&hm=ef10bcc0fa38ed194149b2baa8845c2e0fda8396c21642545300c2429241e784&"),
    ("Sillón", "https://cdn.discordapp.com/attachments/1186763825005994036/1186766184150999071/image.png?ex=65947123&is=6581fc23&hm=3c276580c478e36d214c78e2c0803fe2d6906980a0730d5589c87f920486c905&"),
    ("Turrón", "https://cdn.discordapp.com/attachments/1186763825005994036/1186766847727652925/image.png?ex=659471c1&is=6581fcc1&hm=80daf18344b5885b4bcf2f0a2d3a63e2f0ad776e178e4f56a223196420e439bd&"),
    ("Número equivocado", "https://cdn.discordapp.com/attachments/1186763825005994036/1186767423261638777/image.png?ex=6594724a&is=6581fd4a&hm=45602f04d14308ea6937f8d0246328301389943dc98dea14662e82b149e91e04&"),
    ("Kitt", "https://cdn.discordapp.com/attachments/1186763825005994036/1186768087610052709/image.png?ex=659472e9&is=6581fde9&hm=9129d9811d393ff491496688ad23b27f84a09cb83a7d2d914852628a6db909c4&"),
    ("Niños de África", "https://cdn.discordapp.com/attachments/1186763825005994036/1186769162614341702/image.png?ex=659473e9&is=6581fee9&hm=47dc83ae4f79bb943ce77af3641867662dff0e1b94865a98500081f435be13d1&"),
    ("Mick", "https://cdn.discordapp.com/attachments/1186763825005994036/1186769632749682809/image.png?ex=65947459&is=6581ff59&hm=a7811c8d156e894bc971f50eca622979eff17cf37da9bbcd632ec5049f471a21&"),
    ("Chispop", "https://cdn.discordapp.com/attachments/1186763825005994036/1186770344153981139/image.png?ex=65947503&is=65820003&hm=00d70c7af5bbb55f8240199f91a3af6ae9e8befb3f142f199f54712917d6cf2e&"),
    ("La Logia", "https://cdn.discordapp.com/attachments/1186763825005994036/1186770920703021066/image.png?ex=6594758c&is=6582008c&hm=8ddb5ed90776c5b47805206de8879210a783485c191a140cdd57d7689af3daec&"),
    ("Disfraz", "https://cdn.discordapp.com/attachments/1186763825005994036/1186771467996774480/image.png?ex=6594760f&is=6582010f&hm=9affd773fe92c0c7cbe3b8db9306cafd07604cfcf645758e077e2142698c8310&"),
    ("Kitt se confiesa", "https://cdn.discordapp.com/attachments/1186763825005994036/1186772045120413726/image.png?ex=65947698&is=65820198&hm=493f87bfb5109b42d7356554f4a59c3b6920fd6a39da03c3ca3d241af7cb473f&"),
    ("Sciarpa famoso", "https://media.discordapp.net/attachments/1186763825005994036/1216912672470077440/IMG_20240220_171518_067.png?ex=66021d3e&is=65efa83e&hm=0b642875877f5901ded938b5958681ef5f147ac32db325ae83876f74ec028bbd&"),
    ("Wea god", "https://cdn.discordapp.com/attachments/1186763825005994036/1216913743238135869/image.png?ex=66021e3d&is=65efa93d&hm=d644ac1e56166d90dba4bd3e9f9e7232c7ce126abec36844976643c58280c31a&"),
    ("Lo es", "https://media.discordapp.net/attachments/1186763825005994036/1216914178737176628/image.png?ex=66021ea5&is=65efa9a5&hm=eb0c45e7e58ce4aa07cbde52cd39b41c11f674ac47fb7c7956e0253e9634dc42&"),
    ("Sciarpa consejero", "https://cdn.discordapp.com/attachments/1186763825005994036/1216914588726067313/image.png?ex=66021f07&is=65efaa07&hm=e6a320255f54636250a4f57de58603cc737ad0229403382e5856af770df501c9&"),
    ("Kiki", "https://media.discordapp.net/attachments/1186763825005994036/1186771137363980469/20231004_085649.png?ex=67463340&is=6744e1c0&hm=8e9df97413f53e4a21271360df09faea29622e62013740206c65c3cd2391ca0a&"),
    ("La traición", "https://media.discordapp.net/attachments/1020776041851129923/1222633480945664130/image.png?ex=67462629&is=6744d4a9&hm=5ece7452701936173cb7b16772afb3a28ceccfb619db384808371adf51a19483&format=webp&quality=lossless&"),
    ("Uh...", "https://media.discordapp.net/attachments/1020776041851129923/1224892845174030386/198_sin_titulo_20240402222636.png?ex=6746755b&is=674523db&hm=d30511276e295b94c23b24a913dbf6946bbb4b503d0490461a85c38ed9820579&format=webp&quality=lossless&"),
    ("Turrón cosas", "https://cdn.discordapp.com/attachments/1186763825005994036/1310797771913035776/image.png?ex=6746870e&is=6745358e&hm=a46b11f7af63962ab61a1bc90af141f5706b67db174a4e98fd069013b2a95210&"),
    ("A 9 personas les gusta esto", "https://media.discordapp.net/attachments/1186763825005994036/1310798283618255011/image.png?ex=67468788&is=67453608&hm=fc294007a8e633ec13c3e39d3152efd0d53fc8a0b54adc66a77239b3327a7db4&=&format=webp&quality=lossless&width=249&height=195"),
    ("Leakearon al Kitt", "https://media.discordapp.net/attachments/1186763825005994036/1310798734577373216/image.png?ex=674687f3&is=67453673&hm=db124955634160ddd02bdddc35684d265d79efb987b29dac366fdefd140d305a&=&format=webp&quality=lossless&width=720&height=544"),
    ("Leakearon a la Turrón", "https://cdn.discordapp.com/attachments/1186763825005994036/1310799290293026816/image.png?ex=67468878&is=674536f8&hm=87c64fa87b0b0de08d353f750c5f4a983241757f67cabd91a7734ff29361c7f1&"),
    ("No me corromperán", "https://cdn.discordapp.com/attachments/1186763825005994036/1310799871921619037/image.png?ex=67468902&is=67453782&hm=56029159dfa678d90202ce0be0d05566b06a3d014c3bd3ea0942e048400291d0&"),
    ("Ya es costumbre", "https://cdn.discordapp.com/attachments/1186763825005994036/1310800391541227621/image.png?ex=6746897e&is=674537fe&hm=806b377ba29cfb476abcbb885c014964c4e5a4b716a4291095551444219a9649&"),
    ("El orden natural del Chis", "https://media.discordapp.net/attachments/1186763825005994036/1310800819565629510/image.png?ex=674689e4&is=67453864&hm=536bda126c97b23fe962d17625f17782a5b3db80d71edc1224d2f7f3aeff9b7b&=&format=webp&quality=lossless&width=499&height=148"),
    ("Demostrado", "https://media.discordapp.net/attachments/1186763825005994036/1310801097937522688/image.png?ex=67468a27&is=674538a7&hm=f5d92c6155c2d488329f848f76160cc370e0b9770b7711226f48b99feccf48c3&=&format=webp&quality=lossless&width=650&height=174"),
    ("Criminal internacional", "https://cdn.discordapp.com/attachments/1186763825005994036/1310801345736998943/image.png?ex=67468a62&is=674538e2&hm=ac2d451be534142c1cd19a27486eb336f5fbd8bf5455db88af6c63596bb7c6c6&"),
    ("Mewlvin", "https://cdn.discordapp.com/attachments/1186763825005994036/1310802008705597501/image.png?ex=67468b00&is=67453980&hm=eb97eaa118be044ea4d1e908e585dc469100a0dd7b1bcb28a72b2031550cb928&"),
    ("Alon brainrot", "https://cdn.discordapp.com/attachments/1186763825005994036/1310802337849282671/image.png?ex=67468b4e&is=674539ce&hm=a83fa50b1a7d96d8c6bc3af601926229fe9dcb31a77b0d8d744813bfba04d9b7&"),
    ("Y guitarra también", "https://cdn.discordapp.com/attachments/1186763825005994036/1310803043188478044/image.png?ex=67468bf7&is=67453a77&hm=66dcdb3746355aedadcd8cd88512a1c4e7febf49e74c0c6be462b3c19dc958d6&"),
    ("Logia potencia mundial", "https://cdn.discordapp.com/attachments/1186763825005994036/1310803936655179807/image.png?ex=67468ccc&is=67453b4c&hm=b33395f53e645008123ae1e91dc135791ce7e0ab909df49b4a90af06aa4c052c&"),
    ("Verdadero macho", "https://cdn.discordapp.com/attachments/1186763825005994036/1310804507432583168/image.png?ex=67468d54&is=67453bd4&hm=1162a2ab75a9872b2cc3e0fd88505b2415b1cddc155499db62eb73cafe8e1245&"),
    ("Por favor", "https://cdn.discordapp.com/attachments/1186763825005994036/1310817898884759702/image.png?ex=674699cc&is=6745484c&hm=5f316aaa6129c24b0cbc3389dc16efcd551da188166c070717f29e7227f359e3&")
    )

answers = (
    "Hay una cosa que se llama Google, demás que sabe",
    "compita no ve que estoy tratando de tomarme mi MelvinCola, vaya a webear a otro lado",
    "jaja sí, oie se me está acabando la batería, hablamos la próxima semana?",
    "loco soy un roboc, que querí que te diga ???",
    "honestamente mimportaunpico :cursedwhyme:",
    "Me gustaría atenderte pero veo que tu carnet está vencido, dirigete al edificio de la SDL https://discord.com/channels/1020776041024864350/1154128025013715085 y vuelve otro día",
    "Me parece que te falta avivarte, date una vuelta por el Centro Mundial de Avivamiento **URGENTE** https://discord.com/channels/1020776041024864350/1172551157344911481",
    "luego de considerar cuidadosa y exhaustivamente tu pregunta, he llegado a la conclusión que ya no quiero seguir trabajando en esto",
    "sigue tus pulmones o algo así, ahora dejame piola que estoy jugando DGS",
    "mmm no, y tampoco fui yo el que quemó esa casa, a mi no me engañan :smiling_imp:",
    "‎",
    "bruh",
    "Después de leer tu pregunta voy a tener que pasarme por https://discord.com/channels/1020776041024864350/1088598726790094879 un rato...",
    "se nota que teni harto tiempo libre oye",
    "Da lo miiismo weon! da lo mismo!",
    "y dale con que las gallinas mean",
    "Te respondería pero no me es interesante pregunta",
    "hazle caso a tu :heart:. digan lo que digan los demás",
    "No sé wn. sólo soy un bot, y no me pagan lo suficiente para hacer estas cosas.",
    "no entendí bien la pregunta, ¿los policias sabían que asuntos internos les tendia una trampa?",
    "Hoy no se responde, mañana sí",
    "Sí, pero no, y a la vez tampoco",
    "No te puedo decir que si, ni que no, si no que todo lo contrario",
    "Te responderé Soon ™️",
    "Como voy a saber aweonao, soy un roboc",
    "Si me dieran sinko peso por cada mensaje estúpido que leo, me harías millonario",
    "Error 404: Interés not found",
    "Sí.",
    "oie y si le vas a preguntar a otra persona mejor",
    "La comunicación es la solución para muchos problemas, practicala... pero con otra persona por favor",
    "No responderé preguntas hasta que mi abogado Oso esté presente"
)

helpme_text = """"Comandos informativos:
- _melvinbot
- _helpme

Comandos recreacionales:
- _callate
- _erronea
- _prontuario
- _fiestaspatrias
- _arson
- _luismi
- _melvin420
- _locologo
- _pirate
- _completo
- _roboc
- _durisimo
- _starboard
- _oiemelvin [pregunta]
- _melvinseal  [MICK EXCLUSIVE]
- _thread
- _bomdia

Comandos moderación:
- _ban [@usuario] [motivo]
- _unban [@usuario/id]
- _kick [@usuario] [motivo]
- _regalonear [@usuario] [motivo]
- _desregalonear [@usuario] [motivo]
- _mimir [@usuario] [tiempo] ((formato: Xs / Xm / Xh / Xd | Ejemplo: 12h | Máx 28 días))
- _despertar [@usuario] [motivo]"""

# Generic GIFs
gif_peineta_garcia = "https://media.tenor.com/nqg6FuHs-wYAAAAC/peineta-annoyed.gif"
gif_trash_out = "https://media.tenor.com/xi2fW90l4TkAAAAd/sml-jeffy.gif"
gif_shh = "https://media.tenor.com/K-f1ILAV-WEAAAAC/themask-silence.gif"
gif_regalonear = "https://tenor.com/view/baby-on-lap-sibling-love-cute-baby-cutu-baby-sleeping-gif-24655360"
gif_afilar = "https://tenor.com/view/spider-man-norman-osborn-knife-sharpening-green-goblin-willem-dafoe-gif-20955065"
gif_sniper_wait = "https://tenor.com/view/sniper-tf2-waiting-piss-gif-27404794"

# Generic Images
im_thread_inquiry = "https://media.discordapp.net/attachments/1179960160828018750/1193317307959750717/7c8.png?ex=65ac4658&is=6599d158&hm=4dfc48264b5bb9ea10fa6d17acdb7426542ca898962a8f9e8da6160325a5d1a9&=&format=webp&quality=lossless&width=277&height=670"
im_pirate = "https://cdn.discordapp.com/attachments/1179960160828018750/1180327977138000023/v51mxsd4nqub1.png?ex=657d0517&is=656a9017&hm=c83e3e920d5032c389f771f1af7b911dfa06803659de3643f7cab4b09cb07d66&"
im_completo = "https://cdn.discordapp.com/attachments/1020780174310121613/1180275900839886879/l7bz4h21a7z71.jpg?ex=657cd497&is=656a5f97&hm=1dde1c331cdccbb69aa371d799fc31c4c211a89a4d4aa4d5f534f98a16948304&"

# Generic Videos
vid_chacarron = "https://youtu.be/y75MGw5pcyc&t=14"
vid_bomdia = "https://youtu.be/PxxtBZZXWGc"

# Logia Images
logiaIM_erronea = "https://cdn.discordapp.com/attachments/1179960160828018750/1186778931861393549/image.png?ex=65947d02&is=65820802&hm=9a09a5a46dc585163ce85013c4f8f91a0a8452cb12b7e0e466d08c2cd9f75122&"
logiaIM_roboc = "https://media.discordapp.net/attachments/1020780174310121613/1180276009237495858/unknown-1444-3.png?ex=657cd4b1&is=656a5fb1&hm=be4d2667985568e5dd967b9b18a88ce8e0e4fef850afe46d5cff01c36824ecd3&=&"
logiaIM_melvinseal = "https://cdn.discordapp.com/attachments/1179960160828018750/1180000612692262962/Melvinseal.png?ex=657bd435&is=65695f35&hm=97cd0bdd6a4224c90499ea2195a5ba88751f529ff2fdb1f6f0da46251b35e11c&"
logiaIM_locologo = "https://cdn.discordapp.com/attachments/1179960160828018750/1179991723087241236/melvinhelp.png?ex=657bcbed&is=656956ed&hm=c549a681fd064271a4ad6a68ad42520b72b6a81428eacb0eec27dc3a72c00dba&"
logiaIM_melvin420 = "https://cdn.discordapp.com/attachments/1179960160828018750/1179990996482805780/mel.png?ex=657bcb40&is=65695640&hm=581a116d063008c40ab5917572a90e9f7e83fe41c1faa0ba7d1bccb119a6bcab&"
logiaIM_luismiguel = "https://cdn.discordapp.com/attachments/1179960160828018750/1179990115414724688/luismi.png?ex=657bca6e&is=6569556e&hm=55e6329acb696e6955c38cbea437247575cbdde6e093c594dc61babb7a188b5c&"
logiaIM_arson = "https://cdn.discordapp.com/attachments/1179960160828018750/1179989546629345391/house.png?ex=657bc9e7&is=656954e7&hm=076b88ecac1cea730ac8663177c67a0bf5ac9d8541d82b09f230d92aa55d0772&"
logiaIM_fiestaspatrias = "https://cdn.discordapp.com/attachments/1179960160828018750/1179987125953888407/image.png?ex=657bc7a5&is=656952a5&hm=66d2407194b73c85435c3496532ae01e8fd4faeae6d3d3479b36b4c6cac7c30d&"

# Logia Videos
logiaVID_prontuario = "https://cdn.discordapp.com/attachments/1020776041851129923/1128503634318069820/InShot_20230711_214832802.mp4?ex=6594bd69&is=65824869&hm=a2bc77674c03c5f95d7f06db8e7c536eda604edb2935ad1435ba577c42e53e4f&"