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
<img src="https://cdn5.telesco.pe/file/l9Ok3GDC1DKY2enHntFJFNcOH_b8T7gktxg69k9FgjctNIlr6-kkfK_MUQREOZU1RMSxLi6V9BcBdldG3vKrxMc0PSSYSWPwTlC79eRM46_6xLhZGzmhYA5CCFJVdIxV00uV5-SF2lFKKTgfsbxpYQnslJZfXWZS_xWtQesJVM3iQATWgOH1QujRmMQu3Nllil-c-CLD3426uVDwN5kEfwRA7oDNJv-Po8PxJNn4ZVNwry4KbwWpZ45B2Ta1DPk0GI16Ti47j5JnbhfsvFwJANQNqbJS7m86DDwZldqLt3nhXgyObQ3CqpUGaH7VCAIFDRrA3EOb0JaXYEFUKr8I2Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 647K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 01:23:42</div>
<hr>

<div class="tg-post" id="msg-94059">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c11f876f5.mp4?token=KHRcxF6eUxO2tuvnKPblfGVTuIqG--SS3jkIQV-tMRct-JH1zL_z6e_o0yuj78tnvj01PecsMJsOmtkDx5FoiFm8v7rd9VhAqRdDS1b47oXj71v9WPXczEDvHIGKB8n4Pf1l7BjwuWSQPz1QiJ8pXg4pfaqERTE1oPEl9kIuRlIU-DU5SOrxDLRwev7K-Ef1SPttZNTx2k7tnefN0ebW4R6W9QqHpgG1kx4xAUObxAIvVXJqTfpBqtUzqhuivA8vzMcS1OFvexH2Cr3yoZ2jXrJd_g8hI5LEJvY3FLcro4syUmpuEzuBOFfdbdz6QKQ0lcjkQ9cBi-5mbGTSrbMge77Wcp9IgDF1vzuruh6INGAiJqD4TRDg7lJl3NBJM4UG3eqM7Z8WXWWkeSxl3OVVfUkaTFWg1CHbR6WRfKygnGU6b2nBMep__Nk7dEwE_Ke0OZ0mIDSsTtBfeMBfw3lw6XF5jbsDpan22h7kBgGEcLXpOm3d-IwlLXiRUexcC7-z2LKS8wC8cYhVjBwMGMEa82FahvMBmhEXVJggFKx61fTk-n625UOgPRGYGB4-BReXM7V-34IT7CgtDL_BrH6pj0WqlqIw9ZBn-g7nl80IpAdriDqolmay7ErsJsuS75zT6PG5Tv_ycqiNHJQ1XtFiImoUpSUu_5sP_CJJrXAsFzs" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c11f876f5.mp4?token=KHRcxF6eUxO2tuvnKPblfGVTuIqG--SS3jkIQV-tMRct-JH1zL_z6e_o0yuj78tnvj01PecsMJsOmtkDx5FoiFm8v7rd9VhAqRdDS1b47oXj71v9WPXczEDvHIGKB8n4Pf1l7BjwuWSQPz1QiJ8pXg4pfaqERTE1oPEl9kIuRlIU-DU5SOrxDLRwev7K-Ef1SPttZNTx2k7tnefN0ebW4R6W9QqHpgG1kx4xAUObxAIvVXJqTfpBqtUzqhuivA8vzMcS1OFvexH2Cr3yoZ2jXrJd_g8hI5LEJvY3FLcro4syUmpuEzuBOFfdbdz6QKQ0lcjkQ9cBi-5mbGTSrbMge77Wcp9IgDF1vzuruh6INGAiJqD4TRDg7lJl3NBJM4UG3eqM7Z8WXWWkeSxl3OVVfUkaTFWg1CHbR6WRfKygnGU6b2nBMep__Nk7dEwE_Ke0OZ0mIDSsTtBfeMBfw3lw6XF5jbsDpan22h7kBgGEcLXpOm3d-IwlLXiRUexcC7-z2LKS8wC8cYhVjBwMGMEa82FahvMBmhEXVJggFKx61fTk-n625UOgPRGYGB4-BReXM7V-34IT7CgtDL_BrH6pj0WqlqIw9ZBn-g7nl80IpAdriDqolmay7ErsJsuS75zT6PG5Tv_ycqiNHJQ1XtFiImoUpSUu_5sP_CJJrXAsFzs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل چهارم انگلیس به کرواسی توسط رشفورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/94059" target="_blank">📅 01:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94058">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">رشفورد</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/94058" target="_blank">📅 01:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94057">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بالاخره انگلیس چهارمی رو زددد</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/94057" target="_blank">📅 01:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94056">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گللللللل</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/94056" target="_blank">📅 01:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94055">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">لیواکوویچ نبود کرواسی راحت 6-7 تا میخورد</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/94055" target="_blank">📅 01:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94054">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پیکفورد هم خودی نشون داد</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/Futball180TV/94054" target="_blank">📅 01:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94053">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIKMaUfXkh31aH-u8V9S0P3shD6VY6gxvHP4vT_UKp9LNVRONh4guLbAocyKNadwdiK2saeNbi7Or22PG2hlx-TgvdGuZXZcUJm33lJZ1rfagwQFMExGdPbRiTtj63M1XTRQpp_mxurtPRsmfLG5Jq0kC-12hDX44-q42gTNE48ccdd0utQX3DWWKH5ZdOfm0mrrwziyeDhGoePKiKHhLVcXksZsMb_Pvobnv8TrJ0Ytt38xiAJs24Tyxc_nzRYCWf_B2bhO8XXWIu9gcPWJuyANYv5UCHOrn05jZoj2fMwBf-oygKEQMmkAWVhYHK3_o7oVfI00iI9g4hyoDGqX-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇭
🇵🇦
ترکیب رسمی غنا و پاناما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/Futball180TV/94053" target="_blank">📅 01:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94052">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
#فووووری
سخنگوی وزارت خارجه: همین الان تفاهم نامه بین آمریکا و ایران به صورت دیجیتال توسط رئیس جمهور پزشکیان و ترامپ امضا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94052" target="_blank">📅 00:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94051">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">لیواکوویچ، کل نیمه اول: 0 سیو
لیواکوویچ، 15 دقیقه اول نیمه دوم: 7 سیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94051" target="_blank">📅 00:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94050">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بدون شک بهترین بازی جام تا این لحظه بوده</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94050" target="_blank">📅 00:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94049">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مودریچ هم تعویض شد</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94049" target="_blank">📅 00:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94048">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پشمام بازم واکنش نشون داد</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94048" target="_blank">📅 00:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94047">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">لیواکوویچ یه تنه نزاشته انگلیس گل بعدی رو بزنه</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94047" target="_blank">📅 00:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94045">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rW0vi_2RGo6Ftpd2F8Rq6ZR0obOW_smn5WVm8bJ8H8zjfY2pKA0UWoBgTD1Zf8z7W7288We8mAKhPM_Km97RtkH9dRZ10TUqLNlzF1I2MOfxlPnKMvzxcTDPXIxbWoT2buBsmKUSaxOrz_Zbz8zLMdVly84owjssW0LH59yR4c62baTn3jeZxVku-PhsUB9Tk4_Ox0D0Jx-NUrJrvi-dEPI3cvyVMc15pKhWDEQZ2DomToo4PigBr4keumHASOlyue2hHlM9keKIhPis_KveJR854g8Ccma7imd7RpxD9UNE_abmfhn5LC1GGnr7kl7A_jl1ZUiMAqHNeCg3wO93_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d8mo_WoRkn7yfpaiyexC9XRG0jlykdtwqvkd0emVfVEIAZyU1cxWN-HwxairdqE8uY3HCewRhIvk2cPIUtmOGCArHRTRJvFwzYxLGvrBpg5r_Uel_dBm_maNmMaG-fEVFFGBsQXODbBySrs4lJZwmxoEvZDTE_NuuZFE6_Uxjbf9rhFmWwCK8iAWlMqiOsT6ud-JhIR21CpJMbV1JMX08PBNmAD8NjLNFzfOdjQELox1h8wfz4uWh1I1oKhpBAUXuQuXrTEm8OvxjZVwbdMHd_mQVbq2TXkj-G5xvnLedc5XQhhWaB7pMUpSnTG0GHq9Ad_QaUEN9S0Yl-ZOZ9-1wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شادی گل همیشگی بلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94045" target="_blank">📅 00:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94044">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انگلیس نزدیک بود چهارمی بزنه</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/94044" target="_blank">📅 00:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94043">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">گل سوم انگلیس به کرواسی توسط بلینگهام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/94043" target="_blank">📅 00:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94042">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">عجب بازی ای شده تموم پشمامون ریخته</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94042" target="_blank">📅 00:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94041">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">انگلیس سومی رو زددددد</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94041" target="_blank">📅 00:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94040">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94040" target="_blank">📅 00:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94039">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بریم واسه شروع نیمه دوم</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/94039" target="_blank">📅 00:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94038">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZUc0zbsV2KjwqE0NxN2AphyQX2LGgeWsJdmyqhg8_YzHyX_QZvBo5DLNyIJRtYXUNWU_YrBg2LqEEv4nwcpur8h_WE2RZ3bc2nyYNUCdWrEB19ChMzwSZllygDjZ9bcTKaAKH7PCu7a1J9dwGpn1a493kax4wr-XdaYMJ1f7Mz-ccvk9z4r7qCUEdDA9O7U9YuwZaLPty6teMuK-4Pl0BIZeZrW6gmYsj4eF6VNSGmocTkIEp-7r6vuWSbYtGkyO9J9BnUctn6xb1TYSE5f-qS1OcgO7czbWltln9YCCPM38Kii3rlrYeE_FsEk1w_GO0n3naYwkj_Ihk8QP-MMMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری بانو میا خلیفه برای مهدی طارمی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/94038" target="_blank">📅 00:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94037">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r21Jhomq2QjXetac3j098lXcbrBxI9MaGHG0220eXwC3tFJ2kA0e5yzGDsZsFXdooUzpF08qyweg2tKN3Y33_mGLYUUa5qIQmGRFxmrd1nOk4gxNWLuLkHiCCy904KQj0mYiKwlIxMG4OQfOElXC6rPigDoLJIkw82lcK-XtoQl9wO6qaKH8NWf50krEOrVV7yw1oEZl_EBe4LXgg864UiUKlDPzwdX69UnqkcI2MNWCQ9Sfd1oH1y9BKdq7ViuyTuPQIAC0s0fuAj2LD9VuGJLQTcCtMTM3Hcup4defzlZWk1GhbXxwTplZdw3OqkcWdi7ZHP4W5KADlKVtKhRrwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هری کین با ده گل زده به همراه گری لینکر، بهترین گلزن تاریخ انگلیس در جام جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/94037" target="_blank">📅 00:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94036">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پایان نیمه اول
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس 2 -
🇭🇷
کرواسی 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/94036" target="_blank">📅 00:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94035">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">چه بازی ایییییییی
چه گلاییییییییی
لذت بردیییییم تا اینجا</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/94035" target="_blank">📅 00:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94034">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3d4cdc8f46.mp4?token=q0QTIVUVLk12VNBmdM8R_dQmrV2NiSW1vJJDCZ6SasvtAn_HYoVJCZ2eMBXJK8mhfS4XKgqzpCS28dtnq2p4JIhRAgi8FJCe27l3Ve3qBi68nzMtWPsCszHhwrRUtU3FQDClGNvLZAoAY_BfEmLbETfJ3G0owrXmMIUkmZ-MlbfDEZNRganBZAGUrgynGffWPw0SfkwWhrRoHBGKGK5DIV60Jx0UnZK-eOJQ_f88p3Ni2SmQHxm6ZIXWwrObsNYke0-qlVMlHM0lL9USm5JEFPU9MzK6zJuWjLclsYDK34MJi4RcB9UOdBzd-5Km78NBHd57aKdCzdKUSetZ3AkZOKcMVjfukXPP3zUE_eXLT71hSvd_TYQi1Kse-rEV-q_jPg1XpsNHWjn34l3qCOv3LQ37hhkC-H5tlDWLOnEAt8WkyGLZ9KKAk0It-wOqZ1QraApJAtoCCBdShu9uyOgAVwyFLcitra3xSaowtTEL1odPmtHgBD-yzvaUhyrmaoeMCCyprevGegO3-VxNDrpsEmPrbDMscZXVUO03UnMCo7Isw1c_mSodpciqaCvQ0pbG_dFn5DkuSH8ytyG-m5GnZuutjnKUbk7OSgWMHD2HaRCHqQda8o0Tz22HgdZCIGUKLOTjHqrjGc_w70LKU0QjeSKq58DfBos4yLILxUYMUEo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3d4cdc8f46.mp4?token=q0QTIVUVLk12VNBmdM8R_dQmrV2NiSW1vJJDCZ6SasvtAn_HYoVJCZ2eMBXJK8mhfS4XKgqzpCS28dtnq2p4JIhRAgi8FJCe27l3Ve3qBi68nzMtWPsCszHhwrRUtU3FQDClGNvLZAoAY_BfEmLbETfJ3G0owrXmMIUkmZ-MlbfDEZNRganBZAGUrgynGffWPw0SfkwWhrRoHBGKGK5DIV60Jx0UnZK-eOJQ_f88p3Ni2SmQHxm6ZIXWwrObsNYke0-qlVMlHM0lL9USm5JEFPU9MzK6zJuWjLclsYDK34MJi4RcB9UOdBzd-5Km78NBHd57aKdCzdKUSetZ3AkZOKcMVjfukXPP3zUE_eXLT71hSvd_TYQi1Kse-rEV-q_jPg1XpsNHWjn34l3qCOv3LQ37hhkC-H5tlDWLOnEAt8WkyGLZ9KKAk0It-wOqZ1QraApJAtoCCBdShu9uyOgAVwyFLcitra3xSaowtTEL1odPmtHgBD-yzvaUhyrmaoeMCCyprevGegO3-VxNDrpsEmPrbDMscZXVUO03UnMCo7Isw1c_mSodpciqaCvQ0pbG_dFn5DkuSH8ytyG-m5GnZuutjnKUbk7OSgWMHD2HaRCHqQda8o0Tz22HgdZCIGUKLOTjHqrjGc_w70LKU0QjeSKq58DfBos4yLILxUYMUEo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇭🇷
گلللل دوم کرواسی به انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/94034" target="_blank">📅 00:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94033">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کرواسی گل مساوی رو زدددد</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/94033" target="_blank">📅 00:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94032">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پشمام از این بازی</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/94032" target="_blank">📅 00:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94031">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بدون شک بهترین بازی جام تا این لحظه بوده</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94031" target="_blank">📅 00:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94030">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گل دوم انگلیس به کرواسی توسط هری کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94030" target="_blank">📅 00:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94029">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">انگلیس دومی رو زد</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94029" target="_blank">📅 00:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94028">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/94028" target="_blank">📅 00:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94027">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گل اول کرواسی به انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94027" target="_blank">📅 00:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94026">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کرواسی گل مساوی رو زد</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/94026" target="_blank">📅 00:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94025">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94025" target="_blank">📅 00:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94024">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAPOJJ-SkvZRMZp1A11DP3C8bPJTlQ6ocYXV5t1CeaVDj4f3SWKvmmlIgKjau0dBq6LCZEJTMfhemp5eOdzZLKvczKNDeXkgpyRAkk-UgIwTaV4YtwNp_iHqOj0TmJMm0cQOmI8Hf04ZNtw3DiSu7xwZ037IgNYMVTIXWKKMfgZrcbRNy7iIP-oS-KpnLgniil_VeW-Obk5lT8SG8q49UpwuV6ZSyQsENYTrB03zoN97lEzc9-yf_EGi63LN8yLjOn9n6GpSJy3S15PvzkYWU1KG-xM2uw6vdBNsEI01TgwJYlq4pUfAr1Sk64LX95DJ3H5T-7yZfhcfGHLUK0_Fzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پست جدید رونالدو:
این شروعی نبود که میخواستیم، اما تا پایان فاصله زیادی داریم. سرها را بالا نگه دارید، روی بازی بعدی تمرکز کنید.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94024" target="_blank">📅 23:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94023">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/938fb471c4.mp4?token=sy6JQ3WXzlrPyKS1-1UPzCF4giQp7AqfJHuKkKrm4i3QueZR5ap9abP386PpBrraVoF9D-hH5eTuR_TqpEg84Q9ILoid42aFkPmN918MZS-SXJT7VtPaGEN4otWpIMbw1W5HFa3B5du7lsoHWlyHAa5A0VbMQjX1A2YI7h6tqJofc3PtYdsuXKC-j4Z9H2EIL1HNK6kHNavFwOxR_blf8gntH1UhNmjDSk3X2xckshCo-3nZXxXQ8XU4IIp05DZzu0XasfdjXIHGC8CU_WHp_MxIZ7sHTW9j14JLIFmaga_oF_M6Td38BYhfRfenR0D6jC_dhAzyNb62HJamc8s4qjP4L9sfYTfVWTA0OQtf1SRfPor-TRYhP30fQzvCIfNiETGRwAVB038aMe0FfZH-xIw_SFoDoWjBmzE0-xWhzeEG2XCFdWD6Qjpk8KxUS-2NcEQ1UtiABouK_YoXo4TZ0bcSVarj-fYUpkC72CS98VsWGYUQdHweRg9o3g1tVpbE1RLi5VgohA7lBb1Egr0Xi_ehA8xVApCsohy-yB_-kVJLK4mz51QTBx0rPyffuGMd5zaGGEAczBHTm5P4V7s95FEVPta2CYBJXLT6fUYdADcCubC6bWXUkejyMQNyrqkrfs2M1Rhrb2Zawbs78u2ZkpnclnYKUJlK1Lx_5M9TaGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/938fb471c4.mp4?token=sy6JQ3WXzlrPyKS1-1UPzCF4giQp7AqfJHuKkKrm4i3QueZR5ap9abP386PpBrraVoF9D-hH5eTuR_TqpEg84Q9ILoid42aFkPmN918MZS-SXJT7VtPaGEN4otWpIMbw1W5HFa3B5du7lsoHWlyHAa5A0VbMQjX1A2YI7h6tqJofc3PtYdsuXKC-j4Z9H2EIL1HNK6kHNavFwOxR_blf8gntH1UhNmjDSk3X2xckshCo-3nZXxXQ8XU4IIp05DZzu0XasfdjXIHGC8CU_WHp_MxIZ7sHTW9j14JLIFmaga_oF_M6Td38BYhfRfenR0D6jC_dhAzyNb62HJamc8s4qjP4L9sfYTfVWTA0OQtf1SRfPor-TRYhP30fQzvCIfNiETGRwAVB038aMe0FfZH-xIw_SFoDoWjBmzE0-xWhzeEG2XCFdWD6Qjpk8KxUS-2NcEQ1UtiABouK_YoXo4TZ0bcSVarj-fYUpkC72CS98VsWGYUQdHweRg9o3g1tVpbE1RLi5VgohA7lBb1Egr0Xi_ehA8xVApCsohy-yB_-kVJLK4mz51QTBx0rPyffuGMd5zaGGEAczBHTm5P4V7s95FEVPta2CYBJXLT6fUYdADcCubC6bWXUkejyMQNyrqkrfs2M1Rhrb2Zawbs78u2ZkpnclnYKUJlK1Lx_5M9TaGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول انگلیس به کرواسی توسط کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94023" target="_blank">📅 23:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94022">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">هری کین بالاخره گل کرد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94022" target="_blank">📅 23:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94021">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تکراااار داد داور
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/94021" target="_blank">📅 23:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94020">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">هری کین با قدرت شروع کرد به ریددنننننن</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/94020" target="_blank">📅 23:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94019">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خرااااب کردددددد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/94019" target="_blank">📅 23:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94018">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خطا از مودریچچچچچچ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/94018" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94016">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">برا انگلیسسسس</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94016" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94015">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پنالتییییی</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94015" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94014">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بریم واسه شروع بازی انگلیس و کرواسی</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94014" target="_blank">📅 23:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94013">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jm_ZpzBa7_m7AeBmGNkROGCzi2esBmdIVUJtmIBM1oPga2D72q8yfYXkXyMeEhNsFj9ks2RH6frgX4AVM--23lF5Pqux8h4vZ1jvofUhJkj2n2bFx5wWCUs6YYakKJdQQ9oPfc26JyRZlYQzpuZ-yhg5QDsI2ZhkHqnBWoXyHMcJ4yMjj18bC8kuNGam-WdL8sZFr0mAse7d2UqeAV9BDeOGsrJHmWVwT3TcLSNATJYybKRaqk-9fEYcI0vBMQ46IDXXFhQs3JzZ6-iT1GDJFKWuM8RuBtmQguNsRsXq73JAHwXGirkwQCXLqej3bIi81qSk6XHYIGMiorToMYgMXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوش و بش یورگن کلوپ و جردن هندرسون پیش از شروع بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/94013" target="_blank">📅 23:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94012">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAeAXfSLMG371tMkicusfLVF7-9Wp5364O53RruoJpN2LBWSLeUvWOYFKEXjtZxpcX6jD14dVToPc3iOP-N22ZJk1Y092vNxlsHO4xxez3m35DoeX_fnbPQ7Bajl7B9Qn8vlAmT44gMrQ_vBswuPUSgSMfV6DMdrFlXeCLwaoZFt_vLDxoJddOZTeF27sQrvoA1aTxzS9UA7AH7Kr6NfyNxx6Vu1uBdwpLlq15fSSiW3-hb0UpxAmXRGIDmz041B688BXgb5E-jn8qC8EXQVcwcDfw1wTADPlPwUh6kkrXF16jxjIZSTtEQvSdeUsn8p_qtOXf1jN-iKSJCekZhlng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نوس، بهترین بازیکن دیدار پرتغال و کنگو شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94012" target="_blank">📅 23:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94008">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UtllcBvxNjtvxP0_H58pn8WuArqo7cby7RwfTsXrcY6GAO3zmBgR-T2saZ6UJuOc2fg_KfPVov4fU2ibufGs4f7DECUnZcZcdiA8Pkts4l_oN6zbQ6gN5tM0UxBn5vpOA5vZP0xfXCfYKSAKiXNzmBfOdzA8A_E8_wBEwpPrxnxDYyTwZPMKWDT1O6rkhwuQyBCFVwMv3zEnSNvx5OOVWsAgm1T1mA5HGiPRRSj56tabsEQEWheYBIouKNtbbr8RI7eACdTvXVLnh2R4GrsOhKNXwXc89pPFzzQ-MQqy0qZi6m5Op5PN6PSrziywxuKU0kI-IgL8A_RukwL1EIEaAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hMpwO99-fp0P957ajpP0vCb_p2sFNNIHg7qiinuAFytgXPFMhWEVHDnDaquhERD_Xr9tQrb9fyYNoDMpiRKtxq-eBemYnQWlE3CuwOuhB0OkkGbrfPUnVR9XsuTl5ongbhQHOfdp1wqA45wFblMJoaYHZddt_ZUgUHxReLeCfv3hskzqplf_kkMjHfFnjEY6m_pAJsP5p74YfHsos9xnpjQkr5lCu61nWBwYsQUIv-uArF0xUltfzEBY86apoPwQLfiY-nddrwkEwXIj6bugSToIo091g7XpUPO4neyjLpXc8I0v72lWg_lGBvvnnCHWC1vinKI8LTwEyNlrwqx5WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AbnTQFYohBljIS8yU85KtNmcU1RRaOYjDicxKsWZ4pm25iKcSElofnOdQ9_Hbhgfva0Bo_1zhIPLa8Vml2wFM4CrMFMY85ee2NjA9HQftHEK8m7IcPEDh69h9eICB5uJwNogdhlKZv4WFrNYltTuMr7g3z9XHMK44vyhIIhOSMTk-sFtWzI4AgPtwR072VEs6laNd16Z-rlbKJ-eAbTmTRpDOBaO6MwYELUim_xa4MhR1-aJfBh54rlWRprRIylg3K1J4PhhOwCUv94w9GkJ2xAHvdWvwcCcVR_IBvfTD17_ePvhCwMjFmMzYHVMnHH584Y89r4nSfxjFnkv-lqGrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/unHn8508yR0cklA5kk_mr0j_ab1X-3sHC6-TayksN7tr3whOaynwTyxH8H4fiS7_cOena8iPIA2gFWFzWZaEhRFutVvVU-KP17TW-YmbdHVohj3n-WGNFPCaSbkqw2PeOvATEZwymbgOcxYoUlrbTJeehwUR_2tJh8TfdsG9f3ddZrlVPVslPtzXNoMHrVeNC7u_PoU_OIe8SacCml9oUc8s7_UfgW2vg6_9ydmyZogoLCodX2W1ncEHqtK6Gi_1BJjtL1xAR_Yk_IVy7mR5OX_-Z74XkttLAZE_A-g2Y5_6EtK13qyKNWs9_E-RNeAUVmuLyRqDg4mnLhDaNfj6Dw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
👀
دوباره این عشقتون سر و کلش پیدا شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94008" target="_blank">📅 23:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94007">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFPWA7fMiD02vGEVE3Gc_oUU30ZqIH7aIM5VX7hY4SGM_WrfElyNUOG5zBkhrrgQoA2UTFtcJe97BG8pC5SVh8pmozKDLr9U4XT4XfWVOkFipUEpF6KdfptnLt1IAW_M7u4hZVJPYx0Eruc_xjw9wTlhRox2vggdAliiBZsoMKhWPQpinvBVCojHUJWyCnq-iLMmbrCIyKKCt2462anw_W5QOKX7nm6WMbqMnRcZDI-tVfLd6b_bUB3gowyDpcjhMxxD1MynIrNKeWAgtIO4CLT6ZJsXF-B5s43lfPPdyxNzCSSbiK6fyZG7GRNMzLju0_tpE_Y1pWCvNGkyun31hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی داداش یامال واقعا کیوت‌ترین آدمیه که میشه دید
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/94007" target="_blank">📅 23:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94006">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjEW1C7wF_GtUx2j02cp1bbLVVOobMAjL53OaMWkakW3LLeUqec3XUvatwI8YFasxh63RmlSZX67AxfrPlFPH3YV4jM-Axi8QQRYdl0z-QDSw6v7XGHsJPUTlzVUvrRVFKZrxmRb3_FOVA5SkhjkIfY4Kd5h8_laDcy7sNM9xgeMO68o18DgMAzv7DwY2T0Sy_V7IGQA8VoFWBD8MlEtaDNpXpZw0QyhZ5Maqy1zFvPW2fAryriNWam6X2zebWxKhbAxzM3vqcVF6Dgc8_FZMpNrKGGye1gzQwjJaGY9KPoY1rVrvzC8gI-kGJIer4p8HsqDH8XrauuEx_qVp5s9Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
با توقف پرتغال مقابل کنگو،‌ رتبه ششم رنکینگ فیفا به مراکش رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/94006" target="_blank">📅 22:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94005">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNLSpGffeys0ycpul_MX0WzWEU5MHIa_3rPBdsQCB_lBJfTym0Pe_VDrIiJoRoamd7HMvZasTOsZcFY8k48XL4eVgYR77nTpn6OjXkDSdPa7ECU4iOkb2A4d72Q-NJTNZRYSPv2D76TrfVVBN5RvRJCTo9GObanaI-3-0AgnQPy1nX5DfKR8Ynhlib5OadF98vQRBIj0Y22qy7L2q8S_j9T65nR7uEvONUiTfzzrMSCmUXpGESwdu0kkvAUT3mUWg_-1dfV0yZ5FYQaY9A4ma_JEL2Wjt1jhW2NYd86RtEByFjrySMXxQ4eHNUoi_vn1zibBddYoieP9vzazuXyU_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
تنها ۴ تیم در تاریخ جام جهانی بودند که در بازی افتتاحیه متوقف شدند و سپس قهرمان شدند:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلستان ۱۹۶۶ (تساوی)
🇮🇹
ایتالیا ۱۹۸۲ (تساوی)
🇪🇸
اسپانیا ۲۰۱۰ (شکست)
🇦🇷
آرژانتین ۲۰۲۲ (شکست)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94005" target="_blank">📅 22:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94004">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
#
فووووری
و رسمی متن تفاهمنامه ایران و آمریکا منتشر شد:
— توقف فوری و دائمی خصومت‌ها بین ایالات متحده، ایران و متحدانشان در تمام جبهه‌ها، از جمله لبنان.
— هر دو طرف متعهد به احترام به حاکمیت، تمامیت ارضی و امور داخلی یکدیگر هستند.
— توافق جامع باید ظرف ۶۰ روز مذاکره شود، با امکان تمدید به توافق متقابل.
— ایالات متحده بلافاصله محدودیت‌های دریایی خود بر ایران را لغو خواهد کرد، در حالی که ایران به تدریج ترافیک دریایی را باز خواهد گرداند. نیروهای آمریکایی در نزدیکی ظرف ۳۰ روز پس از توافق نهایی عقب‌نشینی خواهند کرد.
— ایران تضمین خواهد کرد که ناوبری تجاری امن از طریق خلیج فارس و خلیج عمان انجام شود، با بازگردانی کامل ترافیک پس از عملیات پاکسازی مین.
— ایران و عمان درباره مدیریت آینده و چارچوب دریایی تنگه هرمز گفتگو خواهند کرد.
— ایالات متحده و شرکای منطقه‌ای ابتکار بازسازی اقتصادی و سرمایه‌گذاری برای ایران به ارزش حداقل ۳۰۰ میلیارد دلار را آغاز خواهند کرد.
— تمام تحریم‌ها علیه ایران، از جمله تحریم‌های ایالات متحده، سازمان ملل و آژانس بین‌المللی انرژی اتمی، طبق نقشه راه توافق شده برداشته خواهند شد.
— ایران مجدداً تأکید می‌کند که به دنبال سلاح هسته‌ای نخواهد بود. مسئله ذخایر اورانیوم غنی‌شده از طریق مکانیزمی که توسط هر دو طرف توافق شده، حل خواهد شد.
— تا رسیدن به توافق نهایی، ایران موضع هسته‌ای فعلی خود را حفظ خواهد کرد، در حالی که ایالات متحده از اعمال تحریم‌های جدید یا استقرار نیروهای اضافی خودداری خواهد کرد.
— صادرات نفت ایران همراه با خدمات بانکی، حمل و نقل و بیمه مرتبط، معافیت‌های تحریمی فوری دریافت خواهند کرد.
— دارایی‌های مسدود شده ایران به تدریج طبق رویه‌های توافق شده متقابل آزاد خواهند شد.
— یک نهاد نظارتی مشترک اجرای یادداشت تفاهم و هر توافق آینده را نظارت خواهد کرد.
انتظار می‌رود توافق نهایی از طریق قطعنامه شورای امنیت سازمان ملل رسمی شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94004" target="_blank">📅 22:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94003">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnFCqBP_ZKif1zBQpb8GhpoHJUd8h3qKLbMaYNxEeRRpKgQqdPB_g6sU10cu6jYcczJsOP3dFAT5yhYwVaPMY3x93GKtH4uWi6ZX9Qz_aT1Ei6r8JLSb7jJcArcQDYZbg_FJdhhLd3vZm364pBo9yeEFRyssaosKOkswAd_m1nqsGr9_WUHZK3W7FlcnfINgIfKl3SCf9xGFEZd9ipR17SKLpGB2CuRMNEfJ-skulmd6N9LCDkzLW-pbgsaqp417R7c0KHbWiI3erj7tcb2_ZtsOfQdr05X3LjXnMASE7cIWfE8hZst_raDXAX3kmleifFo9NgRacpCq8sJCH89bqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇵🇹
📊
عملکرد فاجعه‌ رونالدو در ده بازی اخیر مسابقات مهم و حساس پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94003" target="_blank">📅 22:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94002">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEc2DH3ko34aWTfaM2BDwvjYJ5wqE0mB2nr_ct0zDQMuYNXl7xrL54aiJdtjgeitH2YAVWHHjL4ZS6QBTarrzahttcc2GUvP3qY5O5UhkNJV4qLWbPTNKI62H_sVBWCAz0gavYTPGBTJzsKTVnpJYZ42Bf-saB2sSGuKm7HFfmz-CCUn6eYa7Z9jxdJULD5EpbuHX-BtZJeTEao0kRfJ5_i12LJmLd25m4S0Fx3D1mQ4qjF4v-8c2oac2kih-HdjqffrDX7DfUbWcX7YPU2_q8QGrJUwfNWcNQ6kNdizah-YOBHzLD0OTTIeTnc5BrP3US4WwbQWThd6pT5L3B_Lhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
عملکرد کریستیانو رونالدو مقابل کنگو:
⚽️
0 گل
🎯
0 پاس گل
🥅
0 شوت در چارچوب
🕺
0 دریبل موفق
🔑
0 پاس کلیدی
👟
25 لمس توپ
✅
19 پاس صحیح از 21 پاس (90٪)
⚔️
0 نبرد زمینی
💪
2 نبرد هوایی موفق از 3 تلاش
❌
3 بار از دست دادن مالکیت توپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/94002" target="_blank">📅 22:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94001">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQcAp2DlRdD0hkUDmYBUdrs1MaiQSCIGsRaa7F_ziFGWE-sKXSyTq8hqn0BMoaCJ3Fcjn1tNn6HjFNXbFBu7PAER_2qLLwD3eZ56haNDuqQiNkMX7RmDSlQXgIiWWfzAU1p5GbKGt1auGkgW26M3s54KO8v8DsPLsFwllzxYBVhydDQWl5p8zrAblHf56XNueRRqh5EDjYOwLJDPZvdgpPQMF5YkoNzybXWCkj83XxhaUWbCS-qJq7x3h37aKxAkT9Elh_hUln0anU50Tfo9aJ1Tj5UzB5VOFBIo0yJrgwMhCmmivYTQ7i6NvtZwjY1k9DncwQiuj9h9Upy2FbJ5eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
❌
پرتغال برای اولین بار از جام جهانی ۲۰۱۸، نتونست بازی افتتاحیه خودش در جام جهانی رو با برد پشت سر بذاره. آخرین بار این اتفاق در تساوی ۳-۳ مقابل اسپانیا در جام جهانی ۲۰۱۸ رخ داده بود.
🤝
😀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/94001" target="_blank">📅 22:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94000">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckqZ6-QM81LPJQ2Efrz9XsELK3k5JVcaiGz9ru1avMtTs5rz4e5xIpF2x9vL9p19o9Xl9UR3hgKnP9S0ZvuIKaHvWBvCO8ODUaor5M09Msn6Jlw_M6fwK-W7aGC7p_H8PpepoLCjIsNU4OVqXEdXpKiCQKoBKIBsIEUbUKq5KZQjg9PTxR6jjylMQIRVU5grqujxAdbrhfZyH4bfujTKEwrnuzpQBvHFAU5EGokVc53qfDjL02GkP28DwqAwfnVSPaYXU4qFqsBhYozmd29lS5Ji472_WcnSG6G4kdck9Fr-HDfwMdrE1u4ACFZy1j-2_GiP-DNmw3EUXkf_R1X_Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🚨
نمرات بازیکنان پرتغال مقابل کنگو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/94000" target="_blank">📅 22:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93999">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAuZMpEQJEYQJeCs690u0hbuFKfK4Bja64H2E6ngtGbsylx7XdnVC83phBXboofWzw_GoRG4eHnuTjTu9tWNnVtCEQAfrUZKyFpKwfnSkkay6KkmUwUTRXeqS_lonz1LWXOWWmsQCB7VQ6adipQPSzzJ06raTuC87Z8YFk-qv5iIPmLK9Vl2lLsdZrhGCm2_6CnxoPCM_0W7Khhb0ggL15GB0xY8DjCx_td7wR22rVpWmnHMMuVckl0ja_kv9kPD6V_lwiHSHZM2X9bV75hZ1_GnLcMagoOM9Pv7ia71cJp8B-ENZYEePgR2IxMXkZWEy5HVR3KjHpEWTTlhzwbZRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇨🇩
آمار نهایی بازی پرتغال و کنگو.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/93999" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93998">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6aoZIsfwqWj0-hecjeQR-EfmevnvmH8bJSht08sjLvjgXQ_rGPS73wh-clGPCdzOt4-sK6zH8hgr14UO1-TAbNvUWnV7R4xyHCSAQIrz-xAYMhl9StOW4pT3bEETctwt64FKnRsvbLDS_-K4Z3Yb3Lw02K8vqFv-xFxBv9VpA1zTLmDJqvMJzPM3DArEMR7fIiga3NHg5p96GU3zC9TFypybysK6UGpmpTOFSofBsG05QbkrjYZlACpLWCwRSmuxaMiniB5ZUl1qfDdJeNkFWv42thX-Mq-KccL2imIjG9K02eNDDAymdnu8Zn8-gYjrGkqXSx2e3UYVrNbAfzcgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|تقسیم امتیازات در جدال پرتغال و کنگو؛ رونالدو و یارانش متوقف شدند.
🇵🇹
پرتغال
😃
-
😃
کنگو
🇨🇩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/93998" target="_blank">📅 22:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93997">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">۵ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/93997" target="_blank">📅 22:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93996">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پرتغال ضعیف ترین مدعی بوده تا اینجا</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/93996" target="_blank">📅 22:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93994">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hE1uxbVlju48FxHM1PEwngoXxOZ6b4f5jFO_veEkxeXWb_rAM9MiykS7j592mcDP5StEcZNL-yZJahJBhuRB3sHVg0UVekscv9E5bte-sPAJvOc7MiiSfLwcuaOz5PeSVW4fEvipoLxBLyoYjV9AN-5l6VA6bEdIe7RXPhjPWKw9InjBJWemhteREHp1CZuYRng3_9a7XnXVEa1xm-IJIE5PUE52GJ_nU83_r1dmUht0sKXDPUGiJhK3m5G7P_VdVlODhjioBqd_nTzRGas91kmiWKN77taQER0XeN8M2oQmkBZN3ArLrFoCUlICy4W00nmlhqGY9XQKiUFvuHbRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BquqVOcs6hGSFup6-hjRTULNNPEAXZgbdIDBKFG2yckfJls8MIzn33jO7eE1NuZlrOL1ieCQRAgNGAIWd4dlNF1kCtv2L9JOzwdl9NkZ2H6hfUbDUG5_cHnuOnOUFjTdGhykWzbr1BtzCL7N10lJ3gd09_A9tbR6DcJ0KEZGRxFywuzp6YmwlbKgYGEgWZBe1jDp-KWV2huR8YBlnHWZQ7kwF5_bqjww4H6L91kIz9uxhRFf_OIB5ErC6Ql5QUWADP1WK0X5EwORrQIRRrwG1l15YCK21dqA3uV9yXw2UJ1JBitSuN25VEHSP_N1-OWnfgW7vAlvokmI5ugFomdIdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇭🇷
ترکیب رسمی کرواسی
⚽️
انگلیس
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/93994" target="_blank">📅 22:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93993">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcFOpP40v41qgNXAgjpPxx83E7jHosuG4kxMrjEqAgKQ4jHa-PlHVcriE3mJt7xU5KJveaUpTcITJHE0kTtQTdYFjc5FuH1VlWBCrCGmrNQO8Yr4UhpwG3vAG0U4Z7tgXv_6-rFY2Jh8fX1rBj4Wxz1JWrRqwCbAhqCLtaB9kN2Ft87cYDL-UMUVxqQG3-hOurql-7DUQqdfooEALwh73K7nuaGK3iG4N6yDYCN-CNcHz6yZEprB8MwytU2_VkUMQ2LZXRl8j9tvC_Mm9_v2Qm0-hf0lXkM-xipqB5S8HMahiCUOgl-tMl4-NK6x449x_MyJwk-wBHVXr2G3tVF9MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو این توپ رو گل نکرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/93993" target="_blank">📅 22:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93992">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وااااااای کریس داشت میزدددد</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/93992" target="_blank">📅 22:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93991">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گلللل دوم پرتغال اما افساید</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/93991" target="_blank">📅 21:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93990">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سیلوا با کونسیسائو تعویض شد</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/93990" target="_blank">📅 21:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93989">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بریم واسه شروع نیمه دوم</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/93989" target="_blank">📅 21:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93988">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mkslZm-Sz5LEBVLmPp9AUAfkbRBIipUQersWOYYIMnqjQKPgs8_3iaTssoFj-aefBr3qfK3H0e03YmHAPXycQiMa8ipJq2lEbXXfYxsZR_OYc3QHSVKfvrvdZaQ9cG_I3Y7YDMMeKdMTjzC-1Q6ccVBzlZfzlyN_SXBT_OQwh2-OK8N9jjMkLq93Urt_LCFycyTCNGms83FV5YpJtisr880pafFrqPXeR9Huaf86ICmlEVDBNoJNDHREzkcLR7wxLJd0vB6_QmvCuPGO2g74jaBQbxWf4nCLkMgjQvmXfuyjBXS9x8QkCQBqufQQ-L8eFduKSfGSQNMV2ZZToKKszw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
وضعیت آمار بازی تو نیمه اول:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/93988" target="_blank">📅 21:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93987">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPHyljT0eDh4JftAicDB_hog-XI1n4ngdIBqkYpgb2YneOwGQ9DWOmsWHmeSZGNTIk39DIhsl5IQ0MFMFrp0XNALtHNYU99oJkQVXSrYNFAnR_OMmxr_BIVKwoD984MhAqk1lErKlxxKFUz9Ll-3d05K5D0pBqTVed7zDLaR9nO-kjX_w9s25Aum66Nmdi1Od8vYCeD7IFMrNJPFh0NywTdNw0Y7C8EYTxKyTmB3Syr8mcFhISiOSi1IR7HgFZnOKP5Pnv_0p7CQNkrDt71ACi_hBJioeavaIVBeniyXmu13CdT_qYCrr-lpt_l1TiT13Z66bkRmtxlo9MolhrvcBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی به قیافه من میخوره پرتغال رو قهرمان جام‌جهانی کنم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/93987" target="_blank">📅 21:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93983">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1K5VL2rALuBJlTvP5i1aA1la6ATNSQmcJ-6tnGYG9e9-m9z-w92P8aoKUGztLrE-jl_2fo95qTyCnSyOISZO8dkLdVSfPg6yIOPyrc5yyDnr4o7rIQlxqb7-VErIbX4Zlf-iM3BHJbvTEB0a9_5OLgNpXdt6MCZd7HhaiSVI-sq7ERI2wlXr8myB-wVfl4EtS8Gk0B1K-8wNFDf_AEneQaUoTitZARmtzNMrInSQ_3LCC4vhrSr_Zg5rtwzq6f9RilqUVoTjoCXJTyv1eakjpD0EyfFIc-Kbg_JITp2fjHFEa8ySwVAYgcfZA0emb5rnpTsAEMGk2WsLxqKMjJywQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R6K2Cog3nUzPQSAjMC_IiW4KKIiIWZWlTaitm5l53JE7E4kKl-7o3dGvgzEfPCs6mpcWPwt-kue8xbE74dwLYP0mMfisKBZNqeDWHCgPrkdhMKLIOO0ULrNyxWBIQsxmpGWtiQlNd2ImDSwV6whSf7DCUBWlUfZvdMy7WHRFoAAtyj7KtG5cfB74llHIS-7HQJmrU7hX598v6Q-Fd6cVDSYMkkSqTXo9SK3o1HiOMOgj9SZdUFBKf-67AcchHKyru7_sSdSVSjGE4pMV6OIHPktLVNeXqsmaQrkcOxKSpZbjGp2ngKMrBmiNrLt8qzwCV2-0vi6qJfMH78ZesAttug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uswXIckOBsoJRsbDXW7gEy6htEpQ0vYFrfPWaQKCjIdXnNkWxPTW3ruCVcvIJBWGEc9qLMlvEuFo3vS_RtwXwmcvQl1dpmpTeMpcLzZrvhHRX2U651P2fHaqYcxiumBk2JPLygOMF8Ecvu0uedYP0MdXjXRC7gz4LBm3PKEgU51kI2g86jgN7J3hGQ36C_73RB_twBs__ILbxP88tQW_svLOGW5FyyNsxzsyvkFuAqF2jHrEWia3g8zdLfg4JGOveMz-LodziMswrlh_aeRlTGUypZZFsxckAzCQ0umdAlFY0FmuTz1KIHdH9S1QmTUuP1Of5UqNSTURpJj9CucLaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rYndzJH792wy9zZ7snMpqsH2_ypdIu81eufkBOBauNMjJOyuLIGLpzuVN3dqJ8ZcQS9Qs_Y3amUlo3xmjL8ZnlBO8ILKU7SwQLyUa73jCAerspLt_PRAr1FnYxlmZE8r6aYUFHdlT9XBuXJ8AtyM0M7P116ZzS30sudZULpQ2_LG3qWkVfGf3i6sgZ9RgGWovCr27Jx27LTQf4ogTCUBZIx-4sJk0_Lxuk1yjp23yR3-LLnHoEdfC9RPPWUv7w6yOdeoRlHw2cHNapylIXQSG5wixsCBCZgaSmAH0BxbwzWfXR6Wgad6marVT4dM3E6u7GvjQidbsD0prRlGdVDREQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Vamos Portugal
🇵🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/93983" target="_blank">📅 21:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93982">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پایان نیمه اول بازی
🇵🇹
پرتغال 1 _ 1
🇨🇩
کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/93982" target="_blank">📅 21:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93981">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇨🇩
گل مساوی کنگو به پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/93981" target="_blank">📅 21:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93980">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مارتینز پدرسگ این چه سبکیه</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/93980" target="_blank">📅 21:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93978">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پشمام کنگو گل مساوی رو زد
😐
😂</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/93978" target="_blank">📅 21:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93977">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFZ_sNVGx9SoBlUES9DYFLG7lqAaqtb7OrcekCGvmLfE_B6DOKaAmYfHEriz3rSumLK17y0WEf3VWSwnbhoGCpqFXOcLMhLtr24vkH-ujfeVkfxjrCPqs6F3rjdy1RkUpHGvF86OYfnZqJH3rmciRp9yAo7sivQSGAqwSe_9ib5fsYddP0x4eTAjjnZdhJ4NSMQ8mcSe_pHZFMJEHBOxAqNht9HDvjWr0OWMTfDJRVXNlELGf1McfCyMAbRE6QnIpf5ijMJG_IGYlQs0IlzrJtj17pv93DUDL4Wj3SG6ESbYY1ArjmTMKoizAUVwhZemGzr88EQSrzJNxtzGx7_B2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر و مادر ژوتا تو استادیوم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/93977" target="_blank">📅 21:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93976">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3nkmlrgvVadNiFhbRmfYhKwmPpH-_jWEuqZaQMxIkYq5XJoE8Kh6AqIBu03XxXryW62g6co7CgcFfSZpHVeGf4El2ga0DwfT7eBZw2ra9gvfyJb1HdrKoQk7mflPMx2D1QGfsFvTDdnFGunoicKEfKYK20DcybHifhxNuO1wiGYQ9xoJIGzRc07zK6ucmA0AG15u_ydM6azTzjpmS51EuRycd839V2CFOGx1sxlvsAblMDwZLj1FA1HHBHXpEIex83Mp2bxQVd6Xoc3vv1cqpX7PxnWnvn4XkZL7da9ec4qeXAabUMCJk7-88iCjfzW3g8iII9r7DbYSyqbQ24bRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
فوری از آرشیوو وار:
تکل برناردو سیلوا قرمز مستقیم نداشت چون این حرکت به عنوان بازی خشن در نظر گرفته نمیشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/93976" target="_blank">📅 21:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93975">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/St5d9ut3yW3Qk6A41U8wEujmJvNZ2qmvRhJzov0WASQ0pVOe73-49nz-NQA8GYlHGALR8wAxm2lWw92qLGEa-LFhnGEU8diGBmqPzMI98fc_JTTFPNkglS5EDSdj2MIpUf1xmi7IJf5blxaj34pcvHj9kecsiAZtQJSLCaE8adL9DXqgNXcV1QGYA-tcuqw8FMwKgPQbH0Srab0a9f17AQHU0nEHwcKxP-5PCqV6tDOCNlea2qKYItJOrVB7LA1NwIUJBrmUcUd_s26cr0ajF7JTvcyyOsAM27tLFGJzZM9kk78TH6z-W0NU5Kc3T5UFUHvmW1jp6fcMQUqoamMKNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتغال عزیز امشب زیر ۴ تا نمیزنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/93975" target="_blank">📅 20:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93974">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">کارت زرد برای برناردو</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/93974" target="_blank">📅 20:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93973">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d7a7ea661d.mp4?token=h1vd58eKhHzo3dYXdVHTcp5jQHGCXujXExgKWktyIGYJ4De4-A1-0KWkQDRmmcTjOzN65tD8hMQzEjBWkLDuMVY9xXQVs0ZPr6fLysgkRpvJzvPrGzHIiRi4iLljlzuzirpLzimG4gOsKHPRWILt41aN-GHmrFJTBs4Txh82AokDTZqh1qjYxx7Ju4jA4h1ThDJkwHlQm6Y7HueBmS7MltRFlaL2hc7WEavOyP2uSZ3wwaWbih3WxkeUPj8JnJS8VzJ0GE0wB995WYc05936djz4Wz6WjJ9xXDDXUF1tWe-RBlnJJF90Yzj6DLaWo3BJFuaLwKsX15nKh4mMMXw98g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d7a7ea661d.mp4?token=h1vd58eKhHzo3dYXdVHTcp5jQHGCXujXExgKWktyIGYJ4De4-A1-0KWkQDRmmcTjOzN65tD8hMQzEjBWkLDuMVY9xXQVs0ZPr6fLysgkRpvJzvPrGzHIiRi4iLljlzuzirpLzimG4gOsKHPRWILt41aN-GHmrFJTBs4Txh82AokDTZqh1qjYxx7Ju4jA4h1ThDJkwHlQm6Y7HueBmS7MltRFlaL2hc7WEavOyP2uSZ3wwaWbih3WxkeUPj8JnJS8VzJ0GE0wB995WYc05936djz4Wz6WjJ9xXDDXUF1tWe-RBlnJJF90Yzj6DLaWo3BJFuaLwKsX15nKh4mMMXw98g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
گل اول پرتغال به کنگو توسط نوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/93973" target="_blank">📅 20:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93972">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">شوووووت خطرناک بازیکن کنگوو</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/93972" target="_blank">📅 20:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93971">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پرتغال اولیییییو زد نوس</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/93971" target="_blank">📅 20:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93969">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گلللللللللللل</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/93969" target="_blank">📅 20:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93968">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uC9-8WG32QNLAxEqBNuRW_g3ciVUJjVgIOJ-JhOmdMtGVtXn0hAT-PhGXHgeM5_qECGbC9tmyHrNH8YjfOmZwi5OK-96-SCrkAB40-caYlGxG2zGAsAMugtHSZR7kHxoOK2nhdBY7I-Axt3Ahw99a8gFhl2rRb8mesY9BGTEOk6BizaJ5koBfh-FEC18QrEBwLBt5DT-75CHS9fTkbCwM4inDMd-mPAMFS2noKS1XwUZ-Nd7iLH-L7s3xNF4dakpk7_EhftotvWtzu2CI8tXFEVzvhP9YmXt8tCak5G86eMs-QMbXuQuIVuBwEp32c0H1HSLZdTB4XLTHYSe9GfFNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادبود ژوتا در ورزشگاه انجام شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/93968" target="_blank">📅 20:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93967">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کم کم بریم سراغ بازی کریس و رفقا
🔥</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/93967" target="_blank">📅 20:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93966">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8532e0a977.mp4?token=vCG9ALkpdOIMP6Cf35cW2laQSYJdho-k383fKbKncle5jbXYkU2dzomod1G9ccb84ACtsMYbZ03r6Dsewt6a3nIvD5Q0MylXIF8cY3md4-fT4XVCZskgnKDUBtbljCr70EamQn-mjla-UTolwMv0-3bAM5TZtI9inKc4eQEwGlfc7L0ql-9dWyulpGPubIbbkDPuNzMexrMCzn80zSs21FGbMpbmrxnEArwvgerp1w_cNACNBTrw3DyP7H3tQ_g6qL8gaHrpGjWrRAAfdjyjnAf6BpEzKwvIlHB_3gLIVCWag-ArXT5WD9Xia3K3eTSJAQ7S_LbpcSRlVI1q2jNGxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8532e0a977.mp4?token=vCG9ALkpdOIMP6Cf35cW2laQSYJdho-k383fKbKncle5jbXYkU2dzomod1G9ccb84ACtsMYbZ03r6Dsewt6a3nIvD5Q0MylXIF8cY3md4-fT4XVCZskgnKDUBtbljCr70EamQn-mjla-UTolwMv0-3bAM5TZtI9inKc4eQEwGlfc7L0ql-9dWyulpGPubIbbkDPuNzMexrMCzn80zSs21FGbMpbmrxnEArwvgerp1w_cNACNBTrw3DyP7H3tQ_g6qL8gaHrpGjWrRAAfdjyjnAf6BpEzKwvIlHB_3gLIVCWag-ArXT5WD9Xia3K3eTSJAQ7S_LbpcSRlVI1q2jNGxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇲🇽
🇳🇱
عیش و نوش مکزیکی‌ها با هواداران هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/93966" target="_blank">📅 20:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93965">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64954456c2.mp4?token=PAAAhDaUC6fGFzKGEJzr77gcf-sPbKdxmUuNa1tI59YqRDtACrHVPWPQD-UqBBnk64F2S1ph0djsFieYwumGaWvKMuwc1qMadpkyoo7abeb2X4l_eFNsnc75fkX_dbZilKdl2YKofK3Vy5STGNxtoDN6z0Fwf4a-Go_jG62Ob0Ngnw2ngUTsp9YwTSDXVlzbqXSKKyRnEaSI4nMlk0ZF2RJpWj70oyxFaxgW1TVNRODbDqUy5E54YaKdP-0Wy7bbr7c8SlNarVQWlyvQIfwi8n8PmVwUL6m-2fZNrNxLrxdTEpBjgKdNtPgBn78OJOAmG7YnHG0dDEOWZLpakF21NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64954456c2.mp4?token=PAAAhDaUC6fGFzKGEJzr77gcf-sPbKdxmUuNa1tI59YqRDtACrHVPWPQD-UqBBnk64F2S1ph0djsFieYwumGaWvKMuwc1qMadpkyoo7abeb2X4l_eFNsnc75fkX_dbZilKdl2YKofK3Vy5STGNxtoDN6z0Fwf4a-Go_jG62Ob0Ngnw2ngUTsp9YwTSDXVlzbqXSKKyRnEaSI4nMlk0ZF2RJpWj70oyxFaxgW1TVNRODbDqUy5E54YaKdP-0Wy7bbr7c8SlNarVQWlyvQIfwi8n8PmVwUL6m-2fZNrNxLrxdTEpBjgKdNtPgBn78OJOAmG7YnHG0dDEOWZLpakF21NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
😂
سوارز مناطق محروم در برنامه ابوطالب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/93965" target="_blank">📅 20:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93964">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggtDpojK6jgZK2s_oGzQof1pHGcYvjOLp65UuuyJVzN68thbwUqoa6BYcJfZg50mJjhyXTOW0gWiu0WQPx69Gy4HmTmDlQCziYLPkkgxwSlUcRixM-QJYcvcwa7tTNMIdL2m7Y8RelWtOM_48Ejb-5xUVSmX8TJAfYMXVSHDTDSaBiyjbsRmRg55yfRwnGh6lIz_rIiupSHFZX8fDc_C1zA86RDMWRnXI1HMPdsXa8_2aOf0YU8Dom-ZAqJv92EcEGal1nAb-r9JA9QUs-m0V8wAbTVNZMDF_FaoSIHOqvQ1fbV36L6EucNNERAU2uNshtIwqjND3vPmiu_Svhde5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تگ روی لباس رونالدو برای ششمین جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/93964" target="_blank">📅 20:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93963">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfyNFvPIpYb86ZFPH35as-yPp9cK45PV3GBDoXfcy18nXe6mzBgTmKuPcw-tiXjkltEBq6vPcsXYx16NL8IZQcBXbOLhIJ43kR-N91HbexCz5sCmW7609DSFIda0Pgzf5cSaJbwo1APwGGzaUz2PnRY8vhAax1FboNAVnc29gMN58aNTyPzni01rfakxiG4TwXHBIn1hn-DSUhbC56AZXmnOf5kExr16z7tdQT2pLQt9tqFyh_OZ1ieYMLMFgc_jhVsAtxTS7idjpF6_xbVjj6NvPHhPdaWKht0NlD_OVUAkG3ZvY3aqegpZDK7WffdY5wwRY2OwbHQj4sdeeKMfnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇩
🆚
🇵🇹
۲۷ خرداد
🗓️
۲۰:۳۰
⏰
پرتغال
🆚
کنگو
📌
نبرد تجربه و رویا در جام جهانی
؛
جایی که یکی از قدرت‌های سنتی فوتبال اروپا برای افتخاری دیگر به میدان می‌آید و تیمی تازه‌وارد به دنبال خلق یکی از بزرگ‌ترین شگفتی‌های تاریخ خود است.
⚽
🔥
پرتغال، یکی از مدعیان همیشگی فوتبال جهان که شاید آخرین جام جهانی کریستیانو رونالدو را تجربه می‌کند و با ستاره‌های پرشمار خود به دنبال تاریخ‌سازی و فتح جام است در مقابل کنگو، تیمی که برای نخستین بار حضور در جام جهانی را تجربه می‌کند و با انگیزه‌ای بی‌نظیر برای شگفتی‌سازی پا به این رقابت‌ها گذاشته است.
🚀
⚡️
آیا پرتغال می‌تواند با هدایت ستاره‌هایش مسیر تاریخ‌سازی را آغاز کند؟
یا کنگو در نخستین حضور خود، یکی از بزرگ‌ترین شگفتی‌های جام را رقم خواهد زد؟
👀
🏆
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/93963" target="_blank">📅 20:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93961">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lf_Q9jwhMgK2IRLoyiS_IVBx5bb5sx6_oaMc_ZMFH8Lyq0tJMcrgnfMxopVrbMYauZnTZqQT2vpsoZt2ENZ56Abit8YMN4ddqyt_Ce1AOEMBcToW7N_L059M7k_u5rxHjso3osyWkCZLRTlMKMMulm1ueBhtPs8QIsS_QcYFpr-Ox2bP7iBDrnKp-XJrO3_IBi4UUMUu6ZaO7pzvW4_u4njo7rymkQUBVNarWaVfPo_azzDtIOUziwwCblEyqFxauaItdudSpDaRlZnV9VEHMSQXcudlUs3-vkeUvfTbjTGM4x9D6ySp4j8YewRvLnruXzVSyt8qexQQgzYswyrFEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇨🇩
این وسط یکی هم پیدا شده و 292 هزار دلار روی نبردن پرتغال مقابل کنگو بسته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/93961" target="_blank">📅 20:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93960">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
ادعای معاون وزیر ارتباطات:
اینترنت دیگر مثل قبل در شرایط بحران قطع نخواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/93960" target="_blank">📅 20:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93959">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q84D7TtggbgKgFmctn9BAU8L1HafrTkCvzeZnI-OLJzqoZnRXO-KhlH3wHRoxZc6M6SKg7EI0oNWw93pLVIvbkhV1RnO6ptvQPLKE_uBsvTpzR2p9885tMnNauNgrhh66zEFmIgdKPCLAQ7Rd9D3MlzYQnvnCe5dQFC8nOWuYZZIhREE9K5ccIQ8X4_EThCi6PEgT8iyiBDdG9CvtykZgh9mjcP5skwPFUEEafYfOvfIqSSv_mPQD-GLXm2_Xw-CO02kSwBojOK_4V6uS2uYOXtBC1lzKveWrJw44Qc53W6ZP6FL9gultWOKaFz7DPZCzrFDkTzZtFkdA5DLrV4vYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار : خیلیا معتقدن تو بهترین مهاجم دنیایی نظرت چیه ؟
هالند : من جزو بهترینای دنیا هستم ولی امباپه و کین از من بهترن و این فصل بیشتر از من گل زدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/93959" target="_blank">📅 19:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93958">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQ4wbMOZGWYmkQ3P3mFsUROC-DX6PyIpLBvJSp0APmUS6nHrc34JA--5fuDJRRj3PkjOeymfQBarXRbwPWmYR07X44tA5YcyqDTQ3TFOsOpHdZLYpt5wGrl-J6c6tawtnTK6gQcpNERwV1VBbYU_Apl3IiD9-ikjgmGT3FC_9l7AdixFREWANEKZacooNG9fztzhDLgCqoLFFINMCE7wlgCTFpQ38St2PEuc_qP3Pwh-NbusgY00ahmbQqZQxgVLnfysiCSMWCSPBqANeHbioPLRcmh3ShSrTOijaGALu2fEu9oAkrI5kwm-6d8Wh0IbPNPG7G-yE91ZW76yoaOKjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
رکوردهایی که کریستیانو رونالدو میتونه مقابل کنگو بشکنه:
✅
در صورت گلزنی، اولین بازیکن تاریخ جام جهانی میشه که در ۶ دوره مختلف گل زده.
✅
الان ۸ گل در جام جهانی داره و فقط ۱ گل تا رسیدن به رکورد اوزه‌بیو (۹ گل) به‌عنوان بهترین گلزن پرتغال در جام جهانی فاصله داره.
✅
با ۲ گل، به تنهایی صدرنشین بهترین گلزنان تاریخ پرتغال در جام جهانی میشه.
✅
ششمین حضورش در جام جهانی رو ثبت می‌کنه؛ یک رکورد تاریخی و انحصاری.
✅
در صورت گلزنی، اولین بازیکن تاریخ میشه که در ۶ دوره متوالی (۲۰۰۶ تا ۲۰۲۲) در جام جهانی گل زده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/93958" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93957">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/93957" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/93957" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93956">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoO3suMcvi91nBrlRDGHlj8SIzzxGihGAntNzq2OvpLdYXJMfMw4glW9wMQLifpSSvvY093N47UNiJ7hx5nc4Z_jBc9ROHhG3vr5AdVu-HluDX0PEhXhwL57cAxLFv0M8V549Xj4pknMvAKl9movq3lLMWeB2_L8LhAUx6wouMhlhoAHCNfQkoOV5eLnUL0RXUDlIQnI3kwc_EXV8zxirB24rpnAM-Yf4y3ArmKXPJCxM1zTcLYLo_5I2hbul8fbIbPgO29tvDz3IXU-XV4ZYxTkB-0Hm0gJ0yMh2iqT-5rHyleXaBoxp51dNviI0UC0fBGTJmz9twDFlkh2ZZwYmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/93956" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93955">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lv5H2blIh6UzP55T1gFRpoMMH-es51XHh2Br2th1e5e3FBtdpC_os9TMyK3t8OZAQqaNi-Gzl_hacRzrtO_ecU4amFX-GMNLCKgzHy1On-yX4_cJiLAELze5LTcMTfqfG2agfoC7PlIULWDx0QQGQgF-I8B5XWA1Ln3tjFboowY1I_xsQoS9CyXT2kiDJST7ur9yjJcttRMEVlc8FsmfFQWaF5_lxhSYnZJqfMqwInwykj8RoXuHU2eYD_WrgjkYW_fuC5nWQoE_ExigWdAkn_fqPHRB86GtknI8f_MQHAofeHj4pBvT84MPhBLJFh1W6Rp8ax0D0ehICm6Z5K02ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کریستیانو رونالدو پس از لیونل مسی دومین بازیکنی میشود که در 6 دوره مختلف در تاریخ جام جهانی شرکت میکند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/93955" target="_blank">📅 19:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93954">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G37HdKffdw1TuadNB0yF_WL2upvigI5I3WJsyKn10swqOMuNGDNPqigQc-95aJbSQfRTDHp7kyo_RGmePoHTJCWgMKFnRjMO0OHNSDlrGuhIApMJSsiBXRGHtjucOMYrdAIrvAN_ezqlJETRymVNjWJVLMXmxmDrjO9WRMKHMmurPeI4C3vXZLEZQ7m3PwRx_gszVHn8cPurptV-SA1oQiF1a4xQlDe0u8uQ4vrdVdd-XGa4dnNvF4BPo2IZ7qHYsRJPMeHtqKpqDNTdawiyfwjV74PQ2z-ygzxK2f82mNbdgI-d1XlWoj9cW0C4uX8tNW7VTdx_nsMNgmgBM2zlNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو ببین پسر
🔥
😬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/93954" target="_blank">📅 19:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93953">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baXnMa5mA9_DDXzh4STnJBuHzzIg1uZ7fIqEPStJSUTvv7xSpRKtUDR4hIP0tO4S5KPTvfYWaOvt5O0TzguLJ7NNoWvprT_Aee9iKyGfMktQIWB6BZvBcxQK_HJ9kLKG-AggM3wRg72v6tam01QELqpHNfqLSOIYDThbx7_11_Eel4bO74mj_kXi_htSt1ndA8_Thnv9cxAPHv5MFJ6Y7X_qrRerAjPU_bzUZgdK-H3icwscnCQFc0mGP5w-h6-hQuazLz9y8IlFNm2loc0kzjNqDgQUCsywCpLYmA_diTk_mQyBRaRiDAbr9WZHUZkrQg3mJDe0jctjUCJgHXirvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ترکیب رسمی پرتغال مقابل کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/93953" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93952">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibnlhqvsvBfBikO93h8H1rpe0fRPvNFbHHvhlD4ao4Xr6lSWAuB52TWJrqN6e6J13y3AclT8_a2powQ7-wN6WC-v4C1eJG33ypkJiGkh8p3kkt5w2Zf7KUmGHlACGq2fb-BGbBxl73DkhrhUCdvO-YCBaiJVp_olZpMCKEIw71KOKY6IfpzoFmbsbvRIlkJJTDQttPgwVaVV5-1i2V0NEm4KZerd5lK9TiHrEjpfJCijNquRIarGPjAO6VypLlxDNEnOcKgI0W53dSh2zofXFlqBHu1n3d_KmIdqe7tbaeJnOROImXWASwZ_RurkoLXv26vwKtpDiZPi5Ycum1AVqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها راهی که امباپه برای بردن لیگ قهرمانان اروپا داره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/93952" target="_blank">📅 19:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93950">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RuRd12mOJVZsvayTJvuMARMmNlgZtwBARdrTdY_BhJmsWN8PU5CEp_wQ8UmQImBYWWGppX4UIptjXiQSZVcGxgN6f2Pv146pEPmAAD2z3Wu7G2MZ7hLGjW53y34yWGEzI8tD6v-IxWaJXPUlwS06qMOhtVlrtuw2g38qcdXYccLBUJ-7KvhVgMDXSzBuhEM-OuUs9U-GID72ZvozMmyoA24h0M-HAAx6rJsbnEEZQ_xNybFC8T2T7w_97WGiUN1iEXlqnnqACKdtOci22_4KhFasEQUtG3JXSWtoWsLwz8UbM1ptGWkPfTXziQV4FXXUUep3irnHS8BeiK11A_bCJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ترکیب رسمی پرتغال مقابل کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/93950" target="_blank">📅 19:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93949">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXCDIIN04uqCoOOmys1bHaq2LKa68eKiFMDbnrrZMhr7I5PBZbOmKl3UVdvC1qHAuu3hz-MleHTJ35Jm0dIf0GbhjhvhxbazjzQ5DQdmz_pQb1_KP7hOkBa6qQUR1Xq6QTfP9XEWJ4rvrBhwl9d6z8_01HrGyXeYUOsmSyP4rD9plvlTioW4yY7GD8jIbqQ1a8ojLAF3dyq2zW5zePK1LPakjsd3Lk09Te2x96LRAd3s9qPIcY7jT6Hgbzvhy4cCdBIHYwV1_WKOFQvJ9_qUNHgRRxpyvI804cbupTw606bw_IHfnmXvQcZPsvoy3Q7P_ES8B749C29HqmJM2DVLFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
وقتی خدا یک شبه برات جبران میکنه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/93949" target="_blank">📅 19:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93948">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caYc81HfAddK4OV1W-tf068qAmy6CHo87jSmV0EojYr9syiZUGOqwLbna2V4DerWPGWbEBB4E_QiNxV5c3R97WY0QS-ir8GRPWhA-qFVo4e4gWYiZ-jVcXw8r3a925i0d7OvCwEbgAJ6zk33pIZecwPIwfRRdphcX-TVHisgD85cCEpywKhbjBL9FGW_kSUWC1iHL6WX-qNA5AbdV6N1tHuy-nyDJFMaj6VMaqI0jTim_JiVXEbrv1ieWz1wPMs1ia_P6gJMUgpD1A13nqYMc0IDyYKEmpOJOwIKoNs18E2OQP_QzI6LnciDrkod-X-Z8OrRlKinOp9ghtfkQzEmAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو به ورزشگاه رسید
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/93948" target="_blank">📅 19:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93947">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ece8d3dd0.mp4?token=tbqTEZDxyUaBBUa6B9RwrS4EaAPufBQ213VIbNwwpmKk3c4hI9H-6D8KXE4B0YejPBCJhfBSbOGZbuBKRCTqk6dGphboBNyHssbbNC8cLSP9FTHTn_k4JsIFEH5_-5usOBgZB7TCFzfwuoWYKVQoiUsrX3wyFlbZ2HvZyBk2rvDfekInB_5kpNj-cBOCxflDDFWZEhgbAeonjf-D_kwigvNcGY4KAzRbwBq8zd5Ovoz33jWsXKBPAhOD6r2LXaoPzbHkHGmtUwZe67ERsM0Lx7WCoy0azBGkeWZOAdH-L2drtRhpeZjD3I-fFZ1FD85tN_yjwKLbvm3ri0bhrkSPm3QSrmeX4WfLKYmD3mWxxhs4Q_Us7vDHw54pmimMET3Nk4t8HW2b7O-uS-mZ8cU4t3nf_qc9s03fCTXJIdJc3r_Oi9KVkH5njbEgQQrviH4nyw-hgcpjoZOKcI5pUtEGmr-kPdH9wjvGb1DlNPy95lbWw48hDJ1O1JBzBj1NsDq14QsCZstEdDcUteGW5Tag9RXeVuRonuS-ftFGmAXq2w6jU6yNpN_j8yyqU3M9Fi454dZCE5JFLZ9D94DFAEkmxUVxS1IsvRWJzbVQVfz2S0hvNus0tTcxkRxO_IA36nSnFPbV7AfohJxyadTFnfV3e-vZoAOdhO3ZkoFSWQX8gjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ece8d3dd0.mp4?token=tbqTEZDxyUaBBUa6B9RwrS4EaAPufBQ213VIbNwwpmKk3c4hI9H-6D8KXE4B0YejPBCJhfBSbOGZbuBKRCTqk6dGphboBNyHssbbNC8cLSP9FTHTn_k4JsIFEH5_-5usOBgZB7TCFzfwuoWYKVQoiUsrX3wyFlbZ2HvZyBk2rvDfekInB_5kpNj-cBOCxflDDFWZEhgbAeonjf-D_kwigvNcGY4KAzRbwBq8zd5Ovoz33jWsXKBPAhOD6r2LXaoPzbHkHGmtUwZe67ERsM0Lx7WCoy0azBGkeWZOAdH-L2drtRhpeZjD3I-fFZ1FD85tN_yjwKLbvm3ri0bhrkSPm3QSrmeX4WfLKYmD3mWxxhs4Q_Us7vDHw54pmimMET3Nk4t8HW2b7O-uS-mZ8cU4t3nf_qc9s03fCTXJIdJc3r_Oi9KVkH5njbEgQQrviH4nyw-hgcpjoZOKcI5pUtEGmr-kPdH9wjvGb1DlNPy95lbWw48hDJ1O1JBzBj1NsDq14QsCZstEdDcUteGW5Tag9RXeVuRonuS-ftFGmAXq2w6jU6yNpN_j8yyqU3M9Fi454dZCE5JFLZ9D94DFAEkmxUVxS1IsvRWJzbVQVfz2S0hvNus0tTcxkRxO_IA36nSnFPbV7AfohJxyadTFnfV3e-vZoAOdhO3ZkoFSWQX8gjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادارای پرتغال در حال رفتن به ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/93947" target="_blank">📅 19:03 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
