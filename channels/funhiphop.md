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
<img src="https://cdn4.telesco.pe/file/fBAmYd-I9BNuZ9ku8kjiNhbLvFZ2r_ThimJMHr8g3NbUTl7vT17zxg5CyNMYDQyxf81HTjSS40djUGe9e9b1hkuQDMpOn0Q4Lt8Dja7EnnICgmTe-IGD-vDZf0peSc_cwDkInqfe9tHuNOeT0rrc4pYlsOeOFX_hfh51iBhWynbUL9luppdI73osm6LmyZzKAs2GAjE6kpkJIMqU0S6Behe1dK0wTLswlQ3V6RXstg2ytYGB23n2MH9kW637K2sXAvf8R-bKWDcGQSpK5fqIpJmcNEgLQ0Z-hCotm8YsyvDixfbkFt80PnhdJj9XKADSpTzLa4XJ05Iu9nYsyQn0zQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 269K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 03:10:30</div>
<hr>

<div class="tg-post" id="msg-84763">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aae0b77801.mp4?token=Odfn0UO5MS38s2sMxNheRFFHMQxs0MaWXL2MZf9V8jqSZOTqtuJ3THAYhzG7G9_u0auHdeHuPLfC0_ykLmMR47Y_G7qKFa5s664vd8Xv04wrAIbaAH6cmoQETnKxFDTtwXxhu4nHysF64lL4nb2c9bD3vvamjF2oi4zDqm3Pu_Cx_6K89yHXpK90JCnrHev5F5Q0fN_apgXtkXhULsaObSfw3XJ40hC81C5vfF5WX3OWkdWjwz7tQKGkwiFtHdDi5Aow0DI52eyPT7sflT3BvkEB4EN09e1p6JAzW0cEEwHz0JW-gX0ebVQSUnAxVmrcYW7l3gPUOsmJk2SMBdC_3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aae0b77801.mp4?token=Odfn0UO5MS38s2sMxNheRFFHMQxs0MaWXL2MZf9V8jqSZOTqtuJ3THAYhzG7G9_u0auHdeHuPLfC0_ykLmMR47Y_G7qKFa5s664vd8Xv04wrAIbaAH6cmoQETnKxFDTtwXxhu4nHysF64lL4nb2c9bD3vvamjF2oi4zDqm3Pu_Cx_6K89yHXpK90JCnrHev5F5Q0fN_apgXtkXhULsaObSfw3XJ40hC81C5vfF5WX3OWkdWjwz7tQKGkwiFtHdDi5Aow0DI52eyPT7sflT3BvkEB4EN09e1p6JAzW0cEEwHz0JW-gX0ebVQSUnAxVmrcYW7l3gPUOsmJk2SMBdC_3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثال عملی سخت کار نکن هوشمندانه کار کن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/funhiphop/84763" target="_blank">📅 01:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84762">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfFGYPbEWdmsL2TE159qX8Xg6Almi4RdJtI4T_RKa7OP5Tm0IDeSdrmckRBXgteK_wRCxlwiuWDRGrMEEO0UHqmVmhbg119Kl6eyrE5XUo5KsQJbYyJsE1xvScln8U8miiAYBcU20hZb0vrzUxw6qMPEWabcFGHQYTWBsfkgDy2wHPr_C3T2hLpvMN6SHYDoCVOj9VeGkg5chXWMSP9AQGXlD1b9LlopNOs27L8UaE7MHUUtIfRjbX-9GkVe9H0p9mKq7xnuiYefIzrhL53YjPu-nf0EqV5h6TYI_zYUeqUsS086_ou6VAAkCsGVrASrBi6C71z6qemNtxVml0GzDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/funhiphop/84762" target="_blank">📅 00:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84761">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خدابیامرز نقشش تو سریال اینطوری بود که اگه اون لحظه جلو آدم سبز میشد تیکه تیکه اش میکردی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/funhiphop/84761" target="_blank">📅 00:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84760">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYRarFE4BdUPk0ipA3hx37K0rG8Ev6r1lOfBxzWj8wExf8BfLWUHt1-MaJabj8yW8R2EYTQI6Z95MhtmNKP6F60ntqAESs_Yz8hfIXJkPVvRxYx5zuEWUjQJub4t6Vy3VEKrgYqRrrbYHzdZ9p2pK7txHcWXmW1DHUFfTSFmJfGY5WG3gnPHXNaaXfp36cOnk71BfYiyQW3DZ46dsJlRgdj5f7IS3U7h3Rxz4-ht7r7bIBbDbxHCjyXwLqhI5hoJirL7uimXHErYcyKxm-gQ1p4uedyeUdfVYYmyd2J6cE5HDV621IjajPaTYuppZLS4ISmRGw_LLT85pol5gQDXNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیگر نقش پسر والتر وایت در سریال بریکینگ بد، بر اثر خودکشی در ۳۴ سالگی درگذشت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/funhiphop/84760" target="_blank">📅 00:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84757">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ga5v2YzNvtyuarrCgQeTAujZGC8p5KH-3P3Pd1YmF5FZ5jfwgXpfunU2PF4dGQ2Dj0fkPDRuIrWye33o9voMImy51mbZrgX5QOs3ZR4tHyd4u6IlUTXiuNXXB0G8xzd72LWmkuWRWo3Fyd3qZ8j7ILivdxOfMxQXq8WKO4DqzK6OLXb3_d7amwxgDO4gX1Gylkj6wBKN1ghNb8cXz-ZLA26RvJNDgXZiOBOCPxweMrc3estyb-LHp88yyDJB4RXt5l7TuAM_dj5CQfb6gARD_OgShEjKOeN5okA3WpkoC0kL2XVOnLiRar8avpjmgiqWsem2h5Tmd9PMh_JawSKPrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داشتم زیر استرس جون میدادم حاجی</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/84757" target="_blank">📅 23:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84756">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFcYqhrQzHGzjyPL5E4G7L5gszpDW1gpgwg5obs414H8TF34_TIQtLYIydPHz14NQgHQloS5kfsZDH3B3rG6P3kCepnbHtRmhsa83VyvGnLi3BUjytZjuFpoEv2DEVXYqS1KM0BPNRGKh7uqWUj1y6tHH1LfE5QJ7rJVpVEYul9R8Aqc0KVn986Y7rArTIZts6DJFo9hHocRsHB09Y0d_M2j9_2dKcLw41jY0IroIw7siWB0FSirAdSFAeVfNoO7hFnDtYOktqwm-9BGbmW7Iu_vhhzE4pbtJsyfzK4sYwLys8jTgTrziYOv6WmRVOxiISU8ovRG0shsuj16SPwFuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید فدایی و شاپور و رفیقشون ارین بختیاری
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/84756" target="_blank">📅 23:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84755">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">حبیب کیرتو بخورم</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/84755" target="_blank">📅 23:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84754">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJYkBMJmIgDNoo5rwZZ4O4EO1B2oTEgQK9i6aboZ_EPd93q6XunOyFIckdE4YXl7YIpjbkIrE3nvMUqHWIStCZ6eW1IfPi8sGkG7zh2WcwVqJKt5FjLTKqpehQZBlIUtU2sQPmjowsCPR6S_j6uTF_WkCnTnQ5pojVGg5Hj2c6KanwLofJNI1Cy2El0hKeJEZiBNNYCwk8NWll4uXUm0z3U28BROmsq9OQfyXmqW3tvrQuUYBL3lncScI_CrcsRJKd_2YwzkCyyZTtYjyzetzFHVmlvSm66sv5uIHYGi16Ex9butLJZsYfvftqFRg7FHvB1T1iCKkBcWfaPtliqCoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیافه رو
😂
😂</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/84754" target="_blank">📅 23:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84751">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">هنوزم نمیتونم درک کنم چرا هلدینگ دو میلیون دلار داد این سعید دالگخیزان رو بخره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/84751" target="_blank">📅 23:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84750">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zz3wQ_1J6KT_1g19Cmj5zITNENZg5ZsfHgfqiwJwu56rcbbzG20hSG4GkhdnpjSwJg1JY23a2Xezee7E9G3s8XI76Du2J2Rgz6DrCWjAPmq3GxPd3AzVlsRtdE6SeZJ3xANbW7zYWXuYt--cT-djK_SJxB4QUiBIm2kwQxRNN6Xm-eDiRTMiKmiJo7FtpLwQn6M0Euqoj4FBioeh0emN3Eg4iOLd65LJVRSx4EOkhU3uaavEBnpezWMW1VvwjhuV4yGvVBGG3u0adYAcD1DkS2I3smZKuaos3bkuMdIasf5ENKTXIiGC--XzHyM2ouuLwDXIgHDQjHX-G0qFBZq4vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین روزاس اسرائیل فک کنه یاسر آسانی لانچره بزنتش.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/84750" target="_blank">📅 22:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84749">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">همین روزاس اسرائیل فک کنه یاسر آسانی لانچره بزنتش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/84749" target="_blank">📅 22:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84746">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940390f975.mp4?token=BaSAJ9mc9wbE79vFyiFX0m8tnM0YBO93HhKLt6edDCCp0yn38doxFNiyQGd_e3_r3RANYPDB0iXzIr1YiwO9S_kbiEbhIkg8zFrfzLD3WbqsBI24euCrhba6oWOuq-VI3pDfRRgTRbn7G9Wjtq2j4lYtLltvPutmAFWwUksJ-TnCEXfTczKxEK-J7LoxrrLkKmU8q84affknAjXKclubXRfpIccmYWLbh44nuTKf7INPpEuHon8nMCnLJMKxIxXgCwfWaFreXDWq4DLDXYGvQVx1wfLZtjM2JFCHXslpEdkelNzaHOpryrPrYnJNFd2DCZzrfUEP1racl2TYqenstg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940390f975.mp4?token=BaSAJ9mc9wbE79vFyiFX0m8tnM0YBO93HhKLt6edDCCp0yn38doxFNiyQGd_e3_r3RANYPDB0iXzIr1YiwO9S_kbiEbhIkg8zFrfzLD3WbqsBI24euCrhba6oWOuq-VI3pDfRRgTRbn7G9Wjtq2j4lYtLltvPutmAFWwUksJ-TnCEXfTczKxEK-J7LoxrrLkKmU8q84affknAjXKclubXRfpIccmYWLbh44nuTKf7INPpEuHon8nMCnLJMKxIxXgCwfWaFreXDWq4DLDXYGvQVx1wfLZtjM2JFCHXslpEdkelNzaHOpryrPrYnJNFd2DCZzrfUEP1racl2TYqenstg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/84746" target="_blank">📅 22:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84745">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c170193b1b.mp4?token=peoEERAfZu-aMCsX-zW-VJtlsMAotbhjlIqSRaCnUOnXJtEOPdVe41UZbGY8Sc9c3g8lDxiLFuQ8Y0AdYlgg_4F6T9DeTWBTA-p6eg4mFKRoWnhxYN5uOd4G0tp7MMa5z_2ZjbSgfOQAktYdxEPEd8FxF2UBqTIG2JOtL3gzecUxL42CuYWFpIdjqG-sZsWQvo37QXd32bWCvC-EPxLXBrEd5hg1Cc8Pp79G8pEEfOOHk4NijuXreX2UOU5iyxaIVq_qFTWiEzHinZK-V0mt3nzMPa02ZKO3wIA26y1UMrn3YJOEjBzI7Hzc1rn-4sFjAxdVY2Ol652yK1HTK6q3Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c170193b1b.mp4?token=peoEERAfZu-aMCsX-zW-VJtlsMAotbhjlIqSRaCnUOnXJtEOPdVe41UZbGY8Sc9c3g8lDxiLFuQ8Y0AdYlgg_4F6T9DeTWBTA-p6eg4mFKRoWnhxYN5uOd4G0tp7MMa5z_2ZjbSgfOQAktYdxEPEd8FxF2UBqTIG2JOtL3gzecUxL42CuYWFpIdjqG-sZsWQvo37QXd32bWCvC-EPxLXBrEd5hg1Cc8Pp79G8pEEfOOHk4NijuXreX2UOU5iyxaIVq_qFTWiEzHinZK-V0mt3nzMPa02ZKO3wIA26y1UMrn3YJOEjBzI7Hzc1rn-4sFjAxdVY2Ol652yK1HTK6q3Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی النصر بخاطر آژیر خط امنیتی (احتمال حمله حوثی ها به ریاض) به تعویق افتاد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84745" target="_blank">📅 22:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84744">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بازی پرسپولیس الهلال بخاطر حملات موشکی حوثی های یمن به عربستان لغو شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/84744" target="_blank">📅 22:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84743">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ناموسا آسانی حقش لیگ ایران نیست</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/84743" target="_blank">📅 22:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84740">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">استقلال یه بازیکن داره اسمش احمدی عه، یه بازی قبل دربی رفت سال پیش مصدوم شد، ساپینتو میگفت به دربی میرسه، یسال گذشته هنوز مصدومه</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/84740" target="_blank">📅 22:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84737">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">آسانی نیست استقلال در سطح تیم سالن بچه محلای ما بازی میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/84737" target="_blank">📅 22:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84735">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بازی استقلال تو آسیا شروع شد...
گزارش لایو با چاقال اسپورت
🤣
🤣
👇
@Chaghalsport</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/84735" target="_blank">📅 21:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84734">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJXZowGLrvvBV92_xEg6D_LEsEi_w26L3mCvJ5SO4fpM9DBQb4puXS5oK6PkdHDfU6g6OmOFy_KMqyCo0D4GFvccTCuBqLGqv1LISKTI6FqZ2EeMNpVmOhcotrUVBKVdNGxMJ7LiK81k6nPvrVWAFwZT-mEZr1v-KAYfVH2jMoznNH-0NeA1bNlIQ_3KMf3FMrj0PPWCalJi6tvuowYWVtoOcmhVOxz1Yij_cCCtmjbQHsCXITVFG41eMMMkY4WIxgP8Pfd0IGsTkBLkAD7ukgEdzZMBdWHRQmPopI7qkyaTyv-nsLsbIiHmLAUXn7JO-hUVNySJCZ1-jXAEXl2Nig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب پرسپولیس برای بازی امشبش جلو النصر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84734" target="_blank">📅 21:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84733">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bff24e8c4.mp4?token=H1EwOoRSYcKr8HNplnJPpRS5BRWH6xRQeAjyMVNzR8FMM7TtXUGLWmDjYzu-XNF8R73Pc7B689DxlbgVcqZQFCsxNGDl70acBx5Y7xKJlOn3RAhWSAqYmqdCyJ6EMo_-lyXnmj_F7hBg6r9Z4TcthRe-A09tgrLy9OQu3B-74CkPRuMzFJY9fHeTiXIl22mX5OPc-CbmdWJpszZWyIK9MbAZC4xkk1zVLg-Ebjsf4EF7XeF9MdylF8YsKqPr285y5mLz9S1E2i5RR5Mzt3TZ6VhQQUJBs3FHhI6FCibWpTkaTPTDYJwDi1dECyXU6qbF4ye1KTAVU7KnPNnybpN6kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bff24e8c4.mp4?token=H1EwOoRSYcKr8HNplnJPpRS5BRWH6xRQeAjyMVNzR8FMM7TtXUGLWmDjYzu-XNF8R73Pc7B689DxlbgVcqZQFCsxNGDl70acBx5Y7xKJlOn3RAhWSAqYmqdCyJ6EMo_-lyXnmj_F7hBg6r9Z4TcthRe-A09tgrLy9OQu3B-74CkPRuMzFJY9fHeTiXIl22mX5OPc-CbmdWJpszZWyIK9MbAZC4xkk1zVLg-Ebjsf4EF7XeF9MdylF8YsKqPr285y5mLz9S1E2i5RR5Mzt3TZ6VhQQUJBs3FHhI6FCibWpTkaTPTDYJwDi1dECyXU6qbF4ye1KTAVU7KnPNnybpN6kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقا چیکارش دارید خودش دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/84733" target="_blank">📅 21:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84732">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">هالند راجب شایعات سقوط منچسترسیتی و جدا شدنش از سیتی: خب اگه سیتی سقوط کنه مسی باید نگران بشه، چون من برم چمپیونشیپ رکورد ۹۲ گل تو یسالش تو خطر میفته.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/84732" target="_blank">📅 20:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84731">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh_NPMb_8N9fQqOKWZzddb59pBVULU_16tc_I8i9AQREwK9lxEuZD7AW8vAmDlJ2AIbggroGoNtUl1UN_hPl780CqgyMqjRoKA-GoA4-WAgq0j_L7cd29CRiB6zqAfr-nGRZFGkhmtWdozqVZVmPa52K71mPBoPcDmm_1o-MmteGu4WOeUrCdV9FHgj8D15Ua8FxWFBICiVsCT0OGBIdt1YZ3Aa6eam_LLOkmirhHcxMF3xUHCRn4alsIg0GSbUbJT4TyNnvERj1YIsWaDiO1A_TQF_UT-7fc4p6DVzBe23mVZZqaBP0kZNDm50pIoswmUb9jP8voChLGXFLQWSsaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران رتبه ۴۵۹ بهترین شهرای جهان رو با کمال شایستگی کسب کرد‌
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/84731" target="_blank">📅 20:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84730">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eecaea14fc.mp4?token=Dsr0gcNNCd6qudLi4x4F83Fb2R2LMMLM1wjTAxg_DlCx9yISAPqSyVJu11fgE1gpaIErMsV0GAHE75bCqHdn09aMSNdrcK2lrSBEaMGvUt4Kpir2sr_GRy_GF4ZLwh4i5-Ys764HTdEdzi8GATJ_lbhbo5H2jkGEerPR7Xizey-k4pKLEzU6AUH6z6wcpbMFDOHSmJ11AY4MBXU5DrxzYnC78Y296Kb7sZnKcnfYCI-azdaURFGAUwdaMxJWq1hQwo0FsPKuaoYOwiCxXXvBIQaRzoiBsvZV1R6uSkJXcUTM73KgtPexTsfbhd3yoJ--DSQak27JMdgvR4GTCfocLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eecaea14fc.mp4?token=Dsr0gcNNCd6qudLi4x4F83Fb2R2LMMLM1wjTAxg_DlCx9yISAPqSyVJu11fgE1gpaIErMsV0GAHE75bCqHdn09aMSNdrcK2lrSBEaMGvUt4Kpir2sr_GRy_GF4ZLwh4i5-Ys764HTdEdzi8GATJ_lbhbo5H2jkGEerPR7Xizey-k4pKLEzU6AUH6z6wcpbMFDOHSmJ11AY4MBXU5DrxzYnC78Y296Kb7sZnKcnfYCI-azdaURFGAUwdaMxJWq1hQwo0FsPKuaoYOwiCxXXvBIQaRzoiBsvZV1R6uSkJXcUTM73KgtPexTsfbhd3yoJ--DSQak27JMdgvR4GTCfocLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فک کن برا ۲۵ تومن حقوق مجبور باشی بری تو باغ وحش درس بدی، معلما واقعا بدبختن حاجی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/84730" target="_blank">📅 19:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84729">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ujy6T--S7my6Wz4Qm3QxrXbUX4Jr_9RUfKh-X-KoPQVt36L_QxfVlaNHLIxFj9QwUx8_6Icn5EMSkBIeUIjRLcjoz07qYJCrobyqBfAGJnC64uhVDgTQxqzGOOSxzZa_NsYPc21DOWNbcsvBkZnO9ubTnvcQAXjUYLCoxHRDE-bhgDlIPpw0KV-l7cYeXY_UsrNiv43KMt1SeH5Fb-Z2cLBm1cPS70ePGdaNaYN3qKL8K0RPG9TNZPS20V6les5hjoo4d9BBV2RfC6nQ8Mmlg2AgLUJOQOIqQV0-nEnHbuOUOZW0sD4NhNa6v6Q2zLAHPQ5LrBC-x4E-0ZEcMUpN7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G20
🅰
🛒
ورود به سایت
👇
✅
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/84729" target="_blank">📅 19:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84728">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">شاهین نجفی میخواد بیاد استانبول، دسترسی بهش راحت تره لطفا با راکت بزنیدش</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/84728" target="_blank">📅 19:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84727">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نخست‌وزیر بریتانیا: حمله به پایگاه RAF فیرفورد تقریبا به‌طور قطع به دستور سپاه پاسداران انجام شده است.
اندی برنهام اعلام کرد:
«می‌توانم تایید کنم که ارزیابی ما نشان می‌دهد این اقدام به احتمال بسیار زیاد در ایران هماهنگ شده و تقریبا به‌طور قطع به دستور سپاه پاسداران انقلاب اسلامی انجام شده است.
ما چنین تهدیدهایی در خاک خود را تحمل نخواهیم کرد. با استفاده جمهوری اسلامی از شبکه‌های مجرمانه مقابله خواهیم کرد و از تمام اختیارات خود برای هدف قرار دادن این شبکه‌ها و منابع مالی آنها استفاده می‌کنیم.
تحریم‌های بیشتری اعمال خواهیم کرد تا توانایی جمهوری اسلامی و سپاه پاسداران برای آسیب رساندن به ما را محدود کنیم.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84727" target="_blank">📅 18:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84726">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شین: پرتاب دو موشک بالستیک از یزد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84726" target="_blank">📅 17:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84724">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jasm4MYJdCHBQsBArMuIj7tuMZZyTdhuH1pkowlbGJbzVPDFfG9aaafKrcV9x5bae8Czmb0OxxNDLQfLnkm6vEcEM26zzD0h3BjAjqfZrT_iPsoc8cjv4Mkei6cnXsIxVNykYcEtfL5f810qiwPz_zWvpBdB80_5p1vcI3pHRmeJjbkzrQ5t-9r0qteqDg7nHKpQgN4gGQTojpRXJLicE5Cg-xpXmwsO5AD0cNAI6YB67aQw3sDEurzza0mtyjTqwLsSCUBuhpRQK_yXMsTfEYBp7kuxU4oRZuxRzkuM-KNpn7GPZKNfI5vAC-h2EsUBZL9Bi44IqucCsZP--g4hAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PDOkeUveuNlD3jrtqM6AgyrXtHeSpev19l-knoA54vfvQvLeOkRoxS1DJ8zLRjRAY6fI03O9xdb-luMkRvawGfTDoADhDbdAaaR_xmwmxuCCMPerS5D0BidvA0dlkJ-qUanNF2WfIo-qfVayMWvs-Xxp5aDo3_1QJ-zXPW7jwC6vt3u9rGSpm85mYOLKFA8G6bq7xuClDuTDaZBdCSitc1dwMDmH9ruzsJvp6aelnCgyqtBf0gRHMgehlwBaIi-MMfEZ6x0Ww8WOvyPQUmAloAoV_DmjA4lTdbTb9pyecKB1pIrm-RR0fuVXb2Y2tfvth1G52m9jha0YPzqtf30FkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتانیاهو لایو گذاشته داره راجب انتخابات حرف میزنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84724" target="_blank">📅 16:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84723">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ca73243e.mp4?token=odl9LF0ucOKSedDhDJ6EcNc17g_S3tkQOafMlaZ3o98wGQg1SWwGAKmHNNuW1ZdD09YrUpA0yqNYpCMCT011yjC0a99-wwzWsFlPpM5p2B_XU8wa7Eq5TQdRt_1An-vJ-Gwi-O-x7N41WPOFSCLPYv2KJG6H3ZzwdsrdVA-WS6wnaalMV_7eQclEqYuXo-cKcJkXfoRpZYBbBffP0eBNPYAh7LNIzH480jIkndmDbOup8eU61_NahmaGT4WkvV7lZPZ-MUOXZIPqFOSd5tEDntpoiybAeXrM9uP89iczkmu9GH7P7J-saAd7NUMGYUe0TrD8Li6hWdlYyCzmV19vbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ca73243e.mp4?token=odl9LF0ucOKSedDhDJ6EcNc17g_S3tkQOafMlaZ3o98wGQg1SWwGAKmHNNuW1ZdD09YrUpA0yqNYpCMCT011yjC0a99-wwzWsFlPpM5p2B_XU8wa7Eq5TQdRt_1An-vJ-Gwi-O-x7N41WPOFSCLPYv2KJG6H3ZzwdsrdVA-WS6wnaalMV_7eQclEqYuXo-cKcJkXfoRpZYBbBffP0eBNPYAh7LNIzH480jIkndmDbOup8eU61_NahmaGT4WkvV7lZPZ-MUOXZIPqFOSd5tEDntpoiybAeXrM9uP89iczkmu9GH7P7J-saAd7NUMGYUe0TrD8Li6hWdlYyCzmV19vbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ی نفر تو ارومیه اومده واسه ی مسیر نزدیک اسنپ بگیره بعد اسنپ رفته بخاطر ۱۰۰ هزارتومن یه راننده از ساری فرستاده، راننده و مسافر هر دو پشماشون ریخته:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84723" target="_blank">📅 16:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84722">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RouOSpv5BeQ3oK5jcUgWQSahhb-6JiNJ3QowAz8mW94GCYJm9JBuKOvNXJaLNbNIs1F7rNDwrF6Wj4p9Ooy5PPGmw3ZU648EoTI4IX9yBr4g9r8cZfzYydxkNgT89R14tn-BtC20pQ1MMAH5kaQGPVWcg8B2Ho2pE2Ej9mg22iP1NXyj4pyOs2NO227Yz1ozaKFItAib45z8aJQiHhElr_yHXfjiPxmSKgm4uFSKaQ0UdY1VpC1CJtSj4dRW83EyYH8lV-_awf6X_CtA2-Wrfm8JOEEzsbJPgyFipUWUGVydjEv_CT-PFHG-WipvXsFhUfcZHT3S20kIsnRaFRukFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو لایو گذاشته داره راجب انتخابات حرف میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84722" target="_blank">📅 15:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84721">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/479ab143f8.mp4?token=husiemTfQGbdjJMVUpiNAKeYQCdHzJuW7NZaKqN2ZPusY27DqXA97ATBwo2AkGamLexC4JFFyq6xsbj6sNtc3gD4gbLhOUFuFZO65hj5PW2Jb7Zv24QNYGd7ccVjJG-L8C8qms17X7H-lKMOPazsilfWpv3YdEg7omIkWNcluF5xeCrhwyecxQTW7Wtb1pBn9Vk4TWAIcp0wHTZmA0N7Dqi3X6DgiQM2B8GWLmcmztKVC4N7HQ48S3u_GVYK9TGdIwJIOzzIS9l1eVzZKvMXHmjzdzbH_SFK1T-OYF1F-cmTzVGdXxaKBADTjjgCXytUFEF1Ki6_356eWpJ1fqra0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/479ab143f8.mp4?token=husiemTfQGbdjJMVUpiNAKeYQCdHzJuW7NZaKqN2ZPusY27DqXA97ATBwo2AkGamLexC4JFFyq6xsbj6sNtc3gD4gbLhOUFuFZO65hj5PW2Jb7Zv24QNYGd7ccVjJG-L8C8qms17X7H-lKMOPazsilfWpv3YdEg7omIkWNcluF5xeCrhwyecxQTW7Wtb1pBn9Vk4TWAIcp0wHTZmA0N7Dqi3X6DgiQM2B8GWLmcmztKVC4N7HQ48S3u_GVYK9TGdIwJIOzzIS9l1eVzZKvMXHmjzdzbH_SFK1T-OYF1F-cmTzVGdXxaKBADTjjgCXytUFEF1Ki6_356eWpJ1fqra0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمرین حرفه ای کماندو ها و نوپو تو سنندج
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84721" target="_blank">📅 13:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84720">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نظام‌وظیفه با درخواست کمیسیون پزشکی علیرضا بیرانوند مخالفت کرد و این بازیکن از اول آبان‌ماه باید به سربازی اعزام‌شود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84720" target="_blank">📅 12:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84719">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پزشکیان : داریم در تهران آب زیرزمینی را استفاده می‌کنیم و اگر تهران هم با همین روند رشد کند از کجا باید آب بیاوریم؟ باید برای حل این موضوعات چاره‌ اندیشی کنیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84719" target="_blank">📅 11:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84718">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUvbrH2bpp22UR4bdfrKGYN9nIpy_wnhTe71zO17u91oBcdIdApXWCs9H7yP20JyMPhsCatxk3Qfze6YItXp98V9--Muy7Xq5YeDEISTpGajmDnw_mRzetJ2B3DGW8F8X5s7DiP27RSj9rpIymj9Uzq7-m6MTsTNHwagrfCTgJdoR6g9-T49D143IU0ZSdGJUiBSgdafPZjxIU8kCuZjo_1QgoBTWRo0EzlOj6Td4eFmJudmKwbHrel9mC_tVGKezQyukZxVRi77Dzj2vaG_5XZRsYumnxiR--DwmsC2X7fjBcdw9nfstgbYEw0rYkkjsxLBm-YsXwGSCMp4XKMaLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭
😭
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84718" target="_blank">📅 11:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84717">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abc4e72c98.mp4?token=u2fxY8mhKR7E6Pz419A10YhFmSCzBrBxSsfc_IwEw2vAK90KmeB0BFTo4xGlM16XtyYJ8N9bl8xjDyByu6Y2yLvR5KDL5HqCZC6qItSt3J_mYqpbI1rRCdygOdztCVdP99PN9v1vkJncCK8mhexHPy1lYLuPJUxUYJnnIxuBPd5_XLTcSr3gbDXkSnW0l9wODaYsugVHYAaYMfdN6PSgN_vY5v2PPb9MkBtJR8OphVLPHGFrO5kFUIfP7w1I_SsONVNnsPXEtcbrnw6lOSjpM6BWW-F1luWVI_OLyJY2WYPaECVNynIAfsIXXVvYCuWvsIe7HcwQRchL4Xt047BFTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abc4e72c98.mp4?token=u2fxY8mhKR7E6Pz419A10YhFmSCzBrBxSsfc_IwEw2vAK90KmeB0BFTo4xGlM16XtyYJ8N9bl8xjDyByu6Y2yLvR5KDL5HqCZC6qItSt3J_mYqpbI1rRCdygOdztCVdP99PN9v1vkJncCK8mhexHPy1lYLuPJUxUYJnnIxuBPd5_XLTcSr3gbDXkSnW0l9wODaYsugVHYAaYMfdN6PSgN_vY5v2PPb9MkBtJR8OphVLPHGFrO5kFUIfP7w1I_SsONVNnsPXEtcbrnw6lOSjpM6BWW-F1luWVI_OLyJY2WYPaECVNynIAfsIXXVvYCuWvsIe7HcwQRchL4Xt047BFTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره دختر اومد تو اکسپلورم باورم نمیشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84717" target="_blank">📅 10:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84716">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84716" target="_blank">📅 10:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84715">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXBzhBMZeTTYfhsvLcLvpIKiMTOtNG5pfVCs4DamKb8zMaRi6V7coXFn_ZTYr0hp1y7twAXFgUx4hkSuLjNmxHr3b2QLzBHm1rAIYVE8wtDzAwX_ekGRLDLwvRyKowNUaTg_VnKENN4IQpaztft8tRE55uBaRKWEbj-oNawdDyqxIU97LiaevfJtOlj0cjYxjFWsR1EQRKOnjdEdumHisUzzRfJXZfhw7LegMGZe84iRPgc6p05kb5_IuqrRvf9KPqfiqiCa7IyA_EZJ3OK6n4fnCtuhk3QyJxf3XKfSCp6E_HyVZ3H1tSNXWH6dSKpkp_Qa_oFkmjBvaCbnEroiSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
الغرافه  - استقلال
🌎
ساعت ۲۱:۴۵
⚽️
تراکتور  - الشمال
🌎
ساعت ۱۹:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r20
🔗
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84715" target="_blank">📅 10:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84714">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/408b52a61f.mp4?token=onzG9_gy3WrFe42wZZsod0xRxla83PfFJf8jMcRIz7XnGS3UJbc2yx0iFPmzzXrkCntvhlVARqptipXNnCKcrv1uvP59dSAbPJH6_oSKESfbWnWmrjOe8T5RHExNVwkjOrTsotSUkPEpxU4-YcDuKykoQiJUEipoMEppAF7gGReUGbc2I8iUzH449akN0GYnbMXHqRl_5evCT1AjeLMy15VaXU86fxGnVSdxrU43kBDEzZ8K_vhWdBAMa3xKnmJuCgUKl37xwkAt9PCLTc5ClNiJVqEJnyBBA-AeGrXyVy2NqJas7WLpzJuCxzbLECnE_wbhnVAnRVr2ufsB9fQXCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/408b52a61f.mp4?token=onzG9_gy3WrFe42wZZsod0xRxla83PfFJf8jMcRIz7XnGS3UJbc2yx0iFPmzzXrkCntvhlVARqptipXNnCKcrv1uvP59dSAbPJH6_oSKESfbWnWmrjOe8T5RHExNVwkjOrTsotSUkPEpxU4-YcDuKykoQiJUEipoMEppAF7gGReUGbc2I8iUzH449akN0GYnbMXHqRl_5evCT1AjeLMy15VaXU86fxGnVSdxrU43kBDEzZ8K_vhWdBAMa3xKnmJuCgUKl37xwkAt9PCLTc5ClNiJVqEJnyBBA-AeGrXyVy2NqJas7WLpzJuCxzbLECnE_wbhnVAnRVr2ufsB9fQXCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرار دعوای دخترای دهه نودی بخاطر یه پسر
انگار یه دختری به دوست پسر یه دختر خانوم دیگه تو اینستاگرام ریکوئست داده و همین باعث ناراحتیش شده.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84714" target="_blank">📅 10:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84713">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">روسیه حرف ترامپو به چپشم نگرفت و به نیروگاه برق خارکیف اوکراین حمله کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84713" target="_blank">📅 01:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84712">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">به رضا پیشرو ميگن: از مسافرت برامون چی آوردی؟ ميگه: تشريف.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/84712" target="_blank">📅 01:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84711">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بچه‌ رضا پیشرو یک ماه دیر به دنیا میاد، ازش اجاره میگیره.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/84711" target="_blank">📅 00:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84710">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دسسسسسخوش و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/84710" target="_blank">📅 23:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84709">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROOmvkGpO2SgjkNt5_t93kaEpS_YiU0mrbuP2-oYPU7COsh_GRG1QzdZcscojFvgYTOT2xtpmDwJaVECYLacN3r03dc1iRSjPeNW4dTRhPo_OmHqOmyNZZzf4Zbxp4r8CfIIPkiLkC07HD083xugJHB1wPvqFPvUXk9c892jHAsRTN_U0wb_BtkRqLK6rdrhKzUIFlKwqSMEULMjOrHVeRrHZ6x-vFAy5yjfx4FLKHVq7ybxR7lkUG3auSISkyPidJbrhEkrOYA557uh-J_Ol-_aUtP3JUHZA3UuJQUfv5x07ma0iOrG5aoN4e5EVrnPkleszpayaBCkPJtKplTekQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان First blood از اینجا اومد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/84709" target="_blank">📅 23:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84708">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تا دیروز هر روز صبح میرفتم سایت چک میکردم بلیط بازی بارسا و گالاتا رو بخرم یه امروز چک نکردم کسکشا تصمیم گرفتن بفروشن و تموم شده</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/84708" target="_blank">📅 21:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84707">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تا دیروز هر روز صبح میرفتم سایت چک میکردم بلیط بازی بارسا و گالاتا رو بخرم یه امروز چک نکردم کسکشا تصمیم گرفتن بفروشن و تموم شده</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/84707" target="_blank">📅 21:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84706">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خاطرات وینی پرایم داره برا ارائوخو زنده میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/84706" target="_blank">📅 20:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84705">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دوکو خداسسسسسسسسس</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84705" target="_blank">📅 20:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84704">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WG5_2-kytq92rAymZQNfCHOu57mBgthPP1fJe8sl4JBH7nmyIb2FH5jaBEKmynm9yDF6cvp-fxPk37VwOtPehLkLbp54f0cZOgZjIeTo-negH3MMAkNyt1UvB_1lvaFHQedrfsUK9EC4sQ50qQd8XQGWZWJphCtrnVZ_vMyVom3kc0dPGaqzpX3fF0ShZoSHxVDOan4HmMp_LakLDq6lpV5OsaG6ILKUDa8rNa_ZwQMhnIFAAbuHG8r4FhJX2KdH-Fm0S2K9gUkfQeK-AeCNbVojErU37fICnNORA--CUgMah72LiqqfG8dZW9BEiLJ5t_h9J0612dWK5OpVu-FAeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه سخنان شگفتی به زبان  می‌رانی، ای مرد؟
❌
چی کصشر میگی کصخل
✅
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/84704" target="_blank">📅 20:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84703">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd2361427.mp4?token=cnGcICsuBWHAYLHYc4dOARmGZLxIcmbB_ZbROmgZT56J0qJjgNQV9zKhu_4C5cotwOHzIxi3pQXJJD6Fa9iU-uUl7VDQCZxTQs-dN3gKARiXukDHnAxJ2miNBZ8tCyoDK4tl-X1bbuariV35Az1izYJ7Y3IqS6NiUC6LXYbxVVQdua0MAqVap2cFJbtqyG0rdcKiX-DH76Zr-T9IgXt7-UscLnLSw8U2X-KemGO_tOeiV64-BIBfsC_LZXnwO2aV8AEXqEwJUBv0LZXE64ZBAowUi_jLAi9OH8UW_UZ4xNnD3XfG7aN-NXIulswdr8IFKop5cUlQ-JZvcDQrBpdGApLsuMUVYgJEEPEUXFQM6LUnkVv204SK-TopO1ERWguTr7hMkyQGPkKQOadssOSjnQ8H2gxasxJ-nsNFRfkqyCb_B1el-GjwJ5wrS2KHF0WZ6J9Ylk99ILyuYYOpW7FfJ2Mo-g-CY6PPKdjzKLH5fpS_vBrlF67dFm1xEkHREJAc3SulZltNrBfJ-7RdYI0fYtTTW9zGzrjj1AhB8vSNsDhg9weZViBxHdQfPV-eUKTI2FTzgYNFRcCJtkK4VOkFXyRQUGDowKuAcfEu8UU0Np1KDEiWxyWqCrFhjoRlQJO9FySpkP41x-me-emtFb1Y9QZwy79mBRlgRPlbJCm3POI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd2361427.mp4?token=cnGcICsuBWHAYLHYc4dOARmGZLxIcmbB_ZbROmgZT56J0qJjgNQV9zKhu_4C5cotwOHzIxi3pQXJJD6Fa9iU-uUl7VDQCZxTQs-dN3gKARiXukDHnAxJ2miNBZ8tCyoDK4tl-X1bbuariV35Az1izYJ7Y3IqS6NiUC6LXYbxVVQdua0MAqVap2cFJbtqyG0rdcKiX-DH76Zr-T9IgXt7-UscLnLSw8U2X-KemGO_tOeiV64-BIBfsC_LZXnwO2aV8AEXqEwJUBv0LZXE64ZBAowUi_jLAi9OH8UW_UZ4xNnD3XfG7aN-NXIulswdr8IFKop5cUlQ-JZvcDQrBpdGApLsuMUVYgJEEPEUXFQM6LUnkVv204SK-TopO1ERWguTr7hMkyQGPkKQOadssOSjnQ8H2gxasxJ-nsNFRfkqyCb_B1el-GjwJ5wrS2KHF0WZ6J9Ylk99ILyuYYOpW7FfJ2Mo-g-CY6PPKdjzKLH5fpS_vBrlF67dFm1xEkHREJAc3SulZltNrBfJ-7RdYI0fYtTTW9zGzrjj1AhB8vSNsDhg9weZViBxHdQfPV-eUKTI2FTzgYNFRcCJtkK4VOkFXyRQUGDowKuAcfEu8UU0Np1KDEiWxyWqCrFhjoRlQJO9FySpkP41x-me-emtFb1Y9QZwy79mBRlgRPlbJCm3POI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تورنمنت پاییزی بری بت؛
5️⃣
🔣
1️⃣
میلیارد تومان جایزه!
💞
🃏
پاییز رو با یک رقابت داغ در
کازینوی
زنده
Creedroomz
شروع کن!
🎰
🎁
هر هفته
0️⃣
5️⃣
7️⃣
میلیون تومان جایزه نقدی
🧭
۱ تا ۱۵ اکتبر
🏆
جایزه برای
۵۰ نفر برتر
⭐️
هرچه
گردش مالی
بیشتر، امتیاز بیشتر!
💝
بازی کن، امتیاز بگیر و برای جایزه‌های پاییزی رقابت کن!
🎉
📱
ورود به سایت
👇
📱
https://ieoruyxtsud.shop/fa/affiliates/?btag=914641_l303106
📱
کانال رسمی ما در تلگرام
👇
🅰
g19
📱
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/funhiphop/84703" target="_blank">📅 20:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84702">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGoY8DYfT6zU_dc3uaEJintv6CFDcxDmu9J8yWQDYZDcwK9PbW0lUPqZYqrwyyuFDHwShyUY1iYjI9klpFEwqUQsEcB2Q1Xr3eynHsIs7l5t3s5TRt5E-yjVd7_geMvZK-94009DnIxXV7BDuJ8TbToaNVaQ5PVJaYhRKRbbNXodZu4uy6iV1Pw687nZUAWMB43s6K2HDZwFntN22_WK4tntT9dg_fTlRIEJnDCINbK3ynsS6djwBkynzKNtPmq0fddCk6m_vHDi2lbi9c05JKwFXicTLF14pG7vPWqIBUyd9fs_x1gVzdKB0mEbj9xPmoHRYhS_P7MT-7BblPAGWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو بابلسر ی کافه افتتاح شده که با پستونک به مشتریا نوشیدنی میده :
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84702" target="_blank">📅 19:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84700">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJPvbTMzVZK_Dq0cBcBUrg35t0uMf4svzCzqGCBNRM4s5E3bgmoeUsYWmM7o859u2gsE_v0RCoyildd4y0h_RODOklacd95ZiMJBI28dm42HidPoIo1I8ql4FORDwbcreh6bSnGAEayZCJoUZRcRmgIUZasqKGeZOghIHlYK9sJ4ulBN28wVbYpntoOuLQoa1GR6sj3bz7w_d3Sp15ENU0mSfyiw6h9uYPkLxh2F-I9gVnB4JCXEX-sYkE3jK8tIX3DmFSbtR0uomKClxDSNwDLkyw_QpHHdM7I36lXv_48Iq7neKWyc_ZQUay1BDIeyHm7y-8-6KJVP_nwx8Htk0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا به طرفدارا لیورپول صبر بده، حضرت ایوب هم نمیتونست همزمان مونیوز و بارکولا رو تحمل کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84700" target="_blank">📅 18:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84699">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XV7Mc2QlPZ8eSRbXajz0sSIdz9QOJ0TgdH3HYRBMEB09bRFMbO9jiV7YsHGfdisRn-PNmxxeE4iIClYJWsggwvAxbeh333QxCYSddMRvB4Gsa2F1OOQ2vlfSwEbAmUeVMAo7qYSKx06d4QvX2nVaRTjLZX7bR6yfJRq89hxpGkfyOrlpx8DxgfMcEV2Tn3xj7spf98TghCZfbbWjOoLnorfIEDgLgN1fg-G-w12kZ8yBUGHSGKswsLWVB0Apf9_ndcNC4-2AquNRW-okCIeMQcBrUHM4JM0XMx_mF0a-TcuSLw03MxjDfxcXw_Lq075WmL_fHHKckoFIS6cwwZ29tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیری که گل‌گهر برای رسیدن به بحرین رفته:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84699" target="_blank">📅 16:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84698">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dde88b838.mp4?token=TK5M1UtNl39Qqg8Nz4-h-o2VByKTuZcPER6Jwj1pi1XjAWD0QJd9z6yHsWkYUzZnWAHwjk9-OQoson7K94mpnUTf2SIv8UXuY6eyotQ7GSQPCPq7n82Xz-LTvk2Q78dvCOtUTr5IUM5HaZODlfi6cBZqkTwWaRoiq77TFChU-IfUd_-LhbszC0pnhAB-WD3EeJsr_e-LRm3m7w4y1oaR2dxm06aR1CpN020r18OnvoJCtHabg4GUm9-f-6SjJiD9YzXJrplYwNXjjhurbSVLYoTu1qUH9gy7Ye9_eVXWrHPUgtoA_ADZBPIKQobzs6QZf9PG1ksYYt9kFfnPQCCcsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dde88b838.mp4?token=TK5M1UtNl39Qqg8Nz4-h-o2VByKTuZcPER6Jwj1pi1XjAWD0QJd9z6yHsWkYUzZnWAHwjk9-OQoson7K94mpnUTf2SIv8UXuY6eyotQ7GSQPCPq7n82Xz-LTvk2Q78dvCOtUTr5IUM5HaZODlfi6cBZqkTwWaRoiq77TFChU-IfUd_-LhbszC0pnhAB-WD3EeJsr_e-LRm3m7w4y1oaR2dxm06aR1CpN020r18OnvoJCtHabg4GUm9-f-6SjJiD9YzXJrplYwNXjjhurbSVLYoTu1qUH9gy7Ye9_eVXWrHPUgtoA_ADZBPIKQobzs6QZf9PG1ksYYt9kFfnPQCCcsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقا ابوطالب یک رپرا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84698" target="_blank">📅 16:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84697">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دختر خانومای گل، روزتون مبارک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84697" target="_blank">📅 16:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84696">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mnd1Ev-aAjyZqW9p47oPNEjUV1pe_lzPkN6i8Yn-14RowVnDSEs_qLVlHg7Udu7uXOgDqjKSl81G8xz-HFX6WJn_HSnE0Q8b1hHFnj8z7qDrScPzTDH8UC6NSt9MgJgU56FlcKZYjBCwLyv59vn6RZNAvDPsyi2Ux0Q-d5LROKdSNV7u1S_N3ASrMo7qs1NPjx8lfJjVq-9EmpAzTZkbSji-tMTZ109uoPMjHCflzinP8lo9OnxPd2QiCEl4lL08LetcjIj6QZmVci6oUjqYmFSG8A8K7fQrBMBuw38Jk8MNF9EoMgydvw3ixINYsIOLLKgCYE7uOLzAPz-j4SogBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گراز پدرته کصکش، حرف دهنتو بفهم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84696" target="_blank">📅 15:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84694">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l37Hrjm81XuxXinl3zgK9dWcW7yn1ME0Nsfux1CGBImp9-E91eNkPYS9iSTTVYmMZad1ZIzSZ31EsBJF38AzNPzQKMMjoXQG6fMwGq70DlcADcFwPcg3w9hAt4gYKJYKVLlSt9siWg8BJ6ctgzwO0CorlJCDlEahSi2ADRTrGTCttK5LG3EHntJ41KMYMO7P2RLIiX_Dgng_pdbMUdk98HCmPnxTkmPUZyGgTlMAE46Q7ZUcSgEinRCksXxTBKD8RrN9SwnDnRlJb8QdQL6bocvnD7APCjFWH7BIcPWdmzehfgyArg7SkGDNcuFUd-S5rzkX7BIRnC6w11AOMXA1kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم یه سری رفتم موزه همینجوری تابلو راهنما رو با یه شاهکار هنری اشتباه گرفته بودم دیگه نرفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84694" target="_blank">📅 14:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84693">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">زلنسکی:
اوکراین آماده است تا حملات خود به پالایشگاه‌های نفت روسیه را متوقف کند، اگر روسیه نیز حملات خود به زیرساخت‌های انرژی ما را متوقف کند.
پ.ن: این ترامپ لامصب چیه که از یه راست افراطی مخالف مذاکره که کشورشو به کام جنگ با یه ابرقدرت کشونده همچین آدمی ساخته
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84693" target="_blank">📅 14:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84692">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/548dd7a29a.mp4?token=pQHbPWwlw_BfJti3pILzxBsi-hCd0GVZR9KSnS2Cu3RgMTPoJS71pHcHUYTFbo6WuG39yTcWY8peZSnyHBUeSRExCgkSj0NdaaOBetSfReGK0suZbvqbE3A10cpR6CASPJeMLpgXbBZeynfRzNV2FzzXrGysum0YUkpMMt69OUu0ij3y7wEZmrSRMRJYo0EUl_oJ1-Dnq96rpCkMrCcYKg0OwOrbTxO9_x7yu2psSYjGXFDFHRYzI1MwBfHWggVARgpuIK-L9YZaHnXfLykqZHDCrl0_vtHKYyK7OpAIJBq-ez8lZJejmLNAxO5HHUhrzG9jr_vaBKO5h_sr5Xz70w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/548dd7a29a.mp4?token=pQHbPWwlw_BfJti3pILzxBsi-hCd0GVZR9KSnS2Cu3RgMTPoJS71pHcHUYTFbo6WuG39yTcWY8peZSnyHBUeSRExCgkSj0NdaaOBetSfReGK0suZbvqbE3A10cpR6CASPJeMLpgXbBZeynfRzNV2FzzXrGysum0YUkpMMt69OUu0ij3y7wEZmrSRMRJYo0EUl_oJ1-Dnq96rpCkMrCcYKg0OwOrbTxO9_x7yu2psSYjGXFDFHRYzI1MwBfHWggVARgpuIK-L9YZaHnXfLykqZHDCrl0_vtHKYyK7OpAIJBq-ez8lZJejmLNAxO5HHUhrzG9jr_vaBKO5h_sr5Xz70w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنازم یه جوان فلسطینی که کشته شده بود بعد از به صدا درومدن آژیر خطر پاشد فرار کرد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84692" target="_blank">📅 13:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84691">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bcs7LfRlVQQ3TNZSpCsG07uyyiGACQTOR7GORjT9QKrOf17JZTqS52wanOSgqu7_gB2Ndjj7W3WhJFKVmrKU93xGA02E9lc483Qriw8LRafl6D_lcCGd7Kj4eMsXaoA5h1n2ugMbkooh9c3lvw1k3LQInMlx_bdP-Ot1fYlArCgbPH_JPMKQSBo0_H3sUvEiGHWwgql33nkqm6R7kabYH0gIypCc6jkC8U7P-Nb8Wxn2I6VJjco0xRGydHSF1sEczB6qgvwC0Xj5jZqDIN8y30-fUQswZd-ozkNDU-eJM3OaaT2ohdniTW-1QJkCwrD_tw8XdFq1jJocEiTaf82AvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گنگتون بالاست مشتی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84691" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84690">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84690" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84689">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvIO5IC5_qnyoPKmrgP4jykFQLcpkMeZaXjbmYKLWoBlHKbyS7PVa8teIZLyFqQAFmquU8kxOIFWwcM5Py9J1ReTQYUCnytyLAffJXes_AYvQ03JOzRCUdYIsWUxPh7GoJEUNGVtq1hRRUJHqJB4g54ro1TXPvk6fuyUlb9S7lAPSV69yfhYTjT4ORLeBM6KULlBA_-o6woJ9zBYzpvgBs77rQ6LKlxdMDAs8hypTx4CtM47Z0tTn_PSrWEygKLf8J5qj37PAH9fpE2FwpyCmUDP0Vtl703_mDUu0vhUAvtnKki8rpK8HHBZe9Q7OOgQcMUzRiPY0eeCPizmxCO-gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
لیورپول  - منچستر سیتی
🌎
ساعت ۱۹:۰۰
⚽️
هال سیتی  - اورتون
🌎
ساعت ۱۶:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r19
🔗
https://ieoruyxtsud.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84689" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84688">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZVABghdEWoKhQxGS08gFuY9g2HDJ6igvsyvJoHYNlGmaMXHa08QZ18OP_FzNi_BTG1WycPHwqVwpCg1zeaIoVaXbnLgwUfowjbtBQTbBD6wGE_QUrYQYqwGh2rXc0E0Qq29fhsXc044Y0-zkr4rzsAwN4nLo9mP_yc_h4WQks-o5Ot-HCR14IgE-LSkhzLlBkoMSzJGNQqU9rwRmCkm0ctyp98IpfvnnGyuJVJcMZeaC3sn9yLLBAt7_b-HGC6BsqcwNAhGD2iFXzafFgNi3g5VRNtFGZxXY8XZcee0Rcu5zv46EpuMLsBuZeulwSc6R0wpwWwWwYL5cD_tXLpDWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دم هرکی اینو ساخته گرم یه ماه بود از تهه دل نخندیده بودم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84688" target="_blank">📅 01:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84687">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJT1dODQ5dTWV9w0ryd3BWveJKpgK7-2EtqaGVb7cJgFhKEeKYigiNWmFaiU1M-TEw7b6-d0WhDQoOojYMxklawg7Ws9tc2R_V277sKJBB07zTv0Eem3h9f2z95-cCvQd2MEjmVIHpzxhSz8QYpckeE6QxTuWP6cQBljXEks8JfsjlaKFs9QYxF0O7l1oCA2FONQEvKriYZlpic1qL8l4jflZI9dhiXqm-JcKJQv3-gRqTQoymqExGBGThWxVyj3qKPYIrjLJtYMl7AaM0qmEzSvwEwgvUMlIHzdhN2wh7Ce03uDIBCpNPcamHE5dKIUZd-avGEeprnDe-CSRkpXtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیرم واس دلت دادا
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84687" target="_blank">📅 01:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84686">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">داور کسکش فقط به من کارت نداد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84686" target="_blank">📅 00:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84685">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b32a1ac263.mp4?token=IH5qzjVdh2vIm9H9NVbBcw_eSKuBYnotc5FTHSRiZCSB4J_L_pmaj67oN4cokEvJmNL_Y7Q_hv2DmgFkHobhtGJDHl_p8ohZc_DN310JDARl-Gjx0j9hdspctjvarfhPweOP5TnCzmb0qGOB2jtFvw-saFoZeFBhFeGwZrDpqIZnFQHpJth_zkpvJipH3aLpN-o8Or-w9LVRiDfBUPNRi38Ad4KoTD0RG7c6sUNnwzU56aoYoqKeo3-Z9NdSLeR-yJ3Pp5Vf4qZq7pkffzfhB-ewNXJKVq8cajLKw8mEUESgdEdzpjsQRqDnF_o9NOB2aw6UNFqeePUndc1gls1q6E4-t2S0nxI5PdTwlmhhngVbp7YIVb7f9jNEZ5SFLZDv6oM0W5iO7JOD7ngEVL-AbacS6qJihCm9uZNFcy6USdvybRrKrGqSWcYW2t6J8WFcCOVMXeOrkYvmWn3zvZNOrOlJPbtfezQihlolTo90d2CgxmcmhYTfconAT2zUKA8b8ocrQeQcvHEYFNehu7328aAwXf0iIguAsePklQuQ4VK6vFCueIiDfAn0xs2rO4ThdagEYhxRcMfujRMVI_IVOWGMp_pk7b1JSmi2IHrUTBivn5KIoxqMcD93YrfpjmoWa2DNvGfOFbqTidcF62VeA4YAuBqO2vxlwC7vbxTPz58" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b32a1ac263.mp4?token=IH5qzjVdh2vIm9H9NVbBcw_eSKuBYnotc5FTHSRiZCSB4J_L_pmaj67oN4cokEvJmNL_Y7Q_hv2DmgFkHobhtGJDHl_p8ohZc_DN310JDARl-Gjx0j9hdspctjvarfhPweOP5TnCzmb0qGOB2jtFvw-saFoZeFBhFeGwZrDpqIZnFQHpJth_zkpvJipH3aLpN-o8Or-w9LVRiDfBUPNRi38Ad4KoTD0RG7c6sUNnwzU56aoYoqKeo3-Z9NdSLeR-yJ3Pp5Vf4qZq7pkffzfhB-ewNXJKVq8cajLKw8mEUESgdEdzpjsQRqDnF_o9NOB2aw6UNFqeePUndc1gls1q6E4-t2S0nxI5PdTwlmhhngVbp7YIVb7f9jNEZ5SFLZDv6oM0W5iO7JOD7ngEVL-AbacS6qJihCm9uZNFcy6USdvybRrKrGqSWcYW2t6J8WFcCOVMXeOrkYvmWn3zvZNOrOlJPbtfezQihlolTo90d2CgxmcmhYTfconAT2zUKA8b8ocrQeQcvHEYFNehu7328aAwXf0iIguAsePklQuQ4VK6vFCueIiDfAn0xs2rO4ThdagEYhxRcMfujRMVI_IVOWGMp_pk7b1JSmi2IHrUTBivn5KIoxqMcD93YrfpjmoWa2DNvGfOFbqTidcF62VeA4YAuBqO2vxlwC7vbxTPz58" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
این فوق العادس پسر. من میتونم کسشر ترین حرف‌ها رو بزنم، و شما تشویق می‌کنید.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84685" target="_blank">📅 00:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84684">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مورینیو رو
😂
😂
@FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84684" target="_blank">📅 00:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84683">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مورینیو رو
😂
😂
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84683" target="_blank">📅 00:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84681">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EdZ4X5Old6pr5Tcq4QYfYuhMVsWxpv5n8Yf224bIvqBOOuMUQofNpddsleo1m4AycGUmjB4fExODrDJFglmZw7LB7KZXOzWCvbl7uvoAfat5jQRGks2N70nWV6l3x0aMppaUxDY6ERQzbC_mRUdpjODhVM9iUtkfjDeYz767BdFcxjaLSc3ky5Y3Zc5652N3_Zk4_jmsimepMlh1o8MsOcV_kDxm1XoRdvF7D-z5iQM75zKYuY_fuP5jXF5GNzxyNXERPPM_CIzMZ72GnQcLopfmI-y-XOBYksVY_4wFwN8TGI93Goum8JJDr1obOHqPfeMJcs9gVumFSIMZVZl_TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kq635_j4xQboaM7yDnwr7tq3e9YJvphVUalIg_OvMBOFEHoEvmk0EKSe45ilX_2vSGc3mo9WUlTjokFNejDijILiVCOXC8W0WW8c_CJdvz0DTl3EmNgJZRJJB4GM9cv2lNQnGfybWvt5Lnl19E5MTEn6i0-BIy0ZvaktiDkFxjVFLJ5MzYdZcm4m4u8aST81YYo9dczqaA4oEnEz8fJtS8TwQXe9KguH6VmZNdFZqlw25dSSMivSMO-_F8ctkDx8rXAlRUzTMIlXSjvl0XVUMvYmNflz_tPEnnPPRF-LHqr4xtIONohbdwxTaWt0ERiEBAhFhOl86KqtfCeJBAhs3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با پاسپورت شمرون به ۱۹۵ تا کشور میشه سفر کرد؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84681" target="_blank">📅 23:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84677">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JKPVdXr864iP8XhJ8nrTmB2bBTaBiJJ-GkoHiMcjS3Kn2L-Gg0FSA5JbPRJwFzSayRVodnJjPxkL6rtJ78XffsPwW2bM82KQpSR_pS4ceVsJG5GoUe0Wj0B1zZlGjToGN-qnD6YiPHU0Y47FYl1nDVKCTxP-2QC4qrISRHR7zHYpa8qMRljIns2INp3ANB1JKHJl326eMhziPJEZCHBBsCXwzG_iQf8deEmMU1XuwsOCStj6eg4G3FnH12HnEhQq7CExDcctjMdcd_Lgjm-TibkceVyI49hXB2FfPJeI40SyxoOjjKanj-0MxozCzBbQkC32Le0igCScxXb-yYQzSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UIZFqklQ58NaEyc022SpLqlvJM7uGKQzVxqsh5r3b5Jr7kUKEU3p7boEHDMUQD2LkWGyG5RJLni53YUWK0M72fr7Ql89_ILROo6B2AIFAtrpnTn7EMPmoZwvxcqB3Mb2plqdwFe3t3TlDuvZWRqWlPCacncdIZspNrrmZSqWz4nmKwI-ceHm09rNgJySHUl7FWyjmXR5XEYN9wpLfVIx603feF_1euxysKVnpnNlWYCTGkeYzz5zstPls4gMoR7LarsR3NMcbPEgqjoWnd2wcAINwyWp_mP8Cb6Rlm6z5klNz0cuzaTkXEOIq_MtLBmacIrVxco8gaWTVONiConruA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i_sdh-DqDu2yT3FfdPw0xg81ZX2QTBTXynmprkcASRuV-ix3J22jgOVpYsv2R8coXCGtz_yuZquOddyNqQAW7m1utzvkyyMXLcxzfPOkz4FR9wbDLflB12xaHbxGcwwTiIRHxXce9XcTwXOJdHPeS3CVgUqxK4Pz-HBXPsEu0pegjN73k7XIFAriI3957SBotDb3fRcPiaMRE2C5kk6Q5PJ9Q_fJJoz6NVyGmpYhytyYas93VmbDnZMu5Ne4MfLw_825d-N2aWF2Nj4X56i3WCO-ljP3knPAjO7U3bfNw-9rGxsn6K7theEI38dZdKQ2OQOlIGb6WevVFECK4Od3nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZdV1nW0Kd79kcTdKYxy1wEVF_4VNEujS2XRQnVEAKdkiQt9pIz1yDXvCm3HcplLgQpYVm0GHHprCKFUBmkCQiL3_3fLV6UexW42IlOOTdBMkQ2u9jeKG5GJIpz4ebGABrMuaVcQvfQqrvd_Mv6ya7jOsAczsWuZOfhvwRDnYvMzPb2ygfpZhOUq5HiFa4ciXVXVzA-jGUeJh-N7Y6ZSg_VO6WxisCqYqVP4cZhFgrdVEnd5hJygV5hndTV3Qi1W05f9BBQbORRHCGwYwrT97UWtpfH-6b6tLB2g1mmHjkKANoGnTZfGFH_psq-oRI9t79xmxhSS8rX8QpVvYYrbzZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بسیجی‌ها امروز با پرچم فلسطین رفتن دم در سفارت فرانسه که به سرکوب خشونت آمیز اعتراضات تو فرانسه اعتراض کنن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/84677" target="_blank">📅 22:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84676">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd88d22e31.mp4?token=LedM9ZzGa5yqG1B_dFKj9I9MAitl1VlJP-hhhVk5oVcgUbBZgGxWPHRzU3KaIzs6KPssu-dfk7n2ULTsBtV6-ruRpM64_yerlnAFIoApk_V-w8otQx1iuT_oE-bjUu1hK-HNyZxNhWZ3-EWLfsxCGMoeTV9h_3T7zpFGoCvvhi88omVZ5luvRgdmBrBt9A-7uXVcgCpuePz8yLkplANeYDg7PIzfltycP5wShm1A4wrvqOK74_etHLtaTlpwBExvyp4f_inSwuiau9CCY6GxhMyxSCHm-0HP6YN6c__8B87S8HXnEbubIlgUkcDOpcyCo20NOt_nT875ev1yCGptew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd88d22e31.mp4?token=LedM9ZzGa5yqG1B_dFKj9I9MAitl1VlJP-hhhVk5oVcgUbBZgGxWPHRzU3KaIzs6KPssu-dfk7n2ULTsBtV6-ruRpM64_yerlnAFIoApk_V-w8otQx1iuT_oE-bjUu1hK-HNyZxNhWZ3-EWLfsxCGMoeTV9h_3T7zpFGoCvvhi88omVZ5luvRgdmBrBt9A-7uXVcgCpuePz8yLkplANeYDg7PIzfltycP5wShm1A4wrvqOK74_etHLtaTlpwBExvyp4f_inSwuiau9CCY6GxhMyxSCHm-0HP6YN6c__8B87S8HXnEbubIlgUkcDOpcyCo20NOt_nT875ev1yCGptew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمسه میگه به خدا من بادیگارد ندارم چرا به من فحش میدید
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84676" target="_blank">📅 22:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84675">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S--X1c1bQRe6fjyS8H5rL0DiGFiGIeQOdspb3VkWVgIz53V0uuGEtnMqfEB7_uRS4yKrA5A558Bibmnoqw_GAn1kH9bZMcidd96HR1ycVvCaMKn5s3VLFBWQxqOC0IvWBov7Nf7Y2RimEqJdEkZZ1K9VC4OklQLpuRNIbGyowX6QQNXLoOP_uC1i_Sw7zDiZrLJMxKHN9JkggXOod_VERu5QdnmbTdfz4G_ZDDAoRkiQrbyYUvno9H1yVSxT7oNFvgCfOpPZxj-H1PQX2Z2TUo6RuWmVBaRWIC_T7Xcfw2lJRa2rkBsJKt26heRNPktPi5TSQkk-vpA9C-i7Ft5-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاره شدم.
بعد از اون کامنتای مردم، اسطوره نوید برگشت به تیجی گفت شما اسطوره و مرجع تقلید منید و افتخار می‌کنم که باهاتون تو یه خاک نفس می‌کشم؛
تیجی هم اد استوری کرد نوشت پرچمت بالاس
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84675" target="_blank">📅 21:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84674">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Talangor</div>
  <div class="tg-doc-extra">The Creator & Lickel</div>
