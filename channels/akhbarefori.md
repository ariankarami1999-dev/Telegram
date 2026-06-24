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
<img src="https://cdn4.telesco.pe/file/tSP6EFCatCb_T-cGtttEHt-aqJYScKiSYgTsXPhkrJKdzSJ55zxbuUvRX4jf1PdTKonG6SjJtcNgBVL7dnppdT-2qAarvLOoniM_-zc4oFzU8NS8KbANE7p9IKfZaof7E6JWEOat19BMEhQE8eowe-PtU4I4nAV7REtEgNfZAm2DqRmVLl3m4w7zF05d3M0R9Kgl-Z2dUZAKSF6AmhuZTo1_nzVpNewgcr_lxVVviovSwhJZDvfBbsJLS5qJm75JfsHFa4gxZXx598g3JDJCW27xNe3kzTK-zGnDxOhi35DMuRWkDATVcR5xUGT9EZ07M3oAy-nXpKoEOtFPEO3PqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 20:55:17</div>
<hr>

<div class="tg-post" id="msg-662988">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔹
پایان دور اول مذاکرات اسرائیل و لبنان در واشنگتن بدون نتیجه
🔹
نخستین روز از مذاکرات مستقیم میان نمایندگان اسرائیل و لبنان که با میانجی‌گری آمریکا در واشنگتن برگزار شد، بدون هیچ پیشرفتی به پایان رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/662988" target="_blank">📅 20:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662982">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bda6a59f3.mp4?token=aWqfzmN6O6b9a7VGRDTJMfDEpfTMEhi6HyID-s0SIctA4hUtl6hU57FZaPGoWrWNkIFBHmQBhPcnoqXdeA1sM5L9N0gxpD4BA_hJVNM5vZq4l2rdLlyAJ7Wz-OLsv-NE3O-xjveYBZ3sjl3tLRv3Q7bf9iL39K46igI5AzMFfC9u38vYgTEGUN0tKr-yS_m2XQ6TJLjMkaY-AIuxe9hLCVIiqn5D_qLe7F-SNDRdisGP7XRh_9sWqLYeWVPY91gtA0ZZi51e-TJkLWUw-UXCtSaD1XtXOyHY3jbHoGEB5H28XaU-fu1zVFWew6ESRp7od1br0t1h10TApgIiIzjVLUa1SLtNYltCxP7u8p9VsCEPenqYYFT0xuFcLJmWi-p53ebtc4krXVpm0uGYregSko9Dun5FwFq8sk1dGCHXPN3qnupLIxoEkkdwNh8FKycnU5QO4oLVsGRV045q5zUVh0fkDIE4RPQKyon7inFjYDoRMSB4OrK68uHry4dmG7QaiKb0pMa9ElwqAiHEJs1R7zPTCoxkag-AzTQRTucSEc3UWzeEGoYrTkoTWL3Rlwl8dji5YbfLyCxd-bK8SP4cii1mc-OH4812g7jQDogQYerWZTFJqkaKAnSiVNM8kfC7v1BHq2kPH_S46BGWFxmn27CNFep7f1RQTunrn6IPUHs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bda6a59f3.mp4?token=aWqfzmN6O6b9a7VGRDTJMfDEpfTMEhi6HyID-s0SIctA4hUtl6hU57FZaPGoWrWNkIFBHmQBhPcnoqXdeA1sM5L9N0gxpD4BA_hJVNM5vZq4l2rdLlyAJ7Wz-OLsv-NE3O-xjveYBZ3sjl3tLRv3Q7bf9iL39K46igI5AzMFfC9u38vYgTEGUN0tKr-yS_m2XQ6TJLjMkaY-AIuxe9hLCVIiqn5D_qLe7F-SNDRdisGP7XRh_9sWqLYeWVPY91gtA0ZZi51e-TJkLWUw-UXCtSaD1XtXOyHY3jbHoGEB5H28XaU-fu1zVFWew6ESRp7od1br0t1h10TApgIiIzjVLUa1SLtNYltCxP7u8p9VsCEPenqYYFT0xuFcLJmWi-p53ebtc4krXVpm0uGYregSko9Dun5FwFq8sk1dGCHXPN3qnupLIxoEkkdwNh8FKycnU5QO4oLVsGRV045q5zUVh0fkDIE4RPQKyon7inFjYDoRMSB4OrK68uHry4dmG7QaiKb0pMa9ElwqAiHEJs1R7zPTCoxkag-AzTQRTucSEc3UWzeEGoYrTkoTWL3Rlwl8dji5YbfLyCxd-bK8SP4cii1mc-OH4812g7jQDogQYerWZTFJqkaKAnSiVNM8kfC7v1BHq2kPH_S46BGWFxmn27CNFep7f1RQTunrn6IPUHs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
پک
#استوری
کلیپ های عاشورای حسینی و شهادت امام حسین (ع)
🥀
امشبی را شه دین در حرمش مهمان است
مکن ای صبح طلوع مکن ای صبح طلوع
محتوای مذهبی ویژه محرم در این کانال
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/akhbarefori/662982" target="_blank">📅 20:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662981">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxB9i4TZemqOKpJE9KnfA7lgdOD7y4GpAiYaI453k0pBViDnOZk-Pzv2g78-kl217JAifg6MVA5yBJ66LlDKwzY8-JS5XweAOzjmUKy_MXBZyrvsmpeDHEs8cM99wKNcWZfsDaN_6uUWLLtT_9wwWZMOBO2kef_yVC3dQr6QvsISsf8HvZswbqnOIiLiENu9XFd6o2CWsLelNvT0oWI7flE81hWZYTK1jlwJO4lhM3D8USMAGB1sj3GhiX47N0gHQpBpznItfMjaBpuVfnVxCXOy_8KZykFfOEIWKSFXFktFonjIfKyNrWSuxY1X2CgVSYbOG3ZvYCuDKlqsOAhQWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
غرب به دنبال جنگ با همه است، و با کسی جز اسرائیل کنار نمی‌آید
آلوهن میزراهی:
🔹
روسیه به دنبال جنگ با غرب نیست.
🔹
چین به دنبال جنگ با غرب نیست.
🔹
اسلام به دنبال جنگ با غرب نیست.
🔹
عرب‌ها به دنبال جنگ با غرب نیستند.
🔹
آفریقا به دنبال جنگ با غرب نیست.
آمریکای لاتین‌زبان به دنبال جنگ با غرب نیست و همه آن‌ها با یکدیگر به طور معقولی کنار می‌آیند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/662981" target="_blank">📅 20:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662980">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa00589e23.mp4?token=VfkJSLK8XG4FcvKgp3F5N9ykQ9siFCZt_ZUk-hf3wexCmU8_hLanEiVpv8mx6es0H1kEtTR-KIAaIsFgnEyJ3zYkKEZZpEjbxqm2F1-o4iIWYTEOTZfICme-7VqmeUlLNDML_xzYS-lxa_V0WUfJmpqklJrItHdcMaj4hloO_c-Yp7n51Itw22Qy160CKOAKeI7AJvuT4w-47eYcDcE3sE-JLPji_5OEW9qstoRjKKyRcYHkBBhNdGVHvvG2OFb1Q3KrrWe_adrWIlUATB0lokBRlURU9rDpFFIYO3KmpoT_k3A5dWGehF8CE51T87zCQ2nUizKRCJs3dMxFm5wTl64gYobQ4JM-yiyppBYdDYMsvIZ2n5dV6huG1QeYlf3JyskLSschT8P-hRYGreBqB8wAQxY-LfN7iXMj9-E82NTWeTfYebtaPRU7nPeSA0X3Wk88DeO2dfCoTe8ZFLLGHVxTKCJVKqCsym3Vv9Rye1XdooQnk8_0--D3KkH5q28dKV43tPIbTNpOHKQXyUHzwAGsfrhFmDbxNJLkajSE7zb1P-o32Fn3cxml7gfKwEfl-q7OeNp6dtZfEfXk_lRS3BhlYsBYwOx8h7wa3FyCR0wqQ7vh_WEyJHL5P5G_2USMMXzpXf1lxp9u-AylWT6yctIIQid5zrgQVb1o0WKmgUk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa00589e23.mp4?token=VfkJSLK8XG4FcvKgp3F5N9ykQ9siFCZt_ZUk-hf3wexCmU8_hLanEiVpv8mx6es0H1kEtTR-KIAaIsFgnEyJ3zYkKEZZpEjbxqm2F1-o4iIWYTEOTZfICme-7VqmeUlLNDML_xzYS-lxa_V0WUfJmpqklJrItHdcMaj4hloO_c-Yp7n51Itw22Qy160CKOAKeI7AJvuT4w-47eYcDcE3sE-JLPji_5OEW9qstoRjKKyRcYHkBBhNdGVHvvG2OFb1Q3KrrWe_adrWIlUATB0lokBRlURU9rDpFFIYO3KmpoT_k3A5dWGehF8CE51T87zCQ2nUizKRCJs3dMxFm5wTl64gYobQ4JM-yiyppBYdDYMsvIZ2n5dV6huG1QeYlf3JyskLSschT8P-hRYGreBqB8wAQxY-LfN7iXMj9-E82NTWeTfYebtaPRU7nPeSA0X3Wk88DeO2dfCoTe8ZFLLGHVxTKCJVKqCsym3Vv9Rye1XdooQnk8_0--D3KkH5q28dKV43tPIbTNpOHKQXyUHzwAGsfrhFmDbxNJLkajSE7zb1P-o32Fn3cxml7gfKwEfl-q7OeNp6dtZfEfXk_lRS3BhlYsBYwOx8h7wa3FyCR0wqQ7vh_WEyJHL5P5G_2USMMXzpXf1lxp9u-AylWT6yctIIQid5zrgQVb1o0WKmgUk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
شگفتی رسانه‌ های دنیا از قدرت تسلیحاتی و فناوری نظامی ایران
شبکه قطری العربی:
🔹
ایران با استقاده از برترین تکنولوژی و فناوری، جنگنده F-15 آمریکایی را ساقط کرده؛ این شبیه فیلم‌ های علمی‌، تخیلی و موجودات فضایی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/662980" target="_blank">📅 20:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662979">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
رازهای برزخ از زبان یک بازگشته از مرگ؛ دیدار با اهل‌بیت و سرنوشت برخی مدعیان ایمان
🔹
00:08:40 ماجرای خمس و زکاتی که پدرم به نیت امام زمان(عج) پرداخت می‌کرد
🔹
00:17:00 اهمیت نماز اول وقت و اعمال نیک
🔹
00:23:10 زیارت حرم امام رضا و کربلا توسط روح در کسری از ثانیه
🔹
00:34:35 درخواست انسان‌های حیوان‌نما از امام زمان(عج)
🔹
00:40:20 وضعیت شیعیان گناهکار در عالم برزخ
🔹
00:59:30 نذری دادن به نیت ظهور
🔹
01:03:00 اعمالی که با نیت خدایی انجام می‌شود
🔹
01:20:10 ترسناک‌ترین لحظه در زندگی
🔹
قسمت بیستم (نذر)، فصل چهارم
🔹
#تجربه‌گر
: محمدحسن حکیمیان
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/662979" target="_blank">📅 20:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662978">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e95ef43275.mp4?token=Li4rNVl8xzz6z_ubfEM6-lz3qfkWoMzz6zHw9rY9Qezg2PVXMcuMwR4DWuh27_yPo_eCxycpsv5Bbe2p7hZjbnB4J-OU0S081PiPcVistV-XJPTvekuEPy0J0PllAWRQoQfF17wRX06Uux887AxlBlfh1HDL1UtOENOER0-oxCx47DYmgseFfgY0-2wQiC7MUn9smB3Pv7r4RnmdsuhOlsuP0ykM1YygIK6z4rFuB1pY7uZMaSgWYHLKJ7LH-rt02BikAz20Igu-xc98s1IsBr8X8eC2XdjXw8Tz_h56_v8XeDgeR5gZYK7OTNnolmdraJzi2HfC60z-wAAvEvQA_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e95ef43275.mp4?token=Li4rNVl8xzz6z_ubfEM6-lz3qfkWoMzz6zHw9rY9Qezg2PVXMcuMwR4DWuh27_yPo_eCxycpsv5Bbe2p7hZjbnB4J-OU0S081PiPcVistV-XJPTvekuEPy0J0PllAWRQoQfF17wRX06Uux887AxlBlfh1HDL1UtOENOER0-oxCx47DYmgseFfgY0-2wQiC7MUn9smB3Pv7r4RnmdsuhOlsuP0ykM1YygIK6z4rFuB1pY7uZMaSgWYHLKJ7LH-rt02BikAz20Igu-xc98s1IsBr8X8eC2XdjXw8Tz_h56_v8XeDgeR5gZYK7OTNnolmdraJzi2HfC60z-wAAvEvQA_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
وزیر خارجهٔ آمریکا: اسرائیلی‌ها با تفاهم ما با ایران مخالف نیستند  خبرنگار:
🔹
آیا شما هم مثل برخی از بخش‌های نهادهای اطلاعاتی آمریکا معتقدید که اسرائیل به دنبال تضعیف یادداشت تفاهم فعلی است؟
🔹
روبیو: من نمی‌دانم از کدام ارزیابی اطلاعاتی صحبت می‌کنید؟
🔹
خبرنگار:…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/662978" target="_blank">📅 20:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662977">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMoHwM1xzvfSYqSOOVA4U28cqwSRdHodQ7wY4y1Ze-mHjtEoONhiaoYMq8LFtNL6xu6odzz1VNcg0SFccV_5DyHGWhMReJY7RZfOoqslte623iKxWcmqYj_Mx_MCBJ_NtQywVrl0zvnDMga8p8CtqUg4NW2mD5e1pu4_X4nrN9eky8v8NS8_5HWRSLpwlx04PXaXSr-n6ZQ_AJn4A0zxn4y7Px4pJdqNqDfG6nUE6w-8YhxqUJCjX9N4Bs5rjIG0K1JVbI1Fz8SCiBC-iCDCzTx_wb57kOQ6wIbHJLc7eKO-LjuGdLT-OY5GhHesqRsjths5R2fCpoNGyD0etAaMxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سخنگوی وزارت خارجه: صلح واقعی در منطقه غرب آسیا تنها با پایان مداخلات آمریکا و خاتمه اشغالگری محقق می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/662977" target="_blank">📅 20:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662970">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KCuic0uhDvrD9Ve41dW1se2YQ9SjEGEPAA_Z-Ad1CFzh42Vu6pW9Ei_25fXB1X4_DP0PhzJbZ4KYhrIEj1ENYadGT_GQf5WLgFo1pnBWLXzZ1QjFqpSxtLL9nAiE8aPFbOZBMllZwu8I7G1RSvtvEgS_VGzQjjTGTm6GDDiIHW0oJjWhmSIXcJvQc9XeoPB7w7naWFTrnS7_uoAIARIKp70LynzCF2Z9VadwQM5C_f6Fg3hRqVwU-yF_AILgOjwv4JVBIdNb3tOlJwezyXG4FmMbRtjcrgBAg6rGL9ffiMxWPdaT3iXtCRulOWQImZQRbAkfL0RG0N1O5B2SaDqVZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MoRZLqrMmOtl4DeCMuYRLUWGyM523IHKXCHw1g3zf2Kx_ic97KQ4poN_OEXjczRD5dYBU2Xk2makHfCgizA-TjHF8K4JQkvdnVqfG0vJVY8Avl5RTBOLhl3dsO6RKrYVtyq0vvFSI9D0HMxN2lCh__tfKO5HCTCcyYRAbKQ5kSIUHzPcO_grA4rNoZF4tWlGExtgWIc_VwnIpfaOIKDy-NLn_Y_eQmNWeVUdh6nFC_PCBwb3OxgvExXJhOCWmPnRqJiByeBXozDl6OemJJuFUKZHNCxa62L8oqQhlzJatEhmkR7P-Ik18E6Av7j9awjdfQOfVSvYCQuNQ-xYFY_ZcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iWKYd6UuxFTFfweEI4sLWNyjDN2T5rsky9HBULLnurKTcrgkC8PZQLLESnPPCfuamhuJKvwA6XY7mBjxsGAOlQCxxTdDr7GiSaAvhFlzdTRZpwE_JxqqmCgAU9NtU0UFNho85nNCaSjS9_r-yukMCk47pAjDJIeMrIKBsZWuLtbwS0F4pmrLRlDJYhrIdmo2A51ZAbMpYa6FGlqhp1BglJEaUg3PiDhHYC4we07F2IVIvnyTdLRKAkl0dTMZIE5kSYsodjWS9r25VwLfSt271--SwFL3TbSHQc7KmPnO8w2eiK_tfgf-IUD9NYh71rEUAHFi6UbZuP208XVQtMDvFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdO2gptj2sNsv9m7SlY3rPqWI2lSpLvo2c-Y2mCsvMZ6WaDBWP1tmye7TsoKUo_xZ5ViAwJFAHI_jBxJvVC63QWnD1eB_e9ilwXy9hrgnoEOrigoVcIGKx7WlKmRPWlt9goYRexg-qqbQYGG9yd2mSOX0HQiaOPLp_ffJpyOy5bIOWDg93rXZoDFOnELXUIHoZD-dL1YubVgBzqb3BsG1gKZPlWvqhuOdlFdxyehxKKrzz_Ktk7kyNyLPstfWH8JBcJ4yK5m9wt8Xr2zIBpXcRxxCIwJD4_JGMwOgEdA4KP0b4EhJOc8jsCywQsTp25q-BZSIdTutdAIiHeMAnVlPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gXgLAkigTqnx01w-7s90IIXYPHHBW51Rgk3gC__RUNepD-Bfe_dsg3MGmsXQ-HOURMj6RAw8SY4VkIonx8dOp5uHosZOvcLSExNbkvR3h3IuL9B7q80oz3QUVUKgG9CIAWlK-DdASjXawN5XxAZlRNpBx5JiY-XGnYRHHPw-QuIOWA9w4VFhkT2ZODbHgMXObv3VcAVnNvzmj3KN4mUJ9eFal2PjhIyxkCtZI90dsJgYFEUhq5-MiarULHfuK5fN1KyIuybbq31qKrru0wDqNrEJ_af9jq1f_3ShWjUK-YE4CAFVOTLo_MRiE-6CVpRnCCEl0F68PDAvUh6ry1Pb0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZXsNpV-cMqkx-V42TWi_UGmyjNEuSco3AFj-jiXppmr4DtJrb73RIlMbYHGomh8sRaHJtSDhn5HTQongM9i8XaRgNIIs3izzn_XS8jaRgqYpm3mC2CP1b9zgP2PzaBPeyBuJzt_Z4-dCnSh8YU_ucnOMj8traiI7DZSb_sn-Ez3-mACva00ztf4N5kFZyk00jfwhP4glPts0CIMVx1t0N1sGQLiUSdI_QlRKuKJH6MMxkgyTo3jYp4jZ5zuLsW0Qab3ckfoxr-0mzdvCnnrupC3Fey59ZUZPnDY_PBDPePFjEnIRAIVgx6XMfrgOnlP2GLHxN5ngCHJpAWGLeVCDow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZzzMA-bXh1bzUCNLfHIA4rcU0CWIstKGHmttnOMF_A9F2oRaq7N1JMDuLCIqPDBXutWTOswzWYvkwPd4lwW4_togL_Ufr8PW7xbpspzyE6EIZKX3qORbrL7C6a7RbtIXqOnkA79osKwTzHZRL7ht9l-EGI3RgoN-v7E0OrFE4s6iCkWGyXahTSMP_nydOspz8zIuXMPR4RI0R9T4fKH9-zUtemI1bDh5DW8ro0JQXbhR0U36m6mR3FGuXVy6LFens9gZV-_JawPyvG-x9Bk9IW6DqK6W1i_mkBEaLOUzO3dmyXvT_BW3jy5GfD8lg_IadFt21xr8xcMwYJD5Ke1J2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نشان حسینی
🔹
قاب‌های ثبت‌شده توسط شما مخاطبان خبرفوری از کوچه‌ها و خانه‌هایی که در سوگ اباعبدالله الحسین (ع) جامه سیاه بر تن کرده‌اند.
🔸
تصاویر خود را با ما به اشتراک بگذارید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/akhbarefori/662970" target="_blank">📅 20:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662969">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45d8ecba5a.mp4?token=NEAANLNLsa6CIfVSetXvdUYhavQWvbdhqdhmjC_EUGw3P4ZuJJy4Bi-RI-k9t468FZTqn4EuxAGANu0l5_ocX4nY7quA42bRTZzLLqAGTqfAunzZnWiEdXlm_9txPhIPq8XZNw722SY-wUncPWPkJBOZk8skj7WLIc8uvmihSSMAf3lctbL8ANkDYLcf7A7xTD8xRwy64YZ_Flm0CPGUtO6lzJyceD7dhSSv0vjZUKkDRYqkp3rHMdVrKAOYIiZCQwxdfhyQDT8M4WDeb9NeQ6pkOH5YUjDA4kx0bFuEpbakm1O7xLxSfQ9JSrRhBApvnXUeWol6VDHjehuVAW24bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45d8ecba5a.mp4?token=NEAANLNLsa6CIfVSetXvdUYhavQWvbdhqdhmjC_EUGw3P4ZuJJy4Bi-RI-k9t468FZTqn4EuxAGANu0l5_ocX4nY7quA42bRTZzLLqAGTqfAunzZnWiEdXlm_9txPhIPq8XZNw722SY-wUncPWPkJBOZk8skj7WLIc8uvmihSSMAf3lctbL8ANkDYLcf7A7xTD8xRwy64YZ_Flm0CPGUtO6lzJyceD7dhSSv0vjZUKkDRYqkp3rHMdVrKAOYIiZCQwxdfhyQDT8M4WDeb9NeQ6pkOH5YUjDA4kx0bFuEpbakm1O7xLxSfQ9JSrRhBApvnXUeWol6VDHjehuVAW24bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
وزیر خارجهٔ آمریکا: تمام دنیا با هر سازوکاری که برای استفاده از یک آبراه بین‌المللی یعنی تنگهٔ هرمز هزینه دریافت کند، مخالفت خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/662969" target="_blank">📅 20:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662968">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔹
آلمان پروژه ساخت ناو جنگی را لغو کرد
‌
فرانس پرس:
🔹
وزارت دفاع آلمان اعلام کرد به دلیل تاخیرهای طولانی، افزایش شدید هزینه ها و مشکلات مربوط به قرارداد، بزرگترین پروژه ساخت ناو جنگی خود از جنگ جهانی دوم تاکنون را لغو کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/662968" target="_blank">📅 20:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662967">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzpTTuV1_Yn4oj23bzELp3AazevmMmcNtqVPNiUdbWk2QN7GZ1cpi9T8_d0VtkEF9sFAeK2uzRzJxUqntbGvN85NUWwZQZSy4p_qkkGD2LQ6ZuNA-2VHwc-nG9bPJ9a0Lj0QZ99wFHSpuHII8fq3aHhF6L5-wO3ZYTahG7Ze9Nfrb--nhW_8IshuUK0MthZ82G7AJ9klhGS6aoMeDjXBECExXwIifJ4p2qB1o_evCDunVaapxHCbRdGRpdErH1I0ecaDGU0HxPdiqCUw9d3GZURZJwYPNzoTcspbU_999oUyTLhOiAEN0R_I6jXwATH9lM2j1X9Ies9Ku8mIfmvq7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تانکر ترکرز: ایران از تاریخ ۱۵ ژوئن ۲۰۲۶ تاکنون ۴۰ میلیون بشکه نفت خام صادر کرده است
🔹
دقیقاً نیمی از این مقدار در یک روز واحد صادر شده است؛ آن روز جمعه گذشته، ۱۹ ژوئن ۲۰۲۶ بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/662967" target="_blank">📅 20:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662966">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53461dc2d1.mp4?token=QgB3LWpzKMRsAzXKANr0sw-bIryKvImhXr3zXXPzo7-jcJS_AtDEbBUhLER0-RjdUYygp67_Uzqzg-F-y_dJdfDfMvyNZtKaLzla39znv6WE53kWtA67D4at6S7YYuWALTQDxhnfp4zZVmnEblcaMrkPgH8GWkGqxiWodRX9STR5oWd3KJ5NCTSmz50o_M_aJqZGtR3MvIMiKaGocmymBxUXOSAq0S64aaHqnalCCgQKbgnl0zh0LRJMT6yifhTP-IvOcvwGSAS1EG6FzOGQk5GCrH2BHJTNNfN6ICVLsHz-Rx8zOWxS1I2xyr4_uCRgd-RdpPgHBt883RsBj0wbDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53461dc2d1.mp4?token=QgB3LWpzKMRsAzXKANr0sw-bIryKvImhXr3zXXPzo7-jcJS_AtDEbBUhLER0-RjdUYygp67_Uzqzg-F-y_dJdfDfMvyNZtKaLzla39znv6WE53kWtA67D4at6S7YYuWALTQDxhnfp4zZVmnEblcaMrkPgH8GWkGqxiWodRX9STR5oWd3KJ5NCTSmz50o_M_aJqZGtR3MvIMiKaGocmymBxUXOSAq0S64aaHqnalCCgQKbgnl0zh0LRJMT6yifhTP-IvOcvwGSAS1EG6FzOGQk5GCrH2BHJTNNfN6ICVLsHz-Rx8zOWxS1I2xyr4_uCRgd-RdpPgHBt883RsBj0wbDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ادعای نتانیاهو: تا زمانی که من نخست‌وزیر هستم، منطقه امنیتی در جنوب لبنان را حفظ خواهیم کرد
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/662966" target="_blank">📅 20:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662965">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9928199fd8.mp4?token=j1Y3LubUTzxmpB_jjDVNhTUr3sPZSfpAujjR2PQTTJo8FqT0kW9G3zVvPrba0kWGCxCZSrFb2QaZ5QeNUS4C-91O4hH0LitvqBu29Y0Kg8WoORYeEYKbB9-j48dZqljTtMXZq6mWOqsnHDJqoHXSFIpK8EUaoUx6MaZQXJTkaaOTY8YRWuIfL-hn286MaRtcMSjwHzWoJSZt_qgaFjc56nvJKZxF4ACADOeeKUEbujuCAygCcvrrSiwHq_slKRW03iRux6m3grlp3O339YKsKHuwb4h-UYcLn_Mkgmwytxc2xQwvAUQTKZ_vcWrHCD76Va_NY0zZ5FG0ALPzNTELvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9928199fd8.mp4?token=j1Y3LubUTzxmpB_jjDVNhTUr3sPZSfpAujjR2PQTTJo8FqT0kW9G3zVvPrba0kWGCxCZSrFb2QaZ5QeNUS4C-91O4hH0LitvqBu29Y0Kg8WoORYeEYKbB9-j48dZqljTtMXZq6mWOqsnHDJqoHXSFIpK8EUaoUx6MaZQXJTkaaOTY8YRWuIfL-hn286MaRtcMSjwHzWoJSZt_qgaFjc56nvJKZxF4ACADOeeKUEbujuCAygCcvrrSiwHq_slKRW03iRux6m3grlp3O339YKsKHuwb4h-UYcLn_Mkgmwytxc2xQwvAUQTKZ_vcWrHCD76Va_NY0zZ5FG0ALPzNTELvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ادعای روبیو: کشورهای عرب خلیج‌فارس را در جریان مذاکرات با ایران قرار می‌دهیم  مارکو روبیو، وزیر خارجه دولت تروریستی آمریکا:
🔹
روابط مستحکمی با کشورهای عرب خلیج فارس داریم و از حمایت آنها سپاسگزاریم .
🔹
آنها را در جریان همه موارد مربوط به مذاکرات با یران قرار…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/662965" target="_blank">📅 19:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662964">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔹
روبیو: یادداشت تفاهم با ایران ظرف ۶۰ روز اجرا خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/662964" target="_blank">📅 19:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662963">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔹
ادعای
سربازان آمریکایی: پنتاگون شدت تلفات جنگ با ایران را پنهان کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/662963" target="_blank">📅 19:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662961">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F31mYvbTwOwEjji_cxGIL-gdsiHgZMe6xCDIPQHvdP6hRd8Tp5EJUC7LoH8YpdzhARXHmHEUVJkbbXYV3mRYo0CRRv63pPc_2psKb6pJx6P14eybqMLw2M1iGmmIxbahUP33BivU20-9E4vDxCdkvp7-7IAQXEQap6Ff-t6emVNEQbqCYkkmlUovlToh2oKhh0xWTkpiDbga7peQ9B-P_O58IwgOEAe9QDE5J6G70bvSNiAgmn8Dieh_7KHfTMS9JzGiXhu2F7h5ugsBDZq4Zbw_cWWTYgo65QPRyYcBS_ugimTeYHgZbHfzFzEtmwI6MMmy4lWHzMXY69aoIF9vzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dL7GNpMGOjfC1EqQgbrydVTHdXx0tObhhEGv8PK36io6FZXRG9s1IMB7KIrDkUR7-PBMr9HjN4F4K5ydrfMy8UWhoTUAZupH8bT3qvh1Qw3s2D--ey7aT8NYFeL3TbEdfmb8ZlJqVtEgMg8uwwZXbC3LF4wWAfHssFmB77XvYa0svrWVOkyD1f5lCA0ZxGnlNJF92xsCvbZ6tTy1ufLGW1pbRdElT9XMM4qvww3TRmtHXugy6gSz0xv9jxTSGS9gA16oS6AGau2IloMVIvxrEPqv72-lcfAx1Ae7l6ra-GW9CRxzjCXajfOFIkYocgwzI-zvMbFqvqDReh_hnARKdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴
اعمال شب عاشورا
#عاشورا
@Heyate_gharar</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/662961" target="_blank">📅 19:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662960">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ca134d1d.mp4?token=PxkpSH1sMoXPyk5fhpxi2FNAVyvzwq8HCiVZcJjc_7ReZ6PbLmMxG8FgxJp9Z5QYv0DY7lODT-GEkgxp0_HzXbBiAYFKh4Wc7btX5Xx3V9CaDVSVqnzNysj2j_Hq1yrGrfNxHnQZnKfFVIGoV16hzTYNfsKsM2iQuum0wILIbTvNSJyIU04wUxAAKgmGhj-xMeYdnfNba5s5BoYbONP0a-QKjcpJ5ZyCrCXRgEMiRtfB21U2ySasZDzfVkXGD5KXcE-8YQZMfElbeSOkYLYyvwRxyL4AgA2hqc7t68OxZFF0rukqfrLEDVsJjcKphCXzupNpGI_0UxCJ8Fs1a5ECVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ca134d1d.mp4?token=PxkpSH1sMoXPyk5fhpxi2FNAVyvzwq8HCiVZcJjc_7ReZ6PbLmMxG8FgxJp9Z5QYv0DY7lODT-GEkgxp0_HzXbBiAYFKh4Wc7btX5Xx3V9CaDVSVqnzNysj2j_Hq1yrGrfNxHnQZnKfFVIGoV16hzTYNfsKsM2iQuum0wILIbTvNSJyIU04wUxAAKgmGhj-xMeYdnfNba5s5BoYbONP0a-QKjcpJ5ZyCrCXRgEMiRtfB21U2ySasZDzfVkXGD5KXcE-8YQZMfElbeSOkYLYyvwRxyL4AgA2hqc7t68OxZFF0rukqfrLEDVsJjcKphCXzupNpGI_0UxCJ8Fs1a5ECVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیرمردان ناتوان حتی
با عصا میزدند بر بدنت
همه جا را سیاه میدیدی
به فدای نفس نفس زدنت...
🔹
عاشورا، یک پیام آسمانی در زمین که پژواک آن همواره به گوش وجدان‌های بیدار آزادگان در هر زمان و مکان می‌رسد و آنان را به خود فرا می‌خواند.
🔹
عاشورای حسینی تسلیت باد
🥀
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/662960" target="_blank">📅 19:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662959">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔹
روبیو: یادداشت تفاهم با ایران ظرف ۶۰ روز اجرا خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/662959" target="_blank">📅 19:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662958">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a822dd944.mp4?token=s7FQbNJXv9j4sk8-z_Bqn8OjzTQ7p-KUVEmOdXpz3U1xT2bC0Hftm6TcGMvEo4Ypkwz8T_ntJJ2zJAh7pDCq5UKzEogvYMtC2prg8tXgoAuGLZIs6HK-Zz3ZC5EhpGhJB1OTEWGEnsRmkopt0jt2lzp3iga8BAou1yjufQirT1Kz4pYBoyfX2OZ63yjTf29OEUrMwhPWbtHgTBNeKlBTXAZOAVZYLYEijQHDDZJbCll9YfSSg5o8FgzNuY2D9SR-9L_13J6SXHVED89npumSsQjo1g0q-vCdFGEGo4AcYslSl_Z_idV-hXPAgjrvuiXmgMdk-zSoJ-VJNqarzJhZ3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a822dd944.mp4?token=s7FQbNJXv9j4sk8-z_Bqn8OjzTQ7p-KUVEmOdXpz3U1xT2bC0Hftm6TcGMvEo4Ypkwz8T_ntJJ2zJAh7pDCq5UKzEogvYMtC2prg8tXgoAuGLZIs6HK-Zz3ZC5EhpGhJB1OTEWGEnsRmkopt0jt2lzp3iga8BAou1yjufQirT1Kz4pYBoyfX2OZ63yjTf29OEUrMwhPWbtHgTBNeKlBTXAZOAVZYLYEijQHDDZJbCll9YfSSg5o8FgzNuY2D9SR-9L_13J6SXHVED89npumSsQjo1g0q-vCdFGEGo4AcYslSl_Z_idV-hXPAgjrvuiXmgMdk-zSoJ-VJNqarzJhZ3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
مارک روته، دبیرکل ناتو، در گفتگو با فاکس‌نیوز: فکر می‌کنم ترامپ دقیقاً همان کاری را انجام می‌دهد که لازم است
🔹
یعنی تضعیف توانایی هسته‌ای ایران؛ می‌توانید تصور کنید اگر ایران به سلاح هسته‌ای دست پیدا کند؟
🔹
ایران صادرکننده آشوب است؛ صادرکننده تروریسم است؛ این مسئله برای منطقه فاجعه‌بار خواهد بود و برای کل جهان هم فاجعه‌بار خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/662958" target="_blank">📅 19:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662957">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔹
تلگراف: ترامپ ممکن است پس از انتخابات خواستار توافق جدیدی با ایران شود
🔹
روزنامه انگلیسی تلگراف بر اساس اطلاعاتی جدید فاش کرده است که دونالد ترامپ ممکن است پس از انتخابات میان‌دوره‌ای کنگره توافق کنونی با ایران را کنار گذاشته و خواستار توافقی جدید شود.
🔹
یکی از اعضای نزدیک به ترامپ گفته که او برای مهار تورم فزاینده و محافظت از کرسی‌های آسیب‌پذیر حزب جمهوری‌خواه در جریان انتخابات ۳ نوامبر نیاز مبرمی به توافق فعلی با ایران داشت.
🔹
گفته می‌شود ترامپ خود را آماده کرده است تا پس از انتخابات میان‌دوره‌ای که موازنه قدرت در کنگره را تعیین خواهد کرد از این توافق با ایران خارج شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/662957" target="_blank">📅 19:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662956">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDoSc0XUA5GOZzdF8AO1RcXB7aMWnGxajqPhIcXFQJza5N_c2jH53TyzbmmsJsdNV2hqDK4oI7L_dfayIjMgHGZWkZf1pxenuGMS0E9PVzDIYsoswl1x2S4kupLxmCfaILTRR-Xf4a8PMrGV1ozHbRbzcgDqMaYBqhsKjqarp6V4JoZRDZAYV4ONvV3zvA3XEgzUP58kWfNxEPUNyNHvI-2X1sCfLsAYRZBGpZ79ioWi8lDicYdTqcttupBw8nRXPU59C7htNhgmUPU3tos-p2YvLY4F6z-uifrZFTGXQVuNnE3oTUMDURM7de9r3J8zhock_AYWDQ4nz9WkZr3Cow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تداوم نقض چندین باره تفاهم‌نامه
🔹
حمله هوایی دشمن صهیونیست به نبطیه فوقا و حمله توپخانه ای به یاطر در نزدیکی بنت جبیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/662956" target="_blank">📅 19:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662955">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvDo-EDftU2LCSBDRmEdmX0Vg66B4R-pnKeIUtsOF_cohUtIP06sJxiNw5ifAvZZceGF1ydG_mRx__5pvUNrNguFrvIpfgQhh7ePlIc2uheTxH5l-CNQsPjRke5Sw_BpDRLygSlCUKs6E__NW066IAEI0dJKPK47DBzhcGMgRqnXResiY4Sl2pV6wmvPoPU2bGmAcIHV9C3Lc4Qd2H0sFb6BLLI6Oh2OZeF8pPhsoTTlAhJWe2dPeDYnDOctzobmfY9LM8ORCaD53H3eI0vM6zVGgDo1nMjsjhsVT1Kl1z9HmIEV0ryBP1aoXEDfrQ5AmIoGLEiTOf3Yw5Ovv82s9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تصویری از هنگام ورود و اهتزاز پرچم خونخواهی در مراسم بزرگ یوم العباس زنجان
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/662955" target="_blank">📅 19:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662953">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abaef1863b.mp4?token=J0mwYNqqDejj6OWU1Su6M7okCWc8ssiM325kXKALDJy9b5MC03K5nJrQ5msWJywVnEwF515LiS_sw_uURlkcUvcx5yCjvhQ0PX2DqeNpMxllWDbVWjYUpoIHKHorBQDsgumd0v4_U3jetZExjm8fmnVncxgGQOhoJFtIyrTve_gH-0yO3sLfEcxsRcAGoK2AXdkhg0KwG3e3WADjAV0z2XvvxhNGQvx8DjAuj6VUWU0wWzWvO_WOlq44Jo4wMMJm5Pt-mtrKxi19tIezyM-Fdph9gmUSoBNlGKTH4GDMKvVU5XhkO1hhRVK2Ju3V9q0KW9auwgkKRGZ99uY1XVF-rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abaef1863b.mp4?token=J0mwYNqqDejj6OWU1Su6M7okCWc8ssiM325kXKALDJy9b5MC03K5nJrQ5msWJywVnEwF515LiS_sw_uURlkcUvcx5yCjvhQ0PX2DqeNpMxllWDbVWjYUpoIHKHorBQDsgumd0v4_U3jetZExjm8fmnVncxgGQOhoJFtIyrTve_gH-0yO3sLfEcxsRcAGoK2AXdkhg0KwG3e3WADjAV0z2XvvxhNGQvx8DjAuj6VUWU0wWzWvO_WOlq44Jo4wMMJm5Pt-mtrKxi19tIezyM-Fdph9gmUSoBNlGKTH4GDMKvVU5XhkO1hhRVK2Ju3V9q0KW9auwgkKRGZ99uY1XVF-rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
جان مرشایمر، استاد علوم سیاسی: ترامپ خیلی واضح تصریح کرد اگر جنگ با ایران تمام نشود، فاجعه اقتصادی در جهان رخ می‌دهد
‌
🔹
به همین علت مجبور شد توافقی با ایران امضا کند که از هر نظر به ضرر آمریکا و به نفع ایران است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/662953" target="_blank">📅 19:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662951">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
فرمانده قرارگاه مشترک خاتم الانبیاء: کارکنان پدافند مردانه ایستادند تا ایران استوار بماند
🔹
جمهوری اسلامی ایران امروز با منفورترین جنایتکاران عالم روبه‌رو است؛ دشمنانی که هیچ‌گونه پایبندی به اصول انسانی، اخلاقی و حقوق بین‌الملل ندارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/662951" target="_blank">📅 19:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662950">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f831a8fda.mp4?token=LPomIsJf9T5z56nqmoqoCpuGWw3Gs5-UydjKWWzAS3kIXfR81NgKCeUzxJLfhPUSAPkfSk41VPxTFplcXiYSZhjnrTgBSPWyDAJinCr38ctPQNXysfBiczTz3LcGoIVMwCWnHP00UIXHWDcqCnh2tA6mGjFdNAnBW3gdEYSzSzHV3ehmmKa6OtQYy01b-dyKjtlXGf8ejBS8epuA2UDqd-MX3h--2C-4PYnw6dapKUqjLulwYaSKZdogx1zqHGK2dPFKcc30qrRh8nov2umvJCZyiUq01VGn49GyrkFBau8eFwhThienwL1zylhTSxwAilHyFDTDuwHlD9B5LVgmsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f831a8fda.mp4?token=LPomIsJf9T5z56nqmoqoCpuGWw3Gs5-UydjKWWzAS3kIXfR81NgKCeUzxJLfhPUSAPkfSk41VPxTFplcXiYSZhjnrTgBSPWyDAJinCr38ctPQNXysfBiczTz3LcGoIVMwCWnHP00UIXHWDcqCnh2tA6mGjFdNAnBW3gdEYSzSzHV3ehmmKa6OtQYy01b-dyKjtlXGf8ejBS8epuA2UDqd-MX3h--2C-4PYnw6dapKUqjLulwYaSKZdogx1zqHGK2dPFKcc30qrRh8nov2umvJCZyiUq01VGn49GyrkFBau8eFwhThienwL1zylhTSxwAilHyFDTDuwHlD9B5LVgmsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تصاویری از مداحی و نظم عجیب یزدی‌ها از نمایی متفاوت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/662950" target="_blank">📅 19:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662949">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ae119ec00.mp4?token=akQxSIYih0cIbgUKMgI8tFlU_r_WzvNryS4bSGfVWEinrfR5_FctD-2uyVmZRf0KYgVxmSFz46nbvvb4mp58uhnfKWRRTnYIT8D_zWvkmW8LP_kTtsLDRNGidzySIoZyazg9ity4TUAh_WD9p1AiWh19ByGLWORVaYN7ZYS2ZHbyrvEE0xezrjTqH2obSdu-yt9JKKnoyvJeFX0Tly4J8x1f_blPc6UVCTxrcrHGTnATkLLolb4m2b_dh3fReSyRWImaV4bLT1SGPBnKtTAoykW764N1FxhGRzCSxYo18RlF1bx5b5ml_Cj2aKLBm1T_TVdmCsblOCbeFaJjyJzWNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ae119ec00.mp4?token=akQxSIYih0cIbgUKMgI8tFlU_r_WzvNryS4bSGfVWEinrfR5_FctD-2uyVmZRf0KYgVxmSFz46nbvvb4mp58uhnfKWRRTnYIT8D_zWvkmW8LP_kTtsLDRNGidzySIoZyazg9ity4TUAh_WD9p1AiWh19ByGLWORVaYN7ZYS2ZHbyrvEE0xezrjTqH2obSdu-yt9JKKnoyvJeFX0Tly4J8x1f_blPc6UVCTxrcrHGTnATkLLolb4m2b_dh3fReSyRWImaV4bLT1SGPBnKtTAoykW764N1FxhGRzCSxYo18RlF1bx5b5ml_Cj2aKLBm1T_TVdmCsblOCbeFaJjyJzWNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
مدودف، معاون رئیس شورای امنیت ملی روسیه: اکنون زمان آن فرا رسیده است که این توهم را کنار بگذاریم که یک کشور یا یک بلوک واحد می‌تواند قوانین و حقوق بین‌الملل را دیکته کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/662949" target="_blank">📅 19:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662948">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-H5E41kW2MdAXUadzNWxfXe9ctAV_fqACMXqN6XWp4V8KJtlvtq9wtwqNmk3XGXkdfzXcbZcgAgicY8fszz5oXL0UfrOxhvnN7KnoLGY7bmlXLVvbKJYdDRxOOuxhJxSRG8I0FGfcPeV5Wf96ovQ0gz6QQyyaFPINStMtg3wVk1YbdAgB16NFGY3Z-mLFxBAzcTpVkyKRqzVwD3hE3uVfgWJ_xLdxicdYbPUKfvGTFU8oFr_4FA99v9FeXRmnuCAb-otUxiyJ6p1buV-rTCO9k4xvGOizy69uAh6hQ0RQK130wgt01rgIJHH_MD-q3ROJIqnmfvoCJV4tk48lVcrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/662948" target="_blank">📅 19:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662947">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔹
ادعای ترامپ در مصاحبه با فاکس‌نیوز: ایران به عنوان بخش اولیه توافق، تاکنون ۵۰۰ میلیون دلار کالای آمریکایی خریداری کرده است
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/662947" target="_blank">📅 19:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662946">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a430f52c54.mp4?token=lFI-ahzc2BwwW3XMyysIDZgBGQuIzj-L_BqUcsGIvcyo4JiXT5UHbD1kYnRvXpaN64-gWT_TRrIFScpNhrUJmErN6ovVVhxI9pUtpFZe1wd68ZKzZUwZqLRcBB7Fd4cZMhb27M2u-LlFk9zBhZ9XrKKhckJ21tZN9n9OjPs_2traIo6pxUPQnhZS74abhueonFUqA7iLGnZFB9CaA73PZGIwyOO0gmMgK0ZjkB7Z144jXOxqgRwK38Dn5cRjGcoK32jjcphFZyigFsBZ8lstyJKgGzyh6-miMofwBYEm-OFsUcz2H9GoAZ8qtY4FsYvNoMySdMiVkbxgIKtPsK0C3H_kTms2iOLJzpD45fhS75L6WB-XkqH39FJTlmLz37NUsleQ3ENtUSIqV0RrOfR5rCvp8NxbLtK_l7ZLm6ahWuBDpUPhcAx1IWOiUHEfOIdzPAw5XrXiSfonp1Vp67dtNErejd-krGfnKlTM2-QhnTdK5IlKKB9zd_YPOAVz630HfOSWegpL3OCXb9jRurV-W4D-EWHFhSh3gi2tk7_wawK8WWRrRsw9UCr3FpztdQZAfc7Y1297WaCMmTqtcp5n8j8PNm8tvVo9mTh_K0viL-G3d7KnmiL0bletBPfiovOfBAfZpI_t-NOc-MYeluVZWdgUMPQwTaHxSf2_BhWzVIo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a430f52c54.mp4?token=lFI-ahzc2BwwW3XMyysIDZgBGQuIzj-L_BqUcsGIvcyo4JiXT5UHbD1kYnRvXpaN64-gWT_TRrIFScpNhrUJmErN6ovVVhxI9pUtpFZe1wd68ZKzZUwZqLRcBB7Fd4cZMhb27M2u-LlFk9zBhZ9XrKKhckJ21tZN9n9OjPs_2traIo6pxUPQnhZS74abhueonFUqA7iLGnZFB9CaA73PZGIwyOO0gmMgK0ZjkB7Z144jXOxqgRwK38Dn5cRjGcoK32jjcphFZyigFsBZ8lstyJKgGzyh6-miMofwBYEm-OFsUcz2H9GoAZ8qtY4FsYvNoMySdMiVkbxgIKtPsK0C3H_kTms2iOLJzpD45fhS75L6WB-XkqH39FJTlmLz37NUsleQ3ENtUSIqV0RrOfR5rCvp8NxbLtK_l7ZLm6ahWuBDpUPhcAx1IWOiUHEfOIdzPAw5XrXiSfonp1Vp67dtNErejd-krGfnKlTM2-QhnTdK5IlKKB9zd_YPOAVz630HfOSWegpL3OCXb9jRurV-W4D-EWHFhSh3gi2tk7_wawK8WWRrRsw9UCr3FpztdQZAfc7Y1297WaCMmTqtcp5n8j8PNm8tvVo9mTh_K0viL-G3d7KnmiL0bletBPfiovOfBAfZpI_t-NOc-MYeluVZWdgUMPQwTaHxSf2_BhWzVIo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
حاج قاسم کیست، دشمن هنوز حیران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/662946" target="_blank">📅 18:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662945">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222f86887e.mp4?token=q2hiOdodxJCU5XtxI7feWvVF0S8_1oyFUBmfcbCAu8jgGvSrP6UWWqepm5mw0q-WJXIsu8QoELDvX9A966FIcQe-w26Y-bf5i1tthgzTmM42FF3t_9dJh7w8A25N1L4y4b-L9tIhm7idp0ZS-fl3p0HDOwayZW8gxk1IrFW7YqPwRT4hFrz8qspojrQ8SMHrD1XBiEUNEOL-B9TTsFTJKH7nvlWWwIdsTKOcY8nDeetXB63jJHZV_xWdo7InUw__H4mIiYiKJrVS1Zv0yauUcLdE_92gfW1S4BhnD0lTH-KOKAFeavGcB7gtbONFhbeKtAMszsTvS-Gkle9uhnX3mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222f86887e.mp4?token=q2hiOdodxJCU5XtxI7feWvVF0S8_1oyFUBmfcbCAu8jgGvSrP6UWWqepm5mw0q-WJXIsu8QoELDvX9A966FIcQe-w26Y-bf5i1tthgzTmM42FF3t_9dJh7w8A25N1L4y4b-L9tIhm7idp0ZS-fl3p0HDOwayZW8gxk1IrFW7YqPwRT4hFrz8qspojrQ8SMHrD1XBiEUNEOL-B9TTsFTJKH7nvlWWwIdsTKOcY8nDeetXB63jJHZV_xWdo7InUw__H4mIiYiKJrVS1Zv0yauUcLdE_92gfW1S4BhnD0lTH-KOKAFeavGcB7gtbONFhbeKtAMszsTvS-Gkle9uhnX3mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تاسوعای حسینی در حرم مطهر حضرت عباس(ع)
🔹
همزمان با تاسوعای حسینی، خیل زائران و عزاداران از نقاط مختلف جهان اسلام در حرم مطهر حضرت عباس(ع) گرد هم آمدند و با برپایی آیین‌های سوگواری، یاد و نام علمدار وفادار کربلا را گرامی داشتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/662945" target="_blank">📅 18:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662944">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1SjcE43eqWi_PfafuMCNQqTmdXRVYsDdVQ-FukIQVJzw1hyIGWFw73CRGFIwKC5Jfteww7C81aGVdiGGkpAH9VIWsC4BDHs6iBdjb_MSmjZUIsGqCFJ9B-8ncw5bLFDozPFt_xIdPmi3E75yTGOeOXexfVL_FN5Km2XVK08QLRDigfD_RL-FxRhT0HNaDvhNOGHSOslYR9DOAAFJA4HegorvD8WK5k7SfZLmFUZdWwzHyACZ3UN1tdzdod-6iOf66t8f5WBHa_VSJs3twjIkfeojnAUjwaBQpxzsugsoTS9qwnK9fhuQTR-ONa4NFqAiAS_G5y5CA_CXZnxvrl6ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فیفا تبلیغات مربوط به مشروبات الکلی را از محل دریافت جایزه بهترین بازیکن مسابقه در جام جهانی ۲٠۲۶ حذف کرده است؛ تا به عقاید و باورهای دینی بازیکنان مسلمان حاضر در مسابقات احترام بگذارد
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/662944" target="_blank">📅 18:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662943">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔹
نتانیاهو: برای حمله به ایران از ترامپ اجازه نخواستم، فقط او را مطلع کردم
#Demon
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/662943" target="_blank">📅 18:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662942">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔹
آمریکا فعالیت سفارت خود در کویت را از سر گرفت
🔹
ایالات متحده آمریکا همزمان با سفر مارکو روبیو وزیر خارجه دولت دونالد ترامپ به کویت اعلام کرد که فعالیت سفارت خود در این کشور از سر گرفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/662942" target="_blank">📅 18:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662941">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaZP6ADyYMSXbKmv1dZl1q7RoDxjXZAroYkbeSp0IoJYT4ki6xXJkhjfBMn6JXWYuuHLBZe1cch_IlTsOUAsYk2N1wKIUmMiKjeDP9WQgB2-baURvSMHVTZ48iFhPB0EJw_8YrHEHTSgQMKmC-Rdj7ldhkEwCzrS99MBQ4iipVsvZSN7zpapKD_mr10K7fns-ytUpdETKOVB3aOk2uPmPdF49jv89mMMvOR2pznS5ELYK-bllhsI3sGFeKHhhsaH85LJ5dZ3a8smuhqFUf9fGSq3f6YSXi39-mYrtkoC31VLmEQdTeP_rCsCXVzEWwcJ3NgxdAINwlh1MXCvlhbL4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سخنگوی کمیسیون امنیت ملی: تنگه هرمز را با مذاکره فتح نکردیم که با مذاکره واگذار کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/662941" target="_blank">📅 18:30 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662940">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e0667054.mp4?token=MSapErE-5VRABB6tCKjk50ZAh5qrnLiZjM-2ci0mFu0Fm6rkbYMapBvARb32U0sxV8YyTrOxYa1A2DZiG9QpjljGsIKW9SyLDb4skD9mHhOvPtCDBcD_yGIJ0ETiABNoWXiBeO9x2Bfr5DACBH7d1xZ3zvBIC8hB8KQoZakqgjIAN4s9B9u-RksCO8J8IG36Y6TLEXp8jCzo9MG1ZEeCzWXTV1Tk50tTlWWCDmP6h74V49eaztdjUR2j_oCm6cVc0euxEiYs1WvdnkKmlF45Gfu6ItyrqYeTdm2RDHmd_17W7sLr0yKR6wNkJhzaKoTJ6WzUEEfqnsLq4enPgLAjrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e0667054.mp4?token=MSapErE-5VRABB6tCKjk50ZAh5qrnLiZjM-2ci0mFu0Fm6rkbYMapBvARb32U0sxV8YyTrOxYa1A2DZiG9QpjljGsIKW9SyLDb4skD9mHhOvPtCDBcD_yGIJ0ETiABNoWXiBeO9x2Bfr5DACBH7d1xZ3zvBIC8hB8KQoZakqgjIAN4s9B9u-RksCO8J8IG36Y6TLEXp8jCzo9MG1ZEeCzWXTV1Tk50tTlWWCDmP6h74V49eaztdjUR2j_oCm6cVc0euxEiYs1WvdnkKmlF45Gfu6ItyrqYeTdm2RDHmd_17W7sLr0yKR6wNkJhzaKoTJ6WzUEEfqnsLq4enPgLAjrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
وزیر امور خارجه قطر، که پیش‌تر بنا بر برخی گزارش‌ها از سوی پیت هگست با تهدید به ترور مواجه شده بود، در جریان مذاکرات ژنو برخوردی سرد با جی‌دی ونس داشت؛ به‌گونه‌ای که نه به او اعتنایی نشان داد و نه با وی دست داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/662940" target="_blank">📅 18:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662939">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0367a0040.mp4?token=r_hQiGKp_KVLmLZ0QV3RwSMHENTY0E8fru-pcpi0gypVapJe5v-hzNKlV_-6nb7fxOjpyyXoJ_eykWHNH1mXd8TzrVw3Nv3T7Q7rOrcTkbh2UJ-YBrOhfFbhPF_Il1Zu0Fk353LBdr-VyMe41xqmf8q6gdpmLJ6PavuwhSJOpPtNxVcyepgxnoydl9ESDUjumCgO7jvO87rCMP6N5yJ1I6KPY7RpJbkcZqhi-HUwLYmA38zVj1nIK1y3Wq6MKmHs-SDt4r1wt7ZYHvMoxSNGb1uukcO67U1u77PHdrvkln2BYTfpE7kXMWwr8Yu71QnZUGDq8H9zOWmSZPrWS3Mz1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0367a0040.mp4?token=r_hQiGKp_KVLmLZ0QV3RwSMHENTY0E8fru-pcpi0gypVapJe5v-hzNKlV_-6nb7fxOjpyyXoJ_eykWHNH1mXd8TzrVw3Nv3T7Q7rOrcTkbh2UJ-YBrOhfFbhPF_Il1Zu0Fk353LBdr-VyMe41xqmf8q6gdpmLJ6PavuwhSJOpPtNxVcyepgxnoydl9ESDUjumCgO7jvO87rCMP6N5yJ1I6KPY7RpJbkcZqhi-HUwLYmA38zVj1nIK1y3Wq6MKmHs-SDt4r1wt7ZYHvMoxSNGb1uukcO67U1u77PHdrvkln2BYTfpE7kXMWwr8Yu71QnZUGDq8H9zOWmSZPrWS3Mz1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
تصویر آیت الله سید مجتبی خامنه‌ای، رهبر معظم انقلاب اسلامی در دسته عزاداری شیعیان با غیرت عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/662939" target="_blank">📅 18:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662938">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf01081c61.mp4?token=bTbPQx0AFvIvD_6sf0WIV0QKqJ7IK6a7w9V2srIjYOlLxO1n4vak0MadkwpGWOl2MuQhqiOXGG202pZi32jtegGf0BV66eHCR0WLWfaaVEjP5ICzNy5sC46m7DyqwxDxjgRvtZsGrCgFTqwjoAbcHEk4QlGrKZVwN_S6PcR3fMopbTuE2LEFihFm4CwwR6DerKjjd86Equ74zQETswdbxlktAiA3Hzl_mb9HYXWnC11uOlHpBxyXhI_37_sFub8K4cnH8tRbH-4Zr80n0ZHr5rKqKuU2Ag65FEh-u5Yd-gpZJP9Uxq4_FkmrISTrGnExQUY6SIjnt0Pbjla28VTKKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf01081c61.mp4?token=bTbPQx0AFvIvD_6sf0WIV0QKqJ7IK6a7w9V2srIjYOlLxO1n4vak0MadkwpGWOl2MuQhqiOXGG202pZi32jtegGf0BV66eHCR0WLWfaaVEjP5ICzNy5sC46m7DyqwxDxjgRvtZsGrCgFTqwjoAbcHEk4QlGrKZVwN_S6PcR3fMopbTuE2LEFihFm4CwwR6DerKjjd86Equ74zQETswdbxlktAiA3Hzl_mb9HYXWnC11uOlHpBxyXhI_37_sFub8K4cnH8tRbH-4Zr80n0ZHr5rKqKuU2Ag65FEh-u5Yd-gpZJP9Uxq4_FkmrISTrGnExQUY6SIjnt0Pbjla28VTKKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
با این ترفند عالی بادمجان را سرخ کن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/662938" target="_blank">📅 18:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662937">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔹
افشاگری رئیس ناتو: ایتالیا در جریان جنگ علیه ایران پایگاه‌های خود را در اختیار آمریکا قرار داد
مارک روته، رئیس ناتو
:
🔹
ایتالیا به ۵۰۰ فروند هواپیمای نظامی آمریکایی اجازه داد تا از پایگاه‌های این کشور در جریان حملات آمریکا و رژیم اسرائیل علیه ایران، به پرواز درآیند.
🔹
کشور به کشور، متحد به متحد پایگاه‌های خود را در اختیار آمریکا گذاشتند./ تسنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/662937" target="_blank">📅 18:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662936">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d2ac6eadb.mp4?token=DQYmG0WjlZhSolecfaU1ntyxXKg74NFlKIqFbyXlfpDhRti8KLx5TMA953K7Wcxb-pMmWkr7WdLHVWrIkUJOyTTRzGXWeje2JbvGkdDD6KDrkObI8ExLhzKpxu39n22PbawYXbKS2kBrAGihUiKN2SgjnNw5swxxygUtQdZjlQ7RO74bfIlrGnq_p4Ig4LH6kwC30TYZ8O50zUcQUh_6ZUVbNqvBJLSJTz0ZeRTrqs6aejE-Sarf4seD5u4rFIiveoTcfPN4t4Hb62Ajf4D0XwcirrYvMY_BX3GnRshu5woXsd8HXl7yl_xLsA4t1B2R0AXQyCBEVJ2Fm-tKJcC9Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d2ac6eadb.mp4?token=DQYmG0WjlZhSolecfaU1ntyxXKg74NFlKIqFbyXlfpDhRti8KLx5TMA953K7Wcxb-pMmWkr7WdLHVWrIkUJOyTTRzGXWeje2JbvGkdDD6KDrkObI8ExLhzKpxu39n22PbawYXbKS2kBrAGihUiKN2SgjnNw5swxxygUtQdZjlQ7RO74bfIlrGnq_p4Ig4LH6kwC30TYZ8O50zUcQUh_6ZUVbNqvBJLSJTz0ZeRTrqs6aejE-Sarf4seD5u4rFIiveoTcfPN4t4Hb62Ajf4D0XwcirrYvMY_BX3GnRshu5woXsd8HXl7yl_xLsA4t1B2R0AXQyCBEVJ2Fm-tKJcC9Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
رونالدو بعد از دبل مقابل ازبکستان:  یه جوری رفتار می‌کردن که انگار من دیگه از فوتبال خداحافظی کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیشتر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود، باید بهش اعتراف کنم، اما خب... ما دوباره برگشتیم!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/662936" target="_blank">📅 18:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662935">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2996f9020a.mp4?token=tMu-FdG6KLFQF93Ae7vPt9bgmtUxDwI028-CcJ22K9XkYzSH7oonqBRohDq0mS_CcIeW04w3OE2QIm_FNPzja2U22OwVQ9_KowbrxGMm0wq-NUN2VRt3FKNB_nO9cxudc39jSdkoRpXMICVFO9bdSj65jq6o6AT7B5eDw3KIIQ63IgxrWZU_KzHs5Va6oy4XohohkNBqTsgpwURlxE0fHa0pWW1X5C36pPkaTjXfj66DrvIudqTsVsYx84sXJQMV-bcqh65tlRKn3eDu0W12hKEz3UBqtuRfyYuZkYbIvQdmR-kUKhS7KPLVlYxJPtOu0adT0Pfh-JIrKMlKg3ZZYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2996f9020a.mp4?token=tMu-FdG6KLFQF93Ae7vPt9bgmtUxDwI028-CcJ22K9XkYzSH7oonqBRohDq0mS_CcIeW04w3OE2QIm_FNPzja2U22OwVQ9_KowbrxGMm0wq-NUN2VRt3FKNB_nO9cxudc39jSdkoRpXMICVFO9bdSj65jq6o6AT7B5eDw3KIIQ63IgxrWZU_KzHs5Va6oy4XohohkNBqTsgpwURlxE0fHa0pWW1X5C36pPkaTjXfj66DrvIudqTsVsYx84sXJQMV-bcqh65tlRKn3eDu0W12hKEz3UBqtuRfyYuZkYbIvQdmR-kUKhS7KPLVlYxJPtOu0adT0Pfh-JIrKMlKg3ZZYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ویدئویی از حجم بسیار زیاد آب رودخانه سیمره در شهرستان دره‌شهر ایلام
🔹
نیروهای امداد و نجات هم از پس سیمره برنمی‌آمدند
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/662935" target="_blank">📅 17:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662934">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INwJvF64pSdKtFl0wigenECe5qOSOxJlojzmqWV0SyKzx3JLdHe-3T3-lqYvpDC9vXKfJ6cJMb3hcTw57-whPsyD_8N_lsorps65_9MRHe4_CzyDcMEpwLfcm06xJ_7gjUhDlkIQvw-Zt5E35FmqI9ya8Pi3wey_AJheKcwhoGYf5aWzbI1hithuezMM78QTvLX4s4-mXaVBQm2lr4ijK0kVrjbvvHOThpPXTpeMboRgQuChan1BeNaL6Efa0fQ90MQCiTTsxFCzj3CKwDMgtxaZxqb7M31QDQzTuvCpyQPB2LrqSPnKz3DIy-Ndfu5FgXgIe9E8RG2OUizciqOyTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سقوط طلا به زیر ۴۰۰۰ دلار؛ پایین‌ترین سطح از آبان ۱۴۰۴
🔹
قیمت طلای نقدی در بازارهای جهانی رسما به زیر مرز ۴۰۰۰ دلار در هر اونس سقوط کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/662934" target="_blank">📅 17:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662933">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94068cf6ec.mp4?token=G61kiHUkABGXncySGbQtF-stCHPMe7z0sr6BV1gwwBqLbCxQhFhNI21jAVH9wTGgWOsl7C9YLvLlJIdCOpRgx0Jl_T9PY2VCIt03s1m_tlUwvZcb7C6KVw4rm_0q2lkEzuv1QWYyp1_0sHquX5jmWUzNHPzy4t4KNESToAVf2ke1yy_aW2fSWw-1bAPbouhWP9x-IJtMCTrGLNk98og6oc40AqVu0JjWYV3vybtxt5TtojPImjd05WqHPFQNgE87ubPdLxAE11zLLUYRz-JCSBcWKvcRVeFfNwF4cldP36l7mMXJ1ASzTA5-Em3FCwealP63cX-vILnHqSprGsAb3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94068cf6ec.mp4?token=G61kiHUkABGXncySGbQtF-stCHPMe7z0sr6BV1gwwBqLbCxQhFhNI21jAVH9wTGgWOsl7C9YLvLlJIdCOpRgx0Jl_T9PY2VCIt03s1m_tlUwvZcb7C6KVw4rm_0q2lkEzuv1QWYyp1_0sHquX5jmWUzNHPzy4t4KNESToAVf2ke1yy_aW2fSWw-1bAPbouhWP9x-IJtMCTrGLNk98og6oc40AqVu0JjWYV3vybtxt5TtojPImjd05WqHPFQNgE87ubPdLxAE11zLLUYRz-JCSBcWKvcRVeFfNwF4cldP36l7mMXJ1ASzTA5-Em3FCwealP63cX-vILnHqSprGsAb3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
همه‌زیر بیرق حضرت عباسیم(ع)
🏴
🔹
این بیرق نه فقط متعلق به یک‌جمع بلکه مسیرو هویت یه امت است؛ مسیری که همه ما به تأسی از رهبر شهیدمان، خودمان را زیر سایه بیرق علمدار کربلا می‌بینیم
🔹
منتخب تصاویر از حضور عزاداران و آیین «علم سلام» در حرم مطهر رضوی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/662933" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662932">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6oaBzW3RL1S8h7NDMZ8XKOBr8qdq8dGiXs5PamCCeCeGodwVvGLuHDdmygBCC1cXaY6cahlvwvnGhyndiC0cSIeq4br28ABM-MYJ9L9oi3XFLO1rAGt9USDeIIvaxoyWMuD41I26C7suUHpXoQdbxcNSynDBLRiI-Id6t43twqwqzvtLr-5qsnExEyehZompdZgDeHiCRjpC1XwI5Z2RSxep0XpUdOWDK2VM6I0Im3xV_L_30747afWNasE0sg0AcrSdbR-RiEOe8SOaPi_wsuo0eVrxTk_o46A19fZAHWQW9Zn5gQhZgptMEZKy_eGCPwm_GAMADJvbGyFOd01Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
۵ اشتباه رایج تابستانی که می‌تواند عمر لاستیک، موتور و سیستم خنک‌کننده ماشین را کم کند و خرابی‌های پرهزینه برای خودرو به بار بیاورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/662932" target="_blank">📅 17:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662931">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDcuNyitGKo42uRd0wKXctNBUyju7qSe-0VqQXmVl2W5bAioIM5URTgGZu-_HWb50oil0imVrOnXPGq8rfVSWlzaZBxiXMexeHk1JiDmskDYyVobZ9XaN1ANbSsRRyfd_eDd62VDHnqxjoYf5DsMpf3mbl-QWXuOmzkOcWdy6MJxJvOjHSNW3m4g14T433VFr77lkK5ytNlB1-vS3LMSuXEYm01DIWyoh49VoHWmv2TcYgxR8D0Qs9MjP1zJ8wb0dUG5Y0v847UED4yBrIHKw56W3qrwIj2JzD8jf5s5WYlFabjduWTtYx_gfNF6NshMyDDwfxfTaeIpTcESY2YYCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سعید عزت‌اللهی در رتبه اول مشترک با پدری در بیشترین قطع توپ در دور دوم مرحله گروهی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/662931" target="_blank">📅 17:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662929">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53f14fb2f9.mp4?token=Gzho-6yEXZ7pqmoavm2XFu2E4icFPQXapFs7VCIXVh692R_mRmiZnp76EHRhTnyjt4UbN-H1n6hvIoPGSVUag0NVt8As70hsFS7lhzqDw9Mxss1vuY_rYiWvYGdPyPsvY9O3Ql7TzNP1PCrfp2BSTZP-2fiREztmaD8S-MHOfP2sHPHxYZypZVpT5OdIbPtf_2IyGWYEZ1Mu2v60k4ZnjMcKaWLzMHnr1cuUd03UAYl52FgHUaISIpjv94D_tf7E6tKAaZlNViz_wvFTKk4oS8cRl-2R4vU8FHwfKcW_LuDTyIy7YH8dsPiBMTx9We0xnNc5r31aL-8iOJ0dQMlKlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53f14fb2f9.mp4?token=Gzho-6yEXZ7pqmoavm2XFu2E4icFPQXapFs7VCIXVh692R_mRmiZnp76EHRhTnyjt4UbN-H1n6hvIoPGSVUag0NVt8As70hsFS7lhzqDw9Mxss1vuY_rYiWvYGdPyPsvY9O3Ql7TzNP1PCrfp2BSTZP-2fiREztmaD8S-MHOfP2sHPHxYZypZVpT5OdIbPtf_2IyGWYEZ1Mu2v60k4ZnjMcKaWLzMHnr1cuUd03UAYl52FgHUaISIpjv94D_tf7E6tKAaZlNViz_wvFTKk4oS8cRl-2R4vU8FHwfKcW_LuDTyIy7YH8dsPiBMTx9We0xnNc5r31aL-8iOJ0dQMlKlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
عزاداری حسینی در شهر دنهاخ هلند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/662929" target="_blank">📅 17:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662926">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c756e008b5.mp4?token=jDHbJUG8DXONdaLLGO5IdWNWwHHfyAnhZT_9nSaq98jh9jthAWovjEzxYO004dSJTsraKuZe24DUK_ue9utvz3dVUs0Bw6BBoLn4MUU-ekmWzTyTCQ-iB8Pd_5EcbURiuCGH6K_1UXVI0SdF-Nn4Cw7gjY3XsRakyanOHU3VslPI9c4VQnJ3SOl6Fzgeh5cfmyHkH2Y09w7vKcfQ_FFkFc986Po4cLGGvD5F3Rq5_YZNEdrZIbEdjelCmrZ8fbFTanPPzbNptVraOK2DaLPJpoRPfJw2LO2ULobukkjZt0PQtHoLI7BbvL0BXSE0km8C0qugwij0XfUBVXHsfwpKWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c756e008b5.mp4?token=jDHbJUG8DXONdaLLGO5IdWNWwHHfyAnhZT_9nSaq98jh9jthAWovjEzxYO004dSJTsraKuZe24DUK_ue9utvz3dVUs0Bw6BBoLn4MUU-ekmWzTyTCQ-iB8Pd_5EcbURiuCGH6K_1UXVI0SdF-Nn4Cw7gjY3XsRakyanOHU3VslPI9c4VQnJ3SOl6Fzgeh5cfmyHkH2Y09w7vKcfQ_FFkFc986Po4cLGGvD5F3Rq5_YZNEdrZIbEdjelCmrZ8fbFTanPPzbNptVraOK2DaLPJpoRPfJw2LO2ULobukkjZt0PQtHoLI7BbvL0BXSE0km8C0qugwij0XfUBVXHsfwpKWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
شور عزاداری محرم حسینی در شهر سماوه عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/662926" target="_blank">📅 17:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662922">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7TmOGl_74BohrtKk_3JODZ_BwOGGswSGbNKjIYf7BJybx_r8HPTys45feasnZ0EB4ZCxPjPYIR31DXk0wCpP_iseiPEX6AbckpYWxrWyiWvVyHR0FEqLGVBwf1FvsGWBE3R7bTftTPgwH291mB7Nmo3hiidbMBwsHUJ0pZ-6D8g28rM8V23rXP9dGd-SZkmg3s2B1eXz2iijCHi-AzarZ8ri-NJ7P_LfL3UqrEaiwzFPXrf1REuxMQUDwoMOGbtEsmGdY40LNtGQDSCudm9m5ULapJ-txoMw1w8_5wz4qCfVNnaq_sJPnSPEBnQLwYDw9dojZN0vEYKZ2m7-afWFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
علیرضا بیرانوند در رتبه دوم بهترین دروازه‌‌بانان دور دوم مرحله گروهی جام‌جهانی
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/662922" target="_blank">📅 16:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662920">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0_n5ZAespYdVduYwkhUDfwZWKpYzpNwr9mk_OpZYySSLBCV7g8t-smHZy-zFuBllFuPTOxdXwNEJB1lM43YEVyYgH0ZNtli60yFT5u-HJXkxAFS4TGzqy9IFNAVvBSdDI5O27oZoagF0WU9O6PZjtHyq__UGvBd03ToLppzdc5OsULkkfbV_uvrRh-V1BJeURdrefCJBlcHreZt5e-BmkaMjczIaB4QGoJVNvpf19EdTjqKXQJnmqkcmxa2eGVApHZVJx7GQhuzNm75Qj0uzY5vUK5-iz6cEKId41wMRhTSOW0nnpR6pLimbvzFpVV86aU9uOP0MaNpxznl_mEQ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمهیدات حوزه حمل‌ونقل جاده‌ای در مسیرها و میعادگاه‌های وداع با قائد شهید امت
🔹
مدیرکل دفتر حمل‌ونقل مسافر سازمان راهداری و حمل‌ونقل جاده‌ای از آمادگی و مشارکت حداکثری ظرفیت ناوگان حمل‌ونقل مسافری جاده‌ای در مراسم تشییع و تدفین قائد شهید امت در شهرهای تهران، قم و مشهد خبر داد.
🔹
مرتضی اله‌یاری با اشاره به فعالیت ۵۶۰۰ دستگاه اتوبوس بین‌شهری با توان پیمایش بیش از ۳۵۰ کیلومتر در کشور، گفت: هماهنگی‌ها در خصوص برقراری سرویس‌های ثابت روزانه و اعزام ناوگان فوق‌العاده متناسب با حجم تقاضای سفرها صورت گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/662920" target="_blank">📅 16:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662919">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔹
شوک بزرگ برای جامعه اطلاعاتی آمریکا!
🔹
خلبان جنگنده F-۱۵ ساقط شده در ایران برای اولین‌بار فاش کرد
پهپادهای ایرانی با چینشی چون «عروس دریایی» و «سفینه فضایی» حرکت می‌کردند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/662919" target="_blank">📅 16:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662918">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXme25TbP7D8ZlOfjYpwaFR9qcmTookwjZlImQIEYAfb4_tfVr06r3ecfN3RzdvQ7KcA87RcOdkpYH5ivUZNqvk6aDgxYkXKZOEbjqBWnMMKJd4CYlKlljd6ALaPG3pWkHZRxsL_zeOwMbHQ4C153FX5K8PKWUIbcIatbFH5GOS8ftX4BaUlZEqtkRJ0FffmhVxSAajkIteqvB6l8KC8UKHMy9fknqn7JrA6gmZk92DCmNejjzddeunjbBGENLiz1z_lOJKf4PniFfRuFQ6yxKySnOZ6GkStzJA1lHt04vy3EA6JPhloZJji38COOY-qrikWcIxW6E69SRqZL7Fw5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هواپیمای پزشکیان با اسکورت ۶ جنگندۀ ارتش پاکستان وارد اسلام‌آباد شد
🔹
رئیس‌جمهور در بدو ورود با نخست‌وزیر پاکستان دیدار کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/662918" target="_blank">📅 16:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662917">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmmQgRrhq56iN2YCuaOSvmSU9jalxoM1jXWCQ2786CB8gRtnGrmivvUtDwjGXPvYay0qZHs1dtMHtocQ3GYOTDuJf4b-ur_SduSXFrJwcYQoZXhgk0GoiMyzIFg1cpe48GSY4dFNbYQTU2E3x7h4aWCYCsV0nFdQaYL5OfYuzL6lQw6wHkFYmZ9YaNhn8N3-RZFOvHsUMyMGBkLKs82vzfaYiZuZXefNavTyfR8b7OPIDLq-w7uqnvizVCyK5qCRLueCL3-AiLWPDW1NLjVB5W11Pxb2Kwxg7u95QDqgNYqfKebG7R76_ILpKsqrCwey8uH0qhpsKbhnAOCf5HCrVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
غول ۸۴ متری در جنگل‌های تایوان پیدا شد/ پیدا کردن سوزن در انبار کاه
🔹
پژوهشگران پس از بیش از یک دهه جست‌وجو، بلندترین درخت شناخته‌شده شرق آسیا را در جنگل‌های تایوان یافتند.
🔹
این درخت هزارساله با نام «شمشیر آسمانی رود داآن» ۸۴.۱ متر ارتفاع دارد و از یک ساختمان ۲۰ طبقه بلندتر است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/662917" target="_blank">📅 16:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662915">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7351a1ba79.mp4?token=ts4WntIcPnywDNEGLmzXuwB4LgtlICGJDik-gI9RzMBojikUPTYbWVgT3Qluw_YcnV4xvATlupNA8ciCgwiW5CDVDM1Wq4Pw2WjahiphSphd5h2cCZEAtKjRkfDlMpuEctsB7cEtt4BQVKLhrJ9kiahAZxJMqoicDh88ZenRO2U4FqR7K08auT-KSjP6Sod1yES17MOqHMlfIeQuvJgf4b08JlfVOW1PQlvTbPC9Xq7nGPDuyNXsRI5fj9m5VbpyhgYxkdljJH0axmA0cBrd_gIIl--wfeGAKhCTBcuY_a2_E2aw4m8SaFfup1VQHloWessV5TYXEEAtdOZAbXa6Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7351a1ba79.mp4?token=ts4WntIcPnywDNEGLmzXuwB4LgtlICGJDik-gI9RzMBojikUPTYbWVgT3Qluw_YcnV4xvATlupNA8ciCgwiW5CDVDM1Wq4Pw2WjahiphSphd5h2cCZEAtKjRkfDlMpuEctsB7cEtt4BQVKLhrJ9kiahAZxJMqoicDh88ZenRO2U4FqR7K08auT-KSjP6Sod1yES17MOqHMlfIeQuvJgf4b08JlfVOW1PQlvTbPC9Xq7nGPDuyNXsRI5fj9m5VbpyhgYxkdljJH0axmA0cBrd_gIIl--wfeGAKhCTBcuY_a2_E2aw4m8SaFfup1VQHloWessV5TYXEEAtdOZAbXa6Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گزارشگر: جورجیا ملونی، نخست‌وزیر ایتالیا اعلام کرد که سیگار را ترک کرده است
🔹
اردوغان: بسیار عالی است. کاش می‌توانستم مردم کشورم را نیز به ترک سیگار ترغیب کنم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/662915" target="_blank">📅 16:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662914">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OP2wh0t1G8XY3DMcwpv0oKPWsw4L0-AGVQTayDSNZyZEIV5-SrGgZk6PYCcYWFyMts2AhnKYVZuoX61qb7pqkKlM_3hymmewSIAGhBpgvKdBulp356ye31vo_8e8OLpA5v1QDJDd3_yFHJ2q-UgxBoayktE4Wrjuyyz1uZsFQFgHF53uvk08LHU6fH_A0IXdK6k2HPJnhsHJbCXoi78QLuD6rRkHR_JSgk15z2__OEy3cmMGXc035A_DuZWcrsaOAs0QfEg5gqR3EvUDWh8H7wUNI2fLYH17TD1C_obSjBPsOmmX6ej9assaQEHh9dMyLdiAyxeLOaGI_U0IjUZFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پوستر صفحه رسمی تیم ملی فوتبال ایران به مناسب یکصدمین بازی ملی علیرضا جهانبخش با پیراهن ایران
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/662914" target="_blank">📅 16:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662913">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
تیزر قسمت بیستم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای محمدحسن حکیمیان که از کودکی در کنار پدر مشغول به کار خیر و کمک‌رسانی به مستضعفین بوده است، در بزرگسالی در اثر تصادف روح از بدنشان جدا شده و علاوه بر رؤیت جایگاه اهل بیت، انسان‌هایی که به ظاهر مؤمن بوده ولی در برزخ تبدیل به حیوان شده بودند را درک کرده است، نظاره می کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: محمدحسن حکیمیان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/662913" target="_blank">📅 16:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662911">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f55b136970.mp4?token=JlRtoIcmG7lG0MLvIcfQ0sAZKR5wsd5LoUGvqzEcpgvBiSzooVeNP1qOUCoNQbigODRqcHDEsw09GFGORMgC7uohSyz53CqnEh-rLsQHHm4Y9gchsHzjTWxR6mEnPq5c4xALd41um0j1FHRhXD_EFYt-gNzJhkU5VAtGSWoSjQ46LfiNKu_HWoNZQ67OHl6SbbvCdCGJvUhQK3hqTIxHxzpR3x1IOJRa_dv_w_oJ0F6_ZtaQPg-OQQd4HXj7ag4H2Kc8Vx3cI5n6vdxgVXcNauXDdOdEbzOWy8tqBOq2WHMw70RHghl3mWGCTwWS2OJSkfuzvkDN3fimZ3PJxrEELA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f55b136970.mp4?token=JlRtoIcmG7lG0MLvIcfQ0sAZKR5wsd5LoUGvqzEcpgvBiSzooVeNP1qOUCoNQbigODRqcHDEsw09GFGORMgC7uohSyz53CqnEh-rLsQHHm4Y9gchsHzjTWxR6mEnPq5c4xALd41um0j1FHRhXD_EFYt-gNzJhkU5VAtGSWoSjQ46LfiNKu_HWoNZQ67OHl6SbbvCdCGJvUhQK3hqTIxHxzpR3x1IOJRa_dv_w_oJ0F6_ZtaQPg-OQQd4HXj7ag4H2Kc8Vx3cI5n6vdxgVXcNauXDdOdEbzOWy8tqBOq2WHMw70RHghl3mWGCTwWS2OJSkfuzvkDN3fimZ3PJxrEELA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
حمله پهپادی روسیه به زیرساخت‌های نیروهای مسلح اوکراین
🔹
وزارت دفاع روسیه با انتشار تصاویری اعلام کرد، نیروهای روسی زیرساخت‌های راه‌آهن و لوکوموتیوهایی که برای تحویل تجهیزات نظامی در منطقه خارکف استفاده می‌شدند را با پهپادهای «گران» هدف قرار داده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/662911" target="_blank">📅 15:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662908">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svls6kn_fPx462rchYJtAnAfxCi42Yn4UpKfHv_bWcC4f_p_C_HBZq2eT7188fK9Mwt4kpdGduoN4yesQyL4l2i9MB08FY4gHsA_wRUolTsbDFO_Ilz_rpd-gUCw4OsCYk5HvzzUUlMP3vuVQ6g0u1By3_wksThGJjxchG7dbUgVYEpkNGHfgQKj51MIXWoyLxeXn1wR84iwVw0Sle6YAKgqE1aKoB8IksXWqF_2XmXP9Cs-xu1QvJeNBNNGd9DFJmGHjDDf6FX-7fb7TT7l7MXFm_VZbIuB0qskrY6-nDWRctoK2jHyhsuJBtEnfMyEdzLYJcAY6UNaHYNExM7OSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پزشکیان: ایران و پاکستان در آرمان‌ها و امیدهای خود اشتراکات عمیقی دارند. تلاش بی‌دریغ پاکستان برای گسترش صلح در منطقه ریشه در فرهنگ غنی این کشور دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/662908" target="_blank">📅 15:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662904">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SFplrEhnaCaddp4LyI508mzMHrmHIJ9KVhgly98oUGt-f9JSgOSmjwmIMWKT5aCId-fHh2HaLNMUH3sgahgOpnpQhxLWWn0LJ1IPfzqUC5KVw_BFShzvI7dLN78f9FAEQxyzmWOQeXx36eu_jfI-n2QKdAGIZVUeLGdRz3ntNt8wXFAxysWap-gWfRvyJ9Ek7lDC84SfVxwvRxnnn32pO309T-y-MnGRqsRpf8rtmMXot1EvdJkKybVnmW9W_wb4qPRe3uuMTwZ6w0cE4SaKcKSxq0Fqxa0zgi8eX-GwMZX5icRQ47HXvWmuRXkY72bbMQbEA-ZD6yIIKPximsu7yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ne65JMYnt0NqJROJWhmoo4tbs-tFyurC9Aj3Wu-qm8qdSqJQg9dyY8KAwhpFUBNhrPPUDwM9TNqIFA-uFq6FprP8kqqDlUtYT1UKG_SLLjCalFX7IHgD6fE_BTWI3gDvHNwdUy1xfNu38AHDs9GmWvIizOFO-8mM83hXfHe6BfNpB0BxF8fQ96Q4xCZoOhp8WhGxZwB78hHNglVQZw7kD11bXZDEWIDMGdv6UoXYdxO8O9MzG4fCH5ehNGxxvzpm9eLYh_G8zD5KHoXMHC_JJl0WXZUyj1DnLjlisYxO-yZkQCoEVpI3KosOD_E7mDrxL-5GqQVHEJV_F9GLEbGtkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XvOYXGxDYPf38ft2H1-t66hWg__f5QTknp0lWfxqXrupWoIR3wy6uMlX9lPksgFF6B93VEOi8jZSnfhCMEMRJyUGW4NogdVic-OpFxUe4lYNbGIcIpXhgmC-51wKNDXe2KnW84cHxi3zxMd_nckkKMctIoidneBz6IaanVJDAwuFhwJuG0umj4UFGW0ri7YLK7q-kYHrzU1Z9JvcPHm9KUMXQuuG70zkrrK9ocWjQPNkICB2V7q4w3FWMIRWXPpl4fwzp7aQv12vGHwdkWP8LBYHtPmV9XBpivyCnnaHoCyd5y4_qY6uwNY17YefUwnBkPdwWp7bWLqvzE6k6FLACg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
عاشورا به روایت شعر و نقش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/662904" target="_blank">📅 15:30 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662903">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmYKHV6n-VlGP3eaeSKOLSbKnp6JcFGh7JvfI2GIsh8TTrMfugIj0H7lDjgfeO6BeGjIvKCZwT8tBaVtRqsGYyrOK3ksNDfnrbdNhGNh3-DJ9yHYa-Cha5RoGJYz1_IfsLnYUfUAz492MZQ5KQAvAfuD7b4QulIu3Zz-aBMWM7MGV7jb_TT5BdH6_eoqCxzV_P1KIiOg2-C5na_Db5H8gIbSx1wrRtAOjaDzqJfobVGky5rC3hxBh5vdfxB7yu9xh6B_NGc6ND87hvLpEybAi9hKXvAdY40gP0Z9fEu-et_O4xlG8mdT1t0QPwcemj9afVQwAb_QAZlFF_zMW8VVsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دیدار قالیباف، رئيس مجلس شورای اسلامی و الهام علی‌اف رئیس جمهور آذربایجان در باکو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/662903" target="_blank">📅 15:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662901">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NKIAn6VjByTuM_BO24UDdggxaBEwAutEzBdPHs3gddBGXP_eYQ6hwkYsu5zhXuWDHUfT_xwOIm71R0KkC4vPnM9EizD7Cgtkj-b3M8nRrp5We_aroVNmzK_Ygwf0x511BoFomtIc2JB_CuUUalX0mMvlSsVYOy8eNFwnbo0IPHbcgHUS4j0WTSLSe3l3OXwIDIeWvv_oyx_dFQOqzUGIsW81JF-uAsBkZUTgrH2x1iWLPd42r4_uHEmHw7IQQJb5iLKzcohzMM_j-qB7tkpkV7SqHj1P-vsM15F01YvcZ0o1DtUAOTHrfKE1lF1tn1LX6ZXABEVOeD_vUVnllwlQBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EC8m1Abr4XccD23Exvg1BgrZJDmQXfsUTzDVsS2GhmPLLF_2xbJ9-1ccBM7ysb25dNeYvY10lH7x900YdHLRekliatANFy06H_KbWiLbv4LIvSAM3LOBAelkeO2p8jb-ThP5R7ZuRltDHXooAfkFKp2Vz25VreeXl17hQdAwUGjztaSUdp5OR72vtc4_O-j3IzlQK1_xJ2VCrMP1HkecJNAPB4MapSRwC5P4t0TeoPEHsE8avni6b7qswkk5C1AJ3-wgJ_Opw5kLMHwBGJEenWXto-NDLCFZv709x2PBDxMfmLzivfkqqo8mhDY6Vo-_911Wvi73ZqxhySUB0TVnxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
پس از پیروزی پرگل ۵ بر صفر شب گذشته پرتغال مقابل ازبکستان در جام جهانی ۲۰۲۶، پست اینستاگرامی رونالدو بعد از گل اول او  به ازبکستان تنها در ۸ دقیقه ۲ میلیون لایک گرفت
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/662901" target="_blank">📅 15:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662900">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHn2jmBQD0y8yYu9X3rc6V97ifPZiU_MwQHrATnqdwn6vqXbjWr6LvAa8NoMyZVjKKrnpVVd0ebDdpwqF34gbM5UmBmV7ucDctgJLrfKgLIQ77VnzvBOuq4WJ4DaijfiuqggvGPDzU5PJ6PuWBvB4MqhrOygGEIrEtdGGs0glKSUvP9LonFfuXZik5SQZ_XRrZOEZd84p2GS_V1j1BbrlbiaWnrEDwdeO-sDbKjyO1FX8gtR0quNkQi-k-gt_NUGMXHftkJF-KsrZnLpoWh2Fmd3YzO0Xgzj4IoYAZKsovBAYMVnImSmiWo-zlA7a2rlhqQ8qHrm9XYv6YSqjtxmZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روز هشتم محرم؛ اوج تشنگی و استقامت در کربلا
🔹
هشتم محرم در تاریخ عاشورا، روز تشدید عطش در خیمه‌های امام حسین(ع) و افزایش فشار محاصره دشمن است. در این شرایط دشوار، یاران امام بر عهد و پیمان خود استوار ماندند و با پایداری در برابر سختی‌ها، جلوه‌ای ماندگار…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/662900" target="_blank">📅 15:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662899">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOwEjl2Y_qmUP2Aai09_yNGoGl9o-qDAuWpEXM_4Tm1xllbNqJhkGfXNf76LI2iaysYeNwRMWEhf3tjkuL8k1jlEe0YAwtfURWf1U6eTsH-QOsLGmSSCDcG-IkHHmo-oXVDpj1ja4n0A6ECcHKmPghGd1fnBtxLG3RVEnfVO77n5f7oF0Hq3CJBZr13iTmKm1qVYcoKqEhsjMvbVQKTYCZiJtMUzdKhLTMJkahRk7QOcI-brVc7M6hm5PBwoPD3Xfo54WexfFCIIJXaldhY58Si9poE6J1kUi-coFMkr-sDYueVOG3bAqJJIMi-07LEolxzPSi4A1zJEekBNilRTCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
ادعای ترامپ قمارباز: ایران به آمریکا اطلاع داده است که برای عبور از تنگه هرمز نیازی به پرداخت هزینه نیست
🔹
هیچ پولی به ایران منتقل نشده و از منابع مالی آن‌ها برای خرید محصولات کشاورزی آمریکا جهت ارسال به ایران استفاده خواهد شد.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/662899" target="_blank">📅 15:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662898">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔹
آخرین اخبار و حواشی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/662898" target="_blank">📅 15:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662897">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qf4c6U_PkWLNM6PLESQAryTiuE-G78p998QxGHzXMMUY980CVMoKGdlAfPlnxgCcD1sMqKD--BrKAei9WIU09EjLTlaZIBk5h7qzWHF77Rl0ZfzRRmzygVc2OJGbEvZa3Kpx5hqJVRijQFkbOB63UZ1tt4uADXAzrRfkraLazix-zGo9Zz1zBil0yT-G8ncoboosaG7HN-SU4C8iTewxP_Ny8CKNcZUe9K-icQZHWwK20b5XLBSGXejGRxCcs2XpH_stXfH51BAUoKMoZZ-GU9y3x183NngbxAIijm_QDQrj-il_Vj1IQUfla6IGPgDkV8YhOmjW3zTjk1V4EPZhdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تصویر پربازدید وزیر میراث فرهنگی در مصاحبه با خبرنگار روزنامه اسپانیایی روزنامه  Diario AS
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/662897" target="_blank">📅 15:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662896">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgFoljY4Yd5ZbH7428NDs4R4Ux9wWolbH8c-5lp3zi8MD2uZ7_Sli3oAk6yi-RkbMk3n_fjBCGvLTGL0ZvFxA3YSV3W1OtbTgdvUMsHvqwVEQvj5OhT7OOeT99IruqqLwUB3xTAVQJUtbi9E97X9PNPtaR4tevGsAMToUU-IqPMGBtCPq3OmaHtaVwcuAcPjAk7FI4IfeCjSgoTJK4r_jivhGo58O5dqjQuJoUdYQZVQohe1tNeIPLjmoLjvTzj34FKyvoLXbjOaYZnzwB_JEtVtmmFyqyfuvLeK0yYuIKD0GksZvk38rgWbNTXQKjaeu0eULL-Ob5ehXvZ-iNxuGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیر تحول مناسک محرم در طول تاریخ
🔸
رسمیت یافتن و گسترش آیین‌های شیعی به دوره صفویه برمی‌گردد، در حالی که تثبیت هنرهایی مثل تعزیه در دوره قاجار رخ داده است.
🔸
در دوره پس از انقلاب ۱۳۵۷، آیین‌های محرم با گسترش چشمگیر در فضاهای شهری و بسترهای رسانه‌ای و دیجیتال همراه شده‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/662896" target="_blank">📅 15:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662895">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iULYiy0AzCInBbt6dWhymo6s8KFms9iTP0WygbGyuh_5fnqJ23dqptdMsY_5ydoww2ko2WJuTN4WJZoUO1DxylfqNZkF2GeEJ2pq-9PuSy9ftkjwey_oy-4PchwodVUl4o0ZbLhLFjSWX1U_rMozMYeuawJRcVYnIlCkYZXwuel1SdjNXbTHgePtAkJA5wPRqMQb1o6k6fTP0v8Bpz6WEA9zbrAleBhUn3mW9eSDD4RLGLMEbmZX7Ujvjl98eN9ZD7NHMFG9hcoaLh5brwihXYx8LmMvvyaWnxM7Da3kaMXqwxRBaKzvTeq2Vaclvs4ptMRfSdG3q5tAR1hSpd50ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥀
بلند مرتبه سقا ز صدر زین افتاد
برای آن یلِ بالا بلند، گریه کنید
غم برادرِ اربابمان کمرشکن است
کمک کنید به آقا، بلند گریه کنید .
@Heyate_gharar</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/662895" target="_blank">📅 15:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662894">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔹
گزارش‌های تازه از وضعیت تردد کشتی‌ها در تنگه هرمز
🔹
بر اساس داده‌های مانیتورینگ دریایی، دیروز (سه‌شنبه) ۲۵ کشتی از تنگه هرمز عبور کردند؛ همچنین خبرگزاری رویترز اعلام کرد که در ۱۲ ساعت گذشته ۲ کشتی باری از این مسیر عبور کرده‌اند و هم‌اکنون ۳۵ کشتی تجاری دیگر در حال آماده‌سازی برای عبور از تنگه هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/662894" target="_blank">📅 15:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662893">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffB2H6sJFfEJtfAqxhcSqm8dFgvbq1C5oZAWoQDn7QaEN3AND1YLjig8B0nk-F9uNYkobcCNL2LZ0rTRHRHT_jrTouxC5g_pbVWqkQlpudI9j-ip7GlPJ_I_5qLw1seZbVuZElK5fa48EPanIc5tqF_Pf-hxokMPWRPKQxzq2STnB3WrmP8spqMhYmE-fn8n2RS3ZPN_LcpRa1Y4cNdy51e0x0NTOf2wrEqbvwGYt48fm7PsIpw94bCHdBEXQ8hho1FvR6aBCm4M-YHNA3vLnCqIJtN_6FizooPEgfQhPlRHA0rtIlSefWNEA5kQ44iPuDncfEvM8-gciEDtqHYQ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
رفع اختلال اکثر بانک‌ها؛ استمرار مشکل جزئی در بانک ملی
🔹
داده‌های اتاق مانیتورینگ شبکه بانکی حاکی از بازگشت اکثر بانک‌ها به چرخه خدمات‌دهی و پایداری وضعیت از صبح امروز است؛ با این حال، بررسی نمودارها نشان می‌دهد که اختلال در خدمات بانک ملی هنوز به‌طور کامل برطرف نشده و همچنان با مشکل جزئی مواجه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/662893" target="_blank">📅 14:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662890">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔹
همتی: تخصیص ارز برای واردات از شنبه افزایش می‌یابد
رئیس‌کل بانک مرکزی:
🔹
با بهبود دسترسی به منابع ارزی ناشی از رفع محدودیت‌های صادرات نفت، از شنبه آینده تخصیص و تأمین ارز به‌طور محسوسی افزایش خواهد یافت.
🔹
در اولین گام، ۲ میلیارد دلار برای تأمین نیازهای تولید و کالاهای اساسی تخصیص می‌یابد تا با کاهش فشار وارداتی، به کنترل قیمت‌ها و تورم کمک شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/662890" target="_blank">📅 14:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662887">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d794686604.mp4?token=cDEbrYOvzRWty_zHzmNQQHyoygItK8O7SNIbE3qV5Kjn7bhX9nRrl58fJE5Xp0L0G3PkCMeijvIgNnTULtTxKtDy0R8sLr7eoeUHFKDUQxO5mBLRaCSNieCuQ69mb7rXRGzsxhzfSLgmg-OCSYR_Vg8xsA0D4NDhMVMvmUIWEC3_ROfXSXHwYKoz904QzoNxvRXvxYcl_H7SUUklb3-zKhA1vdC1ykXJw_yEogno5I8-ytPaLqzAMXaHrfJC5zKFNtqYZWofvPp5k5FkOT_wkdxBRheEkdWJvI1y90u2LU2nEWxeqv8svEkaZPUHIOxs-bbePfdavcaM_iB2LTmnAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d794686604.mp4?token=cDEbrYOvzRWty_zHzmNQQHyoygItK8O7SNIbE3qV5Kjn7bhX9nRrl58fJE5Xp0L0G3PkCMeijvIgNnTULtTxKtDy0R8sLr7eoeUHFKDUQxO5mBLRaCSNieCuQ69mb7rXRGzsxhzfSLgmg-OCSYR_Vg8xsA0D4NDhMVMvmUIWEC3_ROfXSXHwYKoz904QzoNxvRXvxYcl_H7SUUklb3-zKhA1vdC1ykXJw_yEogno5I8-ytPaLqzAMXaHrfJC5zKFNtqYZWofvPp5k5FkOT_wkdxBRheEkdWJvI1y90u2LU2nEWxeqv8svEkaZPUHIOxs-bbePfdavcaM_iB2LTmnAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
بازداشت ۲۵ نفر در پی تنش میان زائران در کربلا
🔹
در پی بروز درگیری لفظی میان گروهی از زائران ایرانی و کاروان اسماعیلیه(شیعیان شش امامی) در کربلا، پلیس عراق با مداخله برای جلوگیری از نزاع فیزیکی، ۲۵ تبعه خارجی را به اتهام ایجاد این درگیری بازداشت کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/662887" target="_blank">📅 14:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662886">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9482fe2fd.mp4?token=mWfOasXF7YvztF4R0xeEyw-cZvMZ2PIpv7WlyMBV-CH1FfH9D8L3qMUW8ST3RbbYDRYzgeazGu4P2sj8Ir4NjX2tN-imErDbMcisllFbmY-8jmKg2CUSRjhhXJdnIELL25WqO6SCVAZuVacj6gRLQ90uC_KDByt9yVtj7DiIbcfREHRpUJ76KxA0Si2AGVvOOIGb0UUurNlWaWJ4dW38lLBVu2CXwWObjGcQW3dbVfbqnpplpv962PxoA8eThSsIuooV5y7-4-6kachUUEAl2qboaM-rNMf_jheZjFM7PJiNU5Of_vF57CATdZUr-VefA3qIOmfTthwC4TidU58tjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9482fe2fd.mp4?token=mWfOasXF7YvztF4R0xeEyw-cZvMZ2PIpv7WlyMBV-CH1FfH9D8L3qMUW8ST3RbbYDRYzgeazGu4P2sj8Ir4NjX2tN-imErDbMcisllFbmY-8jmKg2CUSRjhhXJdnIELL25WqO6SCVAZuVacj6gRLQ90uC_KDByt9yVtj7DiIbcfREHRpUJ76KxA0Si2AGVvOOIGb0UUurNlWaWJ4dW38lLBVu2CXwWObjGcQW3dbVfbqnpplpv962PxoA8eThSsIuooV5y7-4-6kachUUEAl2qboaM-rNMf_jheZjFM7PJiNU5Of_vF57CATdZUr-VefA3qIOmfTthwC4TidU58tjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
اهدای دکترای افتخاری جراحی قلب به پزشکیان توسط پاکستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/662886" target="_blank">📅 14:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662885">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔹
گلباران ازبکستان توسط رونالدو و پرتغال؛ تاریخ‌سازی کریس در شب درخشان
⬛️
🇵🇹
5️⃣
🏆
0️⃣
🇺🇿
⬛️
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/662885" target="_blank">📅 14:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662883">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e6fab5a33.mp4?token=PLByW1VF-KwF-0h7j7LhGWQVycXWKCqTbrWPLDlG3dUKim9KX-lBInpCG0fwgonsJbMqEc_xCEBQ0_0hcULpuaWqcP0N1hJuil_dvWC4uDwZTD4o0rHGbYBdin-NqD4CC_t04enDubqEXVpeFf0Tnn0P-Nr8rqquwTIRic1hGDjIsCwX_U80IRlbFDRlfOkBcHsAvOfUL6eTUSz0SKAnhY0BM9d2rkqKL62wWwW9SmMYivqrAsmIGbJuZXftjFz7_yXgYXsHfJn4vOOwl5JWW64rPoOOAgNzlbbvCy8hKJMKlscOhGDNoj3ibzJQZAptgtibniO4upk46Tgil-KZdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e6fab5a33.mp4?token=PLByW1VF-KwF-0h7j7LhGWQVycXWKCqTbrWPLDlG3dUKim9KX-lBInpCG0fwgonsJbMqEc_xCEBQ0_0hcULpuaWqcP0N1hJuil_dvWC4uDwZTD4o0rHGbYBdin-NqD4CC_t04enDubqEXVpeFf0Tnn0P-Nr8rqquwTIRic1hGDjIsCwX_U80IRlbFDRlfOkBcHsAvOfUL6eTUSz0SKAnhY0BM9d2rkqKL62wWwW9SmMYivqrAsmIGbJuZXftjFz7_yXgYXsHfJn4vOOwl5JWW64rPoOOAgNzlbbvCy8hKJMKlscOhGDNoj3ibzJQZAptgtibniO4upk46Tgil-KZdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
السَّلامُ عَلَیْکَ یا اَبَاالْفَضْلِ الْعَبّاسَ بْنَ اَمیرِالْمُؤْمِنینَ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/662883" target="_blank">📅 14:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662882">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔹
غنا سد راه سه‌شیرها شد؛ تساوی بدون گل در بازی حساس
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/662882" target="_blank">📅 13:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662881">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APRLPracuA236RzkmszpSpB0qNUH979kKtwEBq35GYKpD2fALb465IEF1LpSI9-sazkV_T1L5Z6E1hq-QfDIwYrvsMS3lhxJbBARehMsfrvWIUU7fRhdZB6yeFxvdstI496MNJ4fGH3IV7_eWH81Jxl2lgpgYG_iNv5XJzhKGlNC89lFxLzHjJUGUHHRoNKjxlf8Wam-JolE92ZDOQj-1N_-H8eAyPJOgiI06boVFc7lHPvkYfLXijuZgsUXFNgo5lF7mtsil-k514zPsyuY_YZ-PqlsRdrzLScqQh2HQP2cNt3mtp_BQhN9eluS_mQcGojPcnxfGQlzVO4JmBzLRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
قطر به دنبال مذاکرات منطقه‌ای درباره تنگه هرمز
رویترز به نقل از منابع منطقه‌ای:
🔹
نخست‌وزیر قطر در مسقط در حال رایزنی برای برگزاری گفت‌وگوهایی میان ایران، کشورهای عضو شورای همکاری خلیج فارس و عراق درباره وضعیت تنگه هرمز است؛ همچنین تأکید شده که این مذاکرات منطقه‌ای از مذاکرات ایران و آمریکا کاملاً مجزا است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/662881" target="_blank">📅 13:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662879">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aca3d8385.mp4?token=tIRuLZQXQENK1i-EhXGk1DqGb_sOT5FABJ4TB5FQKNDVdGWMKGcGXRIEunH3Vt6LYcOKsyKBpTIlbOZbv_iGjNoR9Dhp5FGIanAmdKuSpO103UNbrcgXPJnAUedcOTnRPj3cS1zrdbagswuGRqY_JsiveBS-EV75HkSQHPWFeHCGG_Ry7QykePYG0SNdgF9y-ILyiRUj43OORRChiBTk8hePgGGm3sPcnLce9w_uCU02-8a050NLEjPdqocP6z6y5dhBU7bTlFond8SsxZDW3D_xzHmeCXSycuUDndI50BLAbjcxLx1DUIqPT9uK6dqG288vHOWjT3AVQ-oC-bvt7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aca3d8385.mp4?token=tIRuLZQXQENK1i-EhXGk1DqGb_sOT5FABJ4TB5FQKNDVdGWMKGcGXRIEunH3Vt6LYcOKsyKBpTIlbOZbv_iGjNoR9Dhp5FGIanAmdKuSpO103UNbrcgXPJnAUedcOTnRPj3cS1zrdbagswuGRqY_JsiveBS-EV75HkSQHPWFeHCGG_Ry7QykePYG0SNdgF9y-ILyiRUj43OORRChiBTk8hePgGGm3sPcnLce9w_uCU02-8a050NLEjPdqocP6z6y5dhBU7bTlFond8SsxZDW3D_xzHmeCXSycuUDndI50BLAbjcxLx1DUIqPT9uK6dqG288vHOWjT3AVQ-oC-bvt7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
کیم: ناوهای ۱۰ هزار تنی با سلاح هسته‌ای به آب می‌اندازیم
🔹
رئیس کره شمالی، از برنامه خود برای تجهیز نیروی دریایی این کشور به سلاح‌های هسته‌ای و ساخت ناوهای جنگی ۱۰ هزار تنی، رونمایی کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/662879" target="_blank">📅 13:44 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662877">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a3616b819.mp4?token=YiNKSpT5KKU_E4RsA-h_0ndsM2g1MOXFLBPU3hq0u4-LEDrxarjBTCAvet9erwJmkyc4YnacFYOGPhvTFH2xywD7bdqhyV5HMCfGvtkQvIZyXnQf9-RPOmlQrrFAUZibgQyZvM7sAn1lP33EtOL34oQe0s_ONwCxMQf9hFU_3qxKwxjcqb_6wr9b6eWT15IqF3ChhALmGutFjC-2Rw4s1UULSzChO3eR7FDgdNpNWxVFkaCnDFS_O9_X6p4eTTskFqOjkwgKdEEnYJnNPVMbL-GT-mhj-qbsrRddshdgPdj4qJikhFjIUTHGq_ELBmk-673fYIOY-cc_PAtwZVkBzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a3616b819.mp4?token=YiNKSpT5KKU_E4RsA-h_0ndsM2g1MOXFLBPU3hq0u4-LEDrxarjBTCAvet9erwJmkyc4YnacFYOGPhvTFH2xywD7bdqhyV5HMCfGvtkQvIZyXnQf9-RPOmlQrrFAUZibgQyZvM7sAn1lP33EtOL34oQe0s_ONwCxMQf9hFU_3qxKwxjcqb_6wr9b6eWT15IqF3ChhALmGutFjC-2Rw4s1UULSzChO3eR7FDgdNpNWxVFkaCnDFS_O9_X6p4eTTskFqOjkwgKdEEnYJnNPVMbL-GT-mhj-qbsrRddshdgPdj4qJikhFjIUTHGq_ELBmk-673fYIOY-cc_PAtwZVkBzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
اظهارات تأمل‌برانگیز علی فروتن درباره کوچک‌تر شدن آرزوها و سنگین‌تر شدن بار زندگی، بازتاب گسترده‌ای در فضای مجازی داشته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/662877" target="_blank">📅 13:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662876">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔹
ادعای وزیر امور خارجه پاکستان: مذاکرات جاری میان واشنگتن و تهران بر سه موضوع اصلی شامل برنامه هسته‌ای، تعیین تکلیف دارایی‌های ایران و تحولات لبنان متمرکز است و تردد از تنگه هرمز بدون دریافت عوارض یا نیاز به مجوز انجام خواهد شد/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/662876" target="_blank">📅 13:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662875">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔹
انیمیشن شکار در تنگه
هیچ‌گاه از شما غافل نیستیم...
#WillPayThePrice
#تقاص_خواهید_داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/662875" target="_blank">📅 13:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662873">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEYBB91Q_mU5bCEaUdZyBSorV660XB2qw7BIcHWOG0ISaAWo3Kcs3Aycmp36uV5qpHbeQzt7R5sXdPqnHQYfHHe_He_BR3jChmiYhrYlyqDYQPDB6j3E6QAeXxAfOf8ksGE1Lrpw0Pe_MiMNJFhj09E9LkYlAa-Nu--a4uscbKXbO5OjaliT_fnoFE_ZTVwCfuKzanr8aARyq8oTEDmeCu55_sd9zEM2OXPsDlMea-l7GuLvvj-1ny6ysUE33hRtoYOGSg5HrZmu-_KRLxUdZTRNb7gBi9lank2PDrAMZlgRGMjy6lVbXWM5LHTKauRMVdi57PuG_KMTmouWwuvgQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
عاشورا به روایت شعر و نقش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/662873" target="_blank">📅 13:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662868">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگرافیک قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bb_wPAYeog2YMuSfuxE8Bj8HoQ9KCQ95VPYZ-nhhWiXKOzDAegDt3Smc4ah0-f5THZpoTsgN-un4V7ODL1rI6ZE7jH2ZO_l_0aNyixbIsi_OUleulTf6z9sMC2Beh315_6SLHL5LfBmdjy_Tas-pJUam5sw7Gm4pl91FVzX4or_1gqM2TfFm1dSNDJIt12qbSAcgWLq9AtbBn1GEzlpxhVX_OK6sOJ3hZFB0IcDKgLRr6mSgsrG0HYgrOT2hpSKHQ74IcaEW_cAGB9i3FbJGk2Rf_tf-c6Aqe-Lha1myw2DDa6QamTvlLU8U1u8RQECa2v0JcQTN2qvtcwU50bX0fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uxMGGyXx8Umi3zywforysokfKwZtp7NP8Wj8o3trvulh7ioFLiCAPyu2ReMQfJpp1aRNrKk8T2i7zM_Jwe1ZQTtKpKALMkdRK8xwecjUKtisWyjVHi7mojzkC91SgSRodSn5Fbvrs2bDpoz-ABhlZeTF0MIBCy-KBN8lZ_Vlh9oB4oqF1RfZ-qCiolTBDPODLt3RDsqXi-p4Hmv8MunMMLJ2tq24su6azoPuxuU-pXQ1WG9WegiZcn1SUaZquPA6D7Hz-E1jV9MBUNC-0tmaVHCzPERb7CkBMD3ZYyQdwEbNizV9jwz23I5PFeKoiyrGh9E-GdFBEVArof4Cfm-Y-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jHxbmTTjNDaEGPFe2nTE2ZOxqAGLwOrwz1moFbe9NCCan9ZXW9l234uO3deFqR056J07FOgVSRdOSkWM6X_1rg8ZTHBdYrTpSLJE_i3mR8kSyepZrhopBEW9RcEHKfOvgri7pmi-QWcV3WkwbwY5F8xQc1B2C0QTV2l-z5UOmm5iwPuCWQeIzEb3oPcqDkMhpa9v4C2C4z7RpbXNumY2567f-7YDpkOLF1es5ipf3PgPxl16es0biK2_9ZoJhfrZWtsEvXlUyyvGrF01AKXjim1XSFswa7RMryS8zXuDPIRfOHHtbNVdTkjw4jALN3LL2tyZPrGhE-L97W5GIvLBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GhBiJhnSxAc-vsp2JRwXyyZX2HtBHGMP0icxZtsTGMZVTqFMe26cezj4jNPHas1sXCzzjiJyzg7KMb6RYlcXBengVp_5zY164KqUaNLV9AjhDV1XLQ0eZpXc_bl99CuTxism0qOtbKixhG2kOGh4ISAgo1CjLR2uw0CGmidRwK86As4eqOsIbJRQHx0tDgf6MlIzQcB7xvGTYFWuU4wZxCahV403xK4NjbgsVyOpH_zT5SSe6o0Z5QSBnftOBDvKksarVLdgkPZc1VbtxReb2MJ88ygIHcEFqk3AFHWQqfx28ZW9tmecdi1xN53ufjgVPIRXnp3v_jrDOhZMSQ1taw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oytQj4AWp6xS9p3FVS7BC9qTSxTjRIkzJjryupLyzefmsLB0PQgE2EGKYFLrr25IDdtu5BeoNILxMPlD_3OHfzECg91QhcAsn2uHCb7kp97mu9sveVpxW-a-KOzfXw0O_JO--TjNYTpsTdtU6Rf-wOfswvEykEoaXZ-cGzslzUmtVHXXtvOuB88a_CKuwhDaqWafkaj9EFv0KC3llscIDlAKKQLfS0eE3I4R78HbBgkKMi0CZvFQ9PoEINkDsutZ8k_FZdOXgC6hrxQRV9x2Ctlw54LNJELFO--gIozkw_fxumI---unQcj2N8SX7wElHvF9OfGO5Ez-JZ-8wNpdgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖤
#تاسوعا
یعنی دلدادگی علمدار،
یعنی وفاداری تا پای جان،
حتی بدون امان‌نامه.
#محرم
#اباالفضل
علیه‌السلام
#پروفایل
#تصویر_زمینه
گرافیک های خاص مذهبی را در این کانال دنبال کنید
👇🏻
👇🏻
@gerafic_gharar</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/662868" target="_blank">📅 12:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662865">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7nZEG9EqEQsZ5i0OcAi7JQgBwSGvwEoruxDz3cVG_zA7fq-3XlxhIFHbd9oiHspnk3o0maVWQp56qE0QtI_WCd2qCU0bB7TXG_sF7NCImR22v318nsMoEGm0pY1hb386L7vDQgmKo_mAcxhNFj__SzQRJ701kCrXE_LzX2mG5p-8_Ft4Pv-ucDEpwYXvYFWV6Sdcc3voK7IAbBdr5fZIHocQlO-DZzUnrT2_tzsni13oIH6L9EkWBEctbUQCcVE66EbdsumktUVeq4vtafXGy9JIBLVMRLw4ORQ487Ju7xTUiI3n8ULr7EDipwAv8fsiSJVoP7xc8xCpuXJa9E6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
راز آبی که سر به زیر، گردِ عباس(ع) می‌چرخد...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/662865" target="_blank">📅 12:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662864">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSMJ6GjzWHkXs0AgYveVnFF-3AT-Zd38YoKUeHhFKldc-woa8Dgi0lhtwIudFZWDgCMn328_F42knZzyWIUdE6RpDM3Hb4tzlvx0P0X5KTuI6CenWevzXzP98Z-B05oRgwVkoAgM43fWKoC9P4vMF14fMeweGOrgAoXEzMcYoCyHmEEoU9Ig-_vnFuv42-h-tDEW9W0ufdmIQM52WCLnvVYlPiuqkMKpcMaWHyKyaND4FangCN5yncmx5PnPmWasf6nMToD4lx3tS72lI6PMR5JaORdsqZY_RRTukurak6L1GmDoP7N_MfsydVfoq7J45A84Glw_9lHS6fibZRn-xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راه حسینی
🔹
مخاطبین عزیز خبرفوری؛ هر قدمی به نیت سیدالشهدا (ع) ارزشمند است. با ارسال یک پیام صوتی حداکثر ۲۰ ثانیه ای به ما بگویید که امسال به عشق امام حسین (ع) چه کاری انجام می‌دهید.
🔸
لطفا در ابتدای ویس نام و نام شهرتون رو بگویید.
🔸
پیام های صوتی خود را با ما به اشتراک بگذارید
👇
#ایران_حسینی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/662864" target="_blank">📅 12:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662863">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiXReMSjJ-dXCYPHLHeEpCWAO663MEf9Uc2x9Y2RE60sh-onYm67kgPi7C0wKPrQvvU_6yK81wALiysSiYRI2eQo5QoOdHGtXz4CQQvXwwM_i8zHZbKUGHfelMDZ7TZ4G-P8o-k6pmQL0uW5uOQhogZnA8bQg7gPS35nxtUp6bGspOLjDJzM9yfHmmxIk9qQI1vlQ-SbGvnjFX73mXsN9I4EdR_TqybJNqlCTJG8aRW_eFaZK5EQuBmLcII_jgzr9JEvBu9-WdNpOaOx7202-hUL9NclWgxqIUCx3kk8stthqyatA0GPtzXuVb8KzbtW_BlHTeTuwzQR7c4v37nyjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
احتمال صعود‌ تیم‌ها در گروه G جام‌جهانی۲۰۲۶
🔹
شانس صعود ایران ۶۰ درصد.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/662863" target="_blank">📅 12:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662862">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYwp-dnpJpap_gn8FLOs1CyPvasUKuGQ7bKjdUmbNt-5XIkGP78DLVwN_PfbCNdDSj9WPrU1l-ReutwLF5b-bAqlfIhkjLwQYyCJn3EavY5eLNnhlrf02swohw2Amn32YJ0gD1XcPbRzqx6Kq6cVbQSszZsaRISRVqxlCTBdao78z6mh1Lx3NWwXYG32g6FHVretlVWxZMPq2M5fh3aEbfcygt6OlIa7yVwshfsHpAqapDGP61-WDpmz-PVb-VkleU_jWAxzZ_iOl4oY1sdqJZrOoVk4PJUKMu0LY4KDq3mJqL2xD2FY-j6CHO-5Qs0fGtbzCQJfxXXcA1jNMhEcrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
نامه حمایتی و احساسی یک هوادار مکزیکی به تیم ملی ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/662862" target="_blank">📅 12:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662861">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔹
اعمال محدودیت‌های گسترده پروازی در تهران و مشهد همزمان با مراسم تشییع
شرکت فرودگاه‌های کشور:
🔹
همزمان با مراسم تشییع پیکر رهبر شهید، پروازهای فرودگاه مهرآباد در روزهای ۱۲ و ۱۵ تیرماه متوقف و در سایر روزها تا ۱۷ تیرماه با محدودیت همراه خواهد بود؛ همچنین فرودگاه مشهد در ۱۸ تیرماه تعطیل و در ۱۷ تیرماه با محدودیت فعالیت می‌کند.
🔹
از مسافران خواسته شده پیش از حرکت، وضعیت پرواز خود را استعلام کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/662861" target="_blank">📅 12:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662860">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔹
ماجرای شهادت حضرت عباس(علیه‌السلام) به روایت رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/662860" target="_blank">📅 12:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662859">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080e5ecb9a.mp4?token=RT3OFHNCJe0OD45jG9FWiFVlCHE0tV0RR7t6ktFMHgLWPKoI5-gE5yO4ZihNX9nW8sEmRvm6laVk5Ph8cD-I2yzEvmWULXJdeUEVB8sVhYFkjE0WAnsvv6ygWPeH8bshS2RDyAR_UXFCkRWYDULgwNSok7x8Nxtqj5BZ4GHb_Howgt2_5Vs1ye2bbT4KxnmEbR-MnyWX7zeeTEHC5YbWSLwnWUwRxfMdGYxL1n2kb7T_zAcMHnIis_BT9ZBpabLlp1Jzmu93xXnyuYsmzYgduChxpZi2atb28sBYoq85AUYyLAm30fFI4kHBuocqYjCXc6bfX3xzNpYSmOobP47-AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080e5ecb9a.mp4?token=RT3OFHNCJe0OD45jG9FWiFVlCHE0tV0RR7t6ktFMHgLWPKoI5-gE5yO4ZihNX9nW8sEmRvm6laVk5Ph8cD-I2yzEvmWULXJdeUEVB8sVhYFkjE0WAnsvv6ygWPeH8bshS2RDyAR_UXFCkRWYDULgwNSok7x8Nxtqj5BZ4GHb_Howgt2_5Vs1ye2bbT4KxnmEbR-MnyWX7zeeTEHC5YbWSLwnWUwRxfMdGYxL1n2kb7T_zAcMHnIis_BT9ZBpabLlp1Jzmu93xXnyuYsmzYgduChxpZi2atb28sBYoq85AUYyLAm30fFI4kHBuocqYjCXc6bfX3xzNpYSmOobP47-AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ویدئو پربازدید در فضای مجازی از چپ کردن یک پراید در سرعت بسیار پایین در نیشابور
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/662859" target="_blank">📅 12:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662858">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔹
تصاویری از حال و هوای کربلای معلی همزمان با روز تاسوعای حسینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/662858" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662856">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gks8EbHRDe35eH3Oru-J95TOCBA_sUeD3s0V76bC8KJtDJpKbC2I1gLpm7HiXTc5SILvMpMGgGKzrRsWbOO1pqgxuYg-arRITavN8V7pb-z4ZekU-lbLJDlTkok-VobK5GwQo3R1r0H6QKUp1jiauamJDuMbtNIH5q4qaPKmVuiFuti7W4XtCqIZPCvwgUZkRiyzdzppNL0BwMKHmoA74cQpxqoVYKTCA5W3aI7inShadmBhw2m5NCYtzAfTKMzR1M1QAGH5r0i0MX7fjeUAv2x481jUE4vTTiYoKnGhcYQndwXjTSxPGPYicZ2yjzzwM9Y7IdV2TCTbETYjH2NIcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
نتایج تیم‌های آسیایی بعد از پایان دور دوم مرحله گروهی جام‌جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/662856" target="_blank">📅 11:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662854">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c2df765cb.mp4?token=E0lb5XSTp6_ulqI8QbiMiwytrsFgUH7_ilGlca_Uv7TFWOTe2V53-3ZWITqN-3oKUyAcwXt4w2xNy5qzq5DQbgcqldLqx_BABqcUkTEHCtpKiLTX6v91tIGUMPNUrRyOb143I7-LEI7ff_CHIpKpfjxrhYg_D30qB-fINj5D3fvB91HpJzb2s3Bo4ep3RK6cLshGkQxOVpdeKpclVIiU7ptdD3Hr6C6Q91WlI8JRT6Eyf58hMCyk03_dm1rzL7yQ6jR2wBn-UBy4JTqmGIGOPs0m9WUnF4dOn_4CNaAaane_7ivaDNsIAMwejYn69A9BY17j1qfoD4bHHuOMv0a1bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c2df765cb.mp4?token=E0lb5XSTp6_ulqI8QbiMiwytrsFgUH7_ilGlca_Uv7TFWOTe2V53-3ZWITqN-3oKUyAcwXt4w2xNy5qzq5DQbgcqldLqx_BABqcUkTEHCtpKiLTX6v91tIGUMPNUrRyOb143I7-LEI7ff_CHIpKpfjxrhYg_D30qB-fINj5D3fvB91HpJzb2s3Bo4ep3RK6cLshGkQxOVpdeKpclVIiU7ptdD3Hr6C6Q91WlI8JRT6Eyf58hMCyk03_dm1rzL7yQ6jR2wBn-UBy4JTqmGIGOPs0m9WUnF4dOn_4CNaAaane_7ivaDNsIAMwejYn69A9BY17j1qfoD4bHHuOMv0a1bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کل دادگستری هرمزگان: متاسفانه موشک دشمن جنایتکار آمریکایی - صهیونی مستقیما به پیکر شهید ماکان نصیری برخورد کرده است  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/662854" target="_blank">📅 11:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662853">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b38aa3fa.mp4?token=ZvV6Qf-jaJxcjdv2yz3xCxtIMDz2bjVNblblygHD0HSmmeTGe3YVGi_yTGIsQ8T9xWn9we98IEwWVZ8nwvepBcBULvZv8t0gsW3uTLvQF5i2fGrIK5uQ7YDI0R2FS1ex1lwSLAxsV4iBTmJcc1FxZGfQOw6vGa3CWNdEiHzMF2spNDb-jTUUfpq3pd_OGBj_CgArQcGyXv6pOkDfZ8iMuFWXeLifcWQa0mjt4jJLNUfmzygG2fUPhQuBKqMthfpcJ6e423j2Y9b-P65ZJdbI8ngl90e5sBv-3L27ohRAc8dJZqQX8j-zGjjkHz72J19iqUuhE35a1mhpLZJsRvLrEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b38aa3fa.mp4?token=ZvV6Qf-jaJxcjdv2yz3xCxtIMDz2bjVNblblygHD0HSmmeTGe3YVGi_yTGIsQ8T9xWn9we98IEwWVZ8nwvepBcBULvZv8t0gsW3uTLvQF5i2fGrIK5uQ7YDI0R2FS1ex1lwSLAxsV4iBTmJcc1FxZGfQOw6vGa3CWNdEiHzMF2spNDb-jTUUfpq3pd_OGBj_CgArQcGyXv6pOkDfZ8iMuFWXeLifcWQa0mjt4jJLNUfmzygG2fUPhQuBKqMthfpcJ6e423j2Y9b-P65ZJdbI8ngl90e5sBv-3L27ohRAc8dJZqQX8j-zGjjkHz72J19iqUuhE35a1mhpLZJsRvLrEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
مداحی شور‌انگیز عراقی برای ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/662853" target="_blank">📅 11:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662852">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae32ebcfa5.mp4?token=f7haCEB1jc2-BLDvdVF6d2jVrLN0RDNAPEb-W0eE2MjLFWwEwts6Rax8Do-9tdQUgLNRC2tBfekcr2cHwqv_h_6nIGHk89ao38NNLUKGrXkH-_6j1GMJoGyiGE1x1h0_kcDu1YloUNQ-WdI_RrEM7BSHRiejry_NQezkNk9uZ5FX1_ECjySySiiDW7IR3C5ox6dpeb95kRzuc6XvFScT7d6Cy-MG1OQC6UThFWOVWXM4cqyHaA9mdExn5ac2DOrXmt6iFPSyzurtkaTL8EwZV_3eQKUXpTJxeTuKZiy5M3IyC42Ecm0vLiBVvIkNsrEyWCCi1c85xBybbvgenZwJeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae32ebcfa5.mp4?token=f7haCEB1jc2-BLDvdVF6d2jVrLN0RDNAPEb-W0eE2MjLFWwEwts6Rax8Do-9tdQUgLNRC2tBfekcr2cHwqv_h_6nIGHk89ao38NNLUKGrXkH-_6j1GMJoGyiGE1x1h0_kcDu1YloUNQ-WdI_RrEM7BSHRiejry_NQezkNk9uZ5FX1_ECjySySiiDW7IR3C5ox6dpeb95kRzuc6XvFScT7d6Cy-MG1OQC6UThFWOVWXM4cqyHaA9mdExn5ac2DOrXmt6iFPSyzurtkaTL8EwZV_3eQKUXpTJxeTuKZiy5M3IyC42Ecm0vLiBVvIkNsrEyWCCi1c85xBybbvgenZwJeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
گزافه‌گویی‌های ترامپ تمامی نداره؛ پست عجیب ترامپ در مورد داشتن سلاح هسته‌ای ایران
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/662852" target="_blank">📅 11:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662851">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOQgRJf28_aXO4LuSHBro1eYl0a3lLfig3x8soHN_4i_UlffEn5rOnlAnBxF-qfckKeF7CiUzY-wiLhzhEtatNXJO9d0LZ00A6T8lawTtDFDCedR2Xgv01KccAe-OkYcb8ksQCm5_Pv9nG-_HCYPP-thMXRFIowO3F_txMYKky8qdU1OKfu3306cuYqdT0MxY6wP4iGpludKwEIIVcREASaGcDJlRazt4lNZ3a3QAsMWjmrjhTQTG5J2XrB575C-KLJTQLvKhI7aS_8LB1uDxc5YIj7pB6pF6t-UrtKmzUJmbUSxw3C9EPIr19Ng47JOZH_aHWyCvsSCS0ah07yU9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
مخابره کد اضطراری هواپیمای سوخت‌رسان آمریکا بر فراز تنگه هرمز
🔹
یک فروند سوخت‌رسان KC-135R آمریکا که از فرودگاه بن‌گوریون برخاسته بود، هنگام پرواز بر فراز تنگه هرمز کد اضطراری ۷۷۰۰ مخابره کرد و مسیر خود را برای بازگشت به تل‌آویو تغییر داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/662851" target="_blank">📅 11:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662850">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/686d4f02f4.mp4?token=TcGansgpYE8_wJlS61OlbARKogmusdycejdbrEdE5kiWkosSRdQzoQbtJXuQbQAhMtY-wTMB4o3RSKClxZR3xt8qdyDqbwT6gDcSTw7f4tvLoBi-eRTxCFycJ7tVREI5X-Golv9OSHcUxkbTo669x7a8rtG4BTE5RzImDN8-LHNZaYre2qjm6qopkhlPZfU74r_49nOj-Sott4gBmzn2mWCkYQKHDS1tSUFF3kZ0BfnXbY3d8vUai8EFTR67HmIj2TGfDGoc5WHpis6ni4YG6tmHLEhbcM4OGuUbSMWLpketfEqNqw5vfS55X5AoPn1HPrkSK0Sm-oF7VJhd2NfDIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/686d4f02f4.mp4?token=TcGansgpYE8_wJlS61OlbARKogmusdycejdbrEdE5kiWkosSRdQzoQbtJXuQbQAhMtY-wTMB4o3RSKClxZR3xt8qdyDqbwT6gDcSTw7f4tvLoBi-eRTxCFycJ7tVREI5X-Golv9OSHcUxkbTo669x7a8rtG4BTE5RzImDN8-LHNZaYre2qjm6qopkhlPZfU74r_49nOj-Sott4gBmzn2mWCkYQKHDS1tSUFF3kZ0BfnXbY3d8vUai8EFTR67HmIj2TGfDGoc5WHpis6ni4YG6tmHLEhbcM4OGuUbSMWLpketfEqNqw5vfS55X5AoPn1HPrkSK0Sm-oF7VJhd2NfDIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
روایت آیت‌الله مجتهدی از مواجهه حضرت ابوالفضل(علیه‌السلام) با صحنه‌ای جانسوز در کربلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/662850" target="_blank">📅 11:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662849">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔹
قالیباف: امنیت منطقه باید توسط خود کشورهای منطقه تامین شود
؛
یادداشت تفاهم اسلام آباد تبدیل به اعلامیه شکست آمریکا شد
🔹
توقف آتش‌بس و پایان دادن به جنگ در لبنان برای ما به همان اندازه مهم است که توقف آتش‌بس و پایان دادن به جنگ بر ایران اهمیت دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/662849" target="_blank">📅 11:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662848">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
ادعای وقیحانه گروسی: اولویت اصلی آژانس، اطمینان از محل دقیق نگهداری ذخایر اورانیوم با غنای بالای ایران است!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/662848" target="_blank">📅 11:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662846">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d38b526605.mp4?token=vGdsTygFlZ41H47TrR5WqJttL4genFl1bMs6jJcZGUovadK3Pph6KRLgZX2NYZx5bXPLHZGYKQ6-pT0OHBp5Y-kvuj6joChlyxMEcugx6rBP6l_SEqA14z2t4PaooscRd9PEXmLQ1ZkLEYhVWi4Z27FZM0UR7demzZXG7fqjfWAeeWnjezjhxDRYhuF7kgW90gCBTLQwiAEScMPYU0Es8Dr19r8o20SfSzxWR-wrOSdEOnZesdJ1EB6gvOW-_YKy70f1VcoA2QyXPi35M9oV6iBkE7v92uxrcKe8m5ah95rX9mM0axXsjni9S72GlnFNkHx2sOLfJfKqanYsW1s6MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d38b526605.mp4?token=vGdsTygFlZ41H47TrR5WqJttL4genFl1bMs6jJcZGUovadK3Pph6KRLgZX2NYZx5bXPLHZGYKQ6-pT0OHBp5Y-kvuj6joChlyxMEcugx6rBP6l_SEqA14z2t4PaooscRd9PEXmLQ1ZkLEYhVWi4Z27FZM0UR7demzZXG7fqjfWAeeWnjezjhxDRYhuF7kgW90gCBTLQwiAEScMPYU0Es8Dr19r8o20SfSzxWR-wrOSdEOnZesdJ1EB6gvOW-_YKy70f1VcoA2QyXPi35M9oV6iBkE7v92uxrcKe8m5ah95rX9mM0axXsjni9S72GlnFNkHx2sOLfJfKqanYsW1s6MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
صحنه‌ای نادر از تغذیه یک گوزن با مار
🔹
انتشار ویدیویی از یک گوزن در حال بلعیدن مار، تعجب ناظران را برانگیخت؛ این رفتار در میان گوزن‌ها بسیار غیرمعمول است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/akhbarefori/662846" target="_blank">📅 11:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662845">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔹
ازسرگیری مذاکرات فنی ایران و آمریکا با میانجی‌گری پاکستان و قطر
وزارت خارجه پاکستان:
🔹
دور جدید مذاکرات فنی تهران و واشنگتن، هفته آینده با هدف اجرای تفاهم‌نامه‌ها و ایجاد خط ارتباط مستقیم برای پیشگیری از تنش‌ها، با میانجی‌گری قطر و پاکستان از سر گرفته خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/662845" target="_blank">📅 11:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662842">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf3b188c09.mp4?token=lm43SU29_5ALZBKL-Yth6lke14Ng41TqkOm3Irbqa1iTJl8ck2cr0DgrV6fF9OBNa5Munn7sl0WpxCe_KwdiUIwfEOXhyyjdvPI3-6MTG4KODHrjNUQ8L8wRvFte3qur-lM9nPHrzXEIVj80rTHYgpKMY7-_L9lUC6fritAHcf-We0jzv0rv_sHjSaNEJGQX9-RJtDm8qBc6E26Css88ciHuo-60q0riEPVfJUfvM2bF9c7PGxPw3DNVj7QX7m9zO0BpgrSWM5gF7BzIxPC0yyV4FlKIsPepnZ9ekx6KkX6K6tkExB5UrBNbFbjxLZwjPQX--6qzpBy--QYfno00QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf3b188c09.mp4?token=lm43SU29_5ALZBKL-Yth6lke14Ng41TqkOm3Irbqa1iTJl8ck2cr0DgrV6fF9OBNa5Munn7sl0WpxCe_KwdiUIwfEOXhyyjdvPI3-6MTG4KODHrjNUQ8L8wRvFte3qur-lM9nPHrzXEIVj80rTHYgpKMY7-_L9lUC6fritAHcf-We0jzv0rv_sHjSaNEJGQX9-RJtDm8qBc6E26Css88ciHuo-60q0riEPVfJUfvM2bF9c7PGxPw3DNVj7QX7m9zO0BpgrSWM5gF7BzIxPC0yyV4FlKIsPepnZ9ekx6KkX6K6tkExB5UrBNbFbjxLZwjPQX--6qzpBy--QYfno00QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
قالیباف: مقاومت ملت ایران نشان داد که دوران تحمیل اراده بر ملت‌های مستقل پایان یافته است و این در دنیا تحسین شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/662842" target="_blank">📅 10:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662841">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQqa0yqSzpq1NHBloQnZh0_m6Hv1cHOurNmKw67-TyYl31IImToa7ndg23gKGYaXTKytbJLNuMQOAz0OVlUCoDDo1InpWj0iiFTBZIIZWvmOKn7Wi3qaj14V1enCWaKey6jusbGZ_cMELdTw4Awk86cM_1z4wUx9OHlXoPqEv6me1xNCtcbdUqKkp_9uqXKzGxODeCPLueREfG1pa4Z1WBeJIA7SFxzF5rkikGrkC2-zfj8Eo_LK4fFghWebQz00KIoKoTCOhXJmFqjY4VguqIj8RHQdyyRtumUHt9NE8ARgO_bEvGoDwhA7Uk5r2btU5uNHH_riRZxkIwWEC4ESJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دشت بابونه، اردبیل
🇮🇷
#ایران_زیبا
#اخبار_اردبیل
در فضای مجازی
👇
@akhbarardebill</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/662841" target="_blank">📅 10:52 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
