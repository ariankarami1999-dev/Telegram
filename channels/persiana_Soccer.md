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
<img src="https://cdn4.telesco.pe/file/IDlIcgVzMC4pt-LUkL68bFxexMQ55XE5dU7OKE9PK8O5hOlBj3zUxsmfyp7hUjR_IvosrcnS3bgIo0bJgHepZqZON23PGvpHckxqKM2XqndUBST1OZuvrSNplbttYq_A2a9h4wge3yb5GS5YQr9608ZqGT34Petkh2D9MooMv5kvqg52t-wCvP1M7-RKVoFJ_LZ9LGYEQEV6Shse8m1_CeQsVuCyjbbgyHx6Yu-hgTBdXtx0Ah_FSf9cW_7Ca9QwljBjUNJpbZK4t49-PfF_PaVn6jirZs8W5Ik9xQ7oIMp2bhk8NGsaI2CqwjH0O-tHlFszLgocRnZDdpMuR7pIEg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 628K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 15:51:59</div>
<hr>

<div class="tg-post" id="msg-27147">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee60bdfdc.mp4?token=HwUa68fQeTGecnGMhZbgSc00WR3YcPHZ9ujX7AknxT9jhhO5-cy7iHpFdSQaZfYwY02N1Vk7_Vr11CjaV8eNlX35abETAyXjUvs_w85LoVPvSNcLvOGtas75-D9xqLcZ9rbh4mGvmM1uHl1Yxp802jwElJAvJ0kWHWL0ocobyDRpAlFfXbCdrysbSnW-9S4NlMqalzpORkk-F1PHHcZ3gp_0Ei92oVTMhhBicssffFgFH59KnQj2_FSiH-JQl2_q-wv3n5VwNfG6hbn_3nRODhyKiBmuB5MNEnI3u4hOpX3VosiT4EUTxjMCKA2mgnV_ubXD_zS22spPYl9xsQ6qvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee60bdfdc.mp4?token=HwUa68fQeTGecnGMhZbgSc00WR3YcPHZ9ujX7AknxT9jhhO5-cy7iHpFdSQaZfYwY02N1Vk7_Vr11CjaV8eNlX35abETAyXjUvs_w85LoVPvSNcLvOGtas75-D9xqLcZ9rbh4mGvmM1uHl1Yxp802jwElJAvJ0kWHWL0ocobyDRpAlFfXbCdrysbSnW-9S4NlMqalzpORkk-F1PHHcZ3gp_0Ei92oVTMhhBicssffFgFH59KnQj2_FSiH-JQl2_q-wv3n5VwNfG6hbn_3nRODhyKiBmuB5MNEnI3u4hOpX3VosiT4EUTxjMCKA2mgnV_ubXD_zS22spPYl9xsQ6qvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
توضیحاتی‌جالب‌درباره‌پست‌جدید کریستیانو رونالدو در کنار ماشین های لوکس و گرانقیمت خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/persiana_Soccer/27147" target="_blank">📅 15:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27146">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXsEFp6vSrYgwqJEua7GLndI6VnuCYZZx7Pb1Udd5ASz-PZa66nZ7KqUeHKoq0aaRxMhs1K_9yKXARzRdXFdegAlyDciTrpgQPOvvZun7hlMDZswBVC5kgQ3husROCuDlE_h8y6vtmDc1ftLiUsHtCsZVH54ldEZKg6MHpP81Yzkrr25XvYGsM8p0pBDtFvuY9sDqdsd_4BNqGgyasLhvudRAiTkLZNnZUgpxAQU7QqbvcZFGK9VouwwHKtf0pwOKou8OQEh5_QMSoWumUvDEsfPO7V7zzpjY6Ji6cdEeVhkEGOOz-bTke1jrjXSpb0_BOXd04oWR2mZrKTIu_m9CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
فرشیدباقری بادریافت14میلیاردتومان از پیکان قرار دادش رو با خودروسازان یه ساله تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/27146" target="_blank">📅 14:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27145">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jctbalGimfO1RTutSqhWJJAut5JOAAZanFNKARkHisVqYRTct2eC-1uWB1VTFIxy57aRnGxiP1wFktFWN7Lg5s_bBNsowFoMYdQUJ7rMufyzysBWlUcv_OXSpcO9OZNpmQnTUMRUE7I3jQawA3l6JvHhXFJ91iFlbVSQxxwU9OsnBEdVUW9mFQyT2BKEABqyrYd6JkPnGp7bFCf0fibrSxAZP3SHsY2aDa-YkRpI-8ODWBMas4uduX-nTby-tC2a_wm2-BIEPHxAI1BrGoI18SAhmbX7UTz15RyTQBZxTUx9HDbKNBfikmE0Gfzo_DHqWqMxId36Sm_nQCBu0zZsdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های رسانه پرشیانا؛
امیر هوشنگ سعادتی مدیربرنامه‌های رامین‌رضاییان این بازیکن رو به مدیریت باشگاه سپاهان پیشنهاد داده و مدیرعامل طلایی پوشان اعلام کرده در صورت موافقت محرم نوید کیا آماده عقد قرارداد با این بازیکن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/27145" target="_blank">📅 14:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27144">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09ea3c3b07.mp4?token=k4AMYJqc7qjn1jUPJgeWZEqmSEhtWBwySd1s2fV8T9LzKylHFhGgXlypFKTMa1pwqdr7PQnXKYCPrtWf1knF_f4pofp4SY5uRh6s5VAeFmIjFAPA_9moiZcH8vP3pKqdKlD8HcJYGoL034RG2Yjh0OS2n4ibIZSonmKCMQ9lVTBDim9yTh7Mh8pi0E06Xo0VL38fSk7DSP2i198ChJgbo9OggEmzF9TdNZcmFbgh7E_YYttpbEWmyyVS81GTbPWVZo5ioJjvixQjShME8xI90uztymxtw4WqjIbBBxEwiwoshfKV9sCFBLyMstEG_OSPSOrlgSfbDpMpW-Ul43lkp0AiCyx1mSQ4kbX1lAcXGzIqgG9iYkHdAmycZuXv6KWEXI2yYZHm7aRI6iH_32p6tY4WtI9DEsNqKIQVy92LZs0Y3e6MyylayTxoYW49tPwKOmkgXxtyHK-WlmM0fZdwyOQmut7koEJAYP8R2S1qWNIW_QJv65I_qrDPeJj9tlBYEWQlyaCi_ttFUZk392owe74fC3GOODifJvHX840w_3bUyRwqWCYw_7c3A-F9tyjAUpf6Zi8k-ZsR9TtGEKA0r7XFuBzCzMMwgLOjHZvFo5HU_ufMExX9xMbD5Z950yUul3LeOa_9Gj9DNmUsFgwDqjpDFeR2Hnu9cl7jOOc2PR4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09ea3c3b07.mp4?token=k4AMYJqc7qjn1jUPJgeWZEqmSEhtWBwySd1s2fV8T9LzKylHFhGgXlypFKTMa1pwqdr7PQnXKYCPrtWf1knF_f4pofp4SY5uRh6s5VAeFmIjFAPA_9moiZcH8vP3pKqdKlD8HcJYGoL034RG2Yjh0OS2n4ibIZSonmKCMQ9lVTBDim9yTh7Mh8pi0E06Xo0VL38fSk7DSP2i198ChJgbo9OggEmzF9TdNZcmFbgh7E_YYttpbEWmyyVS81GTbPWVZo5ioJjvixQjShME8xI90uztymxtw4WqjIbBBxEwiwoshfKV9sCFBLyMstEG_OSPSOrlgSfbDpMpW-Ul43lkp0AiCyx1mSQ4kbX1lAcXGzIqgG9iYkHdAmycZuXv6KWEXI2yYZHm7aRI6iH_32p6tY4WtI9DEsNqKIQVy92LZs0Y3e6MyylayTxoYW49tPwKOmkgXxtyHK-WlmM0fZdwyOQmut7koEJAYP8R2S1qWNIW_QJv65I_qrDPeJj9tlBYEWQlyaCi_ttFUZk392owe74fC3GOODifJvHX840w_3bUyRwqWCYw_7c3A-F9tyjAUpf6Zi8k-ZsR9TtGEKA0r7XFuBzCzMMwgLOjHZvFo5HU_ufMExX9xMbD5Z950yUul3LeOa_9Gj9DNmUsFgwDqjpDFeR2Hnu9cl7jOOc2PR4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به‌بهانه جدایی رامین رضاییان از استقلال نگاهی بیندازیم به لحظاتی‌که این بازیکن در این تیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/27144" target="_blank">📅 14:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27143">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBtDzqC0-vDepRGFhl9oAVmC1YU9JSoRb6Ec4F7HOkW6NGiBrGcHib4HoR_yO53zyizMz2Fbe0ekZfGeIW6AgYEvBMQSSN1Lxzx851cgB0Wa8bQPfw9vBWm3Gayw-9mK7AAms-VaBZCVjdhNUlmwrTYs4ZcMINDFWwIjXuWi0-vPYlLgzkBVzdY49KD2_Qo8z4dxecz3092EYqvkazuT9kYsCQTizRadv2zQRSRxkA2sde_ULWUuQfGK1dJhtrKYQgehAkarT4ghT4307QkuxmQFhSc6mnJD6CFkqEf3gOMOkYlt4Ta-5_vsC0GxlmW1VHvpjRq98Gl75CBWCeDy5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/27143" target="_blank">📅 14:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27142">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‼️
اولش یه لحظه فکر کردم وحید امیری رو برده اون بالا؛ لامصب ته چهرش کپی وحید امیریه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/27142" target="_blank">📅 13:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27141">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/590b770d9f.mp4?token=TNPDJHA_BKaJskEIkfR5D8ogPfbhek5A0UcIAjleAAiP39hq2ktczKGpqdQy3cPz7IsETE3YklEtKO2dSwOlKA-s7tF1vL3HwSf6aS__ibJlz60aoWiy39ZonG3_qkDbMOxshZQxu8V6MhXdj03q0L6o7GXRS3AeXd5jGbzxczS9F9w4p2zSuxvLglhif4tr4CHDBdVX9pd1eIqldVuisbnJDiK4-bReTqRno1fVuw_jLIw39FmXchBFl0XcLPGkj-qwGonvsgZRnisuQQkPZze4lHSuVxyErJc7z1q8wgAgrppvo6e_8pUepRSQ4qoNeQOvoocgdKEtI4jgdkA9yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/590b770d9f.mp4?token=TNPDJHA_BKaJskEIkfR5D8ogPfbhek5A0UcIAjleAAiP39hq2ktczKGpqdQy3cPz7IsETE3YklEtKO2dSwOlKA-s7tF1vL3HwSf6aS__ibJlz60aoWiy39ZonG3_qkDbMOxshZQxu8V6MhXdj03q0L6o7GXRS3AeXd5jGbzxczS9F9w4p2zSuxvLglhif4tr4CHDBdVX9pd1eIqldVuisbnJDiK4-bReTqRno1fVuw_jLIw39FmXchBFl0XcLPGkj-qwGonvsgZRnisuQQkPZze4lHSuVxyErJc7z1q8wgAgrppvo6e_8pUepRSQ4qoNeQOvoocgdKEtI4jgdkA9yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
ویدیویی‌زیبا بمناسبت درگذشت فرانکو بارسی اسطوره تاریخی باشگاه آث میلان و فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/27141" target="_blank">📅 13:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27140">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇪🇸
🇨🇮
ویدیویی‌جالب‌ازگذشته سخت و درد ناک یان دیومانده ستاره 19 ساله و جدید باشگاه رئال‌مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/27140" target="_blank">📅 12:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27139">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXhh0NsmzPzccmpV-leHQq2qC7Y5WfuCoaSVvLN7Hk_ZuQfN_NjtKyhhTtXNC69svZaV57hx2GcMKvPu0KpRyQj1FT1IiOiMLd5Wy4NNyUpY5ue6HUjtw1NLmLMb7F7mFl37sJ7klX366bXgF5DcUfriaJflTvAgxOqxmVo8Hp6zxHIV5eJmkuTipOqDTL9Y4_n1yX9OKguaQh_mve9v2hSzHlBUmg3kos1kaC33NuvPSFLZOYaNrGqRkaorAKOoRzkR2F4e8ZDaHW-qdGE4u8svdqn18UW0t9oTlVoTqR76zR1TRqCBhFUZKigu1-9gESRuFmY9Kh5Yl72zRgk9rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات|فابریزیو رومانو: با صلاح دید کادرفنی رئال مادرید؛ فرانکو ماسانتوئونو ستاره آرژانتینی رئالی‌ها در ژانویه قرضی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/27139" target="_blank">📅 12:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27138">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdeHYrKnzInEWhihwZverOcS1O5LXPfa9t5nXu6f7Li3mj96mGaGX9gSRCqXgk7qi0i4iWdf0kc7tZlij_5ueWKNEwFLYXe5nQWUHGDvLPPixejI3t_ObjpMSwc4W_2uCt5tDZVaPRzj48culMrbr_UKlOOOop2UDhnamC05-Bvf_yKvIRnheX07y7oQEIpwTxxzL8U8sJrZy8CJfaKDxpBKpxU9BYT_xMQvsHAuW-5rf29SEzF1ZGtshkqUVBOHW1gjcB8lbYhaVSyvKZkO6LIP_ENkerqTgtP0t0zWsD3AetQQnhIJaCNV0m0GP0YTb1pPdUiRhu9eJTqdFCfBAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/27138" target="_blank">📅 12:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27137">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNWWy0SATzYBYexkkdcuLGeC7jtm2eC2Ai8US4pKIJKu_p_JFxgkmWcREXPWSRzS3QOZhnZRdkGBJ73ZqhbazhhK1wCYWVnQGToVVgBsOanBjyb_IXyMble1BF9bSOExSyC1jlLdS-gO7FluwpERiY4kGd3CL6nenKpwXqCgQF2hMBKumq-5BRbKGDPqy8bYQzbKl6Crj1cbqJwMD3KmOLdEV6pNR9hhToxjem-BG1TEb-6B-Yv3CfQKfFRXNjY4M5Yw3JpOLYOkXU3WmAc22pjtABbdHDE8YOTrzF18YPE_eDrfX93GUG4HtfZqaz8MwW2caGA9y_tYcb5NXGJ1CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/27137" target="_blank">📅 11:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27136">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca19ec3ee1.mp4?token=up3sSObqAqszmwwiRxehwC2tXFp6NDPL4sAzhh0C0Ov40wU0guCZNovS8gIko3jMYuM_IhFifFIB66i25eEsQTKmoaaS8cUmVtX5ZUjwaqR2G4Q4BLEkKlYphWcSZGfx3QzIKFLqyYcrXFsONS7aRqR3UmIjYyx8TpCTQAMd7Vm4Epser06pc15E_z4zmAYGPJT-35GWE2_JgmvrSv9qyXYKIhE9U_BOP13C2HfMP-IiSmSXjTWl-FbY1dGsvYKo3_uPAe6K4AbLytK_6blkL0ZhgjhoYonff-FNux20MdP19Rs9sWRfC3wh18Fxrc7KZaAqx_tfECBjG3b7r9eWDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca19ec3ee1.mp4?token=up3sSObqAqszmwwiRxehwC2tXFp6NDPL4sAzhh0C0Ov40wU0guCZNovS8gIko3jMYuM_IhFifFIB66i25eEsQTKmoaaS8cUmVtX5ZUjwaqR2G4Q4BLEkKlYphWcSZGfx3QzIKFLqyYcrXFsONS7aRqR3UmIjYyx8TpCTQAMd7Vm4Epser06pc15E_z4zmAYGPJT-35GWE2_JgmvrSv9qyXYKIhE9U_BOP13C2HfMP-IiSmSXjTWl-FbY1dGsvYKo3_uPAe6K4AbLytK_6blkL0ZhgjhoYonff-FNux20MdP19Rs9sWRfC3wh18Fxrc7KZaAqx_tfECBjG3b7r9eWDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تموم‌ شد؛ صلاح رفت سوپرلیگ ترکیه! با اعلام فابریزیو رومانو؛ محمد صلاح فوق‌ستاره مصری 34 ساله سابق لیورپول به ترابزون اسپور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/27136" target="_blank">📅 11:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27135">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1ef6701e2.mp4?token=rHAL_0kHBW0T16ytWDRchgoSnbL_hmcpONKQ978l4jJYOop5rmfGxvXXqbxmQV_bLJHWLOwhvbOmN4EX5d75Ch0I3D8K2C8IUEePxnkACLGaRyRFHoAWkkH9EZs0WxF3SGD3sFyimLdAq1qE2pSc1uXgcBYh6iTAfL0IJheHsJ51BPdG9oSJI0UPN5ZSsSEcdG0LKQM1FzmtaFCyLwGsy-ZPHf4az32f9MaJa6dCz852nmvQ3piNoD7x0IvFt6EZsjKEUklW5k348yH1TL6kecw0Ex1Jr1S14i1V9wQqwdc57sRp9cLDcQCmDcggs4dA-NcZpGEQl0GokECTrU96UDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1ef6701e2.mp4?token=rHAL_0kHBW0T16ytWDRchgoSnbL_hmcpONKQ978l4jJYOop5rmfGxvXXqbxmQV_bLJHWLOwhvbOmN4EX5d75Ch0I3D8K2C8IUEePxnkACLGaRyRFHoAWkkH9EZs0WxF3SGD3sFyimLdAq1qE2pSc1uXgcBYh6iTAfL0IJheHsJ51BPdG9oSJI0UPN5ZSsSEcdG0LKQM1FzmtaFCyLwGsy-ZPHf4az32f9MaJa6dCz852nmvQ3piNoD7x0IvFt6EZsjKEUklW5k348yH1TL6kecw0Ex1Jr1S14i1V9wQqwdc57sRp9cLDcQCmDcggs4dA-NcZpGEQl0GokECTrU96UDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌تند رئیس باشگاه رمو پس از رفتار نیمار و حذف تیمش توسط سانتوس در جام حذفی برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/27135" target="_blank">📅 11:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27134">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyWNoL-SDPM3IVNXaSstWde_17KRfM3YYNXL4Yzuh9OJtcu6hS2ELmVOhjt2qaInaDJQrlmxdAvJNuOHYKPV_mW1Tu1y9t6rJTK4PMYbmX00GC4QXN1hensvS793_85099gfQ6P0KgsuyxsCaXdS_XIlYOdcyjNfYEMLQt8JwTpsdeNTfVnYMfbQGWLs2k38bv0iAuNBpiUs6zFoPWQFZSPluydpGzirwuHEf8YIYbMEgMJs8VbLxqrML7PwwfsbI1MvIArPoNh716O9h4C39UBK0t3ZLU0AwS_JV-w1fxweYvqt0pGsfaq175Z3nCLomYlYEC3mUxXApEk9q-umkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
🔴
🇧🇷
باشگاه نیوکاسل پیوستن برونو گیمارش ستاره برزیلی خود به آرسنال در ازای دریافت 93 میلیون یورو ناقابل از توپچی ها رو تایید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/27134" target="_blank">📅 10:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27133">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c293e9daff.mp4?token=rHRlrZ3wfA4zSVGRkLhkY0u20Gj-9rgP93_6Cxvyq5fQKHovBqpTp7rmFTOygIFKr7wFZUqC9s8TVuU1LGKOW2V24UA-f2pK0KJhjUtPNMsTEHwY6M11Lw2GdIVrG3FE-xMX0H2zJpsj_c0gu0fW9FV5hBoZ5KS5bq6Maxdo3l75bHPL-GpwKHalrJI9h9VHMLbv3K2vkUtMs9454EPw9BJ1dJZGHibqeM04mIseCCQRvp38ZRmKzI3IEBRxIg5shHuZo70Q5g2hlJB1f4g2y-aLfN0SvN965HMF306pjEXfaFn7mceptbDfHDDxOrymkbfXuGkaphw7G6dYKAE58g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c293e9daff.mp4?token=rHRlrZ3wfA4zSVGRkLhkY0u20Gj-9rgP93_6Cxvyq5fQKHovBqpTp7rmFTOygIFKr7wFZUqC9s8TVuU1LGKOW2V24UA-f2pK0KJhjUtPNMsTEHwY6M11Lw2GdIVrG3FE-xMX0H2zJpsj_c0gu0fW9FV5hBoZ5KS5bq6Maxdo3l75bHPL-GpwKHalrJI9h9VHMLbv3K2vkUtMs9454EPw9BJ1dJZGHibqeM04mIseCCQRvp38ZRmKzI3IEBRxIg5shHuZo70Q5g2hlJB1f4g2y-aLfN0SvN965HMF306pjEXfaFn7mceptbDfHDDxOrymkbfXuGkaphw7G6dYKAE58g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌تند رئیس باشگاه رمو پس از رفتار نیمار و حذف تیمش توسط سانتوس در جام حذفی برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/27133" target="_blank">📅 10:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27132">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pn-IJyYqSHieUiomEMsYNbXYs9H3t2tjrcLZzg3CQ_ewKyDgcHkore_hxLR1HN2z23ikNyxufgeQmtSDij5uUoBRyD9knS49VBnnShQrNDLPDp0pzK-qLObVNkSObEC1-1OAaqpZGRBJKc5f14SB_T12Kz1OS3evwpDVAmhB1zBzcUSi8-bk2b1ahdhCitoKqTRcPhO58-uU2zgSNiEmM2_-DZxm08rzMgwjBI_o6HWmKAp_18OfKbLD9UHtZCVtvQeSQYU2iDYl42THyf2w1iJjE-r2MGDKp4xaRnBaqS8z2PGsZ2ynYjuYR0HIyC5ZLO2mQFjGaH1z_1gB2LkyKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🤩
با اعلام جرارد رومرو؛ دکو مدیرورزشی بارسلونا هم‌اکنون‌درمادرید بسر میبره و قصد داره که فردا بامدیربرنامه‌های‌ خولیان‌آلوارز جلسه مهمی بزاره تاراهی‌برای پیوستن‌این‌بازیکن به بارسا پیدا کنند. چند روز پیش مدیران باشگاه اتلتیکو گفتن آلوارز خودش رو هم بکشه…</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/27132" target="_blank">📅 10:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27131">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmDykLp6j8KiAm8fnV2XoUKxRWi-llUV4_lvPMyFrwjPxYJcIOgYTTDVG_G9bkQ3nAGaZmp7FX2otNbsBujm0MMd8rxZLA3mczACM6kPqUyP3B5dsYHelcGquGZ63deR9afFenMXs2PnFN3IejsePtezuVtdRYDSs-gGo9YaargsfAaX71ZjnmeehcFj8G4hpX2rrZncvv-i7f5h_pihUvZZz0lhypdta67SELA7q3-G8rridwYdEPa_YdilBhTK3ByfnvLLBE5tKr_PGZedou88oeEICkwvJWCIn77A03M8EAb6LfglW4O7vQqtOtEP1dThas77PYBX0EGQkBU8vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/27131" target="_blank">📅 10:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27130">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7ky3MnN16YfvEYwMV67zXITc0tkBtoGTHMDWvMLr5DQ-RbIjbHwo9n1p_UkVmXk6If4ojOA7GeuHMgrsajjtj5r7HszA0stC4lhDA5r1m7_Wlzqv1XeuaX4XLwe0wxyWpbwGH-SatELoo_UQTqZ5lLDusVzvgvQCoGlfOiCExRdtm7kCz6Mtsq2bj8KXfGYY9iVRzt7R93qkp8hX03jTSdGPL8IkQY0lfmOO7TGnznDPPkif7hHu50kIISxU-GxUCO3_YxRZM9sg9EKEN8GRm_0vkIQhQoeS8UIRRtUzO0_VUtVojcng095rJFXjTY9UV4w3jRvr1fcILm94m7g0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
درحالی‌تموم‌اخبار این روزهای نقل و انتقالات شده انتقال وینیسیوس به آرسنال؛ ستاره برزیلی رئال مادرید بی توجه به این اخبار با دوست دخترش در تعطیلات به سر میبرد و در حال عشق و حاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27130" target="_blank">📅 02:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27129">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVrL2ZVHZdjWtce5zjjZEFDHo7RBwsTKHmuSghvyMmXA3-3bQIprdSPMqE49o6pdjBBc3E2o8CgU39zgft9EDxUzYLRjLD5FhQnTfTxd0LheDxTXpoarYSgLfk1Lck9ZVpkZDBOP5tp56pgnMM1yH1l5TWVNxIzJDLRiUuysTzf-HZQYsJmrZT9ilH-f2yVG1BS2QVztH8UxEYSV5g0qw68yVGmT8oyBMZMrARj7BUAne-aLgpvCH6aFb1Hyny8K9N5h9-KpCmhqmjuBioJ4WUGduz7gqncA_hiQgiS7m9PS6CN1rzG_GEevAucyqvzVINv8NrhsbsWJLiEO14gRGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بهترین‌و‌باکیفیت ترین ابزارهای هوش مصنوعی که از همه آن‌ها رایگان میشه استفاده کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27129" target="_blank">📅 01:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27127">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnHb91UhO4uAYUrEC3XHp-156xTpKIPsITwEzJvAFP6VpGDrF8lv6veEASWVchPoYbvKvxpPDZZmhHoLznFlIDwyVBMWYbQl1qEtbvi1Z-NvM0_jFOiqBui9hKA9e5Ba9Ce0u900vA1ArwumthEoWsDwDeQxHzJFpC0vSytJJNtkU-79PtdUIdHJipcjTMGE3E00Vge3xuGqLzr1OCYqDqdLMWwuWqcBdQ4Rz4oDw1I_3Z9DQ9VdjMRDH4ToevUNAxif4uJnlPq3Z6c44ZTlVUF9x1JQGs-FD0rG8v5q0yrO9MI-1Dmpk9ZfqBDElg1cR4eqAvtKUUhUKXLOleOsXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
ازدربی‌دوستانه دلامادونینا تا دوئل شاگردان ژابی و اسپالتی در کشور هنگ کنگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27127" target="_blank">📅 01:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27126">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfiPNVkQ6cn_Nqu90YM9A6cNW_cCqfSipXNFgquHphgb5BfnvKWtU0obNBLIvvG2xc5L4X-5K2fGfg7DdJ29YtNFNbCHX-f1R3kUrbHj3CFPPwMEx0Xc1C7_5aNGLC71kIMzkvAhz01o4ixSvBsMmRywNHFIMnt2yp4dcAiortv-sj9UYZQD0LUfn_o8uIfGsT-p14ajsMXvhdbFR7SIy2vu_26B94eu5Lp7VDgIG7XipGMWtqwf8XNvDLB_WNhei7eyDd47ayPTAgchvjxVaTJtvfF-GcNc606GgLkMr8SmpFIaIWaituRC2irpw9AXHNQ6VkSOxUDGUTxlM584CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
از باخت ماخاچ‌ قلعه با حسین‌ نژاد تا برتری بایرن و رم در بازی‌های دوستانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/27126" target="_blank">📅 01:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27124">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1X_JJEipGV5I_k4zJT99ZBtsMCsDUjgfgvkBC_TVhvekglmbehdrCK2FNbj6mD0tZyr-CyUbH3B9r4ccDIhjTcwyW7deFH6ptsIeEA56SP6rBnQvpEPkslvhBpEvb440yM8DoAxBYymXc07SownFjQrDFtckZFMyJlWXmKWA61vrDkfCYnb0LwFyYhi867Yy4g5fNYoepEjaFGA4U6CcIg_vw22SSJJ53PBJz8XDyV7GduvIlgZ7BAXRDrrPHTgmkJX6xyd7_v3H5i8TZSollYAVwenEty48fFDtXyWVFXLIphTP3eWqzoC9HruV6Pwa4KAYfsn5N0aCAIgXBNOFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تموم‌ شد؛ صلاح رفت سوپرلیگ ترکیه! با اعلام فابریزیو رومانو؛ محمد صلاح فوق‌ستاره مصری 34 ساله سابق لیورپول به ترابزون اسپور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/27124" target="_blank">📅 01:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27123">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjvSYGksE8eLNsCszDCJdUSLXrsw1r8knbFNYHHNRRc9KgRVsDw2aSRjRNQsaEwmWqyt52hl5Jm-VDyZf7mlVEYbJf9g95VpiWx8saIme1T-fq8BKHiXvBkjvSVlDuk38SSyqbuqJWd6SYxwENbEg0ibEqwkEJxfF4Z02JXEgydhDNuyumNT8kolG4Wz6IjnM8OIrxhWDF3Fn_qS9gzuhK_pg10-jMrJ8vw7GBNsoixGZQHttulWn_qHfZSiUB5NgtfoCdE1K1756nKaa8ZQMVJXqVF_nLDlhIzo2lBV48K4RpC15hYe7kAqI9rhntikadauvFPONS6B3wfx_179Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال: مسی؟ فوق‌العاده‌ست. من به نصف دستاورد هایی که او رسیده بتونم برسم بسمه. یامال برای رسیدن به نصف دستاوردهایِ لئو‌ مسی فقط به 455 گل، 205 پاس‌گل،660 تاثیر مستقیم روی گل، 22 جام، 4 توپ طلا، 3 کفش طلا، 4 پیچپیچی، 6 قهرمانی لیگ، 2 لیگ‌قهرمانان،1…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/27123" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27122">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9Px2pTfHuSEjQ3yW49ToX5BpYq1i7SArOJfRSQ7GcLM9IEZy5pO0ckAe3nBcOZjuqSP5uqKSdyi6jCPnQRHohHTsDJso8yvqVBrT8hTq6pHVWfMyBG_vD3Z7UyIcNlCNGbLK4aBbq2URZUTEFmgcrvCCRWJxmsYJ0PXWRw6zlXUJ-1de05axC2sBSaZLkVhXYm7P3UbjUz11AMluokcywrCdErIUhIYO_hwo92G7G6XnduPqBJubYio76jDuQCVGxgGI1m_tScK99oUeF2gBcNpzemRIBzSb5LKma1cx88MBqnSi3BB2AuyxKA-1jTXAfCNBZ5LhfSCYf04CUeEYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سعیدفتاحی معاون‌ورزشی‌باشگاه استقلال: قرار شده بود امروز عصر آقای رامین رضاییان همراه‌ با مدیر برنامه‌هایش به ساختمان باشگاه مراجعه کنند تا ‌اقدامات مربوط به بازگشت او به این تیم رو انجام بدهیم اما برخلاف قولی که داده بودند عمل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27122" target="_blank">📅 00:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27121">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c01adXPElgswivrea1atQ8Jgvpu7GfRC_3GZ8HmdY4N0TnruDSfvQflb3zYhtJFOudhpXqTAENP2iqNq6fUnXDOKGRw9z3T6wmjdslhrj57WTqslVN3tzHTdBoC5Ie27noTSWtT5zys5M1uTQa7XTLEqnEbzoML8TZ6ngUqAq7oL4PhIEOWa5_kl9IdMSyCVdkp5bQTD1E0bRdiEVkP71VlgfrmUPp7uUi9Km7NIZtniZMxjajgtmhkOUEpSQ-qzze23i6iFUkbLuRLOHzyeoJk1lwdDofAVhJJ0w_cR5OqWeOaqGs6IrmbmUAFSsk2Bcko76MJxRhYzMkGbZ0Hv8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
طبق‌اعلام‌رسانه‌های ترکیه‌ای، محمد صلاح فردا ساعت 12 ظهر به‌استانبول خواهد رسید تا کار های نهایی برای عقد قرارداد نهایی با ترابزون‌اسپور انجام شود. ازطرفی‌هم رسانه های عربستانی میگن الاتحاد میخواد بارقم بالاتری هایجک کنه صلاح رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27121" target="_blank">📅 00:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27120">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cu57dAGB7x7AARZXE_ePRBDSbGS_PYFJhs1_P8YrBRhvC-FrZ24cWYLQjGa93MFIrluHHAS32D72Pfc8dLkDEWAgG_Ujk_pSmvBamT4yHo7o_MrYovGFpTyRb1lw6CxtaYklfJkkr9nLNrgwk-Kzlx1erjgT9BPb8w4PWbguQq88SaD_iCaqsHztHSLQRr3-6Ye_ffyv949HHS_0tp1q4iwqwwwzEv9Zmu_9EUv_zLUTkNOLfx_uJRpelwKDnA87rfSNNagFKhGa-ihtqEapI_b8baNSDU2CgRqVE6CPAlnIg4WZOOya6u--Hj54CpEc6-Rkq5vP5lSiUqUwGfNzxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال:
مسی؟ فوق‌العاده‌ست. من به نصف دستاورد هایی که او رسیده بتونم برسم بسمه. یامال برای رسیدن به نصف دستاوردهایِ لئو‌ مسی فقط به 455 گل، 205 پاس‌گل،660 تاثیر مستقیم روی گل، 22 جام، 4 توپ طلا، 3 کفش طلا، 4 پیچپیچی، 6 قهرمانی لیگ، 2 لیگ‌قهرمانان،1 لاریوس نیاز داره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27120" target="_blank">📅 00:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27118">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8a21ccb63.mp4?token=mJvBxqyQ_QAvl-0n3F59ZYCqZAJIfeats5ES13XbvgYMGKYj9fE4zSMvfoFEw3E3WExwvSr2KaEeL76mQNOpQYJsMMM-131SpJnaeJVRvkT4flv4wRb8azxvoTYRzDfRbYow3BjCet-5lsAupaYXw2cngj23FTM019mG2sXxsbdjpeeJkNaP0lOyjBSybhIHBmtLn5RvY3dk413Tf09ataKq0BTOQNHgUvQcnU6Gz8iwXkSFdUC9v_Pyoz-m7fN-Yyjo7LswxdbBxN7_Tep9361Q-yKymIu4BtqB2B2EgRnxjwJPuz4K6Rqmjr-hxOScwgcv0jyA_zU-EF_tShQeEiuSaVd0uWL-_yXg0dx-AobQN9FbTHLX9LK5rhlwbQ0JFep5FE3DN71h9JvCxdJEWPsjtGs_5c6YlTwAdSSEFC9zF1eQKjlxNxN87NCTaqix6AptsAKJX3zLj0_Izu6UCzPW3mvSah5-tQ64VtSO3TjEEglkZ54oP87ncHHubw9x2Jkw69q_aDVuelsAKE-JXMI7BoKo16RgTsXDEB5o82d36Praz72azwIq4nwhd88bTxgjJdv_bt6qaNZrCNd_3xCNiLv_HNc1JS9jWqXteaQRy8nKLiE4HSIJqdKEduLhX3NqRzucLUaG0yC4i_56kjAcZXu-fcQN6t8QJ1flhys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8a21ccb63.mp4?token=mJvBxqyQ_QAvl-0n3F59ZYCqZAJIfeats5ES13XbvgYMGKYj9fE4zSMvfoFEw3E3WExwvSr2KaEeL76mQNOpQYJsMMM-131SpJnaeJVRvkT4flv4wRb8azxvoTYRzDfRbYow3BjCet-5lsAupaYXw2cngj23FTM019mG2sXxsbdjpeeJkNaP0lOyjBSybhIHBmtLn5RvY3dk413Tf09ataKq0BTOQNHgUvQcnU6Gz8iwXkSFdUC9v_Pyoz-m7fN-Yyjo7LswxdbBxN7_Tep9361Q-yKymIu4BtqB2B2EgRnxjwJPuz4K6Rqmjr-hxOScwgcv0jyA_zU-EF_tShQeEiuSaVd0uWL-_yXg0dx-AobQN9FbTHLX9LK5rhlwbQ0JFep5FE3DN71h9JvCxdJEWPsjtGs_5c6YlTwAdSSEFC9zF1eQKjlxNxN87NCTaqix6AptsAKJX3zLj0_Izu6UCzPW3mvSah5-tQ64VtSO3TjEEglkZ54oP87ncHHubw9x2Jkw69q_aDVuelsAKE-JXMI7BoKo16RgTsXDEB5o82d36Praz72azwIq4nwhd88bTxgjJdv_bt6qaNZrCNd_3xCNiLv_HNc1JS9jWqXteaQRy8nKLiE4HSIJqdKEduLhX3NqRzucLUaG0yC4i_56kjAcZXu-fcQN6t8QJ1flhys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
فدراسیون‌ والیبال‌ ترکیه‌ به‌ این‌ شکل از زهرا گونش و خانواده‌اش بعداز قهرمانی در لیگ ملت‌ ها تجلیل کرد. گونش با درخشش در لیگ ملت‌ها یک تنه تیم ملی ترکیه رو قهرمان رقابت‌ها کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27118" target="_blank">📅 23:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27117">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBk-DGzMHI1C3v6qzozIqC6zcMlfw-_VcQ4vfTSr4NR-4h91M8Od_zdBmYQ2jjwZvLm2EVdTDy22siyZAPck2xtNR_ZWAm1VlFizwQBTIiM6P7Wt3C6lafJDxLfvT5hWp77WqoXmFGJKCrSrDbOo19NP3zEJ9PdkFV8EK3pVTtM5aEh3e2LUu61gdkKdM9eP6SpUCIvCdXgi_y2_5IR6Lk4myjE9iVIWoBwaWFs9gYkeWj9RvHyMw1zapOq83nl2Tx25kSoPraaAmCHWAV4uxGJdsduCWh-ZK2zlHV8m0hLexYp4EpKuomGgb2i4lkaxFKcnEPRTuL_vIUTxsE9DGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
رئیس باشگاه اتلتیکو مادرید به زبان عامیانه گفته؛ خولیان آلوارز خودشم‌بکشه نمیزاریم از اتلتیکو جدا بشه. 100 میلیون یورو که هیچی 200 میلیون یورو هم بارسا بهمون بده آلوارز رو بهشون نمیدیم. مصاحبه های آلوارز اهمیت نداره. او موندنیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27117" target="_blank">📅 23:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27116">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAbD3C145jxhbnWFCJmbqcOQ_tdXfrF1UK4aN48q6DCP-Ot1HWpT4glmz000nrVRaNU-q-b4311BCy-NWHNfKAkuzzhE3D_rrjlXzGkRuyPNWOm7uweoYzCHh3pAg9-j3qGhJyNG4P0H0rk0H1boaphGnnVSeiSis2C7egV2ma_pjgGQeOT8b928FyCJ2WvWqcmAudbQZVs1mr4JjlEm8LgjAS9T_NfoRjbX7GJW6HSAMQuFPtowEGeaV-qCu2MtrXz_QrSA2BZ2rDLRZzmfoqDuHZ_UlF6WFWMyS27t3LhAWY2-Aoi7RCyiLazsJQzEQ4WhCfSTn_Yr5x5XgpFC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ مدیربرنامه‌ های رامین رضاییان امروز با مدیریت باشگاه استقلال مذاکرات مثبتی بر سر رقم قرارداد این بازیکن داشته و قرارشده‌ که رامین رضاییان عصر امروز برای انجام مذاکرات نهایی و عقدقراردادجدید با باشگاه استقلال وارد ساختمان این…</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27116" target="_blank">📅 22:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27115">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52510ee628.mp4?token=rr--AiL2JPfaLwGgC_AIS5yjzdB5xXh1foiUN9-RrJs8-4GFiO31YahcD8YtIkV5dKEtN9PtLmrx7Rp9jBeZaEBW8tO2H-3ZUEwnYOE0JTT2nSEGp-9b4q3jj3lop9fToSFUsBkqMyVAhlLgKVwQfUr5p8QVmt9VRvwnQw-6Ok8hmrW6iT_SRRihXfW1cuzkUuoavVxpJ243pOTE98zLtoDqFuIQ9UV2bT8d2s2z_UC3BIciOzGZcl0eYCv2XNNWF8ncgfTsusH9qZZDaZqzOdEYgINRkfQcUbydbO4yhCJBnJGIPGzfnTPUYbH-kxYNTZNSu9RumgE6ohpfMBxHiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52510ee628.mp4?token=rr--AiL2JPfaLwGgC_AIS5yjzdB5xXh1foiUN9-RrJs8-4GFiO31YahcD8YtIkV5dKEtN9PtLmrx7Rp9jBeZaEBW8tO2H-3ZUEwnYOE0JTT2nSEGp-9b4q3jj3lop9fToSFUsBkqMyVAhlLgKVwQfUr5p8QVmt9VRvwnQw-6Ok8hmrW6iT_SRRihXfW1cuzkUuoavVxpJ243pOTE98zLtoDqFuIQ9UV2bT8d2s2z_UC3BIciOzGZcl0eYCv2XNNWF8ncgfTsusH9qZZDaZqzOdEYgINRkfQcUbydbO4yhCJBnJGIPGzfnTPUYbH-kxYNTZNSu9RumgE6ohpfMBxHiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
درمصاحبه‌جدیدخانواده‌نیمار؛همسر نیمار از قلب بزرگ او گفت؛ ازکمک‌هایی‌که حتی دور از چشم همه برای اطرافیان و گاهی حتی غریبه‌ها انجام می‌دهد.
‼️
البته ستاره واقعی این مصاحبه شیرین، شیطنت‌ های بامزه دخترکوچولوی فوق ستاره سابق بارسلونا بود که تمام مدت توجه‌ها را به خودش جلب کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27115" target="_blank">📅 22:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27114">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfkCS9H68mU_PJJtPR1dOj_zvtBqLmWrHEBgmfGKBzOrx8zItRR1UIjCV41Cdo9kd9W5ZpdUS6OFTBHGUEzQCkXovolfusvDX29tFSviGG38CfqP6z-kIABjDh-bT5pHioP94zmJswh9i371SyM_0tyg5EOWiWIyYgB5KVUPCz7onqdJnxgIRvAbkMIUWCl71pxKr_OaOFEIW5ko0J8tcPCCq37A0sWbgYWVfk09JyIOl-HJ0abi40KoA0xaFRNBPkmnc1gFaAOXa0Z7gR1Bda1f1-V1zImoo0gqqs894k3JXsOxrpPsbb_LqBmEZg3CuD5nb7SCtSmYBnzKzQXRoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌انتقالات|نشریه‌ سان: سران آرسنال به درخواست میکل آرتتا به‌دنبال جذب یان کوتو مدافع راست 23 ساله دورتموند در پنجره ژانویه هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27114" target="_blank">📅 21:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27113">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjwCVVvNG8tEyGUKrj3aACf23L5YffwD13rmCtmlEBF7AaAPIGxgtL670jEzlHn2qLF1WkYoB3AA7TeDEwdZ_FIc1TRUrXWCB3imaZMTH-NXd-INKOY2aaWrW6LgDyEvTaA_R79PfdAPwKE2gGs-vW5IM7Ya8CS013PYQDJAYADxzmcejpXNnChnLwoBqjl5X0jVXzEow7ejqtG39x12JpDkP_IwVTN-H4z1WCAA18jKax2wQAAnUh0O8i0JbXkG9dDOjarLerPvDvsrdZrvI_VCtzXhYqNyV64h_jJwyPDtP8WKLggGUD9aAYfCRKh0VonB3bktPhHZ2dlLFEKcZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس اسپی مهاجم رئال مادرید:
الگوی من در رئال‌مادرید کریم بنزماست. میخوام با گل‌هایی که میزنم همچون او در مادرید محبوب بشم. برای دیدار مقابل بارسلونا در الکلاسیکو لحظه شماری میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27113" target="_blank">📅 21:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27112">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bi0Tedx99lP2OIaBurqnyEIOL8jzn7-PhSbJKPdyBax8seNavabghWBOmSBlnA7Pq28gkyOeR6AY4lNGR9ARxK4C2Pvh5OWvVssNfy7d-l7dW21zF72Kp-IOzc8kFy9nNHtfYJkjgEEOc7VmL8CH8UxQzE4czvOe81MafEPWnvDF90kB8yGNYfaOHPENiwg9dtvAjypYy8nxVEV3Cn1twDno3KTfIRn94v4CLMO_Tio2XVWRLm3cirUqzJbi5qt3Ozm7qTUuFNJPObwJki7Gj8EKynjOrbpDcaEGStvEdCSB57OpSkV6FG0Yh_VQbLrnImCd0h-bwvho3bVD09NuhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ مدیربرنامه‌ های رامین رضاییان امروز با مدیریت باشگاه استقلال مذاکرات مثبتی بر سر رقم قرارداد این بازیکن داشته و قرارشده‌ که رامین رضاییان عصر امروز برای انجام مذاکرات نهایی و عقدقراردادجدید با باشگاه استقلال وارد ساختمان این…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27112" target="_blank">📅 20:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27111">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gf3-SWoEXgNAlRGMwDcwc8dQglrodYMTca4nGu9Myd1xzYgpFkbCTQ9O9e7Z5aQvTVGwWR-Pfg3G-IWnGh8nkYE8ETrEOLsPR9sW1O_UiH9sRKBzWR5QidIL_QnRVJkQzc2lpwPIrsU15hK6nlknFUP-8uA6VP5sS2_eZe-ga2o_s78Orxbf8qVx2q3zZZTXdMqZDn-YoQxx_EYTauLmyPqofc-BO-UCUSETJbWPJBhfj4WAQWNYgVT7qI0REGGGFXf0M3Y-GfPRXnSrOpWLVRJ7E1m1g0FmN4URDoBCAwRCwxs4vB_knxWUO1H631M2mTxMpgjwqau4Dgrvr6Njew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: باشگاه ترابزون اسپور ساعاتی قبل‌پیشنهادی دوساله به محمد صلاح ستاره مصری سابق لیورپول داده و منتظر پاسخ این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27111" target="_blank">📅 20:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27110">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBs6t4_N98RBOKJhxNLNu3Yf1OzjP7CyvXEFBL-o96TrK9n2J2UNtGs1tS4coNAcoMIhMAtB_dtmSDEY6ccxLQAZ6ACIgi4CinJmsshcI4qe20X2VQQiKyIJGHL16yF1u0twaJ6NuKD5elkXyyKVn5uIJY34M1Nl5653OcG_NIT0b1Vt4XfuH-n4WXZfTk22ghSzSKQkiQv2UQ7XLHSONfywCk4--HsCEDw4Ar65BKi3UOZvNonKh4up890YbmhVuTolPeukh66EirFTRWwb0-gdjDN4k1z5r6_Aex39EMvne348M-7v2_2EDfKPKrrwx81BwdYbarvxgVSJYfmR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
استوری جدید آلن هلیلوویچ هافبک تهاجمی کروات سابق تیم بارسا و مدنظر باشگاه پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27110" target="_blank">📅 20:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27109">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/St3TS7ZhautjT2ckPJwIiaQU2fsKPAfhod6KrA4CKqgNwVkwuiCi39UBREVRgKMxJ5fHPOsGypjqvtjLOdhYODbppXu2KQUR9T-oNVSl-OlcalTKoh7lMOueDVa0nVV45IPYlTI6hkUNr2Wg4ww7IhLhXyiGR386JDtjG83CbyzTiavImulp4gPno2vn_6YTk7YvyKqa7UkerG4jEsjNinX0r9XiEF0HC5p9Eh1BmXqRLXnoZZ_oVlgY5N8NHuPs_gZasAVY6vwnSRckL_2G8697oIIlrk1Nr58VOVcN9IqZwqnu-KI355ObxgwvzzuP3Cs2kJL-pdigVjktOYgc6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
نشریه‌مارکا: انتقال رودری و یان دیومانده به باشگاه رئال مادرید نهایی شده است. بعد از رونمایی از این دو بازیکن پرز پیگیر باستونی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27109" target="_blank">📅 20:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27108">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AerS1I1t-trdajq6OULj9nmzvGoznXROBHrOfmeYZ_VjEiHbn3XrTNSAbCIIpn0ZFEAslO1RSyl_pSY6_6fbhDiW3dOT6kRyAlQB_Kni1MSRXXW1JFGPGCrq9I-3ERzG1jk4uEF11tbwM3FpkCdFyY2ChG25-njgJBNfrUWvPBJrfNMcYu7iDPAX9rFuGpxFaUKJCyE7Tib6vUzoCznoTni5Tx8LsepXi0613yHtfUZdos_YiCjF7Wq9OIMkjCevQLwaOkpo2KAZwVlPr9EW3gxCd993CJnct_DWHpRz0J1PluyHk9CNQvMJTz_gtBDOj5-48dthCXk5N-HS_y8cqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
پاسخ‌نهایی باشگاه‌فولادخوزستان به پیشنهاد باشگاه‌پرسپولیس‌برای‌خریدابوالفضل رزاق‌پور مدافع چپ‌فولادی‌‌ها: 200 میلیاردتومان نقدبدهید تا ما هم رضایت نامه رزاق پور رو براتون صادر خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27108" target="_blank">📅 20:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27107">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXX621IpEExEkvtXmrcYX-SlctZF8NJDLzaTVts2cj5E_Ah4euJTiJfnD0YD5EM1V6ixBYrSvFbNzyOpRkltkOtc0HKtvdZLFe-q90WszmZYLNfxkUbU-fgLCSIhvXH5HrKBH8fnGsrioE8Z2G1lowOYbr0ZP9OlGhnSNf7iY2EqdwTRtNQxVBZ4fy3qYcPQ0h3ue16szAPpjfiR_avXSp1kz4eC1GhdNPJclmh5C8kT_o0Z46-yqKmfr6dlwJ-Ftl4vW5EtvUnhreZeoqU9zKVgIO7KGp6BF98yTW4v7BpY1Vmf8J5SqXPF6yVlNfPtUAwAU9cJa26gs1lXa-eQdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27107" target="_blank">📅 19:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27106">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6169d08e.mp4?token=s7ITimAwL8My9GDBtcRK6ofDpkESksoStkAwHDlppeNGbCrGJSgoIZFTB_gBm8t2SseorF2SpXSQpgKYEioJaPAp3fn2fyVNBB__MplTRFIeJh9CA7MLykvDyJ26L62nioPk7ktarjP9NGR9aP33v_wCBW7FPmH44YDbz3Ey1c5KqZADH-ZXA6rCR-xC2PSFEQKLDqh2936u53FVp3RXTh0XJFOhmeLtNBKEhVZEIx4a8dpm2iNLC58UFYavgfO7RFcupsHA6E63etsUo-yQRzkX8_q-c_mTF-wM_fmRB57wmal7tU36L2hDLXcqEnsFpTz_6-bWWYQFTNVgXxItXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6169d08e.mp4?token=s7ITimAwL8My9GDBtcRK6ofDpkESksoStkAwHDlppeNGbCrGJSgoIZFTB_gBm8t2SseorF2SpXSQpgKYEioJaPAp3fn2fyVNBB__MplTRFIeJh9CA7MLykvDyJ26L62nioPk7ktarjP9NGR9aP33v_wCBW7FPmH44YDbz3Ey1c5KqZADH-ZXA6rCR-xC2PSFEQKLDqh2936u53FVp3RXTh0XJFOhmeLtNBKEhVZEIx4a8dpm2iNLC58UFYavgfO7RFcupsHA6E63etsUo-yQRzkX8_q-c_mTF-wM_fmRB57wmal7tU36L2hDLXcqEnsFpTz_6-bWWYQFTNVgXxItXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی عجیب احسان علیخانی که چند سال بعد به واقعیت‌تبدیل‌شد! حدود ۱۰ سال پیش، زمانی‌ که عادل‌فردوسی‌پور و محمدحسین‌میثاقی هنوز در کناریکدیگر در برنامه«نود»فعالیت میکردند، احسان علیخانی با لحنی شوخی گفت: «میثاقی رو آوردن که‌بشوننش جای فردوسی‌پور!»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27106" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27105">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxkCbUzBXDEB6AoK0fRLofcqAeN7vtOhPGLUDXlvmUwSLQmqM0nP9eJJL8WysK_D_Vk5JL0cPR2RqfZ8geh5Ygn6XP8hka4SJESCsNhJLJL5tnJR6MTP_7kqTVuiqxVVDf2fo3Req4idK1MRuQChHatZfd6QtQrZ44Li213mtOagmVGiXR-MSxqn7Dg7kwpksDRpg3NXH4IHfYrNxBiuAGq_CXmxZIXfGeQGlKbsI65gQ6zCqEcQbmi9E7syaU5swbiUGoGWr9td7bXLs59FVfrhosK3o1nTgPvmXZ_qN2EB4N4cGmN7sJN0fb97EXEcE-zGjy7Hi4xpBr6QEpd_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
سانتی‌آئونا: محمد صلاح ستاره‌مصری سابق تیم لیورپول برای‌عقدقراردادی یک‌ساله به ارزش 12 میلیون‌یورو بامدیران تیم بشیکتاش به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27105" target="_blank">📅 19:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27104">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=LvlaeLnDatx4mUG174yDk7RInI45aaEPHidSb9eaEtTu_t7j17Nbyydu4bQ0_-wi8lzJwY4RUWbtOBIv1SQxDsl638JsooxUTggI7SPY8qubFTxOORPl-m3Q9bkKcaRt2n4o49S7ibGi0cAS2QLIcyfT7nwdAEiRbaSVGymhqUJHGySrVtd0x3w0RsIXPBjCJ6FH2eZWqfUamjl3mDH7EXKTu4HieV4s7aIioixZqIlXq2RHGF7tsKw1qBEMNLOMVzJspXHqOg3YkOsOTNOFbOCE60Ka5UmQnQfPjgS_kIlvwruleMLD8vzKlQ_9ocnDy8MYFOPHaOhlop0ecP-zDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=LvlaeLnDatx4mUG174yDk7RInI45aaEPHidSb9eaEtTu_t7j17Nbyydu4bQ0_-wi8lzJwY4RUWbtOBIv1SQxDsl638JsooxUTggI7SPY8qubFTxOORPl-m3Q9bkKcaRt2n4o49S7ibGi0cAS2QLIcyfT7nwdAEiRbaSVGymhqUJHGySrVtd0x3w0RsIXPBjCJ6FH2eZWqfUamjl3mDH7EXKTu4HieV4s7aIioixZqIlXq2RHGF7tsKw1qBEMNLOMVzJspXHqOg3YkOsOTNOFbOCE60Ka5UmQnQfPjgS_kIlvwruleMLD8vzKlQ_9ocnDy8MYFOPHaOhlop0ecP-zDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترِکپی برابر اصل نیمار جونیور!
ماوی، دختر سه‌ساله نیمار باشیطنت‌های بامزه‌اش وسط مصاحبه اجازه نداد پدرش‌راحت‌صحبت کند؛ همچنین حرکات شیرین و بازیگوشی‌های او دیشب بازتاب های زیادی در فضای مجازی داشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27104" target="_blank">📅 17:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27103">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835360d02b.mp4?token=Bc87UqqUoASKbU2s8lL53B1qD6hVC-WPmGTewUCIxEN4wjnQhCxQA9FAAojfT2ZHKMKdZLyaDteBOizUubTL_cmde_oog4iizqzOXxhsRu6tw_ebTZZgdVISl41RCNnNQaJRMRFpvI5AX5H-zzPxahpnwPSDBli3iKj8ui60GKFlsLLE1qn7Rc86aDm6oJtyVSJsPI2iX1Pok6seOilXO-XKG4GmUinWNMqeQmn9_BjIxIDLfzViTx-j4wwM03FqEJt1RGSe8JunJBa090r22EKf1tu2Covcb0SqPbketft2DafLZAwy6fzjwVMVMmWooUajLUCegWYExyhCqO4Tsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835360d02b.mp4?token=Bc87UqqUoASKbU2s8lL53B1qD6hVC-WPmGTewUCIxEN4wjnQhCxQA9FAAojfT2ZHKMKdZLyaDteBOizUubTL_cmde_oog4iizqzOXxhsRu6tw_ebTZZgdVISl41RCNnNQaJRMRFpvI5AX5H-zzPxahpnwPSDBli3iKj8ui60GKFlsLLE1qn7Rc86aDm6oJtyVSJsPI2iX1Pok6seOilXO-XKG4GmUinWNMqeQmn9_BjIxIDLfzViTx-j4wwM03FqEJt1RGSe8JunJBa090r22EKf1tu2Covcb0SqPbketft2DafLZAwy6fzjwVMVMmWooUajLUCegWYExyhCqO4Tsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنظرم‌جذابتر از گزارشگران ماگزارش کرد در حد همین چندثانیه؛ گزارش فوق‌العاده گزارشگر زن لیگ MLS روی‌اولین‌گل‌لواندوفسکی برای شیکاگو فایر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27103" target="_blank">📅 16:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27102">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9QUx6u7gsYUDb0AxP66kLcmXWZVcjmSuPA7DhPuvU8c1DDl4fIM-Pjt6ohrs5q8-0di19TlJe6hODVBZtElcGQ8_prYzAk1Y4DKeGh2flNw1wAT_PUJzRKStCuXsFeOoacj2c13DC_9jHoBt8b10OPfgnnC45DAwGJ5FQtNiHd9V8Y6D5G1yq8OSYFt20weEI3-WoJirdkRYSlQ_fBgMP3siWO8mCizt2TRz2UI-7XOKQvW_UoGI9385QeHIXQuFybfabowPgtz1gFOAAOltJGBuBnHRoUBDFKwMDgPDa75KhQ-7CjyytN3GVKfEbO5rRrB1gcSdf7xnSg1SLzy_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
رتبه‌بندی با سابقه‌ترین سرمربیان حاضر در لیگ برتر انگلیس براساس‌تعدادروزهای‌حضور مداوم روی نیمکت باشگاه فعلی‌؛ میکل آرتتا با بیش از ۲۴۰۰ روز هدایت آرسنال، با فاصله‌ای چشمگیر در صدر جدول تکیه زده است. اونا امری در رتبه دوم قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27102" target="_blank">📅 16:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27101">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=qk2inXXEkmpgY6X3V590__zveG5zOCD9EFlJ45rbTPut1LZbupnGUhP8O3N_d-l6ArTzuSeuAmYc4Jbp1-nVdicF420Gqne478A8ESZ5pJNELuicc3hLlAORmyJRR2RmQMyc9EtrAvZQS-r8ehvMYUgpfT1eVYzaIgKM7DDplY0jw3tQVVej0zGJBg5udA6QUCamSqaDve7o9rHqn6KKxk47VX7xaCJSVjFTwjgQHPiq0A3DS3XNo93qsnabBf_MmVo2-_kzdU8cZTOffUjDHUuR1gnEXcZez1PMztEEe3h33aXcQGK6KZItLKmD-8Y7H0duo6tH8GhJ7nfwhz41zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=qk2inXXEkmpgY6X3V590__zveG5zOCD9EFlJ45rbTPut1LZbupnGUhP8O3N_d-l6ArTzuSeuAmYc4Jbp1-nVdicF420Gqne478A8ESZ5pJNELuicc3hLlAORmyJRR2RmQMyc9EtrAvZQS-r8ehvMYUgpfT1eVYzaIgKM7DDplY0jw3tQVVej0zGJBg5udA6QUCamSqaDve7o9rHqn6KKxk47VX7xaCJSVjFTwjgQHPiq0A3DS3XNo93qsnabBf_MmVo2-_kzdU8cZTOffUjDHUuR1gnEXcZez1PMztEEe3h33aXcQGK6KZItLKmD-8Y7H0duo6tH8GhJ7nfwhz41zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو تو چند روز اخیر بیشتر از 12میلیون ویو خورده؛ رونالدو بفهمه تو ایران دارن باهاش چه تبلیغ‌هایی میسازن میاد از همه‌مون شکایت میکنه. طبق گفته رسانه های معتبر، کریستیانو رونالدو و جورجینا قراره بزودی بالاخره باهم ازدواج کنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27101" target="_blank">📅 15:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27100">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atn4Lcd4hohGuNiM18-Z2wEtCES0mZVrKB6z464CNFHXj7UyqN5C8_U5C7o5NS-mu3LQdddVzh_E_I8PtEKjkHehhTYJdMNus1-QBOmltPKSXsjoqTmRkvjAsePcoujpSkQ4x7dUo0qke5KMvMqqpIazJPQiDftvcG371m7VuQ2Mp6zvT1vOiK5kFN_8xWGmgVOLOaNKPnRhI3I4mhhtiu2cW-QrJKHmQDsK0TeGMMCYQL4cti9efL-Z1RNmxOopRNwvclLJyUDDvBwl54LbEpoZyWvzwWmK0t9oxUpT9pKxTMxj1xS6-8jCW7vnzJi7MDuYMum4HuswiiPHztRyTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنایی که بهترین بودن ولی از تیم ملی شانس نداشتن و از داشتن یه تیم ملی خوب محروم بودن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27100" target="_blank">📅 15:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27099">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">قیمت محصولات ایران خودرو و سایپا 13مرداد
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27099" target="_blank">📅 15:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27098">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSXyJvVUr8X5hfCH9ItZzz-KEQz2fybwMS3y_7Y-9aatZcJkA4HCEiYY79ER_fKrlpRogwP-rvAugOAlYz-upWg9cPWXCCOAnJbBLIqbcPshmoQgtcZKrj8_u4Qnz6o2F5ZkqAkYZGEEhRga7oz1B2gEvqRl3bmW4gXyvwuD_QLpwRPcp3lIof_ppjCH2o-q3q37l1GhvMb3eRq3jrH4St11imCF5sT6YplVBc0Jkq-t_s8zq5wyfQy0gFIYHdtKLFzyMbhfjqtJcw90aEGd_OZctfvdepzhaqrf837nDYZRRG52lKNACOlWEQJRxO5l1Vk8UY0Czd772lqtHsjxYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کاپیتان‌ های پرسپولیس در فصل جدید:
حسین کنعانی زادگان، علی علیپور و اوستون اورونوف.
🔵
کاپیتان‌های‌استقلال‌درفصل‌جدید:
روزبه چشمی، صالح حردانی و امیر محمد رزاقی نیا. البته درصورت تمدید قرارداد رسمی رامین رضاییان با آبی‌ها، رامین کاپیتان دوم آبی‌پوشان در فصل جدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/27098" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27097">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MG1ewktB7RWipri6KwOpXn9Y5jZ2d6CdxauuuqBLpJ_hGWv17w1gVgPMnHt2yRZDdFIk8v-eut5cDMnA1FP6fgdL2fTPOmV2UOt50LFHqsVhT608mXU2RH9xJsSho2SvNGNXZv-2fXfWSwJ1zL_3K2XL6s-lMTxnyWM7HdHM_yPexteMGJ5wWmUACwP3VNTiFWsDxp0_QpwSn4lxDhVwUeXGzzC0NKcYZxJX6nWegr2TWMKaOWQ4G8S2dCD-tqqDOBljyXnAOiT-nHDp_MAQy0jIlhoO-Q4azq6vzz2SwqI93jAuPslwS50d01EMeV873rlBgr8hjHlbGqSxtA9wwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
عبدالله‌ویسی سرمربی‌ذوب‌آهن: دوست دارم کاری که‌سال 95 بااستقلال خوزستان کردم رو با ذوب‌آهن تکرارکنم. بسیارسخته‌امانشدنی نیست. امید عالیشاه مذاکراتی‌بامدیریت‌باشگاه‌داشت اما درجریان مذاکرات نیستم. امیدوارم که قرار داد منعقد بشه و این بازیکن با تجربه رو…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27097" target="_blank">📅 15:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27096">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OR5WEVcFG9loYHNCIvBMKDwfJ5nvKsRnS_p7SJjZ_ft5p55aJI6MZ4C82wHak0JnUbFKZZbNBye5lSEdAEjWa6eqc82fmWIrA7sKJfaPyPTkHY3fwwyYYOeDaOnaNjMm3fuSCpleAKD_MyMyUdVXS68Tn0u8RNrtrOy9XSSF8WG9sPBA-_D_QNEDFKQEyMho17Ut998rdaJWLsc-C5dK0woPnZFHmxbgCrRxm9FhA25F8j83kMPoSpL1A-4GYsVLPrQttm2GuJDuXk2ZqEuqDjfhqzqBn3DYDjDdousiSqz6o1lmariCCSVVbJZxm2kHN2RJd1FFvNSdr9ffMIJ3Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛مدیرعامل‌ تیم پرسپولیس امروز به حمیدرضا گرشاسبی مدیرعامل فولاد خوزستان اعلام کرده حاضر است برای خرید ابوالفضل رزاق پور 120 میلیاردتومان‌پرداخت کند. گرشاسبی به حدادی اعلام کرده تلاش خواهدکردکه مطهری رو راضی کنه تا این انتفال انجام بشه. مدیریت پرسپولیس…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27096" target="_blank">📅 14:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27095">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdfyA6EckzkQd1Ywf58KmbFyZ-K-2ODUkKXgTYc0RrdHeBUmGR_aeKuUeyY7Dk7ETwVDId6QY5eF3EkvosXlpd385CMeoobTL-JBByzxW-yRWAon5oVxEJNBFYFQH33geEOJ6G_VjfGVOXMzLMbcA8LKt0v-D5vbAZwjshEacGM0CN7ZDyLYH_1zbLeeRcKaBzbh7BFbVqPWML1U2WbMP6fHnsmIfWV5tno3LBasKE6VgEUJ14RbmLmKjSui1bLxRFmOgvV7sxX9_MavAT1oZwvMTUgUAAiz1a723Q97gQ7z-bobc1fgAAaLOyGwYbB6_IeCG4qsCqU0vUkdTNfzuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌_پرشیانا؛ آفر جدید استقلال به رامین رضاییان برای یک فصل حضور در این‌تیم 150 میلیاردتومان + 50 میلیاردتومان آپشن گل و پاس گل و قهرمانیه. رضاییان قراره ظرف 48 ساعت آینده پاسخ نهایی خود را به این آفر بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27095" target="_blank">📅 14:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27094">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGHhMIcoOcvUc2BlLjJ7SgcvTw1NFBHd9D1psQK_vnk8T7tezpv0lI2PVXGgygiYy2mdliyuCGOUkJdzYGkmvpOSdJy-lChFZnryXRjLDAaM3OyYWO9dsTGVjm6J5pa4Xx0P_8zSNZwHBBfk5xuJapHJaij9NNoPf5Ofqp7h5hYAzgncHHJI_ECiX77U6ep6tsmOF-P_QwjjUicf9zgSJM-lMc-nQLB08q9GCgywNnzupag_6pWQx8_oKjm4KM40DoPjlruc248IefYspcyC9qiEcV4Wgd5vB3kKsCkFakpXsWgBxct7mfpvUJz0XXpfFNOjZ0Ig1_vNrri7FzJDZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
عملکرد نیمار جونیور فوق ستاره سابق بارسا و PSG در کل دوران حرفه ایش در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/27094" target="_blank">📅 13:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27093">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBTgdwUWYANQ2o_sZ8xNi2u0WLZgp_ePHUYi8O-3LFJzhEZE0JXWnexXOqB4NhU5TeSFLLm__WE28XiG_HVPQ3e-5DCyUXLCJjdWrgBCmEybZFCYyJjdEeN6O6LhTIk_asuB-Fafn4dkUe8ZQExl9xMhGdkUtaKRy41RN6dIpFWGc1M1RJw6U9dxw32AhYnCDC36Y5H2UZh8ChyyDgASyfAwQwiHpmBBFLhZCn_0orXzi3tgUonUpg4o9UDH5jpVizq3Gpjxh3fLlG4pGK4CA2hRDghtz57ND20Mvtwj2GYSBUDXPlNU_nY8972VeCv2fh1bMBQdnYoZtCKnhL-RoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روز گذشته شایعاتی بود که فصل جدید رقابت های لیگ‌برتر یه‌هفته‌تعویق میخوره که سازمان لیگ تکذیب کرد. لیگ برتر 10 روز دیگه شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/27093" target="_blank">📅 13:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27092">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnTDy0AouvkoCs3SeAggi8wB_ox5hqTGsf5vvtvStzN-0CkAAJT3wpgxX7kuTb4_l0Kf4W-dXNfWAlJolldLk_SScMdVtTeCh397NtxYc-TMEGSo8LMWAL0V-P5Vfer6abbfxbelVGkpMxoLnvxSnlOKaGhq-tLys_s9Jg377y6nRzTJe3TctKCR3wzpp6XqjINDrk4czajfjQxH2WdtPPTCCnHph9QJ4ESgG_3csEEnNfZcYEKwIpOjm90WpCi_LgrjfxfQSjYUC3vu1crHt8WWdFxW2dR6sVExuJhoIiG13F1s0O68kB_ywSythcKqFT9DRHDs9KGwhl1h_jJJ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
استوری محمد جواد حسین نژاد ستاره ایرانی ماخاچ‌قلعه: پروردگارا بخواه برای من که مسیرهایی نروم که باقلبی‌زخمی‌بازگردم. کمکم کن جایی برم که دوست دارم اونجا باشم تا همیشه شکر گزارت باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/27092" target="_blank">📅 13:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27091">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9be54cc9.mp4?token=awVifxQP8M1Vqs6lZnV9YsaaILXvhTHtE5R0As7xRSc4jryVGkLrfy2z6By7LQkO2SvNq-Tdi6s752bXpMv8p5xUp3Vj1aWOBkFMIGaukq8DYW29zolwfOdwoWwc1w8YPRb4TTlevxGtBZx2W3Yay_cmGAtficQZD2VEQvHrs6SRsVEF-exoNWJ-zgiWM4l8e2nvmPKLJo67b92ume9qc-M3dE7vURQlfR-Sb_jaeDVOaucILbjbpZpnLpE-KLv9LjwhTrI4IC1cYXuZtXy7LebKWCYAhzICmRro7fk0J3GD_TGEY00-lVD_cL5hzwOxm4pYnx5Ed8MczWmZP3iE7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9be54cc9.mp4?token=awVifxQP8M1Vqs6lZnV9YsaaILXvhTHtE5R0As7xRSc4jryVGkLrfy2z6By7LQkO2SvNq-Tdi6s752bXpMv8p5xUp3Vj1aWOBkFMIGaukq8DYW29zolwfOdwoWwc1w8YPRb4TTlevxGtBZx2W3Yay_cmGAtficQZD2VEQvHrs6SRsVEF-exoNWJ-zgiWM4l8e2nvmPKLJo67b92ume9qc-M3dE7vURQlfR-Sb_jaeDVOaucILbjbpZpnLpE-KLv9LjwhTrI4IC1cYXuZtXy7LebKWCYAhzICmRro7fk0J3GD_TGEY00-lVD_cL5hzwOxm4pYnx5Ed8MczWmZP3iE7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌جالب‌ببینید از نحو پنالتی زدن برخی از فوق ستاره های فوتبال دنیا و واکنش دروازه‌بانان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/27091" target="_blank">📅 12:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27090">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17e27275fb.mp4?token=AZ4ODLaTnuBa6AjrdWVNpoBcMd3G4P5yq8xMpe3dcYqMsTDawvU3Z57pKH1S1jCumsXFKBoEyOPkkLLGir96wS0pXLbo2Wc_4jFEBs1i4PXzX7PJyXQXfzAZuNmpXmer2ebkKdD4W3Rm0FaYTQfWrnSzEgWg3B7PNlDqUFG3ieStlLZ4rfqbze6TlSptquTQGIjoT_9SCxn1mgUmS79CGSvTZtPcCVhCntPKMCgBHMbzKTPL75fKCXYA9pUajQhgG85sN2EAHNCoNfVdIL9F-O760G69WhzCymM6lgkVVEFHz6v9aATbmFCS_DOoTNpQRVjdNrmjSXMkhVisAgsX7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17e27275fb.mp4?token=AZ4ODLaTnuBa6AjrdWVNpoBcMd3G4P5yq8xMpe3dcYqMsTDawvU3Z57pKH1S1jCumsXFKBoEyOPkkLLGir96wS0pXLbo2Wc_4jFEBs1i4PXzX7PJyXQXfzAZuNmpXmer2ebkKdD4W3Rm0FaYTQfWrnSzEgWg3B7PNlDqUFG3ieStlLZ4rfqbze6TlSptquTQGIjoT_9SCxn1mgUmS79CGSvTZtPcCVhCntPKMCgBHMbzKTPL75fKCXYA9pUajQhgG85sN2EAHNCoNfVdIL9F-O760G69WhzCymM6lgkVVEFHz6v9aATbmFCS_DOoTNpQRVjdNrmjSXMkhVisAgsX7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام رسانه‌های افریقایی؛ پیتسو موسیمانه در آستانه عقدقراردادی چهارساله با تیم ملی آفریقاست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27090" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27089">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370ff98a06.mp4?token=CwGjIp9Imw5JEBWb2nViqiJkAzYOz6AFOWMAcLIrbsQwKIze5UFGhtymwKipVDtCrHV3cxsRRz0Agj3077gFmzqzjfHLzQCfjwnb3Izxtzt_bSH2uOH2UHC5RAeTY9LAhkRyZ2gKPjsvyoEnRb3JgbbyiMjwauUhn4YVguezaCGut6Xx8mQHAJ_i8KHWl-ppwDuxw7YCUDdJl4AO9dois9dwRNZlShkhySSswjONR6i1CTIoc8eeHms5IZcb85dvaJZc24aZr5otfyjU4lH3ElARJi__OcKFvIK16GfA2RAdBVGb_j3nSzO9VxrVTuva-f4vVJ0OuMv1OPMW7DeI-ropwu_oXauAlGqGl-1p1huqkYQVJc6CeokqYLVUqqYPwu-ZhrzTtH7gAojOwsz_dnAmn6g3fOJ0GSUrW5NwuojZ5kq0fzXK2Zy5E8UeOSYT5HA4NQc_PxFIC1OFSL1vjb9eZeh2zyCvbhO-aoGGF8XVY0Sc9o7H5KUi7hgu8c56KCqwlFcQL8Yxe22_s_aKEdMMCxQfnXVmBKlTNnp1iDM66f1Gazrwf2598zr5pDlZ7zn4i2hCnv0uk4kjKgpxCxOu3uMKB-7eRuhia74rTovtpcuDX94DTYmV2s8co65ZnOiF_wp0Ss_EV9hFyK66cAaEdhCLaD7zRHBFRHONNlE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370ff98a06.mp4?token=CwGjIp9Imw5JEBWb2nViqiJkAzYOz6AFOWMAcLIrbsQwKIze5UFGhtymwKipVDtCrHV3cxsRRz0Agj3077gFmzqzjfHLzQCfjwnb3Izxtzt_bSH2uOH2UHC5RAeTY9LAhkRyZ2gKPjsvyoEnRb3JgbbyiMjwauUhn4YVguezaCGut6Xx8mQHAJ_i8KHWl-ppwDuxw7YCUDdJl4AO9dois9dwRNZlShkhySSswjONR6i1CTIoc8eeHms5IZcb85dvaJZc24aZr5otfyjU4lH3ElARJi__OcKFvIK16GfA2RAdBVGb_j3nSzO9VxrVTuva-f4vVJ0OuMv1OPMW7DeI-ropwu_oXauAlGqGl-1p1huqkYQVJc6CeokqYLVUqqYPwu-ZhrzTtH7gAojOwsz_dnAmn6g3fOJ0GSUrW5NwuojZ5kq0fzXK2Zy5E8UeOSYT5HA4NQc_PxFIC1OFSL1vjb9eZeh2zyCvbhO-aoGGF8XVY0Sc9o7H5KUi7hgu8c56KCqwlFcQL8Yxe22_s_aKEdMMCxQfnXVmBKlTNnp1iDM66f1Gazrwf2598zr5pDlZ7zn4i2hCnv0uk4kjKgpxCxOu3uMKB-7eRuhia74rTovtpcuDX94DTYmV2s8co65ZnOiF_wp0Ss_EV9hFyK66cAaEdhCLaD7zRHBFRHONNlE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ رافائل لیائو ستاره‌پرتغالی سابق آث میلان در آستانه عقدقرارداد چهار با باشگاه منچستر یونایتد قرار داره و توافقات درحال نهایی شدنست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27089" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27087">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBSa6Ojopb31PHfwsShSkNj4nzi-7IZ-tCfDJ9XjQI7UoTuOCLnGUcTa2CoJ3sSozgRrtXcdR9d_SRhqEOPMlMbCbdRVA5YIydRw4aK4M3O4WeyJFn2oZI-xrbtSIjaqR6pogmV-TkjgjetZcn7E5OLn6KE0N6-OKyzVlJVlo02a7Tq14-d8Gisa-WO3BlSuAqD2B5Oidq2ZuICSGDz6MVx21psAoEwoQExrvO2BuEjl2t-l8URr2S1G4F1bg7oEjdlCuWI3BJEricQcX5vUxdOe6JY7EcgwHYIcgHyyGfpUZRnuHO-QMc_oxECzmMC15HvAZYsUEDSkZ8_uW0aQZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینکه‌گفته‌میشه؛ باشگاه ماخاچ‌قلعه رقم رضایت نامه محمدجواد حسین‌نژاد رو 4 میلیون دلار تعیین کرده کذب محضه. بار ها این باشگاه به مدیر برنامه این ستاره اعلام کرده هر تیم ایرانی دو میلیون دلار پرداخت کند و خودِ حسین نژاد هم راضی باشد این انتقال انجام خواهد…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27087" target="_blank">📅 12:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27086">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ymg3Ps5tIrIu53Cf_90ry_zHsReEUzKrzQw5junoZv6eceUly5WEpekHjJN-gxj6KaW6uegWhCJ-3oqNjhYXyp2B6VvxNoGH0JbXiYAdMuU-ert2ecjuCb_scjGhYOzOwZaQQDwsfV4qNGhICLQhwzqE1Ju16stL_4WbEMuZkEdvFe3o60_JPCA50KhCVyCJTYnoSaG0DVxhtnxk7yRwinZ_XUkmoMhFnZ5kzSN0eX3gFu0qyb6MJC__sCW67qsLrDtBBcLdRrpLogJe-PES6vc3v1wVd2oY06LC2fg5biwIw6sISuaW_BMSUkBjYyTsYOIL55ogIAsgfKa5dQdzYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رودری ستاره اسپانیایی 30 ساله باشگاه منچسترسیتی:من‌تمام‌پیشنهاداتم‌از تیم‌های بارسلونا، پاریسن‌ژرمن و منچسترسیتی ردکرده‌ام و تنها هدفم دراین‌تابستون پیوستن به باشگاه رئال‌مادرید است و مطمئن هستم که این انتقال‌بزودی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27086" target="_blank">📅 11:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27085">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Io8TTa5WT9gSKkNDLUsGN0pVNMJu0I_SNLulnTLuWffzZP_yvCuiYYfQDzz8duSLMlndl25JS24PRR4DR6SI3u7ga7zM3qCsTZ3SkTkfidS7ZnQ58ost9-jW40tF3Ui1GbTU2NgOs05OvPvxDPxs07KpnEix2I9dzopxoXzI539_qMmaB05Y15LWVzkzkN-HqUa5rU7RuLU7Av6NGRIyj6O_XzkWN0DdPvMdFKN7ExB9f7zMirz2ATBvJ8CD2SLUzUI1yPNq3q-H4Hqv6SBI1EFzSy_dGiv-NW-s7no0LFMdzHcsdhVNLmCVPvDSrfgk_AXyy2hmMqRVWDohepSphg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیویی یک دقیقه‌ای از سوپرسیوهای تماشایی مارک آندره‌ ترشتگن در دوران حضورش در بارسلونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27085" target="_blank">📅 11:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27084">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWbi_fw7y_CDqzSbmn2Z59UBnSeef1M9475llMxqAqaEzVr6KuiEcvXjxdwkd6rYLbsgi51aD_Db2pfZUnPdXe2dtDDd4OcukxltLMTWv8chdYGJgEKcmzfKOPLf-cJWMUTOyIlYdgPmhuqwcO_D8Wh__cSQqL5YsVUYkq1llgOeu-V5TQd3ZEjZzYFDfxPBlbo_k-o3nqlUghaVFx-a4i70tUEOB16Q2fCZeMKdlVazwI8p7yjm8knjx0bJykMQxAdezeFdetoiIX87TPxmNmcosg5KEBC7XRC9Rmeq7Q_2yDAnbbtLK4dXU9szeHFzu4YEMOjB9mri54Ic9W9K5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27084" target="_blank">📅 10:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27083">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=Y010kRHiv_QHdTl36NGeRbVNF5lkGj-Fk9EnuO-yyyQBp24UJNEdUH7YCYvhRdUS-cBDvm4YPrk8u3cIJni8islPioqgy2ZH2G9iXE5Pl4j57_2jAxY2NqMKsRwe2Tn8ERTM9Jigc29kQl_pbbGctBjx1eM2XotnYxYS8Bpx7XINghgYvjGlDj1OrLbDqLrNnkmSFFsk6uinD3HarVAEQDYhPVsWb8-PhgCkWuXmPOAycKaK3koOl-LaGHG33BlZBFtXyUj8BbbcrgTCRjiRMHeKaRGMHQvEJ24hA0X_rXkUxd1pSrKnVJLBGMW5Uoy9RzPOxv0cVCqRMTVXU_W-6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=Y010kRHiv_QHdTl36NGeRbVNF5lkGj-Fk9EnuO-yyyQBp24UJNEdUH7YCYvhRdUS-cBDvm4YPrk8u3cIJni8islPioqgy2ZH2G9iXE5Pl4j57_2jAxY2NqMKsRwe2Tn8ERTM9Jigc29kQl_pbbGctBjx1eM2XotnYxYS8Bpx7XINghgYvjGlDj1OrLbDqLrNnkmSFFsk6uinD3HarVAEQDYhPVsWb8-PhgCkWuXmPOAycKaK3koOl-LaGHG33BlZBFtXyUj8BbbcrgTCRjiRMHeKaRGMHQvEJ24hA0X_rXkUxd1pSrKnVJLBGMW5Uoy9RzPOxv0cVCqRMTVXU_W-6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هونگ‌میونگ‌بو سرمربی‌کره‌جنوبی درجام جهانی ۲۰۲۶ مجبور شد دربرابرمجلس ملی کره حاضر شود! او توسط نمایندگان مجلس کره جنوبی درباره تک‌تک تصمیمات تاکتیکی‌ اش بازخواست شد. از تعویض‌‌ها و دعوت بازیکنان گرفته تا ترکیب اصلی تیم و سایر تصمیمات فنی اش، همه‌چیز زیر ذره‌بین پارلمان قرار گرفت. هونگ در ابتدای جلسه هم از تمام مردم کره عذرخواهی کرد و مسئولیت نتایج را برعهده گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27083" target="_blank">📅 10:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27082">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnVh7TcDH0RVx3sn1z54Ma4AXipnOoQHdKM__b3qztYvcBewbaL9doVPu6vHbUz2KMF-DNAb3c9btMgxEdd9wMpshd80AGeDo0nceRDklBNjO6zcR7QBHhE5w9RcuEJKtw649VFZZXAJHFMoAnLRnS5MKBnpMgQy_xYTemmf2CSxzmJ1-zwvBQ3Hc4J3B6guQsIAkihFc_OgXRSyBeARAP8qyAGshKGv48GshUE7yUMs15QTFIQFUZgLmloXnTiKDa1bGAHRetnxdUvFU_kjjJhrR1TxjgOEXnd1oKUCzwN9NC306jNGlkwTSutKA4xbWpb6zY7haZVyiEbgODQ2uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
نشریه‌مارکا: انتقال رودری و یان دیومانده به باشگاه رئال مادرید نهایی شده است. بعد از رونمایی از این دو بازیکن پرز پیگیر باستونی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/27082" target="_blank">📅 10:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27080">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JERqIu6HKaAy1eOxvBkSZxTJtNwD8ISGdNfKJ7TwNeLP1f9NKk4Rr6BNmIfpriyxCxNp3a1OXXOg9z-b2sH_M6gQ5Z5Whh-Q1LHyAD6NgGriRGpn50J9fNjl1x799rvKeHUdtik3nw9W2lpclCTYyeF0FlUEiddlRGRuDbokBVC-JV5RSrYXNtPMIcpApaGRUo4NYG5N54kPPohr7daKivOnOUFc84gg6sqJQW42AabLOpNonJzJZgFl5oFL2qiR435h3zMPIeejj0E0Zbwd3MhS_ajrWIjSizvyO7ivWd-YHKXGA_tqpoHjZjN8A2b7QCqhaYQrIJ87IzIAnk4m1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جایگاه‌جهانی تیم‌های ایرانی در رتبه بندی قدرت اپتا؛ تراکتور تبریز درصدرتیم‌های ایرانی قرار گرفت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/27080" target="_blank">📅 10:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27079">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWzW1lxhHgM3h7Zu6svbpluhOJyETT_G4cYFudKZIW0tCVrT5pUouNYlNYIGpNFZ_Wva7Wqds6qsKwTLf5KdVLyEYzcWc29fCQocqFUNCkyy8p_HxaXVinEvJ8TRIuUGcH6iYjKuCUZH0r371CRcDJYbZvmPO7mb1dwePme2PvgYBEtrTwd8YdHxaMSxzqBFvwL6aWfsByMoyfH0ucykNuvfk3MJElrAq7BNlWkpFnNNmASjTYsTLWyHDIM-tsc9twt_9BZGUfcuCDnINha3JDW3uWnZ8dQiGJz5FpsHuy5OVkjRChQg9-bTqnxzLrs0Q-IX4dWDqtrPwN3bcHK2sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق اخبار دریافتی رسانه پرشیانا؛
سعید واسعی هافبک تهاجمی‌سابق تراکتور و مس برای عقد قراردادی دو ساله با سپاهان با مدیریت این باشگاه به توافق رسیده‌است و بزودی باحضور در دفتر مدیریت قراردادش رو امضا خواهدکرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/persiana_Soccer/27079" target="_blank">📅 01:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27077">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdF2tfSxIN9PP4Ja3DRkFGsxnARHlKxpu3z_8pA00mriJGfBRqKoSIqZ415EB2xEzFfEDMf547U5Sak7zjwr5Xr_95GysSuExX5OYAxawRUoQi2v2juMIbIR_oNoU3BHGlsxN1dCBDlIqxwGQrsVor-EvSwBEynNabiDXewEQWwerHZnJR2ibNANMRP4k4psTJuJQBV0ARlJy3r_A1ioR7vM9yoR8rmqLlmhQSqejykEHumRORG4JN8N4xr9wbn2VMyWvgPSDc5KQxvyF6MOcqw2YtRBVcZ5uei-QQ66zkfZCxoOI0AoXZlMuq7aHBSUzfvdNnmysSntqayuNovxsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌ امروز؛
مصاف تدارکاتی و راحت باواریایی‌ها با تیم میانه‌جدولی کی‌لیگ کره‌جنوبی
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/persiana_Soccer/27077" target="_blank">📅 00:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27076">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTjSND1ArRuQLr0RIyc2mwhdeho7Uz-Nz7vfUz2VUT30GpgfX9QSHDHCBihNi-rNz93H3JBLbrnc3vstjgH_8FSqMPj2V14k9tD-aroZsXgECfXFu6ZnVkOuswDhYWJT5IpjrljN9kFZWgeXm2SfL2fFMzkis89dnRpCBi8hPC7zQ7Wq4yn_i1bBGAC0HimMBfv0OY4CmPno_ElWWlvW-x_uwhRF5pB6a2_X194BgID591bUtFu_I5_W0UusxXJCuq2jPpkMbCdh2ihuyZbIJ5WAQA6Z7o6qjFP9YW3VCGLyTfRIfYdB1tBrQp8Q4RlJov_0wuk1RkCSFZ1afx280A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
روایتی‌جالب‌از آیمن حسین ستاره تیم ملی عراق و زننده دومین گل تاریخ عراق درجام جهانی: در سن 12 سالگی یتیم شد و پدرش رو از دست داد. بعدش داعشی‌ها داداش دو دزدیدن و هنوز هم پیدا نشده. بعد بخاطر جنگ آواره شد و یه‌مدت هم بخاطر اینکه مخارج خانوادشو قید فوتبال…</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/27076" target="_blank">📅 00:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27075">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3wcG5-j7STHe0WOYU5yKJqZbsyFf8GQ0qMHOw6ZZUBB1zX01BBOGJIqeG3soBooE9_JRpoSL4tGHsNVeHMZ6Lx96Lnc0a4e8vKLho9b_weqt8d-mpCyHEq7bKlxz8Y7b4CFL7h5JyJCAoJXmdYOWgjAOnr1nqx8k6e_kesDkHbgJqfkIh7XswfQV_i1zguit8F0fSAJ3pvLMWL-SuV7sfdM7SGn5nfsM6Fw0SUC1uKGGWEmf3OmgR53vV_ixwFliUDeWRZ_kUc2r0lCJ5oUBs1qBXTdztOvzcRRqFs1RFvz9BXHF9tAlbjaTUI5CQo9tlomaAUBonhlVFA46C4sjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
محمد قربانی میگه‌الگوی من از بچگی تا حالا کریم باقری بوده. حسین‌نژادمیگه‌من از بچگی طرفدار مجتبی جباری و فرهادمجیدی بودم. خودشون با زبان خودشون دارند میگن که دقیقا فن کدوم تیم بودیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/27075" target="_blank">📅 00:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27074">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWgI1RBhMI76nlMySMgmocglI0HC9iGYca_nF24KgKAUQtnaQjgp6Flpy9Ht3cNr_6-vmGknjmNh_uusWbWZycY_ZL4BrUropiiBO8Mirew3YXSGYCBR_KdpmMPUnS6OLsd2VaasMC3bSrlPndbwAgGvDOLw5UvnLfInrjlhJ_vahehdaorW3JOZS-GNGRYuEJuSSnPNarzL9UPJK0pyUhIuXjHdm2-LmlK360VD32WnkRiY0_iDzl-UvvzGqa3YF72G4xVVhNsaJ0Hgf2D1jjnXtsm_1orpmdrJnDgSYwAStcJ5TdGxbQb_McthuD0Kpzw7lKaMRyq5V314G18FFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/27074" target="_blank">📅 23:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27073">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVLVTOJINyMxw7hbRIapTbv-iKuR2K0e9wzLRcx0cKULGrJnlW6Op3B-5wGPKon2UchecbDKOsw11resTNR11C-062FjQpYFEB0nR-C38r3BE5Uhl4-4MFfVwgXywf_-MET5MDyeFfsAZtWx1S1DFsdzvq9lxqUZLWR3Klzo4PIwwfsmJM7I0JU6JGMgwjXKNi04Jsc7i1X87dSSWZuIHAzSsh1qiqGrO00jmp30tXUADt7lxg_0gSXflbLD4tL-tYO6HksyeUAndoDvEw1VH9GViAlvMP9XasPMOwSVsIgQZcvqf8PDqaEXI98YMrmBOAdF13J90yGIn7JhUvM5JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دادگاه‌عالی‌ورزش "CAS" روز سه‌شنبه پیش رورای نهایی‌خود را درخصوص‌پنجره نقل و انتقالاتی باشگاه استقلال خواهد داد. اگر رای مثبت باشد فیفا پنجره رو بازمیکنه. اگرهم رای منفی باشد این پنجره نیزبسته خواهد ماند و با شروع نقل و انتقالات نیم فصل پنجره آبی‌ها توسط…</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/27073" target="_blank">📅 23:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27072">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSA7DfVsTTMR0dQcbCrbYbbFQfQiMrgzQN66HyAjqa0hOly14Iij01cV2mzAEQfDXEOJMtPvXD7sEWam8mBXHZhsELDp0l71yORKBkPL6-doYAJdupV6Q2j0Rx3cK496LsaUJUdNwJa9O_QMtE-FTQn3UsE5DYJTxP5YNpu0g-Mlnr24Ljp15Zpl76TZ2Lg8Kq2dUBcRNL3FUABsOAU8pkYOhODFg-b25TavgRoJUhfzw2sqeZZkum8ddLQUXY_Pndw14RO7INbAK0mycHQ2JijY7UKOfoHHcFsOSi83k4FeqyCfpsPUo27C_dVJgQOElQ1aRtcrP_W_n6INd0KHwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
اسکای‌اسپورت:الساندرو باستونی مدافع 27 ساله تیم ملی ایتالیا درخواست جدایی از اینترمیلان داده و به مدیریت افعی‌ها اعلام کرده با جدایی او و پیوستنش به رئال مادرید دراین‌پنجره موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/27072" target="_blank">📅 23:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27071">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5uLT2YtKS1q_c7HSIyBAPe0qlK9BtHin8lGyFwTO3MEDADIQQ-VOrSaYSYww2Jpx3GxHnVR_CwdVntkYDJwP0jqwqYJdZpJxxDQQbzazbxGq-I43F57sqfr_1Ydt18SFSYHwf18Y77dwYlvL8Z6nrHu-KKdMbxPzF_89dPGP9lw6QUsdmEF3vpQyAs1Tug5sGcIjET6SnyvBm2-GEhQ6yJsiqWZrRi_WN4sWseJ4KXKk3923ABau6biMcaK9R0Ct4HJoe_9Oj51Huhf1v_v6tdQhHqVk-UKmBJSe0SFBNuZZbkLSiEIZ6Tw2G89VKAPW54p_S_0zc6Vvg8znnA8Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/27071" target="_blank">📅 22:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27070">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8SoMlmVmpPpjcKCpeIxYc1taG7dcdyixfRwlNfdzTGveXssb6EcdJWO5hPnneCGUPUaZNrVM00bQUl25Ym8HSFJLXXNyat5VXgmdtR7uaFiTJzMzsZp0JZ7L0xZ0wvyMNfySDftLkwRkoG41RmQamZWQYeDSXzvmZB9pcZ_Uw85fr1SPTeQi1ad_WjHi2nHhSStJHRIoBloSc947UULfUZDOFvkiVpNaTiaxHcwsDEOUP3HIyXoqx128V4qyrEGVuvkCX-zJ57jbGnZg5iy4a2SFsU9NkKw-0PkAcZLUTVw02ADNRDmfEbFtNIkiI0CPHmViHLeMZPGk7IGuRnC_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ دونالد ترامپ: این آخرین فرصت ایران برای امضای یک توافقنامه خوب است. امروز یا فردا می‌فهمید که چی میگذره. قراره به زودی و به یشکل دیگه، مذاکرات پیش بره. کار خییییلی پیچیده‌ای هم نیست. قراره فرداتنگه هرمز رو کامل باز کنیم. بعدش هم در مورد ظرفیت هسته‌ای…</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/27070" target="_blank">📅 22:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27069">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hudtfyiSRP03FYmYZEFgPPNV_7VzyqnNtoDcpl9HRkXVvPLBQsr4fb1J2onyOvQacTOJ2wrgEIxZhTxJVq1213qR54t_vZhJcBaBnZIe4yMUGDQiAPlzfjJudOhHx8qQCseaLGGJ0azqZYouzvkiqXHnnHENP134OOo9y1Fy0W0ofUG5SW_hS1MUWMUVnoo7R07RhPK2T1JNhQHAGz1n5wK9mIKhKBJ_k3757kswbU0pib68uYVKqQ533HlqCm4x1iaipV3BnajuEBmMTTPNlE-PLlswHhXltrZMV7Ba8V4nF_EVJ8q3vpkPK9C9Y8f3MRYWCYaG92XC5eoFq5Y5Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/27069" target="_blank">📅 21:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27068">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97c6b80b0.mp4?token=k-FvkbxOhW2NcwN8NYnMjCpjARuFfZXzs74eokME-7BHrY1dktVTdiZk-E_B4kNbW5mrNcG0aMInjfaJ3o9pWVOxLRI0VbGktwPBaicMq40_j8DBRPGQk3T_VUmSwLCv160ZTOI-ulc6bgHxi71Ins335DjmlKbJ-YhelCjoU0xiLiDdW_wReJUrIuVao5yBPPIZLQA7N5kWh96xXIPt0DAty0A19G8IstQw38FuIuP12V9nlLhHRISkc-h4KumHfJWS2UWIQNF1YWFCpV_xYyIcHij5lGyAAYAg636VVOv3hi5X-JvTZ0pZcfscerkhYeCP3YugGg9I-0zsWbSGcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97c6b80b0.mp4?token=k-FvkbxOhW2NcwN8NYnMjCpjARuFfZXzs74eokME-7BHrY1dktVTdiZk-E_B4kNbW5mrNcG0aMInjfaJ3o9pWVOxLRI0VbGktwPBaicMq40_j8DBRPGQk3T_VUmSwLCv160ZTOI-ulc6bgHxi71Ins335DjmlKbJ-YhelCjoU0xiLiDdW_wReJUrIuVao5yBPPIZLQA7N5kWh96xXIPt0DAty0A19G8IstQw38FuIuP12V9nlLhHRISkc-h4KumHfJWS2UWIQNF1YWFCpV_xYyIcHij5lGyAAYAg636VVOv3hi5X-JvTZ0pZcfscerkhYeCP3YugGg9I-0zsWbSGcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فصل آینده تو بارسلونا میمونی؟ فران تورِس:
‏من‌قراردادی با بارسلونا دارم، اما در فوتبال نمیتوان پیش‌بینی‌کرد چه‌اتفاقی دقیقا خواهد افتاد. من هم فقط منتظر هستم تا تصمیم درستی بگیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27068" target="_blank">📅 21:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27067">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d787366ec9.mp4?token=VBLQ8nQ8IX_-CACAZkYGm_vl3VW69RZgHVu7U-LWIvYdqXZpH0kEWKSRlBjS_JBP2GUUTRr6C3OA2LS5a97IU7WzpkiuymTtNPn1TGX6PY9o-PktGk8HJrcznM2f00DgWxFHFjd-rlYF870s_C9ON8jeCf5skc_EiM7wDCkB0iWOD9TBq2-tY1nLAcE8Qgi0q678lGkiw_XM2gYok3PjhS8dZ9e2Koemxzl2CzbJ1LAQ3GGcv9pksbuHTs-Al1z3DFpB8Awoe1TV5S18QI9RRg0IFVJwiIURnVtoIaaHZZoRjKvf-Dl0rY7YX4AGrtwMPjIyw_oLz5R2PPvPcqaBnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d787366ec9.mp4?token=VBLQ8nQ8IX_-CACAZkYGm_vl3VW69RZgHVu7U-LWIvYdqXZpH0kEWKSRlBjS_JBP2GUUTRr6C3OA2LS5a97IU7WzpkiuymTtNPn1TGX6PY9o-PktGk8HJrcznM2f00DgWxFHFjd-rlYF870s_C9ON8jeCf5skc_EiM7wDCkB0iWOD9TBq2-tY1nLAcE8Qgi0q678lGkiw_XM2gYok3PjhS8dZ9e2Koemxzl2CzbJ1LAQ3GGcv9pksbuHTs-Al1z3DFpB8Awoe1TV5S18QI9RRg0IFVJwiIURnVtoIaaHZZoRjKvf-Dl0rY7YX4AGrtwMPjIyw_oLz5R2PPvPcqaBnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
دلیل ازدواج کریستیانو مشخص‌شد! حتی قیچی‌ برگردون تماشایی به یووه هم‌به‌پای جورجینا نرسید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/27067" target="_blank">📅 20:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27066">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrlzevPZVhrqnwu5TzBxh1LUD07lL1ph9swi7DcjQnVz60x_IBlojt7SIzqy4wRa6Qs9WoSekyckPbJi5lbtHvid8chwespkzTDivtwTOtd03-DcmVo5hGB8wiubAxYhO7pUDV9rLqTwUCyfFv9R5EBDzfuJU7_WeYRgvSyvuSTo4WDaedXLHJ0LJovXBhtbB_vyYADCqaXode3NXSgrPkWMASuChYM5m9Ib2ELhIOusL855JCJzEHtBoM3REcAGxgzCPRQ3xrHAGtnKZCsOkOcH71NuuG6XwhgUKf_bqZ7c_TXb3ji4BY5g1dZPQ0RQvQOIbtOJzKAhBwMnMAH7pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛
یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27066" target="_blank">📅 20:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27065">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkqwOTo74BqTf4vJi32MH62hIm0PmMOksxGJl70dTQwAFSCR3LrsZYxQK1_x6B2KcD4HriF6F18ZGlFLuWhkZLwTtZ51jy3EHBnsyVFndgcjlmudQifC3FR98JIANPyuH_B2-A9IUliDc2L2_drSxBUExtL6lyjuqAXEewuGgtATolJLbqDY1y0NLNMUa1T-bMFoMSu0hTCPVgB_96Q7o9q8P8Wt0wBUtkR5bMl1tCBRxU71iYkf422111K-KBsr3qM6ecdr6EO9ZtiiU9oxxmDx7Q1HMy2j4g3C4NuKLnuNi6nmbVo4YBsO8N6GH6i5oaj5-cZonQYUY3ebn7m8wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
طبق‌اخباردریافتی‌پرشیانا؛بعداز عدم توافق با مدیران سپاهان و فولاد؛ امید عالیشاه عصر امروز با مدیران باشگاه ذوب اهن جلسه داشت و برای عقد قراردادی دو ساله با گاندوها به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27065" target="_blank">📅 20:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27064">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKifyal-rQZe0HAHp_BglMwPVZeE4mVFdjEtHGTrDsTmDunQaANxcUD6YDdX798hIu9M7nKyFGEY9dK_1rh7soNdByKZvfyCQQqjOFo2nA0a1Nfr92Q3J8JAhAV28x81T_s5fkXxD6-0U_d93CxCaUEmYXxL1NlSUVh7aE3GgRT_w1aX-DyPkSGzcBpaZJPYOv8DgHK1rWefB9QcHCD-7lCOfODq2J_UEomFJ2kYzkev0BOiNHpYuf0zOGTG1EfPxhs3yPN5TxyzkNOc9okM2HbI0bqA3Qq33yEy7CDsAfXlhtI-9c5CUhz7DyYdowxnk2oC9MeMMBFMZ1KHaXphqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
تایید خبر اختصاصی‌پرشیانا بعنوان اولین رسانه؛ اولیه هدیه ارزشمند سعادتی به زنوزی؛ هادی حبیبی نژاد ستاره فصل گذشته چادرملو با عقد قرار دادی 2 ساله‌رسما به باشگاه تراکتور تبریز پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27064" target="_blank">📅 20:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27063">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktklcsVB-2FG8zVmQHliONH0zNvrY4b28Eqohg_AF0Wv7LwwQOhZw01djjsp1SmuW7h39zucMOJwqnMLmcXKrtIm_zTHj1ZiS4QQeqWSjjj40c3m9hnYcY6nmG7NmbEFuFkcF_HXjgavEtHqSLw1dZ38qQ9AT2EWej4i5DqIxvDnKahzjnPXs37QoEzVei-gG32x1w0_GIxk0K-k_bl47Pnyom79iTE12R4NPguHmfW0uGqQvEC8dqQllkX87knbGRZVfChHXqYPWyiS5GR7zBL5pOJkJ5y5AOOxGvikRruyz8GccHU-a-0dW6Ni1odMb1UzjcmYyIicPrVlkotGnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27063" target="_blank">📅 19:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27062">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab970d5a0.mp4?token=Owq3VYqmq2jkD_rlHZ5qB1OUcwhkuuXO5Zn82izGxb5IzXrQQzV0KygwbrauNi3uM74gxWNxuzWHn_r9bh3P7mLU-3s54yWcJo3ZZcwQXxAzQXO9GjoW4Z7ml_WPV6TJC6gQ6yXkWz44nEBlcXK4d0A5Yq0pMK9yTv9zKRM7ujvCwGBZa2jh93frewSi831bg_GmtoGhPYBj3VbjRlgP3nqzrKmxmqFoQ9JN2PTEUlvSwRjeS-guARhoLiO2k7ZQmTdVFgsvbdgBhaZyjC9kZ_PR7dr41sanARs3KycO8FTHJM09_rr0fjArTzAjjJLiGYhHhayZwyZ4oKrs5yz-dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab970d5a0.mp4?token=Owq3VYqmq2jkD_rlHZ5qB1OUcwhkuuXO5Zn82izGxb5IzXrQQzV0KygwbrauNi3uM74gxWNxuzWHn_r9bh3P7mLU-3s54yWcJo3ZZcwQXxAzQXO9GjoW4Z7ml_WPV6TJC6gQ6yXkWz44nEBlcXK4d0A5Yq0pMK9yTv9zKRM7ujvCwGBZa2jh93frewSi831bg_GmtoGhPYBj3VbjRlgP3nqzrKmxmqFoQ9JN2PTEUlvSwRjeS-guARhoLiO2k7ZQmTdVFgsvbdgBhaZyjC9kZ_PR7dr41sanARs3KycO8FTHJM09_rr0fjArTzAjjJLiGYhHhayZwyZ4oKrs5yz-dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ویدیو بازی‌بیلیارد تو اینستاگرام 224 میلیون ویو واقعی خورده بود که یه رکورد محسوب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27062" target="_blank">📅 19:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27061">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADP7TUjjd6w-HFwbg4tV5PbZdDwg9P71horn62HS3xTHNpD7xCKCcyc8UuHxjm7KTKu93CEMNHzl52oaNS_Yt-ImuVil2y6GwxGR9lLuMLBzUsWDZ3diR_HMCWGfNnLTJ7QxohDm8VI8VxG16agGcUE_Rm5mcdZtfS5NP1UJmg0CDsjkcMHpgxFbdSH3JccnaK1tfFqohcq_EgPDBmPX9CqiCl5Js-VcQnJgDaVJjG8ZjMIvIIlg4XfNPL1PQuL3MxsF-IRL3geP3eiSBJEKXQ-f1U7PDGcx0_XjD3F3fW6-wt1cKLbkMfcr64-fA4gVj-CAnMn7QNULQsOeGmeq1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27061" target="_blank">📅 18:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27060">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbjYDviHw5L8UAyCv-mmDzPfq2K6V5J4Wfbzw63Syz4CLg87PtclRI967Mg8d65_yERn_wDoI4FbG4G-1ZVHoCd3CEviFv9rB1T0i7fpi5ONWnvYU-zF1rtY7R3la-BgQ6kAKVF3Sh7R6bACM7udyj3kViNpVOO8KjpEhQ8V1EAbwpsa5ltgRVYcPPYCuOYCcTWZ_IDgnxrCrxP3hpTMs8DmyEl3RWusNhtqaC5WALVAzs2_Yaxs5WnyHZJgRbYM8CLyy2FKwiKAPb9VbRhZzCinsJbMEYBk7rYSW53lSXqCuLhB4RQ7bbivLE6EdNtoWbxXGWkPQhbgcnwYGWVpqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ نگاهی به کارنامه لیونل مسی در دوران حضورش در پاری سن ژرمن در تمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27060" target="_blank">📅 18:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27059">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzFcRRLZlPrsXbd8LD9LeKbTnKZnFDR8kdHBz5KoNrdx-2tDeckjXJEl1Al5c1djGcjb9GmVLa1_IMDqT8nREbPTWRq_ci1Stv_FmVgUxm4pw__8GguycWFhBsFcnhuH27j3mFnr4xgjAA051bnEQGbrfoKjiyMm4nVF9hQF_smofleoy4u9phhv1dtJl1ua0Xe8dDadhlFYDrGunQxdJxnNbyQ_Rk7f2YE4p5t3C8bbPIAp0zxO2uiGGFtUf4OX1zcmZmCVgRSgyELonAlvINh6W5HHCVV-iP8CwpTc2CKF4Xf112a9DU3tJkZKIBeRofkozQ2RaNKbWK_Bw8Co7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛بااعلام‌فیفا؛ دیدیه‌اندونگ هیچ مشکلی برای عقد قرار داد با تیم استقلال ندارد و این بازیکن بزودی قراردادش رو با آبی‌ها تمدید خواهد کرد و از هفته اول رقابت‌ها در خدمت این تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27059" target="_blank">📅 17:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27058">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGJNILdbQ6TFa1x8x2FeVgfS9fB3GJg96hR9Og1kJUcol728T5EzP9Mr03iIYOsVsoND4tNjZxoP5a3PABWlF6ycatZRk1A2yH8PryTORTc_v7oq2gEsxUR0gPWKdngGeuFvAukgqDGZHlxN8024s8B3wzmUeX5o7P2ebsZBE3NSIaTOVehHT12N1IKtmNiL1PanJIU5YwfBEihvTj60wngtkVhPr7In4IwjgFV9i5QVctVztF6A6-UMpoN20EriFSCYKVohmxIF04-6eoMbLsHm1-CJ5qciBTFDi5Y2RfVlif1gBQ_mXM7eJApGvpMV_R_9zKr2QEEKmLQzWCRH1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هانده ارچل: من از بین تیم های اروپایی طرفدار منچستریونایتد هستم. علاقه من به یونایتد به زمانی برمیگرده که کریس رونالدو در آن حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27058" target="_blank">📅 17:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27057">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUtr0ZoKEF0q15loBsD2k2ulux2WC_MKlPpukDabJp4Fw7ox_Ope5N5Upg5CbSSC4UxPhGv7-DLMp96A_20X1nQU8vYWaJUf4Atg391CMGu3V91AFeBDCEk2TmbjLG7QmKA7eV07VIRzquSCCnwJBCRkaBFrxR2yruKIhaK8R1yd2p7dbEGa03gS1q0O1JJ97E9bVXQtYGeD0Qp3ljkpsiK9CuQoLK3AP2y5qHX_i2xhnrgS517flaubk72NgSy8yzlh5r_NDk3YDl218hkstEXBHdRq56DLEuwtJiv4AcUfMKfXtifpxOE86CdMg-VE8hGsK7L2Q_Eg1gFedqhLvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27057" target="_blank">📅 16:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27056">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ny6qy7S6AdDuYQtOsCOz5BMmSiQNAYWmkznqa1bZWwDNXd4RMrMZMBFTj9bX1bWY3w5-015oNt84RENSJf_HeU-R6ljy4Jg-5iavWJOcIycFBeZfpvufyPF5JdAZJ8qZRh0iu23ioLtL1FLPqi0j-EKca2Y-5v47c9PNOmeoDwd7hN5cz84ibVHgQwcxPPiE0JXNp8axAe7u8XfC0LcLjwEIlssqZf89XfxzzuyVLEQEXwVnqDXKZNPYCP3SxgwwhXe1fspJnXv_vZVztq4Wxf3Z2Sf7WH7vFSTWnK2KmiBdpf2CqSQ_5BbYo9uEgAEWcaZMpXOdxlkh1sp29uTK7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ سید مهدی رحمتی سرمربی‌گلگهر ساعتی قبل در تماس با مهدی گودرزی شاگرد سابق خود در خیبر به او اعلام کرده که پنجره باشگاه استقلال باز نخواهد شد و قید عقد قرارداد با استقلال رو بزند و راهی تیم گل گهر شود.
‼️
رحمتی پیش‌تر نیز مانع حضور…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27056" target="_blank">📅 16:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27055">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Orp_O_5N8p-tie-YlZ8s7FZMmgyu98FdbvLdi7EcOpTXd_mRYeSrTXDc1y5FPYxCdoUcukmiuQO77VOeCPueVs95Vu-6hq1Ola91666n1-tWcJQjE2xIpTyTzxeflJhdEHUcPCfBFwsHad4Gl42jdG51K5rFWle6EoKbXjbOpcRCRJuA5g4Gq2jnKGhfihoH_gjSrHbPP0bGQmLIrrLeYpEbsB8JwuwVwb92746cj1uTejYjmxq_scqtiz88oUvcWPXz-nWlr41d2Z_322az0tAn4zFT9V47ZBmTzsHeTbwgWA2gxhFllOPCF-yvJs9wboYADBOVVDdbdwdnAfy9ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔴
یکی‌ازمسئولان‌باشگاه‌ملوان‌انزلی در گفتگو با پرشیانا مذاکرات و توافق باباشگاه پرسپولیس بر سر انتقال فرهان جعفری به این تیم رو تایید کرد و گفت تنها مانع این انتقال مدت باقی مانده خدمت سربازی اوست. درصورتی که فرهان جعفری بتواند کسری از خدمت بگیرد این انتقال…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27055" target="_blank">📅 15:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27054">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2279080601.mp4?token=T5JCs1RPr8OePwPyXKokb3sIdQ_OreeSE3lBPIGZUTAAWLMn_OYFfRNkdV0SOCziRW80xGNgltqRIopodLurc1fdsB0cSdNVsdw8AwFR4f_KGjdWLN1_-VP9tsTaBWGU9uaItFE_-E5kP1KH4kEbj4p8KjeQFiY1jMjuLva7geGgV3UYhN2wqzf5x5E91S-7v4uRu_dSNUQiTsJ4NhBnPzZ7Gub-Z_PWmDCjG4CqvPWh1YO9oaxgrrQkNVgK1rqcd-NDOT4eKP2Tdy6B_dl34sS8S8FwZqZsl-lpmuUh5o32C5hz5c9FqWN6L_11BpT5iSvuanxA3tKBJ78hAYTZkzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2279080601.mp4?token=T5JCs1RPr8OePwPyXKokb3sIdQ_OreeSE3lBPIGZUTAAWLMn_OYFfRNkdV0SOCziRW80xGNgltqRIopodLurc1fdsB0cSdNVsdw8AwFR4f_KGjdWLN1_-VP9tsTaBWGU9uaItFE_-E5kP1KH4kEbj4p8KjeQFiY1jMjuLva7geGgV3UYhN2wqzf5x5E91S-7v4uRu_dSNUQiTsJ4NhBnPzZ7Gub-Z_PWmDCjG4CqvPWh1YO9oaxgrrQkNVgK1rqcd-NDOT4eKP2Tdy6B_dl34sS8S8FwZqZsl-lpmuUh5o32C5hz5c9FqWN6L_11BpT5iSvuanxA3tKBJ78hAYTZkzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقادحديث‌میرامینی‌ازشرایط‌سخت‌اقتصادی:
یه‌جوون‌چقدر باید کار کنه تا بتونه یه ماشین بخره؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27054" target="_blank">📅 15:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27053">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4lCOxtF4OnIk_VLeccc5hBrCLpNDHKlSqBBJg92kJeoPsXVhUS-IJmtEW9wcHVnj872JU_xPiPlvHsUUk_Tqj_5n2aX2sWvmwGE6hGb1AGpXH2lhgBUS9qyHkeekiyPNsAwrP92g7yQjHwnTKITNYMeq9TG9livRbSJe3Xk4PX8FT4QFjM2rPX5yybnzDi9JbpTcFfakz-c4DWNnLppN_dVpf1e6TVhtfQj4fvIRVqciv-cH_dZpF_LjqQHm6nb3HoBwiTwpv3vJ1n77_ywA5ZTqetYrrZDUvPsc4gGe3yzn0McnX1W8YXWebE_DX_srL-Ur7k04UhxPWGaWWkbyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27053" target="_blank">📅 14:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27052">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUJYe1_iGZkDaFrJ-3H4cKcPiz6diqmwaPWptH8uVScn-qjjzsx63BfjDOVI-7CPxDg8jwk_nAOGG3sScu-DmMSArcN_KcmIkyrOC7ihM5NlW4K6urNJbM5fvTqXcNU-K7ZcKIYHT0jonEryto2l4Yf6O-ci8iDMgr9P73xiM5xHJZN3eAQ_q-6Myc66SngLdUFcd9cIgKAp3MszSoXz_HtJ09CgKCaqMNQrzEHNnz7pZa1GqagHyYEyJ8RFdXUcpNm1OEQTtNvb-nWIFzthY6jage3tprPJO4S4wdhjfX-RCK-0YjKQOaqUgsGQ8t3C_cQzPV7TIehaH3pItka5zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
احمد گوهری دروازه‌بان‌سابق‌پرسپولیس‌با باشگاه صنعت نفت آبادان به توافق نهایی رسیده و بزودی با عقد قراردادی یک ساله راهی این تیم میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27052" target="_blank">📅 14:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27051">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFgvZWfgRA0WPjMbU-Q571YAZQPJvjawWQSeEyFo3dAkP9AAWuvtvpst5nrIiwr8AsGjbAWZ33p38nVzQ8WtwX0QYlWLugQ8rjrHB3zbzwH7v39nAvi13u66fIE-P_4QDQYkIKP5VLpFj0wc4y0Gc-LMycGvcBz_NffmcDMNj-DXhV0QK7coZwzqsP-9sy1TJg-KcGJ5FfF0g8Vo5Tcd1t4HdX1tQd1FXkzajV4Y72cjI4y7L5ZIiTc0EE0tgR6krxTWm2Q3_4j6pt3W4hZ0_3RprRXyj5huYyIYTerN_TlzimYNq6M-M1H0rzbLj1XgdeNiCPt8qR0AsNkXTXgNIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌_پرشیانا؛ آفر جدید استقلال به رامین رضاییان برای یک فصل حضور در این‌تیم 150 میلیاردتومان + 50 میلیاردتومان آپشن گل و پاس گل و قهرمانیه. رضاییان قراره ظرف 48 ساعت آینده پاسخ نهایی خود را به این آفر بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27051" target="_blank">📅 14:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27050">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prHHxELUmSaqkbsgEgP9zVS2wNjZKbIwt5ZRl4heh28JqPo1ruOROjY0qIA0jXBAhbVquMFTqhzM79LyYSVx5BJOO7VcLNXo_YSctkG8uBH3V3sV-Q0dKyfLeVIhivC5qbczae2p1cUlBXFkPc5zEblC4U_uCbA5ksz0CyzYXraqvvaoQ7dFpRWhOYjYD1SLr4-kf3cE6WlVtuRG8nVmxFu7p-ao_5NlZkB28eKLVceHX3Asb9X3NXEPBBa2Qr2smSOShaRTBarvj2iHQ_mcRpUTDR94-5FNek4ETH42Lc-qjUkikhEq-GnKgwijCXd0C7GKf1xZIAd84ABkFSiDZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ جلسه پیمان حدادی با مدیریت فولاد خوزستان به صورت ویدیو کال و حوالی ظهر برگزار خواهد شد. حدادی امشب به تارتار قول داده تا پایان هفته پرونده‌نقل‌وانتقالات‌رو با جذب 3 بازیکن ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/27050" target="_blank">📅 13:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27049">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dac122529.mp4?token=V30TSmidXx0tBxH1tD9ONR5nOFrq4Os5bZjPFpVzHtJQmBUrkUDZ_utNDLBouY2H1yorMi5Ia3uelpNS8EVWtV-aH2lxd6ATo2ray8rNCRGn-4sjta7Fxy85x3leguxl-prEC6nkWzTDR4HKwpVQoy658tQuiVY1u6nk3eSAIJy2TkegUKW_qC4Jtl578XIhyAi8xxaLOm9rdIO1hqrkGqRcxu42f_2PhCcVQUcwsOG3w99IdVkp2u1DEh4w7FiPQaADW2aHvA7ttxVr8i1Up4QyxKtytghrOcmfL5BpniajEpvBTKzt-yRKERpwK_gOpzgSMk-0SaRY_wLPnOUK3GH9CRoXQxnSFUjWhCWyp6h_w4puHL4Z1Unuhg_7z3BtxBjWv0HSeDj7LxDmeWHdgUozwVcVelh7xol1XOWT2ngdh9MzlsMEW-fUadEVOoB1zfYeAsiYU4wFPP97J7ou_76jieNdTgynSgeKpL2FQlFI1CE5f-Y26QVCOmKhSX-hPCJmLw_gaGD270kWHly5Q02i3nBczVpFpSxbIUXkIW4_cvT3MWfO6d36EblFmCrNTVZ2Z6-E8hYHuD2tllp2F-HPYZVve37V60LEyNV3tKTmTat_g-M7-zVW3qUPBmkLewzsiSmmFwBO63P6_O7Bg9VVeSNZHrW_gjQ5xgm7Edo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dac122529.mp4?token=V30TSmidXx0tBxH1tD9ONR5nOFrq4Os5bZjPFpVzHtJQmBUrkUDZ_utNDLBouY2H1yorMi5Ia3uelpNS8EVWtV-aH2lxd6ATo2ray8rNCRGn-4sjta7Fxy85x3leguxl-prEC6nkWzTDR4HKwpVQoy658tQuiVY1u6nk3eSAIJy2TkegUKW_qC4Jtl578XIhyAi8xxaLOm9rdIO1hqrkGqRcxu42f_2PhCcVQUcwsOG3w99IdVkp2u1DEh4w7FiPQaADW2aHvA7ttxVr8i1Up4QyxKtytghrOcmfL5BpniajEpvBTKzt-yRKERpwK_gOpzgSMk-0SaRY_wLPnOUK3GH9CRoXQxnSFUjWhCWyp6h_w4puHL4Z1Unuhg_7z3BtxBjWv0HSeDj7LxDmeWHdgUozwVcVelh7xol1XOWT2ngdh9MzlsMEW-fUadEVOoB1zfYeAsiYU4wFPP97J7ou_76jieNdTgynSgeKpL2FQlFI1CE5f-Y26QVCOmKhSX-hPCJmLw_gaGD270kWHly5Q02i3nBczVpFpSxbIUXkIW4_cvT3MWfO6d36EblFmCrNTVZ2Z6-E8hYHuD2tllp2F-HPYZVve37V60LEyNV3tKTmTat_g-M7-zVW3qUPBmkLewzsiSmmFwBO63P6_O7Bg9VVeSNZHrW_gjQ5xgm7Edo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇧🇷
#تقویم؛ 9 سال پیش در چنین روزی؛ PSG نیمار را با مبلغ 222 میلیون یورو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27049" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27048">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxURmzCteKJPyWEwRBQvUDD1EkOi6aDM8zJCqssDQ_6mlfDWW_L8L2Jvc8dWLabYsrAubH8PZlwmBqMcnKNIU0O8kR4ythJw9hBjB2JvT7AJcRu0u1_bvoD2OXDhNzxXXJ78BLUl1oDNc6vh8yJIvEW7nlazIQUImIbcBoSmJgKWD46tetdtFq57RDXYz_MK4cJhhWl0cHnpzqf18CBVhs7MSiHClTBXO8BWT2n1CCzbCmdPtUH2vdx4WpYfVfprl1ebEq94LJeFPbgZvfhvzGgbjcEsFAOHzBl0YDFwSIvMwWucU2CuUI9L9DVHCZ8Gsqy0IOp8eQ7FqjURqwv54Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باارزش‌ترین بازیکنان بر اساس سال تولد از سال 1985 تا سال 2008 با نظر سایت ترنسفرمارکت
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27048" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27046">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qrah5lEm7aT22nUq0eCWKHLUKjkwUibF6l6HtO-RrCF_SvCXMSYmN0LJv7K3ay2zEkAVjp0dxeJ535NlQg4UqCuvLCpi1K7pyVVLiUDGlI_TjWWXWwnX1rBPacvPEHlz7OmC8TSIy7SOjjvECRh3VjmVYqXQyxscdosFb0MszDonIO3KMVcdWyG3jQorhhfzlJwtB1E_cN9DtQl20wY30Er9J6gowKJOj4UspC9_I9EbJmBoc18PfaOSduJMhb1r2e8u06Y2_qXDdBgha0B7CcoeMwP45ZJMSt8sQqhpo2Ubsw8VeQBJVf-xme07XDoU2T06VUbxFcNyeiyzAAAcjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛دیدیه اندونگ بزودی با حضور درساختمان باشگاه استقلال قرار داد جدید خود را به‌مدت دوفصل امضا خواهد کرد. تمام توافقات لازم بین اندونگ و باشگاه انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27046" target="_blank">📅 12:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27045">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1LOdxeTB9IjGp6ZdjjsizRANcDItaNzb27MydQ4o5TxAqEpluAmP5C2TQMO8sHdfxaTEvgsMur7IEY1L5nhpLZQhHuoRh4SOKEcZhoR2woK2esgkU7Hzk0dAHChBrIyRLepcQ0vpZLpEZj-r9sEbWtszQEAMyfFDc5n5_Np8LfGfz_sw-nImcPQB4HvF_zPjCBRsAnu3vkAEkAudK8lxWRsc30hvsn_dEDtMZ6kAnQsjwzCLyuEssjAs-b4xgWn04G_xdszzetrbmSuzyAOj_8pl2kiGmOdqiKrOIc9UXam4boRaH6k-uEQ6hNRQg3D20zQg9PTTXgWisXf3gobJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات مطرح شده؛ فسخ قرارداد یاسر آسانی با باشگاه استقلال در فیفا و سازمان لیگ ثبت نشده است و درواقع‌فسخ او یک‌نوتیس ساده به باشگاه استقلال بوده و با بازگشت‌ او به‌جمع‌آبی‌ها او هیییچ مشکلی برای همراهی تیمش از ابتدای شروع فصل جدید رقابت های لیگ برتر…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27045" target="_blank">📅 12:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27044">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7821302722.mp4?token=apKfcG3RUbXfgsw8flhAxaZMzGUzCNDTBMmQYplVJqQc1pf89rixFm5qDuIVl9CJoFYwCiVI8CM_DSIwGqzjL8ll3vZYg6JCZwrDJmhG2RuwCcIzHRPzprrHcFNncn-3lhUPQFg9tpeeNMgn1ZwGH0nx0UvMg6Lbir2UdQ6c4fh0s0_xiZNJbfFkpalAFzbPwlB6Uxea3-9pheJoq6iL7W6ckRd0NEWtaVMLJRJQ5d2_JL5MrbNY4ZYgqM4BqQrk_N3es1rtqfVozGCjutVSzxfICU62mPXH7FxlmgcOjtughRbQmtG_J8ayD1HU_fv1dM6dC2gzXQ8nhlwvEgHHFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7821302722.mp4?token=apKfcG3RUbXfgsw8flhAxaZMzGUzCNDTBMmQYplVJqQc1pf89rixFm5qDuIVl9CJoFYwCiVI8CM_DSIwGqzjL8ll3vZYg6JCZwrDJmhG2RuwCcIzHRPzprrHcFNncn-3lhUPQFg9tpeeNMgn1ZwGH0nx0UvMg6Lbir2UdQ6c4fh0s0_xiZNJbfFkpalAFzbPwlB6Uxea3-9pheJoq6iL7W6ckRd0NEWtaVMLJRJQ5d2_JL5MrbNY4ZYgqM4BqQrk_N3es1rtqfVozGCjutVSzxfICU62mPXH7FxlmgcOjtughRbQmtG_J8ayD1HU_fv1dM6dC2gzXQ8nhlwvEgHHFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
ویدیویی‌خاطره‌انگیز از شوتای‌ فوق‌سنگین و برگ ریزون کریس‌رونالدو در دوران‌حضور در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27044" target="_blank">📅 12:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27043">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1CGdP45eSKfYoRgwaGTSVGb4pEc-TJvFwzkFTVe_zIm-ySFOAMOA-nUKzONlWHLwNgxNRJ1P7RDDa1Tukeqt1g4In3GxMZWKHvm898qsnqBgj1bfBKc10GmTNPH0G8pDma9lO-JPAQnzAsGABPqAgy2cvjB68I3p20yDqqFoT-9XRunGTXdVfgRC5r9ZBnz7QrW3sxJj1ZiadNFG5XszwYr4_pUrPLjNMpJCFW-C3axYGJv2BvyJsnWfILTvTAKBqQgMoYob3KNhu18S4k1sIUyvelVZ_mThM-R9D88_M9WxFCfmdo0WiDUdE0IbJqRreKxSBST_XCGuSiZH2JwPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ویدیویی‌از تکنیک ناب‌وفوق‌العاده تماشایی نیمار جونیور در دوران حضورش در بارسلونا؛ حیف صد و حیف که به اون چیزی که لایقش بود نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27043" target="_blank">📅 12:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27042">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cu1YgKe6oCLQjifrSsCUTjyu76S6YVSjEMdcKl613xh3KDNCSvVejjc3vzUXy8zVvsHyqgGjgKXwK11yOlSko8Ok2AFQAmktVW4ScmJqbSH0Bg6s7F1v0RMYeKIUnv-9lSZe3nvyHxhuSi2C8P6Oi3BA8Iu2B4qzyrMYAgonokzcLWsInhjH3O2zixrieWLmCZl5kv3Y35VGCA4eTWS2s_g-WkhFyp2X9iYPy5B9kCs6wDYXPWy3zrKSDPJVtK3PUBhGrwhS6AqnChjPCuW879R-FBkB0iPzi_GW3IX1zcnwddBcgSEsb1aiThdUKUl50BAl_Ohasf0mFtJyFpfkxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
💰
#تکمیلی؛ بعداز موافقت مهدی گودرزی با درخواست سیدمهدی رحمتی برای پیوستن به گل گهر سیرجان؛ مدیریت این باشگاه 80 میلیارد تومان بابت رضایت نامه گودرزی به تیم خیبر خرم آباد پرداخت خواهد کرد و بزودی این انتقال رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27042" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27041">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAzqCmH0TDqxFfvbmYR0cnXZ8BWzKJOyCTsC5L-KbaJeIPb7D6shGAEmkHDkzram8d1BHmXEDYbFnhPgbAbIAf87NykAUKog3dp25_ncKJ7LKBvuubQgF_BYGDI0MEo4nMnB9wpLyvQDOKAodUeh4UpHr6SaGj1g7YhljkGlBwoed-qlT3aKour7R8rgy-yo26lKfbJmLa-61qTVxgnykb_LvtiFnE5aosW4EIg4hk3uKJZlFYy5hPgSgpg0E-qVWHAroHf2IEgSW_P0aKsGSyAnQaX5trVrZzN7vMmjBN1eYAsk1JZRMxpGSarr5F0GaLJ6KsWch4IekgKliqeiWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت‌هایی که توی ۲۰۲۶ درآمدشون میترکونه!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27041" target="_blank">📅 11:02 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