</div>
<a href="https://t.me/funhiphop/84674" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام تلنگر منتشر شد
🆔️
@Amircreatorrr
🆔️
@Rapkadeh_official
®
🎶</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84674" target="_blank">📅 21:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84673">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijrPdo7Fbkf3bkyLpSiBvfuEpOltlygEGerIXeE7FaxihiCvxCbifzypeCtrVLEHgBpAkY3UI84WPy3uOAEOPu5Nwa8aYkckpNEIjtmCPp2Hho6We-OwyyveJCtE5dIcp2BmcZJ_3I0NVkKBRBJZmEHT8w252rmt07c71HzBszEVw1thWPNj9Zgddx2O1GfehO24ivx3h0bH6VET2U3Go28to_WFKgi-MiJJDwcbFHB31dLAzaOXCHt9jZQ_hNBng6NQuyjKc58p1FaKItAlLpA0Y8SiBs3tL1-fbHayBR8KHt2Ew8Oz7f_0rps5mgilCQjG5o-oiI1LbNjr4_-ezQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام تلنگر منتشر شد
🆔️
@Amircreatorrr
📥
Download
نظر شما درباره این ترک ؟
عالی
👍
خوب
🔥
متوسط
❤️
ضعیف
👎
🆔️
@Rapkadeh_official
®
🎶</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84673" target="_blank">📅 21:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84672">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25eadd38c3.mp4?token=fgmC7YmYJw7yR8p57JPjTobKRttTtVfFxBEXsoJjoxcqQgTgSW5BHIfzpcGxg93BZG_wE6Tr_0iSwE2cVSWxw_gAQ3lNXsJpHITcKWAwSgdr2hY-vAxK7Yx9hbhxrrrlhD1wMNTnjy5-UFalhVN57-XFv8SwnR0IYJPK8ci58oCSgkbD7EqMPiWWpoguf0wwBZzAgR35Lt2dfT-aUjg7IXDK2HUyjqpAGL9jKWfLnavEhbcQPpdsdcjllKgRLohJLOpYRfSbhHxgf05YXXCq0FyKyXFHPaLCRfq6MTqqg53RH3ROib9NiraNWSHpA-ciJYeZNbtXHfPo811rTeCHOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25eadd38c3.mp4?token=fgmC7YmYJw7yR8p57JPjTobKRttTtVfFxBEXsoJjoxcqQgTgSW5BHIfzpcGxg93BZG_wE6Tr_0iSwE2cVSWxw_gAQ3lNXsJpHITcKWAwSgdr2hY-vAxK7Yx9hbhxrrrlhD1wMNTnjy5-UFalhVN57-XFv8SwnR0IYJPK8ci58oCSgkbD7EqMPiWWpoguf0wwBZzAgR35Lt2dfT-aUjg7IXDK2HUyjqpAGL9jKWfLnavEhbcQPpdsdcjllKgRLohJLOpYRfSbhHxgf05YXXCq0FyKyXFHPaLCRfq6MTqqg53RH3ROib9NiraNWSHpA-ciJYeZNbtXHfPo811rTeCHOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببین عرفان جان میدونم ضرورتی نداره من الان این پستو بزارم، ولی تورو خدا برای یک بارم شده یچی بخون بشه گوش داد، من خیلی دوستت دارم ولی واقعا نمیشه گوشت داد، لطفا لطفا
🙏
🫀
🌱
🌹
✨
🌟
⭐️
🔥
🌈
☀️
🌨
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/84672" target="_blank">📅 20:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84671">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
ترامپ درباره اوکراین:
«پیشنهاد می‌کنم اوکراین رهبر جدیدی انتخاب کند که بتواند به توافق برسد.
-به دلایلی، زلنسکی هیچ‌وقت به توافق نمی‌رسد.»
بابا یکی جلوی این کصکشو بگیره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/84671" target="_blank">📅 20:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84670">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وضعیت فرودگاه ریاض  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84670" target="_blank">📅 20:23 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84669">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOnWfFM45h026LYxfTQtleDWEjshiXtmnwyJHXwLqDQSBFUCrnmvoU_EXZtkkQlzU5fkANHV0eWSdH2bjsK7bel05_DwLOaDOub1x4Jt6h6xRkeD5V-3Voxz4YQVFguOJquynq1sv4oJVljYfzkS6bRBt7NyMTu5Ui0KQhxlF23En1D_kg5_AjyEm9gXF2LS3SpkjQ4pOT7coDPVMMNXe48vWpr_AJvAQNcF7yZGDXLA-GSZr-T5vQkCbkU8_VrNlH__GUJXze72IO6TU8obAAOtQstkY1eA_3CLxgUnwdyn9TpP9LmAOfhgf2sW8WIYAqj8bb-2o0WtnYnhPBMjIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت فرودگاه ریاض
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84669" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84668">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/84668" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84667">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgDE0LzUItFixWzjtln-83UeZuJGnXhcXwpzIRY7-b6eaGF2NAqdw-MvID02ScUgCdKBqM43j2oESp9IxbVzzFuGr0koD9WN0OJBrNTEDV3Lb0sleTxLKOYqJUP7S6wLM50cRMo3UPakjaVAk78ai4PLOUlTkI-ZcRPgl4EAGWZx7NkCHiOP0b8URObN4QQKUCyom5mBvjBSRsq1lZZkTjezcCPblNf8PiD9sDuwbcGD8goroxKlJ0epTGq5N_Rq24WksH6s4o5JyNfp0fqCqYawbib1ceOwKOkyjahPkBgM3XU4mnMzGo-IlZxIo4PJu94-QeXiSnvPrQRXtN7JwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G18
🅰
🛒
ورود به سایت
👇
✅
https://ieoruyxtsud.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84667" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84665">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aae2137c8.mp4?token=MecZ0LwbQm0qCQnbcj3tCVM-dLZ0Z_16JFmBpImsYtXORZNnCOx-7pLnp9ubvseffJ_pwI5EXvGtWheThhJLs6t24jq5jWL3jr2y9pUnbCiucTBBbe9pJZ7j2rCgKCjeMLUYLa6w46Mio97EwezqyJnUGc9T4VcjcY7Qe-cDXZg7bQvQ9DfOfaVJKxhIS4NKzJD3jZ2A7kgSG2rT45DmMUvlxqjl6z6t_01l05Y5Kev8aMlNUex1CVi-Uao758Z1I6_OYHFJOYaJPzN8QlthFbZG0ApSaGKaZj0rHMDouMeBlRZsWcoGfj1_M-YRLJdKQnJd8WjEcFez79-Kf_D4Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aae2137c8.mp4?token=MecZ0LwbQm0qCQnbcj3tCVM-dLZ0Z_16JFmBpImsYtXORZNnCOx-7pLnp9ubvseffJ_pwI5EXvGtWheThhJLs6t24jq5jWL3jr2y9pUnbCiucTBBbe9pJZ7j2rCgKCjeMLUYLa6w46Mio97EwezqyJnUGc9T4VcjcY7Qe-cDXZg7bQvQ9DfOfaVJKxhIS4NKzJD3jZ2A7kgSG2rT45DmMUvlxqjl6z6t_01l05Y5Kev8aMlNUex1CVi-Uao758Z1I6_OYHFJOYaJPzN8QlthFbZG0ApSaGKaZj0rHMDouMeBlRZsWcoGfj1_M-YRLJdKQnJd8WjEcFez79-Kf_D4Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84665" target="_blank">📅 20:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84664">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">امین تیجی جن زده شده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84664" target="_blank">📅 19:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84663">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">چرا حس میکنم هوا دلش میخواد سرد بشه ولی روش نمیشه</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84663" target="_blank">📅 19:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84661">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oz-VctJgGWHsrBWfs9enVZQlD6jL56CB110JpV9VI-gB-Ywtvv1SvB_57dUssLGlbde3Q5vMetirPIRCFiBmypJe5y3OeC1Lw8VBf25ELC4CN7sWcuJ5DNIZ82fK9Ie83Q8AuPPXLO8Xi2x_FTCMeR5XrziZKjHHAVQX4qgnQc_50vM1q6AaYi1QvcGNT0eR43SEOixpOANzVQHXupHSdX2xqqfSQEB1pLCn0D--HgkAaqBoMdhI1hX8eUfgIvWloBpCJRzFNOylqm7hZ6cMiaWPEEEwL-omCfQu-Q3FEmoF2wDWEGwg94MPHywOe4rryjXwB8npDngxz_cE2HJ75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XWF_KI-tJ19j8hPpUhf9hV-O9B6s_a6xeyr-IHawe4vQ_LJr2sedJ7XxTos1cBLNyk9tIukOANDMwz46aJlpATk5INdPOyCJbP_adkOjAxjXqF3y-5rKzHnK0d4JRxnoUyBsV41u1hEG_SDoc0jfXMiHiI9VzJSF5ZyLuJA8nkkTSERFL7koy4BrOmdJP5Y4T4xSnicldYwN5A8hj11QMRHfOyjoIuK7bkV62Qz-SVYJyLbgv5vDCTkceWcvsdIdJvychU6HMID_nJZPD9aE5tyuANCUB2tY9BgbNFOvwQJ9XN85rpy-DYI5V01jFK9L-HBmkhXMtmhybYPxRXHYsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریستیانو رونالدو موقتاً از تیم ملی پرتغال محروم شد!
فدراسیون فوتبال پرتغال بعد از جدایی جنجالی رونالدو از اردوی تیم ملی، تصمیم گرفته فعلاً این ستاره رو محروم کنه.
کمیته انضباطی هم رسماً پرونده رونالدو رو باز کرده و قراره به‌صورت فوری به این ماجرا رسیدگی کنه.
هنوز تصمیم نهایی درباره مدت محرومیت رونالدو گرفته نشده و مشخص نیست تا چه زمانی از حضور تو تیم ملی محرومه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/84661" target="_blank">📅 16:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84660">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کاش آرتا و هیچکس یه فیت بدن، هم فنای آرتا کف و خون قاطی میکنن صدای اگزوز خاوری هیچکسو بشنون هم فنای هیچکس کصخلشون در میره صدای اوب دار آرتا رو گوش بدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84660" target="_blank">📅 15:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84658">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLysd1kwiSdKxNFwC5S_vyawXJxiD01JZ9PfntqZ92_g9zbnXUGLfMrH0WWRs4OaobMPt5KmU95FHgrffWCH7iz7eot_WxeJuEXPi7ppO_F6sRHTRXXiW9aGGT6R8RGztNz6eLL4DpSMNaEOIlwD8WyVKCxV_WsfxmzbZgvm5GBS2UOc67S_OUWIvBASwZG33ryjIAkrXZXQRdTuE18QPUNmbnOO-SnX1eiYQ89RThfh73eiIIHC2Bhbc6KU6Ho16J4b5enGh5prBqVXv6fBvm7hQKrDgYE26IcJTqBICoWN1MjNj1kwg2Le4TXQC4cKmYYT1qDwngMgR73T1zDJ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DMKTk1J4Lv6R7XwUMgX6Ilhi0Fh6AFOBCDnGLTdSP_TiV_coD9SncqGWOstsFnXHZuPaYNu3sT7eoo8xmsVdQpJDDi1_ucK3AHvCeRB9Cym0aEH1WIsqBp3ho74iPYO0m-ywCEr7gnTWq2Ol4AcObpqL_q05ukxNq3yKvnZVqh3NGyJ8s884ovKF_vX9PtJhLNkOgbWJnqYEAUilb7qwtfIzoH2IVy2TMeW9cHCIRf8eus1xNTlOTPUtA51GnPbQk-4PNDwmC5gi0XQyKi4enTqGm6SY04hNgNK6RyeARWHcdZHvFlcfMFAzcMER3LTegF6hRB3qOrGuYFGyvmlQjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سوتیدا، ملکه تایلند برای نخستین بار پرواز انفرادی خود را با هدایت یک جنگنده گریپن در استان سورات تانی در جنوب این کشور با موفقیت انجام داد.
وی همچنین خلبان بوئینگ 737  هم می باشد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84658" target="_blank">📅 13:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84657">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حصین جان جوس ورد از اون دنیا هنوز داره آلبوم میده، این یاد کیریو بده کونکش پیر شدیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84657" target="_blank">📅 12:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84656">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">در این دوره از تاریخ که ما شاهد امپراتوری آمریکا در دنیا هستیم و دیگه بریتانیای کبیر و شوروی سابقی وجود نداره، هنوز عده ای وجود دارن که کلش آف کلنز بازی میکنن، منم جزو اون عده ام، کسی کلن فعال داره؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84656" target="_blank">📅 11:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84655">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ:
ما گرینلند رو با قیمت مناسب به دست آوردیم: صفر دلار!
کصکش املاکی
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84655" target="_blank">📅 11:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84654">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ud0GH31zsaFFcNYwuqiEldlz0K5iO3pzA9zt4Wgv46r9lrEQAaJbpgpbcRnzAn93ZHQW_V-yUY8RpOyZ7TSvDG3Ebpq9MGbuCccnRdayy2aEPPu0SYGkeZeYqPnrNNnuvz4vF3rQ2Ls4e2OO4h55_tKqcO_fQmcTvAgOVS-jT5ehsXSsDePFG3JHfRjElpuZIlkB9gwWueYLcshotZfeq8lw4fyI--yR1Atwcq8-kKx7Oam53at7axs8VTMLd6mw4ziTlQ3ySJa5VXlsj0KtxkXGGqyzNS2H7kr8hK10Ss26RepUV0okTFuZfnDCLy564kKLDh4FHXCJiPDdYzZKEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من میدونم تا مدت ها قراره اکسپلورم با این تصاویر گاییده شه، فقط بگید چقدر طول میکشه، میخوام بدونم تا کی اینستارو باز نکنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84654" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84653">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84653" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84652">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPXMoQODHTTPoIY1tcrrDWiHf0UmXIP-sswWdl6yoJgrpgEM1acwl78BVYIRU37oVMjIQho0wc6AoZhOO9zbvx42Gi11S3lwUzi4qyVk1kWVfEcrLI2Qq2-AJodZhlrBVoIZoqIBBch8TbAK47PuL9Nby0W5tzdLuDYUxbgpYduFdGqxNmufSbc73VlmOI7BZG79QRWiGt32GM9gR6h6jlU5RpLyPeVe1DIE4Qr1uxv34OFI2FqLfeVuM01jsiWPps2Xn-XhP2hbinathfh9tNjBTMcVJQ-k4yPvOWQIFxdmIH-lmvqhoSEp2xnFOomXjeIrZBeXwHkMy5zGykB6BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
چلسی  - بورنموث
🌎
ساعت ۱۷:۳۰
⚽️
منچستر یونایتد  - تاتنهام
🌎
ساعت ۲۰:۰۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r18
🔗
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84652" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84651">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4795cf2815.mp4?token=qcoh-vQq8obYa_7YhDXALu3TfpFhZS8bmY8_d_J1uwcNXiQ_-NAuSYb47gujMgZhLerMzMhnmWLTk0uvj87UHjvHCohXEarJJj11GaPXLQdjWkTw73iSKARgi_A_FopCJvXCw9idZD1WW52nQOzmDlUmxPyDqzgKqrHWdQhdINgFFYual_k0T7hzEqzYyaXr3C4oZJZT10LV4RkJHuWwiQ3hgrOZXbFuD_neOGJNZkl4NROhpM1H1wg3ol0_BbGAehesr7ej2hJTrc_hsoD-a4Fd4m58Tosp27OWMz_rmb3VVtHbxmu9IbShqdvzWTbHyjAWG17QX3JzbORSsOI62w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4795cf2815.mp4?token=qcoh-vQq8obYa_7YhDXALu3TfpFhZS8bmY8_d_J1uwcNXiQ_-NAuSYb47gujMgZhLerMzMhnmWLTk0uvj87UHjvHCohXEarJJj11GaPXLQdjWkTw73iSKARgi_A_FopCJvXCw9idZD1WW52nQOzmDlUmxPyDqzgKqrHWdQhdINgFFYual_k0T7hzEqzYyaXr3C4oZJZT10LV4RkJHuWwiQ3hgrOZXbFuD_neOGJNZkl4NROhpM1H1wg3ol0_BbGAehesr7ej2hJTrc_hsoD-a4Fd4m58Tosp27OWMz_rmb3VVtHbxmu9IbShqdvzWTbHyjAWG17QX3JzbORSsOI62w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداوکیلی ۵ سال پیش به یکی میگفتی پیشرو و هیچکس رو قراره یه روز کنار تهی و ۰۲۱کید و آرتا تو یه کنسرت ببینی فکر میکرد مواد زدی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/84651" target="_blank">📅 09:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84650">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258be0442c.mp4?token=hsFVzb4J-ZlEySQF1y0NDxGiVMeo9XgZi6qTnYn6Grp-VpfhgaEmmda3tLLI9O1RFXKi4hdg2ty4miOA4p7YNDPRT-qP-Qahr-TJ32OSRRF0fGgSkQFYDCVIsGacHVWCj1traXB6mYyqt62eT_fAQns5ydOUcTDfIdoZx1fN5zsoNSlqr8JfVyhfDGx9DQ1XsFLT7iSeBVqewsBtapbPbKntu1NAfByTQMlRSsM77fJKfKnmkJFLZ9KneEUSZzyl1C0ZQ5BrpoHHMlpTuC9dkQZuWp4DNsVLol3BGkCaKGxcnbd7U3xJpwaU2j3ve4ghL6Kne1EGm5TqBNrZeoZR2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258be0442c.mp4?token=hsFVzb4J-ZlEySQF1y0NDxGiVMeo9XgZi6qTnYn6Grp-VpfhgaEmmda3tLLI9O1RFXKi4hdg2ty4miOA4p7YNDPRT-qP-Qahr-TJ32OSRRF0fGgSkQFYDCVIsGacHVWCj1traXB6mYyqt62eT_fAQns5ydOUcTDfIdoZx1fN5zsoNSlqr8JfVyhfDGx9DQ1XsFLT7iSeBVqewsBtapbPbKntu1NAfByTQMlRSsM77fJKfKnmkJFLZ9KneEUSZzyl1C0ZQ5BrpoHHMlpTuC9dkQZuWp4DNsVLol3BGkCaKGxcnbd7U3xJpwaU2j3ve4ghL6Kne1EGm5TqBNrZeoZR2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درمورد جنگ ایران:
آنها یا همه چیز را به ما خواهند داد، یا دیگر وجود نخواهند داشت، آنها این را می‌دانند.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/84650" target="_blank">📅 05:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84649">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تو تنگه بزن بزنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/funhiphop/84649" target="_blank">📅 01:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84648">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اوه اوه
روسیه تا ۷ اوریل سال ۲۰۲۷ توسط امریکا معافیت تحریمی گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/funhiphop/84648" target="_blank">📅 00:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84647">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYULVvSjdehuSFsL5kuYFuHP6ACpDhvxoRIaSeViMstTjdufmkrCg7RPVKbzVGfpHWTOUMdUULyhHsusrjqJdzHxw6TOxcTHLJeEI3aOLUiJm4b-4O5icXnk9tBoWASSUQGHxmZrhID5SUPZLzhwnnCjMKUFkl4Cvg36SdVZCvsPlgsdiDAQ04RJDL8kZ1kIF20l3DjjKCIu4RuuSASf35K6BBRjUvpA7i4_R_DnBmqjN5txVcz0vu_yCbqVjO5DXfQQKVs1ijK1GrHOekWbMktJrlmhg3QzHq-2JRsWwAazXijOQem0zxRgZatO_bhd3sh30QOJuDrVBYK0iw2bMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هی داره یکی بهشون اضافه میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/funhiphop/84647" target="_blank">📅 23:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84646">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idtRcg-NWWvYVwnUb8HTYxiN4g5HbfedSrVKcFj84eB2pKdV20yTNQJF4hv3JpPNuE6DV-38cAZS7lDE2xVzEzGvt98ORWtUcMxoT19HVcp-hMXTZuy5E2xe2sq2XmB6eVzz8zBddtprplxLIRQ7TyRM9r_UwEuxrCyZXr41cdF3J5Pi7etPJGNOW_ol1GPEjS5lYFpxh_UbLnNU8_w0_2PCDhDIVEN9bct57EdYJHJAtVZ7z2AS_i2Ja28BezS25Sp_eRZwkSGTz4X2qmK45sxPSEYANGE7cBoUOM4PGHrK7naajIl9UGfpDgEAzOpXCc2MPJIKthNcyeFo2_IwGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان فعلا پست ندارم اینو داشته باشید تا بعد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/funhiphop/84646" target="_blank">📅 20:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84642">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mYiGfgkkDV0whlOJdeO0ioMAm1-dVZ2lM_A9HCYg94Mqdo3u_bLfHDhgsuimybzShb2D7gD0OowYtql4YOzq7fiKJqp_Elo5bsNAgj2JvRRHBF23G9VsXuMsef44-pS1fOZaVkcyAigkgLFPLkuhxsFY7w9aU4jA5ej9-mUdIWeLsq_8hK5HzxXFr4V5cHsJRnZCpHIMaYoaE-3aX7N5NOWYrDKfCROtqv5jU0mnD5cTERb9X35UJ-uy5kJiJN74hxw1aMRng1JaZ_tqy613EtIWyO8MdLM2G3GVSA6PCcPDENrKiptMje33ptRaGnRY8myZANRcLtLnGFj6h5F_JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DCZjEGOCPN-EJ9dpmU30kMTTYyDl6HUTH1qP1PhgYmLXeFxR498S6XrYwcaTeqNmf4aHqCrx9p-5XtroP2wKPSRFlONQsLoete5sSGs0_MnYcMmm0y2uwE0pzalZeR5e08Xj5jSPQAi_hKQ8AAx3EZ_UYF5_d-Y9vmFzdD_ItByb-bcRunKK8e5r0PeX4rUEyZf1RFRIhSQlg8HbjSjbi2fizcl-LaQuX4z2T8Xr2QBMKQ22VOVIcVZrxR42zwFPj57fFpQtZNPiolOPEQcw__bF_uRvtDK4JI2msgglNckdeXWjTmVsUnWgTJvtL3Xc4Q-Wl5e8XxMK2C59uRUbFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pZOLGxyr_YuQvhp5H-9vxr-w0s-MODFjHpCuv4AONcJFvcf6bA3Sx7PMfMpY_nbllixChqTHBLQJCdMQbQyae3qwGm43atAX5k9WkC0JKKs0HRVvQEme6S1uWb6FNEFt8ZFf9IblC3mVyoMQGMFH6qAO9HXFwPlnX3Xl2dO_3HjXZoJd6BUUcOl2EwdMQ6kCiNhC5dk9WL79CxjFDSil8k0556ZnspRuN3jdGgaI9Ugw2UlG4AJgy74xfAMRbpBVO55a6LDFc625SfhTUJLISWG-VmdMecJYwm7eoubqa9zlc6jNph7QJCyAeEnD4ZIFMar8mV6gYaKro0anIDDgaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jNDnyoHgaEJxYFnbqg9KbSrFAbuvzeoJoKIvCTUgJcHDndLYW8hF7nXeU2wonL70MJBTP4J7NFFLnsJxDW28TL-G38BMulT6xgHm9oNi4eNb6-tvU3VvX8VM98UAoCpO-wVgho6pPUbq3s80j3Sm2tmD_5lv8VPj4o7i_vL8RMNlQlyt87nQBfig0_2JZz18GfiAmYj1PensadR6KjEfWRGurGVDP4zMBv71BpnMWUknwntH5-CfhISY8v_Qx-ZPjUIip6qa8msCzUw2LJMf82cwLhvaG4CDfmTSAVQaAmKgQMRF29WlF82LrlslM9nkPcdKaBXnytCZJB6d9tCDtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همزمان با ماه کامل بر فراز آرامگاه کوروش بزرگ، این اثر هنری زیبا خلق شد:
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/84642" target="_blank">📅 20:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84641">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAPvrzhgmh5TCLcrBd1UTcORo1w6uALngn4fAuAxcmUqtAwY1CZ47T5yzJHGcXod7nLo9KdhTBJn7Yj4gokfDIT6u48EIC5lcLcKLgpJZ0heEu03jGBrg7aaRTU7TXQZS2NpWT9Re4kbvcKbf0xSoX2R0S1fJootju3f2-Z5f6cqWNpZ9rBG7OLZhjwWvirOb8AdaOyXRUjPwNziBoRn4FshVWW7wWZ_2HjWyjORWWDg6h7HQ9DzHSyls4yzYxI_rAzeDRxH7ddzRnSrbBf5HQ24Fg5TWDUZqbcA9ACG0Le8Hf2kXK86gdQNME1kPxBQd4GZOF3VZe6n8lvtrG40mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چجوری مصرفمون از خود افغانستان بالا تره؟
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84641" target="_blank">📅 20:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84640">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdCalitSKw0Q-NQQlvHw_gtcnQr5_Ikg0a1UyYBoDXkKmBPXkbLS2x3igywr8m5fleiCNvZ5toATQgrAo221ALKP4o_p8U0f0DNgO1cS5eoUyO-aHsYu92TnQi0zkWeOCPv3F_x39KgtDbF2XjAgB8U_4gJ4hYcxM8N1J6JTRuQ6A9sbJUzZRPIqNFw7_qG8qL7D36dAp-lETi3D3PIGAZ93SMHX0uibfnnGCUCVY6d9dmnUpeoDlwxF3xAGtao4AHJCtD0_U1cr5bAUcCx_P2qYf7rBNfWBQwEWehSIrhcUMqPFYKu-OgIDYENb9CClj3Anebx_fWZZgSxEg7ku3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G17
🅰
🛒
ورود به سایت
👇
✅
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84640" target="_blank">📅 20:28 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
