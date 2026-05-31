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
<img src="https://cdn4.telesco.pe/file/Jpu_gqbddtMMvReKYupgzpQSUY1RPa1n8OHEOWanyUEkDDb7TtCK9yiQvsrlvjN30xfnLCOKagVVJ0ESog3jdRrzkDBZnNBypRX7PcVBA6939hAGeiiG5ozBkX3JWrK9SYWtvLO7kWXyPxWuUQ-YtYhEZ2sr7xgHLp2y6YYgliPWOcKycfcdp200Me3F5n1Lh6rvQPvkGpBrm_0JEO1zCqY5wDcRtJhD4SWl0RAJGzYjVkka6GZlPO7ts--jUlyXq-bF6SUZNwbI7mlZWtKP0Z7weewdjB02LOhlGQx8UvHPuiM-JV_7Bdb-b5IyeE3lQ7q-fhq8uKFTPQxp6ySgyg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 178K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 02:21:55</div>
<hr>

<div class="tg-post" id="msg-76522">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">مرندی: اگر نتانیاهو در جنوب لبنان متوقف نشود، اقتصاد آمریکا در ماه ژوئن فرو می‌پاشد، زمان در حال تمام شدن است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/funhiphop/76522" target="_blank">📅 00:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76518">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">جدی باور کردید یا دارید شوخی میکنید</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/funhiphop/76518" target="_blank">📅 00:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76517">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝕻𝖆𝖗𝖒𝖎𝖉𝖆💤</strong></div>
<div class="tg-text">مشتی کارت اصلا خنده دار نیست واقعا الان من بخاطر تو کل خانواده رو از ذوق بیدار کردم بعد ریدی تو ذوقم؟
زشته کارت اینجا چند نفر واقعا شرمنده شدن جلو خانوادشون بخاطر تو</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/funhiphop/76517" target="_blank">📅 00:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76514">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromarshia</strong></div>
<div class="tg-text">کیرم تو کونت من اقامو بیدار کردم رفت پای تلویژیون دید چیزی نیست یه پسی زد بهم</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76514" target="_blank">📅 23:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76509">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkZuhn6X0MOObS0IHRRU5wwcP-fRFmuJccRsTUB9ysTE_QfZCRWK0WPZRNyLfDZR9zSOMUdBrsv0AC4fN2VeaQcAGAqvoa-3n_d5r3_2nyl-ZAl4R4FCf8IX-U4m2fHLl-ae84qnEUsKtpEiweOQ7smdD9HAdOB5fJLjTdsD2kjheCOR9duFpXPJZm04h331DsPZbjV0HFTrDxkRJPLwmJUUxv1LNuG1oV49c5wEz1Q0SsBx3AfHfw1An2jxN8yJuqGNm08v_J0coWElXLOn27pZi1UHLHhhYM2c0U46csRvEnDjKNtXeSPSTUSZf1DTLuysZjDEqhd77vK5R7UMvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویویویویویوی  ارتش اسراییل تایید کرد  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76509" target="_blank">📅 23:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76506">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjpQjLQ-V3mgowwOvaPHzJFfHqE_eC_fcBi5VwyPfHJeQZ8aIz93I0LocmSu_lAsfU6gjnSgyluXYL8751HPWbwdYKlit-1hMa7ilwtunOxt_f51HGT2izd7u6zpQ5aD3rgrQ7lIfkpeJQCSiiuSB0jg-A97BceFGdtb8l11gRz8ZXeVvR3m76wGw8Yg9YmXTlAEaYSSCTnDtQbup-9TyVdbRXYrvrI5x3v-mRrYUJHQe7azV4hswtM_my9lHKMpThG8kckQnT5_CcOcTBFXedjgpDbmTiQmDseW2FHjmiDzjAjZoTdjRsRIe3KuTKW4TeXbJN-v3T27Nk6pdg5BOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویویویویویوی
ارتش اسراییل تایید کرد
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76506" target="_blank">📅 23:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76504">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تو اندیشه تهران یه خونه مسکونی لوله گازش ترکیده   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76504" target="_blank">📅 23:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76503">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تو اندیشه تهران یه خونه مسکونی لوله گازش ترکیده   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76503" target="_blank">📅 23:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76502">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کار اراکی هاست
یک ساعت پیش تو کرج فعالیت جت های جنگنده گزارش شده بود
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76502" target="_blank">📅 23:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76501">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تو اندیشه تهران یه خونه مسکونی لوله گازش ترکیده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76501" target="_blank">📅 23:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76500">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">جدی مگه فوتبالو مردم برا سرگرمی نگاه نمیکنن، چرا باید طرفدار تیمی باشی که خوشگل بازی نمیکنه، حالا اصلا هرسال ۱۰ تا جام بگیره
جام باعث میشه تو سرگرم شی؟
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76500" target="_blank">📅 23:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76499">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vfr6XawsG7sxLzLt470HChRWbUsN7Fyc-Eyf1N6VeV-CEliMFY4nVDVCVPdd9z9GfAVAc_yWfJ4hn4qrWc07phqpQDg02OxMHLICVsxysb8fz_NAHBWmiK1tbPYzE-LqtvXB4Mupi_B6OelcZlKe7ExJvHKuxGNe1Ls2esvWIhsLTdX5xz_FZ7nBUHjPV7UgL5g5T-j7KuRxRzk1GB1I2rie-jzGZlGuKZSkKuLBMPzXxLCQrUWZAOPoiNcRO9JNW_lIedyjkK2iodN9ywn9Y0bUBkLmQa4qgCsOZ0f9DUk3zTCKb3kIM9PgkmdZ__1wL4YT4UfJ4jXh-mgWv4cefw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرسنال به اولین تیم تاریخ تبدیل شد که طرفداراش بعد از باخت تو فینال لیگ قهرمانان جشن قهرمانی میگیرن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76499" target="_blank">📅 22:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76498">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پزشکیان :
استعفا از ریاست‌ جمهوری؟ من کارمو با قدرت ادامه میدم و فقط شهادت میتونه متوقفم کنه.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76498" target="_blank">📅 22:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76497">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76497" target="_blank">📅 22:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76495">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYOy2JzNMLG5gtvwIWYE-pgu9NGx2OmX8YB5ZJb4Vw5Tq63ViAsRG0ZR7QUxgjsZnmSJ0YmY9JZElz0bEzrr3DhhD-nI53ozaKyjSGe3WCo1WE9EIOnmSgeJKs7sOMej_TUIy8KpXGRikirC-a5aumZSk65OhZ6GeMcgjZjgiAjE2-hW0Df-FVLdEKhTPoC-ZtjFNcVDiZrtkh3asnsoBPScacuuWb7nB8LoZcbN_5mgpOcZcvZeiSuQXOxn8kyiRHQ_RY2MiluT8L-LZOFWVYTijPuCeqQDmqDNMBmBakVwQC1k9PxuhiJB1PNkGJl-tBPI5SGG9Aqzn9dGFgpFmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76495" target="_blank">📅 21:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76494">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">آخه فکور (منیجر پوری) گوز کدوم کونه دارید استوریای دوماه پیششو پوشش میدید، خود پوری هم به کیر کسی نیست دیگه</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76494" target="_blank">📅 21:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76491">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پزشکیان زیر نامه نوشته
من نه استخر میرم نه با هلیکوپتر جایی میرم</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76491" target="_blank">📅 21:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76490">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8R_0G5tjmvifB0pG8o_QqJpYYFOekITCiLcJbJDddT4JwK9naMKl1SRrpeOxjQWul0C-wvH_owpzlMerEauD692PdZ36zXFujhkdjqD8dsebB5FGER5fR3g2eHE0oAT1R4aAVNiIEqxUnJFpeEXXDel4Z9-iS8JxBWXcMvU8gzDvsDwtLpPvNvxZY5CKCM3hm57b0PrLD38OtlIS3fwVqi5xaWShGWFOdOh0Ae-SHNC80S8x4NsuxabXyNRTghLhk0v2L67PKSsa4BL2AyHD29F1ztdSx0IxkqlUi80WcMcZchh9qhSyVcG_9hArODhLKWzew1-ZBZTHjzGtg0sSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استعفا نامه
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76490" target="_blank">📅 21:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76489">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فرض کن امشب هم قالیباف هم پزشکیان هم مجتبی ترور بشن
روحانی بیاد روکار هم رهبر هم رییس جمهور
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76489" target="_blank">📅 21:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76488">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تا 1411 با پزشکیان
✌🏻
@FunHiphop | ALI</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76488" target="_blank">📅 21:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76486">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">الان مثلا خیلی شفاف باقرشاه داره میره تو کونمون</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76486" target="_blank">📅 21:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76485">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">قبلا پشت پرده یچیو میکردن تو کونمون، الان جلو پرده میکشن پایین میکنن تو</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76485" target="_blank">📅 21:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76483">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خبرگزاری بسیار معتبر تسنیم استعفای پزشکیان رو تکذیب کرد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76483" target="_blank">📅 20:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76482">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">در جریانید اگه مسعود استعفا بده نت قطع میشه و کانفیگ رو میکنم گیگی ۲ میلیون؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76482" target="_blank">📅 20:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76480">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خبر اختصاصی ایران اینترنشنال: مسعود پزشکیان استعفا داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76480" target="_blank">📅 20:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76479">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نمی‌دونن تا گودال ماریانا هم بگردن پیدا نمیکنن رهبرمونو  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76479" target="_blank">📅 20:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76478">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بعید نیست این یه تله تروریستی باشه تا محل رهبر لو بره  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76478" target="_blank">📅 20:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76477">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">@FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76477" target="_blank">📅 20:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76476">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مجاهدین خلق از 021کید به جرم تهدید به شلیک گلوله شکایت کرد
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76476" target="_blank">📅 20:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76475">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خبر اختصاصی ایران اینترنشنال: مسعود پزشکیان استعفا داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76475" target="_blank">📅 20:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76474">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKPc7gONCjxgGXotiTKddOXDDFhj1cO2Ho3fT5ZlsZTsOl8x0Zq_n-Egme0mTK13S5CgKjExJu29x9z1FHTAfINn_Q5s8NktRrITgo2oY9Rnyhod97QmzYfo7aUIVb1CIbBWmhv0W-EbfEejWD42hEAJnoDWMEkUBupyktQrhkoIQZsQRA_5HHRvhS8J_BBHJQgzEeWx7PyH8LI_mRuoZJA9Dz7HcMe_PE0JEghF50lNbbZNULjkGUa91zDvwEUYH3BEPl9xWLkUJDXEHACpt8WDmXABT_KAfMPM-TGr2i09h3J7xl9Q-6TcgVIcr_fQyeTV2pm8gRco_-QGZ3coxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر اختصاصی ایران اینترنشنال: مسعود پزشکیان استعفا داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76474" target="_blank">📅 20:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76473">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مسعودو تو یارکشی فوتبال آخر نفر انتخاب میکردن
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76473" target="_blank">📅 20:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76472">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">حاجی دوران پزشکیان یادش بخیر بمولا
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76472" target="_blank">📅 20:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76471">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خبر اختصاصی ایران اینترنشنال:
مسعود پزشکیان استعفا داد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76471" target="_blank">📅 20:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76470">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">برنامه واشقانی توقیف شد
😂
😂
😂
خایمال تیر خورد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76470" target="_blank">📅 20:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76469">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سی ان ان:
ترامپ با آزادسازی هرگونه دارایی ایران در توافق احتمالی مخالفت کرده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76469" target="_blank">📅 19:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76468">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حسن و حسین امیری، دوقلوهای ۲۰ ساله، توسط دادگاه انقلاب تهران به اتهام جاسوسی برای اسرائیل به اعدام محکوم شده‌اند.
آن‌ها پس از بازرسی گوشی‌هایشان در یک ایست بازرسی دستگیر شدند و مشاهده تصاویری از ساختمان‌های آسیب‌دیده مبنای اتهام قرار گرفته است. هر دو در زندان قزلحصار کرج، به صورت جداگانه و بدون حق ملاقات با یکدیگر، نگهداری می‌شوند. نکته قابل توجه اینکه این دو برادر از کودکی در مراکز بهزیستی بزرگ شده‌اند و هیچ خانواده‌ای برای پیگیری پرونده‌شان ندارند.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76468" target="_blank">📅 19:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76467">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhvvbRoJMGt7cneviRvo813nuyXGNdE8sy1N2iLbVkWB0Y4i8YCn1GLQhP8_pw6FkZ3d9fzsAnycZmvvI8rXRw7yWEiroBpU2VhU2UvGmPLutbc-F_pz9VaBAkim2k9fcG_tF-DmN_VMyWxsopW197IOJDUhYpjAJx-iYgzTyvZ0cqB3T_csH-z8IsHd2fMlyhf1FHKfnn5u-s3IHpOysqYyAXZL0bZEnWwVWJEyPl0t_2y6FNx5nckNIojeNh11Gzyknk9ghEVWJwDYAshezqLRMQFd3jegKqaejBRN5YOiA8UkhshKH-qjzph3SNv4yEGKmoaLhD9D3rTt77zoOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوآ لیپا و کالوم ترنر ازدواج کردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76467" target="_blank">📅 19:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76466">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSeniorVpn</strong></div>
<div class="tg-text">😕
بهترین ارائه دهنده فیلترشکن
𝙑2𝙧𝙖𝙮𝙉𝙂
😀
آیپی ثابت ، مناسب ترید و وبگردی  (اینستاگرام - یوتیوب و....)
🛡
مولتی لوکیشن
🇺🇸
🇩🇪
🇨🇭
🇳🇱
✨
سویس آلمان امریکا هلند
✨
😀
| بالاترین سرعت روی تمامی اپراتور ها
☄️
تعرفه سرویس حجمی یک ماهه :
😀
50 گیگ   | سه کاربره         ⇐ 500 تومان
💭
70 گیگ   | سه کاربره         ⇐ 700 تومان
🔄
100 گیگ | چهار کاربره       ⇐ 950 تومان
🥇
150 گیگ | کاربر نامحدود  ⇐ 1,400 تومان
😀
تعرفه سرویس‌های بدون محدودیت زمانی( Lifetime ):
🥶
50 گیگ | کاربر نامحدود  ⇐ 800 تومان
🔵
100 گیگ | کاربر نامحدود  ⇐ 1,400 تومان
💢
💢
ارائه خدمات پنل ویژه همکار انجام می شود.
😀
خرید از طریق پشتیبانی :
✅
@VpnSenior_admin</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76466" target="_blank">📅 18:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76465">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فایل صوتی وسط بازی عادلو رو فیلم گلدون گذاشتم خارکسه به اونم خورد و غمگین شد ویدیو
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/76465" target="_blank">📅 18:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76464">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">شی سی‌د شی وز پرشین استارتد
اسپیکن فارسی و کیرخر
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76464" target="_blank">📅 18:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76463">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fuk_d7I5FxwDPiADLzWHplfP-ytBtPSgEjXSltzx3VftGduWQk1aIholrHs7W2tY86fF-EowmVRJb3bdS-Afo9JrKM4K0NX9uqGVDhgVeuOE-WxuVkm0ex2SBXAGVvEjiHDi85XRzJKYUvuEFLsyxUN0v5mh7h-MCmh4PXX7at7t9gMipSA1PTmiKdEEK1mP3yVzKkUS4Fp9f6wWeA4hr7pfPS3GwW1Xt3GtPEsQ0hEqRwQLfkDPBQCJ-OUyeHn1_TV70kPcH_PsxdJhxWfHpYeD8z2tH23Du_etCFRoPoCuVTvthzefrY6DKeXGdVuaO0hoNyMP_8JUjZzj2cR6Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف غلامی مادر میثاقی رو کرد تو چرخ گوشت.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76463" target="_blank">📅 18:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76462">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aczcWiuibUhvqqwEgz3JdLp4YI8-xPpn749AZtSiWqd0p1x23FFz4JNsS6tqzvv976P3iWXV15VTVgYf9O4VvWf1NGMEjg2jLCLw5LfWstafTH7F75sp5ABJvtoQDH9auo3rIRPLJN9tIIc91R4EFXHQrOX_OSUSo-cw0mzJ-6n2Oa4a5GbUASLLuQ2h4Ail0eIa5M6yhlhzfYu723m-2MTr_ZKZmWILy4Omzpm2v2gAIWvRkQoaePlTlQL4LJhtCbWjXGrAgb8lKuSzLnx4iadRvkR8VckwFKd_Lc5LFHzuveQ9q24UBS8g6wajhUFvsYmk0nahyyApuoSmOox4sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خالق مینیون‌ها فاش کرده که همه مینیون‌های تو انیمیشن مرد هستن، چون نمیتونست تصور کنه زنا اینقد احمق و نادون باشن.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76462" target="_blank">📅 18:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76461">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vukHHkNf8N1jt7BLeg70cu46sZYlkpTeICeU2lRbqb3K14xGhVGhiK8YmmOwe9ZrZDdwlN3mo1KyeL9S0JBOPCadcRX-xGTfEu4db_gqdBmZGpawGIxyOEE4BYe-jDmLXgwTOgLwk7WDRApgF_z_lEwpgWF_-sT9jATOL_ab8sfel0oCqRdxDgLoZHfoL3JFmhjyWOrzfbp_-qc7OzmpQQpJdrlOZP3LqLd0vrwioOVpK_bqZKW2v15-9EFWNYTx64-EkLajiY9HFGYkVT4qrkJnd9a-Y7bZonIgMXm-NRmgGc4O9PT1gAZGJC-fA2giATYOT7ju8FnHT1IXResSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
سایت بین المللی
bet120x
✖️
👍
دارای مجوز رسمی Gambling Judge سوئد
👍
💳
شارژ حساب از طریق ارز و
یووچر
و پرمیوم ووچر
💳
تسویه حساب دلاری سریع
💊
بیمه شرط میکس
⚠️
فروش شرط
🔔
ویرایش شرط
3️⃣
2️⃣
🎁
20%هدیه واریز از طریق ارز و ووچر
┅━━━━━━━━━━━
🎁
10%برگشت باخت به صورت روزانه
🎁
10%برگشت باخت به صورت هفتگی
🎁
10%برگشت باخت به صورت ماهانه
💻
ادرس ورود به سایت:
https://bet120x.com/fa/?btag=971470
➖
➖
➖
➖
➖
👈
آموزش واریز و برداشت دلاری
👉
🔪
کانال اطلاع رسانی:
👇
g10
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76461" target="_blank">📅 18:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76459">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نیرو انتظامی تهران یه کافه ای که توش اسلیپنات پلی میکردن و پلمپ کرد و گفت: اینا شیطان پرستن.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76459" target="_blank">📅 15:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76458">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">نیوزسیتی پرو: با گذشت ده روز از خرداد، همچنان آمار رسمی تورم اردیبهشت 1405 منتشر نشده.  @funhiphop | reza</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76458" target="_blank">📅 15:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76457">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">چیه دوستان
میگم خبر مهم فکر میکنید روبیو بهم پیام داده از پلن های ترامپ گفته؟</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76457" target="_blank">📅 15:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76456">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تلخون از لیبل سابقش جدا شده‌.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76456" target="_blank">📅 15:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76455">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خبر مهم رسید دستم</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76455" target="_blank">📅 15:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76454">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">امین منیجر یه دوتام به پوری بزن بلکه سفید شه برا چهارنفر
@FunHipHop
|  Mmd</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76454" target="_blank">📅 14:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76453">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پیام های شما در چند دقیقه گذشته:
فرید جان سلام من بندرعباسم اینجا صدای انفجار میاد
درود فرید جان ما قشمیم اینجا چند بار صدای انفجار اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76453" target="_blank">📅 14:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76452">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGT0C1cbWYBHh0Lu9TjuIw4R4vifSnyxIa3lMoaznsOeyADLegoDPCLYcGjzShY2V1ryjZ4dFC3g7-RiZ_Dc_2wVK62kK-sYyuLHmCFWFj6lRgz-92kAls_eI5DOUrf3_VAaxOXrBilObSZ34gXbSHFqPjTG_1CeFQZaclmMH42Prf2QjvUrVHTk24qlGSesclIOBHHWojIwaJia6I4a5R8WDjiS7SnxKSwA3St4FmdjBiUBScunq4cdlUAJMEMBY07uAK4ukACt2bzZE1DI39dab2O2pwbbYZ50VyOMzPGu0v0U-5p1J_t2hbs8eTXHnrWhj2hyKV6QKy8ViTYXBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بحث کالچره پسر
عکس خمینی میفته رو ماه
عکس اینا میفته رو گوشت
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76452" target="_blank">📅 14:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76451">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آقای باهنر یجای ثابت وایسید از رو موتور پیاده شید صداتون نمیاد</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76451" target="_blank">📅 14:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76450">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">الان رسایی دوربین رو تنظیم کرده رو صورتش فقط عمامه گذاشته
نه لباس تنشه نه شلوار
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76450" target="_blank">📅 14:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76448">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">امروز مجلس مجازی بود  @funhiphop | reza</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76448" target="_blank">📅 13:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76447">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">امروز مجلس مجازی بود
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76447" target="_blank">📅 13:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76446">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وزارت قطع ارتباطات دست به ماشه هست
ترامپ بگوزه نت رو باز قطع میکنن
کار مهمی دارید انجام بدید این روزا
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76446" target="_blank">📅 13:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76445">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یکم دیگه اعلام نهایی توافق و مذاکره طول بکشه از لبنان فقط اسم "سیب لبنانی" تو میوه فروشی های ایران باقی میمونه.
اسرائیل امروز لبنانو شخم زده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76445" target="_blank">📅 12:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76444">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مردی براي همسرش پیام داد   عزيزم تو چه كرده اي پيش خدا اينقدر عزيزي كه همسری همچون من بتو داده زن جواب داد نه نماز خواندم و نه روزه گرفتم و خدا از من انتقام گرفت:))
😂
😂
😂
😂
😂
😅
@FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76444" target="_blank">📅 12:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76443">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مردی براي همسرش پیام داد
عزيزم تو چه كرده اي پيش خدا اينقدر عزيزي كه همسری همچون من بتو داده
زن جواب داد نه نماز خواندم و نه روزه گرفتم و خدا از من انتقام گرفت:))
😂
😂
😂
😂
😂
😅
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76443" target="_blank">📅 12:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76442">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مطهرنیا:
واشنگتن به دنبال مدیریت ایران در دل یک نظم امنیتی و اقتصادی جدید است برای همین حذف کامل رژیم در دستور کار نیست
میفهمم چی میگیا ولی متوجه نمیشم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76442" target="_blank">📅 11:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76441">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نیوزسیتی پرو: با گذشت ده روز از خرداد، همچنان آمار رسمی تورم اردیبهشت 1405 منتشر نشده.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76441" target="_blank">📅 10:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76440">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خاتمی جلو عادل اصول گراست
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76440" target="_blank">📅 10:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76439">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">آکسیوس: ترامپ همچنان به خطوط قرمز خود پایبند است و تاکید داره که هیچ توافقی با ایران امضا نمیشه مگه اینکه ایران تضمین مشخصی برای عدم دستیابی به جنگ افزار هسته ای بده.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76439" target="_blank">📅 10:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76438">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d2dea055.mp4?token=vp2_2vFjQpc3I01deeWig6MQB-1zzDwh_yuEKfFpFRphOOO4EymVPFpKCRF8IqamPJymZGJcnfUTy22iUQUCUKZ0ADKBpzM_JxiVGTucdBC-TWDx6MuFb8KP84pGJxiAbT5f03pRZrmt56T0kAkesQ-kgMy0Q_YpFpvnifu1HxWTf2c0RsV7z07s8gO7d19NbGWmMdX6leJ5t0tRLs-1ki2SFnANQq-Zysuylgztk3V2FhlwZkxqs25_-b-TpEd61J2WjuQk7TEZi7yMeMDE73xKWVJzbjhoE09aTdzFxGo7Vwn2k64fvHLJn2vFA5GDkAWgNbdM9Yd3dOllhtTxsDgcAKMPC6ihkF9WIdQ0Sm2pm0_SciFo2Q6Y4LMG7rxk15mmI-V9vXMq_CFtwyuJxm22PMMBU7CPjFHws5Cgm-r0TPnKnilSHAkpIZmP3gEc5z92m7QPD8nxbHc2BtAwX9S8yA_fjFyMKC2ZGHz7AZUaMwQ3hlKIkxo4C2vvBzc2tCTJ4epu5LidusfO8dnd17pSy7cAf_6r6_djj9f0S9U0uBcT04noW-37_KoktuiI658wjfKO4Qxu-PhYzFdSesb34eD9TUQwO_62pbzSi2Ldl1tttk7o4NyLtdiZvtAuGCRrOKD489Hl5Ho7YTTs9ZIqLAeOuv_v2CcditHaM2s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d2dea055.mp4?token=vp2_2vFjQpc3I01deeWig6MQB-1zzDwh_yuEKfFpFRphOOO4EymVPFpKCRF8IqamPJymZGJcnfUTy22iUQUCUKZ0ADKBpzM_JxiVGTucdBC-TWDx6MuFb8KP84pGJxiAbT5f03pRZrmt56T0kAkesQ-kgMy0Q_YpFpvnifu1HxWTf2c0RsV7z07s8gO7d19NbGWmMdX6leJ5t0tRLs-1ki2SFnANQq-Zysuylgztk3V2FhlwZkxqs25_-b-TpEd61J2WjuQk7TEZi7yMeMDE73xKWVJzbjhoE09aTdzFxGo7Vwn2k64fvHLJn2vFA5GDkAWgNbdM9Yd3dOllhtTxsDgcAKMPC6ihkF9WIdQ0Sm2pm0_SciFo2Q6Y4LMG7rxk15mmI-V9vXMq_CFtwyuJxm22PMMBU7CPjFHws5Cgm-r0TPnKnilSHAkpIZmP3gEc5z92m7QPD8nxbHc2BtAwX9S8yA_fjFyMKC2ZGHz7AZUaMwQ3hlKIkxo4C2vvBzc2tCTJ4epu5LidusfO8dnd17pSy7cAf_6r6_djj9f0S9U0uBcT04noW-37_KoktuiI658wjfKO4Qxu-PhYzFdSesb34eD9TUQwO_62pbzSi2Ldl1tttk7o4NyLtdiZvtAuGCRrOKD489Hl5Ho7YTTs9ZIqLAeOuv_v2CcditHaM2s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی زرنگی عادل جان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76438" target="_blank">📅 09:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76437">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CW5VvTbqyUk24B8bZ48JcmYomidYpgJarW_t1gQ6-v6hzwtpT5JV0BODMpgQeuUiNnzYtwS5ga7RxeuO-REsksgILjaflVqlqTc1czMHOQt21NyhhPUbK62lEnmOmV3Qa2KoJhd0YT2Ejbrenbjb7pKElXnTUQ1k9TJV2D3VDQ6gLRU-jiEJnlBD4oqgEt7Jd5DaHMGUgS3LGwO1VBduASIMwBupEP1vNCphg-cdjgu9vwysXZofy9iig1ofiy1rQiEpE3DN-VSC_WzqAGjDvUk-QXnubx3wUf4I37Bpt5REozxoSZFOApD9o7SZmjdEAf6XF3eqzknzpa1kNQezJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صب وسط بسکتبال داشتن همو میکردن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76437" target="_blank">📅 09:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76435">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBPYiVb2w9V6uB8IWgoC6-Uzo2tmcii-ozozoUB2GUZ2atrTAn6DuPE3aQWM0r5nTkot7UbwX7gqhkTSxAi22LRgqV9rtDBLAJszHl8T6o8QSX9WOiLaeOY6ZnPnx1ddM_M2PkPw1FMxHb40WqUIFcCvv7u459Tr1n_8AgthmYmjTez6c3TU5z24SRahYbKGs_1FEIAKzQn3HFNuexaVNn4waM3vrZOIMT9ScQ78d7UkJgljIBsLj7rAw-1GALuMNH3tVe1JkG_1QolQKue13-vP1RgnYkA74DgdZChFTnVRpnsx3F48VuVKh6_aJKbo6DNRkYbdGKkVVZ21-B0g4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ce07890ba.mp4?token=drWPqXHsinQPMx_YeohBaypEk5TPFBQRvcLcu_imE8mdBjRMUOulFMXN0mrtiLA6ilK1WvDSzuNOuq56THY_XGpVzLqF98doF2NiAboZ6ZXcHldVXiTAmfKzW8drGEJCwoSpO5hLj7LXt1E4WDqQqUefLiyd_FwM4HokzR6D3hIok7ox8g-xd-MvTxS3XsMqujg-zLY58STuv-trWCNIHGfDKqXOubHFQg36fS-RyWo7NrC2vyakhPQz1Wv0rq2hp0bONPJ88Quuu0YIho1YCPwwHYx4XmCfJQtyaW3a-3HHiXthJLOxwg165IvXm3jFXZZ5XW8MJ4VKz3gDYQdZlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ce07890ba.mp4?token=drWPqXHsinQPMx_YeohBaypEk5TPFBQRvcLcu_imE8mdBjRMUOulFMXN0mrtiLA6ilK1WvDSzuNOuq56THY_XGpVzLqF98doF2NiAboZ6ZXcHldVXiTAmfKzW8drGEJCwoSpO5hLj7LXt1E4WDqQqUefLiyd_FwM4HokzR6D3hIok7ox8g-xd-MvTxS3XsMqujg-zLY58STuv-trWCNIHGfDKqXOubHFQg36fS-RyWo7NrC2vyakhPQz1Wv0rq2hp0bONPJ88Quuu0YIho1YCPwwHYx4XmCfJQtyaW3a-3HHiXthJLOxwg165IvXm3jFXZZ5XW8MJ4VKz3gDYQdZlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو پادکست جدید بنی بلانکو ، بنی جلوی سلناگومز میگه که از نظرش زیباترین سلبریتی زن دنیا سلنا نیست و مارگو رابی رو خوشگل‌ترین می‌دونه.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76435" target="_blank">📅 08:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76434">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76434" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76434" target="_blank">📅 08:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76433">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rw-szjaprUaG5VVe3AcwyyrI2P5tU7TpNclfAXSEIin0Ril9yNJ9DWS01Eh1ab1H0ZKH5pnlMTVSFi1rjES4VfpuMYBEY-UYRg9t-ITCiJSLYZMmOK1lEuRthMZ2fr03p6uWA5Cz8vbooPTn8raHfpNmDctTVASfENa4Qn_kRuSEGRmiGDZaDfmu7D9Bgu8rrtW4vzJaREZVuYr8Lzi-je_YdTt-6mVqyhIR41pnEggi3v2o9q05eduj1c8X_LqPfOCzaV8GGu9xBhKZ5Qs3QstV83sjYCGgwy7E67ev2zVN2qm2vwyLRLXGYtcKDih7kEfMhPYTIHNlzsagsktycA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r10
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76433" target="_blank">📅 08:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76432">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ به «فاکس نیوز» درباره ارتش ایران: «ما آن را بی‌سروصدا رها کردیم، زیرا فکر می‌کنیم ارتش آنها تا حدودی میانه‌رو است. آنها افراد دیگری دارند که میانه‌رو نیستند و ما به هر حال از آنها مراقبت کردیم. ما انواع مختلف رهبری را حذف کردیم، اما اساساً ارتش آنها را بی‌سروصدا رها کردیم.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76432" target="_blank">📅 08:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76431">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2028de58a.mp4?token=F7P-ID0aFrRV-X7UJRXnCGuCK598STYkCv7MDqQ1cFAMqi3gdxSrawb6iBuz61ggO1hBJH7yWlRe1ANNfGAuGSxMMAWAy9Mia6zVhTvx41jAA_aVLepIdUixxUgwyaf5tiC1wo3R6Y3OQhLWv0d1Y4kDZchL97MpdET1hn4Qa-tjoxL9rJ1oNS0Gw9LNx6Dsb2XpUtCf-WhOmzbnhIIINK3YcMyclNY-6c9TP2ovrjf2iQ8Q794j22FuqsFEbEaJ4WnHqoXxfhjVyc6kM58ejoEZh93oPGAW236MekfnvAk1O33kapHnYBAgU5xwo2rcuhGmOuqJTi2Q3rdctQvQbmAZnJbk0Qlbg4Q7Lls33Zvs48eJInVH4LeV2ALCafR6md_akHAgfKY039faYYiHCutRigRu-B-5vsjjY6tOjvkkG01FtQuUhdWz92S1oQhF59iuc8IaKF6vur-D0tdI8ccc8pYBuftJSoN5tVEXmB6BGgRPBHfvd-kW7J5_kBfI0cBEWA4DGAAyBmjozkDLO0NOHzMvkZycGUsY9cnyuNYht5xqKPIQNzskIqa22-QvluMH2bF4lTwa9G8ZLeNfjjXLIEDsevyT0d8xZikS0ojGmuNZOzYr8UeUwvyR8Przq3G58Qz11OcA-ZQrEkVUAcYnuuV-QwpLQ6nrIzZ2lq0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2028de58a.mp4?token=F7P-ID0aFrRV-X7UJRXnCGuCK598STYkCv7MDqQ1cFAMqi3gdxSrawb6iBuz61ggO1hBJH7yWlRe1ANNfGAuGSxMMAWAy9Mia6zVhTvx41jAA_aVLepIdUixxUgwyaf5tiC1wo3R6Y3OQhLWv0d1Y4kDZchL97MpdET1hn4Qa-tjoxL9rJ1oNS0Gw9LNx6Dsb2XpUtCf-WhOmzbnhIIINK3YcMyclNY-6c9TP2ovrjf2iQ8Q794j22FuqsFEbEaJ4WnHqoXxfhjVyc6kM58ejoEZh93oPGAW236MekfnvAk1O33kapHnYBAgU5xwo2rcuhGmOuqJTi2Q3rdctQvQbmAZnJbk0Qlbg4Q7Lls33Zvs48eJInVH4LeV2ALCafR6md_akHAgfKY039faYYiHCutRigRu-B-5vsjjY6tOjvkkG01FtQuUhdWz92S1oQhF59iuc8IaKF6vur-D0tdI8ccc8pYBuftJSoN5tVEXmB6BGgRPBHfvd-kW7J5_kBfI0cBEWA4DGAAyBmjozkDLO0NOHzMvkZycGUsY9cnyuNYht5xqKPIQNzskIqa22-QvluMH2bF4lTwa9G8ZLeNfjjXLIEDsevyT0d8xZikS0ojGmuNZOzYr8UeUwvyR8Przq3G58Qz11OcA-ZQrEkVUAcYnuuV-QwpLQ6nrIzZ2lq0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باز خداروشکر فینال رو بردن میباختن چیکار میکردن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76431" target="_blank">📅 08:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76430">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">MFGA
دیروز تو فرانسه مردم دست به اعتراضات زدن و  با پلیس درگیر شدن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76430" target="_blank">📅 08:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76429">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">داداشم ومبی ضرر دیشبو شست برد</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76429" target="_blank">📅 06:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76428">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-ug0x4Zpff8usvEYvs8yYWEaIkDPdUHodFLOg77-3QCJZ80Ubdhc26YjHdFJlqp3ec0ahqj6Kh4Izs3pgfH4vefWRG2AF2B1Hdj9cCKFjaIy1H97-Vny_jOSwieXgHWIMRDqaksEdQRMHoqNClwnUBMNPisr3B4XHtBc7JA-Cs8Z18PamMJ8H42zYcMvYkAlZsjaGFlZow7yWlvGh-w0mn8rxkhKi7ZEEN2mKYwCZ_-4i2lZirJFDwR_eOZGCAbQHOtcOW0wwXUZTnyjL4pFGoW965-XDv0opgwhG5j43mPe8A1W9ivP_3vK9R1aD1bpkM4wdWlyZsXUgAXZUQYPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترمب با پست کردن یه عکس از جنگنده‌ها و ناوهای آمریکایی:
شما درحال سردرگم شدن هستید.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/76428" target="_blank">📅 02:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76426">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5pFVI1nZPYXW7esTvSfk3sCtPiDmhnuh5NPgYDgBaZ665DTRt5bYNv0qoA7tnrSO57hJWAXzHmCk7oxSpdns8Gt3KmgewXsgqDuu_uV0ygVJT-7yQYQ7PNg9KF1Fz4_M3NbSRmcmlctc9aztYzOxt-IbOWMje8eZ_3Y1dt1aM-nHWcZ9qQpClEXEj57NG2Hf2mjZaGkfs1YlITercBwiUqf9Cnh5Rz63j9LVbjFa_eFmQGn7Ms4LHDM1wHSvjc0lqtfqGxMzsxlKANCtnSCACzkinw3dvQts2UWMv7QqUczpcqS-xkHGCyzfnAqnNKIYPVoszgU-qUIn3Ru5Z_RZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقد خشن حمایت نکن آرتا، بهشون رحم کن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/76426" target="_blank">📅 00:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76425">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fboMaVRB6EwHphHTFg13AcR1fuqzDESIkDJ2in7qLLrpRKDLHzZlZTVIMnyPSKtuxOMoc3Tc7t1yRkITZ8diVvAqUe-BoB6cTGzlqfLc-xJsbLc8-ZIuI1lfvs3XvNkic_hJ8q4q20B9OHU0XaC0JV0GUDeIDpl6S2QoXa2p2DP_lAJdcakBtmFbMsm3VEfX9QG6tUUsQWVivVAKuCF6ViORt1A9NHlgV9QJMs9WUUTrwuDHa7WQZaccKTFcYurf3aS1gsLc7Kck5yXGp4dX43gzs9AFqvgsgRCXprpvHV_equuA1WfoIFgndhWbmKCH1T97z_hA5HxXxSBFvt9lQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینو میخواستم با کپشن سه تا تیم نجس تو یه قاب بزارم یادم رفت
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/76425" target="_blank">📅 00:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76424">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اینم توضیحات منیجر ویناک راجب حرفای امین منیجر
خلاصش اینه که برا ویناک پرونده سازی کردن ازش باج گرفتن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/76424" target="_blank">📅 23:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76423">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLlfQz5KPNajRr7bYeDa25LUtcC47mXC8KxaHA_sSHROLFi3CObe6M_a9y60NC1-Pc1INbb01b6ezjlzqCqiau6UXL9KODAHNVUQ8Sxg-EaxqT4DUc2Sjxkf_Pa5EnFT6Liox9xB8e_-HirVW-ND5LSsw_Oz3GlFyGfCVeAC7LTMGr86-kpIqVJrpQ62VXkRhVAmzEP3J2jVbx-ed1lKMcT9SNEgOoSF3fC9af79xBJJ8AiFJ7SpsrNkTzRo3OAAjfvyCP0nTIm9J_YjuCXg1RH1VgjfIECCU7w1iW2dXniaCYiGU1Ja8iL3Dt7ZrRY74lNc_VsJ-4h3kfSo_Fi0hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم گذاشت چنلش گفت بگم اینایی که باهاشون عکس گرفتی شغلشون چیه؟  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/76423" target="_blank">📅 23:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76422">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qESRAuqzIRpX14sO4Hb2S-bfNYa0EnCMYrc4XcOSqNNNpW7xtpY5w2tnPIjMhAJmfo1ZYVVLsMeIGPQT3NKmVfWlOIjt938PpDd0Ots6Y44Iu6ucPPevYergg0obQB4B3h1nBUmSgxuVqTGyQkWc_4GP_kqoNB1CIa0YkV-GLyxrHgJIVvp6XNnwdP4lqd2_oKAeQ0vz2Da6rMR3ZkJ_ScNVFO7n4sZpnUbIZoJwjATDaFmX3dupYdM7DXn_ZFzT5COzptbjw-H4KuSGURZRA_o1Kdv6dkxHWnBCGbzjekRo3esaHW9ImS3D1RuByZQe4cZXs9DhgNkgx6ZHXKTyrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام آرسنال قهرمان شددد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76422" target="_blank">📅 23:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76421">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzlQmszI-G0DftjKZzsG6GjYO1d9nO9wdwdzFrvSGyP2v7E6TlD7rAbqQAaNUKGNGAdwVflg3NVbJuNUR2CAPjo5-b8RYbeaP545a4dI7R0jvbbrAcDq0nfuK6nqiAEN4q3QS4ymGt2Ft4mFrTCnOGnIVUcXuwTbFsMj4TdlwsTkvV2b0bfqodfTHI4RiPbFFcjF7uSMFSdh0kURfKmAvWkM09l1AYYFxNhpLBdL9wiw9okI8PpJ8g0pBElk1ao7y5BEv8-WoL18EG03RVAJ1jcEZHI0Kne6gri-kV3kKTRIy4xZWjOtE-ThXTBjFPr18PGgd6ziJ3Z4EV4rV8mgCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم اینجا کیرخرم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76421" target="_blank">📅 23:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76420">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">حاجی فیلم خاکبرسری ریری هم اینور اونور توسط یکی از اکسای قدیمیش پخش شده واسه زمان زاخار رکوردزه
😂
😂
😂
😂
🔴
برای دانلود کلیک کنید روی لینک زیر :   https://t.me/RapiFreeBot?start=get_uplzypfzeequaabv</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76420" target="_blank">📅 23:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76419">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKkDS3zFZP1ca4iBqeDYI7NiYrGqvtimM6M0kSF_qnHtwdjeH3CwL7a_vXNH8MQMHNDyLou7-5P6Id3ZDQanyZccXMu-PGkGjnueiCgyDeX72JDE7rY3OIkFlvpVy6ZJbRXOVBTCPc4nmX1K9VeyKONiyIff7bWcjmGvWBgqBMQvmCgYq5V1mXN5g54Hoglh2P84vHqmX5rbHLEUwMVRaNZRPOm-oWXSiLZyYrc3t-BSNmPPqqr7GKCPVIjoxmN8UlO-gnMhWq7PcQkM84H2lSOvpvK6rVwqRIoeJ20t-mMTGVAJ43-wWVkmdAGqf123QZmCm2U3E0yBc5YUXwpAsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه من همین الان با یه اکانت رندوم یه همچین چیزی با عکس خودم پست کنم زیر ۲۴ ساعت اکانتمو می‌بندن و میان میبرنم تیمارستان می‌بندنم به تخت
ولی این کصکش چون رئیس جمهور آمریکاست همه می‌گن پشمام دیدی چی گفت پسر
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76419" target="_blank">📅 23:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76418">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXmWD35oJUZofqOMJpINcqEka6Ufs9WmFQKLkm9DwZ0wN9VYav_wCs2qmqG8qx9ykCHJXDQWCILe-cQfejWAu5OOFNahW-COj_RADFdYEXTigy4TmtaI4eoatZUYbQCnSR3pUXjMbwLvU3VD1UK6AjpYwCdP3QcDLCuoDivc2NSwF6TrgPXvmMXYXIuEuEZjA8moqLl1KdME3GLWsfm_YMq-Hor6OpnFpupj_WrDdOfWBH-iA69cy3msRR-R63g5Zcib4KaWXcJ0DgcB8H2RrAiIuI4SJLDzVEou6_UJPH2xPn95PAqGGwPlgNfCXHX1koCOoX30b6alRkNnBq8Yyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی فیلم خاکبرسری ریری هم اینور اونور توسط یکی از اکسای قدیمیش پخش شده واسه زمان زاخار رکوردزه
😂
😂
😂
😂
🔴
برای دانلود کلیک کنید روی لینک زیر :
https://t.me/RapiFreeBot?start=get_uplzypfzeequaabv</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76418" target="_blank">📅 22:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76417">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">با این نتایج انریکه چندسالم نتیجه نگیره ناصر بهش دست نمیزنه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76417" target="_blank">📅 22:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76416">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اما امباپه عجب آدم بدبختیه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76416" target="_blank">📅 22:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76414">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrQv_pAPBbJsiygSnNrLodvN1MQ8Bm7omjJcGbGX6TPMTE7Mniz-Ozq4TYB8D-dCB54D0BjtFmtzv13wTZRnd1hdp2MLDG57wqVuqDsNd5ENwKSSedYMhWdw3kuIN7bF2Ka4HpxyNwalCkMoSSlmGBc9nx4PMnye18DVh1f--HUYGzrq7423boYgqYUKxQOKjOZ5WEIYDN8hUVArcgMCvqpXU5AQpxTEQLI-DiBVHC3ZB17YDBhOyG9CEV9X4Z0M_4fIiuVOm3FBJBPRZWTjkYBz8r4_-GBukxZgPb6L4XSr6rvvFMbmSEzRi_C7ZXkuD9hKCSrySogCmIGgppu8Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده مشخص شد https://t.me/FunyHipHopGP/12247710</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76414" target="_blank">📅 22:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76413">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تو کامنت نتیجه بازی امشب رو پیشبینی کنید  اولین نفری که بعد از اتمام بازی درست گفته باشه نتیجه رو  یک گیفت Nft میزنم برا اکانتش  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76413" target="_blank">📅 22:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76412">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هوادارای آرسنال الان یه دوش آب سرد برید حتما چون بشدت حالتون خرابه امکان خدایی نکرده سکته هست،حتما یه دوش آب سرد برید و سعی کنید گوشی رو بذارید کنار تا فردا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76412" target="_blank">📅 22:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76411">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsRjYZcv3IeQW7O1ICaB-iRBrM3pqpJ5XGpyzz-9jBxi8ofi7lHvfee4uxF1eY4EzRMOhN6SpLK84hVu-Fs2TKfaw7xXxm87x1Snv70JM7EOG7SacjpP8Q5mYeh2-naJCOaabVsU4-q2tsGZ01CtmKPilWIpRheAVSsAoC74zgAuKYmB78xUaUsKcf8ygi0MRf06LQ5jqL_1yVdt2U_dyG4JADtfOeO9vnmipoBCpbztfTm2jypJeAtcI9ilJZe0OWnX0oS1X7VbKCECbFJUPLKwk9N9_1FsseC9En9JmnvaFjg5Hb2aNe7ePB5e_GNIip8St0ZZYWTlG_-cFwRFfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پروف
#غمگین
#شله
#نور_از_دل_عالم_رفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76411" target="_blank">📅 22:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76410">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تو کامنت نتیجه بازی امشب رو پیشبینی کنید  اولین نفری که بعد از اتمام بازی درست گفته باشه نتیجه رو  یک گیفت Nft میزنم برا اکانتش  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76410" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76409">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گابریل
❌
اوساگونا
✅
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76409" target="_blank">📅 22:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76407">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پاریسن ژرمن برای دومین سال پیاپی قهرمان لیگ قهرمانان اروپا شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76407" target="_blank">📅 22:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76405">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پنالتی  رو ریییید
❌
❌
❌
❌
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76405" target="_blank">📅 22:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76404">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گابریل پشت توپ
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76404" target="_blank">📅 22:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76388">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رفت پنالتیییی
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/76388" target="_blank">📅 22:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76385">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آخرین بار که فینال لیگ قهرمانان به ضربات پنالتی کشیده شد برمیگرده به سال ۲۰۱۶
سن سیرو
رئال و اتلتیکو
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76385" target="_blank">📅 22:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76379">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گربه های مشهد گرسنه موندن امشبو
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76379" target="_blank">📅 21:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76378">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">۹۰ درصد ملت لوز شدن</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76378" target="_blank">📅 21:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76377">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تمام
بازی رفت وقت اضافی
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76377" target="_blank">📅 21:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76376">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">روح بن لادن رید به خودش
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/76376" target="_blank">📅 21:24 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
