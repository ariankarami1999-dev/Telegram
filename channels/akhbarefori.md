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
<img src="https://cdn4.telesco.pe/file/aGa7Uuia01jEtuYV7xOPdB6eiKQG4hZUonMIbsCV6dRXUKGSxpTaezX8-Xop-JP-X6khihyd1mOmivul6FHBI-B1hJFcd95wgbWg1e1pQezBRvJIq5Qsm9tM3U178-tWc8lob7juy3qnvacn0psVOF8-vZ47ujyJ97kqFRYN_Qx1uCd9aeSfw3fHdTP_xY4RrIV6W0yhoXZAwq8Fq0ua11eSrFrYvG39gAtrnk-Ef-8sebNyv_ptckRLtDEPe30GISO9HGs_BsCdiep00hfh8TY2sK3KQ6d1zLYqc-6xlA6_LDBBmJzhayoHsR1LQByqDJ0Uu-dDaAXhLdlc6i7UVA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.34M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 13:47:57</div>
<hr>

<div class="tg-post" id="msg-674471">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
مدیر مسئول خبرفوری در واکنش به محدودیت خبرفوری در پلتفرم‌های داخلی @AkhbareFori</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/akhbarefori/674471" target="_blank">📅 13:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674470">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXeJpoOyEYvQf6rhWymznO7cP_E7d1Hw_uu_QA6eyi_K04vv_J0LAChRDBe9Kbh91iqR134gPOobqMsB_JwpbMVd3ThLq3raKM369VhxXlCEED87OeQBiTfK3KU5hHVUTLlDrEx94KYKiBSblv_QFEbvv1sZ_B-q71REroqBtfBxZyHAoELOLA7uaYt46WfEGLVHK35SIS0Y-HZWKnBUuyum28zBP3rg84aHa_foVyq2qey99re6-ZuY5TaYXFXlpKBdbx4PhdRwKBY0IOW9BiTHUqpvc7hGylWeif3B4zO-kKUMvV76TmF6xg4MVKHnAa1bj-0u2nESoTZTU0cEmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعلام سیدبندی لیگ قهرمانان آسیا
🔹
سیدبندی لیگ قهرمانان فوتبال آسیا سطح ۲ مشخص شد و گل‌گهر ایران در سید دوم قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/674470" target="_blank">📅 13:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674469">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ac378733.mp4?token=jABS1R6aoYwTswKdN1oPm0AEQd732xBAaab1StqbqBBg33utZdN5Ta3-T5rUVV4u3xn1aYAqV6Zmwv_qv9PPPzt0yFNWP0qjUiJSF-8HGhk94BUKQUs-GmmozUAgHuyEyCKpN7UOVZKv02wUGf7mQpOIauxbJE_P9oDmFMEoEjEAGfRbwF_jxLrj8Kng6GhFzVAvNF7wvfERjmXqmUhPhTqrMyOlkTF12J6ngJYY5M-fLn610h6sDwaTUnzaBMPW7_Yrl5o4YCViRQRew6eNcoO1RwDEKFTCk5ReFbnYNpxx36pVle4oFYa3CPez6BmQgK_FOXdfstnl0A7PDoQ0Aivn2SiRYJgS6AAe-ULTgHxZjrcKVvx5BgF1I2OjHSmDkfEqZDUpssRK9hZHu37Q515zeL7L4ertoHMXJxjflYPUJD1JEYb9aYhY-LGnRaTq9ZkXX8bwLx815uDKRBKops1GzTN3cR3zI9vseoSZi0tE6e-rLSIm-3lWik_oawndtI1ActBaImGaTCvkmyDIdTuVeAZ6cP7k_LgOB20LzX1U2lDK1-LtNVAt1eA0dwZwiGekzvpF20VgHVfEbSodZuWSBTy6bezcZsjE454_5NDN4Vuf1O4vqkzHC2dS_xTyL1gyBClhJpGzRNUmmxRuFGXzhj2rRSLPoR_xH0xjQWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ac378733.mp4?token=jABS1R6aoYwTswKdN1oPm0AEQd732xBAaab1StqbqBBg33utZdN5Ta3-T5rUVV4u3xn1aYAqV6Zmwv_qv9PPPzt0yFNWP0qjUiJSF-8HGhk94BUKQUs-GmmozUAgHuyEyCKpN7UOVZKv02wUGf7mQpOIauxbJE_P9oDmFMEoEjEAGfRbwF_jxLrj8Kng6GhFzVAvNF7wvfERjmXqmUhPhTqrMyOlkTF12J6ngJYY5M-fLn610h6sDwaTUnzaBMPW7_Yrl5o4YCViRQRew6eNcoO1RwDEKFTCk5ReFbnYNpxx36pVle4oFYa3CPez6BmQgK_FOXdfstnl0A7PDoQ0Aivn2SiRYJgS6AAe-ULTgHxZjrcKVvx5BgF1I2OjHSmDkfEqZDUpssRK9hZHu37Q515zeL7L4ertoHMXJxjflYPUJD1JEYb9aYhY-LGnRaTq9ZkXX8bwLx815uDKRBKops1GzTN3cR3zI9vseoSZi0tE6e-rLSIm-3lWik_oawndtI1ActBaImGaTCvkmyDIdTuVeAZ6cP7k_LgOB20LzX1U2lDK1-LtNVAt1eA0dwZwiGekzvpF20VgHVfEbSodZuWSBTy6bezcZsjE454_5NDN4Vuf1O4vqkzHC2dS_xTyL1gyBClhJpGzRNUmmxRuFGXzhj2rRSLPoR_xH0xjQWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به یاد کودکان میناب....
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/674469" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674463">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z-BunV60ksVc4ZrTR85Vs5CIfWLaC-Kb-8_InCTrhB_dTHMOhSGwJB5xCh87eTc79WUTxBkWJRoNf7M9Difeem3w76bcXME8vHBzy-EFYIWpotdIeDGHY86uxiwfdW_xKZcsA1NA1n0rZIrhs9oSj9bfPLkRGNVqQb8oOTOBdDt_KPA7mYCG6lz0M-2I_EOpteRZlMOsfXVNpwTZCaNiRKKFBaf1L4YvMQY6rt9sc8gvNhQfv1x2YQugBFTld-2KoJY5rovlmGnqZleTekXN8jUvz9kAD4JKSnU81Mb5MrNK7DFaxK78gbDEUZrTeciyuJ6Ukxm_sgPJChpfnjOEuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vdFFv0elrm9aXMbTIHObmCOBiwrgpWoKNo4AJlXKvBHATs7Wv7v4y_8AOX5YEcTDAOmRKGUvcJO1ndo18vjbiNxkywl8LgyVPxaBZvNj4s1u6oONX-arv4037OdhgeAeaLV83nyBpxftVXgksDN5hEacrtO-FcRZkX_Yf3BrOYUlFe10QrVf_uZzcwOdFtIxNYnxGEKSzwoVsAys9Xb_nXy88r3ygTbdNQdZqx27w-ELPLtSUIs-mChz6f8Gd8KYNATK7UgVF6AUbEOXWH4wteTr5pxxy2Uq72u1WCbWnYvHO0id9-kg_is-Z1RFmDhCmCmNZadwwVnwLHnu6uVoYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJDfr6FiJiCbLLqMwVMFMA9rbJPyv47mRXAbc2hOG7ewKJoJNg6lIdryvWw8xPk-zacjIy4qXUVuFFAVGErtKjTvYX6re8O6M245qxg9WtufJVUgL_LXFFv8SzX0V231mxaCY8wnNFzlm82a99WZ3s6kflRag0p_uvNwvX8V6Wx2eyol_egaLagHYdU3K2_HAtUCzWr63Cx8CbQ_knfmcgsvWBVvVFazM1-10O-h4_QdEaPQl5sp1Yt7quI5lUrYd6Y77_ZqxvlLR-qYPva7Y44KXh2jb3Dwz3J3TmPkgeJraOceXcCO6DYV_ap4mECpxoatq27KMjwtrmiDIuYRSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jAERVx2tOxpXOwfPRVf4lAlCVMulFqVhGPjOD8gPEpYt9xCT15Ze6Y7U_kT60aUF1i7v3LXFyBYdkeSlxAJUjoZz_WS6NODem7P-o6cppxTcmonx9kLni-D6fdmNfO5ud4w21xahyqPB7TKOVq78Z6jVUDn5JJNIZoVI8Clupuehcn00FtLCM1ZOiqUmiYs3m1zTOv_7qYa45gieJ4OtrwC1tz6Y8LTpUV-ZFhuG-hCi0jhen3ujM59GD2icUYEAwsLj8eN3O4abYqq1UX7g5cRRUCYbaHqVqK_X5EbvEMkC-6MwJ6-dFfBBQZ1CPwAGbfXC5bry6ka1yS48Zw9UCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QilM8kine50Hf7AI5Gt388wfYowtdQ81zHA2AgguKgIqZKbrU8GOIcHLxTcusA5aGNo_ETyEWhaPRP_HVS-R0H9ndev6mTFNp80ewh4ohNhGtZyCOJeU7TShxOz4l2WpFidN_MEyYAO8LRYZt5ML6r9xFo1CuftRiOXC7y0kyAvnKupxZ3a0Dn167al0_8scuU692W2lifr-tAI4ckJk1-yLaccYghkgIWelwkrM0cKFpY0m2LTHEPUQUR4c5EzvbkqQkuSUxl4JBtFXWxXxyfG0tW0ltLy2G-WAzbtkUYhO-3l0mZO2o-nEMJMKJOTo_wWiSBDSCNAs86FAocLpRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NUQfM5fM2IGEIhYXV1TVG1V4SLtjTTJgAxWgjCYPlB166P51oQnjF5hd2me21zbbD9-9yfWn0HBJvhy5VTVH29VGbACGYyKkl92n8csng-lRbbSpbEcrDmXRSDBjnUDPsibeR1Km8UOh1l8F08yrvohtOeDueHZR-1wr7BhQ4WMb1qt6e2OcXrTkDMEj_QBYjjeVnU4XNYnUYeiYje2aOSKFYXL1ffPjvIXyytk2dERswg7w2XddnGgGiXWYnKzfsNjCysdL35a1nz3vGrRgcNMIm1_fD_CvetOEkHg027jdlr0zZm75ZJK1ge3lc731J19T6HhM5tbcw5beM8bBhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
یک عکس، هزار روایت؛ کودکی که در دل ویرانه‌ها امید را زنده نگه داشت
🔹
رویترز با انتشار تصویر اکرم الفیومی، کودک ۱۳ ساله فلسطینی که در حمله به مدرسه‌ای در غزه دست و پای خود را از دست داده، با وجود آسیب‌های شدید، همچنان در خیابان‌های غزه بازی می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/674463" target="_blank">📅 13:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674462">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مقتدایی: بدون استثنا ایران رتبه اول موشکی جهان را دارد/ آمریکا از ایران گدایی مذاکره می‌کند
عباس مقتدایی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
ایران بدون هیچ استثنایی رتبه اول موشکی جهان را دارد و ثابت کردیم اراده لازم برای بهره‌گیری از توان بومی در حراست از کشور و منافع ملی را داریم.
🔹
اکنون آمریکایی‌ها از ایران گدایی مذاکره می‌کنند و کاملا مشخص است که در برابر  عظمت، اقتدار و توانمندی ایرانیان کم آوردند. آمریکا با لاپوشانی و سانسور وسیع کشته‌هایی که داشته، تلاش می‌کند تا افکار عمومی داخل آمریکا را مدیریت کند.
@TV_Fori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/674462" target="_blank">📅 13:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674461">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6272e587.mp4?token=DrBp4xKTQwI-w2jBCEonF6jksfHlpfnInCiYW1mQYKXY4NHn0JZxyNSaoZYGEBnifSb4FQYSil3UORfRkqXAkScumqJF_04vRRGmSvzB5ch8F4TPKetvK5WfPVoq1LzAD7JHgugzMkzzDx8aordNx-oudhm9FtSF5R5QyY3p6h39zXrC2g9R53P0rgqSQCTCpkdAmZ4_dbI8fArOJh-Wf8UjZVplgiYnwA-TVV5IUzO8IPXfrNSYS-eYVDL9DW-MzQZitnkKbNQfzVUJGDcXzAbWdvdJ0UYGqBN5mnwkJOw492XUbOw2cmct-Jt3L5OCkYClWLDTRGG6qBDpEQjjKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6272e587.mp4?token=DrBp4xKTQwI-w2jBCEonF6jksfHlpfnInCiYW1mQYKXY4NHn0JZxyNSaoZYGEBnifSb4FQYSil3UORfRkqXAkScumqJF_04vRRGmSvzB5ch8F4TPKetvK5WfPVoq1LzAD7JHgugzMkzzDx8aordNx-oudhm9FtSF5R5QyY3p6h39zXrC2g9R53P0rgqSQCTCpkdAmZ4_dbI8fArOJh-Wf8UjZVplgiYnwA-TVV5IUzO8IPXfrNSYS-eYVDL9DW-MzQZitnkKbNQfzVUJGDcXzAbWdvdJ0UYGqBN5mnwkJOw492XUbOw2cmct-Jt3L5OCkYClWLDTRGG6qBDpEQjjKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رفتار درست با امضای ترامپ
🔹
رزمندگان نیروی هوافضای سپاه در عملیات بامداد امروز علیه پایگاه‌های آمریکا در منطقه امضای ترامپ را پاره کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/674461" target="_blank">📅 13:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674460">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e635f930a2.mp4?token=VS3GlhP7vcn_kUOpbpWD4ZCF7i8nNdZ2f07aTCV9sGG2sNe66HvzQQ6GA1R7pVIEGNI_w0P4iQGkWfqbT_mo62yQ8D3WUsBpMfseXoxRltnneiwBR-mhZlb4oR4LE1QJAoWoXDt0Pd3RBv28_MznqU6ZxSYy_4htnU5lz2R4DxuLH9dGnHffqmr7mlv3qJS_9vjK93z256iAJYF25jkonEtsCRgsDrbczPyF6sqD0toVzVEMaeEGpJuq-j5S1driok19gx65-gBKna_w8PSCHF6A0R54dz_Po0HCW9SAkYs7XKGmQYY3UhEdIzEiPkhC6Kx_2RPrLj8hyga0oUnaIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e635f930a2.mp4?token=VS3GlhP7vcn_kUOpbpWD4ZCF7i8nNdZ2f07aTCV9sGG2sNe66HvzQQ6GA1R7pVIEGNI_w0P4iQGkWfqbT_mo62yQ8D3WUsBpMfseXoxRltnneiwBR-mhZlb4oR4LE1QJAoWoXDt0Pd3RBv28_MznqU6ZxSYy_4htnU5lz2R4DxuLH9dGnHffqmr7mlv3qJS_9vjK93z256iAJYF25jkonEtsCRgsDrbczPyF6sqD0toVzVEMaeEGpJuq-j5S1driok19gx65-gBKna_w8PSCHF6A0R54dz_Po0HCW9SAkYs7XKGmQYY3UhEdIzEiPkhC6Kx_2RPrLj8hyga0oUnaIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخست‌وزیر عراق به تهران رسید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/674460" target="_blank">📅 13:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674450">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XpGlF6bSREfTRtPgAII5wCjUzcYCpvRpVi92vHBAYtrAhkZKYYw98sLjV1pSiZWEkhpK57tNJPQoGm61SAOdxRmSiJqhxBjNARGE7W-1WVm1pzgrFmmqLfeKHuju4Vx7s_Fxb4V0_Rrc4FB6hlu6S7EkUlRKCkQ5fXsSPEUo3jeK9n_djIUVnVbLU80I4hIV3Ip5YQqTQPlFUlBJ4sQqzOJEyX7Gfo7NjiVM_ZKOATUzjkHElQaBLLwKhAI-aaaliqnsF2bik9eRapqXaQTiBCTv7GJ-V4dd46keN8tQJi7bFpYUU0r4EIi7iDNYOGQbRHVAGVGUaTQPokUr6lDYCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dyxtoZX4-lE3KxGBbfCy5a36_0i6nFwgvnr51HujbhkwY26o8dtXkDm-dD2_6LW4cXM1A_Aj1x8Uct9thxy_RoySIY5sFYThBY5TfX1kZ6Lw-EYAfIHhWe93Gf_7LTBU5dy1OkCg3qZTqdWi2E0Gi2Qt1HgXM8c-JcaI5OMorBk1Au1mT1HgKCZ747d9j36RE7wrp6539kFxFO_Bru34mFwkoxspRfPa-PsT4xslcI6hH34fNHgmEU9Mr9lH6dCOhvJZ8h_LPYj2YgGrvDP60NyJZve5dht_OtzCVeIqwdeareFvmIpwXjXhCrh1WqLIMwQjhvojbUWqid39J3XDpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M0bX9NDFLOZouqPPxAg1GLkWXQ8aK8TAhdqn92D1tkajCCOos-E3eFw1pjzjrP-rGMv8DE3TgUHLhXWxMaOpFB6XjTyEElmcjgZwogTt6o_jprs6_LuJtDOtg4_CAJKOtMrHE-RGrPpspb4yq8ldLPuFbindpsEmU8e7tv_7yWC7Hd0BD70taTB_PGzN5e3SHVfISQnsfjqeBuLyfySVo6rZGpf-0sDAxo7jMpw9lFGegjCinAmeaNHBXb20ZW7Iyw3xGnlu0eKKSzlqwviE6hLMAD_V8gQOHzzsHUGt8OfV9jg5IYst-gtLG06vop4-cQEMhmPrpqME1UdRpIMSSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AqISeUdFwnejyXTSttuW5TJXfDjDtz_vpHccUZGVQ9lmEhuUoM9wUeKJAPbB6Yz3aOHAQbDOR2XYicnn5-03GGI1Sa7CRPJD769J8ZmqCtgiRXVTVZkNH_rKjl2H6h1pkOSeUfoX09a7dVvj55PGQJMsBb7BgbbIE3WVTtAigo5Aq9NuJ60jNg59rFK5GghplRsAanAfOqgbzDksA9_FyR5OoKmyyXMGQ2OE_7LzkwL6ccSEqeDeplEXsNRl8mz2CDga3y9jm5iJ6zn_LwFt6_uN20QiqSwd-T6aMkiywcNr3nEnC8y1UQ8wOA2lTn97d0jHfRYhYgYO5NL5oFxEMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PfwzLX5gTzd_qyyx3gOo1oW7Nx1RmjpzDDi9DcVrKEGbHmHk5aul59gBbjOL_JVEWAwiUDfY1JZ8qUrEcjSmDJfeEb4tKzDZhWu2WyH-FExachh3GGW2sCX2U2rcl-_Q87UqkezMkLAYneFa728CFwcaSpSuaLpBpXsaqsT0bWrT6v8t3BPZo0LUhJQ22YGNfEF8ee4xVH40pHM7aqeWnbW4oLDeH6RbqfD-JC5o81pjNduk1h4ibglFEe2xjyQYFHfdDGMZlfzcZsHchnpFaiTPKh1GxoWrjIMjw2jAXsrfeZXCslvGukVhVKlTH0656dMgNDuhDI0GOu7r9T1ZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/II2iAOn2UJMjCKKLVwmkvt5guaQmCs63bN_rsBkLe2we-GFcRj9uKwOTqvqZisZSDqt8Sw3Nc06DEUVAflGikiJXIcQjuWds7E-QAhr6ccSMNO1oGzUXAjnak1MFYjuAAAiz66PIFrX0JIDrQRCyieSUyRBkdgS-ph1QlPiwllqlXI8Q7xYBSON3evC7Hpc5ZJY5OREWiU6KffFOyAeu-s8-3CTynjzcNq4xaJQKtbV_8GyoXgBYyirelImUc_-p6W4vkw0Lv8Je0b6HSaV_xzfWqkWqk38cMBcN221S1uBph8OYUSHB9A0OKlnzjvCru761JK1MiUGcJHQ-FGdkhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lKRtmGQ2XFJhasBDwN2IVpeIx_idDl8OeqAh0rZqgYwWwhuxZEGsh78BRMRK2wHFzj1_gqLSug9zft_7MuAekTqDgA8CJGfkBB_Ag8zgxSFH6zZnOGPjSfHe-0961aOlyjNgXEfZmu2nTjAQnCb_IoaaeLOcbwIWo0IttVA03sbZAcNELogYbUYzSPpgtETS5-xVtIpviwrrdK2gSC24cCBAEx1Z9kHvKIBHqqmAegAB4WO1DX4eHb3Kssn3KCoMSoF-_9a6IExt2bl_6t9vMWtVT3yghQMQKIhgaazg5tZVxFd9B9_FwS-QVDSjEnQKy3cJsic_xsVxuiEjFpzcng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tF7Y8ElSbYNU3GrFnAgBi1M-cGEj7bOYvhuKLCfZbBF5NOwj3-nquih9TWqbVVr4gNCiWKik5n0ygQqQIjphaP_itB_SPfm1p1iVtJLqzQlhN4tmLEFyjtsevrzcd4xp2-_s2KCFwJZN1FxlrQyBXnjd0kdfpRrZ-YOhOqxiuLWG3Mj1x7SrPDUZimySmvkhJTTDDtyOwH-_iL7kTYFrjbalK1ot5jRScLbqqRBvjYP2SJyW-KvTcI6bpPRfDvmMTdP-p7ooW44L4Co2sxN1SJwPz9fkSClSYgv4NuHGOBZb5dGxZDC-Utu4eUoYcEG5iInVVRqhOnpO-0b_0qhECw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJNqHQSZEHDFG_vXF0ySdIpzgtwgeh7c443Xgxz-8WaQREkLKJI_DDsNXS38ZKtj9Dq1QO6ptlRLWtaiQEUFNZWGYFJJlRyCsoYfTmMHZZF5Mugv6x3NAcGsFeG-fKUhb-RX71B2mxgm4-0sROVZObhgHOZBhTJht_SbyWkpSQ1kaNZnkznr5i8fxreKmBci3t4IHUw2xHDWspo1ytSWOI9NvIBVnbiwYzee_zYxmmMYsWA1ABNAKUPhMiLA2mQ715h2Lst9J1aILmGm-FySluVlBUrbWN_CnXtlLtwQU7O_dJSS9Wkpw-1PSADQUVUB1GeiA5yBVLHBaV_chwKgbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d0IB9xA1U1kNj7kvk3rV_XOqRiZ-mw2PlpbOoBWsulgr1KmSMDQlgZLEVaGOBRuFWpeT-VNPyLNcNwdOjW4FAv40YELAHtjIRIwgZyQEEWfLMsezAYwl_sti3QyqkdKSeh2wxXxeE_SS8VymL905gapvESjsZkMUehqekWXT7_MSXpHrbL7GTgDssFshTHAd6e6pcZCVp3r5abTl-w93qHwn9vyHi560KbrBSQ37nRIvth3NG_BQ-hgaNY-jLZ_i-ce5x5KSawBQjxU3xksLfu8T46GFMNDCsTU9DP_WOLlFWeWEGoshfQxrhb7RY9JgHBUY2maIlJt17NuOhndoZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مشخصات، قیمت و جزئیات هر خودرو را در اسلایدها ببینید و ورق بزنید/ تیترتجارت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/674450" target="_blank">📅 13:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674449">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83fea37c73.mp4?token=iobDyxMCmyD2Nc7Kkb4oPVMkU2OODSfvF8sy9CXmfAV8kPgP1KQUocusEBwxoI8ginQE48243vWR8zUMzSbFURDRM8Xpqv7SAr_-Z1mwCbfvi-YmAGHfp1DZNGyptr5kEj4_r7C3jnoStjE4C4Xa8fgZvhzlTy_jhLEqpdAEUBpVf_9VVpC6fRPbQmhqX3G9RHxNh2N7MMA1hLWDQ_Mskd43FDgbXHOWIEcen2pS1_qSjGgFy0wPwFSPiFHNNsWOQ5BPnFWGUQmkZIR4plqP0wHubTf1cBEczKV06PbFS14r7GKUnQQdjemFA2Au0rXQc4Gf2ZTohokmAJBwtNDE7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83fea37c73.mp4?token=iobDyxMCmyD2Nc7Kkb4oPVMkU2OODSfvF8sy9CXmfAV8kPgP1KQUocusEBwxoI8ginQE48243vWR8zUMzSbFURDRM8Xpqv7SAr_-Z1mwCbfvi-YmAGHfp1DZNGyptr5kEj4_r7C3jnoStjE4C4Xa8fgZvhzlTy_jhLEqpdAEUBpVf_9VVpC6fRPbQmhqX3G9RHxNh2N7MMA1hLWDQ_Mskd43FDgbXHOWIEcen2pS1_qSjGgFy0wPwFSPiFHNNsWOQ5BPnFWGUQmkZIR4plqP0wHubTf1cBEczKV06PbFS14r7GKUnQQdjemFA2Au0rXQc4Gf2ZTohokmAJBwtNDE7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لفاظی‌ روبیو: پاسخ ترامپ به ایران «سر در برابر چشم» خواهد بود
🔹
وزیر خارجه آمریکا بر تهدید دیروز دونالد ترامپ به هدف قرار دادن زیرساخت‌های ایران که مصداق جنایت جنگی است، تأکید کرد و مدعی شد ایران در صورت ادامه روند کنونی «بهای سنگین‌تری» خواهد پرداخت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/674449" target="_blank">📅 13:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674448">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: طرح تامین امنیت تنگه هرمز برای چند روز آینده در دستور کار مجلس است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/674448" target="_blank">📅 13:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674447">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn98Me1kMV4oXk5DPBzWwwJEOse70JmULAM-m0Tw8cjN6W36Ak18oAlXnqeDGkV1ZA6AA4qqQkAigwAm0xOjfx3jBfpoLn4O853RhVWdnhKnDq2mpaKvGgf2VzQj0wpOhEyTCtwavWKbBM-3QKvHx9XxQyJRBAJXtzx7l5PmtgZa8aV59UOsXoR66J8J0vCUVFEr1ejalQdKYfhWrNuUDv4QanXx6oN_9HauanxeIbhiLxdRuTGWf4DBoGU35vake-0PabFlRZuUjdnaV1CNESA7HfSsqHtmORCetjMSWubAhxbG4WbVOOboagRhqYETtkqAE3svlpnZW_YUQSQiPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱ مرداد ۱۴۰۵؛ ساعت ۱۲:۴۰
🔹
در نخستین روز مرداد، دلار آزاد با افت محدود به پله ۱۹۲ هزار تومان رسید.
🔹
همزمان بازار طلا که روز گذشته در مرز ۱۹ میلیون تومان قرار داشت، امروز با افت ۱۷۷ هزار تومانی هر گرم طلای ۱۸ عیار، به سطح ۱۸ میلیون و ۸۲۶ هزار تومان بازگشت./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/674447" target="_blank">📅 13:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674446">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
هلاکت ۲ تروریست در درگیری با مرزبانان
فرمانده مرزبانی فراجا:
🔹
در درگیری مسلحانۀ مرزبانان هنگ مرزی جکیگور با گروهک تروریستی، ۲ نفر از آنان به هلاکت رسیده و مقادیری سلاح و مهمات، فتیله و چاشنی انفجاری کشف شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/674446" target="_blank">📅 13:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674445">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-60T_OWptZzsbz82t3mcUbE96mD4M7xx1NGcSqpPJvNayCk8YgDVWigfJ7lrxpeTJntk9Lo3SkPIiA2hc6TJlCgjJpPxAB9nIlkVlR7-2KTYQQmVk9Hg_R6SfFjEhnVCq7I4BYqyVa0D_mswbHaYt8_MDyAZ3NAm99Wm-Q93MAhleolXbEvdYZuZQI9KAW9Fbb9-3LCTSDWrPIp5ptnJ8UoNHTperRVBlmp7CeJ9G44JzTkGYmhZ0_p5XYEjoiJNQOAUX98YFwcYsiWICJy3NziqvTTErYFXW3UH40bC-Hsxlejne2wyROoNK3JWWU3bEvTBNXiKrA_mpBbT-sY7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت پرده اظهارنظر جنجالی هگست درباره یک بمب مرموز/ قرار است اتفاقی در کوه کلنگ رخ دهد؟
🔹
از آنجا که کوه کلنگ در منطقه ای به شدت کوهستانی، پر فراز و نشیب و صعب العبور واقع شده، بسیاری گمان دارند آمریکا نمی تواند با بمب های معمولی و عُرفی ارتش خود به آن حمله کند. از سوی دیگر، وقتی یک سناتور از هگست پرسید که آیا آمریکا قادر به حمله به کوه کلنگ است یا نه؟ او پاسخ داد: توان آمریکا طبقه‌بندی شده است. آیا این سخن به معنای ورود به سطح جدیدی از درگیری ها و استفاده آمریکا از بمب های جدید است؟
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3232388</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/674445" target="_blank">📅 12:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674443">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYA3fwEVwMEVzPC3MMvaZP0NlMmpw-crhnDxz2SkdLbgsWMZ08_R_87v_ybRH95NvO9upYchT9i96_pTx7vxVXm3cTB7sSBDvUMQcy7xi6ypBylQx1-Kzu5NtOWMSU3MZjMmGJpcw14zKSouI8Uxz92QZbfSWDAQWJiEsyK7fsXrOh-K7oG8DUVpJB4e1-pYiJ2kFy71OAKLY44WLYm-un4JGl-CszXjM0XIZKiN0T8oPC4hCh0ds3s2LOZoa3Sc7fXxe2w2dWLeykU-nIBAkxgfa_XG6RKkwsnPtWDe7FP8YNyu8YWaUjdLKuSUsoMX86jGoD8W50gcssP1RLpOug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه، جنگ روایت‌ها و دستی که نباید بسته شود  مصطفی انتظاری هروی مدیرمسئول خبرفوری:
🔹
در روزهای اخیر برخی همراهان و مخاطبان خبرفوری در پلتفرم‌های داخلی درباره عدم انتشار محتوا در کانال‌های خبرفوری در بسترهای ایرانی پرسش می‌کنند.
🔹
آنها می‌پرسند چطور ۸ سال…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/674443" target="_blank">📅 12:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674442">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrOcnJKBsmkRPfOlV3-PzXG2TTyqdNzLkO5blPvM9qUNqyJc7OyRtOyjhWDc6Gzk-QCVaVfNawyJJaPO9i7UcUn4qdcVtQqCgrA_6FGtQyPUc4Wbe91R4RjHCvoEalCTKgbbKS9LC0Mgz0kj3GfO_DzkK8JA469CSgEzUUUNkTtIMKiuafjh0bcKeTCpDZ1JPaJr5JKod44CukVugtMRH-9NpdqC33UCJwBcZPOPF_WILspOidDVQckHuigYhpF-XCPVVoXO-O5tU7modkZsqo90WEHbDD32p3TfX3ws_HcitM06Xs4JdJt9q6gzhDn96TQDLDszYZgqjGxtL8tyNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇️
افشین خانی در مجمع عمومی عادی سالیانه از تدوین اهداف راهبردی ۵ گانه خبر داد
✅
تاکید مدیرعامل بانک صادرات ایران بر ارتقای خدمات بانکی
🔹
مدیرعامل بانک صادرات ایران مهم‌ترین اهداف و برنامه‌های راهبردی سال جاری را برشمرد و بر تداوم دستاوردها و تحقق چشم‌انداز آتی با هدف ارتقای خدمت‌رسانی به مشتریان تاکید کرد.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/674442" target="_blank">📅 12:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674441">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
هشدار حنظله درباره تداوم حملات سایبری به سامانه‌های کنترل صنعتی آمریکا
🔹
حنظله تأکید کرده که دستکاری در کنترل‌کننده‌های منطقی برنامه‌پذیر (PLC) و سامانه‌های SCADA، تنها بخشی از توانمندی‌های تهاجمی این گروه است و تهدیدات گسترده‌تری متوجه شبکه‌های آب، برق و ترابری خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/674441" target="_blank">📅 12:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674440">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCROjYvrVISPFWmbbV5iLdqCvTC_12m4z4_hLKsDTnEnTmOwrg4ul4ufOtzbZPuTyJlH5AUz_-s3f5MtIcpZHXEGcMSptCQG_Nol-Bt-rfIm_InLoDJlMp7G7iLFp4rnBxktdj0VRV6rg56_BRwpMuIxmLUx9PA83_OTAJceuQMuGp1uhU52niVF5myo20hcbRzCCdEOaSmwXlC5c81M30Q1AzACLBFMlvRWDJBvatZqhIdGxiQFHXigLSMW1jNcvrwGO6jbinVTGjXsQZRsaTYmrFxfJxefXF9-bTP9hMbNpe7_ziarykxLvbRPjq9omDaJ7IPO5XSuRE7rGFY2Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیبایی‌های بی‌پایان دَرَک در سیستان و بلوچستان
#ایران_زیبا
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/674440" target="_blank">📅 12:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674439">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در بحرین
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/674439" target="_blank">📅 12:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674438">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در بحرین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/674438" target="_blank">📅 12:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674437">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46299f1ae8.mp4?token=YTuKdcBljWIVO4PWMrarK5U1nHW5z5SJ0i3R4LvtBJslDhvEk891lQtj9UeRI_2VTbYFMViKTrX6rcW818D3noxK2PuetNS1wsRFJe-M2KRGaSTx2-p5pextbLt-M2_CiR_f3t0cKSQbtrlyI0t-aotxbCkF9A-cPJ78qO4ICqtIdYSxE_TtpeplFVJyezIyTMkhwIhqwrCtC4JsbJwOsmKDA9cYpGtMSpq_TxCeClAO-2m7-GUrxHTBE7zvKOy-tugEWwwakUlNd3t7tvXCjQa_bCj8rI78ucIB0a7oGDo5vEMTDUJTPIFH14-2i40pZt8mlVWSAd94DmKInx8YqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46299f1ae8.mp4?token=YTuKdcBljWIVO4PWMrarK5U1nHW5z5SJ0i3R4LvtBJslDhvEk891lQtj9UeRI_2VTbYFMViKTrX6rcW818D3noxK2PuetNS1wsRFJe-M2KRGaSTx2-p5pextbLt-M2_CiR_f3t0cKSQbtrlyI0t-aotxbCkF9A-cPJ78qO4ICqtIdYSxE_TtpeplFVJyezIyTMkhwIhqwrCtC4JsbJwOsmKDA9cYpGtMSpq_TxCeClAO-2m7-GUrxHTBE7zvKOy-tugEWwwakUlNd3t7tvXCjQa_bCj8rI78ucIB0a7oGDo5vEMTDUJTPIFH14-2i40pZt8mlVWSAd94DmKInx8YqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی افکار ناخوشایند میاد سراغمون‌، چیکار کنیم؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/674437" target="_blank">📅 12:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674436">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
زمین‌لرزه‌ای به بزرگی ۴.۱ ریشتر شهرستان ممسنی در استان فارس را لرزاند.
🔹
سردار رادان: تردد زائران در مرزها روان است.
🔹
با تصمیم مربی استقلال این تیم به اردوی خارجی پیش فصل نخواهد رفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/674436" target="_blank">📅 12:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674430">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ff57370b.mp4?token=IEhKxqIHPg59QKo_UNcv5EPaQVOfD317LXWiNbwNPSl4xReHxeyggVpCa5humCYoEsFafjxcWBpFTRolWUjDHCmbdIjL_XNsBTFMjOaHFTjJh2Wh3eug-2bEYe7-ETkmpzqwW1ebD1SAtNxm0gCAHRXzct4BZzBvx7GgPAbl1jhnq2D0ZJn2JQezn8DZ5ikBAIbIE8EsPhX0vLPKNgj_EZoTkmF3P1cBESZbs4ZBoKQZIYjQ_UfiE4HxnUiJpH9zSPnMjSiOpDhl6v4-IOkyvm73qADCdtBJcQYUk4ZvosCZcEQN1ptqbdzadM1A6DOghmTuJYqcxJQlWlQFgjh4jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ff57370b.mp4?token=IEhKxqIHPg59QKo_UNcv5EPaQVOfD317LXWiNbwNPSl4xReHxeyggVpCa5humCYoEsFafjxcWBpFTRolWUjDHCmbdIjL_XNsBTFMjOaHFTjJh2Wh3eug-2bEYe7-ETkmpzqwW1ebD1SAtNxm0gCAHRXzct4BZzBvx7GgPAbl1jhnq2D0ZJn2JQezn8DZ5ikBAIbIE8EsPhX0vLPKNgj_EZoTkmF3P1cBESZbs4ZBoKQZIYjQ_UfiE4HxnUiJpH9zSPnMjSiOpDhl6v4-IOkyvm73qADCdtBJcQYUk4ZvosCZcEQN1ptqbdzadM1A6DOghmTuJYqcxJQlWlQFgjh4jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از کامیون‌های الکتریکی خودران چین، که ظاهر عجیب آنان در فضای مجازی پر بازدید شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/674430" target="_blank">📅 12:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674429">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
رایزنی پاکستان با عربستان درباره تنگه هرمز
شهباز شریف:
🔹
ضمن رایزنی درباره وضعیت تنگه هرمز حملات یمن به تانکرهای عربستان سعودی را محکوم می‌کنیم و در این برهه حساس، قاطعانه در کنار عربستان سعودی ایستاده‌‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/674429" target="_blank">📅 12:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674428">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
برخی منابع خبری عربی از شنیده شدن صدای انفجار در قطر و اردن خبر می‌دهند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/674428" target="_blank">📅 12:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674427">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه در واکنش به تهدیدهای مقامات آمریکایی: هیات‌حاکمه آمریکا در حال عادی‌سازی جنایات جنگی است
بقایی:
🔹
سیاستی که نابودی پل‌ها و نیروگاه‌ها را تجویز می‌کند، آشکارا غیرقانونی و جنایتکارانه است. این سیاست مصداق تلافی‌جویی و مجازات دسته‌جمعی است.
🔹
اقداماتی که هر دو به صراحت به عنوان جنایت جنگی در حقوق بین‌الملل و حقوق داخلی آمریکا ممنوع شده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/674427" target="_blank">📅 12:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674426">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a6e60fc55.mp4?token=TRWJLhLKD6mi1-2yoWbay5anmBq2PEgp9ap8YvDmjKwytTMlwRPXTVMob0KASxpSB__sJVYoy1KIUbjK0w0MB70a2e-IAUhXYAv3WOaBqQVDDEU_du-oKp0V5qv5EcFqOKrzRdZvYzGVDAqp-Q5QYj_2aaeRHCQxhQfQXt6jRiwh4AvHn5IsL-n-mMFgJhnIgsUTd_2dp7-MTNor5vDR897J8OLCok1UZWFcM0AuN9fol0T0SNHJp0EkwVbQsdR3KnR40KoLn2sCFEf67DbSD5aZGWUW2MIlgJSsSNMGUbXJsezmhCseBndhTTyLSmR2BYgDMEDT_Dnpux_948duzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a6e60fc55.mp4?token=TRWJLhLKD6mi1-2yoWbay5anmBq2PEgp9ap8YvDmjKwytTMlwRPXTVMob0KASxpSB__sJVYoy1KIUbjK0w0MB70a2e-IAUhXYAv3WOaBqQVDDEU_du-oKp0V5qv5EcFqOKrzRdZvYzGVDAqp-Q5QYj_2aaeRHCQxhQfQXt6jRiwh4AvHn5IsL-n-mMFgJhnIgsUTd_2dp7-MTNor5vDR897J8OLCok1UZWFcM0AuN9fol0T0SNHJp0EkwVbQsdR3KnR40KoLn2sCFEf67DbSD5aZGWUW2MIlgJSsSNMGUbXJsezmhCseBndhTTyLSmR2BYgDMEDT_Dnpux_948duzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخست‌وزیر عراق عازم تهران شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/674426" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674425">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vw2l2Asha4Nn0xWS81J6NM-FidrfYsJe4KnENeCKCDma-drlYQtXZzxciTSlxT2MdJmt4fwNtha8OSdxGdkITctyeoM2aecCe9HZ5Wp-weEdxuC3AqlaQDj29VmMK243PJ-uxqKbjsqkUTVefiu8GA3gsYsJWzBDMbOZn2ouCgcFbIVCmZjRY9jZkAB51JVox9vVWpHhgTGhSHi4IyK5ovjlIxBeB_SzbhoDhMR9RBy_fnKk29ke_UGTPCaSkwXyDQg5iz7uXAFm806gVCXfDme1ngMQyjpa3Wg_QbCnhuUNBOyDGCLbQ8M3--yczSZVudOKeX89W3wutaeZYp42pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فاکس نیوز : ایران جبهه جدیدی گشود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/674425" target="_blank">📅 11:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674424">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rv4OCNGZGK9s3XpCp5utG6rbWqXMz9knCpLwoFZGOSQPh1HX5mYaMpvT1EIaf1soeKaA2xZms5jKDBGtLjW_sC1gkf91WOIsSqu7ai7Ppfp3NdviDtNm46dIta0ncDAyM1Hky-zSGLT6waowUPELhNJ6QHW4XZiEXW6An7FOtUsX3gSZPKrvwuhdRle6gpXSzEZBezukFN66tvzt9id624UuhabQfANBqUbZi1FeP2iu-dt3pGIy5kMb7JNcFDEDZKMs1iIHmbpWZZ6-SdwQ6QRycNbtZdulCI-Z_fc2sFpLfAIzoWnmr1PZuHsurwVuiO61Yn-xfhQaBPMjqYk7nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مگاتخفیف
سوپرمارکت
۴۵دقیقه‌ای دیجی‌کالا
شروع شد!
🔥
🎁
کد تخفیف
۵۰۰ هزار تومانی
➗
تا۷۰٪ تخفیف
روی کالاهای شگفت‌انگیز
🚚
همراه با
ارسال رایگان
امروز از محصولات سوپرمارکتی، شیرینی و تنقلات تا پروتئین و میوه رو با تخفیف‌های ویژه سفارش بده!
🫂
کد تخفیف ۵۰۰ هزارتومانی ویژه کاربر جدید:
6TFG
🫂
۳۰۰ هزارتومان ویژه کاربران قدیمی
(۳ کد ۱۰۰ تومانی):
GD33
فقط امروز
⏰
بزن بریم خرید سر ماه در دیجی‌کالا
👇
dgka.me/Wcjhnscdl
dgka.me/Wcjhnscdl</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/674424" target="_blank">📅 11:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674423">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
سخنگوی ارتش: سناریوهای تازه‌ای برای تقابل با دشمن پیش‌بینی شده است
امیر اکرمی‌نیا:
🔹
حملات تلافی‌جویانه نیروهای مسلح تا زمانیکه حملات آمریکا علیه زیرساخت‌ها و مناطق ساحلی کشور ادامه داشته باشد، ادامه خواهد داشت.
🔹
ارتش جمهوری اسلامی ایران از فرصت آتش‌بس برای ارتقای توان رزم نهایت استفاده را برد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/674423" target="_blank">📅 11:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674422">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39a6ab9006.mp4?token=aQyJvp08619Wbd3RAVGFSJApwCFib5gftY2VQztlX6nK1Ut-yGWJY4Q2Q_6N00OxqQDFNAznDSOeaSgF4UcD7Q2_DOUDDwU6qrKgbxana2vY_ONO0QeQoBjD8qeRI8hPsL21QDalBzN6ubMWKts0NZt8ZneAyLsN9ZvXZ-kaUZnwO4gr74EbO-NBe2MgeMsRyVwaFSOKY04FPtyy5qg6DlQy2r9x8lVyhMHqGt7JzXnstNzYce5XWC5ebUrwpmX_YoQG1samA2LCTFS29fuzb_pVkpwzlmvQqAkvH-qFbIwfeL2WwB2OpOxNTVLtbiFxYETqht5W8Z_a1y5W6f-GIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39a6ab9006.mp4?token=aQyJvp08619Wbd3RAVGFSJApwCFib5gftY2VQztlX6nK1Ut-yGWJY4Q2Q_6N00OxqQDFNAznDSOeaSgF4UcD7Q2_DOUDDwU6qrKgbxana2vY_ONO0QeQoBjD8qeRI8hPsL21QDalBzN6ubMWKts0NZt8ZneAyLsN9ZvXZ-kaUZnwO4gr74EbO-NBe2MgeMsRyVwaFSOKY04FPtyy5qg6DlQy2r9x8lVyhMHqGt7JzXnstNzYce5XWC5ebUrwpmX_YoQG1samA2LCTFS29fuzb_pVkpwzlmvQqAkvH-qFbIwfeL2WwB2OpOxNTVLtbiFxYETqht5W8Z_a1y5W6f-GIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رویدادی عجیب در جاده‌های مصر‌؛ راننده کامیونی خودرویی دیگر را از سقوط نجات داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/674422" target="_blank">📅 11:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674421">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1m_AajaULewTr7VDZ-xu4WECnDwo6X0dV82aqfR4lTvCDglytaIk3NOg-FijTO2wmGppKURTu0QnhLVtWqi7rOxS_1mW62ZGOH96Gsc3P6qyyaoS1w98KG3Y0q4n-KmN36y4lBHG7aieGybe1Xd5kMUeQ956y15MuOrDgiEXKuqYsN2aMagSec0bdjHCjkxrm83qlLPEnln8yyn8OHU-JR2BjOhPHYfQmuNspyRMs7ZW96EKpmyzVi1Kvdu3PGGYxGevBy_IaYyC9LtOpAc2eLTlg4VG7tYbmfjXth9oXHXWcyFvcBCo8Yqg19kbQ6tn1XyzhPpb-mH3yCkBw7K8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفت خام برنت همچنان به پرواز خود ادامه می دهد و به ۹۸ دلار در هر بشکه رسیده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/674421" target="_blank">📅 11:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674420">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در محدوده شهرستان کنارک
🔹
براساس گزارش‌هاامروز یکم مرداد ماه صدای چند انفجار در محدوده شهرستان کنارک به گوش رسید.
‌
🔹
تاکنون جزئیات رسمی درباره این انفجار و منشأ آن و میزان خسارات احتمالی اعلام نشده و بررسی‌های میدانی و کارشناسی در این زمینه ادامه دارد.‌ / تسنیم
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/674420" target="_blank">📅 11:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674419">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3YcUwi5f1roN7pLxpY4xdqQ88uUkidmlGZZgw7XDQKWsiwfczUbh6qZAvPCXasR2cho2867NNrjIJFUWqpQ5hyVizwF58B6RGHFMurxzZ7RojCtKLvrU1AGZcKOTuPM9bhnNztCgDtwuDzepAEK7t2ngGRs7HsVoLEm0prqTSReCSIx-erKwepDdC5BzmEBOzwH1wHW1JwFSfTKfkeJkptGDmcrkxrp5fDd3sj2kJS9uXAp19LUei2K-ZpuWLUm0zAGjMh3elJsAorbXxJ_me1sVnyTngeBte7xGdQNtw6B8dLeldLpR8eKVAYNGNvDWosC12KCFPyagYFmp3ABXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میانگین قیمت موتور در ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/674419" target="_blank">📅 11:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674418">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای اکسیوس: به گفته منابع آگاه، میانجی‌های قطری همچنان با مقام‌های آمریکا، ایران و عمان در حال رایزنی هستند تا به توافقی جدید برای بازگشایی تنگه هرمز و توقف درگیری‌ها دست یابند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/674418" target="_blank">📅 11:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674417">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
احتمال جاری شدن سیلاب در ۴ استان جنوبی کشور
سخنگوی سازمان مدیریت بحران کشور:
🔹
پیرو هشدار سطح نارنجی سازمان هواشناسی کشور احتمال رگبار شدید باران، رعد و برق، خیرش گردوخاک و وزش باد شدید در استان‌های سیستان و بلوچستان، هرمزگان، فارس و کرمان وجود دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/674417" target="_blank">📅 11:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674416">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac176b643d.mp4?token=iZuxxVPr9Aat6cy6q96rf6iCvxDz1BMpRGmdiy9sMKZ97gGfx7mORECVoAEe76SaqUyoFx02uak_f--eOXs1RdAEdbX84M9wJRx_TY-3krEmHtnQyS93ypbxrGTGvZA_1VJyOwWVxgfNPhreshD_dF_v8-_QXXR94AzZQLDoAILAHvB__8v3ywhL_FPoCaVLxhAkAgfAygXUq0OhGnwOVpRbRvlhS2nhN7rRg32mXhzUE9KhXKkXmcBBSoVzZdQwwzAusr5YflQ8UuRUixY7rI9Nk3gwCU6DWN4GRPmcd1p8C-ACfVYXiOSIQfyiV7lcJ89SvmezAuQ6ixX4b_YDkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac176b643d.mp4?token=iZuxxVPr9Aat6cy6q96rf6iCvxDz1BMpRGmdiy9sMKZ97gGfx7mORECVoAEe76SaqUyoFx02uak_f--eOXs1RdAEdbX84M9wJRx_TY-3krEmHtnQyS93ypbxrGTGvZA_1VJyOwWVxgfNPhreshD_dF_v8-_QXXR94AzZQLDoAILAHvB__8v3ywhL_FPoCaVLxhAkAgfAygXUq0OhGnwOVpRbRvlhS2nhN7rRg32mXhzUE9KhXKkXmcBBSoVzZdQwwzAusr5YflQ8UuRUixY7rI9Nk3gwCU6DWN4GRPmcd1p8C-ACfVYXiOSIQfyiV7lcJ89SvmezAuQ6ixX4b_YDkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طراحی خیره کننده Z Fold 8 ؛ گوشی تاشویی که نظر همه را به خود جلب کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/674416" target="_blank">📅 11:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674415">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad3f584299.mp4?token=fAmThZYTId1P3h-zdNvsi-LbsH8-T0x4m10OPqw-k3cKqKxKRGosMySnf8216L1O0L70ZCKagUccCxw0bKlNFqb1dTXUbXm7SDj_JAP63yMBHe4obNbl7k--d8TbidqqiwMw5IJoEv6aH0saPYTcpsPs-vPa6-v6Ha0YFjCu4hMqL5TeVVHHNnfi4fKBcqasbu7pP8EdodVAtdrgEBQod-nSmunjZ3JDEXo4Z2SJaqgL90hZzcFQQiGzzQkpjHMABQNbTP0l-sZojMnJVY7Ghp9y0doV7IYOmOpJEqp7vR22gdvFaqKFy_s8I5tc39aII5YDIO-UC0qvz0YVeRnstQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad3f584299.mp4?token=fAmThZYTId1P3h-zdNvsi-LbsH8-T0x4m10OPqw-k3cKqKxKRGosMySnf8216L1O0L70ZCKagUccCxw0bKlNFqb1dTXUbXm7SDj_JAP63yMBHe4obNbl7k--d8TbidqqiwMw5IJoEv6aH0saPYTcpsPs-vPa6-v6Ha0YFjCu4hMqL5TeVVHHNnfi4fKBcqasbu7pP8EdodVAtdrgEBQod-nSmunjZ3JDEXo4Z2SJaqgL90hZzcFQQiGzzQkpjHMABQNbTP0l-sZojMnJVY7Ghp9y0doV7IYOmOpJEqp7vR22gdvFaqKFy_s8I5tc39aII5YDIO-UC0qvz0YVeRnstQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رویدادی عجیب در سخنرانی خوک هار؛ تقلید همزمان!
🔹
مردی که پشت سر ترامپ نشسته بود، با تقلید دقیق حرکات، حالات چهره و حتی جملات او، به سوژه داغ رسانه‌ها و شبکه‌های اجتماعی تبدیل شد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/674415" target="_blank">📅 11:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674414">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0b85691a.mp4?token=kjoPeXtqclVoZPw8U6sh2bD_LmkjTroJPCWlVGWW9Gk5fXzzBbAWr2maMxx0J9q0I2QjB4Ab9jmx4BluKr219M142tMLfl3ckc4RRjgArECQFqlTP0oVbhgfRBN03mB4GOOdOQjk_2aT0xd73Vv3T1iyjlt21kIrkfveHcZamVw9SFehpGh2PrS2z3897ILJHzwcSeUGAjXZzJ5GAhiW01noBu4a6J8ru-OYUpzBpymgqWoZ-q8yCYbXdaspjC4yyogXoEtRF4coPyn7X8qvhAxCf4Z8NMV6ZQ9lCHj7X4YwLWbakJasI33sZW649Iv785DIEoHsnhfnSWGRPpn_Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0b85691a.mp4?token=kjoPeXtqclVoZPw8U6sh2bD_LmkjTroJPCWlVGWW9Gk5fXzzBbAWr2maMxx0J9q0I2QjB4Ab9jmx4BluKr219M142tMLfl3ckc4RRjgArECQFqlTP0oVbhgfRBN03mB4GOOdOQjk_2aT0xd73Vv3T1iyjlt21kIrkfveHcZamVw9SFehpGh2PrS2z3897ILJHzwcSeUGAjXZzJ5GAhiW01noBu4a6J8ru-OYUpzBpymgqWoZ-q8yCYbXdaspjC4yyogXoEtRF4coPyn7X8qvhAxCf4Z8NMV6ZQ9lCHj7X4YwLWbakJasI33sZW649Iv785DIEoHsnhfnSWGRPpn_Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر نفتکش عربستانی که دیشب توسط یمن زده شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/674414" target="_blank">📅 11:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674413">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
برخی منابع خبری عربی از شنیده شدن صدای انفجار در قطر و اردن خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/674413" target="_blank">📅 11:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674412">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_ghM3wLM6cbzC4L-XYiN3uhzZUtjnUlysZSsvWAPrRpUhMzEbzEom9npGTXveUTs15vZelGyZjvRBHLLgb22YAjd5K0RcJxVcxFYeBjdu7uT52_IV4g_R8CssXicY6qE0N4_Zy7C36Mz1KP0bs5qrOMa5q0AxI1lANC7FfA4O3LaFDbYg-yE63-d8ZyTXCLHDCV-_zDW-LhyvxDCbYlq4sBNQen7YTQlDKfkqDsYbPWrE5HPq3FZrR1Jz--KyqaQNupsheLhtHeFlUwISDceY3dYqLl_8BMJbrW0aMEcPOHTU7-QERUXaQtmucOg_BdiUBvqG1A8JbIi-JZPPCfaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افزایش قیمت نفت به بیش از ۹۷ دلار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/674412" target="_blank">📅 11:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674411">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
چندین موشک از مناطق مختلف کشور به سمت پایگاه های آمریکایی شلیک شدند‌ /
صابرین نیوز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/674411" target="_blank">📅 11:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674410">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiS0UuV3IEhcw5QFAIY1A2PdshRySWk3lIKAZk8XTh8Kpjv1JiRyh6RHrXcWvpNFM5WhGBcPB8ftKX5Udruvbu2P-_srAH288YE8jNcyA_-Dga8MNEoEZG4Has5YQmoU0voNKy7gC8gqHuxnG_v5pKFn_3hEqAxw_uR9o35cv5q45R-xP_h-0iwZWhfgkjfo1IyPhXwmAN28TmOzj00VAcI1MOMdAIcCYoUKxwq7l0kBmcxAod6pHG_Je2IBhC17GFWjimmTf_Hxb0n_Ee2nixVXhVSHP_uA_N2HqSOgQr9KRce71B6yN9wyAJrKiu8Yndi8Knjr3MObmCDoQ7imag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخست‌وزیر عراق عازم تهران شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/674410" target="_blank">📅 11:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674409">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f44763d92.mp4?token=VprS8z-lDLZ_XvQs6bIDu9TK_WvUjDhsJql18CQH2x-rqQjbp5E4embFfc-w0l71C4S9ekq_pvdAKuEdg7tf5pnRPjUvAIL97meynlcjR_HHSX3KYxdVHBI-2hbQPeigYqsa4Q5y3HB1pZG3nOi-iHBqqQgIlz4x6HiTFz4Mih6i3Ak_ZQHcbbJTyDQFtQXdwrSd4fFpG6_OlfS4CzNxzzH4RHiaxJx74HEzIH8EXt7UrOoFhu6vj5cdLA8bbtNGSUb_7k0TYu1PiFVgSNmd9uToLJvti2Hibzg8Tt2k3ky4NfiKx-CrltfNaptYTRpZJ5IjCv08YiFV0cmyORPMMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f44763d92.mp4?token=VprS8z-lDLZ_XvQs6bIDu9TK_WvUjDhsJql18CQH2x-rqQjbp5E4embFfc-w0l71C4S9ekq_pvdAKuEdg7tf5pnRPjUvAIL97meynlcjR_HHSX3KYxdVHBI-2hbQPeigYqsa4Q5y3HB1pZG3nOi-iHBqqQgIlz4x6HiTFz4Mih6i3Ak_ZQHcbbJTyDQFtQXdwrSd4fFpG6_OlfS4CzNxzzH4RHiaxJx74HEzIH8EXt7UrOoFhu6vj5cdLA8bbtNGSUb_7k0TYu1PiFVgSNmd9uToLJvti2Hibzg8Tt2k3ky4NfiKx-CrltfNaptYTRpZJ5IjCv08YiFV0cmyORPMMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاويرى از آتش‌سوزی در پایگاه علی‌السالم کویت پس از حمله ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/674409" target="_blank">📅 10:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674408">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر نیرو: نخستین نیروگاه گرمایی ایران به شبکه برق کشور متصل شد.
🔹
سازمان هواپیمایی کشور: فروش خارج از شبکه و دریافت هزینه اضافی برای پرواز های اربعین ممنوع است.
🔹
رزمایش دو روزه چین با مهمات جنگی در تنگه تایوان آغاز شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/674408" target="_blank">📅 10:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674407">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
سازمان راهداری و حمل‌ونقل جاده‌ای اعلام کرد: زائران اربعین استان‌های تهران، قم و اصفهان می‌توانند بلیت سفر برگشت خود از مرز مهران را از طریق سامانه سپاس و به نشانی
sepas.rmto.ir
تهیه نمایند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/674407" target="_blank">📅 10:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674406">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSLdcWx1XgSN2SNdn5d9VY7uOlIE-JDU92D0IiEEMlqxQGvRT-Vk9IFG2lqYtqc47Pn5lW-vwva7FlzLTatkLUeoZ1JUdjWLJh-aCiFmCbXV1S-PSBizVKn4-nEnxtS19CVhl8ygzu1TJki2tt6cZvZw5pj6ql7I-Z0OHo3vrh3oiC_BqeB6oOV7m0A0dReuFib19_63x_6L8MOP-t_rFqBScSLOI5_twtQ9blILiPe2xrAR3EmFGYk_eOJ89Fial52-UIwpBJY4WwWlAIk43wQxT0v0jlM9At6RYYkNeyNLsyJKGv3CfezJHz-emlIYAupmeIoYXRjwX9MHJsE4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قرعه‌کشی بازی‌های آسیایی ۲۰۲۶؛ رویارویی تیم ملی امید ایران با چین، امارات و کره‌شمالی در گروه B
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/674406" target="_blank">📅 10:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674405">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWaVUgGnIpNBjy_u_koCD1nQ81LGsJVtiIytlQVGgKWD7kgeNRLz8ip1nIx_Xr7cgrUCP49B2AEe38pZbJU03AsTKHPDsfw0SIC1VRqRlLHidNs616uwOXTIHvyGUYjRDJMlk6_IBNmqGRiUkJwxc_c24MoZ_ENh4qMklj3OsWXouTJp5hD0noFRf5BHCAG_1a1ZbGml6_29i7NKm7tWA8jG1w_c83s8qFt3HarABkNIedkHzE3XjkEppaGl1H0328kqM0dWbVIqUxfdEaWeReTKJHWy9DxQDkRanJ38Do3aUgMVByrPtURfeYwBtucbjeyzZpiWi0Gi6_sSLr7ItA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۳ توصیه پلیسی-حقوقی برای سفری ایمن در اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/674405" target="_blank">📅 10:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674404">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
رسانه، جنگ روایت‌ها و دستی که نباید بسته شود
مصطفی انتظاری هروی مدیرمسئول خبرفوری:
🔹
در روزهای اخیر برخی همراهان و مخاطبان خبرفوری در پلتفرم‌های داخلی درباره عدم انتشار محتوا در کانال‌های خبرفوری در بسترهای ایرانی پرسش می‌کنند.
🔹
آنها می‌پرسند چطور ۸ سال پس از آنکه خبرفوری با حضور در بسترهای داخلی که آن زمان تازه شکل گرفته و در رقابت با پلتفرم‌های مشابه خارجی بدون مخاطب بودند، با وجود همه فشارها و جوسازی ها، به این پلتفرمها از حیث فعالیت رسانه‌ای معنا داد، امروز همان حضور معنابخش به خاموشی گراییده و با بستن سکوهای انتشار خبرفوری در پیامرسان‌های داخلی، این ظرفیت‌ها را به محیطی ناامن برای رشد رسانه بدل ساخته است؟
🔹
البته احتمالا پاسخ برای آنها روشن است اما از سر شگفتی می‌پرسند چرا در میانه جنگی که بخش بزرگی از آن بر سر روایتهاست، چنین سکوت کرده‌اید؟ آیا این سکوت به سود دشمن آمریکایی و صهیونیستی و جریان نفوذ داخلی وابسته به آن نیست؟ آیا این سکوت به زیان نهادهای رسمی داخل کشور نیست که برای ارتباط با مردم از کانالهای خبرفوری به طور لحظه‌ای استفاده می‌کنند؟
🔹
ما به‌عنوان بزرگترین رسانه کشور که بدون هرگونه وابستگی در ۱۱ سال گذشته فعالیت کرده و براساس وظیفه و تکلیف، از کشور در تمام فراز و فرودهای داخلی و خارجی دفاع کرده‌ایم و هزینه آن را پرداخت کرده‌ایم، تمام تلاش خود را می‌کنیم که همچنان صدای مردم و راوی روایت حق و‌عدالت باشیم.
🔹
اما این تلاش نیاز به بسترسازی دستگاه‌های مسئول و نظارتی نیز دارد که امیدواریم با درک شرایط کشور و در اوج تجاوز بیگانه به مرزهای فکری و جغرافیایی ایران بزرگ، با سعه صدر و درک عمیق‌تری از واقعیت‌های موجود، دست رسانه‌های داخلی را در رویارویی با امپراطوری دروغ تحت کنترل دشمن متجاوز، نبندند.
🔹
خبرفوری در این ۱۱ ساله ناملایمات بسیاری دیده و به عنوان رسانه‌ای جوان و مستقل تجربه های گاها دردناکی را از سر گذرانده و این بار هم با درایت نهادهای عالی کشور به ویژه دستگاه قضایی و تدبیر همیشگی شخص رئیس دستگاه قضا که شناختی ریشه‌دار از نقش رسانه در تحقق عدالت در کشور دارند، به مخاطبان وفادار خود بازخواهد گشت چراکه دود تصمیم به بستن صدای رسانه‌های حامی عدالت، به چشم همه ارکان عدالت‌طلب خواهد رفت و پدافند رسانه‌ای ایران در برابر دروغ‌پردازی خارجی و فساد و نفوذ داخلی را در این دوره حساس دچار آسیب می‌کند.
🔹
ما بر این باوریم که کسی اجازه نخواهد داد در میانه جنگ نظامی - رسانه‌ای، صدای بزرگترین رسانه کشور در بسترهای مجازی وطن خود، خاموش شود. ان‌شاالله...
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/674404" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674403">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puWNknxOYm46kpvkX5q4obE-t-kSzV9nitjYRA_5s8dE0LkiQX4jOT6CLVUZ5vD3112xXX3QbRFoZQpKq7eFRHRSGoJw8DyCJ4ABlXUgyY6F_I59f2vP_-ilpsBlZ9FNS20v4IgTTp7a9EKpEW5VR-ALtR1uo9aHnm_UQ7x4f2xHptxg5JtyZkKFFm1fyY0oHTDtKb1aq52JunznD7gVP8CLOVNqtsMBa7RCkExJHxT1UGbAz6-bREcqew0nS_qH6bcOyHO9ecs75ao3XFRMVFs5eVEGgDxxScJsjjXPay5ptt_XAt0utfO11UGJOqfl2NAk7U3YB4Kk6T8IimFB1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش آزیتا ترکاشوند به حمله دشمن به مرز شلمچه
🔹
تاریخ در حال تکرار است یزید زمان به زائرین کربلا حمله کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/674403" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674402">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JG54JOoJfPrTXhO7X5YpsiXsvceiBHBSndWretj8SEIMAgIpCl4Z5ViTVkTi3ihBBziX7nDegAEfDI5xRoVpCONMOz1v8cRcEY_yiRakUiSJG9aDEYHUh-IVSMKd1QELefefJ6x_T7sDr2NTr33MaxqwvU4NIQsA5QbjbAJmg7K_XRDQqL75WfMni5N5s4IqF9coFBUiQVxgGVAkdYBAvT5z-f67WBzXMd3q7QNKwoHnYwRiWhP5iK2KAkISiOEnfBi4ZVJTdD6hymBAUmE_VPIIy0XGlyePIGTt5c5e9yBcTNjL8EKLmeYqD0KBJZ0C3jUepLcy146hpDgQcUmdeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کوهسنگی مقصد شادی کودکان
🔹
اگر دوست دارید فرزندتان اولین تجربه حضور در نسل سوم زمین بازی کودکان را داشته باشد، این دعوت را از دست ندهید.
🔹
در بوستان کوهسنگی، با افتتاح یکی از مدرن‌ترین زمین‌های بازی کودکان کشور، شبی پر از شور، هیجان و خاطره را کنار هم رقم می‌زنیم.
🔹
همراه با ، قرعه‌کشی و اهدای جوایز ویژه به کودکان
📍
بوستان کوهسنگی
🕗
پنج شنبه ۱ مرداد  | ساعت ۲۰
منتظر حضور و  لبخندهای کودکان شما هستیم.
💚
🌳
🎁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/674402" target="_blank">📅 10:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674401">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_bHCP7GGYxSQDw3PR-N96-y8_QhU-r6qWNy53WKJF7VOOKCgXD7RHLznyJYYAv3Gk48nDmW2-d-cywFXhwUA-GIu5mkYMJl5Dwdrlg1nh8uXMnMxeUq4ydzm0Y1SqZHWwAZk1PAuFmUc6KFtQn-Pc0vp_gAd-0wKa6-0LOZcSpujphOp21cgDOvQjQqAg1Rh3BQ_9uZf1SZLDQusL34e09ttUHEfXHYkGvanlPJXw34mT1e_U6EiJCReH6aYRZjd8F6kNIfQz9lukdZa9H7M1mMG5NBoSdaWV_1kfg-76eMWYrsn1iT_aa9XfMT2IDSFzmSKAjbDX4a0oDEg91stQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصاویر ۴ سرباز به هلاکت رسیده جدید آمریکا در جنگ با ایران
سی‌بی‌اس:
🔹
یک سرباز ۳۰ ساله آمریکایی آخر هفته در عراق در جریان آنچه آمریکا انفجار کنترل‌ شده برای انهدام یک پهپاد تهاجمی اعلام کرد، به درک واصل شد.
🔹
پنتاگون اعلام کرد گروهبان مایکل امانوئل سوینتون «در حین عملیات انفجار کنترل‌شده» پهپاد در پایگاه هوایی اربیل در شمال عراق به درک واصل شده است.
🔹
سرباز سومی هم که پیش از این مفقودالاثر بودنش در پایگاه هوایی اردن تایید شده بود، اکنون گمان می‌رود که به هلاکت رسیده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/674401" target="_blank">📅 10:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674400">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130fef3d83.mp4?token=STx2WOtlCmPNjabSegW6PlP4b4Z7bMg_Ff_Vgo7H6qj-FbtWFSDeWudQI7ye64sN6J0aO4pihunBK5YJh4Y61Wapv1iL95sygmViRXs1zLtkzvccFQA1eSQhx5h71k30ERseNIpMisgzbgkNsHk9gQ9pYMnZ4_Bc8plMYQ1zEOH4Ee7YKw22Qt1uLj5FHldVVpYMiKbx46AK2mEn-muxS5xOJM8nY2fLO6XFogkEPAewqPSTty2_tiFTNWaM7-oNEA6ssVykc5ygSHw9EoXfDCaqd4VpxgwAu36QYcVqkRnqlHodtTptIdkZq40GKFlIeiLB6ga20K696k26aQrGRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130fef3d83.mp4?token=STx2WOtlCmPNjabSegW6PlP4b4Z7bMg_Ff_Vgo7H6qj-FbtWFSDeWudQI7ye64sN6J0aO4pihunBK5YJh4Y61Wapv1iL95sygmViRXs1zLtkzvccFQA1eSQhx5h71k30ERseNIpMisgzbgkNsHk9gQ9pYMnZ4_Bc8plMYQ1zEOH4Ee7YKw22Qt1uLj5FHldVVpYMiKbx46AK2mEn-muxS5xOJM8nY2fLO6XFogkEPAewqPSTty2_tiFTNWaM7-oNEA6ssVykc5ygSHw9EoXfDCaqd4VpxgwAu36QYcVqkRnqlHodtTptIdkZq40GKFlIeiLB6ga20K696k26aQrGRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
این راتاتویی رو‌ به سبک موش‌سرآشپز درست کن
🐭
مواد لازم:
🔹
بادمجان ۲عدد
🔹
کدو زرد ۲ عدد
🔹
کدو سبز ۲عدد
🔹
گوجه فرنگی ۴عدد
🔹
فلفل دلمه‌ای ۱عدد
🔹
پیاز ۱عدد
🔹
سیر ۳حبه
🔹
روغن زیتون ۴قاشق غذاخوری
🔹
آویشن خشک ۱قاشق چای‌خوری
🔹
نمک‌و فلفل به مقدار لازم #آشپزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/674400" target="_blank">📅 10:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674399">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه خیریه مهرمبین</strong></div>
<div class="tg-text">🔶
فراخوان کمک برای مادر مبتلا به سرطان سینه
🔸
این مادر که سه فرزند خردسال دارد، سرطان سینه دارد و جراحی انجام داده است.
🔸
16 جلسه شیمی درمانی نیاز دارد و 25 جلسه پرتو درمانی که هزینه آن بالغ بر 500 میلیون تومان می شود .
❤️
هر کمک شما، امیدی تازه است.لطفا این پیام را برای دوستانتان ارسال نمایید.
شماره کارت خیریه مهر مبین:
6063737004808968
شماره شبای مهرمبین:
IR820600260201108691003001
پرداخت آنلاین و اطلاعات بیشتر:
https://mehremobin.org/help/
📢
گزارش کمک‌ها را در تنها در کانال خیریه ببینید:
💖
@mehremobinn</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/674399" target="_blank">📅 10:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674397">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f4172d4b5.mp4?token=jt8LBPMHZNGRKksCMjVKktIVKt75T0ulM1Ed8tvvL5ZlJ8XMbgNoKiFpMHDrO16L7yWD1l9vcJULkir2NonQqfK-IFulHZPtbTJKsFToK13xbOZOiyQj-Hs1vcVX1thk-XLLXrbvVYdP2idIf_1Zo9ts5x0a3GZCm9StS565K-eaPofDQFYwZdmHsvzc9pNNPfUBdfWj9govhNU7x_Z7_nX5tDHc72TrMespVbIHOABQgaahsZpvA1qBVvD06Gr9O-ElQp8lMw_qxBD3kArZAJPbq4nYUaG4x_c4fuYGzfeRqF_YMH3EYGek0MAQlV8KYGw5qsq6uaZqNdvjYN0i5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f4172d4b5.mp4?token=jt8LBPMHZNGRKksCMjVKktIVKt75T0ulM1Ed8tvvL5ZlJ8XMbgNoKiFpMHDrO16L7yWD1l9vcJULkir2NonQqfK-IFulHZPtbTJKsFToK13xbOZOiyQj-Hs1vcVX1thk-XLLXrbvVYdP2idIf_1Zo9ts5x0a3GZCm9StS565K-eaPofDQFYwZdmHsvzc9pNNPfUBdfWj9govhNU7x_Z7_nX5tDHc72TrMespVbIHOABQgaahsZpvA1qBVvD06Gr9O-ElQp8lMw_qxBD3kArZAJPbq4nYUaG4x_c4fuYGzfeRqF_YMH3EYGek0MAQlV8KYGw5qsq6uaZqNdvjYN0i5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بشارتی الهی از رهبر شهید
اعلان کردن که نیروگاه هسته ای براش(دولت سعودی) می سازیم...
اگر بسازن هم بنده شخصا ناراحت نمی شم
چون می دانم در سالهای نه چندان دوری به دست مجاهدان اسلامی خواهد افتاد/ سال ۱۳۹۷</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/674397" target="_blank">📅 10:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674392">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNoZKSRa8tjBAjaiJUwVLJ07zZTzlrM8x5MLFWpbzX1ThE8R2eGYTwMVEK_3ntxXd2lmWesCzGM00Su19dTL_Uaw2dmkr2Djdvg1JvB3X5rj5SRZt4Jb8-d3NgQY332dduI73w1kpJ-WMmNaJctA8SmVg1EKr9mlHwq4LFN-udfnlMR1As2rDUyebz8hdKYcRURn4okhMVIm3dVge_yO9eepUIuxGNwn1qdKpEDtMn8R1wflBW2hIMFMsp3Tq5yEVI344GrIKRsH1jwDNVYmh71JbTMcEeOfENTszez2QJiaylX8oDQiKqKa10cVkPKbXuxESYhyB-oId6SjsAc0PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توصیه های غذایی؛ برای کسانی که کبد چرب دارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/674392" target="_blank">📅 09:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674391">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEpNtjmOFCmfPJ7JNO27dhWL_2BAlrpzKPstLlw8qF_6_DjEOvHfzOUdtc8X76wo1BFLMPY2xjoJV7wzp2ph8NGoth6oCUv6cmhWUbIjPtoEA0uaR1Zpqo-5YI7XYVF7CyNOjlu_vcbFvUiR1Hqupfvf4gFa9JoqOfR0ogA49N7Dgpr6TnnuyNH12TcryPB-62ADOpTE_vCuY3s76IrqxMpcf7IbjX6WM91Bqie4EqReG8wzzYe50GubwVal_3fi3uuSxC97_THdMCda6sR6QJ-fZmDlO6rN3fmIr-5yrIUp-P5qK-IjtmHyx-y1yw7zD3iIF3yQQzMlE5c5f-J_sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افشاگری تکان‌دهنده اسکای‌نیوز/ موشک درست وسط مدرسه میناب خورد/ در روز حمله یک گروه ضربت ناو هواپیمابر آمریکا در برد میناب بود
اسکای‌نیوز:
🔹
شواهد موجود نشان می‌دهد که یک گروه ضربت ناو هواپیمابر آمریکا در روز حمله به مدرسه در برد میناب بوده است.
🔹
مدرسه تنها ساختمان غیرنظامی نبود که مورد اصابت قرار گرفت، تحقیقات ما ۱۱ ساختمان مجاور را که در این حمله مورد اصابت قرار گرفته بودند، شناسایی کرد. موشک‌های تاماهاک آمریکا درست به وسط مدرسه، در سالن اجتماعات، برخورد کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/674391" target="_blank">📅 09:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674390">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a11234b2.mp4?token=uFQPd8zzdUPzhpMr5r2DF_1NXeXtiyd6TPGXA_Py_wzk0o8-1gA_3fnDtDvkOtLvwJKgZj5LO6Q0MySYC6tKBBk9NK5xj7TZW_X5hDNp5DezsN4q1ejMb4qVtA4IuuQSWsR_X3RNa2I6Aux9MHc4Ep43ynL3GLFA_HHRqyyylXoL0ad88U3GCYzK23cFsczbj_vSaRKLvIgapCFce1_xo9bON6GVh8oS8J50cHJRRA3r31uy1AjxRlHosbQqa0tlhSSoz7BEEfju1BpFU5OF3IrcXDF9yxp0XXAW2mRHScMVPoNYhh8ECaHqFWE-2xxVjpfdY-t1hbPaCxJCQ4WkWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a11234b2.mp4?token=uFQPd8zzdUPzhpMr5r2DF_1NXeXtiyd6TPGXA_Py_wzk0o8-1gA_3fnDtDvkOtLvwJKgZj5LO6Q0MySYC6tKBBk9NK5xj7TZW_X5hDNp5DezsN4q1ejMb4qVtA4IuuQSWsR_X3RNa2I6Aux9MHc4Ep43ynL3GLFA_HHRqyyylXoL0ad88U3GCYzK23cFsczbj_vSaRKLvIgapCFce1_xo9bON6GVh8oS8J50cHJRRA3r31uy1AjxRlHosbQqa0tlhSSoz7BEEfju1BpFU5OF3IrcXDF9yxp0XXAW2mRHScMVPoNYhh8ECaHqFWE-2xxVjpfdY-t1hbPaCxJCQ4WkWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وطن ای هستی من، شور و سرمستی من #همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/674390" target="_blank">📅 09:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674389">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
اکسیوس: آمریکا از یک بمب‌افکن B-1 برای حمله به ایران استفاده کرد
اکسیوس:
🔹
مقامات آمریکایی اعلام کردند که ارتش روز سه‌شنبه از یک بمب‌افکن دوربرد B-1 برای حمله به اهداف سپاه پاسداران در ایران استفاده کرد.
🔹
این اولین باری بود که ایالات متحده از زمان از سرگیری جنگ با ایران در ۱۲ روز پیش، یک ماموریت B-1 انجام می‌داد.
🔹
استفاده از بمب‌افکن‌های B-1 که می‌توانند دو جین بمب ۲۰۰۰ پوندی یا ده‌ها موشک کروز حمل کنند، نشان‌دهنده تشدید و گسترش قابل توجه کارزار نظامی ایالات متحده بود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/674389" target="_blank">📅 09:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674387">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brY1qrluMbqTF5JKqgIChOEWjEX7ddFGMGfoUMS_ufxMaHj7hPtMSQTcXxr8YOQwRnz9c4YjOFtMgiOLE5fbm4JcEQaimo-KvnUte2rpxUOc-mG0pAedPq5h8xdguIxWvQ4icDHWgUc2p8Xs9hh5zd5csJ0RWaPht8ZEaIEULw8go_3XGWrv13KXKvRLUp_XWOZUVMvvDRlSW2y0V_0QSRzg8Pxyv3k0MTntM1pWfJb0pmifGdAwNihlaYQyh8FoLJ0CW4NWrksiTN7YKgY0qhTE3Lvlf44svNpdD7QdQo1MZTemRCZ1Jkflq6FGZ_2Xzcj-oFgsuybjkUPIH5GsIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۲ هشداری که بدنت قبل از کمبود ویتامین‌ها بهت می‌ده
⚠️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/674387" target="_blank">📅 09:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674386">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQlurGRXFBwf1CAIqWsH3v0Ze2RCDayWeYnHQmVgU1nhXoMxv2lfAd9aTMraj6ZOutpAWznjT8vbrQU7jt_EMyIhUOdDHjoFJv2sj61wzYWOcC2ZZ0hstAhNX5klxOZiKcr2hRq--_0lChk_HILVan77GKo6LGApLpQ7-jw8cZm7k86qBBkxCbKpgHUMK0e9UI8IeEFup4BEONEH_9TVyVBQ8kbUKqbbNzwAd8FjzbhGL-PiUR1XoaQ43BsMuTcbK0NIQde-WyOIW3cB4VAhJ74ewf5EnAMppi1iQGovMdUXcnr_qM2kaOrQzvaMq6WjAJZ1thUNoWcvkUr3dm0YJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آلوهن میزراهی: فکرش را بکنید اگر ایران واقعاً کاخ پادشاهی در اردن را هدف بگیرد؛ به نظرم همان روز ۵ میلیون نفر به جمع شیعیان اضافه خواهند شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/674386" target="_blank">📅 09:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674380">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9f6eacc52.mp4?token=YraRMNmrzdvkClF3WwgHhIc6n0dS4NQMhIVXV-0_BVaNY2NRmxo_RlvjvhkOssu5o4uQDH-2hUiAKZRUrg0JHx4f3Ac1Ius8ESAGQuP1IrkNhToLvNRLlDbdYy79cfMqoEBSx3ao4QQxmdfIv7OiDk1gyzMEdivqBlvD8bUFEFzz-ck_U3YYs6CYbjRSpzuqkiVeZG1moXtDZpzmkePWTFjMTyxrso3Fu1SuLl0K0S8X2hY5DATb6USeJMcvyMqPRf-E0OQqIgaIZOo5rU5M1XFolfOzPuOt9HBwacIfzON_tD1kdN4X4ZsHLp_DyC5CCU9QNf3NQVopfD-KGJ5_p4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9f6eacc52.mp4?token=YraRMNmrzdvkClF3WwgHhIc6n0dS4NQMhIVXV-0_BVaNY2NRmxo_RlvjvhkOssu5o4uQDH-2hUiAKZRUrg0JHx4f3Ac1Ius8ESAGQuP1IrkNhToLvNRLlDbdYy79cfMqoEBSx3ao4QQxmdfIv7OiDk1gyzMEdivqBlvD8bUFEFzz-ck_U3YYs6CYbjRSpzuqkiVeZG1moXtDZpzmkePWTFjMTyxrso3Fu1SuLl0K0S8X2hY5DATb6USeJMcvyMqPRf-E0OQqIgaIZOo5rU5M1XFolfOzPuOt9HBwacIfzON_tD1kdN4X4ZsHLp_DyC5CCU9QNf3NQVopfD-KGJ5_p4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف تحلیلگر ضدایرانی؛ آمریکا فقط در ۵ ماه جنگ علیه ایران، معادل هزینه ۴ سال جنگ خرج کرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/674380" target="_blank">📅 08:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674377">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4wBtbyDWKvNa3OCqwfwJY_7-r_blnu_61FFKOCrR87x9jLXj4hRWA-zD06QG3tJ46k-k08Ct9eFIjnXfZIzjSaTcy1YWycuVbYgXz1pj9oy4BOXEIO7HG0uMCZdSSS9b8LQKVqQa9zTiCnIzkhdwh1jX7yP_YrCYCO3lZ1NCWeeQUxG0fMmo6836t9trnR8V19LiB4UU-W0gpZq4KrQzNAbc3pwoqFMPW3uqp2qNUpORlc3Tnp1n_Otz-MnuCw8X1Har1HaQcJIh_TMaCSUoeYv7QjCYHYGfzV054MO0Vt2tL_lrrZ89lvK4EbNSHQ7SXK1nvlUDkCMf48PS_sInw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸ شاهکارِ کمتر دیده‌شده‌ اینترنت
✨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/674377" target="_blank">📅 08:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674375">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a4cc78c72.mp4?token=oYrGJSNABVd9FSdXHHezFWUD8VNXdjcdoDT4n6sFZdfVnChCm6hwn6hgd7r3qYjyFyTneG6GYMmqZbJYPuOCtf92ZEeuqeUFpJBhrxHTfnQukx3ai-meOW_lyB8GInZqDmsQJyk364xfa_q06n_CbsFfxS5jiOejyz0250b8rSO84GxTWbGxy8GeuB5eQZHR9_Svy_42lVelqLaKwe6zTPibywrdwTAFww9Fsmw9KUED6oNRD0EZHSIf51kPXSvmXN_DyqyCl5A-qg-bIwQSBqq8aG-GEx_rl3aEwJnKt3zA5FolAYxlFTj0rQazO1m4mFLpHQRe4wycWA14Wer7qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a4cc78c72.mp4?token=oYrGJSNABVd9FSdXHHezFWUD8VNXdjcdoDT4n6sFZdfVnChCm6hwn6hgd7r3qYjyFyTneG6GYMmqZbJYPuOCtf92ZEeuqeUFpJBhrxHTfnQukx3ai-meOW_lyB8GInZqDmsQJyk364xfa_q06n_CbsFfxS5jiOejyz0250b8rSO84GxTWbGxy8GeuB5eQZHR9_Svy_42lVelqLaKwe6zTPibywrdwTAFww9Fsmw9KUED6oNRD0EZHSIf51kPXSvmXN_DyqyCl5A-qg-bIwQSBqq8aG-GEx_rl3aEwJnKt3zA5FolAYxlFTj0rQazO1m4mFLpHQRe4wycWA14Wer7qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکات مناسب گودی کمر  #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/674375" target="_blank">📅 08:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674372">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
تداوم مبارزه بافساد مالی در عراق
🔹
دستگاه قضایی عراق:
۴۰۰ هزار دلار، ۱۳ میلیارد دینار و ۴۵ کیلوگرم طلا از معاون وزارت نفت عراق کشف و ضبط شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/674372" target="_blank">📅 07:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674370">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWWriAeeuw7GGgK-qxEI-_0LC3AjBgFh4S_-lqHaoioqDy99cXIh8b3pKErmiiXEPBPzgn_AdUCQo7n1tqrwnEmrqgB5HjOMG4OwOFIuOlcADjkPIaZrc2dNeklPi3jgfSDzw23UOmjSDtCaSlmQDJGtyTpqKtt1wXur02qoS8WBvCvq0j6oKYLdMNDJbnSXbUEdjHIeq9WxN91i_E-oCFH1XSbkXeL9gT8FmHJI1v0k0ZA51l_ezZ-iDyvNiwx1HDjZf9mAjclMATolSn1gBp2fDupW5pIcZaLh6mj7wa6deufXZAZUIwNfp0n5NqXGar-QGsmfIS62oHSArZcRDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۱ مرداد ماه
۸ صفر ۱۴۴۸
۲۳ جولای ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/674370" target="_blank">📅 07:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674369">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
مجلس نمایندگان آمریکا بودجه نظامی ۱.۱۵ تریلیون دلاری برای ۲۰۲۷ تصویب کرد که همکاری با اسرائیل را تسریع و هزینه جنگ علیه ایران را تأمین می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/674369" target="_blank">📅 07:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674367">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
صنایع تا دوماه قطعی برق ندارند
🔹
با دستور رئیس‌جمهور و با هدف جلوگیری از توقف تولید و حفظ اشتغال، برق صنایع در مرداد و شهریور قطع نخواهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/674367" target="_blank">📅 07:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674364">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
حملۀ دشمن به حوالی اسلام‌آباد غرب
فرماندار شهرستان اسلام آباد:
🔹
حوالی ساعت ۳:۴۰ بامداد امروز، در اثر حمله نیروهای تروریست آمریکا دو انفجار در اطراف شهرستان اسلام‌آباد غرب رخ داد.
🔹
فرماندار اسلام‌آبادغرب: حمله آمریکا به اطراف شهرستان تلفات نداشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/akhbarefori/674364" target="_blank">📅 06:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674360">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/610b37cc99.mp4?token=JZMG1Eg8FrIXiMhLvbsGJ8WiexFzSz2TL_h4YXAO8mpiY1DeI_1gZ4yJOP3WdW2nkLW6i00yhmVzVr3tGPbZHwMe2vFwCKo3XZZiF32Rwiy4xqd4DLSZJ8x-ENl3noklTYijkNw-VUXhUfexQQjTysYOl-S16gJQSzVB2YhFnOGNKNXssLpHc-pYfwmf5XdIcQPmwEqTciv8uE-211TtmOAiBUr0SCCl4OEIFXjSnxCG_0keIJkJIDir_KksCdfcV3JJjfr-_Z9hAL0kFug8xSJYd4Ap8SgVyMGGTSU1F_WRsFTXU-j3Ni5ogzdcW-gB14jM82Uubzys2Na61zZtoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/610b37cc99.mp4?token=JZMG1Eg8FrIXiMhLvbsGJ8WiexFzSz2TL_h4YXAO8mpiY1DeI_1gZ4yJOP3WdW2nkLW6i00yhmVzVr3tGPbZHwMe2vFwCKo3XZZiF32Rwiy4xqd4DLSZJ8x-ENl3noklTYijkNw-VUXhUfexQQjTysYOl-S16gJQSzVB2YhFnOGNKNXssLpHc-pYfwmf5XdIcQPmwEqTciv8uE-211TtmOAiBUr0SCCl4OEIFXjSnxCG_0keIJkJIDir_KksCdfcV3JJjfr-_Z9hAL0kFug8xSJYd4Ap8SgVyMGGTSU1F_WRsFTXU-j3Ni5ogzdcW-gB14jM82Uubzys2Na61zZtoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۲ شهید و ۱۱ مجروح در حملۀ موشکی آمریکا به مرز شلمچه  معاون استاندار خوزستان:
🔹
در حملۀ موشکی دشمن تروریستی آمریکا به مرز شلمچه، ۲ نفر از هموطنانمان شهید و ۱۱ نفر مجروح شدند.  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/akhbarefori/674360" target="_blank">📅 05:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674359">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
۲ شهید و ۱۱ مجروح در حملۀ موشکی آمریکا به مرز شلمچه
معاون استاندار خوزستان:
🔹
در حملۀ موشکی دشمن تروریستی آمریکا به مرز شلمچه، ۲ نفر از هموطنانمان شهید و ۱۱ نفر مجروح شدند.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/akhbarefori/674359" target="_blank">📅 04:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674356">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
سی‌ان‌ان: موساد اطلاعات کوه کلنگ را به آمریکا داد
🔹
منابع آمریکایی می‌گویند که «رومن گافمن» رئیس سازمان جاسوسی رژیم صهیونیستی اطلاعاتی درباره تأسیسات هسته‌ای ادعایی زیر کوه کلنگ را به واشنگتن منتقل کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/akhbarefori/674356" target="_blank">📅 04:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674353">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97e14d6a38.mp4?token=TDPobinuEVuX11MAUaIQrNVAi71XoRr9XIldE62F4MD-FMZaQ6vRGJJCWqoen8TcAml5l0kDA0-s0ETddRJt6IF7JLbv1JinMWldTaMbV11JWMPcbz-qzJ_Qnyi-LEOuKsl1qhqalS5IY6jJ3yBdIva9F9afFcCBM_e0XKs4wL5IP-zb1GPOM_8TWYWWQrHjOcT8vhiCt8LYvvWICpyoAp7o22E3vIHiGazR6BfIYROavi6PdfEaZTzGGAY54gkuU-H3qLtNl_-n7J94d-0or248jnqr_BKDVwZr13DMWorfPuvKpW0WZiSGt13IgCYWhfuRG0AZRLYni2t26Y05ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97e14d6a38.mp4?token=TDPobinuEVuX11MAUaIQrNVAi71XoRr9XIldE62F4MD-FMZaQ6vRGJJCWqoen8TcAml5l0kDA0-s0ETddRJt6IF7JLbv1JinMWldTaMbV11JWMPcbz-qzJ_Qnyi-LEOuKsl1qhqalS5IY6jJ3yBdIva9F9afFcCBM_e0XKs4wL5IP-zb1GPOM_8TWYWWQrHjOcT8vhiCt8LYvvWICpyoAp7o22E3vIHiGazR6BfIYROavi6PdfEaZTzGGAY54gkuU-H3qLtNl_-n7J94d-0or248jnqr_BKDVwZr13DMWorfPuvKpW0WZiSGt13IgCYWhfuRG0AZRLYni2t26Y05ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شهادت دو نفر در حمله آمریکای تروریست به مرز شلمچه  معاون امنیتی و انتظامی استانداری خوزستان:
🔹
تاکنون ۲ نفردر حمله دشمن آمریکایی به مرز شلمچه به شهادت رسیدند  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/akhbarefori/674353" target="_blank">📅 03:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674350">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
حمله موشکی به اطراف پایانه مسافربری در مرز شلمچه   ولی الله حیاتی معاون امنیتی و انتظامی استانداری خوزستان:
🔹
دقایقی پیش اطراف پایانه مسافربری در مرز شلمچه مورد هجوم موشک های دشمن تروریستی آمریکا قرار گرفت.
🔹
این حمله هیچگونه مصدوم و مجروحی در پی نداشته و…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/akhbarefori/674350" target="_blank">📅 03:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674348">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpS7qXt93CK31N1zP6xCIcko3HAA4ItDFB0PuOPEXMUguaJFaS5KYIIgF2dh47_uCkp1i71Inr34UTb650j8-u-5HmlU8jCLTCiIJn9NsKaVMBvGrmxGC2ry0SCzU6elGi_SzrZcTuQln0YSZmGijk7XzShTu7Bk6qD1ItO1wpHNRwVG25cPaE5WAH-G7W0DH4y3e-6zq_pkkS_h-B1ze7wJhjYpHvF28xxU2sW9PSiOZ_ywbRY9YALcszeROv4K4cbfxu7E6hI9lbwm8953DgHNfluuVXX47fIOJwI7I-AShWV3GIbR5GoPJI7T0jfettVnqEPUOQsalthx-tBVFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابراهیم رضایی: احتمال حمله آمریکا به تأسیسات هسته‌ای، دلیل قانع‌کننده‌ای برای تغییر دکترین هسته‌ای است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/akhbarefori/674348" target="_blank">📅 03:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674347">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8a7d9e0c.mp4?token=Z8ljzzLHBXZSZuvhlEB4kZcYUnyc6EyzE3ScQe0IOx63hcVsPXFF5DeQAGeE_k0OvwDaIepXEyIBGLnIt9eIJ9bVKfhbbuxTkkTIiujXhjMVoQ4asAzpwKl8EqxnietQoxYXWpfmEoXJC6yyHHk1mOZ5iHX0kmpV6emXUarb-H51uLo_wIdG0FEQcRTSZ26WTBCD9xiADS6m_pAhN-X7sccTzV2nuPxofUIStz5eao4Il_vDixgpjA1Y33c_ZL-NpGXSmWghYWazvysPKwQUhnxns4Z8-rsUHdASjpx8oWuJaVBioB6nwjOTXK_Llq_udUXodslHmGilEwKJ095qmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8a7d9e0c.mp4?token=Z8ljzzLHBXZSZuvhlEB4kZcYUnyc6EyzE3ScQe0IOx63hcVsPXFF5DeQAGeE_k0OvwDaIepXEyIBGLnIt9eIJ9bVKfhbbuxTkkTIiujXhjMVoQ4asAzpwKl8EqxnietQoxYXWpfmEoXJC6yyHHk1mOZ5iHX0kmpV6emXUarb-H51uLo_wIdG0FEQcRTSZ26WTBCD9xiADS6m_pAhN-X7sccTzV2nuPxofUIStz5eao4Il_vDixgpjA1Y33c_ZL-NpGXSmWghYWazvysPKwQUhnxns4Z8-rsUHdASjpx8oWuJaVBioB6nwjOTXK_Llq_udUXodslHmGilEwKJ095qmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه عراقی «نایا» نوشت: «آمریکا به محل استراحت افسران پلیس ایرانی در گذرگاه مرزی شلمچه بین ایران و عراق حمله کرد»/ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/akhbarefori/674347" target="_blank">📅 03:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674346">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
اخبار اولیه از حمله آمریکا به گذرگاه مرزی «شلمچه»
🔹
رسانه‌های عراقی با انتشار تصاویری گزارش داد که منطقه‌ای در نزدیکی گذرگاه شلمچه در مرز بین ایران و عراق، هدف حمله تروریستی آمریکا قرار گرفته است./ صداوسیما
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/674346" target="_blank">📅 03:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674345">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8cf6f105.mp4?token=MJf3qTjmvYOn0oqAhYH9E-Iw_syzM9cOEICLuiiGcInTV2ABn_AhnWKhBvU71f7YXH5tn36hKtXfcLA5FLRfqOYhAz_EbygFSGcXvzlYe_kmtR_5D0u8KCBgxmvPvv850uIcsfHbbhBJLiuHIW_xQILr6Cu5tKSY3pUVO49RdFqGUL86xW6qqkJX2EzjnKasdpJj21ytwL7PNPY4tR7ZkliFzMiH6msIDTCLO0N0RtF2tqMfVsj3UFfcjz8ZiJmN9bfF6v6Eu5JbKVWF2prkH4aZw_E9poQAsGjZ68IGuIbFm80-o8z_4iD8aAE9AlocbJyiAUwWXFNb_wSpWXJUKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8cf6f105.mp4?token=MJf3qTjmvYOn0oqAhYH9E-Iw_syzM9cOEICLuiiGcInTV2ABn_AhnWKhBvU71f7YXH5tn36hKtXfcLA5FLRfqOYhAz_EbygFSGcXvzlYe_kmtR_5D0u8KCBgxmvPvv850uIcsfHbbhBJLiuHIW_xQILr6Cu5tKSY3pUVO49RdFqGUL86xW6qqkJX2EzjnKasdpJj21ytwL7PNPY4tR7ZkliFzMiH6msIDTCLO0N0RtF2tqMfVsj3UFfcjz8ZiJmN9bfF6v6Eu5JbKVWF2prkH4aZw_E9poQAsGjZ68IGuIbFm80-o8z_4iD8aAE9AlocbJyiAUwWXFNb_wSpWXJUKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اخبار اولیه از حمله آمریکا به گذرگاه مرزی «شلمچه»
🔹
رسانه‌های عراقی با انتشار تصاویری گزارش داد که منطقه‌ای در نزدیکی گذرگاه شلمچه در مرز بین ایران و عراق، هدف حمله تروریستی آمریکا قرار گرفته است./ صداوسیما
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/akhbarefori/674345" target="_blank">📅 03:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674343">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
اطلاعیه شماره ۴۳/ یک فروند از سه فروند کشتی متخلف که قصد عبور از مسیر ناایمن تنگه هرمز را داشت دچار آتش سوزی و دو کشتی دیگر با سرعت به عقب برگشتند
روابط عمومی سپاه :
🔹
ملت عظیم‌الشان و بپاخاسته ایران اسلامی، حضور عاشقانه شما در صحنه، نبرد با استکبار را روح بخشیده است و دعای خیر شما پیروزی رزمندگان بر دشمن متجاوز را تضمین کرده است.
🔹
سه فروند کشتی نفتکش با تحریک و وسوسه ارتش کودک‌کش آمریکا قصد عبور از مسیر مین گذاری شده جنوب تنگه هرمز را داشتند که پس از انفجار و آتش سوزی شدید در یکی از آنها، دو فروند دیگر با سرعت دور زده و به عقب برگشتند.
🔹
نیروی دریایی مقتدر سپاه تاکید می کند که تنگه هرمز در کنترل ما است و تا زمان ادامه شرارت های آمریکا در منطقه، کاملا مسدود است و هیچ نفتکشی وارد و خارج نخواهد شد و هر کشتی که فریب آمریکا را بخورد و قصد عبور بدون هماهنگی با جمهوری اسلامی ایران را داشته باشد به همین سرنوشت دچار خواهد شد.
🔹
به آمریکای متجاوز و کودک‌کش اخطار میکنیم از شرارت در این منطقه حساس و به خطر انداختن کشتی های تجاری و بازی با امنیت انرژی جهان دست بردارید.
🔹
به مداخلاتی که جز بحران انرژی و کاهش کود کشاورزی برای جهان نتیجه ای ندارد پایان دهید، این شرارت‌ها جز بی اعتباری بیشتر و شکست جبران‌ناپذیری که به زودی خواهید چشید نتیجه ای برای شما نخواهد داشت.
🔹
به یاری خدا عملیات تنبیهی برای این تخلفی که کردید انجام خواهد شد.
و ما النصر الا من عند الله العزیز الحکیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/674343" target="_blank">📅 03:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674338">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
مقام ایرانی به رسانه روسی: برای حمله زمینی آمریکا آماده‌ایم
ریانووستی به نقل از یک منبع نظامی ایرانی:
🔹
هرگونه حمله آمریکا به تأسیسات هسته‌ای، با پاسخی فراتر از انتظارشان مواجه می‌شود./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/akhbarefori/674338" target="_blank">📅 02:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674336">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ادعای روبیو: توافق با ایران دیگر لازم‌الاجرا نیست
وزیر امور خارجه آمریکا:
🔹
توافقات بر اساس پایبندی به تعهدات هستند و ما با ایران توافقی کردیم که آنها سپس آن را نقض کردند و دیگر لازم‌الاجرا نیست.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/akhbarefori/674336" target="_blank">📅 02:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674335">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODWoow3rrf6Os80Z8fjbZB3Nwbfd5t3x5NNK-fheMo19-RtO5jcVhSut57ZRTgJDjIXJqBmrV4uAHQYBPgOR51xcGUP2B5XRyaovLSWKokML5eKGkc2llQbbD3hh6LUh_TBv5WZMqZJq3V-VIYxNZyVCMD9Q3w_mio3gn-qTyXMoHtb_inar9A-LuixOa1Zuz9yL5LSJ0X9ex2Y-o4LopskHJys5j0ATm-efJHbnHfo4ZW5uq0JhUYeV6_7Xd0SUZKP3TMItXCwZND3cxIMugCDERktOCRnCGfF_BTLaL20sbQSJ8XS6BzM5tKEfMt4oBSSo0Cvo93Iml7yY6te7Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پوستر فیفا از لحظات خاص و خاطره‌ساز جام جهانی با حضور طارمی، رضاییان و عزت‌اللهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/akhbarefori/674335" target="_blank">📅 02:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674333">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
الجزیره: مجلس نمایندگان آمریکا در طرحی اولیه، اختصاص مبلغ ۹۵ میلیارد دلار را جهت تأمین مالی اقدامات نظامی و درگیری با ایران به تصویب رساند/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/akhbarefori/674333" target="_blank">📅 01:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674330">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c92215a25.mp4?token=BsVBgWeXu37boxOoOkQYp4uk-WXSqjbog1h_VFBOcvJYHMN9ZtvK4Qf46vrhgR0WqKMPijuUDCpNqw8hwRes2l8W75ff8pWtM2lG-Hp8jIVyI-m-Ql6kdTEbvTMgVG_S_Dnh1CPSfwdF1MD7Gzfa8XNv53i2C3c6PyDqb1-CiV3GZzlUo37mHfC3SSWSlJ-Tfo6U6JXx1oLffAaX2WGmeb4ktepPG2gmJNiF1IRhOG9Tizj6XJOF1o3se8ZrScKFkHzqK2tTZZNfB2m1EVgEEchp4CXU6Bqcw8lgzJAoZjI0-Z18wTuGYd1qWEgqlr4M2lxBUoP1FLiN3frLSG1Smw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c92215a25.mp4?token=BsVBgWeXu37boxOoOkQYp4uk-WXSqjbog1h_VFBOcvJYHMN9ZtvK4Qf46vrhgR0WqKMPijuUDCpNqw8hwRes2l8W75ff8pWtM2lG-Hp8jIVyI-m-Ql6kdTEbvTMgVG_S_Dnh1CPSfwdF1MD7Gzfa8XNv53i2C3c6PyDqb1-CiV3GZzlUo37mHfC3SSWSlJ-Tfo6U6JXx1oLffAaX2WGmeb4ktepPG2gmJNiF1IRhOG9Tizj6XJOF1o3se8ZrScKFkHzqK2tTZZNfB2m1EVgEEchp4CXU6Bqcw8lgzJAoZjI0-Z18wTuGYd1qWEgqlr4M2lxBUoP1FLiN3frLSG1Smw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پهپادی که به‌یاد دانش‌آموزان شهید مینابی پرتاب شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/akhbarefori/674330" target="_blank">📅 01:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674329">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ادعای سازمان تروریستی
سنتکام: با دستور ترامپ، و با هدف تضعیف توانایی‌های نظامی ایران در تنگۀ هرمز، دور جدید حملات را‌ آغاز کردیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/akhbarefori/674329" target="_blank">📅 01:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674324">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vw-Z9zDXHkw6BoD-kZRDAqmGJllp7EPkf7prPp7ibVy7RSNOtuSNYKzYjPImhxzWclAbfyuIe_HKM4I_TmQ4vz6BHibC47Tz_xjLGzaLurBKFGJvxmL7yZzjJZIjUreyHvgpxPkyVhTg9Jd6_Mzutdt18qadBewc5ir-Wh1oT92MXwER3kyJl19yyps_566Zx7w7J5VwzVwh-oembmtNRTq9c8ZUpnECv6dtwISG2TOW7E-PAyOnySY5RYjXRKY3aob5TwrW-ghzXlB31RQeh2uwsII1fgDFKqSURFXcMtlh-R95p5R8X5ezGgKXCJyZ84fpN8tlCRGxB3rcXpdC6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش خاندوزی به عصبانیت شیطان زرد: این تازه آغاز ماجراست
🔹
همین حالا سربازانتان را به آغوش خانواده‌هایشان بازگردانید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/akhbarefori/674324" target="_blank">📅 01:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674321">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
انصارالله یمن می‌گوید دو نفتکش سعودی به نام‌های «ENCELA» و «LAYLIA» را با استفاده از موشک‌های بالستیک، موشک‌های کروز و پهپاد هدف قرار داده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/akhbarefori/674321" target="_blank">📅 01:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674319">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
هدف قرارگرفتن نفتکش عربستانی در شمال مرز یمن
🔹
بر اساس گزارش های دریافتی اولین کشتی نفتی عربستان در ۷۰ کیلومتری شمال مرز یمن با موشک مورد اصابت قرار گرفت و در حال سوختن است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/akhbarefori/674319" target="_blank">📅 01:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674315">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
جنگنده‌های نیروی هوایی ارتش جمهوری اسلامی ایران بر فراز آسمان تهران به پرواز درآمدند
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/akhbarefori/674315" target="_blank">📅 00:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674313">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db2a57c4cc.mp4?token=RrpQEeK5fYIdMP_j6w1j5-93XPoVOOzG6ZnL-AP8RMIhejG3tvwQ1qTljULNsIXrAOzLT4TWo3ciYyV0ewG84ZR5GBfhaOWGAuJYQTYjD5vllm-CU43Tk7mVVU8rT2UYUkMVc9fqW5SVPtlAtJaGyksf3ezMnC00zi37LHDmhL91wmJ5f-nS7p38yoAqws5SwjLmOafk9HAYvPOq0Dm3uShRsxSZ5k4krFApZzELpLKrbQGMPvs1km7AK-mGwlq-GNsu-YGor6KsVT7fZdneDSCIqaQvgU8A0CpE1MB1epfq_lEzhHJQLUhnngtRAfXfnh5FwQj7geqnUs4iDxYFeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db2a57c4cc.mp4?token=RrpQEeK5fYIdMP_j6w1j5-93XPoVOOzG6ZnL-AP8RMIhejG3tvwQ1qTljULNsIXrAOzLT4TWo3ciYyV0ewG84ZR5GBfhaOWGAuJYQTYjD5vllm-CU43Tk7mVVU8rT2UYUkMVc9fqW5SVPtlAtJaGyksf3ezMnC00zi37LHDmhL91wmJ5f-nS7p38yoAqws5SwjLmOafk9HAYvPOq0Dm3uShRsxSZ5k4krFApZzELpLKrbQGMPvs1km7AK-mGwlq-GNsu-YGor6KsVT7fZdneDSCIqaQvgU8A0CpE1MB1epfq_lEzhHJQLUhnngtRAfXfnh5FwQj7geqnUs4iDxYFeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هدف قرارگرفتن نفتکش عربستانی در شمال مرز یمن
🔹
بر اساس گزارش های دریافتی اولین کشتی نفتی عربستان در ۷۰ کیلومتری شمال مرز یمن با موشک مورد اصابت قرار گرفت و در حال سوختن است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/akhbarefori/674313" target="_blank">📅 00:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674312">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0ipRLQgECld7ylbS1TH1sxULs8HX7HIVDDvs_o1SXnIiNynF7YtbShvrSisLFmJSAieJVN9GrYW7BvphTtAL50n6CnUQLjas3Bn_14KmdbVyQ-UMS5CQWZNEQNurvkgtsWnk3PZQMtgEAR4DjNrkS0YHfQx8PkNQvu7vPVxpFNriw9mveiyj5aMZhKIl-pNcelBavmw84jtd_RRAu0wIBc2TXug7d_2TzYOEL426EQtSYl9AHt0toqXAbcObz9TwAr9ygw3Yyl_ajQhv9q7B3yCqMAK_OFiLK2EpV0kfeDBon1LHZC1q6N3ERgbFSKnoK0LO--YL-ys2HE03H8zQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرنگار الجزیره: منابعی در ایران می‌گویند پرونده کوه کلنگ (کوه تبر)، طبق روایت اسرائیل و موساد درباره این تأسیسات هسته‌ای، با هدف تأثیرگذاری بر تصمیم‌گیرندگان سیاسی در واشنگتن مدیریت می‌شود
🔹
برخی منابع نیز می‌افزایند که در صورت هرگونه حمله، اسرائیل از هرگونه پاسخ ایران در امان نخواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/akhbarefori/674312" target="_blank">📅 00:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674310">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
پاکستان انصارالله یمن را تهدید کرد
🔹
پاکستان به جنبش انصارالله یمن هشدار داده است که هرگونه حمله به کشتی حامل پرچم پاکستان یا منافع دریایی پاکستان، «تهدیدی علیه امنیت ملی ما تلقی خواهد شد».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/akhbarefori/674310" target="_blank">📅 00:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674309">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
خبرگزاری صداوسیما: صداهای مهیب شبه انفجار در اهواز / انفجار در رامشیر
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/akhbarefori/674309" target="_blank">📅 00:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674304">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
آمریکا و عربستان توافق هسته‌ای امضا کردند
🔹
وزارت انرژی آمریکا گزارش داد که آمریکا و عربستان سعودی، یک توافقنامه همکاری هسته‌ای و همچنین یک توافقنامه تضمین‌های دوجانبه امضا کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/akhbarefori/674304" target="_blank">📅 00:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674303">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0891f90f8.mp4?token=erWvepTAVjAzxfI8OrYkS7lZkmRqYziQ28pX4XliPyuBx55u6AeHABVPPxj4NQLwnNOe09BUg1OCFA5ftRehtaODaCsaDJq1OANeQrA0P_gitOX5MEznkqgj2ck55T6jjjGqEeRU5OzYFpUmR2YVWQvIhDGoZ7Yt_LTaALb0E8ZM6q_oKhaxCA19W8_TL4upT1oCuweV8suG1JUtXr_bEMMagRQ4yC7TZL1XzXbZ03vy-fBpn6PRzG4HR7Bxmz0Ky2oua9nKLgvvfSRPLH0MKMWZRTybsC1y98TLB1WBQotuSXkGAYtPViIP3f5PToW9DoeHdFBaRuu9dvH9ByTsbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0891f90f8.mp4?token=erWvepTAVjAzxfI8OrYkS7lZkmRqYziQ28pX4XliPyuBx55u6AeHABVPPxj4NQLwnNOe09BUg1OCFA5ftRehtaODaCsaDJq1OANeQrA0P_gitOX5MEznkqgj2ck55T6jjjGqEeRU5OzYFpUmR2YVWQvIhDGoZ7Yt_LTaALb0E8ZM6q_oKhaxCA19W8_TL4upT1oCuweV8suG1JUtXr_bEMMagRQ4yC7TZL1XzXbZ03vy-fBpn6PRzG4HR7Bxmz0Ky2oua9nKLgvvfSRPLH0MKMWZRTybsC1y98TLB1WBQotuSXkGAYtPViIP3f5PToW9DoeHdFBaRuu9dvH9ByTsbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیاده روی زائران اربعین در میسان در جنوب عراق به سمت کربلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/akhbarefori/674303" target="_blank">📅 00:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674300">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86ca146bb.mp4?token=MpS9P87QWQcsiJZ296XgcRO8DtvQY-B8v9qquMqS3RjsEVYX8ftENdGPRIQIdGyT44c0mXwtQHEwO94VlmN-djCUlPLzVA7qn5yRm7ciuTos3r0k1u4zawvj5bz7z2cZsukeutW_jp1aFSRU7rRQO7wRagWYkjLCMjjBsgCfpgwvq2Tx82tEnKPWj8wCpFE11dWha64aUXwf_EiNNJaNTo8taUb3fLsIZdi0W89151Q0sr0eD6_ePDGqup3rvU_rT7l2cx9J2GX5cr0IHI3hVm7NDN49cjI-Dyr-c-0be0_4UjvN1ay1Mb_OKlmKNPIVmGZfY8__h0XOh1UxAXieXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86ca146bb.mp4?token=MpS9P87QWQcsiJZ296XgcRO8DtvQY-B8v9qquMqS3RjsEVYX8ftENdGPRIQIdGyT44c0mXwtQHEwO94VlmN-djCUlPLzVA7qn5yRm7ciuTos3r0k1u4zawvj5bz7z2cZsukeutW_jp1aFSRU7rRQO7wRagWYkjLCMjjBsgCfpgwvq2Tx82tEnKPWj8wCpFE11dWha64aUXwf_EiNNJaNTo8taUb3fLsIZdi0W89151Q0sr0eD6_ePDGqup3rvU_rT7l2cx9J2GX5cr0IHI3hVm7NDN49cjI-Dyr-c-0be0_4UjvN1ay1Mb_OKlmKNPIVmGZfY8__h0XOh1UxAXieXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده تد لیو، سفیر آمریکا در سازمان ملل، مایک والتز را درباره جنگ با ایران به چالش کشید
🔹
شما حتی نمی‌دانید در این جنگ با ایران چند نظامی آمریکایی زخمی شدند. واقعاً باید از خودتان خجالت بکشید که حتی ابتدایی‌ترین واقعیت‌ها را هم نمی‌دانید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/akhbarefori/674300" target="_blank">📅 00:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674299">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jW4wiRDUO6pJpfiGOHoAxHAamb-c4W33vA33RGx2Z34PGuL4bSHU9nFaH7hlZKo8bRmDtxuVAainan39yWqS4ZWtyi1vWz74xt3k0GsFdSW7GX_sVboS4cDp5df4-d_1FCWM2PVLjsosfoovRpY9JpO93oz4TVITDEnECZvhKujUVzFz8shuuFxTkx_9nOUTC2mLKUvYiYGbe2_xvJGKVyOVNoMJGI7hggwpSVwsC7EbQNdpcstzqrgZGHqqRWRvaiihrVXnIYNHawyAFD8_0yxvdfDz_Idji1NTAGgQkHQZQ27JnfaXE-yarTlQLmEe2QZ3X2U1mHe1gT2SV2hdWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛑
اثرگذاری در کمپین های سازمان ها  معمولا مهمترین عامل برای موفق بودن کمپین حساب میشود
ایا هر تبلیغاتی و  یا اطلاع رسانی ، تاثیر گذار خواهد بود ؟
استفاده هدفمند و هوشمندانه از ابزار هایی که در اختیار دارید و یا میتوانید استفاده کنید مهم ترین عامل اثر گذاری خواهد بود
مشاوره تخصصی و طراحی کمپین های تبلیغاتی و خبری با ما در ارتباط باشید
👇
@marketing_mn
برای رسید به اثر گذاری ، ما در کنارتون هستیم در اژانس دیجیتال کست:
https://t.me/+fZbPfI0dd-41ZWNk</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/akhbarefori/674299" target="_blank">📅 00:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674298">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMzs3sV83G7tmUODt4BzoidHJfwiwmdpV0FndA1vHHj46MpPUkfFqJHmSVQzTzfW_VViaB4naezy6c0utYdqDMNj9FpqGFW5DjQ6qF8warSdaseuEg1-FheRptm9q-avO_IWgGYwMa5YCUW3-EZ-_lb1Dwrs7NRri7Wu0UUWLuVThoK9e6pDdIIBtePRxHcht0fFL2IHWCe4FwcVCEwuVi4XiOqjAtLXEpG8kkFh6VDsqxUSElxXlCRZ2dkd4X2i9L0iocIipQ9B8lvwqLqfL74y4Mr1JDJupORRHeC04-oxVIt22fQULIiHRoqHrYtT-wSCC6aeTjy4UlmYwfGFEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
خبر منتظر نمی‌ماند
با کانال خبری ما، تازه‌ترین اخبار و تحولات را سریع، دقیق و بی‌واسطه دنبال کنید.
📲
عضو شوید و کانال را با دیگران به اشتراک بگذارید.
@Parstimesnewsiran</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/674298" target="_blank">📅 00:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674296">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unYgsAD2cPuBmpj8Cstb4pQTBlQBLPMB3RV_rgr1iNebLdhvTRoUZ0-Ne_Nkr54c1z2mqDqDQM2flQ8CLNiCZTNUqeCviKbdLH1eVY1ZfVuZRVjCTHT6cCeCe9k4ILv5oSjoRCFLrWUl6mp9ylN_O3qHaxsruqobPwZvPFr02vb4VEnQyBE6DcRUxBaci0HTt147LM-UZHHaMHEIeURlIwqeyozZwWVPGs1KejaR2y6DG7OvMUoV0m5mj3Ne6NP77imS2Y6zKkbglJ_K8L9p9i9RkriswTgnGdaawOZbzoXwkvYhLzN_h52tIgN3FmRQDRFQTTnL4h7Zq6Z28msLUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مگاتخفیف
سوپرمارکت
۴۵دقیقه‌ای دیجی‌کالا
شروع شد!
🔥
🎁
کد تخفیف
۵۰۰ هزار تومانی
➗
تا۷۰٪ تخفیف
روی کالاهای شگفت‌انگیز
🚚
همراه با
ارسال رایگان
امروز از محصولات سوپرمارکتی، شیرینی و تنقلات تا پروتئین و میوه رو با تخفیف‌های ویژه سفارش بده!
🫂
کد تخفیف ۵۰۰ هزارتومانی ویژه کاربر جدید:
6TFG
🫂
۳۰۰ هزارتومان ویژه کاربران قدیمی
(۳ کد ۱۰۰ تومانی):
GD33
فقط امروز
⏰
بزن بریم خرید سر ماه در دیجی‌کالا
👇
dgka.me/Wcjhnscdl
dgka.me/Wcjhnscdl</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/674296" target="_blank">📅 00:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674295">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afp7JiGwtbAHfQOMyco9Y2ATQ2CeJSIQf2CWtBwQlqZJdqHOFFUBsXdp3_rA5Ix6KiDVxl4VxN2J25TCJ2imcJQGakr_eRVi42ESwrqGkueCtQDyNVx9Ly-CISwYXWvEBPQdpi6x14VX2dfCTw-gCcLUPpNvRxm_Nr_oJmaIRlCAqxvpeTIbChFYNzYCI-2htuWll2ddn6d_EvlKJuwVhPrCJZHpBD2qCwTXSeMflpEh7iRu0WpMQvecFkHawR93R5_AlrzMJ29CEJFn4Id_5jBaM6RFkMtICHlg718C4K8cI-qUSNNz7DX3sNogWT7LxWkcLwZ-YhlvsCdtBKlCTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/674295" target="_blank">📅 00:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674294">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42a1a817ce.mp4?token=Laz3p85S1tdIM4ozHeCLemU_OZZge4JpGuUY3JU_EofyJxernwHyp2eQ1RWUpXOBqB6DzJHg9V2-sWkOlQseODRC5SgpI_5nSgSRB7FaF_MjAZu7jK6gIkxED81tOF9UuopH14I8unDbUHAPQhLLfApUZYIgaHvkYGPmy7UQDG0wBV9I-pMbihOtkRe-4T1z0gKNnYeHJfKF4d1lqoWEdhzMbyOm6RXodyC90bh79DKaqiXqCBRbL4Ws46kIEbwuv6-bFAE8Fz0ajAbuIzRNr6x9sI7hevaddpEwHTxgDzQef57iQux9kf3Q1tVivsGA9IoQQt4xSvM89ZyZZ05a5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42a1a817ce.mp4?token=Laz3p85S1tdIM4ozHeCLemU_OZZge4JpGuUY3JU_EofyJxernwHyp2eQ1RWUpXOBqB6DzJHg9V2-sWkOlQseODRC5SgpI_5nSgSRB7FaF_MjAZu7jK6gIkxED81tOF9UuopH14I8unDbUHAPQhLLfApUZYIgaHvkYGPmy7UQDG0wBV9I-pMbihOtkRe-4T1z0gKNnYeHJfKF4d1lqoWEdhzMbyOm6RXodyC90bh79DKaqiXqCBRbL4Ws46kIEbwuv6-bFAE8Fz0ajAbuIzRNr6x9sI7hevaddpEwHTxgDzQef57iQux9kf3Q1tVivsGA9IoQQt4xSvM89ZyZZ05a5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سالن رقص شیطان زرد پایگاه نظامی است
ترامپ متوهم
:
🔹
ما در حال ساخت یک تأسیسات نظامی عظیم در کاخ سفید هستیم. این یک سالن رقص است، اما همچنین یک تأسیسات نظامی بزرگ، یک پایگاه پهپاد در بالا و چیزهای عظیمی در زیر آن است... این یک پروژه باورنکردنی است
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/674294" target="_blank">📅 23:55 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
