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
<img src="https://cdn4.telesco.pe/file/akrNT6MUbyo4zgosE-HIRwpsjKINJds9zmQl1EFAETxfUz0GOaC756n4o0k0rMaQi3CJV9MToDWbdaCiWNl3BrWfhhMcigAA0mVksAkNYElSBdaHXG9ZdbKAJfGhsIBh2fRNW4cdNxgdk7r2tigzuDPhVHxGKEcLFWTV5sZm8U0iOU_MEfcJ_TO-4ZcCziRMASitLu6guf4gZFjODh1xDDgYMMFbzpzgRSXWDlm_Ff6rl7-w2IyN0ZhBJhihM8on4Cz-IN15iH5-2JUaOuNHplIXeJ_JHfd3vUrbfJ48wCHhnCYXDK_ccW_S1KyN5WIPIKDOmtDujEC-t0dMH9-Cpg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 21:21:28</div>
<hr>

<div class="tg-post" id="msg-436235">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🎥
کفن پوشان پیشوایی جانفدای ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 639 · <a href="https://t.me/farsna/436235" target="_blank">📅 21:16 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436234">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZC4rfBzbPolocj64kXbluzEBkkGVxd9v0Q3NWEhfHkXwpagAcncw6yURO8dR6oaR3XgANYHAPlv2q8GPWSMqk9G1WZc4rEdwtK8_2kgWjhywgkLojdw39z6_rxXubQFUa-D3WyXf0EbdNuUIIAMyDC7Dbeo8d67udRn75yIqMoqEYRvJFvgrAdpjv55c4nsaIOPtU_5Sl7hGvi7qmBlhuhy08ALYSw8AJMn0HfUWLCLGyCCGN6Mr_KM1SCVOHAonPr9Vtn5kW-zVhgA-OcgDDk2NymMmSfoVGW3NO764pW9kpD7Vpb4227SZ5ueLBI8rDmO0B0uX7BSOmo5V688gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه اسرائیلی: وقایع دی‌ماه کارِ موساد بود!
🔹
روزنامه عبری وای‌نت در مقاله‌ای به موضوع اغتشاشات دی‌ماه سال گذشته در ایران پرداخته و حقایقی درباره آن را افشا کرده.
🔹
وای‌نت آورده: از زمان شروع ریاست دیوید بارنیا در موساد، عملیات روانی بر افکار عمومی جامعه ایران به بخش مرکزی مقابله با ایران تبدیل شد.
🔹
ژانویه امسال، هزاران ایرانی به خیابان‌ها آمدند؛ پشت این تظاهرات، «کار عظیمی که اسرائیل انجام داده بود» قرار داشت.
🔹
برنامه اولیه اسرائیل این بود که جنگ در ژوئن ۲۰۲۶ آغاز شود، اما پس از شورش‌هایی که موساد در ژانویه سازماندهی کرد، نتانیاهو به ارتش اسرائیل دستور داد زمان عملیات را جلو بیندازند.
🔸
نکته جالب این است که پیش از این افشاگری، با وجود همه شواهدی که اسرائیلی‌بودنِ ماهیت اغتشاشات را آشکار ساخته بود، جریان سلطنت‌طلب و رسانه‌های فارسی‌زبان اصرار داشتند تا نقش اسرائیل در ایجاد و هدایت این شورش را به‌کلی انکار کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/farsna/436234" target="_blank">📅 21:07 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436233">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-text">دسته‌گل جدید مدیران استقلال
؛
قرارداد ۲ میلیون و ۸۰۰ هزار دلاری بازیکنی که به ایران نیامد
🔹
شکایت کارلوس استراندبرگ، مهاجم سوئدی-موزامبیکی از استقلال که به‌دلیل ارسال قرارداد با ایمیل رسمی باشگاه رقم خورده، حاشیه‌های زیادی ایجاد کرده است.
🔹
طبق آخرین اطلاعاتی که به خبرنگار فارس رسیده، رقم مورد توافق استراندبرگ و استقلال بسیار بیشتر از عدد مطرح شده در برخی رسانه‌هاست و این باشگاه مبلغ ۲ میلیون و ۸۰۰ هزار دلار را به‌عنوان دستمزد مهاجم سوئدی برای دو فصل تعیین کرده است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/farsna/436233" target="_blank">📅 20:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436232">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afa837ee13.mp4?token=kojS-H0Vp64UKqdbxNKLVeDKOcf_VgQUND4sVRdvEMfpp8gwrPKpdARxu_6jNMHCTLc2WrufMPY3ToKh2jHCHHC0ZQLpzKWhsb4uKJJDWf2JNvfNIuVMajAcOM7t6f-_pHekNQ8mJwkjn2HeR97AVvbA6HwT1hAWU5rVXSq5ixv5Nl2elcSULCNTeg_eRrokfauHQV5dd4x0GMZSo-j38NO6yGDBWlW-k_Cob9dyEf3QmVjfPO9QavRd3WGAA6jee-2LoLCOiH1SFjXHjbU9XeXHpGTVxAZSNS5ejbWaAxLEZQYoW-uyNVqES9liN2Xll9ciOylPZGZeqSkbv6zk7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afa837ee13.mp4?token=kojS-H0Vp64UKqdbxNKLVeDKOcf_VgQUND4sVRdvEMfpp8gwrPKpdARxu_6jNMHCTLc2WrufMPY3ToKh2jHCHHC0ZQLpzKWhsb4uKJJDWf2JNvfNIuVMajAcOM7t6f-_pHekNQ8mJwkjn2HeR97AVvbA6HwT1hAWU5rVXSq5ixv5Nl2elcSULCNTeg_eRrokfauHQV5dd4x0GMZSo-j38NO6yGDBWlW-k_Cob9dyEf3QmVjfPO9QavRd3WGAA6jee-2LoLCOiH1SFjXHjbU9XeXHpGTVxAZSNS5ejbWaAxLEZQYoW-uyNVqES9liN2Xll9ciOylPZGZeqSkbv6zk7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهاجرانی: یکبار یکی از دوستان گفت اگر به تهران بروی چکار می‌کنی؟ گفتم پاکبان می‌شوم.  @Farsna</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/farsna/436232" target="_blank">📅 20:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436231">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🎥
روایت دختر شهید دریادار تنگسیری از پیام «مشت گره‌کرده» پدر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/farsna/436231" target="_blank">📅 20:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436230">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5240e3c605.mp4?token=ALWGCpxfAGCwl6rDLgCze6z9EIFxD-UQx8aTS6KjGLsaWWOpnkwSgij9N0MnMDSqcD3Jfcb3nyPBtYvpXqoTBexQP-MM7WIYFXlRtthK7YWE0XfUVeYH6YK6867KjJlQl5XRYGiXO622xaQzaUzhP89gc4UjVJL842f64luDlPK2CadozEgzI2ZEps5C64X-N1ntjyhbfFGvOrpkWqxKvL8bUzmWc5jx4BQRLHmy5r0pYPXWyeE3PmWQ1SkCC9fCRaepmuC8glCy-x3cXHYk3qAQREk2ltDKtv4wQxgjyAcCCfA_z1EnRs1BZtqO2WMHzqZ52cj-ZlGuSGBlTPOkSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5240e3c605.mp4?token=ALWGCpxfAGCwl6rDLgCze6z9EIFxD-UQx8aTS6KjGLsaWWOpnkwSgij9N0MnMDSqcD3Jfcb3nyPBtYvpXqoTBexQP-MM7WIYFXlRtthK7YWE0XfUVeYH6YK6867KjJlQl5XRYGiXO622xaQzaUzhP89gc4UjVJL842f64luDlPK2CadozEgzI2ZEps5C64X-N1ntjyhbfFGvOrpkWqxKvL8bUzmWc5jx4BQRLHmy5r0pYPXWyeE3PmWQ1SkCC9fCRaepmuC8glCy-x3cXHYk3qAQREk2ltDKtv4wQxgjyAcCCfA_z1EnRs1BZtqO2WMHzqZ52cj-ZlGuSGBlTPOkSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهاجرانی: مقاومت و تاب‌آوری ایران و حضور مردم مقابل ابرقدرت‌های دنیا کشورهای خارجی را متعجب کرده است.  @Farsna</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/farsna/436230" target="_blank">📅 20:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436223">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oPDhErKxGXbPG2PBy4ybCMOzv_A1MlR0aNT9l_4omfjim-tczVK222gfh5nyC5Op35loloXMyNZqEl6pmw-U15Vfx6Q4r1Jv7EgVprqbD8ylj0sdzaFAnF6pS-ULMwZyW8XgOkeEP0PSNQ9SQLyz000t8L6KzKYDujWN1VpGJZf7byoLfq3agYv9H2xGJkKtdVZsnLyUw9MpIXV17X3VVfYmKZvAx17plBBH1_uuG2n2OTk8BtHP9KjB4lePNIeBfu1F1lZde4ypMWwnWujA_mVM94I0QMJtTbBkz8TWkjSaapCNR4GlliZYMH5V1A1RNF5iBq5rfxB2DE-bVx4pvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oVB3VASMm_xnvw0wR6ywScnIwzM-1KLzJq0zLICXvBCnN1SSzQF7085Es737RNwX2O1Bme-Nuu_RZ7cK6Hqs_Zh1x-kFwkoFIIyDWNoXqqMfVVMa7HvO8JTRJJQmz-pRJcPx_dutDmWOls2U-KL2O_HXZduw8cwSq3eCriOFTbJrYk-qGJHe7ae2ZqxHxFT9eOeUxV3IvGnJBXEMUol3CKhmPU82py375OVxayGHQ84Z-ZlEHQZ1BDKj5COCYTVf3CrQ8Y6Xjz4s33KVQMaWmyWWFiQMayfGXpAF5c7EloJvvVahH_nW_QH9_UyrAKjpK3CNlvLhlbJT-PYdHvySHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R7lbJbvCbPZSUoxOPpRAhAsloQz9dXN3tfP0h0X3KCqJ6C62_JzgR9yovnOxV_YB81DOcknlHJcNIBwHEHQD7m6o6D-m12wTXSJXEg1WqRc8RS8rWsUjtD4jvcL-r3x0J-TUeH9MLJBD7fVb2jyZKQzotEVYwqRJduWfUBNib2a6gsV7z8ovJcfqaZUaNOSH5rD4a57qt6ayhih5xWRqBsx7xtVUrTjJunemzgGLtXdV4v4CsVQ9kzxnRISGLOOwM5-eSRRjWw1l-27wA32I2GvjOgDHRNOa4eXinTlP1QMlpMDf6Pa4aTbLlVIPPUuN-Ndwuli9ciWukZ23BZU_ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gkXdQwe5CpGj77VDR6sznix6obOYZD-ZvJlz9xduU-JgTPLO-f67kfHCKkaqIJfG1VrQcvZM_rqtPqUiRyV7pt5ZcdLqEXdtfE-WcDGJRwwgXTRrYtKcZcqzyJGkmnB0asKcw-ry6GmIyVE7YFmqxRC7XBdg35Eb32UZygT1Xe3zplso-xe_VLH5bWSIhi5xqUVOCj0KAeEbe_TMHQzFgTbz0HK_eBdeJ0yOPkiZYCCPROY6qCqoJB8GVyJP4g37dkjaEQMwpUt5xdS_NYwX1KjVkpsU-xJEe77QXb6B-Jb6BNqGJPv8mthETp2sZkZc_lCQDUZ9mWhcRNFLomUtSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RnVeayMoTFLMYS7bvj_gCdiIIQ6hV81nglKDzA3DhW-dXdg2pYoVhL-GReEtkO6DEYYKpXYs4lIntbTG_A88UBxVpjo9XKNLxZKWySigDIEWcwKeU_ot-NsJIMEwDWbpsDEypiP6iaWG4QqpvE-n62vddoSA7F1YO8IlAwVLGKh52QJ0feMNyDRF09W0Q22SuSdPxnuaKgeHC3mPwl1nYBIbyQx8pYEd0lC9Y2xutmU8j91MJ2dlfkT28oypwgOoI08AnsuHuB3_8TZv3IEUOCgYJdIwQKdnVl-yl4tlFXJ29Z8PRur7014PMGj2o9ZHXYFDaTS0vpO4w3it41MGBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z7FJ2O8PNVlqfjskkmC4D6p0kndcrCUa1EOf1rilbm1F57gTkogee_g5gUogxIE09kl-D0pqC8hRrXAb58C-MM8aWuJQj4Q8Yc8pvLJ-ejEtF_PLgM0fnVqM2u8A5R4d5py3u92Ba-4p1pFWF74BEFkOGDB5bYcHgLQF_gBZk3JFWXIzHd9D_Stfh_iHUIjTLV5rzqsVgywBKPHE9N2I5U3QL5hgVqXOKBi98eV7xfx9iX2cscABDQkgdiLuR9_1NlznI5b0bK8qcmiIDQAVgaGOPi5U7s1Q_BoXvy2_6VF8rfgqGa4XY4JulxcI97oMZ3R4YJ5ht0lbBmUQOQmDgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nOHSiVmPRed6ts1GKlGY2u8s4a1tPX3Soe3vTnqX0Ex6eWsF5CffX2rDY-lfL2qYIf9WlYpv1B2dF3KQvXxlHBJoYrNADZkqULlxz9k-82JvcoP4BW6y43iMWqwTeNH0ktBE3fSEdvsdr9mGNcwJooOKkpOzVW5Qo2dCaXu1Bkw9mq9KY8iQ_JeZH8UDBMEFsjuQCIsZqmVViUFghoqjKfN9jUPgJl_zDaUcyeunq8SyLz63SEQZm617Kr1HsAyTXzoykkpEscts28HxogxzbfWPA6DJFhDMQ-LNt7n84wCrmEP6JBW8jxWlZqfXX_xM05pfaLyyQcHDpAo0izxLMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگداشت وزیر شهید دفاع در مصلی حرم حضرت عبدالعظیم(ع
)
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/farsna/436223" target="_blank">📅 20:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436222">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مسیر جنوب به شمال تونل توحید امشب مسدود است
🔹
مسیر جنوب به شمال تونل توحید امشب از ساعت ۲۴ تا ۵ صبح روز بعد برای تعمیرات مسدود است.
@Farsna</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/farsna/436222" target="_blank">📅 20:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436221">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVp_GKD1QWlFpevud3G5-7dUa3byoHRJ3v7DS0PGXnG099I9OpkgnQSIgOd2BHeRJdSylC1CZcpoxBWq1AXvPerDpC5m15sFvVQoPHT5OtU339pldLeE7hoOqpzzCHNh3JwzvbxxftQHxV8FKaq0rLZjebka5M5f0oF891yk1LhmJi1XzSdPz-ZWwS941ENzx_3h4QdjUpeS7-valEwcfHQqK4A6tx6ztINmB8Ux9wfhb3KpE3zPW2pK3jx0MORfSV4Y96IHGJ9g8ADuvBS4nlv6OoWz3RjUaV62UyEVpc2fmldzhQ9M_hqX6hPr3vOMoYRGDVkPjYzvJYy5F9hsDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی دولت: تأمین اثاثیه منزل برای آسیب‌دیدگان از جنگ رمضان، به‌جز شهر تهران به‌عهدۀ بنیاد مسکن است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/farsna/436221" target="_blank">📅 20:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436214">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nApdJlrXRk0TbLBGpFRUzA3aA4D96g_iaDmvPrs2kuVHz_UiMVDgzZeLdbzwwVWPQfbdswMzSFPKGajSgIZwmtMAVGSIQvgmEbjcsFuqDGtc1OEYyV5xlLHivm87mgbr_cE9LqpQZwsxuwzSY5OoMFcLRyZnvKnXhLNx2zR3ADMezZhaOS0br7riyn0_l_3ITRhXUV-CloQ9BRD99frO5O_yQpTftN3SmoDdHheDALmXLsRFJG_RRrjcUhVZwY3M6zSgAhwOIBmN3AUuGl9Ndm5bDpm8srKs9RgIJGEYzoMitBQIzEyi5lg9G9bTUUHc_ivcQW1G7hslzjKxLdRf5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PkB2XbKrTn08CNgoaE1u7DijbMGybfHXUi4dEKTjBZwq01q300N9MFmmoJ9mDuX3Zs8ij7TiRnKdMTHL7DBDFxLSBCqTtbHgKatylYpG8CbpmVgSmhJEpKWpCIzKzHZPQ1xSjGBHT0eStKo5NIqz4WqsxYcN2IFKmCc8Xc8LWmdFZWfHIVk5gmHiKTXXVTGB0RFJl0uWjL9G0O4C0M_WrIsviFc3zp7qUBTOQBjvsNEqd2xRcXV3gTvyzCzptrO_J-69VYnlynFRPDyFl3h1IrBO8bd212S_eLeFGXrMf3pmpn5BnRiYclM4k7Evu5tr3wqYcJEHuDcVu3Zxnr8p-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AXl9r47bWhI3we8tk4E1wvEpinRxCYq_wvzKVkxKu1lIyjpECjx8Hcrl_WmJzOjOluf3WKljosXkoQtbWvOESMeVYznnGylo5Cfx1Shp3Vu11e0OFxnF58-penjZV4FRjKBo0gVfMAorbkWMN3GlezTCaYi9wgG2yIeevffHCEu3tJTwAMQq7IzJOB0Tx9Th2J51mc7vboUDrUJ_NzHeVUtqrBnur-uRyl6PQs4OwNP7BY0HpJ9bvaalkfXOCXtFBlUBz7-tF1KHDRAn-z-sfq8TrkQEPBm5KNi_HUQQP3wFcy6jiRga1tSyFHN3wvgdekG7ijBUh_YB5ufLKner4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uuLmZHX9f9O0edXu2SpKMeQRTtdVYwTvvws10oBMeGf_Vi6U9_FyHZwVGfGXMMyxEubxzwRZSDxdnKOUlTGxLTSmyDhzkWKuQy6vGQf3lug1YAD4IQCuaRqo_boF3yCtBVBKbSuJpM6GZ5-5lJbCWZkegicfbJVuExKYDI-XRpLn1t08PaSy9qzay0VI2eZxpGX3doxNQL7rGfLs4vVtajX39AEz-fwOhTexPEEj7vTA70prUiz72uA5xd6QNe8iaqAaoIDA7BxjoE-YYR1MOsU6HSwzawlRDWGlmg_aSvmKkHyeAFf3tQXQdf1FV3FIydOKlC-qVfYS2Wx6SP-b1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZWiul3iB71YgTOqEPm0f91GPa4aEgKtwWyAWGfpg7H6smoK5HP7c5ttnQP7YB75Oe8_8vA9D1j1OdtiC7YLmc9G2MHUAFSwFYX4_ax1rEAw8eeRHhAkuydRmmgH9N4Us7co0yDLgGWIxCIOqNE4TWFn6JAz_tf5vf6ynqzBUpuIdJFtvoO_XZmQUjlB-k70q_RPbfegoAQTUNCIVfHyQ74H0kb9748OVHyfLmUEsnjrxh0rr9Ia4c1kXBCK-uYekfuTB0WcC_E29UITNlMo0-imdvLA2pzQeALnLRgx3bKJBS5HjfqMBCuC2nJE6YoyLmVlg8mjtPoekVoxAs5Lo9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RkfH4Y036ju8yIwAS3FsCzaQmluSb1F5hdhJzvfpISbwfPbBr_gW6kkzae4UKa0PUWHqcVQmeZCXFr4o9ILi_tSxpeuV2G6qEfCRX8az73m5XKvNX_RET5sYyVrtm-4oFQsKqP5bGdx_RqPHeeQgarlkfI7ErTzbWnjCPre0UVfsowSJImNbobnGb7AjO9StEwu1pTXOC-hKypmgRbZHAhQOhboX09BRPZq2NDXD3mtYVitfU21BN4F5fVukJv4EhGg1UttO9hN-ahr1xKW6Qz0vUFzVB9ZR4ILAAmqRjPaHcLeu2f1N541Olw1TH_-AVZgBI0unGpL8u-9lCEQcWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L1BhZW_EraM30Waulprr90ujrFPjskWl2-t7SLmBIq0kfdM4MUDurHfjyh0qLrZQEKLrl-vMQi1jyqWmsdjPpt2OSx9V68jFb3vQM40VLVWs5DsEaIFtwbate0ZiFz24q3QIvqnBON7Pwy9oTGh9jH0RV7q82t42ZstMBH1pLc_agNNHkhbCtbjXWakMd77JoahXXVmAHqwQ4t_kkug-C25LN8xDXGm9gwDq3P_OD2M9f5Og2wlYhedcrEx3fqHe4iYvGwYgS_-xEuiTd0vGjFOv242ay0J3uUzADHVtKmHuidzgsg89EHg_6dnwRYOmkVKPBsYXOZkjHK4huvcJmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌
🔴
وزیر کشور پاکستان در دیدار با پزشکیان: شرایط اخیر به‌خوبی نشان داد که در بزنگاه‌های حساس، دوست و دشمن واقعی چگونه شناخته می‌شوند
🔸
این موضوع می‌تواند مبنایی مهم برای تصمیم‌گیری‌های راهبردی آینده باشد.
🔸
ایران و پاکستان همواره روابطی نزدیک و برادرانه داشته‌اند…</div>
<div class="tg-footer">👁️ 2.51K · <a href="https://t.me/farsna/436214" target="_blank">📅 20:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436213">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/007cdcfef9.mp4?token=XZJ1TqR1gd2F7w9aQeL2eLK9EOcfBrjq6P5IanKBJLqrt11ydUIn6xF_7ZJwjhMROr0z3JwXRyMpidMurTK-MPBHzI_P1cQKth0KRUssASy2XR4WZMpK9AuiXdnuVjaFqPwhHTrj64su6g4TPZjdS0JGkFE7cSUATJo9YWxunT7u6VVQEol6Z06JjziI9hW14a-b0eY5ooesnW3yx4DYmdX-Lt-cIOYUxSxqLNbd7lzXI36RJndjfk9NhRo6wEhPudhAtmvIsn4a7E7X2Yj2CRhZrvd7iZd2-emUnoMsbjMzuczcKk__wlK4KMqbnLV07AwIETrA4h9XNd7wf2upnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/007cdcfef9.mp4?token=XZJ1TqR1gd2F7w9aQeL2eLK9EOcfBrjq6P5IanKBJLqrt11ydUIn6xF_7ZJwjhMROr0z3JwXRyMpidMurTK-MPBHzI_P1cQKth0KRUssASy2XR4WZMpK9AuiXdnuVjaFqPwhHTrj64su6g4TPZjdS0JGkFE7cSUATJo9YWxunT7u6VVQEol6Z06JjziI9hW14a-b0eY5ooesnW3yx4DYmdX-Lt-cIOYUxSxqLNbd7lzXI36RJndjfk9NhRo6wEhPudhAtmvIsn4a7E7X2Yj2CRhZrvd7iZd2-emUnoMsbjMzuczcKk__wlK4KMqbnLV07AwIETrA4h9XNd7wf2upnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهاجرانی: گمان نمی‌کردم قدرت موشکی ایران این‌قدر بالا باشد
🔹
باید پدیدۀ شهرهای موشکی را به‌عنوان امکانات درجه اول درنظر بگیریم. ما باید در کشور شهرهایی داشته باشیم که تمام امکانات حکومتی در آن پیش‌بینی شود که در صورت حمله به امکانات‌مان گزینه داشته باشیم.…</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/farsna/436213" target="_blank">📅 20:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436212">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-38.pdf</div>
  <div class="tg-doc-extra">8.1 MB</div>
