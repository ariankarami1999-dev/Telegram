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
<img src="https://cdn1.telesco.pe/file/dT6ILaS8Y8E2LiQK7g0DObVOMfNgj-Mo5X0jVVqJoJuAEKVDgm6IqV2y0CMawAwTRnoa5-c3sbR8PGWw-YdKg4PwoN0ny179QF7ZbUXR3IG7p13d6VBOfnAYLJ-HtEkmPspHVhxGlc30FN-pcxu-aoerBJkexfYmk9_7xdsiAe0dB2V8SzUZRAXSYkL2MLBpejTUy03ye3QKjfgGtWHKw6Ch2-3HwaRMepZWQWpnNEZMhAM_Ko2uPCvUfsPXavB3OZlvBq7PpSyzOKfFTBXjgNZYr5vLw3oV-nnUy1mMYasJUM-m9z3MQ2xlhe_OkThEGgJb9dDcmoB-He53B2axqw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 162K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPaiهمکاری:@MatinPaiSen</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 21:30:46</div>
<hr>

<div class="tg-post" id="msg-3662">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">Operator: Asiatech/Datacenter Time: 2026-06-02 21:01:30  The status of this service has changed to:
✅
DNS google.com via 1.1.1.1 : 142.251.14.138</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/MatinSenPaii/3662" target="_blank">📅 21:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3661">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-text">Operator: Asiatech/Datacenter
Time: 2026-06-02 21:01:30
The status of this service has changed to:
✅
DNS
google.com
via
1.1.1.1
:
142.251.14.138</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/MatinSenPaii/3661" target="_blank">📅 21:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3660">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RpaYrGc_JJiwS0b0xD3wwmYZZZXwPXUgTg7TvTT6DgRkOkobB2AqyaXkd6gnR9NOszn9eaQrmdNIfCdfjcRouGUrF2DdHRilDUTb_yKOfn4aZvecG5ZRbAsT1j74THwTwDXSmH_TZYZWHVZwoS1gDXgT1JY4lQ38MxnkF7hDUW8njln2n0jI4ly1Rlmj8BJRr_m8TDjbJYwXgrNz9eezI6Dx4FrZZogYoVmIJe05N4NuYONi0ZpMaAcWu3LQApyk6gmukRputxYrVb0S1i13fPAQn0fYCbwHXD4mAXJBQun1uUtNNTcrZI0_vhW0HV5IdrVQtC81-zCVQvvPvae9JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچند یک سری دیتاسنترهای خاص یه سری تانل‌ها روشون جواب میده به راحتی. از جمله Paqet و بک‌هال و  reverse</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/3660" target="_blank">📅 19:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3659">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d3VvMiMHgThoUE3Eu0FIYg6-k-ub9PT7_e1MhfKO1IKP2NA9euOFZ2eWv-8CZRDUtlvH6RIbM3K6La2w-BlmKCs2yRb2p_DhX3idxK-8pZRy4lm5NRr3MNU8IO4SCgzl7ELzcHXDC5qmmPwqWJfS9DNy0Sz8bUl_s6Z7KLGUBbYmKev-JuBhFPOpdgeeLgBCBJvGvA8Hefxc3f5xZyPd1j4GZ27TwOdOqNhX9Z24zB0qkglSsoZRWLE9WypwKrQkaPh2L7va7s6KYNkvqvCKp-7DuXUSq0yzH-9PlloVj6oXgHBQYI0YwhNiXy7Dr94rpOijNIA4gE7wE1W-nKIMIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت نامحدود تصویر با هوش مصنوعی Nano Banana 2 گوگل + طراحی رابط کاربری(UI) و ساخت ویدئو و موسیقی
⭐️
توی این ویدئو:
1- بهتون نشون میدم که خودم Thumbnailهام رو چطوری میسازم و چه شکلی می‌تونید به صورت نامحدود از Nano Banana 2 و Pro گوگل استفاده کنید
🎤
2- یه UI باحال با هوش مصنوعی به همراه پروتوتایپ طراحی می‌کنیم
❄️
3- و با همدیگه یه موزیک در مورد 90 روز قطعی اینترنت می‌سازیم
🎧
🤎
اسپانسر ویدئو:
کانال تلگرامی ذغال سیستم؛ فروش لپ تاپ و لوازم جانبی استوک وارداتی دبی:
https://t.me/ZoghalSystem
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگانه و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/3659" target="_blank">📅 17:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3657">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ببینید MHR و mhrv-rust و skirk و flow drive و تمامی متدهای بر پایه‌ی گوگل، با اولین بادی که از سمت سرزمین‌های دشمن بِوَزه قطع می‌شن
تنها چیزی که برای ما می‌مونه، DNS هست که همون هم ممکنه سرعتش خیلی خیلی کم باشه و می‌تونید از اینجا
https://youtu.be/6Pm7kNQb3mo
آموزشش رو ببینید.
متدهای بر پایه کلودفلر مثل BPB و Edge و... هم که یه پله بالاتر از MHR و اینها هستن و طبیعتا همیشه بعد از وصل شدن گوگل، وصل می‌شن.
هرچند به WhiteDns هم نمیشه ۱۰۰ اعتماد داشت که برامون بمونه چون توی هر سری فیلترینگ ما غافلگیر شدیم. مثلا ما به هیچ وجه فکر نمی‌کردیم بتونن جلوی Paqet رو بگیرن اما تونستن. هرچند امثال پترنیها هم با SNI Spoof، اونا رو غافلگیر کردن!
برای همین شما ترجیحا متد مستر دی ان اس رو توی Whitedns به عنوان اضطراری‌ترین راه، داشته باشید علی‌الحساب</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/3657" target="_blank">📅 12:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3656">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/MatinSenPaii/3656" target="_blank">📅 11:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3655">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-text">گروه Void Verge در تازه‌ترین
#گزارش
خود اعلام کرده: از زمانی که اینترنت ایران دوباره توسط دولت بازگشایی شده، تغییرات گسترده‌ای در شبکه داخلی کشور درحال انجام است. پس از هفته‌ها قطعی و محدودیت، تقریباً تمام روش‌هایی که در آن دوره مورد استفاده قرار می‌گرفتند مستندسازی شده و به دست نهادهای مسئول رسیده‌اند. سیستم فیلترینگ خود را برای مرحله بعدی اختلال‌ها و قطعی‌ها آماده می‌کند و روش‌هایی مانند DNS Tunneling، MITM و Domain Fronting به احتمال زیاد در قطعی‌های آینده دیگر کارایی گذشته را نخواهند داشت.
علاوه بر این، نهادهای مسئول فیلترینگ اقدامات گسترده‌ای برای ایجاد ارائه‌دهندگان واسط انجام داده‌اند؛ سرویس‌هایی که خدمات خارجی را با محدودیت‌های شدید در اختیار کاربران ایرانی قرار می‌دهند یا وب‌سایت‌های ضروری را که امکان استفاده از روش‌های قبلی را ندارند، از طریق NAT در دسترس قرار می‌دهند. در چنین شرایطی، انتشار عمومی و علنی روش‌ها نتیجه‌ای جز آسان‌تر کردن کار نهادهای فیلترینگ ندارد. این سازوکارها باید دور از توجه، به‌صورت کلوزسورس و کم‌سروصدا فعالیت کنند.
در همین حال، مافیای اینترنت در ایران بیش از گذشته قدرت گرفته است؛ مافیایی متشکل از افرادی با دسترسی به «اینترنت سفید»، برخی ISPها و مراکز داده که از طریق سازوکارهایی مانند سرویس‌های پروکسی و سرورهای اختصاصی مجهز به NAT، اینترنت نامحدود را با قیمت‌هایی در حد صدها میلیون تومان به فروشندگان VPN عرضه می‌کنند. این مافیا آن‌قدر قدرتمند شده که توانسته بر سیاست‌گذاری‌ها نیز اثر بگذارد و حتی در شرایط بحرانی و دوران جنگی هفته‌های گذشته، به حفظ هرچه بیشتر محدودیت‌های اینترنتی کمک کند تا منافع اقتصادی خود را حفظ و افزایش دهد.
برخی شرکت‌های ساده میزبانی وب در ایران تنها طی دو ماه قطعی اینترنت، به فروشندگان بزرگ VPN با درآمدهای بسیار بالا تبدیل شده‌اند. ما در هفته‌های آینده به جمع‌آوری و انتشار اطلاعات و داده‌های لازم ادامه خواهیم داد. اگر این روند ادامه پیدا کند، هدف بعدی باید مقابله با مافیای اینترنت در ایران باشد. امیدواریم این روزهای سخت برای همه ایرانیان به پایان برسد. آسیبی که از سوی دشمنان داخلی و افرادی که زیر سایه جنگ از مردم سوءاستفاده می‌کنند به جامعه وارد می‌شود، گاهی از خود جنگ نیز دردناک‌تر است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/3655" target="_blank">📅 11:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3654">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دوستان برای هیستریا، سرورهای AWS آمازون با این سرعت جوابگو هستن چیزی که من دیدم و دوستان گفتن و متأسفانه دیتاسنتر دیگه‌ای ندیدم که به این خوبی باشه. آمازون هم گرونه به شدت
پس از آموزشش فعلا منصرف شدم</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/MatinSenPaii/3654" target="_blank">📅 00:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3653">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شمع Iced latte</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/MatinSenPaii/3653" target="_blank">📅 23:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3652">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/twpJDRfiYs197oIip4i6J9yT2HfrWES-56WtjgItufNjWR2wceJ5gjAh5PIexfD8Lg_Af1FAAbiHPdOkOhcJWK0P3s73KKxUjuPAK_V6CErwWc9OWSv6Jk4etrsea0nbX2Ab73wtI5ji1qmZJ8DEZTrBosSwDWV2yej0CcVWcEdveaOpMk2y6deJ5qnETG4uZLNagVdpoHBmGNEJrrMNnB-9Ul8XHPQ2km6z3FclL0FnjAPUn7ORvZmqHun2gwNf0nb07QxwiOFJuw9I5WSp3LnKDL2Fjo7YiH4e7CevxlgYiCh4CYK2TEyT5MyfJjtrf143MKPvHoLKjw4gnJN8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ارور EOF و 403 گرفتید یعنی گیتهاب هنوز روی اپراتورتون مشکل داره و این یعنی اسکنر نصب نمیشه(باید با وی‌پی‌ان بزنید). طبیعتا وقتی دستور senpaiscanner رو میزنید not found میده چون اصلا چیزی نصب نشده</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/MatinSenPaii/3652" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3651">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux  دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/MatinSenPaii/3651" target="_blank">📅 20:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3650">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ORonWV6EOCZNHg1onjkRLyHO1-DS2U4U-ClfHIo0tE3fek0OhpNTDLsgH1xd4zgCL4hN_6vNNfq5v_im6TusGeT97sf1gI00zU95h1GljmW0rEyDYhd4ZRAR0hATpVV1VKRSoxcfqj-Sed-_OE8Rq0xs-apnNVgI5jABcMSuMHm9-TWMXCobqfge3Jl42SK8QCzl0fYXmteEcnEW0TrHoYFJhwRB8P4qfkH1WDRW0tijNSvNl_Anaoa5FosRxdEyjsqANXMa-CAEZthXVxHovTjhjFNGbmPjVKd6buP3Rfk6v6oIo58EN44bagi8WdL3xTe8ivqWF2QiA3N_73A0DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر به این ارور خوردید، پروژه‌ی جدید بسازید. اگر باز هم نشد، با یه اکانت دیگه وارد بشید و مجدد تست کنید. توی این ویدئو
https://youtu.be/_aXy8wwyRG8
به همین ارور خوردم و این شکلی حل شد</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/MatinSenPaii/3650" target="_blank">📅 19:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3649">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux  دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/MatinSenPaii/3649" target="_blank">📅 19:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3648">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون متصل بشید</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/MatinSenPaii/3648" target="_blank">📅 18:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3646">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MNl_jxfSr6QOJV6IjnfikbmY5BeXBqHsn7nvXQN8X_sk58QBLlQmxD-ccNUsoSWZFi68q88Bqjpv7aZzMhmfaj0GngQx1XWcSs-pzWQgFsb1gYCgXrvlVjFsQ5txILFxO7fGiMYoDulSesO0QB2Y9zQf0EW3FGJPYTeq_DeTmd1J-fdNGLscOGXvBoaJGaTszT0J-n6dwN8161QgBjqJuv9mXNjnPcDrB2Hd68UjAE8y1EuvCyySGwc38kRkPYHWLRqsq5lKR83IrL1OkvDQNm51oPvbpU6GAL7Pxbe7fTEQ6a0osD-FquxPb6jlY6Zn_akuCY565zWNf0zbZRf7xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Kt_7PWmGLOASbw9ZZBRFS7fwGAlpndDiZU_whm4nG4eBzbHKtMxqX8eaA7X-5dC5KOMMaePdMaxk_hhzQ_6RCB2i1EAj_J2CT1V8Sj5CZP7Lx-kcivfhY1s39QsJDTvJBe8FBe30UclWle5su9coqPLoh8MF_ESof2XkCy8GJFdYYgdR_wJhwGEva2xyHstUPHNod5g9bpnmkW8eD8AM5RZ1npgrh0rpywMDQfuU3RzzBDHR8SFO8g5yU6S3u8hWfHhz9yBtFBYn2fk-b8HW0JnEflMtxEANspb_s8HA-UkAKKu5H6pAYky1KNh-x-oXmCIQ0JREy5o1svo1f4kseA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux  دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون…</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/MatinSenPaii/3646" target="_blank">📅 17:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3645">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V4-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">6.2 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3645" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لیست جدید 33 تایی از کانفیگ‌های Spoof که همه‌شون کار می‌کنن و خودم تستشون کردم</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/3645" target="_blank">📅 17:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3644">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">base.apk</div>
  <div class="tg-doc-extra">11.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3644" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اپلیکیشن RSTA(که به زودی اوپن سورسش رو هم میسازن عزیزان)</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/3644" target="_blank">📅 17:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3643">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-on-Phone.txt</div>
  <div class="tg-doc-extra">350 B</div>
