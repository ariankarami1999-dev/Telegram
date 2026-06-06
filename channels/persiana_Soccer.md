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
<img src="https://cdn4.telesco.pe/file/r6I4cdydSYO42GBGHRdQjjk7g1N8eAAqamNc-aGQSkFTe-1oAQ_nGMDQDCu9eXyGWiw04m5qGww-yBCcOwNjDsjCDLxmKDDL7eAWtj3q2fG2saNl0W5y6lziIfCnJJ03b6rG6jqImFdDLPzML_oUpH-JPLJHh268aAyHjfz8EWVgKFW12jfhdxr6OlMxhFiJhVKyzxdDUjR2ojH1QMMmjyOOtM3nZK2XUY7Zr48Sd78EilbQNZkC270__tXFqdhTXAufFQYrYtl3QgHYVWgUK9omHi8bO0UTtt7fIga1WdBbH-UC-qp0Q36oWdvTuXyHl00T8nl3VjZ6A_0fod38WQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 173K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 12:35:58</div>
<hr>

<div class="tg-post" id="msg-22873">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ag9p55ZH6lgn0KqcMoXyibAKQ5FWZ8HOK9B6kfHnATY4k1Phxete2HxwCxRCJETfL0hI9rQY51xuU2Egy0EO3Qb5XtHbUAoiQiOXIguiCqyMJ4xluEOlOmMmq6SmeeeqL3Xh4fMhgnxmK34h7ZQOXCIMx-6e5rpzIERueC_oB5LZI8YYI0oSGgYMx2uU7LKF2COCUfYYzoTO_QXkzKc6IF3wjeJmnNQWJeSsoQEin0LXcjU7Q6Qn4NZLoqB3arl8vkyBMXfXO3KtOTVxWmN6XmYKrUlFMs4ScWr3bEkDUsxKOgchdIteSuQwgl6xvwDjkcjoUreGdDBKVC6sGIVP_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
#تکمیلی؛باشگاه‌آلومینیوم‌اراک: در روزهای اخیر مذاکرات مثبتی با یکی از اعضای هیات مدیره باشگاه استقلال برای فروش محمد خلیفه و بهرام گودرزی دو ستاره جوان خود به آبی پوشان به توافق کامل رسیدیم و به احتمال فراوان این انتقال بزودی رسمی خواهد شد و پول خوبی به‌باشگاه…</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/persiana_Soccer/22873" target="_blank">📅 12:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22872">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjfpbMmFsbNcAhSwclbNMYnPz8Q5rGW6S7lR-93ULQb_JA7qQmUkj_xQ9CtrMhclTKsHb0PiECf2DbPg6UfgkM69AkEdzai8oC1c2yhc9_q8lGK-zgv4eB8F8yg-ZKUNZ4LZ1-K_dZeZuBWq5Il20--KDNGJ0sBdPCoXsa5oHDkb-S7bnxVc-DbL-paY1WYiU4-phrN7q3r1EX6jlfJ-IZWuZ58YoVkbi9e5X64BpeP58PUALo99UWfMRJCFJAScJfqb5RhPMLVgHlHfpuiMxEmdQ4QJjp1SJ49DBzZYuoPT1maApAnQmc-pTFBl2aIrorI94Jgr1iB5E5PaayJlXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل‌نفراتی که دولت آمریکا براشون ویزا صادر نکرده و گفته حق ورود به آمریکا رو ندارید.
‼️
مهدی‌تاج رئیس‌فدراسیون، مهدی محمدنبی مدیر تیم، هدایت‌ممبینی دبیرکل فدراسیون، محسن معتمد کیا مدیررسانه‌ای، مهدی‌خراطی مدیراجرایی، مسعود اردشیر افسر امنیتی، مهدی ملک…</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/persiana_Soccer/22872" target="_blank">📅 11:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22871">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWp4bqY8rXhKjuFFyB7IS0rN6FI6WqrBa2RTXd9946_yOS9w4Q24Bi5Ccic5WFrCxc7YTx98rsBIZa95M0Sw7N3VcV1j3srX8KlWb6GEafz-_oyoxvd0ez7-jpV9Necxcpc_KqAmWkvGJ3HiDa3mIA5PqZgVHzVYgRxvm4WNEgpHKRhbdGCVCeFgeBnMEG-j3XuflwQmzEzsSt7LFYENHGdkT4U-Ih0TZZYE49Yw0soYCr196VzZbse8HE-Aiz8dT_eGp-xZ-QPBxa7s4BXVRcfp0iK-7ldo7Dd7nRjoMMBUxJWwb4e6fZ_2H6FYkRmYBYNR81B6G5onJJafJUWAtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام رسانه‌های معتبر خارجی از غیب احتمالی چندبازیکن تیم‌ملی ایران در رقابت‌های جام جهانی 2026 به دلیل عدم صادر کردن ویزا از سوی دولت آمریکا به دلیل خدمت در سپاه خبر میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22871" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22870">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35d2a48cbb.mp4?token=JHlMRwMMaGMQ1TsMq1fJSsC8e6VqhKFLmXwPkkruRSruz38NGnpFeFvyFGtBj8Ne8QWG1GDC-LW_lf2wKNQv9Gf5tF9OM4p_EU3VhIvbm2n_nsuZQuv_8KqUDCvAq2kKUbviV3_lnE8e_Kan0wCr13daa4Y-I5BD2jyFTLwX1u8JAYFV9gxOMB1tMxHJ5RL6K9uJ3U5gKxbgESJcX9U8kAFfz_8JsYFaxvSMZ8Ow5RPEe8DtyWwve3Is-ms_iRRL1rLMecJDjfbMhNQoYAtw6ox2D2RlsJbRgiQRu65p2lbvc5Fgp9_CL-kB3BlyD4IeVxVVqiEt06WyOHyBvK3zxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35d2a48cbb.mp4?token=JHlMRwMMaGMQ1TsMq1fJSsC8e6VqhKFLmXwPkkruRSruz38NGnpFeFvyFGtBj8Ne8QWG1GDC-LW_lf2wKNQv9Gf5tF9OM4p_EU3VhIvbm2n_nsuZQuv_8KqUDCvAq2kKUbviV3_lnE8e_Kan0wCr13daa4Y-I5BD2jyFTLwX1u8JAYFV9gxOMB1tMxHJ5RL6K9uJ3U5gKxbgESJcX9U8kAFfz_8JsYFaxvSMZ8Ow5RPEe8DtyWwve3Is-ms_iRRL1rLMecJDjfbMhNQoYAtw6ox2D2RlsJbRgiQRu65p2lbvc5Fgp9_CL-kB3BlyD4IeVxVVqiEt06WyOHyBvK3zxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
اجرا‌ها و موزیک‌ ویدیو‌های شکیرا برای جام‌های جهانی ازسال 2006 تا 2026؛ کدومشون بهتر بود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22870" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22869">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">چرا این روزها همه سایت جهانی
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🌐
اسپانسر رسمی لالیگای اسپانیا
😀
مورد تایید سازمان Gambling Judge
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22869" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22868">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGqjepSpcevt_l0Pb2OOWHxk301yJLdkv1YBXNhVhqX6Nu2_-Cn_CwPaSXobn9n8LvlToyzcJjen9XiBE3zxpAb-3U_e5BGGqh7VV0oMjxk4Bup2oQCN_Joite3n4W3ZJgaeyWbO5yrRDK3L8pWcMHgj9s2oC4SceVejqjeib752SfDDPQDJqcsrOSWm0Se4Ov3Rqi0HZCbjWZYApQqYZ1U5DUCjUVZhvgCyeclSaGvynH4-pQC3t8zGKGm0F95uO8n1MksPg4C198TV1EsCWUkaQ-gS7MpeFjQEaAli7xlLzNG2zTSYfA5O4LsKb9ek7OHnCVkiBz5R6yJCJi8SuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ظرف 72 ساعت آینده از لیست اولیه اوسمار ویرا برای‌فصل‌بعد پرسپولیس رونمایی خواهیم کرد. منتظر جوان گرایی و عوض شدن شاکله سرخپوشان باشید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22868" target="_blank">📅 11:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22867">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwqvX3O5Zzx4_YhUUyCf5yWhNQX7R_6jiZJng0KzKkz111bovYG9yh6JbaRPx8JRir5FT5uxiqBWxlV5G8d2wPqT2IWADK8bkPBC2zam9Qd5fUy2Fm4Q0aeWbO5mPmXlUasUpXktBuPKuucWlnDZpKwFr6TJAu3TO9hMtNeJEeT7nxADC_ipLylZh_Jw9VMKTMz9USG7S2s7g_2YGsfWmC4J6xF-PWUneGi7zLmdlehYfr3Kssvvnm3M2lciXB7bLoYW1KE8zPYQylXz6CZZGTIv7SYHd_nqbQxvh_89RYZhbCnA3LBfL3ifCcy2nR6sEHaHflvmxXE_jGC_94UnsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/persiana_Soccer/22867" target="_blank">📅 11:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22866">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=n9dvuL9oLxi3xHWgiqutKrESKOo5EqHHGOZvbo2H-axSf6ZC20LUMKLfaEScF5-8VhUmVrPAiiQbLxPbyTc-_MKp_rjLnasPT5DGUQogM7Ft2BNCj-OKZ9VYuDDi6KXp1xZ7uOP8BIQTuGMrYoU7WJncXHzoJPaf9UFR6sO0Zwtotgy5fGgRgiuLKj_67geVOe-9zcmHnSEseVpmA06JcwI3jP_rP2_ca5ZNLTzQndugdy-Zd8w8mKS9B5mSQjRmh93NMRXkRnyjyFe9TPA24WF8pcgCmvEYMRM1pHZnXUL0V9tuFJJRvhbpiCSN9Fe4jyY5SS-TXFVMSkGXbhwJEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=n9dvuL9oLxi3xHWgiqutKrESKOo5EqHHGOZvbo2H-axSf6ZC20LUMKLfaEScF5-8VhUmVrPAiiQbLxPbyTc-_MKp_rjLnasPT5DGUQogM7Ft2BNCj-OKZ9VYuDDi6KXp1xZ7uOP8BIQTuGMrYoU7WJncXHzoJPaf9UFR6sO0Zwtotgy5fGgRgiuLKj_67geVOe-9zcmHnSEseVpmA06JcwI3jP_rP2_ca5ZNLTzQndugdy-Zd8w8mKS9B5mSQjRmh93NMRXkRnyjyFe9TPA24WF8pcgCmvEYMRM1pHZnXUL0V9tuFJJRvhbpiCSN9Fe4jyY5SS-TXFVMSkGXbhwJEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تعدادی از هواداران پرسپولیس مقابل فدراسیون فوتبال جمع‌شده‌اند و شعارمیدهند که پرسپولیس رو به جای گل گهر سیرجان به لیگ دو آسیا بفرستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/22866" target="_blank">📅 11:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22865">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">▶️
هایلایتی‌کوتاه‌ازعملکردخیره‌کننده مایکل اولیسه دربازی این فصل بایرن مونیخ مقابل پاری‌سن ژرمن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/persiana_Soccer/22865" target="_blank">📅 10:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22863">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9211e2c5d.mp4?token=W7f26tCz4eflC814D26QbWrvtGEjd1zRmG-y_ktee3RJRDOX6OQYUFAAqzuzOXjwDLjawq3IB7XMjc8wswzeIetuAawBb3PZ15Uvs10GO3_7EHD0SM_n0O8izYnobDrTCa7OT7QkZVm8yhIq3ZxshQPkEOSt1rwFgAhklSTSGJZga9jOlH47TdAJgpD_3NgmAdBk8ZlHtbHOGMcVOuwcxVdzOftFw0HVHs7qBxvS8YN0bF_BMAPNjHbqKWZ4aOJroqNFjWnrGN8T2sV2qpgN93WvdtIsHmo9Jlx84NdOwP1i42E6cN8eAYFqD2e8yYsrG4lG6mnWwjJLGbYp2lne7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9211e2c5d.mp4?token=W7f26tCz4eflC814D26QbWrvtGEjd1zRmG-y_ktee3RJRDOX6OQYUFAAqzuzOXjwDLjawq3IB7XMjc8wswzeIetuAawBb3PZ15Uvs10GO3_7EHD0SM_n0O8izYnobDrTCa7OT7QkZVm8yhIq3ZxshQPkEOSt1rwFgAhklSTSGJZga9jOlH47TdAJgpD_3NgmAdBk8ZlHtbHOGMcVOuwcxVdzOftFw0HVHs7qBxvS8YN0bF_BMAPNjHbqKWZ4aOJroqNFjWnrGN8T2sV2qpgN93WvdtIsHmo9Jlx84NdOwP1i42E6cN8eAYFqD2e8yYsrG4lG6mnWwjJLGbYp2lne7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کیلیان امباپه: همه فوتبالی‌ها قبول دارند که رئال مادرید بزرگ‌ترین باشگاه جهانه جز هواداران بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/22863" target="_blank">📅 10:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22862">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3KD3Dn_nYakEInwEvZLxrZ4thmZWAezRinF0o0mHT5vzyMRG4C4v2W-_ojTmpy0G4lHrZWUYFjkKV6yMvPELXlacJ7I96OJfug-levGz2znzZ6jCCXRynCCsRjBJ7E6ZnwDp1IrrjxZnzzM9lGj3Z6dlOMiRv30IGnhcBWQ_FspMyZz-xTOIk-WZw4nd4VmYpG4Ln-QMI3GtyZyy4N8vDS-YXrlHfGbTtU-6ZreJWFjnkO8xujkHYgcuOSTfDmCox2SsHHOr3s4IUv-om_fp_yUU2oZ-c0LHc0Ew0JM6q3BPdIXElI96mc829geLBzgzfU7gNP4iUJKAfcudrP4dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیشترین‌سرچ‌های‌ایرانیان‌بعدِ88روزقطعی؛
بعدِ بازگشت اینترنت مردم اول دنبال چه چیزی گشتند؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/22862" target="_blank">📅 09:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22861">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73764a80a.mp4?token=lqHmpen5w4EqNJF_nnBRjvB48a8h2KGVSPVEiqY1dMgrpUymKMB7vGfhoxo2wIlXw_8V7EKzl2FH4LkG6wjmWl1WhPKPC8Ljy6yObEM3Xx8X7CezsQpjG365rN8hIE5AoAY-cLOCJ3jcB14IQqf-aMBkEtVToFtkc_ozwIwMprW8oaQDOjQ2yTZRU8kkph1MrKX-fw_zteWozLRPxtdhMxbGPojQIytFXnTYOWpmsSavhCzNQVUiezLYgmNZLgdnCaSQHTjapdJ8q0yAHJvUw2eSCu1YIJIeuYHOGXynt3N-KE9gxKyutRsXrnAsKqS16f8AVRTk0Q3vjcmjhThMhaKT4_Zrmku0umCwKNdcfuGLPa0Sm1OCV3gOiw76oieTjra4GqdIncSftxeijc3ae6oe3PvfF5T8SARH98v9ejMg6G1K9-o5_TLP6kgseC72glevnoGeruwB5ummjlMOqrf1PkTWbKqnR2eCdGBo5r96mGt_xgYu_GzBRmi90ReZ9HaGWKFPQXEVzjbRAfF1tVz75pkZCbD5ZTjlWPu5eqiKKqq41UxcsBSggD4EgF-N0OX3XNwQFLmq3IiMT_EW82xEiB31ZbifPGsbBO9HblADeNNu2RCmsPEqswWCh-T9QUvnjkclEJNq24oXyip4XTXXLfDMkzcQzQ1lPKfMNRE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73764a80a.mp4?token=lqHmpen5w4EqNJF_nnBRjvB48a8h2KGVSPVEiqY1dMgrpUymKMB7vGfhoxo2wIlXw_8V7EKzl2FH4LkG6wjmWl1WhPKPC8Ljy6yObEM3Xx8X7CezsQpjG365rN8hIE5AoAY-cLOCJ3jcB14IQqf-aMBkEtVToFtkc_ozwIwMprW8oaQDOjQ2yTZRU8kkph1MrKX-fw_zteWozLRPxtdhMxbGPojQIytFXnTYOWpmsSavhCzNQVUiezLYgmNZLgdnCaSQHTjapdJ8q0yAHJvUw2eSCu1YIJIeuYHOGXynt3N-KE9gxKyutRsXrnAsKqS16f8AVRTk0Q3vjcmjhThMhaKT4_Zrmku0umCwKNdcfuGLPa0Sm1OCV3gOiw76oieTjra4GqdIncSftxeijc3ae6oe3PvfF5T8SARH98v9ejMg6G1K9-o5_TLP6kgseC72glevnoGeruwB5ummjlMOqrf1PkTWbKqnR2eCdGBo5r96mGt_xgYu_GzBRmi90ReZ9HaGWKFPQXEVzjbRAfF1tVz75pkZCbD5ZTjlWPu5eqiKKqq41UxcsBSggD4EgF-N0OX3XNwQFLmq3IiMT_EW82xEiB31ZbifPGsbBO9HblADeNNu2RCmsPEqswWCh-T9QUvnjkclEJNq24oXyip4XTXXLfDMkzcQzQ1lPKfMNRE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
#تقویم؛ یازده سال پیش در چنین شبی؛ بارسلونا لوئیز انریکه با مثلث خوفناک MSN در فینال لیگ قهرمانان اروپا یوونتوس رو با نتیجه قاطعانه و پرگل سه بر یک شکست‌داد و قهرمان این رقابت‌ها شد. این آخرین قهرمانی آبی اناری ها تا به امروز در چمپیونزلیگ بوده است.
⚪️
…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22861" target="_blank">📅 01:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22859">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvWXUl9u7LKfSNid6Bfjp5C7w3AWyWhgy2KEp6jHLwrjgEhPg3uQnFNlL_MkkPFPJ73cs00hiUoW5iNhTw8Mee4fuylwgmC8KsVSH-uptuH0-qxZiqBXuh0yfHIMbKEEI2HyKa7yheQU_k01CD46a1kxCCeAnszkIKIcpmdg1MQP6U6kgEcpBEfPVgx9X7H-brlqi6SDX9TAkwl5p6er5mBFy5xiPE_IOcjlMMlbrqJbdSdfKcy95SgN68dsgBQ2qvvsdIXh-UgWaYI_kG0frwum1D3CXsdzniNFgbwQ7VVasHrtPYMG-fnAjrVrLhBL5OPJTp7nkk3Qo2VkKkCcig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YVj1Ro3fze3ZaRcQN9DHdnCXjjOhk_kUq0xupB1Fw-ESCAITZ_AincdHV7kZtBWLiWKSoaokNcOm7T_y7bMMLErhw84tCYNOOuslww7941btqN19yePUHDR37QNrYmKUMWVZ0C76iUXdaTFgGRhS8r45pS-WwiFnHtBfcvCqv8sSRoCGkyI_nkRpVzNrylxCS6TCN8rQbcKg7iimGhBbN_tyWfmdYcFaFcWYL26Kap_mexCt0prskaKcXZADn0WDO0YZdd2DDC7mSUvKP_P96beVsZn_BUXN176qmBtsAEHmrwfSLAGJNgODWqq8qt5sec7UIa03lTlkQNsD1ckm5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
#تقویم
؛ یازده سال پیش در چنین شبی؛
بارسلونا لوئیز انریکه با مثلث خوفناک MSN در فینال لیگ قهرمانان اروپا یوونتوس رو با نتیجه قاطعانه و پرگل سه بر یک شکست‌داد و قهرمان این رقابت‌ها شد. این آخرین قهرمانی آبی اناری ها تا به امروز در چمپیونزلیگ بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/22859" target="_blank">📅 01:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22858">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxbe76dDtgfdWKJq-5pDYWZoZro1OowoMZOO-0U7idsmRDolVYgDU5TXI3XjJjJp2svl0GopClCulqWuguC9NYmvuBEje7lLEcUzrCFbXtK5jH_fBtzRifnQxRXvwguvCWFXjiEWzu9epTQWadPA4QHhYjqSBt4dUVWVMZYcX4vcLw0Vq-OGttT71ecn_UMjTD8Q5tE9M8DCz989fXcnNb1tFlpvChu-ZWGjGSVQkR5dfPOAcMzOP0j9-GK-uIXaP6R1wN06sJ23wbUI_mKFrlc978KSFG9NRR4C8jHf9fw4H2m9PWGwJXAD7LVRCZr4TxlAaSDwh2e3xFQD-iP9UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌کامل‌دیدارهای‌‌‌امروز؛
ازجدال‌یاران رونالدو برابر شیلی تا تقابل آلمانی‌ ها با شاگردان پوچتینو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/22858" target="_blank">📅 01:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22857">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0I7b2C8DzHbpBmo92lZJZJAJU9tFWBurYZwFtnz4AVdOfo6Tj_JKay3YxIURHoz5tIQF_SRpNdPI0LGGpHnbBbI2ho5AJTfx7r9rz7JjQ_iM8kF4yeqt8T9s30nfp9bX9Cs9cLWwK2JQLTUo_Pg7N6K8gKHq_Iqizaoxs6cE_lnnd18zC46gTnZGEEn-g96EK3YNDBdks0wA9oOM9ke3cHORcCV3pgtC3DUPuhPQuvlSRg55iNsgLVXRc4AO7P5qPLVVuhy-31r4FHI9y-IJ7wQuPJXW52ZEvmYSDTN5y6HpqxrsONfThKR79ZnQoYLiS52yNx8bnpVef4Xyedauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌ روز گذشته؛
استقبال مکزیکی‌ها از جام‌جهانی 2026 با جشنواره گل برابر صربستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22857" target="_blank">📅 01:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22856">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grxtckkKbczK_Vyiu-Cq3hkLPJ_7gfu-E_RAaMAiglfX0I5lLxM3M9wu1-EyB-52mTS83xnlKt0QDFFbHlSipYa9IXyu365oosy8Xf_-XH9vvJJtl2K9gV3aFgOwji0xQTrnmQqNs6qvDf4ct-5Czoq39UyDYAWQ3822rfsOOWkJGQoT1w7il2K0_ZWNUpZDkRc40HehrthEX4eIeRCVKmDRXzm6xxEDwGFAQV27uPCVzEWTFdPOn3RwJ_DkPALuVOKOZGZpHEe1lbI0ZWN74XvKCfb0t6Yp7LMPGnm_Gc1u5C0eqp3qJ5LROiHgglT5g40Xqfx4bHS6dEE-4xTJbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شوک‌دراردوی‌ژرمن‌ها
؛ لنات‌کارل‌ستاره 18 ساله تیم‌ملی آلمان درتمرین امروز این تیم بشدت مصدوم شد و رقابت‌های‌ جام‌جهانی رو از دست داد. ناگلزمن سرمربی‌ژرمن‌ها بلافاصله آسان اودرائوگو ستاره 20 ساله لایپزیگ رو به اردوی تیم ملی آلمان دعوت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22856" target="_blank">📅 01:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22855">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqwoczyQp0iqmK5wNCWxPod5zT8u4BnxJbvpF9YaZAVIsSqsx-7bMSFc9fGA0g_jViB2D667fjtHbFDFO_kX0y369IsLtx1Wulxmfz2llxpwVfmXuu2zc-tWM_BxGT2DFXHq6jC37lAfqAvFPrPURIJ_jxMgjv8DfRteDpQFF_qlSVh6p_GxySuj-bvT9d-emBYBCsDIzSOl4HGobouQU7h_PAG_QqFrHa0_KjWcDphvLBHR0J7znBpthhj03yJ1MT5UN0lRZ9Ptq530Weia6GopJprn7K-Y3Q3OZHk4wlaKuao5SqpLkATvRb6n1Iim7EZdGlR3InKpjBAJpMuFOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛طبق شنیده‌های رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره ایرانی ماخاچ قلعه بزودی از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22855" target="_blank">📅 00:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22854">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moXOZdWmGZua0El7pokyHMObL71dk96GLOZBKDGW-84RRnWuFSVsf2xD7J4Pagmi6T41Ra80caIH5-pxxsNzhnigDMRnDr8RtqLBKW1X0FIl1GlGKwHY3ntxPqmH8qR1AYd_zXKzNNAc_WEuMZ0TK49La61Hyuo7xmR09C4h-OOQTfvIO8haZMQOXxQ9wGVzgIzhqvODVWQfPJ6xoP48PaJueKy3z5f3fzf3COPcLPGnhETne6qeswZRitSs8dAAScKxhy3TMkAkqoPF6Uss5h4yXMvSliGBdpTh9a7oK7CBbSzHMLdpbRi5Z3BVWFQP2v4tevEiScmHQItC0pzwCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چت‌جی‌پی‌تی،دیپ‌سیک و گراک بدون فیلترشکن در دسترس قرار گرفت. همه برنامه ها دارن رفع فیلتر میشن جز تلگرام،اینستاگرام و توییتر؛ سه‌برنامه‌ای که بیشترین استفاده کاربردی رو دارند باید فیلتر بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/22854" target="_blank">📅 00:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22853">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e00cf6e9a5.mp4?token=BKdIxgA5xJM4Z6hiiOhPEYn6hTdfNyDKSWXoLWRlshdzm5HhmtRmBUx5IZI2lcHJywveT_anURyRWHQAUCuEb_YItCgfzEhkwW1WgUmE7cQF-9j90YPHU1EP5cCJaZsgew2wFyL90lddyAp0h-dnx9tgGkooa9XVQiN6r5yxuoohauC8leIIVEpJyc0cCUHgfriDUrzvQyJneFkH_xDvo7CympEQe5_sd1CDy_M9wFc420srAaaQR9SNX3vsD9X0dzX3uPj7FY34mu7sbgmMwiwlmQFl4e1KugBNaVRfUX68QMS7fiZx7CWtl-pHIKJfGw2dLkjiev8otKCCQh1GYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e00cf6e9a5.mp4?token=BKdIxgA5xJM4Z6hiiOhPEYn6hTdfNyDKSWXoLWRlshdzm5HhmtRmBUx5IZI2lcHJywveT_anURyRWHQAUCuEb_YItCgfzEhkwW1WgUmE7cQF-9j90YPHU1EP5cCJaZsgew2wFyL90lddyAp0h-dnx9tgGkooa9XVQiN6r5yxuoohauC8leIIVEpJyc0cCUHgfriDUrzvQyJneFkH_xDvo7CympEQe5_sd1CDy_M9wFc420srAaaQR9SNX3vsD9X0dzX3uPj7FY34mu7sbgmMwiwlmQFl4e1KugBNaVRfUX68QMS7fiZx7CWtl-pHIKJfGw2dLkjiev8otKCCQh1GYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ابراهیم کوناته مدافع جدید باشگاه رئال مادرید هستن دربازی روزگذشته با ساحل عاج؛ واقعا مدافع قحطی بود که فلورنتینو پرز رفت این رو گرفت؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/22853" target="_blank">📅 00:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22851">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYSxX4nUlH4JvAKib2UZ0r3PXf2ajZmmCPG_GUZk_2BOOdnIpvb4835WnJcM5q-y1OzjQVlQ5CSWpkWJtULUwn9Xscmn-2RGOWz_BYRERfVH8F1zNFt6ofhHPZCW669Fwdwuk2TaO5JW1e_Z4ohqu_8sc7ZpWrfGqP5CRvnBcK5eVnpG6E0HQNh3DPaKIb5hr9I5XiDo3y-sYvcOb1dai_hk2dubO0n-XEFMFJQuukvkO6HiXc08JAuEkn-Pvopz-fWRNDfpS5wiXeQgw21LfEwS8t7OkQpf5nTapC3gMqo2RLE_DEb_W9GgWfnGdL6ASfhJ_88F5nT07XtZVCXevQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
علی‌‌تاجرنیا رئیس‌ هیات مدیره باشگاه استقلال: یک‌‌نفر از اعضای‌هیات‌مدیره تیم استقلال در طی روز های گذشته با مدیران باشگاه آلومینیوم اراک صحبت کرده‌ تا انتقال محمد خلیفه رو نهایی کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/22851" target="_blank">📅 00:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22850">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZ5DYk-uCAp-xJJsR0ovcPvA3hXBBazUe-kVdIDMjHZNe5R2bxZHBvvZeowQo2qyAntr8w4Be1ztOQj2ifxoJ9EWcQmok714VkAaSrsmcW1VcXDWhzKZ-9KhX2JUCfUEt9RktcCSj20fa6k7MtLhOnEvpNlOwNmBZwBI3_iB0YQ7AE42_wA03pyn_LfE3OEOFoWPbobmv2czQ058MuEvsabPInsIZZtfvQfsMPegOgkNwKpOGZAwST7IOPTwyzEd69sJv8ZFwvCmGidJZMQhfnX-3l4k039mU2kyGYkWPyjx_ZqVn7mI0NVdyA7ckUhJOxzxFmF1xn0HM8uUHvIsqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22850" target="_blank">📅 23:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22849">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aedcb21ace.mp4?token=nrctwEdoF1iNq670drOZ9L1YMie2qih-ZH6lhHr5TwVZguTwhIV9ajhMAwM8RxFBNUxBcK4Du2hMbjdn_31iHRLCH0oX5UyubZauUW2dS5pVTtpYBgNaiTJkZoWERhhxFdAHoiMtG4Wr1PNLLUJnK8j7kz7jjcAvvb1kNy6MGrBo1t4VDx9bhbJugdEtXGnOlnQdgKDcfCBrmkCS6wCg5gjb7jvRktaAwCs3dGNNVUR-w4sKB14u_d2HvUPRmJxWuWZCA0PZBzyk7__RfjRfoBX-gmSjpkJ5uOofKql8cQnuSojQOuX-oUtAixMpauT2TmQxxLA_ZzDJ9AAYqXCNAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aedcb21ace.mp4?token=nrctwEdoF1iNq670drOZ9L1YMie2qih-ZH6lhHr5TwVZguTwhIV9ajhMAwM8RxFBNUxBcK4Du2hMbjdn_31iHRLCH0oX5UyubZauUW2dS5pVTtpYBgNaiTJkZoWERhhxFdAHoiMtG4Wr1PNLLUJnK8j7kz7jjcAvvb1kNy6MGrBo1t4VDx9bhbJugdEtXGnOlnQdgKDcfCBrmkCS6wCg5gjb7jvRktaAwCs3dGNNVUR-w4sKB14u_d2HvUPRmJxWuWZCA0PZBzyk7__RfjRfoBX-gmSjpkJ5uOofKql8cQnuSojQOuX-oUtAixMpauT2TmQxxLA_ZzDJ9AAYqXCNAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه پرشیانا؛ باشگاه آلومینیوم اراک اعلام کرده‌است‌که هر باشگاهی محمد خلیفه رو میخواهد باید 100 میلیارد تومان ناقابل تنها بعنوان رضایت نامه این بازیکن به ایرالکو پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22849" target="_blank">📅 23:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22848">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e230120d7d.mp4?token=iZUYuSwWDO4PIBInTdjRW1zjtNdxgsmKqzl6y7yUgomMnG3fpnQLbdWiLjya5wdXkZe4pFHGpfEi_V12TObapxs2Km-iJ1UOQ9Rlhiaoc-I1EYWvOkN4h9uai756WkpynBqz7mtadXHgaNDBXUeIfGCImxlkoMg7_pzIasD56VRHmKTXiJj_0c_Bz1SXGGZg3l0VPezeBsFtrP8aVtmRjxFFwrNYfcMgwgNX96_p4QrLTSyN2EsICDVIP63x4vkjkTa3fQfc6ntcHFFcVF-9SbnN_kNDpPRNjDvefR3I9eWI0dXNVPemMS3b6F5XK5t4OrFH-8AvD7fONjHvu4HHgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e230120d7d.mp4?token=iZUYuSwWDO4PIBInTdjRW1zjtNdxgsmKqzl6y7yUgomMnG3fpnQLbdWiLjya5wdXkZe4pFHGpfEi_V12TObapxs2Km-iJ1UOQ9Rlhiaoc-I1EYWvOkN4h9uai756WkpynBqz7mtadXHgaNDBXUeIfGCImxlkoMg7_pzIasD56VRHmKTXiJj_0c_Bz1SXGGZg3l0VPezeBsFtrP8aVtmRjxFFwrNYfcMgwgNX96_p4QrLTSyN2EsICDVIP63x4vkjkTa3fQfc6ntcHFFcVF-9SbnN_kNDpPRNjDvefR3I9eWI0dXNVPemMS3b6F5XK5t4OrFH-8AvD7fONjHvu4HHgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ اینکه خبرمیزنن پنجره نقل و انتقالاتی باشگاه استقلال بازشد زمانی صحت داره که درسایت استعلام فیفازمانیکه‌نام باشگاه استقلال رو سرچ کنی بالا نیاره. شماهمین‌الان هم نام باشگاه استقلال دو در سایت استعلام پنجره فیفا سرچ کنید بالا میاره چون هنوز بسته است…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22848" target="_blank">📅 23:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22847">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtRGVTCm9ikfXxsX-nEz24lpe77p3xU8pXKPLMKaR_JJTSq51anmVc5en0wnFxh3dVEm4HGG2fACh2m_iGKFTd_DB2oU92TRzhl_7ZwU0r6GU71JTcgO3cO825yiIb8BMugMsnaW4gFHKI1cxPkNv24nL56Ac1nC8zbL2BdezZI62C5Q01wZrlKsXMw5aG8ExcIOvBZaUCUbmx7FkjnbN5gnE7OKF5dLmYMLjDAACTxjMbxe24ALgBcEzt2bck2wl_ySnwWx1JzuXQWm_YSvxRGV7ZCzaimn3nzsFsidhbmxha1nyYRcQuSaqS6j_5jNuefAeh6xfNvEK0dqW_5ceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کیلیان امباپه ستاره رئال مادرید: به پیوستن مایکل‌اولیسه به رئال‌مادرید بعداز چام جهانی بسیار خوش‌بین هستم و امیدوارم هرچه زودتر این انتقال دوسر برد برای ما رقم‌بخوره و اولیسه رو بزودی در تمرینات رئال ببینیم. او یک بازیکن فوق‌العادست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22847" target="_blank">📅 23:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22846">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">▶️
انتشار موزیک ویدیو جدید شیدا مقصودلو همسر ایرانی خوزه‌مورایس‌پرتغالی برای جام جهانی
🔥
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22846" target="_blank">📅 23:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22845">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa70e9e949.mp4?token=UBZ0kzERDQoF35Ms07Jk0d7KYB1r6Xjby7Yg5_LfIZGYHkeWrmDNciN3J8jBkr-9dLnGw-ZrlI0jTzw_WHIrNvuQ4yHYI91DC9jBA_WrytT4woAFqvdWNBM3SfjgZEXmSmmHjL_npak6D8arCqbuUEFJe5rNiVH49O36lS5RNoIDDjJdHLBS1OKRG9ocg6qxIjDhCBaiDZYSk01aRcNFZmU7kXM1tOTW2n-hxEKpmAhW2daKhDug1MCEFyYJ886hKKq_2XifX3Iir9ei4eNlFBcAkFvx8iqGLFsyMthxvs9c7BASG-L-s6Ifp72Qhfj5LL4MQErMXGjhYRZWKh545Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa70e9e949.mp4?token=UBZ0kzERDQoF35Ms07Jk0d7KYB1r6Xjby7Yg5_LfIZGYHkeWrmDNciN3J8jBkr-9dLnGw-ZrlI0jTzw_WHIrNvuQ4yHYI91DC9jBA_WrytT4woAFqvdWNBM3SfjgZEXmSmmHjL_npak6D8arCqbuUEFJe5rNiVH49O36lS5RNoIDDjJdHLBS1OKRG9ocg6qxIjDhCBaiDZYSk01aRcNFZmU7kXM1tOTW2n-hxEKpmAhW2daKhDug1MCEFyYJ886hKKq_2XifX3Iir9ei4eNlFBcAkFvx8iqGLFsyMthxvs9c7BASG-L-s6Ifp72Qhfj5LL4MQErMXGjhYRZWKh545Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22845" target="_blank">📅 22:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22844">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080305bcc8.mp4?token=VD17qHWwbYq02tbNbKwfEzJ32kLCjnSoZmpQptMTf5PGZd9dxEiVHhzL4-N4uKcXrbAJbReyhPYL_ZbhWvtJg-1E1MNZ6mMeiT1gR-GXacZW5tnpxhE-BkyS3iX68Zzy09cnqGJaSEh1xNmU9h_thwUlKm1xcr9v86K8N5WJt-orGR60UMX8r7Ul8zm_ZuBePSLFvcqo6z4AZGspkBW89hb5JcnKf4SIj8iPykgJsXo2F1fvUiN--pkjaQ1kJ5ETCiqWpYM4pXZ-YMdY-k5y8IhvSjdjrrOh470XL65ojNlxfEqaBqEi1UxeVjKQiLjE3t7_3GU-yYS_DgLB4ynF6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080305bcc8.mp4?token=VD17qHWwbYq02tbNbKwfEzJ32kLCjnSoZmpQptMTf5PGZd9dxEiVHhzL4-N4uKcXrbAJbReyhPYL_ZbhWvtJg-1E1MNZ6mMeiT1gR-GXacZW5tnpxhE-BkyS3iX68Zzy09cnqGJaSEh1xNmU9h_thwUlKm1xcr9v86K8N5WJt-orGR60UMX8r7Ul8zm_ZuBePSLFvcqo6z4AZGspkBW89hb5JcnKf4SIj8iPykgJsXo2F1fvUiN--pkjaQ1kJ5ETCiqWpYM4pXZ-YMdY-k5y8IhvSjdjrrOh470XL65ojNlxfEqaBqEi1UxeVjKQiLjE3t7_3GU-yYS_DgLB4ynF6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
ویدیویی‌از قهرمانی تیم زهراگونش در سوپرلیگ ترکیه؛ زهرا گونش بهترین بازیکن فصل لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22844" target="_blank">📅 22:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22843">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63cbb26f8b.mp4?token=Ql4635pEHyz6BLNTaIVwxVEQa7sAzMXobeIYF6nUgq7sWHq2AZV_fKyQdpLp7I7mHKmjPzj7xsrlF4i9CbGy8PNjfO8WXKSz-eQ0v4mjwcE46G9V8WQidGh1doPXyDhd6REjU9PF2WS9ccz6ZZ62-TlHW1sntiZT6_q0gDWCQ2-931bB9BnHsOvR2b8o7X5OLFmK8qRyTYUNnswIly9eXGCs3K8Hrb0xrlFx8Fwo6G2wjN2tSFoWCCOG-vkCX9x-TZkBGTfAdw06sUbl_OEjupNDu8IzkY0j4ZvbXMlfYH1FNd3w2eji-brbb1BC0cLkGs49fVY-4MialWWH4QPdxDHuVknyqDHEyyKUVvbu8qWfferYFWeIo7zGuREgt9thk35Fk_UJzV7Y9ZHaYibUqPiaOVZCfimFq_wiEwLzHZYPD_WqjP27vvavx05gg5alp-59uYWxUqpZ_T7UrAGsKGvC4pz9YBAOQp2wPwjz5iIKJvlKS0Xx-nm__DePDmpIIdt96xdgBVwgq5KY_EiNf-YP1KkdssUBlLowcaY_ahy-E878esaW8BgXHUieuA4hSihSIqWNtJAAUIEDflquJ-MesGVHts1h7Q1XuQNlqK_Em0xnxYJSKcncmpuSXgdhwhdz2ptdvqBjsOCff0FbUCZN7DoR36ZaBG6YvZh3Pys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63cbb26f8b.mp4?token=Ql4635pEHyz6BLNTaIVwxVEQa7sAzMXobeIYF6nUgq7sWHq2AZV_fKyQdpLp7I7mHKmjPzj7xsrlF4i9CbGy8PNjfO8WXKSz-eQ0v4mjwcE46G9V8WQidGh1doPXyDhd6REjU9PF2WS9ccz6ZZ62-TlHW1sntiZT6_q0gDWCQ2-931bB9BnHsOvR2b8o7X5OLFmK8qRyTYUNnswIly9eXGCs3K8Hrb0xrlFx8Fwo6G2wjN2tSFoWCCOG-vkCX9x-TZkBGTfAdw06sUbl_OEjupNDu8IzkY0j4ZvbXMlfYH1FNd3w2eji-brbb1BC0cLkGs49fVY-4MialWWH4QPdxDHuVknyqDHEyyKUVvbu8qWfferYFWeIo7zGuREgt9thk35Fk_UJzV7Y9ZHaYibUqPiaOVZCfimFq_wiEwLzHZYPD_WqjP27vvavx05gg5alp-59uYWxUqpZ_T7UrAGsKGvC4pz9YBAOQp2wPwjz5iIKJvlKS0Xx-nm__DePDmpIIdt96xdgBVwgq5KY_EiNf-YP1KkdssUBlLowcaY_ahy-E878esaW8BgXHUieuA4hSihSIqWNtJAAUIEDflquJ-MesGVHts1h7Q1XuQNlqK_Em0xnxYJSKcncmpuSXgdhwhdz2ptdvqBjsOCff0FbUCZN7DoR36ZaBG6YvZh3Pys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
کاشته‌های‌دیدنی رونالدو در تمرین امروز تیم ملی پرتغال در استانه شروع رقابت‌های جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22843" target="_blank">📅 22:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22842">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZ45oWSc54zVSrm3amF0hoP91uI5ctaemdQJH5ycpk9qrwDoMvFIoMepzB7KeWOUXTsXSCzHq0_hdd9FMcPQSHmTc7DgOv7UYKmLBrM4dklfYlfWxbrB8xBL_2zAW7_rWn41RWsT_eDcizi6JIZJHzlN3Wt7BMprSs7TJi--ZWL2rpDEldKkNBKqLBaA2nY8ea2IfDVGaq92JmiWFZCHGDU0aPrBaXQ645v_u-_SxbQojkRMFu6D43dByVXQ1H5MP8zaFPcAqFPBFRqIvQJS_iZBf6RvHFd5QxoBmjFhE0wFqc13JNhOACOrXSu5woK6AEDOZytHHn-QCJVWVsc--Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛رسانه‌های‌فرانسوی: کیلیان امباپه، مایکل اولیسه رومتقاعدکرده تابافشار به سران بایرن مونیخ موافقت‌خود را باانتقال‌این ستاره 23 به رئال مادرید در پنجره نقل و انتقالات تابستاتی اعلام کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22842" target="_blank">📅 21:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22841">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ay4bLfDAEsovKdypeTsh_XZcGUSXj1FMor0G4om8gHaD7lVy8Wye_LNi4hkdRKN_zU_Rd4g8W0U7D1A_QXxZ5KqB1csFGa7lDKW0eb3Dy-366fBvnQJGc59wMpch6X9vekRfzfjpYgRDrtv08vCtUmDE_P7Xlc0Ed7X331r6oKEc5c5qa_i21VancOAuoP6-z4zxJoZeVg6RjcnKd4tIQVfkP8O1BjJ12YxUf-Yqk64-2sv-G5IK7-9TfG97C7SkRtcXuxOpfZUAxnuRiN9TJhWHN57D8XBz18zJSzwTygSRDhnEKALcyztKlBvtuZ6lrjx8tZaD02voFEMIuk3h-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22841" target="_blank">📅 20:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22840">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c01b9049b.mp4?token=ts03VRtNSqf84igwVzOIuFMcy7RkhiHPunaUWqeynTasic80iyBmriRv4MR_nXM_r4R75nJns8WkzfzfFmhLl_uHP4L0NcZ-o2gnTHwdAG6Sw92gf1HB_g6DYlKytYhtTbZB3XA7MES_eKr6n327vkAqZQclHnzez5Dts8wNXTnjph-TvDesB0JLGw0HjJSlR8jMXiF962wu1E3k74C857DJUqzWmvQCU7l0mUcs3uCdLtEt7YDznJzC18m4H9q4AvuE9_i6H8BOtFV9VNF0bFKoxtjdfhNJUo1sSisEGISPAdajqZevz7Hjw0aVZQ0u7TLlGZLidwjvzq-U0O9L6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c01b9049b.mp4?token=ts03VRtNSqf84igwVzOIuFMcy7RkhiHPunaUWqeynTasic80iyBmriRv4MR_nXM_r4R75nJns8WkzfzfFmhLl_uHP4L0NcZ-o2gnTHwdAG6Sw92gf1HB_g6DYlKytYhtTbZB3XA7MES_eKr6n327vkAqZQclHnzez5Dts8wNXTnjph-TvDesB0JLGw0HjJSlR8jMXiF962wu1E3k74C857DJUqzWmvQCU7l0mUcs3uCdLtEt7YDznJzC18m4H9q4AvuE9_i6H8BOtFV9VNF0bFKoxtjdfhNJUo1sSisEGISPAdajqZevz7Hjw0aVZQ0u7TLlGZLidwjvzq-U0O9L6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
@Persiana_Soccer
| Out Of Context</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22840" target="_blank">📅 20:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22839">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lw-UPCBiFyHFbt_n-rdoR1wHVMIG-83DApmgByBnGzawli7-QlEp25ty3jHh6gPK8AL2uh_GqR3WW2UjG_jeDtCcInIaMDbIJZseVsdCnI-SRCL_3IVuH3ljbIe2S4NMFcl8E_4CcCXw3YEMbNBkaR_vUZxo1jCfAcDTHbsJqTgphhWWnsIqxr3QO50qSGeUPOCGRhcghPLSA_XcamTtxH0blLtsMlQ6NB5p9BgUZtmZbeFAfwSAaBiRasPXDyr447iybb_EV-qvM5Xz8SnJnJU8gr8eYAOH0TZl_vuX15hWp_j7ufET4shMGrobUCW9ZbQhUiaxLDAjTqDWkDvz4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#نقل‌وانتقالات|ادعای اسپورت: آرن اسلات بعداز بر کناری از تیم لیورپول به گزینه اصلی هدایت باشگاه آث میلان تبدیل شده و مذاکرات بین این سر مربی و سران روسونری بزودی شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22839" target="_blank">📅 19:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22838">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g03_HcQakjrJv6k-VDzUok1N_2JY-0guSzu_x39qNZvUtXPtrWdIh8YlreUdUXt5HA_EhdoKhbBm0huQcWkdqeiV2xE6FGn5JCvC_lx7hYJuA1ozObavbouZjpm4Ir7Y75GsRuZMinS2PIz4RUpzInjg1x1TLwH2Gd1hrUODhQzFi0Vk4qjvA8iJrrCjic2qzQqjHUbMp7K1l2jvpxbl_YFMgEa5FEjbMFyF3GQIHH48VZGiWQXCk19polwbdZw_7pG5I6-dy1FY8q38jqIA-eEfM7NcZ08CktkFq-r-EtqH5FQMZJKPgVmRaxP4LC29A4eVQITdWlo6pdEnsG11dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22838" target="_blank">📅 19:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22836">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeqi1cMApWpXXDRxcKmAwQ8o1-rp75TMj5xfNbXxx_eSHlIkXBCplgNAeSHctIyAlP-gtHbUZ1Xc03Nh4H7aRM26Ow6QM-rNTZC_PrkZHLV0XEHp_rQqqOUNnu4ZyaJehez_8g4BNauHaSw5vWKJV4-tPIzL93oZfPLslDciMDkPAhXreOr1eFX4SLGK9jqrNUx3lV3xAN3wxcvJErMLEgFeucM81ejbKjN_LF0AHyAknzKQvX7j5D9fU0iOHkUtK5AQmBFDSktzPpL0GgvNmhFPkpuEDwljxyCXIHirnrTyD0DF9iVNH8IchbSzPTOgVCyWb-O8LmCTRQUTSRPEcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a220e76f7.mp4?token=tgK41nlHpF72wMwrs3yMDa7SvEagYTcYRZOMpX71aalAv4LxtAv8CRdl3Z_nWw8hXfhnTmA2zutM4DUubY6mgtKofg0grfhyFVS1FNWftwcj0vS0OpgH5pnkCuR10Xf2xTrIu0HQobXVERYkAmV709ix7WukkBjw5dIBW1G9HFmWmvEAgDejxEJ8J6KirnGEluGtuiJAWNFffwL0gv6ciU8_0VrNfNQmwWdG8nGhtaZAJNaUneV8LyIxIBT7aRtGBLc5UCHggEu7jcnNiLE4fjriQlhWMN9i0XAGjftz8xprnxw1iQWH8vlNLXpipl4dOrv2stFksA3MhIB7FVFzMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a220e76f7.mp4?token=tgK41nlHpF72wMwrs3yMDa7SvEagYTcYRZOMpX71aalAv4LxtAv8CRdl3Z_nWw8hXfhnTmA2zutM4DUubY6mgtKofg0grfhyFVS1FNWftwcj0vS0OpgH5pnkCuR10Xf2xTrIu0HQobXVERYkAmV709ix7WukkBjw5dIBW1G9HFmWmvEAgDejxEJ8J6KirnGEluGtuiJAWNFffwL0gv6ciU8_0VrNfNQmwWdG8nGhtaZAJNaUneV8LyIxIBT7aRtGBLc5UCHggEu7jcnNiLE4fjriQlhWMN9i0XAGjftz8xprnxw1iQWH8vlNLXpipl4dOrv2stFksA3MhIB7FVFzMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ارلینگ هالند جدیدا تکثیر شده؛ نسخه هالند جونیور، نسخه هالند پیر، نسخه هالند دختر:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22836" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22835">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETYLJqQB9oBA-JTn610yVqBLPwhkhJB_LIcSZSsfKYMCfefq51zvYX1Nm8brytnr1OUgTTs9pbiswyf5YCGIZIZsz5vDjhhLmVn87PPLs2J5HueZNmZh-CFEbYJINBGhnRgO_kTIZgglRAj8JS3xSalY4_RhCuzuqfjSR0tgaccIJmSS0Nxi3lCmO5HvTzyaFGRPb8WniHzI3UbpufGK3MZlrHbFIwUkgilBJK7Z2gN7CwPMce-RLvevYzWtTJzcVILGxQ0mf5hkfLTI55osKHEWigk7fxSX_3Eue3OS-HwkglS-N-ezDHqsPt2KwWNkp1-tGykETf8bo-JdXelRug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو هم‌تاییدکرد؛ پرز میخواد به هرشکلی که شده مایکل اولیسه رو تو این پنجره به رئال مادرید بیاره. اولیسه شماره 11 جدید رئال خواهد بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22835" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22833">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijoAa2n8dEFS2RLO7ClDU_n-ozNwtNhM6f4L1BYpey50RqkbztEmdiPGbt00sk4FELiJsD9WL5IJ8Mn2ijxXVTFZ6-ysdjIU8ckDY5f59dsy-l3ZmQ5NdMC6ppV96delNrZIiqCmkIW4l9xBcQm8X2JHyCzzhS6jMcytuLrWS3f7OacpcAxhuvCrmhViynqjZOzw2Oxg_SdpUsmSQ69N4ZEqQCRmcHdENzw-fO_JWYuPqwq1IvPxOy2_REvVz9lsstoJMr15z7ff2f_GxdaKjUEhswE_APDPMCpbd-WIZXjcfcDrqK-V-1DiyyO_F4jINXdAVodXTPzNj1XXAmDjIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا محمد دستیار تارتار در گل‌گهر: باشگاه پرسپولیس باتارتارمذاکره‌کرده واگر اوسمار برنگردد تارتار سرمربی می‌شود! او می‌تواند تیم پرسپولیس راقهرمان کند! باید چه کند تا سرمربی شود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22833" target="_blank">📅 18:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22832">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8480hfTMuFsvQ579uKQ6rpuGRbsFkgLXZa3G0wIJ7oDOloRKoRx-K7wYWO-r3q_rfDmqKF7bxKTeQGqWPxhefRTbmxT-xmhRFz36UdpcWyeWCopJm0uj4wcI9nQeAOVdPIDKbNds7uDc8p4rfgR1R8M9i2qILcNjqE_aWknpKllV-FmTDzesqkByX_tH40RWAN0ACZbnR5qZqdlOMlPmbqpwQ-8F10lWz4HWlTA-Dl47zVwRg28cr8OeCOqnCLenmIEx6xUWY_p1_0SV8pXLzQ4GgY58l7szCZGpNxCmzPG17aCbI5YaA-wI0Mxm0oJNjcUMOdYcRm09jSXAevM1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو هم‌تاییدکرد؛ پرز میخواد به هرشکلی که شده مایکل اولیسه رو تو این پنجره به رئال مادرید بیاره. اولیسه شماره 11 جدید رئال خواهد بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22832" target="_blank">📅 17:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22831">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0xWPK1ghc6W5I3dL0mENlrEi2Pv9fTKWgGFXopkNfLcP78ZKTHUEduF-4DNbcoJwvXQa6XOg8kHpf7s7fFK6kqewT0sms6nMzb-6rJe2zV3GBgBqPylQUqnEiY_OaII2PoY9LobZW0jbFAM3-WQnRFzznnIwbb5pql85nVotZWjtmYpXokSTwzyi8SjtkNMJyCMwYsVDaFcxdaNJUN7nC5yppnA6n-2GSBwWTkBtnULyrjX_sxqBUyy7geaU6qT11YEmSB5UC-arJdeZkwp6CtxgwbNF9icRwfLgaC0fUlO3aG_rlZyyIokHm5Tgv9rXJ-tk3Vcf3I9l5LuknnjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛‌خوزه‌فلیکس‌دیاز:طبق اطلاعاتی که بدست آورد مطمئن‌شدم‌که‌منظور فلورنتینو پرز همون مایکل اولیسه وینگر فرانسوی‌بایرن‌مونیخه و روز سه شنبه پیش رو آفر 150 میلیون یورویی خود را تقدیم سران باشگاه بایرن مونیخ خواهد کرد. خودِ اولیسه هم در جریانه که پرز میخواد…</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22831" target="_blank">📅 17:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22830">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUdgYIWa1-a20eKBhgY7SE9A5Yce6983utrS9RoslKDykMbAbYi0YCZTVIGnpuZ0g-ywYu_e-dg1Ch-mq8q26Qw7C4zUI4Smswk6kvBLo_YmJtFW-TSd58O8eGz5gwSV8f8ZayG28LbyNDpjeKQOlLUoNOy_YLKussrdOXnV4bBGZH0JP-Tjvv3Kcy8xjeajufeqi-yFov6nNGUYN_HEB4WvcsDSZfF1dv_8cMe9uXYNX18vI4nT3vZnq3ZK5czr1SPUouzTmK0DWTHHqV5RxK-YCJtg9Ui3RNlsvcxi-vqyR3DDR6Vy64ixSrc_oh_ecl_mjg7CTltqSPRqh2lYNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خوزه فلیکس دیاز: علی رغم تکذیبیه شب‌گذشته فلورنتینو پرز؛ باشگاه رئال مادرید بشدت علاقمند به پیوستن مایکل اولیسه به این تیم است و قطعا در این تابستان برای جذبش تلاش خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22830" target="_blank">📅 17:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22829">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/976cd07773.mp4?token=SlF9q9XccE47zuOm7cO36xdSFtjXZbaDSRFxpIXwMXmSNpzOsagh4DzX01HYZmMYkoFWzQPWt0Y7D9EINH0LOtJWoMFtNc0J-WhQjGUYAr-eo1Z5teLXTLw7qhZ8PAmhjEAcw9NPnh9POOafgDUvDa75owVPtnuYBOwqaLoEenIgfXgnqiMXT3G8q13E_qZD8mKtTlJunNySNzx0ELcJemApY4bWochXl_tlHwrQksrx_-acKZawrmax6crxpYj8-r97wg5tJAcxqHBcValLDymCRbNJC0Pesswey6R2ZRKKu9cfhmByS7ePlYkljMZuiXrBKgGZy-WqAQ-GZxf7aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/976cd07773.mp4?token=SlF9q9XccE47zuOm7cO36xdSFtjXZbaDSRFxpIXwMXmSNpzOsagh4DzX01HYZmMYkoFWzQPWt0Y7D9EINH0LOtJWoMFtNc0J-WhQjGUYAr-eo1Z5teLXTLw7qhZ8PAmhjEAcw9NPnh9POOafgDUvDa75owVPtnuYBOwqaLoEenIgfXgnqiMXT3G8q13E_qZD8mKtTlJunNySNzx0ELcJemApY4bWochXl_tlHwrQksrx_-acKZawrmax6crxpYj8-r97wg5tJAcxqHBcValLDymCRbNJC0Pesswey6R2ZRKKu9cfhmByS7ePlYkljMZuiXrBKgGZy-WqAQ-GZxf7aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین‌ابوطالب‌به‌تیم قلعه نویی:
شک نکنید این تیم قلعه نویی تا فینال جام جهانی میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22829" target="_blank">📅 16:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22828">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnm2r8i4tLV7HUG12n4gpB4cocr-zELmIW0QtjtcOqTXR6hUmP7H1C5657ED0rmjvG8KevMKMffU4c7UsJPP39t-YAW7nivyAEXvRx94dA7d1bPg44lGe2kn97MMDGfbMbX2uKJcQ1HnBcHp2ufd5mNsaES7S6cL9kXt10hdlN0SBEQMvNJ2TTItKO3kckSZJ_59oi2mfUCmSRqFHVaYJY6SF4Wh-pVKz6Xizk6H1f2Mr7P6Dq3q4GfBo29QZQQ6PyHOLpIE3xrpPBqv6jbJlH2p36kMGpajHyM-tpQxjOq1_HZH4bU2YRjnVv6Vzusvmlewnk_fmn4F8YRUMvxK3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بین‌گلگهر و پرسپولیس؛ احتمال زیاد پرسپولیس راهی لیگ دو آسیا خواهد شد. اگه اتفاق خاصی رخ ندهد! گل گهر رضایت نسبی خود را اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22828" target="_blank">📅 16:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22827">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/un68CW5qQLYz1z4hwKSaK3Nm1Gie-SeVZEld930x4TzIxkPCNy-iKdhig3DQsTscg4Dv4XRnX3OwaQ7hdOr9qwwcbw1Nca35FTAwxmz0ib26Hecgtj5gpBtZNBHAbh9BI4cpX0vSR82O37H8n0Kc_OtntY9mCmSKT1aP6CuIIwZRe0Tr6pts-cjzh1mMLBTYoi7moclyu8I7vsHZ7m-NTanQPglzTbmA3OTsriL6lqNYQQmRPXbvH2asNPWnrIO2uyBma3u71XesplBfUCBQtyGWX-_THasKgGtpGN_mXq42I6SQ1gHOON2o7LiKxuqNHKywY78JtywFEy-hxeeV3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
آقا منظور پرز من بودم. شماها چقدر آی‌کیوتون پایینه. سه‌شنبه 150 میلیون‌یورو به حساب سپاهان واریز میشه و رسما میرم اسپانیا برای رونمایی.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22827" target="_blank">📅 16:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22826">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7414e31a83.mp4?token=qnEATJ-kS8stOxkT5K3OBIrUjXUv7JJjpjGV4T2j78dmcA0h9YhHnN-1kTJRPtPyn9vCSWUqP3pd66gcnwsGHCfwyJ2GtVL7UaGwyRIzWtp4Sl55LvJ5WNzYiJqYZbGgfZkBbqRJCVJxzySw9GLSy3IJR3hIiN0LPKG-zi0G3PkMa12kpD63WBBXlvcXoRtknWBuzWfqXGG7FzPYQatXP8Ic7BR7H4fxchzGQDeJNAZhi_5x9BIrCTeTLY0VCohTEB7-DYjCNrTZN-sCNynnBjBRz6fAKY-WN57XA6ymn_5DkZ9Ha_y2SVaivL1gkn2SFr1EBH161EaaH2aR06XGlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7414e31a83.mp4?token=qnEATJ-kS8stOxkT5K3OBIrUjXUv7JJjpjGV4T2j78dmcA0h9YhHnN-1kTJRPtPyn9vCSWUqP3pd66gcnwsGHCfwyJ2GtVL7UaGwyRIzWtp4Sl55LvJ5WNzYiJqYZbGgfZkBbqRJCVJxzySw9GLSy3IJR3hIiN0LPKG-zi0G3PkMa12kpD63WBBXlvcXoRtknWBuzWfqXGG7FzPYQatXP8Ic7BR7H4fxchzGQDeJNAZhi_5x9BIrCTeTLY0VCohTEB7-DYjCNrTZN-sCNynnBjBRz6fAKY-WN57XA6ymn_5DkZ9Ha_y2SVaivL1gkn2SFr1EBH161EaaH2aR06XGlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22826" target="_blank">📅 16:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22825">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJrCG-WEailEDcx3QTIuBRkow1xbCwS7N3cAx6pV_1G_grUWtma08CBRvamE0ORRAxIjuK1KJNLQOkKyjgGbIsJ2FAbFso5icB-loXBnPGVqnGCRocMpZpEnkI82hjDflfeGTsNnHjdWrD6nsUNKdfYqtKMxqjRrOjh3DoB_QZeg2c0D85AFCWnIZaK2oi2ODtGnbMO7A7_KtCI0CYDsI4thhOzpBw7ojpKhQGjApE6sgejSsc2Pej3oSy1bomCckTIOq4x0ct6hruBsJWbBsRzYjrKsN4Fe6kVPR8sz6KH206ENR3zBFA4ZrDReWLovQH5BJ1ms8FqdSJS_y4i6og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل هفته سوم رقابت‌های جام جهانی؛ از روز 3 تیرماه هفته سوم شروع میشه تا 7 تیرماه‌‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22825" target="_blank">📅 15:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22824">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dy7t8vGStOBRzJ1tWUa4t7cszmAcqbyJDa9e8NNytOidAoCUCC6xvoiKVW5Oqg7uUciSnQx5vak6gHTyoq45DXYJyHcUGQS1DI_gsl6ZrOuEEXWmVtz4_-C1V8Gb6d7lDUnrF8qKRjZ8oQHIcUaGdkJKCHGP0szgb44JbwcQd-5i8BkNPCrrnyBFgtxtEaAp16aLuBmWYe0MU7rs9y2rwQuVBOz7-Tokp7DVEgSFsH5FGd1uSYZI6ba7tfu9j6GfbmmGAg49-lj0gd9kPvwvfdwpqb46td5tDhtYExMJn1UFY4jF3bfQaW8qZwm0W5fS21tMjEnCh-jFs8uqZ8agpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ نشریه‌ کوپه: رابطه فلورنتینو پرز و خورخه مندس ایجنت فوق‌ ستاره‌ها خوب شده و مندس به پرز گفته هر بازیکنی بخوای رو باشگاهش متقاعد میکنم. ایجنت ویتینا و نوس همین مندسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22824" target="_blank">📅 15:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22823">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmvR0rJd2SkiaRx_HPmjLatYfnZ9ihISYt50jsl8AreJaQx3CDIROACWrVcj9F3HLx90MBR81UqGUn-m8FhjTEC3SjNCKso5g-0gW05SZOJ_2E2gMUgtXy4AIC1sMCU9bSiV-3_QJzTEsbG-95dxkcZdGOfFmWvWiFbXxXAMLjJ6iNuh6Eyud3mU6ikdWB41eLJoUsn11MK4ZHPMMq1g4mY5jwVHB2oTz9gXqIQ1Vk-aGuXfxmS3gKzFvFUNPh_-LW9yIj7VIKSzAYg3mIaUmB2goZSZo-RuLqNU8sDThV-VhahHdFNpgqdpbUg38dbpoivJQy4m5G9xO-SbcqzzjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22823" target="_blank">📅 14:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22822">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2hlfQeQ_xZyJIgAmPD5lrx-ZszjM-en_relZdfVXPkfm5c3DT2HCDcQy2iT9RrctxlBOVjFKTl6lH6ovGa0xLVaOZ_JbXU_1OgzNCQ_3c73X0KgKtahI0eMNTfYXvfS247LDqmQOjvAF8mYTwYlNsrL6o3Q2cEjI3JQ96Zre69eRUjaPEjaQjW0yKxcQ4_yO7vZ2dC3gW9sqhPY2g4tEDXfoOW2e_t8s0-gVUuzcl3owK7_z-M8-QkwIjtYIaPQST8Aynz6pMSFMV6XbvpM-TDde31_HlfMgGJdQxGn_s4JAUFSXQGX63NOscSI-0h9i89rXsBmAT3CecQnVrG6eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌عراقی‌اکسترا از انتخاب یحیی گل‌محمدی به عنوان سرمربی جدید دهوک خبر داد. دهوک تیمی درکردستان‌عراق است که در فصل قبل لیگ عراق که شب گذشته به پایان رسید در رده دهم ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22822" target="_blank">📅 14:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22821">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b9b84db0.mp4?token=F-F3CSn82dIf-7ZPFp27-gJIOsqzRXhRsgCFlEIXzXRcP-V6D9-PgWwY5vlsz3BxQ4dSh_e8MCHFiBEj-ofQq3CVWUVebLrMtVQv9JhgG2fxE7IBj7fHK4Wabu-3UEfCPtjnv-iM5XLmzMzRiHfy8lb4tDxq8wiHW9l_BYPSxpz_aoXQm7J_0rhE-U57Zif5TFC7rXV2sjouIzc-mtO6E0LA0UmV8uq7HBbGppzEjGtuWj-FT1M5vf9zyyoXrjC6FB424aDG3fyKeMfX-60BwFoehIcQtOj0CRlG2BjXQQfav60haSOyM5mtD4sUKAdZsMXw2WauX7S0P1gLgKHZVAQmd32ndcFFS5v81GjaIMV3IE3OoEGAmXduvIyEbyBTdF9c4JUyn6lE1V9hiUp-h4aUZ3ho9Qp-Ky5P_9-2e7ZfGx7nXKZRXVRfFm8miK6F88b6W54OsP39IHzeUMqAXy3B-zM8bYhFunczRn0-qQAoyp4kORvSeTJ_-KU1jb-7MROTs2h8tdSo8nb_ec2RZLL9daKleSFoy6SG04q_4tdn2oAPG0AjWVj3HOnB4os2iPMXs40hFXWFn0iW8BSmVBvgY_3JJ0_K8Aa2hmHbhEbeLVTVfqvZQJ11NXbJGSGsmGavAlceNjvt46SV1mTbR0WR2XMPvK0ky8hAJZM1V_o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b9b84db0.mp4?token=F-F3CSn82dIf-7ZPFp27-gJIOsqzRXhRsgCFlEIXzXRcP-V6D9-PgWwY5vlsz3BxQ4dSh_e8MCHFiBEj-ofQq3CVWUVebLrMtVQv9JhgG2fxE7IBj7fHK4Wabu-3UEfCPtjnv-iM5XLmzMzRiHfy8lb4tDxq8wiHW9l_BYPSxpz_aoXQm7J_0rhE-U57Zif5TFC7rXV2sjouIzc-mtO6E0LA0UmV8uq7HBbGppzEjGtuWj-FT1M5vf9zyyoXrjC6FB424aDG3fyKeMfX-60BwFoehIcQtOj0CRlG2BjXQQfav60haSOyM5mtD4sUKAdZsMXw2WauX7S0P1gLgKHZVAQmd32ndcFFS5v81GjaIMV3IE3OoEGAmXduvIyEbyBTdF9c4JUyn6lE1V9hiUp-h4aUZ3ho9Qp-Ky5P_9-2e7ZfGx7nXKZRXVRfFm8miK6F88b6W54OsP39IHzeUMqAXy3B-zM8bYhFunczRn0-qQAoyp4kORvSeTJ_-KU1jb-7MROTs2h8tdSo8nb_ec2RZLL9daKleSFoy6SG04q_4tdn2oAPG0AjWVj3HOnB4os2iPMXs40hFXWFn0iW8BSmVBvgY_3JJ0_K8Aa2hmHbhEbeLVTVfqvZQJ11NXbJGSGsmGavAlceNjvt46SV1mTbR0WR2XMPvK0ky8hAJZM1V_o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لحظاتی‌از عملکرد خیره‌کننده لامین یامال ستاره 18 ساله بارسلونا در رقابت‌های فصل گذشته لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22821" target="_blank">📅 14:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22820">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d7daef98.mp4?token=Iqao0qYk_lB8jhxWgssawzvqw3OD24F1XAQw7Z0GGr5ZGnwmx071T5TNfEBJOgJmYhfTRjHFWTkWGqhueMT1e9tpEn2mKR3a07aszY2NzGbfYXcx5SolVFwiVpbzC-JG6N2yiUKbQVncyEv5Hvbgv3AU2HRal3Yo0VTNNaSRj9moFOAAu3C8d8E6mRKkOG4dIoPl_d54e3Qp78IKBnuH5vFvqujPGL2SRABeEEAuxVxdcq1-EqtfpKJKko7dAqp2uBQquOEmOVnHI2lbFvUWiyIDKHlNqQ_5o8ZAZYtbK7loRQNiLmZMpwf0BSnYjRR78qEdXJd36i5_VkfXL8MfhHU5ET3pGMoZL7jKez-uQLGXqKpcXPVIKsNK2AHU__QIyppXSs-M2j-yK46PFS5809PBcLdic8yKF8cRg95KFZ4nUOfPHNZRqwy6A7bRAoydLiNAhxgFm5nRtklkcgrZPp_AYapNe4KvuDBi1hXVDtkao0JzhAYD_D5lJplFBa5St_o9EK3m9TW6TCLUj7b0y__nL-fvm-Ct25b_zMkXUYLGY-Ovx-xiF3FCRBsB2jdR37sa2-95LqtYCoxMKKTuCVw5wFr2N7j7h1yjkFjYpCJ4ndpWqTu4u8oYkU8A7QjeZ0Hy78Z4MBQEzwVm4O7I2naWPSDuboN2HhaMAKqeXUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d7daef98.mp4?token=Iqao0qYk_lB8jhxWgssawzvqw3OD24F1XAQw7Z0GGr5ZGnwmx071T5TNfEBJOgJmYhfTRjHFWTkWGqhueMT1e9tpEn2mKR3a07aszY2NzGbfYXcx5SolVFwiVpbzC-JG6N2yiUKbQVncyEv5Hvbgv3AU2HRal3Yo0VTNNaSRj9moFOAAu3C8d8E6mRKkOG4dIoPl_d54e3Qp78IKBnuH5vFvqujPGL2SRABeEEAuxVxdcq1-EqtfpKJKko7dAqp2uBQquOEmOVnHI2lbFvUWiyIDKHlNqQ_5o8ZAZYtbK7loRQNiLmZMpwf0BSnYjRR78qEdXJd36i5_VkfXL8MfhHU5ET3pGMoZL7jKez-uQLGXqKpcXPVIKsNK2AHU__QIyppXSs-M2j-yK46PFS5809PBcLdic8yKF8cRg95KFZ4nUOfPHNZRqwy6A7bRAoydLiNAhxgFm5nRtklkcgrZPp_AYapNe4KvuDBi1hXVDtkao0JzhAYD_D5lJplFBa5St_o9EK3m9TW6TCLUj7b0y__nL-fvm-Ct25b_zMkXUYLGY-Ovx-xiF3FCRBsB2jdR37sa2-95LqtYCoxMKKTuCVw5wFr2N7j7h1yjkFjYpCJ4ndpWqTu4u8oYkU8A7QjeZ0Hy78Z4MBQEzwVm4O7I2naWPSDuboN2HhaMAKqeXUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
من خرافاتی نیستم ولی شما این بازی ۲ سال پیش پاری سن ژرمن با حضور امباپه مقابل دورتموند رو ببینید؛ واقعا انگار طلسم شده بنده خدا
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22820" target="_blank">📅 13:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22819">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co9wmvd10SWoaxv6KZY-xKTJvd3mb_qfmHp2jT3ftq4WuigQMhMxsHWaM-xZrStyDUJ6dmcNPAYdh3qI7jU9fvXWqzmhow29GvUNZs-6FlyEsTEVHrIbVKFOM6c-C7Yn-OpsPGufWZy2oY4zr21h2af1W2QJvCnoZbL9kFnXc4YUYEzPpoGgmNq-NoG61dmf6BNEJwdaJ5uwepOk40OSR7FFUFGIgj_GGf_UGaCugbhdZCFCwKuoLCJqBN7uBrlx3vvgrfrVDXOK31VZqZGvLGRfbsEUBqYTnex8hemlIQFgpE5qhTn4GVE9Ee5DzJ9zsR8aGh2gMW1zK--KUHCbtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
#تکمیلی؛ باشگاه پیکان قصد داره درصورت توافق‌ مالی باباشگاه‌روبین‌کازان، رضایت نامه کسری طاهری مهاجم19ساله و گلزن این‌باشگاه رو بگیره و درتابستان سال آینده با رقم بیشتری به سایر تیم‌های لیگ‌برتری‌بفروشه. رقم‌فعلی‌رضایت‌نامه کسری 800 هزار یورو از سوی باشگاه…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22819" target="_blank">📅 13:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22818">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7913f58d6f.mp4?token=f_r-ZgaFZ_pYVDXOrndfkAa0X7MkXYQDerWnh_0lLSk06pCutAWua6fhWt1KbWCS55w8QEGqCLXFEQVzaJwKHBDBEYsCJpS8OKP7F0PEJjYCeFlDnl6hm14QGdmQXFKk2N9zoBLSJyzq0FCjTkxrxWuxoNiIyESctF1-GbjkGONOpyVgiBu5Xm4esa78wb89-CcVsh1Xh_lz5qAI4sPPc9RSM6NWO6RTI8ypxiQ7aN5rBv4eVxtB9RTpg7-vl2Nlti9fn1IchF4YPMyEZRGcoLPob-SZ7QDa3o-C4hcLDCJkYHq2X-IbRJwwXBOZFH7Sw-6f5MWIbJ8TnYpgAuQdqWdBjweKn1WPju2bzyDkHA3znbiAxK8IZJyD-Nr7KKSoj0lKandHRUTz4ZYpmv8MEm-Quk8lYs55idVeu9AY9vYib38wJtVCd9HavXebHCksIgO8mbZDR2woR_BxAoBLYhVBalawkObSf2OpMsVm-7Vt1YmaPKCfVBeakOe2Zt3bO_B39j6E6qZel06RDgT_mG6IUCDgY7_JJGgTr65uys30BFBBZwdHRWNRlXof3hVo1U7k9XwR1YAHJED9gPqgxHW2v6wZAb2dOJ-xuhMuMNNxnusE-7WxgaAAuL6Nhp1OlMnkbzjKJY2PdzQPUk2R5yjE-PZ9v7RZplJUJVqdgdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7913f58d6f.mp4?token=f_r-ZgaFZ_pYVDXOrndfkAa0X7MkXYQDerWnh_0lLSk06pCutAWua6fhWt1KbWCS55w8QEGqCLXFEQVzaJwKHBDBEYsCJpS8OKP7F0PEJjYCeFlDnl6hm14QGdmQXFKk2N9zoBLSJyzq0FCjTkxrxWuxoNiIyESctF1-GbjkGONOpyVgiBu5Xm4esa78wb89-CcVsh1Xh_lz5qAI4sPPc9RSM6NWO6RTI8ypxiQ7aN5rBv4eVxtB9RTpg7-vl2Nlti9fn1IchF4YPMyEZRGcoLPob-SZ7QDa3o-C4hcLDCJkYHq2X-IbRJwwXBOZFH7Sw-6f5MWIbJ8TnYpgAuQdqWdBjweKn1WPju2bzyDkHA3znbiAxK8IZJyD-Nr7KKSoj0lKandHRUTz4ZYpmv8MEm-Quk8lYs55idVeu9AY9vYib38wJtVCd9HavXebHCksIgO8mbZDR2woR_BxAoBLYhVBalawkObSf2OpMsVm-7Vt1YmaPKCfVBeakOe2Zt3bO_B39j6E6qZel06RDgT_mG6IUCDgY7_JJGgTr65uys30BFBBZwdHRWNRlXof3hVo1U7k9XwR1YAHJED9gPqgxHW2v6wZAb2dOJ-xuhMuMNNxnusE-7WxgaAAuL6Nhp1OlMnkbzjKJY2PdzQPUk2R5yjE-PZ9v7RZplJUJVqdgdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازلحظات خاص و بامزه پپ گواردیولا سرمربی سابق بارسا، بایرن‌مونیخ و منچسترسیتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22818" target="_blank">📅 13:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22817">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAOiZkxx0ZMWOACWhLvTl0A-FumZX2e0AlkyaN4t143R-eNwmxiZTufK1Atq8HEUc1toeaeRt2h6_YUOnKoIowUFhXbOpE77URtNAPxAFTaneFwFF50ZrFkuI8Njq5a7IyATjz7ZEy35FS0UNy_Nw_I634UOvU-6gf2HhK9ZanJKj6AiHlFrxFc-SbMvtBVuSWo9k1HTTm1-WrYnFmC4HlkfL2iqUdZN12KZu9epI750SbLF96769WuMHjZawWkmlGdoB-yAZAJ6_tAwURVtbojddw96cxwahM55ZQTM84-vryNNWAc5JB1qTubrOQjl8OC7kFBVCc7FnohenrED9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22817" target="_blank">📅 12:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22815">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/070c28a96a.mp4?token=NafP--YcPhPBGM6O2QP6a1Ht4AhZGfw52HlNkQRhV4S93Am--1zb9b2cWkkdZbbecC6ybhJz4v1NM2t3WlCCXfGElxSHOyaZ5PiB21UjA2CaRj9o-nBwX0qpfLW49s6Soq46-tGK3MzvbrpLJy8bAI3CUUAcRebox2CYzI9tBffgFyZJxPIkhfk-KThemQYbwD3YIHal7OmnnUNmuDppLZ3rU4YBSOZv-LufpCFnJeIPXAdrTSXMPwlhgEZYhKtl_zw8GjO62zDX4WrkK40Xdf64KgaiomjVd17CbdDeMQmDeQPnrdguBf5fEinM7FhppJZqEG6JTwtLkI-BU66WUjBamccGBCXdwnqGXEXLmWp16DlOcRZtOG5J0C5nQvGeZGDEiNVlh4ukOGSLa0tA_LxI6e3hKKPuLhKEdD3sujOTXedogHcqCyXopWgYUAZbCVX4E1DKMOoFIp3juJ-ac-Vr6LQteH4bheT8jXgkFqQ6Dd55VNgDdBrU7mphNKHaUMyhb-6EsCIXTxqZ7JWRo3Wjj7RDYInWna-mV19KrMwvGmnVYTllB7VyBEyHm_RY7BRFjB-fBzInczObJ-uKE4Dy1bGx4OqutLj5E3GM9bV6aD5Kq06mYMzchu5ZnMxbp3I1X-EbX3vCRDfk-ZhZxdWj-oesaCIuv8q68iSG9fU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/070c28a96a.mp4?token=NafP--YcPhPBGM6O2QP6a1Ht4AhZGfw52HlNkQRhV4S93Am--1zb9b2cWkkdZbbecC6ybhJz4v1NM2t3WlCCXfGElxSHOyaZ5PiB21UjA2CaRj9o-nBwX0qpfLW49s6Soq46-tGK3MzvbrpLJy8bAI3CUUAcRebox2CYzI9tBffgFyZJxPIkhfk-KThemQYbwD3YIHal7OmnnUNmuDppLZ3rU4YBSOZv-LufpCFnJeIPXAdrTSXMPwlhgEZYhKtl_zw8GjO62zDX4WrkK40Xdf64KgaiomjVd17CbdDeMQmDeQPnrdguBf5fEinM7FhppJZqEG6JTwtLkI-BU66WUjBamccGBCXdwnqGXEXLmWp16DlOcRZtOG5J0C5nQvGeZGDEiNVlh4ukOGSLa0tA_LxI6e3hKKPuLhKEdD3sujOTXedogHcqCyXopWgYUAZbCVX4E1DKMOoFIp3juJ-ac-Vr6LQteH4bheT8jXgkFqQ6Dd55VNgDdBrU7mphNKHaUMyhb-6EsCIXTxqZ7JWRo3Wjj7RDYInWna-mV19KrMwvGmnVYTllB7VyBEyHm_RY7BRFjB-fBzInczObJ-uKE4Dy1bGx4OqutLj5E3GM9bV6aD5Kq06mYMzchu5ZnMxbp3I1X-EbX3vCRDfk-ZhZxdWj-oesaCIuv8q68iSG9fU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
محبوبیت بسیار ارزشمند علی آقا دایی اسطوره مردم ایران و فوتبال آسیا در بین مردمان کشورش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22815" target="_blank">📅 12:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22814">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/advU6Nw3gUDki8VEg22brzCtwAbHzpc57mLMzwcJGmJAqQPPTVyVdTtKO6yKNbxJn64qaHQJcYbnYiosHBm_f3q6dfEdkm7JioIZGB60ayoVzDNIajaTXNKroBQCZ0-j5BHXCfqnmoWoTivGsIs-UeICYDj8ljzH-ymgnk4vjLFEgq0kghrDXMdbem9_aO0v70MmQ4A6nGcqpzn_qTZECDU8Dk0162eh_X2X7AQtPhKOnj7F8VPfFnhMeGXqb9O67YfH4xsrJCKldCeCaRYlAJ14LK122QEjChVb3cpNbPnb6aWgxE3kBhPZotnPIH1x_61Xs1i3uWklHxwWz8ueew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با بازگشت نیمار جونیور به تیم ملی برزیل برای جام جهانی؛ وینیسیوس جونیور شماره 10 این تیم رو به نیمار برگردوند و خودش شماره 7 پوشید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/22814" target="_blank">📅 11:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22813">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cif5DyYnGXZfsQ42PCAzAk8PLnE1zRIL9JVY0jMl3C-VqjF04AZsjDKS2v22Uf-i2DUDRwQwpDcb9l6Ivdl_mQYkyrQ25cR8qxiVY7wOag4DprXna0g2G3Tvyr8AhVbDJN4lHa8Cg9HOdTWPMeZg6NUBgBdRRLQ_eQS4b30gAHgSLV5N6-SJS4CjNbsjvt-1xJnRPgTmvn7CFHhSRJhKhNxd8-fwdTeLigf9te4IwCmae8AY015HSQBHP0y9bPpf_i-yclyce04TDQ2r3D35Ltk70hzI8RSCmAukSF-mZkRSxhlvgUbt3kv4P0fta-GphfSYkMsXz5ORxj9rRterfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درصورت باز شدن پنجره نقل‌وانتقالاتی آبی‌ها؛ باشگاه استقلال برای فصل آتی رقابت‌ها برنامه‌ای برای تمدید قرارداد آنتونیوآدان گلر39 ساله‌خودندارند و سنگربان سابق رئال‌مادرید از جمع آبی پوشان جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22813" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22812">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5-buNQdZM7euAZH3ZoOUaCZbmy5oVgWUuN270Pe5BzfD7xbhlinauYpSByDw7ENjP2esT83E6U1aV1d-wrWAWY8Stm2XsgjCnu4RZcz0m_B6wp1_khpOH15JiKRAbpm8zE7YFlPl5noU0IzbRSlSr9skDJ2sF9otxD-EU9Q8_JawOoKH73TnAanTdWv3fahrBNvx-Ti5lIoLPQRmU7FL6G_8pVeMKrzUBTsQETy_CQFUbPOqPLT7rUSqTiEl1xKuyToR21z04pCfFbgVPdNXIcNc9KBzP2yWIKQjs7tseA1iRq9g-tLp90ixKFMIjzY9lbiy1nYKuch99JfrlsmAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
👤
طبق شنیده‌های رسانه پرشیانا؛ سروش رفیعی هافبک 35 ساله‌تیم پرسپولیس که بازیکن آزاد بشمار می‌آید از دوباشگاه‌فولاد خوزستان و ذوب آهن اصفهان افر دریافت کرده. درصورت ماندن اوسمار در پرسپولیس قرارداد سروش با سرخ‌ها تمدید نمیشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22812" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22810">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBjIP_fM-la6-rwnOLA3AG4La6oKwG5mjoOpjOZ5_S1x_fM4LR0Byy1zIG1-UwlmHr5kG39B72hspqbPPOCp6YDBr922_LC3j5oWDa3aPnXwwObEQKUr2QEIlE7GJrxNWx2jDJ0Qqm3CFTG2RWQnRneT74CSeiAN6xU8zhgO_hvJWUurfRogAZIVkxc7KiTFPpUZkCTGobB5LOE_wKh_f3zoMsppaTK5cUUT_h7QkazjTK8YFnUWxpHDokhNS6SNzcytYxlcbSZ9LO9UOxd1InZtKKdMgtseIxw0hkCFicMMHRxu0qpakj5tlToQ1jelYhyZeLdQLPoRUKkXaXZakA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
آقا منظور پرز من بودم. شماها چقدر آی‌کیوتون پایینه. سه‌شنبه 150 میلیون‌یورو به حساب سپاهان واریز میشه و رسما میرم اسپانیا برای رونمایی.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22810" target="_blank">📅 10:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22809">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFSWKX6XHjQANTN0YpQPVWjnrLy-h1Eb6sRBY89Sp4pUry9zdLlJVGJjcsjo-kXKB1CM9ld515VvfU4Xt6vQzbQWks89Ece6HhzrmUJOiUjmKTrfNtUdiVEJF44V6gyPvD-DsrLtQN4UxleGsfCrEuKkly-oG3kGukbud4sUDmoGnYiLErHLGQzMtbEdd6qQPJtc2Efa-9B4UyYDCkvOFDjv8STkbBouDDSkvUqZcKiaxwYjV8-v-ZgeJCqtgcTbnIiU0wf_280ZqxZz6EoMqPDLZgwuu-2BxhJPSIJUu4KmDtitXxECHo1-ByEZW8T1MHE6oBHpGh832fcN0AwD2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شماتیک ترکیب تیم منتخب فوق ستاره‌هایی که مفت جام جهانی 2026 آمریکا رو از دست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22809" target="_blank">📅 10:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22808">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbZmzPDXOkcDU7TmsnFL8iesMM77mdtIp4BkEwvRHHN9QFAJTF_hqFmUBUaGI7vDTvfcOTlX7cIfxLZaLLPzb1CIV7drDFSSBBO3UJVbCaB_aGNNeeKHdMlbqXgaFBdNUlvZHjt-ysqr4F29GA6OvvJLU7EaguFrV9iALb0Fb09VYcixQtlVLh_ykwKZ2hyfaJcvS9lC7lZvqcvjAQ8hlRrXJ6dQ7l0waQQLwOSJdVJdRDusabySkPzpK8v5L7jmySLUEaPgBn4ojW7ZTuoFgDV2cdY8gSJBNRSNJNz9JxigGhwRmv_LxW93S-QA-MylsqG9lBFeCPsoIPi1NPO3nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آموزش کامل بازگشایی شیکه‌های کارتی ماهواره که مسابقات جذاب جام جهانی رو پخش میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/22808" target="_blank">📅 09:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22807">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAGybmzASJENrYK0f2kDQ-ILRetOzLtypTbenIACjaOflvEb96VOExUrY1OQvjv8Ndjmy1zMHW-eIVSO8agdLMBMkS1-3zuKPIAkjBwC7IoyZ1ujieGkMPgVwSeD6Xi1lkdHfOMNYPC7U1AfI5ik25t6KDyn1G8_Mm66VCyOJ_8uYeAqiELKUq8dK4VYXkBDKwRNuaaG4zMSvMlvll9oMwbsUUvq3RWhte4-1uCj_sIcN1tMAV20C3KW-WfL7vNR4gqtGsTpKZtJD5cRdLDlb9SDLxWZh-KjGRbXMOUm9DPiuvbjt8xaIe3ElqmMmcnAH5FYv8rOTSFZTzLihtBMCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/22807" target="_blank">📅 01:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22805">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7RKqp4rHP0aPZPNsYBWt6YMlG4d-b8Meb9oIFu_ebfG8pHu8TCHQwdtK_p9PMQloKsMJ9r1JCJc4SXyRoB2k6flXFyYcwELTzVbKa5K3UU5jts8YQIoQSvZ1rVrlxgh_BKWf6OE9BWf2VOpZuQfabtWYLe1xG3SKTcyafVQBHo3TOyrSPllNRQaVwUOgQEEyGRCFMRjjjCxgVtXRmOd_RGT-LP_HQkTuaKqF3_HatoJmD4-_M5d-dmcn9INPQVHwVnhH8_P0yN7JR2s7mmR-10worItJgLqdGA6_I_NRw0aFgxmrQ13lqv_n2A5vNJGvFHqbrGQmqalo1ltzhnAgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/22805" target="_blank">📅 01:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22804">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwJ1Fg38uxVpF0WFU6roA1wfYGXq5F67U5AJF6VlC_zFFpSqGcOmFTnD0n8JSTq4zJkXRZ4966O3zJ8hqOlARI5ij2lEEbvRj-5dq2vxnwu9I3ggDWZGph8BY2ZPtOyzdTnUWkktxd5yYFfXZ7vLS2RiVh2XPNBlP9qVqJ_Rzs5d5E5TYsc-ahagx1MPJyOaGgKihcYBZ5_dMaotiV7-zzYx963C3TVANMzpBZGSKvLnDTebHh19Sz9dNYaDQhjoFiB2Bdjoc48bwWFo7-GDMQazjwRPzNj8db1XGv_jtN2ZIgqEB6l4xSoVZlif0DLfwJh5VKmiWqWNj5CsRgfs5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارهای‌‌ امروز؛
مصاف تدارکاتی تیم ملی مکزیک میزبان جام جهانی برابر یاران میتروویچ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/22804" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22803">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTdwsdQLci5frYQ0799UXRDeg9BmDgTsCyUxKG4TdXVOjvZRphpY_2upaRaFftjxKmVszbTYhNv2yNyLWPVkRtgq8pIDj-jFp0SpMraD5UoYmW5Kcm7h7dlT9hnIJMHam4ftXpO47g_K90GXLWrxVlv_NTDHO2Bq8T0Q9NDBCZu3_HzFUVdp4BMgdFWCgQOBP0ylW2Nw4SbiIsIpXDsOsrWPAqogKQtN0V9LgeTgIRC8no_nqlFKW9IJqyyrEtcrFVw3MSemUbI3lWCY4gYxIcesxbmmMBwfhhG0UmBKxaujclZ1Qj9lYA79e-_QQEgsNd-nVAD_qtKShnUHdgm_9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌دیروز؛
توقف شاگردان دلافوئنته مقابل عراق و شکست‌عجیب فرانسوی‌ها برابر ساحل عاج در فاصله کمتر از یک هفته تا آغاز جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/22803" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22802">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MY5bugHTTqPNoe0kb2JoHo-h35g75_Fj-bpn44xK7Oa8dEp_MjiyIkJGPosfnJwU3jsbXiNgE90O3UeCwJQsN2G9oa_YxAUn9MBqxrlZlu8RPnEQsSsmi8vzCJ383PMSbzoH43VNv0UiDGprOT2laFFcwDMREClxBnU-gcMcRaAYfX8trufC1rsVssBy_7wzXd-8Ulwk7TreriZCTwlK-NheRB68pqUlGR2ggJrBCE33iQ5Jsoiwgkd1eBduJjgrVFluPS5vQc3MIlKfFFvWMGgRqVjaNln3A4CXd92-rfEXXWnUmmEmUAgchien4-SzbgMstxvYAyg_Vvc2UL1csA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اکثر خبرنگاران و رسانه‌ها میگن منظور فلورنتینو پرز؛ ژائو نوس ستاره 21 ساله  PSG عه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22802" target="_blank">📅 01:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22801">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2F7uIwUke4694C1zUNu5saTfohxJ5Uv3UTaZde4UK8JIq4BmG45tiNo6hSwPwT95x1pR2r7ssRdKEwvfdN3A9MRPpqfYHcBi1-pm-udz80dlig2Xbm19ksSAlu6rOevMyN9r4yCbTR4UU8c-FckdakpwqcdLQpW_PRln57X3lRGj9rBfOjLMeM_Xz4mbL5OthNRTOtw5K1dWA6hbttXqfzNzmGrnIk1HimkJka4YC9j9McPxK4H1A3166YPTrf_SP4gOfJG7HLEMfVHqh6G8kOA_BIfc592tRZeIGYyoWFOAs7njfiPjcud_KGeW1Et7MXq2rJKEkTd8HhQ4gguZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فلورنتینوپرز رئیس‌باشگاه‌رئال مادرید: روز سه شنبه برای‌خریدیک‌هافبک از یکی از تیم های لیگ قهرمانان‌اروپا پیشنهادی 150 میلیون‌یورویی خواهم دادم. کیفیت‌این بازیکن بشدت بالاست و بارها علاقه خود را برای پیوستن به رئال مادرید نشون داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22801" target="_blank">📅 01:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22800">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb6f9bc26.mp4?token=o4LPgxnbv6wfeu1vU5zWrBsiqYPgwc2xAWz3RFw1IJ0ZKzZ87BJ9TTO4bj9mxvpM5knvW__jxUTXbd4OerS84UuRcHu-rzzd1qqPuE9C1wIPu7iavVN6Nm_iVEc31IwFEONEookJhKjcYmRRCIv0g0V007A-ohFm-odyBmyzJQPmLQ0REkkxwTRKviptQJuccKRtuJj_MZm2HCWxSBC9aQzdTizkmFuRtNM9Kj-ZzIRrtZB1o7TnpF462hleTl9VlcDbtuLtZ6fVun2Cz2HDDgCAKPa_fTGeybggN6vtaXF3smpyllygJH77FIY7z3FUf9sM_HDPx2yEsptVN_PeoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb6f9bc26.mp4?token=o4LPgxnbv6wfeu1vU5zWrBsiqYPgwc2xAWz3RFw1IJ0ZKzZ87BJ9TTO4bj9mxvpM5knvW__jxUTXbd4OerS84UuRcHu-rzzd1qqPuE9C1wIPu7iavVN6Nm_iVEc31IwFEONEookJhKjcYmRRCIv0g0V007A-ohFm-odyBmyzJQPmLQ0REkkxwTRKviptQJuccKRtuJj_MZm2HCWxSBC9aQzdTizkmFuRtNM9Kj-ZzIRrtZB1o7TnpF462hleTl9VlcDbtuLtZ6fVun2Cz2HDDgCAKPa_fTGeybggN6vtaXF3smpyllygJH77FIY7z3FUf9sM_HDPx2yEsptVN_PeoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇪🇸
تیم ملی اسپانیا امشب با این ترکیب پر ستاره در بازی دوستانه بمصاف عراق خواهند رفت؛ فدراسیون لاروخا ابتدا قصدداشت باایران بازی کنه اما بعد از قتل عام مردم در دی ماه پیشمون شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22800" target="_blank">📅 00:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22799">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcmpPjGQIa1uUp9-kE2mjNMTVBGs4oyFtLGq4WVEAhFhWKvRlUC6QZ0xlwpsALYs9UJGA1IuIOYcEu8DmqBO4G_QBckLfXa3Uso89F3c-W-STc3fnpHjXxuDj1A3O7lYeMoNkAOiWjixTpF3Sts7Fkdqcv0xhE0FEdCyQqpJAl5QA4mgGLeXtpyCcKgw_vO2ZVKeYGvxUAuew5rCD9rcVMXM_U4eZoNlOMSkgNHJcSZDpsjgqt6i_17TMaWog_Y2d4xYvt9j1TfYkn9AT9zOZulR8z7guN64aQs7aVUbvHIdtG51vbl0GPMJf-9n4nXBXrg7rUNzTktMkdUZOxnllQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
برخی از خبرنگاران اسپانیایی مدعی هستن که نام‌بزرگی‌که‌فلورنتینو پرز قصد داره بعنوان خرید جدید کهکشانی ها از آن نام ببره انزو فرناندزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22799" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22798">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e2029a699.mp4?token=dz31is8iEyXMAnr6hVv9CkWszJ55-QQJD1v571v49u-7kMl-Btlu8E3u4bQqGxmMqJFOaMwP7gixiZ9Y6MYvzOHrLF3m7SdlEHxLJ_OYc2d6MuYzFAPzhpAoZSEwrkSQuceDd4O4UT4d3EqZRTy9Fid8LT5vfmVozF7H7m081e7yPNPm1u4xsPVHRqEvz9ThasIrejfsgkmGalSVZrFOS20zn-wcQOm38Dl3-w2CvnhCjE-r03yF_wp411AFOg50k-zyC6utJvuQeFN3LZy1KjmoDY73xmGi40CfpKcHU-VzhK6dcIdpO3DEoxCVsGX-T1TJ9K2_5bLYIBXVToTZAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e2029a699.mp4?token=dz31is8iEyXMAnr6hVv9CkWszJ55-QQJD1v571v49u-7kMl-Btlu8E3u4bQqGxmMqJFOaMwP7gixiZ9Y6MYvzOHrLF3m7SdlEHxLJ_OYc2d6MuYzFAPzhpAoZSEwrkSQuceDd4O4UT4d3EqZRTy9Fid8LT5vfmVozF7H7m081e7yPNPm1u4xsPVHRqEvz9ThasIrejfsgkmGalSVZrFOS20zn-wcQOm38Dl3-w2CvnhCjE-r03yF_wp411AFOg50k-zyC6utJvuQeFN3LZy1KjmoDY73xmGi40CfpKcHU-VzhK6dcIdpO3DEoxCVsGX-T1TJ9K2_5bLYIBXVToTZAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلویزیون‌کره‌شمالی‌بخشی‌ازدیدار کیم جونگ اون رهبر این کشور باتیم‌‌فوتبال زنان کره منتشر کرده‌اند. دراین ویدیو بازیکنان دوتیم‌فوتبال زنان نا‌گو‌هیانگ و تیم‌ملی زیر ۱۷ سال دیده میشوند که هنگام قدردانی رهبر کره شمالی شادی می‌کنند و اشک می‌ریزند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22798" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22795">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJo-QTVibiCIjP5rjT-nGA4jSlhZW_mB0ah3DdnQQxQlSvq_LKWs56QfoRASqtgxHxIx62OIhOCokb-8pBKkeLI2eqy6NB8SwovRI9nSLoM1zHfFaXeGVnIXIZRn1n4naoOITMhu-4dB85CPGWvx3cGODHtGjNvWdEJa_UBZ1PpXGoHo4eNtqouHvBtjBxkLA5Zz1GWwd-8eEQ_RB5baawY52cUiWixPA1bITJHri9v_IuOa3QJyA7cx5NR0CAnY3aPTWfPczivWf-9K1XYc9o78BFbtoRa2vXy1P2pRHVbNGLPmCQGfzP30AFdQO_6xEy2auXkk-YHtg7737FCOVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ نشریه کوپه: امشب فلورنتینو پرز میخواد یک خبر بسیار بزرگ رو اعلام کنه و ممکنه بسیاری از هواداران رئال مادرید سورپرایز بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22795" target="_blank">📅 00:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22794">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⚽️
تیزر فوق‌خفن نایکی به مناسبت نزدیک شدن جام جهانی با حضور ستاره‌های فوتبال و سلبریتی ها
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22794" target="_blank">📅 00:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22793">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JK5YInhWNcBewnf10rTZvPR7rTQ6Fbh71db9epBZi9eXRfiD7UwqTWpiesvPRSPnR87AdiPnCUsj_sZC15uxthEQfU8yrIuSkg5UrYBTAXSmnMZqfnUEYIbHci9Wqn0FYOU5-urWqBthEsdzcbWoUgc56RVO0PiZW-DEVN0DzItKQ4ojficftECb04nHym-XOdE8Jy09517KNtMXJ8lcYj2KoKuTXPYJlSb0-3FwqVwnNezqIommI8Hhfye9KRJOeOPfkR9HQZy2tsWtqtKbzDyIOO3pIwXFXnk1ehn_HxTZozAjMCUIByYGOzoH_V8F1_zfb30c-1izyeuhA8EQiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
با اعلام ایجنت مونیر الحدادی؛ ستاره مراکشی استقلال فصل‌آینده نیز دراین تیم موندنیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22793" target="_blank">📅 00:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22792">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeuiJH8A8d7s-x3hef1RYVLqcG8yW9slU7RvFj4usUufT7_Sx5KnxLEyvnSE8HxmuF8C14FLeF2Bpj1cGNjlioRZMSr_KDNfuenmVkGWSaryCeUWVB2TdRkbWDMPlolPTRpi6LnkQygUAU6Lil9oAwJTm8un02HEkiKaGdmLEp3ZTIx9DVAkxCHnVpcqbdKca1mwWqFdO3KTCwIwndEyJwAsbd9xRKrpeciyBJ26qfgrLfz1D-cc1wPlgjmNslj3CNFTS4r2Kn371N0VGCNlfbpJSy5wnVs1PAUj-wBjyvm6QPM9eHseri0SyJ2yMwTPEScamykNQkt0n3tyqvHqlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آموزش کامل بازگشایی شیکه‌های کارتی ماهواره که مسابقات جذاب جام جهانی رو پخش میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22792" target="_blank">📅 22:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22791">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPPIlnsucSUrEpQx8PT_IZVsWn4bWBCaHVZTipOmEJE86kvrAcfoI7DiQILp4OVc7-qtrfs9-GEINS2j3t0YX6VBB4gUdZGsfEdHXdXnxGPJBvPvEPbqycZ03vhHoVD1qx9JDPhJ4CWdFRrl-wNbLCNkohNrXpL_qH56IP8UviJMq4_ZyoB3TOWs3eEQf9cA8zKU4fUeT00eBZas-iuV460yM26w3ZKQ3lokkDSTzR1J4y0sUSWAfDIlty2HhamZ9PtfPmzcoojD2DtDqTT7R54RquHctWmJJFD5ca5AknDLvQzI2QM-s_IEtbQRBpc0ZaGwkft5EQjfFUGtCJVkHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین تیم‌ های تاریخ رقابت‌های جام جهانی؛
برزیل با اختلاف در صدر جدول تاریخ این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22791" target="_blank">📅 22:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22789">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QqT3ugqh94kxANDzCZKbLHMI5Fu40-nO_rFwosDMd46p4YDrbd-Uz3203VZvDfRRY5IuuachUex3PSfEsvDFnn_uPQMGKu83-dmu8uZTPUlXMi4AC7ff7weyPQjqR4TsruQsYccx-GoNNhRrAOoSpxIDV__h1dy6_ozzlqrZW4MMxCrfRn9wT6IfehCcv5Ok7f8kG5MDBBS81Uulyg8nB3ZTJyTnwuSdM_rqFMx2Ur6Ulyk3bdk7rteIz4Cxi1JbqE-IYZCOThkg_LDZDe-W34a560-V6dHVq1DbPGfoLBLbRN0X0yyfzv328P965YW31eD0PDiHIJb6JvpTyqtG4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ic5tcxHaLGPw6AFBtZygnxtrgbTzgCJkRXNlePa0LxAUSkANk113V3iriEjWhxQl_HI_axrgYfkEVOXbDqFU4SQUQQNZMsKGbfh-Z59YLvz9SfrrEdhtQmImGlPaT5F5xBR3LhH4HtQmtQ2VgfqYAUOW6jEB-OWDfO-Bz44ZgLMOgt6u0LHEX55-SBOhA8Von0V6t9qvhoVWqxHl8OgNNVAN8avsD3NLkW7g3dAGUUQElL3nXvrDr3aT8FXpBgzAYZSgzKyJGbFF9tE7IMeCEkzj1B60U5_cGdQl5auGlmJN9olWiMJfrKi8aB_GohXt-YXbP7o8ogZaynAo4hgbvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو: آندونی ایرائولا سرمربی 43 ساله اسپانیایی با عقد قراردادی 3 ساله رسما بعنوان سرمربی جدید باشگاه لیورپول انگلیس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22789" target="_blank">📅 22:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22786">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e7361d2f.mp4?token=OqeUJBLvQ8MwOOVW_GoKKIXHJnBpKPJa3ORkFVv4DDKmeZfKreRv-xGog8uxGWZmMu6wASSorCiVc_CCI-c_zaRq8PfLUY9F-priBY9wpdeI1c9X1bh8cSAWBmBMBPsyjqBmyrm2pAvRHxthyLBooimovAs8quf2111uP5d9y8WzFvb0AAyASpDj6mSYJS_pOBU9pfkANtRRzgGRBPrK6EjMAcnn8zEV02EzeQBhjMNdLz4d_8zJ26sQHE1RwM9x16_U-9Gm5SILfSmGvM4m7DDkLUvXV0W891A5Vac0JVXpuRp0WbIgBt_zZb_Y9PnEW2c1geDolikaFyw96G3_IZcpBGqyABBWNKIO5CO821fxmUEn1oMnlMlTLbvLfnldyjtiJo8XP8oGUgOGNOpS_ws8V7bTQiURVs3ruH7KMwpl1EB6wpG0zQyIcfrUFmX39SC8b3jml28Ke-MjBQesVJQe81pCEqS3KgJqvCQk08XWFzZlEmAY2K1krr8grb6aBtyewQdJ9piOROZP4MP3VyGzFruIbH1RU4tEj6XKqO89LFNxuGVM5piFetBv639n1u8K-HpNs4GaJfHec65UCmv0c8GD_N-WmpSsl-jEn2w5fKe2t2XXrgV-gaOzpjlSc1UrcFLDkAJ-9QBwbW2AIM7zNc66yUmgaF9jIEW1KAU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e7361d2f.mp4?token=OqeUJBLvQ8MwOOVW_GoKKIXHJnBpKPJa3ORkFVv4DDKmeZfKreRv-xGog8uxGWZmMu6wASSorCiVc_CCI-c_zaRq8PfLUY9F-priBY9wpdeI1c9X1bh8cSAWBmBMBPsyjqBmyrm2pAvRHxthyLBooimovAs8quf2111uP5d9y8WzFvb0AAyASpDj6mSYJS_pOBU9pfkANtRRzgGRBPrK6EjMAcnn8zEV02EzeQBhjMNdLz4d_8zJ26sQHE1RwM9x16_U-9Gm5SILfSmGvM4m7DDkLUvXV0W891A5Vac0JVXpuRp0WbIgBt_zZb_Y9PnEW2c1geDolikaFyw96G3_IZcpBGqyABBWNKIO5CO821fxmUEn1oMnlMlTLbvLfnldyjtiJo8XP8oGUgOGNOpS_ws8V7bTQiURVs3ruH7KMwpl1EB6wpG0zQyIcfrUFmX39SC8b3jml28Ke-MjBQesVJQe81pCEqS3KgJqvCQk08XWFzZlEmAY2K1krr8grb6aBtyewQdJ9piOROZP4MP3VyGzFruIbH1RU4tEj6XKqO89LFNxuGVM5piFetBv639n1u8K-HpNs4GaJfHec65UCmv0c8GD_N-WmpSsl-jEn2w5fKe2t2XXrgV-gaOzpjlSc1UrcFLDkAJ-9QBwbW2AIM7zNc66yUmgaF9jIEW1KAU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بمناسبت شروع رقابت های جام جهانی؛
بخشی از صحبت‌های شکیرا خواننده مطرح این مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22786" target="_blank">📅 21:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22785">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39ef7da3.mp4?token=Pct1IaMO0AJvbNRmaT6yrsMhjs_u28Vq-rbGB-uV85Og9sFNqiM5WlFlWEOFzMlJ3vyig9AFk6X_LsCC-smt1GmpMlW_32X2i7pKG6HNNEe9oFG9AtLHhxsqNYMafM2k34656QL6uVYncwBUbHzFEGackqb8TJkqkw8YfllbaTghtDawUT0GSRMgdQnJNjNeVqyzidvMTUzZRfDuVXR5T55ERtjjZkIiSXcFaZK9T95B5fX9HbB8cgmLDpgGkJv3shYovoGIMkeL362oBIKcOTqh0bPxTkRV_xMaFMdVktFqgCFBfRQKlPpD4XJgdz0M0q3tIkG7aGMINYVM5-msYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39ef7da3.mp4?token=Pct1IaMO0AJvbNRmaT6yrsMhjs_u28Vq-rbGB-uV85Og9sFNqiM5WlFlWEOFzMlJ3vyig9AFk6X_LsCC-smt1GmpMlW_32X2i7pKG6HNNEe9oFG9AtLHhxsqNYMafM2k34656QL6uVYncwBUbHzFEGackqb8TJkqkw8YfllbaTghtDawUT0GSRMgdQnJNjNeVqyzidvMTUzZRfDuVXR5T55ERtjjZkIiSXcFaZK9T95B5fX9HbB8cgmLDpgGkJv3shYovoGIMkeL362oBIKcOTqh0bPxTkRV_xMaFMdVktFqgCFBfRQKlPpD4XJgdz0M0q3tIkG7aGMINYVM5-msYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
جمله‌ای که تمام راه‌های فرار رو بست؛
فکر کنم‌مهدی‌طارمی هم‌این‌ویدیو رو دیده بود که جوگیر شد و به میلاد محمدی گفت بره مقابل تیم ازبکستان پنالتی بزنه، که البته اون پنالتی‌اش رو خراب کرد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22785" target="_blank">📅 21:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22784">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbR1cZnzuIMtErKyDSMiK2_zGHdjawdi4m5PXk85hp7HRU1ixLPwkP4E30P5NwMuNYtV3eyBSLLROiPten7GU9gnL7oGUNxd0hShRJtfGObvrgvM8TDD0iyxVwvKVC1WnbYFXb9MivWQ3xaymT5Jg15RAQmFCNxXLyaLejPvnlZAmUHsBT74aLO_L9OJ4tBd4yJdwwzi-gZpKJbJC0SHc0F6RDloPxz3d_hsq2U2oOzvuzr2NDRaAq1QOm8Jvz4_4frwKvQAPEwkLW73IAx5PTgvw-8iiq8tIA65JxXBka4as8k-IzFdh43h7mTpFzbnxKg-xrZmGkdSpqsgsEmxRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22784" target="_blank">📅 21:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22782">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bi53YPWqIkPxGw37mKAgwP2mUhJrwEdPR9aZffAV7pHyP4__WD_e1vazoV_ZYGu84jejlFm111L3xkL9_ogsYT6wv0vtXiNZhvTGifRJalr2_y9CW7NAEe3NtXZaa6HZmWfave7KvcgNKc9kF4Q7ff80BJtBXYSCzMCP-Kvh-GctRx8owc5VqKdkxUXdMWT_sPCkxtXV569I_Hnjofj2-v9ttEJ2XzQzfG5vhj_PFW2RWLgVrKu6x3-KvIw1AFfBArdfABB2fwx2E2LVT-RodiUNJy6Wpe5eh9nwwaFLCYcJYelPHbn5Z3XPTOrifPHgRIJABsSFOr4oZcmL5oYAuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X3lB7F98BW-bOGYhu518vEKdxhtpFK3Owouzplxy2_s_tgyphC1uk_pxV_pq5dOVyoD-hwnfPd-03w2oAmTPS6kgcLeu3uiDxLKH2lnjO2-9dvBUrO8aDeExzkoC1s313OAXQAq5fZq9kNVKtLxPlkOJ_bvt8FxbXB1RXCDsDbTR1m1Yvfuv4TzFzR6JILNQnd5TfbRQI6MWHcoRiXh845HbZBAh_JKe46IBWTwWsFz2mEMX_4bvU3ymboCLVYYn1Da99Ci5Ca6LN__4ZKNAPDdVZCao-oU-OMMid6edZk0iWI3NgDqgkKBVMCo5fiVSqFL28Hyi7BswVZnR74hxxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22782" target="_blank">📅 21:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22781">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tm-a2frn8EIMwueVqEXIHm0vYGzA7MNc1mWJ7tdLgXhsMRQRRvaADCVUqBMqZx8mlhzgMzCjt4RowSgHvLCHBKKoHO5Ui7ZJ4vmih9x4ik62jnqg2xpAaWI6MiC6qJbUS4qm80XdB9JkBVAesIIe_JleGfM5Ls4f450ELsLxvspjQJdNzB8-cpm3v6WJ6smNzszAAGdq9W3Ht9i8EcnC6Ck_sBGTr5F5oiQMUuqV25IW25OWT_0cnhuu7asQ4cHBI4i9Q_ty-hHjD47Y_YejoJ10fmyanBJXGYX382q8lhmiA0QTbkcEYIxdfCZUA2oi4emaJsFD_XH0ug9k_4Lk2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇪🇸
تیم ملی اسپانیا امشب با این ترکیب پر ستاره در بازی دوستانه بمصاف عراق خواهند رفت؛ فدراسیون لاروخا ابتدا قصدداشت باایران بازی کنه اما بعد از قتل عام مردم در دی ماه پیشمون شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22781" target="_blank">📅 21:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22780">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLCchnVh97ahpSve71ZoWcbACMPyt_4X9eSkIGqw5Vl73u8aKcA23CxVBAZU6rspa5idqVS5QNn1jQ8_W0dAhNUwkmNQLas5zM5-9PvoD_-FXIsx4BXprP7vqPfFHw9AWrTujTS1p6qXqtD39TWqe_u8TZDouX14HVv5VesHsGlR0iLl0msNWSH3ZlXa6Y0xWQsHf0iGxcJIbVTMU5r6tNOQjoN-lfCuNYPaRup3XRlZnTqq7j2nXoqfcFCJxfEo11yqCF6dqHybHztadMvA1pWHtnBvQQDRqvC9wKq-1V-kdHEgP1SBBAwENez94IJt5rokItrEYiAjvdbyweWvvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ ادرسون سیلوا هافبک برزیلی 26 ساله آتالانتا با عقد قراردادی چهار ساله رسما به منچستر یونایتد پیوست و جانشین کاسمیرو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22780" target="_blank">📅 20:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22779">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⚽️
اسپید با انتشار آهنگ جدیدش برای جام جهانی، هیجان بزرگ‌ترین رویداد فوتبالی را با انرژی همیشگی خودش ترکیب کرده. اسپید که سال‌هاست عشق خود به فوتبال را به نمایش گذاشته، حالا با این ترک تلاش کرده بخشی از فضای جام جهانی را برای میلیون‌ ها طرفدارش زنده‌کند. پیج‌رسمی جام جهانی هم اعلام کرده که این اهنگ در آلبوم جام‌جهانی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22779" target="_blank">📅 20:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22778">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAOHLMF2LsqTGCzauF9qOxn-of9nq-FpIrjTDiJn3mFuk_IcsMKolqSRGgT9nwV8omsO1AXrkwGQqz3NQq0BkW1GwEOTzmk2fFfXz61fYq_wl2HqFdh-OsmI_bMT8HECa_ldY4OBhaH4jRgJMiQ9vWRxXx5QRcAAgyGmAD2gSP1jfcnynF6a38ZtLVmj4QNGtQeq7e-Xup0KVjM0lfI6jVF7oo_ecQ9Jn7dnMO2lqU3j17xU7sLepG3n_c1K7vE3q24-MFfEFFWIaDXSffrXdBVkPMU1LScLc8kYJYtUpk_ERvSrTpVEjTHoAIlXqJ4Ia2Uz2mmoMQRpceLr19MGrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22778" target="_blank">📅 20:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22777">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oz3oeVqNQXCsOPxIFd2p1fUGGBChg2F-hYS-u0Gv3TN7TH5ZB4Y8QTiGT-sdPibZHrtA5l78jXv8dsn16xZtWfsomKJuNTZ9ALf3tZ1NoBIIDTliacKw4JFoz33l2WnW9uns4Rdz4EdY9hSlnuqZPH6lBX8oY0FSFzJCbSQYRbmCbdIekD02xxjMrgDgLxJ0ifaNemANPh7WHJphafppBHH43RsZpqNDqWqBQmb3yanoG2Gn080ELDwCzeZWgDUz2VNlMH9xzAGCAG8MLR7gbmCLJCidwynV_wPrjxDpdPHnBC0jnYtUkanApsRykpr_N-B5z3yYHPodSQRsYwjH2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22777" target="_blank">📅 19:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22776">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T69k-D811f6DKGy9VFMub9QGyP2SHDWYtb22dWsXlBX6WTtrXDd9de6crVZFgtsXyZ-hdP8I1YJmHH5wa2taSFWyIkz4aNjBEZnsyj4UZEFAgnGKFcuLJ2ypn4k9LSfBgkHTHUi_C-zNJ9GvE6jsG4Fc7Ij46QrUgVl46_rlnb7TXLePwkTC1UhEV7M0pTwi2B6Ng1SK3mnrliKS7kPwMeO8yL0ec08a_sO6xDCkHNtrsm4zZTwctYYf1jYs7tZDTIWvM73Rh8Imz8NfzWUNzQ6Z6GLCVpGcx6nLVAXopazh8JD2UcPFjG2WjbQWsB8mYtt2xW2SYXCJPRs5EsfFjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛طبق‌آخرین‌اخبار دریافتی پرشیانا؛ فیفا تا 15 روز آینده در مورد باز یا بسته بودن پنجره نقل‌وانتقالات‌تابستانی‌باشگاه استقلال جواب استعلام آبی ها رو خواهد داد. وکیل‌جدید و ایتالیایی که علی تاجرنیا استخدام‌کرده به او قول داده به هر شکلی که شده رضایت‌شاکیان‌وفیفا…</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/22776" target="_blank">📅 18:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22775">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CP-BSyyFJUikEKNCxaFH5PVOdhjNRBWM7uXqj-uEdSrptbrg517uYOJZGJYib8YWijMGOf-LXAI0oUm-pqHvMNIyHWWbATmTFrjGBUSRhamZmi0WkjHxTMu_lHG7UsENqQrBXC2by4m86Q-xYAUrROApRuRd81MupRm4ErxZYMtJkiDbAm9VBjYLLkrXkr2DfAtGf9U1KlKw1bL316R0_7QjQfEfnF6UbAhT2XHft5vMaGUS9P2FX-zIvuSpKFskj77Tcn3FJoDJLIlXongdUbjH1gCPWx0XqdZttgETwqx_9xpVuZdj31QnRiMwBPWqiGUQSCnzLRnOjQw14fe0sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22775" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22774">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoPsx0wAGQAKjUs4kkEvdpZ5UJ5OEQFsvw1H23m8M-91iPmr8tUXb-zHaC1Zn1fiMEyQWFZAqprvPQmu3wijSYFsdwR-JXokMih7vM8tEm43SYBnKDJ2FR7jM_XJdUSNfYxBlmIOtDG1fz0l4FwmWMOaQbMvqhKFdZtzL4zRFyQax0lTIjcXh5Dh5XT76RkL1Y_61i00eGtq6Kki5yYXjNLhX-yVIEcxMlgVjWPqHEmLzTlRPmJnFn1HpgVr8cbxDiBnOgAiN4eoF3usbkeabOROPKYz-DociTT_xvK6lT8LA-UkeB2Vb-oboVrWklcIKcq5D-Hklgtxr9y5li1agw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22774" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22772">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c00997812.mp4?token=MmjdoFJwXgB9SxGRkpRqPbF9RRXsY7dt2a_-_jDB2_9ga0gkd3ryZM8iC5BX9IzTb1Kty0nKVH7SBaY6WwHR4cnJADqRoeRqrZtdUJA2LwUfgWtnIeLXh8p0wA6B_opmUjHX9VFCwM3WzEoTVvCb6-TYOwgZcEYcR0J9gZkOG3FNFBI8Lo0ZdzYpG1s2SJCymYD9ZZri40le5WdtnkKrepwBswaWdR66gKFvZ7g6BnMVUKLaKM7jmENRBjLih1QTNQwmDK2M72hAdWGCMOkB0WnKOMCJiT_tSIsRFq794SSErhb1DFuQDVpmdnd2cHG4mVkkK5JZ6HAxdZKJ2PwgJDT5B_icOEsb6T5VZ9KjzyT4TmDqxZ8qn8B6s54E5N2suuwiH8gDn5dH__684HEb-G98ztDDLW0HJE7mYxuyng-xSC_b08wFqyr37f6GFtuLVR_wHFmVq0Lvwl_cWOG0hx5KT3KcPsW_OoJ3nSTwmSHTh-6keLXQoPBEmg_3xsr62_i84R_6m2I9OcqhOxCP6F65VfzLeNNV-UZLEgK1-3ieCgmtiyc7j07higESSvqbKsxMGc8Usczu2qIE_U3x9Obv2X79BaUwpuH8EEpuEse4LQ3u4R_iTIBXO2AbeHrgcAVzjIy5ncbvkCZD0x7QHcPvJWaR3MKx8n3SYluY4tI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c00997812.mp4?token=MmjdoFJwXgB9SxGRkpRqPbF9RRXsY7dt2a_-_jDB2_9ga0gkd3ryZM8iC5BX9IzTb1Kty0nKVH7SBaY6WwHR4cnJADqRoeRqrZtdUJA2LwUfgWtnIeLXh8p0wA6B_opmUjHX9VFCwM3WzEoTVvCb6-TYOwgZcEYcR0J9gZkOG3FNFBI8Lo0ZdzYpG1s2SJCymYD9ZZri40le5WdtnkKrepwBswaWdR66gKFvZ7g6BnMVUKLaKM7jmENRBjLih1QTNQwmDK2M72hAdWGCMOkB0WnKOMCJiT_tSIsRFq794SSErhb1DFuQDVpmdnd2cHG4mVkkK5JZ6HAxdZKJ2PwgJDT5B_icOEsb6T5VZ9KjzyT4TmDqxZ8qn8B6s54E5N2suuwiH8gDn5dH__684HEb-G98ztDDLW0HJE7mYxuyng-xSC_b08wFqyr37f6GFtuLVR_wHFmVq0Lvwl_cWOG0hx5KT3KcPsW_OoJ3nSTwmSHTh-6keLXQoPBEmg_3xsr62_i84R_6m2I9OcqhOxCP6F65VfzLeNNV-UZLEgK1-3ieCgmtiyc7j07higESSvqbKsxMGc8Usczu2qIE_U3x9Obv2X79BaUwpuH8EEpuEse4LQ3u4R_iTIBXO2AbeHrgcAVzjIy5ncbvkCZD0x7QHcPvJWaR3MKx8n3SYluY4tI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
ترکیه پس از ۲۴ سال بار دیگر به جام جهانی باز می‌گردد؛ تیمی‌که با تکیه بر نسل جدیدی از بازیکنان مستعد، از جمله نان ییلدیز یووه و آردا گولر، هافبک رئال مادرید و با خاطره شیرین صعود به نیمه‌نهایی جام جهانی ۲۰۰۲، وارد این رقابت‌ها می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22772" target="_blank">📅 17:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22771">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIXqg8viUsAXaJ97Vkv6ICS_W6TNYioMfAp3Tze8_Q1up-kOkdGnRcZtvXJP551Oq69lbmATNSA3Ct2C9_dztGddbC9W6lHD-etridAYhFOOvd2CYrvsVmZhN2QGanJvxJaxopf8hPpUnfZijfBsmgXUVQHJj6Bq9tFtmwEbUM4iGw55VYLcz88KWOEClqeC1uwnV7RC5HnFx9QYZKbCmXQ1f5Jexnv0oDItiEsX5Z7aBfaFRaZi2vCo1dmN6w8U7QkC-K7JbSM63KqJc38ibSwCFVvLL6_wRDNDPr6tomMvBZBQjwffbOrt9bnMK5LIuiuf6HRvZe6oxzZ6FBzX-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/22771" target="_blank">📅 17:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22770">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=AfdktKlNDXQ3fj62RAzSKM_jQV9aJ0KciQ4IeBgOkQTm1qVyTMF9haCIBLSZCHq_edrsk3LJN6_APhkQzQyb4ccOocToDtNnPO9HvbhXEYm9lyPBjMDgQzgr8Vnu2PrzJqvYJ0KhrmjQWQKLK5T26We3anR5aIe3pqMRU_CWgRMzroMh5hVP79IuRo6ewxVnCfuSHGIVSQ1DZEjJ4Z0donlNqHwEd8T-U67UAnyguqYWpGwc-wyKbKL7GRCvQQNyn6r6bta9uojARf0ttnknvENFlafBdnCIZ8ygpTrTm-Srp0Kt5x7yef7fnJ0hR7xKjKlopHSXPXVUmE9o7vDdOb3osgDUYuW8OueNeulUaIXikMMS9BhsT-drdEcPZb0WvJaJ3APKjbGBN0gGAPZiLAF97r7jRuS-Sl-FDjnfWOtAk4jqhvN2zL1cmzcp8kC4Y0TVE5i4D2zrDUvEh0bw8PFFw6amSKqF94H_EGQUizxSn7KKbdvIer-mdxrlMnErJro7XD6bsRHBhQ1uSrjMKe9tRtfRQmULyE--qoVv-Cbd0sD0oJneIiu3lHj7FdyzBwNMDb-64I0A530Ih8W5WCBtgikKlHSEObDv0GlyIsK5oS5nVZweq0t2assb8jT-v9JN41-mFfQa9Q-6STFLBW4jZueTFCGHtpwgJdf_hGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=AfdktKlNDXQ3fj62RAzSKM_jQV9aJ0KciQ4IeBgOkQTm1qVyTMF9haCIBLSZCHq_edrsk3LJN6_APhkQzQyb4ccOocToDtNnPO9HvbhXEYm9lyPBjMDgQzgr8Vnu2PrzJqvYJ0KhrmjQWQKLK5T26We3anR5aIe3pqMRU_CWgRMzroMh5hVP79IuRo6ewxVnCfuSHGIVSQ1DZEjJ4Z0donlNqHwEd8T-U67UAnyguqYWpGwc-wyKbKL7GRCvQQNyn6r6bta9uojARf0ttnknvENFlafBdnCIZ8ygpTrTm-Srp0Kt5x7yef7fnJ0hR7xKjKlopHSXPXVUmE9o7vDdOb3osgDUYuW8OueNeulUaIXikMMS9BhsT-drdEcPZb0WvJaJ3APKjbGBN0gGAPZiLAF97r7jRuS-Sl-FDjnfWOtAk4jqhvN2zL1cmzcp8kC4Y0TVE5i4D2zrDUvEh0bw8PFFw6amSKqF94H_EGQUizxSn7KKbdvIer-mdxrlMnErJro7XD6bsRHBhQ1uSrjMKe9tRtfRQmULyE--qoVv-Cbd0sD0oJneIiu3lHj7FdyzBwNMDb-64I0A530Ih8W5WCBtgikKlHSEObDv0GlyIsK5oS5nVZweq0t2assb8jT-v9JN41-mFfQa9Q-6STFLBW4jZueTFCGHtpwgJdf_hGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22770" target="_blank">📅 17:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22769">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_6iYEYUws8dIZ1iJXxqbXgFAzJAIiE6EBwlfC0T8q0KL6DandM6yPNpcoEi7Ss1Zf2IwStU_rUVyaJoi-9uik50BHhmzgCVUDAcK9KTLZkpem_jCTItrVSMcXQnJ_NM7hReObzmKvSRBVLhx2BFU8MJCBLPGk511G3SBlcQLc10lknZV2fywtmEJUKKmXBzqCYwniCu4oUyXe-ixDrid7A2AhS9qn2unM-7aiSVxL7_4k0LPHEZy_EoSwmQNMQSvQDxeV7Koc__H_68d3hOIpp7Vl8bANAcTXRSTUdHF2lVcwEES4OZjxmCvYET-ibp3n5dZUlQsTH5PzTb1RIRYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22769" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22768">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dje4JHpXBsOSCaS8ZepiqQPBevAXjIol1rQ6u0HmF3FWYwW1GNBeYJChRMns3lJcpvCUeRNjuLoy5sQtc2WUENHXFVfqxzSunSV08208wPlAYiOQDx5J-zDY343DnS9iUFZCrHnl-N_xJIi5I0KmeuHzGQ6Zqo7fyQE9VBqQMlSIWwRvT6G0CQTQ2VKGRhBgFjGVwevxO4pEyVwiTUbMyKk7prS7Ht8O6OrTmJeEnHtXGOvC07qlbL8J0rkkEJXxYmMec6Dr-HMIkVPc3aNbpO8Q7IGVRUVhESDR3LVYMLFk1PPQye7-RWLzj8O851fZvPW_2x2_yvlYV4dNPqEG1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی 30 ساله استقلال شب گذشته بدلیل‌عدم‌پرداخت‌حدود 3 ماه مطالباتش به‌باشگاه خود نویس ارسال کرد. هلدینگ قول داده تا 72 ساعت آینده 250  هزار دلار به او پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22768" target="_blank">📅 16:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22767">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcLWYAQtSvFbDPY4tzNcLLI031AiuRKbKgYfqQ8Tw3QxrgPRKy_gImSbbMKGxyNew5Kgy4RwoIb2AdvkttoJ7BOjNSGxgplNw_UplfvPIDST0ks365_1QNEqW_fZ0GIjtek62PuTXJTjwRnm96HDHYNJOUoFRnIqSHn7QCiLD3jvdGlKLbMCrrXekoPGACieO-dt8QXRnvFZaXdZLVP91EiRcxmBFFedDUq7_fGkj14-QSGuddfVJs58RRs02CY9qdtN_JXfu28HhB3aIxZvXvd5CWVdpbjJbqDv_lgmBOU4rDJP95BXudSgTcPMbNpxWPFRA6akskg3iuFyQv-DIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22767" target="_blank">📅 15:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22766">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tn3X1MLZ21Vu-WFZGB6YRh9BvHEWoR0ypbExhdIOMDalHlHUNzxPw31Aw36gE9uwk04q9NB55xDzhNbpEosJPhigsfMi6dE3lrax1cvpvn2ad2pO_iT3RkV6nSJzR9LNeT1HLV048xS6K5FK8_3tmUgJToHI3ovGjBhHsSyP1UnnuKeavvoKvKRTbbDragEoZAW1kyMvAim05g7KVqrs6TfBt389-IHZm2okWF94rrib8nB5Mfc8VsKNfccMg476YCb0Yl0-GpsBfTH7L3vo_xuibcBAVMxVDl0hUNjy85voqy4HlYqpddSKcbb4YSQyWwTdm7-85g3Ju0ChvQBJjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
علاوه‌برجذب‌قطعی‌کوناته و دامفریس؛ ژائو نوس ستاره پاریسن ژرمن و یوشکو گواردیول ستاره خط دفاعی منچستر سیتی دو بازیکن دیگری هستند که هفته آینده فلورنتینو پرز بعدانتخاب‌شدن بعنوان ریاست باشگاه به تیم رئال مادرید خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22766" target="_blank">📅 15:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22765">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔵
مسابقه جالب بین کیلیان امباپه و نیمار جونیور زمانی که هردو در پاری سن ژرمن حضور داشتند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22765" target="_blank">📅 15:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22764">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8Ujsu3L-7qqsc3fXIaCQWy4mkgtMMeShnHkkF9mco-ErG4AwTwYSqn8vVyugxm1sVDJuOqnonblw0RzBeWLaazs_LVDKHdWnG1iAJgceUMtdVeGxs5xOdlx8uQtzVUG1bgJJUJXngHeHa061IZma7zFFy_hH06ivPak-Mba0sNaD6aduD_-3rkY-1InTysrkeVWRY7GolRvm10zZosxovjI6wLczhaBTRU8TR15XVNV_UcMC5Lsp8w13RZrZYPQ9whgjDR7iGa35gygV9U3K03Myx-2c2hMFJOJNQrxQ0LuIfw4RnPzVkSNMeoEoAbmKqU51ALgvwE4T5i_ILg_gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/22764" target="_blank">📅 15:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22763">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLjAI619PDDjtlirZAwgQBxs_U5ZPxjXpTllFmwFwPcMaote-VvTfCT0PQ5Q_cYveHvc-Z7Ja442gi_R298JPmj0AKOymFaHKWJNdPIxJYrc03DCJTIE4i4nLN_V1-csp70qYqWOXa0iwANbR8o5wohpUDpJ3js420UUMBr-Wq1WPQzob2rAp9ZOadFofMxkDNqEnHvzvpLkDpbpRqfJtBTlBp0HqltaYGwyJFfd3DfujbQektJrIKMdMAq3fmMfuKPzBc3UcarOfJtchKLPGAdpyRTPQSjaL-hw5DDesCjkw4_BtrGNhtJsw14gX_2f-pY9Ez18fZSj9U3aH2eGZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این چهره که زندگیِ سرشار از خوشبختی‌اش رو درکنار زن و بچه‌ش مشاهده می‌کنید، همین چند روز پیش برای دومین فصل متوالی تیمش قهرمان اروپا شد و خودشم یکی از بهترین فوتبالیست‌های جهانه. عامل موفقیتش هم نه مربیش بوده و نه همسرش، بلکه فتحعلی‌شاه بود با تصویب عهدنامه گلستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/22763" target="_blank">📅 14:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22762">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSr6Rlxj17clRjXxSEVZCxgJUTTshIAqaQO5jPvjW9ExXT9ft7kqGVSxkpTGxpWOJgiBYIpla200B-BULpO5L9459YrxLjPapb_tFdhNm4gOD_6UEF4kKXIZCEZy4qapEBVlICnMxC4dsKT1T861N_yURtvZo4uKW20Y2r39yWKkjv5aB1Gd4NYu80e4beXf-5brL8zObGTsmyaOFjxyRonSgu-4FhTcDOrVIs4P_SR_XQ9DPQ_DUS47G4wK7eXMnCsS5hjW_ctfoGtOcAcv_5IeTzsITySq8dGEFO804cqpauF03Ru4U2ULlPtqlnL-gmgV4rqgsJgB3O7TstBMrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
رسانه‌ معتبر اسپورت 4TV کرواسی: دراگان اسکوچیچ سرمربی سابق تراکتور از باشگاه استقلال تهران آفر رسمی دریافت کرده و احتمال بازگشت دوباره او به فوتبال ایران وجود دارد.
‼️
پ.ن: اکثر رسانه‌های‌کرواسی خبراز مذاکرات ابی ها با اسکوچیچ‌ میدهند امارسانه‌های حکومتی…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22762" target="_blank">📅 14:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22761">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATbwwS4LBUckjBewFH_6f79Vxy0zlLu0MQE1D1Ba7NVh0jv3nzH4qnY5CY3oeBKo_Lg2mixcATjr3sskl-Bd31J_NuabX8LWRI3Hz61a3cKZ8B9uFTBp0GKH8M3a0IZqM8ix1rO2j4A6_asb7OgTx960oLwdCniQF-NxHPqEqFg8CZTPwE-v11jHKDfY5Ufylsp-IcfY3wG-VxKrhTCkvx3Cc3gv7nss0ra3ELv2FbgdB1SQy0D2gtMi2vHrAwDhnyAVfqQ3ceVDwKQmijgq-mvr61DNG37M3VijkV2oXD28QbEDgpx13GUyGQuwdswKnlpTyg5QxORiItDGHdX4sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ سرمربی‌کروات، موفق‌وسابق‌تراکتور از طریق ایجنت ایرانی نزدیک‌به‌خودگفته درصورتیکه تکلیف مذاکرات جمهوری اسلامی با آمریکامشخص‌شود و دیگر جنگی رخ ندهد به قطعا لیگ برتر باز خواهد گشت و به آفر مدیران باشگاه استقلال پاسخ مثبت…</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22761" target="_blank">📅 13:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22760">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2Z-R5xNAkrTSNNrYDkBxIeCg1u11UdDTjA8LCqhYSbgWCq_VANE5AOPE5f726Y0pzdehWH64Fdyh9MmPHbMr1ES4NWZAlcVC2qd6t9T2eUN2O2PiXrLK0b9WGCC3d2oHCXSp11DZxN85i4Re6CxvjUb1XpwG4OPI3mouh5AYlS0aR2o8iGEZHXbu3floN9m3Z8-0N-oK6s1eo91hSrBziGYHQEG1tM2wqhFanBKwTtGg7HWHwvdf_cNUNhilAAJxySc46gN5SbrGcCOYlWS4je_vg-EAkMu_iXPm_j42LhJZpJvGa3fPy40CanYT2WFj5nYyEA_f82liEilTG3vrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22760" target="_blank">📅 12:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22759">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQ7q_ifOp1PiA8jXO2r-jEYjGeDiG-dYDSvG61IA6EsDJ8ZB9DYVPIRTZp8aUHV7mFZ4A1w-sh-cyLMpyUXuH4SDfaD2dvSMenOUYMr6l7uliE_X27cW6oy9rVKW8s2XZaB50xqKjld7fTSliETZBunngmadkQg9OnvQmDT7U-IOFwYAogcZjVSUFCkXgBE5eTbdZG8UJndfSEuf4AAnAz5M6jJf-2yU6OtSEh_sDrHfWUhAU500nFl2iAKuvZZPRDV5ZkfcTaHfu4Q9sfisewNerb_NWBESa4JozmUsFjRT47oYUU3tvTesxXh7eCsGArVcJcJmVtUKNM3jIIx2JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باشگاه‌های رکورددار بیشترین بازیکن در رقابت های جام جهانی؛ منچسترسیتی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22759" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
