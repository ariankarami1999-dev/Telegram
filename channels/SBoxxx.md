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
<img src="https://cdn4.telesco.pe/file/LyLoFLyYXGeMF1-U8Rc7d3TONzdHlDAb_OXp7RWjoBOWu16lwyqF7RpJGsu154LhCmF3zrOPD5ipwKIBtgmzUILn1F10Z3uK6e1XFSPX-WoY691eJuRQSephI2_uEEcbMq_1Fu-qlspNxzpTVfRRjw4S7zN70bk8Ft2BAZBlAd_XhAjUUYVa6kWZrx6g6sHRJQpDEL_zle7qdhbehh4MVVV3Iup9m-EDZjwjKr6Jebz_EyVYDmH9D3iM2OyH2OCLtNfi32rWImI7XKsk-3IJn2lfR-BigLwNtsi5F8X-Ca-QzZs9o9cCsxb2uNuAeca9GqpU5cJ3KENa-gdgQ6lyOg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 19:28:13</div>
<hr>

<div class="tg-post" id="msg-17984">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">● این میم در مورد مذاکرات ایران و آمریکا توسط خیلی بازنشر شده.  @Milita_Camp</div>
<div class="tg-footer">👁️ 689 · <a href="https://t.me/SBoxxx/17984" target="_blank">📅 19:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17982">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نبرد دریای سرخ: اسرائیل نمایندگی دیپلماتیک خود را در سومالیلند افتتاح کرد  اسرائیل چند ماه پس از به رسمیت شناختن استقلال سومالیلند، یک سفیر برای این منطقه منصوب کرد. دیپلمات مایکل لوتِم پیش از این سفیر اسرائیل در کنیا، آذربایجان و قزاقستان بود.  در ماه ژانویه،…</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SBoxxx/17982" target="_blank">📅 18:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17981">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7wmvzZ4WRUS9J3bsPRiTuRHoEFeb2CtpK4XtnyfQSYHu5GY0Ng4h4gT16ZWdC1HrfBLds5v1BkL6Jh6-K-CBcp7XoBPt8hk3jiVcfzKtnb-27PDthobXG2C5eG1hRk7w2F2Lt_fjObx2Y3Ma94iOqg2Tc4oT7yBFOL2H_hVbqsLnXPgBvNi69e3naCWF4RUsXXrj0RO5UNfhe3N28koIXgjvcfofOFmDQFd0krPHaJtSfjdugojPUEFW2Ztn5Gf9mZH2yCRTOGKRkW9GCHL3RspBNTRQ-JhL5TnzXeigmVZq6w1wapxLuLOnZQRiAlw20f1ay_IcaNKCvlbqbNMxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">- نیروی دریایی سپاه پاسداران انقلاب اسلامی با یک کشتی در فاصله ۷.۵ مایل دریایی از سواحل عمان درگیر شد.   این کشتی تلاش کرد تا از تنگه هرمز از طریق مسیری غیرمجاز و بدون هماهنگی با اداره تنگه خلیج فارس عبور کند.</div>
<div class="tg-footer">👁️ 1.29K · <a href="https://t.me/SBoxxx/17981" target="_blank">📅 18:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17980">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">در واقع دارند می‌گویند از مسیر عمانی ها نروید چون اینقدر خطرناک است که ممکن است ما بزنیم تان!  سبحان الله!</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/SBoxxx/17980" target="_blank">📅 18:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17979">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVyqK4-UrdCOf0oUp6gzGeP72ehIZ6Y1lK7TIO4LYnfkf-QiXWGHp_LMp3mTrN469lsEHZ9hUvzGziNplRu_BD07Evgo4hTHmhHzxZKyCQU9tPGeYIFRfA1qWMaeowNEwhVsGrD5Dz4JzVTbzC4Q-AujprQPLo5qPFTn3n3FlThjSsiurSAfMr_W_d6suC_KjoU_nXZAl1YlCywVFBcrtQwtJ9dCGMxB6pCL1XQnhbd-0MotQ06TJrkW-Zei5fIEsbESAPtUoizwbcfYmsazOahhFQTB2W3KhWT9mMQpKIS_v5V_qZ1_A9k2oWEEj77kFks9DjqmMwlwl0WoVQw_BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وال استریت ژورنال، ایران ۳.۸۴ میلیارد دلار را از طریق صرافی رمزارز CoinEx منتقل کرده تا تحریم‌های آمریکا را دور بزند.</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SBoxxx/17979" target="_blank">📅 15:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17978">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMILITA CAMP</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIg5QR2YecHWu_ffip9_CYTDoz7LLrHzZMxfiEkruwYqkp6-oVrzMHoReIvmTfzCXPHVk76pWmp_jJf7f9YdFSDOxiru8TVVp-OGULKKVNYhFQQephte5L6V2puf7J_ffKrAlI18Aaif_1YTU9sWN03dRN9HRyCu-35CqCwgkNAT2PmfYLvNWEs2UR4KFyu8synf4-R3kl0gHN9TsxoDsLdKjVmJIE3haKneA7r4bF5QuEeV9LYR4ER3SY1zc-X4yrWzWly7Ad99ji1JF2v8McLNKIj2b4bz7Ftm3QLgBdXdFhBITDtwJYSAXL_BF2dRWEF0TYhntlKihHGfanCjnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">● این میم در مورد مذاکرات ایران و آمریکا توسط خیلی بازنشر شده.
@Milita_Camp</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SBoxxx/17978" target="_blank">📅 14:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17977">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پس از آنکه عمان اعلام کرد که یک کریدور دریایی در جنوب تنگه هرمز ایجاد کرده سپاه این بیانیه را منتشر کرده است:
🔸
ساعاتی قبل بدون اطلاع و هماهنگی با جمهوری اسلامی ایران از طرف برخی مراجع مسیر جدیدی برای تردد کشتی‌ها در تنگۀ هرمز اعلام شده که این مسیر غیرقابل…</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SBoxxx/17977" target="_blank">📅 12:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17976">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پس از آنکه عمان اعلام کرد که یک کریدور دریایی در جنوب تنگه هرمز ایجاد کرده سپاه این بیانیه را منتشر کرده است:
🔸
ساعاتی قبل بدون اطلاع و هماهنگی با جمهوری اسلامی ایران از طرف برخی مراجع مسیر جدیدی برای تردد کشتی‌ها در تنگۀ هرمز اعلام شده که این مسیر غیرقابل قبول و کاملاً خطرناک است.
🔸
به اطلاع همه می‌رساند
تنها مسیر مجاز برای عبور از تنگۀ هرمز همان مسیر های اعلام شده از طرف جمهوری اسلامی ایران می‌باشد
، و تردد شناورها در خارج از این مسیرها بسیار خطرناک و ممنوع بوده و اخطار می‌دهیم از هرگونه تردد در خارج از مسیر های ابلاغی جدا خودداری نمایید.
🔸
هماهنگی با نیروی دریایی سپاه برای عبور از تنگۀ هرمز از طریق کانال ۱۶ الزامی است و
با شناورهای متخلف برخورد خواهد شد.</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/17976" target="_blank">📅 12:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17975">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مسکو با فروپاشی بنزین روبرو شده است.
پهپادهای اوکراینی عملیات بزرگترین پالایشگاه مسکو را مختل کرده‌اند  و این واحد تا سال ۲۰۲۷ تعطیل شده است، - رویترز</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SBoxxx/17975" target="_blank">📅 12:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17974">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">به
گزارش وال استریت ژورنال، ایران ۳.۸۴ میلیارد دلار را از طریق صرافی رمزارز CoinEx منتقل کرده تا تحریم‌های آمریکا را دور بزند.</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17974" target="_blank">📅 08:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17973">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دو سناتور جمهوری خواه با تغییر رأی خود از لایحه محدود کردن اختیارات جنگی ترامپ، باعث شدند که لایحه کاهش اختیارات جنگی ترامپ لغو شود</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/17973" target="_blank">📅 08:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17972">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دو سناتور جمهوری خواه با تغییر رأی خود از لایحه محدود کردن اختیارات جنگی ترامپ، باعث شدند که لایحه کاهش اختیارات جنگی ترامپ لغو شود</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17972" target="_blank">📅 07:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17971">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ درباره اردوغان :
او دوست من است و از جنگ دوری کرد.
می‌دانید، او کاندیدای اصلی برای ورود به جنگ با ایران بود.
شاید در کنار ایران، چون همانطور که می‌دانید، طرفدار  اسرائیل نیست.
و من از او خواستم لطفاً دور بماند، و او این کار را کرد.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17971" target="_blank">📅 00:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17970">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506e64b21.mp4?token=ppAT-bTNjwYSS0kKycQXHLa667v2bH8QIp460jmuk3qaYIshCrA6CjTfFN1gXgdcZksqT1S7hrU7WzpFCwnLL1ui_z9cWi9dnkjbjBUimr97YVRt7OMlAuHdMyvDaf_6rfMkcQ91tbAczksXoiaYa21TeOsqNcoLvhjjIjsW-NqG7-p7IwNeHYo1eUNvoC1ioHciDx_Uv-0Wl3K60pkcHd1QRFAZ20Zk5bAxqUBQnIDgoIMRg_dpPyVqej2Y_wcA-rZHjDdFFoTjrI0M3rNGTF1t8xlnYXpuiyC23m7xjOcZ9VEO65JYCY-5Ulm6K1D6MTWoNunhMQEjaTeAVcO5cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506e64b21.mp4?token=ppAT-bTNjwYSS0kKycQXHLa667v2bH8QIp460jmuk3qaYIshCrA6CjTfFN1gXgdcZksqT1S7hrU7WzpFCwnLL1ui_z9cWi9dnkjbjBUimr97YVRt7OMlAuHdMyvDaf_6rfMkcQ91tbAczksXoiaYa21TeOsqNcoLvhjjIjsW-NqG7-p7IwNeHYo1eUNvoC1ioHciDx_Uv-0Wl3K60pkcHd1QRFAZ20Zk5bAxqUBQnIDgoIMRg_dpPyVqej2Y_wcA-rZHjDdFFoTjrI0M3rNGTF1t8xlnYXpuiyC23m7xjOcZ9VEO65JYCY-5Ulm6K1D6MTWoNunhMQEjaTeAVcO5cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17970" target="_blank">📅 00:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17969">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ادعای ترامپ: ایران امتیازات بزرگی می‌دهد  جنگ خیلی خوب پیش می‌رود. همانطور که می‌دانید، ما با اختلاف زیادی در حال پیروزی هستیم.  ایران امتیازات خیلی بزرگی می‌دهد. خواهیم دید چه اتفاقی می‌افتد.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17969" target="_blank">📅 22:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17968">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ادعای ترامپ: ایران امتیازات بزرگی می‌دهد
جنگ خیلی خوب پیش می‌رود. همانطور که می‌دانید، ما با اختلاف زیادی در حال پیروزی هستیم.
ایران امتیازات خیلی بزرگی می‌دهد. خواهیم دید چه اتفاقی می‌افتد.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17968" target="_blank">📅 21:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17967">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">#USOIL — W  در تایم هفتگی به کف یک کانال معتبر هفتگی می رسد و از اینجا ریزش بیشتر توجیه بنیادی ندارد.  این یادداشت را هم بخوانید.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/17967" target="_blank">📅 19:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17966">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWnW9QV5VRMwcxf5G6-QKyEj7UVuEChedmKvPFkS544QIt9m0tH-xPCFwZSP5z0CeLYWCK3L_nyfncXmd-X4rAoeH2x-HiK5RPOMnblWG4R9KCmTWp8hof_afYaoyVxtxZigcB1oc1f1qQ72J5eqSOljvVH4rf-Je_sX_P8LFDsFAOHUWcdXnXTXLbDjp-WbTRfOuuEurgnH8V2epm-2YteoEwnHGWDdz2oYyJac-8v3tN9yi6rX-XgENBwnOkBRXEFLcqUS7N7oVslaaLQhP0cpyUarefLLF0F-HgX5s1-6RakD3f97hopcVEQNMPyZn9OD5JSJ9pnH43aleJ9MeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — W  نفت همه رشدی را که به خاطر جنگ ایران تجربه کرده بود برگشت و اکنون در حال نزدیک شدن به نقطه شروع حرکت است و زین پس دیگر هیچ ریسک پرمیومی برای جنگ در قیمت لحاظ نشده.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17966" target="_blank">📅 19:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17965">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دلار 166 هزار تومان!
بخشی از این رشدها به خاطر کثافت کاری ها و باج هایی است که به طلاداران داده می شود. وقتی اونس سقوط می کند دلار را بالا می برند و بر عکس.
تارگت های 240 و بالاتر همچنان در دسترس هستند البته اما  این رشد دیروز و امروز برای این است که گفته شد.</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17965" target="_blank">📅 19:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17964">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLsnuTUIk8Xk_YQ873vOqVk8apnXeZDRYED0OvTDROqBKP1Y08OMc6OM2aLf0RoercQ0F8lNlAbqYM1QP-YuPZYIPCZzd-VjKOk778UtMjWpgjluN-k6kysaonoIixCb45Vpbmo2MAvcj_OXMzXat-sPsC66uxNphLOzXAPkWjdALLH5vgaFlYbS-lqWnrJC26o2Qkhns5Cx14KmueOpoBoOaX6gOE-p-6CF-LD2m8aBvAjTcsJxl_b3digZKYVyBA08vEplmMFZL6AavrCObrAMNkegsMI3Bi_y9JB-CpGF7Q9y13_Xsh7VDoLxEuF9IlRr9pJjnTYI5nNo8nj-lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  در محدوده مشخص شده می شود به دنبال موقعیتهای خرید باشیم.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17964" target="_blank">📅 19:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17963">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رئیس‌جمهور ایران مسعود پزشکیان رسماً نخست‌وزیر نارندرا مودی را به شرکت در مراسم تشییع و تدفین چندروزه رهبر عالی‌رتبه آیت‌الله علی خامنه‌ای در ایران دعوت کرده است.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17963" target="_blank">📅 16:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17962">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رئیس‌جمهور ایران مسعود پزشکیان رسماً نخست‌وزیر نارندرا مودی را به شرکت در مراسم تشییع و تدفین چندروزه رهبر عالی‌رتبه آیت‌الله علی خامنه‌ای در ایران دعوت کرده است.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17962" target="_blank">📅 16:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17961">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رویترز:   سپاه پاسداران انقلاب اسلامی سلول‌های مخفی در عراق ایجاد کرده تا حملات پهپادی علیه کویت، عربستان سعودی و امارات متحده عربی انجام دهد. این سلول‌ها از جنگجویان شیعه نخبه عراقی تشکیل شده‌اند و مستقیماً به سپاه پاسداران گزارش می‌دهند؛ بین آوریل و مه حداقل…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17961" target="_blank">📅 16:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17960">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حقیقتا «الکسیس میانرودان» لقب شایسته ای برای عراق نیست؟!  تل آویو - اسرائیل برای پشتیبانی از عملیات هوایی خود علیه ایران، یک پایگاه نظامی مخفی در صحرای عراق ایجاد کرد و حملات هوایی علیه نیروهای عراقی انجام داد که تقریباً در اوایل جنگ آن را کشف کردند.  به گفته…</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/17960" target="_blank">📅 16:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17959">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QG1cHQTY6R6kzXa1cJ_vSnJyXUTUcY0NW5QTnRqcHgu42yR2hnStCA_27y8V3-v8-q-1OPIoTwe4xV5nEb7h8QEx307ws6-6uMx2VRCjlbPYinm48pY5bOP8VlSFisJEMKLAQdn2v5Y69P0u-iW8uG5wGeet7MeUGzHUnEzdJp6501QyJOWaHCNFEXd1AXVQPZEV5wZvBIqpQYqU6uvU49HwjfkoPRJTufJwD-TKwY-EYRY5yPmiLIsT0ptXcUk753mDk_ZgvaBe6Rlav79CycnUt1BxIGwke1lxDhD9rRiDeWZu1q9ve0SvEKclF_BDp_k2gTiBypBsPaFrL0HXug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#DXY — W  پس از یک سال رنج زدن، شاخص دلار به صورت کوبنده ای رهسپار تارگت های اعلامی شده.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17959" target="_blank">📅 16:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17958">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d84yZxq94I5lFdjZAAJoxlD3bDwi0mWWfu7Mi7icJ9QqR67MWmLIctA913FNvhVWVxfGeAzFAYPKFE873huTx_3gAK0JYBG6NA48zZ50-GKPL3jvb3ifbKBVcUJ4f8kltgUGPSIiDPqCOQmwLoKhNA_yiT1-WheDXOdT7jpuSVcyLvfmp0xkpl4TE5WyF8LtFWklGaaYCJHpL-6_LJyfTZhyrBJVQLLP4yjzjZGAFgJ4vFP52luaemL46Pm5fArxE7DDgQOzDT9LqNgKwjK9INBvlTO5Q2alWdTHJtcSZE12OhaOl3yQoCMmloBFu3zMBKlT1tumfAqbSMvyzrhCOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#DXY — W  رسید به کف کانال هفتگی!  از این هفته فروش دلار که ممنوع است هیچی، خرید هم در دستور کار قرار می گیرد.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/17958" target="_blank">📅 16:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17957">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ: ۵۰۰ میلیون دلار در ابتدا برای خرید کالاهای آمریکایی به ایران داده می شود</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/17957" target="_blank">📅 15:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17956">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/925922fd6b.mp4?token=aKROIWa2vq3H9Fll8b2381V79C-Guccn9qVokzyTGesgYEbJefc6_qDdsAUMvHMPIUwZuFEpD_ofcFcQ1880gQFIkOeUFK25TsT_aRJibXhnijDHeSxo2sUbXA-ytMUMwPV_PKE8FTa0W0KuAHfONBc7iWKS-zL347v9Qb1BCAcI0XBmyh_z3vQeisfI7uBWJ6tbyADm4bltD0fJ8oa_NsScvUL_9MQ6-Bn_QOzUCp_07E82GMiT-h987WFr28x3FnUPgeCNz3FP8KEjZ9QZ2rA7QT_QPWZxgr55XDp5cYPo3zky6E_Vwg67fhM_XogySvTgtBBRJQW4csWZYIZQPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/925922fd6b.mp4?token=aKROIWa2vq3H9Fll8b2381V79C-Guccn9qVokzyTGesgYEbJefc6_qDdsAUMvHMPIUwZuFEpD_ofcFcQ1880gQFIkOeUFK25TsT_aRJibXhnijDHeSxo2sUbXA-ytMUMwPV_PKE8FTa0W0KuAHfONBc7iWKS-zL347v9Qb1BCAcI0XBmyh_z3vQeisfI7uBWJ6tbyADm4bltD0fJ8oa_NsScvUL_9MQ6-Bn_QOzUCp_07E82GMiT-h987WFr28x3FnUPgeCNz3FP8KEjZ9QZ2rA7QT_QPWZxgr55XDp5cYPo3zky6E_Vwg67fhM_XogySvTgtBBRJQW4csWZYIZQPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خارجی ها مخ شان سوت کشیده و فکر می‌کنند بیرانوند راننده یک تراکتور است!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/17956" target="_blank">📅 14:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17955">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یسرائیل کاتس، وزیر دفاع اسرائیل:
«حتی اگر از سوی آمریکا درخواستی مطرح شود، ما از لبنان عقب‌نشینی نخواهیم کرد.
دویست هزار نفر از ساکنان [شمال اسرائیل] هنوز به خانه‌های خود بازنگشته‌اند.
ما تمام رهبری حوثی‌ها را از بین برده‌ایم، به‌جز عبدالملک الحوثی که در تونل‌ها مخفی شده است.
اگر او در تیررس قرار بگیرد، کشته خواهد شد.»</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17955" target="_blank">📅 14:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17954">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVnBLKyjGKkCqYz0faP7p_A6xq5ZnaTpCSPgY8QrIqB7t73pwLUtuigmtERdnY-lJYcZk4vDBueET9WXYoQhGq1Uyb1bE41hfm7HwYCv9_Lx5sJmfdbCkDxOHCLg5XEJKzJFXiwbQ8LMm7h9jveZHkD_4w7boM_wDwyiY8LKYlH_QmoJLxtMh_dsIGq7T_NXOPbsEhDEz2Ne2K3Y31Y0nSB1GvnWVPjePYvmOKd4tk6v_4HGuMttT7s9OFrBfyvL9WKA6ebEE57yrzUyibdaVed_WhYE2DIwAAZ2Db7Xd5kD2WjqA4GRK9fS3SBdeQopaq-eH4YVvORuVCy4SsJ5gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17954" target="_blank">📅 14:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17953">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5YXSwfDftXWtg25OvjigIl0b15FQrtMW1y3x8JvXepoIQs5CdKiiZ0nXMHBEdp7T5VEV9qWURIOJNB0XDGIqQKKy3DQvUzcN9qH95n7OogD3A1QVCsseBunKIr1kLKkay1rF_Wa7h8II8atm68uQunj65oBmYLLFU7AGMVB3jZH0f-31ik9i_dXnPGjp3RVQyVIef-jNccKNVO9afWuXQtTY0HJ2gJGc9_l3uX3LmsQH8pByv_z1ajY6erN66WbRa-eLNZVocvqArCJ1YBioxTMpyacSEXgdEi7-c-_0DgxbEbt_0ZDU6i-k9LvdRrZWBHhyuHn0XpvzeDZc5RWdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#طلا
بر اساس نمودار، احتمال ثبت یک کف دیگر پیش از پرواز دوباره قیمت بالا است.
بهترین محدوده خرید میان مدت 14.2 میلیون تا 14.9 میلیون است و تارگت حداقلی 29 میلیون تومانی فعال خواهدشد.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/17953" target="_blank">📅 12:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17952">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">هاآرتص، با استناد به منابعی در ارتش اسرائیل:  ناامیدی و احساس ناتوانی در میان افسران در لبنان به دلیل عدم قطعیت ایجاد شده توسط اقدامات نتانیاهو و کاتز.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17952" target="_blank">📅 12:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17951">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">برخلاف تصور رایج، «لابی کشاورزی آمریکا» یکی از قدرتمندترین ائتلاف‌های ذی‌نفع در واشنگتن است. اما این لابی یک سازمان واحد نیست، بلکه شبکه‌ای از انجمن‌های کشاورزان، اتحادیه‌های تولیدکنندگان غلات و شرکت‌های بزرگ کشاورزی است.  نکته جالب اینجاست که این لابی، برخلاف…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17951" target="_blank">📅 10:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17950">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">توییت ترامپ در مورد ایران:  با وجود اعتراضات و اظهارات نادرست آنها، همراه با تبلیغات مکرر اخبار جعلی که همه تلاش خود را می‌کند تا پیروزی آمریکا را کوچک و بی‌اهمیت جلوه دهد، ایران به طور کامل و جامع با بازرسی‌های هسته‌ای در بالاترین سطح برای آینده‌ای نامحدود…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17950" target="_blank">📅 10:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17949">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">هاآرتص، با استناد به منابعی در ارتش اسرائیل:
ناامیدی و احساس ناتوانی در میان افسران در لبنان به دلیل عدم قطعیت ایجاد شده توسط اقدامات نتانیاهو و کاتز.</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/17949" target="_blank">📅 09:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17948">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتحلیل و رصد</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0802e26a.mp4?token=HONgKpNvL1UhSWi8gxIM456MC65K9ZBAVY_QW-msS8KDCacRbIDZkTKUdgrYMIr1FC1wykFwlYJyQaUTsOmb1aELUO6B3-t9tqp6Vr_lNohaR1i0bN_hvPAAoStg7BcLwQbzNPPNFEXgpnk20JSz9iU8KZE1fQOmKCnoXM8R3Hm6f4-AMDV8Chw2LdU-Ea1SVbHEzcMjCXHAMdt3PAkvlMur3nVCUX669xt8rNrJh2m3Pz_BF7Sk2PtRt1cORbFaPMERmp3DkQY6PGZr95OhGHKloz2rFoiBpqhiq6FAfjvKiAxTaRPnJkD7aQDC4-m_wY8HNN4PHxgUgDnuGTIs8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0802e26a.mp4?token=HONgKpNvL1UhSWi8gxIM456MC65K9ZBAVY_QW-msS8KDCacRbIDZkTKUdgrYMIr1FC1wykFwlYJyQaUTsOmb1aELUO6B3-t9tqp6Vr_lNohaR1i0bN_hvPAAoStg7BcLwQbzNPPNFEXgpnk20JSz9iU8KZE1fQOmKCnoXM8R3Hm6f4-AMDV8Chw2LdU-Ea1SVbHEzcMjCXHAMdt3PAkvlMur3nVCUX669xt8rNrJh2m3Pz_BF7Sk2PtRt1cORbFaPMERmp3DkQY6PGZr95OhGHKloz2rFoiBpqhiq6FAfjvKiAxTaRPnJkD7aQDC4-m_wY8HNN4PHxgUgDnuGTIs8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">.
🟢
وقتی دکتر مسعود، نمی‌تونه از کاراکتر دوره جَوونی‌ش فاصله بگیره!
پزشکیان [در سفرش به پاکستان] به نشان دوستی یک درخت تو اسلام‌آباد کاشت که رسم پاکستانی هاست.
ولی نکته جالب اینه که هی شهباز شریف نخست وزیر پاکستان اشاره میکنه مسعود جان بسه کم خاک بریز. نمادینه ولش کن. ولی مسعود هیچ رَقمه گوشش بدهکار نیست و فقط بیل میزنه.
@tahlilvarasad</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17948" target="_blank">📅 09:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17946">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⛔️
کارشناس اسراییلی تشریح کرد: ۸ کانون تنش بین ترکیه و اسراییل؛ ترکیه ایران جدید است  یک کارشناس اسراییلی با اشاره به اینکه تنش بین ترکیه و اسراییل به بالاترین حد خود رسیده است، به بررسی ۸ کانون تنش بین طرفین پرداخت.  ایتان لاسری بر این باور است که اسراییل…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17946" target="_blank">📅 23:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17945">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نخست‌وزیر پاکستان، شهباز شریف:
«کشورهایی هستند که می‌خواهند توافق را مختل کنند، و من می‌گویم که بدون ایران نمی‌توانند موشک‌های بالستیک داشته باشند. استانداردهای دوگانه قابل قبول نیست و منطقی نیست که برخی موشک‌های بالستیک داشته باشند در حالی که ایران از آن منع شده است.
یادداشت تفاهم (MoU) به مسئله موشک‌های بالستیک ایرانی اشاره نکرده است».
«این یادداشت تفاهم به موشک‌های بالستیک اشاره نمی‌کند. هرگز روی میز نبود؛ هرگز در دستور کار نبود.
طرف ایرانی هرگز نخواست حتی درباره آن بحث کند».</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17945" target="_blank">📅 20:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17944">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🟢
پاسخ به توهم برخی درباره شکست احتمالی نتانیاهو</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17944" target="_blank">📅 15:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17943">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکاخ رسانه</strong></div>
<div class="tg-text">نفتالی بنت، نخست‌وزیر سابق اسرائیل درباره ایران:
هر بار که اعتراضاتی رخ می‌دهد چه اتفاقی می‌افتد؟ اینترنت را قطع می‌کنند و سپس هیچ ارتباطی وجود ندارد.
پس کاری که من شروع کرده بودم، فرایند تهیه و قاچاق ده‌ها هزار گیرنده استارلینک به ایران بود که اجازه می‌داد اینترنت و شبکه‌های اجتماعی وقتی قطع می‌شوند، ادامه داشته باشند و به اعتراضات امکان هماهنگی و در نهایت سرنگونی بدهند.
متأسفانه، دولت ناکارآمد فعلی اسرائیل این کار را متوقف کرد، همانطور که تقریباً هر برنامه خوبی که ما شروع کردیم را متوقف کردند.
و وقتی اعتراضات رخ داد، آن زیرساخت وجود نداشت.
@kakhresaneh</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17943" target="_blank">📅 15:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17942">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">توییت ترامپ در مورد ایران:  با وجود اعتراضات و اظهارات نادرست آنها، همراه با تبلیغات مکرر اخبار جعلی که همه تلاش خود را می‌کند تا پیروزی آمریکا را کوچک و بی‌اهمیت جلوه دهد، ایران به طور کامل و جامع با بازرسی‌های هسته‌ای در بالاترین سطح برای آینده‌ای نامحدود…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17942" target="_blank">📅 15:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17940">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nu3zcEL_8AOw8Eb4LYwbd73p38L_ZhI71a-7HSZbokjbSwaNuNaiSn9oPF6eWrdDGsE7h4T0UkyBZ9v0Wr4NPjXO4pVVo7oTKHQGaIXXnIQ47vJbUbSowPKbtpWr9W_RqO1an46QUiAD_jYkjmLyEo_cNh_TfEvi5mN1c5dZ3t53XWW0CuRNAr89uWhy2jW0JJwf38zClvaUOIZj47S0LjutEkrJGvxA7KWtjzyzeQyfNjuw5AtrjxAyzUI1LpUMfZsLYzQtar118fcFpUHcYWJn0ID1HM_CoUkMGVQqPNjscm4bP-98Ej275ZGQczmK5RcJnOXitYIs6r60cYMPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PFedKwuemE0_Icfd3E4Zscl3HXI8nuwGyJSt4aQ5C91oJUB4GEGgSeDICU1OJio3btWwZFaLtatbttDMPGv92ye3w-Kb3a1RgCi9OqLHwKUI-800pBHPHR5xk1FeBXjCiKP2srbJsH65suB0JxgDO2JUT9WwOru0NEbKNF3kT6rEkzBfpNvPjXGXYihz6_drGxOM9PAiCwLb7kIMHeDBjZ7HsYpwZz8U-kSMZ54MKrV6yxAMIWvAMNHIhwu9Owr0kezL-lLAnEA4epB-cnZh1T6BWzCa7Qup0P5-UXgEg5qyRSoCO-mlxHdk0plTtUiPS7-jWbbIq55kUXMr1OV1Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر چه جلو میرویم داستان رابطه مسعود با شهباز
دارک و دارک تر
می‌شود
پناه بر خدا!</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17940" target="_blank">📅 15:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17939">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏
امیر پوردستان: آمادهٔ عملیات پیش‌دستانه هستیم
رئیس مرکز تحقیقات راهبردی ارتش:
🔹
در دکترین تهاجمی، عملیات پیش‌دستانه نیز تعریف شده است و چنانچه مصلحت نظام ایجاب کند، ممکن است با انجام عملیات‌های پیش‌دستانه در عرصه‌های ناشناخته، دشمن را به‌شدت غافلگیر کنیم.
🔹
نیروهای مسلح هنوز بخش مهمی از توانمندی‌های خود را عملیاتی نکرده‌اند و دشمن می‌داند که در صورت ارتکاب هرگونه خطایی، با پاسخی فراتر از مرزها و تنگهٔ هرمز مواجه خواهد شد.
🔹
در یک ‌ماه اخیر، ما چند نوبت تا پای جنگ با رژیم صهیونیستی رفتیم؛ لانچرها آماده و دست‌ها روی ماشه بود تا در صورت عدم عقب‌نشینی اسرائیل، جنگ آغاز شود.
🔹
تهدیدات قاطع ایران سبب شد تا آمریکا برای جلوگیری از گسترش جنگ، به رژیم صهیونیستی برای توقف تجاوزات به جنوب لبنان فشار بیاورد.</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17939" target="_blank">📅 15:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17938">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">توییت ترامپ در مورد ایران:
با وجود اعتراضات و اظهارات نادرست آنها، همراه با تبلیغات مکرر اخبار جعلی که همه تلاش خود را می‌کند تا پیروزی آمریکا را کوچک و بی‌اهمیت جلوه دهد، ایران به طور کامل و جامع با بازرسی‌های هسته‌ای در بالاترین سطح برای آینده‌ای نامحدود (بی‌نهایت!!!) موافقت کرده است. این امر «صداقت هسته‌ای» را تضمین خواهد کرد.
اگر آنها با این موضوع موافقت نمی‌کردند، مذاکرات بیشتری صورت نمی‌گرفت! بر اساس این و دیگر امتیازات عمده‌ای که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و هیچ محاصره دریایی بیشتری اعمال نشود. با این حال، همه کشتی‌ها در محل باقی می‌مانند تا در صورت لزوم محاصره دوباره برقرار شود، که در این مرحله بسیار بعید به نظر می‌رسد.
پول و/یا تحریم‌هایی که خزانه‌داری آمریکا آزاد می‌کند، در حساب امانی تحت کنترل آمریکا قرار می‌گیرد و صرف خرید غذا و تجهیزات پزشکی، به طور انحصاری از ایالات متحده، از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما خواهد شد.
این‌ها چیزهایی هستند که ایران به شدت به آنها نیاز دارد. این یک بحران انسانی است و من احساس می‌کنم لازم است که اکنون کمک کنیم، قبل از اینکه خیلی دیر شود. مذاکرات به خوبی پیش می‌رود!</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17938" target="_blank">📅 14:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17937">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🟢
طبق اعلام معاون اول مسعود پزشکیان ، در راستای برگزاری مراسم بزرگداشت رهبر فقید جمهوری اسلامی ایران ،  13 و  14 تیرماه استان تهران و 15 تیرماه کل کشور تعطیل خواهد بود</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17937" target="_blank">📅 14:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17936">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⛔️
دولت ترامپ ، دسترسی به 2 مدل هوش مصنوعی آنتروپیک را برای کاربران غیرآمریکایی مسدود کرد</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17936" target="_blank">📅 12:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17935">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپارادوکس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c175d38c15.mp4?token=cAAn2IP2LMfZg4g0crRHaxGFaE_zhzohh9wQyU5Dg09nsnqgfzPGLZvpGwS9s-wjynltM3FTB4MB8CMPzGUG98HcItUTLEr5VQ0erhPAyOGsaKzTSYgiowyDi4MCirLMvX5lbdjoGqtERO6GzhIDNHV_fPD2gjIT4PG7TPn2qLUOXVs5ONkej-sb69BzZSbwkQRwTL7eK4iq8nn8ZW3iiYpljf9jrwCB-Jnk-i_4Hh5XYRT3X8iIyHqgvHstxQlWAW6oai2D3cL11dme7KmKj6fBy0E0-mkZrntqsFwirW4u0q6TXuxBI9LjOEve5Un2q4NnAj_U4Ut_H21xyNL6w2tgjHPpYJa6mu5GqB3AtTudZ2Cog4LnHsv90FdaMAM5_XQS8qZ8N14xRLhzr3i1CcsnRtWky3FPgK51GU-WRXmtvKX9aL88h68CFxlOwPkrWX2Y4c5j-T89OeMnYgNXPcZ_U33P2pJFlAQQrQzwAKnEkjj7fUk4B41krX97HqOGgKVq3DoykTP3vQskW2SkF36ApttpFwOcWoUR3MCkIsU0fOW9Xls4kBLGzZzNosz7OmyKhv9-8XgNKpdrBoQq-k0DhV6a4Lyzu3-OcD8xLvlENfMkIhAwP2nTHurznLgGxl1XRFzhpHGLJl-L3lxnhGZYI5T0P0eKmKJJ2F1lGFc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c175d38c15.mp4?token=cAAn2IP2LMfZg4g0crRHaxGFaE_zhzohh9wQyU5Dg09nsnqgfzPGLZvpGwS9s-wjynltM3FTB4MB8CMPzGUG98HcItUTLEr5VQ0erhPAyOGsaKzTSYgiowyDi4MCirLMvX5lbdjoGqtERO6GzhIDNHV_fPD2gjIT4PG7TPn2qLUOXVs5ONkej-sb69BzZSbwkQRwTL7eK4iq8nn8ZW3iiYpljf9jrwCB-Jnk-i_4Hh5XYRT3X8iIyHqgvHstxQlWAW6oai2D3cL11dme7KmKj6fBy0E0-mkZrntqsFwirW4u0q6TXuxBI9LjOEve5Un2q4NnAj_U4Ut_H21xyNL6w2tgjHPpYJa6mu5GqB3AtTudZ2Cog4LnHsv90FdaMAM5_XQS8qZ8N14xRLhzr3i1CcsnRtWky3FPgK51GU-WRXmtvKX9aL88h68CFxlOwPkrWX2Y4c5j-T89OeMnYgNXPcZ_U33P2pJFlAQQrQzwAKnEkjj7fUk4B41krX97HqOGgKVq3DoykTP3vQskW2SkF36ApttpFwOcWoUR3MCkIsU0fOW9Xls4kBLGzZzNosz7OmyKhv9-8XgNKpdrBoQq-k0DhV6a4Lyzu3-OcD8xLvlENfMkIhAwP2nTHurznLgGxl1XRFzhpHGLJl-L3lxnhGZYI5T0P0eKmKJJ2F1lGFc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
⭕️
چگونه نام تاریخی و ریشه‌دار دریای کاسپی (Caspian Sea) با یک ندانم‌کاری آقایان پر مدعا خدشه‌دار شد؟!
یکی از تلخ‌ترین لحظات تاریخ معاصر، روزی که حیدر علی‌اُف، رئیس‌جمهور وقت جمهوری باکو، به ایران آمد و در دفاع از نام «خزر» سخن گفت، حال آنکه سید محمد خاتمی، رئیس‌جمهور وقت ایران، نتوانست با تکیه بر اسناد و مستندات تاریخی، از نام‌های اصیل و ریشه‌دار این پهنهٔ آبی همچون «دریای مازندران»، «دریای طبرستان»، «دریای قزوین»، «دریای گرگان» و یا نام بین‌المللی «Caspian Sea» پاسداری کند.
او در برابر آن ادعا سکوت پیشه ساخت و حتی با صدور بخشنامه‌ای شرم‌آور، این دریای کهن و ایرانی را به نام قومی وحشی و بیگانه، «خزر» نامید؛ نامی که هیچ پیوندی با هویتِ تاریخی و فرهنگی ایران‌زمین ندارد.
⚜️
@paradox_p
⚜️
پارادوکس
⚜️</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17935" target="_blank">📅 11:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17934">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8vc0oxS_kRyEovDXNId5ivx6H_-_HeqUlLMnL1Pxwo25dGauSRm0CO87-Ed4zIVANvp5CRkePBJuPiKSX9YQXahT1LKPrWWH1ibMlvjQBxAzMNnqYuQjMmZBVbYrLQWow0aOnbsXe8FPy5ko_t-3MwBZfffmk2dX1mh8x7gH_QM3ZAz7vNfVQsYqjKrL2KK3v2cGfE34No3Sl7UvB4mZclx-icBlmmZLyqzfZftmxDZ6xbMWW_m8XMH2b5t6j4DnmYH_J_LZ4es2bXVCOkRcY72Y7LrxW7ZKXJh-mW6-muWBZVKxGdAuNsDYL0zLC1V8i75UKisp8geORVsGj0SZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت استاد!
از تبیین کوانتومی آفرینش و پایان هژمونی دلار با ظهور بریکص رسیده اند به رفع نیاز جنسی با دوغ!</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17934" target="_blank">📅 09:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17933">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">این را در دیدار حضوری با تیم ایرانی گفته اند !  پس دارند میگویند اگر کشتی از بخش جنوبی تنگه هرمز عبور کند، عوارضی پرداخت نخواهدکرد  اما اگر از بخش شمالی تنگه که تحت مدیریت سازمان معظم تنگه خلیج فارس ایران است عبور کند باید پول عوارض بدهد!  خب شما به عنوان…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17933" target="_blank">📅 07:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17932">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">این را در دیدار حضوری با تیم ایرانی گفته اند !  پس دارند میگویند اگر کشتی از بخش جنوبی تنگه هرمز عبور کند، عوارضی پرداخت نخواهدکرد  اما اگر از بخش شمالی تنگه که تحت مدیریت سازمان معظم تنگه خلیج فارس ایران است عبور کند باید پول عوارض بدهد!  خب شما به عنوان…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17932" target="_blank">📅 07:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17931">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وزیر خارجه عمان:    به قانون بین‌المللی و تضمین عبور امن و بدون اخذ عوارض از تنگه هرمز پایبندیم.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17931" target="_blank">📅 07:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17930">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نخست وزیر و وزیر امور خارجه قطر در مصاحبه با الجزیره:   آنچه ایران در طول جنگ با ما و برادرانمان انجام داد، غیرقابل قبول است.  اجماع خلیج فارس برای دستیابی به دیدگاه مشترک برای گفتگو با ایران برای حل مشکلات وجود دارد.  ما می‌خواهیم شاهد همکاری ایران با کشورهای…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17930" target="_blank">📅 07:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17929">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyfvwZXGRVhNZehBhwJ_xS8bgbBKxvy3MvQSNFLSt72IwPQPPIbij92oFYa6lrbOdwKm9krMdbYqn5AlAWVzC2qC0zjJkyAolsNjKqAsT94NVv6ZWzkwnYfpX3qNylbzNN2IZPqHNq9olpVOmHNzCjwBcqahtoUBjdGbzK4KoiIL6HYPKR8GXP4oVrq-Z2o_QdL5nAUd-iwnKEbnPx09Rehfuq3yQl8HRXagLkSuCjdB7rBdXCjxlVlAkVy1193bQ1wjJhksNwIDAn8OE6vPQ-gox1y6OsWbrK2YKkYGgWlkVVm6vozU7YzuIEMyOodrs6hGN1CEYNSrYJ9bsbxzNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی رئیس بانک مرکزی:  ما سالانه نیاز به‌خرید میلیاردها دلار مواد غذایی و دارو داریم پس چه بهتر که در ازای دادن پول‌های بلوکه شده آن را پرداخت کنیم. البته بخشی از پول را هم میتوان صرف کالاهای غیرتحریمی کرد. به هرحال این معامله با آمریکا برای ما سودمند است.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/17929" target="_blank">📅 01:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17928">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">همتی رئیس بانک مرکزی:
ما سالانه نیاز به‌خرید میلیاردها دلار مواد غذایی و دارو داریم پس چه بهتر که در ازای دادن پول‌های بلوکه شده آن را پرداخت کنیم. البته بخشی از پول را هم میتوان صرف کالاهای غیرتحریمی کرد. به هرحال این معامله با آمریکا برای ما سودمند است.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17928" target="_blank">📅 01:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17927">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سرانجام کتابی که وعده دادم درباره پیوند ژئوپولیتیک و بازارهای مالی ترجمه کنم، به چاپ رسید.  به نظرم در این شرایط که چندین جنگ همزمان در منطقه و جهان در جریان است و تنشهایی که میتواند بزودی تبدیل به جنگ های دیگری بشود، فقدان وجود یک دیدگاه تحلیلی چهارچوب بندی…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17927" target="_blank">📅 01:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17926">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔹
شبکه ۱۴ اسرائیل :  بنظر ما ، جمهوری اسلامی ایران به سلاح الکترومغناطیسی دست یافته و با استفاده از آن درحال تاثیرگذاری دلخواه روی مغز ترامپ است - رفتار های دونالد ترامپ هیچ شباهتی به قبل ندارد</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/17926" target="_blank">📅 23:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17925">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔹
شبکه ۱۴ اسرائیل
:
بنظر ما ، جمهوری اسلامی ایران به سلاح الکترومغناطیسی دست یافته و با استفاده از آن درحال تاثیرگذاری دلخواه روی مغز ترامپ است - رفتار های دونالد ترامپ هیچ شباهتی به قبل ندارد</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/17925" target="_blank">📅 23:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17924">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9n_UlFTR1v6MqA6uQcN6iCvZwkTBPv4bBwEuxhSfr9ocJEjWaOgXGHi0GyJUKcel3ryz3VEm-lbEyf1z_B3DeqOEPkY1gg1QAniHt2ghjsLmPNqMdEKUZ9dUaNKTbZRgWB-vr7-znBXur7jegqe-kw7wReoxyhaVkUfJiWVAxfKAdeoBtCOInIVZxXbWlgAAKtCiohoCzL0RAUcfF7PlFXtKXdqvJuIiXvR3loKRPTH1qyA_KXS4qTHpppBLi7Kf8AG8AT0G-gnkJdLj7Hda4iZxmoKNGXRQZ29ggTCKmbYwNHevQ-9faM3-69IXLxo9sZBn7mqab3hDyg24WHL8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوستالژی هر ساله ما آغاز شد…
جای کیان رویگری خالی…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/17924" target="_blank">📅 23:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17923">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">المیادین: هیأت ایرانی تا زمانی که ترامپ عذرخواهی نکند و اسرائیل از جنوب لبنان عقب نشینی نکند، به مذاکرات باز نمی گردد!   ایرانی‌ها اکنون تنها خواستار توقف تجاوز نیستند، بلکه خواستار خروج (نیروهای اسرائیلی) از جنوب لبنان هستند.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17923" target="_blank">📅 22:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17922">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">هند قصد دارد موشک های کروز سوپرسونیک BRAHMOS را به ارمنستان ارسال کند</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17922" target="_blank">📅 22:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17921">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ:
همه کاملاً آگاه هستند که ایران موافقت خواهد کرد تا بازرسی‌های نظامی انجام شود تا «صداقت هسته‌ای» را برای مدت طولانی در آینده تضمین کند.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17921" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17920">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خوش‌چشم، کارشناس صداوسیما:
آمریکا خودش تاسیسات ایران را نابود کرده است و حالا می‌گوید در بازسازی آن‌ها سرمایه‌گذاری می‌کند تا در سود این صنایع شریک شود/ به جای خسارت دادن می‌خواهند ایران را استعمار کنند و ۵۰ درصد سود صنایع ایران را کسب کنند</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17920" target="_blank">📅 20:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17919">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مرندی:
🔻
ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی‌به ایران صورت نگرفت</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17919" target="_blank">📅 20:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17918">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تهران توافق برای اجازه ورود بازرسان هسته‌ای به ایران را تکذیب کرد  خبرگزاری تسنیم ایران گزارش‌های مربوط به یک پیشرفت بزرگ را رد کرد و گفت که هرگز به بازرسان آژانس بین‌المللی انرژی اتمی اجازه ورود داده نشده است و ترجیح می‌دهد که هرگز نیز چنین اجازه‌ای داده…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17918" target="_blank">📅 20:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17917">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpL7DurYtp2UQTlqudKV-_3d6L3Yv57qBu7yYzuE2NrgbQk_mAFYNd8_J9qsTVAQYFB0df_cnl8c1lWw8UZiD_joKkCimxp1T_TLqlIOI3PEcd2Gp6D0Io38U-MdywwZDlIA7kh6YdJQZzj7JsUt15DLqyqA65c6Ri3arGy06BYsHooxyw8k84FkgnStxl1ZrgrwfE0iSWmFhhdRgEP6OdnmDZF_f1L9bLhAsc2-8OUZI49fRpOwnaVYetptW5qWAkB1GOx0rd7Cy1KT_luDb-hcJpM_qtEzXRqFueGtpRPeRh3b-ceH1jxFjFH-334xbigjyp9xITBwi9jIQJUIZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه ایران و انیران خواستار ابطال این پیمان هستند جز باقر!</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17917" target="_blank">📅 19:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17916">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خردمند کسی نیست که بتواند میان خوب و بد، خوب را برگزیند، بل کسی است که توان تمییز خوب از خوب تر و بد از بدتر داشته باشد.</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/17916" target="_blank">📅 19:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17914">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LlvN5_Z7CLIER6-bMng2Yjjpo2j7dd5mDyxZE8Jf55zOfQSCkLJ9xsdim5gU4z0uehBsz0zODTEqKD1lc2lxmJT-ldCewes0DojxltMDJsgb9mkmTQ1vx0RNDO0o1hL_ZIrCjP1GmHwuyU2Kkx-QwciBcTXUaKDX9FXNep7JubU5YY82cGWlqYVELK_xv2BEes8rZgb9pgrafKp85advKrJ-UlVFsFNTbFvFV0hOsdBGfQW3y06jYwRZyijIxIqPV7bBBpBIDKa9asfP1pHPmcXrkzXPEmyftZd64KcG3Iyf-ldmpmTThRlA5x4YAt8dQvIrVkGJBaG8N3iT8ZT9pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y2qAn2bSWujFn3rri-RyI0RFu1yoFTw2II5SBd9ZmU2WL49Xjs8ooMdT5FzS3085pe2zkcTdWwS6x_CYjEUoGaeBhcsI_s8kpH4rtneCK397n322GTDx70DuHILBzWlZm2Mv4eS0g_pdTf5Q7EqIn2HVbQAlgCoxNflxG9xPVbmOxGFhhbQJct5AW-8cBRFRLhoN0VDuZ4FHd-l-nak4jE2bTDriLu4GYN2Vh2ILjEq0Ohk7SjFFXM5nRxq-3bVlRWAMVK3da1g_8bLJrs-ZTN7RFfxwb7p3bY8pS-0Ht_sda4VfvcLuJnzEBP348nMre-uwGbq9DXhNoXcJfev5Xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نمیگذاریم اسراییل بزرگ تشکیل بشود اما خودمان دنبال توران بزرگ هستیم و این نشان می‌دهد چقدر مادرقحبه هستیم.</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17914" target="_blank">📅 19:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17913">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیدالله کریمی پور</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_csD4IAC3s1F9LIEKf42gHzeTljNRzyITdeZRm2LTMQkDA245EnjUumfZBcx2UKgKC0KXw8WWBJrOI48jROaxfH3bVx0Do3kpN2jVYWoW6a5xDwUXcP1NkR7A8XwnKo6m8iX4ykLVVJeFe-Gdsz8woEo1z9JpHiZ6QN0fuZK4wHpRp0VGpLQkj5J6xREbuK3ZGbPfdegIc-Glo_fN3lSJCBQr2Yia3jWMJ3iPE07LfZ6L6UQUNLSj-ZF_AlESaoklh8adnyiHhK5Ygf73ARxrgJggLptSbOAPa7DbrYbWlklZZzn9sEe_Pj-1eTF1NV-9y3ENZNCBxaA8cQ64ZZSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو دشمن اصلی ایران
این‌نقشه، راهنما و توضیحاتش امروز یکم‌ تیرماه(۲۲ ژوئن)‌ از یک کانال تلگرامی نظامی اخذ شده است. بر نقشه و راهنما متمرکز شوید:
"کوریدور خیانت؛ تمام حملات هوایی به تهران و حومه، از این مسیر و به طور روزانه انجام میشه... آذربایجان، ترکیه"
کاملا درست ترسیم کرده و نوشته است. باور کنید در جنگ‌های ۱۲ روزه و ۳۹ روزه، تقریبا هر شب و روز‌جنگنده ها از بالای سر من میان البرز می گذشتند.
ولی این کمترین سزای حکومتی است که حاضر به گوش دل دادن به پژوهش های بیطرفانه نیست.
بیش از ۲۵ سال پیش، پژوهش های طولانی مدت و استراتژیکم طی دو جلد کتاب با عناوین: مقدمه ای بر ایران و همسایگان (منابع تنش و تهدید) و کتاب: مقدمه ای بر تقسیمات کشوری(ج یکم)‌ منتش شد . کتاب هایی که نه تنها سرداران آن را خواندند، بلکه مقدمه ای شدند برای اجرای پروژه اطلس استراتژیک ایران. پروژه ای که بارها برای سرداران فیروزابادی‌، شمخانی، باقری، سلامی و ...سرلشگران زنده گزارش شد.
میدانید چکیده کتاب ایران و همسایگان چیست:
دو دشمن پابرجا و اصلی ایران ترکیه و جمهوری آدربایجان هستند.
ولی کو گوش،شنوا.
#یدالله_کریمی_پور
#karimipour_k</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/17913" target="_blank">📅 18:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17912">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfTz0wHDf_1HqW5LInyaRmD3SQPqysNolG5MpU3Xji-7QEYeu1_44zqiZGFn9h3Z2RCISHvBhPGK5Bx9HWahs8a-znl1mo6RuX0gL2HSHFLs794z2ebWZpv6gZ3TWB5JJMN63JjXn0kdR9O2oSSbzvNYpFlOJBgsyqrKYkqdn1ZDZYapu4yCXT7LC6GTQiQG5VORRo1nvZ64L8CzZaPd3916vG7zNIJ_jkKMca9aImAAZjEIyWf51wsIS8mBfw3CUVCRocDZhRYfVl3nhlaVZq-4S8vp7Igln2_DUWOBge7Xm3atw1RLc63iV1G47ZsLfGV_JLdGzFzX1fB1nKsMxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ترامپ: دارایی های بلوکه شده ایران عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد  اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/17912" target="_blank">📅 18:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17911">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تهران توافق برای اجازه ورود بازرسان هسته‌ای به ایران را تکذیب کرد  خبرگزاری تسنیم ایران گزارش‌های مربوط به یک پیشرفت بزرگ را رد کرد و گفت که هرگز به بازرسان آژانس بین‌المللی انرژی اتمی اجازه ورود داده نشده است و ترجیح می‌دهد که هرگز نیز چنین اجازه‌ای داده…</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/17911" target="_blank">📅 18:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17910">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس، درباره زمان شروع بازرسی‌های هسته‌ای: احتمالاً این هفته، حتی از امروز</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17910" target="_blank">📅 18:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17909">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انفجار در کارخانه گاز طبیعی مایع قطر؛ ۵۴ مجروح و ۱۸ مفقود  وقوع یک انفجار داخلی در مجتمع صنعتی راس‌لفان قطر که تأمین‌کننده یک‌پنجم گاز مایع (LNG) جهان است، ۵۴ مجروح برجای گذاشت و عملیات نجات برای یافتن ۱۸ مفقود همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/17909" target="_blank">📅 18:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17908">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1Ovk55GrXXqqmmKF5WK-T1LslJEM41N5ed-mo0j0jssnU_Rq7K9Q4RPCI5nAQg-6uZca8Ex_qnWmXz6iICisZSSdKnUrMO28o_EtbeBnKn-fZQ6EMBtL8QBmPNP50B-K4sxlRteWHnFShwAQ7_XNR6igdh2tN6B7FLqXllu_JgWh8tceJrlh3CgrpWOSqfLkjMBKfe5GQ01-BTiWCo9ZeFVRpQvFRdq9xSwLiv7vl2QsySmyjn9SnQoFurwMD6TkhU9ketXiah62XDZvMgxVqTbEumjnIa04cKTixlb35bf7r-PnFv7b0pRwUlTSp3--GYj3AXfcSQ9Chxyj0Vxzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
یادداشت تحلیلی: آینده بازار نفت در شرایط جدید ژئوپلیتیکی
بازگشایی تنگه هرمز و توافق آمریکا و ایران می‌تواند فشار عرضه نفت را کاهش دهد، اما بازگشت تولید به سطح عادی زمان‌بر خواهد بود و رقابت تولیدکنندگان دیگر را تشدید می‌کند.
در سمت تقاضا، رشد اقتصادی جهانی در برابر ریسک‌هایی مثل دلار قوی، نرخ بهره بالا و تنش‌های ژئوپلیتیکی قرار دارد و همین باعث می‌شود بازار نفت وارد یک دوره نوسانی و چندعاملی شود.
🔗
ادامه یادداشت را از اینجا بخوانید!
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/17908" target="_blank">📅 16:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17907">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نخست وزیر و وزیر امور خارجه قطر در مصاحبه با الجزیره:
آنچه ایران در طول جنگ با ما و برادرانمان انجام داد، غیرقابل قبول است.
اجماع خلیج فارس برای دستیابی به دیدگاه مشترک برای گفتگو با ایران برای حل مشکلات وجود دارد.
ما می‌خواهیم شاهد همکاری ایران با کشورهای خلیج فارس در سطح بالایی از اعتماد باشیم.
مقدمات برگزاری نشست‌های خلیج فارس در دوره آینده برای بحث در مورد امنیت منطقه‌ای در حال انجام است.
موضع اصولی قطر رد هرگونه تغییر در وضع موجود تنگه هرمز نسبت به آنچه قبل از جنگ بود، است.
چشم‌انداز ما برای تنگه هرمز، باز بودن آن و آزادی عبور و مرور از آن است.</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SBoxxx/17907" target="_blank">📅 16:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17906">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCege3uTAvxZVh9g_nBNwvEmBttyx_jmeJQ9Ms0WCIHV1oB7AJJaihKHfhvkiMLcHJDPNKLkkvI46rnX7wu-f033VBs9cCL4T1ERafXOOUslrPI6Z5lDmO_EFC3E-j7u3-MVJdQu-sXWjqV8Z6taa_qQrdoPtS1W-pe5Hc1-SYWhQIIR9jwi0Kqj5g0CFAono7s1BrSFwSsPFlD57fYj1j4zuWKpXKW8OPgwp8OX_aQDISnspAiUyzwdQTBwASxD8A-lJxGF431emFZwTY_RT1veYj2P1Cp0rWPngVnmcrNAhYMlMDtxq6hNynXaedVeEHF1arjzDbvas2-1gYxP7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش احتمال وقوع رکود اقتصادی در آمریکا به ۱۵ درصد پس از توافق با ایران طبق تحلیل موسسه گلدمن ساکس !</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/17906" target="_blank">📅 15:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17905">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">معاون ترامپ: دارایی های بلوکه شده ایران عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد  اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/17905" target="_blank">📅 15:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17904">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کار خدا را ببینید که پاکت زاده های بدافزار «بله» آمدند کانال مرا بستند حالا تلگرام آزاد شده و بعید نیست خود بله و روبیگا فیلتر شوند!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/17904" target="_blank">📅 15:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17903">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">جی دی ونس:  آنچه جرد کوشنر و قطری‌ها و کل تیم انجام دادند، به نظر من، یک توافق کلاسیک ترامپی است. اگر دارایی‌های ایران آزاد شود، کشاورزان آمریکایی را ثروتمندتر می‌کند و به تغذیه مردم ایران کمک خواهد کرد.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17903" target="_blank">📅 15:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17902">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">روزنامه وال استریت ژورنال:  آمریکا پیشنهاد داده ایران فقط برای خرید دارو، غذا و کالاهای بشردوستانه به ۶ میلیارد دلار دارایی مسدودشده‌اش در قطر دسترسی داشته باشد؛ ایران هنوز این طرح را نپذیرفته است.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/17902" target="_blank">📅 15:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17901">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">جی‌دی ونس: ایران مذاکرات را ترک نکرد؛ ترامپ به اظهارات تهران پاسخ می‌دهد
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، درباره گزارش‌های مربوط به خروج هیئت ایرانی از مذاکرات گفت:
«ایرانی‌ها تهدید کردند که مذاکرات را ترک خواهند کرد، یا دست‌کم چنین تهدیدهایی در شبکه‌های اجتماعی مطرح شد، اما آنها مذاکرات را ترک نکردند.»
او همچنین درباره واکنش‌های دونالد ترامپ به اظهارات مقام‌های ایرانی افزود:
«دیروز به ایرانی‌ها گفتیم وقتی وارد چیزی می‌شوید که نسل ما آن را "کری‌خوانی" می‌نامد، نباید انتظار داشته باشید ترامپ پاسخی ندهد.»
ونس ادامه داد:
«وقتی آنها حرف‌هایی می‌زنند که درست نیست، ترامپ هم به آن پاسخ خواهد داد.»</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/17901" target="_blank">📅 14:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17900">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس، درباره زمان شروع بازرسی‌های هسته‌ای: احتمالاً این هفته، حتی از امروز</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/17900" target="_blank">📅 14:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17899">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس، درباره زمان شروع بازرسی‌های هسته‌ای: احتمالاً این هفته، حتی از امروز</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17899" target="_blank">📅 14:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17898">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس: ایرانی‌ها موافقت کرده‌اند که بازرسان آژانس بین‌المللی انرژی اتمی را بازگردانند</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17898" target="_blank">📅 14:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17897">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس: ما پایه بسیار خوبی برای یک توافق نهایی موفق گذاشتیم</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17897" target="_blank">📅 14:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17896">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس: ما پایه بسیار خوبی برای یک توافق نهایی موفق گذاشتیم</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17896" target="_blank">📅 14:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17895">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پس فرق این دوره ۶۰ روزه با بعدش این است که ممکن است بعدش آمریکا عوارض عبور بگیرد!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/17895" target="_blank">📅 14:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17894">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">— یک منبع اسرائیلی به سی‌ان‌ان گفت:
«اسرائیل در حال بررسی اعلام عقب‌نشینی‌های نمادین از مناطق جنوب لبنان است.
عقب‌نشینی‌های نمادین شامل عقب‌نشینی برخی نیروها از مناطق اطراف خط زرد خواهد بود».</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/17894" target="_blank">📅 14:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17893">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">استارمر نخست وزیر چپگرای انگلیس استعفای خود را اعلام کرد.
دو ضربه بزرگ به چپ جهانی در کلمبیا و بریتانیا در یک روز!</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/17893" target="_blank">📅 12:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17892">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انفجار در کارخانه گاز طبیعی مایع قطر؛ ۵۴ مجروح و ۱۸ مفقود  وقوع یک انفجار داخلی در مجتمع صنعتی راس‌لفان قطر که تأمین‌کننده یک‌پنجم گاز مایع (LNG) جهان است، ۵۴ مجروح برجای گذاشت و عملیات نجات برای یافتن ۱۸ مفقود همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17892" target="_blank">📅 08:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17891">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">انفجار قطر بحدی شدید بوده که در بحرین دیده و شنیده شده</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/17891" target="_blank">📅 08:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17890">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بیانیه قطر و پاکستان در مورد آتش‌بس در لبنان چه می‌گوید؟
طرفین (ایران و ایالات متحده) توافق کردند که یک «واحد کنترل درگیری» را بین خود و جمهوری لبنان با میانجی‌گری تسهیل‌گران تأسیس کنند تا از پایبندی به توقف عملیات نظامی در لبنان طبق مفاد تفاهم‌نامه اطمینان حاصل شود.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/17890" target="_blank">📅 07:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17889">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
بیانیه مشترک قطر و پاکستان در مورد پایان اجلاس بورگن اشتوک
بیانیه مشترک قطر و پاکستان:
🔹
اولین جلسه مذاکرات سطح بالا تحت چارچوب تفاهم‌نامه اسلام آباد در بورگن اشتوک سوئیس با حضور نمایندگانی از جمهوری اسلامی ایران، ایالات متحده آمریکا و دو طرف میانجی، دولت قطر و جمهوری اسلامی پاکستان، به پایان رسید.
🔹
اجلاس دریاچه لوسرن در فضایی مثبت و سازنده برگزار شد. پیشرفت‌های دلگرم‌کننده‌ای از جمله ایجاد سازوکاری برای مذاکرات فنی بیشتر حاصل شده است.
🔹
بر اساس این تفاهم‌نامه، طرفین با ایجاد یک کمیته عالی رتبه موافقت کرده‌اند که نظارت سیاسی بر میانجیگری را بر عهده خواهد داشت.
🔹
مذاکره‌کنندگان ارشد به طور منظم به کمیته عالی رتبه گزارش می‌دهند و گروه‌های کاری متمرکز بر هسته‌ای، تحریم‌ها و یک گروه نظارت و حل اختلاف را برای اطمینان از اجرای مؤثر تفاهم‌نامه و سایر موارد رهبری می‌کنند.
🔹
کمیته عالی رتبه بر سر نقشه راهی برای دستیابی به توافق نهایی ظرف ۶۰ روز توافق کرده است که زمینه را برای آغاز فوری مذاکرات فنی بیشتر فراهم می‌کند.
🔹
علاوه بر این، یک خط ارتباطی بین طرفین برای مدت ذکر شده در بند ۵ تفاهم‌نامه ایجاد شده است تا از حوادث و سوءتفاهم‌ها با هدف عبور ایمن کشتی‌های تجاری از تنگه هرمز جلوگیری شود.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17889" target="_blank">📅 06:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17888">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
عراقچی
:
🔸
میانجی‌گری خستگی‌ناپذیر پاکستان و قطر باعث پیشرفت‌های بزرگی برای پایان دادن به جنگ در لبنان شد.
🔸
همچنین تحریم صادرات نفت و پتروشیمی تعلیق شد، محاصره دریایی برداشته شد، برخی از دارایی‌های مسدودشده آزاد شدند و طرح بزرگ بازسازی و توسعه اقتصادی ایران اجرایی شد.
🔸
اولین آزمون واقعی: واحد رفع درگیری‌ها در لبنان</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/17888" target="_blank">📅 06:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17887">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گوستاوو پترو، رئیس‌جمهور کلمبیا، نتایج انتخابات این کشور را به رسمیت نمی‌شناسد و اسرائیل را به دستکاری در نرم‌افزار انتخاباتی کلمبیا متهم کرد</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17887" target="_blank">📅 04:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17886">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رییس جمهور چپگرا و معتاد کلمبیا امشب شکست خورد و جایش را به یک راست گرا داد.  قاره آمریکا در حال یک دست شدن است.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17886" target="_blank">📅 04:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17885">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دونالد ترامپ، پس از ونزوئلا، اکنون کلمبیا را تهدید می‌کند و گوستاوو پترو، رئیس‌جمهور کلمبیا، را «قاچاقچی غیرقانونی مواد مخدر» خواند.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/17885" target="_blank">📅 02:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17884">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromورزش سه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6be0b658c6.mp4?token=OVRzOdsJbCLPOn4EWZncVdujkj2omW6gWNbMOwT2awt2ybwrszywFce4Q5-83P04AsMbHnZ3bgj6Fb9KnDIflbhydEeAEEBfRNLQ_SokVXUeqY4D6Q7oVuVN6BDiILQGNt2vIYRpyReP_OF0udXrMArhzZYoyDty9BJOBaoMBJhqUJWHB0QEtDyzxyF7WA4IBY63KTQ5JwAijiRVRjj35ZhC3R0VO7apzzaxzNXy88SwoWjMEe5wpAKSCEb_pKgoqS-e7vtJuneoOOS4-rqmbfXX1MP2XKkn-BYuLDCUrEY1mavR_lMhBfeq0xp09ElsZE579cPfdsckKNyV306olg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6be0b658c6.mp4?token=OVRzOdsJbCLPOn4EWZncVdujkj2omW6gWNbMOwT2awt2ybwrszywFce4Q5-83P04AsMbHnZ3bgj6Fb9KnDIflbhydEeAEEBfRNLQ_SokVXUeqY4D6Q7oVuVN6BDiILQGNt2vIYRpyReP_OF0udXrMArhzZYoyDty9BJOBaoMBJhqUJWHB0QEtDyzxyF7WA4IBY63KTQ5JwAijiRVRjj35ZhC3R0VO7apzzaxzNXy88SwoWjMEe5wpAKSCEb_pKgoqS-e7vtJuneoOOS4-rqmbfXX1MP2XKkn-BYuLDCUrEY1mavR_lMhBfeq0xp09ElsZE579cPfdsckKNyV306olg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سهراب سپهری به جای طارمی؛
😂
راه حل خیابانی برای گل مردود ایران به بلژیک
🏆
در قسمت دوازدهم برجام رونمایی شد
🆔
@varzesh3</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17884" target="_blank">📅 02:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17883">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">به نظرم تنگه هرمز را بدهیم بیرو ببندد و خودمان برویم تنگه مالاکا را ببندیم!  آبش را هم بدهیم آقای میثاقی بخورد!</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17883" target="_blank">📅 00:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17882">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خارجی ها مخ شان سوت کشیده و فکر می‌کنند بیرانوند راننده یک تراکتور است!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/17882" target="_blank">📅 00:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17881">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9uQs97iK6owFWr2Xxyrby9h84dCvuYKMmHGro5WJM0SH0zJY7OOJf_Ys5G9QOXqq-WkTagls2LSLwEyRc-LmMvJfpcCrebC4RKoMfp3uhIMRSQS6yLUFkfBGrfaYJpcuBXgAojbKRmMQuBVKecwzsKBe6RXxsXB5Qi8bCy1dHw1m5SUzcCFd4qhO0wR3DU9mRlvzZei4Y8qNQtTrtzQrp1Gs87b-HTTzHTn8WghBF5ZPE0JHPuRA8gMvne06oD7zPgVF0gBc9aNze0L2TMdDp49snGsRfFZiWFAxRyPgZzMjU_m0x_pRFIjRF4KDVAgPPZI9tdvHH55n3u-2Th4XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب تاکتیک های ناشناخته ای رو کردیم که سبحان الله!  انصافا بیرو عالی بود و ثابت کرد یک گلر خوب می‌تواند یک تیم نابود را نجات بدهد!</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/17881" target="_blank">📅 00:49 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
