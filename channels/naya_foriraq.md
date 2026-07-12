<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/LzdhB48oBpMjxN6B4EdYKP32pXm30BffwhVGyWPTkUrddRkDOdP8fJhRnNy6ewifG5UIBn-g4A-V5R9PdewiBbGXxSx1sZLxlLjnhCewKOu_ovA67BvpR3nyzkdPyfYlnS5f9MNVJPA12Nx0TbxKDyCVpMSCtSiqhSGmKiJh7J24Ffj3-sAqgWlSMGdjLtCZI2eb9y7z5Cw-vLbKlwebex5KXt0jTvZvMkf_5aNO8x2mHOjX-X6s6_W4S_Rz2dasWhGd4UyQ1c4TcLuUst-5EpY2sFmI42bzYcw-jdEmGA4D0s_pb85nBo1E4ST4Pgzh_Bg5bliJ-vpe9WHrIFhSww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 260K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 19:01:30</div>
<hr>

<div class="tg-post" id="msg-82539">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9320cd179f.mp4?token=U5JF3Rqw0vkTA85p5exkK2D0Cz3V2op6vVdNVRW55560bAW8njNxRc6xmrv6Ze2Pjo93ExVgGuhCeC8bKL1kFJ8uh50N750Lp8b_kQQQRIL1JOrxNIUDe379q7tWiFI0oAIzazeUxm7VzWr9Njc_3itP9G1SJrvqZAUcJDlgauEiPA1M3ve4qC6nefpK4s2pCzNOp1CR4gT6jeLACWtnsj0J1qT7y7Nm48aEmliZxWJWh9v2D6Q1E84X6fQCgvPwRYMFlpPcHv9TSXyTn3StIyOcAjxwBSqndfG2RHhP_4mL51o1Vyou66K0YoAffPiGNBfSxHuphwv4l39W9XWSAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9320cd179f.mp4?token=U5JF3Rqw0vkTA85p5exkK2D0Cz3V2op6vVdNVRW55560bAW8njNxRc6xmrv6Ze2Pjo93ExVgGuhCeC8bKL1kFJ8uh50N750Lp8b_kQQQRIL1JOrxNIUDe379q7tWiFI0oAIzazeUxm7VzWr9Njc_3itP9G1SJrvqZAUcJDlgauEiPA1M3ve4qC6nefpK4s2pCzNOp1CR4gT6jeLACWtnsj0J1qT7y7Nm48aEmliZxWJWh9v2D6Q1E84X6fQCgvPwRYMFlpPcHv9TSXyTn3StIyOcAjxwBSqndfG2RHhP_4mL51o1Vyou66K0YoAffPiGNBfSxHuphwv4l39W9XWSAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد إستشهاد مواطن عراقي على يد القوات الكويتية..
مظاهرة احتاجية لأبناء محافظة البصرة أمام القنصلية الكويتية.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/naya_foriraq/82539" target="_blank">📅 18:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82538">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2KRJZ8eXY9TkE7aDdTHgwqQuiko2uX2oXq1D2Ero1sy7uhCsSBAZRuvej6qkT0_6E3BIxpepj687aZVcDteaQcSHDZRszoGua67QmLE7IHBDhzrJMsPb2-vwa7lVvoapRVHnxCUpS2gAEWC-g6bRAALPz89f3x3c_tHqkYdjc7pSCzsGb4E5N-UY84a30TUL_VUkYyJjuwZzg7_v1miOtkk2dFNvxRmQkjJbFkw0TIdFiNANGyMtW48BFhwdD08ljQeT7HxuchFSG6NUxCEJorfLGE3fQDqXuEBiNasE9wmB7GqWCSQTXTLbdV-wcwFs0D6XrKI-UlCIYBW23TosA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف مواقع إطلاق صواريخ ATCAM</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/naya_foriraq/82538" target="_blank">📅 18:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82537">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d43920ef29.mp4?token=bItAynIkWEYRJoqstBFa_mh1kFZKggyvHnfdGw8K3YvwjICZ7F5EvRxEr1icvQyGG3y23UG6JsG_AHfq7R8IXQa1_KHq3SufvRMuyZgvz3HZQclVNUqvcrkoQUqTEIdZLyFVp09dxCXKalPw0WQ_403dcZWV0XrFsvexo3_WrXUQYYuu9ycnk3RjjHiRRaxC5MMsUOy1plzO2N0vOJ1YAo3sFMDrRxdi6UHG7fyy5s1aGMMvyTqdknENBR4Wbmkf5BodaMY4dPgV6_Vcy-pg3kFODzbDboVcTNbdeq4bDFCTuadyy5pogE0E-XGmapOjSiAaK9NzDrGdj64y_Sf_pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d43920ef29.mp4?token=bItAynIkWEYRJoqstBFa_mh1kFZKggyvHnfdGw8K3YvwjICZ7F5EvRxEr1icvQyGG3y23UG6JsG_AHfq7R8IXQa1_KHq3SufvRMuyZgvz3HZQclVNUqvcrkoQUqTEIdZLyFVp09dxCXKalPw0WQ_403dcZWV0XrFsvexo3_WrXUQYYuu9ycnk3RjjHiRRaxC5MMsUOy1plzO2N0vOJ1YAo3sFMDrRxdi6UHG7fyy5s1aGMMvyTqdknENBR4Wbmkf5BodaMY4dPgV6_Vcy-pg3kFODzbDboVcTNbdeq4bDFCTuadyy5pogE0E-XGmapOjSiAaK9NzDrGdj64y_Sf_pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/naya_foriraq/82537" target="_blank">📅 18:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82536">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/naya_foriraq/82536" target="_blank">📅 18:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82535">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/naya_foriraq/82535" target="_blank">📅 18:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82534">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">استهداف مواقع إطلاق صواريخ ATCAM</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/naya_foriraq/82534" target="_blank">📅 18:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82533">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/naya_foriraq/82533" target="_blank">📅 18:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82532">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/naya_foriraq/82532" target="_blank">📅 18:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82531">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇱🇧
بيان صادر عن حزب الله تعزية بوفاة أمير دولة قطر السابق:
يتقدم حزب الله بأحر التعازي إلى دولة قطر وأميرها الشيخ تميم بن حمد آل ثاني وحكومتها وشعبها، بوفاة الأمير الشيخ حمد بن خليفة آل ثاني، سائلين المولى عز وجل أن يتغمده بواسع رحمته، وأن يلهم ذويه الصبر والسلوان.
ويستذكر حزب الله الدور البارز الذي اضطلع به الفقيد الراحل في دعم لبنان  والوقوف إلى جانب شعبه في معظم المحطات العصيبة التي مرّ فيها، لا سيما وقوف دولة قطر بقيادته إلى جانب المقاومة خلال العدوان الصهيوني على لبنان عام 2006، ومساهمتها الخيرة والمشهودة في إعادة إعمار القرى والمنازل التي دمرها العدوان. كما نستذكر الزيارة  الفريدة للأمير الراحل للضاحية الجنوبية لبيروت ومدينة بنت جبيل في ذلك الوقت كتأكيد على وفائه ومحبته للشعب اللبناني.
كما يثمن حزب الله مواقف الراحل الداعمة للقضايا العربية والإسلامية، وفي مقدمتها القضية الفلسطينية وحق الشعب الفلسطيني في مقاومة الاحتلال لاستعادة حقوقه وأرضه ومقدساته.</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/naya_foriraq/82531" target="_blank">📅 18:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82530">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f44f93dc1f.mp4?token=SAQ0BlkqoNaQMjb5fO4oYSqx2JM0t5AFwo2xejLBKKJZ15k9Fq1kn8sDdBoqm0wjNllCIVV4G1VkJGoIJuEDJxpLq0lek9jVLqTgr1VNuFL3xAjCOuPDD-RgxZvzL8w7eRzsfLMBH16iQc_rG9MN15B6OxNdAl8Up049Na-u3PlH5jkhUxFW4Ix98uDOowhvB4cPRzuJeU0wCeZzHZ2Hu_gfln-GJetJYfK7QSc1khu4_GqZphCmc3CbmyQsf_ybClzmFidcY6dgH90Qt7biLIW7sglUVKO2L2LBB5OEDF5jD0AzwGVOrGUt5LnJotxUzgprq8xYHGzn7pgaFE3fcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f44f93dc1f.mp4?token=SAQ0BlkqoNaQMjb5fO4oYSqx2JM0t5AFwo2xejLBKKJZ15k9Fq1kn8sDdBoqm0wjNllCIVV4G1VkJGoIJuEDJxpLq0lek9jVLqTgr1VNuFL3xAjCOuPDD-RgxZvzL8w7eRzsfLMBH16iQc_rG9MN15B6OxNdAl8Up049Na-u3PlH5jkhUxFW4Ix98uDOowhvB4cPRzuJeU0wCeZzHZ2Hu_gfln-GJetJYfK7QSc1khu4_GqZphCmc3CbmyQsf_ybClzmFidcY6dgH90Qt7biLIW7sglUVKO2L2LBB5OEDF5jD0AzwGVOrGUt5LnJotxUzgprq8xYHGzn7pgaFE3fcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من الاقمار الصناعية..
تدمير حظيرة طائرات مسبرة في قاعدة الأمير الحسن الجوية الاردنية ولا يزال الدخان ظاهرًا</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/naya_foriraq/82530" target="_blank">📅 18:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82528">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromExplosive Media</strong></div>
<div class="tg-text">🚩
SUDDEN ILLNESS
Lindsey Graham is Dead!
Iran Lego is ready :) Who's next?
#KT
🆔
@explosivemedia</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/82528" target="_blank">📅 17:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82527">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🌟
‏ترامب: مضيق هرمز لا يزال مفتوحاً.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/82527" target="_blank">📅 17:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82526">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7929df771.mp4?token=eG-jHoVDezZI1IiWMoYEdRZ1juZHDjarMVvJbJjhD7-C6_2CzlGyuYbpKEfblaLYi9A9xhnxAkX2qnXIQ5Nfdohs-2_O7GyFdWWDAIeHP3RMu_F1_Dbyd01f8hJ2eY6ZHzFRZ_cwtd2QS42FqMkHVKgZabP2SHa517RWAKcu8EjVsXgd_JlEfaRA1bTxR-nkRwBlV3UardeeMZtwAhEEYUSrH1fo7uW5EQXXk5d7xfiG5VjVSQduayBzqzeDo1BNpOJI_V6y3AbxqC1CpbUMSIsK-6jLGg8vfs5eWIMIaBNGMbIYRImBQU7ruaH8x3XnOLPGpxZH8yh-DePSXhEvZ6mYI1-Ea5UlLZXGerGooJ_XJYk6XmTzfAGuF1rhpdBdCVi-WcT83m8FgfNQwP77StoH5rn8AuQHHqHREa4zj97W4hj2LnDL6mPVZm0dul5udtH2Y_i0AQ5TG3ByU9lpdnSLyU8J7T6ewhkZB7PTjfvOTbEsDB6pnz-HZzZmJQXFyT9Bao_65z3_laoinr-Sv87rIdAvERjNBHQU03sR60wwp6bM5HVJGERERh6BniOhU2NpJZFGKmV0vh7Wa3YJy4TIkNq2-NURG8jr1QPe1fN1cZ5Ra1y4POYAkPNnzRL8rlr6ocheBPgCpFY5vT5C28YRVjYwfuZ2G1m-8ZBdh7o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7929df771.mp4?token=eG-jHoVDezZI1IiWMoYEdRZ1juZHDjarMVvJbJjhD7-C6_2CzlGyuYbpKEfblaLYi9A9xhnxAkX2qnXIQ5Nfdohs-2_O7GyFdWWDAIeHP3RMu_F1_Dbyd01f8hJ2eY6ZHzFRZ_cwtd2QS42FqMkHVKgZabP2SHa517RWAKcu8EjVsXgd_JlEfaRA1bTxR-nkRwBlV3UardeeMZtwAhEEYUSrH1fo7uW5EQXXk5d7xfiG5VjVSQduayBzqzeDo1BNpOJI_V6y3AbxqC1CpbUMSIsK-6jLGg8vfs5eWIMIaBNGMbIYRImBQU7ruaH8x3XnOLPGpxZH8yh-DePSXhEvZ6mYI1-Ea5UlLZXGerGooJ_XJYk6XmTzfAGuF1rhpdBdCVi-WcT83m8FgfNQwP77StoH5rn8AuQHHqHREa4zj97W4hj2LnDL6mPVZm0dul5udtH2Y_i0AQ5TG3ByU9lpdnSLyU8J7T6ewhkZB7PTjfvOTbEsDB6pnz-HZzZmJQXFyT9Bao_65z3_laoinr-Sv87rIdAvERjNBHQU03sR60wwp6bM5HVJGERERh6BniOhU2NpJZFGKmV0vh7Wa3YJy4TIkNq2-NURG8jr1QPe1fN1cZ5Ra1y4POYAkPNnzRL8rlr6ocheBPgCpFY5vT5C28YRVjYwfuZ2G1m-8ZBdh7o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إن نفّذت أمريكا تهديدها، وخاضت معنا مواجهةً من بوابة الخليج، فماذا ستفعلون؟
كان جوابهم واضحًا جدًّا؛ جوابًا يخرج من قلوبٍ بلغت الطمأنينة بذكر الله:
«سيكون الخليج مقبرةً لهم.»
فالشيطان لا يفعل سوى التهديد، ولا يجرؤ إلا حين نخاف منه.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/82526" target="_blank">📅 17:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82525">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">#ترفيهي
🇺🇸
القيادة المركزية الامريكية:
إيران لا تسيطر على مضيق هرمز. فهو لا يزال ممرًا مائيًا دوليًا. والقوات الأمريكية متمركزة ومستعدة للحفاظ على هذا الوضع.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/82525" target="_blank">📅 16:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82524">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🌟
‏
ترامب:
مضيق هرمز لا يزال مفتوحاً.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/82524" target="_blank">📅 16:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82523">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pORMcEP-sTPaay_Os5zwijthinDABEKOVV8qnaUSPTii2DVRC6EFQ3Vrzj_hVrw72QL3T1-OBUckGAMMohxAE6N78UA_YtilqIw4cacr5DIK69_LYIwendns2oWLxYatUpq2FfJey4lNskWO5iIhtYjoxYovxWD4TYjXVoxJiX1J9ccvz5u5J93YSLoXx-qH_dLWoH0aKjj5e0wxCw2zbOgKU0uHseD-5hHBxlRwpXtxoB15KFKt0cNnsmJz0bL11vrXTEFXgVYG9yhV750n0PfVne1Hgd3RwFVODiqHVy7sgeI59cF3TYk1UvFktdZfZqHLyyIK2BOUkChWghzuMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هيئة الاعلام والاتصالات العراقية تقرر منع ظهور زينب جواد لمدة 90 يوم في جميع وسائل الاعلام</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/82523" target="_blank">📅 15:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82522">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دويلة الكويت:
نتعامل مع بقايا الشظايا والمتفجرات في منطقة صبحان وذلك من الساعة 3 مساءاً حتى الساعة 4 من مساء اليوم. أي أصوات انفجارات قد تُسمع خلال هذه الفترة ناتجة عن عملية التخلص من الشظايا والمتفجرات.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/82522" target="_blank">📅 15:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82521">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">الخارجية العمانية تستدعي السفير الايراني لتسليمه مذكرة احتجاج بعد تعرض مواقع بمسندم والوسطى لاستهدافات بمسيرات</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/82521" target="_blank">📅 15:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82520">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
سي إن إن عن بيانات تتبع:
حركة الملاحة عبر مضيق هرمز تراجعت بشكل ملحوظ بعد إعلان إيران إغلاق المضيق.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/82520" target="_blank">📅 15:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82519">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IowVatH3Sq2T3vdJUu0_ZKDQLPKaKcTDWgQmv7FBxAbOrLAH3fr9GrIYAxi0fXX9lUm3D6xTE3tJKvrlDNui-SU94J6KRar56T4hRUu0LvnUQYC-OIAygiJ8ivq3vd4U4ks7wDJENZvH2v7Aabxe74JT6SJ83w7IPmFsZ_a9RWYRpWTpSAhuJc5_FLC75LPMwHcqhyoblOXkGiYQQxKA_MJ4PueQXKQC3G9bXPlWudaQCbzk8o6S94XoAM9Fq5Y00x9jQOIJRN2dmQRZpFtfUEDRLxbuZfeSvlbXRyRnf7LlyqsLgXT5d8MZXYjfDExtfxrqcYTh5l2SLvtymUCKzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
الدفاعات الجوية الايرانية تدمر صاروخ كروز تابع للجيش الامريكي في منطقة "دره" الواقعة بالقرب من مدينة خرم آباد.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/82519" target="_blank">📅 14:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82518">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏الأمن البحري العماني: استجبنا لنداء استغاثة من سفينة تجارية ترفع علم قبرص قبالة مسندم</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/82518" target="_blank">📅 14:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82517">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حدث امني قبالة السواحل العمانية</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/82517" target="_blank">📅 14:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82516">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حدث امني قبالة السواحل العمانية</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/82516" target="_blank">📅 14:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82515">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">المتحدث باسم الحكومة العراقية حيدر العبودي: الحكومة ستعالج نقص الكابينة الوزارية عبر الوفد الذي سيذهب الى الولايات المتحدة
لشوكت يبقى هذا التدخل الايراني</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/82515" target="_blank">📅 13:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82514">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNDPaNVrCOHR1CBFgVXzA08kMFhJkMT4T8MTdabBEsVUmAg-WTOxF9yHXTMB0DMopuJF7YHpyfLWw2B9f2M7-l-XcpEJglsbKM2pS-YPs1ZGKhr-QM4HBFIhI-1OpWv27qNZP0_qcurtI_KpkBjAJYl4EYhp0kOTFSIYw8qgIiabEkKHvYMQrR1ykuD1REKdUcqQEN2d_li3st_mZoUpo67XC6TOOYB0IWPc0dHgZrLIVt5FYE2HWRtdQM3o9xfLCxAUyzadYOMmpFAfRrogLif87aGgVfB6ZZZma5jW85WF7Fa3TF0iO3qMqtJ62LQLSR7MMAiOYgASsyYd_97xYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
وزير النقل العراقي وهب سلمان الحسني يصدر
قرار بسحب يد مدير عام الخطوط الجوية العراقية (مناف عبد المنعم) وتكليف (مصطفى طالب يوسف) بتمشية اعمال الشركة.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/82514" target="_blank">📅 13:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82513">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇶
محكمة
جنايات محافظة نينوى:
الإعدام بحق إرهابي حوّل ورشته لمخزن متفجرات ونفذ اغتيالات في الموصل. الإرهابي اشترك مع مجموعته في استهداف القوات الأمنية والأرتال العسكرية ونفذ عمليات اغتيال طالت عدداً من الضباط والمنتسبين وقام بتفجير سيارة مفخخة في منطقة حي التأميم بالجانب الأيسر، أسفر عن استشهاد أربعة مواطنين وإصابة آخرين عام 2021 وشارك في الهجوم على مدينة الموصل، واقتحام سجن بادوش وإطلاق سراح السجناء، وقتل عدد كبير من النزلاء</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/82513" target="_blank">📅 13:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82512">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">في خبر غير مهم
🇮🇶
وزارة الخارجية العراقية تعرب عن قلقها إزاء استمرار التوترات التي تمس أمن الملاحة البحرية بالمنطقة وتؤكد ضرورة احترام سيادة الدول وعدم التعرض لأمنها.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/82512" target="_blank">📅 13:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82511">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇬🇧
‏هيئة بحرية بريطانية: التهديد الأمني في هرمز شديد للغاية</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/82511" target="_blank">📅 11:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82510">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خميس الخنجر يعزي برحيل امير قطر
والحزن يعم مجمع روكسوس وسط بغداد و أجزاء من حي الاميرات و قناة UTV تفكر بنشر مقاطع لطمية الوداع الوداع عذب قلبي الوداع</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/82510" target="_blank">📅 11:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82509">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔻
تمديد حالة الطوارئ في جميع أنحاء الكيان المحتل بموافقة الحكومة عبر الهاتف حتى 28 يوليو.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/82509" target="_blank">📅 11:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82508">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامب: رحل السيناتور ليندسي غراهام، أحد أعظم الشخصيات والسيناتورات الذين عرفتهم في حياتي! كان دائمًا يعمل، وكان وطنيًا أمريكيًا حقيقيًا. سنفتقد ليندسي كثيرًا! سيتم الإعلان عن التفاصيل والترتيبات لاحقًا. يا له من خبر محزن!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/82508" target="_blank">📅 11:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82507">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5bAaRI9-FA2H1203497E3kG8hf9IlNkKR3fH53xCYFFQi3Kqt6YPJg2y_HP2b4gF-9ATQVN7_TIFWwIk-FtM49XPcJLq1TOWdHeERb-0eH0xt2S8U78W_gBOOhTJuX-E3TC88cEmR6YOi0GSHkA5NL0UjG49cJszGBok8cigEo-RF0aAWwVUmC41ZYRE27rf8HXqeFTuB-_K3xs-kCihEsMH3jem53APFgV7YmXlEubv7GeY_z21IArCa4jE81Vl2SsrsD1HJ9juXpPK42WtX1-KBmMFR_eutMPWubH54kSvdHIFJSK4w17ZNObxgGyoriDgOsvdYoaTvqRxj_Suw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: رحل السيناتور ليندسي غراهام، أحد أعظم الشخصيات والسيناتورات الذين عرفتهم في حياتي! كان دائمًا يعمل، وكان وطنيًا أمريكيًا حقيقيًا. سنفتقد ليندسي كثيرًا! سيتم الإعلان عن التفاصيل والترتيبات لاحقًا. يا له من خبر محزن!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/82507" target="_blank">📅 10:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82506">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انفجارات تهز البحرين من جديد</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/82506" target="_blank">📅 10:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82505">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a42f3b66c.mp4?token=OaE4O2wIHefe-VbXChIUezFrwFSoLZQzwhMcR8xoInUmqcKHYF7MPzMoerFLItjHb06K23_tnV41zRfJ-Ts_W5J02QNOw83mT3BNBcoj3Y6-HAZAvM1DUMpCVshhWV4o4cIOPUYhBxONDcj9Z_Z8ukVn4ZaEi4cj6pFG9ey0_RArmOI1d3OwT1TWKmO10nm3z8wqWQlobIH8tDNlVzgD9YADZRITX6IzDgxmX8zGYN82oZh9eWteJl3NgeVaZO1V7EbgXCfI0m8Lfe0dw7lONOb5ZeMIs26cXiYlVwoNcY5T0HfpD_4dEibTMBGB0e4AnQC4NHnMaMMhwzBrlrZTaJe-IVnZ4kj8KEyrY2T8znceC3MYFBPClDNOQe-1qQ13aFP9TY_O7FUtDL9NL5_fUGPYpl3FZjraZLKmsmL7QuJBQoZi5Qu1c_9HNjPRPXexM2Nb6xUtiOA-TiXba7P65oBrSEgHa5ZFWn1PONTcS44Qy4CDmo8NnMZDZPp2EPKa2kypsGdZvhn5edk5oY6sO7f1U2rCxLDXDQfkvY8hsJ7umw7sQ0bMnD_sTpvj81vVr8MMkRVrWNd-NEt03tj42uJeqfyRa_oCBonuRFLVy4v_3ztZlW4q3Ee4fuQMYyW92O7OCBbZiJbQqVjXTSb5nCel_-H5yg0N4f41S3AaGiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a42f3b66c.mp4?token=OaE4O2wIHefe-VbXChIUezFrwFSoLZQzwhMcR8xoInUmqcKHYF7MPzMoerFLItjHb06K23_tnV41zRfJ-Ts_W5J02QNOw83mT3BNBcoj3Y6-HAZAvM1DUMpCVshhWV4o4cIOPUYhBxONDcj9Z_Z8ukVn4ZaEi4cj6pFG9ey0_RArmOI1d3OwT1TWKmO10nm3z8wqWQlobIH8tDNlVzgD9YADZRITX6IzDgxmX8zGYN82oZh9eWteJl3NgeVaZO1V7EbgXCfI0m8Lfe0dw7lONOb5ZeMIs26cXiYlVwoNcY5T0HfpD_4dEibTMBGB0e4AnQC4NHnMaMMhwzBrlrZTaJe-IVnZ4kj8KEyrY2T8znceC3MYFBPClDNOQe-1qQ13aFP9TY_O7FUtDL9NL5_fUGPYpl3FZjraZLKmsmL7QuJBQoZi5Qu1c_9HNjPRPXexM2Nb6xUtiOA-TiXba7P65oBrSEgHa5ZFWn1PONTcS44Qy4CDmo8NnMZDZPp2EPKa2kypsGdZvhn5edk5oY6sO7f1U2rCxLDXDQfkvY8hsJ7umw7sQ0bMnD_sTpvj81vVr8MMkRVrWNd-NEt03tj42uJeqfyRa_oCBonuRFLVy4v_3ztZlW4q3Ee4fuQMYyW92O7OCBbZiJbQqVjXTSb5nCel_-H5yg0N4f41S3AaGiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور لمهاجمات اليوم التي نفذتها القوة الجوية الفضائية التابعة لحرس الثورة الإيرانية، ردًا على العدوان الذي ارتكبته القوات الأمريكية الإرهابية في هذه الهجمات، تم استخدام صواريخ باليستية ذات الوقود الصلب والسائل، بالإضافة إلى صواريخ "قدر"، و"عماد"، و"خيبر شكن"، و"فاتح 110"، و"ذوالفقار". حيث دمّرنا مستودع طائرات MQ-9 الأمريكية المسيّرة في الأردن</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/82505" target="_blank">📅 10:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82504">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔻
سكان المنطقة الوسطى في الكيان الصهيوني تلقوا تحذيراً من إطلاق صواريخ والسلطات تحقق مما إذا كان خطأ فني.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/82504" target="_blank">📅 10:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82503">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔻
سكان المنطقة الوسطى في الكيان الصهيوني تلقوا تحذيراً من إطلاق صواريخ والسلطات تحقق مما إذا كان خطأ فني.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/82503" target="_blank">📅 10:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82502">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">انفجار في الكويت منطقة الميناء</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/82502" target="_blank">📅 10:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82501">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انفجارات تهز البحرين من جديد</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/82501" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82499">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/82499" target="_blank">📅 10:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82498">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇺🇸
🇺🇦
تواجد السيناتور غراهام مؤخرًا في أوكرانيا وكان يدعو لاغتيال بوتين وتدمير غزة وحزب الله و إيران</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/82498" target="_blank">📅 09:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82497">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">الأردن: تعرضنا لهجوم صاروخي وسقط 3 صواريخ داخل البلاد</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/82497" target="_blank">📅 09:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82496">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGT576PvDFXYEOisOKoRGFqa_KTThixkbG6-2MyZxjcGHq_BZBVi-cfoiPt-nbVot-nZLoab4DjbCqzcS82FWg_bX_-sqNXQcswR60u-x29SbLkbg8mvHm5RGiKxN7HgRDpc9N0MwyDyimQcNcXT6IbMcayMUp9udJaCFdf1DxkooTE0yWo2L-9kKNn68CkM3JDKUBgqRsd_1z6FmejjbUwU4QdeKfj-rqWZ7CSkwlrVCV2-Jg0C75Bu65uTflIh1L9ikPhNumzxDfmqv3HA4sii5ewszScSFVcerz4qtWpnl0Y8L5M-V_-o1Jxj8Z4w7T0JNDQwemy8aLT51TeAPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
أعلام العدو عن هلاك السيناتور الغراهام : أحد أبرز الداعمين لإسرائيل في مبنى الكابيتول قد رحل عن عالمنا.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/82496" target="_blank">📅 09:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82495">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏سلطنة عمان: تعرض محافظة مسندم لهجوم بالمسيرات</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/82495" target="_blank">📅 09:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82494">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJAJazRBAI2_RL-L-Gm4DR_XrhBxPXZ2G6TuEnOfCm2qU55iO56IeiCrjjl1WHC2RGTWUCQ7fZo0lOQGzIynPeP6ADDROgVaRRdLlVP023PACn27SAIdqZHhNh3WqeReal0HICeUoh6JkVW3r4A0hiBvAaqelwW70lxqcV8Wt4kl1FEaWMOC4Qet1w1-qjsN-GIC9MPHnj9Xg2ddyKdjW7MJf4ySOOJdCwocs3NqqTww4-hg6UOhJwyM643iHaYerO3iF2_y-qSLyzQn8qJEza05acArUC02uaHLnU3IBgompEDnqXQF8MNexT5LlS5qw0X7Br0wl5twPXw3RIaNbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
أعلام العدو عن هلاك السيناتور الغراهام : أحد أبرز الداعمين لإسرائيل في مبنى الكابيتول قد رحل عن عالمنا.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/82494" target="_blank">📅 09:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82493">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">قطر تعلن إصابة 3 جراء الصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/82493" target="_blank">📅 09:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82492">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔻
🔻
الحرس الثوري ينشر مشاهد لهجمات اليوم على القواعد الأمريكية في غرب اسيا</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/82492" target="_blank">📅 08:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82491">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6297da3bb.mp4?token=ROK4YzNBtlxHXHE2KYDNU_Nr_ANNLPsUU6dYqV0k4fQihpMskdL1jDRjT4Up8WBKB5E1uXWNy-viXEjDlvbHcsSX_Umb86TXctI3eYqNycJMcDXkbIdYsXjKl2OdK2d55Xu4ZFHV14sqXWmmUjaqb8Sm1a2b8M1tDJLFFc7-kgBPEMLHO8tfH1W_qovCwgYTLpYvs32EFwa20T5Ccer1Cbdu2fJ2OrQ2CHnq3pBxJ1iWxZ0AUbGr8FpPpbWc7WcP7A6i75-I-miPE5tjzOS48XR9HCfufCkPVE11GIaV54kvj6wNC03IfNVjT0WvaBt1Sim6Okax8uSxsGdG_2EiwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6297da3bb.mp4?token=ROK4YzNBtlxHXHE2KYDNU_Nr_ANNLPsUU6dYqV0k4fQihpMskdL1jDRjT4Up8WBKB5E1uXWNy-viXEjDlvbHcsSX_Umb86TXctI3eYqNycJMcDXkbIdYsXjKl2OdK2d55Xu4ZFHV14sqXWmmUjaqb8Sm1a2b8M1tDJLFFc7-kgBPEMLHO8tfH1W_qovCwgYTLpYvs32EFwa20T5Ccer1Cbdu2fJ2OrQ2CHnq3pBxJ1iWxZ0AUbGr8FpPpbWc7WcP7A6i75-I-miPE5tjzOS48XR9HCfufCkPVE11GIaV54kvj6wNC03IfNVjT0WvaBt1Sim6Okax8uSxsGdG_2EiwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏الديوان القطري يعلن وفاة الأمير السابق الشيخ حمد بن خليفة آل ثاني</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/82491" target="_blank">📅 08:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82490">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔻
🇧🇭
قاعدة الأسطول الخامس تحترق في البحرين</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/82490" target="_blank">📅 08:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82489">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/82489" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">واحد معطب السرفة و واحد معطب الهمر
#شاركها</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/82489" target="_blank">📅 08:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82488">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f54687295a.mp4?token=FPvczQpC9jA3pUYms3c2r9wcAzfEJJ-ANcZxfXtMETTW-UQIm_8AMOOpo2wuR78EWp2FYLKGiyWr4DgbRRad2O5JX-zoYdeBeqfv7HXmiI2Io35zNu-1UfIngz4TjEgZ9P49q4KPk3lryUIWxtEGY9EYIm7MAZRnAsKi9qyd37C862-pZtiikyBOa3AziigER7KCMJO3PG79BmlmZklxwk9nHIBjlhvquS1OyJE4Obtop2a89j0w7z0adwSHsMVY4PkhtXIGxo4S7XK8OnT-ZKk9J5otOSpC8vDOSN71_oaeTAu7Hx8HQRyBYlj34lzMtY5ktq8-hquB6O-ajtH8_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f54687295a.mp4?token=FPvczQpC9jA3pUYms3c2r9wcAzfEJJ-ANcZxfXtMETTW-UQIm_8AMOOpo2wuR78EWp2FYLKGiyWr4DgbRRad2O5JX-zoYdeBeqfv7HXmiI2Io35zNu-1UfIngz4TjEgZ9P49q4KPk3lryUIWxtEGY9EYIm7MAZRnAsKi9qyd37C862-pZtiikyBOa3AziigER7KCMJO3PG79BmlmZklxwk9nHIBjlhvquS1OyJE4Obtop2a89j0w7z0adwSHsMVY4PkhtXIGxo4S7XK8OnT-ZKk9J5otOSpC8vDOSN71_oaeTAu7Hx8HQRyBYlj34lzMtY5ktq8-hquB6O-ajtH8_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🇧🇭
قاعدة الأسطول الخامس تحترق في البحرين</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/82488" target="_blank">📅 08:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82487">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏الديوان القطري يعلن وفاة الأمير السابق الشيخ حمد بن خليفة آل ثاني</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/82487" target="_blank">📅 08:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82486">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">المساعد الأمني لمحافظ لرستان الإيرانية: تعرض مدينة ويسيان لقصف من جانب العدو مرتين دون وقوع خسائر بشرية</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/82486" target="_blank">📅 08:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82485">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رشقة صاروخية  باتجاه قاعدة الجفير في المنامة</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/82485" target="_blank">📅 08:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82484">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انفجارات تهز البحرين الآن</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/82484" target="_blank">📅 08:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82483">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">انفجارات تهز على السالم ومنطقة الميناء</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/82483" target="_blank">📅 08:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82482">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/82482" target="_blank">📅 08:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82481">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">الكويت: نتعرض لهجوم جوي</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/82481" target="_blank">📅 08:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82480">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">الخارجية القطرية ندين الاعتداء الإيراني على الاردن  #مبلاش افتكر انا قلتلك مبلاش</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/82480" target="_blank">📅 08:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82479">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219677a09b.mp4?token=dNrqhrDpkyjcfUg_sdXJvfVwnlYusNzJZiKUOPGMnN6ayhc1Rwb-ovhjOzGgqY8JUmUVFBSIRnZ7UHsRot8KMTdBpwTZvGqNRY7cO_6u-b5DSSY62P9AEl9foTJUCnmNKC4s-AURBTSLdUEIvbFSDWpuWRd9M_1IqAK3ctflHnBM25ODDVihasicsxZb7-pr9Zv2kTgF_0X3BbgZAs_cYmobGCmHFb5aqIMwla36UIp3ocBhXBNVL6LZnR-aMzW8prDZzUcqbVa26ape0Yq6AWHjqec9excjn464gLPkiu9eFU3_GnoC5RhrJMS9n0c-PZMsTgfKIY9G1VX4Bjfeag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219677a09b.mp4?token=dNrqhrDpkyjcfUg_sdXJvfVwnlYusNzJZiKUOPGMnN6ayhc1Rwb-ovhjOzGgqY8JUmUVFBSIRnZ7UHsRot8KMTdBpwTZvGqNRY7cO_6u-b5DSSY62P9AEl9foTJUCnmNKC4s-AURBTSLdUEIvbFSDWpuWRd9M_1IqAK3ctflHnBM25ODDVihasicsxZb7-pr9Zv2kTgF_0X3BbgZAs_cYmobGCmHFb5aqIMwla36UIp3ocBhXBNVL6LZnR-aMzW8prDZzUcqbVa26ape0Yq6AWHjqec9excjn464gLPkiu9eFU3_GnoC5RhrJMS9n0c-PZMsTgfKIY9G1VX4Bjfeag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم جديد يدك البحرين</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/82479" target="_blank">📅 08:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82478">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a5922aca.mp4?token=T1qDRqkmdZJ-hmUELaSzu4ZzaEKuSBLCSPK2buAiQZVQ6ErO2dDQVgsg1T6OHj6x2JnHio8yZJ7fRQql47p6qbO8w1b84bUFadMKJoDHHo-AE1pqyzTgtGZLwfu7boZqSMuGUcyApFvSNgJtedriuMPVfCU_52__kL1O37fos2cIOwoHaLcQKhZIulntj02jRPhj8vRIvMBnlOPQ0fMmh4bTEpF6mZGt92AVj0D91P8OKRh2AnYwjqdNqJf_YdFWds2MvEu9AA2D4cGN7MGIvbEze-CbsccKVKOojQNOQy5wXKapR_lCY4k9-NI9Admccb3hoal9P0ZJ2Iq3_0LMVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a5922aca.mp4?token=T1qDRqkmdZJ-hmUELaSzu4ZzaEKuSBLCSPK2buAiQZVQ6ErO2dDQVgsg1T6OHj6x2JnHio8yZJ7fRQql47p6qbO8w1b84bUFadMKJoDHHo-AE1pqyzTgtGZLwfu7boZqSMuGUcyApFvSNgJtedriuMPVfCU_52__kL1O37fos2cIOwoHaLcQKhZIulntj02jRPhj8vRIvMBnlOPQ0fMmh4bTEpF6mZGt92AVj0D91P8OKRh2AnYwjqdNqJf_YdFWds2MvEu9AA2D4cGN7MGIvbEze-CbsccKVKOojQNOQy5wXKapR_lCY4k9-NI9Admccb3hoal9P0ZJ2Iq3_0LMVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هجوم جديد يدك البحرين</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/82478" target="_blank">📅 08:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82477">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">هجوم جديد يدك البحرين</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/82477" target="_blank">📅 08:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82476">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
التدخلات الأمريكية لفتح ممر غير قانوني في مضيق هرمز تسببت في انعدام الأمن.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/82476" target="_blank">📅 08:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82475">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvbKOb711V9JbVyaQKPl48r7O0bxmEwJJPWABMGP8QjCKmEfwo2pknUpjxxWx5NE39Ru2WUHJ40sBHpEvM64mkQnGFgW5HMl9sELhcrN7cGdH59CBKRGoKScVVlgiCEZsENfkMz4OjKC_zS9Nzl6Tk2J0KkJ4cs8ZIX71CT6CE8P4QPRWrtnLpYa8x477tKxMLOeyo9oBxWvaa7yhWEj8gWdbC_3WPjlYH33gPnoEc70smw3ir7IFcXNt3Klavpef6fjzMk8a3J7IKcOiG1jIi1mzydYwukd5Stlbru88rNQo0V5NToedPDbY7tzm3WBVL8JgR4ZwOGZL4eE8G--uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقر قيادة الاسطول الخامس الأمريكي في البحرين يحترق بالصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/82475" target="_blank">📅 08:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82474">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rw6Jx_8mJ1ubd7qQBu2GAslyrmUqETqeMKWGNpNxbLvinhsCzIpFZhdp6jKkanmdLLwelRIxbGug8pIQPGwlyMSGhRdQjXEe_0MoMhu1ODE46AMlkyQO8XOHh0xP33DKVABcQLnr-aw8HJwydPr-2p1W0EZFnnAPBMSqJL-CRT14M8R-KDWLYrB6tS56FmwtUfnqXX-LH1olTPKDdiOIqMTK8lbgsbD81S1w6i1wZE3p4G9JubJ6LWi7n60Z93HOrpDuJB0ejA5ADxZg_agRofiTcFUzYytZleDfQ_meJmNBjPlimWZqopIYEssM7WLGe_EDgAFYuOO8e-5rzC1zNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
انتهى عهد الصفقات أحادية الجانب. لقد قلنا لكم: التزموا بكلمتكم أو ادفعوا الثمن. الواقع يطرق الأبواب.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/82474" target="_blank">📅 07:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82473">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">هجمات مستمرة على الدوحة القطرية وصافرات الانذار تدوي</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/82473" target="_blank">📅 07:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82472">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=I3zNk6GR6MvxeU7X3YMinJLPl7rvMr4KZP-hduiAmwRnOCgyBVCQswWCzcZPSJ4AA5-qQd1nf_IA3y14P2nnla_xEom-vjY7FSzasHOK5tEgmYd_0dUOI-P_j5eSYYP6wHIh83WG0CVyAINgWBTnk2bwnXJlLBSIsRcBe9GjL66kGJYWCfJ-xgPLiPUWSmxAydRm4ukNZsCwMMwOBqE00g2yRIVNxoRp5R5nxOe2eKp-1TNCsejM4G2WkO-y9ykC2_tGjmQdAq8IuN69a5aUghBhuIz4I8ha_blVmrzYrF0frp8PNCu6UeOeid-QVBBhMQ-v-XPu_FNXQKML818_eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=I3zNk6GR6MvxeU7X3YMinJLPl7rvMr4KZP-hduiAmwRnOCgyBVCQswWCzcZPSJ4AA5-qQd1nf_IA3y14P2nnla_xEom-vjY7FSzasHOK5tEgmYd_0dUOI-P_j5eSYYP6wHIh83WG0CVyAINgWBTnk2bwnXJlLBSIsRcBe9GjL66kGJYWCfJ-xgPLiPUWSmxAydRm4ukNZsCwMMwOBqE00g2yRIVNxoRp5R5nxOe2eKp-1TNCsejM4G2WkO-y9ykC2_tGjmQdAq8IuN69a5aUghBhuIz4I8ha_blVmrzYrF0frp8PNCu6UeOeid-QVBBhMQ-v-XPu_FNXQKML818_eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة تهز الدوحة</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/82472" target="_blank">📅 07:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82471">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">امشب پایگاه‌های دشمن در منطقه شخم زده خواهند شد</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/82471" target="_blank">📅 07:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82470">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">هجمات جديدة تدك الدوحة القطرية</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/82470" target="_blank">📅 07:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82469">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">هجمات جديدة تدك الدوحة القطرية</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/82469" target="_blank">📅 07:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82468">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/82468" target="_blank">📅 07:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82467">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
تم تدمير المراكز اللوجستية التي تدعم السفن ومنصات تزويد السفن بالوقود التابعة للولايات المتحدة في ميناء الدقم في سلطنة عمان، وذلك في هجوم عنيف ومفاجئ.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/82467" target="_blank">📅 07:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82465">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=esQ6lXwVUVw6osQz8B2Gnr1APTkWq9Glv5vTW-T30ZUX_9Y3zGv_NOPdNZWk3S5aHVTgKh5jun7pWtPtCmfXGqi6GOB2OoQ0cITyuxSbtMghhULpaSVApig74eWSrA1ZK7W1PK7lO12QGOeek-5IKjGJO_yiZHsr06pHWvq2ZpANoS1pWOJKPIXQq-BOlkO3i7YXzC5otd1-5H2EcVku18T9d1f-J-L8TuLbdG0AictMizyC9YqwZjFkB6a7h4NgF0zokzv3QshcLCDsIMFTQc8cbBYu5C9Z_QzcIYYgVbrnuWHewN2zdy_2Q69oR8wyFtB4kYk5cZxNBkfgD87r3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=esQ6lXwVUVw6osQz8B2Gnr1APTkWq9Glv5vTW-T30ZUX_9Y3zGv_NOPdNZWk3S5aHVTgKh5jun7pWtPtCmfXGqi6GOB2OoQ0cITyuxSbtMghhULpaSVApig74eWSrA1ZK7W1PK7lO12QGOeek-5IKjGJO_yiZHsr06pHWvq2ZpANoS1pWOJKPIXQq-BOlkO3i7YXzC5otd1-5H2EcVku18T9d1f-J-L8TuLbdG0AictMizyC9YqwZjFkB6a7h4NgF0zokzv3QshcLCDsIMFTQc8cbBYu5C9Z_QzcIYYgVbrnuWHewN2zdy_2Q69oR8wyFtB4kYk5cZxNBkfgD87r3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة تهز الدوحة القطرية وسط إطلاق منظومة الباتريوت الامريكية صواريخها لصد واعتراض الهجوم الإيراني</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/82465" target="_blank">📅 07:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82464">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دوي انفجارات وصافرات الانذار في قطر</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/82464" target="_blank">📅 07:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82463">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مسؤولين إسرائيليين: استعدادات عسكرية إذا شملت المواجهة إسرائيل</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/82463" target="_blank">📅 07:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82462">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrEQsJy3f5B-URFueKdym3BUAdNK1PS_Kp9G3_QV02n63lYHQKWwYxJ0gv0ojJKF1c3asHlz1WS8qHXgLY8weFCCjFVerfXHmUTjZmwj19q8noim15mkx_feNFhWSFaE1WKY4mMMcZX0g3BwIbeRecR0v7XuM4t_h6JaMoIKa-nqNlSATdRZ-3hgSfmugoEyHCopF1qmTUtkWg1DH7TCklnJzfGUBe-BGj-oP9PWdY1udpt_hzjd5yxVDzOWnDbego0z8ebff2a3XOt7w7kvlxrHR1m8hC-1AOGgEWUVBSGrG2PeCbDmLJwVrtn1sVDSHObBHPFSInbSBrx0Ydbr8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاق صواريخ نحو البوارج الامريكية في الخليج الفارسي وبحر عمان.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/82462" target="_blank">📅 07:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82461">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اطلاق صواريخ نحو البوارج الامريكية في الخليج الفارسي وبحر عمان.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/82461" target="_blank">📅 07:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82460">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇷
الإعلام الإيراني: أنباء عن إطلاق نيران تحذيرية تجاه سفينة ثانية حاولت العبور من مضيق هرمز.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/82460" target="_blank">📅 07:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82459">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/265d875f3a.mp4?token=paYnrj6zAC0_l9dFvzsOHNw1yotY-KS5lbJjvWAA0jp86fqIMNKcIVoSB2Uqu6TD57p_I8Hf1IekcTXgzfgCTtxqLATY3u6dHkHWyc2U0KBNQ-BpXkkfIDDMj0jajFbl40nU6sfnyxPBF1opWu3hRbmFVIKqx1Na58B8B7dca7OKT6VsbchMeaB5CRvOE6nJudLktdlvHl-EiKF4PRvKyMZBZnH8WY8kPrd3yQTzhiDQrOlvXdDZ2C00ybK8MsiQDGi5EI2BxRwIK5ht40pEYO14zcFFN94mwSJgGTRNiKWWlQl_pYl2_Zrzgz6TvUGLr9MdZoqs7ClAsYqlR4A482h1h_xyDMTDEUpWnR0nIzztd_Kmpze9wtI3NfLi92qOMFerYSjbVwA6k28tqVyUfsl31_SK8TFixLsfdmEmwYp2jXyh8iMmWUbMl92sGW5wjIhf42RikrA-hnPALk8PP3kNbU0YYwIFae77jNEOLGIGfMzUsHpzA6TeZbpAY-FG8ZStdwyeqCJs6ubbg97Ev8RPMKrvoz3zo-W9f4uB6GsuGebrpHH9HVGNQ7mogf8S37PiwcA6RyEdci2nGqL1tmDpwMyd_QkcXkfDMbFoU_SnRjSMXUgfDgbYKYe5oiH9V9gNfBB6m4nU7nMPA3mJs-0YQQFRphAdLxmdC1Cso1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/265d875f3a.mp4?token=paYnrj6zAC0_l9dFvzsOHNw1yotY-KS5lbJjvWAA0jp86fqIMNKcIVoSB2Uqu6TD57p_I8Hf1IekcTXgzfgCTtxqLATY3u6dHkHWyc2U0KBNQ-BpXkkfIDDMj0jajFbl40nU6sfnyxPBF1opWu3hRbmFVIKqx1Na58B8B7dca7OKT6VsbchMeaB5CRvOE6nJudLktdlvHl-EiKF4PRvKyMZBZnH8WY8kPrd3yQTzhiDQrOlvXdDZ2C00ybK8MsiQDGi5EI2BxRwIK5ht40pEYO14zcFFN94mwSJgGTRNiKWWlQl_pYl2_Zrzgz6TvUGLr9MdZoqs7ClAsYqlR4A482h1h_xyDMTDEUpWnR0nIzztd_Kmpze9wtI3NfLi92qOMFerYSjbVwA6k28tqVyUfsl31_SK8TFixLsfdmEmwYp2jXyh8iMmWUbMl92sGW5wjIhf42RikrA-hnPALk8PP3kNbU0YYwIFae77jNEOLGIGfMzUsHpzA6TeZbpAY-FG8ZStdwyeqCJs6ubbg97Ev8RPMKrvoz3zo-W9f4uB6GsuGebrpHH9HVGNQ7mogf8S37PiwcA6RyEdci2nGqL1tmDpwMyd_QkcXkfDMbFoU_SnRjSMXUgfDgbYKYe5oiH9V9gNfBB6m4nU7nMPA3mJs-0YQQFRphAdLxmdC1Cso1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
الجيش الأمريكي:
أكملت القيادة المركزية الأمريكية (CENTCOM) هذا الأسبوع جولة ثالثة من الضربات ضد إيران (في 11 يوليو)، محملةً القوات الإيرانية المسؤولية عن مهاجمة سفينة تجارية أخرى في مضيق هرمز. استهدفت القوات الأمريكية ما يقرب من 140 هدفاً عسكرياً إيرانياً باستخدام ذخائر دقيقة أطلقتها طائرات مقاتلة (تُشغَّل من البر والبحر) وطائرات مسيّرة وسفن بحرية. وشملت الأهداف مواقع للصواريخ والطائرات المسيّرة الإيرانية، وقدرات بحرية، ومنشآت لتخزين الذخيرة، وشبكات اتصالات، ومواقع للمراقبة الساحلية. وعلى مدار ثلاث ليالٍ من الضربات هذا الأسبوع، استهدفت القيادة المركزية الأمريكية أكثر من 300 هدف - بتوجيه من القائد العام - وذلك بهدف تقويض قدرة إيران على مهاجمة البحارة المدنيين والسفن التجارية التي تعبر المضيق بحرية؛ علماً بأن حركة عبور السفن التجارية عبر هذا الممر البحري الدولي الحيوي لا تزال مستمرة. ومنذ أوائل شهر مايو، ساعدت القوات الأمريكية في تأمين العبور الناجح لأكثر من 800 سفينة تجارية و400 مليون برميل من النفط الخام عبر مضيق هرمز.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/82459" target="_blank">📅 07:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82458">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eecd065d0a.mp4?token=TqgbAXSWTfd8pGB9PVRbScopAa1rS6ts38reJ57K_PILwmNB11_GDVJavysaxP90ET_Wx8smPZ1tfP6zef-o341OH0gKV9Mu8ExCZ4--9FRROaZ1aPgNAZpJkqRgvjAmmXPSw1jVtBCguXizqGqi3iicYDRqqPiGpSuHklZOe3-gZxyZY9vJ24B0gBJGk3M29dY-XxwtVTYkp1sso17RXqbkU6-z3nI9HK4eYQ4U1QqaPPp2wzxkUZLRw_neLXgPVWqwWsrWevNy43xXa0mg6uj2MhtTw06NGTVB9Kgl5V1YKOUfiH6cO0oOeIZjXnuyKqpOJ_HNcsb-ChtNDlfBh5293Dw0U4JGIaLotJ6qEQ09tPoZ5ACGz7aPCN2IaSd0PcPz3usMg7yyhorBKZLWfOgNT2reNYxVLujdfAQw9p4OIcvGatYQoazyl0YhYmqCLYrsCv4iUYfFuM9KR7sOyHKWgZRd0gvP1LG58AH7ELMrAQBHm_YqxpxOB1GNqgMuRwFEh-jzFLxFglU-hhsYPQvGKLWK63eZSThAY5M9HeLP38aiGHTD8YxJ4f3_zuXOmPKeTr65qiUAZlC5uHDAvw0eat_FOevbcMYcJlPxuTWJoJbZ2Dl3AEBx46dedw5moGztGAyGfNkHlWcsNq8NyJKLCkBDexJr_VQNoHXP8Ys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eecd065d0a.mp4?token=TqgbAXSWTfd8pGB9PVRbScopAa1rS6ts38reJ57K_PILwmNB11_GDVJavysaxP90ET_Wx8smPZ1tfP6zef-o341OH0gKV9Mu8ExCZ4--9FRROaZ1aPgNAZpJkqRgvjAmmXPSw1jVtBCguXizqGqi3iicYDRqqPiGpSuHklZOe3-gZxyZY9vJ24B0gBJGk3M29dY-XxwtVTYkp1sso17RXqbkU6-z3nI9HK4eYQ4U1QqaPPp2wzxkUZLRw_neLXgPVWqwWsrWevNy43xXa0mg6uj2MhtTw06NGTVB9Kgl5V1YKOUfiH6cO0oOeIZjXnuyKqpOJ_HNcsb-ChtNDlfBh5293Dw0U4JGIaLotJ6qEQ09tPoZ5ACGz7aPCN2IaSd0PcPz3usMg7yyhorBKZLWfOgNT2reNYxVLujdfAQw9p4OIcvGatYQoazyl0YhYmqCLYrsCv4iUYfFuM9KR7sOyHKWgZRd0gvP1LG58AH7ELMrAQBHm_YqxpxOB1GNqgMuRwFEh-jzFLxFglU-hhsYPQvGKLWK63eZSThAY5M9HeLP38aiGHTD8YxJ4f3_zuXOmPKeTr65qiUAZlC5uHDAvw0eat_FOevbcMYcJlPxuTWJoJbZ2Dl3AEBx46dedw5moGztGAyGfNkHlWcsNq8NyJKLCkBDexJr_VQNoHXP8Ys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
ردًا على استمرار انتهاكات أمريكا الإجرامية لمناطق في جنوب البلاد، بدأ الجيش الإيراني منذ ساعات، بهجمات بطائرات بدون طيار، استهداف أنظمة "باتريوت"، ومخازن الذخيرة، وموقع الرادار التابع للجيش الأمريكي الإرهابي في الكويت.
وفي موجة أخرى من الهجمات بالطائرات بدون طيار التي نفذها الجيش الإيراني، استهدف نظام الاتصالات وموقع الرادار التابع للجيش الأمريكي "الذي يقتل الأطفال" في البحرين.
حذر الجيش الإيراني: إن عواقب هذه الأعمال وعدم الاستقرار في المنطقة ستكون على عاتق العدو الأمريكي والصهيوني، وفي حال تكرار هذه الهجمات، فسوف نقدم ردودًا أكثر حدة.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/82458" target="_blank">📅 06:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82457">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8b2e00b8.mp4?token=E6rkDWNTLfaS2yu1AnX0wupXVoMZFhXc0hDIgT4YQ7nKC9AA_SeQzxUnc1u7Qm04YuV-HcnHzOLIst4_ZjKIoznw4t1PoS96O7aIJXrxwkFmaHfTNCurz_DaeUqxnxhU6wGE87ZGLiV8WcqnRrHKi32oRVgyWkrFxtzdZzyONoQkDxWkugJnvXBVbU1h1B0yLhb7eOJDUVIHiBxd2vvIj_polY-pP0nWrTRYcOZzRPppbo9skMcSsJCzaWydqNvCTOmqQKEj-bld360pr3iPUYFtHKoKVxJ9HCXPl0EvIETdEq9KD5R8PM9UjVxbsDKHYSV8FvsYNiJxhyVaUY40xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8b2e00b8.mp4?token=E6rkDWNTLfaS2yu1AnX0wupXVoMZFhXc0hDIgT4YQ7nKC9AA_SeQzxUnc1u7Qm04YuV-HcnHzOLIst4_ZjKIoznw4t1PoS96O7aIJXrxwkFmaHfTNCurz_DaeUqxnxhU6wGE87ZGLiV8WcqnRrHKi32oRVgyWkrFxtzdZzyONoQkDxWkugJnvXBVbU1h1B0yLhb7eOJDUVIHiBxd2vvIj_polY-pP0nWrTRYcOZzRPppbo9skMcSsJCzaWydqNvCTOmqQKEj-bld360pr3iPUYFtHKoKVxJ9HCXPl0EvIETdEq9KD5R8PM9UjVxbsDKHYSV8FvsYNiJxhyVaUY40xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقر قيادة الاسطول الخامس الأمريكي في البحرين يحترق بالصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/82457" target="_blank">📅 06:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82455">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=eyz8coDND0tg54cCEDMtghUVqw-HyeTWKwvF6NmWFa5k_EuTJY2e_NlonXIj7kplOIy6l8JW83J5AuDUdpivJJgqflsRNadsIlHjwjZ9puhXZ_hbObJ-_1c2gXVbP4K9RsWSYjYhM7jbWsmKxrzkW49c7dCvdVlVulGnyCHCNoosVA3KUru99x3nmLt3KQqqDUqTenAWNUrpNoVQl_Z-c9mtuCWEhz8x7bSbHUnPylAkJFj8zFh92W2-qdkvNo8xNLhamhTMM47swgr65o2E9yaE1TMpXJw1OOFE65JiGLfPEmANCRAgehwOQdq0dIECrlQF7SoKg1jrQhnIhW7F5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=eyz8coDND0tg54cCEDMtghUVqw-HyeTWKwvF6NmWFa5k_EuTJY2e_NlonXIj7kplOIy6l8JW83J5AuDUdpivJJgqflsRNadsIlHjwjZ9puhXZ_hbObJ-_1c2gXVbP4K9RsWSYjYhM7jbWsmKxrzkW49c7dCvdVlVulGnyCHCNoosVA3KUru99x3nmLt3KQqqDUqTenAWNUrpNoVQl_Z-c9mtuCWEhz8x7bSbHUnPylAkJFj8zFh92W2-qdkvNo8xNLhamhTMM47swgr65o2E9yaE1TMpXJw1OOFE65JiGLfPEmANCRAgehwOQdq0dIECrlQF7SoKg1jrQhnIhW7F5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  اصابة مباشرة للاسطول الخامس الأمريكي في البحرين والنيران تشتعل واعمدة الدخان تتصاعد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/82455" target="_blank">📅 06:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82454">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">انفجارات عنيفة جدا تهز البحرين</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/82454" target="_blank">📅 06:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82453">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e84fbe0232.mp4?token=bHrvItK86_JNIodPKPQ_LJ9G1E2TD-fYM43RDRC3x9vBEUrmDSZ2lcnp_khPGjJcgOMs_zIPZ2Jdff779AiPNf2G5-4BLRMcoQ1MkMdjyQ5nApV7Wek-OIkQmtbuMUwnFxHtbNBQPRuponjntP2PXWkPwPvXM-Hxq9Dh05w8X_8TA667mEt_rJLk8VaOWe4kPr2uM0b6zs_tVn7oV1urvtcj41q8bLxMZWSoV2JgGrg98KDFPE1ftkoD0q_s32a8eHubifSwg_ylW60k4lw-cxZKVU6Sz2gJusJagUDZZVYQHwg-dco3lOGsFfsUr3LnMvsBEDKYVX0fbt5AFNa4Jxg8tDQCQ5wh1utNynyrlEHrI-oFmgCDyCP4l8yJjHBp7FoyyM2BTbN3gY6GYlNdeysh8j6O1R4-OEChhBAYT_VsIf1fHFWQjmfuqfvVKDOCskpw_qhhbEqpgZ_qK6ui3JvWYfbx7ZiT089MOCFM_ZVv6XT_zN3toAJFjp8e8O_FbzyqfuMEpd2MIDVLAynHkZDtdw5EppoHLquIX4wFw4pgJKds1UNA_iP55sCSLJwI_z8Xe3y1OaonZbirsW4Bj_1Y8KTnULY9eh0qhIL-YH1NdoD1_0lWyViV2HBwqe_N3uLbHsbSjT2m_-NoIJ-tA38ASXS2Kj3vGayYDSNnXBM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e84fbe0232.mp4?token=bHrvItK86_JNIodPKPQ_LJ9G1E2TD-fYM43RDRC3x9vBEUrmDSZ2lcnp_khPGjJcgOMs_zIPZ2Jdff779AiPNf2G5-4BLRMcoQ1MkMdjyQ5nApV7Wek-OIkQmtbuMUwnFxHtbNBQPRuponjntP2PXWkPwPvXM-Hxq9Dh05w8X_8TA667mEt_rJLk8VaOWe4kPr2uM0b6zs_tVn7oV1urvtcj41q8bLxMZWSoV2JgGrg98KDFPE1ftkoD0q_s32a8eHubifSwg_ylW60k4lw-cxZKVU6Sz2gJusJagUDZZVYQHwg-dco3lOGsFfsUr3LnMvsBEDKYVX0fbt5AFNa4Jxg8tDQCQ5wh1utNynyrlEHrI-oFmgCDyCP4l8yJjHBp7FoyyM2BTbN3gY6GYlNdeysh8j6O1R4-OEChhBAYT_VsIf1fHFWQjmfuqfvVKDOCskpw_qhhbEqpgZ_qK6ui3JvWYfbx7ZiT089MOCFM_ZVv6XT_zN3toAJFjp8e8O_FbzyqfuMEpd2MIDVLAynHkZDtdw5EppoHLquIX4wFw4pgJKds1UNA_iP55sCSLJwI_z8Xe3y1OaonZbirsW4Bj_1Y8KTnULY9eh0qhIL-YH1NdoD1_0lWyViV2HBwqe_N3uLbHsbSjT2m_-NoIJ-tA38ASXS2Kj3vGayYDSNnXBM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة صاروخية جديدة تستهدف البحرين</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/82453" target="_blank">📅 06:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82452">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">الحرس الثوري: مركز القيادة والتحكم ومواقع طائرات الاستطلاع من طراز MQ9 في القاعدة الأمريكية "الأمير حسن" في الأردن دُمرت</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/82452" target="_blank">📅 06:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82451">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏فرانس برس: سماع دوي انفجارات في الدوحة</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/82451" target="_blank">📅 06:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82450">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8023d66f.mp4?token=S2dkpKLk5V5o0MMH4-AODjsVa7-TjTfaoX2vHZSAS0L4UcbGjA1ccN_L4Te9CTVffVs_P0EW2uZUSYFsm6cYk_m4i83WjZupwGxteAelPTm7MYyxJQJLXxheg9n3iQ6biHfynqpQrpKzidxlDp2ZMlTyHdJIqo5Bv380PHrGDertVrOX-9wO7baSJlP0-6QuP7WllEvCzU838yAPp9aGjogdKKGFuHjmwtL_EVe2lTq3d63ZfgnUzF1wj_yoMHwsl67gNECYKOrRrvs04HvAJ3FIeiWImKgwx5lsERPSwZuBpakRrqzlTCFJjVfaNPErDv72tlUCCnubsP2HA1Zu7pI794nJe4e_XLKnjdswxYy6a5olxdIFqKiKo9VhP8-nVvG38wR5IU4woTMiGAWTxhu3ZQudX2a39tAk7v834OHlFNgbBnWQVQI2obM3zHzVJogmoozi38DEfQzUpSQzoDXgx57fK8DN683BX7RHv8u0S2F_qkGcfSE6-KOHrYYiEcpV1s_lYqY3gkgvyAGDAekjRDp2WQc8Zb95DHc0CmnbyFkGxH2AB1Y-CTalcf_vplcgj_w2N8VOKTyYC24vt2xE1QUFAz-cKZWG31Jq2FWPa71vY6m6GeARSmMQ31wkpYVwT8YoUG-faISOQZnpbCyjYXzLC3N2C6RWcs22eiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8023d66f.mp4?token=S2dkpKLk5V5o0MMH4-AODjsVa7-TjTfaoX2vHZSAS0L4UcbGjA1ccN_L4Te9CTVffVs_P0EW2uZUSYFsm6cYk_m4i83WjZupwGxteAelPTm7MYyxJQJLXxheg9n3iQ6biHfynqpQrpKzidxlDp2ZMlTyHdJIqo5Bv380PHrGDertVrOX-9wO7baSJlP0-6QuP7WllEvCzU838yAPp9aGjogdKKGFuHjmwtL_EVe2lTq3d63ZfgnUzF1wj_yoMHwsl67gNECYKOrRrvs04HvAJ3FIeiWImKgwx5lsERPSwZuBpakRrqzlTCFJjVfaNPErDv72tlUCCnubsP2HA1Zu7pI794nJe4e_XLKnjdswxYy6a5olxdIFqKiKo9VhP8-nVvG38wR5IU4woTMiGAWTxhu3ZQudX2a39tAk7v834OHlFNgbBnWQVQI2obM3zHzVJogmoozi38DEfQzUpSQzoDXgx57fK8DN683BX7RHv8u0S2F_qkGcfSE6-KOHrYYiEcpV1s_lYqY3gkgvyAGDAekjRDp2WQc8Zb95DHc0CmnbyFkGxH2AB1Y-CTalcf_vplcgj_w2N8VOKTyYC24vt2xE1QUFAz-cKZWG31Jq2FWPa71vY6m6GeARSmMQ31wkpYVwT8YoUG-faISOQZnpbCyjYXzLC3N2C6RWcs22eiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة صاروخية جديدة تستهدف البحرين</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/82450" target="_blank">📅 06:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82449">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jf914DP5jpAiUHsgTI7ONWYpJQiecCIjCgU1G8friIOwsbZgcwixX-nwWRKpKMiIht4uOGjVSWUNItrW8TlaCp28f_6lbvY3V2bVwvdoq49YQ4DuxUdC9aOlsIZGIb1BxHCLOuuTtS94SYQJCPDTFBwQx4prIWkzZhJp3uS33KToYhumPtqiSyGZslJutQegJe1pPzekElJppBFr2Yv1iTt-NG9sToldydUwoQ_UcR3tWAg-9AqlXWHp-jGxT151gwrhMbpeXSyhNADescCsjQqhUN0flUCG8mM5uEC60zLSCjKH-wKp9BqtJbbNfnf4zPaNhvgTfjh-zNUth-SMKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هجوم صاروخي يدك قاعدة العديد الأمريكية في قطر</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/82449" target="_blank">📅 06:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82448">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">موجة صاروخية جديدة تدك الامارات</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/82448" target="_blank">📅 06:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82447">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">موجة صاروخية جديدة تدك الامارات</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/82447" target="_blank">📅 06:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82446">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/82446" target="_blank">📅 06:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82445">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سربازان "آقا سید مجتبی" آمریکایی‌ها را ادب خواهند کرد.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/82445" target="_blank">📅 06:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82444">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">هجوم صاروخي يدك قاعدة العديد الأمريكية في قطر</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/82444" target="_blank">📅 06:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82443">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">صواريخ تدك ابوظبي ودبي</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/82443" target="_blank">📅 06:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82442">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">انفجارات تهز امارات</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/82442" target="_blank">📅 06:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82441">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">انفجارات تهز امارات</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/82441" target="_blank">📅 06:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82440">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTaLEXO9HcejHls4PX9zTXAWMQf7dINXcLZG42ufDbUnuLHm1Qhn7n4wlOv6iJC71xzlnJqbsMDok3lFhShxvTz0dSmM-UeAEmEOBkO1ulCFjekpyVQ7vw33HvKvidu-nVDNbp-s_U5rBwc2TA16aBncpqXX6RpAXJTvwTElvUfZC7Fywvx1jzlkBa8_AeDiTFtiTB3OSqSGIL4SU-98VFIkv1_uVLF1qVLJtzrQhvvH9lV99RS3ezPYe1s_8lU0aOtWO-Vb2_i1Lnn9-8hqnFZq6PYW1MaL1HmhT1AA6KRmSYFjX4vyAFhyQ2sFDXwpTMImvIN2f586YSDnW_4FEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موجة صاروخية جديدة تنطلق من إيران</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/82440" target="_blank">📅 06:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82439">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/82439" target="_blank">📅 06:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82438">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/82438" target="_blank">📅 06:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82437">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36b3e9700b.mp4?token=KpWm8bdy5938tTWvu6felXkGZdJXLqLJBLrzOAvBtGJtflKKg_aZi40b3dljVOEY_VG7KDcKS_X27Zqgohc1bDQFQjrlyUGl0X8aGh1W7eMr7HJPhbbykyFQduoRWQxjKWKQBAWKeSAz9W05OT61qWyFCClcqpTWDuI95TdLf5NHy0093ZwtPY9fO532t2c_94I5sqnR-d_laTLFi_Pnnm-yoPgWqcYxLGzRAvuVVCTlsGdpia7gmJCwCsbgeNhk0qPj3PSSND0OdrNr6oasP6SUudo6segzOtbhmkX9v5fiJy9QEC3ODF5n8QxnlK0SU3n_KFk5w6MTdn5-Ixrngw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36b3e9700b.mp4?token=KpWm8bdy5938tTWvu6felXkGZdJXLqLJBLrzOAvBtGJtflKKg_aZi40b3dljVOEY_VG7KDcKS_X27Zqgohc1bDQFQjrlyUGl0X8aGh1W7eMr7HJPhbbykyFQduoRWQxjKWKQBAWKeSAz9W05OT61qWyFCClcqpTWDuI95TdLf5NHy0093ZwtPY9fO532t2c_94I5sqnR-d_laTLFi_Pnnm-yoPgWqcYxLGzRAvuVVCTlsGdpia7gmJCwCsbgeNhk0qPj3PSSND0OdrNr6oasP6SUudo6segzOtbhmkX9v5fiJy9QEC3ODF5n8QxnlK0SU3n_KFk5w6MTdn5-Ixrngw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق يظهر لحظة إطلاق الصواريخ الإيرانية نحو القواعد الامريكية في المنطقة</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/82437" target="_blank">📅 05:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82436">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/338f41fc7a.mp4?token=WyUqd9kSnBmQRPJ-oT8hLNe3340FdtbhEYVnn1yZW9naRph-jZnIo4sHzNqm-LU5FDXhvn-JtNKVqkSoci9ttxcnuZZhmHpOmtfBpjohyQ0rj7v-4-AckjOl030y8-55jHs0WpfnJ9CIOdYbdu1HneuKe0SJmLcqTcV8MPSItSCfvhFRPyhtixFvSiuACtZtGJQMi2pJ_JZ-u2gh3sfvybxo8j_pFjdm59vimA6D8xL-A4VcM6wBq8IVH49KVydGuYIBmDlvoNh3ShjmvYXL0vxvlq1lFBfCy2qZWG1LXeZ-u6iS5i2ALmcKa_Mxrh7SxFkYM7BtGf1J_ZSMEFFxOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/338f41fc7a.mp4?token=WyUqd9kSnBmQRPJ-oT8hLNe3340FdtbhEYVnn1yZW9naRph-jZnIo4sHzNqm-LU5FDXhvn-JtNKVqkSoci9ttxcnuZZhmHpOmtfBpjohyQ0rj7v-4-AckjOl030y8-55jHs0WpfnJ9CIOdYbdu1HneuKe0SJmLcqTcV8MPSItSCfvhFRPyhtixFvSiuACtZtGJQMi2pJ_JZ-u2gh3sfvybxo8j_pFjdm59vimA6D8xL-A4VcM6wBq8IVH49KVydGuYIBmDlvoNh3ShjmvYXL0vxvlq1lFBfCy2qZWG1LXeZ-u6iS5i2ALmcKa_Mxrh7SxFkYM7BtGf1J_ZSMEFFxOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية تتجه نحو الاهداف المعادية</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/82436" target="_blank">📅 05:38 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
