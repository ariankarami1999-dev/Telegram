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
<img src="https://cdn4.telesco.pe/file/VjqPWb0F2LO6KW6EfzBdMRpcAoDWBIlpECFAIGYH0zrTYekiWGWQTodVeH7P6HD5F8f8dBAFbXoXtaHWCA-hQes-jHwtvkwql4QLxc6-LJ_BwDuV0C5o2FX5-stUnZPgaSddx1SNYrF-qAR0OmBihUgxqfRCY8xyHWJJjCE8cjAxvZql-KwY4XaNA9FcnNRv4Q3N8xdn9A-v4CXsqrexrx-k44upOWhanRsvXGlH1bs2uox1er76r1H-vZGlM0_C77GZwn8ulKPxbeSgQw74ubzn7ercw0CnUZ3hEUhKLfR0DeXjBIi2oxv1HXlebAifESf1c6MAC3YMffF83KVpAQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 23:57:09</div>
<hr>

<div class="tg-post" id="msg-134977">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">⚠️
هوادار باید فشار بیاره کنسل بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 731 · <a href="https://t.me/SorkhTimes/134977" target="_blank">📅 23:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134976">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
شنیده ها : محسن خلیلی دیروز با مهدی تارتار جلسه داشته و این مربی اعلام کرده در قرارداد جدیدش با گل گهر بند فسخی داره که میتونه به پرسپولیس بیاد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 824 · <a href="https://t.me/SorkhTimes/134976" target="_blank">📅 23:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134975">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس توافقات با مهدی تارتار انجام شده است و باید تارتار رو رسمأ سرمربی بعدی پرسپولیس بدونیم!
📚
مهدی تارتار یک دستیار اسپانیایی انتخاب کرده و با خودش به پرسپولیس میاره؛…</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/SorkhTimes/134975" target="_blank">📅 23:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134974">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس توافقات با مهدی تارتار انجام شده است و باید تارتار رو رسمأ سرمربی بعدی پرسپولیس بدونیم!
📚
مهدی تارتار یک دستیار اسپانیایی انتخاب کرده و با خودش به پرسپولیس میاره؛…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/SorkhTimes/134974" target="_blank">📅 23:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134972">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
|
#فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس توافقات با مهدی تارتار انجام شده است و باید تارتار رو رسمأ سرمربی بعدی پرسپولیس بدونیم!
📚
مهدی تارتار یک دستیار اسپانیایی انتخاب کرده و با خودش به پرسپولیس میاره؛ همچنین فردا جلسه آخر بین پیمان حدادی و مهدی تارتار برگزار خواهد شد،که «شاید» منجر به رونمایی شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SorkhTimes/134972" target="_blank">📅 23:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134970">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SorkhTimes/134970" target="_blank">📅 23:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134969">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
همه دوست داشتیم اسکوچیچ بیاد ...ولی با شرایطی که گذاشته بود .مبلغی که میخواست بگیره .کار و سخت کرده بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/134969" target="_blank">📅 22:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134968">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
پیشکسوتان پرسپولیس! همچنان علاقمند هستند مهدی تارتار سرمربی پرسپولیس شود و به دنبال فشار آوردن به هیات مدیره باشگاه برای انتخاب او هستند!
🔴
🔴
مهدی تارتار حمایت های علی پروین، خودش رو تبدیل به گزینه اول سرمربیگری پرسپولیس کرده!
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/134968" target="_blank">📅 22:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134967">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فووووری از قدوسی: مهدی تارتار به احتمال زیاد تا ۴۸ ساعت آینده بعنوان سرمربی پرسپولیس انتخاب خواهد شد
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/134967" target="_blank">📅 21:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134966">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/134966" target="_blank">📅 21:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134965">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
مارکو باکیچ: دوست دارم وحید هاشمیان به ‌پرسپولیس برگردد
😕
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/134965" target="_blank">📅 21:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134964">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❗️
دیگه چاره ای نیست باید حمایت کنیم ..دیگه باید بپزیریم .شرایط مملکت جنگیه و هر لحظه احتمال جنگ هست ..خارجی نمیاد ..اگه هم بیاد ..جنگ بشه سریع فرار کرده و کل پولش و گرفته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/134964" target="_blank">📅 21:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134963">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">https://t.me/+Bt80HN28Ils5YWE0
همه فرما رایگانه رفقا
✅
✅
⭕️
فرمهای امروز از بازیهای جام جهانی رو از دست ندین
#VIPرایگان</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/134963" target="_blank">📅 21:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134962">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ji7O6RRKo3owm4DiwkrJPbReMWTvbT7A52rEhb9OpwJsQOmUjBpnhX6MwnuIrfNb9CJI_F75CjusDeHqmRvdk9MCBVU9xqcYvYeO8LJlOsgWAp2uYrwVMhYAvyaqmeGG1UBRVqBuaFaJP7PGD2rIy1TQBWCTWclybXQFhIv51-ZwE9_lv4LCor8qbWDg43jzluZ1zq4uzctRVXnglUFn7-CpWjxR7JQmQjXB4TULdjSg3siele_H6gBx8YQ25--XiWDQnap4S1tC4SIGcFqR6ue8T2XpK0qBctvwCGrXP-jgmqwXMJajkv6KErHo0wSASLbvEV56l5Uq8QJOEaTyyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دوستان بت زن این کانال مخصوص شماست
بهترین آنالیز ها و آموزش ها
🆓
📈
اشتراک سایت های معروف خریداری میشه و براتون رایگان قرار میدن
💥
🥇
آموزش های جذاب و سود ده در مورد شرطبندی فوتبال
💡
چالش و قرعه کشی ها با جوایز دلاری
💵
✔️
⬇️
⬇️
روی لینک کلیک کنید
⬇️
⬇️
https://t.me/+Bt80HN28Ils5YWE0
https://t.me/+Bt80HN28Ils5YWE0
🏆
فرم از بازی امروز
🇫🇷
فرانسه و پاراگوئه
🇵🇾
با ضریب 3.50 گذاشته شد</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/134962" target="_blank">📅 21:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134961">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
✅
حاج مهدی تارتار بلاخره به آرزویش رسید ..امیدوارم صدش و بزاره و قدر این محبت خدارو بدونه ....
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/134961" target="_blank">📅 21:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134960">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فووووری از قدوسی: مهدی تارتار به احتمال زیاد تا ۴۸ ساعت آینده بعنوان سرمربی پرسپولیس انتخاب خواهد شد
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SorkhTimes/134960" target="_blank">📅 21:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134959">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tMaBc8ySZ2wXTNHZXBfsr0zXZR2t032y3EpsCFd4zx7N4aW-7C6rj1ldaYfcgvKm6923Wl9SqJFjzCnDHl7YBqIRvrGSx5mijAkYXMHipqam9ztOk3Whrn2cGHqmBbC_fm91VHD1dXafdCsUlDZAmOVfE2iMOtMd_ZCuAdiD8A_pzz4NzePZUHzuT3y8xamO7iHUhemaz2Vl8Uj1QcN3MhWMWiB9GJ0IG0XY_W10pGiNJ1EzqCWzpx_6Y1M6yt66hx8N_VanEwdWCVxZEW_t97F5f7H1uQTLWEInEzKWQsCY1y3LFqaN56ILkJjE_0fpQyh_a2rFhM4xbACppdNL1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
فووووری از قدوسی: مهدی تارتار به احتمال زیاد تا ۴۸ ساعت آینده بعنوان سرمربی پرسپولیس انتخاب خواهد شد
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/134959" target="_blank">📅 21:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134958">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/134958" target="_blank">📅 21:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134957">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❗️
دیگه همه گزینه شدن باید ببینیم کی مربی پرسپولیس میشه ....
❌
مازیار
❌
یحیی
❌
تارتار
❌
مطهری
❗️
مجتبی حسینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/134957" target="_blank">📅 21:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134956">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
سرمربی جدید و ایرانی پرسپولیس فردا نهایتا پس فردا مشخص خواهد شد/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/134956" target="_blank">📅 21:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134955">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❗️
دیگه همه گزینه شدن باید ببینیم کی مربی پرسپولیس میشه ....
❌
مازیار
❌
یحیی
❌
تارتار
❌
مطهری
❗️
مجتبی حسینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/134955" target="_blank">📅 21:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134954">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
✅
باشگاه الشمال قطر با ارسال ایمیلی به پرسپولیس خواستار جذب اورونوف شد. این تیم اعلام کرد که حاضره 3.5 میلیون دلار برای‌ جذب اورونوف به‌ پرسپولیس پرداخت کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/134954" target="_blank">📅 21:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134953">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
⚽️
❤️
عبور اوستون ارونوف از آلن ویتل
🔴
اوستون ارونوف با گلی که به سپاهان زد، با پیراهن پرسپولیس ۱۵ گله شد و به این ترتیب از رکورد ۱۴ گل آلن ویتل گذشت.
🔴
ملی پوش ازبکستانی پرسپولیس حالا در جدول گلزنان خارجی پرسپولیس در رتبه دوم قرار دارد.
🔴
همچنین سرگیف، هم‌وطن…</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/134953" target="_blank">📅 21:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134952">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
ترامپ به آکسیوس: همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/134952" target="_blank">📅 20:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134951">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
❌
مارکو باکیچ:
🔴
دعوا توی رختکن بین اعضای تیم و کادرفنی یه چیز طبیعی توی دنیاس و حتی توی اروپا خیلی شدید تره؛ اما تفاوتش با اینجا اینه که توی اروپا این موضوع رسانه ای نمیشه اما توی ایران بیش از حد بهش پرداخته میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/134951" target="_blank">📅 20:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134950">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mom0LU0huw-zy6TUOs-pVxMec4GoHdFsWPxb0nNmRZIF3kmyp2x_KCSY3mzFe7qvWX_94Pq0CfzZOcngNudqHX2wLTR2wwDyTG3hCntQTdJO8WLdvFFW0NzFsRNM80U3zv2ZmZd1n5ELb-6AzkSMB0vJxSL7fW6HQOCLvjJ1AoP9fCVzDJ_D0JkLzc7jof87MWM02DndVdP66SuGj2bGhqSzZosyHG8te4IpFEhGXmEP7qJeRoyEYcSL-zj-642d92vZHJQcSTFgYkp2zhTF2eOy_KdJ3qrKoPNdnFugbZZs5Kb71fCUw4UB7_XyYIYA8nvWKrlg2jKY7WqDAuwAnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ به آکسیوس: همه آن‌ها آنجا هستند. یک گلوله [و می‌توانیم همه آن‌ها را از بین ببریم]، اما ما این کار را نخواهیم کرد، زیرا در آن صورت، هیچ‌کس برای مذاکره با ما نخواهد ماند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/134950" target="_blank">📅 20:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134949">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❗️
❗️
حمید ابراهیمی خبرنگار ورزش سه :
🔴
ماجرای خیلی ساده است! عضو هیات مدیره با بازیکنای مازاد بسته تا قراردادشون تمدید بشه و به کمک سخنگوی سکه ای مدیرعامل رو زمین بزنن و با دور کردن سرمربی مدنظر انتخاب خودشون رو داشته باشن و در نهایت مدیرعامل بشن!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/134949" target="_blank">📅 20:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134948">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
دیگه همه گزینه شدن باید ببینیم کی مربی پرسپولیس میشه ....
❌
مازیار
❌
یحیی
❌
تارتار
❌
مطهری
❗️
مجتبی حسینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/134948" target="_blank">📅 20:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134947">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❗️
باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/134947" target="_blank">📅 19:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134946">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
#فارس ؛ مهدی تارتار در یک قدمی نیمکت پرسپولیس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/134946" target="_blank">📅 17:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134945">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNN2kM4vy19A4Qd0vDfPa1RGR_PyJzUCO7CAkLOa3u_N2RQDST-Mk7jVSbB8RM9-mXAFuN2YERmXcZfoMQ1LaJiLIqXbi0UQjoxIbCcpCHg6ti1eYc0Sg2mAJMGJgUTqRDrCvWQl-V-SamGKmubAGzB9EuEL5JuthATYYuvS_3F1TSNVumregSekt8hSZson8awCQSjUMTLpI-H2psdme2nxSHTzq1h3ifLQR0eyU3GJ9RRxNxq-2g_PVX4xt0bUANEVLwitkHYDGxxuklv_3jnA59t2peh38FaqeKiYHwoibsa7FgLznzuEktWUrnMSqfGNDeldTUd7usr4QdRepg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فووووری از فوتبالی: باشگاه پرسپولیس به دنبال عقد قرارداد با فاتح تریم است، سرمربی ترک تبار 2 میلیون دلار درخواست کرده است اما مدیران باشگاه پرسپولیس بیشتر از 1,5 میلیون دلار نمیدهند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/134945" target="_blank">📅 16:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134944">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❗️
دیگه همه گزینه شدن باید ببینیم کی مربی پرسپولیس میشه ....
❌
مازیار
❌
یحیی
❌
تارتار
❌
مطهری
❗️
مجتبی حسینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/134944" target="_blank">📅 16:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134943">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
#فارس ؛ مهدی تارتار در یک قدمی نیمکت پرسپولیس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/134943" target="_blank">📅 16:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134942">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🏅
تفکرات علی پروینی به پرسپولیس نزدیک شدند
💥
بازگشت به روز های سیاه دهه هشتاد؟
⚠️
بعد از منتفی شدن بازگشت یحیی گل‌محمدی و در شرایطی که اختلاف مالی میان دراگان اسکوچیچ و باشگاه پرسپولیس همچنان زیاد است، برخی گزینه‌های داخلی با کمک جریان‌های رسانه‌ای در تلاش…</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/134942" target="_blank">📅 16:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134941">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🏅
تفکرات علی پروینی به پرسپولیس نزدیک شدند
💥
بازگشت به روز های سیاه دهه هشتاد؟
⚠️
بعد از منتفی شدن بازگشت یحیی گل‌محمدی و در شرایطی که اختلاف مالی میان دراگان اسکوچیچ و باشگاه پرسپولیس همچنان زیاد است، برخی گزینه‌های داخلی با کمک جریان‌های رسانه‌ای در تلاش هستند خود را به نیمکت پرسپولیس نزدیک کنند.
⚠️
یکی از این نام‌ها، مهدی تارتار است؛ مربی‌ای که با وجود حضور در گل‌گهر و برخورداری از امکانات یک باشگاه صنعتی، نه جامی کسب کرده و نه افتخاری فراتر از رتبه‌های پنجم در کارنامه دارد. او حتی اخیرا هم در رقابت برای سهمیه آسیایی هم ناکام ماند و شکست سنگین پنج بر صفر در خانه مقابل چادرملو هنوز از یادها نرفته است.
⚠️
سؤال اینجاست؛ آیا نیمکت پرسپولیس آن‌قدر کوچک شده که مربی‌ای بدون حتی یک جام و با این کارنامه، صرفاً با فشار رسانه‌ای، گزینه هدایت بزرگ‌ترین باشگاه ایران شود؟ پرسپولیس به مربی‌ای صاحب‌سبک، جسور، اهل جوان‌گرایی و قهرمان نیاز دارد، نه گزینه‌ای که مهم‌ترین رزومه‌اش حمایت رسانه‌ای باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/134941" target="_blank">📅 16:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134940">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❗️
دیگه همه گزینه شدن باید ببینیم کی مربی پرسپولیس میشه ....
❌
مازیار
❌
یحیی
❌
تارتار
❌
مطهری
❗️
مجتبی حسینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/134940" target="_blank">📅 15:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134939">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
✅
فووووووووووووری
✅
✅
ورزش سه: پرسپولیس با حمید مطهری و مازیار زارع وارد مذاکره شد
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/134939" target="_blank">📅 15:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134938">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✅
✅
شنیده ها: با وساطت سید جلال حسینی، مدیران باشگاه پرسپولیس امروز با مازیار زارع سرمربی ملوان بندر انزلی وارد مذاکره شدند و جلسه ای با این مربی برگزار کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/134938" target="_blank">📅 15:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134937">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✅
باشگاه پرسپولیس: مذاکرات با گزینه سرمربیگری در چارچوب منافع باشگاه دنبال می‌شود ‌
🔴
سخنگوی باشگاه پرسپولیس تأکید کرد تصمیم نهایی درباره انتخاب سرمربی فصل آینده بر اساس جمع‌بندی فنی، اقتصادی و مدیریتی اتخاذ خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/134937" target="_blank">📅 15:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134936">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✅
✅
شنیده ها: با وساطت سید جلال حسینی، مدیران باشگاه پرسپولیس امروز با مازیار زارع سرمربی ملوان بندر انزلی وارد مذاکره شدند و جلسه ای با این مربی برگزار کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/134936" target="_blank">📅 15:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134935">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✅
✅
شنیده ها: با وساطت سید جلال حسینی، مدیران باشگاه پرسپولیس امروز با مازیار زارع سرمربی ملوان بندر انزلی وارد مذاکره شدند و جلسه ای با این مربی برگزار کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/134935" target="_blank">📅 15:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134934">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❗️
❗️
شنیده ها: باشگاه داره با یک مربی فرانسوی صحبت میکنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/134934" target="_blank">📅 15:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134933">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/134933" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/134933" target="_blank">📅 14:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134932">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mDBAG8eNdxiULvpj7_U0SsnES5u9NlcmxJMMWZPpfi4YT0AuL4kBlWeUN65JLNZOUAr5JKyAvZ342FGu8OJs9TfmHT81N2sX7-CJaVvXcb313y7Rer1Yw7I7-5s84WwrjOY5yGK2MvIpi3MZLfc6q3vv_AaEmFDpQaqwLn4b6GyQoVO7Fv4TaD-qTcIjed3lo_lH0wvziM8m9oiN8ZfwfuXNx1poQNPzPB0rAwVlCUc41WVaP_YmGU4QSm7QHMzrTWBhYtbYXVJLsS-REqYsKRxbhinAsOZGDlV59wM-Qfza7bZ7TRtsoxPpNcNuvVt07Hc2OlmP0klq52I9B4b-pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی فوووق جذااااب
کانادا
و
مراکش
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
🆕
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای، مطمئن و در کلاس جهانی پیشبینی کنید!
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/134932" target="_blank">📅 14:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134931">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
ابوالفضل جلالی که قراردادش با استقلال تموم شده، دوست داره به پرسپولیس بره. چون بازیکن آزاده، پرسپولیس شرایط جذبش رو بررسی می‌کنه، اما تصمیم نهایی رو سرمربی جدید تیم می‌گیره.
🔴
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/134931" target="_blank">📅 13:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134930">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
استوری دراگان اسکوچیچ :
🔴
تلاش‌ها برای جلوگیری از بازگشتم و پخش کردن دروغ درباره جدایی‌ام از ایران، مرا تضعیف نکرد؛ بلکه فقط ترس کسانی را که پشت پرده فعالیت می‌کنند آشکار کرد.
🔴
نحوه مدیریت مذاکرات توسط باشگاه، تنها نشان داد که این باشگاه در مذاکرات جدیت…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/134930" target="_blank">📅 13:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134929">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">#نظر_شخصی
🤩
من مقصر این وضعیت رو «فقط بانک» شهر نمیدونم این نظر منه
☑️
ببینید تیم هیچ دغدغه مالی نداره، هیچ بدهی ای نداره، حدادی بالغ بر ۵۰۰ میلیارد درآمدزایی داشته و بانک شهر کاملا ساپورت مالی کرده
📚
از دید من علت نتیجه نگرفتن پرسپولیس چندین علت داره،…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/134929" target="_blank">📅 13:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134928">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
استوری دراگان اسکوچیچ :
🔴
تلاش‌ها برای جلوگیری از بازگشتم و پخش کردن دروغ درباره جدایی‌ام از ایران، مرا تضعیف نکرد؛ بلکه فقط ترس کسانی را که پشت پرده فعالیت می‌کنند آشکار کرد.
🔴
نحوه مدیریت مذاکرات توسط باشگاه، تنها نشان داد که این باشگاه در مذاکرات جدیت…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/134928" target="_blank">📅 13:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134927">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
شنیده ها: پاتریس کارترون گزینه پرسپولیس در صورت عدم توافق نهایی با اسکوچیچ!!!!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/134927" target="_blank">📅 13:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134926">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">#نظر_شخصی
🤩
من مقصر این وضعیت رو «فقط بانک» شهر نمیدونم این نظر منه
☑️
ببینید تیم هیچ دغدغه مالی نداره، هیچ بدهی ای نداره، حدادی بالغ بر ۵۰۰ میلیارد درآمدزایی داشته و بانک شهر کاملا ساپورت مالی کرده
📚
از دید من علت نتیجه نگرفتن پرسپولیس چندین علت داره،…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/134926" target="_blank">📅 13:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134925">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5fH9bE-jMLyip4_zzwDOdnKVAwrNThT3bRAxTjfbLCeNykpLArMbMMpr2AbrmD-Y4yQQM_U5pEpxtF-al58FY7SylkRBCNvGzVG7HR5lDHYeYKK0qgMzq5O0iliVXXtEcS-5ACUXvHoVgOAJT4tuG2pNUjbSHM1d8HTbV4Uutf-sthOan9k8atIFn9HYqryBCVdIs8IdeOBnLYq6ejvs6a0_-JFtTbSbhKsfxpvUk38lnL8i8c8ltXFsAHHmPNy8dptB0TOfTcMnv-IF89l3sp3l-oKUFMfMuieoHi3iFW9A6yrhJ2oeSBVlJ9MZ6bmfUrybM5Yo6mHc9kTy5xVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جام جهانی جای عجیبیه!
🔴
🔴
توی یک شب میتونی راه ۱۰۰ساله رو طی کنی و این معمولا برای دروازه بان ها میوفته
🔴
🔴
مثلا همین ووزینیا دروازه‌بان ۴۰ساله کیپ ورد که تا ۲۵سالگی زباله بازیافتی جمع آوری میکرده اما با یک شب درخشش شگفت انگیز از ۵۰ هزار فالوئر به نزدیک ۱۵میلیون…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/134925" target="_blank">📅 12:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134924">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
❌
ابوالفضل جلالی که قراردادش با استقلال تموم شده، دوست داره به پرسپولیس بره. چون بازیکن آزاده، پرسپولیس شرایط جذبش رو بررسی می‌کنه، اما تصمیم نهایی رو سرمربی جدید تیم می‌گیره.
🔴
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/134924" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134923">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❗️
خداداد عزیزی: پلن B پیشنهادی ما به پرسپولیس یحیی گل‌محمدی بود، با یحیی حرف زدم در قراردادش بند فسخ وجود دارد که از دهوک جدا شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/134923" target="_blank">📅 12:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134922">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❗️
برنامه بازی‌های امشب مرحله یک هشتم نهایی که برای اولین‌بار ساعت‌هاش مثل آدمی زاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/134922" target="_blank">📅 12:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134921">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
سفیر آمریکا در سازمان ملل: صبر ترامپ نسبت به ایران در حال تمام شدن است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/134921" target="_blank">📅 12:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134920">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GllKUuFZ0JS2hYf4HHOPA5RNImmjSI1kTevF50LKOYvqy88SYdlv416zPKKqO2CxhxZN-dabtMFcgB70ZiLdBuGN0PLDH7RVTlVbqB1mS9stxtikIDRPtwFwbhkxwXs-KhQMyWe8Qka45F_taeKVfYE6_fMuOPnL4GtDthmmGiiYLD25OK4rbvboiI2dfm43O16S8bu0YWTpCW0U6wCSCozOV-IqEyZvfUmK7ows1wwh0Wknms1TxBo2Bh7KZGcWxdCSqmZnbi4aW0PsffV_XAjJo_cEtZQcl_ezbt3LHWZEFZ_Nnz0Ewa07-rNlQh32TBKAKiNVBrV7TSwQJ6Qo-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتایج بازی های بامداد امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/134920" target="_blank">📅 12:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134919">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fb54955fa.mp4?token=rIS_t0y60a6GUV3HmT7I8TjSNUAzHEzciulmYU8UtVNJV45URS-EnENH4rNERkHjRGvyz0Jvcnpv_Wou5ZTkGkOW1D-654m0SRKpIOeG9K3jA_tqbMuVzG04JbeqMj7MIVF3ACDhJw6fXaW8b_w85cigXYGVKeXsD-VSVdBrnGreJMETdq_j4YSE9Myzhxhj0DyXl8l0_Ty-zosy_XPa0v_-ArFsoEtPM-7z_339xRj6G0SqLNKIxYAfdwFM9-_gnqq0wEK9fD2ZkDQxSewkGKGl8Of50xKAao2kKjtJ3ZIYq2KECYKPTPkqgFXXVp0japEqHIHsLpAVEx2-BLUXXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fb54955fa.mp4?token=rIS_t0y60a6GUV3HmT7I8TjSNUAzHEzciulmYU8UtVNJV45URS-EnENH4rNERkHjRGvyz0Jvcnpv_Wou5ZTkGkOW1D-654m0SRKpIOeG9K3jA_tqbMuVzG04JbeqMj7MIVF3ACDhJw6fXaW8b_w85cigXYGVKeXsD-VSVdBrnGreJMETdq_j4YSE9Myzhxhj0DyXl8l0_Ty-zosy_XPa0v_-ArFsoEtPM-7z_339xRj6G0SqLNKIxYAfdwFM9-_gnqq0wEK9fD2ZkDQxSewkGKGl8Of50xKAao2kKjtJ3ZIYq2KECYKPTPkqgFXXVp0japEqHIHsLpAVEx2-BLUXXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
از مدیرای بی غیرت خودمون که فعلا خبری نیست پلن B و C و G باشگاه رو از این افغانی پیگیری کنیم انگار زودتر به نتیجه میرسیم !!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/134919" target="_blank">📅 12:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134918">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
شنیده ها : محسن خلیلی دیروز با مهدی تارتار جلسه داشته و این مربی اعلام کرده در قرارداد جدیدش با گل گهر بند فسخی داره که میتونه به پرسپولیس بیاد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/134918" target="_blank">📅 11:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134917">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❗️
❗️
قدوسی : جدی ترین تماسها از بین گزینه های داخلی با مهدی تارتار صورت گرفته و تارتار گفته میتونه از گلگهر جدا بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/134917" target="_blank">📅 11:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134916">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
#فارس‌؛ اسکوچیچ که کلا کنسل شد رفت، پنج تا مربی ایرانی تو گزینه های حدادی ان که یحیی و تارتار از همه پررنگ ترن و احتمالشون بالاست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/134916" target="_blank">📅 11:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134915">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❗️
❗️
تسنیم اعلام کرده گزینه‌های سرمربیگری پرسپولیس یحیی گل‌محمدی، مهدی تارتار و مجتبی حسینی هستن!
🔴
خجالت نکشید! حمید درخشان و بهروز رهبری فرد و پایان رأفت و حمید استیلی رو هم گزینه کنید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/134915" target="_blank">📅 11:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134914">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❗️
🇦🇷
🇨🇻
نانا کواکو بونسام:
🔴
من با نیروهای ماورایی و روح اجدادم مشورت کردم. به مسی فقط اجازه داده شده بود که در این جام جهانی 6 گل بزنه و اون همین حالا سهمیه‌اش رو پر کرده است. ارواح به من نشان دادن که در حساس‌ترین لحظه، مقابل یک تیم غیرمنتظره پنالتی‌اش رو…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/134914" target="_blank">📅 11:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134913">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❗️
❗️
تسنیم اعلام کرده گزینه‌های سرمربیگری پرسپولیس یحیی گل‌محمدی، مهدی تارتار و مجتبی حسینی هستن!
🔴
خجالت نکشید! حمید درخشان و بهروز رهبری فرد و پایان رأفت و حمید استیلی رو هم گزینه کنید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/134913" target="_blank">📅 11:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134912">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
حرف هوادار
✅
اقایون مدیر فکر آوردن امثال یحیی و تارتار و مجتبی حسینی رو به هیچ عنوان نکنید چون هوادار پرسپولیس اون ساختمون رو سرتون خراب میکنه حواستون باشه .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/134912" target="_blank">📅 11:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134911">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✔️
مهدی تارتار
✔️
یحیی گلمحمدی
❗️
پ ن:هردوتا مربی بند فسخ دارن و هیچ مشکلی برای پیوستن به پرسپولیس ندارن (شانس تارتار بیشتره)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/134911" target="_blank">📅 10:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134910">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✅
پرونده حضور اسکوچیچ در پرسپولیس به دلیل اختلاف مالی 1 میلیون دلاری و درخواست بند فسخ در صورت جنگ ، بسته شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/134910" target="_blank">📅 10:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134909">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
✅
ورزش سه: با کنسل شدن اسکوچیچ مدیران باشگاه پرسپولیس به سمت مذاکره با یک گزینه خارجی دیگر خواهند رفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/134909" target="_blank">📅 09:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134907">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
پرونده حضور اسکوچیچ در پرسپولیس به دلیل اختلاف مالی 1 میلیون دلاری و درخواست بند فسخ در صورت جنگ ، بسته شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/134907" target="_blank">📅 09:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134906">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0nsCbmyCOGwlj7-8Khij8HgBTwIbnvwkizCZLXs8uykD7HK1ZjV3Te8-isS2bxNdUy8OJwMGyMgxeCN8KnPWSSYjOfyIjJNsnXebPU04WbZ0rvq9u3ysfNrp6AHsJ38RzTNqPsrqCBYLSM9LKWNUghWKXWj3_Ej0MVMrFYfvMtEykGKptH_kP7AqNzmtZGlCoMtpLjg6CMb4587-E0kVWdWe3ZpsVzAzpJkjC0P7bQI10BbuJ86X75m-VIU2nmiv5JA5KZ84QmlvsAGHZoadCnnXv8z_4fIG61DIGATbDeUbzfjrhr_IdYp8FWrKbiSraP56zcXdpYCw-GPzDSFHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتایج بازی های بامداد امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/134906" target="_blank">📅 09:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134905">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❗️
خداداد عزیزی: پلن B پیشنهادی ما به پرسپولیس یحیی گل‌محمدی بود، با یحیی حرف زدم در قراردادش بند فسخ وجود دارد که از دهوک جدا شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/134905" target="_blank">📅 09:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134904">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ii33FRg1KUiKp1qYk3gSLERoisV3sjBK9WOUMiv-w4hXfi65K8ziXt5EmIcMvWDpIXPNoUGINRl3LFzGnDb3BfogQMOne5b48anISwXpiDCOOkak16n7QRhpaO87jCIoVQPQSrwYv-25Q6i3vfeUbG4jp-GILOsKCxHfSg03ShIuEhLrEFg9Ne41rlDYyvGtOELaBkv1xMsqnOR4KHLrRbehEbVjYX37vzWAv_gO2f5Pxrd0Hn-MKk5RlolSR0X1ePVVMrJkjYa9TgOYJAUL9qvptGiQzONjGFsrcdBpIGVRHL-hRQWZfiAiBxCznmk2bsuflSLOVzXqx3S5vfaO8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
مصلی تهران؛ هم‌اکنون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/134904" target="_blank">📅 09:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134903">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/134903" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر پنجشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://t.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/134903" target="_blank">📅 01:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134902">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pr2x4_3FVJiVbVbpQ5sRhVO-0RSzPJjE63w0Hu2i-cHwXidicR6HsY28Xs0KOB7cflTO-tliEfUu7F72upYa5Ugqn5eYp_VWy8UHgCzev_n0oT6v69J-7rfVFYS0AyCHxVH6MUBeYuCbgb_8hrlXz4_QROzO9lVMderFHFzx1j-3dqZ-tlyxlf5IMmXiJNrQ8hPLV5w6od3a58e5ICgb-x17gw0_L2vB2oE7yYa97MBt2j83kBeMr8Zm4DR71_n7KOLUmJxP80IHB5shraWRqQyoxEgIbfpayv2uX2NuR_pNR4EKeQhSY0iKF9TRsw5jqoyU2lk5sYEayeNv5s811w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین سایت جهانی برای کاربران ایران با واریز برداشت مستقیم
⬇️
🪙
سایت بین المللی و معتبر لاین
بت
❤️‍🔥
اسپانسر لیگ  فرانسه
💳
واریز و برداشت ریالی
👀
بازگشت باخت ب صورت هفتگی
📣
دارای پشتیبانی فارسی فعال
🎁
بونوس
💯
روز های دوشنبه
🎡
کدهدیه ثبت نام
➡️
L5670
🔗
《 لینک سایت برای کاربران ایرانی》
👍
《 دانلود اپلیکیشن اندروید》
❤️
https://t.me/+dukgrB6-zGsyNGM8
🔻
جهت استفاده از وبسایت از آی پی کشورهای آسیایی
🇷🇺
یا کانادا
🇨🇦
، استفاده کنید
🅰
✔️
آموزش کامل و جامع شرطبندی
👉</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/134902" target="_blank">📅 01:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134900">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">#نظر_شخصی
🤩
من مقصر این وضعیت رو «فقط بانک» شهر نمیدونم این نظر منه
☑️
ببینید تیم هیچ دغدغه مالی نداره، هیچ بدهی ای نداره، حدادی بالغ بر ۵۰۰ میلیارد درآمدزایی داشته و بانک شهر کاملا ساپورت مالی کرده
📚
از دید من علت نتیجه نگرفتن پرسپولیس چندین علت داره، ۱- دخالت بانک شهر تو امور نقل و انتقالات ۲- ناکار آمدی و فساد مدیران قبلی در فصل آخر کاری شون۳- تغییرات پی در پی سرمربی۴- نقل و انتقالات شلخته و بالانس نبودن تیم در دو فصل اخیر ۵-یک دل نبودن هوادار و جامعه هواداری ۶- فساد مدیران میانی و انفعال هئیت مدیره و سنگ اندازی هاشون که چشم طمع صندلی مدیرعاملی دارن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/134900" target="_blank">📅 01:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134899">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🫦
جدی فضای خیلی عجیب غریبی شده، قبلا ۲۰ تا مثلا کانال پرسپولیسی بود الان ۱۰۰ تا همه هم ماشالله ادعا دارن مطلع هستن
😅
🫦
هرکسی هم یه نسخه ای برای هوادار میپیچه یکی میگه باند عالیشا داره تیمو میگاد یکی میگه دست هاش پشت پرده یکی میگه خلیلی، یه زمانی میگفتن خانبان…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/134899" target="_blank">📅 01:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134898">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🫦
جدی فضای خیلی عجیب غریبی شده، قبلا ۲۰ تا مثلا کانال پرسپولیسی بود الان ۱۰۰ تا همه هم ماشالله ادعا دارن مطلع هستن
😅
🫦
هرکسی هم یه نسخه ای برای هوادار میپیچه یکی میگه باند عالیشا داره تیمو میگاد یکی میگه دست هاش پشت پرده یکی میگه خلیلی، یه زمانی میگفتن خانبان
🫦
به من ثابت شد اینا همش مشکلات شخصی این پیج ها و کسایی که بهشون خط میده با اون فرده، وگرنه تو این دو سال کلی تغییرات انجام شده ولی روند موقعیت متوقف شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/134898" target="_blank">📅 01:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134895">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
هرکسی رو میخاید بیارید بیارید یحیی نباشه…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/134895" target="_blank">📅 01:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134894">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b80ddf04f1.webm?token=V2TB_w9IX2HJXxrjAo19SPixR5KzqEovTWwdGxwyuMOKGSG4sQPtvpgZMPAPk2F5Vk4gmNrCv1m49Ok_o1BoUsyPGLxzIGhAQIn7lL2fAox2fRKuVydxzVBYnFTM-B3qyGFw4omLcOv1LUw0YZLk8sE2RKZxDjTQ-agJ9NEO2vWME96w9o4GxLwmOR75nlSr6yCeJ9huOMughfUD_vP_BHL-458fmSR_4hKhccIm9968kBJNUkcurmX4d5xTM-eoNGRoyVSn4ZlMP8325XQLXwBmLLLQZHIXWeXzWVOa0jwybnFkeqa2CbFiY4ik-Xj6eQQo0ZOXn4kqFAt_pc3LJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b80ddf04f1.webm?token=V2TB_w9IX2HJXxrjAo19SPixR5KzqEovTWwdGxwyuMOKGSG4sQPtvpgZMPAPk2F5Vk4gmNrCv1m49Ok_o1BoUsyPGLxzIGhAQIn7lL2fAox2fRKuVydxzVBYnFTM-B3qyGFw4omLcOv1LUw0YZLk8sE2RKZxDjTQ-agJ9NEO2vWME96w9o4GxLwmOR75nlSr6yCeJ9huOMughfUD_vP_BHL-458fmSR_4hKhccIm9968kBJNUkcurmX4d5xTM-eoNGRoyVSn4ZlMP8325XQLXwBmLLLQZHIXWeXzWVOa0jwybnFkeqa2CbFiY4ik-Xj6eQQo0ZOXn4kqFAt_pc3LJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/134894" target="_blank">📅 01:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134893">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">💬
چه همزمان فیض بخش و خداداد عزیزی اعلام کردن اسکوچیچ کنسله
🤝
😵‍💫
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/134893" target="_blank">📅 01:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134892">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0fb9d756f.mp4?token=PtweJaHAGC67sDEDY-52FAAySgjG8pu-k84pQ8nE_GrQoMrhX-FX4FQvpZ_9ibE2iRPqxvvRaYVyuYP18oTcHbqeQ9HhApC65Finfc-zVwCAN3lH-MS_vCyzh6hdDn7KtyI3TSIGEAU3d0e9HoN0qmK5ruXQgDKjZ3f0yVIEjlM6zagsZHMrdNYf03FAE476QRTxslDtqPw-5yR4DUHrtxt4RPPRwsrfdl2kbjmWazh70cIauPjCwE5gg-nVAE0EnwfYTNQVF5YMIoLX6l4SKS3MB6DLM3tEUmHyJIdd2N2yjsL4NCveq0JTv1WyoBy0xZ_nu_TfmCUiuPPYK8JSZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0fb9d756f.mp4?token=PtweJaHAGC67sDEDY-52FAAySgjG8pu-k84pQ8nE_GrQoMrhX-FX4FQvpZ_9ibE2iRPqxvvRaYVyuYP18oTcHbqeQ9HhApC65Finfc-zVwCAN3lH-MS_vCyzh6hdDn7KtyI3TSIGEAU3d0e9HoN0qmK5ruXQgDKjZ3f0yVIEjlM6zagsZHMrdNYf03FAE476QRTxslDtqPw-5yR4DUHrtxt4RPPRwsrfdl2kbjmWazh70cIauPjCwE5gg-nVAE0EnwfYTNQVF5YMIoLX6l4SKS3MB6DLM3tEUmHyJIdd2N2yjsL4NCveq0JTv1WyoBy0xZ_nu_TfmCUiuPPYK8JSZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
خداداد عزیزی: پلن B پیشنهادی ما به پرسپولیس یحیی گل‌محمدی بود
، با یحیی حرف زدم در قراردادش بند فسخ وجود دارد که از دهوک جدا شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/134892" target="_blank">📅 01:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134891">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1c6fb008f.mp4?token=dnan_sHtA2KmbbL3JtAua6sRLEFaHNRNu4p3v6NDi9pj2Xf5t6jETptIS7VHVYfCiELHXQDoWZkunSzvaqTf_JO1O97Ok6ne53czfiEWmZPCdXLcW-HVO3DpT7LCYfTbBvMUh61FbI-f6MBo8ZhcS_i6XPvt4MzFq1ez70HxG1o4MlBshmDbXYBuQa0rr89n9WCPaye1OO20PnYdcIuQ5LceHoJNgRFXrpVO6Ip3IzqNe35g86blXkNLLE-YfZNWUV6zyrkLReCx0ubLKRhxTgLhnndzPlyoRkHAR6hwVjj34FWzBaRtt8pfVQPzUlOvuqkTEPStIvHomOLj_S7lYISf-kkmXxvYsIm4Iv7tcbuYTN-5JQmBfiHyVfgSqeqHpyeaH-5tUvr7jRlLotpYYcVbw1_cWVHki6u0fH0oPdrsJh38-0BmecpU0cF8c_X5lLN5k8aWT3N2p769f49AuvRH6QcPuXwQBJ0E4WYKLsekCr2rdYABnxzrGaMdRGyLxPj1p2Q3F5CPjpKQnKCUQ4m5IGYn_CTEgo7L1Rxh6LZPd2lWDp5N9sQnDcSqLwJRdMRGphenNhUAHKbnUeHgwJ4fjd8ZHoxg63hSXMeceQFmylr22VAqcP_fs0_kKnFJd1VC7DTvguRSxHMZOIUBrjA1-K7oNgMkTRcQkVMlb60" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1c6fb008f.mp4?token=dnan_sHtA2KmbbL3JtAua6sRLEFaHNRNu4p3v6NDi9pj2Xf5t6jETptIS7VHVYfCiELHXQDoWZkunSzvaqTf_JO1O97Ok6ne53czfiEWmZPCdXLcW-HVO3DpT7LCYfTbBvMUh61FbI-f6MBo8ZhcS_i6XPvt4MzFq1ez70HxG1o4MlBshmDbXYBuQa0rr89n9WCPaye1OO20PnYdcIuQ5LceHoJNgRFXrpVO6Ip3IzqNe35g86blXkNLLE-YfZNWUV6zyrkLReCx0ubLKRhxTgLhnndzPlyoRkHAR6hwVjj34FWzBaRtt8pfVQPzUlOvuqkTEPStIvHomOLj_S7lYISf-kkmXxvYsIm4Iv7tcbuYTN-5JQmBfiHyVfgSqeqHpyeaH-5tUvr7jRlLotpYYcVbw1_cWVHki6u0fH0oPdrsJh38-0BmecpU0cF8c_X5lLN5k8aWT3N2p769f49AuvRH6QcPuXwQBJ0E4WYKLsekCr2rdYABnxzrGaMdRGyLxPj1p2Q3F5CPjpKQnKCUQ4m5IGYn_CTEgo7L1Rxh6LZPd2lWDp5N9sQnDcSqLwJRdMRGphenNhUAHKbnUeHgwJ4fjd8ZHoxg63hSXMeceQFmylr22VAqcP_fs0_kKnFJd1VC7DTvguRSxHMZOIUBrjA1-K7oNgMkTRcQkVMlb60" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خداداد عزیزی : پرونده حضور اسکوچیچ در پرسپولیس بسته شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/134891" target="_blank">📅 01:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134890">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
با اعلام ایجنت اسکوچیچ حضور این مربی در پرسپولیس منتفی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/134890" target="_blank">📅 01:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134889">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
آقای حدادی .بانک شهر پاسخ گو باشید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/134889" target="_blank">📅 01:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134887">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUCGpT6KrpOP-hi23hWBKSmMpCF5z6lTDeJ1K7l9BO8pIrcERdF9v_7801JHmwZJVXLa9PrGM6pXfGpmyhb1alMXavkryvb5e5QiLgHL-hxRzPD8E9eCyRIk04z26146RjsVyUzD97TyBBu2_gLQxenqA47B8ZgJ7UdDqUBF5UH4wL5ugomly3XbhaOR6NPMAfUScmUblOKsTDVJP5tTd7Uz6S_EKk1q0m7_gqu5HY49flXJqCFyabsSpJP8XQOnkEmdHHaBwBXpmXthwHo1F_7jfUSZUJvtaJXHBrIQ_KXmyfkBsw18Oz0OJouWHByZrlKd7k8lDz7rGEl8t2ICQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
با اعلام ایجنت اسکوچیچ حضور این مربی در پرسپولیس منتفی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/134887" target="_blank">📅 01:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134885">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✅
✅
گویا همه مسیر ها داره مسدود میشه.یکی از نزدیکان و افراد ایرانی نزدیک به اسکوچیچ، بهم گفت؛ بعیده این انتقال صورت بگیره.
🔴
البته باید منتظر واکنش رسمی باشگاه موند . چون اعلام کردند ظرف چند روز آینده ، همه چیز مشخص میشه//طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/134885" target="_blank">📅 01:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134884">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❗️
❗️
امیررضا رفیعی طی روزای اخیر به مدیریت باشگاه گفته میخوام جدا بشم و به زودی این اتفاق رخ میده / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/134884" target="_blank">📅 01:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134883">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLwXnms0a1iDlqBjW20kre0XCCf6NY_guDGoDPcBXy6RRqV1G0I6HBdSWmNH7jCIvjwzqgvVgAhK4IY0uowQ434VBHmib9HEcFkGFlRYxePmpvDR-CRGrVarLC2wDYW0mB0vfwU18iFbUoGivEIn4RnSh52YMTf-7VHzJzMLKJk7OwfuTZxT4NZCb_gspGopwPE3loTkJ5el-3OY-6On8qEQ9TqsQtfm1KY9FHkWohvEbgfAIUgMvLFa3wFgslKxGPJUlw96v2Ad7c28BiYK9bXRotYbYtGMtECmXFG7mC3hrXipuWl6NpRn-6GU0oCJUUsk6sdl-RNX-wOcog6D_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
تیمای آسیایی تو جام جهانی
:
😆
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/134883" target="_blank">📅 01:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134882">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
❌
بازی های امشب
🇦🇺
استرالیا_مصر
🇪🇬
🔸
ساعت 21:30
🇦🇷
آرژانتین_کیپ ورد
🇨🇻
🔸
ساعت 01:30
🇨🇴
کلمبیا_غنا
🇬🇭
🔸
ساعت 05:00
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/134882" target="_blank">📅 00:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134880">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❗️
🇦🇷
🇨🇻
نانا کواکو بونسام:
🔴
من با نیروهای ماورایی و روح اجدادم مشورت کردم. به مسی فقط اجازه داده شده بود که در این جام جهانی 6 گل بزنه و اون همین حالا سهمیه‌اش رو پر کرده است. ارواح به من نشان دادن که در حساس‌ترین لحظه، مقابل یک تیم غیرمنتظره پنالتی‌اش رو…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/134880" target="_blank">📅 00:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134879">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❌
❌
بازم تاکید میکنم اسکوچیچ مربی پرسپولیس در لیگ ۲۶ خواهد بود
🎙
طاهرخانی  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/134879" target="_blank">📅 00:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134878">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✔️
#تایید_خبراختصاصی
⚽️
🤩
رسمی؛اوسمار ویرا از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/134878" target="_blank">📅 00:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134877">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZILAKIPUU4d84a7WRUZ5KDRnSct8w90nhPZR9dRmKqTjM8WVWt5pjaob768CuVEpsIOcGXoTWLu2lXeUfvaxKMPuxXVzqQkWGeV5TEkmlDGFraEnwIvXGYeFk9Gkdvhi7ueslXqMAcejQ-jFc1U3BDMizn4WzKNTzsKggQr2dbaV1h6wpWpyumtCl3dV7yEn1EeUSX0-bSgBjNykghkMmorIazNM5TrnGdO89h1-9nqd-1PXKZ827Q4Y7czDHeR_3FDHtdAhIwAuphbKz90-xINCP_h8D9XHwCIPyqPnsPqV9dLLply9NDyZW7pD74vkS5Qm50lQhh4bqYg27zdaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اخرین نماینده اسیا هم حذف شد.
🇪🇬
مصر 1 (4)
🇦🇺
استرالیا 1 (2)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/134877" target="_blank">📅 00:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134876">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✅
✅
ادعای رسول خطیبی:
🔴
زنوزی مالک باشگاه تراکتور بچه بازه و همجنسگراست!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/134876" target="_blank">📅 23:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134875">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
پرسپولیس حاضره تا ۲ برابر سقف قراردادش به احمد نوراللهی پیشنهاد بده/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/134875" target="_blank">📅 23:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134874">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9537d57a20.mp4?token=iBgst_v_RB6h0UMIPaIyuc0wfEKUFGNxjso3tT-eHvqIYVn9Io0-7voA4QiI2GxZTo_IQX0mVDhp8_LALKqB2fVlsVrcaNTlKfNSoN3S1Do8-9yOQkha2epHmLtBxWYI4Amq9KSO6-rp9QTxZ3lNrItUg3KKjcCifzJL4ntzNn9HXANIe3nSpAgUmC5N-sI_ItZ0K-HxIYimmXY70-p2SINrvgwXuVVQENqZX3kZBztb11e4wFy12nEXBiER947uGsXwn9r--bBLQxEbxoN2f1VcDwEnkJEzqoyVYx1aQoV1xSgOtU44FU1b00D0mhrPJVcWyVhLr2fZYgf0crLjtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9537d57a20.mp4?token=iBgst_v_RB6h0UMIPaIyuc0wfEKUFGNxjso3tT-eHvqIYVn9Io0-7voA4QiI2GxZTo_IQX0mVDhp8_LALKqB2fVlsVrcaNTlKfNSoN3S1Do8-9yOQkha2epHmLtBxWYI4Amq9KSO6-rp9QTxZ3lNrItUg3KKjcCifzJL4ntzNn9HXANIe3nSpAgUmC5N-sI_ItZ0K-HxIYimmXY70-p2SINrvgwXuVVQENqZX3kZBztb11e4wFy12nEXBiER947uGsXwn9r--bBLQxEbxoN2f1VcDwEnkJEzqoyVYx1aQoV1xSgOtU44FU1b00D0mhrPJVcWyVhLr2fZYgf0crLjtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
😐
میثاقی امشب به سیم آخر زد و شماره موبایل اصلی خودش رو به صورت کامل روی آنتن زنده اعلام کرد تا مردم بهش پیامک بزنن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/134874" target="_blank">📅 23:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134873">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
اسکوچیچ برای خودش ۱۸۵۰ میخواهد به اضافه ۲۰٪ آپشن. همچنین برای دستیاراش ۴۰۰ تا میخواهد و گفته مالیات خودم و دستیارانم را باید باشگاه پرداخت کند
🚩
مجموع این ارقام ۳ میلیون دلار میشود.
✅
✅
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/134873" target="_blank">📅 22:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134872">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
پرسپولیس و اسکوچیچ به توافق رسیده اند و تنها بر سر مبلغ قرارداد اختلاف دارند.
🗣
🗣
سایر موانع و مشکلات جذب این مربی کروات، حل شده است. باشگاه از اسکوچیچ تخفیف می خواهد و او تخفیف هم داده است، اما باشگاه باز هم می گوید باید از قرارداد کاسته شود.
🔻
🔻
مسئولان…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/134872" target="_blank">📅 22:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134871">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
✔️
مدیران پرسپولیس پروژه فسخ بازیکنان را کلید زدند
❌
از عملکرد امید عالیشاه اصلا راضی نبودند ؛ ومرتضی پورعلی‌ گنجی، میلاد سرلک ، رضا شکاری ، تیوی بیفوما و  دنیل گرا  بازیکنانی هستند که نامشان در لیست سیاه باشگاه دیده می‌شود. مدیران پرسپولیس چند گزینه جوان…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/134871" target="_blank">📅 22:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134870">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">#تکمیلی
🔴
💥
یحیی گل محمدی به محسن خلیلی گفته من تا شنبه میتونم صبر کنم از یکشنبه اگر منو بخایید باید ۳۰۰ هزار دلار به دهوک عراق پول بدید رضایت نامه منو بگیرید.
🫦
قابل توجه اون کصخول هایی که میگن نه یحیی نمیاد تیم داره با اسم امپرور بازی نکنید  #نه_به_مربی_ایرانی…</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/134870" target="_blank">📅 22:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134869">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پرسپولیس 48 ساعت برای اسکوچیچ صبر میکنه، اگه پیش نویس قرارداد رو امضا کرد که هیچی کار تمومه، اگه امضا نکرد میرن سراغ گزینه بعدی / آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/134869" target="_blank">📅 21:45 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
