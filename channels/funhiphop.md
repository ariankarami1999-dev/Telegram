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
<img src="https://cdn4.telesco.pe/file/FwMbNfb0YRK5Kkw3STtzOUI1UI0qPGYSPc0YFo35a4GV0d15W1TRHU3huPKx5RS6TOW8j79_nvfmcIOr1kOHY2FOfgZEGm3esyOn3OgH784j3D5C8g_VgtrELnOwkzQPjqIoJAEBsWFUzIlfjiJGR-zka4bYktWgq_CPDiOQG9ZBWXOhFMeWnaaq64zbvwSTjLEz965Vfh87TUjQnrDMpnGhfGp3abHnfKzQQVyU3s4GJQBZEUHrUC_cJaE1xlzF-ubH9Qgaebgo4b15clP5D06b49dEn2wujftBBhscnljvA_b1OEv4RDYM_20icnU38osiYlB1aXPAWeUXDTlsKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 19:04:48</div>
<hr>

<div class="tg-post" id="msg-81589">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4m9FWZOIY1hqPXQ0wZgVUz_sJuWH2uhSRunaTjf27LskbH_eGOlAp4A3xMK1tYp1S-JwgqbZrGAPE7lbOHlzWcnBKsghlQ77thTmo5QJB6oIlyEkZfs29mT-fh1v1VS5J2M7ad1YbwY5wIXsioA43EdMki41BZKlGEb2aO0v0gbXPV78HI3_mzXpPBBnywoKihylX88fLd86Qp-JQI2G_alqQaHDVfMn_jVifeJ2Ssh3MLI9X-VgVCB4j3KeKDwjcBTyRwqB-d2vcLr3QmB7EXKjdD5XiTtnWZccN3Veq5Qd2ZFs8KXqFBKw0JHphC70pELJzMaU7DNZPopeU3PEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیپهاپولوژیست هم لایک کرده بود
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/funhiphop/81589" target="_blank">📅 18:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81588">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDr-fP0bUB9YyTohQsBsuAZizvJNzT9-UU3cd_4oTOkH-mp4a_vPIXDoLBZswaqfuDGRO_q5_S48ulbkDFb6xwEiiWHKb8Ffvf5KZmbziwxvrObrXZWamdlw-DxzZM8Vzu_lcdIHpQW-ZOhTIjosjAdFIMC5RbPvIFNPxUqXuAqk2XX8mirk6jzbDxgYpLHz3WuCHmiYdUqhxK6UmRCR_9FPcw9UCOnWu8AffzcMMdr5wk5D0Oc8i2jizgMAR6j4WP8v-D7dfGbRPIFDr12xaJ_egCgquql2c2FL6J-K4MYDhf5ftHGa3BDdiSRW5gsaG5S7ya0F1wIjn7DCGuEYmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/funhiphop/81588" target="_blank">📅 18:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81587">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsUktVtJ7zSHIWH5uUu0TFRbzRGLTb5-lC2XVLWOiaMV920_csuyrwSLPmZQ_1T5u83t1MwKp8uz7Gm-9PkjrDJPPDlA8Sj8dc5itQG4-PUG7CezuqpxagcA_OVmPXDSAe0Ikg3pi_Dk5TpE7ofHmwOMzzPnXXNp_whJv1w0rYAftiSDDQMue5ig6VlfMsX5nuEQYL6Qxtu5Y0RIGGbMHg0BMTTW0GAoIjFqtj318iIDmoDeFoV1Zkv5qTSyY_D7fomrqHZigy6eK2DO9zs7U3T-2MxxVijDarJXGZnrQ2VNgYsJf12eM57lTMs5JJA1L3jT_Qyk97wVHxanfjgRpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بیرمنگام سیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
-
🇪🇸
بارسلونا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
جمعه ساعت ۲۲:۱۵
🏟
ورزشگاه سنت اندروز
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بیرمنگام در ۹ بازی اخیر خود شکست نخورده است.
✅
بارسلونا در ۱۵ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر بارسلونا ۳ گل در هر بازی بوده است.
🧠
مسیر حرفه‌ای از نظم شروع می‌شود، نه از شانس.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r9
💻
@BetForward</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/funhiphop/81587" target="_blank">📅 18:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81586">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗥𝗮𝗽𝗶𝗪𝗮𝗿</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f78835d85.mp4?token=RYXHQeZs2ywxE-ixSoaRTxWS8EyqRZIJ5atQ5khzPaMhjYWiW38DQo1D8mwMALz3rLXqDn6M8wK7StU1lFYYuF0mySNTIKAbCVMzX0_Yu9Q66t6xi4d_SINZZRnv3fOn8CJcMFiR8i6N2ElvSj3i1SXz6riS71pbh-A5z8XCJXfH1wQymX-Qx1LfqUQ_SRe-9jiUCKgIZ0y0IC22-GcCdv9AjssIV9Kqmm7cSsdbF-itjkJTcZt4g6Dv0M3Y7pbIjc63LYRvyVNM7udDQfRPr2GUBqICxkOhdDkBFxYDDgN4g-L4ECJYtHvrj8CMDhg2k04Vzk6HT6VzZFDyu0NdOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f78835d85.mp4?token=RYXHQeZs2ywxE-ixSoaRTxWS8EyqRZIJ5atQ5khzPaMhjYWiW38DQo1D8mwMALz3rLXqDn6M8wK7StU1lFYYuF0mySNTIKAbCVMzX0_Yu9Q66t6xi4d_SINZZRnv3fOn8CJcMFiR8i6N2ElvSj3i1SXz6riS71pbh-A5z8XCJXfH1wQymX-Qx1LfqUQ_SRe-9jiUCKgIZ0y0IC22-GcCdv9AjssIV9Kqmm7cSsdbF-itjkJTcZt4g6Dv0M3Y7pbIjc63LYRvyVNM7udDQfRPr2GUBqICxkOhdDkBFxYDDgN4g-L4ECJYtHvrj8CMDhg2k04Vzk6HT6VzZFDyu0NdOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجام جلوی خود خلسه دست میزنه به اندام خصوصی جی جی
@RapiWar</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/funhiphop/81586" target="_blank">📅 17:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81585">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a90b7fcb9.mp4?token=WUrz-VsnWqPvl0hhMLAa6KrarzdjA2SdZDCvEsMa8A0lDEiuUjaFkhsHeqZE2OCxhNam3ajQpl3aYEWYNCR8VeG_ZHikYCMK-V3stcL9yLy4082_EOq_-eanDCctxrdI3YW_jvU7W2iio6k_iJXIO1wqnQG5qbETzkbj84qo7Ym2j__ZofPoOmdRwCqvqDR3MJ7mr3OXVLCH6yBmKgPiZkjnrw7haU3HoDqwOapRqWND2L_GOJgbvl7uKZ4_-3J8LsinfSEjMARDInXr7_WIs5DPoBfG8G3XicdgXeLhIqx9PXesu1JUp9Ihp3Nbh08r1fHm7Ft01kooLc9oKzpdGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a90b7fcb9.mp4?token=WUrz-VsnWqPvl0hhMLAa6KrarzdjA2SdZDCvEsMa8A0lDEiuUjaFkhsHeqZE2OCxhNam3ajQpl3aYEWYNCR8VeG_ZHikYCMK-V3stcL9yLy4082_EOq_-eanDCctxrdI3YW_jvU7W2iio6k_iJXIO1wqnQG5qbETzkbj84qo7Ym2j__ZofPoOmdRwCqvqDR3MJ7mr3OXVLCH6yBmKgPiZkjnrw7haU3HoDqwOapRqWND2L_GOJgbvl7uKZ4_-3J8LsinfSEjMARDInXr7_WIs5DPoBfG8G3XicdgXeLhIqx9PXesu1JUp9Ihp3Nbh08r1fHm7Ft01kooLc9oKzpdGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دسته جمعی مسلمانان به خانه های مردم در اسپانیا
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/funhiphop/81585" target="_blank">📅 16:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81584">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8_Wan5D_ReetptSN6YKibw22z0RXSnL4WnQulzksTTMd90jUzHvjvKnz9aUW32tjBfBHJEh9jLdbx6eEFttUfG_kiMM6_0YE97aB5iDLTExYPCgZgoPy_K3ZnygrFY7xycHOdTuXxwzpRWmmOB7OFecgK6Exsdcyn05YLLvGF-VuLHhcQGr2R4deGFsXw_QbR5YiaEPpX3PLYestOelfzEBtVyagOP9WdbjQUotX6Ng5KRJOkerGdATNnU9KGXJeY3KJozJvezZ7SoLA2F6LW44BajoYvi9OFvJwjv0QCErwCP5f1T2t6k0RuJxFx00CG5qBe9bBK7v5FSVafoREw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینترنت استارلینک از دیروز در کشور عراق فعال شده.
۹ میلیون برای سرعت ۱۰۰ مگابیتی و دانلود نامحدود.
۱۵ میلیون برای سرعت ۴۰۰ مگابیتی و دانلود نامحدود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/81584" target="_blank">📅 16:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81582">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GFUWObYEUHFWvNL0BQz3IzvBAWupgaHdKBCRXZP_gqwdol61FgUJCWAEnpwNozsJ1ngzhvObCFg2dl6n_7OH_ZV_vLAXA2JjyNM57NPy_uGRIzub7juvAu99SGVw3tR9oUcATjHdAjUDB6mnZqVZvwdc6YP5H9hPEmUjHDA6olWmdzECjpyTPTcqk4KzuNuOpfe4vpZGPyVKvNS46RhM2moG1iZ1wqKfEO4nw1um1k17S3h4rkEy4jGPFvDXyPel6aCMKj2vWuUrJ8BOH9SrjkhfPmrkn3Z0IPJpvUkip2s1I5bRC7F2j3yRVz8cy5NJ1AZ8xT7FRL5QQ1VxrVnCXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tvsmp8kDBD0I93RurBaukJP-ujodWR3LLl4IIXZJpuffZJU3bi8qU59RUsVjB6mwhf0dHm7Za5Ai4KyZ4H0sX-WIy6S2yN3ppV2gKMVdTcaJzYFYBb0QfpymG5t0NcVX-JpnEH_sM47yu6yW5B5DS1SEekSi6IvmY618RMEqQuEbhV03DfFLbPR4RqOiP0kccxaG4Y5iysqNHmTHjg4Pytyl3etBzSzG0jmeh08urUnBeBLGTWgJ9joPYwFDJh1ymocRXq0BRi5VSzC6YU3ewJhKS4ZXWwEVqzrYe6DXT330a007Lrz7I1rDgFBVo6LlKVU7a-z3GTKpGM1SDWEVrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اصلا حواستون هست داریم چه بلایی سر اسطوره‌های ایرانمون میاریم یا نه؟؟؟
🥲
💔
#free_toomj
#تتلو
# اکسپلور
#پرامپت
پروکسی
پروکسی
پروکسی
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/81582" target="_blank">📅 15:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81580">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ao4B4vB_SDqNGVshHEsqmJXdvapmKf_XPY65D1k8O_Msc1fqmPPsqNdSOuUVHtXqIY5jEH7AP24awiJJORZLj5jiHzjR7iCs3hpBhnCdojm2VI3j4redWGpzIQdMS1bsTY05uWM6e6npSeN9mYJg3NizyRo9VX0Yf_5Xgt-bsvtKiXnKSs1P7aqPhmK7DPHPuarhoNo_jIs94AJWPizDujjeWOtA9o7_1IcCHgUA4govbLjEiimpoytgYtAYN_FIzlXSBmtBrqCdAbvQm_s1g__dfEYJoDxG9oHVsvM0AwsJ2kwRV1anh2FtZeOcIKQnG7giAB1tE16oDxs7lidIIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RHlTF1B3fdTf9tvFINdU4armj9prefj1YF03aent8tHB_oZcV9ZeZWu-y9cRXmYhYVOPduZaIB2H0vDKq6Nna2rXlyBrOOK78PblsBP3Hee7ATGdTEifXlqn5K4L5AQtK_idR_h1HW0E59Df46bgE0wPsOIOLELSjUzS_6cmFD1dXpDfFK-_d217To-9Jgvs4aEMpE7ikIIAaF0P5FVxBeWbBCVsdgsOp9jhka1ATrgdDS6OoddXQGGBn57NnjrpTLFTVAmfIqcQa6oR5qYSuKm4vOYC68zI7dMPOLyvcFvsHoI1eP09yBsPZdRtYsrxK0qW40TRL_vc7hyOtW0f8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عاقبت استروئید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/81580" target="_blank">📅 15:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81579">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMtu6cFMLGPOVOOizdvJBofZDikZUU2XViDaWbg5fOGYUtVK760BEs3m15Gf25esuVfpWOD855DL0BZ-RUxXwtO-gt-eY3RdNq1m8ZmkEB7FODGdUfqo3ndLcKb1o2YvJfPsaY76yUkOedbksVmHXn4jmC7qMfTAh2dTblrHBFHG6gBakwe2MvuomfGBSDracO8eBVPpETG2E80gg3Ig9GBhKhvEY_yTiNLE_41q2AyjtEfarNDVARf_xUaB5S5V2-1WrqNZNX5pr7rcXURFaGwqUzdXF9KoXr-DQYgtkXEbFmhu7zyBw_-aKTRoRTG1phsWc9stqPfQBk0aLcimhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم میگم تایماز چرا انلاین نمیشه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/81579" target="_blank">📅 14:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81578">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ امروز با کابینه امنیتی خود در مورد ایران جلسه می‌گذارد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/81578" target="_blank">📅 14:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81576">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دوتا کشتی تو تنگه هرمز زدیم، امشب آتیش بازی داریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81576" target="_blank">📅 14:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81575">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آقا تبریک</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/81575" target="_blank">📅 14:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81573">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMJvIefQcaSLs3zV_drbpssAdjJpzXtm1fDmqtEf6kyQgmKtON6XK7MKu3h--h4nTxQ1pP1hxi4CRQ4848HFdwVmdRHY1yvCAaTq02NyLRsgPfMt-Vp7o_YL6h9g97oMhJc3enQyWgl-4V_SUpHlF2xUxeguVwS4jMbtRHrEp6fdmz7No1Nq5EMN5Vqy1zqJnhohD0-q7we1jBx_uBLDX7dlk5B7EcBbptRjAjofQh0HTEs_-I_Zfpfknnq0VBRt5-NaI4Z9IgVT0OOBXLbzoimZKujNwafSPRkuUgVHVYvmV5SXurJVO8ciQT2o2rGSKAo3IgZlY9VZ0Pf60M8eOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم میگم تایماز چرا انلاین نمیشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81573" target="_blank">📅 13:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81572">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY7FNfH6fw7y3Oem-H9V6El7FfNwMN_NoTMW6i_FDRl70WS-_KyKQqKOKIqEgdip7M9POTy41kTBUIkT1YGrMfjPbKn11gyn8KcGlGX2nuHyBKlAmxDJeQ7jjakcSXif9IKFab5OXvLnauiElBYUcowsQWGTVime6v3UdzNPR-gQe27bA4ybcz-GYzuPr7IuCEVqexiKvtbB2tvBT0vXqI5m4K07G7o6sB2cyiTxoe3v7Aq0_46CLfFUvzhnTmKotqFDguvnbzfZlxlOv7HOk4WUxcTJXYylnz7Mt3WNxcwexpXItl1ZtRw511IbbSrpx43s2yJBk_YEF_iz5MXCgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر وینی چقدر شبیهشه
(پسر دوست دخترشه، پسر خودش نیست)
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81572" target="_blank">📅 13:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81571">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEIy4qIUlJstEQ-m2UbW7CKohM4OSH9SJBIU4J751Rv8OClvDxX-xR4NBBLQxu3kSz2DyVQ-2g_jrGM58L88Y6GEXryM_TRB1-3QzrAhkmqF5zXT7SYyxBMzDKUmF7eMmcww7zhP2z9NVzuTnlM7fkfnhtLueuOQeh9hU-LnRbP0NNLvqldokDYUNgeqs2lbOQcT13rUnhNjxrkXqZDohFVwAjVuv-AISQR7z7pWicQ9fernMDAKb2wZqcYWtDPGnNPpHGnRrn529yi14Ar4TiofZgz1OCTANwN4D7xTLPpL_u8qUhOTv4Fx_sDA1xQOChSQzMQNajQ-sBz8knF8Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آب دستتونه بزارید زمین برید این سریالو ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81571" target="_blank">📅 13:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81570">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBd9Jg4WzQrt47_qFxTrwBunhGfgG1USCNZE6bwhMWxxd8puk_KCBAh-b6VdZ7kL3OOta5welb9JJoLUUfM5wEqHFJpyFwo4-7n1ox0n11l6N9UDRBE8NLFvFpA4mr9leWYbDtO9MBxfbJFnoMwJlzBf8w3cUYTQp7fyuJB30ewrpVUVfNijzoQli0NbtGletcwqKfXwcJBzYu2Qptxfgerv7sdz6-g2k8vNuDLues5FkUwLBGfF8OEH4VHeA1voYo_7UGaHVNOm_mY9rQJt-PSaKOZK3rY9d-mUC1FAHd7qCYz5M1ZLLkM33N7UPERIUQOFqIL95qTrmXR90CKwBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیبایی ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81570" target="_blank">📅 12:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81569">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMRSjBm8C4O34uq8DYzBKndV3LU9Zp_zuYTCNUHj8FrtW7EAma4jB4VjFjkXlmGRFgBuHZ4vR4Qrr3PHOhdCyFKcgFKJn0H25arj2Ax3ypj3gCldw5oYi6c5AZZukQDShIkKw3M0QpGoxhNxrod3l7KJSmFPuky8lZ332UbWoE2qJIig2lh1T_gKysN18qXcvG7Y_DNK6nQFctomCAXKKVqU9AdQKa-P6_Mp0i14lfjHBtGI2DxlvDHxxhXl8WvOgp7YRz-gmGmxmn0Otrbsb_Bv8hJLM0aAT8W5FDYmrpuvgN3-G5iTY4euF4T0po3mP-HiB4igzwTTCh6WgXtbRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بیرمنگام سیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
-
🇪🇸
بارسلونا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
جمعه ساعت ۲۲:۱۵
🏟
ورزشگاه سنت اندروز
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بیرمنگام در ۹ بازی اخیر خود شکست نخورده است.
✅
بارسلونا در ۱۵ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر بارسلونا ۳ گل در هر بازی بوده است.
🧠
مسیر حرفه‌ای از نظم شروع می‌شود، نه از شانس.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r9
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/81569" target="_blank">📅 12:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81568">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bs2sN9GkFekfSMmkBuYa0sOKgEEIvGWwtxRrlsx2rHK-e-6vHDyfJDFvtOB7ndLoAKRlE2Wsh3yqxRrzNQ-dimWkoAzye__JvYjLhyZKBFqOFCkzowsNl-0bod-_ClVjWDtCIoXNKq4VDwhc1ltI4EEWYyDP_-9aQTMfT1D50JJ6Z4XBYCF3CGdVjPYjpE7WNvTq5TwKSnKg5gVQ6w2PLv5Fgu_EU9WbfDMhY84-PmfcCaDC0IrZhtUdN-p95SolEIQJrYwroQGDTYnSYzfmy6S1nziIzhz4cjTZ0Dr4onNsTGcr1qoYyhOU53IxVrhMZmati-vyORwOdp7vNzcMow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81568" target="_blank">📅 11:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81567">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یتیم گیر اوردن کصکشا  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81567" target="_blank">📅 11:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81566">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf580585ef.mp4?token=o9gOj2eLRvhsR7qmxJ3xfZQcYchlEDXVu6XAm-tToRp0fPCJP46qfgBXdtpOnfQAdCpmM4ux8qF_jCzzT2wi8LDu64u9ssfrTzl7Aq_uqmpkFlRK-BBp_B7U76sMAHduJbo4gpPsx4SN4ueb869vFEqdjcB4x2WSsYkuYpYyznAK1uBIBcqL3TZerZp6kAMp532MD-ua6fGBLF3M7CjQ_9maVz7hX1OKHHGpkvapAMMPASkfo7SOyy_ign3i9Dud9UOdIeJBnDHqJsOtbB7wcZbDw6kl--nW7hR02XAwQVacIQndL7UzPT0aIuvlDFbbvnCt5yJSHp2nkYohbW9mJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf580585ef.mp4?token=o9gOj2eLRvhsR7qmxJ3xfZQcYchlEDXVu6XAm-tToRp0fPCJP46qfgBXdtpOnfQAdCpmM4ux8qF_jCzzT2wi8LDu64u9ssfrTzl7Aq_uqmpkFlRK-BBp_B7U76sMAHduJbo4gpPsx4SN4ueb869vFEqdjcB4x2WSsYkuYpYyznAK1uBIBcqL3TZerZp6kAMp532MD-ua6fGBLF3M7CjQ_9maVz7hX1OKHHGpkvapAMMPASkfo7SOyy_ign3i9Dud9UOdIeJBnDHqJsOtbB7wcZbDw6kl--nW7hR02XAwQVacIQndL7UzPT0aIuvlDFbbvnCt5yJSHp2nkYohbW9mJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار مسلمانان مراکشی بعد از نفوذ غیرقانونی و حمله به اسپانیا: الله و اکبر، ما اروپا را اشغال خواهیم کرد، زنان و کودکانتان مال ما خواهد شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81566" target="_blank">📅 10:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81565">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4FYUBirA2gUbb1su0pI5-FVSnN-klhg4yxr6Nwxm5dm1tbw_O7McDCgqn3_iMyHNxhhqBNOX17LY2XoCEYfWg6sqRfcxqaLmH9HD7T_IF2O7sTKvqNl8wqjPy-fR2ipeONhFLuEaVZ7HEDvHJ0_7Q6-WguozNGYF8B_4GEVqBzEiteufnAEgmwWWMMUiXDX1L2UUfsVkG2cSO-yrcgzA_iBwvNPNWKZ0gOBxSCWCTysnmzSojarFE8TlBWQ6PuvDeRjCYIXrn_BzG5tgke2fbcEzP6ePZpFloPvO3bppH8kwiKqt3w9IySMgJWRvZDAVQs1-fo27FpQq90tdymZRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از این تحلیل کارشناسی شده‌ی رائفی‌پور، خبر اومده که عربستان داره برای حمله زمینی به یمن آماده میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81565" target="_blank">📅 09:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81564">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76336c1936.mp4?token=VZi6JRPx94_fM-XBIQ8EYWCDrQxfYRzqLC9Khvem4gcP-rr_Emx-linhHHVDaDu8VsGn1Q4Mvn8prqp58nWB5-kO_FlKxH5aGzsAMWKJxMSgj4F3sExHUF3XvxShT4gpcPIrhiKMNCs2AzdcP_m5oYfTpli2aTD6SPdfz1T7GXuA5Ycs0MY1rU6bAfaY_4RF0a3n7rz0VIInJTSQqpawH26uqm7CPMMI2iKMgnrdp0NTcVUwO5y642oqA7A6IoXT3THrVjM6ZIPnqPGarWwBagvVez0pBhH1GetLBdFVsOUrwSjy2RTgpTHiTeMw3N6_bxRBgii8lcLfAzkuYDazqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76336c1936.mp4?token=VZi6JRPx94_fM-XBIQ8EYWCDrQxfYRzqLC9Khvem4gcP-rr_Emx-linhHHVDaDu8VsGn1Q4Mvn8prqp58nWB5-kO_FlKxH5aGzsAMWKJxMSgj4F3sExHUF3XvxShT4gpcPIrhiKMNCs2AzdcP_m5oYfTpli2aTD6SPdfz1T7GXuA5Ycs0MY1rU6bAfaY_4RF0a3n7rz0VIInJTSQqpawH26uqm7CPMMI2iKMgnrdp0NTcVUwO5y642oqA7A6IoXT3THrVjM6ZIPnqPGarWwBagvVez0pBhH1GetLBdFVsOUrwSjy2RTgpTHiTeMw3N6_bxRBgii8lcLfAzkuYDazqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون سر شوخیو باز می‌کنن بعد تا ما چیزی می‌گیم میان می‌برنمون.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81564" target="_blank">📅 06:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81563">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اسپانیا داره شبیه سوریه میشه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81563" target="_blank">📅 03:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81562">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اسپانیا داره شبیه سوریه میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81562" target="_blank">📅 03:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81561">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حماس خلع سلاح می شود   ترامپ: شورای صلح امروز به توافقی تاریخی برای خلع سلاح کامل حماس و سایر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81561" target="_blank">📅 02:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81560">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حماس خلع سلاح می شود
ترامپ: شورای صلح امروز به توافقی تاریخی برای خلع سلاح کامل حماس و سایر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81560" target="_blank">📅 01:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81559">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81559" target="_blank">📅 01:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81558">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fc3e48dc.mp4?token=UY4P5R75CGr94Lkg9DP5fcQmKuqIx8QIYKPtvZzi13QRItN54vX7NU6uG4dz8RvDVamktGL5p1KpoFAWG0-dWU8L4W4nKDdjRGUZHhzDBXacy2d8Vq_CvZVzV9pAShns6EwM9Arjhq1q7u_v-JqZUbK26EDWDP5teS51qyUNGgR_w6PyP0iBpraBqijGmvpnwl_ezPXW-q0Yy4Ka5Iemkw7aSkU9uLRVoyL-Z10r1kirPWKwtigco0v3pSfVsByOar37EtqrJJSAbS89zJtnmBBdI024yekxy6LOLH5chCxtB-nbprq0P_mtIMYVupnjg8WeMGCAmCkTiDmztuGDHzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fc3e48dc.mp4?token=UY4P5R75CGr94Lkg9DP5fcQmKuqIx8QIYKPtvZzi13QRItN54vX7NU6uG4dz8RvDVamktGL5p1KpoFAWG0-dWU8L4W4nKDdjRGUZHhzDBXacy2d8Vq_CvZVzV9pAShns6EwM9Arjhq1q7u_v-JqZUbK26EDWDP5teS51qyUNGgR_w6PyP0iBpraBqijGmvpnwl_ezPXW-q0Yy4Ka5Iemkw7aSkU9uLRVoyL-Z10r1kirPWKwtigco0v3pSfVsByOar37EtqrJJSAbS89zJtnmBBdI024yekxy6LOLH5chCxtB-nbprq0P_mtIMYVupnjg8WeMGCAmCkTiDmztuGDHzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های جالب پژمان جمشیدی درمورد شایعه‌ی جنجالی
بوسیدن دست وزیر ارشاد توسط ایشان:
آقا حالا ما نشسته بودیم یهو رندوم خیلی اتفاقی وزیر ارشاد اومد کنار ما نشست منم یکم چیز شده بودم با هم گرم گرفتیم و داشتیم می‌خندیدیم درحالی که دستم تو دست ایشون بود یه ذره خسته هم بودم یهو سرم خم شد ایشونم تیک عصبی داشتن دستشون یه ذره تکون خورد یهو دیدم رسانه‌ها دارن تیتر می‌زنن من دست این بزرگوار رو بوسیدم.
😐
این تیترای زرد و سخیف و مشمئز کننده چیه می‌زنید.
😐
چجوری می‌تونید نبینید من همیشه در کنار مردم بودم و برا همینه یک هفته‌ست باید با فیلترشکن وارد سایتم بشید دیگه مشکلتون چیه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81558" target="_blank">📅 01:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81557">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">این پست مربوط به رپ فارسی است  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81557" target="_blank">📅 00:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81556">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvzTEjMyIF1faT11KKqom6sEo6Sev6kCePwI8tnQ6DKQKg0WT4uU2GeL84n8KB9vO_n3dF5gvIl8X8WuR_8i7J6_9iTSOR7Tdna-YWAjH0esGDTgJk9a1xitCbihno5mxg50h21hA30wzwgfG0GV5D7FcF4DB4Oge1ZDT4zynvkNm6q4Z2My-CaOvScFYKCHBMpVD8NCsOBWxcIzILIrdsItwGSj6d-3-qPk8G7ZoJKdkRCvodzsO8uwD-6fecfCwB1IHwHFvlMnp7WqULjhJU48Tg662GeoMCFt0KfZivlif4BsXZlLR5junVfQKieLEXIjwIFudiRsHI-4N5hZkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پست مربوط به رپ فارسی است
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81556" target="_blank">📅 00:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81555">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دادستانی تهران علیه افراد حامی محکومین اعدام دی‌ ۱۴۰۴ اعلام جرم کرد.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81555" target="_blank">📅 23:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81554">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBDlxC1IVigWH0JJ2C7xYZpKacx4GT7yn6OGEsZmn0ISmtH9xy9JysYwudFkXCWb1_ytA36U7MJXIXh03T05uOGpWBbUkwE0yh25Y-AYQY-MPaKwTZgovAnShlkin7-tq8Nc-AtvbU9NIjT3dhyGPXJ2pKDAY6Tw12U5NyzhZM2AS4jout9HuXkFMLuFolciMnNtwrPXCa2UinP7Hd3sqav5d81uTboFRYAZcxMg_Eaas7N-iohb1HYFUeX2xCNPkymRMyWIRUeX9fMncEvVpvfCuyWb40ykku9305Zy-bRNLEfATiCZOcidafewS6-jEpGONu6qDbJTdNICmYB1Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه ها ده سال تحمل کنید تمومه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81554" target="_blank">📅 23:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81553">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37370edf56.mp4?token=LL_SvJEXFtOoc8sllVPCTwOS8fxWtbCM2Pfjl-scOXGfcHlDxIvwOcmwmjglBEyq56gSPpRffZd5_AHecblSXwEK1oNe0FRY2Ns43a8gR3KYyksDY8ZnwdMo7moJamVpSQ2PNRvqNwLtq5hESpGrdKpq-dtN0Eq6Qyb0cpk8gCWF0c7Gg_dwjBEEcDZYO90ba03L9k6wacn1xw7oIrlBRGZFrzPo4tIzTXaHwtuqX0nKaNzFGp8ShG0cHTDBd_ZA8AJ_jKYL5nmX_d1nspNOLJEM267eWcgxLByKJ6I1FbO4skDa0DcE8-POEhAiK02BPGDyLqp2FWR2zW1dQ4Y1eQfe3bhK3aBCDXGL1aEp_FafwjWremV0BMV7M9ZM4C47j4ssI95R33qymyZQPKu4OwnrDUFjznjijk1FS8jEqxM1nl8e2dUsncF0RT9paEfm0WiBNSsTZ4m2pb3fTKGIakH5zbErpjEJMPr6wDwQRhfxvyuRcP82NKj_3kCpegOL7Ja4M4Z1N9U5MyDnP0WK37dkKfVD-08eETXNGilGHOiKB-Mtk28slNzsvSTcBdn3-EYd-b2rRYoATQbdr1AfMibhDfYXEi1qB0iuzXIO2a8LjsyzhyUXOy8SSpFxzFHVsOGDAScIrpq-X9AI9_3XN2atNabkb4tovZAXthl2kmo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37370edf56.mp4?token=LL_SvJEXFtOoc8sllVPCTwOS8fxWtbCM2Pfjl-scOXGfcHlDxIvwOcmwmjglBEyq56gSPpRffZd5_AHecblSXwEK1oNe0FRY2Ns43a8gR3KYyksDY8ZnwdMo7moJamVpSQ2PNRvqNwLtq5hESpGrdKpq-dtN0Eq6Qyb0cpk8gCWF0c7Gg_dwjBEEcDZYO90ba03L9k6wacn1xw7oIrlBRGZFrzPo4tIzTXaHwtuqX0nKaNzFGp8ShG0cHTDBd_ZA8AJ_jKYL5nmX_d1nspNOLJEM267eWcgxLByKJ6I1FbO4skDa0DcE8-POEhAiK02BPGDyLqp2FWR2zW1dQ4Y1eQfe3bhK3aBCDXGL1aEp_FafwjWremV0BMV7M9ZM4C47j4ssI95R33qymyZQPKu4OwnrDUFjznjijk1FS8jEqxM1nl8e2dUsncF0RT9paEfm0WiBNSsTZ4m2pb3fTKGIakH5zbErpjEJMPr6wDwQRhfxvyuRcP82NKj_3kCpegOL7Ja4M4Z1N9U5MyDnP0WK37dkKfVD-08eETXNGilGHOiKB-Mtk28slNzsvSTcBdn3-EYd-b2rRYoATQbdr1AfMibhDfYXEi1qB0iuzXIO2a8LjsyzhyUXOy8SSpFxzFHVsOGDAScIrpq-X9AI9_3XN2atNabkb4tovZAXthl2kmo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار مسلمانان مراکشی بعد از نفوذ غیرقانونی و حمله به اسپانیا: الله و اکبر، ما اروپا را اشغال خواهیم کرد، زنان و کودکانتان مال ما خواهد شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/81553" target="_blank">📅 22:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81552">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/h5LWOYntbFpFXlpuhXUj__-2nzE5FSyQc6DQDPYmtvwaFsKZrhgpG9YwflMvNnPX7hB0U6eaupKNFVlts5VgFOoym0dKEklAMvkrygXwkD_2iacgldU9WIYwCHnB-nv99komGL_mWt_aLmMcQP8qhPlsaJs5lKQ2xrTQf2Otbwdjw0s7uxJKOf7QKs6hEaUyAM-bvd3Fem_g92ONCYyymlMR5phhMqsQ90Q85iYj_4r1nDoJ-oew4SKErQlXyGO6su3W5hpkiFJtKhks5ar_hULVkG4v0hwUrxwqFAOQMnjmlgUfxvec1Cug26VyTVS4-qJYxBezs-8mMez6_0HO1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
پشمامممممممممممم
نیکی نیکول دوست دختر سابق لامین یامال پورن استار بوده ، فک کنم یامال وقتی فهمیده ازش جدا شده 4 تا از فیلم هاشو پیدا کردم براتون گذاشتم ربات چه
کصی
هم میده لامصب
چه ناز و خوشگلهههه این دختر
😍
مشاهده فیلم:
https://t.me/Footballi_Dark_bot?start=get_tbcbmlqhfqdjyaew</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81552" target="_blank">📅 22:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81551">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترک جدید مهیاد به اسم چشات میگاد ۲  ریلیز شد    SoundCloud  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81551" target="_blank">📅 22:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81550">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ul_jIjl1Jl3fZjiTwzogz2FJ9JdvbCaxq6av8xYfO5OLzxK19X2Jj4VDHKL5zGHGuv309h0TnAEkq_WZxbA18nV4qdUjE5zikw6iChmBSa9nuf4jPMjRi7jZa1OA-gYuyJTgVZ38WK3DkhOb6Gd0VU0uRqp_G_YTcUu-MnsvIsJraGLxJStp_7WCJ28S-b1utEzQt7un6ZqApycJIcTsncoTH5Hx0NXvT5H9UquYvugCL2Qyqo96CbrdTg3qN6Bx50aMHqD6F2TeGeplI3j1OaKfzhhtsytiwLbvqlsSKIGlMFjdZkQH-LqQ59_pq-PvgC5VeLm5IMR-K0V4udWQYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید
مهیاد
به اسم
چشات میگاد ۲
ریلیز شد
SoundCloud
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81550" target="_blank">📅 22:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81549">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGegnlegDVZ9eH9Q9n3DRWNhDg3LjbrMl8_s6koht2CiNN5iUFgBLjpuJGkou-uLTJoleAxKBB5RArbRnSslgQMv6_jemA6gP5RW0pvaEugzu1JFM7hZbZNUO6JHkQVaqyq6ZkXw-W8A5Pu-rW4ZNjVteAe0YipVjrHxF26ueqgAjJiFGstJif5bWCgC-B7NhBNLlUMc4BLB0SXhX36RsFyjvikEpkb7RNTLBSbtRAvkDCCWJgc1jgaQmG0miY5KVPIQUld_fSAelKFrqa2HtcVBph5Ox5xsaNhpWL8H25wAIYXy3ak5tDCJfAWf1ovbANt3sPNXi1-KXe17DtHh1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یتیم گیر اوردن کصکشا  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81549" target="_blank">📅 20:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81548">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پیج اصلی سروش ولی زاده برگشت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81548" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81547">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIgdPZnoEjF3fENVyR-OgcL8BxCk1_4Vaq0HUEIYsP0NCUF_TWDeTn9yPHEkaXyp_dca2615HQc7iwITezpAzCZxpDs3FgxqhAXxdMnoYtH7IhODQ3Y7ekB942ycpilzHYJyqXidm7zHFqfiD8SWHAu-o-Xp5ccDn6ZtoCIJ2XKVfqcjLE-bBMJeoxkHMWTvt0W2rAaJnviShFoeFOUR_LOGyFfRIpJ2XQ3Yzteu4TAV9w2BuZ8THbnsobezMZPf8lim0YBngJwZq4R1A6w6dZgN8uhQ0ttqSZsRfE7gicgeEO-a_Ojz1ps4fy9s_cc5QMWA4QObx3OhVa3Btn3U5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81547" target="_blank">📅 19:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81546">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CquWJiWp7ln9qJkKbAefcp4u8rE51aBYBYnNtQuCAx31808wjL7QU9L8E41BsTMclN7W0ROQROLcubKynr-mcgjN6LwnyjreLefZ9VJmZvO1XYPXjE7mZAO_TVAjyG0qa0YiYDSs0d0npOvoDbdKQbYJ65sfcuPmL0NcpjK9urPhjgNUmx1i0PEoVxG15iijN9m5cgdv77A3v6joi6WqcsH-XYHzqwJkepZ16NwYQkDjS1DJZfh5j4BIJmsZlami9Tr1yTMnFLGUIhEu8mWqAB1zDbykc9q5sFerATICOXRcisFHGrOvIsqOqzmYk3UBYJHtX1KkKyEspTR1h1Shlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازی شاهکار رو از دست ندید‌  @FunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81546" target="_blank">📅 19:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81545">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEWSNoWO5c45skmBFx3GvvtONwmnjfWQVdAjeyFnU77dHVVGjX9vr2jzJejxcG6tYVtEIT4BIQPybZ2TTJF0td7tR9hrCVlZvBcgwhRBoleGo-lmYLtXjj6XjSVqSCU8SLB5jfoM4smMicK6QyDg_J2lLp6S2wmeo-aS0wV9AOsJr4D41IJ94S9DjAHxW2BIOjDXiYid5KYO_n2EzrS0dP3o20_GjRqTW-WpHWvDVULPHDeFoUq4xhw27M2gYbOp8DSxTICeEKgSTC0JqvE9sXRbKYG3Estu-0u4dVPBdfQ1m2J7oC3Oi_AhTIP22PyjOLdYi-2s4jUspR-L-LsRCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازی شاهکار رو از دست ندید‌
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81545" target="_blank">📅 19:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81544">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8gWSHSOynYiPEenHC4MWWp-yrnGdxP0tofoFWiJJyTlAZMnPNdsYmU3AMo6fcaGh6KvmDfvPrqLVfzaMKgeN0yBGZqfctciFfRHMR37bR3FMMPQAz5G4alGwL8uA_VCsq27MT26tnxl1PWKeEiM_gMVNMJddP-eaM2OwgLwx_rLq_witu-knIXaLzfDuxR6pcpS2xwwcpLI9so1HYh9IegKqpJf05rpUUDb_Yxc0i-XAPHKaEogCJnjZbaXGGuadXuc_JuveMeVSReLiIYL_NeDVHTHEMcM_mhGdR-yZrc3dkFD8md1VNlJB7XAtrVJPpkWmT4ezXOBR0lU2p_XMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بنفیکا
🇵🇹
-
🇨🇭
سنت گالن
🏆
مرحله مقدماتی لیگ اروپا‌
🇪🇺
‌
🕔
پنجشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه استادیو دا لوز
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بنفیکا در ۵ بازی اخیر خود مساوی نکرده است.
✅
سنت گالن در ۷ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳.۶ گل در هر بازی بوده است.
‌‏
⚽️
نکاتی در مورد بازی‌های رودررو:
در دیدار رفت، نماینده سوئیس موفق شد با نتیجه دو بر یک بنفیکا پرتغال را شکست دهد.
🧠
بودجه‌ی تفریح از بودجه ضروریات زندگی جداست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r8
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81544" target="_blank">📅 19:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81543">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaqZBeq0x-KFTWaq_3Qxktob3qbD04bjYmVWb6FmEx9muGoMUKzeoUIUNzrNyeefxChkdG5i9Lk-j6DvaSdM6IbRPoqeQYsdUbfWrf4ZpfrU4hh7AVCaYcl77x6Rg2XTD0uTV4AEhHOjnHhy1Ee2Rd-KcXKAAjZ9wdHavaoF1yCttdMzx9DOTHoB2Meqvylj6MhiI6XBACPodEekmW4FFTD_IUCJkmfL5_YFfV8i-e57_yCnQqgPxji9lWK3DGwvUHboIetC-TTE2M5AYL2LUTGoeGlZ0gdBJVph0sfEGsE0Rp_laoZR4IctrxqDftDXJuVm7ry7PHfeDWWV0ZT__g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران:
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81543" target="_blank">📅 19:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81542">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvkrvf8rAntamEBmG6bXBM1oNRui72hIDtGi4d2r7HUPKiz6zNhMAcZU2-yRzC49IUrOHSlUTiOyJep7wa6y6kzbubPH7atPPEOJyopt13dRvvUcDXxmsvoHg8WTxTzPCjkV89nedBdas2sR5v8vVga8UxKdVYV4i4V72IDAAMcx3jrE2Jth4Qg28xIay9N1K2PHoy0hIp2Dl4eUY8nJJ9KzD4VHalvaJ1nOP5bvgelEEuLKOMWyeS7LJVzGlYYcQJ2kFTYbpKrdOb2MF74WAQeKZ3R43L4rGizkDk9NvkMHEerip3IbGrNdMsPH5Kzzav1vYx6t1x5rUNf0_xJ3fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلشیفته چقد ترسناک شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81542" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81541">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTczOF97VIPo6kOhAxrQoFh5P9EburxOuDBof0fAUE-NY0i-gITzPK5_iOToJDv5uGYWsLCNnrhxpb-Xie5o_AJchzxzGitBkjkVe58bKyocNLZrUF9KZUHg2go0VYmwyPWSAmGnz1clebehpC1hTbCgfNMI-BHaTjoP0q3TS0YorJmJuBHUFv-ffAR_1uaGAVDAQGGR11NJ7urIbxoVSBA7XjBlwpaabvhuqcz3ds1ZjgnD2Z_vRfJ2TtHCAzd3gC6rCEc03rOsvpAwjwrsNJk5cAG-PlLB3dueB2h-5mHVLd4vs2oDMn0V2TDtFqhroQMgxs2OE_pqibjn49JJNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام بنیامین نقدی، جوون 26 ساله و از معترضین دی ماه صادر شد.‌
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81541" target="_blank">📅 16:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81540">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhYYlTJnomeDPwJgzQw-FnxphhGZqD8nHSuR7PJO6OLgn3V_7_4YL-vZ_2C6kOxwwASNiQiVKHsLeHMmgcjBCV4dRnl0FEgANR6Yeb4ZuLLQUZ1jFcq0-c-sEA1INac4jxCz6dJxBRfpSHULCDNM3eG92g5LqZ056z7pp6QGJsvYFqcEIlGWyvn5VUtTHqkA9UuWkGuJL_Q1YnBPd1WMyufQJXWpOy2Q4YvRuftmDxkT9YQA6uwZ6jN6uA2Yod94qTtpwcdzDgBADq04hIrd5CpJdl4YdNcd1kZtCGhnszjFC0ebFeMYVfW6LRSxl50cGUQzNML4Xso6hfyrF8Hr0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیج افشین فدا بلاگر مازنی بخاطر استوری که برای سه جاوید نام اعدام شده تو اصفهان گذاشته بود بسته شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81540" target="_blank">📅 16:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81539">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">از نیرو های مسلح درخواست دارم کره‌ی زمین رو منهدم کنن دیگه زندگی کافیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81539" target="_blank">📅 16:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81537">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0okajL1yLo-koLRf4wbK4QBj6r2l5wlTva5KeiZp6Rtl9-C4YXdoO8hJtB0W7zvDlkzIAGg1jdn9MFNyL6p1s6H2pcbKYRlsQ-sfuZU5TQPI51gxLnejpkBM883IMGYJF8SCHkS0A_KW7QA3hoNlOWGiGP_pgrBXpo0DJBVduE1nM7AE-fpQtI4JseonFQ_43B1lugFH7j-XYFSnPZ1XfgsQuqKhIDP3Eijk70Wy37fG5ni3K_JAlphMQu1KzUCyeG7lqn9upvvVf2Ax_ZJkCb2J2r8dRb9YnRQEPcslf76dmdAl5I3zl1NAaN5DfVO5eGsRlc_7iJ_mv0P3ThYrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفرود سواری در کشور ممنوع شد
تصویرم از وضعیت یه پیج آفرود که این تصمیم دولت رو به تمسخر گرفته بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81537" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81536">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اشکال نداره چین میاد بهترشو میسازه
🔴
چین گزارش‌های منتشرشده درباره برنامه‌ پکن برای تجهیز ایران به سامانه‌های پدافند هوایی را رد کرد و نادرست دانست.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81536" target="_blank">📅 15:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81535">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnHimJP3JbR-tTOEGtAL8nzMgJiSrULtNVA3moXuGm3Kco8oRMEeJBsF6LdYa_fgz3iFrLlP69HCRc_IF9ESlbXsRGOQklk6DCbGAxJhDo-ispEt7VOUuPhf0wT_uT0aR9__ZAVGidqlWeK06JAYmA51HEypYKJfkmd3xJim54wdGuKQFjEatvhiXuul38xqTIDMw7H6-lZUw3A1u1Z4iKJwhH_fD1WQ1-cwUBMCXaK1RoKTICYJAE0_9D0ndYZfGnlN0HouNKQCw9X01wa0p6k9UnU_LDVeOu8WrG1JQHGvGUVaImJS2FOadSfGgqcsAvmD1_Jv7yZWm2YU4hQiyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده اید؟
صداوسیما: امروز صبح در پاسخ به حملات آمریکا به ایران، 6 تا جنگنده F-35 رو زدیم 3 تاشون کامل منهدم شدن، 3 تاشون هم خسارت دیدن چند تا از خلبانان جنگنده هم کشته شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81535" target="_blank">📅 14:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81534">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fd-WnCIUUkdrKzM3b7zqQbr6Lct5r_7NLgds3n7326qkjfm8YTKC6tnGGTlhfJrhnefcplKLs97R038kj864mtKspHDQB0CAnY7z4SZO0uj2WYN0Rufwr6HaROPXbm4pxyypr7IIy4uHCYbFNxMt2nx6mJCFth5M2D0FOEUEtc_ZIgh_F22XIpva---34TMY0NnPfP36DTlNrO3duQqhzQbgMxqoATm1ARLMtpvUk5ST08o-OZBsMw6_Y_JXt8X3Ik9LWlirZeKY1QXF4nH8Eb7ByffTPygoQ9cl7gI7XBl7PrXKOVs5bGxX9w1KOORSWPfWsEiya6TjnkKYaM21CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دایرکت یه وکیل دادگستری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81534" target="_blank">📅 14:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81533">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=ETuWe0ki3LmLsq-zUjYmM_rgrD07uQjTw61eLTF6qky9xmoVyAfVZdeW1AkJC29HEgOky_dG8yzRn_tpa5cakcxb2SZ-UKC9p0rS7xWNkI_MZ_EQvvQ35fwleygQTs4QfN4Jduhy1N7dJ9gqm0syCXvQRzmNvegbhul1eTzBPZVHWrVY17J3Fk_4W58fmdLXo0_cc4awfUzTD_k7b-cLU3KcZL7itfAyffwwOGKaRsVehnd1BnzIO-IWlXFjrKiBuWbLxUsDp6ckVTj8epZFoAsAeUh6n5bSjqKpu1uoT7Jp8rs3q3-KZHq8L5neW2xTkLIc8a4smWz_-te4i815VqeCfpbyn9Woe9vWVQxTYJgt-arWIBq8ccPw-GkVoZEwhzAPG8agYbNochVSsHmuv-BTzPdjBLppqN6b4PYFfU270-bDzRyjQr8OysBywoYJhRK75cPTK45wCikJ7_tb06IFeDIjepXZ3Y0NAm5ef8-KkmF1yaxhujNVv_w2hFp5W790qyhmAHENwIChoSFvphTpSjDsb3KRkuZCp6KGP7vG40_1o42n0roJtIudN71tlHvu9IvKPglhjeyYFi23MvLurlXfV1KJwtjR8rRd8RdaTgoq4iu0LkI8UyYA8ntaNYIWBc8o5cUKw8QuSZaUSEyATnIieB_A9JyvWpyAVWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=ETuWe0ki3LmLsq-zUjYmM_rgrD07uQjTw61eLTF6qky9xmoVyAfVZdeW1AkJC29HEgOky_dG8yzRn_tpa5cakcxb2SZ-UKC9p0rS7xWNkI_MZ_EQvvQ35fwleygQTs4QfN4Jduhy1N7dJ9gqm0syCXvQRzmNvegbhul1eTzBPZVHWrVY17J3Fk_4W58fmdLXo0_cc4awfUzTD_k7b-cLU3KcZL7itfAyffwwOGKaRsVehnd1BnzIO-IWlXFjrKiBuWbLxUsDp6ckVTj8epZFoAsAeUh6n5bSjqKpu1uoT7Jp8rs3q3-KZHq8L5neW2xTkLIc8a4smWz_-te4i815VqeCfpbyn9Woe9vWVQxTYJgt-arWIBq8ccPw-GkVoZEwhzAPG8agYbNochVSsHmuv-BTzPdjBLppqN6b4PYFfU270-bDzRyjQr8OysBywoYJhRK75cPTK45wCikJ7_tb06IFeDIjepXZ3Y0NAm5ef8-KkmF1yaxhujNVv_w2hFp5W790qyhmAHENwIChoSFvphTpSjDsb3KRkuZCp6KGP7vG40_1o42n0roJtIudN71tlHvu9IvKPglhjeyYFi23MvLurlXfV1KJwtjR8rRd8RdaTgoq4iu0LkI8UyYA8ntaNYIWBc8o5cUKw8QuSZaUSEyATnIieB_A9JyvWpyAVWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛ بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده! مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81533" target="_blank">📅 12:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81532">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PetkwdQ40e8iRYKPgm_ALpVRrJ0peQaYzHLdThjjVGnfthoxYRkfK0EKn7gVr3aiPW_k9zgwukROLhAAwGuv-6IP7-3vY0tZjBjsdJ5F-XE02U_6J8FVjgxmx1tl6562aH-ewgzQn1qN_ireHhbDZz-hSnbdAMTwQ8b-aV1bUCpfpNmY9qyvP6TWEgpRAIPlFTwcT9CZx8lNcSs1x0BfB4av2xIpL5VhOjRCQkom6W3y-fJCulSsktHwWgpcxR8jMCzGLR5JapUbwZJLdXZ3-ZFvX51FVuQkgC2U6p7x9_hroYh-7W3TJC-7NC2HfZMa4UZzS_VgUNnaB0GiXucThA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛
بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده!
مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و دست چپ نوید زیادخان شلیک کردن و این گراز بالاخره زمین‌گیر شد.
این مادرقحبهِ 36 ساله، قبلا به اتهامِ "ایجاد مزاحمت، دعوا و درگیری، سرقت، ضرب و جرح، مزاحمت از طریق فضای مجازی و تهدید به قتل" زندانی شده بود.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81532" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81531">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkXARjqntqjZ5VkmxJQ7HRzIlusKw-9Zk0_h7U7yVkGqDJ91SKM_Sq0khBBIihWU9T3Uw1Y9hq7fr4bDnBKuLVo8w3AlxwGnUNEx6UF5gYO3X8QOWFyFWEeyQkt01zsbWCIqvRGc6m9tsMeaJVK76oEGfkl_0kYvsuS1m7FxG0seCIB1i1NGdAjROrEeLE7Rwe1lZ7Zc4opOoLgYbRFkkQJcShaT3gMNzEc0bTF0ONOsrIWeW2NldIQeh_usKeX9KoXgKUhdI8Vwc3Wd7IvAyLuz_f5BIqm7M0zfhLk44fd9BLjwOQgWRaBpG9HxnOn5iTO5TkXS2PAab6I7k2mdwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بنفیکا
🇵🇹
-
🇨🇭
سنت گالن
🏆
مرحله مقدماتی لیگ اروپا‌
🇪🇺
‌
🕔
پنجشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه استادیو دا لوز
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بنفیکا در ۵ بازی اخیر خود مساوی نکرده است.
✅
سنت گالن در ۷ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳.۶ گل در هر بازی بوده است.
‌‏
⚽️
نکاتی در مورد بازی‌های رودررو:
در دیدار رفت، نماینده سوئیس موفق شد با نتیجه دو بر یک بنفیکا پرتغال را شکست دهد.
🧠
بودجه‌ی تفریح از بودجه ضروریات زندگی جداست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r8
💻
@BetForward</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81531" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81529">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یک منبع آمریکایی به شبکه "i24NEWS" گفت:
حمله شب گذشته گسترده بود و تأثیر قابل توجهی داشت. این حمله تقریباً دو برابر قوی‌تر و گسترده‌تر از عملیات‌های قبلی بود.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81529" target="_blank">📅 10:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81528">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81528" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81527">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81527" target="_blank">📅 10:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81526">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81526" target="_blank">📅 10:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81525">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtY0zd_k11A-6Xshm6TpTeWXsyHp_hM1UaSyrKcwzK1vR1ETCGxWuJa4ne_7ljNrP2rsrbJd7sPTQdHOa2DDcywg_vpYnEijbxqHzPoBlzsnyy_F954MFTw5H_yHwB_IISYLzrAkr3mogu8mzlcAE7s9lyLWQAN6HUgLbzFuUAb4cPJpxRXpXC1sfuzFipQKY-0GeWIb0O9UlD7_p4Gdf-LEqY8bdOz7aB4MaoJay1AuU_1U73HjwZ5OlamYPyNW7TUJ00e0GNuCcX051sEaSfeQf3kXey1hqJ2r8axnZN_sFLOrWUuNFRLSFHXD_3Xmp7-i8mwX0agUPyNvdueZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کیرم تو این اکسپلورم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/81525" target="_blank">📅 08:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81524">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اینکه شب گذشته آمریکا مسکونی زده احتمال داره یه پیامی باشه برای ایران واسه جنگ های بعدی که احتمال داره رخ بده، که امیدوارم کصشر باشه و این برداشت صحت نداشته باشه. (اگرم انقدر اورانگوتانید که فکر میکنید آمریکا کصدسته و مختصات اشتباه به بمب و موشک داده و صرفا اسرائیل نقطه زنه نظر ندید کلا)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81524" target="_blank">📅 08:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81523">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b757b219d.mp4?token=gczV6bzQcy5SWkUSGIq4RU5OVuoIvZG8c91lOH60L43n-KCWZSrWK8JML8iEk3qr6IFO5XqQvG8c4ZrQcXaIANhCp-NUFQzmasF6NT4H-8DtCSaavdGQoQXMJVDs2k2XAoX9sdIZT9KCWAKsrYKvTA1qDg-oq513yUrRrSKoaBxNRGvLSlzxMIhpp6bISi8Rq9eSMYKr0YxsyMa8L1l7dlEf-36V8hY47I1GBGZKGXNS9uH8onhCz1JJR9fpc9yNGQPbcRplHaPa12Qdm8kJCe9q3mI9vhZweTQtqVcg-KxFrwfWw_sTkkfQ4SQYRD5ZJZ2hJAzYfCpyn5TbmI2VfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b757b219d.mp4?token=gczV6bzQcy5SWkUSGIq4RU5OVuoIvZG8c91lOH60L43n-KCWZSrWK8JML8iEk3qr6IFO5XqQvG8c4ZrQcXaIANhCp-NUFQzmasF6NT4H-8DtCSaavdGQoQXMJVDs2k2XAoX9sdIZT9KCWAKsrYKvTA1qDg-oq513yUrRrSKoaBxNRGvLSlzxMIhpp6bISi8Rq9eSMYKr0YxsyMa8L1l7dlEf-36V8hY47I1GBGZKGXNS9uH8onhCz1JJR9fpc9yNGQPbcRplHaPa12Qdm8kJCe9q3mI9vhZweTQtqVcg-KxFrwfWw_sTkkfQ4SQYRD5ZJZ2hJAzYfCpyn5TbmI2VfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متاسفانه شب گذشته هم:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81523" target="_blank">📅 06:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81522">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نتانیاهو:
نمیدونم دیپلماسی چقدر ممکنه اتفاق بیفته، اما نسبت به شیوه رفتار ایران بدبین هستم.
اونا همیشه دروغ میگن، همیشه تقلب میکنن و همیشه برای خریدن زمان بازی میکنن.
آیا ممکنه این رفتار با اعمال فشار کافی، از جمله فشار دیپلماتیک و اقتصادی، تغییر کنه؟ باید این رو امتحان کرد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81522" target="_blank">📅 06:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81521">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">تسنیم:
برق برخی نقاط اهواز قطع شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81521" target="_blank">📅 05:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81519">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">انفجار های پی در پی قشم و بوشهر و بندرعباس
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81519" target="_blank">📅 03:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81518">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بوشهر آبادان کیش
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/81518" target="_blank">📅 03:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81516">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a76739cd9.mp4?token=XnwdkQvYQ5nGoywQFuSCWIAUTjVnqGJSjMW7QId59zNWc81o7iY3yNDi7fxE9qQjtGQONskT537Wy5QEqJy8GSkfaRWYlXIZJVv7Y1iwrX0UFevmueFK3g2CoqxovpqBnV_SLU_MfQaMEnmJf19ECzUfpsBQXwp2C5OND7aezLDMWK-eOpvl1IKkw6ARu-2b4HwiNf8-kssh4NVe2Q4GIq-RK5SkZYSbKOimxRIR_nKo0BdOOGoPJt6lsDwtDxIaTJeRXSCrGPt8HwHW_WnzYz-ZZzZJlaF08fhWkvpAKdWRHiCwALFQijccF1ip9IdoDNlGrZgFTsA3aPsLmprSvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a76739cd9.mp4?token=XnwdkQvYQ5nGoywQFuSCWIAUTjVnqGJSjMW7QId59zNWc81o7iY3yNDi7fxE9qQjtGQONskT537Wy5QEqJy8GSkfaRWYlXIZJVv7Y1iwrX0UFevmueFK3g2CoqxovpqBnV_SLU_MfQaMEnmJf19ECzUfpsBQXwp2C5OND7aezLDMWK-eOpvl1IKkw6ARu-2b4HwiNf8-kssh4NVe2Q4GIq-RK5SkZYSbKOimxRIR_nKo0BdOOGoPJt6lsDwtDxIaTJeRXSCrGPt8HwHW_WnzYz-ZZzZJlaF08fhWkvpAKdWRHiCwALFQijccF1ip9IdoDNlGrZgFTsA3aPsLmprSvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان مراسم اکبر عبدی، عادل فردوسی‌پور در کنار عباس صالحی وزیر فرهنگ و ارشاد جمهوری اسلامی نشسته بود میخواست دستشو ببوسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/funhiphop/81516" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81515">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81515" target="_blank">📅 02:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81514">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81514" target="_blank">📅 02:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81513">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بابا کصخل بمب افکن نیست که رادار خاموش کنه، سوخت رسانه</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81513" target="_blank">📅 02:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81512">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بخواد بزنه ردیاب سوخت رسانا رو روشن میزاره که مهدی ادمین فان هیپ هاپ بفهمه؟</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81512" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81511">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حاج زدن حاج
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81511" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81510">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81510" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81509">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کصخل سوخت رسانا بلند نشدن که باهم بندازن، بالاخره میزنه دیگه</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81509" target="_blank">📅 02:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81508">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81508" target="_blank">📅 02:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81507">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81507" target="_blank">📅 02:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81506">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فعلا چیزی جز صدای پدافند شنیده نشده به فیک نیوزا توجه نکنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81506" target="_blank">📅 01:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81505">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پست آدرویت تو چنلش: این روزا انقدر اتفاقای بد و عجیب میوفته تو ایران آدم نمید‌ونه از کدوم ناراحت باشه
🤧
🤐
🫤
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81505" target="_blank">📅 01:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81504">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81504" target="_blank">📅 00:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81503">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تنها اپی که سپاه و نیروهای نیابتیش میتونن آزادانه توش کار کنن تلگرامه</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/81503" target="_blank">📅 00:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81502">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ این جواب سخت ما چیشد خوابمون میاد</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/81502" target="_blank">📅 22:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81501">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DN_frT7MZCp6YaUXk7IbOru972ypIRoxfxsayHF6ESy7U2VtXtaVzCiB5K931Xrggw9mlG1SE8IItAvUSroqbJ9MkWJpyc-yywEnHQd_1LCOMFicpFptxhWVuIcs5r8IKjgWblFFKRRVcViewRKrz1py3XTIlyb0qNbr24KlEjgxbXJOF4Pph-uWnpDlOEr1f-P0Rtd9k_ttJP21yShjTlMZUBvY4lHcrf9KM4uLua2cRO1XcdaB_kMhMHvDm8385Q6xwNEYjqsGkHXKhLgMK4c62FtFpkXqYxBuguVHSy_wQ48o2qB7C6bJPylPEhBL1-JcaNpFoUTY2OqiKJHn1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برا دزد شدنم ۲۵۰ میلیون سرمایه اولیه نیازه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/funhiphop/81501" target="_blank">📅 22:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81499">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نتانیاهو امروز با رضا پهلوی دیدار داشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81499" target="_blank">📅 21:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81497">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maSm9h8e0LqIIdL2-43WLFbW9022hRaovrN4Qq8u9xigT2KSt8QInkaZwlVAYxD3DHvJ-sUVSCoVTZs2PxM2SXhtPCoafkB_AyqMlg4K7qifzEK-_FEoXH_C6QkOq6yYEHny0HtUChxhBAd-UXyyv1Pd6eyWkNkgjiQeNT_N1VBPG44Bbp-PrtZQRCTP0xewMqeYxkGbOk3T35egF6uVnaMBa6dI7-vOji4SGM2W91fLHYzUCqUHYlIWbgJbqe9IXVi6bt_suQG1dTT3XULoDSUFZ0_0LMiI1t6F09LkNDjF57o6J9uSK4ACW2pGtI0lwVYn-UzwxXUkU9z6-H-4lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام چه بامزس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81497" target="_blank">📅 20:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81495">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEXKBfG78QA1P7nPc9w0eGenMacx13R_dVVsJM9YbgH5DJXg5VTvLZq9faiG15SL_7Bg8oFi0qTEmferYlvF57WLm35Q7z_mIFaa1RYuuRU3DZO5Dxlo78qwX0Q3dpUVLfy4a0JorDycPBzzGknAs6woMALkJUzthssIWz90MsatTxI9C_9oH46B_ndyTYDVvxMh1Vjb1ehmXmf4NLsDebLBdiWP9LsvUnsX2AD3aeavIeB7OuYlZ4l8vw_5KS67mh_HEYinQ-_0ndhI6Uc52Xx16i7s9rToCRlNuhDYfEb-RfqGf_kggs4dsYySlz0xUY3TT7e_bki25XGLlDidQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی بچه اش رو دوماه زودتر بدنیا اورده با عمل که فقط تاریخ تولدش روز رند بخوره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81495" target="_blank">📅 20:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81494">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7dtkP-fyUgd5WXf6QMJWhX6FRAM1sZ7qa-qGdJ35EvmFCoFVZY5Hefh6KNRWO0iISfVo3tDE_Snh0c5T8p8WMJ4EFMeEONlFITj7VsKGEbvS-pMlXj2t5CmSnKlq7fsPU6F88kQNszNYkxHLJC6_Ai1HPEgIgHKZprn8nqMiBrktCH10DxW9e-trHiwUjrxtScYHLKF8gl21I1zr6-pr8ZPJ37crn-POgKGEmXPbZJk3Xur6jkrpiEW3Qh3HdkrgrAgvUu_FfV-NVuID0oD8CzNf8o_dAZElWXsbmk_0wPaOQnUOnOBi677fLkuLFs2Ne4l8V0jvNBl2lcT75NLkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوتیسم پسر کوکوریا عود کرده، بخاطر همین دیکه موی بلند جواب نیست و باید ببافه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81494" target="_blank">📅 20:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81493">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پرایم هیچ بازیکنی اندازه رافینیا ۲۰۲۴ بهم نچسبید</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81493" target="_blank">📅 20:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81491">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">از وقتی تلاش نکردم برا باز کردن پیچ خوردگیا هندزفری سیمی کیر رفت تو زندگیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81491" target="_blank">📅 20:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81490">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پول ایرپاد نداره؟</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81490" target="_blank">📅 20:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81488">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JSgLPMcuJfIENbotFXlWVFMJgw-4zTZ0ItcH7IC5TCfwcr2N6F2-ItVpJcMiU3j4T6XZzxIjpN0t-qwa85-71uHR017OfcuHZ9mME-5aFmS0Xn2CKfo3p65xsus8ttF5Sov855aKgs_9hjCPUE4w4-gfQYVfvOOc_Za1VTqygl87szmaEBRtkyzL03l78YSKb0e8SHWxgAfEj42h3YZwXGG4HaACIvRRD7zadgpZ5BLuwAWsc6IeWEMY-S6BWuBRnXJlPxal41EQjxPEAhl7gM_GaM7Y47HeelkxOgap1mrp8uMWy4N4OuQsfPnORCMNZmu6vYQvdjDqkCvRpuUO4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lIXYj-gC7W6XWjq4oZMs4x1lpiBez95PGiv4NV0WttO53EMcwsRJhh2Vim6fOClpwjDO-3V2-8Mtka733DuIASa4CT8Ji-6WkPBge21tpfToNUoRvjjZkHGxtvGWp7tqJG5gqAAdwA2X0KqovtwBQYHbMq9_p2DAjKEZ5aNLZZ_wvC5rTNTHRqEK4AmIdGTgIbjeRjU2j2oK4SjjAoW7D8T-pKak7I2IqRdGPm-erfIy5tio2nO1KIwkfaahck5JdfAh6Ee9HQjjSYiXJKQXAmRmTEPb2hEZEPHtiOzNrN7DHKKyeBzwL_Ni5lWRZsuOhL6wipAV7d_16DXAC87jpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رافینیا شبیه زن جنده ها شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81488" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81486">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YEYeeBhvoh-x2P6NHf-NCs60x0dx861CN_5QGu3g11oKxLVqbpc558FZmg5CPcTLPcZNZs0vFAcahugVtTjcqGoTkniPFVn2skYE6g9zrOcDxDv4Oc_bz0xkofJ3_blWmr9u-dTCsbf2d857j-MlHxABCkCn-FzgPxrzjW_ei3DIFdLQkKd9WntD2fbYYHpnfNiKgkBRDF9s6BEa5QFVxo4tMvV6zA6zNHYzEfhqQPZzMotoS_dRTqR_9YSnz_wDAbeAEKqgJKHUIi26oomYxwWeQAAQ-eyN1bzyklKujr8yMzSc6z8-bGbxtjCB5j0nqqXYXM14IAY6UL4Z4jvSSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eKHjS2eSRW1aQ4ScEaDcYwPneBVKyxKVWfvumouMuFp4rxYeZA2dCrFBoZqYTmzhGh3n58CPqKk9pOhsNPN2vgAJSTw_0A6jd6TLCScRfty9WpmM2JsZtm6Nl9z6BYeaurg3DlPg6ZRqhQqiD_YtgWzYkV0gNYswt8v8t5ufcdEwvbq3U9Q7arDvqk_20g4WZDGYe6JjrkO7md25A1W870EgxEvPiEh4vOYht_SMRAL-_fDzlULidJaFdhjAH5iw1QVCYGpan8IblNgFAVxZjWXW92kK8BzDbtVBuYWzPowu7tfpKkAAfIXzSoPMQVwWVZg4bTJcLbeWZ47RVc1eWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هرکاری میکنم نمیتونم با قیافه جدید وینیسیوس کنار بیام.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81486" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81485">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQsu5aolylIl4UG0yy3FMg-ceI01Yexo1F07Xt--lwFAVtVOTjhlNjwdxdaq2-w42jCCLKl_vQYWzW3OFyi1DS2KOjVbIfIntd8AXHebQzCnsZrMx0l_WNqdw4nsOdmrUQTHc8-yimt2AiS64RCnQ_4W-fKMYHvoW7OqluBuuo_yVpNEAZKJH7Sfjep28fXCn3YoOKNp_VlDlFAqqLr6A6XAwQT0v0Y6Yt_5QVk8gEcle_KrP0HyCbkynYJG3qPisEFE3YX4iN2Ty9EI-yXV_NKdOuFrH3e9tAcGQy13yXkWyxF-BppsZyCUEeltqg_cC3luD4_RKf0h6NijsXDXDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی بگم والا.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81485" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81483">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKl8d-wDg_YJwZ5EruzGdIL__gWY689apFa6tIDCUUvyp46Xyl6oNebfGQXyzdgnbklbWD4RVeO7Kz5IYpldAZbw2NYP2mHnbAwxr9AJ0GqjGWfmdj0Onfk3mSm9C6ygiBdd0EsSb9QcF3Aub_OoL1KQcopfqBmlDvtKtGc9rHhlS66U0MpzJxQL3uYfRxbE6cD4adiuSPfi4OHPMw77nmHBGjZGAuIQ8S_V-SLsdzJI2JvM-xvWTJZSH_XPFlHyo81yn-Q_EhEnzzSZqBGeuPC1h2FrVH0BGoOGV2OBdutrai7juSgwwNdQnUV7390C-qorC4T8D1iywdVpvUA9tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس جدید صابر‌ ابر و دوست پسرش.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81483" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81482">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmepDlXh3e8kW6dLf1luuq2a3ff2e7hdZB-amQCCRuhK1orrfhT9f1pTXGgrjNpoYpmDhzQ75RKZvBvYARety3J-cv1pvncfLNxO7p6cxd0xMk9IBP7yt_I_WaqI1oNCnIg89z_39a5_HX8r1NB8wZCr9XfJWoArt658PZiAacpf-WvkcxdnZk8eXfucxEozv51dIeyMmCs-6ET2q-PnkZkJk0t11FFG_ipJqbGJ2u-JxqUq4yi9H8a8IrvkJuJ23nFT18s4g9LESHXVVu4xCln1LjrK2uCjY1b298OakLlnr87LL28GIARemXsYB4-oS2VdlsB5SIS_sj-SL-N37A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81482" target="_blank">📅 18:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81481">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXCSJ5j75mXK1rCkct-UwQEdwU_J4wjxH43RKm0Ofb7lrqDJz3QR1VwAfXLgFGcIyVRE3wQnA05DfJcuoIVZ5AOKw12DsRF7TRmxCeE2lMNiX_BpfXDoBwUujtwuOCDB9PlkRUru3Wvwr9k1QcW42YBMlcTy3arXorKoiWjld5Dzh7o-G0ntXIlpQ0-ArOoNcZkPdK7huaioGVESv37mx9cthEZzmrCK-776M1D101ql9V3cq4kaF_U6ZXGfov-e20Gnw_eGBABSDgzxVaA13ixNgI8AnKz1VffFao73RD7HTJgovrISQYO4u5wJaQ0djjupxswM0_FBIxcwVXOIMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش دورف:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81481" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81480">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81480" target="_blank">📅 17:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81479">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIsBHBk9fihhSAEQ_ueIRmff8mz-Jbo_d6L1TEMCKXyXcfqnO2doOUo9OiSabk4zA3eguiXjH_2FEJJ48F7hpkX0m4BB1PkXI4EVHuW74E1nshJP8Z4rKbPSweDjQP1s9NJc4lNszvQi3R83yAjy3of-4qunpqwz0pipUvDTSitDRepjHaiqNeXpEGT0DjIxy_qd_KF3iPh-a80k2sIbeTkyoyNh2c-vDUcT4NXzz17iWAf7s8Vt58pg83LbqEngVLor7JFh4qjLywZKjpqcc6VvQdNQA8lhKMATs7uz5yOZz9cRyl1legktZV6_c1d85FkPC7EQNv4pnXQqM5kV0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81479" target="_blank">📅 17:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81478">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUBaeajIdevSUoUe3WjoZo3NQNtjNqZuVA1skYgFopipAB4zXtt4l_AXOvfc36K9GytcYV6QrHGdLM2jgqP4S-0CQOu0dWGcKpnP7FmxeuUBC2AESYLPrB9ppX63SperYi0HIhKf9k_l-OZl8DvYloQbm2-cUKYmbsaE1YMsk7Q17vZVgO2pI-QFH-jVBR4LxrsLSbJERaIdnmi9agdNHYY-VDygiQ3CxaKzGIDDMc392U-qDRg-Qc95YfRL2IWZONu-YyXUf0iUSjrHRQT4ZcVVMax7U_1-c3l7rSEp6dmI9JnW8pZPHshiaEaUmiRv5gqAa_jgyP3umhIbOlMVYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81478" target="_blank">📅 16:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81477">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ: ضربه سختی به ایران خواهیم زد‌‌.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81477" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81476">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">منابع نزدیک به سپاه میگن در نتیجه حملات دیشب عربستان و آمریکا در عراق، تا این لحظه دست کم ۵نیروی ارشد حفاظت اطلاعات سپاه کشته شدند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81476" target="_blank">📅 15:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81475">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81475" target="_blank">📅 15:42 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
