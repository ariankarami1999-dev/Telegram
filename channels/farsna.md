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
<img src="https://cdn4.telesco.pe/file/Sd_fsjzUosmXMZvdJJhhA8gUobCRP5iRKyBH-L1od2wbnx20LYYwe_OuSCGVtx9pE_fbfa675sIsHnpu4DTy1iPIT3g1p_PEg3Dg0mpGW_RZ7rf0nDz7PRO33ydNNjD9M8EomfZYjz1XNdnDEG-ihCiVBGCpwt-vpFQNj4_ljAQXkTBTXyEes5CjGbTrq9vohY8E8XYmMBY2Rlk4eUA8mUZJ0RkRnBWRPamghgNSCth1QKe4B2MBeI2C6DBf2e6oYvKHvb7veoqJeh3HOGz2xePNpz6NHXSMBnQwAHvIebj23bYalqvPOHtiMtKa03LExxX8b7bCpXOS01AQ0dtwNA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 19:08:54</div>
<hr>

<div class="tg-post" id="msg-446760">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/173a5d7480.mp4?token=QYdiSPu1fUvNZy8IFPQp4xxBjgOUNOYy0dofPYwhCkiGQdJvzYQ0e8dqVFYcLLNEuPC9-dhXvm0wcSuPLnghJKmM8BVPQt38kv54VCyM2Gonr5YQIrIVq_z6giBlPsu1P7nvjUBZ39Hjg-zzB_raD6BaWg9kfU0zmECKKwKSjCfWA6r4gXf06ZUdjlM9iZa6Lk5fI5sj73uvBS4BHzxJTDcpAf9sYCAMVGzbO2GPcx5CQOtq_5zVzOx-Cq8owe54hz7BT0_WRUpv3d2V0b819jN1Q8tH5cPt4DUw9qpeeZSiCugrT_3lTpO6JxSYaiZ50lkzRU7-hQzJJkcrB6Po7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/173a5d7480.mp4?token=QYdiSPu1fUvNZy8IFPQp4xxBjgOUNOYy0dofPYwhCkiGQdJvzYQ0e8dqVFYcLLNEuPC9-dhXvm0wcSuPLnghJKmM8BVPQt38kv54VCyM2Gonr5YQIrIVq_z6giBlPsu1P7nvjUBZ39Hjg-zzB_raD6BaWg9kfU0zmECKKwKSjCfWA6r4gXf06ZUdjlM9iZa6Lk5fI5sj73uvBS4BHzxJTDcpAf9sYCAMVGzbO2GPcx5CQOtq_5zVzOx-Cq8owe54hz7BT0_WRUpv3d2V0b819jN1Q8tH5cPt4DUw9qpeeZSiCugrT_3lTpO6JxSYaiZ50lkzRU7-hQzJJkcrB6Po7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به شما رخت شهادت چقدر می‌آید
@Farsna</div>
<div class="tg-footer">👁️ 301 · <a href="https://t.me/farsna/446760" target="_blank">📅 19:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446759">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db58f0ef39.mp4?token=UWO_aO9853JB9bSTv23yM3R_WLLIfimyP_d6GLteuZi9wPX971o2dWISP8GghV36OI23w74KlM0s9VM44x3VmEHqYYFcj5PSTFJRXjbulkEDL2Vb1if0N6s5TOuL2QNaWwhDl8DkWxgjkMf0TBj0o4txu5OZ6vQu3tGB0eOpX2UYVM3qhR6V5NfwEw3KnIt9N3DDEdNaUHKT7JdSMyF6Q9cUqNOVk3bTXtRXfsoZc71vhvifbHBKvnfbQYimbFEvHSOdD2_Y9WpdfOelVZTJsCdRFENJLu8_zmP6bKQDac-OprzxYbaouQPIKLyOtilds77sTI1wQp7JbGvHY1hGE4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db58f0ef39.mp4?token=UWO_aO9853JB9bSTv23yM3R_WLLIfimyP_d6GLteuZi9wPX971o2dWISP8GghV36OI23w74KlM0s9VM44x3VmEHqYYFcj5PSTFJRXjbulkEDL2Vb1if0N6s5TOuL2QNaWwhDl8DkWxgjkMf0TBj0o4txu5OZ6vQu3tGB0eOpX2UYVM3qhR6V5NfwEw3KnIt9N3DDEdNaUHKT7JdSMyF6Q9cUqNOVk3bTXtRXfsoZc71vhvifbHBKvnfbQYimbFEvHSOdD2_Y9WpdfOelVZTJsCdRFENJLu8_zmP6bKQDac-OprzxYbaouQPIKLyOtilds77sTI1wQp7JbGvHY1hGE4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل خبرگزاری فارس: رهبر شهید حتی در پیچیده‌ترین موقعیت‌ها هم حاضر نبودند خلاف واقع را بیان کنند
🔹
بارها اختلاف‌نظر اتفاق می‌‌افتاد که یک مسئله چطور برای مردم بیان شود اما ایشان خودشان صریحا آن را با مردم در میان می‌گذاشتند زیرا مردم را محرم می‌دانستند.…</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/farsna/446759" target="_blank">📅 19:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446750">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eJ5V6JTD--vvZSULtp4IJLvR1tYP_3Wm-gGHlYVBkjpECuRVlzaW5FFq3orEdCN42kwUYv-YDwM3BRMINBCRJiNVKQ41dRGlOKG_sj68aLIV_qYv1LedAYM2KOLzdmUgekqYf3fIrt1OAszvDu6PBJCxKfe03dwfYZ8mQzdXG9pvo69C_WfsJ0AuYCQuyN0mCPlJ3bPzrFZ14eWxEr5q04EbT9dyzWwDh83W5PoSjf7QiVeZZVqj9M6nFf4vXmyaqalUzYSeE3w27W3HUFgXiuUyvEtC434Qdhz-jWZbxo7L1gtvfQ-1MobtPrF8v5cLc-ERelZ3avBmo6eTwKwF9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kv506bPTclk32H-QRgTl0TJUjnUqp_A7oKldUlPOaDesYhd93_ufXvVuSxBhIofmXqn-lBB5E5SbpRZS-ZRGnAj1PVK1IP-P_GnbGUmqPzcdU8-k5-ZKQ8a4iwzMxdO5-ijsAYFVE7tOSOyJww8bVCIY6KMb9MJll9G3XXWBYAfaslsDywMfFNO3EOOTfTvjGFAfVpVeXtcCOvA-7wYm2cCi7dMkq2JVf45gSMwnv9RTAuoRPsMSUoqSZ_CXu_RqFT_cyNmIwhiAuT9t-6ak9lr7epXnH1YVnfVgM3tW5HCSGMKxCCWJ2LVfJKCR12gaJWbg_JYtJLgHLGfk9XAY7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CqIoPuKNSLJemV9zduNM6xmE2bAPSYhi3pNpw8O-pvANOovu_9xOVgjWW1ps_hofVGpkLVRvvwgl_8drifo0ZgwzfDroDKVMGvVacXMdEHCPOuj8uT4q7nu4gJn3jsdf6eZGQoAufIAtKd7uMYvSvq37yzI0qqWKhMhlJX93e-DjvasBb-ab6UhOtm1uT26wRuXafHAhufZ9g1PpX-NOmROKuQyjC8l0dm32Z3zrQsarPuitqG-4pG1lT00aPzny36SihRn0L5iUQIVObKGpInoxwxyfQ8U38_fI2pfiomG4Zr_nVT17DOQKVQs83RdyoqfvczcUNEH2VVO9wBJwRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZUHEZyx3spMROhZVzd4iWyUbdMt_o-CK3MTqDx3NRGwGPDURsVDMlMZT-F1CoUPtiMS4lXNMbVFhgoMHTbK36HSwmZXrTMqIwjclnc-KqskGdF4QGTHpI43hLnMTknplmLHjHji0C-OuphGsgBDiE0zk1cwPDG-CjMaiqNEuiDrlKulNeXAnTLmsWndPE_pPzZCpRrINb7BsP7PxNXM70cOp0-Mi55-1on89YFwv5L4qQCGgZdF9u-7kuLCeOFaGWp2cNdCLBn1THzCEN21QOkfaVT8Gndg0XdhxQI_5OjBoDEYErBzTpsbEgBDJ0aSM1JsI3HqNCx4mEvLQyDlilA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S6oDqle4ejKVFbjYnZ0bpKN7_YZ-GEXLA2Fnvl8E8LxF1psy_zzkiRgDnyR__gCAjsR02-B7xz535Jl1XOGSVwh4ChufH2YHIKydsXT-E5CPGirOWB29PwZCI7uI6-JIFYY2NllNs2QePQJEHVoj0mFySKztywn8gC9DQa3Fhneh4dC-jqOtM429w-SpxKWXvWkxEs9aW3uTOf7cFNBoT08g9WeSiVhS_Rk2mb5UCKCvZfIFm15jMWoAhzP6T6zddBUC2LkqKbxgYJ6YsFYctS1xsglGA9Tv8WYeBFH_QDJKlK1zihwS_h1HQJMWtf6srvxF3jLooHDHjAlsKiNNYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KdVnl1mJq7BOUivkSz21fb9X5Mg_c8QaLe4Iqajf25--Ho-5YBgLMvSnYUaExnxwPY45Fk3P_P_Fyzi3vXP7pZ8D7X_GN7wMblJObPp68Cw_5PPpYPE9XQoFlYXT20cyeR4EYjdTO-4mK8cT5R1gz9EmQn9hbLGeC5ABEFwSc67chF333V9G3y5dJ3m0630PP3A7cifjZuYvPurSXyPcyAtss43gkEVzjA6sH6C2ppOt_xZttqFhsVtnyCgWn_6h5WkOe6FgMJD09kLxuu-E_9mF8dWGFvLjUodH1FgUEn_9xyNzrhzzr0MXxvc8msMrppcVgAnblYcO1IfVQiChbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uApcwKz1GLc9McJCFRoYUQYbssaLgBT3ZhtCN5rTg1r0EnciWXhIw0o6gcCR8Ix326nMlgrnuPqA5nfKCMWMQVxd1fy-JOjDcyJFC4JKOPJ2ZG-3LtbZAX5LjoIw4H138r-HBcsy0OBGEMUdFQl-CwsIBPfYaqx0aqf00g9W1_nlhDkaJbzVzhJzPu5uFxWP84VBbitavadvV7SNkIY9Om7AGxuLhC9yO4S4CxiKyuVJ6e-FBq9RqQipuTUvYaMDAukMj4SwkXH5fJKdd74MuikluaVJLrmbhqKNEgAVvuXIcwoyGdNAej8gKPaW6Yf6JYUYuLieoCPOrw7DHkkTAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QyKabTqbttwQfRGjTPeZ3CdNAOm-QXpxcxKfwpWLAM6kGZuWh7qNY2_AlAx6SiiYKK62NRDnGAosO6rETUKpkeNfP4B9MEOa-sQl30m4pO6K0p80j_3micNfkA1WYO4_Wm_ktGyDfEs4cx6CKyP-rcve97oTzpGk74y6dNnTLXKSvyJK47iyRQWWkWn1KxgiSUHxJlnXrBcY8iDyqRKEBjT_uU93AQzuYR14M5YY6t4-5zfyvY3pR9EaCIk8IzpNRu-Ugj2ZsM9VvfKGL8iU3HFL7Ufa18uhphii-GZ-vtjo7sibqdfASLPf1syv2ZCzSzsC4aQSHvfovONvQ-54lQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیوارهای مصلی زبان مردم شدند
عکس: امیرعباس ابراهیمی
@Farsna</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/farsna/446750" target="_blank">📅 18:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446748">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🎥
داغت نمی‌شه باورم ای رهبرم...
🔹
مداحی حسین ستوده در مراسم وداع با قائد امت
@Farsna</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/farsna/446748" target="_blank">📅 18:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446741">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7iLV60VPK5caN2pqzohwIBvl-VhAFPNCcCwNcilg4D-_-o5Ct0qzI1fhA1d9OSXqBKhfhhYhr8HZ5juZg-iexxTKiXqXFQ023nWmMrHQKT7XLlvs3Nth9ZQN5g7IcdmXf9L_Zf0BeAln6Uvo4pzZEbQ6YwrUOn2iSpplTRWg5Z_VTglzKzE0w5u7DgnW9zt5MaROg4pAD5yQhKYIsVgxLMrRwiz-vf0TSO7IV8h8V3N8NbZhy8jhjSa2PH7PDD7JE9ceXV3Cd4OiGEa6ZP2TgsFsIGwOM8vwnrbYk73WMdCDVcZSMU3ZI0r2DPEnGYoZ3I-ylX9MGABdb9ykmL4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PqBmg4epDh_M48MMi4cb1JgLamW1z5wy49NRFWV92O1CPwY8hkA8fO78FqONDr9mtg2ltqqiT8GNKtfyGrc-eW4DTdrIBnRljpDRzVK792YFwdtEo4NPXQAatVmM__nB8auS31kec2Y85TICasHZLSe9vA5C0w8SigonnVlEdylGJY1PtEIF5KK7KnPAbT1QoMIQWe4u4arCJqPHpHCY3QfWijYKTiYDktxxZ1OVGYrCiMb8I7q7ftf1JKYDkVw8cOICEx1jtrkjpcCQhEWM2jBxuN94D5iwVSqkoaqylsXCYuyMMKhvhIDVwdEVqOJf5Zt9kw6Fso3AZgM89D32Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I357jcz606uBJWKN8bimH9ZYrsDmzWQRElzzoV5H-yfC_OzR2blZP9BCHO_SAIxW6NS-jFEj7XZtZFe3lX1M5kXqu94J3AYHc3yay5mdoTe-kuotVcQFVU16DVJo6t9Pv8L9deIgHGhtONhykNt6jClDhCL6-ddjfxEnNwbxlq4IApYlb4wX_qSDNJFJrpIyUkSuuvSu9hXEwqXTu-T2IFSTf1mopgkZnUZe_ciK7txYbfDIEpwttEgj3T_gizZH4DRWDrtSjjAwdlLHARklSiXecyoBkpzB4K-SXnmMZ4W0f-kLW_Gk2bjjtnOu6vjXvTLEFVTmVIIcFgOdczdqug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tc2cZuiDKlPPaMnquS6W7c8rIIlLToQKy6Uvi6454r1q6J3odZnEJePidyaJEqKzOLhRU-TciB7a1P8OdPxSANAMY8CU2C8WMlORUMOgcA542CoIUZ4btvRYA9fvmcq5gTNnXbqiZE78Iyj9SVA0uGxzjZ5MWg8U9MoYmJpC3gnkHsxVyVMh9i4sRyugP_SjQSLq_Af5I7sTwvxyUclPl6wOJEPmSc3-Ol1oTmWXuClr3yKetJ07x8v4jJlXIem100MVnGUJCy8gtNJakw3VbglB50QcMR3i2Kbt5EndxSwP1grgpysnFuEXNks31KTa0mazXRjlc5wIuleJ1wotkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WECUxLnfo-MM9A2_QxDmTpCnErMze3RGUtu55PHrZnzO3QcRiw5eVNLt_j-z2HJon08bnoXJd97VcGOndG5c4y3iC1sChXA6oHu4ADDSst8F0SCKVUW5YNpjXt1fgYS64Od7IGatROq6IWceTwLPztTnS1q_Lm2MBehHtQwjGky7mioqyap0XEa5tXPs-yYEPPrizb8xZ6wwUvWMOg3HGUjAy3HpoFjY5dtyYqcNJT5iYWjYTBpqjh_sxmcATr-qCw4-1p5wYIledfUOCJMhWG-cnbtlngmVvoZgzj3qP4EnKJm9rN_KEYp4kKpcJA1xxIcK0ZvfAXXDmUbZKqFnNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/atbV3FU_dsiwyVmeXMz2E99vIukF9Y8sRVY-_1q7I00ux15j27-uRA2iI45R4IZ-DavHN-Oq7akOlOVl21_ZK0MUi4POguOqk_qw2942qRUkl3BQhOm1CcEmW8DyQXbhhqQ7w56q6oJRnah1RF_YujyzOm_MFKQqmt23mEHjGR_qWD830CgSb7PyVw0gkWzlyWkLgWKtjNomb4XHbhj-hRM-f7K3VeNEwmkG-ZudQviwbSSUN2m0iV89MB4wnBzwyU2OFT95k7VDqP3I6nA3v5-ibxHWmtcA9SfxXtkbSOO0CtL1fkxqH8plCw85-2qUCf5u3yv5Xp-QzAmF2MPOcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lf0piJE2-Ye1Zr1HRja1ZFLUp4ew_HM0PkYwucpMoXq8eX5fJVzTQpn3u0jdSSQ7xlN6L1cHXgAOycX4YNZKgouyqT7WEQTnijcmcWlp5c0Gh2vTrgIU4n0gc-2Nhn0Piwaoz3MDV_CRx3bi3JjYOoCh9kCKMxq0UnGC8_WOWhV1LysubeZClNtuOd4d6oJtZTm3RfpNqoyZOIZp8KCT-VrbOdchrVZUcdx1sCPWmc0sewTM1bx5XKayUNIhb_j_gmKpqLJ2yrXlaReQ-iHJBzCVhoFl1BsL4x5z2uVLkklm1RUlsmwZW8kpiHlhICwM3VNl72ikvDda7tGzAsu_sQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وداع باشکوه مردم با پیکر مطهر رهبر شهید
عکس
: محمد آهنگر
@Farsna</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/farsna/446741" target="_blank">📅 18:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446740">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d07c6abfd.mp4?token=sS5e5E27j-fv-6oFMakHk7g5k0CKhiNZ6PDCywnnv2ukwrdX1-J3qPuPFsnPDeZ0sKgBEP-BrZHtIET07Pengf7MLYyilugbDGNX8yXUeONXxYH1q-_qC8YebLEh-6q11drpQvVxUfsIvUxKYntGLP3MV08p_TeGEpfkOiGbHu5Vb6i3D0INll_soNSQ5eA-EDm5-9tYCG8R_3gVI1Bs37AA4vVkyskWKzJreZb8SHvZCuaetyaFQAmzmLL3rxpSVKjyBuZYqqKP199abwCKSmIqgUxvde6ctP-0oDm6F1nDjvh2yDITDsRAby9rcwFXndistc3Y9yVhkVud--5Fwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d07c6abfd.mp4?token=sS5e5E27j-fv-6oFMakHk7g5k0CKhiNZ6PDCywnnv2ukwrdX1-J3qPuPFsnPDeZ0sKgBEP-BrZHtIET07Pengf7MLYyilugbDGNX8yXUeONXxYH1q-_qC8YebLEh-6q11drpQvVxUfsIvUxKYntGLP3MV08p_TeGEpfkOiGbHu5Vb6i3D0INll_soNSQ5eA-EDm5-9tYCG8R_3gVI1Bs37AA4vVkyskWKzJreZb8SHvZCuaetyaFQAmzmLL3rxpSVKjyBuZYqqKP199abwCKSmIqgUxvde6ctP-0oDm6F1nDjvh2yDITDsRAby9rcwFXndistc3Y9yVhkVud--5Fwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل خبرگزاری فارس: رهبر شهید حتی در پیچیده‌ترین موقعیت‌ها هم حاضر نبودند خلاف واقع را بیان کنند
🔹
بارها اختلاف‌نظر اتفاق می‌‌افتاد که یک مسئله چطور برای مردم بیان شود اما ایشان خودشان صریحا آن را با مردم در میان می‌گذاشتند زیرا مردم را محرم می‌دانستند.
@Farsna</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/farsna/446740" target="_blank">📅 18:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446739">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYcMowhLYKnyJzJxPXPVGY2MFGXoLqHVzCbTs9SQUiN1LYVl6wJ7xteOXBL2tZTsZVDtbHFGry4_stSWeaHUbAHQ0GmY56V_fmQlaRrrv3zWJ9dbk7io0ghED0Mh94CJ75bxNIu2yBQr2bTha-LW3LtvEKN08OQIbsI8uKKTZ4-AtY6yVB-8r0_3njFRTI1j79KP2s0DBu0Sb6vu893BUN0_WWvQ-1RF-TjX2qD41bKH5ojgaYyDKyJ_A1FRLnwK_Y_wa3lRfuaMGj9XzIQeySo6BUIQD5oYf-qbHBDpwrCoYDQqYHGW9hXqCnxpXFsnj41hiHC4mnF2rabM0_UlZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موکب سلمان فارسی همراه‌ اول بمناسبت مراسم وداع و تشییع رهبر شهید از روز جمعه ۱۲ تیر لغایت دوشنبه ۱۵ تیر ۱۴۰۵  میزبان زائرین است.
مکان: خیابان شریعتی، نرسیده به پل سیدخندان، وزارت ارتباطات، ورودی ۱۱
#اطلاعیه
#موکب
#وداع_و_تشییع
#رهبر_شهید</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/farsna/446739" target="_blank">📅 18:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446734">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه معلم | MIC Insurance</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eYSXTkpF9unBEVnT7qQMF0Y9Yeie7TCOCL8_hKo5flZpykc1OKLIrhybhcwG_byDHQYcxuyS9Eg_xfG4eAEXhlYCJ7P69CPZ25EOtz8bXWoH99B5RxS5pF7smyZlHM7YLM_ce7UVooJXtEITwrJU93UL_9eP-P6eQOf_qSjIsgdpjrMcAyIf8yOVjz0D95f1YInoirHrxgpI6Yx3uG_usw8xRgEIeQ_ct5q4uHMCJc0JUF639iR-NJgRpGRPfMyioubZHAVnmtNoozm0rfRXlfyNVAw8tk0IOUhi52l66vyzhNWUwafXY3VhVzl2JQs6uOyYV-CmmDhCMa7pf3YY2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fC6i6HM5z_92B-pcVRBZysJx7vGbJWy-nd-clMbGXaoX6l19OqJEqwtB_1yqt4Phui5ko4kmHYwp4ptlA9LIpEYyxmznr8IW1s7CBbqLq7ZtafffJfe6pxVvJxJg3iSC3Du7zTUF-S6b6c_CwNg3vNGzLtqdoY6INaN3Vw7jKDO08U0I8bJ4H8xwLO_TlcAQL94C2BEZgXTVAtn7hhS3tnVVH4wALMelaBVR5lZ-O0wkXgOkNDBWcDYh3sWZvy8kCmylEFxlfBBFpv6OKxU1pxHC9twO_DZ04y34HmM7Izti46wXqk0oHUM9oTNkY2romoOq_AcBq1GKDb1rqbs7QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lTW8qDW6gM58dJfgoRHAFkQ022IFOuv224lf25H_WTtRWVAER5JmSEWGcbcEcd4gMVYi1vi_G8ctMvRcuO9cMdyRJH6QBrHy5G9p4FsQGDmnF9egioQaGNyEz2njvNT7bn9X4ixgQtW6D8eSG1PiV23I20Hz_zH-MkG0qJVRiSOyEOy-G_qBUEiy_4LXrm6SisxwB_QCeVAA9LHsiirQ4fhGs5SDSKThkzp-qfa1caUYmatuc-dt0dsky3oMIlo_IwuNPa1Z7zSocPoACWfZIrGYJM_oytHwQP66X4VCvFVZQb2zaVyFGR41YZzwO8WcAbNIqpp9NcWDH0sIEBM72w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s8JtEFOSegVvDF6V-LNksacaZr0aTip1Jd_F78aKv5O8Uq56XD-77gqA6t_gYHstm1Ix7Z8Qu7XnYi9VyjG1LtLoT4BxoT2CkbO1Xb95dTwuXoj23wp8hMOkj1MOu_ghWSeHlseS97lcklYFpQ9qtlYqwdO2XXqtcv80iMas6AO5NX2akyirX83fWS6QN58vw6CqlmHibFmkNKZw8e55AEHkE3x4-6DuEsGIIho3IhXWDqdh3_Lpl65FJLkWx5-sVFa5fEZ-BtfZ6eXuNupoyubftyogodjqW_7hBbbSDF4apvDZY7s2n2zM9xbpMAaFo4APvlw7dFE86j0TkP7g2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njqtuk0EGHFttFEHtnfj-jDi33BhI_BX_VAEtYWOkyeKRB8Fy6hS00NhTS0q4r0T7xNIlbFw5dky6dMg_M97_EmxDz4LJDcA0FUyxkgvPEHqX5zB3_rArb2wv-zCp_RFAdTAIGd_zJ47-634fPc79rL8uazWEH4hl1PxE61isgJ-K3P20vlepNeq_rbBdx6eA6Ijv-1zkcYrFmjvYWFkEkua--sEf2g2C9u6-A3wD_4Tj9kf3PH6zmC2tMXRj5RQfG3Urb9MTYmCZms2XWy9Gu38azM6FN3rU6JugqR1dDKJy_oUMJnK0q3Vn762lxL2Cbx6fuJKxVhOrFMsnxVR0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
حضور مدیرعامل بیمه معلم در خدمت‌رسانی به سوگواران آیین تشییع رهبر شهید
🔸
در راستای ادای دین به آرمان‌های والای «رهبر شهید» و همگامی با ملت شریف ایران در بدرقه پیکر پاک ایشان، علی صیادزاده، مدیرعامل بیمه معلم به همراه جمعی از مدیران این شرکت با حضور در موکب اختصاصی بیمه معلم بر روند خدمت‌رسانی به زائران نظارت دارند.
🔹
مدیرعامل بیمه معلم با حضور در میان سوگواران و خادمین این موکب، ضمن ابراز همدردی و ادای احترام به مقام شامخ رهبر شهید بر لزوم ارائه خدمات شایسته به شرکت‌کنندگان در این آیین باشکوه تأکید کردند.
این موکب که از سوی بیمه معلم جهت رفاه حال عزاداران برپا شده است تا پایان مراسم به ارائه خدمات خود ادامه خواهد داد.
🔹
محل استقرار: ضلع شمالی مصلی بزرگ امام خمینی(ره)، سازمان فرهنگ و ارتباطات اسلامی.
🔹
زمان: ۱۳ و ۱۴ تیرماه ۱۴۰۵
#بیمه_معلم_همراه_هم_وطن
سایت
|
بله
|
روبیکا
|
ایتا
|
اینستاگرام
|
تلگرام</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/farsna/446734" target="_blank">📅 18:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446733">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/farsna/446733" target="_blank">📅 18:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446732">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25cea1a63f.mp4?token=Um0yTJaoHErVYoSB4Y9L-1HMsHamoo6KiUJCHxYizX6j9Wr25Yd8fomJPHKqX79kmoDkJp_sZT9Qos_NHBPrHWojpq0vhA2svhCwhzJ8LTWKcw9AapO6nkKrxn5vaGT6V4ijbHj_LvnrCnNWDNItEsZPjNcheyh6tPY7YkP_OMw3qCs7R2mWuWDsX4y1rr_ev8ufUSW4cWN_BKfg_h3f199E6ot4jGe0MauA9MCQyqeePzVWtsBIoWHRSVUuMvD7GnH9Jn4zVF3splxeZ3jvMppr8X9jvwqHdEP7Z5tNjs362qLPlh6EARh_yZYz9sprGzeT5BxlWhEx8nOcrhWSNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25cea1a63f.mp4?token=Um0yTJaoHErVYoSB4Y9L-1HMsHamoo6KiUJCHxYizX6j9Wr25Yd8fomJPHKqX79kmoDkJp_sZT9Qos_NHBPrHWojpq0vhA2svhCwhzJ8LTWKcw9AapO6nkKrxn5vaGT6V4ijbHj_LvnrCnNWDNItEsZPjNcheyh6tPY7YkP_OMw3qCs7R2mWuWDsX4y1rr_ev8ufUSW4cWN_BKfg_h3f199E6ot4jGe0MauA9MCQyqeePzVWtsBIoWHRSVUuMvD7GnH9Jn4zVF3splxeZ3jvMppr8X9jvwqHdEP7Z5tNjs362qLPlh6EARh_yZYz9sprGzeT5BxlWhEx8nOcrhWSNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ازدحام جمعیت در مترو برای حرکت به سمت مصلای
تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/farsna/446732" target="_blank">📅 18:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446731">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">جزئیات مراسم تشییع رهبر شهید در قم
🔹
کمیته اطلاع‌رسانی مراسم تشییع رهبر شهید در قم: مراسم از ساعت ۵ صبح روز سه‌شنبه ۱۶ تیرماه با اقامۀ نماز بر پیکر مطهر در صحن مسجد مقدس جمکران آغاز می‌شود.
🔹
پس از آن، مراسم در بلوار پیامبر اعظم(ص) و مسیر منتهی به حرم مطهر حضرت فاطمه معصومه(س) ادامه پیدا می‌کند و پیکر مطهر با حضور مردم تا حرم تشییع خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/farsna/446731" target="_blank">📅 18:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446729">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d4b5df6f4.mp4?token=muqOvr1411MRBjuC2Tg21huzoD3I86_Tjf4ySou_Qnd4qBBjMBWGnpKuRTu7qmU0-r6c_5Dueb6rWoE_XlUa5ydy-4ZfZpjgrpJUE-M4qKHGen4Ln4UmhQsm4tgtPK7MO0CP2b346N2IrqpYWqZgvce-I1VZ6dbg4DHKrUFQH3N7gag4NQHuwfts54aMUEzgEcVCBnYvRBx4T7n2iJaBE-BtLqSMwZ0E63B8heA0t9ht1dPhRs70nhQn_QF20EowVEv_ptQuABuSk79snGhumyNR_1oWDS2YvLAU-kGcV58x59M5KI9zDXVdL242LQsEx-1BFwBHS3Fiw7LYnQOYiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d4b5df6f4.mp4?token=muqOvr1411MRBjuC2Tg21huzoD3I86_Tjf4ySou_Qnd4qBBjMBWGnpKuRTu7qmU0-r6c_5Dueb6rWoE_XlUa5ydy-4ZfZpjgrpJUE-M4qKHGen4Ln4UmhQsm4tgtPK7MO0CP2b346N2IrqpYWqZgvce-I1VZ6dbg4DHKrUFQH3N7gag4NQHuwfts54aMUEzgEcVCBnYvRBx4T7n2iJaBE-BtLqSMwZ0E63B8heA0t9ht1dPhRs70nhQn_QF20EowVEv_ptQuABuSk79snGhumyNR_1oWDS2YvLAU-kGcV58x59M5KI9zDXVdL242LQsEx-1BFwBHS3Fiw7LYnQOYiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همۀ امکانات برای حضور در مصلی آماده است
🔹
زائر پیکر مطهر امام خامنه‌ای:« ما از بندر عباس آمده‌ایم. ۱۴۰۰ کیلومتر راه آماده‌ایم و در این مسیری که آمدیم، بچه‌های ما سختی نکشیدند. امکانات خوب بود و همه چیز فراهم شده بود.
@Farsna</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/farsna/446729" target="_blank">📅 18:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446722">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujBMvQck5_L3NzoNuYcwStrAZAoVQzT_jyEjmOCNimObMqcqn4keI6UMZoApLOFctaSriu8Au0lVrPDIX6IR22f6BfpM6d1b_g3n2EesuduBv5Ni1LByYySv502B_CRiSQMFvhjAe6uY4-bb1yf2gYqz-i32d9_CgNcRK3j57prqJg5sC_uOPGsBZ5pmhQoihpk4PhC05X5SscMjvI1BEx36PtwusViMTTtxCFReiixZBpXUAPmK-vo5ozd8GKz90ZQ10VKSHv40dmuyX3sWJcSIK4bm_BcNbNFSV86Pk98CJuUsZBRGSb-6f-BujTvyurK7gpV0n7Jxt4G014gzew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ISSjBOxc2OwaLfVTkHpYeOvMcWLrsU9BpFmPtyLIa8tZxRxK9gqn9nKG-M3eKE5mpP2GdtNJXZunxAQUd5wrYviNP2aWaXfgMr5DKzWzLxi0aPCQLB3aVVNP-NvDLYIu-jFPVCgV6WTxd0EHbAwW7jQsMkX5H_Wce04gH0ZpcwhWdX8CoN5NXt8tkdUU9OD0ZLS8pTFt08Bcq-Ds1zpp0XSkaU8xzxyoIA1uvEhHeuRLbP_WUYZ_c2fU5UuA6WyUbEpi5uA70k2i1_mwhqPJnzSr4zi_W--S-mN5JpnEl4HSKqJHg-en4TPPV05-lOyAY4yIiovIATBbHMGA-p_SMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eYzBLjFtbZ-EspAp2bFnvsYu1Buy9rtfwaBSWo6L88S7F8-uWkwFaMyoHfyOBfFyce43eeUSfB4AQETnH2_bDipnCbQl_SW4EYTKTCox8FeMPJFoejided1BuZGE6J45v9m9sMUJHujwnPebJVMYHWtLwxkqZWRXX2tToYYevHpccp9MKUtfN-WDxeGqp5FRT4X6jf_shCgHKf2Y7EcqRDeLQAzP0c4kTximgViRZO4y_PRrFokXP3LPc7tsLTuj3x2DTHVeZOxEzqotVdvro19m3VMuZj14d8ZPqHyZZdrvHInstOaEc7zdYHjBvQbXqGq2Vw8B50lUjFk5_peVAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sMmkNzftj5k9rI-snx-1UkixntIfI-Q4gZbFjQD0BX9Hejr91ZqaqtFQXxNCyJkLiQVQ5gM9iqoNLswOnAbdzJDI7EhM1aq7T_HwDNENqVjfNb2jyX5JFIYguBrMUhDaDCIFFhogn02uh5Z-F_FPHiaFAn2lJMqJSiCFqnD8usVj03TNjkksKbwSkbIcE80-UWwr0LoXa_ZbN6dzuEPzvMWXSzZ2h1yoxooexSnRIfrhTOoiLaWhrRLO1DBNE2iHTebvI0ke3K9Y_zelemmzi-gVRXTaYEKZ0vaxllZTe7mMWgjDz_ucArA-XPvrQfu48s1SJeugaEx5_91oTjCzqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h_rQ29vN9bhsUrcgz3_wgmIbniucqM1D8aphIAJmUm_WzdcYObt1R_r1fAI9igV19jM_M-6mzibzemezIErdFm7RVox22qzLfDt6Nt2rh8YXR0T8-CmwaNnOfrPwINZwlvq4iqXyXXubj0qIsWoIbqye9QtKHmZ9t3YyqmG8qBnxSYVBnyaFuLWD6iEvMWjLKl-fEk2JXJ96VubKUC-QHCYOeDK_HbCplMM5wIRLNT9CfE2UlgDKKFAUYJGy9BnIchIN6cdaG338U0ihud59LGLu67Ap3b0SzskjafHW-0dE7glyVQE_b1ONbX6ZtO8x8QHZmpKdnRtO2AHYzJGELg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V7aNgAQt9D65fBBH1Jg2kTC5Q-5kAM_RSanQ96u2uHRSB53NMKd5PUERTovKgQnN84auwzb_lpr0QzPuFvP-qn4kjo14OU5AqOMrj0Uhdfc1htIzec5Vl4ExOABvk9mBH3bMisv1ayvdf_fk8yG97RpeFo_96bbp8JqELSvG6i-giiqMNEwvKfd8h77ijWjRIRRsYLMuuBCtoI7RygeFnnNTxLsMHAIIAiKl5aEZ-dNwqwNWlVRAFrSRQdzOvwIIl0-wFHqjDRPe3FQLZ-PwUgBl2diHOHHwWxyGl11c6YtbFOQE3gByOcYNW6xkMvCrCWPe7eD2qv1jTUkwD-78EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N9muzExXbTHfFcaFIvpxFkMfXh1iAvYyBU7d3Ck-L71x-jsrrFxQtgDzfpC0tIuN-hmD5KsK9v3loYNiB3xdYenUToEwfQ0a1_rKY-0KCk2Ipo1A8OUz_C4FLZ0iTQGb8n6V02GbmczLGX3CVwQGLtEVRrVtTJ5bMj0UDF5mhyn5XZKKwjVoJDMM8Xc7xRovF9gaPWk3OikuIT5-f6XLrgWFSN0NDk_U7cmITL7O1c9mIMXvqMNZPyKhezTm5hoareJJH5CBAe63xiQZYSfI8FZybfINggz86LfxVnZzgb0VOfo7eg7xm7uVF51OYaXjuHXlnuSw2zMgxA-UgPMLEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
همایش بین‌المللی امام خامنه‌ای رهبر جاویدان مقاومت
عکس:
زینب حمزه لویی
@Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/446722" target="_blank">📅 17:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446721">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d664908bc4.mp4?token=LCz0_Gora7MMGlcl0RIJCtoIwmtxjd_o3NQWS2gw-rvA3HEyzZh7qkLK13hH3NizvU9TOLHtHXhoyloyiXSh7yC4EANaKN-pXuioIOcKHdi4koOe3KO5kbyRHQk_MfdIEIwbvXDZTarV-KrtzVPMrvulnrk7ZFL3kc9aRo61KupCG-SK9w4TS0wQyF4I_WT5pOf2I2Sl2XPLKJ95egVSiAOqkZG6Dg2GUpUG6Ep4aQZVJyjMZA9Xs1zGx82HJmbOdA0m_S1rOPoAPs3seS7EYxAzhfYWfhBYugnwp8JBH1wS-rsLqwEOMZXHKELTrN1u8fpRUb_d3LSUSraj9ACR2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d664908bc4.mp4?token=LCz0_Gora7MMGlcl0RIJCtoIwmtxjd_o3NQWS2gw-rvA3HEyzZh7qkLK13hH3NizvU9TOLHtHXhoyloyiXSh7yC4EANaKN-pXuioIOcKHdi4koOe3KO5kbyRHQk_MfdIEIwbvXDZTarV-KrtzVPMrvulnrk7ZFL3kc9aRo61KupCG-SK9w4TS0wQyF4I_WT5pOf2I2Sl2XPLKJ95egVSiAOqkZG6Dg2GUpUG6Ep4aQZVJyjMZA9Xs1zGx82HJmbOdA0m_S1rOPoAPs3seS7EYxAzhfYWfhBYugnwp8JBH1wS-rsLqwEOMZXHKELTrN1u8fpRUb_d3LSUSraj9ACR2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احمد نجفی، بازیگر: کدام رهبر یا مسئولی در جهان، مثل رهبر شهید ما با علاقه و دقت با اهل سینما و هنر تعامل داشتند؟
🔹
هدف ایشان ترویج فرهنگ و هنر در جامعه ایران بود.
@Farsna</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/446721" target="_blank">📅 17:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446720">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a15bb4eea1.mp4?token=R51vfp-ve6jhnFk0mGIzxwZCD-p5f3_tJOQT4J2ga0MwYAd4k4aBKDYw__nDyMR6BDdFd8f79BaZKYjDCyd3VgWXmQ5jqOlnNGx1edQLRoXlYsLc218CvGAFJuhOCkHYss8jGEuH-weNnCxUmu_WdQdab_0q6RFO22b4hgp2euTNdDhU_M52by6-VzVG81nZLTxLGb5yjYZxm0YZ-gwA2FstOOHEYkqXEeMK4SRVubP12JlHyr2K68l5hUbfQDqgY3HFrGOzEYl-7b3jVrdRYrZ_CeAvy8cAwcJVFy6Ky1B2Hr1qlEVP0CMY6SI2FgWJseowtQZp3YTssuvBojC6hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a15bb4eea1.mp4?token=R51vfp-ve6jhnFk0mGIzxwZCD-p5f3_tJOQT4J2ga0MwYAd4k4aBKDYw__nDyMR6BDdFd8f79BaZKYjDCyd3VgWXmQ5jqOlnNGx1edQLRoXlYsLc218CvGAFJuhOCkHYss8jGEuH-weNnCxUmu_WdQdab_0q6RFO22b4hgp2euTNdDhU_M52by6-VzVG81nZLTxLGb5yjYZxm0YZ-gwA2FstOOHEYkqXEeMK4SRVubP12JlHyr2K68l5hUbfQDqgY3HFrGOzEYl-7b3jVrdRYrZ_CeAvy8cAwcJVFy6Ky1B2Hr1qlEVP0CMY6SI2FgWJseowtQZp3YTssuvBojC6hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دکتر حسن ابوالقاسمی: زندگی رهبر شهید به قدری بدون تشریفات بود که می‌توانستید تمام وسایل خانه ایشان را با یک وانت جا‌به‌جا کنید
🔹
رهبر شهید اجازه کوچک‌ترین فعالیت اقتصادی را به فرزندان خود ندادند.
@Farsna</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/446720" target="_blank">📅 17:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446719">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhYscuKYHtDngjMNVfTy1hNIYoFAxniEJ6hKqH2Byh03aO8JHLIizNVgHbV67ZvHMox197-Dq6aNFoGz_qZIliwfwsUCrX5U7EF2P1bYLVY-IkHt15m60oYRg2x7JuxBrCgX37W2FedyNBZIk3HoS8k9WH8SQlXf6VMUP8FlhHfwFHh8jH3YvxDKy46qCuOwVvOi-Nos7KMa4sKC44aVuxuObE-ex1IvlC9S2UJCX8zz7EtAsT995IR1cUPj5AQRtEuzETVHva0jHlrUO1pkOXFo52DoTpptLuUWwWAG6KrShOYC1h0HWoI9MkCetSpeaJ3GJ8oNyndnHn4XURBo5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استمرار اعمال قدرت سپاه در تنگۀ هرمز
🔹
نقشه‌های منتشرشده از تردد شناورها در تنگۀ هرمز هم‌زمان با حضور نیروی دریایی سپاه، نشان می‌دهد ۸ کشتی از ادامۀ مسیر موسوم به «کریدور عمانی» منصرف شده، یا مسیر خود را به سمت آب‌های تحت مدیریت ایران تغییر داده‌ و یا به‌طور کامل از ادامه حرکت بازگشته‌اند.
🔹
تاکنون هیچ مقام رسمی از ایران، عمان یا منابع بین‌المللی، ادعای تغییر مسیر ۸ کشتی یا ارتباط آن با حضور نیروهای نظامی ایران را به‌طور مستقل تأیید نکرده است و علت دقیق تغییر مسیر احتمالی شناورها نیز به‌صورت رسمی اعلام نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/446719" target="_blank">📅 17:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446718">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🎥
دودَمۀ میثم مطیعی برای خون‌خواهی رهبر شهید: انتقامی مانده است  @farsna</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/farsna/446718" target="_blank">📅 17:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446717">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56a0f3176.mp4?token=T2MldVYgMyZM_xP3y4bjtB-QkDUFFb4-S6p1uMvZtoLfCIl4Rr_QiUZrBETb3nVhD7kqfK6j5OJMqfapmBt748Va7FkyQM7CQvQKgeEDZCPGR5iHrS1FSwgZl5hhP04vnB8VkLyYes1GINOeg0fv--YVTgy6rvyiP-hlA_OeIjBIYbGweEOdLJ_tykX6vYR3aFrKNeBPzvMWGYkHXA7QYApsqide9siOTD14dggcs01SPMu3TuSc_BF5isHxZsZTvQCxPYD36lGIJgrwcd9tYi5bhwm-cKN-3e4WA1OAnlwjTpdc0nrEa_YrA1YWm9L4oJIoBY7fNZFD6_gf1CIEZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56a0f3176.mp4?token=T2MldVYgMyZM_xP3y4bjtB-QkDUFFb4-S6p1uMvZtoLfCIl4Rr_QiUZrBETb3nVhD7kqfK6j5OJMqfapmBt748Va7FkyQM7CQvQKgeEDZCPGR5iHrS1FSwgZl5hhP04vnB8VkLyYes1GINOeg0fv--YVTgy6rvyiP-hlA_OeIjBIYbGweEOdLJ_tykX6vYR3aFrKNeBPzvMWGYkHXA7QYApsqide9siOTD14dggcs01SPMu3TuSc_BF5isHxZsZTvQCxPYD36lGIJgrwcd9tYi5bhwm-cKN-3e4WA1OAnlwjTpdc0nrEa_YrA1YWm9L4oJIoBY7fNZFD6_gf1CIEZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احمد نجفی، بازیگر سینما: سکوت در مقابل شهادت رهبر انقلاب مایۀ ننگ است
🔹
همۀ ما مدیون رهبر شهید انقلاب هستیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/446717" target="_blank">📅 17:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446716">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f42a2a3e.mp4?token=ePshLNGrRIgnTjPzCj7GXXGVuZ5CVKub_EA647W7iqF4oJli1YOvgB9tz3EuiNYYwK2UY0k-02qauZg5c4eAvfqBm5OBMlkI6BiCZpDuQLM9WPizUh-4bo-jZxFja6-XMIY4kZ1gj_y3EhyvBpW7PqHLEa23Bbn8wla9CS4AS3sRW2Up63tUex85UgDpAt7ejnskCL7KCdqegAhy6E2qV4JIfr0Y5fEYTlTYYYrjavhmz5e5Z4ZItDejhC_xnORfhb9hvXktDFzpja78W0JSkXZZGB86QLfpKQ7rFQ12TOGLA9Cm6hKHM3ULgdAIiumaqKOFpYta2svU16pxBntjiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f42a2a3e.mp4?token=ePshLNGrRIgnTjPzCj7GXXGVuZ5CVKub_EA647W7iqF4oJli1YOvgB9tz3EuiNYYwK2UY0k-02qauZg5c4eAvfqBm5OBMlkI6BiCZpDuQLM9WPizUh-4bo-jZxFja6-XMIY4kZ1gj_y3EhyvBpW7PqHLEa23Bbn8wla9CS4AS3sRW2Up63tUex85UgDpAt7ejnskCL7KCdqegAhy6E2qV4JIfr0Y5fEYTlTYYYrjavhmz5e5Z4ZItDejhC_xnORfhb9hvXktDFzpja78W0JSkXZZGB86QLfpKQ7rFQ12TOGLA9Cm6hKHM3ULgdAIiumaqKOFpYta2svU16pxBntjiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محسن محمدی‌پناه، مداح نماهنگ «باید برخاست»: مردم در تشییع فریاد می‌زنند که باید برای خون‌خواهی و انتقام رهبر شهید برخاست
@Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/446716" target="_blank">📅 17:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446715">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qs5ZfikQUh897QisrcM8pzWW2yP_mjnlRXhJ_2gBFgw1I_KTaL9NQZO4a_LtgJZ8Z-VjAQZWXMveqnHV9oWnOqnUBAOSbN7qqaje5Ab13DRPdSVtt2ohfCvs_nkrNfNnWze1-mJFNG_zkdYbPJ-ktok3YCWDqI0mJ31QZI0mwyEx30hlgqtdDXqYw4lwQ9R5pteO500uXpHShDffTtzPJ9WApzhSVcyAMyMdjba9EkkAopEjHLg4IJ2KEIwEU5rEwh56vlpIBvPYxU5Elj56Qx4mUskj-Sv7yvVkCcnmb6J6x1NzBNLbWDm8OQ5WoLVegqhpqS8RSoWyqJbk1gKUSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
زهرای من به‌فدای زهرای رهبر
🔹
قاب به‌یاد ماندنی از مراسم ودای آقای شهید ایران در مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/446715" target="_blank">📅 17:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446714">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b5a07723.mp4?token=bSaXeDUjtmBtdPoSpPhvIkCnoTXBPFPTcx-P_K92BceTQXcxfGnvG60hPHasjxw8JFZ1KUaEGZ-jI-y8YRimanv5SQHsSz5Y_Vdb0ahylAfInc1gYnGwFvjUJOvLjhuLxgwpFEA3i2ejOjM4qR6OwbT-OVLbSdeTUH-N5uXZ_eR2B6K0hzB2El7lCaPPHddHINXjC_8GN3HaX8svcG7-cKOsxqz9fKcS_Ax7ICk2ZuscnUkwta31AY136EEiTRbi6m3EkrBcX9ndy-HwYc1wKOFgE5LjHmiIEjc-3lCakD2V0h0TXwjFmzizmdkUvq8lEcscX3PQZOG4A-4yhgqHVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b5a07723.mp4?token=bSaXeDUjtmBtdPoSpPhvIkCnoTXBPFPTcx-P_K92BceTQXcxfGnvG60hPHasjxw8JFZ1KUaEGZ-jI-y8YRimanv5SQHsSz5Y_Vdb0ahylAfInc1gYnGwFvjUJOvLjhuLxgwpFEA3i2ejOjM4qR6OwbT-OVLbSdeTUH-N5uXZ_eR2B6K0hzB2El7lCaPPHddHINXjC_8GN3HaX8svcG7-cKOsxqz9fKcS_Ax7ICk2ZuscnUkwta31AY136EEiTRbi6m3EkrBcX9ndy-HwYc1wKOFgE5LjHmiIEjc-3lCakD2V0h0TXwjFmzizmdkUvq8lEcscX3PQZOG4A-4yhgqHVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان مدیریت بحران: زائران برای هماهنگی اسکان با شمارهٔ ۱۸۱۱ تماس بگیرند.
🔹
زائرسراها آمادگی اسکان بیش از ۳ میلیون زائر را به‌صورت هم‌زمان دارند.
@Farsna</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/446714" target="_blank">📅 17:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446712">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dXG_jf8Mtr2oqP-4CfIv94pf1W-26j4AKA2FVqo1w1N4ZdlJ7oUCkXXRUivD7u1A7sPwNK256u4hWOifspx9iXzvdm1X3sNFt1uPxYIgUA_NetWcivDwPxPRkOTXzBgIlF9kyi_x_5b9xGAAOK3XGiDVFW2rQ_es0_845UL3u6VMJvo7g_TuUZuc-r8QrsvnbCyQJ_mgr_E5rnWOcLXG0twyILAKhp2lqwI87kioEwodwHw9nn9IWOr-JHppmdcViOWjuasr_WcdsRQFY0rRC-BlHrRglWp0PkVQmBAjm-NloshXeTz0GoatuTR0j0Pvlmx6Jd8QRMrfjbrTnA371g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FzGYBGwM9CSjKcw2J7X0XNAOg9jbx6lKpqW4w8soFNLK2PvNR8NPElkYdu3HZfvsKSgZZ3LBvIkX7fwepI_g-yxgopr7bZxRVVpPTAMDWMAYNlLfqUsypF4p_uvoWySgd7ucEwFn4KL6vJhC5r7EmNeIvdOGl0d9nZ9U2ydQlxvFK7-DBm0UEfRzQeHNzoiH3_82RvFnAIBNPGcQNsquqZfxjYqEEXIgNMjTAFmK0s7pTrLm9zxwr0NMrtxTr2c4SPoiT7XnBiZQbuhW3jNaKh3ljkahuBJKuiNoxptDZpdmAcjKgK8OtUf1xoyxS158kJxQsWSBjZr33uvP5Opsfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور مالک باشگاه تراکتور در مراسم وداع با رهبر شهید انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/446712" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446705">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VhDiN65RW51zYKnHaUCm7NkWc-_FLORhuvViij-T7mce_DQoKeAZKmQHl0sNK47ByBXcbe9MYe0ysNsCo12nshxxU17-Tx-nvV1DCP27RnnWgjVPEbDKZjQIyAyohYcVSHnG1zk5LkGoL5ALoXBhnML__LrkvVEtOJZf_nRjoKYpnFkmfB9n4U8VHKu2W8un4E2COEVuK3aSmi-XPRWEPNoBO60t8Nm0pXAoUeiVDC2VkDd3uv6mhjvWxGMV68u4qQ69ZZd_CnMXQlH8lekDKBJYcjoZy94wuIFeA9pVbmCBXMB39mA6bHSMKQpX4OfQhcd3fCOUj74tycD43wY8LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YFoI_6jqNKLNugtVUxbVDnNIBjZRqlfdloKZgkL1FoNwNzK7SAExFFKRw2Hwzxcb-IM5olWgU8i-00XjkWg6K3COz-gwtGUJM_8Mb2UrK3Zu9DK0088r5wM8ci7a2syDBS_p8GwWTvvWtTFf_kNpRz1yN0iaLH7UxrNU-L_uAr-agE1YigLLB0XT3PtCE2G3tCBuCAbekaRUWAiSXs3bxMVFrpCVdbfYzoo_ivoNVkfzgqILpaJaupz52mozRxaPRx_Jqg14LQuJ0BYOWOyOGk29q1GOV_yDYUGa0Zzgt5SC4Lui_qiRezSyWDqSNWuM5hZ7JuISTEzoX4RUnxSnxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U6ElExn6T4sZ-zzXphrYkd1KoA-JwWmXGbybC-ucb6ZYdBM0DTre_WahMN_qHowBRE1Exx7UP17M9R48QjgNLv0dKNxQth5LSYYpKeK8h0nmgQEzUOpl8mrnZ-HJ5eOli_2E-AhtCQBkbSONM4OZuKjGBxQbRrlsQJ-JrDDVSnGQaEiYSnJmaa4oZbJLtplZ8AetgCtPmR12guQS_s8SXnmupjBglUIIR89sbQ5ves2E7ji8yzOqCbGiKJxAbxXbOEwnZGiUZbY7plLfjLeoCAwby0n0L7IG_mxzRVWChjRsbu4YfKt7lkQlyLk4mXXU507pLIXOgqlrwpVMhh9pLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S8xxcIahAgFTiQSVq7fBnmDN0u-4zJZR03Wf4w5AirMGu2I0fL-eo2MIj13chvSyjjfboA1HDu5KfGj_k8TzUegyt7ASbfoXbP2dQFCpNNcVy9KnEkUhbB3C-SOeA383eiSU2P-czzAH10FZb0wIEvRC8eyQJL84w9cU1_gOEyAiMqg_hqVmMcjDdsvudXWbrjNMC6o-Uhce3Huolwhav2aBsHEGbi60UnbbP3taftTsbTaHlB9zhU4X4Rp072bWSmWwDUopUVefzy1Wpc5Ed1mEcBuw_9NUMOsnbLFh1VpPK_afXcKvyTIMo2Ja9jrF9RrWnSpt4PfcrAZrXWhQ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rO8fdZuexROj3iFCZztUKRzu1QXKEg9wLQtBWgYc_lo9FLgNvEkx3e_5YpjWzKqM1vJi39AbV5fqzDyG8j0KyRgiFjfVfoZNZ0UEPClDIBInTCTjtd0zQVmrh1mWUW6hzUg2CfB1N_VOhadQfKhNbWcDYCS3ERGu07Oq6IxuaUUt-R8k7UGTVrxlrVve6GHMlB7Tlf0p2pgt25rLiRaA7dqW__YROh_uxhzHY7n4gfPWmDTGsHf-EvgqB-SEqPRwY1S4JfPbVbzo8-W3tcLoPpXptrUWLf6W5Cu4qlocgVjku61CbpQS7eJhyWSAhmrw8rpojI7qOLPpX_2zSBAykw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QKHqvnVGsIW1VE9AuUlaxNbv_XhUfjvTEmnG_xIzjWd1xKxi1hzi0LmBsDlZZAmJgfl0CQ-xSYOLW_N5aM1OXLfefustTLxzsNODQS2a8UAXEwGLRY2rSAuWtI2xLyEE9kaFqb1GFV7XSlY44UDYCAOoEBhJLXM2sCJUx9wm3a2GasF6fYvMxLMQsVh_pobnWUYdqWKoQSlbL78-vgMrTiMay7hfU_J683CSSv-jHLkMyY8dPMs9gaBdH-p7Q8m8IUHnXj2NqewSiP3y7nMHW6Pht6j7mrXxYnRH4rVzR0xIqPvib75n5HNhsNfBqNovSQr2MaJzNds0J5tGQB1vZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GCImqjRbDi7EqXgc7UtOYrShtfjgAxXwrpfBK4JP1OuFXKPxWaVh7HSQgL9qaMWORtcTfYza7GMoccU3nkAmB6GLXZZBEGD5bK0gHz7EfQXqb0Q7OOnCe6_GojL56rDtmRqCnAOieTPnbcBApY8qkJfw9HMC35dZOlrtz20TJeO630KcUwbsqb4sa8O8krdl_3b11yDHK9kXZMurpS8yH3Oorca5Sc8jTBvbBmP49O4qXzVpFf4DOKbXG50h2h4tNM4uW7BQrxXNlF9uiH8Msn7LDblfk05EydovMtwMBfreoutXMSUdEr5i2qIe3nrvquNw9vJ-WBpsAvmuKce0NA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
خانوادهٔ شهدای میناب برای وداع با پیکر رهبر شهید انقلاب به تهران رسیدند  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/446705" target="_blank">📅 17:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446704">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkIXe81zXhQUKbXKyvdiHzY_3f3Xo9W2XnBOq31h1nQjAUL2o8Rd7SauC16A0YFNAcZfCTGcyXLJMBoPQnyiR4j3E6OQggXRprdDtrz_nYjs9RSzGiImM0Z-lF8YYE9Q5x0RqKbbONizam_yBR3WK1R1zgYKOSPIRD5AYtAHSbMEQkJu2UjuTYKrlnd5lRywrQAVrf3D2EWbLyQ3fF2w2XAyU-FFR7rpKj0OgKnYm6DS9S_-esTNHQmmtdEIPUnvCY1KikNE9WSjC2JMQ4niy_WRu8J9tvXsQUAGhsdpk4uFjXLRdwlXOPweD26ddREJ-5Pejifj3DWvk2alvHISGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لغو سفر وزیر صهیونیست به نیویورک از ترس بازداشت
🔹
هاآرتص: وزیر امنیت داخلی اسرائیل، سفر برنامه‌ریزی‌شدهٔ خود به نیویورک برای شرکت در اجلاس رؤسای پلیس سازمان ملل را پس از اعلام برگزاری اعتراضات و درخواست گروه‌های حقوق بشری برای تحقیق و بازداشت او لغو کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/446704" target="_blank">📅 17:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446703">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🎥
خوشا به حال کهنه عاشقایی که رفتن و داغ تو رو ندیدن
🔹
نوحه‌خوانی میثم مطیعی در مراسم بدرقۀ آقای شهید ایران  @Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/446703" target="_blank">📅 17:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446696">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VwgElRaGyTuYx_c2o0qxImPxL0DPsFnTEF10iKtpHkyrOV5U6sstMoufZk6QL22lYAsxqO41AkUdDJMO14jPrPInldvuRmW2Bln5qCQaAALhtzNpmSve8W92TM0EFeDRyu2S_-3JBlniHhVSdtxs2vP9GOPbcLk0MxUvdsfFSoJwex0TtiwMLnwTm8FLvjzTfSWKYdZwYKlwbyczKkJq66Ydo5Aqc8cgnTJdHZ-QDngBOBsNGP42_6VMcskK1UPlr9Z88PzZce375oP5f60klLeCzBMa4OmaDLK9sc3YsE727V3jhHj16kNJI1zBphMMUo2VWum5cSfJjOhvZWVP6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EuLmJC__wW2O8aD2Ck1ailZNzlJk_4ir85jKKdQ5wYe3YRN7Unkwq8J-FzXaiBzc0CU1BjNfukM-onqImTBqWEcM-OgMSnj6b9Ife_ZUyN9PsG_5HqM9qPtIBx5445zjr-8L5Xg8ybRPM8DbOQQQ1mIdxZ7srrWGSXFqyGMg5tN18lA43pYx5WrAbqjgfO8JrKEvXe2EP27vqe5NikZt_jfyE4ujsTw0EHQ79SwGov5CrKxJZwmeEfnkObWhIK_pK27ENapnxLYhmsuL7Qn-nFYgCqm9cWceEd4Bye8WY5yv8WiHMtjV07S1l5kWNKUKSKVe7QMzCT7Q-wTPfpBS6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h94Wq8xqwyBNpehH2MQ7do9qWs-c43luj2zMTBBwxkd9IMiIxSZDapaiFc2nU4qRyrnwKrojMLhRIE3FHMIvUd0v2v7lfcUAl8pJ-a19N9qztnW74gr2lmhsTi_tO8B7Wb3hWZ6agVGDtVlGvS2rZdyLw9Z4C1K6pxEBXcYBZfWgk4SpAL3dh85W5h379ZgC5ZRQzb9HymRMrRONHW9_CggWh3g1PH1iOTvGrtrWxiHgs5GifFugTemNf34Hq2wauQe0VxM55x4lgdrGBmya2gqIP7HHJpy3WwO8iyllKjlahS44BowMDBltldLvltCmjtW7Z2sWRiyh3I01M040hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VVtNPA5JIe4GiTdl__afw0Q3Z4lQKlX1fKJ_TmPe4-YxjOy7xt7-zwualF7lMOrEOW4k2avC4AsE6fPjxwxnuhvSu-hLLHo09KUIFqHNaNnKPqUdmCuV3wVKhBQRA0oi8kDmQK3ihZEQ9rv10wfazUmfIsdyEDBf6Z0Qi9yZcYYuhq-Wa8gA6zwINrWCMksWbIEM_ucE1Frf9z37vGqVKdudIlMBUF-xcpJJihlxYHvTsbNh6ibXb-5eyhdehqu2FBCXeTqSpTrWzdG3koIhHpsy11j5Sg3mQl9D5ujV-DseAbi7bTAeMp1RdXDV5iDD9N0MgLAzNbLXZIyNp4UCjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/heNXbCcA2Scq_QEen5J22Foht8QWpHXuOvETJnznaI71YHEwXB3bNh_ZY1TYNICKL8Yewh_JQKqk7Xm3JSabbdX6AVtoqovKMwKPLqs_sOkl5hD1WMc_qdYe6tbbRdwVdGdkEbXqYcZ2b39HcUZQldTjdQzo6-HzZE1iyGKaEtvESiiEEoSKHtZoTIu59lKzzXZkm41-bFRYwBeJkKEid4jgDwArmn-S1ZjauDgteC2fQURoeCgETTaK4AKzz6ML3HhsNWj0GIBPb2TNDoWufOXhufsU8-KPV7iRv57cop9K4VeE0_p3tE42dr2WceVpM9u37BlFSJaK8opha2edfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nn8Xi2eL8Ox3fxv9qvnbcrrUxXpMSfLQ0BqwlMhpEwSAFFNQr00pyZZi82_itgQm5oajhIa2xQUWAetS83SFpo5iMUYGjIWKY3doMsg2y-kmUNag8-oo5dAtpbOvgv5XhtsPTugytITF5boBSCQOR8i0-LpSBAYZyQvQ6AQmxFha7ORJc-ArmByDCi8JxX65XZR7vSyuATgkpS3I8owK_fYFHfi0C0UMYOMaPzsoNuLxpAhh-ybYjqfUAZ_6GknFrSKihHA-mIpukIRs_xrk-L3xqBP57rbiw_2QWCYa69EuNjlaWuROLLmnbDN3pVK1-kWqRub78InmbQiWrHHYHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cBVWXEQ6l4BGwtR34dFXGbQZjJpEA7qX6aqu6-Xb8jOGuNVQ1giV6L77niHWo9rf4NZGGqH1OyxFtkJutCCQwPBsq8zLTjNxNsIapf9YoGfnt26RONO7tZxvNaKUJHl238LjUhnLFdFsXcLEwbUlJd1DddgrcHNbMc8Xw5mDCBKZnHMaIUM3pDeVPDbsfjnSv0in841b-A90wO9piyWMfT9fZSAVZvVzRtuUg5Xjy5iGxqhwNEiO2lm35gK2ZiaK9uObzpx6X4TNCo4sps_DK39sQ3Y0qTBxrvHYlHEDrntPkFs6XvToSuSTb4KrA_RCiLRVxOdVtthwSRKsIObLVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
خیل عاشقان در آیین وداع با رهبر شهید انقلاب
عکس:
عادل عزیزی
@Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/446696" target="_blank">📅 17:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446695">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5954bb030e.mp4?token=MSJd7G8d_ypYGgkIqQ9e-2dT8LavS7taPPmllGGQs8ihC2Fzfrh-k92V7m6Bv8SZFDiOkHjFKkAcw8R_GXgWwxBw0XranPFhmgAJmqtgOmdb6sHne2ovSUqUrcXbrZdEzPv1tCrWF8RxR6t8UiPZ7u01pussYjPKvSej5y6_70UfzYNJ-tUwxzRjCoqs8sHx6i6EZG1Sv06tvnbVPpRwkCmabcvu8HUjOkFdsnl1sba4cirMKEDfP6o4WDP2H3dPjevLkmEs44IODIEF5KbkpPV1ZJaeXzY_MY-EOgU2beLBaQD2pGrL8QlB_6kMZdk51gLhbV8nS4XXyBTOO25hGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5954bb030e.mp4?token=MSJd7G8d_ypYGgkIqQ9e-2dT8LavS7taPPmllGGQs8ihC2Fzfrh-k92V7m6Bv8SZFDiOkHjFKkAcw8R_GXgWwxBw0XranPFhmgAJmqtgOmdb6sHne2ovSUqUrcXbrZdEzPv1tCrWF8RxR6t8UiPZ7u01pussYjPKvSej5y6_70UfzYNJ-tUwxzRjCoqs8sHx6i6EZG1Sv06tvnbVPpRwkCmabcvu8HUjOkFdsnl1sba4cirMKEDfP6o4WDP2H3dPjevLkmEs44IODIEF5KbkpPV1ZJaeXzY_MY-EOgU2beLBaQD2pGrL8QlB_6kMZdk51gLhbV8nS4XXyBTOO25hGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: خودمان را برای تشییع ۱۰-۱۲ ساعته در تهران آماده کرده‌ایم
🔹
در روز تشییع از هر نقطۀ ابتدایی که بتوانیم خودروی حامل پیکر را وارد جمعیت می‌کنیم. برنامه‌ریزی شده که تا میدان آزادی و حتی پس از آن، تشییع انجام شود. @Farsna</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/446695" target="_blank">📅 17:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446694">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🎥
از پیشمون میری آقا خدانگهدار
🔹
مداحی امین قدیم در مراسم وداع با آقای شهید ایران @Farsna</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/446694" target="_blank">📅 16:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446693">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/083dab9558.mp4?token=EQ-f__rNsxaXCyE-a1uBJPqMqOJmWURomqLCQgEKtW17e3KJsUkJOPAivF9aAOaeDsOsyAtQMgIhuva2N41kcY1hfFoxIOfO-fIw86d7n0lg6YFqpVH0e3-zJhz_RhNoU0AXRlWHx3zT1feZ_DfS9fT3ENBeoJqn1QyHVlUc_rRAgudcZSfBSuJgkzwyEVs8FnFENJS1yTjS4jCQiaz50TcesRjCy3RA8UoWgRDQfll3rFVu6ZLVfCe2Am8R7hGPewCcIebsNargwwE11xKyEJsSWhGL5h_ReCasX-EEeEQ2amHXhHXYmuCHVpdCUleeTvRByqxoVNwsvaqMLSqrLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/083dab9558.mp4?token=EQ-f__rNsxaXCyE-a1uBJPqMqOJmWURomqLCQgEKtW17e3KJsUkJOPAivF9aAOaeDsOsyAtQMgIhuva2N41kcY1hfFoxIOfO-fIw86d7n0lg6YFqpVH0e3-zJhz_RhNoU0AXRlWHx3zT1feZ_DfS9fT3ENBeoJqn1QyHVlUc_rRAgudcZSfBSuJgkzwyEVs8FnFENJS1yTjS4jCQiaz50TcesRjCy3RA8UoWgRDQfll3rFVu6ZLVfCe2Am8R7hGPewCcIebsNargwwE11xKyEJsSWhGL5h_ReCasX-EEeEQ2amHXhHXYmuCHVpdCUleeTvRByqxoVNwsvaqMLSqrLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن زاده: از ساعت ۲۱ امشب تا نماز صبح ویژه برنامۀ وداع در مصلی برگزار می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/446693" target="_blank">📅 16:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446689">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SnB99oFhMdL-IRiW8JDMSXdNBfhqqBENq0wH0a_mUq8uQNjMxmUmh3ve2i3trvwnR2JM9dmcINKcQ9vSOCfFJ-UL2eb323ciUf9dh-ofo4a5F6S7TD0CGqC6bxnjODFaaGcLCLfLvmhCgqruI86mLcm3xae2HDqQqrnAIyFRdn96Iyrv8Er8BvJNsSLbiaTlYgXaqavlQKrABUgvGXktvsNTfXRJNGXfSzbFt711vuFPKgc14lplfsdxTN9aIiUTjeTGaG1nhI4LHpma4YrMqBU0XMkESI_h0y6rpbgWotbekA0oCy7jO0TJrgnpQL1kGUvyNRZxy0MCqRbkYy7BUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RjyMU1uQUwkim8bTqZI57NxG89tM-R-HfOqlFuz18yq5Xt8gTZ1Hhes89K4WzB2y3X1En4U7jyP8TevJ7Qnvl1bPJHMLXm22ibxvaWWT54kaGusvadjZGY8zCTTx2mH1YNtGQuLdb04ebM4TtMNtarlVHijSvVUuJbiWhvDDpUMTggbBF4Lm1qo1xhEWKk5CwL6HDlGHnUHlg1CogCc1e6DlrnW_LTkRy3jLtxN5VaJEPNyBiPIKrDjG6JL7cm_SQLwG0WrRdqNt6epWT8kUHr8LByT1OuAH656dYJeIiNfWnsyh-eVCOGD90Ce4XFk1jCFKzVtrMRbD2XOJy4hwoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oPu_Olky_6VGyf3wenIlzdIVVEvKAjpzOOPneDGSSwQC3pUEhZQ5nTZUWwu4YQw3vqSOdv-XlYqhHwUpzEtpu_x_NxTnrGjeBmaT-yJAq8TF4hR2Us44EGccCmutG6suovdFd9HkviCOHS-KTXjAFrgIV6mHHZHNMvWszl2PGKuIbKEe6hTIiZCl04IB4Cl3aWOzgWJpgUQgqbLWDCFGoXkOlj4ISDsnFjuW9OP0jQk7-UjiaY5uBqwx_E9RsTZ99jOJnl-KxqcVJeuMZllm3qBc07inY-yfRoOeHMAc12fptojpVqgtyVCPE_vOddLg7TkbtcPdRt23oOCHZjROig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W2V3DODu8-sqKb4Y6D4Kg8iVSQ1dFz2Jcag3cyr9iRHKw4p7q6Z-NwsYdNL9ENMgPSS3BhBw0XP3l-f4b7v-kKuPYJrc7EQVoANMtdKb3KyQoqbKYYTeVWHbkiAdk6jDO-7aQ9zOlVdSKmKj0v5TwNWRC7e9htkBK0FuDfEbdJAII9CEaNqO1KuFoOQYq-945hZ_uubfmSb9yNlOP26le1lXmq2qO3jyZQpr6Uw198O0s50CdABe2TbJRV807mCHI5bP08h3pOI_LxnpWv5g31ihnRGXpoULs-PB6L4goeCY8PcolbEmJO6fobhZtUmdGKp2mWndk7qJAaIczk6Ezw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اعضای شورای رهبری حماس و نمایندگان حزب‌الله با عراقچی دیدار کردند
@Farsna</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/446689" target="_blank">📅 16:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446688">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7a8773584.mp4?token=e-0y8ODaLrJGxwa8flI1ASGQhvfDzrqeToLXCemcy2f42YTJSmo3AU0k9Bx6gC6XBEN4uS85JBa1KDyxIzjNt1u7qnaAfNog8tt8iGCQ3ezq9-d4r1oXNRgEuqr0m6qUpOms5PiGb4bqAU3NdNC5xGYmXQcOxXokA4z8CRRWOH97Mumqyb6O_PMPxX-WY2adu-LvLoFOvjJxhwo9Fwze1P3mhU-MBnHthb5eoeHeArRUbgrXDQtzKQlVgTzkjOUrmufvPOzMKWwS9fQXW87agV7f5NXbvp_6_y90hYkjNiULenUgKfwSQLSjvGwcW03HN73x6DOzx_fa3PvvdwjekQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7a8773584.mp4?token=e-0y8ODaLrJGxwa8flI1ASGQhvfDzrqeToLXCemcy2f42YTJSmo3AU0k9Bx6gC6XBEN4uS85JBa1KDyxIzjNt1u7qnaAfNog8tt8iGCQ3ezq9-d4r1oXNRgEuqr0m6qUpOms5PiGb4bqAU3NdNC5xGYmXQcOxXokA4z8CRRWOH97Mumqyb6O_PMPxX-WY2adu-LvLoFOvjJxhwo9Fwze1P3mhU-MBnHthb5eoeHeArRUbgrXDQtzKQlVgTzkjOUrmufvPOzMKWwS9fQXW87agV7f5NXbvp_6_y90hYkjNiULenUgKfwSQLSjvGwcW03HN73x6DOzx_fa3PvvdwjekQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: قبل از هر نماز صدای رهبر شهید در مصلی پخش می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/446688" target="_blank">📅 16:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446687">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/073eade277.mp4?token=arH1f1aaJQEm6xoMzclMRnVU7rq9y0E9963RfASsk_n5MsP8xASmgW853P36lediTGhGwElZfpNUAfqWLbQwU0ZoXmhQTGN65zL5s77ppLzsugesYWXqT5pqQScGc2s11BR_xkyicIBztlp1No4RgIVYGgAsI0HH7RVbaTLR69lqHd-8INslRPi6PiQGNQatQUVXNRRoK-RpNbsSzynfmSlCcvR21q6jhdjBArQywu8t2kPiFjOr6yC1XgswALK570VW1BLQptK7uTkT69BmFtJsudpS1RkNJv2gZ7qfQUFSrqpGRMLYdDLV8Hzu4EmIcMR3Hct8o38XXDOn_geZ6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/073eade277.mp4?token=arH1f1aaJQEm6xoMzclMRnVU7rq9y0E9963RfASsk_n5MsP8xASmgW853P36lediTGhGwElZfpNUAfqWLbQwU0ZoXmhQTGN65zL5s77ppLzsugesYWXqT5pqQScGc2s11BR_xkyicIBztlp1No4RgIVYGgAsI0HH7RVbaTLR69lqHd-8INslRPi6PiQGNQatQUVXNRRoK-RpNbsSzynfmSlCcvR21q6jhdjBArQywu8t2kPiFjOr6yC1XgswALK570VW1BLQptK7uTkT69BmFtJsudpS1RkNJv2gZ7qfQUFSrqpGRMLYdDLV8Hzu4EmIcMR3Hct8o38XXDOn_geZ6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: قبل از هر نماز صدای رهبر شهید در مصلی پخش می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/446687" target="_blank">📅 16:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446686">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOBUh6H_33FZgCpNqZ57bwsd7-KGVSg7vz5ODCduvfyIH7KWZYoopQKHGR-r7tGw7R7SNl2mgOlj5YQs8CHfP5Fo43qjTuF8HdidCq7yf0KttVWPGXg99RHbiwM2kQluW4qcBKRJULAL0_ZLRyMsiQuTCLnX_NsnkEas9yw8OZx7Jjz0DNiLoJmUr43O0X9TsDHjuZQgB3lq1hEI65fowAv6MBkGDrY2X850kifx_e85h-b-vsWIqGlC-PCbos8pcC4DS0G85ziIgraXk91ssKCsZPQXSQ2ZRBdhXb_TwkldpkNgfgez26xI322oigdZvpynABMuOoo1uIlq9JCz7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهرداری تهران: از ساعت ۵:۳۰ تا ۱۵ امروز بیش از ۲ میلیون و ۲۰۰ هزار زائر توسط متروی پایتخت جابه‌جا شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/446686" target="_blank">📅 16:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446685">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اگر در مراسم وداع و تشییع وسیله‌ای پیدا کردید، این کار را انجام دهید
🔹
شرکت ملی پست اعلام کرد افرادی که در مراسم وداع و تشییع رهبر شهید انقلاب وسیله‌ای پیدا می‌کنند، می‌توانند آن را به نزدیک‌ترین صندوق پستی یا دفتر پذیرش پست تحویل دهند تا پس از ثبت اطلاعات، فرآیند شناسایی مالک و بازگرداندن آن آغاز شود.
🔹
همچنین کسانی که در جریان مراسم وسیله‌ای را گم کرده‌اند، می‌توانند با مراجعه به سامانۀ «پست‌یافته» اقلام مفقودی خود را جست‌وجو و پیگیری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/446685" target="_blank">📅 16:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446684">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b76fa05d.mp4?token=WU_I6xA7N9DVhVL89brp7VRbcnO4y9CQOEaVi2ujrlQ0wG--v6jpSEs0pTaq3rgOoRUM9TjR4ojXZry-oKY1IW5Od6F1jfpGygIv9ajNNyLyqPKtZvz4vJPLF3E6q-ZPAVm3-RK9xxi_JbGs10f-HhyGiO_NjnEyG-RZbrQ3d0Hz15WBz72PyptcEuomyS1fspmU1RAAbCKLIyR7NKDZt7LUchhALsnS5wJcPMUIvelAy6zBNcXQdlHoVxSMVLCgFCjn9N5JXytqpOoQp37QW1ZsuX6bjTtlkWkzl1Ad4Z_eAk7wZXOEcHu-fLpXBnryqAWOkqwYAkHgqCZOpCrBGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b76fa05d.mp4?token=WU_I6xA7N9DVhVL89brp7VRbcnO4y9CQOEaVi2ujrlQ0wG--v6jpSEs0pTaq3rgOoRUM9TjR4ojXZry-oKY1IW5Od6F1jfpGygIv9ajNNyLyqPKtZvz4vJPLF3E6q-ZPAVm3-RK9xxi_JbGs10f-HhyGiO_NjnEyG-RZbrQ3d0Hz15WBz72PyptcEuomyS1fspmU1RAAbCKLIyR7NKDZt7LUchhALsnS5wJcPMUIvelAy6zBNcXQdlHoVxSMVLCgFCjn9N5JXytqpOoQp37QW1ZsuX6bjTtlkWkzl1Ad4Z_eAk7wZXOEcHu-fLpXBnryqAWOkqwYAkHgqCZOpCrBGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم اقامهٔ نماز بر پیکر امام مجاهد شهید و شهدای خانوادهٔ ایشان، فردا ساعت ۶ صبح در مصلای امام خمینی(ره) تهران برگزار می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/446684" target="_blank">📅 16:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446683">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/875ec359dd.mp4?token=U3bSDVDtpztmnadvWsmy7-rL5my2Pc5-mqBbVYCjBIbnJtPPtT9Y83L1XSp7RJCjcguD3Oi6Bnrnp0GG8PcGEiEXEbafVLyH_HXws-NB2A3D51ityGIv-IIpq9_cEY0Vg3BXnirg7KybRLPrA4TMmkS-TDVNkpxPP7ZlTMdarUAijHDsTi7lu_ZRacDuBZsvr-gFjtP4r_uXnve27DbXyjcdVB1-DQeINvoXnDO7clmWYG2ee70psk7hr2i0lYO4CxXl-yEHU-VhTUJ4bXOAhwukM_RTkrPdDaaF0Y6JydBWAdZTLqcL41LTkYgtGFXGtVPKUTm1iBLUcnDwhN2Cul6uOb70xKqVGWXx_sjyQ76dw4V-8BVtnhVqvx4eJvylzF7gwLu5maAgRXDVDihOeqNQRIT1gZL_z1UZ7WHl3F6QhtxYfhxpjxRmt65S4PeVc_e82JXn3kgCop90_XTN5n7bTXs3_hcGYshA7BnZ-IR8gu13SwHnOz9fvk56YpeBqkkwQRobMuShRmwu0tzdX7arB7zep9uXB_jscoZrHJRMfXlcV9tdmPPIvhEdMWGfYeLEQ04ewyrJUsW6egmvDR6O57cTtdVQKP6bn16RYLuLYpwvsnfGUF4OhMxFTTtKWGllvoa5rZ8OG6J9NAlLSbkzNi1tMdFkby4sfL2YAiE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/875ec359dd.mp4?token=U3bSDVDtpztmnadvWsmy7-rL5my2Pc5-mqBbVYCjBIbnJtPPtT9Y83L1XSp7RJCjcguD3Oi6Bnrnp0GG8PcGEiEXEbafVLyH_HXws-NB2A3D51ityGIv-IIpq9_cEY0Vg3BXnirg7KybRLPrA4TMmkS-TDVNkpxPP7ZlTMdarUAijHDsTi7lu_ZRacDuBZsvr-gFjtP4r_uXnve27DbXyjcdVB1-DQeINvoXnDO7clmWYG2ee70psk7hr2i0lYO4CxXl-yEHU-VhTUJ4bXOAhwukM_RTkrPdDaaF0Y6JydBWAdZTLqcL41LTkYgtGFXGtVPKUTm1iBLUcnDwhN2Cul6uOb70xKqVGWXx_sjyQ76dw4V-8BVtnhVqvx4eJvylzF7gwLu5maAgRXDVDihOeqNQRIT1gZL_z1UZ7WHl3F6QhtxYfhxpjxRmt65S4PeVc_e82JXn3kgCop90_XTN5n7bTXs3_hcGYshA7BnZ-IR8gu13SwHnOz9fvk56YpeBqkkwQRobMuShRmwu0tzdX7arB7zep9uXB_jscoZrHJRMfXlcV9tdmPPIvhEdMWGfYeLEQ04ewyrJUsW6egmvDR6O57cTtdVQKP6bn16RYLuLYpwvsnfGUF4OhMxFTTtKWGllvoa5rZ8OG6J9NAlLSbkzNi1tMdFkby4sfL2YAiE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◾️
ملت ایران جفا نخواهد کرد
◾️
دقیقه‌ای پسرت را رها نخواهد کرد
🔹
شعرخوانی حنیف طاهری در مصلای امام خمینی(ره) تهران
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/446683" target="_blank">📅 16:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446682">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ze2XfkVwL1pfZWfFSfuBaM1mUG-qJ2ZM5NCy5gNx9Z7APyb7ZY2ah9lkOzmXsgjS7aKnS3lMAU9zS2WRAmjVnQuVyni70R3zcO6_LeOTedkSVmJAxvJKrGO_pt102avw0eFjHE5nEzL2Z_Jr3bcPFstdCgk_esgo-Q1yEldZSGWhMfB63E5Ttm1u836EJGEOpnpQuoKbG24JwuexdDt35g4SpkxgCKEAzR-O7-6cMbL1rPGj5Wnb7oVZXlppvcAppW30swDMKauiH_-dD3gZ4DfUo-K9nc2lRLB5lXum-1SGCe1ZHBVgG8TsM69S-Q_JDBMAHkVrwCkApV-duk70cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: پرچمی که قائد شهید برای برافراشته ماندنش مجاهدت کرد بر زمین نخواهد ماند
🔹
ملت بزرگ ایران با قلب‌هایی مالامال از اندوه و اراده‌هایی آکنده از امید، ثابت خواهند کرد پرچمی که قائد شهید برای برافراشته ماندنش مجاهدت کرد بر زمین نخواهد ماند.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/446682" target="_blank">📅 16:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446681">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBe3isIq6Eqk11cGjZ8y70bIRVwyBC89_Y3skBRpoJ_FOxDMoZDQ939xs3EvTLlZNNMyDLsGToBc8dsCYl7HkPrbIhCNJQZd-M5QKpr8A18MQ235D2VLMK5WPej41pzuZ5XsCW1XPs3s93fviLzxXoUSEZxGf2cBXcl_PEHfuk-mCQNBmeLrs-KYPzRQAQl_0Cyo0gfmSVF0d_yIq2z7T2h-GV26sjHOvlUFJieqMDI1-CibvYr5y7b8ySU09BuvLJvjhe3AQnOWh5wJRzBr4QN0VV6Dlq1HPoqR5KefaQTkxtxYRkNj6n9DC0q-Oxn2haaabtpndHnCOz3UHYhAiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما همه در داغ تو خوش‌زخم شدیم
🔹
در روزهایی که دل‌ها داغدار است، گفت‌وگوی پیش از شهادت «علی‌ آقا خوش‌لفظ» با رهبر انقلاب، حال‌وهوای امروز را روایت می‌کند؛ گویی این کلمات برای همین روزها مانده بود.
🔹
پیش‌ترها که شهید خوش‌لفظ در ولولهٔ بی‌قراری و ملاقات خاصه گفته بود «یک چیزی بگویید که ما آرام شویم» آقا گفته بود، «آرام باشید. این چیزهایی که شما می‌بینید، این‌ها حوادث طبیعی یک راه دشوار به‌سمت قلّه است...»
🔗
جزئیات این گفت‌وگوی شنیدنی با رهبر شهید را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/446681" target="_blank">📅 16:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446680">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
یکشنبه ۱۴ تیر در سراسر کشور تعطیل اعلام شد
🔹
هیئت دولت با هدف تسهیل حضور گستردۀ مردم در مراسم وداع و تشییع رهبر شهید انقلاب اسلامی، روز یکشنبه ۱۴ تیرماه را در سراسر کشور تعطیل رسمی اعلام کرد.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/446680" target="_blank">📅 16:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446679">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انهدام ۴ هستهٔ تروریستی در جنوب‌شرق کشور
🔹
وزارت اطلاعات از شناسایی و انهدام ۴ هستهٔ سازمان‌یافتۀ گروهک‌های تروریستی-تکفیری وابسته به سرویس‌های جاسوسی آمریکا و رژیم صهیونیستی خبر داد.
🔹
در چند عملیات مشترک با سپاه پاسداران و فراجا در شهرستان‌های زاهدان، چابهار، ایرانشهر، خاش و تفتان، ۵ نفر از اعضای اصلی تیم‌های عملیاتی دستگیر و ۲ تروریست نیز در درگیری مسلحانه به هلاکت رسیدند.
🔹
همچنین یک هستۀ عملیاتی ۵ نفرۀ دیگر در شهرستان‌های نیک‌شهر و قصرقند که در تیراندازی به سمت یگان‌های نظامی و مراکز قضایی نقش داشت، شناسایی و اعضای آن دستگیر شدند.
🔹
در بازرسی از مخفیگاه این افراد، یک قبضه تیربار گرینوف، ۳ قبضه کلاشینکف، ۱۷ قبضه کلت، انواع نارنجک، ۴ دستگاه بی‌سیم و یک دستگاه استارلینک به همراه مقادیر قابل‌توجهی مهمات کشف و ضبط شد.
🔹
این عناصر پس از آموزش‌های نظامی و انفجاری در خارج از کشور، با هدف انجام عملیات خرابکارانه، ترور و اقدامات تروریستی وارد ایران شده بودند که پیش از هرگونه اقدام، بازداشت و هسته‌های آن‌ها متلاشی شد.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/446679" target="_blank">📅 16:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446678">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIP9UmM_znYmgUWI0m9U85KCeMTSUDJDFH9Kuc7a9EkACbw9dmFsYCnPGVGFmSVA56fL5jW1ZQO-pPpGREQcs-4099uNt3oWMkCyHBoCTwGoI9jasJX1OyXwdxwAHFf2z4Fd8EbZjDMPDjNdSEb_j6o7sWUpchB1aHIlpP3xVW8BHNxLiKpLwakaBPSOSrb77HokosqnB_Lf2SmRoko4-WRGyR9b90qxpMCuZZi0rOuJ1rdm3YTEFf2IstLtmH6_YHTNbJxXDObye_7uNV-eleSvjP5NjlcBAdsje56h-lMiaf1ngXfVy3rgJaf30dN-bdimBxFXkFwwQ8e_Y4Z0GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله جوادی آملی بر پیکر رهبر شهید نماز می‌خواند
🔹
کمیته اطلاع‌رسانی ستاد تشییع رهبر شهید انقلاب در قم: نماز بر پیکر مطهر رهبر شهید انقلاب در شهر قم، توسط آیت‌الله جوادی ‌آملی اقامه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/446678" target="_blank">📅 16:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446677">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXcLKkHzYS2fuT521fqBTMHeGGE8JpI5OyREOkbxO5pT7CxE0PoN2XWxnG4dxhnCdlTh60ljK2Z0i6gJIP9P72tx7hQzaNvvrOn728ohhI5dWJBg1cskPb5xVfEUzW9Lv5OqHoBAwsj1ONCeFHpkHpNnVtUlrcpyAbV8y6NGO0NbTKxLeyhcdYZ4xb0BHT_yj251OBVzf57aJv8YoYpGJ9cNQqNSp18Byt4FilP2oHzfLQHzjc8HK0JGpjweBCEt-CEiYJRgs5eR1AAy-sA5DfAF4buHE8g38IO_3yVxW_WrAyAtPMHRYFTNU-V8TEMAMnwj_YimlOfR9e5ekbE8HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیریت کم‌نظیر در سیل خروشان جمعیت؛ مصلی ۵ نوبت تکمیل و تخلیه شد
🔹
به گزارش خبرنگاران فارس، خیابان‌های اطراف مصلی همچنان مملو از جمعیت است و موکب‌های پذیرایی در نقاط مختلف، پذیرای دلدادگان رهبر شهید هستند.
🔹
گزارش‌های میدانی حاکی از نظم کم‌نظیر در فرآیند ورود و خروج است؛ زائران از درب‌های مشخص وارد شده و در هر ساعت، امکان خروج آسان برای عموم فراهم شده است.
🔹
با وجود گرمای هوا، تاکنون بیش از ۵ برابر ظرفیت اسمی مصلی، جمعیت وارد و خارج شده‌اند و این «رودخانه جاری» همچنان پرشور به مسیر خود ادامه می‌دهد.
🔹
پیش‌بینی می‌شود در ساعات پایانی امروز و با خنک‌شدن هوا، موج تازه‌ای از حضور خانواده‌ها و عاشقان مکتب امام شهید را شاهد باشیم.
🔹
نماز باشکوه میلیونی بر پیکرهای مطهر رهبر شهید، فردا صبح در همین مکان اقامه خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/446677" target="_blank">📅 15:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446669">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🎥
از پیشمون میری آقا خدانگهدار
🔹
مداحی امین قدیم در مراسم وداع با آقای شهید ایران
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/446669" target="_blank">📅 15:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446668">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">معاون بین‌الملل وزارت خارجه: ایران به‌عنوان قدرت مسئول و ضامن امنیت تنگۀ هرمز، نسبت به هر حرکت نظامی خارجی در این آبراه حساس هشدار می‌دهد
🔹
امنیت هرمز با دولت‌های ساحلی است. بحران‌سازان مسئول پیامدهای ماجراجویی خود خواهند بود؛ این هشدار جدی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/446668" target="_blank">📅 15:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446667">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14df82d03b.mp4?token=NImU_nYcs6m8f0JXWPi-50WVVaQF8xIg_lT53aCmo-sDZ20PL3m2IPg4GSOnSgUOLdnfEFOmYUW-LKtmLmq8eEuDHRdTesHdWz-eJO7DtFCQBOwENQ6MA6ZIhA9cJGKjhdD3Y0J1t05oSgi5N41ruhCtK_0WSggkN1G95uLCCr6eZ1AM64XvVrlLexCJPqMNWSNKsCLft-9eJC5_YcrqjE7qOf9f3rAJ369UCuvZD33gHwf5Jum213C4Xsp7aMnLTV42u6qPiGdnKx2gB0ZXEPlIM-dA74epq86Uv6uIU_7RUphKynWrv-9t8mXVYQtqoZrPhwELWxToFIMyjhECbjxa4MY2MGjIPIrzR2WHjHRoIGmzOteXpeWgGfOAOz_saxqSgkbAvD9WDcg0pIYayqk4Nc9aCDIZCX-JY2VzZBt67DxfNbykU2TRib3HBfzL9xb0U5s2TN8UWv7Hbmfg0HvsFHtprQOx3t0JP2sH9oHWGQ-aZY-2-7gqtGFEc2uF3ciZCD6uZRNtgJqjyEPV2CbzYVYVQKumUOtuEVxHFhVFY68D5Wni7mNvWmQ5D2Y6dKlbrHcVI3vCCYI2tA9_lQ_bsVQmNmOEz0j0JMyDUYagVdBmvkVWJq5PsRcCK3pjLifBNAfsSxBtf-LwUrE4Lo4L2pA87HzBnMeyi6QvuKs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14df82d03b.mp4?token=NImU_nYcs6m8f0JXWPi-50WVVaQF8xIg_lT53aCmo-sDZ20PL3m2IPg4GSOnSgUOLdnfEFOmYUW-LKtmLmq8eEuDHRdTesHdWz-eJO7DtFCQBOwENQ6MA6ZIhA9cJGKjhdD3Y0J1t05oSgi5N41ruhCtK_0WSggkN1G95uLCCr6eZ1AM64XvVrlLexCJPqMNWSNKsCLft-9eJC5_YcrqjE7qOf9f3rAJ369UCuvZD33gHwf5Jum213C4Xsp7aMnLTV42u6qPiGdnKx2gB0ZXEPlIM-dA74epq86Uv6uIU_7RUphKynWrv-9t8mXVYQtqoZrPhwELWxToFIMyjhECbjxa4MY2MGjIPIrzR2WHjHRoIGmzOteXpeWgGfOAOz_saxqSgkbAvD9WDcg0pIYayqk4Nc9aCDIZCX-JY2VzZBt67DxfNbykU2TRib3HBfzL9xb0U5s2TN8UWv7Hbmfg0HvsFHtprQOx3t0JP2sH9oHWGQ-aZY-2-7gqtGFEc2uF3ciZCD6uZRNtgJqjyEPV2CbzYVYVQKumUOtuEVxHFhVFY68D5Wni7mNvWmQ5D2Y6dKlbrHcVI3vCCYI2tA9_lQ_bsVQmNmOEz0j0JMyDUYagVdBmvkVWJq5PsRcCK3pjLifBNAfsSxBtf-LwUrE4Lo4L2pA87HzBnMeyi6QvuKs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازدید وزیر اقتصاد از موکب شهدای وزارت امور اقتصادی و دارایی
🔹
مراحل آماده‌سازی موکب شهدای وزارت امور اقتصادی و دارایی برای میزبانی از مراسم وداع رهبر شهید، با حضور سیدعلی مدنی‌زاده وزیر امور اقتصادی و دارایی انجام شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/446667" target="_blank">📅 15:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446666">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک ملی ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSU7S34hVXtCoX8Np8VJDoHDXYGYuvTwkMDZO-Ze6djZ9jG83QcJgE01QnpNVRy34pdu1erQ4GTs4R0rxfdcWyvbHXBd1PozNGsccvUM2ciULuVkEIsX6KnFW2d9mh3-brs3ZkbPDlWgMkov_GXqrLWB745A8kGLyR6J6l0b4Qlebzr__pDQPwrqx-aLoBw6s5LWwNr7lbPBd6NwxPulQYOTNCmiJMM42xv02NOMS37nlD3X5_e-0reXaOcxC32wBoc-S3QpJREEV8eyy6KBTzt1fhr1cl5-YNR2glbEnNn3gP9Tr3axwAFecCDmiPOSix9sPFTvTvWHXGaehc9JaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
آخرین وضعیت خدمات بانک ملی ایران/ دامنه سرویس‌های فعال به‌تدریج در حال گسترش است
⭐️
بانک ملی ایران از ادامه روند پایدارسازی سامانه‌های بانکی خبر داد و اعلام کرد در تازه‌ترین اقدامات، خدماتی از جمله واریز حقوق کارکنان شرکت‌ها و سازمان‌ها، صدور کارت برای برخی حساب‌ها و انتقال وجه از حساب‌های فاقد کارت به فهرست سرویس‌های فعال اضافه شده است.
✅
پس از انجام اقدامات فنی و امنیتی برای بازگرداندن پایداری سامانه‌ها، خدمات بانکی در حوزه‌های پرداخت، انتقال وجه، خدمات شعب و بانکداری غیرحضوری به ‌صورت مرحله‌ای دوباره فعال شده و یا در حال بازگشت است و روند فعال‌سازی سایر خدمات نیز ادامه دارد.
🔗
مشروح خبر...
@bankmelli_ir
| بانک‌ ملی ‌ایران
🌟</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/446666" target="_blank">📅 15:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446665">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/446665" target="_blank">📅 15:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446664">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777a7552b9.mp4?token=e-dGcFLjYcrmr_YmAbYT_eFBGYGbpzAAp2skng3zKv48BmitG-LY6HCkxzDKXK4OGuxYIDocks3R_xKmwIQXccFN1q5z_hxXLuHELWNhGcz0DQGE1VHIBqpBAMYvaCSsvtT2a51DifeL4BP2Ub7hu_bSOGD5o9l1SXCizV0GSKwaacrc75n6SQb7prmxH4O4WdPvaU4BwLzjcA4N6mZg01VFdQiDL0fkbmy5e80emj78MH7WBBpmGonZ_deunGC-Gg3yNliZe3v4v6f1Rq-omK1Y5jUr7i6fQlYahqeJ6DT-fu-D-SM71mVeBk12UH3p9_S7_cQA7I-RbfVvBaUM-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777a7552b9.mp4?token=e-dGcFLjYcrmr_YmAbYT_eFBGYGbpzAAp2skng3zKv48BmitG-LY6HCkxzDKXK4OGuxYIDocks3R_xKmwIQXccFN1q5z_hxXLuHELWNhGcz0DQGE1VHIBqpBAMYvaCSsvtT2a51DifeL4BP2Ub7hu_bSOGD5o9l1SXCizV0GSKwaacrc75n6SQb7prmxH4O4WdPvaU4BwLzjcA4N6mZg01VFdQiDL0fkbmy5e80emj78MH7WBBpmGonZ_deunGC-Gg3yNliZe3v4v6f1Rq-omK1Y5jUr7i6fQlYahqeJ6DT-fu-D-SM71mVeBk12UH3p9_S7_cQA7I-RbfVvBaUM-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از اقتدار تا ابراز احساسات
🔹
رسانه‌های خارجی روایتگر وداع یک ملت با امام مجاهد شهیدشان بودند
.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/446664" target="_blank">📅 15:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446663">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRtyRHf4fwFhuq_mlb9plMM93fOqYlV59B6W8Yq_QCsWCMOoXv9pUoGNmYAMqHrFbeX5JaB9IWRiAOcDqUaP8RoRYaA_Yi96Tg-2U-ffi3-0cFBuBhKWi3AVYv8gZOpWONVFOYaXg7QjI8aDZR4ya_DhKdtQ8wrbWo0DxfSNkFA5p5RI8eaxiNA8FHu4nONUwdvKf6mAFcjauTvvlQ3ohErTLeplGsY_2KpOBFJGNuKWQHQsb8UY-6CiJW0DP1OSFykr2fdHFx7ImkZI0XgvktDRtCFqjfogU9S3bzTI_ErzF296IrVJo7g0yrbNRCWSfDqsLPnOktmUtYIZh5yUig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرخانهٔ شورای‌عالی مناطق آزاد تجاری: انجام هرگونه پیش‌فروش خودروهای وارداتی در مناطق آزاد ممنوع شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/446663" target="_blank">📅 15:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446662">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdaac909ac.mp4?token=lJLD-ndDuNE6Ap7IHADa6bP9esztxHPFyK0kp4mXyD47BDrcpRhogv8CpQI2EvsaIDTk1TIkEig6UmosPzVENEN0PCZLqvZggzQCyOGwOsoRuRr7M1W8een40iDpc74HHuVDp4SqB4vnuT6bwREKmtdIRB09OXMX1F-f5ZuGc6HTtjArX7KdAybflR1qsg4VPA6_va64xrgeSqb_OX1Gvc9VNJ_Mp8P3my-ruM6NIOgwdNLnvqUAfb2zKNtWBd1dF7Mh2opcRhVA4HhYkyEWsor4T0Tp3oe8m8VBTe05Idt7X4syo38xzVhoZdX_D51nbUCDdObLC4zW95n1JL3zhDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdaac909ac.mp4?token=lJLD-ndDuNE6Ap7IHADa6bP9esztxHPFyK0kp4mXyD47BDrcpRhogv8CpQI2EvsaIDTk1TIkEig6UmosPzVENEN0PCZLqvZggzQCyOGwOsoRuRr7M1W8een40iDpc74HHuVDp4SqB4vnuT6bwREKmtdIRB09OXMX1F-f5ZuGc6HTtjArX7KdAybflR1qsg4VPA6_va64xrgeSqb_OX1Gvc9VNJ_Mp8P3my-ruM6NIOgwdNLnvqUAfb2zKNtWBd1dF7Mh2opcRhVA4HhYkyEWsor4T0Tp3oe8m8VBTe05Idt7X4syo38xzVhoZdX_D51nbUCDdObLC4zW95n1JL3zhDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم رضوی مهیای مراسم تشییع پیکر رهبر شهید انقلاب می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/446662" target="_blank">📅 15:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446661">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🎥
تو که رفتی ما شدیم همه فرزند شهید
🔹
روضه‌خوانی سیدامیر حسینی در مراسم وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/446661" target="_blank">📅 14:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446654">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q8E54KOmrEx_c-RIft3j_jBo1cRPKd6euAVGwRJtWqaRfGfSFaK1BDkrt-fvrScbhkCdOos3__TLpsw_XXN_DV215w9A0Gvzp3vHbDHDCXxBfRuGiDmK8lQydZfZPST4yW4y2Ba-GLiERukjq0_63PrJneexoIn6LyTGHG4DGdosiYGKDQwCBhb6rhhyy5XSXZiZ-EnPE-qbqisYdzSWVUZb7VA9th97PpY85Qld7h2W2HYdjU34IWqobcvDxFQGnitjxVEPNXpAwph5PAQCdUQZD5fuq8vdSulRJCRYGC9n9K178_RKEiTZVc6AzPHQkXi9lE_fjJA6yFYrfdbNVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R-7XKqxEZHS-5DTXqi1330FJENbR7_bwezWqIbpDuHSFdJCyihAmZG8r5ORFIPc5a_L3Hh4S2WfthCaQON2bcJivB81cnSX3c3uXocYulq07U7hhU44v-_CsLDMIbeuQIK0d7jtwOKvlWKqkbxCGkac39HVJ_zCXbjx5WlJrJdXDzKeYM3t6gyl7PlB3xbKpeqfMXJsw5yd9IdhuydQd0_cBedfHWZ5OzaQYfZaEw52qtEV_vwFqAM8gP_BOaqwgt_mv2kLo_7qNWYi5__wQQEdBzZhbk8tZ4d6VC1aGGMhllIPXAn-hmpqr7op05rQLGBL1nKSVMWaHVlrFZk8kxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8vwvpJNqr3aPhevkl5YrhsApLHffhPY83UJOBfo8uj_mPdF_Fx78fE4skIA_dhOQ1v3lm32ZE9sefcRXu82LiVK83J3VlhTBgBXzMoRP89VSGuF-J5y-S0nigYkEjV4lxNJN135UWIcZsaC7o7dECdCb8loeElkLSG_n7SfaQMNcZWQyWvOoCh5J40q_4B2ls1BHRX-daXfBDnjm0TrlaBoOQxN9iSQxupgLscN1_ap-8xAmcNLGXJDWBD3JGHgKIolx4ssvuPO3Hc9Nd2S4SzPYNpo1JPFeEN7Ji1T_eLSgIc_rj8C4bdpSh2ALCWShRaYdPOUkB1AgDGxonQI-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQnUvHC5e5vOtEN4LQd86nFvajjwYr68lDmsEIC3LPiroNB96wYmbr4DUBNpHT97-diUKkuNtkOKTgLegob6QITYY5gzglk_RVbvhqaIBr0UwbrC0vK9id4Grn80TjIlpx8ggVmBKI7zX6upX_oDs77wShRLp2KzZG7LOB3ARChlIWKSJEqITMfKDogh6wRyDnR5zX4ziXQ_08frgYhx0p-ZMc_drwF45-WtpcXc-QvcleJc6iip08dtMWtOfEKFzLxs1en2GKEhZNdaau1Sdnlqj1AgDP8pyxLLESQOv0b_3JY95cHzqO2rfzUAYMubp8TWECzNpH1m25omWhXfIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F73ELDiW109l-u-mcBvAcYJ1mn4ENscUxzCEzEbL3X9CDu8P0jFHEeQcIDrec7Tcmsy8p7kXgs5cbavAnh2zvRi3gQBq0IwW3iwCHTxLVBEHFmLr8ABtIR9E4qRo2hSc8hXWn4oPwFKyXzIXiq0PND0Dmwd8gb9L5qrRfSDMAQ34iFB-LZdJMgkkOX3TzvsrzXg2FcTmp-2d0Y_JbmoG2xpwXOSMLtAqSIVH7tKl5-q-ok2xXH3APSxbi_bt_7NXnpiAc5MFcYm0NV_fbD64_cE5MnO7adRCyTZU0ODw2MtKyrlZnoGAlWVM59i8wLcygeSMSGkORoKXk2kC5DCvNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TYHv_AZv18g2ht7NNkypfMe9RPpA7_R915KM7GJtd7H_JrzwHUWZqCkIWiIiH3mha_XmQnkNXoLvQ25dujHFM7Y1Spa144D9EJ3-yEqC3TpUPcs9_0BUsmw6xaWL0Qrj44sQCOv6RqPCi-X3AjCHOCdqjzMc_6UFH3PFKhewyfHO3ii6MulMy5KjC-kq8t-XjxuZTJ0jl3qyGXXoIqNWoA8faUqef7DiBXTK2w99NuyxkWBYKib1Q93B57h-_Y5W53cEDDGc5m_OYwnW_7qMhJA-sORv70dzltdrg0VcSdranIVM0rRJYEpp2R-JD7Wxm9h7zp-nA-UYFpwB_8C--A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GsmDB_JpGmQbuHHQk-0wK5OEM9CT43y7hr7-hDwGhTQIfXjPaJWXS6T1_9EolaQUbGiA4tIP7npyeSU0sMoes5IbvL_CA18XN-yPymv_guk2FI98Z9EbGCCKLiYL-3Ysc7jz95G4EokNnnjWUzQLD2OLjqRKh5ZHTReOEo3nMV9V3_D1j0V10MZCGijbzBZKdB7eyx98FN0QggusIIPyYhWNNqNAGA30coEkY7Y0-D_vbLHBJFl8n4u7gKOI8yHGIaeoVnJasjrYynSQIMftfYVTI13RlFf6lstFNaQ1PlBPU_wD0g-7lztjwG0RMmncUa6nQb5UgAE2MZMKpSzXOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آخرین دیدار با آقای شهید ایران
عکس :
احمد بلباسی
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/446654" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446653">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a3072eaa7.mp4?token=sqApdiqTkEHJlYPQ6G3h2DXpyoU_pvEguhuttEtbmLKXL0jyP8YSMBDuml6bdKFRTaSxaep1A6eUTGo9WrFGSt2VxJcP5rxLqqOt8k4bapOwKKjW4jkAZMJh9pnk_0tpkD0yTXIYZv9uJPvccjvrmf0ic5SMeChb8I5C8-zlKa36qpxRdTfAGC2VGkL-Ybn1D4_Rsb9NGaZIeu_u7fiD4lF-MWIGAGsKMcH0ZqwSt0d0qPeKdyaPBZlQjU65KeGKGrG_G0CequUpp_LwGbpOdUIwAyYksHLnVc_7O454yTxtBW_Grl5tfEurF04fSF8_KULpjnohJPlzf4Rw4WI5OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a3072eaa7.mp4?token=sqApdiqTkEHJlYPQ6G3h2DXpyoU_pvEguhuttEtbmLKXL0jyP8YSMBDuml6bdKFRTaSxaep1A6eUTGo9WrFGSt2VxJcP5rxLqqOt8k4bapOwKKjW4jkAZMJh9pnk_0tpkD0yTXIYZv9uJPvccjvrmf0ic5SMeChb8I5C8-zlKa36qpxRdTfAGC2VGkL-Ybn1D4_Rsb9NGaZIeu_u7fiD4lF-MWIGAGsKMcH0ZqwSt0d0qPeKdyaPBZlQjU65KeGKGrG_G0CequUpp_LwGbpOdUIwAyYksHLnVc_7O454yTxtBW_Grl5tfEurF04fSF8_KULpjnohJPlzf4Rw4WI5OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحبت دهه‌نودی‌ها با آقای شهید
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/446653" target="_blank">📅 14:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446652">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-IFMhis_XNXNEXL2Y-SkJNGbdOnK6rZTsepmAmC78aha2rf4HbJVnoGAVctX0V13G41xRP1Eny_21m3Igo3dh6ThSV5HT32yL9eTqzQej5waee4UgXDSgvBLmZJ39jqjfbNuED2k5N90lOu4rD4TcwrT3bZnJ8Vgcr32iLtXwZen6gelxbMoaTRw6S_IzoAnJ2ktDYfAqcrEQiftkg5P94qGqW5tW09eHnJwY0tfbTrhMuH_oB-Cb3sup79uGUfM7iynUE3DDJCIyVkmMkMevA3ogrN3jVPA5nP24_LfscMbcw6SP4FBzfrRHST_-NPQqnM_k1LFAwlgBAc422Hig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شریف مثل خانوادهٔ شریفاتِ اهوازی
🔹
«چرا اینقدر زود اومدید؟»‌ «زود اومدیم؟! کجا زود اومدیم؟ اتفاقا خیلی دیر کردیم خیلی!»‌ این، اولین و ماندگارترین جمله‌ای بود که می‌شد از یک مرد باشرف شنید.
🔹
از اهواز آمده‌اند؛ بدون هیچ اسکان و آشنایی در تهران اما توکل به خدا کردند و همراه با کودکی که بیماری کلیوی است، خودشان را به پایتخت رساندند...
🔗
روایت سفر پرماجرای خانوادهٔ اهوازی را
اینجا
بخوانید.
@farsna</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/446652" target="_blank">📅 14:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446651">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">◾️
بنگر به قیام سرخ آن سرو رشید
◾️
با ظلم نکرد سازش آقای شهید
🔹
شعرخوانی محمود حبیبی‌کسبی در مراسم وداع با قائد شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/446651" target="_blank">📅 14:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446650">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72db04cc0.mp4?token=Bi3hMs_HueJw8W0bw22eP3GBQke0wSiIdWvcCLLdbXKvG09-gP-OFanMKH_0W6h6qOkrxxNALIx3YpoxNXtjJMW5wcOITHHRDZ2xo2G_4tXs8jIHBpxipQCAckmVsE06qy_z4TM_R6M1lTjUW2jDzN4OqafRCVgfpsgDLnDkYzr1IH920hPUpKPlCmzT0V7_7bLZLqJ41GPFy_J_gp_v4LP4s4bhR1-U1N29RXjBaGrW4SddKBYyC5oAvetWvGvERgX4s_IQN2eO4or3qzp4AMRv-VUCPF4hLiZV7Jwc3W4kNvNjLxq8rqIRxOWdXyPKMR8r3f6opwrtjhK1URG1ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72db04cc0.mp4?token=Bi3hMs_HueJw8W0bw22eP3GBQke0wSiIdWvcCLLdbXKvG09-gP-OFanMKH_0W6h6qOkrxxNALIx3YpoxNXtjJMW5wcOITHHRDZ2xo2G_4tXs8jIHBpxipQCAckmVsE06qy_z4TM_R6M1lTjUW2jDzN4OqafRCVgfpsgDLnDkYzr1IH920hPUpKPlCmzT0V7_7bLZLqJ41GPFy_J_gp_v4LP4s4bhR1-U1N29RXjBaGrW4SddKBYyC5oAvetWvGvERgX4s_IQN2eO4or3qzp4AMRv-VUCPF4hLiZV7Jwc3W4kNvNjLxq8rqIRxOWdXyPKMR8r3f6opwrtjhK1URG1ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مهمان‌های آقای شهید امروز از همه جای کشور به تهران آمده‌اند
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/446650" target="_blank">📅 14:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446649">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b3c949c36.mp4?token=oGEqQLYdxVd28ysc8aFP3KHXWYVcOy04UC72DdJKF4sdPhLLa_hvbvnz3LNdo9uRab1iOBbzBzsx1p8bEJKDRVcp35ybi1nFWLlkGNXTpDfeduIltjcQwTYPdYnnUfKqqgy48ii5gNMDV5QS9oHar_ocju85kJOkLETEpS8BmPTD3QJ7u-LeZcgJDX94lcpjo-ds96i5N3ODqspSo2ipc8wLSq6I0PmdOTBGoxWPnG-kACljmtoVEY5-XRMYTHpYUJUpkZx8BxuyUt5imrazE6rKrQAF7-90SUc-zclSyM9LMkvp8NKXEOnWeoazQKC4x5XXrJTMiF4gwrLNhMrIXLiq_pBRiio4QqTjcintTQtBWhujqJUm9BIU_plz6oqLNSGpyJs2LOGC9_gkeWWypjj3vmq9nTs2mymAiPSxmb1hf_5Q_9WB6QYW6zW7niJbKDdrLbaKqahmvdpu3W5lnC-kIaVq5yX3plIzoUZz5TV_aS9TuGRwhv96dIJSl6lePZGdo4Urzxqu9Ozl2watr963r0ZPnKfksMN-wbPN4Ng0-CxR6KcEL3_C9BxI6MveeCYsCYd1DL_NZEPcNKktNQ7OcYse_TbZzKs9n0MO93LQvQ9Ufqn86sCOprSZOneYeTfMfwDDTjFklNlgt33fNU31isBRhMOaKEQ9WzEBtAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b3c949c36.mp4?token=oGEqQLYdxVd28ysc8aFP3KHXWYVcOy04UC72DdJKF4sdPhLLa_hvbvnz3LNdo9uRab1iOBbzBzsx1p8bEJKDRVcp35ybi1nFWLlkGNXTpDfeduIltjcQwTYPdYnnUfKqqgy48ii5gNMDV5QS9oHar_ocju85kJOkLETEpS8BmPTD3QJ7u-LeZcgJDX94lcpjo-ds96i5N3ODqspSo2ipc8wLSq6I0PmdOTBGoxWPnG-kACljmtoVEY5-XRMYTHpYUJUpkZx8BxuyUt5imrazE6rKrQAF7-90SUc-zclSyM9LMkvp8NKXEOnWeoazQKC4x5XXrJTMiF4gwrLNhMrIXLiq_pBRiio4QqTjcintTQtBWhujqJUm9BIU_plz6oqLNSGpyJs2LOGC9_gkeWWypjj3vmq9nTs2mymAiPSxmb1hf_5Q_9WB6QYW6zW7niJbKDdrLbaKqahmvdpu3W5lnC-kIaVq5yX3plIzoUZz5TV_aS9TuGRwhv96dIJSl6lePZGdo4Urzxqu9Ozl2watr963r0ZPnKfksMN-wbPN4Ng0-CxR6KcEL3_C9BxI6MveeCYsCYd1DL_NZEPcNKktNQ7OcYse_TbZzKs9n0MO93LQvQ9Ufqn86sCOprSZOneYeTfMfwDDTjFklNlgt33fNU31isBRhMOaKEQ9WzEBtAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انتظاری که سرانجام به‌سر رسید
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/446649" target="_blank">📅 14:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446648">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJ8XjZUBB3B9d4-VEZ8QHN83VoWjyt3V6u9ZorKAKlA1qT05oi5gIqUIsLMFj3XqTFx-Pq1MHGSaMOtxJEUs3Gsfbi-5uwvqmTHFIMk3RhkfSNVAjdN3V1Qnug-5PzXaux37EKbStY4wPvMwwkG4rC9fHzyReBerVmdkRHQEdj-qAs1N8ZOBltCXRlWXWWCwDMOhJv5MN1p-hsJ5HUNvzUsMKeMuZ8X0L2m_xjO0W_gJAPOk7aq3zzmUN0Ziv60savO-wXy_K5ryLKso1POWQ5VeNk-EuPnCB2Ku_t-XAlUpMdam0liRycZYnetf_IzcvafYQexH_F2nnTSnkorelQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره: از تهران تا نجف، نقشه تشییع حامل پیام مهمی است
🔹
شبکه الجزیره در گزارشی تحلیلی، مراسم تشییع و تدفین رهبر شهید انقلاب را فراتر از یک آیین سوگواری توصیف کرد و نوشت که این مراسم هفت روزه علاوه بر جنبه‌های مذهبی، حامل پیام‌های سیاسی و منطقه‌ای است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/446648" target="_blank">📅 14:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446647">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43ebfac6e6.mp4?token=LevSm1r9QjRAazs6BW5cMvFLml9_cwdkd3b6sdHxoJuMzAx6ToNS-ptIJ2ndXkaRJ15D-F9nltzF81xGhMD4cuTISyo_D8S8hpgLD-5lhpWEnBf_0oX445vJxtPeMoUOw740gfM7_S-c8QggGzninay17bd4fqkBIFkpsXjBxHa8nm2X9DyJgLRhQNwsVwCnbINawxCugQ0zlUQLls7R43vV1VPX4y_fBt4oSD-zk3oR5MfPUBCBGix7bLRWVFTdzP9fl0HydW3r_2Z-SzvjatYnfwTcDJH0ke7WJ8rajKqCt9s6rAco2oOVkrAPe0wrhaebDn7-r97pcosQki-bhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43ebfac6e6.mp4?token=LevSm1r9QjRAazs6BW5cMvFLml9_cwdkd3b6sdHxoJuMzAx6ToNS-ptIJ2ndXkaRJ15D-F9nltzF81xGhMD4cuTISyo_D8S8hpgLD-5lhpWEnBf_0oX445vJxtPeMoUOw740gfM7_S-c8QggGzninay17bd4fqkBIFkpsXjBxHa8nm2X9DyJgLRhQNwsVwCnbINawxCugQ0zlUQLls7R43vV1VPX4y_fBt4oSD-zk3oR5MfPUBCBGix7bLRWVFTdzP9fl0HydW3r_2Z-SzvjatYnfwTcDJH0ke7WJ8rajKqCt9s6rAco2oOVkrAPe0wrhaebDn7-r97pcosQki-bhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طباخیان: شایسته است که این لحظات را غنیمت بشماریم و برای آخرین وداع با رهبر شهید حاضر شویم
🔹
برخی صحنه‌ها در زندگی تکرارناپذیر است و تشییع پیکر رهبر شهید یکی از این رویدادهاست.
🔹
امروز ایران بیش از همیشه لازم دارد که ما در صحنه باشیم.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/446647" target="_blank">📅 14:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446646">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Exf_CguePLwCW83TesrwjPGluagNy49YGbINB32FZApmmxDsFWcAIDfj8g2xrHtSwFO15D8GexU5gtNs0MJqHIgIX5SvLa14zeeWEhwm6gcwC4g1z2m5TV2EkG8a1vh4AFsgqttmWWIN62qYwMJatO0pl-OtVd2YxmS_WA86-rJKqi6kOF_6Xz2fvwzEPYQbhguBmgUtmQMfIl6C5FmoueAMBMyDv7LlQjIQYkHi4Y3xu2y-hpnNchxOHGYur6kmuUbifUOqySFmbjDpJFuqz1xSsfTUjsQEz8YHT6IM0NyVIpaiYj_5NQ7c_8IpzXwpwjDt4DeUwGvoapl7FDbVZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا جانم ثابت کرد علی(ع) افسانه نیست
🔹
سن‌وسالی ندارد. با پای‌ گچ‌گرفته روی حصیری نشسته تا موعد آخرین دیدار برسد؛ از ۴ صبح راه افتاده تا قبل از حضرت آقا اینجا باشد.
🔹
می گوید: «آقا جانم نام علی را زنده کرد. اگر ندیده بودم می‌گفتم امیرالمؤمنین افسانه است...»
🔗
وصف حال زائر جوان رهبر شهید را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/446646" target="_blank">📅 14:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446645">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b3cc359df.mp4?token=pm1DYqWnD675oqpbN562TYH-1LWKCPboE8USbV8XI0YcGeOFf2VfXlvHVVpsSkhZBaYus8IfOgxlMMKndq6RwHCWGXDe4IwabHq2DOdy80NfO98AFTserwGpYBOMNlGwWxvbov9KgYy0S0pvruB4-6y14o8IEaQamOsty4hztwneTRuWiAhHbbEL-btCbxlO06Q1BrCBvKZo1ZIpnJmi5bDdwOVCcV5b3ccyll8yJFNH1UbKC87TU24rBHXKDgNpqRbHdUp5Pr_JmdpKxDN0mQ_vk5dejyKQ0rCbDmqljDRHt5dZYg9AhFmGXaPHlFM4B7fNK7JV2fcCq4QY0hrQuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b3cc359df.mp4?token=pm1DYqWnD675oqpbN562TYH-1LWKCPboE8USbV8XI0YcGeOFf2VfXlvHVVpsSkhZBaYus8IfOgxlMMKndq6RwHCWGXDe4IwabHq2DOdy80NfO98AFTserwGpYBOMNlGwWxvbov9KgYy0S0pvruB4-6y14o8IEaQamOsty4hztwneTRuWiAhHbbEL-btCbxlO06Q1BrCBvKZo1ZIpnJmi5bDdwOVCcV5b3ccyll8yJFNH1UbKC87TU24rBHXKDgNpqRbHdUp5Pr_JmdpKxDN0mQ_vk5dejyKQ0rCbDmqljDRHt5dZYg9AhFmGXaPHlFM4B7fNK7JV2fcCq4QY0hrQuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین یکتا: شرکت در مراسم تشییع رهبر شهید انقلاب، اعلام بیعت با آیت‌الله سید مجتبی خامنه‌ای است.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/446645" target="_blank">📅 14:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446644">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c29877906b.mp4?token=nLrrne2mpgML2JqndizhiOmL1fmdm9QuqXFEUmnKEA0bVhjhoYCrlaI9BbSQk5-yp75A3TENQ0JR6LDrrKlhgS6xIWJ6tG-9WmApGwimuRtzOCRf4dVbCoXHMQl60JTCK1Ve6Mbr3pNZBBSmD6o6HkShkoIR8fqzerEn116fEMY8DjvnJx-dkhjj42EjuLtyMgyz0O69GvhaSReo-xDnTF0Ic_-Rh-8Trz_YVenIv7IHID_03iMMbs6HwORr15kMC-XaHDnPhCD30Z3U1yBwrzaN95zZsZL9EeSCMCjLNCLDyGH4hrTKlUbZEDyJPuD6L3myw05r0zKUiM01ra_AtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c29877906b.mp4?token=nLrrne2mpgML2JqndizhiOmL1fmdm9QuqXFEUmnKEA0bVhjhoYCrlaI9BbSQk5-yp75A3TENQ0JR6LDrrKlhgS6xIWJ6tG-9WmApGwimuRtzOCRf4dVbCoXHMQl60JTCK1Ve6Mbr3pNZBBSmD6o6HkShkoIR8fqzerEn116fEMY8DjvnJx-dkhjj42EjuLtyMgyz0O69GvhaSReo-xDnTF0Ic_-Rh-8Trz_YVenIv7IHID_03iMMbs6HwORr15kMC-XaHDnPhCD30Z3U1yBwrzaN95zZsZL9EeSCMCjLNCLDyGH4hrTKlUbZEDyJPuD6L3myw05r0zKUiM01ra_AtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فعال رسانه‌ای ساکن کانادا در برنامهٔ پرچمدار: پس‌از ۷ اکتبر هر بار رهبر شهید دربارهٔ فلسطین صحبت می‌کرد، در کانادا و کشورهای غربی سیل عظیمی از جوانان واکنش نشان می‌دادند و می‌گفتند «ایشان درست می‌گویند».
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/446644" target="_blank">📅 13:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446643">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871679d97c.mp4?token=KSe4anbj1jz5fOpWeVeBtWDj0gVLKfTIG0dEOq2Zj27aCKhF-_PdPG-FVZv8a2lYKIVTxEYFFenssRDwJl-w2qRFVb4wWozNjmsF7qmHxP8mg2H3A7bj23c0I3j-d3wYr_2rieqlzFpP0WYd6TZvNL6BTBWU3QZ4Z--9g5JqyrKaAEqNTtEi5gQkjXTuSia6UjDKcV97bwwadZcC7UAQMSMvcoM0U_vXbkP0TUZ2TfFJrjQNdJi4rF1nUEuDXIGPconzn3l2MekVVxHBHCR8a_3b3KKieb2PW9L5L668tQDFBSQd-n7cM4IamkSMQzSud5-0exS6_gV6qCpGt874_yeO4BcEFBMBS4sD7Erfia_QjNAyVwjjHNjlC78IAP6G2un-bLfmvt7ir8UMrweRqbX5DcmQt4s-MTtSzLiql45mturV5rul1U9I2IUfar4nIo0ORiTyBSSUt-zKHHBmsCSJEyeMojW67K8OxXFBl6MGMePfBoIzEkfFT2a_1PwqgLCb4QsLx_q98xec-JNBM9Zwh1MtlQo_okaVvXWVe1-U0kzOAjnNymCxSwtbqi26rlVlFcgQ5asPZ9jJGke0OHm6rd8975JulMwv_0fjkbBINe8CyPgRmDPL16_POLZwK7xk2CQFXTfybZ2B60kMp42u0hB___6ID889zTw0Uh8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871679d97c.mp4?token=KSe4anbj1jz5fOpWeVeBtWDj0gVLKfTIG0dEOq2Zj27aCKhF-_PdPG-FVZv8a2lYKIVTxEYFFenssRDwJl-w2qRFVb4wWozNjmsF7qmHxP8mg2H3A7bj23c0I3j-d3wYr_2rieqlzFpP0WYd6TZvNL6BTBWU3QZ4Z--9g5JqyrKaAEqNTtEi5gQkjXTuSia6UjDKcV97bwwadZcC7UAQMSMvcoM0U_vXbkP0TUZ2TfFJrjQNdJi4rF1nUEuDXIGPconzn3l2MekVVxHBHCR8a_3b3KKieb2PW9L5L668tQDFBSQd-n7cM4IamkSMQzSud5-0exS6_gV6qCpGt874_yeO4BcEFBMBS4sD7Erfia_QjNAyVwjjHNjlC78IAP6G2un-bLfmvt7ir8UMrweRqbX5DcmQt4s-MTtSzLiql45mturV5rul1U9I2IUfar4nIo0ORiTyBSSUt-zKHHBmsCSJEyeMojW67K8OxXFBl6MGMePfBoIzEkfFT2a_1PwqgLCb4QsLx_q98xec-JNBM9Zwh1MtlQo_okaVvXWVe1-U0kzOAjnNymCxSwtbqi26rlVlFcgQ5asPZ9jJGke0OHm6rd8975JulMwv_0fjkbBINe8CyPgRmDPL16_POLZwK7xk2CQFXTfybZ2B60kMp42u0hB___6ID889zTw0Uh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای عزاداران رهبر شهید در مصلای امام خمینی(ره) تهران
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/446643" target="_blank">📅 13:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446642">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3779b348ff.mp4?token=mOm2SIN0-Ysl894ECG01LUrRBxlSrR-jWnvt77D8Up-OfzDveDXCSk-EqcQ_tK59qvUupG8ixilotFn_zBJU55brgjtShx_T_K58AuQDJyox8Kn15ZvWxSGsajhqmGP0xZck2djRgE2PFyDXWAGkc0aza65pxf6EmSJDMUG1Jh5rA1mZ9UO1GuGQlhcu5PgpnBCrb7IZrHbxrw01pFqSb7dag7tCasatYhAfLXW_mLzHp-RG7HgtxZvGnw33Ewr4Gsxc0ymGpBDpyi6G_YO1x5n0FFiZSrdnACvJAaMa0W2puYCAn1fFoA24aBAlyXMC8Op3I-El5tQYpsYinRzqkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3779b348ff.mp4?token=mOm2SIN0-Ysl894ECG01LUrRBxlSrR-jWnvt77D8Up-OfzDveDXCSk-EqcQ_tK59qvUupG8ixilotFn_zBJU55brgjtShx_T_K58AuQDJyox8Kn15ZvWxSGsajhqmGP0xZck2djRgE2PFyDXWAGkc0aza65pxf6EmSJDMUG1Jh5rA1mZ9UO1GuGQlhcu5PgpnBCrb7IZrHbxrw01pFqSb7dag7tCasatYhAfLXW_mLzHp-RG7HgtxZvGnw33Ewr4Gsxc0ymGpBDpyi6G_YO1x5n0FFiZSrdnACvJAaMa0W2puYCAn1fFoA24aBAlyXMC8Op3I-El5tQYpsYinRzqkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار مرگ بر آمریکا در متروی شهید بهشتی
🙍‍♂️
ارسالی مخاطبان به
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/446642" target="_blank">📅 13:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446641">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4af6a52b9.mp4?token=cg9YDLDaTfbAcav8HYbPLKorQmeIBkyffVfcZZMgQFoH5oyCUGx9LfBGVuRbfPNfQsAuDmvTsOTF26Y4Km-0VGJ27vbwfgbT2MlBY5_Y1xv6UO0XI-NfWdYNUAHpDBxZUZKOyeGK8PPL57bcpwUWhxDyK8crJD4QSd6w1ONV3HRHsTGyG1raV0ySL9v3gYslDIuGF0bJNdkFm1Fwl1xJ6gpvnIjZ5rN_FqEJMf4Gsu-O_LsNnebpMLaTIdtP0HZVmKIEFPg3XIijD0D8DatFvdsvYJOpU8-HvFcOo1CGe5vRL60YAuBNy397gl3yzYhnfxt-f8qpcbGYDui33nW6NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4af6a52b9.mp4?token=cg9YDLDaTfbAcav8HYbPLKorQmeIBkyffVfcZZMgQFoH5oyCUGx9LfBGVuRbfPNfQsAuDmvTsOTF26Y4Km-0VGJ27vbwfgbT2MlBY5_Y1xv6UO0XI-NfWdYNUAHpDBxZUZKOyeGK8PPL57bcpwUWhxDyK8crJD4QSd6w1ONV3HRHsTGyG1raV0ySL9v3gYslDIuGF0bJNdkFm1Fwl1xJ6gpvnIjZ5rN_FqEJMf4Gsu-O_LsNnebpMLaTIdtP0HZVmKIEFPg3XIijD0D8DatFvdsvYJOpU8-HvFcOo1CGe5vRL60YAuBNy397gl3yzYhnfxt-f8qpcbGYDui33nW6NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت حامد شاکرنژاد از اولین دیدار با رهبر شهید انقلاب در ۸ سالگی
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/446641" target="_blank">📅 13:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446640">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7ktcW7Pfc5am9Mr7l7OlospratYfXCfCoyEh1l7VEXPSHntSWCr7yNcDeukYkfmWUUDx6F7M3NFWdfd6Ljuj1RA497EvyAoTzk3erxY81fbbhlHJYEbBx_D5cTbFUggqFpogRlDyVkJMG2Os64ZskAplcd3PLiJzRTJLjRCm0h232rjSF0lY10XuSaughc1nct01QtFjCjs-Ek-tGDHZ5DThHooPswd81m9suow3CEDN1ytoueih3_g0JrDA5xfEF85CV_TJ4PrZjGKoZLYcwRQBk8nFLYY9MQuMQftCvxVYSa1FGsHi5xkbbltJjtU9sJw_k2vkVU7iZDR6GxOmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تاکسی‌های رایگان تهران در کدام مسیرها فعال هستند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/446640" target="_blank">📅 13:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446639">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b8d10c5ef.mp4?token=GEh1iaShc598K6FkUsQmkqTvdklcF-9WGgEVUSPs1vvSYc-oJKWKIZlbwL-esdFEHqzJbv4ahvwT5l7wmcA-zJdIJniHkrkwyfm_5imeiTeiQVEQKtE9s98LNtpdndQpmtSVaGph-fDXM3gUxCFNXahzUw2BPsDlyzNxZdss3MvWW4PKKz4nWraL1Wzu6uibIqlhoOGl-rTXdjnl-T5Bwg6btYSc7v5qQOqz5UvZOH1B2LwutJX71Fclv4wDmuj5w19zdetNIW5rXQeJuBHtqvijoYbJDw4mjT6j6Quy654iab05NgC2sQv6Oa9bNdknqnaLqNWy7r3TY9XxjR1bOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b8d10c5ef.mp4?token=GEh1iaShc598K6FkUsQmkqTvdklcF-9WGgEVUSPs1vvSYc-oJKWKIZlbwL-esdFEHqzJbv4ahvwT5l7wmcA-zJdIJniHkrkwyfm_5imeiTeiQVEQKtE9s98LNtpdndQpmtSVaGph-fDXM3gUxCFNXahzUw2BPsDlyzNxZdss3MvWW4PKKz4nWraL1Wzu6uibIqlhoOGl-rTXdjnl-T5Bwg6btYSc7v5qQOqz5UvZOH1B2LwutJX71Fclv4wDmuj5w19zdetNIW5rXQeJuBHtqvijoYbJDw4mjT6j6Quy654iab05NgC2sQv6Oa9bNdknqnaLqNWy7r3TY9XxjR1bOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درسی که دختر کلاس سومی از ایرانی‌ترین رهبر گرفت
@Fasranart</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/446639" target="_blank">📅 13:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446638">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnmdWPbQENXvvDbZt82P9Bzesq7oDgj-N8gjFQoHXB_AgBmzMSu5L2DeHR0P6HTgLa2Z2QBsbY5-aauTndOygGME8hTp3MSnk12HUdoiJLLU6AM-Mr6Pg_4bcVsqAJGjg1xRBN0n8t4LEM6dDUk1JZvJhDAN5q_boX2tMKODpDx6_azDgn1TNiqWp5T0fig4hwj2FXaLW7Vdd7Jf6-XwGjQ5QgPWK1IOEmutbnZtuAJuRPMte-0cxQgAJXgdnmHbxvdnkLsHdNaC_HnUITh7liBZ0gBVXq0xx4_PlO6VZ4LI8_E7GQRwaRvUKSUq-7mgrRUPVe_gUNUqQr_3QKU-DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور اسکوچیچ در پرسپولیس مصوب شد
🔹
در شرایطی که طی روزهای اخیر اخباری مبنی بر منتفی شدن حضور دراگان اسکوچیچ در پرسپولیس منتشر شده اما پیگیری‌های فارس از منابع آگاه حاکی از آن است که این موضوع صحت ندارد و روند مذاکرات با سرمربی کروات همچنان طبق برنامه در حال…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/446638" target="_blank">📅 13:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446637">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cb543bb24.mp4?token=ZGThWmcBCSF7zdvVLUU4XZwazea9VWgFa3VGpuXRFqRXPjxLcz4SDPVpm0xekX64V2zfrkKikcAfovehAnL8jpbbNbKG2NCpht5aWcEyxCiF5O6DDm9ktMyF2Mdszu1LKkejBR2864w0HcTu6o806yqEXFg2DmGsDYVPR0Ihv4DWRtUWGBRE3sHDBGsVjENUJ4jvwM7cQ0ikGIFNVVCH-XlCqBRX4_jGouLjuNdp9aC0ZXNmFmvSWjtD87VNEvWw81SwOrtE-AtRle9jYp6iK29XPQbP05kuedQ_T6FRxyHtdawOruJ1WTTPxkfHnmBwL1eyOBpCN_UwIIl21pg_73gaID-wvbPmwtc14Jry2IPZERqmPehdVBMX_LzACJrwiDGyxgcfMRVI_spj0cdyw6wUgWJhwztcZE1j97G0qV69ywFPzFzBKGA9kQ3mIKXlWQ5iw0g0_uXgpUTMkvaOKr9-qO_M5Dw95PP6swuTIFJWq0ffPUoOIjoDt9aSQbzlCNRvFPSK2c05ffuWtsxbPAQf7T_gclNHP-g_uh8KxbNISYXHN4hRIpFMzcgX4S9jRYJclidt9rdgRmZuC2J1uVBqtOeJOTpb_XOLDHPGYsL7yLUM2Ywr5IWmJTqX38xOEPsjvjidqFe_36U7950YG55yKuZxQHvOF5qVWrXzUeE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cb543bb24.mp4?token=ZGThWmcBCSF7zdvVLUU4XZwazea9VWgFa3VGpuXRFqRXPjxLcz4SDPVpm0xekX64V2zfrkKikcAfovehAnL8jpbbNbKG2NCpht5aWcEyxCiF5O6DDm9ktMyF2Mdszu1LKkejBR2864w0HcTu6o806yqEXFg2DmGsDYVPR0Ihv4DWRtUWGBRE3sHDBGsVjENUJ4jvwM7cQ0ikGIFNVVCH-XlCqBRX4_jGouLjuNdp9aC0ZXNmFmvSWjtD87VNEvWw81SwOrtE-AtRle9jYp6iK29XPQbP05kuedQ_T6FRxyHtdawOruJ1WTTPxkfHnmBwL1eyOBpCN_UwIIl21pg_73gaID-wvbPmwtc14Jry2IPZERqmPehdVBMX_LzACJrwiDGyxgcfMRVI_spj0cdyw6wUgWJhwztcZE1j97G0qV69ywFPzFzBKGA9kQ3mIKXlWQ5iw0g0_uXgpUTMkvaOKr9-qO_M5Dw95PP6swuTIFJWq0ffPUoOIjoDt9aSQbzlCNRvFPSK2c05ffuWtsxbPAQf7T_gclNHP-g_uh8KxbNISYXHN4hRIpFMzcgX4S9jRYJclidt9rdgRmZuC2J1uVBqtOeJOTpb_XOLDHPGYsL7yLUM2Ywr5IWmJTqX38xOEPsjvjidqFe_36U7950YG55yKuZxQHvOF5qVWrXzUeE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ا
نیمیشن لگویی «باید برخاست»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/446637" target="_blank">📅 13:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446636">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9nhaJ4n74ohYha-ucG0zh4mC4Gtq1hQygw5FlLa2AOsunJa-kbfwiaeiNhYTSGDdMOhm0EMpD4D0yY2Cmr7iSz1JDRH9Xbq05e1VvcnW4j9LtLw36Tzp6QuADgdo7TO30v1T_vcRVKLKU31wa9G0BlLq8YyAAkIec-uCD3MVAv95hRc09xRjhI34Xs2iHmTmXAh9VvBqYdRX7v4jUifn2ffiLIzXNeLj2HSib_-tzWGG8t3fUTm4wFGg8mCiHZ7wme5J31sxKCOMNaBmYwSSrO2yCGzVYr2GiZLOO290231UPyx5278-S5u4DTqF01p8ycV0UPUaL_KPyD8CZafNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار معاون رئیس شورای امنیت روسیه با پزشکیان
🔹
پزشکیان: از مواضع حمایتی و همدردی دولت و ملت روسیه قدردانی می‌کنیم. باید از ظرفیت‌های شانگهای، بریکس و اوراسیا برای توسعه همکاری‌ها بهره گرفت.
🔸
مدودف: حمایت شایستۀ تحسین مردم ایران از نظام ضامن حفظ ثبات و…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/446636" target="_blank">📅 13:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446635">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffa1600c7b.mp4?token=o3Yo-ojzb6-CqceXrgpXaQqjaC7PxstzpfWURX4VBzjkxJjHrjCBD5LltbiO-JFutORI2SyMtq8Gv_Xe_4atoQPf3I7nM05BDbgc_uu9zU0dKeooMjH9NhjhrxG6_lnfL5xzPPFNdCj77Z4AkOPnExc4SqFvag2gyoPam7oS9Tv1QZY6p_Qzsxs9jL1YiP4xRkt5DeSLaOhku8aDlbVHmyFhj3cyAol1-A96j8snoc37TXnXePtsR_7VnKDwCvgjZeahIlE1jRiQTiVHcUgT29zCxwkiFygkMMKDdF2BuZ0SNiNdKw_df9ie2Q-89691zJ7p6PVEpfV3RX8G1_ueNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffa1600c7b.mp4?token=o3Yo-ojzb6-CqceXrgpXaQqjaC7PxstzpfWURX4VBzjkxJjHrjCBD5LltbiO-JFutORI2SyMtq8Gv_Xe_4atoQPf3I7nM05BDbgc_uu9zU0dKeooMjH9NhjhrxG6_lnfL5xzPPFNdCj77Z4AkOPnExc4SqFvag2gyoPam7oS9Tv1QZY6p_Qzsxs9jL1YiP4xRkt5DeSLaOhku8aDlbVHmyFhj3cyAol1-A96j8snoc37TXnXePtsR_7VnKDwCvgjZeahIlE1jRiQTiVHcUgT29zCxwkiFygkMMKDdF2BuZ0SNiNdKw_df9ie2Q-89691zJ7p6PVEpfV3RX8G1_ueNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نگاهی به حال‌وهوای مصلی تهران قبل از شروع مراسم وداع رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/446635" target="_blank">📅 12:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446634">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130b14ba29.mp4?token=gH5BFCvH2HReKHVa7wYzb9TZ81iXaewYMpw6jNzAuVJ2biMQYp1_fPc1NyC3jnxHkwswrdOvVfE_5KX02GmoQeGthID-ePjeCFSl2r-l4NYOm9lY7AIUPPFGsl1Dksyxoh1tuIsVkrRUMV-1lD0HG38qQ4YbWGmvRqsgPPcWEeCJHRG1fho-TCF8TNG5BTvn8gbw2oN01gJrohsxrjA_xSXgNINiKKPknQlyQKeT6g3UCNjb7Tp32KCpIodaKQTiJ4dl1aMWirhBJZFlZVew_jn9rNTQrETQIHnEWyRPq-fbNpdVAJrXOq3h-f1FQD3PGCVtRZWHM7_rMIik1_6FKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130b14ba29.mp4?token=gH5BFCvH2HReKHVa7wYzb9TZ81iXaewYMpw6jNzAuVJ2biMQYp1_fPc1NyC3jnxHkwswrdOvVfE_5KX02GmoQeGthID-ePjeCFSl2r-l4NYOm9lY7AIUPPFGsl1Dksyxoh1tuIsVkrRUMV-1lD0HG38qQ4YbWGmvRqsgPPcWEeCJHRG1fho-TCF8TNG5BTvn8gbw2oN01gJrohsxrjA_xSXgNINiKKPknQlyQKeT6g3UCNjb7Tp32KCpIodaKQTiJ4dl1aMWirhBJZFlZVew_jn9rNTQrETQIHnEWyRPq-fbNpdVAJrXOq3h-f1FQD3PGCVtRZWHM7_rMIik1_6FKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خانوادهٔ شهدای میناب برای وداع با پیکر رهبر شهید انقلاب به تهران رسیدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/446634" target="_blank">📅 12:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446633">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b8d63a5c5.mp4?token=tQOSgZmjgrDtdubq_SrVplsGzztZ_yzCxs6Lbx5FEeUwtRpLmWQqIXheWWcB9Vnhz9L7VEwWGRG917qNxK52dd8h40Y_QZ_7eytT9LwAAJ3ao0nLtupBPWr3uA0ckadfoZu6IXoqMGDJAhYQB6xSVcBZp3eVVsevpzbZA6ZVypOkmVR0AK0t2EOKLApP22glPpSkSqgUYBFpvaEaCMzIU3tf8rZwAhaJPZKevLlOm1opxuV8vCOlTjwnUa9Yw_L3Awn8xKGIvMpuyfs1y2spOxPL1FGcEQAcIKi-qiVJo--zRza258tVxjPn7KXa5r71_yk41nd7YhvFTZ4FMiB2gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b8d63a5c5.mp4?token=tQOSgZmjgrDtdubq_SrVplsGzztZ_yzCxs6Lbx5FEeUwtRpLmWQqIXheWWcB9Vnhz9L7VEwWGRG917qNxK52dd8h40Y_QZ_7eytT9LwAAJ3ao0nLtupBPWr3uA0ckadfoZu6IXoqMGDJAhYQB6xSVcBZp3eVVsevpzbZA6ZVypOkmVR0AK0t2EOKLApP22glPpSkSqgUYBFpvaEaCMzIU3tf8rZwAhaJPZKevLlOm1opxuV8vCOlTjwnUa9Yw_L3Awn8xKGIvMpuyfs1y2spOxPL1FGcEQAcIKi-qiVJo--zRza258tVxjPn7KXa5r71_yk41nd7YhvFTZ4FMiB2gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع با پیکر مطهر شهید مصباح‌الهدی باقری کنی در منزل پدری  @Farsna - Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/446633" target="_blank">📅 12:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446632">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">استانداری اصفهان: احتمال شنیدن صدای انفجار کنترل‌شده در صفه، جنوب اصفهان و بهارستان تا بعدازظهر امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/446632" target="_blank">📅 12:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446631">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56916aefd9.mp4?token=uUI48wY44GPFqqRo6QgdoigGuNyfiU2S4J2WOSgXHw1ASp-VWTQAv4Vdz4X2Cmv3YHqRe1_N1S5OPE1TiLKVi3XHIn5MZOWepuD_kHgcoo986dYSarUxgfrAWTdmHs_yH0XhN8hetw-ZaiD7PUX_0VH1uA1POpbIUqoCrPwMuW3iQef9PgX_Z2DjHj0qnuWP0I0qpUHG28l_tzF6rW5ix-YP9q82tTqvIL7ewP1ZxjInhJnSniHDVPVz1p9KYFong3E2POe2lOM0UCZbkYoUWgVFrwyl_bgaPm4L-qeTtkGtAgueIaGJkOz10ETAMXvULc7W2fGRryp9bt9u7n1dDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56916aefd9.mp4?token=uUI48wY44GPFqqRo6QgdoigGuNyfiU2S4J2WOSgXHw1ASp-VWTQAv4Vdz4X2Cmv3YHqRe1_N1S5OPE1TiLKVi3XHIn5MZOWepuD_kHgcoo986dYSarUxgfrAWTdmHs_yH0XhN8hetw-ZaiD7PUX_0VH1uA1POpbIUqoCrPwMuW3iQef9PgX_Z2DjHj0qnuWP0I0qpUHG28l_tzF6rW5ix-YP9q82tTqvIL7ewP1ZxjInhJnSniHDVPVz1p9KYFong3E2POe2lOM0UCZbkYoUWgVFrwyl_bgaPm4L-qeTtkGtAgueIaGJkOz10ETAMXvULc7W2fGRryp9bt9u7n1dDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موکب کودکان خردسال عراقی به‌مناسبت وداع با رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/446631" target="_blank">📅 12:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446630">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96248288ff.mp4?token=ls8cBScfD2t3Ass-VzlWWcnKlPFoCpK1Ci_Hb7y-nBnn0N-kzsjA2DGLZTtLNK_2JiJxMPMa6QREpHM3AG_opKZX-y3UFWF-0rM69aN3SugvL02IhjyPeJJyttHKeLwtHj4AVjktHpHbYJKBBj880aecoT6tsCmG0hwh29GvRXHhrZQx0eywptLqNg7ETKyiv750d1fSSKEDWoFeL-TFcvprnxvz-iS24IlZkeHl3ZVnHHVUCUZwudp6HcTZ7SJaZijTEiTQ8W5S8DSsoT7aCM1xbvfzx4d4rpr8e-MaI3T-7w059NYJUudBdBl6MKvdqf9BE8WNpAK84jMwR1KEFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96248288ff.mp4?token=ls8cBScfD2t3Ass-VzlWWcnKlPFoCpK1Ci_Hb7y-nBnn0N-kzsjA2DGLZTtLNK_2JiJxMPMa6QREpHM3AG_opKZX-y3UFWF-0rM69aN3SugvL02IhjyPeJJyttHKeLwtHj4AVjktHpHbYJKBBj880aecoT6tsCmG0hwh29GvRXHhrZQx0eywptLqNg7ETKyiv750d1fSSKEDWoFeL-TFcvprnxvz-iS24IlZkeHl3ZVnHHVUCUZwudp6HcTZ7SJaZijTEiTQ8W5S8DSsoT7aCM1xbvfzx4d4rpr8e-MaI3T-7w059NYJUudBdBl6MKvdqf9BE8WNpAK84jMwR1KEFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
الله اکبر، خامنه‌ای رهبر
🔹
شعار زائران رهبر شهید انقلاب در ایستگاه مترو
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/446630" target="_blank">📅 12:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446625">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/APxJesM9a9dQInnqjOjUZJw9v8XBtzOjejPY0tP5jpIe9GTlrjUb02kEDrc9i04Z0_vT-zihFo-TW1cFRJ4kYzcvFZcuJ22TMaN8IvIL7cBo22En0KVEafA8SomQUvZ5MZQKeb1GnMv_BKjVEpKWZOlHr2KPgydSWIR3JqEP2C_GqxpLuN0kPt4xCTYjfa9Vj9Yt4dgL14hV2SDZUiYxPrDlwkVLGY6A0UnZIZmiKtBTTaZVVntIb7G2Ule9S9Uye4rqkTU4nW5g8KZPC91ZzVpSDSU6EPFy9HBGG-mhFkplgPOfwPEQO0vHjIg8gmGXnrNfz033gIy3VichNL7d1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QMY4b3_qoNKZYNdvE89g4GV4m6U2VI8vllAgWlRlq22XcKIuTsYeP5wi-Kgr4iOhwjw9M7jjvPAwQ0m3fiSqdbUlZlxIKRHeQ75lOaT3wp_vk8OAAl4668FnQwVlq98ozldVSKZhGG771RbcloHrg41ioIIS-ymj-XbqD1jFaX0W38CEjOP0_Xw-TX6onW3Z2Rohhvn-zS-IwkVqi9j69PjBvAo0wdQy7MQ2dDJWoH80dP97FvMVj8eyADGokSp18mQbuWtV13ugbCIkwUuwWYTuZWEZDaY-vXsb7MC61G63hS0DcOv2pRLlHpXMP-Z7t_g49rF51u-6r1KagLhv1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iPlGQR3KLIrVX-fz3QaPoi5OTGW86ML5h-QX_ILUrLWzN0uNsQubncKXmlXzOl4Pw5nNn6oOeQFg6AeCxoj99Kkw_noPUFOo_yqsZAAtxXu9nbW0hwH5Oxx8Z2LW98xJhphTFbHv82ShurHq4_edG-Wvg_WElzVxWOgvXeU4OkpD3MtmclKnY8Dm6p6ufKDrHKcDB82HqBmOjvvuwA4NRgUAKoGh_jLVQQTSjY2WenOY6AWjurSg-TLEzXognR01mH4oRK-_oP6666F0XRvhy4zUBGQAycZ1KXYP-b_N0D3L99fjF3y40rCbdeENTZA6Liwwo2mYowiokmTV7C4FrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UPK1NUtxw4_k-hu9vhpnjLZIruJcB7ZrL88J1wmjTezZjhkjgtBEcDG5ys7tRX3KktZR_rvhGMsuyC6vKicbTwp1WhO8ubWU-LcdTdSdZFHfZDCPeMRMil9ZBAE_EAMeoWbcnPt1ZaYjQ5nyKvrovToeQZJ7t7S-hpk_6b_WL8BT68XfgWgF95xGF-FxrvZ4SgioJA53VGYyBJX0QOSkvjJr6nZkc7a-ZZhXsr-75JpRHHg1ObGSuKJnso2sReLNP7JQuGRPpgBl1brBVWoFtN6b9J5jTFTPmX5zXnTA0F1hI_MDsyZ4bQ2dI3MrMo2qL9lX73152FTcnDqZquNJHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تشییع نمادین رهبر شهید انقلاب توسط شیعیان نیجریه
🔹
هزاران نفر از شیعیان نیجریه صبح امروز با برگزاری مراسمی به شکل نمادین پیکر مطهر رهبر شهید انقلاب را تشییع کردند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/446625" target="_blank">📅 12:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446624">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🎥
به آرزوی خود رسید آقای شهید
🔹
مداحی صادق آهنگران در مراسم پرشور وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/446624" target="_blank">📅 12:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446623">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InCzjyFeQifjnWg0ZlK5_oWKexBcU8zxhrvDfp9l4lHwmaz7Cmb_0JFE_uXxvsdRDD9-BFlQRZjNDwG77-XoU3zZVpsMmFI6pij5PhtyLQF6vXWw5vqf0Xa--RYZogTREfdldnSUz9F5EcbqVKau988hokc5GspQAX8yqcy790xwEPuOgULynGFHopUlydIsdF7Vh3gEsMHfL7szMiFTImylvpjo7_TFjhZVUEyUjOCIbRNS1quNiES_9xtAjhdr79h4nW7zxA8jv1dN8p3Ukc4PoywvvSS3ltwDmE20467JNFvlMKvcw9g65cRYrAz6nXmkc9SbNjXe8Gnsae29MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورودی‌های تهران باز است
🔹
پلیس‌راه راهور فراجا: ورودی‌های تهران باز است؛ زائران شهرستانی می‌توانند تا محدودهٔ برگزاری مراسم وداع با رهبر شهید یعنی شمال تا حقانی، جنوب تا کریم‌خان زند، شرق تا صیاد و غرب تا ولیعصر فعلاً تردد کنند.
🔹
توصیه می‌شود زائران خودروهای خود را در مبادی تهران در پارکینگ‌های تعبیه‌شده پارک کرده و با سیستم حمل‌ونقل عمومی خود را به مراسم برسانند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/446623" target="_blank">📅 12:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446622">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
‌ کیفرخواست پروندهٔ رضا پهلوی و عوامل اینترنشنال و من‌وتو صادر شد
🔹
دادستان تهران: کیفرخواست رضا پهلوی و تعدادی از عوامل شبکه‌های اینترنشنال و من‌وتو به اتهام زمینه‌سازی برای اغتشاشات روزهای ۱۸ و ۱۹ دی‌ماه سال ۱۴۰۴ صادر شده است.
🔹
پرونده ظرف چند روز آینده…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/446622" target="_blank">📅 11:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446621">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
حمله پهپادی اسرائیل در جنوب لبنان
🔹
منابع لبنانی از حملهٔ پهپادی رژیم صهیونیستی به اطراف شهرک «صدیقین» در جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/446621" target="_blank">📅 11:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446620">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da5c9015e7.mp4?token=eIDlyehOc3TL2aQ7Bd7kIrAxAskvfMCiVY-ouVCH1sfrE2c_dWs1Dsrc6amFQKu9w76Pyj9yAV6FEep4ZH_puSRBYEPDitqWJ4Qt4sZhtiwemchLVr4SQFlIm9SJcJ_mpe0s4HTMkjpiV30WGH9cwSEzKWI3tBxb6m4bHgXhE2LeUi6Rl4DEsEZG6zWRs7BSKoJW1qtrxTtxRLooUlZpMuGycS8NuMkpNdPBUJETEiD_ioRw2ZPSIMANR05KM62mwsOwU1C4j7wffyHyvFrtS7GAszVxbjZEIo_EeyT0KXLlhq6qcOvAa5HYO31ot5DrwmKNnoHSQW07qUiL5blMeLWQYRgTm0U-UhHbo-6t1viZbNnAn3pIugiYe7ShhTaPP_OxyldG6qHNAtfokATrWUcY6PEcP8T2E3bubpdskqqDrW06rCc66FUSOkT6tHMKqmKO1jlFr2YJCoDXYgkrXhhSl0iz72l-CRhclYCpocXoAlubnzkSqrlEGuHIAxjDDz5VfV1Vkds5PpXaRk-MUIZXBo3lDqf00ZLZJGH3z1xLSpeXtQ0tWgH06mrFXEG7AkUfQoN0aG_WaxSdc8x6Z6OQ2nvUZhP9U7Q0UKfyM0zgP6YjCqU-RfOFNJYknpwIseyR5yyIHlU4TdnSPAZOsG9wRMMjjB0UbcQhrVg369A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da5c9015e7.mp4?token=eIDlyehOc3TL2aQ7Bd7kIrAxAskvfMCiVY-ouVCH1sfrE2c_dWs1Dsrc6amFQKu9w76Pyj9yAV6FEep4ZH_puSRBYEPDitqWJ4Qt4sZhtiwemchLVr4SQFlIm9SJcJ_mpe0s4HTMkjpiV30WGH9cwSEzKWI3tBxb6m4bHgXhE2LeUi6Rl4DEsEZG6zWRs7BSKoJW1qtrxTtxRLooUlZpMuGycS8NuMkpNdPBUJETEiD_ioRw2ZPSIMANR05KM62mwsOwU1C4j7wffyHyvFrtS7GAszVxbjZEIo_EeyT0KXLlhq6qcOvAa5HYO31ot5DrwmKNnoHSQW07qUiL5blMeLWQYRgTm0U-UhHbo-6t1viZbNnAn3pIugiYe7ShhTaPP_OxyldG6qHNAtfokATrWUcY6PEcP8T2E3bubpdskqqDrW06rCc66FUSOkT6tHMKqmKO1jlFr2YJCoDXYgkrXhhSl0iz72l-CRhclYCpocXoAlubnzkSqrlEGuHIAxjDDz5VfV1Vkds5PpXaRk-MUIZXBo3lDqf00ZLZJGH3z1xLSpeXtQ0tWgH06mrFXEG7AkUfQoN0aG_WaxSdc8x6Z6OQ2nvUZhP9U7Q0UKfyM0zgP6YjCqU-RfOFNJYknpwIseyR5yyIHlU4TdnSPAZOsG9wRMMjjB0UbcQhrVg369A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مصلای تهران غرق در شعار مرگ بر آمریکا
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/446620" target="_blank">📅 11:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446619">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فرمانده نیروی دریایی سپاه: انتقام الهی از آمریکا و اسرائیل چندان دور نیست
🔹
دریادار پاسدار علی عظمایی: اینجانب و همۀ رزمندگان دریادل نیروی دریایی سپاه و حافظین تنگه راهبردی هرمز با خدای خود عهد می بندیم که با پیروی از آرمان شهیدان، راه رهبر شهید امت را با قدرت و استقامت ادامه داده، و رجاء واثق داریم که انتقام الهی از آمریکای تروریست و رژیم نامشروع صهیونیستی چندان دور نیست و پرچم حق به دست خلف صالحش و ولی زمان، بر قله عزت و اقتدار برافراشته خواهد ماند.
🔹
امروز ما وداع نمی‌کنیم؛ بلکه بیعتی دوباره می‌بندیم با آرمان‌های او، با صلابت او، با ایمان او، و با راهی که از سینه‌ی او تا افق‌های روشن آینده امتداد دارد.
🔹
آن عبد صالح و مجاهد فی‌سبیل‌الله، عمر خویش را در مسیر احیای حق، دفاع از کرامت امت اسلامی، و پاسداری از آرمان‌های بلند اسلام ناب محمدی(ص) سپری کرد و با ایمان، بصیرت و صلابت، در برابر جبهه کفر و استکبار ایستاد و نام خویش را در شمار مردان تاریخ‌ساز این سرزمین ثبت نمود.
🔹
امروز سوگوارِ فقدانِ جانسوزِ شخصیت والامقامی هستیم که توسط پلیدترین و شقی‌ترین انسان‌های روی زمین به شهادت رسید؛ کوردلانی که از اقتدار معنوی، صلابت گفتار و قدرت تحلیل آن شهید عزیز در هراس بودند و چون تابِ درخششِ نورِ ایمان و بصیرت او را نداشتند، دست به جنایتی ددمنشانه زدند. این کوردلانِ استکبار و ایادیِ دست‌پرورده‌شان باید بدانند که با این اقدامِ مذبوحانه، نه تنها مانعی در مسیرِ حق ایجاد نکردند، بلکه خود را در صفِ اشقیای تاریخ، در پیشگاهِ عدلِ الهی و در برابر خشمِ توفنده و انتقامِ سختِ این ملت، بیش از پیش رسوا و محکوم ساختند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/446619" target="_blank">📅 11:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446618">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5cb95837e.mp4?token=cXUihTZuCjJsUhppPtxxMT7yrGzghoKQuic19EjVVYZ616CL-flnsj3EGYvzQxZxR4-bJt2qyTcm-0U-oP_cCErKn6za55s-JrCVvaEE7VQW5TxhEUeMJLuOyLNhshsU7k-suYhnB3iubsasa0IMsX2qqFiaCXPvhb1iJnDsULY3rgctCdAVsxk_LNjB_VQ-TWISAX1qkrEOUA527MuK3PAatIw4mCEbAGy_9ZdsmjrXVxgYO3pc_cI3Lr2_6oh5YM_LepogyDkcblAuyrMqO0y0G2UoVm-A8rRfewOg5wc4fzlg3o8wGHCzlGVfShhTn8osilJ21G8lXKAf55iFvCXmBCi1V_TQ2dKl-i0O1x3taymbLBMgOOj14WOLjta76oCQ7mfv4N_AB6RM1oKBMMx-s7MauSBwjpgUhJcap6-8LgIq8pwf5X6jGxhwgcN5yFpV9p_81XWW6q8kcm-_r64VhlTyzPamrWYSp2Td0F2QOgx0hZk9ItnxXVfOZe80dDh0mbokFugxuLkM4xDR9WiYofn0WwtDASDvepa3X3mAOpR23SGkrTo_AJmPqLVryR0ByPgz9ACuqTEOe13-7IjIdowp_Iu6t8IyxWjM0p3A9EeztVYywe5wljqhvvqNNwua0t6pdrGCtAw6K1AoWhbYqvGzAshWac1jJk7zckM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5cb95837e.mp4?token=cXUihTZuCjJsUhppPtxxMT7yrGzghoKQuic19EjVVYZ616CL-flnsj3EGYvzQxZxR4-bJt2qyTcm-0U-oP_cCErKn6za55s-JrCVvaEE7VQW5TxhEUeMJLuOyLNhshsU7k-suYhnB3iubsasa0IMsX2qqFiaCXPvhb1iJnDsULY3rgctCdAVsxk_LNjB_VQ-TWISAX1qkrEOUA527MuK3PAatIw4mCEbAGy_9ZdsmjrXVxgYO3pc_cI3Lr2_6oh5YM_LepogyDkcblAuyrMqO0y0G2UoVm-A8rRfewOg5wc4fzlg3o8wGHCzlGVfShhTn8osilJ21G8lXKAf55iFvCXmBCi1V_TQ2dKl-i0O1x3taymbLBMgOOj14WOLjta76oCQ7mfv4N_AB6RM1oKBMMx-s7MauSBwjpgUhJcap6-8LgIq8pwf5X6jGxhwgcN5yFpV9p_81XWW6q8kcm-_r64VhlTyzPamrWYSp2Td0F2QOgx0hZk9ItnxXVfOZe80dDh0mbokFugxuLkM4xDR9WiYofn0WwtDASDvepa3X3mAOpR23SGkrTo_AJmPqLVryR0ByPgz9ACuqTEOe13-7IjIdowp_Iu6t8IyxWjM0p3A9EeztVYywe5wljqhvvqNNwua0t6pdrGCtAw6K1AoWhbYqvGzAshWac1jJk7zckM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آرزومه همیشه یاور تو باشم، میون لشکر تو باشم
🔹
مداحی امیر عباسی در اجتماع باشکوه مردم در مراسم وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/446618" target="_blank">📅 11:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446617">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">اهدای شال عزای قائد شهید از سوی وزیر صمت به موکب‌داران چادرملو
⚫️
وزیر صمت صبح امروز در جریان بازدید از موکب شهدای وزارت صنعت، معدن و تجارت با حضور در غرفه چادرملو، شال عزای قائد شهید و عظیم‌الشأن را به موکب‌داران چادرملو اهدا کرد.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/446617" target="_blank">📅 11:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446616">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکربلایی وحید یوسفی</strong></div>
<div class="tg-text">﷽
📽
نماهنگ |
#خداحافظ_رهبر_شهیدم
🏷
- از سوگنامه
#بدرقه_آقا
🎙
بانوای: کربلایی
#وحید_یوسفی
🏴
ویژه مراسم تشییع
#رهبر_شهید_انقلاب
صفحه ی کربلایی وحید یوسفی
https://t.me/vahidyosefy_karballai</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/446616" target="_blank">📅 11:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446615">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/446615" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446614">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8B4F2KlgwKrRuNLvTmKiV1HVSAO3obKwhUmgxonWnX0chtbfnY7ow-YHud5cf6fESSKjtiauC4s1hy0Ap8IfNS0CuCgWqzs3O0_LeB2A2cGC5ugSZ4bM16AajuokiIuF4XhSzRMsQ7CSa4ZaXSyIX0CRReGxOh1zcX-_1nzFOR6r7c2SIintEBDi-FYEnvz9fOhKlnxaZGwYwRV8CVBy6lvJyAYUzxzcxI5rquhcBI5MVzBX8FvRmO8kqn38i_aGBQ26ELfy8rIl3MOnZD1rNrcLOQixMKaaZ4r8D-p6hS6HZYRZS4ifKU_KPvxOIeyb_otIeAtL_xYmq-1aHWyrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران مقتدر در سوگ مقتدای خویش
🔹
بیانیۀ وزارت اطلاعات: ملت مقاوم و نستوه ایران اسلامی، بیش از ۴ ماه است که در تداوم مصاف تاریخی و مبارزۀ عاشورایی خویش با جبهۀ کفر و استکبار جهانی، داغدار و سیاه‌پوش شهادت مظلومانۀ عبدصالح خدا، ولی امر مسلمین و بزرگ آموزگارِ عزت، استقلال، استغنا، اعتماد به نفس، ذلت ناپذیری و ظلم‌ستیزی است.
🔹
دشمن سفاک آمریکایی صهیونی بزرگ‌ترین جنایت و توطئه تروریستی تاریخ معاصر را در این فاجعۀ بزرگ رقم زد و قلوب بیشماری را تا ابد جریحه‌دار و محزون نمود.
🔹
دل‌های آزردۀ مردم غیور ایران و آزادی‌خواهان عالم جز با خون‌خواهی از مجرمان این جنایت التیام و تسکین نخواهد یافت؛ که طبق وعدۀ الهی این انتقام و مجازات محقق خواهد گردید «انا من المجرمین منتقمون».
🔹
اینک در امتداد پیمان استوار و میثاق ناگسستنی ملت با رهبر معظم انقلاب و اعجاز مبعوث شدن بی‌نظیر ملت سرافراز و ولایتمدار ایران پس از این شهادت عظمی، سربازان گمنام امام زمان در پایگاه مبارزه و جهاد وزارت اطلاعات برای تکریم و تعظیم نسبت به مقام شامخ و روح بلند و طیبۀ قائد عظیم‌الشأن شهید (قدس الله نفسه الزکیه) و دیگر شهدای بیت شریف آن حضرت ضمن دعوت مردم شهیدپرور، استوار و مبعوث شده ایران اسلامی به بدرقهٔ حماسی امام شهید خود، بار دیگر با بیعت حماسی بر عهد و پیمان خویش با رهبر معظم انقلاب اسلامی حضرت آیت الله سید مجتبی حسینی خامنه ای(مد ظله العالی) و مردم همیشه در صحنه برای گرفتن انتقام خون قائد شهید و شهدای مظلوم جنگهای تحمیلی دوم و سوم از جنایتکاران آمریکائی صهیونی، مزدوران و سر سپردگان کفر جهانی و دفع همیشگی شرّ آنها از منطقه تأکید می‌نمایند.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/446614" target="_blank">📅 11:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446613">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🎥
ابالفضل علمدار خامنه‌ای نگه‌دار
🔹
انبوه جمعیت در مراسم وداع با قائد شهید امت
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/446613" target="_blank">📅 10:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446612">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNBTWRf5Gzd2TGZerKHpFkxaazCTOTJsORXBRARuZFyMQnsfRO6tI5nHIYNSQ399yw8BTbd5_SaYiYdTQqegpmomIBG3Ko7s2xm0gTOjMn9jG53NCJCQQIwS-X0JDJw1tka5-Go-LLEPcXZLs_rO1B2PjzBglNxfyRzS8Sq6-eTlaSIfPxPBMTEpDccx1cxTA8-R32nPxMHot02bYs3abvyFbUzoBamDkmLU__sqEMqNV0yD_fwFTCGuci0Na4gx5mZa-LqCgM12-Lls9kQaWQqk6G93GZnUfEfw-xlDg7RIcba1mAAi6ymjYVLY8gtAj-mn-OzSPJc5E7W4zFBkWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم اقامهٔ نماز بر پیکر امام مجاهد شهید و شهدای خانوادهٔ ایشان، فردا ساعت ۶ صبح در مصلای امام خمینی(ره) تهران برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/446612" target="_blank">📅 10:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446611">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🎥
بعداز تو کشوردوست هم تا صبح باران بود
🔹
مداحی سیدمحمود علوی در مراسم وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/446611" target="_blank">📅 10:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446610">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b766132058.mp4?token=Qms9lZDJKG9p_cll3mjqnMADy-QNXkWYFPFDTL4hh3-ZhxIq5I4-JKxv4yonFG8jyra-TKyts5HibHTB5IeY-2_tkQEi3CALrSfpGw9tlpR_dxweDZj_RS_CQsDOQ79CZhLVIu6a65iaRnTiOj1gaATr8G342uJm7y7agCfgKVuezkWDaEmTxwPfaRRHEzSmt7OlNZG5uXCb8RMuTiwlzLXRL382mv9ip-JvfrDo3dAYIY_0g4ZN49T1eVzQyTq_PQ-yoneYqSZCSNt0dNWGXtwZpR8r6QedA60I43ysuzqc2g2-pLNSpZ4VNkze_5aNkzlSOVXZhGFhvfPnt7ZFmZLQ3mMNBZ8KZGgxcSh4leNybHc4QOdAb6UQ_VrcRa84coNO8MBBuNPvQunA11FPcfHda-c0eLGGKQ9rFsV_1jufPa1yM7lab84eFkoCFFx61puXwHT4hQeDywF52j5dLu-i_ejgthfV2LONzCOiJLAPSsqRZ19dwtZ7_QruZxE3gqS_RE4M3WMwb2fOjtIx8Rv_2PeWIHKQKe9_4V4G7B125-qhEkV4dnCXmNK_MXumhtEXml7wxIiev-bGDxS-3osNwVjmAbO9tP7ZISFbz_e43ke4Ejp59Phmz2iKHm5eugo0lccORuCqp4l3PZe3LSQKTveWajWjFdoeJ_0sWyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b766132058.mp4?token=Qms9lZDJKG9p_cll3mjqnMADy-QNXkWYFPFDTL4hh3-ZhxIq5I4-JKxv4yonFG8jyra-TKyts5HibHTB5IeY-2_tkQEi3CALrSfpGw9tlpR_dxweDZj_RS_CQsDOQ79CZhLVIu6a65iaRnTiOj1gaATr8G342uJm7y7agCfgKVuezkWDaEmTxwPfaRRHEzSmt7OlNZG5uXCb8RMuTiwlzLXRL382mv9ip-JvfrDo3dAYIY_0g4ZN49T1eVzQyTq_PQ-yoneYqSZCSNt0dNWGXtwZpR8r6QedA60I43ysuzqc2g2-pLNSpZ4VNkze_5aNkzlSOVXZhGFhvfPnt7ZFmZLQ3mMNBZ8KZGgxcSh4leNybHc4QOdAb6UQ_VrcRa84coNO8MBBuNPvQunA11FPcfHda-c0eLGGKQ9rFsV_1jufPa1yM7lab84eFkoCFFx61puXwHT4hQeDywF52j5dLu-i_ejgthfV2LONzCOiJLAPSsqRZ19dwtZ7_QruZxE3gqS_RE4M3WMwb2fOjtIx8Rv_2PeWIHKQKe9_4V4G7B125-qhEkV4dnCXmNK_MXumhtEXml7wxIiev-bGDxS-3osNwVjmAbO9tP7ZISFbz_e43ke4Ejp59Phmz2iKHm5eugo0lccORuCqp4l3PZe3LSQKTveWajWjFdoeJ_0sWyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لبیک سیدمجتبی
🔹
شعار مردم در مراسم پرشکوه وداع با رهبر شهید انقلاب @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/446610" target="_blank">📅 10:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446609">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BANQxvLDKgTzA-svMFaAQHAoBiYM_7uVKliudxqdQdMO3yiRpTlIAGLoyicEN0MEv0psj9Dfe0040GCPkIhTx0kaTnIcOAcmPmePgw-0Jj8ZNQZ0eV6BaMC3AR-AWalkuTG6ua9HddB4JepnmIxAc16TdHHa3I2CDWE75PqAazRhkuCgk0bhtR4DTa2RxVRnwvPPSA5gimv6gyZ4TFjWIKHBqBmGjjgh01BrP8pBQu_mkUOlHwFvKVjc-USYIs7RsSw44-o6FoCnnEwqpPBwygJbzPVfiHuAMEXaPGW1qnyHCvWKA6eN8b4xKK4JOCcMXzXRVmF1abICoP-zyXG70Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانهٔ صهیونیستی: میلیون‌ها ایرانی با شعار «مرگ بر اسرائیل» با رهبرشان وداع کردند
🔹
روزنامهٔ صهیونیستی یدیعوت آحارونوت نوشت: مشارکت میلیون‌ها نفر در مراسم وداع با پیکر رهبر ایران، نمایشی از قدرت و «خاری در چشم آمریکا» است.
🔹
همچنین رسانهٔ صهیونیستی وای‌نت هم نوشت: جمعیت عزاداران در تهران پرچم سرخ انتقام حمل می‌کنند و شعارهای «مرگ بر آمریکا! مرگ بر اسرائیل!» سر می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/446609" target="_blank">📅 10:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446608">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5110c90444.mp4?token=U34tCnftT3cseSlqufUgwrKlY3ZPoUX6vpr1aAWPacfuulaGxIul8ezRGPxLgBSXzYEkLpFt-F-t2V-xz7UB8N__Y9faPTl_xeYWmB88vznzNvI2ArrE2t7Um99WlCxgCMP3Ot32Ec4e7CO2JLmLsceAkXtoWrLIAbb2jRK0YzVys4g1Ip8LmWkmtqc6Ojoxp3-qwwR5Gv81OH5x7m9PeGfMAxuKRdFke8ZJkLA6HZ9-Q5v345q-MIwv2-3FFTQp-7ZowrIfwIMnG_7qOrzIZZD3rU0VFzDdhZg0Iud3zcdwRg2lWDBjiuottiECK-yh_4t_S1mnyASE4V4IAM9q1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5110c90444.mp4?token=U34tCnftT3cseSlqufUgwrKlY3ZPoUX6vpr1aAWPacfuulaGxIul8ezRGPxLgBSXzYEkLpFt-F-t2V-xz7UB8N__Y9faPTl_xeYWmB88vznzNvI2ArrE2t7Um99WlCxgCMP3Ot32Ec4e7CO2JLmLsceAkXtoWrLIAbb2jRK0YzVys4g1Ip8LmWkmtqc6Ojoxp3-qwwR5Gv81OH5x7m9PeGfMAxuKRdFke8ZJkLA6HZ9-Q5v345q-MIwv2-3FFTQp-7ZowrIfwIMnG_7qOrzIZZD3rU0VFzDdhZg0Iud3zcdwRg2lWDBjiuottiECK-yh_4t_S1mnyASE4V4IAM9q1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لبیک سیدمجتبی
🔹
شعار مردم در مراسم پرشکوه وداع با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/446608" target="_blank">📅 10:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446607">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5d5bfdddc.mp4?token=UihG2Go85g56g1xyjj8x2-jwjOK8uXofOtXeEQXiJRZp8Pw38lCuB4qlvNf2yc7CfFrlloamUdov0Oy0sqUaGqJCevK0ELuk858YI7-1Ax0NriOj8id62FK59g94fKqEq0MuxS_6S5uFzs461htjgPlkFbDcjSp_trMpe3ONJ6hOkU67ZA5XeIXildtWXEC0trFOQ5azvPDYTHZIidQyUwIzxlteHVY_0e1bGzvUY339V2GS7uILMMyKjpb9JH2_iPEsyvYlEJmKMGrvYNX8CVv07gO94-lZKmHmmxNbvUXObFwtUd9vAJCPn_lZbaz32dsfteAXSjtMMx2Tj0iw_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5d5bfdddc.mp4?token=UihG2Go85g56g1xyjj8x2-jwjOK8uXofOtXeEQXiJRZp8Pw38lCuB4qlvNf2yc7CfFrlloamUdov0Oy0sqUaGqJCevK0ELuk858YI7-1Ax0NriOj8id62FK59g94fKqEq0MuxS_6S5uFzs461htjgPlkFbDcjSp_trMpe3ONJ6hOkU67ZA5XeIXildtWXEC0trFOQ5azvPDYTHZIidQyUwIzxlteHVY_0e1bGzvUY339V2GS7uILMMyKjpb9JH2_iPEsyvYlEJmKMGrvYNX8CVv07gO94-lZKmHmmxNbvUXObFwtUd9vAJCPn_lZbaz32dsfteAXSjtMMx2Tj0iw_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سی‌ان‌ان: مصلای تهران غرق در اشک و فریاد «انتقام» شد
🔹
رسانهٔ آمریکایی سی‌ان‌ان در گزارشی از مراسم وداع با رهبر شهید ایران، مصلای تهران را غرق در اشک و فریاد «انتقام» توصیف کرد و نوشت: هزاران عزادار با سینه‌زنی و شعار، پیکر آیت‌الله خامنه‌ای را بدرقه کردند.
🔹
این شبکه آمریکایی به‌نقل از آسوشیتدپرس نوشت: جمعیت یکصدا فریاد می‌زدند «حرف ما یکی‌ست؛ انتقام! انتقام!»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/446607" target="_blank">📅 09:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446606">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWzYFfSNDvUWgbaCFPCr3Ef1L0BWnQ5Tz1vuFWtvZ5d9f_8FiOD4SiIazlXLU8w4PP-HvsYyy8MqqwqnCy5je20LYfcgAeID7ksvLXGSagNEV1ifNKbZJbRtIVR3qNbKJR2SN0DDTljUcGMpGuGB7L8MyWq5AnJpZ7-1gg3xFD2485s_KuSE7i6qWkMBPJ5Cpzpc-QtpCT4sTGVvgDGr6Yl_TKI0YH8_B7e1KSs_imDmywLCcLg06QQOS-g2-YdP9vLEbF40zYa323ZBxEeJIs9zTdr782O3VV9zAGtfsbBNtIqBpceIjUwd0pmgRQjwNM2HNG4t8MudwxIfHKO9Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایستگاه مترو مصلی و شهید بهشتی باز شد
🔹
از دیروز به‌دلیل محدودیت‌های ایجادشده، ایستگاه‌های شهید بهشتی و مصلی امام‌خمینی مسافرگیری نمی‌کردند.
🔹
اما دقایقی پیش مدیران شهری اعلام کردند که در این ایستگاه‌ها، تا اطلاع ثانوی، خدمات‌رسانی از سر گرفته شده و مسافرگیری انجام می‌شود.
🔹
همچنین مترو تهران تمامی واگن‌های خود را وارد خطوط کرده و سرفاصله حرکت قطارها را به کمتر از ۵ دقیقه رسانده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/446606" target="_blank">📅 09:54 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446605">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">◾️
خون‌خواه رهبریم، خون‌خواه رهبریم
◾️
از حق انتقام محال است بگذریم
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/446605" target="_blank">📅 09:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446598">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fceH0SgqBv3V9klfHUSn5owhU6d25nwdxWlB6q0vAiBzd_debpNf1IHDq3SlQhEw8x3ItdJiWEUk22psPLeP63oQ6F-ZVn_TlF2NpEBkNMvh3gm_yK_-3AE6ilw8VpkFYuAn_JkN5l2G1l07gQpoMMNCjpWJmTUiUYc0phArRE2u4KdsZ_-z2gCuaoPsxebxdQNvj5Vt1de4YLrgjPXgTUb8KbviFjXxL5ZJ5l7k7HUNiVtL34G-c3_1ByfHP8HMizWXecPaQt9__pc-mQSNkIgXZkIiXbE92iKxKgnw75VHNPl06puoxB-3pYktpUMstl5bJs-9nDxNN3M5ght7Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jHmJBBxBLSsxKPYba7omWIh9xPvwgwUS7lLVSDegq0iglUcGCioPMlqad0gs_HRs-WGwqg_Io-FT7awoxSr68fCAfg9MuBKLEmEochfdjuxKRdrjLaZbKx3HkQWDxQ5Xogi0HgqZuzoNVvQkHJyT4jHElzLd3njdCDDmvrIskIoA_aGGLpyU08eCQ2U9RSBKAAL_AaUTOTvVX_dFSEKQgoU07JUNXYAt-lUJJXVK5qkD4aagaRNt3TcskDONXsouGSsZwCAyfnPZMNpluC488NuHbjj2ho4yztYhCUndALW3NdRdm9GRlnT4CAizTmZTHah6smVetY9F-vcxryxCOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SbQdZ4khCjpr4CVGw6LLpu6ssrf7oBT083ZdMhgGI-Iy1QttKBSC6vbpGJKemUChwBL4dYfmpfTn24SpuvowgCdyYC8nqvmG5v4K4QtXzDtMXihX7IjtNRVdmqE5jGx1mCYYFIExjg-ZgsI15TafnHqv5jm4KUJBmYqY0N18FgF116YmcJZfCQaqPrug8fxKzOQ5KIyCSBSVkDpwgPFLnpOP4cRyjrn7Io0xCn_rogpTivSbgmWm_ftPzSBl4B4ICBVUF2ZNbCITTt-_ycJQX7_EmU4ETtF8wVdhIlfrj2J5qi6XZQsKJKt1X2v4ENQeIJhu3-DW9OFtBy_GMyiDUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N2fgF5wbTa5zCO-Nxm8FIDdzh1hPOZJSVc25zBa9roJRmydCWDDCRal18lpEcXNBhkSJrJAkS24eU4Kl5zj4NOlLFD4jafXA_3jASXT0D8weSEeStb--UtI2-f4ForOA40WcMB_SKlAfCKgsQlgaRcKZTN68m424O_iSz7GooKiUqcJRsF5QcGFN2vWn-NSpNWWqxIsqefunAdOYsnpfRfP8QGRptbRZRpsLFDaKkgoROS7FR9MolU0ZOCCwLbucj5yHb0-A_S0eiJ6iPYWx8i5frhdu83jvJayMBlzaewi8vKv88lQtnkYNDWmUdJp6LuYmPFJOmempeMMSJ7aVlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PMHeuyfUvKBFxMEkV_qLU8yYGU56kXDZ0ryrn1tKzbKDxXWS2VHf7jTdoq6X6xaf83LY-duo1bt4afUof7whvtazKCEwIxnWaNWZYXXGLKO3VC3_qLcuqJZ9J13ZbEMa856_5Pwjmzg0c9gLWZz0Ff4Id1Dh2KKUsthB23zE-dQHO5ZWkSPJuOLWybNPUIv9c_rq8y3WATvbHdY33soPhNCpip-SyhtmU7Ysvq6NKavdY55Kz-QupkOvo5pyJ6eZ5UX9vI8gxjwPlzOkoB6tgLM7SEfnO1dITVqGYe1WqG-Fq1DSbW1ssmRpTf3VI12qlgsRFCsMvbSmD7Xqzvhu7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wver0uOxHLQidrW-F0IujEVt5d4I-TYn3P2gw7U8Md7X7ebajtJv5OW7FTIoWWbqdRIRYuzQ5Fw-BjsjgN3INZ01peqsnPfyidC44mFqbAGM_WYoOva7Fdy9dRpsam7YbSKLSS_NGWwjZI8aYXs4zvjEFfNfkmVmMu4LlbW4Wdmin9if4jBfO9STbTerpoM5v8uUcluQcxtE25Sl_0ZQsYY_BCyvwy0TE45n5aI2FiVd3lpO9_pBXadFit9nmqQz7js3ExgtGf4CHE-cgm73AoovpJ15qsGptR_NcQWNjWzg6GSn7_RrDL6aBXZSksfyTZUH0x0jTJrxrTcrOvpjJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LEkcRt-eNExCMsgJd49rD-eKdpErFBDIpbQ2o5X2ReGex1mmHVJDFQn259Ho-CsdFahY_K98-p7mTdK25cHjxzA22inpMhvEtysGYzbu7d0wzh2jaErTYj7UatfqbcSYtkdjI1L6K_PGV5nYDRwB-6dHy1RoQKesyRr3jJBp-orkTS2acSdt7mT7wLd4htLvQj-tf7yLxl-61WgWl-fEQH9pX43ftecG64Tc8O4op68LOlaw9OPbd4LXEbcixXfPYp-fMCz_xs8fXo_MU81C98asZYRSDjZBuAFArPKIxL1kmwMv7sJ1K6jU4LfU_dPU8ivbxbZ-4zhgyZgKetq7yA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آخرین وداع مردم با پیکر مطهر رهبر شهید انقلاب
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/446598" target="_blank">📅 09:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446597">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675844bc07.mp4?token=SSZWfN138PUxDjwccbdUKiZqdckYc82Rm3JaC0FDHPF7bIqdfoAdCgfHo7yqEP287kyie0b2CyjeukBFhb6a1ctFikm8l3ea6UqLdlYvu2ZIfvg8xNR5Te_g2ypoaWBqrgkRh7fhMbEGvuMLqH8lXTxiSAS3EjmLUSK8_sh34a3tmJpj7VgEPMCfJ568sKmgEPzF5zO56rsDmrHIRyYxIFyGveWjgP5mf2ZWG1F353D2A34UQF87lEvUAQDuN_5rgo1I-QiwTWxd_E6hNAT5CESd3A87uRT_rYqwcrDPQw1XHEqiGX4qpDXmCPOahuDwvemJ18bRIfTsmj9zMspmkQX8iHnavyLqjLTe1bR-f65l5YmKDFv_Vb6kC1UlaF__kr_zGpPUn0tS2NpkUL786un-pYgZM_J2Dw86i7v56LA68iwLZMvkBbyXXgws3Bo0sfxB4gaTo_3T-CA6DJLt2fpHpBvxyC1Pd3IZn-_5MDcfnY5IoqxYuLCmlW7xI_cXjWqdFzKEpDJeFXS8mp_OnpNaluh5IKZ6ZRdpg7_DgrNV9rE8YUrLNJKrVmXOZvDgJPsdvNDtvIU-sr4Fp2A0Jnyitn-I105IjgmTdIDozTCIx8md5wmtdVjQGmpBOMRr3gga65kkXoxwKPbE75LgCYTuiMa_tNrLLR8Sq_bjjWY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675844bc07.mp4?token=SSZWfN138PUxDjwccbdUKiZqdckYc82Rm3JaC0FDHPF7bIqdfoAdCgfHo7yqEP287kyie0b2CyjeukBFhb6a1ctFikm8l3ea6UqLdlYvu2ZIfvg8xNR5Te_g2ypoaWBqrgkRh7fhMbEGvuMLqH8lXTxiSAS3EjmLUSK8_sh34a3tmJpj7VgEPMCfJ568sKmgEPzF5zO56rsDmrHIRyYxIFyGveWjgP5mf2ZWG1F353D2A34UQF87lEvUAQDuN_5rgo1I-QiwTWxd_E6hNAT5CESd3A87uRT_rYqwcrDPQw1XHEqiGX4qpDXmCPOahuDwvemJ18bRIfTsmj9zMspmkQX8iHnavyLqjLTe1bR-f65l5YmKDFv_Vb6kC1UlaF__kr_zGpPUn0tS2NpkUL786un-pYgZM_J2Dw86i7v56LA68iwLZMvkBbyXXgws3Bo0sfxB4gaTo_3T-CA6DJLt2fpHpBvxyC1Pd3IZn-_5MDcfnY5IoqxYuLCmlW7xI_cXjWqdFzKEpDJeFXS8mp_OnpNaluh5IKZ6ZRdpg7_DgrNV9rE8YUrLNJKrVmXOZvDgJPsdvNDtvIU-sr4Fp2A0Jnyitn-I105IjgmTdIDozTCIx8md5wmtdVjQGmpBOMRr3gga65kkXoxwKPbE75LgCYTuiMa_tNrLLR8Sq_bjjWY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
باید برخاست، دنیا با آنها و مولا با ماست
🔹
لحظاتی از شعرخوانی محسن محمدی‌پناه در مصلای امام خمینی(ره) تهران. @Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/446597" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-446596">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpQoYbU0yiRc7Bi6cLCuNTBBG1-LOburSVALSCukkDr4sT3Wnf6ACmWrxSr99LsE4_lF_4nZOZ04wOfkNI1zn1C9-lVyJh7r6N3tJR9530IYjI1GmVcPlRhD-8N83TyubFt_7Mr4gxKapVx2ilg_QSwFEp-SliUAakum9n4IZscYuimZz_dwo1_w6p4auErymYn9GszYkcsv3dAWGZk9GmEfiTu1eRauod-dI7ddjp5LMuKQEwecihukPDeYJeftCe8rBHWUrblYD5qIFimzXJVVO9GebLj9mbu8uoqzAK7ywi_saWy8rrcF_-bktEnEjPNAKa4htEdCy8X9eoh5PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: قدردان همراهی ملت پاکستان در دوران سختی هستیم
🔹
رئیس‌مجلس سنای پاکستان در حاشیهٔ مراسم وداع و ادای احترام به رهبر شهید انقلاب و تشییع پیکرهای مطهر، با قالیباف دیدار کرد.
🔹
رئیس‌مجلس در این دیدار گفت: ما قدردان مردم و مقامات پاکستان هستیم؛ مردم پاکستان، دوستان دوران خوشی و سختی هستند.
🔹
رئیس‌مجلس سنای پاکستان هم گفت: من چشم‌انداز روشنی برای ایران می‌بینم و با پیشرفت ایران، صلح و ثبات در منطقه نیز رو به جلو حرکت خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/446596" target="_blank">📅 09:20 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