</div>
<a href="https://t.me/MatinSenPaii/3643" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دستورات اسکنر برای Termux</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/MatinSenPaii/3643" target="_blank">📅 17:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3642">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux
دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون متصل بشید
⚡️
لینک سایت کلودفلر:
https://dash.cloudflare.com/
لینک پروژه‌ی  Edge برای ساخت کانفیگ رایگان:
https://github.com/cmliu/edgetunnel
فایل دستورات ترموکس:
https://t.me/MatinSenPaii/3643
پروژه رسول:
https://github.com/seramo/v2ray-config-modifier
نرم‌افزار RSTA Spoof هم اینجا:
https://t.me/rstasnispoof/2/1076
و
https://t.me/MatinSenPaii/3644
⭐️
توی این ویدئو این مراحل رو پیش میریم:
1- ساخت کانفیگ Edge(روزانه 6 گیگ رایگان با کلودفلر)
2- نصب و استفاده از Termux برای نصب اسکنر من و پیدا کردن آیپی تمیز
3- استفاده از اسکنر SenPai Scanner برای اسکن آیپی تمیز کلودفلر با استفاده از کانفیگ‌های Edge
4- استفاده از پروژه رسول برای انداختن آیپی تمیز به تعداد بالا پشت کانفیگ
5- استفاده از آیپی‌های تمیز توی Json  اسپوف و اتصال پرسرعت به اینترنت آزاد
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این متد نیاز به هیچ سرور و دانش شبکه‌ای نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
(با کیفیت بالاتر)
💰
دونیت</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/MatinSenPaii/3642" target="_blank">📅 17:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3641">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KwZ-1HQ_WV9qm9tAOAN3PGRXHdjT4i8Xs_AVlzYvMiP0ugJ0PZr5xX4JNXUirZX9z_X2i2FmalfG_-nGmi0N_EB9AJLA5SVsVdOHexsWZMwJc-q4F0DT3VfJ1X3ZySn94VyP654WEJ_6xfivOWvTpzAMqtOmCB_NvB1vmzXXsfcJ6ts-cTbEG8n40v5FzQ_QCYjYcKMM0DYgoh6qlPJQDfD5R-d88KAAhifjlodB7-MoPMHiteevND0gIQMguM34tz5pHF0ZxemMBeALY4EQR4Z4dqC1gOjxxqBkQiefmAFni-vkZMFY9e3aVCJlib4Mzqf-08HYZvLH25bGHLb0mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ربات از
یـ‌ بـ‌ خـ
عزیز واقعا باحاله. یه نگاه بهش بندازید:
@iNewsSummaryBot</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/MatinSenPaii/3641" target="_blank">📅 16:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3640">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تصمیم گرفتم یه آموزش صفر تا صد ضبط کنم برای عزیزای دلی که لپ تاپ ندارن و فقط یه گوشی اندرویدی دارن
از آموزش ساخت کانفیگ اسپوف گرفته(رایگان)
تا اجرای اسکنر روی ترموکس(سردرد)
و استفاده از اپلیکیشن اسپوفی که این دوستانمون ساختن
یه مقدار طولانی میشه اما دوست ندارم واقعا که بچه‌های اندروید کارشون لنگ بمونه</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/MatinSenPaii/3640" target="_blank">📅 15:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3637">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LfatWHUFbb2fUhw7ld4DuQ7xWKZaUwLScdL6eJXtPpRm9kdrnOA9RJYE1UUwS-ODl25_J5j5JqmI3Zc-vXspcf2y2M-MSaJmLYmL99bpt4BXWQsgHj2l_5ngIQs_fAhdKTE1U7XlZxFVxMd96dRSLfMs69Lr0K6KcG_OYqvI8F_BDXp1JUxYe5OfeiFfZoZ688Jr9q97bii_FKGx0CdF0XFuySC-WAmvMJ7RGDTFyndWjVCP6IWc8mgX_MFEX82sTQzfaWFJ6w4RlF9VEoccnDn-m-0phZVAigATDXdhjTeDzaHM6GWzV-b7kurwRFxL0uox04nRyYkeB8tH0YsJ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LsrB56QJjt5w7R77D-0YcXl9qW3Qquxo7Z2uQOLu5fhcgukWEMiSdiVx6a0xy-zlvL80q1uXKe-OzIrLTa_7m1govgiSxQCtF4mLvi_pTBdKJfsMWy9_Xi8JAITHHe2pscFJKl7TiCLocSrDCAL9YImLlH0bZkIHzV-HcIApzjv_3LiTDbY75fsWteAxp1-fSWLIQEISdxWErWIY2FucGV4GXgYAAnEGhs7NgO1RGS6ZA1zuaPfZKGNZGHLzdx42KFIA9ALbxDCxzmvrBEbB-GaMhYg53nIPROwLSMfN0YRMKiHVRIMRPQGRKMm5w3ESrwgSkh46qVcw16ROUgl1HA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز راجب اینکه چه شکلی می‌تونید کانفیگ اسپوف شخصی بسازید و روی گوشی چه شکلی برای Config-Json می‌تونید اسکن کنید با ترکیب اسکنر من و پروژه‌ی Shin، ویدئو داریم</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/MatinSenPaii/3637" target="_blank">📅 15:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3636">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">📱
اگر لینک ساب WhiteDNS رو میخواید از گیتهاب داشته باشید، این ریپو هر ۴۰ دقیقه با بهترین سرور ها آپدیت میشه
https://github.com/iampedii/whitedns-sub
لینک ساب برای Clash Party & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
@WhiteDNS</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/3636" target="_blank">📅 13:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3635">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">امروز راجب اینکه چه شکلی می‌تونید کانفیگ اسپوف شخصی بسازید و روی گوشی چه شکلی برای Config-Json می‌تونید اسکن کنید با ترکیب اسکنر من و پروژه‌ی Shin، ویدئو داریم</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/MatinSenPaii/3635" target="_blank">📅 13:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3634">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2a4acd74d.mp4?token=cwEkS_CCsNeJTVuqT9E-zKqF0TFr35zXWBCtZiy8M0PLlEN6IR0ioVBM5Gh6SURDVXF_frJV_wL3WBZ6bzuusVBSwRAVJXDJRVHDix1FqHw-QzPhShl8lPzYw-2MPnMlg6S_CxqQcUrZEs6urtHZMaYhD5rALV9b13OfXaR9XQuO_zhqGBKJrmvsz2p94BRAUWi8i0PRjnHngugualBTUN0FYaf4irEmCz0zxDP60260WnwZSkJeu9F-kpmstY6F5nnyFFylRbNdLFTR1BzZKzimBFV0v9t7fQ4Yx_F8GODqTDo28jArHd4TOwgg4Y0mfesEJOHr8Sp0slt1D0QOC0mwvd_44riB2pNA9gL5dhXbqVnTG3lIhq1B0Cuu63N9UK9lKEVBRGjIcPnUwW1bBB12VoOqY1FFU2sg877gqiBsN_QS-Y9joMQ_lEyiIyC7M-nOGOAH1M2T2pdCKu2pKopbq0ZZp1Vp4mWRf1B68W9AL83YxtOFBaYTeSwfWHJpvv9J7veYjBQ7nWXiM9UfxAAHvmMJUUSBKsKqN0-v-XmRWeA3zHZfjFDu7JzkhBq4dsqauNgy9hUF66WPjXtU83S2zuYUQfo-qFkT8WwI9sbsj445QTcd4eOk7Q3PySK2W_G8HZix2-zkk0cNn3EevpqPUqKF-tyTeDzl7zBcYmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2a4acd74d.mp4?token=cwEkS_CCsNeJTVuqT9E-zKqF0TFr35zXWBCtZiy8M0PLlEN6IR0ioVBM5Gh6SURDVXF_frJV_wL3WBZ6bzuusVBSwRAVJXDJRVHDix1FqHw-QzPhShl8lPzYw-2MPnMlg6S_CxqQcUrZEs6urtHZMaYhD5rALV9b13OfXaR9XQuO_zhqGBKJrmvsz2p94BRAUWi8i0PRjnHngugualBTUN0FYaf4irEmCz0zxDP60260WnwZSkJeu9F-kpmstY6F5nnyFFylRbNdLFTR1BzZKzimBFV0v9t7fQ4Yx_F8GODqTDo28jArHd4TOwgg4Y0mfesEJOHr8Sp0slt1D0QOC0mwvd_44riB2pNA9gL5dhXbqVnTG3lIhq1B0Cuu63N9UK9lKEVBRGjIcPnUwW1bBB12VoOqY1FFU2sg877gqiBsN_QS-Y9joMQ_lEyiIyC7M-nOGOAH1M2T2pdCKu2pKopbq0ZZp1Vp4mWRf1B68W9AL83YxtOFBaYTeSwfWHJpvv9J7veYjBQ7nWXiM9UfxAAHvmMJUUSBKsKqN0-v-XmRWeA3zHZfjFDu7JzkhBq4dsqauNgy9hUF66WPjXtU83S2zuYUQfo-qFkT8WwI9sbsj445QTcd4eOk7Q3PySK2W_G8HZix2-zkk0cNn3EevpqPUqKF-tyTeDzl7zBcYmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از دوستان زحمت کشیده یه آموزش ضبط کرده واسه‌ی اسپوف روی موبایل. چک بکنید ببینید موفق می‌شید بسازید یا نه:
https://youtu.be/spTJKgafNV4</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/MatinSenPaii/3634" target="_blank">📅 13:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3633">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aTbe1s_xfv5ukth1ntb78ks4cDr-G0ee5kU1WdNhwvy6JBJCK0wbKDzi4eZP0JZwhAKuH2oLDrQJulPRIr9eCmDdJHEFWxJ3rBLYEC5SLO8phMqCrYsPS7f-oFfQAh1qPFNY6BvrPrAaqeaCDkOPQIauKREbrMlp2Dga3pN4pltzInZHUsn30Bv4K8LCPhKX_omokACnQf5fmbqgFSCDgmzMKnRnMrQvmg11MFeC_EYUIJLUHNZJ82ei993GrAqQ30IXfU9tHQDwTEpwumSmlw_WNanMrKkadgn-ZP-dm7CHy40wwnGvmjfFiVqGZ9Vhzpqm06ZBu-OK3fYYMi0IPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی  از این به بعد می‌توانید از سابسکریپشن WhiteDNS در اپلیکیشن‌های زیر استفاده کنید:  اندروید: FlClash آیفون: Clash Mi  با استفاده از این اپلیکیشن‌ها دیگر نیازی نیست تعداد زیادی کانفیگ را به‌صورت دستی وارد کنید.  ما در سرورهای WhiteDNS بخشی از…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/MatinSenPaii/3633" target="_blank">📅 13:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3632">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnAHlskZCa1pOvbRw36NoLjzlwjMEln3TYsyUoyhApM6SHvDJEDjfQCRpT6DxbHXFcIrd3qJH-L_UYhg5MqzHtMJx0hLr6dd368LED95-23zRuCcDOPytB7pSpCAmRTUkEKUKRARnKWiVrQHusayXk9DqXMTZAgqhEsJRvwram0KXBCKqu0BjSWx1lpEi-QhBF5MTjmJpdP-wMppU2lfXaJn7OSKKXdUIY9vKXjg1ZM1BN6xQdEQ6XKA4DCx_ZGRvE6lrmnknyoGG5hvbxU6jashO_sgjqXD1uBhIOBoEOjP5Yepm2gzRboAHqArg6FlrhtRSkZMyK1VX0hYkwsoOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی
از این به بعد می‌توانید از سابسکریپشن WhiteDNS در اپلیکیشن‌های زیر استفاده کنید:
اندروید: FlClash
آیفون: Clash Mi
با استفاده از این اپلیکیشن‌ها دیگر نیازی نیست تعداد زیادی کانفیگ را به‌صورت دستی وارد کنید.
ما در سرورهای WhiteDNS بخشی از کانفیگ‌ها را بررسی و فیلتر می‌کنیم. سپس اپلیکیشن موبایل به‌صورت خودکار از بین کانفیگ‌های باقی‌مانده، بهترین گزینه‌ها را انتخاب کرده و به آن‌ها متصل می‌شود.
لینک WhiteDNS Sub برای استفاده در این اپلیکیشن‌ها:
https://sub.whitedns.one/sub/mihomo.yaml
لیست سابسکریپشن ما هر ۱ ساعت یک‌بار به‌روزرسانی می‌شود.
دانلود FLClan برای اندروید، مک، لینوکس و ویندوز
https://flclash.cc/en/download
با تشکر
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/3632" target="_blank">📅 12:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3631">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">MITM-DomainFronting.json</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/MatinSenPaii/3631" target="_blank">📅 01:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3630">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BF2hfkCpEizhGm2qMaRO8zfbtqBeamVp_Q-VEOrXmO59ZLsOcxqPF3fa9S0OMJI6yfX8_grybuu6v3QyUZ0Lk4nvqUIryV7hbT-nCApIM--Ic9oiek2EDwhyblyNQdVgDkYKvFsQzUEmtt8obAjyYyqq_cF2V0uv6pfxGRZ1qFT1eJQNrT1ZfoSaH8nUNdqXuqUM2n3smdj9n2-EL3adqp9OWlmgZkhUIK5J5yTqANxqE7eLgMtAx2hhYLcBTAsgY0-8cC75d2lMBfLynT_9kXISRIiZb0Oqw0FQrG6exfJ2oJ6qsKr8bbMcF37Le40bci62FIaNCYJFbUGr2y7AZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب رفقا آموزش شکست خورد چیزی که می‌خواستم بهتون یاد بدم فعلا بسته هست و پولم حروم شد
😂
خوبه ساعتیه باز میشه خاموش کرد سعی میکنم اگر راه خوبی پیدا شد مجدد یاد بدم اینم بگم که paqet و gfk کار کردن روش که خب قبلا آموزشش رو دادم(ویدئو سوم و چهارم چنل) به راحتی…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/MatinSenPaii/3630" target="_blank">📅 01:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3629">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دو ساعت درگیر این بودم که چرا x-ui بالا نمیاد روی آروان، می‌خواستم یه آموزشی ضبط کنم واستون بعد دیدم ipv4 سرور با چیزی که سنایی به عنوان ipv4 شناسایی میکنه کلا متفاوته و من سعی داشتم آیپی‌ای که وجود نداشت رو باز کنم:| هیچ ایده‌ای ندارم که چرا این بلا رو آورده…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/MatinSenPaii/3629" target="_blank">📅 01:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3627">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aFW87jFDp2gPxVzitx7QPOqBLAeNXQYcxPIvNYP_4FRadeevcUVKrZGAVS3735Vz9OKmNEKT42TYFzZhz5jWcjMdfqfy_ZcvN4szfBwnyqBWFEp5LCTvOngFUQ3qQsx0j2qhlErBcC-UnkdDRJMhmkvrnxlIY5UkvICvRjQnSXhe7tuMoHqUGDREOYf-zQ_gPj3CbnXagzmUrdNm3QWnUwNv-oBJjWyAsSVA028d5HCS7YY6IDc3b1nqKVX--PxD6r9i0oMy61NqOtwrRNksf5vxpj7C5D_hi2dIZc05Us9PtdOUJXtGaT3ZwSv6-O_rIyOi0M5ldRpLNNWnEDjDhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Olh7o_rsqBZcVPd-3pDpxeNkaPTGM3hkuI6PNTaARWw57Pt2qL2G27cs-O5ZEFrcbDrfL1KwQ2B_nOY_pO-A6O9ellwTEdOyh4_dg2Bj_1SmqsaY7rjMq_wNnCYmxhE2YC_lAFwK-guqavbS0dZdHJYma277MDgd3pvlpCD63zdTxBhMJbOyLuJQ35OkXUN3COJe7ba0tyodrc8K-PMwBPGjCowPAN0QrBdhcFv-5coaXafjxQQSOKw0yHyKFE2SwpmT10R9I2gXWWAJwEjM_PCK8GO-phsHK5NLcqZBsLYNlG7X7rIagzu_2lkjAAuk3L4X1w3iXox_nz0l23Xa-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو ساعت درگیر این بودم که چرا x-ui بالا نمیاد روی آروان، می‌خواستم یه آموزشی ضبط کنم واستون
بعد دیدم ipv4 سرور با چیزی که سنایی به عنوان ipv4 شناسایی میکنه کلا متفاوته و من سعی داشتم آیپی‌ای که وجود نداشت رو باز کنم:| هیچ ایده‌ای ندارم که چرا این بلا رو آورده آروان سر سرورا اولین بار بود با همچین چیزی مواجه شدم.
و اینکه با سرور فروغش من تونستم به گیتهاب و اینا ریکوئست بزنم نت بین‌الملل داره. نمیدونم از کی وصل شده</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/MatinSenPaii/3627" target="_blank">📅 23:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3626">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UvNKT63VI2NypJbvvGgI1um0Zs9TYGMvoSX_3ugi_sn1R3VGWNA_AuItMJgti30-kEEvLvzEjbW88RaidUMu2uKBTn2PaeSkmIX6M4ykoWCKHfOCnFyKLopuS0bJerKMjGtiHlxomMiYYdnQjiV0VGrYiPTkuDV25OM52mkNzokM26DviN0It-Pni6V_1STcwjb2vw9K8V549N2aiAIjDiBicD4z0FNTOxdHQkYlhT1Suz_TpUsgIhxvkhzzF4ypTXjJCyGUaUaEVWAejmlkJiYIORRfIud--ImgqYSZ7RKyPM38HvzXon0YKH8e7E7OE_8ACzsm6wrPs5zE9MrCKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرسرعت‌ترین کانکشنی که میشه از یه سرور خارج داشت، Paqet مستقیم روی سرور ترکیه سه دلاری Yotta
😂
با paqctl
سم ران کردم روی سرور
با آموزش اولیه‌ام
هم روی ویندوز ران کردم</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/MatinSenPaii/3626" target="_blank">📅 19:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3625">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ShadowShare منبعی برای پیدا کردن سرورهای رایگان ss   vmess   trojan و...  وبسایت https://shadowsharing.com اندروید https://play.google.com/store/apps/details?id=com.v2cross.shadowshare ایفون https://apps.apple.com/cn/app/shadowshare/id1612647259
📍
آموزش استفاده…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/MatinSenPaii/3625" target="_blank">📅 17:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3621">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShadowProxy66</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fYWgg0VbM9BkfkjrJS5QavoqgA-sUb3hqOTI7srU1tNtWZFCDDjqUAhfk_jRF4u0Q8JPWL7Zjjgu-fsDDE25-DWnNEe1IhQTrRnyGB5wq0xeKzvuMpwG_7aFewBoZq70TiQ3Wq5X8BD7_iDZi8uWfNhtkdnayGum_9Y8XTBQjbtf0uPbHmldZ5z7SbTipv5G7O6db7qgQwkwjJ4VCMYnD1TBe9VzO8-PvwjsMYHQ_mEBKfUSvhQ6XbDnnJ2l896NqJU7xUdTFkrNe-Izd-A_hWxQGuY-TKBk19bsy9OxHt72juZ0P29rHPzDAMHDSYgU5_58KWG3kqDHrRul-PW2Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lq2ZkvyHhxlVMUiA9FAv2B1DVINKHQlK_blG-aQ_l5K5KBWvPZmF0e4M3zctmM3uyM0KH0TUPOuyDlGF4bVO9OgGgRQbExBUe6xqpONE_8oOWG0eV6FKJ_jO4kTv_ZHb1b8gnTNxTUnNoiGRg_cHlVOd_TlRUS7Mhn9T_eQdwLHz1hiB_8UL-ekgv4nH7DIBQy-Q5EVkQcE0duIvqP50CFxXzFaM7KoSvuZ52fgP5uj5o0NHesOdx3kqotjbdZP1v4DxE7EM4NOy21BfFrF0Ftfqy0V9G0zuC_EY6CV7nvYOkhjk4XXBEUgxH5Pp8_DJ8jPkIyrQ9uABPix04bIjqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S4EzY0rdK8X57wybWnnQ7bkepnQApZv-b4fG5e0bBc1dWtCxx76TPF4FHGUk7Rb1qHOBMdImEKKYOYzEp7wORmAxd1AcLDBt05f-C98a5vbAIr8j3IiXaItekO9vwrdVZQwmFYg7trL84A38VVaAsFkJJMk8wvRnluAc6HU-btDh3XIXoVr54k6Ud7Ya7oGMbKsIQiKyJymuCeWjuV7EXzxA3MQrOZxIWZP6uA_m15Wba34rmxVcyBn3rH4px51QHKlpab5yMmGAVZr0LWN9abyp0uiUv9_0u12H7ptC_VaFGAjf_387NKzaRnGgV4wXOqcOWK81q3Ov8TWlYwbYFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UuOjfd0KL31RGgYcYOwM0s38kutMx83GxdG0OGB7fL36dSNYOGcy2-MwORUVFbVDLvdogfPsYWZPup7TuhfvoU_ZJiDXp4ZFvljp3sFzmsWNKFLF9Je5OPyD1Y3iOI0zjBDNC5p7bhQ3TK_qFVgaSYA4URsPsUnRDruMv3IGp2WKWXUomFXZY5SgQPG5Sj1iBsaj7RG-hgu3-n0ROMZTyquzQJUjcyOfvkBbSZrh65MajpLdUfnYf4dFkNnds5JN2knus7JF7G-8qS4bUI6t2QSWVLwlZNu1ACifdNBnhwQX7VXYxLlGtNBPOWo0Pl4GO1XEzFtLS3GelHlq93xt0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ShadowShare
منبعی برای پیدا کردن سرورهای رایگان ss   vmess   trojan و...
وبسایت
https://shadowsharing.com
اندروید
https://play.google.com/store/apps/details?id=com.v2cross.shadowshare
ایفون
https://apps.apple.com/cn/app/shadowshare/id1612647259
📍
آموزش استفاده
(توجه داشته باشید کلاینت یا فیلترشکن نیست)
🌐
@ShadowProxy66</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/MatinSenPaii/3621" target="_blank">📅 16:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3620">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/azq6kMeC79iUB3tduftquu83Cpc0wDfdQzkkkOAQIEpiHPmQb2NQ2zIhx668gIlZ25ECOOYE6NDiOIVbAgPFPmkyx1-A1QkP_pmpfHr_b3xkKD8cI7gJ1OKhGbDs2Wy1mBuP23AS7T_5seKjtWmHa057yM64ttJq7OVpeExVXtEkBtH6iDfxiMV5QTRNL_i94S1-3ap1x3D3w-MeXoZ8JEgayshf3y_uigaGclyqea9fg-zB2xZ8SyjPwp3CJ6Tgrks2L2qIvMQceVbJ62xNWtgWDsJMxIxXr-r4vfYc6z05YxUbHyI7r7UBArDkVW7laRQrhTD1JpHF4kRXnLYrSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/MatinSenPaii/3620" target="_blank">📅 12:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3619">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">من الان با این به Spoof وصلم:
{
"LISTEN_HOST": "0.0.0.0",
"LISTEN_PORT": 40443,
"CONNECT_IP": "104.17.89.5",
"CONNECT_PORT": 443,
"FAKE_SNI": "www.speedtest.net"
}
به جای connect ip، میتونید هر آیپی وایت کلودفلری که از اسکنر(
https://t.me/MatinSenPaii/3598
) به دست میارید رو قرار بدید</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/MatinSenPaii/3619" target="_blank">📅 12:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3618">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اگر می‌خواید گیم بازی کنید، می‌تونید از این کانفیگ‌های هیستریای مسیر سفید استفاده کنید: hysteria2://Masir_Sefid@18.159.104.97:443?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/MatinSenPaii/3618" target="_blank">📅 10:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3617">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rQkvvqkJ0tGjdzqjhMbJsWtx5ngbRW_3UmCk4n3n8anWt3tq3osr2Wffv-OUV737XGQiKskrTehnKHjGPM5i1icI3JPjMI0ksQnzwSv_j_rrSqL_cv9o9JAuI4Sd2iGc3kSL_aS6zn21TtJdMk30idunb3O3KTLgFgIs5uyGy5WFjxjWS5KKOxZfnLs92OSqvNKhMMLqQ88IbfZzi-GD-akmSJKgW_4qkHOwLHMIYq9dwoGm-ew5ZUzGW_3fHHc_iQ4i5AIcRQ582kUfV_YjZsQnbGoROHeLLiNciJ_EwmUa_LbC7tLfnebaQOZkCa86YpdDMdAknNEbi3n-opOj8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر می‌خواید گیم بازی کنید، می‌تونید از این کانفیگ‌های هیستریای مسیر سفید استفاده کنید:
hysteria2://Masir_Sefid@18.159.104.97:443?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:444?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:8880?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:1040?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:4040?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
hysteria2://Masir_Sefid@18.159.104.97:54040?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%AB_%F0%9D%90%92%F0%9D%90%9E%F0%9D%90%9F%F0%9D%90%A2%F0%9D%90%9D%2B%F0%9F%95%8A%E2%AD%90%EF%B8%8F
این هم لینک سابش:
https://raw.githubusercontent.com/masir-sefid/Sub/main/@Masir_Sefid.txt
این هم کانالشون:
https://t.me/Masir_Sefid
من با همین کانفیگ‌ها توی کالاف پینگ ۶۰ و گنشین پینگ ۱۰۰ دارم و راحت می‌تونم بازی کنم.
کانفیگ هیستریا هم آموزش ساختش روی یوتوب هست، باز اگر لازم بود یه آموزش ضبط می‌‌کنم واستون. اما نیاز به سرور داره</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/MatinSenPaii/3617" target="_blank">📅 10:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3616">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5X3UcNu1lZ5u6OT8jgweseX1fSFtsBKbMibN1rQwbt_uBVyOcNWAkRoEL29sIWgZ-k-0TML-gmN78TjbMzTbpjE4nqtkmYGgFfYG4pGmMdIyU5yjD9gC0Mhnz5mw79NYYMMRaN_TuJRrqaTJk10DpfwvNBAb1byMOh-IXFRqV_xpFc0m6Fhc8AM-a688vltGcWyYYf-0BdK6NSVLthrj3tRnwlKPn1jpkG8acbzNXcMaBmrM-24gxX1bEPt8hf1S9qKubz1YldBe-IlFap2nUJe99Yb-O0EyOkUtWaZgI8JOnJqi1llbS6XO151gkFoYyPwlhEDwLMjP8S78DuL3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش تبدیل کانفیگ به آی‌پی سفید
از این به بعد برای تبدیل کانفیگ، آی‌پی‌های خودتان استفاده می‌شود.
@WhiteDNS_Installer_bot
مراحل کار:
1. وارد ربات شوید.
2. روی گزینه «تبدیل کانفیگ با آی‌پی سفید» بزنید.
3. کانفیگ V2Ray خود را ارسال کنید.
فرمت‌های پشتیبانی‌شده:
VLESS
VMess
Trojan
بعد از تایید کانفیگ، ربات از شما لیست آی‌پی‌ها را می‌خواهد.
می‌توانید آی‌پی‌ها را به این شکل بفرستید:
8.8.8.8
104.18.1.1:8443
یا با کاما:
1.1.1.1, 8.8.8.8, 104.18.1.1:8443
نکته مهم:
اگر پورت وارد نکنید، پورت پیش‌فرض 443 استفاده می‌شود.
اگر آی‌پی را همراه پورت بفرستید، همان پورت استفاده می‌شود.
مثال:
1.1.1.1
→  پورت 443
1.1.1.1:2053
→  پورت 2053
در پایان، ربات فایل کانفیگ جدید را برای شما ارسال می‌کند که host و port آن با آی‌پی‌های ارسالی خودتان جایگزین شده است.
@WhiteDNS</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/MatinSenPaii/3616" target="_blank">📅 03:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3615">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UKlz2Jocv3qHWJV0LbxcwMaYMdu3x5_Wxq170eMB1rNH5DmiZh1f6yDg_HfiNwv9O9mvvv20dIBjk7s822InkIxUHpkwu1L7U-8lh5KYAOxK8DEAavgFcgoTfq9MEhZWMERHvsaMHJ1FFHGZSVCAWBXWTqQGnzaSnK1z6_gv1-bixovaM5pG686CfwTtVfqVgA5YKXsKypigoGhnW6gNGb03Ss2GMOpF_vSY0gkEGp_NaiTeBHkzFWmwV7JF7F1sDjJYEOvWip2IZW2Xp_iD71HKqpf8nb1BsbRRMcxJe1CtGwAY6KMGnNuFbY52zxC3uloLj5_uFOwd52IX4HdWrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کانفیگ کاستوم دارید(ساب نرمال)، آیپی تمیز رو باید اینجا جای address قرار بدید</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/MatinSenPaii/3615" target="_blank">📅 02:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3614">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑇𝑎ℎ𝑎</strong></div>
<div class="tg-text">https://t.me/MatinSenPaii/3613
خوبیش اینه با این روش میشه رفت و کانفیگ BPB ساخت
برا دوستانی که کلودفلر براشون بالا نمیاد یا نمیتونن وارد سایت اتومیک میل بشن
همه چیز با همین نت بدون نیاز به فیلترشکن کامل انجام میشه
بینظیرید شما
نخبه های ایران.</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/MatinSenPaii/3614" target="_blank">📅 02:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3613">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MITM-DomainFronting.json</div>
  <div class="tg-doc-extra">9.2 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3613" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">☠️
