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
<img src="https://cdn1.telesco.pe/file/gnKh-KvUElndqeEQ4W07Mm-i79XeRrWG_UXb9GRT7SgLBZlUArXF4SrcAFxa7XzbH0P_5h0ZGhAEC6Hg9Ew1t9d3NMPfHg-udZN5KamM6Wv55NPcxO4q_0XOx4E4e-XxKJy9Q-RUOk110CV19GF9PjOmIMe1gDn77TP1IGzirmJzsNPoLKeiU61ymqJm_78ymIp01vem49QB1OJRfbC7EuOClZxr9KKTwjRqOn0NH11w5sh0qktNSAf_z0ZKDQd3wXPyZAtOb_x68dwm7exFKsKg3tcc4BOi5Oqy29DYzXy2SOmCVcvvipg8km4FA_Z1rtFbFBWVmq2mz2jx3eYCpw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 161K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 13:15:45</div>
<hr>

<div class="tg-post" id="msg-3658">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cYBhr8fP2W6U0Yne9xeylhYuBN2o6BXriB9N6CDyBWz4Fj_BV9RFMCBhEZ9romFa5mnwkQd1sp03pJDSzVyJu_xjLVtaFeeFhoOZj-pfV77QvjgC-IjMwAQJYST4x1JXFGcn9Er0C-OWABr5HZJznFCt_FBo2iOqFzWq-t6G_r88wxPOTVndlS3IHg0K39bGrifhRKECASv_r2i_LXxj20cVgboUTc887O99WNH4bBafxvztQ4neQp4fbme2kKYHVBBTjlQla7WIBDN9v2mlrwowpmCWDcw165-XU_oTY7ce_05lRxydrS3b6PzHabqmESpmfr5LFT3ht8tjs-FTXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینترنت دیتاسنتر ها در حال وصل شدن هست . اختلال ها کمتر شده
اما همچنان پروتکل های مهم ارتباطی یا مسدود هستند یا بسیار محدود و هنوز دسترسی به HTTP3 و IPV6 ممکن نشده
برگشت اینترنت به دیتاسنتر ها میتونه اتفاق خوبی باشه اما باز شدن پروتکل های ارتباطی اهمیت زیادی داره
✍️
Amir Mokhtari</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/MatinSenPaii/3658" target="_blank">📅 13:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3657">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ببینید MHR و mhrv-rust و skirk و flow drive و تمامی متدهای بر پایه‌ی گوگل، با اولین بادی که از سمت سرزمین‌های دشمن بِوَزه قطع می‌شن
تنها چیزی که برای ما می‌مونه، DNS هست که همون هم ممکنه سرعتش خیلی خیلی کم باشه و می‌تونید از اینجا
https://youtu.be/6Pm7kNQb3mo
آموزشش رو ببینید.
متدهای بر پایه کلودفلر مثل BPB و Edge و... هم که یه پله بالاتر از MHR و اینها هستن و طبیعتا همیشه بعد از وصل شدن گوگل، وصل می‌شن.
هرچند به WhiteDns هم نمیشه ۱۰۰ اعتماد داشت که برامون بمونه چون توی هر سری فیلترینگ ما غافلگیر شدیم. مثلا ما به هیچ وجه فکر نمی‌کردیم بتونن جلوی Paqet رو بگیرن اما تونستن. هرچند امثال پترنیها هم با SNI Spoof، اونا رو غافلگیر کردن!
برای همین شما ترجیحا متد مستر دی ان اس رو توی Whitedns به عنوان اضطراری‌ترین راه، داشته باشید علی‌الحساب</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/MatinSenPaii/3657" target="_blank">📅 12:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3656">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/MatinSenPaii/3656" target="_blank">📅 11:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3655">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/MatinSenPaii/3655" target="_blank">📅 11:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3654">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دوستان برای هیستریا، سرورهای AWS آمازون با این سرعت جوابگو هستن چیزی که من دیدم و دوستان گفتن و متأسفانه دیتاسنتر دیگه‌ای ندیدم که به این خوبی باشه. آمازون هم گرونه به شدت
پس از آموزشش فعلا منصرف شدم</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/3654" target="_blank">📅 00:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3653">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شمع Iced latte</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/3653" target="_blank">📅 23:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3652">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/twpJDRfiYs197oIip4i6J9yT2HfrWES-56WtjgItufNjWR2wceJ5gjAh5PIexfD8Lg_Af1FAAbiHPdOkOhcJWK0P3s73KKxUjuPAK_V6CErwWc9OWSv6Jk4etrsea0nbX2Ab73wtI5ji1qmZJ8DEZTrBosSwDWV2yej0CcVWcEdveaOpMk2y6deJ5qnETG4uZLNagVdpoHBmGNEJrrMNnB-9Ul8XHPQ2km6z3FclL0FnjAPUn7ORvZmqHun2gwNf0nb07QxwiOFJuw9I5WSp3LnKDL2Fjo7YiH4e7CevxlgYiCh4CYK2TEyT5MyfJjtrf143MKPvHoLKjw4gnJN8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ارور EOF و 403 گرفتید یعنی گیتهاب هنوز روی اپراتورتون مشکل داره و این یعنی اسکنر نصب نمیشه(باید با وی‌پی‌ان بزنید). طبیعتا وقتی دستور senpaiscanner رو میزنید not found میده چون اصلا چیزی نصب نشده</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/MatinSenPaii/3652" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3651">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux  دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/3651" target="_blank">📅 20:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3650">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KeWhf5oXYz82_-lPIXW38Gna09QLs1HHN_EyIswbxfnCuIWAw_z-4LfKfWPH_beqL_VGccN2zOY3QnOLWKQaVqG9HeA7UDlQeCy0ZgA5H92v7DI54qFvuOmpLDVRi_xSdd_WHtjdjizKVVKkWhAuoRRiAPJG_X0FXPRbt3ozC2lBewc9aW9LBH-TPPwJel0bHc3oYK1aBZEKGqLX2BebLlE96EmWt8svGHhPnyBW9ckzvXueKwjdQ9PHhRhFjd6cVNarR686C0G2GcsahRjWKC_SNfYAq-Ai2ReZUeX_iWNFsyXOVU7Nn-5enIC_-bzby_SfeQzCFeINI7bSvAnOKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر به این ارور خوردید، پروژه‌ی جدید بسازید. اگر باز هم نشد، با یه اکانت دیگه وارد بشید و مجدد تست کنید. توی این ویدئو
https://youtu.be/_aXy8wwyRG8
به همین ارور خوردم و این شکلی حل شد</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/MatinSenPaii/3650" target="_blank">📅 19:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3649">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux  دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/3649" target="_blank">📅 19:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3648">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون متصل بشید</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/MatinSenPaii/3648" target="_blank">📅 18:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3646">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ImftsYJP5C6pKVwrLym9gtiUah1EH2QUU5QzPCaEQ2TK_ByZ6jF-Q2jWKHh7zgSWoJBbYyxzXPiFwVELlyWC0GuX06bDpDMjxFCBXXff6geZfH7Z4sYvkhqfAQn4qjp8Fq1IpY124C1jEfnqYCdBsTlNM7upZS9uWVbtnzHX0P8dTOI9LTBMYqFzSHhhEg54Lkhkcruvbg5SUzREqufasTIxvmO7bhBtyDHJzigEFnoJHHZ7-0I-jXy6SIE80my1WEmcFJISDJJgtQc9CM_IbHcEX5BRYm0wAbaCPvXGpC4N5BLyqhBWfW3MVcWxi4ezMRBfnp6tOhIrCkyqo0jm6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VbxWc9xvDxyijlXLzNLucTmknsC5ojqTtj_nG7Y-gCwob2C0Z0KTbqobj_YmjDredSufHKjM5rMq6ZWwWDEP-Ckjiu_g73KnIgbmEyKte_oMHbkOu8CT7pL9Afp5PUM521rCn2jyXDr_QkhccNLC88VTZhIlTWmsvPiVpCXEYQOZndx3gw-2VJaYj8UyIO3-11lS0vtzUikG59fWpbQAR4snZF53xfMY8vbaJaKAgxLhHsDge4SwIl24i_6K-ZAg_25w_XazsvZjXU3cBX9uzAC6q1H9WIM3uEhu0RcKOV-eW6U0kBOtthvE1q-j0SfvB8sMfJJc8NLXKV5q5LRB7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux  دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/MatinSenPaii/3646" target="_blank">📅 17:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3645">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/MatinSenPaii/3645" target="_blank">📅 17:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3644">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">base.apk</div>
  <div class="tg-doc-extra">11.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3644" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اپلیکیشن RSTA(که به زودی اوپن سورسش رو هم میسازن عزیزان)</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/MatinSenPaii/3644" target="_blank">📅 17:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3643">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SenPaiScanner-on-Phone.txt</div>
  <div class="tg-doc-extra">350 B</div>
