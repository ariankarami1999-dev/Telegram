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
<img src="https://cdn4.telesco.pe/file/SZnCslrkV6i9soFGPeM_8sbSxNra2Htmj5kI6EvBRv2IW8HArmpNQZKmVGEfahrdYdozQl9SH1AnSe6go6i4jYHHWAtd2d6-fLKbKIQnDSrhQdHO-snv39-M8E8J5P7jBkzFHTONy1BntRVd0Pc7tNHiUkPeP2OvxJ3n4azpqp7JTNcsRx1kOBzyGY336l4hILd1D9s4wVRMmb9-b8Ku1CDb3sllvKgUP3b5sPAXxXwPtjnDHXnrn3sLFwIXOwefPB3UZhEjU2avlosnOYAmWIvkdXOHX74KkqYoEh2kXNbS00YEBP9Ifo0ELIHhF0_Aym4KCIYFrEfsP87VdMZJlA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 136K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 21:10:54</div>
<hr>

<div class="tg-post" id="msg-65084">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=DoQUlfhwXWfY2bQQFAhKytua0z5X5hGLS-PhQ3_R-ZAFc4bKag2gn-qqrV2XpdkzhziVuSse22CtTLIjUZyX-MvExpoL3ckV8ACGyjamPbu2DK2Y4MOsPVgKirsNRPAuZeyuJenas_qH2t1M5LTixlDqBsqDqeud1_UqY2R3PTGgzEf5hSad5L4ordsnYW_vJka1WXRWSvbRUvtD85Q2YSF9OJvYs2VrLqUHRqnPuSrn747UyhDcpPREI0mq8JgTf6QN1XQpVe4Vh2sCUpXNHMGNQ6o8edO0j9waFja3Jvn30BQNOEOd5eWLY95B2SyAtlEEC56d2p9CHai39eRp4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=DoQUlfhwXWfY2bQQFAhKytua0z5X5hGLS-PhQ3_R-ZAFc4bKag2gn-qqrV2XpdkzhziVuSse22CtTLIjUZyX-MvExpoL3ckV8ACGyjamPbu2DK2Y4MOsPVgKirsNRPAuZeyuJenas_qH2t1M5LTixlDqBsqDqeud1_UqY2R3PTGgzEf5hSad5L4ordsnYW_vJka1WXRWSvbRUvtD85Q2YSF9OJvYs2VrLqUHRqnPuSrn747UyhDcpPREI0mq8JgTf6QN1XQpVe4Vh2sCUpXNHMGNQ6o8edO0j9waFja3Jvn30BQNOEOd5eWLY95B2SyAtlEEC56d2p9CHai39eRp4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کم‌کم تمامی vpn های رایگان دارند وصل می‌شن  @News_Hut</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/news_hut/65084" target="_blank">📅 17:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65083">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFudo.</strong></div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/65083" target="_blank">📅 17:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65082">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کم‌کم تمامی vpn های رایگان دارند وصل می‌شن
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/65082" target="_blank">📅 17:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65081">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMKPX</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2xKq8LdWJD6VfiZC8bDP5ICKi1ltlsARYXFt9l7jEy3UyjLrWIYta_wrFoCeCNha2OkZndqEsmlf6piSP1aAGfFw5gJTBba9dzSxNi-R17If7Ht9l3odORe0Pbu_MVM19iHGxungfEyYOOiOFrZvdiQ4_Otb7ewgyCurx76tl2aE7aIhFRQc-dxkU-tCxee70BjtFhjthffKIPwnTVRKjcfHyRA0K_bSvKWBrq9zjouEn89VLvXW_nj6EYRgFyavXJ1NZf1Bctf9aFq-vobOQAdBdlEE479jNmAfngoFpRfS9TVauzNutOrGuLwQ6HOIFQ160VntWwlWyFoVSxFjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/65081" target="_blank">📅 17:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65080">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMmdi</strong></div>
<div class="tg-text">درود
کسانی که نت مودم دارن میتونن با jump jump به اینترنت وصل بشن
ما هم بعد از سه ماه قطعی به جهان برگشیتم
بر باعث و بانیش لعنت
به امید آزادی ایران جونمون
❤️</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/65080" target="_blank">📅 17:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65079">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.  @News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/65079" target="_blank">📅 17:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65078">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJA1D0lntFVufhXIbBezFlX8_vWVcNkH_go4NXTDTXF3HyRYDB51z60p0vOAejV_UAmab2uLX8g8p_MKyw8aBxh9ba6AzsgJtnZu7e5f4pa5PfsGXk2oGv1n2qvfitIOzg4A-TuxmWExNtIZLsVb-twdsbZYcUo4cPqNVf4emvuHXQbrhzus1NdKUStrRINf6717fnBjySoA0HEKcEIn_JHNLSYvkUXNs5L834yk1uuCu7V2rIL8DwgZC6rI520qwIZYWjrgeXfDvYrf4s1kzwS8KiYAosWQWehp-HDfi9TuCoz8BMnkygb3WpgEgXdATHhiEHcfCKGn83PtqDVTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/65078" target="_blank">📅 17:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65077">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
خبرگزاری انتخاب: ۴ شاکی حقیقی رفتن شکایت کردن و با دستور لغو مصوبه بازگشایی نت باعث توقف اتصال مردم به اینترنت بین‌الملل شدن.   این چهار حروم‌لقمه عبارتند از: رضا تقی پور، نماینده مجلس کامیار ثقفی، هیات علمی دانشگاه شهد و عضو شورای عالی فضای مجازی رسول جلیلی،…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/65077" target="_blank">📅 14:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65076">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oD3hElcU9sdQrwQdnI78NY_8ekQ6AogqtpNEK7fkZq6g6yNbC68sXr657yJ9OWrmhVfJi6hT4ejxLhud2Ouvecn2CJUQzPnyTwfumzdG1FjqemXOqnHOgokdBI8z-2hAcoLuPPWhYGK1JOCdHqEuixjFYJ2Q7WyYgz2lvpGp41CWtKf1rLCrMuatKCAq-yofQLewee7syc87Crn1S1SAVgNcee9rf_85C26sjOa7gVK0G2lOXA7CwE3ME5CmnN-x6agQ4vgjzTu0VIihEO4jxHjDVdnx6oqo_NsNb3NOzJHJjqh52Dh3OYWML92BH805TDbn8ukX7D5YRI72ADXJUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری انتخاب: ۴ شاکی حقیقی رفتن شکایت کردن و با دستور لغو مصوبه بازگشایی نت باعث توقف اتصال مردم به اینترنت بین‌الملل شدن.
این چهار حروم‌لقمه عبارتند از:
رضا تقی پور، نماینده مجلس
کامیار ثقفی، هیات علمی دانشگاه شهد و عضو شورای عالی فضای مجازی
رسول جلیلی، برادر سعید جلیلی و عضو شورای عالی فضای مجازی
محمد حسن انتظاری، عضو شورای عالی فضای مجازی
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/65076" target="_blank">📅 14:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65075">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سخنگو دولت: بازگشایی اینترنت توسط پزشکیان به وزارت ارتباطات ابلاغ شد و امیدواریم تو روزهای آینده باز بشه  @News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/65075" target="_blank">📅 13:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65074">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇺🇸
ترامپ:  اورانیوم غنی‌شده (گرد هسته‌ای!) یا فوراً به ایالات متحده تحویل داده می‌شود تا به کشور بازگردانده شده و نابود شود. یا ترجیحا، با همکاری و هماهنگی با جمهوری اسلامی ایران، در همان مکان یا در مکان قابل قبول دیگری، با حضور کمیسیون انرژی اتمی یا معادل…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/65074" target="_blank">📅 12:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65073">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee692e46c.mp4?token=uAJOITESrnD8Y5AjFx44-z8opYvzcBmiBl9K3RIJ_pIlZJfq1q3UA9VXzvMwtq6kxJPSvmGgYikRdLqrVNBxhqlTjpexuyXf1llrsrLgXQV1XL4tvDjOaZPyUxXiudXdHVkQS_0wkRSp-IWPIPi86fCwBaloGqe7wR1sXsc3zsi3me1yiTdp_24d3_3h8AnP9ngw-1qIpRClakJfZeuHZDc8HxwrPeWaEqJW5j8MM_2ZOqxtO-M4l4R-KUZWRhMH_d69U5NKKcEak7S7f1opIBSrsec0hLdylZ7VDibXwfHx4jS0W3vzb2vLuuC1K5CTweS6u5a1RZww_N46Yfb5IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee692e46c.mp4?token=uAJOITESrnD8Y5AjFx44-z8opYvzcBmiBl9K3RIJ_pIlZJfq1q3UA9VXzvMwtq6kxJPSvmGgYikRdLqrVNBxhqlTjpexuyXf1llrsrLgXQV1XL4tvDjOaZPyUxXiudXdHVkQS_0wkRSp-IWPIPi86fCwBaloGqe7wR1sXsc3zsi3me1yiTdp_24d3_3h8AnP9ngw-1qIpRClakJfZeuHZDc8HxwrPeWaEqJW5j8MM_2ZOqxtO-M4l4R-KUZWRhMH_d69U5NKKcEak7S7f1opIBSrsec0hLdylZ7VDibXwfHx4jS0W3vzb2vLuuC1K5CTweS6u5a1RZww_N46Yfb5IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگو دولت: بازگشایی اینترنت توسط پزشکیان به وزارت ارتباطات ابلاغ شد و امیدواریم تو روزهای آینده باز بشه
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/65073" target="_blank">📅 11:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65072">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رهبر سوم جمهوری اسلامی: سه چارتا جنگ کردیم همه دشمنان‌مون رو تا ناموس شکست دادیم جوری که ویران و حیران شدن.  @News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/65072" target="_blank">📅 11:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65071">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‼️
رهبر سوم جمهوری اسلامی: پدرم، علی خامنه‌ای خلف پیامبر بود و بعثت الهی یافته بود(از طرف خدا مبعوث شده)  @News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/65071" target="_blank">📅 11:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65070">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فوووری برای اولین بار رهبر معظم جمهوری اسلامی با سوییچ از فونت لوتوس۱۲ به فونت تیتر ۱۸ در جمع حامیان‌ خودش حضور پیدا کرد  @News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/65070" target="_blank">📅 11:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65069">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GG9_a3v0o1po2xoSZOrol-7H4PZkQf5Kn6i2zPzgTzoKOLrZJgDk1GnbxZNX3yakpedkQvm7nWAAlFhfHSwVgdkXaOtZsE4nHiOyoC0mjlLGk47wt35g4EByJ3V7sHLs51_g6KhxTp7ewupICYAUqmr8yNqWfeKeK4Woo8KkfZi4mhMYqDOyYouO-ly3Pq7cflsbLX_cgo7E_23xptaZOJazftrP-iiyj6fSXkb5D5N8vR0XF7_iHO81Ql0KW6XeLUKKuOWODajV43Ihm6Ew4zadjO-fPlf6dxE8EYCjwssMF0Kt3jIWUwFXlso1fdohialPcprY8Us5KIgV2HTCWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوووری برای اولین بار رهبر معظم جمهوری اسلامی با سوییچ از فونت لوتوس۱۲ به فونت تیتر ۱۸ در جمع حامیان‌ خودش حضور پیدا کرد
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/65069" target="_blank">📅 10:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65068">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g09uvEff3DnJ5xqjmLHdXzI7MFCbB1Es5I95zSVjnHeFP96ioe75tSV7JAbvI7YObIVmr9Zv8tXXA4BB0lPz1o7dfVnDsrLx_lrxd3SZtexxApzv-fvGfktIWoOLczNusV56tgjcXAOTwt_YSMMBEa_pJCH3HmnErsBD42-REU77Kn4boE6SzKwyK309ADA9uqD8OrzQokd70WtsauPDynvdwyMm7OZl_1wq8C4ejQ9HT_5GneXEQQ8CTGXU0ng0k3d-umksI2FIUD7tm6eVK_TcNTMSLPaKxn0Rung4C_avjouJ9BJ3qyB0OOkGYlVAGMyzcPWOUhTVsBEoIUq7-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:  اورانیوم غنی‌شده (گرد هسته‌ای!) یا فوراً به ایالات متحده تحویل داده می‌شود تا به کشور بازگردانده شده و نابود شود. یا ترجیحا، با همکاری و هماهنگی با جمهوری اسلامی ایران، در همان مکان یا در مکان قابل قبول دیگری، با حضور کمیسیون انرژی اتمی یا معادل…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/65068" target="_blank">📅 08:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65067">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ljwec92zEh7TPGPDxj-XU-Gra1Xf5WV2wOBeBZ_c0voQHWC4uE-J9PO34KSnfbw7VKU-SGIOagKEfnWPMULxuXM7jBA7TcTPK4R5AX6RTDEWUen_Fa5HD6VYBAox4kbR4yowH8kBWC1smFzLO1gHxN71QzcA942Ln_C8AXZKzxCtIm1dx5uU_V3qAj7msUgKLWJAg9qEsSJUoauwtPdaxshAa7pFQasMPsV4keJX1rwLEA3ogj2eOHoW_F2XiMMIXUZBq4Ngn-M7zbMGDvmqhxjc8b6mgPOtOSp2gMXrjuinEDNnfJB1lgJa7Gp4ToZogQ9EN_kbOvb3uILBoGH-cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شنیده شدن ۴ انفجار در بندرعباس و شهرهای جنوبی سیریک و جاسک  @News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/65067" target="_blank">📅 01:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65066">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">صابرین‌نیوز: امریکا دو قایق تندرو سپاه رو با جنگنده زده و ۴ نفر هم کشته شدن</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65066" target="_blank">📅 01:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65065">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k__pVDvQp9o7iuJ9t9Yk1L_IxpDTnDCD6WxwoNuNkAFD3XtteiuZQi221dnaVWw4oD-7pSN7kTNRRFY2Smt10U7n1juTBArObyGP3pMHXefJUIChdhP4xmqTK_tu91f7RQmnAY_ETVQnGz6v-mpbrLqTkBc0ciLUAq6N55ZmLnFhz8xGjzINzL5dGlxtfGQrWkpB2NqbTduMdyc0b3HowS-lJeZqUxeEQ9Ti2ab6SKUym0BpMEd2xnRzqxIGHhR-6ZIUaNqH0NO90ex7JVpuB8-cKfK_kzlqb6A9nWqqYgCivB1U7KD-0bPi7NXhqFDG4OrQtrFGKQTltpbckTKhOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
اورانیوم غنی‌شده (گرد هسته‌ای!) یا فوراً به ایالات متحده تحویل داده می‌شود تا به کشور بازگردانده شده و نابود شود.
یا ترجیحا، با همکاری و هماهنگی با جمهوری اسلامی ایران، در همان مکان یا در مکان قابل قبول دیگری، با حضور کمیسیون انرژی اتمی یا معادل آن، این فرآیند و رویداد نابود شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65065" target="_blank">📅 01:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65064">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
شنیده شدن ۴ انفجار در بندرعباس و شهرهای جنوبی سیریک و جاسک  @News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65064" target="_blank">📅 01:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65063">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHAtyPSq7EGr_mMR7BUSR83TT5FShXr-mf_jSrVSZTPPGxEfY7ozgIdevt-ky0o43_KRqJly5EcSFWj5LSZIemjy_QqDWxITZvsHGFmMJQs61laJEu2nYQiSBNop4teOYPUN-nht7bsuFyOoQ3p2PLTliZFZSzGfESpj0B1RlERGPBfuM22FBWvdg9sahin_ZGHid7etuEKXc0olR_M1kfmpgIKcDFmMKyAMW9l5Px_KbRaZs754K4AsK3Ki64J5xNXb6GpNGDT3M5VX6mGdIhFzn3FUG7zbKqTn7vYD3CaZOQTqHiOz5eq6IzrCmEiXVxDGpE4qndesUA6rIOw8Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری تایید نشده مربوط به انفجار لحظاتی پیش در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65063" target="_blank">📅 00:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65062">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
شنیده شدن ۴ انفجار در بندرعباس و شهرهای جنوبی سیریک و جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65062" target="_blank">📅 00:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65061">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
📰
آمیت سگال، خبرنگار شبکه 12 اسرائیل:  ایران در حال حاضر فقط حاضر شده به توسعه سلاح‌های هسته‌ای رو متوقف کنه، در حالی که ایالات متحده چندین گزینه برای ذخایر اورانیوم غنی‌شده ایران پیشنهاد می‌دهد، از جمله فروش آن به ایالات متحده، انتقال آن به یک کشور ثالث یا…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/65061" target="_blank">📅 21:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65060">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">به صورت قانونی، ما یه "شورای عالی امنیت ملی" داریم که به "شورای عالی فضای مجازی" دستور میده که به بقیه اپراتورها بگه که اینترنت رو ببندن. به صورت غیرقانونی هم سپاه رو داریم که زنگ میزنه میگه اینترنت رو ببندن. زورش میرسه، میکنه! حالا دولت رفته یه "ستاد راهبری…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65060" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65059">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
ترامپ: من به صورت الزامی از کشورهای خاورمیانه درخواست کردم که پیمان ابراهیم را سریعا اما کنند تا «جمهوری اسلامی ایران» را در ازای بخشی از توافق پیمان ابراهیم داشته باشند  @News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65059" target="_blank">📅 19:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65058">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
ترامپ: توافق با جمهوری اسلامی ایران!! به خوبی درحال پیشرفته این یا توافقی بزرگ برای همه هست یا بازگشت به جنگ بسیار بزرگتر.  @News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/65058" target="_blank">📅 19:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65057">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🇺🇸
تروث طولانی و مفصل ترامپ درباره توافق با ج‌ا و پیمان ابراهیم:  مذاکرات با جمهوری اسلامی ایران به خوبی در حال پیشرفت است! این موضوع تنها یک توافق بزرگ برای همه خواهد بود یا اصلا توافقی صورت نخواهد گرفت؛ بازگشت به میدان نبرد و شلیک، اما بزرگتر از قبل و هیچکس…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65057" target="_blank">📅 19:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65056">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‼️
فارس: همتی، رئیس بانک مرکزی برای بررسی و گفت‌وگو در مورد آزادسازی ۱۲ میلیارد دلار پول بلوکه شده تو قطر به دوحه سفر کرد @News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/65056" target="_blank">📅 19:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65055">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ywpp0_7kKWdGTi9Fh3TmTeaHXSuagSoj2SvmUkQSpSd0XawEQcBs4kl1A6c0I2m2pDlQX-LWUffO18v7xzInzrLw7VV8744VN7ud-PF5_H62bYw1WUzbhGS-qpcHgkY8iuf53GHc_-UCM8ECeH-LXnE2TxtoSxjWQa4Y-FSg7dnawFWT21zgMdL25Jh_MH62bu82GqIKVG1fXO-rac9Ce4ysE2SLcIZcrodLwsKYURJ1EkwGlRwkYVc5U-2uHfohU2pOTg-Npyt1SGPCSkYgqePV6DkyUt-FPj8TzTDg_xTOyr-AeJJxU8_Gcf897eHnU36s2yi7R4dLpDErq0M_EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی گفته یا اموال بلوکه شده تو قطر رو آزاد کنید یا حتی یک گام هم در راستای توافق بر نمی‌داریم  در واقع الان دست بالا با جمهوری اسلامیه نه ترامپ! اینطوریه که می‌گن می‌خوای حمله کنی؟ خب حمله کن ۴۰ روز کردی مگه ما چیزیمون شد؟! #hjAly  @News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65055" target="_blank">📅 18:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65054">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">جمهوری اسلامی گفته یا اموال بلوکه شده تو قطر رو آزاد کنید یا حتی یک گام هم در راستای توافق بر نمی‌داریم
در واقع الان دست بالا با جمهوری اسلامیه نه ترامپ! اینطوریه که می‌گن می‌خوای حمله کنی؟ خب حمله کن ۴۰ روز کردی مگه ما چیزیمون شد؟!
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/65054" target="_blank">📅 17:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65053">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">چه افتخاری هم می‌کنند حیوون های حرومزاده...  سه ماهه حق طبیعی مردم رو ازشون گرفتین و الان از بازگردوندش، دستاور می‌سازین؟ باید رید به سر تا پای دولت حقیر پزشکیان و امثالهم #hjAly</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/65053" target="_blank">📅 17:57 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65052">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‼️
فارس: همتی، رئیس بانک مرکزی برای بررسی و گفت‌وگو در مورد آزادسازی ۱۲ میلیارد دلار پول بلوکه شده تو قطر به دوحه سفر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/65052" target="_blank">📅 15:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65051">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خبرگزاری فارس: در جلسه ستاد ویژه ساماندهی فضای مجازی که با ریاست عارف برگزار شد بازگشایی اینترنت بین‌الملل با ۹ رای موافق و ۳ رای مخالف مصوب شد.  @News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/65051" target="_blank">📅 14:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65050">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxOKB4jjJ_Hiem-mAFWjbVbk0mOpTLtQetU2G1DZc1oXloTJ4Hp9YVyxB0uQ722fwpOtGse5YhGxMTr05zziiFyl3Tsg1tPQjx-Ev-8ppCxiH6axtTz99vF23Mbtu3s1Feye8wXJoe9JFeN3OFK4hdlX1qtu22IbXpRgxyBIN1uzfWpryWPyBIC0PPN7Ecz9e_PHxwhKIxTofv6iXKelmF_MGYK1e15WHk-0GeHDWtARPNYRKI9I4AyB1ZxL39WcrDTfg14JJ1H5moHkeZMAoceclxU8bV00GOfzoavlhce4K3uuk_n1SbouYKlyJZnLX6dRLMnMXr9KV1wmtiIivA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: در جلسه ستاد ویژه ساماندهی فضای مجازی که با ریاست عارف برگزار شد بازگشایی اینترنت بین‌الملل با ۹ رای موافق و ۳ رای مخالف مصوب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/65050" target="_blank">📅 14:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65049">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df45acb25e.mp4?token=RvM1r39Q55pAEfXmMrQ0asMVYMvNmS0R13a0flVpwtVEMjy_znAPfsmY2IEZsoHYkafX3Q9k7H9YzPx1w-YYa076kohbNJFMgAbHFXlAW4wFF7viVL7GbCJKTp9On-HMOXYty5Bi-hlYR11fe-0FEDkazxOwve3F9oLTAFFrCRdoRH9gbH0nBUNCQ6kVlJyx6iP2X9-8JdsL8VU7_wolC8GH7kqcLypzSAPqfP1bDb2rEeL9cWYQa0M7HhYkaJZDi51zpFHJhKYyNV6S3XXUCJP0PUgn5R-7JgQ9zcQVM4Ta5-hM53u7pkrC_LXVQ_L9YRKlli504T2uKIhUhRLzMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df45acb25e.mp4?token=RvM1r39Q55pAEfXmMrQ0asMVYMvNmS0R13a0flVpwtVEMjy_znAPfsmY2IEZsoHYkafX3Q9k7H9YzPx1w-YYa076kohbNJFMgAbHFXlAW4wFF7viVL7GbCJKTp9On-HMOXYty5Bi-hlYR11fe-0FEDkazxOwve3F9oLTAFFrCRdoRH9gbH0nBUNCQ6kVlJyx6iP2X9-8JdsL8VU7_wolC8GH7kqcLypzSAPqfP1bDb2rEeL9cWYQa0M7HhYkaJZDi51zpFHJhKYyNV6S3XXUCJP0PUgn5R-7JgQ9zcQVM4Ta5-hM53u7pkrC_LXVQ_L9YRKlli504T2uKIhUhRLzMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمد نگینی‌پور، مستندساز حکومتی مستندی ۴ دقیقه‌ای از حضورش تو پزشکی قانونی کهریزک منتشر کرده از اعتراضات ۱۸ و ۱۹ دیماه‌،
تو خود مستند حکومتی که منتشر شده تعداد بالای کشته‌شده‌ها و کانتینتر های حمل جسد دیده میشه که جنایت خودشون رو به کار دشمن ربط میدن و ابعاد بزرگ این جنایت مشخصه!!
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/65049" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65048">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2rayYar</strong></div>
<div class="tg-text">🔐
سرور اختصاصی با پینگ فوق‌العاده پایین
مناسب گیم، ترید، استریم و استفاده حرفه‌ای
✅
سرعت و کیفیت عالی
✅
آی‌پی ترکیه واقعی
✅
پایداری بالا و بدون قطعی
✅
مناسب استفاده 24/7
✅
بدون محدودیت زمان و بدون ضریب
💰
قیمت تک: هر گیگ 150 هزار تومان
🤝
قیمت همکاری: هر گیگ فقط 120 هزار تومان
با ضمانت عودت وجه در صورت قطعی
🙏
برای تست و ثبت سفارش پیام بدید و از طریق ربات هم میتونید خرید هاتونو انجام بدید
✉️
:
@V2rayYar_bot
@V2rayyar_sup</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/65048" target="_blank">📅 13:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65047">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d1b11fd8.mp4?token=fl_xLwOH_nLSf9Hs0RYaAAwllG6SUd_RFngr8ERDJG6m0NrJzozGrhRXqV_QvpiUpVTUGhsCrQzRATO1tN833xwbAqP0LHDgl1A8VoYN1RtB0aUcLH1nBBBvsH51hxG-SpNJ7bI97N4CPLgux230N20Zel4VNYo4PNBIFhsdIgImwCIxjJf_44baaktOV2IN6NfXwzWLwFL8p46ZPQJkVYZioeK2_aBfaOmZX0QmmgQnRfT-72a-F5gYQKk6uLS1SAnxiHxmILO6GKhtbqKbqK0zAv6ePxIQSbsHfbn4wCE9XsymcRBivG0Vk-9_UZXDz3VuJjivXLsMmGBXpPCWxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d1b11fd8.mp4?token=fl_xLwOH_nLSf9Hs0RYaAAwllG6SUd_RFngr8ERDJG6m0NrJzozGrhRXqV_QvpiUpVTUGhsCrQzRATO1tN833xwbAqP0LHDgl1A8VoYN1RtB0aUcLH1nBBBvsH51hxG-SpNJ7bI97N4CPLgux230N20Zel4VNYo4PNBIFhsdIgImwCIxjJf_44baaktOV2IN6NfXwzWLwFL8p46ZPQJkVYZioeK2_aBfaOmZX0QmmgQnRfT-72a-F5gYQKk6uLS1SAnxiHxmILO6GKhtbqKbqK0zAv6ePxIQSbsHfbn4wCE9XsymcRBivG0Vk-9_UZXDz3VuJjivXLsMmGBXpPCWxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مارکو روبیو:
ترامپ قرار نیست توافق بدی امضا کنه. هیچ‌کس به اندازه ترامپ تهدیدِ هسته‌ای شدن ایران رو جدی نگرفته
خیلی مطمئنم که یا به یه توافق خوب می‌رسیم یا مجبور می‌شیم یه جور دیگه باهاش برخورد کنیم.
ولی ترجیح ما توافق خوبه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/65047" target="_blank">📅 13:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65046">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">قالیباف دوباره به عنوان رئیس مجلس انتخاب شد
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/65046" target="_blank">📅 11:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65045">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKePD1kZfIxmvTFRES129N6F9bxNzJ9TZr5lWCKZcsXsgFtYT2W0vB-HDTTmMrjnhPCNLlzXueUFC5SlPuqt2ueX9FCZYPwPwYZKdGnvuSg9H7M-Fm2AuLGipQ0_GS-NNdXgnARpGBpxApT_X5D2mgRiLIXHnKTPZ0DZeE9Ud6z-3sndedapeYqPmbAPWshWTV8lYF17CIUe4j_dvGxLVYv1j9Tu_FrJA36UoA5u1PuxajKctQLnrSuTW9FcCjaf_Y4-9J3DFRenq6Pt2qpiODz7n8CmOSK6kw-WBDnmEoF_TVGWujpNQ3tSCSD42xluBL8KtmqHyGo64ajdJMNiFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوج حقارت ارتش
ایران
به روایت تصویر:
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65045" target="_blank">📅 10:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65044">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو: توافقی برای پایان دادن به جنگ علیه جمهوری اسلامی ممکن است «امروز» حاصل شود
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/65044" target="_blank">📅 10:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65043">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام: اگر در واقع به نتیجه این مذاکرات برای پایان دادن به درگیری ایرانی، متحدان عرب و مسلمان ما در منطقه توافق کنند که به توافق‌نامه‌های ابراهیم بپیوندند، این توافق را به یکی از مهم‌ترین توافق‌نامه‌ها در تاریخ خاورمیانه تبدیل می‌کند.  پیوستن…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65043" target="_blank">📅 00:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65042">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqvLUvXNEb55hrSkQ2vU1t7O87U_q8GlVwE5Cxw_rR9dOTbBcFfzh85h-pfq_NLF8GrKeyxB5ZadgymSZK_WWIJpD64AZYVnv-HcHs3HXq3OpSOAhiDBLBbLoDgRQtUChNnpdLlF8Z0DnQiSj6YiagPirMaBHJgCfO8dWhl0L91k1jwZLWd40WJ95PY-UwaDvWS6xq-YeMv8YFLgFaPy602praHBFxCs9f_vZClKncTJkr6SbBLNstwjcJOmBqqkTFgwa0gkz6mJPyRl577tLopAjN7SuDl7yiw4bISeYeg06uRhDL5DgPC0WFzUPdOv9Ox1dYk5xPQbgqbD7gg6QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام:
اگر در واقع به نتیجه این مذاکرات برای پایان دادن به درگیری ایرانی، متحدان عرب و مسلمان ما در منطقه توافق کنند که به توافق‌نامه‌های ابراهیم بپیوندند، این توافق را به یکی از مهم‌ترین توافق‌نامه‌ها در تاریخ خاورمیانه تبدیل می‌کند.
پیوستن عربستان سعودی، قطر و پاکستان به توافق‌نامه‌های ابراهیم فراتر از تحول‌آفرین برای منطقه و جهان خواهد بود. این یک حرکت درخشان از سوی رئیس‌جمهور ترامپ است.
به عربستان سعودی و دیگران: اکنون زمان جسارت برای آینده‌ای جدید در خاورمیانه است. من انتظار دارم، همان‌طور که رئیس‌جمهور ترامپ پیشنهاد کرده است، شما در واقع به توافق‌نامه‌های ابراهیم بپیوندید و به طور موثر درگیری عرب-اسرائیلی را پایان دهید. اگر از رفتن به این مسیر که توسط رئیس‌جمهور ترامپ پیشنهاد شده است خودداری کنید، این موضوع عواقب شدیدی برای روابط آینده ما خواهد داشت و این پیشنهاد صلح را غیرقابل قبول می‌کند. علاوه بر این، این موضوع توسط تاریخ به عنوان یک محاسبه‌گری بزرگ دیده خواهد شد.
رئیس‌جمهور ترامپ: در گرفتن یک معامله خوب با ایران بر موضع خود بایستید. به همان اندازه مهم است که بر موضع خود در اصرار بر پیوستن عربستان سعودی و دیگران به توافق‌نامه‌های ابراهیم به عنوان بخشی از این مذاکرات بایستید.
دوباره، این یک پیشنهاد درخشان از سوی رئیس‌جمهور ترامپ است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65042" target="_blank">📅 00:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65041">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آیا دونالد ترامپ، باراک حسین اوبامای دوم خواهد شد و دستور آزادسازی ۲۵میلیارد دلارِ جمهوری اسلامی را می‌دهد یا خیر؟!  بزودی خواهیم دید! @News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65041" target="_blank">📅 22:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65040">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_7RSwefEq7FzLYLjJasOMhExQApmBUMrpTLMNLMXAQ0_FOXQRB6SI2Yza71REutbKs6G6a-JLm7V1rijzLiJOFkEyj4Hg5-P8bMAuqbaW6goaD3syFvP8NRkGqvX6tAS5RJ3-qOqTWBAEU-yjJvPqrv7q9x68vqIEBRjiUutBRUhCnRZWbHiNXfTNs8Jl08Rnuwt4_0XALRdpErDbmA2BnVrwvwGJHvfaLLgVdGyAMmIKc1gTPiCeDeJK45vsopu701PhILgMePsdtzmUEuE34ZbsBCI1ERvF0CYCjtNYvxZ1umxCDWypNFy7sZzHKNBvCGZnBzWk3pLRbxMfU6jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:  اگر من با ایران توافقی انجام دهم، توافقی خوب و مناسب خواهد بود، نه مانند توافقی که اوباما انجام داد و به ایران مقادیر زیادی پول نقد و مسیری روشن و باز به سوی سلاح هسته‌ای داد. توافق ما دقیقاً برعکس است، اما هیچ کس آن را ندیده یا نمی‌داند چیست. هنوز…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65040" target="_blank">📅 22:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65039">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgaXH5RUI9d-Py7XMKdhHvcpRDwjG105e7nQ0IYaE7-0G3_b4354NUIGySEBv_ZANNCJaMJZscj4029wsDKojy1r-e7qsCgD5XJAt-F0UkyZDs-UEB2FxFkcdcgwL_-zxkeBs55sH7Uxjx4ox3UosimJ6i353l5DVe7OVXwJPYtWE33SYwsZcx9vlMizYFMizd-ApucD6kRWwVVXgy2FJn9xNOnYUXvxyrHUDapr1HSYl-jXbYRy2epE1rm7ocLhDHqqjiplFPDfs2leYl71OtTlqV1X55LBnAdqoWeTa-x2b9nxQ3GvpnV0eNERSn_KALtntT3pbX9PEzimOcsyzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
اگر من با ایران توافقی انجام دهم، توافقی خوب و مناسب خواهد بود، نه مانند توافقی که اوباما انجام داد و به ایران مقادیر زیادی پول نقد و مسیری روشن و باز به سوی سلاح هسته‌ای داد. توافق ما دقیقاً برعکس است، اما هیچ کس آن را ندیده یا نمی‌داند چیست. هنوز حتی به طور کامل مذاکره نشده است.
بنابراین به بازندگان گوش ندهید که از چیزی که هیچ چیز در مورد آن نمی‌دانند انتقاد می‌کنند. برخلاف کسانی که قبل از من بودند و باید سال‌ها پیش این مشکل را حل می‌کردند، من توافق‌های بدی انجام نمی‌دهم
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65039" target="_blank">📅 22:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65038">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو: توافق نهایی با ایران به معنای برچیدن تأسیسات غنی‌سازی هسته‌ای و حذف مواد هسته‌ای غنی‌شده است. من و رئیس جمهور ترامپ توافق کردیم که هرگونه توافق نهایی با ایران باید خطر هسته‌ای را از بین ببرد. این به معنای برچیدن سایت‌های غنی‌سازی هسته‌ای ایران…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65038" target="_blank">📅 20:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65037">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: من معامله بد انجام نمی‌دهم؛ در مورد جزئیات توافق فعلا حرف نمی‌زنم، صحبت های خوبی در راه است
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65037" target="_blank">📅 17:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65036">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">تنها چیزی که ترامپ تغییر داد رژیم غذایی مردم ایران بود
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65036" target="_blank">📅 15:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65035">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db79f15b4f.mp4?token=qkNYLYW_HTjZ96lTtMGRsfKOorDrpka3LZRyGuojSGidFTz6pnF5O1rYYq_ohQy8u3Mya7SVkaMWezk0bGwYG9k_aGCoswREQOJc7wVeFPdWQMjUMw9w4hesKXAjVvNyApAG5_eM7VSfuK3WwWfHkwBB-7xXlXP9FynfIVJsrFbS1oHknglRmEjJs9-unb18ZVYZzmXMbGzblb0DTYsCz3N9cPsmw1rItIZfA4H2BdCyZzWVyCXOD2Ng8Nc04xyAtttcOjRR9HpNynCdPD35XbetK_zgUBY3Amab1LKgXENDt0wxSlQOwxsk6QYjP1mCrJ7EBV6Iuf8kBueNrOWing" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db79f15b4f.mp4?token=qkNYLYW_HTjZ96lTtMGRsfKOorDrpka3LZRyGuojSGidFTz6pnF5O1rYYq_ohQy8u3Mya7SVkaMWezk0bGwYG9k_aGCoswREQOJc7wVeFPdWQMjUMw9w4hesKXAjVvNyApAG5_eM7VSfuK3WwWfHkwBB-7xXlXP9FynfIVJsrFbS1oHknglRmEjJs9-unb18ZVYZzmXMbGzblb0DTYsCz3N9cPsmw1rItIZfA4H2BdCyZzWVyCXOD2Ng8Nc04xyAtttcOjRR9HpNynCdPD35XbetK_zgUBY3Amab1LKgXENDt0wxSlQOwxsk6QYjP1mCrJ7EBV6Iuf8kBueNrOWing" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مارکو روبیو: امروز اخبار بیشتری از توافق با ایران منتشر می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65035" target="_blank">📅 14:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65034">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPoNpF_0Y3cZ1TcGkLxggEZEcV8LQmtrdLwblRbAVjhAkROGvYt7aD7gxjV_k9InaZ59DFAu1GL8jEDnox-ICNhL03R53pVrcHHwisxspKACHbDE9Iwd4K71zS5XGd2tpEbmG14IRpdpRtvIQvlRmjFdK_D8mARVMSiKDxSjdPTIs6MT3EO7Q11IgqTciV6Qz97oLEz2icwGT9PqvyFaUmk27L_R9QSSg2cRwlbvJ_m3CtuiutdMp0kR-8v9jf6Xu5JoNU13rqTtuoAKONlpG2ti0pS06EzHGGM7ycy8NgHoThfD_VGETkEGuvlD_vzFnTO8uuf9fHEulYgAJEFADQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کجایند مردان بی‌ادعا؟
🗿
#Fun
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65034" target="_blank">📅 14:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65033">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مراد ویسی: سپاه می‌خواد روحانی، احمدی‌نژاد و پزشکیان رو ترور کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65033" target="_blank">📅 10:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65032">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kyX0lPebiYu3S0E8f3gDT8qs5BK9RjdYjNnGPCJUXjpql93cPpsq_gRkDJ7xDbvn0TesWageBv656ZE77lEXeqDEnFC67KQu_YWrVqna7L4Fpk2aDXraVjj29A-sCi3rQBZzbsJ3wGtDrqOh9j3vv8m6JhJdt1wmoGs2nUzegh6V32AqWQK534HiU3v36wehOdoRlpiG952U3XlfjDHw7hBOnN0x7bgbZoVaXA9I_P8PLCBS_XJHQ7lcaIqomAaYBytqkd0UXaM3EdOFtRTJ0dWJ-9eQnM_BFjJHJLmlZwaCrDnuKamPeP2OFkhPfJcn8yDgnMuu1WMu4YCLnJPhyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار تتر بعد از اخبار دیشب درمورد توافق تا زیر 170 هزارتومان ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65032" target="_blank">📅 10:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65031">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
آکسیوس: توافق بین دو طرف امضا شد.
👎
این خبر فیکه و آکسیوس و خبرنگاراش همچین خبری نزدن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65031" target="_blank">📅 01:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65030">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f43de325c3.mp4?token=o3r4J8CfG7jAyRs2MGMIazB1-tkF9p-elUIOkTts4tvdfmroYihbwBAVJg00gftZhCM44Jdvh9xShjzP5ok964KT8Kdo2IwEx7qY_V9Rdv0YMsGNqTIL1SiXchCjl62a_PHd9OmBxOKIucNeVIiOYg9pE9SUJz_o_2V5V8FbrFkubz47locK38CWgqRTwgXu8fRDjMLYGrCemNGkD-b3fitvxMgFUUBkkonKzd_Z0eV3XPoLWli1jb52uLeMCDs5OmHh8NWpk6VE-0ps4j9kDfAekO4acUF5YfPrWkdg4l28YpYO4_FH5r1IrCkNRfzf0k4a5WA7WBNZpMwQeGzW0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f43de325c3.mp4?token=o3r4J8CfG7jAyRs2MGMIazB1-tkF9p-elUIOkTts4tvdfmroYihbwBAVJg00gftZhCM44Jdvh9xShjzP5ok964KT8Kdo2IwEx7qY_V9Rdv0YMsGNqTIL1SiXchCjl62a_PHd9OmBxOKIucNeVIiOYg9pE9SUJz_o_2V5V8FbrFkubz47locK38CWgqRTwgXu8fRDjMLYGrCemNGkD-b3fitvxMgFUUBkkonKzd_Z0eV3XPoLWli1jb52uLeMCDs5OmHh8NWpk6VE-0ps4j9kDfAekO4acUF5YfPrWkdg4l28YpYO4_FH5r1IrCkNRfzf0k4a5WA7WBNZpMwQeGzW0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همونطور که اکثریت رسانه‌ها گفته بودند، احتمالاً یک راستی آزمایی ۳۰ روزه در قالب توافق موقت، برای پایان رسمی جنگ و بازگشایی تنگه هرمز شکل خواهد گرفت، و بعد از این توافق طرفین به سراغ مسئله‌ی اصلی یعنی هسته‌ای و تحویل اورانیوم ها خواهند رفت  شما اینطور بخوانید…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65030" target="_blank">📅 00:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65029">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fad8544d2.mp4?token=GtPHt7-EAx-o4NsJ2J35zJa83-xFaF2BgQgyGf9BLztgo9mvTqaV6givnjenDFG2hhH4_gXUwSKh7UCwzDwUya8oncTrYr1irT_yOIrAJxFtuqI0yweDo0RLgHFAcHHS0ZkFOt8ASFE1uA47RDnGvQU-Cs9IJho8AgvC5_6MewB7vQ3LX6gffyV3-u5bNeFU0FLehQOOod5VqV5eGsXGnTfJd8yBSbU1RdjaPd3UcIsozlnV4YIr9EZJXtqumi3jEKb4x0CE4O9Ah4epwUi78KmCuZTQXfp10tWgj7SBw8lFUREtL6LU-0H4_Gv2n9MxkkbDgjkYGuW_jWAqBTPi9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fad8544d2.mp4?token=GtPHt7-EAx-o4NsJ2J35zJa83-xFaF2BgQgyGf9BLztgo9mvTqaV6givnjenDFG2hhH4_gXUwSKh7UCwzDwUya8oncTrYr1irT_yOIrAJxFtuqI0yweDo0RLgHFAcHHS0ZkFOt8ASFE1uA47RDnGvQU-Cs9IJho8AgvC5_6MewB7vQ3LX6gffyV3-u5bNeFU0FLehQOOod5VqV5eGsXGnTfJd8yBSbU1RdjaPd3UcIsozlnV4YIr9EZJXtqumi3jEKb4x0CE4O9Ah4epwUi78KmCuZTQXfp10tWgj7SBw8lFUREtL6LU-0H4_Gv2n9MxkkbDgjkYGuW_jWAqBTPi9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همونطور که اکثریت رسانه‌ها گفته بودند، احتمالاً یک راستی آزمایی ۳۰ روزه در قالب توافق موقت، برای پایان رسمی جنگ و بازگشایی تنگه هرمز شکل خواهد گرفت، و بعد از این توافق طرفین به سراغ مسئله‌ی اصلی یعنی هسته‌ای و تحویل اورانیوم ها خواهند رفت  شما اینطور بخوانید…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/65029" target="_blank">📅 00:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65028">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تا این لحظه طبق اخبار، الحدث، آکسیوس، نیویورک‌تایمز، سی‌ان‌ان، آسوشیتدپرس و... احتمال توافقِ موقت بسیار بالاست، یعنی توافقی که در اون توافق کنند برای به ثمر رسیدن توافق هسته‌ای!!!!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65028" target="_blank">📅 00:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65027">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rDMr7lkG_F3_-QUI161qzg5w4vf1hDYYbJ3Mc5FR3t8BRNtxkj8jVtoSWmUdLHKA6cXMRjpwNQoxpS4a4N3uk-264cdE-WmGUk-U6-sPFTTr6YjoG_xClSi5suxepofp6HW1k6rHf96gTauYUVUcH59HIfDY-PrL_EmqQvHzYnP_-49euz3HtCuUNxHKs8GksK_E259FEFIyU0uZMwHK6Ry0Nw5jt6wuMuaJ1gInPhTu4lxNjOJMe4rfZVkHeRzVtAfYGBxamzYFcXTFYgKXIct1uZPjCFB7C8O7xkwxU8Da01NMLN04gPVM2_VRl_ay7ZGtn4d_qDkKY4WI1v-NaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ:
من در اتاق بیضی کاخ سفید هستم، جایی که همین حالا تماس بسیار خوبی با پادشاه محمد بن سلمان آل سعود، عربستان سعودی، محمد بن زاید آل نهیان، امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی، و وزیر علی الثعادی، قطر، مارشال فیلد سید عاصم منیر احمد شاه، پاکستان، رئیس‌جمهور رجب طیب اردوغان، ترکیه، رئیس‌جمهور عبدالفتاح السیسی، مصر، پادشاه عبدالله دوم، اردن، و پادشاه حمد بن عیسی آل خلیفه، بحرین، در مورد جمهوری اسلامی ایران و تمام موارد مرتبط با یک تفاهم‌نامه مربوط به صلح، برقرار شد. توافق‌نامه‌ای به طور کلی مذاکره شده است، مشروط به نهایی‌سازی بین ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلف دیگر، همان‌طور که در بالا ذکر شد. جداگانه، من با نخست‌وزیر بیبنتانی، اسرائیل، تماسی داشتم که به همان ترتیب بسیار خوب پیش رفت. جنبه‌های نهایی و جزئیات توافق‌نامه در حال حاضر در حال بحث هستند و به زودی اعلام خواهند شد. علاوه بر بسیاری از عناصر دیگر توافق‌نامه، تنگه هرمز باز خواهد شد. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65027" target="_blank">📅 00:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65026">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahshid</strong></div>
<div class="tg-text">بله  مگه چیه ما با ۹۰ هزار ... گواهینامه مون گرفتیم</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65026" target="_blank">📅 23:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65025">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گواهینامه شده ۱۵ میلیون تومن!!!!
الان یکی میاد می‌گه حاجی ما با ۵۰ تومن گواهینامه گرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65025" target="_blank">📅 23:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65024">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بستن تنگه‌ی هرمز در جنگی که ۹ اسفند آغاز شد، تمامِ معادلات آمریکایی هارو بهم ریخت، اون‌ها حتی چند روز قبل مین‌روب های خودشون رو هم از منطقه خارج کرده بودند! دومین مسئله‌ی شوکه کننده برای اون‌ها حملات وحشیانه به کشور های عربی بود  هر زمان آمریکا_اسرائیل به…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65024" target="_blank">📅 22:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65023">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">باز تو این دقایق فیک‌نیوز و نویز‌ها بشدت افزایش پیدا کردن، اخبار ضد و نقیض زیادی به گوش می‌رسه، اما کلیت ماجرا اینه که تهران آخرین پیام خودش رو به عاصم‌مونیر داده تا به آمریکایی ها برسونه، ترامپ نهایتا تا دو روز دیگه بعد از دیدارش با ویتکاف و کوشنر، تصمیم…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65023" target="_blank">📅 22:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65022">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">باز تو این دقایق فیک‌نیوز و نویز‌ها بشدت افزایش پیدا کردن، اخبار ضد و نقیض زیادی به گوش می‌رسه، اما کلیت ماجرا اینه که تهران آخرین پیام خودش رو به عاصم‌مونیر داده تا به آمریکایی ها برسونه، ترامپ نهایتا تا دو روز دیگه بعد از دیدارش با ویتکاف و کوشنر، تصمیم می‌گیره، یا از خواسته هاش عقب نشینی می‌کنه و یا اینکه دوباره جنگی برای اعلام پیروزی شکل می‌گیره، تا این لحظه طبق اخبار، الحدث، آکسیوس، نیویورک‌تایمز، سی‌ان‌ان، آسوشیتدپرس و... احتمال توافقِ موقت بسیار بالاست، یعنی توافقی که در اون توافق کنند برای به ثمر رسیدن توافق هسته‌ای!!!!
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65022" target="_blank">📅 22:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65021">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ شنبه با ویتکاف و کوشنر دیدار می‌کند و یکشنبه تصمیم نهایی برای توافق یا جنگ دوباره گرفته می‌شود  @News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/65021" target="_blank">📅 19:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65020">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ شنبه با ویتکاف و کوشنر دیدار می‌کند و یکشنبه تصمیم نهایی برای توافق یا جنگ دوباره گرفته می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/65020" target="_blank">📅 19:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65019">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
📰
ترامپ در گفت‌وگو با آکسیوس:  در حال حاضر احتمال کاملا 50 / 50 است که یا با ایران به توافق برسیم یا دوباره جنگ از سر گرفته شود. یا چنان محکم‌تر از همیشه به آنها حمله نظامی می کنم که تا حالا مثل آن را ندیده‌اند، یا توافقی خوب را امضا می‌کنیم + ترامپ شنبه با…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/65019" target="_blank">📅 19:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65018">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
فایننشال تایمز: ایران و امریکا به یک توافق آتش‌بس ۶۰ روزه نزدیک شدند!!  @News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/65018" target="_blank">📅 19:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65017">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
📰
#مهم؛ فایننشال تایمز: میانجی‌ها معتقدند که به توافقی برای تمدید آتش‌بس به مدت ۶۰ روز نزدیک شده‌اند.  این پیشنهاد شامل: بازگشایی تدریجی تنگه هرمز گفتگو درباره رقیق‌سازی یا انتقال ذخایر اورانیوم غنی‌شده بسیار ایران کاهش محاصره آمریکا بر بنادر ایران رفع تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/65017" target="_blank">📅 19:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65016">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PA89pgB3tHVq6LsDEsBCVPJzjMfPzMXN6Zvx53NsuUI3NAq2E1OZnrVCbpdqrVWbz3BCxn1KRIjqrDFC_NXzFPEW9l7lEaglG6iTlNLeIOl_TzmN38ob9HcwwTwpkwYXTvro5xq4m0nCcVKkpjPi-tvOZ0N-oeqOldU_f2RSwvqmV6x-49JUWrdH2XOc_uDIB-v6G8fMfj9dUPaJ2I6s7PO7AjCnFsQuH3DiONmj_bVxYwgo9gfaPmau59JI84d1HEDHFj0gFzc_aTmBhKTgSVWVABzlcgmOHU4KpW-yGRFTT4zwGBYRg_1-RZCHNxXnqf_YaaAX-7e1k2FwygPUWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست جدید ترامپ تو تروث‌سوشال: ایالات متحده خاورمیانه!! با پرچم امریکا روی نقشه ایران
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/65016" target="_blank">📅 18:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65015">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛ مارکو روبیو: ممکنه امریکا به زودی خبری در مورد ایران منتشر کنه شاید هم نکنه امیدوارم این اتفاق بیفته
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/65015" target="_blank">📅 17:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65014">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b75d0f1f7.mp4?token=N1xGz50kOxGHJLOChf18dWwBcbeJeb3z-rX2phLPsfO2bGIjM2ayg9vIjdZiw4zdiG5KSi03-SjaLEIeHhPmX0jmtiwqmW2c-IsJZVm6sWOMZiSoY9lCYV7Wa16RooM8AHfheWKLuTHCCPRYG8Qq6hbm4boF-sgIWfiIgGCzno2RwFsoX-y6IIhlJGR_djhpVXte7TrF4leBW9H2ayIbor9yAfiJCxVdg2yoT4ox4HigLkgJ50_fWb9ZzwuETSqujEb6hqC62v31-_ReZqK73BOfE1cOdo0-3vJeeqHO-Voms1coQ-neM6gSHhO5SsUJ3c_XrlMxIEiJvVc1XP6LVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b75d0f1f7.mp4?token=N1xGz50kOxGHJLOChf18dWwBcbeJeb3z-rX2phLPsfO2bGIjM2ayg9vIjdZiw4zdiG5KSi03-SjaLEIeHhPmX0jmtiwqmW2c-IsJZVm6sWOMZiSoY9lCYV7Wa16RooM8AHfheWKLuTHCCPRYG8Qq6hbm4boF-sgIWfiIgGCzno2RwFsoX-y6IIhlJGR_djhpVXte7TrF4leBW9H2ayIbor9yAfiJCxVdg2yoT4ox4HigLkgJ50_fWb9ZzwuETSqujEb6hqC62v31-_ReZqK73BOfE1cOdo0-3vJeeqHO-Voms1coQ-neM6gSHhO5SsUJ3c_XrlMxIEiJvVc1XP6LVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اسماعیل بقائی، سخنگو وزارت خارجه:
ما هم بسیار دور و هم بسیار نزدیک به یک توافق هستیم.
دیدگاه‌ها به هم نزدیک‌تر شده‌اند، اما نه به حد یک توافق — بلکه به حدی که ممکن است بتوانیم به راه‌حلی برسیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/65014" target="_blank">📅 17:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65013">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73653df566.mp4?token=lJZNRcq5vJ7cIdvxKJQWzCAlkRxbXlAP2cSaJbBdU_LPdnMQ1rUr23bodIzBQTefTPhTk4H9qpcsQ5wTXmPgEKRmVZXTS-Uq8ANc8KHfsUohE03BAWNqXz1UyJUW-AfSBs3l11jyMB2U4HNAFwtjWdVVfOkI1guiLRWEmDcHguDhUFZbFt3-WbL5kT7x_CIRyQuLalx_FjuI_wvOapxUp6VR0zWA6-iH-Bh98v50E7t-sckhETJSS2DxJOw4S3sNUYlgSKDM5Jn7ZUm3ZETIYHlgXdyTMG3splpGrq_Tk4lXK8NJgvszpPXLvIIN5iBffvbaeIRrv0Nw7WEfpGWrZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73653df566.mp4?token=lJZNRcq5vJ7cIdvxKJQWzCAlkRxbXlAP2cSaJbBdU_LPdnMQ1rUr23bodIzBQTefTPhTk4H9qpcsQ5wTXmPgEKRmVZXTS-Uq8ANc8KHfsUohE03BAWNqXz1UyJUW-AfSBs3l11jyMB2U4HNAFwtjWdVVfOkI1guiLRWEmDcHguDhUFZbFt3-WbL5kT7x_CIRyQuLalx_FjuI_wvOapxUp6VR0zWA6-iH-Bh98v50E7t-sckhETJSS2DxJOw4S3sNUYlgSKDM5Jn7ZUm3ZETIYHlgXdyTMG3splpGrq_Tk4lXK8NJgvszpPXLvIIN5iBffvbaeIRrv0Nw7WEfpGWrZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توئیتر اکانت ترامپ که با هوش مصنوعی به ویدئو درست کرده از مجری سی‌بی‌اس که مخالف خودشه و ترامپ میندازدش تو سطل زباله :/
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/65013" target="_blank">📅 15:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65012">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SdPSqzNNnhHQu8BGG1ZzrlBDhPRsaDBtLMrb5UnlJAFyHASbecsHmkZ2cgb-CxFZgEg4f-QVOMqHdl56Ogck_0rck9VHHX6J5UMjkvFQAOH6AeTjzHjPcV3iYZQAB6_rqAKTkhd1lLax8h0AxGMHhuixhhYfiLWeyPKNSJ47vkU4rrHBkgy7Y9LpgqBAqk7VTG2SEMgfMhOYpaS17_vOxi2TiE5tiia8IxXj6A3rqTv5gDZqkQckjcgr0DkWmeRb2QUmShJx80qSV8CKzr-HvFoLspZFURJKqjU6Rimz354hvu8dDlVI0z4yd7ZjgVZbbKMR7v6eEyCdL1X7g8auKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ عروسی پسرش بود نرفته، آخر هفته برنامه گلف داشت که کنسل کرده و تو کاخ سفید مونده حالا خبرگزاری‌ها شدن دو دسته یه دسته میگن توافق نزدیکه حتی متن توافق منتشر میکنن یه دسته متن توافق بقیه رو تکذیب می‌کنن و میگن کلا حتی نزدیک توافق هم نیستن دو طرف.  این وضعیت…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/65012" target="_blank">📅 14:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65010">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c1pATJ2o-bjzfbxwmJtU525jCoMfUTXOvsyN23DrACv69IxQxmcUzCXBv_Z1vIJG0prMy3g8sVYgTPQwuDlAYAdrcqVeLrGsZghdTadzU9FSberrzNJ0TBjIq9gWTqA_zWBTLO7fJE2TxKOxMFbwfSdBvfWs-U130EGAxusF6K7XQF1ICaVPpbjUesE_ePqr8qRggtr_T9UxmWeTLmxtd5ZVh3XvM7GrWTsPmim1AouTC3hCtWz27g3QvxpuRLiOIDK8z-PCu-KUuuGPpdQWsl_oYln1IIeeXpNbpsOMxFNnXDLZlgsHw-yctAe9ux-e6-jCSWLnd4Gtrq5LXM4gPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6eddfffea5.mp4?token=H7KsURpxZ28EP5HIXlMTAXFYpRTYmFGhN4ALfwzIw_NrCMtDH9rxplzvA6RTtxpfc00E56yi657NvrxoilOkhDEspVOsPfzTEohWEirV9gow4cwy4BIXl90TqGeBIn1LErp-oyUq6hcyL7KzMIUY_bhpudbvRWzecRBvGC2-WpQiph3L0Jj_QP_7NZqID7f-IF-b92gcta3VxzlYAz4VTO2b7kvU9vJmhD1s6AikztgiaQPrL4cjJu8J5E952nkXKKxoJXta9XlsPbo5If20WfsmQOBbugdf4ZF3upKhXpVQkc0ej1ImIX0bvcCq_KSlAnTWJXJM9yYj21s--NDGVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6eddfffea5.mp4?token=H7KsURpxZ28EP5HIXlMTAXFYpRTYmFGhN4ALfwzIw_NrCMtDH9rxplzvA6RTtxpfc00E56yi657NvrxoilOkhDEspVOsPfzTEohWEirV9gow4cwy4BIXl90TqGeBIn1LErp-oyUq6hcyL7KzMIUY_bhpudbvRWzecRBvGC2-WpQiph3L0Jj_QP_7NZqID7f-IF-b92gcta3VxzlYAz4VTO2b7kvU9vJmhD1s6AikztgiaQPrL4cjJu8J5E952nkXKKxoJXta9XlsPbo5If20WfsmQOBbugdf4ZF3upKhXpVQkc0ej1ImIX0bvcCq_KSlAnTWJXJM9yYj21s--NDGVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بابک زنجانی از برنامه جدیدش به نام مای دات رو نمایی کرد و برای تبلیغات نوشت:
اینستاگرام پولی میشه ولی برنامه ما رایگانه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65010" target="_blank">📅 13:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65009">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
⭕️
ایران با صدور اطلاعیه‌ای، پرواز در بخش غربی حریم هوایی خود را تا صبح دوشنبه ممنوع اعلام کرد.  @News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65009" target="_blank">📅 03:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65008">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
⭕️
ایران با صدور اطلاعیه‌ای، پرواز در بخش غربی حریم هوایی خود را تا صبح دوشنبه ممنوع اعلام کرد
.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/65008" target="_blank">📅 01:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65007">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">واقعاً خوشبحال جمهوری اسلامی که با چنین اپوزیسیون احمقی طرفه، نه تنها پادشاهی خواهان با [به اصطلاح] دموکراسی خواهان دائما درگیر هستند، حالا خبر رسیده که علی کریمی و شاهین نجفی از داخل گروه پادشاهی‌خواهان هم باهم بشدت درگیر شدند
!
شما با این وضعین می‌خواین در مقابل آخوند بجنگید؟ جای تاسف داره واقعاً، حیف مردمی که گوش به پست و توییت های شما بودند و هستند!
#hjAly</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/65007" target="_blank">📅 22:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65006">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ec1cebe91.mp4?token=NPV-oHHKHW45sC2KdFx02PPeqH1Tjzxku_irw8NcXvKyV7tK-tyQdEu6ZkRUNwsTSxVc3AhIaBzZPRzn58erHAEbWiLEQibGZKDS5ITM99KxQZge1VgpkUP_ha9crEYePJ5DaUkjvbKgOs7HN3Kejq-2mETVh6kyORvF_llgpybI-aL5oQNWGxH0NnbeGGtKdBTIITijY1onZSMSuqpNefIDgnKxahwMi3TyFrSGjxNiM550P_oMLhECrD2G2_OG8EDu0V8z8OhOAIpRHlr9kTOihgpgUNHnh-8BHyQJrXiK5PVEumS75Ys5knWA5GQDwokLnLPCACceHXhf8_Kq6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ec1cebe91.mp4?token=NPV-oHHKHW45sC2KdFx02PPeqH1Tjzxku_irw8NcXvKyV7tK-tyQdEu6ZkRUNwsTSxVc3AhIaBzZPRzn58erHAEbWiLEQibGZKDS5ITM99KxQZge1VgpkUP_ha9crEYePJ5DaUkjvbKgOs7HN3Kejq-2mETVh6kyORvF_llgpybI-aL5oQNWGxH0NnbeGGtKdBTIITijY1onZSMSuqpNefIDgnKxahwMi3TyFrSGjxNiM550P_oMLhECrD2G2_OG8EDu0V8z8OhOAIpRHlr9kTOihgpgUNHnh-8BHyQJrXiK5PVEumS75Ys5knWA5GQDwokLnLPCACceHXhf8_Kq6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امتحانات نهایی پایه یازدهم و دوازدهم تو بازه ۱۵ تا ۲۰ تیر به‌صورت حضوری برگزار میشه
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65006" target="_blank">📅 22:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65005">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🎙
خبرنگار: آیا در عروسی پسرتان شرکت می‌کنید؟
🇺🇸
ترامپ: او دوست دارد من بروم. من سعی خواهم کرد. گفتم این زمان مناسبی برای من نیست. من یک مسئله به نام ایران و مسائل دیگر دارم. او شخصی است که مدت‌هاست می‌شناسمش.  @News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65005" target="_blank">📅 21:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65004">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
العربی‌الجدید: سفر عاصم منیر به تهران دلیلی بر توافق نیست و پیام جدیدی منتقل نکرده است، گزارش‌ها درمورد مفاد توافق گمانه‌زنی است و اختلاف بین طرفین هنوز زیاد است.  @News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65004" target="_blank">📅 21:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65003">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
📰
العربی‌الجدید به نقل از یک منبع نزدیک به مذاکرات:  سفر فرمانده ارتش پاکستان، عاصم منیر، به تهران به معنای این نیست که توافق در دسترس است. گزارش‌ها درباره وجود پیش‌نویس احتمالی توافق صحت ندارد و صرفاً گمانه‌زنی‌های رسانه‌ای است. وزیر کشور پاکستان پیام جدیدی…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/65003" target="_blank">📅 21:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65002">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
📰
العربیه: طبق منابع العربیه، انتظار می‌رود پیش‌نویس نهایی یک توافق احتمالی میان ایالات متحده و ایران که توسط پاکستان میانجی‌گری شده است. که ممکن است ظرف چند ساعت اعلام شود.  شرایط کلیدی آن عبارتند از: آتش‌بس فوری، جامع و بدون قید و شرط در تمام جبهه‌ها، از…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65002" target="_blank">📅 21:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65001">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خبرگزاری های حکومتی: عاصم منیر وارد تهران شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65001" target="_blank">📅 19:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65000">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2227480c5d.mp4?token=cKomxQbUjIGnTojTOOkFRmr-26JV0g2UrXHSuo1Q-hv-76X4z3vooiWlypr3aOvX40BAXMXbB0i66czvfsPfkAFslK2VC2Ha77MgRWbd1fOVDRw_FVfcKfXa0Zj28mCUcatgfYFrhgLx8FbL-JoLeE8M5UxbHKNj7JXkADm97JVbytTDLBuvxgOlEn2ov917uaIQW7tGTYbHJLl-W3kUdYEvaoBHZMBN4rYsMiXsCVBtIDj9ExC9LuJv56P3SWkhKpVuI6fBSa5c8BBqWGKEt_bofhndTv8sC62wRk-4PfszpBXNVc6H4_s0r-bj0Nau5Ddtyb4eNwa1_HsYCDrJOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2227480c5d.mp4?token=cKomxQbUjIGnTojTOOkFRmr-26JV0g2UrXHSuo1Q-hv-76X4z3vooiWlypr3aOvX40BAXMXbB0i66czvfsPfkAFslK2VC2Ha77MgRWbd1fOVDRw_FVfcKfXa0Zj28mCUcatgfYFrhgLx8FbL-JoLeE8M5UxbHKNj7JXkADm97JVbytTDLBuvxgOlEn2ov917uaIQW7tGTYbHJLl-W3kUdYEvaoBHZMBN4rYsMiXsCVBtIDj9ExC9LuJv56P3SWkhKpVuI6fBSa5c8BBqWGKEt_bofhndTv8sC62wRk-4PfszpBXNVc6H4_s0r-bj0Nau5Ddtyb4eNwa1_HsYCDrJOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مارکو روبیو:
ما باید شروع کنیم به فکر کردن درباره کاری که اگر چند هفته دیگر ایران تصمیم بگیرد، «ما اهمیتی نمی‌دهیم؛ ما تنگه‌ها را بسته نگه می‌داریم؛ هر کشتی که به ما گوش ندهد یا به ما پول ندهد را غرق می‌کنیم» چه باید بکنیم — آن وقت کسی باید کاری در این باره انجام دهد.
امروز این نکته را مطرح کردم؛ خیلی‌ها سر تکان دادند؛ خیلی‌ها بعد از آن نزد من آمدند و آن را تأیید کردند، اما امروز خبری برای شما نداریم که چیزی در حال وقوع باشد.
باید پلن B داشته باشیم برای اینکه اگر کسی شروع به تیراندازی کرد و چطور تنگه‌ها را باز کنیم، و من امروز این نکته را مطرح کردم. نمی‌دانم که آیا این لزوماً مأموریت ناتو خواهد بود، اما قطعاً کشورهایی از ناتو می‌توانند در آن مشارکت کنند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65000" target="_blank">📅 18:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64999">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/news_hut/64999" target="_blank">📅 18:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64998">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoO5dK7-s1wwVbaVupFO4Zb-IwTcPItrX6jB_nPMSD5KwG1fu9Krt3rqJ6yypg0JwWAe1aRV1832kY7G_3TycSyyiegtQg1fbNMVCaw-9VxtdN-XJAx0BPAXoDnb2aKdceVVvhTIVs-g4DWvAPH6UIcBH9ZgZ2b65GngnvzowYJHem_og74zpeW4AGweDgTQYqA6kXmu6tRsVjk5r28iojEverfdXHcwHRHijlsmC9wokgXiQqo_4PMKN09rB1ufeDs-t7buaee-OIjwRPpkWDqYYt_3LCDapCyVY2J4Qf2wQgZefMm8O2qZzuKCimqLKkeOgXRJfD9XCMv4kBjxBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📰
لارنس نورمن، خبرنگار وال استریت ژورنال: یه منبع میگه هر چیزی درباره پیش‌نویس توافقی که داره می‌چرخه، دروغه و صحت نداره!
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64998" target="_blank">📅 18:07 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64997">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
📰
رویترز: یک تیم مذاکره‌کننده قطری امروز به تهران آمده است با هماهنگی ایالات متحده برای کمک به پیشبرد تلاش‌ها به سوی توافقی برای پایان دادن به جنگ با ایران و حل مسائل باقی‌مانده.  @HutNewsPlus</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64997" target="_blank">📅 17:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64996">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7YR5APv8b5spKxaHsCLpCop-baOlAI8R20rKuncnPvJdCp6IXPKXyZOJGXHdifCsmVhmFfhnRLehCtRxyRxtfizVOaGOJizmuVSwEdW2GXwcomL4gQVsuXMbcRs3xYG5rAMibwzDqKMMRxpMFa3CNsdkbCC1Fhx5D3-D_kddz7b1bwnnoDGzGX9CnlJvhuKi7tmUenC_RZU9bb7OIR3l6hzV9Ed5LfagiyRkkGVq6SF6IHwJzRpBfrTTj58wKol7un8YHilKTllvc-9tAtnbbVjK_cfcy5zNOE7IiM1XtVrAlq2mHVZ5lGkoSLeB2Za2w2CjTp_GRxi1BYwKQG2iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو هواپیما دولتی پاکستان راهی ایران شدند؛
احتمالا عاصم منیر در راه تهرانه
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64996" target="_blank">📅 16:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64995">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jxUsnGMQopaD0cJl2TjUhjo5_Sbcy9Gl-WnmOPrp4mGIWwwzDpMW_q67s8d2Zdyb2NCuWlMCWupRFJ7qK6DSjJOsax-jSg5ihtuRjnEFJnlMJDVtiqAyTJDPIzED8Iaw1xYqq1A7GVphyixjv2rRvvULfuXGJ5ws-a9M7Ez9M9YBiimoBS_TiB2xgdzYCd5IAlFxftCdV17fantLOiJiWR_5Rfwld6WM5hnnL00_L82Zc13A3I6s0Fb0y0Vt0cy-LjwyfrYmU9a5_r2Jfyv1KJlDMIwii4EowpdmJfVvia2nk1VtwyXbm88Olzi1cWkwdC41ZMqWmKAHi8eedfxoqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یزدی‌خواه، نایب‌رئیس کمیسیون فرهنگی مجلس: نهادهای بالادستی به این نتیجه رسیدن که بازگشایی اینترنت به صلاح همه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64995" target="_blank">📅 14:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64994">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سپاه: تو ۲۴ ساعت گذشته به ۳۵ کشتی اجازه ورود و خروج از تنگه هرمز رو دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64994" target="_blank">📅 14:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-64993">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
سفرِ «عاصم منیر»، فرمانده ارتش پاکستان به تعویق افتاد، این یعنی هنوز اختلافات ایران و آمریکا حل نشده
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/64993" target="_blank">📅 23:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64992">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3890f54566.mp4?token=L-_KdvlB7tJe-9fWeaXTxcU2nZWeseU4pXefnu48xEdjEJV2kU-oraJ-4jnBmYYubo6_JEqm5MELkTbQrIXC_8Ru-3N6WyFD_UaEhHv2L2CpoqNIzLwHOvTZ-8HzWbuPdvqTBdusK7Y6MrLwyzgTQp0O50PBbtKfzds-s24qyjfbhOnhbvEucSnH9z31CjqVauytBb05qdxKqdZQebSmhcQBB3i1NN4KxGKfa8MSJQFRSK7JJnFey09O7yN3BCqPjrppsBlW3H49OcqqSRvw7uMnzoLDaBaS9cb7BnRDaWQUMoCWV7mCxKPDV_9wuRdfwWsxMQl-_NxE_k-FOt949g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3890f54566.mp4?token=L-_KdvlB7tJe-9fWeaXTxcU2nZWeseU4pXefnu48xEdjEJV2kU-oraJ-4jnBmYYubo6_JEqm5MELkTbQrIXC_8Ru-3N6WyFD_UaEhHv2L2CpoqNIzLwHOvTZ-8HzWbuPdvqTBdusK7Y6MrLwyzgTQp0O50PBbtKfzds-s24qyjfbhOnhbvEucSnH9z31CjqVauytBb05qdxKqdZQebSmhcQBB3i1NN4KxGKfa8MSJQFRSK7JJnFey09O7yN3BCqPjrppsBlW3H49OcqqSRvw7uMnzoLDaBaS9cb7BnRDaWQUMoCWV7mCxKPDV_9wuRdfwWsxMQl-_NxE_k-FOt949g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: آیا در عروسی پسرتان شرکت می‌کنید؟
🇺🇸
ترامپ: او دوست دارد من بروم. من سعی خواهم کرد. گفتم این زمان مناسبی برای من نیست. من یک مسئله به نام ایران و مسائل دیگر دارم. او شخصی است که مدت‌هاست می‌شناسمش.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/64992" target="_blank">📅 22:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64991">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43db173db6.mp4?token=Nym12ncqNW1r-Jm0EOS3C-zBfFVVsYr533-z7-OsPs3UJOKvv6aw10X34WQ6bSxENnBl2NpJqUWS4ChZELbPtA6ZDCq5OlEnzqjTXGFG6FVUZn2z0itW2cQRUV3V2rKh6MK8Nr2KGzu5iZ8_SvosuGqiSmKkUbL0yo8iJVBPl76Kkp2S2C87w1AVh1Y4yApmlXqsais0m0ZtT5nz9Yn_AvdNg24pI9Z9IYQIpZw45XJAH9BiHAVGnzwN2-pj9ULOcdJ2WJtZVkiA_cCUblZP-ySDwW0LOmtTJl3xTQEWzful19jo4qEzBSBSVI-SuFaHzz4-GFvQxyIzLdhTZxW2tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43db173db6.mp4?token=Nym12ncqNW1r-Jm0EOS3C-zBfFVVsYr533-z7-OsPs3UJOKvv6aw10X34WQ6bSxENnBl2NpJqUWS4ChZELbPtA6ZDCq5OlEnzqjTXGFG6FVUZn2z0itW2cQRUV3V2rKh6MK8Nr2KGzu5iZ8_SvosuGqiSmKkUbL0yo8iJVBPl76Kkp2S2C87w1AVh1Y4yApmlXqsais0m0ZtT5nz9Yn_AvdNg24pI9Z9IYQIpZw45XJAH9BiHAVGnzwN2-pj9ULOcdJ2WJtZVkiA_cCUblZP-ySDwW0LOmtTJl3xTQEWzful19jo4qEzBSBSVI-SuFaHzz4-GFvQxyIzLdhTZxW2tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🚨
ترامپ:
ایران نمی‌تواند اورانیوم غنی‌شده خود را نگه دارد. به محض اینکه آن را به دست آوریم، احتمالاً آن را نابود خواهیم کرد. ما آن را نمی‌خواهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/64991" target="_blank">📅 20:12 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64990">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssLxXQ7OUdfuRbHFQiaSMRyIl-4rWu3ZqkDOTN2g4hg53J0B5bDwTy9NiLkjftvu9oz3iRk5m8LJWqS0yyY-_sKL_GPIpaDIS5Wn54sw-mfOqH8NyYqOmcBBNJrWHU9TmQqDOCLm0u2CwiOq--d7UgvxLvfswMudOn_DGVfUW60pr7Vv-LJKmtfRtbdAD4mi0Oy3edNZz4QvSrYm-I_LQ7oWmWhKxsTz4wMGjzkBQs7_1BJTyMevgnmDMTMRbO2Ooz6VSUh8Fs4ARg9I1hRgQWNHmhfCy3etfTPBlYYT0i4SBfnVX9_GCQ3VAehGyXX7xwNj1vFC7_MuQ_3PwaX1iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ یه پست از نشریه نیویورک پست بازنشر کرد که تیتر خبری‌ش هست؛«چطور میشه تهرانو تو سه حرکت نابود کرد»
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/64990" target="_blank">📅 16:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64989">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7YZhpDWnZS350C0XEJwgWgTFONQNhAdST-a28BWuSOvcRG1sYAmlR1tjK-bSusjt4hFjIpwn6389OlVL2oYpr6lAq-JMVntNHGZwYWpTQZ8nXIDCePgZ8LoAI6hDlHTlD3aFvYSp6DOBVxg9s76a6sk88EX9DZ53ZeCM2KLSl1imgn8iCJtdaZK9gDClIcTMaHkx0wEl121WmWeNwf1STo52_Rr0KqhrPebkWW_rPflpJAydslsdeHm8RXL52a4Bdcf1MLuFpKtIN422fi9hMPlexsFbTSgN9XjWenkrfImximl0MSO02-6GXLEo1d16N_yaVyFn67z1_ExXXmBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ جدید هزینه‌ ریجستری گوشی‌های آیفون
ریجستری آیفون ۱۷پرومکس، ۱۰۴ میلیون تومان!!!
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/64989" target="_blank">📅 15:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64988">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GM1wuNKvTnleZSEDksL2p7yQqjpAryTDIyjR7G8miA4QyrBYx6n8TrfHQc_xVAxqVEt91NwNTz-6rua32eqLBT7XgjJYBWqsRi6Oxj9LplSPlXyuKUPhcycgQ-nA97K7jFpugErOpdJW4KCMuyXCuS3wqJfIvVV3xHugQKl1om2fxavePCkidrASGiVczze1xYAjJTX5ui1AldnGS6bU0-HxuGuHh2fqpXYetxIVKhad-Gb30kGfLLu1VyY8BTIt3kpNHVQRgxs-XN0Mb-L5jwQRmI7NbMtSQFKRGwC8Ma40kJn9mGp3JdFbkk8zLNXdGm25w03lNHeTGJUILLs5LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فهرست کاخ سفید از مهم‌ترین دشمنان امریکا که در دوره فعلی ترامپ حذف یا دستگیر شدند:
رئیس‌جمهور ونزوئلا - مادورو
رهبر رژیم جمهوری اسلامی- خامنه‌ای
معاون رهبر داعش - ابو بلال المنوکی
و برای رائول کاسترو رئیس‌جمهور سابق کوبا (و برادر فیدل کاسترو) کیفرخواست صادر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64988" target="_blank">📅 15:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64987">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
📰
رویترز: منابع ایرانی می‌گویند رهبر معظم(مجتبی)اعلام کرده است که اورانیوم غنی‌شده باید در ایران بماند.  آمریکا می‌خواهد اورانیوم بسیار غنی‌شده ایران به خارج فرستاده شود مقامات اسرائیلی می‌گویند ترامپ به اسرائیل گفته است که این اتفاق خواهد افتاد دستور رهبر…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64987" target="_blank">📅 14:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64986">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
بندرعباس ۴.۶ ریشتر زلزله شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64986" target="_blank">📅 13:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64985">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CwDTxj4inSzcd0hDDUPlEiBsRFn4pJgbMUq-e_VKyHTYeiZvDdb5J_Uz-s9Cul6NIXrm5XYF92-mmi_kH5NqxOh4ftfpPTr3vWss-Ao5ASPPV2OUeQDq0ZakPdJpxcOwId0zcOTyitxNoZyVwT5gbs6IPU9gBb04TuojgwR3G24WXncbWWEQfrlaXgYXIzDgTShI_NXfiYR4bE6-F2JqPLeI-1COoZHXBUWZ0uPYlQ5FuRn_4oDypqDOTB5sjA_6lSyHe6F4bws8cR2s2VZlbkK9zC0i5drLpq_HB2ZoquJr5l5SExLiyXdyB7idMFBiN6rZU2GInnraQdFFMppr1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شریعتمداری: تا زمان شکست امریکا و کشتن ترامپ تنگه رو باید ببندیم
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/64985" target="_blank">📅 11:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64984">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
منابع الحدث: اگر فرمانده ارتش پاکستان به ایران سفر نکند، توافق نهایی ممکن است ظرف چند ساعت اعلام شود  @News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/64984" target="_blank">📅 10:40 · 31 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
