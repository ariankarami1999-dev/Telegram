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
<img src="https://cdn5.telesco.pe/file/vbDUPXRmE4AEGMmclH3iI-z3NYy4UU8ToIOq0ntwZy7gCrB49NE9oF1HjSe0ChxWbaFi_Jn4gVQIO4R8SebIFVFYv358Gpk66OD1FNyAsbLFTXQZlmMclvZQGKMRKbCUvpIPb8OXYwOldAZ-w_1eXE9vx3hmASntZOYCgOLSlEaZSc20v8aoFpTSEzvL7GhdevVxzhkk2rWrjwoQCOXuxz5XTGqpLNrDuNZGV_-Ra54ydJ_UZiZDUsDKEntIlYCtis_Y4-W8opPPnYzNAPmcPZZWLK-TjfyCbDHr6Dwtwibio0t45JVYgJy6w0ClQMG7QLy34yKTzkJbcPPp7-cwEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 578K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 22:34:32</div>
<hr>

<div class="tg-post" id="msg-100101">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بریییم سراغ بازی جذاب و فوق هیجانی اسپانیا و فرانسه
🔥</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/Futball180TV/100101" target="_blank">📅 22:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100099">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ci4pC1Z-9JRRTGaeYsnnz5T6gm1978PrKwIDgpirmK3flNw3yqBz5THLUOJvYqwm2VBn5EapQbRPgaDfaUTrLLjoh6UPTAkPxLCT1U6F2jMLnRF_TYZYKb-jFtO22A1ccI7QG90alGIzJTyh1wACHbotNs8DdMkFfs1rtUGUI8Flb-L-RP8aBY2UogJYQJITwhZfaQwQd71JhLQPNnzSLieypTFZr3QElbE5kJdDqTdSqvmuPXfMSQyftOHZb1zGpNvRSK6RUCtYHUsWqleapDmkXcQ3kxDmVCLUk0S6D_y_QIcTEbcKDQKKr7bcIJL2c6bitE64bJiZJoPpDTbGZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عشقاتونم همه هستن که
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/Futball180TV/100099" target="_blank">📅 22:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100098">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Izw5z0TolDkXM33WMfFV8k1EqhKX8eES4cCfLR1UXAHRzgzjOUzVgMECksE3KcvUDxlG2jX65_Sb4pb9BhuDCHNkUyKYaSyqbUzbperK8nFcYoCbgPTZNp1nsCuiAza3eVCiZ3Z84bTiWJ5E7n-mdxuA5dNb-wGcuNAhQEbSqjnh-M12wZeuLWzj5K1ZjqyiwxD4CLxdlB-2g2wubhlK-GSczzk5saNFRfvmI1REtw0VI8MQmTA9yMFgj5d36xxxEPdfp0aSwFwk52W3kXna-hAxJ98BqnAVl9FgalHEEi0zyvYx9g_uuRVv3HEqOMefh3RxdymbK7nExkAi7hAnZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
گری نویل:
بین تیم‌هایی که توی جام جهانی باقی موندن، اسپانیا تنها تیمیه که بیشترین شانس رو برای شکست دادن فرانسه داره. فرانسه بهترین تیم این تورنمنت بوده، اما اسپانیا سبک بازی‌ای داره که می‌تونه هر تیمی رو شکست بده. من هنوز فکر میکنم فرانسه قهرمان میشه، اما اگه یه تیم بتونه جلوشون رو بگیره، همین اسپانیاییه که داریم می‌بینیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/Futball180TV/100098" target="_blank">📅 22:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100097">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reKDKD2x9A7YsTl4vFkezxTr612fPVZS7OVrXBHpUzKgdqY0PqNBcise7jBfkStfaZGsbCVJyEHAbqtqZ4FzIy2vJWrq8bYxdjZrHeDKsff_AClMY6Wuit3T7l_NwZ3UdJqCJ8XSW8nkA3MaKkDMCrvhYLpm0CzJqfp79kFxKnr5hUGzoA1vGv-BF9-p7tmlyWyeoutFrvLom9m2_z6A1rV25sfu3uZEGr4OhtB7hKqyuQp9q-miOAPHYDWDggqcYrLwWWJcZb5G8yq3Nao9Nv3eWRgWBTTONaXJSp3GOqaQyx_T_GW4TgTIBDsuh7atFk5qWVR8PFU-1-kS2Erfpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فابریزیو رومانو: کریستین رومرو از تاتنهام جدا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/Futball180TV/100097" target="_blank">📅 22:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100096">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnJHVJFFzcrcSCyl4db3YEJWDozOdSpjh71Pxj58mLgKfdk4pIM094aX2q649fUTrilyqxLR8PruFLcgcKvuEfb_JM6jrNEDiHdPsxatk0Y721O5MdtToPU0QLuaQIhwQligQP66w4W4BruSZfsCS7qgzZAuYtPMZR_OFO43FwXU1qgEvmVKP6Jnm6UCl5yUyCGYZ0fvLwUBEPo-VB5R_8n4Hijusp0ZqkwaG3_vOw6yEd9pUxqdqrY-lxELSNHbzz64yQd0ZBZiuYmwMEMvuQq2Zrs4Ts5Yzo_-R7mMgWAnFp9P7NWgcGj3CTqvo5-6S8OefgEofAJ72p1FtDyfQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
افزایش مجدد قیمت طلا
📊
قیمت طلا
با حدود ۲ درصد افزایش، بار دیگر به محدوده ۱۸ میلیون تومان نزدیک شد.
👇
در شرایط پرنوسان بازار، اپلیکیشن میلی پیشنهاد می‌کند:
۱.  به‌جای خرید یا فروش یک جای طلا،
معاملات خود را به‌صورت پله‌ای و در بازه‌های زمانی یا قیمتی مختلف
انجام دهید. این روش می‌تواند ریسک تصمیم‌گیری در نوسانات شدید بازار را کاهش دهد.
۲.
قیمت طلا
را در مرجعی رصد کنید که
نرخ آن بر پایه معاملات واقعی
روز بازار تعیین می‌شود و امکان خرید یا فروش فوری را در لحظه تصمیم‌گیری فراهم می‌کند.
📌
کد ویژه
خرید
اول
برای مخاطبان این کانال در میلی:
gheimat</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/Futball180TV/100096" target="_blank">📅 22:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100095">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ca1OPXkzUwwouLooMnUm6Jr6qF6ZWxRVv8GA6C50ZbBHSJHghlhwIC4lcQp1sCp7rLbPesVAHQRMkd-B3Z-KC6rcYnH2hw5gk1wnJBuN3NkkFuS6R_Ghraw5-d7GIegAt92k8naGgQ86TqvXHYXjsXQuQtzcQKJlbO_6N4Un0ARTjunAyJbodC8kAU__hNN2y4JyLQvqT7oQslq5K4DPXn5UAfx4J_A39_YnHVIQ684366wPWyd39LFxVWi3v8ch0TMEXxIrqpUgvyPJR6maHjZYRtEVlUTytzCnSG4txz-Q2WAQMgvKaVs_O_B5PQeFbNgY7ZogLwiBTuFzALzzWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش یامال هم تو ورزشگاهه
😂
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/Futball180TV/100095" target="_blank">📅 21:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100094">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QERFw9K9FI_V_WMdz_qUOYZ0vchjFfaVZhfM8U6OToCsEiP6Qke446c_X-f7r9Sr_C_6jyS9LsrHXoswtv0q13SUBFzIluicj1CxiALJkJOEOqpWAvva2PMzdQVlXcmXzJarIvdwKcLHebR7mg9o80WS4qz-lwi3Ybn4wXeuXiW8jaFCVQClj5WEjAog1nlfFuwqIaOYVeW4-uFzrpnRVRxZRjCDkgflLlrpsG_uKH73mI1zncnLCC8shxNWVis1lAQvbvQ3DkVMsiKq9GL2pDn4Ovg4I4AvErs4KVfmnRlTkQv3TSOWvmeyScreMHVFnaGmpZga911jxYSOWemjxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فابریزیو رومانو:
کریستین رومرو از تاتنهام جدا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/Futball180TV/100094" target="_blank">📅 21:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100093">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKI3cvsLQv1EltPCPmcVgrXLPYU0PERuKK1n0Xxn59INDHN42CzoWd-xn4FowswoN-GWkVK7Jrp_KOJKD8AG3k3MhKpbdB_1bsVNMFAc2c_yVTKUzPOySUz5shGBqbGOQ8jAMtJmpA8H8Ty5uK0dHXXD5xLw0xH4bk-CkoF3fjR20R3tpdUo7ZvLK55tlz459mckyncdaf31FADgXX0l5Gz51nUl_xfCIOwaTTaTWCymxJEllhc_YqXKQn3OrekYVi4uVG-XxpyMZ90l7HCQwmzGHlUPjI4cKndFNNKq9nDB-sKaUk0-f9Rol5zJzwZA8X3o2E_sR6v1IE0jRRYclg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپیکری‌ که یامال با خودش آورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/Futball180TV/100093" target="_blank">📅 21:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100091">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZMGq8xfee5SOE1LGnGhfdaUaKzLWY-Dx61Qd7pSMLY6rPzV1zXccsQPM3z7wAnHLgcloNw1Sn9MsbVQ_K-urWnU2RF1jTtVLRCmFzV42R_xQN2FZMt6n__dHLAVhUdPgac2DyhOpGanFJjL-nN3PURhD8GtbbbjQWpfd7YLZc-7mpO67zJmbAOE-6NgHT-I-BKxyrxs3eGQXg7uAeCxtuCdHXPYAH30_cFqyKC2xQEK1mSP7OT_t0DAQR5UVNc5PzxlxKAo-GW4AdPwvHVa-K4VbWhCZJR_Zyra1-K-p5gF_CfIyVZ-ONpxOaqy6DGh4_5vPg1CT-QKAYKK8viuOFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
#فکت
؛ کیلیان امباپه تاکنون در نیمه‌نهایی جام‌جهانی گلزنی نکرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/Futball180TV/100091" target="_blank">📅 21:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100090">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fdf9b5534.mp4?token=UbDFqCCyg1XC0YlUJiIMfzhjk6e7ytG0-NWvZdUI6TdILSpxFHJXV2iUGsFtU1c2D6rDmk1wPdwSkE5tzTeKt_AHmRDrDWk48j7mVPWe3HDs3PfVHb_pCRNzI8KKQiQxLhpNu8CuNFm6GJp-kOsdU9Lp5Cz-8JtyNVzdm7xv17WGulXrMa2fv3suZCpp2MazwaO30xLQhyrXdhmzjNSBc0RFQ_tbBzbMtr5z6jVRJxK5eThM9sVet38BZOKEUsJ1uesk_cgp7RCjCsgpJgSDOYXC2m4Wzo80dSOZ1OE6kjGUGMO2RBBXQje7FglSgB462lV2Zgc20pwAnQpnNXJSSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fdf9b5534.mp4?token=UbDFqCCyg1XC0YlUJiIMfzhjk6e7ytG0-NWvZdUI6TdILSpxFHJXV2iUGsFtU1c2D6rDmk1wPdwSkE5tzTeKt_AHmRDrDWk48j7mVPWe3HDs3PfVHb_pCRNzI8KKQiQxLhpNu8CuNFm6GJp-kOsdU9Lp5Cz-8JtyNVzdm7xv17WGulXrMa2fv3suZCpp2MazwaO30xLQhyrXdhmzjNSBc0RFQ_tbBzbMtr5z6jVRJxK5eThM9sVet38BZOKEUsJ1uesk_cgp7RCjCsgpJgSDOYXC2m4Wzo80dSOZ1OE6kjGUGMO2RBBXQje7FglSgB462lV2Zgc20pwAnQpnNXJSSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
‼️
ابوالفضل جلالی بازیکن پرسپولیس: وقتی در استقلال بودم رسانه پرسپولیس را کم و پیش دنبال می کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/Futball180TV/100090" target="_blank">📅 21:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100089">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0d875642e.mp4?token=AgJ3c0KyrH0GGCLBXMTEkX1fMR_bB_XeCFJgqnjZE24gb7b4BOfUo1iu4_v9dN3CG40xzEisXZKSgJOw8XlZf1ty5F2iNOGdSHW6CBJqwxmZpHq-qLjRrhBAHrI4Wby7CIR1TytAQVQDObZi-wx_Vgic6S8SwKfb-sz2ru6cYcQzr2CTKHMx8HtqAgfBv5D4VyGxD9TJc55FGdDGoGhkuzpky6kntx4pXH4aNr5zEuiMORno7a0uzxAHMBfmBrVm-F4ReMJps2powXOYh3fO0m64Dt0xC4zcOs6dDS2kOZoD4WRQtki9FQCxbYFm0tbPboQXh0oKH7PNpWQOupBICw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0d875642e.mp4?token=AgJ3c0KyrH0GGCLBXMTEkX1fMR_bB_XeCFJgqnjZE24gb7b4BOfUo1iu4_v9dN3CG40xzEisXZKSgJOw8XlZf1ty5F2iNOGdSHW6CBJqwxmZpHq-qLjRrhBAHrI4Wby7CIR1TytAQVQDObZi-wx_Vgic6S8SwKfb-sz2ru6cYcQzr2CTKHMx8HtqAgfBv5D4VyGxD9TJc55FGdDGoGhkuzpky6kntx4pXH4aNr5zEuiMORno7a0uzxAHMBfmBrVm-F4ReMJps2powXOYh3fO0m64Dt0xC4zcOs6dDS2kOZoD4WRQtki9FQCxbYFm0tbPboQXh0oKH7PNpWQOupBICw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وریا غفوری: استقلال را باید قهرمان اعلام کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/100089" target="_blank">📅 21:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100088">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XAelzuNctlBh_agPCftSS2iN-KP8SxqQEkFmaYogEiSbhoW_CfMW6HRbCeIqh9_9s0p7d-uHJ3WHYYBQajrjxCMBS1oped8y8GCdd11WARkT59aorrW6YCXl6SN492DrOEerz5cUCPCVbrQfWkhuE-Wu-aKDMq9KxiyeLX0V0PRAIA9BW5cwvq70XMF9a8DaTnwapscybvS0QF7BagNECWUerr5kqywRWR1Ozyq9Z-FU3KTaS44NNajMFWFnCxGRQuuOEBx8Gfh_dCZW7dLp34-DDGj5cJirNlDpvj-H7mQv9O3YtOxVyzKiVBnrn5eNm-rjMuReyD2mqnDXnNbhAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😃
پیراهن ستاره رئال‌مادرید در رختکن فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/100088" target="_blank">📅 21:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100087">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c35230c72d.mp4?token=gwkn4ZKBMCATR3ielgx_cUt0c4QuKe2TevIZOtoLv7mKrZF7Aivu1bRDgNyQB7p-4k9UZ-UqYuV9RD76iTLK3kwK6eOAWqXKlN1TH5-bzUg7iOR-iF-IKchMJ1f_rfxQ4V-Gr9MxgYNw9a_eZplgchBAKNYYBYOvlKsk0U_4_deHPjGk5SIGhQUC1IC7Hq-qdI-hDvpAS2f67pgbBYCtW15CjBSozVZBceTmrY7eUDI8zAHHhQCp4KA9SmystpdcI2a7YQWuUhRuw7c8MRv9rxhL9SRXQ4yDkbyV5z8ONQCAprNGjR2aDoCr8E5S91vUVnrEab6svwKN2sIIWmDCHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c35230c72d.mp4?token=gwkn4ZKBMCATR3ielgx_cUt0c4QuKe2TevIZOtoLv7mKrZF7Aivu1bRDgNyQB7p-4k9UZ-UqYuV9RD76iTLK3kwK6eOAWqXKlN1TH5-bzUg7iOR-iF-IKchMJ1f_rfxQ4V-Gr9MxgYNw9a_eZplgchBAKNYYBYOvlKsk0U_4_deHPjGk5SIGhQUC1IC7Hq-qdI-hDvpAS2f67pgbBYCtW15CjBSozVZBceTmrY7eUDI8zAHHhQCp4KA9SmystpdcI2a7YQWuUhRuw7c8MRv9rxhL9SRXQ4yDkbyV5z8ONQCAprNGjR2aDoCr8E5S91vUVnrEab6svwKN2sIIWmDCHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎯
یک تیر و سه نشان!!
🎁
با شرکت در
جشنواره حساب های قرض الحسنه بانک کشاورزی
با یک تیر، سه نشان بزنید.
🎯
مشارکت در کار خیر
🎯
شرکت در قرعه کشی و بهره‌مندی از جوایز ارزنده
🎯
دریافت اعتبار خرید تا سقف یک میلیارد ریال
🔻
افتتاح‌ حساب قرض‌ الحسنه از طریق
اپلیکیشن‌باران
و شعب بانک کشاورزی
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/Futball180TV/100087" target="_blank">📅 21:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100086">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rC0aPdYxmUW2ZTYLbc1n52w4VLi7f-NqAObTJsrKiy1jL40prvA1AtrAsY_7tuQGOz027LKPbR0omFHxToEkt7wzXURFKvYfZ8n0pf-x8DfvhfzleO-__doD4CyFTMZU8-QRmYyGeIFibEicPyMBf1YqUFVRKMZ-c3WuJtzHVa-ISmwKAohv1oJVcVaSMKX5PqXqATtpb4268YlSm36lVDK66AvOFJJ7Ko3MWM9bUutRyPwRSl-5iCGaoeKgxWg3YaS5KEJue_Rlp4mlPFhynybAFjtyxkiJAsCd6j48B0vWD2A-TWwym-N_7rwtqLyyI2FaIz8C-aeHsYr78HaBGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارسلونا اولین تیم تاریخ جام جهانی شد که 10 بازیکنش در نیمه نهایی جام جهانی حضور دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/100086" target="_blank">📅 21:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100085">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QstOVUoNRgBuUycwrVST0n_SQwuWHysNL9IkkOrxp6XtO_Z7ZtTE8MJfUmldbq8uuugHieJdugZhzwH-qt6MijN5N18qLdqVF56ts687sqJ8iC9zJH9LA5o7FKMRcwkacEu3G5IHn2tGtciT6BUqTx2SC3F-dAIcQKd-pyfcnxDNgk2e-Ng6eZXVvAefSKL-ZPO7I0uWRxrdcQVd4_oUMnPdHKxxfR2eEzBBM0aFK-i5YS4nQQciE5ytfM0kyZL377REnj5nzB0-XejNUiksQC4t8XA4wbxkri0DIknQRzoYde-cx73RT_YV_B1lwZeCx_xUnVkDNM5ot0kfMaD4Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فیفا در حاشیه بازی امروز به تماشاگران اعلام کرده که بلیت فینال جام‌جهانی همچنان در دسترسه و هرکسی میخواد میتونه خریداری کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/100085" target="_blank">📅 21:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100084">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXLFKU7LkU9d_Nv4UHTIDZpMT31p1tEFt6bJpkZ6AUcqI7ojUCy8atY_BiPcoNPLXzNE4OasstTzeV8e4eixowKClgvGMaipJPhS6Q54z9UcO44MjEaz2ih0KqPGUotXQeibZztpHHf3aPCtXmXCji66uws_T_lc52UGz8ohYVcGGhxSrxVzGPRGCaoHaAA4bsoNdhSBb86197wr1L5KKEUrf9WbMkRtGsIK2ep1YCDvZrQBSi_lf72N5x1mL2TWWJaw6i1SnOgJOusX3GpHPe91lUpIk5zUWejDuQ7rqx_MaYybomVgIgn05iK5WfuFKsi3DlteObMS0NSuRqPqWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشالا که خیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/100084" target="_blank">📅 21:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100083">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZTiCzCgFMs7DdkR76W5anxcXU8L3i2oNVSxCgdcV22f1ZYLJjyFbRXIUPqg8fEUm21ojiUHC904LCGt5v3VZSZPsA-9hyNt3DgvZq559OuE5ZynOjVjuh1VPQTWGFyK9iPlmamnD-h5MZ_u2xdbyXi1iFJj6xG0ns25gb7jbl7Bi1r_-JX8w6DuMMILaSGi7QhaQJNNZL1kkTBap4uxpljW687qxSMEs5Q1tmo1s5C_DfaAz8wHEJ_YoxdWOEeKDsi1tS_ycXRPfsx6Db-KQ2-dRDZ_D3dHOYH4tWesYw4tkefL1WTEJhNoCpoh5CwLyXAjuylSa4i3R6O2YDga5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
#رسمی
|
تیلمانس هافبک بلژیکی استون ویلا به منچستر یونایتد پیوست.
💰
مبلغ قرارداد: 35 میلیون پوند و تا سال 2031
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/100083" target="_blank">📅 20:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100082">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🇫🇷
ترکیببببب تیم ملی فرانسه مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/100082" target="_blank">📅 20:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100081">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCiSLIj1fAKC1XDuSNhUiAd3-J31M9gWVq9I4Gjravv9cK18nYrnrrsUKXOqX19ValUs-qg71qbhiNZrNbXOFOUwthja-hbs0JCfJYpaUtXSaNprzxUHFUDC3wokUg1xAeTX2yo6sUNEaZLuZr90uFo5vE7uYvlLNmOv2v5zSJwgFdxU7Wutn8NfNwIOSwGaHE-12gk8m1RP8CA2-Tc3Gq2epG_7CuMeaFPu82XuoDnVpZKv3fL25475BtXnN-HtJwP78aA5TA-ynaiEAUzPOfavlCdi1Wcza5xvjIdlcTBLuiRuFFbnoZk7y4-W9poUgml8hJxOOiuAxwGNzOoqkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب رسمی تیم ملی اسپانیا برای بازی با فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/100081" target="_blank">📅 20:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100080">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dF-VnezVsd0Q-ABSwQFpLfkI3TSND9PnYLofDYGgMhbwtURRhRsWu5MIZ2pM9srTPrxxqvsjvo_UeoG9EJ5nQcqORVNoak-nVyfViHRVxWjAwfJDCda-mbDgK1snpAH2ypryshQJ5RP06Ik3xmYfQkkQu3daaibPk5C3FuyLh0ggd77-bygLCIFmAeDpfdOb4Bk7DkxuYRwDkzupXeMHkDfFIWyK5_YaMIqUcuc8XDhQ7IdLzAf4tAWvSIttHvQGUHoHmbMZUsvW1hvhY5OJYoVkUit7E6Mcq6WBUoXaYInURyOU5-udnhs_xS3gnBnpUUeB-IOupWy5ReIzqxL-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب رسمی تیم ملی اسپانیا برای بازی با فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/100080" target="_blank">📅 20:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100079">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1J6DWgGjSJz6K0kTc_0-nFLlJZ4lcj55OkQWImsQv5cqOCx-g9fX76ZyN9W6P-o3byTuAbmLxi16QyN3DKD6lZDOzYe2C5_mHP0wihz1flVvuXfERxhg0sho1NQKXCUAL-pTsDvsMulT2GSA5bLr4BZZ0C6kIpiHt_-TnMQIFrGr33r4DQSPRD-ljYl4pdiwyYw509bE-t1UQcx1uoJQrCj5B-PR5MLhNXJL8ElG9tVGOiOpWXrFMCDt49c5khBsan0W57Ii-2-pQAdt8UQJXPBKVFIfhXz6s8rFcg7TSx-iufrH2ihjuKmMdO2Xsh93vhmfGrlPU1xZzGQubBpbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب رسمی تیم ملی اسپانیا برای بازی با فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/100079" target="_blank">📅 20:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100078">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSjmYcrCjXOmEUeOrAOK7JOKmWvXT5LCvo3HTXZhHyZct66H1aLVYlxxeUEpr9hueJ_KezFboe6RCIkvqG9VMkOl1zMmVn479T4IJ8UtPiFaVIJ0LfZxqTFVgqa-s-ZFM6w_S0qFVW0yXy1AiUASaCVPH1Lrqk0rJJZ4XUBaOWd2i96RNShgzejyr5qfXID1oo-bVgDXFLNA0-2tbeMUyr03B1hvZcXxA5S3TeYBZd4nRYeKutrDgZypSJhNxRara-xnP825Gj5Cv1JlMKrNNWc7D2fXIR8USzbBfFeby7xVGMx1FmMpdTWcHdPWP1Ls4bVo6z2B6VwtqocGF5P8hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/100078" target="_blank">📅 20:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100076">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_Axruy9oYBv02HA9Z8liztEMepWD75HQhZT1QPaNvkhzEeXPWkkaGn-foV9jk54xyDS460Ss_JJ9FVe1P-yPMnIz041mhGDDyS7WyL4VWuEPrCBGXL07Ic5PbI7VcwUsPDLtqb-8j78QOwOf0_zoORC_2wISCxHg-lRFIjCDmKFL_eoWWvbvdZ7O4gPsOuOtujqJ351H2uSrSc701mwuIuVkVDo0iyt6cK5WXrHsXU_0TIVZ9m2iUsqGcR8W2c1o6EQ2e2bWIAsZ5p2SPN6Ol85lj7P2XpMjkRMonvzbRgur9fSw9KGOqL4i_oUCqg_Y29jHNqLmy8GOqkWDGio_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
اسپانیا در نیمه‌نهایی مسابقات بزرگ، هیچ بازی‌ای را تا به حال نباخته است:
‏
✅
برنده نیمه‌نهایی یورو ۱۹۶۴
‏
✅
برنده نیمه‌نهایی یورو ۱۹۸۴
‏
✅
برنده نیمه‌نهایی المپیک ۱۹۹۲
‏
✅
برنده نیمه‌نهایی المپیک ۲۰۰۰
‏
✅
برنده نیمه‌نهایی یورو ۲۰۰۸
‏
✅
برنده نیمه‌نهایی جام جهانی ۲۰۱۰
‏
✅
برنده نیمه‌نهایی یورو ۲۰۱۲
‏
➖
تساوی و حذف در ضربات پنالتی، "یورو ۲۰۲۰"
‏
✅
برنده نیمه‌نهایی یورو ۲۰۲۴
‏
✅
برنده نیمه‌نهایی المپیک پاریس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/100076" target="_blank">📅 20:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100074">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Km5Yf8oRS3UKFA_jzQAt98VZSx-nGnyiLaXRYLMJ5YYU-eDyXsB-8aO1AqWGI8WZNevON386mwTstvHX0eNaV2qNtx56vATQ_BIa0PiS75lASthGPE5lwJSQh8mcn6d1vTy8-9aEjx2tev3nv47citI7mT-TFqpwh5L27ba-zOTj5y3osrqqyinWSi3slwLjnzdPuyh7OFgmebVG4Ctgkttjp5wFg-auqM0FixuVdk8F8NSMni7sRN6ih8i6qh8i_nQUpcdVKm6zAmu8NRCMD2l311aOJ7jGjg2Q4d9QJnPvEHklMyQb2cWR2T9530VgOC0u-PoQ2YYQz4qy91nX9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KwUObnvLFI3DxbVBgfSLMseE9Kx3gZyqLpD9lWEuECPXDfphfT6CPN_VEHb8RcYCTzHxaHQzQx1Wfto7Jxz4JA-K-ZbJN2RSMvVgZCaNhNdRr14HvpZkGHw18YhOXx34tgJdYfY8RRHyWfFqZe3GbttLPW-r-ftgvJtpUp6bo2M7LbSYT1QkBXZ6HLlKwe5Ei4WCb9HUwS-3ZvS2zT6KLTsuR9ItacyQGU5DANTt5WXzD18bhhNe9EJJqLaMOMxSSgUrnBBhxIYmiKlMuF9VrA80MnfmwrXYSvuFNoNJs3NZKosHsOFAqcMi2zkwKolvQJ_lX4wb2nHawWOqi8O_Hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🔥
کری‌خونی‌های لامین‌یامال شروع شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100074" target="_blank">📅 19:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100073">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnjdARtXdKhkjK5F9J4ycfrhFNpqAP2n-jF-i5xbqt1CBriaLoTZDjfKmZfo3qga0ZA6BsHU6nJUfYMkYL8WPKKH4SGWRy577LkPAfAYgNTgJ5Pawp1XLt6622GkQsBvKiTFauua4wPJ9cZHmcFlAHzJmKCgIahsmytgEUfj76KunkryWZUSm6RfNgNylaAZRtpge_4lDMhtRbHK1CdCZtgv6PK-BNkWxlYQ9bBZoT92g0kTY0nyB8TF7c1TkSNk-VLigVGnKwWonpVLyCU9GfLiBd0fB4X_mRJ1tCD2KJTC5xmgZT6K__du71ABr7ryPAFDvcSNkIR84MskS4sjIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اتلتیکومادرید در تماس با فران‌تورس از این بازیکن درخواست کرده که فصل‌آینده قراردادش را تمدید نکند و به صورت رایگان راهی مادرید شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/100073" target="_blank">📅 19:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100072">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7DtwBQhFB8lT2mc5opGfyXBKFPGYHKK4AsXN6rXxAbzdnBX3JmmKpk5Io1SZKx3hsQMt85NGML1gD1G48Vtg2oiroYTZ04MpxHUZs7EsNOILWa4TCf2FLqhZlHRQjtxcHXy1JvgYM_5Sg3dAASAGIKeuxVpnlADDjSrfX96_zv5OQDt-nMooeJBKrABFUt3FoxbYvKgr9C_O6i4ZnMUp_nPW7kBlGWO6iVzBwUkrsvDlpo2nJvpNSDlQhmDEYhienRpXW8oLoCgzMOJR49FidKD2CV6h_NPDbCHjpGkFsxUQBx-STAl6Er9brVEdgBuT4NVDbHfiPPG5x6ZM2n4nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
هفته بعدی تاجرنیا مصاحبه میکنه که زن یاسر آسانی مخالف برگشتش به ایران بوده و ما تمام تلاش خودمون رو کردیم
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/100072" target="_blank">📅 19:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100071">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔥
🇫🇷
🇪🇸
آخرین تقابل فرانسه و اسپانیا در لیگ‌ ملت‌های اروپا که با نتیجه پرگل به پایان رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/100071" target="_blank">📅 19:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100070">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7893735fc4.mp4?token=vb_yUdio6imkDizaqSNnTSSBp1MSnQ8Uj7SddivOdusutDffuQqu59oEQA7zf5ioz8JGU1jT3gSIJFugq0-uUjiBCY8HPusDW8xjwx0EHmR-lRUfVYuR38Lc_lBHqFHmy85i_-C1edQPxj9WVbCupZ9aoVENrXrkD2REcy_NkP5JE0b7sPS1S3zPrCNyB24E4hqmwSDf8yjQJti0pu5OlgdZ3r0jeOIUeOV5aZ12rWTS6ezc0PBAnrzugx8sgrxTUCnVQ2VaDWVRQcHVynRWzAQpdxF68XLJ85qQHDZJHOPSIMg09H8p5GAqyg2XbxWO5k6CMludxoCbMWoDU_NhNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7893735fc4.mp4?token=vb_yUdio6imkDizaqSNnTSSBp1MSnQ8Uj7SddivOdusutDffuQqu59oEQA7zf5ioz8JGU1jT3gSIJFugq0-uUjiBCY8HPusDW8xjwx0EHmR-lRUfVYuR38Lc_lBHqFHmy85i_-C1edQPxj9WVbCupZ9aoVENrXrkD2REcy_NkP5JE0b7sPS1S3zPrCNyB24E4hqmwSDf8yjQJti0pu5OlgdZ3r0jeOIUeOV5aZ12rWTS6ezc0PBAnrzugx8sgrxTUCnVQ2VaDWVRQcHVynRWzAQpdxF68XLJ85qQHDZJHOPSIMg09H8p5GAqyg2XbxWO5k6CMludxoCbMWoDU_NhNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇪🇸
مروری بر نیمه‌نهایی یورو ۲۰۲۴ و سوپرگل فوق‌العاده لامین‌یامال مقابل تیم‌ملی فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/100070" target="_blank">📅 18:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100069">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PycWjF_ffZ3T_0btWxk9RFkvNOKcS2BFSTjawKqWr_huazvQv9-xfvEmt-t6Y-pLPkbPLshtYQSJOIZczWR8rheAEnnULx03yb0DvnmpFfBnoQmmHCEpgiEILowpIa7on1uJfD6jh7hZghbufB1oIWGW1XooOX7LbQ3_lM7rWOvdB4nurpVuHnGsvE4VaxYGaoYdV3heeswuKLCFd_LfSa51SQDHjrgVbAyhYhhkTM4CimEI9_nXILfUfnVbyqcb7Lf1urZOWuQw5-LHazj-CJx8BvFIzvoVlJsxUiVsLSluDY_VaD_eqVG6_wleJ5E-DYkviuSR_csv5_Bnr5zYWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🚨
فیفا از هنرمندان حاضر در مراسم اختتامیه فینال جام‌جهانی پرده برداشت. این هنرمندان عبارتند از: تام کروز، جنیفر هدسون، لورا باوسینی، نیکول شرزینگر، آی شو اسپید و روبی ویلیامز.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/100069" target="_blank">📅 18:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100068">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/789a70c949.mp4?token=XC9v2QaVND4jG2rSGnrW_MsHkmOiW7Kqa9cUJOPegN7WI0NJfHYGGWJxL9psqe3vgQ1OyEUo5YS-G6GDIjwv4XmIfDH0qDVwNTTbZ1sGtU6KuciAJGCk6CNX9_vH_mFtOGAl9NQxz2j0JmpWK-OS9NJxRzq-j9mL3zz6TrenLMAmCrbQGqMLicPUsdnGvnwbVQy3okEAqQjIyHyHtOTC3UapFLZxT3s6F0i70UYZ5CFuhDEXJS9krw_ui1bjb08iOTsRKOxzt9688jh5-lvKNcxNmf8h2scyCRv1ZzbAE1PZcr68534bLToThTcBQu9gmhTPPNxjkHqkgLHjRXKvPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/789a70c949.mp4?token=XC9v2QaVND4jG2rSGnrW_MsHkmOiW7Kqa9cUJOPegN7WI0NJfHYGGWJxL9psqe3vgQ1OyEUo5YS-G6GDIjwv4XmIfDH0qDVwNTTbZ1sGtU6KuciAJGCk6CNX9_vH_mFtOGAl9NQxz2j0JmpWK-OS9NJxRzq-j9mL3zz6TrenLMAmCrbQGqMLicPUsdnGvnwbVQy3okEAqQjIyHyHtOTC3UapFLZxT3s6F0i70UYZ5CFuhDEXJS9krw_ui1bjb08iOTsRKOxzt9688jh5-lvKNcxNmf8h2scyCRv1ZzbAE1PZcr68534bLToThTcBQu9gmhTPPNxjkHqkgLHjRXKvPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇫🇷
⏳
🇪🇸
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/100068" target="_blank">📅 18:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100067">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c97b0625.mp4?token=L-fN4c41sJUiypP8_754egw5MucDbqxU5NKLwdNIrv2a8zP9sn7uuu4tnY_ApoEd9G4ge8__txG9BpyiuetAc914wfHeYY5d2OynggZhElakQFREOdIOyl7JRRoNvEB7e2ZCItk0G0ab40TpJunrf7rreeeitZhOeozhty0tinIYGcITn0A5BYYGgH0ETKBdko_QSPfJPvZcf-_bYY2-gX0PLd-tJAbhkAgV10450SrXk-q4W01FmA_eV0cEWJAlm--dCinUOyJ4u_FnPX9S2_nV3NiL5T6NxgqOkeDrvQeo_RQsKIajGrfLAHv-SJSxAaUJWtPiwl6I_YcaPFnl-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c97b0625.mp4?token=L-fN4c41sJUiypP8_754egw5MucDbqxU5NKLwdNIrv2a8zP9sn7uuu4tnY_ApoEd9G4ge8__txG9BpyiuetAc914wfHeYY5d2OynggZhElakQFREOdIOyl7JRRoNvEB7e2ZCItk0G0ab40TpJunrf7rreeeitZhOeozhty0tinIYGcITn0A5BYYGgH0ETKBdko_QSPfJPvZcf-_bYY2-gX0PLd-tJAbhkAgV10450SrXk-q4W01FmA_eV0cEWJAlm--dCinUOyJ4u_FnPX9S2_nV3NiL5T6NxgqOkeDrvQeo_RQsKIajGrfLAHv-SJSxAaUJWtPiwl6I_YcaPFnl-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
نبرد حساس امشب میان فرانسه و اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/100067" target="_blank">📅 18:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100066">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWieucLQUljovNC8Py4zpQuCWlY8f8V9Av9Ioo1-w8rgAg4M0jCmT9cwVZ0f7CdVp5btHbW4rK8GF8eSMgAhpbCJmcw7rVJsjiD3vLsVMh161XYYTjWUR0kwXWZF0efDfV6_ytbQewSagRVYOz-JIclfpwvSS3InVlP5N-TwRdaFGymcZGbFO87rcvAUmEowJJzsAfPnY3VgrWkY1-JE5TH4BVx-qtQN3qvPdX1mn36DJ5fE1-H04iECtRsAQ_Llf_yK_-d_KSORhgVQWmeSxpRPvBaE0KWVME7UfN6wGmWAp2mnKYN4l-hSMu4XMM3gsbiDi8MgWMuhWqsssxekLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
فرزند کریستیانو رونالدو واجد شرایط انتخاب یکی از کشورهای زیر برای بازی‌های ملی‌است:
🇵🇹
پرتغال – به دلیل ملیت پدرش
🇺🇸
ایالات متحده آمریکا – به دلیل تولد در آنجا
🇪🇸
اسپانیا – به دلیل زندگی کردن در آنجا به مدت سه سال قبل از رسیدن به سن 10 سالگی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس – به دلیل زندگی کردن در آنجا به مدت بیش از 5 سال
🇨🇻
کیپ ورد – به دلیل ریشه خانوادگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100066" target="_blank">📅 17:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100065">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔥
🇪🇸
بازگشت بارسلونا به تمرینات برای فصل‌جدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/100065" target="_blank">📅 17:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100064">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ffb38d84e.mp4?token=d8VByNPGrW9tmueCitSYReJicsMQ1dcVp4UKyxI-tg3tMGSk7bNo-ftAcy49syRwo5J5Lf8-t63rSUCPDZLe39uH4bgL1tYQh5rMRzx0X3RkCZjWb85VanUHn6MXe7Kz5fnKwQGsKrxW9rSfCG7chuf8asiwfDp9kiev1NeoX5rjEimMjEsQQhF8ok7c_qTtcqIYBrobz0jRoBYWmHaNpblb10w_5blsCeE3ARxHC9kh19njLjuf-8KNtmjqwkpjUHmxnevMmvMFNc9tAarEF9SIxYa2J915yskaNXTc8hzEK1iZbTVXym4gqZ8OIjrVuRRkGPxbjHJkBl5Qd6oLOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ffb38d84e.mp4?token=d8VByNPGrW9tmueCitSYReJicsMQ1dcVp4UKyxI-tg3tMGSk7bNo-ftAcy49syRwo5J5Lf8-t63rSUCPDZLe39uH4bgL1tYQh5rMRzx0X3RkCZjWb85VanUHn6MXe7Kz5fnKwQGsKrxW9rSfCG7chuf8asiwfDp9kiev1NeoX5rjEimMjEsQQhF8ok7c_qTtcqIYBrobz0jRoBYWmHaNpblb10w_5blsCeE3ARxHC9kh19njLjuf-8KNtmjqwkpjUHmxnevMmvMFNc9tAarEF9SIxYa2J915yskaNXTc8hzEK1iZbTVXym4gqZ8OIjrVuRRkGPxbjHJkBl5Qd6oLOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇳🇴
اسکورت و استقبال از کاروان تیم‌ملی نروژ توسط جنگنده‌های این کشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/100064" target="_blank">📅 17:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100063">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMv2GqZ9An3W6OTBujKd_Yy0x4qMOmtXleCUQdCfKIvE-8mbZAEkMLHuzHmkdxkAqhQdNitjyEfmvjLzBZgY2QU-ENolV9eh5jn-RilB5UAYhql2MqGAylrcmFtbZ9Jbq1R-o7MguBa-GNvxuyte8ALbEe9YTtDreG93hLpbjCrAdibVGm_a4ccKn6J93iAwk7USjmhDK9Pd0oYYSe4rApQcXfkTZfOscP8EyiLZCgF_QzXFKiJP4czSeOuIBCOno4eKxB7wWxSM549ilUfk-q-JxrxL32LNqcojbSBonWjXisXPYAd3qxWur6Ab2q1mxWIAz-YcQNCYVxEADdm1iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
❌
#فوووووری از متئو مورتو: فرنکی‌دی‌یونگ هافبک هلندی بارسلونا دچار مصدومیت شده و حدود ۴ ماه غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/100063" target="_blank">📅 17:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100062">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f23f251977.mp4?token=NgZNLlp8UA5AflCs3w6PMMlnEN9nCiVPuwluKRwZGdgVwLt4nslOrL-c7gniMc_X4I6dU8QUim6tzvVQe6xdtxtDV5EDyTuP_ikdtlE49qelWaMrrsNSnEBpFeHPX30yw8_JPJ1Bf4_TvsrKebwnjrZhnLzM5NgdUkGkhOzexIU6_VNjUJ725l7mYIQn9dIkoxiLT_CzSW2LXU8m7PAXp3Vzg7vRkYdJfwyE1X7c36w-fAIKMhHCyDIj5mY_kD-0hMMcHmbAIwFYOuVn9kI6ILYWMxIGqhGtWgqo2Td_RHFgSK8tzmGK9N-fKZW4jDArGUdSskjiMvG72nz8XuLG2yLfzp7VA9VgRZIzHQFBKqAj0Ta3s1xr-gWKbtSIWCAdbk4jkXPA_gws9LmZ9P1zy6wAmL8ASPdBRuqlcofgSdnkG_z0C4ij3JaUIoGU-Cf7lGdDA2hgpTvEAtVz-k_rGfNCDsTDXyflaQFvKO772bav9EpXjSJw9ABsHaD8pltohxMRVZsThTKJTKqoux6HpVCFeFEjvxzgd5Fn2PDZIqXSUUI4hRQIUBgk4j5IjL3-_QxUvLh_gvQ-S8HfDYzRNz9v9FeUEXJgG1Zz4LTM6HyuNE99_HDdUXuZ8UX_A5V6uKznJV-pSRX9h46YKcT3oOAPt4r0lWuDrvexDqkK2hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f23f251977.mp4?token=NgZNLlp8UA5AflCs3w6PMMlnEN9nCiVPuwluKRwZGdgVwLt4nslOrL-c7gniMc_X4I6dU8QUim6tzvVQe6xdtxtDV5EDyTuP_ikdtlE49qelWaMrrsNSnEBpFeHPX30yw8_JPJ1Bf4_TvsrKebwnjrZhnLzM5NgdUkGkhOzexIU6_VNjUJ725l7mYIQn9dIkoxiLT_CzSW2LXU8m7PAXp3Vzg7vRkYdJfwyE1X7c36w-fAIKMhHCyDIj5mY_kD-0hMMcHmbAIwFYOuVn9kI6ILYWMxIGqhGtWgqo2Td_RHFgSK8tzmGK9N-fKZW4jDArGUdSskjiMvG72nz8XuLG2yLfzp7VA9VgRZIzHQFBKqAj0Ta3s1xr-gWKbtSIWCAdbk4jkXPA_gws9LmZ9P1zy6wAmL8ASPdBRuqlcofgSdnkG_z0C4ij3JaUIoGU-Cf7lGdDA2hgpTvEAtVz-k_rGfNCDsTDXyflaQFvKO772bav9EpXjSJw9ABsHaD8pltohxMRVZsThTKJTKqoux6HpVCFeFEjvxzgd5Fn2PDZIqXSUUI4hRQIUBgk4j5IjL3-_QxUvLh_gvQ-S8HfDYzRNz9v9FeUEXJgG1Zz4LTM6HyuNE99_HDdUXuZ8UX_A5V6uKznJV-pSRX9h46YKcT3oOAPt4r0lWuDrvexDqkK2hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
تنها چند ساعت تا تقابل خونین اسپانیا و فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/100062" target="_blank">📅 17:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100061">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1C0NET5S5Q3dWjqxT_HrPBEiU9If2-Ilp9g733TbSqjDOV1jcJHHfqaedNPPuvu_lDkV5kjgBjAffy_-bRGkJNgGxPtosEFDS95MFTcDYaMRWmr500Cs7bBRmj95no2rYiLF7j9ZMZOW-ZXQ1Unf2hzUOk-zkE4nQNiB_kdxXi-GMR3cWJGFelzjuL4OPLl6SDShFKMHsUbGhvWu8fCPsWXQNrjd-kw5pdBvq6R3FVjw3nyarEmdhALlDfD0YcCMp2I0-xefTMdW9Z1LSH4_niWc9iOTw3A1XU8Pnh9VyzTOddTpQZ6qnnnQFGacNFDMppJ7jncnpbkbejt9rKHeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
❌
#فوووووری
از متئو مورتو: فرنکی‌دی‌یونگ هافبک هلندی بارسلونا دچار مصدومیت شده و حدود ۴ ماه غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/100061" target="_blank">📅 16:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100060">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c84de7847.mp4?token=I4LACbA82hzN9531-0vYHMf5vy1MYsM1DiFGqDKpMa9Q5vIFrqLNYXbqBoFCHabcnx9hu9d5LPFM9_JqZOd_oHXSG1lu21iLmOMjkCZ0MkU7jJ3la98rZhjXh0SP38JoGroHD9aR_SYnLacQ9pHnZpPeScWQrfbRiTV6geC3KEt8iH63276JS3-9OmMWDm5jgAUR8FZR-G9whPbxmNneC2SafdZOzaCq7Fv0pCSoDwaUz7YpUn06opoJuhrHgUGnvl5sQ3T8F-Y5-_jg7UHXAOJ29sno7nhI_nFGe_EvPQY-vatPPwuY8u3lcLdbgIVv3FF-WtE_7Tmzih9QnsZsyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c84de7847.mp4?token=I4LACbA82hzN9531-0vYHMf5vy1MYsM1DiFGqDKpMa9Q5vIFrqLNYXbqBoFCHabcnx9hu9d5LPFM9_JqZOd_oHXSG1lu21iLmOMjkCZ0MkU7jJ3la98rZhjXh0SP38JoGroHD9aR_SYnLacQ9pHnZpPeScWQrfbRiTV6geC3KEt8iH63276JS3-9OmMWDm5jgAUR8FZR-G9whPbxmNneC2SafdZOzaCq7Fv0pCSoDwaUz7YpUn06opoJuhrHgUGnvl5sQ3T8F-Y5-_jg7UHXAOJ29sno7nhI_nFGe_EvPQY-vatPPwuY8u3lcLdbgIVv3FF-WtE_7Tmzih9QnsZsyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پارو زدن 150 هزار نفری نروژی ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100060" target="_blank">📅 16:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100059">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/417c844b52.mp4?token=VmWg4_HmShsXb3h2ZJuhzeiPGmhv6kQ-SjI342RQqImGwvvcJvrZnEFa2R1u7uU7QLtgtaNMm5LQnVfXkh94xN6en6lmTQiYNHxnFyNduE9P1Dbr-ulhJVoiPcvzApGDVIPpjoJXL-IAUm6LMN51K1HwABFElrp8WpDiItueiPmAfUDNmm71txdyldruBsyaIhG_FEv4DsY6ZIs07Mn3m3-ChMdclQrWCiK6SHCcazEM4KFDypIuIHtL9gGfgwUJSlIau0otJWQA7Ww_oTXuMF6qOLyZRQq5ABSxLrEXSJutZSlAENCL3noppGni95FHb1LymgODNo--y2Hym3f39Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/417c844b52.mp4?token=VmWg4_HmShsXb3h2ZJuhzeiPGmhv6kQ-SjI342RQqImGwvvcJvrZnEFa2R1u7uU7QLtgtaNMm5LQnVfXkh94xN6en6lmTQiYNHxnFyNduE9P1Dbr-ulhJVoiPcvzApGDVIPpjoJXL-IAUm6LMN51K1HwABFElrp8WpDiItueiPmAfUDNmm71txdyldruBsyaIhG_FEv4DsY6ZIs07Mn3m3-ChMdclQrWCiK6SHCcazEM4KFDypIuIHtL9gGfgwUJSlIau0otJWQA7Ww_oTXuMF6qOLyZRQq5ABSxLrEXSJutZSlAENCL3noppGni95FHb1LymgODNo--y2Hym3f39Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله‌روا و ابوطالب آبروی قیاسی رو بردن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/100059" target="_blank">📅 16:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100058">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_AEa1crOK9KUYpzSAL9nJdi2XGOfDCcACnogwq9WAKQg1DksH-OCY4jd-sJ8wrkn3ErI63SCQm4o9QSoitHWBcyYKoJRCKWTlMaXDo4WGsa7iKHunxSBQDUgsgiB9ZvfirfsPIZuQtYh4kk0oW3QfyF3Hm9KeyE4Up0Lagm0cflrRVnnmtaAgsWcXOKpe4AGtDx6puMlmo4NMqRL3N6aYr3pXJnEc7ZT4Ag6MArKxIwK_MWGm8w8YupAOYtn_u3ZySj0XTG7whLjwOQpVvzQSNPZEv764V4BecUIKgA6HWabs9Pnroh-r7lvllqAJDrLP5bXSUhe7UsLJKHj50bFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
۵۰۰ دلار جایزه نقدی + ۱ گیگ اینترنت رایگان!
🎁
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
🔥
نیمه‌نهایی جام جهانی ۲۰۲۶
فقط کافیه نتیجه بازی رو
قبل از شروع مسابقه
درست پیش‌بینی کنی.
🏆
۵۰۰ دلار بین تمام پیش‌بینی‌های صحیح بصورت FreeBet تقسیم میشه.
🎁
علاوه بر اون، همه برنده‌ها
۱ گیگ اینترنت یک‌ماهه رایگان
دریافت می‌کنن.
⏳
فرصت ثبت پیش‌بینی محدوده؛ بعد از شروع بازی دیگه امکان شرکت وجود نداره.
👇
همین حالا وارد شو:
https://t.me/betegram_bot?start=p7_r4EF37DCE</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/100058" target="_blank">📅 16:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100057">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vx2D5Fxnmf0ltr0Ej_FDFEGTdF3cBxD5KjK3tSIwb9JUg0UKgqDOCmoEdbK-d-V8bqhJkgo123FX905r1Ajy71U1V5aDETEX2821CF62mtanWPe7qgdhkfEIu2wHqvHj1vzp5pihzjrext6YlNmg4PQc5DKgvCZV5vj8a3cu5f9qX2xFEKaF7SyQOb26HI9ZewVRhV-qTMoINu97UfbW-XYR-MGfxRyV0cMhaIHWrNsIKVluz9qom2hb_WmK4nvnqpD6m_qy9HNyuARrk2Lzj46A0PFV43-xXKlVWR3k0p-8J_iQzI1Bpr90CreBFcjcmRJxVE5X3SF3OXEWSIHaRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
دیوید اورنشتین:
لیورپول به شدت به بارکولا علاقه‌منده، پاریس میخواد اونو نگه داره، اما این یک گزینه واقع‌بینانه است. تنها دو سال از قراردادش باقی مونده، و اون به طور منظم بازی نمیکنه و فیکس نیست، در حالی که او میخواد اینطور باشه. بارکولا در صورت  وجود فرصت مناسب، از انتقال استقبال میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/100057" target="_blank">📅 16:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100055">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b8b38999a.mp4?token=qdG_M67fqxzyk7nO0ZEH9JU1zsQyj740kS-USS2cjtitiopXVnlxnSGiz2MwTTxFbFgJhEMPyKE5QvhJ_tYFvEbom8vIm6FtUImOznp0Yxz2o8PFGHoGLTuusQzM0lotNiDVFDw_QTAVkZfrJZwyi6r_iz8QWTLekUqpwPksuz5mAzuRlpgqSVF1w-ZNBTbQibc1YzR3YmzAWEQ-BGzYWIGPt_KbPNoi-seDib1ydygnHwgrwR_1Eg7gK_n_YkbWaF2Qtda_TG-dzhXFFjCQ9k9t4odeQtHNBpmKFL5uDa8TGJgXwNg3I8ZYpjrpP76ers2QijeyVyz3xO8nmxQTurBCEHp8mqxOo7t1jO-POEL-EO4_MBZHmcoiH7peOXQa_MQbn__XRcmc187AFH1Pw8DI-WpRdfHUZzT4dWQW1FeRKEObrL9o6o3RE0XtvVt5adDMBPUeNcLJdKSZFNSmXi71MPoqYD8NX6ZKux-i3nkKyX3Gw-idusWwfUG8ne46lC02d5voPpe3NLMWezXLptqGkidwWsVsuNO47tiRPXpXbv34gIV-sqL0pQxbsW3rCKOK50F0YF7uILoeJOzu9NzD3Q29MFi1oqqRCueF2KZAgg3mpGJ-rym-hUHu7IEgiWY2gkjK2XOoNFXhCtgrQlA-A9Vn78mrmQKGyNLdDM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b8b38999a.mp4?token=qdG_M67fqxzyk7nO0ZEH9JU1zsQyj740kS-USS2cjtitiopXVnlxnSGiz2MwTTxFbFgJhEMPyKE5QvhJ_tYFvEbom8vIm6FtUImOznp0Yxz2o8PFGHoGLTuusQzM0lotNiDVFDw_QTAVkZfrJZwyi6r_iz8QWTLekUqpwPksuz5mAzuRlpgqSVF1w-ZNBTbQibc1YzR3YmzAWEQ-BGzYWIGPt_KbPNoi-seDib1ydygnHwgrwR_1Eg7gK_n_YkbWaF2Qtda_TG-dzhXFFjCQ9k9t4odeQtHNBpmKFL5uDa8TGJgXwNg3I8ZYpjrpP76ers2QijeyVyz3xO8nmxQTurBCEHp8mqxOo7t1jO-POEL-EO4_MBZHmcoiH7peOXQa_MQbn__XRcmc187AFH1Pw8DI-WpRdfHUZzT4dWQW1FeRKEObrL9o6o3RE0XtvVt5adDMBPUeNcLJdKSZFNSmXi71MPoqYD8NX6ZKux-i3nkKyX3Gw-idusWwfUG8ne46lC02d5voPpe3NLMWezXLptqGkidwWsVsuNO47tiRPXpXbv34gIV-sqL0pQxbsW3rCKOK50F0YF7uILoeJOzu9NzD3Q29MFi1oqqRCueF2KZAgg3mpGJ-rym-hUHu7IEgiWY2gkjK2XOoNFXhCtgrQlA-A9Vn78mrmQKGyNLdDM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محدودیت‌های عجیب هاجر دباغ ستاره فوتبال بانوان کشور برای انجام یک‌تمرین ساده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100055" target="_blank">📅 16:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100054">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed789cb4eb.mp4?token=UnrtCsob_gXWTSpOcAIKFdSqo63naEJ5s6GOtBYVNIx500xtjvWDPRSnR87o7QeOq2Tal5zj9-tXJ83y-xw-uHrRwSEBflLmY8DbLnshkuVp1WGE7zvZ9BFU3A85O6xLGlHCpBHqebPXXi51wQYMJ2reJmHWRWKO1eowLdbEwmhNorOZPOpE0QNQaT8NgY6JxTVRps8x3DNFvIMp54GcjM4vvJJZy_SMkWQX9E4ClU9pDAm3JkVY9EHDeOgm14blbFNaeEvRgqgS4Twj_i9mUHL1Wxuvt_MIcrvZOtBLk2BG3UZXDpE1yMuFCXHyL3BtkqI8XyNz36eZYz71BfDVPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed789cb4eb.mp4?token=UnrtCsob_gXWTSpOcAIKFdSqo63naEJ5s6GOtBYVNIx500xtjvWDPRSnR87o7QeOq2Tal5zj9-tXJ83y-xw-uHrRwSEBflLmY8DbLnshkuVp1WGE7zvZ9BFU3A85O6xLGlHCpBHqebPXXi51wQYMJ2reJmHWRWKO1eowLdbEwmhNorOZPOpE0QNQaT8NgY6JxTVRps8x3DNFvIMp54GcjM4vvJJZy_SMkWQX9E4ClU9pDAm3JkVY9EHDeOgm14blbFNaeEvRgqgS4Twj_i9mUHL1Wxuvt_MIcrvZOtBLk2BG3UZXDpE1yMuFCXHyL3BtkqI8XyNz36eZYz71BfDVPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
همچنان از احترام مردم روزاریو به لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100054" target="_blank">📅 16:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100053">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25d6661353.mp4?token=UbvQl2r91pjYV8pP8tpTdvXbQ9530XCZntUmH7a-PQDLbYzc9blPeV_U1Wj42ayqLfjQvwasvW1CQjN0d1MDZyQT0LZMHvsSnMa58qjMwoqly7E3ZjliTKPHXkJR1uvUrkxITwJyrCQw048i7LACD6mcNoTuK-JhTot7i9Mzg9Vi6CFfQLu-vbVapau84eg3SKfLfWzX2aR7IkFe5ro-0Fov3ePtYg4-8buC-qZL1hGAwYWWT3F4JzQipungS3u4l88cdnYaKjAhoFbU8KtTv8GMp6FE6zLI24bti0NoyfYl6lWwV-W071JCJXQ_ZieLoHFf2s1qOGvU_8pxm8Rj0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25d6661353.mp4?token=UbvQl2r91pjYV8pP8tpTdvXbQ9530XCZntUmH7a-PQDLbYzc9blPeV_U1Wj42ayqLfjQvwasvW1CQjN0d1MDZyQT0LZMHvsSnMa58qjMwoqly7E3ZjliTKPHXkJR1uvUrkxITwJyrCQw048i7LACD6mcNoTuK-JhTot7i9Mzg9Vi6CFfQLu-vbVapau84eg3SKfLfWzX2aR7IkFe5ro-0Fov3ePtYg4-8buC-qZL1hGAwYWWT3F4JzQipungS3u4l88cdnYaKjAhoFbU8KtTv8GMp6FE6zLI24bti0NoyfYl6lWwV-W071JCJXQ_ZieLoHFf2s1qOGvU_8pxm8Rj0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وسط مصاحبه عادل فردوسی‌پور با هاجر دباغ یه لحظه روسریش میفته عادل پشماش میریزه
😂
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100053" target="_blank">📅 15:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100052">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5bfb6b282.mp4?token=Yj3WNcjvwk-wyEDaRP58r1yKwlyK4anWwWsgQY0T2_YzJoTAMI1f2PozY97xeZw2VKVOMIiFaSLUEuCVkzMrihHNndshSklBdqOxagz_kzPFYDYlBrp4inM9iZMBS-aN-w4ImhespeL_Xuo2hv635IWVIm0TQEnR8M7C5Smu_z_GV_roUd6TQlEb92EtTKVvt7-YyLpCswCh3o0QV3wTJGuDq4QI78dNRqob-dJCd18UTrG-X65MTPJZ4IwOiwYnnUy31_mFP9HyJ3lqjjor1mKoBeBiBvGuuFv1ossaR6koJVlUa-ahuKgwFVWb_hOph9IfArxDXPX_GVip2DElZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5bfb6b282.mp4?token=Yj3WNcjvwk-wyEDaRP58r1yKwlyK4anWwWsgQY0T2_YzJoTAMI1f2PozY97xeZw2VKVOMIiFaSLUEuCVkzMrihHNndshSklBdqOxagz_kzPFYDYlBrp4inM9iZMBS-aN-w4ImhespeL_Xuo2hv635IWVIm0TQEnR8M7C5Smu_z_GV_roUd6TQlEb92EtTKVvt7-YyLpCswCh3o0QV3wTJGuDq4QI78dNRqob-dJCd18UTrG-X65MTPJZ4IwOiwYnnUy31_mFP9HyJ3lqjjor1mKoBeBiBvGuuFv1ossaR6koJVlUa-ahuKgwFVWb_hOph9IfArxDXPX_GVip2DElZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
💥
در انتخابِ دوس دختر خیلی دقت کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/100052" target="_blank">📅 15:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100051">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxcgB8nsPxxFx01At-T-qbPaWbyEVEIJDvP_svPi4wil1GfaLnuWQCO7xIGQQye0bkfQvJQF023KI6XyL4jTcNrmz_Fpiav0dUEb_QmHEvWz3zLKGFYskHONcriUIwnziqkW58NB-i3yQ_U6FTuh7mAdBgIGJq0gf0rXEb1IlNH-zbwnen10mtacdbxasA69WffdJNtAbqevyBRfMH210k6gfQxZD0c--WMpDZ9c-5qeKUMAx8cu8a2Udoujj4-VcGGx0y6S800AudCKXVp8RzeVmlABYR7XsdfPOfsApNf8tsPXBsBmanUY8rq3QDoTza5BR60V9sFaUz2fuwYlSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
یامال در این فصل، در تمامی مسابقات، 55 بازی رسمی را به انجام رسانده است و در مجموع 25 گل به ثمر رسانده و 18 پاس گل داده است (در مجموع 43 مشارکت مستقیم در گلزنی) و 3711 دقیقه بازی کرده است.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/100051" target="_blank">📅 15:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100050">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50041dee62.mp4?token=cyCqGPggZf_zcI10dwaPbKPVBEL1U4uRFIg9NlBZCN1YPwegbVfun_SEJb5sdisUE8F_RaigOS9r49OnMxE4UKNn1koSyFcQJSXBJHkTjyQIj9SU85CmL5zz6_pu5IbZ-VEJH0QXPfC2LIdi4sGJm8XKtSadlEzg9dAi_eS0TgE1S1U38wAmRyqez6Qqhjg2oZQ4tSLKOYFDWLKHC_z5w-zi4ZkhFc3ATbDiToDJDKSWUyzF02qbYup-6oSJZt_fNmCOfCho_66t0GR_5JI97mBITIuOhRZyjiy-kiNjM3TGVNzbaFVljbKbpTKs6kZpslooHrWc5QwpsTqY-a9QYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50041dee62.mp4?token=cyCqGPggZf_zcI10dwaPbKPVBEL1U4uRFIg9NlBZCN1YPwegbVfun_SEJb5sdisUE8F_RaigOS9r49OnMxE4UKNn1koSyFcQJSXBJHkTjyQIj9SU85CmL5zz6_pu5IbZ-VEJH0QXPfC2LIdi4sGJm8XKtSadlEzg9dAi_eS0TgE1S1U38wAmRyqez6Qqhjg2oZQ4tSLKOYFDWLKHC_z5w-zi4ZkhFc3ATbDiToDJDKSWUyzF02qbYup-6oSJZt_fNmCOfCho_66t0GR_5JI97mBITIuOhRZyjiy-kiNjM3TGVNzbaFVljbKbpTKs6kZpslooHrWc5QwpsTqY-a9QYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
جو فوق‌العاده تختی انزلی از زبان مریم ایراندوست؛ جایی که زنان هم در بهترین جای ورزشگاه، فوتبال می‌بینند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/100050" target="_blank">📅 15:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100049">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693e2b7cf3.mp4?token=BDXA-RlzIy56PuH0JRQ6IFO_p65qOVBxFczeBq2ZdO0gNmQHD93N59F2lzBSfdBtWx-Ky_64YlGY6cO3V_o0QRqXNwGfHnaC7w5fNLlvZIOBmxKNzHvztrV67ur1SIuq4Sb_gi2FSJgplfWc5X4gRAy-kx3pY_x7qwk_qpxv3caOv2m-7x4Cv99PIA0sZzUEeBoE-gaPHuYobKA3WLjdRhJQGUA3qsB-gVXNRsHw9-98YNmElW1NgeowOr5XvOAiY1yp43R6Lklxr22tSnv6W1183YvS9IF8krN6NCuTTXw-jo8EDE7xnBXmdTyYrLOOU51cDn9FYbnrBQakpZBEXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693e2b7cf3.mp4?token=BDXA-RlzIy56PuH0JRQ6IFO_p65qOVBxFczeBq2ZdO0gNmQHD93N59F2lzBSfdBtWx-Ky_64YlGY6cO3V_o0QRqXNwGfHnaC7w5fNLlvZIOBmxKNzHvztrV67ur1SIuq4Sb_gi2FSJgplfWc5X4gRAy-kx3pY_x7qwk_qpxv3caOv2m-7x4Cv99PIA0sZzUEeBoE-gaPHuYobKA3WLjdRhJQGUA3qsB-gVXNRsHw9-98YNmElW1NgeowOr5XvOAiY1yp43R6Lklxr22tSnv6W1183YvS9IF8krN6NCuTTXw-jo8EDE7xnBXmdTyYrLOOU51cDn9FYbnrBQakpZBEXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تنها سوغاتی ارلینگ‌هالند از آمریکا
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/100049" target="_blank">📅 14:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100048">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKD7GZjGhHwWccrU2Xh8Vif6Sf6ZQ8rjYtrZ5dC1zvRfP66ix4Qml5aRxL09Oe6CdL5qOgrZzrDwWfDmqZL-RySHXBaYE838vEO_CeGR9JmZyDr3fuaXcO_SeGE-ftZ0f3Ck-jS0ihFXp8bO9QNi-TkOYJ8KUzrQ6nzuvQjxJyUAwzqgFrkq_aQ0WMm-D03wnhj-NbzcDNfH2WBPKD9x6sBvlMv50p4lZcua2n3LnMZUcZxT6hbhlE1iMyTuoypBA_YTnN9pnxggOOu6iLqWA5awSjrRepA3tQ8fsyGk_CvJb39z19vPOqU6ZwQq8dBEXjBVXi3O3VSblH0aEuJkZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
🇪🇸
فرانسه برای دومین بار در تاریخ، در جام جهانی با اسپانیا روبرو خواهد شد. اولین بار این اتفاق در مرحله یک‌هشتم نهایی جام جهانی 2006 رخ داد و فرانسه با نتیجه 3 بر 1 به پیروزی رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/100048" target="_blank">📅 14:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100047">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t95N5IBBt39kLy21sztBfaeXCezWhcRa9BfBCxDranTa60VsPhlWgOYScVY-0IDxsvjFRYyZvki70Gxu5ioKNM1-OUECL7ClRuDw_5LO5tX-GG1sPk1pPERFrhcQyJityfOCEB16AOffGJmIWhgs1d8RulmbSNhWHrTxnV6DRgQXAjIBeLKw4DL_oxPbyN6sFyn3fJog0FICORDLSM_G7aL7BQIrjGUh27f-6zk8mujDMwaoyC-hiybXJNShUQetHS8nj4BCYwsITJzzB4iNYJKuHwGtW6gq3EGBvaxEH3o7SE4tp87RKIt2J8ayKSw-V43F8q9pnsMGrRQR4UV2Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه عملکرد لیونل‌مسی در جام‌جهانی ۲۰۲۲ و فعلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/100047" target="_blank">📅 14:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100046">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBlrru3acpDuA3ZKUt0KJg2tIIBd0pmVVrch-b5NdMvmSsAJxYNvjiqRVg3RADHWQrLWCGEyOpzNgvfoolULfLmQVR3PqPAy_ecv3o79f7VAvTWegQmiXtTwqnLP0Q4LdTpanJJiBhvJ4ZKIOdtlI7ySBGckCATiY9tWl642k9YNXSUSp2dU-KUbtpbzOyL-wkFRaGCAmSfef9mVD5LnVQkeMzj8gu-ML8E90mLkTko4hfgFO5I3mQrBdcg5ub3OwPxglo1GgmsPfhdZBeCouZtjutpQt0UEGIJGQtaV8z8Ek0ArMOAJQXsusO96NMkAclIUoBr-IOdor65UjFKcag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اسپورت:
خولیان آلوارز با وجود پیشنهاداتی از پریمرلیگ انگلیس، علاقه‌ای به رفتن به این لیگ نداره، خولیان فقط بارسا رو میخواد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/100046" target="_blank">📅 14:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100045">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mD8YF3XU9cRtVEhXvMmSoh-mLzlGRu63R30rhymlBqGeAeUp8qCic2PAyv0VeC9cqA4aMmRpy-T7gnVs-vo6_fC0X5NmkHVWvqDMUh-pBaytplbXQ7QbOpze1IKVPIlFu39hYOJOvc9bNdvXGAYvKqIAbz88-NeiWRaqTex32eEV5BSyYULr-yRDOkwSTmwRc9RjNNZF5P81PEoURxMHg0ERjzz4eIpFx9hvN-8nFH1H8c4DQNibYfCa5lpyf3Dbb1TZKrWoUnNmP6nZndl0uklTmLhij9Clh2KtVfKDlXXY2xctHWfpAis7e8O0PDrKQPlx5tTcOhGvtkiiJ99iag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ساشا تاولری:
الهلال برای جذب سامرویل وارد رقابت شد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100045" target="_blank">📅 14:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100044">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3edea28603.mp4?token=AUwqoyq48FkOa5lOAdghuii4WYbtVDOqCDGRmBmSGo-O3PFwtnLsWDWzP8UhflpXWSjjXC02FTXTUAvIhyAod8zNLCZTYkXpBPpWnqOEHP-t_3U2fOq7Tpg9We9iEzhHjMSn2x_6iz0OO3TrgaWw2ivXO9IYU2BOYn1xsRARsuQXykDFv9NXMSt0dFFA2Ry2Bc9PtrE6uA018-gtlXTqrKu650XbTUcbNFsO595SRqUj_XbkAWLooGvDBD57UyUe7QOX_cOGvRvXzARzzWxKJ6kk6S9Nuctv2tw05xHz2XQsd9jE15XK0Dd_7_f-KbJXEJ9S936Iw_UaMLrBTLVy-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3edea28603.mp4?token=AUwqoyq48FkOa5lOAdghuii4WYbtVDOqCDGRmBmSGo-O3PFwtnLsWDWzP8UhflpXWSjjXC02FTXTUAvIhyAod8zNLCZTYkXpBPpWnqOEHP-t_3U2fOq7Tpg9We9iEzhHjMSn2x_6iz0OO3TrgaWw2ivXO9IYU2BOYn1xsRARsuQXykDFv9NXMSt0dFFA2Ry2Bc9PtrE6uA018-gtlXTqrKu650XbTUcbNFsO595SRqUj_XbkAWLooGvDBD57UyUe7QOX_cOGvRvXzARzzWxKJ6kk6S9Nuctv2tw05xHz2XQsd9jE15XK0Dd_7_f-KbJXEJ9S936Iw_UaMLrBTLVy-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
نظر فابیو جانواریو ستاره سابق لیگ‌برتر ایران درباره عملکرد امیر قلعه‌نویی در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100044" target="_blank">📅 14:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100043">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2OkSvZkN3nsnJPrLgPlibOXBQ5l4zhFhmG5umljwUx65qARX0tCAnF2NnlwkNgwAi-2OwPfM8D_2CthL3jmA7j15j8QW-pSyNvqShHWdAOV5DM_b51xBqvQJNwcVgpMVUN9AFb2cM53Mr-pcOur-KF3UGwFMdL49lunIwTadv_2weQ7oe9e0hw0PmapSEcu1jjHReL4-w1n4-W3jf3QVS6DZxVqF5wtiArmlfPvAKeqF7p5zv4MaxTcRVcwIpBCWepVgz6wpozV6V4u96zH_UQw6VM1f-DYJqoIZgASKqGnzek47xDhi_FIgr4UrTU12TUXs8xWNsTVlQGgQnFYFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
ترکیب احتمالی تیم‌های ملی اسپانیا و فرانسه برای بازی با یکدیگر، طبق گزارش مارکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/100043" target="_blank">📅 13:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100042">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2af31abf33.mp4?token=toE9u5s7M_chwBxkSTWlH8ehnkLmZDA18OD04mChpD7QkiAH1pnLLMJc8y4O0Xm7TsR-YZS4BJZYhzRN5VIUena85UiiBwQSn0kmZlk5X-76tDlAoab0ii6IoM5IJ9OGz-lck7UqYbkZR-LVcVs5NymrfSy7nkeonecmztwwbpTydaZp7vR4TsCX2OP0o5mr92IJ_QBHyEB6fkp4BcTmSmmfwnkViVaYofUwwV3CtVPrvsk-THMqTzU9a2wDQUDmwckgaPuYkW1bhkr9mtxDQ5zKW_rERtbMbttHJRoJGyILdfADJ8D3IJfMw-EHxh5w845zGEKp2VIB6WkBnIaN4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2af31abf33.mp4?token=toE9u5s7M_chwBxkSTWlH8ehnkLmZDA18OD04mChpD7QkiAH1pnLLMJc8y4O0Xm7TsR-YZS4BJZYhzRN5VIUena85UiiBwQSn0kmZlk5X-76tDlAoab0ii6IoM5IJ9OGz-lck7UqYbkZR-LVcVs5NymrfSy7nkeonecmztwwbpTydaZp7vR4TsCX2OP0o5mr92IJ_QBHyEB6fkp4BcTmSmmfwnkViVaYofUwwV3CtVPrvsk-THMqTzU9a2wDQUDmwckgaPuYkW1bhkr9mtxDQ5zKW_rERtbMbttHJRoJGyILdfADJ8D3IJfMw-EHxh5w845zGEKp2VIB6WkBnIaN4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تماشای فوتبال در کافه‌ای وسط استادیوم؛ دیدن بازی فرانسه - مراکش در یک کافه که نزدیک‌ترین تجربه به حضور واقعی در ورزشگاه است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/100042" target="_blank">📅 13:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100041">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff64783daa.mp4?token=HxRRaPzFsg731n-t-tFU-DZ8wXOVae95_DesjnxDrdqYOycRl2DRzQcBTSMd-NRE5zPVh3itmErvnD_fSCawqiSId5P2EseqA_LkDqNtFcmb8O9y_cRzLa2yV3Mls6OftXQ_MA_TsnnQzjJ9IPhqtX3g1WgSMj1VVxVNeM89vOC0Z2Bbte_SSnJiIFaFdITR37H1HwdG7ZWw8-ljVvAJEJ0eBTTWz0SALo4rbmUKALWhKA-Jh-pXGLEVZbK6CvhEDPZug34I9vWwph-bZchhoe3vdRhfh7Pz_zQYunTVfW0dCpKLXJpYNToVOdrTFL_ZC1rkH_QwRhzGrHu_7KEw2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff64783daa.mp4?token=HxRRaPzFsg731n-t-tFU-DZ8wXOVae95_DesjnxDrdqYOycRl2DRzQcBTSMd-NRE5zPVh3itmErvnD_fSCawqiSId5P2EseqA_LkDqNtFcmb8O9y_cRzLa2yV3Mls6OftXQ_MA_TsnnQzjJ9IPhqtX3g1WgSMj1VVxVNeM89vOC0Z2Bbte_SSnJiIFaFdITR37H1HwdG7ZWw8-ljVvAJEJ0eBTTWz0SALo4rbmUKALWhKA-Jh-pXGLEVZbK6CvhEDPZug34I9vWwph-bZchhoe3vdRhfh7Pz_zQYunTVfW0dCpKLXJpYNToVOdrTFL_ZC1rkH_QwRhzGrHu_7KEw2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
🏆
موزیکی‌که بیژن‌مرتضوی بین دو نیمه فینال جام‌جهانی قراره برامون بخونه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/100041" target="_blank">📅 13:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100040">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f3cb94583.mp4?token=ayZxxVxAdGKEZoqIbXrtNyUTSPkJED5F1U5Jn7bZff9jtcsG-MP_vcxqMsxqAno5rxD7hnrEBZ_Sc8S7sNg5bIGOYNgenZjOO1ACBlkQ9aK1EYm4aorF2md3lZHCBUM-5o9FqvHCvQNjOlrdr-Zife6Ak11BzFdIa-lqWK8_hO4rMANSiv7fy8s6yMoHjpmKMI0wr-EUBrmGWkY64GfWp0sYRQV80FAb20mc1K1IuY98PXpAJPeLR92Ilom0YqSbMQZOhs2ni8lsvgSmriNBiWYlHR-uHyVqC1OvjssNEPL8gL0cHM0kbtcrZJs-Ti3J-bz89kWY1Vi_FB2YK_uopw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f3cb94583.mp4?token=ayZxxVxAdGKEZoqIbXrtNyUTSPkJED5F1U5Jn7bZff9jtcsG-MP_vcxqMsxqAno5rxD7hnrEBZ_Sc8S7sNg5bIGOYNgenZjOO1ACBlkQ9aK1EYm4aorF2md3lZHCBUM-5o9FqvHCvQNjOlrdr-Zife6Ak11BzFdIa-lqWK8_hO4rMANSiv7fy8s6yMoHjpmKMI0wr-EUBrmGWkY64GfWp0sYRQV80FAb20mc1K1IuY98PXpAJPeLR92Ilom0YqSbMQZOhs2ni8lsvgSmriNBiWYlHR-uHyVqC1OvjssNEPL8gL0cHM0kbtcrZJs-Ti3J-bz89kWY1Vi_FB2YK_uopw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
پیش‌بینی قهرمان جام‌جهانی توسط گابریل کالدرون سرمربی سابق پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/100040" target="_blank">📅 13:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100039">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8026afaf.mp4?token=WKTa-e5GsmXs01dBOvD3JEnUEMtW9B39l7oe2mWOe96bt4mVuXzn2Lz57wND-2sgBFOgqG74yg5z3rmKvzu4BQTFT4oI9dKjMWCAOF73u-l1bspjp48TKC-S_YvgIQTo3tQsDFLhJxhl5FdH_R7JtPvjwd_v8vUUN3kQyrN5a_pJ9W7PupzwZkmg9b6hdTvRwl6oi9KD6k0MQuxYCqu3qcr2eot2kDOeebTiLvkg4CtoY7fLk6vh0mChG6nHmOfIncsWK-GsU-GEKZg7b3k-mYzjPg8unW9DOaZj2JdZHpWuL2L-N57oDw7ifsMNwnm3s20CnyoZOuZI8t4sB2vMTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8026afaf.mp4?token=WKTa-e5GsmXs01dBOvD3JEnUEMtW9B39l7oe2mWOe96bt4mVuXzn2Lz57wND-2sgBFOgqG74yg5z3rmKvzu4BQTFT4oI9dKjMWCAOF73u-l1bspjp48TKC-S_YvgIQTo3tQsDFLhJxhl5FdH_R7JtPvjwd_v8vUUN3kQyrN5a_pJ9W7PupzwZkmg9b6hdTvRwl6oi9KD6k0MQuxYCqu3qcr2eot2kDOeebTiLvkg4CtoY7fLk6vh0mChG6nHmOfIncsWK-GsU-GEKZg7b3k-mYzjPg8unW9DOaZj2JdZHpWuL2L-N57oDw7ifsMNwnm3s20CnyoZOuZI8t4sB2vMTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای مردم مظلوم جنوب ایران
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/100039" target="_blank">📅 13:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100038">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIF4HJp7B7ig0nQdpHEnmADMtypaVLJ6yS8yaH5ffYautWbUXHRctES4gegaoYFFZN-YcdIsyOBRrQjXNSxyahR2qBd7HVR2Kh8ogywR9TdPrOpPwhprYDnfMo3C58u44x-tR6ghUsDHaty2CVJHor2m24rCBS4SdDI4ox3GeQbiGOtVQgNL6W_6gX00wphTCB6gqLGOeHQN0ZO-Oq-rF__WWl-b-7PTYsXsjbVxMKY8DFJsQY4mqYZTunNhopzWhEtrYjVJd1gI1bl42gbQBEFtVe79Psc1Qv2iHWQEoyNvy8zRWrUbcJlQNUAQyazcjkDZLr0i5PfV-bC5uNPjuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
قرارداد امید نورافکن با سپاهان تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100038" target="_blank">📅 12:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100037">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec7a16d712.mp4?token=uMA6J066LTIliZ-EGkmtZJO4ICmAJtBKwGT27yCCr9h1ZLK9vilYuwu_HrcvlouOZfGQBWOjV4P7umPaRG1q86mNJ2bu-3-V2ZMcUMVcO0WA_2zi3RtqxuoN9XVyWUi9Y6otPGDem80MvOWXk_RbstXdm49MSfdXkXapjv904X_RL88Szye9Gy0-PUz0dl-A8O_JEYOUVBilVHcdz3fhmEy2RP2VMWvIf3N9O_W2UhLbNfeEtNO2ABPgsq8GTRnfucCShT3bkoapRy9ScP_yRBVgPHoDme6GKeMwt38bGzJnc1sqejC08UM8qONAxS672fTSQ6j8m1Lnpd_2MKmHjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec7a16d712.mp4?token=uMA6J066LTIliZ-EGkmtZJO4ICmAJtBKwGT27yCCr9h1ZLK9vilYuwu_HrcvlouOZfGQBWOjV4P7umPaRG1q86mNJ2bu-3-V2ZMcUMVcO0WA_2zi3RtqxuoN9XVyWUi9Y6otPGDem80MvOWXk_RbstXdm49MSfdXkXapjv904X_RL88Szye9Gy0-PUz0dl-A8O_JEYOUVBilVHcdz3fhmEy2RP2VMWvIf3N9O_W2UhLbNfeEtNO2ABPgsq8GTRnfucCShT3bkoapRy9ScP_yRBVgPHoDme6GKeMwt38bGzJnc1sqejC08UM8qONAxS672fTSQ6j8m1Lnpd_2MKmHjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
برای درک‌صحیح خط‌حمله تیم‌ملی فرانسه :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/100037" target="_blank">📅 12:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100036">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sm-upj4bm-d_c4OF2UFaPmDMXNnMx_D0826Ik0YQ4zSQvqydT4pu8xRqywIz0kJ59XrNBuvV39KK0yyshTis08Sws31nAOAhWet67aUH_Em9stxoZ0dqpP6JN3iyJXdt0gnXflk6NwegerYImAh19nvmc24Ue4rTvR8lrtTTSPht7yg98pQfbeo4Mt5gbHNF-AeK75mb7TEPYanwNh70f9AaqhCV8gssHtnRipBav0MpgJ4p9gApuInNzC1uGO2WWt5WUU07rO09Y7o9ScLI6CW40Sw6z7xTE3KL-mmQlMp7KsLi90MnDhIm2f6GEjkX0y9_DCm2tszedv-P3mL5rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
قرارداد فابیان‌رویز با پاری‌سن‌ژرمن پس از جام‌جهانی به مدت یک‌فصل تمدید خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/100036" target="_blank">📅 12:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100035">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZANI70LVUjDCqNmso27XTOW-UeGn4PzhfjvXzdcu3-D9B5HvPBo8NYsRwQs_ZJT6S6HQcYyTx9qtSe9TIWfPleUPSnEHYXnTjnZSloHIAQkUvkKyTrU2fx6vfvGFs0xxxGeloRnvrugjHH-sMrIalrk9VADTDF0nAnZXsQSW1XFKd5cVE1X3q_ehbtYFvfbJlt3vcP1L2-UjKW9a_kZQGO6Si35kYULE1JxlgonfXs8B6v5vqIE8u6R37GLLV8AXv8rbOVeLaUmk9AviVltHjRwh0DyGoggWuUittfXnxngEsnCRy_RjvPTnO722i90HUzjtMKzuzGTTqffA6ijiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
#اختصاصی_فوتبال‌180 #فوری
🔴
اعضای هیئت‌رئیسه فدراسیون فوتبال در جلسه خصوصی روز‌ گذشته درباره اخراج امیر قلعه‌نویی صحبت‌های مفصلی کرده و خواستار رایزنی با نهادهای امنیتی برای برکناری این سرمربی پیش از جام ملت‌های آسیا شده‌اند! چند تن از اعضای هیئت‌رئیسه…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/100035" target="_blank">📅 12:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100034">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mssrCEQrmsle3mItVnvGiBPLbzP7ViqR0mqOcjkOveYNY1aYf9lWh78MiAB_mowa3RbofobH89KkKb7hxpW9pUoPlBBos_lz3_P0oC1mqRIzof1rCYOEqlAimEUC02i1l87xaheyMPH3VQCC1T5oEqocmK1nmlfI1_tH3PEQ9E3BRddru7XfGgv43nCHVJNxzjbQIKVi8QUUwCLJeSg2IUO-T7QelSo3FbpC6NztuzUVGBVXcb6Ip2ioOdvM5L2D6Y2wLo_V8trY0ugdpta5dTkQk9-p8BAzKVjbCRBp0X_QAgjlhHYmv7xMJXVbkB4WAtX4mU0iaxByVq-_vmrGHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از دیوید اورنشتین: باشگاه منچسترسیتی بدنبال عقد قرارداد با ایوب بوعدی ستاره جوان مراکش و باشگاه لیل هست. این بازیکن ۱۸ساله ترجیح میده یه فصل دیگه در لیل بمونه اما پیشنهاد ۱۰۰ میلیون یورویی سیتیزن‌ها ظاهرا لیل رو وسوسه کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/100034" target="_blank">📅 12:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100033">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
🏆
🇦🇷
ویدیو جالب و جذاب از نمره‌گرفتن لیونل‌ مسی در بازی اخیر مقابل تیم‌ملی سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/100033" target="_blank">📅 11:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100032">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cc8dc3115.mp4?token=r8ZFjQX976y98_7AZbz8sprGOWZal4IoOR86ev9bZhZoATRKpfZ-rnmv5eH0wTUBoRVTAGjGtVZ0h049NCoks0g1BV1S9jmod5sVW40FkcUcgo7ffMxS3_Lb9LXRLsYhFivaLHrHcTzQP1pUe0YU5-9ly9OpFHSb5oMGWuAJgFf7Bnnv7564zv6dxn0lOLPvT1T4PYOplPM8vLkZkvRJs-isT7OWR-jJ9WKXxAn6UbasLqaYhmkvTY7ZtV5_LLXKmAO2Q5S4K2wErldVzSW9q9fdMddsa00wuET_dB4U7p7nunPsH2MhLGjhxuSrwxOooEW1J_NZ-aro9hQ4Sr-aI4SB6yIzVhLRcO0vVQIhaFhIWxLWdvZAUjzDE0IrN3m44z1YCCbXtra17OOxek3-P8DCj4WvmvxG0HUz0V7ShMRokJMPsdaD2rldPu1rhQpTn0l5tCfTDw3XXZezGaSyoUEbuGwuyvNR7pOlRJRAo2axBPEea0ZDPz1QRS1KiFnWFOc0Y4v9WkCCgMsPARpP6p7iTpsJgqnOQ2Elz4YHXdKzNBglEdkZR7p_KDodwvexrCYRSKkDiUcxzd8RRkMiwvbsfWKtVCzUmp5nEskcZr8j0hbHt4J_qUSXVTqEIY0a5N8NXLa3iCKJ332PnOJJ5lR-47_ynk-hA4iBteO4iTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cc8dc3115.mp4?token=r8ZFjQX976y98_7AZbz8sprGOWZal4IoOR86ev9bZhZoATRKpfZ-rnmv5eH0wTUBoRVTAGjGtVZ0h049NCoks0g1BV1S9jmod5sVW40FkcUcgo7ffMxS3_Lb9LXRLsYhFivaLHrHcTzQP1pUe0YU5-9ly9OpFHSb5oMGWuAJgFf7Bnnv7564zv6dxn0lOLPvT1T4PYOplPM8vLkZkvRJs-isT7OWR-jJ9WKXxAn6UbasLqaYhmkvTY7ZtV5_LLXKmAO2Q5S4K2wErldVzSW9q9fdMddsa00wuET_dB4U7p7nunPsH2MhLGjhxuSrwxOooEW1J_NZ-aro9hQ4Sr-aI4SB6yIzVhLRcO0vVQIhaFhIWxLWdvZAUjzDE0IrN3m44z1YCCbXtra17OOxek3-P8DCj4WvmvxG0HUz0V7ShMRokJMPsdaD2rldPu1rhQpTn0l5tCfTDw3XXZezGaSyoUEbuGwuyvNR7pOlRJRAo2axBPEea0ZDPz1QRS1KiFnWFOc0Y4v9WkCCgMsPARpP6p7iTpsJgqnOQ2Elz4YHXdKzNBglEdkZR7p_KDodwvexrCYRSKkDiUcxzd8RRkMiwvbsfWKtVCzUmp5nEskcZr8j0hbHt4J_qUSXVTqEIY0a5N8NXLa3iCKJ332PnOJJ5lR-47_ynk-hA4iBteO4iTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیش و مات شدن استاد کسب‌و‌کار مقابل ابوطالب
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/100032" target="_blank">📅 11:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100031">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/601b5e5990.mp4?token=WtAx_w0tOxphklPh6wykhFuyJ1u9VpzoGmot_o6ir5EJEYdCQU2LpDsab-aTHh31R-3CYy4uDi17k6LNTAhGErL4eLjOefBVGgzg8AEC8a9oTb4mSjUid8Rx-56CWS_znsMewJ0VQwJg3kuz1Z2DCM35r0ZqtZwFMOwAaKyqKdLy1ORmFx8aQEJ2NZFwuBYwJkcs6iMCzMpjEJ1H03ItpFrhphXa0pSWoF3NG4hiM0ipEVo78jt0zglH3JExihwb4Lo9-8rIDWsUmAGd_lKsdTVgdb3vne2ywRh1vM1OVUdT7FsDvOjpbnmYjxDJ5AT81d4RTOF7pXD1veqvDIzrCoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/601b5e5990.mp4?token=WtAx_w0tOxphklPh6wykhFuyJ1u9VpzoGmot_o6ir5EJEYdCQU2LpDsab-aTHh31R-3CYy4uDi17k6LNTAhGErL4eLjOefBVGgzg8AEC8a9oTb4mSjUid8Rx-56CWS_znsMewJ0VQwJg3kuz1Z2DCM35r0ZqtZwFMOwAaKyqKdLy1ORmFx8aQEJ2NZFwuBYwJkcs6iMCzMpjEJ1H03ItpFrhphXa0pSWoF3NG4hiM0ipEVo78jt0zglH3JExihwb4Lo9-8rIDWsUmAGd_lKsdTVgdb3vne2ywRh1vM1OVUdT7FsDvOjpbnmYjxDJ5AT81d4RTOF7pXD1veqvDIzrCoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
تیزر جذاب از بازی فرداشب انگلیس و آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/100031" target="_blank">📅 11:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100030">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c8d222e07.mp4?token=PMgqZGsFEOTB_Cj4VTSfc8zLhmchjvLi6bdBaGwGW56aAetmEtJFeBJlzu8oO9cdaU4qmz_GxrCgstqVvO35eEx3p3YYHXGXvwLWbadrDFkKQ8elxaR1NDwkc8c49CUI9_p1F2wni8yaz-VxzSc9Q-V1lsy_eSG8wOGmLSOcfZ9MxCfC58kp9-vSW5EFMNk09ncz1YWbq93cVq39Z_TU2ADmhYmknOBFyDkCZPPZ2XId_5iZgDGYg6Ro3Noafy_XKZ6RyyouvtZVRwBTQr7XYooUH-nm03Po4875EAMzYRi4dB5devLGy3TZgmHV0b-Ruqnu2p31keDeXXE55zDIUjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c8d222e07.mp4?token=PMgqZGsFEOTB_Cj4VTSfc8zLhmchjvLi6bdBaGwGW56aAetmEtJFeBJlzu8oO9cdaU4qmz_GxrCgstqVvO35eEx3p3YYHXGXvwLWbadrDFkKQ8elxaR1NDwkc8c49CUI9_p1F2wni8yaz-VxzSc9Q-V1lsy_eSG8wOGmLSOcfZ9MxCfC58kp9-vSW5EFMNk09ncz1YWbq93cVq39Z_TU2ADmhYmknOBFyDkCZPPZ2XId_5iZgDGYg6Ro3Noafy_XKZ6RyyouvtZVRwBTQr7XYooUH-nm03Po4875EAMzYRi4dB5devLGy3TZgmHV0b-Ruqnu2p31keDeXXE55zDIUjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🙂
تفاوت پنالتی زدن در زمان فعلی و گذشته:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/100030" target="_blank">📅 10:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100029">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfflKTWlocuF4w3-CFJxOd3QSWw0girBBxOYcV_U3oaq_OYa42EbhKJe-XiPAF1dOnPfPQsG2t42yEo7qDs83YBPpElmq5dGcPV7zuUWGKMqYUygCrWaPIJy6lXUR-eu-ntivsukzwx2kzWBdoycjCNQ4zymtwCP7xBJcEXhJ9-12rHRj1p2tS72dGHOCCcp39agDox-Gyu3DTf4U4_dvTCXCk9YIgYhO-S8T8FIE56D2KFPyKeUd6dIQq5tdmvPGiBZrfHdU4M9SeG4rVZ63aKaNuWPez4LA3u0VitAmKk9vKvLxMtf3VRMnM9mME8q6BGhR5Jhfg1kiLRto6QJqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اسماعیل‌الفتح آمریکایی داور بازی آرژانتین و انگلیس در نیمه‌نهایی شد. ماریانی از شانس‌های اصلی فینال هم داور VAR این بازی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/100029" target="_blank">📅 10:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100028">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e78e4370.mp4?token=nr2lWi7qwbU1jZZnHnksB3e5prQAS5L0I0uTYE_t_D9X9pPFE29NGmfRBVoNTDwgwr7tzu5Ghzb1gxNtdQTzJepFN2xoERx9zRtQHeDQowx5kgDfIFLcfPJA0Nc0UAGcEwuFG3KaLn9OEgLLZPEnSl7gOzpO-QnIh2ZfrKJG8EO7KDxWL9cYnxlJtvZN2BcUmbX5nDIC8f5rJNlQdYUJ-PgnTXNpYx48FGL5K-ct00HRw_KEEl0JIRq1jD0BMu_qlxgsckbgYzCXTvE8pEuYSXW-Mf3tk9C0Q48fFU5LmVPqen6s_pgsZjpkFtv5dK0tZy_pSDa_yTLgdO6wiu8E2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e78e4370.mp4?token=nr2lWi7qwbU1jZZnHnksB3e5prQAS5L0I0uTYE_t_D9X9pPFE29NGmfRBVoNTDwgwr7tzu5Ghzb1gxNtdQTzJepFN2xoERx9zRtQHeDQowx5kgDfIFLcfPJA0Nc0UAGcEwuFG3KaLn9OEgLLZPEnSl7gOzpO-QnIh2ZfrKJG8EO7KDxWL9cYnxlJtvZN2BcUmbX5nDIC8f5rJNlQdYUJ-PgnTXNpYx48FGL5K-ct00HRw_KEEl0JIRq1jD0BMu_qlxgsckbgYzCXTvE8pEuYSXW-Mf3tk9C0Q48fFU5LmVPqen6s_pgsZjpkFtv5dK0tZy_pSDa_yTLgdO6wiu8E2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
وقتی عمو رشید میخواد سرمربی باشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/100028" target="_blank">📅 10:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100027">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gF81dNQb_V1Ct4wKMpmeYDXuiwxhrMYqI8iVaaXwL3T4HRP3k7Qhuj_iwDBAibn3zcVu-r0uze_voxHGGUzNLnlMX-5qPAOmWHbVw07pDMIGuktXXPOEfs8lnfgux5pWCscxj2hKasRXr-Q8gG_cWzlbvkUmln6q3MZzgDtL-hEU4H7Ks9DOpLakz3UnROldx2ODDh9TDgZkvbDry0lp2hJUzeF15Z2FD-0iy8BTxN_JvYLuK7DjLE4iozNuNmeQZOVCvWocWnXhc7navfl979iVtaR0iXVfglq7Hh8GbixCLHWStdmVy1SDAhQAzrdeYa5vj0ADtNUYgCutpX0UuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇧🇪
#فوری از رومانو: یان سومر گلر فصل قبل اینتر به کلوب بروژ بلژیک HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/100027" target="_blank">📅 10:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100026">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/020f9569b8.mp4?token=VS4bUt7jbr9ZYFWpQj8DAHyVsvCfP0lnjAGFTQPRnhm2IREFB8r6K8Bd51dEh4-ZtLP39qHBsBgt_CP45HraWn1yVXP4R1uyAS7Y03JmOfDhshl7lTiHMjpdbePeHgZZ8PsGxn8HVgTlX998VBWbhSY_xv1dwE8Vboel87jkyCTm-ihBkgiNLYoG9CukefIMRgYFjM64m5-LaLcqSx8vwtVB0Ck7uEnixofezFwDPrjpRc59iyQpu33JNRN7ufLW2dgsoyWanX00sq9AUjP1dOXAAu4Iy5dOJpJlN91vWmHoIfbSgQa52EypLDrYDPaQ6orRWlS5G2laothM46yvhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/020f9569b8.mp4?token=VS4bUt7jbr9ZYFWpQj8DAHyVsvCfP0lnjAGFTQPRnhm2IREFB8r6K8Bd51dEh4-ZtLP39qHBsBgt_CP45HraWn1yVXP4R1uyAS7Y03JmOfDhshl7lTiHMjpdbePeHgZZ8PsGxn8HVgTlX998VBWbhSY_xv1dwE8Vboel87jkyCTm-ihBkgiNLYoG9CukefIMRgYFjM64m5-LaLcqSx8vwtVB0Ck7uEnixofezFwDPrjpRc59iyQpu33JNRN7ufLW2dgsoyWanX00sq9AUjP1dOXAAu4Iy5dOJpJlN91vWmHoIfbSgQa52EypLDrYDPaQ6orRWlS5G2laothM46yvhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طوری که رسانه‌ها از داوری فیفا برای آرژانتین میگن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/100026" target="_blank">📅 10:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100025">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uY-JJSHE7lBL0xpxnGALHK6cMZHldUw7ONR29fm4LEvgoC82FUaJxFzHJGJ8Lc8NoHOglrgM0fNnQglfMZzsPYON-ORikzJoNLlPhnlPduuEmEM8v-lKZi9tHgIBbpyW82ShA_4m9YR2qmeyO6Ba-z3kjSAlxjOdnEac3thA6_6-8hpv8M-YQEtydUC6nwobM1naWPZjrwDbLNB_vHNg5dvOuEuVJrwC_yDHpYHImLDhD1AnFjCcU4BjHvLL5lJkj-gZjs4Qbkf7Pz7PIIxgFjgBdnX5ugG50qsUgMC2bX2QrUk4fYYptiwb2q7GyIW5-vW4eAIO5rSWC8gSxmY61w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏عزیزم ولی این نیمه نهایی جام جهانیه من که نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/100025" target="_blank">📅 09:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100024">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd1d85494.mp4?token=QP1Yum_xkFzCkmljDYjwm6gkGqYULrZYugCned-eG3-H_TqB1A0t3TmdNtXeA6f0gg-ZUSp6Uj35qW3j2PWWtS-Sv5Oy_O9LbExNOAz5PvzAQmdJ6oTbXFUt-hqqnvTLZIxL2XpV7pxWuhXmiZtfaspeL4NzDqXrWAWXudzFuCbT1kQQ2K6UOz1-V6mpYvfsCaPiFUtOx-XBx44XTf6IByzbUcq6u7WavjCKybzZO_AIUqvVq4lKS4fZfkmC2GT7oUeGpbDcT3vwY_vBonL7JeAr40FxEzdwFyg2B4N_DfxOtVsCAOtUJME5STjvSSzs9qCuwCtgEuIxvaxzFgaecWbZ_9pT9LQpVHAZYwztp5xefsXFpnww01NDKp9VAoyA9PCMkKf304j5vyLp6bOOBsDdukKsLt32bNfrT9qSIqnsAUAdBzs4whKG0oNK-ZW3NhAu4OoxGVn4YznfmrILxSwo-JuZUJnfOiWBbWcJUi2tgL1hnD1fjkOZNRMlPUDmclZhJo5YmIb6lMQGcXrk1EsAbdZnNxTktIqHgm1G2sbXCPb4fo1LUEfEKQxGnWxvWs8hfcghSBfduyM1MdJZXxa96ARRdReDw8mQyay8Xm-HhhkV00AQsQCu4YVtC3kKVnlyOOe_Ekff13JQAmKIonWVlBJjNTqPk3r-ifMrz54" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd1d85494.mp4?token=QP1Yum_xkFzCkmljDYjwm6gkGqYULrZYugCned-eG3-H_TqB1A0t3TmdNtXeA6f0gg-ZUSp6Uj35qW3j2PWWtS-Sv5Oy_O9LbExNOAz5PvzAQmdJ6oTbXFUt-hqqnvTLZIxL2XpV7pxWuhXmiZtfaspeL4NzDqXrWAWXudzFuCbT1kQQ2K6UOz1-V6mpYvfsCaPiFUtOx-XBx44XTf6IByzbUcq6u7WavjCKybzZO_AIUqvVq4lKS4fZfkmC2GT7oUeGpbDcT3vwY_vBonL7JeAr40FxEzdwFyg2B4N_DfxOtVsCAOtUJME5STjvSSzs9qCuwCtgEuIxvaxzFgaecWbZ_9pT9LQpVHAZYwztp5xefsXFpnww01NDKp9VAoyA9PCMkKf304j5vyLp6bOOBsDdukKsLt32bNfrT9qSIqnsAUAdBzs4whKG0oNK-ZW3NhAu4OoxGVn4YznfmrILxSwo-JuZUJnfOiWBbWcJUi2tgL1hnD1fjkOZNRMlPUDmclZhJo5YmIb6lMQGcXrk1EsAbdZnNxTktIqHgm1G2sbXCPb4fo1LUEfEKQxGnWxvWs8hfcghSBfduyM1MdJZXxa96ARRdReDw8mQyay8Xm-HhhkV00AQsQCu4YVtC3kKVnlyOOe_Ekff13JQAmKIonWVlBJjNTqPk3r-ifMrz54" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده نروژ دیروز در مراسم استقبال از هالند و رفقا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/100024" target="_blank">📅 09:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100023">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f18097782.mp4?token=AzrQuuD5g2BBFd2Y9S1aVlGW4tr9TSAEYiN9cw693R1xgGRDR9FVMyvBBMUUs7k-k5fEAb5ynuQtBW7RGCb_GSCa2cpu_PN7YAhzduyIcwVrBkimwrixlb0JGb0zdM2JoHvm9QJ8OsdsYyM5V7oB42lN-2Uw_WAf0mkgV9Ws2DOuf7WAmYB-Jj6e6NipiOnJQ8WgQp9WptxPdJTT8Ok9NLjMsYKjc0PUXVqTGziSWXp-8pOaRqPdvJ3cx34UEpEaFPeS052D9-tA2YndsHycmOMZXNIU5Zk74oONM0LbNnfgZnqbdQ6-LwMN76-p6oF4GP7d_hV8LqatAVUONBymkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f18097782.mp4?token=AzrQuuD5g2BBFd2Y9S1aVlGW4tr9TSAEYiN9cw693R1xgGRDR9FVMyvBBMUUs7k-k5fEAb5ynuQtBW7RGCb_GSCa2cpu_PN7YAhzduyIcwVrBkimwrixlb0JGb0zdM2JoHvm9QJ8OsdsYyM5V7oB42lN-2Uw_WAf0mkgV9Ws2DOuf7WAmYB-Jj6e6NipiOnJQ8WgQp9WptxPdJTT8Ok9NLjMsYKjc0PUXVqTGziSWXp-8pOaRqPdvJ3cx34UEpEaFPeS052D9-tA2YndsHycmOMZXNIU5Zk74oONM0LbNnfgZnqbdQ6-LwMN76-p6oF4GP7d_hV8LqatAVUONBymkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
عذرخواهی دختر علیرضا بیرانوند به زبان انگلیسی از رونالدو بابت پنالتی‌ای که پدرش مهار کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/100023" target="_blank">📅 09:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100022">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇫🇷
🏆
🇪🇸
تیزر فوق‌العاده از تقابل حساس و دیدنی امشب میان فرانسه
🆚
اسپانیا
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/100022" target="_blank">📅 09:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100021">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LqYIJ681CdG8vFGdL2DFyusveO4Ertau74PVqJ6NOqKNwESdp3ntp9LnlApht2nSQ5VtB2EXpb1RhfOxMRz2Koe-Ataov6aIohfuJR40-YS52sMNQ0CyRnZOLfHdYwEWKhfWY7CUd3H-iYZJx3YM2GI5pigQ9JLQDGMWom5aRAwFrCEsndX7SGVUMHsf1Gf608KN9q02-cuebw-Mh74fnihCaIhsvXY9cVEUK8EF_YXmRtXskOsYynwzK5N_QqfsC1FEnZgb8jDBtk4u9pIdBkCAMKiYXcZcjYhpBwop8I80TyYNzBCsSc95NRSyfq6T92BOTl4zlu6546TmNLNL3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
برنامه نیمه‌نهایی جام‌جهانی فوتبال
🇪🇸
اسپانیا
🆚
فرانسه
🇫🇷
🗓
سه‌شنبه ۲۳ تیر ساعت 22:30
🇦🇷
آرژانتین
🆚
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗓
چهارشنبه ۲۴ تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/100021" target="_blank">📅 05:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100020">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/141052eae9.mp4?token=JxYEJknpEFPhQ99v6jgBfX1Uau0MjCjunZ-eUBam-fwMq2MFtVdy-3-HXcIqggZ-r3tVO6y1QnbhtyF7s2kdBm23E4ldZpFqCetL8GDFMMrWW0xw5mToudWhZtbjo9-osCcVt3VgOBPETUzVncOotyjmp6tqRE1S3l6Gm7RUCO4MyXnSp5wa1IYhPodccikDk9H25CsXBOjRETMv14WLYbbur1mYXgx0xxnRFdpnSEg7oKnBOlBWa0ZMhtRXR5AbELxVDAenI0xM0ODjrHp8F3itDElIUwil4ncC9q_WedAmWVD60C1cU6DkzXWhAEEd709kCdnWoqzHWS5w8GiL7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/141052eae9.mp4?token=JxYEJknpEFPhQ99v6jgBfX1Uau0MjCjunZ-eUBam-fwMq2MFtVdy-3-HXcIqggZ-r3tVO6y1QnbhtyF7s2kdBm23E4ldZpFqCetL8GDFMMrWW0xw5mToudWhZtbjo9-osCcVt3VgOBPETUzVncOotyjmp6tqRE1S3l6Gm7RUCO4MyXnSp5wa1IYhPodccikDk9H25CsXBOjRETMv14WLYbbur1mYXgx0xxnRFdpnSEg7oKnBOlBWa0ZMhtRXR5AbELxVDAenI0xM0ODjrHp8F3itDElIUwil4ncC9q_WedAmWVD60C1cU6DkzXWhAEEd709kCdnWoqzHWS5w8GiL7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
استقبال گرم‌مردم نروژ از بازیکنان کشورشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/100020" target="_blank">📅 04:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100019">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ad2f40e7.mp4?token=o_IC6uf13BhprtRTYRw2Q5tccC6a7j8fkw6rGTPs_S_KysABqIw0ukfW04XpKJnoVWr19fmWDSFSV4vXHx3tw0GK01s4ODgJLxcp8GkznNzaB1NIbodPZGpPZ2cw6PIQE74x7PbiKEeWcXy2c8texPJLQbE6MaMzZTo3TGl0zzHdYYIByyY4I-GWKLW-hB6LRSe1XkopK-9-jZ8E_ckT4wAQbz_zAfhmDKp2gymcWu71gGylL1syI9vkGxa1MC790W5kOzjI5SREHaYhr7lStPKWSpF0967B_IGZqIZlK3gmP0T4byg89udrLDE2kMS8LOCTPNRiHwjVQh3lJEVfBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ad2f40e7.mp4?token=o_IC6uf13BhprtRTYRw2Q5tccC6a7j8fkw6rGTPs_S_KysABqIw0ukfW04XpKJnoVWr19fmWDSFSV4vXHx3tw0GK01s4ODgJLxcp8GkznNzaB1NIbodPZGpPZ2cw6PIQE74x7PbiKEeWcXy2c8texPJLQbE6MaMzZTo3TGl0zzHdYYIByyY4I-GWKLW-hB6LRSe1XkopK-9-jZ8E_ckT4wAQbz_zAfhmDKp2gymcWu71gGylL1syI9vkGxa1MC790W5kOzjI5SREHaYhr7lStPKWSpF0967B_IGZqIZlK3gmP0T4byg89udrLDE2kMS8LOCTPNRiHwjVQh3lJEVfBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
تولد لامین‌یامال در‌ اردوی تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/100019" target="_blank">📅 03:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100018">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81cd6224c4.mp4?token=jOMHo6t_wsGT56nC3XipczZiB9d0LmNNpTZIscUrcKdSP4mZcX5YJ_nTefOq5w2qZEHKyd63BbU7Jfa1lUKT_MA-whTGvcKqZ4fbTkgHtVHGF4HUYLSj0r1-2MDH-FRixBUAngehAVkhbh-g0XGXIpJmE1fgyrDmEDIRFdAaArN7q4EuDnrHLwu0LT2iWv7w4n3rdu04TQqFfpcYDRP8mcglHVYA5Tgm0i_bOcdr9YSeFmP8gFG37nS9UGwKrnhELO5uKLNpS_qijqgwJPc6xsj05iFtIa4-U3dzEi2JhF7SAKNifABykzMxvwANnRrrjbo-lnRBVDeBQ41zOPt0jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81cd6224c4.mp4?token=jOMHo6t_wsGT56nC3XipczZiB9d0LmNNpTZIscUrcKdSP4mZcX5YJ_nTefOq5w2qZEHKyd63BbU7Jfa1lUKT_MA-whTGvcKqZ4fbTkgHtVHGF4HUYLSj0r1-2MDH-FRixBUAngehAVkhbh-g0XGXIpJmE1fgyrDmEDIRFdAaArN7q4EuDnrHLwu0LT2iWv7w4n3rdu04TQqFfpcYDRP8mcglHVYA5Tgm0i_bOcdr9YSeFmP8gFG37nS9UGwKrnhELO5uKLNpS_qijqgwJPc6xsj05iFtIa4-U3dzEi2JhF7SAKNifABykzMxvwANnRrrjbo-lnRBVDeBQ41zOPt0jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوب براش خوردی علیرضا جان
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/100018" target="_blank">📅 03:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100017">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuMX7NmyUpy7pAA6zQy76S-ltaS6v2dDz0UIefOIWrSxRD_hP-Fz82ulRwxoZxXWqDu8zljeCTVKpsLRhj7jR0OBdD1BpEHB5CjYFuwntAbYd0Z5qL5__rI49xwee6WwOX3xaU8oFoibGl21NnIlM0YXQV-b6urznLTsLEgd8HBGsy_lIJo3yAZUD30w82W66ixN8z2GlUhwQ1dzIgfrnuAeNKzUZKNHf8dyevkEplawGu2puVJdWFIhukuyQJE86o-Asw0EHeCkQUHaRcQ0zI2dGx4UfA_KcQjW-t6SWO93UCmzfdmm4C2rQr_qMLa6BylbbJzn8cSpC3lZnMoWVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🔥
لامین‌یامال: ما قهرمان اروپا هستیم و طبیعتا تیمی که باید بترسد اسپانیا نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/100017" target="_blank">📅 02:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100016">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2F1ps1ajkmdgoey7fsFevdkfah00iPavC70sn64x578aqmsvkpQmr0pmBTT_EHw6yZeM4QVHvgAcHlJv_OKS-c6T2uI4y3yj8HAkPeKX39Yw2kFWY8Hpz7mnQk2WWoNM18sSMfkEbkuEP_cBmciHm0TRzBiZULUIYSE6BAdMOmkLQLNRaddmzlbR0QgkEnD5mirJrluxrJYrYlVnHtmjt2ARL5P7XOj85sprrLHfOQcFMvLg279J1xX3si6dNr6_7NeEwy8TcuqKGJCCDA7ZcwlrEeRE7VTiMPVcFhBKMPdeLUnrX5iR8oDOR7nXi5yBl9Mv9xYaikJ1BwQCYkU7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🇪🇸
دلافوئنته سرمربی اسپانیا: لامین‌ یامال ۱۹ سالشه و بهش اجازه بدید خودشو نشون بده. مطمئنم فردا روز شگفت‌انگیزی ازش خواهیم دید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/100016" target="_blank">📅 02:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100015">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDCI5yVVQ-MgvBBhloRSH6VTIYh9Q2yGu4XLWxpuxyTh1pdxlLSwavdSbNnbVf8IC4Ji4e197ODDh0UtVAlEs16dcxZSJ4dwy2ijO0J2qtAlU5Tgf99jeUVZN08lntMuNLwaPu20soUGtqnIBfHWGijnraSISz1ICvQVY_JVe39qpsch_epvQ6BT7y2fVV6p6LVm4ePDrr8oTVGK0ZphWI7M_kfWC1pqiNbpMCVr-y-ZbhsyH4NWTuV48uk-vs17yspxw0-QTspyrjU4hBuwJTo3engKDVhjqqkI6fu782r6CcNcMr5lqL_cBk8LI9B1AClGQRC9runNgZ1nXxSxgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
داوران منتخب باقیمانده برای بازی فینال:
علیرضا فغانی، ایوان بارتون، اسماعیل الفتح، اسپن اسکاس، جلال جید، اَدهم مخادمه، سیمون مارسینیاک، مائوریتزیو ماریانی، گلن نایبرگ، ژائو پینهِیرو، ویلتون سامپایو، خسوس والنزوئلا، اسلاوکو وینچیچ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/100015" target="_blank">📅 02:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100014">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a9b623292.mp4?token=T2uHsXE9DtnnzyeCz4ZZgR5l8drZbyH0gPFO44-NZIvlxNK8PHYxD7hpPAXlMKurrP185zIZwJfuyxXuFmWhTiHeAdp3NPu1eizpY5ZNt1lhoqSjKGzFAhoZNI3rJgpl6WFGA1tLsTOZd5KzovyJtWXF9LYSGRT9Xk0mEgH3mrPiHtQfbpKKte6scAMgZTz0RjWdboIDfKY4osWhKCz_TAsru5qwMF_zTRghKKPpknXM6jGs-dEYPk7KG7VOdAhRTt5qlUFGUxCHYZLgt4OfpzTlk8A5FGGPj6IyJvmMBAgWHFqpQReMsPis6UGFKj3C-us_JOFq9Zl-rrFBIxBJeIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a9b623292.mp4?token=T2uHsXE9DtnnzyeCz4ZZgR5l8drZbyH0gPFO44-NZIvlxNK8PHYxD7hpPAXlMKurrP185zIZwJfuyxXuFmWhTiHeAdp3NPu1eizpY5ZNt1lhoqSjKGzFAhoZNI3rJgpl6WFGA1tLsTOZd5KzovyJtWXF9LYSGRT9Xk0mEgH3mrPiHtQfbpKKte6scAMgZTz0RjWdboIDfKY4osWhKCz_TAsru5qwMF_zTRghKKPpknXM6jGs-dEYPk7KG7VOdAhRTt5qlUFGUxCHYZLgt4OfpzTlk8A5FGGPj6IyJvmMBAgWHFqpQReMsPis6UGFKj3C-us_JOFq9Zl-rrFBIxBJeIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇳🇴
استقبال فوق‌العاده از وایکینگ‌ها شگفتی‌ساز جام‌جهانی در بدو ورود به نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/100014" target="_blank">📅 01:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100013">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/dPH63lJ-lTYC5DESLX64WdCtLk-2kSX1VxAxir8h-_5JkNqlBdiPrDXMcKNeFCrdR_3p8lNlpfA48IQ9Ga1csvM-0U-HKI42QSkbMX_ymVE0Bs5eii5qYAtiPTFFPCdAXLL2I7CdLqmJOfmsMBsV5Cz8aqK9MZN6z-JF7yOZrgfETXKXi7SVKbxCSL_s8DT4dCWXWuzVgmAj-wbMaP4PMaoPcbU3ogYCAzp50tHJRfJde_CQ_sgK1fPvRFuDG7J89pwJtgUxpohr8-4Qvt4tUiqJ_DAqJRy8MqFwTTFWBcngd8QlpsUDf7d2WZZKewZUA2NzNVUL1iUiGXhrsWfosQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخدا خستم کی تموم میشه این دنیا
💔
حق ما این نبود واقعا</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/100013" target="_blank">📅 01:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100012">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
🇺🇸
ترامپ: هدف ما از موج جدید حملات ویرانگر به ایران، تضعیف توان عملیاتی آنها د‌ر تنگه هرمز خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/100012" target="_blank">📅 01:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100011">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
🇺🇸
ترامپ: هدف ما از موج جدید حملات ویرانگر به ایران، تضعیف توان عملیاتی آنها د‌ر تنگه هرمز خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/100011" target="_blank">📅 01:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100010">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
🇫🇷
دیدیه‌دشان: کیلیان امباپه صدردصد آماده هست و فرداشب بازی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/100010" target="_blank">📅 01:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100009">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJnQdcoEsUv4Vy8rTgOsS6pMIIc0X-aFRbMXs_r-p9Bo7JsEmxsg4eEV4UY-PMiuokLBi6ZLL1tIGxp534ItIX561XpbA_bFLvi4NaEVnZp7_x4BcQnNzpti_wSOeaNMOBdsjNae0B59oJbTaH7_BofotTlDUuQzadsnX_JNILAh1A4SFu7284iK9pV6BXjrukd3hrtiLzA6LlTTHYBGPNHp36g4IM41jWHZPVklzZiNbKvKtqTSOPeTNkOwZpA1x3gtn3ZDAcwqE4aKltLmDL2CPjGRcM3i8iwiaNkL2FxetRp4hGJFtUW11Gmb_FgXnX3Y6rA_2QvXAEJRjOOd5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
‼️
گزارش جنجالی روزنامه نیویورک تایمز:
موساد در برنامه‌ای چندساله تلاش کرد تا احمدی‌نژاد را بعنوان عامل اطلاعاتی جذب کند. هدف این طرح، انتصاب او در رأس هرم سیاسی کشور پس از سرنگونی جمهوری اسلامی بود. مأموران موساد در سفرهای خارجی با احمدی‌نژاد دیدار کردند و هزینه‌های او را پوشش دادند. دیوید بارنیا رئیس وقت موساد شخصا برای ملاقات با او به بوداپست نیز سفر کرد! در پی حمله اسرائیل به محل اقامت احمدی‌نژاد در ۹ اسفند، یک مأمور موساد او را از صحنه نجات داد و به خانه امن در ایران منتقل کرد. با این حال، این همکاری در نهایت به دلیل نارضایتی احمدی‌نژاد و دلسردی او از برنامه‌های اسرائیل ناکام ماند. وی سرانجام خانه امن را ترک کرد و برای مدتی طولانی ناپدید شد. احمدی‌نژاد پس از غیبت طولانی، هفته گذشته تحت تدابیر شدید امنیتی در مراسم تشییع خامنه‌ای ظاهر شد. به گفته چهار مقام ارشد ایرانی، وی اکنون به دلیل کشف بخش عمده‌ای از ارتباطاتش با اسرائیل توسط نهادهای امنیتی ایران، در بازداشت به سر می‌برد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/100009" target="_blank">📅 01:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100007">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🇫🇷
دیدیه‌دشان درباره لامین‌یامال: اون مهمترین بازیکن اسپانیا هست که بلده در دقایق حساس چجوری تفاوت ایجاد کنه. حتما مراقبش هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/100007" target="_blank">📅 01:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100006">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🇫🇷
دیدیه‌دشان درباره لامین‌یامال: اون مهمترین بازیکن اسپانیا هست که بلده در دقایق حساس چجوری تفاوت ایجاد کنه. حتما مراقبش هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/100006" target="_blank">📅 01:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100005">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSYoveX9PXLlERdQlOt0D9xlbwRD3084hSbPUo6LWWbQTttxYewRjlhNAhf0fk89eO4BZa_Ds3c0uiCgLj4fCm3WU7HwoIS-Zdkl3KcgSm6bjZaLniRxiH5ewqz0xeYdPUJ5whzwi3DpMo_ve-qho5H65bTcxPT80CGfBmzAV1YcxjD8XPwB2Ax-dXTUjnczRjlryHkWUZWaL0lxtI4sCjjJYy2kvppKzWpxHTnJw4nHf-be1GuQpl_N4mogeQlkd4HSButJp0eE6REcBCEmO3yM49YqN0ZMAinyquKM4O-5qIpiJ6nXLB3_bNNn0gAeM8g3bi7fybOdQvKQWVj3-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇫🇷
امری بازیکن فرانسه قبل از تقابل با اسپانیا: راجب صحبت‌های یامال حرفی نمی‌زنم. فوتبال با فضای مجازی فرق داره و فرداشب بهشون نشون میدیم که کت تن کیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/100005" target="_blank">📅 01:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100004">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrEvMs46yNPsxMR20wuz-TsuFI6daJ804Momnsfj2_qJNIpjfIwv3G7aOA8GAk4lFjzrLPv1sQFm-7z-g2GVKSeQtosAqNYskomF1av3O1_9ZLB3FESmWqxQ_xs47Aqdwl9JYaeAeBpg_fouR6eSv6yFHuoR2oDKWBB2s_Kytr-Npwa09ZSvTl40GNIMHMx4sMxiu0MpRtU5MG5VfNUaIt6SMtJa5qCGWCd9hCq4Z6Q4_W2fCyXuFI_NRBloo8pPlO1GRxU58bzNoazjVZWkEi1HQSnz9ZeCkzxnyTb8GvzXeWG7PPRG3ETlWTtXR8K_1Pd0WkZ-duSUmoQbPuEtSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنالیز و پیش‌بینی نتیجه تمام بازی‌های فوتبال جام جهانی 2026
💻
📈
وین ریت 80٪
📈
🇫🇷
⚔️
🇲🇦
وین شد
✅
🇪🇸
⚔️
🇧🇪
وین شد
✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚔️
🇳🇴
وین شد
✅
🇦🇷
⚔️
🇨🇭
وین شد
✅
حالا هم دو تیم فینالیست مشخص و در کانال تلگراممون اطلاع رسانی شده
⏳
🇪🇸
⚔️
🇫🇷
‌
󐁢󐁥󐁮󐁧󐁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚔️
🇦🇷
لینک رایگان ورود به کانال
👈
t.me/bet__gg</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/100004" target="_blank">📅 01:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100003">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بخدا خستم کی تموم میشه این دنیا
💔
حق ما این نبود واقعا</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/100003" target="_blank">📅 01:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100002">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
⭕️
شلیک‌موشک‌های سپاه و ارتش به سمت ناوهای آمریکایی در تنگه‌هرمز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/100002" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100001">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
⭕️
فارس: پرواز جنگنده‌ها بر فراز تهران برای تامین امنیت صورت گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/100001" target="_blank">📅 01:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100000">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpZYb1aFtRayMbWNxXYaOukvzW7ZDGKtvCAECNmpYDegenUrIABG657M4SXzbe-0-a_DVc4v3l8R81rzGS_svO7EpQFV2H_Qh5W3WuHbkakTYeXNaDh8upDhpFYlAyj8uNXdLJYzeh_Pvinbf7uzo162WjHExXOTsw7fEsGW9sIjte_NZmQZ_FVrb7ME9ctxO3gTu1oJfsEAz9eolXj_ifVTnH-5A6JF3bZkHNtNw17fNsOLxrSmMZnZatpSjjr7APtNrq1WGLBRS3ncwc7idM3E-S-tbESilh9D3PTGGSQziRGoDiJcblpvP1cOP2D6ROjurkQc1wh-2rReHM4LVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
رومانو: مایکل‌اولیسه گزینه این فصل رئال‌مادرید نیست و اگه موفق به جذبش نشن، در فصول آینده برای جذبش اقدام میکنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/100000" target="_blank">📅 01:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99999">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jafk_XAE84x2GorQzodjPzkm7hBEF1hk_wFYjdhCQ9Y22rjXFiT2bftZ5_n7iESauLbeSOBlywpyTA17VD8tbkSfpYxPY1ckxBUtj-tEOISb7O3gtVcJYIUEsKODMP7hufbkgg2EZOJB9t5QLUZNKddAal9BcZXO7guNGPZ5SfEdTvboiNOwCuhKhNk4H5-Hl2XLPjfVghTvnJBJUlEjFz0KY3GwxrCpqawmgDGeahA6EgCMl8WQD4ncUIT1c3zxXyJSKiQDFocaYNYUtCg_QTXnT6Yw5r4VLEsMm7c0mIigblPHtuauaG1h3tI7by-FA5z9O1pV3ictMy2hO1eJmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دی‌ماریزیو: باشگاه آاس‌رم با ارائه پیشنهادی بدنبال قرض‌گرفتن گارناچو از چلسی هست. چلسی البته خواهان فروش قطعی این بازیکن شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/99999" target="_blank">📅 00:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99998">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a423066bec.mp4?token=eSaRHZa3o1XzXlAKr76xppn4opBBH7Od26EO2sXEOPNWQgIC7pII5SuaEqjwrCQtvASkAAldBWJAD_muwn8lD7KqAu7G-Mu_qqKIzvKDO8NylqVHvam0jUnS6PX6IwJpQ4h0AyAb1CgwWYSLXrl2JdoZtN3-8cmYMTJxUy9yeuP9uLvzKBy_akZ8b8Vzi1rs89B5wmw_ZCGVmhkMoSUzDsqQhPDqtcHdzurMA-r7OPzJBEvbn7TpT8veOjFlXPuWQ9Wa4y8aczKt-_3zijIbutkR6CDsbDQuxijfox66IukPoVlXgehLKqyRjqqeFKhHXRNRoMjw78p3csW_0ETlLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a423066bec.mp4?token=eSaRHZa3o1XzXlAKr76xppn4opBBH7Od26EO2sXEOPNWQgIC7pII5SuaEqjwrCQtvASkAAldBWJAD_muwn8lD7KqAu7G-Mu_qqKIzvKDO8NylqVHvam0jUnS6PX6IwJpQ4h0AyAb1CgwWYSLXrl2JdoZtN3-8cmYMTJxUy9yeuP9uLvzKBy_akZ8b8Vzi1rs89B5wmw_ZCGVmhkMoSUzDsqQhPDqtcHdzurMA-r7OPzJBEvbn7TpT8veOjFlXPuWQ9Wa4y8aczKt-_3zijIbutkR6CDsbDQuxijfox66IukPoVlXgehLKqyRjqqeFKhHXRNRoMjw78p3csW_0ETlLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو منتشر شده از حمله به سیریک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/99998" target="_blank">📅 00:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99996">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
شنیده شدن صدای انفجارهای متعدد در کیش، بوشهر و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/99996" target="_blank">📅 00:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99995">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kbzw183xRZWB0wvrzAKHPlLOWahZJ_vE0RNruB0hYX6Y99q6bE0VgKwU1F86tv11gNARpgitdEHH5BfGC7F6c8dKmVSSaBXVQR5WQv1oipnzlFm-UQHpRIt1091I3ttsn9UM-bOiAHWQi68FBuZnm2xKSRu2OmyrttQBIQhgZkaRlQ_YatcEIliGXiPMABq2o8c5FepahzzPxE4a4lr67Eeo-nE-TOBTx8usBaCMFxrWKgYMiWd_QU1kfmZ6_TgYPHAc-_3NHZDn5mkjURQisXbxZhF4n_8rWIurKUM4z5fCaQQmV0gnl1oOlE-k7PqPwmCEXUvFL1zYvFVoBMyfgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇹🇷
رومانو: میسون گرینوود ستاره مارسی به فنرباغچه ترکیه Here We Go
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/99995" target="_blank">📅 00:41 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
