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
<img src="https://cdn4.telesco.pe/file/gnvcvypaf-6VsBmdxcUJ2vPtKzhOnkF7u8zOdGGR7p2RzYpIeSXv7umsxHN1VZO73VW9iawa0VmJ4ZIu8s5Apy6KpV8IzAjXsSMQdUSxx_pDhjbkKIrm19rpDXyKpeQ_tHQG0Nkj5_WAADcz82dtlwG36YD7cjxy9HZHu4tZGC2VsFs5FciaPtUG1XRp7fQPtWqT-kfLTl2YnQPFEiGXZwKne2CFtz96HVyYw2Qt7zh23aLHJs71x7Qzw0t39p4i-6et8mlexI_IEq3wx3Qndu-YAp7V-N9dIorebuEAL37_ZewRS-BaVjhBAPop5njd0pX0YgzqzZKqerzdBCpuRA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 17:39:15</div>
<hr>

<div class="tg-post" id="msg-449661">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e80abf18b4.mp4?token=USns96JCtuD0uArWypACUPdvoBx8-IcGmW-xUdXQnfl_FNFMLcMH6DWrGfWho4VJve-16Qb15NNNqa-t7Dikny71aJLGeQbFzBujIUj98zScNtfzqeBBnki6C74J3v0P-Tz6VoOsBwnXh5DM9k2pbHoXAql_2Y3s_ekUHC7pShaa8qLmOSaLMdRJO9SZ4S0JnjR2LJjamtAkKfjUfcJpLBYZ2xNbuILZMFOtFhq0wM4Tu7qbI0dtFSPTQtf2_2HiKlAMlqYK7LU2apMD6DE-WRC71b7C6h6BSymb8EHbz2DnleC-yMxAdfPtkvyOw9Iy1TL5uq64iZv3fnrraSGiPxVXszgy3rAqUI6ftbbbZgRReondL-6VwHsj2LethZXTCqhOeXV69Nk7DiZTZT7VUAwXj2ZFo4jnC8oztkNH9qXsx3px-wmNNK-cP_3cKElvLho97FslRbU0NDjkz1ap-sXPgoLCgn4c0bfKhZHr8PCRwR-jDNpQGYySJg_S0PAaTupeY74oW0l836rBJDPoe78-7nYTVEwX0u2-YMxUFPKEfBIsSLKoFVredUnl-i34a5vFivjKcuvall_swbSJLDBp_7zZabwamocOSFdiaWo7JfNE8SvQiyOioTruXyK_A4y2vuTvx4csSmt5RrPC4dwglqGBxDzVqBDP3tHNjTI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e80abf18b4.mp4?token=USns96JCtuD0uArWypACUPdvoBx8-IcGmW-xUdXQnfl_FNFMLcMH6DWrGfWho4VJve-16Qb15NNNqa-t7Dikny71aJLGeQbFzBujIUj98zScNtfzqeBBnki6C74J3v0P-Tz6VoOsBwnXh5DM9k2pbHoXAql_2Y3s_ekUHC7pShaa8qLmOSaLMdRJO9SZ4S0JnjR2LJjamtAkKfjUfcJpLBYZ2xNbuILZMFOtFhq0wM4Tu7qbI0dtFSPTQtf2_2HiKlAMlqYK7LU2apMD6DE-WRC71b7C6h6BSymb8EHbz2DnleC-yMxAdfPtkvyOw9Iy1TL5uq64iZv3fnrraSGiPxVXszgy3rAqUI6ftbbbZgRReondL-6VwHsj2LethZXTCqhOeXV69Nk7DiZTZT7VUAwXj2ZFo4jnC8oztkNH9qXsx3px-wmNNK-cP_3cKElvLho97FslRbU0NDjkz1ap-sXPgoLCgn4c0bfKhZHr8PCRwR-jDNpQGYySJg_S0PAaTupeY74oW0l836rBJDPoe78-7nYTVEwX0u2-YMxUFPKEfBIsSLKoFVredUnl-i34a5vFivjKcuvall_swbSJLDBp_7zZabwamocOSFdiaWo7JfNE8SvQiyOioTruXyK_A4y2vuTvx4csSmt5RrPC4dwglqGBxDzVqBDP3tHNjTI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ بمباران فرودگاه صنعا توسط جنگنده‌های سعودی  @Farsna</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/farsna/449661" target="_blank">📅 17:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449660">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/964887b02e.mp4?token=AktjlVJJfV8glH_4378gZxFM_NKEuAzqAqlHZM59shmW04ZbbkTkb9pOeF-GHJBd_fgZsreQbWMCtpZdjElVfX788DNfsf3zGr2tXZicTA6gHeFMrqGFFsWBceUWnZEySU1N1k2_M3ju1CVMhw5jHX5izkYgz7DmO9XCYrds5d7OGh68Eslg3nEXXzF8v_MRVmeHa3803NrMokCuINly_a2WVDTUl5KcsqgF3Gbn8YPPmtY1N5BM1VbtmST8l8Ioo26kWscik4d2NDaSrJWA7_bXEOrCXHh35StMQ4Tk6wEj-NjpF5j1DONJlQLXcQT4Dbjauwq5JlUMWxAQpQI6Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/964887b02e.mp4?token=AktjlVJJfV8glH_4378gZxFM_NKEuAzqAqlHZM59shmW04ZbbkTkb9pOeF-GHJBd_fgZsreQbWMCtpZdjElVfX788DNfsf3zGr2tXZicTA6gHeFMrqGFFsWBceUWnZEySU1N1k2_M3ju1CVMhw5jHX5izkYgz7DmO9XCYrds5d7OGh68Eslg3nEXXzF8v_MRVmeHa3803NrMokCuINly_a2WVDTUl5KcsqgF3Gbn8YPPmtY1N5BM1VbtmST8l8Ioo26kWscik4d2NDaSrJWA7_bXEOrCXHh35StMQ4Tk6wEj-NjpF5j1DONJlQLXcQT4Dbjauwq5JlUMWxAQpQI6Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مراسم بزرگداشت امام مجاهد شهید در مصلای تهران از سوی رهبر معظم انقلاب برگزار می‌شود
🔸
سه‌شنبه ۲۳ تیر ۱۴۰۵ از ساعت ۱۷ تا ۱۹
@Farsna</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/farsna/449660" target="_blank">📅 17:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449656">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMNfienL6bLrnNScIdPIDGwEITDQQ91VIdWbaGWqnCAH-YLK6IMt9Ugjpd6HZZNEU1V8nMcVwK9oVB-uA94XB6p_8xvlSAZ17lkw1znehsCKNa4CMQPIy6sENUK-WtJZ272w6GWgsGVc6Ak_T2Sdn8JGL8kbFj03F8fx7000cLkTquD8pZv4XjyuQ_kpwtr-GOD7pBeXCtXmsLiBJyEG479-JitfPqiaVmfANVQ1bXxo84X7rlmv2BW4Koa0mq3gcIK0YVGNMGY5QCQnr7g7IE-QrgG1_5YRHl4OyNEniqbglVYQ99xcimU-S4gW4OxSI6wg2qifXWTBfbMOzUUxKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه‌قضائیه: پروندهٔ عباس عبدی و مدیران روزنامه اعتماد به دادگاه رفت
🔹
قوه‌قضائیه اعلام کرد پس از انتشار یادداشتی از عباس عبدی در روزنامهٔ اعتماد، دادستانی تهران علیه نویسنده و روزنامه اعلام جرم کرد.
🔹
در جریان تحقیقات، علاوه بر شکایت دادستانی، حدود ۸۰۰ نفر…</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/farsna/449656" target="_blank">📅 17:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449655">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6416043ef.mp4?token=Www2RBP1ifONI89-O3au_YPelLcH_mYiStwXsrWRcOjWoK9hLBNGys0pTOndD08Zr1u-vUviTDqh1-MuVQw01fzoerMHok2E3g_JvpUHkrfTICYPgEvjncya4USVxga5lw1DjHVLSDWNlGyeQcB70ohgOLHhLsksV4DxckJGpBYO1kofX4idfsFk81b-2PwwvvDysXhxbYYX8MbTJjEAW2Q2jjhT4sIp-pkabhapCmfCMU77GQi6GQnOwjpNmz-3c45-XFOb5SKzWs3yty2X60E8Zz-E5kVKNyYf6sNU2JSC1z14RUCLcTLnMatTAgpKA7Ipln_fYN1H2ThGIwCSTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6416043ef.mp4?token=Www2RBP1ifONI89-O3au_YPelLcH_mYiStwXsrWRcOjWoK9hLBNGys0pTOndD08Zr1u-vUviTDqh1-MuVQw01fzoerMHok2E3g_JvpUHkrfTICYPgEvjncya4USVxga5lw1DjHVLSDWNlGyeQcB70ohgOLHhLsksV4DxckJGpBYO1kofX4idfsFk81b-2PwwvvDysXhxbYYX8MbTJjEAW2Q2jjhT4sIp-pkabhapCmfCMU77GQi6GQnOwjpNmz-3c45-XFOb5SKzWs3yty2X60E8Zz-E5kVKNyYf6sNU2JSC1z14RUCLcTLnMatTAgpKA7Ipln_fYN1H2ThGIwCSTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
پاسخ در راه است...  تصویر معنادار یمنی‌ها در واکنش به حملات امروز عربستان @Farsna</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/farsna/449655" target="_blank">📅 17:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449654">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113aab1c72.mp4?token=TJwnEhGpYWqkh8nWxSGUyjYI7Z4vubL4bRnZBagULa1tH4b3bYXXbMtSYgvPw7AzJvDQEosrheF31S2hPF5_4V6WoaeRmrTsmg3g6RRBrnLNq6zNa6RdLEJ7CAauBzYHcqlbbeWsBvxOmucI6srqtBn84WcWYJ32d3blRDGlatKs70yGRKQWL7JMzdb1-D0wifAtyFvcnTchW23wnvLwKGpHgTr4ql_V9HD6qslvE2VmAq0MCu7L2IWAc6QrjraZNYcRLdzlQZzjoX8QmBgPbkcKNVZNuM6VRtLSPq6iT2zKAqFGAEWnAqkekGPWqZ6p5ScHCC9WIy0nmXZGgYz1DIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113aab1c72.mp4?token=TJwnEhGpYWqkh8nWxSGUyjYI7Z4vubL4bRnZBagULa1tH4b3bYXXbMtSYgvPw7AzJvDQEosrheF31S2hPF5_4V6WoaeRmrTsmg3g6RRBrnLNq6zNa6RdLEJ7CAauBzYHcqlbbeWsBvxOmucI6srqtBn84WcWYJ32d3blRDGlatKs70yGRKQWL7JMzdb1-D0wifAtyFvcnTchW23wnvLwKGpHgTr4ql_V9HD6qslvE2VmAq0MCu7L2IWAc6QrjraZNYcRLdzlQZzjoX8QmBgPbkcKNVZNuM6VRtLSPq6iT2zKAqFGAEWnAqkekGPWqZ6p5ScHCC9WIy0nmXZGgYz1DIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راز پرچم سرخ در بدرقهٔ آقای شهید
@Farsna</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/farsna/449654" target="_blank">📅 17:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449653">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRfzVH6ieI9GcIQHT6O0X-j8g0D1Td0Y5LBR9kU4euSskkwy0WkiG6FwVDwbd_aBzjQOvzYpCzGybSzFR7iSSclloA_CttBKa8Nl-8dIc9qHxtK9r91txKLjNdgE40xoVl1fp8igJNtUwx2EptTzV3fnPPgSJPjeJVYgcaCaOp1v9Bgz2cRQjVV6xuPvBud92V31VSt1pzK4nVmWIliuQ1SjqHl5DE_6onMJp4ZJzym8Om-iaz5_IINkk3P-kDMQzxdpcctSflGevPnD-liV015ekoPLs5ja2xFxyc2rzg59IifGvNN3k3A0he5EEX5HafKSZxWXGDTr1-Slaqjwvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: حاکمیت و مدیریت بر تنگهٔ هرمز را با قوت و قدرت اعمال می کنیم
🔹
سردار محبی: آمریکا با مداخله در تنگه‌ٔ هرمز امنیت تامین نفت و گاز جهان را به خطر جدی انداخته است و باید جوابگو باشد.
🔹
حاکمیت و مدیریت بر تنگهٔ هرمز را همچنان با قوت و قدرت اعمال می کنیم و بیگانگان و همپیمانان آنان را وادار به تسلیم در برابر اراده ملت ایران خواهیم کرد.
🔹
همانطور که اهداف متوهمانه سردمداران آمریکا در آغاز تجاوزشان را به بازگشایی تنگه هرمز تنزل دادیم، در شرارت جدیدشان بیشتر از گذشته آنها را به خفت و استیصال می کشانیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/449653" target="_blank">📅 17:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449652">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnoR_YDdPHhyEc_5W4y0DSgPDgL2xIjDJuucxn4w6FOZ-kG75as4r97ul3fibxN5xVUmemTRU2BNBBKeixtzBQCph428D64ZoxalhO8hmDNBY1IWfDQfko1p_mnN3f-UlURqXycw1Pp994SKdZBx6r-D1VnWBmD3FeBQmebEiKH6cxySxEZAvXlz5ObYFUNqv-nzDaNXtt7MhAC7oJCryvvKUFaluNb5pBLNk1qXojGVZUmfniJfsY0SCShqQv1ouxpN8_JUX-_q7f0AhdUy30viXrri8EqaqkKGqWqjUM2UBJf8XoTduHaD9ST_ehj2emmcmqUGDMfJSfI_V8qHNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌‌
🔴
یمن: رژیم سعودی به ما اعلام جنگ کرده است
🔹
وزارت خارجه یمن: رژیم سعودی آغاز جنگ را اعلام کرده و باید مسئولیت کامل این اقدام و تمامی پیامدهای ناشی از این اقدام جنایتکارانه را بپذیرد. @Farsna</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/449652" target="_blank">📅 17:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449651">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOdYyprw2eaMNzvNtPc1LOh4E-tnokrVVrjWFg0fqBTRllK-6otQDYZAZdUMKVsiC5qTbJOeTx4GUhjeopuSFhhhMozLydzb8DSK2TtE4r41GOEIsK-IPg27jOq54-1Y1jo8JC7i8xv490XVSemiJDs-IH0rcnn91_qBFyzRtK7PuEFslp5WRO0QIJsowLy8r624dcCsaFAKuuOy0XIglI1s8Z8ocNGvhwbaX3opYkRnBmjQGb46Kp8UsuYlq_OLpSy1-Y9INFwnHGV1anT_LuEACZALYkQBot1nUMSbREfw2WFpaorR7z-krK3SG6B0fZfZ4giPcyFF6f8HkK3mPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصمیم اروپا که آیندهٔ اینستاگرام را تغییر می‌دهد
🔹
تک‌کرانچ:  اتحادیهٔ اروپا قصد دارد پس از پایان تابستان، طرحی برای محدود کردن دسترسی کودکان و نوجوانان به شبکه‌های اجتماعی ارائه کند؛ طرحی که می‌تواند قوانین جدیدی برای احراز سن و طراحی ایمن خدمات دیجیتال به همراه داشته باشد.
🔹
کمیسیون اروپا با اشاره به نگرانی‌ها دربارهٔ تأثیر شبکه‌های اجتماعی بر سلامت روان و رشد کودکان، در حال تدوین مقررات تازه‌ای است.
🔹
بر اساس پیشنهاد کارشناسان، کودکان زیر ۱۳ سال نباید به شبکه‌های اجتماعی دسترسی داشته باشند، مگر اینکه شرکت‌های فناوری ایمن بودن خدمات خود برای کودکان را ثابت کنند.
🔹
اتحادیهٔ اروپا در ماه‌های اخیر فشار بر شرکت‌های فناوری را افزایش داده و قابلیت‌هایی مانند اسکرول بی‌پایان و پخش خودکار ویدئو در برخی پلتفرم‌ها را به‌دلیل مغایرت با الزامات حفاظت از کودکان، تحت بررسی قرار داده است.
🔹
این اقدام بخشی از روند جهانی برای افزایش حفاظت از کودکان در فضای آنلاین است؛ روندی که در کشورهایی مانند استرالیا و بریتانیا نیز به وضع یا بررسی محدودیت‌های سنی برای استفاده از شبکه‌های اجتماعی منجر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/449651" target="_blank">📅 16:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449649">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgZyHv1FrUuvsoL51QtduAtHfXwC2oNpRI2hoH7kKF0BYdzS8qi1gMoYdMmJZHGzs7Md7h4xzUAMiOG4zPtlT3IXdSqgzAkIwJ0Mrn-2UjKsWvb143B7ds7hhISrB2kIQ7BAnm3k7t6WZAApI6llgrmAzSRKUA9ZGR_6lIKgw0gQu9fzQTMptM22PA3uKKfvr35ItGtuTaM9ntxUWFs8_P0xyRJYZsvR8-3554uUbYOjzHZpiCWZuLmXLXfEMCdLO3wXpViFvtpJn4uV5kivKFfRkB_Ucp8xmNFomqMdvy3Uf_zZLPkeTFStlPqHqgQ_W-FGSVOl0e-yjcMe34UlbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ادعاهای جدید ترامپ در مصاحبه با فاکس‌نیوز
🔹
داریم کنترل تنگۀ هرمز را در دست می‌گیریم و بابت عبور از آن هزینه دریافت خواهیم کرد.
🔹
توافقی وجود داشت، اما ایران آن را نقض کرد. تاوانش را پرداخت خواهند کرد. @Farsna</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/farsna/449649" target="_blank">📅 16:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449648">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سرپرست اتحادیه سراسری کانون‌های وکلای دادگستری: طبق اعلام سازمان سنجش، آزمون وکالت امسال ۱۴ آبان برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/farsna/449648" target="_blank">📅 16:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449645">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‌
🔴
سخنگوی قرارگاه خاتم‌الانبیا: به سران کشورهای منطقه هشدار داده می‌شود هرگونه همکاری یا پشتیبانی لجستیکی از ارتش آمریکا، به‌منزله جنگ علیه حاکمیت و امنیت ملی ایران تلقی خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/449645" target="_blank">📅 16:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449644">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‌
🔴
سخنگوی قرارگاه خاتم‌الانبیا: ایران با هرگونه ایجاد اختلال یا ناامنی در عبور و مرور کشتی‌های تجاری و نفت‌کش از سوی ارتش آمریکا، خارج از مسیرهای تعیین‌شده ایران و بدون مجوز نیروهای مسلح، با قاطعیت برخورد خواهند کرد.  @Farsna</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/449644" target="_blank">📅 16:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449643">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
سخنگوی قرارگاه خاتم‌الانبیا: به‌هیچ‌‌عنوان به آمریکا اجازۀ دخالت در مدیریت تنگۀ هرمز را نمی‌دهیم و نخواهیم داد.   @Farsna - Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/449643" target="_blank">📅 16:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449641">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff97123423.mp4?token=kdf1kpjsDqqjKsZTCkMNhE-oiIPDKhyRRzAQrNB6XO00E6SPoBl9W2CMP2XOK1wpKxRx9nn-Il2SGKqD-xgYOqTHKYvyMo0U-ETsjLCVMWOeeWle0V27UMnK9uhlv_g9yTzFWFn5BHZCLrSFcQNgNmQPAyYc6mJjliS9vBfBqIFGTqa6IUN1vDLfp250dqfuas1lblPq-gMcPqA6tfF6MgXvFKOjDryXXsCmGZAvK46XvE23CgKJgJnNGe_AYYUmDYhEGbTRQ2y1HEc04mqMgBxvtXTcy5T_MJIfRZg8synJU7zdcTu5aBL20ggLamcm-IA0eFve1_sZZtEAjrJizQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff97123423.mp4?token=kdf1kpjsDqqjKsZTCkMNhE-oiIPDKhyRRzAQrNB6XO00E6SPoBl9W2CMP2XOK1wpKxRx9nn-Il2SGKqD-xgYOqTHKYvyMo0U-ETsjLCVMWOeeWle0V27UMnK9uhlv_g9yTzFWFn5BHZCLrSFcQNgNmQPAyYc6mJjliS9vBfBqIFGTqa6IUN1vDLfp250dqfuas1lblPq-gMcPqA6tfF6MgXvFKOjDryXXsCmGZAvK46XvE23CgKJgJnNGe_AYYUmDYhEGbTRQ2y1HEc04mqMgBxvtXTcy5T_MJIfRZg8synJU7zdcTu5aBL20ggLamcm-IA0eFve1_sZZtEAjrJizQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادعاهای جدید ترامپ در مصاحبه با فاکس‌نیوز
🔹
داریم کنترل تنگۀ هرمز را در دست می‌گیریم و بابت عبور از آن هزینه دریافت خواهیم کرد.
🔹
توافقی وجود داشت، اما ایران آن را نقض کرد. تاوانش را پرداخت خواهند کرد. @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/449641" target="_blank">📅 16:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449640">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yysd4vn5NQ_ZnPIB-q6SZ0CT41bgBA1R6cu31sNJvYDGkaF7XVeg8hRpz3ewo_kqyBicASvBqdcTKd_rwTKyJTQWcoaReAR-XyDfP5atfflXVznBQq4pEj6g0Z9Pg04dv3W7pe2tN7EMsw0CPGYuys-H2_mqWohQimHjdQj96S0O895i5io5GCEKoYyQpHbzq45XTggw2qsX3Ms_raRvA9eAIL1bdKF7Zt_S7mmzlQ9gHaOd93AOQ-8OXd7Ljqgr5cXhK3vHswpbrSxoUnnUfij0FNizkW3EtRWVi0DZ6qi_j63oc0dMhZjwsplGl0cgkoFZqMMl79Or88D1uZHL-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران مدیریت طلای کثیف در سواحل خزر را کلید زد
🔹
طرح منطقه‌ای مدیریت زباله‌های دریایی در خزر با هدف کاهش آلودگی پلاستیکی با حمایت کنوانسیون حفاظت از محیط زیست دریای خزر در سواحل شمالی ایران وارد مرحله اجرایی شده است.
🔹
این پروژه  شش محور از جمع‌آوری داده‌های زباله‌های دریایی تا اصلاح قوانین، افزایش بازیافت، کاهش مصرف پلاستیک، آموزش عمومی و اجرای طرح‌های پایلوت را شامل می‌شود.
🔹
قرار است از ماه آینده حدود ۲۰ پروژه منتخب در استان‌های گیلان، مازندران و گلستان آغاز شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/449640" target="_blank">📅 16:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449639">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a129099672.mp4?token=RTbTB8vakfzqy5AytZRSRUho-Ou1v8TqskNWSZ9SeLGNccw2JeG3XRFnRBH39nSuCIHpf7XdtXseJyQpB1sV4LkZqvFuIQgyBMYjBBCfz71rJ1OTtmydjOqA83el3cEkNovvk0f3K58tgwDwtX1qq9LVUlkzy0P8hKxaoTXzCxaEElOS3GIP2jjNY_Du3v6WBQ946rlIscTAai1oE_tC32bNDbPvgBRkHDSjiv84IAVSMuZMzFXaSkpXgocH_P1ICEFe1HP-LPeACiymVHxyF5nE_Ko9XOfnsH31kGp74N1w_EL4RWDNDna_ValX21O6J0mHm3UVP3vNAL9FRDN0PbVweeCs3oSnybkU8smHLkVsIWzXB2PyNyQXd7Dh2P_f-flGIpRqpblTIGXV1zd93v3gbW_DOib8mpqDY877-KoRT1n2atGNhHW-ZUB-fk12osDY98Y29IT-BOX7Tr66TXt53L5Jqr5PaThFVoaEFNWQuxlw8KYxbi5O15cGbC3FX7ylYpXoHPTC8ZIlXfyZhj61gPdeJPMLfrRP5X45evJwqArFr-owtH7o9IBmlKuist4wXe2K4bZKP7sA9TEjSfhbxXrP00XWhDXC1rmlnpmiDsl6uEVQIU1tUdSwZ8dktKfEcI_WD-3nd_zrhd7uRchoyPymPKfPVRmp4fvFdjM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a129099672.mp4?token=RTbTB8vakfzqy5AytZRSRUho-Ou1v8TqskNWSZ9SeLGNccw2JeG3XRFnRBH39nSuCIHpf7XdtXseJyQpB1sV4LkZqvFuIQgyBMYjBBCfz71rJ1OTtmydjOqA83el3cEkNovvk0f3K58tgwDwtX1qq9LVUlkzy0P8hKxaoTXzCxaEElOS3GIP2jjNY_Du3v6WBQ946rlIscTAai1oE_tC32bNDbPvgBRkHDSjiv84IAVSMuZMzFXaSkpXgocH_P1ICEFe1HP-LPeACiymVHxyF5nE_Ko9XOfnsH31kGp74N1w_EL4RWDNDna_ValX21O6J0mHm3UVP3vNAL9FRDN0PbVweeCs3oSnybkU8smHLkVsIWzXB2PyNyQXd7Dh2P_f-flGIpRqpblTIGXV1zd93v3gbW_DOib8mpqDY877-KoRT1n2atGNhHW-ZUB-fk12osDY98Y29IT-BOX7Tr66TXt53L5Jqr5PaThFVoaEFNWQuxlw8KYxbi5O15cGbC3FX7ylYpXoHPTC8ZIlXfyZhj61gPdeJPMLfrRP5X45evJwqArFr-owtH7o9IBmlKuist4wXe2K4bZKP7sA9TEjSfhbxXrP00XWhDXC1rmlnpmiDsl6uEVQIU1tUdSwZ8dktKfEcI_WD-3nd_zrhd7uRchoyPymPKfPVRmp4fvFdjM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت تکان‌دهندهٔ قهرمان وزنه‌برداری از عذرخواهی یک آمریکایی به‌خاطر حمله به ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/449639" target="_blank">📅 16:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449638">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5a7N5rfZU2DcI-LZ0AXr00YUCXV2WEktmJM6XszsWvrDglFKdR7GjsQmRCLQH1G_eK4QMzA7N-qmotipSDFFG5cS98hrCiWNMEQDALKe5EAo6mNfBntHMsug9bTKc6ZfQlqdUVBHKGgDH6XrTOG4cpRvoelb3Kc-v1b2k56U_Qwc0PzaR_IWpcRQf7sYm0vZV0nk0RZnbOa-VTNC8KbCSdP7wOoKAq194myDgp8MHVbHZeV311uVsx84psvQ60Z2qYzA-Jgpb66IpBq-eBeCqPxlWVjd0c7L9Me4NUGR2hYFIS2YXsfkbXkdoNWSp83y9FxQ443sAZRswEHnG6oug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درنای بلژیکی «رویا» تلف شد
🔹
درنای سیبری که ۵ سال پیش از بلژیک به ایران آمده بود، پس از ابتلا به عفونت شدید ریوی تلف شد.
🔹
رویا که بهمن‌ ۱۴۰۱ به تالاب‌ فریدونکنار آمد، با «امید» (تک درنای سیبری) مسیر جدیدی را در زندگی آغاز و پس از ۳۴ روز اقامت مشترک، این تالاب را به سمت سیبری ترک کردند اما درنای بلژیکی مسیر را ادامه نداده و در منطقه‌ای در عباس‌آباد تنکابن در مازندران فرود آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/449638" target="_blank">📅 16:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449637">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e523458f.mp4?token=hrMyoV3Qwv_CnnCyx_K5BkDpUyDyrvekmCzVlZDeIhWTayGveXmouFmdKJxcdiS9GZjGcKy4p3QqQsUn7UcYwFSPQ_nIwOlSJicwXlPSBVntK4lr7h89r_3SYOgTspg7tKSOV1UIl5_VpBNAMPNCCbFuj9_Rh3atV3EPveUdw2Jbi-IB10_cdbqFCmizScTqzpPxVkNBjJI433O0qfwg1LoVpH-WUlF4tc2TeoxgxSOc5Y_7uOj-qiNNbyH4D2ctwn_qVVd7Wpj9v6PYqlHbcfHdxMe5a8WNBZLv3tcFUgVINH4g1-NI-k9jY0aLwNmkGsznwBE-dJxKiw9YnqyTYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e523458f.mp4?token=hrMyoV3Qwv_CnnCyx_K5BkDpUyDyrvekmCzVlZDeIhWTayGveXmouFmdKJxcdiS9GZjGcKy4p3QqQsUn7UcYwFSPQ_nIwOlSJicwXlPSBVntK4lr7h89r_3SYOgTspg7tKSOV1UIl5_VpBNAMPNCCbFuj9_Rh3atV3EPveUdw2Jbi-IB10_cdbqFCmizScTqzpPxVkNBjJI433O0qfwg1LoVpH-WUlF4tc2TeoxgxSOc5Y_7uOj-qiNNbyH4D2ctwn_qVVd7Wpj9v6PYqlHbcfHdxMe5a8WNBZLv3tcFUgVINH4g1-NI-k9jY0aLwNmkGsznwBE-dJxKiw9YnqyTYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادعاهای جدید ترامپ در مصاحبه با فاکس‌نیوز
🔹
داریم کنترل تنگۀ هرمز را در دست می‌گیریم و بابت عبور از آن هزینه دریافت خواهیم کرد.
🔹
توافقی وجود داشت، اما ایران آن را نقض کرد. تاوانش را پرداخت خواهند کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/449637" target="_blank">📅 15:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449636">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6DGmRIBQgDdcpOlE0Cq_QoDiCpelVwgI3_CqXzMhF5JOIf3h47___tJ0zDlBomDJC6XUlZXShKi1SeF5dAshRCWczoEFyshGA8AKqZZsl0s_mDkCU1VX6KwpmWEL391hPoor1D1-euvW6YsK050RmQtzj5aiTrhgahJID-7aChEgQ0JFet2rIWZuU8j8nhbZQ7ayGSuCEg7kJDTJXtOghma5SY7frjv0moRIYCoMbcGsqmqiD7xo-OAYBW9o3MMg0dKpoA60FFhmeMT-bK0KfdaoYaDh6OS8M3pQXk7nM9lYloqRAhBr_vctkF8hmvVtqeEI44seADuN5CUW3wqXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مخبر:‌ عقب‌نشینی از مدیریت تنگهٔ هرمز در ذهن هیچ ایران‌‌دوستی جایگاهی ندارد
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/449636" target="_blank">📅 15:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449635">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/850d67ec7f.mp4?token=LWMUstj6aQeAGYQXQ_r74sDLRYADwb2EvHpqzwz8FgWsH-By5hh4DQU0ofsOknRnSAhl9GWkr-bmOZYIgqm-StQjuCwyusczG4eziuSE-eV1oNXZw33ofJlFWbZ3AQbiB-Y6hmF-00391NNGxzG4Eb7ZPnWXlMx_Q7-Nye1Qz61r0AHnrONPb7FbWU0HfM-mr82FNgJ6EGRt77mu0fTF5sdxPcmPIek2t1Dghi2ePDmc2HUrWJedpL4EQx75bw8ZXlyYMzxHNY9BWHe4_ECJil1MH1z4z_HaC9v1Rmfet4EF-3NinLI35XLa0vpby0y1NTYwjMp56CmER3iZLIEgzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/850d67ec7f.mp4?token=LWMUstj6aQeAGYQXQ_r74sDLRYADwb2EvHpqzwz8FgWsH-By5hh4DQU0ofsOknRnSAhl9GWkr-bmOZYIgqm-StQjuCwyusczG4eziuSE-eV1oNXZw33ofJlFWbZ3AQbiB-Y6hmF-00391NNGxzG4Eb7ZPnWXlMx_Q7-Nye1Qz61r0AHnrONPb7FbWU0HfM-mr82FNgJ6EGRt77mu0fTF5sdxPcmPIek2t1Dghi2ePDmc2HUrWJedpL4EQx75bw8ZXlyYMzxHNY9BWHe4_ECJil1MH1z4z_HaC9v1Rmfet4EF-3NinLI35XLa0vpby0y1NTYwjMp56CmER3iZLIEgzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای تشییع‌ ۱۴۰ هزار نفری اینترنشنال!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/449635" target="_blank">📅 15:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449634">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVNEgWNVvFN08GsQ9xQS6cmwgcRmh89wrK49hnUv6zhcsirikdDmgcR2vMBpKjIrOPJZak4JvwUBaeK_1wEhtfmfy2kC58LKeHI1KBxuXt6KjrAdp_pS-D6f1lkqKrP0xjol9as03K5kIeUqEJJQajvMeHHPsP2HJwMz4_NKT2SWrNk3LhinJVru656m87DVaO06FMb5zIsB3UFpoixiGDlCSiSMIR1TTc7o8VC76pAMSJvLxV0iUoqmSd78FbjVFN8POQDj-oLGtvFUE_FnfbMGktHPbrM2hHfsmjb1_ovUhIeB6mfO6KDlC9Va9NZos7jSTe0_eFOvzJOQoxXxIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
انهدام یک پهپاد متخاصم در بندرعباس
🔹
روابط‌عمومی ارتش: ساعاتی قبل، یک پهپاد متخاصم دشمن متجاوز آمریکایی، با رهگیری و شلیک موفق سامانه موشکی زمین به هوای نیروی هوایی ارتش منهدم شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/449634" target="_blank">📅 15:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449633">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRElxhSTaa5byIhk_05pmnltL7St9Al7j0CHt59XUokXOEHNdX_zCtZ8xHpx8RX-xxUHWH06NIsNQqMb1pNAZXf3ZfX75u8ULKdLMVmphcNUre90GiUEGNQSzyx6UQLu2eYb6Jpdq_qgutX2lD_3C47wjYv2fHtfsY41zyoLf3l1M9ts5vFWCLgXtkCfxj3GWYnjiMJH9KdDpnnZP8NBsiqwwCOXb93VXEMoB4xIt55ujtp0w7vVpVia2B54Zihra6FtTxx524zmbK0WbAkxWF-Nj0rNeH4coOf2vj-cIS1D_mD4OzAwLPJm7M-3FYOq5CdMA8sXORwlpQmZ0Kbb5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عضو دفتر سیاسی انصارالله: هواپیما با موفقیت فرود آمد و محاصره شکسته شد.  @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/449633" target="_blank">📅 15:31 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449632">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTW-62nGf_HEQo8hsnhSSEPj22Y44-wUY_128ZlrPyg8Z39uNcnzcGkmEuezH1H9kVJFNd-j6V59X2RXXm9yTDmbpgwy1U8h0jGBUSoYMMb__A3EqwsvRQXZz_8Q1STsbpq2778s8Y2no-OOqdT752KVbNTc2YWqwQvep8XXXOjIFtfXTltyXj2poLls8VgbhcOwIIKzQyvXvVmq1AfEKYYm1iTVOa6COOblGwmLR6fD7q8DYNyXiiVo9me-fw3k87VhibLKsV7pVqVVF0ebEEGbZTA-B3ruy-bv_xlLBzxLy_h1406QVwaJP2tlArpEYVlOE402p9bwqsdMfZGJ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هواپیمای ایرانی پس‌از حملهٔ عربستان به فرودگاه صنعا، در فرودگاه الحدیده در غرب یمن فرود آمد.  @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/449632" target="_blank">📅 15:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449631">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3NYA0riCFFGETBkb14pjY89H1EXw3MqQldDqrPUuh6AsojM3McLvcdMqxbiJgEboLqI_vmlyiAdfSvAjx0H0EAassNDTS7bF5WiajjBV2WLlS8fJxxXQSlrg7nnbFpRaTiuA26eJDeH8V3mKbBNFPbt1baUm95Gm-wo8sS8x90fKFyY_u0bSY5V1fEjH_bQU3bP4aE0aT7XhAQql3xVKnUT0FikQABKsQHSlAbuvFitvsUT6S0OSrc52YkbGwKylBLzScJTMSqlfnkItLlt4n5PmQs9ODaMI7hqzyJMDuFDHkGAyA4mYp8vLSFyfpZjE47D7z8IeV6FumI-TE_rNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اقدام ضد ایرانی انگلیس این بار علیه سپاه
🔹
در ادامه دشمنی‌های انگلیس علیه ایران، لندن نام سپاه پاسداران انقلاب اسلامی را در فهرست ادعایی تروریستی قرار داد.
🔹
شبکه اسکای نیوز گزارش داد که «بریتانیا سپاه پاسداران انقلاب اسلامی ایران را در فهرست سازمان‌های تروریستی قرار داد.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/449631" target="_blank">📅 15:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449630">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUtwrJsAwxPrAFvdsWUvD7Ts51hWd0BNChh0h5coZ2l7mP8sLGA1ofNQF4n63_Mmp9TAwQzhEz0ZMoVctpnw5vtP7K-1ZwftDAMYRu8LgwIEQCw5RftdleJBFna5u_F4Q0d40KSYX0xcMbjXRy7UqHUmKwdyD2X_o3BBAGjr5YK473yNm6pb5vSLqK9dSAZWkNcmZLitOXevrrEeE6OMIRi9urWMzT_3LMkacMgE-rQksN150R1CX6_pozDym08K7CHX9GmsFo800TJEXU-L5S1bc1ULTUdiUobU7UOYibuEyyagaHOgo4-Imd2w6yGw_rVOHMN4-hSOHVRs_IBdMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هواپیمای ایرانی پس‌از حملهٔ عربستان به فرودگاه صنعا، در فرودگاه الحدیده در غرب یمن فرود آمد.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/449630" target="_blank">📅 15:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449629">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‌‌
🔴
یمن: رژیم سعودی به ما اعلام جنگ کرده است
🔹
وزارت خارجه یمن: رژیم سعودی آغاز جنگ را اعلام کرده و باید مسئولیت کامل این اقدام و تمامی پیامدهای ناشی از این اقدام جنایتکارانه را بپذیرد. @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/449629" target="_blank">📅 15:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449628">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🎥
تصاویری از حملهٔ هوایی عربستان به فرودگاه صنعاء  @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/449628" target="_blank">📅 15:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449627">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf09690a.mp4?token=PfiRSN6b9ScB1AXjxEzvt_EJOo_PkvpkomDGnfuol4u1NF2MrKVI774oI9Or5aMnjeTZw8V7QNrsykPsL-Lsk0qQ9l_yH2W__oZeNmKG__hzCyL7U1ipa70rAjMpTddQfBah-6gZS5EDguc-5CljuOOMbj98bjbkQtit_7FVJQiYVJ02BZwnI2LN0mYZ3vmovggM10WZcCcYieohvpoLk9_lGAHP8u_IV3ifcD8qIyX75LFVm939EXj8-aLQTaErTQReCX9Yhf8DoBAAAMxMUoiSZCs47Zns8tiDDBkAN1OjxvJUhxxxUL8Jru9hlXZ2o8-kedTmMZ17LXb9FWcQgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf09690a.mp4?token=PfiRSN6b9ScB1AXjxEzvt_EJOo_PkvpkomDGnfuol4u1NF2MrKVI774oI9Or5aMnjeTZw8V7QNrsykPsL-Lsk0qQ9l_yH2W__oZeNmKG__hzCyL7U1ipa70rAjMpTddQfBah-6gZS5EDguc-5CljuOOMbj98bjbkQtit_7FVJQiYVJ02BZwnI2LN0mYZ3vmovggM10WZcCcYieohvpoLk9_lGAHP8u_IV3ifcD8qIyX75LFVm939EXj8-aLQTaErTQReCX9Yhf8DoBAAAMxMUoiSZCs47Zns8tiDDBkAN1OjxvJUhxxxUL8Jru9hlXZ2o8-kedTmMZ17LXb9FWcQgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع یمنی: عربستان همزمان با نزدیک‌شدن هواپیمای ایرانی، به فرودگاه صنعا حمله کرد.  @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/449627" target="_blank">📅 14:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449626">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
منابع یمنی: عربستان همزمان با نزدیک‌شدن هواپیمای ایرانی، به فرودگاه صنعا حمله کرد.  @Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/449626" target="_blank">📅 14:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449625">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTuqHy2HdvaQftgkjZCXgNRvZL2valYmMkyGSpMwKkhyJt-KR4_bjSWsfpuOAdaNz4iNjFSEBX1WW0it5kFarlqZkrsdRbtYoz14QjjM7l_Ha8kpH09ZG3amT8FRCLX4WKPvwHY6DLyzmR-Ia7ETyW0hVW5NHChhWst-UMgms3fu9UO1ve_P1GJRsadf-ygqBrlM3mNNJcRkUHa7prJdcSFLkEhaf3i6pNO4nqzH5a2-Csh-1Blrms6RVEtIxrKAU0s13pwVyV49V99xXyqPcKuAqF7CNqXPs_E6OtU0ovxw-xmsVgaJoVYODCBQ1npVCwIQI-ksZQN_gXTtyGcDhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع یمنی: عربستان همزمان با نزدیک‌شدن هواپیمای ایرانی، به فرودگاه صنعا حمله کرد.
@Farsna</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/449625" target="_blank">📅 14:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449624">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAr6fCouK4pdj1r987smWXfPBOAVSsRjgXQD5Q4g_HjsqVa__9MvJ_O9pyPHJd5IcK6I3j1L-lYG8psMzZ979fchPtkM1TxO-5TIRCc1p2m4TmOl-cfUZjRmEtIRCLZzPY1AF72rZmrvtIZN1dy9wxjT0j8FwljV0pYdoiyKz8Ke_sZ8vAESY27xHV53KqgWG2scm_r7RbaI0Ckb3JdkEq5SWm67qIvwZ9yWAkfEwMi1c_1lWkwscKBjJLhDddQa2H9Azw82UIUxc_7u5Z5ttrFfqR9UfmlkPzM3gnh_f3DhhYXDKhG13EMRG_pEP9kmkmNeW2b3597vxw_7aTOCCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
قرارداد علی علیپور با پرسپولیس یک فصل دیگر تمدید شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/449624" target="_blank">📅 14:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449623">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d57059b301.mp4?token=k9G_sw4m_NToO34n-DBeg58djNv39yxjVHpPKhIPxAMV-Bim96NVlrowv_1F3IFnxih-CMZrYDEKmby7tmVCC6zT6IELgGpyeX9OsSIdfwmRyGfUSl4fnnpX2NIOslRRz8KjlLhG-r90YOwlW40NUKvVuh3ZKoVH6Viz2xJ6U9vsSS0nkY6KLukHpZhM44T9YmUaVw7rYPnKGrtJPINHTD7Gw8eZwnZ3bV-YtDpVsmUFoCcErbn6U5ebdnAKoKPP1MB9Fo-h4fZUkiqBeop-EtbIwptVJeEDswkFQK7672heRh0Ta9hANwrUv83aar3mVLSogVWm0saqSq1WMfnLeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d57059b301.mp4?token=k9G_sw4m_NToO34n-DBeg58djNv39yxjVHpPKhIPxAMV-Bim96NVlrowv_1F3IFnxih-CMZrYDEKmby7tmVCC6zT6IELgGpyeX9OsSIdfwmRyGfUSl4fnnpX2NIOslRRz8KjlLhG-r90YOwlW40NUKvVuh3ZKoVH6Viz2xJ6U9vsSS0nkY6KLukHpZhM44T9YmUaVw7rYPnKGrtJPINHTD7Gw8eZwnZ3bV-YtDpVsmUFoCcErbn6U5ebdnAKoKPP1MB9Fo-h4fZUkiqBeop-EtbIwptVJeEDswkFQK7672heRh0Ta9hANwrUv83aar3mVLSogVWm0saqSq1WMfnLeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تداوم حملات گستردهٔ اوکراین به نفتکش‌های روسیه در دریای آزوف
🔹
فرمانده نیروهای پهپادی اوکراین، دیشب ۱۵ شناور روسی از جمله ۷ نفتکش را در دریای آزوف هدف قرار دادیم که تعداد شناورهای منهدم‌شدهٔ روس در ۸ روز گذشته را به ۱۰۵ رساند.
🔸
طبق گزارش‌ها اوکراین در هفته‌های گذشته دست‌کم ۴۰ نفتکش روسی را در دریای آزوف هدف قرار داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/449623" target="_blank">📅 14:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449622">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اصابت پرتابه‌های دشمن آمریکایی به ۳ نقطه در آبادان
🔹
معاون استانداری خوزستان: ساعت ۱۳:۴۵ امروز دوشنبه ۲۲ تیرماه، ۳ نقطه در شهرستان آبادان هدف اصابت پرتابه‌های دشمن آمریکایی قرار گرفت.
🔹
تاکنون ۲ نفر در این حمله به شهادت رسیده‌اند و ۳ نفر نیز مجروح شده‌اند.
🔹
ارزیابی‌های اولیه همچنان درحال انجام است و جزئیات و گزارش‌های تکمیلی متعاقباً اعلام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/449622" target="_blank">📅 14:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449621">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f53e24f4a.mp4?token=eJ5eEQ9HjA1ZJoU2ysCSBNiEIdg_Wazpugp_oytFwY7S4I2Jl8alZycbbLxTdGi6E6MK484q_1ebSk-r-qwM4P8Sei4XeJJ0yOVcfbGPH0xzu_0fu8JKjS3rD7d7tL6YrpnR1A38riRVVrdDsNPbmxrwCjhVU6eEgEd4HXBaZq6gbDX-zJgur7goIn6F5hfV5pMsKJY4y8LVrsxG_yjTYdWeuuS1d6ideoMMt1pDU1sx92CWDeGfPYv_hDbMcn_ztxy3It7_07_Jz29Pl1LhXn7Afz5IHtnZ7Y2MMOp1FtJ31fczNvh2VmjFQqjT6fONWEHrgXwXwRtzUR6Qg3SJNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f53e24f4a.mp4?token=eJ5eEQ9HjA1ZJoU2ysCSBNiEIdg_Wazpugp_oytFwY7S4I2Jl8alZycbbLxTdGi6E6MK484q_1ebSk-r-qwM4P8Sei4XeJJ0yOVcfbGPH0xzu_0fu8JKjS3rD7d7tL6YrpnR1A38riRVVrdDsNPbmxrwCjhVU6eEgEd4HXBaZq6gbDX-zJgur7goIn6F5hfV5pMsKJY4y8LVrsxG_yjTYdWeuuS1d6ideoMMt1pDU1sx92CWDeGfPYv_hDbMcn_ztxy3It7_07_Jz29Pl1LhXn7Afz5IHtnZ7Y2MMOp1FtJ31fczNvh2VmjFQqjT6fONWEHrgXwXwRtzUR6Qg3SJNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تنگۀ هرمز در پی نقض یادداشت تفاهم توسط ارتش آمریکا، همچنان بسته است
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/449621" target="_blank">📅 14:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449620">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ثبت‌نام زائران اربعین از مرز نیم‌میلیون نفر گذشت
🔹
معاون سازمان حج و زیارت : در کمتر از ۲ هفته از آغاز نام‌نویسی، تاکنون بیش از ۵۰۰ هزار نفر در سامانهٔ سماح نام‌نویسی کرده‌اند.
🔸
استان‌های تهران، خوزستان و خراسان رضوی بیشترین تعداد متقاضیان را به خود اختصاص…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/449620" target="_blank">📅 14:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449619">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/548ef102bd.mp4?token=vtg8JoZFUnDYfQ3LbcR1mtp27PgrckOXPOsj4uRB8yLHX7JF32Iv05D7TDFw6vTFogaa4Gxhy9_Tdxqx5OgIFf2aUpCAuoGb_pZZnhSFyW3KMtoX-1_YRfieRHPu73lwbGC9ztI8Xi6ZlIZRA0vc_K_zurIjypLTidhzUEfisGYBh0S-05QVcl24uFlfDsimB67uGdd_eP4e9BhBwmTeQHMoe_WvCdZwDFTkivkqwZiviD31Mg0a2il3Dx9FJvplQKPFh-xtXR__9Dkp4aEqkd_lt3hXt5pGLcx8gLbiiWMadTzfiHZz1gzv9i3ymKyHXeoVQt3wqmcHNIGd4y7cfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/548ef102bd.mp4?token=vtg8JoZFUnDYfQ3LbcR1mtp27PgrckOXPOsj4uRB8yLHX7JF32Iv05D7TDFw6vTFogaa4Gxhy9_Tdxqx5OgIFf2aUpCAuoGb_pZZnhSFyW3KMtoX-1_YRfieRHPu73lwbGC9ztI8Xi6ZlIZRA0vc_K_zurIjypLTidhzUEfisGYBh0S-05QVcl24uFlfDsimB67uGdd_eP4e9BhBwmTeQHMoe_WvCdZwDFTkivkqwZiviD31Mg0a2il3Dx9FJvplQKPFh-xtXR__9Dkp4aEqkd_lt3hXt5pGLcx8gLbiiWMadTzfiHZz1gzv9i3ymKyHXeoVQt3wqmcHNIGd4y7cfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از شلیک موشک های قدر، عماد، خیبرشکن و ذوالفقار در پاسخ به تجاوز ارتش تروریستی و کودک‌کش آمریکا در صبح امروز  @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/449619" target="_blank">📅 14:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449618">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آخرین گمانه‌زنی‌ها برای نامزدی ریاست کمیسیون‌های تخصصی مجلس
🔹
پس از برگزاری انتخابات هیئت‌رئیسۀ مجلس در اجلاسیه سوم، کمیسیون‌های تخصصی مجلس نیز خود را برای برگزاری انتخابات هیئت‌رئیسه و آغاز سال جدید کاری آماده می‌کنند.
🔹
انتخابات فردا به‌صورت الکترونیکی در ۲ نوبت صبح و عصر برگزار خواهد شد.
🔹
براساس شنیده‌ها اسامی کاندیداها به شرح زیر است که تا ظهر امروز ثبت‌نام قطعی کردند،‌ احتمال تغییر اسامی وجود دارد.
🔹
۱. آموزش: عبدالوحید فیاضی و علیرضا منادی
🔸
۲. امور داخلی کشورر: محمدصالح جوکار
🔹
۳. اقتصادی: شمس‌الدین حسینی
🔸
۴. صنایع: رضا علیزاده، مصطفی طاهری و ابوالقاسم جراره
🔹
۵. انرژی: موسی احمدی، مصطفی نخعی، مالک شریعتی و جواد سعدون‌زاده
🔸
۶. کشاورزی: احد آزادی‌خواه و محمدجواد عسکری
🔹
۷. اجتماعی: علی بابایی کارنامی، رحمت الله نوروزی،  سید حمیدرضا کاظمی، مجید نصیر‌پور  و ولی داداشی
🔸
۸. بهداشت: حسینعلی شهریاری
🔹
۹. عمران: محمد رضا رضایی‌کوچی
🔸
۱۰. امنیت: ابراهیم عزیزی و علا‌ءالدین بروجردی
🔹
۱۱. فرهنگی: مرتضی آقا تهرانی
🔸
۱۲. برنامه و بودجه: غلامرضا تاجگردون و ابراهیم عزیزی
🔹
انتخاب کمیسیون‌های قضایی و حقوقی و اصل ۹۰ به‌علت پایان نیافتن دورۀ یک‌ساله این هفته برگزار نخواهند کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/449618" target="_blank">📅 14:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449617">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f9c09015d.mp4?token=qLylYNuZXJDnnZtR-73Om8m60w_Y3zZTMBWci1eK6JaYP1iIefk78lp6RTV5TIA_0JRd3CFgWC2VkIHBTcSyQBkN7C2Ld9HL5mvY6z_6UpkjU3m6ImzZH0rJK_TL5o0LvL2ZkRaaeGlga2m1Ql-W2v8K3nXlWcd473MCddAwSHvsgmcT4HeMgwIeNQ0vcalHz7Cr-X_8ZUwFe3YFsggwU72-g_YQYIzts_SCoFecbI5BV0D4juyStGy9hXsR9u7oEJ6ZFsYzopG6A7vxPYBfgSopklh--3yTx3EfEueD92E0w2gTRCn_3M_0Ra6w94XsBZc_T1Fbh-erzMVaUjaUjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f9c09015d.mp4?token=qLylYNuZXJDnnZtR-73Om8m60w_Y3zZTMBWci1eK6JaYP1iIefk78lp6RTV5TIA_0JRd3CFgWC2VkIHBTcSyQBkN7C2Ld9HL5mvY6z_6UpkjU3m6ImzZH0rJK_TL5o0LvL2ZkRaaeGlga2m1Ql-W2v8K3nXlWcd473MCddAwSHvsgmcT4HeMgwIeNQ0vcalHz7Cr-X_8ZUwFe3YFsggwU72-g_YQYIzts_SCoFecbI5BV0D4juyStGy9hXsR9u7oEJ6ZFsYzopG6A7vxPYBfgSopklh--3yTx3EfEueD92E0w2gTRCn_3M_0Ra6w94XsBZc_T1Fbh-erzMVaUjaUjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: اگر کسی در نهادها مردم را لَنگ بگذارد، قابل بخشش نیست
🔹
باید زمینه‌های این عمل را از بین ببریم و آن را خنثی کنیم تا این خطاها تکرار نشود. @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/449617" target="_blank">📅 14:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449616">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98348a8a72.mp4?token=tS_6t9ZzGcO8-vBzdss4w3yivp2lAkkBNSPaIfHnbgYo8Ke9OjyybTpuLI7mZsablXP9Z6-52pDpTHE6pEJYlEqiTYiTQC9tjZgNw4DS43FD7nJawgps1xLEc9THktlYHrl64PnnWuYRsDCXjDHYhtKDKj2KKzC8LskzrqtGZR3kVB3E1IspVGPZcVnimqM4sQaCIQqKOh9iI2IXz6dgGsdGtfC1qoU8xF5ZcgQ_xgJv2eykTXwIBMFC3lFCjHz4JUd4_vEnGR44uBJONXcfU7hjm-sNjsSAB_e9h3ZBLVAZ3aZog8_NYxAdX4xWoEsm0XuDAW2L2NaGYTMDf1cH4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98348a8a72.mp4?token=tS_6t9ZzGcO8-vBzdss4w3yivp2lAkkBNSPaIfHnbgYo8Ke9OjyybTpuLI7mZsablXP9Z6-52pDpTHE6pEJYlEqiTYiTQC9tjZgNw4DS43FD7nJawgps1xLEc9THktlYHrl64PnnWuYRsDCXjDHYhtKDKj2KKzC8LskzrqtGZR3kVB3E1IspVGPZcVnimqM4sQaCIQqKOh9iI2IXz6dgGsdGtfC1qoU8xF5ZcgQ_xgJv2eykTXwIBMFC3lFCjHz4JUd4_vEnGR44uBJONXcfU7hjm-sNjsSAB_e9h3ZBLVAZ3aZog8_NYxAdX4xWoEsm0XuDAW2L2NaGYTMDf1cH4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: مجدداً از اعتماد رهبر انقلاب تشکر می‌کنم که بار مسئولیت دستگاه قضا را به بنده سپردند.  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/449616" target="_blank">📅 13:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449615">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34b88bf07.mp4?token=VYIkDEbj1zQpY_1ndWM5tKaWKx9wR16iah6SfpP8uN0dXRTxHpsfbzB10X5ENoO71035CD2x9iViulsBJFARrMT12LU_ZLubJAoMOPSs5NeYjS4wbm4ExN4uwmr8K9Sd9P0ONYGrT3-WR1hBVOaXId7qOdUGVU0isszdloKD_YJD-F8nOIoOzaWmPwXV96Nr952TouwEhrCHEHyUvPrWYoDBA2e77ZYtzCkU_spFQLwvMjYeXzCA73n9TmYYhmXORDBJCdIaElXV07wZhPVE_-W07-w4x8-7zHhYdwbJ5oOTcFscXFjHjCr219D7f49qq5vLh7DqMft6qspV4NlwWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34b88bf07.mp4?token=VYIkDEbj1zQpY_1ndWM5tKaWKx9wR16iah6SfpP8uN0dXRTxHpsfbzB10X5ENoO71035CD2x9iViulsBJFARrMT12LU_ZLubJAoMOPSs5NeYjS4wbm4ExN4uwmr8K9Sd9P0ONYGrT3-WR1hBVOaXId7qOdUGVU0isszdloKD_YJD-F8nOIoOzaWmPwXV96Nr952TouwEhrCHEHyUvPrWYoDBA2e77ZYtzCkU_spFQLwvMjYeXzCA73n9TmYYhmXORDBJCdIaElXV07wZhPVE_-W07-w4x8-7zHhYdwbJ5oOTcFscXFjHjCr219D7f49qq5vLh7DqMft6qspV4NlwWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از شلیک موشک های قدر، عماد، خیبرشکن و ذوالفقار در پاسخ به تجاوز ارتش تروریستی و کودک‌کش آمریکا در صبح امروز
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/449615" target="_blank">📅 13:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449614">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4a3b9d8ca.mp4?token=fcLzBcblWGviCYYqmIvTXpoULzR6Lqk-iGSz0bHJn6xmtn6F7X0QXmoUCZ9XiAruuYxh9C_wltDu7b3ff8AtWLdIHBTJXaZ4npVW-u4f_MnNgMFZZux1rGbvp47sitjGEPThn7HpMFTT_0HN7bVVnQTfDTQCxpencWgUauEL4T2innLGoME9mYZag9ZEv2gNMrAYGFbpUXut2MTkI2Kcrkpz6FiGP4Q3IIa9n5-xiJ-bgjyEfBqCFwWtlsWYGwV3yW0fh2p5I_z9Z0W41Q7Zt6gwZI5vEpitw4qCEghx60EEijsngv_OtdS-8jArRBduVhFAE7AC4gtOA7P8AjNrXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4a3b9d8ca.mp4?token=fcLzBcblWGviCYYqmIvTXpoULzR6Lqk-iGSz0bHJn6xmtn6F7X0QXmoUCZ9XiAruuYxh9C_wltDu7b3ff8AtWLdIHBTJXaZ4npVW-u4f_MnNgMFZZux1rGbvp47sitjGEPThn7HpMFTT_0HN7bVVnQTfDTQCxpencWgUauEL4T2innLGoME9mYZag9ZEv2gNMrAYGFbpUXut2MTkI2Kcrkpz6FiGP4Q3IIa9n5-xiJ-bgjyEfBqCFwWtlsWYGwV3yW0fh2p5I_z9Z0W41Q7Zt6gwZI5vEpitw4qCEghx60EEijsngv_OtdS-8jArRBduVhFAE7AC4gtOA7P8AjNrXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: مجدداً از اعتماد رهبر انقلاب تشکر می‌کنم که بار مسئولیت دستگاه قضا را به بنده سپردند.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/449614" target="_blank">📅 13:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449613">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">محکومیت ۱۲۰۰ میلیاردی سرشبکهٔ‌ اصلی قاچاق سوخت در میناب
🔹
رئیس‌کل دادگستری هرمزگان: حکم محکومیت افشین بادپروا، یکی از سرشبکه‌های اصلی قاچاق سوخت در بندر کلاهی میناب، صادر و به پرداخت بیش از ۱۲۰۰ میلیارد تومان جزای نقدی محکوم شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/449613" target="_blank">📅 13:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449612">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmbeyFfrOqhBjulM5_FRa-nVW0v-84Xxk7TFEpLodKjb0PTvqbX8pKbVZ-pSdkGkIu3DZoBeVQyojdA0PJHyECA0Y9zMN1blw2DWQBW_4JlqsM4VcbhAdpGBLIt1l1UGiTiJl_38qUdrLk3IxOU88Fxxq0RNKZ4WuUOuIpyRaUiLYUGI7Tamd6sGJFeY5NLWK9fYb4qUbkh4GkBGUJUIrjhhJSI7iZE8z-ieeP5TKMvG2hX2rsSXHdzR_gQTXGHdN8kZ9qxFPBdt_RQI0a4S37Xsy9QrC0jQdm92-YdJwv6jicfC2OTUuyXrQumMIspMSiYEKdaY_gU_39CYNO6U7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارز اربعین از بازار آزاد هم گران‌تر شد
🔹
در شرایطی که قیمت دینار در بازار آزاد تا ۱۱۰ هزار تومان کاهش یافته، زائران امروز ارز ویژه اربعین را نزدیک به ۱۲۹ هزار تومان دریافت کردند.
🔹
کارشناس اقتصادی محمدرضا صدری می‌گوید که «کاهش فاصله نرخ ارزهای دولتی با بازار…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/449612" target="_blank">📅 13:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449610">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOIi4dm08tFujSqJZBBO3qckxxeS5nSai9IwAsy18OtbyDysWcF9-Omx7ERZYctQQcvKjhzZfdqBlAvnNbbKtYtsL51O3ZfwG6fp1YvRMhF0S1OXovdRRVqXuGgUoRqNB1MPGlnhMlwjJMn-1s8DbcWBTiDJUa3WytDZsD-oLp_84L2m0FM63ZEGVNmkOn0-zvUnar3EwdvBHx7NyrneL2Am7tUTX16M3MDQ9SOQZL7_1oj4Z2SWxML9gy6qxbbGPfc_yp1jivgSfNXIwMETe610m_rKG97VetIv4mnEul3ExKhVTjRB8g0gs_0IdgAmO5yrmIPi-MlImEQpqgoriQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
شاخهٔ نظامی حماس در دومین سالروز شهادت محمد ضیف، تصویری از او را منتشر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/449610" target="_blank">📅 13:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449609">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🎥
ماجرای جنگ ۲
🔹
روایت متفاوت جواد موگویی از تشییع رهبر شهید انقلاب در عراق
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/449609" target="_blank">📅 13:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449608">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNXxDpf8GpxiSTSIpkGC1KdVPe-qnSp1CgIB73AyIKyvhXYfuTvP6_A6iS7WYnX_Jx0KxgjYl0Sg0hRaEIx71CcOXlVrts0nAfo2S2qA_fWp58ri3XvFqxn-puxAcS3f6wtGAMW2-sMSgR8mxGIF6ib4p5xxaqqRpsrmRXx1ZpRn8GQdMBAnLZ0KCga4ofzn7aOEMAQYjQazCVduoLu5rqgOEQ0oINnLwwgI18KS6w2h0KG6-xDpCwbNLS4rhsvmSsXHhmbz-ouKrL8ofi1BnXXNmGRuyNAQ1fZTBypC-S0Agy44KeBLy0i6DxjKllEtZVaCQ3XVHyd6NrpOYGpMxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
«تکاپو» در کنار «نوآوری» موفقیت را رقم می‌زند
🔹️
مدیریت پویا بانک رفاه کارگران همیشه به دنبال بسترهای جدید مالی و نوآوری‌های این حوزه بوده که باعث شده نام این بانک همواره در فهرست رتبه‌داران موفق IMI۱۰۰ قرار گیرد.
🔹️
حدود ۲۵ بانک از بانک‌های دولتی و بانک‌هایی با سهامی عام فعالیت دارند. بانک رفاه کارگران که از سرمایه جامعه کارگری بیشتر تغذیه می‌شود و متعلق به این قشر از جامعه است یکی از بانک‌های موفق در کشور محسوب می‌شود.
🔹️
اسماعیل للـه‌گانی، مدیرعامل این بانک طی چند سال سکاندار آن بوده که با مدیریت مالی درست همواره نام این بانک را در فهرست رتبه‌داران موفق IMI۱۰۰ قرار داده است.
🔹️
مدیریت پویا بانک همیشه به دنبال بسترهای جدید مالی و نوآوری‌های این حوزه بوده از این‌رو، در شرایطی که بسیاری از بانک‌ها با شرایط ناترازی مالی دست‌وپنجه نرم می‌کنند از وضعیت مناسب‌تری برخوردار است.
🔗
متن کامل خبر...
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/449608" target="_blank">📅 12:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449607">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/449607" target="_blank">📅 12:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449606">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3fe5c2cf.mp4?token=jKPNp-ubQvKAi_7iolnpymnoXDJ5zXnWX2WZqtUCQjn0VAg37Mpp5k06uQlDmCiG2eG6LcPOKR6WXyKwsgnBFXVgukq1Byplk3K1e5iJVTZkEjPRDvgXj4d1ZpOkZ1E6CREvyxwEyjbPA4p4KNVvkXUCm54AjXqMxfCE_-3oaFj_ASDqUh_i5nf0rFYhrLYygKXrEl4FWFRGJINCCyMdYo-y4gsdGSE0DQH931J-bT8HHn6ULgE55hA8OF1UIWpX2jksAynBhysFWQnEVFDej28f9uwlZ_kSbTycCRhkIgbagPW7nWsNdCtjAW4fDKxIcpA8m1uQ5Q5-JYZm6OKF-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3fe5c2cf.mp4?token=jKPNp-ubQvKAi_7iolnpymnoXDJ5zXnWX2WZqtUCQjn0VAg37Mpp5k06uQlDmCiG2eG6LcPOKR6WXyKwsgnBFXVgukq1Byplk3K1e5iJVTZkEjPRDvgXj4d1ZpOkZ1E6CREvyxwEyjbPA4p4KNVvkXUCm54AjXqMxfCE_-3oaFj_ASDqUh_i5nf0rFYhrLYygKXrEl4FWFRGJINCCyMdYo-y4gsdGSE0DQH931J-bT8HHn6ULgE55hA8OF1UIWpX2jksAynBhysFWQnEVFDej28f9uwlZ_kSbTycCRhkIgbagPW7nWsNdCtjAW4fDKxIcpA8m1uQ5Q5-JYZm6OKF-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وداع کفش‌دار بیت با رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/449606" target="_blank">📅 12:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449605">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2jYc39VZk6WWY7mlcQB4o24_0feNygEo56v8uBbJKTVb1oMa3M9voTw8ORZEywuTr9Br4AGYm1J8a8XMKcmTzyKN7ep5NkdHfdvA6Q0HcXitqFNeN7Murj52rnvvOZ9WgsQCE9uwzk6qxEnSpdR6wt1PnNTQHTSf7mSMnrAY94vFEFHO0SkdK8rz1zEzDgf-mg_Rp1dnnuQbzcptLfaDWAV_1VNU38LgcRDviaEsnFVm6844yqysH-XVnw04BJcAMoBJd3wGXhReCSHRoqyayfYiDD2b-1F7RxyYem_VyAKpre4Lma-wj8bwQtQoA84aekoCMj0X869gwHJMs9K7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریزش بورس به زیر ۵ میلیون
🔹
شاخص کل بورس در پایان معاملات امروز با ریزش ۸۹ هزار واحدی به ۴ میلیون و ۹۶۷ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/449605" target="_blank">📅 12:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449604">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6309b3c7d3.mp4?token=e7zQgD56gE4OJ32O8wNUcN0u1xyZttH7avQLpSjrvdv6So9Hj3PLtfbT6RNo52peVP4K8KBch_l3JrBQ-9f1dqnkPrMyY4ysL0HSo5uNKMDlZ1dwmgPwovjnCHIEtj3eYB4N3XPwuTWX6EfOZ8gGts4PlgVSGGmCc82jMCBjOt9yXqiUxJ4OwG6Wphhjey5r_fj4usejtvGKu4a09uTmiXjB6atg9jqbhbU74T-4JUUL4_WMvqW98KnfDcXy4EeMHttfFBNQ3EngbMDbE1XEp8Uj3QoP2ptNY0tS2aKHMAop3o2gdxeq3CChNyIXZfxop1Ma9YdKDH5kqxk8Qhk28YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6309b3c7d3.mp4?token=e7zQgD56gE4OJ32O8wNUcN0u1xyZttH7avQLpSjrvdv6So9Hj3PLtfbT6RNo52peVP4K8KBch_l3JrBQ-9f1dqnkPrMyY4ysL0HSo5uNKMDlZ1dwmgPwovjnCHIEtj3eYB4N3XPwuTWX6EfOZ8gGts4PlgVSGGmCc82jMCBjOt9yXqiUxJ4OwG6Wphhjey5r_fj4usejtvGKu4a09uTmiXjB6atg9jqbhbU74T-4JUUL4_WMvqW98KnfDcXy4EeMHttfFBNQ3EngbMDbE1XEp8Uj3QoP2ptNY0tS2aKHMAop3o2gdxeq3CChNyIXZfxop1Ma9YdKDH5kqxk8Qhk28YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این جنگ فقط نظامی نیست!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/449604" target="_blank">📅 11:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449602">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uP6Fc7S_iLqErkRRyAFvSltnugBMeh9u1pK_2gOAna7AScZcv-EPbDonzb2NQ5lCwzJxN5wnumvOVbMYjOl9iAzgqOFAt6O9QUHbT3uvd6Pnn1fRohHPxzCo7JBWCBNXGDZJPxQbSJ1xkrBnMpJV2_tjG16PZuEeRsjb9UTMtHMSObtAl1wKctIirmUVkJd7nOKKbVaBfmn6CgnIBXDo_Bi4brrYKATumIMN8WIY57OGH4gouc6rNDsEUexW9NRK8UXpXwYWVni4q2ya1Aw8K7Krl8CN2obzC6KdA9KHkRCXs_J9QybL1rPmD3BXCLcPzxKZpnA82yXXqHWyESXevQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb56bd3632.mp4?token=bNJ17lfYjJ85hDv-dEkVNCURjkfDdfmfMxAzVdePDnJqz_knF0oDwkwnvkMeqlT5ht40h4ptTAMNrbl8jUQ8r7HWIvdQrgPSFY_opNB0a8YyJyXaCMv2kvTUZsx20kkAV2NRpCRBBhz-NRucGEbscZPnJo9b1N0rqSF1-e0YoQl92myINtbkfwa1FpgbYY3wQE3TFuOHe3jLx34AB927dOPKdXGufUc5f25FVBLBtOWRz8aE0E_GIQjkYIUs45ScOBRmOkBXwlMizpR3D-Ph8a1WzwNXZsyLT_H-V4pcrjM6QXGuRlUIXLG2pb6K30aEwE47D6GjOgytne_Mry3dCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb56bd3632.mp4?token=bNJ17lfYjJ85hDv-dEkVNCURjkfDdfmfMxAzVdePDnJqz_knF0oDwkwnvkMeqlT5ht40h4ptTAMNrbl8jUQ8r7HWIvdQrgPSFY_opNB0a8YyJyXaCMv2kvTUZsx20kkAV2NRpCRBBhz-NRucGEbscZPnJo9b1N0rqSF1-e0YoQl92myINtbkfwa1FpgbYY3wQE3TFuOHe3jLx34AB927dOPKdXGufUc5f25FVBLBtOWRz8aE0E_GIQjkYIUs45ScOBRmOkBXwlMizpR3D-Ph8a1WzwNXZsyLT_H-V4pcrjM6QXGuRlUIXLG2pb6K30aEwE47D6GjOgytne_Mry3dCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‎
🔴
سخنگوی نیروهای مسلح یمن: پروازهای میان فرودگاه‌های صنعا و تهران، برای شکستن محاصره و کاهش رنج مردم یمن، با وجود هرگونه پیامد، ادامه خواهد یافت. @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/449602" target="_blank">📅 11:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449601">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3914cfc6.mp4?token=XYklVmiwWsYRPRSb4SA9swHu5p8YXSYCLi0WBMbk3Lmvo-v_1tmsgXbev4mHem8bsuWEXcuO7EKSxx2vLuBSqo_jXF5nOKqYJfARuibKSwlGdq9hk_7cToxBqXBpn-rQXDwlFORiC1mFSgfIMYPLd0AFCK_xR-XnGGcQkUM_4atK-z6xNfTo9E60IS2LuRFNHbTFT4Ql_6Giygl79hpqpKgZvVlYdxrPwWksjdPIWyk_71bFBtDZ4xVN6XAmxmv5V2xzIcFPMK4c9cQFjpZ1J7V5ksULnD0zgSiwFkdcs_nVUzOLYnzpjOdUgSmYPA7s9Al2wzH2em9mlMqYHCEZ5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3914cfc6.mp4?token=XYklVmiwWsYRPRSb4SA9swHu5p8YXSYCLi0WBMbk3Lmvo-v_1tmsgXbev4mHem8bsuWEXcuO7EKSxx2vLuBSqo_jXF5nOKqYJfARuibKSwlGdq9hk_7cToxBqXBpn-rQXDwlFORiC1mFSgfIMYPLd0AFCK_xR-XnGGcQkUM_4atK-z6xNfTo9E60IS2LuRFNHbTFT4Ql_6Giygl79hpqpKgZvVlYdxrPwWksjdPIWyk_71bFBtDZ4xVN6XAmxmv5V2xzIcFPMK4c9cQFjpZ1J7V5ksULnD0zgSiwFkdcs_nVUzOLYnzpjOdUgSmYPA7s9Al2wzH2em9mlMqYHCEZ5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ما در فرایند دیپلماسی دست‌بسته نیستیم و استفاده‌هایمان را از این زمان کرده‌ایم و خواهیم کرد
🔹
می‌دانستیم که آمریکا پیمان‌شکن است و با علم به این موضوع و با چشمان باز از ابزار دیپلماسی استفاده کردیم.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/449601" target="_blank">📅 11:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449600">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWVXxFBoE9n0olAkADkrkaoXNyV8v-ZLWd5eqOXpi-9K0UfoClWrVY7ZOO6tFZlRyIgh4i_FbLBgWiImWNuSFYqB7jExjA9d-fpoX1o2DhSMkS_B4xQdJHnjd_SbWNPGBjLc9YOCNf95tVR5co8lVD97btUtTgfRnpKpvyuOzfxlKy28rmh9Fzepu97lKTJmfcQB0WqU_CARl8FYJsqsa9zmNHV7l4BdwUCxajDxZjkwnYLYNKPFnT6fJSzjZ49pOheaXALCJ-jarlFMEN1TTHuEFyFOKXv9OVsxK462que2xMMU6XdFmtjxK9ynYkWy3aRVDOeH0IyPP8taUWr1jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سم نیل، ستارهٔ پارک ژوراسیک، درگذشت
🔹
سم نیل، بازیگر سرشناس نیوزیلندی که با نقش‌آفرینی در فیلم‌های ماندگاری چون «پارک ژوراسیک»، «پیانو» و ده‌ها اثر سینمایی و تلویزیونی به یکی از چهره‌های محبوب هالیوود تبدیل شد، در ۷۸ سالگی درگذشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/449600" target="_blank">📅 11:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449599">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ابطال کارت مربیگری ۱۵۰۰ مربی کشتی توسط فدراسیون
🔹
فدراسیون کشتی کارت مربیگری ۱۵۰۰ نفر از مربیانی را که فاقد فعالیت در باشگاه بودند، ابطال کرد.
🔹
براساس سیاست‌های آموزشی فدراسیون کشتی، شرکت در دوره‌های دانش‌افزایی اندیشکدۀ فدراسیون برای تمامی مربیان الزامی است و عدم حضور در این دوره‌ها منجر به ابطال کارت مربیگری خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/449599" target="_blank">📅 11:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449598">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96903b5d85.mp4?token=qHCNJgEfDjHs2_y7wjN7fNTFJytlUsKtHLUPDsVQTh_NGQGSnqjE-IcQAMSOATu6ua_bIYcnUus_dD1JD9lfOh2eorKd4XoxDLULAkDYwg1nAKJ9Vhc-EPoN4EUT-LoxOFERJHsNdaGMOA20Db1X6bgyGaPjsTa06h9S8WSmOv-vT0B7Q0EvwqvVJNjxoM0ssC4YY_3Axey2urqOE-i_aLxJhHOYgXGPK6oJ6fTUpXCZPjXYvBkvGb-u06EGOyj84nHuJc-bKfTu1g00UrBtlpjljCc01Q9g3aE2m8d7IB3RNhGv9f6gA_TjZr2BT9AXq4KqJUOpMaZ5thVYodaTFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96903b5d85.mp4?token=qHCNJgEfDjHs2_y7wjN7fNTFJytlUsKtHLUPDsVQTh_NGQGSnqjE-IcQAMSOATu6ua_bIYcnUus_dD1JD9lfOh2eorKd4XoxDLULAkDYwg1nAKJ9Vhc-EPoN4EUT-LoxOFERJHsNdaGMOA20Db1X6bgyGaPjsTa06h9S8WSmOv-vT0B7Q0EvwqvVJNjxoM0ssC4YY_3Axey2urqOE-i_aLxJhHOYgXGPK6oJ6fTUpXCZPjXYvBkvGb-u06EGOyj84nHuJc-bKfTu1g00UrBtlpjljCc01Q9g3aE2m8d7IB3RNhGv9f6gA_TjZr2BT9AXq4KqJUOpMaZ5thVYodaTFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیر غیب به آئورت لیندسی گراهام خورد؛ پزشکی قانونی آمریکا علت اولیه مرگ را اعلام کرد
🔹
پزشکی قانونی واشنگتن اعلام کرد بررسی‌های اولیه نشان می‌دهد گراهام بر اثر پارگی آئورت ناشی از بیماری قلبی-عروقی جان خود را از دست داده است.
🔹
با این‌حال، علت نهایی مرگ پس…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/449598" target="_blank">📅 11:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449597">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41509a0129.mp4?token=E068RfD56HEoDVLp3V2MizuJb5x5FaUU2OCUE-szvCrfNHjOc-QrE6Syz9gekI30AbhiUiWKQPOQ659UwCGQeXLyZtQuUcTvPX9pm6XOT2Zri2lB0Hpob0rQoDEEOj5DfE_HWWQJGkjJG9nnrT596QnYHhVoM7AcDehgyM2AlEU-HGtMq6qAcQNdEnF9mWRaucd3oTbfRxz_eax3N8ESyTFVcstJWS89r48dpsDFHistHyhuBlngNsy6Ljot5jQy2ZNfMYcFKumOALNxVi0IkDcEO_TRUrF4ZieWMLsg7jtW4eRb2w0GcuPHKmqYMTEZ8rAUtDH4DSDInAYj9XmCgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41509a0129.mp4?token=E068RfD56HEoDVLp3V2MizuJb5x5FaUU2OCUE-szvCrfNHjOc-QrE6Syz9gekI30AbhiUiWKQPOQ659UwCGQeXLyZtQuUcTvPX9pm6XOT2Zri2lB0Hpob0rQoDEEOj5DfE_HWWQJGkjJG9nnrT596QnYHhVoM7AcDehgyM2AlEU-HGtMq6qAcQNdEnF9mWRaucd3oTbfRxz_eax3N8ESyTFVcstJWS89r48dpsDFHistHyhuBlngNsy6Ljot5jQy2ZNfMYcFKumOALNxVi0IkDcEO_TRUrF4ZieWMLsg7jtW4eRb2w0GcuPHKmqYMTEZ8rAUtDH4DSDInAYj9XmCgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کینگز، فعال رسانه‌ای آمریکایی: تشییع میلیونی رهبر ایران، تبلیغات غرب را در هم شکست
🔹
شرکت‌کنندگان در مراسم، وفاداری عمیق و احترام به رهبر را نه‌تنها در ایران، بلکه در سراسر جهان به‌نمایش گذاشتند.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/449597" target="_blank">📅 11:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449596">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a7c0e8dc3.mp4?token=Z8iynKJlQGF6Xz1eZhP__jHxBexW6cMRGuL-RTBFZBOhjtwHvL3tIdYwMBeveHqSw36V3CxID4N1QI2mxyjkH2EmkD52281NdXclYSg_f05yur7H6QEk0xyWhbq-rRsV6zDAQbSbrlMCJsJugNHxExYAW43RY0SJJ3VZxuTUI6_iET3Mj7Cg_3fM8magK3WPWz-aqaehGp0jNhRrul7RmaoDJEmzs6-lSH_cd9O1ATUSrnF6MJ-VE4b2MRJLFZUi0mNe2QE27kc4sUu8z0oDwWvMnqJFzeLCWx1WHf1078AyMzlW6Ypvq8B8OgZNx9ZP67u1CBZG-i44G0MCw7GMzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a7c0e8dc3.mp4?token=Z8iynKJlQGF6Xz1eZhP__jHxBexW6cMRGuL-RTBFZBOhjtwHvL3tIdYwMBeveHqSw36V3CxID4N1QI2mxyjkH2EmkD52281NdXclYSg_f05yur7H6QEk0xyWhbq-rRsV6zDAQbSbrlMCJsJugNHxExYAW43RY0SJJ3VZxuTUI6_iET3Mj7Cg_3fM8magK3WPWz-aqaehGp0jNhRrul7RmaoDJEmzs6-lSH_cd9O1ATUSrnF6MJ-VE4b2MRJLFZUi0mNe2QE27kc4sUu8z0oDwWvMnqJFzeLCWx1WHf1078AyMzlW6Ypvq8B8OgZNx9ZP67u1CBZG-i44G0MCw7GMzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: کشورهای منطقه از وضعیت ۴ ماه گذشته که به‌دلیل حضور آمریکا به چالش کشیده شده، درس بگیرند!
🔹
ادعاهای آمریکا دربارهٔ اسکورت کشتی‌های تجاری در تنگهٔ هرمز، نشان‌دهندهٔ اصرار آمریکا برای تداوم ناامنی در منطقه است.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/449596" target="_blank">📅 11:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449595">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4368a18b89.mp4?token=ALpuQbhpS-Q5n2tk8BWjUb6SQrwKGy9KnH6cDOKna3rQA5tYFyKTDd9MyhHjDWFeXcYmiv8QAaW003qi0VLQM3kB56BzNYgru46T2hn8PFj6xZKUApqMTB3ecBDVm9ILwTh07E4C0ALcERaileNnyjEg0w-rZ6Ed4aaSOYafIru1UQJa4ouzvko8mAI3HmJpctSNdW5RyHsUfNnE3MHcPf22DECLcEe4nGrbUUj07cDenFIAUeYnWy7kMeE-YQA_SPPo-3AKj_qq8ezaeIztShkGr8Fee6MQ7HOllvG-jXvsjiqOwb5M1a50NtbzkHEbY7KxkJgpNbmd3KoIMeO2iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4368a18b89.mp4?token=ALpuQbhpS-Q5n2tk8BWjUb6SQrwKGy9KnH6cDOKna3rQA5tYFyKTDd9MyhHjDWFeXcYmiv8QAaW003qi0VLQM3kB56BzNYgru46T2hn8PFj6xZKUApqMTB3ecBDVm9ILwTh07E4C0ALcERaileNnyjEg0w-rZ6Ed4aaSOYafIru1UQJa4ouzvko8mAI3HmJpctSNdW5RyHsUfNnE3MHcPf22DECLcEe4nGrbUUj07cDenFIAUeYnWy7kMeE-YQA_SPPo-3AKj_qq8ezaeIztShkGr8Fee6MQ7HOllvG-jXvsjiqOwb5M1a50NtbzkHEbY7KxkJgpNbmd3KoIMeO2iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: هیچکدام از پایگاه‌های آمریکا در هیچ کشوری از منطقه از بانک اهداف ما خارج نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/449595" target="_blank">📅 11:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449594">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be274bb6d.mp4?token=bPLICxDnDCEp9rbTlSGQMe78USI8IBu7XmUCZNQu6WAuE_2yQlRBF4oRsyOYHTREB6HXuhlFVS4OYxEtsaQ2NWd8eTN4XvMd6xUq10gqi8wcRAERY74ZN58v03AXHr4b_JHreo8qTcojSu4GZkmtN82Tqz2J8ox54Z5J7hXGaFxBY-5gMxpR__je0AFD6Zr4kcWKO_jhXQgWhzXRInMC4qzGw4XHqdGYLkBjfIKKB2DzLA__sWpaE8Qd4RWp23MlUPqcbCI2QoMIQ9hi-g2R2T18LCispUj8MlX_gdow_FqmR8HcQ9Oi58-ahrELGNibSEfkVY0oaV1rC5g7O-m9xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be274bb6d.mp4?token=bPLICxDnDCEp9rbTlSGQMe78USI8IBu7XmUCZNQu6WAuE_2yQlRBF4oRsyOYHTREB6HXuhlFVS4OYxEtsaQ2NWd8eTN4XvMd6xUq10gqi8wcRAERY74ZN58v03AXHr4b_JHreo8qTcojSu4GZkmtN82Tqz2J8ox54Z5J7hXGaFxBY-5gMxpR__je0AFD6Zr4kcWKO_jhXQgWhzXRInMC4qzGw4XHqdGYLkBjfIKKB2DzLA__sWpaE8Qd4RWp23MlUPqcbCI2QoMIQ9hi-g2R2T18LCispUj8MlX_gdow_FqmR8HcQ9Oi58-ahrELGNibSEfkVY0oaV1rC5g7O-m9xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مقایسهٔ ایران و رژیم صهیونیستی توسط وزیر خارجهٔ ترکیه حیرت‌آور است!
🔹
ترکیه باید توضیح بدهد که چطور به این مقایسهٔ عجیب و غریب رسیده؛ ترکیه باید از تکرار موضوعاتی که صرفاً سیاست‌های توسعه‌طلبانهٔ رژیم صهیونیستی را توجیه می‌کند، پرهیز کند.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/449594" target="_blank">📅 11:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449593">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ccc9d5d62.mp4?token=RHp68IKiOy7fQTzfpEtIqIoKpEF08w6DvDWNfK77vgMQ7ggJdBvR4VIFTKlCePuyJbfaQ98zDorEkitucnxAA9wFS_c6wAB3jbSH7Dova7jRf1CrUDzhd0StOCKnE-CQz3wNEj8zrdQcsdbIMQgUKTQQEfw6JT9ZwKc2WFhpY1gHcrXg7to7ITARuaXrgrdqIvfFZnXxWZnKl2JaufL7H5YJ8Lzppf-XE_17hBbtwNSCnmQsODYFTtruW0eOCukfoCY0Poz2MEb_bMEpHzXiNRSWY5XvqERsp2JUQk-5e2P_KW5eQS6mvTQYDHm1kFE5_4z66-lDerVB6N-L-0dkKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ccc9d5d62.mp4?token=RHp68IKiOy7fQTzfpEtIqIoKpEF08w6DvDWNfK77vgMQ7ggJdBvR4VIFTKlCePuyJbfaQ98zDorEkitucnxAA9wFS_c6wAB3jbSH7Dova7jRf1CrUDzhd0StOCKnE-CQz3wNEj8zrdQcsdbIMQgUKTQQEfw6JT9ZwKc2WFhpY1gHcrXg7to7ITARuaXrgrdqIvfFZnXxWZnKl2JaufL7H5YJ8Lzppf-XE_17hBbtwNSCnmQsODYFTtruW0eOCukfoCY0Poz2MEb_bMEpHzXiNRSWY5XvqERsp2JUQk-5e2P_KW5eQS6mvTQYDHm1kFE5_4z66-lDerVB6N-L-0dkKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: در متن تفاهم‌نامه به‌صراحت نوشته شده که ترتیبات بازگشایی تنگهٔ هرمز توسط ایران انجام شود
🔹
اساساً بند ۵ متن تفاهم‌نامه تفسیرپذیر نیست که آمریکایی‌ها بخواهند براساس تفسیر خودشان تصمیم بگیرند.
🔹
آمریکایی‌ها به‌جای اینکه اجازه بدهند ایران براساس تفاهم تنگه را بازگشایی کند، از روز اول تقلب کردند و با تحریک و همراهی کشورهای منطقه سعی کردند مسیر هماهنگ‌شده با ایران را دور بزنند.
🔹
آمریکا با این کار هم تفاهم‌نامه را نقض کرد، هم امنیت کشتیرانی را به‌خطر انداخت و هم باعث تشدید تنش و درگیری در منطقه شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/449593" target="_blank">📅 11:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449590">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r6ROIN8KhNLFMLcpoKyfNqbk1YskHbKRXG3FjyXetZhEQQGyQ802h5g8LkwvxM8TSuuwfvg3MxNEjxDrvbJhQV86PMPQ24ebCOYtLb-9w_G4HLGgJNNTXHFOwkwKQjE6Kt3NBAr7SwvsaUnkgPX326mZCC6xiVbv14gQF-LCM39Lq_ahicX7G1WBP5cAT5f7nW0NdtGMu6DK3FRSH4eEkx-pCjiA-7L9aVBkEWv1hxjXq3b4AkgME1sS7m3t7aoSBsyKdIvPWuBMwgQBHu7Irgg8FtZPjG0H2mISlNn5PuzqqE9egvYiYFYRPT0m4wdzxn3QMgxifE3z5Flbmf2tIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IwZ99EeYfAtJBOQHkcMYLE83EtbcLP9UtzgCBgelnWIEA6UEw0pDMFaJ4rHz-V7Pw4sgzOr0ENsXT86ALioagJGOeSYdMQxfar3IjsNmXiMkr4W2wxn2E8lpAwLiosUK_kOxq2s6kPlyOSNSSnxXIFepB_WxIatdG8VrrxJaLJtW_-_mKwwTobh9K1Xg8DQT-Z07gGGaBS7_Rc_7Y0MW56ZAZXGtZLWu8ue-YznN81hRlKSqwql2X8a6JB6KEN7rnCjLZZ4bYWbYKcznxFedQA5F_UJGoxDiSmOXtqRGjChtDCrEuYM7oDcKHNqkcbA3_jihlpr9VfT8Idw4EJNLuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TCQLquYJB_vv9i4rn89PgW4EeWXkZSPutZeeXeThzeKEWx3fbLZdw6fkIj-PYqDG14RBt_POFhWulk54FSomcs2goOrq5emBU0OKzu5JBwtqtBox365eM0Iea7ueG1gBva2gO8fDmq5Gee-iIhczO-LORTgdQRYrRRPBnhyhIQph9dZ7wjeFztZgvrioFBdz9tagl3w4ja3Tbnu6LPDWFp_6HqirML-ezNnUCQa3Mu_GT0oPN4bjBHI9U4ChCNiJtDui01822PkwxwzEfe6LOgLtfvEFe8pohY5gIhpMd2ksv7rxW3o72PJ23jkjILkmRC6DKGHNxgmZzPKYEzOzlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: دانشگاه باید به میدان حل مسئله وارد شود
🔹
رئیس‌جمهور در نشست‌ تخصصی با استادان دانشگاه: دانشگاه باید از محیط صرفاً آموزشی فاصله گرفته و به میدان حل مسئله وارد شود.
🔹
در این الگو، دانشجو نیز همزمان با آموزش، در میدان عمل تربیت می‌شود و با کسب تجربۀ واقعی، به مدیری توانمند، مسئله‌شناس و تصمیم‌ساز برای آیندۀ کشور تبدیل خواهد شد.
🔹
مسئولیت‌ها باید بر مبنای توانمندی، شایستگی و کارآمدی افراد واگذار شود، نه براساس ملاحظات جناحی، سیاسی یا روابط غیرحرفه‌ای.
🔹
اگر مدیری نتواند مصرف منابع و انرژی در مجموعه تحت مدیریت خود را به شکل مطلوب کنترل کند، باید در کارآمدی او تردید کرد.
🔹
نظام پرداخت باید مبتنی بر عملکرد، بهره‌وری و میزان ارزش‌آفرینی افراد باشد. تداوم رویه‌هایی که در آن میان افراد پرتلاش و کم‌کار تفاوتی وجود ندارد، با اصول مدیریت علمی و عدالت سازگار نیست و دانشگاه‌ها می‌توانند در طراحی و اصلاح این سازوکارها نقش مؤثری ایفا کنند.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/449590" target="_blank">📅 11:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449589">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4852a538d3.mp4?token=mOR5GvMGRe0rwCPokXvkAeZi50xXG2lgbLwYYh925x9STBXGfBhD3B7PnbS6XBkTqZOHkL9-Og4GazYtcIFNF0tBRDM2kWO_j97A9Y3iJ6YIzj6Afrr82M-T9-BVGsB0N9vqip2GODkWBG9_y4O_Ekb975ppS9d84Ci_7m-ssun387Vq1jHENu9KzAvryhS0TUuP-JX46wa1wkPrkUGsd02aHZNWKpCZsCGgsHYR5hclzq2yveh1V5jRr5Y0dB04VzHwjirKU4pjEPUVC5hUY_zJTHypZlyAhTrC3qOJ0aB4WGQkDPC7zrzpqAwrcAsB8K_4dMpq5xKTqDM-N5RZ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4852a538d3.mp4?token=mOR5GvMGRe0rwCPokXvkAeZi50xXG2lgbLwYYh925x9STBXGfBhD3B7PnbS6XBkTqZOHkL9-Og4GazYtcIFNF0tBRDM2kWO_j97A9Y3iJ6YIzj6Afrr82M-T9-BVGsB0N9vqip2GODkWBG9_y4O_Ekb975ppS9d84Ci_7m-ssun387Vq1jHENu9KzAvryhS0TUuP-JX46wa1wkPrkUGsd02aHZNWKpCZsCGgsHYR5hclzq2yveh1V5jRr5Y0dB04VzHwjirKU4pjEPUVC5hUY_zJTHypZlyAhTrC3qOJ0aB4WGQkDPC7zrzpqAwrcAsB8K_4dMpq5xKTqDM-N5RZ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ما در مسقط صرفاً دربارهٔ تنگهٔ هرمز با عمان مشورت کردیم و اصلاً قرار نبود موضوع دیگری مطرح شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/449589" target="_blank">📅 11:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449588">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8b85f616b.mp4?token=uI-peG2av-kuPWGwm_v8xTcvnyRRcNCs4-l6m4hlngJ2oC-_raGrLDdeD4xoD2yaaZz9xWr_VY4RTXPVBxCIIIrBCJ7F2hKPm3WYoUc_HdXlr-LdHdUiYLau0IkZgGhINClrF8qpS2uQ_taaGdmRfOq5wgFhrPzrW4B45wBnLve7BXIxkdNsE9qEvJzUI4I0pPqVkbofoKg2eGiQIERt6z62_rquoXaPLPi5UTgo78T5xLAFtcCEzwnVxbBzqvqHuEbAa9zgnJL4W1pFjJtBS15iVcF-o4L6c1vz1EEM3KCdHZg1eJy9efronhj51sOInfswzPTiJ7AkDhXWLYukcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8b85f616b.mp4?token=uI-peG2av-kuPWGwm_v8xTcvnyRRcNCs4-l6m4hlngJ2oC-_raGrLDdeD4xoD2yaaZz9xWr_VY4RTXPVBxCIIIrBCJ7F2hKPm3WYoUc_HdXlr-LdHdUiYLau0IkZgGhINClrF8qpS2uQ_taaGdmRfOq5wgFhrPzrW4B45wBnLve7BXIxkdNsE9qEvJzUI4I0pPqVkbofoKg2eGiQIERt6z62_rquoXaPLPi5UTgo78T5xLAFtcCEzwnVxbBzqvqHuEbAa9zgnJL4W1pFjJtBS15iVcF-o4L6c1vz1EEM3KCdHZg1eJy9efronhj51sOInfswzPTiJ7AkDhXWLYukcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: بی‌تردید تفاهم‌نامه وارد مرحلهٔ بحران شده
🔹
آمریکایی‌ها در پیمان‌شکنی این‌قدر کم‌صبر بودند که حتی اجازه ندادند بازهٔ یک‌ماههٔ تعهدات ایران دربارهٔ تنگهٔ هرمز تمام شود.
🔹
تا زمانی که طرف مقابل تعهداتش را نقض کند، ما هم به تفاهم‌نامه عمل نمی‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/449588" target="_blank">📅 10:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449587">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVupuGUzmKaEFaYjAdAJQpYPAMrWmn5-ibElWwsSpMkydIWULkEgL9xTIMGEqxejm72runMMrpSnLydRVXYtw5EFFTcUChS0G6UPaYk50_48CROKyLjbftjlrGtJa89u41wzQXoZvuRbxe7PqQJamW0_rtgR1K36Dq8B99I6KTl5WNB3chJPMfUavFEf9RPnToKPF87Z2jRyUgGTvH7_Sp7IIfU-nTwfp_yA5oGKB5aAThpYGgbFV5NJGa-WhmPoujfAlBri942r1OQ-KclilLniy9Ubo4ytRWQoQnrGJYeNE0X01UyIQlbZQfIN3TlQuoaxJAvTVkVijO1YSeEcqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قفل صادرات پتروشیمی شکست
🔹
گمرک ایران با ابلاغ دستورالعملی، ممنوعیت صادرات محصولات شیمیایی، پلیمری و پتروشیمی را که در شرایط اضطراری اعمال شده بود، لغو کرد؛ البته ضوابط صادرات «پیه صنعتی» و «اسید سولفونیک» همچنان پابرجاست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/449587" target="_blank">📅 10:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449586">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKUakKp4KQ6cxPaU5cwIMb0YQvMTItvYbRyDwVVtEjCcKHjF_8MUwZR6vL8ZR4_crO91Tgy95g6x5U0Kh0expMb7oB7mmoCv8GMyF_gdKKQa3p-lRIHO7FmCmzFoFDVJbuUzSIR86ouGbWP6etQsTyNEuM9KXjvtuex-4hrUyFl8KzFUyK9L2nIJ5ptMYl55LrwgKm7GeZH4OdcwXx_E81vhHohSHiiuD-e27I1ootbkwRlGQcWrW2dbAdvNZ33axC7g0vvRw1Ykipc7BhthXCnI635ud4aAa_57ZVA-olnW69b7labMWnR5L-LpeEVnAvEXl1Tc8qOxvV0-QMRTbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تروئیکای اروپا باز هم طلبکار ایران شد
🔹
به‌رغم نقض مکرر تعهدات آمریکا در تفاهم‌نامهٔ اسلام‌آباد، وزرای خارجهٔ انگلیس، فرانسه و آلمان با انتشار بیانیهٔ مشترک حملات ایران در تنگهٔ هرمز را محکوم کردند.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/449586" target="_blank">📅 10:31 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449585">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ac61f4295.mp4?token=m4cQxbJGG-Yor1G0YwCfb1r5lKiciOdAoR6Kj7UtDUvsCNp-29u3_eTmAUnvReBwsoLvaHm71kYs98GxYpvPAj1W4qXlX-1hW-wovK_26BNni27qaN3FRDyppzoQjQP7eG-UHu3rjOYJQhCrLWfUpfwTv7J5TCDrX4LdlA2GiKgV1RuHdMcuAXd3IoP6yyTPwLFTnPUTorkgDhuiAuq_oB55tiAu2tvkQ7kvr9NxHs6PcpWIxXIJdozOnK_sygN5x3vZWn9fig56OBKCAKzaQmgOou_v0zmAh8Z-eHwwZ-qoN0Im7Sdjq5x0Z-iEcfKflIX9C_2tAStq0yYV7Qj9_Dwrck1L5FtcF6IhW1VIi-F4zgduq2wuLEbDxMcZLWwx-nMNRohLMzOhsq4INNeeT8rPRDGigypmtmv6bxxDzVXh8mJlA8XjERz3r38ZPWx8No3Bz9JP6h39ZZN2TVWXb85OLjkyrVI_GKaOEfkWqevCLI0_uFf-8xPDnxCExDjRhNYA75PvypkmNOq6BinYhH4ehvkOzsVcEBjJybMeQJB-aXqDxkd-9D1Um7OyIqs6Y8NzmQWT2ZEZBfg64oO2gqDSeNSRcznx1DHzFDYxdFn7ax8mos8tI4aUUWSx5Wo4TTSK33NWH5E7NPpQ4tnav48lMpWwAynNLLTMYgX_O2Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ac61f4295.mp4?token=m4cQxbJGG-Yor1G0YwCfb1r5lKiciOdAoR6Kj7UtDUvsCNp-29u3_eTmAUnvReBwsoLvaHm71kYs98GxYpvPAj1W4qXlX-1hW-wovK_26BNni27qaN3FRDyppzoQjQP7eG-UHu3rjOYJQhCrLWfUpfwTv7J5TCDrX4LdlA2GiKgV1RuHdMcuAXd3IoP6yyTPwLFTnPUTorkgDhuiAuq_oB55tiAu2tvkQ7kvr9NxHs6PcpWIxXIJdozOnK_sygN5x3vZWn9fig56OBKCAKzaQmgOou_v0zmAh8Z-eHwwZ-qoN0Im7Sdjq5x0Z-iEcfKflIX9C_2tAStq0yYV7Qj9_Dwrck1L5FtcF6IhW1VIi-F4zgduq2wuLEbDxMcZLWwx-nMNRohLMzOhsq4INNeeT8rPRDGigypmtmv6bxxDzVXh8mJlA8XjERz3r38ZPWx8No3Bz9JP6h39ZZN2TVWXb85OLjkyrVI_GKaOEfkWqevCLI0_uFf-8xPDnxCExDjRhNYA75PvypkmNOq6BinYhH4ehvkOzsVcEBjJybMeQJB-aXqDxkd-9D1Um7OyIqs6Y8NzmQWT2ZEZBfg64oO2gqDSeNSRcznx1DHzFDYxdFn7ax8mos8tI4aUUWSx5Wo4TTSK33NWH5E7NPpQ4tnav48lMpWwAynNLLTMYgX_O2Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش صداوسیما از
رونق مجدد کسب‌وکارهای آسیب‌دیده از جنگ
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/449585" target="_blank">📅 10:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449584">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ceD-0kIko5Ry-mUaOVT7tJO-10qk3n6i9g7noA3sYJxGgNTtIzhxssh7JlPsllzEmkYHWcS85s4sI9Od9Yx98v1ZjZf5xCveGUl4T3rDwtc5acZXl4EoD9PRYpvP9B66B5qV14kmKr_f7t_pxrLWDALFO47oicXv_elu5BbK4XxmhVIZ1gxw9FRFyUr2C55meOaBgZtJvAs0fkRelS5ZnENohXWbbwvppHU20CRlE5rrmQY3kI95A7P8MF162drX5zwuZJEZeRBFqNywYrbJ1vZRK2s-x9kJKa04WJD-F5koDPnF7yq8B4PqbkMn8dUV2TdYmvwLg6bVSBrlOZ6fxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/449584" target="_blank">📅 10:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449583">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/449583" target="_blank">📅 10:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449582">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJ8usd_KS7Sd64iE45WVoqyOAyyVilncMRl5qlyCfGe_OMaeOT-RJGpJeKdxwISiwrEy6GE-u_89Fx8Q3RWFgQJZ8c5zwRPgkEjUQuZcZUbWpIrcuYDcFCvpnQWaCb1ClBTa4MFdjKTyV4LVi30PKGoKuDj2yM4Hh9CmQ4ECr9AFmfnuw6e-HYe20u4_-NqLMHVOPU4zOuAjnhHhHE1GwCTyHYF1UDnnBPZ-a1r72uBX8vmRGvo9KSLT63MU2gAWq1DgSLTh8lToEkpRtNSntRSSia5djlNtMDyVygedd__VqtogMPAsgzb_i0IOJw7eBjQqVlp6pAf6bkhYFknyHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز توزیع کارت ورود به جلسهٔ آزمون کارشناسی ارشد از امروز
🔹
کارت ورود به جلسهٔ آزمون کارشناسی ارشد ناپیوسته ۱۴۰۵ از امروز در سایت سازمان سنجش منتشر می‌شود و داوطلبان باید پس از دریافت، اطلاعات ثبت‌نامی خود را بررسی و در صورت وجود مغایرت، در مهلت مقرر آن را اصلاح کنند.
عکس: رسول شجاعی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/449582" target="_blank">📅 10:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449581">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
نیروهای رژیم اشغالگر صهیونیستی، دست به انفجارهای شدیدی در شهرک‌های القنطره، حداثا و دیرسریان در جنوب لبنان زدند
.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/449581" target="_blank">📅 10:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449580">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/059fd71277.mp4?token=bWQliI1c1hJgmlK882gP3zYOv3t0qEbufKs_4LnYt4qQQs0PAEii8A09XaALXJHD5MhwYh-pczV0PprLm7Bdr9jYsVnrvFkwUqGwcueywa9EVRN6fTJYx4A97P9Hld43YAdX7E_cL1840yk1N3IPClz_X3o6G88UiuoNoPc6WwxqoXcS7tljfG9Bgi7nZo4zb8bMZ2s0OwrtMu3CuswRVG3hFyjeCZTMBP1FZ9uNUxGuGxQSvGyOAmdheAazghUfwejzSzXknv_vn_DEfW-9NNK1ACb_JeAmUCf5726j_xKMvRelPodyIF1i1OdQ8BiLsPcKMPsLGuAXd-cA3EYccw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/059fd71277.mp4?token=bWQliI1c1hJgmlK882gP3zYOv3t0qEbufKs_4LnYt4qQQs0PAEii8A09XaALXJHD5MhwYh-pczV0PprLm7Bdr9jYsVnrvFkwUqGwcueywa9EVRN6fTJYx4A97P9Hld43YAdX7E_cL1840yk1N3IPClz_X3o6G88UiuoNoPc6WwxqoXcS7tljfG9Bgi7nZo4zb8bMZ2s0OwrtMu3CuswRVG3hFyjeCZTMBP1FZ9uNUxGuGxQSvGyOAmdheAazghUfwejzSzXknv_vn_DEfW-9NNK1ACb_JeAmUCf5726j_xKMvRelPodyIF1i1OdQ8BiLsPcKMPsLGuAXd-cA3EYccw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیرانوند: آقای مهدوی‌کیا برای افتتاحیۀ جام جهانی به مکزیک می‌آید، عکسش را با رئیس فیفا می‌گیرد، پست می‌کند ولی حاضر نیست هتل بیاید و به ما سر بزند
⚽️
آقای مهدوی‌کیا از چی ترسیدی نیامدی؟ ترسیدی فحش بخوری!
⚽️
آقای مهدوی‌کیا بالابری، پایین بیای تو نماینده و فرزند کشوری به‌نام ایران هستی؟
⚽️
چرا نسل‌های قبلی فوتبال دوست ندارند این نسل تیم ملی به جایی برسد؟!
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/449580" target="_blank">📅 10:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449579">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFNpkEYiBH4P6-Cf1HQra_Za7AOmG_XXxoiTX2DFCC84xrkvA2RVNR6sLhX1OpXAM5cFVq4G56zbthKXgPcScnBBpIT1J4DVQGtWb7OpeO9HDh3xcFMd5_yScfe_huU8MguHH8fQx_Rr4gE0ZGMk_PKza-3R773wiIOnvdDWI9saCIJ5TUI9HTyvBwgBy3uB6Bz3BzFDmlD5QHIfUdy7SPrmkYqZKKHOb7iWLvZJoqkwLIKT_ZdeLIiVmGwe-ssgITsDUhvBUKN1Jk4CHZbfD6VdKMsAYUiwAZ6VM2vlZaZv5ONsTLK80fXyAD5tLC41Wk-xKdBtAImtjb_Ic2jV2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت مرز ایران-ترکیه را برای واردات خودرو باز کرد
🔹
براساس ابلاغیهٔ جدید گمرک ایران، گمرک بازرگان از ۲۷ تیر به‌عنوان گمرک مجاز برای ترخیص خودرو تعیین شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/449579" target="_blank">📅 09:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449578">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
استانداری اصفهان: انفجارهای کنترل‌شدهٔ مرتبط با مهمات عمل‌نکرده در جنگ رمضان در جنوب اصفهان، بهارستان و صفه تا بعدازظهر امروز انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/449578" target="_blank">📅 09:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449577">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86bdc0700.mp4?token=AObVxvjZQhxrXSHsmrvqwD-mPBK0YKmF0k3VgVe48ahUlF2_0W1o1pVWhmxqjAr1iJpkfjQK6JVrwzIFquWSaIHz-REN-H2pcXSYndAxG2egTHGyYJ6IFQgZvefAcOe-y1XZsL0umwFG8H9mLUysN2hYrJUthCVARQR9zf5uZFrUbNxXkrwUtH2nXZ-wObIO_LcUSATzv0SFvlzJDHrUY0xf0S5RBkbE2ffkRwbFHM-ev2ktLFn5BcTNcIq8SGf6heCy_92aPHl-NqQ3pLxxRcPbpIUEsaZAjLzZm6YPmpjbTCF0ztd0F8ZWB8mdbXunQiNo-C-XPLF_62G3UfLNV25joqFSLuDHYS2IDTd2ws8Rd1KwQM8uWLK21J-Ah9ZFJ0Ybb-4D5Vbq9RumuKjRkOVT-cZFMhM-3yKcD1bHVKT2veb32r9d7IrmykCLu5zzUM-j2YC7Dr12XzGJ5AqkAiOv0yV3IS6RwH6LdAA3HOqIoK9XXbgFMv2kkd7aF6gikqz85NT7MhTxwsdh9aFzUPCcU1P-Y9AlLzEmkwHjWH81hFWyH2jTAjGIQnIQtYtLK5CkzupYqgXbpyMcckDwm4Wj9px4KLQatIUBw8gf9nk-NkcC9lxFiAPNqmTdOT37UxCpJmpPnWNAxmUUiJ1yMJ9DOnAhYHhrIlL4Y67jgsU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86bdc0700.mp4?token=AObVxvjZQhxrXSHsmrvqwD-mPBK0YKmF0k3VgVe48ahUlF2_0W1o1pVWhmxqjAr1iJpkfjQK6JVrwzIFquWSaIHz-REN-H2pcXSYndAxG2egTHGyYJ6IFQgZvefAcOe-y1XZsL0umwFG8H9mLUysN2hYrJUthCVARQR9zf5uZFrUbNxXkrwUtH2nXZ-wObIO_LcUSATzv0SFvlzJDHrUY0xf0S5RBkbE2ffkRwbFHM-ev2ktLFn5BcTNcIq8SGf6heCy_92aPHl-NqQ3pLxxRcPbpIUEsaZAjLzZm6YPmpjbTCF0ztd0F8ZWB8mdbXunQiNo-C-XPLF_62G3UfLNV25joqFSLuDHYS2IDTd2ws8Rd1KwQM8uWLK21J-Ah9ZFJ0Ybb-4D5Vbq9RumuKjRkOVT-cZFMhM-3yKcD1bHVKT2veb32r9d7IrmykCLu5zzUM-j2YC7Dr12XzGJ5AqkAiOv0yV3IS6RwH6LdAA3HOqIoK9XXbgFMv2kkd7aF6gikqz85NT7MhTxwsdh9aFzUPCcU1P-Y9AlLzEmkwHjWH81hFWyH2jTAjGIQnIQtYtLK5CkzupYqgXbpyMcckDwm4Wj9px4KLQatIUBw8gf9nk-NkcC9lxFiAPNqmTdOT37UxCpJmpPnWNAxmUUiJ1yMJ9DOnAhYHhrIlL4Y67jgsU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرقت خودروی تاکسی در غرب تهران با یک بطری آب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/449577" target="_blank">📅 09:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449576">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تکذیب شایعهٔ‌ قطعی برق در اهواز
🔹
شرکت توزیع نیروی برق اهواز: هیچ‌گونه قطع برق ناشی از حملهٔ دشمن آمریکایی در این شهر رخ نداده و شبکهٔ برق در وضعیت پایدار قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/449576" target="_blank">📅 09:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449575">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
رسانه‌های خبری از فعال‌ شدن پدافند هوایی پاتریوت آمریکایی در کویت خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/449575" target="_blank">📅 09:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449574">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfbI5H5QudtGMtXNynRGyUg--27AFp7FqrbOhpmAJCcDYAiClutv3myEvH6c13rTnNQ4PGyIxlZPrXiVwWpx8EAU0DSO3-RBCkdr1Y5gReMMjmhImHhZZEy73MrIpzo9Vqf7As3cI1ek9qh6bmMH7bHMNbfqSw4sCNoU6LeLjRBUpD3Rt0hRalYoGJqqeuyvzpqpeg7PCUFmNnI9qPRsyjXa472IhGtBs3VMMBleNBczkmbid5abnrH1VKZbBtBOlJC3yZBAvywPgagcZMcYqNkNVVMNMNsHaz8wcrjXcDirHOIHu7lhr1AGOukdJBMa1rV_l2LKokRyeaI8-TwNyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشت‌پردهٔ تأخیر در اتصال کارت سوخت به کارت بانکی
🔹
کسب اطلاع خبرنگار فارس نشان می‌دهد مرحلهٔ آزمایشی اتصال کارت‌های سوخت به کارت‌های بانکی درحال انجام است و سوخت‌گیری با کارت بانکی به‌صورت محدود و ایزوله انجام می‌شود، اما زمان اجرای کامل طرح هنوز مشخص نیست.…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/449574" target="_blank">📅 09:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449573">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‌
🔴
سپاه: پایگاه موشک‌های زمین‌به‌زمین ارتش کودک‌کش آمریکا در کویت منهدم شد
🔹
در چهارمین مرحله از عملیات مقابله‌به‌مثل، رزمندگان نیروی زمینی قهرمان سپاه، پایگاه موشک‌های زمین‌به‌زمین ارتش کودک‌کش آمریکا در کویت را هدف قرار دادند و ۲ سکوی موشکی «های‌مارس» و…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/449573" target="_blank">📅 08:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449572">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311fad7a86.mp4?token=pPQ8T4npt13znQI4_MtX9dzexPW8P935wNlsC6Ekkwcw_3NB_9GpGdO4-IsmDP2U-9o1uX1-awY4apGzaTEUrEUWUbC1EPwFca1aPH9Z_J8abUyfORk_6llvZYQeojoxBtLfnI9Cg1xsLdB72N47R7GvqflkaTFaGCB88WqKrA9VMPC-SpWYGI_6a9XGsMof3k4usYO0Zz8__u1Y-5q6kXorPpD0UIqzPfRt1O6GGSHFuhXyfGBv0-zdayGQIRE3cV5fs5EeNfTINTWhftb59GIQA1rbfAOLK93x92v4HB712ivPRR68JTV_dMHpQ-KbAs_nRXFGGStg-qzxvNMtgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311fad7a86.mp4?token=pPQ8T4npt13znQI4_MtX9dzexPW8P935wNlsC6Ekkwcw_3NB_9GpGdO4-IsmDP2U-9o1uX1-awY4apGzaTEUrEUWUbC1EPwFca1aPH9Z_J8abUyfORk_6llvZYQeojoxBtLfnI9Cg1xsLdB72N47R7GvqflkaTFaGCB88WqKrA9VMPC-SpWYGI_6a9XGsMof3k4usYO0Zz8__u1Y-5q6kXorPpD0UIqzPfRt1O6GGSHFuhXyfGBv0-zdayGQIRE3cV5fs5EeNfTINTWhftb59GIQA1rbfAOLK93x92v4HB712ivPRR68JTV_dMHpQ-KbAs_nRXFGGStg-qzxvNMtgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افزایش دما در جنوب کشور تا ۵۰ درجه
🔹
هواشناسی: هوای گرم تا پایان هفته در کشور تداوم دارد. دما در ۴ روز آینده در مناطقی جنوبی کشور به ۵۰ درجه هم می‌رسد.
@Farna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/449572" target="_blank">📅 08:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449571">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2a16db93.mp4?token=r5itwvel90Ml7xxai_u2n547UaEzumnsYl5leY-E-_8Brj7gRNUNMxM7JfOWCvlKzLp9k-3VBcM_oIfDP2d67lvKIm02uB_w8upF2Ep8rwmyk9xNaTKvPuRRoU7YHX2XV4RY9zzveR1m1e8BwTPILGr8OW8uwGGdJpMUvpMoo0ddSDY0SMioMKJ6zz6brjMuV6UOeGFcVwLo-4lturHb-_R7webAFMBEMb56qPrjRLEvYod-PVNp4GgS2Ai-Ws2z24HFf5or-TVqNLSs8EirP7Tdrgn1uApIOiD0EZ_O8j58rLIZcDHizDY4KXQzUtAmKHP9QPLUStXV5uEVA7drbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2a16db93.mp4?token=r5itwvel90Ml7xxai_u2n547UaEzumnsYl5leY-E-_8Brj7gRNUNMxM7JfOWCvlKzLp9k-3VBcM_oIfDP2d67lvKIm02uB_w8upF2Ep8rwmyk9xNaTKvPuRRoU7YHX2XV4RY9zzveR1m1e8BwTPILGr8OW8uwGGdJpMUvpMoo0ddSDY0SMioMKJ6zz6brjMuV6UOeGFcVwLo-4lturHb-_R7webAFMBEMb56qPrjRLEvYod-PVNp4GgS2Ai-Ws2z24HFf5or-TVqNLSs8EirP7Tdrgn1uApIOiD0EZ_O8j58rLIZcDHizDY4KXQzUtAmKHP9QPLUStXV5uEVA7drbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز برداشت گندم در چهارمحال‌وبختیاری
🔹
پیش‌بینی می‌شود امسال برداشت گندم نسبت به پارسال  ۵۰ درصد افزایش داشته باشد.
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/449571" target="_blank">📅 08:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449570">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انهدام پهپاد متخاصم دشمن در بندرعباس
🔹
پدافند هوایی جنوب شرق ارتش یک پهپاد متخاصم دشمن را در شهرستان بندرعباس رهگیری کرده و منهدم کردند.
🔹
این هواگرد از نوع پهپاد انتحاری لوکاس بوده که مورد اصابت دقیق قرار گرفته و ساقط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/449570" target="_blank">📅 08:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449569">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11ab67d089.mp4?token=MFyZdbhxc75w8x631HAhVGzLLf-upGaXHxzcpGHjqmk03AA-WN-ZZfY7p7P_awI6rOmB2fEEIYRD2HjDLdIr39aEV0R94adQ00nqsEUQUlpLlv2SCAZkG2InCTUTdc-TqBgkhxp4esMwNpBwIANDdewjIrMM4PUgAXSEhDBwYTMuQTwLQw6LrG4lMcgUmud3a7ib8tDZv5iaRIsSEjUOeRcLa2iynFZ4p_OcQYHxDvUNYIIGqSO8U9MhyyD1U0vl4qdYfiNFvq-e1NQEilLPK3VH_o9g9av1y-Skdv6JNt7YJdSjbQ7eH415EvaG9zzVfdEnIP0dLrX92t7gBs9dKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11ab67d089.mp4?token=MFyZdbhxc75w8x631HAhVGzLLf-upGaXHxzcpGHjqmk03AA-WN-ZZfY7p7P_awI6rOmB2fEEIYRD2HjDLdIr39aEV0R94adQ00nqsEUQUlpLlv2SCAZkG2InCTUTdc-TqBgkhxp4esMwNpBwIANDdewjIrMM4PUgAXSEhDBwYTMuQTwLQw6LrG4lMcgUmud3a7ib8tDZv5iaRIsSEjUOeRcLa2iynFZ4p_OcQYHxDvUNYIIGqSO8U9MhyyD1U0vl4qdYfiNFvq-e1NQEilLPK3VH_o9g9av1y-Skdv6JNt7YJdSjbQ7eH415EvaG9zzVfdEnIP0dLrX92t7gBs9dKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در اجتماعات شبانه از نیروهای مسلح چه می‌خواهند؟
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/449569" target="_blank">📅 08:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449568">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
سپاه: مخازن سوخت، سامانه‌های پاتریوت و FPS به طور کامل منهدم شدند
🔹
به استحضار مردم شریف ایران می‌رسانیم، رزمندگان پرافتخار نیروی هوافضای سپاه، در سومین مرحله از عملیات مقابله به‌مثل و پاسخ به تجاوزات رژیم مستکبر و متجاوز آمریکا، مخازن سوخت و سامانۀ پدافند…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/449568" target="_blank">📅 07:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449567">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گرما فعلا ماندگار است
🔹
هواشناسی: از امروز دوشنبه تا چهارشنبه در اکثر نقاط کشور جوی آرام پیش‌بینی می‌شود و تا پایان هفته ماندگاری هوای گرم ادامه خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/449567" target="_blank">📅 07:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449566">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
رسانه‌های خبری از فعال‌ شدن پدافند هوایی پاتریوت آمریکایی در کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/449566" target="_blank">📅 07:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449565">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گزارش‌ها از حمله به یک شرکت تجاری آمریکا در بحرین
🔹
برخی منابع مدعی شدند که مقر یکی از شرکت‌های تجاری آمریکایی در بحرین مورد هدف موفق قرار گرفته و درحال سوختن در آتش است.  @Farsna</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farsna/449565" target="_blank">📅 07:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449563">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d296bb0b4e.mp4?token=kxIMbfc8u1y9PSQBjTMHNjET-OfaruHD4MvKuBNMB-WzOokLNcodgRsFflfWWDJyNXsa8jhxzF8oiPCcbIP3mVYiFIjAAUZX_iB44mzNlHRdGMXakzHop8M_Wd0iI-tE1nx0IwAKFySBBOZ3b4hqpDUx1pXiNdbJyCpq7pDFmoXsIbwLBT0d6Wzjf9OUXd1sFsIoT1mV2F2m5APtSZGLKCvkyP0BKqGmaivWN5GcJJ-5ck4WDe1Rjumi_T_EO6MfsxLD1qAFovDa53Qz_bkElWX8gUjelRfWI_BhCOVD13HNsUlheZE3IYua6ZpSd9FLiA9bqnSboK2dn-shUWuiUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d296bb0b4e.mp4?token=kxIMbfc8u1y9PSQBjTMHNjET-OfaruHD4MvKuBNMB-WzOokLNcodgRsFflfWWDJyNXsa8jhxzF8oiPCcbIP3mVYiFIjAAUZX_iB44mzNlHRdGMXakzHop8M_Wd0iI-tE1nx0IwAKFySBBOZ3b4hqpDUx1pXiNdbJyCpq7pDFmoXsIbwLBT0d6Wzjf9OUXd1sFsIoT1mV2F2m5APtSZGLKCvkyP0BKqGmaivWN5GcJJ-5ck4WDe1Rjumi_T_EO6MfsxLD1qAFovDa53Qz_bkElWX8gUjelRfWI_BhCOVD13HNsUlheZE3IYua6ZpSd9FLiA9bqnSboK2dn-shUWuiUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
ادامۀ حملات پهپادی ارتش به پایگاه‌های آمریکا در منطقه
🔹
در پاسخ به تکرار حملات غیرقانونی آمریکا علیه  کشورمان، ساعاتی قبل و در دور جدید حملات پهپادی ارتش جمهوری اسلامی ایران، محل استقرار نیروهای آمریکایی،سامانه های پدافندی و موشکی، جان پناه و سوله های…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/449563" target="_blank">📅 07:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449562">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae4fe3415.mp4?token=kGkhz2F7_p4cR9QEi0kNR-1WnbpqHKi0xuXfP1fNTMlxiF8iXxzKo2XsD79hofxDlM0pWu2MB4_hYNPPlnJCbdYcP1oGvdLHIGXHP8aXcbibndT_s-7ZYSszID0MnVlNoM4UHEjo_0ssEcjHiJJkwCvAGH8pHOVyqE1CIs1dQSXetPAXq-5OP2ta0FLapttjQyajr-iRwvBUOe7OweOwv3ZgKoZWxhmRpQIMvTcszzCXvNNAjBtqB5RKk8J78udEUQit7DntUNoV-nRIwkeAUzdzegonlZDy4cUsDcMhKpD0PKzjBVctjVQM5dL-GaPCPd1npT9fEzR7h2dNwjaQMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae4fe3415.mp4?token=kGkhz2F7_p4cR9QEi0kNR-1WnbpqHKi0xuXfP1fNTMlxiF8iXxzKo2XsD79hofxDlM0pWu2MB4_hYNPPlnJCbdYcP1oGvdLHIGXHP8aXcbibndT_s-7ZYSszID0MnVlNoM4UHEjo_0ssEcjHiJJkwCvAGH8pHOVyqE1CIs1dQSXetPAXq-5OP2ta0FLapttjQyajr-iRwvBUOe7OweOwv3ZgKoZWxhmRpQIMvTcszzCXvNNAjBtqB5RKk8J78udEUQit7DntUNoV-nRIwkeAUzdzegonlZDy4cUsDcMhKpD0PKzjBVctjVQM5dL-GaPCPd1npT9fEzR7h2dNwjaQMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کنایۀ خبرنگار آمریکایی به وداع با سناتور جنگ‌طلب فقط با یک گل!
🔹
یک خبرنگار آمریکایی در مقایسۀ مراسم باشکوه تشییع پیکر رهبر شهید انقلاب با مرگ سناتور جنگ‌طلب آمریکایی، با انتشار ویدیویی از خانۀ او نوشت: آمریکا ۳۵۰ میلیون نفر جمعیت دارد، اما تنها چیزی که نصیب این سناتور شد یک دسته گل کوچک مقابل خانه‌اش بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/449562" target="_blank">📅 07:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449561">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گزارش‌ها از حمله به یک شرکت تجاری آمریکا در بحرین
🔹
برخی منابع مدعی شدند که مقر یکی از شرکت‌های تجاری آمریکایی در بحرین مورد هدف موفق قرار گرفته و درحال سوختن در آتش است.
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/449561" target="_blank">📅 07:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449560">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYD5fe0tJtVqtqg-QlDVZ-fv5mSOosgQuJ0mBsjwvy0Y71VFaQHPsuuQRUZ4YnpBQfdZv2_l5aW3dRjjRcUThJLltPx7JcOVaQC8s3kE_sPCV2G7HMU4JUasWtgoglTVtWP6fEu34ctspW1z5lbItGsDtbpS7o0uBsuvvEEOR3aRKjKHU8ETrIFeN14n3SRvR_2OUmk1I56Bg-UMVBdMTQbr26096x4Mz9RsMa1q_eIzOXyYFkGwi7swwawjI9CkBhqnTWu1U-6-fU3ovc3ViCWSARns7vmKGKrFIVGcVJpB8L6ith-4xCvQ6YkSjOF7qI7ndalC4b4GtSNr6LcTug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد قربانیان زمین‌لرزه‌های ونزوئلا به ۴۴۹۰ نفر افزایش یافت
🔹
طبق اعلام رئیس‌ مجلس ملی ونزوئلا، تعداد قربانیان دو زمین‌لرزه ونزوئلا به ۴۴۹۰ نفر افزایش یافته است.
🔹
طبق گزارش خبرگزاری آناتولی، بر اساس آمار رسمی، بیش از ۱۶,۷۰۰ نفر مجروح شده‌اند و نزدیک به ۱۹,۶۰۰ نفر در اردوگاه‌های موقت اسکان داده شده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/449560" target="_blank">📅 06:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449559">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
سپاه: مخازن سوخت، سامانه‌های پاتریوت و FPS به طور کامل منهدم شدند
🔹
به استحضار مردم شریف ایران می‌رسانیم، رزمندگان پرافتخار نیروی هوافضای سپاه، در سومین مرحله از عملیات مقابله به‌مثل و پاسخ به تجاوزات رژیم مستکبر و متجاوز آمریکا، مخازن سوخت و سامانۀ پدافند…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/449559" target="_blank">📅 06:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449558">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
سپاه: مرکز فرماندهی و کنترل پهپادی ارتش آمریکا در بحرین درهم کوبیده شد
🔹
رژیم شرور و جنگ زیست آمریکا که از آغاز تاسیس تاکنون زمان‌های اندکی را بدون جنگ و شرارت نظامی سپری کرده و از شکست‌های اخیر در مواجهه با رزمندگان اسلام هم درس عبرت نگرفته و به تجاوزات…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/449558" target="_blank">📅 06:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449557">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
سپاه: مخازن سوخت، سامانه‌های پاتریوت و FPS به طور کامل منهدم شدند
🔹
به استحضار مردم شریف ایران می‌رسانیم، رزمندگان پرافتخار نیروی هوافضای سپاه، در سومین مرحله از عملیات مقابله به‌مثل و پاسخ به تجاوزات رژیم مستکبر و متجاوز آمریکا، مخازن سوخت و سامانۀ پدافند هوایی پاتریوت در پایگاه آمریکایی در علی السالم کویت و همچنین یک سامانۀ راداری راهبردی FPS در پایگاه احمد الجابر را به‌طور کامل منهدم کردند.
🔹
عملیات مقابله به‌مثل فرزندان غیور شما ادامه دارد.
🔸
تنگۀ هرمز سرزمین ماست و اجازه نخواهیم داد یک ارتش یاغی و کودک‌کش از آن سوی دنیا به دخالت‌های غیرقانونی خود در آن ادامه دهد.
@Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/449557" target="_blank">📅 06:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449556">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
سپاه: مرکز فرماندهی و کنترل پهپادی ارتش آمریکا در بحرین درهم کوبیده شد
🔹
رژیم شرور و جنگ زیست آمریکا که از آغاز تاسیس تاکنون زمان‌های اندکی را بدون جنگ و شرارت نظامی سپری کرده و از شکست‌های اخیر در مواجهه با رزمندگان اسلام هم درس عبرت نگرفته و به تجاوزات خود ادامه می‌دهد.
🔹
در پاسخ به این شرارت‌ها، رزمندگان هوافضای سپاه در مرحله دوم عملیات مقابله به مثل خود مراکز مهم تعمیرات و نگهداری بالگردی، آشیانه هواپیمای جنگ الکترونیک پی ۸ و مرکز فرماندهی و کنترل پهپادی ارتش کودککش آمریکا در پایگاه آمریکا در شیخ عیسی بحرین را در هم کوبیدند.
🔹
عملیات مقابله به مثل ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/449556" target="_blank">📅 06:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449555">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a490ee038.mp4?token=fQPjq4Ch_vHuT6WLhmKfJprpd4HAX-Agc5TI5igUac6VxgXrrhbej3m6bpvMjuVGXSQXmhTWbOE2GeZzgEJ1oZCSKELKLlbSiHsQOeqlEZqRWdiVjvfuFkDkCmXnhBO_bfa9fMlCvGm8Ju43kHbu0BHO_3I_HtDZeCpmd5nlrpKSJoLc7Duktu5d6fr-SPPaY9-PnTt_qgdOJD7SgXoXux8iDlYbxnP3QqB4Yz_Ph9lghD8r_ZP2iXLS3wQ-5p6rvrCzkMnWO8AVLwq3X1xixAYCMz3yFb7b6sgfRtqAwCPYYl0FzZiiYIXenhcCL6BZ-4bTW0dHD_zvgG5MBCelcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a490ee038.mp4?token=fQPjq4Ch_vHuT6WLhmKfJprpd4HAX-Agc5TI5igUac6VxgXrrhbej3m6bpvMjuVGXSQXmhTWbOE2GeZzgEJ1oZCSKELKLlbSiHsQOeqlEZqRWdiVjvfuFkDkCmXnhBO_bfa9fMlCvGm8Ju43kHbu0BHO_3I_HtDZeCpmd5nlrpKSJoLc7Duktu5d6fr-SPPaY9-PnTt_qgdOJD7SgXoXux8iDlYbxnP3QqB4Yz_Ph9lghD8r_ZP2iXLS3wQ-5p6rvrCzkMnWO8AVLwq3X1xixAYCMz3yFb7b6sgfRtqAwCPYYl0FzZiiYIXenhcCL6BZ-4bTW0dHD_zvgG5MBCelcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بلند شدن ستون دود از پایگاه آمریکا در بحرین  @Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/449555" target="_blank">📅 05:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449554">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
سپاه: مخازن سوخت و زاغه مهمات پایگاه هوایی پرنس حسن در اردن به آتش کشیده شد
🔹
شب گذشته به‌دنبال عملیات نیروی دریایی سپاه در متوقف کردن دو کشتی متخلف که با خاموش کردن سامانه‌ها و حرکت در مسیر غیرقانونی، کشتیرانی در تنگۀ هرمز را به مخاطره انداخته بودند، ارتش کودک‌کش آمریکا که خود محرک این حرکات غیرقانونی و خطرناک بود، بار دیگر با تجاوز به پایگاه‌های ساحلی نیروهای مسلح جمهوری اسلامی ایران خوی وحشی‌گری خود را آشکار ساخت.
🔹
رزمندگان غیرتمند اسلام در اولین مرحله از پاسخ به این تجاوزات، چندین زاغۀ بزرگ موشکی و مخازن سوخت پایگاه هوایی پرنس حسن در اردن را با شلیک موشک و پهپاد به آتش کشیدند.
🔹
عملیات مقابله به‌مثل رزمندگان ادامه دارد و نتایج آن در اطلاعیه‌های بعدی به استحضار شما خواهد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/449554" target="_blank">📅 05:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449553">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
منابع خبری از وقوع انفجار‌هایی در کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/449553" target="_blank">📅 05:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449552">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6ejX67NLin9Qwi14-ZhNCl3x4a0TJip7asxaVIwAfcZttPNv_c-FcABxfy0UE-zROQDcHGB1qNclkNmg84dsH205RafQvw_JzCCcXRhzSpCaR3vT9Rsa5UxJoH9YZHGJYg9IJPVKk4zdbwJojk5J9DG6E1GzqaRBOJCrKTIGN7ESubb3_LeblpwikR1F4JUq-pSRIMOV4pGrzPSxsZ0jI11UTVm77PTnLTihrFLhmK8mpca15vUcbJk4kksqgiOycS0n5kn9UTTQvloMKHwujNxpgvq3VJx7NBj_y9Yxno0gy1MJx2Kq-FNAmXxhzOgh0iICU0ujLYkD5FUP3SEoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلند شدن ستون دود از پایگاه آمریکا در بحرین
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/449552" target="_blank">📅 05:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449551">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
برخی منابع از حملۀ موشکی به بحرین و به صدا درآمدن آژیرهای هشدار خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/449551" target="_blank">📅 05:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-449549">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
برخی منابع از شنیده‌شدن صدای انفجار در اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farsna/449549" target="_blank">📅 04:38 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
