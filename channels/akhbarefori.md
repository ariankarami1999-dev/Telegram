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
<img src="https://cdn4.telesco.pe/file/hz1dAJAz7YUKMn4vI8n8wN7bI4_Yn8SDCs5GkSkVTmPAybU9qVca62UqqtJOxMys8T4hAMqvcnAURn6BduFGp4A8J_BtUWJCYByslbIfZez0ErOErVGwMizN13ur4TQFdBtWRdRt_hFwALlKUrFZMeatzWOeGSxt1psgIZLMHai5861tOwfEvRQP7WSmciPjZXQQEG_oLQkRYnrtKIhmotdp62tZKGKMBzqIGcBkLRm4IMM044TJlmSV_aXyAEgaRMLLbfKBbP0gO83345hIdGmxTrNOn6Q8KVwyjBRFYJf-QV0cmkfd5XfgA-vcMApwGCMGYju-3NLkjUSJRZ4R9w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.59M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 09:56:29</div>
<hr>

<div class="tg-post" id="msg-658658">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d8bf8457f.mp4?token=hCIgQX1e_pL3uRfzv8_L8hbhO2Q2TkCZ1D8xFYI8HNmtjfNcwq2eNGJnDfDHfOIpPf6k1RW7bfChyAbyKFun6KG86HZWdI6_H5E6V00L9zw2Yi49w_Z-Y504O4NAJ3nTdvUD5QzXoq-lsYuz0lmVWhb0cDid_OouFs_Sz1LEfM8QPEYFuz-t7p9bZJDqUkF7Fr3Go_nGWNQr1ACZeV3B_pK4LShUyrZcvziM3s66IucuNE0Rb58Jf5lN32z6Hgy5dLMsU0wvU8GX5fH2dcqayDvGS2iEYbqw2eN505YGnSTfOrG7BWnIEpEi87_IdJ2VsGDqsCuedbZIr2rqe-0iMh54g_W8EfA0pJD3vEtu1n-avGkTtGAEe2jWITfj77eGSmbfud34QALJ7aNDYdB2NLf2EuGw5k2cOP4RReK-jxg1zqjlx4SynppDcbNNJNiMNXxHPc6VtrSc0hUOGCw2PSAjl7lAb_PQ2KJQVbYFnwi5u7ZeDaMTWQvwj-PdpzuUlnH5f0Cnh1qfKm8Nf9IfCuJ7tJAw1zLXCGutR5K2pou5W71sD5bX3fd9zKUUvOsWuUrwyZFQ3Lt59PsA-F5PwZOSwBph5DvZ7b6z2GDgILwopqsBB9tvrlGyNGmIHSrprdNnD-3gGeIAMghgP_IbJNwKgbnk57gPiexSWkzjbtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d8bf8457f.mp4?token=hCIgQX1e_pL3uRfzv8_L8hbhO2Q2TkCZ1D8xFYI8HNmtjfNcwq2eNGJnDfDHfOIpPf6k1RW7bfChyAbyKFun6KG86HZWdI6_H5E6V00L9zw2Yi49w_Z-Y504O4NAJ3nTdvUD5QzXoq-lsYuz0lmVWhb0cDid_OouFs_Sz1LEfM8QPEYFuz-t7p9bZJDqUkF7Fr3Go_nGWNQr1ACZeV3B_pK4LShUyrZcvziM3s66IucuNE0Rb58Jf5lN32z6Hgy5dLMsU0wvU8GX5fH2dcqayDvGS2iEYbqw2eN505YGnSTfOrG7BWnIEpEi87_IdJ2VsGDqsCuedbZIr2rqe-0iMh54g_W8EfA0pJD3vEtu1n-avGkTtGAEe2jWITfj77eGSmbfud34QALJ7aNDYdB2NLf2EuGw5k2cOP4RReK-jxg1zqjlx4SynppDcbNNJNiMNXxHPc6VtrSc0hUOGCw2PSAjl7lAb_PQ2KJQVbYFnwi5u7ZeDaMTWQvwj-PdpzuUlnH5f0Cnh1qfKm8Nf9IfCuJ7tJAw1zLXCGutR5K2pou5W71sD5bX3fd9zKUUvOsWuUrwyZFQ3Lt59PsA-F5PwZOSwBph5DvZ7b6z2GDgILwopqsBB9tvrlGyNGmIHSrprdNnD-3gGeIAMghgP_IbJNwKgbnk57gPiexSWkzjbtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهمان‌نواز مثل مکزیکی‌ها؛ جشن جالب هواداران با هوادار کره‌ای در افتتاحیه
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/akhbarefori/658658" target="_blank">📅 09:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658657">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4ZeENFXuLiUYrAbh6X4R603qrKvIklwFlYH6x4s5XSMk5Zsm2eX8RyYnjIrIBC4r2cAvnqyx3eGR0HWTo2rm-szCz49v0o3RhoovbfjLjWMLiTyygLd8UZrVRC2TEMfWxG-9CBiJsBNXHktN1EUy4pBHMSH-D6xixj3mVmwI2U3s3yDZYgKhWIE4co6caguY7HOkSZFb3mARm4cV3UROqyWIbSVOcVzVivOPr9WIbAJOKs7Vnu6XOqAf5FUu3f-8Iu8ywAtdF0h6-9xcAcVF12sdCSVt4brKGNTr7DaYayIY9kNaNquEO9-mLHlgaW-Hrg9U1s4OLXs4CaaWQZiRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روز دوم جام جهانی؛ کانادا مقابل بوسنی، آمریکا برابر پاراگوئه
🔹
در ادامه مسابقات جام جهانی ۲۰۲۶، طی ۲۴ ساعت آینده دو دیدار حساس در گروه B برگزار می‌شود: کانادا به مصاف بوسنی و هرزگوین می‌رود و آمریکا میزبان پاراگوئه است.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/akhbarefori/658657" target="_blank">📅 09:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658656">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
شروع سوخت‌گیری با کارت بانکی از تیر امسال
معاون سیاست‌گذاری سازمان بهینه‌سازی:
🔹
از تیر امسال سوختگیری با استفاده از کارت بانکی در چند جایگاه کشور آغاز خواهد شد و تا پایان سال به همه جایگاه‌ها خواهد رسید.| تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/akhbarefori/658656" target="_blank">📅 09:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658655">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3Gs9ARzAHljWSzMurJP9R1HiTE8oS6oSP0PpqPh0w0UXmxIAwGNNPhzPO1KzZDUeMVp7ZDQlijolFgXlUXPmptR137_awOIpayYX_1b0EAj9TY-ffx1VqATv0mnBoSkY_lcbk4aA5eI-wAF6m_GrsYqYt6dsECmq3jX6ATiBzai5p9UWqep8eTMbEx74l7LWk0mRFePPbNVMnbIdLN4xkm2CMgEGz-TLdSLPN-zaKJA7bkWk1xqA4KblSzXGgvOLzqb7NUNk7E4JiIcEAUWJLZBOaQuwaflVJa9D2Y2dQAjdaheQMmBtY7WBOZLXhBGkGDBkN0X4wD_aWDwV-mAYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میان وعده‌های مناسب بعد تمرین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/akhbarefori/658655" target="_blank">📅 09:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658654">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQkwI6NqKYq60M3e7CE-p2W2pNPwCogXdWwOuahhHPyy_pys-QKmQWc5H1VgpTpWbOMQ6_v8IlYPAUhVOdnc6Te86bWihNJxUIsgqgTfPh5DqLScsSXtKRh-YAF3JQ4wf8zUFULMiFon5vPfaKFiPqpe2hT8esoRgnKxaJvHMuh6GHvawAGRKQjQtvDXQm45ie2Sem0OPT9uCpMLnakh3CxI3_Ml0Me4XXEmNZkCUfM5CeXLgq_saTWTQgyHHR-RQExl5S3m68o7R_exoXR8ZKYypD_5loLiZZ9AR69uEaFz5KAsa2qaEHNU6RtkzNO5nPVs41kzynZg6Q2DgA2NHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خشن‌ترین افتتاحیه ادوار جام‌های جهانی
🔹
برای اولین بار در تاریخ ۳ بازیکن در اولین بازی تورنمنت اخراج شدند.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/akhbarefori/658654" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658653">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvu9nCf3Bxd3HXIc7j_FUW_io-ayNmz9I77_mHfF84P5Uhh4TWb0a8pI1KZJqTd7rriZynMBEaoQkZuGqbRb0bllQZYGZyP2S2psl2UkbZ9XvwjvVbEBZC58mQXexjVOGVLGIA2RfwwX2mIO6IeK_GBX1rAjcJsFY5lgyit93uC2bq0sH2cKKi1wm67TpQe3zZPdCdK5_ZedL_fTHkdavhspK2jRzjEIVOblT9RGfmeEpMLFe_OM_nCVsKmnJsyJkycCtjAq2Jo4DlKd0neYQ3ShoB5WWFKezvS-rSsQ_wiGhXs52cRYIHcX9O2u6nxDrYVchz01uZbYXFuA3VISZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بعد از کارت بازی داور برزیلی در افتتاحیه جام جهانی، این تصویر عجیب هم ثبت شد!
🔹
البته جدا از خشونت جام ۲۳ تا الان، کیفیت لباس‌ها زیر سوال رفت و ضربه اقتصادی عجیبی هم به کمپانی «پوما» وارد خواهد شد!
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/658653" target="_blank">📅 09:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658652">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKW972OpQI7qAIXO27036l5yTrZOEJs3r69ScEjmb8_wD5IxwS71AEiqJLK4HlyaBBgXnDGXHiLFx5EhzEKwOFwzKfIgCVaaGZAn1dUti7ihbpZwd6wOUyNIZH413UUEnnHXU1spW70-sIhf8km0kIeR62gDUzPBoZ1y8yGkVfbRS7JnwO1GYmEOAkyBfc9Fo2y4fuM_pCjZ7fF7GmMNrOQQGgATg3MYGkn4rh5O3ZfPNk7NA2dB_8KMqutsPiBfPlUCB2soPhGjTsvwVlrE_1EJYmqQPzksRRq9Mx5z74xASoP8YWuweLd92yffYe8Jn__yqCesraNdHe8wczL_Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول لیگ ملت‌های والیبال پس از بازی‌های روز دوم
#ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/658652" target="_blank">📅 09:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658651">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
غریب‌آبادی: تمامیت و امنیت ملی ایران موضوع معامله تبلیغاتی نیست
🔹
معاون وزیر امور خارجه امروز بیانیه تعدادی از کشورها درباره فعالیت‌های تهدیدآمیز منتسب به ایران را مردود خواند و گفت: حاکمیت، تمامیت ارضی و امنیت ملی ایران موضوع معامله تبلیغاتی نیست. هر اقدام خصمانه، هر اتهام‌سازی بی‌سند و هر مشارکت در پروژه فشار علیه ایران، با پاسخ حقوقی، سیاسی و مقتدرانه ایران و اقدام متقابل و متناسب آن مواجه خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/658651" target="_blank">📅 09:15 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658650">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9FN8GxMdv2FzMrlX2exm-_ml-xDFFC7nOgcFiTK4QzThevLHzT25pqiWVKn6Xj-4Nr-Nxe_ALjZUZS-ZZDnEtUC4KFmvzeRfrRM_p34M2qZKEmUr1r6EIk6bPIQFHpzuhN02sDAK2T1ljGNGhY_7R_Xm_wOxZAZndHKEZDsfBvU4anfWkCsG3DEHwl7seIDls34p1b5TRSVSJO98EAJIucpedzUgAjmgeY3mhZyZRT2JPhWwwdJiJt7vA-uvRznpQrpSUUCu2NnmpF16jeLnlACaTIZuXJLocexhThdwfKTlFeCC9oRngDxj1t3uYZx_wb131cq4hfK5K1M-zNEzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین اتفاق تلخ جام جهانی ۲٠۲۶| مرگ یک هوادار در جریان دیدار افتتاحیه
🔹
یک هوادار آلمانی پنجشنبه در نزدیکی ورزشگاه مکزیکو سیتی در جریان دیدار افتتاحیه مکزیک و آفریقای جنوبی در جام جهانی ۲۰۲۶ جان خود را از دست داد.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/658650" target="_blank">📅 09:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658649">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c602ebbfd.mp4?token=R83vak5CI8IjZauRvQL1BC1ifUO22nIoVpJM99oDBjqrJDO_Qo30ZYWDMVvUTY3CiDj14CYkeIzpfX3HbTx7VHis2gEfCgOcR2dvZeMLqYu9HBfWNHf32Nr-iXeRxdMsfNg_cYahjhoJln2Qrwc_A23bweLiQlzlPwpY2A90N2IgAkqbceU7bKvCsUBVqYn2o5EgOEw4-5l5A_lLEIXcwPmkvzc9zfBisj7_6zaPRqIk_LELO_MTrfBPK-5Vi9Emoq4QLEylYzp1dvaDotfZSDh6WEM58xCcO8StMhrDP0ApzkqS7OQckr0K1IxWBLYn8suDR5tsIEesfy4aXVQf7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c602ebbfd.mp4?token=R83vak5CI8IjZauRvQL1BC1ifUO22nIoVpJM99oDBjqrJDO_Qo30ZYWDMVvUTY3CiDj14CYkeIzpfX3HbTx7VHis2gEfCgOcR2dvZeMLqYu9HBfWNHf32Nr-iXeRxdMsfNg_cYahjhoJln2Qrwc_A23bweLiQlzlPwpY2A90N2IgAkqbceU7bKvCsUBVqYn2o5EgOEw4-5l5A_lLEIXcwPmkvzc9zfBisj7_6zaPRqIk_LELO_MTrfBPK-5Vi9Emoq4QLEylYzp1dvaDotfZSDh6WEM58xCcO8StMhrDP0ApzkqS7OQckr0K1IxWBLYn8suDR5tsIEesfy4aXVQf7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمام دفعاتی که ترامپ ادعا کرد به توافق با ایران نزدیک شدیم!
🔹
۳۹ ادعا در یک نگاه
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/658649" target="_blank">📅 09:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658648">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca12a42c85.mp4?token=nItcZ1X1gI3AfObKCx7m6zB0xJeTXkGqWBUJii3oO8J5IdxU4Dd0QccgmN59KikSfJ8YPW3JSzNm8zIxgKa5pCXwba7lMlGzwylfFetx91-Hh7e-RO1eayPbfYckvcMZqzwYbGdRY8EwPmokUnY1CM0ksJ-r76SEm7TavalhBfu5Xyi8VxckTYa5R2JKdkEtEhHyCyg7iJE_emiTtOQtYRRYRuEZ-IAcLaE4fZfdH2H7ieBWXogn9IdvkvO5qKofLCSsn_JszHVlRZZmyuKljVQR2vTccsXFJdC4kPiQlwhR3tbMz6eccg65rZPRP3oJpT2fwNK13VHff_LQbeP6lH5dVJdwiy3igGumoCsOMvplegI5KEeqnJW-AZRF0_e7likoxyQE9dLiadW6fGO6VTNy3t1n5yjtflRvsEslTdVUb_hwOFWyrW2X2ogvwANgKijJfTe9IdlwKPlHUKw0mQz5E0BzHpxkRw_YDymPnpVC3IgonTenBzLQKhhfhBIw3RgfAdG10VU1lGLFbwBBIUPszTF9hibL1nEhISKja2x2Ec7wv1RHT__NhsEI3M4EHpeZ_u1qrnHR1DK_q8MUCM0clWUvuX2m9JBf83IJGsLVV6t9ID3PdC8mMuVgzPSs3OtYjfjIFGL4M0-tA3zLsvuWgsasyuLDTNlYh_Rqj4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca12a42c85.mp4?token=nItcZ1X1gI3AfObKCx7m6zB0xJeTXkGqWBUJii3oO8J5IdxU4Dd0QccgmN59KikSfJ8YPW3JSzNm8zIxgKa5pCXwba7lMlGzwylfFetx91-Hh7e-RO1eayPbfYckvcMZqzwYbGdRY8EwPmokUnY1CM0ksJ-r76SEm7TavalhBfu5Xyi8VxckTYa5R2JKdkEtEhHyCyg7iJE_emiTtOQtYRRYRuEZ-IAcLaE4fZfdH2H7ieBWXogn9IdvkvO5qKofLCSsn_JszHVlRZZmyuKljVQR2vTccsXFJdC4kPiQlwhR3tbMz6eccg65rZPRP3oJpT2fwNK13VHff_LQbeP6lH5dVJdwiy3igGumoCsOMvplegI5KEeqnJW-AZRF0_e7likoxyQE9dLiadW6fGO6VTNy3t1n5yjtflRvsEslTdVUb_hwOFWyrW2X2ogvwANgKijJfTe9IdlwKPlHUKw0mQz5E0BzHpxkRw_YDymPnpVC3IgonTenBzLQKhhfhBIw3RgfAdG10VU1lGLFbwBBIUPszTF9hibL1nEhISKja2x2Ec7wv1RHT__NhsEI3M4EHpeZ_u1qrnHR1DK_q8MUCM0clWUvuX2m9JBf83IJGsLVV6t9ID3PdC8mMuVgzPSs3OtYjfjIFGL4M0-tA3zLsvuWgsasyuLDTNlYh_Rqj4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
احضار سرباز آمریکایی به خاطر حمایت از مردم فلسطین
🔹
سرباز آمریکایی می‌گوید من قسم نخورده‌ام که برای اسرائیل بجنگم من را به خاطر چند پست حمایتی از مردم فلسطین احضار کرده‌اند و می‌گویند مشکلی برای امنیت آمریکا هستی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/658648" target="_blank">📅 08:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658647">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
نیویورک تایمز: واشنگتن در حال برنامه‌ریزی برای کاهش تعداد هواپیماها و ناوهای جنگی اختصاص‌ یافته به عملیات‌ ناتو در اروپا است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/658647" target="_blank">📅 08:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658645">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s1e-R6w3CxjmK78s3ptZrMj1eyx6BPube6YvJvshB20DsQEcNURnooL2cO_cJYW5-BkFe3uQvyEShNg4YL4L75UiztVr_bqVmrrt1WciPXb3KKUlK4YLJ0f3srEvi6FWTTBa1ktmruS2n59v3-W6pYCsJQFpohkwyJU-_yriDdI2g6ev-to2YzVCs4s0aEXJ4BgyawwAOh-Cr6MXwmrKV2BcdIMFwXRrEVTS8C3KvqNzCuuQyNrNCM2f7zrwu_HgeHeuOd9PMoYLCCAJEo3Ivj7ZcWdo0jzln11JuWbSJFgMesBdm_7-1NBZ1hEAPeFEsg8ysVckFSa4Tk4r9ijw4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CbZhVwNaHtHhZs7TAgbWc2-8s1Ea5Fng7jJXjj3MJ9iTc4FbAhsXFptM5jLtjtIKH0Ykf5ehJmxPxbf6otuRmYLKje_uFSQICoUj_UqrXg_1jh_EwaeXs2DImDjsZbpyGsCNOX1ceOelUg3sqtEmjCAOqndOQKpJ70rcZfxsUdXd5qUFVaIDxb3m5VCioe2ftWQTMEdYRNkW61Arwht6BHtarPpQKgbKh8bTJCUdByqq29iLrtS5ufdrRla-kvbWr_6k6i5nX_HaAxjQleA5aVfKMeEzJDqNx0a-asU4zuLbjTiOYCM_iQgAW7m2o2etEEw7Ek8txP6aqYbPydFHoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
فوتوشات‌های بازیکنان تیم ملی فوتبال ایران برای جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/658645" target="_blank">📅 08:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658644">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTrLnFKC3GPlQQXvYgDtmigchKgRtncHMnABoSBzSQcR2lxT2U5PCE68AA72bobS-z1YjIG1hGv1NJNnVHQ-7aSt4au6s0NmiiAU3BIe4NkG9LFYsf_itqFZ9yPW00PMffspfm1bfkOrldpC6NWMzSX83o7hOijZDGIVG3U5iuIcTufeXlUc9MGb2f5YQApeKMhK1AozAdv4-7uHMowsp7pfJPZ6xq0qe8ArqvHAR_e9u71YhNdhydArq0Ypgq20u1sqVHz-IhF-eQtXY_3R86ZW0qawdOoKKjKi1OsrY_RbNREiD5ju0e5Cgx-bAMOcCgoSc4CWbAIP4EXbf_9sbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس جمهور سابق کره جنوبی به ۳۰ سال حبس محکوم شد
🔹
دادگاهی در سئول رئیس جمهور سابق کره جنوبی را به دلیل تشدید تنش با استفاده از پرواز پهپاد در خاک کره شمالی به ۳۰ سال زندان محکوم شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/658644" target="_blank">📅 08:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658643">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
مقام آمریکایی مدعی سرنگونی دو پهپاد ایرانی در تنگه هرمز شد
شبکه فاکس نیوز:
🔹
در پی تلاش ایران برای هدف قرار دادن کشتی‌های عبوری از تنگه هرمز، نیروهای آمریکایی دو پهپاد ایرانی را سرنگون کردند./ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/658643" target="_blank">📅 08:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658642">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
زمین لرزه‌ای به بزرگی ۳.۱ ریشتر بامداد امروز پردیس تهران را لرزاند.
🔹
هشدار بانک جهانی: جنگ ایران و آمریکا اقتصاد جهان را به پایین‌ترین سطح پس از کرونا می‌برد.
🔹
اردوغان: نتانیاهو در مسیر هیتلر حرکت می‌کند.
🔹
فایننشال تایمز: فرانسه و آلمان به دنبال کاهش اختیارات اتحادیه اروپا هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/658642" target="_blank">📅 08:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658641">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n00hVtOt5JRgFaceV1lYuZ029mmw9Rb3UqF3jSc9oLZrEw69r8nnneHjUaeUKs3k37gab-X6UDR3ruBX0mX7O7VlOTdspBR2Zjr_9bLwdG9cl50PQsjegeVjay3IRXDs-_R1oxHKBKtkY6CzXH2dcNbtYmQs7cwzyGIOGeO3xxaAekjhcCCwNXTcWDYHFyXdoVEd3TjYETivjYiaFrYqgviurpow7PL-v4I2i4E-fZDJuC-TBtX1gtq2nCOV65FvvgTXod-rtlO6d3BMB1PLVZhrT5oPhJt_Koynkah1WJPgxtu_QgluAhm3j5ZRmn70Q6MDDOz8u3isIrLVHyVeBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سه نوجوان هندی با افشا کردن تقلب در تصحیح برگه‌ها، دولت را به دردسر انداختند
🔹
سه نوجوان هندی با شناسایی حفره‌های امنیتی و تقلب در سیستم تصحیح آنلاین اوراق، موجی از اعتراضات را برانگیختند.
🔹
این افشاگری منجر به بازبینی صدها هزار برگه امتحانی و برکناری مقامات ارشد سازمان مربوطه شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/658641" target="_blank">📅 08:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658640">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DECVw4wf6TMHJ_OyIMPrVBReEVv2tClA2Zqn0-v71HnpucrtJNpeOQMjyfiTQGcNSzL21PWaGUSlYxknkF9Gmg0v8OkAHd9jxoyJcTBWnhWmEp32kSPyGdNVJmtqfDORY1RGyCMZlQkmqujCdDOpEOjLZl8z_jOvVa8CEarWSwESbjIP7P1VyqFqhq_OaA74h76TD-2pJTWv_St9a7iF-kWAs3ksIsE1M9LAdnIr22blqca5pzBolHYiKAEh_qjv4LJdxnnKkqyJtGZ9NChgeXSO7IlswO3ksMW2mzMlH0Ur5dTMF7KqNHFod47uyVrdmlSJOwVw3OTG77gakkMP_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وَلَا تَحْسَبَنَّ اللَّهَ غَافِلًا عَمَّا يَعْمَلُ الظَّالِمُونَ...
And never think that Allah is unaware of what the wrongdoers do. He only delays them for a Day when eyes will stare [in horror].
گمان مبر خدا از آنچه ستمکاران انجام می‌دهند غافل است؛ فقط آنان را تا روزی که چشم‌ها از شدت وحشت خیره می‌شود مهلت داده است.
#WillPayThePrice
#تقاص_خواهید_داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/658640" target="_blank">📅 08:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658638">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/508054e440.mp4?token=h8eb4Jmate7qpW4Efxz_dyGVVa2NR9Wv5ejFK7Wv8EzGll8yKpJlVlgc-65s4rj1sC5IX-w7_DKKbKIAh2QwxB84cmzowIRGDatAeKX_6t9W_EzGec11Iy0N6T9w7qoSuwM0Onlegeo-lHKdIZaPnWliVHXrXWL04b5p3-pq03SREhHRDjQQ1K7ZYCgBAaXILZf3nYibymm1HQD0i2Di7SXxB40WvSN9IIN_M7HD8SuMyS4cC_RufSAg6hGSXbPZTfo96Nf18RaHCfPZqIqmYZ_pM7T8OJfievukQqskvTugBB2NXag8UXC9GWOHkITCabKxRmNzv5ktAHzdeNZvNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/508054e440.mp4?token=h8eb4Jmate7qpW4Efxz_dyGVVa2NR9Wv5ejFK7Wv8EzGll8yKpJlVlgc-65s4rj1sC5IX-w7_DKKbKIAh2QwxB84cmzowIRGDatAeKX_6t9W_EzGec11Iy0N6T9w7qoSuwM0Onlegeo-lHKdIZaPnWliVHXrXWL04b5p3-pq03SREhHRDjQQ1K7ZYCgBAaXILZf3nYibymm1HQD0i2Di7SXxB40WvSN9IIN_M7HD8SuMyS4cC_RufSAg6hGSXbPZTfo96Nf18RaHCfPZqIqmYZ_pM7T8OJfievukQqskvTugBB2NXag8UXC9GWOHkITCabKxRmNzv5ktAHzdeNZvNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یورش نظامیان متجاوز صهیونیستی به محل اسکان آوارگان در جنین
🔹
نیروهای متجاوز صهیونیستی به خوابگاه‌های دانشگاه که محل اسکان آوارگان جنین در کرانه باختری است، حمله کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/658638" target="_blank">📅 08:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658637">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ادعای تازه آکسیوس: زمان رفع تحریم‌های ایران مشخص نیست  اکسیوس:
🔹
هیچ تاریخ مشخصی برای کاهش تحریم‌های ایران وجود ندارد و اجرای توافق تعیین‌کننده زمان آن خواهد بود.
🔹
به ادعای این رسانه آمریکایی یادداشت تفاهم تمام جزئیات مسائل هسته‌ای را شامل می‌شود و تمام…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/658637" target="_blank">📅 08:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658636">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLmAQpifX1hDHR9J5cB79ffQkrkPqlxzBOnjLoLNh0SzPtEVsNAWvWHI71zQqruWw2zpwfcfuqBQt6w6MvFxDkb1FcqbWL7dQ1cRgfgOiskHkV-zPDUyAYO57sfGAc9ejKzYmsg6w0HyLQcEv-MDvEyQj8NRbUTAgyaQqIN7lj08O41frKLwtcNtqnHJB0BmHZVlwYkmNjIqeJy1VXH2ArEEL5caLrp3ACYvEzfSKiGoFaI_lVJWxvtFe46LSApvtqvp3vN9wrFNrS-9skw4J4fAjR7yXCTTjfIcodQOxrj7IdtE1jgiJVbQtvkhuxyk-BTgYlKsBsbq7Q9bzS5IKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پوستر AFC برای تیم‌های آسیایی حاضر در جام جهانی ۲۰۲۶ با تصویری از مهدی طارمی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/658636" target="_blank">📅 08:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658635">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ادعای تازه آکسیوس: زمان رفع تحریم‌های ایران مشخص نیست
اکسیوس:
🔹
هیچ تاریخ مشخصی برای کاهش تحریم‌های ایران وجود ندارد و اجرای توافق تعیین‌کننده زمان آن خواهد بود.
🔹
به ادعای این رسانه آمریکایی یادداشت تفاهم تمام جزئیات مسائل هسته‌ای را شامل می‌شود و تمام الزامات ایالات متحده را برآورده می‌کند./تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/658635" target="_blank">📅 08:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658634">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGfyWY3JgxYpQazijwsuh8TL9MN715WAcybOCvR1Q25UETB_wt9KGK80rrNN-Ys7OHx4idw8WiQPvR9vRS0JJ0T9KmOM4Ef7X66b0UzBNP6Nv1gvriuUoi0ZL4hypwbl-pZU0Q-PXB4_WyHcXRA7W0O02R_eqrZvrABqkHAZ1hv6BgF7oHDPmwxzc1HiAL6RE55Y4K2fXm1O-URq6SycRE3p03i1RcDb3xnY_E3ojvGFhRtuUIXtotokec2IHEYTM2rjXAVUo-1GoBrwxIzhPXeSSmMUjrIeOX03aGuHtSB_a1vqP3zhhGOFaXeb_6iaZqwlBjkr1uXVzw4uOjakrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایلان ماسک پس از عرضه اولیه سهام اسپیس ایکس، به اولین تریلیونر جهان تبدیل شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/658634" target="_blank">📅 08:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658633">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9wu-6u-Z9LIBCoukcf_mKru04wNphhjvn_K4nfTwgu6rj3rYI5Pvr8hQhPyjg3GFwswTxZkLZwqEDeMu4O7LAf2Ta08s7LfHQtpa4eErS-D90FyFE6BxgZAyvgiD1MWLMrPqCJQzr5cZvFSov1BistY961qdL2ih-VWKpShkNXrNDbTo5InioMNZURkPncQQsoadO9Bm78nrkfMD2uwPX6g0DtHglAaS3rDvWmTqhyRy2EBtqpOYSR8_nZZ3l7rPT3GXfAyYBAPwe7dP6aZ5qNEr4mUo32A0j7ZMRbjlDdbbkdn6uHJ8msbrltG6XtXYOj63AN1z6T0ttCCiDPKjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنایه خبرنگار اکونومیست به اخبار ضد و نقیض ترامپ
گرگ کارلستروم، خبرنگار و تحلیلگر مشهور اکونومیست:
🔹
"اعتبار آمریکا تا آنجا تنزل یافته است که رئیس‌جمهور می‌تواند از دستیابی به یک توافق دیپلماتیک خبر دهد، اما واکنش تقریباً همگانی این باشد که:
"صبر کنیم ببینیم {خبرگزاری} «تسنیم» آن را تأیید می‌کند یا نه"
.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/658633" target="_blank">📅 08:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658632">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDejc32DtRKHavLU_xDBwIriWPmTuVjBrVBP0luH8d-ppHrUjJnhUBj1vElMVmQetBaMwPc18ZLTP0XIayEcdXgYuaW-IZLiHpasMl1-8P5cQqV1t_mphCHeziZ1w9eKEn_Tl7OiethWn7AYckeVRibFWx7T6MoV_ZnrK8uwajs-PZRN73k597zVpKH0uaiG5udQCqN2k1k8XByLJC7utDRVqcZZPdhlR9gZroKuG4UMwrKwYGXq8eYsPKJ3_pjvtdCXjD725PSt60rI_XjFrXpo-qOPOMISfHHHy7_Ju_u1F3DCHDmB4YdWTnuJSv3zmpmj0Y3xqkrL7RH6iWShWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رده بندی گروه A در پایان روز اول جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/658632" target="_blank">📅 08:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658631">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
اذعان نیویورک تایمز به احتمال جنایت جنگی جدید آمریکا در ایران  روزنامه نیویورک تایمز:
🔹
براساس تصاویر ماهواره‌ای، حمله آمریکا به یک تأسیسات آبی در ایران انجام شده، اما مشخص نیست هدف‌گیری عمدی بوده یا نه.
🔹
اگر زیرساخت غیرنظامی عمداً هدف قرار گرفته باشد، ممکن…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/658631" target="_blank">📅 08:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658630">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHrEet9Av6UvKL4fAzY7jSbjzniKty97qIJsZLlIUhNMdaC4xGNq1a-lQ0LE2h72S4P7RycYDF-29amNd6nHsMPTtlsLLvnCy-8RCN1yK4ZTSr4Yg69XD-v5UpMBVaJxeBNPlH91sZfRdCxRv0EV0avrXktLyU0utAWWJUMQpTINlxkKuQiSaELYGAXgStU1jnOWkdDrVD_llUxxGFJbf4EUC1N9BANJgfoW2Qn5ezQ5J24YhKd1i_yAEBW2Xv0-IMHArLYCIoKzFrPYmv1UBfr-pYSlVnKiAHmc6KeqPna8wHGAMaQ4fcHQ2I3d2El02rLHRk8lR3Q9lZor0L6xvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ: امروز به جنگ با ایران پایان دادیم
رئیس‌جمهور آمریکا:
🔹
ما امروز به جنگ با ایران پایان دادیم و آن‌ها موافقت کردند که هرگز سلاح هسته‌ای نداشته باشند؛ این همان چیزی بود که ما بر آن اصرار داشتیم.
🔹
کل هدف ما همین بود؛ این موضوع ۹۵ درصد از هدف ما را تشکیل می‌داد و آن‌ها این کار را به محکم‌ترین شکل ممکن انجام داده‌اند.»
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/658630" target="_blank">📅 08:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658629">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1V3_M4vOuIHSgqi7PnLiN3DTlov1Ld1m2chnV-kLwvQWo2Wtg2YWZlOxikQuMGXKPE5uylt7lU6fr1-ZG6jjvlAmEeQFZwzv3cu7G9_paOyD7u4ZUmBEb2a-TJv7HlyrZ0SC4IxfftsZdTJW6X0rAkTeIW5Ni_9Q_54gQu1nJ2ASVE7hEFqMz4mZby51C-W1ubFAVyUtLcr93d16l1hlYnnPGY0GsPRC0wYlHn7pZaYtJO94WhtEbyu3hDMFQe6E8HttZMeRJCAlOFQtbfAVNhn0A1xzriwZIWyJuDSZkhcgtipY8_5AIPR68fx6E9ygcmTyhvch3ZLeIfdaKXHDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین برد آسیایی در جام‌جهانی
🔹
کرۀجنوبی ۲ - ۱ جمهوری چک
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/658629" target="_blank">📅 07:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658628">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
پلیس مالزی خواستار ممنوعیت کامل سیگارهای الکترونیکی
🔹
پلیس مالزی درپی شناسایی ماده مخدر مصنوعی جدیدی به نام «پیو پیو» در مایعات سیگارهای الکترونیکی، خواستار ممنوعیت کامل فروش و استفاده از ویپ در این کشور شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/658628" target="_blank">📅 07:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658626">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcJAM3URhoJocPcGCrcFdpS-93_mA-emJxE5TBjk29dGscn2OawhwpKPiTfxl8cKlAQwbRuJRvzuqHdoJl0o6hLMTNt8CMgJKuz_5kquJ09uEof32iJgTNYnJrMs8fIV4NfSrq8wgpFWi9aHz4PqZuiDn52Ewp14NJix0C2Q_WCXyY9fR2NfhLTCnzJ4oKTq8KsjHDHsvcyvQiJOYdOFRxa0Oy8VXMbqFESs-pL9fpTourpOARhP9Kl5qSf9eAmU1nvAawVzSbQoIaPRRBj_c7Se88U-znTlfm3xTjifCG_cL7PFnBAUjYZOUFOB0CgR6UM-h60t3PQmVDV1x6DfaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/voGDwvnomRydzbo_SSOOAFU-gYQV825Gddqv1olaNBOzieW4d8-DC0CkN4SW8da3UOpVueK2y313yYT6rpb8xQaBjBDSxV4M1neX3mdqD3FG8B3zgDxk_89Lb4xkweVDQ_NCoeEqOPdaqDerP7cQ4afrRPIHN5XbkQ693T63hR9XrDy7VJlGqqZem0IDPslV3Zrz-1gxnP1OeghwemcynvYKn_2D5QZNMqQX0wMovpF4MFpN4Jp07qCa83MnZ-FLr7TB7xybXuk34ECfV03rmcqHsaaE1ML-HJn7rnvNbtjaqkRR9jaOasjEyNQZie8fqC-AjnmM_olbwo_CWfffhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حنظله: در پاسخ به حمله علیه زیرساخت‌های آبی ایران، تأسیساتی آب ایالت کالیفرنیا را هک کردیم
گروه هکری حنظله:
🔹
در واکنش به «حملات آمریکا به غیرنظامیان و زیرساخت‌های آبی ایران»، تأسیسات آب ایالت کالیفرنیا را هک کرده است.
🔹
باوجود دسترسی به سامانه‌های مرتبط، از ایجاد اختلال در آب‌رسانی شهرهای آمریکا خودداری کرده و این اقدام تنها «هشداری» به واشنگتن بوده است.
🔹
هرگونه اقدام علیه ایران با پاسخ متقابل در حوزه زیرساخت‌های حیاتی مواجه خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/658626" target="_blank">📅 07:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658625">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luMEng6W8cGVhszROAsEQ6SQOM_zamRGKnevPJEzaEi3LTRldUo0r7fpZN5FI6Rm6VjASlVo4b_YI8gxaxKXiTtc4rq1I9HD4MnbGkUXRS49TSomi6nx2eKaYqy7kFwrYEMeumc3IAgiVDHIsYEs4XXaZ7iYI4PGScsubApOXnADCeM_y3OVl_Harc0TwVgjoOgDfSM6sentaTAAJ3nH-tfcHHEGvuuxCHID508dWy-rBQEaKeDIHC8xr2sCePDRyooZ2_MK3ybVfOtjvTusI7kfTxDJZBy9YYcdMvymtbY-3JeZbaJKRMUxkyHdmNMjLDHnmOrg6WgEisCcO0g0MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۲۲ خرداد ماه
۲۶ ذی‌الحجه ۱۴۴۷
۱۲ ژوئن ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/658625" target="_blank">📅 07:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658623">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔹
فرصت محدود
🔹
دوستان تنها کانالی که وقتی دلار ۹۰ هزار تومن بود با قطعیت گفت دلار ۱۵۰ هزار تومن رو میبینه…
تنها کانالی که وقتی طلا حوالی ۸ میلیون بود از طلا ۱۵ میلیونی صحبت میکرد…
تنها کانالی که ماه‌ها قبل از اتفاقات اخیر درباره رسیدن درگیری‌ها به ایران هشدار داده بود…
✅
بیش از ۱۰۰۰ تحلیل منتشر کرده
✅
حتی یک تحلیل پیدا نمیکنید که به واقعیت تبدیل نشده باشه
✅
حتی یک تحلیل حذف نشده
✅
حتی یک تحلیل ویرایش نشده
✅
حتی یک تحلیل پیدا نمیکنید که با تحلیل‌های قبلی در تناقض باشه
اگه میخوای چند ماه جلوتر از بقیه باشی همین الان بزن روی لینک زیر و عضو شو                               .
https://t.me/+mdMYdfjfDfAxY2I1
https://t.me/+mdMYdfjfDfAxY2I1
https://t.me/+mdMYdfjfDfAxY2I1
https://t.me/+mdMYdfjfDfAxY2I1
https://t.me/+mdMYdfjfDfAxY2I1
https://t.me/+mdMYdfjfDfAxY2I1</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/658623" target="_blank">📅 01:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658620">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
فارس: ایران اجازه عبور نفتکش متخلف از تنگه هرمز را نداد
🔹
دقایقی قبل نیروهای ایران اجازه عبور یک نفتکش متخلف که بدون هماهنگی وارد محدوده تنگه شده بود را ندادند.
🔹
گزارش‌های مردمی نیز از شنیده شدن صدای سه انفجار در فاصله حدود دو کیلومتری ساحل از سیریک حکایت دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/658620" target="_blank">📅 01:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658619">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
شنیده شدن دو صدای انفجار در شهر بندرعباس
🔹
دقایقی پیش، صدای دو انفجار در شهر بندرعباس توسط مردم و منابع محلی گزارش شده است.
🔹
منشا صدا هنوز مشخص نیست اما پیگیری برای کسب اطلاع دقیق ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/658619" target="_blank">📅 01:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658617">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88480d9614.mp4?token=gYCiJUh-ndBSCIQHho1uZqGilSrRIX5nb7UxnrAIGDnA4uiV7QFRIZygphTWOMHXcjZkot1BQJHDrHHFlagHJYdUflVuHk61AlMIAsZSVlNz5qW1P4srDNVqsl_gieSxIJPhOTHApmECEkqNsdI88DJEDxAF4nlevmONrXzyPwM2to_M-P24yEtSVpBz9rgbP0_gWx3wWv7ejwXDYFA76uRwXp7IocQviYhOE7QOQM8VE2uGLwaP16K6urtaiNXtZvxRzUU0vYlERsfSCG0_dFDlkHto-ako_ASImJJQlxGp2bJydag32U7B8I1ZkS1rdals03o2_WGu0Nhe7H4hmSAsmMmBXzvahIHh_obElxGB7-f0fZDw2TmaiNMnSAoAZz2LSz4Ghk4pyvvDNN6_4w0Q_MtIcPDORDtXG61NrmBDXiMyrrvGPQhzIlmjkzWf4fMEgGfRtG3t8EPrhnEhRCvyycyjtx03UPpwJDnJj7ujtCcH7ke7NUpJavgHASYK7anXTX4z7hO0CU2ce0b4cFthH63zY_Dux1pFiUNl8BZg1NGR1u-QYEbqouFld_GZ3NzugkIvBSN-VmbRbpvLxHmcxE178h-OZfXkt1Q9RwyOU1P-6YCkYWHaz4ZZ-9rIPAM1r80uUruRIPD9Z5el-7A5qNL5b-q9c4mYGNKvLjM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88480d9614.mp4?token=gYCiJUh-ndBSCIQHho1uZqGilSrRIX5nb7UxnrAIGDnA4uiV7QFRIZygphTWOMHXcjZkot1BQJHDrHHFlagHJYdUflVuHk61AlMIAsZSVlNz5qW1P4srDNVqsl_gieSxIJPhOTHApmECEkqNsdI88DJEDxAF4nlevmONrXzyPwM2to_M-P24yEtSVpBz9rgbP0_gWx3wWv7ejwXDYFA76uRwXp7IocQviYhOE7QOQM8VE2uGLwaP16K6urtaiNXtZvxRzUU0vYlERsfSCG0_dFDlkHto-ako_ASImJJQlxGp2bJydag32U7B8I1ZkS1rdals03o2_WGu0Nhe7H4hmSAsmMmBXzvahIHh_obElxGB7-f0fZDw2TmaiNMnSAoAZz2LSz4Ghk4pyvvDNN6_4w0Q_MtIcPDORDtXG61NrmBDXiMyrrvGPQhzIlmjkzWf4fMEgGfRtG3t8EPrhnEhRCvyycyjtx03UPpwJDnJj7ujtCcH7ke7NUpJavgHASYK7anXTX4z7hO0CU2ce0b4cFthH63zY_Dux1pFiUNl8BZg1NGR1u-QYEbqouFld_GZ3NzugkIvBSN-VmbRbpvLxHmcxE178h-OZfXkt1Q9RwyOU1P-6YCkYWHaz4ZZ-9rIPAM1r80uUruRIPD9Z5el-7A5qNL5b-q9c4mYGNKvLjM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیزر فصل جدید «حسینیه معلی» ویژه ماه محرم ۱۴۰۵ منتشر شد.
حاج سید مجید بنی‌فاطمه، حاج مهدی رسولی، حاج سیدرضا نریمانی، حجت‌الاسلام سیدحسین آقامیری و کربلایی امیر برومند در میز ذاکران این فصل حضور دارند.
🔹
نجم‌الدین شریعتی نیز همچون فصول گذشته اجرای برنامه را برعهده دارد.
📺
«حسینیه معلی» از دوشنبه ۲۵ خرداد از شبکه سه سیما روی آنتن می‌رود.</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/658617" target="_blank">📅 01:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658615">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در نزدیکی ساحل سیریک؛ جزئیات همچنان مبهم
🔹
منابع محلی در استان هرمزگان از شنیده شدن صدای انفجاری در دریا، حدود دو کیلومتری ساحل سیریک، خبر می‌دهند. هنوز علت و منبع این صدا تأیید نشده است.
🔹
هنوز از ماهیت و علت این انفجار اطلاعات دقیقی…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/658615" target="_blank">📅 01:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658614">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
ادعای آکسیوس به نقل از یک منبع: نتانیاهو هیچ اطلاع قبلی نداشت و وقتی ترامپ بیانیه اولیه خود را در مورد توافق با ایران صادر کرد، غافلگیر شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/658614" target="_blank">📅 00:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658613">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ادعای دفتر نتانیاهو: ترامپ با نخست وزیر در مورد یادداشت تفاهمی که با ایران در حال آماده سازی برای شروع مذاکرات است، صحبت کرد
🔹
اسرائیل طرف این یادداشت تفاهم نیست، اما نخست وزیر از تعهد رئیس جمهور ترامپ به اسرائیل قدردانی کرد.
🔹
ترامپ متعهد به حذف مواد غنی‌شده، برچیدن زیرساخت‌های غنی‌سازی، محدود کردن تولید موشک و پایان دادن به حمایت ایران از نیروهای نیابتی خود است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/658613" target="_blank">📅 00:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658612">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در نزدیکی ساحل سیریک؛ جزئیات همچنان مبهم
🔹
منابع محلی در استان هرمزگان از شنیده شدن صدای انفجاری در دریا، حدود دو کیلومتری ساحل سیریک، خبر می‌دهند. هنوز علت و منبع این صدا تأیید نشده است.
🔹
هنوز از ماهیت و علت این انفجار اطلاعات دقیقی در دست نیست، اما با توجه به دستورالعمل‌های مربوط به بسته بودن تنگه هرمز، این وضعیت احتمالی می‌تواند در همین راستا باشد.
🔹
با این حال، این فرضیه تاکنون به طور رسمی تأیید نشده است/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/658612" target="_blank">📅 00:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658611">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
ترامپ ادعای خارج کردن نفت از تنگه هرمز را تکرار کرد
دونالد ترامپ، بار دیگر مدعی شد که کشورش کشتی‌های زیاد و «صدها میلیون بشکه نفت» را از تنگه هرمز خارج کرده است.
🔹
ترامپ روز گذشته هم مدعی شده بود که ارتش آمریکا در عملیاتی مخفیانه دو میلیون بشکه نفت را از تنگه هرمز خارج کرده است؛ ادعایی که به گفته کارشناسان با آمارها و داده‌های منتشرشده در تناقض قرار دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/658611" target="_blank">📅 00:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658610">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvgK2Uz_KcD3I2X6QWo7xMdzRjKnjy6ked9CC8kooooSTwSNobejnF4AL8HQRI1KgDO6y9R9mgQjaHB7iXDKPcBef0IR4_nUo57H6iO79zHgT3DWU_iS71P_fe14ECOcgTVxnQI_k4MZF-AD6-VLBbl7USpw8QI_ye5is5l-E_k5cFAgLTUt_vOa556cs6fUJN-O03o_NQmzSY6UKnj52YLqfmJrsfWBGjvKFzUpU_7-DYtXHeTRHps0UDuqRNjB3Rdr6QsFQ64qDD8mitNjKx6bpaJw9Ao6ZqcsAwc9JoYWvFdIp-BNUBdNwTP7sEAX59Tc0RlMDh-SL1WPkHaTuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعداد تماشاچیان حاضر در بازی افتتاحیه جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/658610" target="_blank">📅 00:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658609">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: ابتدا باید مراجع ذی‌ربط نظام دربارهٔ جزءبه‌جزء هرگونه تفاهمی به جمع‌بندی برسند‌
🔹
به‌محض اینکه به جمع‌بندی نهایی برسیم رسماً اعلام می‌کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/658609" target="_blank">📅 00:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658608">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: اعلام تاریخ برای امضای تفاهم، گمانه‌زنی رسانه‌ای است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/akhbarefori/658608" target="_blank">📅 00:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658607">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: به‌دلیل اقدامات غیرقانونی آمریکا در تعرض به ایران، روند دیپلماتیک هم تحت تأثیر قرار گرفته است
🔹
میانجی‌ها فعال هستند و ما خیلی شفاف به آن‌ها [مواضع‌مان] اعلام کرده‌ایم‌.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/658607" target="_blank">📅 00:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658606">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: اگر قرار بود ایران تحت فشار و تهدید از مواضع اصولی خود کوتاه بیاید، یک‌سال قبل این کار را انجام می‌داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/658606" target="_blank">📅 00:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658605">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUuAOX1sQZ5-rAw5v27VMDIP9SAP5in9TLiX-ojwn8TdGEqjMJnBUiILLyN9PlrR0-YzkElsG1J3j3jUq3EP3SimDBoxurma8zlMIon-pTts70MuokEMlU9FzumXc2SDH7eXeJDBc3z_JE3CKTm-Td-vgASaJKXb5KBCH6dIJTM1mWyf7nJYtnogXEbfSJkQVMik9BkZaowGallE82zxw9WBvi7geJZzGc4KmO6Hoc2tTJPD8LLo7txTHrMnW5GeluEXq9yL5au0aJadnzHi_w8vGEEI9VbSR7duSOWwYGX3gOT5ACGxDIXFh7sEgF8PLTQFliI6EkbqO14cK3OKPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک روز عادی نخواهید داشت. هر روزتان را تبدیل به کابوس میکنیم
לא יהו לכם יום רגיל. אנחנו נהפוך כל יום שלכם לסיוט.
#WillPayThePrice
#تقاص_خواهید_داد</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/658605" target="_blank">📅 00:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658604">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
بقایی: وضعیت مذاکرات از نظر ما این بود که بخش عمده متن تقریباً نهایی شده بود اما آمریکایی‌ها زیاده‌خواهی می‌کردند و درخواست‌های جدیدی مطرح می‌کردند
🔹
آن‌ها در حال القا هستند که جمهوری اسلامی تحت فشار به توافق رضایت داده است، در حالی که ما به هیچ عنوان از…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/658604" target="_blank">📅 00:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658603">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c497468ed.mp4?token=Fzyi_i-20fm4s0ZrLTaSI50dOtgZ7-QatMV6qFNOviWcStG2zOwTkgBDnjQ1RmrrMwEL8LcXzBpcHNoloIvcCNudpk5s83gr64_VUwoj3VYirMscGRClchyZbAXwym7JsQFDMFioTGc2X5zU0Zm41CVTL291ok8GIX9iqIhca050yMUl1F5UFmpazXwDFIaiVxBxaZdrXL1VZz4DbRwv1jvC1ehx2PhK9vursmi_DwPyyyd338g-J2cCpuHvkGBYRz8amCBm6LpSJe4N1q59d8Y90fWjvLCWGZ8Dsq355NEGECr4E9DUDBVRjrPerdjXIRaLzzil-scUKhGWxcKyqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c497468ed.mp4?token=Fzyi_i-20fm4s0ZrLTaSI50dOtgZ7-QatMV6qFNOviWcStG2zOwTkgBDnjQ1RmrrMwEL8LcXzBpcHNoloIvcCNudpk5s83gr64_VUwoj3VYirMscGRClchyZbAXwym7JsQFDMFioTGc2X5zU0Zm41CVTL291ok8GIX9iqIhca050yMUl1F5UFmpazXwDFIaiVxBxaZdrXL1VZz4DbRwv1jvC1ehx2PhK9vursmi_DwPyyyd338g-J2cCpuHvkGBYRz8amCBm6LpSJe4N1q59d8Y90fWjvLCWGZ8Dsq355NEGECr4E9DUDBVRjrPerdjXIRaLzzil-scUKhGWxcKyqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم مکزیک روی ارسال دیدنی
خیمنز دقیقه ۶۷
🔹
مکزیک ۲ - ۰ آفریقای جنوبی
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/658603" target="_blank">📅 00:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658602">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b73ad01da8.mp4?token=jh-BXK11EySnUctJigVZypCoSWc1J9c_-IeEcbbLM7dm7D-eM3CWLn_qq0PyGgGPRKifcdduvTRFh6kYAR32oQ94sEcgW7fK2hIT2HX094bACiNH48ZU_asjukCeFVzxQ7Kp76suTFZlUV1L0gqf8TrzI6qp6Dtovj9OgKpQoaZLS2KHReVrUskmksoYTHeqogJx3HjwFTE6YkDm8fLRPptr6XgYZKxe5rFUc-GUWzxkyWQsx-phZx45R0gAFvXZmFk7Tvo_FIT9fFg6m52VYyrpuQj398wkyfsWQ_qyQQWG_3lZZ3Yj6qITjkCdv98iYHb-ZmYn-u8AQsz7xiAJMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b73ad01da8.mp4?token=jh-BXK11EySnUctJigVZypCoSWc1J9c_-IeEcbbLM7dm7D-eM3CWLn_qq0PyGgGPRKifcdduvTRFh6kYAR32oQ94sEcgW7fK2hIT2HX094bACiNH48ZU_asjukCeFVzxQ7Kp76suTFZlUV1L0gqf8TrzI6qp6Dtovj9OgKpQoaZLS2KHReVrUskmksoYTHeqogJx3HjwFTE6YkDm8fLRPptr6XgYZKxe5rFUc-GUWzxkyWQsx-phZx45R0gAFvXZmFk7Tvo_FIT9fFg6m52VYyrpuQj398wkyfsWQ_qyQQWG_3lZZ3Yj6qITjkCdv98iYHb-ZmYn-u8AQsz7xiAJMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش فوری کاربران فضای مجازی به توییت ترامپ
🔹
دونالد ترامپ در توییتی ایران و آمریکا را مقابل هم قرار داد.
🔹
کاربران فضای مجازی هم این توییت را بی‌پاسخ نگذاشتند و با الهام گرفتن از کارتن معروف فوتبالیست‌ها و به بهانه شروع جام جهانی ۲۰۲۶ به رییس جمهور مغضوب آمریکا اینطور واکنش نشان دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/658602" target="_blank">📅 00:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658601">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: قطر و پاکستان به‌عنوان میانجی‌ها فعال هستند
🔹
وضعیت مذاکرات از ابتدا برای ما روشن بود و بخش عمده متن نهایی شده بود اما آمریکایی ها مواضع خود را تغییر می دادند.
🔹
ایران ثابت کرده است که در آنچه را به عنوان خط قرمز معین کرده است مماشاتی…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/658601" target="_blank">📅 00:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658600">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsTLDiCawPNC9tNot15od0nKr9b1KGsLPaNhMAwEnvptnA5sdsdvB9s3WKa-nOTWRbGFdUZHcbw7SwaOMN3UGG83hay73R5Q_87cFTIQlYS5jM6jIlwtqsYFAfzv3G9jxQPUmFSVFW93pwp9A_DPFvZyjU2ZTYZ3aF7-TlVFke_0ya_G1UuZTkI_QsAQYVwW4ratVAcO1WoPQQaY-sSR3fX6PSfoMP-M1rS77rWzF5d4OsEOdrwVIdYA2-k19tzUH5hrE4MVMcLdQlZxqF1Y8Fg1FUvnlEuQUsLR65Te_uGZzpNjdTLwSgX678FjaDosTUtJ6dAYZuBld-XOMhwp-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/658600" target="_blank">📅 00:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658599">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: قطر و پاکستان به‌عنوان میانجی‌ها فعال هستند
🔹
وضعیت مذاکرات از ابتدا برای ما روشن بود و بخش عمده متن نهایی شده بود اما آمریکایی ها مواضع خود را تغییر می دادند.
🔹
ایران ثابت کرده است که در آنچه را به عنوان خط قرمز معین کرده است مماشاتی ندارد. مواردی که درباره توافق مطرح می‌شود گمانه‌زنی است و موضوعی نهایی نشده است/ صداوسیما
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/658599" target="_blank">📅 23:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658598">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e6aafc5a.mp4?token=M5RPnTZFhNVMWrHrBCxtlgTnw4Lz9vB_RUVJi-ab7pc2-yya829tLGvMI5yeJpWiN6YEBBGv70CHlYPwXFDMY_HuKPraKxqIaaGMg7nhoFF8L-8YntKxRAewRbmInfXKNhxZBEOVSJxGLMb40KQW16qmjyQt3SASji7hKYm2e8MsFKrxyR7sGG2Z5ArCvs0vrZWfEyDgLRLTSkFNqEhQ0iWPvZ1OI78xj9GqeoDtdVmEtdL8H-te8JuB19j78S2xdazOQW3Psl151HPWCJJN1qOEt0EjhC1M7lBCLmJpAnHPFbewDKp6EPmT0LrRszGT7Abu6bF1ZBmZf6g4gpkeiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e6aafc5a.mp4?token=M5RPnTZFhNVMWrHrBCxtlgTnw4Lz9vB_RUVJi-ab7pc2-yya829tLGvMI5yeJpWiN6YEBBGv70CHlYPwXFDMY_HuKPraKxqIaaGMg7nhoFF8L-8YntKxRAewRbmInfXKNhxZBEOVSJxGLMb40KQW16qmjyQt3SASji7hKYm2e8MsFKrxyR7sGG2Z5ArCvs0vrZWfEyDgLRLTSkFNqEhQ0iWPvZ1OI78xj9GqeoDtdVmEtdL8H-te8JuB19j78S2xdazOQW3Psl151HPWCJJN1qOEt0EjhC1M7lBCLmJpAnHPFbewDKp6EPmT0LrRszGT7Abu6bF1ZBmZf6g4gpkeiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: مهلت شما برای رسیدن از این مرحله به یک توافق نهایی چیست؟
🔹
ترامپ: نمی‌خواهم مهلتی بگویم چون بعد می‌گویید من مهلت را رعایت نکردم. خیلی مهم نخواهد بود چون قرار است امضا شود.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/658598" target="_blank">📅 23:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658597">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
عقب نشینی ترامپ و وعده امضای توافق با ایران پس از تهدیدهای تند
👇
khabarfoori.com/fa/tiny/news-3222314
🔹
مروری بر حملات آمریکا به ایران در شبانه روز گذشته؛ از جنوب تا تهران
👇
khabarfoori.com/fa/tiny/news-3222174
🔹
حمله سپاه به ۱۸ هدف مهم متعلق به ارتش آمریکا طی ۲ موج عملیاتی
👇
khabarfoori.com/fa/tiny/news-3222176
🔹
شلیک مستقیم طالبان به یک خانم تنها بخاطر شرکت در تجمعات اعتراضی حجاب و تحصیل/ ویدئو
👇
khabarfoori.com/fa/tiny/news-3222289
🔹
آقای تاج بابت دیپورت شدن از کانادا هم دستاورد‌سازی می‌کند
👇
khabarfoori.com/fa/tiny/news-3222313
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/658597" target="_blank">📅 23:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658596">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
ادعای ترامپ: تعداد زیادی کشتی و صدها میلیون بشکه نفت را از تنگه هرمز خارج کردیم #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/658596" target="_blank">📅 23:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658595">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
گراهام، سناتور آمریکایی: هر توافق هسته‌ای با ایران باید به تصویب کنگره برسد
🔹
مانند گذشته، هرگونه توافقی که با ایران در رابطه با برنامه هسته‌ای آنها حاصل شود، برای بررسی و تصویب به کنگره ارائه خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/658595" target="_blank">📅 23:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658594">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ادعای نورالدین الدغیر خبرنگار الجزیره در تهران: دیگر همه چیز قطعی و تمام شده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/658594" target="_blank">📅 23:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658593">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
ادعای ترامپ: تعداد زیادی کشتی و صدها میلیون بشکه نفت را از تنگه هرمز خارج کردیم
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/658593" target="_blank">📅 23:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658592">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
توهم جدید ترامپ: به ایرانی‌ها می‌ گوییم... ما از نظر نظامی در جنگ پیروز شدیم
!
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/658592" target="_blank">📅 23:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658591">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fdc227ec7.mp4?token=ZbgBjEZO6DK0USlePwpNFx1X8Y0XRuNbaPeEeJ4HAgbpygCrm20lRkklL7O-3NcQ6QRWqweBpl7FnIkN6OF2Lgz-A-A2ObRBDdM8J8RVNJg1NL9FIGhhB2nYacyXSBDAxO62gZCLg9LYDWJk48uyTsIZfsw7rPjQeQdakVtBcCs32c3mXsuJuIVzlr6AEUTNe72Tc3SKIpjpDIrFYXBW45Lwm1pMNE3Sg6wrMjRYRVH0ZcDo_xLNcxCvFZ4kaofUD-G4AqK2tfPmh9IpZ9GqoNLDeAazQqYBAL9drZihmHhY8c2OLBD537j3QzSuKxOQigJQ09cNRY5KWDQ-OKyKqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fdc227ec7.mp4?token=ZbgBjEZO6DK0USlePwpNFx1X8Y0XRuNbaPeEeJ4HAgbpygCrm20lRkklL7O-3NcQ6QRWqweBpl7FnIkN6OF2Lgz-A-A2ObRBDdM8J8RVNJg1NL9FIGhhB2nYacyXSBDAxO62gZCLg9LYDWJk48uyTsIZfsw7rPjQeQdakVtBcCs32c3mXsuJuIVzlr6AEUTNe72Tc3SKIpjpDIrFYXBW45Lwm1pMNE3Sg6wrMjRYRVH0ZcDo_xLNcxCvFZ4kaofUD-G4AqK2tfPmh9IpZ9GqoNLDeAazQqYBAL9drZihmHhY8c2OLBD537j3QzSuKxOQigJQ09cNRY5KWDQ-OKyKqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: آیا رهبر معظم ایران این توافق را تأیید کرده است؟
🔹
ترامپ: تا جایی که می‌دانم پاسخ بله است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/658591" target="_blank">📅 23:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658590">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f17a9b2ac.mp4?token=qB0sgBzs73JBv85yHX-2XmcaOrdu2WWk9FzktyxzZbj6RaZcNw4rexiiO51FXBhrUnJj6ZTL1J3EXS9-GeLrl8YclzfT1XRXvoARqAIcaD-KRDKHpP7x0JVOrfpwIBMKGfNTuwuoIi4ONky_iRKJQEcjdkA7GCQGHzUKD_1RyYeF3VnQ6RqpHiwFrijo28y5FF2NcjRCT9-rhRrHl3tuiMh_IWkwxXMPK5ep-ugW7C1uFnww04t9mH0IPAi7j-8drCXPD-P02Nlq8czOFMiGwY6XIC2HvLPoOptOxxWKqdt_CTSrwZxITsls8yMb78NAVW9skc7lz4cTgHyBQ0FtkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f17a9b2ac.mp4?token=qB0sgBzs73JBv85yHX-2XmcaOrdu2WWk9FzktyxzZbj6RaZcNw4rexiiO51FXBhrUnJj6ZTL1J3EXS9-GeLrl8YclzfT1XRXvoARqAIcaD-KRDKHpP7x0JVOrfpwIBMKGfNTuwuoIi4ONky_iRKJQEcjdkA7GCQGHzUKD_1RyYeF3VnQ6RqpHiwFrijo28y5FF2NcjRCT9-rhRrHl3tuiMh_IWkwxXMPK5ep-ugW7C1uFnww04t9mH0IPAi7j-8drCXPD-P02Nlq8czOFMiGwY6XIC2HvLPoOptOxxWKqdt_CTSrwZxITsls8yMb78NAVW9skc7lz4cTgHyBQ0FtkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: وقتی این توافق امضا شود، آیا آمریکا بلافاصله محاصره را برمی‌دارد؟
🔹
ترامپ: بله، این بخشی از توافق است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/658590" target="_blank">📅 23:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658589">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bff61170c7.mp4?token=XqFMR6VaSEbRNv4RG6Xx5CnL2bbpfELMWeK_NR64LYjGnyvzdvK3l16rkMDEFAfPQawjGV1DxEiflwPoWBxAeFMB_OMAxTAHjd3hMShY91UeIO_2aTusjCj_0aLev9oQl2HcLx543RfEM6EKJ08nN_6QZ4waZKCv-TlORMgX-HO7mgWATiUyYUSgmK1b6RfNbbFTyZHA4RfgXly27Bp5YrYziIi0zPZ6wxgg_dzW0lrqhuZq0n5LmHkRX25BHEYVWNAmb90-gFYpRQsIr-MOEaU4VT3bWmKeZQlCWvN8SSzcqF0HJSYHbYXOaoXatJzBZ5M_he7YkWtmWOjBQsqcQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bff61170c7.mp4?token=XqFMR6VaSEbRNv4RG6Xx5CnL2bbpfELMWeK_NR64LYjGnyvzdvK3l16rkMDEFAfPQawjGV1DxEiflwPoWBxAeFMB_OMAxTAHjd3hMShY91UeIO_2aTusjCj_0aLev9oQl2HcLx543RfEM6EKJ08nN_6QZ4waZKCv-TlORMgX-HO7mgWATiUyYUSgmK1b6RfNbbFTyZHA4RfgXly27Bp5YrYziIi0zPZ6wxgg_dzW0lrqhuZq0n5LmHkRX25BHEYVWNAmb90-gFYpRQsIr-MOEaU4VT3bWmKeZQlCWvN8SSzcqF0HJSYHbYXOaoXatJzBZ5M_he7YkWtmWOjBQsqcQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رودی فولر، پویول، داوید سیلوا، ماتراتزی و کولینا از دیگر چهره‌های حاضر در جایگاه ویژه استادیوم آزتکا هستند
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/658589" target="_blank">📅 23:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658588">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b10fe89a2.mp4?token=O2KaUdyr38ofub3raoehcBkL8HxinuNm6FEThzXDw8oB1-a0uzpr4HZZn2Fj_AJeBpWteBqw70UkNgRgLVgMJ6dD27Nw6UlK80OuLHYWwuM1i9aX8zCMBMqRxy50BGCxdhygTErNaHX_ez5ZcKR1YcxY9ULSKYVYGcZRlsCJlHePt7CCXIW4mPEghHlYgLlP_luW1_mBRVEINL0u-rQqK7UQk58TW73YI43afnbKdKaqo9x2wtf_G-nJ2NbgPWuTW3581exPqaZx9pivJ48atRrAh0004R5Rhsz49fdyEAGZztoC3Hp9twSmmjkgD3GexDTr0V-Uk5rv-gnnQjGmCQK98Cghbn4jHWpz9idWIhC4cIObzoLqVJdQgo7pLOskOhpqe137IA9weFjY8JQlmF6Fuv2xBmCyH4v7tUeamv_UFFTl7EAVDyfhUDFDZRqfIhMN_MaJ7OUzlXqJdWAVaFwarwCHZS-gO4Y2eVtcZsK7OBSyEYze65fAcScKGDQMonBQFNBtzYDI853GU7oA9KUiVuNdku3WENEWNN6wsdOgoCvG0Kx-bnvbkVx7l1FBR2ciEnYTeJZ11QUjLveRBOZoScw0uriGVfVbMttzx37T8KFsHBVndi2SrCJ2DK9YRY5qc1rRwPMuKYE2oG3eLo5NqB8ump_BLEjad7duMsY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b10fe89a2.mp4?token=O2KaUdyr38ofub3raoehcBkL8HxinuNm6FEThzXDw8oB1-a0uzpr4HZZn2Fj_AJeBpWteBqw70UkNgRgLVgMJ6dD27Nw6UlK80OuLHYWwuM1i9aX8zCMBMqRxy50BGCxdhygTErNaHX_ez5ZcKR1YcxY9ULSKYVYGcZRlsCJlHePt7CCXIW4mPEghHlYgLlP_luW1_mBRVEINL0u-rQqK7UQk58TW73YI43afnbKdKaqo9x2wtf_G-nJ2NbgPWuTW3581exPqaZx9pivJ48atRrAh0004R5Rhsz49fdyEAGZztoC3Hp9twSmmjkgD3GexDTr0V-Uk5rv-gnnQjGmCQK98Cghbn4jHWpz9idWIhC4cIObzoLqVJdQgo7pLOskOhpqe137IA9weFjY8JQlmF6Fuv2xBmCyH4v7tUeamv_UFFTl7EAVDyfhUDFDZRqfIhMN_MaJ7OUzlXqJdWAVaFwarwCHZS-gO4Y2eVtcZsK7OBSyEYze65fAcScKGDQMonBQFNBtzYDI853GU7oA9KUiVuNdku3WENEWNN6wsdOgoCvG0Kx-bnvbkVx7l1FBR2ciEnYTeJZ11QUjLveRBOZoScw0uriGVfVbMttzx37T8KFsHBVndi2SrCJ2DK9YRY5qc1rRwPMuKYE2oG3eLo5NqB8ump_BLEjad7duMsY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقایان مسئول نترسید!! / با صلابت در ادبیات سیاسی کلید واژه انتقام و خونخواهی استفاده کنید
🔹
بیانیه بدید که این جنگ ادامه پیدا خواهد کرد تا وجود تمام فرماندهانی که دستور ترور رهبری را دادند از دنیا پاکسازی بشه
🔹
ما امام از دست ندادیم که دلار بگیریم!
آمریکا با لگد ما باید از خاورمیانه بیرون برود تا آرمان رهبر شهید محقق شود.
#WillPayThePrice
#تقاص_خواهید_داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/658588" target="_blank">📅 23:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658587">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
سریال استعفای وزرای انگلیسی ادامه دارد
🔹
پس از وزیر دفاع، وزیر نیروهای مسلح انگلیس ال کارنز نیز از سِمت خود استعفا داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/658587" target="_blank">📅 23:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658586">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPWM-sW2lY0zpDNF9BYn6poDMDirEFRd3vN1IfZodk7Jgs-Bu51-Db07GoxP9m4ICWoQejFhUMBhwWktaym-QPGbn3Nxcbort84QoNnOGWPTaaWgRJZW5isAHUfoMVvntScFAxvt8ea08dtHMLoG1AJ7GEzISlxM5QaBJ7p7e0LCPWp-hISmqjaNnSsBhPc18fFPwadjGCMRF3_rJBqn0CER3QntBdnfHx00dG1TZO5u-rOlDz2MooY47zbAah8lvNyOwC7FYEUQ91VZgHwYz90LdGnETXUOdVX2sD2jJ6aDBlfPrt5JoBK2oEc_c1mrvUXcbfV9lT_ELiGrxwbmgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری عجیب از وضعیت دست دونالد ترامپ در جلسه دفتر بیضی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/658586" target="_blank">📅 23:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658584">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
مراسم وداع و تشییع رهبر شهید انقلاب پس از دهه اول محرم برگزار می‌شود    ستاد بزرگداشت عروج رهبر شهید انقلاب:
🔹
زمان و جزئیات منتشرشده درباره مراسم وداع، تشییع و تدفین رهبر شهید انقلاب و شهدای خانواده ایشان در فضای رسانه‌ای معتبر نیست.
🔹
با توجه به ایام…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/658584" target="_blank">📅 23:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658583">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
کانال ۱۲ رژیم: ترامپ و نتانیاهو تلفنی گفتگو کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/658583" target="_blank">📅 23:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658582">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
شبکه الحدث: توافق برای تمدید آتش‌بس به مدت ۶۰ روز، بازگشایی تنگه هرمز و پایان عملیات نظامی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/658582" target="_blank">📅 23:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658581">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
‌
ادعای ترامپ: توافق به زودی امضا می‌شود، شاید در این تعطیلات (شنبه و یکشنبه)
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/658581" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658580">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf783a3f29.mp4?token=Xbf-NwnlPFc6drmnWiiiqMw-WZbyH6eUsfsfvKD2WXURWrADyXK24CV73kjrXoEkZqIkXG7iMBgJoUfpFyIXEdd4dfuUfNlnzhDX9MKOIZKmsOT4e67R0WlEBKmV-FmeJNMtkDcKcTXfSbgR171UyQlmDoxvarWjUixCkVTEin3LopQm5B2rPDuGFHBZy-xGmTQi9ldg95SxRKUNAh6IzOaZ3JzyG6dZcxKqPVpidS5-U4EUXLS-IyynKcOGbM3HxUc19wprln9tbnCpSt_Cu4mqpxVnaF0EcHcYOcSWXRaQbJ7ali9hgLhqqbF_0NTy3Pm_0OlSKcbkykg70wYDlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf783a3f29.mp4?token=Xbf-NwnlPFc6drmnWiiiqMw-WZbyH6eUsfsfvKD2WXURWrADyXK24CV73kjrXoEkZqIkXG7iMBgJoUfpFyIXEdd4dfuUfNlnzhDX9MKOIZKmsOT4e67R0WlEBKmV-FmeJNMtkDcKcTXfSbgR171UyQlmDoxvarWjUixCkVTEin3LopQm5B2rPDuGFHBZy-xGmTQi9ldg95SxRKUNAh6IzOaZ3JzyG6dZcxKqPVpidS5-U4EUXLS-IyynKcOGbM3HxUc19wprln9tbnCpSt_Cu4mqpxVnaF0EcHcYOcSWXRaQbJ7ali9hgLhqqbF_0NTy3Pm_0OlSKcbkykg70wYDlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مزخرفات
ترامپ درباره ایران: ما در برخی شب‌ها ۲۵ کشتی، در برخی شب‌ها ۱۵ کشتی را هدف قرار دادیم. در ۴ یا ۵ شب گذشته، به ترتیب ۲۵، ۲۲، ۲۱، ۲۶، ۱۸ و ۱۴ کشتی را زدیم
🔹
چه کسی دیگر این اعداد را به یاد خواهد داشت؟ هیچ‌کس.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/658580" target="_blank">📅 23:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658579">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2bd57c2ed.mp4?token=SuBwQxTellaqpECNj_nw8MTyBVh36d7aIUNGZwAsEQYKxK91PE9lTdRkNxLbz01E7rRU2TCehC6gj_TWuarUv-Grl-9J7EwhOaNtpzorK90Y6gjlSc3ogdHrYAOlByAvTq_R5_IfYZhE1mxaUAmmkSOHK-tv6_a_wdM4hcpRuJLLmHVgH_nx5q8GnPxSAvhy20d4dyeWT2m9IFZS8ybSPvV7R3iz9aNl2uhxRixbyCc67hKptfGo2oCqiwwSOoRNcAxWl8g4ciRc6lT7vEVucfLJkituxG5O86KJDhx28ZRY-7w2lOuH0ri3_m0OF3IkjEmILTBMggHBBHNc2ZSpGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2bd57c2ed.mp4?token=SuBwQxTellaqpECNj_nw8MTyBVh36d7aIUNGZwAsEQYKxK91PE9lTdRkNxLbz01E7rRU2TCehC6gj_TWuarUv-Grl-9J7EwhOaNtpzorK90Y6gjlSc3ogdHrYAOlByAvTq_R5_IfYZhE1mxaUAmmkSOHK-tv6_a_wdM4hcpRuJLLmHVgH_nx5q8GnPxSAvhy20d4dyeWT2m9IFZS8ybSPvV7R3iz9aNl2uhxRixbyCc67hKptfGo2oCqiwwSOoRNcAxWl8g4ciRc6lT7vEVucfLJkituxG5O86KJDhx28ZRY-7w2lOuH0ri3_m0OF3IkjEmILTBMggHBBHNc2ZSpGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: به‌زودی توافقی (با ایران) امضا خواهد شد و اسناد آن تقریبا نهایی شده‌اند/ انتظار دارم این روند خیلی سریع به سرانجام برسد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/658579" target="_blank">📅 23:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658578">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
منابع شبکه العربیه: طبق توافق، آمریکا تحریم‌ها علیه ایران را کاهش می‌دهد و محاصره را برمی‌دارد
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/658578" target="_blank">📅 23:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658577">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
ادعای ترامپ: تنگه هرمز به محض امضای توافق به صورت رسمی باز خواهد شد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/658577" target="_blank">📅 23:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658576">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
ادعای ترامپ درباره توافق با ایران: همه بسیار خوشحال هستند. کل خاورمیانه خوشحال است. و فراتر از خاورمیانه نیز همین‌طور #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/658576" target="_blank">📅 23:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658575">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ترامپ کودک‌کش: من قادر به حضور در مراسم امضای توافق‌نامه نخواهم بود، اما معاونم جی‌دی ونس در اروپا حضور خواهد داشت #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/658575" target="_blank">📅 23:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658574">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
فوری| ترامپ: توافق بزودی در اروپا امضا می‌شود #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/658574" target="_blank">📅 23:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658573">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvObDIOqkaImIKpXELjoU0_ALr4-8hk30tySFKO_C2dmkcVaqBLXlRsZZZY8bkgYTcrFO6UoWR98dvx5W95tAO9D0mAHmm8Kb1xTcyCtQWGNp1Wfr6Qcx-QodbH2EvWUKaEvheiDIx-EUHr9KB4t-5v6BDaG7-zx0qlCMD8CKi-ux7qNb9eDDoUqNGBhIADiGC9vwVqWH32eGqK0lWzXYNiOiRP3QM3Y3JoJdJ36dQA5nRpr-F2mej-c7AB8lFmo24o6m9WTlsluQjfd21iVHTdAOIDxCnL1OlARMTzZvTOehCY9YWufDjhrie6QQOsWbnQNRCYTUO2v4fr3qyKVbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت معنادار سخنگوی وزارت خارجه
:
از شبیخون حوادث لشکرش در هم شکست
هر که صائب در مقام صلح طبل جنگ زد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/658573" target="_blank">📅 23:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658572">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
فوری| ترامپ: توافق بزودی در اروپا امضا می‌شود
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/658572" target="_blank">📅 23:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658571">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
روایت ترامپ از «پذیرش ایران» در برابر واقعیت میدانی
🔹
همزمان با عقب‌نشینی تاکتیکی آمریکا از اضافه‌بندهای جدید به پیش‌نویس توافق، دونالد ترامپ با افزایش لحن تهدیدآمیز در شبکه‌های اجتماعی، تلاش می‌کند روایت «تسلیم ایران در برابر بمباران» را بسازد؛ روایتی که با واقعیت میدانی مذاکرات فاصله دارد.
🔹
حدود دو هفته پیش متن پیش‌نویس تفاهم‌نامه میان تیم‌های مذاکره‌کننده تقریباً نهایی شده بود و تنها منتظر تأیید نهایی در تهران و واشنگتن بود. اما در خلال این بررسی، ترامپ بار دیگر برخلاف توافق مذاکره‌کنندگان آمریکایی که پیش‌نویس ایران را پذیرفته بودند، خواستار اضافه شدن چند جزئیات جدید شد. در واکنش، ایران اعلام کرد که آن متن جدید را بررسی نمی‌کند و عملاً پاسخ آمریکا را نداد.
🔹
پس از آن، تنش‌های پراکنده در تنگه هرمز و جنوب ایران و همچنین حمله به ضاحیه عملاً پرونده مذاکره را مسکوت گذاشت. اما از روز چهارشنبه، تیم قطری با میانجی‌گری وارد میدان شد و خبر از عقب‌نشینی آمریکا از همان اضافه‌ بندهای جدید داد؛ یعنی بازگشت به همان متن اولیه‌ای که هنوز منتظر تأیید نهایی در ایران بود.
🔹
همزمان با این عقب‌نشینی محسوس آمریکا، ترامپ با راه‌اندازی عملیات رسانه‌ای و ادبیات تهدیدی کوشید القا کند ایران زیر فشار بمباران عقب‌نشینی کرده است. اما واقعیت آن است که تا این لحظه، نه تنها ایران پاسخ نهایی نداده، بلکه این آمریکا بوده که به خواسته قبلی خود بازگشته است. البته بنظر می رسد با توجه به اینکه امریکا متن پیشنهادی ایران را پذیرفته است احتمال بررسی مجدد این متن وجود دارد./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/658571" target="_blank">📅 23:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658570">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APSCKho6Jf3tMgwcsUA5UM2lSFYGcz0_ma2d-aKB4HGtR8a_5MiQS9rw1jRCNo-_2f06e0JcaQ106FXs1X591ct0k2hpjOaplvaTiOfwA4q46lLnPZ0MB91DOxM57Zf9djq8a6db3WLi6Hl6-pN2OiIXhlcXUgG_eR41Mza33ayB0xb65DXNXGV2uJttiAgtPyTcNV7gSQY8_p2uaKmt5S7SmsgZ019ZP80xqX_lEeKcKcXrusgrP1sRHWn2utBqn97k8kNeXMK0SIb--pAqQ-xY7-sGxVjEvrtfQi6d0OWrTlP9hCTsHlSZylISSFlY5RFGf2GBpue9xKQpy-UVLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت روغن طی یکسال به طور تقریبی ۳۰۰ درصد رشد داشته است!
/ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/658570" target="_blank">📅 22:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658569">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYPXKkRvZSXdzMvg8ooPZBL32-sdnwFhURjBRmrvV0zXqfFEIoffcBopvGoQdYuSGPqWfLFMgXvX8DUIRM7oG_zB9pkLQFugsSR4Oan6Up28rfk6Yrt3iwkCKkWkbse5bPcpor2cUhU6ZFXvhKr_Q8VDm95zPDzFcuUcUyDwZvchdRCJ1SlPFuVg9wN62N66H4bzPXN54qaGrdDpk78st-3QuQhM8SJ04mlF_N27WqK4zUJS3rxM8LZtkOYAq85kW2fDfMja7jBCDEP6dXsiJ4g6H6WLCI3uy2YekVsN7-kkhDnvIGYUIGJyHerwov4qamjf7VO27SxHTx1BJTiS5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهدی مهدوی‌کیا، میهمان مراسم افتتاحیه جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/658569" target="_blank">📅 22:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658568">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8484037c82.mp4?token=YCJ7tRQmkXAfB4vOwESjdbZkFyNfyqld4y4rl4IZ_N1wx4wxCpblB54Z4JJHaMLL1_mjEtPKDLYONerRhOrNXVckMVnMDht1Byxsg_hIgk0RrhryqbRd_p1pV_1KKlF4WmnLrWoFnALb7gt1R_whSG30opvXn4TinCzTR7W5a1ePk6THgXj1WYDFO2YxOMeozAd6Pj4cSlCewgnxES9sVIFcn0Q3BRX6Tq-Dopy98QWYFT1_Hx2H6TktN-qcvgU6kSoSS2W66AI6avMuEkPNgF-VRMEw0x0rJ2TSo3wTr8tpX8zpohJSW7HkSV-HkkSGplcmdURahkq7SnVqG_3iyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8484037c82.mp4?token=YCJ7tRQmkXAfB4vOwESjdbZkFyNfyqld4y4rl4IZ_N1wx4wxCpblB54Z4JJHaMLL1_mjEtPKDLYONerRhOrNXVckMVnMDht1Byxsg_hIgk0RrhryqbRd_p1pV_1KKlF4WmnLrWoFnALb7gt1R_whSG30opvXn4TinCzTR7W5a1ePk6THgXj1WYDFO2YxOMeozAd6Pj4cSlCewgnxES9sVIFcn0Q3BRX6Tq-Dopy98QWYFT1_Hx2H6TktN-qcvgU6kSoSS2W66AI6avMuEkPNgF-VRMEw0x0rJ2TSo3wTr8tpX8zpohJSW7HkSV-HkkSGplcmdURahkq7SnVqG_3iyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین گل جام جهانی ۲۰۲۶ به ثمر رسید
🔹
مکزیک ۱ - ۰ آفریقای جنوبی
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/658568" target="_blank">📅 22:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658567">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ec7ef88a.mp4?token=B_ocDs2FeJR6gyHRAZYTL4L_ITsaoTVCBIZ0Ecxr18qSNAt-Igt_25Ql82rYnwMpjevYANY_sHjewl1NuGCTHXMmWwtyjw_ZXIB0fWHVHn0UWR_YSIkaWCDIImaIfFoSi_AlkIWUNXXVUd2hDPMD7j3S7NeYi3P3XaY4NMacpUtmffXdQe8_qM0hP_CcEv7AkrHuPFsIcj8-NZvQylBBKqEcAUuTjl8xt9mJbaUkeotuleiEDg8JmJ_-XELlLnu3L78qG1IhYLEkM0YaQMgEGTI6xLLCr7YYsTWQsdWXvuO0uX_lcv6k8qkA6HMm8r6NemgN-LpTLka2vcjo1rJZpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ec7ef88a.mp4?token=B_ocDs2FeJR6gyHRAZYTL4L_ITsaoTVCBIZ0Ecxr18qSNAt-Igt_25Ql82rYnwMpjevYANY_sHjewl1NuGCTHXMmWwtyjw_ZXIB0fWHVHn0UWR_YSIkaWCDIImaIfFoSi_AlkIWUNXXVUd2hDPMD7j3S7NeYi3P3XaY4NMacpUtmffXdQe8_qM0hP_CcEv7AkrHuPFsIcj8-NZvQylBBKqEcAUuTjl8xt9mJbaUkeotuleiEDg8JmJ_-XELlLnu3L78qG1IhYLEkM0YaQMgEGTI6xLLCr7YYsTWQsdWXvuO0uX_lcv6k8qkA6HMm8r6NemgN-LpTLka2vcjo1rJZpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اقدام جدید در جام جهانی ۲۰۲۶؛ بازیکنان ذخیره هم در مراسم پیش از شروع بازی شرکت می‌کنند و سرود می‌خوانند
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/658567" target="_blank">📅 22:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658566">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cf7c74853.mp4?token=k57gG8nkJVWhdmmbM7mkLBXcLi-rbTrCCX79-FDyWUk1gNTm7JFjEadmOFjXquNDG7QTIJi9VrM37VbHvkO2WL2oH8lexQxWHBHfQi7FhJF82dQT44L0MZ6-Qvp6P8_sw7M3ePqPSfX-7txAkwrgVtmW2gUA1JmudhpvEv7imZwpRDQXZu2NahqG1ivdWAxSpb-PR8EBjVsAVqcWPaob4g_i0eSUWEoawE5gBE1e3RizG1XN2KQcD8Olz3qgZchQrk-ax-I1zvvaRzZr4GNKKIkfT-p4T04SmRLICNjJj-xWobJ48wTGwHN_zD6kBlDMy8s4jDAYQU9YoFLerEX0vFhZrIvhwwqqvYHPRdHNcIXJ_RU5E9j07L-Dg6FHGR1xP0VHF0KofIbocwWMP9Q8tMCjfR3u1dFM5jrJnfz-k_x381dpdoz-NCTpxTluXZ0MVN_LrTGMdrUlVfrS_Udp0yTMOsyos_UR5GbNr94AAyDaELYROGS1lUBTOajkBg4hlyDWS8WbgLon0R7tu0ACRwWxS1_ej2-c6BLw42SKZdR2fDHqQm0JD9fJdeYHDUcUK8MHVnKfNE807CgcPxPBEJHbNPl6HgAq7uH4AWRK_uaDZzYTHt7OhMIhbhnBsXAJig6rAGT5KIQBvNFni44gmS-zRZmGfSNgru6GZSGtCMc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cf7c74853.mp4?token=k57gG8nkJVWhdmmbM7mkLBXcLi-rbTrCCX79-FDyWUk1gNTm7JFjEadmOFjXquNDG7QTIJi9VrM37VbHvkO2WL2oH8lexQxWHBHfQi7FhJF82dQT44L0MZ6-Qvp6P8_sw7M3ePqPSfX-7txAkwrgVtmW2gUA1JmudhpvEv7imZwpRDQXZu2NahqG1ivdWAxSpb-PR8EBjVsAVqcWPaob4g_i0eSUWEoawE5gBE1e3RizG1XN2KQcD8Olz3qgZchQrk-ax-I1zvvaRzZr4GNKKIkfT-p4T04SmRLICNjJj-xWobJ48wTGwHN_zD6kBlDMy8s4jDAYQU9YoFLerEX0vFhZrIvhwwqqvYHPRdHNcIXJ_RU5E9j07L-Dg6FHGR1xP0VHF0KofIbocwWMP9Q8tMCjfR3u1dFM5jrJnfz-k_x381dpdoz-NCTpxTluXZ0MVN_LrTGMdrUlVfrS_Udp0yTMOsyos_UR5GbNr94AAyDaELYROGS1lUBTOajkBg4hlyDWS8WbgLon0R7tu0ACRwWxS1_ej2-c6BLw42SKZdR2fDHqQm0JD9fJdeYHDUcUK8MHVnKfNE807CgcPxPBEJHbNPl6HgAq7uH4AWRK_uaDZzYTHt7OhMIhbhnBsXAJig6rAGT5KIQBvNFni44gmS-zRZmGfSNgru6GZSGtCMc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرگزاری شهر | اهدای گل به خانواده‌هایی که از هتل‌، به خانه‌های خود بازگشتند
🔹
نمایندگان شهرداری تهران با حضور در منازل بازسازی‌شده شهروندان جنگ‌زده که پس از مدتی اسکان در هتل به منازل خود بازگشتند، با اهدای گل از آنها دلجویی کرده و جویای احوال آنها شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/658566" target="_blank">📅 22:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658564">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
خشم پرنده‌های ما این‌بار برای پیروزی در یک رقابت ساده نبود؛ ما به یاد و به نام کودکان معصوم و پاک
#میناب
پرواز کردیم و بردیم
This time, our birds’ rage wasn't just for winning a simple game; we took flight and conquered in memory of the innocent and pure children of
#Minab
.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/658564" target="_blank">📅 22:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658563">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
عصبانیت وزیر جنگ آمریکا از مقاومت ایرانی‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/658563" target="_blank">📅 22:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658562">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: قطر نقشی تعیین کننده در نهایی شدن توافق داشت
ادعای سی‌ان‌ان:
🔹
به گفته یک منبع آگاه، مقامات آمریکایی معتقدند که جلسات این هفته بین مقامات ایرانی و قطری در تهران به حل برخی از نکات مورد اختلاف باقی مانده در توافق با آمریکا کمک کرده است.
🔹
نکات مورد اختلاف شامل جزئیات چگونگی پیشبرد مذاکرات آینده بر سر برنامه هسته‌ای ایران و ترتیب اعطای کمک‌های مالی به ایران بود. به گفته یک منبع آگاه، ایران آخرین پیش‌نویس توافق پیشنهادی با ایالات متحده را از طریق میانجیگران قطری ارائه کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/658562" target="_blank">📅 22:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658561">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
بیکاری ۲ میلیون ایرانی بر اثر جنگ
گلپور، رئیس کانون انجمن‌های صنفی کارگران:
🔹
آمار واقعی بیکاران بسیار بیشتر از ثبت‌نام‌کنندگان بیمه بیکاری است. به گفته او، با وجود ثبت‌نام ۲۹۰ هزار نفر، برآوردها از نابودی بیش از یک میلیون شغل و بیکاری مستقیم و غیرمستقیم حدود ۲ میلیون نفر حکایت دارد. همچنین تا خرداد ۱۴۰۵ فقط برای ۶۶ هزار نفر بیمه بیکاری برقرار شده است./ جریان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/658561" target="_blank">📅 22:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658560">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ua5y8yvNhEYn2XW31vXSkl1BKy_dMwCBRc4VJYFRgbFYe1nypbM_QXHJ5oSsvmYe62KxNXXzO743ORVJVdO1ps5wZlbg_OtB693mCob21bUYOK_NXcbCdVQOXRpPx2wpSV8rdR0tLrmFkisIutaCVdH300_FBaJuCRHSRVefo5E7IR_NgvAX7xs8OZv2VIc6ZC-I97cVs0pcPxjAzFPvn9aSo0dsEStaJlGVdNddJDi6ctice800ogQcHJlPr4I1B1WNCm-F3afIQG1Epyo6cacW3f55HFLpzdU69mk84A_p-9IlhfqM6iBg0x_QSu-2A5rwEu-BsEqz2W2QqHn5JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Danger doesn’t always come from the front; it comes from where you least expect it.
خطر همیشه از روبه‌رو نمی‌آید؛ از جایی می‌آید که هرگز انتظارش را نداری.
#WillPayThePrice
#تقاص_خواهید_داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/658560" target="_blank">📅 22:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658559">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| نَبض تهران |</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e986ed42f.mp4?token=OKl5AsOZtTLDuhkgVXYm_VIyXPzkVBUZGdGFe8tjOo7x9QcEHz29GDWbcVnfmLfgHflMYF4Jg6HvpvNuqt0Giv1DrmAUVZ5NdHXsz5yaXmZ-u-xZh-TtTQ9qI232xiXZRHHyCvPkl33LvOHDVFmO7BnpT9u4wxOfgfTy5ugrovGFtqhaaCrQjzhoABVG4LMpOr9wcIQ4p8NaTpJ4beRBYnBC-mSMQA1rcDsa0x83ECWyNZS9zfi-12tJlU9AjaFkAtsbzmNsNNxXWbLpTb0MDJlQoZPZjkc3_J2aPjnv3Y9qAEUtZMybsAjsz66uxAuzGquFVK2fHpdmNOcv4YTRPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e986ed42f.mp4?token=OKl5AsOZtTLDuhkgVXYm_VIyXPzkVBUZGdGFe8tjOo7x9QcEHz29GDWbcVnfmLfgHflMYF4Jg6HvpvNuqt0Giv1DrmAUVZ5NdHXsz5yaXmZ-u-xZh-TtTQ9qI232xiXZRHHyCvPkl33LvOHDVFmO7BnpT9u4wxOfgfTy5ugrovGFtqhaaCrQjzhoABVG4LMpOr9wcIQ4p8NaTpJ4beRBYnBC-mSMQA1rcDsa0x83ECWyNZS9zfi-12tJlU9AjaFkAtsbzmNsNNxXWbLpTb0MDJlQoZPZjkc3_J2aPjnv3Y9qAEUtZMybsAjsz66uxAuzGquFVK2fHpdmNOcv4YTRPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جام جهانیه
⚽
اونایی که فوتبال دوست دارن منتظر بازی هستن،
اونایی که دوست ندارن، منتظر سوت پایان!!!
⚡️
تا اون موقع هم، کولر روی ۲۵ درجه
«۲۵ درجه؛ قرار همدلی ماست»
#صنعت_برق_عرصه_تلاش_و_خدمت
#برق_خدمتی_مستمر
#شرکت_توزیع_نیروی_برق_استان_تهران
#پویش_۲۵درجه_قرار_همدلی</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/658559" target="_blank">📅 22:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658558">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbf9e93ae7.mp4?token=dsD2JABBvle1rOzUFD5jIZtqpQlzSEwH0aaD08hYlj6OqKjPntLKwDsQs6dZWaiKf1WJXqZzGJVV--DwQcORHCana-RXT48FQdFzmFhOqjBhHAtsebwiUxVJkpgO62A458SpngYcmJjl0wjY2HXy5V0OkR559fwQ7ud3a684CbHwNpJnZ6YMNHMLLcLlQXTRwFnK2KdADBqsTuMRh40gNaGIzficjRqFTL9Lsf07obFAifQo-SUomp3KHiLksz_YuyKCO1ilHDlMSDcm-9FegAyZnU2bzds-_wezFrLU1p_52B8IvcTmaW_DNVH9wuvwLLVnrHfM8aCbcGh9EU-SXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbf9e93ae7.mp4?token=dsD2JABBvle1rOzUFD5jIZtqpQlzSEwH0aaD08hYlj6OqKjPntLKwDsQs6dZWaiKf1WJXqZzGJVV--DwQcORHCana-RXT48FQdFzmFhOqjBhHAtsebwiUxVJkpgO62A458SpngYcmJjl0wjY2HXy5V0OkR559fwQ7ud3a684CbHwNpJnZ6YMNHMLLcLlQXTRwFnK2KdADBqsTuMRh40gNaGIzficjRqFTL9Lsf07obFAifQo-SUomp3KHiLksz_YuyKCO1ilHDlMSDcm-9FegAyZnU2bzds-_wezFrLU1p_52B8IvcTmaW_DNVH9wuvwLLVnrHfM8aCbcGh9EU-SXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی از پرچم ایران در مراسم افتتاحیه جام جهانی ۲۰۲۶ در استادیوم آزتکا
🔹
طرح
طلای
بیمه زندگی
پارسیان
▪️
آینده‌ای طلایی با سود طلایی
▪️
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/658558" target="_blank">📅 22:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658557">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffb76d0e87.mp4?token=CBQyYnwlrPJ44qLhN_hA6raPotCT7LfzIwwgEF3nuTV7TiSFZU1MO3hmlHpoVNLwsMSQx7lEPHEFxm75_xzJIDgvcJax21RTRzwONzLrdoTZc20sPT_itpWS1kvk1tnjEbSyuA9GT_4lVa3J8Ne95WgFu5xEYAaMIs0bSbV_Rz7hAWVYe-INv2vZUu3r60OvT7jdkUlxO8ipY_aDozqpg2OR0wvKT4Xn8b98qjoxvmooWsksOkTHke_OREIPII7FoOdKPeI_qRVzOzglRx_HzVxyprToCadYkBuH_iC0Rpfb4B0iwXME7OMMSl-Z8KMpV6oHP4wmfZxGm-Zwoix5FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffb76d0e87.mp4?token=CBQyYnwlrPJ44qLhN_hA6raPotCT7LfzIwwgEF3nuTV7TiSFZU1MO3hmlHpoVNLwsMSQx7lEPHEFxm75_xzJIDgvcJax21RTRzwONzLrdoTZc20sPT_itpWS1kvk1tnjEbSyuA9GT_4lVa3J8Ne95WgFu5xEYAaMIs0bSbV_Rz7hAWVYe-INv2vZUu3r60OvT7jdkUlxO8ipY_aDozqpg2OR0wvKT4Xn8b98qjoxvmooWsksOkTHke_OREIPII7FoOdKPeI_qRVzOzglRx_HzVxyprToCadYkBuH_iC0Rpfb4B0iwXME7OMMSl-Z8KMpV6oHP4wmfZxGm-Zwoix5FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمای بیرونی و فوق العاده زیبای استادیوم مرسدس بنز توی شهر آتلانتای آمریکا
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/658557" target="_blank">📅 22:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658556">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
تسنیم: تا زمانی که موضوع تفاهم احتمالی، از سوی ایران اعلام نشود، هرگونه اخبار ترامپ در این زمینه را باید به حساب پیامهای قبلی او گذاشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/658556" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658554">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
فارس: ایران هنوز هیچ متنی را برای توافق تایید نکرده است
🔹
هیچ متنی برای یادداشت تفاهم اولیه با آمریکا تایید نشده است؛ این را یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایران  گفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/658554" target="_blank">📅 22:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658550">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eheEAyXKWl3_lD35AyGzIrtE6VGpLo64OtgFCcobla7XhDe0NxQK8xb7OX2UBAoRcoDWlJY_AnyWMjR6KBnlKo8UwDZQCfuyutr-b5pFa4Vsy2N0__RjOiCXwH0xyQSK9DAbk0_gaol93VN2GOWhNcJCAykuQ02LtKxinkkbgGFO3oUB9LK9J_M8UA4EqPoGz_gG67A1vPXyk7OmvVdpB3P8RfyvEAWZaeZwWCAPvveVgeVMANyKWcaITXiltX-2_FddEH7dMMILJFK_qruQEmV2igIeLa4WYh2RvOX7QZVy9Bfwgdr0R9CjkdDAqhSRldHbswk4nkf0FML2WzOUZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pf_1KECv4MufljAN92TJlUKie6vuKwf8krjYlkTxiDJTqTfG-2WG-M59CUbkTWmelGsfw-ETHfhHIePHg32og-XEsrCpL69Cu8Mmd-IbZFZy9eVhaoNYq3vxvx_7SYFwtkMzGGY9zoBp4aGgGWbGqF1anE6avKh5DM3A5LYF3Xh_PLO-_UFUwe-FVxOXmDFrcrgGW9u0zHpEiNm0fNezgTOunR2R86i5h8KNUvjSlpjfsoq1uu_Jzy68ZlsXzhKX5VJAKfBi7ZypSMKVg3mHoS8eoqCaycn8uZ4HR0MLQhmAbv31BM6pnkYxUsDhiLW4rsGQ9omAtHMKSVE24HqBQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Imeo1Gp4jt2XtqzukdHg4pDyufsV1kTGuwz-TlLUf-YureA9yEzCaBqlwEUoiG7eEGU-YK0d_cUCTVhV3Rxr_46S3BSkv6xy_p8a4LAxXXrFU98N1GXTg7fWKetFl2qAdMjOzePBFUxjKp3mgE4dgWa7WW4lKTPjgrtt0T_ZH8livrkYckyjt_K7ESr2P8KpTjXpLrZhgC0xGlwqpbGuPTrHaTYGbazGz69Jgy96ImXd9NiBbZLaTSETcjST_RqzfmgREZGnWXISVzkZOhPKdwJ_oTslP1ZHdUfMDeKXLcv1HC65SczRwXN8Fa7VXLzL2aA84POwDPARfMgyaRDa1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BTsEm511po6mCc3GRRZHKoT0FCv9H_pAwxDCWuB_WpUoXdVnNsiDUR0OWnRjtHX0Agsc7qA0sRhbWr1PXHLxQVOsERKcMSvh5CubbLr7LfZGRMcjvlKjQXoBhKx2IfGglqrIqJ-dofgNUyH6jnhixjlH5Q3B1aqxuyykc9DVPI-HiIVgfc4Hr1E5--5_UtanX6FIqRDkIqOUYV5jgg16pclW4elJd1iHLjdOrPln0g4Q0ym8XrtJTLH3EOco_NS1T7IhTs0IMH0s5rkdyNy_UztGDjJl4b2Z5FhCcIlh0o10ui8koROUG3rfP143dx2Qesy_ug-sos_Iu9X7UPNaAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری دیگر از مراسم افتتاحیه جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/658550" target="_blank">📅 21:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658549">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23fb166215.mp4?token=NVnhenlaeXEZBFyyjzz9EKl_N28f6hTJJkdBLaV5VBf1SSXz1t-M-ooEcOgRp7qjibUKdQe91Mi3hbIvcZXLGV9FWSiApBWL-MezilthJQyhN_-VoPjDIl7SbX1sGVMjYidBopkLvs5Kwk0gIB5dXkyouV6M7_F9ETE2uHZNfN9sDMWvf6dEfOwrF1TwZ6mLZzFh5sMMT-WsFnjVZyfdRbvWxKeKxgLnWPWBdxo3YKgPpb1ouqg5VDd5wTg8YJLDY5hdroW6JjYPD6stwZ7b3YdoCO-TSSYvq1I4m0_oLsWaAOPVd2Je5ngJgtBSfvi50uHj9qktF5F-k17UCN-EiS0YyZIYyRfph8gj1iEjoi3CiU48pgjCFPAEuc_Rf4IMWIDvfKwLVEiexkSAAn1JM_C1jf-bdYiXKf48GXQ6kwsPZnpsinphdkC_iiA4RmwKLsG0rwy8ZsY9-09spwnCUeUl66bncgiLCF31shX936wKfUxp4Ba43qHxomNbexnLxARGDw2dpYg9MK8taW31T2kJPJtJQdoCdEnPunTEHAbJPHoVXyVz4Tnb1VvfqAdL3TfOZQ9kU3PaX9Po0aXi1W_hls6XWpzEddhrMsJmeUheP82AENNFR80zc3-F8eRxnXLRfL1m1Qx4MUcy5BQEiAEc3diZU9ZuQRzZR2y81Hk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23fb166215.mp4?token=NVnhenlaeXEZBFyyjzz9EKl_N28f6hTJJkdBLaV5VBf1SSXz1t-M-ooEcOgRp7qjibUKdQe91Mi3hbIvcZXLGV9FWSiApBWL-MezilthJQyhN_-VoPjDIl7SbX1sGVMjYidBopkLvs5Kwk0gIB5dXkyouV6M7_F9ETE2uHZNfN9sDMWvf6dEfOwrF1TwZ6mLZzFh5sMMT-WsFnjVZyfdRbvWxKeKxgLnWPWBdxo3YKgPpb1ouqg5VDd5wTg8YJLDY5hdroW6JjYPD6stwZ7b3YdoCO-TSSYvq1I4m0_oLsWaAOPVd2Je5ngJgtBSfvi50uHj9qktF5F-k17UCN-EiS0YyZIYyRfph8gj1iEjoi3CiU48pgjCFPAEuc_Rf4IMWIDvfKwLVEiexkSAAn1JM_C1jf-bdYiXKf48GXQ6kwsPZnpsinphdkC_iiA4RmwKLsG0rwy8ZsY9-09spwnCUeUl66bncgiLCF31shX936wKfUxp4Ba43qHxomNbexnLxARGDw2dpYg9MK8taW31T2kJPJtJQdoCdEnPunTEHAbJPHoVXyVz4Tnb1VvfqAdL3TfOZQ9kU3PaX9Po0aXi1W_hls6XWpzEddhrMsJmeUheP82AENNFR80zc3-F8eRxnXLRfL1m1Qx4MUcy5BQEiAEc3diZU9ZuQRzZR2y81Hk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
⁨ ⁨ سوت آغاز جام جهانی به صدادراومد
⚽️
آماده‌اید برای روزهایی پر از هیجان، رقابت
وشگفتی؟
🎁
این بار هیجان فقط به مستطیل سبز محدودنمیشه
💫
بانک شهر با برنامه‌های ویژه، جوایز جذاب واتفاقات متفاوت، قراره حال‌وهوای جام جهانی را برای شما هیجان‌انگیزتر از همیشه بکنه!
🔴
همراه ماباشید تازه شروع بازیه…</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/658549" target="_blank">📅 21:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658547">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
درک مرگ اطرافیان از جمله همسرم و .....
🔹
00:07:20 رازهای مگویی که از گفتنش منع شده بودم
🔹
00:18:40 لحظه‌ای که متوجه مردنم شدم
🔹
00:27:30 نشان‌هایی از حضور روح من در کنار خانواده
🔹
00:33:30 واگذاری مغازه و امتناع از فروشندگی بعد از تجربه نزدیک به مرگ
🔹
00:39:30 رؤیت مرگ همسرم در برزخ و به وقوع پیوستن آن در این دنیا
🔹
00:59:20 رسیدن به پوچی در پی افکار علت خلق شدنم
🔹
قسمت دوازدهم (صدای سخن عشق)، فصل چهارم
🔹
#تجربه‌گر
: مسعود نبی چنانی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/658547" target="_blank">📅 21:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658546">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
عراقچی شنبه راهی پاکستان می‌شود
ادعای الحدث:
♦️
وزیر امور خارجه ایران احتمالاً روز شنبه به پاکستان سفر خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/658546" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658545">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قهرمان جام‌جهانی ۲۰۲۶ معرفی شد!
🔹
یک اقتصاددان مطرح آلمانی که قهرمان سه دوره گذشته جام‌جهانی را بر اساس مدلی اقتصادی درست پیش‌بینی کرده بود، قهرمان این دوره را هم معرفی کرد.
🔹
بر چه اساسی و با چه مدلی؟ در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/658545" target="_blank">📅 21:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658544">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ادعای نیویورک پست: ایران پیش‌نویس یک توافقنامه را از طریق میانجی‌های قطری به ایالات متحده ارائه کرده است
🔹
منابع می‌گویند این متن نهایی‌سازی و برای بررسی به واشنگتن ارسال شده است.
🔹
یک منبع آمریکایی دریافت این پیش‌نویس را تأیید کرده است، هرچند جزئیاتی فاش…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/658544" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
