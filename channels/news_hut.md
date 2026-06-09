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
<img src="https://cdn4.telesco.pe/file/P2NsLXyJldXP7L6X52q6203ws2NgDAtTjUlDZDOvhVZp4P3jEiL8s9UoU4BgGCS9lJfUSqwQkmu99bIWLtFUHQlmj2KM0gDYQkRB5lO-_5RkoRy9piwaHHVtlInmpyi1c-1Dnzt8I62vuWlffNZve1VvuNgkOpViivJ_ooHG4fR_gq1eZbNH2Yveu6CReD2BE0U-ZpTYnsMC6ViX9EhM1qexogITrJirG1qssbu7B1A7Q8yCjrMfkXbpFUxPU6g4-9WvJPvmIsIYm63HHeUwS70W0stb9qP9Iwx5YydTnj0YrBGJRMUK0SJcMo-G2rOIgu8DYvhVEFFCvm_pxKvoQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 227K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 23:56:59</div>
<hr>

<div class="tg-post" id="msg-65581">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
دونالد ترامپ در گفتگو با وال‌استریت ژورنال، درباره حادثه سقوط بالگرد آپاچی گفت که "مسئله خیلی مهمی نیست" و افزود که خلبان حالش خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/news_hut/65581" target="_blank">📅 23:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65580">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
فوری؛ خبرنگار:
شما گفتید آمریکا باید به سرنگونی آپاچی پاسخ دهد، آیا هنوز هم این نظر را دارید؟
ترامپ:
من مجبور نیستم کاری انجام دهم، ما همه کارت‌ها را در دست داریم. مجبور نیستم این کار را بکنم اما ببینید، احتمالاً این کار را خواهیم کرد، باشه؟
@News_Hut</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/news_hut/65580" target="_blank">📅 23:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65579">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
شلیک موشک از خاک یمن به سمت اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/news_hut/65579" target="_blank">📅 23:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65578">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">📌
۱۰۰ میلیون تومان جایزه نقدی - بدون قرعه‌کشی!
📌
​
​
✅
قهرمان جام و آقای‌گل رو دقیق پیش‌بینی کن و کل جایزه رو برنده شو.
​
⚠️
ظرفیت محدود:
فقط برای ۱۰۰ نفر اول.
به دلیل حجم بالای درخواست‌ها، اولویت با کسانی است که زودتر پیش‌بینی‌شون رو ثبت کنن.
​
🔸
برای مشاهده شرایط و ثبت پیش‌بینی، همین الان وارد کانال زیر شو:
💵
​
https://t.me/+5uTOXJ02mftjNzQ0</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/news_hut/65578" target="_blank">📅 23:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65577">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
🚨
♨️
شورای امنیت سازمان ملل رأی‌گیری درباره قطعنامه ۱۷۳۷ را پیش برد و با ۱۱ رأی موافق، بررسی بازگشت تحریم‌ ها علیه جمهوری اسلامی ایران را تصویب کرد. بریتانیا از فعال شدن تمام تحریم علیه ایران استقبال کرد
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/65577" target="_blank">📅 23:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65576">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
خبرنگار یدیعوت آحارونوت: حملات آمریکا جوری خواهد بود که هیچکس حتی فکرشو نمیکنه
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/65576" target="_blank">📅 23:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65575">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNTkn_lEo8VO1ba0YrtG8uJl26TFRsRMFEG4htgVpkCCwxAfUyDyP7HoGEKd3g1rJuLqYQY_gIhCKIlBJNLhXNAHsE57kA9Uso1zgp3zjbmme7N91PVnCceVncIMA3VJYjfdVTgWGwGEmPk1LTwcy1TDOkG3mAf_DtBb1bmVNiOzEPr105nENc7D2W5Bonmu2Ak3xreTk8Ao1LHT8OlDWzNoltxNoqfspnBSXOxWdynf1m2gwVwDImG_875PISXrfPRHaBeWo3zyS5CETpXQTkH11BZAZaXgzSh4m6I_DRlxGEqLKLCDBSF_kOtmw99kdwnKBSpKFg08C2ScdRU3zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
لیست ترور منتشر شده منتسب به سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/65575" target="_blank">📅 23:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65574">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyT8GQQWXBNvrRB5wAuAZ0NlNreSHCbmqbFUufpWELeH1Fw_0PkeRsRHZuNeYBSjeeXArL6TCBXYuec9OK798OB4vT-CEKOpOraYUGN54DaTzdlwraPRShXB9c0AufCWN0LAB1_I0vrQOUacnHAeYaQvHfFMf6El-6z1_TBCoU8wl2JuC75YcRtSWgaV6vqDFURDRu9Sb3Cav7_5C4Mj21wyqF7Dtl3x_Klk1HnK2mfO6vgtu6SDNJAlpkVsZmz4MMj3mqV6Nds2AbYSf3IUyIYeEV-gh6GTjWW82gy1y92p4mp--hgxsftIkwOJpXYnxTiJae2ZkGTogzV7Pk63RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فضای پروازی ایران کلیر شد
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/65574" target="_blank">📅 22:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65573">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
🚨
العربیه به نقل از یه مقام آمریکایی؛ شواهد و نشونه‌ها نشون میده که جمهوری اسلامی بالگرد آپاچی آمریکا رو عمداً مورد هدف قرار داده بوده
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/65573" target="_blank">📅 22:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65572">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
♨️
حمله موشکی سپاه به مقر کردها در عراق
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/65572" target="_blank">📅 22:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65571">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39f367b1d.mp4?token=DbGUfUwKdK_x7chzAMxWt7G_BOlYnW37Apo3fkUcZ1M3PIg_RDbXAcb28Io4rrsjBxRr4ccm21ux8g6xuGh8vCHbhJgIuQMmdBW69njM6QaFnZi_amtxcDcmk9SZef7gk3nGW4dfLGVpcW6-8Cg5vvCb16zBDOPFwO-LSLutRCmxCk93JT27DWLh05Q1G265dkXTjqYTOp16s6BQmYEbR5t0LuoSB-e4COwsOy_-BpdZFgFTcDoycnIko2m3ljiCwFUr1MNvH-a4H3T3UPLpstwR_Snbwn1mIw0pCklg7jh3VZy9FWPyeP5zQAdUbkh97dsPvDLtwLDIoATifh9KKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39f367b1d.mp4?token=DbGUfUwKdK_x7chzAMxWt7G_BOlYnW37Apo3fkUcZ1M3PIg_RDbXAcb28Io4rrsjBxRr4ccm21ux8g6xuGh8vCHbhJgIuQMmdBW69njM6QaFnZi_amtxcDcmk9SZef7gk3nGW4dfLGVpcW6-8Cg5vvCb16zBDOPFwO-LSLutRCmxCk93JT27DWLh05Q1G265dkXTjqYTOp16s6BQmYEbR5t0LuoSB-e4COwsOy_-BpdZFgFTcDoycnIko2m3ljiCwFUr1MNvH-a4H3T3UPLpstwR_Snbwn1mIw0pCklg7jh3VZy9FWPyeP5zQAdUbkh97dsPvDLtwLDIoATifh9KKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
متکی، نماینده تهران: قوه قضاییه حکم اعدام ترامپ و نتانیاهو رو صادر کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/65571" target="_blank">📅 22:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65570">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3LCCM0heaqlLvofyIJcinNJF3bNXLAiHo7m0yEvCIQXnQsDWMI3aWNRFwbvU8TppeX4KFuBPV15YL5BV6L_wMRDihdDlaSfXYQADqhcCXwmVuwr56IVBBUl3SNVQrnV1y9wZP95RElVLLidYYQPzUkgp7eEqNANTIyiwH1xwhJ_V0vXhYd-JEFcluutG5-Fv_8X-jDeTueTeka563JmbTez7FMieLaI1cHf0f82IcSq6khMRP9lHkT8L-pLfJghZuvE4T8XbjcHYz3_aGqYj8qxnzCc_sEVSI77JPUGK_PNj3ubgvhoh-tQvDD7hth8pdk148pfxovfEM7T_jFdLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇳🇬
نیجریه
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
چهارشنبه ساعت ۲۳:۱۵
🏟
ورزشگاه دکتر ماگالهیز
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در
۱۰
دیدار اخیر خود،
شش
برد و
سه
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
نیجریه در
۱۰
دیدار اخیر خود،
شش
برد و
چهار
تساوی کسب کرده است.
📈
میانگین گل در
۱۰
دیدار اخیر پرتغال
۳
.
۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نیجریه
۲
.
۶
گل در هر بازی بوده است.
🧠
اگر دنبال جبرانید، یعنی از مسیر تحلیل خارج شده‌اید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/65570" target="_blank">📅 22:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65569">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
♨️
قالیباف: در صورت نقض آتش بس توسط آمریکا، ایران دیپلماسی را کنار خواهد گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/65569" target="_blank">📅 22:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65568">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f7a7445c3.mp4?token=ZjvfbgaHu6PjkkPttSNF9EYDf6ZlqQ82zgBoNSM8BGfnWpDvskxBN2-2Jlub5ICtnG5uqd_pBNlmS-Bm5zX0bnmtuJuyS3KpFYP99PmMwN05S5aUQzr03mNDMWcMTtTGpVVyZcD9yKq3OFMBAU8kzqN-dRYIMhNKu6QvFotH849xmgPMWRs6lFu79nbs7a0h6YmoemfXuTffqd0vIpd-4u5Mn7HsfnDErRqucSXfILLcxcfmlajdsgclsPS9NQHNt7E-SrgayHvMwtVOcAdEoyVgxlaGyLGW9HSDK-OVHo_jXeIu5fg7Ar5MXJYAne_47YiqZGh5KkJSIfAGh9zaRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f7a7445c3.mp4?token=ZjvfbgaHu6PjkkPttSNF9EYDf6ZlqQ82zgBoNSM8BGfnWpDvskxBN2-2Jlub5ICtnG5uqd_pBNlmS-Bm5zX0bnmtuJuyS3KpFYP99PmMwN05S5aUQzr03mNDMWcMTtTGpVVyZcD9yKq3OFMBAU8kzqN-dRYIMhNKu6QvFotH849xmgPMWRs6lFu79nbs7a0h6YmoemfXuTffqd0vIpd-4u5Mn7HsfnDErRqucSXfILLcxcfmlajdsgclsPS9NQHNt7E-SrgayHvMwtVOcAdEoyVgxlaGyLGW9HSDK-OVHo_jXeIu5fg7Ar5MXJYAne_47YiqZGh5KkJSIfAGh9zaRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
فعالیت گسترده جت‌های جنگنده بر فراز بصره، کردستان عراق و مناطق متعددی از جنوب و شمال عراق گزارش شده.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/65568" target="_blank">📅 22:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65567">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBQaMW1JAJsesHwkgtasFLbK_NXvG81rjQ8-T-JkZtSChVLSLvFetZEL-dQOk-GcTU6DaF2MC8F_hLULCiOsZMr6C_rWI6r463J6k5fX2ooGkN4I2TpzP0fP4YJ5OXd_ZbVq81Tmomah3Vbf0k4JHKmQ6VCCluF3YJ6bMUpHdjqN3ac_nVJ-nW-FLTbIYsS6AxQZcrMIARMPEG7y9XbmwC93gTOWehjQDLwfPme8RT_EyLoTuDcGNLiJJB99Trm4gD4bktNFgns6IHnnMLU83pzCRxMcqw7uUG-3HJ7HSiHHooP0zbAnlLdwriBHp8HSU6YXHZzlVUGQtXhM21Okcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فعالیت حداقل ۹ سوخت رسان ایالات متحده در خاورمیانه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/65567" target="_blank">📅 22:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65566">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
🚨
صابرین نیوز رسانه سپاه: امریکا به اسرائیل اطلاع داده در ساعات آینده حمله را شروع خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/65566" target="_blank">📅 22:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65565">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به ای بی سی نیوز: ایران اگر احمق باشد تمام زیرساخت هایشان نابود خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65565" target="_blank">📅 22:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65564">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
رسانه‌های اسرائیلی:
«اسرائیل» برآورد می‌کند که ایالات متحده ممکن است در ساعات آینده دست به اقدام نظامی بزند، اما به شکلی که به ازسرگیری جنگ منجر نشود و در عین حال تلاش کند تا حد امکان حادثه را مهار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65564" target="_blank">📅 22:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65563">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/304a0cf35e.mp4?token=OnESzgmsu4BSENvnzK0Ij68T2RK-s087V6FcXQYCCIA4HKrDH5yk52a5lZ5SXk3SJ3B-spD4J9dfv9JLqmnZE7-Hvc4N_RbD5NlolR5bu45haXnOiZTSqvdwHkYT-BVEd0p2yLffRiRHzOh-t5uZhA_J4IAp706XaawCDA_YWrXxnGY0S3u5v1G_GuoN1P-5mTyL7q28LIaDAD8AYJDTHiAhlWMr2hAztX_MXymHHM7aHU7Z9Akx_IkxJVos2Y7Irq45HWlJM-FMMpM9vf6zh7USSvOGlSQEeapYm1TTwEXJUJjF-3ty7JAUCSIIn4-bgUBogr0vFNAqrsndKbhQxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/304a0cf35e.mp4?token=OnESzgmsu4BSENvnzK0Ij68T2RK-s087V6FcXQYCCIA4HKrDH5yk52a5lZ5SXk3SJ3B-spD4J9dfv9JLqmnZE7-Hvc4N_RbD5NlolR5bu45haXnOiZTSqvdwHkYT-BVEd0p2yLffRiRHzOh-t5uZhA_J4IAp706XaawCDA_YWrXxnGY0S3u5v1G_GuoN1P-5mTyL7q28LIaDAD8AYJDTHiAhlWMr2hAztX_MXymHHM7aHU7Z9Akx_IkxJVos2Y7Irq45HWlJM-FMMpM9vf6zh7USSvOGlSQEeapYm1TTwEXJUJjF-3ty7JAUCSIIn4-bgUBogr0vFNAqrsndKbhQxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتشر شده از سوی اورژانس از لحظه اولیه حمله آمریکا به شهرستان لامرد فارس
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65563" target="_blank">📅 21:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65561">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">من از این کانفیگ V2Ray گرفتم، سرعتش واقعاً عالیه
🔥
حجمش نامحدود واقعیه
، بدون قطعی و روی همه گوشی‌ها کار می‌کنه.
تست رایگان هم داره با ضمانت بازگشت وجه.
تک‌کاربره حجم نامحدود: ۲۴۹ هزار تومان
دوکاربره حجم نامحدود : ۳۴۹ هزار تومان
پشتیبانی
👇🏻
@khadamatsup
کانال
👇🏻
@apkdownload_sup</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/65561" target="_blank">📅 21:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65560">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd8865cd1.mp4?token=TkzELwFSVsuO7ZJibx2x6iHwTm7OaMa7e-Uj8ZWlRMW7sntN8kcwvjgBXRNEWVJQi3166q7z6r6p9F_bzZ0GfxOcOVV_QY69sGT_LiQTPBseETM-mXZ57tOwSpA0urexdFCsy1CE1iOaE3aK0_UdNLhbkzoSWnYkb8OE5f6yBX04s2l3STpW9rl8BWP7oCea6JIl-qOPwjMtWwglkRJ60lTHn0cVJIfCFTRQsGCHPTYJe_JH3om_NzXBDjqA5JafIF6pZJEM0oREEUDcda5y_91jKbCZYsdMCt4sW9vtWlzuYeddPu_tK1cX4SGe1xCkLCDh5VmdslmEb7Lh4ubnzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd8865cd1.mp4?token=TkzELwFSVsuO7ZJibx2x6iHwTm7OaMa7e-Uj8ZWlRMW7sntN8kcwvjgBXRNEWVJQi3166q7z6r6p9F_bzZ0GfxOcOVV_QY69sGT_LiQTPBseETM-mXZ57tOwSpA0urexdFCsy1CE1iOaE3aK0_UdNLhbkzoSWnYkb8OE5f6yBX04s2l3STpW9rl8BWP7oCea6JIl-qOPwjMtWwglkRJ60lTHn0cVJIfCFTRQsGCHPTYJe_JH3om_NzXBDjqA5JafIF6pZJEM0oREEUDcda5y_91jKbCZYsdMCt4sW9vtWlzuYeddPu_tK1cX4SGe1xCkLCDh5VmdslmEb7Lh4ubnzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
♨️
فاکس نیوز می‌گوید رئیس‌جمهور آمریکا دونالد ترامپ «در آستانه دستور دادن به انفجار یک چیز بزرگ در ایران است»
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65560" target="_blank">📅 21:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65559">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kK0mWQ58W_OBpyPdF6gEdIEl5DqLuetckNv9fMnmaww1lVdRFw4IHCuw5ZBda956pTrv34iV-e6OQyhEMpHNGaCNIvFhqBvrsrepO79bAodIgWxzwoiLXk490tarQUlAyr1gkxHShgNnT-Cf6w2atPnOrGEKf2fuaSz6k5DXoAr5DAUcaCU8jKSIf8b0bC-r001PXOZ4Qu4agaTqIweWIqOnk7QegNFdoB8kj5AOTCAIfXjiXdQCO9qyKtR9FkhH3SA1S6-CejAe9j5eGVc-qZxM9GPqI7V-VGArGSvjlUmn2FlGyw2GyxY189QGjYcxMT7KaGNInQf8PWbE5aCjZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اکسیوس و‌ سی‌ان‌ان:
یک پهپاد (شاهد) این بالگرد آپاچی رو منهدم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65559" target="_blank">📅 21:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65558">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
منابع خبری آمریکا: احتمال یک درگیری کوتاه نظامی حداکثر ۲۴ ساعته از امشب وجود دارد. آمریکا در آستانه افتتاحیه جام‌جهانی قصدی برای گسترش درگیری ندارد و فقط می‌خواهد پاسخی سریع و قاطع به عملیات دیشب جمهوری اسلامی بدهد
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65558" target="_blank">📅 20:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65557">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
‼️
اکسیوس به نقل از یک مقام آمریکایی: تحقیقات مشخص کرده است یک پهپاد ایرانی به بالگرد ما اصابت کرده و باعث سقوط آن شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65557" target="_blank">📅 20:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65556">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02089086e7.mp4?token=a0i32dyVoZQlk0ebg-3TU-JYehF9Q_umokHfSCCKNC-2cm6yODe5G2ISczGkgl4nNH3-wKbCX3FxJP9b-m5gPdPJy1qgThET8_dfEPwfB71y2hQXc3sR3aCDA9XgmJUKeBKzi_dyGcdml4DxbpRZGaR7_kvSNLYItIdFUXTv1q4Sbvp0Ty6pKwDqw1wxwOfFpDySYRCKkaqJuMZ1OTtsudC8Bph20_POeLkkHnZOb1nbhsyhJlsooBvqucVMBxZ1OmZAqaFUeSp4PZneeTxdyotJgOWsk3lEE7USTus3U-XFGCOIIYjWIFwxbDyo0QeH0QESQVajztRAPRVdwx2HtXmBTiD7TE3M3hW-lpNClHWtHDGgOeOkfahyTU9CaTSdAVelDceanThMRuKP2a7kPOaDfZk-EjdKfTfOXGmWCajcjrM60VG4dPnPhfy4hy_Dyo3tFeC2RO_w081Np1r1Z_KIqzZQHQcXSWLknbQbpMte-FVa9rpDHfEm_bkthXmJkR6Nu4iSD-oC8UbiZNI4PtWRz4VV1NNNA3AOxM77CvwBNo8bUAXbm3N3oopGUQVfuEKuHXwc5tCH3xLJFNFGM63Wtolv0gHz9Pa3o1ARMvTN28jbJOIQ2trm4L0XAa7I_pc275wcP1cPf7a7EP9uzaZI4pILabrwaT7fKfeqx1Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02089086e7.mp4?token=a0i32dyVoZQlk0ebg-3TU-JYehF9Q_umokHfSCCKNC-2cm6yODe5G2ISczGkgl4nNH3-wKbCX3FxJP9b-m5gPdPJy1qgThET8_dfEPwfB71y2hQXc3sR3aCDA9XgmJUKeBKzi_dyGcdml4DxbpRZGaR7_kvSNLYItIdFUXTv1q4Sbvp0Ty6pKwDqw1wxwOfFpDySYRCKkaqJuMZ1OTtsudC8Bph20_POeLkkHnZOb1nbhsyhJlsooBvqucVMBxZ1OmZAqaFUeSp4PZneeTxdyotJgOWsk3lEE7USTus3U-XFGCOIIYjWIFwxbDyo0QeH0QESQVajztRAPRVdwx2HtXmBTiD7TE3M3hW-lpNClHWtHDGgOeOkfahyTU9CaTSdAVelDceanThMRuKP2a7kPOaDfZk-EjdKfTfOXGmWCajcjrM60VG4dPnPhfy4hy_Dyo3tFeC2RO_w081Np1r1Z_KIqzZQHQcXSWLknbQbpMte-FVa9rpDHfEm_bkthXmJkR6Nu4iSD-oC8UbiZNI4PtWRz4VV1NNNA3AOxM77CvwBNo8bUAXbm3N3oopGUQVfuEKuHXwc5tCH3xLJFNFGM63Wtolv0gHz9Pa3o1ARMvTN28jbJOIQ2trm4L0XAa7I_pc275wcP1cPf7a7EP9uzaZI4pILabrwaT7fKfeqx1Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو یک سرباز چینی در حال تمرین برای فرار از حملات پهبادی FPV
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65556" target="_blank">📅 20:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65555">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اگه بت میزنید هم اصولی بزنید!
با این ربات میتونید هروز بین ۱۰ تا ۳۰ میلیون وین بشید با کمترین سرمایه اولیه!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/65555" target="_blank">📅 20:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65554">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
فووووری مهم برای دوستانی که بت میزنن!
یه ربات پیدا کردم که بر پایه هوش مصنوعیه و کامل شانس برد شرط‌بندی هاتونو بهتون میگه! یه هفتست دستمه باهاش ۸۰-۹۰ میلیون روی فوتبال و تنیس وین شدم! هم میشه ازش فرم گرفت هم همچیو با هوش مصنوعی آنالیز کرد تا هیچوقت لوز نشین
😐
•
@Algo_Winbot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/65554" target="_blank">📅 20:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65553">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eP0Wl_7HeclNgSHG7z9zT0NKMIxq5WGI6_kS00c4EqGyrr1g7fvhYcnKA7Kd2f6TuAcd1-EGIftP3v5I_vIfumvVpIE_eb77QMcCCo39cSnb793Co0hWgkXoK-uAZN9uGPRAn1QY0cFmMPBYTrKAME0ikbv7M7NAFGWDK4COuuwqeiWpnS5XpMCmyFcEY37mZrAgvml2CpOywDzMYLNVtTj-fbQcZ8hW5I6c2ciK6KEaGSZwei5c96mkHOQr5yDFJmhixbKJJ0oThbfNCR-wP-unFgvNHkogUcK22xuJXme9w_249XnUrd84CfEWJNwaEzcTbQ9_EuPnRXRQHLnEkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کان نیوز: ۳ میلیارد دلار از دارایی‌های ایران از طریق یک پرواز از ابوظبی به تهران منتقل شده است.
بر اساس این گزارش، این انتقال در چارچوب توافقی انجام شده که هدف آن توقف حملات جمهوری اسلامی علیه اسرائیل و توقف حملات اسرائیل در لبنان عنوان شده است.
کان نیوز مدعی است یک پیام آمریکایی نیز همراه این انتقال ارسال شده که شامل تضمین‌هایی درباره توقف حملات اسرائیل در لبنان بوده است.
به گفته این رسانه، تبادل پیام‌ها با میانجیگری یک هیئت قطری انجام شده و هواپیمای حامل این دارایی‌ها در تهران به زمین نشسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/65553" target="_blank">📅 20:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65552">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf531333f9.mp4?token=jgdd7VpITApw08VWBCo1xhRX6RkVGdIgTdJFM5xehVLSw1cymKt0lhcbGSv-GZ_lfmG4Vl0CmF1l2dBC5xmxnQHd0mwsW_QNNngGA9u6IcSpElO6hbSq9wsEC88eOJUxjYFGCwALDTpS5dc6dbDP8JMim-A9gM8pe-tRY6ySOXv_Hp0qLwHSLRWZE7_vz7ZhgFBoMuK1otaqqWND_rxkqnkAIHnJYjD2AjM5rQqk6mK2MZr34UdnL49_KAyQ472dgMzJNDUAXjYPCMB50RSqkjly_D1RXs9SOYqpt1eB7InuFQuFSCNpHGgvFC8fu6ubKZEX61wKeEVDm3nyJB_eAlGLKZo4CIilpYvR5p9CgFOVWrT3BN5cHh2BIN77SY7eV17DsuE-TbbbYDc_QeWe727517OEoLCFEgUm7svbMCH1DtFqgABZbcXWK4kOsJmG65lTk4_QirP4E-A2ZTtdDwfNcMGA8w2AOjyKKONjAZg5WORG0Ui4SIiCeoW9aFHSo3iqGfW0ufVnKL_8GMYX6kVBvZ_766OP6mTM88FFDJ9NWHenh-g0nxfXp-wXqkiAM1QtAI7NIt1nM7MUxptNVHg8oh45VS1sFXgBjjj37KR27bYr3t_mrMJTNs2nUIOoWZO00Qgtx57R7rHD3BtsSXL0LxjdWW0NKhPJngOIZ2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf531333f9.mp4?token=jgdd7VpITApw08VWBCo1xhRX6RkVGdIgTdJFM5xehVLSw1cymKt0lhcbGSv-GZ_lfmG4Vl0CmF1l2dBC5xmxnQHd0mwsW_QNNngGA9u6IcSpElO6hbSq9wsEC88eOJUxjYFGCwALDTpS5dc6dbDP8JMim-A9gM8pe-tRY6ySOXv_Hp0qLwHSLRWZE7_vz7ZhgFBoMuK1otaqqWND_rxkqnkAIHnJYjD2AjM5rQqk6mK2MZr34UdnL49_KAyQ472dgMzJNDUAXjYPCMB50RSqkjly_D1RXs9SOYqpt1eB7InuFQuFSCNpHGgvFC8fu6ubKZEX61wKeEVDm3nyJB_eAlGLKZo4CIilpYvR5p9CgFOVWrT3BN5cHh2BIN77SY7eV17DsuE-TbbbYDc_QeWe727517OEoLCFEgUm7svbMCH1DtFqgABZbcXWK4kOsJmG65lTk4_QirP4E-A2ZTtdDwfNcMGA8w2AOjyKKONjAZg5WORG0Ui4SIiCeoW9aFHSo3iqGfW0ufVnKL_8GMYX6kVBvZ_766OP6mTM88FFDJ9NWHenh-g0nxfXp-wXqkiAM1QtAI7NIt1nM7MUxptNVHg8oh45VS1sFXgBjjj37KR27bYr3t_mrMJTNs2nUIOoWZO00Qgtx57R7rHD3BtsSXL0LxjdWW0NKhPJngOIZ2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر ارتباطات: سیاست وایت‌ لیست در کشور شدنی نیست؛ به طرفداران آن گفتم ماستتان را بخورید!
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/65552" target="_blank">📅 20:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65551">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65551" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/65551" target="_blank">📅 20:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65550">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbKcRhVb91N7rDaW0s0NYT-ulqX2meXWkowASyPYxanNOK9RJ17zwAobqigkKTGt_Gb5kznhL8_QNXcRPGfr2IMIXtLq5UUDKZjuiotLCzNLg58RbpR02zUuBXmsaK64DbgplFI0q_b6aQictSM2UYVzd4aMIvGuUkxJBNOCN7b2opAxU6OSgXMVssOt9HJ6f4p8B853eoNVyG5XRPPEVxDBdljiiLoeQ7g-2TDqAtLLpzBdORvBKoF8DpPPAq_dwhI96zvhkSeHpw7elwwcS4ycpjVz1DvN8Gjd98O3sAZWPSyVWXi64PB2-wdE9bnoAchFZ2gxGPFIhxmmUCSw2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/65550" target="_blank">📅 20:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65549">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIU1EIfDq76qOM-K3ssMnFPBreD_MGUW8Qu6DsVCwAq_2S_QNtaX2hTxz98VP7tADEkqNiXp2GsejGjB8jIZ2Y63tYRHRSbpr6HwlGRlQRy8Bg_jlM78f8aLR_sCE5yfRM2XEmeDFxHznTO3m6RUkl4bAunIFUIa3XiH6HHRvAjl63-zhJlHubX-lpQMiv38kkmGfSBE66OLXGTBwxb1BaOlhXH6lF6E312w0n1gGJ5fa-fcM01sae5s2H92lpHVUpJvs9UA2-POnMhNCCb50EOdzaov1eKzXC8QQbeDpDNS8f3aHvqsfYUTieyx7eLWGDz48tKDh90nhf_ZbVskFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛
رئیس‌جمهور ترامپ از طریق Truth Social:
من همین الان توسط ارتش بزرگمان مطلع شدم که دیشب ایرانی‌ها یکی از هلیکوپترهای پیشرفته آپاچی ما را هنگام گشت‌زنی بر فراز تنگه هرمز سرنگون کردند. دو خلبان درگیر بودند که هر دو سالم و بدون آسیب هستند. با این حال، ایالات متحده باید به این حمله پاسخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/65549" target="_blank">📅 20:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65547">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxzsUUg6tvCCqI8wGPdtKWzGmIiuDeJtpo_X7N7LcopkmsGOj9EdfyjNV83_6_W7xb9AgHg5RFWsJhcxymHgPCC_t6OIoHUb_ODJfI0jIORFc2_JbX8UrA_-hPPOcgYNcnAJFbAwB00eo1uPsaMzOX1VplVLAX6pqLjVnHDfTUCxHu4PEv774N4VYW7pPcV-KNMie7wxaDBMDCfh3rZC7U4wk9svx60xRDgx39conusjEtEnDJoVCPw-iuPZF2EPMtkmWt1OKAUCBag9lnFtvkpi5gBlCQG3OjYFOGD9_RwXqD5GIk34zagNSrGCHQqjHfxm6LDvARlvBs0Vr-ptKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
جی‌دی ونس معاون رئیس جمهور آمریکا:
جنگ ایران یک سال دیگر به تاریخ خواهد پیوست.
ونس اطمینان دارد جنگ ایران به باتلاق تبدیل نخواهد شد و یک سال دیگر به تاریخ خواهد پیوست.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/65547" target="_blank">📅 20:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65546">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
العربیه:
حزب‌الله اعلام کرد دولت لبنان باید روابط خود با ایران را اصلاح کند.
حزب‌الله همچنین تأکید کرد اتهام‌زنی‌های دولت علیه ایران برخلاف منافع لبنان است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/65546" target="_blank">📅 19:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65545">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2MsZQ1M0sk_eW4tEPuBot9ujijxgtE75VBJMvJolRqJvsNBe1aVYvi2RCq0Zh_HFt7xs3OqUKMfR6etm0UZYFKG1axcMUoBSWdjy2MThEzy872na2i-JaUATdkcrQH3kauWijh_GUxXIvoSQOzAZmzKDKKzTqFmkbh0C2e4RDudFZ8lGYwMwVUu2-r0zB1mb9qM1omodMN5Wg3AAS19Bn8hmfxfW-FDGkkSAdPLkXJ1EImxrtI2ln34APYOTz1Kvhl8cqZ4_brZEjvv4LY91ZsyHoLqRni0qzmeyERGENib3B6QjqCM89zGbKQMNUZ4CxscK5m44HizXtfMp4lgqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پست جدید حساب رسمی کاخ سفید در X
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65545" target="_blank">📅 19:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65543">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUn_i0uOATd9ypK21u3bp3KuDBOZxbjb1kE3ozCK7H8xtLDvQfvc8CQoEM66XX4ObqYzRPWjOpMPIFPVWklvyKd4wYbwSwuqBA88SoPEaG5Yuv1uDWp4brgqRuP2aq93Y71dwat_z2l1f7OylTwx8yoMFctBECco6IBb6yeXH0dFuPqxQYiuw7KRXZfG1LwVuPEPb2QICqHaBXg7xIYBxxwkWiTLuil_jbCNMq0KeZmZNFstIKgZ_xj_OXldnx-jI6vVpPvAmw8-Xa37NIBeHfmejkoBI8NBbPwhMankBhL7DlUo6FQvElh4ywpioU4Dy2h03qQk3sPo8YDivyyQGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807b24fc4d.mp4?token=ecPm9D9rlxkfGi-bi8Toz1pRAWxrr09kjAAZvZPZdsIIEMhIrlQbZ4eGKCXcO5Q2ZY_0G1n5A3PwIAeuh9lTvJ8JouWyKJQ5e9byLDqJHZAbyPSIk07HWr2fzFyuzh37HVwd2KOna1EoV7WNWYzHrAUPVVM5biS5AgnMc6r3DIK-TrNBk7dLMXRbn1iCUYLW8irGHTRumy9VKM3PjEMAEyll-pYBX4bi--bjK-iZy6zLP8D3PbfcMUvJLqsaDt5-BqJaTtnJcp2-YyBvwNwqXm33HyRHIAoMsrhYHgART_-BB32aYTW16padp1U2uMaxLhPYn_mWL-_E19GN5tS6Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807b24fc4d.mp4?token=ecPm9D9rlxkfGi-bi8Toz1pRAWxrr09kjAAZvZPZdsIIEMhIrlQbZ4eGKCXcO5Q2ZY_0G1n5A3PwIAeuh9lTvJ8JouWyKJQ5e9byLDqJHZAbyPSIk07HWr2fzFyuzh37HVwd2KOna1EoV7WNWYzHrAUPVVM5biS5AgnMc6r3DIK-TrNBk7dLMXRbn1iCUYLW8irGHTRumy9VKM3PjEMAEyll-pYBX4bi--bjK-iZy6zLP8D3PbfcMUvJLqsaDt5-BqJaTtnJcp2-YyBvwNwqXm33HyRHIAoMsrhYHgART_-BB32aYTW16padp1U2uMaxLhPYn_mWL-_E19GN5tS6Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نیروهای اسرائیلی در حال انجام عملیات تخریب‌ در بیت لحیا در شمال نوار غزه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65543" target="_blank">📅 19:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65542">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAGsVOU-NAEisjxV0fE81llw66ueGRg7njt6-LjB3DF9v3Fc6xrmrAzaqR2CIkOgdOG7kvjYDh58rXKgQ8RbKRQCEs2lirRTY7dAE9GA67JN7FVUutPZObNgO14mxFdW42ZhpW2_6HQTpcyPb9uTg7rUxYmwcTsDl9fei9HAkcGEiQmH0wk5FUcFCdGqY6BP3QObzphvQy1WTZlu3qqxxiHVCGEJqW0TLOmy7sl2n1kHbf7KMZjKAgDIp0Y6f9ZdAaewiuw7j4YCPkg2qrxEFkhrbJhyoRmgC3iN93P4V_B_Kwwty24Z8blrDd5fEpycDwH2ToiBTgFSdCy6QNjIfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوژه و اخبارِ موثقِ بدون سانسور روز رو از چنل [
اینترنت نیوز
] دنبال کنین
👇🏼
❤️
جهت ورود به بهترین چنل تلگرام کلیک کن
🗿
جهت عضویت در [
اینترنت نیوز هات
] با محتوای علمی آموزشی
💦
این (
مـتن آبـی
) رو فشار دهید.
🔶
اینتر نیوز گاد فادر
🔶</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65542" target="_blank">📅 18:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65540">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpK_3ZIsztJYmUcWtrtM3vefKMXJpl9Wedqn34ad1ywl-ge7Ph_xAXEisNxRaLZoPpewT5dNkFATbyEqMnjxc0gtaVyB5PrHxRA2Ekg2l-2ypJ7mPO4eeRwWp9ltWCu0DCppd3Sa84CvEv5GdFPGlHl5VvkqFQyESQ_AW6K8QX0FtCyMulO_fOnz7HKYLRxCJnS4aYMUIhSa3Q4rSkNvs2q4kToH2-6jqQSyD9xGew_f3lZKNMvfCkSLh191S8jUaHomiPQQBwtnzLvgfO0xggC0MitvGlK4LgBvloJGipUH3Wvlp9_1nuo4VxQIm_EuVGZoCXOzK-dPUKP0jUvDwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f53e9fe1d.mp4?token=G0Lhoi_3fb2J4RfbSgta-6mAtBd8Ffnsu-BT4O1o4TNajh2WDMu1Hz7O8TDVO7OCP3IY3x0lGZOirXAWegzpD37Ew9FciTkeOislFUvL6D49KoubMccDVDkxtO7hgzukccS1plX4fyqcmsu2Va3nB_yb1vLL9Ebx1-MDnng1qzWt6UkoUFG8T0zzTiIb6kbR_ewROQLhTVvU0V0ulwdVvZLyvQwjFImfjpHl2iQZTXONygC5khESZRqd1Q5vXNYfjeJFTrJB3qAqz-5fo82nGJ0CAc4qf7OB0G5CDVd45DiANWDgLjJJ3QroX3kR0on6MDDzrSJ0ePbpz4W0XD0BlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f53e9fe1d.mp4?token=G0Lhoi_3fb2J4RfbSgta-6mAtBd8Ffnsu-BT4O1o4TNajh2WDMu1Hz7O8TDVO7OCP3IY3x0lGZOirXAWegzpD37Ew9FciTkeOislFUvL6D49KoubMccDVDkxtO7hgzukccS1plX4fyqcmsu2Va3nB_yb1vLL9Ebx1-MDnng1qzWt6UkoUFG8T0zzTiIb6kbR_ewROQLhTVvU0V0ulwdVvZLyvQwjFImfjpHl2iQZTXONygC5khESZRqd1Q5vXNYfjeJFTrJB3qAqz-5fo82nGJ0CAc4qf7OB0G5CDVd45DiANWDgLjJJ3QroX3kR0on6MDDzrSJ0ePbpz4W0XD0BlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران شهر صور در جنوب لبنان همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/65540" target="_blank">📅 18:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65539">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_-X7ze34JMTt_dhIX-2V--R-qJcbl5IJJiN0j56Q5kMmHGS5qal7jNol8rQPDQmCfYlTFTUyJELZEgToNHZfPbvaqXI7FiwgJfnAsiLl1-9KLZqMbHcNpxwZQt39vOxsUKSBRAAbkgSS8fuhCvE1HyMnPpuzqh220PPx1mN7NpGg5SBBwPCLmnxWvRFGvGmbEms_72U5Sguz9AWzp6YkbcmgWMPqYZZg91s-wgs15XEewuM_d3C_qzKQ32hEYToMEdaYu3iQki7Xtqv0F8VqOokNQl34P_Qg2zOt8mz9xbcrqf8PPRKxAW0m-fczUFjWAZ4xvgp8Wu4ojyJimYS0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رئیس ستاد کل نیروهای دفاعی اسرائیل، ایال زامیر:
نیروهای دفاعی اسرائیل هوشیاری و آمادگی فوری برای بازگشت به نبرد در ایران را حفظ کرده و همچنان حفظ می‌کنند.
تمام سیستم‌های دفاعی و تهاجمی ما هوشیار و آماده بودند. تهدیداتی که به سمت ما شلیک شد را رهگیری کردیم و به سرعت و با قدرت به ایران حمله کردیم.
حمله‌ای که در ایران انجام دادیم، آمادگی برای ضربه‌ای بسیار بزرگ‌تر و سنگین‌تر بود. ما آماده‌ایم بازگردیم و ضربه‌ای سخت و عمیق‌تر به ایران وارد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/65539" target="_blank">📅 18:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65538">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
شبکه الحدث:
نبیه بری،رئیس پارلمان لبنان به سفیر آمریکا اطلاع داده است که جنبش امل و حزب‌الله آمادگی خود را برای برقراری آتش‌بس فراگیر اعلام کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65538" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65537">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZqR6dQfPpCzA7EWY9EfuoBdUCTdB57yijG3J9eErrEsHn4wg5eVqSi02oOvcp0Tsv94YEuPKlblcXqNbaK4OH3vtfhgYx9ZRcDFddIjtFmlYmrwdXRtf2SQahwlDPjIwwpfL-Ic2olvuUscbLOVNVpbPxwUVpmCmxnUFj1Hmiw2wi_OKIOfCilxXOlwaACb6LIxYG1Z6A-BlQaFCseYbk0-U0aC5_qxVlmCWzHpfJbDXM5ULPV8RKSSOJu-8izCpisWknDJ887-JYTEbzt7q150ytF_x5HrJt6iav8kMeL3w5O0iqBu6QOQR1txrZWdPfSJUOF-JPvSMvI9CrFZYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل در حال شخم زدن شهر صور در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65537" target="_blank">📅 17:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65536">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
♨️
پس از اعتراضات اخیر دانش‌آموزان، تاثیر معدل سال یازدهم در کنکور مثبت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65536" target="_blank">📅 16:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65535">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qodhC2oCGM-qu48igqLzGTzsUuDnXun3LodTalWOXBImxn7cwWQCkudSNpM0FwlEgDw5LYh8Y6HrFkBF74lRaTXI3KIkAY_wnP8gMXtirzLJXJkp2id9OtCTWZ1nLcroNMjnIgduOI2AkSzk5gbWrjLFomxp9JSwsZ1EPE2Js6NvSNEkspzwLZaRsvKV7DOzQp2slvtiVf7w3l0PjVhcY5hYQTQTdCaNIRKWMoV437hsMTZnq0ORwmZeNhehegzN68LznF68OWUhkIFxi9VDklVvX4d2NqdGzoY2tXMBjSMQhCfiAeNORfL_kF8n39_gsrAJPuYIvvBnVK05SPzKIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🐸
خان میرزا بلاگر ایرانی در حمله اسرائیل به عراق کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65535" target="_blank">📅 16:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65534">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/km3egB-XDG_WotW2KUlHjUMDTzJUpn-2dFPNuk7G0IsUwcV15JjsbAGKpErBjadSJ2-Tk-HGIxULnBxbGENjD64etvhJSvspVhTz5HWs3M66q4LKeNRaCsDaNE6ndsKdJqVmWz-jS-Gpl5DnTlKhLK9MySdPnE2YMwsS2xebSWjfJM3-uK35AmyorqFH1EoRL_cva-lIGlP1jWbYakn84AV3bhssWXmk6P4Zrrlg7r_x2_37S37SFtth4hi0w4_CB-qZFBbGB05SipQ7d7X7MTAlTs5fk11ncah7H7BNuOec4_qUfd0_fcuFgarFH8bvwWrCNdnFDvDcprgkMmf8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اکونومیست:
ایران و اسرائیل که برای دهه‌ها درگیر جنگی پنهان با تابوی حملات مستقیم بودند، اکنون آماده‌اند تا با شکستن این مرزها، خطر یک درگیری تمام‌عیار را به جان بخرند؛ وضعیتی که دونالد ترامپ را در برابر یک دوراهی دشوار قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65534" target="_blank">📅 16:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65533">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a4903bc1d.mp4?token=puVefysEQJ5I89rqq0PAsd7P2DQpJNuqFojpSSQTflwBnEKgJn52CLzh7Kn0bZ3Lxvpdx2lAWHnPpgEHhQmN_fau90dZa1wH7j4DaUDeGy10Ohh9uCzLp_inauhqXLxR6qS_y8_yyqs9P86QS7mX4z7SJRkpOReuQRgF0zc_TyslGyTwBLmUjQwTc9wajdi-rl9h_lA3dLLgHaF_KdO1WuWhpSl-40eBQxrwGLKvA31n36HNscwm5SKi3sJHb3FDmNTF6k0f61NnXzkgDDIlesAjObEra2YKo_NTWd6usVDGqxaxf1p25LzHwjXRJCJHgDMFZB80i2e6qSFfzsN0zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a4903bc1d.mp4?token=puVefysEQJ5I89rqq0PAsd7P2DQpJNuqFojpSSQTflwBnEKgJn52CLzh7Kn0bZ3Lxvpdx2lAWHnPpgEHhQmN_fau90dZa1wH7j4DaUDeGy10Ohh9uCzLp_inauhqXLxR6qS_y8_yyqs9P86QS7mX4z7SJRkpOReuQRgF0zc_TyslGyTwBLmUjQwTc9wajdi-rl9h_lA3dLLgHaF_KdO1WuWhpSl-40eBQxrwGLKvA31n36HNscwm5SKi3sJHb3FDmNTF6k0f61NnXzkgDDIlesAjObEra2YKo_NTWd6usVDGqxaxf1p25LzHwjXRJCJHgDMFZB80i2e6qSFfzsN0zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
❌
گلایه یک زن حامی رژیم (پرستو) از رفتار بسیجی ها بعد از آتش بس
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65533" target="_blank">📅 16:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65532">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
نیروهای رضوان حزب الله اعلام کردند بصورت زمینی وارد شهرک های اسرائیلی شدند
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65532" target="_blank">📅 15:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65531">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
شبکه ۱۳ اسرائیل:
شورای وزارتی کوچیک تصمیم گرفته هر حمله حزب‌الله به اسرائیل را با حمله به بیروت جواب دهد
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65531" target="_blank">📅 15:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65529">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AIJ6_oyA7WZBoRp7X3BIEnGAUjZ-NiG_0NsCnhpStYypKo2bUD91ovQU-D6yYFS9U7RqTSr9xBsV6IyFlp2k_vrlsjB5q3u6lnxEKvI39s7arHyBI2fNYY_jJORU8UqMv3ULg4qSfH3DlbK3Wt3FeZfndx6mLaxulIvsQn9siNJDYA5j1T8KJvFkHpzrDXaByxzIN6q_Jio2rhsYh8VYin9KlV4adpretkhMqjiVCYRp_1NIxH2g1oqWvy-QSiwQYdy-I-GUXdO6BC3HqG5J4R3ELKIfknAJAZGN5OEJI57-pBTBHQbFbvxA0XqONhK5wwYobQ87tDb_W29N99ulWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jVGXhtTbeTuOLNPc85I8nNRVkO3De1OOLsNSK94rBKFpm3UmPUHdt2sffWT_nG7PD0m4UaqBDZMNQ0tF6wgZw7JUih3zC2ojwbf7QnisLFLu5d-lnwn7rNoJujanukTzbtYX2uTqujcLox9dmYn_meq8iJw1zKIJKzlpsUuZfALkYj31rNv77JjyoFTHA8PL6q7CcI0Ar9w6CCv2OR3th0opbtswCQ34nw_AB5nkSctEmhm_FaTOLz-xZhPVhBk0qHlfsOLxh0n3YNLW5uXLvMF3Q25umfdRLJGFmAPLaAVN72lmDuRcvvEBziFdsKThnuKhG0YJeNzpYbnH2TeRbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
حمله هوایی به شهر کوثریه الرز جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65529" target="_blank">📅 15:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65528">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
ستاد فرماندهی مرکزی ایالات متحده:
دو خدمه بالگرد آپاچی ارتش آمریکا که در ساعت ۳:۰۳دقیقه بامداد ۱۹خرداد به وقت ایران در نزدیکی سواحل عمان هنگام گشت زنی دچار حادثه شد و سقوط کرد توسط نیروهای آمریکایی نجات یافتند.
همچنین علت این حادثه در دست بررسی است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65528" target="_blank">📅 14:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65527">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad4b9120bb.mp4?token=BlQIFUTEwcRRUuylM8wkdZ_E4MfumxqelBDgM6ek9nU2ZZJ5j89hkPR6HDD0P8-cJRhKQIJkjXuWLUOxvxwYtSjI84Mcir-MNqnGJpizwklIVVK7I0tPRU6o0hDk7s2F3Rpw_jZXCAyZIX3xmhjzIN0t1-1VeSYOErDSrwKNbI088tOK17uHFRMI0fsS5ktKYxLKdVDw9x04vl7x9mAhaK6pH8847O79yGcOgoGfZc_vCgKRux69mUwp6tCye6CxCvokKn66NM7kmD3Go2wM7tQuiI1BxQv0iAM1y4qkAk_hf96gACrXRGFQGZotAbjkL-eNzWfoLpKKC9oTKE86uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad4b9120bb.mp4?token=BlQIFUTEwcRRUuylM8wkdZ_E4MfumxqelBDgM6ek9nU2ZZJ5j89hkPR6HDD0P8-cJRhKQIJkjXuWLUOxvxwYtSjI84Mcir-MNqnGJpizwklIVVK7I0tPRU6o0hDk7s2F3Rpw_jZXCAyZIX3xmhjzIN0t1-1VeSYOErDSrwKNbI088tOK17uHFRMI0fsS5ktKYxLKdVDw9x04vl7x9mAhaK6pH8847O79yGcOgoGfZc_vCgKRux69mUwp6tCye6CxCvokKn66NM7kmD3Go2wM7tQuiI1BxQv0iAM1y4qkAk_hf96gACrXRGFQGZotAbjkL-eNzWfoLpKKC9oTKE86uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید از ساشا سبحانی حرومزاده و آقازاده‌ جنجالی حکومت درحال عشق و حال با پول مردم در خارج
تو این ویدیو به دوست دخترش یک ساعت طلای اودمار پیگه به ارزش چند ده‌ هزار دلار هدیه میده
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/65527" target="_blank">📅 14:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65526">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
حمله اسرائیل به شهر ساحلی صور در جنوب لبنان  @News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65526" target="_blank">📅 14:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65525">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
فاطمه مهاجرانی، سخنگوی دولت: میزان قطعی‌ برق در روزهای گرم پیش‌رو به میزان همراهی مردم عزیز بستگی داره.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65525" target="_blank">📅 14:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65524">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0689b8dc9.mp4?token=dPD6d-7YGYj9qW7XV3T53L6WaApeGpknP7kSSqj2UdKhZi64UKX8hWajuMcaNZRW1ekQ7RKP3rl8hdVUOwbJDug0xzpuo8MMZK7ZKzLeD96OmJ9Coi1pWtuyo7SrOYyKEQUeXt_F1q6sydJKfCgiJwNznlFmY9dPSvIAPhwq02kWv7BfgnjhMne_6Kl5SZ43soleAr63aUqR_1OmFRLxPAVPECi-BOS6SmJmQX0qJBMmSCmJ4YC_fQLluQxaT1voCWxqnV7MxmILfu2OQrtnmKjq7cYLKq1TJ1QE637geziKg2nTX1APlUa7aWin1wBtN1qvsul_-RavlwiSAdgqHgqSiMsJyA6lxzYQ_V767oOyPXOR2AiFUlwuLiZaL85oWCF6emBWKWOY1EwWM4jCqR0xYyzSdOyKH-R2oqTVL0hlkaX5EO-KjsXyl3R0ANFh9lI6Gs32FFLSXaKDWogdLOuvnmDt0OldMElKyyjOeoUMfWdnGKVGAw2xoSP8iSA5INLrHFi6IfrJUrYGuhWkLKasjZefljqiu8JY2WbrSu86MUnFlLGbOBFFRcBmF-PmkUkSEMia57E-Cn-yX1DWRYnhvDrEEf_yl-DRdyB6IdI45_vehweI-g8Dx8mz7m06f4vnC4orr6Yc7e_7wfiMuxeWFWZyWTZld3WYX8no5Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0689b8dc9.mp4?token=dPD6d-7YGYj9qW7XV3T53L6WaApeGpknP7kSSqj2UdKhZi64UKX8hWajuMcaNZRW1ekQ7RKP3rl8hdVUOwbJDug0xzpuo8MMZK7ZKzLeD96OmJ9Coi1pWtuyo7SrOYyKEQUeXt_F1q6sydJKfCgiJwNznlFmY9dPSvIAPhwq02kWv7BfgnjhMne_6Kl5SZ43soleAr63aUqR_1OmFRLxPAVPECi-BOS6SmJmQX0qJBMmSCmJ4YC_fQLluQxaT1voCWxqnV7MxmILfu2OQrtnmKjq7cYLKq1TJ1QE637geziKg2nTX1APlUa7aWin1wBtN1qvsul_-RavlwiSAdgqHgqSiMsJyA6lxzYQ_V767oOyPXOR2AiFUlwuLiZaL85oWCF6emBWKWOY1EwWM4jCqR0xYyzSdOyKH-R2oqTVL0hlkaX5EO-KjsXyl3R0ANFh9lI6Gs32FFLSXaKDWogdLOuvnmDt0OldMElKyyjOeoUMfWdnGKVGAw2xoSP8iSA5INLrHFi6IfrJUrYGuhWkLKasjZefljqiu8JY2WbrSu86MUnFlLGbOBFFRcBmF-PmkUkSEMia57E-Cn-yX1DWRYnhvDrEEf_yl-DRdyB6IdI45_vehweI-g8Dx8mz7m06f4vnC4orr6Yc7e_7wfiMuxeWFWZyWTZld3WYX8no5Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حمله اسرائیل به شهر ساحلی صور در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65524" target="_blank">📅 13:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65523">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
‼️
مصطفی پور دهقان نماینده مجلس:
وزیر ارتباطات دستور داده یوتیوب بزودی رفع فیلتر بشه.
«در صورت رفع فیلتر شدن به دلیل تحریم بودن ایران درآمد یوتیوبر های ایرانی قطع خواهد شد»
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/65523" target="_blank">📅 13:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65522">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c1be7dc2.mp4?token=jj-F33ptHFfDc4AoeFghnqUa_HDzO6S1ihRjXis_HRXjduZrVyx9XpDS_B3p_UJtpI9U-msp_7K7tCEAgBAEOHrFUA6hy5fLJfInejkwC8T9h1nCyep6swFHAH4sekDEwEabhFKP78OpC6vVshYQM0INatsiRyjIqjp__Qz9s4F41RnDFmI_Gixuziq8eI8asbu11AyeAQUzukiK_ocsYoWcDqNav1Fk0cdsujHvuHdE9foXub1jQfVCUgmfE2hDBjioT8iRDNqYjWm4vuv5ohDwWuw6wLTRssFrqMdNx_Zxv0JblwHG5jJi-p8l3tXXikliH1ZJib-Hwi6HLpkxnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c1be7dc2.mp4?token=jj-F33ptHFfDc4AoeFghnqUa_HDzO6S1ihRjXis_HRXjduZrVyx9XpDS_B3p_UJtpI9U-msp_7K7tCEAgBAEOHrFUA6hy5fLJfInejkwC8T9h1nCyep6swFHAH4sekDEwEabhFKP78OpC6vVshYQM0INatsiRyjIqjp__Qz9s4F41RnDFmI_Gixuziq8eI8asbu11AyeAQUzukiK_ocsYoWcDqNav1Fk0cdsujHvuHdE9foXub1jQfVCUgmfE2hDBjioT8iRDNqYjWm4vuv5ohDwWuw6wLTRssFrqMdNx_Zxv0JblwHG5jJi-p8l3tXXikliH1ZJib-Hwi6HLpkxnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایشون با کفن رفته تو زاینده رود و از پزشکیان میخواد وارد دولتش کنه تا مشکلات کشور رو حل کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65522" target="_blank">📅 13:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65521">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63397f42b5.mp4?token=omIokWzhZM7AKTtCcq96vjrcGx2zIxDdQi4el_gajan9BJv7QRwb-4RJhAfjwaUh9_2oFIzYTHyuAIWo-8W4wmh4o2mUZ_Q2_wFo4Q7iF6nvLRMtOY4BPcoyiwcs1ogndImGFG5t1DUPDjkMyN8gMruoxGBvVw0oz5_diITimThIa7jHA4ykIiDEECoZOkgyPxFKjLTTtovNpnhj2WvwVIIzxwrVqrxdqIqsE0BRu7S-Fz6i76BFxpSZx0Xmq51A7cglVhjNBvAHkEamkrXHJeXxB-2pngQSaGEAL986VKu6Jt0WfcKPQYIINE4dE1q4g8XFC119ugkcLz4rtYamdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63397f42b5.mp4?token=omIokWzhZM7AKTtCcq96vjrcGx2zIxDdQi4el_gajan9BJv7QRwb-4RJhAfjwaUh9_2oFIzYTHyuAIWo-8W4wmh4o2mUZ_Q2_wFo4Q7iF6nvLRMtOY4BPcoyiwcs1ogndImGFG5t1DUPDjkMyN8gMruoxGBvVw0oz5_diITimThIa7jHA4ykIiDEECoZOkgyPxFKjLTTtovNpnhj2WvwVIIzxwrVqrxdqIqsE0BRu7S-Fz6i76BFxpSZx0Xmq51A7cglVhjNBvAHkEamkrXHJeXxB-2pngQSaGEAL986VKu6Jt0WfcKPQYIINE4dE1q4g8XFC119ugkcLz4rtYamdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آذری‌جهرمی وزیر ارتباطات دولت روحانی و از بنیانگذاران فیلترینگ در ایران: اقدام به قطع اینترنت و فیلتر کردن جوابگو نیست
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65521" target="_blank">📅 12:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65520">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65520" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65520" target="_blank">📅 12:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65519">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oC3_qyb_3ZmRAgffRX6NhlWm-SxL7aXo4hHopHZqi3e5Z1scBh09uroaFeya8YABWfNENtBAHvnR1LGBuyU133I_FPA-KPNh2sdtY37yHFErf28lgGXiBzXA28xXKSLCpm_fnlb8W_DvUKZkimj1Xd7MGBcuOsekYM-9ZCAifeTNlNsdviRD_aQrGMsuId2uMnGu7xikdTF_OJkfygCpp24y4L-twxBPYRZG1z9jKL2QpwhsVz3-olPfLlPQbVyayjcKwKxytCBMh-YqsI7AXnYztFEa4ddPKQmYzBg5mZcDH5_AM5boQ-spcdFfHMmqcmJ8Ate_M8eTEqjylh9fPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/65519" target="_blank">📅 12:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65518">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd926c0a3.mp4?token=lzlgN7Sg0oPRkWqczOLjvmAcmQnwQzLqtTGr2Yb-cigcWCyUofwNyScfCRGzKPAqzujHYEBamF__e-SXV5VgN90wl44y-d0pFa9v1aQseFEEN7XYQWkQp7BDxZ22YD83U9wMVFfS4_upFh9JgHDULxCbrEbeML-PvaKBST2cf-R-Z82FOWiMRCOuwToqKrdIXtuS6QBnKpDltg_U0bptv8CWJk1SItwIkvQYzkX-8kgP3KC5__wtX-vAMVJBnGYZlAX49LM22109Q21vNx1VmmAFjV9nkNxy09-FbYsPTxCidhiy6eUHRt5yOVvqjPFpjM0OxoOCdfqkJ3kMem3mng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd926c0a3.mp4?token=lzlgN7Sg0oPRkWqczOLjvmAcmQnwQzLqtTGr2Yb-cigcWCyUofwNyScfCRGzKPAqzujHYEBamF__e-SXV5VgN90wl44y-d0pFa9v1aQseFEEN7XYQWkQp7BDxZ22YD83U9wMVFfS4_upFh9JgHDULxCbrEbeML-PvaKBST2cf-R-Z82FOWiMRCOuwToqKrdIXtuS6QBnKpDltg_U0bptv8CWJk1SItwIkvQYzkX-8kgP3KC5__wtX-vAMVJBnGYZlAX49LM22109Q21vNx1VmmAFjV9nkNxy09-FbYsPTxCidhiy6eUHRt5yOVvqjPFpjM0OxoOCdfqkJ3kMem3mng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
مقاومت فوق‌العاده یه برج ۳۶ طبقه فیلیپینی در مواجهه با زلزله دیروز ۸ ریشتری در این کشور
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65518" target="_blank">📅 12:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65517">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گزارش باحال حمید معصومی‌نژاد تو ایتالیا از آخرین روز مدرسه تو این کشور که دانش‌آموزا اینجوری همو با آرد و‌ تخم مرغ و ... به کثافت کشیدن و جشن گرفتن
😂
اینجا هم بچه‌های بیچاره هرروز بخاطر تاثیر معدل کنکور تجمع میکنن که به هیچ‌جای هیچ مسئولی نیست
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65517" target="_blank">📅 12:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65516">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPKrVN8v4G-hwWU45Xh9mw72PRzpiAwJ9Sl1LJ9ijZusfVcREA0h1QnEhIlhvq-VQXDlPbzfygMIWOFi84ZzKHhR7-W3KGsI-LuMoS_z3ThUj4JSh_tMlNNs9fVmEBO5cryWCDAUC3YWTI7tfha-kg8Ieik6w-6GR7nC6oZdz1vW3o9qpO4GGYA3pWcDd64ixTa6eVHmA3mizkxPi7pZe1XN6Ot2J_sIV97xAwI0unFO2ZRXVQsGYsJDTVu7PRFXoZa5ZM6_hEB54CxhDHVw5IXIZE8reWAUJTpu1MUkr06yhlSnXGRnIGEnzHqB1b7_ERQbdBEhU47L2Pc5BzbluA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤡
سفارت جمهوری اسلامی در بیروت بجای مردم ایران اومده گفته که لبنان قلب ایرانه و خب گوه خورده
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65516" target="_blank">📅 11:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65515">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🇮🇷
ستاد دفن و خاکسپاری علی‌خامنه‌ای اعلام کرد که مراسم خاکسپاری رهبر دوم ترور شده حکومت حداقل تا بعد از دهه اول محرم برگزار نخواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65515" target="_blank">📅 11:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65514">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
جی دی ونس معاون ترامپ:
مواردی وجود داره که منافع اسرائیل و ایالات متحده متفاوته.
هدف اصلی ایالات متحده در مورد ایران اینه که اطمینان حاصل کنه تهران سلاح هسته‌ای نداره.
ما می‌تونیم به توافق هسته‌ای بلندمدتی با ایران دست یابیم. ممکنه اسرائیل این موضوع را نپسنده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65514" target="_blank">📅 11:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65513">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد ایران:
اگر حالا ما برویم و بمباران کنیم «که اگر بخواهیم می‌توانیم خیلی راحت این کار را انجام دهیم» و دو سه هفته دیگر آنهارا بمباران کنیم، آنها دیگر هیچ چیزی نخواهند داشت.
اما شما تنگه را برای ماه‌ها «باز» نخواهید دید. اگر ما بمباران کنیم، می‌دانید، افراد زیادی کشته خواهند شد. چه کسی می‌خواهد این کار را انجام دهد؟ من نمی‌خواهم.
ما یک سند امضا شده خواهیم داشت که در واقع از انجام بمباران قوی‌تر است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65513" target="_blank">📅 10:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65512">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
خبرنگار: آیا از نتانیاهو خواستید که حمله را تلافی نکند؟
ترامپ: نه، من گفتم کاری را که درست است انجام بده، اما می‌خواهم هر چه سریع‌تر متوقف بشی چون آنها باید متوقف شوند.
این مربوط به لبنان بود و باید متوقف شود. ما می‌خواهیم کار تمام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65512" target="_blank">📅 10:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65511">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
ترامپ درباره نتانیاهو:
به نتانیاهو حمله شد و او هم متقابلاً پاسخ داد و من نمی‌توانم او را به خاطر این موضوع سرزنش کنم، آنها را هدف قرار دادند. آنهاهم متقابلاً پاسخ دادن و حالا درگیری را تمام کرده‌اند.
بنابراین، آنها قرار است فقط برای یک هفته دیگر یا چیزی حدود آن، یکدیگر را به حال خود رها کنند.
این وضعیت خاورمیانه مدت زیادی است که ادامه دارد. اگر واقعاً بخواهید بگویید حدود ۳۰۰۰ سال اما مطمئناً ۴۷ سال است که اینگونه ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/65511" target="_blank">📅 10:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65510">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
ترامپ درباره ایران:
ما اکنون در حال مذاکره هستیم و آنها می خواهند معامله بسیار خوبی انجام دهند. آنها حاضرند همه چیز را به ما بدهند. آنها حاضرند به ما "هیچ سلاح هسته ای" بدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65510" target="_blank">📅 10:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65509">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‼️
🇺🇸
🚨
🚨
ترامپ اعلام کرد در دو هفته آینده "پیروزی کامل" را بر ایران اعلام خواهد کرد!
ترامپ: من فکر می‌کنم که ما در آن نبرد پیروز می‌شویم، اما شما واقعاً در دو هفته آینده که پیروزی کامل را اعلام می‌کنیم، پیروز خواهید شد.
این یک پیروزی کامل خواهد بود. خیلی زود این اتفاق می افتد و قیمت نفت پایین می آید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65509" target="_blank">📅 10:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65508">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
🚨
🚨
ترامپ درباره ایران: ما هر چیزی را که برای تخریب وجود داشت، نابود کردیم!
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65508" target="_blank">📅 09:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65507">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8bb28ac6.mp4?token=pCHuzv3jUebFxQGv1zO0NI-3g_-YX4slbS2xtCPwg_bir1N9fZd1Xk_m_d-KI5sLs1xlLvuOEJpcujS5JuyaAf2c3xnMyn4liNFMqFX9mYehGDIY7WRDRcV66FQa9L-04Qvm8Xg2EAGSs6_74Cx5_o2V-WS9ZwNvXGohlqokd6Gg6WDvRoE6PBYdQa7wYgoEcYMEvY-G8JITvmPGGnmKP6s-dyR9qYV4GHY231mef2Lcc7uzo9SOyDtXeOjO5AgJ6x2ygeHkZ9RNWBIbYpcBG_9ceNOLqG-rbenF4HwNJlgip52SAnyj9PvJ3dUnLudM8Yz_naUgqHLiFa7D8K-Y1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8bb28ac6.mp4?token=pCHuzv3jUebFxQGv1zO0NI-3g_-YX4slbS2xtCPwg_bir1N9fZd1Xk_m_d-KI5sLs1xlLvuOEJpcujS5JuyaAf2c3xnMyn4liNFMqFX9mYehGDIY7WRDRcV66FQa9L-04Qvm8Xg2EAGSs6_74Cx5_o2V-WS9ZwNvXGohlqokd6Gg6WDvRoE6PBYdQa7wYgoEcYMEvY-G8JITvmPGGnmKP6s-dyR9qYV4GHY231mef2Lcc7uzo9SOyDtXeOjO5AgJ6x2ygeHkZ9RNWBIbYpcBG_9ceNOLqG-rbenF4HwNJlgip52SAnyj9PvJ3dUnLudM8Yz_naUgqHLiFa7D8K-Y1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
چندین حمله اسرائیلی در جنوب لبنان، در مناطق اطراف صور گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65507" target="_blank">📅 09:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65506">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
🚨
🚨
مقام ایرانی به الجزیره:
واشنگتن در پیش نویس یادداشت تفاهم تغییر ایجاد کرد و این موضوع غیرقابل قبول است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/65506" target="_blank">📅 09:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65505">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
طبق گزارش
نیویورک تایمز
، یک بالگرد آپاچی ارتش آمریکا در نزدیکی تنگه هرمز سقوط کرد اما هر دو خدمه آن به سلامت به محل امن منتقل شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/65505" target="_blank">📅 09:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65504">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6179637bd4.mp4?token=Dh9Jgr6nWXYs8RIMLihccW50PFuAV2EWDijCglUZLyE40lmHW2wmOXA8CfDLuJVSp8acztOREr62LMgn8Hg20_ty_zrIrvm8OwWcAnTeZHGnfRGe1mRDw2-gZFbOgh4JN-IVnFzDm6mbEJ5w3Txv4TYRPxvl5AxsfKWHL5sTU31nutGyUcP-YCby_WtDoEmZRn4G7jfO7Z2UFNkv4tyZAYJWqVXmn1LC-XXBzYa0W2zL5IHPN6PvIQBrvMRH3qNY3I8-qeNn0rzj8hMKbhq_-l-oio0pyuTjh4VWBuGcbwj8yMUutSZpH0rUyXZjAcvP5xexYKmxDigP8SkAfppr1jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6179637bd4.mp4?token=Dh9Jgr6nWXYs8RIMLihccW50PFuAV2EWDijCglUZLyE40lmHW2wmOXA8CfDLuJVSp8acztOREr62LMgn8Hg20_ty_zrIrvm8OwWcAnTeZHGnfRGe1mRDw2-gZFbOgh4JN-IVnFzDm6mbEJ5w3Txv4TYRPxvl5AxsfKWHL5sTU31nutGyUcP-YCby_WtDoEmZRn4G7jfO7Z2UFNkv4tyZAYJWqVXmn1LC-XXBzYa0W2zL5IHPN6PvIQBrvMRH3qNY3I8-qeNn0rzj8hMKbhq_-l-oio0pyuTjh4VWBuGcbwj8yMUutSZpH0rUyXZjAcvP5xexYKmxDigP8SkAfppr1jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
یک کارشناس حکومتی در صداوسیمای جمهوری اسلامی: آمریکا در جنگ ۴۰ روزه بیش از ۷ تا ۸ هزار زخمی و دست‌کم هزار کشته داشته! کشته گرفتن از آمریکایی‌ها و اسرائیلی‌ها برای جمهوری اسلامی کار سختی نیست و ما به درخواست کشورهای منطقه خویشتنداری کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65504" target="_blank">📅 09:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65503">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65503" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65503" target="_blank">📅 00:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65502">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C67siXKAII_X79IwH4ChmQ7qeeOSlErdryCn1IQo8C3sdKfw8Yz-rSiyANJfDV12UfvBI0SYZfzv-BWmAwtmXdnXPCeYGQHNi27Y-7TUmrPtnfF3kYZdfwyqgNVqHHVe4X9u_hd3VJIgeHqtCC7w2bzKvVaPy4HqlEtwwovrbUHHNxkadhbjy14G6-7_e7OI7evffz74Fibb9Ux7HCRo_xY7DhIgO73H92Du9XiEvUBe_gzm6bqQCc3j1VWpvuY_d4FbU4lXjEWiL87cTNAqOMA-2EZQXAPV2C3cTknBYaRWCVGU0qse-dYolcn19XJfsPejIImIN317a2vt8eOi6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65502" target="_blank">📅 00:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65501">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSapNJuKCHA9Qqp-8NGaxHRr4xUjTASZ_UswsjyKKFGrm-4W57ozSS6RZHuTOiso11Gecv2mqqXytVzrFI_S2krKK3joJdnpL8MLq4-gs2UPUim0IaGmPM6FytT1vUVpmgKIEmRIXLNn1sQ1xJwMsuFEwIc0aVX2dC87V-fMJ4WlzL3ef2-1kRe4pAjdIJJ7HIbYHXmcJ-LN3iWZ6A2UMh-qn87dpVa8DySF2NjhYEBF-aZkytRsH2MzKK6yUGoH3g7uibJzhMUSLguClK-fkjfS6gQiD4rmYPc8vZwVfbup5Z92BUoIv4TIHwJw7j3v45sumSJXL7g1X6X_Osdc6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
اونایی که
۵ ماه
پیش وارد شدن الان
۲.۵ برابر پولشون سود
دریافت کردن
دو فرصت
ویژه
در
سرآوا
برای شما فراهم شده که با بازدهی فوق‌العاده می‌تونه مسیر جدیدی به سوی
ثروت
براتون باز کنه
✅
اگه توام‌ دنبال یه‌راه میگردی تا بتونی درامد خودتو داشته باشی به خانواده سرآوا ملحق شو:
@Sarava_Finance</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/65501" target="_blank">📅 00:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65498">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
مهدی خراتیان تحلیلگر اصولگرا: در ۱۸ و ۱۹ دی ۱۰۰ شهر یا سقوط کردند یا در آستانه سقوط بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65498" target="_blank">📅 00:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65497">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
♨️
🚀
خبرگزاری فارس: انصارالله یمن با پهپاد به سرزمین‌های اسرائیل حمله کرده
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/65497" target="_blank">📅 00:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65496">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🇺🇸
ترامپ به اکسیوس: ایران می‌خواهد به توافق برسد و این اتفاق می‌تواند به زودی رخ دهد
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/65496" target="_blank">📅 23:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65495">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7093313be4.mp4?token=uB3i9Wm4_mcYQsYjuCs_86ncNlvP5f4uY5yPp0g9Jar1Nc6MU4B_qMnMJbxIrwwDeO_MiYp38HMK7_ZFF3K9TmD8biWdh-7Mn5ALPORxTucllAwcb1DO3opVEWi1Mwrltn47aHrMHeiBz4xNJ6ksJ_2nPC84G0YdCszqBmRa5vPmX5pw6BWlzztBH9en6Cqu8RydEQ28pt945AuTTVjPrIAEXwiHu_RNPlIZYZp1AUb8wq9FQ0zKenHSTR3QNPhGXWfm2SjL4A8Qd3Btb7dUFWczmfVb1WuGqKW0rtCnzhuFSQ9r12XGbDuQrXZIRHAW2s35R_OE5xhxcq5VRjMRhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7093313be4.mp4?token=uB3i9Wm4_mcYQsYjuCs_86ncNlvP5f4uY5yPp0g9Jar1Nc6MU4B_qMnMJbxIrwwDeO_MiYp38HMK7_ZFF3K9TmD8biWdh-7Mn5ALPORxTucllAwcb1DO3opVEWi1Mwrltn47aHrMHeiBz4xNJ6ksJ_2nPC84G0YdCszqBmRa5vPmX5pw6BWlzztBH9en6Cqu8RydEQ28pt945AuTTVjPrIAEXwiHu_RNPlIZYZp1AUb8wq9FQ0zKenHSTR3QNPhGXWfm2SjL4A8Qd3Btb7dUFWczmfVb1WuGqKW0rtCnzhuFSQ9r12XGbDuQrXZIRHAW2s35R_OE5xhxcq5VRjMRhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
سپاه پاسداران حملات موشکی و پهپادی به پایگاه‌های آمریکایی و گروه‌ های کرد در نزدیکی سوران، استان اربیل، کردستان عراق انجام داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/65495" target="_blank">📅 23:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65494">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2a7fe1ed4.mp4?token=KSzFk0XUl9mlmxM8QLoKo-4ukygPN0ZhphKt-S2663pPaSDvoFBPnoHGSU6PRfuNeE5kIpa29o8j7eJbib09YGZGnEu66prfShGrgJQXsd35m_1Jmrl7HuvhICxiuVCsGCShWS_j5QQDoies90Pbl3pL01eHdqZGS5vobSEAw7x8bc8aUNpqAMyGruX6mt5nHgFNITn6dqfwpioLK8awUoAwVttItw5JOlqiRBZH2Vtke_ZVhMIivQruRFgPL4xrGf_7wODILjkwy_3MYhKbU-pV3qH9owbIZhw2I9ByI13wx1eXks7cQYAjZ3vTswmP_scBpgdsYSKgDUy9naIC1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2a7fe1ed4.mp4?token=KSzFk0XUl9mlmxM8QLoKo-4ukygPN0ZhphKt-S2663pPaSDvoFBPnoHGSU6PRfuNeE5kIpa29o8j7eJbib09YGZGnEu66prfShGrgJQXsd35m_1Jmrl7HuvhICxiuVCsGCShWS_j5QQDoies90Pbl3pL01eHdqZGS5vobSEAw7x8bc8aUNpqAMyGruX6mt5nHgFNITn6dqfwpioLK8awUoAwVttItw5JOlqiRBZH2Vtke_ZVhMIivQruRFgPL4xrGf_7wODILjkwy_3MYhKbU-pV3qH9owbIZhw2I9ByI13wx1eXks7cQYAjZ3vTswmP_scBpgdsYSKgDUy9naIC1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
رژیم جمهوری اسلامی با موشک به کردستان عراق حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/65494" target="_blank">📅 23:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65493">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
رئیس جمهور لبنان:
اگر حزب الله از تحویل سلاح خودداری کند، مردم از آن روی برمی گردانند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/65493" target="_blank">📅 22:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65492">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
قالیباف:
هدف مذاکرات پایان جنگ و ایجاد امنیت پایدار است، نه عادی‌سازی روابط با آمریکا. ما نمی‌خواهیم از طریق تسلیم یا شعار پیشرفت کنیم؛ بلکه باید به دنبال پیروزی مهندسی‌شده با قدرت و عقلانیت ایرانی باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/65492" target="_blank">📅 22:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65491">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
نتانیاهو به وزرای دولت خود:
ممکن است به چند دور (جنگ) دیگر با ایران بازگردیم، این پایان کار نیست
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/65491" target="_blank">📅 22:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65490">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roDPrjN1EV4srKUtI_hYjvsQsgdCzgdF6JOY0mBePU1HASIyTKsbvD0HssZvxrjzyCX86ir_HTJPUmt6E6c-ZtJEurcoNpb2t6gwqHQYTEKHDsaKmtmmZm22eN9i-IKswFTJRON4AQMq4kjUe7n8wOk9nOQxLOGJRw1Jbo7CaYdimE7SpLThY_Xc66LZKUyAbwfJwCEazgpkDV4Nk0YLsAhKjjp9L55IKOQGVm-baNMOcg2UwNd2c6OaMxrHHGDtRZLoR_FQrFVxA1roNn9Swc1Rea4HKVhYIUjWyXOrhO5c1GcgGuOhDpYt2g5lolr-fe2CKL9OjJ5H6aPCxR0gnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرژانتین
🇦🇷
-
🇮🇸
ایسلند
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
بامداد چهارشنبه ساعت ۰۴:۳۰
🏟
ورزشگاه جردن-هیر
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
آرژانتین در
۱۰
دیدار اخیر خود،
هشت
برد و
یک
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
ایسلند در
۱۰
دیدار اخیر خود،
دو
برد و
سه
تساوی کسب کرده و در
پنج
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر آرژانتین
۲
.
۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر ایسلند
۳
.
۵
گل در هر بازی بوده است.
🧠
وقتی نتیجه از تصمیم مهم‌تر شد، تفریح تمام شده است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65490" target="_blank">📅 22:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65489">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovpeotfkfADAszgludvGofr3_i8LauBnAdIn-t1HcGe1j_Nu_KaDeNpcnWfD5O7e9kbyQX0OMeF4cvPPy5tFBb9lNJm4tV4-YBH5fa4sSKRoeIhY95P88-Pu8y5Xzhwtinxxs28054Ub7YVqb2yUClo0RRSA9_PVj1EIN5uPghcQANOJ27O2Pc4klpXCv_6TpvLQRB3HX_JZZKakPd-xIzucQhCWMMUWltF8Ze3TlB6Dv5mRK8Hgmvu1kcUJJEYBBypvHvQwyvDa81XsSsD5dVNFqeTgSAQebN9tczEWESKEsLwvSqo1zQm28WE4VF0KhIqps--oZzalc-ttjcXOQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
صابرین نیوز با انتشار ویدیویی از شاهنشاه آریامهر محمدرضا پهلوی سعی در مشروعیت بخشیدن به موضوع کمک به لبنان دارد
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/65489" target="_blank">📅 21:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65488">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
مردم ایران بهتر از هر کسی می‌دونن که تا وقتی جمهوری اسلامی سر کاره، نه ایران روی آرامش می‌بینه و نه منطقه. صلح، امنیت و پیشرفت واقعی فقط زمانی به دست میاد که این حکومت دیگه بر سر کار نباشه.
راه‌حل، مذاکره با سپاه و مسئولان جمهوری اسلامی نیست، راه‌حل اینه که دنیا کنار مردم ایران بایسته و از تلاششون برای رسیدن به آزادی و پایان دادن به جمهوری اسلامی حمایت کنه
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65488" target="_blank">📅 21:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65487">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی :
این حکومت سال‌هاست مردم ایران رو گروگان خودش کرده و از جون و مالشون برای پیش بردن جنگ، ترور و بی‌ثباتی تو منطقه استفاده می‌کنه. توی این درگیری هم مثل همیشه، هر آسیبی که به زیرساخت‌های ایران یا مردم بی‌گناه وارد بشه، مسئولیتش با جمهوری اسلامیه. این رژیمه که کشور رو به این شرایط کشونده و هزینه تصمیماتش رو مردم عادی میدن
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65487" target="_blank">📅 21:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65486">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی :
جمهوری اسلامی باز هم برای حمایت از حزب‌الله ، کشور رو وارد یه درگیری نظامی دیگه کرده و بار دیگه نشون داده که منافع مردم ایران براش هیچ اهمیتی نداره
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/65486" target="_blank">📅 21:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65485">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
ترامپ به کانال ۱۲ اسرائیل:
به نتانیاهو گفتم اگر جنگی تمام‌عیار علیه ایران آغاز کند، او را تنها خواهم گذاشت!
من دیشب از نتانیاهو خواستم که به حملات ایران پاسخ ندهد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65485" target="_blank">📅 21:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65484">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
ترامپ :
اسرائیلی‌ها وقتی جنگنده‌هاشون تو مسیر ایران بودن، به ما خبر دادن.من هم سریع وارد عمل شدم و تلاش کردم ابعاد حمله محدودتر بشه!
همچنین پنج کشور منطقه با من تماس گرفتن و خواستن روی نتانیاهو فشار بیارم که حمله نکنه من هم با نتانیاهو صحبت کردم و اون در نهایت موافقت کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/65484" target="_blank">📅 21:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65483">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
سازمان هواپیمایی کشور: حوزه هوایی کشور به وضعیت عادی خود بازگشته است و عملیات پروازی طبق اطلاعیه‌های پروازی صادر شده (NOTAM) از سر گرفته خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65483" target="_blank">📅 20:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65482">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/103c84b28e.mp4?token=gKgjpNRjyLseh7PYQuzNYCKXm4cdgkeduurnGBqSlMpLtMbTEyhc8EXg1yVkVEZRqZqwLsw7AWmUpAaQm7IgTRcNjJTSQhmd7ydeYy7WaJQF_ULsgXX4BWi_w7e_SMOaVDIuuOan5pGMCL0vdTxzUakKwq9vMLCo-wezxEFckMiIEzFmzyIulogKx6D72yfT8VistEvQ5PhXByMskd4kiXL_0fua4P-PDPbBzeuybMsVoq-Am_TPovPbB2_m41NJmw20jZgJ9hTCysQRKSvGG1GAQY4XYng4Fn7KWKC_j6blhJI-Xndhc4ypfQpkooshocK_wiKHskgHPav3ELKGiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/103c84b28e.mp4?token=gKgjpNRjyLseh7PYQuzNYCKXm4cdgkeduurnGBqSlMpLtMbTEyhc8EXg1yVkVEZRqZqwLsw7AWmUpAaQm7IgTRcNjJTSQhmd7ydeYy7WaJQF_ULsgXX4BWi_w7e_SMOaVDIuuOan5pGMCL0vdTxzUakKwq9vMLCo-wezxEFckMiIEzFmzyIulogKx6D72yfT8VistEvQ5PhXByMskd4kiXL_0fua4P-PDPbBzeuybMsVoq-Am_TPovPbB2_m41NJmw20jZgJ9hTCysQRKSvGG1GAQY4XYng4Fn7KWKC_j6blhJI-Xndhc4ypfQpkooshocK_wiKHskgHPav3ELKGiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فیلمی از کشتی M/T Marivex که امروز صبح گرفته شده، پس از آنکه توسط نیروهای آمریکایی به دلیل ادعای تلاش برای شکستن محاصره دریایی ایالات متحده علیه ایران، از کار افتاده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/65482" target="_blank">📅 20:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65481">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdH_h7DC-9E3NHFkeIHSsVe7dGjf6tn3cstl9QLH4-IfCGcxkIlKc5MXA_S1-lZhDmUmkSvoh-OpFcfXG49_FjGNNjzPu7ZzE2nZBTQBBMeQrEaPe8qn38ZfOhoKU8KRulsU2JbKl-qhizl_rsly5xlrhX8auJH8dt0J-7BmI0mnUW_kfYuFW93MO7E7OHWWdEiUsWr-IqngA_6TsMcCNGA89-uzxjAMI3FTC1MAaVstAe2Ds5Od9v8_Xs86YQlChcKC00MmzHF-6riv3na_-hP5UOfUoiLprkZI3J5-juSj3iUJu7tDbLJCLlRZj-kjVD8PP05kTbb6T0BxUllzQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
نیروهای ایالات متحده یک نفتکش بدون بار را در خلیج عمان، در 8 ژوئن، پس از اینکه کشتی با تلاش برای حرکت به سمت یک بندر ایرانی، تحریم‌های جاری علیه ایران را نقض کرد، از کار انداختند.
فرماندهی مرکزی ایالات متحده (CENTCOM) کشتی M/T Marivex با پرچو پالائو را زمانی که در حال عبور از آب‌های بین‌المللی در خلیج عمان به سمت ایران بود، از کار انداخت.
یک جنگنده F/A-18 سوپر هورنت از ناو هواپیمابر USS Abraham Lincoln (CVN 72) پس از اینکه خدمه از دستورات نیروهای ایالات متحده اطاعت نکردند، یک مهمات دقیق را به بخش‌های مهندسی و فرماندهی کشتی شلیک کرد.
ماری‌وکس دیگر به سمت ایران حرکت نمی‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/65481" target="_blank">📅 20:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65480">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/65480" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65480" target="_blank">📅 20:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65479">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7OKFdx84wNp8B9nwPZCOMIKwBO-PTKMmuVPL2FGUHu3xuTyNcvWTqcwOYRn2tS6jLuOGUPcKpva0YawlCdsQq5frq7_64tm_JDmGfIAxAkv4S_BApMjhfC05a6L9C-CUfJv1e4mNFUg9ff57HCqkhkct-_XuF8HcrcR5V5f_qmf_mKwBaystUTpvQ30U0sa0o_UNC_f081IG7vY8UDyXEeYZPdfv3fHAmCi_DMh2tPzb-woEKF1ccX18_1xtJ-H0y7TxoVGcjtojMfE10-aEAVqgiauDNfrVIBgY-ZAWvO9fZ35aPAy4Nvv7o0UQb_eLowyTk2rybQ0vNh7Ln4qeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌇
بونوس‌های شبانه از 1xBet
🌒
هر چهارشنبه و پنج‌شنبه از ساعت ۶ عصر تا ۱۱:۵۹ شب، برای واریزهای 5.50€+، 50 اسپین رایگان در بازی
👑
Crown Coins
👑
اهدا میشه!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/65479" target="_blank">📅 20:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65477">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
رادیو ارتش اسرائیل: ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند.
«این حمله گسترده انجام نشد.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/65477" target="_blank">📅 20:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65476">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
فیلد مارشال ، محسن رضایی:
ایران از غنی‌سازی کوتاه نمیاد و در موضوع آزاد کردن پول‌های بلوکه‌شده جدیه. اگه مذاکره نتیجه نده، محاصره دریایی رو تحمل نمیکنیم و اقدام نظامی انجام میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65476" target="_blank">📅 19:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65475">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
ارتش اسرائیل تعدادی از فرماندهان ارشد حماس را ترور کرد
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/65475" target="_blank">📅 19:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65474">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
نتانیاهو:ایران فکر می‌کرد می‌تواند به خاک ما حمله کند و ما واکنش نشان ندهیم، این اتفاق نه رخ داده نه رخ خواهد داد، دست کم تا زمانی که من مسئول باشم
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/65474" target="_blank">📅 19:15 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
