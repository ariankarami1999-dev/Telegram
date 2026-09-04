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
<img src="https://cdn4.telesco.pe/file/pGGFUxPvsnjDETcgdY9M_QgTzzwcPpgCZFDnYH1GM06Szm8wUgCdqwLHbN_dZRbRa_I_Dk2sfFkYYFLWsmeX76E4I0O_61SsahARHuVRNQwzmZFf9B_hxDStVFdSwRnmgdfUh48iSh1wJG2S0a7nFx01a-xEjfqXbavy23GXdoxFkUtBY2IEK-s3MuFlXBMeD1648AonkQY54krU0C9T-1Vy2bMZiH6dEMw0eTUdQjFnK1KRVa2F4vQqB2Th728hhO1jImNssffdaFtgJ9gOduNdjdFeciOpaFXHg4G8Hzi4HVOimKn5yOyCGj9yU31uTtuuc_JnZEWnVuCuMhyNvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.45M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 20:46:44</div>
<hr>

<div class="tg-post" id="msg-687229">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
رسانه عبری: هر عضو توافق مکه اهداف خاص خود را دنبال می‌کند
🔹
یک رسانه عبری اعلام کرد که هر یک از سه کشوری که توافق مکه را امضا کرده‌اند، اهداف خاص خود را دنبال می‌کنند.
🔹
مایکل میلشتاین تحلیلگر اسرائیلی در مقاله‌ای که امروز در روزنامه یدیعوت آحارانوت منتشر شد، به بررسی آخرین پیمان امضا شده در منطقه یعنی ائتلاف مکه پرداخت و از نبود همسویی در اهداف بین سه ضلع این پیمان سخن گفت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/akhbarefori/687229" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687228">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-text">⁨ ⁨ کسب‌وکارتون رو به فرصت‌های بیشتر وصل کنید!
✨
💫
با «شهرآسا» بانک شهر، فعالیت پذیرندگان می‌تونه مزایای بیشتری برای کسب‌وکارشون به همراه داشته باشه؛ از تسهیلات و جوایز ویژه گرفته تا امتیاز و قرعه‌کشی ماهانه.
💳
با اتصال پایانه فروشگاهی یا درگاه پرداخت اینترنتی به حساب بانک شهر، از مزایای ویژه شهرآسا بهره‌مند شوید:
🔸
تا ۷ برابر میانگین حساب دریافت تسهیلات تا سقف ۱۰۰ میلیارد ریال
🔸
جوایز نقدی و هدایای ویژه اصناف
🔸
تجهیزات جانبی ویژه
🔸
تقدیر از پذیرندگان برتر
🎯
به ازای هر ۱۰ میلیون ریال تراکنش در ماه، یک امتیاز کسب کنید و شانس خود را برای برنده‌شدن در قرعه‌کشی جوایز ارزشمند افزایش دهید.
یعنی اینجا، فعالیت بیشتر می‌تونه فرصت‌های بیشتری براتون بسازه.
🚀</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/687228" target="_blank">📅 20:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687227">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lknyHINnZt_qLJB2PnwpwkZipWH3QR0lqnjb9iprYWwGSC208I7rEaRpZ77I6vbBknNQku_Rv47SwzJOnqXcdDXW3GkumRP6Ezjaho5KhCbutoCCBi_xBSJja2voJqrD7K3s86-GymDiieGt4QpqF8ilVzZX5Po2vgJgRxMNL3PoHbYjBS0JvTHGPTRL-q8ZpQ68WCxbq8CkKRwN7lQ9fThhxkDm_o265VvDMc9fEVWCvBFeSgQZSAl12KJNgW39F3zepITviXdfVDGpPn59L60HDEBxCcM-9wTzeem_YeiF3-QIv7rkYOS3yOnSfAAiuiMvvOo122fpT6szLak4Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: کشورهای منطقه باید آینده خود را به دستان خود بسپارند
رئیس مجلس:
🔹
تأکید چین بر پرورش امنیت مشترک، اصلی را منعکس می‌کند که ایران مدت‌هاست از آن دفاع کرده است.
🔹
کشورهای منطقه باید آینده خود را به دستان خود بسپارند، و ثبات واقعی تنها از طریق معماری امنیتی جدید بومی می‌تواند به دست آید. ایران آماده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/akhbarefori/687227" target="_blank">📅 20:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687226">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda74c1306.mp4?token=B--ExsAxLMyCDuIdM5Pfte3xdhCTFQOsF5sHEEYBgSFrxLENxTOTTydD6QU4OUy3KNLK3WoY3zkBQvQRLgLzQLcxvsC7so1ZAPxAsKz7GZnwqwirOC5oe5eeaqLrIMdVjfyYtJEUPQBgQJ1BBPPEa_RXk9MXivrrRhG-LWl0mGxFBiDT74VDMQHs_6SFlt79G8JSsakpWPKkhyyv7BBtc1IvvJ3bgZ9pUDpLZy6ofX_VSgaoeyEAaqfeRk2a0LHag8HAPFZdM7Q8-Iqt_R7ysmI0sAwaQiogi6Cs0MpteObRFJ4oxSgKCNmSbMQMBJtnQohDx45RVX2OPGzalAJqOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda74c1306.mp4?token=B--ExsAxLMyCDuIdM5Pfte3xdhCTFQOsF5sHEEYBgSFrxLENxTOTTydD6QU4OUy3KNLK3WoY3zkBQvQRLgLzQLcxvsC7so1ZAPxAsKz7GZnwqwirOC5oe5eeaqLrIMdVjfyYtJEUPQBgQJ1BBPPEa_RXk9MXivrrRhG-LWl0mGxFBiDT74VDMQHs_6SFlt79G8JSsakpWPKkhyyv7BBtc1IvvJ3bgZ9pUDpLZy6ofX_VSgaoeyEAaqfeRk2a0LHag8HAPFZdM7Q8-Iqt_R7ysmI0sAwaQiogi6Cs0MpteObRFJ4oxSgKCNmSbMQMBJtnQohDx45RVX2OPGzalAJqOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: ماجرای قلب نشان دادن سخنگوی دولت به خبرنگاران چه بود؟
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/akhbarefori/687226" target="_blank">📅 20:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687225">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
موشک‌های ایران در آسمان اردن   جزئیات کامل
👇
khabarfoori.com/fa/tiny/news-3242721</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/687225" target="_blank">📅 20:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687224">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86f2c982f0.mp4?token=Uf7fTyeTM8MVjFqZLCRw2ZZSr0V3g4nJbQ5Rxc0WeGuSChjgBwOrlvl_S3EVijuiXqaYFyGcIQOtQAvJkpZub5IIrF1PtjWi-SNuTOCfacKv5Fn0drAOECl_qhmOKt1X9g8CB6C_YiFan3ZeqdMJ2Itw4P1PJqDU2xFytI1N5Q9ZD-Qzx95qjEAhuTx0rkJwF530S_pnAnVnDXVLInS5Mmy9a5OFWyT9AA6T8zLstdkG8fG2l_KybbD4P0tJHXTUxjzZYauUsEk9l5UVzdgPXmsW-BDdRwzp77q_rBKCMCUjA6VrRyd4IJ70exKhugB61DK6dayzBwrhsBdRR3qjlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86f2c982f0.mp4?token=Uf7fTyeTM8MVjFqZLCRw2ZZSr0V3g4nJbQ5Rxc0WeGuSChjgBwOrlvl_S3EVijuiXqaYFyGcIQOtQAvJkpZub5IIrF1PtjWi-SNuTOCfacKv5Fn0drAOECl_qhmOKt1X9g8CB6C_YiFan3ZeqdMJ2Itw4P1PJqDU2xFytI1N5Q9ZD-Qzx95qjEAhuTx0rkJwF530S_pnAnVnDXVLInS5Mmy9a5OFWyT9AA6T8zLstdkG8fG2l_KybbD4P0tJHXTUxjzZYauUsEk9l5UVzdgPXmsW-BDdRwzp77q_rBKCMCUjA6VrRyd4IJ70exKhugB61DK6dayzBwrhsBdRR3qjlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک‌های ایران در آسمان اردن
جزئیات کامل
👇
khabarfoori.com/fa/tiny/news-3242721</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/687224" target="_blank">📅 20:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687223">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">11 Ane Manaee (1403-09-16) Marghade Sheikh Sadoogh</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/687223" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه یازدهم
حجت‌الاسلام امینی‌خواه:
🔹
عمل در آیینه هستی؛ تأملی بر جایگاه و معنای آن
🔹
نورِ عمل؛ چراغی که راه‌های بسته را روشن می‌کند [4:20]
🔹
نورانیت نماز شب؛ گشایش قلب، تغییر اخلاق [4:58]
🔹
شرح صدر؛ گنجینه‌ای برای دل‌های نورانی [7:31]
🔹
علم به فایده؛ کلید رفع نیاز و رسیدن به کمال [15:31]
🔹
تشکیک وجود در اندیشه ملاصدرا؛ شعور و محبت، در تمام مراتب هستی [19:27]
🔹
تجربه‌ نزدیک به‌ مرگ؛ وقتی سنگ‌ها هم انس و تعلق دارند [22:03]
🔹
لذت‌های حیوانی؛ وقتی انسان مسیر کمال را گم می‌کند [24:48]
🔹
آنجا که اراده انسان، محض اراده خدا می‌شود [31:25]
🔹
کمال انسانی؛ جایی که هیچ قدرتی را یارای مقابله نیست [35:30]
🔹
حلال و حرام؛ نقشه‌ای برای رسیدن به کمال انسانی [42:11]
🔹
صبر؛ کلید طلایی رسیدن به کمال انسانی [46:59]
🔹
لذت حقیقی؛ در گرو بندگی و انجام وظیفه [50:50]
🔹
چادر فاطمه زهرا (سلام‌الله‌علیها)؛ نجات‌بخش خیل عظیم خلائق در عرصات قیامت [59:11]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/687223" target="_blank">📅 20:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687222">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
فروش تجمیعی شرکت‌های شستا به بیش از ۵۷۰ همت رسید/بیش از ۵۰ هزار نیروی انسانی شستا در دل جنگ پای کار ماندند
محمدرضا سعیدی، مدیرعامل شستا در
#گفتگو
با خبرفوری:
🔹
علیرغم آسیب‌های جنگ، شستا نه‌تنها تولید و پایداری خود را حفظ کرد، بلکه آن را ارتقا داد. تاب‌آوری کشور در دل جنگ با تلاش نیروی انسانی شستا تقویت شد
🔹
یاد و خاطره ۴ شهید والامقام شستا را گرامی می‌دارم و از تلاش همه مدیران و کارکنان این مجموعه بزرگ تقدیر می‌کنیم
گفتگوی کامل را اینجا ببینید و بخوانید
👇
khabarfoori.com/fa/tiny/news-3242509</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/687222" target="_blank">📅 20:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687221">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
خبرهایی درباره حمله به پایگاه‌های آمریکا در اردن
🔹
منابع خبری گزارش دادند پایگاه‌های آمریکا در اردن هدف حمله قرار گرفته است.
🔹
این منابع گفتند در پی این حملات، صدای چندین انفجار مهیب در مناطق مختلفی از اردن شنیده شده است.
🔹
منابع اردنی اما مدعی شدند این موشک‌ها…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/687221" target="_blank">📅 20:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687220">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
شنیده شدن انفجارهای قوی در اردن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/687220" target="_blank">📅 20:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687219">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
شی با هیأت بزرگ تجاری راهی آمریکا می‌شود
🔹
دو منبع آگاه اعلام کردند رئیس‌جمهور چین، قصد دارد در سفر آتی خود به واشنگتن، هیأتی بزرگ از مدیران و فعالان اقتصادی این کشور را همراه خود ببرد؛ اقدامی کم‌سابقه که در بحبوحه تنش‌های اقتصادی میان پکن و واشنگتن انجام می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/687219" target="_blank">📅 20:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687218">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
الجزیره به نقل از رسانه‌های رژیم صهیونیستی: ارتش اسرائیل به ساکنان شمال لبنان اطلاع داده است که قصد دارد حملاتی را در این کشور انجام دهد که منجر به انفجارهای مهیب خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/687218" target="_blank">📅 20:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687217">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
شنیده شدن صدای چندین انفجار در اردن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/687217" target="_blank">📅 20:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687216">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171f23100d.mp4?token=PqgBlhmUEZVWJ4Gf6rSxVQhKEJ5GKRWOYtN_42QV9VvNef1u2e4KUJHvQDxQZpbd6wYbGtlNN5TVOiHgT4Jy1yB26Y-PECtjfG673m-GSAMv4dMTLPtmcGjF0qqNIQ3DwS3r7QoyIdjsFDaQsDYYg6kGyu-EVc0d6gGhok660pZ-Y38wWtCMs2ZHJpuhSLFxxFoiWuG5MYFm3dIT0aO2nIVjMt20UhOx7xDYNJNOqs6t1xGRbRoxB9f2Vv3aTAWCBbR2KHs_cpqqp_JriVG4pXWuU9iOdl1b2lsnhnkDbabfTYX82BoyyzAQiTTNkHGWMnfZhXam6GaXciQ0AGtA9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171f23100d.mp4?token=PqgBlhmUEZVWJ4Gf6rSxVQhKEJ5GKRWOYtN_42QV9VvNef1u2e4KUJHvQDxQZpbd6wYbGtlNN5TVOiHgT4Jy1yB26Y-PECtjfG673m-GSAMv4dMTLPtmcGjF0qqNIQ3DwS3r7QoyIdjsFDaQsDYYg6kGyu-EVc0d6gGhok660pZ-Y38wWtCMs2ZHJpuhSLFxxFoiWuG5MYFm3dIT0aO2nIVjMt20UhOx7xDYNJNOqs6t1xGRbRoxB9f2Vv3aTAWCBbR2KHs_cpqqp_JriVG4pXWuU9iOdl1b2lsnhnkDbabfTYX82BoyyzAQiTTNkHGWMnfZhXam6GaXciQ0AGtA9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: ماجرای قلب نشان دادن سخنگوی دولت به خبرنگاران چه بود؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/687216" target="_blank">📅 20:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687215">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
شنیده شدن صدای چندین انفجار در اردن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/687215" target="_blank">📅 20:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687214">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
وقوع انفجارهای بزرگ در جنوب لبنان در ادامه جنایت تخریب منازل مردم
🔹
اشغالگران صهیونیست با منفجر کردن و تخریب چندین منزل دیگر در اطراف شهرک زوطر شرقی و المنصوری در جنوب لبنان به جنایات ضد بشری خود ادامه دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/687214" target="_blank">📅 20:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687213">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/338f0b7bb5.mp4?token=TZCnhVy45A24vKQFjl2MA8LGhE5iOsb_Slt9lxipbmJQ9tU14MoTdskNyljYKk4H4nkPgnd2dizpVqJTUcYF5KOa7FU40pbFHUxRHQ7BVTE9QDoLcUrRUu3rj_0Vo3sRVz20E140w5sBQZ2_avUkckEp1gVwjzG2KBLs-iPI4IV9crkU7vhvOPjekjTiZ7KM_ZqkouNNcCYrYBDdkyetIsl7epWpIVPu8RJ6-Q27cfxyqdNofPq2laxg0dFNlF9J2lNMsrdvGQA76khotHZq8elLSatBXxa8nNSpoFC-TAI_TiSc-gCo8DZmIczgonW7zXpuiZK8ctIR0Ebne4gi7CVL5UFGE7PKfLmlDm0Qrn6hZ47Z3hkvHMwoHnMT0sYO23ihLiebhD3QR_Tlv7u_JuHsqTVFsjsBhGSlwLu5HbiSi29kRgAchSz-38QGEdrdVLzfn0XjOVQg4pUWfBLprj5kP6Cl2ALrB-gKYWJWl_iRoy_48VS4qjfsoJCywRnV-pLYR8jaJWlL31lOh0CYqUf7__rg64Etg3AgML0S5XSQudZkbFoP773dlhPRPTfseflcTC25CvxLBOxFcv3OnA6I8Bw9rMheoPC-Ipo8Pz5uVXuSlVjj8iO0m08OMksR7j8s4x5Q6825LugtIM_6XoNFFUcz6eWRWalRKZko3SI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/338f0b7bb5.mp4?token=TZCnhVy45A24vKQFjl2MA8LGhE5iOsb_Slt9lxipbmJQ9tU14MoTdskNyljYKk4H4nkPgnd2dizpVqJTUcYF5KOa7FU40pbFHUxRHQ7BVTE9QDoLcUrRUu3rj_0Vo3sRVz20E140w5sBQZ2_avUkckEp1gVwjzG2KBLs-iPI4IV9crkU7vhvOPjekjTiZ7KM_ZqkouNNcCYrYBDdkyetIsl7epWpIVPu8RJ6-Q27cfxyqdNofPq2laxg0dFNlF9J2lNMsrdvGQA76khotHZq8elLSatBXxa8nNSpoFC-TAI_TiSc-gCo8DZmIczgonW7zXpuiZK8ctIR0Ebne4gi7CVL5UFGE7PKfLmlDm0Qrn6hZ47Z3hkvHMwoHnMT0sYO23ihLiebhD3QR_Tlv7u_JuHsqTVFsjsBhGSlwLu5HbiSi29kRgAchSz-38QGEdrdVLzfn0XjOVQg4pUWfBLprj5kP6Cl2ALrB-gKYWJWl_iRoy_48VS4qjfsoJCywRnV-pLYR8jaJWlL31lOh0CYqUf7__rg64Etg3AgML0S5XSQudZkbFoP773dlhPRPTfseflcTC25CvxLBOxFcv3OnA6I8Bw9rMheoPC-Ipo8Pz5uVXuSlVjj8iO0m08OMksR7j8s4x5Q6825LugtIM_6XoNFFUcz6eWRWalRKZko3SI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از معنای پردازش تدریجی هیجانی در روانشناسی
🔹
ذهن مثل همان شن‌هاست، وقتی آسیب می‌بیند، نیاز به زمان و تکرار دارد تا خودش را دوباره شکل بدهد به شرطی که در جریان بمونه و رهاش نکند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/687213" target="_blank">📅 20:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687212">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل پنجم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/687212" target="_blank">📅 19:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687211">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gl7jQ1p6hJ6hTjoqsHqWtYN_-TOqH8rSu5fOyRByXoH80uTEISHfNIJGbscmC358KJWCeFxqrdOpNbHlHKPu9mRrnA-tOr94KRHQKVb3uJYeXngzMO-kNhmjopysp9p2y4i1oe7qgc9FpwHLXMcmNQBSW7pA_q8TAVqQMhmzKR51PZNtIRRgJ4NC_kenQs4n9j_xV_wh9ooR-U_5gN7XxmE_idEdF7HO_IgQym_rJ_T5nPlC3b6NSZuaPYUwt18ZP-e64IJzvVbV6hbqEWguuzrRr0-tttqrdhNNw5WiAUt9SKMulQJfgrxF1GUutfeI2na9y-pKzSQ1e3Q8P9Hstg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشاوره رایگان پزشکی برای متقاضیان کاهش وزن با آمپول‌های لاغری
🔹
با توجه به سیر صعودی مصرف خودسرانه آمپول های لاغری و با همکاری شرکت های دانش بنیان دوراپزشکی ، این امکان فراهم شده تا افرادی که قصد استفاده از آمپول های لاغری را دارند به صورت کاملا رایگان و آنلاین توسط پزشک ویزیت شوند.
🔹
کاربران در این سامانه با تکمیل فرم کوتاه ارزیابی، شرایط خود را از نظر BMI، سوابق بیماری و داروهای مصرفی بررسی کرده و سپس با مشاوره رایگان توسط پزشک از شرایط مصرف آمپول های لاغری با خبر می شوند.
👈
شروع ارزیابی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/687211" target="_blank">📅 19:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687210">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtwoFlPt-38CLm89YosKzIjmbPgbmPcCDydi_P_lZPxa0OCLMJZjj8q2wT4nGbFN0dRplWY-0T72IjIaevuPe5w1ZU6sfwgHGreE6KntR3-_pql5f1CpGM9YHCqMS5zKAw0Y-o1zFPDAAgw7-Gj0hGWVlqipi51x0FEjcBxtRd8hBPA9dChfrQVbg2MFUsVd0OFgLXbu3A5La08lhosQYl5hUmO2rPu33rijWF6Aq-CFGH-VBRZydUPSPGooJRNNrPuoKtKJWl41BClPJMj3jU45ZVD5QkyOt-3AdO0zKNTFXkShrnAN-ZgsL2w1b6inNjm4FKN3egCaBm7wu4ubkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نگرانی ترامپ: دموکرات‌ها ترجیح می‌دهند در جنگ علیه ایران شکست بخوریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/687210" target="_blank">📅 19:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687209">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
وقوع انفجارهای بزرگ در جنوب لبنان در ادامه جنایت تخریب منازل مردم
🔹
اشغالگران صهیونیست با منفجر کردن و تخریب چندین منزل دیگر در اطراف شهرک زوطر شرقی و المنصوری در جنوب لبنان به جنایات ضد بشری خود ادامه دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/687209" target="_blank">📅 19:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687208">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
آتش‌سوزی دو کارگاه بافندگی در تهران
سخنگوی آتش‌نشانی تهران:
🔹
دود مشاهده شده در آسمان مرکز پایتخت مربوط به حریق دو کارگاه بافندگی در کوچه برلن است.
🔹
آتش‌نشانان در محل حضور دارند و در حال اطفای حریق هستند.
🔹
تاکنون مصدومی در این حادثه گزارش نشده است./فارس
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/687208" target="_blank">📅 19:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687207">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
رویترز: عراق تنها کشوری در منطقه خلیج فارس است که مجوز عبور نفتکش‌های عراقی از تنگه هرمز را از ایران دریافت کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/687207" target="_blank">📅 19:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687206">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQuFqrwqSf2Jv8ygFjPe3zV4Rx-Vxa63Q1ODScWJYFzPuF1vhCrFL3faK9QvlQwxZbq9VaVp7pG6KyhkxWTdKWVqCStaRec7iedY-7nKBGXz-3XNR0sfo0sqaoFt-ew3qfb9s08azRN2OfjaJ9bYsZ6u1CmBQINWMvDqxIKpusqB-zmh_l65aPW4E0qTAiO6QAQ63NywTlKmMLq0sRrE6TDZgx38wrwNfMjmHyK1M2nsMSSp1Aj1kJlHUvvJ_NEMMgWMzf4wQSaiV0bLY4sEXyvHDgH7zOZyxS5raHtu47FRZ7EM6AamnbdR23KFdC1baMiYnxzvIleIYFcBwUTubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل سازمان منطقه آزاد ارس در مراسم افتتاحیه ارمنستان اکسپو عنوان کرد؛
ضرورت ایجاد «معماری نوین اقتصادی» با همسایگان/ منطقه آزاد ارس، دروازه ورود سرمایه‌گذاران به ایران
متن کامل خبر را در لینک زیر بخوانید
https://t.me/araspres/24095</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/687206" target="_blank">📅 19:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687205">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02471fcc8b.mp4?token=vh-pZa6bWbxzdFFGf033DpAfIgbf58EhMmuTK5P3nwpHCczbKXZCObPTtT5QqG9gHtKXcPlGt2u1GFV2X78MC-A84OqrKDWWk8ZXy-zY7T0jcnGKGAx9cfBG2GxX0ilpHregdY4Vig5jnKFW2yt2hz_E-ViUBc1Z7k1z1McuxQa_KmCvneF81NyEJZpGxE1igFCSXzM1dRLVd8KfvCr-OvZXQhufrbJqMF_URHPlhOOnwirIkA65tEdWNaCK5X8xUbH64jwvKen9t-2s_zhXLAIIiB1ckghTNJ_v8C-TeDcTCKEeXfiVAVfq4WeAOq5kk1gSjCqMocTuORUpW3QGbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02471fcc8b.mp4?token=vh-pZa6bWbxzdFFGf033DpAfIgbf58EhMmuTK5P3nwpHCczbKXZCObPTtT5QqG9gHtKXcPlGt2u1GFV2X78MC-A84OqrKDWWk8ZXy-zY7T0jcnGKGAx9cfBG2GxX0ilpHregdY4Vig5jnKFW2yt2hz_E-ViUBc1Z7k1z1McuxQa_KmCvneF81NyEJZpGxE1igFCSXzM1dRLVd8KfvCr-OvZXQhufrbJqMF_URHPlhOOnwirIkA65tEdWNaCK5X8xUbH64jwvKen9t-2s_zhXLAIIiB1ckghTNJ_v8C-TeDcTCKEeXfiVAVfq4WeAOq5kk1gSjCqMocTuORUpW3QGbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش باران در جیرفت کرمان
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/687205" target="_blank">📅 19:18 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687204">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2356cf30c3.mp4?token=nXTcfij4UYmsjZEgRW6u2qDa2T8JBL8zHW8EObVAerFar8Yr_pEw7eFoCkhjmkahMVjqwRc1BU5pWVjAmS9vkLkydTB6SM-PoaEikujSMVsHJVIEt8ah_WXGoYPOddAg95f1eVsfJS7UePbtP4C2DpM3UYkABZvNeSRjltSltoGr8nFNRbDM7SxgT6o53xwqU8oCFEtmkfLwiC8iRD44i5woKkeioFgZlx0Hr8wFEDzx2Czwf3MvliclDN-DeDZLv1DlJ06kB7bNO91vPKTSa_kxZMY3l0pMDM9aaXb7rY_hQKTiG_-PYGAHA55v1F1Ur6ORZEqVCXm4RISM3tn0ZKizqEHEi15kvZNFnIOSHhV287yPde02use3O0ztocRJmAHtVrDeasH6QtPH9RL2fJuM_mUDQFQGvo0mw3If9czxgoRaoJKPN2bh1bUG2YkGGcv0DjlMXP5RrsNVRWtZqi1JoCgQX4CMR1DQwd6pHTQ4Nx3D2DsoEegaDVkLZpguUDFcH12EGDBTQLBWU1S7TpuSQr9588E-8QmPYsFqrdEuFY6zrfQTdD35R4GtHYNXoq1cLT8h6iy2TWkh7V-pjhVESOL2CZ8Naqu25X2V-4qd50H2sLM3k3Y6d6oYgQiJF5ywt6P7H8YpOPlxARDIkU_pJva0e00MzA1Hv6lFsBY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2356cf30c3.mp4?token=nXTcfij4UYmsjZEgRW6u2qDa2T8JBL8zHW8EObVAerFar8Yr_pEw7eFoCkhjmkahMVjqwRc1BU5pWVjAmS9vkLkydTB6SM-PoaEikujSMVsHJVIEt8ah_WXGoYPOddAg95f1eVsfJS7UePbtP4C2DpM3UYkABZvNeSRjltSltoGr8nFNRbDM7SxgT6o53xwqU8oCFEtmkfLwiC8iRD44i5woKkeioFgZlx0Hr8wFEDzx2Czwf3MvliclDN-DeDZLv1DlJ06kB7bNO91vPKTSa_kxZMY3l0pMDM9aaXb7rY_hQKTiG_-PYGAHA55v1F1Ur6ORZEqVCXm4RISM3tn0ZKizqEHEi15kvZNFnIOSHhV287yPde02use3O0ztocRJmAHtVrDeasH6QtPH9RL2fJuM_mUDQFQGvo0mw3If9czxgoRaoJKPN2bh1bUG2YkGGcv0DjlMXP5RrsNVRWtZqi1JoCgQX4CMR1DQwd6pHTQ4Nx3D2DsoEegaDVkLZpguUDFcH12EGDBTQLBWU1S7TpuSQr9588E-8QmPYsFqrdEuFY6zrfQTdD35R4GtHYNXoq1cLT8h6iy2TWkh7V-pjhVESOL2CZ8Naqu25X2V-4qd50H2sLM3k3Y6d6oYgQiJF5ywt6P7H8YpOPlxARDIkU_pJva0e00MzA1Hv6lFsBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک: ادعای اشغال کامل علی‌الطاهر از سوی رژیم صهیونیستی در حالی مطرح شده که این منطقه ماه‌ها زیر شدیدترین بمباران و محاصره قرار داشته است / مقاومت مدافعان علی‌الطاهر با وجود فشارهای سنگین، به یکی از نبردهای مهم این منطقه تبدیل شده و برای اعلام سرنوشت نهایی باید منتظر بیانیه مقاومت ماند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/687204" target="_blank">📅 19:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687203">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
تاکید دیپلمات ایرانی بر شروط تهران قبل از بازگشایی تنگه هرمز یا هرگونه مذاکره با واشنگتن
رئیس دفتر حفاظت منافع جمهوری اسلامی ایران در مصر:
🔹
شروط ما و باز شدن تنگه هرمز مقدم بر هرگونه مذاکره با واشنگتن است.
🔹
هرگونه هدف قرار دادن زیرساخت‌های ایران از پایگاه‌های ایالات متحده در کشورهای منطقه با واکنش ایران مواجه خواهد شد.
🔹
ایالات متحده هنوز درک نکرده است که مردم ایران مردمی مقاوم هستند که تسلیم نمی‌شوند. /ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/687203" target="_blank">📅 19:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687193">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nS5CHskJ87i4VwtHWTQaJd6Y5j4fz8-oaAhISBB2Owgd8F61vxvTAolaFOvfa35tTaP49jmniblQMuWzJRsOAEAFHNRBTgURoTwPFdOGuAWPJ_TNBgkB2GrX_yw0NVDO0wfM_FT4p-IL7QAy93nepL34qWEWBgBfvm7KdFUQyuMNGyZZijRDsxS15lFM3Dfx9gX47x2Xh4YdV9eHIN8Uy2jxW6IOgjjbWswEhsa-6zNF7-yoeI7tlMa0UF_PP3hoE70_MKbQtthpAJUfTVUPzX7By-UYtwAlPRUazx-3s2o_7zQ0Ne-8AOUu3raHZeyQeXD67rgP0axvt7bSY6FQ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dW-QrFiV1USo56tY-i1jf2pKnXiE87beXfnxhQfu6DC6ixJ_vMopPSrK8pwA2NQuhgY2IXeP22kgFo16YS6kBEjaVytDz2KTPZGYjQ1W8MY3YqbTNxXhcH4nHjmsSkeQLwvEDz3j9hXOEYmOA9dH0pSipAoDWH00frXvZOYZP6syrJXU9YI-Up9Pu8f_9B6nncHeFeOaW6kqCMFP117J9OHxd7ppZaFo4nA4KiVr3IivU43O6YfQuGXZSblgBkmWhZpqrU9RdGKsH24AmgkaqzISddIoAyvhKS0_Q_VbT0JMWqhNZ2wFMXYJfixOkaGXEn7L-i4T-NbHm6tqnTECWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ywm6o-VUL2bQDh7PFuzGpHagdSVLdgTGbCBvq5yXiiPKULnBxdfEitbIxtjxgWzp1P9i74scFeEkRS7TJERxf7arkWHybbkcrLAkTY6LJiiNDz__aArWplo0rOZKCrpBQ5qLWo0u_2AahGV5Cz36hpfPbFe8YQQlSUmdOm1G5FCrkawQJ4LCSSqzBVF_5z0L4Uh5-2nIkiBzyPf6puZf-lSZPZznkRUkxqvyVIV5D4YrIFuKb8lPJeaqKE3SLvh2PhIVKLyutJWdPlStghIkeEv7vxq2SpTn6pwNuz0wYQURqpGgKMwkSPXGLRbMR5qnshQBeAJuALpkvf9q4ygxgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A3pKeiAhJwybnklVQpUA9CzEM_ThPEhApL6YQNJmGci8_S9yHqGDsDN-DpoSN36drIKpmsvCWGjfUV169Je0BogETOGWx1sur-OEF4OKKKcC0PQUlj5FniPyXJBW_NazJuNoNmfJPj-zd1apOmxzT0Rv12HfH__OM6d95sdakwfCC08aLqzENPLQon4wfI5JVnnFCAeiy8-lHe-7MrDotx7CeTbD58vl7hpaTMVxdoIGNYSJlEGuhTqQdAHoM5D8jCx2HWuXky4yyQ3nMAp0H1NdupF7ql4aHPkp_xholiHesKmog3A-aMgmZ0J5yPibxaXnVnZ8THgqSxIjQVWgzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X5bzrmUkaTpr1wF5i7KnV74ao5LdZUnaF9ar1oJasEssOxrGKm2d-QAo9SJiD0srCHacmhAoLi3egRtSoPK5McDcShXpKveoWIpiJrew-Nkfc_CFCEzIhJpxzQKSdMIkVWMZRrNU-4XfrcJ5K0Urc58WNt45mybscwIkuX-JsxiJCwM3M377D2ffJgOSBhFB3K8MkiSWs72LKpHrbHwV6CbaCrZPYW0CKYAmFxnCVP9TVmA3wFZQGRRgRSnjGY6L-CyNMs-lO_3ykGNhxWZ5PMF1_KEit01hGkGrdPVN3p84ioJLHlOeTd97H5fUA85s0hqcuIoCNY31QGQbFNxqzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/owUr5l1-K4irjYYniSQXixI_LOLTW8U8RDdrozBAfODK-WZIfGhTt4hDcC5G-rs7ezJa-4fn-10nXwWBeYnsXdOhz4k9h2vu-QED4w9SDGBYY4UdGHplmvbKjWQhNmsBVRQnRhwy_TlXnHgmqeDKHURUFG6igV1HCCzBSaJ6w2JekmolI2zofKc5nHtlrMdJYcmOgEnDudNucHhvcLi-0iubHm97KTXb02Xg4FxuJMvCwmFIy9MHr4hO7OscGDN9RG64DFTcRXVoeHwfI4cgwwL8n8-BpOPs8UhE4PqRaav7xQGgfvy2Rid-te_CT8vkYYeAuT6T9-IAUqZyyTCu0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KkFHqi0JO1Crae1Lc_wWmdyFWsOiw9Qspxv1VpIUmawZvfhwbQ6LWGxBdiy8MsgGfX7jX-82Qizz0lNauGfucfILKXI2h2xXvOAh3zQIAGL9UcF3rZK19lyy5gR5saJ9qTZou9XutbP9rAKoIaKA8ugTsFu3YOGNpCiq6_CClc0oHZX9VymVD_i6b9E--H-u-H1gB_7kTb0IzSsTaq6F3tWAtmthU8HG5geDRcv5GtkDMRsLIbMS5dKxbJCOdx-K5akXXPjc_oHf1LEfrCTxGt4HbuP1GGjCRQmpunTuP-vtvAELcn8ajNE99rNXoOvCL3h2p5-BH6z9syGmftxiiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kadp2cCsi-8ksM66BKcNfu4h_prNtenFuClFAU2mTFo9dB0DQNiEK8kXb0vBvYYSFqHcGryScIDaLFSKKnJn-Bthwk7l-RdAhGzVT1kQgkQVBqXIOZ7YZMmW3JNiZ52u7ncxJerSeEtlUSPqK0qdCkjFgFdp77EkEj6tF2Pz16RZC9T1Z3dF_Qll8qB_DMTXlcV1qg_Ikbw_oLUfQKXqHYafZlhVGgIACe3JOj7X8e7HzooJX0zc5MItJ8rPM4-3IEHlyBUMusVwmJZ_kfYdlQXBzUVrwMzEnqrgKSJ2pnNfchtF_HNHXbe5PwfxjVS2YTOYoTId8lH1PvNicMHaKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sAIXcZqOc6xgQiCslff_QMJ_jBNEqd4sGwpJY9jKniwIcnQQeybG8Qfe-3ccmdQw9vJ0fBL0SYSkLPJqmwTL01igOmg1qEu4-Vu35o3FNvUH9s30iDa8Yr6UeH-eBOprmoJ4zse4kwirpozAkL8aN8zbF6fIp98hQ_v_a4mT2boOD2TEaumGqYoDOsxx07zwRTj9oSWNiD9I7SJp6Y1J6RsGkau9dghyiOJg9SbytQSZ4Ys1t6PBRW_8bW2NIn_RdYFwLGxo1zohxGBViHG6lWUbPQ1qJIbow2rhZyev5PhsIZ7I5Ds2z1afPXo7ODgfk3FkqPxnkI51LCMs7JZFfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phDpgNrCZUtdU7zU33Po6O8U2BiVj_j5-aPbw9aMEtQSrEOsgyjtgwTe7PtYMNL_XaI9FMAwaOWng-tvqjfJWaLr67gg8MNwKx3YHwCq2_SqWfUn1Rhyr5qbVZGnxBSjoT3p5fnUThj3GqN8EeObhugPXe2OJGOLgumn0S2pvqGmnrCLwTaOnwcFmON6lKoTJ-qAMOmXT7XpjOXPJiDk83J0B-wniG-MHDWnIVRKVhyjAnTcsqeW-CTKa3JDWUtDVDvkM5hYOfBCuUfy1QhTSG-_kQT_q1dszdt-Ar9F537ka7bHQ_ElXkKoKLw4TDwD2OZE_hGRlT4NM6shfOuW0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
موانع و چالش‌های واقعی در تأمین داروهای ضروری
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
#درد_دارو
@Alo_fori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/687193" target="_blank">📅 19:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687192">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرمانداری قشم: انفجارهای کنترل‌شده مهمات عمل‌نکرده در قشم روز شنبه انجام می‌شود.
🔹
جاده چالوس یکطرفه شد.
🔹
رویترز: آمریکا و متحدانش خواستار ارجاع ایران به شورای امنیت از سوی شورای حکام آژانس شدند.
🔹
فائو: جنگ و تغییرات آب‌وهوایی قیمت جهانی مواد غذایی را افزایش داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/687192" target="_blank">📅 18:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687191">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fff2a5ffec.mp4?token=AEs9O8eMk30W_vwunLhLezy2aVOedo52VEFePxBMVtlld7BGR8oMa2ovHwOJTAYqJGEJBLl86qhZgvKg5sNCknLLwKHqqasWUQzj7-g3NeLvshUhXndXmTzgg95ZXhBcxC14zlkJQGjSFhT8wDu0O4CM1Pq8NZhnz_oWVPjYhvi3X_3Hx-z2hugXMhbLNCDYPVNtEbv5QGa0DYPJHdFqpVbtRGyDwzVo1_H5n7vDH3x4zFlUDeEL68PwwsxtHz8WMAnJR-gDG8bdl0GaV7E9CY5_yap__MmuCznhEZk9_Aj7XiQwxwXkUS_UDQiVJYhSQkBnI5lpsnF4fIWgJfAGSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fff2a5ffec.mp4?token=AEs9O8eMk30W_vwunLhLezy2aVOedo52VEFePxBMVtlld7BGR8oMa2ovHwOJTAYqJGEJBLl86qhZgvKg5sNCknLLwKHqqasWUQzj7-g3NeLvshUhXndXmTzgg95ZXhBcxC14zlkJQGjSFhT8wDu0O4CM1Pq8NZhnz_oWVPjYhvi3X_3Hx-z2hugXMhbLNCDYPVNtEbv5QGa0DYPJHdFqpVbtRGyDwzVo1_H5n7vDH3x4zFlUDeEL68PwwsxtHz8WMAnJR-gDG8bdl0GaV7E9CY5_yap__MmuCznhEZk9_Aj7XiQwxwXkUS_UDQiVJYhSQkBnI5lpsnF4fIWgJfAGSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای بسنت: نفت ۴۰ دلار خواهد شد!
🔹
در واقع فکر می‌کنم بعد از این، در بازار نفت با مازاد عرضه زیادی روبرو خواهیم شد. احتمالاً قیمت نفت خام را در محدوده ۴۰ تا ۵۰ دلار خواهیم دید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/687191" target="_blank">📅 18:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687190">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZp5ZPxipIK6hzrDGL2xLCIHElYf46zR72KO3Bm4VFOE5gC2oPXuiZLdXczFoaEw8wv0-S6_0oJsmZfXGblCj8B42HSF6ZC0o25lHEWurMx7gXt_1MKk2FfJDSRf04p-Tzm88m_4vppZBwjqUgDGBEqWyMWFQigzO-jWqCt6H5fOVCNaKMw1hGOGEUvr9CcGlX6L_Kz8HZHfGp7jlxDb5D2Hl_T6VJEmb0a8xsIqXNN8KTbAJQ63Q4syZav0G0lATigSd1wtBaSUf8S0dallheoc12ePSw0cFSiparGp1ausFqpiRZLCCYjwi1lHWUBrYzV81SuJiBILKqhyYqYx7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابعاد پنهان اثر استروئید روی مردان!
🔸
استروئیدهای بدنسازی فقط توده عضلانی را افزایش نمی‌دهند؛ این مواد بر سلامت قلب، تعادل هورمونی، باروری و سایر اندام‌های داخلی اثر بگذارند.
@amarfact</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/687190" target="_blank">📅 18:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687189">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSNdORo9fQfOVHQoiBND4VqTvtcZ7gSN400nE3OAyXuuT5NQmEAbJ9lh8UDEaFmc7cQaAxt2XbLRHnUgq0Jwu14Apr0WFfbJGWZPLz5a3KddDMjqXKxjJde3hDPJq4cUus0QmCljctqMzv9Bb__sUtdFsRpNNALYf-UO0rlNvjHJ8BI75cCgPiKIKHz6TRxB9sOSmTfaM0GHsUpcZ5cPxKAhN_1ajR9Kl2PcaR_7QGJSraQ5pSxF9fCWoY4lnmw26wQ6Zj_OzPPqfhhR6DERoJG8grrcHoOetzQicbFOkdLNmbIsQmVPQlKzXQeR92tk9RGCSRz1uMqnVMtI3hQcjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ربات چهارپا با تقلید از سگ‌ها به دل آوار می‌رود
🔹
پژوهشگران با الهام از حرکات سگ‌ها، رباتی چهارپا ساخته‌اند که می‌تواند به‌طور خودکار از میان موانع تنگ عبور کند. این ربات با مشاهده حرکات سگ، یاد گرفته است که چگونه بپرد، پاهای خود را جمع کند و به‌راحتی از موانع عبور کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/687189" target="_blank">📅 18:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687188">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npRZyZOGJfb694P1gF6wcHMGZYfL-9MQbttHxwNlzst2kUoUo8xKwP7lbpBYkEOO-2Nmcy7fj_i70ZJf9vXKPpLa0x4CgcCMpiCkvKtEy5T9IN3GV_duXY4bL2oV7VESqR9mgRHHV18yy-aroVPj7hUENDsHwMFnpsUFQUtedzrWacA3lMHm8mAwLOReMolxOpE0NTpGI90D4YNNfKLRRd9KPOk8AastDpSqaw5i1kcubfHdUu8powD0Y9zjhCgIzb_8YcItwo9Tc3xMzSSDw7dh0BNjVezeR4YXHS1n1214yxkuKqqambZS4RuqclmMilfEf6iKyhmfw3fDkTm4zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه هفته ششم لیگ برتر فوتبال ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/687188" target="_blank">📅 18:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687187">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
سودآوری شستا در سال گذشته بهتر از سال قبل شد/ خروج چندین شرکت از زیان‌دهی در دل جنگ و ناآرامی‌ها
محمدرضا سعیدی، مدیرعامل شستا در
#گفتگو
با خبرفوری:
🔹
با قاطعیت به سهامداران اعلام می‌کنم که سودآوری شستا نسبت به سال گذشته حتماً بهتر بوده است؛ تحت تأثیر خبرهای جعلی قرار نگیرید.
🔹
هلدینگ‌هایی مثل تیپیکو، تاپیکو، تاصیکو، سیمان و شستا هم کپیتال گین بالایی داشتند و هم سود خوبی؛ این نشان‌دهنده قوام سودآوری شستا است.
🔹
به زودی مجمع سالانه شستا برگزار می‌شود و نشان خواهیم داد که شستا در سال گذشته درخشیده است.
🔹
در سال گذشته چندین شرکت را از زیان‌دهی خارج کردیم، آن هم در زیر جنگ و ناآرامی‌ها.
گفتگوی کامل را اینجا ببینید و بخوانید
👇
khabarfoori.com/fa/tiny/news-3242509</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/687187" target="_blank">📅 18:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687186">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eca538937e.mp4?token=duEcBfdE-SbKNOD-OK-Foewch4lWO_sPIRWOInXbI0IRKDwfi6UTZe9XWm-R97rVhEyeO8ifQ9RyTtDU_iJV-bsy0U68yZ9WnZVVf8UlzYNVF_6hAhu8_IVEpsmIPsNLAC67LtS5Btfq5EvnCX2cNPmalGgdY3zN1SIztOJUVQqjde1lPCWuRO8kLVa-NrmWqoHDW9yI93ZwF2JOn7KU9wkLMnkbnIR0bnvw0180w5yePuxG63Gz6-ZCgWRu_RjTWrcWjIN5VgEulMPkrYKLxZYuXVJ6wA6PjhqSIgKYm-qO5sc3AiMphHCiF-mxPDBB85v1go3zi_khOqZCrvxMDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eca538937e.mp4?token=duEcBfdE-SbKNOD-OK-Foewch4lWO_sPIRWOInXbI0IRKDwfi6UTZe9XWm-R97rVhEyeO8ifQ9RyTtDU_iJV-bsy0U68yZ9WnZVVf8UlzYNVF_6hAhu8_IVEpsmIPsNLAC67LtS5Btfq5EvnCX2cNPmalGgdY3zN1SIztOJUVQqjde1lPCWuRO8kLVa-NrmWqoHDW9yI93ZwF2JOn7KU9wkLMnkbnIR0bnvw0180w5yePuxG63Gz6-ZCgWRu_RjTWrcWjIN5VgEulMPkrYKLxZYuXVJ6wA6PjhqSIgKYm-qO5sc3AiMphHCiF-mxPDBB85v1go3zi_khOqZCrvxMDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش ترفند مخفی کردن بند کفش برای ظاهر شیک‌تر
👟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/687186" target="_blank">📅 18:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687185">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
تحریم‌های جدید آمریکا علیه ایران
🔹
منابع خبری از اعمال تحریم‌های جدید دولت تروریستی آمریکا علیه ایران خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/687185" target="_blank">📅 18:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687184">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/687184" target="_blank">📅 17:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687183">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
عذرخواهی AFC از ایران بابت اشتباه عجیب!
🔹
کنفدراسیون فوتبال آسیا (AFC) از فدراسیون فوتبال ایران بابت اشتباه عجیب کمک داور دیدار کره شمالی و ایران در جام ملت‌های زیر ۲۰ سال آسیا عذرخواهی کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/687183" target="_blank">📅 17:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687182">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
تحریم‌های جدید آمریکا علیه ایران
🔹
منابع خبری از اعمال تحریم‌های جدید دولت تروریستی آمریکا علیه ایران خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/687182" target="_blank">📅 17:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687181">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
قیمت گازوئیل در آمریکا به رکورد تاریخی رسید
🔹
قیمت گازوئیل در آمریکا روز جمعه به رکوردی بی‌سابقه رسید و برای نخستین بار میانگین قیمت هر گالن آن به
۵ دلار و ۸۵ سنت
افزایش یافت.
🔹
این جهش در پی اختلال در جریان جهانی عرصه سوخت در پی جنگ با ایران رخ داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/687181" target="_blank">📅 17:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687180">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/852c8954b8.mp4?token=rk-QPp7MUja4iANxxXWvKlBAupugDngHSpUSHrY6YeScy6c8o9ZzLnNyjrnBThs-_KoQNaoWcfqCWLbGdo5P1BiuebZuoORpsk7R_0do3iYjxvWE2by-PLdBL32ghYgJ_kWhUw-wY6Cy9iqT4jZkCLDdOnaz-p5rzQ_FkjQFoLzaxpIn7EDgoafvfMhAkfG8wNjbJNb9RXU1J7T_4rlsUD6RNAgKOl2nV5D68lTp3yl2-DupkSJ4oXzF-k5ReSzs3KbeYYtqdAMb-A247DB15CxZt56emwRtDzGULAJ2zZJE8InSgIFTGCN5JfMupO8gDvWrnElqqGdMdCzsRM2Uy4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/852c8954b8.mp4?token=rk-QPp7MUja4iANxxXWvKlBAupugDngHSpUSHrY6YeScy6c8o9ZzLnNyjrnBThs-_KoQNaoWcfqCWLbGdo5P1BiuebZuoORpsk7R_0do3iYjxvWE2by-PLdBL32ghYgJ_kWhUw-wY6Cy9iqT4jZkCLDdOnaz-p5rzQ_FkjQFoLzaxpIn7EDgoafvfMhAkfG8wNjbJNb9RXU1J7T_4rlsUD6RNAgKOl2nV5D68lTp3yl2-DupkSJ4oXzF-k5ReSzs3KbeYYtqdAMb-A247DB15CxZt56emwRtDzGULAJ2zZJE8InSgIFTGCN5JfMupO8gDvWrnElqqGdMdCzsRM2Uy4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین چگونه می‌تواند به ایران کمک کند؟
🔹
پکن در شرایط بحرانی که آمریکا جنگ اقتصادی را علیه ایران آغاز کرده، اهرم مهمی دارد که می‌تواند به ایران کمک کند.
🔹
جزئیات را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/687180" target="_blank">📅 17:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687179">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62a5eb2d1b.mp4?token=cyhEWXkOWdKROab0o89eBUbXXz7eG3SnPpNu1z2oCe802YwI-k3gqg4qOdPzJ3hGma5JCt9MLc5-4-DXL7I4jMyRrwiV8opXYI9vqd-s5qw39tbti-tpyP5rIO_ZZgxqBkz8D253Sm2_VzjFjxmsDjy8kwkFcRIgzkNaHFJ9Jb3yVaDXQYL8bB5s3SmqqhqCLITBXyapDZwk3BlQ_OnES1g8gfGTpr1y5acZrcitYLArwZWJ2yahMJfLWYpk-z62DjqQiCPIoJcU9MBLfOzrkEzHUgVQf3r8j19jO2DBgWlGMuxHKr-Cq-_6BK9DnIXcqq2NIyo8OYN7VXtt81fANw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62a5eb2d1b.mp4?token=cyhEWXkOWdKROab0o89eBUbXXz7eG3SnPpNu1z2oCe802YwI-k3gqg4qOdPzJ3hGma5JCt9MLc5-4-DXL7I4jMyRrwiV8opXYI9vqd-s5qw39tbti-tpyP5rIO_ZZgxqBkz8D253Sm2_VzjFjxmsDjy8kwkFcRIgzkNaHFJ9Jb3yVaDXQYL8bB5s3SmqqhqCLITBXyapDZwk3BlQ_OnES1g8gfGTpr1y5acZrcitYLArwZWJ2yahMJfLWYpk-z62DjqQiCPIoJcU9MBLfOzrkEzHUgVQf3r8j19jO2DBgWlGMuxHKr-Cq-_6BK9DnIXcqq2NIyo8OYN7VXtt81fANw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساختمان کنگره آمریکا در محاصره طوفان
🔹
نمایی از ساختمان کنگره آمریکا در حالی که طوفان دیشب  شهر واشنگتن دی سی را درنوردید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/687179" target="_blank">📅 17:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687178">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
رئیس شورای‌شهر تهران: مترو و اتوبوس‌های تندروی تهران تا ۱۹ شهریور رایگان هستند؛ ادامهٔ این طرح به شرایط پایتخت و تصمیم دوباره شورای‌شهر بستگی دارد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/687178" target="_blank">📅 17:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687177">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQmhFnAdu3rWGe7JRrTjaDA46hopVnRLsoph7thYrl2RFmMsgtBFzXzKP5e-jqPcoz3NsIZA9dBoCG4qRM7E2HKxsMCCqymHqlaeiKj8VxiLLQ8QjEP4DmIPcT3DyIw0l3fdIKVLX5j31-O0PG-idDJeW0-ALK-jZsRkm28Yvb9wkNJn9f3iVR_e1_wP4aMeb1QWgkIfvMOJ_4IiS9jwyNKul0nGIu0J7w3BJjYLsCIauK8FxQZriRgYruvSiXk5-dXwkA_N9rbBlH468m9OKrSYzEmASw9n124dxrE48uSQogKap3gM9okY7tbHvJGVqbjkyJPbyyv8nZP7Q_6R-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصطفی نجفی با اقتدار قهرمان جهان شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/687177" target="_blank">📅 17:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687176">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eed0161f0.mp4?token=AcyydE0DmmF6gggZVQGqjqoE__U-bU8lCyLtyKV8P9g6dMcq19tR0iQBIXMnQ2eT530iEHCWDku8E_VOnliZF7_1q0q4L7CV-GJ_2JqjrJIf4dHmOZh2s4eqxI_zt62Q9UqpUrOdfVYnfEzBIvZbh91WP_gTBAAYMTX54cg6fnHUaNQDo5FuEt9areNhI3zBM9scLparOLdCrlrj70F7J7wbsHWNnZK2MVAcqIRFh1lwJ0sVLdUAuwZvTDIlB0LMPePp2_ZicT_Uix7Amhx4Ra833nfiFxC6zqUdOrM663Pm2kWu0Nj4ekThaeKN-jaY9QwQvBmEAJtJLaqq9ydRKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eed0161f0.mp4?token=AcyydE0DmmF6gggZVQGqjqoE__U-bU8lCyLtyKV8P9g6dMcq19tR0iQBIXMnQ2eT530iEHCWDku8E_VOnliZF7_1q0q4L7CV-GJ_2JqjrJIf4dHmOZh2s4eqxI_zt62Q9UqpUrOdfVYnfEzBIvZbh91WP_gTBAAYMTX54cg6fnHUaNQDo5FuEt9areNhI3zBM9scLparOLdCrlrj70F7J7wbsHWNnZK2MVAcqIRFh1lwJ0sVLdUAuwZvTDIlB0LMPePp2_ZicT_Uix7Amhx4Ra833nfiFxC6zqUdOrM663Pm2kWu0Nj4ekThaeKN-jaY9QwQvBmEAJtJLaqq9ydRKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روس‌ها دفتر پوک‌لاد، رئیس سرویس امنیتی اوکراین را هدف قرار دادند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/687176" target="_blank">📅 17:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687175">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lI5zfJUdq4M3EyF4tWlaXYjqOYzfS2_VYePCI6YfCMXUuaGlQIbPNOYbguosr4RczAypWtCbjWYF1DxYUZBLntKxhtSdIZtZmNy3WIBzZYqud1-rfCLUFxl6RFciXexiQSEFWPhOA8c9IGrghSvcE2HJCDbG9-Tb39kFZWOytfM_gfGSadxNe8X0DcNQXvm1NVvEk44sWfDz84wcQ-XK__lskODcNLefiBpPahjVCvAH3joEBeY86yCXEAXup1peY7rCQPIZhQc48U9hxCXRhrlar0oBrQhj7g6YswfoHj-IjHAXOqjMr7sFVfCBNspsUCjinFWWZNa0jpp8b04OAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همزمان با کاهش قیمت طلا، ارزهای دیجیتال هم سقوط کردند!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/687175" target="_blank">📅 17:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687167">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/upxwYOojOjRii4-IWVLhdJbX318r1sZW2Z38ww_QI1bpK8CkA9Wy2jkyK0gKojLIlKGMnFzYlfbXhzKfKvT3s2Tz7c2FM0nIWyv1BXs43duF1QzmFAxkHIi3i1v8JsILN03AAioJRdQ-_Rhdh9kA2wmIWLFdCC_WMP80yXapDPepnsPW6bbLcCb20bKLtxeCd9wrjWuYA__e48U0HwkHRM4R_dPZ2KzhpPDCP0j7D4yA_UwkDzcN7sEaai0_uE6aPfeUdNrOHke9UkjHrprReBg4z1zZTleF0JTMJzjU64DlCLIeBQ3YgyhjNOgrZiU_Rvs4ljj88AysReUpGd1zVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ggu82DT4asbfaHQCVrBSmIB1039p6eYhyFQQ8nJpYvvFs8BSM4cjMaH5Xp0f1Hjayt_2cur8uNGqV2Fl0Wj-KIrRX9tt7lr61qJSnbAVi_EO4e0hnVNqSsEADlcZjm9YqQwdjzAZ3sNXoQmZBwmUgW-MuY7cOYuckUuimd2jIuPJYVBGhDftaSkoZ7X0PKVuQtW9X8PV6YSao3jN5YLDN6HlOl1G4zvQ3LFEc3SCkP9CZ5vl-TVDirs3PT1O9tl48jAD4OO0mIYrlRQHgknxdm362fWe5p9FzGlfetsQs8kI6eYIWvKxWIvGTvQW-k5OHkRG_461J8tCd5k_RUIanw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sRQQKe_ZETGpllwxkSOC5BiWNRDmquMf_S2kAJbACtlChDEqxQcRqr4G8wzHhd6rT2X_HgKbPLIC9tCoVR6RMuxtrbHqru7R8qMyjOHXyvVpMv8qOXdLFjyClywvjgvf_qjVn7urjeZR0Ka9q4mZOegvXHz8bTRZmdnb2PuEoZ4_F-d2fCmujedXTZ-RNooFfIDCXLIwlhDt-T32CdXuYEjjLqXkQ1EOpUe91eYpT8F5JfNHxdsB_chCyazHUjnP4hskGZLzliW0W-dLNgyUqt4sTt3LCj6mnxf1N5IaGG_Xpt7NWMJTuSn2m3JL_XO5m-GSIIXI461b7dzRpCCXDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kCEQXghkXMGlvzqvLG0UaKJAj_cQEH_vrFNSo1nT-DOCYDpXv5r17m16yGZRNC89gkrj8xye_9uAImhYCXtWsLA2ANwad_upW-e8F0edoY9SqRozIsNb9USq5hB-e43MfVAWK87MBU_aKVyRHDpGdGNwEIHmB7eWJc_bOvlCffBNncualjF4cXWEPtVuU6nxNWQt0Tgv6eaR9zVF9HToAAr9Iyh2WLwTsP-IIpM_UlnpY2_eEyujToxlOrZLE3uT8fU3hErNuVkgqF9OYFpP6VuqPZ0L4mn0BgXdIW2NNkjLAECxDD2mcdzgFhuVx7fOx-Rf1zH1Z1KLa3CTtV9IJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKxannc4K-zz_cLYO23_LXwczFzhH7pXiUhm_qJRjNCFjTlvCU17HLZFtWBN4A6HlPINxYjfg1RqdcfW3GopJi0ndJmxQjDioNEn6gsHdOLTQA1C45sMmmL4pyPEuxlGGQSCY46RZDaLeP9p2X9utDSZ-Ji_izZqRKdg2DnSGjuZz629c5KQ19xwNU6aX6mHSJ680I7dtd2NjvOF2bNPd5Qov_iKs4_XFw5tfyew4NYVVuBnw1VvkjzAxr_4JthvCKH4JvMQdjsT6PfVASA0nmpNBRTJk-ZuKgSpY-DlTMIbLAMdn1zucTqc9cR_5nCyuTv26F28fBHQQazizIPmqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cji9C0Rc-rT2c8fZLMNO-iAjEqie_zsj2Y3c1cKUqcB5pyb_GlT5o645NuTOm0kzmSwwsBdAVNbbqhE8Wg7G7Guc-ANiY1dTMBZyhqfMc7grzD-MTyI22wQ5dmu5FvgUOO8M9TTpnPVm5OA6isWEwJ65iSrPTZBRYw8Gy09vJf5IRy6Z7WLYT7JarDo9tm0pPHFQIX6d2OpuJU3CN0vRBFRPiKVjW44z1UgX2dKwKZeVgoKwGVkECYzSjh35kVMnfG4PUYdXC7Urzn0gr9nERLAsAKmp1BfBfwO5E78v7MdR0VruGPPtKj-_E3ge2CHE1iNK7Kcrqy7WO5a-6B9PyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fzK1RXTJ5lX0MIJDITh2H5f5poFbeZDZ4pLXPpvjOF2nJMx9AppWKoA-k5SVVDYOHzJNlrTKzyuMODMZVgXWpx9_cfc3Mnzdwz1gTX5rBoJ2gccB1SAqbNyB5vwjMuqfZJb7AMjXXlIrs_BPByMuVXmB-0nUivJyUcum85aEUmGuRu3JrjqtnM_9D1H5ewDl0bg5cKR0Kz8-c5JNBsJQwy1xqbn7olAICCjEcrCKu9eDV2bPiGKG2xmgYvJ7anay1L_XWIv8yw8RveTHs9B0yGQ0y6ECxuYjpkLHBn911DpLpzcxXbG8fUqlYL9ZZmuqtFoK8CKCGnfxGuOhN7_qag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cvgg-huPpkUiYkJZDeoCpCcbUHsxIHXu9Q8Fe2AwZmzBy5sjmRl9GxSijWleCi-gUX9qAh11WmV6vJn8X1ISuocTtR39Yu7AyVTAENMvpsFzDpSOHubAjRj5bTjBn4GZrrPvPc0XXlGtpV3D187xuP5HgQR041FUkijYxq_ccf72LIdiGMIzjzYngzSLbyddMsXTnU8j6sEGhFkj35X9_WHv6eqVX0cq0pEufMhYYfvjOGSpBmOrjQ6oim92KC857N8jIQ7FSw4-joHuGmDkq527BqAv78jEfOWtR8t3OXgoYBpPsTvufl9Z1kMEXg7m54HThI_7MTtwyrBNFv1VQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت اثرِ یک همراهی
💫
✨
هر همراهی، وقتی به نیت خیر گره می‌خورد، می‌تواند اثری ماندگار بر جای بگذارد.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با نذر و قربانی و توزیع گوشت قربانی، در مسیر حمایت از خانواده‌های حائز صلاحیت، این اثر را ماندگار می‌کند.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/687167" target="_blank">📅 17:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687166">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vO5ybWng5eJuEUPpkKFncJO-1mqUpOSyiiMuTbMXCUZ01U9XbCsIAMGVFy4KEtjiig9oCOhvsKCr_apog4BjCsyU3Bx8uAp5mmJvcvIShO88BoCa6UY4aW78lTeaCmu1-pVJ2oquWHymFuo7f3lHx2eeHbw8gV1s1sYt4Y01DY7_wcHC-gUQhaD2x9dXGvNkZm9yhT3hw6324afuAKwG3V0i1yqsPdJ-aP9tSuiWq0Okt-Ok_J94q_LvbXHGpAio6dkMci-jLoV16uxIHcAzV-UN2c-AkBJxURaj74rFzD-Q0P_BU2iPlz7LRKXPkypkwTYWpdfcaiYfp1h1U5CosA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش وزیر امور خارجه کشورمان به اظهارات اخیر همتای اردنی؛ ایران برای پاسخ به متجاوز چقدر باید منتظر باشد؟!
🔹
به نظر وزیر امور خارجه اردن ایران چه مدت باید منتظر بماند تا به متجاوزی که نه به حاکمیت کشورهای عربی احترام می‌گذارد و نه به حاکمیت ایران پاسخ دهد؟…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/687166" target="_blank">📅 17:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687165">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3GLjugEqLRPsq65aDZdrTMBnUIz6p4Gu3tanTtgGJmfyZPdwKK7LB6TwKIwC0LW5M4n6mR8TROazZgVGRLQfhLgQ0yVGQlzroDcuoIfWBfaX3SJYt6tzCgjkkyoGznA3Fs5peSKUWuvsTuRIKqvIeSMPm5gCPh8gTk_UvYGc6VLRh-9ez1iivhsS3MZ0U5CWDrIgJKKda4ZLzYRnsxnE-fwQusoajcw_biLWzws5I6IjTrapeGwyp2ksO8D7huaDnXuwS6sOvYGBPcKpAhPXMnqF2fgAHQTO5SJpZps1uh8ceFDi3Wns0pYh0lw_o2WWEOp_ahosDhCGE_jJA_k9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ۶۰ ثانیه چه اتفاقی در اینترنت می‌افتد؟
🔸
تنها در یک دقیقه، حجم عظیمی از داده در دنیای وب جابه‌جا می‌شود؛ از ارسال ۲۰۴ میلیون ایمیل و انجام ۲ میلیون جست‌وجو در گوگل گرفته تا بارگذاری ۷۲ ساعت ویدئو در یوتیوب.
🔸
در هر ۶۰ ثانیه، ۴۱ هزار پست در ثانیه در فیس‌بوک و ۱۰۴ هزار عکس در اسنپ‌چت به اشتراک گذاشته می‌شود که تنها بخشی از فعالیت لحظه‌ای کاربران در شبکه جهانی است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/687165" target="_blank">📅 16:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687164">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyNKwpsGvTwfWpc22YYZTBbjI9LtjEmgtPRBaWltOMj1E01UEBGI6WMk8WjkVp2JItF-bYHcFQERpxhIbSMkU02t452D3XdYi-T3apJYdyX9H6AvS-6KSOxgRl5F8QAXR4l128WlL4TTfv41koqJdU3lrQxpGgMkbpWntdMbMlpqzqhgKKZphm9Ax3TQYQ-oGYco3EOlqoSiuSismP8IPZE1_kwrXwTcIfOm_-PKDkw0SfL0ilw7WDONoGDGt-fPsb2hnZ6f130ZPwiI9hu23iNCpViXEmWG5e5l-abaoCJ-kzLJrrymhMV_c30qR05ES_u3FDiIlt1U071XI4JdnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره ادعای آمریکا را زیر سوال برد/ تردد کشتی‌ها در تنگه هرمز زیاد نشده است
الجزیره:
🔹
آخرین داده‌های ردیابی کشتی‌ها تصویری متفاوت از ادعاهای امریکا را نشان می‌دهد و تعداد بسیار کمتری کشتی در حال عبور از تنگه ثبت شده‌اند.
🔹
طبق گزارش شرکت تحلیل دریایی کپلر، تنها شش کشتی در روز چهارشنبه، ۱۱ کشتی در روز سه‌شنبه و پنج کشتی در روز دوشنبه از تنگه عبور کردند. این شرکت میانگین ۱۰ روزه را ۱۳ کشتی در روز اعلام کرد.
🔹
سایر سرویس‌های قاچاق کشتی نیز الگوی مشابهی را نشان می‌دهند.
🔹
شرکت داده‌های دریایی لویدز لیست اینتلیجنس، از ۲۶ آگوست تا ۱ سپتامبر به طور متوسط ​​حدود ۱۲ عبور در روز را ثبت کرده است.
🔹
اگرچه بریجت دیاکون، مدیر اطلاعات و تحقیقات دریایی این شرکت، گفت که آخرین داده‌ها ممکن است «به دلیل تأخیر در شناسایی عبورهای تاریک» ناقص باشند.
🔹
این بدان معناست که برخی از کشتی‌ها چراغ‌های ردیابی خود را خاموش می‌کنند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/687164" target="_blank">📅 16:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687163">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دیدار و ادای احترام وزیر ارتباطات به استاد خود پس از ۳۰ سال در اصفهان
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/687163" target="_blank">📅 16:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687162">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-9b2gsXrYKntHQ7jObtughy4sxm3ddb1EHhE2k55AvwL85V-mWYEcgJpaXSjFDeFwY8NogfEtxzhsSG2pA7JgsSvKrhhUQC2IkuFFqAPzxWit_9Ut6JxIDX0YrprFHq3EGm0A39rWTW9xiCXfdeEhk71OtTgDzX7xzc_Flg5V3i6tBP-JF8mAILqBskDkM-R4C47Z5FXcSpKHONMyQZsTwsfSezc7OXJTmsJZju-EBfyDI02QbJThFic09dNC-SFzvTvO3Qr1Hex7jSe4fVV1o_0rD9-pnI1AGoCc-NJEwuB85AlaTOxTqXTDTfmk8BI9lONXS5ptAB-2UcRBTzOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نیم‌رخ» از امروز در زی‌ویژن
سریال معمایی «نیم‌رخ» به تهیه‌کنندگی علی طلوعی و کارگردانی رضا شریفی، از امروز جمعه ۱۳ شهریور، به‌صورت اختصاصی در پلتفرم زی‌ویژن منتشر می‌شود.
مهدی سلطانی، حامد کمیلی، بهاره کیان‌افشار، سیاوش خیرابی، شیدا یوسفی، مهرداد نیکنام، شهروز دل‌افکار، مهرنوش مسعودیان، مهدی رکنی، پونه عاشورپور، افشین سنگ چاپ، لیلا بوشهری، رضا کریمی، بهزاد خرازی، یوسف مرادیان و محمد شیری بازیگران این مجموعه هستند. سریالی که روایت آن بر پایه رازها و رخدادهایی شکل گرفته که به‌تدریج برای مخاطب آشکار می‌شوند.
زی‌ویژن، پلتفرم نمایش خانگی نبراس پیکچرز، با انتشار «نیم‌رخ» نخستین سریال اختصاصی خود را عرضه می‌کند. نبراس پیکچرز پیش از این تولید آثاری همچون «شغال»، «جادوگر»، «ملکه گدایان» و «مانکن» را در کارنامه داشته است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/687162" target="_blank">📅 16:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687161">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
سخنگوی ارتش: پاسخ به تجاوز احتمالی اسرائیل سریع‌تر و کوبنده‌تر خواهد بود
🔹
از بین رفتن سامانه‌های پدافند هوایی دشمن در جنگ ۴۰ روزه به‌معنای بازشدن مسیر حرکت موشک‌ها و پهپادهای ما به‌سمت سرزمین‌های اشغالی است.
🔹
اگر رژیم صهیونیستی دست به حمایت یا تجاوزی بزند،…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/687161" target="_blank">📅 16:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687160">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec2d056894.mp4?token=LfBk4W6AKogc708DwM4TXNuI-jj_t2aHZkAwcN4J28YdiB4ILorzToorb94ISu_NFXtibPYkX3HTNPbo4UFXESCB7VM8bJ0r6OEVhGGFA8z3P6qmT3XaZ2R-BP_bEgLAt79W3GW85vYgdMuMJX57jZxDc3Ar6llhEpSc5gGfl2L-vCDKe9jyoddtU2ZjKZR7ZlZw7By06BUwsZvSxP7av7YT9MAysOQCCV9MsLDVQyivqMls01Is5vGtY7hC-2dpMfM7oRzB9pENM-dfGeJG8EPgHCHyVZBLyQY0FRpJJqnEL-MRESgEzLchFYr1sTa2HsHp3G-KAsbXwdHERtNy7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec2d056894.mp4?token=LfBk4W6AKogc708DwM4TXNuI-jj_t2aHZkAwcN4J28YdiB4ILorzToorb94ISu_NFXtibPYkX3HTNPbo4UFXESCB7VM8bJ0r6OEVhGGFA8z3P6qmT3XaZ2R-BP_bEgLAt79W3GW85vYgdMuMJX57jZxDc3Ar6llhEpSc5gGfl2L-vCDKe9jyoddtU2ZjKZR7ZlZw7By06BUwsZvSxP7av7YT9MAysOQCCV9MsLDVQyivqMls01Is5vGtY7hC-2dpMfM7oRzB9pENM-dfGeJG8EPgHCHyVZBLyQY0FRpJJqnEL-MRESgEzLchFYr1sTa2HsHp3G-KAsbXwdHERtNy7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه میخوای بدونی پنکه سقفی چجوری کار میکنه این ویدیو رو ببین
#موشکافی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/687160" target="_blank">📅 16:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687159">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWCz4Ju_w2zLTDTqcMetitWaXzIZzloL2jEBokkoFxgKoLwQQy005D7Srj_IC2d8fRpQRj52lAaer4_SfTLt9CAZDojJhWHdlEEB5JETOIEiHge1Gaagt4672wQl6lPXBYcvf-NJ4YxrEtYiSbkHOUA_KVg3o_jol6awhyWiOn2JUgOi6bPMNvTORZ9XJi50AwpZOt3guVdyA5rCVO68Qbx6GiwMYgf1vt7NRvWlmTkkOVCrGOjL74GqETEXktQrh747XZS_8Kb2xyv5hJvjiwH2EGoHhol8E90blM6g2OHWGFLUfaBaCxLJwK3lh0oQAPT5L1iaIFcUfSGerYalXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همزمان با کاهش قیمت طلا، ارزهای دیجیتال هم سقوط کردند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/687159" target="_blank">📅 16:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687158">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
برنامه‌ریزی شستا برای سه وضعیت جنگ، نه جنگ‌نه‌صلح و صلح/ ستاره خلیج‌فارس در مسیر IPO
محمرضا سعیدی، مدیرعامل شستا در
#گفتگو
با خبرفوری:
🔹
شستا برای هر سه وضعیت (جنگ، نه جنگ و نه صلح، و صلح) برنامه‌ریزی دارد و امیدواریم توافق‌ها به نتیجه برسد.
🔹
امیدوارم توافق شود چرا که در سایه آرامش و توافق، کارآفرینی شستا در داخل و ورود به مرزهای بین‌المللی شتاب می‌گیرد.
🔹
سیاست حرکت از بنگاه‌داری به سمت سرمایه‌گذاری، رویکرد اصلی شستا است.
🔹
ستاره خلیج‌فارس در برنامه آی‌پی‌او (IPO) قرار دارد؛ ورود این شرکت به بازار سرمایه، لنگرگاه محکمی برای بازار سرمایه کشور خواهد بود.
گفتگوی کامل را اینجا ببینید و بخوانید
👇
khabarfoori.com/fa/tiny/news-3242509</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/687158" target="_blank">📅 16:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687157">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
سخنگوی ارتش: پاسخ به تجاوز احتمالی اسرائیل سریع‌تر و کوبنده‌تر خواهد بود
🔹
از بین رفتن سامانه‌های پدافند هوایی دشمن در جنگ ۴۰ روزه به‌معنای بازشدن مسیر حرکت موشک‌ها و پهپادهای ما به‌سمت سرزمین‌های اشغالی است.
🔹
اگر رژیم صهیونیستی دست به حمایت یا تجاوزی بزند، حتماً راحت‌تر، سریع‌تر و کوبنده‌تر از گذشته مورد هدف قرار خواهد گرفت و آثار بسیار مخرب و زیان‌باری را متحمل خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/687157" target="_blank">📅 16:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687156">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1caa70bc30.mp4?token=oaXPlzu0kaWD4o-mzEu6imtMYthrHOISqGSedgv5BNWWyOG29YRhOMA1d6-m5_99s60IOO68ijohsSnyCaOhdjh2aJEbeaS8uvyW7y--RCw-1TiwmPANEdQw8HvS7qlFbuedBGCYu-oZsF42CHtfqUTcfj4EIx53dKQT-lFvmZynJ8nvurnWSaJVAIdVn_Fc7JrY9zaH9LTJuqqfXgQCrCs8MoESVnwjRhez1UivtTPZYEfZnKiG4SF4eATH25dNFEth6tPHqbJGfhhSKTVnoog1dVcR9b2-FyoVMH49302jh-szxzAUJzgSrcNyzb90nIzghHaayIGN9rqZN8fESw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1caa70bc30.mp4?token=oaXPlzu0kaWD4o-mzEu6imtMYthrHOISqGSedgv5BNWWyOG29YRhOMA1d6-m5_99s60IOO68ijohsSnyCaOhdjh2aJEbeaS8uvyW7y--RCw-1TiwmPANEdQw8HvS7qlFbuedBGCYu-oZsF42CHtfqUTcfj4EIx53dKQT-lFvmZynJ8nvurnWSaJVAIdVn_Fc7JrY9zaH9LTJuqqfXgQCrCs8MoESVnwjRhez1UivtTPZYEfZnKiG4SF4eATH25dNFEth6tPHqbJGfhhSKTVnoog1dVcR9b2-FyoVMH49302jh-szxzAUJzgSrcNyzb90nIzghHaayIGN9rqZN8fESw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حاوی تصاویر دلخراش| ویدیویی وحشتناک از یک تصادف
!
🔹
هنگام عبور از حاشیه خیابان بسیار دقت کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/687156" target="_blank">📅 16:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687155">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soQOHSB7rLJBkVUml_yqqnXIrzkoBUE_e5gle9LF6xJ6d51FMpA7R6-4HFvMSaZU15Y3qfZtmz7zfj9Va3zZGYr0J888IENkojfd68Fyp9U1Rxcsb6xH91TzsWSg4EtcwSo-rQBsf82BjlSDDcHPxNnRWbdmQQP0ipypNpGJYy5ZEIDBPiaTRpdApe9JRe3hSALm3wTn1t2JYXDTry1qC_XW5qWgP9JZkfbKBAkkPMy2mTnRHLNztPMg3nXsUA6yR3WpoEdxECceyI-KAw9YyfERX3eJDMOpJUyAA9RNsjcc65ED8RXAVXvLRtdsBeVDUzoxeE6cpeSm-JfKwLSNcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
سایت گیزمودو تصویری از آیفون ۱۸ منتشر کرده که از وجود احتمالی دکمه جدیدی روی این گوشی خبر می‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/687155" target="_blank">📅 16:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687154">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
سازمان اداری و استخدامی: ساعت کاری جدید ادارات شنبه ۱۴ شهریور اعلام می‌شود و بانک‌ها نیز از یکشنبه ۱۵ شهریور مطابق دستورالعمل‌های جدید فعالیت خواهند کرد
.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/687154" target="_blank">📅 16:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687153">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/501dc301d9.mp4?token=M5XKBpxcoaOgsZnFA5A1upTyJQ3suQkhF3uEuJcjgQifubHYaNHAlXqn5ACPKBfnVM0NFdAlDDSD50-UP2vUfTRVzHVLEqirauUurSWYWQFFazH4Tov300IgtGsk5ReTUPjvWay8piYI84jFbb67Ue4nYHhq_eA0iQ-2CaMpA3pWyPGRknowveQLUX51yu46ZulToQ2bdVOD1Xp71VhMy70vL7f3bFXzSzV64rr_2d021umtGcPX7zjk4T_qwmeO43VxDim1K9zaokwPkd4YHBR7WLLf9PkA8Z0Luwq3a7awNG-bR8jntF9iib2ncOwq0s_uu-w_Zrj7krAg06Vy0IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/501dc301d9.mp4?token=M5XKBpxcoaOgsZnFA5A1upTyJQ3suQkhF3uEuJcjgQifubHYaNHAlXqn5ACPKBfnVM0NFdAlDDSD50-UP2vUfTRVzHVLEqirauUurSWYWQFFazH4Tov300IgtGsk5ReTUPjvWay8piYI84jFbb67Ue4nYHhq_eA0iQ-2CaMpA3pWyPGRknowveQLUX51yu46ZulToQ2bdVOD1Xp71VhMy70vL7f3bFXzSzV64rr_2d021umtGcPX7zjk4T_qwmeO43VxDim1K9zaokwPkd4YHBR7WLLf9PkA8Z0Luwq3a7awNG-bR8jntF9iib2ncOwq0s_uu-w_Zrj7krAg06Vy0IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شورای عالی امنیت ملی تصمیم گیرنده درباره آغاز و پایان تعطیلی جلسات در صحن مجلس است/ هیچ کدام از نمایندگان از شهادت نمی‌ترسند
سمیه رفیعی، عضو هیئت رییسه مجلس در
#گفتگو
با خبرفوری:
🔹
مجلس تعطیل نیست بلکه فضای فیزیکی آن بر توصیه و مکاتبه شورای عالی امنیت ملی، جلسات در آن محل برگزار نمی‌شود. پایان این ماجرا نیز باید با توصیه شورای عالی امنیت ملی باشد.
🔹
هیچکدام از نماینده‌ها از وضعیت مجلس به این شکل راضی نیستند. نکته در این است که هیچ قوه‌ای نقش جمهوریت مجلس را ندارد و جایگزین کردن آن هم راحت نیست وگرنه کسی از شهادت نمی‌ترسد. امیدوارم شروع برگزاری جلسات مجلس در همان صحن باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/687153" target="_blank">📅 16:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687152">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1daecf089c.mp4?token=G1EBO0aNQ6H2I2TQXZF4I9wFn6LTjldNLthO1C1eouHZuTNc6-88Zcp9voiQxhzALalJ4UoIgH0mwO2yDc6CtLchIcj_DxvXfFHqotIYzMtHqHqrkkgHBg0cAxMeOcDfG8v3i1AoWkBBR_48UZiKTlxfN1tohovnk58XRT5g5UHuO1TgjvvinGZNv4Oe3G-hpU8NQXhF2NBhvalYNGqYaH7eoAaH0NsINJy36WIOoTVdvrjTahzDbQYd4h_HAF-b5zPLtSLYKA_K7deERpgWuhwCdZkbGckiIuYUStZsfiLkPOzJGs98ZWSjNaEDH01GUZPYmnxs7z5wIRcah-izcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1daecf089c.mp4?token=G1EBO0aNQ6H2I2TQXZF4I9wFn6LTjldNLthO1C1eouHZuTNc6-88Zcp9voiQxhzALalJ4UoIgH0mwO2yDc6CtLchIcj_DxvXfFHqotIYzMtHqHqrkkgHBg0cAxMeOcDfG8v3i1AoWkBBR_48UZiKTlxfN1tohovnk58XRT5g5UHuO1TgjvvinGZNv4Oe3G-hpU8NQXhF2NBhvalYNGqYaH7eoAaH0NsINJy36WIOoTVdvrjTahzDbQYd4h_HAF-b5zPLtSLYKA_K7deERpgWuhwCdZkbGckiIuYUStZsfiLkPOzJGs98ZWSjNaEDH01GUZPYmnxs7z5wIRcah-izcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عرب نیوز: حمله پهیادی دقیق ایران به یک واحد در آخرین طبقه یک برج در کویت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/687152" target="_blank">📅 15:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687151">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
البوسعیدی: عمان از تلاش برای توافق درباره تنگه هرمز عقب‌نشینی نمی‌کند
وزیر خارجه عمان:
🔹
یکی از محورهای اصلی دیپلماسی عمان، تلاش برای دستیابی به توافقی بوده که آزادی کشتیرانی در تنگه هرمز را احیا کند و مسقط با وجود پیچیدگی موضوع، از این مسیر عقب نخواهد نشست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/687151" target="_blank">📅 15:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687150">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
هشدار سازمان غذا و دارو درباره ۱۳ محصول غیرمجاز
🔹
سازمان غذا و دارو اسامی ۱۳ محصول بهداشتی و مصرفی فاقد مجوز را اعلام کرد.
🔹
این محصولات شامل کرم حجم‌دهنده باسن و سینه AICHUN BEAUTY، کرم ترک پا زرین الماس، پماد ترک پا، بادی‌میست GALAXY، ادوتوالت TEA ROSE، ادوپرفیوم DELGADO، مایع سفیدکننده فرنود، ریکا سیاه، شیشه‌شور الماس دریا، پاک‌کننده NANO TAK، نمک ماشین ظرفشویی FINISH و پودر زغال فعال هستند.
🔹
سازمان غذا و دارو با هشدار درباره خطرات احتمالی مصرف فرآورده‌های فاقد مجوز، از شهروندان خواست از خرید آن‌ها خودداری و موارد عرضه را گزارش کنند./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/687150" target="_blank">📅 15:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687149">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرمانده پدافند هوایی خاتم: به‌زودی دشمن را غافلگیر می‌کنیم
.
🔹
وزیر بهداشت فرانسه: نداشتن کولر دو برابر جنگ ایران قربانی گرفت.
🔹
۲ ماهیگیر در محدوده سد تاریک رستم‌آباد رودبار غرق شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/687149" target="_blank">📅 15:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687148">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای اتحادیه‌ طلا: ۲۰۰ پرونده شکایت برای فروشندگان طلای آنلاین تشکیل شده است
نادر بذرافشان، رئیس اتحادیه تولیدکنندگان و فروشندگان طلا تهران در
#گفتگو
با خبرفوری:
🔹
اتحادیه‌های طلا در سراسر کشور با فروش طلای آب‌شده از طریق پلتفرم‌های آنلاین مخالف هستند، اما اگر فروش به‌صورت محصولات فیزیکی باشد، موافقیم، زیرا در فروش طلای آب‌شده مشخص نیست آیا معاملات پشتوانه فیزیکی دارد یا خالی‌فروشی صورت می‌گیرد.
🔹
برخی پلتفرم‌های آنلاین ادعا دارند ۱۰ درصد معاملات تحویل فیزیکی دارد و مابقی مشتریان خودشان تحویل نمی‌گیرند، اما اتحادیه این موضوع را نمی‌پذیرد و معتقد است هر معامله طلا باید با تحویل فیزیکی همراه باشد.
🔹
پلیس فتا نیز اعلام کرده حدود ۲۰۰ پرونده شاکی علیه این پلتفرم‌ها تشکیل شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/687148" target="_blank">📅 15:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687147">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ترامپ درحال بررسی اعلام پایان جنگ است؟/ مدیریت پایان جنگ با جمهوری اسلامی است و با تغییر دکترین دفاعی به تهاجمی، شرایط پایان جنگ را ایران تعیین خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/687147" target="_blank">📅 15:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687146">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EliObo81iGpe8Pn7CLnbPw8Tq1io6EkM9CC-iXf7Ux7g99pw_Dqaknjdn7SYcT0sKcYzgqflyCEimv6YwTy2JlWP6jvdUnbjbgfD_6fcJavXdpd6XSDQgJsw5RMKAB4empdsaILGiIvpz6b5oJxjZgQws2S4vs8eu58pNad5_aziErR62B-0FlWuOrjvlo74Z9H8IqtVjmuz2rddmovACj-JINRfpvHI7Jd9RA7xEu26XXL405v-LQj1PLqy7McXe54rXJbcj9ti4gk7nE54QZjW1e3wBQFrJOgz_bJGpzJoKKpItnoHcwvQWBgg9oQJ4qAU0xLGwohtSN1MPSd_bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی ارتش: راهکار مناسب برای آمریکا پرداخت هزینه‌ها و خروج از منطقه است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/687146" target="_blank">📅 15:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687143">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca83f4e683.mp4?token=nwbgCRzN0_CRxQ87qjanL4idHm1admMr9GgipoMoygx-kuXz97PycwOMeZ4oITXR4lH_gF5dGVTu0ZsnK8hWN0ExvLYNNvCGDaZbY9pcEakVvs1wgGKreZLOjeI_iFLkPsCh_rzgg7r7IiULMLTM6X0DDSSDtqshawgZsiRSuXCOmslHCjZrjvmi4Q5iGFHiDVDKdgP1yHHWo8mR0uDa1uiLXYWSfD5BZ5kuq23WUXJJsUqz0yMf38BH2oNT1mCgeljQWrxa-RPvFqJtcX77CsiASmtAaamOwsx19px5ZxvGiFq-4IEv_NWOyo3bcQ0DrePSDEYUSKVkkaR6PDe7uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca83f4e683.mp4?token=nwbgCRzN0_CRxQ87qjanL4idHm1admMr9GgipoMoygx-kuXz97PycwOMeZ4oITXR4lH_gF5dGVTu0ZsnK8hWN0ExvLYNNvCGDaZbY9pcEakVvs1wgGKreZLOjeI_iFLkPsCh_rzgg7r7IiULMLTM6X0DDSSDtqshawgZsiRSuXCOmslHCjZrjvmi4Q5iGFHiDVDKdgP1yHHWo8mR0uDa1uiLXYWSfD5BZ5kuq23WUXJJsUqz0yMf38BH2oNT1mCgeljQWrxa-RPvFqJtcX77CsiASmtAaamOwsx19px5ZxvGiFq-4IEv_NWOyo3bcQ0DrePSDEYUSKVkkaR6PDe7uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی جدید از شرایط تورنتو کانادا بعد از بارش باران و طوفان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/687143" target="_blank">📅 15:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687142">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
دویچه‌وله: آمریکا می‌تواند مواضع مهم ایران را نبود کند اما دانش آن را نه
ادعای دویچه‌وله:
🔹
تهران در حال تعمیر یا تهیه تأسیسات راداری جدید، مواضع ضدهوایی و موشک‌های ضدکشتی است.
🔹
بمب‌های آمریکایی مطمئناً می‌توانند مواضع مهم ایران را با حملات هدفمند نابود کنند. اما دانش و پایه صنعتی فناوری نظامی ایران باقی خواهد ماند.
🔹
بنابراین، بازسازی می‌تواند به تأخیر بیفتد، اما نمی‌توان از آن جلوگیری کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/687142" target="_blank">📅 15:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687141">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5QQ5TmOKYmHQfqp4KphLTnQXOtgYHYV5OpmMC7V0DNnAm0PYsMjkox5hJiF3Kc7-tejS-HLRj5Z34RepignHjGc1RGX82qsHJnrLWh_8lrT4ZzJQtvzpoFIS2vh0OMwkraEymOLlAa5uzpT7TpeK_ZasOICO-a_bxbPRrYAJ713LEOz-AlPfZbg_hSbK3yXlVLAfsBG_4FSrySE78-pM-ZnSXYX7-dmKflRRa0rhmFcq1AR3mLfV5kTF5SUcjuNVXPWzSKUgZ1bF4N5vgkvfqOeGH4Txyd9y5jc3esqYUbLvFbx_k0irUK9Wk-sxjslkjZCfhwusvZHhHNzl_h1yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: مهمات آمریکایی مستقیماً به مراسم عروسی در ایران اصابت کرده است
🔹
تحلیل کارشناسان تسلیحاتی از تصاویر و ویدئوهایی که رویترز صحت آنها را تأیید کرده، نشان می‌دهد انفجاری که روز سه‌شنبه یک مراسم عروسی را در جنوب ایران به خاک و خون کشید احتمالاً ناشی از…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/687141" target="_blank">📅 14:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687139">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Co6RXLXrZHdBpdQ3yf-nHZFS9NtlpKGhCHD1nlv4yhdYwWkV9w6vw7eyQ971nblAsNbBRhDDeWuHGhMF_L52Aa_dfaKHl4C4lQxJgmske6F5BLP4xE4UGf1U0fjqYKahIzAnlRlqu43XF-CaaHMxjbTsEJm1RzsqkV5Jj3lfTYfLgiEzIb2v_2EKZY63yR366WVFJWNPJvuCPIQ2ET6CPdyKiQfnOb3wZL0F-T3wFMnxwYUNQA-oLdefKgv3hxPr_LJvq-5J1rAShOfFh4w8Enqxa-lh5oOuF5ZeT2raSII14sYTucW7rS833PlsbvYbVO2xY5vnAUUOyq-hfH5QIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذخایر گازوئیل نیروگاه‌ها به ۳.۲ میلیارد لیتر رسید
🔹
ذخایر گازوئیل نیروگاه‌های کشور به ۳.۲ میلیارد لیتر رسیده که بالاترین میزان ثبت‌شده برای این مقطع است.
🔹
مصرف روزانه گازوئیل در بخش غیرنیروگاهی حدود ۸۰ میلیون لیتر و در نیروگاه‌ها در نیمه نخست سال حدود ۷ تا ۸ میلیون لیتر است.
@amarfact</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/687139" target="_blank">📅 14:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687138">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
خبرهای خوب معاون عمران وزیر و رییس سازمان شهرداری‌ها و دهیاری‌ های کشور در خصوص توسعه حمل و نقل عمومی
نصرتی:
🔹
با تجمیع منابع مالی حاصل از انتشار اوراق مشارکت، طرح‌های مولدسازی و درآمدهای مستقل شهرداری‌ها، حدود ۳۰ هزار میلیارد تومان(همت) برای خرید چند هزار اتوبوس و چند رام قطار تا پایان سال اختصاص یافته است/ اتوبوس‌های فعال در ناوگان حمل‌ونقل عمومی کشور از ۱۲ هزار دستگاه فعلی به حدود ۱۵ هزار دستگاه تا پایان سال افزایش می‌یابد/ در صورت مساعد بودن شرایط، با احتساب خریدهای انجام شده و تعهد تولیدکنندگان داخلی با همکاری سازمان برنامه و بودجه و وزارتخانه های اقتصاد و دارائی و نفت، تا پایان سال، حداقل هشت تا ده رام قطار برای ناوگان متروی تهران و سایر کلانشهرها در دسترس مردم قرار خواهد گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/687138" target="_blank">📅 14:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687137">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ffb4c5058.mp4?token=Hf0S65fn8YYvfxVhvVeQC7fbhlw378Y27JEJ5ssxNPLaXTQHtyGoihwtPfZVcxx74u1iQLAf9I2GdcwZrLqhoYWIZekQhjO_U7TBRo1Fm_1gHHzHTvc_hxdgz3A-C8cT7J-GksUc4aFj3VKjpcnmUbsMbqXgi6EaO5T9JQHfWQOa0dnRL3e_x_fphyHh60f0JytYjSOTTNGVHsClpsUlrYUPiV_mSD9sDpoRlGENVsNlBvNWzSjwCpPioFWnKmzmnyKLQ19iWWblwZZe0Fv4uPtkJzZ3Z-DUTht-GZsCOCoxyGMT33C-a04iY6ZRMfMXEBxk_UtD0ezWKe-7_2B9o4HMu0P_HKhjExZka_4PgqqtXFJRkt6A0BHYvnoFR7HGK9U9azukEzttUeKQysIlEMy86drPsMbFC3mtcx7S-PJVgVpOIm5NeNMBbZl3qAWwtEvovzdkOXI1MReloI_4JQi64gAo-zeTF6koPuCPFIGmuU1BdG6A0BWmYn64ilgUz_VCka5odaeAx-K4bSXFrQELEfMue7acYgrzHg6GvSU_wBwOTzYKvtrZUBVQWlzHL8NSa06ewvZDRYGE7OR45xNK3uOMkrSKQSOJte9uwSZTlRfXnlegVUmgHQtZUWE-_lN9OzGjScu7L7526IOf-ckvRvt0syqtPSzcrRLS1lM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ffb4c5058.mp4?token=Hf0S65fn8YYvfxVhvVeQC7fbhlw378Y27JEJ5ssxNPLaXTQHtyGoihwtPfZVcxx74u1iQLAf9I2GdcwZrLqhoYWIZekQhjO_U7TBRo1Fm_1gHHzHTvc_hxdgz3A-C8cT7J-GksUc4aFj3VKjpcnmUbsMbqXgi6EaO5T9JQHfWQOa0dnRL3e_x_fphyHh60f0JytYjSOTTNGVHsClpsUlrYUPiV_mSD9sDpoRlGENVsNlBvNWzSjwCpPioFWnKmzmnyKLQ19iWWblwZZe0Fv4uPtkJzZ3Z-DUTht-GZsCOCoxyGMT33C-a04iY6ZRMfMXEBxk_UtD0ezWKe-7_2B9o4HMu0P_HKhjExZka_4PgqqtXFJRkt6A0BHYvnoFR7HGK9U9azukEzttUeKQysIlEMy86drPsMbFC3mtcx7S-PJVgVpOIm5NeNMBbZl3qAWwtEvovzdkOXI1MReloI_4JQi64gAo-zeTF6koPuCPFIGmuU1BdG6A0BWmYn64ilgUz_VCka5odaeAx-K4bSXFrQELEfMue7acYgrzHg6GvSU_wBwOTzYKvtrZUBVQWlzHL8NSa06ewvZDRYGE7OR45xNK3uOMkrSKQSOJte9uwSZTlRfXnlegVUmgHQtZUWE-_lN9OzGjScu7L7526IOf-ckvRvt0syqtPSzcrRLS1lM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری نماینده مجلس از لابی‌های میلیون دلاری و خطرناک در مدیریت پسماند/  مدیریت پسماند زباله‌های صنعتی تنها در اختیار دو شرکت است که با ارکان دولت ارتباط دارند
سمیه رفیعی، عضو هیئت رییسه مجلس در
#گفتگو
با خبرفوری:
🔹
خیلی برای من عجیب است برخی موارد مانند خودرو یا موضوعات اقتصادی دیگر لابی‌هایش مشخص است.
🔹
در موضوعاتی مانند پسماند که لزوما تمام تصمیم گیران نسبت به آن حسی ندارند و اصلا نمی‌دانند این موضوع می‌تواند اولویت چندم باشد. باید تازه تشریح کنید که موضوع چیست و با این کلونی ارتباط می‌گیرند و از منظر تامین منافع خودشان موضوع را در نظر میگیرند؛ این (اعمال نفوذها) بیشمار مصداق دارد.
🔹
مشکل قانون قبلی پسماند این بود که ضمانت اجرایی و جرم‌انگاری دقیق نداشت. زباله‌های صنعتی باید بی‌خطرسازی شود؛ شاید در طول تمام این سال‌ها شرکت‌هایی که این زباله‌ها را برای مدیریت می‌بردند فقط دو شرکت بوده است؛ شرکت‌هایی که مرتبط با برخی از ارکان دولت بوده اند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/687137" target="_blank">📅 14:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687136">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0L_-5--2xowTT6SY3qbqidzCJNtURM-XldwK2mSBVMM1husgDpLCpRYlEko4UySxdbmDxGElICxmldsC0VxpqaDRtmRAc_gfnnZyrw6oUyywh_Not_IZOWN0_a3TTCZuo3lowJgvjS4uA7eHBIvuDTCc3Zuh2oRAjJsnUS4sF8IInYROPa7EpQ4yBbNnw0Z2cRMQyQ7BN4F0rQAgOj8AFNqvVJleSyMhBDts5qyOY8jz4FJrieqVq1h4mTMiIRNFFIX8DAY9jjLUGnjYLfZ-pmhM9xAXuXvb2AqVbJb1nMVKZAXIib_OeYA7VDon-mETP7TQg-1Rqn_G0CgzASWpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یک مرزبان در درگیری با گروهک ضدانقلاب
فرمانده مرزبانی کرمانشاه:
🔹
گروهبان‌یکم مرزبانی «رضا دارایی عمارتی» در جریان درگیری بامداد امروز مرزبانان هنگ مرزی پاوه با گروهک معاند و ضدانقلاب به‌شهادت رسید.
#اخبار_کرمانشاه
در فضای مجازی
👇
@akhbare_kermanshah</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/687136" target="_blank">📅 14:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687135">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmBChZcWxzAvyEvljfij_TD0F6SwCaU-5zU8wyrK3nTCw6bbtIBTvUx6DiE9feDaYKGjnkhD98iNMG6n8D-Yw8nCg5o5wVngjWrUm_ZC_bZKtT9ihAs_gcyKsTRF1WniuwHk-2hGmiG4EAImtBTX66K2W8nRd6U-GZ_zUuuCgcnx91rVA8c9NrT2cO5PgUipRpoadOO3haIM04EMuecjjnKaFN82VPHf42TTY8dOG9Tidl3OEzms9J7E12OPOoPpKoQGiRYXif8im3zfxv1UMzoEgJQleOSWOZ4ZLx0HiaCuntZZ6cNesr6otB1eWssTef_eVbGFfOwaoRFmHkAqiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا برای دریافت اطلاعات از یک سردار ایرانی جایزه ١٠ میلیون دلاری تعیین کرد
وزارت خارجه آمریکا:
🔹
تا سقف ۱۰ میلیون دلار جایزه به افرادی پرداخت خواهد شد که اطلاعاتی ارائه دهند که به شناسایی یا تعیین موقعیت مکانی سردار امیر یاریاب، فرمانده عملیات سایبری فرماندهی سایبری سپاه پاسداران، کمک کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/687135" target="_blank">📅 14:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687134">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
آمریکا تقریباً به اندازه بودجه پنتاگون روی هوش مصنوعی سرمایه‌گذاری می‌کند!
🔹
سرمایه‌گذاری آمریکا روی هوش مصنوعی حالا به ابعادی رسیده که می‌تواند کل اقتصاد این کشور را تحت تأثیر قرار دهد.
🔹
برآوردهای دانشگاه کلمبیا نشان می‌دهد پنج غول فناوری یعنی آمازون، آلفابت، متا، مایکروسافت و اوراکل، ممکن است سال آینده بیش از ۱ تریلیون دلار برای زیرساخت و توسعه هوش مصنوعی هزینه کنند. رقمی که تقریباً به بودجه پیشنهادی ۱.۵ تریلیون دلاری پنتاگون نزدیک است!/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/687134" target="_blank">📅 14:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687133">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Plj9vaEVMeaNZT0PiOeMdRaegFgXHOL_SDRjudGxFfy8RahTt46CSRqEugrg_wS3Cg42B_2-a6pgCf1eSsFIkn7N2W0QEu3InPeQLry2AdmHfUj3a8fTvy6yMeA9Zoxyz_bno0ln6QIG_HoJ7bsbdv_dDRt9t-TAxW5wee94-C-zDENQA935bcfqGz7zwPqkWYxAJuAo7ztF9E2Dphxbf4PWzM-TLePEVOuJr2Xijgf3yrehvOiAzmxEXlWK4y6zliTBpsunRvX-XP_KaWm6Kpw3P8vQg-n83cgwSJ3-Mj-pOLdV3pyOV6UFchsaeE_LmQ_VBo5pn4eYDlHIzBZ2-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شتاب چادرملو در توسعه معادن جدید/ هدف‌گذاری برداشت ۵ میلیون تن سنگ‌آهن تا پایان سال
فرید دهقانی مدیرعامل شرکت معدنی و صنعتی چادرملو به خبرگزاری تسنیم گفت:
🔹
چادرملو در پنج ماه نخست امسال ۱،۵ میلیون تن سنگ‌آهن از معدنD19 برداشت کرده است. حجم باطله‌برداری از این معدن در همین مدت به بالغ بر ۱۵،۵ میلیون تن رسیده است.
🔹
در پنج‌ماهه نخست امسال، یک میلیون و ۶۵۰ هزار تن سنگ‌آهن از آنومالی ۱۰ استخراج شد؛ این در حالی است که میزان استخراج در مدت مشابه سال گذشته، ۱۲۰ هزار تن بوده است.
🔹
برداشت سنگ‌آهن از معدن چاه‌گز به‌دلیل حجم باطله‌برداری هنوز آغاز نشده ولیکن برنامه‌ریزی شده تا پایان امسال از مجموع سه معدن یادشده ۵ میلیون تن سنگ آهن برداشت شود.
🔹
همچنین در کنار تأمین، برداشت و خرید سنگ‌آهن، توسعه فعالیت‌های اکتشافی و شناسایی فرصت‌های جدید معدنی به‌ویژه در شعاع ۲۰۰ کیلومتری مجتمع معدنی چادرملو، با جدیت دنبال می‌شود.
🔹
مشارکت در محدوده اکتشافی زمان‌آباد و پیگیری فعالیت‌های اکتشافی در محدوده‌های بایچه‌باغ و کال‌کافی  از جمله برنامه‌های شرکت است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/687133" target="_blank">📅 14:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687131">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c52S0-J1ErU9725-6z8PHy2jDUDFkqwgYwGplihS4LT3v5ecGJO2r2mn5r6vGchBtemtJkYaMt9LZuZKCes9ZHYMSWurkrJ37hgzd1hyr4wlHhwNXz2tecxmE59w_QIlvDfr2G3H0Z8Jk5FeVxlG01IHLjTSqcgjI7opLQ1SMVcs1x6r-EoXgJhN06jRVvzLHcqzleTjmKAzrFj1KjVfkd2yoR0SV8UFTJ9sngv6Sdu4SX2Nt5Cur5j2w0Q1eCwollAzizm8FOQsIsntkBw5pJWyR9Y4vtekpgjJBmLdGi7ST1oHcQaka8sTbxXeiotYouwOnHbqQaUit1fy3VqljA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طبیعت چشم‌نواز حاشیه رود ارس
🇮🇷
#ایران_زیبا
#اخبار_اردبیل
در فضای مجازی
👇
@akhbarardebill</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/687131" target="_blank">📅 13:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687130">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یک تخصص ویژه ایران که آمریکا را کلافه کرده است
@Tv_Fori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/687130" target="_blank">📅 13:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687129">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر نفت: بیش از ۵۵۰ اصابت به جزیره خارک داشتیم.
🔹
۵۰ کیلو مخدر شیشه در آذربایجان‌غربی از یک خودرو کشف شد.
🔹
ویتکاف و کوشنر به مسکو و کی‌یف می‌روند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/687129" target="_blank">📅 13:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687126">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kv0NyOcuvWKC5Z_NB6lxdyKBD7Ho5nnNa--Upe1ikAiudWozS06rCdJY96df9Qxkq4c07UhsOKaJQzXK8j9a41k8hdhByS6WvKM12gjYHgLmE42Gcf3xJ-EuCAuPzoF7sL3gWiYjT-eBJbeCWWSG4as3fMFznMqOhbCXVx2IMYvDVGSlXmwTq-lZbMVZLGNA7iar9V-S0xaERstsYg3QbolTd46rf5wK1mbW6c8TGbHkOBjl2DAxuGSzWII68R_pioWb_XoW4hgbvjiuhNesK9dZmdFaI6xORozCmnjqib_z4lSBpwK6B-NMCPZfi1Mh04p_q8BhCzmn2mUrb_O2Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rIECXDwKyN5XQCbCPWxsujM-pfk7HI4p_cuqEUzJxWpunkloqG19STvWMptbcZaKjiZCXGW_7kHejcJE16tVY2EfKSZeCdeJPYqQz4ywT7deAFW6nwsiHQQKBxM7L_5YjvjTuJlkKKhYWurK1GZtTlRX4JKKAP0Czy4_boo8FuaPDJVwBP6gFu1ZgbNKi9hYNp75FNSf_ZGTJ0cX4bTRo5hOp2fFrBfqQ1M7wy3Z4rwCqXEkhGlIB3zNgfTBA0di48zTB06Wt8mPrkt0nmbI7gMCxqxR0vr32ROUmJnX9gys-wQnO8Hc8EVWigWmEA8qlq-ItNutEmoF3kuLhwAUvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UAq8FGbTUahtud22wvH5XR7BmIDO0mQ6h8RP2kvpsZTYXFJex6yFLvM1DArpTC0RsaS4R4db8b0b2HYDHjv3taadj5V02D0sqhwxDKtK_ghJj5jf7wasLD1BkywAHw8mJ3cFhK37B9fsyLmvGActiZX418WfXYsSBPnBSSyadr3DzZ7FSmvx1WH_e1RMAZrVl89CapNbgVMa68bvsqd16vW_bBYT9VSPnRj_fvTMFpSI_KRDQyegV3MKTxGWsDnfUyHvGVucFmFXY_JWM7w6wnKQ-FaEfR4Yl_MErvoU_hb3xQfPcR1PELHcsoVfqM_LFsehvl7SACc9bL61noR1uA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
در اعتراض به قانون ممنوعیت حجاب دختران در مدارس اتریش، زنان و مردان با حجاب در اعتراضات حاضر شدند
🔹
موج اعتراض‌ها روزبه‌روز گسترده‌تر می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/687126" target="_blank">📅 13:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687125">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
حسن روحانی: صداوسـیما باید ملی شود؛ از رئیس‌جمهور تا مردم نمی‌خواهند این صـداوسیما را ببینند
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/687125" target="_blank">📅 13:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687122">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a812884e.mp4?token=pYOCd5_uiFR09gdtb9iqMARB-QveAQdbyzTPXnRCUB-xbMBjbw4KgF7JMig5diXTAkw0tknO049ZAWIpdCZ7M5twEgL7U_I684R8T1NYu3_728MbbAgc1x26py-MBWZd43six7bzvrp6I-ZcKHAOObb336OxYHXVn8Ti_IlAEbIizbNeig-fRPjpU68pzxWty2kbLID9Uh5aDjOZl0BMZJ9mAksHoPv6zCtQxO5zeQRW7RV_2JnZisVEq_ATAYW3xjdyNh4fxi7tYFM3s_34JXXyIdWTqNTGaUQOqG5DTdwTb3hgSU_mxoSqOPhrX7VRH0OoLP3ROcu0YJd29XmMwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a812884e.mp4?token=pYOCd5_uiFR09gdtb9iqMARB-QveAQdbyzTPXnRCUB-xbMBjbw4KgF7JMig5diXTAkw0tknO049ZAWIpdCZ7M5twEgL7U_I684R8T1NYu3_728MbbAgc1x26py-MBWZd43six7bzvrp6I-ZcKHAOObb336OxYHXVn8Ti_IlAEbIizbNeig-fRPjpU68pzxWty2kbLID9Uh5aDjOZl0BMZJ9mAksHoPv6zCtQxO5zeQRW7RV_2JnZisVEq_ATAYW3xjdyNh4fxi7tYFM3s_34JXXyIdWTqNTGaUQOqG5DTdwTb3hgSU_mxoSqOPhrX7VRH0OoLP3ROcu0YJd29XmMwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رخ عمودی شگفت‌انگیز K2
🔹
قله K2 با ارتفاع ۸۶۱۱ متر در رشته‌کوه قراقروم، دومین قله بلند جهان پس از اورست است و به‌دلیل مسیرهای بسیار دشوارش شهرت دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/687122" target="_blank">📅 12:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687121">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
طلا دوباره آماده جهش می‌شود؟
🔹
تصمیم جدید خزانه‌داری آمریکا برای دو برابر کردن بازخرید اوراق بدهی بلندمدت، موج تازه‌ای از توجه را به بازار طلا آورده است.
🔹
شورای جهانی طلا می‌گوید این اقدام دقیقاً «چاپ پول» یا QE نیست، اما می‌تواند دلار را تحت فشار قرار دهد و نرخ بهره واقعی را پایین بیاورد، دو عاملی که معمولاً به نفع طلا هستند.
🔹
از طرف دیگر، رشد سنگین بدهی آمریکا و نگرانی درباره وضعیت اقتصاد جهانی باعث شده سرمایه‌گذاران دوباره به طلا به‌عنوان پناهگاه امن نگاه کنند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/687121" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687119">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15209ee1b.mp4?token=GHV8pLiFm35kVGadv6tq_WbyZ3JiBRAGfmXKgSyTt99v0zdx_jManpviO6Zhe0EqOuAC8M9sfuV0aokjK4uHjEKYxFb95twRP_OVgXjUAaH0iShk4Hu9cxn7ixkoFX0WskZQ5E206tmzRM0_XGLrkP6ycgWxNTfJs7hJo5Bt2g0D_r6XHax63e8Ps7TiUJ_iPAMPv22FPp7UKSZZ2eHC923CCUH5lfakgJZRSxhwrjVaDyJKDyo6i3E7orRBSlmU9sjXyjUg55tV-15RgMtRWP8ZDqa4np8oNgXeRgffimEiCUiuUmOBYyaHEdHg4t9yG4p6-P8rKdhC77lT0JcXww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15209ee1b.mp4?token=GHV8pLiFm35kVGadv6tq_WbyZ3JiBRAGfmXKgSyTt99v0zdx_jManpviO6Zhe0EqOuAC8M9sfuV0aokjK4uHjEKYxFb95twRP_OVgXjUAaH0iShk4Hu9cxn7ixkoFX0WskZQ5E206tmzRM0_XGLrkP6ycgWxNTfJs7hJo5Bt2g0D_r6XHax63e8Ps7TiUJ_iPAMPv22FPp7UKSZZ2eHC923CCUH5lfakgJZRSxhwrjVaDyJKDyo6i3E7orRBSlmU9sjXyjUg55tV-15RgMtRWP8ZDqa4np8oNgXeRgffimEiCUiuUmOBYyaHEdHg4t9yG4p6-P8rKdhC77lT0JcXww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تسلا تاکسی‌های خودران Cybercab را در بخش‌هایی از آستین تگزاس راه‌اندازی کرد؛ این خودروهای دونفره فاقد فرمان و پدال هستند
🚕
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/687119" target="_blank">📅 12:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687118">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرمانده پدافند ارتش: فناوری پیشرفته دشمن، تضمین‌کننده بازگشت هواپیماهایش نیست.
🔹
کره جنوبی: تصمیمی برای اعزام نیرو به هرمز گرفته نشده است.
🔹
گرمای بی‌سابقه در فرانسه جان ۷ هزار نفر را گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/687118" target="_blank">📅 12:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687116">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb3a7636f1.mp4?token=livCp3YvaZzojdRH67ZnWp59W464kDs-0UpGAcedFubLmEphPdBZgatP3orjNu85LSuLuU3Z0hZDOyvYWwVS67JRHGEXWHEtuJuv3KO7RCi2LmPbwyVDZ_sHm8CoCu5yTcwBSBOBRPcV9VK1uEVmJMr3G8MIFniy_2-JlpHoP-Oj5zCFcQ9HUOteHBPQZvrvplXw126dnj5eOEHIV1h5QSw39xyaZDj-2oPcAYQhna4Ylm3kQiDeN9UqnFUoinfO5cAG0N1mCEEtLCetNvCpap9OR8-B7Xgaa7eadcnadkSpIjRmclbQke8W-Y-CjPzadGIrQC9nU1SYZirXttbDDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb3a7636f1.mp4?token=livCp3YvaZzojdRH67ZnWp59W464kDs-0UpGAcedFubLmEphPdBZgatP3orjNu85LSuLuU3Z0hZDOyvYWwVS67JRHGEXWHEtuJuv3KO7RCi2LmPbwyVDZ_sHm8CoCu5yTcwBSBOBRPcV9VK1uEVmJMr3G8MIFniy_2-JlpHoP-Oj5zCFcQ9HUOteHBPQZvrvplXw126dnj5eOEHIV1h5QSw39xyaZDj-2oPcAYQhna4Ylm3kQiDeN9UqnFUoinfO5cAG0N1mCEEtLCetNvCpap9OR8-B7Xgaa7eadcnadkSpIjRmclbQke8W-Y-CjPzadGIrQC9nU1SYZirXttbDDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودروسازی که از دوطرف می‌خواهد از مردم سود بگیرد/ آیین نامه دولت را که حق مردم در آن دیده نشد بود از دستور کار خارج کردیم
سمیه رفیعی، عضو هیئت رییسه مجلس در
#گفتگو
با خبرفوری:
🔹
بودجه‌ای در کشور بابت یک قانونی (در خصوص خودرو) وجود دارد دولت باید مشخصاً آن بودجه را به مردم بدهد؛ نه به خودروسازی که از دوطرف میخواهد از مردم سود بگیرد.
🔹
نظر ما در مجلس با قاطعیت این است که این پول و بودجه که از منابع بیت المال است باید به آحاد مردم برسد.
🔹
همین که توانستیم یکی از آیین نامه‌های دولت را از دستور کار خارج کنیم که در آن اصلا حق مردم دیده نشده بود، و الان آیین نامه جدید را که ببینید یعنی زور ما رسیده است؛ البته این کار تقریبا به انتها رسیده و هنوز ده تا پانزده درصد دیگر وجود دارد که باید کار آن انجام شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/687116" target="_blank">📅 12:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687115">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f56b44f1.mp4?token=sXdPCVVbBVMqAOSxyiVt0IA8YyBRZjT3EHRSHT-Dn6NhE83Xu-W9wwVw8kfruHOmLHeOPS5pBS82XZWhLVzxYFp0JRrCdN-P0zsButxtc36Wt9cQm7-BrWlf_HuC0mSvuQCGvLbh1Y7TVUkXrwS_xKlrRWVYB9GndK_vyNtT-i_ov_nQ9kXEldxiq_InFh6dT0kmgMeJR6vJu-DfXN62hEgQxP-zmvBd-_KG7t35ItidpYbqM6yszdee1C0MAZn1zCfCF1LtsHLgFLJn7ZLYH_avVHzTpRwlnACLZOyr7_eoxd1g-omITQQMIvFExmSRVUfJ6mT46T7goKq0d4SjhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f56b44f1.mp4?token=sXdPCVVbBVMqAOSxyiVt0IA8YyBRZjT3EHRSHT-Dn6NhE83Xu-W9wwVw8kfruHOmLHeOPS5pBS82XZWhLVzxYFp0JRrCdN-P0zsButxtc36Wt9cQm7-BrWlf_HuC0mSvuQCGvLbh1Y7TVUkXrwS_xKlrRWVYB9GndK_vyNtT-i_ov_nQ9kXEldxiq_InFh6dT0kmgMeJR6vJu-DfXN62hEgQxP-zmvBd-_KG7t35ItidpYbqM6yszdee1C0MAZn1zCfCF1LtsHLgFLJn7ZLYH_avVHzTpRwlnACLZOyr7_eoxd1g-omITQQMIvFExmSRVUfJ6mT46T7goKq0d4SjhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سونی ربات میکروجراح خود را با دوختن سطح یک دانه ذرت آزمایش کرد
😳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/687115" target="_blank">📅 12:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687113">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
تلاش عمان و قطر برای آغاز چارچوب جدید مذاکرات ایران و امریکا
🔹
فایننشال‌تایمز از تلاش میانجیگران عمانی و قطری برای تدوین چارچوبی جدید برای مذاکرات میان ایران و امریکا با هدف مدیریت بحران میان دو کشور خبر داد./ مهر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/687113" target="_blank">📅 11:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687112">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d791cc65d.mp4?token=oINMObo3u_j06S8bN1xQ4bQeCllDd2LlmgALxnmL008USvqpxClS8l_DkXffBfwM8d9npAIskduqDwEcbjKkl3IzluShtV6VTUsh-jOlJoc43jl_7SNbc3EIe5-gg7r68lboNH7-jH87vGIc5SW8nCToZcRpP8-TEVN-NGtqhsIGLMqdWvT3Dm0Pc5hDIlzakYYcL66LCanovToQ549Tk64OAHUEDYy25WQ1P7gK6DI2ui_36_E8lnkuj1SP8_GpLLI1xM15WMldUPxdOmwGOmZZFuw1FA9TJngSXTldtkpyBi5y0JJwYTuCo65FnPZnB8hw4L28WBTMoQUUymdqAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d791cc65d.mp4?token=oINMObo3u_j06S8bN1xQ4bQeCllDd2LlmgALxnmL008USvqpxClS8l_DkXffBfwM8d9npAIskduqDwEcbjKkl3IzluShtV6VTUsh-jOlJoc43jl_7SNbc3EIe5-gg7r68lboNH7-jH87vGIc5SW8nCToZcRpP8-TEVN-NGtqhsIGLMqdWvT3Dm0Pc5hDIlzakYYcL66LCanovToQ549Tk64OAHUEDYy25WQ1P7gK6DI2ui_36_E8lnkuj1SP8_GpLLI1xM15WMldUPxdOmwGOmZZFuw1FA9TJngSXTldtkpyBi5y0JJwYTuCo65FnPZnB8hw4L28WBTMoQUUymdqAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر جدید لحظه وقوع سیل در نپال
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/687112" target="_blank">📅 11:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687111">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مدیر عامل پالایشگاه تهران از راه‌اندازی واحد CCR که تولید بنزین کشور را روزانه ۱.۵ میلیون لیتر افزایش می‌دهد خبر داد.
🔹
صندوق بین‌المللی پول: اقتصاد امارات وارد مرحله خطر و کسری تجاری شده است.
🔹
فقط ۴ نفتکش از تنگه هرمز در روز پنج‌شنبه عبور کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/687111" target="_blank">📅 11:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687110">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
افزایش شمار نظامیان آمریکایی زخمی در جنگ ایران به ۷۶۷ نفر
ای‌بی‌سی نیوز:
🔹
بر اساس به‌روزرسانی ‌های انجام شده از سوی وزارت جنگ آمریکا (پنتاگون) که طی ۲۴ ساعت گذشته انجام شده، شمار نیروهای آمریکایی زخمی‌شده در جنگ با ایران به ۷۶۷ نفر افزایش یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/687110" target="_blank">📅 11:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687107">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LuOczDEQGQmIKNNHvWnHVNH9UQngSwG-SZAoMOtlccAA4TyotT-0aezyc_y7uNi99SQHVXUPaoUIzKRIPbpBqNCDYsbWBRZjrI8t8Qd3kLSA5T2iYqGXA2WZzXiqW01YVVGvjeScQPD8LHV55acT44O9tpyszo_rWUjRv-ZIDxhEBrWL7rOQika5cI7QAkhCjXAfvS3HWxZtIrHrLf54D6PzW5DJrElQP6cqyQNYGoqx58dejmp4_sDRImCrPEjFi43BCQtsCPAhrnN-iQk4fzYJru-6IM_Ec9bJeEav5ZYfb-_PIjhW5_UWNQHK_6YZaIvTs74ZypLSf4MC7Dp2_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hmue9yMlsVdHQD9NeaW0oBvPnwmPnAFeqkYOgCj9JsxXm_UdEA80X3A4wphbPNnraSdnYc8ACGfsx-mGRyWo1FF7YnyRQsCqjfp5i_0BY55zN5jotkK55G-kiL2iP4siKNqWSfM0-Vk4Iqdb8GIyoZkt_W1OymPaAR_LwtPysidQDhhT4cwAIYhN_uG6gsycvVntTCRBQLY37TXo1F3-yqp4bawoXgn5tBu-VnTPNnh9VA-ehRXgUIArvQcWxq5JXYp1qs9G0loEStIdwrIMztbEQvDc751m0IqJ0au-omqafu1WeDu-jhG1OyzeITlZAMk-r1Ojh2ddrRId4fm9wA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ced1356087.mp4?token=kNkZmax53dvHriw1DEydK6JeRUnA5yxH_8KRjn97EA4LCucwF05opdh2Gme8TJOCKA8KBxl047ULKJkwFsN5ZV18tPEud9yS5r7CpvmInFoVuEH0vNDDD5MfjO4MVMlDJiMtsuGayzKlEdkCryaDcaUC6vd02VGGT84a15zoPwO7PyAWu7P_zySLImYdZNubq-Shuqc1-UGpkBdifKdm6pz0CoTnLK66GhW5uKwk1ns6qUlxSAFSvt0uqTb8KrROhYGlfQx6AVkHx8L-kxuv3OR737xymIoEDEo25U_4Bq08z3Qy58ln_nOtkMAEzk40VA02WQUONjbV-N5sMDBJ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ced1356087.mp4?token=kNkZmax53dvHriw1DEydK6JeRUnA5yxH_8KRjn97EA4LCucwF05opdh2Gme8TJOCKA8KBxl047ULKJkwFsN5ZV18tPEud9yS5r7CpvmInFoVuEH0vNDDD5MfjO4MVMlDJiMtsuGayzKlEdkCryaDcaUC6vd02VGGT84a15zoPwO7PyAWu7P_zySLImYdZNubq-Shuqc1-UGpkBdifKdm6pz0CoTnLK66GhW5uKwk1ns6qUlxSAFSvt0uqTb8KrROhYGlfQx6AVkHx8L-kxuv3OR737xymIoEDEo25U_4Bq08z3Qy58ln_nOtkMAEzk40VA02WQUONjbV-N5sMDBJ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حادثه عجیب برای هواپیمای مسافربری ایندیگو در فرودگاه سرینگر
🔹
هواپیمایی هنگام پارک با تیرک سامانه هدایت برخورد کرد و آسیب دید، اما همه مسافران و خدمه سالم ماندند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/687107" target="_blank">📅 11:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687106">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLca6cxZyA8EcHyMPhpjU31xnV9a6-9FWuboSMnarLXde3JxB8-zuuqbhijmY_Gm7TEKnoztFuSMoSnjxQVTlRUgRfutRdlC-ImCs5REOKfkqbU5wj94hLSdDUKytzRoXCqdMZOfkyNezlFWd47S_D9ulR-MyEfD_Im1xhJtEBQF-p_pt_IB0WxpDfhiY_EvZKUY4yScvUie2zBcqg9hfFAiT_oWfnYKtKJ71YWeU9h-4YtNTADG-31-YnXNOidPQ7YYz_whzx3YW11ji3oCRrwC80bCDSboPZCNjmtL9OlaxUzYfZwCffF6CEEscdnwPwJmV3y0t07_r2LAy27DwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش وزیر امور خارجه کشورمان به اظهارات اخیر همتای اردنی؛ ایران برای پاسخ به متجاوز چقدر باید منتظر باشد؟!
🔹
به نظر وزیر امور خارجه اردن ایران چه مدت باید منتظر بماند تا به متجاوزی که نه به حاکمیت کشورهای عربی احترام می‌گذارد و نه به حاکمیت ایران پاسخ دهد؟
🔹
آیا او واقعاً از این موضوع بی‌اطلاع است که در نخستین حملات آمریکا، از حریم هوایی، خاک و آبی کشورهای عربی استفاده شد؛ حملاتی که به کشته شدن ایرانیان بی‌گناه انجامید؟
🔹
ادعای وزیر خارجه اردن: حمله ایرانی‌ها واکنشی نبود، چون دو ساعت بعد از آغاز جنگ حمله کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/687106" target="_blank">📅 11:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687105">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15ca2b9ae4.mp4?token=j_g9-w1_MXyXJdgpRIgP7lZaWfmQg4hdWiPPAqOf6gfjL_mKjFNXMcIgbHb9lEs62JLTjvLA2_ogranIrBsJ1cXAOIvIEGoX0sNFzYrKD1eLppQsKXmTFipQtFE5Z590Gv9wK4K4yns1BgNjNY7YmBdWiSQGdzDsKtNL8YoOH-jC04xKpDyHtV-QECeMV9ac2Fx0jwSPOkPZgnoa2KUKRzb0iMOv07rSEvlOS__mroSQ0BLc6GQaDjIOzmST-bqLHTUeP2qkqOGEUCilxizr1NMlH1Afn1LjlcCMxB46IVRgMXh-FUN-Ic5SIKYydu7kEHQn_FcIZUKnH7w_h8oYQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15ca2b9ae4.mp4?token=j_g9-w1_MXyXJdgpRIgP7lZaWfmQg4hdWiPPAqOf6gfjL_mKjFNXMcIgbHb9lEs62JLTjvLA2_ogranIrBsJ1cXAOIvIEGoX0sNFzYrKD1eLppQsKXmTFipQtFE5Z590Gv9wK4K4yns1BgNjNY7YmBdWiSQGdzDsKtNL8YoOH-jC04xKpDyHtV-QECeMV9ac2Fx0jwSPOkPZgnoa2KUKRzb0iMOv07rSEvlOS__mroSQ0BLc6GQaDjIOzmST-bqLHTUeP2qkqOGEUCilxizr1NMlH1Afn1LjlcCMxB46IVRgMXh-FUN-Ic5SIKYydu7kEHQn_FcIZUKnH7w_h8oYQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقابله با عریان سازی نگرانی زنان با پوشش‌های متفاوت است؛ نه صرفا زنان محجبه
سمیه رفیعی، عضو هیئت رییسه مجلس در
#گفتگو
با خبرفوری:
🔹
یکی از مطالبات مهم زنان این روزها بحث به سامان شدن اقتصاد خانواده‌ها است.‌
🔹
همچنین مقابله با عریان سازی‌ است که دارد اتفاق می‌افتد؛ جالب اینجاست که خانم‌ها با پوشش‌های متفاوت این اظهار نگرانی را داشتند. نگرانی در این راستا صرفا مختص زنان محجبه نیست.
@Tv_Fori</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/687105" target="_blank">📅 11:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687104">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a98fd41f19.mp4?token=ID5eJyYU7ykeyFZJYeFN0TV9bupp_igNWyXL6jBPqhCCuUjraXdzOgaSTC7b3NJyKt_Qu4lumGpROJphpucVdFIh88-vo3uQw6PahjV93hzDuU91CDomVukeA0hJT8w-F9KB1AYZHBnvHzZZuThiFYeLIVXBcDQKrh9nLj3pfKLcctbrMS9JFFHvrCLchAzRz_67w-OdmSmJpOpFK-ntbiyfdCX-_1ntfBCOqvrWwQLWzN3g8ZWQ7XITIRYQMc_N5VVN7CXC2SJfuSh6Mf70lb74xC2n4R5XxPDc5tRgH2I6qqUChlx8dpLCo5GFn3o2iyhmVtJ2O8FZ1-hdO78AQClSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a98fd41f19.mp4?token=ID5eJyYU7ykeyFZJYeFN0TV9bupp_igNWyXL6jBPqhCCuUjraXdzOgaSTC7b3NJyKt_Qu4lumGpROJphpucVdFIh88-vo3uQw6PahjV93hzDuU91CDomVukeA0hJT8w-F9KB1AYZHBnvHzZZuThiFYeLIVXBcDQKrh9nLj3pfKLcctbrMS9JFFHvrCLchAzRz_67w-OdmSmJpOpFK-ntbiyfdCX-_1ntfBCOqvrWwQLWzN3g8ZWQ7XITIRYQMc_N5VVN7CXC2SJfuSh6Mf70lb74xC2n4R5XxPDc5tRgH2I6qqUChlx8dpLCo5GFn3o2iyhmVtJ2O8FZ1-hdO78AQClSb-5XafBgReHqfHyBKfeYI5QbHWo3HW_ebK16Zg5PI6ZlPZNBtueQHRtcoEjVWluY_SM0IHmuIhJEz9lKLk_z4BpMkfV0hGQpNyFtZZ5v4oOOz6JjVoF2T2RjIyrj9crX9Q8AVCZlTdIqNah60COUJh25AhQIMeSE1pWZQHxlKGw2tUuOSc6e438LT4dSUzC6ktSGMeTc85YwBRkTBP3PvHufrlkVQsTQppEdS-X3cG-rEXYiy62eirBy3FMsJ-PWk6AoNf8MRNziO_fqzLhaaoGn8pLVctv6QZdToSxhn0pfh0j0x2xN_V42pah-Qkl-SVNVGLHMJ1RJmr08dQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد وحشتناک قطار با کامیون در لهستان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/687104" target="_blank">📅 10:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687103">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d72545c257.mp4?token=LYtBv2ydOb1aatu91SXmupseUMx6iJZDzYR6kK_oJwp3rgJIlPaTpVJk71PlQVgJUcy9W5tEOMVGYlKquKit9RgLbWW3exoURg3zuNdYCbQs8tD0uxX-CrdmKUUEvVbvjQBXYQsU577OuPVV8K6uu3Bcu2xdfuvjjweLsz1jiXZ47_vMkscC9JCLkKVfPubGilLnBjK1BvgXzCf_wIHxq7juoSK0Hzg_LEiBB1BNnk0h82ZRAmHUdD6wR3LyxYawevRehtkeDiCD1D86ufz5yGBHI0S43cpwYjkU3hf949OIalyPewVD9HgdI-fYACwwzvBkrkgfGnrqEOekats6bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d72545c257.mp4?token=LYtBv2ydOb1aatu91SXmupseUMx6iJZDzYR6kK_oJwp3rgJIlPaTpVJk71PlQVgJUcy9W5tEOMVGYlKquKit9RgLbWW3exoURg3zuNdYCbQs8tD0uxX-CrdmKUUEvVbvjQBXYQsU577OuPVV8K6uu3Bcu2xdfuvjjweLsz1jiXZ47_vMkscC9JCLkKVfPubGilLnBjK1BvgXzCf_wIHxq7juoSK0Hzg_LEiBB1BNnk0h82ZRAmHUdD6wR3LyxYawevRehtkeDiCD1D86ufz5yGBHI0S43cpwYjkU3hf949OIalyPewVD9HgdI-fYACwwzvBkrkgfGnrqEOekats6bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پشت صحنه لوکس‌ترین مرسدس‌ها؛ جایی که طراحی خودرو هنوز با دست انجام می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/687103" target="_blank">📅 10:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687102">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
اولین جمله رهبر انقلاب پس از بیرون آمدن از زیر آوار بمباران
فریدالدین حداد عادل:
🔹
موقعی که زخمی از زیر آوار بیرون آمدند، گفته بودند: من نمی‌روم تا تکلیف خانمم معلوم شود. نهایتاً به بهانه‌ خطرات امنیتی و احتمال بمباران دوباره، ایشان را از آنجا بردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/687102" target="_blank">📅 10:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687100">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43dc132b42.mp4?token=Q7XlTPsSQFZA2ZopKpfN12SAmukX5S_2_7WCCbeEp-FAVghqbyCPHAvrfnYLLbjisGJcFHrOr9JCJclS-kKOjG61BE7PuoHBNLg5ced-TDbQ9TGujHN7V8lEF_mBjiY8rGU2US6ABvBWhPA9kH7cehozOs-bqo4stIZqJNGk9CbKnQB2EOtzzOKYbR-WhgaxMg8ft9JeZE87HqJKOs1ybC3A5daePyrirKcTmCJngAQlR2L2nKedTKlGmMLynyH-TEl_ID_idIQsQWjoYhGw9boRObgk1qwCJWEgV-Np0MuE1udXEWRDW_U9fnJrztjnbeHbpgFDUNBSSM1uEtOkgVixw0lfNVue3nETqf-OB3db_HGq7BS0G6tRMMfxqyQvBFWfP4mW3bzP3SXO7gSM66kE5YN0lZnvsXlQY7zEsU2GT4EJaXNFpp2kIRLALbreQJdHboukoSPlfxU3TaPtwKNYhgFQ_GUU89LlkhPluWblw9434JmpNPQYju76xb3t3ies43m9XHXucnh-wYezhM029S_qdQdNGhhfOU4ufpqyhXlhbsDIUkJ8Q8OJx7iOfTxxqgtv0TETqgXb4vtZdlLLJWqx1-XzzLXvE2_nEgUrbDPq6_bxoLK4wkVc9OWMutsLI-Xa-UQWJL-dFWRZEN8tnF491mnm006qk1F84Rc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43dc132b42.mp4?token=Q7XlTPsSQFZA2ZopKpfN12SAmukX5S_2_7WCCbeEp-FAVghqbyCPHAvrfnYLLbjisGJcFHrOr9JCJclS-kKOjG61BE7PuoHBNLg5ced-TDbQ9TGujHN7V8lEF_mBjiY8rGU2US6ABvBWhPA9kH7cehozOs-bqo4stIZqJNGk9CbKnQB2EOtzzOKYbR-WhgaxMg8ft9JeZE87HqJKOs1ybC3A5daePyrirKcTmCJngAQlR2L2nKedTKlGmMLynyH-TEl_ID_idIQsQWjoYhGw9boRObgk1qwCJWEgV-Np0MuE1udXEWRDW_U9fnJrztjnbeHbpgFDUNBSSM1uEtOkgVixw0lfNVue3nETqf-OB3db_HGq7BS0G6tRMMfxqyQvBFWfP4mW3bzP3SXO7gSM66kE5YN0lZnvsXlQY7zEsU2GT4EJaXNFpp2kIRLALbreQJdHboukoSPlfxU3TaPtwKNYhgFQ_GUU89LlkhPluWblw9434JmpNPQYju76xb3t3ies43m9XHXucnh-wYezhM029S_qdQdNGhhfOU4ufpqyhXlhbsDIUkJ8Q8OJx7iOfTxxqgtv0TETqgXb4vtZdlLLJWqx1-XzzLXvE2_nEgUrbDPq6_bxoLK4wkVc9OWMutsLI-Xa-UQWJL-dFWRZEN8tnF491mnm006qk1F84Rc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رول سیب‌زمینی پنیری؛ ترد، کش‌دار و بی‌نظیر
😍
😋
مواد لازم:
🥔
سیب‌زمینی پخته
🧀
پنیر موزارلا
🌶️
فلفل قرمز (پودر)
🫑
فلفل سبز
🧂
نمک
🍋
آب لیمو
🍞
نان تست
🛢️
روغن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/687100" target="_blank">📅 10:28 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
