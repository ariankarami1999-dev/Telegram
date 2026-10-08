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
<img src="https://cdn4.telesco.pe/file/h3iGs57JPlXd8JFw4KYoHB4JV9MJn-8cqWkcvL18Y3gfA2ZoQtlay8ceD83V2Z_W7zBr4JP8R8jWN2kLuN5LxD4jYdFst6T9Wk8p0oolRIwv_JHoDSNAQNL57V8PB3i7Pl5uwgBUJHVFyitnjtQ7nBa1thoTjNT5oeNE5ZeoIFMANeoLjlsTDl7svl180DJWTLh0N-jYgHuFRQ4y0TB9vHhOkVjGq2b7pqc0fKI8nAyn5eNJ1WgMJ4KBnxpMhKFGVYvzeNK6Fw8N5kyXZPGnkP4CxKmDT6bVOe4vofgfOZYO64Px06QGC6lQ4MIYhzyf5uGFaqeS_FuXK72Otu9vZw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.34M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 12:43:35</div>
<hr>

<div class="tg-post" id="msg-696575">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-z9dmYLkmVvEXpPjaaZCjnuZQsaXKnG7leOAEvxaJzTVlnhRhisOgE7KQx_aeq_ME0cPL20AXBCHHrD58veg5d7Bqo7r6CuE-kTqgqy_Hi7u60Ad1Y3Lkum5nMw2XHHDyeRTEg9kbTMp6Q_n-Fi0CLd78d0s_uha9tGG1F-0ZUXvQgPpaQXDs30OXXoy-VNRkW7FgSJIck3cMKG0XF3ABHRw5eHTcPZOHTbGtJL4uO-re_0gc0xAv65Mtjb5t487IgcTlDGApEXTTS-SHTCKrQDMJNcv_ucdgBSHG2Pv9OC4L2HQ1cXhGJOIQZZz3Vqx_Am7iWkHGxvFFrwjmKTEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgpyoFKILlR-37wGQxdMv3NiZZjvCbSf5IPUv0pf5sJH8zBfNDudl7yJKmCUsz_OM9XszJ2J9ievadbHeKXqgrZs8EEpXLnONP7PVeLfdjXQJtFBCi65681wqEfH-GUhii6UrD-eWqyZ_9yyhKKAb5zNrjT0UDwjm5r79ph8Gy2enl0XWNB9Qrw-udtmn_XoHJ5bRG-R2DAEg00YfIfQwDXfxxenmWulMJ4JJYT3_LCpM87s1eVO0ADE0RebLFROgIiZvXljmKIKONiE-kqGPWJRrxPCfjCSfatPRPEdZhlnvr1KxaT1vw42yCP2ZADZvXKEONqAXVdxCEyvfVqRWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SwjjbpzTkUHCOiJVtvXmLGlgoMB_Xr883qxXXHmyFCA_DRJXVzLnbACOsBskMJGAUO3Yxgts2HQU8D-g8u8BuHfK6iX_tufUmdMZ1y1gIVX9NIfHc6ThfBKYO_YkK-jHI0-rHLixtOSK8Br2ttJ1NKFPvxJPBlQthj6GxSUH-LeV-a4k6e-snW3lnOFfaMiJ9vvdyh88YG-gtszaXeJVBoU4BsZCjhhnAnUPLgs6qqooWXV2GbZNYvO7T1dP5b_4DAffZ6xZlYOJTbLqgVorTavMB7DRdWNuC3-OMxL89a7rPpt5HbhHbRg82TLuUWrFHEjCokSY-NNfB9Brdm3EVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IBWuc8bv1Ggurva2n9zV-7BABZ7z1aHIaaMxoc2Jb-5GF_D3t_8tqUdP7RdxNwmYgnCH_3Cg34Q3PDyt52cG7ZrUko1AEl7v--V8Sh51azHARGlN_iqJ9iWbzMuleM3-yWJMKHl-_PrLlJ5fUFUL27x_KNraFsImGsChr_4saZBTjnietI_HdpR2PKjnvSz1JDWxLf9gTnv3h0l8bq3JGhIgWjQDzUJN-lS4loJr1-aISmE9SFmTECjbyC55JUxoJaQ1LnR874TzY_O0Wb5vdPjXVNEB1B-2DgpwYqcbKVex_99kbAZJCrOySPR6SkMQi6XL5DxBYxFiFhDpkZ3V6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O-vJjdpLLLpCQp5nmuMLBLGRK0q9JeUcHhSluM1ShgpbzRcWAYbpbxs6QpQ_c64IcbM7tzXcImRFjLIIQ1rTf8mdL1jBmE8vEqVUScMy5XpNcuFxlvY8Sl5vPSDvju01nMz8-ScWoCAb1VjeAdwlmT-vdqxYU59FRR25R4NbvC_ihRvK4ybF12f_8wtM3aBsFiWNfHzBW7R9WOIDm9sfv7MNEDQmjudI24cEp14rFLcLdVyLShiobzGRW-_M-jWutunajEDu5g7v5DRQzPWKyBeoc6uXIR7cKfxuFfu04CztBL_aBjYCmVm51bSqs5W5sTs4DsFKCU4ulDE57-fOTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵۰ پرامپت وایرال برای ساخت تصویر با Chat GPT
#هوش_فوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/696575" target="_blank">📅 12:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696573">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
حملهٔ مسلحانه به مینی‌بوس حامل کارکنان نزاجا در زاهدان
روابط‌عمومی لشکر ۸۸ نزاجا:
🔹
ساعتی قبل مینی‌بوس حامل کارکنان لشکر مستقر در سواحل مکران که برای تعویض شیفت در مسیر بودند، مورد حملهٔ مسلحانه قرار گرفت.
🔹
در این درگیری یک نفر به‌نام محمدرضا اوکاتی به‌شهادت رسید و ۳ نفر مجروح شدند.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/696573" target="_blank">📅 12:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696572">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amvMZgVkCuk19y_s8my6LhB2OjKZOLlcZJSF3m72gqnIXptE9BmX0jluVdYnede21gzb4IBlrcH1nkKelD0XsPk6l7FWc2eLEry9x2NbCtw-GvJILEVmWAcuBxE8f195efj3s96YUzoh-kWESadOZD9sVbMllnOlDf1m2DFyjxNYF_TwKm3ha4mh74QWUraEWI9V7Zpx1Vf9ErcZTBkxmOUipGAo2T1WXXqpoI62DMGYywdl75uOeGz1cqYXpIlR-feE8lZzRi7oYjlQFAtrUrj-Xom22cPVVRhfspaLqATWRn9D6w7JjUoMoIinpLc_AUIhX_Q-WbQ4ejSlKWadXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا شب‌ها انگیزه برای تغییر زندگی داریم اما صبح، پشیمون می‌شیم؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/696572" target="_blank">📅 12:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696571">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
رئیس سازمان برنامه و بودجه : افزایش مجدد حقوق‌ کارمندان و بازنشستگان فعلاً در دستورکار دولت نیست./ مهر
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/696571" target="_blank">📅 12:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696570">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-B1wMTCYlqAO4Cc2YjYsgfCP7vZiVNaMUhDMlK4GysOlQL_IXde7AIXO1Vz89M-JJfK75N7MJ47zq8DS_3HaWuVq685MYw8Zdcz3B8dU9wNt0aY25ZnxS4PwGlHT_ZUieJ4c_hK5f-c9_-c_MVI6Kvk87JrmK_FULTfWMrF3pkgx8MTYN5G3URF0_iyfW29LutYw9D-o6MMJJiwt_3YAxx4zMfPHMoDwHg6Y96dpzi8aQgvaPYUxz5CkYCEcUDCS26rF5H28-Qg8wpwDHDF808OC3GNO3N5bKvBJFxwi8R8lEGow2exGZ_-VhavRnskiykN2oKKMnCsxONNc5D1sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گرانی نجومی خودرو در ۴۰۰ روز؛ در یک سال گذشته خودرو چند درصد گران شده است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/696570" target="_blank">📅 12:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696569">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ساعتی پیش یک خودروی پلیس در منطقهٔ نصرت‌آباد زاهدان هدف حملهٔ تروریستی قرار گرفت
🔹
در جریان این حمله چند فرد مسلح به‌سمت خودروی پلیس تیراندازی کردند./ فارس  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/696569" target="_blank">📅 11:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696568">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b1340b42a.mp4?token=Kd-9g44ggnjzxDHdzDDDMTr6E5jYUaPyIbcGk1XsJNlMLg7ifbIHFBnmuFw7nS2U-jH3pRDXmbnJlYS0xOFtkYDlnwv_1A35o2EiecTlpYOI-s1BZp-tpomHWooOqvI07B_-_PP4F4OrPzabKDXcSwlgU-TH3nne3OtG54Q4Nv8IWv8XwN4sKBbB12x4GjYwnsqILZAHZiLhKAG6yf78T_QYKBr0ZpAEb0TuPAW0MRcWvNTD4y9tix89rdch8SdBoK4bQU4Wo6XVYymJZKZ77ITKgc-uJmvf0_E8CJTfrZ3G3eGZTanC0iAhpMJtRVhm_d6AYur5kzC6JnxqGFtaDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b1340b42a.mp4?token=Kd-9g44ggnjzxDHdzDDDMTr6E5jYUaPyIbcGk1XsJNlMLg7ifbIHFBnmuFw7nS2U-jH3pRDXmbnJlYS0xOFtkYDlnwv_1A35o2EiecTlpYOI-s1BZp-tpomHWooOqvI07B_-_PP4F4OrPzabKDXcSwlgU-TH3nne3OtG54Q4Nv8IWv8XwN4sKBbB12x4GjYwnsqILZAHZiLhKAG6yf78T_QYKBr0ZpAEb0TuPAW0MRcWvNTD4y9tix89rdch8SdBoK4bQU4Wo6XVYymJZKZ77ITKgc-uJmvf0_E8CJTfrZ3G3eGZTanC0iAhpMJtRVhm_d6AYur5kzC6JnxqGFtaDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راهنمای‌کامل‌برنامه‌های ماشین‌لباسشویی
که هر خانه‌داری باید بلد باشه
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/696568" target="_blank">📅 11:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696567">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
سخنگوی قوه قضائیه با اشاره به رأی پرونده‌ کلثوم اکبری: ۱۰ خانواده‌ درخواست‌ قصاص کردند؛ به ۱۰ بار قصاص محکوم شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/696567" target="_blank">📅 11:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696566">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
اسقاط خودروهای فرسوده در سال ۱۴۰۴ با افت ۴۱ درصدی نسبت به سال ۱۴۰۳ از ۳۴۹ هزار به ۲۰۴ هزار و ۴۹۹ دستگاه رسیده است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/696566" target="_blank">📅 11:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696565">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
بازگشت افسانه آمریکایی؛ دوج چارجر کلاسیک پس از سال‌ها خاک‌خوردن دوباره غرش کرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/696565" target="_blank">📅 11:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696564">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5df45dd269.mp4?token=uN0qmL7-_uiYVvKsypoMcuH-oJNkuNeehkEuGRkF4quVTQPB-sOD2-0Z_i96kjM9K14NjIfIuah81Qyp3A0KPlQiJ8IOxPnNPcZAZaPfYDwUfZTsEs4Btvd11nWNrdGsWF67ga_T-Uzgx7dyAoZOcP5wGiTvs1jKY5iqH3VNNw4-PgC_50-lvfvkwUOCr-6mZNyYBKkvCfVeBBLfxappV77tW4ShDsrmwmVJcZ8f-x7t_WBiw9pUrZuF1DrsSEAORYpb85McYbklYe6gG1IRp87KxTLYSCgh_J9C9wih-sPKSEHQPdFu7Q9Enw8H8UI3CllpXCd0IKkrUBSADvbKig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5df45dd269.mp4?token=uN0qmL7-_uiYVvKsypoMcuH-oJNkuNeehkEuGRkF4quVTQPB-sOD2-0Z_i96kjM9K14NjIfIuah81Qyp3A0KPlQiJ8IOxPnNPcZAZaPfYDwUfZTsEs4Btvd11nWNrdGsWF67ga_T-Uzgx7dyAoZOcP5wGiTvs1jKY5iqH3VNNw4-PgC_50-lvfvkwUOCr-6mZNyYBKkvCfVeBBLfxappV77tW4ShDsrmwmVJcZ8f-x7t_WBiw9pUrZuF1DrsSEAORYpb85McYbklYe6gG1IRp87KxTLYSCgh_J9C9wih-sPKSEHQPdFu7Q9Enw8H8UI3CllpXCd0IKkrUBSADvbKig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدرضا باهنر، عضو مجمع تشخیص مصلحت: امام جمعه کرمان چه چیزی از مذاکره می‌فهمد که در این خصوص اظهار نظر می‌کند؟
🔹
کسانی‌که در میادین می‌گویند مذاکره نداریم بیخود می‌کنند چنین حرفی می‌زنند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/696564" target="_blank">📅 11:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696563">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNFGPLU6cOPO_3ku2rJCCGLfYAkjXtelHNgNw9OmBD1CT_CTmPu2rYWSWZElV199SI2OdW3cnX5IIhyT-LBtNjbG2Q12CjIV6sGCv_m4cpjzThBI698n1ohiv6F2hZYVmK0duwt6D9qQ_f7WlXrNUopZyL6n7SO5HshdxBheas3MD4aAIU-8iUtvg8xIWXvZgpylq8e05E2I5gVz7G1oKyYt16HZVgRwUHgr1P44fUEW55UnZ1DesBHTGMu9nuLTC3ZMGMupifbHzPYyCX4xnMnJBU6L9WN-BjBnDJGbkP0l7x-Q0kbhuR6rDierGSHAzNc-F5qPiH2Ux0FvPS7OWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کرگدن ۲۰ هزار ساله در سیبری؛ کشف باورنکردنی از عصر یخبندان!
🦏
🔹
در یاکوتیای سیبری لاشهٔ کرگدن عصر یخبندان پیدا شد که شگفت‌انگیز سالم مانده، این کرگدن جوان فقط ۳ تا ۴ سال داشت و ۲۰ تا ۵۰ هزار سال پیش مرد. نکتهٔ عجیب، سالم‌ماندن بدنش است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/696563" target="_blank">📅 11:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696562">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
محل تجمع نفتکش‌ها در نزدیکی امارات منفجر شد
🔹
آتش‌سوزی در خلیج عمان، ۳۰ مایل شرق فجیره، ۱۴ کشتی در ۷ روز در تنگه هرمز هدف حمله قرار گرفتند.
🔹
قیمت نفت هم‌اکنون در مرز ۱۰۲ دلار است و تحلیل‌گران می‌گویند با تداوم این شرایط، نرخ نفت به‌زودی از ۱۱۰ دلار عبور…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/696562" target="_blank">📅 11:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696561">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CpQSDRyy0TzfTi3ey0GSUbEmyp4zYFZwnXTKMO0vhprgocVljqLoaCuvD0OnV3i5IdWo8KEFJq5Hsrz_iPzV18vwPBHkT4al0BG6i9Hlll0H9Ts9M4HXv3e7sfk1nsGqVm2ka8XrsKMK7JNQNt__xEpZg8WqRME7N8UO15hbGNFWa-4J82lslMAvZMTpBfH9ramn34GpTI1QWqc1aepKUhSd7CpEQF6ueDlYwGSgshStd0-pUGlYUPfwwaEcaR-fD-5OqSDWppd3oSoVEu0p01ewIf6wiEHUeGIMZDpCcz3YK18jA2vJy8KY5XkCGiktv20KXVeQmFG5986KFycefw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای کامل کدهای تلفن همراه
📱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/696561" target="_blank">📅 11:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696560">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
ساعتی پیش یک خودروی پلیس در منطقهٔ نصرت‌آباد زاهدان هدف حملهٔ تروریستی قرار گرفت
🔹
در جریان این حمله چند فرد مسلح به‌سمت خودروی پلیس تیراندازی کردند./ فارس
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/696560" target="_blank">📅 11:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696559">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAmyLbsWRI3DnI33GeSPBzxWM__f9E-9TYqnoC5CJ_GLycRbjjUMz0Hbjqik62PuEJh57OUdVyx2_f5dHPt094OrrpS_cJI_SJIZ44wnbx9-29QeoNjUgxKCr5C3G75s_0cY3lvcQV_qvCk38xiRMICiAxooIWFIAXEF4483nWM1Vbh2va6QnTFYal9bIDHpT-rqOcCtsTYRxQy_ZgdDsxwWUbZX6Sp4YMxJtcJLObz_mu7ZDxzkKE_5LcxFbYOWb_zVr-27uYZEOZCJ1jsmJ5iTWAAWP24sqL5MRshPNhv1uVKAFcudcYK1__AGxqMERtE554Bj21DY1GudCKxdsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدیرعامل شاتل موبایل: ۹ سال عقب‌ماندگی تعرفه‌ای در صنعت ارتباطات داریم/ طولانی شدن سرکوب تعرفه‌ها، صنعت تلکام را به یک وضعیت قفل‌شده رسانده
🔹
آرش کریم‌بیگی، مدیرعامل شاتل موبایل می‌گوید تعرفه دیتای موبایل در ۹ سال گذشته تنها سه بار تغییر کرده؛ یک بار ۳۴ درصد و در سال گذشته نیز ۲۰ درصد در آذرماه و ۱۸ درصد در اسفندماه.
🔹
این میزان افزایش با رشد تورم، هزینه تجهیزات و نوسانات ارزی و همچنین هزینه تمام‌شده ارائه خدمات همخوانی ندارد و تشدید تحریم‌ها نیز فشار بیشتری به هزینه‌های اپراتورها وارد کرده است.
🔹
کریم‌بیگی با تشبیه وضعیت تعرفه‌های ارتباطی به «ماجرای بنزین» معتقد است طولانی شدن سرکوب تعرفه‌ها، صنعت تلکام را به یک وضعیت قفل‌شده رسانده و اصلاح تعرفه‌ها باید با در نظر گرفتن شرایط اقتصادی و به‌صورت تدریجی انجام شود./ ایرنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/696559" target="_blank">📅 11:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696558">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
امروز؛ آخرین مهلت انتخاب رشته کنکور ۱۴۰۵؛ داوطلبان تا پایان امروز فرصت ثبت انتخاب‌های خود را دارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/696558" target="_blank">📅 10:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696557">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
یکی از عجیب‌ترین اتوبان‌های دنیا؛ تقاطعی ۵ طبقه در چین!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/696557" target="_blank">📅 10:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696556">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
علی مطهری: آمریکا ظرفیت یک جنگ تمام عیار را ندارد/ بسیاری از ادعاهای ترامپ بلوف است
علی مطهری نایب‌رئیس مجلس دهم:
🔹
آمریکا ظرفیت جنگ تمام‌عیار با ایران را ندارد، چون تحمل تلفات برای آمریکا دشوار است و به اعتراضات داخلی منجر می‌شود. او همچنین سخنان وزیر خزانه‌داری آمریکا را فاقد واقعیت دانست./ ایرنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/696556" target="_blank">📅 10:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696555">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
منابع خبری از شنیده‌شدن صدای چند انفجار در پایتخت عربستان و توقف پروازهای فرودگاه ریاض خبر دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/696555" target="_blank">📅 10:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696554">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e09d3f41e.mp4?token=izmUU3q-NpH_FTFFFrhMnOaOt8ob976GgsbrmOVXIyBEkDK9GPh_AG7FwIQIHqqz1JTgh3oPCo41l-9n9dbc1ofTNoI8z6zE8VmpJDj0uITPju-ucuUZeX5XLyUOKsLXDtSpfl_4zDV4KYSskJB6hyCKdhEQmfM1lSCKMz510SgkCwGdYAQYeHxdMTzcctJ8yOOVVa5Z48OJ7v7XNUIv1N4WJoxlvyvD0PfXIXXJmabd6rN1vnL45ahOeK090VlIuyx59zStPrG7gyyVddE1j-ABA2N_cEgtXt5gyiQ_Urd4yUPurrN6xSH2YamvS6wUoMgV_7sG7FhbQKpyiGdiOHKURIIlBt_2bQsP8bGQeBTd48Q2i6lfMTkOLnC2jRZWPBqI_f2RZxsUJen8DrBplLoafuq0SYf4DlGbW38Qpgb-ZjRPoiAbgAnKnlUaqMjXAKGfzgv7-VDRBpVWYH7oZfGI_vRrlKPNnEJQfNuHPgGdgwM26mTCTOCgKEb6f7UR_ZsZny5hzrLQtwpTkdJMgr-50Cfh7Zy703wpKwPf6N1_9Zn5uT-rmRceE40kZdUNjpj0KBVT_QRWCBxRtHCCSifkMI6c89iik7SIxlNRAbFtFq4_RJJRE5R0iunF-C5g2_NOnGL2cW5mxn03YqT-yiRpMYCxIt_ojsiBfAzfTgU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e09d3f41e.mp4?token=izmUU3q-NpH_FTFFFrhMnOaOt8ob976GgsbrmOVXIyBEkDK9GPh_AG7FwIQIHqqz1JTgh3oPCo41l-9n9dbc1ofTNoI8z6zE8VmpJDj0uITPju-ucuUZeX5XLyUOKsLXDtSpfl_4zDV4KYSskJB6hyCKdhEQmfM1lSCKMz510SgkCwGdYAQYeHxdMTzcctJ8yOOVVa5Z48OJ7v7XNUIv1N4WJoxlvyvD0PfXIXXJmabd6rN1vnL45ahOeK090VlIuyx59zStPrG7gyyVddE1j-ABA2N_cEgtXt5gyiQ_Urd4yUPurrN6xSH2YamvS6wUoMgV_7sG7FhbQKpyiGdiOHKURIIlBt_2bQsP8bGQeBTd48Q2i6lfMTkOLnC2jRZWPBqI_f2RZxsUJen8DrBplLoafuq0SYf4DlGbW38Qpgb-ZjRPoiAbgAnKnlUaqMjXAKGfzgv7-VDRBpVWYH7oZfGI_vRrlKPNnEJQfNuHPgGdgwM26mTCTOCgKEb6f7UR_ZsZny5hzrLQtwpTkdJMgr-50Cfh7Zy703wpKwPf6N1_9Zn5uT-rmRceE40kZdUNjpj0KBVT_QRWCBxRtHCCSifkMI6c89iik7SIxlNRAbFtFq4_RJJRE5R0iunF-C5g2_NOnGL2cW5mxn03YqT-yiRpMYCxIt_ojsiBfAzfTgU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با بچه‌ها درباره شوخی‌های خطرناک در مدرسه صحبت کنید/ ممکن است جان بچه‌ها را بگیرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/696554" target="_blank">📅 10:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696553">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H48sQq_QzNuHMORpnqJEWv_b2AEjWXJKWct7X10tPSqlfxPQm8VVzeP7C6l0m1nitibx5rOLlZ9ATPW3FoKUoCMOtlOv-5qggqTt66P1dNkNB0InT3aL363s1NkHihUUAk1hm5Gb4g6RIK4UZCPwCujAzjldHEj2TZ0uAcY95OxglKN4l0oQBV8WwGH6LKoEA7AK7lxJuZl0rIr5a9L7iDLLvIsyTnYNbGIDzsDpF-wabRFV9ST6EEefAVCukDdulKTpgYkKE3b97tEFEDVMLnXjYJspko8I4tDdgfFk1UZm5a_b6gplpwtzu8oqPVh-WQROX4hLQl9EPGW31NsxOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت سوخت در بریتانیا به گوگل مپس اضافه شد
شبکه BBC گزارش داد:
🔹
گوگل مپس اکنون قیمت سوخت را نمایش می‌دهد تا رانندگان بنزین و گازوئیل ارزان‌تر پیدا کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/696553" target="_blank">📅 10:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696552">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAvCiD6AL8LrGhaKZqCnaucdgqiVI_kjiLrKV8KSnaHl8e_dE4tLIwHEVxbzLDGaM8FAReYg6a_UNUFW5QgNqXMZtxFYQ7o9MGsfuZbQ7Avsu9GKYi1sx8sBZvYoZwDUvJTFATQ_hrHDaaeDUVy_QXm0SYi_si354F0aAhqWQoUq1sewZ3F2gTRy3NMVGltJpwz9hFVI4CP-wUKBPO-wQeNbqKHB28hbWhClPAX3Q6-zk_IK3Uo0MSmTK6fzK8bOnZFfFfABdj1sld1ePmScshxbcWI2ypTOhZ6elYAkKR0WIQMDKLoYaqI4wSpuIdWIqIMz8Y2BtgNgIIvasMQ6-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محل تجمع نفتکش‌ها در نزدیکی امارات منفجر شد
🔹
آتش‌سوزی در خلیج عمان، ۳۰ مایل شرق فجیره، ۱۴ کشتی در ۷ روز در تنگه هرمز هدف حمله قرار گرفتند.
🔹
قیمت نفت هم‌اکنون در مرز ۱۰۲ دلار است و تحلیل‌گران می‌گویند با تداوم این شرایط، نرخ نفت به‌زودی از ۱۱۰ دلار عبور خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/696552" target="_blank">📅 10:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696551">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
سه قلوهایی که رتبه برتر کنکور شدند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/696551" target="_blank">📅 10:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696550">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nttMkZ2cCbfqD5Y67OL4m598WnY-gaWGO00HXH-DoeziIOkJE47EQ5SpOhXvEjLqbsSHy6W-4VljXXYw1Ivl3cZfYZH48gDFmBxtbOFE1P3GWlFvJMVtmNTstMCx1ivY4kxpgX4NUYf_4GQ2L8qTvEyYZIMmYfoRFekpKxQU3loNDo4H5n17Wyi5Xs1i8ld1mW6gvUY_x_qigSa-_7Stm7v2DoyUd14Gllmd1ZJAG4-kQZoj-dknUBpr4Z1KChjvdX84kAvzQnRSFMVdYMQx26n052A7JtvIrdxNuPD6tojxdp0OSnS754H1zDEjcCjnUFQ8o3IIzkb5I4pqzy5Lzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: قیمت نفت به سطوح پیش از جنگ بازگشته است!
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/696550" target="_blank">📅 10:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696549">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c93242736a.mp4?token=JW2w-G7lSOPf6IyVDgCwODk_q1--JCvVz3HiUj_Rbd1RcQvfxYpMYYH25UOkHEmy94lNEbtw6iVhfJYxojGTw5qauX99CpGtbVQqwIJS1m59zeYaMlje6OhQwI00rAyLUhUp4mRgxebQ7vgH6ADnit0xEnXlT6fziA7sgK4tlzDyvQIJM1Yfn_rSUhE52RhJKoA91eO5-AijYPj9RQeSogaROE7oVvl2BgVnoQKhy-GP8B0A5Ktk65SwiVpeM-nrtxazbZ48S2rTEPGse13S1EnXwgw1XjVyKv-09Wsq1_23fHTIHEd7IdqoUgD6Dtkuz89bEKJmnJhB6FIEfJ10LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c93242736a.mp4?token=JW2w-G7lSOPf6IyVDgCwODk_q1--JCvVz3HiUj_Rbd1RcQvfxYpMYYH25UOkHEmy94lNEbtw6iVhfJYxojGTw5qauX99CpGtbVQqwIJS1m59zeYaMlje6OhQwI00rAyLUhUp4mRgxebQ7vgH6ADnit0xEnXlT6fziA7sgK4tlzDyvQIJM1Yfn_rSUhE52RhJKoA91eO5-AijYPj9RQeSogaROE7oVvl2BgVnoQKhy-GP8B0A5Ktk65SwiVpeM-nrtxazbZ48S2rTEPGse13S1EnXwgw1XjVyKv-09Wsq1_23fHTIHEd7IdqoUgD6Dtkuz89bEKJmnJhB6FIEfJ10LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایش هیجان انگیز و تماشایی آتش‌بازی سرد در کوه مینگشان در چین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/696549" target="_blank">📅 10:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696548">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
معاون وزیر خارجه ایران در گفتگو با رسانه روس: جمهوری اسلامی ایران طرح خود برای حل بحران را از طریق میانجی‌گری قطر به آمریکا منتقل کرده و اکنون توپ در زمین واشنگتن قرار دارد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/696548" target="_blank">📅 10:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696547">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
استانداری هرمزگان: صدای انفجار دقایقی قبل در بندرعباس ناشی از عملیات امحای مهمات عمل‌نکرده دشمن بوده است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/696547" target="_blank">📅 10:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696546">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGoldiran | گلدیران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358f4d9375.mp4?token=MQ-12B1OhHOBxZrN4zSW5Vu6qvpdq98oZyUWjJZDfYuD1DBegQz9xOVXhn-x53nzrBoLkJ6coINQ7KEtBYNmYGzu8U2E950sW7Vj2rLTacn7OjuMl2R-ujFyQnvh2Yi_I0pSUWiTI62bVlg8pmoDI4DdOeOKBFftxuY3dskhBCJZ1Qz4jASxVVuiZYZjmb2Zk2i3USrAyI8OxLDyitwKO5Pc9lmWXdZTLwmaFEP2aIzFV5-ODbXW_kUV-xpgKwDnazjP4BP6O7lsGm69PbqaA9O6quVyJqT29WCssTyYAh-GtTuqJuiy2R-cGfmPoytArbGo9LUOGg-y_KVl7Ej_wX3mgr_zX1xHN2xHwnrRoxSvh83cC7T_HztCIcZ9dzK_SqnTr-yCngPcp7hMOXeS3bwQllS4qxmxlQJRR3efSssoKv2MRf08lzjNCo3jmad0Gbt7XV5eM2BL_JGXucXyPA74Ycip1ioZeWy_sRuJTrUfhRm6CbK_hvY6-nITqulC7ZeQFcX4TmOWwiCAF4V-oyrWcpaV77THxSBhscP8ZMwzzcqK6WG9Kprkm1rzHZHwr3YtPnmc2wDa8t2bOCx9-VBKuyLj_uVJnDONLNzAT94ULoqiEND9vHdj9On9RLsyJRgy4hcfUZKBkLFQWyxDpAEwsqQwDZEEiPECMDKJsaU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358f4d9375.mp4?token=MQ-12B1OhHOBxZrN4zSW5Vu6qvpdq98oZyUWjJZDfYuD1DBegQz9xOVXhn-x53nzrBoLkJ6coINQ7KEtBYNmYGzu8U2E950sW7Vj2rLTacn7OjuMl2R-ujFyQnvh2Yi_I0pSUWiTI62bVlg8pmoDI4DdOeOKBFftxuY3dskhBCJZ1Qz4jASxVVuiZYZjmb2Zk2i3USrAyI8OxLDyitwKO5Pc9lmWXdZTLwmaFEP2aIzFV5-ODbXW_kUV-xpgKwDnazjP4BP6O7lsGm69PbqaA9O6quVyJqT29WCssTyYAh-GtTuqJuiy2R-cGfmPoytArbGo9LUOGg-y_KVl7Ej_wX3mgr_zX1xHN2xHwnrRoxSvh83cC7T_HztCIcZ9dzK_SqnTr-yCngPcp7hMOXeS3bwQllS4qxmxlQJRR3efSssoKv2MRf08lzjNCo3jmad0Gbt7XV5eM2BL_JGXucXyPA74Ycip1ioZeWy_sRuJTrUfhRm6CbK_hvY6-nITqulC7ZeQFcX4TmOWwiCAF4V-oyrWcpaV77THxSBhscP8ZMwzzcqK6WG9Kprkm1rzHZHwr3YtPnmc2wDa8t2bOCx9-VBKuyLj_uVJnDONLNzAT94ULoqiEND9vHdj9On9RLsyJRgy4hcfUZKBkLFQWyxDpAEwsqQwDZEEiPECMDKJsaU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
این جارو جمعش می‌کند!
💥
جاروبرقی جدید جی‌پلاس مدل Hunter با موتور 2400 وات به بازار عرضه شد.
جاروبرقی هانتر با تمرکز بر قدرت مکش، عملکرد دقیق و استفاده آسان طراحی شده تا گردوغبار و آلودگی‌های روزمره را حتی از نقاطی که کمتر دیده می شوند جمع آوری کند.
🔥
برخی از ویژگی‌های هانتر:
⚡️
موتور قدرتمند با توان حداکثر 2400 وات
⚡️
مصرف انرژی A
⚡️
فیلتر تصفیه هوای 5 لایه هپا ( Hepa Filter )
⚡️
گنجایش مخزن 6 لیتر
⚡️
شعاع عملکرد 9 متری برای پوشش ‌‌‌‌‌دهی گسترده
⚡️
لوله خرطومی کنفی مقاوم و منعطف
⚡️
لوله تلسکوپی با طراحی ارگونومیک
⚡️
نشانگر هوشمند وضعیت کیسه
⚡️
سیستم محافظ حرارتی ایمن
⚡️
24 ماه گارانتی گلدیران
🔗
برای مشاهده جزئیات و خرید محصول، به فروشگاه‌های گلدیران پلاس در سراسر کشور یا سایت فروش اینترنتی مراجعه فرمایید:
🌐
Goldiranplus.ir
گلدیران؛ روی خوش زندگی</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/696546" target="_blank">📅 10:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696545">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
اسکات ریتر، افسر سابق آمریکا: ایرانی‌ها و انصارالله با تسلیحات کمتر و ساده‌تر می‌توانند آمریکا را شکست دهند، اما آمریکا تصور می‌کند هرچه بیشتر هزینه کند، بهتر است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/696545" target="_blank">📅 09:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696544">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
معاون وزیر بهداشت: هنوز ابتلا به طاعون قطعی نشده و تاکنون نشانه‌ای از انتقال پایدار انسان‌ به‌ انسان یا خطر شیوع منطقه‌ای و پاندمی گزارش نشده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/696544" target="_blank">📅 09:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696543">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d9bf4e68.mp4?token=EwYFuYWAtvF42JSrmDhv4kxNWliidQFgwcWBcaGBwuizTJU_8spgGdfbyfhYVGahlyvzfKq47Cu5zNTR95Sc9HgDWdilQ4rMksj_T1Rsv0YIcNCiQL1bn6hAkENJklMMEnANdTkpqHtnme6L2_rApj-kM4rK7axrIv91bTuX03zs6AgT9KJBebEhs2kzCcx_AAOTkbjeopzvSmoZkzm3GKz6Kh2qTs1BYCWm5C5oc4vGHrgYFLamwdwXFBosVQD9hsfR_31c3ae1l4G667m5nYxvkcELnP5JqhE1iF7FotZAod5mM_DcVXra8JxB8lvB7aQbQewe4IhChWBBwtYqfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d9bf4e68.mp4?token=EwYFuYWAtvF42JSrmDhv4kxNWliidQFgwcWBcaGBwuizTJU_8spgGdfbyfhYVGahlyvzfKq47Cu5zNTR95Sc9HgDWdilQ4rMksj_T1Rsv0YIcNCiQL1bn6hAkENJklMMEnANdTkpqHtnme6L2_rApj-kM4rK7axrIv91bTuX03zs6AgT9KJBebEhs2kzCcx_AAOTkbjeopzvSmoZkzm3GKz6Kh2qTs1BYCWm5C5oc4vGHrgYFLamwdwXFBosVQD9hsfR_31c3ae1l4G667m5nYxvkcELnP5JqhE1iF7FotZAod5mM_DcVXra8JxB8lvB7aQbQewe4IhChWBBwtYqfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هوش مصنوعی با ضریب هوشی ۱۵۵؛ فقط چند قدم تا سطح اینشتین؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/696543" target="_blank">📅 09:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696542">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqJ49cra4xXenz-ECrEzBDIIbg4EQObl-_t91Cgrt1stO57TEHhyA9IKUN3np7mYsBdsKDPKsZ4ZGwRWYuEn-w05FrU-wLSETc2nAI6-vMCK7amYigzsTMsfCAO28zhKBFvf_5A2ivHxQO-QyW1SWgwoVRzVAjw-Cw6Qj4S7DvX-66jKRehISytS6t2c8bHMMGtsasmpo_sr_pXpFnlWYi7VGYnLXupzQwWo0JgB1gDjLHr10PUtqaJqqSkCEZOZiUZlTSXbi6WxfzFdytzIhIvLwx_4AXKcPbmdSTe5m5N-Gsiw3_kuBVT-oDoBPtfscKf83a1YtlQ6Z3PzkZfr7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صاعقه‌ای ک به دماغه هواپیمای هندی برخورد کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/696542" target="_blank">📅 09:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696541">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/696541" target="_blank">📅 09:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696540">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcTJ6Z07-qA9FrSZbg8XjEiwuGcmKGJQzeS9-cveVuv0gPKgVJI7jY7g0sbXQ6_E5QaJ7jSETo4kaeWlahhgogIGsspxk3gvuSwvR9nLiSpt3w56T9hLo2E0rNkq8mmMBYeb1JTiDpTfi2zsZYfz5IPoRG3z3n4P6VoPXc5c1GieUL10glTBnaIdwxmS7bxU8tSCwQiu_oc4jQ9OnE_m7GPHzqzgMw2trGP-oF0NCIbiLkNqvFGMIyrL5UF0UahByGS_R_iKeYQ99xbjd2MegBr2Tk04oDHkDGJ8Khk5LyWu_35CVJneqguOb_yYwg9b7iHJBXBbtWK0tptcSoEJjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش وزیر خارجه کشورمان به پنهان کاری سنتکام از خسارات وارد آمده به ارتش امریکا؛ نمی‌توانید مردم را برای همیشه فریب دهید
🔹
در ماه می، سرویس پژوهشی کنگره آمریکا اذعان کرد که نیروهای مسلح ایران ۴۲ فروند از هواپیماهای نظامی آمریکا را از چرخه خارج کرده‌اند. اکنون این رقم به ۸۱ فروند رسیده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/696540" target="_blank">📅 09:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696539">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
چه سناریوهایی در انتظار ایران و آمریکا است؟
الجزیره:
🔹
۱- ممکن است شکاف دیپلماتیک دوباره ایجاد شود؛ تهران در حال بررسی واکنش‌های خود است و واشنگتن منتظر است، در حالی که میانجی فعال و مؤثر است.
🔹
۲- واشنگتن ممکن است لحن تهدیدهای خود را تشدید کند و بدون ورود به رویارویی، تا آستانه تقابل پیش برود؛ با این هدف که امتیازاتی از تهران بگیرد.
🔹
۳- رویارویی نظامی؛ ایران آماده است و واشنگتن به دنبال یافتن یک سناریوی موفق است که هنوز مشخص نشده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/696539" target="_blank">📅 09:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696538">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
فردوسی‌پور: فدراسیون فوتبال، از بازیکنان ما پول زور می‌گیرد! درآمد‌های افسانه‌ای فدراسیون از باشگاه‌ها و بازیکنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/696538" target="_blank">📅 09:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696537">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
رویترز با استناد به داده‌های ردیابی کشتی‌ها گزارش داد: شدت تردد دریایی در تنگه هرمز به پایین‌ترین سطح خود در بیش از دو ماه گذشته کاهش یافته است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/696537" target="_blank">📅 09:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696536">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
مصرف چه تعداد تخم‌مرغ در هفته مناسب است؟
🔹
حدود ۷ تخم‌مرغ در هفته مناسب است، اگر کلسترول سالمی دارید و رژیم غذایی قلب‌سالمی را دنبال می‌کنید، ۱۴ تخم‌مرغ در هفته هم معمولاً بی‌ضرر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/696536" target="_blank">📅 09:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696535">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76d1b4d0d.mp4?token=IEJ4YDJ9YszHdb7oCvLQiffrrXMG0Uzbk0QLJiokSGDEXq-YfrHMEZKkxJbLdYvAZYzJVjPU2GMBODyOo3kUzAfHF8Ds6Wjaj9FSD_aF54qDLYjXWGamy5O_-853lV6T6XeLNiM1D2SOItzL2UzeXKVC3es9f0fngn53owBrv3y9lbgsHvNLU-ojt72L20jvzcSMrZWWDMPEzKhtGrTuLveq1M3m5t2Pc5M_GhWm1MKd_jcHQcKUQ0UtTIc2YUil_jVESE8H0Z9v20lV3brQBnhKlGr6ZmUVw9tp-proimTw3lZkVsAisLie-EozVg_H0N1h5WVMSMIkfVGT9Dye1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76d1b4d0d.mp4?token=IEJ4YDJ9YszHdb7oCvLQiffrrXMG0Uzbk0QLJiokSGDEXq-YfrHMEZKkxJbLdYvAZYzJVjPU2GMBODyOo3kUzAfHF8Ds6Wjaj9FSD_aF54qDLYjXWGamy5O_-853lV6T6XeLNiM1D2SOItzL2UzeXKVC3es9f0fngn53owBrv3y9lbgsHvNLU-ojt72L20jvzcSMrZWWDMPEzKhtGrTuLveq1M3m5t2Pc5M_GhWm1MKd_jcHQcKUQ0UtTIc2YUil_jVESE8H0Z9v20lV3brQBnhKlGr6ZmUVw9tp-proimTw3lZkVsAisLie-EozVg_H0N1h5WVMSMIkfVGT9Dye1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هواشناسی: بارندگی‌ها تا شنبه در برخی نقاط شمالی کشور همچنان ادامه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/696535" target="_blank">📅 08:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696534">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b899c26623.mp4?token=js2xRBRBtCXFgNKkOCTv6bEJkTxASdwdg98za8wq7s7UUOwS4hjHtFV_-q_NTHnYiXGguZXjcbjFe7-dm0ZRy5dqqN3gwxsYg9hltWG-rWa1OPD6Ljx3P3rRKzw1M-7ex8AasNYdPQDpoHq-Kk8vGNQmui96jJGPmzewVQ_Tvx0OkS4SbPdD0hDfvtJ_MY-2LYQi2O7lCH3d8Xd1rUNQE3UdcPvoSSTFc-jNCLzpFUZc-iI3cX73PF0pgLWIibfKyhVRTWa87Bk4WBxFWfi5vgfGBR0Ip4tWSzL1mPsZDLaCaJ_lBxCNP9JowW0FarCmXlU2gh-SLD7mJYsf4o5JgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b899c26623.mp4?token=js2xRBRBtCXFgNKkOCTv6bEJkTxASdwdg98za8wq7s7UUOwS4hjHtFV_-q_NTHnYiXGguZXjcbjFe7-dm0ZRy5dqqN3gwxsYg9hltWG-rWa1OPD6Ljx3P3rRKzw1M-7ex8AasNYdPQDpoHq-Kk8vGNQmui96jJGPmzewVQ_Tvx0OkS4SbPdD0hDfvtJ_MY-2LYQi2O7lCH3d8Xd1rUNQE3UdcPvoSSTFc-jNCLzpFUZc-iI3cX73PF0pgLWIibfKyhVRTWa87Bk4WBxFWfi5vgfGBR0Ip4tWSzL1mPsZDLaCaJ_lBxCNP9JowW0FarCmXlU2gh-SLD7mJYsf4o5JgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با چند حرکت ساده قوز گردنتو در ۳۰ روز درمان کن
🏃
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/696534" target="_blank">📅 08:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696533">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
فوکویاما، نظریه‌پرداز سیاسی آمریکایی: ترامپ بزرگ‌ترین تهدید علیه دموکراسی آمریکا پس از جنگ داخلی است؛ جمهوری‌خواهان مجلس نمایندگان را از دست می‌دهند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/696533" target="_blank">📅 08:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696532">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da0788c0ee.mp4?token=BA-e3luV2eQpgphYWluugviHDiOgXVizY8bwrnzrGSPTs4DgqYxeiGxcfddPeNA9yil2knKmqhopKhzKb_M9WcgxHDVeG3ry36yHuUTzJuxIGcjVKcWDBkNacnN7rGNHwl4BPi4mjdsAfHHeagc4pZlrC1uUOMJU-BY5RVQtVe61lXcg9QEUr6pVhOyp7FMJwFmDfjhsrVKSX_i8_O6PSekwNojMeHXjAPZGVcLPRMSyLBQsIB9nCUK97LEotCTcz_60UTUgtouMLd6tWhLb1e4u7TWAnNxSz6K4I-9_pW049CO7hoKMofi5OZGkYeePw93xSuAyZI_0y_vP3qWPWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da0788c0ee.mp4?token=BA-e3luV2eQpgphYWluugviHDiOgXVizY8bwrnzrGSPTs4DgqYxeiGxcfddPeNA9yil2knKmqhopKhzKb_M9WcgxHDVeG3ry36yHuUTzJuxIGcjVKcWDBkNacnN7rGNHwl4BPi4mjdsAfHHeagc4pZlrC1uUOMJU-BY5RVQtVe61lXcg9QEUr6pVhOyp7FMJwFmDfjhsrVKSX_i8_O6PSekwNojMeHXjAPZGVcLPRMSyLBQsIB9nCUK97LEotCTcz_60UTUgtouMLd6tWhLb1e4u7TWAnNxSz6K4I-9_pW049CO7hoKMofi5OZGkYeePw93xSuAyZI_0y_vP3qWPWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دیشب در جریان سخنرانی‌اش برای اولین بار با هو کردن بخشی از جمعیت روبه‌رو شد
🔹
همچنین دست‌کم ۱۲ معترض از تجمع او در سن‌آنتونیو توسط نیروهای امنیتی اخراج شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/696532" target="_blank">📅 08:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696531">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3051984f8.mp4?token=mKqGBHLz9VYL44bcmbkWb8kWOIywTfA6AOJn2t_5MRKWkCz7LzxqW0wpFDrjiSuhkwO2SAAcpoPFeFrU8qJj2I_W6H0Fwa1wx262nHTUtmIQXSmzMbOvPnngpXG8baQE2_lyULJFQUnqwyjMPYlpn17BHWlF9vVAHh68bgkrqBZsStaKIr6jNHvbyfTtzy3lnhPgKuGOD5Pp01VYQS8vxPOj6TYSdLgb-4doC0wmKgdkJwweG5hG48UBwifHU8NPcwngKkRmWqQgK_FJ43NsDQ5-oRRn6d5JlfQw9Heccil91GFV0FtIxjDT0CZCHkDz3eKnq1GLcE1Y9HRLpZnthgQZrGs6h09mGhy4R3WMA5ANxEVPU0jaasHSnkf0NOqVWLwTeKRxdhw2p2jhKKvWqTD-Od4qm4w5JB_EVqk-UKgGafZOO0ENi7GC7fnz1psNc3wAEC_n8vwC748xv4ytrCwB1NObRbzp6qsXgKsV5_tSlqIXY8KeJm_8HmWrLAM_9WvVLuB9mvDZZIEv78GhJebO_-Poxis2GGSlTd8oI3ESp4eTsalNftGHstGPbY7FQ-GJuJMaAOSGAeuxLq9TUKY_3Nu2MHzGNu7yd6cEGDw7yT0qi0mLP70kcnoh-FBJ85xYOHYlp1haAvX2Ym79sOSCcVhm-tvmVPiW3PP-DIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3051984f8.mp4?token=mKqGBHLz9VYL44bcmbkWb8kWOIywTfA6AOJn2t_5MRKWkCz7LzxqW0wpFDrjiSuhkwO2SAAcpoPFeFrU8qJj2I_W6H0Fwa1wx262nHTUtmIQXSmzMbOvPnngpXG8baQE2_lyULJFQUnqwyjMPYlpn17BHWlF9vVAHh68bgkrqBZsStaKIr6jNHvbyfTtzy3lnhPgKuGOD5Pp01VYQS8vxPOj6TYSdLgb-4doC0wmKgdkJwweG5hG48UBwifHU8NPcwngKkRmWqQgK_FJ43NsDQ5-oRRn6d5JlfQw9Heccil91GFV0FtIxjDT0CZCHkDz3eKnq1GLcE1Y9HRLpZnthgQZrGs6h09mGhy4R3WMA5ANxEVPU0jaasHSnkf0NOqVWLwTeKRxdhw2p2jhKKvWqTD-Od4qm4w5JB_EVqk-UKgGafZOO0ENi7GC7fnz1psNc3wAEC_n8vwC748xv4ytrCwB1NObRbzp6qsXgKsV5_tSlqIXY8KeJm_8HmWrLAM_9WvVLuB9mvDZZIEv78GhJebO_-Poxis2GGSlTd8oI3ESp4eTsalNftGHstGPbY7FQ-GJuJMaAOSGAeuxLq9TUKY_3Nu2MHzGNu7yd6cEGDw7yT0qi0mLP70kcnoh-FBJ85xYOHYlp1haAvX2Ym79sOSCcVhm-tvmVPiW3PP-DIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ توصیه ساده جیمی دایمن، مدیرعامل بزرگ‌ترین بانک آمریکا برای پیشرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/696531" target="_blank">📅 08:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696530">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
جان‌باختن خانواده ۱۱ نفره بر اثر گازگرفتگی
رئیس گروه کنترل و تضمین کیفیت سازمان پزشکی قانونی:
🔹
استفاده از بخاری فاقد دودکش یا غیراستاندارد در فضای بسته، عامل اصلی مرگ با گاز مونوکسیدکربن است.
🔹
۱۱ عضو یک خانواده که در خانه پدربزرگ خوابیده بودند، به دلیل نامناسب بودن دودکش بخاری، از پیرمرد ۹۰ ساله تا کودک ۹ ماهه جان باختند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/696530" target="_blank">📅 08:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696529">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7205ec1c32.mp4?token=qUtaNBpHNmkDJVW2Qq0kr3G1Pi2TbIxnEocpO2YqaCdWK63sVbxW2-S--_AaSRYXU6LPGfEc5Wuvb0Q8vDrsEWsLmAsLhn3YKyBFp8YnEv8H52ohr5bS1DCJWHePJzeLemJDIe6a3KWtD3D6tJsTfHJ51ag5xQ5pbaz2ZLUZsEOxUncbVjrbUYHeiT7aYeF4vZgSNMThSABMTdoorGEF5Wr8HXng_R4uVY8iyLnWn-yB_lcW6q9aRRMhZUKtuhe3-aHnNo6HrZIimXNJ_esUSiEaJZ7SGTKXKsU2TXPpyz5Ji0zLfKpxehMpCZvQw4MLSyROmJflACrJtHH7GlhaFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7205ec1c32.mp4?token=qUtaNBpHNmkDJVW2Qq0kr3G1Pi2TbIxnEocpO2YqaCdWK63sVbxW2-S--_AaSRYXU6LPGfEc5Wuvb0Q8vDrsEWsLmAsLhn3YKyBFp8YnEv8H52ohr5bS1DCJWHePJzeLemJDIe6a3KWtD3D6tJsTfHJ51ag5xQ5pbaz2ZLUZsEOxUncbVjrbUYHeiT7aYeF4vZgSNMThSABMTdoorGEF5Wr8HXng_R4uVY8iyLnWn-yB_lcW6q9aRRMhZUKtuhe3-aHnNo6HrZIimXNJ_esUSiEaJZ7SGTKXKsU2TXPpyz5Ji0zLfKpxehMpCZvQw4MLSyROmJflACrJtHH7GlhaFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سفیر آمریکا در اسرائیل: در غزه نسل‌کشی و آپارتاید وجود ندارد
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/696529" target="_blank">📅 08:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696528">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05c961e8d3.mp4?token=j5r0dLBFaXSAzOBoikzV5IfddY-SB9ZvNVEeToYwqRLAKqBkBfd5qo1vYSnBFEy11OYyDEYffztd9pnCv7K45YrMw2oLhN2C2-YF9yiCko_wgyfk-XSC8z_6Hv0RnqZMhbD1lNAcAjtNZzCkj9PznaY9IEnKNT2U55N03W7IOUhbs3ixGofwKJIQIFPq7PqN4z3TCHjzl7V2oTuHd0erMJYxv_QHZCNEESjv4rmePKq0NGX77GbvyxAOLN6SFP8I_Xx6BhkvUK66mg4FCrgHLfEoyaFa6q1AqhPptpz6tHwCkjdOKKlUXsyBGTnXWxfAgSUN-QYZykD4qgYeMH9uMisw84k_M-WqAHf1vn-Bzhxq7Kg-Ksi03-2wActRw_VotvDJDxTKWU-m-PlDzWFguF5PIg5FEBRMIHvZIBbpyT7cIbhhsENOKQov6Pqdz634Gvyzs2kFXun00jaxGM4EveesD0YWDiptwShmYRSDdQj8kNqAmDvgddasclAKbdTmw49VLS01widntJgwi7Y63-hCkc2Ch3B-Y-D5CaAUApbdD-9F65M5-XS5WPfqF4WIboWfDC8fJTaH0wOhkwBxvGX2Ews7th82zl0aydM0R0MAICHJ63mqBVawwjJCpOot9Lyox4APSb-t1VuwRTv2jmNsyBycfE99lWFZ2wvLcEo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05c961e8d3.mp4?token=j5r0dLBFaXSAzOBoikzV5IfddY-SB9ZvNVEeToYwqRLAKqBkBfd5qo1vYSnBFEy11OYyDEYffztd9pnCv7K45YrMw2oLhN2C2-YF9yiCko_wgyfk-XSC8z_6Hv0RnqZMhbD1lNAcAjtNZzCkj9PznaY9IEnKNT2U55N03W7IOUhbs3ixGofwKJIQIFPq7PqN4z3TCHjzl7V2oTuHd0erMJYxv_QHZCNEESjv4rmePKq0NGX77GbvyxAOLN6SFP8I_Xx6BhkvUK66mg4FCrgHLfEoyaFa6q1AqhPptpz6tHwCkjdOKKlUXsyBGTnXWxfAgSUN-QYZykD4qgYeMH9uMisw84k_M-WqAHf1vn-Bzhxq7Kg-Ksi03-2wActRw_VotvDJDxTKWU-m-PlDzWFguF5PIg5FEBRMIHvZIBbpyT7cIbhhsENOKQov6Pqdz634Gvyzs2kFXun00jaxGM4EveesD0YWDiptwShmYRSDdQj8kNqAmDvgddasclAKbdTmw49VLS01widntJgwi7Y63-hCkc2Ch3B-Y-D5CaAUApbdD-9F65M5-XS5WPfqF4WIboWfDC8fJTaH0wOhkwBxvGX2Ews7th82zl0aydM0R0MAICHJ63mqBVawwjJCpOot9Lyox4APSb-t1VuwRTv2jmNsyBycfE99lWFZ2wvLcEo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از راهپیمایی تعدادی کفن‌پوش که مربوط به روز سه‌شنبه و در تهران است با واکنش کاربران فضای مجازی مواجه شد
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/696528" target="_blank">📅 08:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696527">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
دبیر: دوستان نترسند من علاقه‌ای ندارم به فوتبال بیایم. برای ما دوم جهان شدن باخت است ولی برای فوتبال جزو ۵تای آسیا شدن آمال و آرزوست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/696527" target="_blank">📅 08:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696526">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7edaa3ac25.mp4?token=f5mT4wOaSfcdSygWvmcG5VcWAtT54q1vQX2DRNQ0RRWSQ21-aTuL1P03pHgQhhO_vxpD-xFyXJcv1FBza4eiJFjWvoQo5u-egNsM8H4c5RnBZfHoRK5G0vT8bP8BR6G0hxI2BSpONsp9i9kEvHkISD3BuYKQWLVN6fu8Ek19Ga50KfYv7CBmbTGBgJ45lezR5eeMPJ4sl2e1BygGYvfDCr_oBfnjtDJgAjzWaKRu_6t37SVnUQE4sFyrHn2nZvQDgRn2N4Vv9EYfvyJURE6S3ka12x3oWR8QbDK7XMUgHWYOuO9hTjZLCpdVxMeDtnH9GEW01pR6-KjL_OwOQU5Q8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7edaa3ac25.mp4?token=f5mT4wOaSfcdSygWvmcG5VcWAtT54q1vQX2DRNQ0RRWSQ21-aTuL1P03pHgQhhO_vxpD-xFyXJcv1FBza4eiJFjWvoQo5u-egNsM8H4c5RnBZfHoRK5G0vT8bP8BR6G0hxI2BSpONsp9i9kEvHkISD3BuYKQWLVN6fu8Ek19Ga50KfYv7CBmbTGBgJ45lezR5eeMPJ4sl2e1BygGYvfDCr_oBfnjtDJgAjzWaKRu_6t37SVnUQE4sFyrHn2nZvQDgRn2N4Vv9EYfvyJURE6S3ka12x3oWR8QbDK7XMUgHWYOuO9hTjZLCpdVxMeDtnH9GEW01pR6-KjL_OwOQU5Q8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر ایران جنگ رو ببره چی میشه؟ پنج روند تغییر میکنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/696526" target="_blank">📅 08:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696525">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ترامپ: ویتکاف برای دستیابی به توافق با ایران تلاش می‌کند و پیشرفت بسیار خوبی دارد
🔹
به زودی از ایران خارج خواهیم شد و خواهید دید که قیمت‌های نفت به شدت کاهش می‌یابد و به دنبال آن قیمت کالاهای دیگر نیز افت خواهد کرد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/696525" target="_blank">📅 08:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696524">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ان‌بی‌سی به نقل از یک مقام آمریکایی: ترامپ پیش از انتخابات میان‌دوره‌ای، گزینه انجام حملات به ایران را با تیم امنیت ملی بررسی کرد
🔹
واشنگتن و تهران در ماه جاری میلادی در نیویورک، طی مذاکراتی غیرمستقیم درباره برنامه هسته‌ای گفتگو کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/696524" target="_blank">📅 08:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696523">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6b48213b3.mp4?token=vwo27_rIt7UQZk999NYUPazpprKAV5_DwLfceZs-7w7wMljug8w-isH0XPjQhJA6lxka90YFS2CttLC48M-6Iii3BiUTVT5DKv8x6jyDXp9W7UQtJoYwjAsOSjouNcb82aCoMf5VbOZjhd5sn6pkyveqqEhDfrVxMyml7RmvaJO-CYAoJ7XbxTs7e13H_19tAmhkhdpH9Jf9iqg2I7tkkzSmj0f8tl78vyXxOs0lorqe4XNg5xWPxDe2EWnJdyl_MuuE7nve5AviGW_YkMKmbT3RVr2DGN6DASuq6L3UJuNJukgez-iv_ScsTLFijxhkQ4TibeEXJ4shTN6V4rbmPXs62N5XLJRPtxHB1jpVp1K2aasl5moQ7jEpUK7JkM_220uGaXd5zXgNfvrLztswB7oRBRxLtJFyOnsND4hVfl-YF84cWMxp6bhlFmBwd0SAwoOUEnWTl9N7Y2mX7fzLnJ-f0XoETdp1Huro_Bw0z5RKYFTqxtoUTDa4ezQQCYAMp4tZ8ftEpNfXz65z6KKPvQpuk_GnCnElg2WmXXxTwUR6WFlTp7OjqkYCCZQZfAs6_IfyuwDlh_PE6Na096zThFyAGE8OnlrglDiMtf1lH73IZFNYmhg73eQNAGfQbpm1g3Qhb4zvOCqOzyixTVgFWliV7xFkZqyAWSSgHSXb1Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6b48213b3.mp4?token=vwo27_rIt7UQZk999NYUPazpprKAV5_DwLfceZs-7w7wMljug8w-isH0XPjQhJA6lxka90YFS2CttLC48M-6Iii3BiUTVT5DKv8x6jyDXp9W7UQtJoYwjAsOSjouNcb82aCoMf5VbOZjhd5sn6pkyveqqEhDfrVxMyml7RmvaJO-CYAoJ7XbxTs7e13H_19tAmhkhdpH9Jf9iqg2I7tkkzSmj0f8tl78vyXxOs0lorqe4XNg5xWPxDe2EWnJdyl_MuuE7nve5AviGW_YkMKmbT3RVr2DGN6DASuq6L3UJuNJukgez-iv_ScsTLFijxhkQ4TibeEXJ4shTN6V4rbmPXs62N5XLJRPtxHB1jpVp1K2aasl5moQ7jEpUK7JkM_220uGaXd5zXgNfvrLztswB7oRBRxLtJFyOnsND4hVfl-YF84cWMxp6bhlFmBwd0SAwoOUEnWTl9N7Y2mX7fzLnJ-f0XoETdp1Huro_Bw0z5RKYFTqxtoUTDa4ezQQCYAMp4tZ8ftEpNfXz65z6KKPvQpuk_GnCnElg2WmXXxTwUR6WFlTp7OjqkYCCZQZfAs6_IfyuwDlh_PE6Na096zThFyAGE8OnlrglDiMtf1lH73IZFNYmhg73eQNAGfQbpm1g3Qhb4zvOCqOzyixTVgFWliV7xFkZqyAWSSgHSXb1Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر CBS از ویرانی کامل پایگاه آمریکایی «عدیری» در کویت پس از حمله ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/696523" target="_blank">📅 08:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696522">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ادعای اکسیوس به نقل از مقامات آمریکایی: پنتاگون به سنتکام دستور داده است تا مقدمات ازسرگیری عملیات در ایران را نهایی کند
🔹
از سرگیری عملیات در ایران می‌تواند شامل بمباران اهدافی در تأسیسات انرژی، زیرساخت‌ها و هسته‌ای باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/696522" target="_blank">📅 08:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696521">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoFfMOMfkjK7NahqOOBj4lw03VoJXsWabIhq7OriwUMfnbnuMrvS7PsWQ0-l1LeI4hIhTwvoc9w0daiIKUO-VODztSkcACsBQbFxfUMQsFAgbL_nVchIqLnViqPFcTMnjwODI7WfGHRJs2SevLTJny8m6e-V6goakbvSInNKIy1jLpQJPwZd4qsglzHr-Ov9KO4tU-0a-OLW2wHUmME2ppCeaNbpJpHFkS__40SvrW9xGQE8NHu5lvEl6Gzd6_h0zd349Imcm59HWm_k4q8Oc9zwwxuUh9rP_mhtvYCn3M99wlypqdM3Ap1ufwm0gdB2ElPr9wRxC6bwWjqCk1mBag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۱۶ مهر ماه
۲۶ ربیع‌الثانی ۱۴۴۸
۸ اکتبر ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/696521" target="_blank">📅 08:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696520">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار مشهد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0SchuJoy8eIkdsOD-e-zj-YY6sm3yhVpeSB5SDomdhBY-cX2vA9zscRFQtaZ55gtN87gIFRj0M76_1227nm-EfzEIaFJslFFIEkQSjG3sAOU-bHSicC16ABH8Cmhx9FwOITsvMMIpEB9e9DnaCYzmsVujTRhaR4TG_nCMZF8tZJTmtq14fD14md1W0bquTg4eTSZiWOYgqXu_lk33io7mJJ_DK2e1Y5z6nr6PyNEYYPP6ljC97jA4_jdr4TIGqQ9SXAPZkO_gHxNzJoBne7S3MWRMZArWqf4bz_N6qqTY4AbWGUu819jVa01m7omlqecM4y_l0nfNh0DRmzK7dJfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تک رقمی‌های کنکور ۱۴۰۵
موسسه عارف
🫡
💡
فقط درصدت مهم نیست
💡
جایگاهت مهمه !
🎯
هم مسیر رتبه‌های برتر
🎯
از همین امروز شروع کن
💪
موسسه کنکور عارف
🫡
| موسسه رتبه ساز | کل کشور
کنکوری داری؟
پس این لینک رو براش بفرست:
👇
https://t.me/+xVKhaZN3zi41OWZk</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/696520" target="_blank">📅 00:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696518">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VG09MRnSgGZtnVOuFxRJDowGsRia97fYhHIsJNYSnbeBUFeMA7V_bSTD-wIQUywn7hMXhN64BERCsn03kHYdwvq_puFVK3oMKLz9drni7t80Y6ronLRgwr_akdlqrYJ5G3JLZhmuYGSoW6feBBtGLGHyDshjkuTOsH2eqjnWLfQCRIuUy14OfRM_VTWPXT98ii2aunMY_KNoNQygJTJc6u4ihSMVTD762IExX-LeCLi3lQjuPJHLXeSJ4FPJ9AITQIWNj1hiWoXA3_ulzKe0qoYkU-dO85qn7FQrLGxfECCxZjwyIjDLpWbXaqUFaGhXLENEo08RWX7VdLtepPyQuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11af97c4e9.mp4?token=oFVjD0ep9YV7Rw1s6rGz_Q42Dcp6T_NF1ZVl8XgA5wvE3SPnDizVX5_1alYyTZwhkf_i0j35AFHfTZ2wCvdlszf9oc3b__85JzISnm3IEOQ94_0smEjZ9QTODtJOymHSFKAjyqd45zCw3nouIGbhs8Nthl3s2elIVNIPYkRXQZ_5y5IelDQ4T1EalPJfbzFrvFhA1kchMmhcar4M1OAjN867zLp4-B1xclU3bse9GX9iAe-PQPN_JqDs-h9mfVAwwSIUfo06_Nw3TAyYw-vhgEDJRaCPCcMtJCt58JExnZLksTgmEAXcQ_h4cdfth82FZLrSBUSxcnKOgNaIXQVqDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11af97c4e9.mp4?token=oFVjD0ep9YV7Rw1s6rGz_Q42Dcp6T_NF1ZVl8XgA5wvE3SPnDizVX5_1alYyTZwhkf_i0j35AFHfTZ2wCvdlszf9oc3b__85JzISnm3IEOQ94_0smEjZ9QTODtJOymHSFKAjyqd45zCw3nouIGbhs8Nthl3s2elIVNIPYkRXQZ_5y5IelDQ4T1EalPJfbzFrvFhA1kchMmhcar4M1OAjN867zLp4-B1xclU3bse9GX9iAe-PQPN_JqDs-h9mfVAwwSIUfo06_Nw3TAyYw-vhgEDJRaCPCcMtJCt58JExnZLksTgmEAXcQ_h4cdfth82FZLrSBUSxcnKOgNaIXQVqDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💆‍♀️
خستگی عضلات رو به دست خودت بسپار!
⚡️
ماساژور تفنگی شارژی
JIHAM
؛ یه همراه حرفه‌ای برای بعد از ورزش، یک روز پرمشغله یا وقتی عضلاتت حسابی خسته و گرفته‌ان.
😍
▫️
۶ سطح سرعت قابل تنظیم
▫️
۴ سری ماساژ تخصصی برای نقاط مختلف بدن
▫️
شارژی و قابل استفاده بدون سیم
▫️
سبک، کم‌صدا و مناسب خانه، باشگاه و سفر
💰
قیمت نقدی: ۱,۵۹۸,۰۰۰ تومان
🔥
الان بخر، بعداً پرداخت کن!
💳
امکان پرداخت
قسطی در ۴ قسط
بدون نیاز به پرداخت کامل مبلغ در لحظه خرید
😉
🚚
پرداخت درب منزل
🔄
ضمانت تعویض ۳ روزه کالا
اگه دنبال یه ماساژور کاربردی و حرفه‌ای برای استفاده روزمره‌ای، JIHAM می‌تونه انتخاب جذابی باشه.
💆‍♂️
✨
https://memarket24.ir/product/fast/64852/180124/</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/696518" target="_blank">📅 00:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696517">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDigikala | دیجی‌کالا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4xBWIFzFabFHq1jKFQFIZ_rFaIZVGV_ixfpCHnsfiF-C7Dy_VbKFVuPlnYrzDNGlowPuR3m2LoToob55k8OtO_KhAZUTp0710SQKNxQMlX_PjPvMtVyIKqRM6DHADjmQqi0JRYTaguHj1Px7247unou48PBRFvX3kHRkjLWZVpQ4gRwl4-t7VvPes2IWfnWpnXW7dwrBcOo49GWboI3w3XQ6BmHfELDeAf79GoohQieiuWjSZ8rHoVYXiMXHNFZJF8h8Nj84IR90tMh7snLdny0NLyQ1Llrw41A1X0VhqdBc-eaP9Yq5bsC1S5dWNBLqM0-LPkjjrk0Cmx5rHvYtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با اشتراک پلاس بخر؛ آیفون ۱۸ ببر!
🎁
⏳
فقط ۱۵ و ۱۶ مهر!
🛒
هر خریدت از
دیجی‌کالا با اشتراک پلاس
، یک شانسه برای
آیفون ۱۸ پرو
علاوه بر اون، با خریدت
۱۵۰ هزارتومن طلای دیجیتال
دیجی‌کالا هم میگیری!
✨
😊
پس
وارد لینک پایین شو
، هم تخفیف اشتراک پلاس بگیر، هم تخفیف خرید کالا!
👇🏻
👇🏻
👇🏻
➕
از اینجا خرید کن
!
🛍
✨️</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/696517" target="_blank">📅 00:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696516">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qu0YFvZEArpXoSVD80H6mkMAivegjCFoooYXSIH5jmmCiTuEArDe84UwryMtG-tFnvO_a8wNeKUKaZ7UraifeQnYfmeV7W9zyK88tHy-TS8frKlDc5Xbc7pIt3GVeVgrnf215hPPQ78PnCVd52uNY7hDcBTqkI0P5_dFmsvVVEdAnjKe0z0bAzjwNt6ajLM2xjfDJxtDEVqkvTOpSkTITsf9dIbQ3f_CUavV_DqLpukTTmlop7-gkETGugZOXoIzBGTQolCsEQ9Cj6NF0ZtaY19wUHjciNspPJMN9qQ_a8Q1naZTXHEO8mzboNtriNqmuaGBSwD0l2QfieX3LXI42Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با دکتریاب، دیگه توی صف و ترافیک، نوبت دکتر نمون
🌟
تا حالا شده برای گرفتن یه نوبت ساده، ساعت‌ها توی ترافیک بمونی یا پشت خط اشغال مطب کلافه بشی؟
ما توی «دکتریاب» اینجاییم تا این مسیر رو برای همیشه کوتاه کنیم. فرقی نمی‌کنه دنبال نوبت حضوری باشی یا نیاز به مشاوره فوری تلفنی داشته باشی؛ با دکتریاب، پزشک مورد نظرت فقط چند کلیک باهات فاصله داره.
✅
چرا دکتریاب؟
دسترسی به لیست بیش از ۵۰ هزار پزشک متخصص
رزرو نوبت در کمتر از  یک دقیقه
امکان مشاوره تلفنی با پزشک، بدون نیاز به خروج از خونه
صرفه‌جویی در وقت و هزینه شما
دیگه لازم نیست نگران شلوغی مطب‌ها باشی. همین الان وارد دکتریاب شو و سلامتی‌ت رو به زمانِ ارزشمندت ترجیح بده.
🌐
همین حالا نوبتت رو رزرو کن:
https://doctor-yab.ir</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/696516" target="_blank">📅 00:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696515">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a492ad0ba.mp4?token=p7SlpYvWF2p8RSdAQ3uRqc3t3em4bf3v_3OpJNr42AwunJAXmBdeIvAv4YrDvT6U-PParOxHO2Lsi2QOMMjWj5fk246A0ObOX66-aTwE8InkxgzEITcEBmL4358_WNOmOUZP-mxuEAkOuzPcipwRvAchDc9k41hXPR1gEzdh209nAb89mSwE9TbjY2R9fHqxg17yNkBUWfvp2jKETcXGmDTKoyt81lzkjIKv9jYg7NQbEPWTA19RiBlmYmjM6IHAcF3zJdmYgWvL9E7ZH0vxkhJHFSe6XYGimZd-czfL4X6dd6nZUZoppiElcqCiVgVjI3wszkQALZWOzfCLLJLyWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a492ad0ba.mp4?token=p7SlpYvWF2p8RSdAQ3uRqc3t3em4bf3v_3OpJNr42AwunJAXmBdeIvAv4YrDvT6U-PParOxHO2Lsi2QOMMjWj5fk246A0ObOX66-aTwE8InkxgzEITcEBmL4358_WNOmOUZP-mxuEAkOuzPcipwRvAchDc9k41hXPR1gEzdh209nAb89mSwE9TbjY2R9fHqxg17yNkBUWfvp2jKETcXGmDTKoyt81lzkjIKv9jYg7NQbEPWTA19RiBlmYmjM6IHAcF3zJdmYgWvL9E7ZH0vxkhJHFSe6XYGimZd-czfL4X6dd6nZUZoppiElcqCiVgVjI3wszkQALZWOzfCLLJLyWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معین در آخرین کنسرت خود نه تنها اجازه ورود پرچم شیر و خورشید را نداد بلکه قطعه «حماسه خرمشهر» را هم اجرا کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/696515" target="_blank">📅 00:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696510">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YdkHRtj4svaH8QfisUAsFQMdOExtAq2HqjJMLO1lbj1F8t53HFvGIyAKe9KQmO6irZ0oBNGb9A3-sgJYI1PdLPGJenByndEx5kLFymHLzWKzXqaCGdOFo84_mNb7PYkfsinyXKQ-9c5Urt_vOLO0P-7Um7uAjZdiAgA2-oQcXRHhe1MRsA2MQ4_ucdK9wXYqCi6fxfbdwuaJwWa1At_uuisKyX5f58LHG2_4Ss2K4oHDOi9w7Q9tKnvsZTeP-uHqwmtmEPQcU-vRjFwjvhIfA5qxsHrYzgcQZo5UV8pCNGk0bjSZS48qs-mDPU5jQMYExyGV7M6hM-WSaYbTN4bAPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZoUBlOyK9_QFqpMT8QY5clBU8hIiFuIIHZWDT1rU5lrvuFCT7WWN9ikD2qwYAADC5i0suZh6kT-Cx-gH5xgLsp4u5yAR3tQOBSf345XFG5HlFv16l8JmL016CmxvSvkb0BmdUA8Tg7LUGNLGxBWSvUQe-ZnotodAurxhJvjAfE-XuKX4nMdf0gh_WlRNx2yqNRaxUPLPn0OpOISYgJNUHIzpmbkvvFDJZaHK7my4x1pAEik3beZW5S7ySdWQE-29UWaeuFTfm2aGx4E-aiQR3mW164Qku84vX-jmI6xh8vQtZwbfneiHFyUBgaaAHX013n2QjltN-d4INUj0Ye1emA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RZZPJLrQyCtwijk9TTTt9Jevdi7LkLy3scL3AjQRoiPzBKikudOGDRhjwjqg5Tu7JTpEH1ePEqXVqdT44D3v-3OubdwsSoXbjLx_y0jfyuRU3s2q0HUw76VZ12QtbTbo1VSmer7fq94iBcxa6K4qHGJh02mHDPH4RERzk6WAWxLRCZkwpz1nts2R47-A1aMJIFIsE2KQsD3Z-YYIP97GkH40mAceNKdRj4HMosvSmiOXvHxd7hitjnLrYb4ZbgmSmK58n04PhQizJ5SS74ZNTl49nDca6jRwgcMVQEJJQnSSAAbpySfKb3qiNZ8aKh6nQdh7XWQDgJJ0pBmT2Jb4iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkNfkpLP8RzlXhKcGjEBDSJNw1ui27wB7gE0Ugv03j6tbazikkeCM1ZYKMNBmYq31xCUypte_U120XHoOIBzR9ZCrzlx24bCkOS4XEhjPTmYhwm9h_pb-ai4NTZasKBfhGDxcK8jcYj7uVa9yqO2ZHBEQ28XK41GRcxizj_LPn_vQ5vJTqvDTiNsvhdSDNgQayeiRvIKZJ7hnoZMKBDgEuX8bS3axfOh5rRzCR8naTmZUmurWKRQHn1qcbqoI_jN8KZmg59k19fhW4u9BMvQrtVTJstY67sr8S6U0bKbEZawnPQD6LX5a3aK-fHyXU-NKGJZ-zYqxzujp47VhW8erw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ناسا یه سحابی بزرگ به شکل قلب پیدا کرده؛ این سحابی حدود ۷۵۰۰ سال نوری با زمین فاصله داره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/696510" target="_blank">📅 00:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696509">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ایران و عمان درباره مختصات جغرافیایی مسیرهای امن رفت‌وبرگشت در تنگه هرمز و نحوه اعلام آن در مرجع بین‌المللی مربوطه به توافق رسیده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/696509" target="_blank">📅 00:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696508">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58ee5495d8.mp4?token=dP6wMby9lGSqALwdXLs3esEP-oaBk4GHgRPMwP-i8EcpX8Tdq8rSILwghv4ABSkh5qJHulrvcn8uSHduvA1c48c_p_Gf-_4ZkDfcdQc1reGAxOLYuwFVy-uSOc95PZUhBCsscsuBRntGFjKS2GwaRyUwT4KR8OPCjFLYaHqK53bMYJHQr_Q5U7NPoGC4clBX7wX3emGj7aq3iPZdkZdFGsSk_6oOZbI7NMrxSajy4r2rLX0hKgM83R6i0TXKNK26XC5-7YuVRT9RpQCcRFl5Rv64xLTzFGvniMED9iDWcrikLa7KAyVG5Y2lGmxp3BLXgKzIcOEg9wURtqLA5ELvew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58ee5495d8.mp4?token=dP6wMby9lGSqALwdXLs3esEP-oaBk4GHgRPMwP-i8EcpX8Tdq8rSILwghv4ABSkh5qJHulrvcn8uSHduvA1c48c_p_Gf-_4ZkDfcdQc1reGAxOLYuwFVy-uSOc95PZUhBCsscsuBRntGFjKS2GwaRyUwT4KR8OPCjFLYaHqK53bMYJHQr_Q5U7NPoGC4clBX7wX3emGj7aq3iPZdkZdFGsSk_6oOZbI7NMrxSajy4r2rLX0hKgM83R6i0TXKNK26XC5-7YuVRT9RpQCcRFl5Rv64xLTzFGvniMED9iDWcrikLa7KAyVG5Y2lGmxp3BLXgKzIcOEg9wURtqLA5ELvew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظاتی نفس‌گیر از نجات یک غواص که پس از شیرجه زدن به زیر یخ، تنها چند ثانیه با مرگ فاصله داشت
🏊‍♂️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/696508" target="_blank">📅 00:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696506">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcqFa4ahfOSZXKhCNBhajbB9EkXsxmN5wjeuy-1JsgNXlVQrRzCBC2KBLC0sLnPExLOcQg3GDPJ6SFtDzGiKm29g0LXEAAEODBM_sg1UZkOkEgCodnx3UpBNX5cMdgsQdSFwFxb6_CAThXF286mhPjrkdBm0u_rvPG8x638X_722is-ndPLyergVSccC7k-8r27TlDjUf693QIefIBCgcyXPlXA04qCTYw5MuIRcGuEujhfrOaqiiWQ9QvB8eXXUJ0spmgm23qKLKYvVTAIwKT7SU12lzrBf9iXk5RT-U3Shqo_ZNDY77ZwGSnNOvK9qwqAdDgQj3sqLS9AvfjKRpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/696506" target="_blank">📅 00:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696504">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
خبرهای جنجالی را در وبسایت خبرفوری دنبال کنید
🔹
🔹
لیست ۱۰ نفره سیا از مسئولان ایرانی؛ اسرائیل نباید این افراد را ترور کند
👇
khabarfoori.com/fa/tiny/news-3250587
🔹
آمریکا شروط تازه‌ای برای توافق با ایران تعیین کرد | ونس از غنی‌سازی عقب نشست؛ پنجره توافق با ایران باز شد؟
👇
khabarfoori.com/fa/tiny/news-3250718
🔹
رتبه فرزندان مقامات ارشد نظام در کنکور؛  رتبه پسر رهبر انقلاب چند شد؟
👇
khabarfoori.com/fa/tiny/news-3250579
🔹
خودروهای برقی در چین چطور کار می‌کنند؟
👇
khabarfoori.com/fa/tiny/news-3250764
🔹
زنگ خطر «مرگ سیاه» در ایران | طاعون زیر ذره‌بین وزارت بهداشت» | نگرانی از طاعون روسیه به تهران رسید
👇
khabarfoori.com/fa/tiny/news-3250513
🔹
صفحه اخبار داغ خبرفوری را اینجا کلیک کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/696504" target="_blank">📅 23:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696503">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lT7tqOiXt64su7SUlRJIVCHyMTrFcXpT44aUIMir4W2K5nKJhzV0MEEfl9KVLI2jkMe7zlA3tGiGByIE3ysWtZr7p5n82BycEMjrRg6Cl8uxex9gXKSemCnV3099n9Wr5jvDL5jYn_XRpeievpAvp-Yzli4kjEiFmwQ2YFm4SnIKM68M0tQ85zZGow3OSzAxu9H61H1pCg-5jQu_NrldNT_-gq7GxQlT4vm8dHl6gpkHtnTFXojnb_vcKKKM4n2ICE5bi0SN1caqxstTA4uttBZRvomLq_hFUPQ55KOrOz_d_4zpkxuC9Dnn6gIgN3tqnVzDdd44SN0ETugVdTv8RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیونل مسی از بازی‌های ملی خداحافظی کرد
🔹
لیونل مسی با انتشار پستی از فوتبال ملی از تیم ملی آرژانتین خداحافظی کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/696503" target="_blank">📅 23:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696502">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f129a9c7.mp4?token=l_MQ4Z7-hsZf-I3ak3AoBmctAHAJsYvMZl2TgqUy1olbWY2ejIVZHYkNwZXbA_1YeT-KPAQ2ZmxZq9aMNM4B85_Fp5mV5AofH_Wyqx-1ONBxIkRtso40n-T6Oh8lx5YedaEefejDaPpOJLUZvR1dRpD-CGOakhdcihAJL0kKjEBKycFpBZpc6XyZU8MDjVja7WAi-38qwgP2dhayp_boYXS6Qipc3IqIWzpeHt1RtB-sdgA0RN-I8Grrt_Nqb1yvl7qD_4UqPSKe52EMyhnqa9NpgtVzOPfWVj9KmiOOi3BSD0pqzmJLHGrXdjrHyyk9CtFK3UJ94kElZzVsFrO0iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f129a9c7.mp4?token=l_MQ4Z7-hsZf-I3ak3AoBmctAHAJsYvMZl2TgqUy1olbWY2ejIVZHYkNwZXbA_1YeT-KPAQ2ZmxZq9aMNM4B85_Fp5mV5AofH_Wyqx-1ONBxIkRtso40n-T6Oh8lx5YedaEefejDaPpOJLUZvR1dRpD-CGOakhdcihAJL0kKjEBKycFpBZpc6XyZU8MDjVja7WAi-38qwgP2dhayp_boYXS6Qipc3IqIWzpeHt1RtB-sdgA0RN-I8Grrt_Nqb1yvl7qD_4UqPSKe52EMyhnqa9NpgtVzOPfWVj9KmiOOi3BSD0pqzmJLHGrXdjrHyyk9CtFK3UJ94kElZzVsFrO0iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فقط یک چراغ‌قوه نیست؛ یک ابزار نجاتِ همه‌کاره‌ست!
🔦
⚡️
🔦
نور LED پرقدرت
برای روشنایی در تاریکی
🔋
شارژ USB + قابلیت پاوربانک
برای مواقع ضروری
🧲
مگنت قوی
برای نصب روی سطوح فلزی
🔨
چکش شیشه‌شکن
برای شرایط اضطراری
🔪
تیغ برش کمربند
برای مواقع ضروری
🚨
چراغ هشدار
برای افزایش ایمنی در جاده و شرایط اضطراری
🔥
قیمت ویژه: فقط ۱,۱۹۸,۰۰۰ تومان
💳
الان بخر، بعداً پرداخت کن!
✨
امکان پرداخت
قسطی در ۴ قسط
یعنی لازم نیست کل مبلغ رو یکجا پرداخت کنی!
🚚
پرداخت درب منزل
🔄
ضمانت تعویض ۳ روزه کالا
🔦
یک ابزار کوچک، با کاربردهایی که ممکنه یه روز واقعاً به کارتون بیاد!
👇
برای خرید کلیک کنید:
https://memarket24.ir/product/fast/30291/180124/
✨
تخفیف آخر ماه؛ فرصت آخر برای خرید با قیمت بهتر!
https://l.memarket.me/lp/65/180124</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/696502" target="_blank">📅 23:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696501">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7750f552b.mp4?token=Dk4Fho6R4wkA0Gwm6HhW2eJn5TR7mPYMJE1pIAu3jJct8ljsj1vfUvO51qloFZXxM300Zt10otgn7NXRTHh5Q0kzlDqnylZMhQseQhGeeOZsxz4ztzxM1JsN2Ognn4K76Pgfeh8LW_UkwU9cokhQF-idiNt-FkT9blsvPlgCXM3EVTvy0pCcfZyTp6lTr03BSkc1yZiI8nNMPLbClbjJKzY7ScHeENnZ5VwHKV2-kFYDSlH_NK51XBnX-OoTikKoxQI-m5XV7a2KhjIbxV2JqIpE2cnDOPBmnxMBPk26sJ2D_9O_f8rUWPp9WeB4PrVEDrMRlAQW7rCFY0wrAFYEhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7750f552b.mp4?token=Dk4Fho6R4wkA0Gwm6HhW2eJn5TR7mPYMJE1pIAu3jJct8ljsj1vfUvO51qloFZXxM300Zt10otgn7NXRTHh5Q0kzlDqnylZMhQseQhGeeOZsxz4ztzxM1JsN2Ognn4K76Pgfeh8LW_UkwU9cokhQF-idiNt-FkT9blsvPlgCXM3EVTvy0pCcfZyTp6lTr03BSkc1yZiI8nNMPLbClbjJKzY7ScHeENnZ5VwHKV2-kFYDSlH_NK51XBnX-OoTikKoxQI-m5XV7a2KhjIbxV2JqIpE2cnDOPBmnxMBPk26sJ2D_9O_f8rUWPp9WeB4PrVEDrMRlAQW7rCFY0wrAFYEhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی عجیب از خانومی که بخاطر عمل زیبایی ماشین خودش رو زیر قیمت بازار فروخته!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/696501" target="_blank">📅 23:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696500">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AicZW7m6qhz8eZwJfluGXHEEgPQHtR1ZStnGrJLN23jt6tc7X5eDT_oc9Q-Jx1CmvV3hWxLYHjeZQK-HNCYynHkQLZ9UNm_Zr0ywodXU6Xd9Hws3kB5IojJ9hvD3NtFRGD_Ujt2u0n8R_pAaKCSXwkvF62A2k1pY9nMMjDuy0rKPi2xF-fXSTJKEAIhQVYor5J5H1uqbAchf66If3GRD82Dv-M2lRlmq9GYfZHQbfdSZz4aAL2yxQnNrXr0Gbp1oAU2qxkEChkI0XYcYTY8BDQut0EdfwkUqERjpmtYLFHeC1ZE9ZfeiO_OLfWXdSBzA6Vc2HkgnvzC7qA6HCJ3hnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمای زیبا از «نوشهر» که بارش باران از کیلومترها دورتر دیده می‌شود
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/696500" target="_blank">📅 23:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696499">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U18-S33fFkFtNSCaaqn23lnXc7jvUNXyEBJC-ymYveoNk-dRHgLf-ANIzHOHKuSrFGBai5PlfbhLF42K4nMmOZdHnowmtwGUyolKGYi__aQ91s4vJxyP6uQByMdbStpBZPhXDRfGsUUKOM5JtsAPqYs2jSizDYWrcEfhFo9GiBlfqzOOyyNj-Vki1adKBJLCKZhzpl_otZum2mYjCl1c3QfK1h7J9j6xrji2VALrxXgu0ctM8PxOR4fq7TCDrrRkLlVhMZOHrHUOD-62QFQ0HvzPkouANDOtOuwJkxQouFhpAe85yU_NTqki1V2Lj5WHFrQ_Hv-wMnFMgVAjPxP0Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشکل اصلی آمریکا با ایران؛ علم و رشد فناوری است!
🔹
دقت کنید در جنگ، مراکزی مثل انستیتو پاستور، دانشگاه علم و صنعت، پژوهشگاه شهید بهشتی، پژوهشکده نانو دانشگاه شریف، مرکز فضایی کشور و تأسیسات هسته‌ای هدف قرار گرفتند.
🔹
نیویورک‌پست به نقل از جی‌دی‌ ونس: ایران برای پایان دادن به جنگ هفت‌ماهه باید غنی‌سازی هسته‌ای خود را کاهش دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/696499" target="_blank">📅 23:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696498">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff1e56a10b.mp4?token=toFadZT5X9Rb-I4v4PrV1S-QA5h5v3Ui8WZ28E50R9x8evlYiXKsMXmqthNy1sDx2F0lDNMzZouI7xvB_yWyY6PD4V6c-SWtmv9v8al3DPjqyPDC7Dl6XLG7501ZoKe0IGWkT1-lJmMOE42nglx1X1quBaQNR_50ZFUBJ-tFaj4ecEEx-JpSEV_mVuT93pMhoigwXEZAd_mkGvkkAsx1pY98uKJp0hkKsdwEdRi0VhN8STAEZF_67aBN_Yg3qGcR4X1L369BkmkHHJp4NbYPvL0xLbbZ-4mWlf01rmLQDe4Bf4GYdjku28X6Yp28gM6zm97CEI9nsC6n9uZVYseHHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff1e56a10b.mp4?token=toFadZT5X9Rb-I4v4PrV1S-QA5h5v3Ui8WZ28E50R9x8evlYiXKsMXmqthNy1sDx2F0lDNMzZouI7xvB_yWyY6PD4V6c-SWtmv9v8al3DPjqyPDC7Dl6XLG7501ZoKe0IGWkT1-lJmMOE42nglx1X1quBaQNR_50ZFUBJ-tFaj4ecEEx-JpSEV_mVuT93pMhoigwXEZAd_mkGvkkAsx1pY98uKJp0hkKsdwEdRi0VhN8STAEZF_67aBN_Yg3qGcR4X1L369BkmkHHJp4NbYPvL0xLbbZ-4mWlf01rmLQDe4Bf4GYdjku28X6Yp28gM6zm97CEI9nsC6n9uZVYseHHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت‌های مضحک نتانیاهو: اگر ما علیه ایران اقدام نمی‌کردیم، بمب‌های اتمی ۱۰میلیون اسرائیلی را نابود می‌کردند؛ ما دود می‌شدیم و به هوا می‌رفتیم
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/696498" target="_blank">📅 23:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696497">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
مدیر استان البرز بانک صنعت و معدن: موضوع فولاد بافق یک مطالبه ساده بانکی نیست؛ ابهامات معامله و شرایط پرداخت باید روشن شود
🔹
فرزین سمایی، مدیر استان البرز بانک صنعت و معدن، در واکنش به مطالب منتشرشده درباره عدم پرداخت تعهدات مجتمع فولاد بافق تأکید کرد: تقلیل این پرونده به امتناع بانک از پرداخت یک تعهد قطعی، تصویر کاملی از واقعیت موضوع ارائه نمی‌کند و تا زمانی که ابهامات مربوط به معامله پایه، مستندات و شرایط ایجاد و پرداخت تعهد به‌طور کامل روشن نشده باشد، بانک موظف است در چارچوب قانون و مقررات بانکی عمل کند.
🔹
سمایی در جمع خبرنگاران با بیان اینکه موضوع در مرجع قضایی ذی‌ربط در حال رسیدگی و بررسی است، گفت: «در این خصوص دستور قضایی نیز در چارچوب موضوع مورد رسیدگی صادر شده و بانک صنعت و معدن خود را ملزم به رعایت تصمیمات مراجع قضایی صالح می‌داند. در عین حال، اجرای دستور قضایی باید دقیقاً براساس مفاد و حدود همان دستور و با رعایت الزامات قانونی و مقررات بانکی انجام شود.»
وی افزود: «نمی‌توان مفاد یک دستور قضایی را فراتر از موضوعی که در آن تصریح شده تفسیر کرد؛ همان‌گونه که نمی‌توان مقررات بانکی را نیز براساس برداشت‌های متفاوت کنار گذاشت. تصمیم نهایی درباره چنین پرونده‌ای باید مبتنی بر مجموعه اسناد، واقعیت‌های معامله، نظر مراجع ذی‌صلاح و الزامات قانونی باشد.»
▫️
مدیر استان البرز بانک صنعت و معدن با اشاره به اهمیت بررسی «معامله پایه» اظهار داشت: «پرسش‌های موجود در این پرونده صرفاً به عملیات بانکی محدود نمی‌شود. زمان انجام معاملات و شرایط کشور در آن مقطع، هویت و سابقه فعالیت شرکت‌های طرف معامله، چگونگی انجام معامله و مستندات مربوط به تحویل و جابه‌جایی کالا، از جمله موضوعاتی است که باید به‌صورت دقیق مورد بررسی قرار گیرد.»
▫️
وی تأکید کرد: «طرح این پرسش‌ها به معنای صدور حکم یا انتساب تخلف به هیچ شخص یا شرکتی نیست. اساساً فلسفه بررسی کارشناسی و قضایی نیز همین است که واقعیت معامله و انطباق آن با ضوابط، پیش از اتخاذ تصمیم نهایی احراز شود.»
▫️
سمایی درباره استنادهای صورت‌گرفته به کد تأیید بانک مرکزی نیز توضیح داد: «وجود کد بانکی یا ثبت یک مرحله از فرآیند در سامانه، به‌تنهایی به معنای پایان بررسی تمام شرایط یک تعهد نیست. برای اجرای نهایی تعهد، مجموعه اسناد، شرایط معامله و فرآیندی که منجر به ایجاد تعهد شده است باید بررسی شود. بنابراین میان ثبت یا تأیید یک مرحله از فرآیند بانکی و احراز نهایی شرایط پرداخت تفاوت وجود دارد.»
▫️
وی همچنین در واکنش به مطالبی که از وجود دستور قضایی برای پرداخت سخن گفته‌اند، اظهار داشت: «بانک صنعت و معدن خود را موظف به اجرای تصمیمات مراجع قضایی صالح می‌داند .آنچه برای بانک ملاک عمل است، متن، حدود و مفاد صریح دستور قضایی است، نه برداشت یا تفسیر رسانه‌ای از آن.»
▫️
مدیر استان البرز بانک صنعت و معدن درباره طولانی شدن فرآیند تعیین تکلیف پرونده نیز گفت: «صرف گذشت زمان نمی‌تواند جایگزین بررسی اسناد شود. آنچه اهمیت دارد، احراز شرایط و مستندات تعهد است. اگر شرایط پرداخت به‌طور کامل احراز شود، مسیر اقدام بانک روشن خواهد بود؛ اما زمانی که درباره معامله پایه، اسناد یا نحوه ایجاد تعهد ابهاماتی وجود دارد، رفع این ابهامات بخشی ضروری از فرآیند تصمیم‌گیری است.»
▫️
سمایی در ادامه به نگرانی‌های مطرح‌شده درباره وضعیت تولید و اشتغال در فولاد بافق اشاره کرد و گفت: «حفظ تولید و اشتغال برای بانک صنعت و معدن به عنوان یک بانک توسعه‌ای اهمیت جدی دارد و بانک از هر اقدامی که به تعیین تکلیف قانونی و سریع این موضوع کمک کند استقبال می‌کند؛ اما نباید میان حمایت از تولید و رعایت قانون یک دوگانه غیرواقعی ایجاد کرد. حمایت پایدار از تولید نیز باید در بستر قانون و ضوابط انجام شود.»
▫️
وی تأکید کرد: «بانک صنعت و معدن نه به دنبال طولانی شدن پرونده است و نه از تعیین تکلیف آن استقبال نکرده است؛ برعکس، تعیین تکلیف روشن، قانونی و مستند این موضوع به نفع همه طرف‌هاست. انتظار این است که به جای تقابل رسانه‌ای، فرصت داده شود اسناد و واقعیت‌های معامله در مسیر کارشناسی و قضایی بررسی شود.»
▫️
مدیر استان البرز بانک صنعت و معدن در پایان خاطرنشان کرد: «اگر پس از طی فرآیند قانونی، وجود و شرایط یک تعهد به‌طور کامل احراز شود، بانک در چارچوب مقررات اقدام خواهد کرد و اگر ابهامی در اسناد، معامله پایه یا شرایط ایجاد تعهد وجود داشته باشد، ابتدا باید همان ابهام برطرف شود.»
▫️
وی افزود: «حمایت از تولید زمانی پایدار و قابل اتکاست که در کنار آن، قانون، اسناد و حقوق همه طرف‌های ذی‌نفع نیز رعایت شود. بانک صنعت و معدن نیز در این پرونده دقیقاً بر همین مبنا عمل خواهد کرد.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/696497" target="_blank">📅 23:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696496">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
علیرضا دبیر که تهدید کرده بود اگه حتی یک نفر از اعضای تیم ملی ویزاش صادر نشود تیم ملی رو به مسابقات جهانی آمریکا اعزام نمی‌کنه، امروز ویزای تمامی اعضای تیم‌ملی کشتی بدون هیچ کمی و کسری صادر شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/696496" target="_blank">📅 23:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696495">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6z5ELl9gYMgD_OmmCCta6tydRavVNtigZDubQBHQy2s0D981O0Rj08EQdnW4d4EDmt3VuTEVCrsSAa9R4yLmIo4dbxRlr2jE9YBtP-3CG76eN1mYn9d3xjqajB0q7z32_xDHgjXSV9F5sFWxUF_NHhiZ7fNFqTM2QvTr3n6kH-ZOBtnAAJ7GfBenr0-CmfB5M5EKpUPxBG_XYNFOFTsKdGMyde9_2fX9U1fpTOchdofR2RDTFaM_AE5CSc3IlVevtFVhFQPRDaxZJYNAlhRS-aw50_LSRqeaUAPR26L3u01HuhFyFB1U99lpjtlymDp3Peai-fdzAkkpYS9-KwvKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غزه پس از ۳ سال؛ جهان چگونه در برابر یک نسل‌کشی سکوت کرد؟
🔹
سه سال پس از عملیات ۷ اکتبر ۲۰۲۳، درگیری‌ها تا حد زیادی در چارچوب یک آتش‌بس شکننده فروکش کرده است. با این حال، دشوارترین پرسش‌ها همچنان بی‌پاسخ مانده‌اند؛ اینکه چه کسی کنترل این منطقه محصور را در دست خواهد گرفت، آیا حماس خلع سلاح خواهد شد و اسرائیل چگونه محدودیت‌های اعمال‌شده بر زندگی فلسطینی‌ها را کاهش خواهد داد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3250763</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/696495" target="_blank">📅 23:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696494">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgAP-VkkfVcPvX9HTp2CEXD3VUMfjTo084UjnGAJXGSxGX05frwWLlEPJaWtd-M4ML2gTB9Jsb1W-bUVI8IpEniRVtNgBrOdLOt5Tqf4ClBqkjYSnUFEB5StJcKcGSkwBo1RFf5m2YBTCg4k_zuAztjlxU9KkXqG2LRwTKuKWTNPrwwQdwcPniKqOHXLm7qCHRBQWt5KFd2XMHqsCPfwLAzAfOWd6zXvgn43sZ2m9orHf2L9edc9hL0u_0IYNRgrwCIytQMo81pEFBpwtV5MIUfU4mAFRuRqrQQhJfW6C31i48ZTlKJJvQTmxRwj1lYGksHcbqwTzhHSw_1aVN-N0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انفجار یک نفتکش در نزدیکی قطر
سازمان تجارت دریایی انگلیس:
🔹
یک نفتکش در نزدیکی قطر هدف چند اصابت قرار گرفته است؛ این نفت‌کش گزارش داده که توسط چندین پرتابه هدف قرار گرفته و آسیب دیده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/696494" target="_blank">📅 23:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696492">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صد میدان 8- میدان هشتم، جهاد</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/696492" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
شرح صد میدان خواجه عبدالله انصاری
🔹
میدان هشتم، جهاد
🔹
جهاد بازکوشیدن‌ است، بدان معنا که در مسیر سلوک روح هر فرد در حال جهاد می‌باشد.
🔹
می بایست در مسیر به آن شکل که شایسته‌ی پروردگار جهانیان است جهاد کنید، بدان معنا که به هیچ وجه کاستی پیشه نکنید و از هيچ کوششی روی برنگردانید.
جهاد سه قسم می‌باشد:
🔹
جهاد با نفس_جهاد با دیو_جهاد با دشمن
جهاد سه رکن است و ارکان به صورت زیر هستند:
🔹
با دشمن به تیغ_با نفس به قهر_با دیو به صبر
مجاهدان با دشمن:
🔹
کوشنده ماجور_خسته مغفور _کشته شهید
مجاهدان با نفس:
🔹
ابرار (نیکان)_اوتاد (مرتبطان به جهان هستی)_ابدال (جدا شده از بندهای ذهنی و نفسانی)
جهاد با دیو:
🔹
مقربان (به علم مشغول)_صدیقان (به عبادت مشغول)_اولیایان (به زهد مشغول)
#صد_میدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/696492" target="_blank">📅 23:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696491">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b31ff4edb.mp4?token=Jb5zqWbIwFMyhWpS3fQNUCtT789uRKyTC27_Hpcc5cjWQaGGirXeMh1G7u3JWqzSduvIlrAldlwzP2jpSKs0gcTiIZCMw8Nz6y244uOmhk7vLhRc_sXdMM643BI-BAyXG0VF6BPcfAp96YBd6MBnEMbkiccnp7C44_RsfXn60v_PJI2_swroH_id-pbJUuHyQG3c0YJA85OMlXrO3IJ5flB5NIsGz5lwBPbBVM7JgAWQmjZ8sIy1aaIQ46nCgYdzPe_FOG47Xyf7fDic8yQTXKGo8iROtg0nlmxQ0iNjMm8YX3qvui1RbIH8bN4EgDSaok06C6E4Rd2aGbOyB8Av_g9HOfiNklKMg4OadHTgroberApeFnKSPCsJGMfh_h3BET1LKuLVufbrGE1g01AsoMoCj2r9KBAGYwxN-xcnJP7b3MA2_YugH7PfsnP3XyBGLCUs64z-Iv-kwi4Xv7D4AySaWzWH58lJT3i_N5LTBKsUsvzq7tdUZzVmu9pb8oH5gP4aUq2CuQebW8UCcAPuUGK4kn_PIUK2S-t6D9vEU34HcihMl4tawdS52zvtLnlDno-44fjYOJnpqK9yPjK_d_BllW4MRau1b3kDi08ZZ-HFP5NkXcz0Dk_PfT61slY-kxCKdTIVtpa2kEcSp2nxYJdpNmVDFCK1yLxV5QFoBsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b31ff4edb.mp4?token=Jb5zqWbIwFMyhWpS3fQNUCtT789uRKyTC27_Hpcc5cjWQaGGirXeMh1G7u3JWqzSduvIlrAldlwzP2jpSKs0gcTiIZCMw8Nz6y244uOmhk7vLhRc_sXdMM643BI-BAyXG0VF6BPcfAp96YBd6MBnEMbkiccnp7C44_RsfXn60v_PJI2_swroH_id-pbJUuHyQG3c0YJA85OMlXrO3IJ5flB5NIsGz5lwBPbBVM7JgAWQmjZ8sIy1aaIQ46nCgYdzPe_FOG47Xyf7fDic8yQTXKGo8iROtg0nlmxQ0iNjMm8YX3qvui1RbIH8bN4EgDSaok06C6E4Rd2aGbOyB8Av_g9HOfiNklKMg4OadHTgroberApeFnKSPCsJGMfh_h3BET1LKuLVufbrGE1g01AsoMoCj2r9KBAGYwxN-xcnJP7b3MA2_YugH7PfsnP3XyBGLCUs64z-Iv-kwi4Xv7D4AySaWzWH58lJT3i_N5LTBKsUsvzq7tdUZzVmu9pb8oH5gP4aUq2CuQebW8UCcAPuUGK4kn_PIUK2S-t6D9vEU34HcihMl4tawdS52zvtLnlDno-44fjYOJnpqK9yPjK_d_BllW4MRau1b3kDi08ZZ-HFP5NkXcz0Dk_PfT61slY-kxCKdTIVtpa2kEcSp2nxYJdpNmVDFCK1yLxV5QFoBsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی چوب، سنگ می‌شود!
🪵
🪨
🔹
این فسیل یک درخت باستانی است که به آن «چوب‌سنگ» می‌گویند.
🔹
هنگام پوسیدن چوب، مواد معدنی جای مواد آلی را می‌گیرند؛ پدیده‌ای به نام «جایگزینی معدنی».
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/696491" target="_blank">📅 22:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696490">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
«باج‌نیوز» در دادگاه؛ یک رسانه در پرونده شکایت میلی محکوم شد
🔹
یکی از رسانه‌هایی که با انتشار مطالب خلاف واقع علیه پلتفرم میلی قصد اخاذی از این پلتفرم را داشت توسط دادگاه مطبوعات محکوم شد.
🔹
در پی شکایت شرکت سرمایه زرین ماندگار (میلی) از پایگاه خبری «وانا نیوز» بابت نشر اکاذیب، شعبه پنجم دادگاه کیفری یک استان تهران رأی بر مجرمیت صادر کرد. به گفته سخنگوی هیأت منصفه دادگاه‌های سیاسی و مطبوعاتی، هیأت منصفه پس از بررسی مستندات پرونده و محتوای مکالمات ارائه‌شده، به اتفاق آرا اقدام مدیرمسئول و روزنامه‌نگار این رسانه را مصداق باج‌گیری و سوءاستفاده از حرفه روزنامه‌نگاری دانست و آنان را مجرم تشخیص داد. رأی صادرشده قابل فرجام‌خواهی است.
🔹
گفتنی است در روزهای اخیر نیز برخی رسانه‌ها در فضای مجازی اتهامات مشابه‌ای را علیه این پلتفرم مطرح کرده بودند./ مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/696490" target="_blank">📅 22:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696489">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-VW9eVklZLjuAeFKsCIwNwKMQnOpOfpJt-_oMB2HiVCKxmnz6-IN_vuGFFU8sa6GqbgNSzrFaQdlCB-IOy5-TNOh-E96Hb-9m8dWrgvwRDk5n07FXrjQC9nBhO3ApKSSVizUVCAcR5-ZPtpmpKCLHhPpcc6eBiY3g6EE9caVVLlAXsaUQh_Kyf13w-9ehH1v0q8dlaFoJJpnM38fPjH67F24cswhMTuFyz-Vg4sJRQD14GPhQMXVxC3n2gZvdUvFaT-Z9WAXk14YAzPyqEaQw6hsEEvHkKxy88F_lnimA2yENQJi-LKocIUtCpSegvS3eTFoPgOMpMO9fslfwEZgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آکسیوس: فاکتور گرمایشی زمستانی بی‌رحمی در راه است برای خانه‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/696489" target="_blank">📅 22:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696488">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3yVaqUvzyW_EDnaqYJ5XQtaprcKDtA7195aRVKQYS6NVPdQo976gpbvw5IBi-M-PNQLTZizgadVcb3H-4RLnpOQKdvt9YZQcKugYhQpY7YKpCVl2DRvfYX1mupTuy7tEnImHijBwl11qjtJDyiMQYATmRXcMpZdEOGSEpwb71aRhD_CkJ5u5KAhcIoayCeMdNDpzQQCSycv9gTbY-TQnPePBPLa5BS52fozZV6iaqiHKVHqbJhaaU5eKmna9UKnhmBHydAmf-jGPb0sjUCnNivS81vpkWH5RPDd0-GQePRvBqDJxitQWiPZiQh0QKSyOGYpwWvbyyYhtzTXbYY5Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آتلانتیک: ترامپ پیش از انتخابات میان‌دوره‌ای دستور حمله دیگری به ایران را صادر می‌کند
🔹
کاخ سفید از پنتاگون خواست گزینه‌هایی برای حمله به ایران قبل از انتخابات میان‌دوره‌ای آمریکا آماده کند. تصمیم نهایی هنوز گرفته نشده/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/696488" target="_blank">📅 22:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696487">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
شنیده شدن دو صدای انفجار از سمت دریا در کوهستک سیریک
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/696487" target="_blank">📅 22:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696486">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
هشدار آمریکا به شهروندانش: ممکن است بزودی فرودگاه‌ها و حریم هوایی عربستان بسته شود
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/696486" target="_blank">📅 22:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696485">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7Jw-zbkhdFfmGt2oDhmp4TWzooYOwSbcWaHoPZAH1fmEV1uPsFRyYm2BveA5FaJ2vLkFJF0Pgb9HH73BoxkNmyHh3jq6oVt22m51L0_GW4j2-8rr6ql4J2YnVHl98UX3P2-xKiR9PGq89MNPcFnRIndtm-bq3SIPe25IXC1CNieIF6_0o6KCKG2VTjNZZROPJnfkmG_gKGmUVRkdbrpf7MZ0qvVaQPmCwnKIM-DCuTmtY8rORQULlmpkNziKqE2wDduJy6C6Awz_1JlOvTRPlr_wZ4ukVguq9U3voPmD0PSMs8wFNjMDaZc0A-Z1e2Vcwj1rrpwcjUGWdrjvqakFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لاهوتی نماینده مجلس: مشکل میلی خالی‌فروشی نبوده/ فقط موجودی طلایش از خزانه دیر تحویل داده شد
🔹
کسی که طلا می‌خرد، در هر صورت باید از اعتبار و اصالت معامله اطمینان داشته باشد و حواسش باشد که فروشنده یک مرجع رسمی باشد.
🔹
در فضای مجازی اتفاقات زیادی رخ داده است. در سایت‌هایی مثل دیوار هم موارد زیادی از کلاهبرداری دیده‌ایم.
🔹
میلی گلد هم مجوز مدیریت و فروش خرد طلا را دارد، هم پروانه کسب‌وکار و هم سایر گواهی‌های مربوط به فعالیت در حوزه فناوری‌های نوین مالی.
🔹
مشکل خالی‌فروشی نبوده؛ طلای موجود خودشان را از خزانه دیرتر تحویل گرفته‌اند و نتوانسته‌اند آن را به‌موقع به مردم تحویل دهند./ جهان‌نیوز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/696485" target="_blank">📅 22:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696484">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
تسنیم به نقل از منابع امنیتی: حمله راکتی در جالق سیستان و بلوچستان کذب است  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/696484" target="_blank">📅 22:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696483">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
حمله مسلحانه به مقر انتظامی در گلشن
🔹
بنا بر اعلام منابع آگاه دقایقی قبل یکی از مقرهای انتظامی در شهرستان گلشن مورد حمله مسلحانه قرار گرفت./ صدا‌وسیما  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/696483" target="_blank">📅 22:34 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696482">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nq51fiAONJi1LB_XMrXsaEhqb5xSEYzLvhm22HJDU7IWtsFR4x6s5n4KUfuKEhy1SE460jN24nVojcbV0apTbOjJVtGIN17g4d76BEyErn3S3LVh5scjJwBKMJfJaHiy4zdZaO_xQm_vOTVDgQlboRB53wDAMnEqLSNOkA6y5lLourI3UdQKDv3siGmlMoBwDmAKSZhQGCIp_TJgxpjc1pOVWuQbx69i8sx5ai25xZ6oOzK-6rm3DL_1NrTEA4-g2ULvW3Okc95Rf5O5C0N--U64RKJBvh-ltQAXu9xusyHVT1V2TSn0aV3NRJekrtWHo-_jY96Nmgh5w65SGX4h6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آپدیت رنکینگ جدید فیفا در رده‌بندی تیم‌های ملی مردان؛ تیم ملی ایران با یک پله نزول به رنک ۲۳ ام سقوط کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/696482" target="_blank">📅 22:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696481">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
پزشکیان: من یک دانش‌ آموز شلوغ و بازیگوش بودم و درس هم نمی‌خواندم اما وقتی وارد جامعه و نامردی‌ها را دیدم تصمیم گرفتم درس بخوانم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/696481" target="_blank">📅 22:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696480">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
سخنگوی ارتش پاکستان در اظهاراتی حضور بلندمدت نیروهای نظامی این کشور در عربستان سعودی را تأیید کرد و آن را بخشی از «ائتلاف مکه» دانست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/696480" target="_blank">📅 22:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696479">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
سخنگوی انصارالله: فرودگاه ابها و تجمع نیروهای سعودی در جیزان را هدف حملات موشکی قرار دادیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/696479" target="_blank">📅 22:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696478">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ادعای
ترامپ: درگیری با ایران به زودی و به هر نحوی پایان خواهد یافت
؛
ایران در شرایط سختی قرار دارد و هرگز به سلاح اتمی دست نخواهد یافت
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/696478" target="_blank">📅 22:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696477">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0482c0e27e.mp4?token=W6yWhBjdoE2V1aXIeERfvhJz19RO42Var3BYzC4xnEfG_cPkzXEeKjroaZENsOT5ZaSmGGSXKE3Qe_w0_m2kF6tWb8Kn5Lm_0GIhIPwR2zVzr_dqj3fQc6kEaWA_XBUmUMnDIkwo6m6g63HrVGe0Y_XLZiN1eWrvgI_4-4UhvToxNU-cVxKXzHBaPO1krG8JeXwY-gZUWEZSoZXIByDZhLsFkVHxvVBc3F44fA_C3U38Mo-LoezWPF_IrgJhZpSSV9GOPveAmWimM1lHx2uY32Ml-4vgATlE1mKfSwogBsUo4jviiiUonukT2V_oYqWRY0fuZDy-bXuBwsZJyfPCkzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0482c0e27e.mp4?token=W6yWhBjdoE2V1aXIeERfvhJz19RO42Var3BYzC4xnEfG_cPkzXEeKjroaZENsOT5ZaSmGGSXKE3Qe_w0_m2kF6tWb8Kn5Lm_0GIhIPwR2zVzr_dqj3fQc6kEaWA_XBUmUMnDIkwo6m6g63HrVGe0Y_XLZiN1eWrvgI_4-4UhvToxNU-cVxKXzHBaPO1krG8JeXwY-gZUWEZSoZXIByDZhLsFkVHxvVBc3F44fA_C3U38Mo-LoezWPF_IrgJhZpSSV9GOPveAmWimM1lHx2uY32Ml-4vgATlE1mKfSwogBsUo4jviiiUonukT2V_oYqWRY0fuZDy-bXuBwsZJyfPCkzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلاش هگست برای حفظ آبروی ملوانان درمانده ناو یو‌اس‌اس آبراهام لینکلن
وزیر جنگ دولت کودک کش آمریکا:
🔹
چند نفری در رسانه‌ها سعی کردند ناو یو‌اس‌اس آبراهام لینکلن را به نوعی نمادی از روحیه پایین یا مأموریتی شکست‌خورده جلوه دهند.
🔹
می‌دانم که این موضوع دقیقاً برعکس است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/696477" target="_blank">📅 22:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696476">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDFwkY23vkNKWe2HBTm8RB7nDaHN9Zk6NFTS7i7n__FxitSxInSx_uQGkV-aBkn6PovcjC03Dou2Etcypl4kJlKPzKBRx3IlgesvOnLCJrP7PfgkXpJDWRFUXQiAXlN3F-Pb8yl6KdI6vHQZ24woeb4ZM3TitA1uA13sY3yseN4DN3Mum_jQO4w4hvb_OGjj2JoLdrGCtPsowNW5ovCT9jnu4RZTgx1sa2RfT37IuKxuVTImVQXogdXNH0hA2ltFThgqLj2P5U0EaQ6-EdtgmfkYCHcwh7fm-MsGFeGaDJk2woNczkiOHQKSkt1zqaB38MNzUpjJ9rDA9ELNiDMMvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این ۴ آنتی‌بیوتیک رو خودسرانه شروع نکن!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/696476" target="_blank">📅 22:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696475">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
این ۳ تا ویژگی که علیرضا مطلبی درباره ثروتمندهای نسل جدید می‌گه رو باید جدی گرفت...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/696475" target="_blank">📅 22:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696474">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
ادعای یک اندیشکده پاکستانی: عملیات سپیده دم یمن با مشارکت پاکستان و دیگر اعضای پیمان مکه علیه یمنی‌ها آغاز شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/696474" target="_blank">📅 22:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696473">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
تسنیم به نقل از منابع امنیتی: حمله راکتی در جالق سیستان و بلوچستان کذب است
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/696473" target="_blank">📅 21:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696471">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c9fb18cd4.mp4?token=cROlrvW9n1D_Tm7DzXBRygLuA0d0fCddOK9e0dXDdA4CW5uxvv0KiBfw-R5P_37lN_mMzLbUMGZgCIt0pAGHn8120_2OSsmMZt2HHS9jWfWFa0uG1TnhbhiJm1aRYMY7LYnU7p--sUHXtPjaKV5pLo57UKDA9EEkAewjyzxSAsT_sFAmopcrbJ7s7DS-ZfP9jj8Dt9qVZ10EDk21bG-rPtgm-a-iVn7UbpUdhTYqFNJvMf7cL_b-XbQPauaVEHITgYamPna0foZTWIVk8Ch1x1yzv_shyZrgqPEvh3gZnr9vSpBuBknwhHoCkZnXN_2lJR3tW-7LvX23BmCtQs73DQ4ddghSY2fkYcjMSeMLOwi9Ac26nqw38JDKqyQ9PczFuPmB37zTAkxIam4UWOZYfQVLOKPCRM5RVU7U8WZYkmAOJWcl-hWIncbbTU-Xls19cjB6zBCI_Hl9pHRF9ihEmMrGtefI5mf8F1WuEvjgowJ1g1gUyLa3QljenepEiqEpyxzqlCar9Us_vQyoFaGxVzzEbgNu-6fRCbypo74k08IfE-rZY_MkArUdhAOpBR3HvLJvieoH3DeoWs3zKghnbWwCew7Vk5znjCBJtM3DlV8tl833wKaioSACXbHORpABGhQJ524WreSS5LZcJ7HMaEY9PniKXiB07M4HjbfCwXY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c9fb18cd4.mp4?token=cROlrvW9n1D_Tm7DzXBRygLuA0d0fCddOK9e0dXDdA4CW5uxvv0KiBfw-R5P_37lN_mMzLbUMGZgCIt0pAGHn8120_2OSsmMZt2HHS9jWfWFa0uG1TnhbhiJm1aRYMY7LYnU7p--sUHXtPjaKV5pLo57UKDA9EEkAewjyzxSAsT_sFAmopcrbJ7s7DS-ZfP9jj8Dt9qVZ10EDk21bG-rPtgm-a-iVn7UbpUdhTYqFNJvMf7cL_b-XbQPauaVEHITgYamPna0foZTWIVk8Ch1x1yzv_shyZrgqPEvh3gZnr9vSpBuBknwhHoCkZnXN_2lJR3tW-7LvX23BmCtQs73DQ4ddghSY2fkYcjMSeMLOwi9Ac26nqw38JDKqyQ9PczFuPmB37zTAkxIam4UWOZYfQVLOKPCRM5RVU7U8WZYkmAOJWcl-hWIncbbTU-Xls19cjB6zBCI_Hl9pHRF9ihEmMrGtefI5mf8F1WuEvjgowJ1g1gUyLa3QljenepEiqEpyxzqlCar9Us_vQyoFaGxVzzEbgNu-6fRCbypo74k08IfE-rZY_MkArUdhAOpBR3HvLJvieoH3DeoWs3zKghnbWwCew7Vk5znjCBJtM3DlV8tl833wKaioSACXbHORpABGhQJ524WreSS5LZcJ7HMaEY9PniKXiB07M4HjbfCwXY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیام تصویری نماینده جنبش حماس در ایران به مناسبت سومین سالگرد طوفان الاقصی: مردم غزه ثابت کردند در برابر ابرقدرتها شکست ناپذیر هستند و مقاومت با وجود ترور رهبران و کشتار مردم همچنان ادامه دارد
@TV_Fori</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/696471" target="_blank">📅 21:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696469">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
حمله مسلحانه به مقر انتظامی در گلشن
🔹
بنا بر اعلام منابع آگاه دقایقی قبل یکی از مقرهای انتظامی در شهرستان گلشن مورد حمله مسلحانه قرار گرفت./ صدا‌وسیما
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/696469" target="_blank">📅 21:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696468">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8nnRDnsC-MwLkWV4KMexwUw1esLKrIxDTP28UpF3r6QhNpi2-mgSQd3IpyvWFye0tlhVrzpYcMKy_cysvL0c5CLw9DU21ViVV6tEvxiY-EBohmjDwH2PTWpQSVMsf10k2udZlyko4Ck-iBtplS7PVE-mHqQ-ZikHYPpn63cmZhGg4Aol0o1de5FzlU1uC0zdzHzddDL7w03XuqAloRGK-XlRzzs-9FO0zKv3jfM-LGAMNJ9T1Lq_EVG53v_g_z19z5rtKCTa8QANyyvCTGP9L4SUwJOEbl6NF54aIHhQFfUeuoJp29MQD6QK2uhgOu105LLzE94JJfwmsLcw1DONQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نارین پس از روزهای سخت به آغوش مادر بازگشت
🔹
دو دختر سنندجی بعد از مداوا و درمان دیروز از بیمارستان مرخص شدند و به آغوش مادر بازگشتند.
🔹
این دو خواهر خردسال سنندجی پس از آنکه برای مدتی در سرویس بهداشتی منزل حبس شده بودند، با حضور نیروهای امدادی نجات یافتند…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/696468" target="_blank">📅 21:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696467">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRNOb_dqGRF_-B1GB-P7ijnix25qZX26walZqefkPjsveNyxdqevO3dXJ_g6HSQ19UzPHgeTmweqQeZRtbG8oxyxyWd758lSc90eIE-7FLDEAdsDOHfQ1d86WDtAVrGNj3K5Ac9ST6m9LPxWxBqR24wpOnYT3zZiun3BqJbCwsrWv0ZNu0mi8ieDI3NRVl6R3aMkAuX4whGbRh08OInXwewxLE81tLszC_ptok0QQ84wg4St-nAbjJCIDWcQHLeX5pwQ63_4HdU8jVHwMnLzuk1FXLJsy3iIlNtHIlD2jB58V4HR19X5NzLWxArs75-kaLRWMygX-iyVNJZPSvlXmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از مدرسه تا بازداشتگاه؛ برخورد امنیتی با دانش‌آموزان معترض
🔹
اعتراضات دانش‌آموزی فرانسه از نارضایتی نسبت به کمبود معلم، کلاس‌های پرجمعیت، فرسودگی مدارس و فشارهای آموزشی آغاز شد و به سرعت به جنبشی سراسری تبدیل شد.
🔹
تا ۶ اکتبر بیش از ۶۵۰۰ نفر بازداشت و دست‌کم ۲۱۵ دانش‌آموز مجروح شده‌اند؛ همزمان صدها مدرسه نیز تعطیل، نیمه‌تعطیل یا درگیر اعتراضات بوده‌اند.
🔹
برخورد پلیس با معترضان نوجوان، استفاده از گاز اشک‌آور و سلاح‌های کنترل جمعیت و بازداشت‌های گسترده، انتقادها درباره تناسب برخورد امنیتی و محدود شدن حق اعتراض مسالمت‌آمیز را افزایش داده است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/696467" target="_blank">📅 21:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696466">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdPSKthEpgjsiU7X5sjlTp5xamZFO0-vcguTxNi2QCEIc-hnMO2LjculOgnl6PVN4f3kDR1OnG6AGbmF_-k8tVyJ8ju1Z-HKSpUnBFOWixU_ZXxCuAdL8KdWFp96UaELXjnEXf2ubY0pnfWMjMkr4NE0-aVSBEzWXPC1bzOIMgo5KvvN-l7qwtxBBuKNc8fI5zAaoHcIIMjo3oigulk70IsxGF2yn4DChnRUI6bw0TPZI0_bq7HmD4LiidGNAYRfv981510Hh0T1tov9sHABEbXFFTmPNRT7bSHnwKOkfkMZ8GDHAQtmWkWzKkfAz_SBGtxeOHTGwK82skUYxFjDwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پچ روی یونیفرم سرباز اسرائیلی مورد توجه قرار گرفت!
🔹
مناطقی که میخواهند و به رنگ آبی روی نقشه است از نیل تا فرات است که حتی شامل عربستان می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/696466" target="_blank">📅 21:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-696464">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">23-1 Ane Manaee (1404-02-10)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/696464" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه بیست‌وسوم؛ بخش اول
🔹
تبیین دوگانه "تدبر در قرآن" و "دل‌های قفل‌شده" در آیات ۲۴ و ۲۵ سوره محمد [01:00]
🔹
توصیف ویژگی‌های قرآن و اهمیت تفکر و تدبر برای فهم لایه‌های باطنی آن [13:05]
🔹
تشریح فلسفه "وحدت وجود" و خطای بزرگ انسان در اصالت دادن به ماهیت ها به جای دیدن وحدت در هستی [22:10]
🔹
نگاه قرآن درباره وحدت وجود و تجلی حقیقت در هستی، و تفاوت نگاه فلسفی و علمی به مراتب وجود [29:37]
🔹
بررسی شخصیت ذوالقرنین در قرآن و تاکید بر منشأ تمکن او در زمین از ولایت الهی [35:32]
🔹
علم واقعی در اتصال به حقیقت است. علم به این حقیقت که اراده الهی منشا تمام صفات و نیازهاست [49:47]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/696464" target="_blank">📅 21:30 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
