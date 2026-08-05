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
<p>@persiana_Soccer • 👥 627K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 13:56:31</div>
<hr>

<div class="tg-post" id="msg-27142">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‼️
اولش یه لحظه فکر کردم وحید امیری رو برده اون بالا؛ لامصب ته چهرش کپی وحید امیریه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/27142" target="_blank">📅 13:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27141">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/27141" target="_blank">📅 13:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27140">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇪🇸
🇨🇮
ویدیویی‌جالب‌ازگذشته سخت و درد ناک یان دیومانده ستاره 19 ساله و جدید باشگاه رئال‌مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/27140" target="_blank">📅 12:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27139">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXhh0NsmzPzccmpV-leHQq2qC7Y5WfuCoaSVvLN7Hk_ZuQfN_NjtKyhhTtXNC69svZaV57hx2GcMKvPu0KpRyQj1FT1IiOiMLd5Wy4NNyUpY5ue6HUjtw1NLmLMb7F7mFl37sJ7klX366bXgF5DcUfriaJflTvAgxOqxmVo8Hp6zxHIV5eJmkuTipOqDTL9Y4_n1yX9OKguaQh_mve9v2hSzHlBUmg3kos1kaC33NuvPSFLZOYaNrGqRkaorAKOoRzkR2F4e8ZDaHW-qdGE4u8svdqn18UW0t9oTlVoTqR76zR1TRqCBhFUZKigu1-9gESRuFmY9Kh5Yl72zRgk9rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات|فابریزیو رومانو: با صلاح دید کادرفنی رئال مادرید؛ فرانکو ماسانتوئونو ستاره آرژانتینی رئالی‌ها در ژانویه قرضی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/27139" target="_blank">📅 12:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27138">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdeHYrKnzInEWhihwZverOcS1O5LXPfa9t5nXu6f7Li3mj96mGaGX9gSRCqXgk7qi0i4iWdf0kc7tZlij_5ueWKNEwFLYXe5nQWUHGDvLPPixejI3t_ObjpMSwc4W_2uCt5tDZVaPRzj48culMrbr_UKlOOOop2UDhnamC05-Bvf_yKvIRnheX07y7oQEIpwTxxzL8U8sJrZy8CJfaKDxpBKpxU9BYT_xMQvsHAuW-5rf29SEzF1ZGtshkqUVBOHW1gjcB8lbYhaVSyvKZkO6LIP_ENkerqTgtP0t0zWsD3AetQQnhIJaCNV0m0GP0YTb1pPdUiRhu9eJTqdFCfBAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/27138" target="_blank">📅 12:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27137">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNWWy0SATzYBYexkkdcuLGeC7jtm2eC2Ai8US4pKIJKu_p_JFxgkmWcREXPWSRzS3QOZhnZRdkGBJ73ZqhbazhhK1wCYWVnQGToVVgBsOanBjyb_IXyMble1BF9bSOExSyC1jlLdS-gO7FluwpERiY4kGd3CL6nenKpwXqCgQF2hMBKumq-5BRbKGDPqy8bYQzbKl6Crj1cbqJwMD3KmOLdEV6pNR9hhToxjem-BG1TEb-6B-Yv3CfQKfFRXNjY4M5Yw3JpOLYOkXU3WmAc22pjtABbdHDE8YOTrzF18YPE_eDrfX93GUG4HtfZqaz8MwW2caGA9y_tYcb5NXGJ1CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/27137" target="_blank">📅 11:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27136">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/27136" target="_blank">📅 11:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27135">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/27135" target="_blank">📅 11:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27134">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyWNoL-SDPM3IVNXaSstWde_17KRfM3YYNXL4Yzuh9OJtcu6hS2ELmVOhjt2qaInaDJQrlmxdAvJNuOHYKPV_mW1Tu1y9t6rJTK4PMYbmX00GC4QXN1hensvS793_85099gfQ6P0KgsuyxsCaXdS_XIlYOdcyjNfYEMLQt8JwTpsdeNTfVnYMfbQGWLs2k38bv0iAuNBpiUs6zFoPWQFZSPluydpGzirwuHEf8YIYbMEgMJs8VbLxqrML7PwwfsbI1MvIArPoNh716O9h4C39UBK0t3ZLU0AwS_JV-w1fxweYvqt0pGsfaq175Z3nCLomYlYEC3mUxXApEk9q-umkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
🔴
🇧🇷
باشگاه نیوکاسل پیوستن برونو گیمارش ستاره برزیلی خود به آرسنال در ازای دریافت 93 میلیون یورو ناقابل از توپچی ها رو تایید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/27134" target="_blank">📅 10:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27133">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/27133" target="_blank">📅 10:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27132">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pn-IJyYqSHieUiomEMsYNbXYs9H3t2tjrcLZzg3CQ_ewKyDgcHkore_hxLR1HN2z23ikNyxufgeQmtSDij5uUoBRyD9knS49VBnnShQrNDLPDp0pzK-qLObVNkSObEC1-1OAaqpZGRBJKc5f14SB_T12Kz1OS3evwpDVAmhB1zBzcUSi8-bk2b1ahdhCitoKqTRcPhO58-uU2zgSNiEmM2_-DZxm08rzMgwjBI_o6HWmKAp_18OfKbLD9UHtZCVtvQeSQYU2iDYl42THyf2w1iJjE-r2MGDKp4xaRnBaqS8z2PGsZ2ynYjuYR0HIyC5ZLO2mQFjGaH1z_1gB2LkyKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🤩
با اعلام جرارد رومرو؛ دکو مدیرورزشی بارسلونا هم‌اکنون‌درمادرید بسر میبره و قصد داره که فردا بامدیربرنامه‌های‌ خولیان‌آلوارز جلسه مهمی بزاره تاراهی‌برای پیوستن‌این‌بازیکن به بارسا پیدا کنند. چند روز پیش مدیران باشگاه اتلتیکو گفتن آلوارز خودش رو هم بکشه…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/27132" target="_blank">📅 10:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27131">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmDykLp6j8KiAm8fnV2XoUKxRWi-llUV4_lvPMyFrwjPxYJcIOgYTTDVG_G9bkQ3nAGaZmp7FX2otNbsBujm0MMd8rxZLA3mczACM6kPqUyP3B5dsYHelcGquGZ63deR9afFenMXs2PnFN3IejsePtezuVtdRYDSs-gGo9YaargsfAaX71ZjnmeehcFj8G4hpX2rrZncvv-i7f5h_pihUvZZz0lhypdta67SELA7q3-G8rridwYdEPa_YdilBhTK3ByfnvLLBE5tKr_PGZedou88oeEICkwvJWCIn77A03M8EAb6LfglW4O7vQqtOtEP1dThas77PYBX0EGQkBU8vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/27131" target="_blank">📅 10:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27130">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7ky3MnN16YfvEYwMV67zXITc0tkBtoGTHMDWvMLr5DQ-RbIjbHwo9n1p_UkVmXk6If4ojOA7GeuHMgrsajjtj5r7HszA0stC4lhDA5r1m7_Wlzqv1XeuaX4XLwe0wxyWpbwGH-SatELoo_UQTqZ5lLDusVzvgvQCoGlfOiCExRdtm7kCz6Mtsq2bj8KXfGYY9iVRzt7R93qkp8hX03jTSdGPL8IkQY0lfmOO7TGnznDPPkif7hHu50kIISxU-GxUCO3_YxRZM9sg9EKEN8GRm_0vkIQhQoeS8UIRRtUzO0_VUtVojcng095rJFXjTY9UV4w3jRvr1fcILm94m7g0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
درحالی‌تموم‌اخبار این روزهای نقل و انتقالات شده انتقال وینیسیوس به آرسنال؛ ستاره برزیلی رئال مادرید بی توجه به این اخبار با دوست دخترش در تعطیلات به سر میبرد و در حال عشق و حاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/27130" target="_blank">📅 02:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27129">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVrL2ZVHZdjWtce5zjjZEFDHo7RBwsTKHmuSghvyMmXA3-3bQIprdSPMqE49o6pdjBBc3E2o8CgU39zgft9EDxUzYLRjLD5FhQnTfTxd0LheDxTXpoarYSgLfk1Lck9ZVpkZDBOP5tp56pgnMM1yH1l5TWVNxIzJDLRiUuysTzf-HZQYsJmrZT9ilH-f2yVG1BS2QVztH8UxEYSV5g0qw68yVGmT8oyBMZMrARj7BUAne-aLgpvCH6aFb1Hyny8K9N5h9-KpCmhqmjuBioJ4WUGduz7gqncA_hiQgiS7m9PS6CN1rzG_GEevAucyqvzVINv8NrhsbsWJLiEO14gRGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بهترین‌و‌باکیفیت ترین ابزارهای هوش مصنوعی که از همه آن‌ها رایگان میشه استفاده کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/27129" target="_blank">📅 01:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27127">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnHb91UhO4uAYUrEC3XHp-156xTpKIPsITwEzJvAFP6VpGDrF8lv6veEASWVchPoYbvKvxpPDZZmhHoLznFlIDwyVBMWYbQl1qEtbvi1Z-NvM0_jFOiqBui9hKA9e5Ba9Ce0u900vA1ArwumthEoWsDwDeQxHzJFpC0vSytJJNtkU-79PtdUIdHJipcjTMGE3E00Vge3xuGqLzr1OCYqDqdLMWwuWqcBdQ4Rz4oDw1I_3Z9DQ9VdjMRDH4ToevUNAxif4uJnlPq3Z6c44ZTlVUF9x1JQGs-FD0rG8v5q0yrO9MI-1Dmpk9ZfqBDElg1cR4eqAvtKUUhUKXLOleOsXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
ازدربی‌دوستانه دلامادونینا تا دوئل شاگردان ژابی و اسپالتی در کشور هنگ کنگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/27127" target="_blank">📅 01:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27126">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfiPNVkQ6cn_Nqu90YM9A6cNW_cCqfSipXNFgquHphgb5BfnvKWtU0obNBLIvvG2xc5L4X-5K2fGfg7DdJ29YtNFNbCHX-f1R3kUrbHj3CFPPwMEx0Xc1C7_5aNGLC71kIMzkvAhz01o4ixSvBsMmRywNHFIMnt2yp4dcAiortv-sj9UYZQD0LUfn_o8uIfGsT-p14ajsMXvhdbFR7SIy2vu_26B94eu5Lp7VDgIG7XipGMWtqwf8XNvDLB_WNhei7eyDd47ayPTAgchvjxVaTJtvfF-GcNc606GgLkMr8SmpFIaIWaituRC2irpw9AXHNQ6VkSOxUDGUTxlM584CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
از باخت ماخاچ‌ قلعه با حسین‌ نژاد تا برتری بایرن و رم در بازی‌های دوستانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/27126" target="_blank">📅 01:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27124">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1X_JJEipGV5I_k4zJT99ZBtsMCsDUjgfgvkBC_TVhvekglmbehdrCK2FNbj6mD0tZyr-CyUbH3B9r4ccDIhjTcwyW7deFH6ptsIeEA56SP6rBnQvpEPkslvhBpEvb440yM8DoAxBYymXc07SownFjQrDFtckZFMyJlWXmKWA61vrDkfCYnb0LwFyYhi867Yy4g5fNYoepEjaFGA4U6CcIg_vw22SSJJ53PBJz8XDyV7GduvIlgZ7BAXRDrrPHTgmkJX6xyd7_v3H5i8TZSollYAVwenEty48fFDtXyWVFXLIphTP3eWqzoC9HruV6Pwa4KAYfsn5N0aCAIgXBNOFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تموم‌ شد؛ صلاح رفت سوپرلیگ ترکیه! با اعلام فابریزیو رومانو؛ محمد صلاح فوق‌ستاره مصری 34 ساله سابق لیورپول به ترابزون اسپور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/27124" target="_blank">📅 01:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27123">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjvSYGksE8eLNsCszDCJdUSLXrsw1r8knbFNYHHNRRc9KgRVsDw2aSRjRNQsaEwmWqyt52hl5Jm-VDyZf7mlVEYbJf9g95VpiWx8saIme1T-fq8BKHiXvBkjvSVlDuk38SSyqbuqJWd6SYxwENbEg0ibEqwkEJxfF4Z02JXEgydhDNuyumNT8kolG4Wz6IjnM8OIrxhWDF3Fn_qS9gzuhK_pg10-jMrJ8vw7GBNsoixGZQHttulWn_qHfZSiUB5NgtfoCdE1K1756nKaa8ZQMVJXqVF_nLDlhIzo2lBV48K4RpC15hYe7kAqI9rhntikadauvFPONS6B3wfx_179Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال: مسی؟ فوق‌العاده‌ست. من به نصف دستاورد هایی که او رسیده بتونم برسم بسمه. یامال برای رسیدن به نصف دستاوردهایِ لئو‌ مسی فقط به 455 گل، 205 پاس‌گل،660 تاثیر مستقیم روی گل، 22 جام، 4 توپ طلا، 3 کفش طلا، 4 پیچپیچی، 6 قهرمانی لیگ، 2 لیگ‌قهرمانان،1…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/27123" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27122">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9Px2pTfHuSEjQ3yW49ToX5BpYq1i7SArOJfRSQ7GcLM9IEZy5pO0ckAe3nBcOZjuqSP5uqKSdyi6jCPnQRHohHTsDJso8yvqVBrT8hTq6pHVWfMyBG_vD3Z7UyIcNlCNGbLK4aBbq2URZUTEFmgcrvCCRWJxmsYJ0PXWRw6zlXUJ-1de05axC2sBSaZLkVhXYm7P3UbjUz11AMluokcywrCdErIUhIYO_hwo92G7G6XnduPqBJubYio76jDuQCVGxgGI1m_tScK99oUeF2gBcNpzemRIBzSb5LKma1cx88MBqnSi3BB2AuyxKA-1jTXAfCNBZ5LhfSCYf04CUeEYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سعیدفتاحی معاون‌ورزشی‌باشگاه استقلال: قرار شده بود امروز عصر آقای رامین رضاییان همراه‌ با مدیر برنامه‌هایش به ساختمان باشگاه مراجعه کنند تا ‌اقدامات مربوط به بازگشت او به این تیم رو انجام بدهیم اما برخلاف قولی که داده بودند عمل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/27122" target="_blank">📅 00:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27121">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c01adXPElgswivrea1atQ8Jgvpu7GfRC_3GZ8HmdY4N0TnruDSfvQflb3zYhtJFOudhpXqTAENP2iqNq6fUnXDOKGRw9z3T6wmjdslhrj57WTqslVN3tzHTdBoC5Ie27noTSWtT5zys5M1uTQa7XTLEqnEbzoML8TZ6ngUqAq7oL4PhIEOWa5_kl9IdMSyCVdkp5bQTD1E0bRdiEVkP71VlgfrmUPp7uUi9Km7NIZtniZMxjajgtmhkOUEpSQ-qzze23i6iFUkbLuRLOHzyeoJk1lwdDofAVhJJ0w_cR5OqWeOaqGs6IrmbmUAFSsk2Bcko76MJxRhYzMkGbZ0Hv8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
طبق‌اعلام‌رسانه‌های ترکیه‌ای، محمد صلاح فردا ساعت 12 ظهر به‌استانبول خواهد رسید تا کار های نهایی برای عقد قرارداد نهایی با ترابزون‌اسپور انجام شود. ازطرفی‌هم رسانه های عربستانی میگن الاتحاد میخواد بارقم بالاتری هایجک کنه صلاح رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/27121" target="_blank">📅 00:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27120">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cu57dAGB7x7AARZXE_ePRBDSbGS_PYFJhs1_P8YrBRhvC-FrZ24cWYLQjGa93MFIrluHHAS32D72Pfc8dLkDEWAgG_Ujk_pSmvBamT4yHo7o_MrYovGFpTyRb1lw6CxtaYklfJkkr9nLNrgwk-Kzlx1erjgT9BPb8w4PWbguQq88SaD_iCaqsHztHSLQRr3-6Ye_ffyv949HHS_0tp1q4iwqwwwzEv9Zmu_9EUv_zLUTkNOLfx_uJRpelwKDnA87rfSNNagFKhGa-ihtqEapI_b8baNSDU2CgRqVE6CPAlnIg4WZOOya6u--Hj54CpEc6-Rkq5vP5lSiUqUwGfNzxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال:
مسی؟ فوق‌العاده‌ست. من به نصف دستاورد هایی که او رسیده بتونم برسم بسمه. یامال برای رسیدن به نصف دستاوردهایِ لئو‌ مسی فقط به 455 گل، 205 پاس‌گل،660 تاثیر مستقیم روی گل، 22 جام، 4 توپ طلا، 3 کفش طلا، 4 پیچپیچی، 6 قهرمانی لیگ، 2 لیگ‌قهرمانان،1 لاریوس نیاز داره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/27120" target="_blank">📅 00:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27118">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/27118" target="_blank">📅 23:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27117">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBk-DGzMHI1C3v6qzozIqC6zcMlfw-_VcQ4vfTSr4NR-4h91M8Od_zdBmYQ2jjwZvLm2EVdTDy22siyZAPck2xtNR_ZWAm1VlFizwQBTIiM6P7Wt3C6lafJDxLfvT5hWp77WqoXmFGJKCrSrDbOo19NP3zEJ9PdkFV8EK3pVTtM5aEh3e2LUu61gdkKdM9eP6SpUCIvCdXgi_y2_5IR6Lk4myjE9iVIWoBwaWFs9gYkeWj9RvHyMw1zapOq83nl2Tx25kSoPraaAmCHWAV4uxGJdsduCWh-ZK2zlHV8m0hLexYp4EpKuomGgb2i4lkaxFKcnEPRTuL_vIUTxsE9DGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
رئیس باشگاه اتلتیکو مادرید به زبان عامیانه گفته؛ خولیان آلوارز خودشم‌بکشه نمیزاریم از اتلتیکو جدا بشه. 100 میلیون یورو که هیچی 200 میلیون یورو هم بارسا بهمون بده آلوارز رو بهشون نمیدیم. مصاحبه های آلوارز اهمیت نداره. او موندنیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27117" target="_blank">📅 23:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27116">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAbD3C145jxhbnWFCJmbqcOQ_tdXfrF1UK4aN48q6DCP-Ot1HWpT4glmz000nrVRaNU-q-b4311BCy-NWHNfKAkuzzhE3D_rrjlXzGkRuyPNWOm7uweoYzCHh3pAg9-j3qGhJyNG4P0H0rk0H1boaphGnnVSeiSis2C7egV2ma_pjgGQeOT8b928FyCJ2WvWqcmAudbQZVs1mr4JjlEm8LgjAS9T_NfoRjbX7GJW6HSAMQuFPtowEGeaV-qCu2MtrXz_QrSA2BZ2rDLRZzmfoqDuHZ_UlF6WFWMyS27t3LhAWY2-Aoi7RCyiLazsJQzEQ4WhCfSTn_Yr5x5XgpFC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ مدیربرنامه‌ های رامین رضاییان امروز با مدیریت باشگاه استقلال مذاکرات مثبتی بر سر رقم قرارداد این بازیکن داشته و قرارشده‌ که رامین رضاییان عصر امروز برای انجام مذاکرات نهایی و عقدقراردادجدید با باشگاه استقلال وارد ساختمان این…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27116" target="_blank">📅 22:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27115">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27115" target="_blank">📅 22:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27114">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfkCS9H68mU_PJJtPR1dOj_zvtBqLmWrHEBgmfGKBzOrx8zItRR1UIjCV41Cdo9kd9W5ZpdUS6OFTBHGUEzQCkXovolfusvDX29tFSviGG38CfqP6z-kIABjDh-bT5pHioP94zmJswh9i371SyM_0tyg5EOWiWIyYgB5KVUPCz7onqdJnxgIRvAbkMIUWCl71pxKr_OaOFEIW5ko0J8tcPCCq37A0sWbgYWVfk09JyIOl-HJ0abi40KoA0xaFRNBPkmnc1gFaAOXa0Z7gR1Bda1f1-V1zImoo0gqqs894k3JXsOxrpPsbb_LqBmEZg3CuD5nb7SCtSmYBnzKzQXRoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌انتقالات|نشریه‌ سان: سران آرسنال به درخواست میکل آرتتا به‌دنبال جذب یان کوتو مدافع راست 23 ساله دورتموند در پنجره ژانویه هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27114" target="_blank">📅 21:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27113">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjwCVVvNG8tEyGUKrj3aACf23L5YffwD13rmCtmlEBF7AaAPIGxgtL670jEzlHn2qLF1WkYoB3AA7TeDEwdZ_FIc1TRUrXWCB3imaZMTH-NXd-INKOY2aaWrW6LgDyEvTaA_R79PfdAPwKE2gGs-vW5IM7Ya8CS013PYQDJAYADxzmcejpXNnChnLwoBqjl5X0jVXzEow7ejqtG39x12JpDkP_IwVTN-H4z1WCAA18jKax2wQAAnUh0O8i0JbXkG9dDOjarLerPvDvsrdZrvI_VCtzXhYqNyV64h_jJwyPDtP8WKLggGUD9aAYfCRKh0VonB3bktPhHZ2dlLFEKcZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس اسپی مهاجم رئال مادرید:
الگوی من در رئال‌مادرید کریم بنزماست. میخوام با گل‌هایی که میزنم همچون او در مادرید محبوب بشم. برای دیدار مقابل بارسلونا در الکلاسیکو لحظه شماری میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27113" target="_blank">📅 21:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27112">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bi0Tedx99lP2OIaBurqnyEIOL8jzn7-PhSbJKPdyBax8seNavabghWBOmSBlnA7Pq28gkyOeR6AY4lNGR9ARxK4C2Pvh5OWvVssNfy7d-l7dW21zF72Kp-IOzc8kFy9nNHtfYJkjgEEOc7VmL8CH8UxQzE4czvOe81MafEPWnvDF90kB8yGNYfaOHPENiwg9dtvAjypYy8nxVEV3Cn1twDno3KTfIRn94v4CLMO_Tio2XVWRLm3cirUqzJbi5qt3Ozm7qTUuFNJPObwJki7Gj8EKynjOrbpDcaEGStvEdCSB57OpSkV6FG0Yh_VQbLrnImCd0h-bwvho3bVD09NuhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ مدیربرنامه‌ های رامین رضاییان امروز با مدیریت باشگاه استقلال مذاکرات مثبتی بر سر رقم قرارداد این بازیکن داشته و قرارشده‌ که رامین رضاییان عصر امروز برای انجام مذاکرات نهایی و عقدقراردادجدید با باشگاه استقلال وارد ساختمان این…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27112" target="_blank">📅 20:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27111">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gf3-SWoEXgNAlRGMwDcwc8dQglrodYMTca4nGu9Myd1xzYgpFkbCTQ9O9e7Z5aQvTVGwWR-Pfg3G-IWnGh8nkYE8ETrEOLsPR9sW1O_UiH9sRKBzWR5QidIL_QnRVJkQzc2lpwPIrsU15hK6nlknFUP-8uA6VP5sS2_eZe-ga2o_s78Orxbf8qVx2q3zZZTXdMqZDn-YoQxx_EYTauLmyPqofc-BO-UCUSETJbWPJBhfj4WAQWNYgVT7qI0REGGGFXf0M3Y-GfPRXnSrOpWLVRJ7E1m1g0FmN4URDoBCAwRCwxs4vB_knxWUO1H631M2mTxMpgjwqau4Dgrvr6Njew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: باشگاه ترابزون اسپور ساعاتی قبل‌پیشنهادی دوساله به محمد صلاح ستاره مصری سابق لیورپول داده و منتظر پاسخ این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27111" target="_blank">📅 20:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27110">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBs6t4_N98RBOKJhxNLNu3Yf1OzjP7CyvXEFBL-o96TrK9n2J2UNtGs1tS4coNAcoMIhMAtB_dtmSDEY6ccxLQAZ6ACIgi4CinJmsshcI4qe20X2VQQiKyIJGHL16yF1u0twaJ6NuKD5elkXyyKVn5uIJY34M1Nl5653OcG_NIT0b1Vt4XfuH-n4WXZfTk22ghSzSKQkiQv2UQ7XLHSONfywCk4--HsCEDw4Ar65BKi3UOZvNonKh4up890YbmhVuTolPeukh66EirFTRWwb0-gdjDN4k1z5r6_Aex39EMvne348M-7v2_2EDfKPKrrwx81BwdYbarvxgVSJYfmR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
استوری جدید آلن هلیلوویچ هافبک تهاجمی کروات سابق تیم بارسا و مدنظر باشگاه پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27110" target="_blank">📅 20:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27109">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/St3TS7ZhautjT2ckPJwIiaQU2fsKPAfhod6KrA4CKqgNwVkwuiCi39UBREVRgKMxJ5fHPOsGypjqvtjLOdhYODbppXu2KQUR9T-oNVSl-OlcalTKoh7lMOueDVa0nVV45IPYlTI6hkUNr2Wg4ww7IhLhXyiGR386JDtjG83CbyzTiavImulp4gPno2vn_6YTk7YvyKqa7UkerG4jEsjNinX0r9XiEF0HC5p9Eh1BmXqRLXnoZZ_oVlgY5N8NHuPs_gZasAVY6vwnSRckL_2G8697oIIlrk1Nr58VOVcN9IqZwqnu-KI355ObxgwvzzuP3Cs2kJL-pdigVjktOYgc6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
نشریه‌مارکا: انتقال رودری و یان دیومانده به باشگاه رئال مادرید نهایی شده است. بعد از رونمایی از این دو بازیکن پرز پیگیر باستونی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27109" target="_blank">📅 20:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27108">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AerS1I1t-trdajq6OULj9nmzvGoznXROBHrOfmeYZ_VjEiHbn3XrTNSAbCIIpn0ZFEAslO1RSyl_pSY6_6fbhDiW3dOT6kRyAlQB_Kni1MSRXXW1JFGPGCrq9I-3ERzG1jk4uEF11tbwM3FpkCdFyY2ChG25-njgJBNfrUWvPBJrfNMcYu7iDPAX9rFuGpxFaUKJCyE7Tib6vUzoCznoTni5Tx8LsepXi0613yHtfUZdos_YiCjF7Wq9OIMkjCevQLwaOkpo2KAZwVlPr9EW3gxCd993CJnct_DWHpRz0J1PluyHk9CNQvMJTz_gtBDOj5-48dthCXk5N-HS_y8cqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
پاسخ‌نهایی باشگاه‌فولادخوزستان به پیشنهاد باشگاه‌پرسپولیس‌برای‌خریدابوالفضل رزاق‌پور مدافع چپ‌فولادی‌‌ها: 200 میلیاردتومان نقدبدهید تا ما هم رضایت نامه رزاق پور رو براتون صادر خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27108" target="_blank">📅 20:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27107">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXX621IpEExEkvtXmrcYX-SlctZF8NJDLzaTVts2cj5E_Ah4euJTiJfnD0YD5EM1V6ixBYrSvFbNzyOpRkltkOtc0HKtvdZLFe-q90WszmZYLNfxkUbU-fgLCSIhvXH5HrKBH8fnGsrioE8Z2G1lowOYbr0ZP9OlGhnSNf7iY2EqdwTRtNQxVBZ4fy3qYcPQ0h3ue16szAPpjfiR_avXSp1kz4eC1GhdNPJclmh5C8kT_o0Z46-yqKmfr6dlwJ-Ftl4vW5EtvUnhreZeoqU9zKVgIO7KGp6BF98yTW4v7BpY1Vmf8J5SqXPF6yVlNfPtUAwAU9cJa26gs1lXa-eQdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27107" target="_blank">📅 19:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27106">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27106" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27105">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxkCbUzBXDEB6AoK0fRLofcqAeN7vtOhPGLUDXlvmUwSLQmqM0nP9eJJL8WysK_D_Vk5JL0cPR2RqfZ8geh5Ygn6XP8hka4SJESCsNhJLJL5tnJR6MTP_7kqTVuiqxVVDf2fo3Req4idK1MRuQChHatZfd6QtQrZ44Li213mtOagmVGiXR-MSxqn7Dg7kwpksDRpg3NXH4IHfYrNxBiuAGq_CXmxZIXfGeQGlKbsI65gQ6zCqEcQbmi9E7syaU5swbiUGoGWr9td7bXLs59FVfrhosK3o1nTgPvmXZ_qN2EB4N4cGmN7sJN0fb97EXEcE-zGjy7Hi4xpBr6QEpd_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
سانتی‌آئونا: محمد صلاح ستاره‌مصری سابق تیم لیورپول برای‌عقدقراردادی یک‌ساله به ارزش 12 میلیون‌یورو بامدیران تیم بشیکتاش به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27105" target="_blank">📅 19:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27104">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27104" target="_blank">📅 17:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27103">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27103" target="_blank">📅 16:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27102">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9QUx6u7gsYUDb0AxP66kLcmXWZVcjmSuPA7DhPuvU8c1DDl4fIM-Pjt6ohrs5q8-0di19TlJe6hODVBZtElcGQ8_prYzAk1Y4DKeGh2flNw1wAT_PUJzRKStCuXsFeOoacj2c13DC_9jHoBt8b10OPfgnnC45DAwGJ5FQtNiHd9V8Y6D5G1yq8OSYFt20weEI3-WoJirdkRYSlQ_fBgMP3siWO8mCizt2TRz2UI-7XOKQvW_UoGI9385QeHIXQuFybfabowPgtz1gFOAAOltJGBuBnHRoUBDFKwMDgPDa75KhQ-7CjyytN3GVKfEbO5rRrB1gcSdf7xnSg1SLzy_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
رتبه‌بندی با سابقه‌ترین سرمربیان حاضر در لیگ برتر انگلیس براساس‌تعدادروزهای‌حضور مداوم روی نیمکت باشگاه فعلی‌؛ میکل آرتتا با بیش از ۲۴۰۰ روز هدایت آرسنال، با فاصله‌ای چشمگیر در صدر جدول تکیه زده است. اونا امری در رتبه دوم قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27102" target="_blank">📅 16:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27101">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=uyS_PgsRXUzPmHsP6E00LR_FqTXrkjGXP7XSEUjk0OE0QoZI46NS1TLmJa474ZcDuMpTeFKB0Iy4vfjzznsZKWPf693olVa7WkbNRMqF3Nu9io_0mX5J0GDxSXnI2XrgYOkzaaKayHD_r4hCRkW0cqeE55VpM0L8ltxWRhmgYpEvQk-u81viKyROJ90hiGKh_UqzIdkYCfBEUV9qTYPbQzbH-UZgTf6pTk0rC03C4PRlP95Rdw7vjXQMUE3JHYTghNKABThR3O77mjSyAKjqihqS-y1Xb26i9j8jil5woDSWsHwlGQlTDoTiziqr2zGFWWYF7qlriREfpISDaYbHmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=uyS_PgsRXUzPmHsP6E00LR_FqTXrkjGXP7XSEUjk0OE0QoZI46NS1TLmJa474ZcDuMpTeFKB0Iy4vfjzznsZKWPf693olVa7WkbNRMqF3Nu9io_0mX5J0GDxSXnI2XrgYOkzaaKayHD_r4hCRkW0cqeE55VpM0L8ltxWRhmgYpEvQk-u81viKyROJ90hiGKh_UqzIdkYCfBEUV9qTYPbQzbH-UZgTf6pTk0rC03C4PRlP95Rdw7vjXQMUE3JHYTghNKABThR3O77mjSyAKjqihqS-y1Xb26i9j8jil5woDSWsHwlGQlTDoTiziqr2zGFWWYF7qlriREfpISDaYbHmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو تو چند روز اخیر بیشتر از 12میلیون ویو خورده؛ رونالدو بفهمه تو ایران دارن باهاش چه تبلیغ‌هایی میسازن میاد از همه‌مون شکایت میکنه. طبق گفته رسانه های معتبر، کریستیانو رونالدو و جورجینا قراره بزودی بالاخره باهم ازدواج کنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27101" target="_blank">📅 15:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27100">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gx7rVShk2zCmPfs79l2fBR_X3p5E5mJHFQ38d-GK1c-k_1MYzmj_9I83Vb8TRvqBCFn6_cnO1-E_NvacglUxxr0JvkjL3HsIptfgUO2VDLTmqf0RkgxBp0YxXQBF-TG-0-r0HLhnIo7jvC6AgyHPjAVBTVD_CEQJQdAg75eW0UPw9-F-stJwRT1-0E-aeIo1SWCqjBkcgs-Pz6bb0TDNDI9qWwpCU5DRlg6X-RWeiT3rD4R-idOjsM210ncNQkmy02dbSZGkI04xL-Tr3qM28_Iki_cD6FuG_-QFX_TYQ24qw8ER8zRZa-E25tswN0nkrmUR5ESxBLcyAJfa6ktP3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنایی که بهترین بودن ولی از تیم ملی شانس نداشتن و از داشتن یه تیم ملی خوب محروم بودن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27100" target="_blank">📅 15:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27099">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">قیمت محصولات ایران خودرو و سایپا 13مرداد
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27099" target="_blank">📅 15:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27098">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4fr6hQFpjb5ILTmMUhhIJIBMr4-SsqnoDaw1f5J_JRbKMC8I2r3VBb8X8SCwDfsqEv_wqBDw9RNa3nLcx3cr4VzBcXaHxMuSGoP2hCcYCHRUnA8a1syiqIgnrjvRvBKjIvY7iu7RCQ2larluEt-lai2Z0P_4uQ9UIx1Dh_tCiUKTZaJKmmZn3ToX7OCAMlBn09wMyN6W1_vUegA_fmEfQXcsOemtwwgCwH8NQOscsgaSeTIxXOed6ZWZUGG0nMdD9VgohneCvXtEn8yjXixCmrTCVXZvNkj34RS-3UT1_JCLngaCjf_50MQb2WjOCnTMesKkaHoTFB4YRQtQGIrkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کاپیتان‌ های پرسپولیس در فصل جدید:
حسین کنعانی زادگان، علی علیپور و اوستون اورونوف.
🔵
کاپیتان‌های‌استقلال‌درفصل‌جدید:
روزبه چشمی، صالح حردانی و امیر محمد رزاقی نیا. البته درصورت تمدید قرارداد رسمی رامین رضاییان با آبی‌ها، رامین کاپیتان دوم آبی‌پوشان در فصل جدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/27098" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27097">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhd1pADI9Py6LYCM2AUiD6XXOi4WjuEsP6BvRAddxjBBeAEcJ-grwaZ_4SP2KHDWUKXoMAdHfKYoYAmLEzSFFYIsS48FfLz9hJtBSpz95VQkM69_E_OFXTkdDyW80EhqlRxwVxxrbmXZ5gEe42C9moqqUB1M8wkZ0FAfraODMyd8j2JnxNE-jCTs6RozohnJZ54zzRcUcWklKyYwDvdeGEF_QztR6PUEmDPn0uIsUN7rE6tz15nyV0QsK6pARjgC7lABdr-uwa_PX-66lkiuszC1Eyuv4BLAxyAQhTkdOFxCSLDzgeJMc3Fq0yg35_e8AKFCcj-5555F1lMdGyMUYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
عبدالله‌ویسی سرمربی‌ذوب‌آهن: دوست دارم کاری که‌سال 95 بااستقلال خوزستان کردم رو با ذوب‌آهن تکرارکنم. بسیارسخته‌امانشدنی نیست. امید عالیشاه مذاکراتی‌بامدیریت‌باشگاه‌داشت اما درجریان مذاکرات نیستم. امیدوارم که قرار داد منعقد بشه و این بازیکن با تجربه رو…</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27097" target="_blank">📅 15:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27096">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvuXSIa9MHqgLhvtGh_cjxCrIZ6XhpDNZl7TmShq5EBRMYuKptdwCuR7yX2ni2w4aVx4JJdCwlh7aiOfutk-bLNnqolB0DmDIG95NTHWmG2i4UNMX7GUG2gW6uswk-3QEJDgzhil0uNtfNH3PBAQjDU-2MYxw0GWA095ZmazO7AdukpSTwQ0_fFvcXMLrROMiBeHmEJmmYmeRAfnYFCbHYtwLGVqCqnkP589lq_zz8ZBlFtQ5wSk6E-JMjemJrl4E9u1DE2iAWEgMpQOF3K8J3Gmb5sVIcp3kjlgEPopAinA_LgUa1-DJEsrfO9V8NrMVzsahPJ9fSxtkh99H62Pnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛مدیرعامل‌ تیم پرسپولیس امروز به حمیدرضا گرشاسبی مدیرعامل فولاد خوزستان اعلام کرده حاضر است برای خرید ابوالفضل رزاق پور 120 میلیاردتومان‌پرداخت کند. گرشاسبی به حدادی اعلام کرده تلاش خواهدکردکه مطهری رو راضی کنه تا این انتفال انجام بشه. مدیریت پرسپولیس…</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27096" target="_blank">📅 14:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27095">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyABajTBh711ZTHsli7UdH1_5OOIjYBhgeVDeqZcEolS4_OINZChByNK1hGsMfy-86sOmQZDHq4e_wOmG9h7qLXLpXvbAlPjFmTzltqAIiPPd6vrsozadDk3rpOw6CtJq9Kj63cQitzB4PbBSmOJipSvCirONIYDq7V22lP6nESk_GlvNePun2NMArL-BHBCn6eBQWbh_ZvFZtfiSsDpyfGTjrvmu6c5sFQ7s45EXBUZNCmKYaVr-EF0qqImZKRTm7IFVYeAnLPZxP2bdlSwV23B5cJuO9Qrqh3AryYCiwsIUtRpI0v1lJLs4z1iYI2FHLU3WfC2HuvgnCzpwFIFaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌_پرشیانا؛ آفر جدید استقلال به رامین رضاییان برای یک فصل حضور در این‌تیم 150 میلیاردتومان + 50 میلیاردتومان آپشن گل و پاس گل و قهرمانیه. رضاییان قراره ظرف 48 ساعت آینده پاسخ نهایی خود را به این آفر بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/27095" target="_blank">📅 14:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27094">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHnu_79ol84asykcr8eO7wgwBI3G2mDAoZ2Qd5lSk6WdVnpuZRxkg8HKIbV269yQuaQ_LfS-ivTwy5HJr_jyhmbn2h_fdPs95-y4aeRX0Hx6p64yqmyGp-u4_qQf-LngftygDSBu6p9pZ9p_DvrGDaQf32t2OCaMLm7quyF0VcQ5KGaDUWFysE4VRRuVJtN7T7pFj9iiGIRGHxxFUYdK924JScOXvrWi1YOc26YxZFkgMVhckFqUXMRBMhKav21CIHZ1bODAG4aWM0j7dvGUQP9_hBJ5JsH8F-l8dT1rRhb8zONZfchVho4nHmBPXosM8dBZbaDZXFp-xYoeBgzU2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
عملکرد نیمار جونیور فوق ستاره سابق بارسا و PSG در کل دوران حرفه ایش در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/27094" target="_blank">📅 13:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27093">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dazqo-SOrab_E8zRw8_0fuiJJluzrYJ4yTfJeweWDv53hbBk_uRjufgR3qF08ebdIEHp5pqo0Yl-TRkueTMVsPGEuNuNRbW7QnKQax6xDgbXakjF859F4N_3wyJujEL_c0yaaSekO5WKjB5jM1fGyi31plDzQMho6cWSJ-DA8bf6zEdJnzotCONS0OpaqkRP4GGSPECCB9ZC822uils-l9seHeaubDhcK_ZwGaXqA_Qh0ehZFn1at35lHBRRXMMhgrounHgG3nnB3CEBr5gNajwqWMZfh1FIFfNeVyqKIpheu2sLqHqSUGFIfYEr9hpT59IY0brJO_zR76BgZgpveA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روز گذشته شایعاتی بود که فصل جدید رقابت های لیگ‌برتر یه‌هفته‌تعویق میخوره که سازمان لیگ تکذیب کرد. لیگ برتر 10 روز دیگه شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/27093" target="_blank">📅 13:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27092">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXkBBLqLEI0wB1o3GLXuJKxXP6pOFLK0lG0wcfBMeN5TeYbS3OugAFmxCsBaPTM5OL_9x6jqzeEhy2se95NuqNiPhXqYG6Qz89YS5mODlScrnO4Q50yFqgw-CuClk0tBp8gvlCbMVBwctQTAeZ78zTXanvC055m2H7c5pqKh9CkFtu3mZvvQXTzTTUaMK6qcpPlKWQsF9M6mOVgQggzah0Vzb_05K3mrT_YtbvhFO3VeRfSqM6SneJQPeEFESNQpWIRCjGY62IAK5UKFJbWI7P-PFMsAtETzrwbmBpkdNiuDd6r5ePNwA0vPdKY6ZsbGLPPHKPvllfNjMfi4XQUi9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
استوری محمد جواد حسین نژاد ستاره ایرانی ماخاچ‌قلعه: پروردگارا بخواه برای من که مسیرهایی نروم که باقلبی‌زخمی‌بازگردم. کمکم کن جایی برم که دوست دارم اونجا باشم تا همیشه شکر گزارت باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/27092" target="_blank">📅 13:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27091">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9be54cc9.mp4?token=LnFwz0JckZvialYlw6TIvyIGDgxuIAeMkBap8TDWI9R7YHJJ2op0tMZadK-VOXsIRiQKLWdNjCe5wEqzcZ0dkzdNdFaNDzGgsUdgoBUYqlfGN_cucWHRnG2M9z7IUu92q9RzF609fRPkLwNv-b7bqzeqMyo4eUuanmKg2Vo5lXw-OEE2BwrIenMwGGQj0an61LveqJ4VhVC2jXasmwT5WAxN3L0ww9dLrjbUHz902vqAa6W5jHlGfyyecRQ4md3S0cql3BWTyjJst74Eb8MHukNmUJ_Udfu86iHMXdqQXkyy7PbMiWUD8u2oSOvnRCPPoV5wBt7uWuuItNZa1AdPrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9be54cc9.mp4?token=LnFwz0JckZvialYlw6TIvyIGDgxuIAeMkBap8TDWI9R7YHJJ2op0tMZadK-VOXsIRiQKLWdNjCe5wEqzcZ0dkzdNdFaNDzGgsUdgoBUYqlfGN_cucWHRnG2M9z7IUu92q9RzF609fRPkLwNv-b7bqzeqMyo4eUuanmKg2Vo5lXw-OEE2BwrIenMwGGQj0an61LveqJ4VhVC2jXasmwT5WAxN3L0ww9dLrjbUHz902vqAa6W5jHlGfyyecRQ4md3S0cql3BWTyjJst74Eb8MHukNmUJ_Udfu86iHMXdqQXkyy7PbMiWUD8u2oSOvnRCPPoV5wBt7uWuuItNZa1AdPrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌جالب‌ببینید از نحو پنالتی زدن برخی از فوق ستاره های فوتبال دنیا و واکنش دروازه‌بانان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/27091" target="_blank">📅 12:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27090">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17e27275fb.mp4?token=kgDEQPEe1A7mDv06OTQYlcuZwOTlisVNO7ov4cSqFjcb6AUR2j39TuFv1CrvMLf5Dq1pyjjFAhxtTpcW8nJ70FWnVE6_mJYej62Kito4cW3Q3VGjypwFB_f0Rfzujm65tmT9HIx0zTYfsQ_hCPDM5IjFgkJn2W6Adr8R_x9kkmdhrKSvvh74CFD3n3TAxoCy7W586cyE5aRwfGC-1PFoRDyrSybGoRl-Aj0i85FNly7iADwRXcPSmSauKtqE5F5f5XP_1cINucwtIw6zpmzoCjkT7CIXsx2FGVJ_ww-Z6gTndirIfC7aWg5oKQ5VwuP8Bxc8FqIqAeyEjCirQYSJtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17e27275fb.mp4?token=kgDEQPEe1A7mDv06OTQYlcuZwOTlisVNO7ov4cSqFjcb6AUR2j39TuFv1CrvMLf5Dq1pyjjFAhxtTpcW8nJ70FWnVE6_mJYej62Kito4cW3Q3VGjypwFB_f0Rfzujm65tmT9HIx0zTYfsQ_hCPDM5IjFgkJn2W6Adr8R_x9kkmdhrKSvvh74CFD3n3TAxoCy7W586cyE5aRwfGC-1PFoRDyrSybGoRl-Aj0i85FNly7iADwRXcPSmSauKtqE5F5f5XP_1cINucwtIw6zpmzoCjkT7CIXsx2FGVJ_ww-Z6gTndirIfC7aWg5oKQ5VwuP8Bxc8FqIqAeyEjCirQYSJtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام رسانه‌های افریقایی؛ پیتسو موسیمانه در آستانه عقدقراردادی چهارساله با تیم ملی آفریقاست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27090" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27089">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27089" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27087">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCkPagC8bi0doRJLZ-Br2aNI0bW8GKSFCPkDWdWt5pTt6nsw_32v0uBSPYwG3togwo3aj6pvuE0ubw1l33sCoAq9tSFQOeYYXkmE7k1WoNe48cadJN380KysDXsvfenDNQ0h1Obz2M-x-pO77ptDYy0TNgeaZuVhVWIf324aoDZdx1WvShy-ATcdai9jIcUXJy2Nr0zv7PqufRYFNgB_TQFHDFjzWcc-mpln637YdCta3Lno9sAJvoVrh-VVWmeE2Lc6wc4WeG3s7svR6go57tQ-Y6Qi7yGT8s5SRO3sRqQ3PskJK7uusK1O55fQAwm7GQSQoW6kAIeCFoLpxJeFnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینکه‌گفته‌میشه؛ باشگاه ماخاچ‌قلعه رقم رضایت نامه محمدجواد حسین‌نژاد رو 4 میلیون دلار تعیین کرده کذب محضه. بار ها این باشگاه به مدیر برنامه این ستاره اعلام کرده هر تیم ایرانی دو میلیون دلار پرداخت کند و خودِ حسین نژاد هم راضی باشد این انتقال انجام خواهد…</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27087" target="_blank">📅 12:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27086">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xq63VRhRL2qjohKC3hGz6S1IGqlgYuIeEiYwzo6W9IGf8HUTtVnbmLneEKKwC0NCa6Fz2-2qFj5BATceL1EGvIS_3xOqz_R7gaWz9f_JBZ58qDvkjBKQ5YUfFykMI7hEq0hTUUtX3LxIeYVeiWCflIFP8O4ELNq_sZOoRTQ21a6zLKMK7N3Ctj-q2p3uvedqQrTkISEKshKYfp0Xn_MKaA3-S4641pegvozc7skKASO_d9cWwq8wJkFRZ0Fkl2gqww17mw3DYF5fS3NjhTIx6G7JxBWKRwKXsF3Nw9AlgLHygKwzL61SHMDGgj9NQb1JzfwbPWBeIf3KEGnwcgAzaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رودری ستاره اسپانیایی 30 ساله باشگاه منچسترسیتی:من‌تمام‌پیشنهاداتم‌از تیم‌های بارسلونا، پاریسن‌ژرمن و منچسترسیتی ردکرده‌ام و تنها هدفم دراین‌تابستون پیوستن به باشگاه رئال‌مادرید است و مطمئن هستم که این انتقال‌بزودی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27086" target="_blank">📅 11:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27085">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbzGeDU4xbkKyGGd0LWYCzUHcWWXPYHNDompvLLM0SHtqEZoErDu9f_qauaymOxBHH33M_lYD7s6iaxVkryNk0l8TEFxxOPkqeshnGd54hoPaczNK6KVarRe_tWqsZnZKJvPbr3R4lOnJigqQaNXiJP7YDwiGrdqHvpwv6FD7AUVB7TfYAovjOAciajprbrgi7BfH2En11Pi_gj1N4qTtkjBXU0xaDptO735JsK9I-joZ3lJJ1UmrB7Tp1YFlowdkZTCY_lbxZLfaaKuVHbcJAA70mC1kxtONIGU4KKY0xOR8k9xNxwtJkARsFDGoZAAx8hzMHv1pbRXxNhOF6J1AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیویی یک دقیقه‌ای از سوپرسیوهای تماشایی مارک آندره‌ ترشتگن در دوران حضورش در بارسلونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27085" target="_blank">📅 11:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27084">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZQNip7V1HaIGgvz5IlLy_FvmvItoUaUeCYfPwse6hXhifWzZFYs8_hvs01nQUA0g0jnK-8dFunAi046pQTVoSKl3DOoCpA1857hy2msgHGag6PJkWT3gRPg6OeoIj5o0QNpDn-sZfJT6DzqJxzK89DIAbSut0QRtQ02BuV_P3UstPWEeebQ0pszQa-ZQ6jgjBpKYk9HXNCvLaLLAhO3ET3Nb7C0Vw1soVAuJIiXP5M9Ly_gflEt5qIEjuyIQE1Vjkr_vPT5hf_IjcCXXq0iQ_r3xdvFgLKQUGYA8dzxxI7lAmrUyOaslMwC1yiISu6PO2ZEAgIPbb7GIaXENZzhOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27084" target="_blank">📅 10:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27083">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=sjFdmPjijrep7pLXOkeufRQ9F-6BCRgC0lT8L9sOIFWuz88iPgRfpwBFIFG8S7OJxqMPuC9fynSZU1GW2SY7azH0PQGhijsx7B-yArCMmCn2aDWrNTaweu9yeDzRSDTUaTwRDZ0w9dPGNaNQoyuYpfXgyRzrBppukxAKBkOqKB1WXgQ1YT09oWXMfgd918oOLUPYE13zpblgIrr3x3juONZ6bSxnvoehzJHzX5nRoKhn2OJppfnG3swffpaN8fvQQTCFDpHfI0By3B270sIYafLxq-1nfNNNHV6vwZ_A6pr5s582IWapraBuH_B-uizErO0wI0SrqEc7iIuVC1uCZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=sjFdmPjijrep7pLXOkeufRQ9F-6BCRgC0lT8L9sOIFWuz88iPgRfpwBFIFG8S7OJxqMPuC9fynSZU1GW2SY7azH0PQGhijsx7B-yArCMmCn2aDWrNTaweu9yeDzRSDTUaTwRDZ0w9dPGNaNQoyuYpfXgyRzrBppukxAKBkOqKB1WXgQ1YT09oWXMfgd918oOLUPYE13zpblgIrr3x3juONZ6bSxnvoehzJHzX5nRoKhn2OJppfnG3swffpaN8fvQQTCFDpHfI0By3B270sIYafLxq-1nfNNNHV6vwZ_A6pr5s582IWapraBuH_B-uizErO0wI0SrqEc7iIuVC1uCZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هونگ‌میونگ‌بو سرمربی‌کره‌جنوبی درجام جهانی ۲۰۲۶ مجبور شد دربرابرمجلس ملی کره حاضر شود! او توسط نمایندگان مجلس کره جنوبی درباره تک‌تک تصمیمات تاکتیکی‌ اش بازخواست شد. از تعویض‌‌ها و دعوت بازیکنان گرفته تا ترکیب اصلی تیم و سایر تصمیمات فنی اش، همه‌چیز زیر ذره‌بین پارلمان قرار گرفت. هونگ در ابتدای جلسه هم از تمام مردم کره عذرخواهی کرد و مسئولیت نتایج را برعهده گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27083" target="_blank">📅 10:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27082">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBNSJu5sIEdWB7kTajma0ho0PnVLkg_Ke0ImZMDCRAwR4NecGkmrVFnC4QSvojOd_JBrcoS_POLU5jkFERGKym0w8EmeJ2qmo59zrPoJwHZEzfoFSBizJrrlTWGNNATsQuyjO13Sj1jnkAbX8kUMiUS28WBkHKM7DB0Vs3c83PAlL10DG_nxmTbSb11PiYfhs9ibeqRvYO84vFbD9kL-wmM0UIsvvA8iH_4Lm-_hBwmCuWHdErauyV2SefzcOLl77G9n_7xbg_8vw_uB9xaO8uCUK97QhAvTUOO_Iofb-k9uuAfKnUT4z94H_b-uQXUeaG9TsOC_j2SpZHZB180CfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
نشریه‌مارکا: انتقال رودری و یان دیومانده به باشگاه رئال مادرید نهایی شده است. بعد از رونمایی از این دو بازیکن پرز پیگیر باستونی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/27082" target="_blank">📅 10:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27080">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWabtEz8E7QFp3_xJd_UOPA5DJ2udr1-LBqaOZI7ldLmsQ4bSG_7MC6U79bKVEUXx80ieTA2bzeyhtmO_yM8pd2ZJ-Z2RV9vXlaFkhNVNNiK7up2_rcJjcxERYqTJ5mBYacgmzej4cUpD9b-KCrk-fUzT01_6C7szhQF8JsYP-6fNA2bkbqDqRZJtrSVpNF9sJ8uIpXFBQ1mkfWDYxzls5pbrVrEFcQG4d2puB5yI3oTJnlseDrWP6Ig1Kpbba4vFiEVaRwKrUsypvruiyOuqhULo2Z0I9mPE0Pv6h5eZXer7t38Tx6kOEXa5Ryo1EyUv-VgOSNQb2HrJ8gLbSd4eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جایگاه‌جهانی تیم‌های ایرانی در رتبه بندی قدرت اپتا؛ تراکتور تبریز درصدرتیم‌های ایرانی قرار گرفت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/27080" target="_blank">📅 10:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27079">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiQAzR9WK2RGjcrutdYc4K74jgTVfjH8R6QLaU4agDz1-x18CpZi0oDEWROnhnWJD46Apur0h6ef4ui6PszeIr4-kfZVRn8CrssAag936Y5OrDikNGqoFK5MOTzkCqoS2jH_WlTTMgRr2Uj0Tg_tarj4_paGb4Q4uaj_f9WFxUydw0XKb_-AW96iNim5nVDabnDTdC4BOoyFGn_WpcydfCX10VDW4vr9nk8wzMmaeFn0vRuTOfL81f-I_2AgvBqpliIRZ9l5F9fe9u93DmYWXsafAd7s5S2P94oGxpZjhQeM9MEY0dNW9uDdRHMsJ40BU6cBLcIiCSe1CmfIO1uydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق اخبار دریافتی رسانه پرشیانا؛
سعید واسعی هافبک تهاجمی‌سابق تراکتور و مس برای عقد قراردادی دو ساله با سپاهان با مدیریت این باشگاه به توافق رسیده‌است و بزودی باحضور در دفتر مدیریت قراردادش رو امضا خواهدکرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/persiana_Soccer/27079" target="_blank">📅 01:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27077">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_IqUMqQ7Sa3TmWY-aVdurSY7LAzZSRmd0qJcyt1W7WKvCP0WAqwb6i5_zdtmORa5g15TWgWHO6ypfnxul3KROkTUPtg96nKXNnNleBb7J0WMxHxeLmuHyTdHHwKDyOxNf5LBafQKXJXrHu_vBEKHEdnj4u43s_y82SrOc-NFabSvouRLPYuadOoUdvq284hNzDf6NB-wf9AyUR8G4SyyTtRvu_xwueW5sRJgFwE6VwxIjml_fVT9jtmSz2yj3y7CIs-T-hA5ayOtA_F9NrB5xL0GnJdf8ehdP4vtH4pCt5r_1zQ0d73flKQL7wHBAYi5S7l_X_ZGjH8bQGNZLCUMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌ امروز؛
مصاف تدارکاتی و راحت باواریایی‌ها با تیم میانه‌جدولی کی‌لیگ کره‌جنوبی
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/persiana_Soccer/27077" target="_blank">📅 00:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27076">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjHmQSRbEx7ayljWhF_gh6iX99gMWLKLJKrMxerEgJFnVei6u6-twED3pxHkzm3Ci-K3hM-NEuLuCHYMZgbZalLfp1K-kNEm0jR8b-IKrMrJ_dZd_2dHcnzSX1uvgiQWuStDlWgAgqq7mmsLIEyeG6EPoR8w6pY56fijP_RiCSKpSbRccCh-xoRQcCKleiFFDPkiejk5IFVOH0Ziv2tWYErRTiGBP_Vvd0dFRocQYl9W2nTxWDrtzn1EWeUe7PpngzCrSZX89RDvBAt8rvvPhzGxIFfd41vqgzmM8iTXBGepS8sSW9xJS3XDRiSc0Q5XRLQO0Yo2fsFfMQbq9OfqCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
روایتی‌جالب‌از آیمن حسین ستاره تیم ملی عراق و زننده دومین گل تاریخ عراق درجام جهانی: در سن 12 سالگی یتیم شد و پدرش رو از دست داد. بعدش داعشی‌ها داداش دو دزدیدن و هنوز هم پیدا نشده. بعد بخاطر جنگ آواره شد و یه‌مدت هم بخاطر اینکه مخارج خانوادشو قید فوتبال…</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/27076" target="_blank">📅 00:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27075">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnLuZ90gqli3WBHuQt1jOjTSKwCavPWrxawdAJD7EuTXQBbkkj6HaxclTXVRjs3iW163qtZM403RDsLvlcdDG1k9rjyj10Mwo8Go2cP6_o3LFJ0HLHgQoTSWXzHC5Bm6GZj-lVUHEafIAdaSim1PR49rYYZRyuWluoAVxpsXDK6u-rPvphwSQmGCzfXe75Ch9R7uAXBxmbGviYmJxH8XdPwjwhnQKCI0WQTfwXj7esoYgHJxCh0VaKDYD3VpYg42sqtNf4_0--lhapvyL9L0zjuITSQL9QTPzEEhF_iJ2A9DyatfZkHZW0bM3CA3on9rrv2wSvkO6jv6LnIOUVd5DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
محمد قربانی میگه‌الگوی من از بچگی تا حالا کریم باقری بوده. حسین‌نژادمیگه‌من از بچگی طرفدار مجتبی جباری و فرهادمجیدی بودم. خودشون با زبان خودشون دارند میگن که دقیقا فن کدوم تیم بودیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/27075" target="_blank">📅 00:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27074">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8thLk3Kp9ThA3wqWiqiqRUxp28WIF-FiicPbjhc5LPfEvwegLqAu11LNbh-pe3yFHebF5jIOsTDOMw1cyJdZJMp27_1oCTYaGLFNi4355jrBSqU74yw7z5L8oRyB6djpjuFizM2TdRTflBtwbRXJ-f2ONZ0-Fw_5jRkWPlx3W7Ssr9rBtY3evkQzdY6oIDNluE1XBYiHUkbEHHvdcvaAtlcfSlDIeMjvxr_91yCroPvFXk8ROroGHudvF9zg5NJKJR5Vo6FqFpfy534zJsdLNRAgsb0-rt5ufcqfqzF6pKU-t8e_75a4hAnSsK5t_7Wnn9Zo2F2bnb9IR4bVqiJfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/27074" target="_blank">📅 23:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27073">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCXt6qTCRFkAndPmK5hzyYbOOTZBIeaVExHUse90GN4jpyYGMZHDGV7yEOZucO81w4VNiIfu7IijQFXmZOfdyiuqCHnebfzdhVL0oeo9ZnSXo6BOftmLXLWib3Wiefz9Mf5gDd3paVNuXL3suwHzwUDxgitkZDcUIhpEGQSLiWAltHBL98kbfuT1PclXa-np-b8AJk2ZHeMTU9kJ3CmMnonvkAH-0URZJ67GhNyezzOUFdsvFnL5Zf8-0CiuSINimZkZrGfcV7gks3JbLXjtyxtVX4aNe4SnuE_enUkcH4NrEAjnT-R2Q4ghtEHAdbi4wQA7rx8RtNQAh-RlBv5Ugw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دادگاه‌عالی‌ورزش "CAS" روز سه‌شنبه پیش رورای نهایی‌خود را درخصوص‌پنجره نقل و انتقالاتی باشگاه استقلال خواهد داد. اگر رای مثبت باشد فیفا پنجره رو بازمیکنه. اگرهم رای منفی باشد این پنجره نیزبسته خواهد ماند و با شروع نقل و انتقالات نیم فصل پنجره آبی‌ها توسط…</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/27073" target="_blank">📅 23:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27072">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tt67oB7AW3Q1Ygx_ZOUWZU0gROiYhUmV6eCKeAREmK0iHAx8iCArEZtVk3oM4Fv5Q36OzJwYDmpnBYgSMlub9IhUEi3aZ-z9YofrBjl2MPtMMoLhCugyfRKIRRfUFr_hpQaeTg7aAMpeYWJecIT3ERtnkKVvjMoOKRTTlsuMeNrdrFbsNjAX0wku8UdTVxbx2azDqwn24R8ErwK-VlX7yLY3PPtJJU-gBx_PrtZQw7VS8Sdej1yrHwLuTls0CMdvuSSDZcIJEtxcw9Y-3S84coS3roBLdSIMnsEQEWUzQRgR3_nRMin6Wyl91HtxTPPu939PCEiMnKjhGxjp0vy5LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
اسکای‌اسپورت:الساندرو باستونی مدافع 27 ساله تیم ملی ایتالیا درخواست جدایی از اینترمیلان داده و به مدیریت افعی‌ها اعلام کرده با جدایی او و پیوستنش به رئال مادرید دراین‌پنجره موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/27072" target="_blank">📅 23:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27071">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZJmvlIlTymHdVCPqyOxOKeBWOwrCCpbvt09iSqnc4AJKltoS9cwNjM70kRAv0mKWhMBwqu4LJU2RVhE8yVk_iJ6BJo0exwZFXj7bAkAcUsDHKMW7QKqkKoz8MEu5LMuko2DSLYb7c3_LUn2KP1_QT6hYgqO0W3BltjN675Ofuor5sOF_MYj8pTdoLii1zBJy9z5jRCNrtn8JFEY2E6znkL6gaH7cE2s-HS2Jb3nKLKv4V1AnlOm2FgOfDT2QAzL7NPprRCiuEHEaU-c_wcykd-QZGRkAGjy2Eld8WKEy0lEmwiiEes5gtyxoLH_wxmVeucc5vT-FS1DoVgsWAu5EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/27071" target="_blank">📅 22:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27070">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hN9NqXomxrukha1Hc6fcW62eaAUN9UVNLB0opoRsgpEaeHdMrgBUhTgZT-fKcnXoaY5w8e2RdmC0A3eKdKuVuA3aZP89f_r93l-ZfciBxKm3IQe7kCAFPHpyE9dkrDbpUrljgY0bmJew8i0ryAcNpGyCSn9knvN5GjEmLz3k0Av82yoO63ZVW3qE4nAlk0WQ43yG9KW-0PVk20cKY6JsfmeiykLQ8SHiTAl0X50e2ySmsO8dXjjTpki-U7qr8Cn5L-EzaL7VRkLP7jEaMvCGdlTzgT1ZjX5b_q5Z1DWPLYd1Qq7SLU1PYIcVFr2DInKDjxEDNGXYWkLHLK_kOF19JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ دونالد ترامپ: این آخرین فرصت ایران برای امضای یک توافقنامه خوب است. امروز یا فردا می‌فهمید که چی میگذره. قراره به زودی و به یشکل دیگه، مذاکرات پیش بره. کار خییییلی پیچیده‌ای هم نیست. قراره فرداتنگه هرمز رو کامل باز کنیم. بعدش هم در مورد ظرفیت هسته‌ای…</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/27070" target="_blank">📅 22:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27069">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbBEqHnU-niYU5N6CMCLrLit5OfKZmGsyCeLAHlNspwo2UtJZS0sGWg2QnuZCZPZw1nU0r3PQBbFREcmPT_tul75qS5zCiPTJ47cVs3DyzxGtydQCCJXVMuaj9l-DlU6g7yFpHXD6VPGzUQzdXMThpDTKwvyDDJCPwZlHMRNG2ccNtjAKADviiN6aIUZoaPtWTFbAvRPlQHKed6-gnIbkPBhylWNtGdvG08UqSs5_JrkGho8sCqgxemuKlN43nu3K6XA47f7b3Ofc33nYU6tm0woNfQ70FOjjiVlzF3BQ4Q9FY0c3HCKtfbCUx86vS2yyrvs_SoUTsn0pwHO_knd8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/27069" target="_blank">📅 21:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27068">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97c6b80b0.mp4?token=D78sTdWP1OK-oE0hH9VSXWOANsu656HC8oUisoWTQv9jDkaXarGpInckz8J2YEiEBKV5TzbuFf5wo-K7h5nAE0_OurywrgFiQHJ4tekxtEcSrYR84Mkso6Kd-0Rxwbv5lP2GxQQ6n0eiT_roYEZWiYrEUkTn_015AP7J3QIEfGjlh2kcpu8HkoX6SyFAtj5ag-itzqlTYGLp6K3b7ADthgYx89c3pnR46_u8JmtULvQilUHKh1RBzqeRR5q74YpQofrStYHiNrv67VV-BURwIooXCLNfCw2S4B8m46PMSmTwth9wFOpjQ0CTdGiQHnDm1RAIuL4ifoPupZ2OAXEBSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97c6b80b0.mp4?token=D78sTdWP1OK-oE0hH9VSXWOANsu656HC8oUisoWTQv9jDkaXarGpInckz8J2YEiEBKV5TzbuFf5wo-K7h5nAE0_OurywrgFiQHJ4tekxtEcSrYR84Mkso6Kd-0Rxwbv5lP2GxQQ6n0eiT_roYEZWiYrEUkTn_015AP7J3QIEfGjlh2kcpu8HkoX6SyFAtj5ag-itzqlTYGLp6K3b7ADthgYx89c3pnR46_u8JmtULvQilUHKh1RBzqeRR5q74YpQofrStYHiNrv67VV-BURwIooXCLNfCw2S4B8m46PMSmTwth9wFOpjQ0CTdGiQHnDm1RAIuL4ifoPupZ2OAXEBSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فصل آینده تو بارسلونا میمونی؟ فران تورِس:
‏من‌قراردادی با بارسلونا دارم، اما در فوتبال نمیتوان پیش‌بینی‌کرد چه‌اتفاقی دقیقا خواهد افتاد. من هم فقط منتظر هستم تا تصمیم درستی بگیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27068" target="_blank">📅 21:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27067">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d787366ec9.mp4?token=sOhWdqyJy2wQodtMvHLh1K-Z7LpEQKGYM5arK7-c6tpUAjH--QRCJgJNfuEhrs86L2l53LcHbuUMFmwI64PqlBVDkFPt4C0c6QUO2k6_9jYsVowDt2T14qq0YiltwXHDrE3y_KcWhYkv-hEG1QTLzNGNXvCiuafiDIKrZofuoSD3vFQ0rgfz5eOlpaQkFkrs7W7Fy4DFGOFINc7j0QQLVkNznnN4iXQfC4FuF_zpzdjzk3cVaqfnP2l-XFlAnGSyM11nvZdHjV1jJgyKPMxYb72toExgzQdu8Tl9CXIwv2jIafiGyVVzESS1kYEGhONEUHyPGsO8N7rVMROiWB3q7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d787366ec9.mp4?token=sOhWdqyJy2wQodtMvHLh1K-Z7LpEQKGYM5arK7-c6tpUAjH--QRCJgJNfuEhrs86L2l53LcHbuUMFmwI64PqlBVDkFPt4C0c6QUO2k6_9jYsVowDt2T14qq0YiltwXHDrE3y_KcWhYkv-hEG1QTLzNGNXvCiuafiDIKrZofuoSD3vFQ0rgfz5eOlpaQkFkrs7W7Fy4DFGOFINc7j0QQLVkNznnN4iXQfC4FuF_zpzdjzk3cVaqfnP2l-XFlAnGSyM11nvZdHjV1jJgyKPMxYb72toExgzQdu8Tl9CXIwv2jIafiGyVVzESS1kYEGhONEUHyPGsO8N7rVMROiWB3q7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
دلیل ازدواج کریستیانو مشخص‌شد! حتی قیچی‌ برگردون تماشایی به یووه هم‌به‌پای جورجینا نرسید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/27067" target="_blank">📅 20:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27066">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txCEJ4-x21Niz9v3ClrIhyCGawPkpPRCzDYv6CtYbDt329abzcUWWFsoDFe6d9BUpphLtH9T3SI2csPARSxvQf1I_8vGxvRWFYsJAsKsQoHhzGbv7mGCTWFOpjW0XeADCfrZN2GnT1RwzuTYd-AdsScEsn5cLFQU0QVPKJZW21Y874BPkOT17XLM1vpRwRzzlY31ObTaxh1oe1-pL6_quK7_6uea4jWpWAVXN4b6sVc1Raih3WNNR9Fmz3JEtcraIHtBMdf0DQrxzAZEY7yuTfKege-EiNKmglErFlaf2qfd3cJnOUfPwFzeqk_loI9lkay0nn5gNvF2uX4t5diArw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛
یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27066" target="_blank">📅 20:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27065">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpzq4TPCLAs9aWo-12qxXRN0SZW09KlUCT9n3QpdgBRvgnzEhcYULFTdyC1ZLGvo3j7ztxoWJ1u6G1fQQtpg_zxXyILYX9cYv6ZPmyZzh932LlEQ3GAvpqkgRkkMIR_1p2yG6p2GTYBFz2yoFW2Cqx5QqmnvcOHg48Pnhy7c_fSL9yagqaa91rSnarfwAO3P_9da2Gv-KbaQ9w5G1h7pvPraMdu8Jn5yo6GeOn8d8VBwA92pt57I6LNNKU5pgOCYKUVZ8eliEo-EqCQgXjTz13V5Moszgi4DV4XPRFvYmjnE_IIk1-omX3MYuomGjhEBbc4r6WSxjSe1jkPTbwahYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
طبق‌اخباردریافتی‌پرشیانا؛بعداز عدم توافق با مدیران سپاهان و فولاد؛ امید عالیشاه عصر امروز با مدیران باشگاه ذوب اهن جلسه داشت و برای عقد قراردادی دو ساله با گاندوها به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27065" target="_blank">📅 20:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27064">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnV6HdMLHBJSu2k5kTbXiI7FX6YNe7S8NjKOX7H_vj-2Y4eUtWuLjQbJ63OH5bjQiG6VxCJvQ_XVILUOH-QKkCwT3Th9XE2CsSXULsExGqYMGi1v7ushy1XKO2mYK8DfIuLxIrHOwB1c-VRbEZ_4brO9-BCf6nyL0Opp6QspzzlL2EVb9Gtng8VogiF96m2Igy2fLDa_4hdfgS4i_uL_sJH1tiyLQ1Vr0tlV3vlC9dbnXmBWPuSgH_iNjTIklRXmH8LBz7REXFw1rgB39qKUUHAQLZyE4jJvqzUBdo6cUXr_pQVYek8k1tgU0F_yVsmaqbT-R3eQ0Lku_Uozhqeh7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
تایید خبر اختصاصی‌پرشیانا بعنوان اولین رسانه؛ اولیه هدیه ارزشمند سعادتی به زنوزی؛ هادی حبیبی نژاد ستاره فصل گذشته چادرملو با عقد قرار دادی 2 ساله‌رسما به باشگاه تراکتور تبریز پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27064" target="_blank">📅 20:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27063">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dt-awOI-0Vt3XRmpBz4E-ZdNmvrMUUDEohdDit9q2GpUVdVG1SwDqdfwgEW4l48qim_enGNJ44kyIKNNk80cW3Ft4b9E3KbIqBwJ_2EhigSIKfR-_ZFrbOQ_2Eg4CmwbYEoC06pbCQsvB9BFtrRN-JP_AwHas1aajtK0K4r_kts0lCbExCysowcfS43sZ3NmIwGgxBzgu8QkcfpnrhTbfu8oi_OTSTdaYpwwp1athRiEUR4i_25jPf3zpO61zjgXq605sFgKRycsAQLxu29UOjtMRXd2YvrEeSPSHk3lP-zWSbzFnrCZVUC3Dd7kq3So3QAa6V296Ob17eEP8q_V7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27063" target="_blank">📅 19:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27062">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab970d5a0.mp4?token=tdfAdox7Zjc88kYPbwwg8sULSOt9SNNXZ3rIkILsTY4FGDZTdHZmlGir0AuDU6bGskT3aJg0CHP9GxX95Ut0GG-aE5En7I4yWzDBOEvcDrkPD6nlJgRuzxYCK7OC2DJBwh_jUhnW1ExikKjWhQnDC5zH7HM_uVYKEPpamGGCoKzKLyYM-R_Dtboxi02xS21ncVj9355HDAN9GZnjv2gGh7MXrUmJ1_JLewfOBMzJhkOueO2uBrjiuPoQkL6ZX5NvFtO7nu-2ohZqYWXowvc5O0aTdR37V0igcVxu1rVh0GZxlU0LfbhIGIPkLwICCwYrZftSBDOyxzzpFstt1gC8cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab970d5a0.mp4?token=tdfAdox7Zjc88kYPbwwg8sULSOt9SNNXZ3rIkILsTY4FGDZTdHZmlGir0AuDU6bGskT3aJg0CHP9GxX95Ut0GG-aE5En7I4yWzDBOEvcDrkPD6nlJgRuzxYCK7OC2DJBwh_jUhnW1ExikKjWhQnDC5zH7HM_uVYKEPpamGGCoKzKLyYM-R_Dtboxi02xS21ncVj9355HDAN9GZnjv2gGh7MXrUmJ1_JLewfOBMzJhkOueO2uBrjiuPoQkL6ZX5NvFtO7nu-2ohZqYWXowvc5O0aTdR37V0igcVxu1rVh0GZxlU0LfbhIGIPkLwICCwYrZftSBDOyxzzpFstt1gC8cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ویدیو بازی‌بیلیارد تو اینستاگرام 224 میلیون ویو واقعی خورده بود که یه رکورد محسوب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27062" target="_blank">📅 19:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27061">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkvYSeN7XwZ4QKEG2VFRNfOLa-O3ugZAIq_5HXyp-be09mBnE5Ni74VSvw6daip3DuXE0quS1hHBJr-EtZDUQIrQJJErgwmLmHyfvBFn8jLl5LZxFG522JSYOYHCdm7UPJlotsli1lIhRh0VoqGwZtUbJspRIenxcFCmaWjjaYoWsy9__9rry6dQn_ne0UKMDvvE-UhTavjE9xaSzgUxjxB2DaFLuXMof7ytCDaZDz3QbOmpfD8H8Sd3xlOoRg6Y_DnnEYiiFJp1bjUETYJib6xa1Ta-aEl90QDemlTQhfqxgBUx0TzY-CUb74K3qcGG1oHs2wduv8TTt129S1mzxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27061" target="_blank">📅 18:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27060">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1PUHvd0kLjulpkEZsmbvwOAhl_3eLzITEkokvqnKPnRr-mg2R5uLZHpR1BK7ZJ9TirlrCg1yi0zwExXFKp-nt8iFMQaPuIyAIWEG0hnjjeptF_KRHCdAHmFJGmrWg84QnOPHXaF3xBB2uosJk6Sa0HNohXwdF3tXm_2bonA5egP3lU2nFBcQniGbeaB-AH5Fwt8zB-lL2H1irEmqNVt5K9JTo1Zlvh7c2SkoJXaBdtk7yL7a4B8BPBeTvumktJR7zbD67ojvG6Uea7arThJVNqV9x1feFiXa7wdAPFtrFvufFFNiqabcvCOh_pQhKXMEnGXBOc0cgtyMzqxATK9Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ نگاهی به کارنامه لیونل مسی در دوران حضورش در پاری سن ژرمن در تمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27060" target="_blank">📅 18:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27059">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJxud07YaY_btB0aU6T1d1h83xcOOO9AVhMhOaYdRmoG9Kl_uueaZSw8xBIJKNhteWuvEXgos1fD2O-S78bPbYYFDZjUj0v5Q89Bd-ttmHENmJKEy_SlpSkgKhgAp3xzRBwAARwu5gdGUfgN9O-ETSAD-Tdvt81F-lt4XOqUB7vurJoxeloy3ELV_nCy4jIHRqUGuqcllvdohzpdzY8v0v-Z0xjBuPAr5koVQXCeHuU5YBaS4-MocqjZjvDZULTDJbSkm0G_acEzG9Opd4fA4L3eZHR7894Z_haRT5neGrnpHEDFx7YEvH0cOFyPU4QyVVg_pkMb4X9l3o4pPqppSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛بااعلام‌فیفا؛ دیدیه‌اندونگ هیچ مشکلی برای عقد قرار داد با تیم استقلال ندارد و این بازیکن بزودی قراردادش رو با آبی‌ها تمدید خواهد کرد و از هفته اول رقابت‌ها در خدمت این تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27059" target="_blank">📅 17:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27058">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDMN4gFiKpAv11jx31EJbN6Pjjs3UnxXqYLn21jtT3qRRSFyZ8g_amZvF99gu1eVz84cNhhpTxTbYcMCF1gwqKug3DQBKsZub2q0YaWy3YOotxM_gzo9BQPOCxKztZtkdLcp7ESFUa1oz4kvjTYAkED5-n6twhuoAf8v63KvkDF5nGiELJMBxoJaV4tEYthswgwdvSnXLYljxFADl6T8BlHw_TitbEyNb1GcRjUgQD-mTYoqPIJerUXX6L964pNejI2yofNmKlqabyvZhAHwAsaFhW9_lhYL6P-c-lQF2QO7Lvsb70T0uafNow4aVCjHuLqNK_z9y4C8CC5E3l-JIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هانده ارچل: من از بین تیم های اروپایی طرفدار منچستریونایتد هستم. علاقه من به یونایتد به زمانی برمیگرده که کریس رونالدو در آن حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27058" target="_blank">📅 17:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27057">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCaNhc9g1YmZK7Blb59FUc2K5Dx4dJxZSkYbZ1reunmTN1DWcoKBRWlICrB-_DyfQCpeAilo7XlPfr1RtJDMXVp5oMS5FE4sGEECk7uh1oZLfbV9zTef-OsbSQNs23pNqiEdnB8I5lEZhmISF1rzoHZ7jmZWHvxepnHfeF_zWWLKtSxkea7Bi9fbXY5aYJsaPN-ZxTrtXy23StNF4dWD8u3x7oDfcmJAfN3RWQbKUEOewewmtFPd9Gxcq02brz2GVe_fjq4nbY0AooQXgPN0xNAWE6hlgxz1mqF8OsvXwxhCqRCHxSqrahZCYWLxR7SIG9-osAVTs5sv3f84zr564w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27057" target="_blank">📅 16:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27056">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fixifTMZFX3UAzWw9YoJFMFH8x1o_dxgO9vZI3t4WVzhtZXEACdeT3Vnz-6occBPrvCBO9-eAcDRjXYkoV_Yv6w_kgdv3YKMY1LZ3m3FJe0XKEe0ZMlrPSACNMcHWd7CYppiisibWS1Y8L9ZW7h4aJApE5D_C2nzPO9gh2RfyL3gteMHs5aPdeevN5RH0ajJTdezmUTZ4JcV2IP3dQyoZEdtNGO3I5VJyPwr57W6OWgBvPCN88mtr_czBIUhLRMHxDtvpvHOxiyIv-7Ox1T2PZ-Sk3n1VZqgyJVjrxlOpoXaWVQE5tcFtZV34oubf9F4rjoS34JQGTXh4RILOVaWSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ سید مهدی رحمتی سرمربی‌گلگهر ساعتی قبل در تماس با مهدی گودرزی شاگرد سابق خود در خیبر به او اعلام کرده که پنجره باشگاه استقلال باز نخواهد شد و قید عقد قرارداد با استقلال رو بزند و راهی تیم گل گهر شود.
‼️
رحمتی پیش‌تر نیز مانع حضور…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27056" target="_blank">📅 16:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27055">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahCrM1mozQpGpsr0zLKO8psK5TytIK-o0D2qtyHNaaWipNyWc7kduVedWPyOkwP-LjlL-tUPmAphiePfNngRrPA9v3r-c16mBmCjnAnYVGJbV9f3TgY4fAC1xleJ09gA9K1Ehuv5ZBzmsmPOk18ZqeQcdrvR1brhB9fHJh3TnsS-srOzK9rklbKqYZRSqiRSW4PcEOFzFeKMwzWb3xcqf7_K3E7Z717NKxKg5iHSV6GEFk23YW2iXKoPWMfk8CKI7Gc9p5eZmN4RXk_QQJe2ckTYM8kcGynPjHj5fx5h1JBNTqXkjUKbdareLjc_xLsNC5n8CImHmcHFKVF-ir6PXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔴
یکی‌ازمسئولان‌باشگاه‌ملوان‌انزلی در گفتگو با پرشیانا مذاکرات و توافق باباشگاه پرسپولیس بر سر انتقال فرهان جعفری به این تیم رو تایید کرد و گفت تنها مانع این انتقال مدت باقی مانده خدمت سربازی اوست. درصورتی که فرهان جعفری بتواند کسری از خدمت بگیرد این انتقال…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27055" target="_blank">📅 15:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27054">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2279080601.mp4?token=aOOaN-58l-cAgPcVuSUWvOxKZlYZA-_eB5PjZLCQiv8SA9i45vzO0XB3c-VdWOLZIwluL1CW_UCveaXesmDUa4NLJzWMTc4fbIyBZ0KtelmpZbit9Tzd_eOgqWdp0CoXAPQy5DB5ILQn_OUHrgr8L0k5CLH3MSqLK4GvpwtKTOeRa0Gs3SmNj60q1UBoGFtnRTqZj5a1c3EjQTEq9qV9pukFrDnuh0kfeuX0FLnaW_zSzqNCeUN3Exy0JaUEyI5EZ_hcqE-hXV_df8X-lbgkKssiI2mZxbwXEfo14AFSbVa_0mm9wepkQw55rLTq3NPCKA-4MOebyHeaqOSBRYN9gjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2279080601.mp4?token=aOOaN-58l-cAgPcVuSUWvOxKZlYZA-_eB5PjZLCQiv8SA9i45vzO0XB3c-VdWOLZIwluL1CW_UCveaXesmDUa4NLJzWMTc4fbIyBZ0KtelmpZbit9Tzd_eOgqWdp0CoXAPQy5DB5ILQn_OUHrgr8L0k5CLH3MSqLK4GvpwtKTOeRa0Gs3SmNj60q1UBoGFtnRTqZj5a1c3EjQTEq9qV9pukFrDnuh0kfeuX0FLnaW_zSzqNCeUN3Exy0JaUEyI5EZ_hcqE-hXV_df8X-lbgkKssiI2mZxbwXEfo14AFSbVa_0mm9wepkQw55rLTq3NPCKA-4MOebyHeaqOSBRYN9gjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقادحديث‌میرامینی‌ازشرایط‌سخت‌اقتصادی:
یه‌جوون‌چقدر باید کار کنه تا بتونه یه ماشین بخره؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27054" target="_blank">📅 15:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27053">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDVowA2V-AbjVsnZD8naR0m4cJu2E1PF5qifCMk7WZ-fNkOT5ZHiAik0Y0cwdCjRR-ZCDZlAvMWAYa7t5WLX0LZQ9hw0MmmvzJFMzKV2FHhEX1a3q3FImFUDp03xMhioxUsLY-BppRv849mNB6wvHxKN_asGky16yC7IQtE9GJUPi_H3P3htq684xlBOTRgEzG_oNPreNqCAx80J8B2o2YnD2X9lH8c-YbH_IMnrck9camC0FGn1idhujoz2PtGwrdixWOutT5clddqq47YGb7sjil_ZsfPBkbS_wVnCCa1s9e0ew2MbraGD-nmO_nTHTdoH8hVNyo86Ws988jZCJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27053" target="_blank">📅 14:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27052">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPX03NufyTAS4JfR4qOyHlx73Rxac2jZPyH1YJE_1h2mqeoVfPoYqU7_ZD9w89yTsqWY4sndv4dHTCWN8Bihdhzm6O6a_Kayw5alhAKygwnhwba1TH4sl24zE_HOYrRyGWpJgZMxLtCP_7lmZAaQuht4LJRUfqATOMJmxIa_mGoBD2zgaMhel-76Awl6J0EUdk2Q6YvOJ24r3BEqSRXryfHK7BBeMi3BRNpahYAyXt91WkzZJTVtzb3Ys05-0E5SAk06x-BebG_J_Mgx02yB29EQ3zy2FU0j1ziTsrEKSAtodIYxn6qtZ5FijgmCr-wXoyICPJeqLHjmFuvEYoQslg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
احمد گوهری دروازه‌بان‌سابق‌پرسپولیس‌با باشگاه صنعت نفت آبادان به توافق نهایی رسیده و بزودی با عقد قراردادی یک ساله راهی این تیم میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27052" target="_blank">📅 14:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27051">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDtSbk0Wy3W4s2e-V9K3SbNxCaIRq71H54EiA2FuggIbkr5xHBCOtRfFDdYVU9Hvzo92ow0yV6LdgKiwnxX3KvY4EN81VJ1TTbX94hwGrOssxQatNLxRSwRqIAX0ydJb9vZpHrk7qz3etdYAqVVol2qOCICpaXlNFi0iSPiVjJIyCAD1GNLgLeIGM6ku08di0zz6nBi64yFwdIfFGdYWt_W-8QBHAB62OzqM3PVF50OqehGU9WFdV5mx_jeYdQ9HiY2DxaU8uazk5vyiB8s3666ed1xlvd7ZWawhSCKCxdwBdHlxV0jYxCeYT-hr6mXHfkzPrkqFVyoB532SrXv8xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌_پرشیانا؛ آفر جدید استقلال به رامین رضاییان برای یک فصل حضور در این‌تیم 150 میلیاردتومان + 50 میلیاردتومان آپشن گل و پاس گل و قهرمانیه. رضاییان قراره ظرف 48 ساعت آینده پاسخ نهایی خود را به این آفر بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27051" target="_blank">📅 14:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27050">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rz73Trkf8wrlrp3YvycNyrXMtGmbuIua9Q-3AFjFFQKnqTA9ht8R8jVu6_O5_c7dm_Xq0uUea1RrK2G52WtVq-9pwlqelYphSzURnjNzeWSMBogW20WiaMHAu3eVP4LfJzIsTLOdMrzuMJYtXGUAc_uD92n-p6XOwHSHzaWzs3aq4OxoRK-pT7IhU2NPquvi0lbtlr2rEU2jJa2Pju3qSKOf-CqFa9dUifraghlnNM823qFKmSf_2dllwfdTAEUHcyEtpAqydoDo8N8_vY_JE_obcgjFN5PaVpBil5U6hw3A-6XwDFQsS15qTo7jwSZo3SWeCEDc_xsJSXcbx0l7uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ جلسه پیمان حدادی با مدیریت فولاد خوزستان به صورت ویدیو کال و حوالی ظهر برگزار خواهد شد. حدادی امشب به تارتار قول داده تا پایان هفته پرونده‌نقل‌وانتقالات‌رو با جذب 3 بازیکن ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/27050" target="_blank">📅 13:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27049">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dac122529.mp4?token=V30TSmidXx0tBxH1tD9ONR5nOFrq4Os5bZjPFpVzHtJQmBUrkUDZ_utNDLBouY2H1yorMi5Ia3uelpNS8EVWtV-aH2lxd6ATo2ray8rNCRGn-4sjta7Fxy85x3leguxl-prEC6nkWzTDR4HKwpVQoy658tQuiVY1u6nk3eSAIJy2TkegUKW_qC4Jtl578XIhyAi8xxaLOm9rdIO1hqrkGqRcxu42f_2PhCcVQUcwsOG3w99IdVkp2u1DEh4w7FiPQaADW2aHvA7ttxVr8i1Up4QyxKtytghrOcmfL5BpniajEpvBTKzt-yRKERpwK_gOpzgSMk-0SaRY_wLPnOUK3Gkzh2RMkTUjtPGwurneXPJyKR9evpIz_H979U7AvXJXwtwWaFjFkOf6FW-p-3qxVCBTIKlo6lWHYwdcOQhkrNi95J5oPNghxT44zwq7m5wUuZsVzzxvW8V3G_dzpJyUaz3VJUB5k1LkeLTcTuueXdYBNOlTVbIKlVV75dEnlEPCHQXDzBjxIgWjR_37eoOeMKLmzkx9pPu8lJYd4IV_bobIVONMJJHHdEcjrujKl_PieTCEM8iaXvt2PeJzwx_cr_Epsf5VwIuX8WJ5eRec-IASs9LdKAheuVkZ2AOfvlGt-5jwmeS-C98Y-P7C6f6oWrXHP_csP4GRm-Nu5DKYvi0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dac122529.mp4?token=V30TSmidXx0tBxH1tD9ONR5nOFrq4Os5bZjPFpVzHtJQmBUrkUDZ_utNDLBouY2H1yorMi5Ia3uelpNS8EVWtV-aH2lxd6ATo2ray8rNCRGn-4sjta7Fxy85x3leguxl-prEC6nkWzTDR4HKwpVQoy658tQuiVY1u6nk3eSAIJy2TkegUKW_qC4Jtl578XIhyAi8xxaLOm9rdIO1hqrkGqRcxu42f_2PhCcVQUcwsOG3w99IdVkp2u1DEh4w7FiPQaADW2aHvA7ttxVr8i1Up4QyxKtytghrOcmfL5BpniajEpvBTKzt-yRKERpwK_gOpzgSMk-0SaRY_wLPnOUK3Gkzh2RMkTUjtPGwurneXPJyKR9evpIz_H979U7AvXJXwtwWaFjFkOf6FW-p-3qxVCBTIKlo6lWHYwdcOQhkrNi95J5oPNghxT44zwq7m5wUuZsVzzxvW8V3G_dzpJyUaz3VJUB5k1LkeLTcTuueXdYBNOlTVbIKlVV75dEnlEPCHQXDzBjxIgWjR_37eoOeMKLmzkx9pPu8lJYd4IV_bobIVONMJJHHdEcjrujKl_PieTCEM8iaXvt2PeJzwx_cr_Epsf5VwIuX8WJ5eRec-IASs9LdKAheuVkZ2AOfvlGt-5jwmeS-C98Y-P7C6f6oWrXHP_csP4GRm-Nu5DKYvi0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇧🇷
#تقویم؛ 9 سال پیش در چنین روزی؛ PSG نیمار را با مبلغ 222 میلیون یورو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27049" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27048">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjZyqqG6ovWfIiK8s5KT1OcXgCwXTtIvTGrBVPKUMhsL6LPPbTFV4xgfAZHtkzdkp9jqIIhtJol2BGsimX_yTglScyJpj_iuQL9PbZFMga6Zie0tpgl3sk-OPpi-x9HMI40PNrKPmfQP4cHHpFZyyHVKPduI5jCKre8AnghZDwIvggiCG-B7qkp-COSzI94A7fn4lO5DB_tmq6JOvSU0NnPtAiZIvCGN2DEaYYXHOhqYxQKdVDhkgPf-pvvE5B806fU6fwi9hHTjzXE6-Ht8xW9WgGqLYA7z3kVYxyAEGhgG9LvGq6BobYXYu6cHHALxqmh6IRFBEoXjgpgdw4Pazg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باارزش‌ترین بازیکنان بر اساس سال تولد از سال 1985 تا سال 2008 با نظر سایت ترنسفرمارکت
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27048" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27046">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIySToaC6Zt0oSfw7BZHkdhOxaefCA1SeBuU4TBsrxWO7z3j_LVDolXAZw1t_zIMYGOWiQyoZUJattz586Dfa36MMkrtcTQHnM565-5muz58XBMIkHCsjm1cNTR3ZSsZPTM6si1ySuA1VA1Uc1peN_rcghphGTsRDWwRudI1tO9NqzESq-37IVJhGBFuPIffk6MXFRDXlxpBNDTgNhJ5GJig6qYW4wyMx754o-qKTnsxQX4btTNAHTlX2cp_6eaga7yAWJDCCcM0qEWgc2eIuTP2tapSWk0b0npY66IFwCb8qnKxiFopN85cx_xsCEpIAGlNbcg-IoimGchBD5ldEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛دیدیه اندونگ بزودی با حضور درساختمان باشگاه استقلال قرار داد جدید خود را به‌مدت دوفصل امضا خواهد کرد. تمام توافقات لازم بین اندونگ و باشگاه انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27046" target="_blank">📅 12:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27045">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZn78To0LrGK-8dkI1pvRqdoRYW2D3-REQmKirUwGz94k5Pczv9uHe7A26E_2l3E58k1Fi6ZAhOidSvsMMFVPLmnOMB1P6lWaCoak0NiQUxGTdBz4j-Z-SZz8O0lED5rF1uyJoQojCJ_aCqfTybB2gXdBsMltOEUoXBKHiFc0WuxYKeE8Xq9uCnChHXqG_IwFA3FfbN8bNSfYzLmOON2xTK_vnMaWM2MFAWERD7V9f4Lp7-p9b1re3YULZYF7ZybWXFfdPNT6ij87CMAsVlg_hBdMyzEd50S8zusdBF37zQIi86x2atNG5657sw9SjNNjfiJ5urx1Wipeg5-MgnBgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات مطرح شده؛ فسخ قرارداد یاسر آسانی با باشگاه استقلال در فیفا و سازمان لیگ ثبت نشده است و درواقع‌فسخ او یک‌نوتیس ساده به باشگاه استقلال بوده و با بازگشت‌ او به‌جمع‌آبی‌ها او هیییچ مشکلی برای همراهی تیمش از ابتدای شروع فصل جدید رقابت های لیگ برتر…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27045" target="_blank">📅 12:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27044">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7821302722.mp4?token=XkKrS_mWLd4yEp31j2YeZ7YIM0Nc-gKhGWO8sCxcGSfJbc5pWKdapbwE9Xt2x0Xc3Y0rY5ooSQB2d6Lxrfh2EvDG_V-PKTE4EFRmbfYVcpTK2qhhWSxcdy9OpS8lhVbtbUTrGkfaCSXJ1788eE2HjJIZbHD9lVRMqeTMcYoMptdg4QqoUnUYjRl97Pzh_Bp3jrh0g1QlAwcXTB8GBWIhdcZC5PKb64UL7J0UtL5XE1G4HOjme0lxt08V7RHe49Fp6UpOoX0I1R8mG5VqhNaVjKCZXrOeKWhXBEk9j8vl6wneUeT2vvsZ50Tz5vhx22IXhtZUKmXI2nYT2P4DpiPXpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7821302722.mp4?token=XkKrS_mWLd4yEp31j2YeZ7YIM0Nc-gKhGWO8sCxcGSfJbc5pWKdapbwE9Xt2x0Xc3Y0rY5ooSQB2d6Lxrfh2EvDG_V-PKTE4EFRmbfYVcpTK2qhhWSxcdy9OpS8lhVbtbUTrGkfaCSXJ1788eE2HjJIZbHD9lVRMqeTMcYoMptdg4QqoUnUYjRl97Pzh_Bp3jrh0g1QlAwcXTB8GBWIhdcZC5PKb64UL7J0UtL5XE1G4HOjme0lxt08V7RHe49Fp6UpOoX0I1R8mG5VqhNaVjKCZXrOeKWhXBEk9j8vl6wneUeT2vvsZ50Tz5vhx22IXhtZUKmXI2nYT2P4DpiPXpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
ویدیویی‌خاطره‌انگیز از شوتای‌ فوق‌سنگین و برگ ریزون کریس‌رونالدو در دوران‌حضور در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27044" target="_blank">📅 12:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27043">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PL0oS38eKugwmsCWDEM8sNlfz-vW-T-XR4f_j7ILWRWz2bBqAyKvtDvKYb8egAlrgF6UrTFEMdOzmnrfibZYwjHeLyC4g5J2w4SiKLnVvak_Yy4rcfIR5w5ScxYHpaUU8-dEfjfMl-YtZkrqFqJ9rYp8KlmRGcAXlJK7lJG8q-546-LSE06g1onxl-EG9YdNQsaBb15NME32jFn0Kn3f7wlctCS_ds4VBBJxSzFN8M26D1eIeFBpA6FJhddVFXIYUKNZBFSsFswl9wtfu21LgK_KQCbzhbVX0H_qgC4OQrOBXI73vqJCgltl7rCdCKPfOM-ZTw44ePR8g8wte7ABeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ویدیویی‌از تکنیک ناب‌وفوق‌العاده تماشایی نیمار جونیور در دوران حضورش در بارسلونا؛ حیف صد و حیف که به اون چیزی که لایقش بود نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27043" target="_blank">📅 12:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27042">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I84_3mLJkDILSPV7wDf1Ac6VgDoLeHKEx27ekj7hq1f5p5Vo1lxpDm2WMaLTbNarqQjcvtq1xS5PbBWK4mwfdQgVMlK6HDVDg3-oda-_JfaC8sN2vuWfvVrksdJ78ybA-XDYPJ7uksBfH5FdAtxKOHm6LIbXSMJtGF1LGl226pVqIAeAsm7KQrMYd2Nm6U7R2FXdNlqRQXyFbqFVlqfovxPSPCuW7iuy1oxWx-68_UaIWGjAxqbkKm09-fW37sSuru66PxrAuuz2nrQl0lI4gpIx08S-ciBI6rIg7NAx71QuA4FGnJXKnQfQhweh3p0m0scZgtdbsVLhujzKayBmrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
💰
#تکمیلی؛ بعداز موافقت مهدی گودرزی با درخواست سیدمهدی رحمتی برای پیوستن به گل گهر سیرجان؛ مدیریت این باشگاه 80 میلیارد تومان بابت رضایت نامه گودرزی به تیم خیبر خرم آباد پرداخت خواهد کرد و بزودی این انتقال رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27042" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27041">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAcPIw8Y1bXhuTorwDmSVb1IVTO57hMF7-_hy2x-lrm1tM4Q0tOer-NMHOpA98i4tdH85rnTak9WUPYWuLPg_OR9kCWYIJEGt3CfTXdOr9ZFifroS6_8n6QYpEfFG-OSDGJz7blxCrSO1wlXD7YfvQoRaQZoPhtK0-y6FsF2UXGQciPoAARpkycebjR29lH59Rbkf9exE3VndQLei3NGTJCzeen03z-DfsLllquRTuNKoBZbHxR7yr3oYoLR797hO6BOr2mRxUyxS6HfytKg6Ec-omBA5WtJF_7VldfbjG45nK9PeSpRwRKXQ5Su69K_bE1tAXCJaj7cRozgxTpr6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت‌هایی که توی ۲۰۲۶ درآمدشون میترکونه!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27041" target="_blank">📅 11:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27040">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZXxXPqgSzxD2Ffa5l_hJINTh_s4bvCZyJpBCPyOsra-5TPmW4TEh4reh_AJ-_2QZovXwPeg8Y4Y2BPSZgl5CdZaXLbMNuHqaEOcwuFkbFtWBA50el8Z4UpFvut158m-YZNo76sekzkiH1p8UWhgFGt05I2RPHEMVuq2JVWQrecHFpgq0djYLX_qkbs77AdtilMWuwA9EyrYk1TO0Z1NbBSyaJiTy3z5_jC7_pCjdj4WPrhIFnVS8MA2SZARkpRtGzRJMPnzw7VT-0yXOET-r8f414hncmrk31Xv23e8cVciP7OsYsV2_lZ0Gfo371_JLuYthNZUAPJth6_oSlo1pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27040" target="_blank">📅 10:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27039">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7UlTFlGgBQQ6CxeGkqTI-qA7KrXYYVqGgGoWEiCqPjBvjGvVhDEVi6ax7v_p57RDwaeolUWWyeqSRgdCCx_wGPNfAsRCTlmJQZJE6UGydDKCYFoF4282rGlFzKqg3WSCE-MPmaxED7PakF73loPegmtn4CGrsmfbcOtg7RYW8oguWESjf3f3xXZXKLHX3EG5vTpssIDL0j_B0hb20u-v1aZ-Pl8qVuOktiy1ORoFTefXvRmcDAyJMezHR-lP7SvJKm4jYIfayXuT3Ok29mcar08uU1GFpiaVyaIbr_8KLxwY4IsZZgPOeZ6TKmPDCjIuD_BQanAp97lRc0Z5zEXFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27039" target="_blank">📅 10:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27037">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_QeXByqrhRvOIueSPaHx1IMcXqduLn0YdFLNgkb2PIMLRjPVvwd4kSEfDCNAI94EZ_M3ctUUX6ZU1_PeeFBA38ucrQ_JmIcHuwjhUnRtzbbFIctBecow5i9ZAIYxU7RbF8ZzZnP8Xxq9ZI8LMlTw5h3WGu_DlCp5_oT4z0fn8RJQ7RahdF0kWz_evjiceO5qhkznQ0fxPfU-eoqrE-9VxvxcHrx7Ly5S6v3yKxexFJ86X1zBmOME1j3oy__0tpG4FOtocbGioOCT8nEZn0fYBsU2jXUyEVNrCx5eurRUZBLtYvKmC6VvOMecLXd847UeX3JpLCvVO2-QdSq1m8fuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هانده ارچل بازیگر معروف ترکیه‌ای که گفته درفصل‌جدید رقابت‌ها طرفدار منچستریونایتده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27037" target="_blank">📅 10:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27036">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJo2vE3YbKcrSqJcRuw-m1vJp2SVBQqTlx_asp8sKVfgitohpNmntqJkY5nxGVHQLnwGAshowFrM5onY5x5kUHOtciAxM2GoFyKVHhSntGrNdl0e5eo5hYgAJwLh3z0YsKD_WhsS1uiF01LmJofVLkXgoFtD8sD93kdb1VEyF9Voys1x-UK3KwD-djWZhLj_QpOvcqBMqDt3XWrm7O_f9sTKxTJ41CfRCUnjo8Z_93f-DyiaGsCn4BKKl4Ss_8H17KPcIN0pQLwcXGUjZjV1arahqz2y-lnWzX01BWD40ykmzHI8KpKD8ZaoweNNw3tdBMdMrAU4_nbF64EZoVBy5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27036" target="_blank">📅 09:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27035">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcvIOrHAll4PupLevg6R_OwWendYL8kk9K1wIg58RIrTOfUjPvpejX2cSs1uKOErtF_UteZ7uc1EJ7lBh9QtSUBYox_Zrlk2uHXrFK5pSYKMnxjS-cprJ5eib8iDgScZ0eJDiLqBmpYlbchYhyKUml7v48lnhp3MF_RSUR9MNJeCi_vVWMAvmnf7_qLlBHX_3D7r_yyLP751NIBPXyXxXpxoN32rpLseEuWwPw4DiUUAI1BQxiqWWMkTz9Q5Sl259-hMSzFScggU3L9r3ED-9voUF5322iAnr7pxs36s5pO5FLIdRFRjIOTL1Hw-gbCz14-94DFIzRk9K9UgtyY4sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27035" target="_blank">📅 09:46 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
