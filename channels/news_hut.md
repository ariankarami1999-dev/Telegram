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
<img src="https://cdn4.telesco.pe/file/A2kF9hvfSXZqGgwrgH2TS0L56pP-y0zKMLjrP3hhl4goqUmxHot539CVnglkH-ym1oTteANtC6OyLXvQ8O3DGW8i6o1rU_LohdKMdEmc4FIgWxEb3KiHQFtVcuUtD5mZ0IcDW-3BHopAUaGqTrCURybNAozAJLwQBVYqEkz4Sy4Fl1wmA8mQ_ermW2C-QNFz66gJZnN5ufHUq6qaWtNzvn_NY8GL_KdtRFT2mnW5G_3mDXMrYJQf2TQ9ZOaWjdgFPKrsAGT-MwRnH81aWP1RzoPXBo1OXdjGlJUy0vVRa7RCUto_M6Z1ZkRHn3XWSZWrN8Hj0jOQzn6WIbZLVMje0Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 151K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 11:14:09</div>
<hr>

<div class="tg-post" id="msg-68923">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=PTXTzR2oYV_n6E6SYA5dPjd1gH6ujbNyHWNlq1SRwUu6Yh2tbAcA7Mlx5fqrQmVR6_UqMcfBbndhRJPwe0s0Y90MVKSAv9zZX1XT6lb4KNOLXEmsvLdN4OOc44UijwhredT9SvGCrV_D97blCQYqOtuwkvTk3TCUBWhLg4bTazsdihJVAFuTR9I2iGQN7XBSwSwHjXpCFShMdT8tJJhoSrwxmMQGxJDxbl6-B17D7d2zZ35Oq3O8O667NLCupyM3OQm881GjTNct3E_A2twRvcjbUY-iMBSdMuppKwoX0j_BGICpEXWrEcLCs58DWBqai38pTd_tOsa4NhFzhUto3Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d0a634c2.mp4?token=PTXTzR2oYV_n6E6SYA5dPjd1gH6ujbNyHWNlq1SRwUu6Yh2tbAcA7Mlx5fqrQmVR6_UqMcfBbndhRJPwe0s0Y90MVKSAv9zZX1XT6lb4KNOLXEmsvLdN4OOc44UijwhredT9SvGCrV_D97blCQYqOtuwkvTk3TCUBWhLg4bTazsdihJVAFuTR9I2iGQN7XBSwSwHjXpCFShMdT8tJJhoSrwxmMQGxJDxbl6-B17D7d2zZ35Oq3O8O667NLCupyM3OQm881GjTNct3E_A2twRvcjbUY-iMBSdMuppKwoX0j_BGICpEXWrEcLCs58DWBqai38pTd_tOsa4NhFzhUto3Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش هایی از سخنرانی ترامپ درباره ایران زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/news_hut/68923" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68922">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=Z1XXXZjt-PuZePR8Rr3hrWUWMROS80zzdlIcYQrGnv8eNa7H-39YPVFZwRDkU2CINy9ozcx5cCmcA5oc81Lxmj_LHluWjrIM9dbygsbSyfS4aS_f0R4SWacndyrtYqzI0LJZ2NK3FpXWOsOJIaF43nTB0zWspnoq917acOBiuUB5_-jAhM5dMWJeJQv_Sa4s-hpF5Ybx1Dj6GYycBD1_0az0uIPW1FRi_zLHLVmXhQiSh_JXLwWxnr-H89M0N9u867rhq8HPBgvqaH2Tz1dzR2zh0W7vHGDLO0_E-FzW-QK7TNxykn5dMAyPzDP75qtexrP6KVgyqiOFYhy6fP-bGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/021ea7ea3c.mp4?token=Z1XXXZjt-PuZePR8Rr3hrWUWMROS80zzdlIcYQrGnv8eNa7H-39YPVFZwRDkU2CINy9ozcx5cCmcA5oc81Lxmj_LHluWjrIM9dbygsbSyfS4aS_f0R4SWacndyrtYqzI0LJZ2NK3FpXWOsOJIaF43nTB0zWspnoq917acOBiuUB5_-jAhM5dMWJeJQv_Sa4s-hpF5Ybx1Dj6GYycBD1_0az0uIPW1FRi_zLHLVmXhQiSh_JXLwWxnr-H89M0N9u867rhq8HPBgvqaH2Tz1dzR2zh0W7vHGDLO0_E-FzW-QK7TNxykn5dMAyPzDP75qtexrP6KVgyqiOFYhy6fP-bGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری به ثابتی:
تنگه رو بدیم بررررره؟؟؟ مگه مال ننت بوده که بدیم بره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/news_hut/68922" target="_blank">📅 10:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68921">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=XQAjOCsgE0DNOX4Dpi2HcuCoujXLPdGdnzjaVDGeLH7zFuUsz9G5r1NS62u2N59nwkoBITnjPbk8TSVXlEJc4NfR3mNN1C6s4fwbSiCgFDCRkxfHBjaWtzmjIOgrKC6yeBgt1XZmRsRUEr97t2Y194756SbQamveBt1V36eI7l4ZLqrPJIeLd24-jt55QGZltazAJl0Q2EJF7Q7e0_n0f5cZMjjDvkXXrJmn7rtrq2YhzvG7BBUAAaLZ-p_uJ2w9-bUtoceDAHkeezYPDwDhxifZn6siqqKNdaYl3ZEOjS7l78dXyaW8RaL8_0UBzoPm0lZWB2euxVooMxHwiIG17A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9407cf213a.mp4?token=XQAjOCsgE0DNOX4Dpi2HcuCoujXLPdGdnzjaVDGeLH7zFuUsz9G5r1NS62u2N59nwkoBITnjPbk8TSVXlEJc4NfR3mNN1C6s4fwbSiCgFDCRkxfHBjaWtzmjIOgrKC6yeBgt1XZmRsRUEr97t2Y194756SbQamveBt1V36eI7l4ZLqrPJIeLd24-jt55QGZltazAJl0Q2EJF7Q7e0_n0f5cZMjjDvkXXrJmn7rtrq2YhzvG7BBUAAaLZ-p_uJ2w9-bUtoceDAHkeezYPDwDhxifZn6siqqKNdaYl3ZEOjS7l78dXyaW8RaL8_0UBzoPm0lZWB2euxVooMxHwiIG17A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جواد اوجی وزیر نفت دولت رئیسی:
ما ۱۰ خط لوله بزرگ و سراسری گاز داریم. در بهمن سال ۱۴۰۲، یک شب ساعت ۱ بود که موساد روی خط تلفن بنده آمد و گفت امشب می‌خواهیم آتش بازی کنیم‌.
از من پرسید فلانی ۳+۵ چند می‌شود؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز را زدیم. ۵ دقیقه بعد دوستان از دیسپاچینگ گاز به بنده زنگ زدند و همین خبر را تایید کردند.
تا لباس بپوشم، موساد دوباره زنگ زد و از من پرسید ۴+۵ چند می‌شود؟ من گفتم ۹، گفت خط نهم سراسری گاز را هم منفجر کردیم. سومین خط را هم زدند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/68921" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68920">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
انفجار شدید در مراغه
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/68920" target="_blank">📅 04:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68919">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران  @News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/68919" target="_blank">📅 04:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68918">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=Lsc9MWoDa44i69UpHfuyvBSMr4s8oekG8p6ILo3q5h61HdnrtE0of9HgK7LrCzhOko-2Q1INF_azVnciriuNYylbPs7aTEpBX9t1nqtBsZl_3YZE7sFax9QEvyZxbdjjYB0uU7j3BfrylB_uvML6thm0nQ2Fkvx7s7WmIwHEg2z2kWIe4WiFEGfWMX8mYiEvys6w3fN3Mh1JjfvlVg6lptflgFdofg4ZdIVcF0eeDd5472OhodCHNNYqp0sTQq3RA_H46roxkRAtmT8IGWezG93pKcqR2gRUH-LVg3a5vvlcDFQuiGFV6XEW9i5wYy68P6l_vhfU_JMqrHDshdEi0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c72c3752.mp4?token=Lsc9MWoDa44i69UpHfuyvBSMr4s8oekG8p6ILo3q5h61HdnrtE0of9HgK7LrCzhOko-2Q1INF_azVnciriuNYylbPs7aTEpBX9t1nqtBsZl_3YZE7sFax9QEvyZxbdjjYB0uU7j3BfrylB_uvML6thm0nQ2Fkvx7s7WmIwHEg2z2kWIe4WiFEGfWMX8mYiEvys6w3fN3Mh1JjfvlVg6lptflgFdofg4ZdIVcF0eeDd5472OhodCHNNYqp0sTQq3RA_H46roxkRAtmT8IGWezG93pKcqR2gRUH-LVg3a5vvlcDFQuiGFV6XEW9i5wYy68P6l_vhfU_JMqrHDshdEi0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
هم‌اکنون فعال شدن پدافند تهران
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/68918" target="_blank">📅 04:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68917">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سرعتی.npvt</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/68917" target="_blank">📅 04:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68916">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CA1Ac1AYbaYlS-WlEXOiVNCiGZKoduUSbPo5Lu7h0xVYwreC6PspjyxI-E_An5mWwtyevvzeM9EWIbd6sdBVF3G34rqCexmSubMaDEDPMRQI7jU1fLgheECieyW634iImlsJGPWsd7ZFTDHtaawXVCdFOYT9UFbSyM8CI_tRVBlorZkp3lhWqrQtFS_RtTNS2LlrYCN6oYhuhrw3oY9f3AoX9-cJsy0fxqyzgptTHTnVOaIf4ZegBsPgu4ifWzbESdsR8CU0HQBgPA1NBYUhJpxJbAjo3a7sI1VXVBvepYPJqWgM0OZfzbLaN0ociDKgoPCG_C3B9jyFpKQCHkOxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ پدافند تهران به دلیل حضور پهپاد های شناسایی آمریکایی ها فعال شد
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/68916" target="_blank">📅 04:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68915">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7CjlSYwTdkwTxOJR4OYQO3tYfU6Zz-eHjrKVbokmsgrvmWcoVNbsUDN-LLWV08NCiAEXDOncszhB6bhcs2FpOBMUNud87f2wW3NHk6AjPNeAsPj5XhMxAI-3zXJ_MDjE8bupXO7tYh5_JB8tH0rwLdCgVqWkSar_SR2jGPCtBX-Bg-hR8EJ_lHbcK8V07Wpz9a3a1K83ENjIzt-9b1fxzTb1bnUFjf6D9jWjKyepPnsW5dJtXVmlOtueJFuPfGpQP02IYJwKca48FT-1zVOemOm3IjCEgxltyJByAHnF0lvYx-jcfKS8yP24V0pRthPm10_D9LRk6jxxfkywUPjTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/68915" target="_blank">📅 03:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68914">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
برق مناطقی از بندرعباس قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/68914" target="_blank">📅 03:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68913">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_hVGC5bIO86xm2pt9LTQ2bupRJ_M38j9RWcGmxUkScQOiBWxxG-X0eOlGyfKzPSchljkI4B91FNZIB4SZ-7j0FVyi9FJQDXmhkkqkvSXSZIUsiYba1chrWAO_Yjmr1i13DLQHEmqUIGE00avT8vedWQOr67jxEzRWBP51et4FiNdK_vGez5bH28-_57EBOMfPT7350xR5rQsbKtn2-6zbr9iCrfwhCG7-xNraG7a3ebrBu9MxkPOwD_R47G_dpMYl1qMzIYRkTGEDWsmBiSubHAmx3LC3JRjiEOC3GUvGloltQKhunMPLdOMSQqv2QPNbxRb7GjWnT4lWRTCJv7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بندرعباس؛ امشب  @News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/68913" target="_blank">📅 03:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68912">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🇺🇸
منابع آمریکایی: ترامپ در حال بررسی امکان بازگشت به سطح حملات مشابه ابتدای جنگ است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/68912" target="_blank">📅 03:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68911">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=tnSkWIVbOVMvzKuKgsHh1E_Ve2tAGxCsTlf6bCplHgXzhOUnwYwivhSVW6gZbI6UxCPe-MK7_p_LrwDe7IdnhjPQknwxDfGLVvz-QGlTsRPhrspzvQ6BbAggj-yKXttekiOmsiSE_aP_N-iOglANzQE_u-S_P_cUeVsK3S1MoN5FFFCMvkngQcgpvtUMtyP9nq50Fu80Xs29ENgbNFi9d4X9Kwo6aNdFyhfBGN9n2MnUKEA4bTD9vihLCHN99M92f1vtkkdtkwu6C6SGqVN1HRVlhU32XKWiOR4oTHN5hwtmFmKInCArmUkO48MD21pV8YXN-ZtKX08GCLRNoJhmhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37ca8b5fd7.mp4?token=tnSkWIVbOVMvzKuKgsHh1E_Ve2tAGxCsTlf6bCplHgXzhOUnwYwivhSVW6gZbI6UxCPe-MK7_p_LrwDe7IdnhjPQknwxDfGLVvz-QGlTsRPhrspzvQ6BbAggj-yKXttekiOmsiSE_aP_N-iOglANzQE_u-S_P_cUeVsK3S1MoN5FFFCMvkngQcgpvtUMtyP9nq50Fu80Xs29ENgbNFi9d4X9Kwo6aNdFyhfBGN9n2MnUKEA4bTD9vihLCHN99M92f1vtkkdtkwu6C6SGqVN1HRVlhU32XKWiOR4oTHN5hwtmFmKInCArmUkO48MD21pV8YXN-ZtKX08GCLRNoJhmhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بندرعباس؛ امشب
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68911" target="_blank">📅 03:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68910">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
دقایقی پیش صدای انفجارهایی در قشم امیدیه و اندیمشک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/68910" target="_blank">📅 03:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68909">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=W8TK39E-zbdApsg9JznX8AdJTkg8xwdAi_p4G3At1O7oqyvoy4mKd-Hr-Wi8tGsloGnExwHHd_b91lI-CBNsg3VSfOgcuck2DYWdp0N-buq2GFTBawb9l99HaUnl411Yye-wtCjBQ3J7xI5N0S0GFE8SNqroW52W7lJ5Yt7mYy7JHn1utK-shTKQHn6TItsf9R5Vl1a8GbkwISzQFxV2u_FUOGB8e4iYFWCUTWEzY1HLj-2KwP6m5wcHyTT_xt8OcZvRN4ufmm5dyb45sxvYK5-a2FjeqkVLEa8FF0BLpF367oNRSUPHFg0m_RuRH6HAHZ6V_vA-68uFNyYa43C1LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893c5afe7e.mp4?token=W8TK39E-zbdApsg9JznX8AdJTkg8xwdAi_p4G3At1O7oqyvoy4mKd-Hr-Wi8tGsloGnExwHHd_b91lI-CBNsg3VSfOgcuck2DYWdp0N-buq2GFTBawb9l99HaUnl411Yye-wtCjBQ3J7xI5N0S0GFE8SNqroW52W7lJ5Yt7mYy7JHn1utK-shTKQHn6TItsf9R5Vl1a8GbkwISzQFxV2u_FUOGB8e4iYFWCUTWEzY1HLj-2KwP6m5wcHyTT_xt8OcZvRN4ufmm5dyb45sxvYK5-a2FjeqkVLEa8FF0BLpF367oNRSUPHFg0m_RuRH6HAHZ6V_vA-68uFNyYa43C1LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
منتسب به حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/68909" target="_blank">📅 03:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68908">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=A1-z9982EshWRxdeUSjduzRThd4KWa-FK7jyNpA547HCkLQsZLOk_ykmQXr1Ak4vjt0BOnlbs0HM5P4NLglV9iaogPA47HOQiALsetTFoY_3Tdu_WLD6TUuPLCuB5R5W6WBeF0xCciuUTpSaTDHu1is-6EBOgHm9rplPOvuZGdFNVilHyWHQslL7EiJUJ1PtEdHreJmZbffYkzK2ZL4XB68dNtjm2MkLDOZqhCdJ-fUu-Vl3RCXAHw_PgSCkZmK8IGx5zoq-ainOA7NRCLUC-xjKF1ie79XHXQ9d372uakKp4S9Qs6zzTlQaS5iDJ2VvEJpx-1K1abSyCT0KTKYK_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e6ff0ec3.mp4?token=A1-z9982EshWRxdeUSjduzRThd4KWa-FK7jyNpA547HCkLQsZLOk_ykmQXr1Ak4vjt0BOnlbs0HM5P4NLglV9iaogPA47HOQiALsetTFoY_3Tdu_WLD6TUuPLCuB5R5W6WBeF0xCciuUTpSaTDHu1is-6EBOgHm9rplPOvuZGdFNVilHyWHQslL7EiJUJ1PtEdHreJmZbffYkzK2ZL4XB68dNtjm2MkLDOZqhCdJ-fUu-Vl3RCXAHw_PgSCkZmK8IGx5zoq-ainOA7NRCLUC-xjKF1ie79XHXQ9d372uakKp4S9Qs6zzTlQaS5iDJ2VvEJpx-1K1abSyCT0KTKYK_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
لحظه وقوع انفجارها در تپه الله اکبردر بندرعباس، دقایقی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/68908" target="_blank">📅 03:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68907">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFKj8yn8H362oVB1V9haClQU8BpbLbRpoEon8R-XjTop2mRFc8bwKBFNSBEnI_2noGJ3EPfLwoKalJo_3FCXRbHcTLzuaqfNNsnfxVyw_3DAPS-nPhCQhm96R7A2PKdez5710xRO3-UHTLsPasjYsAFldb4TSxrYX9iilRMNJ2qUGPkHHBYgG-Vn6FWN2SyApUpGf4tt4XQQtBhmNZkl_LTRmPpjM8-4O8ye_aqx71i13-IFYVlVzZtMYAcMWgUJXyiJlpUreoB5UAhaHV0E-OigIrtgwTMgkQLb1iY4KyUuFOXRUoLYO0RlQ8QIexpjO2DdMEPB5QTtK6m_jPSrJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/68907" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68906">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی  @News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/68906" target="_blank">📅 02:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68905">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=Xe1kEsS6kK4ZT7JwTpovEIT56WgellakCaj0yRtk9tTogVv7KSAO09ndOd2usitbCxh25kfq3XZYImbFkM5JnJ2zJCBBDxSl7ogKWzpaMd4zZ1bj4J6a12rzv5xm7o-ltAHV-u05TPPJEhRFvJkICjISTMz1dxLp-pwrPWIF2atFVVYFuxxnN8WS_BHpibarVR9vadRktSFuHsT4Mk_1p1IkmhevddqQZWHV7HGZcaZ64aTvW_WBAaIUfC9ZhKeuCrFSl_bKUlslkfC34-mW6f8hCZqcWPG29M1XQ1wLDjX5Iase_IQHkD2TjX58Jk9NeF6cYxcHl6bHalY-3I-HLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114f82e10d.mp4?token=Xe1kEsS6kK4ZT7JwTpovEIT56WgellakCaj0yRtk9tTogVv7KSAO09ndOd2usitbCxh25kfq3XZYImbFkM5JnJ2zJCBBDxSl7ogKWzpaMd4zZ1bj4J6a12rzv5xm7o-ltAHV-u05TPPJEhRFvJkICjISTMz1dxLp-pwrPWIF2atFVVYFuxxnN8WS_BHpibarVR9vadRktSFuHsT4Mk_1p1IkmhevddqQZWHV7HGZcaZ64aTvW_WBAaIUfC9ZhKeuCrFSl_bKUlslkfC34-mW6f8hCZqcWPG29M1XQ1wLDjX5Iase_IQHkD2TjX58Jk9NeF6cYxcHl6bHalY-3I-HLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران پشم‌ریزون اهواز توسط بمب‌افکن‌های آمریکایی
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/68905" target="_blank">📅 02:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68903">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=CASOcfFdMRawN57ydItsFCmC93SbNSGD8J113MRLZ1jK2EZh7bgdl3YGr6JAGGEx19eXMzuYcUbxNf651IHY5yQVZhwsLrZUfefMESvNScx9_tChLOkFcpwSjdOAvHQjQVobKbV0jPo05V63GcX2c099Hmgm-GUgDB6oiwK-lNLBEYWZjXXLY9VZJrfFx-ytqhVWnPF16eCkuBGBr2oyYnimivD4N5oZgeYra2jjGBP-WmyyUEqrx9dkRqDkJ96N1qAkjz6WQ34NMVMVh-OLmZ0hoUNuzSi2sLhUY2ObG-vpd8L-s4Q9BMiemCzB_AaydaXQGDYQSmft8uwnV2gUJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd4f521a9.mp4?token=CASOcfFdMRawN57ydItsFCmC93SbNSGD8J113MRLZ1jK2EZh7bgdl3YGr6JAGGEx19eXMzuYcUbxNf651IHY5yQVZhwsLrZUfefMESvNScx9_tChLOkFcpwSjdOAvHQjQVobKbV0jPo05V63GcX2c099Hmgm-GUgDB6oiwK-lNLBEYWZjXXLY9VZJrfFx-ytqhVWnPF16eCkuBGBr2oyYnimivD4N5oZgeYra2jjGBP-WmyyUEqrx9dkRqDkJ96N1qAkjz6WQ34NMVMVh-OLmZ0hoUNuzSi2sLhUY2ObG-vpd8L-s4Q9BMiemCzB_AaydaXQGDYQSmft8uwnV2gUJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/68903" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68902">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bh2GXRKdHKzk2kMzkUSTXxVqrlcIwWpOTubrVyOOIPCs_YY7NUtlYY2uY2TYn2pIomRhCVJFIGahjedNF4S1yohamn3uqd6YJBDzTdwUmeV8SSjT5jJBsr2SrsESYutfClthXMC8W0uoloVdOQzwKD9Ezf11pYNhY-df3U3xrtho6VY4xxU9BqfWA6Mi_xAac_kYh5Y60wZwrNtpIwi6YA4l0kDDqBXvCjP_ipYP79C_BNC29_AXNjMhUe_L51GTQz925BNPivpISCfrRJcUs_ZoReEu3S-K4RramWurydpkxj_o96Rmpltjf2PkB-vY9xnLvxlwH4XIFqNFgcyxYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی امروز ساعت ۶:۴۵ بعدازظهر (به وقت شرقی)، دور دیگری از حملات شبانه علیه اهداف نظامی ایران را آغاز کردند. این سیزدهمین شبِ پیاپیِ حملاتی است که با هدف پاسخگو کردن ایران و کاهش تهدیدات سپاه پاسداران انقلاب اسلامی علیه کشتیرانی تجاری انجام می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/68902" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68901">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدیدی از حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/68901" target="_blank">📅 02:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68900">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
چندین انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68900" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68898">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=Quq9fglWHzY3ajmvmD7oQ-sunr25Lq-p6Zsgf35XxgMnYgx4Xw4oJYuzHBh8DeTGbI2CspPmS2AbuB-xzZc_CeLUA83Qo91p3W5Ymmv7waDnzA4LFOOAY3177MzgrT1vyopQbhc97a8vfRKdGcI4d1iODw7fW0oURLt7e1daSgyY1XArYjejfxsAssA0hzD9piLXI1GlQc7ViIoXeae3dES7mSVJfkgxP7RvCl2UB9ZNsNCsMY7VXbPlzWCN_5O89Ut6J7y42lvPQeYp-dSbMaA2uXx1OJ8neXtVgfjZ8NhoTEB4Cp_rjZ1PRbD2RHZFZ1E2CP9ViAuDkXGmYOJ0mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5461419a5.mp4?token=Quq9fglWHzY3ajmvmD7oQ-sunr25Lq-p6Zsgf35XxgMnYgx4Xw4oJYuzHBh8DeTGbI2CspPmS2AbuB-xzZc_CeLUA83Qo91p3W5Ymmv7waDnzA4LFOOAY3177MzgrT1vyopQbhc97a8vfRKdGcI4d1iODw7fW0oURLt7e1daSgyY1XArYjejfxsAssA0hzD9piLXI1GlQc7ViIoXeae3dES7mSVJfkgxP7RvCl2UB9ZNsNCsMY7VXbPlzWCN_5O89Ut6J7y42lvPQeYp-dSbMaA2uXx1OJ8neXtVgfjZ8NhoTEB4Cp_rjZ1PRbD2RHZFZ1E2CP9ViAuDkXGmYOJ0mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بمباران اهداف توسط ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/68898" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68897">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=q_t_BbQh2Y6MYiEAv1DJ9ey7b-mKPKbZDlwXW9qneEBZkiozldNMM8xts5pU8BkG-T2tMIrRrnzY9u-cfD9azORZG8pi0XUuYwdnOifB6dRjCS4c2uM0NiK6nxgNo5qHpdhBm5WqYY7oh2BdB-XXzMK9zvYuUSYKHAiWkS-SsRIW1A08HwO_yR6UHkHSCOjtqw-2s9o98H80IyeOSZolRlbU6IaR-cFMyDLyZDzwo7h8PoUSKvfwGX1cbx0A_addVDb5FN0oP5LgwctChb63PoxPFbkPwDEj4D01b1ezFRMLoEOq6UALHaM8V1NMm3ssE3eSbdrWf5vWIUu9z-_skQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1175f94fc3.mp4?token=q_t_BbQh2Y6MYiEAv1DJ9ey7b-mKPKbZDlwXW9qneEBZkiozldNMM8xts5pU8BkG-T2tMIrRrnzY9u-cfD9azORZG8pi0XUuYwdnOifB6dRjCS4c2uM0NiK6nxgNo5qHpdhBm5WqYY7oh2BdB-XXzMK9zvYuUSYKHAiWkS-SsRIW1A08HwO_yR6UHkHSCOjtqw-2s9o98H80IyeOSZolRlbU6IaR-cFMyDLyZDzwo7h8PoUSKvfwGX1cbx0A_addVDb5FN0oP5LgwctChb63PoxPFbkPwDEj4D01b1ezFRMLoEOq6UALHaM8V1NMm3ssE3eSbdrWf5vWIUu9z-_skQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حملات سنگین به اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68897" target="_blank">📅 02:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68896">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3266056eac.mp4?token=IZRbD0Cs_FmqTD_ZNQrAwAjymkrYuvgKhWBACAlULVhSQaSodcXEzXymxs1dranmR6VGch9DS65Pyxrl5DGMN9Y9Mde1rdVC0PwlCxlx1h2jWPuAq4vOaxHkWiAdmgonP741LoD1WhGPnHIJis7joF9KDgQjsjWO_kfI_P45yAC8zawz8gLY1fMMKMk1d0RTjpdIHd1tggVRbTuuL4DsYkzpFqojZRasYPqolhrsB0LI1KiBI2w2NE6u4J3F6iyRh3_KC2QOCUO37U2nvosczaU5s3nHuBSTMsLpRgJBMRkSRKixp8rVc-GE1nGnUeXVoGVgP3D7Vkd3IN6urz269A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3266056eac.mp4?token=IZRbD0Cs_FmqTD_ZNQrAwAjymkrYuvgKhWBACAlULVhSQaSodcXEzXymxs1dranmR6VGch9DS65Pyxrl5DGMN9Y9Mde1rdVC0PwlCxlx1h2jWPuAq4vOaxHkWiAdmgonP741LoD1WhGPnHIJis7joF9KDgQjsjWO_kfI_P45yAC8zawz8gLY1fMMKMk1d0RTjpdIHd1tggVRbTuuL4DsYkzpFqojZRasYPqolhrsB0LI1KiBI2w2NE6u4J3F6iyRh3_KC2QOCUO37U2nvosczaU5s3nHuBSTMsLpRgJBMRkSRKixp8rVc-GE1nGnUeXVoGVgP3D7Vkd3IN6urz269A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بمباران سنگین اهداف نظامی در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/68896" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68895">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از بمباران سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/68895" target="_blank">📅 02:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68894">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
فارس:
گزارش‌های اولیه از سقوط یک هواپیما در آسمان جزیرۀ قشم حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/68894" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68893">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68893" target="_blank">📅 01:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68892">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نیویورک تایمز عملاً تبدیل شده به فارس و تسنیم
😐
آخ که چقد این چپ‌ها ولدزنا و حرومی هستن
#hjAly‌</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/68892" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68891">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:   لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد. اگرچه ممکن…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68891" target="_blank">📅 01:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68890">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0BNn0CFMF0j0wP3E1gRJOLM6Q-oQRN4nVPGg7JNiurRGaiLb73S4wXLjqOQwBKhNYPwqfHCz75XLqjnQtlknoumy7YZDwVjmoHTSLn6cgrUnOAkRkdV31TYseyTmoqKVOX8EMvOjtOGSa3N71_R_G4kUm_vmgsKylzXlrmc_ouCkuIKm9qLXseNzI0CuiO9kuIgtBiCuPvIkYMbm4L5FJx6D5EA42MTmjaXfoYg0cnkNK8_O8uBaZHQ23mkI4mjp8xkd2rgN4MXXrlHVPNsr3WVlpmNSHjzSn4E6KAfpl3hfku9SgifzKe7-tbpBrge9iDy6unE6gC86xiMg6tSSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ:
لطفاً این بیانیه را به منزله اعلام این نکته در نظر بگیرید که از این پس، هزینه هرگونه خسارت وارده به کشتی‌ها، محموله‌ها یا هر مورد مرتبط با آن‌ها، از محل وجوه ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد.
اگرچه ممکن است این خسارات بسیار سنگین باشد، اما با این حال، این اقدامی عادلانه و منصفانه است.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68890" target="_blank">📅 01:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68889">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=IW_sa9uQyBUjkRgrLvulOtP4cVTdWBhvTB1LOXGRIimNRRHBnWUoBCDVlPkVc_kuk9uHT2gvQhD9IoH4334zqLR9QJQkrDQA1p6ZEy2ySLwJMFguIPyib2h1QyXoZ_dXPTfQdc5KPgt3CgDSUeWOK3FFm_9P-mW9W2Cb130tRwUvqagHYrwEtEPPtFGuTgKeu0Xeu9vio28ow6htt-5XnudDla1Khgl9Gq_UpD57RVfY2zT5CGLlGvhen4MJemWhYkGBBs2uv8OxpsHpmasuX82UdhQfyvyZXVqOlHGgzgLy-kWElgFo3-PmARsgU3YS3fQ_2yrINxZ5BNNNUxaCyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc8bcdee4.mp4?token=IW_sa9uQyBUjkRgrLvulOtP4cVTdWBhvTB1LOXGRIimNRRHBnWUoBCDVlPkVc_kuk9uHT2gvQhD9IoH4334zqLR9QJQkrDQA1p6ZEy2ySLwJMFguIPyib2h1QyXoZ_dXPTfQdc5KPgt3CgDSUeWOK3FFm_9P-mW9W2Cb130tRwUvqagHYrwEtEPPtFGuTgKeu0Xeu9vio28ow6htt-5XnudDla1Khgl9Gq_UpD57RVfY2zT5CGLlGvhen4MJemWhYkGBBs2uv8OxpsHpmasuX82UdhQfyvyZXVqOlHGgzgLy-kWElgFo3-PmARsgU3YS3fQ_2yrINxZ5BNNNUxaCyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
مقدار قابل توجهی از هواپیماهای باری نیروی هوایی ایالات متحده (مدل‌های C-17 و سایر هواپیماهای سنگین‌بار) امروز از اروپا به سمت خاورمیانه در حال پرواز هستند.
برای توافق دارن میان
😃
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68889" target="_blank">📅 00:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68888">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
دقایقی قبل دو فروند موشک در جریان حمله  آمریکا به محدوده روستای مسن در جزیره قشم اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68888" target="_blank">📅 00:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68887">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b133a06016.mp4?token=MbivvLuGOQ1cKHx0paqeipqS3ec8m1basDHE9jDJE_QSwk9xChkr0d4sTH4yq-1l8HVk62ZOQQ8B9dAgug-HWuPGTVsxuMRACBfV0hD_Yyme99UpSoglpceV9w8N1-sZ6W1a2GJULEtZVnLKanQv_FKy9b_V7ATAZLQGnULnD8XASztPTRoSU-qAgOGSSizpt4TuyWrEXDmlvDiD7sJ9m3hYtr20Wp3GaH35xRZznLelOMi7A6WeqADCAMvoikf8M9GFvbd8LM1mBFnAuTgDBtqQT8MjM53pl2yEYqclbH6U8PUeHLYpwAsP64pNi2jNhTngzOwMCfPqWF1NpCTU3Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b133a06016.mp4?token=MbivvLuGOQ1cKHx0paqeipqS3ec8m1basDHE9jDJE_QSwk9xChkr0d4sTH4yq-1l8HVk62ZOQQ8B9dAgug-HWuPGTVsxuMRACBfV0hD_Yyme99UpSoglpceV9w8N1-sZ6W1a2GJULEtZVnLKanQv_FKy9b_V7ATAZLQGnULnD8XASztPTRoSU-qAgOGSSizpt4TuyWrEXDmlvDiD7sJ9m3hYtr20Wp3GaH35xRZznLelOMi7A6WeqADCAMvoikf8M9GFvbd8LM1mBFnAuTgDBtqQT8MjM53pl2yEYqclbH6U8PUeHLYpwAsP64pNi2jNhTngzOwMCfPqWF1NpCTU3Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امشب تو میدان ازادی تهران
زیردریایی سپاه و سامانه‌ موشکی ذوالفقار بسیج
به نمایش گذاشتن
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68887" target="_blank">📅 23:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68886">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgX5GBzfsmALsKT1OvtBRGQ9SeP4-JnD6_biFYFZpKV-OP8vhZIlcVsxC8WQAcQutghCoMDX6C0tcDHOxeyOj-eOmzgS7eFCD5IXGd2714cJfAvqRNyX49iTm5fvMF1nM5fs8_La4nu0-6_wawhzI4o-D6uLZmkkG6i-aWy8pDV7czhPm-Z9o0dQsLjTxRTg_PjxRxscbW2Od_RNft1mREm0hX9FxS7W_ghpt0kbURaleViH7HMrhNil3ldCmlulruxDDqexd1YFHcc_49ZBOpKUDCY2p5FRYkPqQ_T9OMSBJrpmVcArc0y_8WbEJMgN230qaHJ4ZgF-EpQdiigS2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک دیپلمات آلمانی در گفتگو با شبکه «فایتوکس» (Faytuks) می‌گوید کارکنان سفارت این کشور در ایران خارج شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68886" target="_blank">📅 23:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68885">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن  @News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68885" target="_blank">📅 22:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68884">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: رابطه‌مون با ایران خیلی خوبه، اونا توافق می‌خوان، اونا بدجنس و باهوشن
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68884" target="_blank">📅 22:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68880">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BERS-1BIM-jBhKsA6rGZF5Ij2l9J6vNaHkHNcWI50ZqN2FL4eEDQ2JmoHUNA0-OCxgf3dUyw91MOl27IL_i_pjsZH3gXr3VgtnMdtzLYdc2PcIc2mVux_Rq9_T-Abv9UiWLPu8RIQFlqIKCHDyTqI9xdMUY-XrFKG1HlMH-mya_oJ9NkTCrTOhCLrq1g8aDHZIuEXV5tNvuA7hjXUmQHn6mHKoS6pPAWfAzm_9DIz7F8Q_PCyGnTToLs1wlxe26lTrmpOLaCSCBsdE5LFFuUz_FZ22FZyKK9FjrGuOUSvvAEIxXrtBJKL5X_t_-QBKmJXj6sdb9QxfrEQ3x-nx96JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zjo4MieI-SsquTK59NEebRy8MSGtSzP-WVO8Eoflv9660sxvFQRCUlWSMqV6sesrT8cpFWDzbtbh8ldJjAvn4rcwct_WzhKwQCY-L5X2WGOMvF0tynZHvfZydaDxJw5qDAhcSvc-cFG_q5qI2zPyWhQ8-ApyxO8S86pz4E8cjzHrzXzcfBtgfjvF33gG5VjXJf5GIz__n5Er0WuwqMioQWUFQW88BsbbWtiCIrYl-eWtAVCca3Wu5olun1lUt1YCpr_Rp1-fI1HWrwLJSscpwt7UlgG0aYabuZiDTZw0ZVL3Wj3zIEBrKdG8dhZB7s864RTylYiFWz6r6hUi2truCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=dvgB9Y6-MFuoViZpYwDVIRts9dXq029MdHbjXR7SgKXswdOC5NkGutFmsjkOCAD5HpTcNGGKgWLVdWRUS_c5MHnC0hbUApSUHNGGEpCe1KTm5lGmqFEz-fPMqk8lVzPtvIpvn4S8hn9crtpMwCS99pFQcPzf27EKT3WXZg3o5Q7cIMVz_NFiHzXDLQYFNQC5YoYxZA5n84f6lt2PjMGCp9s5sRrYpdN2r1xpfJK9H244G2c2QN0lZmqOwToT5iFEkRYBlXR7M5jFBe0eo4NAifuCtcVZo3JpzuBr8560vmPNGf29t9ZBkqD8LifNENMdkerwSD_O0aB6eAvTP4Bn-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a671667b4f.mp4?token=dvgB9Y6-MFuoViZpYwDVIRts9dXq029MdHbjXR7SgKXswdOC5NkGutFmsjkOCAD5HpTcNGGKgWLVdWRUS_c5MHnC0hbUApSUHNGGEpCe1KTm5lGmqFEz-fPMqk8lVzPtvIpvn4S8hn9crtpMwCS99pFQcPzf27EKT3WXZg3o5Q7cIMVz_NFiHzXDLQYFNQC5YoYxZA5n84f6lt2PjMGCp9s5sRrYpdN2r1xpfJK9H244G2c2QN0lZmqOwToT5iFEkRYBlXR7M5jFBe0eo4NAifuCtcVZo3JpzuBr8560vmPNGf29t9ZBkqD8LifNENMdkerwSD_O0aB6eAvTP4Bn-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای تهاجمی اوکراین در یکی از بزرگترین حملات از لحاظ حجم آتش شرکت بزرگ تجارت الکترونیک روسیه، Wildberries، را هدف قرار دادند.
این تأسیسات که در شهر کراسنودار واقع شده، به‌طور کامل در آتش فرو رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68880" target="_blank">📅 22:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68879">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇺🇸
ترامپ:
کیرم
تو هرچی کمونیسته
#hjAly‌</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68879" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68878">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند  @News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68878" target="_blank">📅 22:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68877">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: کاری که شروع کردیم رو باید تموم کنیم، اینا وحشی هستند
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68877" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68876">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">همین الانم ترامپ داره حرف می‌زنه
#hjAly‌</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68876" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68875">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اگه امروز این قطعنامه رای میاورد، ترامپ مجبور بود جنگ رو تموم کنه، یا اینکه قطعنامه رو وتو کنه! #hjAly‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68875" target="_blank">📅 22:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68874">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.  اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68874" target="_blank">📅 22:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68873">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=dRkDIvp3xYLDDa9d2Pl_E-atJjVV_ooDULcRM0UO6gpDg2mV_EDmRYfN6sDx6BiTfwI_Ew0GlZIbULUhokumfZ_jS1B2Sb-Hkv6PiC2vgycWvCNa7Q8befTS50lGpVgeA_cxnD2JGDcE7P7upim5aqMb2wEsILsIGNzAl9oXwXBErMISrtYB948SrAHXb7jkrWcwNQpfVs3rWvoxyqjkbPB5vv6Cj6jig4q5cbheyokJaWvUN6tpnr_USKhyJmJOQAYHEy3Igvx0z-LvhI9s2q6LUbodM9trtowxw9Fjhso3jlS5Zr4EBWDJHrC7L16mE86OddV9aT-wU5keXkLJ9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/351349ff2d.mp4?token=dRkDIvp3xYLDDa9d2Pl_E-atJjVV_ooDULcRM0UO6gpDg2mV_EDmRYfN6sDx6BiTfwI_Ew0GlZIbULUhokumfZ_jS1B2Sb-Hkv6PiC2vgycWvCNa7Q8befTS50lGpVgeA_cxnD2JGDcE7P7upim5aqMb2wEsILsIGNzAl9oXwXBErMISrtYB948SrAHXb7jkrWcwNQpfVs3rWvoxyqjkbPB5vv6Cj6jig4q5cbheyokJaWvUN6tpnr_USKhyJmJOQAYHEy3Igvx0z-LvhI9s2q6LUbodM9trtowxw9Fjhso3jlS5Zr4EBWDJHrC7L16mE86OddV9aT-wU5keXkLJ9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
سنای آمریکا با ۴۹ رأی موافق در مقابل ۴۷ رأی مخالف، قطعنامه اختیارات جنگی علیه ایران را که رئیس جمهور ترامپ را ملزم به کسب مجوز کنگره برای اقدامات نظامی بیشتر می‌کرد، رد کرد.
اگه این طرح تصویب می‌شد، ترامپ برای هرگونه اقدام نظامی جدید علیه ایران باید اول از کنگره مجوز می‌گرفت. اما با رد شدنش، چنین محدودیتی اعمال نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68873" target="_blank">📅 22:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68871">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0_boY8j4X8wXUzsxRsu5P2Qo7sR6UPvWZBG5_8e7mzVW8qkrPFCksnv-4PqmoEbqgTM9nMBbVQC5NjDc4dTEmxLoErBKz2oWfKuI0JOY8OdgHmYhEBa94MnZ5B4PFQOIWKnsxZcjvvLRWf_QKFYz-XIDg_Ecoa4cl__e6LJeZLgltJ-qpIBF5_X6s948j7bglmIv0Mv2R3Z56w3lCfABRb27nA51O1c7tOStULg9-FKVtOOdbBK7YwO_yRlSOX1Q9RSCpiV0DbzicJbRSECZTjOetf_DaWiYI7UySkdldUIfykQ3cwa6pckuo1VT-j2Nr0GaOZiLK9aRXJJVIbRdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=fXJr4R7oEma8CQiQPTYlfueeJGFqaxPt8Fc1kXC12RQ6Qt1fKlt3E5P2uMm18PiG9e-muVVjCbU9kzbJkmHavbUmPPUrTUa3zLIC5Nxvp-zB6Ix4UNkTlyDrxIHpivdLhThXB0bR04mRHBeOdOuCe9NCatG8ixr07i_cEMYG8oTVfgtA1c-T5TxCAomEXK_F4KZsCyTGvNhk2ol2ydEp-gSOKAoHZ-dVHTNO-6l9IR50zenvXmi1LABK8OGK2t59z1zQFU3xPkTP0qBzdwlkrfB7XHNdLUTF7WSTKQFEW0BQ69Kf-H49C3Ai5i1Cycl8V_tBnqqFaP3lV9IDg7ttYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca0071632.mp4?token=fXJr4R7oEma8CQiQPTYlfueeJGFqaxPt8Fc1kXC12RQ6Qt1fKlt3E5P2uMm18PiG9e-muVVjCbU9kzbJkmHavbUmPPUrTUa3zLIC5Nxvp-zB6Ix4UNkTlyDrxIHpivdLhThXB0bR04mRHBeOdOuCe9NCatG8ixr07i_cEMYG8oTVfgtA1c-T5TxCAomEXK_F4KZsCyTGvNhk2ol2ydEp-gSOKAoHZ-dVHTNO-6l9IR50zenvXmi1LABK8OGK2t59z1zQFU3xPkTP0qBzdwlkrfB7XHNdLUTF7WSTKQFEW0BQ69Kf-H49C3Ai5i1Cycl8V_tBnqqFaP3lV9IDg7ttYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ساعاتی قبل سپاه پاسداران یک نیروگاه برق در کویت را هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68871" target="_blank">📅 21:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68870">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=QjQdsoh_K-3eBd8c-Jzs9Sknt2yZ-mb4aVxzVg2qoyJMew4lNQ4JNdsBU58G8uWji2ZgfKePY0WAJQ_rlem8sHsPfcrgOtyE5YLm9RYgi2tZ3pOTWLFJB4kaLgzH9lbNKM7wrQJ8nAviFRkXNLKNz3dhU6TQUNIVCAcN8Dn_6xowd5KiJaDNZOp4A3Hl2Ow95su9ElW8XHaX4MwfTE3JhRRWfwBd_IPhIgOaKtkGwPW22WpE3YR-78t3UH05QWUyZ5EDbarQyd0CXfcPwYfbPjyWpDpwU6uUFn5uKlblTDSWr6KqIvyGOA5DZFgP5C9H4azsrij-L-5CU2gca8_T9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abbda0c817.mp4?token=QjQdsoh_K-3eBd8c-Jzs9Sknt2yZ-mb4aVxzVg2qoyJMew4lNQ4JNdsBU58G8uWji2ZgfKePY0WAJQ_rlem8sHsPfcrgOtyE5YLm9RYgi2tZ3pOTWLFJB4kaLgzH9lbNKM7wrQJ8nAviFRkXNLKNz3dhU6TQUNIVCAcN8Dn_6xowd5KiJaDNZOp4A3Hl2Ow95su9ElW8XHaX4MwfTE3JhRRWfwBd_IPhIgOaKtkGwPW22WpE3YR-78t3UH05QWUyZ5EDbarQyd0CXfcPwYfbPjyWpDpwU6uUFn5uKlblTDSWr6KqIvyGOA5DZFgP5C9H4azsrij-L-5CU2gca8_T9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب یه دلقکی اینجوری پشت ترامپ اداشو درمیاورد که حسابی وایرال شده
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68870" target="_blank">📅 20:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68869">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=YmQiEMn9nj-X2AOAahnoBRPzCtV6lBVA5xa727PY8N5ghM709Kr6_vFXdsqYyBI9_1h0tJQ5iztdv20-rGhUIOPedX3nNCOBK6Jz5OdL6LofQKXonNzTLRzLEJoVrElsjZTEupKOiuJOVdGpR0M_VSA97t-gPD8e7ICEjbJ0ZiIqOMXPb7ZC_doaNCDw7or-KXMAzH3j9Jch2sPkuuQkQXoVoHX5HnahBn6EJGoOiH6vbRYECPnKpVCMDTy52Ws3e9ZfM9GigsRm0B_hwBjjkGEzkUuLUGp3lvRsiXtdaEBXO8a7MRYWPQ9GqyRnsFiRWQpnp2TwwIRMdkN6Fbs__BBfNjCg0EVJAoF_ntfifRhOcvPUD2s8i7bxFvXJltO4VKSnE4RblDiIsxvkguXsWsYyXOIsGb0wSYEH9NOHuQRomE3gp17gwedYcXCSBboQbJLZmF1HsM8iGwOIgO3WJFPgBh1YbOs0wgTskddJAE9PFZ9blknNpmO7bJNj5vnSZsCt76CmFahA3uHkzbdkwJziAWjWWnU1IROfnLdR0HftLj2KCFSB-BLk5YX8ZqtiIhGhqsss3sVMjuRG4olzJXbS6edwX0MJIpNuCfFY_BNjwr7QOA33hycnr2JEdP6Qew6LT3NShdrgUvs3AvuLA7qcekOqbFB8uJ3WX26ATuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed7300c82.mp4?token=YmQiEMn9nj-X2AOAahnoBRPzCtV6lBVA5xa727PY8N5ghM709Kr6_vFXdsqYyBI9_1h0tJQ5iztdv20-rGhUIOPedX3nNCOBK6Jz5OdL6LofQKXonNzTLRzLEJoVrElsjZTEupKOiuJOVdGpR0M_VSA97t-gPD8e7ICEjbJ0ZiIqOMXPb7ZC_doaNCDw7or-KXMAzH3j9Jch2sPkuuQkQXoVoHX5HnahBn6EJGoOiH6vbRYECPnKpVCMDTy52Ws3e9ZfM9GigsRm0B_hwBjjkGEzkUuLUGp3lvRsiXtdaEBXO8a7MRYWPQ9GqyRnsFiRWQpnp2TwwIRMdkN6Fbs__BBfNjCg0EVJAoF_ntfifRhOcvPUD2s8i7bxFvXJltO4VKSnE4RblDiIsxvkguXsWsYyXOIsGb0wSYEH9NOHuQRomE3gp17gwedYcXCSBboQbJLZmF1HsM8iGwOIgO3WJFPgBh1YbOs0wgTskddJAE9PFZ9blknNpmO7bJNj5vnSZsCt76CmFahA3uHkzbdkwJziAWjWWnU1IROfnLdR0HftLj2KCFSB-BLk5YX8ZqtiIhGhqsss3sVMjuRG4olzJXbS6edwX0MJIpNuCfFY_BNjwr7QOA33hycnr2JEdP6Qew6LT3NShdrgUvs3AvuLA7qcekOqbFB8uJ3WX26ATuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فاکس‌نیوز در حال بررسی فهرستی از اهداف زیرساختی احتمالی در ایران است که ممکن است مورد حمله ایالات متحده قرار گیرند؛ اینکه کدام نیروگاه‌ها ممکن است هدف قرار داده شوند؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68869" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68868">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9UEeXVANQ0dHcgI4hrwzKZWj0gheUWQbn0KwNcksZ_6HuUZVwy4iqv_T6tolgAsy7gF68fyM8xajbEmi3Qvi9H2_gy6xXcc5-ADeHM42Co_gmDOMRTA3yHtMAzUGqFzQY_3-uBbE0qkiSPU3QS2-dupBHZlD-970zPjGf8ElqA5Ovq_sWtUsaKyZyDbvwOyvR69smLYIZMxgYjfQixWvNl5ZxtLNlr88qQAsGlUR1ueBxKftIgR4OZtHC30bvB3RimSF2GmpMzKShuvdit-fNFB5-ItVTIc6JDyYeHeLNJoUSFovjLlT9KoEyxD3ACwsSnZPNGeRfvrNsuM4qk6xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68868" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68867">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioDMq56aGDY5nA5creOC4TQEVh3YLU3V1bdjh-tm0qUzr__xDJab4FCqZXgHtdA5R-6PaTs-Ayrv6oHCGDPLxaNdQQD0CK28Rya8pzdXCp2QqV9KQcDfSkOfzG3mYerJX7NL74Q4HaIfCtYnpiShKaNhxuhhacbxQ1IQG5YmqBDZRJKU_06wFKv5AeheBf8Fp1dhFz5tlVJRdkyQG1HVT2bwjg1D7gt0DkEWEHSBeptiC3hJXf1IEH8QYSdebOTz6MRUyrqLlstr7jvxRDdT8JtDH41M7Jf_CiLQN8ZmHLOfIwGQHCt7kDeIKu8GAyst31CSxy2C5H8wN3JiGdYVbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
آنها می‌خواستند ایران را تنبیه کنند. در عوض، خودشان را با نفت سه رقمی تنبیه کردند.
استراتژی ۱۰/۱۰
👏
👏
👏
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68867" target="_blank">📅 19:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68866">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=LYWBMH5wpDVjnaBLdGBVE_ABJMu27vj8Pt66Xd0Cc31O6LIID_eKUByIK9Z8FmCSuuiFSSyXKvggBGL-4x1blee5RYocDkpJu-dV0OA1dHBzIfzoFHnxS0KlEE0b-ZAYL6qg-YUFMnxNPVK88ToIfbCgFQPrtTZH1CV9L38FXNuhWjI89JTSr2scGMPO85C0EUXKmn4yAbZjTsPSlJCPDfBfw_zkdrkFB8TtGkqHOXnYLPBW7so7c2Az2mBwmeJV6Xg3VGmZh9XZcqnZKwF43JxV__oh9IxJHSvXY_u30McYe-NmOZY1wgmlBN1eubSW39B6jqGyVxXP3EwPXVJ_yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7d5a3d25.mp4?token=LYWBMH5wpDVjnaBLdGBVE_ABJMu27vj8Pt66Xd0Cc31O6LIID_eKUByIK9Z8FmCSuuiFSSyXKvggBGL-4x1blee5RYocDkpJu-dV0OA1dHBzIfzoFHnxS0KlEE0b-ZAYL6qg-YUFMnxNPVK88ToIfbCgFQPrtTZH1CV9L38FXNuhWjI89JTSr2scGMPO85C0EUXKmn4yAbZjTsPSlJCPDfBfw_zkdrkFB8TtGkqHOXnYLPBW7so7c2Az2mBwmeJV6Xg3VGmZh9XZcqnZKwF43JxV__oh9IxJHSvXY_u30McYe-NmOZY1wgmlBN1eubSW39B6jqGyVxXP3EwPXVJ_yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العدید هم که تخلیه شده، بنظرم خودمون رو آماده کنیم... #hjAly‌</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68866" target="_blank">📅 19:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68865">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJxJJK6X0jqqfZ-TTIbqHwR24Ilmq_2U-gbL5BA5mxzbo_6I-tVBg7EUxjKSfTdfizLF8nSP5RPDyAZ3kRZt5RB1EFOISucbPjOBFCpEzB_MGLsbUUdpuRhIKs5ojwMA5hsZoNTFOr8c8ncIybPf-VnYXoC8Kvib8VDr3Pmr0ccroUygdFjvqu--ieVgCbMxMDiFKLA6ZkGxDlKESjdvOXyQsQiZ6X9QYwB4-Im8q_fF3KD7oCL1f1eoFafWQCy-Zrtgup2mgvdyHUXNCsoVlD1txo3E05_7QopjVxh8d4GlMvYscBL3hsHj8y5E-aY3H0CMMzve9KK-7FjheyQeXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین نشونه های نزدیک بودن حمله، تخلیه پایگاه هاست</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68865" target="_blank">📅 19:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68864">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ همچنین گفت:  همه چیز برای این حمله آماده است. اگر از اسرائیل بخواهم ظرف دو دقیقه به ما ملحق میشود اما ما به هیچکس نیاز نداریم.  @News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68864" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68863">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری؛پرزیدنت ترامپ به کانال 12 اسرائیل:   من در حال بررسی یک حمله گسترده هستم - بزرگتر از هر چیزی که قبلاً اتفاق افتاده است. من به تصمیم گیری نزدیک هستم.   @News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68863" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68862">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtWG3_621lfmM6tBHQCej-fEdYS9QKyOsWU0iajAuVtDumXUyuB_8wigD_GzARLGDtfRHw1uO-wJu28Vt6_saY1pQAd4aZjBy5zWkJJ4ygNrMBw1Apvqo0hdvV1z-dnpwDNqBe25Mp1T3EVGl29c6ZNE-Zv-OGlwGJHviNSRQJWYHk82t-1rnNZ5C-1HQpIOWEYwtuZQwEShW7r1uSWY6Zn6pnVFTxb6xvFVG-pcBqTcsEV8UbMjSrwFVpE66b6-ngmwkO-cST2CTxkN7JF-HVouupX8GrmksO_tKpwggiLV9ixQp1fxoKrUWuZbcQ2e-69UucpTaomvHwP1yGs3Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری
؛پرزیدنت ترامپ به کانال 12 اسرائیل:
من در حال بررسی یک حمله گسترده هستم - بزرگتر از هر چیزی که قبلاً اتفاق افتاده است. من به تصمیم گیری نزدیک هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68862" target="_blank">📅 19:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68861">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a86f5d96ba.mp4?token=O3Jox06BI5S9pKvAXLqIQq7dmJBfr8EMRclf_l7KVNnq5E5_8FXWqt5aL0pZKwdO6dE0J0DUtxPXZZnI2Iq5Dh9bwanvGUzIeolE9JWmVtIhRUUiJD4XLn9-TwkzrQOHbHiD64tmzZYU4U7UJgZL58CbpjgZll8OJ8kwFwEXzSvCKbv8HrVETgVFlw0Sqq7dA91165Y_x63mUKW4j9bT_SJO98xxOz4rga4IBA9gh57mRgbqXq3utXaaOiRAVJxWoFioXlZbw4BQdWUX1wSXYHW_TLCXBVUfj8F2vVds1eb-JMnr0-aIoNy9k8zr-Z_qegm-pcdHxEVfL3miSf9Tag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a86f5d96ba.mp4?token=O3Jox06BI5S9pKvAXLqIQq7dmJBfr8EMRclf_l7KVNnq5E5_8FXWqt5aL0pZKwdO6dE0J0DUtxPXZZnI2Iq5Dh9bwanvGUzIeolE9JWmVtIhRUUiJD4XLn9-TwkzrQOHbHiD64tmzZYU4U7UJgZL58CbpjgZll8OJ8kwFwEXzSvCKbv8HrVETgVFlw0Sqq7dA91165Y_x63mUKW4j9bT_SJO98xxOz4rga4IBA9gh57mRgbqXq3utXaaOiRAVJxWoFioXlZbw4BQdWUX1wSXYHW_TLCXBVUfj8F2vVds1eb-JMnr0-aIoNy9k8zr-Z_qegm-pcdHxEVfL3miSf9Tag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
من بلافاصله پس از انتخابات به دیدار ترامپ رفتم و با هفت اسلاید بزرگ به آنجا رفتم.
اسلاید اول، اسلاید دوم، اسلاید سوم، اسلاید چهارم. "این کاری است که ما انجام خواهیم داد."
نه اینکه بپرسیم "آیا به ما اجازه می‌دهید یا نه؟" بلکه من به او گفتم: "این کاری است که ما انجام خواهیم داد." و ما به اسلاید آخر رسیدیم و من گفتم: "این پیشنهادی است که به شما ارائه می‌دهم."
شما بمب‌افکن‌های B-2 دارید – این بمب‌افکن‌های بسیار بزرگ. یک مکان به نام فوردو وجود دارد. اگر لازم باشد، ما خودمان نیز علیه آن اقدام خواهیم کرد. اما بسیار موثرتر است اگر شما بیایید و به سادگی بمب‌های سنگین خود را آنجا بیندازید.
او گوش داد و در نهایت موافقت کرد. من بسیار خوشحال بودم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68861" target="_blank">📅 18:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68860">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3008b12665.mp4?token=eWq7rl7L0-IkL4yTMy_8npe27tMKQFqZTbeGa1FC9VJpqCRM9uoij7lvrioFb4Ja56xYmtpecgNhMP_eBx6qROILgU-5PJfRAt_rAdnkoBt67NQEnZTDfJbYdNOe8KaTtmkApSoIh7dQ93XUFb3t-Bdz9J7YMiTOYyimiu8iKpkCeM-O3QRSA0-QjjV91ek5bShFsrEGhz9gcigM2A5e_UuxNObnJDjZ5qAL7HLYSO8hL1yRyF94kEUEnfRPuYMqDsc4a9b-7ffiFVH7GZFPykBN3rQ8QjZ1Mc3TGLa4hYmmbl9yujlDD8_Rn3DC4u0-iDTvOKdVEtZLNLuMahHePg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3008b12665.mp4?token=eWq7rl7L0-IkL4yTMy_8npe27tMKQFqZTbeGa1FC9VJpqCRM9uoij7lvrioFb4Ja56xYmtpecgNhMP_eBx6qROILgU-5PJfRAt_rAdnkoBt67NQEnZTDfJbYdNOe8KaTtmkApSoIh7dQ93XUFb3t-Bdz9J7YMiTOYyimiu8iKpkCeM-O3QRSA0-QjjV91ek5bShFsrEGhz9gcigM2A5e_UuxNObnJDjZ5qAL7HLYSO8hL1yRyF94kEUEnfRPuYMqDsc4a9b-7ffiFVH7GZFPykBN3rQ8QjZ1Mc3TGLa4hYmmbl9yujlDD8_Rn3DC4u0-iDTvOKdVEtZLNLuMahHePg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
شهریاری:
الان تو دنیا کدوم کشور با ما دوسته کدومشون دوسته بجز مردمشون؟
⏺
ثابتی:
اونام دولت هاشون مثل حسن روحانی تفکراتشون امریکاییه
⏺
شهریاری:
توهین نکن حسن روحانی امریکایی نیست بعدم تو در حدی نیستی بخواد بخاطر این حرفت ازت شکایت کنه اگه تفکرات روحانی رو امریکایی میدونی یعنی تفکرات 80 درصد مردم امریکاییه..
⏺
ثابتی:
کی گفته؟
⏺
شهریاری:
کی گفته؟ اگه جرات دارین رفراندوم برگزار کنین تا مردم بگن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68860" target="_blank">📅 18:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68859">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🇮🇷
هشدار سپاه پاسداران به انگلیس: بیش از این پروندهٔ خود را سنگین نکنید!
به رژیم پادشاهی انگلیس که عامل اصلی بدبختی‌های مردم منطقهٔ ما بوده و سوابق سیاه تجزیهٔ کشورهای اسلامی، کشتارهای گسترده در این کشورها، تحمیل دولت‌های استبدادی و بدتر از همه سازماندهی هدایت عملیات اشغال فلسطین و تشکیل نکبت اسرائیل را در پرونده خود دارد و بیشترین مشارکت را در تجاوزات آمریکا و رژیم صهیونیستی علیه ایران داشته، هشدار می‌دهیم که بیش از این پروندهٔ خود را سنگین نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68859" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68858">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrsrQ3BXFbWIWcG0Z5N7YcpZKj59tfvUS0NRDR2LSNYIboen0HaWfxnAxD19Hw5VrjCYK1LbJvyJTq0aV-EkGuXgEtOoLUb6aKu_cx8-i3xzYPbt0dUt9DnrPENWMBsF86AamBKNaxR97ot4YCTOizD_pUAX3y2boci9GcdOI22oPb3EeA_KRJvVTJzr7iMQGNjBPWkWREmtroJVmKXg5EPu1OmNajPSpkso9_7w-qnNkyMsJqhZUwvdVFEVPZwZ4AH8oBW0kpchXDZw9DkIxA9Ytn1P_I1ueiXPvr1TMjbshvAk3ZC9qR2gHeXZ5bdnQSV3CIaXUxZbrqH1YTnd-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
نفت برنت بعد از تقريبا دو ماه، مجددا 100$ رو رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68858" target="_blank">📅 17:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68857">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgUtaJ9syEcmjDG7YqgZJ9cxRmB47Ay8ssZzjSeRcIDQr4GQU6jDsVv7rT_uCBFZLHYK78U6SyuAT_N35tMm6zsw-YF79GrR7kWZ-BzXpG-XBOhW9-hn3689syA4RABO5UAgWlJxsRefBACc_dGG9JW8rNMGCKRBjOYPXVJv4tJ86p7R4Cb-IuZSdiFihEQFBqbMQKeYEGayXjEKM5ozonvTdUNLY20HsKNZekqhWwTVwFhaLsH7YWI16fzqtrpM_Mx_7ZCqCovNo4qGFqbgkJ-trMnW9G1BcVjMkHJYJaUMl1P5yXBkUam7rG01KzYXVTPMPBoDEiTxJnwqCOF8CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آکسیوس:آمریکا هم‌زمان با تشدید حملات علیه ایران، بمب‌افکن B-1 را مستقر می‌کند.
مقامات آمریکایی اعلام کردند که ارتش ایالات متحده روز سه‌شنبه از یک بمب‌افکن دوربرد «بی-۱» برای حمله به اهداف سپاه پاسداران انقلاب اسلامی در ایران استفاده کرد.این نخستین باری بود که ایالات متحده از زمان ازسرگیری درگیری‌ها با ایران در ۱۲ روز پیش، مأموریتی با استفاده از بمب‌افکن «بی-۱» (B-1) انجام می‌داد.
استفاده از بمب‌افکن‌های «بی-۱» — که قادر به حمل ۲۴ بمب ۲۰۰۰ پوندی یا ده‌ها موشک کروز هستند — نشان‌دهنده تشدید و گسترش قابل‌توجه عملیات نظامی ایالات متحده بود.
هواپیمای «بی-۱» (B-1) می‌تواند در ارتفاع پایین با سرعتی فراتر از سرعت صوت پرواز کند و در عین حال، سنگین‌ترین محموله بمب را در میان انواع هواپیماهای بمب‌افکن حمل نماید.
در بحبوحه تداوم تقویت قوای نظامی آمریکا در منطقه، رئیس‌جمهور ترامپ همچنان بازگشت به عملیات‌های رزمی گسترده علیه ایران را مد نظر دارد. مقامات آمریکایی و اسرائیلی می‌گویند این اتفاق ممکن است ظرف چند روز رخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68857" target="_blank">📅 17:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68856">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d380ae3e6f.mp4?token=IIFRKeb8HRwkvMnIilC3oP86Ia6SuIdnU6C5TntesgJpnZq4QlGJ7gpRQja6Jlqc4Cih0stGq462d3eQGKiZybAQ4sI-4B07YF7F-UZnlblSEi5zX3ekCtCqJl6_8H24Zm0IRUvt-cS2uHEUy-kuVlU40OedVAN2BtnljwVYKKyi_3JcsJv6bmo05ZHk56PtX3ebqi3psEEB-p-BZ49KL7yzdXNjbhqhR9xRcfOxl8I6ImS4T6xOoiJnjUJc8efGnVf2NUlHXw5dbNUio8EHFtzEwgprZ5TAA5cI2_ly6d33NxpCetZ1V7Cjk-m4qJ-Ccz1ZC1jNrl6jDLw1LN-g3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d380ae3e6f.mp4?token=IIFRKeb8HRwkvMnIilC3oP86Ia6SuIdnU6C5TntesgJpnZq4QlGJ7gpRQja6Jlqc4Cih0stGq462d3eQGKiZybAQ4sI-4B07YF7F-UZnlblSEi5zX3ekCtCqJl6_8H24Zm0IRUvt-cS2uHEUy-kuVlU40OedVAN2BtnljwVYKKyi_3JcsJv6bmo05ZHk56PtX3ebqi3psEEB-p-BZ49KL7yzdXNjbhqhR9xRcfOxl8I6ImS4T6xOoiJnjUJc8efGnVf2NUlHXw5dbNUio8EHFtzEwgprZ5TAA5cI2_ly6d33NxpCetZ1V7Cjk-m4qJ-Ccz1ZC1jNrl6jDLw1LN-g3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاره کردن امضای ترامپ هنگام شلیک پهپاد به سمت پایگاه های امریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68856" target="_blank">📅 16:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68855">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:  یک سال پیش، ایالات متحده آمریکا به دلیل اخلال حوثی‌ها در امر تجارت و بازرگانی از طریق تیراندازی به کشتی‌ها، حمله‌ای بسیار قدرتمند علیه آن‌ها انجام داد. از آن زمان و در جریان تنش‌های ما با ایران، آن‌ها بسیار مسئولانه رفتار کرده‌اند. متأسفانه،…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68855" target="_blank">📅 16:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68854">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UeM3txEc-vX9x2r50Jye0wuap6s9tOFTNKsls_iMOb1OEA8wSadZST4Il3_6yPFCyArEbOVmrFhP-tIrnxjvDjja9NznhqoXhkzJZZjqzRbe5DRemN0tA5peqiKLF0mALR2EE6_iJX-AdvO-PA1B5U3t1PExPUd2BYI53qrVWWt_dDtUXrnGYdEhAlRTXQMWMaN8AwLBi-Jz6gkRfRJuB1_tEtANaef4AHY9LgqGOce67o9QxNSgAPNu0Np1XfDrMyxvf0HCBEY8qU1oT4im4Pk8VNq0gbmB6JGR4eaWxFaQIVpPrAmXolVLuvB7n11SvWGAs_2g_rYKcgOVwdlptQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛فرانسه در حال تخلیه کردن کارکنان سفارت خود در تهران است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68854" target="_blank">📅 16:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68853">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkW3WDqRicZ3L0uE3b8sjucpdjF2oWNnYl0n2tFHhMuHxh8MrQzQdGashpX1hEzvPatAMDNGtOAZctPfxFuQzsVzMpy60qtuh-8nmnqVLVxp7Po4iTWvHaOChXP9THIzqVa1d_Mnymx_CKOWrHiqtkmHuocK0ZB1H7KteHr9VrgSyliYzQyUZ3QJtHJHLp8U_8Px2chVtEOBRcGtwTq_RTMLln177CIyIcW6yg-KETFgiz0stXYySJ-PKXJL73vKUwo0nH6v-9LRj0bz9o5ZybQDKwLg1sE07rf4RICTpYK-RI6zAep7srU1pxKmLESj5Mwh2IyevbchC0S_FDXZjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت
ترامپ:
یک سال پیش، ایالات متحده آمریکا به دلیل اخلال حوثی‌ها در امر تجارت و بازرگانی از طریق تیراندازی به کشتی‌ها، حمله‌ای بسیار قدرتمند علیه آن‌ها انجام داد.
از آن زمان و در جریان تنش‌های ما با ایران، آن‌ها بسیار مسئولانه رفتار کرده‌اند. متأسفانه، اکنون آن‌ها دوباره فعالیت‌های خود را از سر گرفته و دیشب به دو کشتی عربستان سعودی شلیک کرده‌اند.
لطفاً این واقعیت را مد نظر داشته باشید که اگر آن‌ها دوباره دست به چنین کاری بزنند، ایالات متحده ایران را مسئول خواهد دانست؛ چرا که حوثی‌ها نیروی نیابتی ایران محسوب می‌شوند.
در آن صورت، تنبیه نظامی سنگینی علیه ایران و البته خودِ حوثی‌ها اعمال خواهد شد؛ گروهی که عملکردشان تا پیش از این بسیار حرفه‌ای و هوشمندانه بود و اکنون موجب ناامیدی شدید من شده‌اند.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68853" target="_blank">📅 15:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68852">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPPSm5ytweGYhatENSTo3iL_Ihu4JulZ14W9xqu9-GUYZFRgteBx0oj4GKKDOvXKlyYXjhK8bUU09E-KwRlIWD97jyeYj-27Cs5JOLMnseB8UD0mRzgmTj9KyfIpFM0xMLi3c3pwKQ-ZF49AwioxRyt7NmCTznW3X0HCom1V8xKJhCAlCnBw30dbkmy-wtDQEoyFVidGPEHq8dgTVrJkD8ihuqE4oa0jIYMcmoLQ3I5VWRmvSpgWpwTiIfT-0n9cJGrVFFUmNyTdTT58248u8nKwkROkQ-VVeBg8mxiebJw3mxyjcYf0IcFPr5WrxKC3U89mGHbL7uH9iPEqerMQcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
توافق هسته‌ای غیرنظامی (که شامل هیچ‌گونه غنی‌سازی مواد نخواهد بود!) میان وزارت انرژی ایالات متحده و عربستان سعودی — که صرفاً به مصارف غیرنظامی، مشابه آنچه ایران و امارات (و دیگران) در اختیار دارند، مربوط می‌شود — تصویب خواهد شد؛
اما این امر کاملاً مشروط به پیوستن عربستان سعودی به «پیمان‌های ابراهیم» است که بسیار محترم و موفق هستند.
ایالات متحده با تأسیسات هسته‌ای غیرنظامی (بدون غنی‌سازی) مخالف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68852" target="_blank">📅 15:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68851">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ed4a8fc7b.mp4?token=X8SN0deVV3Xk-Y7llbZFR6mDi6CN9XvhpnMJd9-85FfnykOOzsibaIWu6BxVWSMByClN_syfGIlnVp9xUIRb1wZS1PWQk9fEExroB7KFDThLgS2sc9UVXowB5oEYbk8UJbe9vQfuAHgbwiPUcO9uEgDjwbt8LXZOZ5-RS81yk4hzrwEI2EyC2cNgJAP5ULJZYhQhhDICqSBpqzDgvJqh4zTavSVAbczAump4YW2zRu3KjDLWf5jp3FFJyTYqLUmUvHlDBxfv6H-LwbRlkdlCvqbIFPYktnbfE_Cw9YL5Q-nmLM_3GV82qSjrbKF_Rn57E3-9CeOf9s2tp2IbBioZ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ed4a8fc7b.mp4?token=X8SN0deVV3Xk-Y7llbZFR6mDi6CN9XvhpnMJd9-85FfnykOOzsibaIWu6BxVWSMByClN_syfGIlnVp9xUIRb1wZS1PWQk9fEExroB7KFDThLgS2sc9UVXowB5oEYbk8UJbe9vQfuAHgbwiPUcO9uEgDjwbt8LXZOZ5-RS81yk4hzrwEI2EyC2cNgJAP5ULJZYhQhhDICqSBpqzDgvJqh4zTavSVAbczAump4YW2zRu3KjDLWf5jp3FFJyTYqLUmUvHlDBxfv6H-LwbRlkdlCvqbIFPYktnbfE_Cw9YL5Q-nmLM_3GV82qSjrbKF_Rn57E3-9CeOf9s2tp2IbBioZ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو فروند هواپیمای «EA-37B Compass Call» صبح امروز وارد پایگاه نیروی هوایی سلطنتی بریتانیا در «فِیرفورد» (RAF Fairford) شدند.
این هواپیماها که بر پایه بدنه «گلف‌استریم G550» ساخته شده‌اند، جدیدترین هواپیماهای جنگ الکترونیک نیروی هوایی ایالات متحده محسوب می‌شوند و مأموریت اصلی آن‌ها مختل کردن شبکه‌ها، رادارها و سامانه‌های فرماندهی و کنترل دشمن است.
در حال حاضر تنها
پنج فروند
از این هواپیماها در خدمت عملیاتی قرار دارند و قیمت هر یک از آن‌ها بیش از ۳۰۰ میلیون دلار است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68851" target="_blank">📅 15:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68849">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-oD9LKmE9mtc9h9uqeU-_ZcyGA6_d2NltWHL6uNz-uW2jmN4meiGuzAHg-ChF3mnoy21d6Q-J75CFYnrGJyfNudcmZFio0xbhVz4_h0RsUvE5GEBZZs5ga1K3C3SfL-xlZh8kuBYDZ9s6xeqZCOiwATlxEv14UtpYXLea9-fiQZUceCe_zJV66yHk65uYX2S5wu0KjPMutjSmxUOzacTscaPogqaVBV6pj2mDR0a10bt28pPq-zyHySSBI_tQEX1GIzgjD4998Hrtbl-OB6nTe21-qod7Eyyol04bUpATkVe1KNV3QZa5GGrDokSaasCH9TN9g2QYNEYd95dUop7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c87fead2.mp4?token=pEMFrMSNTbI4hn1ZCS4WvA1OOmmjyAYcTZgHbNSCx2QQ4Di3rRFwU94tyOUPh3eHrDfcaLor8MruwCd5MNRsTb1JbsWr6Fouy8LfRwf3jiTYBMjd9W-EIh5E2ZdUE47ff65mVMxNmn9I5sGwwOOKakizU1QTTIInCwyR5SlbcjsR8r8uOOLzUYw26jkY5ySGHhpTQWZ_l-gozjUbHv1n1dYKCTf8zMfE0P7ieqIDCTefZCrJWkgzhphi6q-x7C6xhJeSY8AFkQwYtR2-EvqUhGIQvEUapp_8dx9-myUrjzwgUL_lCvB0Cd6OY7x8i0XialSx92xH7eYcM7ooWh9OW7ISdhWPESUac4wS50Ayef5mgwM4P2x_vpNySKarOZn0OFqYuvdzVyc3xyVhtZ3E8424XzUlTB6ru0tIDq5u_YOOKnsu4HcgPPzXU4TaSGc3bg-j2e1J9eZv7qZrrxeMkFfzINSugn-mebcMyrITGVdZQVMfWktLzRckLOchco5AaBPhxfQ4iCBM_6r2wvsm9bYBnJRKi0g27NhxRI-MkzctodBoKmfaZ2CcFBHZtbQI1tgdm6BMy7xRHyscoe_MxDzoemK0JMHF27eJiWJpWOCpk52KBlV9MFFiJNbBXUYkIEPxVFEwi-5aVLEB0RUQYzaYSSHuVtA7FbbVso7qYBs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c87fead2.mp4?token=pEMFrMSNTbI4hn1ZCS4WvA1OOmmjyAYcTZgHbNSCx2QQ4Di3rRFwU94tyOUPh3eHrDfcaLor8MruwCd5MNRsTb1JbsWr6Fouy8LfRwf3jiTYBMjd9W-EIh5E2ZdUE47ff65mVMxNmn9I5sGwwOOKakizU1QTTIInCwyR5SlbcjsR8r8uOOLzUYw26jkY5ySGHhpTQWZ_l-gozjUbHv1n1dYKCTf8zMfE0P7ieqIDCTefZCrJWkgzhphi6q-x7C6xhJeSY8AFkQwYtR2-EvqUhGIQvEUapp_8dx9-myUrjzwgUL_lCvB0Cd6OY7x8i0XialSx92xH7eYcM7ooWh9OW7ISdhWPESUac4wS50Ayef5mgwM4P2x_vpNySKarOZn0OFqYuvdzVyc3xyVhtZ3E8424XzUlTB6ru0tIDq5u_YOOKnsu4HcgPPzXU4TaSGc3bg-j2e1J9eZv7qZrrxeMkFfzINSugn-mebcMyrITGVdZQVMfWktLzRckLOchco5AaBPhxfQ4iCBM_6r2wvsm9bYBnJRKi0g27NhxRI-MkzctodBoKmfaZ2CcFBHZtbQI1tgdm6BMy7xRHyscoe_MxDzoemK0JMHF27eJiWJpWOCpk52KBlV9MFFiJNbBXUYkIEPxVFEwi-5aVLEB0RUQYzaYSSHuVtA7FbbVso7qYBs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وقوع انفجارها در گذرگاه مرزی «عبدلی» میان عراق و کویت، در سمتِ بصره (عراق)
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68849" target="_blank">📅 14:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68848">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaCLlzyE8BEZ6EeUGlf8Q8utM0SsJwQh2FkXFuiGgms0fQikONSl0ogStxa-WCPPKJJ0udTulCkYUatMI4GR-UD7psBeHiBJVFPVkpeSFSRJDQaPNEmmeV1cSbgjjVmEnWMfczlEDavgTHcX9x6hKK2R2kX0X0l1i4TB_iMlpFaT9a2_TS_pc0tuB0JTJ1sjBEm8MoEmiYY2tWJ70Ii-ppkKFYBECHMbC9WL9UrvNkeKCtzyhLS_cKgUyueqFXnw3wBfV3hV2wIj3RdW73zvXFLfcWBn5xWE6Eif1SlML5l7zOXYVVEvw2zg7dsED6xDgWO8qLsf1XVW3LQ9PCd5FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابوالفضل ابوترابی، نماینده مجلس:
دولت مسعود پزشکیان با ارسال ۲۸ نامه به مجتبی خامنه‌ای، رهبر جمهوری اسلامی، برای مذاکره اصرار کرده و او را «تهدید» کرده است.
قالیباف و پزشکیان در «تله مذاکره» افتادند و «باید به عقل هر کسی که الان حرف از مذاکره می‌زند، شک کرد.»
اگر جمهوری اسلامی «دو هفته دیگر جنگ را تحمل می‌کرد»، آمریکا و دونالد ترامپ، رییس‌جمهوری آمریکا، پیش از آغاز مذاکرات «همه خواسته‌های» جمهوری اسلامی را می‌پذیرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68848" target="_blank">📅 13:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68847">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d3c9fc2c.mp4?token=XoCg3kccOv4wGbqBtZTC_R4aOp2b8ZgfRpmDiw-5zrFWGqxNSoT9T3kd3D_PcBugBTuuMkD8B2sgOHGqG_PyiGegKukdkHHA1xuKaanB6NW2KOZV4InG-oNc0QR7KwsQBQS7kz6Hdzpnqcd7Wwd8VSql-bVhXkibBoG4qFS7qMosapdzXcSg7U57WwuGowc4z8u9cAr52b2Z7Z7V_VHg6XW-B-ZVmP76q16zKUg0sYBy0VolKgOrVvZlZGNdMjHAVsTiLPjc_4O9IhJCKhK4HKtPxnXow6VLQHiHdDRu74jcKQI5RvIGZF8TnTc_gNpjSvOM7EuMXtaBLYTIUVupMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d3c9fc2c.mp4?token=XoCg3kccOv4wGbqBtZTC_R4aOp2b8ZgfRpmDiw-5zrFWGqxNSoT9T3kd3D_PcBugBTuuMkD8B2sgOHGqG_PyiGegKukdkHHA1xuKaanB6NW2KOZV4InG-oNc0QR7KwsQBQS7kz6Hdzpnqcd7Wwd8VSql-bVhXkibBoG4qFS7qMosapdzXcSg7U57WwuGowc4z8u9cAr52b2Z7Z7V_VHg6XW-B-ZVmP76q16zKUg0sYBy0VolKgOrVvZlZGNdMjHAVsTiLPjc_4O9IhJCKhK4HKtPxnXow6VLQHiHdDRu74jcKQI5RvIGZF8TnTc_gNpjSvOM7EuMXtaBLYTIUVupMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظه حمله آمریکا به حوالی بهبهان
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68847" target="_blank">📅 13:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68846">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwzRSfOY6MZP1nOl86ehF9_2WOfPagd01oKEO-Y1m9-fH1_7-vFtuDxPruT-sHTx1iK3dL-BDvcfsoCmv6lFQB7siecCycpXCFXepZikvCZmXD43_yyWJwO57gxJNaghjHelW6mF75JDlwokza7g2q69F587ArYBmgm5ARY2oqbnTJLL4rz94UMepsYYuwFTxz5WbtwB3T7tlL92Vgx7WOolkCGtPdAeELksaKkWqui1Lko6Y_4HzPq0-yp3MT5ka1NskqbTqgD3p-h47iTpNh9n5GHYLuJvzws2DGJwDxto8wqZ_7Zz9gwmHxPW-quzBskNob-37YOBafuvAWlsdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68846" target="_blank">📅 13:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68845">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇱
شهردار «رامات گان» در اسرائیل:
«ما تصمیم گرفته‌ایم تمام پناهگاه‌های شهر را باز کنیم. ارزیابی وضعیت نشان می‌دهد که خطر حملات موشکی از سوی ایران در تعطیلات آخر هفته افزایش یافته و دیگر ناچیز نیست؛
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68845" target="_blank">📅 13:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68844">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c953cd20.mp4?token=JBavHh_vv6JCFceqL1dIR2VTFJHXjK6MVxtmIdSJcz1XSWLKNGCkStn5GCRig2NuoqmQtppWMPSM09bmSFrVd9g3E4iavF1On1W2Soujbdu5nKT0GyCiTBIskgdliqjze1-laKmUfYQRP5WVaVk2KcZtOkMHdtfkGZ-a32yf060GAI_4BhQw_qcSuu7mQtPxueuxWFQBH28RSd7uCZUg9KKwURb8D2Q-g007Ti1hB4vXiTp_3YAZFobmYr308EXP3fM6YmfkW9NdG9eFY5PgPPEhoX2VfgRnSOR2L0Ipo2jxReX_UPfHB6Vv5VEQ5oAGjQl_r1xysCbbjtbMyxjSfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c953cd20.mp4?token=JBavHh_vv6JCFceqL1dIR2VTFJHXjK6MVxtmIdSJcz1XSWLKNGCkStn5GCRig2NuoqmQtppWMPSM09bmSFrVd9g3E4iavF1On1W2Soujbdu5nKT0GyCiTBIskgdliqjze1-laKmUfYQRP5WVaVk2KcZtOkMHdtfkGZ-a32yf060GAI_4BhQw_qcSuu7mQtPxueuxWFQBH28RSd7uCZUg9KKwURb8D2Q-g007Ti1hB4vXiTp_3YAZFobmYr308EXP3fM6YmfkW9NdG9eFY5PgPPEhoX2VfgRnSOR2L0Ipo2jxReX_UPfHB6Vv5VEQ5oAGjQl_r1xysCbbjtbMyxjSfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
عراقچی می‌گوید سیاست آن‌ها "چشم در برابر چشم" است.
سیاست ترامپ "سر در برابر چشم" است.
آن‌ها بهای بسیار سنگینی خواهند پرداخت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68844" target="_blank">📅 12:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68843">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1p-CcSrzfWu0Nm4ywDiX-qDjyR1TTG8yVaDuPY3kSHpZrN4CbM3znjhRuwDz2PXEL2x5ZwvRiyV9p6baEMRzc7xZ5Gc1-GJpmA6QgVqFR3Dj7VQ8rIJsaTUHlsExRbxzvtbU2F3w5_KRH1kZZaOt88K6zI63yU_veA5wc-AHrrn8ITfI0U2kMAfF5opgU_cEaAs2YiH3MJQmfBuQkn-gV7Ud5g6s2asrEwFeTR0Xa1s3sRIxJXaSde1LvF6g0I8-xFMHfFo6okf28jvgyvLIckEwmHE2KRBPSvxV-l5lxMO9w3Al6mdRdm1qwBjy1LyYdNpQJFoB9HJHUESu4wg5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پایگاه دریایی ارتش جاسک که صبح امروز مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68843" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68842">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c812fbcc36.mp4?token=qUHK1fYNeuw5AJd2gt1wppJpKFhqjBM36ag-HxDqX2H9UjFVM7oS4uGsr3tN3nOka4bv8sI1FRqCBpidh_c4XDVuvZ9tmRDjYIFAVSa-hccgna_cNF8NcOwF2g4pMXlWyHbX0JK3DFltR0p_5XwEBA2tyei5A5LT_gwnkQ2vuEKmeFVNp12sbn_0jwieHlfzlzDvjkPGnat8sXeuuDWefDOrUBDy7LKo9zbV289axP3-1X07g59tbFz4hlTsyXicMEBGolLyDAOE8XzzUpXVSFQpeGRVenXA3CbAKjK4g9RV9bpxmd2vs5OEavIxa3yY9skt8hxHeFazS2UYWA5BlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c812fbcc36.mp4?token=qUHK1fYNeuw5AJd2gt1wppJpKFhqjBM36ag-HxDqX2H9UjFVM7oS4uGsr3tN3nOka4bv8sI1FRqCBpidh_c4XDVuvZ9tmRDjYIFAVSa-hccgna_cNF8NcOwF2g4pMXlWyHbX0JK3DFltR0p_5XwEBA2tyei5A5LT_gwnkQ2vuEKmeFVNp12sbn_0jwieHlfzlzDvjkPGnat8sXeuuDWefDOrUBDy7LKo9zbV289axP3-1X07g59tbFz4hlTsyXicMEBGolLyDAOE8XzzUpXVSFQpeGRVenXA3CbAKjK4g9RV9bpxmd2vs5OEavIxa3yY9skt8hxHeFazS2UYWA5BlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوای ناموسی در پخش زنده
😃
⏺
امیرحسین ثابتی:
نباید تنگه رو از دست بدیم، نباید تنگه رو بدیم بره. شما می‌ گید تنگه رو باز کنیم، مفت بدیم بره.
⏺
شهریاری، عضو کمیسیون امنیت ملی مجلس وسط پخش زنده :
بدید برررره، تنگه مال ننت بوده که بدید بره؟
مال عمه‌تونه؟ مال کیه؟ ارث باباته؟
⏺
امیرحسین ثابتی :
آقای شهریاری ادب داشته باش چرا وارد بحث ناموسی میشی تو پخش زنده...
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68842" target="_blank">📅 11:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68841">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1ee66466e.mp4?token=D86vfmzsBAomSUI_PIBbnU1n4FUtEJkrTZlAuB4QqB28kER3rgJqLnBr6Ix-7Sv3ntpLqy5-9_o8g59YdtQhKkmPs95a0ytnCuQyzWJ-1mggSz7nABTvXwI_7ZOHFv1G7cuOpogq-CBg5ks3I0mYq-T0a4t8bkYiMHJZWp3fNtOfVwGyKEWX0A_1eHIXM5QkeiT-0ArKq_Y9ipWd4RA6B39e9rl4zzYzjuAzXiHMjWSiF22AD8qYj7OPzXVaicm4JPWS5AoR4FW0vXoIwKFKNG0zJzqttRCdaYzraTnt69froVSm05uhAA0wUvzRiNeIOpVDidalrok0uo5Zk0otn4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1ee66466e.mp4?token=D86vfmzsBAomSUI_PIBbnU1n4FUtEJkrTZlAuB4QqB28kER3rgJqLnBr6Ix-7Sv3ntpLqy5-9_o8g59YdtQhKkmPs95a0ytnCuQyzWJ-1mggSz7nABTvXwI_7ZOHFv1G7cuOpogq-CBg5ks3I0mYq-T0a4t8bkYiMHJZWp3fNtOfVwGyKEWX0A_1eHIXM5QkeiT-0ArKq_Y9ipWd4RA6B39e9rl4zzYzjuAzXiHMjWSiF22AD8qYj7OPzXVaicm4JPWS5AoR4FW0vXoIwKFKNG0zJzqttRCdaYzraTnt69froVSm05uhAA0wUvzRiNeIOpVDidalrok0uo5Zk0otn4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
دعوا بالا گرفته بین قالیباف و افراد افراطی!
🟡
الله کرم رئیس گروه فشار:
بهتون اصلا اجازه نمیدیم به هیچ وجه اورانیوم بدید بره.
🇮🇷
مشاور قالیباف:
به عنوان کی داری اینو میگی؟ نماینده مردمی؟ اندازه حزبت حرفت بزن زیادی نگو.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68841" target="_blank">📅 10:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68839">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ebdcc84e7.mp4?token=UzyNjc0MSbgvlintsZWpT3cpt7laxrXV0YrthH15TZ9LKqIax10oJHhwS1iqPZ_MTe0ejADVWalc13BP30bwAjvs9QWr5LArYfsdNs2FDNLtesvjNFLqSmftHnrW9n3reiTl5g606Vag6A5_LI8VcqpDBFlgLHJZvpvbhHo66K1Z0-lEhgaEWSZWzAHnRp1JgZw9q3izkKhVuOqPe8W-kKTTUW0SzmJjVs-eoRPVYUOFXyokp56MbW2qjOBSQ_KzAhUZjVepb63XuERnLvxkgUtT5g9g2CaK9lBExuaNPQW315NL8KDTPpSZSH9sDyW1Z5nyc03-uAC9osgIVA5aKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ebdcc84e7.mp4?token=UzyNjc0MSbgvlintsZWpT3cpt7laxrXV0YrthH15TZ9LKqIax10oJHhwS1iqPZ_MTe0ejADVWalc13BP30bwAjvs9QWr5LArYfsdNs2FDNLtesvjNFLqSmftHnrW9n3reiTl5g606Vag6A5_LI8VcqpDBFlgLHJZvpvbhHo66K1Z0-lEhgaEWSZWzAHnRp1JgZw9q3izkKhVuOqPe8W-kKTTUW0SzmJjVs-eoRPVYUOFXyokp56MbW2qjOBSQ_KzAhUZjVepb63XuERnLvxkgUtT5g9g2CaK9lBExuaNPQW315NL8KDTPpSZSH9sDyW1Z5nyc03-uAC9osgIVA5aKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حمله دیشب آمریکا به پاسگاه مرزی شلمچه
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68839" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68838">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q_dbCqNUoaCuIpGPiLxKX8U8Y1Jfz6Y11-n9r-acrgminku6VhGWoyMDxbWf7fgj63A3F5FxjAwqF8Va-LFJsVzfZOIgROA0qdS16Ukij2Ujkq-DMVFXmpRDbiOWvewQH08pfu4mZYEBxvKeMKJUy0yN_E4qxSSPCCJf93_3YprExXgSzUwmJXY6ddVk2ZtYCnI-50KI15XOKvMekynUj4x4g3eWnoACGY0aNXc5bnl2Cdr1sfid0QvLrUjzw98yHlcmhVEzCxh9mCVrF6rDLmGURVZvo78bETcVxTex5iyJMrgKZTdvW93ZI47chReisuHxH5-HPNgKc0recZ8jpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عکس برگه صحیح شده یکی از دانش آموزا که امتحان نهاییش رو 0.25 شده!
در جواب تمام سوالات نوشته:
با این مملکت درس خوندن جواب نمیده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68838" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68837">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYvJ3Zn-7dYUzwnuZ390YESEHW8ZowdUq6mmmz9qWdHdBKbCFc_z5bTxGoSc0B1oiyi3hcOv8EGMgJZJ11eOziMbynCTn-hfyEJxt_5lYw8bfoNISwv8Z8AyIpfSUGFr5APm2s38gnK0aGsPEDR_GAEHThlqzZu84GloNbkfB7tfeZX0o2j8gMR2avJGqWIXA65w5OA4dwax8RqWuaIN3uMFfGpWDk_6fGJuvS02Z8L_5_lLEwjFP1Uu63sgCxXC_7i6zRvvgF7K24RCAJesQZPZt9DsZ4A0fFHI0d1PB3avhOA0NY2Rd746P-03nlJ7nAkyCcrdyCWNQMAjCfWdpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
👌
وال‌استریت ژورنال: ایالات متحده در حال اعزام گسترده نیروها، کادر درمانی و تسلیحات به خاورمیانه است تا در شرایطی که رئیس‌جمهور ترامپ احتمال گسترش درگیری با ایران را بررسی می‌کند، گزینه‌های نظامی قدرتمندتری در اختیار داشته باشد.
به گفته مقامات، ایالات متحده طی روزهای اخیر پروازهای باری را از پایگاه‌های محل استقرار نیروهای عملیات ویژه به مقصد خاورمیانه انجام داده است. نیروهای عملیات ویژه در مرحله نخست جنگ موسوم به «خشم حماسی» (Epic Fury) در عملیات‌های رزمی جست‌وجو و نجات به کار گرفته شدند، هرچند توانایی اجرای طیف وسیعی از مأموریت‌های دیگر را نیز دارند.
به گفته برخی از این مقامات، بمب‌افکن‌های دوربرد نیز در حال آماده‌سازی برای انجام عملیات‌های رزمی بزرگ هستند؛ از جمله بمب‌افکن‌های «بی-۱» (B-1) که هم‌اکنون در بریتانیا مستقرند.
وال‌استریت ژورنال پیش‌تر گزارش داده بود که ارتش همچنین هواپیماهای سوخت‌رسان، جنگنده‌های «اف-۱۶» (F-16) از پایگاه هوایی «اسپانگ‌دالِم» در آلمان و جنگنده‌های رادارگریز «اف-۳۵» (F-35) از پایگاه هوایی «لیکنهیث» در انگلستان را به منطقه اعزام کرده است. اردن و اسرائیل به عنوان میزبانان احتمالی این هواپیماها در نظر گرفته می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68837" target="_blank">📅 09:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68836">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⏺
فرماندار بوشهر:
روز چهارشنبه، یک نیروگاه در مجاورت نیروگاه هسته‌ای بوشهر در جنوب ایران هدف اصابت موشک قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68836" target="_blank">📅 02:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68835">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a493fb75ae.mp4?token=FgAuqs8UPsk_rpSdJPiXZxRRaLnb3pMBDn_HXrQbFN03aD_WNxQ_1A57DSD7RZnCj57eOD5WaUIJan40fkYrXA2gYvUnx61l_n-jtOCU49FemnnFCCyxGLYx4wv8zBYGurKIBh36Z77HZIDFYXSgPknktd7PL2ccqqyvsTCGE-1t4MwLYV5Ezl2GHLQ97v4RHwTcIPz-JB14fTpOh1tM3hbJAWeCD82Hn6Ma9HRpF8-znlSqzxDZZcust7sbxMqdskjlbdA9CRPBzC_rSdY2IcQ9wKr1kD_xsrG_a1pV1YwjkxOrCx7JeGhXrcn9aYImJvX03g2VvWrlyCtnmzKl7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a493fb75ae.mp4?token=FgAuqs8UPsk_rpSdJPiXZxRRaLnb3pMBDn_HXrQbFN03aD_WNxQ_1A57DSD7RZnCj57eOD5WaUIJan40fkYrXA2gYvUnx61l_n-jtOCU49FemnnFCCyxGLYx4wv8zBYGurKIBh36Z77HZIDFYXSgPknktd7PL2ccqqyvsTCGE-1t4MwLYV5Ezl2GHLQ97v4RHwTcIPz-JB14fTpOh1tM3hbJAWeCD82Hn6Ma9HRpF8-znlSqzxDZZcust7sbxMqdskjlbdA9CRPBzC_rSdY2IcQ9wKr1kD_xsrG_a1pV1YwjkxOrCx7JeGhXrcn9aYImJvX03g2VvWrlyCtnmzKl7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
#فوری
؛مجلس نمایندگان آمریکا لایحه سیاست دفاعی ۱.۱۵ تریلیون دلاری را با اختلاف آرای اندک (۲۱۶ رأی موافق در برابر ۲۱۲ رأی مخالف) تصویب کرد.
این طرح شامل 95 میلیارد دلار بودجه نظامی اضافی است که عمدتاً برای تأمین هزینه‌های مرتبط با جنگ علیه ایران در نظر گرفته شده است.
این لایحه اکنون برای بررسی به مجلس سنا ارجاع خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/68835" target="_blank">📅 01:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68834">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HL0FAHN3obIsbjahlQZhqEPiwlFKwbOQ6-r989gWLqPbBEvsU8Ph6fo1wcwP1LGkxHXQ73sY-e6zhp8bs-31fhK6wgiVQV_VmAB5RslcPilRxz7wWAamoIN3GKq_b6AhWABAfQOLdrOTMCoKlmGhqzXa8D9DaRyppHR8O8PbnL8ezNzdD9VBZs7EHIEd1SL03lILdccyckHu7kiFAQYeWx1vkpQ7ZDPnEm274-NyK3yOcHg7l3nDC7ukzVIk1gZJEm-Xs4IWu-_eBk03DD0MM7TGc29DPDO17r1ZZ_qKE9vhw8b_WiIcbd5lI_eVP3uHUxPZjv0T-T-YUdd8lAjO9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
ستاد فرماندهی مرکزی ایالات متحده (سنتکام): امروز ساعت ۵:۳۰ بعدازظهر به وقت شرقی، نیروهای آمریکایی به دستور فرمانده کل، حملات بیشتری را علیه اهداف نظامی ایران آغاز کردند.
این مأموریت با هدف تضعیف هرچه بیشتر توانایی ایران در تهدید دریانوردان غیرنظامی و کشتی‌های تجاریِ در حال تردد در آب‌های منطقه، ادامه خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68834" target="_blank">📅 01:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68833">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛سنتکام از آغاز دور جدید حملات علیه ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68833" target="_blank">📅 01:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68832">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🇮🇷
هم‌اکنون حملات سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68832" target="_blank">📅 01:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68831">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSeLnltSdflPwb8TAF6Dlt73CMRIgQoEwBAIlMLLLA-30ptHLAa3ck7WZeW0ae9hWG924zx9-tz1gjwi4i2d7MszNCRu2xVqFx7ny8po6gRMNO72StXg-l8I35cgE0v4FpisUeqG0o7GfYz-6kooiI1SdDE2bjKpneLHKfNZt_Py-6K-9QiAsSJ4qPzY6uahqCSUDo-XTXVWA-gtlkQvAJdM8vL0QmCUyEyFWhKegudzx2HrSSFkQNogddRipOS7LYRSM6xW1Z1W5ZHG5NY4BckkDbksm6G6szxIhmVsAvU_6g3Azz-O9jOuM2Za3UJn-2AxR-5srSFG7140Aaatew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نقاطی که امشب تا این لحظه هدف حمله قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68831" target="_blank">📅 01:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68830">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eimrSLoif6y6TKYL-HQx_r53W8sOn5LAx_K6BuUm4GoZ9mJi490I29y5Hlj4QlKtX1afufk2Zf-Aei82iGt2HtKEt_tDpbK0A-56G0dtQ1eDDCItI1Ph0swpqtphVVsvtDvGR2CEJCkUzzVfQ7_DD9C-y8GQtP_tvpjVfTlc0A5SxW5zyxFsXegy-aUpd7KbnDexA2VkWh9M6B5xIlhxrbOgnjno0AF3jyTieeGqT5adJR2yvJSOYtRDpjaKWqZc-vCvLiRvFepv_FC32l6lzFtbZCh3sKgD6zmAp7QhS0i9SNwaWJ08bF8zJf8sDsLQBdQeD3MSxvH0LBJG9rWyJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
برخی منابع از حملۀ موشکی به یک کشتی نفتی در نزدیکی شمال مرز یمن خبر می‌دهند.  @News_Hut</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/68830" target="_blank">📅 01:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68829">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30afc95033.mp4?token=CSTheU5LgAFO7ZBzDxh7zIIb_gefs-ukhZCBZWAhCuWLqLBbAKE1YjoHpqDDMJ7QhdVpHCmO_nk0nqlU1st3qH4880X5wj_rg6M9epPNdt9NCZD8C82347qaxn3seSGFzo_APfwXdmtJpNR5O9HdEViuqQ2Ezuc67w4YwkKwfPU4P5IaotXc7rmfmlc3gZo2XQd4SRvSb0kObkoaX_mr8oM8L9C0X8nEEk4pIoEWusDkwktqKxSXm-jHJpAN9W8NJ-mM8-FWsGmB1vC9KO6Uo08OhEYLy5uBRr2TlsKy446eJs2uimf7VTDDSScY00XS8IlnHOFFBfDlFPQ_aGqpdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30afc95033.mp4?token=CSTheU5LgAFO7ZBzDxh7zIIb_gefs-ukhZCBZWAhCuWLqLBbAKE1YjoHpqDDMJ7QhdVpHCmO_nk0nqlU1st3qH4880X5wj_rg6M9epPNdt9NCZD8C82347qaxn3seSGFzo_APfwXdmtJpNR5O9HdEViuqQ2Ezuc67w4YwkKwfPU4P5IaotXc7rmfmlc3gZo2XQd4SRvSb0kObkoaX_mr8oM8L9C0X8nEEk4pIoEWusDkwktqKxSXm-jHJpAN9W8NJ-mM8-FWsGmB1vC9KO6Uo08OhEYLy5uBRr2TlsKy446eJs2uimf7VTDDSScY00XS8IlnHOFFBfDlFPQ_aGqpdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
برخی منابع از حملۀ موشکی به یک کشتی نفتی در نزدیکی شمال مرز یمن خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68829" target="_blank">📅 00:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68828">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
صدای دو انفجار در بوشهر شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68828" target="_blank">📅 00:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68827">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
فارس:
حملۀ موشکی دشمن آمریکایی به یک سولۀ انبار آسفالت در اطراف رامشیر استان خوزستان.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68827" target="_blank">📅 00:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68826">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWhGo3xkbWJHiZuYDXRlkA2DwFSuMYZ7X9S6r4NG5iJxrz2G66FotG9CUZRpZUyu2hCyh3h5vFWtBfyZTOV4MMYehGGLAztwOa3hGqEfBPRyd30yNE12AB2wzejVHJe1-3IBTLTBuVv1_Q4ChPaUbB6QZXUS7lWH-rvbrRhU_nY5KovJOtSIPBSjD20CAYEy7z8Aa7ByAYzSFWhJ4DgEibDFm4DHwHqAreHKXXKFvuGFcWeIejyD0V0dLLThHaDAKzbTweWQPrNNEWX0DC6MAUGLbbpfgekgn3Rrbqj7Ua-YG6phwulofHYRfoLzkXd_jhH6QnM9B-ENP-PTFlq7Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
یک جریان مداوم از تجهیزات هوایی آمریکایی به سمت خاورمیانه در حال انجام است، که احتمالاً شامل هواپیماهای تانکر سوخت‌رسان نیز می‌شود، در چارچوب آمادگی‌ها برای تشدید عملیات نظامی علیه ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68826" target="_blank">📅 00:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68825">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
پاسگاه دریایی زیارت در سیریک هدف اصابت موشک قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68825" target="_blank">📅 00:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68824">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
دقایقی قبل صدای چندین انفجار در اهواز و ماهشهر نیز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68824" target="_blank">📅 00:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68823">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
صداوسیما:
چند دقیقه پیش، صدای انفجاری در منطقه بمانی، واقع در شهرستان سیریک، شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68823" target="_blank">📅 00:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68822">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/030860acf9.mp4?token=ksYTvJgXGU2Evgcc6QYSzrBfJ1IbR12_0bYNNZJkrGYKNJYH5-eTY7jaRUe9lKIB87kfjL1TAUrFA7BXS5ZP3X-UlzRC7MptQBD_01G7Xuyr3332ymtBeUf4taSryt2fNrJOU59LB04Iw_0ChAJLdRf7EnJdJ3aq88cF6t2sCW9tdz-k_gsjm8t-xjjb07aB1bkpkEtreU-uv0-Y5fiOCJ3j1WtVG7_GdJzZht65sWARFXH2Rh7w29wmpoIlTAQg0g98NKs7Vt7rmKG8B-4G5Z-vmlxTLykvC0cwrFWLikBNK2SRXA5jf-HJH0H6a5MSA0OiA41G7wwM2NpWMGuSwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/030860acf9.mp4?token=ksYTvJgXGU2Evgcc6QYSzrBfJ1IbR12_0bYNNZJkrGYKNJYH5-eTY7jaRUe9lKIB87kfjL1TAUrFA7BXS5ZP3X-UlzRC7MptQBD_01G7Xuyr3332ymtBeUf4taSryt2fNrJOU59LB04Iw_0ChAJLdRf7EnJdJ3aq88cF6t2sCW9tdz-k_gsjm8t-xjjb07aB1bkpkEtreU-uv0-Y5fiOCJ3j1WtVG7_GdJzZht65sWARFXH2Rh7w29wmpoIlTAQg0g98NKs7Vt7rmKG8B-4G5Z-vmlxTLykvC0cwrFWLikBNK2SRXA5jf-HJH0H6a5MSA0OiA41G7wwM2NpWMGuSwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه روز پیش که پل کهورستان رو زدن ، سریع اومدن یه جاده آسفالت از رودخونه خشک شده اونجا کشیدن که رفت‌وآمد متوقف نشه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68822" target="_blank">📅 23:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68821">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b162fcc101.mp4?token=cKQAqFLyPD0yRIKmumPg50Y3oNjhkzM3ZpMYJoQNCpuTFamBwDsw-Wvp-ucozkb7j8_u3aRFODskUghWbQIjC0QcEraBiUhPu3hJ6Qj1_h4MdZoaZC-8k8XOfFiMYKeM7LyB7LXvxKHd993haIyyeMtsX3IJ9tpbNCbbSEcyd9HzNl90uxhAFkM6-7K-Gb9ZNuPse0oKbjmEHl5Y6zBvCweH0pt4jDCmf3C9UjVA5e-j44g2vPA5DQm6buhpy4pBOr0-RhPpYOBkuLxGfyWUGGKE1OtrFkmoGedQk935AeOIPVLNOXT6zD4EixjdFAy6NL1EryVq_6uXvNq9RJLjlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b162fcc101.mp4?token=cKQAqFLyPD0yRIKmumPg50Y3oNjhkzM3ZpMYJoQNCpuTFamBwDsw-Wvp-ucozkb7j8_u3aRFODskUghWbQIjC0QcEraBiUhPu3hJ6Qj1_h4MdZoaZC-8k8XOfFiMYKeM7LyB7LXvxKHd993haIyyeMtsX3IJ9tpbNCbbSEcyd9HzNl90uxhAFkM6-7K-Gb9ZNuPse0oKbjmEHl5Y6zBvCweH0pt4jDCmf3C9UjVA5e-j44g2vPA5DQm6buhpy4pBOr0-RhPpYOBkuLxGfyWUGGKE1OtrFkmoGedQk935AeOIPVLNOXT6zD4EixjdFAy6NL1EryVq_6uXvNq9RJLjlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ما به تنگه‌ها احتیاجی نداریم؛ اصلاً به هیچ‌کدومشون نیاز نداریم.
ما نیازی به تنگه هرمز نداریم، اما مجبوریم این کار رو انجام بدیم، چون نمی‌تونیم اجازه بدیم ایران به سلاح هسته‌ای دست پیدا کنه.
من اسمش رو جنگ نمی‌ذارم؛ یه درگیری محدود بین ما و جمهوری اسلامی ایران.
اون‌ها اون‌قدر تحت فشار و ضربه هستن که می‌خوان توافق کنن، ولی به نظر من هنوز آماده توافق نیستن.
الان هنوز آماده توافق نیستن.
ولی خیلی زود آماده می‌شن
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68821" target="_blank">📅 23:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68820">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🇮🇷
ستاد مرکزی خاتم‌الأنبیا:
رئیس‌جمهور ایالات متحده، که رفتاری بی‌منطق و جنایتکارانه دارد و به قتل کودکان متهم است، بار دیگر تهدید کرده است که به زیرساخت‌های این کشور حمله خواهد کرد.
اگر این تهدیدات آمریکا عملی شوند، نیروهای مسلح جمهوری اسلامی ایران اجازه نخواهند داد حتی یک قطره نفت از کشورهای منطقه صادر شود، و زیرساخت‌های نفت، گاز، برق و اقتصادی منطقه هدف قرار خواهند گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68820" target="_blank">📅 23:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68819">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5763ed03e8.mp4?token=FPWMg88GWlepRTuds8UrlQxjMP55toY1_642jCa87JD1v6qEPkuwjHoRlDMJvWob9HhsXmTy7xKQTO12cosmsAXN2NqZ7x6h84roe36BexfSfUchkOudG70YrrWHGmZ9RPH61d0Lwlt7UKwdqXUPWKMl3WpEv35AfovVDoXBBpv53-O5c6Qx6UqrCTI1vHgWEGFZrowlnx4k99isxWTe8930axqaazSw-zwct2je3N6BHHhNxcYVDRiCGYHaVnaJEvb_AV4FCUip71BQGX31mpRdpSLN6YmijDZ8gERWXhNOmOGc67l6oegTdk_OmzmVPLUgMrqUxdzlRMcbwi1vlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5763ed03e8.mp4?token=FPWMg88GWlepRTuds8UrlQxjMP55toY1_642jCa87JD1v6qEPkuwjHoRlDMJvWob9HhsXmTy7xKQTO12cosmsAXN2NqZ7x6h84roe36BexfSfUchkOudG70YrrWHGmZ9RPH61d0Lwlt7UKwdqXUPWKMl3WpEv35AfovVDoXBBpv53-O5c6Qx6UqrCTI1vHgWEGFZrowlnx4k99isxWTe8930axqaazSw-zwct2je3N6BHHhNxcYVDRiCGYHaVnaJEvb_AV4FCUip71BQGX31mpRdpSLN6YmijDZ8gERWXhNOmOGc67l6oegTdk_OmzmVPLUgMrqUxdzlRMcbwi1vlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو این اوضاع ویدیو های سمی هم وایرال میشه
😔
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68819" target="_blank">📅 22:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68818">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGbHPBk8MxBxEqXr1QmIobKnI3IETlXpzRJ2xGF9epGxkmZydrg3ZFLPf_K06uzRmMozLSSv047ghoxvddNNU1c34rFr_7uuP4GGNhPRAl__NOrysHoxB4MGlAA9u_XJ8q_guk3U-ZpRZu5-AzK0nG4lYdR83l7zrR_z1OqxjWN8W9tY3uQdzqjvLpLHvIvMeXeD66P1cNsALNzSqOk4rawSiQTWexXhJHcEg9ZVhJJOcDSDMBAVrWYWAjL8n76YBNW4yJfFwWJD6O4wu6utORMIeDI7HuaKvBSf1jT8VQ1OVNFVH_nudE7GqrYdLxkQh45wkDZEO65xqk1txRLQBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مجید موسوی فرمانده هوافضای سپاه:
اگر به پل‌ها و نیروگاه‌های ما حمله بشه
خاموشی برق متحدان و میزبانانِ کودک‌کشان، قطعیه.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68818" target="_blank">📅 22:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68817">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad77b1ff68.mp4?token=PdKIshjbOsY_VhVC9QhX6Z6q8IkctO_-Ph6J87Rg_q6wsCZyqMs0-r0jnZoqmb8nPDtgbutqTOtjtgqHtKKGzBH1meGzj_vlWFU1ZXcoRho8Z0ggEmBE40ylr3HlV1DZx8oUk4mb9KlpUuTRONHaigcm6APcY6f9fTEfmAW3ZiWl8tIDiOBGta27KbleU4WHUeI5ejaihLgdUOiXf6aDTS6FEQqTJRPWRuLrtQfVBSBCOvszKEkpsbLbsjfDKYc3iHx6WEJSBUl3tCMxGTK4irLMnlDGGY-1JoD3pthCHmQj9ljQO8YWNHXGrVjBiqJMMBA3Zivu7v4_DjFaH7Jc-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad77b1ff68.mp4?token=PdKIshjbOsY_VhVC9QhX6Z6q8IkctO_-Ph6J87Rg_q6wsCZyqMs0-r0jnZoqmb8nPDtgbutqTOtjtgqHtKKGzBH1meGzj_vlWFU1ZXcoRho8Z0ggEmBE40ylr3HlV1DZx8oUk4mb9KlpUuTRONHaigcm6APcY6f9fTEfmAW3ZiWl8tIDiOBGta27KbleU4WHUeI5ejaihLgdUOiXf6aDTS6FEQqTJRPWRuLrtQfVBSBCOvszKEkpsbLbsjfDKYc3iHx6WEJSBUl3tCMxGTK4irLMnlDGGY-1JoD3pthCHmQj9ljQO8YWNHXGrVjBiqJMMBA3Zivu7v4_DjFaH7Jc-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ظهر چهارشنبه؛ لانچر مستقر در تپه‌های پشت اسکله طاهرویی (سیریک) که روز گذشته مسئولیت شلیک به سمت کشتی‌ها در تنگه هرمز را برعهده داشت، خود هدف اصابت موشک قرار گرفت و یک ستون دود از محل برخورد دیده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68817" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68816">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_Lc9Uuzcpfc7c9kQlqsuDOtbZhcibnQNCvub6KHUB0SeQCesyzoX8qKtmCT3CpGaMvdbKSt_1FqL7rkzi8kO3uq9sAQLXAZj3JApSXHxsKFPu6L0pLNanhuCtQRMkwP_r_HYMTyD3wjHOx6eqRIBRCzKrTt1CrTzjx51J3k6uywzE_Zoi0jstQRiqmWZPL5osMlr-JYi6E4SV_Q2xZ9XrzjFdVGn8Tg0jkvPdkaV0bnpYr0Bk5da4YIWb3nO_u9lSIw37Dond6WOwkkEabtS-L6i5uErIgLQzx0HycarAQ5JR-WlNZ5ensTwHcGgXL3tzzgK5HnBt28j8-1zx3gDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:معادلهٔ این جنگ مشخص است: یا همه یا هیچکس!
در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت.
اگر امنیت ما تأمین نشود، هیچ زیرساختی ایمن نخواهد بود و امنیت تنگه در نبود نیروهای آمریکایی است.
بارها گفته‌ایم که وضعیت تنگه به قبل از جنگ باز نمی‌گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68816" target="_blank">📅 21:15 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
