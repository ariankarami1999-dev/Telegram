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
<img src="https://cdn4.telesco.pe/file/KmxajTR05LXVpvXVrAnJIfiEwi0FfwkckQI-kK26T89es_K9l2_tvx8_3VVtZr7jxvs_3MPmUTnSFFgS9OnPB-1gFjjC-D5c3NJo3KX33Y3LQ4Kw_7EsVsf8S3TGtXl0vDvV1pFs7nkc6o7LacvsB90gKCUI9DIeEVwKjHqWXA8idpN-t3oCu2AONrZlNV1pGjizWgcOtzFLekBBZpdMjEz65bhXTs_p-Th6yGcU0TSs568DaBel0Ls1M-l_ZKEAF6jsHz-Xe0OEB3vH7_7QxA9o8a6lc5iVKR-TJYlSa5LafuuULm1Tl6FERytOFhl2oI7dXzZgS-ldxtSLqX9ZPQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 16:41:52</div>
<hr>

<div class="tg-post" id="msg-17979">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVyqK4-UrdCOf0oUp6gzGeP72ehIZ6Y1lK7TIO4LYnfkf-QiXWGHp_LMp3mTrN469lsEHZ9hUvzGziNplRu_BD07Evgo4hTHmhHzxZKyCQU9tPGeYIFRfA1qWMaeowNEwhVsGrD5Dz4JzVTbzC4Q-AujprQPLo5qPFTn3n3FlThjSsiurSAfMr_W_d6suC_KjoU_nXZAl1YlCywVFBcrtQwtJ9dCGMxB6pCL1XQnhbd-0MotQ06TJrkW-Zei5fIEsbESAPtUoizwbcfYmsazOahhFQTB2W3KhWT9mMQpKIS_v5V_qZ1_A9k2oWEEj77kFks9DjqmMwlwl0WoVQw_BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وال استریت ژورنال، ایران ۳.۸۴ میلیارد دلار را از طریق صرافی رمزارز CoinEx منتقل کرده تا تحریم‌های آمریکا را دور بزند.</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/SBoxxx/17979" target="_blank">📅 15:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17978">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMILITA CAMP</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIg5QR2YecHWu_ffip9_CYTDoz7LLrHzZMxfiEkruwYqkp6-oVrzMHoReIvmTfzCXPHVk76pWmp_jJf7f9YdFSDOxiru8TVVp-OGULKKVNYhFQQephte5L6V2puf7J_ffKrAlI18Aaif_1YTU9sWN03dRN9HRyCu-35CqCwgkNAT2PmfYLvNWEs2UR4KFyu8synf4-R3kl0gHN9TsxoDsLdKjVmJIE3haKneA7r4bF5QuEeV9LYR4ER3SY1zc-X4yrWzWly7Ad99ji1JF2v8McLNKIj2b4bz7Ftm3QLgBdXdFhBITDtwJYSAXL_BF2dRWEF0TYhntlKihHGfanCjnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">● این میم در مورد مذاکرات ایران و آمریکا توسط خیلی بازنشر شده.
@Milita_Camp</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SBoxxx/17978" target="_blank">📅 14:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17977">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پس از آنکه عمان اعلام کرد که یک کریدور دریایی در جنوب تنگه هرمز ایجاد کرده سپاه این بیانیه را منتشر کرده است:
🔸
ساعاتی قبل بدون اطلاع و هماهنگی با جمهوری اسلامی ایران از طرف برخی مراجع مسیر جدیدی برای تردد کشتی‌ها در تنگۀ هرمز اعلام شده که این مسیر غیرقابل…</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/17977" target="_blank">📅 12:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17976">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SBoxxx/17976" target="_blank">📅 12:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17975">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مسکو با فروپاشی بنزین روبرو شده است.
پهپادهای اوکراینی عملیات بزرگترین پالایشگاه مسکو را مختل کرده‌اند  و این واحد تا سال ۲۰۲۷ تعطیل شده است، - رویترز</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SBoxxx/17975" target="_blank">📅 12:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17974">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">به
گزارش وال استریت ژورنال، ایران ۳.۸۴ میلیارد دلار را از طریق صرافی رمزارز CoinEx منتقل کرده تا تحریم‌های آمریکا را دور بزند.</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/17974" target="_blank">📅 08:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17973">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دو سناتور جمهوری خواه با تغییر رأی خود از لایحه محدود کردن اختیارات جنگی ترامپ، باعث شدند که لایحه کاهش اختیارات جنگی ترامپ لغو شود</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SBoxxx/17973" target="_blank">📅 08:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17972">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دو سناتور جمهوری خواه با تغییر رأی خود از لایحه محدود کردن اختیارات جنگی ترامپ، باعث شدند که لایحه کاهش اختیارات جنگی ترامپ لغو شود</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/17972" target="_blank">📅 07:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17971">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ درباره اردوغان :
او دوست من است و از جنگ دوری کرد.
می‌دانید، او کاندیدای اصلی برای ورود به جنگ با ایران بود.
شاید در کنار ایران، چون همانطور که می‌دانید، طرفدار  اسرائیل نیست.
و من از او خواستم لطفاً دور بماند، و او این کار را کرد.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17971" target="_blank">📅 00:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17970">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506e64b21.mp4?token=ppAT-bTNjwYSS0kKycQXHLa667v2bH8QIp460jmuk3qaYIshCrA6CjTfFN1gXgdcZksqT1S7hrU7WzpFCwnLL1ui_z9cWi9dnkjbjBUimr97YVRt7OMlAuHdMyvDaf_6rfMkcQ91tbAczksXoiaYa21TeOsqNcoLvhjjIjsW-NqG7-p7IwNeHYo1eUNvoC1ioHciDx_Uv-0Wl3K60pkcHd1QRFAZ20Zk5bAxqUBQnIDgoIMRg_dpPyVqej2Y_wcA-rZHjDdFFoTjrI0M3rNGTF1t8xlnYXpuiyC23m7xjOcZ9VEO65JYCY-5Ulm6K1D6MTWoNunhMQEjaTeAVcO5cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506e64b21.mp4?token=ppAT-bTNjwYSS0kKycQXHLa667v2bH8QIp460jmuk3qaYIshCrA6CjTfFN1gXgdcZksqT1S7hrU7WzpFCwnLL1ui_z9cWi9dnkjbjBUimr97YVRt7OMlAuHdMyvDaf_6rfMkcQ91tbAczksXoiaYa21TeOsqNcoLvhjjIjsW-NqG7-p7IwNeHYo1eUNvoC1ioHciDx_Uv-0Wl3K60pkcHd1QRFAZ20Zk5bAxqUBQnIDgoIMRg_dpPyVqej2Y_wcA-rZHjDdFFoTjrI0M3rNGTF1t8xlnYXpuiyC23m7xjOcZ9VEO65JYCY-5Ulm6K1D6MTWoNunhMQEjaTeAVcO5cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17970" target="_blank">📅 00:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17969">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ادعای ترامپ: ایران امتیازات بزرگی می‌دهد  جنگ خیلی خوب پیش می‌رود. همانطور که می‌دانید، ما با اختلاف زیادی در حال پیروزی هستیم.  ایران امتیازات خیلی بزرگی می‌دهد. خواهیم دید چه اتفاقی می‌افتد.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17969" target="_blank">📅 22:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17968">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ادعای ترامپ: ایران امتیازات بزرگی می‌دهد
جنگ خیلی خوب پیش می‌رود. همانطور که می‌دانید، ما با اختلاف زیادی در حال پیروزی هستیم.
ایران امتیازات خیلی بزرگی می‌دهد. خواهیم دید چه اتفاقی می‌افتد.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17968" target="_blank">📅 21:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17967">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">#USOIL — W  در تایم هفتگی به کف یک کانال معتبر هفتگی می رسد و از اینجا ریزش بیشتر توجیه بنیادی ندارد.  این یادداشت را هم بخوانید.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17967" target="_blank">📅 19:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17966">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbtZtwlQKcpZRI2NQbzWdpP-2-7ef0LUCa7GxYN9Py58GNXlyglfIskS9jRXpR7Cm3k2dI-dfYwAaJjwGmlJVjdrbRsSwf_MgqoLnAt0QkPWvxOZSUWISv2ufEpHGsUHGNzDE2asV2tvAOea0zuu6O6TVzuS7RX_RWyuOp0ADCVOECm8mxm4xkyER2o6iDg_KzXKA1RyOQmiRu64Laho_W0JGECsRlU5kwyanUSyJ2IjEANdg8pckI2O_Ol6x7qT0Llh_dgWegvKyx5ePb4VTZSotINX1PAic0lEjS-aeck4UDs_ipwjFau10Vs1wpbzfPyTv9lAMvgD3Mn_axoiIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — W  نفت همه رشدی را که به خاطر جنگ ایران تجربه کرده بود برگشت و اکنون در حال نزدیک شدن به نقطه شروع حرکت است و زین پس دیگر هیچ ریسک پرمیومی برای جنگ در قیمت لحاظ نشده.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17966" target="_blank">📅 19:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17965">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دلار 166 هزار تومان!
بخشی از این رشدها به خاطر کثافت کاری ها و باج هایی است که به طلاداران داده می شود. وقتی اونس سقوط می کند دلار را بالا می برند و بر عکس.
تارگت های 240 و بالاتر همچنان در دسترس هستند البته اما  این رشد دیروز و امروز برای این است که گفته شد.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17965" target="_blank">📅 19:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17964">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F99pQzLYCkgHK5Sq-vz7ShK_1iF2lgzJTNxSrz9uRzdNAH0oxB0w8_GdBtb_snQ-teQeL_5_yQKzlY2_xC7bzSY5hiUPP-g8iSzHb_Kpwy9pT2LFoUs-fx8m-vOAUmee71h8d4wrXoDmLWM9c2K9-YrbWKpluA6pMZh3r629ufdoBY5EZEaDzTMrgSuhHS30i-KRnjDjFmkJ__mPHBOwTbz3L-QW9xPOO3EVn0hdQVsREYTuqWHhZESSDOJbUEFBDn7ekXBZk-U-BwqYP7aWpk2q9o-ph-jBEPeO0XgXiOOp2_MlxZvi82WxfUr4RU-eAuD_BQgpa0aEB5GLUZJUzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  در محدوده مشخص شده می شود به دنبال موقعیتهای خرید باشیم.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17964" target="_blank">📅 19:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17963">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رئیس‌جمهور ایران مسعود پزشکیان رسماً نخست‌وزیر نارندرا مودی را به شرکت در مراسم تشییع و تدفین چندروزه رهبر عالی‌رتبه آیت‌الله علی خامنه‌ای در ایران دعوت کرده است.</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17963" target="_blank">📅 16:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17962">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رئیس‌جمهور ایران مسعود پزشکیان رسماً نخست‌وزیر نارندرا مودی را به شرکت در مراسم تشییع و تدفین چندروزه رهبر عالی‌رتبه آیت‌الله علی خامنه‌ای در ایران دعوت کرده است.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/17962" target="_blank">📅 16:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17961">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رویترز:   سپاه پاسداران انقلاب اسلامی سلول‌های مخفی در عراق ایجاد کرده تا حملات پهپادی علیه کویت، عربستان سعودی و امارات متحده عربی انجام دهد. این سلول‌ها از جنگجویان شیعه نخبه عراقی تشکیل شده‌اند و مستقیماً به سپاه پاسداران گزارش می‌دهند؛ بین آوریل و مه حداقل…</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17961" target="_blank">📅 16:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17960">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حقیقتا «الکسیس میانرودان» لقب شایسته ای برای عراق نیست؟!  تل آویو - اسرائیل برای پشتیبانی از عملیات هوایی خود علیه ایران، یک پایگاه نظامی مخفی در صحرای عراق ایجاد کرد و حملات هوایی علیه نیروهای عراقی انجام داد که تقریباً در اوایل جنگ آن را کشف کردند.  به گفته…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17960" target="_blank">📅 16:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17959">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQBJ1VkJNLok2v2eFdS-8sLNtuoBsyFsBP3K-WdRbKB8TgvMA-G02YOKrDPqceUIQnQa7SscuwYy3TLfzMR_AxvMWIm1vWsuynZ5SbjRQiU2fqSn3HLrhY8sb3Ep7fpjC-2133uBEhiPjk5_5rQvzVnWKX_a7swPcmFctM7r6ITFb8mibyON85a5Tueva5CYeSFUEsnhmAWzxWnjpT1Q0hfxglgC0hwNLh89a29aLEKjvPSrLmF3M0hR65ZeZX41BJK0AmWXtitTXsmb7basCejiBqQZwjj2yyziMifklMxuXIp69Lngm28Pg6iiApyW11bbmaUP3oY7gr1l3-kzPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#DXY — W  پس از یک سال رنج زدن، شاخص دلار به صورت کوبنده ای رهسپار تارگت های اعلامی شده.</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/17959" target="_blank">📅 16:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17958">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcSq5lJemREuz66Sqdhsn4ijBUQopOrBA0VThevYtiqPsCinHRbIyVgjmtNL2sE2zOw8WKtsjXSRlBC5tXiFDXrfz27XpiZ0TKeQFZLlpkT1LODrGi8zzTqVkcbNKqXwhtY99SR7BvUnnNcr0g3jDn8YBKKGfAdZnPKIqkEWs_dzk530_SAobxYNb5rHEq5FcrcngxyjPz_BoQvUBuiwjZrlo1auiOqMREZj1xyanENN-KVvFStMY54KBt8H4jI1_YsvoRy2vIlEjMhg6IybESGRomjUil-iInieI54nljb9xiE53CcLAqMdfhBAZg6lFpSR_3ItVpTSE9HhctH3NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#DXY — W  رسید به کف کانال هفتگی!  از این هفته فروش دلار که ممنوع است هیچی، خرید هم در دستور کار قرار می گیرد.</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SBoxxx/17958" target="_blank">📅 16:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17957">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ: ۵۰۰ میلیون دلار در ابتدا برای خرید کالاهای آمریکایی به ایران داده می شود</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/17957" target="_blank">📅 15:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17956">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/925922fd6b.mp4?token=l1iTPl0PPQqEu8eF7y8kC1Uhfy7iZnhJHURVj2BUOakweuSYZ2uI9uc14OQOJjJqtoLM2Bp2UGYK7VoRIPQA5BoT6SmWoxdqP2W_BHWHsaLTaCKO5amtLik0l5SWKlKutjDBIrPeVGvINt5kydPekLGVh9AlmdErLiYzzgM3g92b0NCBgxh_nQoAElsBJlt_f6SgoTybraZtLK0jQkiyrBLGvYxD5RZ1IysJns15XqZne6E2eedMI0RVd4hv-R2aoYcdvnOWHh6ZAUTnFpIdwmfjLSn5merJGElh7FeYrH8V9FWZJChMITnMCFQTbxyhQRWkTTPNrokWWEhXI1lHHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/925922fd6b.mp4?token=l1iTPl0PPQqEu8eF7y8kC1Uhfy7iZnhJHURVj2BUOakweuSYZ2uI9uc14OQOJjJqtoLM2Bp2UGYK7VoRIPQA5BoT6SmWoxdqP2W_BHWHsaLTaCKO5amtLik0l5SWKlKutjDBIrPeVGvINt5kydPekLGVh9AlmdErLiYzzgM3g92b0NCBgxh_nQoAElsBJlt_f6SgoTybraZtLK0jQkiyrBLGvYxD5RZ1IysJns15XqZne6E2eedMI0RVd4hv-R2aoYcdvnOWHh6ZAUTnFpIdwmfjLSn5merJGElh7FeYrH8V9FWZJChMITnMCFQTbxyhQRWkTTPNrokWWEhXI1lHHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خارجی ها مخ شان سوت کشیده و فکر می‌کنند بیرانوند راننده یک تراکتور است!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/17956" target="_blank">📅 14:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17955">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یسرائیل کاتس، وزیر دفاع اسرائیل:
«حتی اگر از سوی آمریکا درخواستی مطرح شود، ما از لبنان عقب‌نشینی نخواهیم کرد.
دویست هزار نفر از ساکنان [شمال اسرائیل] هنوز به خانه‌های خود بازنگشته‌اند.
ما تمام رهبری حوثی‌ها را از بین برده‌ایم، به‌جز عبدالملک الحوثی که در تونل‌ها مخفی شده است.
اگر او در تیررس قرار بگیرد، کشته خواهد شد.»</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SBoxxx/17955" target="_blank">📅 14:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17954">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0kuEqI0PFvvuEOizEhyf3nvK1vgsW69tIS_xs0bGzKI9QMAtq1kYBS9crzVvXVrdjTxcUOlQcIAJcIdymW4LqRYDHfDr5182L9OYeLdCoqVENCu2daL8w16wbozys_B77GpDyM9V6XWo3Pnza6_NwHv55TxNie1BjrqIN5ZK30syt3E6enwfUiPQuutWGB836fGe_3PUWF8ta2rtMnmHyOpKP9lqYUxs2oFXnRBeIPE0xfQ6nBu-RkE-Z35pRxFg601x7SWPSOYsSCMGQhnkdJuumvHMg_AAgMphT2DRAmFloToQKGfw_vN3zousqLOJANa7ddKrJx68kwrVgJGow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17954" target="_blank">📅 14:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17953">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1hS8bP0mxgFiLGa6X_Na1wS2lf9-kEEd89cTmf5BOUtCCMzWnKLPdj21zNNurpxIb_b3HR7Qk7AECt-R6OY8RqSgadwyxT2A5qTUoBkVX1l525q9GPd0lS9dy0hJ90VkuF_ocwh-_pZBlvVy8RArs3985TVipks9UAn6ObsUbTzNcpEf5znlFF6XUxV_PBYJhJfDFCfq9tXcIi9hM9yQldXoMAkj26YEyz2iVQTK509qWRoGTF15ke6nDSaJL6416ZML-O6YF0kCqYcISPhfZytlfsQrnlj7jVpOB9Y0mecrYNNSp9euJbhvDa22sak7FkvD2TnAwL5cNG5tbX1kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#طلا
بر اساس نمودار، احتمال ثبت یک کف دیگر پیش از پرواز دوباره قیمت بالا است.
بهترین محدوده خرید میان مدت 14.2 میلیون تا 14.9 میلیون است و تارگت حداقلی 29 میلیون تومانی فعال خواهدشد.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/17953" target="_blank">📅 12:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17952">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">هاآرتص، با استناد به منابعی در ارتش اسرائیل:  ناامیدی و احساس ناتوانی در میان افسران در لبنان به دلیل عدم قطعیت ایجاد شده توسط اقدامات نتانیاهو و کاتز.</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17952" target="_blank">📅 12:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17951">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">برخلاف تصور رایج، «لابی کشاورزی آمریکا» یکی از قدرتمندترین ائتلاف‌های ذی‌نفع در واشنگتن است. اما این لابی یک سازمان واحد نیست، بلکه شبکه‌ای از انجمن‌های کشاورزان، اتحادیه‌های تولیدکنندگان غلات و شرکت‌های بزرگ کشاورزی است.  نکته جالب اینجاست که این لابی، برخلاف…</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17951" target="_blank">📅 10:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17950">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">توییت ترامپ در مورد ایران:  با وجود اعتراضات و اظهارات نادرست آنها، همراه با تبلیغات مکرر اخبار جعلی که همه تلاش خود را می‌کند تا پیروزی آمریکا را کوچک و بی‌اهمیت جلوه دهد، ایران به طور کامل و جامع با بازرسی‌های هسته‌ای در بالاترین سطح برای آینده‌ای نامحدود…</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/17950" target="_blank">📅 10:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17949">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">هاآرتص، با استناد به منابعی در ارتش اسرائیل:
ناامیدی و احساس ناتوانی در میان افسران در لبنان به دلیل عدم قطعیت ایجاد شده توسط اقدامات نتانیاهو و کاتز.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/17949" target="_blank">📅 09:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17948">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتحلیل و رصد</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0802e26a.mp4?token=Uy09yoe_9VCb6kuDkE2er7tNUaqO-ZLR2sRDvWbLcyrs47Zpq-SfBtgoUVnmY7fxvbYzTAav3y5-jK5gVbpC7kBNiqAGQ19aBp7GqeJSybHiUgzkRj7A9PYuc01VftBrQif6j-UceraBe3e4Op6cjjrE2ZhrcRLVp6mSteyECLH1aJ3LxXd2dIdkkvWAe5BEfu7OBftRB7ke5ixf5n4EovSr4S6cm0BPwLYAj_JVDxidqX4feRex6xSy-xO6qA364peTnIhm_edRmN4Xwj_evd96JYNYCLORcwhLfJ50U2If3TL3lCxGLvk_vkscEwoTemuu2eW4GfGOxGFslHoxzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0802e26a.mp4?token=Uy09yoe_9VCb6kuDkE2er7tNUaqO-ZLR2sRDvWbLcyrs47Zpq-SfBtgoUVnmY7fxvbYzTAav3y5-jK5gVbpC7kBNiqAGQ19aBp7GqeJSybHiUgzkRj7A9PYuc01VftBrQif6j-UceraBe3e4Op6cjjrE2ZhrcRLVp6mSteyECLH1aJ3LxXd2dIdkkvWAe5BEfu7OBftRB7ke5ixf5n4EovSr4S6cm0BPwLYAj_JVDxidqX4feRex6xSy-xO6qA364peTnIhm_edRmN4Xwj_evd96JYNYCLORcwhLfJ50U2If3TL3lCxGLvk_vkscEwoTemuu2eW4GfGOxGFslHoxzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">.
🟢
وقتی دکتر مسعود، نمی‌تونه از کاراکتر دوره جَوونی‌ش فاصله بگیره!
پزشکیان [در سفرش به پاکستان] به نشان دوستی یک درخت تو اسلام‌آباد کاشت که رسم پاکستانی هاست.
ولی نکته جالب اینه که هی شهباز شریف نخست وزیر پاکستان اشاره میکنه مسعود جان بسه کم خاک بریز. نمادینه ولش کن. ولی مسعود هیچ رَقمه گوشش بدهکار نیست و فقط بیل میزنه.
@tahlilvarasad</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17948" target="_blank">📅 09:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17946">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⛔️
کارشناس اسراییلی تشریح کرد: ۸ کانون تنش بین ترکیه و اسراییل؛ ترکیه ایران جدید است  یک کارشناس اسراییلی با اشاره به اینکه تنش بین ترکیه و اسراییل به بالاترین حد خود رسیده است، به بررسی ۸ کانون تنش بین طرفین پرداخت.  ایتان لاسری بر این باور است که اسراییل…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17946" target="_blank">📅 23:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17945">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نخست‌وزیر پاکستان، شهباز شریف:
«کشورهایی هستند که می‌خواهند توافق را مختل کنند، و من می‌گویم که بدون ایران نمی‌توانند موشک‌های بالستیک داشته باشند. استانداردهای دوگانه قابل قبول نیست و منطقی نیست که برخی موشک‌های بالستیک داشته باشند در حالی که ایران از آن منع شده است.
یادداشت تفاهم (MoU) به مسئله موشک‌های بالستیک ایرانی اشاره نکرده است».
«این یادداشت تفاهم به موشک‌های بالستیک اشاره نمی‌کند. هرگز روی میز نبود؛ هرگز در دستور کار نبود.
طرف ایرانی هرگز نخواست حتی درباره آن بحث کند».</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17945" target="_blank">📅 20:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17944">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🟢
پاسخ به توهم برخی درباره شکست احتمالی نتانیاهو</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17944" target="_blank">📅 15:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17943">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">توییت ترامپ در مورد ایران:  با وجود اعتراضات و اظهارات نادرست آنها، همراه با تبلیغات مکرر اخبار جعلی که همه تلاش خود را می‌کند تا پیروزی آمریکا را کوچک و بی‌اهمیت جلوه دهد، ایران به طور کامل و جامع با بازرسی‌های هسته‌ای در بالاترین سطح برای آینده‌ای نامحدود…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17942" target="_blank">📅 15:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17940">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VaJr7h6OaR6w2EmfuQz3BRC4xtxTOg7oB9sXvkNqhucakvBSNaSanw8Zu8ip2Zuh6qavbqKe2uLmUub07wECxZpfZxFajt-AuVeO4T7lKn27ZaEmw_LVpSZidP1w72gxiB7iffzDbZUXV4_6iPVKmGxWxlzXulhsvduBACnKJz5hvNTyLhdd9OvWGpWjdyUOkE4DQzZuaSd30lyvOZJumNGAs7y5cdtz6BY-roKhURbc9Dw6RMUQQ1Dmc07jTZ0VUJM_IipxUysgbVirAzY1d_dZctEL9c5OVwOtK7FuOBap5FTIN0-uMAdJGM2t5rClzCNoRZht0g-EsCPCKJ79IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hxWMYJNWISDkBSfkc00wp3_RT5qUXbe_l3vBPawF5H85f8jXYfUJWpnYHf2w6Dg-S7PqD15b-voJqcX_QODWLibtyEMOV1EXwVgpVVAbelRjN7wf2h6SilsA2kf1ZDIGpfFHsyEXl0PotUZ4s7jdG_NxvFcMELq7DzMdFWjdWOumH1IwaU9v9FxDPSdwYWQeyke1FLWlhC2c2RCQsSyyDb9SB-to8hJ3i-a5Xy98yd1zwkc8MfGdy-19Ge52qq96dtrbpaRwJAxs8N-nDVaUx5gPpyUKwqPpIQGASZmfPCUTjc0iB17azwtNc2Gzy86fC0TWH8o2hQn_R4xeI1QQbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر چه جلو میرویم داستان رابطه مسعود با شهباز
دارک و دارک تر
می‌شود
پناه بر خدا!</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17940" target="_blank">📅 15:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17939">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17939" target="_blank">📅 15:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17938">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">توییت ترامپ در مورد ایران:
با وجود اعتراضات و اظهارات نادرست آنها، همراه با تبلیغات مکرر اخبار جعلی که همه تلاش خود را می‌کند تا پیروزی آمریکا را کوچک و بی‌اهمیت جلوه دهد، ایران به طور کامل و جامع با بازرسی‌های هسته‌ای در بالاترین سطح برای آینده‌ای نامحدود (بی‌نهایت!!!) موافقت کرده است. این امر «صداقت هسته‌ای» را تضمین خواهد کرد.
اگر آنها با این موضوع موافقت نمی‌کردند، مذاکرات بیشتری صورت نمی‌گرفت! بر اساس این و دیگر امتیازات عمده‌ای که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و هیچ محاصره دریایی بیشتری اعمال نشود. با این حال، همه کشتی‌ها در محل باقی می‌مانند تا در صورت لزوم محاصره دوباره برقرار شود، که در این مرحله بسیار بعید به نظر می‌رسد.
پول و/یا تحریم‌هایی که خزانه‌داری آمریکا آزاد می‌کند، در حساب امانی تحت کنترل آمریکا قرار می‌گیرد و صرف خرید غذا و تجهیزات پزشکی، به طور انحصاری از ایالات متحده، از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما خواهد شد.
این‌ها چیزهایی هستند که ایران به شدت به آنها نیاز دارد. این یک بحران انسانی است و من احساس می‌کنم لازم است که اکنون کمک کنیم، قبل از اینکه خیلی دیر شود. مذاکرات به خوبی پیش می‌رود!</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17938" target="_blank">📅 14:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17937">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🟢
طبق اعلام معاون اول مسعود پزشکیان ، در راستای برگزاری مراسم بزرگداشت رهبر فقید جمهوری اسلامی ایران ،  13 و  14 تیرماه استان تهران و 15 تیرماه کل کشور تعطیل خواهد بود</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17937" target="_blank">📅 14:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17936">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⛔️
دولت ترامپ ، دسترسی به 2 مدل هوش مصنوعی آنتروپیک را برای کاربران غیرآمریکایی مسدود کرد</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17936" target="_blank">📅 12:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17935">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپارادوکس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c175d38c15.mp4?token=cAAn2IP2LMfZg4g0crRHaxGFaE_zhzohh9wQyU5Dg09nsnqgfzPGLZvpGwS9s-wjynltM3FTB4MB8CMPzGUG98HcItUTLEr5VQ0erhPAyOGsaKzTSYgiowyDi4MCirLMvX5lbdjoGqtERO6GzhIDNHV_fPD2gjIT4PG7TPn2qLUOXVs5ONkej-sb69BzZSbwkQRwTL7eK4iq8nn8ZW3iiYpljf9jrwCB-Jnk-i_4Hh5XYRT3X8iIyHqgvHstxQlWAW6oai2D3cL11dme7KmKj6fBy0E0-mkZrntqsFwirW4u0q6TXuxBI9LjOEve5Un2q4NnAj_U4Ut_H21xyNL6w3FVDgUlVCRD4Z3Yowtyv4nzFp6amV7dLOwnFvAbUBSL8Xbn3RqkXzK6XU7m2t0lqZE2lacY1IhHdLpDMieyYJn6oXys8ZzINT-P9hO6FE2Pf1NzR0rjxkxzsjsSLZzKx8g6UYEXCUtSTJlHSF4bZQqOXjqWF2jkzrfc6YbWt9JKABdnNGFIPXS11XSu7YfDNkJMXoeBbzLJLnSDianbeehi8FrgX4xLhrBflQDo3nDPxeBaI9QwZtCvkCx5fHlij5_ifJ2L_LeC94KFB5bW8XPd_w9VfPHZDJ0tGqYX4IdkUCnPgbvzsNyiJlngGdvumXA4Zl1fJgB1sjacySGQMqM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c175d38c15.mp4?token=cAAn2IP2LMfZg4g0crRHaxGFaE_zhzohh9wQyU5Dg09nsnqgfzPGLZvpGwS9s-wjynltM3FTB4MB8CMPzGUG98HcItUTLEr5VQ0erhPAyOGsaKzTSYgiowyDi4MCirLMvX5lbdjoGqtERO6GzhIDNHV_fPD2gjIT4PG7TPn2qLUOXVs5ONkej-sb69BzZSbwkQRwTL7eK4iq8nn8ZW3iiYpljf9jrwCB-Jnk-i_4Hh5XYRT3X8iIyHqgvHstxQlWAW6oai2D3cL11dme7KmKj6fBy0E0-mkZrntqsFwirW4u0q6TXuxBI9LjOEve5Un2q4NnAj_U4Ut_H21xyNL6w3FVDgUlVCRD4Z3Yowtyv4nzFp6amV7dLOwnFvAbUBSL8Xbn3RqkXzK6XU7m2t0lqZE2lacY1IhHdLpDMieyYJn6oXys8ZzINT-P9hO6FE2Pf1NzR0rjxkxzsjsSLZzKx8g6UYEXCUtSTJlHSF4bZQqOXjqWF2jkzrfc6YbWt9JKABdnNGFIPXS11XSu7YfDNkJMXoeBbzLJLnSDianbeehi8FrgX4xLhrBflQDo3nDPxeBaI9QwZtCvkCx5fHlij5_ifJ2L_LeC94KFB5bW8XPd_w9VfPHZDJ0tGqYX4IdkUCnPgbvzsNyiJlngGdvumXA4Zl1fJgB1sjacySGQMqM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17935" target="_blank">📅 11:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17934">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuKD9LzOCdZdTPoe_nWJFCNFqddj6E6qWVPvtQ8p-C0Ewqx3KGZXOfZFzhKH18dXaLxiRx5vt-dsp9NeYUp82QbU6is46En_1EgyTPe6EI41sQARnLBUrclxvOwX3LVQ8XcXGBfwEGzHIx-5vza07oGIeNsRD9eo8QVTv5Kx8RSD8TcMJ-a4DASEaedlm0ncb0gCjRTYTEFBU65Y-qwcZkuN0LaRbzUNoiEmDa_TwgXAKeahgZcV7x--6qTKbeCEl4WFqfWJpQYu44Aq1HsncxLqmK42AqBWmxHBHb2BxT_KQQG6EVzZcJXJL052A9ty4HS7WpfYVlatG-t7v-w0Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت استاد!
از تبیین کوانتومی آفرینش و پایان هژمونی دلار با ظهور بریکص رسیده اند به رفع نیاز جنسی با دوغ!</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17934" target="_blank">📅 09:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17933">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">این را در دیدار حضوری با تیم ایرانی گفته اند !  پس دارند میگویند اگر کشتی از بخش جنوبی تنگه هرمز عبور کند، عوارضی پرداخت نخواهدکرد  اما اگر از بخش شمالی تنگه که تحت مدیریت سازمان معظم تنگه خلیج فارس ایران است عبور کند باید پول عوارض بدهد!  خب شما به عنوان…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17933" target="_blank">📅 07:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17932">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این را در دیدار حضوری با تیم ایرانی گفته اند !  پس دارند میگویند اگر کشتی از بخش جنوبی تنگه هرمز عبور کند، عوارضی پرداخت نخواهدکرد  اما اگر از بخش شمالی تنگه که تحت مدیریت سازمان معظم تنگه خلیج فارس ایران است عبور کند باید پول عوارض بدهد!  خب شما به عنوان…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17932" target="_blank">📅 07:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17931">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وزیر خارجه عمان:    به قانون بین‌المللی و تضمین عبور امن و بدون اخذ عوارض از تنگه هرمز پایبندیم.</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17931" target="_blank">📅 07:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17930">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نخست وزیر و وزیر امور خارجه قطر در مصاحبه با الجزیره:   آنچه ایران در طول جنگ با ما و برادرانمان انجام داد، غیرقابل قبول است.  اجماع خلیج فارس برای دستیابی به دیدگاه مشترک برای گفتگو با ایران برای حل مشکلات وجود دارد.  ما می‌خواهیم شاهد همکاری ایران با کشورهای…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/17930" target="_blank">📅 07:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17929">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoWYM_ke3N95vBCC7Fku9paA54xEFtz_aAC8Y1SwYamJJhvDA_SBWCEJOttYZFtS88UEiMS0RySy7fDnbRSyL4qLPJ3UJDRgBVTiVXlE18NmfRbkVaHCZNgWtySezCKHHgR925n7sHgmnuKP0EeZMX_jABQ3nqY68bFBZkDF4AB-TambI_22mtTYJVQ8_OzDuSvUJsbHx5h76p3uDp1CoSbBWj3APvfXnVoPsZs5nOgZW9hPpC7fnQmF1gs7fNPpJkH6IDHOwsMNZ5dLQXPiz2twXl1u8aNNYQ3mLudWU8SkbLjnXFE1opTMnIgfeCN_AmZIqJaw42t08ZUcf3mlLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی رئیس بانک مرکزی:  ما سالانه نیاز به‌خرید میلیاردها دلار مواد غذایی و دارو داریم پس چه بهتر که در ازای دادن پول‌های بلوکه شده آن را پرداخت کنیم. البته بخشی از پول را هم میتوان صرف کالاهای غیرتحریمی کرد. به هرحال این معامله با آمریکا برای ما سودمند است.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/17929" target="_blank">📅 01:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17928">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">همتی رئیس بانک مرکزی:
ما سالانه نیاز به‌خرید میلیاردها دلار مواد غذایی و دارو داریم پس چه بهتر که در ازای دادن پول‌های بلوکه شده آن را پرداخت کنیم. البته بخشی از پول را هم میتوان صرف کالاهای غیرتحریمی کرد. به هرحال این معامله با آمریکا برای ما سودمند است.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/17928" target="_blank">📅 01:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17927">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سرانجام کتابی که وعده دادم درباره پیوند ژئوپولیتیک و بازارهای مالی ترجمه کنم، به چاپ رسید.  به نظرم در این شرایط که چندین جنگ همزمان در منطقه و جهان در جریان است و تنشهایی که میتواند بزودی تبدیل به جنگ های دیگری بشود، فقدان وجود یک دیدگاه تحلیلی چهارچوب بندی…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17927" target="_blank">📅 01:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17926">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔹
شبکه ۱۴ اسرائیل :  بنظر ما ، جمهوری اسلامی ایران به سلاح الکترومغناطیسی دست یافته و با استفاده از آن درحال تاثیرگذاری دلخواه روی مغز ترامپ است - رفتار های دونالد ترامپ هیچ شباهتی به قبل ندارد</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/17926" target="_blank">📅 23:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17925">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔹
شبکه ۱۴ اسرائیل
:
بنظر ما ، جمهوری اسلامی ایران به سلاح الکترومغناطیسی دست یافته و با استفاده از آن درحال تاثیرگذاری دلخواه روی مغز ترامپ است - رفتار های دونالد ترامپ هیچ شباهتی به قبل ندارد</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/17925" target="_blank">📅 23:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17924">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDc2Do9JwymgpNLO-vp9YuNPBEAMR_CWeel9a3By9xXEXyQ6hmBwO4eGz185I4aXqORznIJRYUnhKEaa7NWG7K9bu2YykmFWEffnSoMFaG-3RuXEsFUbsYYd9DxmyvB_korgUdQT6soRBxZRujfd_nOa8bfq2wqBl9RL3-fxGF5xDieDtel_Wd8G0uu8CbTqA5r0I6dLJ2eRx3PvGWb0UxBoTlXvZSJm9CJlNFPemEDqJ5qng9sOplU8eBUrlPWaJjU2lsTURp81oN_9WGH-GZgKDnd4tWSMoap2Dxeii673VGO6OKyFw08QvpGRd_zUQXAlJrDckA_FlXGYtzypPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوستالژی هر ساله ما آغاز شد…
جای کیان رویگری خالی…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SBoxxx/17924" target="_blank">📅 23:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17923">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">المیادین: هیأت ایرانی تا زمانی که ترامپ عذرخواهی نکند و اسرائیل از جنوب لبنان عقب نشینی نکند، به مذاکرات باز نمی گردد!   ایرانی‌ها اکنون تنها خواستار توقف تجاوز نیستند، بلکه خواستار خروج (نیروهای اسرائیلی) از جنوب لبنان هستند.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17923" target="_blank">📅 22:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17922">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">هند قصد دارد موشک های کروز سوپرسونیک BRAHMOS را به ارمنستان ارسال کند</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17922" target="_blank">📅 22:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17921">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ:
همه کاملاً آگاه هستند که ایران موافقت خواهد کرد تا بازرسی‌های نظامی انجام شود تا «صداقت هسته‌ای» را برای مدت طولانی در آینده تضمین کند.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17921" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17920">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خوش‌چشم، کارشناس صداوسیما:
آمریکا خودش تاسیسات ایران را نابود کرده است و حالا می‌گوید در بازسازی آن‌ها سرمایه‌گذاری می‌کند تا در سود این صنایع شریک شود/ به جای خسارت دادن می‌خواهند ایران را استعمار کنند و ۵۰ درصد سود صنایع ایران را کسب کنند</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17920" target="_blank">📅 20:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17919">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مرندی:
🔻
ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و دیروز هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی‌به ایران صورت نگرفت</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17919" target="_blank">📅 20:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17918">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تهران توافق برای اجازه ورود بازرسان هسته‌ای به ایران را تکذیب کرد  خبرگزاری تسنیم ایران گزارش‌های مربوط به یک پیشرفت بزرگ را رد کرد و گفت که هرگز به بازرسان آژانس بین‌المللی انرژی اتمی اجازه ورود داده نشده است و ترجیح می‌دهد که هرگز نیز چنین اجازه‌ای داده…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SBoxxx/17918" target="_blank">📅 20:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17917">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJeMy5tkqfnC5Ymw-7rya5MQpvVUfGfywLDTiJl9MIgkbmiiXNfk7394muF9dl_IY9AEECY7nFAwF--5aXjb4xNiWfq489ABAVn_omz1rOF3ZYOD1IzdK-f45GKOxjrmic2uM2WA9Es8dJc9wLfW5yJ_JId0nxuQQNJtg8DcbClIqJET3Wfr65hg3AcKi6tt8IOYsZA6OD9bldNxyP9vzOV0x6FTWQeeg746Uos27zZjRHDt6ALRQtWDcf8TqqpHYaWmCzgy3CFIwOlKLANJeh_4CPkIkT25DrHzoYM90t93_ZjERvNjH7gYvsN7KyDvhv6y_6dM8PBL3hZwC9-rFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه ایران و انیران خواستار ابطال این پیمان هستند جز باقر!</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/17917" target="_blank">📅 19:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17916">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خردمند کسی نیست که بتواند میان خوب و بد، خوب را برگزیند، بل کسی است که توان تمییز خوب از خوب تر و بد از بدتر داشته باشد.</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/17916" target="_blank">📅 19:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17914">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ed9WU28VZsr2a5IfrHwQX8fDpufD8ZDWtBz-IRROnxabBIhzD3wO6bNHJxwHILE81BkF3ogX4lhWiMDw3DSIZWBmCm-989sPmkiS2_EvoG3vWmmr0THOMLdoj02bCOce-9SsQjpz1OwAGYK8FfEpmlc7y7FTNJUxr712_JbFSNp0Cv32LPZTm20Z40jCeF8XN_6E3kJrlyR6lInn5v79Nlpjj8-5DrX5KPprCSb17LOjpxTgDWRc86qSNtTr4rIm3aDUU_JMG0MtKTwr6ZnXfpzYIlfsA75XT0lNEj7L8ms1fWzk4lFMOBsYcID20lz_HUsy5PJ8PUNYl8T-qv74Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fKEErOLv2O3lXPz9wDdbvkaeEUjNiyfAcpDz58O6XGzT2jCvddXkFHOQyM2oMYrI7dSBxThzSxmMBGLWMg-FrMzTiD6eT1kZCBkbf-AUOvcF6kBTRkeCXR3nxNXfMBeFojixZmD3BL8YQrbeCOCcw8i61hgYORxZxZlWYhlvi0W8le38nnxvYg5X3rUmWw2Zp3IGkq1dEvhj7EdFFT34dQYD7L2vw3AXMVtR2-_8j_uNm5wLLQVAAzl6a8O5ImpToh5KJ_-VpXuUso_S1dPUCdpQPsIbSHESck3--CTCV8J54rk2R7Z1EnyfHBg9evCHjsyE2Bjw3um0mUL_ycydHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نمیگذاریم اسراییل بزرگ تشکیل بشود اما خودمان دنبال توران بزرگ هستیم و این نشان می‌دهد چقدر مادرقحبه هستیم.</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17914" target="_blank">📅 19:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17913">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیدالله کریمی پور</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-75aUnLgbwNfrbGwi333YPx_tDCr7wGHkR27MNv38_9AK3j2Pc38ALq0ZFRRPDQIvhB5ZjzzDt7wUrDVPiyEu02FpEVc__Rwj1-7R-dFtj6qCpuZqIZfvQG_wJHDgRENQj-yzuen1ZvTK5JZcgOvcwKkFbAGDwUZkImIxyhAPP6hdhaijhYy80guMI6TkX06hIW7Kw9NprGX2qUA_Ohq4WAkCAOuZTXEeagLifGKVqbtxkt_P4ZqbOCAdwjiRAajQ_wQVyjkh9F2sQnJoOFNVdcXOsMwtZqIj4ayD9ik4XJ_XRViSXwTDPPVK_OLB0HbtslaBrgqoyBdGecHRoagQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvnG82LV44xqpUmVdIOPmXryrWSh6N405YehdTlv4lN_ZybmA-fuf4Os0HMOErxVI9kjVCl-1ZbaSHK4SdaL1UQxHgk5MdyDTEaNaAw-pwXoYv4uJhj4S2thTt559o6QJ_HNLLMJNV0YH65yeBCdjBofpOqIk55KLcZCjcb0-jOwsS8kB1v-fsFOF70gyajpiE9KFLmay8kS1YGXhl_tcJE0w2g8yqnQtvucCprVRX8b_pCLmXKt8NfVF7H4xP7gEXO7MpVmVW-I3XPrVluGhMDgBnfb5FA7zLXKzQrLVvCPB7xZ1Az2eFDoqmlR_cBBsO8zzAxpTjAF1Olg9FVTWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ترامپ: دارایی های بلوکه شده ایران عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد  اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/17912" target="_blank">📅 18:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17911">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تهران توافق برای اجازه ورود بازرسان هسته‌ای به ایران را تکذیب کرد  خبرگزاری تسنیم ایران گزارش‌های مربوط به یک پیشرفت بزرگ را رد کرد و گفت که هرگز به بازرسان آژانس بین‌المللی انرژی اتمی اجازه ورود داده نشده است و ترجیح می‌دهد که هرگز نیز چنین اجازه‌ای داده…</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/17911" target="_blank">📅 18:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17910">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس، درباره زمان شروع بازرسی‌های هسته‌ای: احتمالاً این هفته، حتی از امروز</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SBoxxx/17910" target="_blank">📅 18:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17909">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انفجار در کارخانه گاز طبیعی مایع قطر؛ ۵۴ مجروح و ۱۸ مفقود  وقوع یک انفجار داخلی در مجتمع صنعتی راس‌لفان قطر که تأمین‌کننده یک‌پنجم گاز مایع (LNG) جهان است، ۵۴ مجروح برجای گذاشت و عملیات نجات برای یافتن ۱۸ مفقود همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/17909" target="_blank">📅 18:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17908">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjGUYP0WgCXy0_t28EXPpoO-j_zwNmFDbWJWJOfj4A2wgg0Y4OjjaPCEL2ppVQcL7TPHuCUDlcLoer7nJxKNAciukzBNgNh_F9Zute3p4-nvqfERVAUNnApbK-GVTi8jnOzIqBlJCmfvTZoq5NOTWBcEpRAAVqq9OTDSVXvMbRJ1vvMnokqnyTgamg9ceO055w04PiDMmG1V1lSpGBXR7eZAw-Zkv4na4Ezwmfl4EDGgmTdt3bW349Cr_3A2D0JXW0HDyjMCcXaSi585D5zlzZIp63I83-KqrWs1Jv7-mBTc3qhp9gBYyOf1vlWNn2ybZUvYVGX51BsJ8MBiB0jmow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نخست وزیر و وزیر امور خارجه قطر در مصاحبه با الجزیره:
آنچه ایران در طول جنگ با ما و برادرانمان انجام داد، غیرقابل قبول است.
اجماع خلیج فارس برای دستیابی به دیدگاه مشترک برای گفتگو با ایران برای حل مشکلات وجود دارد.
ما می‌خواهیم شاهد همکاری ایران با کشورهای خلیج فارس در سطح بالایی از اعتماد باشیم.
مقدمات برگزاری نشست‌های خلیج فارس در دوره آینده برای بحث در مورد امنیت منطقه‌ای در حال انجام است.
موضع اصولی قطر رد هرگونه تغییر در وضع موجود تنگه هرمز نسبت به آنچه قبل از جنگ بود، است.
چشم‌انداز ما برای تنگه هرمز، باز بودن آن و آزادی عبور و مرور از آن است.</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/17907" target="_blank">📅 16:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17906">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZT_U2M8nJA0PiXltcBs19pLNg4pKzPeTUXSx3c2W8l2nc87KkpOwaZFy4jjkaiG7U9vpvLuP-ETQ9rnBzYRN7pVEu2KHnrWyn_1-GMFDISZSlofR58W3smIYEbLTRkEQFerTJTL6Q2TdNBLHRIKk2kfM6PXgLpu31yycVV05_mKKn5mYgC7YF4wOe-gA4BpFrs_2iogkWUYGSCUCzoW4GJUT2vdBUMX6otw64loNNEqlXYly0c_K-wQ9V9MwcLGjGonxti9BTpVGlXWjmM0Mr3H0KzausNCdCWu5PvRCnb7hAQRti7RbCCFhHR15XRHReY8uFgn5IrRbehAM18moQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش احتمال وقوع رکود اقتصادی در آمریکا به ۱۵ درصد پس از توافق با ایران طبق تحلیل موسسه گلدمن ساکس !</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/17906" target="_blank">📅 15:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17905">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">معاون ترامپ: دارایی های بلوکه شده ایران عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد  اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/17905" target="_blank">📅 15:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17904">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کار خدا را ببینید که پاکت زاده های بدافزار «بله» آمدند کانال مرا بستند حالا تلگرام آزاد شده و بعید نیست خود بله و روبیگا فیلتر شوند!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/17904" target="_blank">📅 15:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17903">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">جی دی ونس:  آنچه جرد کوشنر و قطری‌ها و کل تیم انجام دادند، به نظر من، یک توافق کلاسیک ترامپی است. اگر دارایی‌های ایران آزاد شود، کشاورزان آمریکایی را ثروتمندتر می‌کند و به تغذیه مردم ایران کمک خواهد کرد.</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17903" target="_blank">📅 15:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17902">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">روزنامه وال استریت ژورنال:  آمریکا پیشنهاد داده ایران فقط برای خرید دارو، غذا و کالاهای بشردوستانه به ۶ میلیارد دلار دارایی مسدودشده‌اش در قطر دسترسی داشته باشد؛ ایران هنوز این طرح را نپذیرفته است.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/17902" target="_blank">📅 15:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17901">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">جی‌دی ونس: ایران مذاکرات را ترک نکرد؛ ترامپ به اظهارات تهران پاسخ می‌دهد
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، درباره گزارش‌های مربوط به خروج هیئت ایرانی از مذاکرات گفت:
«ایرانی‌ها تهدید کردند که مذاکرات را ترک خواهند کرد، یا دست‌کم چنین تهدیدهایی در شبکه‌های اجتماعی مطرح شد، اما آنها مذاکرات را ترک نکردند.»
او همچنین درباره واکنش‌های دونالد ترامپ به اظهارات مقام‌های ایرانی افزود:
«دیروز به ایرانی‌ها گفتیم وقتی وارد چیزی می‌شوید که نسل ما آن را "کری‌خوانی" می‌نامد، نباید انتظار داشته باشید ترامپ پاسخی ندهد.»
ونس ادامه داد:
«وقتی آنها حرف‌هایی می‌زنند که درست نیست، ترامپ هم به آن پاسخ خواهد داد.»</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/17901" target="_blank">📅 14:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17900">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس، درباره زمان شروع بازرسی‌های هسته‌ای: احتمالاً این هفته، حتی از امروز</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/17900" target="_blank">📅 14:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17899">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس، درباره زمان شروع بازرسی‌های هسته‌ای: احتمالاً این هفته، حتی از امروز</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17899" target="_blank">📅 14:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17898">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس: ایرانی‌ها موافقت کرده‌اند که بازرسان آژانس بین‌المللی انرژی اتمی را بازگردانند</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/17898" target="_blank">📅 14:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17897">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس: ما پایه بسیار خوبی برای یک توافق نهایی موفق گذاشتیم</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/17897" target="_blank">📅 14:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17896">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا ونس: ما پایه بسیار خوبی برای یک توافق نهایی موفق گذاشتیم</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17896" target="_blank">📅 14:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17895">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پس فرق این دوره ۶۰ روزه با بعدش این است که ممکن است بعدش آمریکا عوارض عبور بگیرد!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/17895" target="_blank">📅 14:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17894">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">— یک منبع اسرائیلی به سی‌ان‌ان گفت:
«اسرائیل در حال بررسی اعلام عقب‌نشینی‌های نمادین از مناطق جنوب لبنان است.
عقب‌نشینی‌های نمادین شامل عقب‌نشینی برخی نیروها از مناطق اطراف خط زرد خواهد بود».</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17894" target="_blank">📅 14:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17893">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">استارمر نخست وزیر چپگرای انگلیس استعفای خود را اعلام کرد.
دو ضربه بزرگ به چپ جهانی در کلمبیا و بریتانیا در یک روز!</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/17893" target="_blank">📅 12:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17892">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انفجار در کارخانه گاز طبیعی مایع قطر؛ ۵۴ مجروح و ۱۸ مفقود  وقوع یک انفجار داخلی در مجتمع صنعتی راس‌لفان قطر که تأمین‌کننده یک‌پنجم گاز مایع (LNG) جهان است، ۵۴ مجروح برجای گذاشت و عملیات نجات برای یافتن ۱۸ مفقود همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17892" target="_blank">📅 08:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17891">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">انفجار قطر بحدی شدید بوده که در بحرین دیده و شنیده شده</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/17891" target="_blank">📅 08:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17890">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بیانیه قطر و پاکستان در مورد آتش‌بس در لبنان چه می‌گوید؟
طرفین (ایران و ایالات متحده) توافق کردند که یک «واحد کنترل درگیری» را بین خود و جمهوری لبنان با میانجی‌گری تسهیل‌گران تأسیس کنند تا از پایبندی به توقف عملیات نظامی در لبنان طبق مفاد تفاهم‌نامه اطمینان حاصل شود.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17890" target="_blank">📅 07:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17889">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
عراقچی
:
🔸
میانجی‌گری خستگی‌ناپذیر پاکستان و قطر باعث پیشرفت‌های بزرگی برای پایان دادن به جنگ در لبنان شد.
🔸
همچنین تحریم صادرات نفت و پتروشیمی تعلیق شد، محاصره دریایی برداشته شد، برخی از دارایی‌های مسدودشده آزاد شدند و طرح بزرگ بازسازی و توسعه اقتصادی ایران اجرایی شد.
🔸
اولین آزمون واقعی: واحد رفع درگیری‌ها در لبنان</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17888" target="_blank">📅 06:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17887">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گوستاوو پترو، رئیس‌جمهور کلمبیا، نتایج انتخابات این کشور را به رسمیت نمی‌شناسد و اسرائیل را به دستکاری در نرم‌افزار انتخاباتی کلمبیا متهم کرد</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17887" target="_blank">📅 04:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17886">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">رییس جمهور چپگرا و معتاد کلمبیا امشب شکست خورد و جایش را به یک راست گرا داد.  قاره آمریکا در حال یک دست شدن است.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/17886" target="_blank">📅 04:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17885">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دونالد ترامپ، پس از ونزوئلا، اکنون کلمبیا را تهدید می‌کند و گوستاوو پترو، رئیس‌جمهور کلمبیا، را «قاچاقچی غیرقانونی مواد مخدر» خواند.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/17885" target="_blank">📅 02:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17884">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromورزش سه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6be0b658c6.mp4?token=vAXPL-SyVZkMpcZOHGVKhb5G75xIrpEhSxJIsELcU6LtuVXOq9-Uu32f1uZhiYmu5fweowrgm48V_WX9SjB3VKqlm2HJXIpbx9MVq3QiURRAJayRbTnGj7T53AbAGcvlysGGp5lKNQxQyQY0964BV30aYe4Pv58f2sWUFVB_hKRqz0rfWkns_fBuZiaLLAAPQAb5HH8ddzo-NqNQoA28VXt7ZFILksP6fFZSlf0IMRNeQm1L0cr_5YALX0nuyD4LfPGA1MZks2in4OMkb3hfhEXvXey2t5qE6cvBaXcSRU3_kQTuOyhSTJ6sQChogAQdcFLAqY4APZ9dM0eeUfAQKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6be0b658c6.mp4?token=vAXPL-SyVZkMpcZOHGVKhb5G75xIrpEhSxJIsELcU6LtuVXOq9-Uu32f1uZhiYmu5fweowrgm48V_WX9SjB3VKqlm2HJXIpbx9MVq3QiURRAJayRbTnGj7T53AbAGcvlysGGp5lKNQxQyQY0964BV30aYe4Pv58f2sWUFVB_hKRqz0rfWkns_fBuZiaLLAAPQAb5HH8ddzo-NqNQoA28VXt7ZFILksP6fFZSlf0IMRNeQm1L0cr_5YALX0nuyD4LfPGA1MZks2in4OMkb3hfhEXvXey2t5qE6cvBaXcSRU3_kQTuOyhSTJ6sQChogAQdcFLAqY4APZ9dM0eeUfAQKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سهراب سپهری به جای طارمی؛
😂
راه حل خیابانی برای گل مردود ایران به بلژیک
🏆
در قسمت دوازدهم برجام رونمایی شد
🆔
@varzesh3</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17884" target="_blank">📅 02:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17883">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">به نظرم تنگه هرمز را بدهیم بیرو ببندد و خودمان برویم تنگه مالاکا را ببندیم!  آبش را هم بدهیم آقای میثاقی بخورد!</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/17883" target="_blank">📅 00:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17882">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خارجی ها مخ شان سوت کشیده و فکر می‌کنند بیرانوند راننده یک تراکتور است!  سبحان الله!</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/17882" target="_blank">📅 00:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17881">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hG94Tjfx54kTSaa8yFuAJxh3wPobbFaevg-pDolG4VNelpTszOPWJt4CMnq5NGHj1ZCX__Y2P-wRjogTcRmX8c6iecBase7pFMOcSHZBunC2I3SDRZnbRgzM2iupYh65fsoMtYptRc3NaaI2HbwoCkFRlhMpRRhpG1a3i67nw9sdpMed455PGSgVMz12-SmOwElO_yvG73xFqPsH5ap7ZWfokt5bSx0v_56UVbuMUBwc7XvTrnG7nG6_u9gOP7iNyN4ER9cTu2a_OKNpJnpypgd8zxxCmqhljeIipAn_GGRxK9UsLJo6-JCYBl3VvUT_Cy6ygp4ITQ5xdS3c1Ht-Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب تاکتیک های ناشناخته ای رو کردیم که سبحان الله!  انصافا بیرو عالی بود و ثابت کرد یک گلر خوب می‌تواند یک تیم نابود را نجات بدهد!</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/17881" target="_blank">📅 00:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17880">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fjycn9keBPBErHFCC7UYcBT48Uirht-bGvj4_jH_qj7i78V4wBalKbhOrWjz_FiYYnW79IJXpAbS58Y7KX5rsKtMIvSEmz9zYEPsVp4UV-3ki0lrqd2FXmGRO_mrJFJYwYf-5-_CHsYly_riC13Nvec0HjlESldCDvEJHs77tX7vgkHRZv2_U0wQgo_dataSTkUhsfIwppyRoDJkUuZkH2kl6PEdeI9y3kK8k-WS89a5d4SKMiydpqK5BXGJBqsn1UzN4bHZUiRkl7kK-8cjZk7hy5gyFmDfOH9UlL7mLtTwgilAUdzpSC4gRNP8plAyrHBdrBgWMVH9Z_WVtUhpdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب تاکتیک های ناشناخته ای رو کردیم که سبحان الله!
انصافا بیرو عالی بود و ثابت کرد یک گلر خوب می‌تواند یک تیم نابود را نجات بدهد!</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/17880" target="_blank">📅 00:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17879">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9e2be94a.mp4?token=BZ5AK7VxlRywtw4kIJlQxFUoCquErw9c6epOHlCnffn_4XfiIABIrxOF9gJ_Dw1vIoF3oN5kAzcSYMY8vDgVTpkaho58mxFN4U6OiV0hVoidVHPxJDaKIQDsNpUz8Dz7sz8lJP22UIwEAvOPLElyzwZG_PBaYVfOZ4nuKX3N8u-hwK4Mh9bjzbkCIvT2deX4lyQiEA4dIgBS4owqWLhgbUpNkDfwrKHedm_ANzkLwpPzrK0F0ISOVUhoCtN4hVJ35oTrQKduUeQRfsyCaEQaDTSDF7oRaTblAgWmdhY2AgcKiw-GouRxaUI4WzOmtcZA5Ag2N986J5CUAne-KM-fxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9e2be94a.mp4?token=BZ5AK7VxlRywtw4kIJlQxFUoCquErw9c6epOHlCnffn_4XfiIABIrxOF9gJ_Dw1vIoF3oN5kAzcSYMY8vDgVTpkaho58mxFN4U6OiV0hVoidVHPxJDaKIQDsNpUz8Dz7sz8lJP22UIwEAvOPLElyzwZG_PBaYVfOZ4nuKX3N8u-hwK4Mh9bjzbkCIvT2deX4lyQiEA4dIgBS4owqWLhgbUpNkDfwrKHedm_ANzkLwpPzrK0F0ISOVUhoCtN4hVJ35oTrQKduUeQRfsyCaEQaDTSDF7oRaTblAgWmdhY2AgcKiw-GouRxaUI4WzOmtcZA5Ag2N986J5CUAne-KM-fxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دلال های محبت فاکستانی را ببینید!
شهباز شریف از عراقچی التماس می‌کند تا با ونس ترنس دست بدهد اما عراقچی پشت کرده و می‌رود و بعد شهباز شریف و عاصم منیر شروع به ماله کشی برای آمریکایی‌ها می‌کنند!</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/17879" target="_blank">📅 00:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17878">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">راس الفان همان منطقه ای است که ایران تاسیسات گازی قطری ها را در مارس به آتش کشیده بود</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/17878" target="_blank">📅 23:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17877">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خبرنگار صداوسیما:
هنوز نمی‌توان گفت که مذاکرات به پایان رسیده است یا خیر اما از شواهد به نظر می‌رسد هیئت ایرانی در آستانه بازگشت به کشور است</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/17877" target="_blank">📅 23:34 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
