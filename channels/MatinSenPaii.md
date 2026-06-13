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
<img src="https://cdn1.telesco.pe/file/M1LkiLFBl8Oby0570mcZU6SeuImBA-KyqgYi1QeNVuPT1i3Fenb5uZPOXRPJV90aAIRQwXrhjNCo97P3poTQaLGzgdu3HiKRqP-XASaQRHSOBOoLib9bN5ENliYv8f7fgrdX9_y-bj-KGrQeCkjsmvy13En13outkyVNRLWHVagzGOavNbqzgvvrmKYitN0aQUUXIfTMw-XjY7ZLJIh6X27cbzb-O34-QcifHZ6Fs2EpLW950pIls7qQ0l2KNRby6jpWJTvYTeoqxXKKgu7l8HeiyguayzSXhugkxShzKYjO85Oab4nIHOtV9FPvaWt_Kb8oTZAucPXLt18VRImFNA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 162K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 00:15:23</div>
<hr>

<div class="tg-post" id="msg-3865">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DIIoKhab-VQVly9LmjObotOnhEgVeV9Ve4nhqlxK2K0LpbOdYrUodmch6gKXvp_hU8K9xzVp3VFq1HyHrr1CcrEnJ9ciOfsqoK42Rajn_Oh4sFC0NDfkGEtWMjgnenfAunaKod-kjT8xm520gnIKq80_wh-eFw2VxlCscMet5r1r21DbOaE9YjIxt7Px69ZSGqFDKCFRyERNY_eKdaKJGP-a__838rz8GBsSshH1pDx1FsvMUW2QX24gBpY2YqM9GyKwM1M1f1fGcZmBTW26KVSKT703Yahg7j06xGTKxanuQ3Z8wf5ag-yxo93NYfN1h9I7Dqrtz8de3V7XiV_nlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا به هیچ وجه روی کانفیگ Websocket معمولی سرور شخصیتون نباید اسکنر ران کنید. فقط روی Workerهاتون انجام بدید که ارزشی ندارن و ابیوز هم نمی‌خورن</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/MatinSenPaii/3865" target="_blank">📅 19:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3864">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">برای اندروید و ترموکس، کسایی که مشکل دارن طبق این آموزش دوستمون برن</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/3864" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3863">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">برقا باز شروع کردن به رفتن؟ خیلی دیدم امروز توییتر وسط کد و گیم و ادیت و... برقشون رفته بود</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/3863" target="_blank">📅 17:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3862">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مرحله اول  همه بخش مرحله یک  رو کپی و توی ترموکس بذار
pkg update && pkg upgrade -y
pkg install golang git -y</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/3862" target="_blank">📅 15:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3861">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دیسلایک فیک میزنن انقد خوشحال میشم پولشونو میریزن جوب
😂
(توی یه ثانیه یهو ۱۸۰ تا اومد)</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/3861" target="_blank">📅 14:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3860">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">نمیدونم این کانالای تلگرامی چه گیری روی ری‌اکشن دارن
میگن ری‌اکشن بزنین انرژی بگیریم. انگار از ری‌اکشن برق تولید می‌کنن
عقل ندارن راحتن به خدا</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/3860" target="_blank">📅 14:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3859">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دیسلایک فیک میزنن انقد خوشحال میشم
پولشونو میریزن جوب
😂
(توی یه ثانیه یهو ۱۸۰ تا اومد)</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/MatinSenPaii/3859" target="_blank">📅 13:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3856">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WviA-vGSGVf5w_rqP58wb-Pmv9lEwZg9YTMSl9UZ7GIzAWPoEaGs1L4Br89Imldy1K0JhxUJbD0ypEZ_vTX-aHWszaLzvBgyHbaRfgyWfHLLJU2Pvrjc8kAIInwcQ7S7937_C7891MqvijXZSRDuau7AgoFAynFFJatcx6-XDN62ic3qQ0cPcXJ3aVNtZROETK9Uhh6K5-7fZQoLD-qwuSWZFkVo90Mq69MzBp88K1o_rk_1uBe9KR2PCN-KHyFGddgHx1EtiqGThlX7yRiNK5G6TH2IEwTEz1TMd7ModrBn1FRgJRGwNINhyZ1PSjbbQAsbONwwdISkH1VJe4YEbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Zj58fJSUOfZrbPxY2PHT1JPC3Jk2CoGFXARKW3T3A0jy_EHKoGSGh3aeRR052Wl4WQksj9ySyre_97rD1DePHgqT92BtnY8lh6zjHgI7gby2cZngDC385GYfhVpxgltOr0pqFSbXl2kNGx0d02U2D3ShdaOUgRkPkRdn8aSpvQrPRpMhLcGVmEcK-0_sAfmQ7R3LoqlXIJ2vwx9eVOG1W9xWXekDjfxYDBMLROE-06oNLnGZlPWmGW4surXrdJXOHkKgPQZOfAZKPpRROOqVoolFbzbhEJTL7m2uKYidN0r45g-BCJCJMDdideiN4vgk-OEKh8CvOxEXh-P_qr0zFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BfDlcRZdIPF8QLfg4NleJRs18LN0Ha2PysBcYEtAmMCTXGKPy2AXj2O2X2n_EaFmW2rVLpC5bZcizulm_MC4aLrjavdz48ffJMBXfGybM6TJdBhT5UtLXpPaNeTVEyiS3lh_U_Jvhx4-OUN52iRchrorNXOKenStZXhPpZXwyKsNdpA1i9Vscu4kX3WdiD4HnzqLkqDIbRNEebnHqx5E7s-i8aRmpkxy44EhHvooc9ZUnY9SZ5gh9HR1_eolCYhFzPGC6E8NjCD0FsL27nwZ1S766m7APgMD3sQTEqCvyVr8p2uUGSQFUn0VjvlDcxuJAUVQVjfr-QKxhoTOJ8b4aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن 0.7.1 از SenPaiScanner منتشر شد
✉️
😏
پروتکل‌های جدید
: پشتیبانی از
Shadowsocks
و
VMess
اضافه شد — هر دو از فاز ۱ اسکن تا فاز ۲ xray کاملا کار می‌کنن.
🧮
خروجی چندفرمتی
: با زدن
e
بعد از فاز ۲ می‌تونید نتایج رو به سه فرمت صادر کنید:
1- لیست Subscription
2- Sing-Box JSON
3- Clash YAML
🔥
تنظیمات سرعت
: فیلتر حداقل سرعت، تست سرعت آپلود، آدرس سرعت‌سنج دلخواه، و سایز sample قابل تنظیم.
🤖
ذخیره تنظیمات
: تنظیمات اسکن ذخیره می‌شن و گزینه «retry last scan» هم اضافه شد.
📚
پشتیبانی از CIDR
: حالا می‌تونید توی
ips.txt
، مستقیم رنج‌های
/13
و... بنویسید.
📱
اولین نسخه پیش‌نمایش
اپ اندروید
با Kotlin و Jetpack Compose اضافه شد. معماری MVVM، تم‌بندی کامل، و ساخت خودکار APK از طریق CI/CD(هرچند CI/CD باید روش کار بشه هنوز).
لینک دانلود آخرین نسخه:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v0.7.1</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/MatinSenPaii/3856" target="_blank">📅 13:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3855">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دوستان، این شکلی میتونید به من پیام بدید:
https://t.me/MatinSenPaii?direct
اما از اونجایی که دایرکت به شدت شلوغه، و من پیامها رو اسکرول می‌کنم پایین، ممکنه گاهی اوقات زده باشه سین شده، اما من نخوندم در واقع</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/MatinSenPaii/3855" target="_blank">📅 12:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3854">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حقیقتا MiMo اگر پلن پولی بده، خودم اولین مشتریش هستم. توی تسک‌های متوسط Backend شاهکار کرد امروز
هم توی سرعت
هم توی دقت</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/3854" target="_blank">📅 12:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3853">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هم پشتیبانی از Trojan و Vmess و Shadowsocks اضافه شده
هم تشخیص ISP
هم تست آپلود و شخصی‌سازی تست دانلود
هم WebSocket(که بهتره On بذارید)
هم هسته رو به کلی بازنویسی کردم
و این به کوشش دوستان عزیز برنامه‌نویس دیگه هم بودش که اسمشون توی Release note میاد و contributer پروژه هستن. من شاید 20 درصد از این 10 هزار خط کد که اضافه شد توی این ورژن رو نوشته بودم</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/3853" target="_blank">📅 12:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3851">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GPf5KPPSj95SLEAig-7EK_W94Lov-Em4CSc0JfyfWVOZJUflx84OrTtQexbJtxnz7FfhugfaTPVYyeDBEvn9t85CCYr4Etg9r4hRJy6HWrFXUQZJ6xarfeFc63lIBd7jbNcf6t9r7mbWTooS2dqH1jCkzo3MPFXLoQp4hB06NpEekJxzNRfQhVd4JC7ou-ngAWB0dM3Jsg645y7vdvPi2F3cB55sEWwEibO6CpMIa3TgJxt2asPECKlDR_izylMGiW3-RzJh5Kxi_Ypglg6GkzZPN3itBgUUEZLnv4ogTcgGfiwXIJOuKA2_J3L3LotREIGGt3UwoKfybKoh2dN6nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bJv65Mq3Dh8hd89KLUD94v3I_Iy9rJn7JQvCBoY6JM0vaj11AS4L8vMcKi01Uayp_GmwjrHPFTGnesWQ4AeEDrtsibNRCiUmXtrpyx0Mw9IpQ4QLWZIkKgTFlHiMzxYrH3t2EAvRxFzEPvFIn5sFZxz6BDLMpe91PLx0KMqIWQ3XTQ9-rckIvHYfII_m55RQbAixCCjcbXybK9t2XgdCHuSg7JzX-J4jCEh_dp8pEQwTT_7Fo0ABSo7EBdBSNoC8dIbzS7h-hPOgt1RwUwaWjO1xbHEVDJXjqDnepBDV8OlFAAXW1PPioELpe7S3t1sN9gxetweCMVz3MPWoxoBulw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بازخوردهای خوبی گرفت این ورژن که باعث خوشحالیه
❤️</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/3851" target="_blank">📅 11:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3850">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/txJXexkfrcW0fkSk-E0ScXGu1RbUPI0I9eVhJHmx-_vmOU-6ApNPckkf_pFjHLsXdlewnAk5pnjqMloaEVTSgR8Q496YEUT-k0lA69_ne0ac3_zo80NicHQUisDubydCd27CuXnHnRXLwIgRoPwadbk9BZNG3n-h_wjIPqdsf0Dyy4kBZ67rLjuVRVMKIv15mz6UqWIAIwIGOgWOwJCGTJIQn1fTtZ9reNeCHRf51M2Oguf0IxszsPS76NNMC7_x4-QezI1a6lWEZ8AL0h1dEKNyaPQnf6xdE8xgVq6PEsD4IuhtucLmFqsetZc-0e-0YMetFspioYiJphV0uCSzgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازخوردهای خوبی گرفت این ورژن که باعث خوشحالیه
❤️</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/3850" target="_blank">📅 11:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3849">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/3849" target="_blank">📅 11:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3848">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kQDgRA5ENPvojGumFw3LzlqbhIO2yDW5r3oVFk_U-AHYUz82ubHSoZM0QVz-dMjnbJTdfx5gz2yLqBpXlk88jnm5tPG3L37MwYr-2A69xP2DU3TZWyOXfNP5kqIn4WuNzXcW9XqUclxpYSz9ZLoLHFQk0hUAT2XgwaHsxxRswqPw0JEiFqBePcEWvR7OTcx6PIxy8-Dwp37m6MvZgavwFUdg8kpQkB7vMRbMnCR7Jol-bRZD57ywIYUPkKDNeJq5POiDOXodror1wRg3TyhasqnFPGe95iZiP8lwoHGLzLYHfy129sJk50mqcEOyu5RkVB3IE9Amvl05fa2Jzm7pjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان خوب، لطف کرد و هسته‌ی اندروید و تمام چیزی که برای ورژن اندروید نیاز داریم اد کرده، صرفا منتظرم که خود اسکنر عملکردش به بهترین سطح برسه، اون موقع نسخه‌ی اندروید هم بیلد میگیرم</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/3848" target="_blank">📅 11:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3847">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نکته‌ی خنده‌دار اینجاست که دولت آمریکا دستور داده دسترسی به این مدل‌ها برای هر فرد غیرآمریکایی (foreign national) — حتی داخل آمریکا و حتی کارکنان غیرآمریکایی آنتروپیک — مسدود بشه!!  آنتروپیک اعلام کرده که چک کردن ملیت کاربران به صورت عملی ممکن نیست، بنابراین…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/3847" target="_blank">📅 11:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3846">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/3846" target="_blank">📅 11:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3845">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">senpaiscanner-windows-amd64.exe</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/3845" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3838">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">32 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3838" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خب، دوستای من هستید یه تست از اسکنر ورژن 0.7.0 بگیرید؟</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/3838" target="_blank">📅 11:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3837">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خب، دوستای من
هستید یه تست از اسکنر ورژن 0.7.0 بگیرید؟</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/3837" target="_blank">📅 10:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3836">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ocOUc_GxG12C5VNjUSHi2wtJB3zUmV7a_BhC5YGSg243ql4Wxk3UDMmrUmvb9SIO6w3jc4wTxH_7EBeHwtnWCKy55FtZksbV0mmn6kARCcKxbSoUOLdDz1WNRQw2BOlW4io1ZXST4rt42L-3-H7uPMHU4fzfdMldAbCFptAxfRZ0xGNKmQXTcvzCQxK0H3AXwsGYBCSsJjENrkG77_X7lj68w4EcxKmAYOTg37asiQ4pdV1z6XgpG6VpEFKJSDKxYqAzrOqibkPJ2rJ4HeJ_noTHuz-iU8qL0g662JAfsds9vQ6y12zMwJUXwCmhQD2aAanRgjMftAqPqpCwmRdBww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لپ تاپ اوکی شده الان اومدم تست کردم MiMo رو و خوشگله یه تست پرفورمنسی بریم باهاش روی SenPaiScanner</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/3836" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3835">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XcZfNruqNJPdVbio2p1NyFqzfvfQRkHa1TzKYRhoNIUae89IFe3dQsQ57lOUFz31GSc6rQ2OQXKEzLM-KTqpywJQ8gep1hH6bMOD27UCbcu_mHQyecC25V5XJIjLxc1T94Rr5_QL-0SDblTrWOFyWttRi5OqF9z2QwSDn6KjTo-j98L3K8XNB-nLqj1nMdiP7rNqC2gUPXa1Fl7W-KOkATwZa5uoPQzhlqQqWL28FifuYLbn7C0QII5sx-LElFgXNp8-V7DAsjFhztI4AItLGjmgmuYtFfLdewwecE7DkAYFU7X4KHg9O4DctFZhs2Kv9Q0p3ecctGwGzxiKZ6XunQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد  توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش فورک OpenCode هست!).  خلاصه‌ی ماجرا: تیم…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/3835" target="_blank">📅 10:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3834">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">برگام! آنتروپیک به دستور دولت آمریکا و دلایل امنیت ملی، دسترسی به مدل Fable 5 رو برای همه‌ی کاربرا مسدود کرد!!</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/3834" target="_blank">📅 09:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3833">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DOtKTgcUOP-q2gFrf9oDct4da7sGJ0nYHubtiku7pDukXuwwuhk8oemJR5xFoQjoH9yxxPIUMnVqJ272TbGDHFysqH1arHiApSSQe-EhKXbiFUU9iEFACmqID_JoOQ5t0--RpQ8YtzYLHpggPWTzn6tBH88Q1SEm-0EfctKg6SrgdqbmhFPEP12Yen8FBCUAqd65TFsG4Wp9-Riew88E_YJ3_fEa1J5T8iCKhY4cm4f3OGZonkx_D-mpiltwZ1EReYkeE-CjLLgFcwBeo5ZgLhc7DCdEkWPfSV3L4HJ4j3m8X7vYHVOxHOde1xUPWSX0PRojV08fZgz77K9gJ9gntA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام! آنتروپیک به دستور دولت آمریکا و دلایل امنیت ملی، دسترسی به مدل Fable 5 رو برای همه‌ی کاربرا مسدود کرد!!</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/3833" target="_blank">📅 09:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3832">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">این سایت رو یکی از دوستان معرفی کرد برای دامنه‌ی رایگان، یه امتحان کنید http://l53.net/</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/3832" target="_blank">📅 02:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3831">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a19-R3tk3tWJf7NkyW5J2Uivf2Xl9oVsVCD7lZVFkiZasj6jrFfs9MDKhS_MyPuQuvJV13zTxIw4rzjFsMP0PR7fWQHYE6jQQ4qni6thZpXxvyt8Ds5HUXFWFvTpnJ0SVcnCrWClfzVLSZADagMOjhLyOs2y53gBached7W72BF6ajVdKGLOvsws4yj7DFqAFvZVcIr1WNAGF2pPemUtlLfmIx5Gm79WlkPwskL_2aWrNqObFE-OvHVUIqn4tzPFJ4DV2I5Pfnml_gNc4M_s8KGCOOlCo06zWjsX1l4-1xXLJiOZ5Kx08hm4lP0fTDDhyv_VDAIXiyOWTeGNLXh7Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت رو یکی از دوستان معرفی کرد برای دامنه‌ی رایگان، یه امتحان کنید
http://l53.net/</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/3831" target="_blank">📅 01:55 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3830">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">من شرایط ضبط نداشتم دوستان. یه مشکلی هم برای لپ تاپم پیش اومده که باید بدم تعمیر و ممکنه کلا مادربوردش بسوزه اگه روشن کنم ترجیح میدم ریسک نکنم چون دیگه پول ندارم بخرم
😂
تعمیر شد، آموزش‌هایی که قول داده بودم رو ضبط می‌کنم</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/3830" target="_blank">📅 01:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3829">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWireguard Configᵛᵖⁿ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=nz4jKKAuBg7aIHPh214Yzq6GvKLXVKAkS272ob5U6C5uGxAcAqvJrDWzVcKUwK0vr5ENyWHnE65ev7UvZ3SLenrLjvpoXPu82XzV0niwDwqyBgB8zi6dX3Btw63MIcvaAHyWUBmWQqevgk8f2Agxgrx-bfiyb2z-m8Ed5UbLSu2reD3fRAbeTT7Ncb5-nsACDVgJcLMhEdYPU1lgo03o9M4EdqdFL1tAwJgAzmT-84ydEaoHo6-pEnbzDtev5ww2Mr7kZc2HSUkOGkK5jpqcTThSI-3jy7HX7qmSdaSei-1NPY6F5fs3d63hFQlz3PAIR6i2iX_VNWXF0ghrNAMm5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=nz4jKKAuBg7aIHPh214Yzq6GvKLXVKAkS272ob5U6C5uGxAcAqvJrDWzVcKUwK0vr5ENyWHnE65ev7UvZ3SLenrLjvpoXPu82XzV0niwDwqyBgB8zi6dX3Btw63MIcvaAHyWUBmWQqevgk8f2Agxgrx-bfiyb2z-m8Ed5UbLSu2reD3fRAbeTT7Ncb5-nsACDVgJcLMhEdYPU1lgo03o9M4EdqdFL1tAwJgAzmT-84ydEaoHo6-pEnbzDtev5ww2Mr7kZc2HSUkOGkK5jpqcTThSI-3jy7HX7qmSdaSei-1NPY6F5fs3d63hFQlz3PAIR6i2iX_VNWXF0ghrNAMm5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سا
خت کانفیگ Amnezia VPN
• صبرکنید ای پی ها رو لود کنه
• بعد یکی انتخاب کنید
• تیک فعال سازی پارامترهای امنزیا 1.5 حتما بزنید
• بزنید روی ساخت کانفیگ Amneziawg
• دانلود کنید وارد کنید داخل Amnezia VPN
• میتونیدم کانفیگو کپی کنید + بزنید بعد insert بزنید کانفیگ اضافه بشه
🟡
فعلا روی ایرانسل
💯
جوابه(همراه اول ،مخابرات،سامانعلی)
📍
ای پی جدید هم اضافه می‌کنم
https://darknessshade.github.io/Amnezia-VPN-Config/
@ConfigWireguard</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/MatinSenPaii/3829" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3828">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کلا فکر کنم ساعت از ۱۲ میگذره دکمه‌ی بمبارونشون روی سیریک گیر می‌کنه</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/3828" target="_blank">📅 00:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3827">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XXHqqQR27TSkP9PEQEqkScao20FcFRiF3-QsQbZrg6zYO1rV-NdbphZwdYP0Z8dGpyMhregiZYwC-BX7aqjNBOCa5nqpxJS2RqPn50J9G3mhvBE72fnqCwVXBqckK9FcidssyCML7gLt6G4ao97pLyOn7a_ZrM9Ew2LhQ2DPSuE4y6eeja-k1Y3pRue7UNrqYpcJmIvulaHgEc4LTdu0hKfdR8Z7_qqe_Xr5VCzWYnIaYJ-T3ZWugD3DLnLqWyDlS7xgSGoBwRXSusytYMtXaPij2sNT4frpwYklgB_kIk_MmeHEQ-X3mytnCWXZfOOT_Rw-tCMY7I9C8wzlotkDvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد  توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش فورک OpenCode هست!).  خلاصه‌ی ماجرا: تیم…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/3827" target="_blank">📅 00:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3825">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اگر مشکل باز نشدن توییتر با پنل BPB دارید، همونطور که توی
ویدئوی تنظیماتش
یاد دادم، NAT64 یا ProxyIP ست کنید. اگر باز هم نشد، صرفا کانفیگتون رو عوض کنید با چندتا کانفیگ تست کنید، درست میشه.
proxy chain هم صد درصد درستش می‌کنه.</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/MatinSenPaii/3825" target="_blank">📅 21:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3824">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nwg5ztIFKRNdqD6icq99ZLoBXjluIxkR3vjMoP-9qk8XvfGlDotPRGKI5YMrEtl0WOcWGNVR6hrETTKrF538x1DT3_TICbn6Ler0rmsml-Gn9WFF73YLn2d3-cXzIAWdtKF-YUFnPnj1YIRB0zcLMVXiQftYv7o-jjncwlJRmDCDVl95HgavuCOmD-hTpJagpo24RysQbcGq-aqaMctc7fepYiNj-M2IXIEVnaY59ijc6gsBUsQiRu6DCX-vUN9_dGNsZ32dS-9VXu4CumcmyIzP1fB98MSKfnJykFIaobGomSY6bodiqsDVkGJzA9L2We0jCnQP_sSYmha2TEl3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیائومی از MiMo Code رونمایی کرد
توی این مجله‌های زرد دنیای AI بهش لقب «قاتل Claude Code و OpenCode» رو دادن؛ ولی بذارید واقع‌بین باشیم — یه سری ویژگی‌های جذاب داره، اما قاتل این دو تا عزیز دل نیست
😁
(مخصوصاً که خودش
فورک OpenCode
هست!).
خلاصه‌ی ماجرا: تیم MiMo شیائومی به‌تازگی، دو روز پیش (۱۰ ژوئن ۲۰۲۶) نسخه‌ی
v0.1.0
از یه
AI coding agent اوپن‌سورس
با لایسنس MIT منتشر کرده که توی ترمینال کار می‌کنه و برای پروژه‌های پیچیده و
long-horizon
(بیش از ۲۰۰ مرحله) ساخته شده. این ابزار فقط کد نمی‌نویسه؛ می‌تونه دستور اجرا کنه، با Git کار کنه و در طول جلسات مختلف، درک عمیقی از پروژه‌ت رو حفظ کنه.
از اون‌جا که نسخه v0.1.0 هست، طبیعتاً یه پروژه‌ی اولیه و اکتشافیه — ولی معماری‌ش جدی و قابل‌بررسیه.
ویژگی‌های جذابش:
۱. حافظه ماندگار (Persistent Memory):
برخلاف ابزارهای فعلی که فقط به context window مدل تکیه می‌کنن، اینجا یه subagent جداگانه (به اسم checkpoint-writer) توی پس‌زمینه کار می‌کنه و تصمیم‌ها و پیشرفت رو لحظه‌به‌لحظه ثبت می‌کنه. حافظه روی
SQLite FTS5
(جست‌وجوی full-text) ذخیره می‌شه و توی فایل‌هایی مثل
MEMORY.md
،
checkpoint.md
و
tasks/<id>/progress.md
نگه‌داری می‌شه. وقتی context پر می‌شه، خودش از روی آخرین checkpoint بازسازیش می‌کنه؛ یعنی دیگه نیازی نیست پروژه رو از اول یاد بگیره.
۲. ویژگی Dream و Distill (خودتکاملی):
دستور
/dream
به راحتی جلسات اخیر رو اسکن می‌کنه، دانش مهم رو به حافظه پروژه منتقل می‌کنه و موارد قدیمی رو حذف می‌کنه. دستور
/distill
هم کارهای تکراری رو پیدا می‌کنه و تبدیلشون می‌کنه به skill یا command قابل‌استفاده مجدد. هر چی بیشتر کار کنی، بهتر «پروژه‌ی شما رو می‌شناسه».
۳. قابلیت Max Mode (آزمایشی):
چند راه‌حل موازی تولید می‌کنه (best-of-N) و با یه مدل داور بهترین رو انتخاب می‌کنه. که با
experimental.maxMode
توی فایل کانفیگ می‌تونید فعالش کنید.
۴. قابلیت Goal Mode:
با دستور
/goal
یه شرط توقف تعیین می‌کنی؛ وقتی agent می‌خواد متوقف بشه، یه
مدل داور مستقل
چک می‌کنه که واقعاً شرط برآورده شده یا نه — در نتیجه جلوی توقف زودهنگام و خوش‌بینانه رو می‌گیره.
۵. ویژگی Compose Mode:
با زدن کلید Tab فعال می‌شه و یه workflow ساختاریافته برای توسعه مبتنی بر spec ارائه می‌ده — با skillهای داخلی برای planning، اجرا، code review، TDD، دیباگ و merge. کل چرخه از spec تا کد نهایی.
۶. ورودی صوتی، Git و Multimodal:
ورودی صوتی real-time با
/voice
(بر پایه MiMo ASR و TenVAD، مخصوص کاربران لاگین‌شده)؛ مستقیم با Git پروژه‌ت کار می‌کنه و multimodal هم هست.
۷. سازگار با Claude Code:
authentication، skillها، MCP serverها و دستورهای قبلی رو توی یه مرحله import می‌کنه از پروژه‌ای که داشتید با Claude می‌زدید.
۸. انعطاف‌پذیری مدل:
MiMo Auto به‌صورت
رایگان(1 میلیون توکن اگز اشتباه نکنم) برای مدت محدود
و بدون کانفیگ در دسترسه، ولی خودش هم از هر API سازگار با OpenAI و prov/erهایی مثل Anthropic، DeepSeek، Kimi و GLM هم پشتیبانی می‌کنه — یعنی vendor lock-in نداریم.
نتیجه؟
طبق ادعای شیائومی، توی بنچمارک‌های SWE-Bench Pro و Terminal Bench 2 (به‌ترتیب ۶۲٪ و ۷۳٪)، با همون مدل پایه حدوداً
۵ درصد
از Claude Code جلوتره(که هنوز بعید میدونم. به چینی‌ها اعتماد ندارم). اما می‌گن تفاوت واقعی‌ش جایی خودش رو نشون می‌ده که کار طولانی و چندمرحله‌ای باشه — نه «له کردن»، ولی برتری معناداری توی long-horizon.
نحوه استفاده (خیلی ساده):
۱. نصب یک‌خطی (Mac/Linux):
curl -fsSL https://mimo.xiaomi.com/install | bash
(بهترین تجربه با iTerm یا ترمینال VSCode)
ویندوز:
npm install -g @mimo-ai/cli
۲. اولین اجرا:
خودش راهنمایی می‌کنه — MiMo Auto (رایگان) رو انتخاب می‌کنیم، با حساب شیائومی لاگین می‌کنیم، از Claude Code Import می‌کنیم تنظیمات و... رو، یا خودمون می‌سازیم.
۳.
می‌ریم تو پروژه و کار رو بهش می‌سپریم (با زدن Tab بین agentهای build / plan / compose سوییچ می‌کنیم).
لینک‌ها:
- گیت‌هاب:
github.com/XiaomiMiMo/MiMo-Code
- سایت:
mimo.xiaomi.com/en/mimocode
- بلاگ فنی (درباره long-horizon):
mimo.xiaomi.com/en/blog/mimo-code-long-horizon
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/3824" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3819">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lbjydzgj_FeKL8Uo4nQwXhdo-eC1O0QaXn39QtSOvPGcHzQpQwF-nj8sf6BN__OvYRUnCE_M0WApwLDFQmj7VSv3npTO1gNpbYZvW8BysSvVyxg4fx5YKbUMlYpXRhD7YA4m93rTGS49aFv6biWLLvEFD5I2oV0EvYuyREyDhOzmmkiWYrc9UFO39lHVNTKmJAw0LevnKGUVyfiRrmIpEWdyTJQ52HWTNbWomLGvWDTHJ784GqsylQprTMl6kWUqpAuTkMtuK6Gcq9RMmLoOLkpTCr8iyFLlpK2Fv5GpKgsGFGXyfvlUznvjiOjaxLzqHWNwzdqC0EX8Pm9FkvGB2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از ChatGPT بپرسید که
یه عدد بین ۱ تا ۱۰۰ انتخاب کن
بهتون به احتمال زیاد میگه 73! علتش رو هم از خودش پرسیدم:
وقتی کسی می‌گوید «یه عدد بین ۱ تا ۱۰۰ انتخاب کن»، من واقعاً عدد تصادفی تولید نمی‌کنم؛ بیشتر یک عدد دلخواه را انتخاب می‌کنم. بعضی عددها مثل ۷۳، ۳۷، ۴۲ یا ۶۹ به خاطر الگوهای آماری و داده‌های آموزشی بیشتر از بقیه به ذهن مدل می‌آیند.
جالب اینجاست که در آزمایش‌ها، وقتی از انسان‌ها می‌خواهند یک عدد «تصادفی» بین ۱ تا ۱۰۰ بگویند، عدد ۳۷ بیش از حد انتظار انتخاب می‌شود. مغز آدم‌ها از اعداد خیلی گرد (مثل ۵۰) فرار می‌کند و به سمت اعدادی می‌رود که «تصادفی‌تر به نظر می‌رسند». من هم تا حدی همین سوگیری را دارم.
پس اگر چند نفر قبلاً همین سؤال را پرسیده باشند، کاملاً ممکن است من دوباره ۷۳ را گفته باشم
امروز توی توییتر اینو دیده بودم و واسم جالب بود علتش</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/MatinSenPaii/3819" target="_blank">📅 15:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3818">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MTdyGzUDxJU9GUvUSb6p--8ejZjs35rV_gvUiAY886sGP8k0YHh6z2_HbC1QvO421jgd-LnqeXV4H67FRUuPk5Av2tNyMoqskehBgCcwJrS0fhJjIeRVVdIgPVOGTJlJkkO-VVOg5AtJNUXteH-JoO1ovH6FtmtJIIe9_sr4R2v-lqILlJY6Zyt7qq81IUfXjr62d27rB3sQ2LWZ72N2qSEQi2qbXiZHn2Vft76CkKXUBIFL2c1h5Ym1EjSHNEakk-wyJqzCi2AhvlFDYBbDyJtWYCCqKPmGS4_kxnR7W30OWELY-f0HDZBgjQJ9S9hoxKWcQslq-55b_INOAlVmFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ابزار باحال آنلاین پیدا کردم: یه عکس می‌دی بهش، بهت گرادینت میده با کلی تنظیمات.
برای وقتایی که دنبال یه بک‌گراند یا پلت رنگی هماهنگ با یه تصویری، عالیه.
تو مرورگر کار می‌کنه و رایگانه
👇
photogradient.com
‎
✍️
Reza</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/3818" target="_blank">📅 14:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3817">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا
ابزاری که امروز معرفی میکنم...
داخل این سایت میتونید تمام ip های مربوط و بنا بر نت خودتون چه برای ورکر و کلودفلر یا شیر و خورشید اسکن کنید
❗️
ویژگی ها:
💡
اسکن راحت و سریع و دقیق
رابطه کاربری خوب برا همه سیستم ها
داشتن ip بیشتر cdn ها
لینک سایت:
✅
https://cdn-scanner-pro.vercel.app/
توسعه دهنده
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/3817" target="_blank">📅 12:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3816">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2658a29175.mp4?token=WU_BTzntpFYjjJQUCL2Q58FWEauYoRRou4h81VGa68hfYtzndSsl6dF8wjgMujAcQPSOH0aIU0ifUfpYrqw32FJl77pZgsyiUksFJ9XqphWvD7KkBaPKGZGaO4bPZb4RaluZ3cHKwf-nKL5kbK3mVtbUVrY67oLsYJrfbpPKX41RESNnS8yX6sYO13EsE7b0DCkUTb_3cRsU85nq94YejDQTEPYYqJF4ktzbk8JrLzpx-Xx2DAl-FYNRm9LQmtzkyXDzLGIV3zoaQH2VmA4Dml9qJq4gmlKWPpG1HzjK5DQYaBx-0QgiuobBSxFAN9p5cG2_7LslbfZ3ygMKtnX7oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2658a29175.mp4?token=WU_BTzntpFYjjJQUCL2Q58FWEauYoRRou4h81VGa68hfYtzndSsl6dF8wjgMujAcQPSOH0aIU0ifUfpYrqw32FJl77pZgsyiUksFJ9XqphWvD7KkBaPKGZGaO4bPZb4RaluZ3cHKwf-nKL5kbK3mVtbUVrY67oLsYJrfbpPKX41RESNnS8yX6sYO13EsE7b0DCkUTb_3cRsU85nq94YejDQTEPYYqJF4ktzbk8JrLzpx-Xx2DAl-FYNRm9LQmtzkyXDzLGIV3zoaQH2VmA4Dml9qJq4gmlKWPpG1HzjK5DQYaBx-0QgiuobBSxFAN9p5cG2_7LslbfZ3ygMKtnX7oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیگما یه اکستنشن کروم منتشر کرده(فعلا برای کاربرای پلن پرو) که با رفتن توی اکثر وبسایت‌ها، می‌تونید با یه کلیک، تمام اون صفحه‌ی وبسایت رو به شکل فایل قابل ادیت فیگما دریافت کنید.
برام جالبه که سر بحث کپی‌رایت و اینا کسی بهش چیزی نگفته هنوز
😁
اما خب گویا هنوز با چنگ و دندون قصد دارن نگه دارن اکوسیستم فیگما رو بعد از اون سقوط سنگین سر Claude Design
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/MatinSenPaii/3816" target="_blank">📅 11:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3815">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏این روزا اسم Agent Harness رو زیاد میشنویم، ولی بیاید ببینیم واقعا چیه و به چه درد میخوره!  همونطور که میدونیم context window مدل‌ها محدوده و اگه به صورت کارآمد ازش استفاده نشه، خیلی سریع پر میشه و مدل مجبوره برای ادامه، یک دور summarization انجام بده.  بعد…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/MatinSenPaii/3815" target="_blank">📅 10:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3814">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mSLhE1Kudpt4xr_vyw_cqi6JanSUBk7T4GPAtDrZhMJ5xZl9ZZ4m0VttsviO-muthbNzjQkLdWOqxDJ-2Ofk9gSxaIX54x-2x-oWDqKVXJZKLWpBU-GsOECxDDkeGDJHV93UF7oX8FpPB3fNzBi4T7-XmdBpBN8KUQwMSA_nSWZlpUSDObC377_0SR2vM7bLAi59XAONP1MfwGWrmx8EKdLiHuXRw0KoCk00j6TU-CacMlLtaPgHEqPdQNksZ7h6Ra8d5l2wHcUSza09VC7jE41-xHvQk_mRJMrXWkUYx482TsuTcYMOZK7-XHkvUIT98yGnE_WbtTk-9Rl1EPet5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏این روزا اسم Agent Harness رو زیاد میشنویم، ولی بیاید ببینیم واقعا چیه و به چه درد میخوره!
همونطور که میدونیم context window مدل‌ها محدوده و اگه به صورت کارآمد ازش استفاده نشه، خیلی سریع پر میشه و مدل مجبوره برای ادامه، یک دور summarization انجام بده.
بعد از چند دور summarize کردن، نهایتا بخشی از دیتای مهم از بین میره و تسک به صورت کامل انجام نمیشه! پس اومدیم یک سری تکنیک پیاده کردیم مثل تقسیم کار بین sub-agentها تا از پر شدن سریع کانتکس اصلی جلوگیری کنیم.
بعد این ایده مطرح شد که بیایم هدف نهایی (PRD) رو تعریف کنیم و اون رو به تعداد زیادی sub-task تقسیم کنیم، بعد مدل رو در یک loop بندازیم که با هر بار اجرا، یک context و یک prompt جدید داشته باشه و بعد از هر iteration چک کنیم که تسک به صورت کامل انجام شده، و در غیر اینصورت چرخه رو دوباره تکرار کنیم!
در واقع به جای اینکه برای اتمام تسک به مدل اعتماد کنیم، ما در یک لایه بالاتر این رو validate میکنیم و اجینتِ تنبل رو harness می‌کنیم :))
✍️
Amir</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/MatinSenPaii/3814" target="_blank">📅 09:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3813">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DxnQgrKsNoVY8xlyCjmldVRWT7mEv8w8I83ErHHFcFvv6sKGtglEw4-lgR0SaPTeFL6Hmx2t4OzkIB8WqKIQIeo6sWh8Qv6jDDuzpEBYOcz5dIYWMa__kRGuhDUVcYt20r8xsehLOU6hVU7V8YTzg3swtOVRZnIcwaq3asgbxAfKMNCE6nAL1DukIYXrE6H0JtaUb-S2I-APLV6UZOtA8hmVVwNiWVVW0hunWd7a8sAWN8XnXO3W5TA3e7RAn9qDW7Qd3OoQmwvhRFg8qe7Co1K2VSQi9kv2Ec-n8G3HprffW6wBdA3NfjX3d5D9UN1PjQjF9N75LGkw3Ko0j_hq7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله شما می‌تونید دامنه و سرور خارج رو از سایت‌های ایرانی هم بخرید، اما چندتا نکته وجود داره:
۱- احراز هویت سایت‌های ایرانی کلا جالب نیست و خب این ریسک رو باید در نظر داشته باشید
۲- توی شرایط قطعی، فروش دامنه و سرور همه‌ی این سایت‌ها میره روی هوا
۳- شاید عجیب باشه شما اگر از سایت‌هایی مثل netlen و با کریپتو خرید کنی دامین+سرور رو، شاید ۸۰۰ هزار تومن(با کارمزد و همه‌چیش) پات بیفته. اما همین دوتا رو از سایت ایرانی بخری زیر 1 تومن نیست</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/MatinSenPaii/3813" target="_blank">📅 07:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3811">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نکات استفاده</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/3811" target="_blank">📅 01:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3809">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DhQIJaVMAiYzbXbpsCYvcWtwEQDThvYXJdNCjBMF40x5mAYevrjGpXppFb3DSpZLWzjRU3WVSbXgdihIa1QRRC-Fp7ngQTiOKmbiLByCrZtxfe9OnNDEc8NmrzFaBl-l7jcDPh1DEvYYzZ_jEgZuvj7I9ovz8ItzZXMbWzx5LeaGL3eDGHJcMA9V9JB4o_43hidhKI0t43rfNcY9d6Xc8Jbd1jufSKJEIMVG9KmwfMLNx8hMpiXwysgC1MskPqqnNdm-_J-2SX4bnNCX-Eaz6g-p9QolRzWm6QNY9uc2CqRxuH-QuLYL89Z0SnbxKRgtGEpDhpt3aLq2xe7zcrKFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran  * دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)  ///  * حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)  * کافی است لینک subscription را وارد…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/MatinSenPaii/3809" target="_blank">📅 00:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3808">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">https://github.com/patterniha/Serverless-for-Iran
* دسترسی مستقیم و بدون واسطه و با حداکثر سرعت به تقریبا تمام سرویس‌ها و وبسایت‌ها (به جز تلگرام)
///
* حتما باید از Xray-core >= 26.6.1 استفاده کنید (v2rayNG >= 2.2.3)
* کافی است لینک subscription را وارد برنامه v2rayN/v2rayNG کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
* نکات استفاده رو حتما مطالعه کنید.</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/MatinSenPaii/3808" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3807">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jLRS0y3IbUHxZ28xo968naWGzeSm-fn5-LpXjLbZwtLA1MatoKqUmxMib1EIPWx2_nFTpdZ36haUbNZaWW0A2HPBJvdk9oSuibVq5uBcFdvb1Hxe-iULPJsCOz6-X5UtXuXVe8EX-OOMtSCRm3pmphtO6mHH_Si82pYIEqIerv11XQB3mudSiuywR4U1obmZxeOZP_h_0puWkdiAwgvdgR0wyBhPuYVKiH9Iv6RMLepcTrJEJ7IljfSgtSYDd-_ZmOdDe7Yc6Tss_M5P9C_4m4rDgcWvKRU0Ksly2iwRjYP3sxEBl_02L6hyO4WQlPW5N1UYzux4q-XEIZxMLaT5uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از http://Netlen.com.tr بخرید، دامنه یه دلاری هم می‌تونید بگیرید و با یه سرور ۳ دلاری و کارمزد، کلا میشه ۴.۵ دلار یعنی کلا ۸۰۰ هزار تومن. دامنه یه ساله هست، سرور یه ماهه. یعنی ماهیانه ۶۰۰ هزار تومن تقریبا. ۵ نفر باشید میشه ماهی ۱۲۰ باز هم خود دانید</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/MatinSenPaii/3807" target="_blank">📅 23:52 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3806">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">درود به همه رفقا
🍷
اگر از پنل bpb و... استفاده میکنید میخواید ip ثابت باشه ولی جز لوکیشن آلمان
🇩🇪
میتونید از ابزار زیر استفاده کنید برای ip های مختلف برای مثال:
میتونید از ip چین استفاده کنید برای دور زدن تبلیغات یا از ip آمریکا برای بیشتر هوش مصنوعی ها خلاصه این ابزار مشابه واسه خود bpb برای ثابت کردن ip هست ولی با لوکیشن بیشتر
❗️
لینک پروژه:
✅
https://smart-ip-scanner.10-354.workers.dev/
توسعه دهنده
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/3806" target="_blank">📅 22:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3805">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‏خطر سرقت اطلاعات و رمزهای عبور؛ مراقب نسخه‌ی جعلی X-VPN باشید  محققان شرکت «سایدرز» (Cyderes) کمپینی فعال را شناسایی کرده‌اند که در آن نسخه‌های جعلی چند برنامه محبوب برای انتشار بدافزار استفاده شده‌اند. یکی از مهم‌ترین نمونه‌ها، نسخه جعلی اپلیکیشن «ایکس وی‌پی‌ان»…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/MatinSenPaii/3805" target="_blank">📅 22:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3804">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R8H1KUYQg2lu_xcLC_Udirnrjek-992szd8Pc-tcpSgyKoElzEXEfJDQLAFRgKlXLc1vpnXoEJE4RBSoX-huzmXnB5GxTaA2qKXjstP7CAC-lDDPxTQ4mM2kyqAS4euyEVTVLSsrYHtM-8XgguI-f0iNvqaOla6CGKFO3kAN7or-KREvnVcrQ8GjRzdiAxXnTyW5K-etEXJAjjloYbbLfTYLk2wGofb6-r_NGVdnH6LCeEGg7hso2Tfnns9JD-ykrTWWHPCEFmO9V_SPFEYoD3XpVJQoF3OODjmUEfCd0HDifZY45dpWRo7_SzYuJoTRLEq38zwfpHa3vEcd4UzQdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
خطر سرقت اطلاعات و رمزهای عبور؛ مراقب نسخه‌ی جعلی X-VPN باشید
محققان شرکت «سایدرز» (Cyderes) کمپینی فعال را شناسایی کرده‌اند که در آن نسخه‌های جعلی چند برنامه محبوب برای انتشار بدافزار استفاده شده‌اند. یکی از مهم‌ترین نمونه‌ها، نسخه جعلی اپلیکیشن «ایکس وی‌پی‌ان» (X-VPN) است که برای نصب بدافزاری به نام STX RAT روی سیستم قربانیان استفاده شده است. این بدافزار می‌تواند رمزهای ذخیره‌شده، نشست‌های فعال و اطلاعات سیستم را سرقت کند و به مهاجم امکان اجرای دستور از راه دور بدهد.
در این حمله سرویس ایکس وی‌پی‌ان هک نشده و کانال‌های رسمی دانلود این برنامه سالم هستند. خطر اصلی متوجه کاربرانی است که نسخه آلوده را از منابع غیررسمی (در این مورد، یک مخزن ناشناس در سرویس Bitbucket) دانلود کرده‌اند. در پاسخ به این تهدید، ایکس وی‌پی‌ان به‌سرعت آپدیت نسخه ۷۷.۵.۳ ویندوز را با کنترل‌های سخت‌گیرانه‌تر منتشر کرد.
➕
نوشدارو پلاس: این هشدار مشخصاً به نسخه ویندوز X-VPN مربوط است، آن هم زمانی که کاربر نسخه جعلی و دست‌کاری‌شده را از منابع غیررسمی دانلود کرده باشد. طبق اعلام X-VPN، نسخه‌های رسمی دریافت‌شده از وب‌سایت X-VPN یا Microsoft Store تحت تأثیر این سناریو نیستند.
▪️
روش زیرکانه هکرها برای اجرای حمله
این کمپین ابتدا با نسخه‌های جعلی برنامه‌هایی مانند «بایننس» (Binance)، «بای‌بیت» (Bybit)، متاتریدر ۵ (MetaTrader 5) و کیف پول اکسودوس (Exodus)، معامله‌گران را هدف قرار داد. آن‌ها حتی به سراغ پلتفرم بازی استیم نیز رفتند و در نهایت تمرکز خود را روی کاربرانی گذاشتند که از ابزار تغییر آی‌پی ایکس وی‌پی‌ان برای حفظ حریم خصوصی بهره می‌برند.
💡
نکته: بد نیست بدانید شرکت Kaspersky (کسپرسکی) پیش‌تر متوجه شده بود که همین بدافزار با نفوذ به سایت CPUID، بیش از ۱۵۰ قربانی را در صنایع و کشورهای مختلف آلوده کرده بود.
بر اساس یافته‌های شرکت سایدرز، مهاجمان در فایل نصبی اپ‌های معتبر یک فایل مخرب به نام CRYPTBASE.dll جاسازی می‌کنند؛ تکنیکی که به آن «بارگذاری جانبی» (DLL Sideloading) می‌گویند.
به دلیل ساختار سیستم‌عامل ویندوز، فرایند نصب برنامه در ظاهر کاملاً عادی پیش می‌رود، اما فایل پنهان‌شده، بدافزار را مستقیماً به حافظه دستگاه تزریق می‌کند تا آنتی‌ویروس‌ها متوجه ردپای آن نشوند. پس از فعال‌سازی، بدافزار می‌تواند ارتباطات خود را در قالب ترافیک عادی و قفل‌گذاری‌شده وب پنهان سازد.
▪️
چطور قربانی برنامه‌های جعلی نشویم؟
دفاع در برابر این نوع حملات بسیار ساده است و نیازی به دانش فنی ندارد:
• دانلود از منابع رسمی: برنامه‌ها را فقط از وب‌سایت اصلی شرکت یا فروشگاه‌های رسمی دانلود کنید. این هشدار برای ما کاربران ایرانی که اغلب ناچار به دانلود از منابع واسطه هستیم، اهمیتی دوچندان دارد.
• تایپ مستقیم آدرس: برای جلوگیری از ورود به سایت‌های مشابه و جعلی، آدرس را مستقیم تایپ کنید و روی تبلیغات کلیک نکنید.
• استفاده از نرم‌افزارهای امنیتی: داشتن یک آنتی‌ویروس قدرتمند و به‌روز در کنار رعایت اصول دانلود امن، لایه محافظتی محکمی ایجاد می‌کند.
اگر گمان می‌کنید نسخه جعلی را نصب کرده‌اید، فرض را بر لو رفتن اطلاعاتتان بگذارید. فوراً رمزهای عبور خود را از یک دستگاه امن تغییر دهید، از حساب‌ها خارج شده و احراز هویت دومرحله‌ای را فعال کنید.
✍️
یونس مرادی(نوشدارو)</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/MatinSenPaii/3804" target="_blank">📅 21:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3803">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bI5SLNzvI1-8jAiFQ5614rRAnLqFb5K_J-tUP3dKAtM8rrnZzDw56nsNa_AlOY0ZasFT5pJtXhOf_T2m51At2c02q0Ik1U_7fn73MvfbJCmLGQiRaLMcM7PxV9WSTxeGTA9wHoiutNoRRU4g6vwGbSPUPljUyHnHysMuHpStmm0aNKGAOJPSU-ua4cI6TYh9JkKc9TnzOdu0NcpBjiKeaJKsHFfXm194usvbG6bFC-42cgInN7mKanR7poDHA5EYvbrLhYJlbBuaMkDvnqsFuZPq91oRmWrcxF8TL--V0YPqe4WAgc_CaERlIzWDBMQ7Efwp6wPoRSucirwRNSqF_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏یه نکته‌ی جالب از کنفرانس WWDC اپل!
توی ویدیو هر بار که کلمه سیری گفته می‌شد فرکانس‌های ۳، ۴، ۵ و ۶ کیلوهرتز صدا رو کات می‌کردن. چرا؟
برای اینکه وقتی دارید ویدیو رو می‌بینید، سیری توی دیوایس‌های اطراف شما بی‌دلیل بیدار نشه.
✍️
Behrad Javed
منبع</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/MatinSenPaii/3803" target="_blank">📅 20:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3802">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اگر از
http://Netlen.com.tr
بخرید، دامنه یه دلاری هم می‌تونید بگیرید و با یه سرور ۳ دلاری و کارمزد، کلا میشه ۴.۵ دلار
یعنی کلا ۸۰۰ هزار تومن. دامنه یه ساله هست، سرور یه ماهه. یعنی ماهیانه ۶۰۰ هزار تومن تقریبا. ۵ نفر باشید میشه ماهی ۱۲۰
باز هم خود دانید</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/MatinSenPaii/3802" target="_blank">📅 20:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3801">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ببینید واقعا درک می‌کنم که ۶ دلار هزینه سرور و دامنه براتون زیاده، اما اگر سه چهار نفر با هم بگیرید بهتون فشار نمیاد. همه هم می‌تونید استفاده کنید
برای من سود و ضرری نداره صرفا می‌خوام بدونید که با نفری ۱۵۰-۲۰۰ میتونید راهش بندازید</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/MatinSenPaii/3801" target="_blank">📅 19:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3800">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-poll">
<h4>📊 میتونم بپرسم چرا هنوز راه ننداختین؟</h4>
<ul>
<li>✓ هزینش زیاد بود واسم</li>
<li>✓ آموزش پیچیده بود واسم</li>
<li>✓ حوصله‌ام نشد و بعد از قطعی مغزم نیاز به استراحت داشت</li>
</ul>
</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/3800" target="_blank">📅 18:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3799">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اینطور که من می‌بینم، قطعی در پیش داریم به زودی</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/MatinSenPaii/3799" target="_blank">📅 17:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3798">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">تمام آموزش‌های مبنی بر اینترنت آزاد که من توی کانال یوتوبم منتشر کردم به علاوه‌ی توضیحات و اینکه توی چه شرایطی به چه دردی می‌خورن. از بالا به پایین، برای شرایط سخت‌تر معرفی می‌شن تا شرایط خاموشی کامل:  1- متد Paqet، ویژه‌ی شرایط الآن(کلودفلر و اینترنت بین‌الملل…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/MatinSenPaii/3798" target="_blank">📅 17:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3797">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اینطور که من می‌بینم، قطعی در پیش داریم به زودی</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/MatinSenPaii/3797" target="_blank">📅 17:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3796">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-poll">
<h4>📊 آیا سرور MasterDNS راه انداختید برای خودتون و خانوادتون؟</h4>
<ul>
<li>✓ آری👍</li>
<li>✓ خیر👎</li>
</ul>
</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/MatinSenPaii/3796" target="_blank">📅 17:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3794">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">هرچی کانفیگ مرده بود با این تنظیمات واسم زنده شد. توضیحاتش رو هم میدم خدمتتون که هر کدوم چیه و Mux رو خاموش بذارید</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/MatinSenPaii/3794" target="_blank">📅 16:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3793">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QjuKoSZ85uDXE8Eecy24mMOEXPpUvW4gZvJmut8ebRaVAAXTQsYEKtw-IOlHQNx2G3waA83YIhbvuUWrDvRbz-5xs4OZFdBGnyXqEoV0rIedUjL4vu7QNFCF5q2xqsFsJMwTM91JjNKeVXYf2UC4OuXihCm5m_lzthnxSrpyyU3AsdKGFxr_3aXZbIeqVoK_q9ikl2t82rDZtZQWRlx0Xpw_QQ-pFpmJNPstdlmt0egYQalk_Dv-D99O_R6f1fvKsLlEVSgxuox8xvYTDRgvHYgJodo29AIEJpq9nfXmTT8wovuJRf2hnyVma94QKgyQ7KdyJLc-ZYGxj9b7HYP3LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی کانفیگ مرده بود با این تنظیمات واسم زنده شد.
توضیحاتش رو هم میدم خدمتتون که هر کدوم چیه
و Mux رو خاموش بذارید</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/MatinSenPaii/3793" target="_blank">📅 15:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3789">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pzFWe3x4EQTJxPguOxTGcSSsl586JiRzX5BF2t_ipziLaqlIMu2xlbVbJmkikiJ4b-jQk8Aox66YaOYIVu7p262eAU5ZgmSNdmu9_penwMBNUoBEB5-ASCGXUqDEc2tSZn24iGEdLO0mZP5zncSsE6jV1WeP5obUqMUUkVNLu3ZHQ0oJ5a9FNFJOS2Ws_a4nQr8oV2H5ZAH7FTTVzHaAjKq6Yhe0dZngBoHbkF7O__UWkzXgCXxbTvdjk8f170U4wZwgqnYFOM5_heUv0lLHXTIrSzjwq6AhOBkE3T5pCY3k8smr_2mdT-V7nygHDL7V8SF8Wfb3hwPnaFgNtYB68Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A_QLa3o3iMbKqRX7lUASkRGcGPD2S3em9l0-w2H-dhYtzLVV8VQst4ETyHSJVQ6BYkhukgvjRf9zOEftuG_7-SpAVH5Q2yeDGd2RhEuePnPnaNvYZgPU5FHjnI4PzCnfZsddhzcu6CvSLqh7Fk5T_DG9iDqRx4walXgdq6xi5yMWA1g9KUDKH-yiNtr16inFlDziql586RX158Qrti7YFKC126SH3gdHpbdt3YzsTZqSJMp8fhFxoWZrL7Gc1kk5HyjMgUQ3HPrw70IyvH6DZCw5snEObvyKgCKP1ZwxYZmntzXaar40k9ZURFOIp1NXX26BbZxOcH88yscLVGKuAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aEV2zmGAaQpIRKf1vutoARrKpKUdf9s0fbDt4nM8t2aRIapxu1TKXaicyqdDRrkoqrK0mG7X0MswDR45bM1AaMggCHFPVn1Zr8ZX_LdwSC3Dh9lZluEWsryLDYuiws-CtlVa22VFGmQjQaGUrc3fMcIKz3tMzuyLnsY36nJsnxjWUAaKFeSGKGFjSeeupdeVmlmihx7ESNpjHMD_AuTW5feCMHjE6FI22CrWKZy46w20UMKK7edrcAH3M-Sa3u5xHGDSKn7aZaWXfBCHgEnBRbz-F21Hf67cu6f-3Ao5ZlBVMVhTeQlgkjQMhfqYB-41UntbuayO9sMLgaYPQV8o_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kGeufQtl-OWpAN1nDCP5Kejo90PG6X2GnlOCMbC2NKa8-XeSar49lkb6ZCue2IZlnf2Gf9iEW9tejxN0QbiOh-LYli5d2lpxyOVh5nVX87qqLS1mKrJByC_m4aAna49K65gFEd_AqRyqJDBBe-NI8C-RHkGESoIINl71Aea-d8oXrMlWuw1072ys8aQv3Nxt_g3ubDaF1E_EyWj_foFzPcXwa__q5ORP8OwGPGH73rTpw67tIhFYICEYzw-L2cFJ8zadoC6AP3PyfewSwZMYXXLoEISScVfuJ3dOGMBNMjGc4nHrggHyu28eeY6gduGavvV9q-BKciSz40TCbsjUlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش فعالسازی Fragment توی اپلیکیشن MahsaNG برای رفع مشکل سرعت آپلود و محدودیت اتصال توی برخی نقاط
روی Auto بذارید فعلا، من در ادامه واستون یه سری تنظیمات پیش‌فرض می‌ذارم که تست کنید روی اینترنتتون
اگر الان کانفیگ واستون با سرعت خوبی وصله، نیازی به فعال کردن Fragment ندارید. چون سرعت کلی رو پایین میاره</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/MatinSenPaii/3789" target="_blank">📅 13:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3788">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ما آخر نفهمیدیم جنگ شد یا نشد</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/MatinSenPaii/3788" target="_blank">📅 09:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3784">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">امیدوارم
WhiteDNS
ستاپ کرده باشید. برای اتصال توی شرایط جنگ
دیگه حوصله‌ی اصرار نیست</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/MatinSenPaii/3784" target="_blank">📅 01:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3782">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اگر خواستید مفهوم فیلترینگ منطقه‌ای رو بفهمید، سوار اتوبوس بشید و از تهران برید خوزستان. به هر شهری می‌رسید آیپی تمیزهاتون از کار میفتن و باید دوباره اسکن کنید. به استان خوزستان که می‌رسید، گوشی تبدیل به یه پاره آجر بی‌مصرف میشه و فقط می‌تونید باهاش زنگ بزنید
😂</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/MatinSenPaii/3782" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3781">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kDFJHcHvQQZGbBQhNm4r5dtRXf5y_r_Sqwf5H7nYWt81_7-fD14RhJ07pP9vFoyzRqBxRPbVcqfC4145K83QmZi9VjHc98lwPPx302kPpBD1WIViwIlmFKkvL8qdR6uNGGc_q1bhXdblzTH5ZPp9X5nVdMsXO91CcBKGgBJwAETXoKaBC_iHIHE2LBjuQ5wii9c07bhEwnOGb75O4FBD8_Ui1fTy-dFeZIHZyUhE-pUxCCRocjQf3FZU5WHQjo6gLxk15vcgcHt_kk-I5RQtsTgAdNsHDFkd1A-wF-bnQymgQewk3T8moC8_wUYLkr_WrSbpN_QbtpzkjipIcOaB3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏وقتشه یه سری حقایق راجب بورسیه MEXT ژاپن بگم.
حالم از این پوسترا مخصوصا راجب بورسیه‌ی ژاپن به هم می‌خوره.
واقعیت:
۱- از چندین هزار متقاضی، سالانه زیر ۵۰ نفر(متغیر) مجموعا از تمام مقاطع برگزیده میشن که اونم کاملا شانسیه.
۲- انتخاب شدن شما تماما به نیاز ژاپن بستگی داره و اصلا هم اعلام نمی‌کنن که ما به فلان رشته نیاز داریم. ممکنه شما تمام شرایط عالی رو داشته باشی با بالاترین نمره، اما «امسال ژاپن به رشته شما نیاز نداشته باشه»(مقطع ارشد و دکتری) و این رو به صورت مبهم فقط بهتون میگن که شما رد شدید! یعنی هیچ دلیلی برای رد شدنتون بهتون نمیدن توی هیچ مقطعی. شخص A با دانش نزدیک به صفر بدون بلد بودن انگلیسی یا ژاپنی قبول میشه چون ژاپن این رشته رو نیاز داره، شخص B بدون توضیح رد میشه با اینکه دانش و علم خیلی بالایی داره یا حتی مدرک زبان ژاپنی داره، چون به رشته‌اش نیاز ندارن. و فقط میگن رد شدی بدون توضیح.
۳- روند غربالگری به شدت غیراستاندارد، و رد شدن توی هر مرحله بدون توضیح هست(سه مرحله داره شامل ارسال مدارک و آزمون کتبی و مصاحبه که هرجا رد شدید، علتی نمیگن)
۴- ثبت نام برخلاف به روز بودن خود کشور ژاپن، به صورت کاملا سنتی و با پست کردن مدرک کاغذی برای سفارت توی یه فرآیند بسیار زمان‌بر و استرس‌زا(نکنه فلان چیز رو یادم رفته باشه) و هزارتا دنگ و فنگ انجام میشه. همه چیز کاغذی. همه‌چیز. یعنی حتی زحمت نمی‌دن به خودشون کد ملی شما رو وارد کنن اطلاعاتتون رو بگیرن. و توی همه‌ی ۱۵-۲۰ تا مدرکی هم که می‌خوان، یه نقطه اگر اشتباه باشه رد می‌شید توی مرحله‌ی اول. که باز هم توضیحی نمی‌دن بهتون که چرا رد شدید. صرفا میگن نقص مدارک
۵- شما ممکنه تمام تلاشتون رو بکنید، همه‌ی مراحل رو قبول بشید، اما در نهایت ژاپن توی اون سال Mext رو برای ایران کنسل کنه!! بله درست شنیدید. پارسال به خاطر جنگ ۱۲ روزه، ژاپن بورسیه‌اش رو برای ایران لغو کرد(
🤣
🤣
🤣
) صرفا چون تایم آزمونش جنگ شد. به تعویق هم ننداخت. لغو کرد. امسال هم همین شد دقیقا و به دلیل وضعیت کشور، لغو کرد. و تمام کسایی که پارسال و امسال هدفشون رو گذاشته بودن Mext، گند خورد به زندگیشون.
خلاصه‌ی کلام اینکه برای بورسیه تمرکزتون رو روی ژاپن به تنهایی نذارید و چندین تا کشور زیر نظرتون باشه</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/MatinSenPaii/3781" target="_blank">📅 00:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3780">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r5dqosT-DiNQdpLXujJAghTLWjeOi5XErFsNMusefeagtHuR8DhgKy987SFypir7CxXx9aiHkVT16WhyShHg7e5k_hgDSuvA-Z-U4UtG4VAFFIOysoheB_kHs7JsmpJKygIrjkp6oVCOG4hpq2JiltuQ7-cWe3o2AYoQh1l-NGb-fLCi5d3onS2nukchTVntV0MoRRzkZElIs5bK3R4olbfPv3SPWEnFcGx34CDMCKoLrFG1PsxNvxD9-CDL6g-7EFlzgM7XcFI-GCWbUYcXUPQ1bmuhcTJIHzvQmUxJty0iWLBGdLWCQhSCP5Go6zTq2zLe4U_esa23cTQMHA8JJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
پروژه‌ی FreeLLMAPI — یه پروکسی OpenAI-compatible فوق‌العاده‌ست که ۱۶ تا از بهترین ارائه‌دهنده‌های LLM(مدل‌های زبانی بزرگ. همون هوش مصنوعی خودمون) رایگان رو روی هم جمع کرده!
تقریباً ۱٫۷ میلیارد توکن توی هر ماه ظرفیت inference (از Google Gemini، Groq، Mistral، Cerebras، OpenRouter، GitHub Models، Cloudflare، NVIDIA، HuggingFace و ... + هر endpoint سفارشی مثل Ollama، vLLM، LM Studio و غیره) می‌ده.
ویژگی‌های اصلی:
🔤
یه endpoint واحد (/v1/chat/completions) برای همه‌چی
🔤
روتینگ هوشمند + failover خودکار (اگر یه کلید به rate limit خورد، سریع میره سراغ بعدی)
🔤
مدیریت دقیق quota هر api key تا زیر حد استفاده‌ی رایگان بمونیم
🔤
کلیدها به صورت رمزنگاری‌شده ذخیره میشن
🔤
داشبورد باحال برای مدیریت api key
🔤
نصب خیلی راحت با Docker
در واقع همه free tierهای پراکنده رو تبدیل کرده به یه LLM قدرتمند و همیشه در دسترس، بدون اینکه مجبور بشی با کلی SDK و rate limit جداگانه کلنجار بری.
بهترین‌ها برای کدنویسی (بر اساس این پروژه و لیست هوش مصنوعی‌ها) عمدتاً DeepSeek V4 Pro، Qwen3-Coder سری (مخصوصاً Qwen3-Coder Next و 480B) و Codestral/Devstral هستن.
⚡️
لینک پروژه:
https://github.com/tashfeenahmed/freellmapi
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/MatinSenPaii/3780" target="_blank">📅 23:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3779">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">من خودم با Hiddify راحتترم برای ساب، از اون استفاده میکنم کلا(با نت H+ الان دارم این پست رو می‌ذارم با همین ساب) اگر پینگ نداد، توی تنظیمات Tls Fragment رو روشن کنید</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/3779" target="_blank">📅 22:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3777">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/m7cZV1sESXtFrQwPBQC_g-r-1kySpHRRQud2vhSO8IQdawypJoDiP2iRs1j2uqp60aluGqOxeHgONPMAGx0PsIqqEjnyesI0-_tSzrnFK0WWTmGq6TL8kEXdx3Z6YrAbIhP3YsakMJoLOD8xQXg36-CnePFuAhSSiDDe1HO8UggyMFIAhvsNsSDTQ3ATB-eQ15V0WS9Y_WW768JHO7Kwhyfg7zvtifMsoL3LMNwJQ4Z_hFUJL5Ffqu7BSUeTKXeVMW_E8swD7HH14oTHdJQBUk0RVBx__VfHI0EfL2EwtzMiAMpUmxOdcSvKIDyj7Po_D8Wm8RKfEJjndgCYhjBe9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qco3h-RopTN2Yc8GyuOwph8SjwYpcFzVRaLwxnOBxxHlPCZKP9A8bX5zB2N_Ef9MwGxr0LH-Dv4Qi7WCIfN2tWMDac77dUOTR2dpoPnkaLXpSZng2lEZucRRTPEFfeA0jy_g-cEFsij24GnKklt4umjPaXXpaGIgNF3jses8JKdjdhobk1LiGwDuSQQ4z_z79R0YQUP8xQAN6Knld9xoZKS1i4pLRkcM-i2D4spbBPS68Gi0gnsSGTeCBK-QBZyKUBuq8KIAxfDR3p4Q3-bnp0YM2dE3eql-bXPnr91jyqYCS-7yDkSSVinsVXy1Sy3kJFo5cH9u8kfhfbgXAcHiHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بچه‌های WhiteDNS دارن رو یه چیزی کار می‌کنن که شاهکاره ایده‌اش
(عاشق UI اولیه‌ی اپلیکیشنم
😂
)</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/MatinSenPaii/3777" target="_blank">📅 21:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3776">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/khOHspygc1id7SNhhcSH7-hGXCnKNQ5-gRDe7kMIkc9aw-B6W4mndHDLliXMRaufShMQto3nW6u8Eueyc3Hl51K9YgUczOlcieHSfyogqxoJT_H_Stxb9WCJLUcbEWkpwTat5ens1G1_b_ngHxLXglv80hO59XmENe_3UYscerA_2FZPoFXghLwXVDa_p1XwJtUV0ryViN4uJgzGypn-lNuqMffv3jVyZmfN4nfqgCUA6U4uoAPEOqy8bh3q-uwxU22dQ01mLf2dpwAuo-d1Po9S4mE_R8NbsX8XOU6aXCyXMBATngDjFHAkhylaYBiePjR8FZYspYqkPqUrruSYKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک هنوز جوهر Opus 4.8 خشک نشده بود، مدل جدید Fable 5 رو به عنوان قوی‌ترین مدل عمومی Claude معرفی کرد!  این مدل توی برنامه‌نویسی، تحقیق و همینطور تحلیل تصویر عالی‌ترینه؛ هرچقدر کارمون پیچیده‌تر بشه، برتریش نسبت به مدل‌های دیگه بیشتر و بیشتر مشخص می‌شه.…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/MatinSenPaii/3776" target="_blank">📅 19:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3775">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79adfc024d.mp4?token=EdODTE2ooI_28vcSPi5ThRxeQYj2Qj3ucDwkwMZM4wbE7oDzV0Pp4Y5J67-13bLX9CGfaSFQ5EL4iiuxir6JFdQurkakFsMD5iA99GfiKlQKpI_i9negjH0HEwePo3Ys_VWW_7_fBn8RXtL4BOSuy7rQrydlVXWpb93a5k4bNLPZvqx7hgYFtYx_F3YkQWfxRljeDBg3eNX00nEQNzDQijmTHJD0O_fCRud1n_ii2SRnrEBdpbWPxPfxqH1Jro4dez_cdetBMDHhbYJ5WS3TvhuuF7NVsoIHCrMZ4OSrDW0XdLmHJftV4q1JyluKwhFt5mtY5Jy8m8MZ_vypm-pgCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79adfc024d.mp4?token=EdODTE2ooI_28vcSPi5ThRxeQYj2Qj3ucDwkwMZM4wbE7oDzV0Pp4Y5J67-13bLX9CGfaSFQ5EL4iiuxir6JFdQurkakFsMD5iA99GfiKlQKpI_i9negjH0HEwePo3Ys_VWW_7_fBn8RXtL4BOSuy7rQrydlVXWpb93a5k4bNLPZvqx7hgYFtYx_F3YkQWfxRljeDBg3eNX00nEQNzDQijmTHJD0O_fCRud1n_ii2SRnrEBdpbWPxPfxqH1Jro4dez_cdetBMDHhbYJ5WS3TvhuuF7NVsoIHCrMZ4OSrDW0XdLmHJftV4q1JyluKwhFt5mtY5Jy8m8MZ_vypm-pgCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آنتروپیک هنوز جوهر Opus 4.8 خشک نشده بود، مدل جدید Fable 5 رو به عنوان قوی‌ترین مدل عمومی Claude معرفی کرد!
این مدل توی برنامه‌نویسی، تحقیق و همینطور تحلیل تصویر عالی‌ترینه؛ هرچقدر کارمون پیچیده‌تر بشه، برتریش نسبت به مدل‌های دیگه بیشتر و بیشتر مشخص می‌شه.
همینطور به دلیل توانایی‌های بالاش، برای موضوعات حساس مثل امنیت سایبری(هک و امنیت)، زیست‌شناسی(شاید تولید سلاح‌های زیستی)، شیمی(شاید تولید مواد مخدر
😂
) و مطالب مشابه، از مدل ضعیف‌تر Opus 4.8 استفاده می‌شه.
همینطور همزمان مدل Mythos 5 هم معرفی شده که یه نسخه از Fable 5 با محدودیت‌های امنیتی کمتره.
فعلاً Mythos 5 فقط در اختیار تیم‌های امنیت سایبری خود آمریکا و زیرساخت‌های حیاتیش هست و ممکنه بعداً برای پژوهش‌های پزشکی و امنیتی به افراد مورد اعتماد بیشتری داده بشه. طبق جدول منتشر شده، Mythos 5 و Fable 5 در بنچمارک‌ها امتیاز بالاتری نسبت به GPT 5.5 و Gemini 3.1 Pro و خود Claude Opus 4.8 کسب کردن</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/MatinSenPaii/3775" target="_blank">📅 18:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3774">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jLTfEUk_tdfU8TCoEfItpx_l3kqgn3sDL_kN-Tgtx1YH6OxnSDq3DPsK8dgQjEalFsXHfH6gZ3jrMcj-sEJ8CGeuxUatOVXgV_qXV9M-IwRKr2M7nSNUzna_JZvgsm465RcE5cFov8JubJ0fxo1sl3olb8OsWtvFYKxvD4fip1am2op6gSblJ6Jp-_cb25CtCcy9DfA-3UoP-Kd-6QtqQpRWlDZrDh83BhS270JwSrRcS9mlG1IJW1QGsMeq2zO84v6K_AeH9jtn9G4y6WI5_JWTSqoORiiulcyEEcfL4aoSNyllkTAkw9NAnHaf5ighUQTb1bh5DTBZlB81BjFEhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من خودم با Hiddify راحتترم برای ساب، از اون استفاده میکنم کلا(با نت H+ الان دارم این پست رو می‌ذارم با همین ساب) اگر پینگ نداد، توی تنظیمات Tls Fragment رو روشن کنید</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/MatinSenPaii/3774" target="_blank">📅 16:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3773">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E2dAqwEHqybh4i8ggzrn-F7gy-8mvSDYYfoEKpd_Rt9c9Tm-J2Lbglj8BTNbPoaEuhZWTD4TvbFzziX5J-XPCJW7c1d6SDi3bH2ZEctgACNAwWsXGnI9mh5QJd1J_MHPNh10JgEJYbBYEML2M-F_bx0EfnU6FeLgRcBF5-LDJ0WPTE-kNmeXtHyek_idwsNeWxQXZ5NU2QfafPyZS2u_qHu0p-RvmBWAkhRV_gzyJ_fLYwdj7EUIXVZVZ_w1fVVNUNfNRiJLYi2mRFMOh41Zat8oVZNCeiKdvKPvw8DPgR9sYVTbFdnGgfmMmiXv0w3RAum4XqBQninaSlsbPK0VLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ساب‌ها رو می‌تونید توی هر کلاینت V2rayای که دارید وارد کنید و استفاده کنید ازشون</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/MatinSenPaii/3773" target="_blank">📅 14:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3772">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ساب لینک مخصوص تمامی اپراتور ها نامحدود
❤️
✔️
اپدیت کنین ساب رو اگه نتونستین اضافه کنین ساب رو کافیه لینکو توی مرورگر بزنید بالا میاد و کانفیگا رو کپی کنید
⚡️
لینک ساب دائمی کانفیگ ها: https://raw.githubusercontent.com/masir-sefid/Sub/main/@Masir_Sefid.txt…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/MatinSenPaii/3772" target="_blank">📅 13:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3771">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">ساب لینک
مخصوص تمامی اپراتور ها نامحدود
❤️
✔️
اپدیت کنین ساب رو اگه نتونستین اضافه کنین ساب رو کافیه لینکو توی مرورگر بزنید بالا میاد و کانفیگا رو کپی کنید
⚡️
لینک ساب دائمی کانفیگ ها
:
https://raw.githubusercontent.com/masir-sefid/Sub/main/@Masir_Sefid.txt
⚡️
توی تمامی کلاینت ها به جز npv میتونین استفاده کنین پینگ نگیرین وصله
🟢
نحوه ی اضافه کردن ساب لینک با اپدیت خودکار
⭐️
پروکسی 1
⭐️
دونیت برای کمک به ادامه دادن این مسیر
❤️
🪐
Channel |
@Masir_Sefid
| کانال
🪐</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/MatinSenPaii/3771" target="_blank">📅 13:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3770">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⏯️
ویدیو آموزش استفاده از WhiteDNS Wizard و نصب و راه‌اندازی کامل و اتوماتیک پنل ثنایی
https://youtu.be/rxxlNXLcaqU</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/3770" target="_blank">📅 11:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3769">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🛡️𝔽𝕣𝕖𝕖 𝕋𝕣𝕚𝕒𝕝 𝕂𝕖𝕪𝕤🗝️(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c2b536338.mp4?token=jFuJgqw-mfsLRmB1e0ussRugFyyiRMaN8N1eJUGGxb3r93I8-HbF5HkZDK1wIryMSeDmy5xpSpgjO76siD8-AGpC7GQN9EhNx2Gzs17v00EdArI9gzcpZa4JSW0UyqbREQNLqQSeUrWTfGut2Qf0pWSpFbZSg1IEQEYYQ_dIDmCTOKdwLYYEFLlP2j80WIJS6cfA8FCH8sV2TdsLEdZSE0894fxfRwFWFWXEAI4GODyFp6akkpAaEvCAf3-AKB6yj4F2v_p_uza6fe7T8Gs1k6YoO4l434l3pL6MW5dsh6UcQAlu47QPuozbrtT5iFzrh0HECkRu2iEl-EQELsI52Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c2b536338.mp4?token=jFuJgqw-mfsLRmB1e0ussRugFyyiRMaN8N1eJUGGxb3r93I8-HbF5HkZDK1wIryMSeDmy5xpSpgjO76siD8-AGpC7GQN9EhNx2Gzs17v00EdArI9gzcpZa4JSW0UyqbREQNLqQSeUrWTfGut2Qf0pWSpFbZSg1IEQEYYQ_dIDmCTOKdwLYYEFLlP2j80WIJS6cfA8FCH8sV2TdsLEdZSE0894fxfRwFWFWXEAI4GODyFp6akkpAaEvCAf3-AKB6yj4F2v_p_uza6fe7T8Gs1k6YoO4l434l3pL6MW5dsh6UcQAlu47QPuozbrtT5iFzrh0HECkRu2iEl-EQELsI52Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روش وارد کردن کلید avast secureline
هر کلید برای صد کاربر هستش
اگه به لوکیشن گیر داد داخل نرفت یبار کلیر کش کنید دوباره کلید رو وارد کنید یا به نت دیگه و vpn دیگه</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/MatinSenPaii/3769" target="_blank">📅 01:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3768">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🛡️𝔽𝕣𝕖𝕖 𝕋𝕣𝕚𝕒𝕝 𝕂𝕖𝕪𝕤🗝️(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b056aeeb9d.mp4?token=o7O5MaEbmAHcP-_VEVeNLSJVg2fuf-e6a0Qf791APoxEjWIPXf4eDodv_qafyd4_LxUa4x8t_8A7tr7Rk-6IKV9Ai9TW0IuJ25Z-8WRw4yM7HNnCuZlMf5G42JSa8JtAs2qAk55q6zJgshzEnZs5V5R1uZzdcAaFuqfa6u0CI3u0Z5R7mHmlVZJSP0BJYRpeho2QziSngetVuKt2HL2Jfgc7sHxx71O79rRsVuzb2sGuJH6WeQYkBTzUa-GY19HJSwmKeuVtvW72Yt_w0YFdM5NiB3M2ySSavyFxv9zsI4CWRd0UIhOVtQGObaEUc0xpwl78XJzym5llhRGH4hLrd76ZtGYqNssKpQLnko25XS3pwWiRHW6zCCycrdLMn3MufSHuc_evgxVNVvPX3vjqqHmsdqF1oMXOLzwYaN_2Tzo6HkP3mS7la3xrGzButDsR5PwuPfL8lZthPysWgIkcs1TRNyx3mGOBGFVDsU_vrBYbaeSnLshyImWpKZwwxab5uMryEg7djkKkjtU1pOwqjQrLcB5b2aJ3Pf8SU4kmaQYZ7q3XG5JE7fCUpEEa_B06vSG3iuvx6uzTh-RNhCNURf-aoB8kQ8nk9I-wcuYqpwC6mlEMmzVOguMs3egZskrAE73xFmzKlRqntIJQhZD9cAynbNZs6RFWAtWA0oFlFeM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b056aeeb9d.mp4?token=o7O5MaEbmAHcP-_VEVeNLSJVg2fuf-e6a0Qf791APoxEjWIPXf4eDodv_qafyd4_LxUa4x8t_8A7tr7Rk-6IKV9Ai9TW0IuJ25Z-8WRw4yM7HNnCuZlMf5G42JSa8JtAs2qAk55q6zJgshzEnZs5V5R1uZzdcAaFuqfa6u0CI3u0Z5R7mHmlVZJSP0BJYRpeho2QziSngetVuKt2HL2Jfgc7sHxx71O79rRsVuzb2sGuJH6WeQYkBTzUa-GY19HJSwmKeuVtvW72Yt_w0YFdM5NiB3M2ySSavyFxv9zsI4CWRd0UIhOVtQGObaEUc0xpwl78XJzym5llhRGH4hLrd76ZtGYqNssKpQLnko25XS3pwWiRHW6zCCycrdLMn3MufSHuc_evgxVNVvPX3vjqqHmsdqF1oMXOLzwYaN_2Tzo6HkP3mS7la3xrGzButDsR5PwuPfL8lZthPysWgIkcs1TRNyx3mGOBGFVDsU_vrBYbaeSnLshyImWpKZwwxab5uMryEg7djkKkjtU1pOwqjQrLcB5b2aJ3Pf8SU4kmaQYZ7q3XG5JE7fCUpEEa_B06vSG3iuvx6uzTh-RNhCNURf-aoB8kQ8nk9I-wcuYqpwC6mlEMmzVOguMs3egZskrAE73xFmzKlRqntIJQhZD9cAynbNZs6RFWAtWA0oFlFeM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Avast
Secureline
آموزش دریافت لایسنس‌کی یکماهه
لینک سایت
https://businesshub.avast.com/dashboard
فیک میل
https://temp-mail.org/en/
https://internxt.com/temporary-email
https://mail.tm/en/
https://temp-mail.io/en
لینک دانلود
•
Android
•
iOS
برای کانکت شدن از ی vpn کمکی حتما استفاده کنید
از پروتکل mimic و openvpn استفاده کنید
ÐΛɌ₭ᑎΞ𐒡𐒡</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/MatinSenPaii/3768" target="_blank">📅 01:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3767">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PaP0hbhGSYCdtNDWUOQY2RyetxtkNfWmqzICiyEfK_nCpZPpeoHOAM5K44pxvIFyh089Xmkwmc-W_kYZmP4W5MiPRlno2hGdMRht_WZpcl1I3ZxigK0Gc78JwMK3XjISAS7HKglByHnUkP_bK_E-lRiclmLrIrx5CfHnvoSmWPJv83tkIP103_xGN1dWJuV3wCg5efg39PwrOU9s9vlgDzaGNkEQQVcSeZIkMPXUMNaH8m-EAoGPuX3B4tUXRyn16kj7DNTSELUjEAK8iO4IxB4Iw27V5F-dnwa6fbKnv4f-gvoCpGxKB8oicaTyla36BsVT_Uz0MTahXofyRRaLRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد وایب کده. اسم دیگه روش گذاشتن قرار نیست ماهیتش رو عوض کنه
و نه خوبه نه بد. بحثش به شدت مفصله</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/MatinSenPaii/3767" target="_blank">📅 22:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3766">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">برای WhiteDNS از
http://Netlen.com.tr
هم میتونید سرور بگیرید. فقط قبلا یه تایمی درگاه ترونش خراب بود نمیدونم درست شده یا نه
اینجا میتونید با شماره ایرانتون هم رجیستر کنید</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/MatinSenPaii/3766" target="_blank">📅 17:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3765">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K2qwcxTo4jcEyBvsOaHxTHqEymU2tWeCAQ883IXbrcr3HL8u95tP65Z6PlisTJ2A6yHs5WiW95jBtlWPrss8hGTlvYrAOIvv6tUOAb7zgHxfA9bGgMj1H89h0barRfEdTRkATA4UEkG404XShOnrxC0hx_C1TBFiuSc-KNedNUHgT5lb9TUdsh3daGw30O21xnCmFH3pi0KLjoT66lA5VTiZH4XTm_oMk_OFOgzY7tNPhzljTNlxCA3yTeNPRURXoRaP7swf0yZO4ncYzDXZQ8N1z0M-zXAfFjKBfpQePS8rNJUs_4r9WdYcrKwtShhGPejU4rn_JzWzvkcWlMcp2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام بچه‌ها:
متین جان لطفا تو کانال اعلام کن که از namecheap دامنه نگیرن. من گرفتم و بعد دو روز به علت تحریمات اکانتمو بست.</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/MatinSenPaii/3765" target="_blank">📅 13:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3764">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اگر توی ساخت پنل bpb یا edge یا nova یا نهان ارور 1101 گرفتید، کلا از اون اکانت Log out کنید و با یه اکانت جدید شروع کنید</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/MatinSenPaii/3764" target="_blank">📅 10:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3763">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اگر توی ساخت پنل bpb یا edge یا nova یا نهان ارور 1101 گرفتید، کلا از اون اکانت Log out کنید و با یه اکانت جدید شروع کنید</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/MatinSenPaii/3763" target="_blank">📅 09:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3762">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دوستان اگر خواستید از سایت yotta سرور و دامنه بگیرید، می‌تونید آدرس فیک از
fakexy.com
بگیرید و استفاده کنید</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/MatinSenPaii/3762" target="_blank">📅 23:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3761">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">Valid-08-June-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/MatinSenPaii/3761" target="_blank">📅 16:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3760">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/67cf13d855.webm?token=Sq_jwnJZF_rvFR606dMS_bZngG9AFS292d96vKTtzu6jGXsr33X_3DdB28jHPd-8aHt73MaR11YcoHqAhS3k_QVh4k9oVuZ4L4jF3gMh34oTfifvaFC0JbH5TBpADCQ0SGgNoF9sKUDVT0d838_RH-feplIPTmTp4XnUDFWIi23mzBkQQ4l11nmCy0-CLwbhFFA0-xMBwnBB_AWnuPhNSKTe_Msd5U0ojK5B7SdsF1D5drJXwEfRAdhHeYPmBZZiEGlcM4MzpAZ0Kikuz12UtjgTZVEQqU9_OiAVxBP5sm3FPyMD5VBYc48LYG4smRGRYIeORtXpu4wFVEKbliVN1w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/67cf13d855.webm?token=Sq_jwnJZF_rvFR606dMS_bZngG9AFS292d96vKTtzu6jGXsr33X_3DdB28jHPd-8aHt73MaR11YcoHqAhS3k_QVh4k9oVuZ4L4jF3gMh34oTfifvaFC0JbH5TBpADCQ0SGgNoF9sKUDVT0d838_RH-feplIPTmTp4XnUDFWIi23mzBkQQ4l11nmCy0-CLwbhFFA0-xMBwnBB_AWnuPhNSKTe_Msd5U0ojK5B7SdsF1D5drJXwEfRAdhHeYPmBZZiEGlcM4MzpAZ0Kikuz12UtjgTZVEQqU9_OiAVxBP5sm3FPyMD5VBYc48LYG4smRGRYIeORtXpu4wFVEKbliVN1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/MatinSenPaii/3760" target="_blank">📅 15:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3759">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Valid-08-June-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">9.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3759" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اینها 688 تا ریزالوری هستن که Valid بودن توی دوره‌ی قطعی برای من، از اون 5800 تا ریزالور ویدئوی WhiteDNS</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/MatinSenPaii/3759" target="_blank">📅 15:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3758">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-poll">
<h4>📊 دوستانی که سرور دارید، دیتاسنترای ایرانتون...</h4>
<ul>
<li>✓ اصلا وصل نشده بود هنوز اینترنتش</li>
<li>✓ وصل شده بود، الان قطع شد</li>
<li>✓ وصل شده بود و هنوز وصله</li>
<li>✓ سرور ندارم، دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/MatinSenPaii/3758" target="_blank">📅 13:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3757">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترجیحا هیچ VPNای نخرید دوستان. هیچ تضمینی نیست که اگر اینترنت قطع بشه هم اونا وصل بمونن یا نه. مثل اوایل جنگ که خیلیا اسکم شدن
همون هزینه رو بذارید whitedns راه بندازید</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/MatinSenPaii/3757" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3756">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هر پنج دقیقه میرم یه پینگ میگیرم ببینم وضعیت چیه
روانیمون کردن</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/MatinSenPaii/3756" target="_blank">📅 12:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3755">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اینکه هنوز اینترنت قطع نشده جای تعجب داره به خدا</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/MatinSenPaii/3755" target="_blank">📅 12:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3754">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مجددا تأکید می‌کنم که سرورهای عمومی سرعت به شدت پایینی دارن مخصوصا توی محدودیت‌های شدید و بسته شدن ریزالورها. تمام تلاش رو بذارید روی راه‌اندازی
سرور+دامنه شخصی</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/MatinSenPaii/3754" target="_blank">📅 11:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3753">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سرورهای عمومی MasterDns(با کلاینت WhiteDNS):
1-
https://t.me/Masir_Sefid/612</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/MatinSenPaii/3753" target="_blank">📅 09:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3752">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AqJWPzGGPtGUMohZydnijR0vTJLqFOyrBoBXvZXmcSTrv8nuph68O85XAkr01J7C8RFUPE99vWDWm6NSeI1hD0Ftd6DbsuefaEKBxO-LdHOWynXX6TVi5SMJ3BodjZSch-uf1a9CicbK8j_bZ3Stk2AqoK3HcnV9cApcmRrjGwCTK_uZ6EaZavSSjCIp51MoxrZww03qEsecA2sSUWrX1gA6GvGK1DIN1Tx9bDKfVt5kTeDJznuUcfe5eRLwTkw8wTXc-LFcJKQfxWipoauwMaOo0wliZxLWYacRuhqC666MuY1zsROOjC_ezsuqFtyAbgTjFtUAGUKb8PDGmMUVUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب همونی شد که فکر می‌کردیم. جنگی در کار نیست انگار تا بعد از جام جهانی. فعلا اینترنت داریم</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/MatinSenPaii/3752" target="_blank">📅 08:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3751">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خب همونی شد که فکر می‌کردیم. جنگی در کار نیست انگار تا بعد از جام جهانی. فعلا اینترنت داریم</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/MatinSenPaii/3751" target="_blank">📅 08:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3750">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دوستان دامین سالم این شکلیه. نه اینکه از ۵۸۰۰ تا بهتون ۴ تا valid بده</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/MatinSenPaii/3750" target="_blank">📅 00:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3749">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uhrG6xGoA87mH0K7_sj6kAqdP8oHaOYFCR0k2PfQ7b-i9KqvWi43c5z1wVGJKHuPbtWE_zigGwCaSgnb8xKFFKrrbgg9UbcphirSWUDXDOoLlYD7s8zkz7gI89L-y11eYAC54iRO1ZpvrjE9dKFJG6p3K9r8SLohhsHpfREkloZbo7SmKvd8FvlQNIfahjZVE4sMbwSZRQy6EhlI21aaS9597dOSH58kRQWm0SAAiJ7VXe3q4jJd11oBcADQGV-YV0Ar_hBczE7s-HNLrvC1j8xWJ7vZE2JDCob0B3RvFPewKkNq17GLZhOZOsP7Vp43Wnp1xfKRapvpfxvtJKQpnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان دامین سالم این شکلیه. نه اینکه از ۵۸۰۰ تا بهتون ۴ تا valid بده</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/MatinSenPaii/3749" target="_blank">📅 00:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3748">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-poll">
<h4>📊 سرعت اینترنتتون؟</h4>
<ul>
<li>✓ تفاوتی نکرده</li>
<li>✓ یه کم کندی حس میکنم</li>
<li>✓ تمام کانفیگا از کار افتاده و نمیتونم به هیچی وصل بشم</li>
</ul>
</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/MatinSenPaii/3748" target="_blank">📅 23:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3746">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">Matin SenPai
pinned «
دوستان با این اوصاف حمله‌ی پیش‌دستانه WhiteDNS+Master راه بندازید که هر لحظه ممکنه اینترنت رو قطع کنن متأسفانه. توی ویدئو آموزش خرید سرور و دامنه و راه‌اندازی و تانل کردن کل سیستم و راه‌اندازی روی گوشی و سیستم هست کامل: https://youtu.be/6Pm7kNQb3mo سر هر تحرک…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3746" target="_blank">📅 23:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3745">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/MatinSenPaii/3745" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3744">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">تا حالا حمله‌ی پیش‌دستانه تجربه نکردیم. اگر منطقی باشه، اینترنت به جای قطع شدن باید قوی‌تر بشه</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/MatinSenPaii/3744" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3743">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دوستان با این اوصاف حمله‌ی پیش‌دستانه WhiteDNS+Master راه بندازید که هر لحظه ممکنه اینترنت رو قطع کنن متأسفانه.
توی ویدئو آموزش خرید سرور و دامنه و راه‌اندازی و تانل کردن کل سیستم و راه‌اندازی روی گوشی و سیستم هست کامل:
https://youtu.be/6Pm7kNQb3mo
سر هر تحرک نظامی و موشک مجبورم این حرفو بزنم چون احتمالش هست واقعا هر لحظه</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/MatinSenPaii/3743" target="_blank">📅 23:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3742">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">تغییرات WhiteDNS Wizard v1.1.0
- خطای ACME و DNS بهتر تشخیص داده می‌شود.
- قبل از ساخت SSL، برنامه چک می‌کند دامنه واقعا روی Cloudflare فعال و درست تنظیم شده باشد.
- پیام‌های خطا واضح‌تر شده‌اند و کاربر بهتر می‌فهمد مشکل از توکن، دامنه یا DNS است.
- آموزش دسترسی‌های Cloudflare در README کامل‌تر شده.
- Reality XHTTP با Reality TCP Vision جایگزین شد.
- Reality حالا از
xtls-rprx-vision
استفاده می‌کند.
- انتخاب SNI برای Reality امن‌تر و پایدارتر شده.
- مسیر نصب روی سرور از
/opt
به
/var/lib/whitedns
منتقل شد تا روی VPSهای بیشتری بدون مشکل کار کند.
- مشکل ساخت فایل Docker Compose روی بعضی سرورها رفع شد.
- نصب Docker Compose Plugin روی سیستم‌عامل‌های مختلف بهتر شده.
- بیلدهای GitHub Release سریع‌تر شده‌اند و به صورت موازی ساخته می‌شوند.
- چند مشکل مربوط به مسیر فایل‌ها، ریستور، تست‌ها و آپلود فایل‌ها رفع شد.
https://github.com/iampedii/WhiteDNS-Wizard/releases/tag/v1.1.0</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/MatinSenPaii/3742" target="_blank">📅 21:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3741">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یه جمله‌ی مشترک که از افرادی که پایتون اولین زبان برنامه‌نویسیشون بوده و بعد از اون رفتن سراغ یه زبان دیگه(علی‌الحصوص
زبان‌های کامپایلری
) زیاد شنیدم، این بوده که تازه با یاد گرفتن یه زبان جدید فهمیدن برنامه‌نویسی چیه. و درک و قدرت حل مسئله‌شون اونجا بوده که رشد کرده. علتش برام جالبه</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/MatinSenPaii/3741" target="_blank">📅 20:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3740">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">این پنل هم دیدم بچه‌ها زیاد باهاش ساخته بودن vpn روی کلودفلر. یه تست بکنید https://github.com/IRNova/Nova-Proxy</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/MatinSenPaii/3740" target="_blank">📅 17:43 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
