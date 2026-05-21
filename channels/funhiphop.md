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
<img src="https://cdn4.telesco.pe/file/sXLZOdC1sNLnBR_lL_MLHgn1dUpBEAqkzN77Y9uYEA1EtegLQ7iijhLRgjZftVLRTwcjsrOX4tjVO959EQfaiWUtXLOvCTL2ZNLQYncm9zFYYmxdfECGzQHJvpk-cX5AW7ywRJaHw83VQTnD1gq0XgRvZJoPZ3HYFOzUOt6Sa0VAJwvJ1pFL1y3e9NE5aq_j9VV7vDBdgYIMRbNb1pWMir9nGqSOoD9S-1--k2lb233iea4so2uuEZrtB08vBZTOf-UnVxXiF29GVfsaQxkMxcbKtg40Vi0Rmta4__Fq8fIFeLXoghsBwwoGua-4Yt4VLr4KdQeTeF397qnW-Y6ohg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 164K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 20:07:52</div>
<hr>

<div class="tg-post" id="msg-75495">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">😠
کله زرد بنگاهی
ما نمیخوایم تنگه هرمز عوارضی بشه
کنترل تنگه هرمز (محاصره) کامل در اختیار داریم
نود و هشت درصد توان موشکی ایران و از بین بردیم
ایران نمیتونه اورانیوم غنای بالا رو نگه داره و اگه بهش دست پیدا کنیم احتمالا همشو نابود میکنیم و ما این اورانیومارو نمیخوایم
درگیری با ایران به زوری به پایان خواهد رسید
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 351 · <a href="https://t.me/funhiphop/75495" target="_blank">📅 20:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75494">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDKfK22qFYw7yts04fcWPniSwTe31LTWScadDgDHj2zaahi13oxm8-IWrjWqZ_awXgk16SKpaThoSH-LP8beyix3y_2k5SEA31NhhJ_YbJli2pfiVk3IYCd9naRmUWUUIBsc3jfeNadONvItPrHrz5S0SJBFfdCWcYY5s_T9-x0k7MEDipf8jewIHK1YHHUENRPK-VPQ3qCMwjGM6WThfOWTEuqBSXl9T-pAIZxqD6Uvnwwi51BPpowEEUIjtrsIq2fgsjyLj5B0Jqcn40T6dnmw5QgyD7qNw9zuNHpUNBCU-TiOlvJ-Ytr59cVjR8ogj_0rAzO5YHOYZ__YuXSsNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔜
فایننشال جوس
مارکو روبیو، وزیر خارجه آمریکا، گفته اگر در تنگه هرمز سیستم دریافت عوارض برای عبور کشتی‌ها اجرا شود، رسیدن به توافق دیپلماتیک
تقریباً
غیرممکن خواهد شد.
😶‍🌫️
این حرف بعد از خبری مطرح شد که گفته بود
ایران و عمان
درباره
دائمی
شدن
عوارض
عبور از
تنگه
هرمز
در حال
مذاکره
هستند.
👻
یعنی آمریکا این اقدام را
تنش‌زا
می‌داند و معتقد است می‌تواند مذاکرات سیاسی و توافقات منطقه‌ای را سخت‌تر کند.
👍
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/funhiphop/75494" target="_blank">📅 19:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75493">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">امشب النصر قهرمان میشه؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/funhiphop/75493" target="_blank">📅 18:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75492">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دلم میسوزه برات ناموسا، کاش میشد یکم عقل تو کلت کاشت.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/funhiphop/75492" target="_blank">📅 18:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75491">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjQhZRdYnDw-iTwg6aSRu-mqQ9DwZONUTRJmAX26CS_TNdzfzY_NeR70YVLhV24V4tmCS_igS_5BsjutS6a5IrUl8deMmfdRT2fOsVXa_eDwEkOPVrS-oEnnOspfIvaKD1JHoInXRLyFoa1cxjSc4Kcytp9Yqm8QHh_t3Y8eUKXsZaPmNr9M-d7-zVUWOYYKsWgT6-h4RvOwVQBaiiwix5AWX05Nqbya5hj9tdemolF9OuWesv80kANIb4pfJXI7uYr5xWMg3iSN_D3QK2bsbipCFcDuYQ0FKL7KStBrzXGwocubJsDZE02BOfwpH84kh9xRfRxWZDVMzvHl9Vkz-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلم میسوزه برات ناموسا، کاش میشد یکم عقل تو کلت کاشت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/funhiphop/75491" target="_blank">📅 18:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75490">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">📶
بهترین ارائه دهنده فیلترشکن
🤝
آیپی static (ثابت) ، مناسب ترید و وبگردی (اینستاگرام - یوتیوب و....)
🔥
| بالاترین سرعت ممکن روی تمامی اپراتور ها
✅
تعرفه سرویس ها زمان دار :
🥑
1 گیگ | 4  روزه ⇐ 290 تومان
😼
3 گیگ | 9 روزه ⇐ 850 تومان
🛍
5 گیگ | 14 روزه…</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/funhiphop/75490" target="_blank">📅 17:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75488">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فاکس نیوز
طبق نظر سنجی 60 درصد آمریکایی ها با اقدام نظامی علیه تهران مخالف هستند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/funhiphop/75488" target="_blank">📅 17:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75486">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tvLfik2Peeo-clqEBVguUV8lxkylZW3v1Hn-8qBvk3ET732H4VWqUF4zk8rE8ZlBDOUaNYCGfH2eHn43n31EY59VGelqEpcpk02KlV_EaCrTnDUSC3FLyxFuT5xfMkWrnJQpZ42IZJr4DqLPfJcrK58fu-GGTjp85qE-rSK3urap1meAdc-g6PARJE5POi4IHLmQA61MhaBEyKF6JurCU5s2vezdF5yglcso8Y7XJppaOOjWQn8-VzkIbVQDwpUVmhErw79IH2IH_By7QcF4vPjwmcTlvit2s3qdf_kPg4pD0s40_nxW4GObHOiR2Zo4a9a9OhtnzCkyRoHb1KKUnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e5fHo3LWlBe1gvJXekONsGu3WRkHmQBimxjh0PZFEfcNAuPLP8c8XBnXGyf7MLo2p-WNip6i1CqzGElSBU2czAvu-OtQXDaKgnxEP9dvFiNKSrc1Ct9zNAZil5rkPoOhfgLHabosASsghx18PMRS2wjrb4N2M1PioMMbAiJIGbxfgZ_86LEYL7ueIHCaBsIcp2qCppH0_9NXbJ8BVKxzDPRElbpH8BP7SJwuqYTxmZDiQtRtVzTEJdl7JvMbNqYP75taFzFChYrZJQKr-W4aeedwMB3C2kw_dvpIN7DxyuhGKQSgNp5aXyNkAwYBObIcE_asbmqd3e5oNsi9wG4eRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همون همیشگی دوستان اشتباه شد دارن میزنن هنوز  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/funhiphop/75486" target="_blank">📅 16:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75485">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">هیچوقت نفهمیدم چرا رپرا وقتی تو ایران میمونن کم کم بنجل و گنده گوز میشن
وقتی از ایران میرن کم کم دچار زوال عقل و بحران هویت میشن
چرا بالانسو رعایت نمیکنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/funhiphop/75485" target="_blank">📅 16:21 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75484">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ:
ما داریم با آدمای خوبی در ایران مذاکره میکنیم/مذاکرات داره خوب پیش میره/اونا با عقل شدن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/funhiphop/75484" target="_blank">📅 15:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75483">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حالا ترامپ کصکش باز میاد میگه مذاکرات مثبت بوده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/funhiphop/75483" target="_blank">📅 14:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75482">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رویترز:
مجتبی خامنه ای دستور داده که اورانیوم غنی شده در ایران بماند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/funhiphop/75482" target="_blank">📅 14:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75481">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">به پیر به پیغمبر من خشخاش نکاشتم، دست از سرم بردارید
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/funhiphop/75481" target="_blank">📅 12:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75480">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJDX0JqzQlyifJHclVV7g4W0ZoGc0N8P3X1g5CKPVcCeo9Uc8ApSpGMeciY_d8HQ16XaZnwLMp5EyELYRS4v8JgBQH92moKlyRE2-aSbEh4vcx-ZiURK9QshK9mTVldDla5u7lPB9Y_AniMt1tuUAB2siP61s_77VlEZHxM3AXnAujrpbNuCJM6d1U82sY7uB9eRnN_J9xfPj-jM3Z1MeqrzswzhLHiSVa9F7mHi1iUB1psJ2MkQ7DbJjfk40eAv5SQ1a0qVmy8D02TP4-2r-1KRURXOYDNdSk3BHsZgi6XHUpnGMZ7448RG6puzuz4hetOwIIS0W1oxCJ3l8Wq1Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید سردار آزمون
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/funhiphop/75480" target="_blank">📅 12:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75479">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ویناک رپر سیاسی شد رفت
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/funhiphop/75479" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75478">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حواستون به قحطی نون هست که خیلی چراغ خاموش داره میره تو کونمون؟</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/funhiphop/75478" target="_blank">📅 11:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75477">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">واقعا چطوری ملت میتونن طرفدار پهلوی باشن من  الان داشتم با بابا بزرگم حرف میزدم میگفت اونزمان ملت حتی نمیتونستن یه جومونگ ساده ببینن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/funhiphop/75477" target="_blank">📅 10:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75476">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec7c8d7ea8.mp4?token=ktU5PsbvYfMMGS9e-RcKKEgRn8ShIYXg9Fy8-pMAMmUM6mLr8mEbWcHluEm14VCzDUqMzUR-lHkELx00BhYbMeBltmOJ2Li7m0zZ4HBQe0iNMnuRLE0jvufk4wHbdFvYy_9y0xKw0k53GVHdrAdqTBIU9ECuOczJ51qrmCl5HLhfrAjDq1cZzKgvOgREDJiJ8lADhp66LASINcVSuMdm1xhuYFjntWGVR3JN6oAi4E353nz66Ut42tZ472MdGIsswzttx1j-JY38o6D_qUx7MSS7zZsphbep6YrDhcqCosel5gy3MDUfwPmxOYfT8z3X_ITRGcMGqNUA-G-tZOqN3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec7c8d7ea8.mp4?token=ktU5PsbvYfMMGS9e-RcKKEgRn8ShIYXg9Fy8-pMAMmUM6mLr8mEbWcHluEm14VCzDUqMzUR-lHkELx00BhYbMeBltmOJ2Li7m0zZ4HBQe0iNMnuRLE0jvufk4wHbdFvYy_9y0xKw0k53GVHdrAdqTBIU9ECuOczJ51qrmCl5HLhfrAjDq1cZzKgvOgREDJiJ8lADhp66LASINcVSuMdm1xhuYFjntWGVR3JN6oAi4E353nz66Ut42tZ472MdGIsswzttx1j-JY38o6D_qUx7MSS7zZsphbep6YrDhcqCosel5gy3MDUfwPmxOYfT8z3X_ITRGcMGqNUA-G-tZOqN3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحاتی مختصر درباره برنامه هایی که رو گوشیتون نصب میکنید
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/funhiphop/75476" target="_blank">📅 09:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75475">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">از اتفاقا دی حدود ۱۳۰ روز گذشته و تو این مدت بیشتر از ۹۰ روزش رو انتظار کشیدیم
ایوب هم بود روانی میشد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/funhiphop/75475" target="_blank">📅 09:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75473">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">😑
رویترز
کشتی‌های متحدان ایران مانند
روسیه
و
چین
اولویت عبور از تنگه هرمز را دارند.
😅
برخی کشتی‌ها برای عبور امن بالای ۱۵۰ هزار دلار
هزینه امنیتی
می‌پردازند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/funhiphop/75473" target="_blank">📅 00:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75470">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">معاون فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی:
دست ما روی ماشه است و
اگر ترامپ فکر می‌کند می‌تواند تنگه هرمز را با زور و کشتی‌ها باز کند، باید بداند همان نیروی دریایی که ادعا کردید نابود شده، شما را در کف دریا غرق خواهد کرد.
دشمنان ما باید بدانند که کاملاً اشتباه می‌کنند اگر فکر کنند این ملت با تخریب زیرساخت‌هایش عقب‌نشینی خواهد کرد، این ملت در طول ۴۷ سال ثابت کرده است که ممکن است تخریب شود اما تسلیم نمی‌شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/75470" target="_blank">📅 23:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75469">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بچه ها اگه کانفیگ میخوایید تهیه کنید میتونید از ایشون تهیه کنید، ۲۰ روزی هست باهاشون کار میکنیم کارشون درسته
قیمت: گیگی ۱۹۹
@TornadoAdmin
| خرید
@Tornado_Ping
| فروشگاه</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/funhiphop/75469" target="_blank">📅 23:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75468">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">با اینکه نداریم سیم‌کارت سفید میشناسنمون تو ایست بازرسی</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/funhiphop/75468" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75467">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خبرنگار :
پیامت به خانواده‌های آمریکایی که از هوش مصنوعی می‌ترسن چیه اونا نگرانن بچه‌هاشون تو آینده کار نداشته باشن
ترامپ :
هوش مصنوعی فوق‌العاده‌ست ایران نباید سلاح هسته‌ای داشته باشه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/funhiphop/75467" target="_blank">📅 23:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75466">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مایکل بی، کارگردان آمریکایی، درحال ساخت فیلمی بر اساس مأموریت نجات دو خلبان آمریکایی پس از سقوط جنگنده‌ی ارتش آمریکا درجریان جنگ با ایرانه؛ تمرکز این فیلم برروی عملیات گسترده‌ای که تو پشت خطوط دشمن در کوه‌های زاگرس در غرب ایران صورت گرفت، خواهد بود و بر اساس کتابی آینده از میچل زاکوف ساخته می‌شه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/funhiphop/75466" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75465">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2221a06fe7.mp4?token=Ld9i1-l7zzY-fXaYLUPM2ZXywbmxO9TUpyNAhkrqB6TJ1FcX3Bjf0vlH0NVAgP4Iz1sl9CmRmn45TWyJvDgwwYxMeKiTTQ1edMO3Q0YS-SA0MhJZu3RaGEVeIpp5YAey0IzH-ocDbL_Io8sERPWZItaHa6M655rlkokyy_ZvdGPmsgIS6tREkW2_j3TX051_bAUAAYgXeHD6fvqAUy8zwOoNc0h4GJmSOgibmb_z4THMgsu_Re3ppKsF0WUMhijPpb5HSS9lAvYb3c0MtKNMF1BVPsGDCxGnuDgdlr6KnqC4BfRF9Sz_yd3Ui9vzzij9J2rYcvrDPRL5tjGapof1mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2221a06fe7.mp4?token=Ld9i1-l7zzY-fXaYLUPM2ZXywbmxO9TUpyNAhkrqB6TJ1FcX3Bjf0vlH0NVAgP4Iz1sl9CmRmn45TWyJvDgwwYxMeKiTTQ1edMO3Q0YS-SA0MhJZu3RaGEVeIpp5YAey0IzH-ocDbL_Io8sERPWZItaHa6M655rlkokyy_ZvdGPmsgIS6tREkW2_j3TX051_bAUAAYgXeHD6fvqAUy8zwOoNc0h4GJmSOgibmb_z4THMgsu_Re3ppKsF0WUMhijPpb5HSS9lAvYb3c0MtKNMF1BVPsGDCxGnuDgdlr6KnqC4BfRF9Sz_yd3Ui9vzzij9J2rYcvrDPRL5tjGapof1mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
اگر پاسخ‌های درست را دریافت نکنیم، اوضاع خیلی سریع پیش می‌رود. همه ما آماده‌ایم. باید پاسخ‌های درست را بگیریم.
باید پاسخ‌های ایران کاملاً ۱۰۰٪ درست باشند، و اگر اینطور شود، زمان، انرژی و جان‌های زیادی را نجات می‌دهیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/funhiphop/75465" target="_blank">📅 22:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75464">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ace87a5520.mp4?token=nsGDBx2ci2oEniiCq3j-ZJQnR6byeiQESaIxDVKwC8NwA3LnZ3mSQuumtGb5EOfK5mriOSnGnpEKb1IOiaQ1eSDohkLfC3t4dVhzz0XqrJM_1ndwhj2skZRv-kWSJq_N6uoo-j_rS4046r4i4uc48-DcivGe_YxLch5kVo559MzfQ-37I6jPGiVRNU-gw6KT93XumGFWdfXw78yNkA9LhRZQhg5MHei_nTAs7rPuRSHCi8jPbwPSRnCVgI4QoLjwzs5XsC5LEcBF0lx13oafL4AuhUG-icUJ5wFgSbSj0ljJdJL3Om7SCiAFRMMOLcohK09FYRiEVyRyZtqa36tvAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ace87a5520.mp4?token=nsGDBx2ci2oEniiCq3j-ZJQnR6byeiQESaIxDVKwC8NwA3LnZ3mSQuumtGb5EOfK5mriOSnGnpEKb1IOiaQ1eSDohkLfC3t4dVhzz0XqrJM_1ndwhj2skZRv-kWSJq_N6uoo-j_rS4046r4i4uc48-DcivGe_YxLch5kVo559MzfQ-37I6jPGiVRNU-gw6KT93XumGFWdfXw78yNkA9LhRZQhg5MHei_nTAs7rPuRSHCi8jPbwPSRnCVgI4QoLjwzs5XsC5LEcBF0lx13oafL4AuhUG-icUJ5wFgSbSj0ljJdJL3Om7SCiAFRMMOLcohK09FYRiEVyRyZtqa36tvAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
آیا آمریکا در جریان مذاکرات صلح، لغو تحریم‌های نفتی علیه ایران را پیشنهاد داده است، همانطور که رسانه‌های دولتی ایران گزارش داده‌اند؟
ترامپ:
نه، من چنین چیزی نشنیده‌ام. تا زمانی که آنها توافقنامه‌ای امضا نکنند، هیچ لغو تحریمی انجام نمی‌دهم.
وقتی آنها توافقنامه را امضا کنند، می‌توانیم آنجا را دوباره بسازیم و چیزی داشته باشیم که واقعاً برای مردم آن کشور خوب باشد.
اما نه، ما هیچ پیشنهادی نداده‌ایم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/funhiphop/75464" target="_blank">📅 22:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75463">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ درباره ایران: ما در واقع با برخی افراد بسیار خوبی درحال معامله هستیم. ما با افرادی با استعداد و با هوش خوب معامله می‌کنیم. ما از هوش آنها کاملاً تحت تأثیر قرار گرفته‌ایم.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/funhiphop/75463" target="_blank">📅 22:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75462">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb46c8698f.mp4?token=p2f9rj1A9dOAn3Z4pzHmeyEuIcbwO3V0cEhJQWYOW6zThGblL3eq3ZQkCNMUagYHDT1Y_J_74RjKfUvCam3zsuitIIatpcRdmP8eH2QgOsPQcPVixbzQU3yWm-YwGKBbQ_WjR9Zk0f8MBaMBABVrMHGR9COkfZuIjCaXb0yBLl-eSSkSHPkODUWRwxpMikb_3eFh3lS0uHk54QCqExYQz6IUy9VRr2hhgb_tgglMCpRJBTiz6b4PmZevm6245Y9Oj4bKny0WrcNzzvVrhTA2jk-tICnNu7T0XD6rXISeZAj67fazy0TgVNT867X_aqtPvKERVrm7L-rTEgPyYItEYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb46c8698f.mp4?token=p2f9rj1A9dOAn3Z4pzHmeyEuIcbwO3V0cEhJQWYOW6zThGblL3eq3ZQkCNMUagYHDT1Y_J_74RjKfUvCam3zsuitIIatpcRdmP8eH2QgOsPQcPVixbzQU3yWm-YwGKBbQ_WjR9Zk0f8MBaMBABVrMHGR9COkfZuIjCaXb0yBLl-eSSkSHPkODUWRwxpMikb_3eFh3lS0uHk54QCqExYQz6IUy9VRr2hhgb_tgglMCpRJBTiz6b4PmZevm6245Y9Oj4bKny0WrcNzzvVrhTA2jk-tICnNu7T0XD6rXISeZAj67fazy0TgVNT867X_aqtPvKERVrm7L-rTEgPyYItEYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ما در واقع با برخی افراد بسیار خوبی درحال معامله هستیم.
ما با افرادی با استعداد و با هوش خوب معامله می‌کنیم.
ما از هوش آنها کاملاً تحت تأثیر قرار گرفته‌ایم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/funhiphop/75462" target="_blank">📅 22:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75461">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwHnxAjFLI5jZ7xxG0R2eWF4B-__HTIyflW1eQOiOqGIBUI_m9fTWe9EwqRPblcl_9WUv3ynH6aWEbwTg_1NSE0-wxzyYLytM72tcI9kvSRxNweiyZaa-jjyYc4wBQDSnAxbqITplQsOxxojJdjWsepwH8Xwo011c5i1YjibVu7H18iK5z37vV6QFsn5qaPMJkEPu9suCQaPa6ZfjDbrciI3XQvljkku7zGh5t0xde6CA5XaVYhaAtQRmxKuHauE4mxZrMrV8oDo0VyMipeZwldcvKWYIgCJiDgnpDFUA0hjQAZMb3Fhd-YbSoJhuIQ4q35cAqNe6hXH2Fu6BWjUng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من الان که فهمیدم که لارنس نورمن در واکنش به حضور مقامات پاکستانی در ایران برای پیشبرد مذاکرات گفته این جالب و قابل توجه عه و اتفاقات جالبی درحال رخ دادنه تا ته ماجرا رو رفتم جدی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/funhiphop/75461" target="_blank">📅 22:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75460">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rj6tdUMq7F2wlWGGQAn8LiW837TuMmiEBdLomw8I9YjltBj58FlbbVFF6ew-6zKlKd8Zo512htUc45M3N6k9Mo_pNdsy-yGabtPnbKvVVffpKo0odBkwgNvj--pf8tTpoPo32jqQEen1GJvOeDONwIhPGOpOia3eN7jGzd9RyjOrVjzuTuLf9BVKBUyjTktwlB6f_CK2i_2gdoOyK0U_H2SOFWe0c4O6iony8WYlIHCiC0p3SP1aIG0dw5Ex2t49Dg98Q3ZbokpHkF70FY5WqHN88yPxnAKzmS8S_B0XKAKyaTr1IqzwLCKULeRC1U6C_3mnKfqihnqXAxmndksj7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت بزشکیان:
ایران همواره به تعهدات خود عمل کرده و تمام راه‌ها را برای جلوگیری از جنگ پیموده است؛ و همچنان همه گزینه‌ها از جانب ما باز است.
مجبور کردن ایران به تسلیم اجباری چیزی جز توهم نیست. احترام متقابل در دیپلماسی عاقلانه‌تر، امن‌تر و پایدارتر از جنگ است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/funhiphop/75460" target="_blank">📅 21:51 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75459">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">العربیه بمب دراپ کرد:  کار برای نهایی‌سازی متن توافق بین واشنگتن و تهران در حال انجام است. فرمانده ارتش پاکستان ممکن است فردا برای اعلام نسخه نهایی توافق از ایران دیدار کند. ممکن است طی ساعات آینده از نهایی شدن نسخه نهایی توافق بین آمریکا و ایران خبر داده…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/funhiphop/75459" target="_blank">📅 21:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75458">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تیراندازی افراد مسلح به سمت یه خودروی پلیس تو یکی از جاده‌های شهرستان سراوان، منجر به کشته شدن ستوان سوم امیر‌حسین شهرکی شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/funhiphop/75458" target="_blank">📅 21:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75457">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">آکسیوس:
دونالد ترامپ و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، دیروز تماس تلفنی طولانی و به گفته‌ها «سخت» داشتند که در آن دو رهبر درباره نحوه پیش‌روی با ایران اختلاف نظر داشتند.
ترامپ به نتانیاهو اطلاع داد که میانجی‌ها در حال کار روی «نامه‌ای از قصد» هستند که هر دو طرف آمریکا و ایران آن را امضا کنند، که رسماً جنگ را پایان می‌دهد و دوره مذاکره ۳۰ روزه‌ای را درباره برنامه هسته‌ای ایران و بازگشایی تنگه هرمز آغاز می‌کند.
یک منبع نتانیاهو را پس از تماس « با موهای آتش گرفته» توصیف کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/funhiphop/75457" target="_blank">📅 21:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75455">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کانال ۱۵ اسرائیل به نقل از منابع:
پیشرفت‌هایی در پیش‌نویس یادداشت تفاهم و اصول بین ایران و ایالات متحده وجود دارد، اگرچه شکاف‌هایی باقی مانده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/funhiphop/75455" target="_blank">📅 20:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75454">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سازمان رادیو و تلویزیون اسرائیل به نقل از یک مقام ارشد:
مسئله زدن یا نزدن نیستا.
مسئله اینه کِی بزنیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/funhiphop/75454" target="_blank">📅 20:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75453">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کاش هند همین امشب به پاکستان حمله کنه و خوارشونو بگاد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/funhiphop/75453" target="_blank">📅 20:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75452">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تو آپدیت جدید اینستاگرام هم دیس لایک برا کامنتا اضافه شده هم میتونید عکس کامنت کنید.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/funhiphop/75452" target="_blank">📅 20:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75451">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">امشب میزنن.</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/funhiphop/75451" target="_blank">📅 19:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75450">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ: آمریکا در مراحل نهایی مذاکرات با ایران است. باید ببینیم چه اتفاقی می‌افتد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/funhiphop/75450" target="_blank">📅 19:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75449">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">این چند وقته هر VPN گرفتی یا کند بوده یا هی قطع شده، ولی این یکی واقعا خوب جواب میده
💎
هم سرعتش خوبه هم پایداره
✅
لینک ساب برای دیدن حجم مصرفی   هرشب سه گیگ قرعه کشی داریم چنل داشته باش.   @mortalvpn_bot</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/funhiphop/75449" target="_blank">📅 19:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75448">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvABvriz-9z3CgzRD_1iarEJVGbMv18pynegmVUGHeUr55y0gJnfddoDIaSgjMK_CJuGf9T0MMry8tu0leZoJzciwkX7mQtwu9gBNdSBupa9ocAKL_vYn8XYLKtJPvBn3N2EG5PSg5CXeu_NaGBRLlREk4ppXVtXGe5TJyURQyT6MNkFbUGOFNyoV1-iE7nxQ8vPG7Awy5xBtn1PUh7QkAH94SXiATlHNCSUvJW1FyQ4HRwO1bBvC2SzxMng0Iz-CcKeGWdkKsmawxjjGyFiQayMrZI-ixuxVwdZ9L5tFP5oYA7EHUNpkNxhlxgjez3ysjgkFDVGa4L7Fqg6BbAkBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چند وقته هر VPN گرفتی یا کند بوده یا هی قطع شده، ولی این یکی واقعا خوب جواب میده
💎
هم سرعتش خوبه هم پایداره
✅
لینک ساب برای دیدن حجم مصرفی
هرشب سه گیگ قرعه کشی داریم چنل داشته باش.
@mortalvpn_bot</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/funhiphop/75448" target="_blank">📅 19:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75447">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ:
آمریکا در مراحل نهایی مذاکرات با ایران است.
باید ببینیم چه اتفاقی می‌افتد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/funhiphop/75447" target="_blank">📅 18:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75446">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سخنگوی وزارت امور خارجه:
ما نمی‌توانیم به ایالات متحده و اسرائیل اجازه عبور از هرمز را بدهیم، زیرا این امر بر امنیت ملی ما تأثیر خواهد گذاشت.
وقتی ما خواستار آزادی همه‌ی دارایی‌های مسدود شده خود هستیم، منظورمان دسترسی به آنها به عنوان حق ماست.
استفاده صلح‌آمیز از انرژی هسته‌ای و اجازه‌ی غنی‌سازی یک مطالبه در مذاکره نیست، بلکه حقی است که توسط پیمان منع گسترش سلاح‌های هسته‌ای تضمین شده است.
وقتی در مورد لغو همه‌ی تحریم‌های یکجانبه آمریکا صحبت می‌کنیم، این یک مطالبه در مذاکره نیست، بلکه بخشی از حقوق ماست.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/funhiphop/75446" target="_blank">📅 18:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75445">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">العربیه بمب دراپ کرد:  کار برای نهایی‌سازی متن توافق بین واشنگتن و تهران در حال انجام است. فرمانده ارتش پاکستان ممکن است فردا برای اعلام نسخه نهایی توافق از ایران دیدار کند. ممکن است طی ساعات آینده از نهایی شدن نسخه نهایی توافق بین آمریکا و ایران خبر داده…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/funhiphop/75445" target="_blank">📅 18:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75444">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">العربیه بمب دراپ کرد:
کار برای نهایی‌سازی متن توافق بین واشنگتن و تهران در حال انجام است.
فرمانده ارتش پاکستان ممکن است فردا برای اعلام نسخه نهایی توافق از ایران دیدار کند.
ممکن است طی ساعات آینده از نهایی شدن نسخه نهایی توافق بین آمریکا و ایران خبر داده شود.
دور جدیدی از مذاکرات بعد از فصل حج در اسلام‌آباد برگزار خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/funhiphop/75444" target="_blank">📅 17:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75443">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2e5bd4236.mp4?token=Xl3O8pXMxCl2hR5sZeaWOlvAVQ4yg6ywgkIvPCL1CHtQdeeq4E48RqEqCcezLSCt6POGzONbuha3S2sBx1N-nYYZ5f-mmj5U33dkbyleNIzQPBXyeExS2zl5GydXQwodiqx82TaD_ajqU606KuU-xz4eFRZ7W90A2A05ze6YuwsrC0HqdB72do13SNTr-1vFwmEwNRw_HG9YipZA0KVvLPewz2vGpo-4_Rku7LLFXtwOfB4BArgN5yagbuyEE2YDnWgOt8_lzY6yXlTAwSe6nUX5xYR-ALAR-yG9jJ34MTLpMSTG4o1I0SIMfWVBTIVr4rbVvJFnTIre0XrttyrQ1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2e5bd4236.mp4?token=Xl3O8pXMxCl2hR5sZeaWOlvAVQ4yg6ywgkIvPCL1CHtQdeeq4E48RqEqCcezLSCt6POGzONbuha3S2sBx1N-nYYZ5f-mmj5U33dkbyleNIzQPBXyeExS2zl5GydXQwodiqx82TaD_ajqU606KuU-xz4eFRZ7W90A2A05ze6YuwsrC0HqdB72do13SNTr-1vFwmEwNRw_HG9YipZA0KVvLPewz2vGpo-4_Rku7LLFXtwOfB4BArgN5yagbuyEE2YDnWgOt8_lzY6yXlTAwSe6nUX5xYR-ALAR-yG9jJ34MTLpMSTG4o1I0SIMfWVBTIVr4rbVvJFnTIre0XrttyrQ1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در ادامه:
در مقابل تعداد زیادی کشته، می‌تونیم هر دو روش معامله یا جنگ رو انجام بدیم،
ولی من دوست دارم تعداد کمی کشته بشن.
فقط تعجب می‌کنم که آیا مقامات اونها خیر مردم رو در نظر می‌گیرن یا نه، چون بعضی از کارهایی که با من می‌کنن نشون می‌ده که اونا خیر مردم رو در نظر نمی‌گیرن، و اونا باید خیر مردم رو در نظر بگیرن.
الان خشم زیادی در ایران هست چون مردم خیلی بد زندگی می‌کنن.
تحریکات اجتماعی زیادی هست که قبلاً به این شکل ندیده بودیم، و خواهید دید چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/funhiphop/75443" target="_blank">📅 17:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75442">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خبرنگار:  چه چیزی به نخست‌وزیر نتانیاهو درباره ایران گفته‌اید و تا چه مدت باید صبر کرد و از حملات خودداری کرد؟ دونالد ترامپ:  او خوب است، هر کاری که من بخواهم انجام خواهد داد. او مرد بسیار، بسیار خوبی است. هر کاری که من بخواهم انجام خواهد داد و او یک—او یک…</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/funhiphop/75442" target="_blank">📅 17:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75441">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خبرنگار:
چه چیزی به نخست‌وزیر نتانیاهو درباره ایران گفته‌اید و تا چه مدت باید صبر کرد و از حملات خودداری کرد؟
دونالد ترامپ:
او خوب است، هر کاری که من بخواهم انجام خواهد داد. او مرد بسیار، بسیار خوبی است. هر کاری که من بخواهم انجام خواهد داد و او یک—او یک آدم عالی است. برای من، او یک آدم عالی است. فراموش نکنید، او نخست‌وزیر زمان جنگ بود و در اسرائیل به درستی با او رفتار نمی‌شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/funhiphop/75441" target="_blank">📅 17:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75439">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBxtqD8lfsXI0SAnGnVseJxvFHKShsY6jxOqWl2uA38Jtr_6c0tR3gcEz7JgRjVOZQWrrMLqqB0ee_rL6WpnIcev2LXWnzl34DgJ3nr90_t3l_rng8QYE45SXcnVjx8XC3hrsPCzHsV5rJ-w3qsSsgB4JrHealKZnY0cVhATw8ZH6fKS-X83-RdYeTPecQabEtgrRK4wZ5R86u7asPAi_VxvK8_lsZMUl3J8oA8n1R2xkKdOWiTCxF9danR_7C0NL6h8TETQ1r8Vo1vViQDLLGK--nic6EmYJhu_pQr7VN15OJIRfPIkOP5FxvV9ZXdjTDUyCgBRfguwotfVlT3pSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صببخیر  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/funhiphop/75439" target="_blank">📅 17:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75438">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حصین زد یا فدایی
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/funhiphop/75438" target="_blank">📅 16:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75435">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcqYvGoL6MLfYiZbgFsRvB6hDU7Mk0nyJ2by2SpKJ6y8e51A1d2yQHr_qrYGsXNsgFDxH-C9flrl7bInh2IVikfiW_dIlPzIPtULKfuiMafI4rMHsDItN2SPUvkukLxPZLMF3ryiH_5epy8_aDctz9DOvA_DpMeIt6_EVKy1Xmf68QJ6tn_otCdeRpIU6Bc5R9FkoVuc2M4_FBBhZ3cv67lOQziUAN4WqO9XF41qjcB_jhhzbLQuoElbiLQ4L33ZWk6znE42FS_uyiDrLsqtOcYtCC1dNdD89FkWU7zdBYGuC8zRgSHqtspmNwLoKdN1MPj4ZG8soKNb2eS_jIJC-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست خدا عیان شد حضرت آقا تو یه کشور دیگ رویت شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/funhiphop/75435" target="_blank">📅 16:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75434">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نیروی دریایی سپاه:
طی ۲۴ ساعت گذشته، ۲۶ کشتی با هماهنگی نیرودریایی سپاه از تنگه هرمز عبور کردند.
@Funhiphop
| ALI</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/funhiphop/75434" target="_blank">📅 16:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75433">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سی‌بی‌اس به نقل از منابع دیپلماتیک: اسلام‌آباد تلاش‌های خود را برای حل مناقشه دوچندان کرده است و معتقد است که شروع مجدد جنگ برای همه فاجعه خواهد بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/funhiphop/75433" target="_blank">📅 15:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75432">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اگه کانفیگ با قیمت و سرعت گاد میخوایید میتونید از چارسو تهیه کنید، گیگی ۱۹۰ بدون هیچگونه قطعی و افت کیفیت:
@CharsouVPNBot</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/funhiphop/75432" target="_blank">📅 15:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75430">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نیویورک تایمز: هدف اولیه جنگ، به قدرت رسوندن محمود احمدی نژاد به عنوان رهبر ایران بود/در اوایل جنگ خانه احمدی نژاد مورد اصابت قرار گرفت تا وی از حصر خانگی ازاد شده و کودتا کند.  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/funhiphop/75430" target="_blank">📅 14:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75428">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بیانات-رهبر.pdf</div>
  <div class="tg-doc-extra">115.2 KB</div>
