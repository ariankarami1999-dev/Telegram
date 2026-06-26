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
<img src="https://cdn5.telesco.pe/file/sP7IuOnoEyfCSWWMsQho6qEvmTbDcEeMrfmZwXgQJSs_rOi7UgDa6MgtI-aqFPlMFcmOIVdyjf7EFfVJMZ3H_-xSkjEwIoNpoqKSL-ccuWUSSNnJgfitez3v1K4RP0XOKB4qMmwn1wTJak6wrMXzcBpNrgC6sNKky-9kY5b4qKVwqKm09TNFCziG9xpaF27MhLZKcwd--1UOqBTeMawzoZ4l9p0d1hT8_wjBb3JExjY0UvIsyR6AD9TG1NDWLBovrR0N1jtcH_mDAI_wpR4WgykxR7Fiqu1RU1DsxC8aguQi-Xw35qMf2dlioaFqt7uNEny0ITcsuDVvvWMe5SWbHg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 692K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 15:59:24</div>
<hr>

<div class="tg-post" id="msg-96044">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkRzx2NJQ2-7MEluArPzGvpzinnGLLQBxiVTuF_O4f7zFvWBgZLQGgMYLUHmO_BdrP_wCRkDsYcfKB6_DlwOvYhYPookvGn4JA658vZlC9SnQkI7QMiXLz4lcND2cJ39wf3WwzkXjDdULrRp59LLx5FdTenIGL1jWkFsI_8blZauD92nuxrYNvove2WEFs1pGKhG_ZithBfSSTeSKREQJZ_En8WDbphTNjJrY-RSpEvd0zWf6pf_XWFd0oa09TIxRC3DOYeaep8juDXzYp0p2yz-ntJ9GgrEL2H90589lZxU450s9Fm3o3LyLvCBnr_GyS3EeWSstDfSfg1KgphDIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
کومو با رئال بر سر خرید دائمی نیکو پاز به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/96044" target="_blank">📅 15:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96043">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7trhZmdNzQOrDZrxK8nQ-v4bfQ5Y8YYX7HHpImLN2al1J6OCdH-X6Hd2DIRj0NcL2KSTvbqJLpBI0JIUiSlCoP2Zo2rGa1kpufX7GErlmkBMDE0XlnSM8fLMc_oUMaKSJ_7wvsWtpq3YsBPdH2WdgVIupaS0KjYAFZEqcr3wVG0W68SA15PZduxn1dVjVdS13EQ95QTiTDAipTAgLb7zt-ykowNeUeOX_8q4sS6mBnT7bGa49vh10VuX0CNjTP2pR3PWXSWhIcGYkq9HFhd7RJ5K7IGKX6wOaDScpl5amroLH28BXlSSzt_HD5BEOHGf2ywGrco1yawndK6q6l7fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بازیکنان کدام‌تیم ها در جام‌جهانی گل‌بیشتری زدن؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/96043" target="_blank">📅 15:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96042">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1pAfgFYvEqRsJbtgVXVo5GQA8XVP7cniwsCKQnyKlF93KgFImWtX0bO-nzK0jg92atH8eLgs9skqDc4pD_UaTStXA2kBeosA-4kWqxtlZ1CXHFwVv4LftRnREuwzJPfV-qnUfy2T4017k6EUS2gYkIIqUHgNzl-Hrp7lFTe-47qVjIICJcQ5Gj3to1oYld11lfZSXKMBtDvMli5q9Ej_gNukg27av3qxqz0aNyaffV-tnp9SsXQmmdzVaxM0fovfABF0l3zhdijZfmQRYY8XZi-P-9SYyxBn2Sx9eP1vOwfaVt1jriUVchMgP5BHTJjsyUj3Ih8EgCehkjlGHL4tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏆
🇧🇷
تیم‌ملی برزیل در ۴۴ سال اخیر همواره در دور گروهی جام‌جهانی صدرنشین شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/96042" target="_blank">📅 15:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96041">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c2067f79e.mp4?token=ElraGLgr2OLL7WhQDOEfCo_mX2X_qRFE47dlnG5GgipLey-D0vUcOXRjg26oT6_RwRMPPoPHjOwM7-4ibdTymVwmme8I_kJt0eqZ2QCpVMm0EdTzKok1b8OigKRgoRTRJH7q8gOpeU3alOOzlWjYK5a644GoB5ZcpMVbH9RPgRRlliCBon7K0_65tjaertxZmg4aY5Sy0RswbwGk1apD5SQOVDjbsYCAaANCKq-DOMEZHJHwSYa6HfFKK4CdBn3jPi5ojaOUbLmzlgZSOhKJVarUNRrWEpLAms3cQUb10s3XUXbdbZ4Rf9_dTfMryC694xcgcgr37YM2TCoYTa666A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c2067f79e.mp4?token=ElraGLgr2OLL7WhQDOEfCo_mX2X_qRFE47dlnG5GgipLey-D0vUcOXRjg26oT6_RwRMPPoPHjOwM7-4ibdTymVwmme8I_kJt0eqZ2QCpVMm0EdTzKok1b8OigKRgoRTRJH7q8gOpeU3alOOzlWjYK5a644GoB5ZcpMVbH9RPgRRlliCBon7K0_65tjaertxZmg4aY5Sy0RswbwGk1apD5SQOVDjbsYCAaANCKq-DOMEZHJHwSYa6HfFKK4CdBn3jPi5ojaOUbLmzlgZSOhKJVarUNRrWEpLAms3cQUb10s3XUXbdbZ4Rf9_dTfMryC694xcgcgr37YM2TCoYTa666A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
▶️
خاطره بامزه مرتضی تبریزی از زمان حضور فیروزکریمی در ذوب
آهن:
‼️
سه روز مونده بود به پایان لیگ گفت تیم از نظر فنی اوکیه مارو برد ویلا یکی از دوستاش تو کرج باباکرم میذاشت کباب بازی می‌کردیم عشق و حال بود کلا. فرداش مارو می‌برد یه محله پایین شهر دیزی میزدیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/Futball180TV/96041" target="_blank">📅 15:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96040">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OINFAOTp4hsx8fCZGEBh-2ygqNdbuxsdiU-dhxOwj2hlJS-zRR3fIOvmi2xOvM4EwWMeYELWI-AiAY8609TrDYZI-N2n3tIrobbaDz1njs6BwtjLpewXgwh0lyDejNft1xrycw269gzVa5LQAn8b41s2KgvBoG_xaV1Cejpwlo9oLaLOXR1vSSIJj3Y2SIYkHhxjqJHlxE1NlYgrC4oGdQ04x1Gszgj8XOeiMG5TJCX5O_t2FXDp9JVIouFLEZg0m70uraorbfDNaGZPVpCK8rLacfuQesZx3G9lPr_4pK24Je8vT_fju9IQAUS7iTNLyuZEFIO8RpB6aobBrTXAEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فنای تیم ژنرال رو ببینیم.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/Futball180TV/96040" target="_blank">📅 15:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96039">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZISQjxR4ZSO7iPFhR7rUf885mbSYbrZKW19rEfmd6Gtj0f4MJrxW-ip53ZJaXEst8rtqAG0cI1yXG1ILXkAA3isCsXx4dqyKnA7DpBj4cWFCBZUDrc707LgAhZCnnGWoByyVl8QxVCYEDszRYNvAB7Eex6UfebkXd8E2ZOz1spBarvbdO7NPXFaBu_RWf_CHU2zF46xd8ieuDNzDych9VHPM_xUksRS8uUknoMf-uM4yYoeTp8RLb5fWGJTFYaaaak373ckfZ6Tsapv7fCzOmjJlUXhOeePi2wneSSy9yKbyT4bR01fU0egTYe675RnZY-UlCTx8JT-dqlREld8mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇧🇷
ادر میلیتائو:
تیم ملی ژاپن همچنان در حال پیشرفت است و در جام جهانی ثابت کردند که قادرند به مراحل بالاتر بروند، بنابراین باید بسیار محتاط باشیم. آنها هرگز از دویدن دست نمی‌کشند و انضباط تاکتیکی عالی و بازیکنان متعهدی دارند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/Futball180TV/96039" target="_blank">📅 15:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96038">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74737ca0a5.mp4?token=JNLHkNq0AjAt69kBcBAgKFEuKW4zo6BCPlNJnn9-9ROophSaBr_RXN29IxmTUb5_jpxtUS92nRTSkjz_ixYZX7n4zddxtKlzOTHZNeE3eKO7-EPDSBZXyZNXLmWoPj-YMrFFtVAKZ7PTA-y-lqcOlxQ5zonOaYbCSW6rM2h11lv7ehRWM8ZMej_2erqPIeFDLXfrZ5QIzbWvKVsLqGC56LZ_AdJBarPN82UUkGz75U3rmwJRaB5c535k-t1ASVRYrMXw_DcO-2BVRXvJLx8QCjfFldsFRdctKfxA-e2y6Y-ZF_RMBtk_lgbrXpZSlFo-SsIS1f4yj7TTB9oie4Jnfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74737ca0a5.mp4?token=JNLHkNq0AjAt69kBcBAgKFEuKW4zo6BCPlNJnn9-9ROophSaBr_RXN29IxmTUb5_jpxtUS92nRTSkjz_ixYZX7n4zddxtKlzOTHZNeE3eKO7-EPDSBZXyZNXLmWoPj-YMrFFtVAKZ7PTA-y-lqcOlxQ5zonOaYbCSW6rM2h11lv7ehRWM8ZMej_2erqPIeFDLXfrZ5QIzbWvKVsLqGC56LZ_AdJBarPN82UUkGz75U3rmwJRaB5c535k-t1ASVRYrMXw_DcO-2BVRXvJLx8QCjfFldsFRdctKfxA-e2y6Y-ZF_RMBtk_lgbrXpZSlFo-SsIS1f4yj7TTB9oie4Jnfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
▶️
وقتی الگوت لیونل‌مسی باشه بایدم اینجوری بدرخشی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/96038" target="_blank">📅 15:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96037">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEtIyZNFp7Z_yE1o9NnTvboFUkSTJHSNMB_zY0Nr8JFzy5SzwX0KfNnmxCmAyKGRUsLaUGC2s5bAYks2Uxw5WLg_pEkpRUgih4NuTc9bWVt0NFCb-u8xfwj_v6ETRppTb_7WuLaz1vUduZt9XodcKuG_Pvb9KGd-u7lvTF9U89pjjABS-dVj5LJXCSJN0PzO3IKyrpV4TVIucxpy6-UZ78bnLhVgCcv23XhmjXWito9GVFlGxszmBJ6rvvg8_14hzY8cWFxSwCoVemhSdiEaohM9SQ4uEVnUB-xC7YQRUsQDtdHVjyPUS2lQQuP1HuFxG_flBb2wItN5AgQy7cRUXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
🇵🇹
مسیر مراحل حذفی آرژانتین و پرتغال با توجه به نتایج فعلی مسابقات
🇵🇹
پرتغال
🌬
🇫🇷
فرانسه
🇪🇸
اسپانیا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🇦🇷
آرژانتین
🌬
🇨🇻
کیپ‌ورد
🇪🇬
مصر
🇨🇴
کلمبیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/96037" target="_blank">📅 14:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96036">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
📊
🏆
نمودار مراحل حذفی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/96036" target="_blank">📅 14:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96035">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d3c29823.mp4?token=gs0EcbvcTi-y8xl1PAjZhkS-_HNAMhVRieaqxCTeGYI_Xjc3DIEaH0N8m7MxlfX8IEimZj4QuE7Q_uF5GL1q6CS-43PSDK3sRi-2eSiZRdgBqvqQedummSLpI5guyzovNIHxamPG5uJibfwROcHIpMK64KnmnKNjmV7dE6lVWhUCmHCqvLQRz5f7uqeY8muDIdc2mnZcfDiIDdBZ5lZbcSs7zgUx4sF75zYcOSprkiLdsyMlNnkzQwM0xQxPHdvB40dU8FYZcvSCy6GgIZGI8v-U5MnSxNA3LBULNZsbdZA7MT7du8AUE9e-pD2-iAMdH5-9-DejT0j1vgkCdda2X0ZqBuRtumi6Obj05NxVnQ1eyWzqC_rCBivrSD6UByTVRIV0Vw0ptsBnvy8yAxwF86cVXcdAS7Kz_nzcGA09KKDzOLsUmKeSQ9VPpZmye7BBTQpHOIuDIMbNYu1_LIpfkuStNGvWMrvoqmVGbl3p_U3HCBF7-Fj89ZANZgNiRFB1xu4GBzkA3UKKvS09WJIYLNq3DWJzbn-L-9mL-yrigGo86wyYngt3WYuXXjrzCbjcAuT3ePzwmIdOfpSLA4FAKkspYe8gtkAB34x9Jx8JE6788PRNYd0AAUslI9-kgq7Kx8J7uye0lLPLM12U0BBQ1YRB9lXUERvzPMLtTHORfnI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d3c29823.mp4?token=gs0EcbvcTi-y8xl1PAjZhkS-_HNAMhVRieaqxCTeGYI_Xjc3DIEaH0N8m7MxlfX8IEimZj4QuE7Q_uF5GL1q6CS-43PSDK3sRi-2eSiZRdgBqvqQedummSLpI5guyzovNIHxamPG5uJibfwROcHIpMK64KnmnKNjmV7dE6lVWhUCmHCqvLQRz5f7uqeY8muDIdc2mnZcfDiIDdBZ5lZbcSs7zgUx4sF75zYcOSprkiLdsyMlNnkzQwM0xQxPHdvB40dU8FYZcvSCy6GgIZGI8v-U5MnSxNA3LBULNZsbdZA7MT7du8AUE9e-pD2-iAMdH5-9-DejT0j1vgkCdda2X0ZqBuRtumi6Obj05NxVnQ1eyWzqC_rCBivrSD6UByTVRIV0Vw0ptsBnvy8yAxwF86cVXcdAS7Kz_nzcGA09KKDzOLsUmKeSQ9VPpZmye7BBTQpHOIuDIMbNYu1_LIpfkuStNGvWMrvoqmVGbl3p_U3HCBF7-Fj89ZANZgNiRFB1xu4GBzkA3UKKvS09WJIYLNq3DWJzbn-L-9mL-yrigGo86wyYngt3WYuXXjrzCbjcAuT3ePzwmIdOfpSLA4FAKkspYe8gtkAB34x9Jx8JE6788PRNYd0AAUslI9-kgq7Kx8J7uye0lLPLM12U0BBQ1YRB9lXUERvzPMLtTHORfnI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مداحی محرم با موزیک واویلا لیلی
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/96035" target="_blank">📅 14:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96034">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBT2tsnYO7nEKMuw5OswSm2sVrbP0PHPzuujOkcKbZxQ9_-cCoLFy3aiyF3AUdA6EkdbBsuSmwaROlsQSqYQ0DnKXieDNPINB8OfhP-9mI7AWbGB3pZeBOXy4ZXloYox4yP5qXIV7OUOOEbB5hwai7glDAnrdLKOlyH38D1YLwODxGlHOzVoo5RHj96aFISp0wEmQFzHW2FUhW6oqQGuE0q0io0ICCrI1ohK156zO1l4_EWiLyipxM_Afx-Nemhbd9vwWnI8VmkYJqjadJJIUIdx2GsO1srsqqAVvL4fkZAH6gC0Psu0aJBkjJXvRUQt74-mhhf6RBQY8PXO7IAESg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه هالند و امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/96034" target="_blank">📅 14:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96033">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=lt9XiEjUNhmiP70zGTQMgT1IkCCdIpyMaMm-xVTyrMWPMWm3mK08szuLLK1oi8JQOC8H2k-ogzA326yE7cgGpdCuXGn1QMp6GlvEvl-xevbCrnhlgHtG0wtiNkOR5hiOv8q5p4vZUMemECyQTI7w0iNnrNvBXMeAjB9PZvwt8L1A8ndlmvmfawVlO3tL0XWaIRaHcqN7MrQsB09zRFERgAwQa6JXkvoyhlzHhvQw40AECJmMfx67kw6GiWopYW9vyZsVhv3suZO9xZAVre79zC2Lj4ic4amL8LNFM08vMOCg_-hcdiffDOforV0SOc01H8tuW7bqDUFjt6X9JHbUpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=lt9XiEjUNhmiP70zGTQMgT1IkCCdIpyMaMm-xVTyrMWPMWm3mK08szuLLK1oi8JQOC8H2k-ogzA326yE7cgGpdCuXGn1QMp6GlvEvl-xevbCrnhlgHtG0wtiNkOR5hiOv8q5p4vZUMemECyQTI7w0iNnrNvBXMeAjB9PZvwt8L1A8ndlmvmfawVlO3tL0XWaIRaHcqN7MrQsB09zRFERgAwQa6JXkvoyhlzHhvQw40AECJmMfx67kw6GiWopYW9vyZsVhv3suZO9xZAVre79zC2Lj4ic4amL8LNFM08vMOCg_-hcdiffDOforV0SOc01H8tuW7bqDUFjt6X9JHbUpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
💍
امیر قلعه نویی درباره حضور پرچم‌های رنگین‌کمانی و برگزاری مراسم حمایت از جامعه LGBTQ در ورزشگاه سیاتل
:
ما اینجا برای فوتبال هستیم، نه مسائل دیگر. تمرکز ما بر روی مسابقه و کسب موفقیت است. درباره موضوعاتی که در دین ما ممنوع است و وجود ندارد، نمی‌خواهیم صحبت کنیم.
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/96033" target="_blank">📅 14:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96032">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIA6j3uresi62fibCutFT4KqJ4WiDo3sOh4FURF5kAKvRR30rXGXcuFKRalNpIefd08H-QcihNStJLb6xB7e3vSLsE2xO5BiZ_pZgDyMBmHzRjftojRW2-TwfT0daAe87P-0tCnii7ypVVIHsW-kddzsDheWHpFo0Yq2Kmxg0nPP9B-XUtvIwiOlBD_GZFa1tPq0TtmHxpSdYu_buzkiVD7akkka6jvSLKIVWH_bDob6WbyDlXWHIWI_rIVr0jknOryMKJCQkqr9HQcCrX5cvTA-iQvrT9RDcEWrb_CVnqvj9UFrHRM5vR8WN83rtR5wnfTkF5mgD8-2RATkc14e3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇪🇸
🇦🇷
پدری‌ستاره اسپانیا: دوست دارم در این جام با لیونل‌مسی روبه‌رو شوم و در نهایت پیراهن اسطوره را از وی بگیرم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/96032" target="_blank">📅 14:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96031">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21833a49a4.mp4?token=cuZYPZbkmE5ZLtaeYkG6Wx1U7eDyWoIWMR4vhDFcKStqxnvPxlQT0JWmoQrZBt0zWkVi7w3NdMri2zJeG3JD0Y3JHKCVBsmgtOzMI2HAhdk4GLC2rruFF0vwcyQMNwm29qkGYNClUDPI2yx2RpwhjquxJhNDBjCbKSTnkXYmi5yTdRkX28r-Qnpivh9y__hfkz6Fi0b6FjOXDqrEqxXeNRt47gkNqHBHQ9MooGDfgxCJ-kVzJ8X-0hUrVW32mfzo0QcsTlFTWNzWwO1-m1vc37Wamx8rj3PolrGRrTDxBl80JbzwCOH5y-8osBjpxnUmzZlnU_9Y48jTMPcKZ_zRiqeQxe-YDh0AfByHfW3-Ls0_mM7noli_BKhpN3CGwaZD-tLWqMpDrwp9Z1g9PLyBjjkNtDYKIi5-0DmZgremZfAGTQo_rmNn4AGwLZniWSofNzAlM5-Y_3wkU5FG9V0gxwBfF8nXnycnVdaeOl0TIVut-NbaSoFuKHbwxBQFvQyoiR1scVL-Owbh6mdrPae0-7SqnO9kKfm2xqo6Ck10t_sZ1o_6FoucVZETezECqm-N-yHCj4XqKlbdTQjoFwOkzrn4fieFcbTs2ThXS46hygkIrYsi-ouUhKPcskrxKT_S2z4r0jefPEryUm2O39P6tq91EGzHkHeJgwIX1BBTNK0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21833a49a4.mp4?token=cuZYPZbkmE5ZLtaeYkG6Wx1U7eDyWoIWMR4vhDFcKStqxnvPxlQT0JWmoQrZBt0zWkVi7w3NdMri2zJeG3JD0Y3JHKCVBsmgtOzMI2HAhdk4GLC2rruFF0vwcyQMNwm29qkGYNClUDPI2yx2RpwhjquxJhNDBjCbKSTnkXYmi5yTdRkX28r-Qnpivh9y__hfkz6Fi0b6FjOXDqrEqxXeNRt47gkNqHBHQ9MooGDfgxCJ-kVzJ8X-0hUrVW32mfzo0QcsTlFTWNzWwO1-m1vc37Wamx8rj3PolrGRrTDxBl80JbzwCOH5y-8osBjpxnUmzZlnU_9Y48jTMPcKZ_zRiqeQxe-YDh0AfByHfW3-Ls0_mM7noli_BKhpN3CGwaZD-tLWqMpDrwp9Z1g9PLyBjjkNtDYKIi5-0DmZgremZfAGTQo_rmNn4AGwLZniWSofNzAlM5-Y_3wkU5FG9V0gxwBfF8nXnycnVdaeOl0TIVut-NbaSoFuKHbwxBQFvQyoiR1scVL-Owbh6mdrPae0-7SqnO9kKfm2xqo6Ck10t_sZ1o_6FoucVZETezECqm-N-yHCj4XqKlbdTQjoFwOkzrn4fieFcbTs2ThXS46hygkIrYsi-ouUhKPcskrxKT_S2z4r0jefPEryUm2O39P6tq91EGzHkHeJgwIX1BBTNK0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
▶️
🏆
توضیحات هوادار ایرانی برای جایگاه‌های ۴ نفره و مخصوص جام‌جهانی به همراه امکاناتش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/96031" target="_blank">📅 13:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96030">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c892433e.mp4?token=d4SEZSumTzMsBEM8WDTCEJ6B0p7vKykrK57TR9cIXwHXeip391FqGAr-sKG0jUpozTjXGchOGtZqAhvh3b9UV00ElePYvmlwGhNw7p53Ei1F496Ofc9sM7vMBNr-igYd-Z1gd2-gotKgQL4mZg4JVkZvF9SOcDJDu9zbBTJe4NgP2V2z_3lfwKkMJoZ-9IXhNOVx2ag1fSva3e7zcGVX3hP68ou0X73G55fRlndYz0eblQHg7yITj2nfpSkn49ltFzaUtgCZYsHMsUvWUDTQqNGcD3VkChfxPtMuuThPFKVpQkJc4y2NMR5BI79SnSylLS55jcagPzRmkXnQ77WB3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c892433e.mp4?token=d4SEZSumTzMsBEM8WDTCEJ6B0p7vKykrK57TR9cIXwHXeip391FqGAr-sKG0jUpozTjXGchOGtZqAhvh3b9UV00ElePYvmlwGhNw7p53Ei1F496Ofc9sM7vMBNr-igYd-Z1gd2-gotKgQL4mZg4JVkZvF9SOcDJDu9zbBTJe4NgP2V2z_3lfwKkMJoZ-9IXhNOVx2ag1fSva3e7zcGVX3hP68ou0X73G55fRlndYz0eblQHg7yITj2nfpSkn49ltFzaUtgCZYsHMsUvWUDTQqNGcD3VkChfxPtMuuThPFKVpQkJc4y2NMR5BI79SnSylLS55jcagPzRmkXnQ77WB3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متن حماسی که در اتاق همه بازیکنان تیم ملی نصب شده است
🔹
در تاریخ فقط یک چیز می‌ماند، آیا ایران صعود کرد یا نه
🔹
چند روز دیگر هیچ‌کس از تعریف‌ها و تیترها حرف نمی‌زند، همه فقط می‌پرسند آیا ایران صعود کرد یا نه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/96030" target="_blank">📅 13:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96029">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkVzbrV5K8NKNwgh-Owa0TeODn151vwPEAGe57wYHokc7ndh9ZWlTKetR6JZa9tXe35W1dx57V2FBQkR7MECLf3k_U13PpukzL7GgnQgNiIRCt-VNzEqY5H85EEix0XZBKK9B2qd8t6y4D7R9yclUaNh4KINhWToPktd5k5tIBwiIDheEo-z4Ndq5w4y6Yp-QQDBBR-W0eU1G8YLG9_vnYJZw6Yy7npRW5HN77rp1CcdfOdbsLf2mIYhYkzqh9ON34bTlF-Ts2jSVshyh-c0vc59exS_BUlnZcz8QkiI9_WqSylBQZu4dL6Gh8-uk8sW_v6t2tsRbGOQOfi2Ysw4Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇬
🤩
💍
حسام‌حسن سرمربی تیم‌ملی مصر درباره حواشی بازی فردا با ایران: برای ما حضور یا عدم حضور اقلیت همجنس‌گرایان اهمیتی ندارد و فیفا اختیار دارد هر تصمیمی بخواهد بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/96029" target="_blank">📅 13:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96028">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEp68S5cqYMIVlA_EQSGXitBct8UeUVR4xjhgJzE5wFcOXuFv6djbzryKXT0jOuJFyWimVdiim0jAosWPsFPck2_dKQ6idxcmsFTaQjnVFuX38k0wRGwR2o0DX7zv1bR6UMNPproGpUhvR1OzP7VYpdH2HfkMegmTQ8GuO59xR5z-zp6UqgYQ6BBVu49WIDGhzLLWXSX0EUWTO3VMAka5ULC8uWTzLDw0_RAgsqWhve2bfCHCna-zoFwt-hRloApN5j_HciVSCq_w6N9Dop3ls1T7UZcaJ8rEiNaf3w-qAKG1JvJmVeqIcKDCn9KaP15B36jJ9WFrPizsQb025HsSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
لکیپ: مکسنس لاکروا ستاره تیم‌ملی فرانسه پس از جام‌جهانی با عقد قراردادی به ارزش ۵۵ میلیون یورو راهی چلسی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/96028" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96027">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sG6r_ZFNkURetAO7Of5r1SZZTn8wNXrpWL-0p048CbBSFe0KfJ1JFVcdQitzb5GSMHRQ3Pt5FgszlBK6CPwq6TLSI7UAKEZ2djH2akiO-6QjoKL3pK0YeN7kltCvtHfRFHcyu5nP4zBaoB014gXGMQSyYH5wsUJr5_m4uXRUa5n1JXmnXpeYThqpibk5zq0mqbWHypajD6F2cK3B2xIqzGfiJq_I3wvLCC06ap8xKGjKtLgjhdbFKEYIeSnlIlTlsqoeLW8UKSA1I-LvPgu18j9lAMcU7t7vd0Vro-6uW5rtGfbcJhIJerW4Ln7OqUJypb9iQRP5JMDK8iKdK0hwIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
تصویری که لامین‌یامال از زیدش منتشر کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/96027" target="_blank">📅 13:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96026">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8aae82768.mp4?token=P-KA8VLumyzat6SOndhpWP8wX0FAshP_IjMT0CXQ5LUCISwPvuQ1soLsx_WKGFR9-lDtwJHid8dZZU1FY94NUZiR0IMJ4L8DLj_nq9QpL2BVhJM8gVmEZOzxzCXm72zxwu3FTnHi8lvZb-UHSfZkxNMH9CPlLzPkXh3gmk1cHFB3w27UC2VFEiCouDw6wAz0qlbZ13cNF2SgBjJ-cAZkVLtJKnK2gQ2Ihc8WS9ctwEMWDDwI1YOI35SD4uv5nPjOXeNY7RhP4c8977AVx9lft9sO91zz0z_snF_Ng_kmqIlfWCkwXjZdJNaPmuf9skqq-wEgpS-n8DZWYmeRZt6BBk-kB3zkIY6apZVvJ56CKIxjIkFzY7uzwowJzLrF0Nfra1jlVog79CC6V9bri4TjGEj24Feqv-Ko7a50X65YMTgOy1tAa7lF3afzlRUrCCUUD9TNuFFC-Yf8oggEsHASLEmDQWS_9VBJmU5uUtzWOfcD_QXGFUd86QlnJ3kdtA3G6GsHFl0eLQMoaqmmBslQvvmPnLeHUsEkE-0zrCxkTTP_cQEEyaXO_D_g20S2svqATgao0C8_W2yxDTFBCii8VgBflZT7fgltQphubG-O5CyJCq_GdPshILOb22fKGv97VFeH2IlzQTog0fx6NelWZdwviGEnOSJ5__OlHdYGgb0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8aae82768.mp4?token=P-KA8VLumyzat6SOndhpWP8wX0FAshP_IjMT0CXQ5LUCISwPvuQ1soLsx_WKGFR9-lDtwJHid8dZZU1FY94NUZiR0IMJ4L8DLj_nq9QpL2BVhJM8gVmEZOzxzCXm72zxwu3FTnHi8lvZb-UHSfZkxNMH9CPlLzPkXh3gmk1cHFB3w27UC2VFEiCouDw6wAz0qlbZ13cNF2SgBjJ-cAZkVLtJKnK2gQ2Ihc8WS9ctwEMWDDwI1YOI35SD4uv5nPjOXeNY7RhP4c8977AVx9lft9sO91zz0z_snF_Ng_kmqIlfWCkwXjZdJNaPmuf9skqq-wEgpS-n8DZWYmeRZt6BBk-kB3zkIY6apZVvJ56CKIxjIkFzY7uzwowJzLrF0Nfra1jlVog79CC6V9bri4TjGEj24Feqv-Ko7a50X65YMTgOy1tAa7lF3afzlRUrCCUUD9TNuFFC-Yf8oggEsHASLEmDQWS_9VBJmU5uUtzWOfcD_QXGFUd86QlnJ3kdtA3G6GsHFl0eLQMoaqmmBslQvvmPnLeHUsEkE-0zrCxkTTP_cQEEyaXO_D_g20S2svqATgao0C8_W2yxDTFBCii8VgBflZT7fgltQphubG-O5CyJCq_GdPshILOb22fKGv97VFeH2IlzQTog0fx6NelWZdwviGEnOSJ5__OlHdYGgb0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🏆
یه خانم‌ایرانی خواننده خارج‌نشین برای جام‌جهانی موزیک‌ویدیو ساخته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/96026" target="_blank">📅 13:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96025">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u1W1nJAwDjVMnJqmOnKNJJMVpRr_eNKMvmfqvPzVytxeQnNrQHwvQr-vJ4nDR5Df_Pd5ga1PYsX5PfsqrNsd2rRkHbXDUZ6qg2coi9E1qbLyIQwzkMmNGMJcNnXbkmenoONUbgbP2sFayprW6UNt6ziB5nuq3ya5mnQHPj6vnzhMUUqNFKP0riS6ZFPrkcAlVKe6X_xbvn7wdSXa528qU7onv4o4wsDOuaemwWz5HcUU5XaIPFLbb5RhxZ6zD-hfqW2ACxTkZVaZTGiAk4o0gWKNwUX_FdCqm-tUbVm_jh9-Co8EDUzqWriicB1k0d_95lAAgkaSv17QLU3bebHOXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💍
🇪🇬
🇮🇷
وضعیت‌سیاتل آستانه بازی مصر و ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/96025" target="_blank">📅 12:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96024">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53bad2b136.mp4?token=rgHAVoBA-S0F9Gm7ZgKDZelDXdbF0buUAsirth8AT9E418tHCsYCFjPhXAqEXhZvURKhIF5MrIx3HqavjSlBTSDbZZaUxmqfeZhYlqsjbVQSpYUJxjoo-8YQakdC4EBvKzmh104sAAGtuhBLXfSYUIWO8ufsEvJlMcJkqf83XoI8Zg6CjuWYOcXbs9upbqSIYowFuV1vGTmfZAYHFIO_Eoxe2n_PkyY8HgyX0nFMy-OrFTk-Mdc1bBndzVWZEDu-UQd8G7aZYdMvA5EVbCeNk_-bDjmvy7meahpVzT-efSW9WPh_G4_tz6GjPLhNNiVkdtTgs3dnMTZ3rSQj-ZvuLmx2J4MnLJVXoih53o71811jyWzxhi7_Ks0xesJuLIVElV5Zk_hODkZ0CMSx48T156CedSZGIu7zauQ0_Taij-1N6zre4JUWNUuG9LyjuLWzdvxubNUFsrA5p-VehynGJg_u0VAuWeC7GB2aKAhpxg3SkOHaQQ5Xjh9dETF9r5o1rtwK4AV1trZFHwSYISoR4XLIuXnKlzukys7r2lCQiV7wPlaWcKulFZX1O6mEu9ovJEvSIhUDmuCIC8tm7_aZs79cjBRBafHmPPYfNTEBaPr_cMp4sQpGoZJEnxgtJVujNDTgQlzCSsozrGsvmfD-aow7aOeFkNmsr_W9XrxjLHY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53bad2b136.mp4?token=rgHAVoBA-S0F9Gm7ZgKDZelDXdbF0buUAsirth8AT9E418tHCsYCFjPhXAqEXhZvURKhIF5MrIx3HqavjSlBTSDbZZaUxmqfeZhYlqsjbVQSpYUJxjoo-8YQakdC4EBvKzmh104sAAGtuhBLXfSYUIWO8ufsEvJlMcJkqf83XoI8Zg6CjuWYOcXbs9upbqSIYowFuV1vGTmfZAYHFIO_Eoxe2n_PkyY8HgyX0nFMy-OrFTk-Mdc1bBndzVWZEDu-UQd8G7aZYdMvA5EVbCeNk_-bDjmvy7meahpVzT-efSW9WPh_G4_tz6GjPLhNNiVkdtTgs3dnMTZ3rSQj-ZvuLmx2J4MnLJVXoih53o71811jyWzxhi7_Ks0xesJuLIVElV5Zk_hODkZ0CMSx48T156CedSZGIu7zauQ0_Taij-1N6zre4JUWNUuG9LyjuLWzdvxubNUFsrA5p-VehynGJg_u0VAuWeC7GB2aKAhpxg3SkOHaQQ5Xjh9dETF9r5o1rtwK4AV1trZFHwSYISoR4XLIuXnKlzukys7r2lCQiV7wPlaWcKulFZX1O6mEu9ovJEvSIhUDmuCIC8tm7_aZs79cjBRBafHmPPYfNTEBaPr_cMp4sQpGoZJEnxgtJVujNDTgQlzCSsozrGsvmfD-aow7aOeFkNmsr_W9XrxjLHY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇲🇽
مکزیکی‌ها وقتی ورزشگاه نمیرن اینجوری بازیو میبینن؛ غرق در عشق‌وحال و مستی
🚬
🚬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/96024" target="_blank">📅 12:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96023">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🔴
🟡
دیدار امروز پرسپولیس و چادرملو ساعت ۲۰:۳۰ آغاز خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/96023" target="_blank">📅 12:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96022">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b381fab19.mp4?token=UVtBevVlxEScRvucRYAAPXhhOb_a7foT0rDu1CnddRJguw-9yZ2Emt4A1TEB18-YSakvEYZI4AQkqSnaO5ii4Vb8VmJXhBsoeB41YRdbpIrg2tzw9AB_LwSCJCA7bSODWwGtvqxwHo5J020tCCAxdonPctMKyVaHe_dvCe6CLvYypGUP9AiPm8So1Pa6sdzPGAxUzrQ8qQC9hWswg1cUAAQbUgPF1_7v3t4GmODyfkJHY4rYgsagSPGiTaWgXIc2X6oZaZpYC7KRgoUi-3EkVkSlliRZTmLhnCkiSgCI4Mzy8gBoximQe-8JUCUW_NwzFSkzy5zd8K_G0-QmB-ikBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b381fab19.mp4?token=UVtBevVlxEScRvucRYAAPXhhOb_a7foT0rDu1CnddRJguw-9yZ2Emt4A1TEB18-YSakvEYZI4AQkqSnaO5ii4Vb8VmJXhBsoeB41YRdbpIrg2tzw9AB_LwSCJCA7bSODWwGtvqxwHo5J020tCCAxdonPctMKyVaHe_dvCe6CLvYypGUP9AiPm8So1Pa6sdzPGAxUzrQ8qQC9hWswg1cUAAQbUgPF1_7v3t4GmODyfkJHY4rYgsagSPGiTaWgXIc2X6oZaZpYC7KRgoUi-3EkVkSlliRZTmLhnCkiSgCI4Mzy8gBoximQe-8JUCUW_NwzFSkzy5zd8K_G0-QmB-ikBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
✨
▶️
همه عمر می‌توانم کنار کروس بازی کنم
مدافع سابق تیم ملی آلمان و بایرن مونیخ بهترین بازیکن تاریخ این کشور، و یک هم‌تیمی برای همیشه را انتخاب می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/96022" target="_blank">📅 12:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96021">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZAQAplyZ05lsTXk8rs1wFtz3auI9xOjXaF-3dNQOeowUqkNtqFecor6_NjVrM7o7q95GCyrU4jVuGVXNVv96-tumPACxBPVtBS-BQXmWAtnVFFfZnsg64nhBBloZarD07P5J7iEvWZrnMKpsiD34RgEy4TXjoo-ApRKP71R5TyJ2YPVJDiWIOsSmAzooIDi38wiyKKCjsgf0JzMWBW2Z-3TmGbK_eKAiCfVOz1NOLkj2fhRtnvZYNAyyXG2yIItqhvp0X310-BX6s5EDkJ74r_5nY3R9Kk-dfrPIkRsmritsf-ByU4V_KaKkePoSk60mxmM87rc_A3T-SIsFBfxng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
#فوووری
؛ آرسنال اولین پیشنهاد خود را برای جذب برونو گیمارش به نیوکاسل ارائه کرد. نیوکاسل به تیم‌های خواهان ستاره برزیلی گفته که این بازیکن فروشی نخواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/96021" target="_blank">📅 12:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96020">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871d57299e.mp4?token=Ven-pOhFASDEIVi-1D-D93K2TbUYSKHT68yqCYBFyAsDikxYHFPbP2_W9h8naJAFXsb15aHnF-J7HYGHeLghiUVTHNrex_UMjYMAIxsIKUhDil24OOTfRJd7SHasjkw2E-Q0CDhyd5rtaZ0mhNiixPgkh4HvwSQg73BIvLSzRjA8B1CrfA_-i7bsKXbPVLLsFNqkG2Fe3L3-7zHyS3gZhS010LPoQHVMJSzuSSCD21o74SVJP0ULsMeQmDTSDs7ewIbYgRVjdDDt6T59MBrYNwV5B3exqKv0bUhNMQ-hnEE59lhoA15UywNT9MOTp3JyBcJwLK7AaWJvqZchQTf_bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871d57299e.mp4?token=Ven-pOhFASDEIVi-1D-D93K2TbUYSKHT68yqCYBFyAsDikxYHFPbP2_W9h8naJAFXsb15aHnF-J7HYGHeLghiUVTHNrex_UMjYMAIxsIKUhDil24OOTfRJd7SHasjkw2E-Q0CDhyd5rtaZ0mhNiixPgkh4HvwSQg73BIvLSzRjA8B1CrfA_-i7bsKXbPVLLsFNqkG2Fe3L3-7zHyS3gZhS010LPoQHVMJSzuSSCD21o74SVJP0ULsMeQmDTSDs7ewIbYgRVjdDDt6T59MBrYNwV5B3exqKv0bUhNMQ-hnEE59lhoA15UywNT9MOTp3JyBcJwLK7AaWJvqZchQTf_bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
معمولی‌ترین هوادار برزیل جلو اسکاتلند:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/96020" target="_blank">📅 12:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96019">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AT5PEGW699VoqQNwqMw3R1_f2IH_j8ug7UOtzy_e85wcieo5C9vDcn73LHCZrvEwJ00_nH5U0-jH6LYv7c095VmsQMvUjLO9zkkKgHTBc46am85oE96Rp2rwvdjU1wdo8fvP0OVNmx7lZWr3HAk3ui4_9-csnKUYRUAzBJDzntljpVeki3kV32loU9tdeVqeP8D5YukSZtqwZfCOivmhnEf3Kw5RHnYsuKQ3LdzUcfGDATOp0v8riB775YY1phh5s2kamVAHJ5iAotuaoEnXzhJloXg7Omx0u_7okdezjz18s5D4y5dyBGRC9YZwzEpFw3v1VsCUaQzF-4TOlQxAhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🏆
🇪🇨
پس از برتری تاریخ مقابل آلمان و با دستور رئیس جمهور اکوادور، امروز در سراسر این کشور تعطیلی اعلام شد تا مردم به جشن و شادی بپردازند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/96019" target="_blank">📅 11:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96018">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plu3nMe8uRoTqpY9DpMshLTqOB_pGCMo3LGfihwJ9b9jjFlXrgOyXkxqFFxriJGAx0MODTYDuTu_wq-51Nx71PM3-_FG-ciAbOiaLMNi3QiBeU-CmzgcDRydQRsZI6qMu9vw5XHhof4rCohytk4Snjm1J4JDW3Pi4LZ3TzdraMQ5-NQ6kkgV1l2ckxrQ_p7D7Zi1xEDvG0-ixnoR9c7E6K-Z9cV-LXlz6jxSJez8ITQELOUFHgPnW935H4E25xFW0VQTodoBzjUlgRUKHxR6XYBLEM2gST_2EH2Ts0uNIA31JDf8_gyWye8vV4g6ELf-yI-8bX4FTY8I8ykbDzyL0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇺🇾
هرج و مرج و درگیری در اردوگاه اروگوئه پیش از دیدار با اسپانیا.
🔴
اختلافاتی بین مربی مارسلو بیلسا و بازیکنان وجود دارد. تعدادی از بازیکنان از جمله [والورده، اوگارتی، بنتانکور] درخواست کردند به صورت خصوصی با مربی صحبت کنند تا به او بگویند سبک تمرینات و بازی‌ها را نمی‌پسندند.
‼️
بازیکنان از شدت تمرینات شکایت کردند که باعث مصدومیت برخی از هم‌تیمی‌هایشان شده است.
❌
بازیکنان همچنین درخواست خاصی از مربی داشتند که فردا مقابل اسپانیا با دفاع پایین بازی کنند و روی حملات ضدحمله‌ای تمرکز کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/96018" target="_blank">📅 11:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96017">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9ab104e91.mp4?token=hYvUiaY8dttUmofq1Nsdw0nw7JDDOoHdxk9xOrm3w5bnSgw1LN9lvp07zww7MhLMI7saAwtV1q31X4-ZUDBSjDS9rX5qACDU5bsmNq1npzIeevys07XuwARQzt43a-hpi2WXN9geqOCcW_af2vCCeQAEg7ytjUNWkwtezq_GM3X07bD48qLlP3-mnm1oshyHVDV8ej97xvNwTQT0nxJOVvbBg6aZ0bGvkJlPjBFysVNCtXwzfN73vUb7zz-8fw8iDV9Yguuw8u61euhzQPjH_lthZpc63xiIxkcYkbDV-Z7A5K4J3zWPlJ8VOWbCj-zuo4jyebEXd-6_7HY6kHo2RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9ab104e91.mp4?token=hYvUiaY8dttUmofq1Nsdw0nw7JDDOoHdxk9xOrm3w5bnSgw1LN9lvp07zww7MhLMI7saAwtV1q31X4-ZUDBSjDS9rX5qACDU5bsmNq1npzIeevys07XuwARQzt43a-hpi2WXN9geqOCcW_af2vCCeQAEg7ytjUNWkwtezq_GM3X07bD48qLlP3-mnm1oshyHVDV8ej97xvNwTQT0nxJOVvbBg6aZ0bGvkJlPjBFysVNCtXwzfN73vUb7zz-8fw8iDV9Yguuw8u61euhzQPjH_lthZpc63xiIxkcYkbDV-Z7A5K4J3zWPlJ8VOWbCj-zuo4jyebEXd-6_7HY6kHo2RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🎙
💥
امنیت و آرامش با حضور نویر
‌
خصوصیات مهم مانوئل نویر از زبان ژروم بواتنگ دروازه‌بانی که کیفیت کافی برای بازی در جلوی زمین را هم دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/96017" target="_blank">📅 11:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96016">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeU78BNokm3-OtzdF9O6tnw9Q9vcwSqfJBD9VWnpZPo7k3kKYbv5AwiXuuiatSJ_CWSCb3SY0RE8MdkNow6sU_m8aw_Cb85IJT9F_ai0EfbypwzdaMQsxSpKqBn2Q_UncfYhoT1sboH7_8FzZPWg1IyithUXlWHGcD0Kn9w2bj5CtbblGw5Ydgcg2GSbH6ZLei0yHiYMc9zSRuz1yU4v8AHwTgBkMcpcwZPF-xnjwn0Fu-YePVek9DaTpm5pRbIiSQ3uNHLsqPCVj1gHGPuFxLN2sCiGhL7bSSiq-P88GqA1unSm6yBg87gzPjjDSLoFYMO8trtu8-We8RVf8SKS_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📊
🏆
🏆
تیم‌های آسیایی با بیشترین حضور در مراحل حذفی جام جهانی به طور کلی  :
‏5 بار —
🇯🇵
ژاپن.
👑
‏4 بار —
🇰🇷
کره جنوبی
‏3 بار —
🇦🇺
استرالیا
‏1 بار —
🇸🇦
عربستان سعودی
‏1 بار —
🇰🇵
کره شمالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/96016" target="_blank">📅 11:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96015">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOBD8DVgCTr9tmEyQEItyE5h6bxf5ak9JrIGIDbKT3Ywuqhxr18BPGkAAeYlIbBKiY8SzG9ktakeIqEnKQyPLv3AMLpQD1d7-xe_d8KuTxt96xgkRBZvCC14XqRwpLqSsMTgluaOCuiAzMrtYZJozigxkcvxABvpnk483ipnMKDHfErbbRU8cjwT_-kw2rftC3ck-aZ7X3kLtZBgHngL3812uczCVvG9J4q8rh_9V0OgjBC4-0u2vyQv_YQKnILGoFaifOMXGfLtZKirIsFLW4fuW-avUpm96x59s_YlaOFmY-iWvI2zAw1EqW5C2bwVRCAleX20oovbM6xD5xx0Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇬
🇮🇷
پوستر فدراسیون فوتبال ایران برای دیدار صبح فردا مقابل تیم‌ملی مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/96015" target="_blank">📅 11:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96014">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd157c98e3.mp4?token=jB7gn4-mlUWefLBMZSF6_G3-5at5yur6X8lFkP1euB7rHQSwPL9bQKRBGoxwDRF73dUiRAf8f208Lyntplu5dcyz4Mt7EfRsTnZ_5aLv6f2zmjyCbGR3rZ13_ujzTBkEUQMYFUOeTfdP34ISjXiP7ZebBzdxoQw0ND6qfa6wYD7AM4k7cLaFLmwdXY0Hyy_zOJCkZHjcGln65gSazdw1hmyfjWMAimMPvlBM5628sdkL5dMWgFqEnz8C5M-Qu4mUwJNl6ZtpJcxCan2fAnj20UbkubKbKWsio5pFfjG3bv8KSwMETOawLjrwGWGtx12yNaWMwKgHvU58QyZ1CAiXKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd157c98e3.mp4?token=jB7gn4-mlUWefLBMZSF6_G3-5at5yur6X8lFkP1euB7rHQSwPL9bQKRBGoxwDRF73dUiRAf8f208Lyntplu5dcyz4Mt7EfRsTnZ_5aLv6f2zmjyCbGR3rZ13_ujzTBkEUQMYFUOeTfdP34ISjXiP7ZebBzdxoQw0ND6qfa6wYD7AM4k7cLaFLmwdXY0Hyy_zOJCkZHjcGln65gSazdw1hmyfjWMAimMPvlBM5628sdkL5dMWgFqEnz8C5M-Qu4mUwJNl6ZtpJcxCan2fAnj20UbkubKbKWsio5pFfjG3bv8KSwMETOawLjrwGWGtx12yNaWMwKgHvU58QyZ1CAiXKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇫🇷
مصرف یک چیز عجیب قبل مسابقات جام‌جهانی توسط ستاره تیم‌ملی فرانسه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/96014" target="_blank">📅 11:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96013">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOdRvGsKL8x5F-mqCgJa7Ierg54sbclvXDbbQBkeX0kdoIdLfRHqIyFKnwA7dNc_IgVcZYNs2mPHygEMpuy4BUNYpIgSSTxQBM6oidKRB8mFLL_qtboeyOzbEHhl-pWwgUGJrFHnjEJT4V4iwnAMTjtURFaF0SfqI23748A6Xg-JSqpgjSX9c-RL8gGlC_QHfNU0iy6r9_g3pQZTY6Z_NlA0qRAFsTomrPTSEFLJ8ajy_UUUsy-dh2EmGZSlbMJ7vRezGmxN3WB5Wo0PLQBeEKZJe82DTmljOv0cp7CfmnH0lebW7DT5VL_SQRU5kuCCcQ5l7Dn0BL4g09eIWVsefg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تقابل دیدنیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/96013" target="_blank">📅 11:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96012">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4G1JPifdgKg5epkJqxxJx1T1J5-OxOHIYfoyt-1bFb2NWiGsG7BBPptq-wtG4xSsfFfPt8VlUnvug9wNP1PlmrDpk6FSxMpb9iS5Tq3rchAZRhHvnGHZ5L8HwWVv8_acfQpCoky-UAy9XvhTRtgl6AdGbxaP2CSsLzsqel8QN8ZZqnvaSwcB8KtDDkY2Yj0rm7yP0iqtznm4qncEbkrhwo6KgFqYSBvpwlFCXL2hvTrDLlr1pD7TR97lycHGS14TYyRzxLkeSxE2w3_Aqkj2rL9g_TRUj9HA0LRoJRKe9vys97C-bnpJejTn66Bcv2koQGVssvzlrcqyNLMJKIPeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
تکلیف دو تا از مهم‌ترین بازیای این مرحله جام‌جهانی مشخص شد:
🇧🇷
برزیل - ژاپن
🇯🇵
🇳🇱
هلند - مراکش
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/96012" target="_blank">📅 10:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96011">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83cfa0a889.mp4?token=oXqv7x21StJ_8P1CWogZjk6ZfME11DcoeeF23yvC5G4QI69_1w-gEhXWwa2DNLMUiosn-8R8_tSwDJUSld8i0pIWAFKhCqReuWzE55GXf3MJFfsUAk0fQXKAMYjhtAfLv_D_J2G5uX3sghmI85c9pJe0ZOHSibOzUeoIi9hu2MT4VAO-U-UNKrmTnDY0NQ7VGYS5VHn44eDOQYzK3OoWIAm-swW9F1YjqinE8_O1ATT4D6UDUtbkR0p8F0hwTSq8zkhq_N-jRhNSP-zOK47jkmiTGRbLlKvOe4px62s7GqRx49AjM4tinTAy2zW9kqnp28udAFPao6c-EKE-eeMoNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83cfa0a889.mp4?token=oXqv7x21StJ_8P1CWogZjk6ZfME11DcoeeF23yvC5G4QI69_1w-gEhXWwa2DNLMUiosn-8R8_tSwDJUSld8i0pIWAFKhCqReuWzE55GXf3MJFfsUAk0fQXKAMYjhtAfLv_D_J2G5uX3sghmI85c9pJe0ZOHSibOzUeoIi9hu2MT4VAO-U-UNKrmTnDY0NQ7VGYS5VHn44eDOQYzK3OoWIAm-swW9F1YjqinE8_O1ATT4D6UDUtbkR0p8F0hwTSq8zkhq_N-jRhNSP-zOK47jkmiTGRbLlKvOe4px62s7GqRx49AjM4tinTAy2zW9kqnp28udAFPao6c-EKE-eeMoNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به‌مناسبت حواشی بازی ایران و مصر این صحبت سمی مرتضی فنونی‌زاده رو بشنویم
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/96011" target="_blank">📅 10:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96010">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89114baf09.mp4?token=EH_r4hDuP5pzqP7UZlJDrtx_8aB4wVMHBHMGlwCK-_qNBeZSZUrKOWSKM-Fj0DyYkk0n25u76WF4ZmcWP98SkuEPk2qYjAdMO3cciDwM1hmesp1sajB3Nd6PZTIjjND3XD_smpPQ_kco9X8TZSJEZ2vmHnP6HImOMHdSVukI56PCT7fzg5BysUsBl1TQaGSNKg6uOXR2cvNfKcZ_eonpngsndZe9EKPtbIpsRYw2A0XrrEQgebEx1HCKZ4CDPTSNWZeO5fh35iIWnuCmpVoNmFmtXkm1jwc6moN60jFLC1cyqwEwLQ-n190vCjuhcXsha8EVG9P0M6LN__VuReEObA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89114baf09.mp4?token=EH_r4hDuP5pzqP7UZlJDrtx_8aB4wVMHBHMGlwCK-_qNBeZSZUrKOWSKM-Fj0DyYkk0n25u76WF4ZmcWP98SkuEPk2qYjAdMO3cciDwM1hmesp1sajB3Nd6PZTIjjND3XD_smpPQ_kco9X8TZSJEZ2vmHnP6HImOMHdSVukI56PCT7fzg5BysUsBl1TQaGSNKg6uOXR2cvNfKcZ_eonpngsndZe9EKPtbIpsRYw2A0XrrEQgebEx1HCKZ4CDPTSNWZeO5fh35iIWnuCmpVoNmFmtXkm1jwc6moN60jFLC1cyqwEwLQ-n190vCjuhcXsha8EVG9P0M6LN__VuReEObA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
🇳🇱
دیشب مکزیکی‌ها به هوادار هلند یه حال اساسی دادن
😂
😂
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/96010" target="_blank">📅 10:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96007">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YvWKSb-jJQ6DCkvMadd-iTv-ze9bIuNeRw6EvYIXz0l7J5hurtDueDq3hoDFkutdi5TirqOgy8d866B8CVJaDhawaPeMCmKj6g9yl9R0GOq5j0DGt0eiS7IYVTpZWGqXLBUi1FrArAOtotMrNdgPFmwscOlGY3QIVaXKYSKyvTHTXajmfujg1Bx1kTR-XCiLtC67vRCApbOZd-gxZWgpT2TabYxbe35eDgy6RGB19UjQl7nTMSn7ZuqL4LIjQ9mY5jdCdc50PwZKDNVRk67SKnhJehQw_wAUOHrABGhf006DWF1rXkpa3-6tzXAEU0cWf3_Odt7AwQckGeqL6gyLAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phVierVWSZv5l4OgpW3LTobKxZdPmHwe-gTz9ICUT0QeL2imlcXnySrCBEBiWbcGAoyDmg2Cp-FusXcbXELsMzdGb9bfLNnC0bG7WKqkzq-kY7dc1-JRWHd1AqwxdJa8P26eeuKwmQaFrfs__nTXdnB4HSGGOxE_Q-WWhYEPzINKu0aqKXet8VjkTBshsPCgO91uxiHBcPYY-KiGD6fFgfi2gYUVkz9TTao-CwqK1gut-6-4a0RvU2jGSuLHCcKyNaXtzCa0WajrrCU0bYfWQS1jX1U954SlKK0TyGCyLpIJoIX56sXeI3lg9KBfOxT-XGyjuXHggBnk0uzmTOA--g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KuH7Mxzn5XTIqDCcoQhn0IWeiiWxPhkuLatEmabwPdrYQxqh5QLQKCLXRHP4x-lLdxHs-I5ub400NaB-sSuV8EIzAIZ0XD4UNmDh9iNj6hsTYKNbz4iDkDZUG5ZiL0ihH43oqhWF86eQtSwhhjqBIFLpHaexrTLitEKcAeEuaGYpliEATAsDCx3LBCL6VXZ1Yx6ZViMAMXgB8xPSvlPayzdmdZIiiNoNaxX-tHn6FNI51j1l_Ew0YP6ONViItEva56OAOuNV4-o-vjcn1qouUdebC_upJByH2WVnLL308jNmVEcIXY_CKCDCLa6TFq6DltfAYxUIpv61HHe_s56bdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر چی از کیوت بودن فنای مکزیک بگیم بازم کمه
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/96007" target="_blank">📅 09:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96004">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
ویدیویی عجیب دیروز از درگیری سر گرفتن یه ظرف نذری تو شهر همدان
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/96004" target="_blank">📅 09:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96003">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d6d7c284a.mp4?token=LBGjz2DNn0NTy97dyLziGihaY8TuVAA34yT9Rjk0Ah6h7CxI8z-yWmK8ifNzW21qNjkAbvxGfmvJiA125EV4l_bd3TLOK_TS5HtyFsQJ6qNl-yWdjXIpjNgz_LSzZiu4taqne47isyPaB_YsGQa79iZkIaH5G-LI0p3ri3K6FY0nmaEmnxMf5zz_fzpsaxjvHHPxkMW2S30RdOiQ5PaEe6A-Y0jiQ4y4IZQ_Xosa6t81YBrSbQiYVXs9fwXW06yL59RRs7L4KopY4p_YqguyG8Y2wEsJrKblYdjtHKbZs7ddb9BpRMBrF5Ofiz2o6FbpOJZ57QGY16DzR57i304v1FgsFQ8QLlVzLyxGizEtRs3XPFJYCNM-zu4Z27gpP-KynNvqNX_vOOWgZ3EINHCP-Id1qf07h6QUCUbxQKDZKAixb_p_Fx9C4kAm2R3ENhlDNG0XoS-6kJxy1cPU-X5qSbQhOUyT9mITEHzfO5eP5LcHgEoodJ-CIPmtGp4NH86-Amf8O7vbdPhwYVo6u9YNufgsBj7NxR1_Yk75Da9W6qF4MuVzSYnCSphtJ-FjXEPZCqtj_rAOooDWBl-H2nfIRAyNPmF5lIGnJ3xu_yNPNqY_nDozOasDZa6vVFR1tSCN6RbyQHrD0iTft_37vD8t2WSKCe4Y69GSlPB6H_MKAT0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d6d7c284a.mp4?token=LBGjz2DNn0NTy97dyLziGihaY8TuVAA34yT9Rjk0Ah6h7CxI8z-yWmK8ifNzW21qNjkAbvxGfmvJiA125EV4l_bd3TLOK_TS5HtyFsQJ6qNl-yWdjXIpjNgz_LSzZiu4taqne47isyPaB_YsGQa79iZkIaH5G-LI0p3ri3K6FY0nmaEmnxMf5zz_fzpsaxjvHHPxkMW2S30RdOiQ5PaEe6A-Y0jiQ4y4IZQ_Xosa6t81YBrSbQiYVXs9fwXW06yL59RRs7L4KopY4p_YqguyG8Y2wEsJrKblYdjtHKbZs7ddb9BpRMBrF5Ofiz2o6FbpOJZ57QGY16DzR57i304v1FgsFQ8QLlVzLyxGizEtRs3XPFJYCNM-zu4Z27gpP-KynNvqNX_vOOWgZ3EINHCP-Id1qf07h6QUCUbxQKDZKAixb_p_Fx9C4kAm2R3ENhlDNG0XoS-6kJxy1cPU-X5qSbQhOUyT9mITEHzfO5eP5LcHgEoodJ-CIPmtGp4NH86-Amf8O7vbdPhwYVo6u9YNufgsBj7NxR1_Yk75Da9W6qF4MuVzSYnCSphtJ-FjXEPZCqtj_rAOooDWBl-H2nfIRAyNPmF5lIGnJ3xu_yNPNqY_nDozOasDZa6vVFR1tSCN6RbyQHrD0iTft_37vD8t2WSKCe4Y69GSlPB6H_MKAT0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
🇩🇪
زندگی باورنکردنی دنیز اونداف
سرگذشت عجیب ستاره تیم ملی آلمان در جام جهانی ۲۰۲۶ که با شادی‌اش، اصالت خود را با افتخار به دنیا اعلام کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/96003" target="_blank">📅 09:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96002">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAmhUr5tX3fI7mD-HAhB4_yDPa3gCSplH6V-0HOFxGeFGmUiiz49hYLFDO-5WFHVIVs9MouJaP1d-UuKhPaeiO7li1x46uzq0C6Owu3PjRLxT_GnS6JtNL35Vk3TFsoy-t6h7TgOPC-8uNnGOU8VhrdnhYzPtZ9vDcSHdEwiKgL7UWidABuj-6S45a_XSJD4MHJSJosTwGrvW3X6CAxngSNShO6zN5Ee1nw9NfEALRgd6pUew6no9c8wOQUrJIAfwb6Pa8AvPJdrIUmRlbNQk09J17SXPysEboeQOPYOLdqqMIo0SscsJqhL2R75ON56BZdMxFmKy2I7LYN507Q1XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
💥
ترکیب‌احتمالی فصل‌آینده بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/96002" target="_blank">📅 09:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95999">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQup4afvtsZf8wAQXXSLkl5whAbCOENXKUIAsnZacIv1YCPwcks71Am0XHq2HEwhUhPKzJrhGR2TnxooS_PtOVeFrDfoZ2N1Av5__BZHmKZYBINb1tQQbO-pIQkPz13fhLYVSGLz3wmUsMUEkFwPaJi-X6o2RDfzxwe4WbPGYbN9_1Kj0tHjuZm6-Q7j6LFDwcnzsIP5omBJZvEzF6xK5AK9aBc-xlSkGlLR8-HNJXUDT-HNIcA-UvZ9o8aB8lAbqJ0AIre0GuaGrm7U_lSohjbpnB6HcO_S_KX2BMHHyB11sSH9IXXMU9a138Z9DejAew0x8ePvgvqhGdUfS67VYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ofxzi7gW_YbstvTNO-cDcd5FKTjDhpjarwuYthf5xYmjm2xBKL5nQGqkHLYUrwSM2wLK1_eqktKkDfQe7c0eXn3WLYXy8QLoi49vQ1_1vTSmFZ3Ex7MBL7MM9jAfmLxmy-r9HQS7rlS2pRByZHaNLiZuVHIyrjBU7umJ0d0SJ-Dv3MB92afEMwmwMNQ0JYQZ-MhKlJYsmi1LxnQWuN7sCaihZwEh6pT0u2_hd0eQ4FS9DkPgdn2v2oBxoOtufP6X2KgoU9TNy4O_0caqdVjW9YuxFTvW5rqWvk3Wq1GFfphm8kna8XraSZj3ViLBLKNJq7Qimuw2XbuUzkKiBajJXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JFeIG2TVrGN9iumTYDEYA821FEvjMmjqPv8W0WiB8VnxqulXraOJl_9oPGfeSy79k9G8Xa4y-DAmfZSXpIYELmIUrw0-6-2UnfrB67Spl7bIVZ0WPfFc8ILhCpL0NTXHpa3GcXriZt9Z1WzMNNc86hazJtutVK_TuionIpruGqu0EIyUIJliv7aqws4kDi_arq0MnYcYfyn7khge2V9GiTiICTn61rEHfHUrQ30ojcxvRLqS_A5BlPlW6qwJ7xjE9bCDhEOwfLQOEeKXYcSf5mbRPo_pa7KinyTLeCueglykajxQBloGSSXhGcEUfACGx8rd7WWudONuyny-WABwvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ای خار جبر جغرافیایی رو
🫣
🫣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/95999" target="_blank">📅 08:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95998">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYYRFkXfUqmHU6TykxUV7rJcrspbZ686yb20938lNxP870hZtw6j1D9m38lu7Lo6VdRyJJ7_PnsKQ6CLSleKlsP4Vzj-kZZbP2kpN6d2LkQISvftejaXHI3tmOZ9YHWeuH-wdxeHfYsioEGEL1VaOnNuJjTnZqMAuJKAeBCjhNCu0I7EjDbHJa_iIH8I1Ldss2JzQ0ouKZWFKP6I-01beQ-jiJlZ_I_dOICPi7Be6eHHFtV_uyDF90R-3vtm1WDN8tzqPVF4UnnbWJKTNs7gDNCNIbzR_FANBW4XUfjqqQfe2yqzvZqyLqqLHznx5KsyDZ5EzxOzGYpeUgPIIQQYpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
تیم‌های راه‌یافته به مرحله حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/95998" target="_blank">📅 07:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95997">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIlh3sboKLda6ykzgVfC8lw9agz4ih5XGHyg7sJEkoZLLKce86pAm6Y4HCc9wwJ4o8KewRTDUSTjUOpFliGK39nzCXwUyfTTId1vAYSRani9y4ApDD3cnCsMSX5FJmhuYfyG9lLNNAQPqAd-dVj5PiBMWWgO7BVZMp4HTcyfjGIuVqONqWyjCV4bkt4Zby-ti8_C7EHaHMTsBPa_3s_li4KJhMWf4QOiOr0Xnt8oEhZVpHX7c8NC4hy-OuLc_3Maic2qmLljAG8thvjgEfRlKtyHzDpTSaF5wezme-qysM34SKKy4HVrEYfN8m_IDCC_DALGk-y8RO0dcxj2rkdztQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
جدول بهترین تیم‌های سوم مسابقات؛ سه تیم اول تصویر مجوز مرحله بعدی را کسب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/95997" target="_blank">📅 07:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95996">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqROEhxMICGZsGpooG0zrOZYomB5o3w8GsPzOwHIDUPvo_VBSAleV1ibq021x6gx9qZ_EKYHryMzWcXc2_6jooKvZ_tNdD-CmHcVdxdWRJ1DedaMLk9dIWQfJHo7tXxxPACkSz22jJ5-0DOn4KodWkf4P4fYthYzKyIn2uwvGf8yTaUl9yy9-XjlNYA_tkO51f2eeSVCC3DwLsDpgv-XyWf3IZY7BdR23ApQNwA9DvfyjtZhe69fkR5Ta7C9BOYU-K0IT91uueZN2snx_Hk3PNMD8kpiWnrkc6d1kViMouM7GGS3pvnBQ0n83Rhb44HRLRtC402VKrVUwAQibA6TuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
جدول گروه D در پایان مرحله گروهی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/95996" target="_blank">📅 07:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95995">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aO4mFXbaj49toZU1wQCDQXkXI3iKyALD1t6MzuPr_fFDejBCBm_zWRw5xAx171rXwTkcwyOtd3mpu-yA5mFGmZ6FcUVfffhDG5zqrcVBPrDY5EbaazEzOSqgNYbYmpX8gP5gO3edeBXzYeo1onlMUeBbk7vvqZflYHu9cJCk1UWiK1N3zGLR0JyuA-fNC38cU-F1yrOHq4d374btC_qqgzIc4hK0ZTyTGhXacHu9lY3-atNj3Atv6E6uYIrjhZsmch28T2F0ivu9aXJbK5WZyWCuzAhgvVI21G1rEQdu-JlgDCzZB8G3V0K2Sl5dQzBy6-Dunj32EDmBAuSUHmP-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
نمودار مراحل حذفی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/95995" target="_blank">📅 07:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95994">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLAKEekG1-UDCNN7_5OySEr5OanzGgH52AmVlzj36ur1fy6iN9xxaimPm3CKsbgs7kn_ZhOoYef0hwPaoIYiWwADP-S4u-rURQuAHNrslSCm1oUuqhabmLaHtqRL1SQnQ4N4nj--nKRYAs4I3NATZtJC-IlZ5ToTrnD-ZGUvccdP9q_YevmM2tD52PuJEbIgq3zPsS5R9hvAlQsQnmObHM5ZVCrDxlSc4wSEJiv9XudJfSrzEP-cC-B08zzbWj85Cedsm_YoPPjaGZz71EZeoqeZhDvJia4uaam4C4WdXY2w7EMY5aiXP3O-cxPcE0cCS5WWGGQhL8e0-7kqd9j4Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
تیم‌ملی ترکیه در آخرین بازی خود در جام‌جهانی مقابل آمریکا صدرنشین به برتری رسید و با کسب دو باخت و یک برد از مسابقات کنار رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/95994" target="_blank">📅 07:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95993">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
🏆
پایان‌بازی گروه D جام‌جهانی
🇺🇸
آمریکا
2️⃣
3️⃣
ترکیه
🇹🇷
🇦🇺
استرالیا
0️⃣
0️⃣
پاراگوئه
🇵🇾
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95993" target="_blank">📅 07:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95992">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
🏆
پایان‌بازی گروه D جام‌جهانی
🇺🇸
آمریکا
2️⃣
3️⃣
ترکیه
🇹🇷
🇦🇺
استرالیا
0️⃣
0️⃣
پاراگوئه
🇵🇾
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95992" target="_blank">📅 07:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95991">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dwp5yQcxvxGigWKD1r4RDTDy_EAi2YvNLRcRj0O71OZE1a06BKZtG__w_BbY22kcOhrzwrStN4Hz-CZ6yqacHkmXfMBSM2VZpZf4asSaGIxeY3m_iLyC-iptOjiIpGF4rPlbjwW74e9RehZcPwdozS65I4YlyQgSPicKRPRyvu-2xc5sabkzLIPVAa9iVmnTE_ikO8NKkGxwsppqvi0_lAg4LedQ6zCdNALSCUiJaeTULxeQ8QBfEL6JHdcMDF6QTM9bed_pVJCZiQQGndWl2w5mQCVnDlTeI2CmGlGGr7DobPV11fJ7fo3vD-f8M5RAZVJeGHARaG8A_sCQuT8r7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت قاره آمریکا مقابل اروپا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/95991" target="_blank">📅 07:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95990">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8XdaNouNdGFUNnWJOWFx1E8brk7nkRzCST-5qMY6uq-rjsUNTevJhJz-ocBf-uPCOj9qPuDoZ1kDA4k57UY9EjamXxRlg8SCK0DjOpmSSO6pcismsIBaMXOtWTF_LSOlKoKRq3VsqgrN5Yu6sQNQDHt5kr1gUiusRFm0SGown8PReq6zK6hDzeWRmt7l79Yi4rlhZx4YC1ph6ZPtacvWHqMUf99TUngkJSa5VjIzy10folEn7U-zXDqeK6lxWMMOLUleyRgGprtGOmn1kSj3gv_2gT1dQ9wvAYqP4oR2lNXbMtn0QbHjuYxw2rzbXPvHfd_mSwp2GoASye_zxx1Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینا رو ببین خدا وکیلی
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95990" target="_blank">📅 07:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95989">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a795f9561.mp4?token=ergp4jr8keX_se8i3bl-I5WTxbNnMN03FRPbMFBJ0gz6oSG97vIncp-fFXZ3j-dF3eI0eWwhbdjnwgl3quurSJ7lnBpDe9spHWCt15x3fueRZ2r0Ox3-abPHMuXz2XM40ZZiL-e0gsDYMfTV1_ajjc7aiqaqv4ZU4aB7Ehq8Vtqr2W0WKdRlcGG_1Tv1Epx_2MNTsDiJ8XWyIHBdczs_cWzxQEZQUnYoOaiv1N4u4GptraIB2CjedOqbgHHkW__yGG-2oUjyt3pTU6K-TGu79ZYm0e6v_4mCY0H0uOHlvR0OZEwhKK4rphiY9B2O5vvfQmS5WRqGn0jNlBeNEPBDcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a795f9561.mp4?token=ergp4jr8keX_se8i3bl-I5WTxbNnMN03FRPbMFBJ0gz6oSG97vIncp-fFXZ3j-dF3eI0eWwhbdjnwgl3quurSJ7lnBpDe9spHWCt15x3fueRZ2r0Ox3-abPHMuXz2XM40ZZiL-e0gsDYMfTV1_ajjc7aiqaqv4ZU4aB7Ehq8Vtqr2W0WKdRlcGG_1Tv1Epx_2MNTsDiJ8XWyIHBdczs_cWzxQEZQUnYoOaiv1N4u4GptraIB2CjedOqbgHHkW__yGG-2oUjyt3pTU6K-TGu79ZYm0e6v_4mCY0H0uOHlvR0OZEwhKK4rphiY9B2O5vvfQmS5WRqGn0jNlBeNEPBDcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپر تقه آمریکا به ترکیه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/95989" target="_blank">📅 06:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95988">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">چه فلک زده ایه ترکیه
😂
😂</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95988" target="_blank">📅 06:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95987">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گلللللل دوم آمریکا</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/95987" target="_blank">📅 06:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95986">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80336e0918.mp4?token=a7DCoQhM-CLeN1Ib8cNdq9rcbHARcFziKVFqMvFzXZHg3pDVNlLG6XUZWE0bZPDpUL8uQcAALvvzKH__3_QNJef2ITUT6KOPILkMygIi_W_itJrDVnxDMO5vYc-pg5ju3BMK0vsFysY1P4ackUnRy6p1T-lT8TdzFXl71e3EDC0a3t6bg-xkBAZFFeiLxy9ws5wJLFhVV5RhYP6x_pRH5K14lpBcQA2V8oxAZ2bFACQ0Oea8Rj7Ebo-sNurorr94zyaWmcA1SCyEAOSTAMbHxfbyBvmZ1ZcYVgHCCiEbOxWqmCzyD-NnjzyPzTB9btJdLWxmH-ZektHxkxOVEDP13A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80336e0918.mp4?token=a7DCoQhM-CLeN1Ib8cNdq9rcbHARcFziKVFqMvFzXZHg3pDVNlLG6XUZWE0bZPDpUL8uQcAALvvzKH__3_QNJef2ITUT6KOPILkMygIi_W_itJrDVnxDMO5vYc-pg5ju3BMK0vsFysY1P4ackUnRy6p1T-lT8TdzFXl71e3EDC0a3t6bg-xkBAZFFeiLxy9ws5wJLFhVV5RhYP6x_pRH5K14lpBcQA2V8oxAZ2bFACQ0Oea8Rj7Ebo-sNurorr94zyaWmcA1SCyEAOSTAMbHxfbyBvmZ1ZcYVgHCCiEbOxWqmCzyD-NnjzyPzTB9btJdLWxmH-ZektHxkxOVEDP13A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم ترکیه به آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/95986" target="_blank">📅 06:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95985">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ai9W8XEhBUV_SBeMMMZHY7JO0wUwjyNOrK9tyEUPqxGF3ZAKScmn3JynvREyNDV_FHx6D1phgMerRl11jd-UgqrzdQd8U4tWuGmK7SnftPgz-VL0KNwwqB1UvvfGMBm1TN274WEmFFakPRu4c45Pw49oLpC30U4DP1Q7ZAm4HD3bD6gHtPn-1GOcPTuhmSHbKzgJ0vCH1N93Rob4xdiGuy8DSRh4CXrlxK0lQiWm7SSF9fkSGKeYqyXVr41dCu1HqTb39ax9tQhftW09zrU1h_A1dzmn1cMlyXKzaNMWPtI8-m3FLxUB-OwYRX5Suf-iblX6excZ8n-xFXyc9F5d9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تایلر دردن در حال تماشای بازی آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/95985" target="_blank">📅 05:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95984">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba51004b9.mp4?token=i6_ctgNSTqcZR4lS7VXpBIClDvYxvRQkraWhXXy8oJcUHio1Ud8IkXmA2_BFkhNR648DHGPFiOKUmFwemTNhHkPp2SfQcXA-IlvTzrece3C4IMLCDwKIBsJ4EZ52v2ZJLoTM-6GfKDZxZIDoq3_BBd37h1xVjRlMf6bvoGPYFPivoOfcOJNTC3nD19q8XqcT17DYEc2ddWqH7uzv8wkD51iaJl1iTH_4-njwg2xOFn0RpjU9sEf5FlvdCG_kzQMdQZCzSODkYEwV8POvLI1W0d5mNDTyxRY17CwS5OZUvpISitJO80WqVivMoPKWpK-5vGrG4rFarPQGKrK42EfTbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba51004b9.mp4?token=i6_ctgNSTqcZR4lS7VXpBIClDvYxvRQkraWhXXy8oJcUHio1Ud8IkXmA2_BFkhNR648DHGPFiOKUmFwemTNhHkPp2SfQcXA-IlvTzrece3C4IMLCDwKIBsJ4EZ52v2ZJLoTM-6GfKDZxZIDoq3_BBd37h1xVjRlMf6bvoGPYFPivoOfcOJNTC3nD19q8XqcT17DYEc2ddWqH7uzv8wkD51iaJl1iTH_4-njwg2xOFn0RpjU9sEf5FlvdCG_kzQMdQZCzSODkYEwV8POvLI1W0d5mNDTyxRY17CwS5OZUvpISitJO80WqVivMoPKWpK-5vGrG4rFarPQGKrK42EfTbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
گل اول آمریکا به ترکیه توسط تراستی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/95984" target="_blank">📅 05:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95983">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72cd71076b.mp4?token=jyOVnuCm4hsFg4H-r4rOQFGEynPKyPICywP5-ALAIt-6JJT_bwXXLuZoQfGMc0bT6ckMcpAh--WkBAzSHHimVbMlnttNnrLHsPOoTuNQlfWenLv_UFBMAv7x-ZN_2YcdTpm-CsAZP25WjPr08JBKbb5D_Wd0zk8Se4F_n8TJRW39Xt6w1knx69APPBDY0v1-DJFPkK0bKKyrRZ0GPn2-6urLmUu3_LfUbDoFhv8iwCJn4H4rfYxLN-lCkgzP56vdkik-nPyttK6yneS6T7Jn2rVtqcE4w-J1Yg8kBfbhzmFhlfs8v4HdXok5qWS5oY21me-nFRspNLZUuQKYdNyp2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72cd71076b.mp4?token=jyOVnuCm4hsFg4H-r4rOQFGEynPKyPICywP5-ALAIt-6JJT_bwXXLuZoQfGMc0bT6ckMcpAh--WkBAzSHHimVbMlnttNnrLHsPOoTuNQlfWenLv_UFBMAv7x-ZN_2YcdTpm-CsAZP25WjPr08JBKbb5D_Wd0zk8Se4F_n8TJRW39Xt6w1knx69APPBDY0v1-DJFPkK0bKKyrRZ0GPn2-6urLmUu3_LfUbDoFhv8iwCJn4H4rfYxLN-lCkgzP56vdkik-nPyttK6yneS6T7Jn2rVtqcE4w-J1Yg8kBfbhzmFhlfs8v4HdXok5qWS5oY21me-nFRspNLZUuQKYdNyp2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
گل اول آمریکا به ترکیه توسط تراستی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/95983" target="_blank">📅 05:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95982">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPuA71DilijM7caK2jMeZX_eybS_ceiSV9PGKGBgC2C84-7YiwcXzasI7DQfOmEa_krC7ja8iJ8ZzlNt2yUypFbX-xY3NDbScNZrBsxHvLlNLOnvgt0m9oT2CdpEPLdJiOya_vqN2e3ptWD_t7xIeGrP408ExaYOOX0eUZRvUzZtDb63nuttFOUfFsFDG57GSuA9CzIArosSLxqoOTMH8GKrjjG7-2EF-To5lOJg13i3Ze3XH1Q1SyX5xDMfEW9xxGRwmkLZ7BxR7eVDMW1NBETJTdoN4vxNfnxtXQcVHgqsyeWi2Y1S720fTPoq3GMJ0IdY9qfSOqJ3xvMrxTNcSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
جدول فعلی برترین تیم‌های سوم مرحله گروهی جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95982" target="_blank">📅 05:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95981">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0ZoaUZEOppC9RqnFr4uQHTIUUOgW0zG4AczsNVV_Tr1bsMUMTPr-390SHLYRjfAOmATi4WxawFbPEWovPgs09AYGVj9HPVb09kVO9NLn-xqAkTSwgUqohqgguNpZPyoc0BcGy88-zVzBjReY-RneTx8RdnKQRkEOn5UGUh1wVfK7bCB32Nlugt8MPyJOpvErF93ZL8oB3QqRK2VjmMbse6Q97sqPWIdwfArVIS378txlIucECq_Nfks9H-mTOQlY0_eEiTGGC91h1PTY7ZPfhHcN42M9kuv73LBUllD-SaoF_jhF_zerNlblvI7KqQfIB0U9pxn8O1weW-iT85qIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین حضور تیم‌های آسیایی در مرحله حذفی جام جهانی:
5 بار —  ژاپن
4 بار —  کره جنوبی
3 بار —  استرالیا
1 بار —  عربستان سعودی
1 بار —  کره شمالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/95981" target="_blank">📅 05:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95980">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pez5rYNjRk2KesZKgGjf90jjLVeM_xKCHgAUZIymfEgARovMzEaX04OEeBLKSkoAYYVCuBw6d1-UxPGbqBjQFeCzqacNWO7a_nbZ6ZYSprAF0XIP2-YHY0n1FgDpF7t1tZz0M7ha9meNvXKqA4fFGGyuiwlUydMTMo5CZ0CDuq8seb8uZxPcnM3-H-_-gRqvEAboTQHEHHzhWUquaotnNR6GMnm3pfhs7kl5Q_A__3GF774t5iSiPCjPI7nnkWLD2G3araSkk9zDzFIPySh1cXgclIdJkn-K8tBPc5c5hV8DXqrSnXs-qX1LhqummPhSfxQI8f1PwOPEwJkS3_fDyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🌎
بازیکنان رئال مادرید با 9 گل‌زده بیشترین گل را بین دیگر باشگاه های جهان در جام جهانی ۲۰۲۶ زده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/95980" target="_blank">📅 04:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95979">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jf6SP-vwOCUzDQUeTSsegrB1dSpcm1TBE5LqvodfIqqsg_E7RuBioVle_kynm_KQLrfbLDY87gvu-wDrh-R937-UNLvOCQlSfiwAIZwe88Sjd6CfO4LYdMtg_m13ky8Dt8slVTnFFkVStRO0hE4wchdEHhk19WwhQzcvKVFd0glEyu4lWt9dDCh0SF-6b525LaC2xHHpLU7IDGaMHfqrGIggKbQuUyVcHU4Uw8_ow5kfD_N8flyF22UJHvwXlBFOyvCcIJcwB-Tcsn7BpQidwiVs2cvuCvbCWLhIdbLzqNU_E1C1EtJSit-hmxtFS6U3TLWlSZaF5nKmQMgsl_WKJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه F جام جهانی 2026 پس از پایان مرحله گروهی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/95979" target="_blank">📅 04:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95978">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIwf_GUG3qU0OybCOgUdSylyC0_6qbFmNfqzkPv6T2op2vNCJwXAgIul5MVCCTQcosf4Z6qz79BHy1jEWSZyljm3wixvdlrc3rco-TEB_3ySXA18_9yiAutN8-WZ2RhEwpgSVbcy-NaNSNWljExXjshU53zXiXM8E78qA1csWfseuSxS_ADGLHBfQYXEeDhY16fgwMZTHLh5R07KN_ZKpITkGbRmtBcz-PUElElkeLiW5Mk4ZU6FmKe3kjPXrf7OGZrbxZoEOMMdo_2jkb7mEQHxBWj4n-TJktTH4C-jN-6_ij_i4UHOWfOBWlo4Hx8GXoJgOUsaQ4zPZA01WwweMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
تکلیف دو تا از مهم‌ترین بازیای این مرحله جام‌جهانی مشخص شد:
🇧🇷
برزیل - ژاپن
🇯🇵
🇳🇱
هلند - مراکش
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/95978" target="_blank">📅 04:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95977">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETeBojntr2W4s-MoerO-VRiCFspN6LV_EpZWXujSOcRltTV-I76b_4BErdvLBbnwHXK6voCS95jvc48thwlFMgcI8xpC0BJ59OsweIqG_SpMDs33WGalV8J9uIGJk2ELAJgPntdsVl9YPHFvPwbxxLIMsd4ybBr142OoTs6CUf-33ZLnI90_wcsojS5fXdFgmbl18QAbGBUfQEVfVit6gLwsrZJtokumzICnk7k3YF210RyrWCCIK0c2quGsi4i1WyYt-GCoNThoba9GRBq5FMGv3Pni8A4Wt2rlQPYcNnTaPEg4H0A9rXBfSYkrb_63U-_ldYgopdOpkjn1AqCiPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | سوئد دست در دست هلند و ژاپن صعود کرد!
🇸🇪
سوئد 1 -
🇯🇵
ژاپن 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/95977" target="_blank">📅 04:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95976">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzESAYOHAvaeaQxXfjNLqpdkOfWF2KBdp7HTOnvkcoJjtFZ7nJXTbkX_lGP-m0n0V1EjTJxkpoWBeGuzCDf3UdPEBFSw_FCXpOzm_FnGApYFQJKuhmoEbH11E6FD-6LSkevoU9rGyAEsh9FDyqQKfOd0Ja0f7rPAt1VJ6hGEZqyqzCfPHqD7zjUQQhi9AUVFp96H2_x-ReUALLU78yoqBIyHB2_Pwqhr2dkb0_f3_PavgYWcEQEIV8CObh92570sPROoKBRdXPYtKmPMc2C4MQ2Z5608UEdqcohzz61zJRgwH5mFpAYsxxS6VwTiNeLyyeEjyxZXjXlQBurd0_LfqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | زیبا مثل لاله‌های نارنجی؛ تیم کومان احتمالا حرف‌های مهمی برای گفتن دارد
.
🇳🇱
هلند 3 -
🇹🇳
تونس 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/95976" target="_blank">📅 04:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95974">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qj6x6myutTPxWVBSBgZh9Wh70ZvFibGkFyrESTCHfpbNRu5Comuper4j9F9RZw31NhKVZ0wpSudHgtZzQfc1uLWWW09ss8RcWmEoTOF-jpqXk_7dnEg5Dje3OhzwOVXnhjpEUkReXgHO5t-T0mPLTbJMQYt1gLA7GDnPTpHkG_4bZfJ_GlJq2VWF6vJSI_sEugD2AjzAzTDiCPZH6qgpw5hRpCOd3X08-N_W7n0RNUXGrOJvx5Nt5uKEcxJEsaEU-gNTWe4nVO5iGvIvI2IqYUyG-lfJDJR_g4YMFbwqb7qDoV9F73yTmGhhaRkYwvUwppSf1wbw5H8W-G_QnaQlDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v95LBZwOIg8gaoT18ayJZwYLEtRZZUV-bx0hvdClwzW6UGKlVUARvyYpIbq1dXcBsPvkaEulbNjiDyoqlRJrydtzh89b_mJHvE6P5wUlhmEpcrJMfrp2BE662GzrvhtR7VTu9-K-tXWuTJ1-UPzt4lhC2qXx2At1xe2VwOgZ3pxxZCxqYjJR6ia5TwZxaZfy6kHrOWh-vKQILB8g8iJfKPBcogbqF8KyV1RDK4ZDyF8oTax70JW14Vh0n5OyRvsGXOwrEOf1mgSuZTUI6NuZ8LuFYCI40AGacjtuF4vHCUHb8dKn-bUxuYkM12lX2hD6X-Q6Lo1LjHxSUKVclSFMgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
🇺🇸
ترکیب رسمی ترکیه و آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/95974" target="_blank">📅 04:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95972">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlhUr0uCV-BCfDsqn_1-w3nXp4HPE47Lp3Njqcg4tkgp9PiOceom2ghxSeLKFgh43VNNWkoGIDIAqHBJG3w3dgmH9KxFIBYd3j8Jmx_YJuD-jrukE61fzNVm53gSjnNSA_Ur6c9Q4MMe3qRZ2zpbaOC2DDYXZ9On6UNkyHdvozvHRECJKZyxNoJQxhu_BY2fK7gDn-dbITVNxFyV3pE-ljIo2r7vcoBwSXjDub5ZBqhWvshW5LfumA6UiNnYdqxW-h98dBZKBUSlFxN0Hc9Tey9cUYyey2LJuY7HvYSM4asqKcrLfXaT4PDBEuzS2_Fwm7mVxt98SPmmwOVkR9EDEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CpwZHb-202GkVKsKs3pNhLUXfQZZU1HKvwI4uNfx2OoZGRNVOaez9wERUobCCXQMfapDvMu8Lr8WSwRboEDh-Mrwq2NdhRDOldtLWehPLuEkK414c8Hh2aUXjlhBaJ55cAO_dH1bX8HQBO384b1YB9rsyhwP_WiItifTfCRpLR4nT88xBRMWWLSRu3ZBPj_cyGhPFThZHwSFfV9MCPf63blO2L5n4B1tFwUKnTqFWugUdsDmu6_HyHDh3-coDcbtavGtejECoGug-m1MB5xCxU4a_qr1fVNe3ZLWr4PKijbzKtE3Rx9B7mKUJTeKpzLOrfiCGBJ9w3ckD0IVgtO_oQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇺
🇵🇾
ترکیب رسمی پاراگوئه و استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/95972" target="_blank">📅 04:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95971">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b281416ebf.mp4?token=CqmJz9SSn9A6gJbUGrRB71tVsOgKc453PL1TI81V2qGSwLOXB4W8TW127pma9yiZ5GK2LmTWsmEcBFPr29hgMThOGEc1RfPkAmfjj2m4N02Zb6jtb1C44R5m1ypO-gWcYa-jW1j4qBJBZkKFoDv9HL_rNyklJWoTIUL1nSYMKuYsEQJ3S2_oTsM63gydbZnHKQseLRALwbj5nPH3S2pc4R1IqTmGhFYj_DvP6eZcHmErb7vDfoTk8-8aboaSD5a-eFN0FgR-orMTksBuva39NrPecSihuQK9m1zyFu3LT6gac2yNOwYxA_jMolPyAN58m6xziG9B66RE8BE8PWvf9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b281416ebf.mp4?token=CqmJz9SSn9A6gJbUGrRB71tVsOgKc453PL1TI81V2qGSwLOXB4W8TW127pma9yiZ5GK2LmTWsmEcBFPr29hgMThOGEc1RfPkAmfjj2m4N02Zb6jtb1C44R5m1ypO-gWcYa-jW1j4qBJBZkKFoDv9HL_rNyklJWoTIUL1nSYMKuYsEQJ3S2_oTsM63gydbZnHKQseLRALwbj5nPH3S2pc4R1IqTmGhFYj_DvP6eZcHmErb7vDfoTk8-8aboaSD5a-eFN0FgR-orMTksBuva39NrPecSihuQK9m1zyFu3LT6gac2yNOwYxA_jMolPyAN58m6xziG9B66RE8BE8PWvf9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گللللل اول تونس به هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/95971" target="_blank">📅 04:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95970">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac282eb0c.mp4?token=TpNfaX-VswD3t8AHOqtvc-XqcQV2-BchAnR5NkDml6xmPhCtCgix_4Vp02-xsskO-4bKhz8UhW7IMIMmr2eP9cihqX4cDBTVB4LDWODqlbSnZJzRF7K5S0CVHXGBZvA_10GFXAX1iPXpDPo-7NRHPMhA2SeM4xANEgDrA741dQZRvjaY2GE3qdah4K0YbX18EDcIP0ppYvr4sTdXgI7T3b2XuEgKIFR2DNIiUSWWpTYz44vRcefVozWYPftGnmMF00BZQKLXu4uzBvSJmjxnSsvUFvhnmhyrytwJ9w1nBCo_Lpq9VlgAp_vmJos0fFdVilAB1Niu7XoUeHkP1-bH2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac282eb0c.mp4?token=TpNfaX-VswD3t8AHOqtvc-XqcQV2-BchAnR5NkDml6xmPhCtCgix_4Vp02-xsskO-4bKhz8UhW7IMIMmr2eP9cihqX4cDBTVB4LDWODqlbSnZJzRF7K5S0CVHXGBZvA_10GFXAX1iPXpDPo-7NRHPMhA2SeM4xANEgDrA741dQZRvjaY2GE3qdah4K0YbX18EDcIP0ppYvr4sTdXgI7T3b2XuEgKIFR2DNIiUSWWpTYz44vRcefVozWYPftGnmMF00BZQKLXu4uzBvSJmjxnSsvUFvhnmhyrytwJ9w1nBCo_Lpq9VlgAp_vmJos0fFdVilAB1Niu7XoUeHkP1-bH2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان نیمه اول بازیهای همزمان
🇳🇱
هلند 2 -
🇹🇳
تونس 0
🇯🇵
ژاپن 0 -
🇸🇪
سوئد 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/95970" target="_blank">📅 04:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95966">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nup9UzP5pUqP7Bi1Sn3F2vxAJSl7sQiQlgMo6oGCrNHlnR5tVMotz27gGg1ouTCC03c18WhGIDreA46gtzhM9BJkP2iij9R0Eqm80R346ivP3i0cN_9ZkH-CFiNSQGbQksNS75PvXBRNNdFBkls_BmoN0iRJTcywGln74i50u5hCyTtCHeZBMss3AdP6yUG0F0lxbNId-0bnsaAo1gSvCf5YA-RvUT-FoYPouosIIZ26ktUnGxKDtWWofzpnJ5uRTgXV0-QbDXw9tZVhTToJZ6Oh0oI-OiRmf-g_mGOwLt8w716jXenHfWGoA7KL72X-ZvVLGaS57Vze9w35oF8KVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cP8GT97xwdwfXz673bFxa5Sij3NbDL-Al8LPSd6_CO6bWdmEjbKHV1owAIMvmlYl_Ggge7-rL0bl62WR3o94PevjYhyMm-uFB4Uytdf2Ashz4fvDVU3DhDSFWxNptD7PlLmxjv6xuWmQB2sRlaM--GaJTrc9MiQQbxNYERXUGhvWTHC4dhdjqj9uRTePzffusw13idD3Gj1M3m6Mbx_nbTs1lRjEpjL6KHUe0a7HYcpF_cQGQXEDaHUJl8rr0_GRAm7BNTus2-HBs4-zf-G1zRA86bgj6HzHhyqzXC3eD5cSUkzouQKnT8xjUdqMcJK_n7_29vu9hj9gjUyJd4IuwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXKubBtRIPwtIqqZuPuFJMhnH7GdFj3y9OoQs56QGh_nDozc6VO3FDLeTmCOoYyfCkNth5NVXoWR5wjjWqFsmfvSTDIz48wsDT6Yky8Kqzx4iv9D86T__uLYYPre2Up6Ekp7CgY_ekKnqhGMgOcX1N5FkwbLh-OxvWHPcHcaVJDywOL9-Kadwx7aiXCVq9bPqna0tG0szFVEbLRamupjqJkYBi6fNgIa8gbeVScsRjVqTpHHmKwSbuWD4nMaHUh0mtG2uGSx74aZP15Ty7vfpvm991NAjHjwQvHm4dx22YmAKfGOk7BZpTlDkIV1_LXrxV9L_HSdKzWP3t_NwTc1hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aKwLqvuHiKuxmGqH59C9Vfp3xyGC-D491KeFFVE6XSMAHrwKHjDa9SP-jcMecyoifL8PEPk6RFY9LGfSlPDKqqFqS___6_6RJOMSuUsRigUW7B1P14ijX5qoqyb3MXHxWLnVjUq1f_9k1EB_hbBnLUB9TbcH3NHx1GAOTypDZdjkgoEqhDXTru7Zwh4dFt7BcR7Sfs9Y74-kwFzg1OKktTHewZs4F0rnMSbx5VW_kMzovpJMvfb1fFbp-QQWI0jqP05e919Q9enmZgy_DBkzrPFv8qq1WZTp7j1FptsRo6XFJomAvo4YTeWghRpPiyVDpHWRGVP9QvZznFImB-mVdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اندریک برای احترام به زیدی تو بازیای جام‌جهانی یه چسب زخم دور انگشتش میپیچه تا نماد حلقه ازدواج باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/95966" target="_blank">📅 03:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95965">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پایان نیمه اول بازیهای همزمان
🇳🇱
هلند 2 -
🇹🇳
تونس 0
🇯🇵
ژاپن 0 -
🇸🇪
سوئد 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/95965" target="_blank">📅 03:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95964">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPmnC7hXq4dI_lfC7nYB0-LeHA0y71umw-Fa48xnZcdw2MzjFRfKuvpkuK53LusNVXm30iMCwNlWbTwwClRRwiBU21cHvWcRLh2-z3k6CAc8z7PQ70_tjgDfbFM7P734db4xHs9u4wPYO2Dnwo6ZeP3mKpnqWBw3Z4kK1X-KfSmNbXhzjntqzIiFOUTcxUKwm9mkZyFXTUYa91OLzguhK8THhqdiHozEFMFYn3RJRbNlAVDHDN0s4BcUUo7xUYXtne2QTmhh0iZvlSCpkMQDKgDwrXE81pJl2eLBM53PzpxTWv1-SklSQD8ufo3vQqdG93JHwLyNLWwMIW7_ZDKiMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رتبه برزیل تو گروه خودش در جام جهانی تو 44 سال اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/95964" target="_blank">📅 03:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95963">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIbVGpoJuTNYoLN2y0qxR0pxkzjaIb5nAOBhK1OgiK3xxj2p8mplMKuyaT6V_-MAveSv0n6Q9kJo6VAUe2tw3ah4zADRqfLYJ1hU6i2USqzAlCmJJzT8mCZZhWEoPItECj-mKVbT41XrpqZIZHQNOV-CD_J7tzqOgkCUMMdh2aybcbWrkp49MwcGItcKTG05mWgDUD3ksLdUThDur2yvIj-muhgHBA_Wajj9TKaz1nC-suQkZ0JFnxhFKpb4pbUnbvAWNyFRE7Kr2GbfGvSKhWGqFgTAQSDaz5S0H-JmkZDXaljRm5YNKf-sISVOmcQeKKb_wNz_RGwuZUYUKZ_pQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدونم طرفدار کدوم تیمه ولی نباید از دستش بدید
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/95963" target="_blank">📅 02:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95962">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a48b42c7dc.mp4?token=YXajA9-oI-OQ56BYXfmQBISZSA0HtmnBRyOSFpIz1fVVgdM9IFHM3coIJDoyXZ4TwetpqrBoFgqOS6iLIMvs7fNPfqzOPcXTyZx_pYjOLsHAo6jyOC4VHBIRrD6pJyj6dvRxAhm6yVyazMbKy2lAIh8qd8WteuIS_SYq9sQcRXU8BhvGUtcDd-QnJd5_8I-niuCumDA58J-mOYC9-0TD2rYxhZ_48CUTlX3x2MGZfFlMVBAvk7iFzelTipsbiWyweXTkK612eDzEPEQ8WxnvFBAYrWMDlGjPILirP9R1XeBlSa35tYSOF6SMl64sWoVVUYyBAsvntq47meY6GQarmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a48b42c7dc.mp4?token=YXajA9-oI-OQ56BYXfmQBISZSA0HtmnBRyOSFpIz1fVVgdM9IFHM3coIJDoyXZ4TwetpqrBoFgqOS6iLIMvs7fNPfqzOPcXTyZx_pYjOLsHAo6jyOC4VHBIRrD6pJyj6dvRxAhm6yVyazMbKy2lAIh8qd8WteuIS_SYq9sQcRXU8BhvGUtcDd-QnJd5_8I-niuCumDA58J-mOYC9-0TD2rYxhZ_48CUTlX3x2MGZfFlMVBAvk7iFzelTipsbiWyweXTkK612eDzEPEQ8WxnvFBAYrWMDlGjPILirP9R1XeBlSa35tYSOF6SMl64sWoVVUYyBAsvntq47meY6GQarmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم هلند به تونس توسط بروبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/95962" target="_blank">📅 02:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95961">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3Ufvix3evbGLAtDkOTFS8M3MRqggEEoVklYljvRtHns2686tcbWFNCMxXIn1yebSGtvK1lehNKzJsZR6JxVRVpXvSPagYIpchosLiPKa5AHt--G-kYifvQsyrnGaotBORT3cgDLjvZIiMQuwWmQQ2rGBJFTo-AZ8s7JZKfNWhSHfub89MQ-UkbQVcqHuXcjGFfLnrWaMhkFm8SbLYx8pA3RszbwHjN1sOemYComwF-C_8Ob--Fe2B2G4rG6cee4IYUo37zFzmDSBlHZExHJB1ISkOzidv6TOpfaEJYwrGTEVq_BPzpMT1ZT5KCKiEiwa0kCpz5ZkhGa_l5SVxKdyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوادارای ژاپن تو استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/95961" target="_blank">📅 02:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95960">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf81f3272d.mp4?token=KtkzYSleQREE5vvc3DQ7Hb_uC6uoJkzeABjx4iOAi660i0Q3wrkjx-NDKB-bvE6ZgLLGwa5fjYkp2K0Nmr6v8_uRiOmGPTgkuY7vW9cSMQEF7qrkQVxIWhj2zbNGgmICS2F1-E_wWZ2_m-UVfw5AFUMoEbAe1VT5YF4aWBYS9adw64aJfi50d31opBn-OmMcTIhRFSIZ2gCUgMfQvUyX-R2zU1AistH5_rDdwUQemYGVCBUHfZOONPPpXuoXjsJhMA4Ca5YYtxRuB9tZlTSrqpfBgrdvP-oPWhyKy-_CAElK8RaZGDrBK1zFDg556yD8f-xrlTmncpvPApa20dyOvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf81f3272d.mp4?token=KtkzYSleQREE5vvc3DQ7Hb_uC6uoJkzeABjx4iOAi660i0Q3wrkjx-NDKB-bvE6ZgLLGwa5fjYkp2K0Nmr6v8_uRiOmGPTgkuY7vW9cSMQEF7qrkQVxIWhj2zbNGgmICS2F1-E_wWZ2_m-UVfw5AFUMoEbAe1VT5YF4aWBYS9adw64aJfi50d31opBn-OmMcTIhRFSIZ2gCUgMfQvUyX-R2zU1AistH5_rDdwUQemYGVCBUHfZOONPPpXuoXjsJhMA4Ca5YYtxRuB9tZlTSrqpfBgrdvP-oPWhyKy-_CAElK8RaZGDrBK1zFDg556yD8f-xrlTmncpvPApa20dyOvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول هلند به تونس توسط اسخیری (گل‌به‌خودی)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/95960" target="_blank">📅 02:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95959">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">هلند دومی هم زد</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/95959" target="_blank">📅 02:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95958">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">هلند دقیقه 2 زد</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/95958" target="_blank">📅 02:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95957">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
📊
🏆
آپدیت تیم‌های برتر سوم جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/95957" target="_blank">📅 02:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95956">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hl0c1S5T5c-cXSUzslmUvijz3yewJC1Uoia31Ahm6cXj0dBA2ilIlX46nWxfB-EdltDbFV-B8PZ8QX7nPDgxDtino39QUwGOOFvDEAk_jD6VFfODXZxx3dFTjOhAhpsXzVDzrGNRryLGhLwN2toYFWtijJBjCraofmUm8t6uAWLZaWtvLPwQ9L0el1Mv-5xAqpsx1_lTzNby0a5P-PhAWbkIRe543-0tUBIhDYZj5d81vZrn7PvpT7sFZZAI3QjepmnJEPYJgVhq36nBW1BcaqSxguag4bZ3zljmOfJsihGHrzhqp-_mfXAQ2L1i8r3t3QHegcGd6ncdPLW9mgA79A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آپدیت تیم‌های برتر سوم جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95956" target="_blank">📅 02:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95955">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wm6BZjAqTT4Bt1Vv9fekkUd4G8FfEru1hSEyxuW-wmlkUXi_tyeId9m-AkQMrTWY9SxEQXSHbYTVXAnK30zwivumB74eL2-Sn3dNYwEnJoyyqVFv6s-m2SwKMujx1LDUqPUygRnG5F-E2w6MOjIW727yDDXbhNjO_RaiuQxrN-mbsGBwg0UD0GJ0O8DTct-RF1IcGV954MlTUZ54n7aVBnGXqaby-Gvg6ZHbDUaiPM3X-6nlURTBr5tF5Z2GoFMeqoWiO4cqZgERo9mE-yJBFr48cAofaAd0sqNOgSJoRO9j-j1RQ1VGX9BTI9ZxvvhBljCoh25mMU0son4QLYgC_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌های که تاکنون صعودشان به مرحله بعدی رقابت‌ها قطعی شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/95955" target="_blank">📅 01:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95953">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F66iKEw6oF79UNeS7YJnDZcWYxggygiIcjkKhFxrOuFS5FZlVwykDFJVx6Ou56ZgpH5XBJ0m2pxO2n3zwdl_lnuzo-o5DWp6t9SOcnMt69TJz7MzlzFmvlL4OOPHO8LxVkj6-3YTa4pr85_3Qdn_o27yzLq6bXbHfjbceZ6NIhnRpfh8uLSYL7clAYqhxM2C9R9MibhrtJ3eEtmm4EeLGpHumVrmPLA3LDQJC4rCXxH-yxX9fjGq5wy-CsyxTkwOGJZQcGTboYeWs9ZIOF5msOZgcHGU3PyvD_osIRjM0-lFTljSNKXXjQC0mqqp8ZXWMatLmklac5qMf8omim6B0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKvyWThGC1g_44UZm0ogYAuFAkXRIXuOdkBoIkB5CjZfqaQ_hGA_7FN8uwsjEs6oZHM_GnIc1b77wYNNt5ghc8EHc2-zGcxxfKItlPANIE_2puyRquVZ0xijv1bVZXtn9bHkc35Mjg_QiZy-ZSKDSUBq9gAUhd_-QSPKtJ-wiaFOtjEBuowi-YC4PaDnDXfExbsKa62egxSVtuu8AjmCHI2eo61KD3zqaB-ZiFl5Fg8b9zIiktAJhLP6YA-iNcuS54hd5-EbD3eRvnsYOwmZTcDjzrk_9AVxIfrnyq2BhxgcTTWw5n1XV2hBoqAQuzhOq283z1dPbDs3KdmKNY6OSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇹🇳
🇳🇱
ترکیب دو تیم تونس و هلند
ساعت ۰۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/95953" target="_blank">📅 01:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95952">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtAFSL5jNOKf5DBHV8PffnReYUCvkl7bpTcK23aFPq4R8u46mh2kS_CEdEvNVD5CEtgCb5hvv9qLjZ5VLh3oFBHefkdoGZsiHSI2mVyYUwUC-ZngDcVOp_tyhKtXiSC9rlmac3HdfdIAp_uOQ35yTrZQMZtcf314BOkFlxXpJpTjHxpOTcBM_ef4tkeg0sN5jxJ9Jpp2b4xFWJOG6ptTsivLcOQ1EgcJcyBZRMae4wuMjtD5WvgDT_VLrvVDoYKX8Mfy2n7WDNkbFP4Nejvs0DoZx8PYOFGcLY8Fc5hXcACEYUWgHIUreQxCjg7_MiNgp-SL439wVytr7UqweyoQCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇮
تیم ملی ساحل عاج برای اولین بار در تاریخ خود در یک دوره جام جهانی به دو پیروزی دست یافت.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/95952" target="_blank">📅 01:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95951">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhVB-iSIeRE8EmAILjJr6TPc5Kk61OorPSZ3xmMn1k91G2evh8DHm3RBjIvuY9R38RHmb_Yq4DbCqZCk_z0ObuNftBmE0XiXHpZjbRBcp5RAAtnC4Jd4bOjRco9WuEI_20pYdoAP0gqfBEqWmIupOJ7wh-bGiL3RFmM58W8ppo8QyD3WYkGHws_SwbFCaAkza6J6BiT2f01vEaKZDNAel-286Z79OEzQMS6E-pAYqvw0p-8QqSRrzTD4z-sv08JVHc57uw329Ys6nWRF2-nlfB-bXXqIuGJKDwhX8WgDDbo35m943TmVlwAOhPZD6UAsd96XkBe231YKRisG795GEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مانوئل نویر در 9 بازی متوالی در جام جهانی گل دریافت کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/95951" target="_blank">📅 01:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95950">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWj2V490TsDpE7c0knpUiX61Ob4iYve0g5ALwcsYPHY_cWJhUx4QdcliN7NtJ8sd4wwNdhhkQoOkFc3oAyvLi8rXEnLOcAp1MOjwH8Stx4uiQSRosOeXu5vgvna9RLSvC_LbM2_q0PdBebhaRejK6MBXmt8eUAu8gi7jpTNWWwHYm_CA5qe4x-Nw-IO_CElQeuwPoRT7Oh4QVrWGare3zBKTQZn99_nouPzF35l1xXuWB8DC02IxMFubVp5zY4GegdWOnk9SNaKFeSUASIMuXkcVrIJlvBEOyQR3DRUCr7ayfRKSZdVZjgo42Q1Mh1L7OxzKdh7rdSGfYCjVebIW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇮
🚨
🔥
🏆
یان دیوماندی تنها بازیکن این قرن است که در سه بازی اول خود در جام جهانی به دو دستاورد زیر رسیده است:
💥
بیش از ۱۰ دریبل کامل
💥
ایجاد بیش از ۱۰ موقعیت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/95950" target="_blank">📅 01:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95949">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال @Palang_Bet شو چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی @Palang_Bet     @Palang_Bet</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/95949" target="_blank">📅 01:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95948">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azvnlVgzItbNkGkPMbkr_XTgnFN1q4lgI-HkZlIRKGKea201d_Yk7rs72Q1SxSbvXVfqU31xXGD5QbDFj7hJwJNnN1S5UZ-yt-qP7lf5h4S8eFyAmCIQJnggrY0qCuSDyEgMb0a7V3Wn1WqJ5Z_qc-JFw8-ba1eo-jO4-_dM5Q3VDq1A3tdxzu54GLIPiqeqSddxli6jfsLtPYEDn5f_i5oZ2MD3DkxSg2Nk2rKN3J6ualZeQVfB4Ed1nGkT8VIuUxfAlb3z8dEDZIe0S7f5fqgVc-TRaKKNPzE3O6KfvxXVNagpIS63BLhEht0Zp8g88vU5TY8-9eKBqaHNeTy39w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
@Palang_Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
@Palang_Bet
@Palang_Bet</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/95948" target="_blank">📅 01:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95946">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkU9j73F01Nv--ay7Pa3rON2e-Wbl01-rOSI_9YJdJZY8uUrB03jC0TzKaqddViu8JEpZg4Ugu81qBj7yflyEcrTmgdKo-ujtybtCqbySfhLl7JkDykJW66ZKidEM1zh1boS-PVHWylcfbKmWeBUAvCq--sS1aTR5bfV38qyI4xt1ccAnMCVwvrjziBmLTlaaU89SnxGRuUtM14QUNw0e1yGzBwVYKkxPMwWwIrjZHG57luxC-UMeqRbt3Ud3qJiYiXAnrZqYxWl1VBXnvc8Bx8SSuSYnynHDDE20oV23H3fe1sfd8m1ci-c3zuYLBg0PniK0pln5gBInUbcAJFo8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
❌
تیم‌هایی که بیشترین باخت را در تاریخ جام جهانی داشته‌اند:
‏
🇲🇽
مکزیک — ۳۱ باخت
‏
🇩🇪
آلمان — ۲۵ باخت
‏
🇦🇷
آرژانتین — ۲۴ باخت
‏
🇧🇷
برزیل — ۲۱ باخت
‏ ‏
🇪🇸
اسپانیا — ۱۹ باخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/95946" target="_blank">📅 01:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95945">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">جام جهانی 2026 با حضور 3,605,357 هوادار، به بزرگترین جام جهانی تاریخ تبدیل شد، البته که هنوز تو مرحله گروهی هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/95945" target="_blank">📅 01:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95944">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivRdYE--e0Ne89Kn5PiH-YMjQXsOTj2SaFO7fC4gkQG0ej7HUI9aXefg6FZ-5z8arjO_El2axqS5TA-a3xo-0wkFf82OXA1X43rw1JwjagdNeMooFUIHZq3mjLOYeBqOAAILtW9yBYKljuGczHvxjlTwJ4liacXnfT1_mAPwm2jwma_fOK9PdMCSM0cNRj0xqtLumQ2NjYKq_JH9OSFK_kMfevswAojrnerDBEzhhAsQxAO19WEgkxaomTXp8sUZ9OoCfjeE5_2sxQvNBcrGH6iIINRL5jjWZ8wB5bl4ruEXLuo_FeqnzO8Q4F8GdvZXqzPKW5R4nCRB9dMa1KpNKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مربی اکوادور بعد گل تیمش رفت با زنش لب گرفت
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/95944" target="_blank">📅 01:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95943">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2_022uJaJW7BXl3zLbn7b1yUM_tuaacYSSAUHb-ojMNXgWZnz1lZNQVs76z6irlSo2FZAOWsKFwFb9IO8n4VzQIjxFn9xncRBvnKcAUbQUfnCfzXwHm7ax_rdxMLHZMN5NocVrdw1bAd_LcHy_fssQeGRuRyY33WFf4-A5092MDztnCOtjQSXHC9BnxqNO9Y43q1T0UAJfyEeoLur2xBFEXUCmOduL1mcpgRsulO_p_w4LaKMsbIiJtMTuJNVacAOcWgusssf95YyxHPRoCmrRMpnk6dEFbvLPZ5mFMJ19YyEAxZRkThC2lT4HJxJ8a0DPeqkwba7GNNAKflK_1kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه E جام جهانی 2026 پس از پایان مرحله گروهی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/95943" target="_blank">📅 01:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95942">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇨🇼
تیم ملی کوراسائو در مرحله گروهی با جام جهانی 2026 خداحافظی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95942" target="_blank">📅 01:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95941">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NAqgEnw1T09tCixzVDUdzvzk_at8WqhHJoKWMFl-GznB2ueki5W2v2Ir74IzrPOGn4mdYDGo2PrmSeRyZqsatk8iYr1mtXaOfe84FxwG_ajiUef4bpBGPAkBEEhzR1iDRgKFbUSnXYc8bRagdRyiCt6B1aJVyGkHgQPmLU5nWQjueuJKxT23vul8SGnlk_vgik0PiiLFwNHJfjHRBTXZPRHTQaj17Uhoslm-Sg4z8Uvkz4sKeZb76nDRSLon8Kyi_8p7HMDA6lwUT5ihTLTgFnjrIuikufyhnA3bBvAyIEPaGAtt5cf2Qd3KlKCw3QAEQIjLbibdveSza3BfNukxnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | رستگاری اکواردوری ها در هفته آخر و صعود به دور حذفی
🇩🇪
آلمان 1 -
🇪🇨
اکوادور 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/95941" target="_blank">📅 01:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95940">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🏆
پایان بازی | نیکولاس پپه امضای صعود ساحل عاج را نهایی کرد
🇨🇮
ساحل عاج 2 -
🇨🇼
کوراسائو 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/95940" target="_blank">📅 01:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95938">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TNkvRL31-peWfS-NrMFpBtYO4vl_djzgyROketyRGCiwvU5LWodFfwi0zVD0wZLQu6i2QeVGhhH47dtCH-MO8fVB89cdVGlW1RHXxPlTsnX62GcyHc1VUb64ES6YVl71BgqH2WBpeuOL3oqj8wwFwZ0TDuSuKz6dRCdInw98fSeWKOiwabSSB1YfEuaMALYHGn2r7CXKdeUPLmoNDutiX8hkodMahNkAM94mkXMlJMNHsWlsWgYCXtu9FaJESGmrZoo_WA_2pv9oGV05O6hKCSC-07LUCGUdUcWpvBWza2e8n6vdSCDV5y8BSg4jcCgl3SPzwtyAtkcMtNNJPDIubw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VFbjEoteF4salofKYWsl7oH1pZAodWq_rbhFikO_pXHoGQ-DUYQRbDbkl03qetEJrmMNkzOeczOCRIG5dCoR6BtnjcaN0RlSDExYeYY6jjCqa7toTX0NR9FjTKlXSYjZaY2gUHiNzV3rcE-tKwXJCcA-gnH33KQhX5F1vU2pgUTa6yWLE557QwS1mfDxcQOhoPBfAAChYQb21IDqXwlEH-O5fWr3OrH4mCjPlMtlAAVznIHxqTXxd15k7TqWAX9z5JMlBRA_HMjFkPWH_0V0YCAhTuOqk-1yJsKLi3neV6I9VBPmUAnk35fgETTsk2fHmDK-iZLNvGCGxQiyUEsWdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇯🇵
🇸🇪
ترکیب ژاپن و سوئد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/95938" target="_blank">📅 01:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95937">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dbd9f7642.mp4?token=WztsuSTFiZFNliMBMg0vZEPzzj18ku2nkaxJ7-UCO6-lA-XJ7H1x0puP9zLB8htk8kAnohMQzoJ2Qumm74ONNNG3nQSpp-NqZfvIs5eaZNsmxWavgbg4hfVjabJqY_xWfsl_FDO4fneIs08TXzxFvJv5ZZSasbUR0dlOTPLtMBnjjjutBPpyWgmKx6OJXFFEhlZJcIjKM5OU-zkORTZwAKYN_R5WiEgcEG3inaS_T5pZWHNPCynO3r9Kn8xDk2QWXjcWLj785If3wZMfhfqK7QaVk63SZslhgoLb1UGX3d0M3M1_q2G4trM6A9g0Zcvk1pvoEWsh2KLihNEOTviEgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dbd9f7642.mp4?token=WztsuSTFiZFNliMBMg0vZEPzzj18ku2nkaxJ7-UCO6-lA-XJ7H1x0puP9zLB8htk8kAnohMQzoJ2Qumm74ONNNG3nQSpp-NqZfvIs5eaZNsmxWavgbg4hfVjabJqY_xWfsl_FDO4fneIs08TXzxFvJv5ZZSasbUR0dlOTPLtMBnjjjutBPpyWgmKx6OJXFFEhlZJcIjKM5OU-zkORTZwAKYN_R5WiEgcEG3inaS_T5pZWHNPCynO3r9Kn8xDk2QWXjcWLj785If3wZMfhfqK7QaVk63SZslhgoLb1UGX3d0M3M1_q2G4trM6A9g0Zcvk1pvoEWsh2KLihNEOTviEgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم اکوادور به آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/95937" target="_blank">📅 01:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95936">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhFbUCnd5rZq9LOdH7ZKZph0TyzXvjFGnyuK_hVgb_9dWFD3DSFUBqgW5VrR7Ee_rYXJmm1T82n3vtsx4U4bnXeTiiZ2SKfAFs0seL0vX6cBtxi0up28-FOtR-osdBrYfzUht0l4YtBzVc4xDn7yr9dECxHqAI_yRyb0Zw8ig120t8BcCNjIu_ePVQTvoM09RThYh-JAQnnChjW5sbvdOXJi48q8ytlIGAzko3MWya4hXG_hAa1vTPaTSFRENIqI-3sPzSxFVgRXD3JjQ7_JMHQJNRt1G8Ojj90hYPHB2th7cfyCJzU4W8dA42Wm5lq0cYdK2hMnNe_k36cS2BgIyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مربی اکوادور بعد گل تیمش رفت با زنش لب گرفت
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/95936" target="_blank">📅 01:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95935">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نویر اینجا هم رید</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/95935" target="_blank">📅 01:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95934">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اکوادور دومی رو زددددد</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/95934" target="_blank">📅 01:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95933">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/95933" target="_blank">📅 01:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95932">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXqDwky5XSwN7EPpkcaqoj5LEZHTN2C2JyCoeP-DEPf_wNvMWrxaTPC4UuB8Wp7LgP50o6lUzFWtefGVk9hg3zfcMfkeZZUnf4SUUEX_34KZ2ctkHoQl636opd2ZRxPRDA9nRKgYzA0Ff-W9tVj89Ja5InrH6lgtf6i0R6-gZQee0VuRveEcjMDt_iNDjMEMGnRR9RK6yJxC9L6FHEsEF1RDg-gAQQaneG1NcFmeFn_RP6_XeLuVPz9mp8jS3KDcrTa5MI77xvzUtqLcWEdCzAkQnSsJNUeuhhYjn7P8ErpgoyDKX-XHPY92RExaH-Z5p6T7kIx0pR1DTiPCiC7lDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نویر
😦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/95932" target="_blank">📅 01:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95931">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3fb1037b27.mp4?token=lf5YKyzMO1SwYw3spgviaucbAzYkwrnR4Mywi1eqfvWPee3wnxZBv1A_8CGPhBi-mlJR66GUxY4Ec2P-VXWBHrUJWdoIvwTA8sg_6MtT1oYlMF2YMGETmBeBoSE40V9t50i36HhvecBI9zBLyR_Nnuz62fMK5mxVoVOLZlfSwEEzeUjR2RQS_jNqUd9gLvVuHhtLA8Boh20LPtKlpfcWpkjGV71WtFTl9sS8vBUCgwQC6I_1uBM6Rc3OpJBCD7rM7ElbJcisEyvfbduxVN8UJKADnX02OTwHrvARcsKkNzx9ZCPbOuw0CplX8UXp8olsA8FMy59elJgTg9ADv3VYMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3fb1037b27.mp4?token=lf5YKyzMO1SwYw3spgviaucbAzYkwrnR4Mywi1eqfvWPee3wnxZBv1A_8CGPhBi-mlJR66GUxY4Ec2P-VXWBHrUJWdoIvwTA8sg_6MtT1oYlMF2YMGETmBeBoSE40V9t50i36HhvecBI9zBLyR_Nnuz62fMK5mxVoVOLZlfSwEEzeUjR2RQS_jNqUd9gLvVuHhtLA8Boh20LPtKlpfcWpkjGV71WtFTl9sS8vBUCgwQC6I_1uBM6Rc3OpJBCD7rM7ElbJcisEyvfbduxVN8UJKADnX02OTwHrvARcsKkNzx9ZCPbOuw0CplX8UXp8olsA8FMy59elJgTg9ADv3VYMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم ساحل عاج به کوراسائو روی دبل نیکولاس پپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95931" target="_blank">📅 01:00 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
