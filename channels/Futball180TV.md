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
<img src="https://cdn5.telesco.pe/file/EnJBuxfszWoaL-HsYuzSU6FxouckcfnR32clTw_UVdRzcM484bijDWNd2ZDEaZp2RJDQQhVWs5ZfgXOyLQVMzoTUc37SJNRE5iaqIxaqny37-6HSCL8ff_McrZedigrzlwErL1nTS72WFuP1rA1oKn3cmDYQt_5WKQo1819cxEMCyF-enUOxtiK7bglya_EgJKub8oKsfcaKaZOMv5vebAHrUcEX-6HWLoFA-8qQuLYm2yxJmStgT62An13BSy2KurbqFBveMQtdepEqHvuPJGuyFHVliG4O3pmJI5BoYz0AFvVJtyUYPcvf-54wckA-tExxpjOt-XAGCDlR4I7Q1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 705K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 23:39:52</div>
<hr>

<div class="tg-post" id="msg-95020">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q2R6u_1ChfKlcsqp45K9bRzeSdM6seinWLz-eoTTtrWSuR1gcg2p-V_DMsGAYDOC8AuUo0oIKhv0krJYzLAdrR63WxQVQ85JH_Et-mCS9crKhNZVeJVmLiMjMyNNnGzo5cMqGfnq7OovF-v1wVXk96T8MB6opTXP9-uQEJ5062fzpR1a293E8R9sH6uxfvxcq33BRdr8zKrnzeD3ApR4bSuaBPYffxvJ5a3Bu-zPE8X4HuZhkXlJmXXpKqp-oiDW90G2gET92lCBKJMQK3KBpx9HN9-nC8MTgvjwYEvRuHFsHqSAZprZSqRl500-OXLh3kbT64bZr6o0WZ9HPDx4WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kyBP_p9uP46qV7Hgj84bEp8kBleQ86PEPjQvSfiRQ270Ct8yMVJzO0FYbPyUJJDukJwiMTk3aKHgmBGaRZIBRh76NNC1A4V6lrnx8Om6GGp00qmhGbEjy91sqI4blDuL0XNPPYI_0nP8HWKF8pFDTi_LtTTRuz1mZ-xOmeaX-GfrUUc1KWbzY16NLj7clXZy7lZzaNv1hPsaOQwoHbPdjO8meiwHkum8wo1mcoC-3To8AYwQO3lNratOGxldu-R-yIZNQj9Ik3-xSrGP2xKHMS6gohLRpjvFNIFuzuZ6Qm9lP08lpzbJIf31LGa8WDcOLAEOp5QRoR8IdqlWRTrrTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مثبت فکر کن، اونی که حدس میزنی نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/Futball180TV/95020" target="_blank">📅 23:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95019">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بریم سراغ نیمه‌دوم بازی</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/Futball180TV/95019" target="_blank">📅 23:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95018">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOV7CxoVhthXpYQauwp7qrgMnb7qV--jxDcGzf1Zb02jV2l_dy5Z0NaZbPEH_43Tb9K8sVRRlfPokLJV6-TdJe5-OLvJ674il4Rh1jBb71lJMqT7gWU5v_iYmzcparE9NEw5-ntAM2Dc1za9gRksGcIee1dd9ndYRojohp6Uq4lptQdmgA7lXSsYhVwv4cC0m-oKVGUHcgp9CG3pg9Yy87SpfZJraimut3hFV5npvOc4CpuX9jHTDUE4yFkpeP8IK2-gd-1nIaXS64bSAvqaaIByhdY45X0pK_-CZkBPB5bv3ENSZmst0DsVu425NqPNqkVW4-AAjAOwHLdJcxWb2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیجای ترول خارجی این عکسو با کپشن ادای احترام طارمی به اسطوره ادن هازارد پخش کردن
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/Futball180TV/95018" target="_blank">📅 23:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95017">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klmafkLmH7qYVXOxvfI4n6ZTFsqC6M1KxEE-Twe7gi1ZVMjIOY15xFFK-Ja-1-3cEXWtJGVq6VQIlZI018JqbNZalCvurwbW3fY4qsRc9TReyo2ag0gNjVr8UowMTqvF04Z7hE4F5WVzWcx7JGKN7ETZz4VCCl4-m-wzyFudv-HxH2tO0T9U2ha3zbZLC5lC6f3PSPvwGU3REEC-9IwpHCjqRYULan6XKdBYrPF_mDSHlEoyPpkZvgg2JWnK48eO8YkdmCdx3pJWzFCZvcZ8daAFYZhaP9j9aRIqJWJDcBY18udj6AB0eD8aS9Ug85MMexzci34fjsvK5ICEGgA9GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیجای ترول خارجی این عکسو با کپشن ادای احترام طارمی به اسطوره ادن هازارد پخش کردن
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/95017" target="_blank">📅 23:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95016">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVcPQScXiGfLpT9STqNZ1akI9NZ_P0-2Mgao9EdZnbmVvAVVjTdSj4Cc6vAEeQijNc6WjP5HtGd_WzYW0zo_n_bo4yimW3aemGBHe2hvDHT0E-2PGBmUKu-f3VOQh0REHyX2jmpBlGO-F6EZ9HqsjnbpC5Q5x3kY0CWu-I42v_jZ5Cuyyg0KMO-VZy5yZ6WS1MC9YxSwg7WAnck5Kpb7IUQgjDHa8Yu8bSgknWlgArynyCKmSOwDdg5I6-3_sOxF172s6Sj6nFE5QCfaTvoY7hDElsvuukRAtKdNvG-hyQgmgWQYGdF3TphIMxjSeJnjdEcdAFyrb36tg2dYhXzchA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار نیمه اول؛ توپو میدادین ما هم بازی میکردیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/Futball180TV/95016" target="_blank">📅 23:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95015">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-e9LfmIo5UKp9gEsrN5Vw6kiPofOCYmjUI5xj7L8nz11tId4aw6Y2DEQG59rTbC7iX3M2pogKvuRphPYDu3LlmH4WusgbpILu53rwfJHFkvQTwDcIg-fJSIuOXDrFQ6cBxQdEvW64ATETI1X70sDSy7tvJBf3sx7ACKmNrCeDmMr2fqDq4kBAyExZZ_xeEvcVY7mlsNela1-UMMoWe0jPWBiUUrUK3JONndEVABcg8sOw9YZwVYUrQvoGEpFpsZ5svmMVWAlbhROVy2ptyx1JEelPUe2RJopYaTV2AiTHK4Qr1v6RELQYRcJIkj8_lYusuJ9kQ-KWn_tNgxvOfZGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهراب سپهری اگه نوک حمله بود همه چی عوض میشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/95015" target="_blank">📅 23:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95014">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🏆
پایان نیمه‌اول با تساوی بدون گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/95014" target="_blank">📅 23:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95013">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دفاع منتخب ایران خیلی کیریه</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/95013" target="_blank">📅 23:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95012">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">لوکاکو بولدوزره
😐
😐
😐</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/95012" target="_blank">📅 23:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95011">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">۸ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/95011" target="_blank">📅 23:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95010">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">شجاع خارکسده نیم ساعته خوابیده وسط زمین
😂
😂
😂</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/95010" target="_blank">📅 23:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95009">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بلژیککممک نزدددد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/95009" target="_blank">📅 23:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95008">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/95008" target="_blank">📅 23:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95007">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دیبروینههههه نزددددو</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/95007" target="_blank">📅 23:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95006">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/95006" target="_blank">📅 23:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95005">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4Y4XVIHah0xpi9h1T-iL0WTT_qY8ypPo-OPUGco3ZgE91ptQRgVAIcj0KF3gHGTHE-zh8sU1gdSQoI1kvaCkYOTQjbxZAPhelhFoL7PrWTzDw500Vs_WQ7EhqNvxxPssIkvklyywnRxMXYke2FNy1IKpkNamzXf3cnjlrtS8ECMddvbC449Cw_weXQ2TuMtgpk1XZZbxJRJfH4bbKHRSQoUSdCkzcatDQMiP_EvH0Pt0TMwRdT_jbCQIaUYPaQ8BAdImvw3Lmph1c4jDl4scI5lbkM3YPTGi0CAUIZWICC-Bqgm4as16yOgPRKdgY6v3w0dkVp1W6rFwpVjaSEBjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کون بزرگ طارمی خوشحالی ژنرالو خراب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/95005" target="_blank">📅 23:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95004">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">کاشته خوب برا بلژیک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/95004" target="_blank">📅 23:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95003">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">لوکاکو با شکم گندش همش ضربه سر زد رو سر شجاع و کنعانی</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/95003" target="_blank">📅 23:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95002">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
گل‌آفساید مهدی طارمی مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95002" target="_blank">📅 22:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95001">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/416694c9e3.mp4?token=cbiVph094HN1iCFbs6mP7KPhaXDI5K9XMibGlsaOKodO3B7SRh7__CWgQq1XbBZP1nhGJpwK2g3lleEphZ9gs1QvxQOm9XKw2D_VM3GvEoyukg6C1oFL5kUr3AxnNudQT5DnmroiXaP7gAssLyKLb0SnKdCrhLOAFf0HauYZXl6oqu83PVwodKNRORpXpVe6LGyE36FkYxuX8qq6QDO0vG4eCKIezIEB7RDA2FRejoZxLfSv0rK_fl_orGpF3dXnxoKrwT2jQQFsKldITMc83N4v_sj5R__fyrFZVutK2TXV--AlbhNpg5XNpDx-U-qwbDXz90-TkJREMicAWqM8VjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/416694c9e3.mp4?token=cbiVph094HN1iCFbs6mP7KPhaXDI5K9XMibGlsaOKodO3B7SRh7__CWgQq1XbBZP1nhGJpwK2g3lleEphZ9gs1QvxQOm9XKw2D_VM3GvEoyukg6C1oFL5kUr3AxnNudQT5DnmroiXaP7gAssLyKLb0SnKdCrhLOAFf0HauYZXl6oqu83PVwodKNRORpXpVe6LGyE36FkYxuX8qq6QDO0vG4eCKIezIEB7RDA2FRejoZxLfSv0rK_fl_orGpF3dXnxoKrwT2jQQFsKldITMc83N4v_sj5R__fyrFZVutK2TXV--AlbhNpg5XNpDx-U-qwbDXz90-TkJREMicAWqM8VjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
گل‌آفساید مهدی طارمی مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95001" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-95000">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
آفسایدددددد شددددددد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/95000" target="_blank">📅 22:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94999">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">قلعه‌نویی خوشحالی نکرددددد
😂
😂
🤣
🤣</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94999" target="_blank">📅 22:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94998">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پشماممممم</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94998" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94997">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آفساید بوددددد؟؟؟</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94997" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94996">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">طارمی زددد
😂
😐</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94996" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94995">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گلگلگلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94995" target="_blank">📅 22:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94994">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کاشته برای منتخب ایران</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94994" target="_blank">📅 22:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94993">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کاشته برای منتخب ایران</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94993" target="_blank">📅 22:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94992">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بلژیک خیمه زده</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94992" target="_blank">📅 22:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94991">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بیرانوند بازم گرفتنتت</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94991" target="_blank">📅 22:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94990">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94990" target="_blank">📅 22:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94989">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">عزت‌اللهی هم داشت میزددد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94989" target="_blank">📅 22:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94988">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94988" target="_blank">📅 22:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94987">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کنعانی داشت میزدددد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94987" target="_blank">📅 22:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94986">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94986" target="_blank">📅 22:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94985">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">چه کونی آورددددد منتخب ایران</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94985" target="_blank">📅 22:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94984">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94984" target="_blank">📅 22:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94983">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ضربه دیبروینه به فضا رفت</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94983" target="_blank">📅 22:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94982">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">علی نعمیتوووو</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94982" target="_blank">📅 22:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94981">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بیرو برگشت</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94981" target="_blank">📅 22:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94980">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اوخ حسینی داره گرم میکنه</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94980" target="_blank">📅 22:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94979">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">لوکاکو با زانو رفت تو صورت بیرانوند و کارت زرد گرفت
😐
😂</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94979" target="_blank">📅 22:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94978">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بلژیککککک داشت میزدددد</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/94978" target="_blank">📅 22:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94977">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/94977" target="_blank">📅 22:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94976">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">برررررریم سراغ بازی منتخب ایران و بلژیک</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/94976" target="_blank">📅 22:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94975">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/688c1aac3f.mp4?token=IKq5P8UkQIQDxkS-XPgv5oeHx1QXL_epSqUbrOfDs4L-aJh6o2zmwDkeoW4F4kQFutu8BIc3DoeklEQAO9_mZlqhaYJ9wEAote1_PUnsL-lZJsiVZ_tElf1OOUqe4V7ljojiad7rcxck66xo0b8NGxQq25j8IcJBCdQPM-0o5ArSmhjJ3nvOgfQZb8sfs_Ab42lboscSGTEwTEEPSozr162zXfjvhj3s2sEcA1czRXCpcZxE5TWKykkZklyVtGR2fa8FwSIe6wibhePMBvlsjqZc0wexfafv1R1dtH-kwNprV64nfKgdwxfI-7CAVshnGZpPaMJ4tslVciL9gKrA6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/688c1aac3f.mp4?token=IKq5P8UkQIQDxkS-XPgv5oeHx1QXL_epSqUbrOfDs4L-aJh6o2zmwDkeoW4F4kQFutu8BIc3DoeklEQAO9_mZlqhaYJ9wEAote1_PUnsL-lZJsiVZ_tElf1OOUqe4V7ljojiad7rcxck66xo0b8NGxQq25j8IcJBCdQPM-0o5ArSmhjJ3nvOgfQZb8sfs_Ab42lboscSGTEwTEEPSozr162zXfjvhj3s2sEcA1czRXCpcZxE5TWKykkZklyVtGR2fa8FwSIe6wibhePMBvlsjqZc0wexfafv1R1dtH-kwNprV64nfKgdwxfI-7CAVshnGZpPaMJ4tslVciL9gKrA6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ایرانیان حاضر در بازی امشب با بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94975" target="_blank">📅 22:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94974">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAZGRgvEkz70XFUAq8K4iWJlyA1YOZJv5NLMzSsAIWO3wr_4w7E1ah35DjPg9RXo5nb31dVuwuv8U9K9e5lk-jTaEzpgbeD4jkAFq4nvgJhkbEEG824op9CqtEYnH2r_88smuR0bhIPtCLhbfZmAl-pT6xtYoJvjF8KGeabm2wW8ModRH6CLgAOkKkfWkoOOOxdavt8VTmnoe7tA5Iv_dsaFfjtnQ0FE1qty9DCsO3N-nz20J7sBH47BIuv_jlpHMNqU2Z2Y3pzTzEMbVqRodQlhEaJPldL1dJmVvAnO5cs1SHty5jCiap7YTt-UzlXtyXJ9xbBrrWlYpNqjSO0XFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آرایشگر لاشی مسی ول‌کن نیست و اومده اردوی آرژانتین تا برینه به رخش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/94974" target="_blank">📅 22:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94973">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjgjSHKip6f4uGH2YqZk1hkvnC9nMMXoDPIgGlMdbbMfzRW56tyh6D5Dg1Np_eEhHxpRbjsTVe0k8FrHmaHaBqopl404l7mbskRfjGKZ-TijBPDckVQwazCQfHnppbtAv7rr5JoxvHEvTUFf5yNYnijm9RdBBrp1C3J8kXsQIJfDDaZmiOcS4H0XoqOZsuvRa7BTLPRBx6loGUHRw4_pp3hD9bv0ziIv3-WA9bpEOv0KormjIEfOqsaA-cklkv3f1Fsf54eqtbSPY-F5r3M4zU78F_HTG48adhLQICh1QHsDXsxZdIBYw32u1YzkfJoYKAn8X3SuciCw34hVJWXswQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
از رویارویی با اوپامکانو میترسی؟
🔵
ایمن حسین:
نه، برعکس خوشحالم که با بهترین مدافعان جهان روبرو میشوم و انشاالله میتوانم به آنها گل بزنم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/94973" target="_blank">📅 22:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94972">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d88277b344.mp4?token=ShnMxquuCqvXVQ9nqnicWK6hRY-qBwX28uT0erajhHflDSsFa72Xs9le19vJlut8pGWwT2-nVf9I8ZBiJNVOvPP7zpAzzgXCIPF-3J9JBqDVh56SSyHJHWcoD4FuNGdbH4uuS5cSZjS93wGToMk2H5CFOEXRjlhShVnMQD1uPbcbdtxsCXxrTl8cCcYdH3Xmbb-9MpWBX1PFrl0dnQzRjXbYcYY6WB6H2sitwhda1PhgRmTqV3LFOv1JOjbQrRgeRJetzzBrjgdbmAQFF-gX7iMDWq_0Ty3Gu-3JxyBu5SvJJDX0WTkZM48FVbG6tUf-YczlCLxvjF4Gb9JJnezoniz78fkfznmg2Rq8We9CKcc3xBbat237tPHMC5kbBCIg1Bvw_mXGbvCF0GcGYuFitxwemgg1AZVoWToxTsuCxD5CIfrp5-pPqjrfzEY9tZx3N0fXTUf5QX_I_8jME9pNdi8JPT_9rFrBA6k50ofgjoYECJ-A7Uf6PtGsxOuv8I7jQUhxiOKWKnT1DeA_OqgeaQ-dlAjR7f5I-Gk8WJkZA2fScZXR4mBfBFiO51RoE04CVqQ64wb6J8H8O-Va88jmKUP-c41ja9ObxSHBStR1ffLZYlW6MkxhqrLbuXaBn8iDwOCsxWeItDrRna3m6zl8Bv5InyzxbVoJs6hr4ktCrh8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d88277b344.mp4?token=ShnMxquuCqvXVQ9nqnicWK6hRY-qBwX28uT0erajhHflDSsFa72Xs9le19vJlut8pGWwT2-nVf9I8ZBiJNVOvPP7zpAzzgXCIPF-3J9JBqDVh56SSyHJHWcoD4FuNGdbH4uuS5cSZjS93wGToMk2H5CFOEXRjlhShVnMQD1uPbcbdtxsCXxrTl8cCcYdH3Xmbb-9MpWBX1PFrl0dnQzRjXbYcYY6WB6H2sitwhda1PhgRmTqV3LFOv1JOjbQrRgeRJetzzBrjgdbmAQFF-gX7iMDWq_0Ty3Gu-3JxyBu5SvJJDX0WTkZM48FVbG6tUf-YczlCLxvjF4Gb9JJnezoniz78fkfznmg2Rq8We9CKcc3xBbat237tPHMC5kbBCIg1Bvw_mXGbvCF0GcGYuFitxwemgg1AZVoWToxTsuCxD5CIfrp5-pPqjrfzEY9tZx3N0fXTUf5QX_I_8jME9pNdi8JPT_9rFrBA6k50ofgjoYECJ-A7Uf6PtGsxOuv8I7jQUhxiOKWKnT1DeA_OqgeaQ-dlAjR7f5I-Gk8WJkZA2fScZXR4mBfBFiO51RoE04CVqQ64wb6J8H8O-Va88jmKUP-c41ja9ObxSHBStR1ffLZYlW6MkxhqrLbuXaBn8iDwOCsxWeItDrRna3m6zl8Bv5InyzxbVoJs6hr4ktCrh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
اوه اوه چه دعوایی بیرون استادیوم
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94972" target="_blank">📅 22:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94971">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dbd8c3b71.mp4?token=cH6rLv7A0Sb0AyqvIJBzx2kKi95CM0g96WKAG8XWVdBa4ToSoA0wsYYUIBQrDduJ4_wQfoQcJm5-yAVra3h9oBfIGa_gBhZ23EuszpYHdYHVts3k0QycQqzE3smcVJoafd3kfYbhZqcxOuWq5lrLFo18Ga9WXvuqNX-dwbHQqNIkOxYMRRPGLRdLsdIqRIdvyLlgYBtIMmTpVD0NM3ODIreZQiXJgbp4_V5pBVp8MLhr4rPKFWg2OkT6b0YS-uT13QlQ6YDam0eEdWEDp1oLczCD_E9715fDkpMfYOjW_DjpRh-51SdndhsESeEj0c824T1Ly84KGCu1MEETGVCAmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dbd8c3b71.mp4?token=cH6rLv7A0Sb0AyqvIJBzx2kKi95CM0g96WKAG8XWVdBa4ToSoA0wsYYUIBQrDduJ4_wQfoQcJm5-yAVra3h9oBfIGa_gBhZ23EuszpYHdYHVts3k0QycQqzE3smcVJoafd3kfYbhZqcxOuWq5lrLFo18Ga9WXvuqNX-dwbHQqNIkOxYMRRPGLRdLsdIqRIdvyLlgYBtIMmTpVD0NM3ODIreZQiXJgbp4_V5pBVp8MLhr4rPKFWg2OkT6b0YS-uT13QlQ6YDam0eEdWEDp1oLczCD_E9715fDkpMfYOjW_DjpRh-51SdndhsESeEj0c824T1Ly84KGCu1MEETGVCAmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤯
پشماممممم یه پیجی ۲۴ ساعت پیش اومده مسابقات امروز رو پیش‌بینی کرده که بازی عربستان و اسپانیا درست از آب در اومده. حالا بازی منتخب ایران و بلژیک هم گفته سه به یک میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94971" target="_blank">📅 22:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94970">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3607c70f6f.mp4?token=TqKvrgtCxIyytGln-ymYuyoOSm3fvl7DVjtSMFUZskpe6hjnjWWrpQo4utXdG3aa_K3-m8xOCxdMP1N1McfPGeuaecvfbdfk8-JmXp6SeVnQXaBTKlYZqX67uJFhA0gWldm5nJiP3ruCjmC4VuWVgnMKofXyzXxV0XA2eHSzxPzusVnbXMfEAFmALLBlCNUvuNCk-3k6c4wjsK13T8tnaNOdVKqK4eHigFYDWlOvEKsaMTA9YOdMoKPgWkb2VkBTQ4JZIxoyeUx07tQXnip6WvnpD49VPdMNgsCAptaOu7h0YXeP28BEvphDUdkat0D4wgHvSWaREokAcslf5Oua9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3607c70f6f.mp4?token=TqKvrgtCxIyytGln-ymYuyoOSm3fvl7DVjtSMFUZskpe6hjnjWWrpQo4utXdG3aa_K3-m8xOCxdMP1N1McfPGeuaecvfbdfk8-JmXp6SeVnQXaBTKlYZqX67uJFhA0gWldm5nJiP3ruCjmC4VuWVgnMKofXyzXxV0XA2eHSzxPzusVnbXMfEAFmALLBlCNUvuNCk-3k6c4wjsK13T8tnaNOdVKqK4eHigFYDWlOvEKsaMTA9YOdMoKPgWkb2VkBTQ4JZIxoyeUx07tQXnip6WvnpD49VPdMNgsCAptaOu7h0YXeP28BEvphDUdkat0D4wgHvSWaREokAcslf5Oua9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
💥
👀
از اونجایی که کوکسال‌بابا آخرین بار چند ساعت پیش طرفدار عربستان شد و مورد تجاوز قرار گرفت بنظر قراره بلژیک هم به قلعه‌نویی تجاوز سختتتت بکنه
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94970" target="_blank">📅 22:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94969">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21d1ba7e62.mp4?token=SZrk99UsIBj5duuhy4A5A74fj5OToqp1gdzDOhEwIwc3VCDKgckN6epu2sc4Pa_piMsMQO8cP2bjOPS_C20lYXbcNfj2XWwww7N6x92UJUYmfQ4avXMDJjb7Duqj9KP6m4_9I-3Y3OPIfLni6YkhDdTy0iouClTFNbX0wfWlyq1W8_JM3vA-caOBYNwwSO7soIb8JkL0MbzE_RnmILzFIE9OnjAEX6FSpPZrHiPiE2eHHThmfRkaT1keq-Budv1H9rkLVzCB6GVjboxrX8mBbKFtnooD29lYe090uKFXewqp5SANpP-olL3S55hNfzi1vijswP-2I2PHwM06Ue4mOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21d1ba7e62.mp4?token=SZrk99UsIBj5duuhy4A5A74fj5OToqp1gdzDOhEwIwc3VCDKgckN6epu2sc4Pa_piMsMQO8cP2bjOPS_C20lYXbcNfj2XWwww7N6x92UJUYmfQ4avXMDJjb7Duqj9KP6m4_9I-3Y3OPIfLni6YkhDdTy0iouClTFNbX0wfWlyq1W8_JM3vA-caOBYNwwSO7soIb8JkL0MbzE_RnmILzFIE9OnjAEX6FSpPZrHiPiE2eHHThmfRkaT1keq-Budv1H9rkLVzCB6GVjboxrX8mBbKFtnooD29lYe090uKFXewqp5SANpP-olL3S55hNfzi1vijswP-2I2PHwM06Ue4mOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💥
هوادار استقلالی در استادیوم لس‌آنجلس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94969" target="_blank">📅 22:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94968">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3GmnohyvnEoHzoxgm3AHqNECVyqj9h0itjuC9MvJLp_7kFgXaQHXjzTXFWpq7ChhyKKZmR9b5z0ELyJveQVt7DaFtd-xIogli0RN_U0qmv19SQI-bHRppmq5WqjXMfXOve3o8g3rCt-W9mkmbmtLbqETZIlvZnENrHR3d54La7JW7BnwRVj4BWwcERflTZQVezHRe9luCtH_XTfHufscoMV1n3Y7dMNcQ-F80VwOjtSIbk9BZyY3AoZ1cGemvSXmABzysx8XqrdNp-0X6ftfnA3fFe7v-If8MEUjOCB7q98Zt9__J_ivMIjMNXhzqZjLPdVWIQXRc2DpaZ-yi2SRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💥
هوادار استقلالی در استادیوم لس‌آنجلس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/94968" target="_blank">📅 22:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94966">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i_w0VxMPYLTLDHSX4DQ5nxZI_jH5LxzGeN32GDJh5BqFNm1Du1Un-dx1JM0sCraCG0JbsyhiPFBWMzmHc6i3HgCUEuHdETuUwNea2qSn7kYZuE7MPdDwtqN82qnkyMPapUMzFV3gVPbUZ7C6vGJ5TUhi64M2lAtA2EAITk6jNIjlLt6vPogX_Ea12yQ3X9Vodwm01DD6DaEQ0OIf8XIVU36aIhbUSvISeG-Kr6HCxN1gLeSE71ItRJcOq8mZjHT25_bPy-99PvIQ2QkKIa08_ykQGBhz8jYq6vilv4xklP_4qYRpN6zI4ejR7qaoYe_y7aozgWlh8hWWF5mdWnkpWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VuAx7g6Z72N6cb6E0LKlYnz1SlCrZRUMNhIAX74kI4kv2XsOEWDw5WCcannYUs_aSbhm_axJC_8ZbeM77kdp7Zohw3gCnAeAxtmVFzowOuGFOizfnJv_EdcrYghWUOvpaTqP6jhO3Oqaw0YZifOT-G0KMQFKLeQff_zrof_W8m3aodrYwu8qltDxXWACrKog2xudTb2FyDefDZoSSNxxIB9UFJ9CYdKjrKmgH5X4IR9yYYJ_JKETtki75TObAtLFtqoLdLkIAhVQFPm2pGMyuW6LW-UTbvWHaSuoi6fMgBeOX_CKIP4ePPFJhTWxUX2wcP1065NxDdYU9AjzLeApQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایشالا که خیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/94966" target="_blank">📅 22:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94965">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/976dcd02e4.mp4?token=c4-Zmwei63rGIPOBmTFDQBzH7RAvcWwrO-zQH6nYmlncureHaNKT756eGgCFbxJJSGc38fR5z3VsBE8X_GP96La5ukzkrNYniFyuG9DVhErx9Qx29Ubt-NWIOowAAb1o76zOHKoeoaRdpsuYdR_NHo0t9Cs1pSBwruwLNAOwjPw4qM6QyvsJbgHk5xPn23C0v7hSLGZD3HI2yPEIVDjdS0eys4xDXwLfV7VfAttQBGuOZs_wLtscJgNcucLFZ9RfLCbHCTlGThaVi4MkZDaFOOdin3G5e8qNIIVgKjckKCoZiR2AQkJk7c1q7m9BCt2LoiTzZj5UHFNNcyP8WgyxoGNyeAOiYiZeH7-01p1kcAigrfm39JPkMcfAHHPFF4SQYZKKfeNPHN-c03NexPjlvmWp7TnDAcbWbZQeUviMzhBrjAWHR-ToSsKO2AytDJVLG2Aw56wIGOppKw1vG-Cb9odVHqMpEI55rTQeEDX9gPs-aIGFpWAmR1mwLpgYBx97p8GjQRnlHfDVWRLZL28y_rahRaVkI99gK3q5ug7X_kbtm9lNhAUSHgW3z4Hz-HxZMzNbmELGK-EiDvjO4HDuzkE7SLkr3vRWt_mXck2XtS_LAUfWde8wgwRCH7B1QtPDKo3CflRCfhRPP48w7cEykuzo-Vx7gJYQ_l_98kiUC0s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/976dcd02e4.mp4?token=c4-Zmwei63rGIPOBmTFDQBzH7RAvcWwrO-zQH6nYmlncureHaNKT756eGgCFbxJJSGc38fR5z3VsBE8X_GP96La5ukzkrNYniFyuG9DVhErx9Qx29Ubt-NWIOowAAb1o76zOHKoeoaRdpsuYdR_NHo0t9Cs1pSBwruwLNAOwjPw4qM6QyvsJbgHk5xPn23C0v7hSLGZD3HI2yPEIVDjdS0eys4xDXwLfV7VfAttQBGuOZs_wLtscJgNcucLFZ9RfLCbHCTlGThaVi4MkZDaFOOdin3G5e8qNIIVgKjckKCoZiR2AQkJk7c1q7m9BCt2LoiTzZj5UHFNNcyP8WgyxoGNyeAOiYiZeH7-01p1kcAigrfm39JPkMcfAHHPFF4SQYZKKfeNPHN-c03NexPjlvmWp7TnDAcbWbZQeUviMzhBrjAWHR-ToSsKO2AytDJVLG2Aw56wIGOppKw1vG-Cb9odVHqMpEI55rTQeEDX9gPs-aIGFpWAmR1mwLpgYBx97p8GjQRnlHfDVWRLZL28y_rahRaVkI99gK3q5ug7X_kbtm9lNhAUSHgW3z4Hz-HxZMzNbmELGK-EiDvjO4HDuzkE7SLkr3vRWt_mXck2XtS_LAUfWde8wgwRCH7B1QtPDKo3CflRCfhRPP48w7cEykuzo-Vx7gJYQ_l_98kiUC0s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
#فووووووری
؛ طبق گفته یه هوادار تو ورودی ورزشگاه لس‌آنجلس از سوی مسئولان فیفا پرچم‌های شیر و خورشید ضبط میشه و اجازه ورود نمیدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94965" target="_blank">📅 22:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94964">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bf0900e27.mp4?token=oKQvbFD_npux4nQBXnanKBxlaK-QjlzxJoasTGFR7KkOSz6eD38KW_qdmU2UBC7KvrSwbKJ3XmvhzGtmtvTfJ2gLtxlm9Ip09xDpYLNtmxqanPRku57lgi1qCjxFKMsTR288Yii01nUelQJNDJHXGnq_7lCQYFvP5vw8F0ff0goEn6zmExlwsYly0Nw9lwJeUu3DaEcbHcKp7Ib7-_PC9qeIG8vJ8uOn30U0Cx-Zjqtt2gH25Oc4HuHfI5qZELjkjQ6GrjpEaGfr7ZijXSj71iLn6Yy4Q_cMgozPtnUeDkWVP0cDBTZ9DJdcu1RdVR8YLEQUhZeH__PtI4Q7uE8XKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bf0900e27.mp4?token=oKQvbFD_npux4nQBXnanKBxlaK-QjlzxJoasTGFR7KkOSz6eD38KW_qdmU2UBC7KvrSwbKJ3XmvhzGtmtvTfJ2gLtxlm9Ip09xDpYLNtmxqanPRku57lgi1qCjxFKMsTR288Yii01nUelQJNDJHXGnq_7lCQYFvP5vw8F0ff0goEn6zmExlwsYly0Nw9lwJeUu3DaEcbHcKp7Ib7-_PC9qeIG8vJ8uOn30U0Cx-Zjqtt2gH25Oc4HuHfI5qZELjkjQ6GrjpEaGfr7ZijXSj71iLn6Yy4Q_cMgozPtnUeDkWVP0cDBTZ9DJdcu1RdVR8YLEQUhZeH__PtI4Q7uE8XKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
محتوای خواب دیشب آقای‌رضاییان:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/94964" target="_blank">📅 22:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94963">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGClqaqsH3AqPTtH9t_lhhB1JJbEQn_WW-LG3ScePMJ6_xuGx4YfCM6xsRlvyNN9BDDRkUZdp2VHbuO5oRazcIzazgrl771Jak6K3F_ZQ2d_eKzQ8-H4YWrBGp8LYBNqIaativ80eUHY39rw74r7xsOcw_pxmC4xUUHZCpsps32NtsdfW896c26QSX_YDq1Ck6bETrfrzFYI4xxXZHlUomj_b-JP3fPZDZu7mn3ByAF4h34fFXQZso5hZs8_RgwOOb3n6IPIikK4ifeznr7Qb_bvyudYbCP-qnF57l9lTEylJlF0Cy7WUDcoG-cdn7YIFhYOUWm3jSEztrVK4W3QEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
✔️
این هوادار معروف بلژیک رو یادتونه که وسط بازی رفت تو زمین؛ واسه برد امشب بلژیک یه قول‌هایی داده که
🔹
💕
🔝
🔗
عکس دفعه قبل که رفت تو زمین و سوژه شد رو داخل لینک پایین گذاشتم
👀
💥
🖥
🔞
https://t.me/Worldcup_uploaderbot?start=7UdC7Kyn
💦
⚠️</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/94963" target="_blank">📅 22:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94962">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFJ_LgGiVuQHplLVyqIxTs-NfeqP8nvTfOFod4yQXaEvtBINTk8le1mW0Z1lys1bh8jaxBFoUQblPAisSnHiWmExvDzRmjzMER3PY0NU-Mrod0wxRyX4PS0u9ZomEt57_hJGB0SxHM75LZpJ5b7sf72ajOIzJgUVjLSNfmiNNdRJH1fGmYL2uUfyo11TAXrUx8kTPKLAvL7JQ3tlK1ZfGDX7dozlSXQwCNJumld8T82FgRLz3kg3zIeZVNssFA6_PUiDNXjvMU4Tuyw_TKXw_74NcZYOv3JoIsr4-rybTSgby9JQA9QwqmTXnrmlNLQh0j-wBoytbNFyrcdJRPDnIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصاحبه جدید اویارزابال:
🔻
شما خبرنگار‌ها گفتید که من در بازی اول به مدت ۳۰ دقیقه نتونستم توپ رو لمس کنم، اما این بار در ۲۴ دقیقه دو گل زدم و یک پاس گل دادم. فکر می‌کنم نه پله، نه مارادونا و نه هیچ بازیکن دیگری قبلاً چنین کاری نکرده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/94962" target="_blank">📅 21:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94961">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBe9rw3JYqY0EMKPFcwujl_bzsZJf1C49RVYxSw3hKZGQYUf2txrbMh2lvjgjoiNR4P_6k2dxQ5K4hlX55L3duUIdPOeFoHUUsZywnWqY7PqWKMeWbMGmecmdzW6XdCa1boB3xAghDFr_HkpBkV0KwWuYRT5f2AqUEnr29UfJHXbvjjQG-bucO4BJHVPpqU0E8Ct6UiL_wduAClc1sdv0MR9OVbeK1h1j4qCFprdGLyFgiWe5kJNoWMIbXR8oyiycZBBkzLj5zrJ5oAI1jpgERASpFw4Bc2q0qCVww_3NcFyDjpOF8dLz4ih2NQF9wXDoK12N_9ZTrdQf2FY0TAMfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
تصویری دیگر از ایرانیان‌در استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94961" target="_blank">📅 21:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94960">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBIpuNtGEBW7BeknQYNq7eqGPQeyCZcX0cXimhATdtf_D-nSLsDyh8Rq_p_Xa4s-qpBxKm8CxrQgVTo4UlGrBGc0hgXkJWLke_wdMMPhmGYfzmIf6MAX21evalfkIXfOrid2_9PQgMCXwRPPJfRNnuYcioEZ95byXk1AXcY9bZ1B6xW2jzJkKAQvlnv9LmQcDrer2hudH4u_P6eQYa7I4Iztw5itQNVDpPVNGU9om7LYfqKisxmfYWevCzEKgHkTFSBbde14gdmaGV7K7tdEm-XMFzCz6BgFFMSCMmAJTrhqkp8I0Kc-gY7EVcB59bw0LX0remhZ56dL_PxPcK-uNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤣
آمار پشم‌ریزون تیم‌های عربی در جام‌جهانی: ۷ گل برای کشورشون زدن و ۵ تا گل‌بخودی به رقبا دادن!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94960" target="_blank">📅 21:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94959">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gI8vrdBDoKiXPMsp-0iz-8IFM2gBlV2mJx_Rvm7h7IAYoMCcTjeiqisx_8BQkkPA445QOTeZnESeFOo_HyjsY5Q-AGLf01tJHboEvKv_7OO1MNk0cIlis1kbFnumIJ-mS7X28f4a-CK6gPgfsQyF54mgzGfPsFNNN2CZ7jrfrPAPpX1MAGgSFmkD3Mo-2folijw4gtWhWd93KCu11fi4-rgwAL5va4-It0i5d9NqDa6ZKUMgV5ZPtRPhgfJCLEQ61WzdKvtnYr4sOba38ygSJliyIvQ2hRV7nGevjY9hQ9LlnyHfzLR7iyirkEiUueLlTlcaM5r8TV638jfkpWBZBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤣
آمار پشم‌ریزون تیم‌های عربی در جام‌جهانی: ۷ گل برای کشورشون زدن و ۵ تا گل‌بخودی به رقبا دادن!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94959" target="_blank">📅 21:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94958">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdjHTnZbv1q2onjHFKdsMFHlTXPmpZicAMoVt1XAGI6HS9_VoaERX9MtWUHmWsav12fQwzmTvi_RkQG9diDt1yqCFCm8McG275T_EbrcAnVbK0oDMm77Ow4yQLo0EFpxp4zIRXpTop7VH3CMJ_0bNoY_Kj9B6eBAnDwl2zrmyHolI08j9jq89A2upSK3k5MjHoq29x194xxdp0sNQP92nmobYHJpefGlW6qVdZkBak_cWCL-jlIcMeMuYOqLq3z8zqNS6RVBqM9sGFvSuo-lhg9da6lltwGJwnQGhpUKWsecF-1GBQ9SUPTqlMafhkqRva2WiVZtWM_-oJLDDrvzdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
تصویری جالب از هوادار ایرانی در استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94958" target="_blank">📅 21:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94957">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFuqEmQrKPrVRfVs5p4cedN39T3pmskv4FNesBSmfe-iUmop_-_17RZeDUWLYxTgm8VgF3amCZmN-MbvWkGwqtD8Tk6xKDgHEBjA1rKfqANa4F0gYZw8LR9eBlOEK74zFaqLHHPebnhSJ1UQpOAzc9z04tlNQ0_RY0rgOdwHvP-CVesqJgaHBUNPBdBHRuhUP0fpU4Tl1LjTZaUZd8c04chF6pLDPLIVz20scldZISRR8sxV1YJQhnRmkIMMAavwxKK2ulY0OwENo7JWghSnx9A8gOAmFBbGQ7El6UJS70IrWOJQvLaNtA7z8IgLBYcsW_ViaSZrGNsl8grTQ3K2dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇪🇸
🇪🇸
#فکت
؛ اسپانیا در تمام هفت بازی خود در مسابقات بزرگ زمانی که لامین یامال به عنوان بازیکن اصلی حضور داشت، پیروز شده است [جام ملت‌های اروپا + جام جهانی]
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94957" target="_blank">📅 21:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94956">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXNTBB0DwlMy-seKSp9Ct5mzM9frwmvidPZOLAsPZmZvY7v67WMm43XPXq305ooApDIcs5MhefcVgNVPg3vhJhKKVIgbzO7_NnZ0hizDSRADXEeEYF4Ki4gVmUu1UbNaQ9gDE0wIluLNeDvwDYBvOfY60qJmSJjXs165kmMQm32szAXxVMNA93bGI_ufzRnmsqZ5CNuv0L6yi9cv0uCNL1pnM4e_FctPka8nv3fp1KvOkNwBfmVRQDdMQ1I3eGTj2E7zVeHtJnbwvxdQSXsSAsl0zAAMtSC6sLWI-Xt_CzG5J68yTUT6S-Pi1pITwpF5mq2-bG3iHikPgrvWD1XjEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرگل‌ترین نتایج اسپانیا در تاریخ جام جهانی:
‏
🇪🇸
اسپانیا ۵ — ۱ دانمارک
🇩🇰
(نسخه ۱۹۸۶)
‏
🇪🇸
اسپانیا ۶ — ۱ بلغارستان
🇧🇬
(نسخه ۱۹۹۸)
‏
🇪🇸
اسپانیا ۴ — ۰ اوکراین
🇺🇦
(نسخه ۲۰۰۶)
‏
🇪🇸
اسپانیا ۷ — ۰ کاستاریکا
🇨🇷
(نسخه ۲۰۲۲)
‏
🇪🇸
اسپانیا ۴ — ۰ عربستان سعودی
🇸🇦
(نسخه ۲۰۲۶)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94956" target="_blank">📅 21:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94955">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8XWeuDzbyqNJ1kDyi-CaLt9601-3pHGbrMdquV0V_Kki5Xs2MpgJHBQpS5hElnL-FPwpVe-XjDTgZz6VVfN0SLRE8Vrd-1TlKG6F1J6P_sxhwPyXOLJnHSFxSTPdjuDEtWm7EURJ20AWz3kiYguo1FCS_Clp6Kg1wm4cCwfXhDkpJLnY7uSPEldbe80Is6K8LTI4Oe55W3iJRpl0eTW1Lbt3Rzv1ROLsJvXNp03c-ua6eUC1Ec4Ne2VVIIo_zgTb_0NJg9tvro0LP-ugkex-hSFi5m8So_6WmlgfByh1mY6G2XyRmimgjqsd7nRCZnxxjN81Htynw2FPaiwDckemQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سرمربی سرخ ها مشخص شد
- پرسپولیس آسیایی با چاشنی بمب
🔥
✔️
خرید اول سرخ ها فردا در دفتر باشگاه
🔥
پوستر باشگاه برای سرمربی جدید</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94955" target="_blank">📅 21:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94954">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNmo3gGuvY26ybpRMuSQQwbikFHZWxQrvC0st7o8ftw_ZdN4oI1s_XuvsS_j0xcL4cUhxLK1KkGwhBykyOCo-w66B-0qeoYx6pMvYzUHvAkBxxR7NFvMev_BwHSV0z2FKGvZJpQsrQ0ln0Cmw_EEHmhUtmyyapBD_dV3A43ZZsfC0yGswF-I94DfeQm8sSf5qHa12DkKELpG4Il9wuSnWAiiC8YPmntokUMK_FKBd16xsqOKSz6THq_AknrAydk_aXuE2kdY5f6R6YPe0TZZvAQLmx7MUgoxkNelPZpASb7nW7mAOIelWSzUTG8hyaYzPpI0RZnMS8mp9TjY-UxOMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت هوادار بلژیک بیرون استادیوم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94954" target="_blank">📅 21:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94953">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdf3e66b09.mp4?token=M3GnmawaKNaDQMApAfVM3Z1LFuTWOQpZIwa0h96llTbCj0MnWheZlpv_v8u6gfbW_5-CtACH4s5G8mmF7aT0NqmuepVPxPUq6RX9ySMgNDxV5appc-VZXt3tfyAC1NAIY6s6zNmoMecjNkfuoGwrEPM41ii1Ky5151i72RukVlW_88-Tz13GnsKXgvWhXlLqPE1vOMild3--DRS4nvtxEf0NoVv87D1dfx99k4J0nLVvDqxgXe-T1OOJCviVV-EDesz4Me69t81SAdxJBq0OAiIIQYDT2XLC3xj7uDTUMuOxiGQjqrKXXwFqoaV35CR-TLrri_OiIrlhgTenMBs--Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdf3e66b09.mp4?token=M3GnmawaKNaDQMApAfVM3Z1LFuTWOQpZIwa0h96llTbCj0MnWheZlpv_v8u6gfbW_5-CtACH4s5G8mmF7aT0NqmuepVPxPUq6RX9ySMgNDxV5appc-VZXt3tfyAC1NAIY6s6zNmoMecjNkfuoGwrEPM41ii1Ky5151i72RukVlW_88-Tz13GnsKXgvWhXlLqPE1vOMild3--DRS4nvtxEf0NoVv87D1dfx99k4J0nLVvDqxgXe-T1OOJCviVV-EDesz4Me69t81SAdxJBq0OAiIIQYDT2XLC3xj7uDTUMuOxiGQjqrKXXwFqoaV35CR-TLrri_OiIrlhgTenMBs--Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
#فوووووری
؛ تجمع ایرانیان ساکن آمریکا در محل برگزاری بازی منتخب ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94953" target="_blank">📅 21:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94951">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUzQql_YbVUwWV_2LseeNvnmXG8vIywa1EAb07WH9POQMadXQJNJj86pbocxQDSQomh2fCB5uAC23tYi-ZoQ0r5nfWWT5tS23f0xF4MhwBC76YLYUqxMLukji34t4iA12Bx7saDW4EaR8UBuNAAN6TkcHW0Y3_iLZQTUoHeK18J1M8J-pIQ-E9aX0PtUcrpnVRh07uCttPYfPAEv9LTwIgJJvmP8Rrsl5RUinZnBrdSDKNpBxk39MCOFS5MEfSITAXZtzjh13_RuM2DGv_hWapMcMJMWkZg1nigA0sRhQnOfIYNzTXjCXSgadaqdjztdN7Xt07DaRukjkXoMuNVQFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
👀
⁉️
بوی‌قهرمانی و این‌حرفا؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94951" target="_blank">📅 21:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94950">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-wLwp6NrErQ40RKK_H5svTwJcWC1jEf8mweb3_GETjtiuxVJrg2oz7Wj58t5_liiKB6KAjb3ryAIhXxtp-NprFI5k66App1piSmu-_MSOnEZAlHRAahdS7MjZ913wHZRvtsi0gp-IUxgLp5bIY9CP_L5Lsn6MM35FAcA172zu4KyMFxjCHc1KICirxjm5TXomfw3CwjOQepaze2lgGgpa1xUZ1Fma8Cl8T4f1JZjOvN8GCLwh9CSaOcjeD2CSwommwz5WdCEgMEo_PbzLPZIwrIXocTP4GbGQa2r61-QL04_9ncoLLtPWyCT06cljxrrbEafvhhqj2MPBlc9EQ2oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
در جام‌جهانی فعلی ۸ گل‌بخودی ثبت شده که تنها ۴ گل دیگر با رکورد تاریخ این مسابقات که در سال ۲۰۱۸ ثبت شده، فاصله دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/94950" target="_blank">📅 21:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94949">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZozdqDtBJLTo9PYdDeVLGExjiOtcaiYjtqMDW9mTp-_UnYy3RGsIu9E9DxxzXnMooo2qOAYqpNLDUf5Ng-ki1h8FZ25J8eOQMcG8Jm6tEb0GQANKk6TVrOKP-iRbi9LYUZDEGCF_LE_DXoD-w19ma51E0asBqcU440DwNWI5tfe2iTyJ0fT63bR7qgD6msj9PD7odejaDEO63vBiSXVH_--rr5wKXMFgrbCdk_E8fVmFK5cMXO5gEOe72INn8tYv2_XBOwtpOfy6fbAG4oqJmYp2THo5eDGIs-aZP-3CXlxjs1AwqjGF0LI_TAepN_P7-oPmz_7Xlr7a8OdvuYLyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😁
با صرافی ارز دیجیتال اوربیت از جام جهانی ۲۰۲۶ جایزه بگیر!
⚽️
🔥
سوپرکاپ ۲۰۲۶ با جایزه 4,000,000 دلاری شروع شد!
‼️
بدون واریز یک دلار، رایگان ثبت‌ نام کن:
✅
وارد بخش Super Cup شو
✅
ثبت‌ نام رو بزن
✅
کارت تیم‌ های جام جهانی رو جمع کن
✅
الماس (Gem) رایگان بگیر
✅
توی مارکت پیش‌بینی شرکت کن
✅
جایزه بگیر
🏆
جوایز جذاب برنده شو:
⌚️
رولکس
🏎
پورشه 911
💵
هزاران دلار USDT
🔥
ویژه فوتبالی‌ ها:
با هر گل تیم ملی ایران 2500 جم رایگان دریافت کنید
💥
نکته مهم:
این جوایز با قرعه‌ کشی نیست و هرکس به نسبت پیش‌بینی‌ درستش از جوایز سهم می‌گیره!
توضیحات کامل کمپین سوپرکاپ
همین حالا ثبت‌ نام کن و یکی از برنده‌ های بزرگ جام جهانی ۲۰۲۶ باشی!
🌟
https://www.ourbit.com/register?inviteCode=OurbitIR</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94949" target="_blank">📅 21:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94948">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1uZUaTcyR7SMv8Lu-qCnekk6RsCwbjBfTCEUvEvImvY5TEFoFdyxbpvU1utvCyuLy7YXFxXgUyTOUxCg_QMNcMW41s0QT1uBcyQjQfA37fpSteejOUaV7U9cMcl-V-tOsHDbQ4EoCVG2WGP9apYpI_ipeOOzS2GES41Scq_IXJKwKkbPYxBAgwITLYU49H6s35emLnm1sCV73BlOl5SxVNxwD2o7PE7AAR6THRZaI57KHwync20H0lVJHt2nGx0aw24x4KOD41ixz7Q7JhCxbY5Y67E5mlFA1gjbL_wGebM3IGhHFlKApE2YzA2u_6eLgC4rWVhfvclrh_qfhSpHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|شب تلخ عربستان؛ اسپانیا با اقتدار پیروز شد.
🇪🇸
اسپانیا
😀
-
😏
عربستان
🇸🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94948" target="_blank">📅 21:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94947">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وقتی عربستان اینجوری لنگارو داده هوا دیگه باید ترسید که چه عرض کنم باید ریددددد
قلعه‌نویی خدا بگم چیکارت کنه امشب سوژه میدی دست عربا
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94947" target="_blank">📅 21:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94946">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فران تورس
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94946" target="_blank">📅 21:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94945">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc6utYW6n0gKkBz1NqhnZaiy8NIp6M0r5uX5IqnlEEFZqrReS8g9CHKDyEV7P8VioOddr4WV6aslr5RBMsd4zrADr_P3gfADu64R6L9PG3zwsW11R0xvqJGOJ9DJRuPs_gSEG5tmd9NFj7zM2XyNiogtZ2CiwGXD5d3i7aqreTKYRPPku4FzvxTnevBQExL-hhcoHNYIBzIY4iSrU9kyEhP0R-Gm7qa4ZUJH1E6eyJxRK22WgnUu_K0PRTvSfCkK7kUXREiPkmmy6YALngAz6S0LGrGsP2PLy1sYfMwI7NldudbU-dGUykHFRKxsugQDKZC6SfxB69yt1UZkcSo4cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوادار عربستان قبل بازی : اگه میخواید قهرمان جام جهانی بشید به عربستان ببازید
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94945" target="_blank">📅 21:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94944">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOnYrajRCgKWonDEqaWXb78bnNxTPH0Hq-h8SJ8Pya2jX8L_gDFkhnKZAf2nOv3sTgPgbfqfAaBJxeGYZti-vftntd9u47pE0qdEgt7Gxdls3H1krmhLcgUW8phh3MBknc0jdJA4sZHQN1VIvwYpdIWc8yJKHVR-Yb271qXjez9tRdHymlP198TDePnJwlPzboShHKDggLFdBjnhYSyCxsl5WR80FXQ7Rm9fxyeT9w5atMZAUzAcYRXyPbHSB1BcOg3_hzKx3ZktQR8VeXMOMYwsMhhgClyd97XyMDt8iSYEeegUuUu4WQHYA0lBYLOTYfPUalQRYk1i5BobrmjcLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚔️
🇮🇷
یوز ایرانی vs
🇧🇪
شیطان اروپا
🔥
تاریخ‌سازی ایران یا بازگشت قدرت بلژیک
📅
۳۱ خرداد
⏰
۲۲:۳۰
🇮🇷
ایران در ۷ حضور جام جهانی هنوز به مرحله حذفی نرسیده، اما این دوره یکی از بهترین فرصت‌های تاریخش برای صعود است.
🇧🇪
بلژیک پس از حذف غیرمنتظره در دوره قبل، به دنبال بازگشت به جمع مدعیان فوتبال جهان است.
🏆
یک نبرد سرنوشت‌ساز؛ آغاز یک تاریخ جدید یا احیای قدرت غول اروپا
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/94944" target="_blank">📅 21:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94943">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
‼️
🏆
برخی از نتایج تیم‌های عربی در جام جهانی تا این لحظه:  ‏
🇶🇦
کانادا ۶-۰ قطر ‏
🇹🇳
سوئد ۵-۱ تونس ‏
🇹🇳
ژاپن ۴-۰ تونس ‏
🇮🇶
نروژ ۴-۱ عراق ‏
🇸🇦
اسپانیا ۴-۰ عربستان ‏
🇩🇿
آرژانتین ۳-۰ الجزایر ‏
🇯🇴
اتریش ۳-۱ اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94943" target="_blank">📅 21:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94942">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فران تورس
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94942" target="_blank">📅 21:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94941">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گللللل پنجم اسپانیا</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94941" target="_blank">📅 21:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94940">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmdij4pellflAUiLbEOiQ_Ymc_Jl7b96f07TMlDZxbt6W6i6iMSS4CWcnxJztlAzPvJl-tJfOHUi1MTnsoq80tT6FgSF1sK4sl72wpW8pt777Eq88fFw_RPi3BejxNJ3auBOq47XzZ1SHiSmovI98GevF1dMbHI8bifzFW20U4GYQWdCah5mM98duafWEEV5QBYVCONrc_Wug4dVwDZkhsjRPMGjNlDNdBxIkk5Mlk7f750Ez9tYLujnncz1U0QyX2R-imHygLqQNZr_qOeBUvX97_UHv00G5gp3jS5-gZRNX9JDrd63EzQDGz2QoKnmmGLLDMLwbUPEYDSj_5exSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🏆
برخی از نتایج تیم‌های عربی در جام جهانی تا این لحظه:
‏
🇶🇦
کانادا ۶-۰ قطر
‏
🇹🇳
سوئد ۵-۱ تونس
‏
🇹🇳
ژاپن ۴-۰ تونس
‏
🇮🇶
نروژ ۴-۱ عراق
‏
🇸🇦
اسپانیا ۴-۰ عربستان
‏
🇩🇿
آرژانتین ۳-۰ الجزایر
‏
🇯🇴
اتریش ۳-۱ اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94940" target="_blank">📅 21:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94939">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic2kXWtF3YXliPXEtfbXZBwkCnDsPR9xcMKES5LeA_KB9T6JS5hiVvD_i6VF4Syr2iOZxE6j1eNIyzCOaRhJuw8ka2To2KcIGpoqPs84-Yx-Mjd4kyjYXs7F37Eru97DA6Jd2UDr2RoxMXh1qk9Y2-ChVZxCKSb7rSj6beg7GqOCUejHzcTo897FtmoQS4130KdXZ1Dokq4qwneU_c_cAJ1XdvhwstvGS1AxmfLqr6xA0TA-3U2bnOphI2XwX8z5pfo1DmrR9HTgs4ldFFigx21FzI3l963x4Egeim8H8yhZPQ2Mu9DR8sYzqwTDbN582_E3oEYjuN86rZMozy-w5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فران تورس در یک اتفاق نادر امشب این تک به تکو خراب کرد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/94939" target="_blank">📅 21:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94938">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yt99B6K7PmN6dqNXdlLiS1BUNUcFFVf6z6MBL9dEduLEkCaL9XvTHfRzQq7XDD6XGtqhRldkIbsdiZedeDJ1MtnKUUa2F2iH7E-mH5W-HVnUSqTRoa_6-7V37z_DgYYFeAAvpvE5Rj2i1Ve5UL4-fh0RMRX3MHI3voi9h9W6jzkP7IjJz0gZSOtF0BkcVkW573OCZ1VP5DZLGse7tCkB51F8SU6qVXpOCoA6OJ0AV7urjtFdXn9MQ6Afpi8tj2eaZVo2KkApr161a8A3wELg-unD2tM565iEvOasU96VslSNiVlV428z6ekr2tzmkCQgvf8ZIYX4DZnRnD3sHeosgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇭🇹
ترکیب‌رسمی منتخب ایران مقابل بلژیک؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/94938" target="_blank">📅 21:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94937">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🇭🇹
ترکیب‌رسمی منتخب ایران مقابل بلژیک؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/94937" target="_blank">📅 20:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94936">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ja8ttBPqttarxuqDKKOEspYd-YfQoJAUBjxuTyiHKmolwZgzCXYL0OqKSPmyoC0NCHy5xsXlPfUM__WHl5ltdy6v7wMnrElX14bNpOrYImPQEs2nboth_cRK27iK3kRnAjettlDEnQT9pBO-4zt8-KO3sM2tzA7JugW7mSACncaT_SFHzgOtDVRjPQnMRK5u5bhE13tMjaqGLq8AggSWYe10-pLrQ1SzBEjLASMKjq7hF7Ow_c7SRDXaZiPbJbSEZKMN8P7gEySA17Oj_tUVssbqVZHk0arQxUHfIX98WV6BR7kJe-W6QaFY9EQMwk2qOtc-w_XgLQUMJ2YG3BtoYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇭🇹
ترکیب‌رسمی منتخب ایران مقابل بلژیک؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94936" target="_blank">📅 20:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94935">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c051daab83.mp4?token=e-l1tBCG2FSmjzq4aHj-Ubc2wsnVy3IHe2On6mcZfkEyHqoe9hTWybtWaHvx72CJh7_ZUgStYXtwI-4VexvGJRNeSu1lOyoaG_jDhdKrlgwA0OhArDyIlSEsXbHU_pUuiQ8OXRO37rDhz5-utk3aP80IhZQrZ_MdNCPojbmmbNxygpW8gYZ--iqFu1gDJrJMWfygA52_bVAj-2UKIHnODCn-m8zplzho8Iy6rFy-Kp5Hj37gNfzp2EQ660SQSLGabFcjFwBl27BYmX8X-JWHmTCXySK7ccTvE8oAlKsnvsH1oo4argS-E_sLjlCLxkxWG9uqbBBgik6e-mFnXieHew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c051daab83.mp4?token=e-l1tBCG2FSmjzq4aHj-Ubc2wsnVy3IHe2On6mcZfkEyHqoe9hTWybtWaHvx72CJh7_ZUgStYXtwI-4VexvGJRNeSu1lOyoaG_jDhdKrlgwA0OhArDyIlSEsXbHU_pUuiQ8OXRO37rDhz5-utk3aP80IhZQrZ_MdNCPojbmmbNxygpW8gYZ--iqFu1gDJrJMWfygA52_bVAj-2UKIHnODCn-m8zplzho8Iy6rFy-Kp5Hj37gNfzp2EQ660SQSLGabFcjFwBl27BYmX8X-JWHmTCXySK7ccTvE8oAlKsnvsH1oo4argS-E_sLjlCLxkxWG9uqbBBgik6e-mFnXieHew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل چهارم اسپانیا به عربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/94935" target="_blank">📅 20:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94934">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گلللللللللللل چهارم اسپانیا کوکوریا</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/94934" target="_blank">📅 20:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94933">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گلللللللللللل چهارم اسپانیا کوکوریا</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/94933" target="_blank">📅 20:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94932">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نیمه دوم اسپانیا و عربستان شروع شد
یامال تعویض شد</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94932" target="_blank">📅 20:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94931">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHgv2MkHB1qk5g0R0M_l81QCYjP9JvqU3zk4_qz8zDJhkhmQ5jf9gufGzd5Lwa16RUkrLHtPvqs1xtsv23pixNUmWzqxNchkzmMvJRXZfm_bSkmRP0pPbHRcHcKB9z1DEA_-SP3ZT6D_t2zfe3S_BdrNUYY8NiZtgut5hlHyp0b_-fCSdR2OoiCqJdPZB1xJPolUbAF6C1tJ0kKj0gFGLn3s3oTao3xYK55TddCC_n0uEA75r6JM-S1U-l6hqsxiatdBBfd6eFa_tnEwAl9nzWz6uqvzZ2v1FXObkHKwzrssb14CZ_VYGnF1tqBheZSbdGwcZQgnSbcAINq2j1-Zeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
وین رونی:
یامال باعث می‌شود هم تیمی‌هایش به توانایی‌هایشان برای قهرمانی در جام جهانی باور داشته باشند، درست مانند آنچه در یورو انجام داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94931" target="_blank">📅 20:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94930">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFlT2GBAqDynNTvaxoO1LvTn6LBpp8Rr1BeAOH-WPNPBcvOgdw6trBtkZH3Yg9J5pgMmb9h3-1FwrqdJ5JfwPKD7FOAFgNvQh82KUPq1wFGop7DUXQqxEg1uqDS6oZPS2zzbNpnJe_YknbaxusC2pCkpbhLK0iChuBkR5ILfnz2lbI0HjjjKmVzpYGnVPQJPiges586HFrmDBUitJMrF4iQQSkVDV70rFToPqscgKesC9YmxyJR44Bx1tzR9-3qAO6slHJulqOx0oXXCkcVVuUEXrfg0krSknXa37PaDutM92YIt1NR7_DU7C6fOrFgxMFa7K0cgJbgIDHr8eYfV0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اسپانیا برای اولین بار در یک بازی جام جهانی سه گل در 23 دقیقه به ثمر رساند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/94930" target="_blank">📅 20:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94929">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/94929" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94929" target="_blank">📅 20:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94928">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptXZZ7m14ggHgs21sBPUj-ozYc9lXCuJKUkjIjJCwXu0KgvlIWxdRXp3ey2sgtvejvuRG1wGQlv4j7ZeKXiWCrv1MzUyTbaU1GF9ScEOZ19mdwgZRtwx7uhADCN-y4USoJOIEN2alUJpXkYEHicbAfhwRKgn-ujD2-QP49sWVyeA3Zhjr0bMXhJwXF_O8VsX88GMz3U9kBYlCRxhLJGuRmnR_87xTlneM5KajIzixoqEKzEs7vOk5vazeG9A6tTsqqIQ_5EVijzr95FMFS8MkpS2bzFNgv7cZ3EQC7JW7FtDCRfSOtdSk6ylfp4qvP1_v01KH_RlEL3MqCVeYpLLQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94928" target="_blank">📅 20:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94927">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESS0IUpEYvJdSui1hQdDgfLyXviZheHtH8W92sf5mlWOq5EMXzFiWBZjttMJ-dKkvChCC1TejzDSyaR_yrvTYrsadO6Ws7ilFkTd0Kkvx8gXdGSEblWg7UoEK-5xxC_ypcikxdFNIVW2C1ugaMxzJ6AbSbm9kXZMoNrwwHsOa9tZ-UlXpmC51VK75-txMX42M0UE1AT4H5nVIAd3IkcLzuJq5D3plLuKfZtoNb-LJ86QRvHuqlAkMO4NgNKTdYtDmDAHwLdCLiPKZw0kxtMoTbVUhlFMBsXqgKmitPw9DgXqfQFPq5U2AOr16f1iNXQ9t_XyVkNbZP53pqy2yN8ciQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی بگم والا، حتما حکمتی توشه.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94927" target="_blank">📅 20:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94926">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baLl8pIs-4_7YvHUmFrsiVyic7rRHv_iePeCVuorVdoSbFAnj2sGF9eQD3DhHdBoZ4YKtKw_cSpe0zraDnww1I-SoyqzsumW8s1poRr51UIODow_34EnbrZqWWyRxuXLgAIvgk-BjOzsThX1Z1vmyHHC2ZBmGga8woF0yZ67ZZYBKSdQ1ESMysPeBdxRIGF-Ur7jGQBdyRDyIul0uxVUeFdWf8JJ76oVBv9aPw3Sa60VZBZI68DBD1DjFICg6DuFxGGqsRQpL6fzNjvZkrETj7_srOCWbfeXfMReOUcfkJOq34Tf183mr64fmZe8Q_A0MBp1W9jZxmeRtanQPsJGow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇪🇸
آمار بازی اسپانیا و عربستان در نیمه اول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/94926" target="_blank">📅 20:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94925">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پایان نیمه اول؛
🇪🇸
اسپانیا 3 - 0 عربستان
🇸🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/94925" target="_blank">📅 20:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94924">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">امید گل ( XG ) عربستان : 0.01
🤣</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/94924" target="_blank">📅 20:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94923">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XarS5GtSLRLAKOQGLfGz00EcOjBVC-xKFOP_lS7QbuIb-vvr0YKJh0-sKe1Etfco1i_3IQvS4J1DXBdvAfyf5FiTHr7bV-mFL5nEaqm0PuOK36J2P1xukBoiyCvYkXGTF3l0TTedJOU0QfSv9AU8qdCxKjSlW04DjJWZuYbp2lpZhyV4XQHjJxz43yVxlukkmHWwiePsNMA-GimWNDTYPSi5IHzdBrQrg6FeF0_gUACuZNy5zsfeIoS4dO-E5IFSiC0c89Wh3_Sf5RG-jQCU6Qvw_2RCbbnZrqA16wpMoPJlHhHs1zT-_4PbjaluUazwMlJHgJvD9JipJRI3HzC-mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
2 گل و 1 پاس گل مقابل عربستان در 24 دقیقه؛ میکل اویارزابال اکنون در ۱۳ بازی اخیرش برای اسپانیا ۲۱ گل/ پاس گل دارد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/94923" target="_blank">📅 20:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94922">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIxGkcTq0IRqDmwS3Y8joBoIy2j6mSACSQWBpx8kcFJtP4cMuM9I3_3HukABbnFImUXInlgO931cvI08aNiFxMR6pqixmG4bBr3GuEeTkE7iI3fwleuniO62-cyeNSN8waqvis9DsgBQKbs8zKL9cEyA2PR8s7bKIbQkztUbfhkO-P6Q6AyOQiMOoB-H66x2LcNEmKXXBvXonZwdrVqVsNEVvP8A2Vhy32fRWrV-X2v5H5wjef5nMt-ujO21WCnFTLw7hSXATU5b5paecssWQ2j4N1ePu15E7d06bxIdRhzymbx0vJGxL5ni2lSe1Rs-ehTSjcYrHvfiaJwZzmHEUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی: ۱۸ سال و ۳۵۷ روز
لامین یامال: ۱۸ سال و ۳۴۳ روز
👤
🇪🇸
لامین یامال نخستین گل خود در جام جهانی را در حالی به ثمر رساند که تنها ۱۴ روز از لیونل مسی جوان‌تر بود؛
🇪🇸
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/94922" target="_blank">📅 20:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94921">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/19139588b4.mp4?token=GGpCwp9GS4mY87PCG30WCAf6lIouTKxXRG3aXknrdnB6vWZc5zzFMbUXfEqzi2pP3Otv943eqIoUUy9eqOcBxpzeSZTYNBLOVfm6Qs-PylJfmTc7wEg0uMfkVf_cKP-_ly0WxmdmqG1Pmp1FwY8XOeF01__X8yLy9_uJMnhu2V-IJnFqDZifmEyobxD5oDiKAw2aZQx09lQAO0VE7ndVedCbh2Z-ye1YPg0ySU8V2Z7p5NSKSeAcng24nx4H7C4KiZ-uZKFaelGtYj0CFSpi4OHU8Nh43T4VV_9vFHuSSuDvNfdqHknbzaIoaIx_HVLfwoylpGDEMixVTs-UZwpAfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/19139588b4.mp4?token=GGpCwp9GS4mY87PCG30WCAf6lIouTKxXRG3aXknrdnB6vWZc5zzFMbUXfEqzi2pP3Otv943eqIoUUy9eqOcBxpzeSZTYNBLOVfm6Qs-PylJfmTc7wEg0uMfkVf_cKP-_ly0WxmdmqG1Pmp1FwY8XOeF01__X8yLy9_uJMnhu2V-IJnFqDZifmEyobxD5oDiKAw2aZQx09lQAO0VE7ndVedCbh2Z-ye1YPg0ySU8V2Z7p5NSKSeAcng24nx4H7C4KiZ-uZKFaelGtYj0CFSpi4OHU8Nh43T4VV_9vFHuSSuDvNfdqHknbzaIoaIx_HVLfwoylpGDEMixVTs-UZwpAfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل سوم اسپانیا به عربستان با دبل اویارزابال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/94921" target="_blank">📅 19:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94920">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d28a05ce5.mp4?token=l8HnbglXECoHp1npw7sAQ082A0N5HGcFomZBahcBo1HBHfx6ssRmblgilihYAv8UwNZ9nHMBhYu7PPGcLWEOs5w3OXm2dJqbjLCxYpvEyW1GK7vvbnqy7d2qC_KjYvNcj7SsNBZOiFQNb_GvxOu8G7mf4xvGYT1L2Db6pynoUu7lAhFYztrp63maTC4O0D1e1u2ixL8VdPvYKr4-_FBVBsBVIPxlBefLEngwZ7fFGR3rppXyU6IIqrOPcFiojtmdL7PBDW8h1tcXcB36j4sNqcR3T49U4ZO7EPfs-eF2q4yDZ1FvgCnarBLwKo6YxipDBOl3uDySsqujK2HkpWGJA5U9dqujyZBahzidaZ_vRY6T1WRv3FTP_SPNOTInerAf9tEymDKA94FCQcqXU2O8IxgtRPappwDY0vq4WPjf8uSHoBUrQhycPFsyaLC182vgQvC65XYtW0XokARx0GX_iMQpohzVvew0b_qWiuMt1OSuyC_XJW9q8pRYt4-XA0-tDDA8f7t_kPjQcH1shGlLViwl5ECFzLSuo2n268pig8pK_Sh_PFuL9Cll_nkEEbFAbFiu3-89hXMc6uoKLAWuLqok73kx2ZOX-JJnPCENa7HRkhsweJ5vjFwRS6pFXs7OJdlLd80KMV5Iqi8K1fO7Gw6q7kUeuqYz5QqwA8UG8B4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d28a05ce5.mp4?token=l8HnbglXECoHp1npw7sAQ082A0N5HGcFomZBahcBo1HBHfx6ssRmblgilihYAv8UwNZ9nHMBhYu7PPGcLWEOs5w3OXm2dJqbjLCxYpvEyW1GK7vvbnqy7d2qC_KjYvNcj7SsNBZOiFQNb_GvxOu8G7mf4xvGYT1L2Db6pynoUu7lAhFYztrp63maTC4O0D1e1u2ixL8VdPvYKr4-_FBVBsBVIPxlBefLEngwZ7fFGR3rppXyU6IIqrOPcFiojtmdL7PBDW8h1tcXcB36j4sNqcR3T49U4ZO7EPfs-eF2q4yDZ1FvgCnarBLwKo6YxipDBOl3uDySsqujK2HkpWGJA5U9dqujyZBahzidaZ_vRY6T1WRv3FTP_SPNOTInerAf9tEymDKA94FCQcqXU2O8IxgtRPappwDY0vq4WPjf8uSHoBUrQhycPFsyaLC182vgQvC65XYtW0XokARx0GX_iMQpohzVvew0b_qWiuMt1OSuyC_XJW9q8pRYt4-XA0-tDDA8f7t_kPjQcH1shGlLViwl5ECFzLSuo2n268pig8pK_Sh_PFuL9Cll_nkEEbFAbFiu3-89hXMc6uoKLAWuLqok73kx2ZOX-JJnPCENa7HRkhsweJ5vjFwRS6pFXs7OJdlLd80KMV5Iqi8K1fO7Gw6q7kUeuqYz5QqwA8UG8B4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل دوم اسپانیا به عربستان اویارزابال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/94920" target="_blank">📅 19:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94919">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گلللللللللللل سوممممم اسپانیا</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/94919" target="_blank">📅 19:54 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