(اندروید و ویندوز) رفع تحریم سرویس‌های گوگل از جمله میت، جیمیل و درایو بر روی تمامی اینترنت‌ها به صورت نامحدود  این ویدئو، مقدمه‌ی اون روشیه که برای یوتوب گفتم و ویدئوی اون هم پشت این ضبط میکنم و قرار میدم خدمتتون.  لینک داخلی ویدئو: https://up.theazizi…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/MatinSenPaii/3613" target="_blank">📅 01:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3612">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/riKB9g1UhEGO32omB3fOcVdPYSWwZw7kYWVg0ZpRVLrt6SM5UbvMVAyU_CvqMV7cQm_cQRWSmmA320TjqEBJjAN_V7atmIJdtv4MpwXrhYgRItZ772VVz9eixY6HjEBZB9CkSLIAqVyZr47u-peAFl6p_Ipbr0dXPaTA1RppVGvCcU6Vcl38MbHLdO2fTgPWaR1xBENyJ3p_ri-ut7TRNU_R8UFbh2IFa4iy27poJDi14lZFThMdWOL-2ym8jOkWdsfrgTyiXAPV5AZmAQFOqelnoflZAwGF1PjkYeH5cVA3WMZ9Ffmb02T3HrDKVvqsF1TW8u8VlN_N6YsR5YxyQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیستریا هم روی اینترنت من باز شد</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/MatinSenPaii/3612" target="_blank">📅 01:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3611">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Mr Lou _ Ey Iran | مستر لو _ ای ایران (Rock Mr Lou Version)</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/MatinSenPaii/3611" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/MatinSenPaii/3611" target="_blank">📅 00:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3610">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دوستان اگر از Undefined در نمیاد،
1- صفحه رو رفرش کنید
2- حداقل نیم ساعت صبر کنید
3- اگر نشد، پروژه‌ی Worker جدید بسازید و دوباره مراحل رو انجام بدید</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/MatinSenPaii/3610" target="_blank">📅 00:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3609">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3609" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3608">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/MatinSenPaii/3608" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3607">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/MatinSenPaii/3607" target="_blank">📅 23:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3606">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pTfGygSeP1NORGNRKN-YOQvcADR0kk3YZYw3xtsei4s5pyjfPbmpivRpkeLkEbNhXFubB509OHjAaxVNl7ELkVJ4uZ8jtmEQEoegnSmS27fJ2AuwJtwUk9yU5ZlWdvad_8Yqths9wILbxkV31dZ6AIl3hbtJAHD0aMoVsit1YXsV8yRzDpRXu4NEh8vlMZZp9rhTkHiCSmxKz-LfzdMTUiGzBUl4rCgvNK9ZzEOCIKP46gZTM1EtfrY-arTBUiPo3bLmeceFfm4DRUMVecXkHNgiHCqImVTTIDOwIagQCkSIPt2AoHQEPDo0mfitmI4cArzGBbfUMTpNOfsbRdaVJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای SNI Spoofing
SNI =
www.speedtest.net
IP =
104.17.148.22
✍️
Kharabam</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/MatinSenPaii/3606" target="_blank">📅 23:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3605">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/MatinSenPaii/3605" target="_blank">📅 22:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3598">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">31.8 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3598" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ورژن 0.5.0 اسکنر
راهنمای نسخه ها</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/MatinSenPaii/3598" target="_blank">📅 22:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3597">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر:
https://t.me/MatinSenPaii/3598
پنل BPB روی گیتهاب:
https://github.com/bia-pain-bache/BPB-Worker-Panel
پروژه اسکنر روی گیتهاب:
https://github.com/MatinSenPai/SenPaiScanner
پروژه رسول:
https://github.com/seramo/v2ray-config-modifier
⭐️
توی این ویدئو این مراحل رو پیش میریم:
1- ساخت پنل BPB ورژن جدید
2- رفع مشکل پینگ -1 کانفیگ‌های آپدیت جدید و درست کردن تنظیمات کلودفلر برای کار کردن پنل
3- استفاده از اسکنر SenPai Scanner برای اسکن آیپی تمیز کلودفلر با استفاده از کانفیگ‌های Worker
4- استفاده از پروژه رسول برای انداختن آیپی تمیز به تعداد بالا پشت کانفیگ
5- توضیح حجم مصرفی و استفاده از این روش روی کلاینت‌های متفاوت
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این متد نیاز هیچ سرور و دانش شبکه‌ای نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/MatinSenPaii/3597" target="_blank">📅 21:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3596">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">جریان اسکن از اول طراحی شد تا هم راحت‌تر باشه، هم نتایج رو همون لحظه ببینید و واستون Save بشه. همینطور یه الگوریتم کوچولو برای اسکن پیاده‌سازی شد برای تشخیص همسایه‌ها، و روند تست و سرعت دانلود بهبود پیدا کرد.  https://github.com/MatinSenPai/SenPaiScanner/…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/MatinSenPaii/3596" target="_blank">📅 19:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3595">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">جریان اسکن از اول طراحی شد تا هم راحت‌تر باشه، هم نتایج رو همون لحظه ببینید و واستون Save بشه. همینطور یه الگوریتم کوچولو برای اسکن پیاده‌سازی شد برای تشخیص همسایه‌ها، و روند تست و سرعت دانلود بهبود پیدا کرد.
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.5.0</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/MatinSenPaii/3595" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3594">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJvxXQ06lhvFa7jqUhaX-dzPnr9qGMSE9IU38UhUM3M917gUVV3jv4RPFImJc8-QO81WG4aeHgZsaDE-Su_YpQW8iZMq1K4vgegBZQIVsnbrsGRKaQEJlWHVULLt_j8iShszFM6zpT0n1PS3v036V2B-UmJoM5lIEZ30071Zhzqfl__rTOODq_kl0a9zcJG1XP-fidZFYOXYkvO8cQEi6YdSFpyp07_nkvo6Sa7mkbcxRcelu73Mtr2c5vvO-0MgC3IbwxekoDyzTV2NXJyRTpoUHZj3SC8NEKSKn86suWwlfaEA2Ap9eikvQkldNQqpIHsyCf3bTk-iwc36gWXNAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😊
آموزش V2Ray از صفر تا صد | نصب پنل، ساخت Inbound و Cloudflare Clean IP روی سرور شخصی
در این ویدیو نحوه نصب و راه‌اندازی پنل V2Ray روی سرور را به صورت کامل آموزش می‌دهیم. همچنین با نحوه ایجاد Inbound، مدیریت کاربران، استفاده از IPهای تمیز Cloudflare و اتصال کانفیگ‌ها از طریق اپلیکیشن WhiteDNS آشنا خواهید شد.
سرفصل‌های آموزش:
✅
نصب و راه‌اندازی پنل V2Ray
✅
ایجاد و مدیریت Inboundها
✅
ساخت و مدیریت کاربران
✅
آشنایی با تنظیمات مهم پنل
✅
استفاده از IPهای تمیز Cloudflare
✅
آموزش پیدا کردن و تست Cloudflare Clean IP
✅
آموزش استفاده از اپلیکیشن WhiteDNS برای قرار دادن کانفیگ‌های V2Ray پشت IPهای Cloudflare
✅
افزایش پایداری و کیفیت اتصال با WhiteDNS
✅
تست و بررسی عملکرد کانکشن‌ها
✅
نکات امنیتی و بهینه‌سازی تنظیمات
😊
لینک تماشا در یوتیوب
https://www.youtube.com/watch?v=vVjqNQBUGIc&feature=youtu.be
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
🎞
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور
🎬
کانال یوتیوب WhiteDNS</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/MatinSenPaii/3594" target="_blank">📅 17:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3592">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اینترنت دیتاسنترها هم برگشت بالاخره؟</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/MatinSenPaii/3592" target="_blank">📅 17:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3591">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏دوستان می‌دونستید که این روشن/خاموش شدن Wifi ویندوزتون باگ نیست؟! به‌خاطر فیلترینگ شدید فایروال‌های ایرانه
🤦🏻‍♀️
دلیل و راه‌حلش:
تست اتصال مایکروسافت (NCSI) که فیچر ویندوز ۱۰ به بعده بلاک می‌شه؛ به زبان ساده، به‌خاطر فیلترینگ، ویندوز فکر می‌کنه اینترنت قطع شده و برای همین هی وای‌فای رو خاموش/روشن می‌کنه تا اتصال برقرار شه.
راه غیرفعال کردنش:
۱. همزمان کلید Windows + R رو فشار بده (کلید ویندوز همون لوگو ویندوز روی کیبورد)
۲. توی کادر Run که باز شد، بنویس regedit و اینتر رو بزن.
۳. برو این مسیر:
HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\NlaSvc\\Parameters\\Internet
۴. روی EnableActiveProbing دابل‌کلیک و بعدش Value رو ۰ کن.
۵. سیستم رو ری‌استارت کن و تمام.
دیگه این فیچر غیرفعال می‌شه و VPNتون قطع نمی‌شه :(
البته تا وقتی که غیرفعاله حتی اگه اینترنت قطع باشه، همیشه «Connected» نشون می‌ده.
✍️
گیک‌زهرا</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/MatinSenPaii/3591" target="_blank">📅 16:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3590">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Pp09MH5aqV5idyJT4JBuLu2J-xoPOmtGr1DtQz-Zf5KmfJ7Be9VG9OmwAUruezfaiDL6Mew3nFXzVA1oQ1dtrpBPrmdEBC_wA10qLoT7m4QJQRFc1hd0Jv88HK_6q3ggtcEV-4tnw3kDfNrpVBpBN1NPZOuJlz8PfBeG5mz81HhjIZgll8rUmqLU_HI15I6WwYlkycJMYuVdxdlDg8tOlqEMn4447lBxQG6KQE0VG-Pz-CncqWEHPP-_YmkVqw3wDl0mfoOYoIJ94Gvw0dTCb1Nfkeu_CaQUVlLiz4zRaSUV-xUXsklw8xsqnF4lT62w1w6vfW2IALoEhnyYioICyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه به این علت باید حتما اسکنر رو توی لیست سفید آنتی ویروس قرار بدید. ویندوز دقیقا این بلا رو سر BPB Wizard هم آورده بود یادمه</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/MatinSenPaii/3590" target="_blank">📅 10:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3589">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">متشکرم از دوتا دوست عزیزی که 105 و 3 دلار دونیت کردن. من تازه ولت رو چک کردم
❤️
مقدارش مهم نیست. کم یا زیادش یه اندازه ارزشمنده و کمک بسیار بزرگیه به من. ازتون ممنونم</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/MatinSenPaii/3589" target="_blank">📅 09:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3588">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.4.0</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/MatinSenPaii/3588" target="_blank">📅 09:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3587">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مشکل bpb هم به کمک دوستان حل شد</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/MatinSenPaii/3587" target="_blank">📅 07:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3586">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GqZJrv0LJJebzlNc0NF5P2XOcx4MCcan6SA7hf6qm87Wd4QsqLUZt_2c7i6M5E3Y6bfEgLTBYGBSIVxafFImdeYHv7tEUHjTKkcbq322lu34j_athmIQesYzJMclBNmSksPWr76pDYXFAW2mR5pcs1dR9l4SbxTfG5dhFBirhUJkrEQVJkx_qH3saF4UbsVakHiP7lLFPE39ya0oiTEkWvpgQcBW4ZoG2KVMkZCaNKJoUfTWtq6Z-GQBHDnlVIN2tgxcLJeYGIOuPkl1zkQ0eCEmA8OKNxBZXmNDuxv75S6brqFm4USFO_GpWMwzCOEZVKvgna9AfzUju0hvbe0qKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکل bpb هم به کمک دوستان حل شد</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/MatinSenPaii/3586" target="_blank">📅 07:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3585">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YGq-2JTO15vIMKvNjgtW8QD8LrOYHHroZsepgQN4O8SQj0syWqRefxXbu9HUu4NumJuiTFcZRV3Xqho9v4QyEIFVRb0TTYN-qgS-SgyUWDBxiqHIQTfYJVSU3sEFioFqkCgiQjVTxV4M07-c6iLfX85khm2UyYjNWAcqRzBw535wJSTh9ziVGx3bV2Gkj4VsiItloO7F9a9qLOalZI2WJaaHYOulEJJCPB4PXk82xz2c3dbdEds41Z8UNomhHopx96e-_xwVaC-dQzNj88pJDVEy2-rseqEwvAg1xIy1AGapIiX1kT7UQU5FLGz2u5UHnFTgkR_9wm82DowMIqNg0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگار که عملکرد اوکی شد بالاخره. چندتا دیگه از دوستان هم گفتن
نسخه‌ی اندروید و دارای ui درست و حسابی به احتمال زیاد منتشر نمیکنم چون خیلی درگیری و کار و درس دارم، اما سعی میکنم روش کار کنم با contributerها. فعلا تمرکز روی درست بودن عملکرد بود که حل شد
برای همین prهای فعلی هم reject میشن همه. تا ببینم تست چطور بوده تا به اینجا</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/MatinSenPaii/3585" target="_blank">📅 07:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3578">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">31.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3578" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">V0.4.0</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/MatinSenPaii/3578" target="_blank">📅 06:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3577">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hfqfd0swbOKaiCsy1-hSzxnejgp82a1Jhx5kDDjDHl51zSB5K_VcBvCdHcn4eMvIYkoRPRpqcaAJ7Uuknb9hEO3EubXNSCIt1GirrX0-ve_Ca8XM4PxCsTehS4sUrrWIiVYirn2_aSVXQUeX_Z0RSY76im-fh-XOx0rOJsicwWX-Qahq2rAtJXDgUmJV4C42XxFwg-qR1Zli06d7W8TDzB2NE-GBfYuKxAhOX-7b876EJ0swu5ZD_JPgWlwOBz58wXZxUmJsQeINd0x-7O4ppUPzgvr5mFIQq8rWn-Pdnj-2030ihr8S84PVWi7PJUM1E5rXQKfQaDDwLQAn1PoqEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب، فکر کنم یک بار برای همیشه مشکل آیپی تمیز فیک حل شد.
و ممنون میشم تست کنید و بازخوردتون رو بگید. تا اگر مشکلی داره برطرف بشه و بره برای ریلیز</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/MatinSenPaii/3577" target="_blank">📅 06:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3576">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qsmFp-eR7vi5IUgRYaIZ5uNzFBx8amKEUipayLYWM18DffqEI5h74OJfUU7AfVcewkI7ARVxWh8cFBY5J46tCm6ZYy-WX--ZmUb3jHZRHEQRIns5PHQPH5qapwPAmiqR6eqIUwbEBPHNiZgSYNSoUK9oteO4Odq_AM-6OLbjKyL21fV0JKDpcgVBs_5B7xCNXvywsNDSCUq-hi79Njjp6Yi6_lPYtvqzljJa0zi6hpjQNwo8MOr5-nV4EvLi7Z0GgLWer2Ku5XzXm8-tHNIPtS730TBDg2RgGYNB_UD4TsMAYv-ZspQdsX_M82v0KbTvdLUCih_ibPxKiO1qsZHcfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پترنیها گویا روی یه متد جدید کار میکنه که به راحتی می‌تونه فیلترینگ الان رو با یه استراتژی جدید دور بزنه.
منتظریم ببینیم تصمیمش این میشه که الآن منتشر کنه، یا بعدا</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/MatinSenPaii/3576" target="_blank">📅 04:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3575">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">دوستان، اگر پیامتون توی دایرکت سین میشه به این معنی نیست که من دیدم و جواب ندادم
🙏
من میزنم بیاد پایین، همه سین میشه
روزانه بالای ۶۰۰-۷۰۰ تا پیام هست و من نمیرسم متأسفانه جواب همه رو بدم</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/MatinSenPaii/3575" target="_blank">📅 03:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3574">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vi7lSJfXHuXgAIMFmadRIi-ZlxoSQgrEu2kw4p_wfmdXQIrGW6hvGCEKiIkOhw3lMLMoOuNN_TkzGuHTYW0HBNxX6nRcmqeUTBscNzS6AUnvXvsS3qHSBDj8MkLzmqSkFkAwKCqRmAROGB4qjIj2bBnCeccpKR-VOhsypZTPOJPtSEug4vLGIwMmrRxJT_pDYjKNapbK1asun1F7MHVirlAG0xlbEIFchGZHMqM4AD29EuCoJ_bM4pzuo-wla-Xg0kMZNGKi8mEDtd8uW-MWX64_vQUpxFU0yy7xmJhm4zPhBP4gzRfMJQjTh6MRK-WZ4UWAXOc8P5Ppw-_W5s-mBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشتراک 20 دلاری Cursor اصلا نمی‌ارزید. خیلی خیلی خیلی زود تموم شد با اینکه از مدل‌هایی مثل Opus هم استفاده نکردم
اکثرا gpt 5.3 بود یه کم هم Sonnet
افتضاح زود تموم شدش</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/MatinSenPaii/3574" target="_blank">📅 03:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3573">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مشغول حل کردن مشکل رو اعصاب آیپی healthy فیک هستم. خدا رو شکر یه سیمکارت پیدا کردم که روش دقیقا همین مشکل رو داره</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/MatinSenPaii/3573" target="_blank">📅 03:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3572">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jo1lvJEae4Y8XJEilZHf5yGnnqJOci3OjQ4HO96fBBB5sDHn_mIjIYj7mYh0NNuHUyTjKqVO7k_O6ucrpPeV0n0dJvkcSIq6dP1CSXvHI-xVROh2rb6cLjVAquIVXYZspWvbZxNFOl93ayd8lXc-Hs4-kDcqeCDFDFQ-shSoePA7bBsuRCcC44ZflBxpPWQvSpA-x4RAyXh6Dcl3Yud79GjiIOi9tqDuYXzpbhUIRXUGzewXxCXJ8FU8o50VJLnw0S7C07ycxn7E8qQtx77C_Qj_0L---ISyt4NJDBw_MWGy1BLxqLfYH6F0tYVp6DR8ivwa3jnXSzxpp-HoTkvX9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روی یه اینترنت عادی هم این شکلیه نسبت. یعنی تعداد آیپی‌های سالم کمه و همین هم شانسیه چون range ها به صورت رندوم انتخاب میشن. حداقل 200 هزارتا اسکن کنید</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/MatinSenPaii/3572" target="_blank">📅 20:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3571">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">V4-Spoof-Configs-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/MatinSenPaii/3571" target="_blank">📅 20:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3570">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اسکنر همچنان مشکل داره متاسفانه روی اینترنت‌های دارای اختلال. دارم روش کار می‌کنم</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/MatinSenPaii/3570" target="_blank">📅 20:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3569">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V4-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">6.2 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3569" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">V3-Spoof-Configs-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/MatinSenPaii/3569" target="_blank">📅 20:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3568">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ورژن 3 منتشر شد https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.3.0</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/MatinSenPaii/3568" target="_blank">📅 19:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3567">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اگر اکانت جدید می‌خواید بسازید، از BPB استفاده نکنید فعلا. با این آموزش، edge tunnel بسازید:
https://www.youtube.com/watch?v=svYBcv4bSzo&t=618s</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/MatinSenPaii/3567" target="_blank">📅 19:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3566">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ورژن 3 منتشر شد
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.3.0</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/MatinSenPaii/3566" target="_blank">📅 19:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3565">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oeSfX8yCDgw-xq6HjZQENmTiU08uel7JrX4vR0KEOYbXYz6qnLuQ4Eo89l7FGcSvT-KwzN40HB2Pmya7lN0aK2ljfRJ4Teu5H9Wq7YX_wYbTHkxao6-V03-ccxur-ehQJxJ1tZfWBAKB1GrOEo5rVagijIf4EiXpP6FoDNszfdLeQDEbIbDBSVzVg3aYi-r-Vp8wAbtwMrOFqHEsGpafESN-dfPH1rmUOMWjAECIZ7nlNz44yHsnHaijFG9jOVOaUahxCh49lkh4QYSBX_gsa_ToXCsSuUM5N7Fyo9Xpj0tNRgSqUUkmPnWu9ZcgMvyBwI95SfSzAv-UD_5shUnL3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به لطف دوست عزیزمون abolix، به اسکنر هسته‌ی xray اضافه شد که دیگه پینگ فیک نگیرید. همینطور دارم باگ‌هاش رو می‌گیرم که بتونید راحت استفاده کنید</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/MatinSenPaii/3565" target="_blank">📅 19:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3564">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">به لطف دوست عزیزمون abolix، به اسکنر هسته‌ی xray اضافه شد که دیگه پینگ فیک نگیرید. همینطور دارم باگ‌هاش رو می‌گیرم که بتونید راحت استفاده کنید</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/MatinSenPaii/3564" target="_blank">📅 18:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3563">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jKCDUKdWZF8fxXwnbF8AmMpqWRwoun6S_IBWMeqpsTJSDsNTmeNvIdLKMzYFE6Bhg2KV850tzdOQ8p7ddPRx7PKfMYvXflauaCWFgfVi99o2fZPTDRds2qStCnBk_4orLp3f-8mjQyXfMbW5M3hDpfu_OJFP9elKNEiQs9KV5tiqRZb3qdHYxW8OfF96JieyUxMysNKD3-mDcDon73XdA9ojo8hSmNRXOW8CMj_CxNPpu38pK5YWTFI9mhMpjlTyFowfZ3nruyV1xwZiNM_OsoWbOamJTarS8v0PTxt5nBzXrY6VFm-dIM4PyzexM0CYMUgLW6e1CGd2reawbdGAQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">BPB - Edge - VahidFarid
فقط Edge داره کار میکنه. هر سه هم روی یک اکانت</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/MatinSenPaii/3563" target="_blank">📅 17:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3562">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خب انگار مشکل از BPB بودش. چون الان edge tunnel بالا آوردم کار کرد اما bpb دوتا بالا آوردم روش کار نکرد</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/MatinSenPaii/3562" target="_blank">📅 16:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3561">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">امروز به دوتا نتیجه‌ی مهم رسیدم:
1- روی یه سری از اپراتورها، اسکنر نتایج فیک میده
2- پنل BPB ممکنه از اول تا آخرش ستاپش درست باشه، اما در نهایت کانفیگا کار نکنن. که دارم سر در میارم علتش چیه. فرای از اپراتور این شکلیه. یعنی با یه vpn دیگه هم ازشون پینگ میگیرم پینگ ندارن با اینکه tcping میدن</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/MatinSenPaii/3561" target="_blank">📅 16:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3560">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">همچنان از
@Whitedns_Installer_bot
می‌تونید کانفیگ رایگان دریافت کنید. تا الان 21 هزار نفر دریافت کردن دیروز و حدود 5000 نفر، حجمشون رو تموم کردن(که امروز دوباره شارژ میشه). به زودی مقدار حجم روزانه هم افزایش پیدا می‌کنه</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/MatinSenPaii/3560" target="_blank">📅 13:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3559">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یه آموزش کوچولو داریم امروز</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/MatinSenPaii/3559" target="_blank">📅 12:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3555">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M8OCfCwC-9Td0q8MyD8gI2YBq3uZKeBZQp21IZHJj4IJk7y-DoqAjVKn8fSdCvp6-sZG137Z5C_ym2M46DwkW8dWoo1uHMOsEFH2xJbTcwtRBRhMT5tzxWCiIEcgkWTZ_0ykfeiLI4pSy8NvR2pHP1vBINGj-z2L14kJ2DV2qvI7D0Tjq6UJEzdxHAOPR245V2OTJHdsrgfctZbOlQEPdpMS2eDIA1wjlx0v89zjOKH5e683N46jsi41PC3enlnNuz95Jl4LzMiKpaHBc07NXPJU7sC1hq-L6NcZxQFyHsaUJ9vJZUP-P05gxjvH0Qd_SIM5f_LL-fBXHMjMxZIs8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DLBzenWLYuyevDra6tBE5Z93y4fe65okpxa-bShP5cCHi2pYsnOsK3ysa_aem0u7dAWFJWfmmdB-mrNSgBs23HLxbhn7aFhI4rhY_khEJpWSqGa45QDVQ-94u5UqvUt0n7Lk7ImTzENdqUq3PVfgh4ecxT9gGIuMa2tkGo_x-hxLMhS2lPHtVjhCwNMlVd2Emup2kADeXDeF8zCQ4C9Lqzwg5sokNtu3YDOQgtQzsjUwheAmLUaBu0pZSQBAW493m0I4cNb0ypBFxydvDJZdCbcueVcmNYFZvuPKhQyiThr-UT21gdmT4Ta3Q7vJpLjEnmwHq1ye6WyYdxeNuZn4Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UTW0L4WFfGzs2pJR8PmhDaPgIfZwrnKVgVcKz2rKgBcpS3A-v2P0q7C_ZX2ZO-AIVH8drG9Cr3If0yBGy8O0xsfVxUEINg_WiakGXD4tkQE0t_X9dc2ze7qDJsMJXyriGK5-AKHm7soEiMpskpBhuDAhDheAB5CcEIdqJ8kbKPt2oPdbNO0xV63g6popcFV1b-lPEQ4wOTTniBJG53jUZZR6DOappfHrNukhsXAMrgqNBCX5sWJdwnQ8mJU72BfTXsURcL-HOzwGnM6xNvfbgurvl8_x6msq-SXUvNkWW9kEBwC5CGX7-5-U9bKz_GxwLApkn-qeriWhlZbMljfdzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ed3-B8ySu8KtMJ4WDlbYjGuwqlIW-mHdV58snalFEJ830pT5NBetwo6FBalt9lpSJrd81_-Gzv2t0zU4qcfy1iRTBQtCTzIF6M21AHcaDyweizPmWxWdGydwPCecTVptEDsrsGocyGKavKuCEne1h3rqKL5f2agaoh1P2GiiNsL90FqIeP6V5_CYG8vqIWLEfKw4F5bSvN5Si1uxdgxOeJf8KNUfJCYv_owEEeMWMb2LuKqx6hQKRmFZ3HPRLUiPunPYU2M-BEovq5QBgcVw4d9pxilWHAaPvs41rureCgbTDR1npTWAdx-uBtfho-5laemS7VTQVKDKS24lXBxuZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاری که خودم کردم:
1- صد هزارتا زدم بره برای اسکن با ورژن جدید سنپای‌اسکنر. با 200 تا worker کلا 10 دقیقه طول کشید
2- برای من 4 تا آیپی پیدا کرد
3- آیپی‌ها رو با این پروژه‌:
https://t.me/MatinSenPaii/3554
بازنویسی کردم روی کانفیگ پنل BPB(هرچند خودش داره اما این شکلی راحتتره)
(صفر تا صد ساخت BPB رایگان)
4- کپی پیست به v2rayN و ادامه ماجرا
سرعت آپلودا هم اوکی شده الان راحت اندازه دانلودم میگیرم</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/MatinSenPaii/3555" target="_blank">📅 09:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3554">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اشکالاتی که فرموده بودید رفع شد. پروژه با هوش مصنوعی نوشته شده و تمرکز بر سادگی و استفاده‌ی راحت مردمه. اگر اشکالی دارید توی استفاده باهاش بفرمایید و issue ثبت کنید یا اگر خواستید، pr بزنید و مشارکت کنید.
باز هم عرض میکنم خدمتتون که این اولین تجربه‌ی من از اوپن سورس هست و اگر اشکالی به وجود اومد در آینده، پیشاپیش عذرخواهی می‌کنم. سعی می‌کنم که یاد بگیرم و نیاز فعلی رو خوب پوشش بدم و همینطور پروژه رو هم در بهترین حالت ممکن maintain کنم</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/MatinSenPaii/3554" target="_blank">📅 04:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3547">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">7.3 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3547" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">راهنمای ورژن‌ها
تغییرات و بهبود‌ها:
- رفع کامل LOSS% اشتباه روی شبکه‌های محدود و DPI (مشکل اصلی کاربران). حالا تایم‌اوت بین Dial، TLS و HTTP به‌درستی تقسیم می‌شه و پکت‌لاس فیک کاملاً برطرف شد.
- ذخیره خودکار IPهای سالم بعد از Quick Scan و کپی در کلیپ‌بورد با زدن دکمه C
- خروجی فقط شامل IPهای سالم (بدون IPهای مرده)
- فرمت txt حالا ساده: فقط یک IP در هر خط( از
https://t.me/MatinSenPaii/3543
برای بازنویسی کانفیگ استفاده کنید)
- پیش‌فرض‌های هوشمندتر برای شبکه‌های محدود (تایم‌اوت ۵ ثانیه، دانلود ۶۴KB)
- کاهش تخصیص حافظه و فشار GC
- حذف IPهای تکراری در اسکن
- اسکریپت نصب یک‌خطی (شامل آپدیت و Termux برای اندروید)
- بهینه‌سازی منو و تمیزکاری کد
ممنون از همه Contributorها:
ProArash
،
M-logique
،
Mralimoh
،
Hoot-Code
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/MatinSenPaii/3547" target="_blank">📅 03:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3545">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rKGs6JzTdWyV2tBaxpn1kzZ9B_T_McPKZoLhaiTCpdrSYYx3GTghZ9zuGuIeukylvEHb6ss8MzcDIGvm6EE4q00ppn1bXIhfGQ2gct0BnqN8l6mCAKbGmO8Ha39peg1C1gTjcDMQGFg_G1YqdjkfPsX-5s6NA-V_TGCqgmBYc0XvfQ16DduPuAY4yIqhBLempFdX_uirjVR69t59XcARJYROdcaliJ6fLdD7iE7JLf8IIvUmXzt6o5EVYZyLt0KOY-5IQuLdIVfpFKRgSemRMEYt0cLGxUs3bXwUOZ8n_OYyjYWzLx-rMD2oUaRa6a2P-UmRCZAkPKiMCRQl8mHMLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MAfus3pGapv3PG50GPj_nIcujBKlNcuMpesDSnfuGroR_vjSK1eSOn-HH5iQjRVhm5kOPfkQRE3GhmpzOstkZdzcfz9_1WknNFPg4i9nkwVCyD_7MVERG7-AT4w8LBsNnWeyccxt7gwk6czYdq9XIRyNLOpOQ2l7foi0D3mkEUCI9yPkmWB7l0OEjl8IKYSNW51Uy58-MphfIUsPNhWtlu4T233AHZ2N9Ydh6JL1MymDrQhWcIpJGCnxgm3jZ8nIBNSxK6qA9S_E-ftODaw4L-SOBubCB8ttR0xWQtCcQhR3D_Qfwleq-ff-quGA0kZ6BDYBoHQ8CUyuFNKyt2v4vg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توی آپدیت جدید اسکنر، آیپی‌ای که Healthy هست واقعا بهتون پینگ میده!
همینطور با زدن دکمه‌ی c روی کیبوردتون توی تست لایو، میتونید این آیپی‌ها رو کپی کنید.
یک سری دوستان عزیز متخصص هم برای تست بهتر، روی پروژه pr زدن که دستشون درد نکنه واقعا.
تا دقایقی دیگه منتشر می‌کنم
همینطور که توی تصویر می‌بینید، یک آیپی به من healthy داده شده و همون داره واسم کار می‌کنه با سرعت عالی</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/MatinSenPaii/3545" target="_blank">📅 03:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3543">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/skgQsG4pDmnKzrKDFgftGMTv3jKz3lwCfiFxkcjUdExmJT1toO1a4vxKiqCHNUXOYWHGt0A8H9A7fpBLQeV_9kE0RjJqhAFw0pPJpq-4TZf1ycZr40WoUjlJFerPocSd5-wBndt4u_xvjsQkpD6g_pPSG_KQOAstTTPLkNX8oAUz3IP8yMY5bnVeinm6Eift84S6yXQkWz15AtICGVYCgaKszfEKIdWXIp_WjEnWskCi6s0KwX9q_u-Kpa_h34KQVjM8ASKderf0D8U2D0aexLQLY-vyf_KPbznT7mtsU2KEtJWn3bFCXWH2aRBnk8AgcidXb38vG26z0JipkWvHQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازنویسی یک کانفیگ تکراری با آیپی تمیز‌های متفاوت!
با این پروژه‌ی رسول عزیز می‌تونید این کار رو به سادگی انجام بدید:
https://github.com/seramo/v2ray-config-modifier/
این هم نسخه تحت وب ساده‌اش بدون نیاز به نصب:
https://seramo.github.io/v2ray-config-modifier/
برای حمایت از سازنده، روی گیتهاب بهش استار بدید اگر دوست داشتید</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/MatinSenPaii/3543" target="_blank">📅 03:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3542">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECP7T7vDybOth2K5_XNyfSbihZO1A1ngeCyOM7w96s4VZthCOVVdpl3M_c04xd7aQvqIx1xgNjz82bpIxWpD4Pr-j7KJ4429QvS6Ju-JdxINA9N7DuSdt8yTBr2h1u14K-VMZaOT5Lg-mKJRwdfpDVpJX6K6TBKoEuqNcD9JHK7dVFmNjHknQmRin7kjgJy-m78ZxfDMdrsrSHyXuF6T-jJ8ccwKxrNI4-0jBGdfDOeFTikzGjX680WtT22pVtuiowpfBLt5isjYvbu3guN6u_cuPI-JOHY4XAAfbdBzJPfpttmZOYRJfj2npRgYHWccn81QXNeSIxRC3vpNXOkn5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با شرایط امروز اینترنت، دسترسی به کانفیگ ها برای برخی اپراتور ها امکان پذیر است و برای برخی نه. ولی راه حلی هست که امکان داره کانفیگ هایی که سالم هستند ولی پینگ نمیدهند رو هم به کار بندازید.
با امکان جدید ربات
@Whitedns_Installer_bot
میتونید کانفیگ V2Ray خودتون رو ارسال کنید و اون رو تبدیل به کانفیگ هایی پشت آی‌پی های سفید بکنید.
وارد ربات بشید، روی «تبدیل کانفیگ با آی‌پی سفید» کلیک کنید و سپس کانفیگ V2Ray خودتون رو بفرستید.
تشکر
تیم WhiteDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/MatinSenPaii/3542" target="_blank">📅 01:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3541">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دوستان، ترجیحا همه‌ی پورت‌های توی پنل bpb رو باز کنید. چه tls چه non-tls</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/MatinSenPaii/3541" target="_blank">📅 01:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3540">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دوستان، ترجیحا همه‌ی پورت‌های توی پنل bpb رو باز کنید. چه tls چه non-tls</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/MatinSenPaii/3540" target="_blank">📅 01:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3539">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خیلی باگ‌ها پروژه داره و تا الان نزدیک به ۱۰ تا issue ثبت شده و دوتا pull request
دمتون گرم. همه رو اوکیش می‌کنم تا صبح
❤️</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/MatinSenPaii/3539" target="_blank">📅 00:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3538">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kiTdtuAJekRhQqMCaNlf_csjxTNZhR_TWXw1HcYeLgYbH442j4ydAVDr7Mp1FReVVayMNkKzNs3DjqT_Y7yO8lWZ8mezl--9OjNQ80EgK1-sTNnteUsT1Pds1qe2Y61OC5oindTmdz7QwzaGBrG-a1yyvVVVnvKWBYuwqI1ziKKbpyBn_U7gxrtl2CKNfF0odiI5sVRnpJsSP6lCD3Gt5SZLOxn5IGU2YTkLyq1zWFhc0dHlCqlc-Ri_z7pPrJRuqnU2dnSPQE4VTqLghd5EPMewD2MAXghfN9h7TbPIwILRG-naWUowyQ286KaE72s67HpqkV-XXqos7wlztJ7UOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اکثرا جوابای خوبی گرفتن از اسکنر. باعث خوشحالیه و خوشحال‌تر میشم که دوستان متخصص issue ثبت کنن یا contribute کنن
🙏</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/MatinSenPaii/3538" target="_blank">📅 23:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3537">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">عدد سمت چپ اینجا 104.16.90.120 در واقع آیپی ما هستش عدد 2053 هم پورت ما هستش. ابتدا بزنید روی گزینه‌ی ویرایش کانفیگ، و بعدش آیپی تمیز‌هایی که توی کانال‌ها می‌بینید رو، به جای عدد حال حاضر آیپی قرار بدید. پورت رو دست نزنید.</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/MatinSenPaii/3537" target="_blank">📅 23:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3536">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aRrwQwYKEXeE-W7M6Ui3p__5e2IGq2jDUV0qrIwesCoADkSfF19Gv5jDX_q9OYpOu5-kYEmOm2cf38RA8kAS1v5-0TTJC3IwQeKZLERCjYa0mI1ndJNWZ-Z-qH2pPSyQASFdcIubeJNxtO3KUAEau-kNYL8qoUJuIhzfOe860-hmLbEhNyOyfjksFzZxkzEN2tcZYix6un5ycxJieNbEAG2r1kg539gu9_Nc3ZCcTGXPgYeAJ7RiEJd85e0bTYGdrSKxX-yjACAJFWzSOMMl2YOKtsbpfxum-ybckvhS8gG0Cx2EPqON5_6ziwtEtDebrjRQUn-2oUGeIX-xg7QElQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اکثرا جوابای خوبی گرفتن از اسکنر. باعث خوشحالیه
و خوشحال‌تر میشم که دوستان متخصص issue ثبت کنن یا contribute کنن
🙏</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/MatinSenPaii/3536" target="_blank">📅 22:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3535">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qDWceslJ3JzoFxOB5osTgP0FEAQNSrxsoRTY6uxlZtbHPx0xwuNnXr1V-4rwh6Uwo3eB6-LPRyQQYZV_MisyVvjkwAxPxnX2zxFWL7Ohe1gKYnTlZhSW6vZuzaKeNBvjShYS3lY4REA7JxLAB9DorUxUpqkeGCQU5qxMfLawUpOPJHxpL-PwffV4EMlMIAMd1NcrxhUuGXJnG1Lu5g0KMjHBpxpw4bIUchYnqGUpMI5MGZZZemErIr-C4n6WkijEKlVznqx2sA-bnftkSHrhkmRUbNzm-_bUHg0gQygq-l5q1USWrQ3WSRuOaIsDYMB7LSiFE4FaRgLVq2RBNT-njQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌ها کاملا رندوم اسکن می‌شن. برای همین باید تعداد رو خیلی بالاتر در نظر بگیرید. حداقل ۱۰۰ هزار</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/MatinSenPaii/3535" target="_blank">📅 22:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3534">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">این اولین تجربه‌ی واقعی من از اوپن سورسه پس اگر کم و کاستی داره، ببخشید. صرفا این پروژه رو زدم که نیاز خودم رو برطرف کنه اما دوست داشتم پابلیک باشه و یه پایه‌ای باشه که از ایراد‌هایی که روش گرفته میشه، دانش برنامه‌نویسی و شبکه‌ام رو هم ارتقا بدم
❤️
امیدوارم که این پروژه‌ی کوچولو به دردتون بخوره
به شخصه از اسکنرهای پیچیده‌ای که هزارتا مقدار داره داخلش و نه میشه به عموم توضیح داد نه میشه به راحتی ازشون استفاده کرد، خسته شدم. نیاز داشتم یه اسکنر داشته باشم که به صورت رندوم، به تعداد دلخواه آیپی اسکن کنه و تست کارکرد بگیره ازشون</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/MatinSenPaii/3534" target="_blank">📅 21:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3527">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">7.3 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3527" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">راهنمای نسخه‌ها:
🪟
ویندوز (Windows)
senpaiscanner-windows-amd64.exe
مناسب برای:
سیستم‌های ویندوزی ۶۴ بیتی (بیشتر لپ‌تاپ‌ها و کامپیوترهای امروزی با پردازنده‌های Intel یا AMD).
senpaiscanner-windows-336.exe
(یا همان
windows-386.exe
)
مناسب برای:
سیستم‌های ویندوزی قدیمی ۳۲ بیتی.
🍏
مک‌بوک / اپل (macOS / Darwin)
senpaiscanner-darwin-arm64
مناسب برای:
مک‌بوک‌ها و آی‌مک‌های جدید با تراشه‌های اختصاصی اپل (
M1, M2, M3
و جدیدتر).
senpaiscanner-darwin-amd64
مناسب برای:
مک‌بوک‌ها و کامپیوترهای قدیمی‌تر اپل که پردازنده
Intel
دارند.
🐧
لینوکس (Linux)
senpaiscanner-linux-amd64
مناسب برای:
توزیع‌های لینوکس ۶۴ بیتی روی کامپیوترها و سرورهای استاندارد (Intel/AMD).
senpaiscanner-linux-arm64
مناسب برای:
مینی‌کامپیوترها (مثل رزبری پای ۴ و ۵)، سرورهای ابری ARM، یا لینوکس‌های نصب‌شده روی مک‌های M1/M2.
senpaiscanner-linux-386
مناسب برای:
سیستم‌ها یا سرورهای بسیار قدیمی لینوکس با ساختار ۳۲ بیتی.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/MatinSenPaii/3527" target="_blank">📅 21:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3526">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BPFdh7aP44mxq0ennUN4NAe_LSYYRzJ8-sjyPQ_Qyj1y821GGfyHAgmlMZBhgbfZygYXqHg5StIlpygL12uI7IYsATI-tKmw_QeZv_O2sM85cjdx7AiuSiE43M-NYbLr436G-pISg7GTjjwIYMKdRe3O03CJ4XWS8bNCblXbl8B8CydZ6Ln7e-WOJwT8j_fSBuMhymZ9k2fmliJfiyleMxQuAtjeSfgOEkogwyXTmT4kSSRLQBxrxmCV0sIEGE3IDwcgY1Rov5V37TlVNtvHuqdCm3hpkchfvNyrfde06tjLTBXAVRk6Lc7VR4DsLKyG5SMen5IV0DPIST-3wpmy6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
پروژه‌ی
SenPai Scanner
— اسکنر IPهای Cloudflare
چی کار می‌کنه؟
از شبکه‌ات چند هزار IP از محدوده‌های رسمی Cloudflare رو تست می‌کنه، سریع‌ترین و سالم‌ترین‌ها رو پیدا می‌کنه تا توی کانفیگ V2Ray / Xray / Trojan بذاری.
چطور اجرا می‌شه؟
فقط فایل مخصوص سیستم عاملت رو دانلود کن و اجرا کن.
۴ حالت اصلی:
⚙️
Quick Scan
— سریع: تعداد IP، تعداد worker و timeout رو انتخاب می‌کنی و اسکن شروع می‌شه (پیش‌فرض: حالت HTTP + تست واقعی داده)
⚙️
Custom Scan
— کامل: تعداد IP، پورت، محدوده CIDR، فیلتر دیتاسنتر (مثل FRA)، حالت tcp/tls/http، خروجی CSV/JSON/TXT
⚙️
Test IPs
— لیست IPهای خودت رو از فایل
ips.txt
عمیق‌تر تست می‌کنه
⚙️
Discover Colos
— می‌فهمی از شبکه‌ات به کدوم دیتاسنترهای Cloudflare دسترسی داری
چی اندازه می‌گیره؟
- تأخیر (latency) و jitter
- درصد packet loss
- در حالت HTTP: تأیید Cloudflare + شناسایی colo (مثل FRA، AMS)
- یک نمونه دانلود کوچک — تا گول IPی که «وصل می‌شه ولی داده نمی‌ده» رو نخوریم
نکته مهم:
این یه ابزار
پروکسی نیست
— فقط IPهای خوب رو پیدا می‌کنه. تست نهایی هنوز با همون کانفیگ واقعی‌ات روی Xray/V2Ray هست.
---
🎄
پلتفرم‌ها:
Linux · macOS · Windows
🔗
لینک پروژه:
https://github.com/MatinSenPai/SenPaiScanner
دانلود فایل‌ها از گیتهاب:
https://github.com/MatinSenPai/SenPaiScanner/releases
دانلود فایلها از تلگرام:
https://t.me/MatinSenPaii/3526</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/MatinSenPaii/3526" target="_blank">📅 21:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3524">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V26V2Qg3EMKxBqzqrx1ggp1g4lUOxbmVRFPz2b3qUcPckODlaiAakHQtJC-qjJwcF6ttQMxBKk1NuQ22Fz1idC-WBGvN3o7tYOYHGW-jvGIpny0Pm2g6L_s9mSYzrS0LG0fGYsJfQN7Q6WOOw8PTG8fvl9i6vkog7p7fnXAeTF4_S4ImxFv4-MDWkmeUCVCI7sTLkFGybayjapPrBWXu0MIqrW3dH8b1HJhQ1DsRc7LojdmirbMs0zwHqm9vhOvb7hEqp08bE3KngYlO6VYRt57b7_7ZclH7asiiEPRhuFvPbMYL_DBu-bXY2lzi8n9MfTFpw7jNGGTtWaQgVnNMQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/m3TIPRM6CLJsFWQ8Q6UWBgOJ_IwDxzB_jZUjusMpHRJoXHZBN3zb2X6e0B9KcHiF76UTYzK5E6suquV_rwg1T6B-c7W8I8lLDoC6IPPlalUrYSVXn8xQK73wLo7RcSJBUCk6RHeYtuj-eFqnV4NSUBhgu6ipVJn-vUoE51qUzqhFBtLmhzBtDfQf6JeLQPWTPKeczoA3NyQoZDW4guf4uds14F3B_EL4OzE71CKpNacYEdMTwzpuyvU5ZRoZTk7Uwv7hpTQ_qg8yOR2PA-FMyoBY1bQB9EGwvUS_rYwZ4Ugv5N9o-cb9meDjimn2m3NoF7wCIe-3g5uFlHfnifiTLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اولین آیپی ای که اسکنر پیدا کرد و داره کار میکنه
مبارکه</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/MatinSenPaii/3524" target="_blank">📅 20:25 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
