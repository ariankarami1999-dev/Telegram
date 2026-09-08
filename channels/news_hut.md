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
<img src="https://cdn4.telesco.pe/file/afKLmoGvCp62j475DquBz5TFPkWJ3Ds62RT2JbG7yiCwIjyBGedNI4i2lh1-Ne5nNUvDYXHaUgFrCg-LE11o6X4hSzA32PABk9XG16L_UK0NlXWv7z2WniEpZqGUUv4is-EOfchDBmt46PgpBNXknUmNeyRhv_tNGQiwq3i1jlSVl8f0uAqjogfzje299xUj7Yk7YVOg1EpiENK_fEeQUOjUhnyl3oFscU41Nbe1jQzqlty4tBj_CTKKuaSEyX7YpPBKTljDf4IeCY8CnDTEtxS52sSjNl-bfQfc-2SniAnY2SRzjlnNe9hpy1WwBaSJTm00daFGuqEm7eSO3K-exA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 112K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 21:28:15</div>
<hr>

<div class="tg-post" id="msg-71302">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a391f5b86.mp4?token=sRSN7H9oLiVWHUewir7iqqkNvcJqwaqz0xW_sndKlqQqPgpGTg_kwTd1pXUR4xeLqXuinBhlCONEKXOeLcOTmost_Ji7GhCLDIILKGKsfn4kAlzI_e_2Nj5SInIJBkyHX4X94q1UzUd-MnYkG9NlsXFxmHixs3R-u4ju7RoWIXdRvcoE8AB_d_kBr9b2R_-p-vQiRF_zD8tBOvsdQ72GNcW3wQlaJcwlG6uihZpOBhuJ5_UoTbubYBweMUlELjeWa1O1LjfbPJGyxeWtD8twELEM1m765X1SfmghKjE2XasBsur1OYKlpsH2plLvOZWxkf1GmH_Lz224VQoz8c2prA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a391f5b86.mp4?token=sRSN7H9oLiVWHUewir7iqqkNvcJqwaqz0xW_sndKlqQqPgpGTg_kwTd1pXUR4xeLqXuinBhlCONEKXOeLcOTmost_Ji7GhCLDIILKGKsfn4kAlzI_e_2Nj5SInIJBkyHX4X94q1UzUd-MnYkG9NlsXFxmHixs3R-u4ju7RoWIXdRvcoE8AB_d_kBr9b2R_-p-vQiRF_zD8tBOvsdQ72GNcW3wQlaJcwlG6uihZpOBhuJ5_UoTbubYBweMUlELjeWa1O1LjfbPJGyxeWtD8twELEM1m765X1SfmghKjE2XasBsur1OYKlpsH2plLvOZWxkf1GmH_Lz224VQoz8c2prA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
زمانی که بچه بودم و در کارولینای جنوبی زندگی می‌کردیم، خانه‌مان نزدیک یک مرداب بود.
گاهی مارهای سمی زیادی در حیاط پیدا می‌شد.
وقتی سر مار را قطع می‌کردید، مار می‌مرد، اما خودش نمی‌دانست که مرده است؛ بنابراین باید مراقب می‌بودید، چون سرِ جداشده هنوز می‌توانست شما را نیش بزند و دُم مار هم ممکن بود تا زمان غروب خورشید تکان بخورد.
اما وقتی خورشید غروب می‌کرد و هوا خنک می‌شد، تکان خوردن دُم هم متوقف می‌شد.
🔴
حالا مار ایرانی — یعنی همان رهبری — هم هنوز نمی‌داند که مرده است، اما در واقع مرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/news_hut/71302" target="_blank">📅 21:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71301">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc7c3d5f1.mp4?token=ZFzvSvKXPZZtLj0YOnB_1qxOTQNbQfH2gVNQybojGBoNMaprQQrCt39vUbXiP9Y_S2I83Dtsy56h1GBsm1RB1QyFrWUemW_WmNtUbKm_5QKy2zYY5ysMYfd-3J2WVTHmN4NnxV-q8-VCfCjjm8FHjSfEVbrNcRB1Zv2MlhH7akCrLHXlF8249373KLJVcDFUte-eCb-iMGK2LDC5fYBfoPO_lwdWElbrUnHpE_3aPRqCWt4aEN7w2ZLYCYl68GdN-74O5qpw_DH8hY_FwfTwbmZ9hwgd_SKN-AJNaSBZx51aFB8El19yRntrNvYS0Kx3tDSJUkLM_Iogx6gYt_-8bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc7c3d5f1.mp4?token=ZFzvSvKXPZZtLj0YOnB_1qxOTQNbQfH2gVNQybojGBoNMaprQQrCt39vUbXiP9Y_S2I83Dtsy56h1GBsm1RB1QyFrWUemW_WmNtUbKm_5QKy2zYY5ysMYfd-3J2WVTHmN4NnxV-q8-VCfCjjm8FHjSfEVbrNcRB1Zv2MlhH7akCrLHXlF8249373KLJVcDFUte-eCb-iMGK2LDC5fYBfoPO_lwdWElbrUnHpE_3aPRqCWt4aEN7w2ZLYCYl68GdN-74O5qpw_DH8hY_FwfTwbmZ9hwgd_SKN-AJNaSBZx51aFB8El19yRntrNvYS0Kx3tDSJUkLM_Iogx6gYt_-8bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اقتدار به روایت تصویر؛
🇮🇷
مقام جمهوری اسلامی:پمپ های قدیمی جا برای بنزین ده هزار تومانی نداشتند؛
یک صفر دستی اضافه کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/news_hut/71301" target="_blank">📅 21:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71300">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">از دیشب تا همین الاناست که مسلمونا افتادن به جون هم، شیعه های یمن، سنی های عربستان رو دارن با موشک و پهپاد می‌زنن، یعنی کشوری که خانه خدا اونجاست
عقل
🤯
#hjAly‌</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/news_hut/71300" target="_blank">📅 20:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71299">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZGKsbHwK2EFcB1DcBYY2EVmqmNHTWt7iFgJcztv1aXuAe7piSxjyObzg87hDKYjPfchUzOzBvCplfH-d4URvrEIaFIWjbxhr6yknrO6LHOYdf0wePCZ3H-Af_EStxUAS2BkywEAh8woe75aWF0mL5WjIzYqSsUH9FxdVEv1K3ep1DbKFAh8tijet7sTXJw8fOFGN1d4xNrsmgd7LnVJRphtQ-6JPF7FZlImLI6rt5VZagtncnY7OxXHKVghBCigvOhdB8djK_U-LeXjpHo172AUkjz0esFvImi6K0tDwNa6r3jk6Yal1Nhn-jSt1cLvA8hoF3XdnImB6wRN_seW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
⭕️
⭕️
وزارت خزانه‌داری ایالات متحده تحریم‌های گسترده‌ای را علیه بخش هوانوردی تجاری باقی‌مانده ایران تحت عنوان «عملیات اقتصادی مطرود» اعمال کرده است که ۳۶ نهاد را به دلیل حمایت از خطوط هوایی ایران، دور زدن تحریم‌ها و شبکه‌های تهیه هواپیما هدف قرار می‌دهد.
دفتر کنترل دارایی‌های خارجی (OFAC) ۲۷ شرکت هواپیمایی فعال ایرانی، از جمله ایران ایر تور، هواپیمایی آسمان ایران، هواپیمایی کیش، هواپیمایی قشم ایر و هواپیمایی زاگرس را تحریم کرد.
وزارت خزانه‌داری همچنین چندین مجوز هوانوردی، از جمله مقرراتی که پروازهای خاصی را مجاز می‌دانست و به شرکت‌های هواپیمایی غیرآمریکایی اجازه پرواز هواپیماهای آمریکایی یا تحت کنترل آمریکا را به ایران می‌داد، به حالت تعلیق درآورد.
این تحریم‌ها همچنین شرکت‌ها و افرادی را در امارات متحده عربی، ترکیه، بریتانیا، مالزی و قزاقستان که متهم به حمایت از ماهان ایر هستند، هدف قرار می‌دهد. وزارت خزانه‌داری اعلام کرد که برخی از آنها انتقال حداقل سه هواپیمای بوئینگ ۷۷۷ به ماهان ایر را از طریق امارات متحده عربی و عمان در تابستان ۲۰۲۶ تسهیل کردند، در حالی که برخی دیگر محموله‌هایی از جمله قطعات پهپاد، تجهیزات صنعتی و قطعات هواپیماهای ساخت آمریکا را جابجا می‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/news_hut/71299" target="_blank">📅 20:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71295">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EzW0yDGTgGxXH_-33CW3UyhcvAoM7ZM0EPd2o4qsaC0mRc1oJA48iBlk2K-Ogc3TXStNWpDRILIIHnC4Spj0IN5qsCbj4D-J0qaJtDh3hb97f4OXpJWrtasqrZlE7bUiHNh1iFYv9P9HfMNugMPnYiSMREjEF2rU35GmMyZNWoN8XhScc1a-CFYSEuuFnwrZYLnK4oqnaimDygrok88WbVL8m95JLU8tcHj2mSQHFwh4ReLsXz_qvbFVD0iVeOMUphJ_G8vf7J0pidwCQwZLu_pXwJ0Vp3mW7QTu7RxlFaGMjbOI0eYgmg70BgRqUPe0EzET_eI9UUIiInJSnEsmCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d307bda604.mp4?token=TPKtkL7_5C3E02ZKwkpojF-H-rJ6F7bLFBBShSgjPvxm0SdoHFZI_CPoK3pAK4dEe6vWuIXNihX4eLujuAbPw3oKG9eP3mKTeGSbh5U7_EIntk-5-V22tx-np4TYNPGuxLT5NA4zSO7jFCz51j54ZwtlPw3qLFoxmgyGVKBzx5kyo8qf0x3lMM3Er4KvkhKmdLEpHNWLl60fjqqmDHeMXPy9O4d5IOmzPde79oVO6_gKAgWf9IUCjJbdpRFwUDcUwiy5PSwHtUyP56qbuny3DxdPtg3X5xuXiGTjq67fsTiiJB772LdyRDZt1wMHFMYCBnbTRHJvJ0WyYLrZ_tizAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d307bda604.mp4?token=TPKtkL7_5C3E02ZKwkpojF-H-rJ6F7bLFBBShSgjPvxm0SdoHFZI_CPoK3pAK4dEe6vWuIXNihX4eLujuAbPw3oKG9eP3mKTeGSbh5U7_EIntk-5-V22tx-np4TYNPGuxLT5NA4zSO7jFCz51j54ZwtlPw3qLFoxmgyGVKBzx5kyo8qf0x3lMM3Er4KvkhKmdLEpHNWLl60fjqqmDHeMXPy9O4d5IOmzPde79oVO6_gKAgWf9IUCjJbdpRFwUDcUwiy5PSwHtUyP56qbuny3DxdPtg3X5xuXiGTjq67fsTiiJB772LdyRDZt1wMHFMYCBnbTRHJvJ0WyYLrZ_tizAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌂
امروز صبح رسما شمال کشور رو سیل برد!
به حدی بارون شدید بود، که حتی آب توی خونه‌ها نفوذ کرده و تبدیل به استخر شدن.
ماشینا وسط خیابون تبدیل به قایق شدن و برق اکثر مناطق قطع شده.
باد و طوفان شدید باعث شد کلی درخت و... شکسته بشن و بیفتن روی ماشین، خونه و مغازه مردم.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/71295" target="_blank">📅 19:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71294">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dz95Tu8LmekkMatkAHecKuSkl6OMu6x6mk9hU0vXRdR52nuhytHkz9THK5KSD8GBMfB-jvqEMvz1jWIhXN6-78mhekDIXWjMxiA2-7bTsOOfMrE0szVpu_J63xAdHCOZDCcjrqRUOH86neLEBZXQ5vowiUoM70ACTe5_FRrd8HiHC_XwzJr428FwlFIOXBCHZi117RwfdzuWEzRqBe8avJxKRGBxgfQyDmImXThefn6Fvc5yFKpWuSQaW8S1YQaWPphEiudckfp1fvdQL4BUwO9JccErrFPJ1XU-ZJXRWFZTc-3_C84g_oSMo9Yacf8sty_m70H9s12kmeyy2rUJMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران انقلاب اسلامی:
مردم مبعوث شده ایران عزیز؛ با عنایت خاصه خداوند متعال رزمندگان نیروی دریایی سپاه یکی از مدرن ترین زیر دریایی‌های هوشمند و بدون سرنشین ارتش تروریست امریکا را در ورودی تنگه هرمز طی یک اقدام پیچیده اشراف اطلاعاتی و عملیاتی در سحرگاه امروز به دام انداختند.
این زیر سطحی هوشمند از جدیدترین تکنولوژی در حوزه زیر سطحی در دنیا برخور دار بوده، که سال ۲۰۲۵ میلادی به ناوگان ارتش تروریست آمریکا تحویل شده است.
گفتنی است این زیر سطحی اکنون به غنیمت گرفته شده و طی ساعات دیگر تصاویری از آن منتشر خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/71294" target="_blank">📅 18:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71293">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">⏺
🤩
تسنیم:
تا دقایقی دیگر خبری مهم از شکار رزمندگان نیروی دریایی سپاه در تنگه هرمز منتشر می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/71293" target="_blank">📅 18:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71292">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da31dc3dd.mp4?token=DkWAloO0nSixbwLAC6Vcffp3OZzpotwFtOjvHVDMPVW3uChVkKa-0RfjUfc1RvqKNgghS4Ggh6S09Fuxwzmu6ragYbpN71OIubPI--p6gzlC6Be1e1DXR3lXkAkXPZbGxYPszg7U7SURCohC1tCyiSAzylnue7JjDEUoKIkkzSy6JdrMY1UUPsXuTJvnP57yebj7GFQMwtQcUH-GfujNQrEl8yCnyYf2x18bRfnKPaafK7maehkMtOu0V27opM0qZ449c2e_8hYn2Yv5RnyBfj37Q3Qj0kM37L1zWDwKNQ-2v2TthxuTOG9a2A7ss4u6267BhC-ZxdnAoh-nkEgcmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da31dc3dd.mp4?token=DkWAloO0nSixbwLAC6Vcffp3OZzpotwFtOjvHVDMPVW3uChVkKa-0RfjUfc1RvqKNgghS4Ggh6S09Fuxwzmu6ragYbpN71OIubPI--p6gzlC6Be1e1DXR3lXkAkXPZbGxYPszg7U7SURCohC1tCyiSAzylnue7JjDEUoKIkkzSy6JdrMY1UUPsXuTJvnP57yebj7GFQMwtQcUH-GfujNQrEl8yCnyYf2x18bRfnKPaafK7maehkMtOu0V27opM0qZ449c2e_8hYn2Yv5RnyBfj37Q3Qj0kM37L1zWDwKNQ-2v2TthxuTOG9a2A7ss4u6267BhC-ZxdnAoh-nkEgcmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
⚠️
🇺🇸
افسر نیروی هوایی ایالات متحده که در ماه آوریل پس از سرنگونی هواپیمایش بر فراز ایران، دو روز زنده ماند، برای نخستین بار در برنامه «۶۰ دقیقه» (60 Minutes) — که قرار است روز یکشنبه پخش شود — به بیان ماجرا می‌پردازد.
این افسرِ مسئولِ سامانه‌های تسلیحاتی که نام عملیاتی‌اش «دود ۴۴ براوو» (Dude 44 Bravo) بود، یکی از دو سرنشین جنگنده «اف-۱۵ ای» (F-15E) به شمار می‌رفت.
در حالی که خلبان ظرف چند ساعت نجات یافت، «براوو» به مدت دو روز در مناطق کوهستانی ایران، در حالی که مجروح و تنها بود، از دست نیروهای ایرانی پنهان ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/71292" target="_blank">📅 18:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71291">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71291" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/71291" target="_blank">📅 18:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71290">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iauzC4X4-4Aj5GBgW4iIj3rxOXqKzMAZvh3omSMwDPy-P7vkS3ag-zU3FQ-MlO6YzX7WalojJBG8PwXyk44Ii_FIEhIGPYFnl_aH0uZFNjdoTOrWwVZehb6P2BeY7VX9eJhUFZ9yLN2FEYen8eeLfpROZiF-RPVAqe8bAr8zMPAybFl07Y7npr5I7Bje4DodcdNZIMZhYGnDsdhdwAAGerp-a8Q1SyFaWQYI3FhTaII22KxKSM81A40R0M9DsT4xQSS-Wl2Qzbm--wTqUa4rTMAp7_tiyFgPM8B19wNh31nBW_7MeW_uZsPOJGcQNMgjG2oGiGiUiBgMd6B6PUAdEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
منچسترسیتی
🆚
پورتو
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در تقابل‌های اخیر:
⚽️
منچسترسیتی: ۴ بازی، ۳ برد و ۱ تساوی، ۹ گل زده
⚽️
پورتو: ۴ بازی، ۳ شکست و ۱ تساوی، ۳ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/71290" target="_blank">📅 18:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71289">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
دقایقی قبل صدای سه انفجار از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/71289" target="_blank">📅 17:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71288">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b881718fc3.mp4?token=kyUxWn3bu9zBfQymDU3PrSHCLluMSRtSaE6dwbsCq18ZZZRQRstKzGbHpIazYFTaCJBi0hKaSEJVqTJkGdpnXZBg6oJcZ1iBMra_usGTLfYtlRYz9rekZl0pyuNwIozHYk1KhPXvoZkxXCyCImnR-5-FrnOvt6KXIgFtjPMFqZI07O2ASytiZsKlLabcIKyu21wHC0KELC-AZuxRoIvHX4yTKVxZ9iFQ1TlLdnpjzxFnoeFJJmspsJYuOSVqDo0wzLv1Gv5oMXR_PECnXrSpzcvsVO-C4u0a3hfFqAnXDyQvjb3ous0oWaqfkF0wsAbbqDsaY64f9YN_JwMDyT5sxXu7sJaOkZQJUZNBRDUBAL7DHLXq1MBB-pqClmNygPF4zkHqS6f6YAMJzt2AkV3Mel79OpnpdaDL8ejlpMfQ8rLJyHCdaRWUKcbWf4-j-IHw-xcA6T3rC0LCNZPsp3pUYgM1pDRSfpSiknfmfDCZISAYOn3mVCC14A_VBrq9WoLk7eordrRkZ4WRlsSuoHmcdxJlM2G75rr1-g5Koi7TAlkAbbbJuN29vGSFrWa_gSPtVmvz_MQxThVSu9uX4vNSkIV0msYhBHMRv3rnY9Lt1n9FSSQtvQjTyfaZLMWf9_f3qQEyj2sbIOXgC7CFrOVZ5F3cPJ1jKYb7tfUo3o9bNAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b881718fc3.mp4?token=kyUxWn3bu9zBfQymDU3PrSHCLluMSRtSaE6dwbsCq18ZZZRQRstKzGbHpIazYFTaCJBi0hKaSEJVqTJkGdpnXZBg6oJcZ1iBMra_usGTLfYtlRYz9rekZl0pyuNwIozHYk1KhPXvoZkxXCyCImnR-5-FrnOvt6KXIgFtjPMFqZI07O2ASytiZsKlLabcIKyu21wHC0KELC-AZuxRoIvHX4yTKVxZ9iFQ1TlLdnpjzxFnoeFJJmspsJYuOSVqDo0wzLv1Gv5oMXR_PECnXrSpzcvsVO-C4u0a3hfFqAnXDyQvjb3ous0oWaqfkF0wsAbbqDsaY64f9YN_JwMDyT5sxXu7sJaOkZQJUZNBRDUBAL7DHLXq1MBB-pqClmNygPF4zkHqS6f6YAMJzt2AkV3Mel79OpnpdaDL8ejlpMfQ8rLJyHCdaRWUKcbWf4-j-IHw-xcA6T3rC0LCNZPsp3pUYgM1pDRSfpSiknfmfDCZISAYOn3mVCC14A_VBrq9WoLk7eordrRkZ4WRlsSuoHmcdxJlM2G75rr1-g5Koi7TAlkAbbbJuN29vGSFrWa_gSPtVmvz_MQxThVSu9uX4vNSkIV0msYhBHMRv3rnY9Lt1n9FSSQtvQjTyfaZLMWf9_f3qQEyj2sbIOXgC7CFrOVZ5F3cPJ1jKYb7tfUo3o9bNAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇬🇧
⭕️
#فوری
؛اد میلیبند، وزیر امور خارجه بریتانیا:
ایران هرگز نباید به سلاح هسته‌ای دست یابد؛
از این رو، ما نیز در این هفته همگام با متحدانمان اقدام به ارجاع پرونده ایران به شورای امنیت سازمان ملل متحد به دلیل نقض تعهدات هسته‌ای‌اش می‌کنیم.
همچنین امروز می‌توانم اعلام کنم که ما در هماهنگی با اتحادیه اروپا و ایالات متحده، تحریم‌های اقتصادی عمده‌ای را علیه ایران مجدداً اعمال خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/71288" target="_blank">📅 17:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71283">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645274372a.mp4?token=aziZXFAFk0i3BVOjJwagPK5YEhmsTngTwQyE0bRQ9tSQfQT0iD83psfs8Mt2sMYnZrWKjigYhahEMlJmJb57ptSWc5CuoQ1zcBYdykoCegSiSGaGPbXegHCk6U32_2zMPF_wKc6pJv1YBa464BWZbFKY1k18Xc_K9PRb_aURKpUbxMEaL0DxGdMyX2uVW3qqgqSJmdzsV2vmDZUfWe6lWTzO2DU6WHEYTBJ3Zls9SvOZBvm0xv_-0n1rqwqt0e3OWk5Peb57vxt8szZBg644Wv12HOaJn7pVN53N-B9L6fybalQpi2fZQyItxsQ9JHDyasdbpdejib4WhDRz3YBCrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645274372a.mp4?token=aziZXFAFk0i3BVOjJwagPK5YEhmsTngTwQyE0bRQ9tSQfQT0iD83psfs8Mt2sMYnZrWKjigYhahEMlJmJb57ptSWc5CuoQ1zcBYdykoCegSiSGaGPbXegHCk6U32_2zMPF_wKc6pJv1YBa464BWZbFKY1k18Xc_K9PRb_aURKpUbxMEaL0DxGdMyX2uVW3qqgqSJmdzsV2vmDZUfWe6lWTzO2DU6WHEYTBJ3Zls9SvOZBvm0xv_-0n1rqwqt0e3OWk5Peb57vxt8szZBg644Wv12HOaJn7pVN53N-B9L6fybalQpi2fZQyItxsQ9JHDyasdbpdejib4WhDRz3YBCrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇦
🇾🇪
نیروهای «شورای رهبری ریاست‌جمهوری» (PLC) تحت حمایت عربستان سعودی به همراه جنگجویان قبایلی، شهر «الیتمه» در استان الجوف را از کنترل حوثی‌ها (انصارالله) بازپس گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/71283" target="_blank">📅 16:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71282">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⏺
فارس:
یک پهپاد MQ-1 بر فراز منطقه راهبردی تنگه هرمز با هوشیاری نیروهای پدافند هوایی جنوب شرق ارتش جمهوری اسلامی ایران شناسایی شد و هدف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/71282" target="_blank">📅 16:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71281">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77de453ade.mp4?token=FXCpnKYIbrKul9FGj6_IekpP-3dfZUbqCznzWYHIbRMWALVHVjlw9V5A_jBIhYEUanaeVjKXrUtKExUuWRku5f9fXPYocKXziSEMCrxvdFSIHArq1eUeNzBCH1_bHeXGfktLfH85jVjen8MjBbZpUnW6t0-AZWDD8a2S2Zwpd5P2iy8YCg8aJ_7-XNSY-2mws9ugS4yiQJ7NT9r6sqvsh34E5rvNgSblPKNFHS4GS4GVdLqwv3QiELnqyDnkx_9YoYzTrCt7-SFTSLDKsLcPZS5vZEHy5EgZjHk7DcrAD_5HFvhXxEmE82a5BMsH_bVgusB00Qsju-SKcCvsF6gJSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77de453ade.mp4?token=FXCpnKYIbrKul9FGj6_IekpP-3dfZUbqCznzWYHIbRMWALVHVjlw9V5A_jBIhYEUanaeVjKXrUtKExUuWRku5f9fXPYocKXziSEMCrxvdFSIHArq1eUeNzBCH1_bHeXGfktLfH85jVjen8MjBbZpUnW6t0-AZWDD8a2S2Zwpd5P2iy8YCg8aJ_7-XNSY-2mws9ugS4yiQJ7NT9r6sqvsh34E5rvNgSblPKNFHS4GS4GVdLqwv3QiELnqyDnkx_9YoYzTrCt7-SFTSLDKsLcPZS5vZEHy5EgZjHk7DcrAD_5HFvhXxEmE82a5BMsH_bVgusB00Qsju-SKcCvsF6gJSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جنازه و تابوت ترامپ و نتانیاهو زیر پای طرفداران حکومت برای بار هزارم له شد
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/71281" target="_blank">📅 16:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71280">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a724fc44e.mp4?token=MoGnbcCf3nUZH0-LF5L2ZVJetYMwTxuMW3ywZFj1ebQ0X3vOLiXfOGDm__C_CYK16y9Wx87nLZyWUJG0Kku84BXMHQ8UAfigUKmJL5I7FHwGUo8KsVo0hZuozxUQHtRQLaTMil1gGAuDgsVtwCHs16SFNDOsDtYsURB8IsKy59EANv5Mz9xsbC-abVTT4tqdXCjWX9gmwMAWvghR8sRX2hUp0T9XIA4RcubCCxmvwGAuqKxm_UAXlgQ5UTHAJMsnJOfQUEErkXNBb5UGa7Rn9G-FaiGs4fGuJxvhKXEgJ6ZQcca371mlDk5qNLCh8AcqghgugJ7sGZpPFUH8O4wt_TaMN8v2tZNj_KBQzBMwb0K58dGnCLFnSb3e6gNMe6yeKLwL8kojJchlUcFz0uiBuoeAVy-rOLvqjRUv1ACHnFMUgxa80UOoGemhhjY373PGVuw8HL39wkRy4LVmmdbk7lFxAh6Aenm4_hQanl7dLoIaFTq1j4i6MFqgq3jQyDHdDkbDbi0Qd-fxoTCLhMur6poO0rghoCg3X4DyMqjafEpLOTcR8ANQStiT_ic0cVbHoVRy7GARs6umedWa7jsj3mb8aMyuvQIORrcEPfo0WLV6inILuoLM1kXF6xdGGD97VQSrFf6kLYH9PuwLKm2ueEyLSM3WHuC3eqDJyxV-Jc0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a724fc44e.mp4?token=MoGnbcCf3nUZH0-LF5L2ZVJetYMwTxuMW3ywZFj1ebQ0X3vOLiXfOGDm__C_CYK16y9Wx87nLZyWUJG0Kku84BXMHQ8UAfigUKmJL5I7FHwGUo8KsVo0hZuozxUQHtRQLaTMil1gGAuDgsVtwCHs16SFNDOsDtYsURB8IsKy59EANv5Mz9xsbC-abVTT4tqdXCjWX9gmwMAWvghR8sRX2hUp0T9XIA4RcubCCxmvwGAuqKxm_UAXlgQ5UTHAJMsnJOfQUEErkXNBb5UGa7Rn9G-FaiGs4fGuJxvhKXEgJ6ZQcca371mlDk5qNLCh8AcqghgugJ7sGZpPFUH8O4wt_TaMN8v2tZNj_KBQzBMwb0K58dGnCLFnSb3e6gNMe6yeKLwL8kojJchlUcFz0uiBuoeAVy-rOLvqjRUv1ACHnFMUgxa80UOoGemhhjY373PGVuw8HL39wkRy4LVmmdbk7lFxAh6Aenm4_hQanl7dLoIaFTq1j4i6MFqgq3jQyDHdDkbDbi0Qd-fxoTCLhMur6poO0rghoCg3X4DyMqjafEpLOTcR8ANQStiT_ic0cVbHoVRy7GARs6umedWa7jsj3mb8aMyuvQIORrcEPfo0WLV6inILuoLM1kXF6xdGGD97VQSrFf6kLYH9PuwLKm2ueEyLSM3WHuC3eqDJyxV-Jc0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چنتا دختر با کیسه زباله خودشونو شبیه لاکپشت های نینجا میکنن میرن تو خیابون...
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/71280" target="_blank">📅 16:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71279">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2ae4bae8.mp4?token=rpco5qFqlW1O2EjGXOKTdS1ccOksD7nCJ9SyZDu_F3LDRII__6lKzK7z_Y_J0WH_lchqVsEiYHBhKr0F5pWiJsWlFA0OHE0az0eq_9WsnGE11OT2_Gqk9XCq3r6Wby22uV5OyqdArEHyhBDtTUTHZgzo44NufQCect0wrgtm_ThZ0QUQr0FwXOGS19tJNo_T85VJVdLSlzNKAiWIWX2Iu00LNG9u_qeBJdNtKP-m18CsDLI0qDfxLzhx5Kmur2nehCLJL4NUdk6vMsy22W71HtjBtY_iMPGOmC31uEp38MwCzwhW5QjznG97XFAkj0GrW4f6kFKZJE-ZD1_MihcT-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2ae4bae8.mp4?token=rpco5qFqlW1O2EjGXOKTdS1ccOksD7nCJ9SyZDu_F3LDRII__6lKzK7z_Y_J0WH_lchqVsEiYHBhKr0F5pWiJsWlFA0OHE0az0eq_9WsnGE11OT2_Gqk9XCq3r6Wby22uV5OyqdArEHyhBDtTUTHZgzo44NufQCect0wrgtm_ThZ0QUQr0FwXOGS19tJNo_T85VJVdLSlzNKAiWIWX2Iu00LNG9u_qeBJdNtKP-m18CsDLI0qDfxLzhx5Kmur2nehCLJL4NUdk6vMsy22W71HtjBtY_iMPGOmC31uEp38MwCzwhW5QjznG97XFAkj0GrW4f6kFKZJE-ZD1_MihcT-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
آتش‌سوزی در تاسیسات آرامکو عربستان سعودی در پی حملات حوثی های یمن
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71279" target="_blank">📅 15:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71278">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef148c5074.mp4?token=Hb40ISf88lZOzLtN-9JPRGzOj16AZO-PjeQhH7LGi2nZx0LZJ15IST5sSnPC0YVGWqxgKv2j6ljVH0l7j2fwdtcXZ3h5NLCGgfT2rJyKOS-BhbSViRyE9eiso2c9daDuKhTxYsExY2aJ0egE6kSqsTbZEOxMZ1NaNbPfNrnQj9s9KOBGTy4YIlQrtRjUlsFXtn44EyiWTlEoApWYocJcSW6LnrYLPjpeRAm8lFzrBNlgklIU5rfhff4IJWY-4zp-oUPmGQZABlWzls4mkSY8lUnkFazpWJkO6pu6EN8BL9z5a5P6PnJZ2XxN-r1i1aS8QYIUOoDuEJF-DoF7PvBA3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef148c5074.mp4?token=Hb40ISf88lZOzLtN-9JPRGzOj16AZO-PjeQhH7LGi2nZx0LZJ15IST5sSnPC0YVGWqxgKv2j6ljVH0l7j2fwdtcXZ3h5NLCGgfT2rJyKOS-BhbSViRyE9eiso2c9daDuKhTxYsExY2aJ0egE6kSqsTbZEOxMZ1NaNbPfNrnQj9s9KOBGTy4YIlQrtRjUlsFXtn44EyiWTlEoApWYocJcSW6LnrYLPjpeRAm8lFzrBNlgklIU5rfhff4IJWY-4zp-oUPmGQZABlWzls4mkSY8lUnkFazpWJkO6pu6EN8BL9z5a5P6PnJZ2XxN-r1i1aS8QYIUOoDuEJF-DoF7PvBA3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
در سمنان برای دومین شب پیاپی میان مردم و دانشجویان عراقی وابسته به حشدالشعبی درگیری شد.
این درگیری روبه‌روی خوابگاه عراقی‌ها در باغ‌فردوس اتفاق افتاد.
ماجرا مربوط به متلک‌پرانی و مزاحمت آنها برای زنان و دختران است که بارها اتفاق افتاده.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71278" target="_blank">📅 15:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71277">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FBMVO__gqV6r19mj_4svdlJiwjNnmmDD8CCdHjICh33Mu7sWLorEm1LxvkEmbB2aIcof5TM-Y5pL-CXZdT4OoAJV1sPsWViwiQSXYI1fjiu80Grbv1A0H5Yw6D5Bkb-l138vkOC_tO6etIv3xNUo-fPyruSYOXFEGr19cW_a-5Z8meWIylpJMsMPBI3Kb_FYkpEmxWfKETPxneY42SSBe8sXdg0WdDh3sjH77cDSQdd89I80RK5m7W9QTvvROPeh4yO7fO-lJixk8TMqdZPPegXfNV_-DSAOPBU13yosZN4L6iv6P6jG14sZoilAQWnmVgWisyfvvtXHNg9U12AP4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
امروز ۱۷ شهریور، تولد مجتبی خامنه‌ایه و ۵۷ ساله شد.
اگه زنده ای شمع هارو فوت کن
.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71277" target="_blank">📅 14:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71276">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed3b8e81d9.mp4?token=BKKkosu6eQtuBHbwdIARIlZyfRRhHO3CFPbUZoVw8FT8U94d-zOblR18x85W7-lkebt73A5JJ99YH3-zP-8WgfYpeSsYIDbV2Ivu8xoMkT3o-hWkrDjAkDuTmAyul9YHo33Awyv5WM8UuGIdaE09sac01T16NswmIMwaTNvtAiftHIQkSJw8VSIUVAllDbz8TQAUCrIzdG1WSZqc73d64oY78VRSx5RldInGTiFf8C0pr3ZMtFgwtXUit7__C0py6qd8I09gwPxqKpYElZEbQYUx2abKwwWeO9ksXOL7Ks1OBiUrlD_adkV3wF__JhFXlADt0lYCTSNF9AtEOaUBWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed3b8e81d9.mp4?token=BKKkosu6eQtuBHbwdIARIlZyfRRhHO3CFPbUZoVw8FT8U94d-zOblR18x85W7-lkebt73A5JJ99YH3-zP-8WgfYpeSsYIDbV2Ivu8xoMkT3o-hWkrDjAkDuTmAyul9YHo33Awyv5WM8UuGIdaE09sac01T16NswmIMwaTNvtAiftHIQkSJw8VSIUVAllDbz8TQAUCrIzdG1WSZqc73d64oY78VRSx5RldInGTiFf8C0pr3ZMtFgwtXUit7__C0py6qd8I09gwPxqKpYElZEbQYUx2abKwwWeO9ksXOL7Ks1OBiUrlD_adkV3wF__JhFXlADt0lYCTSNF9AtEOaUBWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
شب گذشته در سمنان، به افزایش قیمت بنزین اعتراض شد.
این اعتراض در پی تصمیم جمهوری اسلامی برای دو برابر کردن قیمت بنزین خارج از سهمیه یارانه‌ای از روز سه‌شنبه صورت گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71276" target="_blank">📅 13:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71275">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uo1PZwMl6sciPATxoUl-K73zx6kzp1tWgKJRlCoCIGc2fv7kxeJQIAx3fOUd5FjQwHjKpwqEjc1LCoVzX6ZnjOVbfPYcnIYlq1gpTwNSk-KNK4Rf2wxcXw9Y4YQbF3gGEBZ93WDXiPnBFj08Uo9RU36CfEn8fyDOhKPndelKDOx-iLy76z8gM64Wp0W2vaBqpv8CZR8s0j46mt_YN7EQ7GulOsz-cuYGXooa9Awz9Op9p_YVigFEBsg3dCfMIrnPGmFywQfpw8pPFcknxk2vG7S0acsx5itqpS1W9nnFvdhG_MIrHKwHS3U3M8J8pKFq7DbJieysMVKbLf3CghVYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مسعود پزشکیان:
جمهوری اسلامی ایران همواره با جنگ مخالف بوده و حفظ منافع مردم و امنیت منطقه را در پرهیز از آتش افروزی دانسته است.
اما چنانکه تا امروز در برابر تجاوز، دلیرانه به دفاع برخاسته است این مقاومت را تا پشیمانی کامل متجاوزان با قوت ادامه خواهد داد و پاسدار حقوق ملت بزرگ ایران خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71275" target="_blank">📅 13:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71272">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LbhQKvLJt4bUL2hV_qdnlYTMPBqbs6jOYsfVlf3yO4LiDk0-3knNMYhaMvH9zuKcsm_HQ1FkFCNc3Ksmu8I-9EV0pJ6bR1ih56z1kdqQNW8cfSRQJkpR8nSgBn0fNR51BH8WbFoYRueVuLwoPI_tkeMIDx2pv9WFp5U7NemKaWutIk2SRG1WJzx_RQzW5slsfVRrR-sn5PrGRJAs4E0WE17wj_u_3nMq8Kv-RpiwFZ7XDF8jSnUecjLDBNP6X0jgCCI7fqTlBdcxJrjbWboX83c35Ghu3eeXt8huBTxdvI7gJ5ayz2av9oLw8tFdob-PISAkGYReAHQWvsfpBfyyNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8833895957.mp4?token=Cwqq6tYAGGludgiFuzKZWM02pNhmkNyvEe0YY6BGloxWmaiELuxsGEsHVM-kt4FULghQsitc2y6ByEbItvLRcJKSrC-7nkgTm4_9IgpmxJhKiCCYx25HWKdsMNrhHhhMr4LiQ8SWir22Jp0QcEl5eN_psufU3QF3Weeef9P-fF4dBMfnZVkwmzBIF7hjH2Rbsq3hs2PImik5Zn4d0YrZsQK1QOnqeIJmKlY8VYULNkfUjoKWXyVDd4G3RV2qk_rcl4Siy4MfYOdSyG98p3Ch-8nVlXX5BQd8lLHjYdPRiu8KYpHDfk2LHDc9jt1rDIDFSkcRRDYtSrR5-xUOEfqp0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8833895957.mp4?token=Cwqq6tYAGGludgiFuzKZWM02pNhmkNyvEe0YY6BGloxWmaiELuxsGEsHVM-kt4FULghQsitc2y6ByEbItvLRcJKSrC-7nkgTm4_9IgpmxJhKiCCYx25HWKdsMNrhHhhMr4LiQ8SWir22Jp0QcEl5eN_psufU3QF3Weeef9P-fF4dBMfnZVkwmzBIF7hjH2Rbsq3hs2PImik5Zn4d0YrZsQK1QOnqeIJmKlY8VYULNkfUjoKWXyVDd4G3RV2qk_rcl4Siy4MfYOdSyG98p3Ch-8nVlXX5BQd8lLHjYdPRiu8KYpHDfk2LHDc9jt1rDIDFSkcRRDYtSrR5-xUOEfqp0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌧
بارش شدید باران دیشب در رشت که منجر به وقوع سیل شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71272" target="_blank">📅 12:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71270">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bpx8DXPSQWHpgP-SRMh9Rj6wc5foCq5yT6x4uYrSVnIuOvYFsqoUAc020kF_26iWckTFK_Wxl1BCrO7Xo3KsloRDZHWPFV1ucEbFtq4cduLZF12Pk7zYWNSbL0spb3KEqhV2dJEDO-fN3y8KgQh8uNPN1WToAYtu0L0Pa3aQ7L650r-P7UsqNa-8Mq5UzLopEMhcBJexyuLVh9JJb6iKVKJWmIjilI16NHCZOyQydpHpHCCbASsUXaWm5jbta81k2VoW7wJXIhullC-cIe1UjJF-zS0z__EChOh8J3pZqFpybKOqdAiHMUo7nXFVfhfdnCUbBbYhSRxxGbt9etx5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bd51248f.mp4?token=r-lRlHreGCYQasMQjkcgsrRNENaiGw5LDdwW8zBY_RMLVyU34UoweBUK9gfyBuAvIopyIf48zkax2MXwR4RQvs8VuqeDvhDbU5rx337LFVw98Okal0RxIxVyxmQ2N8HtY3w9sGPVspbpXHJFmuifmSt-opZwNnUlI-nR9xqIfurpZpbpxqjd2JUtqkR-sCgSryhySBBPr9R6455cCpf9kAy_P8Kk_9a6ufRhXcwiIolRoWOzrZerqqs4J5fkfvL9rXYkmo52wtQIao8Eg8TYOCIl5dSfPd-4jd-nKe0dTirInTbjLTjb5JZhqSIDZ8QQ2-7QE1kuocA9CvyDn40wwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bd51248f.mp4?token=r-lRlHreGCYQasMQjkcgsrRNENaiGw5LDdwW8zBY_RMLVyU34UoweBUK9gfyBuAvIopyIf48zkax2MXwR4RQvs8VuqeDvhDbU5rx337LFVw98Okal0RxIxVyxmQ2N8HtY3w9sGPVspbpXHJFmuifmSt-opZwNnUlI-nR9xqIfurpZpbpxqjd2JUtqkR-sCgSryhySBBPr9R6455cCpf9kAy_P8Kk_9a6ufRhXcwiIolRoWOzrZerqqs4J5fkfvL9rXYkmo52wtQIao8Eg8TYOCIl5dSfPd-4jd-nKe0dTirInTbjLTjb5JZhqSIDZ8QQ2-7QE1kuocA9CvyDn40wwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپاد اوکراینی به یک ساختمان مسکونی در پرم، روسیه، تقریباً در ۱۶۰۰ کیلومتری قلمرو تحت کنترل اوکراین برخورد کرد و یک نفر را کشت و چهار نفر را زخمی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71270" target="_blank">📅 12:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71269">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71269" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71269" target="_blank">📅 12:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71268">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzwhRA9rA8lO50hRbQmjsWpG0kQdHlr42tUi9JbKbM1eRVmu4xnD4dLv0XllumgfK65MwjgIX7tUmjuXJjBM_qtcFWUtfisfaqhb3VUeuLsko02oNyXNDzbqAJTl7-zMYsB-5JQZzgmEppJmcaBmMz3JQeF9imwsPuobnZsYrUETFJfwSfNB8RJ1FV7BrKGKjFWE-kysEtQikFHFm4GYYjiiHE62apvb9re0t-I-TX0Am2nwUug6SK26892q4meby3xsPFAvqd5OfXcNjZG7w0f_j4bAPz2EMq512NuHo7dS1OTyRSZIqodyt5tnFONC1V2rjGonrhC8-gu9O-rFgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
رئال مادرید
🆚
اینتر
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در ۵ تقابل اخیر:
⚽️
رئال مادرید: ۵ بازی ۵ برد و ۱۱ گل زده
⚽️
اینتر: ۵ بازی ۵ شکست و ۲ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71268" target="_blank">📅 12:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71267">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193f66d1ff.mp4?token=htCAcAera6tCxLv7SMi3KoSbB8HIscP7NZb0TDVRULP_Qh4CqXWrMRCokV4uHLDomGIi3GvO2yCH0C36u33nFNIuU4YQ9bam-C5nhttivrmRgK1TmMfKmvmnpybdlZb8dpGWNr-0UZFD61FVSQGqcC720l19CWblQ9-ERiWiS37asBQfgnJOC8uMckft5FolQPABKxSkZqdKfU2l4WWeXAp38k8wLeDR6xadRVUSHdUsjh1SZN42fDp3KSX7POlBwKvXtSsh_UVTclyaXowQAzx5CtQSD_Srdk-DtZVpZSGCy_cQ1Cx_G_ROJpoHDAl8YfTh8HNuuIjI14AMm6qT0DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193f66d1ff.mp4?token=htCAcAera6tCxLv7SMi3KoSbB8HIscP7NZb0TDVRULP_Qh4CqXWrMRCokV4uHLDomGIi3GvO2yCH0C36u33nFNIuU4YQ9bam-C5nhttivrmRgK1TmMfKmvmnpybdlZb8dpGWNr-0UZFD61FVSQGqcC720l19CWblQ9-ERiWiS37asBQfgnJOC8uMckft5FolQPABKxSkZqdKfU2l4WWeXAp38k8wLeDR6xadRVUSHdUsjh1SZN42fDp3KSX7POlBwKvXtSsh_UVTclyaXowQAzx5CtQSD_Srdk-DtZVpZSGCy_cQ1Cx_G_ROJpoHDAl8YfTh8HNuuIjI14AMm6qT0DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
حساب کاخ سفید در پلتفرم ایکس:
در روشن‌ترین روز و تاریک‌ترین شب، هیچ شرارتی از نگاه من در امان نخواهد ماند.
آن‌هایی که قدرت شر را می‌پرستند
از توان من برحذر باشند..نور فانوس سبز!
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71267" target="_blank">📅 12:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71265">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/658f8cd399.mp4?token=lLcPkYsv1O0bPiprKpFDcLJUUF37BpDzC6Rd26QnJ94T-gekCKRylVWo5nJYwhaeXy9MdppyxjzM0Ua5ts8KvOFob6yxZdIIRgqM_81o3hNZkQ1MfdGEz6NkgTL1CkbjWWTe1O1XioWSw3oWypmVl2UgCF9jgISm9HXlq0EFplSctYw9_2B7iGo1WQxnbicA9ONlF0oXIpQg34x12RxXOfm1KUxRtyFcdi1Cm1unrl_iw8k2Uxt6iWIraNfyjUmlILBEDKA56Eu1rGPYDffQaK-usflMcbC2vTM9S3DMKqmplgJCaYcvt5W9bOCNRLhm81XT6fJZ_MrT4YKLxQPtQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/658f8cd399.mp4?token=lLcPkYsv1O0bPiprKpFDcLJUUF37BpDzC6Rd26QnJ94T-gekCKRylVWo5nJYwhaeXy9MdppyxjzM0Ua5ts8KvOFob6yxZdIIRgqM_81o3hNZkQ1MfdGEz6NkgTL1CkbjWWTe1O1XioWSw3oWypmVl2UgCF9jgISm9HXlq0EFplSctYw9_2B7iGo1WQxnbicA9ONlF0oXIpQg34x12RxXOfm1KUxRtyFcdi1Cm1unrl_iw8k2Uxt6iWIraNfyjUmlILBEDKA56Eu1rGPYDffQaK-usflMcbC2vTM9S3DMKqmplgJCaYcvt5W9bOCNRLhm81XT6fJZ_MrT4YKLxQPtQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یکی‌ از مراسم های تولد در بالاشهر تهران
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71265" target="_blank">📅 11:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71264">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0de73320.mp4?token=O8Hq1R1vYSaZpSYOe986qrMlAZIPeW6NDzgTLQlLifhhOWLvApbcTBa3p95f7xngtwba9mMPrVhce-l2_WEfh2r2bU2FivJKnay4hKJp2WxnvPJeLf1fGl_Y9GKAfc2TFpfDugl4rMt2sqg2ax4Ocatz9wMyC1GxhFVP2OQARVhmthhphBfAiW3ibIfmTLqfxrqw1XcFoWu_9MSS9AWXkY_X7IwaAddYA0jGWAyBsZkdWm59vUw_kFO-dH7tapOdU3blUOZcsKp6jmfH5PV7cd7FlUtlZZJhHtu-BMFeMRHOSaGxkY2Kmg5H3zk9kuDQX9W_LSvplGcpX6v_dB6LkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0de73320.mp4?token=O8Hq1R1vYSaZpSYOe986qrMlAZIPeW6NDzgTLQlLifhhOWLvApbcTBa3p95f7xngtwba9mMPrVhce-l2_WEfh2r2bU2FivJKnay4hKJp2WxnvPJeLf1fGl_Y9GKAfc2TFpfDugl4rMt2sqg2ax4Ocatz9wMyC1GxhFVP2OQARVhmthhphBfAiW3ibIfmTLqfxrqw1XcFoWu_9MSS9AWXkY_X7IwaAddYA0jGWAyBsZkdWm59vUw_kFO-dH7tapOdU3blUOZcsKp6jmfH5PV7cd7FlUtlZZJhHtu-BMFeMRHOSaGxkY2Kmg5H3zk9kuDQX9W_LSvplGcpX6v_dB6LkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
یک پهپاد اوکراینی در طول شب، بمب‌افکن تاکتیکی سو-۲۴ روسیه را در پایگاه هوایی ساکی در کریمه با موفقیت هدف قرار داد
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71264" target="_blank">📅 11:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71263">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/233fc1eb07.mp4?token=vRGvnHENY1KuFwpc-6s9WT6QovUNvG5fd1HqSeAt1-egLaUYjWTJ4jpCkrMyi2wB3Ne6YensTS5I04f9yNzaA4_JYtiwfE1W6Yh6ajYD5C1QSjuGk1AdtYchkG0Wi9bpnsuZszNOZMoMVzXx_cVpF2iHIx1lpNeB42zfWXrGuh1LOzvimVBpWVK0tODYmUmKg5bXzg1MihZ8p3e_vcoIHqs7ueQtocOR45MhcZ4ak_n-fXa8FlOMeDNvM006sgAIjGHbSTDq2SAAXThYVIipD-3P-C-1iJRR2_-oKsioq22cCJ7u-2T_4n8-mBkaFdpKVwNkhcI81lUbmJ9zjIhxgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/233fc1eb07.mp4?token=vRGvnHENY1KuFwpc-6s9WT6QovUNvG5fd1HqSeAt1-egLaUYjWTJ4jpCkrMyi2wB3Ne6YensTS5I04f9yNzaA4_JYtiwfE1W6Yh6ajYD5C1QSjuGk1AdtYchkG0Wi9bpnsuZszNOZMoMVzXx_cVpF2iHIx1lpNeB42zfWXrGuh1LOzvimVBpWVK0tODYmUmKg5bXzg1MihZ8p3e_vcoIHqs7ueQtocOR45MhcZ4ak_n-fXa8FlOMeDNvM006sgAIjGHbSTDq2SAAXThYVIipD-3P-C-1iJRR2_-oKsioq22cCJ7u-2T_4n8-mBkaFdpKVwNkhcI81lUbmJ9zjIhxgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تهران، بیت رهبری، ۹اسفند ساعت ۹:۴۰دقیقه صبح
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71263" target="_blank">📅 10:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71262">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4221662e8f.mp4?token=tmXAti8-G9Q-vPZjvrauGG9mXf4xc71SnR4S1XCABYVe4IQYqTh7AIlDxoIUnIEKS5OWJVoUSobkL_2ommE9L2y-QPVuzpy-QDQrrF_d3saeFB6hR9bJdZKFYIhZVWHga_wM3I2crDm_9Xjz68L-FuduhMUX9GOrnFNnXoSIIIaj9B9Yccw5storvuVUJetM_oHK-vATrH5R314PUu_8LyM91LqVa1GPPZ8Dv7YIUzfdNQJIKGof8huWwEMiulDLm3_O4cb8WoZ8h3EE6GnMsd_JmMFx2bl1Dix9YAf4kltQkRp6NfjM6Ksjwh5igimwsXG70rp7wvyaP64aE-luxXtzEjD18e8dUP1MYYWXwDAEerQBobJc-vUM5pEbW9UKwqtC75Y_28CJXhWBJ2MwTf9rAjW4YrIvj5m4UfA6Py20ps0vxuuSadngsGAFtD8Q8JvGsaO6C35IxkSqNgk3O4Fe4D_kOoNnhSxCrROnakx5h1qCJ1EIZBPAZ5Lg8QKrIFgr4Bpp27A8aGMz4hY05udCVqRse0PiwBwMBXVKaP7J9GUZX_aOMkwniGp-jVVg6Izw2-8eQJ0FFyE1_45NMt-4bRA3UBANV-i2qWzqj05MrdvTM00XnRRE14v4Gy2IVGaYs1LCpVqK9JtGPBzSNWh222DOgy89Sf5sJ40HLBU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4221662e8f.mp4?token=tmXAti8-G9Q-vPZjvrauGG9mXf4xc71SnR4S1XCABYVe4IQYqTh7AIlDxoIUnIEKS5OWJVoUSobkL_2ommE9L2y-QPVuzpy-QDQrrF_d3saeFB6hR9bJdZKFYIhZVWHga_wM3I2crDm_9Xjz68L-FuduhMUX9GOrnFNnXoSIIIaj9B9Yccw5storvuVUJetM_oHK-vATrH5R314PUu_8LyM91LqVa1GPPZ8Dv7YIUzfdNQJIKGof8huWwEMiulDLm3_O4cb8WoZ8h3EE6GnMsd_JmMFx2bl1Dix9YAf4kltQkRp6NfjM6Ksjwh5igimwsXG70rp7wvyaP64aE-luxXtzEjD18e8dUP1MYYWXwDAEerQBobJc-vUM5pEbW9UKwqtC75Y_28CJXhWBJ2MwTf9rAjW4YrIvj5m4UfA6Py20ps0vxuuSadngsGAFtD8Q8JvGsaO6C35IxkSqNgk3O4Fe4D_kOoNnhSxCrROnakx5h1qCJ1EIZBPAZ5Lg8QKrIFgr4Bpp27A8aGMz4hY05udCVqRse0PiwBwMBXVKaP7J9GUZX_aOMkwniGp-jVVg6Izw2-8eQJ0FFyE1_45NMt-4bRA3UBANV-i2qWzqj05MrdvTM00XnRRE14v4Gy2IVGaYs1LCpVqK9JtGPBzSNWh222DOgy89Sf5sJ40HLBU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
🔞
وایرال شده از رقص و شادی سربازان ناو آبراهام لینکلن توی کلوب شبانه توی پاتایا تایلند
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71262" target="_blank">📅 10:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71261">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b860e39243.mp4?token=J5tNOuVnGxwQHRKuFpIIJOgGfsKWQuiVAYEigOpZAPWgMPV6jMW3gOvNXuCcIMs9-S7DkBVXRCR-ImF9EzAlX6JblsgWO7bmxAQzJDWiVl-Z-E0IRo3nnaSWnXdGOY83zh8vp3E1J-Qfhmt1BNTeCm6ITE01YALTM68AfwQow_EpKlkjSOGl7q-M4XGrZd19yySP15amaGRuAxr_sB1Cg3-w_hlmZmUrXAbCs1pRtdECc5rOh6YRmajv2Vqs2_959_5UXhO1kNQqct4Jw_m7D61CD1f3pqr4yjpyvoB0LsN_pqm7A9nsdfgSLqxbS5S2hEJFst-GCS3ZgYzo4L6yig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b860e39243.mp4?token=J5tNOuVnGxwQHRKuFpIIJOgGfsKWQuiVAYEigOpZAPWgMPV6jMW3gOvNXuCcIMs9-S7DkBVXRCR-ImF9EzAlX6JblsgWO7bmxAQzJDWiVl-Z-E0IRo3nnaSWnXdGOY83zh8vp3E1J-Qfhmt1BNTeCm6ITE01YALTM68AfwQow_EpKlkjSOGl7q-M4XGrZd19yySP15amaGRuAxr_sB1Cg3-w_hlmZmUrXAbCs1pRtdECc5rOh6YRmajv2Vqs2_959_5UXhO1kNQqct4Jw_m7D61CD1f3pqr4yjpyvoB0LsN_pqm7A9nsdfgSLqxbS5S2hEJFst-GCS3ZgYzo4L6yig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیلم ترسناک منتشر شده از یه بیمارستان روان‌پزشکی و رفتار یه بیمار ساعت ۳ صبح بخاطر مصرف مواد مخدر شیشه، گل و...
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71261" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71260">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84f97591b9.mp4?token=v4b8DFla_VEBAs96aO67SimiJoX0dAV1Kmm1xdBH6O3VRKiVNIwOHi4HPOtPuWk9WowWlSuF1vo-mSTWfNGpuFN57JHD-l1rUR7W_Mch_Ch2ZSzpfQdLrUZpsX9ivcBnNJBJwnk8XU6dvcnz1MxUYHmHhAgz58yZ7WmlfGK8PfbORVVcw5ybZodpOSDUdtq_S6Fgje6ThKTWgmVPKQSZNLYl_C652jzVim0HfL258EVe_SfMQqb4vxdtLNzIujKspN_7dglvvOVuTC8XXBVusz1Yz9x9GlgdQlrj19snEc-xK-_5HW_5vT6z_5wp_dGJCUd0OlQNYZwkphYMydPo4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84f97591b9.mp4?token=v4b8DFla_VEBAs96aO67SimiJoX0dAV1Kmm1xdBH6O3VRKiVNIwOHi4HPOtPuWk9WowWlSuF1vo-mSTWfNGpuFN57JHD-l1rUR7W_Mch_Ch2ZSzpfQdLrUZpsX9ivcBnNJBJwnk8XU6dvcnz1MxUYHmHhAgz58yZ7WmlfGK8PfbORVVcw5ybZodpOSDUdtq_S6Fgje6ThKTWgmVPKQSZNLYl_C652jzVim0HfL258EVe_SfMQqb4vxdtLNzIujKspN_7dglvvOVuTC8XXBVusz1Yz9x9GlgdQlrj19snEc-xK-_5HW_5vT6z_5wp_dGJCUd0OlQNYZwkphYMydPo4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
⭕️
گزارش‌هایی از تماس‌های ناشناس با ساکنان جنوب ایران؛
درخواست برای خودداری از حمایت از سپاه در درگیری‌های احتمالی آینده
بر اساس گزارش‌های منتشرشده، اخیرا تماس‌هایی از مبدأ نامشخص با شماری از ساکنان بومی جنوب ایران برقرار شده و از آنان خواسته شده در صورت وقوع درگیری‌های آینده از سپاه پاسداران حمایت نکنند.
گفته می‌شود این تماس‌ها با کد کشوری سوریه برقرار شده‌اند، اما هویت و وابستگی تماس‌گیرندگان تاکنون مشخص نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71260" target="_blank">📅 09:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71259">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71259" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71259" target="_blank">📅 01:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71258">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Admc7LCPpOLRHo8eekxTwlKOmVuZwUpUEpfQkFs83Ymiapj9260_DjQBn5p4W3GfkxYE9Pd28b7WRYzB8VMCzwS7lbEyPFbVzhkOnR3Gq1A90hmBs3Q6cTESIapkHMDyUyATAh1Jf9NSfI9PNwvq6UL9hnSQF4Il0yfgQsqsnResa-X-60wY7irM3KelyvwGm00f_3cqYzExrBNCZ8syJlhDDsIXrcyNHbgKWNT28ajhI13_BZ2P82fceKst3ffnhwY9_1Fs4IsFDvwWX_WIKCw9iIcaoAeSyD-3mpJj_z4Szol-ow6-GTMXdulofGVE2-87Rh9r1Pe6FwYlxh32GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان
US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71258" target="_blank">📅 01:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71257">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⭕️
⭕️
از دقایقی قبل نرخ سوم بنزین به 10هزار تومان افزایش یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71257" target="_blank">📅 00:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71256">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56a780504.mp4?token=pB60hY3RaxbWE2CPOi6U4EjXafKsfSHF2dHK3WBJnny_FXbMC-zbsZ-RiUPfq4nOY97Kerx09cjP-1CIcxZLnD-JizddnCZJuZAIn7X3Xda-k5287GwOaiNCgp6IGkVadVmMRfnJFW4aSN0V3MxwjbcW4Ww7nwYz93b0RHGq7SehfcUPKhsYQejsyjlUlJVsv8-CqJHrHlsnlRCIMp76asvLRV0_LJFWBZ9by_4b2Ox3MokFyw1EiZPcMY5LFzzVywqVhCpii-r3Y2VKvEryvGK9gu9wr9XbJSWlayLDoz5IX-ZacPvCyL1Ho6gCtg0OHERCs30ZtWUkrEUjSpEOJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56a780504.mp4?token=pB60hY3RaxbWE2CPOi6U4EjXafKsfSHF2dHK3WBJnny_FXbMC-zbsZ-RiUPfq4nOY97Kerx09cjP-1CIcxZLnD-JizddnCZJuZAIn7X3Xda-k5287GwOaiNCgp6IGkVadVmMRfnJFW4aSN0V3MxwjbcW4Ww7nwYz93b0RHGq7SehfcUPKhsYQejsyjlUlJVsv8-CqJHrHlsnlRCIMp76asvLRV0_LJFWBZ9by_4b2Ox3MokFyw1EiZPcMY5LFzzVywqVhCpii-r3Y2VKvEryvGK9gu9wr9XbJSWlayLDoz5IX-ZacPvCyL1Ho6gCtg0OHERCs30ZtWUkrEUjSpEOJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇱🇧
عادی‌سازی سقوط تپه علی‌الطاهر توسط طرفداران قالیباف
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/71256" target="_blank">📅 23:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71255">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23e98b62df.mp4?token=Ci3TjndQERCcSAq3WvCxvLiYu3i7AERhqMSjNRk8uuFgaoq1PlnMdNUa7JdaIKJ0k7lsyxrXo1K7tuxKCW_isjx3OIcfLtaEwtHCbBK8A4BDjljl9SNfSieG1pM_eihVLzGBZe1UJsaH-tGA6KGL3qwe38eNlk5yxnKIoyseqd_Il27PS0vOg2NAieLd9-D6N8jc5dZR6k3J1KY_bBh9M9RH3MefJKm0ECATjIgYagk1bm6HypfHHsOfsQGFLr-w627ukqnd7Fgawpe_nKPqjprgBZVXL-JvFgAnFpJGc_Nc3tJjiEmlwsO4F1GZro2Jbj5ytFBlYg_7-G1Zyjj8Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23e98b62df.mp4?token=Ci3TjndQERCcSAq3WvCxvLiYu3i7AERhqMSjNRk8uuFgaoq1PlnMdNUa7JdaIKJ0k7lsyxrXo1K7tuxKCW_isjx3OIcfLtaEwtHCbBK8A4BDjljl9SNfSieG1pM_eihVLzGBZe1UJsaH-tGA6KGL3qwe38eNlk5yxnKIoyseqd_Il27PS0vOg2NAieLd9-D6N8jc5dZR6k3J1KY_bBh9M9RH3MefJKm0ECATjIgYagk1bm6HypfHHsOfsQGFLr-w627ukqnd7Fgawpe_nKPqjprgBZVXL-JvFgAnFpJGc_Nc3tJjiEmlwsO4F1GZro2Jbj5ytFBlYg_7-G1Zyjj8Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یادی کنیم از اوستاااااد خانعلی‌زاده که در دوره جنگ 12 روزه معتقد بود جنگنده های اسرائیلی هرگز وارد آسمان تهران نمیشن چون باید چندصد کیلومتر داخل ایران بیان و برن و این کار ممکن نیست  و اینا همه شایعات مجازی هست!
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/71255" target="_blank">📅 22:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71254">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚫
فوتبال مملکت هم اوضاع جالبی داره.  خداداد عزیزی امشب کلش فوق‌العاده کیری شده و اینجوری خواهر و مادر امید عالیشاه رو به فوش کشیده
😳
😳
😳
😳
😳
@News_Hut – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/71254" target="_blank">📅 22:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71253">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
⭕️
دقایقی پیش صدای چندین انفجار از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/71253" target="_blank">📅 21:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71252">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ead429175.mp4?token=O-5jHqY-DmB9UoaboWrjq1VcKxIhmK0Icy7aCPd0x5Un13Ui6T6L-pd-7bZ-tXCLEFOsT89ltq7bJW2iwaJwqJGvDmjuYsM12wohiQBJxvu6Jsj8VNY0yCwOSQvvIxbZTd3IxsTNxaeodHIsdOCSz9pwem3UVzme4MWepVYpD57t0jVKhmBMt8gmYKhlS4kOg4cuFU1FnLdhNOZPjzpDHEzqUCnO9tVA4n-cbU3m1q3_62ycrYkcWJEU5S8OPmq1qwe53pMoZbjM74NO2BIcxM_dcY4w3vuBxbEA1c8rbn6rK7LqGoVvJqWBp6ePsFNEZ3Bkr4huumOJpLBd00dj-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ead429175.mp4?token=O-5jHqY-DmB9UoaboWrjq1VcKxIhmK0Icy7aCPd0x5Un13Ui6T6L-pd-7bZ-tXCLEFOsT89ltq7bJW2iwaJwqJGvDmjuYsM12wohiQBJxvu6Jsj8VNY0yCwOSQvvIxbZTd3IxsTNxaeodHIsdOCSz9pwem3UVzme4MWepVYpD57t0jVKhmBMt8gmYKhlS4kOg4cuFU1FnLdhNOZPjzpDHEzqUCnO9tVA4n-cbU3m1q3_62ycrYkcWJEU5S8OPmq1qwe53pMoZbjM74NO2BIcxM_dcY4w3vuBxbEA1c8rbn6rK7LqGoVvJqWBp6ePsFNEZ3Bkr4huumOJpLBd00dj-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
دیشب خبرنگار لبنانی داشت توی نبطیه گزارش تهیه میکرد که همون لحظه به شکل پشم‌ریزونی اسرائیل حمله کرد به اونجا و همچی قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/71252" target="_blank">📅 21:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71251">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a7bd5cfa8.mp4?token=lMf7IFBeFOhQR0_uLVJcjTmmvxIVuxqjhrOxPEd113_3z8hUeN7RplXRQGhGQ411YCFp526L6IPsStMkDVjLC34J6264PgGJqlJlPOSdewEq5CEIOH6lJ84gRQrxGGQEWshdOOcbtyjiR_NMSWrnrbGfedbc83kL6IXJLPXjig_KMkHKgXZO8SywLwz_r59JC-5nOD24WLDqa72KU7ZhQyDLUbxm2Pi7c_vDRKcd0xMODnKFiSXKczzB526Ll4Kt-WZL4MMwIgrB-r_DXgwxvSX8SP2J2mt3jWYz9PAq1LOI81Va0cz8Rz2mim7ipLGxls42QW4hG5PWFesO23O0piOPGJbFYrcQJtwala6gTqFd4wcKerupPxpYqymSW4pMsdey863ZtzBadmzaM0-GOwm7fu9r5rxiG3A5VJOCOEQli-hRLyiQ82Z97hGIOeVdPbf5ML7StMbDnXdC_8r0T5TWw2ad9vfR48ubIz5t1ppXEL1wpeOVEKn-2oo8-PbNyjuFsPK7BnUeEHM6qxQgs09AVZuWu964eGgD5eGcYUAvjevU30HFTXsyT4P95DMORxTpOa9RzHUV_9ZJEjKCGYxDCsachejAOz3Rl7db0ze3sSW5qZ-bb6sJxlrbz2u6OQWuww0pqbkEwSKJ4Bj9alNmCPGM0cGHAuldSoq2MJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a7bd5cfa8.mp4?token=lMf7IFBeFOhQR0_uLVJcjTmmvxIVuxqjhrOxPEd113_3z8hUeN7RplXRQGhGQ411YCFp526L6IPsStMkDVjLC34J6264PgGJqlJlPOSdewEq5CEIOH6lJ84gRQrxGGQEWshdOOcbtyjiR_NMSWrnrbGfedbc83kL6IXJLPXjig_KMkHKgXZO8SywLwz_r59JC-5nOD24WLDqa72KU7ZhQyDLUbxm2Pi7c_vDRKcd0xMODnKFiSXKczzB526Ll4Kt-WZL4MMwIgrB-r_DXgwxvSX8SP2J2mt3jWYz9PAq1LOI81Va0cz8Rz2mim7ipLGxls42QW4hG5PWFesO23O0piOPGJbFYrcQJtwala6gTqFd4wcKerupPxpYqymSW4pMsdey863ZtzBadmzaM0-GOwm7fu9r5rxiG3A5VJOCOEQli-hRLyiQ82Z97hGIOeVdPbf5ML7StMbDnXdC_8r0T5TWw2ad9vfR48ubIz5t1ppXEL1wpeOVEKn-2oo8-PbNyjuFsPK7BnUeEHM6qxQgs09AVZuWu964eGgD5eGcYUAvjevU30HFTXsyT4P95DMORxTpOa9RzHUV_9ZJEjKCGYxDCsachejAOz3Rl7db0ze3sSW5qZ-bb6sJxlrbz2u6OQWuww0pqbkEwSKJ4Bj9alNmCPGM0cGHAuldSoq2MJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سردار محمودی بعد مصرف یک بَست:
موشک رستاخیز ایران می‌تواند در لحظه اصابت ۸۰ کیلومتر مربع را نابود کند
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/71251" target="_blank">📅 20:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71250">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkQOLoomwJqV_KXCOcV8r64XjagDSCNaRQvQrHyBI5hcQZRiq1pDMNGxrao2vcLzyDxirLhsz9Q3Oa0davzDyG6iOv2RGR2XZ6QtnWLwyqCCxzKDJ9ELn8IkxM-Y40omcRKl73IMXIiCS2ISZScAj-LOpJfS4_0jSUivnhZKqMfocGDJwPYAH7YYQzd6U7FPyr7WoBg8CnaBRJ5Xs08hGVFgOQMZL_hmh_DVstoNS9NYb1BByFpgD60baHMWjfYZTHdS3KdEKt_t7iWnBYwR15RvmBxcpWuVpW_XNVI1DfeqjsR4jQajZE7kjnglgUMaSX3a9fwn2zOXE0T_bjQ64Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
🇺🇸
ترامپ بازنشر کرد:
سیاستمداران ارشد ایران خواستار پایان دادن به جنگ هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71250" target="_blank">📅 19:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71249">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807f8a83aa.mp4?token=p1Yle5HVFGgGkKAI-lbal5ot-YAb-oPo0zFp6LqZJ38QTh8a5J6_kLGz-buBVmi_6-FgyXLQY4p-4qjaLNqgt_uhTb9_TQ4UECYLZetZffafhsjDWmF9ELdsa_wB3w4CK6Y00nI8CjUdN7ClCPglxjsHPpWrXxEeETedFtN4uARCka2Xv2r4TDCX7bE8gtXqHSgmHGyfsONGuw7f4YyjFcapwSSevjO2AosznlOXoFBl2slzCcXgEA7E6rIRuEBCOWvwTvQEebGUIwy5VNzaE-6r5ZdqFAnxlqc0pnr3VyB8b81iHHzDesvPQO6P1oYVoD6YvZotkJqJCLmV-V8EpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807f8a83aa.mp4?token=p1Yle5HVFGgGkKAI-lbal5ot-YAb-oPo0zFp6LqZJ38QTh8a5J6_kLGz-buBVmi_6-FgyXLQY4p-4qjaLNqgt_uhTb9_TQ4UECYLZetZffafhsjDWmF9ELdsa_wB3w4CK6Y00nI8CjUdN7ClCPglxjsHPpWrXxEeETedFtN4uARCka2Xv2r4TDCX7bE8gtXqHSgmHGyfsONGuw7f4YyjFcapwSSevjO2AosznlOXoFBl2slzCcXgEA7E6rIRuEBCOWvwTvQEebGUIwy5VNzaE-6r5ZdqFAnxlqc0pnr3VyB8b81iHHzDesvPQO6P1oYVoD6YvZotkJqJCLmV-V8EpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
به تازگی یه چیزی مُد شده به اسم «جوجه پارتی» ، تو این پارتی، پسرا رفیقای دوس دخترشون رو به همراه رفیق سینگلشون به این پارتی میارن، تا برای همدیگه جوجه بکشن و از سینگلی در بیان.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/71249" target="_blank">📅 19:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71248">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pl1KEsuQksmRdYbsaGpmB4RK3k17ZFul8EFGeDgqT-lLq999OP69VlxyFCDfvobHcSs-hUTiVNJEB7nl9Zhg3FBMXBovpipsKVzboTx_hR1DiKF2qUKHAtzGumtwNPuSwK5bWJLV-lySLMctOhyxLinj_17u6xdkIuq-3bCHAzfO07mIXvJDcBzGHR-tsI0pSWUuIf5teSaRx9Z0464qK4dXQXi0Iv8Byem47uD_PjU6hoQDwRu8TV4wRXnj6iuOfCr2LzgpxzXdJ3BvDfk6nYEnyp87ncD3FX_gcPg0vauqzx6wS3aesTNcXD_JbbCVMJ5o1bbpeMAfkZtJHQYHKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه موضوعی هست که فکر می‌کنم تقریباً همه ما به‌نوعی باهاش درگیریم؛ هزینه و شرایط بنزین.
شاید خیلی‌هامون هر روز درباره‌ش صحبت کنیم، غر بزنیم یا فقط سعی کنیم با شرایط جدید کنار بیایم، ولی در نهایت چیزی تغییر نمی‌کنه مگر اینکه صدای تعداد زیادی از مردم شنیده بشه.
برای همین این کارزار راه افتاده تا نظر و درخواست مردم درباره این موضوع جمع‌آوری بشه.
من خودم اینو امضا کردم و فکر می‌کنم اگر شما هم با موضوعش موافقید، چند دقیقه وقت بذارید و امضاش کنید. حتی اگر فکر می‌کنید یک امضا تأثیری نداره، همین امضاها وقتی تعدادشون زیاد بشه می‌تونن نشون بدن که این موضوع برای تعداد زیادی از مردم مهمه.
اگر دوست داشتید، لینک کارزار رو برای چند نفر دیگه هم بفرستید. شاید همین کار ساده باعث بشه افراد بیشتری از وجودش باخبر بشن.
🔗
https://www.karzar.net/346254</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71248" target="_blank">📅 19:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71247">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71247" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71247" target="_blank">📅 19:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71246">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8Cqj5oUmJS3RIRiEmlHa-0O6OeLxije8aQRtZ3_gqJZZ_UcK1vAKkbB2dKpFqLh1kWvK_ryUTf6u2LqE2R3JmspcXyDE5WQUzrkuzR1nWm-7GDy_wWrstrTsfr0utIdSMS2TZCxRL9XmIrJ5b66oMrUrlnfudVBGNS8Y1r-SrCA4MddjjSZRZ4Ko9bKbraHEdDj29j60TcQoPc9UJ-8Cnds4ckZAcD04cEnXu29RUqCvn1RD6bKdibtxmx_iU7sPxSfgpl_j-aiy3HFYc7mNkVIoh4O2G_Ydo24_W4-exolazlbeU1aZiTDSDZAGPzpNib2mQzl7RKFsXLpN_FYOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71246" target="_blank">📅 19:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71245">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">▶️
🇱🇧
🇱🇧
این ویدیو رونمایی شهر موشکی عماد است که مو به مو طبق شهرهای موشکی و پهپادی سپاه پاسداران ساخته شده؛
دو سال پیش حزب‌الله لبنان از این شهر موشکی زیر کوه‌های علی الطاهر رونمایی کرد.
جمهوری اسلامی بیشتر از خود حزب‌الله لبنان خرکیف شده بود؛
از برنامه ثریا تا اخبار سراسری صداوسیما تماماً افتتاح شهر موشکی عماد با ۴۸ کیلومتر تونل بود که مدعی بودند ساختش چندین سال طول کشیده و اکنون تسخیرناپذیر و نفوذناپذیرترین دژ عالم است.
این شهر پس از سه ماه محاصره توسط ارتش اسرائیل سه شب پیش در سکوت خبری تمام رسانه‌های جمهوری اسلامی سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71245" target="_blank">📅 19:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71244">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c892ca398.mp4?token=P6qvnAmRlLYC7g3Hxb8pNtIWcHiaue2CRMY92Gu-Bx2U4tGRGUQfMj_j_TnTiuPt8inmEIUepIqviB7x0iYJ_AqFhsiLGciZlyyaMHYRRExRHkRxeaZfOj3nBLKjUJ0Kk1UhQash9ZpDOoedC6V2B73Zl1-edWocK2Q9exwmFsI3rcgFF3_PpDMN8WaMq2vEtfU_TrJXfuhGR9Y4L3mjjElRpBKbqle6nUS10stt-Kr1_JlW5xLeXoAoMd9L4ZO0nDOjXUIq8DYWa10HCqBuVTP9WRlbU9BzbXjDzhSj4i93sSPTtZmF1xSsJMVSyJ1K8qyUd_VaByw5J7vFhO2HKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c892ca398.mp4?token=P6qvnAmRlLYC7g3Hxb8pNtIWcHiaue2CRMY92Gu-Bx2U4tGRGUQfMj_j_TnTiuPt8inmEIUepIqviB7x0iYJ_AqFhsiLGciZlyyaMHYRRExRHkRxeaZfOj3nBLKjUJ0Kk1UhQash9ZpDOoedC6V2B73Zl1-edWocK2Q9exwmFsI3rcgFF3_PpDMN8WaMq2vEtfU_TrJXfuhGR9Y4L3mjjElRpBKbqle6nUS10stt-Kr1_JlW5xLeXoAoMd9L4ZO0nDOjXUIq8DYWa10HCqBuVTP9WRlbU9BzbXjDzhSj4i93sSPTtZmF1xSsJMVSyJ1K8qyUd_VaByw5J7vFhO2HKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از لحظه فاجعه انفجار تانکر حمل سوخت در سنندج که باعث مرگ 11 نفر شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71244" target="_blank">📅 18:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71243">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08df0f1761.mp4?token=PCHmydCzfHv9HCrX__5sz21pkUHlhf6B-_mnUocO1UyqeUDg2mB3NCE3zK-5Yz0JK9l12GgY3t8xNKYbN69lZ8bvFblQJis7ppSlX2NHNeEABBSVi3U0hhuIZgkH_M2NsKR4B1Onwd3A9F62h3KEePDMKb4O-VORGTKmP5iL_Fif2Ks7isDxZBerYD8UTDBsfJtsDux0d75mpkn_iqwO36BOM23joC_oEFKzqlpcbExye2fljLIqt4LY6OdLYj7CeVLIQMJKHne81bCMg3xNksXu-2fev7Kd148_V5T_i8b7d-PakiZehB2O0abuEllUpolTMHvZQohs8n3GfQc3Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08df0f1761.mp4?token=PCHmydCzfHv9HCrX__5sz21pkUHlhf6B-_mnUocO1UyqeUDg2mB3NCE3zK-5Yz0JK9l12GgY3t8xNKYbN69lZ8bvFblQJis7ppSlX2NHNeEABBSVi3U0hhuIZgkH_M2NsKR4B1Onwd3A9F62h3KEePDMKb4O-VORGTKmP5iL_Fif2Ks7isDxZBerYD8UTDBsfJtsDux0d75mpkn_iqwO36BOM23joC_oEFKzqlpcbExye2fljLIqt4LY6OdLYj7CeVLIQMJKHne81bCMg3xNksXu-2fev7Kd148_V5T_i8b7d-PakiZehB2O0abuEllUpolTMHvZQohs8n3GfQc3Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣️
طبق قانون، استیکر و گیف خنده داری که از رفیقت میسازی جرمه...
و میتونه ازتون شکایت کنه و تا 1 سال حبس و 5 تا 33 میلیون جریمه نقدی داره.
اینکه شوخی بوده هم هیچ تاثیری تو مجازاتش نداره
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71243" target="_blank">📅 17:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71242">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff06303045.mp4?token=hGly5b9QZCUamm2okia8ZU_jg0FYCZccSPEri8nhNlPw-dUhIPaVwEAFvsozpWUYMSyTz_pnkN7dg2DGvwIzHlRSXiU0ixF3O0860OhrApbg3CqUph-TiclepPmQXSJgWZ23yzZilfx2lGH98YtuSmkWy6R5zWRQANQ9pIEe4bHpCXKe5ZCB0UxvctmtR6Xsp6_ZTuIiiAJ6nCQVRPmGpjlHxXQYYyQ9Csy3ENFhAAzfMoQCQX9KkQPMaYZH1i-WRQf0zDX-YZHb-XwQuFWQ_n3yhxl8ultvgfSvBctsAfpGq9qxrBARya3owhc-6hQetuXtLj0BQgATaGYDJJX_k1YaeY32ULHP40v36kn5sLfFDMdEbSPuvWbvnYFJCxr4U6_8uuPaKyVXb8PkBh6GVjkxvRymHhkJgCeMcOydzkwvsOTlkbBdCBBzmte2EKgq4UApMm-fxiv4cPuwgGwhRnZYgjedKXT-QeqM2G91-U97LOMTFmp7siF5TQK0SPv5FYRSjESU9Vv79pSMeDBnlH2MyItPyviAo2xof-BMCTZ23oRiknu5GWblJFAIzLHhDTwfbLgeA1exVJ_TLrDn-3AUUNBDWJvlD4ib1PuJeMmhvCs-vkAP82RbmJXKWNTuFelJu8O_7m-xjD7KuOW2M9rgnoz9DD_kO_NACflO9uM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff06303045.mp4?token=hGly5b9QZCUamm2okia8ZU_jg0FYCZccSPEri8nhNlPw-dUhIPaVwEAFvsozpWUYMSyTz_pnkN7dg2DGvwIzHlRSXiU0ixF3O0860OhrApbg3CqUph-TiclepPmQXSJgWZ23yzZilfx2lGH98YtuSmkWy6R5zWRQANQ9pIEe4bHpCXKe5ZCB0UxvctmtR6Xsp6_ZTuIiiAJ6nCQVRPmGpjlHxXQYYyQ9Csy3ENFhAAzfMoQCQX9KkQPMaYZH1i-WRQf0zDX-YZHb-XwQuFWQ_n3yhxl8ultvgfSvBctsAfpGq9qxrBARya3owhc-6hQetuXtLj0BQgATaGYDJJX_k1YaeY32ULHP40v36kn5sLfFDMdEbSPuvWbvnYFJCxr4U6_8uuPaKyVXb8PkBh6GVjkxvRymHhkJgCeMcOydzkwvsOTlkbBdCBBzmte2EKgq4UApMm-fxiv4cPuwgGwhRnZYgjedKXT-QeqM2G91-U97LOMTFmp7siF5TQK0SPv5FYRSjESU9Vv79pSMeDBnlH2MyItPyviAo2xof-BMCTZ23oRiknu5GWblJFAIzLHhDTwfbLgeA1exVJ_TLrDn-3AUUNBDWJvlD4ib1PuJeMmhvCs-vkAP82RbmJXKWNTuFelJu8O_7m-xjD7KuOW2M9rgnoz9DD_kO_NACflO9uM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
🇰🇵
روسیه و کره شمالی یک پل جدید را در امتداد رودخانه تومن افتتاح کردند. این پل دو کشور را به هم متصل می‌کند و با گسترش همکاری‌های نظامی و اقتصادی این دو کشور، اهمیت این اتصال نیز افزایش یافته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71242" target="_blank">📅 17:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71241">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8cf25fef.mp4?token=nqkzNgU9IQKtYHFePwZaHc51qkfT_cfl7z2b_OHa5FiUnWl_3r9BYHjQp4vpZfzXaxQmdrs9zCqLz0TtiJGp7k5liDimKbLsbrY0ioZyN4VmxZ0oV6_zRkTA-nbHWii83s_T-Or_nDoQafextGziYR92RhpBvCBhVsb-zTajUznjPhc2KyOYsl_QqBgVxIqTM8-gtFDOSVMF3MJeR_exSn8sVLO18iZInvSybOaDvzsV86nUmOJz45ge8VoqfSX1AWNcNVBm5mpgmUd0Mfx2TnUOLF6hk13JiE7f9EtfhhqMrhEJhmfU6A5toU6ghXvbyneyEAztGSZ5yPN-fLeVWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8cf25fef.mp4?token=nqkzNgU9IQKtYHFePwZaHc51qkfT_cfl7z2b_OHa5FiUnWl_3r9BYHjQp4vpZfzXaxQmdrs9zCqLz0TtiJGp7k5liDimKbLsbrY0ioZyN4VmxZ0oV6_zRkTA-nbHWii83s_T-Or_nDoQafextGziYR92RhpBvCBhVsb-zTajUznjPhc2KyOYsl_QqBgVxIqTM8-gtFDOSVMF3MJeR_exSn8sVLO18iZInvSybOaDvzsV86nUmOJz45ge8VoqfSX1AWNcNVBm5mpgmUd0Mfx2TnUOLF6hk13JiE7f9EtfhhqMrhEJhmfU6A5toU6ghXvbyneyEAztGSZ5yPN-fLeVWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
معاون وزارت ارتباطات :
حتی تو شرایط جنگی هم اینترنت قراره برقرار بمونه و همین که الان اینترنت وصله، نشون میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه؛
اینترنت پایدار و باکیفیت جزو حقوق اولیه مردمه و خدمات ارتباطی باید ادامه داشته باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71241" target="_blank">📅 16:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71240">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a6ea773c3.mp4?token=Da25xBE0bz5xty66C_tR3nZyxXX-cY2AgslOZjtFO_nNgCMgYnC9axzIQk-yuQ2sfHfhpvMwLYAqarCE_C9V6MgDKBtcOMmbqAukLhTWmbr32eRZZ28zSmgbBv9gWcfNGLkCOiXrNc1DLgQbJXokT2L5t_hz9CZbhxX9F4bLAyRAfof1O-7Y8v6rYu1VnVcpgH7nwRGw3QU9L7snZ-577y_nVzSh_b19OGm0mDFYoK_wyqmGOQC1rNy2uZSU5kNDZf4qgM3g2RTbA1ncABeR_nBBh_CgSogfziJEI21qWxebL7Ra1NgjdyyYGTMhOjZJVDjdb7MTaa6nvbzip7mDJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a6ea773c3.mp4?token=Da25xBE0bz5xty66C_tR3nZyxXX-cY2AgslOZjtFO_nNgCMgYnC9axzIQk-yuQ2sfHfhpvMwLYAqarCE_C9V6MgDKBtcOMmbqAukLhTWmbr32eRZZ28zSmgbBv9gWcfNGLkCOiXrNc1DLgQbJXokT2L5t_hz9CZbhxX9F4bLAyRAfof1O-7Y8v6rYu1VnVcpgH7nwRGw3QU9L7snZ-577y_nVzSh_b19OGm0mDFYoK_wyqmGOQC1rNy2uZSU5kNDZf4qgM3g2RTbA1ncABeR_nBBh_CgSogfziJEI21qWxebL7Ra1NgjdyyYGTMhOjZJVDjdb7MTaa6nvbzip7mDJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آخوند قاسمیان:
برادران یوسف 11/11 وحدت کردن یوسف رو انداختن تو چاه، این که وحدت نیست، وحدت باید حول محور رهبری باشه..
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71240" target="_blank">📅 16:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71239">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/98f065761f.mp4?token=kgWfI1xxQxEabyl7Vp6gZr6p4vHekXW21vt0h18n0D5ugy51k12fTocK3gNfDN7wM2zry22FeeDN98JsO4ckfN7jd3Qir5kIua60sRDpzRh23vGOsvDcJIcJP9mrpQ5R7EcGiGsl025JXL9jhrBEiot-gRcxlpQqZpd5gay4l1FO1TKOUDs25HvW-PBFtwL4gGIebo-AAc0kr6oFMvYaL1jWC-bJu1dVTSdp79AnpamVo_rIe93sz7Bw624JPAR1rMpSkAMu8DN5L_lPPxpKArnFJCJT7a_BLt-3A6ad5oxAb1xXQs3skko8JT92rXOmQWuxUWApMO2YcbJ8atDisA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/98f065761f.mp4?token=kgWfI1xxQxEabyl7Vp6gZr6p4vHekXW21vt0h18n0D5ugy51k12fTocK3gNfDN7wM2zry22FeeDN98JsO4ckfN7jd3Qir5kIua60sRDpzRh23vGOsvDcJIcJP9mrpQ5R7EcGiGsl025JXL9jhrBEiot-gRcxlpQqZpd5gay4l1FO1TKOUDs25HvW-PBFtwL4gGIebo-AAc0kr6oFMvYaL1jWC-bJu1dVTSdp79AnpamVo_rIe93sz7Bw624JPAR1rMpSkAMu8DN5L_lPPxpKArnFJCJT7a_BLt-3A6ad5oxAb1xXQs3skko8JT92rXOmQWuxUWApMO2YcbJ8atDisA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایشون رو آورده بودن موقع زایمان پیش زنش باشه و بهش روحیه بده، آخرش دکترا مجبور شدن خودشو درمان کنن
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71239" target="_blank">📅 15:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71238">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f53489458.mp4?token=YcR59o3VglStFFiqrHa2-5JbHYzZ6MN12posWMOpD-2SB6NdDhUa1gPj5tWSxM-46g11AfkrFHol50l_iLW3_tPVOmSqI9uFHdOq9fXRQYHegeXP7R3qu9Vdzr3sFQbXqzTLTlRRqgXk0MMDFM4lRD8uWckwis6kU8Y9i5NWA-h1x_EyI0gD602WnMlwy0B2o4-v9oEYGO6WfdazolwI6ImWjphH7RCy0CYpwqverCibdUNpwXPG5QfLPCJ0cbjKEV1Y74VNjld6nNWfTHcMqYJ-_Qc5sFQqBZCCtuQ_1CugH_-Rzm8eXmKI6K_O9dmpyPx6jOMTZybD1ElLFYAOJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f53489458.mp4?token=YcR59o3VglStFFiqrHa2-5JbHYzZ6MN12posWMOpD-2SB6NdDhUa1gPj5tWSxM-46g11AfkrFHol50l_iLW3_tPVOmSqI9uFHdOq9fXRQYHegeXP7R3qu9Vdzr3sFQbXqzTLTlRRqgXk0MMDFM4lRD8uWckwis6kU8Y9i5NWA-h1x_EyI0gD602WnMlwy0B2o4-v9oEYGO6WfdazolwI6ImWjphH7RCy0CYpwqverCibdUNpwXPG5QfLPCJ0cbjKEV1Y74VNjld6nNWfTHcMqYJ-_Qc5sFQqBZCCtuQ_1CugH_-Rzm8eXmKI6K_O9dmpyPx6jOMTZybD1ElLFYAOJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ویدیو وایرال شده از یکی از معلم‌های مملکت :
اگه مدارس امسال مجازی بشه، از گوشیِ شخصی‌ام نمی‌تونم استفاده کنم.
چون پارسال 4 تومن گذاشتم رو حقوقِ 14 تومنیم و این گوشیِ 18 میلیونی رو خریدم.
امسال همین گوشی 70 میلیون تومن شده!
حقوق من چقدر شده بعد ده سال تدریس؟ 20 میلیون تومن...
اگه این گوشی من خراب بشه، دیگه نمی‌تونم گوشی بخرم.
آموزش و پرورش باید به فکر تهیه وسایل آموزشی (گوشی و لپ‌تاب) واسه معلم‌ها باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71238" target="_blank">📅 15:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71237">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
این خانم ادعا می‌کنه که در جزیره اپستین بوده؛
صداوسیما هم صحبتاش رو پخش کرده.
ادعا کرده که به کل جزیره تجاوز کردن و شرایط بدی بوده.
بعد میگه خداروشکر فقط خودم مصون موندم و بهم تجاوز نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71237" target="_blank">📅 14:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71236">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c603211e44.mp4?token=SJljjCMaYgud_QcoTFwL2rSHRN2v264Yhc5FKpLk2_EPGLdafvrzE9RQdKJjF2lMnN43a_WD8rR1_MMC6QzTWxlQEHGTunN0aqndcF9RNJjcB1osfPliw_4Y6CnG26oO130jtC_FPa0YHZpquYIeMaDTc1g__ecTQGsEQm-qMnhYHjeim6K0Q7dF9nIs28IeQtWPfldEn4X13fN219vaC_f-PvjUHrRz7eWhVXU-qCkHjHV6riSNvL7M_jr9Hz4XBlSeRzVg8ONueh7QLduzDapycESPuHj_1dXDEdOfEgDesv57Wcnqyqd7BOAcBeNtPbETyBBxQ18e-3Nngp77YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c603211e44.mp4?token=SJljjCMaYgud_QcoTFwL2rSHRN2v264Yhc5FKpLk2_EPGLdafvrzE9RQdKJjF2lMnN43a_WD8rR1_MMC6QzTWxlQEHGTunN0aqndcF9RNJjcB1osfPliw_4Y6CnG26oO130jtC_FPa0YHZpquYIeMaDTc1g__ecTQGsEQm-qMnhYHjeim6K0Q7dF9nIs28IeQtWPfldEn4X13fN219vaC_f-PvjUHrRz7eWhVXU-qCkHjHV6riSNvL7M_jr9Hz4XBlSeRzVg8ONueh7QLduzDapycESPuHj_1dXDEdOfEgDesv57Wcnqyqd7BOAcBeNtPbETyBBxQ18e-3Nngp77YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی
:
چهل‌هشت ساعت پیش اولین موشک ناوشکن خودمون رو بالای سر یه ناو آمریکا تست کردیم
واقعاً یک جهنمی به وجود اومد.
🎙
مجری:
موشک بالستیک؟
🇮🇷
محسن رضایی:
موشک خاص حالاااا. موشک خاص
😟
ناوها فرار کردن.
حادثه آنقدر بزرگی هست که سنتکام هم نتونسته نفی بکنه. اعتراف کرده به این
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71236" target="_blank">📅 13:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71235">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2rDZG4kCQ-MknAsXv2RiTfSmuoL79g8yQCIZIMsuFpTXgY53TUJz4abT7EPqlJyP46SoDGVijSnmvGr0zjT4CKf7mwjMYSXLm1YhWChJXleaqkmSIKveboVbspxE9QOXeId97ACMLdOyehTXcVBwPMPgXo3GaACsyIowIF5zcxfUT2scn7dNAL5q_xOp_D4MJNTclnobOpV7BSMnOjDoSEdA_dWA6Z6xEL6nGlyusYyw-SrmbqGnB58xmM29lnV_ktzFYeshuRb9CP-OI-2wTWaoPDDOOukS7pq3Kv6PbtwmpIc3qtnAIzqHYMvyDbXYrKIQbgUamSTcW_lUpIZYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
⭕️
🇺🇸
👀
افزایش شمار هواپیماهای سوخت‌رسان آمریکا در شبکه مرتبط با عملیات ایران
بر اساس نقشه OSINT منتشرشده توسط DefenceGeek در ۷ سپتامبر ۲۰۲۶، مجموعاً ۱۹۵ فروند هواپیمای سوخت‌رسان KC-135 و KC-46 در شبکه مورد بررسی این نقشه ثبت شده‌اند.
⭕️
جزئیات این آمار:
۱۶۶ فروند KC-135
۲۹ فروند KC-46
مجموع: ۱۹۵ فروند
این نقشه پایگاه‌ها و نقاط مورد استفاده برای مأموریت‌های تانکر در مناطق تحت پوشش CENTCOM و EUCOM را نشان می‌دهد و علاوه بر پایگاه‌های فعلی، برخی پایگاه‌های مورد استفاده قبلی و مسیرهای ترانزیتی را نیز دربر می‌گیرد.
در نسخه فعلی، تعداد KC-135 نسبت به آپدیت قبلی(3 اوت۲۰۲۶ منتشر شده) ۷ فروند و تعداد KC-46 ۲ فروند افزایش نشان داده شده است؛ بنابراین مجموع ثبت‌شده ۹ فروند افزایش داشته است.
منابع مستقل نیز در سال ۲۰۲۶ از به‌کارگیری گسترده تانکرهای KC-135 و KC-46 برای عملیات مرتبط با ایران گزارش داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71235" target="_blank">📅 13:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71234">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1tzBHg1GLBk2FN9DAq4qguWsvZUurR3Ja4D7-MBtUA8_XthOXZXWyEFxCorNpg31hxJnpeO26d_DnSQWL-t8o71SZkVNnV-wm2E9EziLZ67DA3SScB1Uh3TqpcwFXovYYbc55oHiQUAdmPykGbo4Mb_Rf8wXyUQ4RR6a1P04zLVHiojz9KK0fZgG6eJdZfTibr8a8nOzZGSPnl9gEh3E2pn5qgkXGFDwI9xe4wmxncxpX9RnxN_UO7dVwHUeX168hACEc5kVTZVVigoDTUnlp-mIUkaf3B9V-6hfBGiPSwkyWif6yBl7z83-G_R2ewTu81OJXbcJdErJ1FPHhYvYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
موضوع ساده است: زنجیره تولید نفت و گاز در اینجا گسترده، در دسترس و آسیب‌پذیر است.
شرکت‌های نفت و گاز آمریکایی که در این آب‌ها و تأسیسات حضور دارند نیز در معرض همین آسیب‌پذیری قرار دارند.
به دارایی‌های ما حمله کنید، ضربه خواهید خورد. ما پیش‌تر این را ثابت کرده‌ایم؛ از پایگاه‌هایی بپرسید که دیگر کارایی ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71234" target="_blank">📅 12:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71233">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9570398f5.mp4?token=W0KYnDTaLpju2gcY96DE-iXEX3Pbsi2lrBworGJav_IlOlqURuAbcSNvbPl6D2aWdDpmB-7MKvscXLv_RMjmogC7S17WO4K48tofGuP3IVqBp4Z8kfmclmrUSIB7uL7J-kTaJ9Bt6AFFUck8JhxvatzJw9Hr6E5ljlPyY7bdL12L3R1-NwBqgLiLmYft54fTyVk5W5ReDwofnUy08Hhy97j9gMfmdHKgjrp47sQzzWVsmfZxyefJe5uo1g3NahgaVJRRPgbR9OGWNoPQozEC0JoMZnWbbRZPvwCoD1u8baJFRTDdkqMY48EIe6ilyOs2_ibBCPmxpPQ0DVtrNhbrpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9570398f5.mp4?token=W0KYnDTaLpju2gcY96DE-iXEX3Pbsi2lrBworGJav_IlOlqURuAbcSNvbPl6D2aWdDpmB-7MKvscXLv_RMjmogC7S17WO4K48tofGuP3IVqBp4Z8kfmclmrUSIB7uL7J-kTaJ9Bt6AFFUck8JhxvatzJw9Hr6E5ljlPyY7bdL12L3R1-NwBqgLiLmYft54fTyVk5W5ReDwofnUy08Hhy97j9gMfmdHKgjrp47sQzzWVsmfZxyefJe5uo1g3NahgaVJRRPgbR9OGWNoPQozEC0JoMZnWbbRZPvwCoD1u8baJFRTDdkqMY48EIe6ilyOs2_ibBCPmxpPQ0DVtrNhbrpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بمباران آخرالزمانی پادگان فتح خوش‌نام کرج توسط جنگنده های اسرائیلی در جنگ ۴۰روزه
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71233" target="_blank">📅 12:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71232">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71232" target="_blank">📅 12:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71231">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mntCqkQaZ1ZijqxT2Mvn3LpLvKZvWi0NXa3x4bgUNOm0hK510W7lehZ7Kql6lFnFb9lWv9hFHDgVRKVpLx4ZBVv0mocFj9-PXTzD8MjO7q9fG0XRdEF81btc7K3BI9q2ermP1x4UR2cJ3xn_AR9mFltzW3jm6b8uKjsW3nX-H-aUnAurMPDd7A8z18RZNmgZ4jSGnWqI-b_z6Yq3kEAxD7Iqk7EIVS1rQCrdYn6KCgfwAgofE76R-x33zNI_Xlu87jnmC6ZKmvClq9339pUUcyKLtUUAdEGipQleaJYlsIR56i4sAoyNlP8_wB2vRoSL1Pr6LDjcRbe35z21xuPiWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
ذوب‌آهن
🆚
پرسپولیس
⚽️
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی
به آمار ۲ تیم در در این فصل
ذوب‌آهن: ۵ بازی ۱ برد, ۳ تساوی، ۱ شکست
پرسپولیس: ۵ بازی ۳ برد، ۱ تساوی، ۱ شکست
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71231" target="_blank">📅 12:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71228">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6953e87af5.mp4?token=BQw6z_Lt1KeVb3w0iJQiYu8Tvq3G3LWJuI19bd9B7FMIaTsYK6EWnzF3n91w0vy5HDf6FYO3_bsGUA2Edeni5acWdFU3ZeRYWLcHJW3Sw9ZO6HaJsbzqELlsdIU82LsYasnHAXSXH3Qjgsqg9gsjMzqvyOMi89yzWvpUCvbYZftioGKOUvpd5e26p_yVI28ERAxEbXbNaJlRZ4eT5aLKoLI6RAeH_x7lgtWLijUJIjbYbTvzF6gGRovMFyusl53HW2BpH0KgSFGQD3PGz3ZaSRyf9iAvk83rREzzGFBLDiX82B6BbOPlxGET7zIydnySOZ7DciGUzbW_LAycfByFCg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6953e87af5.mp4?token=BQw6z_Lt1KeVb3w0iJQiYu8Tvq3G3LWJuI19bd9B7FMIaTsYK6EWnzF3n91w0vy5HDf6FYO3_bsGUA2Edeni5acWdFU3ZeRYWLcHJW3Sw9ZO6HaJsbzqELlsdIU82LsYasnHAXSXH3Qjgsqg9gsjMzqvyOMi89yzWvpUCvbYZftioGKOUvpd5e26p_yVI28ERAxEbXbNaJlRZ4eT5aLKoLI6RAeH_x7lgtWLijUJIjbYbTvzF6gGRovMFyusl53HW2BpH0KgSFGQD3PGz3ZaSRyf9iAvk83rREzzGFBLDiX82B6BbOPlxGET7zIydnySOZ7DciGUzbW_LAycfByFCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇶
#فوری
؛ بیش از ۱۵۰ ایرانی به دانشجویان عراقی در سمنان حمله کردند.
🎙
به نوشته خبرنگار بغداد الیوم در سمنان:
گروهی که این رسانه تعدادشان را بیش از ۱۵۰ نفر اعلام کرده، به محل اسکان دانشجویان عراقی در دانشگاه سمنان حمله کرده‌اند.
گزارش ادعا می‌کند پلیس پس از اطلاع از حادثه به دانشگاه رسیده، اما هیچ‌یک از مهاجمان را بازداشت نکرده و صرفاً تلاش کرده درگیری را متوقف کند.
طبق این گزارش، مهاجمان وارد محوطه محل اقامت دانشجویان شده و تعدادی از دانشجویان را به‌شدت مورد ضرب‌وشتم قرار داده‌اند و در نتیجه، شماری از آنها زخمی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71228" target="_blank">📅 11:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71227">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6387c174d3.mp4?token=She2u_jBOrU1v2yxcbpEQm3EkRCwbOHOLDgOcyCaEv1biwY2ZKFfCC7Al2cocIvwZw79WZ-fIuIu4ttXg1sNhk_2IUq4ZGVna1bv-ZTYDEiE0Y5BtjW45dGd_xZtZjhSPPq7nl7LcmGpw7Hje849Ht00jh_SqgSNO_UZ4_cQXwqxjZ1cU7E4-i8z_CJ0oZJbxS3-91V5J3lnPZt9Ze3sfZ9a9Fj63heM9kYGJCzRHRbzRQpN9-vfpLQvD9KKuKYiBSnPug6AX9ghxOtgm-x5tIKqtHbboM48Eniqc3WijOrDgooyvGqeOUvKQPxwmfFwyYZDFlSjN38OKUgyTY5ylQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6387c174d3.mp4?token=She2u_jBOrU1v2yxcbpEQm3EkRCwbOHOLDgOcyCaEv1biwY2ZKFfCC7Al2cocIvwZw79WZ-fIuIu4ttXg1sNhk_2IUq4ZGVna1bv-ZTYDEiE0Y5BtjW45dGd_xZtZjhSPPq7nl7LcmGpw7Hje849Ht00jh_SqgSNO_UZ4_cQXwqxjZ1cU7E4-i8z_CJ0oZJbxS3-91V5J3lnPZt9Ze3sfZ9a9Fj63heM9kYGJCzRHRbzRQpN9-vfpLQvD9KKuKYiBSnPug6AX9ghxOtgm-x5tIKqtHbboM48Eniqc3WijOrDgooyvGqeOUvKQPxwmfFwyYZDFlSjN38OKUgyTY5ylQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از روز انتخابات دانش‌آموزان پایه هفتم آمریکا که این پسره ادای ترامپ درمیاره و مثل ترامپ وعده میده
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71227" target="_blank">📅 11:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71226">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb757b4cf.mp4?token=RWmiCUuhcwuuttPcwrtygoGKeNt2LADXxuMKakSU-_CrHQoBU8YEAnSK6Htcg3XVeWbgZOCQdvdVkOtj_jRP6nTgiYZj1Qvb3OnnV5hvBGud_PAISP6Y1ASpH_NQTJK71xyf1FkDXqO8Kp4gfhJtQo5DUI_jfy-8phB41y6ALZMN7LPuKkStVJxjkW1iU4wRXNj7CwtIK5Mx7GZkJlfkPujpD7-Q8yk0HV_KSM6CNxHiOD_35FUbL52X9nBGkjX83Fl1nyMSq17wu1JPCT2VbEpzYVPejgx7VQrjeiPLM7YY_K6j09sltXOJhaZmOldHo-XuGrhXzMGjS59RUKxc74mCnqzdFwsyGxzwbohcryx3vbtsPLVM8UG5ZtpNdIPL3b7Acdn530RqBKwyibUw7q_ag-A5r4u-mbhuV83ZipdklVBhqmPwI7a53Tmr-1IF09ejcJfaycNRS9pAws1R0VEQco6KTod_s-wm7PFUmMnf6OR1IuMP6Kb0VSGw8mvz4W_IqDtbYJ8-klK3BB45Hgh-LnOATCA-QHjkt6Szh8IP5cBohH_ijykfntmOqRUATbwHfeflJiN0l1EpwWF9Jo9M5e9md_VFNh4YEliGsdKk8xyCLG-Ss21rTqrLkRm0LWO9DYHLcBbhNwdwZ00xgumxQ-8zp5dMYDImCxA4n6c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb757b4cf.mp4?token=RWmiCUuhcwuuttPcwrtygoGKeNt2LADXxuMKakSU-_CrHQoBU8YEAnSK6Htcg3XVeWbgZOCQdvdVkOtj_jRP6nTgiYZj1Qvb3OnnV5hvBGud_PAISP6Y1ASpH_NQTJK71xyf1FkDXqO8Kp4gfhJtQo5DUI_jfy-8phB41y6ALZMN7LPuKkStVJxjkW1iU4wRXNj7CwtIK5Mx7GZkJlfkPujpD7-Q8yk0HV_KSM6CNxHiOD_35FUbL52X9nBGkjX83Fl1nyMSq17wu1JPCT2VbEpzYVPejgx7VQrjeiPLM7YY_K6j09sltXOJhaZmOldHo-XuGrhXzMGjS59RUKxc74mCnqzdFwsyGxzwbohcryx3vbtsPLVM8UG5ZtpNdIPL3b7Acdn530RqBKwyibUw7q_ag-A5r4u-mbhuV83ZipdklVBhqmPwI7a53Tmr-1IF09ejcJfaycNRS9pAws1R0VEQco6KTod_s-wm7PFUmMnf6OR1IuMP6Kb0VSGw8mvz4W_IqDtbYJ8-klK3BB45Hgh-LnOATCA-QHjkt6Szh8IP5cBohH_ijykfntmOqRUATbwHfeflJiN0l1EpwWF9Jo9M5e9md_VFNh4YEliGsdKk8xyCLG-Ss21rTqrLkRm0LWO9DYHLcBbhNwdwZ00xgumxQ-8zp5dMYDImCxA4n6c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرفداران حکومت یه بازی ساختن که برگرفته از بازی مافیاست و فقط نام نقش ها فرق میکنه.
در این دور از بازیا ترامپ برنده میشه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71226" target="_blank">📅 11:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71225">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecc54f259a.mp4?token=GA6BEzZ532JRbCOj1_4XoN6fPQN73jL8L9BBwpg-EKYN9yLoNi0ohKomzjWpFHzjx0mVWS6P5fCp4sbGJO26NrGzl_8gi0ps00ZK82mzeGeKxdOBex_LERQHpnYVhzZl6oxlOky6RCxk-H8m0CgCebq0LHY8bB1CCqHKshgHtQvePVPzM07a57NvSIoXHuMwaR50ZzyK9p-oepmRadRPaGYrjEqSOW29PcqAqmGqRv2OBCt8utVHUpIFRCgtHtFtG7FapM1COO5jKJKzl-T9UDuKeI4LOl459A8UHp6ZpK5QKRf-1-ht_-1SBIDb1_BHoPRSbqJi_efImCnaa4IHAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecc54f259a.mp4?token=GA6BEzZ532JRbCOj1_4XoN6fPQN73jL8L9BBwpg-EKYN9yLoNi0ohKomzjWpFHzjx0mVWS6P5fCp4sbGJO26NrGzl_8gi0ps00ZK82mzeGeKxdOBex_LERQHpnYVhzZl6oxlOky6RCxk-H8m0CgCebq0LHY8bB1CCqHKshgHtQvePVPzM07a57NvSIoXHuMwaR50ZzyK9p-oepmRadRPaGYrjEqSOW29PcqAqmGqRv2OBCt8utVHUpIFRCgtHtFtG7FapM1COO5jKJKzl-T9UDuKeI4LOl459A8UHp6ZpK5QKRf-1-ht_-1SBIDb1_BHoPRSbqJi_efImCnaa4IHAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ادعای عجیب یه آفریقاییِ سیاه‌پوستِ ساکن ایران:
خیلی از کاکولدها به پیجم دایرکت میدن و اصرار میکنن که بیا وارد رابطه‌مون بشو و با زنم بخواب!
حتی یکی‌شون می‌گفت هرچقدر پول بخوای بهت میدیم تو فقط بیا..
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71225" target="_blank">📅 10:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71224">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_cgDPZLPEg_4umLHRqkK8zEbfsXgc8mA9AjOup0KrwcpiEolJy-oxziN0fcXjMVyZDe7q_gFwjvy9ADoVsbGoYgR5TMh_aYMFUPo1bOAqX2QybfQt4xlRdqXbR7yFaa0xVgYjc66ewVqBrVNL8lJDVCNGPjatOvUqk4NdoaOPDWk--lXQRMAPOALtP7mJx6hacHYauLP2Vv-9jW27PYj3HZiYJnDw8IgGc6EsP85CMZL1R4U6SEuem0cGZecBPtEHQEMpTaU5o4VtzuMZBKDZHWbqhiPHMDcbySKTCMeKq6XSFA0D8aZ-qTaxY55MyHk1hKbmBDdZ4ckan6ckT61Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
شاهزاده رضا پهلوی:
هم‌میهنان،
جمهوری اسلامی بار دیگر با افزایش قیمت بنزین، هزینه بی‌کفایتی، فساد و جنگ‌افروزی خود را بر دوش مردم ایران گذاشت.
همان‌گونه که در پیام ۳۱ مرداد گفتم، گران کردن سوخت در شرایطی که مردم زیر فشار سنگین اقتصادی قرار دارند، اقدامی ظالمانه و خیانت به ملت ایران است.
به رژیم ضحاکی و رهبر مفقودش می‌گویم: فقر و فشار اقتصادی که بر مردم ایران تحمیل کرده‌اید، نتیجه مستقیم سیاست‌های ویرانگر شماست. منابع کشور متعلق به مردم ایران است؛ نه برای پر کردن جیب مافیاها و نه برای تأمین مالی تروریسم و جنگ‌افروزی. اموال غارت‌شده ملت را بازگردانید و حمایت از تروریست‌ها را قطع کنید.
گمان نکنید با کشتار ده‌ها هزار میهن‌پرست توانسته‌اید اراده ملت را درهم بشکنید. آتش خشم و اعتراض مردم خاموش نشده است. ملتی که برای آزادی، رفاه و آینده‌ای بهتر ایستاده است، در برابر سرکوب، فساد، بی‌کفایتی و تحمیل فقر سکوت نخواهد کرد.
پاینده ایران،
رضا پهلوی
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71224" target="_blank">📅 09:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71223">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sycNJ2hUuvUCbAdXqWjQP1svF4f8n2eNqNEkpJFmeVMs7-uPMjbyaVj56ddBg1weD4-zzQhCqHRI9HVKh9ufRJV3Te7cy6JHkc6NCx6D5aSUqMvTKwnNwjHfQoBnCkt3xHFR5GLFBRZRE0cqdH6-3RwEEQ2z72GyWuEIdFhrQVsasySxEV_xjVf_P_1jBKT4Ftab586gbBiWByF02ap7UlviSs2ThQ6Z4LUB5Gk3tyuyijoHddc1M-zNxJezGkRy_juYASrK8lkGOZp4YqOUpUnWoUykpv_ASCbEnLqNsKGmm9cVwWkMT9puFTCLOSKKTawEvDb3bBAYL_QLD7gs5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71223" target="_blank">📅 09:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71222">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/924d85f6dc.mp4?token=JBeZyRmQWCk0cFa_pMRfFoIYwIa-5B9GWvWVlvFoNjKyzN1_HAo3Kk66o0iQ4slgOw2cXYfsgQ4nwP1umcguGXpeYytKrqDdG9lXVzEa-Ze3sr2KhlAQ-cZQV-t8zsv6BFz4dEYMYoZqWImy5wl7swmRRt9-sGkN--2rFEer-A66YCBjL4Bl9bHM6DA44byQP4Ofz_ntS8EiMv_tSNQgvHj9N4ytqz2TYKpRkVpQYCJm_biMFU34SLzVDEA2cqJWXO-BB81PDItuz4Cpk8jvW0W-30KHEwjLmPCgvDHWjFCGKnYEk7stGWC2uZQB2_NoR7Kg1GBjGatbu27SmGNsgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/924d85f6dc.mp4?token=JBeZyRmQWCk0cFa_pMRfFoIYwIa-5B9GWvWVlvFoNjKyzN1_HAo3Kk66o0iQ4slgOw2cXYfsgQ4nwP1umcguGXpeYytKrqDdG9lXVzEa-Ze3sr2KhlAQ-cZQV-t8zsv6BFz4dEYMYoZqWImy5wl7swmRRt9-sGkN--2rFEer-A66YCBjL4Bl9bHM6DA44byQP4Ofz_ntS8EiMv_tSNQgvHj9N4ytqz2TYKpRkVpQYCJm_biMFU34SLzVDEA2cqJWXO-BB81PDItuz4Cpk8jvW0W-30KHEwjLmPCgvDHWjFCGKnYEk7stGWC2uZQB2_NoR7Kg1GBjGatbu27SmGNsgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک سرهنگ ارتش :
از فرمانده‌ی کل ارتش ایران تقاضا دارم، یه قایق پر از بمب با جلیقه انتحاری در اختیار من قرار دهد تا خودم را به ناو آمریکایی بزنم و منفجرشان کنم
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71222" target="_blank">📅 09:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71221">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26767c2cac.mp4?token=AauFiaheQtQlDW20z8OChuop8QKEOOMw74oDwzr0QM8mtHXpo9PzP__zQ0kR8W6Ymela6pnWc2ugfvB6Lv02mot1NLzl39kwZDDL8DmvzEEtFIHI1Qhgdbs490nUydPkWWSWVIjDsOQ3C_H-zmjO-rmJICwdgPNQKUz2nfsvy0zGLINncHFzGT5md9mS4vHzsDbQKh67ES1FBv09_qwnM6STLOJuZ77kDZ883PBPElEHs0C7smFsfL7Ic6NgtDceVJtm1PG5uAPnOFqZlg__Gn_t6t5nd9kyzFHZCh0h7YHmNNe0Vbos7qjAqvFq4XQgMWiJp-maESVjyBuUd6NaxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26767c2cac.mp4?token=AauFiaheQtQlDW20z8OChuop8QKEOOMw74oDwzr0QM8mtHXpo9PzP__zQ0kR8W6Ymela6pnWc2ugfvB6Lv02mot1NLzl39kwZDDL8DmvzEEtFIHI1Qhgdbs490nUydPkWWSWVIjDsOQ3C_H-zmjO-rmJICwdgPNQKUz2nfsvy0zGLINncHFzGT5md9mS4vHzsDbQKh67ES1FBv09_qwnM6STLOJuZ77kDZ883PBPElEHs0C7smFsfL7Ic6NgtDceVJtm1PG5uAPnOFqZlg__Gn_t6t5nd9kyzFHZCh0h7YHmNNe0Vbos7qjAqvFq4XQgMWiJp-maESVjyBuUd6NaxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان زمان انتخابات:
خیلی‌ها میگن من اگه رئیس‌جمهور بشم میخوام بنزین رو گرون کنم، ولی من بارها گفتم بنزین رو گرون نخواهم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71221" target="_blank">📅 09:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71220">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71220" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71220" target="_blank">📅 00:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71219">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDPs5p3WlIK3XDH5GwTCtbeIKDMs0X2_rNwKdMyyOVwgJbzli7I9IoxEOB26Y_McHsdcTjc3aEw-Mh879zd8XF7_Tl1OiRi-8pcfW7037VnNjZE-nPqG_0zqFTs_qRX0cWtMjyzJlcjQOIR9jls9fdw41bC6wEG8uKWFPYqMHVgawMjkzEKgjGIRdcBNsVJXxw9wPOxvs8HB6n090ijuDrxbJLAToh2utElxUlnD8rh0BtjZVugnlhcCkUUc-iN9TKSMZQ6fHne6nxnj4SS2LfOCc5R56PKqojRhL1FbAs1bXzl1Qqe7awd9anekjCSW4swUkpqt0P_tw2N7yyAccg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71219" target="_blank">📅 00:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71214">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mj5IztUT8NZTTv7XlrHv4QsInEFw_nCyZ4Y786MOmqoOlY3hyOX9lm7WcnNnPFfpg_agMhXq-SYOJXcqEq4oYeG_unHHX3Ukq7iqVFYwgoMjJrSemzhz5vAxT097uL8CZ5RvLuvA5ep24byoWQF3BNPmoaOW4bN5u27HtGFCk-UHfNdcZ_vUGax13IiTekP15unXA7sOfg0vRjY9eYaWvbTF7DaSRV1YHYKshxfrRqRISPqOxfuHGr9E3mtu5Uy3wDBSDxHgofvrNumzMJYYpG8eau2NJf_vnnWFfPdFU2KMknL5Cwqy0qMdAQCFsNOOd2IAEAMPSpO52ozo7kH98A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TWfGPeanL4O1RywmLM3kqRlMD35JlVa1NNhMR2l-8r_3BL53WXRaqUgg53XMPnqxArN7tKdeCiZmAjZIZOA6fcWFkMNGHu_aHBhtt93POYbNFH7_C6jzP-S-yTft9r3X82u8WgN9MkMPPiAEGoOAdYxat_IfLvZyTUnPmhiLobrWhK6Lo3EbHH7IztAvndF0pZLqnMslV6d1HtCb7H855lB02-Wp0Kja7XcGRar3-TXmDlkHxdM0GHEJdV2cUKsVCyq7G7ZD97ytMOI0tdnNPJ3EXowITlYAgT9Qw7kqnBY9JMpp11ssE12dIC0_LpynMZbhujGdChb6XLWzZtO0HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/czCLhLe3mZNN7gv6swT8LwO1Hb0ZQWgfjQTrIUu3qV1_OwOlr1BfTkZeZwpM-X9vfBTYX5FTPomFcNtq34z7WNnuI6EZzmow_X9IzWcuRszkRdSThVYyayobZ8pYHXSbPbnrb0M1Ef-3dOKafcmBUy9udkxyhf_Jc7pR6LSWQrSCSi30480Bd2EGFnP6DeDHHrcT6okAcpFwkr5fPxCbGl79BN-lH804zrWNXtsTxteYlVSRLL1yzH2TSpe4jTlPuS24ST8AsLX-v0RRhCB9M8V4KRAqWcKtBLprBtQJzGQ2Iku8k1dKv-_Wv9h2emljOyfWh_nFKuJNOEtEHW5vPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gXcdNDkjy-YB09w9H4A3iD5HT-tYo7FJoxiVQqxxhtZeqsCfCIsCZm98VdiUjoRF9JNJxAseL1HYucLoyaU3MWTY8NM-MeK2Q01OuRLPQchm55yryWKfRhyRvRwkFyW3TMIOYtJhIFNxhhP2wHzN5sb4bPZ-YXNqS3rjlbe9-hpALwQsFlSjiUbk9N6e-RQnIznnjcCA0ehhKDCJ8wTqF2gSq-IOt3y-N_OEWxAgUb5G7za33bKgJSFCq-eaKETl-vS4mu-nHGwlWEq7Y-ZoYyVqbNKR-6c6CZ_gTQ3zaEa0_ln3e9X-ZIZguflZQX098CannFuSjCWXwhg3t397Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HV6B1XlWCxgyZyDMAwomWdPDwC4CGmzqoQKmdztB7ppnJyrjVAzu56j0jxSEGDUcF8iv02YszHXF7BMtMY0cGgUYPIb5XlrmDC5SiQ9HOvPcpwGuE5PdN0bMTXxayX9_q24RY-LgANYeLZ-AeLDRZVrGTaD3UwZ1or4epOnGwvVGDTskU-hNo07M1BWgYiRFjbz1wmUw6bIU7RVlo7VJ7i4hq7VRpnQkZNKwBScKUyEuUaFriA3YEirJz_dzoUOZ9kNi8t--JyAvT9Z_oLKvz9TtJOK9Dqs8J8CM4xl2U4tIUcnFi5Wh7HfZWOTdK9koIE4FFXLIGme8FwQDJ46TjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
ترامپ:
۱_ایران کشوری در حال فروپاشی‌ست.
۲_خداحافظ جزیره خارک.
۳_ارزش پول ایران از بین رفته است.
۴_صادرات نفت ایران به شدت در حال سقوط است.
۵_ حجم‌های نفت هرمز به سطح قبلی بازگشته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71214" target="_blank">📅 00:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71210">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BB1H2fp8dT3qu6DxPzeFnOXh22LWnGERL0KcZFapfQGEExOfQFkjcsLoEiJUEkThCrXr8v3Kegyxw_k6pujLYyjcBUg8ge0OLTEpxRWsbMwf5HK7iSQaWOVrVlcRYTZFCpCdr0MysjGzpWhCN8-_amHDfSWupjwm7hOUPb4Q8ijVU4ihZrmkMvj4JTAOs63OuOz7cjRBe5UC_j1Hb7aJAvnOzLKKIGD_Py5UqZMhECCVuD7pEAYrTVPjhtMt2fMBRJeBFJ0mEVeiT7xQCIt0K78HxSwQiIueZCGnS4Mj2S3HaPQfb1PCXgoh7lSw0NlBbzRbTH5ZOv3taskBDmUqkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C76-3jjjrlIhbHyqeQOgvZts0FYZ1SPpHvdcfQiLYzvQ9FICK132FiZJBanwd4fACVaqfbhx5yr3E0mgCbPGiXdT5LpP-0djcvkY1XlACJzFtYBy1VVCuhFMbbGjzEL8yfBBNXcpNtUPC-MvyFr7Y45nzOkTuh4Ma298hNGZhCR-_M1Q1TjQk1-lw7x62qRG-0_JunORAVCTOQErx1DOHOO2ImGEu37BLRt1sYoIDK9qsY-gQrTVa6RMdAb2DwF1ZJrSOr3NWDj39chk9hICZzbbfTxvYrNuFgaMASXOnIGrxIHceq0ZUY5PtlAUzNa2Mw14Opb0vU3rFirtmjH3Ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری که ترامپ در تروث سوشال منتشر کرده
😟
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71210" target="_blank">📅 00:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71209">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca8942d62.mp4?token=OJCc-fq0clGwdRcZdbr48wlTLT5wkGCyR-zVJVLV4fSr_4Lb-hNkezYodEWgF9io7Vje7_UOalAOTl0OEU76FUCR7ES5VY3u_ZPv1-APeR0A1ls188tXYtgXx74J7ZZ_kSCbeguWue13UlpXmiLQoHu9G38nnfvFI-fZkAjqACLwCRnUPOtaN2P9-DdRFLYpBJ9rlU59aeor4egB-CQRk-422cGFwfH4q5HZxF1HaKoPFQAX21YFmXE8zLbjSgza4kEXWsHmy6o0ujw5uy0HJsQQh2Q1pW_HFHv4NINOE8khSegsc3OuRwqdgjaobJfXD1Jcqu249wRl-SDxQyRPeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca8942d62.mp4?token=OJCc-fq0clGwdRcZdbr48wlTLT5wkGCyR-zVJVLV4fSr_4Lb-hNkezYodEWgF9io7Vje7_UOalAOTl0OEU76FUCR7ES5VY3u_ZPv1-APeR0A1ls188tXYtgXx74J7ZZ_kSCbeguWue13UlpXmiLQoHu9G38nnfvFI-fZkAjqACLwCRnUPOtaN2P9-DdRFLYpBJ9rlU59aeor4egB-CQRk-422cGFwfH4q5HZxF1HaKoPFQAX21YFmXE8zLbjSgza4kEXWsHmy6o0ujw5uy0HJsQQh2Q1pW_HFHv4NINOE8khSegsc3OuRwqdgjaobJfXD1Jcqu249wRl-SDxQyRPeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دو عدد سیب زمینی 100 هزار تومان؛ اینکه قیمت یه دونه سیب زمینی بزرگ‌ به ۵۰ هزار تومن رسیده‌؛ یعنی فاجعه اقتصادی.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71209" target="_blank">📅 23:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71208">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a65cbcd011.mp4?token=aqTxIVd4Co03M6vCpizviYRYoDV_KYwYVsZDyi6RPE9NKESTap4cXHkTB_LQ8kjwPoMkVUrhNSt1ZZ9GiZe_zApnJ10q7YRKW2oav8C5hXItp3xk67lCMJ9m3na2zA8X7xw13IDXKPfzNUrMNwjqCpBjHNflq5iRc6CaSxfcwd_5nBhScmwLdhwRQnrJYE9-mu1l2ti22_Yt2mQ79mhaEQyQ9SOccRv_ZAeqOQL0zZ50-iEss3E_55SyM8Vhk-p156xBgOD0I5BeYWGgII1OLTDZaqjPDrGrrN88G6MjnjqfDGgKjhDfvAq1z22UARsXAqSRmtEZAu7VdH8Z8CX9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a65cbcd011.mp4?token=aqTxIVd4Co03M6vCpizviYRYoDV_KYwYVsZDyi6RPE9NKESTap4cXHkTB_LQ8kjwPoMkVUrhNSt1ZZ9GiZe_zApnJ10q7YRKW2oav8C5hXItp3xk67lCMJ9m3na2zA8X7xw13IDXKPfzNUrMNwjqCpBjHNflq5iRc6CaSxfcwd_5nBhScmwLdhwRQnrJYE9-mu1l2ti22_Yt2mQ79mhaEQyQ9SOccRv_ZAeqOQL0zZ50-iEss3E_55SyM8Vhk-p156xBgOD0I5BeYWGgII1OLTDZaqjPDrGrrN88G6MjnjqfDGgKjhDfvAq1z22UARsXAqSRmtEZAu7VdH8Z8CX9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سعید لیلاز، اقتصاددان و کارشناس اقتصادی:
«کشور با تذبذب و دودلی، مس‌مس کردن و فس‌فس کردن  اداره نمی‌شود و حکومت باید تصمیم‌های قاطع بگیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71208" target="_blank">📅 22:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71207">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnTXi25td1cw0p9WM4fPbdIE3SGYdxw94lUfgshJNYBy5CLV8c6yZEenRCD_UcpgccSz97VsNw4aWINmS9OvlWeDI7oLkG_ofm30OPlBIQOIAiAnclGhqg5E6bFHXYkDsheUhMM-TRHu8fH2-jseH4AXmZkLvfED3NG7O6UweU0mjoW-SO4xE3p88ae7bYgblrWL2s2nOPnMZh-shi4yeubT30anYhPZqWEJ3MXIml7Zoft9EiJrBUf6qKCF_bPjfHphCPZm0Vs4hIwCPvyohlhDb9gfr_kyd_9ESuIHFy_q4ZoPuQo2SnIZ5gkYV_bFlFkVuYWUXUwj1b8u5WqZJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث که اومده کلشو جای نقشه ایران گذاشته
😟
😟
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71207" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71206">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6400639d7.mp4?token=pFoWYhIas1z7nCIFC-scq9DhOwHCJURYdTBZIX0apyHlPRNxF1rlRoCHnPEcVr2kV_c6BPx60Z60v-M3BXJSFD1-brAQY8wQcIGPUDdwUY43_kDZPz0nKITobJ5DMJCjP7BYMhad7MQXMDATyosEcgnkWU0zimouf3RZP9Dt-nUTsLbkQ8818Q6zx7yhtyW_bahaSGYAjygCNh6-pFZJvu_imKX26iT3zyOrpQp-G_KbmjzQUFkDudLencSV2poNVXBp1_fJznSMOnznU7kcH7OuLo3m_7ZbzugiOHoQ_JXxzvbJOakzaDEET8yQvOd7fsi22GHGEwutK4X2uDX2EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6400639d7.mp4?token=pFoWYhIas1z7nCIFC-scq9DhOwHCJURYdTBZIX0apyHlPRNxF1rlRoCHnPEcVr2kV_c6BPx60Z60v-M3BXJSFD1-brAQY8wQcIGPUDdwUY43_kDZPz0nKITobJ5DMJCjP7BYMhad7MQXMDATyosEcgnkWU0zimouf3RZP9Dt-nUTsLbkQ8818Q6zx7yhtyW_bahaSGYAjygCNh6-pFZJvu_imKX26iT3zyOrpQp-G_KbmjzQUFkDudLencSV2poNVXBp1_fJznSMOnznU7kcH7OuLo3m_7ZbzugiOHoQ_JXxzvbJOakzaDEET8yQvOd7fsi22GHGEwutK4X2uDX2EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
مجری لبنانی:
مجتبی خامنه‌ای، رهبر عالی و ولی‌فقیه، اگر به بیروت بیاید باید بداند که هویت ما عربی است، نه فارسی.
بگذارید این را به روشنی دریابد: اینجا بیروت است، نه تهران؛
اینجا پایتختی عربی و آزاد است و هرگز به پایتختی فارسی بدل نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/71206" target="_blank">📅 21:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71205">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
⭕️
#فوری
؛ نرخ سوم بنزین تغییر کرد
سخنگوی دولت: نرخ کارت جایگاه سوخت از بامداد سه‌شنبه به ۱۰ هزار تومان افزایش خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/71205" target="_blank">📅 21:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71201">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L7vNZ7k_C8zYPxTINCpKklHuv5sPfeu0mjfsCHV1nIO1PhSazqGr8eH9kv1TnyWP4nlqqFbM55Gwx80pqFF5-YEs8UzS5y-rzbg-AkI8bhAEbHXBLges8nC2W7z3AKG7KM0rnN8c4mFM3nRQ0GSq9ZU7YERJkImQiFhgZZfb55SqjTDBAWKVxC1cAzGK9gq60xRmijqvl8HipPjK8w5hapWPlJAui16lqrResDnnmoZUfHC5OGBUFZzP-ijNEXWRR7YAd8da7MfO0mHSH6xs6wS054y90LDJMbp1wQDPgHVD_XjLIVockhOU8-8s5ArYzOidsRxTKO5n1ycgfV10AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q8hHZr1C8P0Pnr0lWhlRzxhmWdogdenth9SRIGkJsSqGyfHW406orHHbya2upAUg-fFLw_uQ_v7A7errA00wQW500503KtM9R7g-EFRtbwaFxlZQCtqusQjnrFVJcBFwTAx_JOEJm2fy367NGyjlmFk4ZJUkW-ENeU4kD-feRshGLxSHqb4fZye56ulxwXefAaeHcDpOhoml1pGmL0Ce4o1Y9A_hNmjZx9BG9aDU_5JCprIuSXKE20sZe4LNPVIv7Kqe7PustiipqqgcbIChdSq9lCfc_NqyWOeaVBX1AaraCFl2UrTbPG_yvPj4xDi3E1e_GfYiESsQ__GeUKWHpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98460c35d8.mp4?token=GEh-BwiUvyGwkAsUAwgk4DuQXhml9EFbJTorElOFKhK5ykhLjyuWpqo3XU40qUG_NpZP99EcrdNox-pyw1DXxQUoFx1uFxhGL-gFft9Pfg2NEmUQqq81T0y-DAYwi9VFSYH92OHOozjsG5Lb7kpQWrMzQpBPXU-Ouatb25MwFp36NT-EElOi2MZJUnAyUg4OeuO7-j0NTDJZ5gEZrKNkwLfuA41LqmPMUIx5OFIM0ZleDCQzf3AVuobfyKTx1ll7Z5hlgie2MyUS0-j-5OxyK15bNAcPqKNCfJFaiQfeUKegxLxT7h5xYk2a3gMRYk-GcAx9x2lh7nVCpf3cA63s7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98460c35d8.mp4?token=GEh-BwiUvyGwkAsUAwgk4DuQXhml9EFbJTorElOFKhK5ykhLjyuWpqo3XU40qUG_NpZP99EcrdNox-pyw1DXxQUoFx1uFxhGL-gFft9Pfg2NEmUQqq81T0y-DAYwi9VFSYH92OHOozjsG5Lb7kpQWrMzQpBPXU-Ouatb25MwFp36NT-EElOi2MZJUnAyUg4OeuO7-j0NTDJZ5gEZrKNkwLfuA41LqmPMUIx5OFIM0ZleDCQzf3AVuobfyKTx1ll7Z5hlgie2MyUS0-j-5OxyK15bNAcPqKNCfJFaiQfeUKegxLxT7h5xYk2a3gMRYk-GcAx9x2lh7nVCpf3cA63s7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
حملات شبانه جنگنده های اسرائیلی به ارتفاعات علی الطاهر و نبطیه الفوقا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71201" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71200">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a237cee509.mp4?token=dPk3JRy6bWM6vcysfWKcdGG2Bc4zIZwOjuBW7iXAL8-k1_HDpW1LKq69Sz5rS2VDxpXRgoJB7Bx0D4qktYSoVrpXaoTHF_F_w5HPENYAuJq-pU6PmY43kSV53de-XBXjpW-zvNqHMzOT4Gmbc0DJTYeueGDC_BH24NvBv_3Vss2MnKrB1YgWYKwtGWLNV14Yr0PcWBnuAhAg83E9agtXGbUCGdZBWxaabXB3REEHYAE8O7tUrGTUSvEu1Lm1GGnnoIwIerzB92drUl7L8PoDZIbCmiFA0HVGMX5F4K_IhsWjWgU-dorthZVw3AbuvTq4Q5LwY4Q7tFI5rITNYCXm5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a237cee509.mp4?token=dPk3JRy6bWM6vcysfWKcdGG2Bc4zIZwOjuBW7iXAL8-k1_HDpW1LKq69Sz5rS2VDxpXRgoJB7Bx0D4qktYSoVrpXaoTHF_F_w5HPENYAuJq-pU6PmY43kSV53de-XBXjpW-zvNqHMzOT4Gmbc0DJTYeueGDC_BH24NvBv_3Vss2MnKrB1YgWYKwtGWLNV14Yr0PcWBnuAhAg83E9agtXGbUCGdZBWxaabXB3REEHYAE8O7tUrGTUSvEu1Lm1GGnnoIwIerzB92drUl7L8PoDZIbCmiFA0HVGMX5F4K_IhsWjWgU-dorthZVw3AbuvTq4Q5LwY4Q7tFI5rITNYCXm5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
زاکانی:از وصیت‌نامه علی خامنه‌ای خبری نیست، احتمالا در بمباران از بین رفته.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71200" target="_blank">📅 20:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71199">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90305378ee.mp4?token=biMOPO8hNVoQQzAEaeo49kIQ7CFVHtgocnADsN__dZQaxbLo0zBAUjBovOdSkP1SN2v5Xz9KF6vrWF56cwQzpfQQxvDKKFF2axMVY1S-MjRBExJDMZJSRm2z1S4OWC4S1O8x9gOm759_ndXKFrC7uiC-rBkUGxnapxJI-uuYHMI2sPnJNYrbmICFnHBq55_Ul6pxM-bPpeQmoyQIxSVuJBlrydHZ6frxCxELHUK-1ex3qDcD68EyHudoRfaiLQmRa3weeHSCJW8Bk6Y8chRJBTh66sWci1QS50ywVibbDuyKLtZEYEVBbATZaCxFyZ51mLxu-iocDIJfwV-3-L3znQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90305378ee.mp4?token=biMOPO8hNVoQQzAEaeo49kIQ7CFVHtgocnADsN__dZQaxbLo0zBAUjBovOdSkP1SN2v5Xz9KF6vrWF56cwQzpfQQxvDKKFF2axMVY1S-MjRBExJDMZJSRm2z1S4OWC4S1O8x9gOm759_ndXKFrC7uiC-rBkUGxnapxJI-uuYHMI2sPnJNYrbmICFnHBq55_Ul6pxM-bPpeQmoyQIxSVuJBlrydHZ6frxCxELHUK-1ex3qDcD68EyHudoRfaiLQmRa3weeHSCJW8Bk6Y8chRJBTh66sWci1QS50ywVibbDuyKLtZEYEVBbATZaCxFyZ51mLxu-iocDIJfwV-3-L3znQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇵🇰
بلاتکلیفی بیش از یک‌هفته‌ای صدها راننده ترانزیت ایرانی در نقطه صفر مرزی پاکستان
این سنگین‌سواران ١۴ شهریور در ویدیویی گفتند که بی آب، غذا و امکانات بهداشتی به حال خود رها شده‌اند. با اتمام سوخت یخچال‌ها، بارهای فاسدشدنی در آستانه نابودی است و گمرک هیچ‌یک از دو کشور پاسخگو نیست
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71199" target="_blank">📅 19:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71198">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بیناموسا مگه نگفتین از امروز برق نمی‌ره؟ رفت که
#hjAly‌</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71198" target="_blank">📅 19:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71197">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd3aa09393.mp4?token=pDwsjx6wIc3IgHVB9IW4ZQ40bLc3Uh9URnEq4wDlxFGDs6JNrVCPngt3sqP9kln0qHUn9FCVXMdAxfz4toLVjOKcJwcxe1KXcG4GWsGGeFSj9ogguwhYKFeMgYdpK3iFmG85-ONgeQ7QxiVrIcXbiMoQl3oeejdMy587iQJdU60r9mEXMeGQ6MxLInIjxFqztajTNzbMgNxxLy8QG5vFsMr6JbxOxTRSUfDIqJfBQ1Y7s5t5zjJ249z8P0N9uSm2vlPtyj2ImfaqzRLkRFY-de0Bi2nyz5ZX2wEFVA0fJ9YR-bk2GLI-tMNvuAOGrjRetDFwzC2lz3wbFAFpBIxWYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd3aa09393.mp4?token=pDwsjx6wIc3IgHVB9IW4ZQ40bLc3Uh9URnEq4wDlxFGDs6JNrVCPngt3sqP9kln0qHUn9FCVXMdAxfz4toLVjOKcJwcxe1KXcG4GWsGGeFSj9ogguwhYKFeMgYdpK3iFmG85-ONgeQ7QxiVrIcXbiMoQl3oeejdMy587iQJdU60r9mEXMeGQ6MxLInIjxFqztajTNzbMgNxxLy8QG5vFsMr6JbxOxTRSUfDIqJfBQ1Y7s5t5zjJ249z8P0N9uSm2vlPtyj2ImfaqzRLkRFY-de0Bi2nyz5ZX2wEFVA0fJ9YR-bk2GLI-tMNvuAOGrjRetDFwzC2lz3wbFAFpBIxWYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست‌وزیر نتانیاهو درباره ایران:
پایان این رژیم در ایران نزدیک است.
این رژیم ضعیف است، برای بقای خود می‌جنگد، متزلزل شده است و هنوز مأموریتی ناتمام باقی مانده که ما مصمم به انجام آن هستیم.
این امر در نهایت چهره خاورمیانه و مسیر تاریخ را تغییر خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71197" target="_blank">📅 19:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71196">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIIShPkuajGGUxhYSJeakDv_gvORs4rObsjS1QxGVb5SvLD5IXjtn379CPMryH2tUurin03GNwkHjbkaTAW2-ZmChuoIZlVpB5zpqTvy40QXazeDLuiDiLgozwm2VO86YCGs1NWc5lSFPWaSYePZ1u9w8elrK-EIw2ssSHrRZYwgpk6UQqmC-R6NwMQaMDSfAF8LTNeHidVppQV4M_e3mICeYz5x9oW60H21WliF3wEuir8MuvhUmsWPhxsW-coDMSbqrxrEifIUKYGjclz2vljXyEbFHj53YcV9-q80WTFu9QksZEVZ4Ea7nOfQpeAioZPkH8oDoqCsi41bskSxmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیس قالیباف به بسنت:
چرخ‌ها آماده. گرم کردن قبل از پرتاب:
دیزل ATH: فروش فوری
بزرگترین طلبکار شما: موفق باشید با Yentervention++
80میلیارد دلار کاهش می‌دهد: نام نروژ را به Americaway تغییر دهید
استخدام کم: بدهی به خدمات با DO[Israel's]W، طبق گفته عروسک‌گردان‌های شما
اوه. طرح نقطه‌ای فدرال رزرو قرمز چشمک می‌زند
😁
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71196" target="_blank">📅 18:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71195">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jasK2mBYtMuTDlwPay7rvkZmXbi4oGIadLFqhiGum-jMAtvgl4SKefJh2ortqrnhZrgacRTKkb9xs9k44-SBvjZtW5OHb7dZBx5D0_EcElAgbyY7bm5AfyVXAEAej0k0rnnyarfWxWv61hzUD5z0_9uDkhXR6G7CJhbx3bqwtLynuR_ixDXaKmzqNRqLLsuMsy0G_eCzocrvi3TO-eyMe4gdJm9dL90qe5wpm1FwprlsVol745GJxC0d1YCy7Eyyxf-QqF4GHU5kr01RkS-e10GeLv9npQCqNooiQJnYLWH0josaJvhvRnc-esrV8ulOMIR2hOwtjPZuRdJpWIqvsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
گویا املاکی موهاشو رنگ کرده
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71195" target="_blank">📅 18:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71193">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3zxWPPEAP6YTqQa5mEMZQZ_OXb9JaEbxxWfhveZ00k8NY300kS7NYNYt-LxLHddAAb6mOMLS6hsqRIbDrxe1hVAhaDX3aE99er37XI_76XrX64aLDipGSvnmh7D1nD-WVKoET4AgpjQb3TBUfc-9dR-CRk0SYOaQgwO3o5ODITi_MekwbMNo58Ooth4JVewtV2i3553WXL65CIMj-bt53tEojXVzO5ypGhzgStwbX1F5ZDSC9Xh4un3zKTEkiyzOeK6RrkT1orWPLXg5DuqeNT-GRbaPRE28g6xbE0K6t0AE_4LT7tLt5WBBN7NNy11ehLzFrXDv5TkekgVQSiNnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/385d0bbd1a.mp4?token=EXsbJz3ovO8mP_3MXmdH8dP-mdbjHQ0wSms_bpr16nn0CZY5uEmAKOkO4G9_l-awuMj4lzcldnc0BParrnIGJKr2ig3ne-2L1Id69t-cPmtzuYyA_KSQ3DWxk3oRz9nt_idNwgwzKGsiuHWamYZdSRuD3UAy5bnepkH9_Cye9l6Ygme5hKiOjbJdgermTgxdNZ4ew2__BCyL0GwGpOoEdVh7UOXNoJGoL863LahxuOz1l4tw-kqIM5_wKK_2M4bxsk_d0lKxK5tI0vQlP3k7L-0Uj0qZBBjMuXnZbMj-vfVFyModaBziZFwYS4ukQXo8w33y68lMlwrrkmmsX_LEVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/385d0bbd1a.mp4?token=EXsbJz3ovO8mP_3MXmdH8dP-mdbjHQ0wSms_bpr16nn0CZY5uEmAKOkO4G9_l-awuMj4lzcldnc0BParrnIGJKr2ig3ne-2L1Id69t-cPmtzuYyA_KSQ3DWxk3oRz9nt_idNwgwzKGsiuHWamYZdSRuD3UAy5bnepkH9_Cye9l6Ygme5hKiOjbJdgermTgxdNZ4ew2__BCyL0GwGpOoEdVh7UOXNoJGoL863LahxuOz1l4tw-kqIM5_wKK_2M4bxsk_d0lKxK5tI0vQlP3k7L-0Uj0qZBBjMuXnZbMj-vfVFyModaBziZFwYS4ukQXo8w33y68lMlwrrkmmsX_LEVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
تو همه جای جهان هوش مصنوعی داره جای آدما رو میگیره ولی تو ایران برعکسه
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71193" target="_blank">📅 18:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71192">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa47cd6f21.mp4?token=UBQPYapHLB4eRFcxGC0mmQ3uh2nFAXRMaHn5SpWXb4WUJjcHGhL7C6-7y96N3WdYVMEVQqZ8LPRAWOPNLKku_mkYxk8Z20h7xpOd2x0d91GGOmff0DI-mBEQDdSImC6TtKJnu6Ck8m_KCErPd1sqgTvck5p0rW4xYL3ISNGWKkpQl7puQv0KwhAM3DqxUmEelWx_2XEmlc16xkfFkGZ_sZbJOB-o8IdabrE25C8-rMLJsFFWyk0c2q6dhdgHt8UJvqcXMc3nBpvc95SOyM_qDJy8Qm8GWYh-kjHsx_DqhFM3qO1JpqQ7eHy0MMEJmeOuc0fKFsKwzw2JD8SDI2RLaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa47cd6f21.mp4?token=UBQPYapHLB4eRFcxGC0mmQ3uh2nFAXRMaHn5SpWXb4WUJjcHGhL7C6-7y96N3WdYVMEVQqZ8LPRAWOPNLKku_mkYxk8Z20h7xpOd2x0d91GGOmff0DI-mBEQDdSImC6TtKJnu6Ck8m_KCErPd1sqgTvck5p0rW4xYL3ISNGWKkpQl7puQv0KwhAM3DqxUmEelWx_2XEmlc16xkfFkGZ_sZbJOB-o8IdabrE25C8-rMLJsFFWyk0c2q6dhdgHt8UJvqcXMc3nBpvc95SOyM_qDJy8Qm8GWYh-kjHsx_DqhFM3qO1JpqQ7eHy0MMEJmeOuc0fKFsKwzw2JD8SDI2RLaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوای دو تا ترنس تو پارک لاله تهران!
فقط آخرش
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71192" target="_blank">📅 17:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71191">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=a04OUf8ztmo9sFo2QQvFHLjBy-BLxRTpeG1QAxsan9ZgDCdmBPZEAN_NhQW-41rPSaGNwCvWx3z7h6mZ1vvhqbo_x4-T6h798i3ltXlXt7oH1BBSdNmZxsRzDGGe1xz6R6eZo6aSGiOpiqrIb7va6yVdGR5jggVEgld5VpR4AIFIMNGA3APQgChUDmfZSykRglvVdyhd1b2FyntFuzoSwfl16PVAD6A9-RqvMOx2ysQtlX9aRxTBabBq9zjeMhXSH6zlbGSCqGq2Cn4GW5D6Ex2eHmfUivQDbwC2XJle5p2Rkq_ChjoCfZcaROg_ULxd1proPumHMSPFkNzTdqb7ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=a04OUf8ztmo9sFo2QQvFHLjBy-BLxRTpeG1QAxsan9ZgDCdmBPZEAN_NhQW-41rPSaGNwCvWx3z7h6mZ1vvhqbo_x4-T6h798i3ltXlXt7oH1BBSdNmZxsRzDGGe1xz6R6eZo6aSGiOpiqrIb7va6yVdGR5jggVEgld5VpR4AIFIMNGA3APQgChUDmfZSykRglvVdyhd1b2FyntFuzoSwfl16PVAD6A9-RqvMOx2ysQtlX9aRxTBabBq9zjeMhXSH6zlbGSCqGq2Cn4GW5D6Ex2eHmfUivQDbwC2XJle5p2Rkq_ChjoCfZcaROg_ULxd1proPumHMSPFkNzTdqb7ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
🇺🇸
وضعیت دخترای حشری تایلندی بعد دیدن پرسنل ناو هواپیمابر آبراهام لینکلن در پاتایا برای تعطیلات!
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71191" target="_blank">📅 17:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71190">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/45226525f2.mp4?token=N_dcKhRArVz41iGEwNXvGrIY-tM49Y71WPlgBunMmUwbMFXjBZOKFeIp6d__OJ8VvbOXclkvUInojBuRaRqNqCss0RMGmV0EoTy5LmO7oeyOoGdkJXpWay1gGaakRCHQBHEXjOZ6M8LjNFnh1c8Q-b9GGSHPwlXNGVXcfi0dDqdxaUrI9S7ha8GyXuEFxLdA19CP8OB-qKpPOzdxYzkbHk6p4RH0Mzci99jVWE7g7D5kyY0r-GPSoWgPHB15Pb2Z3rzFXYv6jI460kJ6c0_sTKS2_qEaR1Y202lrGCjfhFCwis0BDv8ulAlQ53jvoGwVWMM-Mou_q5HtK12RAzaeFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/45226525f2.mp4?token=N_dcKhRArVz41iGEwNXvGrIY-tM49Y71WPlgBunMmUwbMFXjBZOKFeIp6d__OJ8VvbOXclkvUInojBuRaRqNqCss0RMGmV0EoTy5LmO7oeyOoGdkJXpWay1gGaakRCHQBHEXjOZ6M8LjNFnh1c8Q-b9GGSHPwlXNGVXcfi0dDqdxaUrI9S7ha8GyXuEFxLdA19CP8OB-qKpPOzdxYzkbHk6p4RH0Mzci99jVWE7g7D5kyY0r-GPSoWgPHB15Pb2Z3rzFXYv6jI460kJ6c0_sTKS2_qEaR1Y202lrGCjfhFCwis0BDv8ulAlQ53jvoGwVWMM-Mou_q5HtK12RAzaeFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
راننده ای که چند شب پیش در مشهد طرفداران حکومت رو زیر گرفت:
عمدی نبود تعادل نداشتم به یکی برخورد کردم تشنج کردم جای ترمز گاز دادم و یهویی زیر گرفتم
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71190" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71189">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71189" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71189" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71188">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArocEFI-SfOcsteS_EgCZ3BZBZU6qn2n44tIfvfj2s_VQhrH_lZruaVqyXxMcODbP93Tn_3tGyImLs2GSYrK5eC7HmxVAQsRFMyyq13g98FqXBIoWt310BEJDHWZvePUOSvrtAJb9-FjfBIgi6KO6mR1RN17xU7wd4ivkAdMnacHhVB_F-l-swnxs5ktr6YuLHSeMHCzm_EPM6yPqp6y74Rqj95udreGqym3NS9AO5Byd67GCpUY-XcslaqhYHQKF-Q_VeuStlP7Gket03QoCYAwmUDmMaHHmxuXCPlH-19SKdkTC_u1tpgmPM1zevEfIZAzOKHtuql65C2wljKgOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
چلسی
🆚
آرسنال
⚽️
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار ۲ تیم:
چلسی: ۲ بازی ۲ برد و ۷ گل زده
آرسنال: ۲ بازی ۲ برد و ۴ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71188" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71187">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJMXEF5N9A0iCYDowkrjVaZdvlIqe7iwXWxcSe1HH4_ARtDtOqG8lTqW23EYLY1xUaLkiR-SnhgyclLhqMKK61NdApNE6sjjcM2VZTvXZru9aUcajpym4JYZi0D0NhRnpvR36MRCKKiO1b50-fp0g3jR7CPRYnoGoKDcU2bx52_KdZbAfTE9tiOIsTHECpqX1K8V73BHrd6DrBnV6m4OTzKqUL4m9dLwvNfqOGcpdGjyvgGndJltcSJqFzKkZ5Wn_iBhq3-ybmtmC84JraZm9txCleR2jX8ZWcaHqaPnSxc6s9iDYGJmOol1Fplv3vDP7VDOkPnzFl6FZTeyhUGO9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇰
🇵🇰
پارلمان پاکستان برای نخستین بار در تاریخ این کشور، فرماندهی قانونی هر سه شاخه نیروهای مسلح — شامل نیروی زمینی، نیروی دریایی و نیروی هوایی — را به «عاصم منیر»، فرمانده ارتش، واگذار کرده است.
او می‌تواند بدون نیاز به تصویب کابینه، کارکنان این نیروها را بازنشسته یا اخراج کند و یا در خدمت نگه دارد.
دوره پنج‌ساله مسئولیت او دست‌کم تا سال ۲۰۳۰ ادامه خواهد داشت.
او با دریافت درجه «فیلد مارشال»، این درجه و مصونیت قانونی را مادام‌العمر حفظ خواهد کرد و برکناری‌اش مستلزم کسب رأی دو‌سوم نمایندگان پارلمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71187" target="_blank">📅 16:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71186">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22246726de.mp4?token=fHFl7PQU5twe-LRqxINAnbpnKGskderLO0R3OU9hz6wae_J_D9a-rSBsdCZdfCpL0LLquJaRI7oFJ2r_m8NokRfrSXYIguKWBybcRydyAb4BhVdzF5tJZZ6gVcAPMgs-KCvWfXTWWZZ4ARWFNDplYkSG7lAlsReiCYCtLlU1ONL_lKpVu6KqpQBA87QB3vAviVyw5AX5ovpEbngbtO_y46FTzUzB43d2cli7ANkOKTgt6y1yqFMzzYnJzDVgQnZvOGngKlNjvuyZC8gb_wMbM6pA4j9p1lMgXw7CFTfOIhLxK8K5RG3B4bdLKF_AKPIeGA91rJy5jYtHsPLeUYB2Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22246726de.mp4?token=fHFl7PQU5twe-LRqxINAnbpnKGskderLO0R3OU9hz6wae_J_D9a-rSBsdCZdfCpL0LLquJaRI7oFJ2r_m8NokRfrSXYIguKWBybcRydyAb4BhVdzF5tJZZ6gVcAPMgs-KCvWfXTWWZZ4ARWFNDplYkSG7lAlsReiCYCtLlU1ONL_lKpVu6KqpQBA87QB3vAviVyw5AX5ovpEbngbtO_y46FTzUzB43d2cli7ANkOKTgt6y1yqFMzzYnJzDVgQnZvOGngKlNjvuyZC8gb_wMbM6pA4j9p1lMgXw7CFTfOIhLxK8K5RG3B4bdLKF_AKPIeGA91rJy5jYtHsPLeUYB2Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم وایرال شده از ی دختر ایرانی که با یه پسر مکزیکی با هم وارد رابطه میشن و بعد از ۴ سال بالاخره به هم میرسن و باهم ازدواج میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71186" target="_blank">📅 16:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71185">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aza_CoA8zUwIrx4IsIfIZGHQdbudV2OiUY-4iRDPjbmg847jYTNcKHMUNjgHW4dBmMVc9p-hcYAJVNts-yD1LfJjiFYA0by8ab6fv6pSl9qqH7hmhZu1tSFosl5RMRGPT8nQm5Lz_SaZhY79qAJ0ERp7yYja1DQ0w8Xxprg3eVw1HCMvW8VLNZNz1hMYTSMhvo0wzkOQrr76RwIXnA0s6jxgV9FcX8e3u9rPt71U-_C_xs2bmxOkDdG278S4oB2pvBuUtNqDzFbEmHfYYwT-IaGRY3v8W_Aes-nLnKYRRykVNKudbxUqKp9nQks9fOWGjbLoClPMckv_aT-FO2Kw0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیده شده در تجمعات شبانه:
قالیباف
:
علی الاصول یادت رفت
علی الطاهر هوا رفت
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71185" target="_blank">📅 15:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71184">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64baa312ad.mp4?token=jrNo300Um2uMvWckpWnjDV8tU-l6IrBQ6pkAPD3sfdU-MiUjZe_iOuDsrgBHWQcCGWGQx5jac2Y5iZt3uR2mgcGthgvk4LnRKE063EDykTfqRyXkcF9cofEKDe5ITumqZslfjRFdzEZna54H6iaBBPYnER5CYxJfWK5YIxlfRnwk7vHqc1qLRc-Hw1epVKPEXvrk5AX_w9CJVdr6sLj0NQsJ1uP5ZQPFSotbT7PDFKaDRJOBwZDJ7Hm-o0-0iFQGIcgl37nXfN2TnozkMoyELRrLTlvRD7ycfnnZdGweGZlYs0Ikenta9zNLrkB1Q9tCFVZGTx5zaM9PGsmUKKebFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64baa312ad.mp4?token=jrNo300Um2uMvWckpWnjDV8tU-l6IrBQ6pkAPD3sfdU-MiUjZe_iOuDsrgBHWQcCGWGQx5jac2Y5iZt3uR2mgcGthgvk4LnRKE063EDykTfqRyXkcF9cofEKDe5ITumqZslfjRFdzEZna54H6iaBBPYnER5CYxJfWK5YIxlfRnwk7vHqc1qLRc-Hw1epVKPEXvrk5AX_w9CJVdr6sLj0NQsJ1uP5ZQPFSotbT7PDFKaDRJOBwZDJ7Hm-o0-0iFQGIcgl37nXfN2TnozkMoyELRrLTlvRD7ycfnnZdGweGZlYs0Ikenta9zNLrkB1Q9tCFVZGTx5zaM9PGsmUKKebFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو درباره یکی از جنبه‌های سختی مرد بودن در حال وایرال شدنه:
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71184" target="_blank">📅 15:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71183">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c325a7591.mp4?token=Hb9CE4ea_NZMal87EchJkunR37WVgH0Zao7zNmYKoCpYaefPBmG2Fe2NcZjpKiNgh0LwLk4YykeuGUDdK5HkKpghro43QsWeMmbTwlKyIrLnHMUPalQI8cWSYQl5fRNSQH7K6w_TDMqVN3BpvqVy-6VDs7Mnl6UHp3ZrAaiqrP3hKbxCy0EYK3oXJPOn96LgBNsOpfq05VQnwuIb3iTkvJA2LnRFTTpfvxMf8kmC1282IDA-e9LbBIxVDtHgOKH78q6wpA7KveY2FRIeq9SP5cFv2taxoCmV8lRYhn2bI5IQwd6AVoZlYo3lCDygn6qJqbwXcoZQMMleex0jatySB4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c325a7591.mp4?token=Hb9CE4ea_NZMal87EchJkunR37WVgH0Zao7zNmYKoCpYaefPBmG2Fe2NcZjpKiNgh0LwLk4YykeuGUDdK5HkKpghro43QsWeMmbTwlKyIrLnHMUPalQI8cWSYQl5fRNSQH7K6w_TDMqVN3BpvqVy-6VDs7Mnl6UHp3ZrAaiqrP3hKbxCy0EYK3oXJPOn96LgBNsOpfq05VQnwuIb3iTkvJA2LnRFTTpfvxMf8kmC1282IDA-e9LbBIxVDtHgOKH78q6wpA7KveY2FRIeq9SP5cFv2taxoCmV8lRYhn2bI5IQwd6AVoZlYo3lCDygn6qJqbwXcoZQMMleex0jatySB4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مراد ویسی درباره مسعود پزشکیان:
حساب اینو نکنید این متخصص قلبه. از نظر سواد اجتماعی یه آدم به شدت پرتیه پزشکیان.
گفته کارمند‌های دولتو داریم صحبت می‌کنیم در سراسر شهرها، نیان تو شهرها. مثلاً اگر کارمند بانک‌اند اولین بانکی که اونجا هستن برن تو بانک بشینن کار کنن. اگر کارمند تامین اجتماعی‌اند اولین شعبه تامین اجتماعی که هست برن اونجا کار کنن
😟
گفته دو میلیون خودرو میاد کارمند ما اگر یه میلیون از این کارمندها رو بگیم روزانه نیان سر کار تعطیل کنیم اداره رو یا بگیم اولین اداره‌ای که می‌بینن برن اونجا بشینن کار کنن.
گفته یه میلیون خودرو هرکدوم روزی بیست لیتر مصرف می‌کنن یه میلیون ضربدر بیست لیتر می‌شه بیست میلیون لیتر مسئله بنزین حل می‌شه
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71183" target="_blank">📅 14:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71181">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c318eb355.mp4?token=sk9x4bGyZ-EpeskglM80bFOcvygaMjZMhP0XpbbFJ0LlLuVnVFXrZBauy8y9eQNjMj_tLNtfujVdfEz3HEgS1RwZGh1BOwtdFUDI2GzA8Wv-DI4QsBC4FGLIzuc_lo6r83slVBtuTaFbz8UEmcm82ttWnuEINYzIL9p1p9RVPhsJpczpYXTuiDsR5Dr8PevjYILEDi2upoWPYLYEx30XnbP63R40iKidCNxFVxkKMAabtBO1Lyi3jVkFRrGWmCKQrmi_FZsWFw1dexNbTKCsyMPQ3II52M57BsfI0o_FRQjq2o8BwZuuFABOuMKIs1Rvik6dttwWvFzfhZcTAd-mBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c318eb355.mp4?token=sk9x4bGyZ-EpeskglM80bFOcvygaMjZMhP0XpbbFJ0LlLuVnVFXrZBauy8y9eQNjMj_tLNtfujVdfEz3HEgS1RwZGh1BOwtdFUDI2GzA8Wv-DI4QsBC4FGLIzuc_lo6r83slVBtuTaFbz8UEmcm82ttWnuEINYzIL9p1p9RVPhsJpczpYXTuiDsR5Dr8PevjYILEDi2upoWPYLYEx30XnbP63R40iKidCNxFVxkKMAabtBO1Lyi3jVkFRrGWmCKQrmi_FZsWFw1dexNbTKCsyMPQ3II52M57BsfI0o_FRQjq2o8BwZuuFABOuMKIs1Rvik6dttwWvFzfhZcTAd-mBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
〰️
ناو هواپیمابر «یو‌اس‌اس آبراهام لینکلن» (CVN-72) اسکله C-0 در بندر «لائم چابانگ» واقع در استان چونبوری تایلند را ترک کرد و مسیر خود را در عرض اقیانوس آرام به سوی پایگاه اصلی‌اش در سن‌دیگو در پیش گرفت.
خروج این ناو در صبح روز ۶ سپتامبر، به توقفِ حدوداً چهارروزه‌ای که از ۲ سپتامبر آغاز شده بود پایان داد و مرحله بعدیِ مسیر بازگشت آن به ایالات متحده را رقم زد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71181" target="_blank">📅 13:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71180">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/003437fd92.mp4?token=Tn61Gxm6VBcndLztLngKknqM5Brf9ZmpNKe0UPFsQtfH-jsWn12Nj9wNAw8wK0JfBnyOBi7NGOgG_hUBiOcAZlmObT45torqmjmXpRpTAeJmK3nX06iIBsU9byAk-oH6XK-vi_02mJ_JHf_ryHGcAxDE9rzQsoH7bihqvVAT9yBMdNb_LdW8YkqPkKnteUr9oW520L1IpLgq67zppytiH2cPbXIxA4ez2Yl_eIJuROtznJymjnAs0lu6PbBaRbWh5N4JhOmr99t0Lmp399YHQ4qAHZBD0jgoyH4PzH1HsAQF95lZ4LinC0bPLsgnQPO9dTFba-urL2vqm09zXQZdCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/003437fd92.mp4?token=Tn61Gxm6VBcndLztLngKknqM5Brf9ZmpNKe0UPFsQtfH-jsWn12Nj9wNAw8wK0JfBnyOBi7NGOgG_hUBiOcAZlmObT45torqmjmXpRpTAeJmK3nX06iIBsU9byAk-oH6XK-vi_02mJ_JHf_ryHGcAxDE9rzQsoH7bihqvVAT9yBMdNb_LdW8YkqPkKnteUr9oW520L1IpLgq67zppytiH2cPbXIxA4ez2Yl_eIJuROtznJymjnAs0lu6PbBaRbWh5N4JhOmr99t0Lmp399YHQ4qAHZBD0jgoyH4PzH1HsAQF95lZ4LinC0bPLsgnQPO9dTFba-urL2vqm09zXQZdCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی ایتا و روبیکا، ناو جرالد فورد رو بمبارون و غرق کردن
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71180" target="_blank">📅 13:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71179">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71179" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71179" target="_blank">📅 13:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71178">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2YYFGi7A10ibevPxy7PFOdTZl69TNh4buUjAYeWrugo8odKPd79i2TjktfiplU9iECu7OaBpUceN0IijjXCi2nnIdpnEm_4sL7oMAS_YRu2FITWlHdh1FZVF-4WjP5f4LTl1fmqhvGaUrzzrKIIHIhLoNvV93JzNzrKBjDePIoBP5aAwmT7ZxIHkFGMDSFNfaiD4DqMDzZXsSb5GXTd6m2qcN2rKD05RGYMlVtMee_t-I05KSndv3y5yPIsMLbR9upBmxSB1x8wA7Yuc1bRnAXpxp_IMtOnchHbQQXXFPhKLlL9Mkbs0bHzQkUGqcwKelNzK91wI8cYpvUnLDRArg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید
.
اورتون
🆚
منچستریونایتد
آرسنال
🆚
چلسی
آلومینیوم
🆚
استقلال
والنسیا
🆚
بارسلونا
یوونتوس
🆚
میلان
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز و برداشت آسان و امن
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71178" target="_blank">📅 13:52 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
