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
<img src="https://cdn1.telesco.pe/file/abLHLQ7tS_nDGF3NFbVmkGjDtyFJW1V8wjsn4TqehlMr_1n9wbuY-pQe4t_LU-awIpU_iXAUwiUTlak7XpKxPB_Pjk4xy89evH9dFDrLu_DDcd7TWkkugJ_O6RWzCClfClo2_Dlu-PmHY84W6wmglGcNHFrStOFr6nCvhfNQzVp86hpyIZ4TjldkacU3pS_EFIiwfU8CMdlKx_po7G7r1lneXuAGVHsFJbDBnrDcairvY3muUGEXE5SqAvpvmlER9xcdPavXgY-6nf7E5emLcOGU5bLiZkPa9HYU14gvgj3IFcMCJ_L4XKKHHzZdOmL4Bvb6_i4J3SoJizSlVwR25w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.3K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 15:07:03</div>
<hr>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EI3r9VpMy4HIVlqTxya2ajNhCcttJTPBGimG7poSHKATLwzEXAjaFBD9zNdxpF9tA_QZtVVwQUrK1a769MxgRwYi8ppxjC0-qQhYD8xZHIszm-ZGJP7HFsW-cnAwD2KEDbc8-qwsHd9Yqmm5L6qd5rT4QR3iav5Es0X4W0_O2UnGJhs7Loq7jlq5CiunMhQqZMgtB8kIa4sxDkgPGD8xtCdfe8ST4h2vxyC_gnKbWvXJ0CKRm-cpR07TxRM1VCa5HpueQITuXCucbTYxCrRqt2DNdP5AJEuQOm2naka1ffAVzzOajr8ludwYX4ripGHo500MsKDfd7CcNVORS_lrNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتابیسی که ادعا میشه مربوط به کاربران فیلترشکن JumpJump هست، توی یکی از فروم‌های دارک‌وب منتشر شده. منتشرکننده با شناسه leakhunter ادعا کرده این مجموعه فقط شامل اطلاعات معمول کاربران نیست و اطلاعات شخصی و نسبتاً حساسی مثل اطلاعات پرداخت، اطلاعات کارت‌های بانکی، تراکنش‌ها، موجودی، لاگ فعالیت کاربران و اطلاعات دستگاه‌ها رو هم شامل میشه.
البته فعلاً نمی‌شه صرفاً بر اساس ادعای منتشرکننده با اطمینان گفت تمام این اطلاعات واقعاً متعلق به کاربران JumpJump بوده یا اینکه کل دیتابیس ادعاشده صحت داره، اما درصورت صحت‌سنجی، همین اطلاعات نشون میده جامپ‌جامپ ظاهراً اطلاعات شخصی و جزئیات مختلفی از کاربرانش رو نگهداری می‌کرده، که این نشت می‌تونه برای کاربران دردسرساز بشه.
اسم JumpJump قبلاً چندین بار در گزارش‌ها بعنوان یک اپ ناامن و مشکوک مطرح شده بود. بنابراین اگر از این فیلترشکن استفاده می‌کنید یا قبلاً استفاده کردید، بهتره موضوع رو جدی بگیرید و حواستون به امنیت اطلاعات خودتون و افرادی که باهاشون در ارتباطین باشه.
©
hamedvpns
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HaE-44o5k-9z1CQ2E74fclaaStlmvtWRb1u7FghH_tVIeS1KFghLbT8tw-8WHHi2dTXACf0dz1OwWsp3xAyAWi_u52Y4SF_K0VJaMPE4KWTa9M-nF40GanNlrDthsmJ7lf8ISt5fjZrrsHnspmtGAjjnl3escL4GQXviNpF78QLDDy05aCx1G9-wdyFcLmVMZxgOiYAXLBWn4EWyyTdjYLjC2MzKPgRox_y-vg17s26zzgkVVBJyFiu4CuHhjhPWTJ_nduP5_KFXmx3IsoZKDJ1b1fyYfoNxOdwhFFXngrQE7xyEjhzxG1Q2AlGkjCnabsCX9NkgFDpzGsru8YSFhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/okX0GCKhE63Dla5-u5t-Eez4XZou8eVGHg7Uz_NJPJiqu0gElvbWn2KETvvSWgKjKv_kT2Q4EFNZ8UvFm-58yrFWr9NbcUCM_wTMFQ-xAR5CIDpt1HTj1bexDcZSsHrNDHS28Pp_OOanaqpj0Xz5QHKdjT0ER81nxnaPhKNc2Cw83DXfu5KqQ9ObK7qGdGiXqLQ5Czx7T65_5umAGLeAyeMNZgadPtn-wxnZGx5YoYbNWfv5wmAKihvc2i02iSiiO2aLKy9god9d6rbp3Bk6eu2U_MlL3Ot0g8AVuHyUp_1txnJaOpR8aMztmM6v6caxhBLScF6HafGhg812fjzRNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از مدت‌ها وقفه، بالاخره فیلترشکن Oblivion به مسیر توسعه برگشت.
در این نسخه که برای اندروید منتشر شده، هسته برنامه از وارپ‌پلاس به Aether سوییچ کرده، تا امکان اتصال و دورزدن فیلترینگ از طریق متدهای وارپ، گول، مسک و سایفون فراهم بشه.
👉
play.google.com/store/apps/details?id=org.bepass.oblivion
💡
github.com/bepass-org/oblivion/releases/latest
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T9Nmq2xXLcTsK2dJdRQkhhjxMTtL1XK_H2ewadCvl6fV68LxXw56IMzkI5WvFsAhKtUeL98T3PIUKgL72lq0RoiNucAI7rq4ZNsghFNPz0jCCoeTzoE0cWNfvVu5rZwUOHzpy2b1ih0Ob0Bhc15ycktLOcEIlulSla21uP38fwV8viheOyzDVWqfdc100GK2PprQAen9p6d5e2xDwTWbD077E5sPp0sBbheIVFB-fOV5z8ByCifExXqMhqOmwrFhnPDHk79Uf1EY6GthPlqjNAtAllgHsJL_B7YUnFMT_izgTlFcoQTEPVtbygY9UeYxBZJIdo3tDidwsmLLZuTFhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل یک آسیب‌پذیری روز صفر با شناسه CVE-2026-85046 را در موتور V8 کروم تأیید کرده و هشدار داده که هکرها از آن در حملات واقعی سوءاستفاده می‌کنند.
این نقص ممکن است با هدایت کاربر به یک صفحه آلوده فعال شود و مهاجمان را قادر به اجرای کد مخرب، سرقت اطلاعات یا از کار انداختن مرورگر کند.
لازم است پس از به‌روزرسانی، مرورگر را حتماً دوباره راه‌اندازی کنید.
/فیلتربان
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sH6HU801uPsgVcLhQrR0i5wjIwZzvA5FOByfJNRkp7rHXop93OaA9wdNkPoIeR03NpPvo4U5m63buhWmNXVZ1OgDchJzV-uX9i1vsTCEMNN_0ElOG-OpgkBYZxeJmAffdQe5vr_J5Mv5hns3Nc2wiPGSpMc9SaHcDnBaEatL5nsa89X5qeSI_4qT97WuatcqldzhE6nzq6jqIvKeXzH2fZcL00zATxiKnX9BiW6VO49IeZW5cVtmW300ETezJlmyoOV6iYLHufLp4adwd4dbPjUxJD4LHO47y_dAPxqFTigTbz0ciQU-YI_v1gas4P9cFUZeDQeqi324rnjnQRI6EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیفیکس اعلام کرده که این فیلترشکن توسط تیم امنیت
پس‌کوچه
مورد ممیزی امنیتی قرار گرفته و تیم توسعه درحال بررسی نتایج و کار روی چندین بروزرسانی کوچک و بزرگه، تا در کنار حفظ عملکرد و تجربه کاربری، کیفیت و امنیت برنامه رو بیشتر بهبود بده.
این تیم گفته ممیزی‌های مستقل و همکاری بین تیم‌های امنیت و توسعه، یکی از بهترین راه‌ها برای ساختن نرم‌افزارهای امن‌تر و قابل‌اعتمادتره. هدف این فرآیند، شناسایی و برطرف کردن مشکلات پیش از سوءاستفاده احتمالیه و انتشار خبر این ممیزی هم بخشی از شفافیتی محسوب میشه که به‌گفته دیفیکس، کاربرانش در چین، روسیه، ایران و ... که با فیلترینگ دست‌وپنجه نرم می‌کنن، باید ازش مطلع باشن.
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kM_kFcVDnL76fHJpqRJI_S-mFyRRqpNMFdVZQ5ZT4KU1hDYniYtTDVdkgPSqpawQf7x52KrnS8ho8fVOP-t-MtWi-kRpdW8I5P7ds3gg5GjtQYsQWqxPbhvzxzC6mUrBPN94NIHCPhn-azEWkV07HBG7doJRoDGZkrLamS1aBfgACttxchFXFKnUP0sLX_DDSkTeg7TCaWQexmuW4gwz6Gx2_hJgDhRYR19mqyITH9zvbVq23v3ljqLTwaL9MFjCA-fK7UG6y2DEBLBydhoJt1RINy7A758ASVwyHei0YmlFzNUmvhG_lr2-xE3oH5HgJkEKwEJGckwlQhONNXvgzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jvUBUfdZDSSUWPXgmylB5ZjTngLidS9ql0Szc19fAHcgi2LLtKpFiyc281ttgN8kWS6ME9hh84c57Urh1pbc1lDYbJopY2vpx1vjF4vKaQpyEIKUhxKtK1igJHR859iaYqt3cHjGxhcALLj3QbqTv7IXRm48ZLdzQmfgwbK-cuTv2PeQl4vJGLLPscQnc9aoYeI4GLWwl3Xe82Xb5rjLLfenjNE0rV-0up1GwOvhr4puM0Px0rx5jLfxGddW7sRZ9BPAoFCfeq2Msb0mPmyyzBaKnOKYji-hUq4gJkskWKGe98G1VaLWyIT-oSIH8tYAScX-bfxScBJMnjdjzYXwmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سم جدید
😃
☠️
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/owr438O2B7rM7E-sMogoYeajgYWbmFOZHAR0sIyZiIiSVoRYaLBKa3IyrwK0m-zTObVOs6_2OVuv6Y6bIzD-oMfNanG5IgR1p3WdFUE_ze7Aq6ioR8uVMR83JEUGKs1ir-nXnj3TLzepr9CL3jdDaT_IEiOk3_nT01ypN9-SBfEW6LFPA_oxCnopIeNrLEBD4PgfdUELrs00RgR7mYKcoJQnHeDE4BCZFgWuqS_g1mZ3xAUGSKaJGcczeVUp-xLU1JpdfWz5ZlFMqsPsay2_uNwWMsUOWChN6aAbuut7M0Z2jpQ4SXYAfIWXXKWLwwrnYLvPnzXAq2jAECiYAh8mGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات معتقده "قیمت
#ملانت
به اندازه سایر کالاها گرون نشده" و احتمالا باید بیشتر از این دستشون رو توی جیب ملت فرو کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jQcx3spuCjvpy18gtd6z2IGU1N7RiIG2d3mkYyeysDNM0ilW8dw7VMeyDiQJ_yddGsC_AsQRB6HZzNeU7ehnOcggn3pmniK3jFBHCTUu9tSj9U4cEFPWmupNpUEsDaAEgYZOfoplZwq-9bZXeUE6VhSpbSGcPvffgjV7smeFeZyYPBEmOfXKanBgoqDPmbfkZx43Osxw15chUL2EWqR-Tzbr9-VN26k2etJAzJ5r-29_Z8XW_khG-ViRIr3R1Gd9DJ7c4_doqlRnfivjrWUfYKDW60ceYSKEIRVfTQOjpzqcuZ0o524VXIzcwuDufYdF6-ZlWA_X5WSlWNta6rfS-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واحد امنیت تیم پس‌کوچه در ماه‌های اخیر حرکت حمایتی قشنگی‌رو شروع کرده و اپ‌های VPN متن‌باز (که در ایران مورد استقبال قرار گرفتن) رو تحت ممیزی امنیتی قرار میده.
طبق آماری که دارم گزارش این ممیزی‌ها تا الان بصورت محرمانه برای ۷ فرد یا تیم توسعه فرستاده شده. اکثر این اپ‌ها درحال کار روی بروزرسانی‌های جدیدشون هستن و بیشتر از نصفشون آپدیت‌های کوچک و بزرگ داشتن.
این‌قضیه تقریبا برای توسعه‌دهنده‌ها و جامعه‌ی هدف برد-برد هست. اون فیلترشکن‌هایی هم که نسبت به مشکلات گزارش‌شده بی‌اعتنا باشن، به مرور از چرخه اطلاع‌رسانی و توصیه به افراد کنار گذاشته میشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CwMFK8OOFY0cBPpciK5dHYcGYdoDDNNBEVH81m-9D5FpppFtegBqfthvcIkL4BEeehGISlsc3RUQNnV3CxNJ_eTDaG4Dh2-ywoH5E7q1IKVH0vRrFWJICpoK2p2z3ZHKTiiFxyuow2ZmdMleqUXH3A3uPDND5zg2kL9NYwDodbR3zQhzHxbdrmybyzMzxfi_faUnKl8PExf6CvDdbIgK5dFvEEeAhLhL53GZnRd4Qw1u1J3pjKRIkB7-2qU1bzFWgv4W1LQvdDlsu9QISE3qSUzh-zsvhXnyACPlN0bnQz-oi12iHtKOmsyCWYIzwE3TBSOo9QxQiZrfw0QIbDhkSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QYrMg5GNw5-WIjSfN4--XCZI9DOpJz4icM1snRX_Xk20Z101pHlglhrvCoJg6JLlfr1znVz6aLuIzLSn_UBPja8JLITAMOhG8GmmHOGODDG95derojoQwiTNpdKAojPJflZ-rOrvnEyJgHXn-1zwn3YNlvgq1uA2JYU0XAnNvMkmXd3BW9nN8uQZ7g2E4vlA5PELGx5NUJLZ37ymDgUs6iL0_vhS6jH4DRl4TdyuMH5SsInRVclAIhUQwIwBrLXEb6MRgueoRVIP07GgSk2oUs2uJAcpkA-6TJ3TtEhbiI7i8DxlsB8gZwBbU4CaQJRn-7BucYZeylrBeliwJ3je6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pNWTNswNq9yUMxDdB72XsTACYKtJeM88G2HMFb-tuo8Ry0xRAR8eRAydrfqxT24w2Z4cJTUtU2o_6mQSKcM6szWR7d1YyTNH920v8Sm4-SRwS502Pqi4PIUqGb1GIidaHkpaLaXdVa3UdQkwIrsQXgN8secVsNeA5j47SymxDst0jcPRnF65SbO_FS9bboh676pjXSywyPdPejIbCv-ivS9-SAVKY46lhCDe4TJVXS8rbHHcBsX6TGheTn_zqAsTVw_l8l8FcouAvgEShgA2ZICwq_-mY5cnj5fuVMknc8qwFzcERBOrIyB0dQnE1tW5_IY5LR-aUCHtq4f9mGGP6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسپین یه ابزار رایگان و متن‌باز برای ویندوز، مک، لینوکس و رزبری‌پای هست، که دستگاهتون رو به یک هات‌اسپات مجهز به VPN تبدیل می‌کنه تا بتونین فیلترشکن رو با همه دستگاه‌های خونه به اشتراک بذارین.
کافیه لینک VLESS، VMess، Trojan، Shadowsocks یا Hysteria2 خودتون رو وارد کنید، تا ترافیک دستگاه‌هایی که به Wifi کاسپین وصل میشن، از تانل Xray رد بشه؛ بدون اینکه لازم باشه روی تک‌تک دستگاه‌ها VPN یا پروکسی نصب کنین. درضمن اگه تانل قطع بشه، کاسپین دسترسی اینترنت دستگاه‌های متصل رو قطع می‌کنه.
👉
github.com/Iman/caspian/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/agAStnagtYVIvs6sHb1gUlqh6qWXcuUfUA-UaYbmVebgImYg6PnS2sgQ4OMBanXotQqXRZsrgNcu1BushcLGbBqAAnk7INaKSuWfoa4EChhBbj2YSc2yLvrrRS5gXXPfPpJUL9m5NwdOpr0c5ypk63hPa-xFEguHWXlf7BaTKFTry30DqUiPx0UYFwUYHnj6Ofigt2CrdQMf7AcBvX2t_N20WWSV0iu31SHnO6wsMkcSm-YsRWKDrFaVNt4IFPOGMmiazdb1k4DMizKa3FMop3SmKg10hhYU4PtoDgPdMRnu5KxNHQkfdfIm3g-NrdmxafcnMNMv6w6pyLI1fADD_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Misga یک پیامک‌خوان متن‌باز و رایگان برای اندروید هست، که به شما اجازه میده پیامک‌های اسپم، تبلیغاتی و کلاهبرداری رو بصورت دلخواه فیلتر و مدیریت کنین.
این برنامه چند فیلتر داخلی برای اسپم‌ها و کلاهبرداری‌های رایج داره که می‌تونید نگهشون دارید، تغییر بدید یا کلاً حذف کنید و فیلترهای خودتون رو از صفر بسازید. با Filter Studio هم می‌تونید با Regex یا متن ساده، قانون‌های جدید تعریف کنین و حتی از هوش مصنوعی برای ساخت الگوی فیلتر کمک بگیرین.
👉
github.com/mirarr-app/Misga/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Htn6P4pDIZhqqfgFNeWe0P5TOyTzichoqi11gJ0g1ZH9n-pfC8qRJvi6gMLlH_95vWpoHxAKhYICro6fz_EC9fw7xyIcHy2ZLtDZ_EOuyAT1D-HM5wXmPdJWkMdZwOkcPh-5DnvFa3eRwVDzv-m0cx8xN0VH-tX-s33fBeJz9YxDe4ROE5pXr_egKqs31IGnJrIUsLK3scMKVsW4pdpY3i4D6pP6Ow9_4XIo1c9uRzkjvy6zvA5X6bX1XQezPiWG9zUIC5ymX9XvZDO8VT6vuOfzvtIPtTKyx0UohvTuyj0Wznc69_RppgTktTiGXbmh56RhyUTfSO9i0zc5qnuCtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند آسیب‌پذیری بحرانی در RouterOS پیدا شده که بعضی از اونها در قالب زنجیره‌ای به اسم MikroTrick در حملات واقعی هم مورد سوءاستفاده قرار گرفتن و می‌تونن در شرایطی دسترسی کامل به روتر بدن.
از طرفی Shadowserver در اسکن اخیرش بیش از ۱۲۲ هزار MikroTik با SSH باز روی اینترنت پیدا کرده که حدود ۳ هزار موردش مربوط به ایرانه. این عدد لزوماً به معنی آسیب‌پذیر بودن همه این دستگاه‌ها نیست، ولی نشون میده تعداد قابل‌توجهی از روترها مستقیماً از اینترنت قابل دسترسیه.
اگه MikroTik دارید، حتماً RouterOS رو هرچه سریع‌تر آپدیت کنید و بعدش لاگ‌ها، یوزرها، Scriptها و سرویس‌های ناشناس رو بررسی کنین. SSH و WebFig هم بهتره مستقیماً روی اینترنت باز نباشن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gqlPMMj9lBwkGFSIIrphtBj5N6-8viGYfdDxKy7jgO9MV_OtU7nz0DlD-n-mpGCNkCS6yWO_HG8JA7hoJzNJ5h-asxs_KlYCY1vjO0lVHULvyaiBtuUzgraAuEGQyBoiMB6oAGzcXL8t94FyLuOZN0JCkoUgatqtzaVzuXAoXqu92fkA1uRCBFntkYK0pMtLcwM8P34dyhF0qDMUWh3UQtON7-UiHLv68hrYzeIWTYd0HwV0ogjDj_pyHGBNVBkGT0JNcWeHAaI3iOu5ZklyJflkSuDafIXsT3h2qfqb1HdB5I4mUZzgF--UjJ0J1zGbSZm4sSbNdwG4AOrnCaAofg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه یکی از زیردامنه‌های gov[.]ir به افراد دارای مدرک فوق‌دیپلم یا پایین‌تر اجازه ورود نمیده و حتما باید لیسانس داشته باشین
😁
©
SePeHr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pSb35R424_uq1vULsCESC1KyjxqUB5T1KmzANxnm2fngiE2csgBmKgY00DtADdEcAkITyOh5QIJOOvmQjPktBxoSegF_Qj7RC0xOvI6BSQdNcxk8fVvEo4ZjCFu-XXrKyCh6-alHLirwPuJ5g_JV1OgymqQn_8P_D1gzzhBHGzlHiT-nB1Cjs7DzywZVZ7Hgjt214kZVGQ6qB1ivaMQuf0ZnQKMLenVQGY8k29v_vCeA0WXY3VvOwsWYX9qp2EeQNFmocpEAC1ZzXRwm7Qv0KEbwYZ4OYEWKzTsobLGCyhQLQutyn6W8avwUH4BNDCkaP80O2WndMKrNXZ6DrBbvcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن متن‌باز و رایگان دیفیکس اطلاع‌رسانی کرده که امکان تغییر زبان رو در گزینه Diagnostics & Experiments مربوط به بخش "ترجیحات" این‌برنامه قرار داده و حالا کاربرانی که به چینی، روسی و فارسی صحبت می‌کنن، می‌تونن DefyxVPN رو به زبان مورد نظرشون تغییر بدن.
البته این‌بروزرسانی بصورت آزمایشی از طریق گیت‌هاب در دسترسه و بزودی از طریق استور هم در دسترس قرار می‌گیره.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ایسنا خبر داده که
#قوه_عاقله
بخشنامه مربوط به "ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها" رو لغو کرد.
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حکومت در حال تهیه لیست IP کاربران و در قدم اول مشتریان دیتاسنترها است.
در این طرح شماره موبایل + شماره ملی + آیپی به هم وصل می‌شوند و بدون ثبت آیپی در سامانه شاهکار، دسترسی به اینترنت ممکن نیست!
نقض حریم خصوصی کاربران و حق ناشناس ماندن در اینترنت با قدرت در حال اجراست.
©
souzangar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W2r56buIkm9LS6_EKl_aOqhzbwX1RdhxofVwi8pNX1K-vreTIP2tEQX2s_56FYJj6U-Qi918PxZTzOe9pCHJkbfSPmVyKAF9Fjjk0TrpKbUFQYfymQUINi3xYQDn9AAFyWKubRVoPp7J8PBuc9Ske3t69S7gn400sw5FLTen-Y-ivIXpuLDAgXhrqAVL_Y7uUHMSu8h35J2lqagXRyzpdCJ0LQMbl0mMed4YQMTQur516vP0v6qp1rCTLpUMT-PHhW4UFGMhB5t_31Baa3S9cCiMt5YD0eXowofC6lXc6EeHSwHdJnWGeCIDqBaxds3nlPkXmPEqxnQUFm6IT2xMHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether با تمرکز روی بهبود سرعت و عملکرد منتشر شده و مهمترین تغییر، فیکس شدن مشکل سرعت MASQUE روی HTTP/2 هست، که حالا با اصلاح پنجره Flow Control، مسیر ارسال، فریم‌بندی پکت‌ها و MTU داخلی، باید در شرایط مختلف عملکرد بهتری داشته باشه.
از طرف دیگه، محدودیتی که بخاطر بافر دریافت TCP در Netstack روی همه ترنسپورت‌ها وجود داشت برطرف شده و این بافر حالا بزرگتره. ضمن اینکه می‌تونین مقدار بافر دریافت و ارسال رو بصورت دستی تنظیم کنین. البته برای WARP-in-WARP چندین دستور جدید هم اضافه شده، که اجازه میده اندپوینت‌های مختلف رو بصورت دستی مشخص کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZfpMKAGSGoUkcN9KSxGzIYOAY74f_65U81TsUafIUjGpDXXNZif225EphAnskjL0e0Xf3trgdepiwzNraYl6s1vQN0uuNQQ-u7fvqGSrQVarpz2_Tp1ugAIEJRt4klXdO6RPI4k66jsPBG7TsXgewmJ_pfYTFXfrONZem33GzWGgekoHbFeLNk9Q9ZdGyghSRzSKA4kYAJdFdyB7r_i4qUQfjLtS5rLQNx6TpsM50aGsVAT3cfbBC8bF8F1PxlR92-R_aokLBkcR7tSTMZoqM3knNUwhcZymbpkyYB9f-3ZcdtSJIA2z9yk9d83_EuyDWSwuIkBi_YFWR6NYOEnZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HuM7lUJpb7i1Toj9tPBZoRQwX-LBgHQ1ehzYStPzaraQh08tzHq1JSeCQzxHy8rrLcqXzZpDYWm0457H-3IeWGq49JbXadrs6xonxmh3ag5ULAqx8N_xgMQ7bMikar8R6n3vwn8d7HlfNwXc_uFPOfziupM29VdhpzEzNDGtqsT0ykiWqphDL2KskdtHC-gfsa_Mf2SSciQKdGyk9tqQlMHwsP5cWFRkBtby0zaBtyn2OaSWBQOJ52Drf0H5Jl69aZoucyPYtWDaO4jhSoICyaVdFATuyfIPZR-UPV4aPKly1ySM7qdHSvpSsZPyavLqwBxabNkzc5_CO8kVzqo7RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه باگ توی واتس‌اپ اندروید پیدا شده که روی بعضی گوشی‌ها می‌تونه اجازه بده بدون باز کردن قفل گوشی، به گالری و عکس‌های شخصی دسترسی پیدا بشه. این کار نه هک پیچیده‌ای میخواد و نه دانش فنی؛ فقط فرد باید گوشی رو در اختیار داشته باشه.
ماجرا از طریق تماس ویدیویی واتس‌اپ و گزینه‌های Meta AI انجام میشه و روی گوشی‌هایی مثل Pixel 6 Pro و Oppo K13 جواب داده، اما مثلاً Galaxy S25 Ultra جلوی این دسترسی رو می‌گیره.
©
notebookcheck
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">معاون سیاسی دفتر رئیس‌جمهور گفته "پزشکیان معتقده دوره محدودیت و فیلترینگ گذشته و اینترنت طبقاتی و فروش فیلترشکن به هیچ وجه قابل قبول نیست".
حالا حدس بزنین رئیس‌جمهور و رئیس شورای عالی فضای مجازی کیه؟
جواب درسته؛ مسعود پزشکیان
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EjsRWJTKlS6f-d7neHh1DUu1Z40dTcn2x0EkWZ-ae6aI-4Ood6H3ZZ-G3S5SAfvxIUuTIIordGG9iQZ8yvB5aqitwh1jzo6FisbW-EL6P0_h1_CDcDyi6mN4rgqQK87pptR-TRdpnl-hn53v93Y1JbPNLrov744lRmF2-mGxPu_4mlMqzv9tLW8vyRkwyThi9EyfaDHRwlFXMEbEy6gFugX9VGMlk-GJt0EP0jNffg33kaiYR7a7j9CR3x6WQCA1kxdtuGuXHFMAoS-wkf2Xk2dPYv-XGEXAvJUzrplrr-yLk6R2DPLlPhmTrQf02I3iklzr8mgLClFgdyktwQ-U8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Echoes یه ابزار متن‌باز و رایگان برای کارهای شبکه و توسعه هست، که چندین ابزار کاربردی رو یکجا در اختیارمون میذاره. از جمله امکاناتش میشه به پینگ، اسکن پورت، اتصال SSH به سرورها، بررسی اطلاعات DNS، WHOIS و IP/GeoIP، ارسال درخواست‌های HTTP و مدیریت DNSهای کلودفلر اشاره کرد. همچنین امکان بررسی وضعیت سرورها از نقاط مختلف دنیا و مانیتور کردن آپ‌تایم اونهارو داره.
👉
github.com/SinaXhpm/Echoes/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gOKMjm2Rbw-nvztfbnd5AmTkYcq8YWNr2iSZiX7ftxYvbJb_MmHUiq0QrImGLFUKG6krkuqFbBork14ApJ3x-wgMa3ChcKyeArs85WPa85B8qZqFVRUZ6r_O4EVoj6CxJwKBzppsDI8iHbT2nAdGn03Sd2nQ6ovjnJO47n1p2wOeqanxtcy6Yuz1sYUhHxGvgXLbCFaENR1JN7b09I9qNvphveGKohLueRIhuEULpOvAMNAeHz2BVVTDSiQXktI_EqFp5zr7n1Kf8P7znQdlyaw0lptsjvOtHOU5hNMHw7lP4h2eyO64Exqtx4LKWdlR6pFQZHsO8O8kkVU2hWfrmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بانک مهر ایران!
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k-CvvwdePuIYwadnYd4_js44r9xUaeS0K3ho31lFVPFj5uuEXtPTnlD0CbgoPA0ElVS7oTnnKLC8TzhJ1B948q_9Pb5SzpbN3PzgXXHKJgnqO1v3MGUe1bLbJ6kx6hFIlBw0kZoESFesm6NiPU22FFdBxije7_XOsKezvlS5S-xDA-A5tTepSwTXl8_FvmPmubqeZVgaIzjQo1FF9P3gn_-qYkaNYWH92bSSX3qbH7Lhgyx469j2LkNAgrMwkLZhDjyRm-o-NGC8YSaEINcRxyd9TSSBIRnhfMOnFuaIiaf9B1VwD5Qj8Gt2t0z2DkFtz4A50ywPZwxTBW0689OSgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که بانک مسکن داره، ستودنیه!
کاربران پیش از نصب نسخه اپلیکیشن همراه بانک لازم است، ابتدا هش نسخه دانلود شده از سایت بانک یا سایر منابع را با استفاده از الگوریتم استاندارد MD5 به یکی از طرق معمول محاسبه نموده و مقدار بدست آمده را با هش زیر، مقایسه و در صورت یکسان بودن مقادیر از اصالت و یکپارچگی نسخه دانلود شده، اطمینان حاصل و سپس نسبت به نصب نسخه اقدام نمایند.
©
alirazzazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LgKmu1xmR9S2KkKeqhwika87EaHa0TMk-eq0jAPZ0Jy8EE4maaWPP-g2xClJpoIG7uAstpik8SbyfRhI9seExxcGFg9mIsTVieiL-PhHJA9o0tr4ManjQcxM5Ztds40fPznlJyYOtp65ndkBo8w84SCzlXceQ9PR2AJVITQGUCf8wBIxHxP_3pr4_hXZGb-PKhMWqqQzROpIoiA0WvireRnCFbh1DNc9ybPsldcuO6MLvBbze0VwvkhuGbE31YHCksKecrw41Hh3Jf2XWTJQhcpciGzV-UIFjsEsm3K_o40f-CeUAsv-rAMcZB1VhDE7FkWVBFQafzCIcqyXECoahA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دستور پیگیری فوری
#ترافیک‌خواری
اپراتورها به کجا رسید؟
چندبرابر پول اینترنت میدیم، چندبرابر هزینه VPN میشه؛ تهشم آشغال‌نت تحویل می‌گیریم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mcsJgjMtB2NVDymdzBMPhQB77adAzDjJv0HNNVKlEpWNLm8koGtvUbrdO4OeGs0a4mcX61m-im0vjd8WzrRGQncYmim26aBwqsjtIdan4wcFMRWlmBBmlT-H0dcPK9ueqOu2qD9tIrU6xcH_LXN0WuJO5hDCUwcwFOif_uYWyYvmSAklwpmmH-8-8HhovXbrm_gCHbRRaFvVcTbm3OnOMmeqHBrrUiM-OBsCLKMo0gM1hA-obibU7VLVNEcDkHN917I-YSWdvI0zs9stWik3jT8jRtFhTHLvzPku5KqwTeW3HbzRReWjnk5oiDwqttr5BZ0NH1OLPfsLHM-CwUf-Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پانتگنوس یه ابزار متن‌باز و رایگانه که برای پژوهش و بررسی‌های امنیتی روی فایل‌های کانفیگ VPN و پروکسی ساخته شده. این ابزار بصورت خط فرمان و نسخه تحت وب در دسترسه و می‌تونه فایل‌های رمزنگاری‌شده با فرمت‌های اختصاصی بعضی کلاینت‌های اندروید و دسکتاپ رو بررسی و اطلاعات قابل خوندن مثل مشخصات سرور و تنظیمات کانفیگ رو از داخلشون استخراج کنه.
ابزار Pantegnos از فرمت‌های مختلفی مثل SlipNet، HTTP Injector، DarkTunnel، NapsternetV، NetMod و Happ Proxy پشتیبانی می‌کنه و برای تحلیل و بررسی کانفیگ‌هایی که توسط بعضی کانال‌ها و منابع مشکوک منتشر میشن، می‌تونه مفید باشه.
👉
github.com/FrontierTM/Pantegnos/releases
💡
frontiertm.github.io/Pantegnos
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NHzouvz5-bX6Aitny4biaRL7bKHGGV0cnW6SRFn3hd4-IyAsfi618vBoRPryQ90EFZ-YCF6t4CvE7c30O375OpQIMlsfLzg6dQf-fO184xHWzN627mGEyS51zHFuJ7A6qRRl8BdJQVRDyr4TftkJ9omHEVj8GZMrR-0Ipj7Fuxo-Rvq-EhbZJDIbhPlyeeoT5JKRtOanMVBty_qhNeoZj5KZSaA0ufOiQSALkU7gkbZaFXtkvgGZY1NZ9Q7l_aQxBJwPQRN1-vyEqqbTQTE_Wk2FuQU19lvPRUefBgebjNy4_1zcu6HVLwp5zVuyYqoaAGOITDPp07IV5Mz1gTIenA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپیس‌ایکس می‌خواد Starlink Mobile رو به یک رقیب جدی برای اپراتورهای موبایل تبدیل کنه. این شرکت در گزارش مالی جدیدش اعلام کرده قصد داره سرویس اتصال مستقیم گوشی به ماهواره رو گسترش بده و در کنار شبکه ماهواره‌ای، از زیرساخت‌های زمینی هم برای ارائه خدمات موبایل استفاده کنه.
©
satellitetoday
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hghWc98Qh2lu8MUzm22-ce6ZZVdDKEI2QlCW91XfzGrzpOAgMF51Vrf5GJL4-4MVUPhvhsPaETTMPJP9qN_mZ-agjU3NzGZKBzhXqrXy5k1KRzGl5-BrepeNXrMxFLAgKHXs4En-mliiv6QDh8FrkcbL9gK8D6Y0OtVEiLfok0PoYOJ4mouIzjbnhg7lIpDsJj27MVEuPifbXwCcmYbJcvBgSQsXJuqy1BaSupq49aGDCquyzkqjRHJ5W4p_SEjcRQb-8VBEoa_40LH3wtBTQQ7I5-ZhbO9iuVjL8HAQyyk8pyv2U3ReA5xGqXg4qrLC6r0FU8vQ0Rg83NXFOdbINg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fhIRP5kvh9nx40i07DbOXbG5GKFKinZRNIrOtC-SU43dre5KIl2IjdWYvXlPl56-sA_x5_Ym8AOHWYlR1QB1OZTEVuL2mUF-toWw3WnecA5QxIQq--NBT9rWFqRmizQnD8BEftwSc-vyOk-9tTmf-li1Ecz9vkgVe8cVMdgbuB4He0Zap47a3DA4Td5EnpBFj5hctToo5e0U0AOn3m93CFyd4igtEiCpRqn245rGxo_hB2AcU5ZU3ez11SLgCj_jBBrLllCnXljIE6TxVa5JX-Fp_xojok07jMmx8zKaYQ3ksxTSWCwJbTuJ0NNt0gLgkl2Uixi03e4x3xYdEM0Riw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام داره روی یک نوع WEB Proxy جدید کار می‌کنه که ترافیک معمول MTProxy رو از طریق یک WebView داخلی و روی HTTPS یا WebSocket منتقل می‌کنه. در سمت سرور هم این ارتباط‌ها دوباره از هم جدا میشن و هرکدوم به یک MTProxy معمولی وصل میشن.
این روش به سیستم‌عامل خاصی وابسته نیست و نکته جالب اینه که دامنه این WEB Proxy مثل یه سایت HTTPS معمولی دیده میشه و فقط درخواست‌هایی که اطلاعات مخصوص پروکسی رو داشته باشن، صفحه واسط (Bridge Page) مربوط به پروکسی رو دریافت می‌کنن.
👉
github.com/telegramdesktop/tproxy-server
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cZikloIGFTD24dol_VW8cJ3ThovdzWbYg-5BJ9dCOchEM95C9-eosWLALEblpEvHMXkAURNrO1Zau4xZsA0Y3MKpdNIBk4DIWqe2wdGeNYhqcN1bAOnFX4uyFJ1dWiG4rTE8Jz0I2GFbUZnaTvF0bsn4QN4goEawtHPEtk8LQOgwVlYiTt4debvcR4cpSjpn2fMAepUwvydN6EXIH1l14Z6ODSgx30HYt5N0sx9Tf4a-cUO9ccsINEk1Grd1qaiFOSBPWlO2dFaj4wYAvbP6V1R5NyEVcIXm7Cppo5XzjBv3WEgUm0PdD758R2ySy_ZoLmDsAD2JZO73UVpa8OpXHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدهای نسخه دسکتاپ از تلگرام نشانه‌هایی از یک پروکسی آزمایشی جدید با نام WEB مشاهده کردن، که از WebView و ارتباطات مبتنی بر HTTPS/WebSocket استفاده می‌کنه. این قابلیت هنوز در حال توسعه هست و مشخص نیست نسخه نهایی اون دقیقاً با چه معماری و مشخصاتی منتشر بشه.
©
telelakel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RoK5wLeH-cxUB-gd5sy5SCGPQny4kqHmmRpnKmhi-KoSrguEgFRZk8QFRoezof25UJC8C4IdBn1-rVJC8IVmYEyRpzTvPPOyu3EbbmV5cfjBN02nyE2UemZiWgTcc7IdgE0YXckbcs6xfD8PTODL8lXtBkdOV96SzUuHIqSzNDMEbBsE8WTCIv9zs5mcLMs4jdgUdqrRY9dicRdzw2dJLGq4DffAAPhduwcW4F2EX72Y3t-yJfDzHrepQm8ZWxM_WIAQTR4Xi9A0gU9lBytD3htK6fLo0q6MEYpZvkMl5A9X3BGIWuFhLTofnC94dJlE-cr4OQdBCw1QxLfB-OCr5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا با همکاری سازمان ETSI یک استاندارد امنیتی جدید برای VPNها با نام EN 304 620 معرفی کرده که در چارچوب قانون Cyber Resilience Act قرار می‌گیره. بر اساس این استاندارد، VPNهایی که در بازار اروپا عرضه میشن باید حداقل استانداردهای مشخصی در زمینه رمزنگاری، احراز هویت، مدیریت کلیدها و مقابله با آسیب‌پذیری‌های امنیتی داشته باشن و این موارد هم قابل بررسی و ممیزی باشه.
البته این مقررات به معنی ممنوعیت VPN یا محدود کردن دسترسی به اونها نیست؛ هدفشون اینه که VPNهای ناامن و بی‌کیفیت از بازار کنار گذاشته بشن و سطح امنیت سرویس‌های موجود بالاتر بره.
شرکت‌هایی مثل NordVPN، Surfshark، Cisco، Google، Palo Alto Networks و Airbus هم در تدوین این الزامات مشارکت داشتن. از طرف دیگه، ارائه‌دهندگان VPN باید آسیب‌پذیری‌های جدی و فعال رو سریع‌تر گزارش و برطرف کنن.
در نهایت، اتحادیه اروپا میخواد حداقل سطح امنیت محصولات دیجیتال، از جمله VPNهارو در بازار خودش بالا ببره و اجرای کامل الزامات این قانون تا پایان ۲۰۲۷ دنبال میشه.
©
techradar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r78fChHmGdjXxR-OZqyvlx6lRPa_7eWQ5EVdbWYnQ0fh0OdDSp04QnnAHCi3leRy_qv_3n-ENYTocXo4Dnc8ucb_lyHNE2kk5kjkzC7RjyQTD77R9Ej0mQrxeOqBtJf5a2c5s6yN9OvClts4wLlR7VPo46lzm1veSvVDiu6Dg26NrkWg334RttR1tS_-9IIG1HSFTVLE9fF4At5vZV4J4LYwv2_RP2uoXjAHWVxo2WqIk3YynmhSXGzb50VRi-l_KQv2a2l-pt3wqivAArpWXGM6VM-_FFdanixT4DFpqXYeR9jczzPnjUaIEWSu74XG07vjIqnDeyFJ0HbFN3ZT6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم پس‌کوچه با بررسی نسخه اندروید فیلترشکن Line VPN که تا الان بیش از یک میلیون بار از گوگل‌پلی دانلود شده، ۶ ایراد امنیتی مهم در بخش‌های مختلف اون پیدا کرده، که در سطح بالا ارزیابی میشن.
مشکل اصلی و مشترک در تمام این موارد یک چیزه، که اپلیکیشن در چند نقطه حساس نمی‌تونه با اطمینان تشخیص بده آیا اطلاعاتی که دریافت می‌کنه واقعاً از سرور مورد اعتماد اومدن یا نه، و آیا هویتی که برای اتصال استفاده می‌کنه فقط در اختیار یک کاربر مجاز قرار داره یا خیر.
پس‌کوچه این وی‌پی‌ان رو بیش از اینکه سپر باشه، به ریسک امنیتی تشبیه کرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eOIdHc9XuO1GBuTpicHI7PpPRm0DKfwMc-1vQaeX3BAnLHhBcohdzeky_YstS5WRbWJQwC8vFyY4ux56ScSq4jfJUPLo5cAD5J20eLCK0kgZY9nUsyrkQiqFQoX0NNSQYh09lBq0pkdK8KyZfw_HS-Z2BXJNWik1FvmG9RZQYm-S8duthWEQgATQQsUIGYNl8RrkGBMm1LD5qr4Q_XazS8ex7NrIPnh76MddciCyzDSRZDxNGqv1RjnwiJNof2UB1JeIQkrXeE7LDh0DybM7jcXNtmTsKKrhPT5dedlNUiXeOU0Dz7HkZfwB8Ts0WQqelXlunsWK9rtivZdTSqcD3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ایرانسل و همراه‌اول فکر کنم یه بسته رو به چند نفر میفروشن.
©
ali__m___i
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ظاهراً پلتفرم شنوتو، میزبان هزاران پادکست ایرانی، توسط کارگروه تعیین مصادیق مجرمانه فیلتر شده است. طبق قانون شش نفر از اعضای این کارگروه ۱۲ نفره از طرف دولت هستند. دولتی که در «ستادش» اعلام کرد دیگر هیچ پلتفرمی بدون تأیید رئیس‌جمهور فیلتر نمی‌شود!
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F-m_ePcNShgCXnY9FnBNNzWSjP2gOlyynS1B4ybhyBHxTeMTKa7YP7GAtGOXdv48_hNg--iE9JyRtJxAuvqAiexq2GDHjIlyZFf2ysM3fy_Xl_Dk37zy6PuaYn8JmytSZ_IkAx_VcO6ZVgBuFPajcRc4FRAcAu1HvxfTv4ODLR3GyHAbiZw5eUKU6vhjgS-0WNRkvmXfjtvvGh85Rqd25eVb7wyaCqjL7_oDx_TaTKEo1HdXYZYt5HellWeO5_KkdUm_aA10fBb0r840GUrf_5PtGKbL3NSvRWsdYicgF_7VIhd9kMC7a9TCNnxCGIvfL-1cDJMTMq5r1rvK0yB-0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران شرکت امنیتی Socket شبکه‌ای متشکل از ۷۳۷ افزونه رایگان VPN رو در فروشگاه Chrome شناسایی کردن که عمدتاً کاربران روسی‌زبان رو هدف قرار می‌دادن. این افزونه‌ها در مجموع ۷۵٬۴۸۶ بار نصب شده بودن و ۲۷۴ مورد از اونها با جعل نام و هویت ۶۶ سرویس معتبر از جمله Proton VPN، NordVPN، Surfshark، ExpressVPN، CyberGhost، Windscribe، TunnelBear و Cloudflare
1.1.1.1
منتشر شده بودن.
بخش عمده افزونه‌ها پس از اتصال، تمام ترافیک مرورگر رو از طریق سرورهای SOCKS5 تحت کنترل یک زیرساخت ناشناس عبور می‌دادن. در نتیجه، گردانندگان این زیرساخت می‌تونستن مقصدهای بازدیدشده، IP کاربر، اطلاعات SNI و داده‌هایی رو که بدون رمزنگاری HTTPS ارسال میشن مشاهده کنن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uk1oAOaUB3UAlhhm-QSeTKWghjXbmbjtzINdGXnSyGwMtM-RufMFA5Hy6O97YJkKftOHQumBzoAecSmf81KmtKs6rjjunoETNu5jl7dIvp_NIW7AEJC9JIIPhWLWwa1W8BG71A8MgL8Tl0ztBmuh94B1o2XDgA2wm_6X0ZR3Vyt7H87m-SWFB6OJoo5FP8lKnd7TQGu1w0fATkdUgXLNEIlDAkYueutNRouLi_Jvb2xMk2e32H_QKf8YoILsKeXRCcyqJ5_vHvSoaW4ernT5V6YrNCwyntcYhtCFWHu_WsBIbZuiaX3GOlevK6n2o9YLf43AzXv1gmEcNRyOf-M1gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteVPN یک VPN متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که بر پایه‌ی هسته‌ی Mihomo ساخته شده.
این برنامه با پشتیبانی از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard، امکان اتصال از طریق سابسکریپشن یا اضافه‌کردن دستی سرورها رو فراهم می‌کنه.
👉
github.com/WhiteDNS/WhiteVPN/releases
💡
github.com/WhiteDNS/WhiteVPN-Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">قوه عاقله برای بار نمیدونم چندم دامنه
workers.dev
مربوط به کلودفلر رو فیلتر کرد و مشخص نیست بازم از فیلتر دربیاد یا نه. بهرحال "در سر عقل باید"، اما 404 مشاهده شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اینترنت همین الانش هم طبقاتیه، چون هزینه بسته‌های اینترنت رو اونقدر بالا بردن که دیگه خریدشون در حد توانمون نیست!
©
Kiyas
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اینترنت ایران باید به لیست شکنجه‌های تاریخ بشر اضافه بشه ...
©
thepanue
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=bxpctOWsIoeICr96Zl-Uge4vRcv_o9U3Noo8sI12vHSsF2j606M_pZHz8zHZNkhY6G-fBRDAKafJ7cue63175EK1wXYk2X12qZibxyP1Ac570lIEGeiDSvuQe3VYj8H_F82p9m9r-F5TMtYOXCj_CIB8Uq7OwAJY_VJb81GB3Y8XyxUgD2ZVDgjzHX1ENLiDnUG6Iv3dsys3cm_pL705JIVihbxeL19hFtjkfiNomdj1SopWsrS29HZ8S9uDPRJa54WlvugXO7XhEMOMGo0bV59YEu2nMYEcWLGQGQuuRpIq6efh-uQQmtathlKqk2IZEdFibv2akjmlisJ6Kvm5eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=bxpctOWsIoeICr96Zl-Uge4vRcv_o9U3Noo8sI12vHSsF2j606M_pZHz8zHZNkhY6G-fBRDAKafJ7cue63175EK1wXYk2X12qZibxyP1Ac570lIEGeiDSvuQe3VYj8H_F82p9m9r-F5TMtYOXCj_CIB8Uq7OwAJY_VJb81GB3Y8XyxUgD2ZVDgjzHX1ENLiDnUG6Iv3dsys3cm_pL705JIVihbxeL19hFtjkfiNomdj1SopWsrS29HZ8S9uDPRJa54WlvugXO7XhEMOMGo0bV59YEu2nMYEcWLGQGQuuRpIq6efh-uQQmtathlKqk2IZEdFibv2akjmlisJ6Kvm5eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ممد ساخته. یکی از محمدها، که نمیشناسمش و قرار نیست بدونیم کدوم یکیشونه؛ ولی باهاش کلی خندیدم
😂
©
Mohammad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HPygU7Ky8zrQGWEx-RG0EmnCdvFkFSlusfPdfjBiK048_LKsjweNcTjI2f8YwxzcxfLuL5hgmMzsbJUL3pyphUcS9lUZStqDle5uxP5g9By2GvuH3CtiHpkXklClzU_IDqBe4tgPcwIkZyM2eBF_dq-tX5ilZkv3shJXfZfAGTs17qVlWoA_3vpjtnHTft-sLTFApL3kwWsueV2zbFGw8YpaEWQeuiUJj1ZyjmmbdjB2ygyr567A2fZSMRwh2Lyw3tGz5f7k9Srb41z3Ef21E-bgH-CSeFX5bhpiGURokvZmLoGPNmDqiZ1HlzydmvZ8t42aBKKz7JVil-_43sLL5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکثر آنتی‌ویروس‌ها (از درپیت تا لاکچری) سایت بانک ملی رو فلگ کردن، چون سرتیفیکیتش منقضی شده!
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kTuXfcOdN65rDWNGcMrTQXUH4vNvbCUAf8_XGG9uRE4bkir9C3J5OvSwK-P2YjQCA0MwGg6ExN9_fXAyRcTDrcSGVsXoy4zCo8X4axOdkl5A8mf2zCnAcmzKDir9hnkV3k3RokLS2JWgoFvPiZ0kaeVaWWjELR9AfpXjA5fJHhIeVRaNPYybh6CJWot9LuxEqttLMZZnwhxwc7VAuVpxbadRhr5nIyyKAduk9sz6AGBCr44spofqZ8spe4LyFx6NGwiainwRKHUMlbkVqbytQVmlJf04tMrV58KkJxYSFdhQBAUezbWX66p2Za0SBZfcTKhR70wNPRtf8fGfz0pfhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات مخابرات گفته دستورالعمل جدیدی برای محدودیت VPN روی اینترنت ثابت ابلاغ نشده و ممکنه از مشکلات فنی شبکه یا نحوه عملکرد خود فیلترشکن‌ها باشه!
🤡
در رابطه با اینکه اختلال‌های اینترنت وضعیتی فاجعه‌بار دارن که جای صحبت نیست؛ فقط اگر بدون دستورالعمل دارن گند میزنن، یعنی دیگه خیلی کاسه داغ‌تر از آشن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hX_J59k7mIBPJlhxW_mnW4JxrPFQqSc85aucSeIVJ9b1E1xe-QoTKP0ficQehE2BwbVvZY5gnE2iaU0ZPKcdHW5Jg6ICtbP3dihkxEO-kL4aNH0R-UiYHSHLgtl1RwlxexLaD9R7CfRTzLWlRB4NO5HJgckfPTqoSS5guaUsi4FY0r3971qNqZL2QqLKBBCUexbp5cIkC3IQl1iG0ubMQIjf811SBx0n1tv7AXHjoluHJFs2IIoacRueODjAe09eA8EY2z9tt6Ju-6rYN3aCCf28_TtcO28dcLRB-XyQBbOF3c0mz5qzFN_pu_akEAl673dt4KyHr6TKKBAkRWrQ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nkxch-T82tclYyPLc1js1n6oEl1vpO4_t6SbD5Q1tCvSjh8yhZkzevZntZF9Iy47F0Rjx4U7HWnrixHcYT-nl2V6nVpEAuScL6mLIEmh_DN--e9tn2LZg2i5VwTEKyeuSeqkUkuzgpgIbYCMxXeRym9kmbm3wMBj2wzPBO_xTpYYU9lu6Zo-vya7CSJLJmvdg2DK26KOpqAgzKVMKzLcbTuOIAX2YHEAPDWNxo8_Ppl4NZ_AJ2uRSzfSS-GO_aLy3VqjHhjIgGuM82EM17K1AHkq_fVjuTuZUFG5HdDkkQ6eJBTy7vFqNq0ajiqZAyV_Nbqpzl6F39N0jfgpEMY7-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B9h2PUUA4Bl_6cDKyD10PpdmjFoiu-1JywDUse-r0pZyRsccjUPnc2xHV4EUCw2Uar4sPW6f6oN8x5UH57jTqVsYBnCSCNQorhgwBYP8lFJD_T8A5v8sbaZUaHrRkgAGdmgi7WEcUiVRHyq6XdeTVQkEz1gTOKapXP6iV7ynLfxwzozTAcN8NYmEz1JSMQE7c270VCyeQr3OBak_QQkeab5X4SwdcNqDHFLLTyc8tB505z3CjIULu-HYc4QJ4rhfq4P-y4oAQtFBkqd5417q4_9uCu73AuzBcSsv-ndJ8Gg6eDxcWUltRYBDQ0yuXsl90ykS03XfMjnB_unM4xqEng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NmHaEvz4IhN7E0yTRWEeu90augcFXU3FZubPVW1wKwGY69eW33g7UtbgD-MtNLVR1NVPW84Vx6IXLdC5G-3Rs5tWd5o50dp0khI8WU3FxlDDXQC-S7wRpSvd434_IF8eGQCv71q6nEhwhqy8mNVWGahffZfQaZCAMDtYdKcDj4UWQWo1c5LF7lBNCQj9ba56U7KKukxOmbErrnTRTDdtE0ZCOXO1fHgDUYca16872KQS414SmqZZx_gK0gxmQs7uHcRA_jhf3dhylwXK86f4_m12VRXLUuMaGKzWMJTtIXE7wfEKWW-TqRLYNrG7lQLq7Kmy_vfC4Ow02F-Y-KRINg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه عده‌ای از عناصر فرصت‌طلب سودجو عنوان می‌کنن اینترنت قوی و زیبای ما گران شده است. برای شفاف سازی میگم بسته‌ای که شش ماه پیش خریدم 1,348,000 تومان، الان شده 3,870,000 تومان. قیمت فقط ۳ برابر شده، گران نشده.
بنده هم با ارائه سند میگم اینترنت گران نشده، فقط ۳ برابر شده!
©
mrweb24
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gr__HYE9JHnqG24BttxUvUORuC2-j4MVSp4uz9UhxgYVM5KPSs0Q1rp1lwgKprz0POumngT01w5zqsSqEBC6_ABdRjZ_CHnr0CFDNkGSxAIFQCas2trvZ82WkspqjAY6kLWQVWd5GdfOlL8YmYNp_jr65IBe5rTb2xy0ThhaKHQffqo87MHOLAPwdMffn9bNXhc4a4440t704CXVPG96vZSjRY770ZsVaxhzBHjuHhLnjwgWjr3O__PQkB7J_7J8q0oQBv8wfUNpLF46iJkf5YQzjqX6i-AfyeUbyWh7R1mxkqSWKGloqHr4ffP2LM4gnLlQGyU0eYECf0tzsOARfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Je-BDKWDuxnp6A0QzDVU54kNhbhduyiXbufvRmdO0peiyVIyGsRZyArzKeQip4gfseCqPCyTKQwpGr1i7t1y7xwS5udGkMx6CwKdw_csvTS5yFr_Ho7WiKlFZwvvexY8CsCbIKHk7foaHdHU93eO34ttcJs6OlnOLZbJxnc-bo5kd2uIL78dsZzIqco8OjI88kxl3i0XQhVSco38sZt690IiUzJQYNNXQmnj5plvMkRivgPDkK4v14TrcU8hYGoG_ZAxmlHPcJJFSP-xu0HL_Mbcmp1x7fzNo8-JcoNox2CQ-z3UmT7s8SMGeAoZvrQ1ILH8Os7m5TGr4GTTZ2W1Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">چند پورت مهم مانند پورت ٢٢ از سمت زیرساخت بر روی آیپی‌های ایران به سمت شبکه بین‌الملل محدود شده است.
همچنین شواهد و بررسی‌ها نشان می‌دهند که ارتباطات زیرساخت برای ایجاد یک قطعی گسترده در حالت آماده‌باش می‌باشد.
©
manageit
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qw517UWqy0PjPc6X1gv2TAJbeq-_Vznm3-efN2QBRcVxavVJn2lrY_ESX91drWMEOnE1vBNpyfDI248VvrxtwNYBKuLcxzBDFYpnEB5eSqpH76F5KoZhzUa2Ll0SGTedF2jSfGPANwJMLBwKytJade35A1aG7c0IwisT4CSwJhw5Dp1Zt8BaA_vjNMqNoonaSzlVMvLxzra__XIZHEp9HNiT7IIzmZeb1RKgo2APScKAVQDe1DqLRdcwNSwHXCkS1yhatqo6oe--PEYxACW_nH4JznhqZ2_kiOqKwvDwGUQfgztMwL-OWGtyW_v6jU_qZtOhxM1N0IgjtwDlr9O-3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">چرا کسی از این موضوع که "سیمکارتایی که استفاده نمیکنی رو واگذار میکنن، در حالی که طرف با اون خط اکانت تلگرام داره و چتاشو شخص جدید میتونه بخونه" چیزی نمیگه؟
©
shara77miaa
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GfgTgjK-EJYqrklGJ3S19vzvsxIPH0MoIPCwsoMf3xwJjlAQsg4bIQAhnhg2iYHe6_dKVHasOxyH_NEf4MYys0w_SNblsC1QWfzhhIyA-Kjpj5JrIaurlh02fsiS0RuCCJGFJ8N7G0YTkFQx7X_7CGmscEiSoNxIjgnn19E1TRzmBPXSLHNIC_n_le7LSTOkcjpP9ZpTNdJOdVVcOm2FIQFGw2uQGHxCS1Saxlkm0UpfC1-N4YJE4xImQIsfup4WO-sHu8DdWru7XsxHOwMupODCVZsx22FTVmIUBOItHJWDF5-Mow0lgBmA-Gstvj8T5pfN_i7yb7ztotWVDnEnkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HYJKALgDw7ynUB4dvjnOod1niwPE48necH027A7CGucXS0z4-yBM_CY5trRrDjl-tiQsT6wETQB9ZSV7DgAK2CpHd9uF0Sy6MEQLs6eVOFnFj-CXL7VUkSHAjmieX4cP6BO7WlzH8KVG6enM27nSXZ0OXd_cN5jON-Hq_sMsQZkh6r3WDTOo88i2vlXD8wlygIZWIkvVVXfDnbimwwE3yuwLDZT-nPcKQWQ1AM4Nl7xTFB7SCTOL3FawiPknJ467CY9vRQ3umZYXQAMD6u8rbC4H8mjNuTdf0LygMQdMbA6kIq8a94b6HWXriETsiYm_m8mqeOPMCf4Vlp5vvVmEEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی و با چه مجوزی تصمیم گرفت ضریب بسته‌های اینترنت بین‌الملل رو بدون اطلاع‌رسانی تغییر بده؟
قبلاً ۵ گیگ اینترنت میخریدیم = ۱۰ گیگ داخلی بود! و فقط پول ۵ گیگ رو میدادیم. الان پول ۱۰ گیگ رو می‌گیرن!!! فقط نصف اینترنت بین‌الملل میتونی استفاده کنی! بی سر و صدا دزدی میکنن با عوض کردن مدل درامدی!
غرامت قطعی‌های ماه‌ها اینترنت هم هنوز پرداخت نشده. این دزدی سازمان‌یافته‌ست که با حمایت وزارت پست و تلگراف اجرایی شده !
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qVSs_jC8BgDCrq7HzYKzFYC4W8WXoIomPrhn5-0LlKhkymvqCZSqmvSCfHM-0Bbgflzsf-_Zi-ypmygKB-8a7hgdtJSPn_X6sKm0l5MqvUc0DBxDw7YYGHp8xgUnk-Ft3bSiXiygugmI064yARnRu7lFUq-vqKtFRy0L8y3OHB1j-1Qe5gppa5tlZnqbZcdaW5jZUlvc7SCLKorg4XRCT6eBVpls-bjzafN3S_n7hm35lsGm52TpNZea5P_Kgvfb_HvzkF6cFY12dt3EQdAv5Gei2y3MDjYIPhJOVOFIPJaKNBBwAXdO3CArHBpIXwi2ZaRQ5f_xZKN5FzUGixkPrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aerial یه رادیوی متن‌باز و رایگان برای اندروید هست، که باهاش می‌تونین بدون نیاز به ثبت‌نام یا استفاده از فیلترشکن، به ایستگاه‌های رادیویی مختلف گوش کنین.
👉
github.com/shapeshed/aerial/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JGsVGXpsvUEYMxf9AOpHRZoe2DLIhnYSjj61s-IizTfPh_pJ91iZFiuHS5K-CbL4awQEPhUtAtrrod5X2evVWnJLF38NWL_iK48Y-OCW8gN0MiHEb9Oqrbl2Qfy7g9td91zpJE5pAUmMyQw75NUblYaOwyy3ozKfHV8zGqHcHwg90ep3Zi0VgdGXMbXy9vfo5NbJPlr_y3LU0hnx5XD_2JYPaKF2i9dywvLuFTLO3wJjxZvOm81ksjqZ0eyCco6kifD0MwyEDoX_UUKmPasDPLrIbKzKHYMKoeTzL9ulNjD0DfKhTsFc8b8Fov1dFWzkNZu8SbhEE1AiLDBuPaq4ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cwT_Liz5Q9tjBi9Ckmfg2nLGYGtXavafYBzBHyVTaSOmWNaB8SDS9ZneyuRlLdkIVHW3PuZGqU8Qwf0BO0sAb4DrDKaZEBJZWTRYGg_uOSYmaJDu3icOu6Y3aM4XoQvk8F_piBU2b3MhjQwG1crWh-6s4uzjcxjKbatCynKwi7UCHJSA9N2PHWirSt4w7ieQ03G_p-PyoeVkBgUOdiUQpjvHs_CYVwKRQkBWWpwsSYUxNMGr6nAhscDC6tMh7xhRFIihe2fHt8DIln284K8NU0VGWMk-t56u4iS4dzPz_p-lQnQgk4tgN-j8pAyl15Ur17EjlinF4NYjdnR8yO3g3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از راه‌ها مخفی‌کردن صورت مسئله، اینه که چندهفته پیام خطا نمایش بدی!
©
AmirMahdi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NJA1uIL_Fvmgy7FLF-ZRBjBMRELrVZzQ1eWeBu3eKdnthKvLliE1QM8Z621-PEFLVNutvzGHXHRCd9_bn-zXz3IyjKZLQzgKvMirhitkeNfVrvb5535VvPdDWmQbEgN0Kjyrcb9WFxUpmHbUx_7LFvQHs_UdcwejE5LjO9cNI3uV2VMshHCAYE9Z3PQmn9jQRQIQp_jXd-SgUmPVDSEpVLk6SyZhU5K3bZvN4AELZKTSjkDsu5YAALxYkY3A_sMYs10hF0a6McW3xkIsXHkuK1d8zg2CYZDFviL7PRSxmYiGZNikdtLe6P76RNSv26Cx_OJyuVs09jKd28t3UDvjqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yct3njKn60MYF-Np2jtq9u6LDO7dlZuCTvhnFt5Y0K7Qjf5c9l3L-nho2LbIeLciRPVwEOo0zm8JVFP4grsN4REEhjUuflRWwtRM9hukthJd3v56hD3wlG2P4Tiqy3PFgoIfKq7WLli2mpTGcV4ysPtep1RW2DJ8Hm_BGZJWtkyBBHpu2R6aM87lJU45yJpdt99YxrFaEFBJuiGvrHd2HXxbR3-oUUJaeUzfoi6TVlvsw8zRHdU7wIBdwY2ednz1Y5B1hX7RXO04IwMe0tkxfpXZCYhge6CCilNPDhW_6GId_0OW2oUAyvRDfS-xoDgQY0fqw0Lk2CrOiXWBqLAgVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ضریب اعمالی به اینصورته که شما اگر ۲۷۰ گیگ اینترنت داخلی دانلود کنید، ۱۰۰ گیگ حجم از بسته بین المللتون کم میشه.
این کار کلاهبرداری خواهد بود، اگر حداقل یکی از حالت‌های زیر اتفاق بیفته:
۱. اپراتور موقع فروش به شما حجم ترافیک داخلی رو نمایش بده.
۲. این اتفاق برعکس بیفته، یعنی شما وقتی ۳۷ گیگ دانلود کنی، از حجمت ۱۰۰ گیگ کم بشه.
ولی هیچ کدوم از این دوتا اتفاق نمی‌افته.
متن دقیقش اینه: هر گیگابایت ترافیک بین‌الملل معادل ۲.۷ گیگابایت، ترافیک داخلی است. به عنوان مثال سرویس دارای ۱۰۰ گیگابایت ترافیک بین‌الملل، معادل ۲۷۰ گیگابایت ترافیک داخلی است.
مساله اصلی اینه که
این تصویر
و وایرال شدن این قضیه، شاید بیشتر بخاطر ویو گرفتن بوده نه انتقاد یا اعتراض. ما میدونیم که انتقاد اصلی، انتقاد به گران‌تر شدن و بی کیفیت‌تر شدن اینترنته؛ و همیشه هم این اعتراض رو داریم و در موردش بحث کردیم. اما انتشار این خبر که مبنای درستی نداره، صرفا قدرت تکذیب اپراتورها رو در مورد مسائل مهمتر بیشتر میکنه.
باید اضافه کنم این ضریب ۲.۷ اینترنت داخل،
در آینده میتونه بهونه‌ای باشه تا بی‌کیفیتی سرویس رو توجیه کنن! ا
ما فعلا در قالب یک هدیه، کادو پیچ شده و به ما تحویل دادنش.
©
Taha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی ۱ به ۲.۷ هست؛ یعنی اگر ۱ گیگ خریداری کرده باشین می‌تونین برای استفاده از سایت‌های داخلی به میزان ۲.۷ گیگ مصرف کنین.
اما چیزی که کاربران میگن دقیقا برعکس همینه و جالبه!
چند نمونه از پیام‌ها:
- اپراتورها درحال شعبده‌بازی هستن
- ایرانسل و همراه اول ضریب دارن، اما هنوز از رایتل ندیدم
- من مصرفم در یکماه طبق آماری که خودم دارم حدود ۵۰ گیگ بود، ولی ۲۵۰ گیگ رفت توی پاچه‌م
- بسته‌های اینترنت با سرعت چند برابر تموم میشن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پیام‌های زیادی در این چندروز داشتم که میگفتن اپراتورها ضریب جدیدی لحاظ کردن و مصرف اینترنت بین‌الملل رو چندبرابر محاسبه می‌کنن.
یکی از پیام‌ها اینه که "امروز با پشتیبانی آسیاتک تماس گرفته بودم بابت اینکه یک فایل ۵۰ گیگابایتی دانلود کردم و اونا بیشتر از ۱۰۰ گیگ از حجم اصلی من کم کردن. پشتیبانی بهم گفت که اینترنت بین‌الملل با ضریب حساب میشه و همه اپراتورها این مصوبه براشون اومده".
توی خبرهای رسمی چنین چیزی ندیدم، ولی اگر اطلاعات دقیقی دارین می‌تونین برام بفرستین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tsWAXE612ivDpXjxTskHWy0U6CgkeACOZc6QJ4GRnFVemWNtFKYZDKl9dcu2AqjhRZbb5O-b7cizRGRImRhmwcbMSDiecPoWcvBqGvVojpeQLPbncWLXYZ_d3O_lry8k1TF2Sa_BAlmxyeypjJOayKpkcZpiQA-zXVpeYU3mbP53JzSFoCkEM1T9I1-W2oafCzIW1no8ChXKemBFQjwUlKnJnN2tGk2XGCWqCP66BqQf74h6dTrTqiDzTzCzcc0NqnhH6NLuje386gB6VbPu7Dt6jk8b1xHbqs9sZP66kL_J4MkwBrpAwuUduxqmCjNfKfwI9tD977PfAGCbKVV8sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ‌کس این چنین به ستیز با مردم برنخاسته بود ...
©
sadroddinfallah
بروزرسانی: تعدادی از کاربران میگن متن داخل تصویر گمراه‌کننده هست، که درست هم میگن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gaz_qG1BOZey3Ugb_dGLB4sT4g2nMF0BW8nr7_tIgCysncXsrXcgjjrIznWq28ExdBFLBvS_yKH2oxMF1J_MGiV4gQAOEb_pJNQZo_WzgB7rwj7hwXPNqUzrCJR9M5fE1gLnfQvbFntjeISW8hGdxcQandgTbzc3XI0iSvPQmeyOHGj42n_kGWB5_w3YplZB_Wik2ENVvWEo5pnRSvAW15qExSTS3vvmCqWhbENGfTrcisVN_LNAvlGuBsTgTNmy9drpbpvwxL042_kBjiQJO0O_OjKYRn-M6Cch-DQqnFUnamJ4ld2OLKitXrJe6MxxCM7o3Yjml2YLqhVzSOwhYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هسته Aether یه آپدیت جدید داده، که امکان پشتیبانی از Zero Trust و تعریف قوانین مسیریابی، مهمترین تغییراتش هستن.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NwTDWqMhlM_9nMm9_O34iYWvkPz957ITN1QAw21Jg4K7aIgSkHOfBoMfO6nzUmHiVwJlORMRPY8CZTekkUG5TU3tftiUHXZn2ozu1o8siw4vmMOUTwGFc_hbTUAz6aruo_QQVkE4ZVea73r5cX1CGD611AHsFFhwn0isFwvXwfHFO6VbQRTagr8Hhb-nUQqKjhkq8oyplCGLqvsBBhjGE4p-8y9WRFohiPCl35ptNO_Ncp95SChxQ00k6UWRS0PWGVrSZhrzPvc9zZ5cFJ5CqMWZD5ZbTWMFcrHAaIx1Nd72H_TgZqIC1KQnLlMfK9hDri7A7uvLPNJ3BtRnbLJApw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از فیلترشکن بگذر برای اندروید در گوگل‌پلی قرار گرفت. همینطور می‌تونین نسخه ویندوز اون رو از صفحه گیت‌هاب و نسخه آیفون رو از تست‌فلایت دریافت کنین.
در این‌آپدیت هسته ایکس‌ری به جدیدترین نسخه بروزرسانی شده و روی افزایش پایداری اتصال، بهبود عملکرد کلی و افزایش سرعت برنامه کار کردن.
👉
play.google.com/store/apps/details?id=cloud.begzar.begzar
💡
github.com/Begzar/BegzarApp/releases
💡
testflight.apple.com/join/cRSCr51a
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته توسعه زیرساخت‌های ارتباطی کشور حتی در شرایط جنگ تحمیلی سوم متوقف نشد!
انگار نه انگار ۸۸ روز اینترنت کل کشور رو بصورت سراسری قطع کرده بودن و بعد از مثلا وصل شدنش، اختلال‌ها در ملانت ادامه داره ...
برای راهپیمایی اربعین هم در ۱۰۰ نقطه اینترنت رایگان درنظر گرفتن و پولشم که با افزایش ضریب و هزینه‌ها، از جیب مردم پرداخت میشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nXwy9qqclb769THZDDbQs74QJNXgbPLoNLYUEfBICYGK_xoOXH2OH25f6SKBV4YpDxVm2I4L6xqhk-ewia0PBzEZC6K-RM53e6ISCFBA4RtX5winbt-2KWlWwymmmmRieQi0JX-ACJrbragSFPXc-qJjkBXALJySBN2WIHc-DztvAWHRe2thhGnPZSRnhqq_M6UX0L6k4f9AArUxZhIN3ysq4nIRe1RuqNQFoMbb6xiKYRdqWUBLa0ldfTyCxZaPjUKMD1-_a_ueiRvqMc0VIQboavRpe9P3o61txXdRficiHym18-_oYKd_v94JaGh27R3DQxdPddpruG5bMvNJxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Tv27NxLoH4HKIOg1_rilMC4J4bmQ4evsqH4SuXcg5r4zC91x0ZfG-3e6o7ouAG4QUhyeaG_HgAYyKV91jgxhJFUJiNCqsZBkr_E7KHPm087_hzbqeMVkQqMThqPBN9r0GdWfL8kNx9xVeVRJ1ere2i4_kkeXpBG87UN9xVXymuxnzwroNYpFlb9VgT3kkKy9yfbtrs_47AefXMbVm3nPqwaRLgk5dyFfLJ_cVFX36g-X_LTZsWh649W25S2H36jEnHP4pvpFAIAxfECvM-NPiInK-xviGvTuT_EdC02-KCB0Q9KQjvo0sAD3Aegr7lb5j0BVFncxwyj1LQsy0A-w2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vXd9fJCwcTynh7r7vjFMlLN3h6YvTFXbxZ2cFtlkKeJKflu0oi-rUH3FSIfEltcROLO_6zKWQ47_wZZbedWrbjyX-PsKoBHm9GjrSoexQWENEi5MH3HUKG9b06U_KXYeJwPOS2UWSka1smwXnH8qXflX656B7IoXfAcN9Kv-lAh-DNP1npkadUktlflVYeDe8ZL5rntEzzvgFmBHiIhlPEhqJmKzqlaA0DgRBPH0NxsUdf8Heu7E9BzDR2KgReHrpODSdLr3RCMuVXQ6kMMw0xkBQZgm7kkPCz-ToQEhR6_4TbUyx7LFxFsKKUD_Lg9PaSdHw0bH3i_65Je1smkq6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ AetherST Tunnel یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که با ترکیب هسته Aether و SOCKS5 مبتنی بر HEV، امکان اتصال از طریق پروتکل‌های MASQUE، WireGuard و Gool رو فراهم میکنه.
👉
github.com/immaghzbad/AetherST/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bMF8Xj8oKvMI-GNKb5zZyOFeE-2kHXqIwkI_Zq-8yPj100rsgboUAdKI8SVBZ-rgTKA45em6niEs8X3jHmt1KefSrk4snL5Xm0MoGv1Whxe_w2O24RyTHWTtv9ctaRPYo756MF3ixzmMzQFUEUxd1ojsX-mddVX1tt9F3OnnIrF3XHBnxdUhfLKGoWd1X7vO-Hj3swhBuYduz0QrDmiTrMYM5LqLUAPA8Yf8KRtTADZuy7KSePdZKGOewuYxdwzxSH_8u6mhfOE3gswEQLzmvbQTVcjmueKR9ggiNUDdtnwi7o_FAXTYmf-Dkz0NUjrhgAV9y4KGoQFKzyAkA_Gx4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از چندروز آینده بخش جدیدی از قانون هوش مصنوعی اتحادیه اروپا (AI Act) اجرایی می‌شود که شرکت‌ها را ملزم می‌کند در موارد مشخص، استفاده از هوش مصنوعی را به‌صورت شفاف اعلام کنند. بر اساس این مقررات، اگر محتوایی مانند تصویر، ویدئو، صدا یا متن با هوش مصنوعی تولید یا به‌گونه‌ای دستکاری شده باشد که بتواند کاربران را درباره واقعی بودن آن گمراه کند، باید برچسب مناسب داشته باشد.
همچنین چت‌بات‌ها باید به کاربران اطلاع دهند که در حال تعامل با یک سیستم هوش مصنوعی هستند و محتوای تولیدشده نیز باید دارای نشانه‌های فنی قابل تشخیص برای سامانه‌های دیگر باشد. البته استفاده‌های ساده مانند اصلاح املایی یا ویرایش‌های جزئی معمولاً مشمول این الزام نیستند.
در صورت نقض این الزامات شفافیت، شرکت‌ها ممکن است با جریمه‌ای تا ۱۵ میلیون یورو یا ۳ درصد از گردش مالی سالانه جهانی مواجه شوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KL0uGfjNkMt9VkUVORVqhstfYs2q4RDtTUXri6i9nM5Rl7S3VuHrwRUgz6s3uD2JhkVk8khIoNJyiMNrSytqcOgKX_hO-2Cj92lgqTV4EiWeP732kTuIqNWhS_h2Lxm4Jpm9vi5uz1q4yr6SXCsAdADB-etWwVO1pfiwvzoF4_QgnWdb_yubPxIghlOT3J_t4-cTv74Vy36VUyJtAakSyTDglUf58UTEnflyhI2hF3GZF6LT_yLBGpm_lD4CXDD0x7RgtE06xsrtYje8h7OYTEbuVWkMHCVTpQF7r4Uch3VQyKcN6xFWfEvRJUnIXdpp9Fk7UtNwD5ntY9Nu9WZjjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسپرسکی از فعالیت تازه گروه هکری تحت حمایت حکومت ایران به نام Nimbus Manticore خبر داده، که با نام‌های Mirage Kitten، Smoke Sandstorm و UNC1549 نیز شناخته می‌شود.
این گروه در حملات جدید خود از یک Backdoor ناشناخته ویندوزی به نام NightLedger و دو ابزار Tunnel با نام‌های BridgeHead و ArcBridge استفاده کرده، که قادر است اطلاعات‌ سیستم و شبکه را جمع‌آوری کند، فرمان اجرا کند، فایل‌ها را سرقت یا حذف کند، Processها را شناسایی کرده و از صفحه‌نمایش Screenshot بگیرد.
بخش نگران‌کننده‌تر، ابزارهای BridgeHead و ArcBridge هستند؛ این بدافزارها سیستم آلوده را به یک Relay مخفی تبدیل می‌کنند تا مهاجم بتواند ترافیک خود را از داخل شبکه قربانی عبور دهد و به سایر سامانه‌های داخلی دسترسی پیدا کند.
روش نفوذ اولیه هنوز مشخص نشده، اما این گروه سابقه استفاده از پیشنهادهای شغلی جعلی و صفحات تقلبی استخدام و ویدئوکنفرانس را دارد.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فیلترشکن
#دیفیکس
در نسخه ۵.۸، هسته وی‌وارپ رو بروزرسانی کرده و میتونه به دورزدن فیلترینگ از طریق متد مسک روی بعضی از اپراتورها مثل همراه‌اول و مخابرات کمک کنه. همینطور مشکلی که باعث میشد فرایند اتصال در همون ثانیه‌های اول با شکست مواجه بشه، در این‌آپدیت برطرف شده.
👉
defyxvpn.com/download
💡
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i5WpBspIOKZ9HumSLnRn6XMilnpIQhhhKYb0GVoDXMnPNfwE-TJln4mONoEYnckDE8zr56GD6-ktS_msgVnWWDSmpt4yb_Tiql8CgxgaFlVgGUoASjAVugw7ZDHccCKUY0QhFN_2CvGqSajSdTAtXsvUmh32vBBCE0L6KJLqNCO0n5VmPiLRwrvWwyC5LPh9PIU03U5yH7pWf_95IoD1N4WCV4NSPSR6Vad1ZRjBNEuo4lsi2Ib53c-4M4eZJiqWypzpPEx6IB2R_yW89VnVK4qqg-60CmuKcfnCQKV7HJwTbqoHJmBHhOf-cruNCFArLN0QlgGDP6-8UTwE8GEGkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ
#Aether
یک فیلترشکن متن‌باز و رایگان بر پایه هسته Aether هست، که برای اندروید (AetherMobile) و ویندوز (AetherDesktop) ارائه شده و از پروتکل‌های مسک، وایرگارد و گول و حالت‌های اسکن مختلف پشتیبانی می‌کنه.
اتصال مجدد خودکار، انتخاب و تغییر خودکار پروتکل درصورت شکست اتصال، برخورداری از حالت نویز، امکان تنظیم MTU و Keepalive و همینطور Split Tunneling، بخشی از امکانات این برنامه هستن.
👉
github.com/QW-AI-Code/Aether/releases
👉
github.com/QW-AI-Code/Aether_Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ucQ0pIBc4kuWlrS9lqgVH4CzxeBWIaZwhRH0xo5pj7-o004eEeACZzknxKIPNHpawlNwMaszLB4IWCHjVk8-WLQAMFhdS-3T7EU-w-KbQ3HbKPXKUgXv_Omt1lMhh1XEeM7Hu40p4yGNVD8yLb3z6u7wSFe6CrG3U1qHZPITv1YgfxPrU5M5zGt9fxISRPs4VtgDO4g4dAuS_lX27Zk2hx_4PpG8H-BSUUfDo2OsbDgdKnE52VgfvRgmKqdSsC6P4mRg1k_XJGXgbkTGsDt61l_KnlC-6Zh-hYemMkcjsodNuFh4riLaH-4nyQGrGg4DYp-ccW8CXZL6SbashOp2Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین نمودار ترافیک اینترنت ایران بعد از ۲ دوره قطع اینترنت، نشون میده ترافیک هنوز به حالت قبل برنگشته.
الان دیدم یه نفر یادآوری کرده "۴۰+ هزار نفر دیگه نیستن که به اینترنت وصل بشن"!
#دی_ماه_خونین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jXh_zjKnnEViE_doCW1eT8u6e4JxaMzmVk93S-dwMyOrC8l31CK8fYm83wH6p0HsrNSjaJMjSSoayPgJYOU4rzTQINqtDStYNRWSrJ8q2KxAp4SLAxG5tDY_bRzctzdhObQtXrj72OLdqoCoQD_kaCnCjU3aWs0esArnrLIE1-GoQRWYbeRJvgpiN7PDTnnYlDM-nOca7acNs1bhEP630DfjfW8dhHuNHushlZCY7IpAzxMYjw9Qj21l4cGtunDP4ejXKYo0f2_nOZ-vqBPM90HxsET0JS70fELrCFhnnascXT3fu5zkRXpGbqr8FU1KBgYyG5EZY3NnH8ZTKqremg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته "سایت‌های ارتباطی در خاموشی‌های بیشتر از ۲ ساعت قطع میشن و راهی برای تامین انرژیشون نداریم".
یعنی از هر زاویه به این مرد و عملکرد درخشانش نگاه می‌کنیم، حل مشکلات و امیدواری به آینده فوران میزنه!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZLkWOxfQ6wBv5Pm59a7eVrBNCwtW66S3tSLUxYqCK9x5y1wJh_Q_nb9uXjY0FMpnE4sKuher9aIwPiH24OkQ0t35DXTzN8eDlUoo1UnmNep2gxq4eW9XShEfvy8Tic41gvpNmzLgyMUXoejHq5d7vTUuM_S5b7ytZd6PWxmU8jeC8YT56i3QXRnHXk1iqZo3bkS5KFYLBtFlJOX2Gl1Fg4-wWvswmI8GNBA-ms-6T-etQxfu18CTzpai4CQnUFR0znvb6niVsb8FoUmpGEs0hon-Z0I03QxnC6lS7kF-XCQZ_9pfpUvVy5IUr5qlk3x3c11-ITIYg2rcbojzLSDOow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی هسته ایکس‌ری از نسخه ۲۶.۱.۲۳ به بعد یه سری هشدار برای قابلیت‌های منسوخ‌شده اضافه شده، که شامل allowInsecure و Shadowsocks، VMess، Trojan و VLESS بدون Flow میشن. مثلاً برای Shadowsocks این پیام در لاگ نمایش داده میشه:
"The feature Shadowsocks (with no Forward Secrecy, etc.) is deprecated, not recommended for using and might be removed. Please migrate to VLESS Encryption as soon as possible".
اگر در حال ساخت یا انتشار کانفیگ‌های مبتنی بر Xray هستین، بهتره به جایگزین‌های پیشنهادی مثل VLESS Encryption مهاجرت کنین، تا بعداً با حذفش به مشکل نخورین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KPwaNGXqsgj6B6dyna5mNid-GOHp0XeV1j2fu0t-a5wmLRDYiO9ZPkluB69nrIK_i9Y3B6JDlwbxUmLwb9oM91jkRDMamiuVZY0C9cGlYuLgZSWCY9mqDvYFPERTv77WunpKJ-k-quWns9Prh03K6LBgZGu4hTysiza94MeC_Brg5Gwq8SyVi476Shjul8haEnkvcaYZvgzmZMkaFzFb819PbL3_saTvAaLentI_6MUQG22AI3qmfnh2gzcSEfp7toIrYG3CDy9KzLbrW9XRG3TQ2sqEwgs-3RLvAM-bZNOa8gW1oZXMiyDhF7woZ4uS-hRSMRuQWOWvFhXwE8DF5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت دسکتاپ v2rayN یک بروزرسانی امنیتی اضطراری منتشر کرده و از همه کاربرا خواسته هرچه سریع‌تر برنامه رو بروزرسانی کنن. این هشدار در چند ریلیز اخیر هم تکرار شده و توسعه‌دهندگان تأکید کردن که نسخه‌های قدیمی حتماً به آخرین نسخه ارتقا پیدا کنن.
در توضیحات این بروزرسانی اومده که "یک آسیب‌پذیری امنیتی بحرانی در دانلودر داخلی نسخه‌های قدیمی برطرف شده، که می‌تونست به مهاجم اجازه بده فایل دانلودی رو در مسیر انتقال دستکاری کرده و به جای فایل اصلی، فایل مخرب رو بهشون تحویل بده".
👉
github.com/2dust/v2rayN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KXW0DbNcS_zMzaOuojCKjwSHGCvZ_kpAHHb6oBpbH-PzKKIUJvr0_QjMTwmXj_m1PWTcletM2353-DLv0vNHPxpFRRBHh5X2b9mPtRUu27I0H0j7P1hbS1sT5uj3CZNV8oKc346Mxy_TJJG1qrB2_GBX3G6jGxoFzfTm4JhIM8-a2SfCxhbsmvG5GdUquQQ42Taxt9zi_-H6RxHyZjK0ylDEnnGBtUqMZTgSmTPXOX-k1Ff8Utf24H-MbF3MHEkdtqh4GjgI-V3kZM2T9zhFGROZux5XSORpIWTSKkfFu2niJQWZIoAd56jAroSFuI9XtjUhwpRkfzXVecR6TvKP0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IaNvhEvyXK85GmVEE9Gkq4tm8YidDN-BxB_3cPjtZQwrDcXpjvE--mbrUSIfp5HSopaOPwg657P0GQ8Y7Uj0PVcJqoV8BGJeP2N6q78acscz6EP3KQFaOQ9g4sLr6vHq2jAd28onQj0brHsil3CwlvGZ1_7fV00FWxR0EBJ-qCORn9vQ2uQg21vT1D7XVCILafstJhsyh6HaBgs_It4TNZp_sqhkk5bnirHxMia2YkPsFYubikENu49QXnaf8n2VuW2y5cjFyEfbTDsn9SOWQGDi7grXsNZzYzpD3eJYuW8WFBxQXELSo3d0ud7-6y8mJWXyvGsDxT5dVpEVE8PCew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ABo4dXSaTePOiKTvafHGqoQ6LDsTHkixx_3pGT6cqbwCIjqsGhiIhZ2u_L98DbwvEqM9drouwQHxmpMFvI0QYvw55p7LwSMjgE-D3cg6b3f830u7wD7Zvydst6LhyEUd8xOQhCbluH4J-G_IC6gb0GUwva2dUuHzvGPC5LthGW4mJcyWGp3mmkBL-66pzGjBgxe0aulZoOazQG4jefwNujcrpAa48XHXh85Qp7q7Ba1X2d__8r8nltJ2w_buwVOMoDsT_nhckim0X4bvOy9UFEKJz5fnYTp34wbgf9D4vmdP0UR3gZMGXjZORyRhXKopcXi0eUpGdzQcfFZrRF-Ogg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MJ3n90tACeAxAUfLu30j6ndTDLURv7KFB9KVhUCFBzd-Dpt384Y6pBcAd-rVUdR_TtMCYUSMHBYkrvgDAUBk3OAMKnAtoxujcnF_tIXDcp7Jw0Yfid-vMsSbQeHYCyXGIfqucDVDPOdoIyIrFGAWq2-KeA7yR9EmUjW33hcRGqysAaHaL5snzbFjA4ArmSJqXzFOf1Vgb8WEeGVU-p1_qn5MsobHfrDQr6a4lEODKJCQ4fTHYq1mZ8u0JsxfkrhqVRsCDciypq1WNQGSvzXWzgXdNCGIH9Ub-wvZNOWQRL9NI8G6Y-mjGJ-Qv-7oQEtc0IVTPvpPfZzJmcTB0W5mIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ ShineNET VPN یک فیلترشکن رایگان و متن‌باز برای اندروید هست، که از امکان انتخاب هوشمند سرور بر پایه هسته‌های Xray و Aether برای دورزدن محدودیت‌ها استفاده می‌کنه.
👉
github.com/shayanheidari01/ShineNETVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jUwaRnhGp0DDl8UV8rBuWVW_S7JVLyQ1A9ih7OcHsDV40drMCGm7CA3rBYFEMJp1n9yy91ejqBFDfdFAY8AwbqibLxFyxQvn0pth3eWMtHUqUWk4u7EziUqMjQ3iCC-WwFl1uWNjw1hwO3l36YIF1BywdoF1MDkUcnVy-8snRrFExE9bqWqss25U6TTXTuwPEVgF1NXyw4E0ynLVNgB5Lv9aUmXd7zlHhS3xIiQZYJ84hJUCqTLcVdZXZhRnoYIYjrZtswjfDjHl7_4Nb9mmn8isEMi5B5eczt684zexqurDv1zo_m0Jr7mxR5AFzuDLjhfDQXGG8GW3HOuVdhMLVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EXHLaqP0-DXqSNdF_rdUGkLlIP3mE4rHxqK5E0pnlSm6FpZYWksCZqfO3mMgRGbwOoIqeLKapN1shhr3HQ_KZhzwHCUIOrXIgZ-zJGf7-rJSbFJtrzxaXSSZnSTxxgAv7t4-_B7F7Z1KMTQ4ySU9-OS6gAFSLNlPR8rx6EgGocdPER4mVJvCoPB7guKlze-tBmyI31qiN_8L35YM6bcgurLCWAGYVGnlYS4tk64Fe5VXB_1G8Yv4Flw1UjSNc7rRIPqi6Pzzd_y-zL02H95TbVxNSnhSLQ1QlEPDqV8W_CLEIN2Ha_2pldqtcryMTSx079h2GeOBEa4R2tf63IJChw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن Aethery برای اندروید یکساعت قبل به ورژن جدید از هسته Aether بروزرسانی کرده. اپ Aether-GUI برای ویندوز هم کمی عقب‌تره و ۳ روز قبل بروزرسانی کردنش؛ البته احتمالا بزودی براش آپدیت جدیدی ارائه میدن.
👉
github.com/ZethRise/Aethery/releases
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aonP01gjfypCZ9uc_EDXax9wzJQw3gqUcqzvUswcWUnpuAmDAWf8LkrMnSTT1Lmmk-gN-fCof6z_k7SnoZAMiNtZm4pqdhBEkYYneVn6M5rcRepk0Vg0oSw8UOOA37MTcNte-QeY-u5mwux52dvGOX15YCx6Dk8z_LLOwouD-yGIwFlv7ne-qLJllPlVV4SYeBie9ygtNK2gCnewPcwfUBbrP6uopmn75gMi78nfMeY28kqb1IWRc9V3hjfg7SvyysquhSV_JZ4ZXN2hQj2wog9YouZAENE0rNVJ8UfWn3ntmG3hWLvVjLl4MX8VOGTu6V6HA6ZxEKE94-8hYts6NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۳ از پروژه متن‌باز و رایگان Aether منتشر شده و مهمترین تغییرش اضافه شدن حالت اسکن Ironclad هست. برخلاف حالت‌های قبلی که فقط بررسی می‌کردن یک اندپوینت در دسترسه یا نه، این حالت قبل از اینکه به یه سرور اعتماد کنه، یک تانل واقعی برقرار می‌کنه و یک درخواست HTTP از داخل اون عبور میده تا مطمئن بشه اتصال کار می‌کنه. البته این روش زمان بیشتری می‌بره، اما در عوض احتمال وصل شدن به اندپوینت‌های خراب یا ناپایدار رو تا حد زیادی از بین می‌بره.
توی این آپدیت روند اتصال مجدد هم هوشمندتر شده؛ اگر ارتباط MASQUE یا WireGuard قطع بشه، Aether دیگه برای دور زدن فیلترینگ مستقیم سراغ اسکن کامل همه اندپوینت‌ها نمیره. اول همون اندپوینتی که چند لحظه قبل روی اون متصل بوده رو دوباره امتحان می‌کنه و فقط اگر از دسترس خارج شده باشه، اسکن جدید رو شروع می‌کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پژوهشگران امنیتی Insikt Group وابسته به Recorded Future از شناسایی یک کارزار جاسوسی جدید خبر داده‌اند که با استفاده از بدافزار MarkiRAT، کاربران ایرانی را هدف قرار می‌دهد. این عملیات به گروهی با شناسه TAG-182 نسبت داده شده و طبق ارزیابی پژوهشگران، ایرانیان داخل کشور، مخالفان جمهوری اسلامی و فعالان مدنی مرتبط با جنبش‌های ضدحکومتی مقیم اروپا و آمریکای شمالی از اهداف اصلی آن هستند.
مهاجمان برای توزیع بدافزار، نسخه‌های آلوده برنامه‌هایی را منتشر کرده‌اند که برای کاربران ایرانی کاربردی یا جذاب به نظر می‌رسند. از جمله آنها می‌توان به فیلترشکن Pis2ray VPN، نسخه‌ای جعلی از Star VPN، برنامه‌های YESHICA، YEPlayer و YEMPlayer و همچنین یک وب‌سایت جعلی با هویت Starlink اشاره کرد.
بدافزار مذکور پس از اجرا می‌تواند اطلاعات سیستم، فایل‌ها و داده‌های مرورگر را جمع‌آوری کند، اسکرین‌شات بگیرد، دستورات مهاجم را اجرا کرده و ارتباط خود را با سرور فرماندهی و کنترل (C2) حفظ کند. پژوهشگران همچنین زیرساخت‌های جدیدی را شناسایی کرده‌اند که نشان می‌دهد این کارزار همچنان فعال است و احتمال ادامه فعالیت آن وجود دارد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EZWX-mUw-BYaHmTI9taDN8yrdUsPOIaKFqJSyHssB8J0w7LjdEXasFUdLOiES2ODPBzn8I7awTGdXhp41K-niFP7l4yEcVg45UpIhN1Jd56uQxZ4Fc1YXxeeQi9Oay-yTlyuJA-XSwsfVzkPGq1CAU7rwQPxUhpRO9mwR0YlADKTr8dO7Vla7eEKc1r5l0A5jJo3EWo1RlPGldtVpt1kjBa6GJJ-WxS8SyEqiDylfGtuNmeZI_H8XV6dTtw2v1imOLDO5wvsiazwJfGq8WKYhS24OMBmHGok-5KsqsGV4AVpnnfG8XVpeJGlBRBx1sxxx7AeUCZB7WdOE0RCrvP1pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران امنیتی از شناسایی یک زنجیره آسیب‌پذیری جدید با نام wp2shell در هسته وردپرس خبر دادن، که می‌تونه به مهاجمان اجازه بده بدون نیاز به احراز هویت و حتی بدون نصب هیچ افزونه‌ای، کد دلخواهشون رو روی سرور اجرا کنن.
بدلیل شدت این آسیب‌پذیری، جزئیات فنی و کد اکسپلویت فعلاً منتشر نشده تا مدیران سایت‌ها فرصت کافی برای بروزرسانی داشته باشن. این مشکل در نسخه ۷.۰.۲ وردپرس برطرف شده و برای بسیاری از سایت‌ها بصورت خودکار در دسترس قرار گرفته.
©
slcyber
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dzfYYaDwHZb16KB8lK-emGheqhNOsYhppgXRvezDxRrEIQxVU2j5YvqFaQQB1V04fNjvlhSxGk6GT_rsDA6teHBXnax4jazTORo_jvW3WDD_goP06gDcLDQMEfZBa1IaPtYN1AFg2RsRx6hvI57ZjQnTbsfnrz5_axcDRsD5K1AaKl1Y86npmAeMohk2kGr8afFWpXy32gd7tUzBgpRkYLNKL_mWATg0QGSruQsgfEBludVmYrdyLbnEiiOrPZEfpqjXb0dw1WZ44mSlZf_z1mYkHbw-0jJLCG8W8D2EfX917x96smtHEqwVt4o-Ov_AvsC2y9Qf6l0VkJIXQzgUNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ozgrWNxZUGJCaOD7fdzxu7f3g0J4pHvR-62O0IGVzv_AbvkZeWzVGRLr-klJaY1g81yyP1OeUeDqf0IwG1TiSfLG7uBSgHhD47qmV1dyh5mwEqDEOEVv0lLcxvs6DZtbnZ_RXoLrnrsOGV4QuGow2joMZTwoQxAWHR7mwFNB-gtnZuBcJuLO5mpKZp36ASsWPBjvzaRykDMmw9-3FZR6QW5xaBUrw01AuFW7sTl5vgQ7C-dXhsnHOf7IQOT_JlTA0pU96BdPoemAz9b-7WcOFbGmtLwg_mjDFGpzgWEhRYCeDN6UcLBuNp8EebJYcgHh8vVXYjD6eU7vI-s6awtMSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ dicodePing یه کلاینت متن‌باز و رایگان برای اندروید و ویندوزه، که مدیریت و اتصال به کانفیگ‌های مبتنی بر ایکس‌ری رو راحت‌تر می‌کنه. این برنامه از مدیریت سابسکریپشن‌ها پشتیبانی می‌کنه، می‌تونه بصورت خودکار بهترین سرور رو بر اساس latency، jitter و سلامت اتصال انتخاب کنه، از حالت TUN/VPN پشتیبانی می‌کنه، آمار لحظه‌ای اتصال رو نمایش میده و امکان تعریف دامنه‌ها و برنامه‌های خارج از تانل رو هم در اختیارتون قرار میده.
👉
github.com/mcodersir/dicodePing/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پژوهشگران دانشگاه میشیگان، دانشگاه نیومکزیکو و مؤسسه فناوری دهلی، ۲۸۱ وی‌پی‌ان رایگان اندرویدی با بیش از ۲.۴ میلیارد نصب رو بررسی کردن و به این نتیجه رسیدن که بخش زیادی از این برنامه‌ها برخلاف ادعاهاشون، امنیت و حریم خصوصی کاربران رو به‌خوبی حفظ نمی‌کنن. توی این بررسی مشخص شد ۶۱ اپلیکیشن بخشی از اطلاعات رو بدون رمزنگاری ارسال می‌کنن، ۲۹ مورد دچار نشت ترافیک یا DNS هستن و بیش از ۸۰ درصدشون هم با سرویس‌های تبلیغاتی و رهگیری در ارتباطن. علاوه بر این، خیلی از اونها هنوز از تنظیمات امنیتی ضعیف یا روش‌های رمزنگاری قدیمی استفاده می‌کنن.
اما نگران‌کننده‌ترین بخش گزارش مربوط به ۵ وی‌پی‌ان بود که فایل تنظیمات اتصال رو از طریق HTTP و بدون رمزنگاری دریافت می‌کردن. این ضعف میتونه به مهاجمی که روی یک شبکه عمومی مثل Wi-Fi رایگان حضور داره اجازه بده تا اتصال VPN رو به سرور خودش هدایت کنه و تمام ترافیک کاربر رو بدون اینکه متوجه بشه زیر نظر بگیره. به گفته پژوهشگران، ۲ مورد از این برنامه‌ها این مشکل رو برطرف کردن، اما BambooVPN، Free VPN و 101 VPN همچنان در برابر این حمله آسیب‌پذیرن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DiYntoa95WRi_oWouH5VDfmWjG4q5j3hLvjt15FsEFqG5X7WlLXVB1tzkLHEpUS1B7vJ96ainDR_ymfCRzyqMbwgocXQ_rvTu91-SBdjH6WxCLaN3QrkgNDzSP2E6AjivfTPtjqhdX2EbRMlPwFvbfTS_QrM_ztLhEggjgrUQa3lElijMNOarf_S9EzMInZg-BMYHcEGPIjRI4RZzDKspgY6IPOndhZsxumcqJCJLiIZQRYiRkUuJRpeqknnUxDZTvoIQM0pRNjagZyICXd8_iRXIvdKe89ol526_v9cj-hSQudHXTIA9OkzPOfNhO6nYePQ_pgCtWgpn1tlO6YobQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aethery یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که بر پایه هسته Aether ارائه شده.
👉
github.com/ZethRise/Aethery/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KBiZBtyUem199SwaNHNwHHHhDIRkG2M9c6EuDctkr0DqqKZdoD-RdGHEq4WriYC-Y7ZPXA4040A2ieTJ-nlEnxwq_MSvZkCaKyf3nqY9Hbg0HrLQ6ILcHLJ3IMUMopxg-nrjm-PTIksyIIcGYjricceYFmcaTBqk6PN4xEal1oT2SAEh1JaIViuyRpCrlY4M9ZbBQEA-4FoCTs0TX8gfH72nW3ksyUTTQGNKndhmXxDnX9fH7nWwo0nDmo3wnD4zq6UQJ5muUvNdW-uE9axjA14J2ZIsBbK1sv6ikvsOwiL63PeTWaRlcjH9kbEwx0rUAxH_lQMVh5yw1SVkoFoi2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت رسمی Sing-box برای سیستم‌عامل ویندوز بصورت پیش‌ازانتشار عرضه شده و طبق اعلام توسعه‌دهنده‌ش، همون تجربه‌ای رو ارائه میده که پیش‌تر در نسخه macOS در دسترس بود.
👉
github.com/SagerNet/sing-box/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
