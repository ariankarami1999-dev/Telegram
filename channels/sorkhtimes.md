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
<img src="https://cdn4.telesco.pe/file/D5_qugTFleMna3HFw6D_2CgoKA92kAeUpXf2mkGydU7E85J7NUrkQiNkyq8SqsFu1aIxX7cA8jVjwkE6OUIiTFXgMacGP2_aZiXL2t8AQvhUp_YyYq3U-zvdCB11M-jFSjpoc6tUIhsWrIk9qvlIZwfZtdUEQQgqVIlKUnbPL7VMMvj9lmy8SwCljnQ_kYWIzva6kcCXuz1NMy6_Ur_IUFVnHy5Bu6h1OQnZY2lZ34SjLmadegXz3sNaN338Hz3_yZzxCZZ1U-dhIrRqlX5VDwpgt3F2zJXO3blsT-lZ4-rnqfieXO-p18pyQQ2bWz9t4_P-7VO01zjLWCGSrIGK_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 03:32:20</div>
<hr>

<div class="tg-post" id="msg-134571">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmV-Gliy59pszj9rj2F9mvfsLOnyhBTCoYc9e6cRXlBGr_1FiplAk6TWgoFD-DdP2G2sQGKWXIujtagngJnRJqwPrhKokpi4G9F8Z1_h-GsCjBAovV6W7SUfkEA6AddAX1JxZvNDyLrHJf4Ihpne72u5iECdxVh3k3Sv-uyh80jXWcVQheQpJlNIjRq3eXHHTVMQzibb-9Yrl2CK4zGwOT0uypUFiQpWVTxaVKho6Zh1GHbtN_e41z8A67CUMAdZUlOyOSsI4QcLuyY0tkUkXoTRuGtLeQUFBpNE_s7HSfmuOldfWxs8rFVlYwMKvjWVAizuJHYkKcqkFcg_QAaf2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت رو از دست نده، همین الان وارد سایت شو و گردونه رو بچرخون!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/SorkhTimes/134571" target="_blank">📅 01:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134569">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">#فوری
⁉️
👎
خبر منتشر شده مبنی بر مذاکره حسین خبیری با بانک شهر کذب است،و نقل قول منتسب به خبیری صحت نداره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SorkhTimes/134569" target="_blank">📅 00:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134568">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
🔴
فرشید حقیری: مدیران باشگاه قرارداد رو برای اسکوچیچ ارسال کردن…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SorkhTimes/134568" target="_blank">📅 00:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134567">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
✅
حدادی  : خداداد عزیزی و خلیلی گزینه های سرپرستی تیمن  / هیچ فشاری از بانک شهر برای اومدن خداداد نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/SorkhTimes/134567" target="_blank">📅 00:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134566">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
🏆
برنامه کامل بازی‌های ۱/۱۶ نهایی جام جهانی
🇿🇦
آفریقا جنوبی - کانادا
🇨🇦
🇧🇷
برزیل - ژاپن
🇯🇵
🇳🇱
هلند - مراکش
🇲🇦
🇺🇸
آمریکا - بوسنی
🇧🇦
🇳🇴
نروژ - ساحل عاج
🇮🇪
🇫🇷
فرانسه - سوئد
🇸🇪
🇩🇪
آلمان - پاراگوئه
🇵🇾
🇲🇽
مکزیک - اکوادور
🇪🇨
🇧🇪
بلژیک - سنگال
🇸🇳
🇪🇸
اسپانیا - اتریش…</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SorkhTimes/134566" target="_blank">📅 00:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134565">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❗️
پنجره کیسه بسته است بابت بدهی خارجی .ولی اونوقت مجوز حرفه ای گرفتن.عجب داره واقعا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/134565" target="_blank">📅 23:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134564">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
⚽️
پیمان حدادی مدیرعامل باشگاه پرسپولیس در گفت و گو با نزدیکانش خبر استعفای خود از مدیرعاملی پرسپولیس را شایعه دانسته و تکذیب کرده است  بازگشا سخنگوی باشگاه هم در گفت و گویی که داشتیم استعفای حدادی را شایعه دانست و تکذیب کرد/قرمزآنلاین
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SorkhTimes/134564" target="_blank">📅 23:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134563">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❗️
دانشخر به سوراختور پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/134563" target="_blank">📅 23:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134562">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaDNOe5hWWDLYGl28EBahpuyKr6VNXXfXk-dc9fdEeKLxEQ_N9Mn0-VANwqyJh5ynzbhdZWw9KCWE9ojc1OkGf14mToCJHebBsnBT_Xd0NSBcIQi_kyyD3EvJ3RxO4enUalS-HsVdDGnzlB8TmMm5MXZ8Os32RQMqUdpvvyKleyj2GKLoLcRT4dnKabddKjVwJRkzHpwMNSg7ug0sfBg7C4K8WZOxYT0Irzn-ZHm32L8574l4A3WHcXrJU2gkB9nKRNrKwt3JB3sRzuOQw9XNH6JG38Jy28DCWPdrEuKV916N_cnb9rG5PcF3G_9RLT6gMLRSs6McR-MTsEGNEoZWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚩
فقط ۴۰ روز تا آغاز لیگ برتر خلیج‌فارس باقی مانده...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/134562" target="_blank">📅 23:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134561">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59577ce95d.mp4?token=FaNs5NGMYM36s6HPR2tAJ7Tp9mmiRFU7ItB2tQW50jApcoBKXRTnNhLMRUQhiAlxhmg1oskl5Z1DLb9IAwHj1tBAe15kU2aMbb_VJI0NGxNYHGh571zV51_nlZpOKH4rXWHFLd3ae8xQynIv5EZqzP70Hy-ea7ksR9pjBvdhkdb9Pfpzsf1Q-f3kGo8zgYoF526PQb2JNHJC8Hyn00uUe8djNLevAIbriRrQ47a7WFdkwT1uurzFrBL-Ked7C9f_4a_yVUriSoXt2hYg9gpn6Qlhcw5wtwa3YIXIomtNcVIpydgxK2VTR_H9pvHNJ9ipIqLkytmuJuUAYdTDNC6Ahg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59577ce95d.mp4?token=FaNs5NGMYM36s6HPR2tAJ7Tp9mmiRFU7ItB2tQW50jApcoBKXRTnNhLMRUQhiAlxhmg1oskl5Z1DLb9IAwHj1tBAe15kU2aMbb_VJI0NGxNYHGh571zV51_nlZpOKH4rXWHFLd3ae8xQynIv5EZqzP70Hy-ea7ksR9pjBvdhkdb9Pfpzsf1Q-f3kGo8zgYoF526PQb2JNHJC8Hyn00uUe8djNLevAIbriRrQ47a7WFdkwT1uurzFrBL-Ked7C9f_4a_yVUriSoXt2hYg9gpn6Qlhcw5wtwa3YIXIomtNcVIpydgxK2VTR_H9pvHNJ9ipIqLkytmuJuUAYdTDNC6Ahg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروز کریمی: اونور یک دقیقه ای بازیکن اتریش اومد گل زد، چطوریه که طارمی سه بازی گل نزد؟ طارمی خیلی پولدارم هست و مقصر صعود نکردن ایران هم خودشه باید پول بلیت برگشت کادر و بازیکنان رو بده
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/134561" target="_blank">📅 22:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134560">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❗️
عادل فردوسی پور: مدیران‌تیم پرسپولیس باخودِ مهدی لیموچی برای قرارداد به توافق شخصی رسیده‌اند و درصورت توافق با مدیران سپاهان این انتقال انجام میشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/134560" target="_blank">📅 22:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134559">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
|
#فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» حدادی شخصا میخاد با امید عالیشا،میلاد سراک،رضا شکاری،مرتضی پورعلی گنجی،دنیل گرا و تیوی بیفوما فسخ کنه.
❌
حالا باید ببینیم بانک شهر برای فسخ و آوردن بازیکن جایگزین بودجه میده یا نه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/134559" target="_blank">📅 22:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134558">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
|
#فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس توافق نامه دو جانبه توسط اوسمار ویرا امضاء شد و رسما اوسمار ویرا از پرسپولیس جدا شد!
❌
مفاد توافق نامه بدین شرح است: باشگاه پرسپولیس باید ظرف ۲ هفته مطالبات باقی مانده اوسمار رو پرداخت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/134558" target="_blank">📅 22:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134555">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/134555" target="_blank">📅 22:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134554">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozPocczO61K_8FSuc2m0QbOo9rNeOA_vYsY2jcQQyOUFKdAqhHfdVhC_Skrn8Yl4Cse4CiWRyklFUmKTnrzbv_aM64Ly-MxJUYiqSShtmt37EQeNqZ18shcfE66qbhgrXW-QYsRI9zkkJYE-ux0ogVBr-YPRtIbYL5HWa6RYaJLuJAl6z1ANK_uvijKHKVeUPSbV7F9WoZNOEXlZlMuuFEvYqxBcN4JE1ljNrhnTagQ0--F0wMiDddla3EG8Cy7UQMWyr5ItUD2zrsZ7uOz7sD5J9KU0ceBxQ6Y9aTS6tN2JTMIwwkyzfV-bLnV0io-tUfa6xXMceyzlmXooMlGcWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
مرحله یک‌شانزدهم نهایی رقابت‌های جام‌جهانی
6⃣
2⃣
0⃣
2⃣
از راه رسید!
🔵
اوج هیجان فقط با وینکوبت،
دیدار جذاب امشب کانادا
🔴
-
🟡
آفریقای‌جنوبی رو با
🔣
0⃣
1⃣
بونوس اولین واریز پیش‌بینی کنید!
🔴
جام جهانی ۲۰۲۶ رو با وینکوبت پیش‌بینی کن و ۱۰ درصد بونوس اولین واریز بگیر.
🟢
چرخش رایگان گردونه، شانس روزانه تا سقف ۱ میلیون تومان.
🔗
برای پیش‌بینی بازی‌های جام‌جهانی با بیشترین آپشن ممکن همین حالا وارد ربات مینی‌اپ وینکوبت بشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🔗
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/134554" target="_blank">📅 20:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134553">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❗️
❗️
اسکوچیچ خواهان جذب دروژدک مهاجم اسبق خود در تراکتورسازی، برای پرسپولیس شد.
🎙
خبرگزاری تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/134553" target="_blank">📅 20:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134552">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فرشید حقیری :
⛔️
اسکوچیچ سرمربی پرسپولیس شد تمام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/134552" target="_blank">📅 20:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134551">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
سفیر آمریکا در سازمان ملل: صبر ترامپ نسبت به ایران در حال تمام شدن است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/134551" target="_blank">📅 20:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134550">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❗️
عضو کمیسیون امنیت ملی مجلس:
✅
ممکن است ترامپ به زودی دامنه جنگ را تشدید کند و تفاهم نامه با ایران را پاره کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/134550" target="_blank">📅 19:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134549">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
شنیده ها: پاتریس کارترون گزینه پرسپولیس در صورت عدم توافق نهایی با اسکوچیچ!!!!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/134549" target="_blank">📅 18:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134548">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iP9LJlLC5KTIEPwIfO6e8d-dS6XJqgLx68-1UaubE54NsRqAer2-pfsRgiYsTOls1o5ED4LKTSawsyujZ7qaiyMS6xjlANZqIw94PcOjKBntUbkJqqBUHSn5iTD55Bp5mCrIiOqoYwIakUeLnO84GuAQqXTZdEUUvX1BnJZUvI1l98AuoRH0yNm6KAUyQ_MP1lhe45ugPneX4NeuWNYP_LVdFqFFjJGH8Rl36duqARDIS6l747ePXqTAIaGdcx81BCxnu2ovvB1g_GfFjMpyhZa4zZKrD48GpInYKIPlTA87aXhDnFrDsyhKWC9i-1io9T3kr1_GBOdlmbPoRKKJnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏐
نتایج تیم ملی والیبال ایران در هفته دوم لیگ ملت‌های والیبال ۲۰۲۶
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/134548" target="_blank">📅 18:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134547">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
زنوزی، مالک باشگاه تراکتور به صورت شخصی با مرتضی پورعلی گنجی، مدافع پرسپولیس وارد مذاکره شده تا این بازیکن راهی تبریز شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/134547" target="_blank">📅 18:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134546">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3CJ913EnCF_9VG3zMxw5sSILsDL4paHiEq6pfuf-TYxPZ8KLmkUcdsKJIBxekJUHWtHFfi7lYqAhVftO-9oH8NRit59fxYIOctRRXlGhlSuWfHHr26R3JrOPvPjg1LvVbJVemi9NYsYHTHzsnXOSOLPiBdSkP9lh2RAV73xgZt2kE6uJBNeUVYNbgx0OHd6lauNIo-UrI7ecYzUzzwSyR5dnyXqO4DmID8PfpM3oQXvWyQuITmxKccauXlWAMjm1Xdqfh_SY9CZocxyT7ADMtg0wO0vQWDmWhTm6cGclES4M4FaKqzkoV-f0-bVbUcEi5mRDB_8r_CxPFgoHILhgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
فوری از قدوسی: علاوه بر اسکوچیچ، باشگاه پرسپولیس در حال مذاکره با یک سرمربی نام آشنای دیگر نیز می باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/134546" target="_blank">📅 18:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134544">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
❌
قدوسی: اوسمار ویه را از سال گذشته 400 هزار دلار طلب داره و تنها در صورت دریافت طلبش فسخ می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/134544" target="_blank">📅 18:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134543">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
⚽️
پیمان حدادی مدیرعامل باشگاه پرسپولیس در گفت و گو با نزدیکانش خبر استعفای خود از مدیرعاملی پرسپولیس را شایعه دانسته و تکذیب کرده است  بازگشا سخنگوی باشگاه هم در گفت و گویی که داشتیم استعفای حدادی را شایعه دانست و تکذیب کرد/قرمزآنلاین
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/134543" target="_blank">📅 18:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134542">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMobin</strong></div>
<div class="tg-text">این خبرها همه سفارشی از عالیشاه باندشه که حدادی کله پا کنند ح رومزاده ها فکر کردند این باشگاه ماله باباشونه که بخوان تا زمان فسیل شدنشون تو اینجا باشند واسه این همه هوادار تصمیم گیری کنند</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/134542" target="_blank">📅 18:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134541">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
قرار است امروز (یکشنبه) جلسه هیئت‌مدیره انجام شود که دور از انتظار نیست خروجی این جلسه، برکناری اوسمار، انتخاب اسکوچیچ و البته پذیرش استعفای حدادی با انتخاب سرپرست مدیرعامل جدید باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/134541" target="_blank">📅 17:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134540">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
#مهم | لحظه امضای نسخه فارسی یادداشت تفاهم ایران و آمریکا توسط دونالد ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/134540" target="_blank">📅 17:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134539">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
#فوری
🚨
هیات مدیره پرسپولیس برای فردا صبح جلسه فوق العاده گذاشته و درباره آینده پرسپولیس تصمیم گیری خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/134539" target="_blank">📅 17:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134538">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❗️
به گزارش خبرنگار قرمزآنلاین، طبق اخباری که قبلاً منتشر کردیم، باشگاه پرسپولیس و دراگان اسکوچیچ بر سر دو موضوع با هم اختلاف نظر داشتند که یکی مدت قرارداد بود و دیگری درج بند فسخ در قرارداد در صورت تکرار جنگ که اکنون خبر می رسد دو طرف، توافق کرده اند مدت قرارداد…</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/134538" target="_blank">📅 17:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134537">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
دیدید حالا نمیشه
✌🏻
🔴
تا وقتی به مردمت پشت کنی و دل مردمت باهات صاف نباشه احتمال ۹۲ درصدی صعودت هم به صفر تبدیل میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/134537" target="_blank">📅 17:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134536">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
فووری از فارس: مدیران باشگاه پرسپولیس خواسته دراگان اسکوچیچ را پذیرفتند و این مربی با عقد قراردادی دوساله (مشروط) سرمربی پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/134536" target="_blank">📅 15:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134535">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🏐
برنامه کامل مسابقات تیم ملی والیبال ایران در هفته دوم لیگ‌ ملت‌های‌ جهان؛
❌
از فردا شب شروع میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/134535" target="_blank">📅 15:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134534">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
فووری از فارس: مدیران باشگاه پرسپولیس خواسته دراگان اسکوچیچ را پذیرفتند و این مربی با عقد قراردادی دوساله (مشروط) سرمربی پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/134534" target="_blank">📅 15:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134533">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✅
تمرینات پرسپولیس به مدت شش روز تعطیل شد و قرار است از شنبه هفته آینده تمرینات پرسپولیس برای فصل جدید در تهران آغاز شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/134533" target="_blank">📅 15:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134532">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⚡️
2- آلویس نانگ (Aloys Nong)
⚡️
آلویس نانگ نامی آشنا برای فوتبال‌دوستان ایرانی است زیرا عملکرد خوبی را در لیگ برتر ایران با تیم‌های فولاد خوزستان، نفت تهران، تراکتور، استقلال خوزستان، پارس جنوبی جم و سایپای تهران داشت. او که با سابقه بازی در باشگاه‌هایی مثل…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/134532" target="_blank">📅 14:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134531">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⚡️
⚡️
- سانل کونیویچ (Sanel Konjevic)
⚡️
این مربی اهل اسلوونی دارای مدرک یوفا پرولایسنس بوده و در زمان بازی، حضور در تیم‌های اسووبودا و اینتربلاک از اسلوونی و فرلاخ و استراسبورگ از اتریش را تجربه کرده است. او به عنوان سرمربی در باشگاه‌های اینتربلاک، برینیه و…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/134531" target="_blank">📅 14:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134530">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❗️
آشنایی با کادر احتمالی اسکوچیچ در پرسپولیس؛ از مهاجم و مربی سابق تراکتور تا دروازه‌بان سابق دینامو زاگرب
👇
👇
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/134530" target="_blank">📅 14:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134529">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
سایت اسپورت نت کرواسی مدعی شد؛اسکوچیچ و سه مربی از کرواسی، اسلوونی و کامرون در پرسپولیس
🔴
- آلویس نانگ بازیکن سابق فولاد و تراکتور
🔴
- سانل کونیویچ دستیار سابقش در تراکتور
🔴
- ماریو یوزیچ مربی دروازه‌بانان سابق رییکا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/134529" target="_blank">📅 14:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134528">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRnxbRG9eRvjAuM_NIWu44OyasxUNZK62wnDKHWUiwS0fDSUKESg-JgCMg61IK81KfNvcnUe-6t-tCFpmSrd-KeyXINvaIntQjkL78l-5iR5Citztn36HrRhLo0tQxfEUHl8bJi6zQPD9m0szeFQ8caGzXejGtVxv75r4Tks2W7ouxmbzE6jn3cLH_02woMgd4_IMRTnASy_xGpz7f6fRMiBsZWUs_GsC-yKa7XwRG_6YOqrRNlCqvjy0R5QT2GXH3ISZTToFDIatd5Igfv4125-95XkR1tRb8CQhPg413WhA8ob8oNkk4oqE2LMmPxHuun5VYbtZBO5u65pllvrWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویری پربازدید از اقامه نماز در رختکن تیم ملی فرانسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/134528" target="_blank">📅 14:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134527">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❗️
اخباری: گل لحظه آخر را بازیکنی زد که تازه داماد شده و دیشب به تیم اضافه شد. او گفته بود روی من حساب نکنید ولی گفتم کنارمان باشد تا روحیه بدهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/134527" target="_blank">📅 14:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134526">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
فووری از فارس: مدیران باشگاه پرسپولیس خواسته دراگان اسکوچیچ را پذیرفتند و این مربی با عقد قراردادی دوساله (مشروط) سرمربی پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/134526" target="_blank">📅 14:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134525">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qy5q3XXKB11Y4Ydu2p_kcSsxtTCUgvEnooE7QIkCONAhhG9tIMrtqyPZnChPvtaRgrgl0i163oh0TpXvpKrDp7oCm53ATZqfG2_4peYhxnPGh0UlD4PkSw2EFx5ENzjwp6EV_Xtl96ptnz2eBZS850Xhg4u5VO-zdTstxDtAkZnf2hPf9FGc6P3mfjuukSSPUI5VleSRnE-SZQN2EUE3nEEjYYDJPJZqMreeYak78rJXQSMBirFNFkxZS2AwF5kBIoWnNBVtf7SdIm8Nu8cPoH3ZWANHA4UHrQMX10HjeATqZ5SL0vTLpUjnc1Q68Y_8w3_q1rlvmB77myaLdEtXnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووری از فارس: مدیران باشگاه پرسپولیس خواسته دراگان اسکوچیچ را پذیرفتند و این مربی با عقد قراردادی دوساله (مشروط) سرمربی پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/134525" target="_blank">📅 14:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134524">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
⚡️
تیوی بیفوما و دنیل گرا برای فسخ قرارداد به باشگاه دعوت شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/134524" target="_blank">📅 13:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134523">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d69fbc8a47.mp4?token=W7kNWzmy_6gfqMzYHqHzN-oRpEXYKdCI983goFd2A22T5WXLYIKwxFsmsQtSKw7P94Dr30TeH38at6bZ5RWm1bwrar-lwaMyj6m-JESvutM66QaeGrtf9kygbeLcgUwFJCytiJW40QmxX-NhjIAfFmHQab3zxwnqF7wMrbTfEZhDbjxxauyYwVqg9jRutGgALqNZiK8DspeRjVrTA1qV8BQnJ-K0zuTK3u38pU5JxGEA2XGjyVA_d09ytpYGILyRWrLQGcx4PeDgaUz8Y5meU_FsyUwNIYCi1CjCwP-DJB3I8-hNQQwK-eH4Wx-13X1zvH8E_REVvcaYqQBQb19AcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d69fbc8a47.mp4?token=W7kNWzmy_6gfqMzYHqHzN-oRpEXYKdCI983goFd2A22T5WXLYIKwxFsmsQtSKw7P94Dr30TeH38at6bZ5RWm1bwrar-lwaMyj6m-JESvutM66QaeGrtf9kygbeLcgUwFJCytiJW40QmxX-NhjIAfFmHQab3zxwnqF7wMrbTfEZhDbjxxauyYwVqg9jRutGgALqNZiK8DspeRjVrTA1qV8BQnJ-K0zuTK3u38pU5JxGEA2XGjyVA_d09ytpYGILyRWrLQGcx4PeDgaUz8Y5meU_FsyUwNIYCi1CjCwP-DJB3I8-hNQQwK-eH4Wx-13X1zvH8E_REVvcaYqQBQb19AcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
مصاحبه قلعه نویی بعد حذف از جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/134523" target="_blank">📅 13:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134522">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNPpokaejv-9RGaAXR0sggNQee48dTOWNAz7bwyEOjAXWXPEvMGf_yy6-t_nNqs2sKf7L0zeCj4z0EEk9yVnQ8Pbcl1HNM5w1cI6DR0FCVK2dWMi4P1h0N1KiB0r4PJJq49p7lv574vbCmaQxeHF8nTRhtAQiecVOqWLzX1koH4ubR3xlEpzH1DM9ozyGFyOgrwBnh0ZM3S-WfkGEHruCfOc7tDCUE7vIBlNUad9VrIrEwnW-tIMfJXqBvSIViRABib7pdM0aW-Lyb5axw3S6V388QKSfAuddfseFTqxYSSmC66HtyYQEYvWlWgcxw47DBqts7PbpzzlE_X8F9KLnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
یک‌شانزدهم نهایی جام‌جهانی ۲۰۲۶
[
آفریقای‌جنوبی
🇿🇦
🆚
🇨🇦
کانادا
]
⏰
یکشنبه ساعت ۲۲:۳
۰
🏟
استادیوم
سوفای
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/134522" target="_blank">📅 13:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134521">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
قرارداد گولسیانی با سپاهان 700 هزار دلار بوده و او برای فسخ قرارداد، کل این پول را خواسته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/134521" target="_blank">📅 12:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134520">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
ابراهیم اسدی: شأن پرسپولیس حفظ نشد
🔴
🔴
پرسپولیس در حد و اندازه‌های همیشگی خود ظاهر نشد و این حذف برای هواداران قابل قبول نیست. ای کاش تصمیمات مدیریتی و فنی با دقت بیشتری اتخاذ می‌شد و تیم در مسیر بهتری قرار می‌گرفت. این سبک آسیایی شدن در شأن تیم بزرگ و پرهواداری…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/134520" target="_blank">📅 12:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134519">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uitI5KiQFpRRg8rd8zqrBXZYSyftJfUD7Mp8GcpkyCRCRt_648uICJU1Z7ztwuu6PnRpDxxxaI7uR0eh-09vdHAwEdRDv2uHiq1bg4sz3oMJf2djK-3yHghUgArdVLwmTuAg4x5B2xSivwoMLeq0d1SlazaO06aGBMdE34rthOLt3ftJjkYCf3kJvi3hNO2XdBLCd0vKQoI1kitoM7lcGkPiDQ5mickLOXP6kslaiQ69o7DAG4bsJa2fZ57kWq2bdA1E_5ZSTcr6DUKxwPIeh-b8-u5Wg9Ng5v9Dh0f7LPnEFeMOlL40T1Jsf77pQQLGjNdZPO9rBRHtfssbm0XzBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعد گل سوم الجزایر اینجا بازیکنشون میگه اگه ببریم میخوریم به اسپانیا و ریاض محرز تازه میفهمه چه غلطی کرده بخاطر همین شل میکنن تا گل سومم بخورن.
😁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/134519" target="_blank">📅 11:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134518">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
واکنش میثاقی به تساوی باورنکردنی بازی اتریش - الجزایر: این بازی اصلا عادی نبود
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/134518" target="_blank">📅 10:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134517">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
دیدید حالا نمیشه
✌🏻
🔴
تا وقتی به مردمت پشت کنی و دل مردمت باهات صاف نباشه احتمال ۹۲ درصدی صعودت هم به صفر تبدیل میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/134517" target="_blank">📅 10:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134515">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">😂
😂
اتریش دوباره زد و ایران حذف شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/134515" target="_blank">📅 10:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134514">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
واکنش میثاقی به تساوی باورنکردنی بازی اتریش - الجزایر: این بازی اصلا عادی نبود
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/134514" target="_blank">📅 10:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134513">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
بجا مانده از امروز صبح
😐
😐
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/134513" target="_blank">📅 10:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134512">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/li_GCBNThAGCZRFuM83Ah0-eq6c7hFBgp8KLTiOzb14X1_ZpoFjH4vJnZG4vpobjq4fFM7akEHWPrpsEPMYIir7QRjFFuOIrTI6XnfjbAAKrSw7OubkpxoGTs8Q2Etr8UoHO2WJ9VG55wHOpSKFd4crYkP4iOOSc8oyckMVp-TdeccK0BOpJRAtZgpIXdAUL1xqBgm1EP_lImo_F_f01GJx2vVvoGFpkPl_rgSak1fq8ehZDVSqrX8XTn1kGYjkbZx7PNgEQAsG8FL65bfcrvj_JNslW5-kfRa8KxjjkVWyiYvO869GbtL3JZCV8Xe76RCuNCBFKVfNdlRPdWr1w0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اوسمار ویرا برای عقد قرارداد سه ساله با باشگاه تراکتور خواستار مبلغ 5.5 میلیون‌دلار برای‌ خودش و اعضای کادر فنی اش شده. درصورتیکه مدیریت باشگاه تراکتور با این درخواست موافقت کنند اوسمار راهی تبریز میشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/134512" target="_blank">📅 10:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134511">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
یادتونه ژنرال قبل از مسابقات میگفت تیم ملی یه کاری میکنه تو جام جهانی ایران یه هفته تعطیل بشه؟؟
🔴
هفته بعد تقریبا ایران تعطیله کلا ؛ ژنرال صعود نکرد ولی قولش رو عملی کرد
🙃
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/134511" target="_blank">📅 10:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134510">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0mCnzZayxuFnyQcVCSz9sBKb7bOVhFh0SkSoip3AsYyso02j6I02SvZr4LPOAwNmEXB_pYHh8Pk8RWG9iXZsZDaMoefqB08fphquqMlr2XzmGIzBc4DclbbJMtyyfK_KAGKYGFEhwZE6hi3NCZZ-kbL07VvEeAgO3mw9j9iuYc10cU5h3CaXlGOzAkam_FjpODETSNaQZayKyYKW4Kqa_7vqfSQoK_qI-lRAogniHVuW2uG9nDVcaDFKS8IM4-SOnbP1b5aoTiAkiUOjXv6hGvIDGi9lub0k4yElnd70jnpwWGCobODSaBbMXgEHYdQFaqHs2qjCp19cKJqvq2i2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
یادتونه ژنرال قبل از مسابقات میگفت تیم ملی یه کاری میکنه تو جام جهانی ایران یه هفته تعطیل بشه؟؟
🔴
هفته بعد تقریبا ایران تعطیله کلا ؛ ژنرال صعود نکرد ولی قولش رو عملی کرد
🙃
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/134510" target="_blank">📅 10:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134509">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❗️
❗️
تسنیم : قرار است به زودی در وهله اول باشگاه پرسپولیس مراحل اداری قطع همکاری با اوسمار را انجام دهد و سپس به طور رسمی جدایی این مربی برزیلی اعلام شود.
🔴
🔴
پرسپولیسی ها که با اسکوچیچ برای جانشینی اوسمار مذاکره و توافق کرده اند، هنوز هیچ قراردادی با این مربی…</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/134509" target="_blank">📅 09:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134508">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
دقیقه 92 الجزایر گل زد
گزارشگر: ۷ تیر رو یادتون باشه؛ یه تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد.
😂
🔴
دو دقیقه بعدش اتریش گل زد
😆
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/134508" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134507">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
واکنش میثاقی به تساوی باورنکردنی بازی اتریش - الجزایر: این بازی اصلا عادی نبود
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/134507" target="_blank">📅 09:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134506">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b235a5b41.mp4?token=Vl013Ol-pMXrkH9B5MRc25_LatEjymUEdxrrfBIiwY-vtiJ9ZjtDktHmqrlLEuLQEi7Y5iDS2d77n99X1JTrw5B8qQbhZDliPYAnyB6TsyjxllE1Y_O9IPpfed3p67IeWK_NeBTwbkjGuWFVGVXMnjqkqmBPHTQ54ITRjG68NmoYnGfjZ3FbAm3R51og3pvF8eMJOgarRFyzepSbRk03_B8LqMydyKBbZ_ED6Q3R5t4PNE_20-gxZuYzDNkQ13Ow2-pzpHvA_dJdrFUR8jGkxRt0tc-fHJnB58n-aX7624aogKMsBW0PItM_PKTq5409vNrrpewsE314z_dTWy9Zq1P7Xbn0b63FzDNso5SKXSbdrhj2RQFQWAnxeAqmVIV8kGKVPADCLeNnQlZQxw6oeA7bZky2RsKrSElUZSR47SpQCpOVbN9GxxDRoKzhzPE_APTeB8cWKvaEqzlYlaxWe2cjj4uxnI2xxQyANwPg78td_btEeL3Bn0KEfyC8wk0b887sp1My2jXZzEXJeS0ExbTjTE4VLhua3svyYfLhJiPRyLa9yqTa7N9mvjZDbP8S15cyjCXZZDwdvPxEe8ix1nsu09HXf-s7NfhvRbccyX-wovc2brY1NTKRlIbL6j9uM9WDyvsMN5rcPV2STK6rl1DQcLNOq03g8szzAefSO2E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b235a5b41.mp4?token=Vl013Ol-pMXrkH9B5MRc25_LatEjymUEdxrrfBIiwY-vtiJ9ZjtDktHmqrlLEuLQEi7Y5iDS2d77n99X1JTrw5B8qQbhZDliPYAnyB6TsyjxllE1Y_O9IPpfed3p67IeWK_NeBTwbkjGuWFVGVXMnjqkqmBPHTQ54ITRjG68NmoYnGfjZ3FbAm3R51og3pvF8eMJOgarRFyzepSbRk03_B8LqMydyKBbZ_ED6Q3R5t4PNE_20-gxZuYzDNkQ13Ow2-pzpHvA_dJdrFUR8jGkxRt0tc-fHJnB58n-aX7624aogKMsBW0PItM_PKTq5409vNrrpewsE314z_dTWy9Zq1P7Xbn0b63FzDNso5SKXSbdrhj2RQFQWAnxeAqmVIV8kGKVPADCLeNnQlZQxw6oeA7bZky2RsKrSElUZSR47SpQCpOVbN9GxxDRoKzhzPE_APTeB8cWKvaEqzlYlaxWe2cjj4uxnI2xxQyANwPg78td_btEeL3Bn0KEfyC8wk0b887sp1My2jXZzEXJeS0ExbTjTE4VLhua3svyYfLhJiPRyLa9yqTa7N9mvjZDbP8S15cyjCXZZDwdvPxEe8ix1nsu09HXf-s7NfhvRbccyX-wovc2brY1NTKRlIbL6j9uM9WDyvsMN5rcPV2STK6rl1DQcLNOq03g8szzAefSO2E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
واکنش میثاقی به تساوی باورنکردنی بازی اتریش - الجزایر: این بازی اصلا عادی نبود
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/134506" target="_blank">📅 08:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134505">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">😂
😂
اتریش دوباره زد و ایران حذف شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/134505" target="_blank">📅 07:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134504">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❗️
❗️
یا حسین ....الجزایر دقیقه نود و چهار گل و زد و ایران صعود کرد ...عجیبا غرببا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/134504" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134503">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
قشنگ دارن دو تیم اتریش و الجزایر تو زمین راه میرن که مساوی تموم بشه ....و ایران عملا حذف بشه ..چوب و ضربه بازی نیوزیلند و خوردیم ..و خداحافظ  ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/134503" target="_blank">📅 07:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134502">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
ده دقیقه تا حذف ایران از جام جهانی ...هیچ حالتی اتفاق نیفتاد ...غنا باخت .ازبکستان باخت ..اتریش و الجزایر با تبانی و هماهنگی فعلا تا دقیقه 80 مساوی هستند و میل بردن ندارن چون هر دو تیم صعود میکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/134502" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134501">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❗️
❗️
صعود ایران چگونه محقق خواهد شد؟
🔴
تیم ملی ایران فقط به یکی از اتفاقات زیر نیاز دارد تا به عنوان یکی از تیم های سوم صعود کند
🔴
شکست کرواسی برابر غنا
🔴
شکست نخوردن ازبکستان برابر کنگو.
🔴
عدم تساوی در دیدار اتریش و الجزایر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/134501" target="_blank">📅 07:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134500">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❗️
مثل دیشب
🇺🇸
🇮🇷
فوری از باراک راوید، خبرنگار نزدیک به ترامپ: مقامات آمریکایی حمله به تنگه هرمز رو تایید کردن و آمریکا رسما مسئولیت حمله رو به عهده گرفته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/134500" target="_blank">📅 01:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134499">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
خبرنگار فاکس‌نیوز به‌نقل از مقامات ارشد دفاعی بیان می‌کند حملات هوایی آمریکا همچنان در جریان است که باتوجه به حجم تحرکات هوایی در جنوب کشور ادامه‌دار بودن آن قابل انتظار است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/134499" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134498">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
برای اولین حالت باید ساعت 12/30 منتظر بازی غنا و کرواسی باشیم .که غنا ببره صعود میکنیم ..نشد باید ساعت 3 منتظر نباختن ازبک باشیم .....نشد باید ساعت 5/30 الجزایر و اتریش مساوی نشه .....
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/134498" target="_blank">📅 01:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134497">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJFI1el_iT1D-MBdh12J6GBpbEewrgF7Cc4tNY_HtfygY_bYODh4lwCsuPuXiqlpRWnxw80jhy7YIkQP_UMCd26XE-IAhe94qhwH7HUmOwOvIsTTI0iND7_diQPqRdf4FDWftpeJKmueWFGkk2amqkgIj_pnhT8Dm0j4qhD9lJBjT_1UKAkuzSTmDDDUxaKC1D1yC9I5auyGh5GzFdzwqWEgT9TF03MgRhvK9Y1o33Ic4mdbVontL9EUdBcwghfH7Dlt4omcVwBz305Z9_wq58QTZYuMoDqUcWdbbssMeNzvua4RPb2ZPHIETgfJtN4XawigC8RTL9gzQj3YcwoVGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جان سینا : ظرف روزهای آینده برای امضای یک قرارداد اسپانسرینگ مهم با همسرم به ایران و شهر زیبای شیراز سفر می‌کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/134497" target="_blank">📅 00:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134496">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❗️
بعیدع کسی سه بازی و بیدار باشه .ولی امیدوارم صبح که از خواب بلند شدیم .بخونیم که ایران صعود کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/134496" target="_blank">📅 00:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134495">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⚽️
باشگاه با سرلک و پورعلی‌گنجی تماس گرفته گفته بیاید برای فسخ
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/134495" target="_blank">📅 00:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134494">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
مهدی طارمی: این جام‌جهانی فاجعه بار است، فاجعه‌ بارترین. فیفا باید هر مشکلی را که وجود دارد، حل کند. اما متاسفانه از همان ابتدا نتوانستند چیزی را حل کنند. اکنون دوباره برای رفتن به تیخوانا سفر خواهیم کرد، بدون ریکاوری. این منصفانه نیست. اگر این از نظر فیفا…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/134494" target="_blank">📅 00:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134493">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❗️
ساعت 3 تا دیداری که روی صعود نقش دارن:
🔴
کرواسی _ غنا / 00:30 بامداد
🔴
ازبکستان _ کنگو / 3 صبح
🔴
اتریش _ الجزایر / 5:30 صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/134493" target="_blank">📅 00:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134492">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
جزییات تاریخ برگزاری آئین خاکسپاری علی خامنه‌ای (رهبر شهید )   ۲۰، ۲۱، ۲۲ خرداد/ وداع در حرم امام‌ خمینی  ۲۳ خرداد/ تشییع در تهران  ۲۴ خرداد/ تشییع در قم  ۲۵ خرداد/ تشییع در عراق  ۲۶ خرداد (اول محرم)/ تشییع و خاکسپاری در مشهد  پ.ن تخمین جمعیت حدود 25 تا…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/134492" target="_blank">📅 23:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134491">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
مسوولان باشگاه به موازات این تلاش ها در تلاش هستند توافقات اولیه یا اسکوچیچ را به قرارداد منجر کنند. آن‌ها بر سر مدت قرارداد یا اسکوچیج بر سر امضای قرارداد یک+یک ساله و مشروط برای سال دوم توافق کرده و تنها اختلاف حل نشده درباره بند فسخ همکاری در صورت بروز…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/134491" target="_blank">📅 23:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134490">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
مسوولان باشگاه به موازات این تلاش ها در تلاش هستند توافقات اولیه یا اسکوچیچ را به قرارداد منجر کنند. آن‌ها بر سر مدت قرارداد یا اسکوچیج بر سر امضای قرارداد یک+یک ساله و مشروط برای سال دوم توافق کرده و تنها اختلاف حل نشده درباره بند فسخ همکاری در صورت بروز…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/134490" target="_blank">📅 23:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134489">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a47998bb9e.mp4?token=bnzbPYWHswoIyEk04V7pYQfGOpXr7e8VCEShU83sKDXYBnVKnF1NME9paLnKrVYpd_XOtFBwJ2WTQpGENeq3BZc9-tU5rNxzgBEGNPM4GJFpJK3Rrvf7vRfFXGjn6vyzClhPu1hzpsC-QZr1lXIlBJreX5QVvQ-iVId95MSNSxiDjOqS-4r0KsPGV-DY2z6kjXV2bGyPPoE29jsWKeesAOIZlGSLzQ8QiJaCkOkUGGGTaB32SRG-DUGowjBxsVnuT64MyWRRqCVnfZz2Y1qjgePwVmmgEpj14Cdo9DZmMYieLMjlktdF2JP4ZI8CDdsAL7Hl_wcvIG0wPGkT1Gc9KHEdzbekeR_LRupG64YcR1N6jTZORwYxWcLwtNeN4H0UY86hJ9mwUitcxR2p79ydgzZjMIsQzfGflQxE_KdH2hp4nLidn51-itycRYPuNfe0XjJvih1pf5R1vXCV-3XvLhzTQnm1wuBmhqeD2Wo9WWV0eYyEbty9zSCryt_wqqubb1u3WM3EOyrK7ZV8hawyeKyEletzljIR8vNdkGOKUU73PLoUTi4sblUDpoIpk0wvyPMyv6WZQqrPa0CbURcisBrV-wgmVSGpbTJSDhy5X18-E0_rSCb6en6Z8gYL1jwCBjno_WV-4bF1iYbo96yssxOlldF-Z8lSFclDU1MhF6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a47998bb9e.mp4?token=bnzbPYWHswoIyEk04V7pYQfGOpXr7e8VCEShU83sKDXYBnVKnF1NME9paLnKrVYpd_XOtFBwJ2WTQpGENeq3BZc9-tU5rNxzgBEGNPM4GJFpJK3Rrvf7vRfFXGjn6vyzClhPu1hzpsC-QZr1lXIlBJreX5QVvQ-iVId95MSNSxiDjOqS-4r0KsPGV-DY2z6kjXV2bGyPPoE29jsWKeesAOIZlGSLzQ8QiJaCkOkUGGGTaB32SRG-DUGowjBxsVnuT64MyWRRqCVnfZz2Y1qjgePwVmmgEpj14Cdo9DZmMYieLMjlktdF2JP4ZI8CDdsAL7Hl_wcvIG0wPGkT1Gc9KHEdzbekeR_LRupG64YcR1N6jTZORwYxWcLwtNeN4H0UY86hJ9mwUitcxR2p79ydgzZjMIsQzfGflQxE_KdH2hp4nLidn51-itycRYPuNfe0XjJvih1pf5R1vXCV-3XvLhzTQnm1wuBmhqeD2Wo9WWV0eYyEbty9zSCryt_wqqubb1u3WM3EOyrK7ZV8hawyeKyEletzljIR8vNdkGOKUU73PLoUTi4sblUDpoIpk0wvyPMyv6WZQqrPa0CbURcisBrV-wgmVSGpbTJSDhy5X18-E0_rSCb6en6Z8gYL1jwCBjno_WV-4bF1iYbo96yssxOlldF-Z8lSFclDU1MhF6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
😆
جواد خیابانی در ویدیویی به زبان عربی، از الجزایر تقاضا کرد اتریش را مغلوب کنه تا تیم ملی ایران به مرحله حذفی صعود کنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/134489" target="_blank">📅 23:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134488">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
یعنی هیچ موقع تو زندگیم اندازه امسال اعصابم خراب نشد،حالم بده
❌
نیم فصلم استاد خلیلی و فرزاد پوفو…. دل و قلوه میدادن باهام دنده دادن تا راحت این دلال های دوزاری اوسمار و خود کونده خارش زن تیمو هوا بدن،اقای حدادی تنها اشتباهات اوردن خلیلی بود
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/134488" target="_blank">📅 23:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134487">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🫦
جمع کنید
کص کونتونو،ولدز
… ها دوتایی ریدید سر تا پای تیم برای ۵ ماه ۱.۲ میلیون دلار گرفته
ولدز
… گوه زیادی هم میخورید
🫦
کونده پدر
تو لیستی که به باشگاه دادی تو هر پست دوتا بازیکن اولت مال دلال های خودت بود کیر تو فیست
🫦
مرتیکه کوتوله تو بوریرام قهرمان شد…</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/134487" target="_blank">📅 23:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134486">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
#فرهیختگان؛ اوسمار وقتی فهمید با اسکوچیچ مذاکره کردن اصلا نمیخواست به تمرینات ادامه بده به اصرار ایجنتش این بازی رو روی نیمکت نشست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/134486" target="_blank">📅 23:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134485">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
باشگاه باید ابتدا از لحاظ مالی با اوسمار توافق کنه و سپس از اسکوچیچ رونمایی کنه/طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/134485" target="_blank">📅 22:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134484">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
نساجی مازندران به لیگ برتر بازگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/134484" target="_blank">📅 22:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134483">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
باشگاه باید ابتدا از لحاظ مالی با اوسمار توافق کنه و سپس از اسکوچیچ رونمایی کنه/طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/134483" target="_blank">📅 21:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134482">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❗️
❗️
صعود ایران چگونه محقق خواهد شد؟
🔴
تیم ملی ایران فقط به یکی از اتفاقات زیر نیاز دارد تا به عنوان یکی از تیم های سوم صعود کند
🔴
شکست کرواسی برابر غنا
🔴
شکست نخوردن ازبکستان برابر کنگو.
🔴
عدم تساوی در دیدار اتریش و الجزایر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/134482" target="_blank">📅 21:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134481">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJZwduyt3rTflkwAEDwW_q_ihhqH38NU9zMVtLkBX8ANjj4loeMZDK1iHqyFZmUpwkeEhc_3Yxsz7mY9IX5fTW0TaCC2LDW2iMKc0vUpw6peUZNa9VxuIQkIHvXHTcRJSLHgTu1iY2rzFhNgeJskKnIu0Lmdf1AiTWIz0ItlDGhaFT4H7_S4W1vUVcdChHn-ewuTjnPq04kx0Fvn7IP3vnKAoI83SK7LQywhW3ToXfnHOI2ABYgeiaJtAJ3oYUpbArumUXTHTuZ-d1APJpWKgEBE0eyyTozVKg4XGVmZuj4mWmLTcdLqBZj4XHmW1WLfSo5pNzHzQRT89IWO5tFOwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
شادی بعد از گل شجاع خلیل‌زاده که تبدیل به یکی از بزرگترین میم های جام جهانی شد.
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/134481" target="_blank">📅 21:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134480">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔸
بیرانوند و جایزه بهترین بازیکن زمین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/134480" target="_blank">📅 21:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134479">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❗️
❗️
تسنیم : قرار است به زودی در وهله اول باشگاه پرسپولیس مراحل اداری قطع همکاری با اوسمار را انجام دهد و سپس به طور رسمی جدایی این مربی برزیلی اعلام شود.
🔴
🔴
پرسپولیسی ها که با اسکوچیچ برای جانشینی اوسمار مذاکره و توافق کرده اند، هنوز هیچ قراردادی با این مربی…</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/134479" target="_blank">📅 21:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134478">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
اسکوچیچ سرمربی جدید پرسپولیس شد؛ توافق نهایی انجام شده و قراردادش تا ساعاتی دیگر ارسال می‌شود. او هم به‌زودی برای شروع کار به ایران می‌آید.
✍
ایسنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/134478" target="_blank">📅 21:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134477">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🎙
کارلوس‌ کی‌روش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتوانیم کرواسی را متوقف کنیم تا ایران به دور بعدی جام جهانی راه پیدا کند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/134477" target="_blank">📅 21:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134476">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
واکنش تند زلاتان ابراهیموویچ به مردود شدن گل ایران: رؤیای یک ملت را دزدیدید
✅
زلاتان ابراهیموویچ با حمله‌ای تند به تصمیم داوران درباره گل مردودشده ایران گفت: شما فقط یک گل را مردود نکردید؛ رؤیای یک ملت را دزدیدید.
❗️
اگر این سطح داوری در بزرگ‌ترین تورنمنت…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/134476" target="_blank">📅 20:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134475">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brCzvlI51_7Od-HMQ8Sw8_Assh0-pXgrHYS7meid8BCB1jZlXNMOfTAoiSIZArkWfAptF5uD4SQD0Tis2UFPYrmChIh0QZRekhmJZxSd0C0ObcwIdO8nhJOAIKTWJ_ZIHoC9tKF1rrGNtIAgSKj42olWkvwDpuZye2oTefIcu0dBLqGDcdS6Kf2dSbSGxUA47bxxPZheyCpcDt3oOMPDgltR97h9PWYQLm2EdTBNohUINpCHEbPuS9h63Hf6lb9PH6WoaojvzX8vWc7qElXdK9DKSBPPhWl6Rg3jvps0mOlnwZv3CtblCrF8ErRhdaqCY4m3yYGc3GM3Nmq4-5f-IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
دیدار حساس و هیجان انگیر امشب پرتغال
🔴
-
🟡
کلمبیا رو در وینکوبت با بونوس ویژه و بالاترین ضرایب پیش‌بینی کنید!
⚫️
🔣
0⃣
2⃣
بونوس ویژه جام‌جهانی روی هر واریز برای تمامی کاربران!
🎁
تا پایان مرحله گروهی جام‌جهانی روی تمامی واریزها
🔣
0⃣
2⃣
بونوس بگیر و فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه فقط تا پایان مرحله گروهی جام‌جهانی فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/134475" target="_blank">📅 20:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134474">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
نظرت در مورد بازی ایران و بلژیک ؟
🔴
ابراهیموویچ : نزدیک بود نیمه اول خوابم ببره و نیمه دوم واقعاً خوابم برد
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/134474" target="_blank">📅 19:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134473">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوری از ایسنا:
🎙
اسکوچیچ سرمربی پرسپولیس شد و طی روزهای آینده وارد ایران می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/134473" target="_blank">📅 18:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134472">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❗️
❗️
اگر اتفاق خاصی رخ ندهد؛ تا روز سه شنبه باشگاه پرسپولیس از دراگان اسکوچیچ سرمربی جدید و کروات خود در فصل جدید رونمایی میکند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/134472" target="_blank">📅 18:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134471">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
❗️
اگر اتفاق خاصی رخ ندهد؛ تا روز سه شنبه باشگاه پرسپولیس از دراگان اسکوچیچ سرمربی جدید و کروات خود در فصل جدید رونمایی میکند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/134471" target="_blank">📅 18:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134470">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
شنیده ها :باشگاه‌پرسپولیس‌ برای‌دراگان‌اسکوچیچ بلیط گرفته و این‌سرمربی این‌هفته رسما وارد تهران میشه. قرارداد اسکوچیچ با تیم پرسپولیس دو ساله است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/134470" target="_blank">📅 18:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134469">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
⚽️
فرهیختگان : پیمان حدادی دنبال این است که با  دنیل گرا و تیوی بیفوما برای جدایی این ۲ بازیکن و فسخ قراردادشون توافق کند ؛ این درحالی است که هر دو بازیکن یک فصل دیگر با باشگاه قرارداد دارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/134469" target="_blank">📅 18:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134468">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
میثاقی: اوسمار بعد از بازی دیشب اخراج شد و پرسپولیسم قبل تورنومنت 3 جانبه با اسکوچیچ بسته بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/134468" target="_blank">📅 18:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134467">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrOrcPWkBEAzaeXpZ3dnfGG5sixcGwUBgZ5F6ocZI1AQrRxa3HpP3uP5WOn3wDBZm_PvzVcOi4aVqoYUPFindtrN73dF6FJensg6Rj5uErx52YN2jMy2qLmWebm4WRAIA2K6UGW11I3yQ0KiLe-bn8LqarRZLuS10JN9XuBEnhS4743DM29BIM8WWDdnsL_tMDIGly88ZaPzT9foCeTDY_FxmQsL0CliprLFpQhgpOc5BN6CT7g1H5-S7NQnSQ2WDtwaN3VAoT9V6Pc7fNHmFEhaLE39aWI3tj6TsoYoWkwTVZnpa2p2ARiz0tHqwoO_hedXShbraVaBnqXS0da_2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شنیده ها :باشگاه‌پرسپولیس‌ برای‌دراگان‌اسکوچیچ بلیط گرفته و این‌سرمربی این‌هفته رسما وارد تهران میشه. قرارداد اسکوچیچ با تیم پرسپولیس دو ساله است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/134467" target="_blank">📅 18:13 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