</div>
<a href="https://t.me/funhiphop/75428" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">تا ساعتی دیگر پیام متنی و pdf شده رهبر به‌مناسبت دومین سالگرد شهادت شهید رئیسی منتشر خواهد شد.  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/funhiphop/75428" target="_blank">📅 14:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75426">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvdGXwSgyYVfnVgKIJPTFx9uFRJinEMfyRbD9xea2DvuDA9DKA7lQ8Jo3fZiZ2_LgGtt8B7M-BqjLcFJ5u3BiPgTb8nLVZh89a5g3_M_xDRT_lkiTx_RkG_7-Ndy64xVkTKcrp802wd5Onj2KtSHIgBw-_uy8uFfX5XhrdH2lMSgRgPKpvuJaUaHhRmzXdMDI-XgmpVeTShHkAMLM4IqCOuHm414oc96_ODyM3v5stl3166nEVLcSk1L06KA_nNzzxrIvFIaFEdIuq7pRqsLPVvZellUlA60adSvSwYwkOo4GaoiMqhHt8MfXepGO55-jqDcNHfmFuR-KT9dArokWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf67fa05f.mp4?token=twn7HXWxclR42EuFKD2-Zov6msWeq9tP6FnI74UBAgNtcVJ3DEDKVPfBVyvpX1h9zTKRVdlA4OjBw08BT9wNArbmZRiUizgYrrkH2cAWCmyUIsRkZci5g3HSRBSDk_UpEghTdXzwdrB-CrusP64Gm-WhsXVXh10kUBfch7ktnMV9rOtqOzDfW30ftV0snMg9rkTao7y8UbdTX7sw1fpw86CcLkyfxEW5wC3X-od1N1pQghh28iBE58ehYFfZQtXgLSadPEADr5241b_uC_4JXhhusC0PxMGmNPgqmocZA8RDq8jG46NMbKV9j02zK4gibQKKHSRQDa9WEyAHY9Tx0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf67fa05f.mp4?token=twn7HXWxclR42EuFKD2-Zov6msWeq9tP6FnI74UBAgNtcVJ3DEDKVPfBVyvpX1h9zTKRVdlA4OjBw08BT9wNArbmZRiUizgYrrkH2cAWCmyUIsRkZci5g3HSRBSDk_UpEghTdXzwdrB-CrusP64Gm-WhsXVXh10kUBfch7ktnMV9rOtqOzDfW30ftV0snMg9rkTao7y8UbdTX7sw1fpw86CcLkyfxEW5wC3X-od1N1pQghh28iBE58ehYFfZQtXgLSadPEADr5241b_uC_4JXhhusC0PxMGmNPgqmocZA8RDq8jG46NMbKV9j02zK4gibQKKHSRQDa9WEyAHY9Tx0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانر مک‌گرگور دوباره به UFC برگشته و تو اولین بازیش هم قراره 11 جولای مقابل مکس هالووی قرار بگیره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/funhiphop/75426" target="_blank">📅 14:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75425">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚀
Velora VPN | تجربه اینترنت بدون محدودیت گیگی فقط و فقط 180 T به مدت محدود
‼️
⚡
اتصال پایدار و سرعت واقعی
🎮
مناسب بازی و پینگ پایین
📺
بدون قطعی برای یوتیوب، اینستا و استریم
🛡
سرورهای اختصاصی V2Ray
✅
تست رایگان قبل خرید
✅
پشتیبانی سریع و دائمی
📦
پلن‌های اقتصادی:…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/funhiphop/75425" target="_blank">📅 13:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75424">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXadmSi1ShgY9YLP9JPUkxu5q-1TS1EnjozE7-0F5aJ_A6whPoH9NJZTVFU_pz15b387Fn0uMVUqPhGyspNf9DhEanOqGrhWRFkG4at_lNTZjS-30313JqDF-7iLk1nMtFxuTFERPMqVxUqeAmKJIDg0CKLJyDWhTKvb7RtmJe20Ag3aQebgBjLVVnnzec5czPemcNIUOUYBeYeCi3ykPJQfdb6ivzFUWjiYvytJ-BFXUyJ3kOIku5UwAy9VacO3Z4bPhdvfhVpA4-u2lJ0e-ObrLtRA9m3GgbP791UpAKV5rBL0j_USrr_Y9TB036VKHPeKj2YFyjbj8cswnbgL7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔜
اکنون روز ۸۲ام
#Iran
در خاموشی دیجیتال است و پس از ۱۹۴۴ ساعت، کشور هنوز تا حد زیادی از اینترنت جهانی قطع است.
در دورانی که قطع ارتباط حتی برای چند دقیقه بحران محسوب می‌شود، ایران همچنان رکوردها را می‌شکند، معیشت‌ها را نابود می‌کند و حقوق را تضعیف می‌کند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/funhiphop/75424" target="_blank">📅 13:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75423">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رشید مظاهری قصد داشته است با تغییر چهره و پرداخت رشوه به ماموران مرزبانی از مرزهای غربی به‌صورت غیرقانونی از کشور خارج شود که در هنگام خروج‌‌ بازداشت می‌شود./ به همین دلیل هست که در زندان مرکزی ارومیه به سر میبرد
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/funhiphop/75423" target="_blank">📅 13:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75422">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تا ساعتی دیگر پیام
متنی
و pdf شده
رهبر به‌مناسبت دومین سالگرد شهادت شهید رئیسی منتشر خواهد شد.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/funhiphop/75422" target="_blank">📅 13:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75421">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وزیر کشور دوست و همسایه پاکستان مجددا برای گفتگو با مقامات ایرانی عازم تهران شد.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/funhiphop/75421" target="_blank">📅 12:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75420">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">صرافی ایرانی اکسکوینو مردم و اسکم کرد. قوه قضاییه داره دفتر های این صرافی و پلمپ میکنه.  البته نا نگفته نمونه که مدارک اسکم این صرافی از چهار سال پیش توسط فعالان رسانه ای اراعه شده بود ولی کسی اهمیت نمیداد و بالاخره این اهمیت در این روز ها شکل گرفت.  @FunHipHop…</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/funhiphop/75420" target="_blank">📅 12:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75418">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/funhiphop/75418" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75417">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/funhiphop/75417" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75416">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhdcifJo-uFnj0hsUSQrWOhiFXCj0pXvx4YhBcUFMFeXgJR2dg9etPhRLbKSsTxsOATspmagUs9KlTHiM8pg8H-zU-chmz4g7ZVtLpMVnzeanqq5sAZJVc1Nd4uNlmrMVfjqYIi4whUMUYz4l-8Vq8XjBBNkPqLepfeBXr6_ADX-uVXYJm9s-U39KNiOxGjPpltpSavrwiUHczqywvpzaPdR2ZXXeSWRxufFlJLdb5GT0Z-29TQeqEGM5e076apit1yke9HBDOdZor2AgVEiKU7iVmec2lngyNAqkgTj08-ifFKD0NODOaR5h0Ce3k6T7FreH1VXNgCmD1Z4FG42Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز:
هدف اولیه جنگ، به قدرت رسوندن محمود احمدی نژاد به عنوان رهبر ایران بود/در اوایل جنگ خانه احمدی نژاد مورد اصابت قرار گرفت تا وی از حصر خانگی ازاد شده و کودتا کند.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/funhiphop/75416" target="_blank">📅 12:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75415">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVoWy7fk3P92vgiXYa-L6boCYymRewjyIWG--GGjUzbtL2d9MjhzGnICADvE-siDkGueP6PVLeqFO_3nH6MAUBn-tcDwJFk9A1ayw4QZniUYmfK5yUxpIuWn2uOkbJ39zlULTx0AhvF_VgCkKCKlOfdDvA3-9Tdpl0ug8jgQQi0MclcrHZwzIIN0PLHc5hyxbs9nrVmVXQxFCPwK0hq0i4vxQRheiCUKx8vqIfQldc_zssjm5SKrRT6H7k8vDczNd-ZkDP7rf9vlwVxEIlPKuV1EdD3dS5SuIhZ-gMUUCvKWAEyZWBfgDseolw9fKsjrLHdFqialM9co3_5BjWIDnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسری وصلی های جزئی به اینترنت داشتیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/funhiphop/75415" target="_blank">📅 11:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75414">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W08oqSDkphmEa04Oby9-V1lS_F4GW4cs8Za4XyHO8qk4tSSu7UZD477S5-EFFmtN8qaV09VQUe0Bn9XvXNSPPxPOXjVIsKvMRG_oDOREcj-Sqg262tcqVVWcsal_gq1_JvFO9A2jmdP9Mn878axySpE1fnYwm5QPcUzLVGzju-1FQWk7u4qHpwZRLVgJ60qRwdXaF-q3n0ZejRrN8ENB3FXK4ZD11EK6qQXvxzmy5OBZyJLvDSdozrKIDZ3U7NN1NVSaFNYFpl3XOm_jBW-YYJOV-vq_1XmL9oFi9UE3eXI5DgmJOxa2wqsuepUJEdgzONnnnqLSECm8ucL4Kco63A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Velora VPN | تجربه اینترنت بدون محدودیت
گیگی فقط و فقط 180 T به مدت محدود
‼️
⚡
اتصال پایدار و سرعت واقعی
🎮
مناسب بازی و پینگ پایین
📺
بدون قطعی برای یوتیوب، اینستا و استریم
🛡
سرورهای اختصاصی V2Ray
✅
تست رایگان قبل خرید
✅
پشتیبانی سریع و دائمی
📦
پلن‌های اقتصادی: 5GB | 950T
10GB | 1800T
20GB | 3500T
50GB | 7500T
100GB | 13,000T
📩
خرید و پشتیبانی:
@VeloraSupports</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/funhiphop/75414" target="_blank">📅 11:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75413">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سپاه:  اگر بازم بهمون حمله کنید اینبار جنگ رو از حالت منطقه‌ای به حالت فرا منطقه‌ای می‌رسونیم.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/funhiphop/75413" target="_blank">📅 11:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75412">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سپاه:
اگر بازم بهمون حمله کنید اینبار جنگ رو از حالت منطقه‌ای به حالت فرا منطقه‌ای می‌رسونیم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/funhiphop/75412" target="_blank">📅 11:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75411">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">حمله بعدی امریکا کوتاه هست و میان یه لایه دیگ رو حذف میکنن و دوباره مذاکره میکنن و فشار میارن که تسلیم بشن.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/funhiphop/75411" target="_blank">📅 10:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75410">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPIQ26nE8R1tahyGwEGSCaRMP6XAf1aJrbPODUrnE-sDqdfg1SGV0d6RZ0MtC9r9Dl9Xx7fkqbuLXnsZMAT6Jzp5E8MTai0a1cCqSteOjKV4mL7LX7EEk4C_39ZuTEde5XXG58Enn9W5f6jOWuYmCnuqK3YExWldgtNCgIO_DNDGzYM-LEueV9fphRED768KNePnMxsOMKP3UAaVZ6hqalaib3XvdyBPT6dyYhb6tK1FC715zoEL_PljpVJivhZ5fMxkWVs-QQYrmc7UxxG0N7N_cJfvONvjrJeCY7qbXXgofd_kjoVLSfcCBz1fxIeQjt6FEUJjWbd_TxyzpqXq_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای از ۱۸ مه نشان می‌دهد که ایران چهار ورودی از پنج ورودی تأسیسات موشکی زیرزمینی آبیک در استان قزوین را پاکسازی کرده است.
پنجمین ورودی تا حدی پاکسازی شده است.
این سایت در جریان حملات هوایی آمریکا و اسرائیل برای به دام انداختن موشک‌ها در داخل، عمداً مورد حمله قرار گرفت.
ارزیابی‌های گسترده‌تر اطلاعاتی آمریکا نشان می‌دهد که ایران اکنون دسترسی به حدود ۹۰ درصد از شبکه موشکی زیرزمینی خود را بازیابی کرده است.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/funhiphop/75410" target="_blank">📅 10:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75408">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DZn5GeaN6Tjv5J99Y-kTrMJFOuRvhRxpNtXP3KQjIL-TezFijoynlIf2MrKLDM8lx6yLPmh9ebxj48jpnyGyFsghz43k2clZD7kro0xMBjZdWdfkQ35Gm8Dr9gX3Qq54vacyF_1Dx3Pt28eLoPD-DKPsZn40A53mWcPEcawlapZ6_fTsrpdoxvNemyTHsfpLq53vrUBqOaPQftEFVuzjWEqoCZRuwIrTgX1VDCqoqkb5BXeUZ3gKK4hL2oVBIYPDjyUxngMuA2yHNZo0qTOmsg09qQeltdb9qW3ffaz8IhJ5JRX7BRMoy02ffN2gjQqEEiVYE7q7Y1h9xDjtsqGbiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tn0etvdgtqhTeqHc3Qyrp2rlXSEXmhs49ZKvnGECpaZFD2_QzXmVQiBUjbwSxpm2lkiU_qeXRuMFIPC9IMGGfpEgUvD_K8OmVjGWWCQ1plK4dRrwSazbDl1T0a4MYrGM0pWdrfKpOn1O0LrtoS6iT9TpgLzqKnoPsYWinSAD7-ocJ4ioquoVqoF8Nq98pYj0m_MFLaiSzCl1v_g3rIZehKooob8tZdaSS9CboJhFi5BTJzqnSHvYue0iERd9F1w1rmRpwUeqn3wgWq3KRccQ6o8kqu4qFS_LZwIJVs9YvG6iRg64Sal5Tqg59_98al6LFLYTofhmsCtuNL9aEeZQPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به مناسبت قهرمانی آرسنال، همچنین یادی میکنیم از جاویدنامان امیرحسین الوند و علیرضا صیدی
❤️
@FunHipHop
l Farid</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/funhiphop/75408" target="_blank">📅 10:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75405">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شمال یجوری داره بارون میاد که شبیه افسانه ها شده
سال های پیش اصلا چنین بارونایی نمیومد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/funhiphop/75405" target="_blank">📅 08:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75404">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پوتین رسید چین
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/funhiphop/75404" target="_blank">📅 08:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75403">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jw0kv7NfPyy5Tokkvbbkq1JbbCxVr1H4PeqB580S0U4lSHDtIR6QNUgTUuH-SS0_smXijWNNB2rfdmJIWU-UDT2gkqdvFPFi-oXK8YKpWH-M8W8PA_r8an-5Cuc1uxg2BaddjJLbYpCQ1DG3hbPulMHmvaOMl1_0FjSEciLwEx1-rmv_yYYzCn86NggEoOg5i_lxH83kfjmOhdG3ld21ABfnNq46UMGH7qWIBQdndmUhTMTuUHhY4vYj1VwuRbgay-iYzY4rIfwNufahiQxDHodV9a6f8Bn74OBjCnO2nz1v3WdsgAVkyZMJYCpzF9u-xRPvwtrqVS-JfFuUXepckA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی ایرانی اکسکوینو
مردم و اسکم کرد
.
قوه قضاییه
داره دفتر های این صرافی و
پلمپ
میکنه.
البته نا نگفته نمونه که مدارک اسکم این صرافی از چهار سال پیش توسط فعالان رسانه ای اراعه شده بود ولی کسی اهمیت نمیداد و بالاخره این اهمیت در این روز ها شکل گرفت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/funhiphop/75403" target="_blank">📅 06:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75401">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نیویورک تایمز کاملا از حیطه کنترل عقل خارج شده:
پیش از آغاز جنگ با ایران، آمریکا و اسرائیل نقشه‌ای برای نصب
محمود احمدی‌نژاد
، رئیس‌جمهور سابق ایران، به عنوان رهبر ایران طراحی کردند.
این نقشه زمانی به مشکل خورد که
احمدی‌نژاد
در روز اول جنگ در حمله‌ای اسرائیلی به خانه‌اش زخمی شد.
از آن زمان تاکنون به صورت عمومی دیده نشده و محل فعلی او نامعلوم است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/funhiphop/75401" target="_blank">📅 03:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75400">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آکسیوس:
برخلاف ادعاهای ترامپ که می‌گوید یک ساعت تا صدور دستور حمله فاصله داشته، مقامات ارشد می‌گویند ترامپ اصلا تصمیمی برای حمله نگرفته بوده است!
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/funhiphop/75400" target="_blank">📅 03:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75399">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کانال ۱۲ رژیم صهیونیستی جنایتکار بد:
ترامپ در ۲۴ ساعت گذشته هم در گفت‌وگوهای عمومی و هم خصوصی موضع تند درمورد ایران داشته است.
او در جلسه‌ای با برخی از نزدیکان حامی حمله گفته که هنوز گزینه حمله را کنار نگذاشته و این احتمال وجود دارد که انجام شود.
در مورد زمان‌بندی، حتی در گفت‌وگوهای خصوصی نیز ترامپ یک جدول زمانی «مبهم» ارائه داده که بین یک تا چهار روز متغیر است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/funhiphop/75399" target="_blank">📅 02:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75398">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پس از ۷ تلاش ناموفق، بالاخره با عقب نشینی برخی جمهوری خواهان، دموکرات‌ها موفق شدند و سنای آمریکا طرحی را تصویب کرد که مصوبه کنگره را برای ادامه حملات نظامی به ایران الزامی می‌کند.
سنا با رأی ۵۰ به ۴۷، اکنون به طور رسمی «قطعنامه اختیارات جنگ در ایران» را پیش برد.
این رأی فقط گامی اولیه در سنا محسوب می‌شود. و حتی اگر هر دو مجلس کنگره این قطعنامه را تصویب کنند، انتظار می‌رود که ترامپ آن را وتو کند.
اما دموکرات‌ها می‌گویند این اقدام حائز اهمیت خواهد بود و می‌تواند طرز فکر رئیس‌جمهور را در جنگ تغییر دهد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/funhiphop/75398" target="_blank">📅 01:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75397">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcSgkRpaeS5z2bWArtjJDTyuZ_2oCUWVJYdTkVq09-yrHYJiXD1rWBm_hqrZyEKKwzuo40VRn8syzdnhSsRKITKjrUlf5gwlBSBb47C97LEBk04p5CS8QgUQa9YOtKbvbivSC0m5cQjgjJg3as1vdY3EPeoonVvebJ7pMhiHC-eEhGjsqVEoQN6r0ay6-vLeX-vUiDBvlcREQO-2BfJWCdWj1ln-F2sYTG_Am7ajcdVp-GVrHysswGykBfQEWkw7MQiYhIk_37XBowQLyU1rEQ3QYv3eW_sh3fKVlQWhfQYEL1rxmOcF1OJzb-IjS9yw89y1iaddFFo7z1WkJNV3Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز:
فیفا قصد دارد بار دیگر ورود پرچم شیر و خورشید و پوشاک مرتبط با آن را به استادیوم‌های جام جهانی در مسابقات ۲۰۲۶ ممنوع کند.
این پرچم همچنین در جام جهانی قطر ۲۰۲۲ محدود شده بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/funhiphop/75397" target="_blank">📅 01:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75396">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLyHt2thE8MTJITd0zjLlgHEUXjOPAsaWdKKohEoXmpqlx_nZ6wxOEyhLwXDHNP1hUAKmJ2bjWicIalIkaX0a0AQC09i42rfZv6kH-p41EKtnDkRL9s3KMg5puypbkn_nS9dZHnLlsyYDfs8hB3fbGtp78Vka9MpOmRbGlopZNaEK7vXSTUyMgh4TZP1n0Vh9A8AGJa5x-sGKDcyZbS9GFk623qM3K4B2lZ4XmU_a4VtfxmraVJ2VQWTdds1T1RbLWMa-gadSCsp0M4vRUipphfCp-o_H5aRzEy0J0HGjDATYkQe3ZYs7MbUDxF2hr86lp0CSe8mDoFOsouUE2qMyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفسور عراقچی:
ماه‌ها پس از آغاز جنگ علیه ایران، کنگره آمریکا به نابودی ده‌ها فروند هواپیما به ارزش میلیاردها دلار اذعان کرد.
اکنون به‌طور رسمی تأیید شده است که نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه F-35 را سرنگون کردند. (به اجدادم قسم اون f15-E بود)
با درس‌هایی که آموخته‌ایم و دانشی که به‌دست آورده‌ایم، مطمئن باشید بازگشت به میدان جنگ با شگفتی‌های بسیار بیشتری همراه خواهد بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/funhiphop/75396" target="_blank">📅 00:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75395">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMpdk2UcV2AXKsT15a8QD37I-r5xzoRLxTNiOskLnv9QZECpDjxbHGA6mxj2Ml6mdGbRatMRdWbE5MNKb_Pp4qpXK86QgesrzPtoR7gu33fwFHvtM8QGOP5Unt2H00gEnKkoG0B_unnktkWISif-CMMYMG4AyQStfaVBn4eU3owciRXZwQRmFsvwYBZd0obJpbRSJqvKoC6mk4XOUTUVAvZmd5IGxC2zj4iyb9eCPkpZPP9UY8rgF43JCODYl1vXcK0be6WmUlhvMSH5g0Sqh1L5D9SZSPdidDMYUoBXWYcuRZ2CtQHoc-S-9bMqpQO25RcORAOT_eJ7cVZZkmn2Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت قهرمانی آرسنال در لیگ برتر، یادی کنیم از جاویدنام عارف جعفرزاده
❤️
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/funhiphop/75395" target="_blank">📅 00:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75394">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">آرسنال پس از ۲۲ سال قهرمان لیگ برتر انگلستان شد
🏆
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/funhiphop/75394" target="_blank">📅 23:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75393">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دیگه به هادی چوپان نمیشه لقب آرسنال داد باید به همون مادرجنده کفایت کرد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/funhiphop/75393" target="_blank">📅 23:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75391">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حکم پژمان جمشیدی صادر شد و به ۹۹ ضربه شلاق تعزیری محکوم شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/funhiphop/75391" target="_blank">📅 23:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75390">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d909bc992.mp4?token=PY-BU3sDZeB8Gu_F9Addab4WhEyvfhpPWe4DbHKWdOufoOaXJh_L0AcsmKVZFncOwp4PEQgHdzoflQcarJh7JJgL6x4FJvT__HGLa3XJHceqcHTTyl-XU_kBCZTiwMG7xjr9iFN_qK_fMZNiuImHxays19fK8hGtjKZ3g72jAkM0avfvFPlxca07HzSMDH8SJDNG3otZT6oV0t6B39haalM-FNypcF4is7623NQVfy-tJ9odv_wDEiFZORPcx6ZyVBFI22HXOWAN4qDnOtkgv3PIa5fDmYJDpCQ1LdJe7IGqsQCkGWfvvw5-dGwsSwoEL3ezXB7c3PuQmeEQxfN1nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d909bc992.mp4?token=PY-BU3sDZeB8Gu_F9Addab4WhEyvfhpPWe4DbHKWdOufoOaXJh_L0AcsmKVZFncOwp4PEQgHdzoflQcarJh7JJgL6x4FJvT__HGLa3XJHceqcHTTyl-XU_kBCZTiwMG7xjr9iFN_qK_fMZNiuImHxays19fK8hGtjKZ3g72jAkM0avfvFPlxca07HzSMDH8SJDNG3otZT6oV0t6B39haalM-FNypcF4is7623NQVfy-tJ9odv_wDEiFZORPcx6ZyVBFI22HXOWAN4qDnOtkgv3PIa5fDmYJDpCQ1LdJe7IGqsQCkGWfvvw5-dGwsSwoEL3ezXB7c3PuQmeEQxfN1nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرمانده سنتکام به کنگره:  مدرسه میناب در سایت فعال موشکی قرار داشت.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/funhiphop/75390" target="_blank">📅 23:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75389">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فرمانده سنتکام به کنگره:  مدرسه میناب در سایت فعال موشکی قرار داشت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/funhiphop/75389" target="_blank">📅 23:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75388">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🛍
تخفیف ویژه تا پایان امشب
🛍
دوباره تخفیفمون رو تمدید کردیم
😍
هر گیگ فقط 149 هزار تومن
‼️
✅
پینگ عالی و پایدار
✅
بدون ضریب و محدودیت کاربر
✅
لینک ساب برای مدیریت حجم
✅
پشتیبانی ۲۴ ساعته روی همه سرورها   200 گیگ شارژ شد
⭐️
تا تموم نشده به ادمین پیام بده…</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/funhiphop/75388" target="_blank">📅 23:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75387">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🛍
تخفیف ویژه تا پایان امشب
🛍
دوباره تخفیفمون رو تمدید کردیم
😍
هر گیگ فقط 149 هزار تومن
‼️
✅
پینگ عالی و پایدار
✅
بدون ضریب و محدودیت کاربر
✅
لینک ساب برای مدیریت حجم
✅
پشتیبانی ۲۴ ساعته روی همه سرورها
200 گیگ شارژ شد
⭐️
تا تموم نشده به ادمین پیام بده
🔗
کانال مشتریان
🔗
خرید</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/funhiphop/75387" target="_blank">📅 23:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75385">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">من سیتی گل خورد
قهرمانی آرسنال از همیشه نزدیک تره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/funhiphop/75385" target="_blank">📅 22:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75382">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceda97bf16.mp4?token=RLvKUx2q7dz_NB4ryRDc7-12EsfUFr1HvmvIFELmLtHHRhrbzkhtxJWLN8qV8v2ohl6809JGsRx7OCSOWXBHz6fvuih25r4ymSpc426XD3_Z2pEzCpf9Cb5IcJqRo_ffrzg_Ji3oy2M1thgNhwbMKIS93F328pvUQTciPk4QsyCHw_sjRNfa9lvW2o5MqJHlq8EhW7COkbYKms-5e5eihjXa2JkOe6ViTYMzc2uFU-COu5jQ5PxPnptpMzsESj74X4cwbeibo3uOPNawz7RCbLmEZ603uIJ_KTY-QIWaqXL5ttFInt9D1XezVzM6hBXScNYnViOeHZz7H-c9D-8Kig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceda97bf16.mp4?token=RLvKUx2q7dz_NB4ryRDc7-12EsfUFr1HvmvIFELmLtHHRhrbzkhtxJWLN8qV8v2ohl6809JGsRx7OCSOWXBHz6fvuih25r4ymSpc426XD3_Z2pEzCpf9Cb5IcJqRo_ffrzg_Ji3oy2M1thgNhwbMKIS93F328pvUQTciPk4QsyCHw_sjRNfa9lvW2o5MqJHlq8EhW7COkbYKms-5e5eihjXa2JkOe6ViTYMzc2uFU-COu5jQ5PxPnptpMzsESj74X4cwbeibo3uOPNawz7RCbLmEZ603uIJ_KTY-QIWaqXL5ttFInt9D1XezVzM6hBXScNYnViOeHZz7H-c9D-8Kig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جِی‌دی ونس :
ایران کشوری بسیار پیچیده است. کشوری است که من تظاهر نمی‌کنم آن را بفهمم...
این یک تمدن بزرگ و پرافتخار است.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/funhiphop/75382" target="_blank">📅 22:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75381">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9aacc343d.mp4?token=LqZ7Z0GREPf0FjGfEe7V1rO-LWD1Zthw2ZrDw-lRHIDtYQifQq-6MZBQgkYj7mjs-8IJRNNa1KrxNTCCWw6n_aRoLZ86U20vbrHoDPLXTgL-oocja7bDnyRRQb0ER56WM80CYo_m5QcS0zcj9Lm9yNbNIAqTyvuK9kLEU_H6oF7WzXbcCC0rZNK9YTCeS7zJlWiBF0oOra0oSMB9vEc98aJCfqPw4x09bDQVmk3E9rWG4OkvsXU-taof6CBov4ylJy3jrTsT2fnkbFpyGySfOE3nafxLzeySIMogEe5hXMTqBmFO23NUzkvU-8WH-IBfbdjtCwJiT-qZ9EOMhSQJog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9aacc343d.mp4?token=LqZ7Z0GREPf0FjGfEe7V1rO-LWD1Zthw2ZrDw-lRHIDtYQifQq-6MZBQgkYj7mjs-8IJRNNa1KrxNTCCWw6n_aRoLZ86U20vbrHoDPLXTgL-oocja7bDnyRRQb0ER56WM80CYo_m5QcS0zcj9Lm9yNbNIAqTyvuK9kLEU_H6oF7WzXbcCC0rZNK9YTCeS7zJlWiBF0oOra0oSMB9vEc98aJCfqPw4x09bDQVmk3E9rWG4OkvsXU-taof6CBov4ylJy3jrTsT2fnkbFpyGySfOE3nafxLzeySIMogEe5hXMTqBmFO23NUzkvU-8WH-IBfbdjtCwJiT-qZ9EOMhSQJog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنان قصار استاد جی‌دی ونس درمورد ایران:
تا هنگامی که ندانید، هرگز نمی‌دانید.
تنها کار خوبی که ما می‌توانیم برای ایران انجام دهیم، مذاکره با حسن نیت است...
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/funhiphop/75381" target="_blank">📅 22:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75380">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">امشب به احتمال خیلی زیاد آرسنال قهرمان لیگ برتر میشه
پیشاپیش به طرفداران این تیم تبریک میگم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/funhiphop/75380" target="_blank">📅 21:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75379">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مقام امنیتی ایالات متحده به کان نیوز:  تدارکات مشترک ایالات متحده و اسرائیل برای از سرگیری عملیات نظامی علیه ایران تکمیل شده است، انتظار میر‌ود ترامپ به زودی تصمیم بگیرد.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/funhiphop/75379" target="_blank">📅 21:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75377">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwqqCvvL9MKEkdRlIZRcEd9krkSO1g0zuC7dtg79LRhHKP35c2NQzbNBw7cebZXaFY7pkxIGWpJKdPfwoWq7XGrZrOKf-Nmp7HwqovgaILNROkeso9IqCIPWd7Gr76gaosFXw_I7qjYihlrVJZhkGzbDUZ6JWS1lugLt5oO2cEZuZKoFla7phkYYWEW6nTQzyB5mK5TloORC2edA3WlSPCBdAmRESkM4hkq0QNCQ0clKuOt6II0bSl5udzQ8NbcMS1tDFbVHRzPkWtNQ3h-8IyrindidbVMbSKzWkhqO6k4wWbXePCdqxm4wrDd3ndVBiaInV4ERH1u339DVtNLAeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گیگی ۲۰۰ پول وی پی ان میدم که برم اینستا از هر سه تا ریلز دوتاش صدای آنچلوتی باشه که میگه نیمار جونیور؟  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/funhiphop/75377" target="_blank">📅 21:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75376">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
تخفیف ویژه زیر قیمت کل تلگرام!   دوباره تخفیف رو تمدید کردیم!
🧃
قیمت هر گیگ فقط 139 هزار تومان!
😈
( فقط 300 گیگابایت موجوده! )
💥
✅
بدون ضریب و بدون محدودیت کاربر
✅
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی می‌باشند.
🤩
@TornadoAdmin…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/funhiphop/75376" target="_blank">📅 21:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75375">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مقام امنیتی ایالات متحده به کان نیوز:
تدارکات مشترک ایالات متحده و اسرائیل برای از سرگیری عملیات نظامی علیه ایران تکمیل شده است، انتظار میر‌ود ترامپ به زودی تصمیم بگیرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/funhiphop/75375" target="_blank">📅 21:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75374">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4psOwfStC6lBlzJruHRY41zuB23zwZGPfc9AyXg52h1WxtOLxHcU1A56WcHYYAOli9ybI64hBzt9T-Ah_Ed2W4w9sKhQSTktDLMXeSxR6lyiIJHnhQkcWHGnfHnZ85anDXxeiRCpkPsNtTFC2k8RYvuhRHVrYLrd5j52-wm1Ctp_GJTkwd23Pa_NMQ8iKPNe_yiZm8HBY0olHumjZLgUjeIJLlZpoIw9FwdrsgwE30Ep1YDRBU-glkcGH8rtn8uqNFBgbBreX5swovXfHwlKj9KcIPddYOWIWtRpHWGfIOEmQCPZQp0kG2zkIx3NwDOi1nomxipeshjaBZj9XRETw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و استاد جنگ هوایی و دریایی.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/funhiphop/75374" target="_blank">📅 21:06 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
