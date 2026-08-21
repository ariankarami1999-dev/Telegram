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
<img src="https://cdn4.telesco.pe/file/iaWB7MDc1dHliDQK12R5YMtpS238bEoVQnNmumkkh5omoqvLj2TpbFhntFyrY1BwfcoB6ArxdbAZXEDqeB9LWNS6t54FGSftMwMuLJi5_sOemfddCl_4bHYn_zchxcs5LyzsRZnPUMUbxy5sNyNdZzfG54q6JgQ7-ftSrGH971jdbih_FWRw1YBJm-ZJ4PjlyJv_MgyQUqrTasQLPaZJ1unYqYCE-v2Se5XK3xpOs6-pjAUj9XMydxpgpHmramLfzXouAvVa2tBwiAX_l12-vaL2Xeb6OQl6gnWhRSyBQsWsGx3fB8H3LRmDel7pSr1QrYwSACwg8c3MhWx2cC2aug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 989K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 17:34:59</div>
<hr>

<div class="tg-post" id="msg-143044">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
لهستان سفیر اسرائیل را به دلیل توقف تحقیقات در مورد مرگ امدادگران مرکز آشپزخانه جهانی احضار کرد.
🔴
لهستان سفیر اسرائیل در ورشو را احضار کرده و از تصمیم اسرائیل برای بستن تحقیقات خود در مورد حمله به کاروان امدادرسانی آشپزخانه مرکزی جهانی (WCK) در غزه در آوریل ۲۰۲۴ که منجر به کشته شدن هفت امدادگر خارجی از جمله دامیان سوبول، شهروند لهستانی شد، ابراز ناامیدی کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 15 · <a href="https://t.me/alonews/143044" target="_blank">📅 17:33 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143043">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMolLM3mijBDnU0d6z4aQ7SYZhiRAJRGi-hWRVG3IdW7CkjeUDQW53C7XzjD_Dvn05FQWOVCtHLldMmyJgNnXqO7HY4S3JBCLmeBBm8zkF_2XveTNRm3G9VG4BNr7weYhqufTlI9pkcsDEYltpxK83gq0EKpQYz-Tz2dIAqLS78wU0wiObEk3cIAVgFIhRviEasXzyXYN0K28gb1_ccIB_RHVJpxTi3Bg_x-ymgj7cnkUg5ch73Cz4-L4rkmfuovTRMghyzDu4Vgb5YDKtRtHvgV_s2CnAZctMpvcAsGi7uWBDG4rE4hM1BQMqCQmmGT6VzHib52BhYGNU4TrHn0kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت در ساعات اخیر چند بار به 94 دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/alonews/143043" target="_blank">📅 17:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143042">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAnA-M6athWiSmT7kENZDxRDZD9e8FX7BcMpTgnUWnZ7CHuSkMEOtJJsSTJ0JOTt2d0sK4kBfsS4f3JDv9kViv42trbpDkK39tlDW81ZLOJ_C_DQ7k-FV8T5AhpwOk2tTdBJ8R-594Zhc00wFXPPB8TCBK6jqozGYGoOgkmQTQxcpD-KmJHFGRSBwip0WEmLem8Nfcdh3hNXQKrr8X1Uzn0RXad_0u3WYvugvLenZCWBynFbVpcRBFaQkOwtPEqP4wfZl50RLyGLxt_TPhSiubI5mcu3Rz5PaI0cNzcalCeQ7WgXtExFYuow6rvIZ1xEIvG-gsR98CXTR0Dk6XVMkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالی بافته شده در عراق در سال ۱۹۷۰ که خلیج فارس در آن حک شده است, ۱۲ سال بعد از دوخت این قالی، "هیبت الحلبوسی"، رئیس  پارلمان عراق به دنیا آمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/143042" target="_blank">📅 17:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143040">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6LshsTZFbYc7NKBuL0GhQtdiWnTaisFvD7uwwTOX9rox6XP-k6kVwf9DOZqYUDJPYbIpXetS3sDoc4A_csFf4b6vToVbTKohy3d-T_g3c7MuPNTNJB_DpFEdfoH6l8jXKriTSJsksRU0gmZCa2MeYbc-Wjd4uvSlY8Mc_ohR81OtpQhoHdAEaQVNe0gv7bIUf1CtNHdTVMGFIDD8KLvt1at3QbE-cypCyHMRH3etQrmlQalVImGbClTDunoSB0fMMO6Y22mnlreWZHSr4A-p9iama7hWava77nnoeYwGFgRLDnYWrMFIvjPualw00SojvazyKhlifje88S5Y133Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تورم در اتحادیه اروپا به ۳ درصد رسید
🔴
نرخ تورم سالانه در اتحادیه اروپا در ژوئیه ۲۰۲۶ به ۳ درصد و در منطقه یورو به ۲.۹ درصد رسید.
کمترین نرخ تورم در میان کشورهای اتحادیه اروپا مربوط به:
🔴
سوئد: ۰.۳ درصد
🔴
جمهوری چک: ۱.۳ درصد
🔴
دانمارک و مجارستان: ۱.۶ درصد
بیشترین نرخ تورم نیز در:
🔴
رومانی: ۸.۲ درصد
🔴
لیتوانی: ۵.۴ درصد
🔴
قبرس و بلغارستان: ۴.۴ درصد
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/143040" target="_blank">📅 16:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143039">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
طبق گزارش ها، ارتش اسرائیل تمام بالگرد های نظامی آپاچی خود را از جنوب این کشور به سمت مرز لبنان و سوریه منتقل کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/143039" target="_blank">📅 16:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143038">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMZ_zFyKl1f_3HT5okCOUxqxdO03_RDgJfqFQ-SiVyUzI95tQRjesm1yAboJH_wxNybgIxEw9op8MSZCGhUlzWKI8JBuYSkTOx1XWGQYd8cHZqVoMFvVzKuTTw4os3Ew8QmOmTPTFLuWicVZaqOyaNROdBB5Aa1zovxOZ9ukCYOnikEoTjQF9xZenRKeV9Rs5HcVG8E4LwAKs-3ilgsPBDqiDsmgBLTGLxtf-Mljl1q_mZK8mIfBrUkF9OvVJkqiqrtWQP8tSw_YULaavEXf7kfmgOiku_pr904WgLfRx6psiM2aoGmktTImnegl-Jp1XT4EX8tCgvi_iiIA6zOJ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: به قدری اسلام رو ناب در کشور اجرا کردیم که آمریکا میخواد اونو از ما بگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/143038" target="_blank">📅 16:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143037">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xy410GwbDFZxDeoR6jGVnPASYhx3NZC2_qsuKPCdo7PtFVVIs9Do4aeDQ5T3N7eFKR0aX-5PZqkLxtabJ3oo9saEsI7jwO5bNngxYdmWEkMG-EUclHSdkAQKFdl9xHwfvFNfHK9BQ2ELFUAEWyCeJvzFRNMiLqZzOVj8rV8iQG9-l4gNY61TCrG7xTXSTTuziuho6DXsmF-pSUbuhV-qejI5JTzUrgeHGwnaQZk41SDOgvpVesLldZ3tG6kT1FkCe7hBsj_hKobOs5u4aHkA4qtF8KsPqqyPTt1oiyC_ndTJLHKV747fFKx4DCVc36qA-P-2k2It5njV4RLqHwLmdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امام جمعه اهواز: نباید تسلیم بشیم و باید تهاجمی باشیم، بنزین و .. هم مهم نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/143037" target="_blank">📅 16:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143036">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_J-uCInAgukmqsdOdebWO_74tsE93RYW5fvbfqPa_brImIos3YCWB1tu4hVXOI0iso7n5NViQ6anHEAe2vnEqe6KT_ve009GKcWyDBnsMVVT7WyV2sb-TILtI1bhj8i1MTX7dTJwo_M0cSA6Ii4TTl1yUDrFA66kutMZz08nfhad2PcK6wMsu158smszIHexgnmFwAT4ojosR6uUbLgdKV87WG9zdiGDjt1vG-AaC5ErZ5zIJrhJfYN6meAt1ccoOTyAIhSxuEk4oRl2D3-w2X45j5Wldkr31lM5KL8oR4EQYmAfO1pECt9chppBI9_SLHZWZgzKRmDGTv3D5rDVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان:
حرف از صلح در شرایط فعلی یعنی تسلیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/143036" target="_blank">📅 16:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143035">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
کانال ۱۲اسرائیل: سفرهای اخیر و پی در پی مقامات ایران به عراق بخاطر بردن دلار در چمدان برای گروه‌های عراقی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/143035" target="_blank">📅 15:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143034">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ef3638ca.mp4?token=QhO6P7LdI29-ww2f4hKnqT5NLi7BY0vZrul-qD-2v0W-wFgufRunXIjABxvwQu2NNBXOmhmK9od1YNOmSiRLSQpb0nSSIkk_9LvcTiTCmKcC42_WEJ75BtKHV_0FGQowJamhgGJ3MrR0_IA9WGzuslo2T_kBeJlLaRRGbYFWi9ExrKf6xqj4f0jozd69esVRuEVga9q3ghpjOTOnbS-ryp88Z5qXaFTWXSeHJKq06UyTsxC10HcuCV9XMQeI37kysZIp7g4YaYacKqnWssDdRruMx6zL7wgN3cJFlJTwjDRb8sSCxN4GEK2Xq72XnYkVNBL7ewHYE1pip7mItehA-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ef3638ca.mp4?token=QhO6P7LdI29-ww2f4hKnqT5NLi7BY0vZrul-qD-2v0W-wFgufRunXIjABxvwQu2NNBXOmhmK9od1YNOmSiRLSQpb0nSSIkk_9LvcTiTCmKcC42_WEJ75BtKHV_0FGQowJamhgGJ3MrR0_IA9WGzuslo2T_kBeJlLaRRGbYFWi9ExrKf6xqj4f0jozd69esVRuEVga9q3ghpjOTOnbS-ryp88Z5qXaFTWXSeHJKq06UyTsxC10HcuCV9XMQeI37kysZIp7g4YaYacKqnWssDdRruMx6zL7wgN3cJFlJTwjDRb8sSCxN4GEK2Xq72XnYkVNBL7ewHYE1pip7mItehA-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این ویدیو حتما ببینید
🔴
تفاوت واقعیت و توهم، توهمی که سالهاست سفره مردم رو تحت عناوین مختلف خالی کرده و در آخر برچسب‌های ضد میهنی بر مردم ستم دیده میزند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/143034" target="_blank">📅 15:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143033">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=SvhuZCxkdumeZ9iKdjF1c66Z2IEcFEGNsShqv8x8Kfk1AR_B_3JNCb6oUcB4I-i3DvJIAU3F9fwFjTBJmb4lgQSvXE2ptpn97Y1KqTfM9K2W47eDaNyVhuGQOcg8a8WikPNSr8Hcn3d740tV9OQtTbqA21ua2PpyS0XRPvFS3Ndbw-pHFVOEAgNPmFzGZuFsAje0Qxy758M3QBGI6GZOq5H4F95h-19dBgkWwpr22LY-eJR3dzOznQBJ0wf4DcfuYa2lEMlucDMtcv4EYghdq5Oo9HDW1tQXwuz6LmsSCgB5Jh8lIx20BETdhmgIsFzayhIQgdGQB1Vv2h2mMJaTLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=SvhuZCxkdumeZ9iKdjF1c66Z2IEcFEGNsShqv8x8Kfk1AR_B_3JNCb6oUcB4I-i3DvJIAU3F9fwFjTBJmb4lgQSvXE2ptpn97Y1KqTfM9K2W47eDaNyVhuGQOcg8a8WikPNSr8Hcn3d740tV9OQtTbqA21ua2PpyS0XRPvFS3Ndbw-pHFVOEAgNPmFzGZuFsAje0Qxy758M3QBGI6GZOq5H4F95h-19dBgkWwpr22LY-eJR3dzOznQBJ0wf4DcfuYa2lEMlucDMtcv4EYghdq5Oo9HDW1tQXwuz6LmsSCgB5Jh8lIx20BETdhmgIsFzayhIQgdGQB1Vv2h2mMJaTLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نرخ تورم در آستانه 100درصدی شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/143033" target="_blank">📅 15:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143032">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
دولت ترکیه حکم بازداشت نتانیاهو را صادر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/143032" target="_blank">📅 15:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143031">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=i6I8FzBn5msMX5xpn73HN3UeSmSY7wv1DwtABuYjCyrhpngjPGwFBmPZTz6WfVxIhYtkBc20v8Txa1LuPTIUbsa6z1FQQCKyc_URdKd_b-6UP5qCBY_0YF-GiILplviznwd_D8AcbOmXvENM69vmqJSsy3KN6xZxlMN0RmbNpY3Y6eUOJv4XbwfiMVvnx2YYRlUhoUM3HArFpI6_l1_u7DpWEt9-Yz52TPpNhb-8hQ0Q6NlRCJrEqIS0D0hMhJ4psIwXVq8YaQA7uQbCqkUq1Gdv-Lp3LzJbD_wm3blf_prtuHWQ5-Nm6vFh1me3ICNyCj-GlcnqgZTqnWomIuucBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=i6I8FzBn5msMX5xpn73HN3UeSmSY7wv1DwtABuYjCyrhpngjPGwFBmPZTz6WfVxIhYtkBc20v8Txa1LuPTIUbsa6z1FQQCKyc_URdKd_b-6UP5qCBY_0YF-GiILplviznwd_D8AcbOmXvENM69vmqJSsy3KN6xZxlMN0RmbNpY3Y6eUOJv4XbwfiMVvnx2YYRlUhoUM3HArFpI6_l1_u7DpWEt9-Yz52TPpNhb-8hQ0Q6NlRCJrEqIS0D0hMhJ4psIwXVq8YaQA7uQbCqkUq1Gdv-Lp3LzJbD_wm3blf_prtuHWQ5-Nm6vFh1me3ICNyCj-GlcnqgZTqnWomIuucBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خانعلی زاده: آمریکا درحال فروپاشیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/143031" target="_blank">📅 15:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143030">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
این خبر قاطی کردن متانول با بنزین یعنی نابودی موتور ماشین‌ها و ریه انسان‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/143030" target="_blank">📅 15:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143029">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
عقل عرزشی:
+باید با همه بجنگیم
_خب محاصره شدیم و گرونی اومده
+تقصیر پزشکیانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/143029" target="_blank">📅 15:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143028">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
حالا این وسط یه سری عکسا هم پخش شده از جورجینا و اون پسره
💢
مشاهده تصاویر  فقط قیافه پسره
😐</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/143028" target="_blank">📅 15:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143027">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKVXZ_mGCbyqmi7lRruVWyVL-Xdvtl6dwUlPPAZO9YAW_I8bJPDl5Ta_q1SFrxpq3-W2tXRWC4e4lC9hmNF9m_GXF9_J0XNSdIlhNXXNOBgEo7Hr-9z7Uzl2mTh_hO-8_0myEcn02pqSvX1StdBdKWCs7gHI0D_bWD7Si8ygXG--J1Ndb93eJ1OdvPMDeuuRp-C7Lxd95f-BLJLwVmPNcyZsLeSdyMdobY05y408bCaZAN_YGMIS6D_uqDtD0R7nwEjxr6XJSaY4I3lPkmEwRKSHjyuCBNik2i1ir94dcES5tFh2wCk87UQeOeRxfsWdIuwig_3Ks2IMwjBa6Ymc6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تاج گردون: آقای پزشکیان فعلا بنزین گرون نکن چون اگه مردم اعتراض کنن سرکوب سخت‌تر میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/143027" target="_blank">📅 15:12 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143026">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
چین و امارات بزودی یک رزمایش مشترک هوایی برگزار خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/143026" target="_blank">📅 15:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143025">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYmQDkHQ-m43rv5vJbNVqtQS_oLvlKZkJSBwqjMS9RMwThbBFIzA9Z0yk0tj_n0vQFioUWvS9LEA9zBETLxM4uccmK7a-pypMLnUwhtDao60lYTUdD_Hy0DuI3nB93V2ybnzfnHQZ7ZPTfEflJPt9WL-yA2Kl0zMbfPporhtTDxoHSaNUix8aqM4Nm-e3EEVXf9yGS178QvC-nqqpfvFeb9YNPprZqwZwjSo2Bs-3U-rVl7m1rNkCvZXv0JS4kHq4YB45uD9N0Jz6VsIPsofmgmCgjZOZ_cHL1_9bUOkmjZ13fKmPZzgD_-dd47vRzwbqb5tjTKkQ3T_VUGZ4JaAhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: دستور دادم قیمت گوشت چرخ شده برا خانواده های کارگر آمریکایی ارزون بشه، این در حالیه که تو دوران بایدن قیمت گوشت خیلی سریع بالا میرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/143025" target="_blank">📅 14:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143024">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
طراح طرح جنجالی مجلس: بر اساس ماده‌ی ۱۵، همه‌ی
اشخاص حقیقی و حقوقی ۳ ماه فرصت دارند تا فعالیت‌ها، قراردادها و ارتباطات جاری خود با کشورهای خارجی را با سازوکار جدید تطبیق داده و در سامانه شفاف کنند
🔴
جزئیات نسخه تازه مصوبه جنجالی مجلس: تولید اثر هنری بدون مجوز از نهادهای قانونی کشور، موجب ۶ ماه تا ۵ سال محرومیت و دو تا چهار برابر هزینه های تولید اثر خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143024" target="_blank">📅 14:49 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143023">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
پزشکیان: قیمت بنزین 130 هزار تومان است، چه کسی گفته است باید آن را 1500 تومان بفروشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143023" target="_blank">📅 14:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143022">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
سخنگوی دولت: درباره قیمت‌های جدید بنزین هنوز تصمیم نهایی اتخاذ نشده است
🔴
پ.ن: اونجای آدم درغگو
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/143022" target="_blank">📅 14:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143021">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879faa5c66.mp4?token=dlKd0TYbV1lPLFl2Lt05thzlrYeMOpqTiuY8SJKPRu282KNGZf9opo74fkWHphi5UDFrRJEB5BlhnCjcBlRz7Tqja2JgsWucP-9ut-XDXQaPcyD3qVR6qEukNXw3ucicdeTpyHxmmhWNoMZrAv2UgMY2RaOwRerzki9SqmfsmLUTffdymA9f12fGFosaeJTmaBYaUVZ21hq48xB69OVcvkkP-IWhLesuWu3EnJ8MK0Zev4riD98CfWRY04wzSVhoAx0PngUy_Qqmi5OUG3shocFzYJQ0bzpZ3M1g0BsdeDZEfe3HqGHU448pFWRW3M0KKwNBUS86AB83ZUaRwv6tfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879faa5c66.mp4?token=dlKd0TYbV1lPLFl2Lt05thzlrYeMOpqTiuY8SJKPRu282KNGZf9opo74fkWHphi5UDFrRJEB5BlhnCjcBlRz7Tqja2JgsWucP-9ut-XDXQaPcyD3qVR6qEukNXw3ucicdeTpyHxmmhWNoMZrAv2UgMY2RaOwRerzki9SqmfsmLUTffdymA9f12fGFosaeJTmaBYaUVZ21hq48xB69OVcvkkP-IWhLesuWu3EnJ8MK0Zev4riD98CfWRY04wzSVhoAx0PngUy_Qqmi5OUG3shocFzYJQ0bzpZ3M1g0BsdeDZEfe3HqGHU448pFWRW3M0KKwNBUS86AB83ZUaRwv6tfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ساشا سبحانی، پسر سفیر سابق تو ونزوئلا: اگه باباهای شما کارگر بوده و هیچی نشدید به من ربطی نداره، من دارم عشق و حالمو میکنم و بسوزید و حسودی کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/143021" target="_blank">📅 14:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143020">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eee4976979.mp4?token=ocDd8D05H9LS9mzhYVe2D2FDXaCcC7LK232mcq-TAbQe_Peo-FY5QwdDr1FL9fwZLSAClNLovr6OTRkYW10_UJrxchuQgzhxBrTQ_M8grZYmgX8msNehCH4Zejtzn_4VS9AUMTEk6LrME7Gz13gSha2i9FzCAzD-CKuGDTPfP6tmvqTgJvONASnzIA34LKtbuyF2QB-MxYzeMws6vuE7EiHxGaezx5OLwn5VEyjLjLgUZ4SS86jOEUsexu61a1Xc6WoBJ5t1D1JKOexCsvw7ke_a-YoR9f00LziCizLQRugyja-PD4zVsGQqsjcHUKOii1d7Xi876XEE6SnLZBIlVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eee4976979.mp4?token=ocDd8D05H9LS9mzhYVe2D2FDXaCcC7LK232mcq-TAbQe_Peo-FY5QwdDr1FL9fwZLSAClNLovr6OTRkYW10_UJrxchuQgzhxBrTQ_M8grZYmgX8msNehCH4Zejtzn_4VS9AUMTEk6LrME7Gz13gSha2i9FzCAzD-CKuGDTPfP6tmvqTgJvONASnzIA34LKtbuyF2QB-MxYzeMws6vuE7EiHxGaezx5OLwn5VEyjLjLgUZ4SS86jOEUsexu61a1Xc6WoBJ5t1D1JKOexCsvw7ke_a-YoR9f00LziCizLQRugyja-PD4zVsGQqsjcHUKOii1d7Xi876XEE6SnLZBIlVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خواهر پژمان جمشیدی: برادرم جوونه و با دخترا حال میکنه و نوش جونش، عین بقیه جوونا داره عشق و حال میکنه، زحمت کشیده و باید بکنه
🔴
پ.ن: منم جوونم و دوست دارم با خواهر پژمان عشق و حال کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/143020" target="_blank">📅 14:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143019">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4291f4458.mp4?token=GJwXQKSQZ3GUBuJXsuYexIWZK7dP_TJxFunHQA7nhel1irdm7kApIgnAUWLl2FQRCvoFD58Do1fiu1nz0i7iAi53hUHVUF0rLOVVkU3uZhuKVQMygZOvQ2OgSFNOx4tLXulgCEM2MJJQim0e12rRYmITKDpRZCotNnCwEW-9D-DC-qCdUJbAVM3lkMwNP0XqPwX2N5idJBhElqGBe_sHl0ebvHhuoBsKpwt87Xm7FJI_BQXM5ZVI_-ZSpC_2nNLb9OmHCKYEGC6I0_tXrP8_w1CfnuTQZXbYW8OLo-ypmrQ3HX-Xvu1YNJgQOZIYk86k2uqg1rBeNcVnEBM9Z41HpWfYim_rIe-ffRRsJoyNMoffGJC1dph9XqCUU-5-Xi7bn0tn4Pd4y_kWCxiN1esXNADczGHI1LIX2WOgKlVIX1KgUxF54mnYPtSElhU9ssrvDTqyLmd6Cktn2jYivKzakoyP2cKCpz757N7EQo5AeU-zP-JLp6sz6mmxLaOPiNQQwKrBy-kEdG93UL62lqnNMoAHEM14yFb5MAE9oLcIxMq-2QM0QCofuqKyQ0UfGCQtcTF3qVORN6aQ0xva8fUQSGInHrhKKOaBsgl9pIGLUUUqe5IAO5CFJLciHM1PeJlKQdSbv0sCLqDivEcWa9kvraVPBvYxfDBCTdLtH0eHdRk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4291f4458.mp4?token=GJwXQKSQZ3GUBuJXsuYexIWZK7dP_TJxFunHQA7nhel1irdm7kApIgnAUWLl2FQRCvoFD58Do1fiu1nz0i7iAi53hUHVUF0rLOVVkU3uZhuKVQMygZOvQ2OgSFNOx4tLXulgCEM2MJJQim0e12rRYmITKDpRZCotNnCwEW-9D-DC-qCdUJbAVM3lkMwNP0XqPwX2N5idJBhElqGBe_sHl0ebvHhuoBsKpwt87Xm7FJI_BQXM5ZVI_-ZSpC_2nNLb9OmHCKYEGC6I0_tXrP8_w1CfnuTQZXbYW8OLo-ypmrQ3HX-Xvu1YNJgQOZIYk86k2uqg1rBeNcVnEBM9Z41HpWfYim_rIe-ffRRsJoyNMoffGJC1dph9XqCUU-5-Xi7bn0tn4Pd4y_kWCxiN1esXNADczGHI1LIX2WOgKlVIX1KgUxF54mnYPtSElhU9ssrvDTqyLmd6Cktn2jYivKzakoyP2cKCpz757N7EQo5AeU-zP-JLp6sz6mmxLaOPiNQQwKrBy-kEdG93UL62lqnNMoAHEM14yFb5MAE9oLcIxMq-2QM0QCofuqKyQ0UfGCQtcTF3qVORN6aQ0xva8fUQSGInHrhKKOaBsgl9pIGLUUUqe5IAO5CFJLciHM1PeJlKQdSbv0sCLqDivEcWa9kvraVPBvYxfDBCTdLtH0eHdRk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو جدید از زلزله شدید چند روز قبل کلمبیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/143019" target="_blank">📅 14:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143018">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏
👈
استفاده از متانول در بنزین تولیدی ستاره خلیج فارس تایید شد/ احتمال افزایش خوردگی در برخی قطعات خودروها
‏
🔴
مدیرعامل شرکت نفت ستاره خلیج فارس استفاده از متانول در ترکیب بنزین این پالایشگاه را تایید کرد.
‏
🔴
انجمن خودروسازان ایران پیش از این در نامه‌ای هشدار داده بود که استفاده از متانول در بنزین سیستم سوخت رسانی، باک، فیلتر و پمپ بنزین، لوله های فلزی، واشرها و قطعات پلاستیکی را دچار خوردگی شدید می‌کند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143018" target="_blank">📅 14:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143017">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
الجدید: نخست‌وزیر لبنان، نوفل سلام، تأیید کرد که هیچ تاریخ مشخصی برای دور بعدی مذاکرات بین لبنان و اسرائیل تعیین نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143017" target="_blank">📅 13:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143016">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
پزشکیان: جنگ باید در یک مقطع به پایان برسد.
🔴
بهتر است امروز که در قدرت و عزت هستیم و تمام دنیا به پیروزی ما اذعان دارند و آمریکا در دنیا منفور است، جنگ را پایان دهیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/143016" target="_blank">📅 13:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143015">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
نخست وزیر عراق: برخی گروه‌ها سلاح خود را تحویل داده، ارتباطات سازمانی خود را قطع کرده و به حشد الشعبی پیوسته‌اند؛ با گروه‌های دیگری نیز در حال گفت‌وگو هستیم
🔴
هیچ قصدی برای رویارویی نظامی با گروه‌های مسلح وجود ندارد
🔴
اجازه نخواهیم داد این کشور به عرصه تسویه‌حساب‌ها تبدیل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143015" target="_blank">📅 13:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143014">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
عضو کمیسیون برنامه و بودجه: مشکل بازار کمبود کالا نیست، بلکه گرانی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143014" target="_blank">📅 13:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143013">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
اعلام نتایج اولیه آزمون سراسری در اواخر شهریور
🔴
رئیس سازمان سنجش : تلاش داریم نتایج اولیه آزمون سراسری و پذیرش دانشجو- معلم سال ۱۴۰۵ را  اواخر شهریورماه اعلام کنیم سپس یک فرصت یک هفته‌ای برای انتخاب رشته در نظر گرفته می‌شود و  پس از انتخاب رشته، مراحل معرفی و مصاحبه رشته‌های دارای شرایط خاص و شایستگی  پذیرش دانشجو – معلم انجام می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143013" target="_blank">📅 13:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143012">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
یک سوخت بر: اینجا تو بلوچستان نه شغلی هست نه درآمدی و ماهم مجبوریم بنزین قاچاق کنیم و الا زن و بچمون از گرسنگی میمیرن
🔴
حکومت ول کرده مارو و پول نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143012" target="_blank">📅 13:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143011">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
اختلاس مدرن مسئولان نظام و توله سگ‌هایشان
🔴
30 میلیارد دلار ارز از بیت‌المال به چند شرکت داده‌اند تا خودروی چینی وارد و با ۲ برابر نرخ جهانی به مردم بفروشند؛ با همین پول میشد کل شرکت bmw المان رو خرید!
🔴
فقط مدیران خودرو ۶ میلیارد دلار گرفته؛ تا از شرکت چری که کل ارزشش ۷ میلیارد دلاره خودرو وارد کنه و سوبله توی ملت فرو کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/143011" target="_blank">📅 13:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143010">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
سریع‌ترین ستاره کهکشان راه شیری پیدا شد.
🔴
یک جرم کم‌نور که به دور ابرسیاهچاله «کمان ای»، ابرسیاه‌چاله مستقر در قلب کهکشان ما می‌چرخد.
🔴
این ستاره که S301 نام دارد، در سریع‌ترین حالت خود به سرعت حدود ۲۵ هزار کیلومتر در ثانیه می‌رسد، این یعنی این ستاره با سرعتی بیش از ۸ درصد سرعت نور حرکت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/143010" target="_blank">📅 13:22 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143009">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bab4f4f325.mp4?token=moapf8Qip4kOMJgEAv5ICvas8LBGSf4_9pHG3y8TCuw4c-34tyJvgLBujJXO0HYprtsoprgtYijejoqAeDuLx-EntFFpBIPrBlKLmk5SlKEvi5Hos18M4xeLcLy_HLX3S4oOwY5DQB4zrnIVHZKBvAOOziu2HTHPZuxtUGPjN4J-WTdpZRhIXRh3Ae1rxdeYji1G5G2jdjKvyBTJue5JLC0MJi2DAN7KVZ0-ZoDmmPK2B3ZeY24whv44JDN0iINqeVz3Q84WlBBF2Zq7a-3BMgW3aqBnl3JLUAsgNy4XLQlJezDEBGGsa5qI7JBw4v3VXbwuH6_lfVA_GLmNUgnhQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bab4f4f325.mp4?token=moapf8Qip4kOMJgEAv5ICvas8LBGSf4_9pHG3y8TCuw4c-34tyJvgLBujJXO0HYprtsoprgtYijejoqAeDuLx-EntFFpBIPrBlKLmk5SlKEvi5Hos18M4xeLcLy_HLX3S4oOwY5DQB4zrnIVHZKBvAOOziu2HTHPZuxtUGPjN4J-WTdpZRhIXRh3Ae1rxdeYji1G5G2jdjKvyBTJue5JLC0MJi2DAN7KVZ0-ZoDmmPK2B3ZeY24whv44JDN0iINqeVz3Q84WlBBF2Zq7a-3BMgW3aqBnl3JLUAsgNy4XLQlJezDEBGGsa5qI7JBw4v3VXbwuH6_lfVA_GLmNUgnhQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله هندی‌ها به کامیون‌هایی که گمان می‌کنند حامل گوشت گاو است!
🔴
ده‌ها راننده کامیون تاکنون جان باخته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/143009" target="_blank">📅 13:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143006">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H1tANR9EtM8djW1RVQMPI4LQ-5HJrTr99FWYhPQTqIYAZ7mfMEM44CsXaDTIPy94sSJH2R8vPH0X2PKzBhHqa6SqccHGYN9b00wbz2g2t0Djka_g7jERK2y9UOtEBGcpUOsKj2XO5gE8E14QEzN5l552-nrzx19b-VWnDuVFxojHupPn9-mwm2ZWQACpIAUbDyuu3oJuf6u2gOg9PON1Hk1gXk9imKhIml8XQTVHO2cV282-w46XZ-TqS0pAQjhaoFoVWVs0xcX89nlbX2k73KhBNH2I0_K_knyDIdBov_Q3NWhYgu_5OtPa1a9wYaDoUb5yNwawd0KqsnIwfOxLOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LrJIh_6X2ViAuNjA8P2CLcghbOTr3IGaZ8SqaAP9FP43myrcu4bc8_ZDmmVV_GKEKKqSc870zK0jgQf49LC1gVGhbL11P0TMl-y6-_JZJnAXCLDpoUMw2Y8mpSS6w7mfav995n-SqIsYFyoSKCDETB7Z1d3FwqYo5nciZrpKSFAW56fdmRpHSEa27_xMcmnngJ3jpvxqE9OEeX432hriIGsMNuwZN2R9eE4S3fVr9sl99LOo_pOfsvQWshg2qvACrtNEcXyzEvYTFeqW2-ieoAzVVq-AmlO8mRAo9gFVwZJgX8u1RQB0NAF45ZV6CKnXmRQgdbRxHx4zxfBFzWFnGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yloya2fvrplw9vyF6RcsndoBrUEBXvTt68h3rba_uX51jVBKLQAccod9VImQPkvCa6z7XDSIFpCt8xVSZ6GAxC3svM0OE016Ip7tlkOTs9DH-p_p5ODxrt0SCVGPOsOarXk4JNtc9FMtLnGUuNexJWvORUm6w60ZHVWJ4Q60zbkDEl7gumAylAZ3PbYi0k-BH43hPUN-yV2ykzYkkd2ChjHH5mfeEMkItgCH7nyCXwmvmQjbbBHZboRwfcvGbzoMa9KIBYwwerbQot03J1qFmTEV8zLb1pTblxk_J1TkY0d8qc0oliQH3Nt-WHKJEfJPzqmmsr_CUZc0O4ru-KJNMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143006" target="_blank">📅 13:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143005">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnAEHjY2tXptNB-GSLwNX5aXyj67cbK7BKNG7ba1s_oMJ6SLkHU_t7-W4837Ec8vyZrRogtcGeIU_p8jnAOVbyPdr5PNT4ImeoTXqVm3WbD6CkA2F15UysVCObOD-nPEIXBU35TgJvYfRHlS27ae0uZmsr_0YS_hM2thr5MMwesp-co3IVUCDW6bxn9TVYypmXFbm-8V59Slf0gUoTm4Ub6LK9UstV-9eKnkV36K5LPofrFbXKJwcX6mKNcTLLLXbe4-7iy8aqP0REexmFiDlkldFujADUCNxsu-aNmC62iEUX-xEDSoUiqAi4YOHDN0r6rTa1-Svei6EVQTHU6rIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک تانکر نفتی سعودی از تنگه هرمز عبور کرد، این بار از طریق مسیر عمان-آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143005" target="_blank">📅 13:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143004">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwmapTb0EzaK_2Ek1rtYTfKPMntI6I4m38UQiHD1wzcLUZCasvjXLbTMo66MEMOddaU1Zc_JtfTwm5WwKdoH57esJeio-_-S-_o9BcA970i6I4ooyNGnTBs3geDEnTCTq0lsBo3d0sWI6MmvmbfUW5z9kzeXRtaqGjO0FvaGxrqU0Dj_ZKryIVhwkySv6vVG3nFiMBfuk8J3VxpzpWRDH6INJwokhvyO5yWKFl-A6phNuEBersl-JK8wU-B1rQwrtMGHF2N9VuhkrAoo9X5H2LvIfhoyFQqKKIm0WML5ExcxyRxBG1MJZEUE7ws0uqezwABSL4vEfIwobyqIpeNoOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوسان قیمت نفت برنت در ساعات اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/143004" target="_blank">📅 12:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143003">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
قالیباف: مسیر مبارزه ایران و عراق با آمریکا و اسرائیل ادامه خواهد داشت
🔴
آمریکا و اسرائیل بداند که وحدت بین ایران و عراق هرگز گسستنی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/143003" target="_blank">📅 12:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143002">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
بیت کوین 79000دلار شد
😐
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/143002" target="_blank">📅 12:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143001">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
بیت کوین 79000دلار شد
😐
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/143001" target="_blank">📅 12:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-143000">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d4d99d90e.mp4?token=XdOipTZbMcnA3rSM8KN0u3o9RMVT3W1CJHQXKhUCwFTtpIfVBCQUoYoH48Iqo20iIR-hL0QAAPN4kh_I64Qvn7e5NnWJMYVLt046JLyz4aBpfmao_cNL9Hr1a7Fz86iIJ9TpT6g3YgIGBec4RYeul43shjcfWWHXWcpHLt3b6iRYPSk-wbiebAsdBmmkog-FuTYsMBZGNY83Hi2rzX13SfUgvkvUhQ53b5zbOvKFSXwowpvtEin6HXd99HjXiGmA9TaLUnZTbmTtl7b5FX9M2vyPuYMHltTagX9ipFOMSUESKvycGKKPYo-pVCeSDMY5xm1NExR-BmN0kHPhCrk2VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d4d99d90e.mp4?token=XdOipTZbMcnA3rSM8KN0u3o9RMVT3W1CJHQXKhUCwFTtpIfVBCQUoYoH48Iqo20iIR-hL0QAAPN4kh_I64Qvn7e5NnWJMYVLt046JLyz4aBpfmao_cNL9Hr1a7Fz86iIJ9TpT6g3YgIGBec4RYeul43shjcfWWHXWcpHLt3b6iRYPSk-wbiebAsdBmmkog-FuTYsMBZGNY83Hi2rzX13SfUgvkvUhQ53b5zbOvKFSXwowpvtEin6HXd99HjXiGmA9TaLUnZTbmTtl7b5FX9M2vyPuYMHltTagX9ipFOMSUESKvycGKKPYo-pVCeSDMY5xm1NExR-BmN0kHPhCrk2VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تبلیغ بستنی میهن در کشور امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/143000" target="_blank">📅 12:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142999">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsCRWVJdc4QBvGW3gzT0Zgld5ndYnq4LI_AAqwFFUqbOS_whFwBVoyJwd5yB8twr1L-ekj7329LYbtXg7m37biuTr2sS7ClRDB4JKCQ12Q6-UgsexkG9bSF7oeU9lr5c81KB9Oe8d2XF8nj61Nd3CKe2bvmrSit9Ivt4ai5-7dkGD-yTTNexbmeNiyUx8BeviLjMK9gBmOxI_8YmR6nH2M6Qqvs-DP2TGQQRqNQ1pBP-dIAhtecYoURsoDW8E6YBIApUs9nWhXcjtBbL1M9Gew7viY9GibMcIx8kPKRiOxH5-JJNTO0JRQKw_Fxq6i6m1fXFviI_2siVVH0UcZ_dMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
ای‌بی‌سی‌نیوز: FBI از احتمال حمله پهپادی ایران به کالیفرنیا خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142999" target="_blank">📅 12:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142998">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c16ebc80a.mp4?token=R8DhPlWT2oaoGv90-A0DllutNvy4a65gzYHai70UbXRHFFiHHzSsYwvFy5n3HyjpbagrDIh52mS4z8rZInPrmb-XzTmy1lauup7-PaJeIY9mo-C7h5iQDKp4Lm2-dVSZhvW5i_Kj3rn6-60SvM8XgWyYwYK7efI4ktUj3vuUoBb5IFL0_lpwA7e-l3obqpCqR1OqMKGzZH2CHY0_GyHvu43U10JsO-0li29xBktQzwYqPMTcEuISD_i__5Z-0zQ2InepgDbBTRdTVAKJDN5hBNeahmYHg1WsdvKbbWtfBgDqmiaRsTjdHi-CbEV84BHF52i5iNKhetISztAn2pSmew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c16ebc80a.mp4?token=R8DhPlWT2oaoGv90-A0DllutNvy4a65gzYHai70UbXRHFFiHHzSsYwvFy5n3HyjpbagrDIh52mS4z8rZInPrmb-XzTmy1lauup7-PaJeIY9mo-C7h5iQDKp4Lm2-dVSZhvW5i_Kj3rn6-60SvM8XgWyYwYK7efI4ktUj3vuUoBb5IFL0_lpwA7e-l3obqpCqR1OqMKGzZH2CHY0_GyHvu43U10JsO-0li29xBktQzwYqPMTcEuISD_i__5Z-0zQ2InepgDbBTRdTVAKJDN5hBNeahmYHg1WsdvKbbWtfBgDqmiaRsTjdHi-CbEV84BHF52i5iNKhetISztAn2pSmew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایلان ماسک: تلاش برای بازگرداندن بینایی با تراشه مغزی
🔴
ایلان ماسک اعلام کرد شرکت نورالینک در ۶ تا ۱۲ ماه آینده نخستین آزمایش تراشه بینایی خود روی انسان را آغاز خواهد کرد.
🔴
به گفته او، این فناوری می‌تواند در آینده با انتقال مستقیم اطلاعات به بخش بینایی مغز، به افراد نابینای مادرزاد برای دیدن کمک کند.
🔴
ماسک همچنین مدعی شد این فناوری در آینده ممکن است توانایی‌ هایی فراتر از دید طبیعی انسان، مانند مشاهده طیف مادون قرمز و فرابنفش، ایجاد کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142998" target="_blank">📅 12:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142997">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afZybpBL8fIABJF6rvsSdFcLsQxiAc6D8ygq3YjhAESYJW6I2pDfO99LH0MdhSvxV7qe2OyfCDp-4QScenYGe7EhgvJtfepqFLtB0D6hW3EOytsbsUrmd3FCkRPxlQ3g_IFi90OraxGq6vbBWR39u-FhcuUThVYiM3xRwgmeUURN1YJ0N12T9MTx5ACPWLKydKzRw0kOju-4KXUWz85NpH8rsLDvofqXKVsn4HapzRu18s6gJE7jZlxnM6XteMQHJfKeacHFrkGYoreUM7C1rQyiqPAuHRW4vCeuF4lwOlgUNUs3UlXQwcaRJt3sLqskkQVJfYY5GYSWXt59pbGSfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجید شاکری: پاسخ نظامی ایران به حمله اقتصادی آمریکا ضروری است، هم معقول است؛ هم به موقع!
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142997" target="_blank">📅 12:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142996">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
معاون وزیر راه: هزینه بازسازی پلb1 نیازمند تخصیص بودجه‌ای بین ۲۵۰۰ تا ۳ هزار میلیارد تومان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142996" target="_blank">📅 12:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142995">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/230ca39aff.mp4?token=sWV4J4YSwD3vWW-uM0bRrFBuqEhN-Q_Q3oUYpU4Z013dwgQWBr_A5MH2vrq8F5ZShmaSf0cGuH3K72CRlOTqe2LMiHdT9Fnk5Gnf4ATus978OGa0KIElsR-RDSK777GtuCh5G4tSiXgFwnXaG2N0iH-1o5zrJJbaL2wKa5ii4No9bpgBh4Ab9F6ifFLWiJ15m8B-5j2af8OBJZ6WM3DgszDRJsyafOsUrH4e4kIDjxCqePMPIt3tQIOyJukb28y39XdMPFVESLH4ERykVKEpQLEwi8VIA-MK9hKaZzgE8l4EoEMHNODcTP40_xlDysVE0QlN2fKRoSSnE14dguWi1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/230ca39aff.mp4?token=sWV4J4YSwD3vWW-uM0bRrFBuqEhN-Q_Q3oUYpU4Z013dwgQWBr_A5MH2vrq8F5ZShmaSf0cGuH3K72CRlOTqe2LMiHdT9Fnk5Gnf4ATus978OGa0KIElsR-RDSK777GtuCh5G4tSiXgFwnXaG2N0iH-1o5zrJJbaL2wKa5ii4No9bpgBh4Ab9F6ifFLWiJ15m8B-5j2af8OBJZ6WM3DgszDRJsyafOsUrH4e4kIDjxCqePMPIt3tQIOyJukb28y39XdMPFVESLH4ERykVKEpQLEwi8VIA-MK9hKaZzgE8l4EoEMHNODcTP40_xlDysVE0QlN2fKRoSSnE14dguWi1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از آثار حملات هوایی ارتش اسرائیل به فرودگاه ابوالظهور در سوریه
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142995" target="_blank">📅 12:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142994">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc041fd169.mp4?token=D5Fci2fEjKRPXJy72uWGvRhWcZrWoMryEKHjJbDsHicLEfkhX5OCn_XahFmMNccsUECrDGffXQJxTlB43DHMhsUqLngMEGL3FVikkbQv_Yl-NaBh45Gzka1Rt8OEiQp8vQRHACSZnohMebUOp2-MlD_J3VjP68bBwJmCPFj_FCYJJ4ijN8811dPOrQtSJXjRZuG1ZqAblESmpuG2-JQIqoHSjITAwPjWDcQvLHY5JW3lXKb2bhA9IId1a1VpodpZmMSXvoyG4JljomEvQOVI_aIufBYXOJWWkhMfhqvAd8JMquw6Azbi2bfuG8ihX81OZaqXYFgwqLRAQc0rlpwkUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc041fd169.mp4?token=D5Fci2fEjKRPXJy72uWGvRhWcZrWoMryEKHjJbDsHicLEfkhX5OCn_XahFmMNccsUECrDGffXQJxTlB43DHMhsUqLngMEGL3FVikkbQv_Yl-NaBh45Gzka1Rt8OEiQp8vQRHACSZnohMebUOp2-MlD_J3VjP68bBwJmCPFj_FCYJJ4ijN8811dPOrQtSJXjRZuG1ZqAblESmpuG2-JQIqoHSjITAwPjWDcQvLHY5JW3lXKb2bhA9IId1a1VpodpZmMSXvoyG4JljomEvQOVI_aIufBYXOJWWkhMfhqvAd8JMquw6Azbi2bfuG8ihX81OZaqXYFgwqLRAQc0rlpwkUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم از بمباران هوایی اسرائیل به شهر باعراشیت در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142994" target="_blank">📅 12:12 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142993">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMXqlxYQq4qHMUZrNaXRgO7eelzgkkaEv6Dfsqt9xY4gbVkhcEUwtOE75WptYG9BgXnuYLyDzyIwaV23TdmE7fFKdXn4XI4aK_EOz3nLdHnfEmG5PBiXyF5VgeOnhgcAFQM9mhtN6i2JsQ-Ue3pz03rrBvrBaDbzfDNCkzvuhInQfvv0yh5BH5ZrXbbpPH95-oseFJp45_qxTfe06UIhQ1uJ_XyoYNHHdKy8OGuH1lf8R4utnQr1e6G2oGkxZEKPv8XRYA8gXl2B5bRBJAGnyywG8VBBYVTp1bwk3UUVACEdvgdPyA50AZ_3Z3D7chRcUTvoSGRDGPWNsAt4C18bBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیلی به شهر بااراشیت در جنوب لبنان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142993" target="_blank">📅 12:08 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142992">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
پیشنهاد اینه دولت کافور وارد کنه چون عده ای با دیدن مو هم تحریک میشن
امت مبعوث
❌
امت
حشری
✔️
🔴
یکم ب خودتون برسید تا بتونید زن خوشگل بگیرید تا چشمتون دائم به زن مردم نباشه! وقتی شبیه گوریل هستید قطعا گوریل گیرتون میاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142992" target="_blank">📅 12:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142991">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLJlEZqR-fzEtKlXWA95Y_tPw7zo-wL4q68S3yJC0wGkeec1tMm2PTSR_scpiUP9D8IPO8cxw760RT7t7hwpYUvWkg47qZJuknjPOkFPkcT9HdNkC7Hup3R9SZib2k5PSb194XwxuNaws1DXFfNL_Uw1i_DaDXuWbt5EYnz2aVCxhCn1SRp89v48nogv9oLoX-DKikXWMTqk1PM1B8hcrv7g8Bw6M4OVURah9WIjOgv1O89Xn4Cn-O8MIwkguxfisKzRQZ4-KWYpJZ8eGNHXfl14IvVVd-lvoSNT50HhM5TFhrOmo2pOP_WH71s-CZge6nBcIjLhx0tHQ8UWUHiiJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
میزان محبوبیت روسای جمهور آمریکا در تابستان پیش از انتخابات میان دوره‌ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142991" target="_blank">📅 11:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142990">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ستادکل نیروهای مسلح: پاسخ ایران به تهدیدات نوین ویرانگر و پشیمان‌ کننده خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142990" target="_blank">📅 11:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142989">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jv-Ki4bGH9Hjq5T2foK9qyDpya5qZG0bzaND9ona5lYlQ6N90wR6DprzTtAsGe7onM1Mx71gu-hMawpQE3q9QyOxxVjhJjlIHSUUeLnz8v4Yo0TXHcpQR3WUzSEj-JqYnCZvMPMHCqhgryVujnDzQftiqKvSDxMOMidEuyNOYof0mO9WiXoULpO0ny0FyYgParUO731Rx56yegHaaU5jBfrll8x0775RDiFoy6_Al1zU6PC9RzPxB2WLpacG8Cg00Sp_Gg0wuGWDuEuFQGiRhi6I8UkavwhQC9vgR114tyDCMebj9KPyQ_R6H_fyrs38NN6_HR8v6kNvR_jYZbtaEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری پر بازدید
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/142989" target="_blank">📅 11:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142988">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
قاسم روانبخش، نماینده قم در مجلس:
قاسم روانبخش، نماینده قم، از مطرح شدن طرح خروج ایران از NPT در مجلس خبر داد و گفت این موضوع در حال پیگیری است.
🔴
او همچنین با اشاره به مسائل فرهنگی مدعی شد برخی جریان‌های غرب‌گرا، حجاب را به «دیوار برلین» تشبیه کرده‌اند و معتقدند با برداشتن آن، موانع دیگر نیز کنار می‌رود.
🔴
روانبخش تأکید کرد نمایندگان پیگیر موضوع حجاب هستند و از رئیس مجلس و رئیس‌جمهور خواسته‌اند نسبت به این مسئله توجه جدی داشته باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142988" target="_blank">📅 11:47 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142987">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JkZdR2rFMzcioq3Qyn_AM7M0SfZK0LxyQ2YMmgECTVwM-5-R1ghSxhKQoGcgPWd0-RJ9cTF1l2BjVF2-i1mp529KuxmuBN52CEqSGyDoeLWlVA39owITdm4Bxo7unk4xewEMdlNAE2hz9bC998Abi8SV9lvoZ_G4a18_KUXHyfEx37yMSNOrJJcCKQsj4aPpWGM5Fokyx9ow3IS-Hd_EMmLxwm57AX_aWLjHSAax20KM6fDmhGl-EZ_QPii3_y12CwXeGSfZrbcsruJI2fF47e22V1-F9qxc5a9UnlTWo_T4u17_zm80dSSjADQ22AsiBUoCLJ-ilIEvoVre3CEkkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پالایشگاه نفت پرم روسیه در پی حملات اوکراین حال آتش‌سوزی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142987" target="_blank">📅 11:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142986">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
رسانه آمریکایی سمافور به نقل از یک مقام آمریکایی و یک مقام کاخ سفید اعلام کرد: دولت آمریکا معتقد است مذاکرات ایران و عمان چند هفته پیش شکست خورده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142986" target="_blank">📅 11:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142985">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏
👈
منتشر شدن فيلمى در شبکه‌های اجتماعی که انتقال تجهیزات زرهی و لجستیکی ارتش ترکیه به سمت سوریه را نشان می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142985" target="_blank">📅 11:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142984">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وزارت امور خارجه لبنان: وزارتخانه قبلاً به سفیر ایران اطلاع داده بود که اعتمادنامه او پذیرفته نخواهد شد و ویزای ورود او تمدید نخواهد شد، زیرا او به عنوان فردی غیرقابل قبول (پرسونا نون گراتا) تلقی می‌شود.
🔴
مجوز اقامت سفیر ایران، محمد رضا شیبدانی، در بیروت قرار است در ۲۴ اوت ۲۰۲۶ منقضی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142984" target="_blank">📅 11:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142983">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3m7lkoyAIiwvD-SCzryadLI8slasqyz1z9ByD6-lmg6FbsarWtwLEa0RL3aj0dhN_Z2Wm92-mAn_fyABV2IYg5resFyoHutQRvTR8Wxg8w1mzwHEJ2OnxpWveK4-JOLW4hYEaT6NSaTB0QuoC-_7VUTm48vKrRKTxfv-ofgeIjw-a1zlJ3Sn7DQoWf0xMzbb6u1x7fze8D-sk-JLBAHrQ3lUrJCfq5jcGbZr2CWcVzzaNTeFg0KCsEI4sSXeXI3a1zEO2MOyahfvtxC-Zl6bVQdJgp4Br5GjCF2wisL4F5H40wI2lxNEbVFkUb3LMt0xgQqcm1Chg5kxeB7RSHhSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت بیت‌کوین از ۷۶۰۰۰ دلار عبور کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142983" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142982">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
الجزیره: چین احتمالاً واردات نفت ایران را با وجود خطر تحریم‌های ترامپ به صفر نمی‌رساند
🔴
پکن توانایی واکنش متقابل، از جمله محدود کردن صادرات عناصر خاکی کمیاب را دارد
🔴
در زنجیره انتقال نفت ایران به چین، هر بار که تحریم جدیدی اعلام می‌شود، طرف‌های درگیر معمولاً راهی برای دور زدن آن پیدا می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142982" target="_blank">📅 10:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142981">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MZq4a25YUknI5r_S8wDimrrs5RZreCrar8LhGGBi-NeoIEjHPTlCjGJbFn1aFNRaWX-OVniLV4Lsh31foOGrcz5e3CNDBt57-hfJAHxDAH8qx0DCMyU4Y3sh6deV9vSa6umW08vx1Cs0012w-IBnqOOZTMSE-0YBWgRyD29VII7UQS9om6NmmQJkhHRM1IxK_cKol7C4sHqS4tUXu4ZXhTatTRc_MpbU8hq8VeR1HDpOU4rMNQ5R1Is5OHeg2D9EGTdlFCv67vaRCF2UyT_vfwjuP1V-fIcSbP_Gj2U_D4oKrjQi9KK_ga59O58vNknxoCpFAh9u3Jjr7OSSijUx7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پالایشگاه نفت پرم روسیه در حال آتش‌سوزی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142981" target="_blank">📅 10:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142980">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpQUXo2ufvQeH-cmHf71KcqzIYHkxj5fTO2li1GvDpnc9taCm-zWY4p_mkMATr9CaH1t61ABG9i1YQdmXXyX6vv4LLEmN-lxg2qDvuDeZqDriUhDeVG9zdw4n_1sYt1kpAEyxSiF6FFuRwQSci0goQj0Lyhr2qSMiWsXRq4u-AFawH6Kxx92KRkXUbT1-YAtlDwKttPzvtwIKij6CS1BWvwE0cPqmCMO2yWslI0jNgku2wQUgMFC43SbqigNYe3k_qzB34KMhB59LzWGamjSNxoeID2N1Sl0P_ewaYbvghymWJwgAClicpHqideXCa-572Y9QNcWPdDJlUe_6IzQRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون ارتباطات و اطلاع رسانی دفتر معاون اول رئیس جمهور: در پی انتشار ادعای ساختگی برخی کانال‌های غیررسمی مبنی بر «اظهارات دکتر عارف درباره بنزین ۸۰ هزار تومانی»، بدین‌وسیله این ادعا به‌طور کامل تکذیب می‌شود.
🔴
موضوع مدیریت مصرف سوخت در مرحله کارشناسی قرار دارد و هنوز هیچ رقم یا تصمیمی به جمع‌بندی نهایی نرسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142980" target="_blank">📅 10:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142979">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/964b9429cd.mp4?token=diSZJP8QQXrKIwnu8KccAJGPVUe0seUjsHc4jKzkBicohBLreTiadNgfQSvOif8l98xj1vuqT810iE5AIHY0jihIM6pdfLnx4JEcZiYeeA0IgShcihjY9UJ9ifbZe6vJUOw3Obf1UqQMLDKVWJEtFIkbC41xd0iTryMBCpD0cVAuWl9icf2BvoyPuLcfvVRhSYQKOAfhvUXOLHPJh6F3sc93_AT9ecL2KtKHMq9L7vjw9JpTP7YSdYhcWUaz0V3A7_jpOINi59i6N3CoGRFQVbmDikYaOQZxsqA-3ctelzb3L0tJOb_sLNLu80M8j92v3dUjLjYE1kHki575_1TsDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/964b9429cd.mp4?token=diSZJP8QQXrKIwnu8KccAJGPVUe0seUjsHc4jKzkBicohBLreTiadNgfQSvOif8l98xj1vuqT810iE5AIHY0jihIM6pdfLnx4JEcZiYeeA0IgShcihjY9UJ9ifbZe6vJUOw3Obf1UqQMLDKVWJEtFIkbC41xd0iTryMBCpD0cVAuWl9icf2BvoyPuLcfvVRhSYQKOAfhvUXOLHPJh6F3sc93_AT9ecL2KtKHMq9L7vjw9JpTP7YSdYhcWUaz0V3A7_jpOINi59i6N3CoGRFQVbmDikYaOQZxsqA-3ctelzb3L0tJOb_sLNLu80M8j92v3dUjLjYE1kHki575_1TsDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوش چشم، تحلیل گر صداوسیما: ۵ _۶ تا مین دریایی هوشمند ببریم و در خلیج فلوریدا بندازیم تا این تنگه استراتژیک آمریکا را ببندیم و آنها را به مصیبت بیندازیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142979" target="_blank">📅 10:33 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142978">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTda8wbLafys7awb-sB7ldh05NmF0GA0ltmWbdO0--i2ThVdUw5FHliMTkuZvJpRJvQRkqlYsZYQO1pMQpZT3WrTWaLaOeT2bYOXPmjQN67_QhP59Sc_qkJJWIapIPwz1UV0Md2K52cUKiFP4-_l1UTP3e5g1DkzYlwove0zkXa2Vf6FDImoyekdG-lSnqsSkRUXsCNbrV8jelcaq4WiJUMllkA8Q_ate1q_TQC9ejLxZYd-UP912YR2Q8g0PQkmQxqhji12p08e3jCejML0uLEpRPaQCyneYFM4oOhhxHFqgucM-01YAWLbmUuF4AShwt5o9nrOz9ZDwILbxbBebg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
نیویورک تایمز: پشت تهدیدهای ترامپ درباره جنگ اقتصادی علیه ایران این پیام وجود دارد که او نمی‌خواهد دوباره وارد جنگ شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142978" target="_blank">📅 10:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142977">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
کانال ۱۴ عبری: با وجود هشدار‌های  نتانیاهو، گزارش شده است که ترکیه، دسته‌ای دیگر از تجهیزات شامل ۲۰۰ خودرو، از جمله ۲۰ تانک، را به سوریه اعزام کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142977" target="_blank">📅 10:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142976">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2oThw7S5KDlmAb67Eza9TFEbQSyhBxD_W3tH40oL9wod_Mw30reFZ5N0nUnkA1NkUGphWcbRB4jxqWw_sifyJx5ltorYgPgULc4pNEeSFnpkmfFTn6mQliT35v8-Hrc0uJbK5vNVXrMHRmFqFM6OGgamqH3scKaETWlXzUKHgpL0vRL1d_Zq3PgYB34w_VZnD2BLdK6HyAQnbQKNFMp877P4tokQ5yTD58LjB7855REaBC9Nzd8q-qRnj3uH9VxDrPuEmw96k4BAwt7wLU0ob1QdkH8iorsxTXxf0d-WSWRSHoIsXzWAF_U-pIIOuT5gLdOP8hjnBipJD9m8CFOQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: ما هر چقدر قدرت نظامی داشته باشیم ولی اگر مردم گرسنه باشند و گردش مالی و رشد اقتصادی نداشته باشیم، دوام نمی‌آوریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142976" target="_blank">📅 10:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142973">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af775012e6.mp4?token=mk3fCBmFwNHjj4C6bOwyiz7DUIwZeI60UwREU1EMmHoiPT7F7nTjEHgzA7s0BrVeJpcikpde7R-b4s5DI3-3FDXBVSXj70JdVOd20pzyyXeUX1LHYcfwXYTVGz68dv-tUXKQOeB6TcEL1sZLdDcSH1ZOxDMwR11Y8SbeCB9DpgQc4W_S_izWVcBa8B8v-OEKy20NbokUUmvy1k0zus_AgeMFOOlQV-lsdX80boD4ojaTsaS7dyOZCm3TbbBH-T79kZbKIA3UjDcJZzj2St5NaiOPfZyQ4Gd7qDUmGAFWYxONdNDby17am2tP1WJ8wW26uGfREySHPW0qW_ax--d6UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af775012e6.mp4?token=mk3fCBmFwNHjj4C6bOwyiz7DUIwZeI60UwREU1EMmHoiPT7F7nTjEHgzA7s0BrVeJpcikpde7R-b4s5DI3-3FDXBVSXj70JdVOd20pzyyXeUX1LHYcfwXYTVGz68dv-tUXKQOeB6TcEL1sZLdDcSH1ZOxDMwR11Y8SbeCB9DpgQc4W_S_izWVcBa8B8v-OEKy20NbokUUmvy1k0zus_AgeMFOOlQV-lsdX80boD4ojaTsaS7dyOZCm3TbbBH-T79kZbKIA3UjDcJZzj2St5NaiOPfZyQ4Gd7qDUmGAFWYxONdNDby17am2tP1WJ8wW26uGfREySHPW0qW_ax--d6UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر تکمیلی از حملات هوایی اسرائیل که اوایل امشب ارتفاعات علی الطاهر و مناطق اطراف آن را در جنوب لبنان هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142973" target="_blank">📅 10:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142972">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c0312f82a.mp4?token=VRNfceuYU2Ko3arAuAbuDLVonRuRbq1XiaM0w2GjuaGKjLTkCRMopQIFwSbxRkUNI_L25PEIXaul9IsHJDOfCllJ6JWfEhch08gORKAzmrGK9rF-RdsfGfejPkZNMCi9AzosGkkJKNG2Mgc7JSa-7H9_VCbkJFvnVQviI6WU829dskHRRI1ubiN3ZYgoOMb7WKOIgfbBCu0nusaYIMuAeYzgK17sZbAIszTAsQUxgDQUXWU7Klop5rrJPFyIu-oLLGgx_r-Ghde-19OV_y_8ZRXaUDbbBlKrRD-w1Eh-pBn5YOjD2rdReZduHQYQu2LxC1n-9E-pJjg1h9Tl_2xubw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c0312f82a.mp4?token=VRNfceuYU2Ko3arAuAbuDLVonRuRbq1XiaM0w2GjuaGKjLTkCRMopQIFwSbxRkUNI_L25PEIXaul9IsHJDOfCllJ6JWfEhch08gORKAzmrGK9rF-RdsfGfejPkZNMCi9AzosGkkJKNG2Mgc7JSa-7H9_VCbkJFvnVQviI6WU829dskHRRI1ubiN3ZYgoOMb7WKOIgfbBCu0nusaYIMuAeYzgK17sZbAIszTAsQUxgDQUXWU7Klop5rrJPFyIu-oLLGgx_r-Ghde-19OV_y_8ZRXaUDbbBlKrRD-w1Eh-pBn5YOjD2rdReZduHQYQu2LxC1n-9E-pJjg1h9Tl_2xubw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شورای انتقالی یمن ویدیویی منتشر کرد که در آن ادعا می‌کند حمله‌ای به جلسه‌ای از رهبران حوثی (انصارالله) در استان حجه صورت گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/142972" target="_blank">📅 10:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142971">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
شرکت آمریکایی «پاوروس» قراردادی به ارزش حدود ۲۲.۳ میلیون دلار برای حفاظت از زیرساخت‌های نفت و گاز خاورمیانه در برابر حملات پهپادی امضا کرده است.
🔴
سامانه این شرکت تهدیدات پهپادی را شناسایی، ردیابی و طبقه‌بندی می‌کند و اطلاعات را به مرکز کنترل مشتری می‌فرستد تا اپراتورها تصویری یکپارچه از تحرکات هوایی منطقه داشته باشند.
🔴
نام مشتری و کشور محل اجرای این قرارداد اعلام نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142971" target="_blank">📅 09:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142970">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
رویترز: در تهدید ترامپ علیه کسانی که به ایران کمک می‌کنند، حتی متحدان واشنگتن که در میانجیگری مذاکرات صلح نقش داشته‌اند هم ممکن است در این دایره قرار بگیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142970" target="_blank">📅 09:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142969">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال به نقل از منابع آگاه گزارش داد محدود کردن مبادلات با ایران از سوی امارات بخشی از برنامه‌ای از پیش طراحی‌شده برای افزایش فشار و بازدارندگی بوده است.
🔴
بر اساس این گزارش، ابوظبی قصد قطع کامل روابط با تهران را ندارد و رویکرد خود را بر تشدید تدریجی محدودیت‌ها قرار داده است.
🔴
این منابع می‌گویند امارات ابتدا محدودیت‌ های حمل‌ونقل کالا را افزایش خواهد داد و در صورت ادامه تنش‌ها، ممکن است اقدامات گسترده‌تری علیه نهادهای مرتبط با ایران در نظر بگیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142969" target="_blank">📅 09:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142966">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64d76a6c81.mp4?token=kFc4S_0OKNJuUVHZ1cGgX0eQ91I02MaPm_gbqmdHT11yVNGVtjgDOoo14xMm7jkcmytAKj6PCrsq1h6sb6MIR0NoBgI3abjRMgUjpEVinQEyxTUwYDaXMNHJPU1SVrODUWSpEoAj6wEWXztnN5P2pDyxAkMU-YUI2XECU3zZnv9R_p15FTJBZvZ3mjzZu9pQ3vLg27k-MElnhO-a27dkibUOM6q5balE2eVEV_EPkpBTlCl1KQBI6DUwOBbNfvZggioikfmeASqrFSGr46sh_lezDX7pSINm9scpQhUKFyKm2Ts_yQIH9CBD1xEaTh8QOH5rmBwIUVC9Ljo-yKKBhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64d76a6c81.mp4?token=kFc4S_0OKNJuUVHZ1cGgX0eQ91I02MaPm_gbqmdHT11yVNGVtjgDOoo14xMm7jkcmytAKj6PCrsq1h6sb6MIR0NoBgI3abjRMgUjpEVinQEyxTUwYDaXMNHJPU1SVrODUWSpEoAj6wEWXztnN5P2pDyxAkMU-YUI2XECU3zZnv9R_p15FTJBZvZ3mjzZu9pQ3vLg27k-MElnhO-a27dkibUOM6q5balE2eVEV_EPkpBTlCl1KQBI6DUwOBbNfvZggioikfmeASqrFSGr46sh_lezDX7pSINm9scpQhUKFyKm2Ts_yQIH9CBD1xEaTh8QOH5rmBwIUVC9Ljo-yKKBhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات هوایی اسرائیل کفار رومان و ارتفاعات علی الطاهر در جنوب لبنان را هدف قرار می دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142966" target="_blank">📅 09:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142965">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1g0J0IrLFI-JO4wR8MpAjSOzWZXfs5IfI2EaYXyskqL5prhCojCMT7wNzzaSPB_Pr8CTmnh0rdnuQVHQhsbZwUmW3VF8IMILYbx4g-wDMRQX8hvo36-LO8rIgyhvBXVum-YDpZ3baClJpvHWeTrnTY1BFD9r3NlwgyiOLosqy4bR-mQE5n_AeYi-56B9jyd7YIpAx8fJuewNsbIm-2FqD2xHrpRQDUBkptNLUWxzukczais8J2z9JASJw--5JyO4ThxATazJZLr2nv-Hri39SVXxAR73cBrdR31NakiR837MbOyELTLfu0xZTsEM6zYeDvC3oSHnqaoPUc0IqT4Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این قیمتا مال ۵۰ سال پیش نیست این منوی یک رستوران تو اکباتان تهران تو سال ۱۳۹۹ هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/142965" target="_blank">📅 09:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142964">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وال‌استریت ژورنال: اقدامات امارات علیه ایران گام‌به‌گام خواهد بود
🔴
به گفته منابع آگاه، محدود کردن مبادلات با ایران از سوی امارات از پیش و در چارچوب تلاشی برای بازدارندگی در برابر حملات سپاه پاسداران به کشتی‌های این کشور برنامه‌ریزی شده بود.
🔴
مقام‌های اماراتی اقدامات اخیر را نه به‌عنوان قطع کامل روابط با تهران، بلکه به‌عنوان بخشی از یک روند تدریجی تشدید فشارها ارزیابی می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142964" target="_blank">📅 09:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142963">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
«کپلر» اعلام کرد که طی روز گذشته تنها ۷ شناور از تنگه هرمز عبور کرده اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142963" target="_blank">📅 09:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142962">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
اسپوتنیک: یک هواپیمای هشدار زودهنگام آمریکایی هنگام پرواز در نزدیکی خلیج فارس و تنگه هرمز، کد اضطراری ۷۷۰۰ را فعال کرده است.
🔴
بر اساس داده‌های پروازی، این هواپیما پس از اعلام وضعیت اضطراری ارتفاع خود را از بیش از ۶۷۰۰ متر به حدود ۵۴۰۰ متر کاهش داده و به سمت غرب تغییر مسیر داده است.
🔴
هم‌زمان سه هواپیمای سوخت‌رسان KC-46A آمریکایی نیز در محدوده تنگه هرمز و امارات در حال پرواز بوده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142962" target="_blank">📅 09:22 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142961">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3mOGdCuwOvIMbgvgBqVF3zEwgDeZknCViTYqjwuUPQubw7mXm7tkwmLvZOGWUpedOE7TM0WikpHFjyNKaFquSMCVq_Pe0T_GAf3IZc8hZWp0e6CHy-sAoN6VFgW9nxIoEQgoAcCbq-VUIvracV2aihrX78ffqfmEGWNdr3vactO686hqf7JyhIzAA3KFx6NGkummDFR7mq-ouqZREZJGeO4LLR-vRfc085oRGvkyA1iRdcYM0eQtW_sOKXmmmkEqP9lcFqnjKTHfHZVR5vBgkmzTJy_JmYw_uC-UlT0bBVRPIy4CtImETX7RHjp8Ctyi6c4vhfOrnv0-0dQEjMU2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش آتلانتیک، اوکراین طرحی برای ارسال تا هزار پهپاد خودکار در هر شب به فرودگاه‌های مسکو بررسی کرده است.
🔴
این پهپادها با کمک هوش مصنوعی می‌توانستند بدون کنترل مستقیم انسان مسیر و اهداف خود را پیدا کنند.
🔴
هدف این طرح، ایجاد اختلال در پروازها و افزایش فشار بر روسیه برای مذاکره بود. این پروژه فعلاً متوقف شده، اما مقام‌های اوکراینی احتمال ازسرگیری آن را مطرح کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142961" target="_blank">📅 09:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142960">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fbc460410.mp4?token=gopRPUl-lxFwPMTEuPGmw18_ZjSdetU-GyG-4t3wBH4WuW-wotPCMUrVK4Jj--2Le87IO5YFRnyE0b4eGtXkddKn3KbpO7PgdVe4n34Na2Ppp2Q7eb5FUDIa2cmLkRmqptnKd1rPeT6-6a_3jBgnw0mIjiXaBUVwzLdgeGh8p73d0DgsQzm_5qOoFGL_QU-MYn4HJuDl0HvAMqGkcu-hkxQv7w1zoG9HV0IxSoHrSsyiTX0GqE6QpKSnbhzkPwm-Z8rhrsSLi2xVH2CgVtor4qtng5UvkGsGb_3rTWbpodw1OCSxaNqFmfIscqMhxzalxzKpkn573YO69SpIhgt3DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fbc460410.mp4?token=gopRPUl-lxFwPMTEuPGmw18_ZjSdetU-GyG-4t3wBH4WuW-wotPCMUrVK4Jj--2Le87IO5YFRnyE0b4eGtXkddKn3KbpO7PgdVe4n34Na2Ppp2Q7eb5FUDIa2cmLkRmqptnKd1rPeT6-6a_3jBgnw0mIjiXaBUVwzLdgeGh8p73d0DgsQzm_5qOoFGL_QU-MYn4HJuDl0HvAMqGkcu-hkxQv7w1zoG9HV0IxSoHrSsyiTX0GqE6QpKSnbhzkPwm-Z8rhrsSLi2xVH2CgVtor4qtng5UvkGsGb_3rTWbpodw1OCSxaNqFmfIscqMhxzalxzKpkn573YO69SpIhgt3DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهرک‌نشینان اسرائیلی یک سنگ‌بری را در الخلیل به آتش کشیدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/142960" target="_blank">📅 08:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142959">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
از دقایقی پیش کنکور انسانی، ریاضی و فنی آغاز شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/142959" target="_blank">📅 08:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142958">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sg-W-T05oFGxgr4_caaxJp-UvDxcTQatXJLJFsyMn39HUYCvAuzhNym4zQRBFyWKtxw6bToJjVYNUgUb75EGev7Ld-Be4TpejkiBQARBMAOwNHAJHS7XWfJ4LG8u1U-KX5Hyk_2y5CjOT0ODgT56qVuEwPf-5tU2aJDF5_K_128BRvFwhuEuzG0r21skUrNK-0iQ8POXhmUotSucCLQ6jbnm4ftCOPt_m0Bzgw-2qvR3Rj3YzNQFQV9Qwd6ElI1wG1b_FY6zUYjQ2gByN-0oTyH8XrHrVpRWOUTTgoLUVi0QwSuS4vo5tZw61xfaWK4zlIZblMv3oITCF4m2PYNgPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چین از آمریکا و ایران خواست با مسئولیت‌ پذیری رفتار کنند و برای حل اختلافات از راه دیپلماسی استفاده کنند.
🔴
لین جیان، سخنگوی وزارت خارجه چین، تحریم‌ها و فشارهای آمریکا علیه ایران را مورد انتقاد قرار داد.
🔴
این واکنش پس از آن مطرح شد که دونالد ترامپ تهدید کرد کشورهایی را که از ایران حمایت می‌کنند، با تحریم‌های شدید روبه‌رو خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142958" target="_blank">📅 08:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142957">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
روسیه: فقط تهران درباره مذاکره با آمریکا تصمیم می‌گیرد؛ ما بر هیچ‌کس فشاری وارد نمی‌کنیم، چه ایران باشد و چه هر کشور دیگری
🔴
آنها خودشان تصمیم می‌گیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/142957" target="_blank">📅 08:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142956">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
یمن (حوثی ها): از عبور ۴۸ کشتی متعلق به عربستان در باب‌المندب جلوگیری کردیم؛ ۸ نفتکش را هم هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/142956" target="_blank">📅 08:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142955">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1263ed070e.mp4?token=SJRy5MOzPP2uCGjxxKRiTOGisB9rx6vgRBthdxo6ecyrET3awJuEYikJPYlgGuFRQFbYGhEpN6fWkLsZvE_F-zAlCnjGjDFI8k2OuNtis5f9Z7ehIoynNDAlX_VeZXQ3GOWB8ctTdd5eIdybOKWF-GIW2We0itBGsJ-fL05C7Dqsi4TeqiLRfQ4N0UMNCEIbcLKN_Ai9RR07i0jZ-nTxGDm2rF-BGDzm9HOa_TUtnyOtlElGO7dCBFRrfumBeS087wWrKYrAHC7EdnOPimb8kEGhb8pscLYq07XDFygG8pAeRxjSUHOo9fKLJetNEpHhNu8mXN_LoGiSHSz7bPthaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1263ed070e.mp4?token=SJRy5MOzPP2uCGjxxKRiTOGisB9rx6vgRBthdxo6ecyrET3awJuEYikJPYlgGuFRQFbYGhEpN6fWkLsZvE_F-zAlCnjGjDFI8k2OuNtis5f9Z7ehIoynNDAlX_VeZXQ3GOWB8ctTdd5eIdybOKWF-GIW2We0itBGsJ-fL05C7Dqsi4TeqiLRfQ4N0UMNCEIbcLKN_Ai9RR07i0jZ-nTxGDm2rF-BGDzm9HOa_TUtnyOtlElGO7dCBFRrfumBeS087wWrKYrAHC7EdnOPimb8kEGhb8pscLYq07XDFygG8pAeRxjSUHOo9fKLJetNEpHhNu8mXN_LoGiSHSz7bPthaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انتقال عمران‌خان، نخست‌وزیر سابق و زندانی پاکستان، برای درمان به یک بیمارستان خصوصی در اسلام‌آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/142955" target="_blank">📅 08:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142954">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ترامپ: ایران در وضعیت بدی قرار دارد زیرا نرخ تورم به 300 درصد رسیده است و حقوق ارتش خود را نمی پردازند.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/142954" target="_blank">📅 02:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142953">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ترامپ: ایران تعدادی موشک و پهپاد دارد اما توانایی ساخت آنها در مقایسه با 5 ماه پیش بسیار پایین است.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/142953" target="_blank">📅 02:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142952">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ:
ما ایران را در بحث نظامی شکست دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/142952" target="_blank">📅 02:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142951">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ترامپ:
هیچ‌کس نمی‌داند چه کسی ایران را رهبری می‌کند‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/142951" target="_blank">📅 02:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142950">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6a2752a41.mp4?token=s6EflDUM5Sr6jysbQ2kQBitE6bywTYXmFWTxAynTUeud6qIK6-gxyz-vWoLg6ALva0CS3zQ9JlsCk2iUBvpvErEy6icZbdBb137iEEM62a6GO7FEls35GXhyuvAule7t-ihGXrHAy-YT50RfPQC5vpBmRCKI9p4j14_eEr7TQWPrrUxY6MjS6C4AotwX1QUvktNTjzKDb6qXfMR-LvylGO2uoW8Z7f9I6JuGz6XQjrGLWINc5h8ApgzLR9b3tB4_axo-d78EYDueHs4UeW3io961KskcBvAL0fb8U0TtADOyInu2-0CnmEB-bd5m8JMuCCON8tC4OAsrPIoadufHtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6a2752a41.mp4?token=s6EflDUM5Sr6jysbQ2kQBitE6bywTYXmFWTxAynTUeud6qIK6-gxyz-vWoLg6ALva0CS3zQ9JlsCk2iUBvpvErEy6icZbdBb137iEEM62a6GO7FEls35GXhyuvAule7t-ihGXrHAy-YT50RfPQC5vpBmRCKI9p4j14_eEr7TQWPrrUxY6MjS6C4AotwX1QUvktNTjzKDb6qXfMR-LvylGO2uoW8Z7f9I6JuGz6XQjrGLWINc5h8ApgzLR9b3tB4_axo-d78EYDueHs4UeW3io961KskcBvAL0fb8U0TtADOyInu2-0CnmEB-bd5m8JMuCCON8tC4OAsrPIoadufHtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ درباره ایران:
ایران به کشورهای نیمه بی طرفی مانند عربستان سعودی، قطر، امارات، کویت و بحرین موشک شلیک کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/142950" target="_blank">📅 02:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142949">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ترامپ: نیروی دریایی و هوایی ایران را حذف کردیم و توافق آسان نیست زیرا رهبری ایران را حذف کردیم‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/142949" target="_blank">📅 02:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142948">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ترامپ: اگر ایران سلاح هسته‌ای داشت، از آن استفاده می‌کرد و اسرائیل و کل خاورمیانه را نابود می‌کرد.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/142948" target="_blank">📅 02:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142947">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0583bdb8b1.mp4?token=nHIIsBaGdSGyWLk8m-tn5G7tFXo5lmUp2H0LpAH_pBTvsucMRcyhahFKDBj2Am1KiXGBFQHeOR49ItmaijmXvgZvk3lKsFBay9TviAZxRTLT2THBlQLHA4UbezBACw3iHTYJKM9WG-vi0IXut7nFucPpFrSvX0p3u_CkqpcMvIPHReoPmezJC2Opas_PDi8530RjHdfKTa3sjtLNXzcZkoIEntNr9aVB6jHIUnhXUEVlrAcBs-L-aJtnkZTD0p3qy--xByvMysy3DOZ-QeWta3e7wbutNoYq_5Wg9YZx2iW2rfqRNCaf105nZCOErK21FQJkLiaWWaKEPweLxKdh1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0583bdb8b1.mp4?token=nHIIsBaGdSGyWLk8m-tn5G7tFXo5lmUp2H0LpAH_pBTvsucMRcyhahFKDBj2Am1KiXGBFQHeOR49ItmaijmXvgZvk3lKsFBay9TviAZxRTLT2THBlQLHA4UbezBACw3iHTYJKM9WG-vi0IXut7nFucPpFrSvX0p3u_CkqpcMvIPHReoPmezJC2Opas_PDi8530RjHdfKTa3sjtLNXzcZkoIEntNr9aVB6jHIUnhXUEVlrAcBs-L-aJtnkZTD0p3qy--xByvMysy3DOZ-QeWta3e7wbutNoYq_5Wg9YZx2iW2rfqRNCaf105nZCOErK21FQJkLiaWWaKEPweLxKdh1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اظهارات ترامپ درباره ایران:
ما هیچ انتخاب دیگری نداشتیم. من این کار را 100 بار دیگر هم تکرار می‌کردم. آن‌ها نباید به سلاح هسته‌ای دست پیدا کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/142947" target="_blank">📅 02:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142946">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترامپ: ایران هرگز سلاح هسته ای نخواهد داشت و ما کنترل تنگه هرمز را در اختیار داریم‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/142946" target="_blank">📅 01:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142944">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd25da48a8.mp4?token=ivwBcJrMvsS39PqqcgJQuC5FFWbiciw1hZ9dVUGdSOyNnAKZaFvtwPY7A89LMgFYWhNujJdUe-G-1sc9wik-svGBFd5fykTZ4mqhn_CiHHJa31yHTjtByFBdwo6_-VurdZdxX-LVmSkYxX2vHYNNto90_OoqX0kwOHg2YcNbCj-ZjjtKrmSv0IOcsIr6xwM1gekcxs1D1zsSlLQbSFkqhCpJ3lJuh9JiD57rlZPtECCgYjQnGWATk2sK7rqoVMLl6Jv52ZL39Y2jdmG1RyKdfEKZUxRjxECbVY5mIjFsi0IxL6UNCSNVDUYaHFWWzpxrJgTAgrYGZ8EN5gQeo5MOjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd25da48a8.mp4?token=ivwBcJrMvsS39PqqcgJQuC5FFWbiciw1hZ9dVUGdSOyNnAKZaFvtwPY7A89LMgFYWhNujJdUe-G-1sc9wik-svGBFd5fykTZ4mqhn_CiHHJa31yHTjtByFBdwo6_-VurdZdxX-LVmSkYxX2vHYNNto90_OoqX0kwOHg2YcNbCj-ZjjtKrmSv0IOcsIr6xwM1gekcxs1D1zsSlLQbSFkqhCpJ3lJuh9JiD57rlZPtECCgYjQnGWATk2sK7rqoVMLl6Jv52ZL39Y2jdmG1RyKdfEKZUxRjxECbVY5mIjFsi0IxL6UNCSNVDUYaHFWWzpxrJgTAgrYGZ8EN5gQeo5MOjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شلیل دونه‌ای ۴۱ هزارتومن
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/142944" target="_blank">📅 01:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142943">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: روزانه ۱۰الی۱۵ میلیون بشکه نفت از تنگه هرمز(مسیر جنوبی) عبور میکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/142943" target="_blank">📅 01:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142942">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
واشنگتن پست به نقل از یک مقام دولت ترامپ:
ایران «کاملاً ورشکسته» است و ترامپ ابزارهای متعددی در اختیار دارد که می‌تواند طی هفته‌ها و ماه‌های آینده با شدت بیشتری از آن‌ها استفاده کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/142942" target="_blank">📅 00:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142941">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9190ed7396.mp4?token=kepKSY2QpM76JCAk1Der0cy9GuDGDT8MybPfDunk2c1MnlVKb6qvQ8ZGltp1hzXoOAnh-5Y8OZojzZY8MM7UBnxuQp1r_eCUVdmNiuzk_Re0LfbhBpMU9AShSHWMQkCBKODZnKYWJPX8LtUsQBlJGEhNdxpv0M1EE-n-8u2bw71VcR-abOWTkHsMSBz6V8v-_fPW-63dbdyuc5iExcTgCY7W9vl-SBCWnIJowanbNqCcVah2dsTLU4Mc2-etFV86rTux1-scsVoUJbmTyVreV1n52TRaLmoq2JAnKbEPxBMQvvRnQHw-winZvmxdQJQo8wZNqNSvBKNVp1CMW5aA-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9190ed7396.mp4?token=kepKSY2QpM76JCAk1Der0cy9GuDGDT8MybPfDunk2c1MnlVKb6qvQ8ZGltp1hzXoOAnh-5Y8OZojzZY8MM7UBnxuQp1r_eCUVdmNiuzk_Re0LfbhBpMU9AShSHWMQkCBKODZnKYWJPX8LtUsQBlJGEhNdxpv0M1EE-n-8u2bw71VcR-abOWTkHsMSBz6V8v-_fPW-63dbdyuc5iExcTgCY7W9vl-SBCWnIJowanbNqCcVah2dsTLU4Mc2-etFV86rTux1-scsVoUJbmTyVreV1n52TRaLmoq2JAnKbEPxBMQvvRnQHw-winZvmxdQJQo8wZNqNSvBKNVp1CMW5aA-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
‏قالیباف، ۱۰ تیر ۱۴۰۵:
‏اگر به سوئیس نمی‌رفتم ۱۲ میلیارد دلار ایران آزاد نمی‌شد.
🔴
‏همتی، ۲۹ مرداد ۱۴۰۵:
‏یک دلار هم از پول‌های بلوکه‌ شده ایران آزاد نشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/142941" target="_blank">📅 00:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142940">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RpmwN1hcdMKFpX01s_ZXLQj_sX4RB1SDzIBBB_qEPXf5bSFWE1MDQ3Ao6gBmgeL7JmB_tWCwFE5upP5A55cYdzo1rnT0TxejEPcT3GJh7HiKU1xfDw5ApZZNsXFZogczxKiE91te6VRRCx5zhRIzLZ5anX26Ceg2Bp685K5UdSfGegKXjeBqBn_r96q17goJekMroK1rQ1CnkUo3x6xWFtvmLxhgIexYkY2WkqSoo0D5sgxuySv_XgMR-7mDp9UddDemspQ98M-aRveZWMgsg7K1cKZeCRaFuv1e2UERC-zV1rHxj8bsDivJasqET9a8bHJ0iPAuR47HkaEDsuv1hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال 14 اسرائیل: مجتبی خامنه‌ای «
ایزوله
» شده و سپاه کشور را اداره می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/142940" target="_blank">📅 00:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142939">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
نشریه موندو: همسر رونالدو بصورت پنهانی با یک نفر دیگر در ارتباط بوده
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/142939" target="_blank">📅 00:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142938">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFf_Sskt3JIH0Af3Mv4PxDqf8bCJlBOYjFCtJfysAHsVTMr6Gn2s4TBwYNlImDiCf5SEdAVPi72Pe283usfEjxsgDbcISljPDH7LAQ6uB_4Dr6EwfbV6XTh7xekuq9PKyE7Ppsz1vKQC3OINm2fNX3naHglN3_BYcarENSeiOa7Yr2pBMDUDPrdbyU5AXwBF56-Eu4QUI7fdkfcvCPtKITMgKfp9vX5xZM8maY89hnVrpWq67QFPQBzdi2VEQprRaOEdpUjaR1aQhZ8GuPKDrnHzDRAmzvVOl_Cv2hiB_YE6XBfNItSQ2hshkZK8tgaK2gP3ZXmuWs7_xOFUK7tPZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نشریه موندو: همسر رونالدو بصورت پنهانی با یک نفر دیگر در ارتباط بوده
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/142938" target="_blank">📅 00:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142937">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
الحدث: محمدباقر قالیباف از بغداد خواست تا به طور مخفی یا موقتا، سلاح های سنگین جمع آوری شده حشدالشعبی را به ایران متقل کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/142937" target="_blank">📅 23:59 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
