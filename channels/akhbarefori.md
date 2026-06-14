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
<img src="https://cdn4.telesco.pe/file/NUIVp5sXc4mLUFnGkYtWYqTUH0o9d3nRD2hFLP1oWZ4FEQKW7B0vxN-UAoGh85xLLm9Brr4M2QsURcyj1pr8fkrPo98mM7rKVK-od_KhHaoWZLIGjLP_yn6L3V_gbGTK45G6vE4-mQAuwb3OGtpFbvIuHjy7kOE4zUdgjAcgqNBXK2O_1iwERdrolucPb52KqZ916QTxs5ZcKsu75rCUxS0cS081Zf-s_zStKGg6k38xKRHDc92E17Snm1FHSzSLLM7h3gPyNOZH7L4rQ-5XJVkwKK7G_Be9adoEEuBYriLd5uxbszbdZUvuvY8miYXQJqwiE-o7AaZVwXIp0ZwUPw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.54M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 01:32:36</div>
<hr>

<div class="tg-post" id="msg-659549">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون وزیر خارجه: میانجی‌ها در مذاکرات آتی همچنان حضور خواهند یافت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/659549" target="_blank">📅 01:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659548">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
نیروهای مسلح ایران دستشان همواره روی ماشه خواهد بود
غریب‌آبادی، معاون وزیر خارجه: نیروهای مسلح ایران همواره دستشان روی ماشه خواهد بود برای مقابله با توطئه‌های دشمنان.
همواره برای مقابله با هر توطئه‌ای آماده خواهیم بود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/akhbarefori/659548" target="_blank">📅 01:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659547">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
مذاکرات تا یک ساعت قبل ادامه داشت
غریب‌آبادی، معاون وزیر خارجه:
🔹
تا زمانی که آخرین نکات و مطالبات خود را وارد متن تفاهم نکردیم، با تفاهم نامه موافقت نکردیم. مذاکرات تا یک ساعت قبل ادامه داشت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/akhbarefori/659547" target="_blank">📅 01:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659546">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
غریب‌آبادی: تعهدات ایران نسبت به دستاوردهایمان قابل قیاس نیست
غریب‌آبادی، معاون وزیر خارجه:
🔹
به زودی متن تفاهم نامه منتشر می‌شود و مردم می‌توانند دستاوردها و تعهدات ایران را ببینید. تعهدات ما نسبت به دستاوردهایمان قابل قیاس نیست.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/659546" target="_blank">📅 01:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659545">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
تهدیدات امشب ایران در پیشبرد برخی موضوعات در متن مذاکره موثر بود
غریب‌آبادی، معاون وزیر خارجه:
🔹
برخی اصلاحات مدنظر در تفاهم را با اتفاقاتی که در لبنان افتاد و با بیانیه‌های نیروهای مسلح، پیشبرد کار مذاکراتی را تسهیل کرد. نیروهای مسلح آماده پاسخ قاطع بودند.
🔹
ترامپ هم مواضعی اتخاذ کرد و نسبت به رژیم صهیونیستی انتقاد کرد. و حزب‌الله نیز پاسخهای محکم و قاطعی به اقدام تروریستی رژیم صهیونیستی داد.
🔹
اقتدار نظامی و تهدیداتی که صورت گرفت کمک کرد به فرآیند نهایی کردن متن و پیشبرد برخی موضوعات که برای نهایی کردن متن داشتیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/659545" target="_blank">📅 01:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659543">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون وزیر خارجه:  دشمنی که حمله کرده بود تا اهداف شومش را عملیاتی کند، در تمامی اهدافش متحمل شکست شد و جمهوری اسلامی ایران پیروزی‌های بزرگی در جنگ کسب کرد
🔹
در پیش نویس تفاهم، تمامی مواضع مهم خود را گنجانده‌ایم.
🔹
پس از امضای رسمی، متن تفاهم‌نامه…</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/659543" target="_blank">📅 01:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659542">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون وزیر خارجه:  دشمنی که حمله کرده بود تا اهداف شومش را عملیاتی کند، در تمامی اهدافش متحمل شکست شد و جمهوری اسلامی ایران پیروزی‌های بزرگی در جنگ کسب کرد
🔹
در پیش نویس تفاهم، تمامی مواضع مهم خود را گنجانده‌ایم.
🔹
پس از امضای رسمی، متن تفاهم‌نامه منتشر خواهد شد. قبل از امضا نیز از طریق رسانه‌های عمومی، ابعاد مختلف یادداشت تفاهم را تشریح خواهیم کرد و دستاوردها را خواهیم گفت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/659542" target="_blank">📅 01:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659541">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون وزیر خارجه: پایان فوری و دائمی جنگ و عملیات‌های نظامی در جبهه‌های مختلف و از جمله لبنان، از همین امشب اعلام می‌شود
🔹
از امشب خاتمه محاصره دریایی آمریکا علیه ایران آغاز می‌شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/akhbarefori/659541" target="_blank">📅 01:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659539">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxewwoL5pNzMv5fQETzWe5Pv63asYcxRs5c14xSyChrt1eoSOm-xrJQuYnMdg6AMbwmL_WzM4xG7Rx7JtGLzQlFhmjyFyBXOMuJBp-5nZBWbFMrm8MWfV_2T9p4KF4uEDy_JMEZVvucoBCzCvLa69IN_cPucxpKmiV46UBja0zNu_iKi6wz57ZVEtE7-Cb1jiuGX3G_UVuUwh5qnhcWFCLBmC7bVp0MPz1zKPK0biizpZ-9JHJvdGs_Af7vbFjG5GzH4DmfAWhOiEopBVXHqDThdHLrKSTVD1t-WpxGMF7TsxwqJCNh49FdD7P2PrkXGffAjN4Fm1oA1sVPbGOh9cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط نفت به ۸۷ دلار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/659539" target="_blank">📅 01:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659538">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون وزیر خارجه: پایان فوری و دائمی جنگ و عملیات‌های نظامی در جبهه‌های مختلف و از جمله لبنان، از همین امشب اعلام می‌شود
🔹
از امشب خاتمه محاصره دریایی آمریکا علیه ایران آغاز می‌شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/659538" target="_blank">📅 01:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659537">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون وزیر خارجه: متن یادداشت تفاهم نهایی شده و امضای رسمی یادداشت تفاهم اسلام آباد روز جمعه در سوئیس انجام خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/659537" target="_blank">📅 01:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659536">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb2c4f204e.mp4?token=nmweDIVKk01Q80UWqXUWVbAUUTUZk2Kj_EQ9EjPqK_rqH2y6bqEnSbW-O3USTO63IVR8BvdmP9z89I-M0zAjmt0imDjfRjsDjSB67XQDsqZjNWTf6eEr3k35-GNQ1iAsWgb2TkMjxJ1DgQ3kx_Z0pHKvjPqXY_Bw7AL1ZIs4vnZyag8ckCXu1vt2Bb7kQL_6cWDTagmCL1c7GN_LpvYbOsMxXXicplFXENV0kqylYcfJaob6M92i56GTstop84jimmvzT6EBL9NloC_2yKcYqZXNWaw6PKFN9lRptEsiX-DFnloQEfkQ6VTOZmlz7yS3L8IJ2nHVWNRLLMQSrz5ksQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb2c4f204e.mp4?token=nmweDIVKk01Q80UWqXUWVbAUUTUZk2Kj_EQ9EjPqK_rqH2y6bqEnSbW-O3USTO63IVR8BvdmP9z89I-M0zAjmt0imDjfRjsDjSB67XQDsqZjNWTf6eEr3k35-GNQ1iAsWgb2TkMjxJ1DgQ3kx_Z0pHKvjPqXY_Bw7AL1ZIs4vnZyag8ckCXu1vt2Bb7kQL_6cWDTagmCL1c7GN_LpvYbOsMxXXicplFXENV0kqylYcfJaob6M92i56GTstop84jimmvzT6EBL9NloC_2yKcYqZXNWaw6PKFN9lRptEsiX-DFnloQEfkQ6VTOZmlz7yS3L8IJ2nHVWNRLLMQSrz5ksQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم ژاپن به هلند توسط کامادا ۸۹
⬛️
🇯🇵
2️⃣
🏆
2️⃣
🇳🇱
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/659536" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659535">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دقایقی دیگر بیانیه رسمی دبیرخانه شورای عالی امنیت ملی درباره توافق آتش بس منتشر خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/659535" target="_blank">📅 01:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659534">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0b85cc77a.mp4?token=WzXPYdHsTLvjfZZlBS5EHn_Y4du0_OljJXDqrYTxzXPV5VkUZYgDBohxqoZSsXRzqxIjgWIf2TezRpOvB0BQCk7PC1VRy5Ag0djYxyqBBwSOgPakuzTU1G8spa9EtcqfWE0aAknqMUeaTwtEuDZmw3N2rxvR6utgim9fZv7hI4mALoghI6VaVX-gEqhlAYzcEWqmhb5qaNvIpsFoZ7gSHP57tuH4SFfykJC_GBIgC3elRABZ0vi5p5MHtuCE33otzWBv5kfb1DtBpnBJPrsUBsG71Q9lRRFX3o75v0sIlK8SOoR_DIED5Nc2Q57VU7WYASY4sEGZ58QD_9pHZF6cAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0b85cc77a.mp4?token=WzXPYdHsTLvjfZZlBS5EHn_Y4du0_OljJXDqrYTxzXPV5VkUZYgDBohxqoZSsXRzqxIjgWIf2TezRpOvB0BQCk7PC1VRy5Ag0djYxyqBBwSOgPakuzTU1G8spa9EtcqfWE0aAknqMUeaTwtEuDZmw3N2rxvR6utgim9fZv7hI4mALoghI6VaVX-gEqhlAYzcEWqmhb5qaNvIpsFoZ7gSHP57tuH4SFfykJC_GBIgC3elRABZ0vi5p5MHtuCE33otzWBv5kfb1DtBpnBJPrsUBsG71Q9lRRFX3o75v0sIlK8SOoR_DIED5Nc2Q57VU7WYASY4sEGZ58QD_9pHZF6cAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاخ سفید به شیوه سنتی امضای توافق صلح با ایران را اعلام کرد
🔹
خبرنگاران تصاویری از دود سفید در کاخ سفید را منتشر کردند، طبق سنت، این به معنای امضای توافق‌نامه صلح جدید است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/659534" target="_blank">📅 01:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659533">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
نیویورک تایمز: ایران یک حمله برنامه‌ریزی‌شده به اسرائیل را لغو کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/659533" target="_blank">📅 01:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659531">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
خواسته ایران در موضوع اداره تنگه هرمز محقق شد
🔹
با تغییرات لحظه آخری در متن تفاهنامه ایران و آمریکا، تنگه هرمز با ترتیباتی که ایران اتخاد خواهد کرد بازگشایی می شود و نحوه اداره تردد در تنگه هرمزو شیوه ارائه خدمات دریایی و دریافت هزینه های مربوط به آن به جمهوری اسلامی ایران و عمان به عنوان کشورهای ساحلی  تنگه محول شد./ صبح نو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/659531" target="_blank">📅 01:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659529">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLGH53XiMhunr3WwnLDw88A9hWOsTFNg3MXRdZT9ppMKt7PkVhvbEMx64WzE1iCt67lKWaYpIfa1QwKBNHNE3v6eR5GHOjb2_8glSCNQF10JooO0Pwb_PzNbqcnPrkxrWHIFRQH14j_040N2XPM3d_Mvn-nq9VAE-25r5dins-ZxOFoM9yNMn18_TGF1ZavZ8xmXo51unPEP7naBjsjwScDAiPULGhw_V8OTmj8_J0bJnI99MPYS6zW2oL603AD3NXgNUAnziDv-GFKzvKU8AgKO7Lv3R3iYO9nww3IZr6DScXGBTItVNpbjQA2IuTDwoqsMRDP7EFsLtRQk7iybAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستاورد فوق العاده با ارزش ترامپ:
بازگشایی تنگه ای که قبل از جنگ هرگز بسته نبود!
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/659529" target="_blank">📅 01:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659528">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">خبرفوری
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/659528" target="_blank">📅 01:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659527">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
ترامپ: کشتی‌های جهان می‌توانند تردد در تنگه هرمز را از سر بگیرند
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659527" target="_blank">📅 01:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659526">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
تسنیم: برخی منابع حاکیست که تا دقایقی دیگر مسئولان ایرانی درباره خبرهای منتشره راجع به تفاهم صحبت خواهند کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659526" target="_blank">📅 01:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659525">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
ترامپ: توافق با جمهوری اسلامی ایران اکنون کامل شده است. به همه تبریک می‌گویم!
🔹
بدین‌وسیله من بازگشایی بدون عوارض تنگه هرمز را به طور کامل مجاز می‌دانم، و همزمان با این، لغو فوری محاصره دریایی ایالات متحده را دستور می‌دهم.
🔹
ای کشتی‌های جهان، موتورهایتان…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659525" target="_blank">📅 01:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659524">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d70bce1a9.mp4?token=MBlDzQ7VnFQp7mD_E8f6emxHX15XWHePa2m87iuI6RhJm6-IEYGZ1a6g0MH0x8WYVxrFHZB6Sc3J6Ua1jzXmsPNlzuPs3ZDzXf1vXKbZbTuyZ_lcny7FcI9DbPkUKiwpYEnqe37qeSLGfCeyzOTA-_t0Ohj9fePDqU2yaSwF2VeZ_Wg3sLbZZcQuF6EJgfq4RaxaCeA9O0IjJz0OkLElG326zilMlQEmoALl5jcu6kEsYZIcQLcSZHcPPdaqY9ll0wMTgvVhb4-M_uVlMI1Rb0MdikjAQ5wcQh2uBAS7jKJ6DhIIN1a_MXfj1wraX1wHeGtRDr6Hvq5o97nA39AFNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d70bce1a9.mp4?token=MBlDzQ7VnFQp7mD_E8f6emxHX15XWHePa2m87iuI6RhJm6-IEYGZ1a6g0MH0x8WYVxrFHZB6Sc3J6Ua1jzXmsPNlzuPs3ZDzXf1vXKbZbTuyZ_lcny7FcI9DbPkUKiwpYEnqe37qeSLGfCeyzOTA-_t0Ohj9fePDqU2yaSwF2VeZ_Wg3sLbZZcQuF6EJgfq4RaxaCeA9O0IjJz0OkLElG326zilMlQEmoALl5jcu6kEsYZIcQLcSZHcPPdaqY9ll0wMTgvVhb4-M_uVlMI1Rb0MdikjAQ5wcQh2uBAS7jKJ6DhIIN1a_MXfj1wraX1wHeGtRDr6Hvq5o97nA39AFNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعلام رسمی خبر توافق و توقف جنگ در شبکه خبر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659524" target="_blank">📅 01:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659523">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwxIB6DiBI80bFll5PI_tfxmzqOKn7GayTygjYgHoSMQQsKvsPyE0J7ZMRfkrWmiRjJsBcevRzS6-4itRY1Yc1jTW4xj4tXeMFsr5cEzKUkbHU3kXBQWzVo43b22IRD-3JUqbrrxGS7BCvXO11nFNFRt4DZUzZxx4Yi1yi4DJ5mm-c0OU4OfD2wbNg7fKMMsHg6K1PaiiTFJ662A67oK8fcyh9dfsra_Ssi7oznYlIeRZUB_Rybi9GyQRjaH5ipBQU4mlAWM_5vjBDT0Mhnx_3B2v9rtGkm68nCZx3SBNuune7HmCbtazVdIRKOccJUg2mqXaeh768LogXI71g1KHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلاکارد هم می‌خوای بگیری دستت، اینجوری باشه
🫠
‎
#WillPayThePrice
‎
#تقاص_خواهید_داد
توییتر خبرفوری را دنبال کنید
👇🏻
https://x.com/Akhbare_Fori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/659523" target="_blank">📅 01:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659522">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ترامپ: توافق با جمهوری اسلامی ایران اکنون کامل شده است. به همه تبریک می‌گویم!
🔹
بدین‌وسیله من بازگشایی بدون عوارض تنگه هرمز را به طور کامل مجاز می‌دانم، و همزمان با این، لغو فوری محاصره دریایی ایالات متحده را دستور می‌دهم.
🔹
ای کشتی‌های جهان، موتورهایتان را روشن کنید. بگذارید نفت جاری شود! رئیس‌جمهور، دونالد جی. ترامپ
📲
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659522" target="_blank">📅 01:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659521">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxOMNisEdlxcm30Ells0_BqZXokiF1Bim46bM_GNSwuhWC5YHTCZbYlzpwtVBmd1Q99M0Q19_qBGPFVdSQF1fU8ONfCahG-hOmsUFnqyvvZ0oo14L5YbN-HwYLNJKFuzzbFWmezITxpCtPvSDas7GxNDTjuRqx7EUG7EC5KUz9djwG7wJ29xWSncyuTC6IGy8yoiB8gZTDqCy4bvakxN77rSZzTRu7FJmSYdxs2N8yl-t01Qk8XZvsv-Au92qHw3Mid7f72qsX81-u0eOJCTh1Dgha_4j1l_x6vd2sU1lOTQ26matAagZeiktHaxPYCkhtF5dq1jpFig2Z6rQj6YvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: توافق با جمهوری اسلامی ایران به طور کامل نهایی شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659521" target="_blank">📅 01:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659520">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0372d04149.mp4?token=px9rCPVd-nqDIMNlqlzSB1vU9lQ3K4sCiOil_xpEiHoKOozzd1uGOX9Guufer5wuZ7bdQNztO1XjC25kJ3CpwBQFsitjQe2sdkzX944X56KJ4SSeRHURuQt53FAwAQYV63ccxapxuLdojya5SxufiIUzo0rrObI8Ijbbewg5aAHxofq6I8mqyuxQRMT3MvJn39-XAtyhJjZFUlWn_ybPb4Qhpq_LoUXBI0DiDw25lty4HcJsBrxyM6UgNkwViw2lJBv2oBBex-3ZhYn-xPXF6v__waIuaI6w4ePbctMFMVNaVR21ep9oUJf4dI5O9WfnCx_t0Tp4fQQMYcbo9cIadA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0372d04149.mp4?token=px9rCPVd-nqDIMNlqlzSB1vU9lQ3K4sCiOil_xpEiHoKOozzd1uGOX9Guufer5wuZ7bdQNztO1XjC25kJ3CpwBQFsitjQe2sdkzX944X56KJ4SSeRHURuQt53FAwAQYV63ccxapxuLdojya5SxufiIUzo0rrObI8Ijbbewg5aAHxofq6I8mqyuxQRMT3MvJn39-XAtyhJjZFUlWn_ybPb4Qhpq_LoUXBI0DiDw25lty4HcJsBrxyM6UgNkwViw2lJBv2oBBex-3ZhYn-xPXF6v__waIuaI6w4ePbctMFMVNaVR21ep9oUJf4dI5O9WfnCx_t0Tp4fQQMYcbo9cIadA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم هلند به ژاپن توسط سامرویل ۶۴
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659520" target="_blank">📅 01:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659519">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e2fecc6be.mp4?token=csPY9NGgvGhMIC8gu5hXcboKmmQsjP6ODo16wtVcQjDIOzSCH0gJYATdmc3bn9dtWaeP6sId4eX34NueRNzQHMt9JzN7oRAJPJJaysNX2prKmz0ZlKgPjWIIMYJxwp5LI6lBXcxG1_AL6zVBsNXUs_hZwY8srvvF8zpX_LarqAw1lJkRV8v7N-CEOp8ZWJn674WDa2i3uQ_YOVU9uo-3e4FKwgU9Kt0F_Pm_MdrpeY_n2fXYGftcXDLs1H41ZX3jr2It1WtD5E8NJerA7L0JVgC5AiJGJCXrB2KQcbT21qeR0X64h6siFchJO6X_709kSdAVA5yuk0gkcDNddrZENQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e2fecc6be.mp4?token=csPY9NGgvGhMIC8gu5hXcboKmmQsjP6ODo16wtVcQjDIOzSCH0gJYATdmc3bn9dtWaeP6sId4eX34NueRNzQHMt9JzN7oRAJPJJaysNX2prKmz0ZlKgPjWIIMYJxwp5LI6lBXcxG1_AL6zVBsNXUs_hZwY8srvvF8zpX_LarqAw1lJkRV8v7N-CEOp8ZWJn674WDa2i3uQ_YOVU9uo-3e4FKwgU9Kt0F_Pm_MdrpeY_n2fXYGftcXDLs1H41ZX3jr2It1WtD5E8NJerA7L0JVgC5AiJGJCXrB2KQcbT21qeR0X64h6siFchJO6X_709kSdAVA5yuk0gkcDNddrZENQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین واکنش مجری شبکه خبر به امضای توافق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659519" target="_blank">📅 01:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659518">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">#خبرفوری
عقب نشینی دقیقه آخری ترامپ
🔹
در پی ایستادگی هیئت مذاکره کننده ایرانی بر خطوط قرمز، آمریکا در لحظات پایانی عقب نشینی کرد و قرار است رئیس جمهور آمریکا اعلام کند که محاصره دریایی علیه ایران که براساس متن در طول ۳۰ روز برداشته می شود، به یکباره و به طور کامل رفع خواهد شد/خبرفوری
📲
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659518" target="_blank">📅 00:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659517">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
صداوسیما: آمریکا بند پایان دادن به جنگ در تمام جبهه‌ها حتی در لبنان را قبول کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/659517" target="_blank">📅 00:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659516">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
قیمت تتر به ۱۶۵هزار تومان رسید
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659516" target="_blank">📅 00:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659515">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozljToNtnMgT31Pyxl59zbp9MVssEaStkBHmm9ivPWw6Q5Ete4yknLkyD_-tMg5oJhOe-4fd0j6DrxsaiP7dMR7H69n5dYRjDGMDElCx7ELQr7hvRVIUX0SV896yCsKVIq-f-hM5QiMWTV8zAN9ChMsBothIBeFwO-WLnQiGz3IpGAcypgFuGLNyHlTICKhsCyaIXgiy9a8EWcTQN9Spz0iHmumoEH5_Brp6a3hLEP4OisdYIkGAd59vJ1MNZhZS2eb030Ma659C9Cw_yDOSJ_Bj4j6RSMiRF91hfSVbiP0mF39ll0wTBJsNRM9Zmpd7KwcdJdtoenfwexTvuhkEIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیرنویس شبکه خبر: نخست وزیر پاکستان از دستیابی به توافق پایان جنگ آمریکا علیه ایران خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659515" target="_blank">📅 00:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659513">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad78c1119.mp4?token=RPlJw11xJT2VNgRiQ8dxn33JVirnRsvp3Hi98hN3pgnENkJ3EqFIXhMlirrAjqVfjfU3Wwex0Jeh9MXPrxuW-ZpZCTQUTBsA0QWnAi4V2Y6twG5cdrk01H_ww3B6Jvc9KNgLKOMPt7fweL185QgyduouSIjjZsftwTmuihbaQtKBIOIjh3YxwPd_Pn73Zp4DFbNv_dDpZJHkgSrcZ0erzNt6k8hrepBfXpaRZIuC5emhhu12ZKFPvISTEMi2C9FOGg9UriJgiwe0vXYAi5nq-pxCFI2KwvJYuzEqibTvgMOSjq_PRHfA6sQtFmoZL7UMgFw46h3vqPn_4ENHPH4M1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad78c1119.mp4?token=RPlJw11xJT2VNgRiQ8dxn33JVirnRsvp3Hi98hN3pgnENkJ3EqFIXhMlirrAjqVfjfU3Wwex0Jeh9MXPrxuW-ZpZCTQUTBsA0QWnAi4V2Y6twG5cdrk01H_ww3B6Jvc9KNgLKOMPt7fweL185QgyduouSIjjZsftwTmuihbaQtKBIOIjh3YxwPd_Pn73Zp4DFbNv_dDpZJHkgSrcZ0erzNt6k8hrepBfXpaRZIuC5emhhu12ZKFPvISTEMi2C9FOGg9UriJgiwe0vXYAi5nq-pxCFI2KwvJYuzEqibTvgMOSjq_PRHfA6sQtFmoZL7UMgFw46h3vqPn_4ENHPH4M1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل مساوی ژاپن در دقیقه ۵۷
هلند ۱ ــ ۱ ژاپن
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/659513" target="_blank">📅 00:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659511">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
نخست وزیر پاکستان از دستیابی به توافق با واشنگتن و تهران خبر داد
🔹
پس از مذاکرات فشرده، با کمال خرسندی اعلام می‌کنیم که توافق صلح بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شده است. هر دو طرف پایان فوری و دائمی عملیات نظامی در تمام جبهه‌ها، از جمله…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659511" target="_blank">📅 00:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659510">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZfK2Y5qGzmkZX3AcononxShaITCdf6bCGxdm_2VzRGQ8dnp3oYE-5GL6JTvz_-u09iEplX7eZelpKUkQ3hQT7LCK56EoJs4KWtDsIswJCDtY6zyGMDdgaohL19re3gWfGUrB4tee9rCje40wC3SvmJGtaJRjOlLt1F7V1uiT4OAwptbnLsofUUWghaTKj2azlzblLuU01mLHrjDPNsFaqez6l0aTQOnpeLve-fObuzSPl5_iWJu-gEhFmwLBgfQmBxJLZVdfsj9ivE9abLsJHA2zmKXrN73XbTCh-0XlCrvjd57Wiwj8nVlFn8GuP5e05_EhMzBvGKnWyYKpQX_Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخست وزیر پاکستان از دستیابی به توافق با واشنگتن و تهران خبر داد
🔹
پس از مذاکرات فشرده، با کمال خرسندی اعلام می‌کنیم که توافق صلح بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شده است. هر دو طرف پایان فوری و دائمی عملیات نظامی در تمام جبهه‌ها، از جمله در لبنان، را اعلام کرده‌اند.
🔹
ما مایلیم از ایالات متحده آمریکا و جمهوری اسلامی ایران به خاطر تعهدشان به یافتن راه‌حل دیپلماتیک برای این درگیری تشکر کنیم. همچنین مایلیم از برادرانمان در این تلاش میانجیگری، رهبری بزرگ کشور قطر، به خاطر حمایتشان در دستیابی به این توافق‌نامه، صمیمانه قدردانی کنیم. همچنین به ویژه از رهبری دوراندیش پادشاهی عربستان سعودی و جمهوری ترکیه به خاطر کمک‌های عظیمشان در این زمینه تشکر می‌کنم.
🔹
با حصول توافق‌نامه، میانجی‌ها این هفته مجموعه‌ای از جلسات را تسهیل خواهند کرد. این بحث‌های پیش از اجرا، پایه و اساس مذاکرات فنی و مراسم رسمی امضای توافق‌نامه را بنا خواهد نهاد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/659510" target="_blank">📅 00:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659509">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ: این توافق به صورت الکترونیکی، یا توسط من یا معاون رئیس جمهور ونس، امضا خواهد شد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/659509" target="_blank">📅 00:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659508">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ترامپ در گفتگو با وال استریت ژورنال: ایران هنوز تأیید نکرده است که با این توافق موافقت کرده باشد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659508" target="_blank">📅 00:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659507">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">#خبرفوری
🔹
یک منبع آگاه به خبرفوری گفت: پس از حمله رژیم صهیونی به ضاحیه با تصمیم رئیس هئیت مذاکره کننده ایران، اعضای تیم مذاکراتی مذاکره با طرف قطری را متوقف کردند.
🔹
همزمان نیروهای مسلح آماده برای حمله به رژیم شدند. با توئیت قالیباف در واکنش به حمله رژیم به ضاحیه، ترامپ مجبور به ارائه امتیازات جدید و جدی به ایران در موضوع لبنان شد.
طرف آمریکایی و رژیم، تهدید ایران را همچنان معتبر می دانند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/659507" target="_blank">📅 00:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659506">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ادعای ترامپ در گفتگو با وال استریت ژورنال: «بعداً مسائل هسته‌ای را حل می‌کنیم» و افزود که «هیچ عجله‌ای نیست» و می‌توان ظرف یک یا دو ماه آینده به آن پرداخت #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659506" target="_blank">📅 00:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659505">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/844b0be1f8.mp4?token=JNnxoWiN0DtD45B3VvGyhJEk6B8cKLgsQrtjIcr4tK3xy8UXQYgaUMbs1_zoKvyRAny8MLgyySa9sdEf_rj5FDTet-ZhjHcqUWhezPRF_q413hV4jRC8rLKM5lBDlQrx2l9mvz3zHPLGb1BbmQ8LWRiGY6tl3-G7ePjKcovJtuZK13LZl_mSCJWxrCeknjLu1qu48yYLOrj6nrTRgK6a69TUqkAdapQ5P9aX2_Ej2t3PnYH61Y7ciOwr4GzSAxWMxgbNnQQR6MpG_o6jqj-Q10q2Qip88xsox-ZV2L_JKkgK4FtQJ47pivJ31inegS4WTe80cwl-RFFk0CWypu4cZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/844b0be1f8.mp4?token=JNnxoWiN0DtD45B3VvGyhJEk6B8cKLgsQrtjIcr4tK3xy8UXQYgaUMbs1_zoKvyRAny8MLgyySa9sdEf_rj5FDTet-ZhjHcqUWhezPRF_q413hV4jRC8rLKM5lBDlQrx2l9mvz3zHPLGb1BbmQ8LWRiGY6tl3-G7ePjKcovJtuZK13LZl_mSCJWxrCeknjLu1qu48yYLOrj6nrTRgK6a69TUqkAdapQ5P9aX2_Ej2t3PnYH61Y7ciOwr4GzSAxWMxgbNnQQR6MpG_o6jqj-Q10q2Qip88xsox-ZV2L_JKkgK4FtQJ47pivJ31inegS4WTe80cwl-RFFk0CWypu4cZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول هلند به ژاپن توسط فن دایک
۵
۰
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659505" target="_blank">📅 00:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659504">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
فوری/ ترامپ به وال استریت ژورنال: به زودی بیانیه‌ای صادر خواهم کرد که تایید توافق با ایران توسط ایالات متحده را تایید می‌کند #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659504" target="_blank">📅 00:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659503">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
فوری/ ترامپ به وال استریت ژورنال: به زودی بیانیه‌ای صادر خواهم کرد که تایید توافق با ایران توسط ایالات متحده را تایید می‌کند
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/659503" target="_blank">📅 00:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659502">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rdr2Sdp_-qSj6NifE776baQLHCj9tic0jd4OJNVFQb0wJzrDdRX3XAKwPtuvzKy3xLYE5g0WfPD8gsUUM-vaPdleY7kUFS-mmkFFRRzmk2UttodzezbInsa5MXfaLuCCKt2pszxQQSxM7pC196BCvcO_6Nd-XzvAdCF66A-99G7WPpRurUKltxL8bl_wnvAFaM6j_j8hCpYrQ8s1NLC9MxmmK69yPkdg6etj8kZtIcXs5KxcUloWHi-MQgSeGpaiZmi7frkh2lzv5V8dq7qXiP8Q_GmcPwak1dNdyXkILQ_xoCCte1xGsvMInHQGd5Jvz3XN_BCDEC4OI8beLDns3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توییت وزیر کشور پاکستان: الله اکبر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/659502" target="_blank">📅 00:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659501">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
فارس:
تفاهم در «یکشنبهٔ موعود ترامپ» امضا نشد!
🔹
ادعای رئیس‌جمهور آمریکا مبنی بر نهایی‌شدن یادداشت تفاهم در روز یکشنبه، با گذشت این روز و عدم تحقق هرگونه توافق، عملاً خنثی شد.
🔹
ترامپ طی روزهای اخیر بارها بر تاریخ یکشنبه به‌عنوان روز امضای تفاهم تأکید کرده بود.
🔹
با این حال، مقامات جمهوری اسلامی ایران پیش‌تر به‌صراحت اعلام کرده بودند که تفاهم نهایی حاصل نشده است. حتی در فرض نهایی‌شدن، تأکید داشتند که الزامی برای تطابق با تاریخ اعلامی از سوی ترامپ وجود ندارد و این تاریخ نمی‌تواند به‌صورت‌ دیکته‌شده از سوی طرف مقابل تعیین شود.
🔹
اکنون و با پایان‌یافتن روز یکشنبه بدون وقوع رویداد خاصی، مشخص شد که این ادعا نیز مانند بسیاری از اظهارات پیشین ترامپ، فاقد وجاهت واقعی و در چارچوب عملیات روانی و جعل خبر طراحی شده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/659501" target="_blank">📅 00:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659499">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ebc4a08.mp4?token=LFInO3xk5p5B4Si3tHpCcBejRXcOxaNdE597icCeDOktZnnjPGXATtP0pUHPraHWTQmUFFEq3ug2sKv3TOwcqgidnKB2qt-hS3PBAjjwYnmH57Uz8JlaWituP25TOOsMcBtypDmKo2_Rk_UmxHOOffcNZvAEfwdQINDNgEPS_ey4pkiq0gEUBHRHPpfftE5RG5KpuXdU84q70rjivIR6WJU11q8xELzIamLBPiShNqHPCx3j0QQ50r0AvEWXbBRMEte-mN141q2_oPniY8x1s_Bw6R0ZhO9lxUnoI9qsDPqystJ1Z9NscCB7ahH9MHC4ZoISl1G3_oiCEpDqTjygmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ebc4a08.mp4?token=LFInO3xk5p5B4Si3tHpCcBejRXcOxaNdE597icCeDOktZnnjPGXATtP0pUHPraHWTQmUFFEq3ug2sKv3TOwcqgidnKB2qt-hS3PBAjjwYnmH57Uz8JlaWituP25TOOsMcBtypDmKo2_Rk_UmxHOOffcNZvAEfwdQINDNgEPS_ey4pkiq0gEUBHRHPpfftE5RG5KpuXdU84q70rjivIR6WJU11q8xELzIamLBPiShNqHPCx3j0QQ50r0AvEWXbBRMEte-mN141q2_oPniY8x1s_Bw6R0ZhO9lxUnoI9qsDPqystJ1Z9NscCB7ahH9MHC4ZoISl1G3_oiCEpDqTjygmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار جبهه مقاومت : امشب به صورت همزمان ایران، یمن و حزب‌الله به حمله اسرائیل به ضاحیه پاسخ می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/659499" target="_blank">📅 00:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659498">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
اراجیف تکراری ترامپ علیه ایران
🔹
ترامپ، در حالی که برنامه هسته‌ای ایران دارای ماهیت صلح‌آمیز است، ادعا کرد: «ایران هرگز صاحب سلاح هسته‌ای نخواهد شد.»
🔹
با تکرار ادعاهای خود درباره تنگه هرمز، وعده داد که این آبراه حیاتی به‌زودی به روی تجارت جهانی باز خواهد شد.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/659498" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659497">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
منابع عبری: تماس تلفنی وزیر جنگ آمریکا و همتای اسرائیلی
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/659497" target="_blank">📅 00:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659496">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار جبهه مقاومت: اگر ضاحیه را امروز رها کنیم، مقصد موشک‌های بعدی اسرائیل تهران خواهد بود/ به زودی اسرائیل را با یک حمله بزرگ تنبیه می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/659496" target="_blank">📅 00:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659495">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
شبکه ۱۲ عبری به نقل از یک مقام مسئول: نتانیاهو و ترامپ لحظاتی پیش با یکدیگر گفتگو کردند و ترامپ نتانیاهو را در جریان پیشرفت‌های حاصل‌شده برای امضای یک توافق قرار داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/659495" target="_blank">📅 00:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659494">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_4AjcYGz4GTQe45U30G-L6V_V22yNLsaBlrXsYNq3TQVmF3TQ4QRiQ9TRqjtmYRD1UlsZIIRxjCUvHz84Iglf6rRCSbHI6Haz2fazz35IGunjmUToqTnsCtizCk0CsQIa-pX0FRsNR4MnzBTkwSbWG5nayDvcq48m7zzx5ksSTv1Sy7lhgMjPfxbB6e-vmS9y-wpgx_KfDI5TPqUbK-gYfxGJV7SCHjMOwEx2gln2EFc6SevWKQoZpfq5HwAzT-eL51OWWvDNZNZwgYG8ECqn653TN1-frsuEY1pWb8YXK9youRY1veM-ysuqD9vRD8-iJdc7E2au0oTQ2IS0DyOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: دولت خود را موظف می‌داند از نیروهایی که برای دفاع از کشور و امنیت مردم در میدان حضور دارند، حمایت کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/659494" target="_blank">📅 00:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659493">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
یک منبع آگاه، خبر برکناری سعید جلیلی از شورای عالی امنیت ملی را تکذیب کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/659493" target="_blank">📅 00:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659492">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-WfXiTiyORztfKwxxqrpl0zwFPDEC3Xf2ZaP2PxUg3UZpKD71QIuXwlKJULj4-egaGPvFte0-trOOTVKXPgGlrO7WILH8iNbEl_ooComCruUDnHMBWoNdFS9WSg-vT5GU65U4bSLwOfEVKIfnf4PZg2s75T2cCkMrL2fSsYh3PNkNtCb6Fgrap92tyEpaFf96M66N6dso3GNg5Gu-BG6AIX89Yq1rIaFzQPBarxcvh6a7OZ_Kzh5qpSF2a5NVBkkT5EwFYB89FOn_yWTp_MkG9X3lCNFjECGN4HNI_UWIEgkphF6peuoOo2rokUx_wfF7EMpHACFggD2qVxI6Xf3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کجا رو می‌خوای بزنی تهمتن من؟
😍
توییتر خبرفوری را دنبال کنید
👇🏻
https://x.com/Akhbare_Fori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/659492" target="_blank">📅 00:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659491">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IduOYC143p8pvWJSPg2Y2aagcOA3LCCkk026kwiuYhEaDtR_XLNB0HiBb3fQODyJ0KRpFDNANycscVi0G587eeKrTrcOajY2x-CMzxGPVTV1fv5gUfD3MfsedJHjsmAcdug8TeCDhwrE_UKoGoL6k_UsiGC7F7z0RDpR8gJCQyAbHdLHoTukZYTGe38kHGk8OO1r6DOdJEDj4_5wevV2GOaSaYPiYODgzOCZrKGHxzcoUB1hFLfgJaNca_zF5HGkHofoYNwwbRd2V30Qt_JcR4VQmS3NPESD3JM1af9iaDImyzSqRw4bs29d36aA6PiYv5rWMbuG8kNB9tTsL5J0hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/659491" target="_blank">📅 00:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659490">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
المیادین: جنگنده‌های رژیم صهیونیستی منطقه صور در جنوب لبنان را هدف قرار دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/659490" target="_blank">📅 00:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659489">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
کانال ۱۴ عبری: یک کارمند کنست اسرائیل به جاسوسی برای ایران متهم شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/659489" target="_blank">📅 00:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659488">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcXelqDQaTJewDgXNHFA5E5D_Mxdg3Xau10GfM4_nkqyeXrC7l9P24ovYu1cyjiik_s9zDCUMpGT7WvjhDMdbDMBCzlgmNS6G8UXhWa_FKEloqvG4KWLZmuTPqvTZ_eIJLVCSc-FxexqWlcZot_n6TyL1_05sq7JiLrUtpiSl6jkPI3WxWUuYqYNLw0VmldbtRVxvqKStaxqShcx9Yh0gsr5KDdTkwXUDxYd0Vfq-n58ZAJdj6rMPZpn62bZY-1vjiUUoKMoT86nNvNb1t-00s2s88rYCt732RANed021V9c80Q22zvzL9rnWEVv6J0HpuZn0xqxLoaHShwDR5s3wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چهره عجیب هوادار ژاپن در بازی برابر هلند به سوژه رسانه‌های اجتماعی تبدیل شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/659488" target="_blank">📅 23:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659487">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bffdcb7ae.mp4?token=fOvUrHlSajD_bpZ_KD-a-tYx5uZywdN97NOPTVBQa4y7sj_yldfeoCG2PscRMSTa2af8DDQGLHmPbxdFY_r43ub4Cv28uj2S1J_G4jZtf_yLg_x1ZzseRpPuZgFccuU_jebtPyF4nseR70WZoX51qF3_XnIUidt1AmoNQbEOfUf4zftNNrs4Awx49ja85rG7gVNEySqdlt_6F8CWJllJLMluTk42yYYqlgf42kho7ew5n3Lj62kXC2wJQzY8ZNvCaAFyrUzuytt_p244CQchS1MTWKqwyJFJ2wFxY32khBesXHNh3EAb5wpXBUSORaqnhMQfeFsnV55aA-hunjnL3jleNUolB2lZW9u96H0kO1JlK-XCBdeBSf0Pv2DuJpSPDrTFqtzn7j-_fQD_FOI9P8suLSczR26oHuCZ_NrZAeqiMpdI2fxAH0p2JOEd4dVWGDsEorBUnetuhUV5EIzh1M9EVNC4y-uQZZYW8Dy7181hL3dO0WAgML6qcWcSB8EdLjMFHzSy3kotnX9eH2jBd5b8vMup7HyGZ6em09puYuou5irqsMUllLpaZ1wMHL_KIgz-6ZcXBuIKlPmGLxRdtpLmuYxzbcgaxrS59bp7NfeRGMgh9YnyDpDkN1SEDqUNxruvOgSi2lY-pClUe0zfJgu40uWGo9SOPnIq4J8tKKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bffdcb7ae.mp4?token=fOvUrHlSajD_bpZ_KD-a-tYx5uZywdN97NOPTVBQa4y7sj_yldfeoCG2PscRMSTa2af8DDQGLHmPbxdFY_r43ub4Cv28uj2S1J_G4jZtf_yLg_x1ZzseRpPuZgFccuU_jebtPyF4nseR70WZoX51qF3_XnIUidt1AmoNQbEOfUf4zftNNrs4Awx49ja85rG7gVNEySqdlt_6F8CWJllJLMluTk42yYYqlgf42kho7ew5n3Lj62kXC2wJQzY8ZNvCaAFyrUzuytt_p244CQchS1MTWKqwyJFJ2wFxY32khBesXHNh3EAb5wpXBUSORaqnhMQfeFsnV55aA-hunjnL3jleNUolB2lZW9u96H0kO1JlK-XCBdeBSf0Pv2DuJpSPDrTFqtzn7j-_fQD_FOI9P8suLSczR26oHuCZ_NrZAeqiMpdI2fxAH0p2JOEd4dVWGDsEorBUnetuhUV5EIzh1M9EVNC4y-uQZZYW8Dy7181hL3dO0WAgML6qcWcSB8EdLjMFHzSy3kotnX9eH2jBd5b8vMup7HyGZ6em09puYuou5irqsMUllLpaZ1wMHL_KIgz-6ZcXBuIKlPmGLxRdtpLmuYxzbcgaxrS59bp7NfeRGMgh9YnyDpDkN1SEDqUNxruvOgSi2lY-pClUe0zfJgu40uWGo9SOPnIq4J8tKKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سپر انسانی توسط گروه های سرود به دور زیرساخت ها و اماکن ملی کشور تشکیل شد
🔹
ویدیوی فوق ، سندی ماندگار از تشکیل سپر انسانی در ۱۲۰ نقطه زیرساختی کشور است که با حضور مقتدرانه مردم و گروه‌های سرود رقم خورد.
🔹
در پاسخ به تهدیدات اخیر مراجع نظامی و رسانه ای غرب علیه مراکز زیرساختی ، علمی و تمدنی ایران، رویداد کشوری «ایرانِ یکصدا» در سالگرد آغاز جنگ ۱۲ روزه برگزار شد .
این مانور مردمی هماهنگ در ۳۱ استان کشور، فراتر از محاسبات کلاسیک اتاق‌های جنگ دشمن رقم خورد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/659487" target="_blank">📅 23:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659486">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0WEl0RYdPdWD--UH6mCU0jf5YJh_vGopvO2-u5fUNVxDrqMS-nO9qxnddFDSFAgqn7ipAX-bIL68BrIQqp9H0nGZvpPm7NPbKyyc6z3iG_FG6OunYf8mufUC_8Buw3kJajHJsTHtjcf4sCNSSqcltlTk2pn8smmRsKX58o2fSsUZV0qIxvTtAlkLE43L5JBrdj0_d3OUnydpT2nOsdRSKny8u_PFU42udCrdS_C_3CUioDCyqAIsg6jyyH1IJgledZ0b3wAkrD6F2J7Za0rNRQuNbNs4_XpKjGRDvVPHIgWkyicsEfmx27ucsaPhQTZLzYhi2jlSz2eS1xv0Jrmog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام دکتر علیرضا زاکانی، شهردار تهران به مناسبت اولین سالگرد شهادت سپهبد علی شادمانی
🔹
شهید سپهبد شادمانی با اینکه از فرماندهان ارزنده دفاع مقدس بود و بعد از آن نیز در عالی‌ترین سطوح در مسیر جهاد ثابت قدم باقی ماند اما مسیر گمنامی را برای خود و خانواده‌اش برگزید.
🔹
شهید شادمانی در همان مدت کوتاه فرماندهی خود بر نیروهای مسلح توانست هدایت قوای نظامی ایران را بدست گرفته و رهنمودهای او نه تنها تا پایان جنگ ۱۲روزه، بلکه در جنگ رمضان نیز به کمک نیروهای مسلح آمد.
🔹
رحمت خدا بر روح بلند او و آرزوی صبر برای خانواده‌ی ایشان.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/659486" target="_blank">📅 23:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659485">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
با ورود نوزدهمین و آخرین گروه پروازی حجاج به فرودگاه بین‌المللی شهید دستغیب شیراز، عملیات بازگشت زائران حج تمتع ۱۴۰۵ از مسیر شیراز پس از انجام ۱۹ پرواز به پایان رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/659485" target="_blank">📅 23:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659484">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
سی‌ان‌ان: یک منبع اسرائیلی گفت نتانیاهو به دنبال دیدار فوری با ترامپ است
🔹
نتانیاهو تلاش می‌کند پس از بازگشت ترامپ از نشست جی‌۷ در اروپا، آخر هفته آینده یا اندکی پس از آن، دیداری ترتیب دهد.
🔹
ترامپ روز یکشنبه پس از آنکه ارتش اسرائیل، بیروت را هدف قرار داد، به شدت اسرائیل را سرزنش کرد و گفت حمله به پایتخت لبنان «نباید اتفاق می‌افتاد»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/659484" target="_blank">📅 23:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659483">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ادعای یارون آبراهام، روزنامه‌نگار اسرائیلی: در ساعات اخیر شتاب قابل توجهی در مذاکرات برای امضای تفاهم‌نامه میان ایالات متحده و ایران، با میانجی‌گری قطر و پاکستان شکل گرفته
🔹
هدف آمریکا ارائه امتیازاتی به ایران، شاید به شکل پول یا تسهیلات اقتصادی، در ازای امضای این تفاهم‌نامه است/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/659483" target="_blank">📅 23:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659482">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rc152XX-a36GF4YtisfY9_xXHpk1ihj5xjWnwdvckEVqt8YUc2JNdKZeSs--Vsa8_CeMAfdBNWHdvlXVIdciCi8TAEBl4XfsHDqaf7jw1lfP-djZ1Ft-FhL9eK-AlLmsz8VjQiIH-K-7bCRd3AhkkK-FEcaUSfIRwpjNVAGF9LSxZ8RIeCAX8VtcRBwXyCz6PIpmPhNa92-65NMZAtUtmUCN2ZmJlVU9n4GsUXHgMXVnE4xhB8EglQCSEkCQwPInQommekY9--m-753ZUXhA4NC7DPNOo3ZGBST1lfkiJhLweLiE5IQvaken0LXxD_lmLQ4edq6Z9IuAiNGcdeRhog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت جام جهانی فوتبال ۲۰۲۶
🔹
همراهان عزیز خبرفوری، برای شرکت در این فراخوان کافی‌ست یک ویس ۱۵ ثانیه‌ای از پیام‌های حمایتی و انگیزشی خود برای تیم ملی فوتبال ایران ضبط کنید و برای ما ارسال کنید.
🔸
صدای شما می‌تواند انرژی‌بخش ملی‌پوشان در مسیر جام جهانی باشد.
🔸
پیام صوتی خود را به آیدی ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/659482" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659481">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
توحش بی‌پایان رژیم صهیونیستی/ ادامه حملات هوایی و تو‌پخانه‌ای دشمن صهیونیستی به مناطق جنوبی لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/659481" target="_blank">📅 23:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659480">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ورود نظامیان صهیونیست به مناطقی از خاک سوریه
🔹
منابع خبری گزارش دادند که نظامیان رژیم صهیونیستی در ادامه نقض تمامیت ارضی سوریه وارد مناطقی از جنوب این کشور شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/659480" target="_blank">📅 23:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659479">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ولایتی: ساعت صفر فرارسیده و پرتابگرها آماده می‌شوند
مشاور رهبر معظم انقلاب اسلامی:
🔹
خطای محاسباتی در بیروت، صبر را به پایان رساند و فرمان صادر شد.ساعت صفر فرا رسیده و پرتابگرها آماده میشوند.
🔹
حزب الله پاره تن محور مقاومت است. اگر آتش شیطنت در لبنان خاموش نشود، دو بازوی قدرتمند جغرافیا یعنی هرمز و باب المندب شاهرگ‌های اقتصادی‌تان را تا خفگی استراتژیک فشار خواهند داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/659479" target="_blank">📅 23:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659478">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6qj27t_bu-oYVvJw-qBlWhEplowmjZkjF4zWcwVj-PzD7G4BRms7p-teUthYD3Bh5RttS7_LqPCXxrBBUuQVG73aqNixmAgSABgPjoj3Y_nwIQ-Wvb-Tiy7z6vxvtns59vQ9c3Ux1MtAe-fwvsuqcqnOA8Ab89TE1GFZBISFCgVem4mP1MUCZ5b05F7hEKrSbYmPwqYKAp7XAJzXPf0QCXCYkN2lOFY9vPAi-NBtUMv4I4SPUji7sG0dswSRD8Tz5HHI8HlcRrJNAVcVS1pLa1Fa4kHASiYVvlNb9xVaYtSrmb0LmA8eC6zkrTbXh-0vY3nGh-UwDRXV5US-ABebQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تسویه حساب
🔹
فرمانده قرارگاه خاتم الانبیا در پیامی خطاب به مردم اعلام کرد که  فرزندان ملت در نیروهای مسلح «دست به ماشه» آماده شلیک به قلب دشمن هستند. سردار عبداللهی گفت که اتفاقات یک سال اخیر، از جنگ ۱۲ روزه تا «جنگ رمضان»، علیرغم خسارت‌های سنگین و داغِ جانسوزِ شهادت امام شهید، فرماندهان و مردم بی‌گناه، یک فرصت بزرگ برای «تسویه حساب تاريخی» با جنایتکاران فراهم کرد؛ نیرو‌های مسلح به  مردم و با عنایت الهی بر سر آن‌ها آوردند آنچه لایقشان بود.
🔹
هفتصدوهفتادوچهارمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/659478" target="_blank">📅 23:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659477">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
رضایی، سخنگوی کمیسیون امنیت ملی: مقامات نظامی می‌گویند که احتمال یک درگیری دیگر وجود دارد و برای یک جنگ بعدی آماده‌اند، اما معنایش این نیست که لزوما امشب یا فردا جنگ می‌شود، اما منطقا و عقلا باید برای یک جنگ دیگری آماده باشیم
🔹
حتما برای دور جدید درگیری با دشمن آماده‌ایم و تمرکز کشور بیش از آنکه بر حوزه مذاکره باشد در حوزه ارتقا توان دفاعی کشور است. هیچ تضمینی وجود ندارد که در آینده جنگی بر ما تحمیل نشود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/659477" target="_blank">📅 23:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659476">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
اختلال گسترده در سامانه‌های جی‌پی‌اس سراسر فلسطین اشغالی
🔹
رسانه‌های رژیم صهیونیستی از بروز اختلالات سراسری در سامانه‌های موقعیت‌یاب جهانی (GPS) در تمام مناطق تحت کنترل این رژیم خبر دادند.
🔹
این اختلال باعث از کار افتادن یا خطای جدی در سامانه‌های ناوبری و مکان‌یابی شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/659476" target="_blank">📅 23:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659475">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzC7lr2Vl--BoXaxfUqZSmt7-qHTW1yyCCR0ZXpMtnBACzAcStfsB2IPqcdp4dUrYer8Jzjbazt6nT0eXBoMOzKSCfVkCPhqM16cyj0orXLGyk3v5Xb1_Bml1Z0gkXwPXgKAihQkXCZyMMaZCHj9sG3jAJSgl5qQzytJx4MjV21tdoZZ87QDOwHFZQbi8U3f1owKgFEfMrDOmZYPECyCri7z4iCj3tsJavJ4Win-n4f5X68Q1UHibq8K2ESrgZZAbCqD5RKsSLLPqgBHQg2zbhLVQvMoyAz70LdsqmVItDoOieolbIA4BGh8VBAl2uJIuG4Ga6GowFCsqo2Kj4CpGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخبر در واکنش به تجاوز مجدد به ضاحیه: نه لبخند دیپلماتیک آمریکایی قابل اعتماد است و نه توحش صهیونیستی قابل تحمل!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/659475" target="_blank">📅 23:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659474">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
جی‌پی مورگان: طلا تا پایان سال، ۶۰۰۰ دلار می‌شود
جی‌پی مورگان:
🔹
افت طلا تا محدوده ۴ هزار دلار، پایان رالی این فلز نیست. این بانک مشهور و قیمت‌گذار با وجود تعدیل برخی پیش‌بینی‌ها، همچنان انتظار رشد ۵۰ درصدی قیمت طلا تا پایان سال را دارد و معتقد است در بلندمدت حتی رسیدن به ۶ هزار دلار نیز دور از ذهن نیست.
🔹
به باور این بانک، تنش‌های ژئوپلیتیک، تورم، کسری بودجه دولت‌ها و خرید بی‌وقفه بانک‌های مرکزی همچنان سوخت اصلی بازار طلا هستند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/659474" target="_blank">📅 23:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659470">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kHfvPQ5RsDSU9cRZ4-kO6zwn9bZQkkh75GxB0Bx6JQJ_Q7jZHSgIgWSh5C_O8oy5b-d5lhOEANGe1_E--LCKWqDDxQPW_UCk_TUng_HG5nC9P4lqQhFXbD16yGbjRfnBWYzOVhSMZgmciffCwO_iYlmLGDTsZLqtUtA3nbhdF0vqz7gbzTQ_g4ly4LJDzGuDN0JILb-lFeSoarGAYGAvnfkCcm02gMjQAyI01OzXRS0loanf6wL-Jod3_k9RsO1HdT3JUSyBI-PwAzM_onS3GDDbM08EPrfvsqdNEV24wqWxD3tPetoQkrd7m115TLfSgQoJdYqs5DJbDKp-9MfaZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ueqPc476RvWlKpuWMVCsSYA9ftTK66K9edTknbYVRlLTxopKSJoyjqdeiQLzKFI2OEnN9tfjJvnluBlHUtBg6M_DgsOqh-UqyhJxxcLMKR5tfivXiMQxoOJYz1dAEcblYwryR-H89HoOafQsUDsiHfxV6TuEXp3w5OLGunKsqIhZCW1acXawdjMgs64yK7OClOczAApO_34IvgPTkKsSq1IYWAXVnWQNabHc6LrETtTBHPsQY0SldzoNefBXch97FbKNxm1ov8UOLDmhsA6amTepiQ9-yTIsQBBVl7Zcl92XEQx5q1VuMyE7hy5qvJH0Ptk_RgwS-Es5aoRfDrpcGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRjbXBBcDJvAsvzHCZMyQiWmY28HTSKOYiKE4qu6KUgrHNqO6ouwKTaVOQFjRJMobLGP3BI9uAhpimHntEbXX2yq20H-BQx_6d1XVoA8wmTn_5i3sTT2TiqLK47T1O7rJMrf-ngiIx0msMcEqiaU9bHpJb8H8LYbYQfQ0tiBZfRFTsuev_aR9lEIJz1YeD9L25bGhDBwybUcBhHRvIk2CXCIyUyab-0jNbAacokna-c8bQBcrrInBTmBD1ibZf4xo9ZJ3edDqhj5pEeUXyg7d05orv7ybyxP5AJxh6yRPSOVMxBAELQI_450M9wstV32Oyulnj-4p2wagpWSHmDnnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MvFQulMEdgsvgXF8ErF4QDqaHu6RAlWAcuULTWl6bKPZqOdGP9i1c5onDRXQNAXe8nbqdqXuWPWyZBuboONjmFzxpCYj6p79fSS4oEDQKORD_EUAh0kTpvMTLA98i0QUKAjUOioeVhQv5SdLa7lswmOyoFJbQMzpY7UT3yRR8-JMqGzGemDgjUXQm-5ieJt8iBkY0iU3f3NdZcdR7fyM0klRlpRWXH767oEtvTTlWlo_dS77Gy-VuVAdNFJHv2krBdBEeXWt4fyh8CoivSd4yCzuFMD5DiFv_mbARtLkVEq7aYv7R5OT-WebnZ5MdugeUHowknew8VFB6Uexrlk4lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از عزیمت اعضای تیم ملی فوتبال ایران به لس‌آنجلس برای دیدار برابر نیوزیلند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/659470" target="_blank">📅 23:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659469">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_MnaH__g4bKNmIAbVgklcmjeB1cwuSkT2ROk1tHr70PFa6D_SuQpwm8-2FA1Qg6YqaR4Y3TEKFOMFsrsu-FUrIwKVTI7Gn3QD15sX1QcY1PKbgRuFsQJA8nIXFYXZnNZgMLwaWrdCjacO_ANKBAQZdRdSK88LHQntNWWSy9N5mK37z7YpfNdckrkCr7SgrMhkTDkhr_SMnDBE7IAgJV4n8ZKyK-vP5Kqdobz1t87H8g0N-cMYiYVDDZp7ETwOGplPw6GP-dVIkUJQMGw8D3zK_BOw9WBW--mqho1otn6IAzPKr4WaLJUAVFCquj1XlTreQfun4FXcOcMvTJcar8JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلاکارد جالب جوان عراقی در حمایت از ایران و لبنان
🔹
«ما از عراق قلب‌هایمان با ایران و لبنان است.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/659469" target="_blank">📅 23:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659468">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46eeb5f33b.mp4?token=GQ13resFYw7XgcMqltXh3dBVeDVE21IcUDu1kwJOU3GtfWlnufPpy0LcCtRwvz5zUMHq5OtIDm3BG5JKHHd29j56ZhxAqNRAWPFqUa4leb9tYyYvN4-feB7LDgvfTKWxXwt8FBtju-J1EcpAXMVDMtJ4N_-G6A_0Yy2Mqq3rahhLAOFUD2__Xm2ViP2UJh5ksvF7XXTTsnNhajjwOTBIGKqfXGgy11gz_wb4ePZ5CbD5dvT163RD4GQzk_QwyJFT0e45zN2qjY6ec5pMjwCoVLdY7JzvnyGDZbMk4jHj8s1kxsOKADEavRrcWwHbxr72ZKxgWXqM0QotPrVIeQlVTnrf-Y5YyYMIdYMOVjoUw51lyinGCyem7yKfRdNbwUavKTtgpqKQh7Lz99LgrFNtfWD99mI4rKPBOxYK5hoZv2MoP_aw0Pwr8d-3h_UV8C_GFZs38CQlc4tilYp72ia-6dFu7YYTeW-iW4-Iesin-qHKv6aJs4s44SScInrtRxPbZM6Q7gFh1575Q70_hYpTPzOkqvfKv4KuaW9C9NBRxfTMutnE7YqBmlA-Mp8ke_h1Ix55F_0SJ0aGda8t-46MAisgWp23GQyxS4sSbItcBI7LNxE3nIrp40h62AVKBu61QYLo3CbXXaxrjD6j7Ww0ZSYx67jsSj0UIybzwBHjA1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46eeb5f33b.mp4?token=GQ13resFYw7XgcMqltXh3dBVeDVE21IcUDu1kwJOU3GtfWlnufPpy0LcCtRwvz5zUMHq5OtIDm3BG5JKHHd29j56ZhxAqNRAWPFqUa4leb9tYyYvN4-feB7LDgvfTKWxXwt8FBtju-J1EcpAXMVDMtJ4N_-G6A_0Yy2Mqq3rahhLAOFUD2__Xm2ViP2UJh5ksvF7XXTTsnNhajjwOTBIGKqfXGgy11gz_wb4ePZ5CbD5dvT163RD4GQzk_QwyJFT0e45zN2qjY6ec5pMjwCoVLdY7JzvnyGDZbMk4jHj8s1kxsOKADEavRrcWwHbxr72ZKxgWXqM0QotPrVIeQlVTnrf-Y5YyYMIdYMOVjoUw51lyinGCyem7yKfRdNbwUavKTtgpqKQh7Lz99LgrFNtfWD99mI4rKPBOxYK5hoZv2MoP_aw0Pwr8d-3h_UV8C_GFZs38CQlc4tilYp72ia-6dFu7YYTeW-iW4-Iesin-qHKv6aJs4s44SScInrtRxPbZM6Q7gFh1575Q70_hYpTPzOkqvfKv4KuaW9C9NBRxfTMutnE7YqBmlA-Mp8ke_h1Ix55F_0SJ0aGda8t-46MAisgWp23GQyxS4sSbItcBI7LNxE3nIrp40h62AVKBu61QYLo3CbXXaxrjD6j7Ww0ZSYx67jsSj0UIybzwBHjA1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود اضطراری «جی‌دی‌ونس» به کاخ سفید همزمان با اوج‌گیری تنش‌ها در
منطقه
🔹
شبکه راشاتودی گزارش داد در پی افزایش سطح تنش‌های منطقه‌ای و نگرانی‌های جدی واشنگتن از تحولات پیرامون ایران، «جی دی ونس» به طور فوری و اضطراری خود را به کاخ سفید رساند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/659468" target="_blank">📅 23:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659467">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_RhheZ_agzM8sYluTfcMvAN1P8TP256-wAdA33AU-kBwAPcjlO4e-NK37TZhSVu4sCFH69w-YHKZQKnVfomyDeTYB8ooDY3OWFAQFv-r15wbhmj2r2eomib5xMxWQdimk72LE3KWXE_EMcQDB_u7vosxmV8Ozi58URHTuyL2B43Ix1xfSXjwnpzvhqzmkSH5rPeXQ_03F_X2D0NKuF5q9FTCSUG3f3K09IHtt3xTBTeCIuUVNuebO9FzfvR6UDaXRN7xTE2q_I8Vt1biQTzin6uKK50_zeVms4dKQSAA7hoQBnL6nwr0qtiuK9fmwrvIIr5pGTn0A5ib1h-u3gr7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتشار برای ‌نخستین‌بار؛ تصویر شهید «حاج علی موسی دقدوق» در کنار شهید حاج قاسم سلیمانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/659467" target="_blank">📅 23:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659466">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0Z2fQ7OFzIe2lVfeNBbCZRYwiHP_6upb5kDtMYZ8LYjMiPv9jyxTYqhVYvAHrHpsdmSxXDf6rdU5ppwv_5VueScXEukvmo5ZHyvQYljsNYvyFRP54YrrS3KrD1rHgEFdmF6mOVL0cTaz5wPYM1bB2etuf4tp91YFrSdRZHHgXxPE-FfPzHsrHW3iEKkygnF2jRn4oyfJ7ecvgDAzo8TWoGwtSzStGM5jtpIbows3uIXjmQV5hEqA2t_acWoynIfg6kzOPRI3n89kEQWDcS1Lplk0cDQcgNaaoMTePMpG3X3m8mpJ476JqGLbNPCc-w250UznpOA1OK7JCck_KhaTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه درباره تداوم جنایات رژیم صهیونیستی در حمله به ضاحیه بیروت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/659466" target="_blank">📅 23:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659465">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufIMmVtCgjjXZgDJkVMJjfbgUjOKCZ8zXrU3sdHamNCQHdfgl_T0fW-_VT8ii6SEgsIX_UapJj8NEa_diNhQTvsQpkIz5STtSyNB1wBKr1Be0j-e3FumovosWdhAFx4gpn7Znpndfps3WK6gxwtKDlX2oXjnU9vA-OIhlKRGFEWyr_cqzXNpdiJsMdFJJludVzmtTCI5xynuMztacuN9ssRLZjR5dObpYuWjVUjJZJNcnlkovdZv-2lNgl2U6Rczs-nj9WVt0vKWF6rK5mjMoMyqWh0OQexXFVNpVhZh0CbQMDnYdXrQVinVR2oygvadUIGnVo2crQSa9fv98hQTDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درخواست کمک آمریکا برای مین‌زدایی تنگه هرمز
شبکه WRTV:
🔹
ایالات متحده با پیشرفت مذاکرات ایران، از گروه ۷ برای مین‌زدایی تنگه هرمز درخواست کمک کرد.
🔹
ترامپ برای مذاکرات گروه ۷ با مکرون به فرانسه می‌رود تا در مورد توافق صلح ایران، مین‌زدایی تنگه هرمز و پیشرفت در مورد اوکراین و هزینه‌های ناتو گفتگو کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/659465" target="_blank">📅 22:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659464">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
سه انفجار مهیب شهرک «الطیری» در جنوب لبنان را لرزاند
🔹
نیروهای اشغالگر رژیم صهیونیستی در تازه‌ترین تجاوز خود به مناطق جنوبی لبنان، شهرک «الطیری» را هدف حملات خود قرار دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/659464" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659463">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
اعتراف رسانه رژیم صهیونیستی: حمله به بیروت با آمریکا هماهنگ شده بود
شبکه ۲۴ تلویزیون رژیم صهیونیستی:
🔹
ترامپ از حمله به ضاحیه جنوبی بیروت عصبانی است اما این حمله با آمریکایی‌ها هماهنگ شده بود.
🔹
درست است که اجازه موردی برای این حمله گرفته نشده است اما با توجه به هماهنگی‌های قبلی، اعلام غافلگیری یا تعجب آمریکایی‌ها قابل درک نیست.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/659463" target="_blank">📅 22:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659462">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
سناتور آمریکایی: هیچ تهدید قریب‌الوقوعی از سوی ایران وجود نداشت
‌
سناتور دموکرات آمریکایی:
🔹
اگر ترامپ می‌خواست جنگ علیه ایران را به‌عنوان یک جنگ انتخابی آغاز کند، هیچ تهدید قریب‌الوقوعی از سوی ایران وجود نداشت.
‌
🔹
ایران هنوز موشک‌ها و هزاران پهپاد زیادی دارد.
‌
🔹
به قیمت بنزین نگاه کنید، از ۲.۸۰ دلار به ۴.۲۰ دلار رسید و من معتقدم که قیمت آن بیشتر هم خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/659462" target="_blank">📅 22:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659461">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
ینت اسرائیل: دونالد ترامپ از نتانیاهو خواسته است که آتش‌بس در لبنان را اعلام کند و شروع به عقب‌ نشینی نیروهای ارتش اسرائیل نماید تا ایران پاسخ ندهد، اما نتانیاهو هر دو درخواست را رد کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/659461" target="_blank">📅 22:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659456">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rBLU3WbjI8gCAHRT9KQC6Go4X26zttfOknb0eKdpfAWiQgtZWJ3Z-5kv7nWtjC-nJmbmoe7chV8AVSEHj1-jFZzpuRrPBxVUKbws70Uw3HX_SIy3PBdBsnFbU2npsJ6s15m97ttIV_Z2bk3JcEgskmk9psLXsHV6omKUlNKHd9maVfkCEojsN4KrfBfL2Pd34Hj9S_Ph85hwrL5NUk2IXmzNIMAvNc13UqQQa0jWSXkV18GjbXbMMfuY14JABVt29o7iMWqGL_1KNQP78ZZiq6oTmFCnZZkgZLj-j-i-fZcxj78UhGGbzbNyrKh8W5SiZ3LYV9WhrbUVbKgXTHSyWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ffGifxHmSLMz3L1fuLGoUGJh8gIlhGLeV7XeyNBLB0Vntyd4kAya5GRCYHnj7BgeKZ7YZkc5Uek3sR8GFJkJZivk9j76-sPcFzv2Ecw2eECPbEg7EDsuiCJNangrLr6XtM_pKZNX2ZWCqHSuBim85_SC4aIKaEHWqcgWUGuJirZ6JG9qPpJXftfzx5XB4JWEuju2ozooAceQV_iODuU82oPgxt2MPlTqPrEkioagl8Pi0G7b9sIQ7XXCEQTziRYWxsmJCkp9ni2JxjaLqBh9a-SP_YhUeFlfCAqDBcz5n97cu0cNrGq2vQfaUtcf14LPykGMVfF3jintqqirjgi9CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AC5mMRMZl38SA7QWLLa0NPtrETgiYjUpp3ZE6HfAcHGLbPOONYmRBGOa4vAgBBvcEi_vtJLkWxsbWz-s30yHhXSu64orgtNLjpIYbfSuKQ6RlVYMIQoAbr73RoOU7luT2lmQPVXhw2L-J2v7KwHB7T8oXS1L4_QjYybFi1SbP8HRfTyPG0qoI_YjQcrt4AKKkEZdxSK19cO0N9ul7bMzEeFHwwARL2E23Fsanoz8dOvPA-4VcayBBxgBodANtU9CcP7Oue9tq5MfWdFanQuZ4hWRxAkF36l65hyq__O1RBltPdEhIGng-rIgPoOOHTSaZ1k5EedBQo5aoQyilkE5jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/joMrkQjcplX40CFrWoKph4WVAqKNsmNS_Neg8W5RhGHN1J4YqTp7E8RxQ_0Wpq9NotvYov350_BSUQ82BaH1tCnx8ttaCd2jtDWREb7CBcGjrkCaSaJvTg7iWbJ-Jd4V5efmhqUR883uxeaQ3MLw5tAQjUF2ckVRyf0kPtOdxmWlinrqEWqkHbTqgL63WoKUbrGQ1WZBp4P8uewacDsg3LgHDdLJYMjsolLNrO7O2Yt7Yhxl8WfOBz7ugwpr-F0PH6Odafs1KkaLd1vC3uSRCYA4SJa7SHRhuFtRwYeWotsgIv_0JJT_d2pAdPTZXwruNroxzvysnL7UqZiAbYv55g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oAA5fVOo61ZNxPcIRtMBQfszab-E2Y4TlUaBkas5gemjNUcAJa7WA2qJdtBtVFJIWY-SBOCyxrz8lNSaLAqhzP58gfeguz-YXOacUVtjshCPfM2dE-i1zzUg6MI_ojq1BuNimxYRtH_9b1SVYPCC6UAXZttf1uHiGDyaNqzaI94Ub3N9e7JrvLBYBnuuFBK4fkF638Oj_NA3OaeXCbaryb3399uamoFKIVgCQAglMWBvE_MxLg7l-DImNljEBssOHdLR5Mg0j2AcZSIWWiD1ex0XQkXGWGVDcOosCh38Fro_q_0-tbgwalCuEeuesTMCc-ohR2_yYOqT14UJJOVjog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چرا نفت هنوز ۲۰۰ دلاری نشد؟
🔹
با وجود اختلال در کشتیرانی تنگه هرمز و گذشت بیش از ۱۰۰ روز از آغاز جنگ، قیمت نفت زیر ۱۰۰ دلار در هر بشکه باقی ماند.
🔹
این در حالی است که در روزهای ابتدایی بحران، برخی تحلیلگران از نفت ۱۵۰ تا ۲۰۰ دلاری صحبت می‌کردند.  پس چه چیزی مانع انفجار قیمت‌ نفت شد؟
در این اسلایدها ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/659456" target="_blank">📅 22:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659455">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jz2hgawWGBF1P7lFKvDTuK7JLrLmCDCR9szd6lnqUnvjJTH-EIAPnQtsjqYPoah3UNApBSGRv05sNzMnkStbyo4VcKener0NXQeDNmTAGhD2Qdc1-Dix86Lqepegj6Oi47H6Syy1hadVDyFcRcygpp2l-QacZ-NmuiXoL46WphapwOl5aqmW9kNxkg1bSL1T37W22g6XYYYFAKO1gErrNgZLN4uwvs-f_wyysaEkb3x5fiuVzzTcK5om5bR7g1_OR6UNbzEgrThkQrjDPqJHyJ7zgt6Yx-s8WSDHI9nBdUqYJ3MO4E7zMFv6m_B161r_Sw-ml0bVQmREGRrfd83KBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: هرگز نمی‌توانند هیچ بخشی از ارکان مقاومت را تک و تنها گیر بیاورند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/659455" target="_blank">📅 22:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659454">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
هیچ نوتام جدیدی درباره محدودیت پروازی صادر نشده است
مجید اخوان، سخنگوی سازمان هواپیمایی کشور:
🔹
درباره برخی اخبار منتشرشده در فضای مجازی مبنی بر صدور نوتام جدید برای محدودیت پروازی در فضای هوایی کشور، اظهار کرد: هیچ‌گونه نوتام جدیدی در این خصوص صادر نشده است.
🔹
نوتام مربوط به محدودیت پروازی در غرب کشور، همان نوتام قبلی است و اطلاعیه جدیدی در این زمینه صادر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/659454" target="_blank">📅 22:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659453">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/615a222da0.mp4?token=SYtotm3rHDM1ZOUEANsXP5RVkB2-2c5XCq_WkEbZUzWslTDGV13eY582_dy11XWrAbCnsBmF2EKFuExUSE2VKUJLibY3YY4faIwtZJ9X4h3wQqbClyzadxS9LFUPZYgQZMPkYtbDpSzlDDnwiS9yhORTVe4vR9vfJ-7zQ-nocZYMqx4_DjuqQ6-oUt3rYhja0L4QwXj8EAUDm5vnTs81pk9vPnna1tL1EkfrvD_Z9L3aQdV818yk0Vgk_qLMnjCr2G8i4ZN7oLHchQGjWgKkAg7-mO3cAduuNaIWyBLkGOff7X_nlWLbQ_IBFCcQVxJilYEsmfCR364xZ4-GRxPMcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/615a222da0.mp4?token=SYtotm3rHDM1ZOUEANsXP5RVkB2-2c5XCq_WkEbZUzWslTDGV13eY582_dy11XWrAbCnsBmF2EKFuExUSE2VKUJLibY3YY4faIwtZJ9X4h3wQqbClyzadxS9LFUPZYgQZMPkYtbDpSzlDDnwiS9yhORTVe4vR9vfJ-7zQ-nocZYMqx4_DjuqQ6-oUt3rYhja0L4QwXj8EAUDm5vnTs81pk9vPnna1tL1EkfrvD_Z9L3aQdV818yk0Vgk_qLMnjCr2G8i4ZN7oLHchQGjWgKkAg7-mO3cAduuNaIWyBLkGOff7X_nlWLbQ_IBFCcQVxJilYEsmfCR364xZ4-GRxPMcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روایت جذاب از مسئولیت‌پذیری و همدلی؛
🔹
این انیمیشن یادآوری می‌کنه که صرفه‌جویی در مصرف برق، یک انتخاب کوچک با اثری بزرگ برای همه ماست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/659453" target="_blank">📅 22:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659452">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImKZdOikNP9Pn69UECaQo-A2AnSqjZE_Zena2zkml7eMtuHF4riFoCp80RtthSEsQnNSSVrBOQIVGPdJSGncW9CO5DrverqDTSVCCy1Tk8VwxrU6f0vx5zc87ciIkICDbJIRztU_0L_1yJizn_11_kQzFUeSoRr1W3mqsMDw-gGiQGriDGYm1UXMAoqWFIVwS8CUhJkwrfB2boWQpzlm8-kLHxOOglMNlUXhX3QNkTJQCDP9LDFzB57cb7rczODByd-TVRmC2DRz85Q0gbZqYstk7UTpRlN1C6cgD7AfLk-1Okt_cm7c9GmdJ5S3oykoJoHN-g1VSvCTE3FFT9DTYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مراسم رونمایی از اولین لابراتور سیار خلاقیت و ساخت | Fab Kids (فب‌لب کودک) به همت سازمان فناوری های نوین و نوآوری شهری شهرداری تهران
🔹
فب‌لب کودک یکی از مدل‌های تخصصی‌تر و نوآورانه خانه خلاقیت است که با استفاده از آزمایشگاه های سیار و تجهیزات فناورانه مجهز شده است و در فب کودک برای تقویت خلاقیت، حل مسئله و مهارت‌های علمی و عملی کودکان راه اندازی شده است
📅
دوشنبه ۲۵ خرداد
🕙
ساعت ۱۰ صبح
🔹
شهرری، میدان صفائیه، خیابان شهید طبایی، مدرسه وحید کیهانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/659452" target="_blank">📅 22:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659451">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca0d181bb8.mp4?token=arw64IiWMA1kOxd_c3WRRC8xejS9Wu20gYq71YN7jPlne5T6vRv9DXyud2ZvjPfT2vb4yfLzGJEPhFGOsVn1lRSu1FI92l1k0OTONMD0da-_0qnhJMpLSjca-iaIQp9DqiIvf7T18bXv4gjRmY-h40vxm8ACim0MHIm8SLsf5jWt0rysaiEQ83hUkEdA5Ht48ce5Ib_FPTIWkTBjq2k1y2qSOf7FEdjcA2I9EJEydabK0Z8SNvk9_tY_oSebUVHrgezO-q5wmLrB60MlhzcVlOKbIfv7Z0VNcHkocGsSj8_qmsNdWCleEJ3HQcoAeIApBK92WIiTDxOim0YSYVS7qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca0d181bb8.mp4?token=arw64IiWMA1kOxd_c3WRRC8xejS9Wu20gYq71YN7jPlne5T6vRv9DXyud2ZvjPfT2vb4yfLzGJEPhFGOsVn1lRSu1FI92l1k0OTONMD0da-_0qnhJMpLSjca-iaIQp9DqiIvf7T18bXv4gjRmY-h40vxm8ACim0MHIm8SLsf5jWt0rysaiEQ83hUkEdA5Ht48ce5Ib_FPTIWkTBjq2k1y2qSOf7FEdjcA2I9EJEydabK0Z8SNvk9_tY_oSebUVHrgezO-q5wmLrB60MlhzcVlOKbIfv7Z0VNcHkocGsSj8_qmsNdWCleEJ3HQcoAeIApBK92WIiTDxOim0YSYVS7qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد دو بالگرد در ریودوژانیرو برزیل و جان باختن خواننده معروف
🔹
بر اساس گزارش‌های منتشرشده، اولیور تری، خواننده و ترانه‌سرای آمریکایی، در پی برخورد دو بالگرد در جنوب‌غربی ریودوژانیرو جان باخت. همچنین در این حادثه ۵ نفر دیگر جان باختند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/659451" target="_blank">📅 22:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659450">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77d995e7c9.mp4?token=I0rhmWUPoHc2AmePyao_d_XD2kzZIdz3JGUYPi8Wczeq_8deqmuw2lcfmiUjPNB9oHPuhWk5j-Yya0LXFZJbpMXI97x4gGxqtvt9bLKsae33FVxDU3mBlKRnJeFyRatEdKFdiB5cczNa75DscKQypCVhFv5Jkw24GpG8VoMRNEZuB3SNkwxu_XZM8mUBkU9p9NZFepdmKXthZSayQ8Gd2c4tL8Z4W18-fyxdn4gUlH6MkF7aziqTCR-bZb_-rkYhC5WyDWADQbBckMN3DZDypQU08-Ehj6XaozwSY_nGedD4ApCkrENGcBKuN2j7BdYiD8CLwK9dhMAHiXpeKdmTGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77d995e7c9.mp4?token=I0rhmWUPoHc2AmePyao_d_XD2kzZIdz3JGUYPi8Wczeq_8deqmuw2lcfmiUjPNB9oHPuhWk5j-Yya0LXFZJbpMXI97x4gGxqtvt9bLKsae33FVxDU3mBlKRnJeFyRatEdKFdiB5cczNa75DscKQypCVhFv5Jkw24GpG8VoMRNEZuB3SNkwxu_XZM8mUBkU9p9NZFepdmKXthZSayQ8Gd2c4tL8Z4W18-fyxdn4gUlH6MkF7aziqTCR-bZb_-rkYhC5WyDWADQbBckMN3DZDypQU08-Ehj6XaozwSY_nGedD4ApCkrENGcBKuN2j7BdYiD8CLwK9dhMAHiXpeKdmTGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل هفتم آلمان به کوراسائو توسط هاورتز ۸۹
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/659450" target="_blank">📅 22:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659449">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42d742fffe.mp4?token=vqDy1BKeLFhrkcoTgzCfg4V2mLXXt_KaIohsaRkvp_87STKnLHpgkzhpJDVh_kvKqY-kpFDgAx6mS21F9aDMbLTb81wlH8R17gg1_u13IMF0AD0dluSCKq9hCGz15U6UblNHp7WYlzQf0BQyYehIxg8ujZ3GbPKdPJuHNuu-tqQgiLeZIPHcq5CRgh8ebs4gMi4_hRUQgJKuLJwMbVHS3pA2yvWxE7Uu_OjE-doneO-gghm2ybFD8W_4KvIzLFIEPDIZGFAzriy_7XYxihn60K2R6M3mJM8xn8HkflyMrewPeRi2cyyCgPtehDFutgJTVTh9wXLNeGD0FXxNnyLMtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42d742fffe.mp4?token=vqDy1BKeLFhrkcoTgzCfg4V2mLXXt_KaIohsaRkvp_87STKnLHpgkzhpJDVh_kvKqY-kpFDgAx6mS21F9aDMbLTb81wlH8R17gg1_u13IMF0AD0dluSCKq9hCGz15U6UblNHp7WYlzQf0BQyYehIxg8ujZ3GbPKdPJuHNuu-tqQgiLeZIPHcq5CRgh8ebs4gMi4_hRUQgJKuLJwMbVHS3pA2yvWxE7Uu_OjE-doneO-gghm2ybFD8W_4KvIzLFIEPDIZGFAzriy_7XYxihn60K2R6M3mJM8xn8HkflyMrewPeRi2cyyCgPtehDFutgJTVTh9wXLNeGD0FXxNnyLMtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: شورای عالی امنیت ملی با قاطعیت مصوب کرده مذاکره کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/659449" target="_blank">📅 22:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659448">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtlW2lyRaZKYoLfS69GFmb0txjWbuPI7Zedq7AVeml1JZqsgC6HE5sGq8QIgrbpUs24zG4lRjs7MyPjpEL0irJCJ_Ek8Uk73EwBs6B7-P0Dhwjc8cwVY2zLZfrkTk48mwgPO90wdNRru6XXLEUVye0bPfm81eaj4nkjtcSPKXZHFeEkMNNa6FG1W6Hdoc21Z-UqYXm3pHXvIUVuMurt6ZtGALhg1gw-NgoCOei5DaOI5EcQRsrLUs4Bqevy-sx21sd3liEN3eQhJq5WuAI9uydL6phhMwDuaAYvT7C3u5ze8Dhla4R0YqAgOAd_YrLhKZa2MCGHqB1nQkWOyugeO-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
از فرشچیان تا کیارستمی؛ مروری بر شب درخشان هنر تهران در حراج کاویان
🔹
عصرگاه جمعه ۲۲ خرداد، مجتمع ایران‌مال تهران میزبان رویدادی متفاوت در عرصه هنرهای تجسمی بود؛ جایی که حراج خصوصی «کاویان» با حضور جمعی از فعالان اقتصادی، مجموعه‌داران برجسته و علاقه‌مندان هنر برگزار شد و مجموعه‌ای از آثار شاخص هنر ایران را در معرض فروش قرار داد. آثار ارائه‌شده در این حراج که ارزشی بیش از ۳.۵ میلیون دلار داشت، طیف متنوعی از نقاشی، خوشنویسی و اقلام کلکسیونی را دربر می‌گرفت.
🔹
در این رویداد، آثار هنرمندان نامدار و تاثیرگذار هنر کلاسیک و معاصر ایران به نمایش و عرضه درآمد؛ از جمله استاد محمود فرشچیان، غلامحسین امیرخانی، حسین محجوبی و حجت شکیبا. همچنین آثاری از پیشگامان هنر مدرن و معاصر ایران همچون منصور قندریز، پروانه اعتمادی، ژازه طباطبایی، نصرالله افجه‌ای، عباس کیارستمی، کوروش شیشه‌گران و صادق تبریزی در این حراج حضور داشت.
🔹
در کنار این آثار، مجموعه‌ای از کارهای هنرمندان شاخص دیگر از جمله حسین علاقه‌مندان، منوچهر نیازی، علی شیرازی، بهرام دبیری، رها محسنی کرمانشاهی، علی رخساز، محمود زنگنه، ناصر اویسی، خلیل کویکی، مجتبی سبزه، علیرضا آقامیری، رضوان صادق‌زاده و محمدعلی ودود مورد توجه حاضرین قرار گرفت. همچنین اثری از «آدولف ویسز» که در سال ۲۰۰۵ در حراج کریستیز ارائه شده بود، از دیگر آثار ویژه این رویداد بود.
🔹
یکی از نکات قابل توجه این دوره از حراج کاویان، عرضه اقلام کلکسیونی در کنار آثار هنری بود؛ به‌گونه‌ای که علاوه بر نقاشی و خوشنویسی، دو قطعه جواهر دست‌ساز اثر ریتا نیک‌فرجام و دو قطعه شهاب‌سنگ کمیاب نیز در فهرست آثار ارائه‌شده قرار داشت که بر جذابیت این رویداد افزود و توجه مجموعه‌داران را به خود جلب کرد.
https://B2n.ir/bu5751
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/659448" target="_blank">📅 22:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659447">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ebc07bf83.mp4?token=DnV6t028VGXpQmNCSHf6t4zcgGTEJyrjyBs7tNMPaRfAmaWwIhJrac2FergwR8jo4gpbFeUZinpr3uNlQ_JW3qG3JOgDVAPjYeMYxSZCm154TE6_b7v6G2EXIkwiAp0FA6cAssf9jI0m247WvR5g1Ro94nWcghgnHzQPnYriePTA6M_ijdmp-hIulhlMgDI2dm0jTq8QtTp5LVgWaMlmGi_KOihASs03irTzEq1jhtBZ0ue5i59hvvJIdT-5w_aWJThaAHT2Z12ABZsJdt5_jbxBCXeW7O4_VuCWwCVeJaVJr-DfZWtvvGsrll3oUWgzxt4Zn00s3Urw5qRFSrhEWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ebc07bf83.mp4?token=DnV6t028VGXpQmNCSHf6t4zcgGTEJyrjyBs7tNMPaRfAmaWwIhJrac2FergwR8jo4gpbFeUZinpr3uNlQ_JW3qG3JOgDVAPjYeMYxSZCm154TE6_b7v6G2EXIkwiAp0FA6cAssf9jI0m247WvR5g1Ro94nWcghgnHzQPnYriePTA6M_ijdmp-hIulhlMgDI2dm0jTq8QtTp5LVgWaMlmGi_KOihASs03irTzEq1jhtBZ0ue5i59hvvJIdT-5w_aWJThaAHT2Z12ABZsJdt5_jbxBCXeW7O4_VuCWwCVeJaVJr-DfZWtvvGsrll3oUWgzxt4Zn00s3Urw5qRFSrhEWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل ششم آلمان به کوراسائو توسط اونداو ۷۸
🔹
گراد؛ انتخاب نسلِ شیک پوش
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/659447" target="_blank">📅 22:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659446">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ادعای کانال ۱۲ رژیم صهیونیستی: ایران درخواست ترامپ را رد کرد و تأکید کرد به بمباران بیروت پاسخ خواهیم داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/659446" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659445">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
لغو پروازهای غرب کشور تا اطلاع ثانوی
🔹
پروازهای فرودگاه‌های غرب کشور تا اطلاع ثانوی لغو شده است. این تصمیم در پی شرایط موجود اتخاذ شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/659445" target="_blank">📅 22:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659444">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6d836523f.mp4?token=D6x_FVWMAreJYtnU0EvKvvYNM67qshfTzQmCsKd1PRX2Nv7nqFswUwQu8lZSUG5ChdobCFSSj9Duo4VbhiMZmxhXz_kU9eeuKzWGD3XQh-tEx4XX_JaCeiFq_euwzrzd5ejshQMS9IY-f8htIsPxfsmbL0fw5AOUjVQn4jaKh5EFhSFQQFl-1lvm8IelOtGQdT6PylIkavbwsYkKAhe1_d49-v0budMIHpwOOvXnhnYDvsexth_I1a1eq285b5Bc1T8kRQyiW9g6OOMI18rGfAdczYwc-idfxzjkB3czvUrUhfUvbth9b17n8pdrBf1RANST7oScEf0IMjORNNP6ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6d836523f.mp4?token=D6x_FVWMAreJYtnU0EvKvvYNM67qshfTzQmCsKd1PRX2Nv7nqFswUwQu8lZSUG5ChdobCFSSj9Duo4VbhiMZmxhXz_kU9eeuKzWGD3XQh-tEx4XX_JaCeiFq_euwzrzd5ejshQMS9IY-f8htIsPxfsmbL0fw5AOUjVQn4jaKh5EFhSFQQFl-1lvm8IelOtGQdT6PylIkavbwsYkKAhe1_d49-v0budMIHpwOOvXnhnYDvsexth_I1a1eq285b5Bc1T8kRQyiW9g6OOMI18rGfAdczYwc-idfxzjkB3czvUrUhfUvbth9b17n8pdrBf1RANST7oScEf0IMjORNNP6ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل پنجم آلمان به کوراسائو توسط براون ۶۸
⬛️
🇨🇼
1️⃣
🏆
5️⃣
🇩🇪
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/659444" target="_blank">📅 22:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659443">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
اعتراف کابینه اسرائیل به بن‌بست راهبردی
؛
پرونده‌های ایران و لبنان تفکیک‌ناپذیرند
🔹
وزرای کابینه امنیتی رژیم صهیونیستی در ارزیابی‌های داخلی اذعان کردند تلاش برای جدا کردن مذاکرات لبنان از پرونده ایران به بن‌بست رسیده و این راهبرد کارایی خود را از دست داده است./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/659443" target="_blank">📅 22:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659442">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-6zK6JyDWONv1-VGMLG08emBhbQ9uHOl2PMQpKpJtGND1MbaQgx8rg7lFzEToriA_Qre96LXs1XF0fKQaZMioyVByidiFyyLzzbErP0xTDitukGSsLJDOG5JJgUnXDN9h7yCSkAiwzyxjim-O1frqa2amE6joAmxZbl2HZXq48UGi6rGXsqjZ0m8fs9orZPi92Sqzb8J3Pu1uJx0wlJlsjPoIRf9jIk0K6fZgL0M-xscHAmc5lexrLd8UbVCWQZtCMYTEKn-wmi6X4J9QOWkMFE-dunKsondAeWZkQWGIjmcSNiVXMuXrSmB1LeZG0I_34iCdOb_zgO0ZZBP-y0TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چند جرعه بنوشیم از حکمت صد و بیست و نهم نهج‌البلاغه
🔹
سوار هواپیما که می‌شوی و از زمین فاصله می‌گیری، آدم‌ها، خانه‌ها، مزرعه‌ها، شهرها کوچک و کوچک‌تر می‌شوند. آنقدر کوچک که در نگاه ما گم می‌شوند. ارتفاع، اندازه‌ها را جابجا می‌کند.
🔹
امیرالمؤمنین علی علیه‌السلام…</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/659442" target="_blank">📅 22:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659441">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYv8dZy0sdQTz7gEbddXS18Ip1JMf5KlrRijctpQ3TCxozu-s0dUSlvstAfsj7ad9tW4skaZsLnHsFKU0xcQcze-YiCsjAk4ZhIer3m2D06eHlF9i8UD8nDwFWuqBF_G_RNfMChJ7mVKcwqXLIvYROCUs3cs9hOWCzI2-plcVECq_QFZVtg-WZHu_PJGuxco5Zy4G65ZsXd5MIUT45vraUFQtJViqWUAbtblAwAXpgXlQ-w1BmpiNdqknVSoa2zxLx3pyuwuElW-QDN2HDEqJPRL0DtcZeFs_5Fpps5h6q4aoENl_gFLljMJkBE_5El0PtNpCa6EbAq8uVp8bav27Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وضعیت آسمان منطقه و ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/659441" target="_blank">📅 22:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659440">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3b1f60ac5.mp4?token=XMCmOfzH0eSzGEzCP3p8_oS7nQD8hqfUWZOTvrYvo_o5DpFg69zSS_Thv3f7OZaMfltMRA_f1tKD4HJ092oi-NsaKt73At8RadUZWpmAhjwYPpNLNADjLlCRZJeytlLdfgGdujXnfcfq9KP7B_u0aj3KvdMWTOBzyn2lgANk5k0QbHUPWQbEkTTsl5H53gYDz-ON5Ly22sa8WgL915PhuneEGoRI_iz7426Ai-wrZUfh0DBGp_2sZWmXX8cpy_IC4Ert91_kKZT4dUiCsCP9Uf6vo9QxqO3hSU7DFUb7Is4J40EROSL08L2yBUPPxEF3xwD_aRzPju_GcKUo71MfaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3b1f60ac5.mp4?token=XMCmOfzH0eSzGEzCP3p8_oS7nQD8hqfUWZOTvrYvo_o5DpFg69zSS_Thv3f7OZaMfltMRA_f1tKD4HJ092oi-NsaKt73At8RadUZWpmAhjwYPpNLNADjLlCRZJeytlLdfgGdujXnfcfq9KP7B_u0aj3KvdMWTOBzyn2lgANk5k0QbHUPWQbEkTTsl5H53gYDz-ON5Ly22sa8WgL915PhuneEGoRI_iz7426Ai-wrZUfh0DBGp_2sZWmXX8cpy_IC4Ert91_kKZT4dUiCsCP9Uf6vo9QxqO3hSU7DFUb7Is4J40EROSL08L2yBUPPxEF3xwD_aRzPju_GcKUo71MfaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اوباما: ترامپ در جنگ با ایران شکست خورد/با قلدری و بمباران به هیچ جا نرسیدیم و در بهترین حالت به توافق قبلی برمیگردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/659440" target="_blank">📅 22:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659439">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ادعای کانال ۱۲ رژیم صهیونیستی: ایران درخواست ترامپ را رد کرد و تأکید کرد به بمباران بیروت پاسخ خواهیم داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/659439" target="_blank">📅 21:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659438">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
واشنگتن‌پست: قطر «توافق مخفیانه‌ای» را قبل از جنگ به ایران پیشنهاد داد
واشنگتن‌پست:
🔹
قطر پیش از شروع جنگ ایران با آمریکا و اسرائیل، یک «توافق مخفیانه» به تهران پیشنهاد کرد.
🔹
توقف تولید گاز در ازای دریافت تعهد ایران برای حمله نکردن به زیرساخت‌های انرژی قطر.
🔹
هدف این پیشنهاد، محافظت از مجتمع گازی «راس لفان» قطر در برابر حملات ایران بود.
🔹
این سایت در نهایت در ماه مارس (اسفند-فروردین) هدف حمله موشکی ایران قرار گرفت و خسارت قابل توجهی به تأسیسات وارد شد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/659438" target="_blank">📅 21:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659437">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwJ7YdhvFsW3wJQuwdefWx3zupw8z6tFoV-4qnx_1smmQaF80jBvpj6QErEMP_QD2rmlJ2ET-U3h4ilEOh3Of6xyRota3MK0fEneH7T6lJLO3ZGtjqC-1as3k-2ElUOOZZbzvR7Ox-AA1n0sNGyO92N3aQRCX_pIFgOdSoh0rE0qEpegRYV3nm9b5wYmii_Hi9SVODvRt1i0entpyobowJeUaRkIp2c-l2yS0G7EHYbDltnbQh2oEZhoxf8bmotwohQYbVpHf6cVw2wHiPrMeJCHmMu-o7pgrIQcKBu4nQ9YPWgLzVJc9O19yOjtlb41Svl-UlYLcQsYqxU_JvPljw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راه خلاقانه آرزانتین برای برخورد با افرادی که نفقه نمی‌دهند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/659437" target="_blank">📅 21:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-659436">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
تماس‌های خانگی رایگان شد
🔹
شرکت مخابرات همزمان با افزایش ۴۵ درصدی آبونمان تلفن ثابت، اعلام کرد مکالمات درون‌شهری و بین‌شهری برای مشترکان خانگی از ابتدای خرداد رایگان محاسبه می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/659436" target="_blank">📅 21:49 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