</div>
<a href="https://t.me/MatinSenPaii/3643" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دستورات اسکنر برای Termux</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/3643" target="_blank">📅 17:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3642">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/MatinSenPaii/3642" target="_blank">📅 17:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3641">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vZGNJCgqxYwSnKIahONwA-W9mAT5NjoJZTdP6KjrP4meTJa5zYFm_0OnbiRotmTlifVkDL0dwCwe2BnxsG8xT0CjVuyusAzqmU5vx4N67cH6NkddFi8Y8klNTmc5lX0c7I9vC6lExwGB6jP65b0UEPDDtL3-cDRdG2JS2bOzgozkLbj9C12o6SNXZo1_B_542k6ubZMRaJt_ihk8xRe0UkIOBaWNMw3wmleN3huW4Po2elbWIZe5yXva-KmaufJuo8RNsDtkb-Td9d5trqhXsD-dD4lUGjUl2LKGQkLaLxCoLgaiAKhPww8v8vflif-xEkL-cdx3Y256zUAYrLbn0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ربات از
یـ‌ بـ‌ خـ
عزیز واقعا باحاله. یه نگاه بهش بندازید:
@iNewsSummaryBot</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/MatinSenPaii/3641" target="_blank">📅 16:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3640">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تصمیم گرفتم یه آموزش صفر تا صد ضبط کنم برای عزیزای دلی که لپ تاپ ندارن و فقط یه گوشی اندرویدی دارن
از آموزش ساخت کانفیگ اسپوف گرفته(رایگان)
تا اجرای اسکنر روی ترموکس(سردرد)
و استفاده از اپلیکیشن اسپوفی که این دوستانمون ساختن
یه مقدار طولانی میشه اما دوست ندارم واقعا که بچه‌های اندروید کارشون لنگ بمونه</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/MatinSenPaii/3640" target="_blank">📅 15:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3637">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hmsMsorES70-elLMFFZrNagihAtSSqOfHhJztTpwtX0fKH_W4nJ-KJ91StCZ5xNtUam3L6_qy815mW7N2QDYNGodHlnIcxYVnT1hT2FGvdagihyHkBzuLV30_BVWRpFb-P444WyCoqXjQqrCtJIpNf790G0gS1NQFOWjlJJ_sk1NFJAOi4od6yZ62v_uNfRpWZxqNYKBJnyxOo1gmtJVgz5m0DMO_l_qbCMADjMp-giZ2Kmwln_di_uFayj4ZqB6-XV2ZlXJ0dB8Un34x_L-e-7wmtuPnDIsZ-rsd8IViRt2rYp170IwPuijXKpAK4frtbkl-gDplRGUmMovCfki0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MF122oEu9UIUfVYk3wXt7Rjq3n6tTqkIB7YgfP50iFYcR2tJ4P_qFVnMCZeiCAaBkMCIBPQ06T2Iww0YMAliYr8PzVYK_vDFJzAp1G4QSpzfrOlxBthiFOLzWX8UfqSPXdr07HTHLQr9bf2d8tX4bGAoFHV8YhSlZ0EOeN-fDp0hoMhU8ZI1nom5LK2bl7T9csAGLCJckkH1oIX-ekvcRCYT1ceqxfk4Cg27vg77gXFHWfpCX1TkZ9J5CXxyRbIKRzVhHJO6IVTyruAC3xWM0vLhf4WKf9NOcIgCpoeRQbeJx2eMEdZLUxsU4wBbQC_Yv6P8yMj337bLrJ8UAq5ddw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز راجب اینکه چه شکلی می‌تونید کانفیگ اسپوف شخصی بسازید و روی گوشی چه شکلی برای Config-Json می‌تونید اسکن کنید با ترکیب اسکنر من و پروژه‌ی Shin، ویدئو داریم</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/MatinSenPaii/3637" target="_blank">📅 15:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3636">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">📱
اگر لینک ساب WhiteDNS رو میخواید از گیتهاب داشته باشید، این ریپو هر ۴۰ دقیقه با بهترین سرور ها آپدیت میشه
https://github.com/iampedii/whitedns-sub
لینک ساب برای Clash Party & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
@WhiteDNS</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/3636" target="_blank">📅 13:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3635">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">امروز راجب اینکه چه شکلی می‌تونید کانفیگ اسپوف شخصی بسازید و روی گوشی چه شکلی برای Config-Json می‌تونید اسکن کنید با ترکیب اسکنر من و پروژه‌ی Shin، ویدئو داریم</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/MatinSenPaii/3635" target="_blank">📅 13:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3634">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2a4acd74d.mp4?token=cwEkS_CCsNeJTVuqT9E-zKqF0TFr35zXWBCtZiy8M0PLlEN6IR0ioVBM5Gh6SURDVXF_frJV_wL3WBZ6bzuusVBSwRAVJXDJRVHDix1FqHw-QzPhShl8lPzYw-2MPnMlg6S_CxqQcUrZEs6urtHZMaYhD5rALV9b13OfXaR9XQuO_zhqGBKJrmvsz2p94BRAUWi8i0PRjnHngugualBTUN0FYaf4irEmCz0zxDP60260WnwZSkJeu9F-kpmstY6F5nnyFFylRbNdLFTR1BzZKzimBFV0v9t7fQ4Yx_F8GODqTDo28jArHd4TOwgg4Y0mfesEJOHr8Sp0slt1D0QOC0mwvd_44riB2pNA9gL5dhXbqVnTG3lIhq1B0Cuu63N9UK9lKEVBRGjIcPnUwW1bBB12VoOqY1FFU2sg877gqiBsN_QS-Y9joMQ_lEyiIyC7M-nOGOAH1M2T2pdCKu2pKopbq0ZZp1Vp4mWRf1B68W9AL83YxtOFBaYTeSwfWHJpvv9J7veYjBQ7nWXiM9UfxAAHvmMJUUSBKsKqN0-v-XmRWeA3zHZfjFDu7JzkhBq4dsqauNgy9hUF66WPjXtU83S2zuYUQfo-qFkT8WwI9sbsj445QTcd4eOk7Q3PySK2W_G8HZix2-zkk0cNn3EevpqPUqKF-tyTeDzl7zBcYmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2a4acd74d.mp4?token=cwEkS_CCsNeJTVuqT9E-zKqF0TFr35zXWBCtZiy8M0PLlEN6IR0ioVBM5Gh6SURDVXF_frJV_wL3WBZ6bzuusVBSwRAVJXDJRVHDix1FqHw-QzPhShl8lPzYw-2MPnMlg6S_CxqQcUrZEs6urtHZMaYhD5rALV9b13OfXaR9XQuO_zhqGBKJrmvsz2p94BRAUWi8i0PRjnHngugualBTUN0FYaf4irEmCz0zxDP60260WnwZSkJeu9F-kpmstY6F5nnyFFylRbNdLFTR1BzZKzimBFV0v9t7fQ4Yx_F8GODqTDo28jArHd4TOwgg4Y0mfesEJOHr8Sp0slt1D0QOC0mwvd_44riB2pNA9gL5dhXbqVnTG3lIhq1B0Cuu63N9UK9lKEVBRGjIcPnUwW1bBB12VoOqY1FFU2sg877gqiBsN_QS-Y9joMQ_lEyiIyC7M-nOGOAH1M2T2pdCKu2pKopbq0ZZp1Vp4mWRf1B68W9AL83YxtOFBaYTeSwfWHJpvv9J7veYjBQ7nWXiM9UfxAAHvmMJUUSBKsKqN0-v-XmRWeA3zHZfjFDu7JzkhBq4dsqauNgy9hUF66WPjXtU83S2zuYUQfo-qFkT8WwI9sbsj445QTcd4eOk7Q3PySK2W_G8HZix2-zkk0cNn3EevpqPUqKF-tyTeDzl7zBcYmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از دوستان زحمت کشیده یه آموزش ضبط کرده واسه‌ی اسپوف روی موبایل. چک بکنید ببینید موفق می‌شید بسازید یا نه:
https://youtu.be/spTJKgafNV4</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/MatinSenPaii/3634" target="_blank">📅 13:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3633">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aTbe1s_xfv5ukth1ntb78ks4cDr-G0ee5kU1WdNhwvy6JBJCK0wbKDzi4eZP0JZwhAKuH2oLDrQJulPRIr9eCmDdJHEFWxJ3rBLYEC5SLO8phMqCrYsPS7f-oFfQAh1qPFNY6BvrPrAaqeaCDkOPQIauKREbrMlp2Dga3pN4pltzInZHUsn30Bv4K8LCPhKX_omokACnQf5fmbqgFSCDgmzMKnRnMrQvmg11MFeC_EYUIJLUHNZJ82ei993GrAqQ30IXfU9tHQDwTEpwumSmlw_WNanMrKkadgn-ZP-dm7CHy40wwnGvmjfFiVqGZ9Vhzpqm06ZBu-OK3fYYMi0IPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همگی  از این به بعد می‌توانید از سابسکریپشن WhiteDNS در اپلیکیشن‌های زیر استفاده کنید:  اندروید: FlClash آیفون: Clash Mi  با استفاده از این اپلیکیشن‌ها دیگر نیازی نیست تعداد زیادی کانفیگ را به‌صورت دستی وارد کنید.  ما در سرورهای WhiteDNS بخشی از…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/3633" target="_blank">📅 13:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3632">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/3632" target="_blank">📅 12:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3631">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">MITM-DomainFronting.json</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/MatinSenPaii/3631" target="_blank">📅 01:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3630">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BF2hfkCpEizhGm2qMaRO8zfbtqBeamVp_Q-VEOrXmO59ZLsOcxqPF3fa9S0OMJI6yfX8_grybuu6v3QyUZ0Lk4nvqUIryV7hbT-nCApIM--Ic9oiek2EDwhyblyNQdVgDkYKvFsQzUEmtt8obAjyYyqq_cF2V0uv6pfxGRZ1qFT1eJQNrT1ZfoSaH8nUNdqXuqUM2n3smdj9n2-EL3adqp9OWlmgZkhUIK5J5yTqANxqE7eLgMtAx2hhYLcBTAsgY0-8cC75d2lMBfLynT_9kXISRIiZb0Oqw0FQrG6exfJ2oJ6qsKr8bbMcF37Le40bci62FIaNCYJFbUGr2y7AZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب رفقا آموزش شکست خورد چیزی که می‌خواستم بهتون یاد بدم فعلا بسته هست و پولم حروم شد
😂
خوبه ساعتیه باز میشه خاموش کرد سعی میکنم اگر راه خوبی پیدا شد مجدد یاد بدم اینم بگم که paqet و gfk کار کردن روش که خب قبلا آموزشش رو دادم(ویدئو سوم و چهارم چنل) به راحتی…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/MatinSenPaii/3630" target="_blank">📅 01:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3629">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دو ساعت درگیر این بودم که چرا x-ui بالا نمیاد روی آروان، می‌خواستم یه آموزشی ضبط کنم واستون بعد دیدم ipv4 سرور با چیزی که سنایی به عنوان ipv4 شناسایی میکنه کلا متفاوته و من سعی داشتم آیپی‌ای که وجود نداشت رو باز کنم:| هیچ ایده‌ای ندارم که چرا این بلا رو آورده…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/MatinSenPaii/3629" target="_blank">📅 01:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3627">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aFW87jFDp2gPxVzitx7QPOqBLAeNXQYcxPIvNYP_4FRadeevcUVKrZGAVS3735Vz9OKmNEKT42TYFzZhz5jWcjMdfqfy_ZcvN4szfBwnyqBWFEp5LCTvOngFUQ3qQsx0j2qhlErBcC-UnkdDRJMhmkvrnxlIY5UkvICvRjQnSXhe7tuMoHqUGDREOYf-zQ_gPj3CbnXagzmUrdNm3QWnUwNv-oBJjWyAsSVA028d5HCS7YY6IDc3b1nqKVX--PxD6r9i0oMy61NqOtwrRNksf5vxpj7C5D_hi2dIZc05Us9PtdOUJXtGaT3ZwSv6-O_rIyOi0M5ldRpLNNWnEDjDhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Olh7o_rsqBZcVPd-3pDpxeNkaPTGM3hkuI6PNTaARWw57Pt2qL2G27cs-O5ZEFrcbDrfL1KwQ2B_nOY_pO-A6O9ellwTEdOyh4_dg2Bj_1SmqsaY7rjMq_wNnCYmxhE2YC_lAFwK-guqavbS0dZdHJYma277MDgd3pvlpCD63zdTxBhMJbOyLuJQ35OkXUN3COJe7ba0tyodrc8K-PMwBPGjCowPAN0QrBdhcFv-5coaXafjxQQSOKw0yHyKFE2SwpmT10R9I2gXWWAJwEjM_PCK8GO-phsHK5NLcqZBsLYNlG7X7rIagzu_2lkjAAuk3L4X1w3iXox_nz0l23Xa-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو ساعت درگیر این بودم که چرا x-ui بالا نمیاد روی آروان، می‌خواستم یه آموزشی ضبط کنم واستون
بعد دیدم ipv4 سرور با چیزی که سنایی به عنوان ipv4 شناسایی میکنه کلا متفاوته و من سعی داشتم آیپی‌ای که وجود نداشت رو باز کنم:| هیچ ایده‌ای ندارم که چرا این بلا رو آورده آروان سر سرورا اولین بار بود با همچین چیزی مواجه شدم.
و اینکه با سرور فروغش من تونستم به گیتهاب و اینا ریکوئست بزنم نت بین‌الملل داره. نمیدونم از کی وصل شده</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/MatinSenPaii/3627" target="_blank">📅 23:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3626">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gFjRD2UTmuDRyFnEit68evKKTJKragWo0hEIkdLqise26wXlNX9RufzcATbPBBQOvU0DFO_IA5uIuCo76X9tBdFQXcabGxc076Ugmqhw6UaCb4fd9BCGZhfYTdfxLYWVluCDNloCBYnNvlpfy1Fy_HmWBUb-PKr_qrXLbDaO9gjRTYbbaV_PQb54gzH3xA8A6uDm5QNFBWZha1xHHv3RO3hIvAP9Sa4czFCl9kuUMapdxvdAFD2O66cl9xRAH1BgJFh0iw6N6xmUfa8RtnGn-sU0mTX5zjsxUYvu36Tj5Uhy1kx25W3qKub1CpYGUnyhvlzQlqXHVyBgcpctKZ0P5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرسرعت‌ترین کانکشنی که میشه از یه سرور خارج داشت، Paqet مستقیم روی سرور ترکیه سه دلاری Yotta
😂
با paqctl
سم ران کردم روی سرور
با آموزش اولیه‌ام
هم روی ویندوز ران کردم</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/MatinSenPaii/3626" target="_blank">📅 19:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3625">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ShadowShare منبعی برای پیدا کردن سرورهای رایگان ss   vmess   trojan و...  وبسایت https://shadowsharing.com اندروید https://play.google.com/store/apps/details?id=com.v2cross.shadowshare ایفون https://apps.apple.com/cn/app/shadowshare/id1612647259
📍
آموزش استفاده…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/MatinSenPaii/3625" target="_blank">📅 17:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3621">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShadowProxy66</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mw4lCxFpThlaiKDlWVGIyNI49zr4yyb_kTmGQUqfXDBoz2G30Tdj6y0tcK-NuC4FEZQMi-41p2ptc9PrR1k3dGp326DmgYp1-mzsl7pu-L4wQ2hdMDazmMcPlNtDHN7M95aQKdJZNaLdbJvKPMRll06oKgH9WCgpX4LBzKiihl2_LfZDmLYftrsB1mLz1GsvFTemvVFj96Qj834ZAULsx_KdYdF_COWtdD-VSXKvtqY4FaJYghti1Xhy03Mo9ApG4wTtK9ydCqVkUxbogmgrFr4_xuEUFpFc0o4r25iBECXl3RaTaYx7ydVZKV9Oa_7sDZqedIO_odWu3za7y6yUbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TGDuF5OJzAdHjNjXB-ch1tgeMozoi6d9-emAqjjKzSq-h8AgkIPSXRBQycTixLvf9goJLYUOXlnIwKzYl13dzx0WSQH2gHVYtmzcTxjIFeUQ30ekFc1slNV2y5MAONRbi8nIaOTNSmmpBZocivzgtEh_y-IEohXsaF8036g4Ze0letDUPVNz7PO_ybdEaorS_xRhjMVwWy-VM7-901OTsfRjLWAhgXZ9HH869ieDREf7YXRylzirIMWg9YOC_kXAicgMOwitUXYuQe0-xyxQSbHOTG8eodevOhXp4aUEer8BGQhmQLeQAQ7fGKephqdsRd6KJxVr4IQbVjtge2wnwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KiiIm_jW-7tIQ01wpsRmNsTCBAdf-jaTV_HtbfJPk-mr3wA3N-Pshcb4FjWGtutqZNUIaYfa5au8CDphPzUDt-oifO4wHv9FyzPhv-mrNd7JRCTTPLnUwePBs2Re0_yw3YViS9B_hv-lyBHnwLq9YOkL62wL4aKcgdAMZBxQ550ty5ccCG2eOIzZ76eed38rDn3au18LSm9ppzJDk3io0N5zV-VlY2aDaHGp1u65WTUIHiv_n4IXujyFWts2ulsoau6uCTWxXrtS1zTjVKcrdgMa1-d9R3gOXIoljRFa3bWerHw4HufEFf4pc3937RUp0due4C2Fm43kqCWM3U2nUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OmPym-_WXW92uZwFuKX2nn3qPS7eprapp8_HPvh2xvqpcVuW2eS_j58AKkiCFyKUuMdJA4CPWmQgVWll2b66m1qreZ1k_hcFkMLnTRxuQflLwMQBUVPymyCuLNHEUQzBT4zhmEGMOG-M5feyO2oBAMG7ZKH0vps0Rh6d8gBKb8Fs-pfzHMU4IzYKsZEi_rtHyCZeg2cEYJ3rAUwnZ5TkTyPjzp767QPcPwI1fXMg-5D2_aunrgdW07sI952xMGZ6VcIwzDFwIJCuVJt6giltb6E-XBejALp2Sn7SjjTfY2EfF0rMh-edHzZbJH1nV3rDX_T9k_YJVpMdb_RLFGAaPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/MatinSenPaii/3621" target="_blank">📅 16:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3620">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/azq6kMeC79iUB3tduftquu83Cpc0wDfdQzkkkOAQIEpiHPmQb2NQ2zIhx668gIlZ25ECOOYE6NDiOIVbAgPFPmkyx1-A1QkP_pmpfHr_b3xkKD8cI7gJ1OKhGbDs2Wy1mBuP23AS7T_5seKjtWmHa057yM64ttJq7OVpeExVXtEkBtH6iDfxiMV5QTRNL_i94S1-3ap1x3D3w-MeXoZ8JEgayshf3y_uigaGclyqea9fg-zB2xZ8SyjPwp3CJ6Tgrks2L2qIvMQceVbJ62xNWtgWDsJMxIxXr-r4vfYc6z05YxUbHyI7r7UBArDkVW7laRQrhTD1JpHF4kRXnLYrSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/MatinSenPaii/3620" target="_blank">📅 12:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3619">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/MatinSenPaii/3619" target="_blank">📅 12:12 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3618">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اگر می‌خواید گیم بازی کنید، می‌تونید از این کانفیگ‌های هیستریای مسیر سفید استفاده کنید: hysteria2://Masir_Sefid@18.159.104.97:443?sni=qus.masir-sefid.shop&insecure=0&allowInsecure=0&obfs=salamander&obfs-password=Masir_Sefid#%40%F0%9D%90%8C%F0%9D%90%9A%F0%…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/MatinSenPaii/3618" target="_blank">📅 10:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3617">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/MatinSenPaii/3617" target="_blank">📅 10:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3616">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBUgc-7IZuYyXGSB_F-Y1F9qSJ-2KlAhgxJWPsvsOM-2qN1T57-rj9IQ_mxXhSuqfywQXrv_Q3oGHRHBQxQaGqA8F8R6uPBACUHvOJ54rkz0kCIJUCfMuoh0R-Jz2AgsyswJYynMw8p0laJ02rLn5AjeZk7tc7R3vwUgKNKeKhNdxTdo3gzyDFQU177zp7ZtHX0F9j7tHabWsBCXeHwHgxHkfGXm1SK2u0WESyghDehlSsP8_38doQ-cqg51W-jd1mlHadyugCfAoYpeR0cZEp7tbNM02NmkfS1kVvyudVcM3Nc0m-p6k9qHUCitNOAFd2nSlo778aSvlHok8kh5yQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/MatinSenPaii/3616" target="_blank">📅 03:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3615">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ErUytrOol-oS8ULKQOxptzjrmIgcmYB0tYHoFaE3dzdQjvz2L-9PwJ-5A1L48g3dBJTtvsAaavbK6i2X9GzAE4RlwYgineUlqMMN3Kmec9N4VYHonXVitVaxNCikJ4zVkFTlGoCdc0qlISft-IRntAeOH94nEYfqnsY_KaJZSvfx4n6ilb8PATPQSgqZoOePmwg5OuBTz5ot4bGgHpVbaCncEBIFfNJAfkT8PE-9wadOGpzQP2mwR_VNm9tcUxSvS5CzciKqrG2HEk1z6UCundIVwIMT_dMh9ilzTPIVDQnHsMCW76CbmMrN8Ukq7oi6CvB6nWCOiYhGTnn-9q_l1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کانفیگ کاستوم دارید(ساب نرمال)، آیپی تمیز رو باید اینجا جای address قرار بدید</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/MatinSenPaii/3615" target="_blank">📅 02:21 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3614">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑇𝑎ℎ𝑎</strong></div>
<div class="tg-text">https://t.me/MatinSenPaii/3613
خوبیش اینه با این روش میشه رفت و کانفیگ BPB ساخت
برا دوستانی که کلودفلر براشون بالا نمیاد یا نمیتونن وارد سایت اتومیک میل بشن
همه چیز با همین نت بدون نیاز به فیلترشکن کامل انجام میشه
بینظیرید شما
نخبه های ایران.</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/MatinSenPaii/3614" target="_blank">📅 02:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3613">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/MatinSenPaii/3613" target="_blank">📅 01:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3612">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iKoXRlwgAdsIbCBw6VobLN3sOtnIkZL6YwuemH3ZLZRkjwiH2Vq27xhB46rEFpWYDremk3RRi5AkB1-9X8eTTc2BIWEiQcH89QF0PPRbpPdZaRLcupdBCpT-oNgsDwPVWiC-AJbjacwrqjGAABngQKaRu3D8AvRfZBauPtKOLTq1LOQPxIB36LtmW9CXqmJSVUExBlE_uxxfy18SNlZ6q4IvAEAXFr9jZK1liNd81S5Hu0Zu94IIvq1EjIbh1YyDxg9_SxDr5Qyu53397zUxzYzC2Dyn6x51br9K07NB_M5do3nYQ8PTlL8ovILsgQc18EJWxOGBXOWcE2_1sMqWrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیستریا هم روی اینترنت من باز شد</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/MatinSenPaii/3612" target="_blank">📅 01:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3611">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Mr Lou _ Ey Iran | مستر لو _ ای ایران (Rock Mr Lou Version)</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/MatinSenPaii/3611" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/MatinSenPaii/3611" target="_blank">📅 00:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3610">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دوستان اگر از Undefined در نمیاد،
1- صفحه رو رفرش کنید
2- حداقل نیم ساعت صبر کنید
3- اگر نشد، پروژه‌ی Worker جدید بسازید و دوباره مراحل رو انجام بدید</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/MatinSenPaii/3610" target="_blank">📅 00:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3609">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">Matin SenPai
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3609" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3608">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/MatinSenPaii/3608" target="_blank">📅 23:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3607">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/MatinSenPaii/3607" target="_blank">📅 23:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3606">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uJ0nW2fWDs-l_yUyssOYKUYm64I8Q28n-BjSNtfuXiMVJ9fUEg3Y53d_RUpL0hAZvFXpyD0IniFWOxQXmzv4l_DOY-lXQdDCvb2LT1CmhBjTw_Nmo4yS2cAKT4mqIvUfx3N9Gt4ibrjJ0q1fjDPS6xUkj7IuSGNdrDEwvEIGTkDSvB7lOl3yxZnOH6RdIntARx7-pU6Y2oKyXhoImxAaChKSX83ZpvbPttBpIiLrpg48pCDTa8f0LBWhc-_rhkXeobbOOxe9hIrtPJv8jiNYWgrg3Qa63lZ1abVcMX8vBskyVrK8khAKyHXGwQ1iqyc8jXg5Lm4LK_mbLrkTwCtX3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای SNI Spoofing
SNI =
www.speedtest.net
IP =
104.17.148.22
✍️
Kharabam</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/MatinSenPaii/3606" target="_blank">📅 23:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3605">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">☠️
آموزش استفاده از آیپی تمیز کلودفلر و اتصال رایگان به اینترنت + آپدیت ساخت پنل BPB
💦
⚡️
فایل اسکنر: https://t.me/MatinSenPaii/3598 پنل BPB روی گیتهاب: https://github.com/bia-pain-bache/BPB-Worker-Panel پروژه اسکنر روی گیتهاب: https://github.com/MatinSen…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/MatinSenPaii/3605" target="_blank">📅 22:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3598">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/MatinSenPaii/3598" target="_blank">📅 22:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3597">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/MatinSenPaii/3597" target="_blank">📅 21:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3596">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">جریان اسکن از اول طراحی شد تا هم راحت‌تر باشه، هم نتایج رو همون لحظه ببینید و واستون Save بشه. همینطور یه الگوریتم کوچولو برای اسکن پیاده‌سازی شد برای تشخیص همسایه‌ها، و روند تست و سرعت دانلود بهبود پیدا کرد.  https://github.com/MatinSenPai/SenPaiScanner/…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/MatinSenPaii/3596" target="_blank">📅 19:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3595">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">جریان اسکن از اول طراحی شد تا هم راحت‌تر باشه، هم نتایج رو همون لحظه ببینید و واستون Save بشه. همینطور یه الگوریتم کوچولو برای اسکن پیاده‌سازی شد برای تشخیص همسایه‌ها، و روند تست و سرعت دانلود بهبود پیدا کرد.
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.5.0</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/MatinSenPaii/3595" target="_blank">📅 18:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3594">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-7lfz2D3dsmS87Qs7tYc8jL8fV2CX4fmUFCdm99-6PxhHPT5eLpeHFTqMrGWTm6p_1dKAbLkaL2H3pRS5jlLgsA8NQNk330WUooMo2-z1BA-9b8qbEZG4W8UZSVMt4eUf7x0r75V07WtMJLJzXnEPYforMKoO_d-Dd_j-yWqDrkXwZ8JWLO_N6FmEajnRWTzsbEeERaDsxi5L7vw_teadR7leR7ByYJG72gGEGfSgNmRzci7jafuBGwPLCggzkoxgRfCFlUyGcblmpNfvtG_F6N6r8EeMVYMRReFosW5PHT4-YrKmG92MLvad5DNsSlzfmIkQ8WHyuwFc2h6_AdEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/MatinSenPaii/3594" target="_blank">📅 17:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3592">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اینترنت دیتاسنترها هم برگشت بالاخره؟</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/MatinSenPaii/3592" target="_blank">📅 17:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3591">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/MatinSenPaii/3591" target="_blank">📅 16:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3590">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v7omvDF8wa6HjuDOuiqn1eS4pPJPNhK4hrEuzq58VH7DIkcBvObGfJTbmgH11JqwyQdhVvEjtkYzBl7tnSoaQSlJ9-0W6C9iXrWKuwXNGyRsL9Lui2btHgfFrvgDNiDUEVcwOQc_73idM1LhZa8QmLTdrvilxurDtlQ6Te_dihwDh0_pTrR88lXigXSUj9XG_u5qEAX2eGbEbYGDj9ZzkcN4G1I3CBTuHeTBqK-ySKiHN9PG-pfWMPEbnz4S_YHYdv1fYaiaDsnTrhkswIn8PujbgH8WrxwVXreUC6K2rJxa1jTCqbS7btFPiJCI05F7t8tRZYZsM5F-ReolYizU1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه به این علت باید حتما اسکنر رو توی لیست سفید آنتی ویروس قرار بدید. ویندوز دقیقا این بلا رو سر BPB Wizard هم آورده بود یادمه</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/MatinSenPaii/3590" target="_blank">📅 10:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3589">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">متشکرم از دوتا دوست عزیزی که 105 و 3 دلار دونیت کردن. من تازه ولت رو چک کردم
❤️
مقدارش مهم نیست. کم یا زیادش یه اندازه ارزشمنده و کمک بسیار بزرگیه به من. ازتون ممنونم</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/MatinSenPaii/3589" target="_blank">📅 09:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3588">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.4.0</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/MatinSenPaii/3588" target="_blank">📅 09:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3587">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">مشکل bpb هم به کمک دوستان حل شد</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/MatinSenPaii/3587" target="_blank">📅 07:48 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3586">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GqZJrv0LJJebzlNc0NF5P2XOcx4MCcan6SA7hf6qm87Wd4QsqLUZt_2c7i6M5E3Y6bfEgLTBYGBSIVxafFImdeYHv7tEUHjTKkcbq322lu34j_athmIQesYzJMclBNmSksPWr76pDYXFAW2mR5pcs1dR9l4SbxTfG5dhFBirhUJkrEQVJkx_qH3saF4UbsVakHiP7lLFPE39ya0oiTEkWvpgQcBW4ZoG2KVMkZCaNKJoUfTWtq6Z-GQBHDnlVIN2tgxcLJeYGIOuPkl1zkQ0eCEmA8OKNxBZXmNDuxv75S6brqFm4USFO_GpWMwzCOEZVKvgna9AfzUju0hvbe0qKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکل bpb هم به کمک دوستان حل شد</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/MatinSenPaii/3586" target="_blank">📅 07:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3585">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LYLhwYKZaay_wRwJWUkji6obCNxhdLa7LoZ-lZ0FWgFX7AnpFUAtduSE5QjKArXgzcQ47GM1LmQ_c_y2nXy-3EbNiLHbYQ2O55pLMna80bx3gYs4vZ5Urw99FRid98rAaLtzQy1o5Jh0EOaVuc3fhydeOTw7aizdtZaX1ASHY7uhtA1I2v-wJ5dqEv0gSl_iWr6KDPmX3vYoykeguGkq7zERyelujLwLyYpmLjra3uZ1LuxXcoR2lwAaurFMZeguLO4UjgSdTUsQfoecyUAKCo3-Truqo00_ft7v3d-sGpWD4S14X7IKBXbddmeLugBts-mX1IpcDfy2AdcuuH6Y6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگار که عملکرد اوکی شد بالاخره. چندتا دیگه از دوستان هم گفتن
نسخه‌ی اندروید و دارای ui درست و حسابی به احتمال زیاد منتشر نمیکنم چون خیلی درگیری و کار و درس دارم، اما سعی میکنم روش کار کنم با contributerها. فعلا تمرکز روی درست بودن عملکرد بود که حل شد
برای همین prهای فعلی هم reject میشن همه. تا ببینم تست چطور بوده تا به اینجا</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/MatinSenPaii/3585" target="_blank">📅 07:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3578">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">31.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3578" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">V0.4.0</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/MatinSenPaii/3578" target="_blank">📅 06:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3577">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T0cT-v-hJ6ZqNQPbXd_m6Yg7V1T3r22S6Ic0iLgkXNfy4xNg07J6-jmV4Fkv9n9DXyv95c0Jfy_Zy5alppWDkZ_xQko3XSjHohxj6kedTJkQwn-Ct1B5Vrj1cNEc1kMVeFhtTdULSC5HC4KwTnoDYroLOmDWCRBQ9ICM6--V2eXHyXNtPI-3bFu331RvbRiA-J-1Q0T7H8VBDMh0Xst_znkCrrAplO5Wz0PauMsh8IMAp_1reh_pG0e9n0TAsE1AAHdZ5gU8k6EEkJ_EMIcl8E3R1QHcwupnzFDvdWEjYVj_uJtDU8z93lqjGuZ89JYwV0bYilEbxo_Uc-4XM-kPyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب، فکر کنم یک بار برای همیشه مشکل آیپی تمیز فیک حل شد.
و ممنون میشم تست کنید و بازخوردتون رو بگید. تا اگر مشکلی داره برطرف بشه و بره برای ریلیز</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/MatinSenPaii/3577" target="_blank">📅 06:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3576">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X0Ach9Lqr6fud5xxg0pZ24IvIUEKsaPB9n-fK1aOvwwqQfjNHKvhkvvLXNq6xfmXDLnJu6rqC7NR7rliJsc7NJxWxZEX7HtYtR1aMCDt9UweckvRKa0Uk3ZNIYNyAD_8eNFXkd_v6b_GBdzT82SlCAyU19WpvLZ_tgEuS6Nue5g5u3IJwqDb0qaZt5oaVNxMV-mGoGRWuP0ZDDlyf9mQ_SGIF0FXDsU1Oe12y1eTs0KYzgztTPGlJeds6DzYhMGCqyvbfBspD5nwODc3jkrzJ3-mSXOsneCz2GdciJ9vxpA2RleGkMbeMRPsUh_atddl03bDryTIi73Jj0a5WKyE8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پترنیها گویا روی یه متد جدید کار میکنه که به راحتی می‌تونه فیلترینگ الان رو با یه استراتژی جدید دور بزنه.
منتظریم ببینیم تصمیمش این میشه که الآن منتشر کنه، یا بعدا</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/MatinSenPaii/3576" target="_blank">📅 04:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3575">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">دوستان، اگر پیامتون توی دایرکت سین میشه به این معنی نیست که من دیدم و جواب ندادم
🙏
من میزنم بیاد پایین، همه سین میشه
روزانه بالای ۶۰۰-۷۰۰ تا پیام هست و من نمیرسم متأسفانه جواب همه رو بدم</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/MatinSenPaii/3575" target="_blank">📅 03:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3574">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oIuodNwL_Ez-8fG1ZFM1M1txZ-L6lCAVwdXjihGoSgAXZkilxWYw22Tp-tXD500i2w1hetfPvSAU4lsyaByU1w-82VtA2PjPCjAGcXeRZPboBVdeCdzeNgsY7DlVDwQ23lumUMKzFYD1Y-u6iPfMuZC2kE4R_smoeRyLJWwlal9oXohq1kRabhzPp5_k8wd4HsNzAdTIuFcH28HbHYieywWHybcL7NKeu3IbEZaHzG2DpFibEBbMCUc12aBBfKuOTnXxEG8P6kzxik8R_QA_eDv5PdVSbO-x9zwqQjcSkiCaQGgym3ri_yqgXmmI7W7vNBX5_fWynC2E-Kv3DyOmpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشتراک 20 دلاری Cursor اصلا نمی‌ارزید. خیلی خیلی خیلی زود تموم شد با اینکه از مدل‌هایی مثل Opus هم استفاده نکردم
اکثرا gpt 5.3 بود یه کم هم Sonnet
افتضاح زود تموم شدش</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/MatinSenPaii/3574" target="_blank">📅 03:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3573">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مشغول حل کردن مشکل رو اعصاب آیپی healthy فیک هستم. خدا رو شکر یه سیمکارت پیدا کردم که روش دقیقا همین مشکل رو داره</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/MatinSenPaii/3573" target="_blank">📅 03:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3572">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iNFtZh8dOFjfbt7Ax4xNFkFnivjbVsauOh83lRcGTYueVuuL_jugCT6y20PvoFc-sMjhtEc05r3wbQmfQD2JwRhi5gzMKz6HUXUjIe9SmZvhWWhjdnYHqDA3JPgh6SBncikUPWcelC7vjofEW0kRhcwbFe82i14JPqKaCtWZbirK1Awuf_rA-L8zKtNgEwYtiBHSAJZUq1E2j7ZIVIh9WZcy13qCblM1WffOQ7R4Aj6NS61uIhOEe0Z6eAMJyMJ5O4XasrJWH9NilGs5Vp_8NnTnSpN5xWjCdcW4vjaqRruJkk2iYskI5Q5kOv15q2qm62n9HpuSBfLxKs8Sj8OzBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روی یه اینترنت عادی هم این شکلیه نسبت. یعنی تعداد آیپی‌های سالم کمه و همین هم شانسیه چون range ها به صورت رندوم انتخاب میشن. حداقل 200 هزارتا اسکن کنید</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/MatinSenPaii/3572" target="_blank">📅 20:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3571">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">V4-Spoof-Configs-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/MatinSenPaii/3571" target="_blank">📅 20:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3570">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اسکنر همچنان مشکل داره متاسفانه روی اینترنت‌های دارای اختلال. دارم روش کار می‌کنم</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/MatinSenPaii/3570" target="_blank">📅 20:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3569">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">V4-Spoof-Configs-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">6.2 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3569" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">V3-Spoof-Configs-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/MatinSenPaii/3569" target="_blank">📅 20:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3568">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ورژن 3 منتشر شد https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.3.0</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/MatinSenPaii/3568" target="_blank">📅 19:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3567">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اگر اکانت جدید می‌خواید بسازید، از BPB استفاده نکنید فعلا. با این آموزش، edge tunnel بسازید:
https://www.youtube.com/watch?v=svYBcv4bSzo&t=618s</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/MatinSenPaii/3567" target="_blank">📅 19:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3566">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ورژن 3 منتشر شد
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.3.0</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/MatinSenPaii/3566" target="_blank">📅 19:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3565">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b9eSlMfksT9dosY0Xdp7TU34vt_D8MSqMopDmw4w7-2IcFiXrcLvBkkYAd6gFd_diQ6pKWkYj3CFgLiiOWYrujImdVNaMiAuPP-txi271cLWult_eyRIXmnysWbLCyTOthbbVZnUx7gskYAx0e6r6mkD4ASgCJa8YHeEN9tr62AcEQiF_-_fGEZtx8eP7pAIOdFHVjEZLzAV6cIv39NTy5GV4OrxFeh8HvnKshtQy_fnhv4q7tmP8Gle7x9GeUMS130P6qKXaEcwPHZDbrBFbQ5d1HpYTgkSceamJH7CDIZGgkzuW_LKC7Jl_MJv7jiXaytE2SAVnnHDILXGasqu-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به لطف دوست عزیزمون abolix، به اسکنر هسته‌ی xray اضافه شد که دیگه پینگ فیک نگیرید. همینطور دارم باگ‌هاش رو می‌گیرم که بتونید راحت استفاده کنید</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/MatinSenPaii/3565" target="_blank">📅 19:01 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3564">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">به لطف دوست عزیزمون abolix، به اسکنر هسته‌ی xray اضافه شد که دیگه پینگ فیک نگیرید. همینطور دارم باگ‌هاش رو می‌گیرم که بتونید راحت استفاده کنید</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/MatinSenPaii/3564" target="_blank">📅 18:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3563">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dY-Tj7t1gVg3eNpyVWVb-ZsS15i1cWD0Pzt4TzuoUh1z1GH4PmM_h3eF1ZrMh-wEgp4FNtllt6HZ_y6T7WNI4teikq408vS5QDS82V6fSpiIVzB0p-8Fv9PT7paWg-PDUJ3bwc7HfePTMtqvysP1I4ApJCpuYhjPMr59vw0jkte0CJhXDb_d5fQLuqa5KTPIdcoSbWKFslCqFHCWiGjIelRmSL9a8yZ9Nhe7GEbkXwBazToptVT1EyKgtx90IJaG2j59Uz_E_G6s-yotvKg4c34DCfnLA3nupxD2_Kwzfp_Viw0k9lm2CTFUlTrfCYtD95DCp5NqF4CUKoOQ-MrXeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">BPB - Edge - VahidFarid
فقط Edge داره کار میکنه. هر سه هم روی یک اکانت</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/MatinSenPaii/3563" target="_blank">📅 17:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3562">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خب انگار مشکل از BPB بودش. چون الان edge tunnel بالا آوردم کار کرد اما bpb دوتا بالا آوردم روش کار نکرد</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/MatinSenPaii/3562" target="_blank">📅 16:56 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3561">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">امروز به دوتا نتیجه‌ی مهم رسیدم:
1- روی یه سری از اپراتورها، اسکنر نتایج فیک میده
2- پنل BPB ممکنه از اول تا آخرش ستاپش درست باشه، اما در نهایت کانفیگا کار نکنن. که دارم سر در میارم علتش چیه. فرای از اپراتور این شکلیه. یعنی با یه vpn دیگه هم ازشون پینگ میگیرم پینگ ندارن با اینکه tcping میدن</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/MatinSenPaii/3561" target="_blank">📅 16:48 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3560">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">همچنان از
@Whitedns_Installer_bot
می‌تونید کانفیگ رایگان دریافت کنید. تا الان 21 هزار نفر دریافت کردن دیروز و حدود 5000 نفر، حجمشون رو تموم کردن(که امروز دوباره شارژ میشه). به زودی مقدار حجم روزانه هم افزایش پیدا می‌کنه</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/MatinSenPaii/3560" target="_blank">📅 13:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3559">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یه آموزش کوچولو داریم امروز</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/MatinSenPaii/3559" target="_blank">📅 12:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3555">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vcS_Mq_yt5SscXcDgfi8ZQ69MHvevHFhGzye7C3qY-wNTazt9ya3lsuPzro_BgUIve-Ob-9nVoKKMnNXDfj7MVnIOhorqiWfRzhPnlsdxD2Vt5Uoeqbiu5ssA-jX5hzhIMaCnsmW1rVINybJ-XfvFb3bCf6tl2niPTC7DnNts0fi0lHPhnT1dDBWGLRuMFd2g3ckXh-uxsmL8ZOJVAKiSI5ntFZsJIuqimM0kbc2tW3FGkL4VhkMu_gfClENpyrchAMg6oVXQt9aSw2J5FHCTh4oG5L6-RiaWqXBKYkWivQqTPgepDr29zBDrYfQOrjrqTOVw74bf90K99lYOe8-rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J_M0ovuJZOepal4snVkNmaOdlcCecuDJAvTNM8a3vu4_1Rh63xgwNkI3vYpsbysLzmX64e2_9c9aNNfhzeZkoZjJI57AAQKbIjgCD8NovCBS12odIG07wrIp6YqJcVG2Z1HI2hCmsfln1x3_rpMilr-qMeXpnyge7gV5UKqnAVEm3woby6axlHxCXdKoX0RDjxtXRUTwMS1PLbRdLy6jHBOZBTTcWCfmvn3_6qSWqy1_8CnozelYw66gB1wcGq1n_RmnRxsuwWHGQmE-qFkvn8KfT-1qFc3znaQKDpSIIEK_W_4y5B0dMQogKABgdgI5SxwuIzQoxOnHgHdMbzwesA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qinq2uAs3pval4CnJWSrNYvOcYCvud9Z7RW0u3DCgl3_3pt0D1ERSWsBnLRLzqqBi_cp7vKFpdjz1ZJKsZmnlri7NiKuBPi4NXxwlnpsxrxDN_AK7T7VzMMot2F6voP_apt8uC0z34cNsuX9Jxf5y5GF78o5CCxWvrOyDSAUi4AkkywcHbO836znD9kX_ODvk8ARJoj2cl5DlzFZoQGgrOY-bl1ewMP5GQM1TrUmTeVMhPlokivAJTJvHwHcRf6A87RXsVES6qjTEjNTDawYoNx9XegdddDfFcinjoqt3ydSYzQdcaykdnAB0VUsg2-cns2dmYX4f7-0tGwm2xJQbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VF1qCfwA8BsH7DMG27O-SME8SRyC32XY1EwJkPmxTPOYlGD6W_YXKv8neIlz5DK0Fw23SnsbTZo6Rgpa-hBzlJLMDak2DtEtiK4XiIvTBtVTHU7o2xBbVFB1ugEPgINxNqA6Uo0UbrsVhN8PR6ky5HGm55TDTi_WbfkIBDP2HzX3PwKmVq_EQX9MxJhk5xs8e3WLB-9v_6OcxIu-aDuAajdMODpJZJglcs1o8nK5u7lthJOIf1KvskmiIvmXENg5uM8u0_I99cc1QPDJECq-0-CsTxDA1zZdocIVqQUapVJLyl1HPJa-Rrx53lB7qT1Xls0DZt5XntHbG-G2wV7LHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/MatinSenPaii/3555" target="_blank">📅 09:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3554">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اشکالاتی که فرموده بودید رفع شد. پروژه با هوش مصنوعی نوشته شده و تمرکز بر سادگی و استفاده‌ی راحت مردمه. اگر اشکالی دارید توی استفاده باهاش بفرمایید و issue ثبت کنید یا اگر خواستید، pr بزنید و مشارکت کنید.
باز هم عرض میکنم خدمتتون که این اولین تجربه‌ی من از اوپن سورس هست و اگر اشکالی به وجود اومد در آینده، پیشاپیش عذرخواهی می‌کنم. سعی می‌کنم که یاد بگیرم و نیاز فعلی رو خوب پوشش بدم و همینطور پروژه رو هم در بهترین حالت ممکن maintain کنم</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/MatinSenPaii/3554" target="_blank">📅 04:05 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3547">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/MatinSenPaii/3547" target="_blank">📅 03:59 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3545">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hsRuqQI3GTvuPfAXz1WFsSxRRP2HLhWgMtvYU11HZVME85SIY5J8TGnlUB1qG2vJTmScl8w5ux4IqTE1ZdREFHYHrcvEqMz9UPulH8TkE8E94hb05b0d8Vu15GNA9F4j2PDzIEMFgVmn6hjZDWRo1tPrTw-PDzw9CXbjmDdHxHLKlqai2uk2bdLuTR5tXu6jfHsgXCGe2jxovPnDaV2eLrW8RmFTNG4rm-xejFzwHYehPZ7H6oEmyM_h0r0kN3QVVsyRpPlIN3_409V23FTe8OwDijjkrB1rr-NgFRRHWKjYzoRG1oZ7olzoM3_CQuH7yuL2Nn_dCGkeTKx0sSWy5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RfDNZF6NMHLX7xBkZo6M9Ec9dokPYKZZsTnD7e2IzdPXVNY1QRJ_7sP-BJdPBg_JNJicRhHVrPB7ypmD84hW1fWsyn8aqhVx5Yuw2ZuEoLcw84uMEyg7zdKzKD4zXZkrZm7E4k3Zl3SYUT8RXGwmxwlI9s7Nq6SXGTv4EbR0iPazi8mczSrSW7N8nJ8Nk8uZ-ARNhTw0AKS4aho9X_1NR7HfwPfDc7HSN-G52t4egAwAyR1ezREnb-TjgCC1pUUEogprO2hK4C4UM_PZCuCc_NTy011j62YDXfV8UHpxqNC6pGgWjBcp3pWSPveoKYYt6UVhPB6ue0y_DdB4sLWLyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توی آپدیت جدید اسکنر، آیپی‌ای که Healthy هست واقعا بهتون پینگ میده!
همینطور با زدن دکمه‌ی c روی کیبوردتون توی تست لایو، میتونید این آیپی‌ها رو کپی کنید.
یک سری دوستان عزیز متخصص هم برای تست بهتر، روی پروژه pr زدن که دستشون درد نکنه واقعا.
تا دقایقی دیگه منتشر می‌کنم
همینطور که توی تصویر می‌بینید، یک آیپی به من healthy داده شده و همون داره واسم کار می‌کنه با سرعت عالی</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/MatinSenPaii/3545" target="_blank">📅 03:46 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3543">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vCss47mdNKoBdsUkah565nLE4FS_0Eh13a7UA9j43Cp_YcTb3Pc_ti2jE7EwhuBgPmopg02inrDhxfR0Zbj8grHFYn7AfIar0NjfVeY29TkJToPa-ehxfVVqTsd_mrR_ykfCyZ0JbnqRh5bxIe-dhqusZ8o5Ct-kvSsveVVjFfQSHOWXKTbyzSMW5NuHqHbTN3NN9N3Qd2YLadiRuKUl21Ow9WgVe3ZFDecoxz2cz7NtPD9oD3C3qreKmhHqo6LtzxfY1q7WqiQqzlFkSFKJiOLMZOs4lGqpWnUmDlR3VbIzaUWiCzMp2d37-qMGumGhypFHTkdW5azb3Twjr4xvaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازنویسی یک کانفیگ تکراری با آیپی تمیز‌های متفاوت!
با این پروژه‌ی رسول عزیز می‌تونید این کار رو به سادگی انجام بدید:
https://github.com/seramo/v2ray-config-modifier/
این هم نسخه تحت وب ساده‌اش بدون نیاز به نصب:
https://seramo.github.io/v2ray-config-modifier/
برای حمایت از سازنده، روی گیتهاب بهش استار بدید اگر دوست داشتید</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/MatinSenPaii/3543" target="_blank">📅 03:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3542">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYAq6d8w_tRtZ4MWO3Yf2Lalh9hi94RLdHFwJMGpE-JCjhLIPIgHftraciZz97OpFEtd8F1tyIdDq9vXnPyqPHxvsN5kVz-pe9gSLLtXLN4VQratdLUi1i54YOdvjol5sXHDQE7tIg1T0jkSOF2jlKUelie3jpjc82SZD5MYFDHmSzZ5Uas9DYJbV50p8dQxZrrheZ5tVtycqIpXzAdBehoLnLMPwP8YFAYtL7Pgoinu3zoRPiriZvOdkkeq6pv0nZbO8Z5QMVD5R6jO0gaVOim5X08MK-_K97xhTIjjPHZr_9ImLZ-l7U0MoTkGhAZd0qvvE4PUsl31vIrCZxkkUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با شرایط امروز اینترنت، دسترسی به کانفیگ ها برای برخی اپراتور ها امکان پذیر است و برای برخی نه. ولی راه حلی هست که امکان داره کانفیگ هایی که سالم هستند ولی پینگ نمیدهند رو هم به کار بندازید.
با امکان جدید ربات
@Whitedns_Installer_bot
میتونید کانفیگ V2Ray خودتون رو ارسال کنید و اون رو تبدیل به کانفیگ هایی پشت آی‌پی های سفید بکنید.
وارد ربات بشید، روی «تبدیل کانفیگ با آی‌پی سفید» کلیک کنید و سپس کانفیگ V2Ray خودتون رو بفرستید.
تشکر
تیم WhiteDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/MatinSenPaii/3542" target="_blank">📅 01:58 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3541">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دوستان، ترجیحا همه‌ی پورت‌های توی پنل bpb رو باز کنید. چه tls چه non-tls</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/MatinSenPaii/3541" target="_blank">📅 01:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3540">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دوستان، ترجیحا همه‌ی پورت‌های توی پنل bpb رو باز کنید. چه tls چه non-tls</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/MatinSenPaii/3540" target="_blank">📅 01:23 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3539">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خیلی باگ‌ها پروژه داره و تا الان نزدیک به ۱۰ تا issue ثبت شده و دوتا pull request
دمتون گرم. همه رو اوکیش می‌کنم تا صبح
❤️</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/MatinSenPaii/3539" target="_blank">📅 00:39 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3538">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ol0M5_20_8K4vyAWRvrC4qQerJ3a02KaLfPGOTkZhXauITnA6Pg0GBpsjhzu3V69NJAiISxI3A0GNo_bNHiGxTBGi3rBgT-Kozl7z9KssKe-WyZtHRh3L2roztqJUSGeOicD-BUsh8BD3SdVj_Ok7cLRz-ft29yS_NO1pm0DXKlvceioOtGm-QqhY6CU2Iuy_3fag_vAc_QcwbsI95SQUcWSguwFQntjBCdePyC--4jIyBFVv2chZLWWzO9tZRyg1jeBjtW9rZvhsVF2kvPBlAIS5WkFGqGwkjS87acA_UpxcyrVIqaavpt5-_Nsiu2BH0Uj9BsAAgDjssHO7-j9Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اکثرا جوابای خوبی گرفتن از اسکنر. باعث خوشحالیه و خوشحال‌تر میشم که دوستان متخصص issue ثبت کنن یا contribute کنن
🙏</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/MatinSenPaii/3538" target="_blank">📅 23:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3537">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">عدد سمت چپ اینجا 104.16.90.120 در واقع آیپی ما هستش عدد 2053 هم پورت ما هستش. ابتدا بزنید روی گزینه‌ی ویرایش کانفیگ، و بعدش آیپی تمیز‌هایی که توی کانال‌ها می‌بینید رو، به جای عدد حال حاضر آیپی قرار بدید. پورت رو دست نزنید.</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/MatinSenPaii/3537" target="_blank">📅 23:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3536">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BcPL9U9gyHJpObLt4Y1uiaX0bcV9EYB-_NLj-S-0QhctREuzMMffDBchYv46VnhkuV7TYAZLf8_qvoiH0w1ASpe60ycb2HyKzkZ0sHfIFjSPdrEwiYod_KhLuKhgvt9xeIfCOFghZQf4229mgmzhqXXjQzXEQO-9JJLhuV3kaIS_DnuJWmDlgoFC_GBGue7eLq1QS72U1PJwkqArxuOLlV4qXnECKjjo_HIDE6k3d-9S9bCiMl3JPeQDNci2tq1Fk3ZaVXECbDBCdbXBiuYywj0XYMEpH4u7Hc7lgHwd4ixLACgwK86PyfBykza_n_15B8jYH_8A5dQnbO-zV1-LFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اکثرا جوابای خوبی گرفتن از اسکنر. باعث خوشحالیه
و خوشحال‌تر میشم که دوستان متخصص issue ثبت کنن یا contribute کنن
🙏</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/MatinSenPaii/3536" target="_blank">📅 22:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3535">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CgFXs1_hM0SPuzuF-um5rWI_ohN6ljuixVGVwJdhVoE4jPYDGv2U_eUlCrUgs_QAph2e814nydqAiKW7uuKMpZh4IIlDkF3Uw_Hahg9fs128eGByRNG6GWblLF8K2tI3B5OEIfRK9d9RB7K5luWNOlKOTTWAHEwh9-AuQCeEVx5QCPXHSNhwnW1XrQWWmbRZoRjanpPU8vW_VYIcWVvGmFVFuJhBE-M7ia2y-wA7z15Dh5z14P-1C6M7hEIICUiRobuFxP0mMKWmWpSgEYFkFbiw3CL9eTRxgM3r19tBOsGOqPSuS9CmD1k0ilgpBjK_IHaby1T7aqntIfjhddFXNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌ها کاملا رندوم اسکن می‌شن. برای همین باید تعداد رو خیلی بالاتر در نظر بگیرید. حداقل ۱۰۰ هزار</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/MatinSenPaii/3535" target="_blank">📅 22:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3534">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این اولین تجربه‌ی واقعی من از اوپن سورسه پس اگر کم و کاستی داره، ببخشید. صرفا این پروژه رو زدم که نیاز خودم رو برطرف کنه اما دوست داشتم پابلیک باشه و یه پایه‌ای باشه که از ایراد‌هایی که روش گرفته میشه، دانش برنامه‌نویسی و شبکه‌ام رو هم ارتقا بدم
❤️
امیدوارم که این پروژه‌ی کوچولو به دردتون بخوره
به شخصه از اسکنرهای پیچیده‌ای که هزارتا مقدار داره داخلش و نه میشه به عموم توضیح داد نه میشه به راحتی ازشون استفاده کرد، خسته شدم. نیاز داشتم یه اسکنر داشته باشم که به صورت رندوم، به تعداد دلخواه آیپی اسکن کنه و تست کارکرد بگیره ازشون</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/MatinSenPaii/3534" target="_blank">📅 21:23 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3527">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/MatinSenPaii/3527" target="_blank">📅 21:20 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3526">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rTBaMXyUjFoZ8spMrmgiZRZCQkav0n9BWe_aH8GrWrG5ao4oNLDgOz9KOkWBo9I6bAgcfMkQSIyt_iHsv9Dij6GRvPn9N-5RXARPRj5k9N8QWoYjxZNVtNU8kppENYQGpgV0ftldktND5sd8bIFO6WKgk3Ils2Uw48K8IdQKVzc2M2Y33Fq6TgaOToiOAUgu4SgSQxj7BFj0K1bGJMuR67SIaHtYfDgprpa-mLmxzGLAa3dXk92GOVKq_RUe3T1VIgpq8YCT4yiew_hGcTn5kFJukOomekUEmiiV98qJTQ6kgRgrOmvM6zUDOjAI8YBZzvFIMoymDrSEE0m0DWD0nw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/MatinSenPaii/3526" target="_blank">📅 21:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3524">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HBGVKkfi8oAfOfAhHXs5KSFBMEtVBVbP-o34maFTsbCPSNRBDmPQDxA1qtPZ6hQnYoH-abt2L7co1dREdmU1x-E9KaLMFxWxeNwLEjwsutJ1fCvV-t6UUPRhD7zp-B946TzLw62ErEPlO9D9sXobTERMWoH0c-sHVgR31kLb5avNrsEFQTkhWBaph5KBHDp6pG7yW_thGmcA-2lE9050jd482z-Hu4ubFDcyaAppAfU-HK8Wn2fWKTZysXFhOyWoqBi5BA-SjFnLmVxus1ODCpuM1wSRRaiTyLzxZ2UeNyzJNgt-cotUsKXSBT9yD4I7hofcUXktLs3Fpz00zxmErA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JcTXYqiOBIyed7rE3PpXYiwcHlUTkBfOwFqRjgN3oeD56JFlcINWlkBPjWuFHzlveOEKWyGQsq10zukEoPZQUPEWJNeXAYXqkb70qg2SAQeAW-g2ykKbPbwi9LVjE1XLuEL_tB64yW8fnEkTUApKMFn83ZyG84a5HDPcmi_EzkFW6NOAofPNola-eXJaNaAQWEG2bL2YrIkd-LbB0te5gmNf30d-ewL6fVn3ceK3m2r8ZxwFt5ZF_r05HxvpQTlb6sX2ToTYw0tCbuVuJmeMg8LorHTo-1ygCckCZWCnB4TuO3RdtAoHdsxl5yGBp6AtdpvWpjXx0tOrlM3v70ceTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اولین آیپی ای که اسکنر پیدا کرد و داره کار میکنه
مبارکه</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/MatinSenPaii/3524" target="_blank">📅 20:25 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3523">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آیپی تمیز مخابرات 69.84.182.49</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/MatinSenPaii/3523" target="_blank">📅 19:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3522">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P8QYEjaMIl8Is0xadprr2-LxJKnnCZXlAMeHW4JsAuhnfD9PHg8MUvMYK0aQtwH4vBloaUCPq4ZR8X_4IErsHssuM0TcTkIIQ0Tj3ddbiuof1d5-plEwmxh4SGxZCPG5yPO8LblNud0g0tJymO02jSj9EHB3daEYogZshnzA1Qn9G_hqwhnO4AT6so2nVsUQI02bmtz0jG3yGMW_ApPfDFEt7WTMK8pjGnHSSNy7NonBQU-THYEhX2AIVbOVNJDzD3_CkCglgNmCo5l9_Bsm02xMaXo4EpSwmFw7OqzjuQT0x5xPKYgnZe-GEJ9jcHiTRiD2FOohLAcv24fGczIkGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عدد سمت چپ اینجا 104.16.90.120 در واقع آیپی ما هستش عدد 2053 هم پورت ما هستش. ابتدا بزنید روی گزینه‌ی ویرایش کانفیگ، و بعدش آیپی تمیز‌هایی که توی کانال‌ها می‌بینید رو، به جای عدد حال حاضر آیپی قرار بدید. پورت رو دست نزنید.</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/MatinSenPaii/3522" target="_blank">📅 18:59 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3521">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s69FYCwq6MAM0-t1r97Z3D57oG0LfiZ8ef4igAPgbqSDvOhXs_k-fKEFa0_BRvIoNfiC17piRhE-H0KUwk-rRSSfQ0aBN-ZAHJyJMiG_DTbKrGsavzlv2Rju0jKzTdC7C_0rYMfQx-yKF_rvz3dnx9g7Tc9lBmPaUdW5fiml3-TdcpVpFpxmvkweJsgulllo_FTJS41sq95hJpHdPJr8H5JlpgtELYXMc4hvNZwm3MZO8aroUYfKn_cz_b_B0hD3GyO6ACUk_xdEdZDVydd2B12gNauNssV4qhEBSfewaNcNTwOAgY8UPC1ooCpYeDmcga-u_icpfVxC724_rwhgMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی تمیز مخابرات 69.84.182.49</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/MatinSenPaii/3521" target="_blank">📅 18:49 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
