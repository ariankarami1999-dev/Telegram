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
<img src="https://cdn4.telesco.pe/file/fmhiJGaTNUY5IKvUKUKA1aTNBmwO4WtQL7ysil7pXd4bYB-HlQXGmeqtd2QtxqsEwpULODbnvU3W0t6LzvSihan8YGLE0jzYYiCsZeRTLnAr8DDvfWoIGcrAITyVFhTsr8m4VfPj9ojDZ2UuBUY1-ZtDLny5BjnkC4GSVoKRqaFWyuUHPjq2ZiQPqKzawZ5n5xR5jlWayPleiH-SFDIVAIJRrwZu68-YZgkdNrnF1jFyP6yC0JH6MTEGl1N0Cg04v_VSaFaKjQPFP-vreuVGt80lS7UP-WzjA1ps7LZ1_dbuOKNAMpuqJJtIE4PwSQeoXOW_s5vvki0MzIirt6-8mw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 466K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 23:07:58</div>
<hr>

<div class="tg-post" id="msg-24075">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نیویورک‌پست :
ارتش آمریکا در حال استفاده از
سامانه‌های لیزری
برای مقابله با برخی پهپادها و موشک‌های کروز و همچنین اهداف زیرساختی ایران در منطقه هرمز است. طبق گزارش این رسانه، هزینه شلیک لیزر به‌مراتب کمتر از استفاده از موشک‌های رهگیر عنوان شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/withyashar/24075" target="_blank">📅 23:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24074">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سازمان هواپیمایی کشوری امارات اعلام کرده پروازهای شرکت‌های هواپیمایی ایرانی
از امروز ۲۴ سپتامبر تا اطلاع ثانوی
به مقصد و از مبدأ امارات تعلیق شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/withyashar/24074" target="_blank">📅 23:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24073">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رویترز ـ مذاکرات آمریکا و ایران وارد مرحله جدید شده:
منابع نزدیک به مذاکرات می‌گویند تهران و واشنگتن در نیویورک درباره یک
توافق مرحله‌ای
برای پایان جنگ مذاکره کرده‌اند؛ طرح مورد بحث شامل بازگشایی تدریجی تنگه هرمز در برابر کاهش یا پایان محاصره اقتصادی آمریکا و احتمال آزادسازی بخشی از دارایی‌های ایران است.
@WarRoom</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/withyashar/24073" target="_blank">📅 23:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24071">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مسئولان جمهوری اسلامی بعد از ترک سالون، عکس قاسم کتلت را روی میزشان قرار دادند. @WarRoom</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/withyashar/24071" target="_blank">📅 22:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24070">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDxSEXfndNMZN6RXUkM5OjDR1JY8KipfCqsNNth9eFG1Ghp8ujP0AMRsAaHUO6rqdqW_acQskO-k6ODR22g_D5I3cbpYnoW5rq08rLAUHy1VDE3717SfVP4QSJBjioasHJmpF4yIncSoTrPqw0c_d0DmAK-n-Q--uFa4glLNyoVrOsGt46KamYMpYL43mfhQcjVxcnWpYMuiWFGtoPSwO9dPhXVGU1yeugBTsBStsUlR7xL2JiqFRUv7yS_SkQsFb7gXrFzSORCMMqVOLQPp9214GKV258iJT9PFZov6MFshL6FJeBMwtHfj6EMXJedSNI_bKxf31Mb2MJgC_SG6DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسئولان جمهوری اسلامی بعد از ترک سالون، عکس قاسم کتلت را روی میزشان قرار دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/withyashar/24070" target="_blank">📅 22:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24069">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/withyashar/24069" target="_blank">📅 22:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24068">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/24068" target="_blank">📅 22:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24067">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/24067" target="_blank">📅 22:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24066">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/withyashar/24066" target="_blank">📅 22:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24065">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نتانیاهو:
در طول قرن‌ها، حکومت‌های مستبدی که تلاش کردند ما را نابود کنند، بارها و بارها شکست خورده‌اند و به خواست خدا، همچنان شکست خواهند خورد. اگر شجاعت خود را جمع کنیم و عزم خود را جزم کنیم، به پیروزی ادامه خواهیم داد.
همان‌طور که در کتاب مقدس آمده است: «נצח ישראל לא ישקר»؛ یعنی «جاودانگی اسرائیل هرگز لغزش نخواهد کرد.» و دلیلش ساده است:
ما انتخاب دیگری نداریم.
از همه شما متشکرم.
חג שמח לעם ישראל
؛ عید بر مردم اسرائیل مبارک. متشکرم.خداحافظ
@WarRoom</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/24065" target="_blank">📅 22:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24064">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e66c6dc10.mp4?token=QrtvgTF0fPloNzOEidvYS3kGaoFR5A0Sp19qxdn90GIwxMiNTT9uPVSZBJtz-ACFMq6f-zTnToahA_S5t9mjrxOI0e3IDdVOju7TfsmigWyIqoiSgIzXFSmqXZd8ideqFuCTamjSNnPa6lrYLyD9IWemEZGELfz3arDsMApFp0TqLopnExw1KUPzmLIueAReOQHP3qI6lDpEgD-othUvh5RMCN7Qoxi9fJo_3CoG5r7HvM-rGmP67guldSwz5RUuSMm2od0zspxwDOQNG8_443QyYcFzYXLp8WFuXGlWbBTrzDaBGOvP-Te_6Q8FbO21XVzzMLV99TAqQPbJRFh0kL5BcwUTF8mQiwXdtsnjDwCittATSwm9QiOviDi2tY8jQYFTiiQh44x9APjLITYIZ-qfFtKrF1id1LZ_FcrEo_Gy-zfiXa-nVvXQ9SwJDU5h8gUAiZ_83B3y0-_W1bHu4T9c4XRD_r7WKS-FggrRNTcDYbsljbLb6rOneX7QJtbMlkBEj0c4NY4U_MF9Gf-RefyAz7OkeF5Y8J0UgDkDoKXCPjUprri0kwgHtWx2Md_boas_a3rgs9TxksYj_QD-DiWdrcSL-UwFjIMCYxIa7NyYgBx7BipH9iB1HzXeu-akWZz5PwyHs358znYsehaZoZnipMCaG2YxJwbxuPnNtAE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e66c6dc10.mp4?token=QrtvgTF0fPloNzOEidvYS3kGaoFR5A0Sp19qxdn90GIwxMiNTT9uPVSZBJtz-ACFMq6f-zTnToahA_S5t9mjrxOI0e3IDdVOju7TfsmigWyIqoiSgIzXFSmqXZd8ideqFuCTamjSNnPa6lrYLyD9IWemEZGELfz3arDsMApFp0TqLopnExw1KUPzmLIueAReOQHP3qI6lDpEgD-othUvh5RMCN7Qoxi9fJo_3CoG5r7HvM-rGmP67guldSwz5RUuSMm2od0zspxwDOQNG8_443QyYcFzYXLp8WFuXGlWbBTrzDaBGOvP-Te_6Q8FbO21XVzzMLV99TAqQPbJRFh0kL5BcwUTF8mQiwXdtsnjDwCittATSwm9QiOviDi2tY8jQYFTiiQh44x9APjLITYIZ-qfFtKrF1id1LZ_FcrEo_Gy-zfiXa-nVvXQ9SwJDU5h8gUAiZ_83B3y0-_W1bHu4T9c4XRD_r7WKS-FggrRNTcDYbsljbLb6rOneX7QJtbMlkBEj0c4NY4U_MF9Gf-RefyAz7OkeF5Y8J0UgDkDoKXCPjUprri0kwgHtWx2Md_boas_a3rgs9TxksYj_QD-DiWdrcSL-UwFjIMCYxIa7NyYgBx7BipH9iB1HzXeu-akWZz5PwyHs358znYsehaZoZnipMCaG2YxJwbxuPnNtAE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: شما درباره ایران هم سکوت کردید، اما من خبر خوبی دارم؛ با وجود این سکوت و آنچه من ریاکاری می‌دانم، روزی قدرت مردم ایران بر حاکمان آن غلبه خواهد کرد. ممکن است این روز چندان دور نباشد. مردم ایران روزی آزاد خواهند شد و رژیم حاکم، که من آن را سرکوبگر و جنایتکار می‌دانم، به‌دلیل دروغ، فساد و ظلم خود سقوط خواهد کرد و همه ما آن روز را جشن خواهیم گرفت
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/24064" target="_blank">📅 22:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24063">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نتانیاهو: به هیئت ایرانی توصیه می‌کنم این پیام را بشنوند تا اگر روزی از کشورشان خارج شدند، بتوانند آزادانه داستان خود را در شبکه‌های اجتماعی بازگو کنند. خطاب به معترضان حقوق بشر در خارج از اینجا می‌پرسم: وقتی حکومت ایران ده‌ها هزار غیرنظامی ایرانی را شکنجه و مجروح کرد و هزاران نفر از مردم خود را کشت، کجا بودید؟ آیا تجمع گسترده، اعتصاب غذا یا اعتراضی مقابل نمایندگی ایران در سازمان ملل برگزار کردید؟ درباره مسیحیان تحت آزار در ایران و خاورمیانه چطور؟ هیچ‌کدام
@WarRoom</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/24063" target="_blank">📅 22:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24062">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نتانیاهو قول بر اندازی رژیم و جشن همگانی را داد
@WarRoom</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/24062" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24061">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac08257aa.mp4?token=IzhOEb9dU3ttJVaSOLfXI0mK62RDz5llI8waQk1sjIrgwisD-OLVbvm8_RIlJHxnjuDR0fPKtoXN5ixyaUhXa8DGfB8Dqm8RwZcvXJGYTJ7QNpuGQdB1B78Y8OLMYEOmMu-jGtIdA696fEi2Dy8NxmyL_crgTr1kSttByUT5hAMH0wqRqpaaLtz0Yb9Mlpv8bPCf7aBBVDjnJ9DoZ8mUio_oTg9Ge6udXbcAp51-x2HXOixj9IzWJ88u4zXQS3gkyl-R0beGo6VZ2GkJ4lTxKoQQiYyTulqCjd-AUUj2U4ftmLf9YW9pbmsXT4WzrocjNJNDXQ4FUiLAJVeApuujZV22vNjLIkPJ23dlT8CSc3SIENFfw4DF7M90rhmB_i0uZn6zBarCUKBJbY8B6TgqfN2AQgwPad96m9Whr1OHcV_nwJmWInsxmo-Z9NaMDePo59TI32SFKAXJ23Fg8MnkbmVqbkBuuCpRXfpW_xtwotiCxvRDXKSLwc7ieNMLPVeXiZc6gmf8ZmcNqMsvXV81c-ZDqfWcCue3M45pSNOjQBbdigH3rgWFT0DmyQyEB51hwp8Lja--pFbNwomEagh6GiVnO5ArCNAL3xX9f_ajiz2yvcu_zZzzHJ9-WeqHfulXrix0DDMbLNjfTHornAbBRclecf-dZ303lwumuWtRvm0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac08257aa.mp4?token=IzhOEb9dU3ttJVaSOLfXI0mK62RDz5llI8waQk1sjIrgwisD-OLVbvm8_RIlJHxnjuDR0fPKtoXN5ixyaUhXa8DGfB8Dqm8RwZcvXJGYTJ7QNpuGQdB1B78Y8OLMYEOmMu-jGtIdA696fEi2Dy8NxmyL_crgTr1kSttByUT5hAMH0wqRqpaaLtz0Yb9Mlpv8bPCf7aBBVDjnJ9DoZ8mUio_oTg9Ge6udXbcAp51-x2HXOixj9IzWJ88u4zXQS3gkyl-R0beGo6VZ2GkJ4lTxKoQQiYyTulqCjd-AUUj2U4ftmLf9YW9pbmsXT4WzrocjNJNDXQ4FUiLAJVeApuujZV22vNjLIkPJ23dlT8CSc3SIENFfw4DF7M90rhmB_i0uZn6zBarCUKBJbY8B6TgqfN2AQgwPad96m9Whr1OHcV_nwJmWInsxmo-Z9NaMDePo59TI32SFKAXJ23Fg8MnkbmVqbkBuuCpRXfpW_xtwotiCxvRDXKSLwc7ieNMLPVeXiZc6gmf8ZmcNqMsvXV81c-ZDqfWcCue3M45pSNOjQBbdigH3rgWFT0DmyQyEB51hwp8Lja--pFbNwomEagh6GiVnO5ArCNAL3xX9f_ajiz2yvcu_zZzzHJ9-WeqHfulXrix0DDMbLNjfTHornAbBRclecf-dZ303lwumuWtRvm0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو:
این یک وسیله ارتباطی است؛
استارلینک
. ابزاری که به مردم اجازه می‌دهد به حقیقت دسترسی پیدا کنند، انتخاب داشته باشند و از آزادی اندیشه و آزادی بیان برخوردار شوند. به همین دلیل است که رژیم ایران از دسترسی مردمش به چنین فناوری‌هایی می‌ترسد
@WarRoom</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/withyashar/24061" target="_blank">📅 22:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24060">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نتانیاهو:
می‌دانید چه کسی می‌ترسد؟
مستبدان تهران.
و بیش از همه از چه چیزی می‌ترسند؟
از مردم خودشان؛ مردم شجاع ایران که برای مدت طولانی فداکاری کرده‌اند.
رژیم ایران به‌ویژه زمانی می‌ترسد که مردم ایران به ابزارهایی برای دسترسی آزاد به اطلاعات دسترسی داشته باشند
@WarRoom</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/withyashar/24060" target="_blank">📅 22:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24059">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نتانیاهو:
ما در اسرائیل منتظر نمی‌مانیم تا دیگران از خواب اخلاقی خود بیدار شوند. ما به پیش می‌رویم و در حوزه‌هایی مانند پزشکی، کشاورزی و هوش مصنوعی پیشرفت می‌کنیم و این نوآوری‌ها را در اختیار بشریت قرار می‌دهیم. اسرائیل هرگز قدرتمندتر از امروز نبوده و ما نمی‌ترسیم
@WarRoom</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/24059" target="_blank">📅 22:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24058">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نتانیاهו: جهان باید بداند که حماس از غیرنظامیان فلسطینی به‌عنوان سپر انسانی استفاده می‌کند و از بیمارستان‌ها، مدارس و مساجد به‌عنوان مراکز فرماندهی بهره می‌گیرد. اسرائیل برای دور کردن غیرنظامیان از مناطق درگیری، میلیون‌ها پیام هشدار، تماس تلفنی و اعلامیه ارسال کرده است. اتهام نسل‌کشی علیه اسرائیل، به گفته من، «بزرگ‌ترین دروغ قرن» است؛ زیرا اسرائیل هم‌زمان با جنگ، یک میلیون واکسن فلج اطفال و دو میلیون تُن غذا برای مردم غزه فراهم کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/24058" target="_blank">📅 22:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24057">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نتانیاهو: برخی کشورها میلیاردها دلار برای انتشار آنچه ما دروغ علیه اسرائیل می‌دانیم هزینه کرده‌اند.
قطر و ترکیه
از جمله کشورهایی هستند که به انتشار این روایت‌ها متهم‌شان می‌کنم. قطر سال‌ها از دانشگاه‌ها و رسانه‌هایی مانند الجزیره حمایت مالی کرده و ترکیه نیز تحت رهبری اردوغان بارها علیه اسرائیل موضع گرفته است. اردوغان خواستار نابودی اسرائیل شده و گفته است که می‌خواهد حاکم اورشلیم شود؛ اما این کشور و این شهر، پایتخت ابدی ماست
@WarRoom</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/24057" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24056">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نتانیاهو: مردم اسرائیل در برابر هزار موشک بالستیک سنگین ایران که بر سر شهرها و غیرنظامیان ما فرود آمد، ایستادگی کردند. شما در سالن مجمع عمومی سازمان ملل نشسته‌اید؛ اگر تنها یک موشک بالستیک یک‌تنی به اینجا اصابت کند، می‌تواند کل این مجموعه را ویران کند و دو موشک از این نوع می‌تواند سازمان ملل را نابود کند. حال تصور کنید هزار موشک عظیم از آسمان بر سر شهرها و خانه‌های شما فرود بیاید. من به شجاعت مردم اسرائیل و سربازانمان، از یهودی و مسیحی تا دروزی و مسلمان، ادای احترام می‌کنم
@WarRoom</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/withyashar/24056" target="_blank">📅 22:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24055">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نتانیاهو: چرا پیروز می‌شویم؟ یوناتان نتانیاهو پاسخ را ساده بیان کرد: «ما انتخاب دیگری نداریم.» هدف ما در تمام این جنگ ثابت بوده است؛ پیروزی با اراده‌ای تزلزل‌ناپذیر و شجاعتی بی‌وقفه. این اسرائیل است؛ یک ملت با یک آینده مشترک، از چپ و راست، جوان و پیر، مذهبی و سکولار
@WarRoom</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/24055" target="_blank">📅 22:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24054">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نتانیاهو: در این نبرد با آنچه «بربرها» می‌نامیم، هیچ شریکی بزرگ‌تر از رئیس‌جمهور ترامپ نداشتیم. از او و رهبری جسورانه‌اش تشکر می‌کنم. او دهه‌ها پیش فهمید که اگر با رهبران افراطی ایران که شعار «مرگ بر آمریکا و مرگ بر اسرائیل» سر می‌دهند مقابله نشود، در نهایت به دنبال عملی کردن اهداف خود خواهند رفتاسرائیل و آمریکا در کنار یکدیگر برای حفاظت از خود و نجات تمدن اقدام کردند. خلبانان شجاع آمریکایی در کنار خلبانان اسرائیلی در مأموریت‌های مشترک بر فراز ایران فعالیت کردند. دو کشور همچنین برای بازگرداندن گروگان‌های باقی‌مانده همکاری کردند و همه آنها را به خانه بازگرداندیم
@WarRoom</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/24054" target="_blank">📅 22:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24053">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نتانیاهو: با وجود همه این رنج‌ها، تسلیم نمی‌شویم. «نریا» در آخرین نوشته خود پیش از حمله به او نوشته بود: «ما کشور دیگری نداریم؛ دفاع از آن یک افتخار است.» به نریا و همه قهرمانان اسرائیل قولی مقدس می‌دهم: فداکاری شما بیهوده نخواهد بود. ما به دفاع از کشورمان ادامه می‌دهیم و پیروز خواهیم شد، چون انتخاب دیگری نداریم
@WarRoom</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/24053" target="_blank">📅 22:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24052">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رسانه های عبری : نریا لیتر، پسر یحیئل لیتر، سفیر اسرائیل در آمریکا، در حمله با خودرو در ایست‌بازرسی مَکابیم در مسیر ۴۴۳ در کرانه باختری به‌شدت زخمی و به بیمارستان شعاری زِدِک در اورشلیم منتقل شد. راننده خودرو محمود محمد محمود سلیمان، ۲۹ ساله، ساکن روستای بیت‌عور…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/24052" target="_blank">📅 21:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24051">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نتانیاهو:
ای
امانوئل مکرون، همکارم، به این موضوع توجه کن: دو یا سه روز پیش، یک شهروند فرانسوی به نام ناتانیل شوکرون، پدر شش فرزند، هنگامی که همراه پسر ۱۶ ساله‌اش از یک چشمه بازدید می‌کرد، هدف گلوله قرار گرفت. یک تروریست حماس در یهودیه و سامریه از فاصله نزدیک به او شلیک کرد.
آخرین کلماتی که او بر زبان آورد این بود: «فرار کن، فرار کن پسرم، خودت را نجات بده.» این اتفاق سه روز پیش رخ داد
@WarRoom</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/withyashar/24051" target="_blank">📅 21:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24050">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نتانیاهو:
سران تروریست‌ها و بزرگ‌ترین عاملان کشتار جمعی در جهان، نه‌تنها اسرائیلی‌ها، بلکه آمریکایی‌ها، بریتانیایی‌ها و شهروندان ده‌ها کشور را به قتل رساندند؛ خامنه‌ای، ضیف، سنوار، هنیه، نصرالله و هزاران تروریست دیگر که در پی نابودی ما بودند، همگی از بین رفته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/24050" target="_blank">📅 21:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24049">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نتانیاهو:
می‌دانید چه اتفاقی برای بخش عمده زرادخانه عظیم حزب‌الله، شامل حدود ۱۵۰ هزار موشک بالستیک و راکت که همگی برای هدف قرار دادن غیرنظامیان ما آماده شده بودند، افتاد؟ همه آنها از بین رفته‌اند. رهبران حزب‌الله کشته شده‌اند و روحیه آنها درهم شکسته است
@WarRoom</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/24049" target="_blank">📅 21:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24048">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نتانیاهو:
ارتش، نیروی دریایی، نیروی هوایی و تأسیسات هسته‌ای ایران را هدف قرار دادیم. اسرائیل حماس را به‌شدت درهم کوبید و ما نیز حزب‌الله را به‌شدت درهم کوبیدیم. آن ضربه را به خاطر دارید؟ می‌توانم این را به شما بگویم: حزب‌الله قطعاً آن را به خاطر دارد
@WarRoom</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/withyashar/24048" target="_blank">📅 21:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24047">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نتانیاهو: دشمنان ما انتظار داشتند اسرائیل پس از ۷ اکتبر فروبپاشد، اما ما فرو نریختیم و جنگیدیم. طی سه سال گذشته، سربازان ما در یک جنگ هفت‌جبهه‌ای با حماس، حزب‌الله، حوثی‌ها، ایران، شبه‌نظامیان عراق و سوریه و گروه‌های مسلح فلسطینی در کرانه باختری جنگیده‌اند. همه آنها برای نابودی اسرائیل با یکدیگر همراه شدند، اما شکست خوردند
@WarRoom</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/withyashar/24047" target="_blank">📅 21:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24046">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نتانیاهو: به دنبال برادرم، یوناتان «یونی» نتانیاهو، رفتم که افسر ۲۱ ساله تیپ چتربازان بود و واحدش از قبل بسیج شده بود. وقتی او را پیدا کردم، از دیدنم شوکه شد. از او پرسیدم چه اتفاقی خواهد افتاد. مکث کرد و گفت: «ما پیروز خواهیم شد؛ انتخاب دیگری نداریم.» این…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/24046" target="_blank">📅 21:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24045">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نتانیاهو: به دنبال برادرم، یوناتان «یونی» نتانیاهو، رفتم که افسر ۲۱ ساله تیپ چتربازان بود و واحدش از قبل بسیج شده بود. وقتی او را پیدا کردم، از دیدنم شوکه شد. از او پرسیدم چه اتفاقی خواهد افتاد. مکث کرد و گفت: «ما پیروز خواهیم شد؛ انتخاب دیگری نداریم.» این جمله را هرگز فراموش نکردم
@WarRoom</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/withyashar/24045" target="_blank">📅 21:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24044">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نتانیاهو: اسرائیل کشوری بسیار کوچک است؛ مساحت آن حتی به یک‌سوم یک درصد از کل سرزمین‌های جهان عرب نمی‌رسد. با این حال، ما را به استعمار متهم می‌کنند؛ آن هم از سوی کشورهایی مانند بریتانیا و فرانسه که خود سابقه استعمار گسترده دارند. این هم یک دروغ دیگر است
@WarRoom</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/withyashar/24044" target="_blank">📅 21:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24043">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نتانیاهو: در بین کسانی که سالن را ترک کردند، کشورهای بودند که در خفا برای نابودی قدرت هسته‌ای ایران از ما تشکر کردند؛ و این نهایت تزویر و ریا است.
اگر هنوز بزدلانی هستند که اتاق را ترک نکرده‌اند، از آنها می‌خواهم همین حالا بروند.
@WarRoom</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/24043" target="_blank">📅 21:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24042">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نتانیاهو: تخریب تاسیسات هسته‌ای ایران بسیار سخت بود، اما برای من یکی از آسان‌ترین تصمیم‌هایی بود که گرفتم
من به آقای احمد الشرع سوریه ای می‌گویم که یهودیان از زمان موسی در بلندی‌های جولان بوده‌اند و اگر جرعت داری علیه جولان اقدام کن.
@WarRoom</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/24042" target="_blank">📅 21:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24041">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نتانیاهو:۱۴ سال پیش گفتم مانع این میشم که جمهوری اسلامی به سلاح هسته‌ای برسه و ما دقیقا این کار رو کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/24041" target="_blank">📅 21:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24040">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نتانیاهو : ما باید ببریم هیچ راه دیگه ای نداریم
حاضران : تشویق
@WarRoom</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/24040" target="_blank">📅 21:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24039">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اینستاگرام بی بی رفت لایو</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/24039" target="_blank">📅 21:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24038">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/765c13dc80.mp4?token=SEovDoa_PGpJLBAjGeDuW9hNSlFLnpqlIyJ8X-ZIsGb1LfqjedUf5pxuXP0w0q5S8Ht9QjFF2G-9nO1rhIjnCZzFeROgyxaWlmHwXdakF_MEpEq_gPn1exbNZKuDR6c_bwkHMv3W_LH1I2Uj2KLdOH_KIBQkX2EiXEZjFr_yJROpdKwRZD5ZsykEnr6930lbDTeX_a_MHgRFrXjjcs_sKOIcZ6oacNXPG9ppLV8NjaPuy9z8T1c38R6vHRTI7rs7dlgxzRYpAmxIUXQLXo3nNqSUMpiqkclccO1L-zmbA5ov_F5cBVyWvbUullSpFuLPud_s_al8OF4ZHw0dYV-H3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/765c13dc80.mp4?token=SEovDoa_PGpJLBAjGeDuW9hNSlFLnpqlIyJ8X-ZIsGb1LfqjedUf5pxuXP0w0q5S8Ht9QjFF2G-9nO1rhIjnCZzFeROgyxaWlmHwXdakF_MEpEq_gPn1exbNZKuDR6c_bwkHMv3W_LH1I2Uj2KLdOH_KIBQkX2EiXEZjFr_yJROpdKwRZD5ZsykEnr6930lbDTeX_a_MHgRFrXjjcs_sKOIcZ6oacNXPG9ppLV8NjaPuy9z8T1c38R6vHRTI7rs7dlgxzRYpAmxIUXQLXo3nNqSUMpiqkclccO1L-zmbA5ov_F5cBVyWvbUullSpFuLPud_s_al8OF4ZHw0dYV-H3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/24038" target="_blank">📅 21:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24037">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">شروع نکرده گفت ایران داره بمب میسازه</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/24037" target="_blank">📅 21:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24036">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یه عده سیاه پوست و محجبه سالن رو ترک کردن
@WarRoom</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/24036" target="_blank">📅 21:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24035">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نتانیاهو اومد پشت تریبون سازمان ملل
@WarRoom</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/24035" target="_blank">📅 21:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24034">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBx8Ao2Wm4homO7Z3Nc4sh0AYwuveEEEp_If-8OaEY-aKyMaDoOld9x93qERmZMv1kiPHP3nHYMKjlVJM6xfAjR2ZfgUwwWfCBDR6kciWj01bafEvsZg7ia3yvEUANRDHPiSElAWkbfzkSIlRNXwmZLP5XYwGyDyke6RcTGYaAGxsHskWe-gxhQu3w43xbGgJ5ky3omTv5DWuhANBmxihZCURZ55m28s5ZjZlh3PeT0ms7ve8S9W1FjDxDbVaOf7M5vlA3eTgTYj3eXwOopBXSd9S9qN9KCrlU19aj-l4CVgv7GHK4vrzBmW-4_3DBME4B_7qK_0bS8MPpjaaWz-cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، قرار است امروز پنجشنبه ۲۴ سپتامبر، در گفت‌وگویی با «برت بایر»، مجری شبکه فاکس‌نیوز، حضور پیدا کند. این برنامه ساعت ۶ عصر به وقت شرق آمریکا پخش می‌شود که با توجه به اختلاف زمانی، برابر با ۱:۳۰ بامداد جمعه ۳ مهر به وقت تهران…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/withyashar/24034" target="_blank">📅 21:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24033">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بنیاد FDD: ترکیه در حال افزایش فشار بر شبکه مالی و حمل‌ونقل مرتبط با ایران است.
نهاد ناظر بانکی ترکیه مجوز فعالیت شعبه استانبول بانک ملت ایران را لغو کرده است. این اقدام پس از تحریم بانک سرمایه‌گذاری گلدن گلوبال ترکیه و دو شرکت زیرمجموعه آن از سوی آمریکا به‌دلیل ارتباط با سپاه انجام شد و ترکیه نیز وجوه این بانک را نقد و آن را تحت کنترل دولت قرار داد. ترکیش ایرلاینز، AJet و پگاسوس نیز پروازهای ترکیه و ایران را تا مارس ۲۰۲۷ متوقف کرده‌اند و آنکارا در حال محدود کردن فعالیت ماهان‌ایر به‌دلیل ارتباط ادعایی با سپاه است. بانک ملت حدود ۳۴.۸ میلیارد دلار دارایی دارد و از سال ۱۹۸۲ در تسویه تجارت ایران و ترکیه نقش داشته؛ آمریکا از سال ۲۰۰۷ آن را تحریم کرده و در سال ۲۰۱۸ تحریم‌های مرتبط با تروریسم را نیز علیه آن اعمال کرد. این گزارش همچنین به پرونده هالک‌بانک اشاره می‌کند که آمریکا آن را به انجام ۱۳ تا ۲۰ میلیارد دلار تراکنش مرتبط با ایران بین سال‌های ۲۰۱۲ تا ۲۰۱۶ متهم کرده بود. در جمع‌بندی، این اقدامات نشانه تلاش آنکارا برای حفظ روابط با تهران، همزمان با کاهش خطر تحریم‌های ثانویه آمریکا، ارزیابی شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/withyashar/24033" target="_blank">📅 21:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24032">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نتانیاهو: پیش از سخنرانی در سازمان ملل، به دیدارهای سیاسی خود ادامه می‌دهم؛ از جمله با نخست‌وزیران یونان و اسلوونی. با یونان در حال گسترش همکاری‌های انرژی و بین‌المللی، از جمله نشست سران اسرائیل، یونان و قبرس هستیم. در اسلوونی نیز با افتتاح سفارت اسرائیل در لیوبلیانا، فصل جدیدی در روابط دو کشور ایجاد کرده‌ایم که به هماهنگی نزدیک‌تر سیاسی منجر خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/24032" target="_blank">📅 21:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24031">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وحیدی : از جنگ نمیترسیم
@WarRoom</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/24031" target="_blank">📅 20:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24029">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">۴۵ دقیقه تا سخنرانی ‌و سورپرایز نتانیاهو
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/24029" target="_blank">📅 20:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24028">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اسرائیل کاتس، وزیر دفاع اسرائیل، در مراسم ورود ششمین زیردریایی نیروی دریایی این کشور،
INS Drakon
، به پایگاه دریایی حیفا گفت ورود این زیردریایی «پیامی مهم برای همه کسانی است که اسرائیل را تهدید می‌کنند، در رأس آنها رژیم آیت‌الله‌های تهران».
@WarRoom</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/24028" target="_blank">📅 20:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24027">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گزارش‌های تأییدنشده
از شلیک
دو موشک/پهپاد
از
ارومیه، به سمت اربیل
عراق
@WarRoom</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/24027" target="_blank">📅 20:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24026">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3bc11b06.mp4?token=lpbwmhgXKyLmSC0yq8_LJ7QcPHkD0yrsIROj7hOebeyZ3vReUUUU17dHOWEAd9G5rtxeA9NxCd9Zbppc8O_FuzhSOJYg-fw9rZzpZqQEPYn8k5oJ9xFuGOdx6dPqEmJsz1GP_8wKH_EmL1jxQd8qHJjG9jvl0fDLlGVqrkaV6d8fBe925xMqLU4DEPhL4a_nxBTnJgP76PD1UcuLDjjons28yR3O-YFQvT8BQx2AMcfmkfQ5s18-In63IOFTU4Qqpy9XadUulH47SQWSRmTTmq1m5MQvwKS8OhU_mYAVQ4FFP9Ux9UZVTLY5o7dK-tXVSHPYlahoy3d1jLzfQ-dnCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3bc11b06.mp4?token=lpbwmhgXKyLmSC0yq8_LJ7QcPHkD0yrsIROj7hOebeyZ3vReUUUU17dHOWEAd9G5rtxeA9NxCd9Zbppc8O_FuzhSOJYg-fw9rZzpZqQEPYn8k5oJ9xFuGOdx6dPqEmJsz1GP_8wKH_EmL1jxQd8qHJjG9jvl0fDLlGVqrkaV6d8fBe925xMqLU4DEPhL4a_nxBTnJgP76PD1UcuLDjjons28yR3O-YFQvT8BQx2AMcfmkfQ5s18-In63IOFTU4Qqpy9XadUulH47SQWSRmTTmq1m5MQvwKS8OhU_mYAVQ4FFP9Ux9UZVTLY5o7dK-tXVSHPYlahoy3d1jLzfQ-dnCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون آتش سنگین و ستون دود عظیم در شهریار یوسف آباد صیرفی
@WarRoom</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/24026" target="_blank">📅 20:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24025">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خبرگزاری CBS: بر اساس گزارش‌های منتشرشده، ۸۰ کشور با صدور بیانیه‌ای مشترک در سازمان ملل بر ضرورت بازگشت کامل و بدون مانع تردد دریایی در منطقه تأکید کردند. همزمان، مذاکرات غیرمستقیم مذاکره‌کنندگان آمریکایی و ایرانی در نیویورک ادامه دارد و
بازگشایی تنگه هرمز و پایان جنگ
از محورهای مهم گفت‌وگوهاست. گزارش‌های قبلی رویترز نیز نشان می‌دهد که بازگشت کشتیرانی در هرمز و رفع محدودیت‌های اقتصادی علیه ایران از موضوعات اصلی مذاکرات بوده است
@WarRoom</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/24025" target="_blank">📅 20:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24024">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">داداش اعتصابات  من خودم مغازه دارم  و دور و بریام تا  لحظه یی که  خود مامور اداره برق نیاد داخل پاساژ بگه  فردا برقو قطع میکنیم. پرداختش نمیکنیم  ینی تقریبا هر ۵ماه یکبار پرداخت میکنیم ، اما  هم  هی فله یی میزارن روش هم اخرش وقتی مامور میاد مجبوریم پرداخت…</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/24024" target="_blank">📅 20:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24023">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMilad</strong></div>
<div class="tg-text">داداش اعتصابات
من خودم مغازه دارم
و دور و بریام تا  لحظه یی که  خود مامور اداره برق نیاد داخل پاساژ بگه  فردا برقو قطع میکنیم. پرداختش نمیکنیم
ینی تقریبا هر ۵ماه یکبار پرداخت میکنیم ،
اما  هم  هی فله یی میزارن روش هم اخرش وقتی مامور میاد مجبوریم پرداخت کنیم
چیکار کنیم</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/24023" target="_blank">📅 20:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24022">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مسعود پزشکیان و عراقچی در حاشیه مجمع عمومی سازمان ملل با نواف سلام، نخست‌وزیر لبنان در گداخانه دیدار کردند. @WarRoom</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/24022" target="_blank">📅 19:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24021">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMDAIBbuNI_Ns7JuSYomoTzbPrVM6Nr4lryNXtWr1vThFPkxcIw8RU8YOIjMwwhbGN1bPGHwVRD93t_K8ZmkZjNaCevdLPtgAQmtDX5KS4mSSm_BHG9pEB4_SuWMyo9WTKq5KqMvWpLI2aHw1rNBcmUa9tsHP1bJXzlZnvrqFEeYqdc_fRNUfC_PMBORHpdOt32MUMWb2dDKFo7TbLkO7cx1U3MLhLnOORSLwPPW9ma0wj4XBmp20qK8LV0GI8w95-kWX88BZmr7VQWCN50d0PPZM96g_UVz9KYQTpP6vJyrnJclCrF2kltzmGwk1fFtpEZyIpsugXrgyQ99fk6ohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان و عراقچی در حاشیه مجمع عمومی سازمان ملل با نواف سلام، نخست‌وزیر لبنان در گداخانه دیدار کردند. @WarRoom</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/24021" target="_blank">📅 19:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24020">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFlKeyxNixlwExvo9OCr_ca27XREDni7E1p6UPj3o_68pZOs-rmTTmHVY2wHTcyybFcSH6ETrOr1aZxuOVBgxPzTPPBwOPtpj2zlowYhQIeVuFqEGlY8K5tS_UnxABXQzgHFwlrsKZwpE6z9fmLeU04Tr7LFB26Vrxdbk4Otg7HQm5DcRLhG4tY20IoLwt6Mv_ZYXjJhcvDswssPVlp0AyI5b2kVTaIGvdXEwLw4F3w8d5n_jFsPVmYHFrTC03Tiw0faFbOhHGN1GpeMD-5I44RphqvekdV0R-wZo6cC9wIuF49gQ0GBRkDl6DXyvDX9c887rrkR4MLPX26eiL4L7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان
و عراقچی در حاشیه
مجمع عمومی سازمان ملل
با
نواف سلام، نخست‌وزیر لبنان
در گداخانه دیدار کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/24020" target="_blank">📅 19:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24019">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d37142d90.mp4?token=NrYZX7xovreMBnaJ6msT1dGKChlkl3W9W3SYJXigZo3mAqiP320lpk6QjI9WVgoJbXEmFfEagR6H34PnHPTcnJxqdsxJ_yIjsQ3n4uJhm-nTwiUug11U8U2JgRM9U9Z5PDJZO1PUGtLhDtXHh8uTosvBca-eLVgJ1wgwbzIAZRpMRlstdBL4E9ezOCYdZVQWDS-m0VK6SZ-SjkwYGXZuW03NByKSDhsmDU92j3Zj2y-MT3vnchyFW1i6WPLv3OdvUAhriigwflaZVlBJMU6-a3lNtJbTlDHT_WJUTZGZOuClnAQW-W9uwYOA3uIHGTe1XT8CMbJfrHoZlfsJgMN_bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d37142d90.mp4?token=NrYZX7xovreMBnaJ6msT1dGKChlkl3W9W3SYJXigZo3mAqiP320lpk6QjI9WVgoJbXEmFfEagR6H34PnHPTcnJxqdsxJ_yIjsQ3n4uJhm-nTwiUug11U8U2JgRM9U9Z5PDJZO1PUGtLhDtXHh8uTosvBca-eLVgJ1wgwbzIAZRpMRlstdBL4E9ezOCYdZVQWDS-m0VK6SZ-SjkwYGXZuW03NByKSDhsmDU92j3Zj2y-MT3vnchyFW1i6WPLv3OdvUAhriigwflaZVlBJMU6-a3lNtJbTlDHT_WJUTZGZOuClnAQW-W9uwYOA3uIHGTe1XT8CMbJfrHoZlfsJgMN_bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو وارد سازمان ملل متحد در نیویورک شد
@WarRoom</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/24019" target="_blank">📅 19:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24018">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/24018" target="_blank">📅 19:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24017">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نفت به کانال ۱۰۲$ وارد شد @WarRoom</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/24017" target="_blank">📅 19:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24016">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2b2b37f7.mp4?token=KxltwFJHO2L1QjbKxDSBkmk0gFwgBnwIEiNopUjbRj4RxSSkFNVsodSYzJuYymSdOHAusCMgWfeOdbp8xxjSDh00JfLpULdtru1ZgNoPtczeCrbX3ZByHz8O6JQq40nGpdA9EXi9kvW0V7nFfw2Hdj25qcXpH-aRfpeeY5ARARdJMTntnno9A9X15SWK7CIxBBOyfv9tUeOIVsDZRWV6HssKvRWnTp2Z7YEYzY1RiPnb62vLGTg70i4vfMymxcyKBpti_OI9UBFJ4SOEWN-_fLKzyCH8ZWzv-UBLkk6WQdMf1FXMTqiM9GivORi3s_ACspev96Bx25iaVrkLUYzcjqmW5kICWD6QuYzeQmlehusuffSe5AfOJW74dFClKJtHBVyblbVsTsBowSFQJwMyorT2lrvEO7SbRTU4o4255tFkbSyDvNVqJ789v3BVGR8VZ5HKtQde76QLmQXSgr4qaze4F7miylMrmQTHCH8wfutzzBN7jmTTp252KVNVJUY6p4dlGkDTKsr7ej6QxmSuuoBNp8R1g4WsYfaA3ANrj6vr3T_CKBlsjCIem5qOmD6pkKdaJROWHxliWRzQydulVbPwQRr-BU33xesu3TE6bUuxCy0Cc0esHia2Z8ZpmwxSKAsV3T0aubQKTzQFZaDKABPgNc0UJQIglA10ynAO48Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2b2b37f7.mp4?token=KxltwFJHO2L1QjbKxDSBkmk0gFwgBnwIEiNopUjbRj4RxSSkFNVsodSYzJuYymSdOHAusCMgWfeOdbp8xxjSDh00JfLpULdtru1ZgNoPtczeCrbX3ZByHz8O6JQq40nGpdA9EXi9kvW0V7nFfw2Hdj25qcXpH-aRfpeeY5ARARdJMTntnno9A9X15SWK7CIxBBOyfv9tUeOIVsDZRWV6HssKvRWnTp2Z7YEYzY1RiPnb62vLGTg70i4vfMymxcyKBpti_OI9UBFJ4SOEWN-_fLKzyCH8ZWzv-UBLkk6WQdMf1FXMTqiM9GivORi3s_ACspev96Bx25iaVrkLUYzcjqmW5kICWD6QuYzeQmlehusuffSe5AfOJW74dFClKJtHBVyblbVsTsBowSFQJwMyorT2lrvEO7SbRTU4o4255tFkbSyDvNVqJ789v3BVGR8VZ5HKtQde76QLmQXSgr4qaze4F7miylMrmQTHCH8wfutzzBN7jmTTp252KVNVJUY6p4dlGkDTKsr7ej6QxmSuuoBNp8R1g4WsYfaA3ANrj6vr3T_CKBlsjCIem5qOmD6pkKdaJROWHxliWRzQydulVbPwQRr-BU33xesu3TE6bUuxCy0Cc0esHia2Z8ZpmwxSKAsV3T0aubQKTzQFZaDKABPgNc0UJQIglA10ynAO48Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سی بی اس : در جریان مراسم استقبال رسمی از شی جین‌پینگ، رئیس‌جمهور چین، در کاخ سفید، یک فروند بمب‌افکن رادارگریز
B-2 Spirit
به همراه چهار فروند جنگنده
F-22 Raptor
بر فراز محل مراسم پرواز کردند. این پرواز بخشی از برنامه رسمی مراسم استقبال دولت آمریکا از رئیس‌جمهور چین بود
@WarRoom</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/24016" target="_blank">📅 19:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24015">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLBbXCj06ax1woUjvm7iWYSHFeyMtmjrzKIE1IEDYo-LuMtkXyadhN3wzy2O4NcUk5yu-r0ZXiuweI8EilKfI32T5L-pwCp4HVmDqjmnbXxcshM-obOwk4FBr9FSenLF7Dnv6_edOOehO10KNWw6cxHKCoewE92__U6h2zo3WMd84Z3XkQggun7MJ_cjP_6KWDnNy9oTh8S1b3xQFT0pfY1a8r9o1VZgaQCLsFCbDD4BvrQtArTKt-QDHuQGQCvRb-F6PBTPdKWCDIdN3RjkNrt4T1IKCXvDi6rY6TSL2H5n4go8MZjHGKIvF4RSX4oN_LgDAJy1I0qK7cgY2pxuwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت به کانال ۱۰۲$ وارد شد
@WarRoom</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/24015" target="_blank">📅 19:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24014">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pjea3-hJHyfQra6aTBdmx7341KTM-Uyhy3cXJRNe1JWpoX-jiQN4WEdV4nvpwicjybAL9b19bpcHclIJx7lK7m__ZiH6J1BSsEeadjdrxr4QbEAwYxbyIlycFxSrnaqo2n2JHeQxygZi-0wG-KhCu3pDM6aLwzdLFo7Ee4_4Bl7CI6uDkB-R3ai9ousaCyqxB4btozR06DfRD7z6zVH_YoTVqemdCv_-RgvvRB-Dywzirh-kU73JerHSWUqwgA8Idri-n6vf_nUGf4HLL8EDw4WqWqoBcJM2qipOs2Kn8o5AioLwpN4rJuMj1RHr0o3K4mwbjPsKW6GSn4yhDsPB-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، قرار است امروز پنجشنبه ۲۴ سپتامبر، در گفت‌وگویی با «برت بایر»، مجری شبکه فاکس‌نیوز، حضور پیدا کند. این برنامه ساعت ۶ عصر به وقت شرق آمریکا پخش می‌شود که با توجه به اختلاف زمانی، برابر با
۱:۳۰ بامداد جمعه ۳ مهر به وقت تهران
است. فاکس‌نیوز برنامه «Special Report with Bret Baier» را در همین ساعت پخش می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/24014" target="_blank">📅 19:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24013">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وال‌استریت ژورنال: نتانیاهو در سفر کوتاه خود به نیویورک به دنبال ترتیب‌دادن دیداری با دونالد ترامپ بود، اما این دیدار محقق نشد.
همزمان، هواپیمای نخست‌وزیر اسرائیل به جای فرود در فرودگاه‌های اصلی نیویورک، در فرودگاه «استوارت» در دره هادسون و حدود ۱۰۰ کیلومتری شمال منهتن به زمین نشست؛ اقدامی که گزارش‌ها آن را در ارتباط با ملاحظات امنیتی و لجستیکی سفر نتانیاهو عنوان کرده‌اند. منابع اسرائیلی همچنین از حضور غیرمعمول نیروهای سرویس مخفی آمریکا در تمهیدات امنیتی سفر او خبر داده‌اند. نتانیاهو پس از سخنرانی در مجمع عمومی سازمان ملل قرار است نیویورک را ترک کند و در این سفر نیز دیداری با ترامپ در برنامه رسمی او قرار نگرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/24013" target="_blank">📅 18:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24012">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، و ملانیا ترامپ در کنار شی جین‌پینگ، رئیس‌جمهور چین، و همسرش پنگ لیویوان، در مراسمی ویژه به تماشای اجرای گارد افتخار نیروی دریایی ایالات متحده نشستند. این یگان ۲۴ نفره که به «گارد افتخار بدون فرمان صوتی» شهرت دارد، مجموعه‌ای از حرکات نظامی و نمایش‌های دقیق با تفنگ را به‌صورت کاملاً هماهنگ و بدون دریافت هیچ‌گونه فرمان کلامی اجرا کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/24012" target="_blank">📅 18:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24010">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">شی جین‌پینگ، رئیس‌جمهور چین: بسیار خرسندم که به کشور زیبای شما، ایالات متحده آمریکا، سفر رسمی انجام می‌دهم. از شما، رئیس‌جمهور ترامپ و خانم ترامپ، بابت میزبانی گرمی که برای من و همسرم به عمل آورده‌اید، سپاسگزارم. به نمایندگی از بیش از ۱.۴ میلیارد نفر از مردم…</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/24010" target="_blank">📅 18:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24009">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9f270237e.mp4?token=eAVKEx9FXDL2uwiQl4iMnPTB3wbV5OE8hoQMq3YMQSi520GXZK300oFqw8BMPhPPJp70az9rmS7FqYY-P7ZCbfNZwrBD4-AKAzRAyIc-cwtF_L4ecqDHz9wbyKsv52XQSqG3A9vBgRR_R-4E_V08tkNPG-CeNPdo-MVtKIRDWy-rz0SnGKq8e0HMeK5oUHpnDJPFZ8CNPuAde3J2FbtBNpkrTS97EHPcu_GHH-lAArXK-B_HFDRl3VWl0ljNzi7TrV-qxTafoKbpozd0z6G6ChhWl66GwupWIPgjFHktiDAA8AbQpkATkkS4FsMqokbhzFvYKvSgKnocTLPbmpEVcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9f270237e.mp4?token=eAVKEx9FXDL2uwiQl4iMnPTB3wbV5OE8hoQMq3YMQSi520GXZK300oFqw8BMPhPPJp70az9rmS7FqYY-P7ZCbfNZwrBD4-AKAzRAyIc-cwtF_L4ecqDHz9wbyKsv52XQSqG3A9vBgRR_R-4E_V08tkNPG-CeNPdo-MVtKIRDWy-rz0SnGKq8e0HMeK5oUHpnDJPFZ8CNPuAde3J2FbtBNpkrTS97EHPcu_GHH-lAArXK-B_HFDRl3VWl0ljNzi7TrV-qxTafoKbpozd0z6G6ChhWl66GwupWIPgjFHktiDAA8AbQpkATkkS4FsMqokbhzFvYKvSgKnocTLPbmpEVcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شی جین‌پینگ، رئیس‌جمهور چین:
بسیار خرسندم که به کشور زیبای شما، ایالات متحده آمریکا، سفر رسمی انجام می‌دهم. از شما، رئیس‌جمهور ترامپ و خانم ترامپ، بابت میزبانی گرمی که برای من و همسرم به عمل آورده‌اید، سپاسگزارم. به نمایندگی از بیش از ۱.۴ میلیارد نفر از مردم چین، می‌خواهم با ابراز سلام صمیمانه به مردم آمریکا و تبریک صمیمانه به مناسبت ۲۵۰مین سالگرد استقلال ایالات متحده، آغاز کنم.
@WarRoom</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/24009" target="_blank">📅 18:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24008">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پرزیدنت ترامپ: رئیس‌جمهور شی اولین رهبر چینی در تاریخ است که دومین سفر رسمی دولتی خود را به آمریکا انجام می‌دهد. @WarRoom</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/24008" target="_blank">📅 18:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24007">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed7ca36547.mp4?token=OyKhV6XOmTQ8x7pzrdwzW16r04KF7r_MuJ2M3S5mF9lfcIFVEVQS1d9Kjq9zQdWKRQS2rTvZZovyEgSOsgP8d5_RVI-Yn5GlxarQmuHbuDMi-sCV-hieUYwYcmNKzNw3WtZ7Rm-rcidMPeJIqejglMH16hJb6ZiuCKteynVpobMgfYX4vBFSidQUdeWMGYmVy6uuI0pST7KglSPeds0KwUUezYsVoE5Owr2AEpoxp5ME00by1-fzyFWUM9VvHVCyga8dIN_L8Ez6GQ_3GvhCxD5H2L8W7Gj_g-C7ZHwabiJWbgJMnVlJV-LZn-Qg5043E42f1vQQ9oCWofA5XjaBlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed7ca36547.mp4?token=OyKhV6XOmTQ8x7pzrdwzW16r04KF7r_MuJ2M3S5mF9lfcIFVEVQS1d9Kjq9zQdWKRQS2rTvZZovyEgSOsgP8d5_RVI-Yn5GlxarQmuHbuDMi-sCV-hieUYwYcmNKzNw3WtZ7Rm-rcidMPeJIqejglMH16hJb6ZiuCKteynVpobMgfYX4vBFSidQUdeWMGYmVy6uuI0pST7KglSPeds0KwUUezYsVoE5Owr2AEpoxp5ME00by1-fzyFWUM9VvHVCyga8dIN_L8Ez6GQ_3GvhCxD5H2L8W7Gj_g-C7ZHwabiJWbgJMnVlJV-LZn-Qg5043E42f1vQQ9oCWofA5XjaBlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
رئیس‌جمهور شی اولین رهبر چینی در تاریخ است که دومین سفر رسمی دولتی خود را به آمریکا انجام می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/24007" target="_blank">📅 18:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24006">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">شاهزاده باید هرچه زودتر یه فراخوان اقتصادی بده ، حتی اگه اعتصابات هم نبود ، باید فراخوان پرداخت نکردن قبض‌ها و هرگونه تراکنش مالی با رژیم رو اعلام کنه که همه همزمان انجام بدن !!!! خانوم فلانی آقای بیساری که اینجایی برسون به ایشون !
@WarRoom</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/24006" target="_blank">📅 18:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24005">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نتانیاهو برای سخنرانی امشبش در سازمان ملل وارد آمریکا شد @WarRoom</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/24005" target="_blank">📅 17:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24004">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نتانیاهو برای سخنرانی امشبش در سازمان ملل وارد آمریکا شد
@WarRoom</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/24004" target="_blank">📅 17:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24003">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwVZcSYs2Iz-NfMKXdASWiW-x2_MaWmEwjRqX5HJl-rbf0cBOh4EV2xR1nOZ3HU25AC9AM0UBpGpT-uiuaT6ZEFJgi8weud3uCNfn7YxCzfjy4J4QBZrim2xIhEyYf2ShEX64bDUp_RNRFNEyKNIhIbYgNJwcMehYQ-aVWvXn3g0OioHZlvY_O_ZtQk5NcQfHa89QnOCWNKllRl10R9Tt284kYgPlP8UmR-bEvv_ICch7Fc7HWcNf7ynJ5S3M_LvIMm9iKScxBBNeErm9-uRD7mKkLHPW_KvLk5OcdO99MCT43htkLbjNz4SxaGEjqHJCtBAXNxIMBL8YImzTMIsGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پل سنگین ترابری نظامی آمریکا در این لحظه. همچنین چهار سوخترسان هم اکنون بر روی تنگه هرمز مشغول انجام عملیات هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/withyashar/24003" target="_blank">📅 17:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24002">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تنگه صدای فرمانده پیشین هوا فضا سپاه میاد
@WarRoom</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/24002" target="_blank">📅 17:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24001">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سی‌ان‌ان: در نشست ترامپ با سران کشورهای عربی در نیویورک، قطر و عراق با هرگونه اقدام نظامی بیشتر علیه ایران مخالفت کردند.
به گزارش CNN، رهبران کشورهای عربی و خلیج فارس تلاش کردند ترامپ را از تشدید بیشتر جنگ با ایران منصرف کنند؛ آنها نگران گسترش جنگ و کشیده‌شدن بیشتر کشورهای منطقه به درگیری هستند
@WarRoom</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/24001" target="_blank">📅 17:18 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24000">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خبرگزاری فرانسه:
یحیی رحیم‌صفوی، مشاور رهبر جمهوری اسلامی، هشدار داد اگر آمریکا حملات خود را از سر بگیرد، ایران ممکن است دامنه جنگ را از خلیج فارس و دریای سرخ به اقیانوس هند و حتی فراتر از آن گسترش دهد. این نخستین‌بار است که یک مقام ارشد ایرانی به‌طور صریح از احتمال کشیده‌شدن درگیری به اقیانوس هند سخن می‌گوید.
@WarRoom</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/24000" target="_blank">📅 17:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23999">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بلومبرگ: ترامپ و شی آتش‌بس تجاری آمریکا و چین را تا ۱۰ ژانویه ۲۰۲۷ تمدید کردند.
این توافق که قرار بود ۱۰ نوامبر منقضی شود، دو ماه دیگر ادامه خواهد داشت و از تشدید دوباره تنش‌های تجاری میان دو اقتصاد بزرگ جهان جلوگیری می‌کند؛ هرچند اختلافات بر سر عناصر کمیاب، محدودیت‌های فناوری و تایوان همچنان پابرجاست.
@WatRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23999" target="_blank">📅 14:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23998">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نیروهای دولتی یمن: سرنگون کردن یک پهپاد متعلق به حوثی‌ها در آسمان منطقه "جبل حبشی" در استان تعز.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23998" target="_blank">📅 14:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23997">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یک منبع اسرائیلی: ایران فعالیت‌های خود برای انتقال و تقویت تأسیسات هسته‌ای در منطقه کوه کلنگ، در نزدیکی نطنز، را افزایش داده است. این منبع مدعی شده در صورت عبور تهران از «خطوط قرمز» تعیین‌شده، اسرائیل بار دیگر برای حمله به تأسیسات هسته‌ای ایران اقدام خواهد…</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23997" target="_blank">📅 14:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23996">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سخنگوی ائتلاف: ۶ موشک بالستیک که توسط شبه‌نظامیان حوثی تروریست شلیک شده بود، منهدم شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23996" target="_blank">📅 14:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23995">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سخنگوی دولت بریتانیا به شبکه الجزیره: ما با فرانسه و کشورهای دیگر همکاری می‌کنیم تا طرحی را برای پاکسازی مین‌ها از تنگه هرمز تدوین کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23995" target="_blank">📅 14:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23994">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap8SEE8UC3GN-Zkc6m3Fv2g2aW9rNgdekDHP72csHLZENzI7FNNMlS_Oj9Oc-i0IpqYCljPq3ALWicTuw36URcuR2vVqPcarX2v9NvMC9vMmkt2yh5HFnSy2zBX3PoDz2jPXl4_0K8kaK3s2xKKM2iWeusqhJD1S79tT7-D4w2h4Li2YqSAjDDVU42QfCanwcSfnwIHXWHfDTJIXwjUvvw5vDRDIih1QyoHogcXc7sjXikzTJUe7JVVOs-O_cGpTSn8lBdcCn7QH62ONWRR1lEiOsfCM3wAO46hty8tiofAq1zdqlPPnuvuuFkS2X9KmWw0-B0M-5C2CpHukhoyzdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدان استاندارد کرج  خودرو ضد شورش زرهی تو جنگ مونده بود زیر آوار از زیر خاک کشیدن بیرون
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23994" target="_blank">📅 14:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23993">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eba653675.mp4?token=ZsBOdr1Y1SaOp_nIdSmmqpcAm0BNfgNIjPIAl6f1RDdBsBBFfX58ZZ4j1928ODTh7N9ExVwHt4Lqe9OdPW-MCoApKnvi9w-wN4lb9Quu0X90dEn6L_b5zecNEF2b9-mjO-HLDDeveeHuWmFfElBTu282B8eHXbexzLBzXY_4vqgF12VGAeiv0puTdsc8Xf3Zmy7380m4qxizoHD771TsvsJzSr5_N-8l7Fy4hqwf65Quw793g417O_D3-PLvJheAWiwI28dNV_W-Ojd19w7kKnUkJ0UzysuqofzXVNZS8fqhIxt0P8a7VBS5ifxW-WRLUWBjI95vcxgfxSd7j75Nww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eba653675.mp4?token=ZsBOdr1Y1SaOp_nIdSmmqpcAm0BNfgNIjPIAl6f1RDdBsBBFfX58ZZ4j1928ODTh7N9ExVwHt4Lqe9OdPW-MCoApKnvi9w-wN4lb9Quu0X90dEn6L_b5zecNEF2b9-mjO-HLDDeveeHuWmFfElBTu282B8eHXbexzLBzXY_4vqgF12VGAeiv0puTdsc8Xf3Zmy7380m4qxizoHD771TsvsJzSr5_N-8l7Fy4hqwf65Quw793g417O_D3-PLvJheAWiwI28dNV_W-Ojd19w7kKnUkJ0UzysuqofzXVNZS8fqhIxt0P8a7VBS5ifxW-WRLUWBjI95vcxgfxSd7j75Nww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتوبان نیایش ، شرق به غرب، قبل از باکری ,ساعت یازده صبح پنجشنبه @WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23993" target="_blank">📅 13:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23992">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گزارش انفجار هایی در جده عربستان
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23992" target="_blank">📅 13:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23991">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0962eac3cf.mp4?token=sf5_7YWNTHUDsf2NHfuHxGt3dJ5_iRvxlOfIJpVlng5tNRVzMCKKrc57-TnQitLTPhvxuxrrbWtzwwmQe0277VIAPivlCjOGdF4VtPPg67vQqvWkkBNWB2dI4aCdrMMDOrZE-7ipqA87enC0iBhun73GloDeC5p7GfXZJSDReF3pI2yJLh6Wwk5vTtbmG0dXL_OY--O8g1KXj8dVzzXkN8XWcsto8fIP-3mcTjEPQjC0vgHVviw012iSvniL3BjKdicG9CrVqKf6HL5G6psq2MKRx-KT2cfczIfrpfhxGDXVdx4c7YT71esGXMtyp_Cig8GG4enO0WNUsAiWJo8owQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0962eac3cf.mp4?token=sf5_7YWNTHUDsf2NHfuHxGt3dJ5_iRvxlOfIJpVlng5tNRVzMCKKrc57-TnQitLTPhvxuxrrbWtzwwmQe0277VIAPivlCjOGdF4VtPPg67vQqvWkkBNWB2dI4aCdrMMDOrZE-7ipqA87enC0iBhun73GloDeC5p7GfXZJSDReF3pI2yJLh6Wwk5vTtbmG0dXL_OY--O8g1KXj8dVzzXkN8XWcsto8fIP-3mcTjEPQjC0vgHVviw012iSvniL3BjKdicG9CrVqKf6HL5G6psq2MKRx-KT2cfczIfrpfhxGDXVdx4c7YT71esGXMtyp_Cig8GG4enO0WNUsAiWJo8owQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتوبان نیایش ، شرق به غرب، قبل از باکری ,ساعت یازده صبح پنجشنبه
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23991" target="_blank">📅 13:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23990">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62fd497cbd.mp4?token=gODWYnXyww-kaeTt_JHtR4crx8_hruNBCMFb0u9GNrgsrU41_PoxeDingnNOFhWxllSh6lTVhJexCy_Sb1ejowbxy6CVIvv78fdEbm7g23ovyuRFfw68tr5Jp_cBTGh7FH4gx58LnI7B1sg_FQ8rq22-utweh21jloNlwUzLwkgT2qeX5BifJ1rSHawpqotoZqF_9KcPRKm2RSy64gDMy_xfHOFlloQ5OFucaVCspH53V_BErDOEAktyCctTUE0BSHHoYBcTtaCIo5rqR1nAYoOQvTL7ziHasLDXeZy0w-cO6oznPtX9Q6BgpnhDVWzfES3-jXnAG3QICxbJTCm2yxfLKsBuMYp88DCpIoFcw7gpJszz2o083fOr3pMgJ9mDNLWsc8cm9v4MHw3mEfnz6Z8u4zkbb7om2VEL2d597UcCMSMsqUqISlslKOqxbdKIcj3LQBFJoFgccSF5bURjoovjfv0p5dRDv7cTcu540bsz4RJ1qKpNu48OOeYZTequQ9dNBXP2pksjLFyWszEsa7Se-HK7YPJkXLOtStp-Ba45H-Roa-_gJZXcJH9eljM6lxp9moLcsdB_4MbmLKag5JDFSoxVG0wTRGhlN2bDQQUAKRKxh5fBGKpJ5guZzUPkD81Jf4SnUURawIPzBk3wo92eDDcw10BQqfhnOvktZsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62fd497cbd.mp4?token=gODWYnXyww-kaeTt_JHtR4crx8_hruNBCMFb0u9GNrgsrU41_PoxeDingnNOFhWxllSh6lTVhJexCy_Sb1ejowbxy6CVIvv78fdEbm7g23ovyuRFfw68tr5Jp_cBTGh7FH4gx58LnI7B1sg_FQ8rq22-utweh21jloNlwUzLwkgT2qeX5BifJ1rSHawpqotoZqF_9KcPRKm2RSy64gDMy_xfHOFlloQ5OFucaVCspH53V_BErDOEAktyCctTUE0BSHHoYBcTtaCIo5rqR1nAYoOQvTL7ziHasLDXeZy0w-cO6oznPtX9Q6BgpnhDVWzfES3-jXnAG3QICxbJTCm2yxfLKsBuMYp88DCpIoFcw7gpJszz2o083fOr3pMgJ9mDNLWsc8cm9v4MHw3mEfnz6Z8u4zkbb7om2VEL2d597UcCMSMsqUqISlslKOqxbdKIcj3LQBFJoFgccSF5bURjoovjfv0p5dRDv7cTcu540bsz4RJ1qKpNu48OOeYZTequQ9dNBXP2pksjLFyWszEsa7Se-HK7YPJkXLOtStp-Ba45H-Roa-_gJZXcJH9eljM6lxp9moLcsdB_4MbmLKag5JDFSoxVG0wTRGhlN2bDQQUAKRKxh5fBGKpJ5guZzUPkD81Jf4SnUURawIPzBk3wo92eDDcw10BQqfhnOvktZsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز هواپیمایی وارش از تهران به شهر دوشنبه پایتخت تاجیکستان از مرزِ هوایی لغو شد و به فرودگاه امام خمینی بازگشت
+ همچنین تمامی پرواز های ایران به دبی لغو شد
@warroom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23990" target="_blank">📅 13:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23989">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">این وضعت زندگی تو ایرانه من با پراید داغون اسنپ کار میکنم عراقی اینجا درس میخونه و بهترین زندگی میکنه این خیلی زور میاره ب ادم ک ما جوونا هیچ تصویر ذهنی از این ماشینا نداریم
😞
💔
(دانشگاه کاشان)</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/23989" target="_blank">📅 13:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23988">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromreza.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RohtNm0YjTQiDcSgC3qPzfWw3-i5Ex7zTWj90Jtr9bwdEGHI4VISsuki8-yUZB0s7CV5C87Z3gghFXE7vOyvh6Rw_Axv74umkwwSORWTpmY5foyR4niSM7_CJ2P9hRVAr9qemi5Mp37Kx-HkrYdantIqpwB0WO0aPEtHhnHSJYBohs1c1tkqyOgvi2RV_KBsM-iMzjZ8KWUmLSrKKOWuS65x0K-MODVSKLeCe1n-nluI6_1f5w8LC7yvWWV7-sX1JQ8EXVZC-9fwNaehnurHXf9BOdLLCLqVBHMr53eiuNyrRmhbY7ojkYV0iguiimTiQ6VA0kQWBLIvjC4qeSH_lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وضعت زندگی تو ایرانه من با پراید داغون اسنپ کار میکنم عراقی اینجا درس میخونه و بهترین زندگی میکنه این خیلی زور میاره ب ادم ک ما جوونا هیچ تصویر ذهنی از این ماشینا نداریم
😞
💔
(دانشگاه کاشان)</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23988" target="_blank">📅 13:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23987">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تلویزیون اسرائیل اعلام کرد که برنامه سفر نخست وزیر به نیویورک، شامل دیدار با ترامپ نیست و او بلافاصله پس از سخنرانی به کشور باز می‌گردد.
@WarRoom</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/23987" target="_blank">📅 13:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23986">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گزارش اختلال شدید جی‌پی‌اس در‌تهران
@WarRoom</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/23986" target="_blank">📅 13:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23985">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">روزنامه ال موندو: دستگاه اطلاعاتی آمریکا به چند دولت اروپایی هشدار داده که ممکن است روسیه در حال برنامه‌ریزی برای عملیات پهپادی علیه اسپانیا، فرانسه یا ایتالیا باشد
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23985" target="_blank">📅 13:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23984">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خبرگزاری‌های رژیم: تمامی پروازهای شرکت‌های هواپیمایی ایرانی به امارات متحده عربی، از نیمه شب گذشته، لغو و اطلاع رسانی شده و مربوط یه الان نیست
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23984" target="_blank">📅 13:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23983">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یک منبع اسرائیلی: ایران فعالیت‌های خود برای انتقال و تقویت تأسیسات هسته‌ای در منطقه کوه کلنگ، در نزدیکی نطنز، را افزایش داده است.
این منبع مدعی شده در صورت عبور تهران از «خطوط قرمز» تعیین‌شده، اسرائیل بار دیگر برای حمله به تأسیسات هسته‌ای ایران اقدام خواهد کرد. گزارش‌های پیشین نیز از ادامه فعالیت‌های عمرانی و تقویت ورودی‌های مجموعه زیرزمینی کوه کلنگ خبر داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23983" target="_blank">📅 13:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23982">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اسکات بسنت وزیرخزانه‌داری به فاکس‌نیوز:  ما اکسیژن رژیم را قطع کردیم ، انها ۵۰،۰۰۰ نفر را کشته اند ( بیش از ۴ دقیقه با زیرنویس) @WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23982" target="_blank">📅 13:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23981">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e053007122.mp4?token=TipFb490ayvW383raz968ckPCxr4jksOqVzEdPQ5tj5BWfsIt55nJHiWsptFA8Frv1SFlNZe4cYMNPH39vPFaJwfo8l8RV0ge0CBRpywktvQF1tUnWj9m0JOBLaRLrS9tXtKGvRxaFuVqp7a0-muu_ckMHzlEbn7Pd5Wl4z6LGAhcBu2lsMEk6qUx58BO7BRHSOuC7H-rI6gDJ1LPwlnyQtiBVnRPjDAPTzdqJZjiwYsspp1OjVAQhz6LjNoQHpEvuIz7MerpkX3yxCaz7A6PUMofnANGINz1-SJ6yK-sVu5p16R8ZFV2Xx27XCr9RIy8KL8F0c8lj903-TU8LMSSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e053007122.mp4?token=TipFb490ayvW383raz968ckPCxr4jksOqVzEdPQ5tj5BWfsIt55nJHiWsptFA8Frv1SFlNZe4cYMNPH39vPFaJwfo8l8RV0ge0CBRpywktvQF1tUnWj9m0JOBLaRLrS9tXtKGvRxaFuVqp7a0-muu_ckMHzlEbn7Pd5Wl4z6LGAhcBu2lsMEk6qUx58BO7BRHSOuC7H-rI6gDJ1LPwlnyQtiBVnRPjDAPTzdqJZjiwYsspp1OjVAQhz6LjNoQHpEvuIz7MerpkX3yxCaz7A6PUMofnANGINz1-SJ6yK-sVu5p16R8ZFV2Xx27XCr9RIy8KL8F0c8lj903-TU8LMSSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف رفت مدرسه بچه ها  ترسیدن
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23981" target="_blank">📅 12:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23980">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">استانداری خوزستان: صدای انفجار شنیده شده در آبادان، ناشی از نقص فنی در پالایشگاه این شهر است
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23980" target="_blank">📅 12:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23979">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نیویورک پست:
سه مرد بامداد چهارشنبه حدود ساعت ۴:۳۵ از یک دریچه فاضلاب در نزدیکی هتل محل اقامت بنیامین نتانیاهو در نیویورک خارج شدند و با دو خودرو از محل گریختند. پلیس نیویورک می‌گوید فعلاً نشانه‌ای از ارتباط این افراد با نتانیاهو یا تروریسم وجود ندارد، اما به‌دلیل حساسیت محل و برگزاری مجمع عمومی سازمان ملل، همراه با نیروهای فدرال تحقیقات و بررسی‌های امنیتی بیشتری انجام می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23979" target="_blank">📅 11:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23978">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">زلنسکی : اوکراین دو سرباز کره شمالی را که در روسیه اسیر شده بودند، به کره جنوبی فرستاده است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23978" target="_blank">📅 11:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23977">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqzgYQa40fhC8T0UlxdauZjWLuielcBBRxNppNlTxHhbrSLGYNAPT651PrT5ha5wSsWGVm9QiCDA2BJeYN4mHzs8t-wc7PlHwqtbnPLKnAJ3Zt26cwZmXcCZo1At2y9kChl1cnOngzHhmfVusidf1WdYYnGT2GXkixZ-MPOK58Ry1XW6lsRchmkFI7KbXqKPSvOh7pn11uQMSmUgczKwuSI2PC0GsoP3c3oVYA09B19_RvbiL_aXIdWpKwPGkCYk3XIDFdPRvLujiNINnxe3NsyOu4jAAACOgVXJDxcJMyOLy1z1qDAVuIqvyLsr0qsew2JTO7QbN1lTureR0oroEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل:
محمود عبدالفتاح عواد، فرمانده شاخه نظامی حماس در شهر غزه که به گفته ارتش اسرائیل در نگهداری
۷ گروگان اسرائیلی
از جمله دانیلا گلبوعا، کارینا آریِف، دورون اشتاین‌برخر، نعما لوی و زیو برمن نقش داشت، در حمله هوایی اسرائیل در آخر هفته کشته شد. ارتش اسرائیل همچنین مدعی شده او اخیراً در برنامه‌ریزی حملات علیه نیروهای اسرائیلی و بازسازی توانمندی‌های حماس نقش داشته است
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23977" target="_blank">📅 11:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23976">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دولت بریتانیا:
محدودیت‌های مالی علیه پنج بانک ایرانی فعال در بریتانیا، شامل
بانک سپه، بانک ملی، بانک صادرات، پرشیا اینترنشنال و بانک تجارت
را تشدید کرد. بر اساس دستور جدید خزانه‌داری بریتانیا، درخواست مجوز این بانک‌ها از این پس به‌طور پیش‌فرض رد می‌شود و تنها در موارد
الزام قانونی یا شرایط استثنایی و فوری
امکان صدور مجوز وجود دارد. همچنین مجوز عمومی فعلی این بانک‌ها پس از پایان اعتبار در
۲۲ اکتبر ۲۰۲۶
تمدید نخواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23976" target="_blank">📅 11:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23975">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd879fd06.mp4?token=vy7f3muvKaAeFQbXVAYKlCB4IYsaHQCXjer3DNcabIKmo1dcOwqiK3AFiWoT6K4nKEBIML8FZTRHSNbhbdzerds3ACjvffOLR9jZJqyO4DD8VuBZMXKtf4iZ0rWAKXr-X1t56deK6e1sEQpOlrSWihDJbdMpIyuT0vdvGlPKdYZZmlKmhHjjRvBgiD_xDUGsHKuIPsQnAnSPUHW4c1bqiaWqwmgw9P_IuY5f1raSv_KBlx86wLU02K8RIBHMcf8UZ36A8FlaLw1Ob06BG7ndi3-5LVSaZbmpJf4vI6hysoUtFPkncdoWB2xyq8wWXkfcG6jGvieqO2Q0JqMgOvzpnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd879fd06.mp4?token=vy7f3muvKaAeFQbXVAYKlCB4IYsaHQCXjer3DNcabIKmo1dcOwqiK3AFiWoT6K4nKEBIML8FZTRHSNbhbdzerds3ACjvffOLR9jZJqyO4DD8VuBZMXKtf4iZ0rWAKXr-X1t56deK6e1sEQpOlrSWihDJbdMpIyuT0vdvGlPKdYZZmlKmhHjjRvBgiD_xDUGsHKuIPsQnAnSPUHW4c1bqiaWqwmgw9P_IuY5f1raSv_KBlx86wLU02K8RIBHMcf8UZ36A8FlaLw1Ob06BG7ndi3-5LVSaZbmpJf4vI6hysoUtFPkncdoWB2xyq8wWXkfcG6jGvieqO2Q0JqMgOvzpnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوئی که
گفته می‌شود پیامدهای حمله ایران به یک نفتکش LNG
(
گاز طبیعی مایع
) را نشان می‌دهد؛ این کشتی بامداد چهارشنبه در حال عبور از
تنگه هرمز
بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23975" target="_blank">📅 11:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23974">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23974" target="_blank">📅 10:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-23973">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
ایران در مذاکرات غیرمستقیم با آمریکا در نیویورک، یک هفته به واشنگتن فرصت داد تا با شروط تهران برای بازگشایی تنگه هرمز موافقت کند؛ اما مذاکره‌کنندگان آمریکایی این درخواست را رد کرده و گفتند ایران کنترل تنگه هرمز را در اختیار ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23973" target="_blank">📅 10:52 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
