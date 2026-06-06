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
<img src="https://cdn4.telesco.pe/file/ocVDeNuEXmKXrvs81S0SGTH5H5z3hTpsPbe_l8ABthcUER6a0N4eW4b2C9KxKSvXTXHVqdMGKBp1V7e1DFTBibWv-Y_oDh2tV-TbDncxW3vcShMCdKuiZHHb_IiaL3CmQ84YLCoSsbMyB8J-39gwEM9SckanTj8XOoy9bUCyOZDosSIzjhHYhTKmSFeTHezUk1BGiG4n5pOCtjq_0-MpTpnep7VpGGEYQglsrUmbo5i_H-AacVVfFGppkT4xGlzoSYmCxup5v7vX0TrhtJCuVGOp3L9q2TSKyRYg1OlukP9WM17Kk8zc7V1dSDUhOEuAy_IeVH_p8UuV_msetfnbCg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 291K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 22:15:48</div>
<hr>

<div class="tg-post" id="msg-13642">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a15cea3880.mp4?token=eZ32zuemNTIK0yrsN6PpUm9X7n72vHt4730sLRaJZEc80DflcAHthj0jpj3STh2BOTywhOcp2uW2Jf2elmKTBn5EDQMQmElxtRPib6GWT2elDNELX9owh6MuEwaO4zb4tlh2ZAK_pqh2Smdu7KcZErJ2yxZWWxvJPOtwueQsQpuYW-gyUJNCFhdYSac_4TVGLfmdxopSS77mk1cGnYPYm0vmptJFLVWUzOwDKGZaQWKY7xknIn-d3LsqTQGqoqVGOZfho4ecxWY8GviUQ2u7QDa7YRXBuY-SzAewsPrhiXwyS5G0aFJThhU1ymDb7YzYE_-afBmPD8Ex7EocSb7xFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a15cea3880.mp4?token=eZ32zuemNTIK0yrsN6PpUm9X7n72vHt4730sLRaJZEc80DflcAHthj0jpj3STh2BOTywhOcp2uW2Jf2elmKTBn5EDQMQmElxtRPib6GWT2elDNELX9owh6MuEwaO4zb4tlh2ZAK_pqh2Smdu7KcZErJ2yxZWWxvJPOtwueQsQpuYW-gyUJNCFhdYSac_4TVGLfmdxopSS77mk1cGnYPYm0vmptJFLVWUzOwDKGZaQWKY7xknIn-d3LsqTQGqoqVGOZfho4ecxWY8GviUQ2u7QDa7YRXBuY-SzAewsPrhiXwyS5G0aFJThhU1ymDb7YzYE_-afBmPD8Ex7EocSb7xFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نورتروپ گرومن سامانه دفاعی
«AN/AAQ-24 LAIRCM»
را برای هواگردها توسعه داده است؛ سامانه‌ای که برای مقابله با موشک‌های حرارتی و دوش‌پرتاب طراحی شده و به‌صورت خودکار با استفاده از لیزر، جستجوگر موشک را منحرف می‌کند تا به هدف نرسد.
رسانه‌ها آن را به تهدیدهای منطقه‌ای علیه هواگردهای آمریکایی و اسرائیلی در خاورمیانه وصل می‌کنند. نورتروپ گرومن می‌گوید همکنون این فناوری روی بیش از ۱۵۰۰ هواگرد از ۸۵ نوع مختلف به کار رفته است.
@withyashar</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/withyashar/13642" target="_blank">📅 22:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13641">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3cd7dfbe.mp4?token=W7K1Y00llGlYJ5KXG04uRuZRHLg-CdXJTDCSjPQYN5z9O2uYEB1PJ4dGy_EIx8jZx4o5jal6LxQ7fX7LB9EK9ljxuaO-pJZqTjLHSfCVwKhIrVForlayv_YiGmJDzCqP8EDgW3GzvQbZOU0ek3qMUMocfTig34Iznue011nIoKEzxnjdvKLPQp2fhjTOfEP1FI_TIB0IxF_VH0kMOZLIfbGpSKJ5GSoAOCHkAFG1t23EA71fd2kcFrJdHi2VOsWjebp00O_mRNmCbTo6KzBJqq-w68lkyvSik248ekgNmkMQiU59MoncwgxVTlSEV-L3W81tYCxOneTbW8qm3peiwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3cd7dfbe.mp4?token=W7K1Y00llGlYJ5KXG04uRuZRHLg-CdXJTDCSjPQYN5z9O2uYEB1PJ4dGy_EIx8jZx4o5jal6LxQ7fX7LB9EK9ljxuaO-pJZqTjLHSfCVwKhIrVForlayv_YiGmJDzCqP8EDgW3GzvQbZOU0ek3qMUMocfTig34Iznue011nIoKEzxnjdvKLPQp2fhjTOfEP1FI_TIB0IxF_VH0kMOZLIfbGpSKJ5GSoAOCHkAFG1t23EA71fd2kcFrJdHi2VOsWjebp00O_mRNmCbTo6KzBJqq-w68lkyvSik248ekgNmkMQiU59MoncwgxVTlSEV-L3W81tYCxOneTbW8qm3peiwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین الان بابل پهپاد شناسایی دیدن با کلاشینکف دارن میزنند
🥴
@withyashar</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/withyashar/13641" target="_blank">📅 21:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13639">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مهر: صدای انفجار در خارگ مربوط به خنثی سازی مهمات است
@withyashar</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/withyashar/13639" target="_blank">📅 21:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13638">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLgoEMJChIjogF-UOLubZ860R_5wl8HcVMc8z0l6zn0ENI4yNzxNbyBXqFoGX0p7EsnzkzvqxnnzKMUDVox83WRjHpjo6C8whkrMUh8TT-bU_8-B4u3yLrVoeD0X9b-LCwsymBkc_kYFTIHI_1bocuHZHrf8cXtkIVjrkyXK9fLO72m2au3pg4rDvnb9S2R7-WY5CUa25D07ede1KWS7WPrxymf0EF8mB66jN92R_zqzBcj8TL8sR5oP9WEppN4So-3PjwTUtQgBw0TuHw2kwlo4i9iLH1ZFhY_7NbrMRbC9Po0Vr9o2ulTKOUWTQbS5Qrs-Efb23n7LXjG9Wq9kJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار وزرای کشور ایران و پاکستان
@withyashar</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/withyashar/13638" target="_blank">📅 21:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13637">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کامنت رو رفتم زیر پست جدید پیج دوم شاهزاده   https://www.instagram.com/reel/DZQKl3sRlmS/?igsh=NzNsemFkNW9lcml0</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/withyashar/13637" target="_blank">📅 21:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13636">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/withyashar/13636" target="_blank">📅 21:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13635">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کامنت رو رفتم زیر پست جدید پیج دوم شاهزاده
https://www.instagram.com/reel/DZQKl3sRlmS/?igsh=NzNsemFkNW9lcml0</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/withyashar/13635" target="_blank">📅 21:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13634">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d77683181b.mp4?token=Y4gY1Vad3aDJbnn4ISHt5_xugJMFx3fJ7v3ONc0ag_08bsgGbGu6Ppx5SGAu27g3KIqKTodMgWK0LyB777USSNnFt0PHmAs3GxLGqFsn_3ErKHmuj77bXMUQnQpxjNXPWhQmPN2GBeqhqLgKOi5OjIL-jjMkEDdEJzfWOtxzgNkB2057Pxgrq59M-sbXVnX0d0ZBvCPCZKRNg-r6C9n86N5KGGlCc3T9rK_WrNSYnJbyuFCknzt5S7FRh03fpHr4gmhHDdAjtcLMpqbAUwPK2xng-UBi7LvnUKaNuXmUMfqVS8dNdlq6gKhbxyJmny3J_0X48LPucggZEsW6fEf6zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d77683181b.mp4?token=Y4gY1Vad3aDJbnn4ISHt5_xugJMFx3fJ7v3ONc0ag_08bsgGbGu6Ppx5SGAu27g3KIqKTodMgWK0LyB777USSNnFt0PHmAs3GxLGqFsn_3ErKHmuj77bXMUQnQpxjNXPWhQmPN2GBeqhqLgKOi5OjIL-jjMkEDdEJzfWOtxzgNkB2057Pxgrq59M-sbXVnX0d0ZBvCPCZKRNg-r6C9n86N5KGGlCc3T9rK_WrNSYnJbyuFCknzt5S7FRh03fpHr4gmhHDdAjtcLMpqbAUwPK2xng-UBi7LvnUKaNuXmUMfqVS8dNdlq6gKhbxyJmny3J_0X48LPucggZEsW6fEf6zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش فعالیت جنگندهای ناشناس در آسمان بندرعباس
🚨
@withyashar</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/withyashar/13634" target="_blank">📅 20:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13633">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/withyashar/13633" target="_blank">📅 20:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13632">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a6234155d.mp4?token=flxsIbmjffuaym_-_Nz9tZow3VLJjs062SWhNkfay2sciGJk0JQsMFb7fmYxejG6UKNh5aw4ngd5ljhl8ujoJTaXE5TpyaYaNwGTSA6CTav0IAm2OFrDN4JGKwlb9VBO5-rqzPJINeDyPjaYAnQPqWFe5WzJUTgzAcc7iDajfIf27d0JtS2hhh7Bv4miQMG1L9XM8VIeUBgixYFEsOe4JmHXBbZgrPdo8GPDtmxQJngUG42Ws61kFxzXXv3nZjPQo3P43hfIZJNnQiv_93b8ynK16gMpFl9SrVEFOL9GsSYqdh6UBMF4f_hxJFyeBzRBWNODOZkAp4uZ7B_j6w9c3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a6234155d.mp4?token=flxsIbmjffuaym_-_Nz9tZow3VLJjs062SWhNkfay2sciGJk0JQsMFb7fmYxejG6UKNh5aw4ngd5ljhl8ujoJTaXE5TpyaYaNwGTSA6CTav0IAm2OFrDN4JGKwlb9VBO5-rqzPJINeDyPjaYAnQPqWFe5WzJUTgzAcc7iDajfIf27d0JtS2hhh7Bv4miQMG1L9XM8VIeUBgixYFEsOe4JmHXBbZgrPdo8GPDtmxQJngUG42Ws61kFxzXXv3nZjPQo3P43hfIZJNnQiv_93b8ynK16gMpFl9SrVEFOL9GsSYqdh6UBMF4f_hxJFyeBzRBWNODOZkAp4uZ7B_j6w9c3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/withyashar/13632" target="_blank">📅 20:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13631">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/withyashar/13631" target="_blank">📅 20:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13630">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yk5TAG6x6Wv_jhWmbGVectuSAI-f3cSVGZIKc4WoVc0NTgFN5dYj4wFLlb9MSVHAx1X5ThyGStp7Vk84Mtgloar4joGKoSQafxdABFMyUi1UKOFmZlRcjeTEFLZbZWWyi6Ut0UG7O4mEyMWMz2DX8EZga0I_2zoFZfSBgp5dg0-wRTdtiQNvZcrIgghod29_TY9fVjhArNytWt_JQzSauSug2lkLRx2qh7OMWgHX8Aar7fpp0AnQ1c-rVJGEBytwukslV8Wu5WOaxIV0LhyPQgvHb5xeRxc4lVP3shRCb-y4fc7AU38TetfMlorOhz8-0v9Rj3Q1BuL00tVoHm-dmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ایران و بستن تنگه هرمز، به صادرات تکنولوژی‌های پاک چین مانند باتری، خودروی برقی و ... منجر شده و به بیشتر از ماهی ۲۰ میلیارد دلار رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/withyashar/13630" target="_blank">📅 19:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13627">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">العربیه:
ترامپ به میانجی‌ها اطلاع داد که مذاکرات با ایران بیش از 60 روز ادامه نخواهد داشت که این مهلت در روز های آینده به پایان می‌رسد و ایران باید به‌سرعت پاسخ دهد.
« این خبر فیکه که پخش شده »
@withyashar</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/withyashar/13627" target="_blank">📅 18:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13626">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d35551fc6.mp4?token=LhJerVz967QOzlYqgHYrRJAS0ol73U8vkmC3EfYcKOglskixqP1bQla27znj4t6yLgzOJ--dWQtmz9C-WTrcvQT-2iD8knw9cp5fa6hVVk2hVzrSIvyJ7F6YxW8xk4Jp4Olk-WrSMEv08MJQq_tUi3f0LE7uBBB1zppYsfoLrn6mNkIgwjgrOIdqAIOMbqSzB_HBGaBC3juvt0DtRu5TSgGuH8RjuzLAAOJGnBEb5nC70M2HUWHyA_lhmbIuZD4-r5NY-R63oFdyqa9XumBdH1DxnumSKxx6czni6qhHoKBKb02FYe4PnFRa_yr2kBtzuMz6bBM-YF8iq-XAPFneRmzDIHT5OlkV_vxu2V41zyfWMpg_BfouJyKR1SEKUsZ3ZGDBT8d-cETFGPtBFZPZx1-Ju_2bEXbi1jPng-WMw-U5pqBBejJHLv48njoqRxYz2YCSifvX2BXOduTAo7w-g1k-qqgkCyZV2RluCPQTc2dZsNTzYqxM0xfk7xL6ZaSyfngexWoLtchoh9_-_sJNrrSLwESXdEymT5y-lllje_YGcFXCX0zogX6nxqoVWL6trcGHRaKeRnZfQLczL462CTYOgNxb5QMtodIqlQO2ta6i11ZqEPPinqg4oFy9gH2IsVUyfyUwNCxeWa5FDwqe26ZaHKTAV6j0IDgYx4TnIZI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d35551fc6.mp4?token=LhJerVz967QOzlYqgHYrRJAS0ol73U8vkmC3EfYcKOglskixqP1bQla27znj4t6yLgzOJ--dWQtmz9C-WTrcvQT-2iD8knw9cp5fa6hVVk2hVzrSIvyJ7F6YxW8xk4Jp4Olk-WrSMEv08MJQq_tUi3f0LE7uBBB1zppYsfoLrn6mNkIgwjgrOIdqAIOMbqSzB_HBGaBC3juvt0DtRu5TSgGuH8RjuzLAAOJGnBEb5nC70M2HUWHyA_lhmbIuZD4-r5NY-R63oFdyqa9XumBdH1DxnumSKxx6czni6qhHoKBKb02FYe4PnFRa_yr2kBtzuMz6bBM-YF8iq-XAPFneRmzDIHT5OlkV_vxu2V41zyfWMpg_BfouJyKR1SEKUsZ3ZGDBT8d-cETFGPtBFZPZx1-Ju_2bEXbi1jPng-WMw-U5pqBBejJHLv48njoqRxYz2YCSifvX2BXOduTAo7w-g1k-qqgkCyZV2RluCPQTc2dZsNTzYqxM0xfk7xL6ZaSyfngexWoLtchoh9_-_sJNrrSLwESXdEymT5y-lllje_YGcFXCX0zogX6nxqoVWL6trcGHRaKeRnZfQLczL462CTYOgNxb5QMtodIqlQO2ta6i11ZqEPPinqg4oFy9gH2IsVUyfyUwNCxeWa5FDwqe26ZaHKTAV6j0IDgYx4TnIZI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ در تروث
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/13626" target="_blank">📅 16:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13625">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkV0rVsLRey94qqvoZrx2xTcFQarjoXeZ85sU8paLlvlnjoIz2hikpCct4hrOQl8Nppk2Q4Bl1VA5EyLpgNQ8NT76bpxLyn0D3nzXsvQpyG_jQTS44zzgCYZfzY-XN4r_kKyrghPS0bg5TgntCSdOtaqn06-hqZwT5hL4iUcgaAg0dGq8JxXnP-D4OjvghhBFGtCr861xrK6j-kncBDixoM69BT1qAgmlxtJUHiZY-gVGAkQmn29krebZn7uyX5RfDY9Vnr4RH4N7ticN41NYIlvfUZwRCbStIn7Wh9Y7XOhnP2uX4m0yhi9HsgKFEjDL7yREarbTu061HH_yaamzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکل مخابراتی پایگاه شهید راهبر نیرو دریایی سپاه در بندر سیریک که شب گذشته، هدف پرتابه‌های آمریکایی قرار گرفت
پیش‌تر اسکله این پایگاه در طول جنگ هدف بمباران آمریکایی ها قرار گرفته بود.
@withyashar</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/13625" target="_blank">📅 15:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13624">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وزرای کشور کشورهای عضو شورای همکاری خلیج فارس (GCC) جلسه اضطراری تشکیل می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/13624" target="_blank">📅 15:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13623">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مدیرعامل آسیاتک: اینترنت دیتاسنترها همچنان قطع است
مدیرعامل شرکت آسیاتک، با اشاره به تداوم مشکلات دسترسی به شبکه در بخش‌های تخصصی، اعلام کرد که برخلاف برخی اظهارنظرها مبنی بر بازگشت وضعیت اینترنت بین‌الملل به شرایط پیش از دی‌ماه سال گذشته، دسترسی مشتریان مراکز داده (دیتاسنترها) همچنان برقرار نشده و کسب‌وکارهای اینترنتی کماکان با چالش مواجه‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/13623" target="_blank">📅 15:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13622">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ به میانجی‌ها گفته ایران باید زود جواب بده
@withyashar</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/13622" target="_blank">📅 14:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13621">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">الحدث: ایران خواستار مذاکرات سه‌ماهه درباره جزئیات پرونده هسته‌ای است
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/13621" target="_blank">📅 13:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13620">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">صدای انفجار قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/13620" target="_blank">📅 13:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13619">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">(IG @yashar)‎⁨منتظریم کی شب حمله فرا می‌رسد⁩</div>
  <div class="tg-doc-extra">اتاق جنگ با یاشار (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/13619" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/13619" target="_blank">📅 13:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13617">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وزیر کشور پاکستان(
سناتور سید محسن رضا نقوی
)امروز به تهران می‌آید تا تلاش کند در مسئله دارایی‌های ایرانی مسدود شده، پیشرفتی حاصل شود
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/13617" target="_blank">📅 12:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13616">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8d357648b.mp4?token=HyF3VRf3gzB3XciSVQpEql8v3KXQX2CUpbsE2-hzEW17L7MkYtFLU_r94nRQ8ejdjxscVrAsSmRwtmrJzn9OVUU_AR2ONYOSAtTXmJ3Px6ql40th55VtVIWudYYtLt-mLrLWlzlfexCNdkoUKNFpudikim5lOe_XFlI2qSIQSK3NZmv5cYsYjL2D2PRH4WF3Z9L6J5QjJ8WqE90rpuV_equhz4HjCwrq2c3JBemLPupqZgd3Yn3g54_5ETqfRqgqEvNQPa0FFJwAiNfd_qzZRXZ4vr_UBuykuatEE__s5IEpX2ecHLRYpJMsuyfi2d--LVtZx3rTW1lR_Kmlo7uJFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8d357648b.mp4?token=HyF3VRf3gzB3XciSVQpEql8v3KXQX2CUpbsE2-hzEW17L7MkYtFLU_r94nRQ8ejdjxscVrAsSmRwtmrJzn9OVUU_AR2ONYOSAtTXmJ3Px6ql40th55VtVIWudYYtLt-mLrLWlzlfexCNdkoUKNFpudikim5lOe_XFlI2qSIQSK3NZmv5cYsYjL2D2PRH4WF3Z9L6J5QjJ8WqE90rpuV_equhz4HjCwrq2c3JBemLPupqZgd3Yn3g54_5ETqfRqgqEvNQPa0FFJwAiNfd_qzZRXZ4vr_UBuykuatEE__s5IEpX2ecHLRYpJMsuyfi2d--LVtZx3rTW1lR_Kmlo7uJFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همکنون پرواز هواپیمای اف-۵ ئی
تایگر ۲( تک نفره )متعلق به هوانیروز جمهوری اسلامی برفراز مشهد
@withyashar</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/13616" target="_blank">📅 12:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13615">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dA_sLc83uWf4ZByTzNIobycm-WSJxcfo5hNL6AXkR3vuqJCKUPl5SsgSr3uwU3YDtxDzBroYigt25R2UrQQmvzoVHAOS6URJegOVB6VDNBoytND8WbilBP1OJX8uxMvHXSoHcDIT_6vvzEIAyNqYVmQ6ZJdrbljJq57y4WE2nA3JDX2mB67yGpbuXaZ_QBaYVMFrE5NR9YnsslrpIR_MHjI68DUsS-KN8-o6JwoT9JbYzw519XmTEXC4KbZIHbf1jDM5TKAKK38Jtk6UkyXVpRyNWMV-f-UE8x19fBVXfeN8Ka060rEfk_7Rh1dxFkrVhlxOLx6uQfKLcHoPF3PPbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس های جدید پایگاه هفتم شکاری شیراز بعد از جنگ
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/13615" target="_blank">📅 11:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13614">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ورزش سه :  آمریکا به 15 نفر‌ از اعضای تیم‌ ملی ویزا نداده و رفتن ایران به جام جهانی در هاله ای از ابهام‌ قرار‌گرفته.
رویترز : کسایی که ویزا نگرفتن برخی از مربیان و هیئت همراه هستن وگرنه تمام بازیکنا ویزا گرفتن.
آمریکا اعلام کرده اجازه نمیده افراد غیرورزشی به بهانه ورزش به آمریکا بیان
@withyashar</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/13614" target="_blank">📅 10:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13613">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سنتکام: ۷ موشک بالستیک ایران به سمت کویت و بحرین شلیک شد
فرماندهی مرکزی ایالات متحده (CENTCOM) اعلام کرد ایران هفت موشک بالستیک به سمت کویت و بحرین شلیک کرده است.
بر اساس ادعای سنتکام، شش موشک توسط سامانه‌های دفاعی رهگیری و منهدم شده و موشک هفتم نیز به هدف مورد نظر خود نرسیده است. سنتکام همچنین اعلام کرد هیچ آسیبی به نیروهای آمریکایی وارد نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/13613" target="_blank">📅 10:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13612">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ba7b496b.mp4?token=sCX-m_dbTdj0ApT7cYk3Gb4ov0jr1OOAndzK163_0w1U2-xhsWlfJfgghj2OnCpbpAbBy5qEeTtPlfCvSChXwIHDEMFkwAhYXD5upJwZ1oIthhnizvJxKUNBFBFkW0v9i5zQOyQJW1o6NCNuAioaGVEUKhkmUrwiAzz3XHO7Cmx1IhouBiF1n5xeluJWqS_aefymnPZSCT7pV5C2MQb9LW1v6YMymrJCTI8IGgQxXq9kt2gO-_L5pIY8mp2n7u1WcnJLiJOvfPoP2jv8KTUB_zYfpx1lCmKDrYFhY7Ez-sqjWVRTPET1tmQd3ewKANgueDh_sP5cs6GJPNRfraqxbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ba7b496b.mp4?token=sCX-m_dbTdj0ApT7cYk3Gb4ov0jr1OOAndzK163_0w1U2-xhsWlfJfgghj2OnCpbpAbBy5qEeTtPlfCvSChXwIHDEMFkwAhYXD5upJwZ1oIthhnizvJxKUNBFBFkW0v9i5zQOyQJW1o6NCNuAioaGVEUKhkmUrwiAzz3XHO7Cmx1IhouBiF1n5xeluJWqS_aefymnPZSCT7pV5C2MQb9LW1v6YMymrJCTI8IGgQxXq9kt2gO-_L5pIY8mp2n7u1WcnJLiJOvfPoP2jv8KTUB_zYfpx1lCmKDrYFhY7Ez-sqjWVRTPET1tmQd3ewKANgueDh_sP5cs6GJPNRfraqxbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام ویدئوهای حمله به سایت‌های رادار ساحلی‌ایران در سیریک و جزیره قشم را منتشر کرد و
کفت
حملات تلافی‌جویانه ایران به بحرین و کویت رهگیری شده است
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/13612" target="_blank">📅 10:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13611">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ارسالی : من بابامم تعریف میکرد که زمان جنگ عراق و کویت صدا های بمب هارو میشنیدن خرمشهر
@withyashar
گزارش های زیاد از شنیده شدن انفجار کویت از خرمشهر !</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/13611" target="_blank">📅 04:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13610">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBX6F8AVpCtxeGqbr2axo2ebcrLpDNiy81BjOvjeGu4H5dxRdTJkemha-JWfNyP6Sy7suk3m4sFOHUu6ECPeJTFNbgoOVw2hg3o_hA1TFV-9-exN1PNZ4myLq89z9WSphVfqCejaYJ834g0fRyVEQ0Pyzv0BcxJNDQ26R_QDcrrcyASATYlw7CfLQnwz_QFxZfYDIZZ_0ZlG87mewft-TL6Efv6uIiASf_QCRbNdzG3GBS97vF0eTD-nRJWqA4LTtTNcJuKOP9MZ9j9Y7O_QJ2l73EShIgTCNtQ-R2ZMwO-u3mq1Mdu4M7AYjHdAJxXNcXAutucpQQaEN31lHNBOng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی : کویت آلارم اومد الان ، ۳پا موشک زده سمتش !
@withyashar</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/13610" target="_blank">📅 04:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13609">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622170a597.mp4?token=armPFxFBawHIK7P3PPDeP00k69dagBQucZPrT1gJ-D3uNWnbgc6nuPcl6pysWGrqZepF3HnaCZU3J6XwuBMmFEyUonKAKN5wDlHPBqKe0CSxGV50eKeqxgrBQVe27Dmz_JM6kgAYu4x_w58XTyNzi_utR9jZDpTm0A0TNSdcRYUQ6aImTpLW_KUtLlWSBt6o7fczRxck4fr-HBZbAFh1wZbKjoT-HVcLDaRZ_j69CG7THOsYGkCqEQpH_dyGakKTx3IuzRGPm8chl3H5bAxC7t5qLouAHkXZpFadMOJcS8NQyYd4NIWQmUyOUukuXm4s44NdoT8q5eFYlKB_TLUpMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622170a597.mp4?token=armPFxFBawHIK7P3PPDeP00k69dagBQucZPrT1gJ-D3uNWnbgc6nuPcl6pysWGrqZepF3HnaCZU3J6XwuBMmFEyUonKAKN5wDlHPBqKe0CSxGV50eKeqxgrBQVe27Dmz_JM6kgAYu4x_w58XTyNzi_utR9jZDpTm0A0TNSdcRYUQ6aImTpLW_KUtLlWSBt6o7fczRxck4fr-HBZbAFh1wZbKjoT-HVcLDaRZ_j69CG7THOsYGkCqEQpH_dyGakKTx3IuzRGPm8chl3H5bAxC7t5qLouAHkXZpFadMOJcS8NQyYd4NIWQmUyOUukuXm4s44NdoT8q5eFYlKB_TLUpMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ در‌تروث : نیروی دریایی ایران
@withyashar</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/13609" target="_blank">📅 03:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13608">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda12e11f6.mp4?token=i0RzWZ8UNgednUqtdaQ4lPrOlobLMuc3cUkpkdrK5GPq11J0YsvPHwW9YVOz6vxafevrAqj5XvIBYRuMqjIvuKR6GZkxUPmev_Af71GRDGK480HPxlZSGKJ6-_L2X7NXXM-l6YSm2i3bpdCNEmsQhVWyk4Q9Za8hoRSdRle4TIUyWZKeKr_P70P7ms-iVLtc7ZuxEZmQ4OBkSYex9-Ava7laIEe9UhRMCoSPKCGk06kz3D4EvII1xzNflW0HGiwaYoGNBGKWqzww_UCdzJE6FaGz8JPsoxCkPszGq6kfqQahjJmxgDn2pfCSUeJyLr9i4zkbmQ7gAtoPdYSGP1RkhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda12e11f6.mp4?token=i0RzWZ8UNgednUqtdaQ4lPrOlobLMuc3cUkpkdrK5GPq11J0YsvPHwW9YVOz6vxafevrAqj5XvIBYRuMqjIvuKR6GZkxUPmev_Af71GRDGK480HPxlZSGKJ6-_L2X7NXXM-l6YSm2i3bpdCNEmsQhVWyk4Q9Za8hoRSdRle4TIUyWZKeKr_P70P7ms-iVLtc7ZuxEZmQ4OBkSYex9-Ava7laIEe9UhRMCoSPKCGk06kz3D4EvII1xzNflW0HGiwaYoGNBGKWqzww_UCdzJE6FaGz8JPsoxCkPszGq6kfqQahjJmxgDn2pfCSUeJyLr9i4zkbmQ7gAtoPdYSGP1RkhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همکنون
جت‌های جنگنده آمریکایی در حال پرواز بر فراز استان بصره عراق نزدیک مرز ایران هستند.
@withyashar</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/13608" target="_blank">📅 03:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13607">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea974c1bb.mp4?token=ufy_3o-l-pbCBb3Muw76lzNVZRa7618-dj5kYQGw-zLcVpHU7r9xdofh6mN2_THh55Z5VkolMRNl4XoTmLhkVtpE1j2p80N8wOBSah-YzPxTfidTKylFN5X_75zgTcxAIs_QMdMfMS4iULRgEU0_qyOhAt0FfgFArAO2SBgYfob8Lct6ieB7xi-A41Joa7jbyQ6pO-nMtjZL_0BXkA2a33uk7bq5-aHTlKETHVYPDefclCkjbN8Mk6UMsoXpNe7qyxgDRpTrAqv5kMkSL_k9J27SoRgDiUUDThzMp_sfMynnMezVgW8Ykgy75t9T5sIewSt0xhvVjqw6gUr8_JxBSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea974c1bb.mp4?token=ufy_3o-l-pbCBb3Muw76lzNVZRa7618-dj5kYQGw-zLcVpHU7r9xdofh6mN2_THh55Z5VkolMRNl4XoTmLhkVtpE1j2p80N8wOBSah-YzPxTfidTKylFN5X_75zgTcxAIs_QMdMfMS4iULRgEU0_qyOhAt0FfgFArAO2SBgYfob8Lct6ieB7xi-A41Joa7jbyQ6pO-nMtjZL_0BXkA2a33uk7bq5-aHTlKETHVYPDefclCkjbN8Mk6UMsoXpNe7qyxgDRpTrAqv5kMkSL_k9J27SoRgDiUUDThzMp_sfMynnMezVgW8Ykgy75t9T5sIewSt0xhvVjqw6gUr8_JxBSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشتک نیم وارو پهپاد های شناسایی اسمون بندر عباس همین الان
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/13607" target="_blank">📅 03:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13606">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/13606" target="_blank">📅 03:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13605">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/13605" target="_blank">📅 03:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13604">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb45455c0d.mp4?token=ehvn3EKqufXOHeTSeTZM07URsn2KEAtHJxt83u8q5aENiEinL_k8p8nVgrgflMdqu4wYT6Oft1oYWWRCAY1BZKdFHYRvymWfdDZXNU-5hb2mM4I92NgiQk50uSpXZBddge-X0zk8PuyByFputwggHYRFNIZ_njoqhQUVdOL7nlJYtvjnXgBqCNLQ6DRxbYe8BpacUxWK4CWd5hOUs-ezHw0GyND3SiZPlUtrIGfDQW18YZ94DcyiPX4YnvSFHiIGtqoW61Cstnch7B-f3H2gn306pc2agJ371nyoM3MG1h2wA5oTFnQhPaIYAYGSJdskXFDaR4PXHDb84ipQMLEZvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb45455c0d.mp4?token=ehvn3EKqufXOHeTSeTZM07URsn2KEAtHJxt83u8q5aENiEinL_k8p8nVgrgflMdqu4wYT6Oft1oYWWRCAY1BZKdFHYRvymWfdDZXNU-5hb2mM4I92NgiQk50uSpXZBddge-X0zk8PuyByFputwggHYRFNIZ_njoqhQUVdOL7nlJYtvjnXgBqCNLQ6DRxbYe8BpacUxWK4CWd5hOUs-ezHw0GyND3SiZPlUtrIGfDQW18YZ94DcyiPX4YnvSFHiIGtqoW61Cstnch7B-f3H2gn306pc2agJ371nyoM3MG1h2wA5oTFnQhPaIYAYGSJdskXFDaR4PXHDb84ipQMLEZvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar
منتظر زارتان زورتان</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/13604" target="_blank">📅 03:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13603">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">۳پا باید یه جوابی بده چیزی‌ دیدن یا شنیدین بگین</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/13603" target="_blank">📅 02:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13602">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">چندین انفجار در سيريك
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/13602" target="_blank">📅 02:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13601">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کانال ۱۴: همه امیدوار بودند که آتش بس برقرار شود، اما بازی به طور کامل در حال تغییر است. برای یک آخر هفته فوق العاده گرم در خاورمیانه آماده می شوند، زیرا ایران و آمریکا از اعتصابات تصادفی شبانه به رویارویی های روز روشن تغییر می کنند!
@withyashar</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/13601" target="_blank">📅 02:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13600">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سنتکام : چند لحظه پیش، نیروهای سنتکام چهار پهپاد تهاجمی یک‌طرفهٔ ایرانی را که به سمت تنگهٔ هرمز پرتاب شده بودند، سرنگون کردند. این پهپادهای تهاجمی تهدیدی فوری برای تردد دریایی منطقه ایجاد کرده بودند. در ادامه، نیروهای آمریکا برای دفاع در برابر حملات بیشتر، سایت‌های رادار مراقبت ساحلی ایران در گورک و جزیرهٔ قشم را هدف قرار دادند.
نیروهای آمریکایی همچنان هوشیار هستند و برای پاسخ‌دادن به تجاوز بی‌دلیل ایران در چارچوب دفاع از خود، در حالت آماده‌باش قرار دارند.
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/13600" target="_blank">📅 02:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13599">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
سنتکام از حمله به سایت های راداری قشم خبر داد!
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/13599" target="_blank">📅 02:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13598">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">چندین انفجار در سيريك
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/13598" target="_blank">📅 02:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13597">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سی‌بی‌اس نیوز به نقل از یک مقام آمریکایی: نیروهای آمریکایی حداقل ۴ پهپاد را که توسط ایران به سمت تنگه هرمز پرتاب شده بود، سرنگون کرده‌اند.
🚨
@withyashar
بچه جنگ شده باز</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/13597" target="_blank">📅 02:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13596">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⚠️
@withyashar
گول نخوری !</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/13596" target="_blank">📅 01:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13595">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فقط در ۴ ماه ! بسوزید عرزشی ها</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/13595" target="_blank">📅 01:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13594">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">💥
290k عرزشی سوز ترین کانال تلگرام</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/13594" target="_blank">📅 01:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13593">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گزارش هایی از قطع شدن اینترنت
@withyashar</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/13593" target="_blank">📅 01:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13592">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سی ان ان : منابع می گوید ایران چندین پهپاد را به سمت تنگه هرمز پرتاب کرده است. نیروهای ایالات متحده حداقل 3 تا از آنها را رهگیری کردند
@withyashar
🚨</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/13592" target="_blank">📅 01:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13591">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دوتا صدای انفجار الان ومد همین الان قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/13591" target="_blank">📅 01:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13590">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مجری ان‌بی‌سی: رهبران جمهوری اسلامی معتقد نیستن که به‌طور کامل شکست خوردن.
ترامپ: ایران به دلیل تصور برخورداری از قدرت کافی، از امضای توافق خودداری کرده. ایران در نهایت گزینه‌ای جز توافق نخواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/13590" target="_blank">📅 01:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13589">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ به ان بی سی:
خیلی از مقاماتشون مغرورن، یه سری کارها هست که هیچوقت فکر نمی‌کردن مجبور بشن انجام بدن ولی الان مجبور شدن، راه دیگه‌ای ندارن و این قضیه زمان می‌بره.
داریم درباره 47 سال حرف میزنیم که هر کاری خواستن انجام دادن.
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/13589" target="_blank">📅 01:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13588">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ به NBC : وضعیت برای اونا واقعاً سخته
یه جورایی استقلال زیادی هم دارن، ولی سال‌ها با یه رهبری ضعیف و بی‌اثر از طرف آمریکا و بعضی کشورهای دیگه طرف بودن؛
طوری که عملاً گذاشتن هر کاری دلشون خواست بکنن.
من فکر می‌کنم خودشون هم الان باورشون نمی‌شه به اینجا رسیدن؛ جایی که عملاً خیلی ضعیف شدن
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/13588" target="_blank">📅 01:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13587">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ به شبکه ان بی سی: رهبران ایران چاره ای جز رسیدن به توافق ندارند‌‌
@withyashar</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/13587" target="_blank">📅 01:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13586">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ به شبکه ان بی سی: ایران بین 21 تا 22 درصد موشکهای خود را در اختیار دارد‌‌ @withyashar</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/13586" target="_blank">📅 01:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13585">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ به شبکه ان بی سی: ایران بین 21 تا 22 درصد موشکهای خود را در اختیار دارد‌‌
@withyashar</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/13585" target="_blank">📅 01:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13584">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">به نظر می‌رسد جنگنده‌های اسرائیلی از عراق به سمت ایران می‌آیند
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/13584" target="_blank">📅 01:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13583">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ارسالی : پدافند ۱۷ شهریور گنبد کاووس فعال شد @withyashar</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/13583" target="_blank">📅 01:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13582">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ارسالی : پدافند ۱۷ شهریور گنبد کاووس فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/13582" target="_blank">📅 01:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13581">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">به خبرای هست ولی نمیتونم ثابت کنم</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/13581" target="_blank">📅 01:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13580">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/13580" target="_blank">📅 01:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13579">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گزارشهایی از صدای جنگنده و پدافند در شمال کشور
🚨
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/13579" target="_blank">📅 00:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13578">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ: ما خیلی سریع از ایران خارج خواهیم شد و نتیجه آن، به هر شکل، بسیار قوی خواهد بود؛ چه از طریق یک تکه کاغذ (توافق) و چه از راهی بسیار سخت‌تر. شاید حتی راه بسیار سخت‌تر، آسان‌تر هم باشد.
اما ما از این مسئله عبور خواهیم کرد و قیمت کود شیمیایی شما به‌شدت کاهش خواهد یافت، درست همان‌طور که چهار ماه پیش بود. قیمت کود شیمیایی اکنون هم کاهش یافته است.
قیمت انرژی، نفت و گاز نیز همگی به‌طور قابل‌توجهی پایین خواهند آمد. و صادقانه بگویم، من تصور می‌کردم قیمت‌ها بسیار بیشتر از این افزایش پیدا کنند.
@withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/13578" target="_blank">📅 00:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13577">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گزارش های تایید نشده : چندین جت جنگنده آمریکایی حمله‌ای را به بندرعباس و مناطق اطراف جزیره خارک آغاز کردند و چندین بندر از جمله فرودگاه بندرعباس را هدف قرار دادند. پدافند هوایی فعال شد و درگیر نبرد شدیدی با جت‌های جنگنده شد.
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/13577" target="_blank">📅 00:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13576">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گزارش هایی از شلیک نیروهای ایرانی به سمت ناو های آمریکایی
🚨
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/13576" target="_blank">📅 00:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13575">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شنیده شدن صدای انفجار در جزیره خارک
🚨
@withyashar</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/13575" target="_blank">📅 00:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13574">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">@withyashar
only for pro members</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/13574" target="_blank">📅 00:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13573">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">@withyashar
operation economic fury</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/13573" target="_blank">📅 00:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13572">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/13572" target="_blank">📅 00:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13571">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انفجار ناشناس در نزدیکی کنسولگری ایران در استان سلیمانیه در شمال عراق.
@withyashar</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/13571" target="_blank">📅 23:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13570">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyzdhrfTu0eFuWIuAJhrVccCrbJBACJUyEu7UtRTiyQbHOXR64WNRGGLe9nK-ryneCJaaT1-bnLpFLz0IyhNduopuOmzIfRR6rL5bGeRBcvOmT1ZwCBZmxM9Z3uQAX4n4KCPFjFeAdFdeFmBZJpleA8zCkdZHkKqzHBcM7_O1T9NoHbmOiU0Ufe-H-4oF6d37hCkH74oS2dKFyWXOthekLpEuOo-tbzNRn81ATiPVUEBePPty7JePOHzcKfVKunstcBnVxUN93ZmgjJdVthJmhH1fGDqnibT1OPp0zbnufIpOU9ATCnjCLwcMCdTGXyfrQOITXuBeMzTDEAV2VDCfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواستگاری جنجالی قیصر از الهام چرخنده در تجمعات حکومتی
قیصر در یکی از تجمعات حکومتی، به‌صورت علنی از الهام چرخنده، بازیگر سابق تلویزیون ایران، درخواست ازدواج کرد. این اتفاق غیرمنتظره خیلی زود در فضای مجازی و رسانه‌ای مورد توجه قرار گرفت و واکنش‌های زیادی را به دنبال داشت
@withyashar</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/13570" target="_blank">📅 23:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13569">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شبکه ۱۲ اسرائیل به نقل از رئیس ستاد ارتش این رژیم: قصد نداریم از سرزمین‌هایی که در لبنان پیشروی کرده‌ایم، خارج شویم
@withyashar</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/13569" target="_blank">📅 22:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13568">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اکسیوس: استیو ویتکاف و جرد کوشنر به طور مخفیانه از تأسیسات هسته‌ای اوک ریج در تنسی بازدید کردند تا با برترین کارشناسان هسته‌ای آمریکا دیدار کنند، در حالی که مذاکرات با ایران وارد مرحله حساسی شده است. @withyashar</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/13568" target="_blank">📅 22:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13567">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اکسیوس: استیو ویتکاف و جرد کوشنر به طور مخفیانه از تأسیسات هسته‌ای اوک ریج در تنسی بازدید کردند تا با برترین کارشناسان هسته‌ای آمریکا دیدار کنند، در حالی که مذاکرات با ایران وارد مرحله حساسی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/13567" target="_blank">📅 22:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13566">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گزارشگر: بازی که شما می‌روید  ببینید ارزان‌ترین قیمت بلیت ۸۰۰۰ دلار است. مردم عادی آمریکا نمی‌توانند بلیت این رویدادهای ورزشی را بخرند.
ترامپ: می‌توانید آن را از تلویزیون تماشا کنید. تماشای آن از تلویزیون تا حدی رایگان است.
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/13566" target="_blank">📅 21:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13565">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ درباره پوتین و زلنسکی:
بگذارید خودشان حل کنند. من کسی هستم که آن‌ها را به این موقعیت رساندم.
@withyashar</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/13565" target="_blank">📅 21:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13564">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ درباره جان بولتون:
فکر می‌کردم او در زمینه جنگ رادیکال است، نه در زمینه چیزهای دیگر.
او می‌خواست با هر کسی که دهانش را باز می‌کرد وارد جنگ شود.
او همیشه می‌خواست مردم را بکشد. من هرگز به او گوش ندادم.
@withyashar</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/13564" target="_blank">📅 21:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13563">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ درباره ایران دم مسترا:
ما در رابطه با ایران موفقیت‌های بزرگی کسب کرده‌ایم.
آنها در موقعیتی نیستند که سلاح هسته‌ای داشته باشند.
ترامپ:
پیت هگستث معلوم شد که یک گوهر است.
@withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/13563" target="_blank">📅 21:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13562">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682cd2dd57.mp4?token=Mqznpuw_uiwk8CM_288Df1yCnhcAijqO3UhwGqYltYbdNA9-ig4MeEmp3yxm9QBsXjZd3S8k4FVp8ZPCCorSfLS3HRncgRFHI3pCXqLvsXkJl-mGPSJQVEt4YorCUQmrn8WArlXdKqe6GAeYMul_B7FItqM663_8my-NVdZeCg934vWdkSGxL7fOyHrTXBNLzlUP2RV5CHvY_3GCEcssJrrVjZ6zegYVMZyXSeJ7UuPXJSHesml1sPpUYasHC7Zjxi2rbG_-cTB03DwLGYpAN05iPh7hGadsGgrgQ5O3kRPX0iUTXvnlG0_vhFD3gwtpNxjMofowBhpf0nCHGxN-Zoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682cd2dd57.mp4?token=Mqznpuw_uiwk8CM_288Df1yCnhcAijqO3UhwGqYltYbdNA9-ig4MeEmp3yxm9QBsXjZd3S8k4FVp8ZPCCorSfLS3HRncgRFHI3pCXqLvsXkJl-mGPSJQVEt4YorCUQmrn8WArlXdKqe6GAeYMul_B7FItqM663_8my-NVdZeCg934vWdkSGxL7fOyHrTXBNLzlUP2RV5CHvY_3GCEcssJrrVjZ6zegYVMZyXSeJ7UuPXJSHesml1sPpUYasHC7Zjxi2rbG_-cTB03DwLGYpAN05iPh7hGadsGgrgQ5O3kRPX0iUTXvnlG0_vhFD3gwtpNxjMofowBhpf0nCHGxN-Zoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بیرون کاخ سفید با خبرنگارا حرف نزد، و قبل از سوار شدن به ایر فورس وان هم هیچ مصاحبه‌ای نکرد، ببینیم دم توالت چیزی میگه یا نه
@withyashar</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/13562" target="_blank">📅 21:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13561">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">جروزالم پست:  منابع اطلاعاتی اسرائیل معاون رئیس‌جمهور جِی‌دی ونس را متهم می‌کنند که نقشه موساد برای استفاده از نیروهای کرد علیه ایران را مستقیماً به اردوغان لو داده است، که سپس اردوغان به ترامپ فشار آورد تا آن را لغو کند. خط قرمز اردوغان: هیچ نیروی نظامی کردی…</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/13561" target="_blank">📅 20:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13560">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">جروزالم پست:  منابع اطلاعاتی اسرائیل معاون رئیس‌جمهور جِی‌دی ونس را متهم می‌کنند که نقشه موساد برای استفاده از نیروهای کرد علیه ایران را مستقیماً به اردوغان لو داده است، که سپس اردوغان به ترامپ فشار آورد تا آن را لغو کند.
خط قرمز اردوغان: هیچ نیروی نظامی کردی در نزدیکی مرزهای ترکیه نباشد.
@withyashar</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/13560" target="_blank">📅 20:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13559">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بلومبرگ: طبق داده‌های ناوبری، رفت‌وآمد کشتی‌ها از تنگه هرمز تو ۲۴ ساعت گذشته به‌شدت کم شده
@withyashar</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/13559" target="_blank">📅 20:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13558">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">️حمام خون در بازار کریپتو!  بیش از ۶۳۵ میلیارد دلار تنها در کمتر از ۵ روز از ارزش کل بازار رمزارزها محو شده است. @withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/13558" target="_blank">📅 19:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13557">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آلمان با صدور هشدار امنیتی برای شهروندانش، نسبت به سفر به خاورمیانه هشدار داد و دلیل اون رو احتمال تشدید دوباره تنش‌ها و اختلال در پروازها عنوان کرد.
@withyashar</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/13557" target="_blank">📅 18:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13556">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سنتکام:
ادعای نادرست: ایران ادعا میکنه که به سمت کشتی‌های جنگی ایالات متحده در خلیج عمان تیر هشدار شلیک کرده و کشتی‌های آمریکایی رو مجبور به «عقب‌نشینی» به سمت اقیانوس هند کرده.
حقیقت: نیروهای ایرانی به کشتی‌های جنگی نیروی دریایی ایالات متحده حمله نکرده یا به سمت آنها شلیک نکردن. انجام این کار نقض فاحش آتش‌بس خواهد بود. نیروهای آمریکایی همچنان آزادانه در آب‌های منطقه‌ای فعالیت می‌کنند و در عین حال محاصره مداوم علیه ایران رو به طور کامل اجرا می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/13556" target="_blank">📅 17:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13555">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Gloria2018Remaster(IG @yashar)</div>
  <div class="tg-doc-extra">Umberto Tozzi (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/13555" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/withyashar/13555" target="_blank">📅 17:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13554">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f252f83e0d.mp4?token=jQ46tmDLU5B_feHaVcbjJz3JW2cHhi8rzDkOB_QX4cdd_E6GdEYtCVY-d9ri_Jot072GEeSGvGM9CDPVNq3MnYTn_w1M6OBOivMSAM1jt8qTJ8hIWAFJWFV5quit40ngQJ317XejFfNH-siX1V2abSqMAIdt20VLXYSI8gyARUyyscrFvWBEFAtOl_vsFpKtmAOJ2OMh2hv6CTO-_xSAbLbmm9uaybJiCUnl5Or04Vj2UaFfU0GRMY9kK1g8n4mese0PxN9DBAbQtWyam_x8iYt4yG2uWOUnTQxQryqSnteQ55O7NgW3G9fMIkIjKbCOOWX8Mm_ymVQWs_QItt4t8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f252f83e0d.mp4?token=jQ46tmDLU5B_feHaVcbjJz3JW2cHhi8rzDkOB_QX4cdd_E6GdEYtCVY-d9ri_Jot072GEeSGvGM9CDPVNq3MnYTn_w1M6OBOivMSAM1jt8qTJ8hIWAFJWFV5quit40ngQJ317XejFfNH-siX1V2abSqMAIdt20VLXYSI8gyARUyyscrFvWBEFAtOl_vsFpKtmAOJ2OMh2hv6CTO-_xSAbLbmm9uaybJiCUnl5Or04Vj2UaFfU0GRMY9kK1g8n4mese0PxN9DBAbQtWyam_x8iYt4yG2uWOUnTQxQryqSnteQ55O7NgW3G9fMIkIjKbCOOWX8Mm_ymVQWs_QItt4t8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ ویدئویی جدیدی در شبکه تروث منتشر کرد که در حال بازی گلف است و یک ضربه فوق‌العاده میزند. همچنین از آهنگ معروف گلوريا لذت میبرد.
یاشار: آخرین باری که این آهنگ ویرال شد در فیلم گرگ وال استریت بود. مضمون این آهنگ این است که
کنترل نکردن زندگی احساسی می‌تواند خطرناک باشد
توجه زیاد دیگران همیشه خوشبختی نمی‌آورد
باید قبل از اینکه دیر شود، آرام‌تر شد و به خود رسید
@withyashar</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/13554" target="_blank">📅 16:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13553">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رئیس‌جمهور لبنان، ژوزف عون، در مصاحبه‌ای با سی‌ان‌ان ایران را متهم کرد که در رویارویی با آمریکا و اسرائیل از کشور او به‌عنوان یک برگ چانه‌زنی استفاده می‌کند و گفت: «این کشور، کشور شما نیست.»
عون همچنین افزود که مردم لبنان از جنگ میان اسرائیل و حزب‌الله خسته شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/13553" target="_blank">📅 16:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13552">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ماجرای پرواز جنگنده‌ها در ارتفاع پایین بر فراز اصفهان چه بود؟
دقایقی قبل پرواز چند فروند جنگنده در ارتفاع نسبتاً پایین بر فراز برخی مناطق شهر اصفهان مشاهده شد که صدای آن نیز توسط شهروندان شنیده شد.
این جنگنده‌ها متعلق به نیروهای مسلح کشورمان بوده و پرواز آنها در چارچوب مأموریت‌های عملیاتی یا تمرینی انجام شده است و جای نگرانی برای شهروندان وجود ندارد
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/13552" target="_blank">📅 16:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13551">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130435eef7.mp4?token=e62PMucdueCEfv_0RD-42feCpRFNciYo6Fdki7FbWyLPehGaEC3V0KhT3IH0xDx1NSrG-DBImr3uYZUuZEjluNoeZjYuOlWvyznnCgIFKeH6urKCMXtbEfy2QUs1puPXOnZSCvK17Ye1HvXIIm4QMKXfgOVTACREpLNTSiizYeOhq_iPj2ThatZrxywBZvmeXmqVnOHS9MIn8e_aW6FNsJK6zOXtbFQgT_rzzdGdrzDpTvxoZG9Fo8dvS2RHQ9aqjHCPxW587gZKLr0JkLB1v5sJeTNdnGVSx-1ZwJ-EWzzow1rhW593qIzKvTzJq6b2-UV_iSAYGYmm04z4TgfgsqR2_T8LfUKZj6erO4_ePUjOhFGIkQ8yMUowRFUPSBz6hLj1sZrDxQ05YbkkBKtwuFp_6TDjfKWKuDsx7J5RI-6BhU7IQS-9bcZtb5PLm2LTj4M25GGKU4otO5ly4OJtuJPx-wodGeCamrzIU6vNq2ranBCel6I01kQLXYewINv4DirZa8Iz_rNB-02QVVQ2bFgqlvlg2TU7xvAFa3qmYqr06TLttzvCW_AcF0SmZApfEzzeyeONLGTPFiY3tFMn-Z8Htv43vxpFYy48DxYABdYS4w2c_jDqYwrvpaB9wzHqWxnWMlabMEX9tWkIpoemhrKl8WmXawF2nTZMaJiv62k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130435eef7.mp4?token=e62PMucdueCEfv_0RD-42feCpRFNciYo6Fdki7FbWyLPehGaEC3V0KhT3IH0xDx1NSrG-DBImr3uYZUuZEjluNoeZjYuOlWvyznnCgIFKeH6urKCMXtbEfy2QUs1puPXOnZSCvK17Ye1HvXIIm4QMKXfgOVTACREpLNTSiizYeOhq_iPj2ThatZrxywBZvmeXmqVnOHS9MIn8e_aW6FNsJK6zOXtbFQgT_rzzdGdrzDpTvxoZG9Fo8dvS2RHQ9aqjHCPxW587gZKLr0JkLB1v5sJeTNdnGVSx-1ZwJ-EWzzow1rhW593qIzKvTzJq6b2-UV_iSAYGYmm04z4TgfgsqR2_T8LfUKZj6erO4_ePUjOhFGIkQ8yMUowRFUPSBz6hLj1sZrDxQ05YbkkBKtwuFp_6TDjfKWKuDsx7J5RI-6BhU7IQS-9bcZtb5PLm2LTj4M25GGKU4otO5ly4OJtuJPx-wodGeCamrzIU6vNq2ranBCel6I01kQLXYewINv4DirZa8Iz_rNB-02QVVQ2bFgqlvlg2TU7xvAFa3qmYqr06TLttzvCW_AcF0SmZApfEzzeyeONLGTPFiY3tFMn-Z8Htv43vxpFYy48DxYABdYS4w2c_jDqYwrvpaB9wzHqWxnWMlabMEX9tWkIpoemhrKl8WmXawF2nTZMaJiv62k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی-اقیانوس آرام ایالات متحده (INDOPACOM) اعلام کرد که یک کشتی بی‌تابعیت تحریم‌شده متعلق به ناوگان سایه ایران را توقیف کرده است
در طول شب، نیروهای ایالات متحده عملیات بازدارندگی دریایی و حق بازدید و سوار شدن به کشتی تحریم‌شده بی‌تابعیت MT DAVINA را در اقیانوس هند در منطقه مسئولیت INDOPACOM انجام دادند.
ما ادامه اجرای جهانی دریایی برای مختل کردن شبکه‌های غیرقانونی و بازداشت کشتی‌هایی که حمایت مادی به ایران ارائه می‌دهند، هر کجا که عملیات کنند، را ادامه خواهیم داد.
آب‌های بین‌المللی نمی‌توانند به عنوان سپری برای بازیگران تحریم‌شده استفاده شوند. وزارت جنگ ادامه خواهد داد تا عملیات غیرقانونی و کشتی‌های آن‌ها را در حوزه دریایی از آزادی مانور محروم کند.
@withyashar</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/13551" target="_blank">📅 16:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13550">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c96db917.mp4?token=SGH3lp3XIx_YTnOEvxG8dfv5Y4asHiH9Wb6yhtw0tQhnwcCiS9KEzbJekLXsGfBYZm_ag7wSYiWAdzI7kDoNakqw6m2tCGDDsrILtIcz8lwHPaN9nwUfUX7f8AiFJLhMpX2UFeISFE6rqHi0L4SU78BtXUncAi7W366jC-pltYrWSdqtowcFOIYxH-Eu8sLxJ2ffAy1KRecJ1WJbfOTKtsMb2MjFHR2n0OOZn-JclhBa7IMB5lX6kBN9n7fgbMbbcwNgHdFZ9SJSKYdF1DNPUVbo-eMFr0caJ4U2znW2RClsbCH0bkwpSsAtD6916btU2mA2oxLR3MhFHjfAP1jBnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c96db917.mp4?token=SGH3lp3XIx_YTnOEvxG8dfv5Y4asHiH9Wb6yhtw0tQhnwcCiS9KEzbJekLXsGfBYZm_ag7wSYiWAdzI7kDoNakqw6m2tCGDDsrILtIcz8lwHPaN9nwUfUX7f8AiFJLhMpX2UFeISFE6rqHi0L4SU78BtXUncAi7W366jC-pltYrWSdqtowcFOIYxH-Eu8sLxJ2ffAy1KRecJ1WJbfOTKtsMb2MjFHR2n0OOZn-JclhBa7IMB5lX6kBN9n7fgbMbbcwNgHdFZ9SJSKYdF1DNPUVbo-eMFr0caJ4U2znW2RClsbCH0bkwpSsAtD6916btU2mA2oxLR3MhFHjfAP1jBnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی ایران اعلام کرد که به دو ناوشکن آمریکایی (DDG-103 و DDG-87) در دریای عمان شلیک هشدار انجام داده است  موشک‌های قادر و پهپادهای شهید دانایی.
هر دو ناوشکن به سمت اقیانوس هند عقب‌نشینی کردند.
ایران همچنین ادعا می‌کند که ناو حمله آبی-خاکی یو‌اس‌اس تریپولی مجبور به ترک منطقه شده است.
هشدار نیروی دریایی ایران: اگر کشتی‌های آمریکایی بازگردند، از موشک‌های برد بلندتری استفاده خواهد شد.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/13550" target="_blank">📅 15:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13549">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLlD3VChmb6wE9Dm6B2m4loz25Szs4v8cWy6Hw9mVs8yueBeYmGiubT3NrtI95wAjX03h1Fr3ZjXjLsm_nEQA_udNDdvHZerSDmRJ-qAo7YLKw0T_FxHiiGtHs_npKaMda1WJBj8p1jKb0VP4OFLC0SijIKhS2YVx5mvnlX84qdkuyf471m4cCCAubwyiidBANEmE0RkcIifk7UWRqW8ZJRq9h0KKnC2O8ZPRgq8pOgc-KXZXqgxYQif0QHfL3ub6-MSrhcb1PnOXW1Jeav23P0J7WhHIqoLACw8gMStxHDrWAQ_snZb5EseEkTybJrnvhUZwadCcQNsPO7MPNpodw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">️حمام خون در بازار کریپتو!
بیش از ۶۳۵ میلیارد دلار تنها در کمتر از ۵ روز از ارزش کل بازار رمزارزها محو شده است.
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/13549" target="_blank">📅 15:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13548">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddb4336455.mp4?token=OYWZbUga47KjVTrjpk6ROxKsTJ0QuLdq8-r650KruhRnoqDurbSq7mU7oo9eECpp2bcC-z-tOkzYoOXDvznPukn4aetyuFKJYOisJ02cLIi4vN7NyicYmDHymKwiqdD4wHVm11RoGlEi1OWLyP2hqAysYcSmLIY_UOSQrvGVbmIMwv6WvLtH4YfVRIFsRz8PSQRDGRN8vQdN07pgerOIvrxUMuQwks8XP76jLbeiaA1MMWQa_MCSSHDpJ4uCHCe5AFh-w5GAbkcXZaR1jrN3hwdW5P_lgJbQLDvpA16fF0VNlFaV1bRpZ1YZ1EPb-wSbFdidL5c2UhnyAfx5OdR9CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddb4336455.mp4?token=OYWZbUga47KjVTrjpk6ROxKsTJ0QuLdq8-r650KruhRnoqDurbSq7mU7oo9eECpp2bcC-z-tOkzYoOXDvznPukn4aetyuFKJYOisJ02cLIi4vN7NyicYmDHymKwiqdD4wHVm11RoGlEi1OWLyP2hqAysYcSmLIY_UOSQrvGVbmIMwv6WvLtH4YfVRIFsRz8PSQRDGRN8vQdN07pgerOIvrxUMuQwks8XP76jLbeiaA1MMWQa_MCSSHDpJ4uCHCe5AFh-w5GAbkcXZaR1jrN3hwdW5P_lgJbQLDvpA16fF0VNlFaV1bRpZ1YZ1EPb-wSbFdidL5c2UhnyAfx5OdR9CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ستون دود حجیم جنوب مركزي تهرانه  همين الان
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/13548" target="_blank">📅 15:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13547">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بر اساس نظرسنجی‌های معتبر آمریکایی حمایت افکار عمومی آمریکا از پایان جنگ و حرکت به‌سوی توافق، از ۴۹٪ پیش از جنگ به ۶۸٪ در آستانه توافق رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/13547" target="_blank">📅 15:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13546">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">العربیه: ایران بطور رسمی به پاکستان ابلاغ کرده که با انتقال بخشی از ذخایر اورانیوم خودش به یک کشور ثالث مورد توافق طرفین، موافقه. @withyashar</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/13546" target="_blank">📅 15:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13545">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فیفا: نقص سایت باعث صدور بلیت‌های رایگان شد
‏فیفا تأیید کرد که نقصی در وب‌سایتش باعث شد ده‌ها هوادار بلیت‌های رایگان جام جهانی دریافت کنند!
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/13545" target="_blank">📅 14:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13544">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">العربیه: ایران بطور رسمی به پاکستان ابلاغ کرده که با انتقال بخشی از ذخایر اورانیوم خودش به یک کشور ثالث مورد توافق طرفین، موافقه.
@withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/13544" target="_blank">📅 13:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13543">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سی‌ان‌ان: اسرائیل پرسنل نظامی و اطلاعاتی خود را به‌صورت پنهانی در طول درگیری با ایران به جمهوری آذربایجان اعزام کرده
@withyashar</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/withyashar/13543" target="_blank">📅 12:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13542">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سازمان ملل از حزب‌الله خواست به تصمیمات حاکمیتی دولت مرکزی بیروت پایبند باشد، به حاکمیت کشور احترام بگذارد و روند انحصار سلاح در دست دولت را بپذیرد و از اسرائیل نیز متقابلاً خواست نیروهای نظامی خود را به طور کامل از خاک لبنان خارج کرده و به حاکمیت این کشور احترام بگذارد.
@withyashar</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/13542" target="_blank">📅 10:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13541">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c45ee52c.mp4?token=cH830FXrv1cWRP87skmJsAbRW9MptZYi-ovfZsoZuZwUgdHRIt8R1EvabyvW7tnGwZqs_Ely4nBhKqCwtQZn-_oNPhHudXVxQd0K7OuYENmk9wpwCx9gZq7CEYFA1Oq_iD0Lragj1AhLMBIi1x-KSlhvbH3kD0lK-JeLPdFIDDPFjhxIurE-0JxkM3yTenNKFaF1TKjBdhlcP0GFvMjuIKgaY0uZpGs1R-Cz4Xj80ZYNr0JSPVBqIABJzF-0WQ7_8V5Wl07bitlYE7rO-sE9sPeM4oKTdpBKr96xdKCqSO1alKYBwuonyE6YOaOXanDKcwUyUN8L1aBo_ejvgpMgMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c45ee52c.mp4?token=cH830FXrv1cWRP87skmJsAbRW9MptZYi-ovfZsoZuZwUgdHRIt8R1EvabyvW7tnGwZqs_Ely4nBhKqCwtQZn-_oNPhHudXVxQd0K7OuYENmk9wpwCx9gZq7CEYFA1Oq_iD0Lragj1AhLMBIi1x-KSlhvbH3kD0lK-JeLPdFIDDPFjhxIurE-0JxkM3yTenNKFaF1TKjBdhlcP0GFvMjuIKgaY0uZpGs1R-Cz4Xj80ZYNr0JSPVBqIABJzF-0WQ7_8V5Wl07bitlYE7rO-sE9sPeM4oKTdpBKr96xdKCqSO1alKYBwuonyE6YOaOXanDKcwUyUN8L1aBo_ejvgpMgMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو اصابت یک پهپاد به تاسیسات بندر الفحل عمان که موجب توقف بارگیری نفت در این بندر شده است
@withyashar</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/13541" target="_blank">📅 10:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13540">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یدیعوت آحارونوت: کابینه امنیتی اسرائیل شب گذشته به قطعنامه آتش بس در لبنان رای نداد
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/13540" target="_blank">📅 09:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13539">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">طبق روال هر روز صبح حمله سنگین اسرائیل به جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/13539" target="_blank">📅 09:55 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