</div>
<a href="https://t.me/farsna/436212" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">خط-37.pdf</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/farsna/436212" target="_blank">📅 20:13 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436211">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ct0DETgeTozJHLV_Z6_wtZwBE-EcA67OYRKcmS6SYCXkyV99PRbExSd5I57IUncyzjoxHjfafqbAtDyNlt05abws9b6sr540SHsXKIGV4e50tzEUgs7oIqbNESH2rVIdufi48NEYOF-32UJ10cK1rplWAFBCZZPJVEMvehljC3h0a6SWNzs_ITvDqiGgKJjtE7MlSPE2Y1H5kREv3_q9vI2IgJMIIIeh_b291h7vRFZDeJc2SibPcxF0ohaLX_ONwEZPG7LWFjdsiSrSTbeg8HSc-rPyYgj-y2XFVYrauganCJVJS8sDGoum727CFRlPtu5iTpDImaeT-r44lhUSPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی فوتبال اعلام شد
🔸
علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه
🔸
احسان حاج‌صفی، میلاد محمدی، امید نورافکن، شجاع خلیل‌زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی
🔸
سامان قدوس،…</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/farsna/436211" target="_blank">📅 20:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436210">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-text">علی پروین در بیمارستان بستری شد
🔹
علی پروین پیشکسوت باشگاه پرسپولیس برای دومین بار در ماه اخیر در بیمارستان بستری شد.
🔹
پروین به دلیل چکاپ پیگیری برخی از موارد پزشکی مرتبط با خود در بیمارستان بستری شده و نزدیکان او معتقد هستند که احتمالاً تا یکی دو روز آینده از بیمارستان مرخص می‌شود.
🔹
پروین چندی پیش هم به دلیل مشابه در بیمارستان بستری شد اما پیگیری‌ها نشان می‌دهد که خوشبختانه شرایط جسمانی او پایدار است و مشکل خاصی وجود ندارد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/farsna/436210" target="_blank">📅 19:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436209">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9hvJhPak3GpOnNgkdn-OmwuTWxUokyXEFEfFPZcpOr1HlxI-iMLhcMsMAZU1kEQ5Gy_VFF9qYrlm4wJJc0HQrANU7gT8Uw7W9karfOwcI1AoaaBzTTMFNWao0JRHHLDx8x3c2vyv5k2WRDWDKNGyXT3TlFGnJI6ERksw-No6f0pzo3KbmMD9P4mBY9IZYtYCZk0bZ3H26swqP4JP2wgWaRvadshqeLio1oPQNlEGp3Yipm5PEvZXtKp10ySuJgaZZF46epS7_fm27f2tvE4EvAfPRMz55-g2wt15JUX1CxvubUBgAbAR7mkvCVwWreTipw-clqUMBFZ7VHf7o_0Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قدرت تنگهٔ هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/farsna/436209" target="_blank">📅 19:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436208">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fddccd8a31.mp4?token=g49PQoTBeg6-6Fbm9elIE7r87fnH74vuMkbquCzRKZV-QfjT4kI3mHg2k-M_Da-bOALfhUUfn4b_r4xWsba0kAaOk2oevniPipnINkbCQ6j-gVF_Z-GRpVJQk5pJMP5rswnir0XlnVVnbqx1ZWk_DALj9OIShgVjIND1563O4-paYU7DV78oEOqS82N2cMfJC-Xlu_XG0TAdXTWiO--ZItQfsqQJOX57Let9xySv1RWximP1-_Xx23IPvKebGQDoues-IpjHJOeDccGc005S0e6cMkcq1HlA8uLg-9QUGv1Ms1guMQ0_eA95Q19Sl2cgbZatB6rfVFjkRRLNa1mxJArRZuUvTxmM3mTERoqAnK7p9DM7gOQReVRqOn8-pwU43IrFocFkikZOrdypO_MYx9bLwz-6d-7XF2QkL5Fm1uKvUKU87rvqasry3igr0gI5h8g3iKpqa0Z3ys7mxOkX90zckaFRZb444PL3mpAN7ebW3-TxYpCwiC7GEZXWQHVH03o4whK8_rUA3Whb7-tJFDSVZeZYA8Q7Mjctx8Mr4suGoZYti4MVHutLttc9cDIZ_xNNGIiFOFX0dWfec-V5IU0JEvLqGfxJ0TJ20wiKzcTM9DGAV-2cb2q28niyxGw9OLZh4nJD1LWzMq2S85ptZDrgSxSbOC5vHzTqb3wp4QE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fddccd8a31.mp4?token=g49PQoTBeg6-6Fbm9elIE7r87fnH74vuMkbquCzRKZV-QfjT4kI3mHg2k-M_Da-bOALfhUUfn4b_r4xWsba0kAaOk2oevniPipnINkbCQ6j-gVF_Z-GRpVJQk5pJMP5rswnir0XlnVVnbqx1ZWk_DALj9OIShgVjIND1563O4-paYU7DV78oEOqS82N2cMfJC-Xlu_XG0TAdXTWiO--ZItQfsqQJOX57Let9xySv1RWximP1-_Xx23IPvKebGQDoues-IpjHJOeDccGc005S0e6cMkcq1HlA8uLg-9QUGv1Ms1guMQ0_eA95Q19Sl2cgbZatB6rfVFjkRRLNa1mxJArRZuUvTxmM3mTERoqAnK7p9DM7gOQReVRqOn8-pwU43IrFocFkikZOrdypO_MYx9bLwz-6d-7XF2QkL5Fm1uKvUKU87rvqasry3igr0gI5h8g3iKpqa0Z3ys7mxOkX90zckaFRZb444PL3mpAN7ebW3-TxYpCwiC7GEZXWQHVH03o4whK8_rUA3Whb7-tJFDSVZeZYA8Q7Mjctx8Mr4suGoZYti4MVHutLttc9cDIZ_xNNGIiFOFX0dWfec-V5IU0JEvLqGfxJ0TJ20wiKzcTM9DGAV-2cb2q28niyxGw9OLZh4nJD1LWzMq2S85ptZDrgSxSbOC5vHzTqb3wp4QE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروج ۵ کشور کلیدی از یوروویژن در اعتراض به کشتار غزه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/farsna/436208" target="_blank">📅 19:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436206">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aundPuhn7gcpdPQn41dEmdalTtYAki_DcH7j3xBjAmvfc5VwWn4u9YXowghbO19lUuh6occYXBixf3XeshP3ubOfytvrRyPsd3NH0yHKRGFn0mygEswuEO9uKpIA6Vp0yBJKMVi3K1tnij9v4TdDDoZ_slneIvGd9sAUScRvPXljzck3658z2I5PZ3H5v6uOVBoQrXNGAqsiuys5iGCYD4hswe17ZM3uTGNLy_0KcE_8jCDEukDsgbk_DlzqKScHQVzjzyOOpvWBEow5feIEzBBRaRORCNTWn9dRpi119KB1xNg1nVAYRcsHwGXEhgwLwi8PL3hHxZhXfuy9DsBfXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سناتور ضدایرانی: هرچه بیشتر تنگه هرمز بسته بماند، ایران قوی‌تر می‌شود
🔹
گراهام در مصاحبه با ان‌بی‌سی ادعاهای خود علیه ایران را تکرار کرد و خواستار حملات سنگین‌تر به ایران شد.
🔹
وی با اشاره به بسته بودن تنگه هرمز گفت: «من فکر می‌کنم وضع موجود به همه ما آسیب می‌زند. هرچه قدر تنگه هرمز بیشتر بسته بماند، هرچقدر ما بیشتر تلاش می‌کنیم به توافقی برسیم که هرگز حاصل نمی‌شود، ایران قوی‌تر می‌شود.»
🔹
سناتور ضدایرانی با اشاره به نگرانی‌ها درباره شکست هم‌حزبی‌هایش در انتخابات میان‌دوره‌ای به خاطر جنگ ایران گفت: «ارزشش را دارد که شغلم را از دست بدهم. اگر مجبور باشم شغلم را برای اطمینان از اینکه ایران هرگز سلاح هسته‌ای نخواهد داشت، از دست بدهم، این کار را می‌کنم.»
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/farsna/436206" target="_blank">📅 19:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436205">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba8410dfd5.mp4?token=DP584kEl2FYdnRp8zgHJfpDaGRm3fotuT4TVjO6ihAcM-CMfJ8JSw2A6Hwm1VZhKX2JlHNnQC5Vfh4-kV-DAwcebD6vusCMPUFZ-hUqVk-0f3b6bdVUpaFDnynd6GbHD8ByduPpug2fm6DLGJwL2zWwqs9pMB5gaXMuscpRgWnq2Luwkr3X4zHdzLKfW58pkIl4FMtm6ycojZbVya91974TvKG4GZDXLQ7-EGPdKZKCqnkNRtPtgHnlFhdh_NyCH2x39hDfpEPhRtq75MdpWuFL920O6Spz2RFrBgpzub6FH8eykkyGAHncHSjx7wEh74-p9umF-csXkr4rOugAMES7kkmRZMfWqay8PDO2DKrt-6p7qIvw1FUln4_J3MaNLflzMzRFJgbDggxZNJRfAMqqa8GX5dDKYxoicC49ZwtsZMVW_zBSBwlL8PY2IL75qOiYdkYvpiszMCZKkdx5A_M_4zcgpv5JWu99yBWgfRP1i8YmcfHhG6UXI4eyLlCzwa_zdbE5iyZGdQZnvYC4OKU9isiJsQXFSv2Uby6CFHNPhxcaw1XF8hijKFnOR-R8XL2Y8zFfKlGJviglq7J8xxuH7Y89s8jdM1-DktPgbhAepXUo06dar6PHBoAMsEURHU8kTMu71Hbfy4RtQAV6oV3_I8sRyk6jiKXE0Fw_XE3c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba8410dfd5.mp4?token=DP584kEl2FYdnRp8zgHJfpDaGRm3fotuT4TVjO6ihAcM-CMfJ8JSw2A6Hwm1VZhKX2JlHNnQC5Vfh4-kV-DAwcebD6vusCMPUFZ-hUqVk-0f3b6bdVUpaFDnynd6GbHD8ByduPpug2fm6DLGJwL2zWwqs9pMB5gaXMuscpRgWnq2Luwkr3X4zHdzLKfW58pkIl4FMtm6ycojZbVya91974TvKG4GZDXLQ7-EGPdKZKCqnkNRtPtgHnlFhdh_NyCH2x39hDfpEPhRtq75MdpWuFL920O6Spz2RFrBgpzub6FH8eykkyGAHncHSjx7wEh74-p9umF-csXkr4rOugAMES7kkmRZMfWqay8PDO2DKrt-6p7qIvw1FUln4_J3MaNLflzMzRFJgbDggxZNJRfAMqqa8GX5dDKYxoicC49ZwtsZMVW_zBSBwlL8PY2IL75qOiYdkYvpiszMCZKkdx5A_M_4zcgpv5JWu99yBWgfRP1i8YmcfHhG6UXI4eyLlCzwa_zdbE5iyZGdQZnvYC4OKU9isiJsQXFSv2Uby6CFHNPhxcaw1XF8hijKFnOR-R8XL2Y8zFfKlGJviglq7J8xxuH7Y89s8jdM1-DktPgbhAepXUo06dar6PHBoAMsEURHU8kTMu71Hbfy4RtQAV6oV3_I8sRyk6jiKXE0Fw_XE3c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت امدادگران از ۸ اصابت در مجاورت پایگاه امدادی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/farsna/436205" target="_blank">📅 19:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436204">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec43abb129.mp4?token=C-8oPc9vpGFm8nfe0vXnWKBGn1A1YyM5jXbP-BlHRq1xCk_b9yet9Ehd362bpxALSWhnseHddXIkMno1QELoZ4cMYSiNJLvJ0b-ubuXf55jbZRYsffo629dSY84OBC8fx0wqWf5I_PWHWRZYyA9T3QwcJjXqsm3hLaeP34vSlG0e3b2ROzD3RXItwGf0PKcVMkZLEvwruiSzxzZQRf6R_IH5BpUUfljrI0vRWx7mo1W04ci5nOTwTInWNAcjlrnssX00tFjNV0MD7a-Ni4B9Thrsc65lhaVcZUa-btO95tKVghd6hEAT1Z__e3cRYr7hO6S_8OrLBBaP4N0S1jzsRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec43abb129.mp4?token=C-8oPc9vpGFm8nfe0vXnWKBGn1A1YyM5jXbP-BlHRq1xCk_b9yet9Ehd362bpxALSWhnseHddXIkMno1QELoZ4cMYSiNJLvJ0b-ubuXf55jbZRYsffo629dSY84OBC8fx0wqWf5I_PWHWRZYyA9T3QwcJjXqsm3hLaeP34vSlG0e3b2ROzD3RXItwGf0PKcVMkZLEvwruiSzxzZQRf6R_IH5BpUUfljrI0vRWx7mo1W04ci5nOTwTInWNAcjlrnssX00tFjNV0MD7a-Ni4B9Thrsc65lhaVcZUa-btO95tKVghd6hEAT1Z__e3cRYr7hO6S_8OrLBBaP4N0S1jzsRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دریادار بازنشستهٔ ارتش ترکیه: ایران عزت جهان اسلام و آبروی منطقهٔ ما شده
🔹
ارتورک
: من یک اسلام‌گرا نیستم اما باید گفت که ایران با ایستادگی خود مایهٔ عزت جهان اسلام و آبروی منطقه شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/farsna/436204" target="_blank">📅 19:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436202">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🎥
طنینِ حماسی، لاله‌های میناب در نیشابور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/farsna/436202" target="_blank">📅 19:16 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436201">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eR76eGORUfb8SHbhivqRkaly4ojAQcNSNMUD0zNiBeSJLHOMWxBtm9TqSSnL3MPzN3FLQwroHxMfIjKFLj-Ycb9TGkqJO9L0YImj_l-ooQD9TRKozPUbbD1f1H7n66nKge5zcLi5IJ9T_L53-ZsWcqlwci9CcGRabipRHoPYImQfVMW68iy3yBeLoIpbj9RFh_PsC4FgzaUveci8iVq86Aihj45WK0xewZ5rNKTXi80YbNwrk2P1AMv3NFclOlOJH92qwB3YULcpChdkmxtg-iN0Ia-vjR78AN5FmEok8sqrGwJJj5OT_vEvx-Xzhz2pijfkAut2ZupSCBmvrex08A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶ عملیات حزب‌الله علیه صهیونیست‌ها از صبح امروز
🔹
حزب‌الله: مجاهدان مقاومت در یک عملیات تلاش دشمن برای پیشروی به سمت منطقه صافیتا در شهرک یحمر الشقیف را رصد کرده و در مسیر حرکت نظامیان صهیونیست مین ضدنفری را منفجر کردند که موجب کشته و زخمی شدن آنها شد.
🔹
سه حمله کوادکوپتری هم آشیانه توپخانه ارتش اسرائیل در العدیسه، یک خودروی نظامی و یک تجمع نظامیان صهیونیست در شهرک البیاضه را هدف قرار داد.
🔹
محل تجمع نظامیان صهیونیست و خودروهای آنها در شهرک رشاف نیز امروز با چندین فروند راکت مورد هدف قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/farsna/436201" target="_blank">📅 19:15 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436200">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bccb5391a.mp4?token=ZALjl8nf1NksqBm6WhCFzdgnl2lxIIqBV4iH92vyLvhkPNrmQeXR8M33Bc43MHZ4AIf-9ouFSHBlmN3FQEIH6iwoBUSLIT9VM4RFEC3Qi5tqUcH58gJuLhHwIOKZQsiFbTQP1hZIJ2IL0O36nBGkIc6r8nBWOy_0xo_tdC8hhHa7vmApAJOsvBWcehodavAQOn08cbqqNiYgAMknvQmhzjFgQ7IfdPUoRKytKGmzjHxL_xHS3XPonudu-nPOWbZY7sQiCf5SsPADU5-aQHw-jTt0Sg4jzLP4zv97gI0BII563HvinEtoaaOWyfMj1j6MUBJOgtUTpesCMvKF3jQMYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bccb5391a.mp4?token=ZALjl8nf1NksqBm6WhCFzdgnl2lxIIqBV4iH92vyLvhkPNrmQeXR8M33Bc43MHZ4AIf-9ouFSHBlmN3FQEIH6iwoBUSLIT9VM4RFEC3Qi5tqUcH58gJuLhHwIOKZQsiFbTQP1hZIJ2IL0O36nBGkIc6r8nBWOy_0xo_tdC8hhHa7vmApAJOsvBWcehodavAQOn08cbqqNiYgAMknvQmhzjFgQ7IfdPUoRKytKGmzjHxL_xHS3XPonudu-nPOWbZY7sQiCf5SsPADU5-aQHw-jTt0Sg4jzLP4zv97gI0BII563HvinEtoaaOWyfMj1j6MUBJOgtUTpesCMvKF3jQMYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهاجرانی: ایران چریک نیست، مدافع است
🔹
آمریکا در جنگ به اهدافش نرسید، بازهم حمله کند نتیجه‌ای نمی‌گیرد. @Farsna</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/farsna/436200" target="_blank">📅 19:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436199">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb5650da56.mp4?token=RQJtEDw0zJGAP9w4pZSqh7OciPEJcbnIltJwKWF68AVaHt6ZIUVTpHZqo6_23mcI6GBN0FD8zUCtFqRaSslvKKvVtO6F8JA_JWd_U2x8i4v_MSSfWDpRkxtCGtc0Hhj4SqKonYACVv8FJ5l0gtvZWnX6b4gosH9oBKe0JFko7zHdWVUMTkITOnaxJZ41Q9ZgL596VFbGqM2Oyn0S7HWSeWMXE9jaUCjmoYuqJr3KSEu-29SY6hNMMacfklzwkI4vZx71apAuNToo7oVY4756YxXFdp4wI8P9qzlWF57Xm55AWxUDZrQkyq2XrNBXaS5o53HTaMKp2HEBxh4p9PaM-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb5650da56.mp4?token=RQJtEDw0zJGAP9w4pZSqh7OciPEJcbnIltJwKWF68AVaHt6ZIUVTpHZqo6_23mcI6GBN0FD8zUCtFqRaSslvKKvVtO6F8JA_JWd_U2x8i4v_MSSfWDpRkxtCGtc0Hhj4SqKonYACVv8FJ5l0gtvZWnX6b4gosH9oBKe0JFko7zHdWVUMTkITOnaxJZ41Q9ZgL596VFbGqM2Oyn0S7HWSeWMXE9jaUCjmoYuqJr3KSEu-29SY6hNMMacfklzwkI4vZx71apAuNToo7oVY4756YxXFdp4wI8P9qzlWF57Xm55AWxUDZrQkyq2XrNBXaS5o53HTaMKp2HEBxh4p9PaM-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهاجرانی: الان کشورهای جنوب خلیج فارس در برابر آمریکا موضع بردگی دارند.  @Farsna</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/farsna/436199" target="_blank">📅 19:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436198">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‌ بازگشایی بورس از سه‌شنبه
🔹
معاون سازمان بورس: مقرر شد بازگشایی بازار سهام، انواع صندوق‌های سرمایه‌گذاری در سهام و مشتقات آن‌ها از روز سه‌شنبه هفته جاری صورت پذیرد. @Farsna</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/farsna/436198" target="_blank">📅 18:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436197">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22707d6d68.mp4?token=E-z-m95y_FknHfhTUD--DbaIoIeQ9lfWCpGIAmLoZxb0u_vsQV0mLOZeh1EbTP6pHdLWMp_4cLPDaFd04Nc5hB-E_QZkAeHSAerNMZenh6JfmSqaOrmuDPg7K0vDMD3xnN3s6hiXPxc19SIbOENyryGPWkk-M2j_hvafR1dADU4XjM4hY2TSh1k2pMIcS6fmT13KYKlnfDyC8KNyCbOZ92MtktkTA5LyJPBVAzEy8d2vY-kXXrpj_lQcuM5pO5VPEIt3L_zqPrigIUIjghn2VXwO1lWGb2MBFE_y2Uzzes1SGTmoFiiYn68NGCCHt1_paoqJ55O7CEaZyEFiDxSfQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22707d6d68.mp4?token=E-z-m95y_FknHfhTUD--DbaIoIeQ9lfWCpGIAmLoZxb0u_vsQV0mLOZeh1EbTP6pHdLWMp_4cLPDaFd04Nc5hB-E_QZkAeHSAerNMZenh6JfmSqaOrmuDPg7K0vDMD3xnN3s6hiXPxc19SIbOENyryGPWkk-M2j_hvafR1dADU4XjM4hY2TSh1k2pMIcS6fmT13KYKlnfDyC8KNyCbOZ92MtktkTA5LyJPBVAzEy8d2vY-kXXrpj_lQcuM5pO5VPEIt3L_zqPrigIUIjghn2VXwO1lWGb2MBFE_y2Uzzes1SGTmoFiiYn68NGCCHt1_paoqJ55O7CEaZyEFiDxSfQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهاجرانی: آمریکایی‌ها ما را بردۀ خودشان می‌بینند و این موضع هیچ‌وقت تغییر نکرده است
🔹
اوباما این نگاه را با ادبیات ملایم پنهان می‌کرد اما ترامپ این موضوع را ثابت کرد.
🔹
به‌‌طورکلی تفاوتی بین نگاه اوباما و ترامپ نیست؛ ترامپ این موضوع را با لمپنی بیان می‌کند…</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/farsna/436197" target="_blank">📅 18:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436196">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad20418791.mp4?token=qH-xRmIYTFPs8QknbDUS6YbJV_rOKO5HCDgjo8xAKUnvQoKbFxbXgyBq-TKS3gzGOC9APt6ydqsJx2BFin3TZ4Ua6nx2cP_5gxLYTv_gpWCCirbZ6vXiJmn1Easl8DWFE3aFbBK0ixRa8p-0Hf4mMuy5ESIF6K2BA7Ey0WT0p0vxHeGjCY37nr7lyz7jF01bTrdlQCTAARna10ZOpmyKw14zGI1gUKW2Szxqzk6W-o6rNdYb3uWJDqaCvyd_cyC9wWR1ZniOth60lEIGAe1W7U1lGcz6WcGwMfHO72MrFWM8G1YbEiilA1gKJjKBYeKrkvZM09fTX2Y_kqNA1-7dAIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad20418791.mp4?token=qH-xRmIYTFPs8QknbDUS6YbJV_rOKO5HCDgjo8xAKUnvQoKbFxbXgyBq-TKS3gzGOC9APt6ydqsJx2BFin3TZ4Ua6nx2cP_5gxLYTv_gpWCCirbZ6vXiJmn1Easl8DWFE3aFbBK0ixRa8p-0Hf4mMuy5ESIF6K2BA7Ey0WT0p0vxHeGjCY37nr7lyz7jF01bTrdlQCTAARna10ZOpmyKw14zGI1gUKW2Szxqzk6W-o6rNdYb3uWJDqaCvyd_cyC9wWR1ZniOth60lEIGAe1W7U1lGcz6WcGwMfHO72MrFWM8G1YbEiilA1gKJjKBYeKrkvZM09fTX2Y_kqNA1-7dAIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهاجرانی: اگر دشمن درپی دیکته‌کردن شرایطش باشد طبیعی است که مذاکره را نپذیریم
🔹
هیچ‌کس این را نمی‌پذیرد مگر افرادی که ضعیف و ناتوان باشند. @Farsna</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farsna/436196" target="_blank">📅 18:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436195">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4b17bc31.mp4?token=LXxkQIOyJ2ze6fUy5yG1ErozW4S-mdsCTGM9qkYTVLQvKGMhwRRgxNWXDGhTlIJ6ZhRvJqv5VoklhaPwAKUMN_g5qj-F-pbwH3RrJK1D9QsWOi7w76WqhOKSjmhq8_kqLWmmk9LOmq5sZW0yhw_oknL1DPIFW1hpm_SgZ55fXAcaLwFlhFcRSB0h77_0RHRuG0B9AP7SI_03gp0WFQiWVhgnTkb-f7D-UVYHOqvOk_nQOZLCNQuPkc3_KJmhLQic3NGKY-UdEwkkIpnoapYqRU2Exwk0oETRNS--jyz40JlPbuNxrVuxnTy11q7CzkKte8SRAWNhf9knjCykmzDw7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4b17bc31.mp4?token=LXxkQIOyJ2ze6fUy5yG1ErozW4S-mdsCTGM9qkYTVLQvKGMhwRRgxNWXDGhTlIJ6ZhRvJqv5VoklhaPwAKUMN_g5qj-F-pbwH3RrJK1D9QsWOi7w76WqhOKSjmhq8_kqLWmmk9LOmq5sZW0yhw_oknL1DPIFW1hpm_SgZ55fXAcaLwFlhFcRSB0h77_0RHRuG0B9AP7SI_03gp0WFQiWVhgnTkb-f7D-UVYHOqvOk_nQOZLCNQuPkc3_KJmhLQic3NGKY-UdEwkkIpnoapYqRU2Exwk0oETRNS--jyz40JlPbuNxrVuxnTy11q7CzkKte8SRAWNhf9knjCykmzDw7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
حرم کریمهٔ اهل‌بیت میزبان دسته‌های عزاداری شهادت امام جواد(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/farsna/436195" target="_blank">📅 18:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436194">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc5fe32273.mp4?token=Ob-K7P3IDXGkHs7X-_-Y5EesOS0SyEo6nNJUgV2xE7osiJnvoeTCd_NQfGXfhYJkWMQu1tFKdd1-hd5kMZysiRz1LHOKJV6Tk1toBAZVIDX6f9vX4jFS_RhLtJlEwhuNc3BfkodyqHONK_yteU2-QkXDBFvU1oZQcyQUFKqt3eAVI5rdbVeeX43gBHYYecKBM-A36bC9ioPhADa2Nv-JC93PEiACvGoX7u022lsiOm8_NrbNSYkj6GTEBtlY5taDMcs8IZxfkG-O5sjRk7HoHUgpdx9qbwUIv0CW5mbHiAkDa_aEkriH7QwaeZH3fPpILvCVk_BCJcZCQ5Sasg6DYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc5fe32273.mp4?token=Ob-K7P3IDXGkHs7X-_-Y5EesOS0SyEo6nNJUgV2xE7osiJnvoeTCd_NQfGXfhYJkWMQu1tFKdd1-hd5kMZysiRz1LHOKJV6Tk1toBAZVIDX6f9vX4jFS_RhLtJlEwhuNc3BfkodyqHONK_yteU2-QkXDBFvU1oZQcyQUFKqt3eAVI5rdbVeeX43gBHYYecKBM-A36bC9ioPhADa2Nv-JC93PEiACvGoX7u022lsiOm8_NrbNSYkj6GTEBtlY5taDMcs8IZxfkG-O5sjRk7HoHUgpdx9qbwUIv0CW5mbHiAkDa_aEkriH7QwaeZH3fPpILvCVk_BCJcZCQ5Sasg6DYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
فنجان دوم اسپرسو با مهاجرانی  گفت‌و‌گو با عطاءالله مهاجرانی را هم‌اکنون در سایت، ایتا، روبیکا و تلگرام فارس ببینید. @Farsna</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/farsna/436194" target="_blank">📅 18:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436193">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvicauhH-VMY5adJG6Rc-XspOeyGWCf7vpc3-N0vryeQFewgaif2RZLndESr3Zpg4HKef0MQTlMX4yUiZqs9M347Ho7SZVYmlKh7PhBgRBi1zBstCdrMXjmpN7x9xtN87O4GW34DruZadbgzJowXlPzMN3eeoDW41jU4Oh7MFmvroqZLI5J10MX3QM3EXauh0F_dV3bicLAkFRPhvmzmBCI9SMk0QGXscHF-6pTlSLIrufysLE9ClXsoExwRuMSbVqm14Sahz2fqePSHx1kTAO_ZuKbNJfQyGdP1sJrrygSBdZbRFKVtDD2sblGY5stMeH6dQAuDJTlooKTbd9VUpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
فنجان دوم اسپرسو با مهاجرانی
گفت‌و‌گو با عطاءالله مهاجرانی را هم‌اکنون در
سایت
،
ایتا
،
روبیکا
و
تلگرام
فارس ببینید.
@Farsna</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/436193" target="_blank">📅 18:10 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436192">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/farsna/436192" target="_blank">📅 18:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436191">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🎥
پیکر شهید عزالدین الحداد، فرمانده گردان‌های القسام در غزه تشییع شد
🔹
شهید الحداد دیروز به‌همراه همسر و دخترش توسط رژیم صهیونیستی به شهادت رسید. @Farsna</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/farsna/436191" target="_blank">📅 18:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436190">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb58f7967.mp4?token=S1g4f3zvd6lYGqBfXtCHx-hpC2w0TFEEkC1xAAjNWWPEqslZEH-f0MZBcG5BjnijbbuZkva-YPGFdEWT-_L-zKizB8TVrp1SEQ4J2lSRF6pIoJEPo88dmQHRkThHeB1xLn-uTPk87DiddPV8u0DHutDeWcbxVZLaKf52wcwNA0o2jn8TjNgGt_XBQUpJFUD_NO15BHPUryAZQYInTS4GNCe8k9R4nh8INCFmZ1TWgTDdC5_YsvrSVy1-YtqyKckS_ORSKnE-mUQB9A8JWOWy4zIBAoHnHe4DqxhxFngCGNfEzLFCNNxs8r_qi_tO4L1YOc9hJE4CUqzigc9xxS-9WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb58f7967.mp4?token=S1g4f3zvd6lYGqBfXtCHx-hpC2w0TFEEkC1xAAjNWWPEqslZEH-f0MZBcG5BjnijbbuZkva-YPGFdEWT-_L-zKizB8TVrp1SEQ4J2lSRF6pIoJEPo88dmQHRkThHeB1xLn-uTPk87DiddPV8u0DHutDeWcbxVZLaKf52wcwNA0o2jn8TjNgGt_XBQUpJFUD_NO15BHPUryAZQYInTS4GNCe8k9R4nh8INCFmZ1TWgTDdC5_YsvrSVy1-YtqyKckS_ORSKnE-mUQB9A8JWOWy4zIBAoHnHe4DqxhxFngCGNfEzLFCNNxs8r_qi_tO4L1YOc9hJE4CUqzigc9xxS-9WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید انقلاب: موج گرایش به اهل‌بیت(ع) از زمان امام جواد(ع) گسترش بیشتری پیدا کرد
@Farsna</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/436190" target="_blank">📅 17:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436189">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‌
🔴
قالیباف در دیدار وزیر کشور پاکستان: برخی دولت‌های منطقه تصور می‌کردند حضور آمریکا برای آنها امنیت‌آور است اما حوادث اخیر نشان داد که این حضور نه‌تنها امنیت‌زا نیست بلکه زمینۀ ناامنی را هم فراهم می‌کند.  @Farsna</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/436189" target="_blank">📅 17:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436188">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">📷
وزیر کشور پاکستان با قالیباف دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/farsna/436188" target="_blank">📅 17:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436187">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3564b1a7a8.mp4?token=C0jf3hn2oPEzQ4JXDha2p5pFvUKgkG39b6pnMHj1chR8LcTGSqyJwH2xTGy6b5pupXikdxccHfFfTE1kyrEC4Naf8uLTUQLQeSWsjn9EyD9sdVadpipoJSO0HVzIAPRPbv4lBFalt4g11KKbMwmxy_SNanh0eO4Vpe1TRh7p4NPw2HMZwCM11oAirfb-C19jnM48jZDs6LgmhJMCdTzS-n_wpkqU9laxCJb5I3EOZRXEBJJONzpPM8FWp4XiJTQ1uCsowe-6qSbE5PDBxoqwhteCo3TMPPlY1L2dfVM0ceQ_mOT3IK5u92mrmpTqipBRCNLdZ9qUNcH9R_KW_XMilA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3564b1a7a8.mp4?token=C0jf3hn2oPEzQ4JXDha2p5pFvUKgkG39b6pnMHj1chR8LcTGSqyJwH2xTGy6b5pupXikdxccHfFfTE1kyrEC4Naf8uLTUQLQeSWsjn9EyD9sdVadpipoJSO0HVzIAPRPbv4lBFalt4g11KKbMwmxy_SNanh0eO4Vpe1TRh7p4NPw2HMZwCM11oAirfb-C19jnM48jZDs6LgmhJMCdTzS-n_wpkqU9laxCJb5I3EOZRXEBJJONzpPM8FWp4XiJTQ1uCsowe-6qSbE5PDBxoqwhteCo3TMPPlY1L2dfVM0ceQ_mOT3IK5u92mrmpTqipBRCNLdZ9qUNcH9R_KW_XMilA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع سربازان ارتش رژیم صهیونیستی هدف پهپاد حزب‌الله شد
@Farsna</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/farsna/436187" target="_blank">📅 17:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436186">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8efY_o923zAC_eE-pefv7yETJvLNP2BMOh0lJ9mDUKsyIoPodvlDRmo5oOqsh9SoZMs7eLRh1nlHRFwcsS5aV9ljcvZq0lmcKoiLXzENQ3dnTLMbxWmUhz1wQFJGCLZWkJriLcx7fDNaJn54oCmYdFbKvnTG0l4JaDSyNO6tQgRBOfZtxOcOWMm8WCUGwlsDMsAArUGASmjQrIU4Kitj6v99YdJWBGf377vy2dWFVFHpjdWFeFT4-xWW9KK9CgLs2DQeM4n1vJnpeTOW9o4N5PTPAO1HZ-JAA-KZyN-gdzxLBIGGGm3ZgfKiVpVH2E6ceFOP-3KBc1ZfTZPE-JrdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت برق را گران کرد یا ارزان
🔹
دولت با تصویب آیین‌نامه‌ای، مشترکان باقدرت قراردادی بالای ۱۵۰ کیلووات را ملزم به خرید برق از بورس کرد.
🔹
عمدهٔ این مشترکان، شرکت‌های توزیع، صنایع و کشاورزان هستند و بخش خانگی به‌دلیل قدرت قراردادی کمتر از ۵ کیلووات شامل این مصوبه نیست.
🔹
طبق بررسی فارس، رقم خریدوفروش برق در بورس انرژی طی مدت گذشته در بسیاری از زمان‌ها از نرخ دستوری دولت کمتر بوده است.
🔹
کارشناسان معتقدند درصورتی‌که ابزار بورس انرژی برای تجارت برق در اختیار دولت باشد، میزان مصرف بدون اعمال محدودیت قابل تأمین است و قیمت از جمله عواملی است که در کنار ساخت نیروگاه، مدیریت بهره‌برداری و تأمین تقاضا زمینه مدیریت انرژی به‌ویژه در فصول گرم و قطعی برق را فراهم خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/farsna/436186" target="_blank">📅 17:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436185">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c0a7ab35f.mp4?token=JExVdjP4IPsBsLbeqjj-ak0fXQr_5N8dFq1Daib824Y1AQo3bsjVQE_pbOjTsaDySfL3yWz8tedQNejzZXhQNM9CUzpuT0HTDC7vwC5OqdzlDnn-XyGFP6T5IjvrRjNTXIB9BV6y2-I7NLzii3VywGfvEUrtpVrYf1K1a8B_ibp7AUhFMrBjYQGqE6T3MjF0-y0PfET7htddLwypb_cYHhwLHuMQUXkh40MQdkfMQEmBknBjZST3mCZaUSbZyqNlihPP3jeJJmDJDkdyqbaR3UGQBlNtS2RrQBgu7xqQGXg9aQtktpHB2I1T9GNhSxLJVCFMUOZA5wJBhvfli8pqMi7E9xVo4sARQprs3U1rfbNLODYnSyvqfcyCvF8s5_VCFDP5RTdBFbn-eMrzzm4DJaiKfPotanuhU5ErZWTh3znb1gWa9T4N9mz81DPv5r5Hc8lLKZDUMTIIadRrEeGOk3zUgYtjbXlnqVgohau5EYVmjJ_xCm8qgXu7XrBZql0FQ9XtwLUaVRJFLwHRLqxBdczg2-Bp8YTLDCMd7nLU0l-xL-pSCdXAoXlBSXqNUwqPjGrcNVuNxHov1Pxp5Bz9-g7REGABppSvf5kB61Gq2yXEMM3WtFEkiFyVaMYd49378TD6wYpnlcAXvP4-33_wfXu2SNJux39LKsQSiwDsKII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c0a7ab35f.mp4?token=JExVdjP4IPsBsLbeqjj-ak0fXQr_5N8dFq1Daib824Y1AQo3bsjVQE_pbOjTsaDySfL3yWz8tedQNejzZXhQNM9CUzpuT0HTDC7vwC5OqdzlDnn-XyGFP6T5IjvrRjNTXIB9BV6y2-I7NLzii3VywGfvEUrtpVrYf1K1a8B_ibp7AUhFMrBjYQGqE6T3MjF0-y0PfET7htddLwypb_cYHhwLHuMQUXkh40MQdkfMQEmBknBjZST3mCZaUSbZyqNlihPP3jeJJmDJDkdyqbaR3UGQBlNtS2RrQBgu7xqQGXg9aQtktpHB2I1T9GNhSxLJVCFMUOZA5wJBhvfli8pqMi7E9xVo4sARQprs3U1rfbNLODYnSyvqfcyCvF8s5_VCFDP5RTdBFbn-eMrzzm4DJaiKfPotanuhU5ErZWTh3znb1gWa9T4N9mz81DPv5r5Hc8lLKZDUMTIIadRrEeGOk3zUgYtjbXlnqVgohau5EYVmjJ_xCm8qgXu7XrBZql0FQ9XtwLUaVRJFLwHRLqxBdczg2-Bp8YTLDCMd7nLU0l-xL-pSCdXAoXlBSXqNUwqPjGrcNVuNxHov1Pxp5Bz9-g7REGABppSvf5kB61Gq2yXEMM3WtFEkiFyVaMYd49378TD6wYpnlcAXvP4-33_wfXu2SNJux39LKsQSiwDsKII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
من پشتم به این پرچم گرمه
@Farsna</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/farsna/436185" target="_blank">📅 17:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436184">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‌ الجزیره: پس‌از حملهٔ پهپادی در محوطهٔ داخلی نیروگاه هسته‌ای «براکه»، در این منطقه آتش‌سوزی صورت گرفته است.
🔹
العربيه گزارش کرده که «این حمله تلفات انسانی در پی نداشته و هنوز مبدأ آن مشخص نیست». دفتر رسانه‌ای ابوظبی هم خبر داد: نیروهای آتش‌نشان، آتش‌سوزی…</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/farsna/436184" target="_blank">📅 17:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436183">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‌
🔴
پزشکیان: در سایۀ وحدت و همگرایی اسلامی، رژیم صهیونیستی هرگز جرئت تعرض و تجاوز به کشورهای اسلامی را نخواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/farsna/436183" target="_blank">📅 17:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436182">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‌
🔴
پزشکیان: از دولت‌های پاکستان، افغانستان و عراق که اجازه ندادند از خاک آنان علیه ایران اقدامی صورت گیرد، صمیمانه تشکر می‌کنم. @Farsna</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/farsna/436182" target="_blank">📅 17:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436181">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
پزشکیان: هدف اصلی دشمن ساقط‌کردن نظام اسلامی بود اما تصور نمی‌کردند که مردم کنار نظام بایستند
🔹
هدف اصلی آمریکا و رژیم صهیونیستی از حمله به ایران، ایجاد بی‌ثباتی داخلی و تلاش برای تضعیف و ساقط‌کردن نظام اسلامی بود، اما آنان هرگز تصور نمی‌کردند ملت بزرگ،…</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/farsna/436181" target="_blank">📅 17:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436180">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
پزشکیان: هدف اصلی دشمن ساقط‌کردن نظام اسلامی بود اما تصور نمی‌کردند که مردم کنار نظام بایستند
🔹
هدف اصلی آمریکا و رژیم صهیونیستی از حمله به ایران، ایجاد بی‌ثباتی داخلی و تلاش برای تضعیف و ساقط‌کردن نظام اسلامی بود، اما آنان هرگز تصور نمی‌کردند ملت بزرگ، شریف و آگاه ایران تا این اندازه با انسجام، اقتدار و وفاداری در کنار نظام و کشور خود ایستادگی کنند و در حمایت از جمهوری اسلامی و مقابله با نظام سلطه، این‌گونه حضوری گسترده و معنادار در صحنه داشته باشند.
@Farsna</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/farsna/436180" target="_blank">📅 17:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436179">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b4dbebb04.mp4?token=M6x2VQ_kp-D634mbRFehHn9fkkp9Q5J7AP14OnzfTN4B8WX2kGfdXnrCVrI-2rXvSu-zI_jd0ZNXIP_6Uu9cN_ObCjbegbBvdc3JmkGiu3PA07u15zx8m9MnTosGzkgACiXWNDnrgAmAzXkTFtLOO2qWj4x9U4oGhvoZF7ZGYArF046f8jUSNde79JSkNmWgaUXIMNADbdi62xuK0UhlxjS5W85UlufkVwrBXnSepuHaIT2EnHgjQefGq-LS6ghCQGe3M62iykaNTkNEbR5CEf4jKZh90iPIWLNbO2wbMEwCrHYFpVP1WylydE2Dfn6v-d-BOlb4rg5BgIRS5qdlJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b4dbebb04.mp4?token=M6x2VQ_kp-D634mbRFehHn9fkkp9Q5J7AP14OnzfTN4B8WX2kGfdXnrCVrI-2rXvSu-zI_jd0ZNXIP_6Uu9cN_ObCjbegbBvdc3JmkGiu3PA07u15zx8m9MnTosGzkgACiXWNDnrgAmAzXkTFtLOO2qWj4x9U4oGhvoZF7ZGYArF046f8jUSNde79JSkNmWgaUXIMNADbdi62xuK0UhlxjS5W85UlufkVwrBXnSepuHaIT2EnHgjQefGq-LS6ghCQGe3M62iykaNTkNEbR5CEf4jKZh90iPIWLNbO2wbMEwCrHYFpVP1WylydE2Dfn6v-d-BOlb4rg5BgIRS5qdlJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ اتفاقات مشکوک در انفجار بیت‌شمش در فلسطین اشغالی
🔹
شبکۀ صهیونیستی کان مدعی شده که آتش‌سوزی مهیب در بیت‌شمش واقع در غرب بیت‌المقدس در نتیجۀ انفجار کنترل‌شده صورت گرفته است.
🔹
با این حال، کاربران فضای‌مجازی گفته‌اند که این انفجار بدون هیچ هشدار قبلی به ساکنان…</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/436179" target="_blank">📅 17:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436178">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f87e991cb5.mp4?token=dp0qiE6uebyJkEr5rnW-GJ9mlUaKvyt6Wx6y6tp9DDUBTT3C-Ts5-zoQo0WCw9O5lLZOTsZZj2Rf8erzWy6TdKlKC0CmFFNGWwjJ9aN_cAESpaKx9jKBM_IRaUI_JlOwRNo2uxC2Y6oIYTDM-wk3DNUGeTtzfhFGgsh3AWQKthN-ZkIIPi4uET4w5uFmcp7xN25LOxgRV6HYUPRWml5xlh39Iavrl2NXi6e6wL9nzzMPgVsJVBk5VdJ03Tzu92j-wCR-9zXqysJDRiWmE0dZH_nj1pthyXlxyLrAtP-24Vj1NtDdi4V9hCTDKy2JnNq423bWG8t7s9kviSIjBTrpSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f87e991cb5.mp4?token=dp0qiE6uebyJkEr5rnW-GJ9mlUaKvyt6Wx6y6tp9DDUBTT3C-Ts5-zoQo0WCw9O5lLZOTsZZj2Rf8erzWy6TdKlKC0CmFFNGWwjJ9aN_cAESpaKx9jKBM_IRaUI_JlOwRNo2uxC2Y6oIYTDM-wk3DNUGeTtzfhFGgsh3AWQKthN-ZkIIPi4uET4w5uFmcp7xN25LOxgRV6HYUPRWml5xlh39Iavrl2NXi6e6wL9nzzMPgVsJVBk5VdJ03Tzu92j-wCR-9zXqysJDRiWmE0dZH_nj1pthyXlxyLrAtP-24Vj1NtDdi4V9hCTDKy2JnNq423bWG8t7s9kviSIjBTrpSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت دفاع: نیروهای مسلح آمادۀ پاسخگویی به هرگونه تهدید و تعرضی هستند
.
@Farsna</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/farsna/436178" target="_blank">📅 17:18 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436171">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cgzrl_FtUI1lQ7d4zFpApBu0-NPQiqLQOqHgPFUfVZOIv-r79RNmqTs5Z1UTaDMUEWVFhGRayuI85H-pti39pDIDGS7goE3geWkaBSj3YPiGzToYJQdRfevbwj3yGQ7E01wLsFV9b3T3UKGZa16QP5qDbfdTAfRAJFLYv-4blXJeQki8n7JkQ6VSJXOVweg17NX2E7AiWFrIrG2SN4dbq6_uCRjs7b8FrR06yx3rPAZh9wdDpiK7ZMjGDIih6-PxzLVFSvQHzS16p3IIp4WEfpEzZCh4JlFgl3Wo4eDzhxfhKz9rKqqc5fJ4c7OEB8ONx1QWWA6Z9s9UpHsRG2vukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PH6PYlI-Rcb6JHo5saf6ySiykrvIz-H4VvUlbghKzp4SpLtPAVUNjzXQCdiKDOF9MDDdoyoCV-InimNk_fMzx5c_Y8Z83xj-Tie_0ppOBYKRjduzk62LR-Yj0h9O99CWnTu9yiUcRW-GlL5kmepblNc0E11XMgNBRCv5Z0XCPAFABYq1OLwlqB6ihWqV2gdhemDK5dzlVqB6oHfxw5S3kprnST02euMgXK93d8-X4MB_97YIBBMZARY89gu19O_IM_XVQrpe4cOx9rUZbJKjdY7Z0qXM0tTq94oiVObHHxGGs9kJZYouWzMZnA25r6di8HvrFX-knQq4iGjpKMP_6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vd2Y20-mY2A9AlWbiAdaIpV00h47FNdRXECdd9gcaCPRDk1YQlUbhZWWb-b55hwIpBzZbx7ylQ706eA7D7oF__JGWCYvzDzg9hwXCy0_6ZDTR-mWleH922Oy_QtbIMq1uE9cNaWHeXqMRAm60PhmzWIJ36CjSuRe21EcJStOVHkn74KqhiKfuzTE9hovduvK_M4n-51bfD1KrM28sEXw248_-y919d4jIqGclSum0WqSXH_fjZvMdD8wMStuIAZhyU_iQU1nwCJSiIlGKH0ab_MiKCK6AKg-LGYoTIAnre3_KrteYSraJoWCmmOfhSdOWDsy7cwRwdBPl3ilXxi1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VUnJDUaiGvWEujtCtgPW--etOswcsDZRjvzNah5Qu_2LjcQR82sDf7XPJYOev1u2StzlZA-JtTRFr096j1eEHoxpdeerQ6NFfOFcXRF3RHRHs2g5K7Cni0lKtxsygFZUEt3MKylPvGPWR8F0FA_ygsMrxOF3YN9Sl8nMOu9MlNZPN5fpqncMbql-NqU9RHpDzL6xxYBA8OuV49yF5e6lUwi37EPaz96Ypo4wtiJPHQs2kfAGpN7jEKPcnjXTeeH4WP6bQoGqzacuQraXVEhOC0LqEV8pjuyd-Q22Hqg1dwvwTDnRO0E10DPMcPQLewDFPCe_gV6cvE5NCu2cw8JO4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dL6WavJL8HY3P0XSXU7TdvH_kNo6VrvbY8sC9-UXfIGJzzqSO4K8qnHTNeo0i1igB0B-ceJ574jFoSxuOZXlxWnfml7JxAq9RTG14Z7IXY0nj8VQsu48o0jNSWAGStdMtMTRH7ovhN-zGqKbVNkaXQ0di6jAAAfJ8IQNsQHAZSnQ0hQSlHIs6opijqw7lR-AdrHYKK39S1OsebmVdWuHNz435neORcMA1IyOi4b9KRxs3zFLjpZATKOjApW_woqyeLLwQN7SoalZfCn5XAS6G3ng8031T93Ufmhh8dFqSzgAye5BoB8G5BaDW2nUMNuIADrUGKFKpRUjEtVz0fW6YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GGgvE8GRNHu2thN-uFEpErAb5BEnlWSUunu4p-W_Erxt-eeQN9zIZkiFoTeKvmeJMMwYXnGA-js8gQXleWtQ4tva_QUEGJ4OY9YIpOxRDOt35lGnaNfGzD7O-ES49hqZRh4oI20sGgFQ0JJm3YGsu1eJPl7cjBKrujvnLJ_zbVHOgjDzau78jMWmv-v6om4T7FtnyG6MsJDrZ0A76NiaF8nw2urffEg1XsIWi4YUrAxmDQb2XYS6kNGIs3VsDiIvaCPYbLry4pDMOMI5J12hWIDlHAnEGLGE-xfRfWIZoOxOY4S4_VG4eO7dubQSRENEU1pIBh9eQVOnHatyJmzFeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eJ1c_8xjS5llBd5KgCgP6rBKOlQrTQn14F-qL86Fr_o8d6Nbr411ENtKPuI6BaMivpGV0fyDpMoneNj-tgFs4Wse9Ij_-mV4-xV59fFmcCSxjSPkXNSNQrslqo95C1HDbyZawdkgV2s21qdsGdRasn30ueKd-yDEpCcJfKo6LquiyG1W26CMCXgHnmnMBoYdg0zc2gJMv759rBt1l3MIgxma2-t36KPPya_HsDEe09lBP53L0kbCMnBAlBG_VTca1ZY2KpOr0rZMtENN5zYpKSZnFzXpqpJAfatza_3xlXIX4SlBYTzX9Eq3YpJKUn270UcTUMvSIq4laVUZB99vMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم عزاداری شهادت امام جواد(ع)  در امامزاده صالح(ع)
عکس:
محمدحسن اصلانی
@Farsna</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/farsna/436171" target="_blank">📅 17:18 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436170">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">هزینهٔ ثبت‌نام کنکور ۱۴۰۵ چقدر است؟
🔹
سازمان سنجش: هزینهٔ ثبت‌نام در آزمون سراسری سال ۱۴۰۵ و همچنین آزمون اختصاصی پذیرش دانشجو–معلم، مبلغ  ۴۰۰ هزار تومان تعیین شده است.
🔹
همچنین علاوه بر هزینهٔ اصلی ثبت‌نام، مبلغ ۲۰ هزار تومان نیز بابت بهره‌مندی از خدمات پیامکی در مراحل مختلف آزمون دریافت می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/farsna/436170" target="_blank">📅 17:12 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436165">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p9Xtxw0WXhMaM3fi-oNXCuRPuaNZNHlBIn_D5k4b2acckm57bJQApABdh9vIC5GlFVsivSDIOfAGEuMutx9XqTi1KByzh3Bmiq91q-Ku8Gay8f-K_DyayrXQ23qgPV5pN4aLdbUVtbMxVE_orv9ViTeNTuIYP6rM612y-8NGG18oZtoVGyY6zXTMNuS_Gtbu0i_p4qY-QK5Y8a5WjNvPQYSbrnifWz9YC3xvRUFdZKHdUD3UCXKdt2s_gnCLwTqnqa-m7OdSMTihhswKIVY0g-Q3zhZpxbcoRHh2B2b3a6xFder0ZJIYLqwfA2_m2IUhJL9FKeJszaEXDgavAmINew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nlx5VVZ6Ze1jxJJ2c1czb0CtKnXtwIUk-PJYCfuwF_VTvQpuWBVeWZw3vN1T8O2FBc5C_THLRKOn7LDyHVpgx56mASO0UyqbOUvyCuos7FzHJMjyFO4njXNyQLgj5Sq9ne5wNXgfYAkwOGogw0L-dnjWI-fEh7X0Z_TWhk0NWIZ8nBme0SVsFmcBfCNwedY9BtzLzeH9M_H0G1ohyZYPWPdwY-OW5qR0coAJUcHo4cZsv6mPQj7F4xC5-9zYftl_rO9yXJPuWApXF4PIDs-07tzPfdXWFZXa8MQBsi6nZNZIbbhOC0buNPGgJ8jHg352gcYSuBBdEPZ3DnYsOiej5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LQIndR74qYVHVqoljsF2AFLA691F4bcGGuTXTtrglLrcOfwBlC91wXiaNs32NPU7V-OBaZttW9w5MKw0UWPuH8hiFKdUe_MZ-HO4XsCYT0KZHeFx3xVlN2vuBMddYY9XIrgt2qC6Zx0Mm-Pmwu5fCksMasepGKLltD25RCQe3cB5UXC3bam-T2-9nZ0iTeG0zDbTVE1x-IJP1IZLgVax2kyWrx4kIbCtbmjmTfNu1d_DPfm-T-5Wt1RRearaC4DTF_3U8X5WjkAFbBNUtwidGTYZMMkXMxlevymQZqoeX2casMD61AlHnqV1cBrXXOhsgBHahh89LYapN0SjSHAaqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XglKIrwcm9ZCz9a6WnoqPNZIB7p0nZtcTMhbelkPPG8m0YBl2QdjPdi-TrtyEBlmwMSvt2uyRO3_KjC6hGXgv8HGU0pOW-JqGMGSXVhc_9KYYSZ1y1IA9g_Wp2Uxta0IMRHnm0MkAGeR7VceZ9eqTxvTACHXAykSNph5ziklzz3C7DBoDmCNd0ZWE0vzGJEXCWoGNZoVv58J8ITRFkSl76wZiij7rSdHWQWUQVGjbGTYpPPlNxPB40LvYlAHBrvqlrPzmCxN7Tb5pI5OPlkwBcoWZ4-hYrtZebRKc-v1GAsI4oF6WeK7zWhAYyoZvETiMvXNKnQ2PhTswlY1B6QZCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GirfmAJ-1oQYtVRWxbH9Gu17UrcoqxKmZkGtK2JkSJe-7CcwDCTySkHC1eA-gO3bfDUgQoPzmBoMhcau156TosixfIuPLIu9yM4KVzb2wU0NT2qdiJ_QAoidCjqVQpGYeLvSBkbJHo82jDtKA0VunBu2Is6rpgAboEDvTcsttS18GqfGcMn-OQeH9elppjgNOQJkGy9iU_f8I6oCklDpC0Of21gJ7e7Ga_uf5TkseHtCVD4O_WkWfdP94SdptSLv8pgnUnQMbvcA2THf7mu8L4u5K6k0gxiOBE0FteOd4pDlQr3M7jf2D_CFjnbY57_YfnfLdcwReieryNrgVxq3hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وزیر کشور پاکستان با قالیباف دیدار کرد
@Farsna</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/436165" target="_blank">📅 16:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436164">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/280d1519e8.mp4?token=o1IeI3CHgfuIkwx6tGZceKUt_rxkWwAEIVHylcvxfOCVuCRUGUxRQFw8QBZ8siDCZA6i4XtjmdI5uCR3-1yuK9M3_Fk01WjPYmJiY6yaZyj5dxQmR6H9oHy2OZbOTqAYYB9uaD4TrC9BYJQRy-nqSK5swk6KCSCExsDIJDv0AVtmMRH1DXbyGMafP9gOZ2u3Tq9LH6oim4blkV2JvqDVJTpHMFHpIqvKbditzbi-zqQQU8aLrIPetdC8F1-fR5ouIVLN-EjrNNphRahHp_THePhzHZrrV6vQiINJIICIwK21I2qOT6Ying4IgE40zcnW_52aawAaK35buaB15EQp-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/280d1519e8.mp4?token=o1IeI3CHgfuIkwx6tGZceKUt_rxkWwAEIVHylcvxfOCVuCRUGUxRQFw8QBZ8siDCZA6i4XtjmdI5uCR3-1yuK9M3_Fk01WjPYmJiY6yaZyj5dxQmR6H9oHy2OZbOTqAYYB9uaD4TrC9BYJQRy-nqSK5swk6KCSCExsDIJDv0AVtmMRH1DXbyGMafP9gOZ2u3Tq9LH6oim4blkV2JvqDVJTpHMFHpIqvKbditzbi-zqQQU8aLrIPetdC8F1-fR5ouIVLN-EjrNNphRahHp_THePhzHZrrV6vQiINJIICIwK21I2qOT6Ying4IgE40zcnW_52aawAaK35buaB15EQp-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاجی بابایی، نایب‌رئیس مجلس: اگر دشمن به نفت ما حمله کند، کاری می‌کنیم تا مدت قابل توجهی هیچ کشور دنیا به نفت منطقه دسترسی نداشته باشد.  @Farsna</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/436164" target="_blank">📅 16:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436163">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ثبت‌نام آزمون سراسری ۱۴۰۵ آغاز شد
🔹
سازمان سنجش: ثبت‌نام برای شرکت در این آزمون از روز یکشنبه ۲۷ اردیبهشت منحصراً از طریق درگاه اطلاع‌رسانی سازمان سنجش آموزش کشور به نشانی
www.sanjesh.org
آغاز شده و در روز شنبه ۲ خرداد پایان می‌پذیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/farsna/436163" target="_blank">📅 16:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436162">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JU2q7A5Lv4cq8vA_x3c4CAAw5_Un3E2gy2-Y3mtQf1leFtOnPNDLjafpk8gIh1pDb-hvQKbh2uc_t0T7nsEzuez-BYaunztVdP9WRPJ8mZrwx003vcvE4tcegvsqMkTaDM0FfQsq4YLOb70DB5i8uWyzD9c0ryIbQCa23SYIH0eYdMw3OU7IVML74KnZrceDpSGfGHKBaZ3lPReucmdv7y4v5gWPUpOTy6OQp5g_bs8RZwXl7wVi3NHHIh0hvfiBhV-JOeZ-GZgKLa2b7fITQWscROHqPyKbIYFokUMo7ru1qHHDqIm442b7ZR1TWhHXoJTv4FwknZebc5fLEpkf2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مشاور رهبر انقلاب در امور بین‌الملل: به‌زودی واشنگتن باید با فانوس به‌دنبال بقایای اعتبار خود در غرب آسیا بگردد
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/farsna/436162" target="_blank">📅 16:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436161">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlpPKq1ERkwtCZKTDqw4CFzULTWsU2Aho73M3CPpgKw7vAcfpp9IVjSMVlDIrB_hISoOi7ptSTyR-3gZem3ECXAH9xJZd7yyWn895gRySm5OQm5i1O_J-pE0hfyJ9vzzXpBkLQmMt34odVh2hKe3-dXPk-m8GllGZz36eprI5hd-DfQvQ1cnSjIVlNjFY2Wk2YE38D_UIb7cC5G7d9GGRJ5AtgH4p8lGPTuL6LZ7mgAsaWBZM_Jeub9HhNtTqkJaSO2vu1ijcMLZIyzWiMkaA4j0zgfzvYNqPdVh-TZ3VVhIOa2j58nFMSNGAKSUCqZEoVzzJF0tFroSACcGzq_w9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام قالیباف به‌مناسبت شهادت فرمانده گردان‌های القسام: شهادت الحداد در دوران آتش‌بس مُهر تأیید بدعهدی دشمن است
🔹
رئیس مجلس در پیامی به‌مناسبت شهادت عزالدین الحداد نوشت: بار دیگر دست جنایتکار رژیم صفاک صهیونی به خون مجاهدی بزرگ و نستوه آغشته شد و در زمانی که…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/436161" target="_blank">📅 16:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436160">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0c7e1bde8.mp4?token=BHBqbLc80ldHjdK3jAXyeKc7KcWNWuI17QL3Loblkm0NHjEJ7O3n0OFB58o5cc_RsdL_aarIS-6-4irkiuVVwDe_mU70yKVzNOr1d4u-q933G4e4BjxhBsV-FCYa_3KVIi0qnTjojXxsevCpqpWt2efJKbcZP0whj-tfk1pYHieAxD430871dtcypooIkP36frIKGjx_M6CLajNQixw5FKuowXPtb7gQhtDMQQEpdM3qdjEyCLO2Jjs1srG3szAUMzSmmvHmL1OpErz2jtF_L7f9xYy_icIHGidzuAGDTS5_VOm2cXm3VYIZ42f74GfzSCAqwgqB1yuPd_DaL5GCeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0c7e1bde8.mp4?token=BHBqbLc80ldHjdK3jAXyeKc7KcWNWuI17QL3Loblkm0NHjEJ7O3n0OFB58o5cc_RsdL_aarIS-6-4irkiuVVwDe_mU70yKVzNOr1d4u-q933G4e4BjxhBsV-FCYa_3KVIi0qnTjojXxsevCpqpWt2efJKbcZP0whj-tfk1pYHieAxD430871dtcypooIkP36frIKGjx_M6CLajNQixw5FKuowXPtb7gQhtDMQQEpdM3qdjEyCLO2Jjs1srG3szAUMzSmmvHmL1OpErz2jtF_L7f9xYy_icIHGidzuAGDTS5_VOm2cXm3VYIZ42f74GfzSCAqwgqB1yuPd_DaL5GCeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاجی بابایی، نایب‌رئیس مجلس: اگر دشمن به نفت ما حمله کند، کاری می‌کنیم تا مدت قابل توجهی هیچ کشور دنیا به نفت منطقه دسترسی نداشته باشد.
@Farsna</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/farsna/436160" target="_blank">📅 16:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436158">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27888157fb.mp4?token=feGI-Q2mku6F7ojTa1v_UdQkBqDG9ZxvGaXMYKvrKFhiwAShYRC0MV3DhwwV2HHl9SRiCafgHboDazfl0bpQGk5LbYiyWhYajcqux_ibGfaZL8dfASDcgnngQZEdb5S5cPG5Uwba5ZB4WGBZBXoXtxSJCBfPoqC1Dff6xALCWSSF_URXCjO5CNlIH4y01NQdEpZcQPHnsGAt6f6HecFFySYjerkk2fXT2AZHnU3CrVG_4AH5XLM7GxXXmzPXU0tYn0SwrOydZwqL173OpvkM6FzigsPG0iDGSMeJjhwVy9-xCaY14h7QjyzyMUYP0YC3FuEyAmn9Z85g_5tHoxRYoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27888157fb.mp4?token=feGI-Q2mku6F7ojTa1v_UdQkBqDG9ZxvGaXMYKvrKFhiwAShYRC0MV3DhwwV2HHl9SRiCafgHboDazfl0bpQGk5LbYiyWhYajcqux_ibGfaZL8dfASDcgnngQZEdb5S5cPG5Uwba5ZB4WGBZBXoXtxSJCBfPoqC1Dff6xALCWSSF_URXCjO5CNlIH4y01NQdEpZcQPHnsGAt6f6HecFFySYjerkk2fXT2AZHnU3CrVG_4AH5XLM7GxXXmzPXU0tYn0SwrOydZwqL173OpvkM6FzigsPG0iDGSMeJjhwVy9-xCaY14h7QjyzyMUYP0YC3FuEyAmn9Z85g_5tHoxRYoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جاری‌شدن سیلاب در خیابان‌های بجنورد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/farsna/436158" target="_blank">📅 16:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436151">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UUiYD2f20P2SnyUyJhOnQ-eEYTU2dKQamsDmKFEHm-QUr24slhcz4Bf_w00q5m6z_x8hqyDqTUsCKce03da272DO8hqQZzAEfrYiZ7aKEAglEGzEXpZ0EaHeUVKABl2I9KQbJJSAqOa3CXq0ssxPk6sbxlBETQrhnt9P8X7p4p8PTXSVHeShLo75ftNfqKOl7dSrkJ_AnQXUGefntFfKgldslYxDLE2yna7wHfTc4JU9JKRYj9_XRMFxJrlaHuSklRSsljSVDl1-5go5M14YAMzASL7ccv3vMyNILVBbHukSE4CGnQYJ9AESkNC3-TgSMLyMWPPXZPC7GHF6G-k_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xy6FL9HqkuCKx5lBL8o4ttgazjjPFQc2qeXYbrSsDRFVDjxc-EKS4aa-iVosamnnE_k_uBAEEYoOj335v1691rMbSPq9M1APDJCQnXJKQAc5-bLlT1PmG6IUP5w0QxWSEGonVxQKdbe2mFfvcG1ovY4tU-ucZc3AK4UzMneyIkV6EnmLL6F7GmMg_NcEfDbiYGJa9oLQD-wlr_mzN2re5cVGsOYNSHh7kfa-yXDZj6Gs6HPAsx3eCRYqb-oLPgfIjT2flaOttq4rC_OvxvNla7TltBx7Eppty5mg1_8dZjP39wx2iHlMWxgq66TSlA1Sl2bciRszENE79-jvuru6pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eqbkUQeN_XtMn1HX6ISR62lvuq78qCnV_rGJhIDO_ivUtloCOlE-tbOGlXaI6nqsKJYQ331LXpzqOryXAUkVNmxzk8gdLyxcAZvHTYqbepCp7T5EDfmIXLTPMbjHSxMsDtgYGVVmayZxSp0yYhD8c20zKx-iAex49Si2EgajqkS0XG7QH8XiBQgHrSOtZ57Hc24asfocZ1FfUX_5_4mxj0N0GkaYzpHDXMz5EHO-3dqm4TzdWye95K2zfC3Tk4bi76Fa_yLV_8MBNRYhwqbvG8rzEr0jNkb9F6mpO640qR0FQj8l0b52NHQGHu7_PL27u_TM-KDinPOyPWbEQ0exVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/no0hgBqH8xwzE_r9jOBzq2V-d7V5tZIomL2WeZbgq8e8Ys_ZVWpxttdTVbxLLtMy45MT6SUXAI2Pc5TmWytIWM-ZLCW4YBlPp67hoj_s5rAp26mexUYMyDtmu6nbQs9moZ-tOUdhU1WikguUm2tITHmFmWo-QNy3k63l6Y82qL27oF23-Y8dhKUHxWBvvPLg6ZZuF-LUN_Gq8LtNihLt1omLIyapQlEtmwyAUkly7mLaXrF6dHHkQy-Z4kULpmr7UXdZ_ndTzchz95ysRFFzgsuWtbR8PTU07RHAX-uPt5vtMMhOe-_Q63kmt6CaKyeKTlZDV_4UlwMNxkP1b1ZiCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h5Iug8w5xlaw8ht9HZ23aj9tSTNj-kKNErUhF8asFvmYU_DkKxtNxZwjqweP7WPcrXm3BKuI9i0oo7gfyDvyegE6Xj5CwZMrjX4WVZis8qtdP-1YAJf7uwdhHHacFC4Qm2uDIgFT2LFQqcCeBfKiHJJlQmX5qjZPes-j1s1cXGlpFSuiu4P-unuM1RTZDw8CyYGvifJJnuTDNUDnoDdWtEum0KSlWwe4-rZ09E9ytGqC_b7m1xEgDp2-aymA85fKie4nz7dkBuUvTrBNC63h5sW4mHOsfQgQNKN6lMMZQzaGpxvB9DZoLCKGbSOQ7kiKA4xL3IUevnLarjkq2v6yKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZWxHgUxCCGx8NbQzfuCA3JrToDuc9_NQwjd3mzATmUJfnmmgbIOjy7axgp92ANs5VCI9zSIrRiHBiaCE53xRtZbYcKaUcm9g-MRDETvuY2sfgxGO9BZ_NRQF1t-sNvtZgAjlJqo7Zm4VkTb86ojLyyOxCnGfauYLcyREf-k1pASNi0nsfTXvuvCiZOKyeA2NxcLyJP7xGLJ_Ixv-juSVzdRxLnfZnOAkTWQAs9JylI_b4UDBGsAwVC7cjz5vxCVFc5GffRMBPDvbAD9sa0guDbL1RFOSQVmsIeufQae9Avq_ZhswUjnQsc3Wkbmpl3B8Q7RrHxlUWJHh_lH6RlcNkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_i6wuJeyoV13JVJ_okWUr5eY1kEDTZZ0IWg80SLG9P9R4Is3X-F30entbJ4e8oQk7Bd-xLK5MAi9yI55w_yHAIKy0zTu7VCQK1BQK7PnZJ3-XYfwhVtXYWGPFuzxzsdLRTTY3YiQVE9kb4mVYff2op-aM0ajFIplyugiZA1gzoNSamF3FUIvo_iqGUCjKs0QgtO5sr3q90Ji5TnZ207C01ojUuAV2BQmg6PSd8NfLakjmvMEcMGhQRD3NdzWnnzaLTV_1ITZqh7jduKsMCU6aCXVaKLms1LxdadxW5sAffFUns0ng6L4ciB4Yq4yj1VvNkAQ4nQgPLYrRO5lssZ_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مزارع البرز غرق عطر گل محمدی
عکس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/farsna/436151" target="_blank">📅 16:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436150">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef687a9d1.mp4?token=jsHD0y7MrDTSwc5UXHwNQ6JbCJQy-dROXGKk-KlcCoXxkSzHxfLunQeGBTLThuzYStjA0AUgzp0tX8fIfW1QqnM189mjFUjrhRog8wSSeUigmb71ZKiMM5MuAWro4og0b5P76HxAoOi8GfVsp3VrPfpmiPsKID6rEn6Ki23RZchy5sE3_8bp09Q3UsoguzUmQ0TETdbSf3hp2qao1_wSUZ5Y70PVjH_v42pqxdsakn-3aaCHbIX1UHN-U8F0WkN7j5eieaehZSzPQP5kNIpgyPx06qmlp4o53M4kWchKCM5i4Cs3TGzqjNSDpeyLLLfjRM7ijLUuICDWXnqucRzuoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef687a9d1.mp4?token=jsHD0y7MrDTSwc5UXHwNQ6JbCJQy-dROXGKk-KlcCoXxkSzHxfLunQeGBTLThuzYStjA0AUgzp0tX8fIfW1QqnM189mjFUjrhRog8wSSeUigmb71ZKiMM5MuAWro4og0b5P76HxAoOi8GfVsp3VrPfpmiPsKID6rEn6Ki23RZchy5sE3_8bp09Q3UsoguzUmQ0TETdbSf3hp2qao1_wSUZ5Y70PVjH_v42pqxdsakn-3aaCHbIX1UHN-U8F0WkN7j5eieaehZSzPQP5kNIpgyPx06qmlp4o53M4kWchKCM5i4Cs3TGzqjNSDpeyLLLfjRM7ijLUuICDWXnqucRzuoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
#فیلم
|
توضیحات آیت‌الله صفایی بوشهری عضو مجلس خبرگان درباره محل درآمد رهبر شهید انقلاب
@rahbari_plus</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/436150" target="_blank">📅 16:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436149">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1IEUEMWOE2mSQWb8vITQg58GqhQ3KSS2PkZWEU3GzEplm_CUKyWBlDV6hIPaoX-bADXnZ6gLgp8o6J0sKtMuDLW7jmdGXL7YZVTLfFvnAX_wLn2OjYHsgB79gmlJRBtDUbVhhl86HenZNAcUXZjrktX4i5yARgeKZFgM5miCnPFyFa5V6VizpT5wdQ-ImS-0xASkDE3k4csZP18ZNYU2vIJdu1rb_VMLilLgnRRMX9klc1g-SwSGxF_jjXWVF6n65z9FIV0mvLE2zmk04IVcnqPgSLo5zC1FJFLOemT-iq_HmGHsMewSIzkM9lUlnan7KjWAFYgHHHsI_6z2c8A8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور برزیل: من با جنگ آمریکا علیه ایران مخالفم و ترامپ هم می‌داند
🔹
داسیلوا: ترامپ می‌داند که من با جنگ علیه ایران و مداخله در ونزوئلا مخالفم و نسل‌کشی در فلسطین را هم محکوم می‌کنم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/farsna/436149" target="_blank">📅 15:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436144">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5AnC0Qgsk_a4DTU7QrmtLnlN5FyWsspwKbFMWtASUs_MmiCeeJyBqIjzgaQIAhLGmXqQeKrMswWxL_T3p4G8HxhNz7lBLvu3BrPTbh26F60l0hqHQ5EorCqOD1NrKvyc0n6VNUA-vE2tyzhPKpXOrlyLj-jjeQuo6QAqVR3YSYi-Ai5YrsXhfCgadWFPjgGzk9jDuHUSyXz8HiPda3COOtzJiqXxTE9nksi1GqbKDjrQIo_O15eSgjLMSWyC3t8yh9fZJZ9SgwzLaS6qBN50hSNUlConKZ2qPKM7Iuef4JT1CvOXovy8Yck8TrrZubVfVE4vbze_JEeIKS2V5KC4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bM0fge9ErvbzrDy5B0Wp8JqAGYcQ4XYlFzgJHu9oFiQphIne13o865eZSOAoyETKiap8sdivZI5xehNiVKc3jdx3xPSpEIolwI8sTqA6NXrQ-VRcxq_-2oY9DWcvprLp49IpAY6EBVKWyydyC4GmaGgnOrW-vcfyKw6VMfVyc9wqougxE3Wl756Psc3K5YnOQv16zmfp0brrMIQtz78E8XC-WWWkEsmZw49XWuCdTkmaQiknBj7cwu3o9UWuNZVBCLp6KwtevhEZQKBOoC8ZeL6sE9cO4ntdLoSIIunGVtuN7hd4jmt3T7li4gYoCYY5xsYQWqn47qqBMupRWvSCeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sQfJZfL6tyc8gaSDwY6pfc23hAzUPjpQ0UhHWF9Aa3dE8OV9dA-IQhROFaP_wZmGQCustw9aXgShu_M8NhP7aAEt-3ktAQTqcGiwsd86dg7TUsRCwX3pzGUsJZ4lvwn8D-m5U_bQEolf1-fOj5HaDcMoRQyXf2Vgr6ChKsdmF5_crESB1nXvxRazWACYxIcxUs3gMLt7vGMRg8wYFKe1xGkvTDMY8w73eoQlGSsRV7gfV29OK4of8wasPBIY4pQ8WDI4wOK9VnnCfcFn_WaCCLXMCN-qD6xdGhGYH7mc8Hane7LQ19nvwwoWmQjttnOIo-yM6z3-lATxck3vAUCauA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tEuM716P4K388EMPHGSRplA_ioi9DA6Z0qn-G5cNk2oDTlOwwT-YAfurMIdZ4A2eXUnkvMFMjtCtcACuE94QwvN8JUvGsDK5m92Wv6AiKknuWS1MVTDLRDSENbhBBKQGAINsxrS5uOEKI3M596KLSdVmA7ZAoTa_X2HahSJf-yDHzPI-V0_7exueXU1MX-MMMKLB8vKQf4Ihhm0cdkGj-TQuzashb0n8P1O0fJo51zySPJYFEpccp-Fe1OQiOM4687gfN7wopViJhDYdAPxfQQXfYkFhhWWPwNTGe8bM_er98GRdfKKZsv3xn5I_YWGD_jL4u3mdcKpeZmWH4nHViw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MocvlpPdF4D28gVL-cqMZaqBVGu7Ckh1QQlgYiJwLOoQ2JjrL1CVk5ud1VH4vz5tPBFTaWN2_v-qDOxUzTP-IXtfMJrELwdyZ4dfGwlwNIg8YLKQTra-QRiDLVQWwFjhEmjHO7AgDuL9DhZPW5JqraefZ2uGfEXukpLwiuNjNCzeW6Ic9Q5q-H2i_4YGENMsXHpD6nCwyP8ZgXLXRxooHB-EzaAAgm47S-iNVipkhS9O4U6dFE9Ewn2zZ2sjyFVImBafIbNsbH4pf0mhngp3bNxcuLdoMQ3ISlujHJ9fo_1dj-soAVkAaGKWjk9hZkbPR21TK5arVFgtnUFtkaA2Hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور قلعه‌نویی در مسجد جمکران
@Farsna</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/farsna/436144" target="_blank">📅 15:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436143">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdYqMDikG0iQ1rXAB6nlxJqAPBoSwkcQfAFafDpYSVIgtONwn84nUooZMa9pPKdokqoGxdZTgg-KBfeU69wo_c2KPmGofOfrFq_esJggtHjnssLg-yAA590I199lJ8QAIKOxlnFr6RlsmXeS6Nh3OlRJ8AgiHwIMJYVl0skVB3UiHR70T8mfVjrbdkjuC2Wf5F2GnshW1ve_sr_YcGaHhH6sgulV6_XmvOEqHR93J_hkMogXlveFotRdqdTMuDNAE-VNPO8YhpjTqMwbditHT0QDfL-aJmO3c3qWTgKboHIly2r5KEmcfV6Ow3Bax4NbmB1hPfdtelRBZFxm7WxH2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریزفاکتور دور زدن محاصرهٔ آمریکا با کمک میانجی
🔹
براساس نامهٔ معاونت اتاق بازرگانی، طبق داده‌های دریافتی از سفارت ایران در پاکستان، مسیر کراچی به مرزهای ایران درحال تبدیل‌شدن به یکی از گزینه‌های جدی برای دور زدن محاصرهٔ دریایی آمریکا است.
🔹
طبق این نامه هزینه‌های این اقدام شامل هزینهٔ بندری، خط کشتیرانی، سپردهٔ تضمین، ترخیص و حمل از کراچی به مرز ریمدان است.
🔹
پاکستان همزمان سیاست کاهش تعرفه‌های بندری در گوادر را آغاز کرده است تا بخشی از بار ترانزیتی ایران را از مسیر امارات به‌سمت بنادر پاکستانی منتقل کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/436143" target="_blank">📅 15:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436142">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
حزب‌الله: تجمعی از سربازان دشمن اسرائیلی را در چادری هدف قرار دادیم و تیم‌های تخلیهٔ مجروحان دیده شدند.
@Farsna</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/farsna/436142" target="_blank">📅 15:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436141">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDIIkWYfuTfC2YBCLjknsN53C4XP7nSzQ3zaigo87GCOSwy1yOochfx_wEx-zBKC7sJnmvaYPKUBRUMul8B05W6frSkccj53oJHObHA_jc-qFEoEIGslACndPulHo6cBxtFleO474RKLQyMno5szVsqhE7r6j7HPC8dMT7inNQAtSo6FGRz89B-igrM6MIhpIuihq6ofQwl7VpMvn1WPanFmGbcXNeZVw3TZQuokOu8Ij4kLLPMorZDJ7l9ifM9_AohWNHDsPheQUPXjC2QoQh0_rfW1ekB7J5H7w6zjObpCQQ7T1_v8dXslSgzzq81ziIKA_KsIyLSmyijmw3SJfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان خواستار آتش‌بس فوری در غزه شد
🔹
رئیس‌جمهور پاکستان: خواستار آتش‌بس فوری و پایدار در غزه هستیم. رژیم صهیونیستی باید پاسخ‌گوی جنایت‌های خود باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/farsna/436141" target="_blank">📅 15:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436140">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/340656f1cd.mp4?token=DJ7jqXTonD6PZtPmVOuX0RqWUVTc0SkdJ8f5aarLpq_aTLbkfLK-xP0AV8b1EbG1aQCXxg6QcESN5kyYrsJn7uXRfNsfFxcprd7l-kypveBpX33DHu4aT8VdKlSdGMTJTYKuY4X3-GTcZqFReMCWUNzUBzhEa5GHdybch4Pu6qZmV6tUtIdwdWLnjcevxaZweJZEJos3q-K52Td9ZtQIhtRVhEEs5WDoZDW3_dZhYCX6YE4w4Z1j-xAuCP0YJFscs8gHcx63ch0wXQFs1WWqQbq88WVPDrhPu6qynO-wW1QR-zqu_MEgwraLjb85tGjZF4csu2SrM_mASoAVciYX7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/340656f1cd.mp4?token=DJ7jqXTonD6PZtPmVOuX0RqWUVTc0SkdJ8f5aarLpq_aTLbkfLK-xP0AV8b1EbG1aQCXxg6QcESN5kyYrsJn7uXRfNsfFxcprd7l-kypveBpX33DHu4aT8VdKlSdGMTJTYKuY4X3-GTcZqFReMCWUNzUBzhEa5GHdybch4Pu6qZmV6tUtIdwdWLnjcevxaZweJZEJos3q-K52Td9ZtQIhtRVhEEs5WDoZDW3_dZhYCX6YE4w4Z1j-xAuCP0YJFscs8gHcx63ch0wXQFs1WWqQbq88WVPDrhPu6qynO-wW1QR-zqu_MEgwraLjb85tGjZF4csu2SrM_mASoAVciYX7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجهیزات ارتباطی صهیونیست‌ها هم از حملات دقیق حزب‌الله در امان نیست
@Farsna</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/436140" target="_blank">📅 15:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436133">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t_wwyZ_j-BDXm42CUQ5ZegHATN3QQNTicr2OKftM7aualKZf0t06qp0VELOoPUOlCMJCBwECpAdQ_xUiuzZNtEtjKQoWUAuCbTN66uXXj1UWHLUEWz3QMWygN4sS4lNqAr2tkqV6d8GdQv4zbxuhQbOy8e43_uoIhZbBA4xWIlhNCaoqQpZ897rd-8hko9F2X6RBtDsIelAk6NMI-BfoPmk7LyNMaiQCpa-sldEVHsObiImMjD4etkpev3APKtIqwgIkugyyLczZvFrTKuHc-kKzTCmTdmR8GM2oMQYxHnhcvTJTTiwV283NO48Gj_Z_x0Dr57V06Yz-pSMuzhY_vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4EghAjnH8uiSmFThfP4KINwU-dzGYSyjJeJYWrbNF-pjICO0CqIVnDIBA3x_9b5_LPlm0cX2gxN5V38YHkBw-e82QuPh12eKArc1JzXBXtqVEQAFM_2Gbd3a6qrVbLzVyOK_jIB3efFoiUf-zOydp1qTvd3YdfG7FWfd4bMdn0lW1r2x-qAF3qvwddRbSOpMptvpc9kAiAkGOBiMBqaLd4cP-rUTnO9OXzGrdms0Wz1ziqAC5HrFmG02cL1X6teGFRS9pjtRKiIkdwNJ9bHqS8u2xJT9k_s-Ze0oMs7ccC_r1AhfCdI1p5Qzw2BF5y_BYk_qZzgs7IvErKdc5ejYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rhC1JImoH7MZKrFpjNcIAeYec1K96MbngWR3KrOcVL4ARmYE5lg2K2nB-H96tygrUFertoWCPVerHrjnG8v_sQ2QqjXlQdV-aWvr5YMrughpCMOZNHk8EoPFHel_nreKaQx3ftD4FBeI1keCanjV9-q0wX95fboE9BHegZ59JyfkICPbJGui6nA_U1NirIS_okGHDFTmPY_9KlTwKBlhbBljwporMEbCbeHYoXjkpUa_tNLvlRkDmIcVflJDnBcHIA6lNObAU2b5WOJhmUaGbIf3MHEZk4dOgH2Y3K0H4TWSRRoAiv2hQ1bJKLeLAzvsYqIWKawGI0EhAbD6UU0jpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RrScIHDMcCxgs8P8ophXfKG4UbI3TNCSsrGN5fvPIjTYwZ8-jWYOf7RFlm_bfRrRBcdjVGt4Czi2h0SpGTFqD_uT-euFJQdfxCu2DSubEDdZ7C7DAH0ThC4DlT9ArhYp5Ezwtq_ImDG3yT_wGX4RcC44R_20pXdFSCEvWbDk0XnZVwMHu8OATj552UzzwNTzWmgS4FScoJqkhPWw8FGsHZRIUlNmP55cQJ_cdIYNwTv_M3n2ddT9ziorfEByygg4aNAwnnSRERgjM3Sl-BsLppFsDMoUR7AYwYr8cuPBUHL_t_KPGIZMBVWNjrOwmC3tUYlmDGrDCLKFoLlpAm85AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JA9zqv9wTwzF8Uq18uAmNQz9Si7gvcBDQVBPhriAFH5Xnro34NJLc8P04QEZyfa9PEsioNlUGNHQ2jlAftZOf9BacU60tXr_YOlV9tUAxHv66hWd7KxYxhVMxcQGOvUZZutqpxAPgfbUa8K9o8cA_OkFhExKrkq7XhAY4M4D38BeYhYisTpBpwOF5Nz_l5iAOMvtQ56cHzYJft7pCXUVoc1KRlzc1aBPbCTJ1jqJzu0QaG5ydQB48T1brPa-srRx-i0-QPHnLmzvH669VWjQTxzqc6-ZyXl0_eHibtYFCOPAjNBCpfGg4Iz6jUyq6QzajP5jeFFXNXw-7YMT0I1a8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y-3rNaCwfmhCpl_OVhQs_26dA7IHbYDOy7w-i6dDE8N3GzhI8hh_MhBO9saE70PFSaKe65iCtKS-VqFMAJXXx-n76VG4XcE_c0qVO9YrTOmPs_jvre6Izz8085mOmHkiftg6_jYkEveYeyHJcIpv4gr2nyQBKvU3p7oHVuv2XKytGsh6q6AchwNtBLyQFGQESyRFpEkR2cbLJIYrzNxaWaCzS-k5AGGK5arCB17C6ZEezZi2BCIg5uEfan86zQ0ZCk_3HpcYdWSTXxLcBfP8h1JyiVj3W_m7tXluH1emHUXAcJKVh3IjcXJvumLdZpQA3SQjlqY2Ec09cwG-hapjfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H92rnFhDjOsCJT4OVtwyookqxYuJMArrCjyVEYeu_Hsjw_BmLGzWaIqRFsIuLsEb5Roj5QJKi_e5xb9xvgQEz7772DqfP2-1XgyJvdTP-t_Iu4ML9_aC4Sd5Ug_oRbWCeD0XM9Qr1uSoOrLU1OFal5AipqCSc3TpyFVwcY6paXLG2EjjrmdpucRse2pg3qUMpP6pgIiNzcc0aCG66zZHGg4KdHbCKHgs8YrztC35H6NK2EEzlCaom7NTUQ6ko-0WLN8ZOPfd-lP0NPu50eoI60n2mLbut2TKEUlqfgeqaxET19fmbn0Q3Ok96uQxnNZ9k5sTorObc_dG4b_x0pImoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مرمتِ باغ گیاه شناسی ارم شیراز
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farsna/436133" target="_blank">📅 15:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436132">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44fda16571.mp4?token=fJ0TR49wWQJzao5QkQziQEpxOBHkKBFD8gWX7waVsMF87QofCPolf94t3qxI3JmApSrWhHEC17J3HWcOrUyKWPMzk2Kj6zG-ocSJCZ7o_lFaiQZ2XPUAOimQ73iJ3F4HiPgpLXFspf_1ul3FMTAMctuy6IZ5ntiel74gmrmmtcSGwRckYouVfrj574R-QkPq1N30pD6T57RUunIHAF8hXyeJbesuMIb66x9f6RoFyjlPjNDQBmmohH_5imn0csOtJdfv0rCQkmjGgvi5_ESu2H1MdGdJ0cHBfcLb1kG9iKx765_jsby69Vc_rM2lnQReNCg6gkndF-PCyO1HRb2Q8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44fda16571.mp4?token=fJ0TR49wWQJzao5QkQziQEpxOBHkKBFD8gWX7waVsMF87QofCPolf94t3qxI3JmApSrWhHEC17J3HWcOrUyKWPMzk2Kj6zG-ocSJCZ7o_lFaiQZ2XPUAOimQ73iJ3F4HiPgpLXFspf_1ul3FMTAMctuy6IZ5ntiel74gmrmmtcSGwRckYouVfrj574R-QkPq1N30pD6T57RUunIHAF8hXyeJbesuMIb66x9f6RoFyjlPjNDQBmmohH_5imn0csOtJdfv0rCQkmjGgvi5_ESu2H1MdGdJ0cHBfcLb1kG9iKx765_jsby69Vc_rM2lnQReNCg6gkndF-PCyO1HRb2Q8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رکوردشکنی وزنه‌بردار ایران
🔹
علیرضا یوسفی با مهار وزنه ۲۶۱ کیلوگرمی، ضمن شکستن رکورد دوضرب جهان، مدال طلای دوضرب، برنز یک‌ضرب و نقرۀ مجموع مسابقات قهرمانی آسیا را کسب کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/436132" target="_blank">📅 15:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436131">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3ec27fb9.mp4?token=QVvr7ohJDdCP7gn1_SH9NfBYr_966hH48N-zXN1GknZe5AaCirenWcOskq1E-cigJOEfxxgEe4D5GJlhDwyQ_mz-JZ-gM3THAyNyVTC87seucoy-KnAXQxGvU05PseuQaoaM2VXhsyMD8mydmKJVOhQkGXBH9iAWJ0U5uni6eDk5XexiR9ByhRwyW1rrBalmGYNiegGTrk5BR7eKSc96y3UEMZuVjmr1GJgzoeH3AXbAeATwlKz6cNSkiCv-g16Z5aLKKRQ2DL9-uLTEmGGgs7WFt5iDdr4TAVB0Y6ydNiy7E0PSNRlw3xz2M238vhMyHIJhq-rkZYHc9njLlV59i6vWhP0rmmn5Fe0GfTdpNOMWaOBbITXO7cORAJ4K1JpVVqgXsSSxljYxqvs3TnPGzlGzfjS4fzlElWGxCd-sh2EF_8TUMuYyTzpMkFaHrztSjUIEnriabCPm_sqsiZzO9IQjYY-2BB_jsCn-8nOS86-s2TYit0XGTZkmmRSvEYRfrai0OxXNlxYrem67LWbgBYCluByJPXkAKkjo9QxsTAwyxVwtPOwRntbbBzP_qFUvQQ1v_XefWQCprfJSkLq8H-UKMwgyEB4EOEGR8UWBoR2vJM12hmXoBCMrIXY1S90Xm3wJsKtHLqCW-fh3YSypM4nsW7dobMssCCCactY1cR4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3ec27fb9.mp4?token=QVvr7ohJDdCP7gn1_SH9NfBYr_966hH48N-zXN1GknZe5AaCirenWcOskq1E-cigJOEfxxgEe4D5GJlhDwyQ_mz-JZ-gM3THAyNyVTC87seucoy-KnAXQxGvU05PseuQaoaM2VXhsyMD8mydmKJVOhQkGXBH9iAWJ0U5uni6eDk5XexiR9ByhRwyW1rrBalmGYNiegGTrk5BR7eKSc96y3UEMZuVjmr1GJgzoeH3AXbAeATwlKz6cNSkiCv-g16Z5aLKKRQ2DL9-uLTEmGGgs7WFt5iDdr4TAVB0Y6ydNiy7E0PSNRlw3xz2M238vhMyHIJhq-rkZYHc9njLlV59i6vWhP0rmmn5Fe0GfTdpNOMWaOBbITXO7cORAJ4K1JpVVqgXsSSxljYxqvs3TnPGzlGzfjS4fzlElWGxCd-sh2EF_8TUMuYyTzpMkFaHrztSjUIEnriabCPm_sqsiZzO9IQjYY-2BB_jsCn-8nOS86-s2TYit0XGTZkmmRSvEYRfrai0OxXNlxYrem67LWbgBYCluByJPXkAKkjo9QxsTAwyxVwtPOwRntbbBzP_qFUvQQ1v_XefWQCprfJSkLq8H-UKMwgyEB4EOEGR8UWBoR2vJM12hmXoBCMrIXY1S90Xm3wJsKtHLqCW-fh3YSypM4nsW7dobMssCCCactY1cR4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاجات دنیایی را از امام جواد(ع) بخواهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/436131" target="_blank">📅 15:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436130">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/259c769a28.mp4?token=QEkmQ4NmiNy5pXG-HoSS8nWeouBPq9X-8zJIgWfcURfBIYs51a3vcdI3md1sgroYcr_WAO57r4qe1mPXJTLVOJ-2yxKtQkpiWQ6CZyqC7g9YlD278hIaqb_mgbI8ue1yZgOPC_d8PO3J7v836twWYC6EoMIntFNWXBBbNtyCl1jn4xveHDeVzWf7OSO6rDcM1GhnNnWB6S5UvCZ3YFkP7YcEqOkiC0Kmtuspo69PmJNw5mfFhCZvUqzrlQz7eRhb_KZuqKFYhocXC49TsJUbW1d-kzsTIFQFMr_dA8p3Q5ugC2_jGQuipP2jBkzsYGkOuc-EzyLgSyaTUvaEz7IHTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/259c769a28.mp4?token=QEkmQ4NmiNy5pXG-HoSS8nWeouBPq9X-8zJIgWfcURfBIYs51a3vcdI3md1sgroYcr_WAO57r4qe1mPXJTLVOJ-2yxKtQkpiWQ6CZyqC7g9YlD278hIaqb_mgbI8ue1yZgOPC_d8PO3J7v836twWYC6EoMIntFNWXBBbNtyCl1jn4xveHDeVzWf7OSO6rDcM1GhnNnWB6S5UvCZ3YFkP7YcEqOkiC0Kmtuspo69PmJNw5mfFhCZvUqzrlQz7eRhb_KZuqKFYhocXC49TsJUbW1d-kzsTIFQFMr_dA8p3Q5ugC2_jGQuipP2jBkzsYGkOuc-EzyLgSyaTUvaEz7IHTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت فرزند شهید سردار نائینی از روزهای آخر زندگی پدرش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/436130" target="_blank">📅 15:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436129">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">احتمال شنیدن صدای انفجار کنترل‌شده در اصفهان
🔹
سپاه اصفهان: به‌دلیل انفجار کنترل‌شدهٔ مهمات در محدودهٔ نصرآباد و میمه تا فردا، احتمال شنیده‌شدن صدای ناشی از این انفجارها وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farsna/436129" target="_blank">📅 14:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436128">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6ef998be6.mp4?token=beOtilvV9CgeJp0uU1UUck5W-LLiL7jna50tpqEC-LLNcT_e1JAamhLXDVtZTJAg1Vl_xzj-8Q7EyvW0zwEAcPiAes7r_O-BONQP-JQySKGI5Q3stRBh8dxqKbEf1xqbEyEIL3IvoSTJUliKwzPf71SxBdrKRbikxyecZ0G0Msw1eEfJZTKaQ9fj-irneKfuqgdiuErTr_rkjLruhAdchtlLztLeBgLi4ejqAE9CaeRBbdr-GQB8jLe8xC4b-uhB3P1tZ0ci6YcjHhOBy6bFNIfQg95aMAKNdmqh5rA5Jv-JsbMGjTNVK2Gr4HlNiCMsLD46b130UcDSCoJZiLm0rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6ef998be6.mp4?token=beOtilvV9CgeJp0uU1UUck5W-LLiL7jna50tpqEC-LLNcT_e1JAamhLXDVtZTJAg1Vl_xzj-8Q7EyvW0zwEAcPiAes7r_O-BONQP-JQySKGI5Q3stRBh8dxqKbEf1xqbEyEIL3IvoSTJUliKwzPf71SxBdrKRbikxyecZ0G0Msw1eEfJZTKaQ9fj-irneKfuqgdiuErTr_rkjLruhAdchtlLztLeBgLi4ejqAE9CaeRBbdr-GQB8jLe8xC4b-uhB3P1tZ0ci6YcjHhOBy6bFNIfQg95aMAKNdmqh5rA5Jv-JsbMGjTNVK2Gr4HlNiCMsLD46b130UcDSCoJZiLm0rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشاورزی: امیدوارم سازمان برنامه و بودجه زودتر پول گندم‌کاران را پرداخت کند.  @Farsna</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/436128" target="_blank">📅 14:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436127">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8837ced8eb.mp4?token=XX753XY-VdD9TxTVW27hfzgrMIJGTPSn_xaziuU_TI382XppxjNTaG8IB7WMOuFTXr1LqkeWKryTyJI4691fS-2ZNFi1c784A_EphHcKVtsNahyfxfCMaynrF18QTrSV2C5be_80iWhfEnGiog0nuFg2LH3rD7-yM3zIqYz6QzfrvqxBj2vPsMiAzSRe2rP8Et5_8fUFFAeDZPZAVqess2B-NIyCpnlODg6diNIrgYO2VbK62i_ci_izkO22POlD6qvM5oxMKKybgiBLMVgQn7FqJvFsNfToAhK8Rx10OrEIIc2iSV65hrQSGo_H5rtl2rAX1lJZsfoU8roQpj7seg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8837ced8eb.mp4?token=XX753XY-VdD9TxTVW27hfzgrMIJGTPSn_xaziuU_TI382XppxjNTaG8IB7WMOuFTXr1LqkeWKryTyJI4691fS-2ZNFi1c784A_EphHcKVtsNahyfxfCMaynrF18QTrSV2C5be_80iWhfEnGiog0nuFg2LH3rD7-yM3zIqYz6QzfrvqxBj2vPsMiAzSRe2rP8Et5_8fUFFAeDZPZAVqess2B-NIyCpnlODg6diNIrgYO2VbK62i_ci_izkO22POlD6qvM5oxMKKybgiBLMVgQn7FqJvFsNfToAhK8Rx10OrEIIc2iSV65hrQSGo_H5rtl2rAX1lJZsfoU8roQpj7seg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گندم به بازار سیاه رفت!
🔹
رئیس بنیاد ملی گندم‌کاران: در حالی که وضعیت تولید گندم امسال بهتر از پارسال ارزیابی شده تا امروز یک میلیون و ۴۰۰ هزار تن از کشاورزان خریداری شده که نسبت به پارسال ۲۸۰ هزار تن کمتر خریداری شده.
🔹
کارشناس کشاورزی ابراهیم مرادزاده علاقه…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/436127" target="_blank">📅 14:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436126">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77409e12f6.mp4?token=S_-Nu3YQHaxzYHiGzy7iA4KsPjZjSI1glruvpgJSqcKQQ-vtNOpuRtnmSmKqw7nby6UGSvTFHRAtZ_rtJxAt4QL0D1n334m5aCwgOJwgtTVCbMmVbrDt2knWyWkjMn5I78scheLQo4S5eBxdq2TV2jIaX8OvOVYSp7rd73sbRsF4PMMwI0JitrE6AvVsQOnvo63r04SJ9XSyC_cuVnq3z-9UsWZj8iZNAkHJCrRLh5VcNCQTQzd4EcwI1Ykv9lRLm03IdZlqvcwvO1kwKR8yFAexBnQw8UkQnoqVIom0DDY7QcfUVxgXFDMwe4V-P9QFbB9WBseA6QVNfhkZFB5L6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77409e12f6.mp4?token=S_-Nu3YQHaxzYHiGzy7iA4KsPjZjSI1glruvpgJSqcKQQ-vtNOpuRtnmSmKqw7nby6UGSvTFHRAtZ_rtJxAt4QL0D1n334m5aCwgOJwgtTVCbMmVbrDt2knWyWkjMn5I78scheLQo4S5eBxdq2TV2jIaX8OvOVYSp7rd73sbRsF4PMMwI0JitrE6AvVsQOnvo63r04SJ9XSyC_cuVnq3z-9UsWZj8iZNAkHJCrRLh5VcNCQTQzd4EcwI1Ykv9lRLm03IdZlqvcwvO1kwKR8yFAexBnQw8UkQnoqVIom0DDY7QcfUVxgXFDMwe4V-P9QFbB9WBseA6QVNfhkZFB5L6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشاورزی: برای اولین‌بار ۱۰۰ هزار تن محصول تولیدی کشاورزی فراسرزمینی شامل جو و روغن از قزاقستان وارد کشور شد
🔹
دستورالعمل جدیدی در پایگاه اطلاع‌رسانی وزارتخانه قرار داده شده و حتی افراد ایرانی که خارج از کشور هم هستند می‌توانند بدون مراجعه به کشور و از طریق همین پایگاه و با کمک نمایندگی‌های رسمی کشورمان در آن کشورها این فرم ها را پر بکنند و نسبت به کشاورزی فراز سرزمینی اقدام بکنند و از امتیازاتی که برای آوردن محصولات‌شان به داخل کشور، موجود است بهره‌مندشوند.
@Farsna</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farsna/436126" target="_blank">📅 14:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436124">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lM2ELQLlSrerCypuH09a538JfLEqjCppsbgClEEGmH2-h4OrVuqsEPhC5yeBvPwghWnMCtnwNuvZOFPtVKOeggahVPg1pjZAiItO07y9K-N2eJDrzUZc2IkOdM_lCLedSSzDzO4OCY6U8M0gt0YoDGE9UdmobcS24mcf5JRupHlQ1_b27eJ34Xbga54c1FMywca-5L-qiOanImEYY43PjELg1oMoMJAXHDpbp0ENKapqzLVCFRpf5kc9szZyXlpYz70zN4RsQ3qYQqZEP5eRUCm7LkJ07u4hTQVjxq2_cYjW4L_KCm-rzi8ibgIGH1HD5UPLRlEmlRNfD3hPhOB9ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eaGLmwFkTfeN4Jl7Cz728de-UM-Kl2poxZWYQcHNMdGmFnFFE-jRWjp4ihTPMK4UBGKdR7XP2nORJuQqT4A5vti9vdH60WjknyBokf0K70bAW9FnSMVMbJf2BpMeSqZXM7cEhPVpg-AkFgHiEK1ZIooc4V9pqal1JCx2G6tWHWkt2EAaWHtc99oC6XF2g5ZOlMVoToVC6DHr_POMmZ6VbA_AvmRkb-hVA934hZW4v6kTkrEyW_XBFtcurNL8dT0IYD8pydEKPfXhXeEwmGZutS3soVk91j44w5_P11ud8eIs_C_y7bvbuFMBFIlzn9G7c8QahkZjxqKejKkXr9wdpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عاملان شهادت یک پلیس در ملارد دستگیر شدند
🔹
فرمانده انتظامی ملارد: ۲ نفر از سارقان خودرو و منزل که در جریان اغتشاشات دی‌ماه در شهادت سرهنگ دهقان مشارکت داشتند، ‌دستگیر شدند؛ در بازرسی از مخفیگاه آنان ۲ خودرو نیز کشف و توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/farsna/436124" target="_blank">📅 14:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436123">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فرمانده کل سپاه: امیر نصیرزاده نقشی کلیدی در توسعۀ صنایع دفاعی و تأمین نیازمندی‌های نیروهای مسلح داشت
🔹
موسم گرامیداشت شهادت سرلشکر خلبان عزیز نصیرزاده، وزیر دفاع و پشتیبانی نیروهای مسلح که در جنایت حمله تروریستی و جنایتکارانه دشمن امریکایی صهیونی همزمان با امام شهید و دیگر فرماندهان عالی نیروهای مسلح به شهادت رسیدند را به محضر فرمانده معظم کل قوا، خانواده معظم ایشان، نیروهای مسلح و ملت شریف و حماسه ساز ایران تبریک و  تعزیت عرض نمایم.
🔹
امیر شهید نصیرزاده، که عمر پربرکت خود را در راه دفاع از عزت و اقتدار ایران اسلامی سپری نمود، از سال ۱۳۶۱ در سنگر جهاد نظامی، خدمت خود را آغاز کرد و در دوران پرافتخار دفاع مقدس هشت‌ساله، با شجاعت و تخصص در قامت یک خلبان دلاور نیروی هوایی ارتش، حماسه‌ها آفرید.
🔹
مسئولیت‌های خطیر ایشان در دوران پس از دفاع مقدس، از جمله ریاست ستاد نیروی هوایی ارتش، فرمانده نهاجا و جانشین ستاد کل نیروهای مسلح، نشان از درایت، تعهد و شایستگی‌های برجسته علمی و عملی ایشان در عرصه‌های فرماندهی و مدیریتی بود. سپس در کسوت وزیر دفاع و پشتیبانی نیروهای مسلح تا هنگامه شهادت، با نگاهی راهبردی و تلاشی بی‌وقفه جهادی و انقلابی، در جهت ارتقاء توان دفاعی و خودکفایی نظامی کشور و ارتقای توان بازدارندگی ایران اسلامی گام برداشت و نقشی کلیدی در توسعه صنایع دفاعی و تأمین نیازمندی‌های نیروهای مسلح ایفا نمود.
🔹
سپاه پاسداران انقلاب اسلامی همرزمی با این امیر سپاه اسلام را افتخاری بزرگ برای خود می‌داند و یاد و خاطره ایثارگری‌های ایشان برای این نسل و نسل‌های آینده چراغ راهی خواهد بود که نه تنها پایوران نظامی که آحاد جوانان کشور در دفاع از میهن خود مشی ایشان را سرلوحه رشادت‌های خود قرار خواهند داد.
@Farsna</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/436123" target="_blank">📅 14:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436122">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWoE8c_45AQ26uOIvwqg49DpJ2F2tCmPxPEPXLsdVV4PZBpbtAM7zeabXGr_bD7iDpTVxVmlTvUb9NeqnkybvHnDhsITur4dU-t4tbf9h3yeBKn_enqLXWeHKVXvLYVm-Kbb8vbKFXI1zXSwQV1-Qvlz7e9mjatkaFwW9yeuCZIzgtjVraKzryY1vY4n6Rw5vkmLFfgIHg5yeyMYPFvxE6lZ21xu-eiEFk1hPBNNiaxgyU2B9dnpyyBfnbQ2ZHONeXMZB54_kZmxNdij-GHOXZxA_EpE5Lh5bJ6Rl7dsUu0li-yHndI_m40JoTb9fGxWeVBrOoTfBx4FpI0iKS06hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن فولاد: سهم فولاد در خودروی یک میلیاردی فقط ۷۰ میلیون تومان است
🔹
معاون اجرایی انجمن تولید‌کنندگان فولاد: افزایش شدید قیمت خودرو هیچ ارتباطی با قیمت فولاد ندارد و نهایتا فولاد ۱۰ درصد قیمت تمام‌شدهٔ یک خودرو را تشکیل می‌دهد.
🔹
یک خودرو که به‌طور متوسط حدود ۱۰۰۰ کیلوگرم وزن دارد، مانند کوئیک، تارا یا شاهین، حدود ۷۰ درصد آن از فولاد تشکیل شده است.
🔹
اگر قیمت یک خودرو قبلاً یک میلیارد تومان باشد، با در نظر گرفتن قیمت قبلی فولاد یعنی حدود ۱۰۰ هزار تومان برای هر کیلوگرم، سهم فولاد در این خودرو حدود ۷۰ میلیون تومان خواهد بود.
🔹
فولاد مبارکه تقریباً به همان میزانی که در گذشته ورق فولادی به خودروسازان عرضه می‌کرد، همچنان عرضه انجام داده و در اردیبهشت‌ماه نیز به‌طور کامل عرضه‌ها انجام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/farsna/436122" target="_blank">📅 14:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436121">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_Gs9voMHY_5K6Bz2GckyKLcCQEeZO1Isc0o93wHVk7Qtw78rIuO2Mbz6Xbk6WsuJr6rzwEz05StjB-VFEitdDs0cGGt2M7dN8DGdjLmvMBTh6Q_aNCX_7kdxhN7k5vj421oVLyFyzh28KzU5uhpegGLGocGqFOYKyAXyOP5r0zGQz1JFicorTEDAtTLktuDev2lCZrdowZAFD4SpbRJYWY6D2dvRVq3DjaSgYPb476cNTRJ2SJO5AhLhSi5dkW02WlGnGM6LlM95bVuIlHkXJ8GZHsMfQmiMBO_g7qsbeZyLFX-R6-siksuI8ZrlFagC8Y17vGFovClYMY6FxLFQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پیکر شهید عزالدین الحداد، فرمانده گردان‌های القسام در غزه تشییع شد
🔹
شهید الحداد دیروز به‌همراه همسر و دخترش توسط رژیم صهیونیستی به شهادت رسید. @Farsna</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farsna/436121" target="_blank">📅 14:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436120">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c56f73861.mp4?token=IPC-sec2_SmhPFMVVMlOaheIHtbPUe2RNR-tg28knYH2L5pHp-iWM1X8FQYsZVIzvfIPk1JBmlouAidVr50O2SA91QVRdFfMCI0wVXR2jYi4zpdzOvezN3Dm_GBc8Xua9-Drq5TWm-F8B3oIT6wiH0io7-0Qe-frLdXF83LWOxpF5unDr37GLYcd1lCaTkxiOzLTYwmiWe1H4lNE3SU7FU1UIWCXxCRLAONakKWLgnzZOLcLJVAJwNgaQXjOhWzxibclyMp60u4ZMjXEfZLS55ORReBWXcHbvVEMyZ-H5iIeDhF20ZolfTZYRdEE_qjKPJ16BRunVVdDe7o5rE_JFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c56f73861.mp4?token=IPC-sec2_SmhPFMVVMlOaheIHtbPUe2RNR-tg28knYH2L5pHp-iWM1X8FQYsZVIzvfIPk1JBmlouAidVr50O2SA91QVRdFfMCI0wVXR2jYi4zpdzOvezN3Dm_GBc8Xua9-Drq5TWm-F8B3oIT6wiH0io7-0Qe-frLdXF83LWOxpF5unDr37GLYcd1lCaTkxiOzLTYwmiWe1H4lNE3SU7FU1UIWCXxCRLAONakKWLgnzZOLcLJVAJwNgaQXjOhWzxibclyMp60u4ZMjXEfZLS55ORReBWXcHbvVEMyZ-H5iIeDhF20ZolfTZYRdEE_qjKPJ16BRunVVdDe7o5rE_JFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از آب‌های شمالی تنگۀ هرمز
🔹
آرامش بر تنگۀ هرمز برقرار همچنان است
.
@Farsna</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/farsna/436120" target="_blank">📅 14:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436119">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT3pcps--fzIIXHTVEUjH_hFvUWOZNXhRhQAHtZ3Vf5kd6_tzRxBGbl-G7dpJeXa4TUsPQU7Yf0hL0RlBMRa0Atc6SIm5N4V3jWYTEmxlG5Ks0SYvsdNIIrdyktAjhYiK0liqBe1zMbAH1XYRW14naot2k4nVFF7OrrG4gqLSrZl9vS0OkK0vvVfx-ksN-WzGZ5IQets6X5at8FWeKuUaTrKdlcrVnegOoFzSFDpA8zTgjjaJ1_Bte7wh7OGWOBfquTrDXY5h4GvbZVmH9P-7XtfE0oWZDJmXJkPemxAanEfLGezmAowMZW2uIdeURrG8Xa0QFpC86VkkJSIbvRpQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیۀ دفتر حفظ و نشر آثار رهبر شهید انقلاب
در پاسخ به انتساب یک شعر به امام شهید
🔹
به گزارش پایگاه اطلاع‌رسانی دوران، به‌دنبال انتساب نادرست یک شعر به رهبر شهید انقلاب دفتر حفظ و نشر آثار رهبر شهید انقلاب در این باره اطلاعیه‌ای به شرح زیر صادر کرد:
بسمه تعالی
🔹
دفتر حفظ و نشر آثار حضرت آیت‌الله‌العظمی شهید سیدعلی خامنه‌ای قدس‌الله نفسه‌الزکیه، در پاسخ به پرسش برخی از اهالی قلم درباره‌ی صحت انتساب شعر و خاطره‌ی بازگوشده توسط یکی از علمای محترم، به اطلاع می‌رساند انتساب این شعر به امام شهید و نیز ماجرای سُرایش نقل‌شده از اساس صحت ندارد.
🔹
دفتر حفظ و نشر آثار رهبر شهید انقلاب رضوان‌الله‌علیه قدردان دقت‌نظر و حساسیت اهالی قلم و فرهنگ و عموم علاقه‌مندان آن قائد عظیم‌الشان در دقّت بر مطالب منتسب به آن امام مجاهد و شهدای خانواده‌ی ایشان می‌باشد.
@Farsna</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/436119" target="_blank">📅 14:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436118">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3ukyOTwQr-ps_lWs-3qVvqMc5nCj7Jmxzq0P0pfDL7zhYzYOo8ITED7gP3tO0FOs64oTkcsYrP8rSjmn6lJFUkSF78xMpCUVoZZp2KMSNmDNd-HPv558LCQuDE_Na_wecYymu6KTNikFUaCAfgNziP8PnLvQxrIJo4L-KSXIOf5q7mc_Oia6895ojV_uPH3rLftsCT1Nraiuhq0ft40xmXEs9ydqOsonJ1KZRwxGxk4pJgpnPONEejRAPvAGUBFmHAEKl3Sq6R_yvQlLsLJBEg2l7meio7Je6sGsJlzuIQI6kl1AdWC_xskZW3RQnky1BmclXZPRNbsXHjywJ7mtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پیام تبریک پزشکیان به‌مناسبت روز جهانی ارتباطات
🔹
در روزهای جنگ، فرزندان ما در ارتباطات و فناوری اطلاعات، شبانه‌روز ایستادند تا ارتباطات و خدمات حیاتی کشور پایدار بماند.
🔹
دسترسی باکیفیت و پایدار مردم به خدمات دیجیتال، بخشی از آرامش، پیشرفت و حق زندگی شایسته مردم عزیز ایران است. ‏روز جهانی ارتباطات را تبریک می‌گویم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/436118" target="_blank">📅 14:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436117">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پیام فرمانده سپاه به‌مناسبت روز ارتباطات و روابط عمومی
🔹
روابط‌عمومی باید با تولید محتوای کیفی، واقع بین و امیدبخش، استفاده از ابزارهای نوین رسانه‌ای و شناسایی عملیات روانی رسانه‌ای دشمن و مقابله با اخبار جعلی، خط مقدم این جهاد عظیم را با صلابت شهدایمان بایستی ادامه دهد.
در بخشی از این پیام آمده:
🔹
فرا رسیدن ۲۷ اردیبهشت ماه روز ارتباطات و روابط عمومی، را به فعالان پرتلاش عرصه ارتباطات و روابط عمومی، به‌ویژه کسانی که جان خود را در راه روشنگری و تبیین حقیقت فدا کرده‌اند، صمیمانه تبریک و تهنیت عرض می‌کنم و در طلیعه کلام یاد، نام، خاطره و نقش آفرینی‌های سترگ شهدای روابط عمومی و عرصه ارتباطات، خبر و رسانه، که چراغ راه هدایت ما در این مسیر پرافتخار و مسئولیت خطیر است، را گرامی می‌دارم.
🔹
در چنین مقطعی حساس در دفاع مقدس سوم و جنگ با دشمن اهریمنی، پیام راهبردی امروز ما برای مجاهدان عرصه ارتباطات و روابط عمومی این است:
🔹
ارتباطات، خط مقدم جهاد تبیین در عصر تقابل، و تلاشگران عرصه آن پرچمداران حقیقت، خنثی‌سازان تبلیغات دشمن و تقویت‌کنندگان وحدت و انسجام ملی هستند.
🔹
روابط عمومی باید با تولید محتوای کیفی، واقع بین و امیدبخش، استفاده از ابزارهای نوین رسانه‌ای و شناسایی عملیات روانی رسانه‌ای دشمن و مقابله با اخبار جعلی، خط مقدم این جهاد عظیم را با صلابت شهدایمان بایستی ادامه دهد.
🔹
دشمن به دنبال ایجاد تفرقه و شکاف در جامعه است. شهدا، فارغ از هرگونه اختلاف و مرزبندی‌ها، در راه دفاع از ارزش‌های مشترک و آرمان‌های مقدس ملی، انقلابی و دینی جان باختند و به ملکوت پرواز کردند.
@Farsna</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/436117" target="_blank">📅 14:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436110">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i-reWw211lYi6AjoJTBW925-52Om-zctH3iZRFApspq6Ty4njUGwC0j25B8Nwb2E-jwuHuLR91_DxTOvj9XrRvHBBDXvE-pe6AVCxGYFJ4vtJuP6jJkqvLt7MdgnCP8M0DnoeFf11_MHezh3EoDXv0LYvHv0vpIyiips1bKF8HqQIBqiW3rUjxy59qib1PfbvzxrKqpAdTkvE7wX0Eu-Pw2F__Jm7JMwmTLBFLp9jkUmCKwQEYrnR-v-u6-4pc7-efVP92YxCqNL-MTbHkqf1j6qWuxoj2MXuDqDS1qsQLO7_bR_AKO5wV4SGY8rDm3mlRfJ57Ek5O6-3fA6Dki2Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d81gVOGuxYwAEA8dj7zsx37qEPnGMAuAfuEonqNX1k9MT3UumjptWH1B8EffZ4CEjbxkCgtiVGQMMKEpzxykaQvwLeYwhLAV1c5V1knfyc1lyU9qiEZtwCQtMuI-j15Cxtcs23G5Os_w5gy1iTCS04IReCwen9GZl8tNpYI-QYdBn94jRqkZzTKEbKho8iHn2JyBVbezye0GQ-3oJEBLlyMcJIXQwxTfFhJRSxMFJQcX0yRjKOQZvyDIRnNRuz8GpdNGXy9rXvrIym4PFjprmBN6brXsUUZIpG8r0VgP6c2hS0Bs4EEdvRBaOHEPZpBW24YSjV5BWuOw_FdAhKJYRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D1wCjAdm9zkONLU0uxFftjkWYDNhSNHqWtNsQloSv6R8woprKqYiEjlU6B9wrUWPnj1YXLCHTa_qHXOUfPDfOkji_oNYTJMZNiIQLWX7SnvWRowz2ch8ViJ9jn7QUaob4-kqVMOpJPCHDnL23hDhHGsGX3zQuU_hSMxtLtkjzq4YnuWr7AOlNxUGKQukwB-zON9JjMATS7W4edg7eMSHJCzhQ64z7WSXW0RZPBQ0AmHSzUXLZ0I0JpOvGSaIxPvliZR3Gtvn3eOe78JgwbK5yS-TOKelQet8DHVh0gHiHNUaZeEA82DaMzlhv31Srua9ddqPYO_pIYmPOi4nHJ6BrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mVdFKXSfTEbOUJ_O7o2O8w74bGZSFjbp4vBzuibN6wnLJ_qtjfRODTpbKNR25Fc0JNeZfIwwIwgXANhahEWaHIUy1OH6ROC5paaXf91diUR30nwP_1ro4P1gxD3a9Ufs5-l28mfP-mzIbI3DpZ5T5WRSySAtw6J2MOkWoHKs4gxGeOS4CKg8Y0I-O8uVBJC1jPzA2W8kch_kv8qAPAbS0Edg4tDI-hZWeYntAfmMwnIPqjCKr_v3Xg9La7vc7lEI7W602i1D9cSjjadNLOaDSJKppEPzlTZH_f13RfHTqsyQ6XH26uyVw0GuZ0bOf2xs3JFWNKpPqQ9Di2l6kh2XNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pbZFSK8pg0Zog_R81GDe8QkVqT0o0zx21zzD-5bOw_V0zZd5wBf0udR8WVfDW4b_fEDLi2eE25mO5Z8x7VFWTSraZWOFWgeMCWs2-UQgD6cV8CmAnkwURF75FtZs6Zg3VrFWOIUJVoqp3gl93lkkmaL1TpN1RBjr-OIuotfc7e_hYmIw5Qxh1i7BoTtDIcvZgJ2sp4oFFioOOeePSdkkNg5OX_a_BeYCsyXQQ2raDOC0d_6MDFvbEdmux-0aDIjWohTn6v9fpGrad0YJpvKjSHKR6Deey2HxbFuN7pJYcY_Kp0QSuGsMFF2Lem6VzeVrjtO9u-2u7nu40BWqIFnLwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HGHqcBfvA-E4rnl6XTAMjs8OtPSgZr62xiXf88HsPCvEnd7xn9Lq0EaopzDyMyis4f9OxmzLbx0n9O7lfDJtVbVKMUNrBGecrQCWDLzAVuLjSd8HQ4K-qsAnJLd5K1R7gObFC5R1UpBVprPeEf77UN_ph_GxgFcTX2LXROiJ0LLdEaaiinR_MjyFgPhkOUkuwg3ttEwjNZBeVh_XuAdy-xF2jOx8vCi56e-uQXOvRsh4SvVtMuDyEzcay40SNaBxbDu8I6o4pmlUbOcU5An2f1xwKIXFu-CW5whWlnwqIohU2II4r2B5IvBhoCVMl0zBo7ldg7AGAkdKaQNKF0HD0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NsltnGudeon49ni3gtsEA0BtiQZ6fQbgku1R_9r84dTDCZs0wSd_Ky__r_oABESo1fxHJ1scsObnCoW_RbarEyXZImDL3PIjrsQZGbjJdxGz8wswmN9Cqtgi7XpfRfUyCzABKDw5urcs5SnQUoBGX6YQFCMe4tGJKnT8EgMAmPfP6xa6Hv3kkh_7BYh9os1U9hx4QqYxO4MWXiRrfWFkqZaSwXpQUzU2mWJjwi_UF43MhjOFXF_0XlCmuQtU93CAe5zcKTdcx2S4_7miGtxHUZwc57_NamGVxZU8V9GJQXIHQSac1QBU60EVnA93wulk9kZCHPRNG0v_v4A215akDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دستهٔ عزای خادمان حرم حضرت معصومه(س) در سالروز شهادت امام جواد(ع)
عکس:‌
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/436110" target="_blank">📅 13:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436109">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
وقوع چند انفجار در ابوظبی
🔹
برخی منابع خبری از انفجارهای مهیب در پایتخت امارات خبر دادند ولی علت انفجارها مشخص نیست. @Farsna</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/436109" target="_blank">📅 13:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436108">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
وقوع چند انفجار در ابوظبی
🔹
برخی منابع خبری از انفجارهای مهیب در پایتخت امارات خبر دادند ولی علت انفجارها مشخص نیست.
@Farsna</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/436108" target="_blank">📅 13:42 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436107">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t94LM1y5vX-5aDMBcl9ZL-0MC9f45_dCTt0X-MqWMohrKcMjFo4AoWQ7Olr15PLbPu4vbeDiVY7PIZBqd9eqjy5Z-hPrrbZH6OSYJG0TOdprY9AP8lQrc1aQm10zqny3hsaRbyarYS9CpY5Ft6X1qyWvy2ivoMlSLtZ4RZP5F_lR8OtIWEaOcXiZxGy_pS5F0uLVMIb240_VD0PoIOI_B9_-HPl955LT4W1Cr1hZFy2adnfWXsra8y4cq1uwntyimhfC80Naf1yHf8GnDQXcFFKzlD0-2M-IHHm4bTxFWqyHdTezHq2zxOU0DxighjjSCXtQ9XXQ-Gc60aKbOS_CcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علت گرانی روغن موتور مشخص شد
🔹
پیگیری‌ها نشان می‌دهد ۹ اردیبهشت جلسه‌ای برای ممنوعیت یک‌ماههٔ صادرات هیدروکربن‌های روغن موتور تشکیل شد؛ اما رونوشت آن ۱۳ اردیبهشت تنظیم، ۱۹ اردیبهشت ارسال و سرانجام ۲۶ اردیبهشت ابلاغ شد!
🔹
با این تأخیر از فرصت یک‌ماههٔ تنظیم بازار تنها یک هفته برای اجرا باقی ماند؛ آن هم در شرایطی که قیمت روغن موتور با گرانی ۱۵۰ درصدی، از ۹۰۰ هزار تومان به نزدیک ۳ میلیون تومان رسیده است!
🔹
این مصوبه در شرایطی تصویب شد که به گفتهٔ مردم، در ۳ ماه گذشته به‌علت افزایش قیمت روغن موتور، هزینهٔ تعویض روغن خودرو حتی بیش از ۲ برابر نیز افزایش داشته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/436107" target="_blank">📅 13:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436105">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCu0X9hDAXLt54tW9o4mZg5XhpZxFCXRPwqkIi9xIN0vtNEGA9eoNDzz1SVQnmQqcQSNyHHzoa9X-hcZEi-5nb2yCAV1LR-mprAAHZbEHbcEYEVDXqYYQbH2Jpy6oMHyyZLfnfZl952-VV68vMVuQsru7V6oBg55VmcIzZeAWUc5kw5UfeUErvVwrUsUItdj3KB-G8bZ-Bs4qCmkCVpfjIviHeinzOJ_mKHdcQLu7HWrTjGW60sUalIw2XlBEsbGrOO5KVnNq-SNin6PbJgJqDKL070esAO6r7dJladLRikY6Du6K-ODDiy0Sy9kKd-ETgLkvmrsTc92QNm6bA9E6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دومین جلسۀ مجازی مجلس یکشنبه برگزار می‌شود
🔹
سخنگوی هیئت‌رئیسهٔ مجلس: دومین جلسۀ مجازی صحن مجلس با حضور وزیر رفاه و با محوریت مشکلات معیشتی مردم و پیگیری اقدامات حمایتی از جمله کالابرگ، یکشنبه ۲۷ اردیبهشت ماه برگزار می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/436105" target="_blank">📅 13:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436104">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رئیس شورای‌شهر تهران: فعلاً طرحی برای تمدید رایگان‌بودن مترو بعداز ۲۷ اردیبهشت به شورا نیامده
🔹
هنوز طرح یا لایحه‌ای برای رایگان‌شدن حمل‌ونقل عمومی به شورای‌شهر پیشنهاد نشده و مطالب منتشرشده تا کنون اظهارنظر اعضای شوراست. @Farsna</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/436104" target="_blank">📅 13:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436103">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🎥
گزارش اکونومیست از پهپادهای مرگبار ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/436103" target="_blank">📅 13:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436096">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CsvBJtQStZU4bryUt_fUy7ZrqtmhNLpY63g69KTRLi4MGjIxw8AOeBZdy1gB4ZbxYQokRJuyl8xNJT5g5bQ75FcM7BWRLBCTtEXcOWTXh8njQhuDB5UQVj3f6U7uRAxmyTIWs6e-FpbITby72wIocJv3hg9PW3wVfGErXkaAnmNqDD4mFZOFjCctEeUfjwbaqN3Ih9CPEqu21XI3K3D9r7j0q_DWGiSgWWB-cgW-gqTNWvLhsRVOwkFPATYkRYAkTzWvJdevAfpI86oW1ueFh0ZCOGupclTFZ4zULIEBanF4ZJfmNtQcOQtMqOss96j2PVFW91mThkA25nGnuhFbtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hDh_BN9THyxl1X1XnMQAQSZWhsxFR31k5tDkRVQNHgvxUlbNSg80PS-xS1p8GiJf_i-Ogew_P-yfFLKhFP-_vbrs1x0WfClEr7zJgjnz7JPBgl3o-y3bjiseOlTHTsQClg4NhO355igkCa3xMQu8u6BF7H017klrCVpszSHAP-aKZ6_rjJXXU0GmU_i4u4jW50iT4u3kcFZ1gCFso-D4-RIpn1xHnjhoh9vCLx_-mAZVMJEKwHexmZf5WrSFP6q_fHkTumPFlP9odf2t1lsDP_dEgyqIAMHFHmbebRNMHGA_jngRaFUQMeu9ODQdlBCMzv6u3AC2tijtGjpjX16xzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYXB4P5aEe-Wdg2iZ8HaCqOoveu2KIfrL2cYZcwhjQGMx3O__3eTBvBiHcsDWLDs1TWwFK6porZ8k-6r7oO-0r7ppI2r5FXVgZpntdaACi8ma0bxkBDlbpxLllKxd6UhZjVLLI8rvYGaZq5f3CGJ6IW4AkKr-QX3tFK2ruZaQOwD6BlxBrXsowVZCKVkqD6ayUcrRGAzalTOvVLE8LNLyHTM7ncFskPfRYtPEMai7JVf3xn97PPfqwRV4yMV31Ltd19K4DcH9xRCq5OamgNiGfMEVAhE1OQn8H1x1hZompUOsCHWkRlXyK3dOBmvM30upxi32cPJgDIs8EcTMKP5yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AekNRDc78bwEQ44nYagM6QD7fjtq_3FXeN2tIEpL8zDY5LVsTq05_3-I4TZn-TM6x80xo90b4M3kbCZUD_2BazQxGLkZ60qqSbibeptU_Cbx6dGNoMD0WiNgiwsfmQYxUzWJPKNGsF6V-lzW6tBc9S8ZluQOVx_OUa0KWXiYYJrcdKHA7IKlMo5VpupwrJpfASeZpxQtcYHEJGXE5bUv_XlsFW7J4TMW1QlYL3e8TFLsm1_TSz1sNwXZAQrXSNALVfS85O1lseeLK_Tqp74gsDSby0GzGEeMQrjK_aifMGIPbNzeSBDNwKNepp4HWzat3YdSRfQy2zPCixZPAEB8oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJsYtIIzPUpLkBg5on00HzFOwYQJueZZJDa0Af7Riv5poVS1qKFwmGo1OmTCuEHIKt8dYTJjvMZ6oSutXdS9cDdzEDYgZkk1J8dG3ESR4MQp5yuxV_hF5HKpaUUEFW-mkAngM405iE2lVr8pH5P1JbNkrziXmAHyRIxQk6iOx1y_hx5yBe_oD_nRWX2YUeuLU6cRQOcDkdt8pJ-prVv4YdXwNBrhWpHK4eHlXT4YMf3N1zEMMgiEe1e1hchYBCAmuVNtdyk0zUGApJ6jOR3K9EXDJBl99lYjPjEM5q-vO8UTXBCxEAT8zpAgrDvYFcdnVO58axb_9rIAt1AISaKZHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OgKctKb5plSKCanVywPipKSj2tmTQuzVmaSh_hwwhx8PWGZ0oqS6M6H-e3-w_IvFx-J_2J8WhRvtVvSB9OrmYoKzk5OVJlUFiy5lgG3zevDWbkD-i2ZeiV3RVU1aCrKZMtxcGcPvcJldNILFvkKX0zVXW5kfdeMDNoyxs9Om_YCvSl-kLlSVTXj-eocuhj6YhuBILClIwNV1OiTPcVVTLV9Qx76ul6-YV1_nBGoXqj0FL1FlF3NjmTMXBMl7u1L3_6B8X-gKnJcN_-g2cAlzUvueGxyOlQ0iKvKIL6YKZjFtig3_hgMcoeFwSAqVqmv2gKaBrH_-jDBz8FKfkmqQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DKC1CxVlktUyv2p7mg6NbSHOYU8bxeDmI2SuJq0h3uTfrGig4p7UQ_HjoLMYjECdqmqNL42LIGQRygog2c704NVoJlyUgyoWi5OT1uzvHqD1YWxCO6KUCO4rMRCS5awo40jKTpnRzWYG-lR0n5WQWQ58K5XAYFo0EfoLNm_Hy005gzdudHieDWlsQDyNthFgjD7cJTCjfZChs_dOxyOTc3kDW9LrFrDQpCndz6pq_RySTDfQ5gaeKRB6W156HULEL5t_77zb0l6fZYdBtXcjepr255fCayecR-UZbJdKrje9NniIbIB3hwO5zaI5Cd_UA3k6oyp_uChFVUkRlpsnEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
طراوت بهاری در باغ گیاه‌شناسی ملی ایران
🔸
باغ گیاه‌شناسی ملی ایران این روزها به تابلویی زنده از رنگ و طراوت تبدیل شده است؛ جایی که گونه‌های گیاهی از اقلیم‌های مختلف جهان، از جنگل‌های هیرکانی تا پوشش سبز اروپا، در دل بهار و پس از بارش‌های مناسب امسال جلوه‌ای چشم‌نواز پیدا کرده‌اند.
عکس:
#زینب_حمزه_لویی
🔗
تصاویر بیشتر
@farsimages</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/436096" target="_blank">📅 12:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436095">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">جزئیاتی از درخواست‌های آمریکا از ایران در مذاکرات
🔹
براساس شنیده‌های فارس از پاسخ آمریکا به پیشنهادهای ایران، ۵ شرط اصلی واشنگتن به این شرح اعلام شده است:
🔹
عدم پرداخت هرگونه غرامت و خسارت از سوی آمریکا
🔹
خروج و تحویل ۴۰۰ کیلوگرم اورانیوم از ایران به آمریکا
🔹
فعال‌ماندن تنها یک مجموعه از تأسیسات هسته‌ای ایران
🔹
عدم پرداخت حتی ۲۵ درصد از دارایی‌های بلوکه‌شدهٔ ایران
🔹
منوط‌شدن توقف جنگ در همه ساحتها به انجام مذاکره
🔹
این گزارش تأکید می‌کند که حتی در صورت تحقق این شرایط از سوی ایران، تهدید تجاوز آمریکا و رژیم صهیونیستی همچنان پابرجا خواهد بود.
🔹
کارشناسان معتقدند طرح پیشنهادی آمریکا به‌جای حل مشکل، درپی دستیابی به اهدافی است که این کشور نتوانسته در طول جنگ آن را محقق کند.
🔹
در مقابل، ایران انجام هرگونه مذاکره را منوط به تحقق ۵ پیش‌شرط اعتمادساز دانسته است که عبارت‌اند از:
🔹
پایان جنگ در همهٔ جبهه‌ها به‌ویژه لبنان
🔹
رفع تحریم‌های ضدایرانی
🔹
آزادسازی پول‌های بلوکه‌شده ایران
🔹
جبران خسارات ناشی از جنگ
🔹
پذیرش حق حاکمیت ایران بر تنگه هرمز
@Farsna</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/436095" target="_blank">📅 12:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436091">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/csxMVxfPcih-4S9noobmBv7W9lFYcVIZTNmetbFeHU89XT-tQdSfJ6UWUb80acHTMoGWnnxP7wLcBnRu0mo_D9Rt9NyySkO4syun6fRX5esA9LDMl_wjxyfDA4Er5BoMk4GiUkTMuHH89vcCSZo3Zaw27YqbHCPyWRfxaho1QWXMVWrprLdUxXza-Dmf174fPvYWOZepHXpKSUC1cKUzKRHueu9mueMOEjv1iekWtiK9JkPMCR0TUiPWTgsGGPCLGj1a5WZiYKCU7RwR80i3qcez-5-aT8J9U3q3QXHsKqlL0-6dfeEbx4AFceA7iaQ6hIZe6s5ZQQE8LRijybh0lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t6-yo_Ym81IekZ77ESqXOMvau0XwoJIX8yq0r4d8NDWbP2IKjzt1JOooDS3_aE7CxLBipXr8p1t2ob_bv9jY6fLVD4-s-ljsrZXJ7jHvR8srWsvhp6Xh4HXIS0ApthSTgxmGbJDnA6U9hgyjC73otI2rhTc-NqEAJ-ROOkTX8PfxR7kRimaiQDSoGnZT3D7n1XrPy0Jl8lDkczqIdO4DPGzx7LhSobBGIUOeh8WHeJzBb4IUAbJrYDRKX702Jb-AEKrVXHUBrH3dqvMPbHnrXvhk_XDiIie2CfjaxEywh8Jog8GqtdV0HPURxaxg5UL5WqQ3SG06gseAB9s4ofZJ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dd20K91-NhMJR3j-jh8QbYpZSZERR64kQqQVN5ypwyNlT-U3fH8Lw1PceEJlU9j_oZr2KhIhK1ThVf_uJnJpyYbhJizLHmRfvQPBVjypF7Pz8ttS5xLMpYM8u94PpZIFZ4t0KKZMnmqyjFTSTau2OqkC4RN3v7ljzTnWa6mBiDBtveC8i5dneip5hdXX09DUQSg6um6whcTBPM0CDzfytKvCFeHK6kGzKvPtrPYnKL2-8RUpl-cBuK8zpMcBlb_iWB4ZNPMcJM8zyYmagtdnY_KHjn8WhPwHRMTiSSAlfy8mOEQ-cbvCE3r_svUYxTt6g0JeXD1emWgmqzGVwQeWYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bngWUbRpYZA-NcMvnDW9K15l2uOrBerEI_nkzIKsf2FgmnDo7mpZF9rI05o0Z6PpCDbx7rMeoXjGoW2lBo-q5j94X4qHU5NdgIjwTiM9CCuN7Qv3-jO-RJ7YJAASUi1yMvRLiAsQS_5AG_diMmVN-ZRutzYa1bz1bdvJ5h7VRcS2TX8JbcMz11AenPz06DP4Ah2Ve_po2LaOhVb2MfGi4KZt5-IXyN8MvHe61OwXHygbUel0s4c3SEuuF2AzaZ5MR7oP4isu950FKFIafXPQRwETMx1iOO-h-3owXt-W0uWgQ6QD0j6rm0OCPnTqyw_xSPVbJJikBvI8Lna3tjIQnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: تغییر رفتار مصرفی جامعه، نیاز فوری در شرایط کنونی است
🔹
رئیس‌جمهور در بازدید میدانی از اجرای طرح «حکمرانی محله‌محور و مسجد‌محور»: تغییر الگوی رفتاری جامعه در حوزه مصرف را از ضروری‌ترین الزامات شرایط کنونی کشور است.
🔹
مساجد به‌واسطۀ برخورداری از سرمایۀ اجتماعی، اعتماد عمومی و نقش تاریخی خود در ساماندهی امور اجتماعی، می‌توانند محور اصلی ترویج فرهنگ صرفه‌جویی، مسئولیت‌پذیری اجتماعی و اصلاح سبک زندگی در کشور باشند.
🔹
اگر خواهان ایرانی مقتدر، باعزت و برخوردار از توان ایستادگی در برابر فشارهای خارجی هستیم، مسیر تحقق آن از مدیریت صحیح منابع، صرفه‌جویی، ارتقای بهره‌وری و مشارکت مسئولانه مردم در مصرف می‌گذرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/436091" target="_blank">📅 12:15 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436086">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPv_Vi3aNkXCqxjqVx6cA1dOsaMx9azZH1bS-ZPolCpy6lECykxaxD-apsAdVD5RXx_FeoQj2d8G2c_SDO29NqtYWp7J3dgtYxo8s30Ml-qnUX7iL9tzJQjnKFrG2EEivqInYZd07F4lBZPxxeUJfyaBdxeFxj8Dne9KChtK0ATAmZMcM4mISC75Y5cKCsZiEAMgtCgg-H_16F7Piv3GlUSKC6tIi1Zx--p2J3MrFVEJonx2rlc6deN_l8UQZPKcRhndnPCJVOTGeAGHLTz0PlsYrOQKiPoplOauZ6-1nDtlnt9v1HZCxibmue-E5EFABmF9z_I7E6unGu-er_NcFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سردار شکارچی: تکرار هرگونه حماقت آمریکا پیامدی کوبنده‌تر خواهد داشت
🔹
سخنگوی ارشد نیروهای مسلح در پاسخ به سوال خبرنگاران مبنی بر تهدیدهای مکرر و یاوه‌گویی‌های رئیس‌جمهور متوهم آمریکا علیه ایران اظهار داشت: تکرار هرگونه حماقت برای جبران بی‌آبرویی آمریکا در جنگ تحمیلی سوم علیه ایران، پیامدی جز دریافت ضربات کوبنده‌تر و شدیدتر برای آن کشور به‌دنبال نخواهد داشت.
🔹
رئیس‌جمهور مستأصل آمریکا باید بداند در صورت عملی شدن تهدیدها و تجاوز مجدد به ایران اسلامی، دارایی‌ها و ارتش مضمحل آن کشور با سناریوهای جدید، هجومی، غافلگیرکننده و طوفانی روبه‌رو خواهند شد و در باتلاق خودساخته‌ای که نتیجه سیاست‌های ماجراجویانه همان رئیس‌جمهور است، فرو خواهند رفت.
@Farsna</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/farsna/436086" target="_blank">📅 12:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436085">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jwb-TK7ZMUZq-AVzafO72TnMAwAKyipSQM9MPB2gwdtL0-Y9A32IZYtkJd9jijw5hOAt0xWFFbqUOojrrazUoY7C4zBXbCJXnfy0p7Fp2SVY4zGIZBcEnWdkpB61kqwE4TYPfy44HqjpNkWS70HlbmtqtTFBo2jmeTx6bel8J0T1dQePXRMjDYNKrFBeV6tmFS7E31i7RRwWRPWdZDnb2lmRPJED_OJ2ey8sv2xD3NnvaGBEECV6DtiVS6KyU5FdjwffyE6XKkNuZlT6yZjwz-7FKPrRVPKueX2K9JytyViPSjmSMw41VIgVz8fsNAC4n5TxicYYMwTUPITHbmeudQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
دادگاه رسیدگی به اتهامات صادق ساعدی‌نیا برگزار شد
🔹
جلسه رسیدگی به اتهامات صادق ساعدی‌نیا مدیرعامل شرکت صنعت غذایی و کافه‌های زنجیره‌ای «ساعدی‌نیا» از متهمان کودتای آمریکایی-صهیونیستی دی‌ماه ۱۴۰۴ در دادگاه انقلاب قم با حضور رئیس و مستشاران دادگاه، نماینده…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/436085" target="_blank">📅 12:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436084">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a6fce360f.mp4?token=eYRorlwGBHEWavWIzmtKpt5KwXY4dKzDazlyrn2CFt1LgqIs-DExYzPNXKcqBx8GHxv6ViQ_KucKjeCDlVBF4VnT3cXnlocGkJtfVTsculAR-8E458JomGVjqmYl5nH8S_Q0KV1D0SrTIqAW5MJZKc8cEnP7M9DCMghM3xpHcCXqf6_CDvmNky-68hxICblxz01qS8nzk9qGfE9JvX5Q4Uvqp3nX063pdZ7uPklLNvkPL8Zf4ikC46wE9hm6IfzpnSDCLEzaq8gTq2PRLuKILhqM3om11vkxzfMaeaQeQr8vMyNUoH0tj9IcVSLXYaBGf7bG-riOdF4MMpjizpmjMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a6fce360f.mp4?token=eYRorlwGBHEWavWIzmtKpt5KwXY4dKzDazlyrn2CFt1LgqIs-DExYzPNXKcqBx8GHxv6ViQ_KucKjeCDlVBF4VnT3cXnlocGkJtfVTsculAR-8E458JomGVjqmYl5nH8S_Q0KV1D0SrTIqAW5MJZKc8cEnP7M9DCMghM3xpHcCXqf6_CDvmNky-68hxICblxz01qS8nzk9qGfE9JvX5Q4Uvqp3nX063pdZ7uPklLNvkPL8Zf4ikC46wE9hm6IfzpnSDCLEzaq8gTq2PRLuKILhqM3om11vkxzfMaeaQeQr8vMyNUoH0tj9IcVSLXYaBGf7bG-riOdF4MMpjizpmjMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعدی‌نیا: خودم و پسرم اشتباه کردیم؛ از مردم می‌خواهم ما را ببخشند!
🔹
محمدعلی ساعدی‎نیا، مالک برند «ساعدی‌نیا» در نامه‌ای که با امضای او به فارس ارسال شده، ضمن اشتباه خواندن اقدام به بستن مغازه‌هایش در  ناآرامی‌های دی ۱۴۰۴ از مردم بابت این اقدام عذرخواهی کرد.…</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/436084" target="_blank">📅 11:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436083">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b54d485d5.mp4?token=PhrRUjBGw3ztusdoU-UmQdUPymwptnoUSmbBrSMCdBsewPkU_kT2yYMQjPRIMYTFDQfbL4Y4CcTYm08w5qiBqZ8MfZwifwJr0x-uDo1Y7VgRT5D3mq7dUFu-oWsDx3UDdllQGq7rx3pAy2iJMDNrLTtz2xUm0nhNjWjKEBbPDagp6S1bzHpDP38LEqRpLeJ7ELNC9YsqK3VS_10ezi06LvhgwTLD8ozeNpboNXpm2GCIBkbTh8ZpLFaAgtbrga0NPHHOPi2w2g4TTQBgOxyBHKnYGJBydLB6dWM3uehfXgJ03gFVff4MlyijfKN-ClbEewnIESCkx31NSGmXqNnbSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b54d485d5.mp4?token=PhrRUjBGw3ztusdoU-UmQdUPymwptnoUSmbBrSMCdBsewPkU_kT2yYMQjPRIMYTFDQfbL4Y4CcTYm08w5qiBqZ8MfZwifwJr0x-uDo1Y7VgRT5D3mq7dUFu-oWsDx3UDdllQGq7rx3pAy2iJMDNrLTtz2xUm0nhNjWjKEBbPDagp6S1bzHpDP38LEqRpLeJ7ELNC9YsqK3VS_10ezi06LvhgwTLD8ozeNpboNXpm2GCIBkbTh8ZpLFaAgtbrga0NPHHOPi2w2g4TTQBgOxyBHKnYGJBydLB6dWM3uehfXgJ03gFVff4MlyijfKN-ClbEewnIESCkx31NSGmXqNnbSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زارع‌پور: شهید رئیسی شورای‌عالی فضایی را پس از ۱۱ سال احیا کرد
🔹
وزیر ارتباطات دولت سیزدهم: شهید رئیسی دولت را در شرایطی تحویل گرفت که عده‌ای اجازۀ پرتاب ماهواره را به این بهانه که مذاکرات را به هم می‌زند، نمی‌دادند.
🔹
شهید رئیسی اولین رئیس‌جمهوری بود که از صنعت‌های فضایی بازدید کرد و در دو سال فعالیت دولت سیزدهم، ۱۲ پرتاب فضایی انجام شد.
🔹
در دوره شهید رئیسی، پس از ۱۱ سال اولین جلسه شورای عالی فضایی کشور برگزار شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/436083" target="_blank">📅 11:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436082">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spPklL3d6I99WdY1pjp06JFtGT0IXL5TuIAqaq0uTFOBza8xMcJ6D1ZnNZWO2N42RYgmXG31qNb9ZmCHu8wJSHBTbo48ujYM8zlk4SBePZsMxoVCur8gRcKFSQcQi4BN9uFxgqekDrTyc7eKggP5af_ZdsOsGwHSubCGbX_c-SygxCd7HpnABLvOszPdl1JD5GCF4Do4qGpR1xNcLXIKTYnG8kIiY2vbbRDzvDd82IiY5ozR8tL9ieUrauRULBu9IBTMWTCoprdDQeoU5EaTnrjfA_yMmJpLNSvyH2A5hKtsBgsiy7ep5dJDKZQXm-Wv2pywph_kYdUW1___3VNZag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابلاغ سلام رهبر انقلاب به خانوادۀ سپهبد شهید موسوی
🔹
سردار سرلشکر پاسدار خلبان علی عبداللهی فرمانده قرارگاه مرکزی حضرت خاتم الانبیا (ص)، با حضور در منزل خانواده معظم سپهبد شهید سید عبدالرحیم موسوی ( رئیس ستاد کل نیروهای مسلح) در فضایی آکنده از معنویت ، با اعضای خانواده ایشان دیدار و گفت‌وگو کرد.
🔹
سرلشکر عبداللهی در این دیدار، با ابلاغ سلام رهبر عظیم‌الشأن انقلاب اسلامی و فرماندهی کل قوا (مد ظله العالی)، به خانواده مکرم سپهبد شهید موسوی و تجلیل از سال‌ها مجاهدت، مسئولیت‌پذیری، نظم، درایت و منش مردمی و فرماندهی تراز مطلوبیت‌های دینی و انقلابی آن امیر مومن، مخلص و مجاهد گفت: ویژگی‌های برجسته اخلاقی ، مدیریتی و فرماندهی شهید موسوی از جمله روحیه خستگی‌ناپذیر، نگاه راهبردی، انضباط سازمانی، پای بندی به مسئولیت و اهتمام به کرامت نیروهای انسانی همواره مورد توجه آحاد نیروهای مسلح به ویژه ارتشیان غیور و دلاور جمهوری اسلامی ایران قرار داشت.
🔹
وی سپهبد شهید موسوی را از چهره‌های اثرگذار، متین و پرصلابت عرصه خدمت به کیان کشور و مردم ایران به ویژه در دوران تصدی ریاست ستاد کل نیروهای مسلح دانست و تصریح کرد : شهید موسوی با برخورداری از شخصیتی منظم، مردمی و تربیت‌یافته در مکتب اسلام و امامین انقلاب، در مسئولیت‌های مختلف، منشأ خدمات ماندگار و راهگشا بود و نام او در حافظه خدمت‌گزاران این سرزمین با احترام و عزت باقی خواهد ماند.
🔹
وی همچنین با تاکید بر عزم و اراده نیروهای مسلح و فرماندهان و رزمندگان مدافع وطن برای ادامه راه شهید موسوی و دیگر شهدای اقتدار ایران اسلامی، افزود: تکریم خانواده‌های شخصیت‌های خدمتگزار و فداکار وطن، به ویژه فرماندهان و رزمندگان شجاع و حماسه ساز نیروهای مسلح ادای دین به سرمایه‌های معنوی کشور است و یاد و نام کسانی که عمر خود را در راه مسئولیت ، شرافت و عزت و اقتدار ایران مقتدر سپری کردند، همواره مورد تکریم تعظیم و احترام نه تنها ملت ایران بلکه آحاد امت اسلامی و و مجاهدان راه حق و حقیقت خواهد بود.
🔹
در پایان این دیدار، خانواده مکرم سپهبد شهید سید عبدالرحیم موسوی نیز با قدردانی از ابراز محبت فرمانده معظم کل قوا و حضور سرلشکر عبداللهی و همراهان ، با برشماری ویژگی‌های اخلاقی، تعهد حرفه‌ای، روحیه مردمی و اهتمام ایشان به انضباط، وظیفه‌شناسی و خدمت صادقانه به کشور و ذکر خاطراتی از آن شهید ارجمند، وی را سرباز مخلص و فدایی ولایت و ایران عزیز توصیف کردند.
@Farsna</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/436082" target="_blank">📅 11:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436081">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jz_Hu5kT9uaTU3K2pLoOt0sGGm1OiE3gjXkqeAexLt5onwB31RZA3C4KCqs_tiqBnLI5qv_8SxsGZxbFA1Qy0o2sS6_j-fT0PxHfPi2VAM-uEoOiMj_CTo8FFSxRP61w3UNlbCImPObNOgvxCdAJ3HlRo4M8tq2z4qggVTpxUlyiSzXZsRMEgcJjUM3vNEGI4T0tjjRPRU-zTJmaN3NeVeqtFNllVbB_RExqrKfsVxayG6V05eJjMMrNlSyRNP0-FoJ9-rgm9oNt7xikv7j2yHUAVkRgsWWL8mIrm9SGF-astS9RV-Z64KRBTNPzyI1XHjg4RqFioTXAJ-Yy95eowA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف نمایندۀ ویژۀ ایران در امور چین شد
🔸
پیش‌تر شهید علی لاریجانی و عبدالرضا رحمانی‌فضلی چنین مسئولیتی را برعهده داشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/436081" target="_blank">📅 11:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436080">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">قیمت تخم‌مرغ اصلاح می‌شود
🔹
وزارت کشاورزی اعلام کرد که با استناد به قانون اصلاح خرید تضمینی محصولات اساسی، دستورالعمل خرید تضمینی تخم‌مرغ را اصلاح می‌کند.
🔹
با توجه به نوسانات اخیر قیمت این محصول و نیاز به ایجاد ثبات در بازار، وزارت کشاورزی بر آن شده است تا…</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/436080" target="_blank">📅 11:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436079">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJL9rYejc4-tvpU6BTk_qQjdGZh_LYh1XYAmeIiPL77991jyAC_Fy1ixq6gK2nElrrtFi65uKL6WV7dreS5hsWmXnlTSM1ib-ieRa2zVDPoASqycKoJcE5C4drUK4Acezwg8MmZNGqfNA2xuOeaYOflR_z6-1v2VjNp5JqtqLqvIQpUQA2Uo0c1IqYk9ajRdjkW-TKDqKyrMZxxZCnSUHMRd-OhAzMbPnL_LAr36YgKVsE8dnTzSfbo-U7cgFVjObzoXlZ28RV_o79eLaM0BOsPbSMajcbI1hP3pQIiPNxZHii_c82lDXRMvdmhyJthSq5rj0ueOEK0f3InA5qJ8gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقیف اموال مهدی نصیری و ۲۱ عنصر وابسته به دشمن در سمنان
🔹
با دستور قضایی اموال ۲۲ نفر از خائنین به وطن و مردم که از عناصر وابسته به رژیم صهیونسیتی و کشورهای متخاصم هستند، در راستای حفظ حقوق عامه و اجرای قانون تشدید مجازات جاسوسی و همکاری با رژیم صهیونسیتی…</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/436079" target="_blank">📅 10:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436078">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
امیر سرتیپ سلیمی: شهید موسوی بر قلب‌ها حکومت می‌کرد
🔹
همرزم شهید سپهبد موسوی: اسلوب فرماندهی امیر موسوی این‌چنین بود که صلابت و قاطعیت را با فروتنی و تواضع در هم آمیخت و از همین طریق در قلب نیروها حکومت کرد.
🔹
اگرچه جسم و کالبد امیر موسوی در میان ما نیست، مرام او، مکتب او و منش او همواره در میان پرسنل ارتش زنده و پابرجا خواهد بود.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/436078" target="_blank">📅 10:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436077">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DijvTa2YFw8KNvEu4SGpC62he2CaKX7tApGUl8oqPxncpZyZ0qAoNbrTWiIvB3F5JtRBX28fHH47VTiXtvw1b7fE_Qm4MQAY_VuRJA9bUcviClIeHuEJg1_V0m9-oEdMzNzmVGOxxSD4obBdRv4qfjQkrIJdIWNwQqWN8_3s2q0StcvRDhpNHrZmF0NjGj-OSDKA-IuV12AevIXJGn9KeAxCxord4_qhUuP8bYksJfpXaSTijcwfUmXh9MFQuYE4yc9Vza2rEXNorijeib9ydkfOjBUZOjxvDZQRaRR0-7Yzxn9gKLpDBpJUyknu2MPYaPWWphr0sEUni4BbMmB2iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولیانوف: حمله دوباره به ایران یعنی آمریکا و اسرائیل درس نگرفته‌اند
🔹
نماینده روسیه در سازمان‌های بین‌المللی مستقر در وین میخائیل اولیانوف در پیامی در ایکس گفت که «کارشناسان غربی معتقدند که آمریکا و اسرائیل ممکن است حملات نظامی علیه ایران را در روزهای آینده، اگر نگوییم ساعات آینده، از سر بگیرند. اگر این درست باشد، به این معنی است که آمریکا و اسرائیل از اشتباهات استراتژیک گذشته خود درس نمی‌گیرند».
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/436077" target="_blank">📅 10:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436076">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دستگیریِ کارچاق‌کن مدعی نفوذ در دستگاه قضا
🔹
رئیس دادگستری مازندران: یک کلاهبردار و کارچاق‌کن حرفه‌ای متواری که با جعل اوراق قضایی و ادعای نفوذ در دستگاه قضایی فعالیت می‌کرد، با رصد اطلاعاتی دقیق دستگیر شد.
🔹
این فرد سال ۱۳۹۹ در یک فقره پروندۀ قتل با وعدۀ نفوذ در دستگاه قضایی تهران و مازندران برای برائت قاتل حدود یک میلیارد و ۶۰۰ میلیون تومان وجه‌نقد و ۷۱۲ قطعه سکه تمام بهار آزادی دریافت کرده بود.
🔹
از منزل متهم تعداد زیادی اوراق قضایی و دو دستگاه خودروی لوکس کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/farsna/436076" target="_blank">📅 09:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436075">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDI-E-ch1CaCv3-NpcCW99Z7sckb0QPilsd0b835RNJpf7kAGvVOXo3Rxu0No6ibYahgwiEewXy9TBGihQTqyyWiiCWrs5NRSnSLdsbq1w-vBx5vGA0jKX9s74TIHNBNVF8cCf5FaN_sjmPhIBHRNEXNjJ_OWJfsiyE8PPJ_V_E7i0nfQKeLAkolCC8nL25Wx5Wn7ohf6pjNj__Ij5zp9G9qC3VhkhwP7E9ACI-QMewKmjDqW4qCnMKxilwDG5xVuilkQ3my0us0kFNTYemXFAN0crZ0AIrg-DDDuBlbnkO8psRPhynsY1OWSSUcy-CBfCIqLroLkGayxigQOEapmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
هشدار تاج به آمریکا و فیفا جهانی شد
🔹
رئیس فدراسیون فوتبال کشورمان به‌تازگی برای فیفا خط‌ونشان کشید تا امروز نشریۀ اوجوگو با تیتر «شرط ایران برای حضور در جام جهانی» به این موضوع پرداخت.
🔹
طبق قانون فیفا هیچ دولت میزبان و هواداران دیگر کشورها حق اهانت به…</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/436075" target="_blank">📅 09:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-436074">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آغاز صدور ویزای عمره از امروز
🔹
عربستان با تأخیر یک ماهه صدور ویزای عمره را از امروز آغاز می‌کند. وزارت حج عربستان اعلام کرده که «پذیرش زائران عمره از ۲ هفته بعد از آن آغاز خواهد شد.»
🔹
امسال زائران خارجی ۲ روز پس از پایان مناسک حج می‌توانند به عمره مشرف شوند. البته سازمان حج و زیارت کشورمان هنوز مجوزی برای اعزام زائران صادر نکرده و وضعیت بیش از ۵ میلیون دارندۀ فیش عمره در هاله‌ای از ابهام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/436074" target="_blank">📅 09:24 · 27 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
