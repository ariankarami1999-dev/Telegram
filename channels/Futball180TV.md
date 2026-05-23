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
<img src="https://cdn4.telesco.pe/file/CmKw1pFb7QyoxyUqPP-u-Nv6jUIk4L6QGECl6j22YJqQzO1loyqgk9zsVwFsbEEUjP7joBvz421hSd0Ruzxg1erSUcvWEtCOybXngvtKAcdtOloS_LvUMFIrKzSXM9XZ92RCtEaYHyfujDbvbZ4VibhoBlciyv_7K89WsRYT6Iif8cRb6PTs-HQVyF1TqslQPxTtJ5MGXVcC4RvvePg1V_Q2MySfmqFHv9iAiEgLm7K17wlywAJiwRENX9WsNjwa2cvaFl8sAM_BeTbw_Ik-lGLyRVja4g4uqtu_M2M4C7oQHcVPs-6GGk3gWvV0KtYAoK_9VlS3_ILzk2bwZ-iRpA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 129K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 15:25:22</div>
<hr>

<div class="tg-post" id="msg-90169">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=HTlLcX0SrdhZEFNB7XJqMmKmP6yAPJQlrQwEVxqp-1lz2zkcaLBm1T1cKdouWfr-3EJfS2WTeM8XRDLnSa4hTt6m0n_kt28ESRJ7FvTtWYh21-IOHh-HHJC_jddlnI3qlF94OdbC67HMJpL-B0WCJJNNYu8SaLcMHSwy8tIani8OYFOYVA2Awdja5eu12_pXY4yn16W11q4wglomOPGB4TqXNzUNSnMfaE_IBxgyg6LIPZOo1Yuizau8udTH1BVOoEA3mS6Eexa-NN3EkzG-qePUfPRzrjLdDkT_2LM0Ousn5zaW1xHPAqzY9wcAVmA2S-5G8RohTF_sa_wNU5eviA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=HTlLcX0SrdhZEFNB7XJqMmKmP6yAPJQlrQwEVxqp-1lz2zkcaLBm1T1cKdouWfr-3EJfS2WTeM8XRDLnSa4hTt6m0n_kt28ESRJ7FvTtWYh21-IOHh-HHJC_jddlnI3qlF94OdbC67HMJpL-B0WCJJNNYu8SaLcMHSwy8tIani8OYFOYVA2Awdja5eu12_pXY4yn16W11q4wglomOPGB4TqXNzUNSnMfaE_IBxgyg6LIPZOo1Yuizau8udTH1BVOoEA3mS6Eexa-NN3EkzG-qePUfPRzrjLdDkT_2LM0Ousn5zaW1xHPAqzY9wcAVmA2S-5G8RohTF_sa_wNU5eviA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پادرمیانی همسر ناصر حجازی برای برگشت فرهاد مجیدی به تمرینات تیم استقلال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/Futball180TV/90169" target="_blank">📅 14:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90168">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-IricJo7hJ8nBJ1dk3EPQMATGZERJC_-tn_7ses0l_Nos_LOSZe6veyJZ2vIW5yNUikyyYTHGY6rA1JcLxHFphfwveLj6rW--MwW9hFjCuj1oop6_bMd2wtT3RAPvkL5kRLJ6lgisvgKDZalfjmBu7VGI_wrs7l5tJU8j_GnXfO2Wcsw0Ip_8WmQsDOLMnARU2Wn1w4suiiHBGZsdCgQCa3lPqP8b3qnfqEVSOROAvQUoKD5oKVeOqDHd13bUkLG6fqhdfkLryHhcqiPivdBmGebI9gQap0dGCM9j0qHZ_rBgLFXDwqDdhmbU7u6Qr9Lv5S7KAamvhqlUWhayxUiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برونو فرناندز به عنوان بهترین بازیکن فصل ۲۰۲۵/۲۶ پرمیرلیگ انتخاب شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/Futball180TV/90168" target="_blank">📅 14:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90167">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbobwbn8W2uw6meLmNPsdPWbWScV288zGxFYQj92_y6OEjoGL73eP1mpei2MsYqAFqXv0ZMFQjqlMwONzKuu-W7EBnTvNPRa_nt7-LlqRuLjUNgEXRQnKqLbq1jtZV6w6D4LNv2S1PNuFAhXvmCbvVB0BU92oaboilI7WdKL6sohlJqzoH25ww0hsytkhOlojtPn9DlFH8j5t1weJ8UKaz2sknH2DMkRom7P3I6mSpuMTPvTjOa_WtJDk6M7AA8AoWkVRx4_Jl0w00c3WzBOW8r1f4TC-YZ6Kv0iSzfWAublCX8KcOa0Hqu85ylpyPdH_kHLdOGtTLKuz_bRsSaRfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گستون ایدول (روزنامه‌نگار آرژانتینی):
🔻
فکر می‌کنم ۲۰٪ احتمال داره بره آرسنال، ۳۵٪ پاری‌سن‌ژرمن، و ۴۵٪ بارسلونا.
🔻
اگه بارسلونا واقعاً می‌خوادش، باید این رو با یه پیشنهاد قوی ثابت کنه. تنها تیمی که واقعاً قدم برداشته پاری‌سن‌ژرمنه. بهش قول یه حقوق خوب دادن و پول کافی برای مذاکره با اتلتیکو مادرید رو هم دارن.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/Futball180TV/90167" target="_blank">📅 12:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90166">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90166" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/Futball180TV/90166" target="_blank">📅 12:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90165">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eY_dUeD78BetQ166zGxb0qRTdxOIp3yIHmtT-cnfzZ2DEAX_RZ9g0TGigOrVd_vhCd-hbLFZJosRD60gBZW1BAxaDZLdqDV4QZopurzZAPpWDk57Awjn9cPR0t_RDD32OeMXpArUOYGHiuBI0MhuO78NbWiVSiXD9CBl5hjvuxD-SiPlGjB7xM3aY_Dy714nH1kL2xNOtWnCBpjTfRw9z5UfpdPFw4MBHqcAYOc7CCqXPDxuuiGGXeQGT2kNq2RR6-_oomPsQ9CukmtffhyHXdbl74zhnvz3hgM56RfGdGWFvz_fDYjF0D1gIdhu1ZbELYWyRYV6Wvp1fU0r6ia2kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
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
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/Futball180TV/90165" target="_blank">📅 12:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90164">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bb02d75b.mp4?token=p9TDvSlij3TTQzyI_gceMoROO6jrMUU4hakZ4tAgTSr8jLYJ_9Pz2JvZ1ieSN-CP4dLZGLsYZYt6QgSkpLVyA-96_qpoUKJvQR6HcqCoqP2Lg8xHNhoYFwlRyhHufjl_78aS3C53y3ipBIb9GES3uKUQHc_BVezXCbnKdXXjA7BYuN5lIp8bVlcue2eRp472gyaK6iWcGqOIXttG9NNjfNiEXAaZZvW0HdncojWPHYDzOyUAwG45VRheyv9iSDtNRUvrNURBVeESdA6LMmcRD2ofQgOtAxcksZrkIrWEOsTLMUtjnHHB_QSQAn_0NFR8w-eS8TzH5OLUpONTLwnZ7FOcHWHbF9BScf9fZ-h25Gidby6mccHgaxEPYGzbxR0NUoySK0Oso7Zyd3kCG2tay6ttpBV_2XSelgwT59vUyLKhqQZ0xDwxx3Esfw7p62vkYy6HD5Ot_dKMx_YRvXlKu7dEHR2vGV9td9tKOQsTdzNy0wArwQXIe4et_0Sm89K_6SfwYcIx0uz8vX4-8jCNZ55Kankfp6EubN8U7B8TPpfyFmP_F1s50ovLQ5mHLBbXAFATXD95MHsTx13u9CSOa7K_u76G7GvCesNpCQR3kJClw8aUIMxvsxLGpixrDAtn4h0JxAmyOY0Q_VmsJ73Y66mugP0fb3g1l7b06GsuZ5E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bb02d75b.mp4?token=p9TDvSlij3TTQzyI_gceMoROO6jrMUU4hakZ4tAgTSr8jLYJ_9Pz2JvZ1ieSN-CP4dLZGLsYZYt6QgSkpLVyA-96_qpoUKJvQR6HcqCoqP2Lg8xHNhoYFwlRyhHufjl_78aS3C53y3ipBIb9GES3uKUQHc_BVezXCbnKdXXjA7BYuN5lIp8bVlcue2eRp472gyaK6iWcGqOIXttG9NNjfNiEXAaZZvW0HdncojWPHYDzOyUAwG45VRheyv9iSDtNRUvrNURBVeESdA6LMmcRD2ofQgOtAxcksZrkIrWEOsTLMUtjnHHB_QSQAn_0NFR8w-eS8TzH5OLUpONTLwnZ7FOcHWHbF9BScf9fZ-h25Gidby6mccHgaxEPYGzbxR0NUoySK0Oso7Zyd3kCG2tay6ttpBV_2XSelgwT59vUyLKhqQZ0xDwxx3Esfw7p62vkYy6HD5Ot_dKMx_YRvXlKu7dEHR2vGV9td9tKOQsTdzNy0wArwQXIe4et_0Sm89K_6SfwYcIx0uz8vX4-8jCNZ55Kankfp6EubN8U7B8TPpfyFmP_F1s50ovLQ5mHLBbXAFATXD95MHsTx13u9CSOa7K_u76G7GvCesNpCQR3kJClw8aUIMxvsxLGpixrDAtn4h0JxAmyOY0Q_VmsJ73Y66mugP0fb3g1l7b06GsuZ5E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
یکی از جذابیت‌های فصل آینده لالیگا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/Futball180TV/90164" target="_blank">📅 11:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90163">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
⭕️
شنیده می‌شود کشور آمریکا ویزای مهدی طارمی، احسان حاج‌صفی و شجاع خلیل‌زاده را بدلیل گذراندن خدمت سربازی خود در سپاه صادر نخواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/Futball180TV/90163" target="_blank">📅 11:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90162">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiR46SmWCMS8TbtX2fIDYixHWWzHes50UM9VdQv3UOlU_eswWWjADFxZGD9kRU3xGmjf7ESj6Yc8DfANIZfR5RHwQMJH81agP3GfAY5-3tPUH9s3h8n_9-Q3dHma-wik_dmF3sV4_K5TiDhYUGaBvulR656VsPBVjpa8moBG6l3obKS6CL3uJ524A_lOzHhRL5rzkoJpqFjiUzHM0_w_0LZ3MPYDx1EkObDea33mZ1M8E3HMwRpiLX50ZL8Krb1I-buB-71mDKAC4JhpwHc1xbOKgkkmweilP1nBSGITf42KzhjaBVvq7Uy69bUtfLquISQgmfZtx8wuoXchJaD04w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توخل: این فقط یک مسئله ساختاری برای ایجاد تیمی متوازن است تا پنج بازیکن در پست شماره 10 نداشته باشیم. حتی اگر این تصمیم دردناک باشد، معتقدم که برای تیم ملی انگلیس تصمیم درستی بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/Futball180TV/90162" target="_blank">📅 09:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90161">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90161" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/Futball180TV/90161" target="_blank">📅 00:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90160">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVzNkTphWDNAidKQt3Qtzu5e9G4iFwxO_MSzXUcxmPCfobv6_26gauP79zjiJ-8gs6YnChlN7maatc69_iVEXoUZDqaibtEREQuthbj1iYPEgL3mlpeob32XUf1Y6UlQ0xlf5Ao6o1zRaVJzahw4HbkTauisWg9JTpFicC2HiYzEfAO1Oa5EAzwP6zUcmi8uK8EBFh_GQVfHzeG7HJGLqDtm80_9C0Z6LJK0FT1OqB497MZAFBSxmyJn7yxdPz6XGyBm4FJZxlE0leLKzTnNILkySI35-LHY6WWltz7JQP6sSHFOiAX8mxpR1gpGZvpp9HWrLIsadCTQqbX8SEXVdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
با پیش‌بینی روی مسابقات افسانه‌ای Roland Garros در پروموی Grand Slam Tournaments، فری‌بت‌های تضمینی و شانس برنده شدن جوایز بزرگ رو به دست بیارین!
🏆
جوایز ویژه قرعه‌کشی:
📱
گوشی iPhone 17 Pro Max
📱
گوشی Samsung Galaxy Z Flip7
⌚️
ساعت Apple Watch Ultra 2
🎧
هدفون Samsung Galaxy Buds3 Pro
🎫
فری‌بت و امتیازهای بونوس
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
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/Futball180TV/90160" target="_blank">📅 00:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90159">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12eda9dfdf.mp4?token=ebEIAZ3KtK-LQVTVTldy0L7OP8NcDoGl-tK3fhZFCJsqQyXatviqGX8cfnhadU6Y3yLL3K44SlxkhkSA5bBsmVbrJN1XNIFo2GX1jnDEpkutTxU9qCxbDthlifckBbnjFKqPNvC-KUVdqtbOW_VAbfP_clc7k8bejhiywE_QJMfC7QEy7DjgxFXcfHwu86TUOBBSLecd-v6ux7gdy8pzBjj-vg1k26OJXf90bX_Si4sCyGUO3aom06kOADiLXmghVFbcNNAbBumdKM9WjonbKGfMJAuivyFRPQOC1QjhpZKcY3In-65I-M8rGPjei9KbsBqF9fnIqqbIsdBRXFeTpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12eda9dfdf.mp4?token=ebEIAZ3KtK-LQVTVTldy0L7OP8NcDoGl-tK3fhZFCJsqQyXatviqGX8cfnhadU6Y3yLL3K44SlxkhkSA5bBsmVbrJN1XNIFo2GX1jnDEpkutTxU9qCxbDthlifckBbnjFKqPNvC-KUVdqtbOW_VAbfP_clc7k8bejhiywE_QJMfC7QEy7DjgxFXcfHwu86TUOBBSLecd-v6ux7gdy8pzBjj-vg1k26OJXf90bX_Si4sCyGUO3aom06kOADiLXmghVFbcNNAbBumdKM9WjonbKGfMJAuivyFRPQOC1QjhpZKcY3In-65I-M8rGPjei9KbsBqF9fnIqqbIsdBRXFeTpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ترامپ در سخرانی امشبش:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/Futball180TV/90159" target="_blank">📅 00:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90158">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnjt99XXuAD6azdg86k8FNm5jTVlfAbW82Xq7kPAKhaylJuCgMHqwrRv7yA-OFAgxrmSGvgZmYaW-GKd3t0w6VeLyrFgVXWwX9tSNCutdSDE5oKk7p0VdzNpmXS09rnsn_OLZ2T4kXQ3pOri2rASb7RSCYXcm4jB29N6yFk6R8YH1dISi-obMjYc6nubBHt8PdqmASFAAQhgFplM5EFYQRKa-0Hzgd0UDwMijzY-t8DySEKOTjo8qmnmizeZJpXbmB1tU6d-mnnrYhYixTDhiJqel9zURdT0zuUvroLegsRInq_ebMmm1XBLjZDqdRQpZpaFskpJu9H8Qh6Uqo9CiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی کریمی خطاب به شاهین نجفی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/Futball180TV/90158" target="_blank">📅 23:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90157">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgtApziTVlQrh_UamTVA-00VLVe4WfMeUs2RNlxCKyfNBxCMc3ELDFkRLY1QuG9fJTZyUDpIvKhWKYyXQFMo2-nBo42fbOHv3XR0-fhC8Qt8gr0c6wsr79RrMU3KHLtfKXTO-7vlV79TmPmrvmSKec_by8LIJ1z73uG3Htg5NLU-DOyqx64RsljMWeiOZ4vyBo4udZ-ukkKc98ATROGUtQ0U009XqImGGevYluMGyRXj5bilCdWc1KCa-OPb5dgWEkRzVxLLMHMMDgt1ovdCzc0QTJ59UACOiuJUxqYMmDfht2otbPpnqtIM5oTMDrWlEeuximfazGKEIitCZiKKNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رئال مادرید - اتلتیک بیلبائو
🏆
لالیگا اسپانیا
🇪🇸
⏰
شنبه ساعت ۲۲:۳۰
🏟
ورزشگاه برنابئو
🎲
با بیش از ۵۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
رئال در
۱۰
دیدار اخیر خود در لالیگا،
۶
برد و
۲
تساوی ثبت کرده و در
۲
مسابقه شکست خورده است.
✅
اتلتیک بیلبائو در
۱۰
دیدار اخیر خود در لالیگا،
۲
برد و
۱
تساوی ثبت کرده و در
۶
مسابقه شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر رئال مادرید در لالیگا
۲
.۷ گل در هر بازی بوده است.
🧠
وقتی نتیجه از تصمیم مهم‌تر شد، تفریح تمام شده است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/Futball180TV/90157" target="_blank">📅 23:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90154">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lC8QDfLH700OLQt43pl-tJRaDTBpE_KG7HaeLQKqBTq0jLyvMlAnVdiT--dar3M8nHnjzSrq-a0qs9rs7TwGUmXR32-CoflhCRUIFXZ0AtHg6Jc9Zjks2IM1K3n0UEX1Oxk-GB4WjE7XhCwq7nkBm3t_6EnvCvtBzl0TFCVik07V-PJDM_kyBySFBi8anHtvq99uBflNJ4_TTSs96MEknuxhhU7AZZoFSXFKYiLXiYETmVf2uavdZuUBU8vfOwEAHq56fpCiyE0BULv0Wi2vMYwy7EgojWDmtsziI6KP8u55XKHv-RaCmvkBJNEw59lMZqiUn7mC_s12gwCtvKyKYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mi4wq9Bm12TmWP1W2270mM3V8RtRhi8YdK6i7eYOQyYvE17l5LzGDBmmy1xjXT60FhjcKnRwC88Ilmor6cN0xac3RSnHFzPOIbPe7nn7cyBRnCJVeuighNjw5E6Y-BUH5k03twvvDO0GfvhdgFlcqyC0bnB3y1Ld6p-LeO7xnLEfMIMiNzixHMlJ4VsRhbmB2HhNjGRPah7L78h8lRAgekg_EUXRSlKH2ARhYal2FpmfD9k4EmUuF29ueH2U1DvRvSNg4-xzMruCV56w_8JVtKITCD5C_ufOfsaNdMF-FZmlL_X-wiG9ory-mwCYnz_V1rM2ba15x62KnxdANR1kgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UdjwjFf1nafpZjL0RCfqmXqMKSAWSS51xFh3KY3kbo48got0r8R6YR_N_vUbMaMX82o3C3Hin1h3mrkvHR5l2-KGki-peyGT6u1grviZPN2ZKmJ_zaGxcpOMmzj4DG0P_pvmQ4bXCZ7fgimLIxZdTZcFXCvHKfFHGmnN4fulvveEYhyb4KF0f2Wp_-W9sLTCmcZQ8p7eldxeIpgVhr2aozGDuWR3UavxQA8TwC_HxqTo255Tik4Bq5C1VByKPG-tXRuL107H34Qbp5dslANqdnIEDFjhAWQHqP1_t4eINUxHiXWr4GGt-keQCU6JX_bul-B2De7Ys3u4_ExzHyoXdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عناوین برتر سری آ تو فصل 2025/26
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/Futball180TV/90154" target="_blank">📅 20:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90153">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90153" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/Futball180TV/90153" target="_blank">📅 20:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90152">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEH9mwTRDLXE39u-T0Ht_-0HbiyPuJImyQQXaU8ras_QzTuHf0kWAW729sU2MFMDbwH8BSEMnLnUTnR7VYY-wEhfK_ZjaVcGqyF7d2y61L1HOJMUKkNDz3L2jPjmBYcu_1FucZyPt9-09qHtF1k3xShwmcjoW8K8gd_1eyKlDtzpXuPsjrYxM2B0QkOaxF7i_A_QDUOkN-xVUi6rkXJXUiAR4-WETgAmRQvpMnynqIQanxorrmlGQ4MhYEWFnc9X4_Jmb_xd51TjVxHYgYS3tDj5lgaGRQDqDhNTVNGsDIUB5HSSDAB6UdhrPA-rWmr0Y9qQhdzFpRv5Ex875tRFjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
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
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/90152" target="_blank">📅 20:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90151">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
العربی الجدید به نقل از منبعی در وزارت خارجه پاکستان: واشنگتن و تهران انعطاف کافی در پرونده‌های اصلی از خود نشان نمی‌دهند/ سفر فرمانده ارتش (پاکستان) به تهران ممکن است آخرین تلاش برای جلوگیری از بازگشت منطقه به جنگ باشد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/Futball180TV/90151" target="_blank">📅 19:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90150">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoSuSUhaqXjT58fT7SyjcWuPMvJDl22dk3cM0dnyRClejwDqDmbg1w-Kw6OL7heBxZlokJ0RDOaM1bM1m3_BYfLTNYXz4RAJqDpa5oMvWKhWAau0XVq9SUX5XETrHIbD7eUV0KnrzBaquGZVdMxmHB_SvnepPLzADKaE9aXiF22sjwaRNKY21Cu6OL_O20FbdYA5GlCbupha1xheBfQa9n43oVhKXh8vVXHWekb0jzD0qCqUTgXx4ZtuK47MgKDec7VJT_v5N_U62OEWxH5zTdm2b0VnQsLGKiGqpXc2sv4nx5E91S-mzpvfC7ofaQepxXKVE8MOjvsfdbz1zcdWxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ کیت اصلی بارسلونا برای فصل آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/Futball180TV/90150" target="_blank">📅 19:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90149">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmoAdmin</strong></div>
<div class="tg-text">⚠️
مدت این آفر 3 روز هست
⚠️
💎
پلن حرفه ای
1 گیگ : 280,000 ت
5 گیگ : 1,150,000ت
10 گیگ : 2,050,000ت
20 گیگ : 3,900,000ت
40 گیگ : 6,900,000ت
💎
پلن اقتصادی
5 گیگ : 850,000ت
10 گیگ : 1,600,000ت
20 گیگ : 2,800,000ت
40 گیگ : 5,100,000ت
🟢
کد تخفیف به صورت خودکار روی ربات فعال هست و نیاز به وارد کردن چیزی نیست
✈️
آیدی ربات جهت خرید :
@AmoAdmins_bot</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/Futball180TV/90149" target="_blank">📅 18:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90148">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🔵
باشگاه استقلال مذاکرات مثبتی با آلومینیوم اراک برای جذب محمد خلیفه سنگربان جوان این تیم انجام داده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/Futball180TV/90148" target="_blank">📅 17:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90147">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8BThKseW30AslqsZ8ynyyEcjmR4Uo03ZoR1cHAAqSSD8th27ske_uGpp3UcMOREk7vsWSLpf8oG6Mmeqiz_6HRQT-Cu5Gjax7e7uoc91XTCx0IqBv_j5Pp7ijPX5RRgr3KE1ir4CclzxVyqMxji_ZSxo6pGxppZrOd8oUslhU0G-pQfmwQ-P4mXLnzZFIQJUjkCMOGjDdEy376vbhRf8i7NSQ5KTRkr1KyXhBVKMU8PIivs4Yov7t-zCyJ-z0V22e_0JEwndywvqX38YCg-QCB3CsHlmKa91lgcGpbhwLVh4v5ckMoWuPwAxViG6p1L7wn8ifGjhmfhLIV2lBn1yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب‌منتخب بازیکنان خط‌خورده انگلیس از فهرست توخل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/Futball180TV/90147" target="_blank">📅 14:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90146">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzUvT4UjHtYpjvqHkx8QavZLpl0cO3ehWQrELx0dBmkMy6SGTjPw5EQ2nH8CQHThH012WKjvQ6pvaI-UqG04xHQPGHBChcH4w6pXzkrgFtNFfk6OlznbtGp-4YDEOVyj0B8B5Oh20P9V2HsyDLeA7jjNTJzl421AF32voG4QgkVgnh7ziDe9FWBVY442Wq2mp4Otv49jjuuKg4MVymYexauOlV5c6VbB15ndZqHiDLEo3-KB8J4K99izKxheGi-woAuJNRjjaXznKZTx_AOlsyTel6JANQPcuucXcvtrYbCOAc-1m4sgCtoTK4Sm3iyZ5PLdvbYZAYz99PAugpR8YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک با عقد قراردادی دوساله رسما سرمربی دائم منچستریونایتد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/Futball180TV/90146" target="_blank">📅 14:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90145">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hj4ThLVtTbzigF2Nt0Yhifvqg36BfRxL_Xsp44_vPatD5rqOx0qF77_ID2a9-KBPUoG8MGo7ly7iqlsGHncmGi14jzC9tSVKPgF5r9dPQ6RUKLppVbyoZ_LmWvZjehvpH7DNYSgklbdJbSf2oY_6YUrzweo2p9sT7PUj8X5xtTuttHqs88IOSyq6PuuixDPk4-lUEpGYP_C0jxmnoB6cjkqcXfI6UYpp-i6xXY7P_D7iQsrrSo6PjooNH2OHy2W5VEB5VlGybh35Xstdo5IzQr_OOwuD86o1M9vx_3BUkaFb3vO82Gf2Q0rMn4RoCAvYBNdZPsBkPbLqsM9Td7RynQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمی
؛ پپ‌گواردیولا از سیتی جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/Futball180TV/90145" target="_blank">📅 14:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90144">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90144" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/Futball180TV/90144" target="_blank">📅 14:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90143">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLEtXTBv0tmZmijXYeFCJigmmjq9-8bLC57BALE4LMtLGqsoEXYZAoGr_ZZiucQJX9ncuB4KYva0DgNK8HrU8G5ggl5fqA3qtFkqrK0bUUu6lBzXB1sKNFeMbfJUJg34AONzrXbxUBWIUMaCnHOVhl-4u2nzRMMN0flW4zPBm-XConF5bMmwMmJ-k3FF976hN1pLuC6K58TectI95imDQGlXOq-by0DlagcNIw_hdNVFAhKt36jGl0JfQlrLiQqRXHNYXuv3_sW5Iya6-ZWRgzAxrCTQQjnS1SCK3YN_kiq3q9oIze8np4p8OlZAFGe4cjy0z1BOO7QGjhSOaW7X3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/Futball180TV/90143" target="_blank">📅 14:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90142">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست تیم‌ملی انگلیس برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/Futball180TV/90142" target="_blank">📅 12:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90141">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZLdSOL_ntMVn8fm7Zpg9OwsMsze1PSiUHhxTiJYq2y3C4Hj5Z_rK4GC6BQ7Q30ve88n1wBeUYQHhuV9NmqMhhPOaSN56aJK7Pn4QfU8LVs8KUgS7b-leJaWmM6Jbm7lsyTjJ7zYtP6rmACxc-_A1xifsdIE5mVLDmKmS4HXKJYrec187vwB6sQC_HSkyjsH9KzUyUd6w3jtcMG6NmVev6xq5Oh9xzJy3_OZUJ46bXqyoT_ufJgapUXGGK1mRiPw77K_IzWz-GMoLRyHWXUBJOLpxj87a44mZqV_JMK5uedOXkLMlo4WrLSC2QM58i1pMu50BryeADIQiUkELJKKnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست تیم‌ملی انگلیس برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/Futball180TV/90141" target="_blank">📅 12:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90140">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🇪🇸
آربلوا: با عشق و احترام فراوان،‌ فرداشب پس از بازی رئال‌مادرید را ترک‌ خواهم کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/Futball180TV/90140" target="_blank">📅 12:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90139">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🟡
باشگاه سپاهان با انتشار اطلاعیه‌ای با کنایه فراوان به سایر تیم‌ها، عدم صدور مجوز حرفه‌ای خود را تایید کرد و بدین‌ترتیب باید شاهد تیم جایگزین برای طلایی‌پوشان در آسیا باشیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/Futball180TV/90139" target="_blank">📅 12:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90138">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
❌
در صورت عدم کسب مجوز حرفه‌ای توسط سپاهان، یک تیم از میان گل‌گهر، چادرملو و حتی پرسپولیس راهی سطح دوم آسیا خواهند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/Futball180TV/90138" target="_blank">📅 12:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90137">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpvSP6eUoV-VaDnOXOK0YbQn-6QyTe4bYeetVgfM31TM6G4ujGacNDBd7Eh8fPhktG093I8tiEuCycbS6g-AfNK7VdH_23ehznpo-u0Nwzx-y1be8--AgeL8bObxVZS-gjlTu16tOys2wNtPyrut0nlSoDWfwM9pdkHVqaWpiDmyW_Su-gh9IexUjfU6l2Xm4_w-UcNuCrSROZEhIsZDyk058BLcTXtgg4mrfEJdrrvB8h0mhzyz7M6kK-dxM9i21tNc94TMZrzKkU4QDrj6UVElgxVqYSJsXUSi8Ex9mQMuxNzUPOxYeL-aNK1QzRxcvxeSYA9OInAoKtgnXNybzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کیت‌اول تیم‌فوتبال میلان برای فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/90137" target="_blank">📅 11:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90136">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
❌
در صورت عدم کسب مجوز حرفه‌ای توسط سپاهان، یک تیم از میان گل‌گهر، چادرملو و حتی پرسپولیس راهی سطح دوم آسیا خواهند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/Futball180TV/90136" target="_blank">📅 11:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90135">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCcDMPbeKI41ZtYTDnbzo7RCqr87xYITuy6GVmAji54m40HcothTG0CkH_ARIs6dJydUBoIFPHcwZT2xT7REccsOjg7Ln24McaW4kuQk3hyLVN5z5qQCNdzjk1SuLrAdaflEix10pRMa80jprthbJJhazN36yppBqslr0pkd9sIcRI1Du30jImDnvS_S9JtAqhjwAEDfmtMcDJQ3WAz14vH4B1qZsJd4Ih4F7oCIEKO-Hkw8DctSBrs6JevcMfjQ-iMx6u2waQwKJx6_KezKUh32R2fKGa6p9j10AD-tHDjjiY_hzRQ9nw1qbquWtA4554ZWI5dNpCNf9YhR3OZp8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
آرنولد ستاره خط دفاعی رئال‌مادرید از لیست انگلیس برای جام‌جهانی خط خورد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/Futball180TV/90135" target="_blank">📅 10:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90134">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lt7hM2v3qoQNeqvaRVygWawsRjOzZ21aga8l5xy_1hN6rr_6Ik8XODKXtj4DR-Ag264Aj7eWu2k0-hk6jOgOu-rfbMG4JJR0N3_8tNVzwgFZQbBc8Svvqo5heQolrW8ZWp85gGHPMjeWf7NtqWxPZy7cqZ-q3bDj3PB3ZUUanNN8lJNW17GKz9-rcFJ6YU0tAvUyNNNHWZQs2mvPnjlFAnbzy53SwvD1aa0Wt3abRpv_PJTzPajbyYt5QEK_atVCLfi5zhx1YHNqtXAmptYuvd_It1q_2QSCLIlIRagyrU8FebCsAFNhjKXwlxulv6Z4HpGiZ5OHLWEO8MBfjGeRxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کارنامه بازارهای کشور در اردیبهشت ماه:
دلار ۱۸%+
💵
طلا ۱۱%+
🥇
بورس ۱.۷%+
📊
مسکن ۱۷%+
🏠
خودروی داخلی ۴۵%+
🚗
خودروی خارجی ۲۲%+
🚘
بیت کوین ۱%+ دلاری
🪙
اوراق بدهی ۳.۳%+
📜
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/Futball180TV/90134" target="_blank">📅 10:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90133">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90133" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/Futball180TV/90133" target="_blank">📅 02:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90132">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDcjiIjvoF7PghvpLUP1A5f_3nva67SFcnrr_FUgrRfv1PapLRxtCPBVIdmivN11efjx6Aj2MEzdn48lV1A6KVW8nKEr_HvuXPwdFsKCTd446neASZVyHunLugh5sFdiTz4We0iQXEapzF2fOZibAYv4jQ2wyE5syTZAHXNZPanq9wWWGVmALu4FU40xUhmN-esaLwQI255CjKCuET4WL-0bNtC4gzcNy5iuaCslhYP994f9cOFxdH2JNocnk4A9hd156YydebUNnyNLm8eJN4vW1kK1zqfzzMxNfyFdASYP_oj8oexd6jb_b5896Y0V61D11yIyzUc2xQwQ5HK1Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
با پیش‌بینی روی مسابقات افسانه‌ای Roland Garros در پروموی Grand Slam Tournaments، فری‌بت‌های تضمینی و شانس برنده شدن جوایز بزرگ رو به دست بیارین!
🏆
جوایز ویژه قرعه‌کشی:
📱
گوشی iPhone 17 Pro Max
📱
گوشی Samsung Galaxy Z Flip7
⌚️
ساعت Apple Watch Ultra 2
🎧
هدفون Samsung Galaxy Buds3 Pro
🎫
فری‌بت و امتیازهای بونوس
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
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/Futball180TV/90132" target="_blank">📅 02:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90131">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItTTPV6uQ185ztCqgTjJGolWDgwB18-rqm1-VFVe2pykjpB0WZISUqVXB7ECVGAnUPpcl4Loz0agc1LFVIhrvOZzlLvO1bG9fmeE8iQ3V0RnrV2mjT3tV0YVBFirEsx-ybrwpCrZSFha9-mUmFUvLgOfTstHqsMuY2Ck8gspl-90ZYo_GRx-twJvNLDew8tphLSy61eFOow2_B1wc-Mc5IrIgAuGt_GZBqryM5D82s8AovmGi_xDAuMUC7JwQFAw6MaYw3PGeMu9Jxv-4kbiesBLaVTcpfa4tEq8OjGr9nRxeoG5wm_7j-Q4i32m95KBq5CJbOxZYIp1-deOfyp2DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
دستیار هوشمند پیش‌بینی بت‌فوروارد
✅
🔥
با قابلیت جدید هوش مصنوعی بت‌فوروارد، تجربه‌ای حرفه‌ای‌، دقیق‌ و سریع‌تر از پیش‌بینی‌های ورزشی داشته باشید. این سیستم با بهره‌گیری از AI امکان تحلیل بهتر مسابقات و تصمیم‌گیری هوشمندانه‌تر را برای شما فراهم می‌کند.
🎯
تحلیل دقیق مسابقات با هوش مصنوعی
📈
بررسی آمار، داده‌ها و اطلاعات بازی‌ها
⚡️
ثبت سریع پیش‌بینی تنها با یک کلیک
🧠
چت با هوش مصنوعی برای دریافت تحلیل حرفه‌ای
🔥
استفاده از ابزار پیش‌بینی‌ساز برای انتخابی دقیق‌تر
🎲
ترکیب قدرت هوش مصنوعی با هیجان پیش‌بینی ورزشی
⏩
با دستیار هوشمند بت‌فوروارد تحلیل کنید، سریع‌تر تصمیم بگیرید و حرفه‌ای‌تر پیش‌بینی ثبت کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/Futball180TV/90131" target="_blank">📅 01:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90130">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90dbd94917.mp4?token=AcHWckdPdCaPRaBOuL55pN4xTvFCi2PwZ-tXzhJrUhcP966Y54MMHrrwWL5XuxYNr-IHQII_Rgm_ex_OzblmqmalGvW_X6hkrtwoyXRo-ONIpHsG30ZLsZCtJUcqNN8EFh9ELPHTKblufDSWEYTX1Mfw0FsFD8JDB7Apsv4ZI_MHu2DD3u33toGHlK9xFTtEov3_ZI-57nGjiX4EAQHDk177Uur5815d2df2gcLD9Pws4I4tFSlmeIE-JOzxyqMh90kQb8W25BAGPgtDFPD-RKM2AHLGnnfts3E7Ylo0ML7EGHOrV5N2DP8xnq_OT0o-PhPgf2XCf0u91EC-Vj3I2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90dbd94917.mp4?token=AcHWckdPdCaPRaBOuL55pN4xTvFCi2PwZ-tXzhJrUhcP966Y54MMHrrwWL5XuxYNr-IHQII_Rgm_ex_OzblmqmalGvW_X6hkrtwoyXRo-ONIpHsG30ZLsZCtJUcqNN8EFh9ELPHTKblufDSWEYTX1Mfw0FsFD8JDB7Apsv4ZI_MHu2DD3u33toGHlK9xFTtEov3_ZI-57nGjiX4EAQHDk177Uur5815d2df2gcLD9Pws4I4tFSlmeIE-JOzxyqMh90kQb8W25BAGPgtDFPD-RKM2AHLGnnfts3E7Ylo0ML7EGHOrV5N2DP8xnq_OT0o-PhPgf2XCf0u91EC-Vj3I2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی فوق‌العاده رونالدو پس از قهرمانی در عربستان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/Futball180TV/90130" target="_blank">📅 00:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90129">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnrSPJtCUbXLmW-K9dCq16AaqHq_UPRv6oyZNX1nAfSQRfPeK_R8-xU9-yWv-S6qU8aOxq837JbGVfluEDVPVs0007rS0cid5Q9M4wxvbYQPdk0BuJqyTdq2wT56Sk3ew1lHnjr9HGOcPJ0f1-IqYE5RldsTxLAlxlm4u5deBocP9PjxKcSUUWA4z2ltQoJCGXXIhM-lE7Z8WZj54N2rXOJfsV2VSVsrGCkTlztjktoaB7dc35D7snXGKjQk11cO5smLjfhqZrchPVYdvwHmbz_QBRzgFEYKeLv94Irp-y02wk47vVc6IO0YIa-yzkEpFRDGSgRXtWZnP2_5FEi4VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
النصر قهرمان لیگ‌عربستان شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/Futball180TV/90129" target="_blank">📅 23:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90128">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY_eh07EzbhgThyJOOWl0aQAA_XKsuY1QsIv9FbtBVINSGA2qn5heWdIY4BHX5fR9BpVj10NV-OjqeWuVr-USWkC4Wehet0OOPFp2Gish_XEOr_NLjG3nDzkGqCE1RjTUB5NMQh80C4GrL47YjY-BqB-Ntj_EcKmwS2kfYFtMfaTgQ0RTFC96R9v8VUM5fa0RstH2E_ySkctw6feM9YKTEz3H9ZYLbQdSFE9tyf-G4-7l0J9epXTD9OkRFhdGPSnVgPTbEydvCKPxTK8-D1mZ5oO_L0qU22FDhWP7grtWTdcsAblemDrMEC4RvgKIbMMkOcqMRmclf01D37wSFkdVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقدیم گل کریس‌رونالدو به جورجینا همسرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/Futball180TV/90128" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90127">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9421ab7b51.mp4?token=Y8xsAy4WHfBmjTG-KteYP8Qsn2rBaSrqtT0loJIwyC1csoNuudbXjCcFiOscsb25CrE2AGedFVBqGAzWEOHSlBhaH4dBB1vhlbiWgJKbOc2Vk4oj6VN3M9Krt0ZuwBMcRqBeet3iNsG-1sYfwSYm3foBDpaIZjl7QVILujXtJn1wAGKlF4oJOEmCWA5A8CLkEiHe4uamO-JQCZ5C7KNRBgl2B2cdqsy1bNZ_Kdi_ALIfHBmfqhI9Fzn4uOGWFj20wd30sZSypYH1LgMi_YPwElHiSO4pjwWF_5bQDsCDmghgu4YryPibY4CeMMre1AseMTHj1-CtosTaVR-84XFNej9EnTQGgNJmscVphmcX7V0aaIKPTRod8xa9lm4A27yHAgJgMsJ3vW9oRMU_jitg4Gwss6mRc4EbaNrBrlI5K3SIzGdMX_kAnznRz5UO6wnWgCr_AH6Vit92K3ckSAbcRLEm5x-Kc9PBnlShrHN492fEv6BDMkkDC_eHyZP_VNKuTrBQXy6n636gm0hywqYRkWJH5uFOgC6BpOAIWvY-Hv_XnnG6NBVUIiy4-M4n1tK75JPmTp0e-DugXjnESycjN2_KXz3bId1-MTwSo0jAa8FrxkOnhWD4A1BJO7FQOXEkn0d4V-kfl3ZbUwsAtjj4PDWol9nzyn5AdgnkzC_l95w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9421ab7b51.mp4?token=Y8xsAy4WHfBmjTG-KteYP8Qsn2rBaSrqtT0loJIwyC1csoNuudbXjCcFiOscsb25CrE2AGedFVBqGAzWEOHSlBhaH4dBB1vhlbiWgJKbOc2Vk4oj6VN3M9Krt0ZuwBMcRqBeet3iNsG-1sYfwSYm3foBDpaIZjl7QVILujXtJn1wAGKlF4oJOEmCWA5A8CLkEiHe4uamO-JQCZ5C7KNRBgl2B2cdqsy1bNZ_Kdi_ALIfHBmfqhI9Fzn4uOGWFj20wd30sZSypYH1LgMi_YPwElHiSO4pjwWF_5bQDsCDmghgu4YryPibY4CeMMre1AseMTHj1-CtosTaVR-84XFNej9EnTQGgNJmscVphmcX7V0aaIKPTRod8xa9lm4A27yHAgJgMsJ3vW9oRMU_jitg4Gwss6mRc4EbaNrBrlI5K3SIzGdMX_kAnznRz5UO6wnWgCr_AH6Vit92K3ckSAbcRLEm5x-Kc9PBnlShrHN492fEv6BDMkkDC_eHyZP_VNKuTrBQXy6n636gm0hywqYRkWJH5uFOgC6BpOAIWvY-Hv_XnnG6NBVUIiy4-M4n1tK75JPmTp0e-DugXjnESycjN2_KXz3bId1-MTwSo0jAa8FrxkOnhWD4A1BJO7FQOXEkn0d4V-kfl3ZbUwsAtjj4PDWol9nzyn5AdgnkzC_l95w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبل رونالدو در دیدار امشب النصر مقابل ضمک
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/Futball180TV/90127" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90126">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92cbf0b75a.mp4?token=pX_bVyRfKDqz0QRO1QUReuolin54kz_iDW4l4JPEwXVDfbOUpGDi_8Bs6w1GULPIL6AX-9bndWpUNCcKBYWVWrZ3FKq9xSzChqLSiVm8Kn5n94MRG838qwx0B8P6lFOMRVlCvGaNCXSyFj9doCqX63g0PXCYVRUlzgk9t169W83LEQmrPxqZ5UMGpcXUHrsxwV1Wxu0qQPc0oQIc8jbNccHR_mmIjEe0FS7JIHVYpGvOYBde09w8I3CSpx5iHR3jM6DjSAGKMbjYP_lB01VaRuP5Kcls3FoY2G3PcfGCI-_gUTnc7nlBSTQbEyAsCJb55YPmhZ0v_dT2Rd8kP5gxNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92cbf0b75a.mp4?token=pX_bVyRfKDqz0QRO1QUReuolin54kz_iDW4l4JPEwXVDfbOUpGDi_8Bs6w1GULPIL6AX-9bndWpUNCcKBYWVWrZ3FKq9xSzChqLSiVm8Kn5n94MRG838qwx0B8P6lFOMRVlCvGaNCXSyFj9doCqX63g0PXCYVRUlzgk9t169W83LEQmrPxqZ5UMGpcXUHrsxwV1Wxu0qQPc0oQIc8jbNccHR_mmIjEe0FS7JIHVYpGvOYBde09w8I3CSpx5iHR3jM6DjSAGKMbjYP_lB01VaRuP5Kcls3FoY2G3PcfGCI-_gUTnc7nlBSTQbEyAsCJb55YPmhZ0v_dT2Rd8kP5gxNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
سوپرگل کریس‌رونالدو برای النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/90126" target="_blank">📅 22:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90125">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJyFLjnzMogkvo2JNJrLkxKDwoaxUavEa043ENwbeiIHMaziEoolYEv15BvbcyKGseuBmb7XF67vA8W-_27asqCjR4g_r7XB_f17y5ibQD8NGE8uXTUD1sPdueJkpcyR0pdbCtVB5dDYAwXGp7nL13Bx4vNCMzHjDBh1bvpGGe1T6BOUlf19IusClbIPmfi9MXh5oyxR11lBv0byFUiuilaFKiYpz-qVN0BFlmMG50ZDNvF_XQy1JzkhAmEF4VC9CLG8S_d1IYIthE4MOuPc6Ou-Vy6BvaFrif4Mxz0u-2PPzY3ZFqPMMjtGiXmW05rUDsl8ULqj0SUl2BeNjIlQuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚬
فیفا قصد داره جام جهانی ۲۰۳۰ را با ۶۶ کشور برگزار بکنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/Futball180TV/90125" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90124">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xk5DGBq462Zpkv-wEwMgZs2Lk3uqSelgyNJ9ormy3_6o1V_A7jSGBmpDb6UW8wuWzAyNgHozkf9t4C9Xc5hgrcxviFN1Y5dVNVfjCdiKjg4tO6eWIeThwK3uACGHdFgzK9ZNy--DWHOcC2IFZy0qlCqGPEMWEulSETI6jvYstksTcYiDIT3v63fnh5GCWLZLqGGPKdwFpVYUxko2jeyNnfdXMburLEXPUCZqkUKnCdAhVt18awgDIrF2MwXR2i1UNLEF3UjOQP1mCKvBCbOrOK0IeJO7mLcEkGCONVAbYO1gDh55YJcKmtuDjsvxpmxyHKh_bTAty5GSUw05MvdrHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دوس‌دخترهای لامین‌یامال در سه سال اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/Futball180TV/90124" target="_blank">📅 19:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90123">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90123" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/Futball180TV/90123" target="_blank">📅 19:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90122">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mus_CPg5DUAdNVyRkfPD2w3UXRmXmyMkICN1t2droGgsOfnxGYRZrTaR0Qp146lxUpvJxKwOIKiR8WdgWO0kOKPjb6zbkydg_e6h59MBEA2xqOWSugq12bmgXKJ2-MW4ZYSqhXwFdmDLS9IEYf1x8HsJqhgwAEpxMFoqAHMplLpTKIdxzMcrQX_aY62BAZY3yTmSl2agZSnhITjTN5f6SJhkXRTCbevvUH5aGQvMsDFo4DXy7BIVaLdKNmKW2S9IdGhwUqtQDBx15aWzUTK0iqch5J50oz6fKdssBNJx3rkBGNLspibCY-NNaHSmJkeHrmLNvyr5kZLu5xOFK70gFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
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
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/Futball180TV/90122" target="_blank">📅 19:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90121">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5UKaMSq511cHYUADSAKJND5hr7dLol9x-QY8-AWc1LFVWFOy3NaEak2XQWGcBV_TG0l16oFM630HuYsKMDgeCwLjnaeSJ9q5STlGs684XnQHhkLz-SbhZbgfwPmAJe6OfkkUQVs8_7oDIj5gLb1OFGPb3RbA3ZoeB3-TkhoR2Iy7Owz9hmjGOZrmaoWzK5Ix2WLaQ9AFupC4MkqfE1iRqAqpgauIWY-lgo5iv7RPc8yOpkzeE1VoPX_gRzkygXrGfXpkXb3ricW9aKJ-bS_fEuJzBR1GgsuBKPjhaJ4iLv9uAHfD4E5nxJFZg2ODh_6F5k9fdevUI3QdSTcS4N4TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
لیست آلمان برای جام‌جهانی اعلام شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/Futball180TV/90121" target="_blank">📅 18:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90120">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW8j5dv42o0qgbFSVieZN1iI6Rbdbv77oPdXBBWY_Xzaa1ksQ3FBtqAHs96uG6Ly7eC7J0nxpkXE0wZKXUtoiV0FWWwclrnhcTQDA_Ge9YJ5UlUsA2gGK6Tvs-dCWBLVPwy1tfrPYCZWBFa67gugf7pjP6-NsIbcb55juwusolMmFmjlkpqN-GxKfEtZvGdvlK06v9yqBiBlK6W035gcxJDejIp7aezAlRJLHZmo1cgkRN05FQwp2DsZbSv_XkPaKe197h3zPuIz9W0XsZ0ty1R349HZ2OefHigrpJfHoqo-GZRb1haGKWYTKinUZLGdfHIU7jzkLCj_JggFE-R35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آرتتا به مانند آرسن‌ونگر‌ پس از سه فصل نایب قهرمانی، بالاخره موفق به فتح پریمیرلیگ شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/Futball180TV/90120" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90119">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7sy8rMsztkzbNt1cyOyYtzoi1uZ4zdDarWBIII7r_Wn-0nb_ijIinRizOF9WLK5OlPlUjC7VW7a9Yyi_M9XFBXA4ozAlChjvhl-wQAEx-7t5lU6kp1PWFH36iWGcWz7OfpJGVyKXp89dZiOXAlue3XlX8A_Zrp2kNMfVb9hrrv5Mo1srzYYEt_Wx8KbDjSmlDOlUh_ezGkNLehgb2eZyC9heiQpojmiVimmzJG0JwfEuux6RomotD9y7a7zc7KgtKfq9RSqDleMbGFq6FMucF6OPNlgRyaDwsXQPAjSj73kw4BeXT9PrjbjKc4T38k-Ne0MvdQH5RyqAiDSMEeTOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تیم‌ملی جمهوری چک برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/Futball180TV/90119" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90118">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90118" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/Futball180TV/90118" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90117">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvZNbNKqSNkIUsAqdNSLtZQX1GHotb1ni0UltMvHsvZ4TO8bZHvlTTG-SqD9PUIy80RD9zzz_flix5gmm4Kl-M4R63TZXj-VlF-ZOEmgFyE8Jyf3CaVmZvC7oOPB_J6zifSgwu9yNnCnmUUp1CkF1n6cDaeC0D7BI2t2E0HAEXUVX7B4SSPqgyvnqpEKAGQcvdoUK40B60keD89O7ghHpnTXyo-NzEsr_EqeiPPXBsJ-rBh4x2NdDyIVQ-NWHEsoDl-EM-v740RBOtXFwqV9iIKRSHt5TCKai4PaIgYwZ3I7SmBqX4vrTaRH4nieA63rxbH-xz-5_QUiQ0WSTJ12-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎰
با 1XBET راه خود را به سوی ثروت بچرخانید و از سرگرمی های بی وقفه لذت ببرید!
🎁
تنوع گسترده از اسلات ها و جوایز فوق العاده را از دست ندهید!
💸
فقط کافیست ثبت نام و واریز کنید تا از جوایز و بونوس های فراوان 1XBET جا نمانید.
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
فایل نصب اندروید 1XBET</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/Futball180TV/90117" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90116">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
فرمانده ارتش پاکستان، عاصم منیر دقایقی پیش وارد تهران شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/Futball180TV/90116" target="_blank">📅 12:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90115">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDeCaiWTefmPqjORpiw5ivDqtC0RqUQ3Y_WjsAZicAFOtLQel25hRB_dzebmIm5R1eByBvekqImpqZag3_sKxRqHueDFhJpNK5jlqRg2RLHIsViw6IrIiX0qorU35lm2HZ92iXDmq_MS4AE5bN2uoUeMuOyPulqVzEbHE2Gk1ITK0J7ZERI8k5YrK37EI4l7lGj8gJ2PHqFIN9MiiHP5WJo-tboXNtgTYIVdBzxYiLZAAIT83cD9wQ9pU3f9rLHs78DUmO9ef4udI_SCIfY9PtcsXZJH3lmcI7J98EaZ42H9V_rMwVh91EZG63Ps5cN2oUVHn7d5HV6DhxsAfGuxGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه کریر فوتبالی لیونل‌مسی و رونالدو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/Futball180TV/90115" target="_blank">📅 08:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90112">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAT2z1swpFNpC-9snnsnAuwt3WTUij5H9ib3Don2vz5N2GtMme4npNJxZxV7zZJNmCLhQn0GHUYfp-GSQYHz_KqS0iaf17TfRd6WV23vBVRDRLO9w30GYmpgBUMIRG3Xo3Lvf-M2NS6US9lzqY10o4dBlE2tCx99aaKcrVFKUiRcoSUBXr0bc5ngDORYKXH0U2C-8UmPcaggdtq2598ABK05XhwkzGhC31mu5uV-OSHN3HidoGxVJG61WzGeEeXJcN2lrVX7cWGrulQLxS4V4kLgg3OwYULNhxkRK9Mgn_nL_8BpS3JWYH8rgNTomc2sZt6K977ICB87DL8MgTg79w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇺
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون‌ویلا با برتری قاطع مقابل فرایبورگ قهرمانی لیگ‌اروپا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/Futball180TV/90112" target="_blank">📅 00:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90111">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
👤
برخلاف اخبار منتشر شده، سردار آزمون بزودی قراردادش با شباب الاهلی تمدید می‌شود و‌ این بازیکن قصدی برای حضور در ایران ندارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/Futball180TV/90111" target="_blank">📅 00:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90110">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
ترامپ: منتظر پاسخ مناسبی از ایران هستیم تا از تشدید بیشتر جلوگیری کنیم.
چند روزی منتظر پاسخ ایران خواهیم ماند.
تا زمانی که به توافق نرسیم، هیچ تحریمی را از ایران برنمی‌دارم.
در ایران افراد باهوش و بااستعدادی وجود دارند و امیدواریم معامله‌ای خوب برای هر دو طرف انجام دهند.
اگر پاسخ‌های ۱۰۰٪ صحیح از ایران دریافت کنیم، زمان، تلاش و جان‌های زیادی را صرفه‌جویی خواهیم کرد.
امور ممکن است خیلی سریع پیش برود یا چند روز طول بکشد، اما ممکن است خیلی سریع هم به پایان برسد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/Futball180TV/90110" target="_blank">📅 22:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90109">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpcFan6lQ1hKgY8LCg3w_bw18HH-fBgPP1CudeVF-CdHPyzFxqDtXRHyLeKrpxYOtH5Bzz7RUJr_jntCx_yBBpJMGWFjAYeApj4774BQ2OwntuovBTbvJmFHMWpAREGHwNKj_gSfqQ4y3EG0ymvQ0J-JJz4Wgpg3gTFHx7vosTN0UBPBsj1mJuWFHfLHhnxU1UNOe8Mtne-60BK0UkgLN37-O4f5aB3RhoCLwgH1wIRbT7O4Cfta0IzTFYDNjgt4rM_5D3LU7kPv2G1K-vGpGfilaakLIagJY13hx3S_8cUIM8v2_RviGW01pnTkxwB6Y3j4V62czHZJtDle8yyeDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار آزمون: ایران هویت، قلب و افتخار من است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/Futball180TV/90109" target="_blank">📅 22:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90108">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🔵
مجوز حرفه‌ای باشگاه استقلال برای حضور در لیگ‌نخبگان آسیا صادر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/Futball180TV/90108" target="_blank">📅 19:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90107">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTJ4yBw516P8cayb5ogYclwnJ30GKvczHZLfssr_NJI_-C0P0tWC9Cyv35FoFRoBlJG2SUsERihJhYv_TV1dLIFqJJfUAVcBI7eltgSxJCL458tIVaLjiGCbrEmResvpTaBREy2an0sIPAnKn45CVmZPBqhlXBv0uqkYW_ztpLpTYFaj1ii14pzff67tFfnhh-YRqMoI-DwACipNQQUOfTU-P-t9xvmIcR4DYerSp7IbUhKxGPx43EoZhuNjPLifvM7MQQ9b4seH-_45Fq5egA5myruJ0MP1gq4-bcHuawkN9oZ4DMHK4cFBgz1ExwdcLAfseC53AnjgwiFMeeYHXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید کریستیانو کریستیانو؛
همان شور و افتخار همیشگی؛ بیایید همه چیز را برای پرتغال ارائه دهیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/Futball180TV/90107" target="_blank">📅 19:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90104">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ca121cc7d.mp4?token=uZ8LhZi4HD7lSkopLskhSgueAcef8GO8LCwQgA0J3QNgVlbvuPchcsy0wLS7DWPv008KqL7Nh2aUINpsBMx7NVpf9D-lmVlKDiAsFa7sUZZRCpKeHqfik-FzUMLc7fkcxNmFZunpE-d9AHAq0t5t2xvpAACQNMBkckB2mCISdmvFkNNSg9qHDm1-2hudQNocqhYhhsinkGdi09AR9bHIw1SD1S7ZqIBWgVuwZW6-RpUwwtE2nsYJnBRjgjP8xNGsRa-P5Gc1F4-xRbCaHWg7EfdRtYcYWyaXrpXPrXbeIEVXTnPtcDjVr4Ou7xk7wi_ZBRTvQxtl75ZpCgTr7-oITA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ca121cc7d.mp4?token=uZ8LhZi4HD7lSkopLskhSgueAcef8GO8LCwQgA0J3QNgVlbvuPchcsy0wLS7DWPv008KqL7Nh2aUINpsBMx7NVpf9D-lmVlKDiAsFa7sUZZRCpKeHqfik-FzUMLc7fkcxNmFZunpE-d9AHAq0t5t2xvpAACQNMBkckB2mCISdmvFkNNSg9qHDm1-2hudQNocqhYhhsinkGdi09AR9bHIw1SD1S7ZqIBWgVuwZW6-RpUwwtE2nsYJnBRjgjP8xNGsRa-P5Gc1F4-xRbCaHWg7EfdRtYcYWyaXrpXPrXbeIEVXTnPtcDjVr4Ou7xk7wi_ZBRTvQxtl75ZpCgTr7-oITA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
ترامپ : الان تو اسرائیل ۹۹٪ طرفدار دارم. می‌تونم برای نخست‌وزیری کاندید شم، شاید بعد این ماجرا برم اسرائیل واسه نخست‌وزیری
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/Futball180TV/90104" target="_blank">📅 17:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90103">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dc000d4d3.mp4?token=hGF6QcZpuk4dzAWjYlyyxgwm8q06hRrqd64UOcadW0ROIF7RjseWbBhcSmOp0WR8qmKjoAinsII5GjTp0KIlRIXWMyJgMA8HiugMrckhoYuu6-tp_u9j6tbVvXbsRGBi0wUj7rjaUrmUM8sEtMsi4aVC0JfwJBWX5B7Fo325fGYay20D0dmpH_3XHEoQB7ph6bpK0S-ihiGeOehCMdb8V8RdL82Ru_C_2P-EFECf6E-9_iGaXXiFL0eh3cUp2cmy4LAJ16lFLxTDIQVBCd_SRew1aUL8_WtljYW-nOam8F2nd_sTGvFaEBuwXUDsf4TLEonRsFb80bMgrOHwZlMhlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dc000d4d3.mp4?token=hGF6QcZpuk4dzAWjYlyyxgwm8q06hRrqd64UOcadW0ROIF7RjseWbBhcSmOp0WR8qmKjoAinsII5GjTp0KIlRIXWMyJgMA8HiugMrckhoYuu6-tp_u9j6tbVvXbsRGBi0wUj7rjaUrmUM8sEtMsi4aVC0JfwJBWX5B7Fo325fGYay20D0dmpH_3XHEoQB7ph6bpK0S-ihiGeOehCMdb8V8RdL82Ru_C_2P-EFECf6E-9_iGaXXiFL0eh3cUp2cmy4LAJ16lFLxTDIQVBCd_SRew1aUL8_WtljYW-nOam8F2nd_sTGvFaEBuwXUDsf4TLEonRsFb80bMgrOHwZlMhlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جدایی رسمی برناردو سیلوا از منچسترسیتی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/Futball180TV/90103" target="_blank">📅 17:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90102">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/252c545abf.mp4?token=bru2CNkhAtA_DEBRFW8n2aFY4TfiXgOasWfjvt8X8IksWb_CL3K8m_2FQd-B5pa_tQQE_2IwxtPlr4dgBmYQWlToU16qLycZf3ppk771XquhJnvHsrMKKkLh6epCOT09qE7UKKsWu0xHapQNjoGS_10-Hsz7zYlI82nSG09Iiku8rSdrUDWIJE2MtmoTB85rgw4029au-k5PGFbhFDxARVhYW-pgO8wPOpGhaAHR6gskrtm-MTzGA834S7Nk6CZYn_rhVE9NVrpFSgbx7sVeSHFs0IrHZqXlYxcW5RC8kuJsGw2oNepdh0Phg1uyvyr5bKdTozTWYUEU29Ym3Xt4vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/252c545abf.mp4?token=bru2CNkhAtA_DEBRFW8n2aFY4TfiXgOasWfjvt8X8IksWb_CL3K8m_2FQd-B5pa_tQQE_2IwxtPlr4dgBmYQWlToU16qLycZf3ppk771XquhJnvHsrMKKkLh6epCOT09qE7UKKsWu0xHapQNjoGS_10-Hsz7zYlI82nSG09Iiku8rSdrUDWIJE2MtmoTB85rgw4029au-k5PGFbhFDxARVhYW-pgO8wPOpGhaAHR6gskrtm-MTzGA834S7Nk6CZYn_rhVE9NVrpFSgbx7sVeSHFs0IrHZqXlYxcW5RC8kuJsGw2oNepdh0Phg1uyvyr5bKdTozTWYUEU29Ym3Xt4vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چنتا شبکه‌اجتماعی غیر معتبر روسی با این ویدیو مدعی زنده بودن علی خامنه‌ای شدند و گفتند که به این کشور پناهنده شده :)
❌
سطح اعتبار این ویدیو : 0
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/Futball180TV/90102" target="_blank">📅 17:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90101">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
⭕️
⭕️
🇪🇺
تمام باشگاه‌های لیگ‌برتر ایران بجز پرسپولیس و گل‌گهر سیرجان با ارسال نامه‌ای به مراجع مرتبط خواستار لغو ادامه مسابقات لیگ‌برتر و مشخص شدن تکلیف نهایی تیم قهرمان و سهمیه‌های احتمالی شدند
🔵
این تیم‌ها با عنوان کردن مشکلات مالی و ...، موافقت خود را با قهرمانی این‌فصل استقلال اعلام کردند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/Futball180TV/90101" target="_blank">📅 16:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90099">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qpn4Ay5bsslK_Uv_OPiKG1qPG-lQ18ToxOH9CzDdm4SnUywkeocZ22_0SKtf-6EGzI4050QyWNQkRL9Pf3nXhDP_DBSCV9OgpkEe12jpIrl-jk5fjoMciYsKKsK6M72jhg_wrre42hBngKSfVHRe_-nR_7pxTV65KcNo9HaDp-uZJHwsb9UM4rd6CTFawxw_QVu_kRa9-LkRFem9gmM4mpXdCHa3fQE-h2ShqgeQgCk5MBLrQOnKrOhN-AtzLTs5TwIF8a8OEvFhm7FLL5EsSCg6TpWW_QY1DrdZORIfL6xsqwPMhM1ZH5o62Wwlw9yynWquIurQnP5TAgT48k5VUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CtBnKU2Y64cFeoM1aQTbKXZ6Se0uV-fMpofNoMEGCecdopO3dwgfarC4odBQUbGCMIwkofq-kN0YFEX5NWEOPLMT5n6URueqFvQ_L-tjkJDhmb3-5qzL4Pbi6o0ruAXuV-N7MZo8R4CgaAXtk0Q5EuWBesxYdAGz08mzaVg05s9QDSI4BAj79n6tMpSN20KMJXBqBdhAZflRLeZ-nJOoq1qO9ImqUE1f51SDjsTpKIVeO_kgILy7focCMSlRd1HWSE6Rd8TcYz4cjz7fGdPcOYC5s9KiNXnke7lVfK2v2zMFgv-fbcxBy12SMOuNkcmZj8pInkdXFZmOHKSgaQhmqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینس گارسیا بلاگر ۲۱ ساله اسپانیایی و دوست دختر جدید لامین
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/Futball180TV/90099" target="_blank">📅 14:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90098">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
⭕️
رشید مظاهری سنگربان شریف سابق فوتبال ایران در حین خروج از کشور در فرودگاه بازداشت شد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/Futball180TV/90098" target="_blank">📅 14:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90097">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ece86e352.mp4?token=rIapx1jYMywzvPavYoBtTPqKjqWYnQHe96mhhykXhiTOF6F7HvlSm3uLjdCui4iTRMYSEfAlf5q6wNhPZronIrkKVBYpcM_LdA_srKiSKMJn0_aoJs1ssIu6pPfyRmsXNCRmutwBWPy5VT8sblnrexCf43oxIxfP8IaQwqMjntxFwil4o0emR6l2yl1dAbIcGBGrmxwEHw8q7pl3Z5jPkQLwVwiOmkt635ns0VxDwaMMDymdSIF_ACYyKlt6ulUWDJt8YuVz9Q5ys8S1AG_JSzHzOJ8j8FZwAUVHmS-9VBiMDWCI5V906QTzhmHIGyEmKQN4Z3azZlN24ZoD2AaJ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ece86e352.mp4?token=rIapx1jYMywzvPavYoBtTPqKjqWYnQHe96mhhykXhiTOF6F7HvlSm3uLjdCui4iTRMYSEfAlf5q6wNhPZronIrkKVBYpcM_LdA_srKiSKMJn0_aoJs1ssIu6pPfyRmsXNCRmutwBWPy5VT8sblnrexCf43oxIxfP8IaQwqMjntxFwil4o0emR6l2yl1dAbIcGBGrmxwEHw8q7pl3Z5jPkQLwVwiOmkt635ns0VxDwaMMDymdSIF_ACYyKlt6ulUWDJt8YuVz9Q5ys8S1AG_JSzHzOJ8j8FZwAUVHmS-9VBiMDWCI5V906QTzhmHIGyEmKQN4Z3azZlN24ZoD2AaJ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
شادی گابریل مدافع آرسنال با خانواده‌ش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/Futball180TV/90097" target="_blank">📅 13:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90094">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnhYhWpgjzqNXXXFaIg-u6HCPTp6h3y-2j-HUW972D98v2T47naGwdh8yWy5xggswgkJbY02q2PBgUMUAJdhGd59p-6urSLZKSAORlLAvJVpuABZcnX00wgqi36picZpqT-ftDyCmJYwNI9nRKBqM28Fl2fwFZbGqipzHDjUCeD8YFwVqapobUaALNGCcoROKQ6MX-zkjK2t2BQYYFd3NkHoKZj9nhv1ZrpMYMaAlmm5Y6AcXO2dhhDQnkBN47XZ2xsAq9t8dmjloM_oSKx1zDYFtP6Z65N-gDBrsRx_RXFnnKGU9CdBTzI_qH652-TXanztmRv5SJ9TrLcRKXgZTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
توییت تاجرنیا در واکنش به شائبه‌ دخالت غیر فوتبالی در تعیین تیم‌های آسیایی: ‌عدالت یعنی سطح دسترسی به قدرت سیاسی، تعیین‌کننده نباشد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/Futball180TV/90094" target="_blank">📅 12:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90093">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56d546629.mp4?token=Z-zTotQHE8mREeqk4b1xmw3U6wX2JmCFSPPm4NhQJLxHUb8uGwVF93_nl116SzchYNkLUNOtGsHT3aZ0Dzxtfj0znju-Y1hfTFVCfSEFNAgNcqrtseaiCLgMwVdC42cQ2rQWNzYBd4g78lBPamQyPnaHjnIbAGW3TsZpPNCIO6XoOA633NFjy0LlDxBKm5fRQUUcfVp95V4zsYQJYmKIGcuJxbTzu0v-NCuW1ycOKTWJ5SEs5n6D_-7M2LIDF4hEZaPuiLiJoFSnsMdeSkYVhKVY12-aTSXNl0JQr7VZIZPC6xuPAmvTab0vroR5OAfXIStZ_sXgkIMy6tmNx9sVcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56d546629.mp4?token=Z-zTotQHE8mREeqk4b1xmw3U6wX2JmCFSPPm4NhQJLxHUb8uGwVF93_nl116SzchYNkLUNOtGsHT3aZ0Dzxtfj0znju-Y1hfTFVCfSEFNAgNcqrtseaiCLgMwVdC42cQ2rQWNzYBd4g78lBPamQyPnaHjnIbAGW3TsZpPNCIO6XoOA633NFjy0LlDxBKm5fRQUUcfVp95V4zsYQJYmKIGcuJxbTzu0v-NCuW1ycOKTWJ5SEs5n6D_-7M2LIDF4hEZaPuiLiJoFSnsMdeSkYVhKVY12-aTSXNl0JQr7VZIZPC6xuPAmvTab0vroR5OAfXIStZ_sXgkIMy6tmNx9sVcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداوسیما: هر کی جنگ نمی‌خواد، جمع کنه بره‌‌‌‌...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/Futball180TV/90093" target="_blank">📅 11:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90092">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🟢
باشگاه آلومینیوم اراک بدلیل مشکلات مالی در آستانه ورشکستگی و انحلال قرار دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/Futball180TV/90092" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90091">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e96fba692.mp4?token=v3A6LyQ-cH8MFV700SNpBhbwe9pZXR06cD9LvMcSMZ34sM0_FEEW3GSacz8f0LW-VWB3Nud1tA5Kx-ZjCum2TedLKpP-xLB4bxGXKqi-tTGyiavQe8HM1FlAhuLMDn481PGrKx1Zm60j3p9C3SnkCveK9F21kgsx-xVNBEFX_P9sMsMBhBE8EalPwfoNO1rhj0QOEeSpOMiw50YrkpM_RHJ5bcBnWVxoomcYknM6osaIze8_hBYEnAK607vtku5yFQ0DYjVlz3rBLIUBosom5C8s5tX1B8FY1JjrWFhM9MrKmq8LQr6dJDdSeNH9zOg1Kj7eQW2cvs_JmmGA1oE3PzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e96fba692.mp4?token=v3A6LyQ-cH8MFV700SNpBhbwe9pZXR06cD9LvMcSMZ34sM0_FEEW3GSacz8f0LW-VWB3Nud1tA5Kx-ZjCum2TedLKpP-xLB4bxGXKqi-tTGyiavQe8HM1FlAhuLMDn481PGrKx1Zm60j3p9C3SnkCveK9F21kgsx-xVNBEFX_P9sMsMBhBE8EalPwfoNO1rhj0QOEeSpOMiw50YrkpM_RHJ5bcBnWVxoomcYknM6osaIze8_hBYEnAK607vtku5yFQ0DYjVlz3rBLIUBosom5C8s5tX1B8FY1JjrWFhM9MrKmq8LQr6dJDdSeNH9zOg1Kj7eQW2cvs_JmmGA1oE3PzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
واکنش تند مامک جمشیدی، خواهر پژمان جمشیدی به خبر منتشر شده درباره صدور حکم پرونده برادرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/Futball180TV/90091" target="_blank">📅 10:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90090">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔥
خیابان‌های لندن در تسخیر هواداران آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/Futball180TV/90090" target="_blank">📅 10:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90089">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7pWnGt3cVa0j-5UTMbeWuY240P5F4Qy5GRhSVcvDWuBNaie0pylB7YZ0RLG2Phi9SWXdKksp8hTW2Dg4szHF2mX8QReek3iU2Evp7xJEJMai8xXgSlNvTkt-JfWFuRr4pysRy3m8tzahJnG7agCLLKVsDAppsrtyVT7gUXJiTh-t46kiRymYl_sS3eG95XdpSZkSeMQmBK4orM6nJNd7RfVFAEZd8uO8mCFRdNdNk5Omh9WjUp7zQUwTzqQDQsNGAOvHHoe-Yx7B_QXlJcAWQps7tCys4iovZFeRDlAxevIEW-Ei6xgeFlEdLKnf_bslZColPnQ9Phy32MStnholA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد مسی، نیمار و رونالدو در ادوار جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/Futball180TV/90089" target="_blank">📅 09:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90088">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f7578a72.mp4?token=GRXwxacVNjPirhDKzJ2N0l11HA5sTUXOLrrhLfVScXK7lAnb3qVmTvuMZRfdZStU9TMbbUdUV9p0Sd__qUKxcLLs5P7uELuvVYifL4LljO6pZr1bp5hwLVmPX4iUMcL-LzyG7DPuXtC-5-Vk8uEWsq2ZWgVo0DTC9Aeg4oiKz0pFBlzUmnrgq5I9s76UH3Na3zs8u2UOA5ZqfwscLgtlvuLcEMCM_6_u1rD2vnOglsRvkHM73GuxUDCBTSF9QwBiMdyM8dEqmAo_9FPKOcIOzJQRDPqpGS_9cWpjPZLP8mWmy4LPyV_Yb-5CMzBLaZAMocUnb3GYZsmd1m4t-eVI6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f7578a72.mp4?token=GRXwxacVNjPirhDKzJ2N0l11HA5sTUXOLrrhLfVScXK7lAnb3qVmTvuMZRfdZStU9TMbbUdUV9p0Sd__qUKxcLLs5P7uELuvVYifL4LljO6pZr1bp5hwLVmPX4iUMcL-LzyG7DPuXtC-5-Vk8uEWsq2ZWgVo0DTC9Aeg4oiKz0pFBlzUmnrgq5I9s76UH3Na3zs8u2UOA5ZqfwscLgtlvuLcEMCM_6_u1rD2vnOglsRvkHM73GuxUDCBTSF9QwBiMdyM8dEqmAo_9FPKOcIOzJQRDPqpGS_9cWpjPZLP8mWmy4LPyV_Yb-5CMzBLaZAMocUnb3GYZsmd1m4t-eVI6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
رختکن آرسنال دیشب
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/Futball180TV/90088" target="_blank">📅 08:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90085">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4882a411.mp4?token=dRK4xRmMVUBwZzCZoXSQv3nzZgikWcoRKzBWCPWwAonv8u66KrjSSHwiuwpl5HSiK0-dXzqUW6e9LqLPMvE5LrN_USqxT_kIvep39a0rN7WfKlbLTXViWu8GMl9gSdpZmbZgdXo2dCcA0S3Yo0O05MS0jAy4ywdV-5gmTxqhPqazBZVstX7BdQpxb3Hygih6qv7aRUEgpcPRd5H2JPKSilxIV_ADsY4auBAYqZUyBS_FqXj7wr-wjc2bGCk7GaADrPM5c5FN2OtcZjyKj3TZuz4GJHNFzS41XRY_H71_syZaPfyrcVlBSznZdFlhjgEXsOQkAC3IMYLLwcAdpTGEhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4882a411.mp4?token=dRK4xRmMVUBwZzCZoXSQv3nzZgikWcoRKzBWCPWwAonv8u66KrjSSHwiuwpl5HSiK0-dXzqUW6e9LqLPMvE5LrN_USqxT_kIvep39a0rN7WfKlbLTXViWu8GMl9gSdpZmbZgdXo2dCcA0S3Yo0O05MS0jAy4ywdV-5gmTxqhPqazBZVstX7BdQpxb3Hygih6qv7aRUEgpcPRd5H2JPKSilxIV_ADsY4auBAYqZUyBS_FqXj7wr-wjc2bGCk7GaADrPM5c5FN2OtcZjyKj3TZuz4GJHNFzS41XRY_H71_syZaPfyrcVlBSznZdFlhjgEXsOQkAC3IMYLLwcAdpTGEhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارجدید حمیدسحری با کپشن:
تاج‌گذاری میکل آرتتا در لیگ برتر.
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال قهرمان لیگ برتر در فصل 2025/26 شد.
🥳
⚽️
Channel:
@Futball180TV</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/Futball180TV/90085" target="_blank">📅 00:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90082">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7eae73a44.mp4?token=gYmkh33Hh5YG_4praVlXGxnOt-yBXQDF4ovFJmJzxW4KGWh7B5h_508uP11Nc-CkxMv2TetS_McIP1Z3sZKwuTE2dFE4Bkz-0P_y7K6LXcPEk_-T7kA7lcOs9UEQmMRfFFaoNYbzE9V514iNg7M3mYj4NvyMJLkI4xPtcBmj9_ZksEqX6eyqDB4PwVZeW8tc5wCRlPxzql7a9XpHPHMZtxlUx_rlSe4L36B9pLqA6nbDmAx5wLL1vMAGADwaguP4XqIw7E25FmSXQ3XnQ3Q6go3o3uI95Rz6Grh_1WepCUzY4HZH8cJhOF_hps39nJNUpAE2YAfF__9lGAJRvxH4cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7eae73a44.mp4?token=gYmkh33Hh5YG_4praVlXGxnOt-yBXQDF4ovFJmJzxW4KGWh7B5h_508uP11Nc-CkxMv2TetS_McIP1Z3sZKwuTE2dFE4Bkz-0P_y7K6LXcPEk_-T7kA7lcOs9UEQmMRfFFaoNYbzE9V514iNg7M3mYj4NvyMJLkI4xPtcBmj9_ZksEqX6eyqDB4PwVZeW8tc5wCRlPxzql7a9XpHPHMZtxlUx_rlSe4L36B9pLqA6nbDmAx5wLL1vMAGADwaguP4XqIw7E25FmSXQ3XnQ3Q6go3o3uI95Rz6Grh_1WepCUzY4HZH8cJhOF_hps39nJNUpAE2YAfF__9lGAJRvxH4cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💙
سهراب بختیاری زاده سرمربی استقلال: یک ذهنیت به وجود آمده است که پرسپولیس عادت کرده است که بعضی وقت‌ها با فساد بازی را ببرد یا به این عادت کرده است که همیشه دستش را  به نحوی بگیرند و کمکش کنند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/Futball180TV/90082" target="_blank">📅 20:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90081">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pn1NuOG0EcvbwCvTpmvyjxNh9mr_7rnceWPWQlWwwE5bGcJHVyAdSMAAyPK9M9EFIVqn90NVEL5iUmyIJLKOyZtuUkGccqvG-Gux0AtxArac0EfH101i4uRtXCAHTFhvVTfFSfbs_j4c2ZIB3RNQ98GNnt_P3r_qJiKByRR0JaiyQhti01NGfFciJbTKVjaENfcgiF9QaUPcr7kMWSJiXBYGhp1Oj7pDH2buPdrtrj6AYEi6BP-e26gL08Xyhm5vsNDfleuqTe1_FyrTSRRQyctd1iTfPwXl5oLNy_IW49qRvWMT0_HMdgvq3Inj9U5WD3FCcCp6VXtTpJXb3m4rLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
از این منظر نگا کنیم؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/Futball180TV/90081" target="_blank">📅 19:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90078">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd848eb99.mp4?token=f0Npn1-r61KcnhSFOTDslmGowZW6qm5KUh4DgDlp_et8fDdQorbIEtgJDcfFXR5VtJ7AANblAlbhFTu32amRgsQ67yZOYcOO6burt_84M82ZI0cRcPHj24jl3WRA5nB1KhyX7lGFII8K1QikvDBtV-sjCyrJRmgTrv8ohHnHHaLhD0NkZsr89IOXmQvl8h9B2JQmZb9j_IwviQGW_1g9MX_TsHavbnoFTxPrTZYuEve_6OTbvw3ZklJUBWTTaOIYnGWPpArbKUcDo-JQOC_qnmATCr8H3j8P_-9DVn0lAwOJQaMp8ajSPE5Uh_yeX9hwcKGlQcC2LSTQJ431HtJ3tTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd848eb99.mp4?token=f0Npn1-r61KcnhSFOTDslmGowZW6qm5KUh4DgDlp_et8fDdQorbIEtgJDcfFXR5VtJ7AANblAlbhFTu32amRgsQ67yZOYcOO6burt_84M82ZI0cRcPHj24jl3WRA5nB1KhyX7lGFII8K1QikvDBtV-sjCyrJRmgTrv8ohHnHHaLhD0NkZsr89IOXmQvl8h9B2JQmZb9j_IwviQGW_1g9MX_TsHavbnoFTxPrTZYuEve_6OTbvw3ZklJUBWTTaOIYnGWPpArbKUcDo-JQOC_qnmATCr8H3j8P_-9DVn0lAwOJQaMp8ajSPE5Uh_yeX9hwcKGlQcC2LSTQJ431HtJ3tTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
۵ صحنه بامزه از گزارشگران عربی :)
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/Futball180TV/90078" target="_blank">📅 17:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90077">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2bf46e469.mp4?token=bW9Hs0l0HbXAAj4Wf9Dii9PyQDJDcP36tfaiWg_3HTPaVOh2TLDOjXU5LdUkTkp1GIcOITVAeXbfPAp1QFP1mcFQ0bT-V17UDrIjJA6_OfyfbnwwcHepyQ8yIBPnp5qvq47yggQglRs9gjX1aTSCDYRnH7emkz023wHu5bdm8AQknGmq-yymEJ-eSPP5lgvI26fweuA6LguXKC1ZJoagZvWYAhzKDStAnvgI0HV8Pt16qjH4N_AoybcttnxE73IUbW4Qr-lnnggwt9rtAc1yntjKG-ObkNZp2qsv3bPFk4C83oXrVoQB9auls-H_yGZX67-GO_pcrHAXOg0ulkSTcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2bf46e469.mp4?token=bW9Hs0l0HbXAAj4Wf9Dii9PyQDJDcP36tfaiWg_3HTPaVOh2TLDOjXU5LdUkTkp1GIcOITVAeXbfPAp1QFP1mcFQ0bT-V17UDrIjJA6_OfyfbnwwcHepyQ8yIBPnp5qvq47yggQglRs9gjX1aTSCDYRnH7emkz023wHu5bdm8AQknGmq-yymEJ-eSPP5lgvI26fweuA6LguXKC1ZJoagZvWYAhzKDStAnvgI0HV8Pt16qjH4N_AoybcttnxE73IUbW4Qr-lnnggwt9rtAc1yntjKG-ObkNZp2qsv3bPFk4C83oXrVoQB9auls-H_yGZX67-GO_pcrHAXOg0ulkSTcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
شادی نیمار از حضور در لیست تیم‌ملی برزیل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/Futball180TV/90077" target="_blank">📅 17:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90076">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tSlxPvr8t36H8HtkUe9VlKZrKvuq5wvveHz5AEemktq9Vav10UE-QKPy2bcVaydfVlHalI-7rsLcswQEFWPsMDPgb9mjzch60WG2zQ9sbIa_zxqSQq8yPQV6eKJGx_ZjlY6QuQL6PWuB-bMC7ak0HObxAdRwC8-H4SNGc5Bw0TM-P6epfG2DBSE9uvkdHJNGj4_vnkwCQBGAMeO7P4kkmuDG37_La5_RgfXxMuLoIu91N5l0QheedBg820hWSlJ4DLEZQu9uTi8EpsooaZG7Rb0W4EZEBf9I5QvT2cL9TOH-bqh5WSWWjyIXKGgvPAh_4zUgajV6oXYvMQ3cBcoJGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
لیست تیم‌ملی پرتغال برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/Futball180TV/90076" target="_blank">📅 16:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90075">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe3576e35.mp4?token=Exjs33vByN8nvW-FIBRpIxjPxitxqUBVJYsyEXvOzTKDmAlW22GKACw14w8E13ssso1gOQJa-Mo9Slly2ZXjZKwEinxYvFjkUS7ocDt9p-0-jZlSVKJZmI2n4R5rJehE8CgwkR2h-yNHyIMlVo12rBqfCyQDb1nS-naxVfm5vI5yN1xYq12ifyyWwpza72B5CStpDCM34g4c-x2cbR9PpIeu2drnUTpI6PMN1eEXMHGtFI71pQb8_JLjZCYCTsTCT-g4kcgfPIbbdHVTl_NqnBJsEqN1lk8eFfuszXVqTpsZlKSry8Py7q5_E7TfMItuPt_tiL6EREZmtlh3roKNFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe3576e35.mp4?token=Exjs33vByN8nvW-FIBRpIxjPxitxqUBVJYsyEXvOzTKDmAlW22GKACw14w8E13ssso1gOQJa-Mo9Slly2ZXjZKwEinxYvFjkUS7ocDt9p-0-jZlSVKJZmI2n4R5rJehE8CgwkR2h-yNHyIMlVo12rBqfCyQDb1nS-naxVfm5vI5yN1xYq12ifyyWwpza72B5CStpDCM34g4c-x2cbR9PpIeu2drnUTpI6PMN1eEXMHGtFI71pQb8_JLjZCYCTsTCT-g4kcgfPIbbdHVTl_NqnBJsEqN1lk8eFfuszXVqTpsZlKSry8Py7q5_E7TfMItuPt_tiL6EREZmtlh3roKNFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خدا رحمت کنه زنده‌یاد علی‌انصاریان عزیز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/Futball180TV/90075" target="_blank">📅 15:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90074">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1631168f15.mp4?token=lv4WHNDdv7xqnbaZYgfgkCaBVh01vTZRQDuerX_sTMLN8Nes8ZjHfskkjMEcWXGlhJViPSau8OTaF7qbTj7j3IYnR7ygyR0RSzY6CWRnhh3nElUaH0GfbpDPWB2mRdgwVW8_0LELEJBjuDbEt6HSeOODQ7VoZdof_Ga_RRFjwIj6d4zBZlwW0QYS06OGc0y0Hf3NgcfOiQKOEvXQ-iJHi4WM6jWc3-eWNWVqANHmTpq1Bjpv9woFCED9PzMkFR42no91wq_zekO7BC-3wHC5YESrexyL7aJ1UL1ezKsWg2L_Cv58SeHgiFxEMXX-lnB3rGAJe6OhVJB6l6DWtZsRxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1631168f15.mp4?token=lv4WHNDdv7xqnbaZYgfgkCaBVh01vTZRQDuerX_sTMLN8Nes8ZjHfskkjMEcWXGlhJViPSau8OTaF7qbTj7j3IYnR7ygyR0RSzY6CWRnhh3nElUaH0GfbpDPWB2mRdgwVW8_0LELEJBjuDbEt6HSeOODQ7VoZdof_Ga_RRFjwIj6d4zBZlwW0QYS06OGc0y0Hf3NgcfOiQKOEvXQ-iJHi4WM6jWc3-eWNWVqANHmTpq1Bjpv9woFCED9PzMkFR42no91wq_zekO7BC-3wHC5YESrexyL7aJ1UL1ezKsWg2L_Cv58SeHgiFxEMXX-lnB3rGAJe6OhVJB6l6DWtZsRxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
ناراحتی شدید خانواده ژائو پدرو ستاره چلسی از عدم حضور در لیست برزیل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/Futball180TV/90074" target="_blank">📅 14:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90073">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqYo6YI9U1tuye3KcE1STrI8_4z7qKz6YHET3rid7to5_yTCKUlAiqbjejaVuZDV3AObSDpHVJP9ZCcnELBSxQ_79hPTu4AR5HX9TtvDOeghkGufa3OsCaMC2Av3bqZV69oJzIC82F8LTPBta9BVEiBYvTYiiACQRA7mEezsJbdHKk0uRhzae6kMHB3JuBvt4i3rmPaBSewg9ZX-zgItRGI1eRyzxD0-0fXqT9afl7EvX30QR2XBPVE2fObW3IJI_R8-X0oaCT-WbB0-zUegITfbMhgCA8LtgOElRaGlw3xfm36c7hQ-Fz7dwT1tTHNPIBoX5tpgoy72c9ze6qgq0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رئال‌مادرید با ارائه پیشنهادی خواستار تمدید قرارداد یکساله با آنتونیو رودیگر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/Futball180TV/90073" target="_blank">📅 13:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90072">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AK2Oa4DtLDh9lFblgitdLW3P5EJBHLm7_tzU4sAA85Dcj8rFl40UTfD-pKqwJNlGQ30whgKFvgzhsoWkfLMKgP5uZeCprieHo8XvJNBbh-6NfNOVKSFMBHMgNEZQQaudX7YqKkwnhuGNpS_xMz3T9YZ-ygQ5w2r5ldJUkpSnJ40OEpBbO0SlV-uM_D8o2ryXmSGY3_E_lj2nJimOr1zuG_-nZG7EfpxOVo2VTm9-waLuBbGhLqgBbOlaE088Lnrc2GLp5Yhpad5ixbzBI7-WURw12P70ipyrj-6qsSf8i6SOVHNq4gaauLgHlNMhVcndQ5fCv_dBNlgovFaGIbBOsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستریونایتد قصد دارد با ارائه پیشنهاد هنگفت با لوئیز انریکه سرمربی فعلی پاری‌سن‌ژرمن قرارداد امضا کند اما در عین حال این مربی پس از پایان‌فصل قراردادش را تمدید می‌کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/Futball180TV/90072" target="_blank">📅 13:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90071">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c098031df0.mp4?token=EzWmqrRCE2jYmRzSAEh6Nj8epDOznUpC4Ae130nF_QmzVK9-H7RGPdnDvrgtPaA-M3xLKy2Ay85IrNxZnwnBcEfUpXb06VKF1yRvT3PRh9JY2EMojeveIP9iDt05EvAA8ectqB2JSH2N5j52l4kK-RpqO-8klEU1sK4-GLidpE6buKqwfc_8QpUUpCsD193jGQzehdqyOD2Wyma2w23tWaHUDqHQiAtH7ABPjwyESgh6m7xVZFpO2Rh3uza2KvLEClb-_ue0So0FIsSq8XVFINKSMRDHARHyrrJABnPocun-MBql6N1ifC8VLiqdQyKJEcUeGi7x5F6-r2Z_KKu4dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c098031df0.mp4?token=EzWmqrRCE2jYmRzSAEh6Nj8epDOznUpC4Ae130nF_QmzVK9-H7RGPdnDvrgtPaA-M3xLKy2Ay85IrNxZnwnBcEfUpXb06VKF1yRvT3PRh9JY2EMojeveIP9iDt05EvAA8ectqB2JSH2N5j52l4kK-RpqO-8klEU1sK4-GLidpE6buKqwfc_8QpUUpCsD193jGQzehdqyOD2Wyma2w23tWaHUDqHQiAtH7ABPjwyESgh6m7xVZFpO2Rh3uza2KvLEClb-_ue0So0FIsSq8XVFINKSMRDHARHyrrJABnPocun-MBql6N1ifC8VLiqdQyKJEcUeGi7x5F6-r2Z_KKu4dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
پاکتا هافبک تیم‌ملی برزیل و دوس‌دخترش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/Futball180TV/90071" target="_blank">📅 12:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90068">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZA3t2X30yNqdZAA_7t9BJpXKhfcdqy_QA_8gjiPAtJdnLape45ekyrcom4CuWXWh7KcdvnOyiKif8zLvz4JzAvKydX8pYN52IXnlsTgyvkFKRaeZepi0SB2IDZVvVntKnthnf9t_-76t4UXktIkQ0mC8ZoW3qofrj3NoLKGSbZ_5n5mNTpxz73ijNVyKbjNGi0ggBYUVA197bof-1QV5daRj9axOJSom2_ZWz3jlsQ6fFcB95fvK57sQ1b4NdeMYDuFvXy6z8RrmeNEpYUpJyWW3W0tbbCCssY8gEOcPjgXGfqoFhAz60qyGHUWSYditrxesUCdVQsPgRy8EGXiQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
کیت‌اول باشگاه اینتر در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/90068" target="_blank">📅 11:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90067">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y569r41q-ZSJcuFuYFzu9hvDZcTT5hSdFtP_Uf5aIVDPet3OXru3j5WPsT8PDNpGvTLsoURYPIGyEj2P9OlT110ZBfCYzzikPd_tSp-uFXfvlX-itdLQnf0L4_P2HveEvMBMn1mftbeE3be-3GV8IZVNyEeHfLJJJzcGi2hbeWf0uNoxsShkOhpA8_QweY9l_A9Rkik2yNCAHCm7RYvq6oxnK0G53-r7fLxniu7r61g_h7r8F6e8w3MfnQ6V4SdF8rPPysv8htLdQvqwT3w_9qlPPdTzeUTZ8fywX8lWMUo1qbFwO7IAIxdm9sKfw1aup02sIC_ra1D0tsPUB2TGvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌اول فصل‌آینده لیورپول
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/Futball180TV/90067" target="_blank">📅 11:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90066">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1fd62d6ae.mp4?token=SQciciulvSumLwizFXy_dxs9BoMS9NtNY8M3VI8jiP1oHnaZhB8XCUsbvd7PvjqStU5F8_-Fbd8rcVGEx7sb4GGXNd8ndAPNbAKL8l922ytT7zkh4pEADhcsxr-p2Xr84lGKhFoh9yejjD9SU59FpFRRmxz9sluMoa8oMYQHsXGUUYnYraCS90ukPN9ibNvzVRRC6Vs_pxgC69UHRPzqoZv7LNrOytUc3ZaYO5djHMJTgudei5FC_5XW5a5K4C6Brokd3Gap0MGkHuAMGt78jajShfIN9OMkLcNcSCaovRatyGVkyzQ9pHA7yXzljQwfkg2zvsr0bUwAMRUDWYgM1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1fd62d6ae.mp4?token=SQciciulvSumLwizFXy_dxs9BoMS9NtNY8M3VI8jiP1oHnaZhB8XCUsbvd7PvjqStU5F8_-Fbd8rcVGEx7sb4GGXNd8ndAPNbAKL8l922ytT7zkh4pEADhcsxr-p2Xr84lGKhFoh9yejjD9SU59FpFRRmxz9sluMoa8oMYQHsXGUUYnYraCS90ukPN9ibNvzVRRC6Vs_pxgC69UHRPzqoZv7LNrOytUc3ZaYO5djHMJTgudei5FC_5XW5a5K4C6Brokd3Gap0MGkHuAMGt78jajShfIN9OMkLcNcSCaovRatyGVkyzQ9pHA7yXzljQwfkg2zvsr0bUwAMRUDWYgM1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپر صحنه بازی دیشب آرسنال
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/Futball180TV/90066" target="_blank">📅 11:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90065">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
قرارداد آرتتا با آرسنال در پایان فصل به مدت دو فصل دیگر تمدید خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/Futball180TV/90065" target="_blank">📅 11:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90064">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Amn5Tg1rF3HVxcCYpi6n8jXjiyGOQYOSpvHInsLXFaVLEEF8vysHBb4Vb7k0-ZpmfLauwi3JLR-5zrFjmOJ4SoMA31c7VivTGzr7qfoXpeQ6QTcbI9bb9x_vRHyED9v5pnlUDAGF5zRLEeJ6N51IMV4vos47K9GfikYOr1PRssRXHcoTMn1-25C_fk2bwB1OO-sNH04bGwKC_OpoIV7ncnhvapYXHK9vFKGISoO7w3tnKMcoiQAFDldgg977Ay08bhjPXTyzBPd_GWBLIzDh0nXh24Gnc63x-sQKPktdsQePvqHr4_HGQRhTAUpeurQP8LCYlgj6hYjwyC2KMuryuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
با اعلام‌فابریزیو رومانو، انزو مارسکا با عقد قراردادی سرمربی منچسترسیتی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/Futball180TV/90064" target="_blank">📅 10:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90063">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a4a423232.mp4?token=Es0oPVSYRCbIYdO30va5jlgonNfQ5x3FkL31KPyz4UaVMuaioWwb2beJofsYaUVqLhWybFUkCSY155KphT2BFc30_oCfAMU-KtpRMWgiRTkxTG3L4oNXL-1w0iiaZ-iEUhiiFDnAOSmERxC5GLpBAI8L1RoYTCpzGRuQiRB1I85mpB3y_zQLD3ev_U2mt7HJFlGqBk8pWyvCGOefLm7yIjFiPpzmQOuHsXEY79nJJctupIXySCr3P4v_ngl2RfH3flGiPIlNa20Xk0Ik8zAEQI_xeQ_XjPXahZlgRy5qEXZfpbDCRYJu0HanlNvtkOHHKMCjo8y8NqBwM_R-2iVOuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a4a423232.mp4?token=Es0oPVSYRCbIYdO30va5jlgonNfQ5x3FkL31KPyz4UaVMuaioWwb2beJofsYaUVqLhWybFUkCSY155KphT2BFc30_oCfAMU-KtpRMWgiRTkxTG3L4oNXL-1w0iiaZ-iEUhiiFDnAOSmERxC5GLpBAI8L1RoYTCpzGRuQiRB1I85mpB3y_zQLD3ev_U2mt7HJFlGqBk8pWyvCGOefLm7yIjFiPpzmQOuHsXEY79nJJctupIXySCr3P4v_ngl2RfH3flGiPIlNa20Xk0Ik8zAEQI_xeQ_XjPXahZlgRy5qEXZfpbDCRYJu0HanlNvtkOHHKMCjo8y8NqBwM_R-2iVOuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🤯
شادی فوق‌العاده برزیلی‌ها از دعوت نیمار
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/Futball180TV/90063" target="_blank">📅 10:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90062">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2da1d08628.mp4?token=rA4I4UVDEhcD3zRraiuBHPpslQ7selMkyHjLtpYW2dJ7jrAuy9n6Xs2e7CJj0VW6cYs1Z3GugigevysEh_eSZ-bU9UF7sKlO3XoIms4dat-GDSCpal0m_Dt0vrKomBi0dREYmMT4lTux-mIZ6uXhQTwFpMw6BuxHWwmwJ4G42MlocF6h0CtSEhFTrLdGL3ing_4zrfXjCpCRyNE6vYvuxAKLHfU93JxwaJUkoFU6A-VO7kuHn-j97JWFiPZ1Eb9gQvXkXlCe26uob5YUHafD4vLErwASc58r1KdYFHD9_6fIqhsqgukL2ua8mmgiMOuRG4pRWZJ4iI24xDYuYY9K8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2da1d08628.mp4?token=rA4I4UVDEhcD3zRraiuBHPpslQ7selMkyHjLtpYW2dJ7jrAuy9n6Xs2e7CJj0VW6cYs1Z3GugigevysEh_eSZ-bU9UF7sKlO3XoIms4dat-GDSCpal0m_Dt0vrKomBi0dREYmMT4lTux-mIZ6uXhQTwFpMw6BuxHWwmwJ4G42MlocF6h0CtSEhFTrLdGL3ing_4zrfXjCpCRyNE6vYvuxAKLHfU93JxwaJUkoFU6A-VO7kuHn-j97JWFiPZ1Eb9gQvXkXlCe26uob5YUHafD4vLErwASc58r1KdYFHD9_6fIqhsqgukL2ua8mmgiMOuRG4pRWZJ4iI24xDYuYY9K8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
خوشحالی اندریک در کنار زیدش پس از حضور در فهرست برزیل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/Futball180TV/90062" target="_blank">📅 09:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90061">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf11ae109.mp4?token=sGUZ2DO3s-xOg9mBKky2z-vLskBwwNJic-N715NOEKCCEeeX1RKlM00GYkCEiJvQLqemeGT8obqaWlker6coPAhS088uk3hHrWmjcf-J7woMgawZt4IrTZBkyVC_N61PN2PBf13jkg8xuxpze46c5jqXBwwYDAsfNPQ6XRfj2UsqM8LA5Aa-uMvUxX4AwH5rHA7vRVjbx_eJyKseQlht3gU2BjAo4Y6qTqZdp-OiWQ5Iu7EJfTbjaB-J9wNxLhon-yTtbhxRZe5wDlpJF87yseP_B0JnjYpkhWq_OT-CRfTdA-hTzqqc9eucm8loJsYj01wXsCTBOvEJ-d1UwZ5J1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf11ae109.mp4?token=sGUZ2DO3s-xOg9mBKky2z-vLskBwwNJic-N715NOEKCCEeeX1RKlM00GYkCEiJvQLqemeGT8obqaWlker6coPAhS088uk3hHrWmjcf-J7woMgawZt4IrTZBkyVC_N61PN2PBf13jkg8xuxpze46c5jqXBwwYDAsfNPQ6XRfj2UsqM8LA5Aa-uMvUxX4AwH5rHA7vRVjbx_eJyKseQlht3gU2BjAo4Y6qTqZdp-OiWQ5Iu7EJfTbjaB-J9wNxLhon-yTtbhxRZe5wDlpJF87yseP_B0JnjYpkhWq_OT-CRfTdA-hTzqqc9eucm8loJsYj01wXsCTBOvEJ-d1UwZ5J1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥲
پایان عصر لواندوفسکی در بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/Futball180TV/90061" target="_blank">📅 08:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90058">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de7e2f01eb.mp4?token=Q1N7-n-HUYumNIVeDDyIk11mrvarLsQuj3QdUfWHESm8BsrpzHI8n-suyiKvRAivzz3lgd6DYA1HyK0Pn1Wwxi8Dcx4vjV7kXyjxYwsIwYDGJ-MwjWVFqsR-pyRoFhL_ntLOiMcp9bACCSpp76f8NXVcW0cUH2uiqPWCmp8D7u7BhHYd6i-q3iW1_mkTusAfZLa7-t--yyHSwdUidDuRipk8UUv-ot61BCU0zxvIVWCik5yRpnf4G7BqaBj-2TarIv9HG5UatVt6MlyjUQwRwWLgxEBqA5KofodRJEEIV1utFba0EuBpU-p6Y4JOB7g9ptlNxlk_Pv3-PyZ2oWUDiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de7e2f01eb.mp4?token=Q1N7-n-HUYumNIVeDDyIk11mrvarLsQuj3QdUfWHESm8BsrpzHI8n-suyiKvRAivzz3lgd6DYA1HyK0Pn1Wwxi8Dcx4vjV7kXyjxYwsIwYDGJ-MwjWVFqsR-pyRoFhL_ntLOiMcp9bACCSpp76f8NXVcW0cUH2uiqPWCmp8D7u7BhHYd6i-q3iW1_mkTusAfZLa7-t--yyHSwdUidDuRipk8UUv-ot61BCU0zxvIVWCik5yRpnf4G7BqaBj-2TarIv9HG5UatVt6MlyjUQwRwWLgxEBqA5KofodRJEEIV1utFba0EuBpU-p6Y4JOB7g9ptlNxlk_Pv3-PyZ2oWUDiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😍
خوشحالی مارسلو برای نیمار
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/Futball180TV/90058" target="_blank">📅 00:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90057">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lu0prL5fFdlM9YC5NPrUyy7USuHioBi-_SgqTUxD07L--YI1eGPmOE8tTWYSoYHJaEVkclq22FsKekI62T4lu39i8E5e-JYLT-4QAeFn2-7OY5JOQNwPgYI55MliS5xegMPyhIm-ZyJF9zIujjzrzIYceQ6dnksVRX7wYuY-trI8ANF3gCKqsyLvtTzfMIsthP6lsCboLN71RVGjKwDUQgi23Kmhh9nURioJ9TCkWvtVoMjCLv25xEns8TcweOxPCOd7MCPqTyFm8ICtfDu5ETtHn6efVPZxydV-AsulWMp44aRBZk9hYU5UEOCa9WH8ryPkDsxV_Mrv9iUMc4B6Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول لیگ‌برتر انگلیس پس از برد امشب آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/Futball180TV/90057" target="_blank">📅 00:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90056">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5dl7gxcWw8MRgJgSlqrAceGK51VvbNuQdhftzd-Vn9fDJBKQsMoR20Clstcg0V9_UuumO4Q58vAZy8oS7whYoy7yBeip1BVXrr5TQ3lK7T4Wk5TxPtrJg8Z2kXQbdmN4qgw9aBE6W9V15Ld5WV_TYyCULyH9N-uMkmWKhySF3sgiqRU-jO77PN9G6dVbrFH4V26QZJBKDqWDzxLI2sUNnLgIt-n_vU_lJj43pwKHquef6WNOYrAWKoxbXQNv31zIO7-udb64ZDhRghjN9uQCvfP5cmv-rK51o2R-4iIHu_HJvHddv0ZYNy30PBn8z87ROyRVzsB8fCz-pjjTF6HAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
لیست‌نهایی تیم‌ملی برزیل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/Futball180TV/90056" target="_blank">📅 00:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90055">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYAPMdZxiQL0VFKKV41DvOBzM2sQLAJgphsh2yCRURVmYmRSfQlT7fjx71DDVi_NN3pna683vEf6ufLZgREpCufs215__G9_DAolN3iJcbRjK-HhJNDNRCRv-33jVBRX8ZJ_qbPlIzo3qWs2kR8Zxa382QUwV8GdrmJX8kgWaYeKJ6DSec7bv-8L0aHyyfzrKuUG6HRZ7Op6vI4vgtjEp4oB9PUljPFxBDdZPY3ggkGPV4lBebp8FFsHOIPFBZoteX96ZSAQWtoNPvQHYkRA78baPQERSziq4eySRnmgD7xIuDNROsX-gciDlk-P8Y_TZcYz6MJutfjroJn34-VfZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
نیمار بیو خودش رو به پرچم برزیل تغییر داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/Futball180TV/90055" target="_blank">📅 00:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90054">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6072fc8645.mp4?token=b_v2zMlb_1XEu0xgHyJcR7Hy0BzLGb6LN3w06XbpJOVzs0QMcoXyV9ThAAh9wrwkKkcvsAfKspTBINqDFBdFChmLFezSUPPUW_1qWOjn7DBR7qgyr5UU_Q4mLi8VKM8TmXQoKj3aEhSjSWqIMNDPx3mZFg29pKmd40w05bgBK3vHDd0vhtVaaI3GVZDxzhxXbHPmwqq4yt9iWYWDjCNyaXuANz2BY1PJIOKazSNXQQmuUE4_t3bc2zAzo-w7IHLyUU3S-InKJv0B2cdYsiAtCyWhBZdL-Brq6qe61cGILvvLH4ZMNJUS8SpUESSdoPgcsJEhFdJmv9e-NizBPOGUrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6072fc8645.mp4?token=b_v2zMlb_1XEu0xgHyJcR7Hy0BzLGb6LN3w06XbpJOVzs0QMcoXyV9ThAAh9wrwkKkcvsAfKspTBINqDFBdFChmLFezSUPPUW_1qWOjn7DBR7qgyr5UU_Q4mLi8VKM8TmXQoKj3aEhSjSWqIMNDPx3mZFg29pKmd40w05bgBK3vHDd0vhtVaaI3GVZDxzhxXbHPmwqq4yt9iWYWDjCNyaXuANz2BY1PJIOKazSNXQQmuUE4_t3bc2zAzo-w7IHLyUU3S-InKJv0B2cdYsiAtCyWhBZdL-Brq6qe61cGILvvLH4ZMNJUS8SpUESSdoPgcsJEhFdJmv9e-NizBPOGUrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
🙂
شکار لحظه‌ای صداوسیما از بازی امشب آرسنال که با برتری یک‌گله این تیم همراه شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/Futball180TV/90054" target="_blank">📅 00:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90053">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqSIwNmioP_sFD7SwPCUISNEQ1V5ba-xMyW6ysQDwAI3lDHd1KvuClwMV_FKLWc7tDcueNc1CqgTqzLAV_mTTHxxeoHr2kGc9jBfyhWtgtvOihdoRsC39d_CxraWadJ86gDlw_zXayYbftqzT7roIw1oxDHR-Sat2fYdsJA43fdJLwMaow-xofRj1IBRPtUYPZNXpjb5EHGuXBZxMz21DWxEqZbjtAS5okcJP4PSlTh-GOMKRA8hnk_4bBb6ELQ6jSbFHu7qJfm8gXL1WxJmF8BP6TnR0EWC2HLcQHwQs12ycjFcnSj0DAkkO-a1VbIZ9eOahwdK1NytT1BE3BKQZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
نیمار بیو خودش رو به پرچم برزیل تغییر داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/Futball180TV/90053" target="_blank">📅 00:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90052">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🔵
🟡
🔴
با اعلام سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان خواهند بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/Futball180TV/90052" target="_blank">📅 23:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90051">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
لیست‌نهایی تیم‌ملی برزیل تا دقایقی دیگه توسط آنجلوتی در نشست خبری اعلام میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/Futball180TV/90051" target="_blank">📅 23:38 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
