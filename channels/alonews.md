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
<img src="https://cdn4.telesco.pe/file/nDNjPIM_DSd-c2uXfSExS60To_frAVbQuVV2HSLR40zzAk3urnJ_EAs4DOzoT13WKpisFyySxKR7fftxlwIARt9ROiV4lMQdi0m-OoI4TU5qlHKv2Nr3sa31yo8FycJqBu72hIbLIJQd2FwDYtVp7T36zJ7yEMXjYipyTqVgur1js1Fex7MeCrxoUhtct1njsqfj-CdOzUgv-fo0OxYUnAECy_uLT5VHyln_05Z0j2386DsShkeZEkKCOAkRxNNrpmDGq0qT9VwWmhXoSzpSalYc5LNVy2QuHgsDEp2NBUHoIWZR7uDTh7gM4lKbCGx2Dfu2E1QFifliRiV3-p_LBA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 989K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-28 19:03:15</div>
<hr>

<div class="tg-post" id="msg-142655">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67623992c1.mp4?token=mlEDLBymK1DifwXS9Ezu2CHTlek6apJA0CcZzisJUP4sev7o8YejKwzjjdYVWbEe5YxgBI8DSRmx1w_DxpHD198IoAufpC4O8hsBF-VCC5zji6AKCorcra7gjsI4jVSLwowZPMvamC_VoMwqpZeJS3wnWfIUovs9A022DyKhkKWuoL8oAm0B_WjIEslvHqz5noH5KKPs3QXxnCInrWB6Nal8E03CuiFAmusbvNJWHRLpLlh30UxAt7bZTgXsbBqPQHOV9VxHWQqOwUY4UQoiX3fk4PkNnt_Xgn3vvL5z6JCwF0n3rHYHzeX53hzthk3rNgZu5L-bL8VlgJcUHakxBTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67623992c1.mp4?token=mlEDLBymK1DifwXS9Ezu2CHTlek6apJA0CcZzisJUP4sev7o8YejKwzjjdYVWbEe5YxgBI8DSRmx1w_DxpHD198IoAufpC4O8hsBF-VCC5zji6AKCorcra7gjsI4jVSLwowZPMvamC_VoMwqpZeJS3wnWfIUovs9A022DyKhkKWuoL8oAm0B_WjIEslvHqz5noH5KKPs3QXxnCInrWB6Nal8E03CuiFAmusbvNJWHRLpLlh30UxAt7bZTgXsbBqPQHOV9VxHWQqOwUY4UQoiX3fk4PkNnt_Xgn3vvL5z6JCwF0n3rHYHzeX53hzthk3rNgZu5L-bL8VlgJcUHakxBTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره پروژه سالن رقص: تصور نمی‌کنم دیوان عالی علیه ما رأی دهد
🔴
خبرنگاری از دونالد ترامپ پرسید: «اگر دیوان عالی علیه پروژه سالن رقص شما رأی دهد، چه خواهید کرد؟»
🔴
ترامپ پاسخ داد: «امیدواریم چنین اتفاقی نیفتد. نمی‌توانم تصور کنم که چنین اتفاقی رخ دهد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/alonews/142655" target="_blank">📅 19:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142654">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8ffe259f.mp4?token=SM4tF8B90v89RHORZEd1NiEhhrczZhBihAaIL4remQifloJ_W3cQyDX-T9Eu8fagQmP0omAgva_c76evXdZoj1jG4-b3GEMjgeh0MpC3aGddxae9oMbywbs8DCz9xMZ6shnPbQqSW_SuDSU_m2AAClsCcdHxc0BHDuHTso4sstxE01BebEjJgDXxXrnfCbBhKfuOftjjTqtig43CPigeFJZ1pESYTPhVWRfmzDbwVEyqsoz4o2gCxzEH2vwCCyR2Ty9YtlPpjLvp7b3ZROMk5d1cepM5G03l0zLIfG3V0W0BOchymNPnKfHDHEaKGyCscgTN-P10jyuG6zDRjIe2zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8ffe259f.mp4?token=SM4tF8B90v89RHORZEd1NiEhhrczZhBihAaIL4remQifloJ_W3cQyDX-T9Eu8fagQmP0omAgva_c76evXdZoj1jG4-b3GEMjgeh0MpC3aGddxae9oMbywbs8DCz9xMZ6shnPbQqSW_SuDSU_m2AAClsCcdHxc0BHDuHTso4sstxE01BebEjJgDXxXrnfCbBhKfuOftjjTqtig43CPigeFJZ1pESYTPhVWRfmzDbwVEyqsoz4o2gCxzEH2vwCCyR2Ty9YtlPpjLvp7b3ZROMk5d1cepM5G03l0zLIfG3V0W0BOchymNPnKfHDHEaKGyCscgTN-P10jyuG6zDRjIe2zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
من در چین بودم. آن‌ها اتاق بزرگ دارند.
🔴
آن‌ها اتاقی فوق‌العاده دارند.
🔴
این (سالن باله کاخ سفید) از همه بهتر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/142654" target="_blank">📅 18:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142653">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8f77c6fe5.mp4?token=fQNE_3uYjkCpqTqnO4uKX8l_W3mPY96-0Rcvf_56o51VTIXX_bKoc5coc4ocMpeZPBxFBSYvsJ4QV1hjsqDIVgEDFiHUxNHG11kk9MvOck-5T1Awz4sBaytgJaX3FZyuNsxdEDKAUbK0tN6otqnKzU9A5tyycCKOjVN4pvFoHaFxdwuIshDC-x4m_WxEon0kWzo_WiggK0xFPTAgk_AvKX7i34gXsL6AnUUPjYproq38IEGQfLIcPND_GPAu7R6pkWDlbH9gV2l0rkWF4a7IF600e4mdEsxZcuVyZ2nhsPIM5_dnZ1p1PQnhyocl4GlviiTcQ4iNSwSYzWSyeZ4d54i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8f77c6fe5.mp4?token=fQNE_3uYjkCpqTqnO4uKX8l_W3mPY96-0Rcvf_56o51VTIXX_bKoc5coc4ocMpeZPBxFBSYvsJ4QV1hjsqDIVgEDFiHUxNHG11kk9MvOck-5T1Awz4sBaytgJaX3FZyuNsxdEDKAUbK0tN6otqnKzU9A5tyycCKOjVN4pvFoHaFxdwuIshDC-x4m_WxEon0kWzo_WiggK0xFPTAgk_AvKX7i34gXsL6AnUUPjYproq38IEGQfLIcPND_GPAu7R6pkWDlbH9gV2l0rkWF4a7IF600e4mdEsxZcuVyZ2nhsPIM5_dnZ1p1PQnhyocl4GlviiTcQ4iNSwSYzWSyeZ4d54i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار
:
برنامه شما در صورتی که دادگاه عالی علیه پروژه سالن بال شما رأی دهد، چیست؟
🔴
ترامپ
:
امیدواریم این اتفاق نیفتد. من نمی‌توانم تصور کنم که این اتفاق بیفتد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/alonews/142653" target="_blank">📅 18:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142652">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e129e6b9.mp4?token=h5-vRsMoaqx2MI2FTH8qARgR47hUbX-G_zTbbvuom6d4ZAd7tBKdASu3aVXsFY5mVSzIU8ntF496iMMfSDAyCZLqAGUKyRCc6iM9Nw1l_6h4AQtW4xwxWzMNZe_KdSMW7GIe7dR4DeaqzpUGyXKD2MsGtLAmJPBj8QeT3WE-n-P8oU_bABcxF21Z2ShTmw6gJOJhX2r94k323nXrFHpQilWfBcBKO9eOpXJSHBguli7ug-OdDa8_2yDfQEKnVQE7JFaOWD6iDzVvpaxscPvIVKxtpiW6-S6CNvEIvQKkPSIPgM2Ph5RY4v1E0RxuTZvsZJskk-OfvJ6Mutwg9hGBYjtQHF4FnhQQAnFNMgS0mMtmjH9zTSs3nZdrBNJEsKwLg4mxl_4QNrLko2FMvcMcfVhLlRg45QER3bMKADeHjMCV92YK7UwaAi5X1hN4L8n1Myid6XAwjdLmphHGmLG3wfurjqW4dVS28EsxzsnBCqZw_uxCgS8rgZmkhDlY42JV4-GnFQViBphaEGOuybiPomONOnNwAg_vnK6lrZ6IVUxpTsdug5W6655siTP3xyXppC7OXjJwooJrWqYRsA871j1AuyWKadCLoAe0mJerQ5eSSgzqgcoCFX6FgwuRcq7sc3bY19dCPX2gEamG_VfmYoIykmjFhcfFNBU1d3z8JKM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e129e6b9.mp4?token=h5-vRsMoaqx2MI2FTH8qARgR47hUbX-G_zTbbvuom6d4ZAd7tBKdASu3aVXsFY5mVSzIU8ntF496iMMfSDAyCZLqAGUKyRCc6iM9Nw1l_6h4AQtW4xwxWzMNZe_KdSMW7GIe7dR4DeaqzpUGyXKD2MsGtLAmJPBj8QeT3WE-n-P8oU_bABcxF21Z2ShTmw6gJOJhX2r94k323nXrFHpQilWfBcBKO9eOpXJSHBguli7ug-OdDa8_2yDfQEKnVQE7JFaOWD6iDzVvpaxscPvIVKxtpiW6-S6CNvEIvQKkPSIPgM2Ph5RY4v1E0RxuTZvsZJskk-OfvJ6Mutwg9hGBYjtQHF4FnhQQAnFNMgS0mMtmjH9zTSs3nZdrBNJEsKwLg4mxl_4QNrLko2FMvcMcfVhLlRg45QER3bMKADeHjMCV92YK7UwaAi5X1hN4L8n1Myid6XAwjdLmphHGmLG3wfurjqW4dVS28EsxzsnBCqZw_uxCgS8rgZmkhDlY42JV4-GnFQViBphaEGOuybiPomONOnNwAg_vnK6lrZ6IVUxpTsdug5W6655siTP3xyXppC7OXjJwooJrWqYRsA871j1AuyWKadCLoAe0mJerQ5eSSgzqgcoCFX6FgwuRcq7sc3bY19dCPX2gEamG_VfmYoIykmjFhcfFNBU1d3z8JKM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در کاخ سفید: اسکاتس میراکل-گرو یک شرکت عالی است. آن‌ها در واقع به کمپین من کمک کردند، باید صادق باشم. شما آن را متوجه خواهید شد.
🔴
فکر می‌کنم بزرگ‌ترین شرکت چمن در جهان باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/alonews/142652" target="_blank">📅 18:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142651">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/134287961a.mp4?token=OEZZOFA1COOhkXKyeHJrkXsnLfiv50guICZZ10VIZkgnmg8UHepcrSvzo_LsmzoNUpE9-_j1UDrIi3SlaWiLx-IOepqmVLnMrDVQC65t4jMv8PxJKdeYTpGPFahJRuwm04XbojE45Y45hKj4aefF6xRcZolO8LpE6s6tcg1pPO4BU79lyGsXz8hs75F2RkaO76NxS0OGPL5FtagcNZ-61eJv8j2wKKrUXzHvmD9p7XgXmZ4IeZGxz4sxQww-SNahi33CesV8WePPibtFT1PFTauayuhZJ1IyxCc6KQFXWIR3W8PUaIyPkq9NABYp5IyPPQNoNPRxPoXVRQerHW9dVhrDF1Gytv9-Nbm4QTLP4X7w7XDfdhCltqKX7XBQQKwCUVBZHQO28Mr-WqwYDZovr4sA3S2TX1ivAP1cfrkcLgLHLFN5Qs3PzIOWduiiPNy6-7TwRn0I2UPmv359SA6Xm9vr-tmXjAlsW8TV8iEJdIq1268KV_IhBHUZTEXzR6-JGgBVPMrQFfyYtTUqJlq6hpG_j2fxMMC2tvZcKy5icvp5G_0BFsUbxI41l2qO-gKwPQiOneiUwAiYhW38ydXDqyKaicoDzFNAOhfnQHEo5Ws_OgpXsY1c_EnrNmZYwvJidl_hWPwtQEmliPKf4rW90lv2Z2IOPmrDrmX3SdPmfsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/134287961a.mp4?token=OEZZOFA1COOhkXKyeHJrkXsnLfiv50guICZZ10VIZkgnmg8UHepcrSvzo_LsmzoNUpE9-_j1UDrIi3SlaWiLx-IOepqmVLnMrDVQC65t4jMv8PxJKdeYTpGPFahJRuwm04XbojE45Y45hKj4aefF6xRcZolO8LpE6s6tcg1pPO4BU79lyGsXz8hs75F2RkaO76NxS0OGPL5FtagcNZ-61eJv8j2wKKrUXzHvmD9p7XgXmZ4IeZGxz4sxQww-SNahi33CesV8WePPibtFT1PFTauayuhZJ1IyxCc6KQFXWIR3W8PUaIyPkq9NABYp5IyPPQNoNPRxPoXVRQerHW9dVhrDF1Gytv9-Nbm4QTLP4X7w7XDfdhCltqKX7XBQQKwCUVBZHQO28Mr-WqwYDZovr4sA3S2TX1ivAP1cfrkcLgLHLFN5Qs3PzIOWduiiPNy6-7TwRn0I2UPmv359SA6Xm9vr-tmXjAlsW8TV8iEJdIq1268KV_IhBHUZTEXzR6-JGgBVPMrQFfyYtTUqJlq6hpG_j2fxMMC2tvZcKy5icvp5G_0BFsUbxI41l2qO-gKwPQiOneiUwAiYhW38ydXDqyKaicoDzFNAOhfnQHEo5Ws_OgpXsY1c_EnrNmZYwvJidl_hWPwtQEmliPKf4rW90lv2Z2IOPmrDrmX3SdPmfsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در کاخ سفید: به مدت ۵۰ سال، یا حتی بیشتر، می‌خواستند یک هلی‌پورت داشته باشند، اما کسی نمی‌دانست چگونه باید آن را پیاده‌سازی کند.
🔴
ما در حال ساخت یک هلی‌پورت عالی هستیم. این هلی‌پورت توسط شرکت سیکورسکی، شرکت سازنده هلی‌کوپترها، اهدا شده است، زیرا ما هلی‌کوپترهایی داریم که حتی نمی‌توانند اینجا فرود بیایند. آن‌ها هلی‌کوپترهای کاملاً جدیدی دارند که مدت زیادی پیش خریداری شده، ساخته شده و اخیراً رسیده‌اند.
🔴
آن‌ها نمی‌توانستند روی چمن فرود بیایند، زیرا قدرت موتورهای آن‌ها آنقدر زیاد است که چمن‌ها پاره می‌شوند. آن‌ها امتحان کردند و چمن‌ها واقعاً در همه جا پخش و پلا شدند.
🔴
هزینه آن توسط شرکتی که هلی‌کوپترها را می‌سازد پرداخت شد. ما پولی برای آن پرداخت نکردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/142651" target="_blank">📅 18:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142650">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a23b388398.mp4?token=eZ63gZ4ZXh2uux2SYqr3AY50UluKqTZiZs7nBk830tSLYpKdyIWa5nplrTkqAMhz_0JmfWpfIc_7k3ESAtJlK5HERmZ_QghhIj0dr-lV32PAbaMmi5vc3-Qen0gPg81eqHcofzBHJkH6viQ-ZRI-z2hup0gUYPreVkiNvVJNnpOikYJitoh_jXemL_QurlIOQILX44Gh_7kDVCLXiov0htBZHIRYLCxc21WSZytcsPzOU6Wu6viBJKfI7G1CIdN9Otnx7rJN06c-F1qjEeZDz-7ZqoXSaj0Ujcj18GSEBexCpY9hvwzpe9SFUf_eCmITt0o1AawjwVA3ytO9M_KMXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a23b388398.mp4?token=eZ63gZ4ZXh2uux2SYqr3AY50UluKqTZiZs7nBk830tSLYpKdyIWa5nplrTkqAMhz_0JmfWpfIc_7k3ESAtJlK5HERmZ_QghhIj0dr-lV32PAbaMmi5vc3-Qen0gPg81eqHcofzBHJkH6viQ-ZRI-z2hup0gUYPreVkiNvVJNnpOikYJitoh_jXemL_QurlIOQILX44Gh_7kDVCLXiov0htBZHIRYLCxc21WSZytcsPzOU6Wu6viBJKfI7G1CIdN9Otnx7rJN06c-F1qjEeZDz-7ZqoXSaj0Ujcj18GSEBexCpY9hvwzpe9SFUf_eCmITt0o1AawjwVA3ytO9M_KMXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما زمین کاملاً جدیدی را روی آن ریختیم. مواد مغذی زیادی برای چمن وجود دارد.
🔴
اگر شما چمن باشید، بسیار خوشحال خواهید بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/142650" target="_blank">📅 18:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142649">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
آمریکا در حال حاضر حدود ۵۰ درصد از کل تولیدات نفت ونزوئلا را دریافت می کند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/142649" target="_blank">📅 18:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142648">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gj6FLo5YafvFij3IM8lp0KgcLkk5pQQnpgcg7M7jpRhR8t9FzPRi54VcnsE-pnMZcAGu3fTCpZsEarmW8DXoPikBgPk3Xi4DDDA2LJDjp-rUtaa56ceQVZ1Ysx13qmw_QeKNbbj8o2-n5GQbH6zyrmYQ7YNv5D2-OFF-IcOCcf1eEZ49F0FQ24c0JqxWPptvoxIMVFOBFB_mFrV0ub_zMsIKVCpDZBs7_XOdzsdIkGU2-2T95LHZv5mGmM3quqzGmbaIz1b95f0KfI5g0ac-8r7ZJVuEiFzXmYR74KyOUZ3zWCStaKWDAs1p_OqySfLJcaM8BGZ7-ArUKskwSrrDSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: من به کوری میلز، نماینده کنگره از فلوریدا و دوست من، گفتم که از رقابت کناره‌گیری کند، اما او گوش نداد. او فکر می‌کرد می‌تواند برنده شود، پس چه کسی می‌تواند او را سرزنش کند؟
🔴
ما اکنون یک نامزد عالی به نام رایان الیج داریم که به جای او در رقابت است! رایان نماینده همه چیزهای MAGA است و توسط همه مورد احترام قرار دارد. او حمایت کامل و مطلق من را دارد!
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/142648" target="_blank">📅 18:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142647">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سفیر ایالات متحده در اسرائیل: گزینه جنگ تمام‌عیار علیه ایران، یک گزینه مطرح‌شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/142647" target="_blank">📅 18:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142646">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
معاون توسعۀ محیط کسب‌وکار وزارت صمت: با پیگیری‌های وزارتخانه، محدودیت برق در اکثر شهرک‌های صنعتی به حداکثر یک روز کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/142646" target="_blank">📅 18:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142645">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ppFdtsmic_FsoaDKt8U0-SdSTkOR80nUxpR4g8EIr9T-SJtyTAbfiYW5j9wanBaiKAWRPmEOYKhRsgL-wkmkZXDlpWcpJ0_sjaToOvXGoaX8PLaGOtfbrYXHlfdoWDtmumFua6vNBJkN125Plc7qXIMpSSwhUnNAQo8gfU-EAS-zn5fE05n2J4DFpte6kkBLyE2NL_9kjab3OsZAZ1UbJmdN-rfTzXCUbbzrRMz1dQfsSGVPmlLtyp6MkK8qcGyQIiBe-3W5-o_SM0JRT-UGV15iB9xLknipD5y3gJZKoOa9rM5gok8tV_fvnkLRyQyYSXuEird0XihrT8D6xOCZkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نتیجه واکس سرطان موفقیت آمیز بود / سهام مدرنا 150 درصد جهش یافت
🔴
برای اولین بار یک واکسن سرطان در مراحل نهایی آزمایش موفق عمل کرده است. در یک روز ارزش دارایی سهامداران خود را دو برابر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/142645" target="_blank">📅 18:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142644">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ارتش اسرائیل: در کمتر از نیم ساعت، دو فرمانده حماس را در غزه مورد هدف قرار دادیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/142644" target="_blank">📅 18:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142643">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0G7RvjT-SLzJZq5Oaq3vFYqXKM-Og12FjN25kInnqA9oTENvsoYAmHrnRqv_TxqxwwWup56eiektZftOTaQBxxkeG8Rby1yvDbSIS-51AeRDY2yN94JXSEIGf1BId1ivMKNUJagqY2rzGiRAJCT50gxlLuPINZmhy1GHoLE1L4CM6HCNcKi6VIYdd0_Jnj5PPxC7Ok85ZrQ1cE0xACgdJtcy-cyGkinl2sUKs6tDcfGOinE8pLN0VBEthZ4N9GEYoRKLq4GPbQFRqtxP2pcTjz6vMMhDUwZmU4kLbw5z-FfSdZoAN5CpbyMbcfNAjf5Prn38-ju_p9v2lwAP30sww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
رسمی؛ دربی قراره تو ورزشگاه نقش جهان اصفهان برگزار شه؛ 11 شهریور ساعت
19:30
@AloSport</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/142643" target="_blank">📅 18:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142642">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkEhCMcFk_aLXnZx6YpMpEHveNn4IeyCtDyf-H-5pI3KgkY0GmaauAhIoxAZmhDWVuYPJuIRxTWvTnLMFySgDlNSQfbCGL4OLKlDs5rQ2Y6uzeVEh-utTp-TCarbHLl-uC-O7w7LANRun7QjNTzS-lAoR6qesO1YtoG7wNMIkMMpnNTWivQvJUPmc-yF05C-bwCkMIq33w1SVyZMCZNZjo0_4bxESxzBtFLRXVJZ1JUrQXgG5uzqDTMOawwDTfYdo42yenKZk5iKE7noNanDQNh0XkDMfBmEH4Bc-Q1qNWLAhu2NHeh6TDbSuOxnMN5djJTPOOkNWnMOdp8CNn1ysg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خاتمی: مردم گرسنه هستن ولی کمبودی تو زندگیشون ندارن
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/142642" target="_blank">📅 18:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142641">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
گویا در تهران بزودی از خانه‌های ۲۵متری رونمایی خواهد شد تا شرایط ازدواج جوانان راحت تر شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/142641" target="_blank">📅 17:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142640">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5214028bd8.mp4?token=F_RqjM-xxYVRLMXpLobD3y1q50-pzrmDXv4V__Pgbh2BXVjBnSIb21dzFda2_Ae_rAgnseQht7iYdxOxgJyhHAw2GHoPrl0B-BeG0Yq-MJlySJlPcep4huuglxVJnLhY4_1QgszbtCATPeNPZlI67WyCI7w-xdhC3TTQ-Zp_L9Sv8IZSytaD_-CirxWWjfZsksGv7QbWQ8FK8EVyXKaoiyzNSKkzo-6B8xqDFnYX60S78ArBshoSH4fWGx5qWKES1If2pOWJsnQGRRlFyaK3WhA1IZ1kDZ9P4iz9UsPQ0KCWgoBy7NBB-pX6RjMA4YAEeBtzzbsU_QKoajJfKxj-Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5214028bd8.mp4?token=F_RqjM-xxYVRLMXpLobD3y1q50-pzrmDXv4V__Pgbh2BXVjBnSIb21dzFda2_Ae_rAgnseQht7iYdxOxgJyhHAw2GHoPrl0B-BeG0Yq-MJlySJlPcep4huuglxVJnLhY4_1QgszbtCATPeNPZlI67WyCI7w-xdhC3TTQ-Zp_L9Sv8IZSytaD_-CirxWWjfZsksGv7QbWQ8FK8EVyXKaoiyzNSKkzo-6B8xqDFnYX60S78ArBshoSH4fWGx5qWKES1If2pOWJsnQGRRlFyaK3WhA1IZ1kDZ9P4iz9UsPQ0KCWgoBy7NBB-pX6RjMA4YAEeBtzzbsU_QKoajJfKxj-Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این سکانس فیلم آژانس شیشه‌ای دقیقا برای این روزهای ماست
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/142640" target="_blank">📅 17:46 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142639">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‼️
افزایش شدید قیمت طلا
‼️
پیش بینی قیمت طلا در روزهای آتی
👇
https://t.me/+S8mMBRHkHmFiMTFk
https://t.me/+S8mMBRHkHmFiMTFk</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/142639" target="_blank">📅 17:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142638">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
پولیتیکو: ایران و آمریکا وارد فاز صبر و انتظار شده‌اند؛ هر یک منتظرند تاب‌آوری دیگری زودتر تمام شود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/142638" target="_blank">📅 17:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142637">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
قالیباف:
آمریکا به دنبال خروج آبرومندانه از منطقه‌ست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/alonews/142637" target="_blank">📅 16:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142636">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
یحیی فست از حوثی‌های یمن (انصارالله) اعلام کرد که سه اصل اصلی بازدارندگی علیه عربستان سعودی را برقرار کرده‌اند:
«محاصره در برابر محاصره»، هدف قرار دادن استقرارهای نظامی سعودی در هر کجا که مستقر شوند، و پاسخ به نقض‌های قلمرو و فضای هوایی یمن.
از ۲۰ ژوئیه تا ۱۹ اوت، حوثی‌ها می‌گویند که هشت تانکر نفتی سعودی را هدف قرار داده‌اند — پنج مورد در دریای سرخ و سه مورد در خلیج عدن و دریای عرب — در حالی که ۴۸ کشتی دیگر را مجبور به بازگشت کرده‌اند.
آن‌ها همچنین از نه عملیات علیه اهداف در ينبع، نجران، جیزان، ابها و شرق عربستان سعودی در پاسخ به حملات بر فرودگاه صانعا، بندر حدهیده و نقض‌های فضای هوایی گزارش می‌دهند.
۱۴ عملیات دیگر استقرارهای نظامی، تجهیزات و کشتی‌های حمل‌ونقل نظامی سعودی را هدف قرار داد. حوثی‌ها می‌گویند این حملات منجر به صدها کشته و زخمی، تخریب تجهیزات و انبارها، غرق شدن یا آتش گرفتن دو کشتی فرود نظامی و تخریب بیش از ۱۰ قایق نظامی شده است.
این گروه هشدار داد که هرگونه تشدید گسترده‌تر از سوی عربستان با «پاسخ جامع» مواجه خواهد شد، در حالی که پایان محاصره، پرداخت حقوق و خروج نیروهای خارجی از یمن را مطالبه می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/142636" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142635">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/La6byw_mwXFfRrwHHcJGPZT0FWZWUFHIEf4plbeVAXGpcHmZ2WOt0u0HaDNC3nEMBdIrjke22mTBJIrydcRbhq4G-ukXRDTEU8lCmOmtR-U1x6UtRIzYXm5ATUAIB8KlIaGgkeDnUGhSdoUI1IVaEvL-E5TKCKWHGFkHxnOsd8fGMtVDh3lrWfvzh4fumOiD8vRRXdOOSsE5SOPfVi1NbG2cNvrzQYTEzAYiM86Pt3eqloxYKcgBPhgM8z8d7ZZz2XoLQFw-e2Yg06dpy5NYhjimsxSH8qDR0VL9i14T_33Wn_CZKV-a_zeBn_gDys_g7tkKd8Sjm9zxFz3oMuyPEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی: کاخ سفید همچنان در حال ارسال پیام به تهران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/142635" target="_blank">📅 16:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142634">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tk2qMGIUMEaLHucUBcmd8kKymefIZ8dXonaPj8oukH7K2RjpPlWUAgPuXDJ5ThEB2_nYUtHvgGKBstVl5ioTBY-wr7u6gUpsw2gURY1ZwkdjPR6G63--f61ktAKa6SVu57Xjq6WuGgGBpcaXXpUYGT-UnXSUlLY5Erc4SYDrlAurtZdbwRRaf32FR2MtUWUCFqK21rog5kUb0l398YuN37mhW2k5yspPZCArLpY6ccZR-brbheUNNFHYZKdwDPWCt7uHihEAaD3n4nkwnQ48iJCp5_MkspggKjVT46xVm1i-wUZ6vn_T8e6PhBDExhHbaJf-EfSlcfkw2Ixxzv8RZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دولت با طرح «مقابله با نفوذ» به علت مغایرت با قانون اساسی و حقوق شهروندی، مخالفت کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/142634" target="_blank">📅 16:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142633">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXCNu31v1pegqLzQ9Sn9bQfByvDaDcp5sgyTPrB5XTY_2eXwh7JiyjP31Sx422XVgnVELvcLhzdz7KKPbU5a7BNthDz6W0nG4goU3zaOghc7Rc9Hp3nRnrnjAYy6PH4a5-Usxsh0FbOlnedsWQhCk9pCaj8Yl2qkdCuYKC06Oxxq1d7CSgfIL9bhvpSAubidiI-e-B6aCAWB0dkpCQ5RKmdmnBmLYmRP1om73k8Zsw9JMSrexZkoeUvtq-4rjSGDfdCRGgtUTdmYdi1WCLf1Yg02NAbC81f-ZSIjIQgPzIOs2eIBhVLNth5tetfduepaB5JPgSNGKWFoE1gHME5hIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش رسانه های حقوق بشری
«آذر یاهو» به دلیل گذاشتن استیکر خوشحالی برای مرگ آیت الله خامنه ای و همچنین کامنت گذاشتن برای نتانیاهو؛ به ۳ سال زندان محکوم شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/alonews/142633" target="_blank">📅 16:13 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142632">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RF4G_Q4G5sxAT8z4pKmK_k5OoilBMJKp0XnBlBMGMiuWUBefKT-UdJqFek1T4GVYN1P7cSzBw8RD_b0PflmaWv34ja33Lj7c7YlDgn5yqRyIZLS9xDDid2FaxWaBd-7mVqvLo6Ns9Yaq4OVSQY_nlMw8Ss9YOhtzMfwP-jasK3A5qAptv34VPPseAAsrp1DDevRgPCqRGPDg5-BZGto_mVg1bHomwnF6SCpwrfWbA3R4adLRfsM0BoBKs9shoe-1PUeBJjAlo65JdvvXn6TIHUM8tJOXB7yuont-acKHyI75n2X3TDk-z0_mkMg-tkAUX3IyoYpbxhIMgBfiAXnFtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: باید آب‌های فلوریدا رو با مین‌های هوشمند مین‌گذاری کنیم، اینکار میتونه حواس آمریکا رو پرت کنه و ارتش آمریکا محبور بشه بخشی‌از توان نظامیش رو به آمریکا برگردونه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/142632" target="_blank">📅 16:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142631">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eb1f98eb1.mp4?token=v65YONjNUFSkQgqc3WC5Xm0eZuPYk-8A1y2uUCqxKN2s2lYUpEAr8j_L3OgRYD-7h0yKDjeB00y7fbcsHwm-WAKq-UfWR21VEcX6mqJ0Akx5-veuLa6fQplbqnc5YQhhojnwci-I7eZvwwIWpnhJprQcSZnG5hvM72uouQqI2j-M-ezsAcy8jtdJtg73tQMsNMeeyp8BUe4gF4TqpJLndrEYREPablHw_Dpj58fG3x-Ee9IxBDb1kDj8Qc2rKn64ybb6_jpkYMpbzce4Z4bWjm1C9GsmjD2Wg3TWHy7iZ5POlfIFRa-dTZHtoNWl33hX76T-BMCmAal9brETApULIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eb1f98eb1.mp4?token=v65YONjNUFSkQgqc3WC5Xm0eZuPYk-8A1y2uUCqxKN2s2lYUpEAr8j_L3OgRYD-7h0yKDjeB00y7fbcsHwm-WAKq-UfWR21VEcX6mqJ0Akx5-veuLa6fQplbqnc5YQhhojnwci-I7eZvwwIWpnhJprQcSZnG5hvM72uouQqI2j-M-ezsAcy8jtdJtg73tQMsNMeeyp8BUe4gF4TqpJLndrEYREPablHw_Dpj58fG3x-Ee9IxBDb1kDj8Qc2rKn64ybb6_jpkYMpbzce4Z4bWjm1C9GsmjD2Wg3TWHy7iZ5POlfIFRa-dTZHtoNWl33hX76T-BMCmAal9brETApULIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ظفریان، معاون مرکز پژوهش‌ها: ادعای کسری روزانه ۱۵ تا ۲۰ میلیون لیتر بنزین غلط است.
🔴
با افزایش تولید بنزین از ابتدای سال تقریبا در مرداد ۲ تا ۳ میلیون لیتر در روز کسری داشته‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/142631" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142630">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
اردوغان: جنگ ایران و آمریکا راه‌حل نظامی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/142630" target="_blank">📅 15:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142628">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCciRPifQ4-wSrYgZhE6Z-HkBH9QuV78tmE0AKogRuq5vdJNPE-arj_N5tXxIXRftuoV-TUoKttPCW1ikZ9lfNJ4RysVc6J0IUqKY_0nUKH_5-GkIAxIKiZG_5kjt4A9Xagxj-jFIJTcT_SvRVEw-4G1aG1sfwItyj2v9RuPhI8jbvbfCwsP2_9Utr7ZW722x_cnpBrn9700mg4aFX4PnGaxKINA8OTNognLx-bs6U5OXB6bI4CKBmEJspEW21o-ozpOVuN4_-U1-XR1QbK7p2XY6WKdBUSSBwaO0XvKq1SSUYhrvTZV9mcLsaPG4iZxgcM59GhjXFGvFpBA4XKI8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
حداد عادل: تنگه، تنگه
😈
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/142628" target="_blank">📅 15:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142627">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a6fb20727.mp4?token=TDvE_nNpNqviUOTBUi1JkGnKUGFuS-qIRevir8ZRLq_YdWGWXzlm56jlJQVBoEOpFUtZUVQmZXJ_-ZBAPPRhDY_s41BUg3brf71THVpEY38qlzCrV7HwwDl4fTedSatDryhsBbsmDCCIc2DF0JhP35uE9uqeqhGDMq_WaeuVwdgJoiATJxZiZN48Lw_Kn9xeblBVi9ArCzdY-NsI4EvqTDSvLVBdtubFDP-B4LEDL7oURrkjXlPn0brEWBcSrGJOyyagP2G6lIc_sm4x2KJKRIQSwSygxMWvjwYuGNAW8wOyO9xOIux2yCwsVj4DBAaNtfoEmaBwANgoo144PWbh4Xfa3UNboXtemS7HRbHa9mRkMpXzx-jG3iKj3DyWdfQFq6J9ma6QKyLdQ7xorz8STNY97xgICj_Dryx8uEBfq-6NZnDI_9nE4E5uL47Gfy36JzTCf7N4DBd70BB0g7oHNDch2wnal2gtWv8uhtwycdJ5WUR9jWxyn_n2wLYzykKCfDuZxEawkovX9S0mE9jFE8L6m2RjECfefDwjYL9gRjYigJm45lcNPyGEr0gNBav5UogL4Inu5vby33VtsIQoVJZtxunKoaNwQJ76mgYy6R8Cw2ekq7cpmvn3_3uy9dUWP6HDWu-Yvw4Fxpj7Dzp4ttXrsAukHjBIoWpl5tSuDwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a6fb20727.mp4?token=TDvE_nNpNqviUOTBUi1JkGnKUGFuS-qIRevir8ZRLq_YdWGWXzlm56jlJQVBoEOpFUtZUVQmZXJ_-ZBAPPRhDY_s41BUg3brf71THVpEY38qlzCrV7HwwDl4fTedSatDryhsBbsmDCCIc2DF0JhP35uE9uqeqhGDMq_WaeuVwdgJoiATJxZiZN48Lw_Kn9xeblBVi9ArCzdY-NsI4EvqTDSvLVBdtubFDP-B4LEDL7oURrkjXlPn0brEWBcSrGJOyyagP2G6lIc_sm4x2KJKRIQSwSygxMWvjwYuGNAW8wOyO9xOIux2yCwsVj4DBAaNtfoEmaBwANgoo144PWbh4Xfa3UNboXtemS7HRbHa9mRkMpXzx-jG3iKj3DyWdfQFq6J9ma6QKyLdQ7xorz8STNY97xgICj_Dryx8uEBfq-6NZnDI_9nE4E5uL47Gfy36JzTCf7N4DBd70BB0g7oHNDch2wnal2gtWv8uhtwycdJ5WUR9jWxyn_n2wLYzykKCfDuZxEawkovX9S0mE9jFE8L6m2RjECfefDwjYL9gRjYigJm45lcNPyGEr0gNBav5UogL4Inu5vby33VtsIQoVJZtxunKoaNwQJ76mgYy6R8Cw2ekq7cpmvn3_3uy9dUWP6HDWu-Yvw4Fxpj7Dzp4ttXrsAukHjBIoWpl5tSuDwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اظهارات نفتالی بنِت، نخست‌وزیر سابق اسرائیل، درباره ایران: اگر حزب‌الله به ما آسیب برساند، ما به ایران آسیب خواهیم رساند—به روش‌های مختلف.
🔴
هرگونه حمله از سوی بازوهای "اختاپوس" ایران در داخل مرزهای اسرائیل، منجر به مجازات‌هایی خواهد شد که در داخل ایران اعمال خواهند شد.
🔴
در دولت بعدی، ما این سیاست "مجازات" را به طور کامل اجرا خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142627" target="_blank">📅 15:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142626">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
۳۷ تا نماینده مجلس برای حجاب، به پزشکیان تذکر فرستادن
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142626" target="_blank">📅 15:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142625">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzKx8M131OiVV5vBSxlxbE9YN0vajtrE9FdXFzWvI_-4es8JiLGdmaWfEHQA1Mtmn8nSUW6Q_IdDV0QAxfFmETr_PmIPOIQ4V2Xmphpa5xHAoqtLM0PtVKJVHqr0gvAhrG49p_xAbkpqf3ehkgJDnDjGWGXZO85N0k4LOUq48QYz8d0JT1J57ugwxMF9w3mcHvBq5F7GGAE9NxMsOi23AG0HNNmT8EZmZqCiAA8sWVqvRc0nZgOexM91LRbybEkxsgB7lf-0J_NoDo-21P99oxLECXBXFEkYCJAFGRC8MITcS8j0p-OKPy5srMMrCwOOUdLVX9JeoaDnwAt-aA6new.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو شهروند کشته شدند و دیگران مجروح شدند پس از انفجار یک بقایای جنگی در شهر میفدون، جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142625" target="_blank">📅 15:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142624">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
وال استریت ژورنال: حملات اخیر ایران در تنگه هرمز، روشی را که امارات برای حفظ صادرات و تولید نفت خود به کار گرفته، تهدید می‌کند
🔴
در این روش که «سفرهای شاتل» نامیده می‌شود، نفت خام و فرآورده‌های نفتی از داخل خلیج فارس به کشتی‌هایی منتقل می‌شوند که در خارج از منطقه منتظر هستند تا محموله را به بازارهای جهانی منتقل کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142624" target="_blank">📅 15:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142623">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
رئیس ستاد کل ارتش ترکیه در تماس تلفنی با دن کین، رئیس ستاد مشترک ارتش آمریکا، درباره روابط نظامی دوجانبه و تحولات خاورمیانه گفت‌وگو کرده است.
🔴
جزئیات بیشتری از محورهای این تماس منتشر نشده، اما گفت‌وگوی مستقیم فرماندهان ارشد نظامی دو کشور در شرایط پرتنش منطقه، قابل‌توجه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/142623" target="_blank">📅 15:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142622">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
جمهوری آذربایجان، دادخواستی رسمی علیه شبکه خبری سی‌ان‌ان (CNN) در یک دادگاه آمریکایی، به دلیل گزارشی از این شبکه که ادعا می‌کرد نیروهای اسرائیلی در جریان جنگ، در داخل خاک جمهوری آذربایجان علیه ایران فعالیت داشته‌اند، تقدیم کرده است.
🔴
جمهوری آذربایجان این گزارش را به طور رسمی تکذیب کرده و اعلام کرده است که اجازه نمی‌دهد هیچ کشوری از خاک خود برای فعالیت‌های نظامی یا اطلاعاتی علیه ایران استفاده کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142622" target="_blank">📅 15:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142621">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4wI4lhipb9D7qRWcmg92Q3UhX4YKgjDQ_2-sSe3SW-vxXLiw5xMI2voT1BjrrDlMoGnafnsB-ueATZmqZK3FixEYkEzfajhFQFkm2-Dco5EUQJjJze0mloeDKxRB7ZWQI7jcxoQFKDyJuynlKqjDoBC_N1i0JoXNK3S9mSXStCiC2GWZnRopHkoQTrDcRkKqAS28nSQt3xRO9hYDpfzWrJwqqlT0SV3s_3LTqvSkYLS_1AaubE0I6iDegYJz4aPe7N1z6hFsL6B08HwNu5G0gXLsCZfC9V3GiEA9vx7QmEUeIoUAc4prbdN1tphPm8oH6Xp-JemEyl_QJJtNK4sjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی: کاخ سفید همچنان در حال ارسال پیام به تهران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142621" target="_blank">📅 15:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142620">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
رئیس مجلس عراق از قالیباف خواست تا اجازه عبور نفتکش های عراقی از تنگه هرمز را بدهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/142620" target="_blank">📅 14:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142619">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
پروازهای فلای‌دبی و ایرعربیا بر فراز فضای هوایی ایران از سر گرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142619" target="_blank">📅 14:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142618">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPxNg-vnuMRJuk2elq5_EicOJcrhuNipf1yEC2qoc_nEQKOPzcyV-jLnydWcsgKXkZL2IWY5rSD-RZUmFpmwwENTKF6n3uOPBMZt0Wtdwu1_3KzR-Iq5FjF3lvT821kI6ZZzLaeH2I2ryre1E-6aXaB1S-8w1wDNVzoHoapRV9b74jUsQAjwz-62YizdSb83g_tHczC5Wpmm3fKTKSEgSdcK0uo9UR-zBhdqylpUh0zBxEAoT3ydVgfTHo6JN3z-HilEmIKz9i1RiHM7yN0JwvUnSEZ4MIfeAu7rADAMoQ3Ka38fijigwHPMYoQEFe7fIpPjv7RmGWrHNzMV2FqkWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسما از سوی فرانسه اعلام شد: اخراج دو کارمند سفارت ایران در فرانسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142618" target="_blank">📅 14:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142617">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9t1lBSyiFPDHw85LEj6pecYHM5t1N9_G0j9eeHMC23ZSLc6w34WDqozWJet3j2IOaPdRRfvGqTwHr8bdYU3hdx0fPmE5bFZ8HvH2P0HwbrC5m3bRBOA9kUzuG9vk_J9szxJkIEzNq9V-i7dCWH-kJZqadH1FpYvwg5KmxKbxOi6ek1ZFW68ZGfNz0B1XfePacj5X0LaJCi5UByjodwMjqJ99-3G7ZQawrGS_Mys_cX2FdN7PjNZzXVZS2G82k7uGPwBM3fF7mU6mKcAL4_FOpo96oGG3-ev42r-Qh7h8q982c6ArAxqk_erW3T_p0BmpgV6nC778_J6PsydI5vJIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابراهیم رضایی، عضو کمیسیون امنیت ملی مجلس : لباس‌های ترامپ هنوز بوی غذای هواپیما می‌دهد، اما ادعا می‌کند که تنگه هرمز را تصرف کرده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/142617" target="_blank">📅 14:46 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142616">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
به گزارش بلومبرگ، شرکت سعودی آرامکو به دست‌کم سه پالایشگاه اروپایی اطلاع داده است که در ماه آینده، تمام حجم نفت خام تعیین‌شده در قراردادهای آنها را تأمین خواهد کرد.
🔴
این تصمیم به معنای ادامه تحویل کامل محموله‌های قراردادی نفت عربستان به مشتریان اروپایی در ماه آینده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142616" target="_blank">📅 14:30 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142615">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
اسرائیل به هیات صلح اطلاع داد که قصد ادامه دادن حملات به حماس در غزه را دارد و فعلا حملات را قرار نیست متوقف کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142615" target="_blank">📅 14:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142614">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abb069838.mp4?token=UKEqwo0pQc1Ekqa4UoctUPnnqYFeXoFa_7W3YhqHHpIZiBVU9NXLbxzxmPtsoWT8P8FdXBDYm_dwy8sZBOJonp_r44e0YQm0pA6BZHzOO0h1Tha-JqfIOGsW-x9pANvUh4sA74ZyRThhJdDRNJ1bkLMv8ysmjRxVPeEzYB1_7Zi84lh27HxA1Dq4KxkPQsU33-uvMuIxwCENXQNxQvQGUez3pEgx-aEvsAfrPyLALvogCGY5yTLhHYPJzolm_gW2mTQvk3ybfLJUXuihZTeYnvX2W9FaYIuHVjTMIEwbDq8FvMfzm9eVbnY_JX8q7zqO9pFJ_vHysUzzIG2IsT9Urg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abb069838.mp4?token=UKEqwo0pQc1Ekqa4UoctUPnnqYFeXoFa_7W3YhqHHpIZiBVU9NXLbxzxmPtsoWT8P8FdXBDYm_dwy8sZBOJonp_r44e0YQm0pA6BZHzOO0h1Tha-JqfIOGsW-x9pANvUh4sA74ZyRThhJdDRNJ1bkLMv8ysmjRxVPeEzYB1_7Zi84lh27HxA1Dq4KxkPQsU33-uvMuIxwCENXQNxQvQGUez3pEgx-aEvsAfrPyLALvogCGY5yTLhHYPJzolm_gW2mTQvk3ybfLJUXuihZTeYnvX2W9FaYIuHVjTMIEwbDq8FvMfzm9eVbnY_JX8q7zqO9pFJ_vHysUzzIG2IsT9Urg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیشب تو تبریز ۱ پسره مزاحم دختر میشده و کسبه هم گرفتنش انداختن تو سطل زباله
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/142614" target="_blank">📅 14:20 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142612">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a77ace1c.mp4?token=dFKZe7uEUqLTMbZldRwl6jmSCUVyAjaANcBfu8nMEuuHrFfDfTsCAojOidtJlj1KPyMfg3eGCINCwCW1DW9zH_8tHPDvqpZs2bV_-Dlv9EjGTWuU5823rRPEpMtGYAzABbZ2wTwQvxZbzGV-dHwZGJIJF3RQac1Yh8GIQydQoTdKkLSOlj1_qKzJv8FLDx_dK1OgALj-rfWfxE-ftdWatCiEmiimNoDKXncu1U3w92hSn0jgWFQF5uoaLxXgoIUzMbBrbj1tIsfWB3F3jmkmH1Ml-iNERtjJEQ3AjuuZqOHsi5Qo_cKu6tJrI32mjNsOabcoCNtyofUh77Vj0q9Qmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a77ace1c.mp4?token=dFKZe7uEUqLTMbZldRwl6jmSCUVyAjaANcBfu8nMEuuHrFfDfTsCAojOidtJlj1KPyMfg3eGCINCwCW1DW9zH_8tHPDvqpZs2bV_-Dlv9EjGTWuU5823rRPEpMtGYAzABbZ2wTwQvxZbzGV-dHwZGJIJF3RQac1Yh8GIQydQoTdKkLSOlj1_qKzJv8FLDx_dK1OgALj-rfWfxE-ftdWatCiEmiimNoDKXncu1U3w92hSn0jgWFQF5uoaLxXgoIUzMbBrbj1tIsfWB3F3jmkmH1Ml-iNERtjJEQ3AjuuZqOHsi5Qo_cKu6tJrI32mjNsOabcoCNtyofUh77Vj0q9Qmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در پی ریزش یک معدن طلای سنتی در منطقه زامبوی در شرق کامرون، نزدیک مرز جمهوری آفریقای مرکزی، دست‌کم ۱۰۷ نفر جان خود را از دست داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142612" target="_blank">📅 14:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142611">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpY2v-P9NrCdeydTMr3ZZMzSYMm5-KklqKhSzyX8bk0z4POF39xwz0v6Vm9M7Rq71ky854_id7THQFQnZ7_6xGYHTbhmi0JX90VgNDF9wU8vzYGhBlqM1vg-qDWjZsoBNIYX04wOWFYAgyqpVvoPmyEC96ekxWoezmBlt8mBQWmo3gedjgLaXqzRTivWqcusdloqLOExWLOgUH61mc7NCtW2u-8PNAN1vDiHCxSiZIkIDpyNgC8VugmhMDhk6VtfeouG2q7PPFlu66kdWi9erszdE4WhkBOXKkayvYkpoYzmKHRQfgN4YiLK6EFDpP_TQDWJZ3Cpdx7Ww0GM5ZzhbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گیدون سائر، وزیر امور خارجه اسرائیل: بیل کلینتون اگر تصمیم درست در مورد کره شمالی در دهه ۹۰ میگرفت، این کشور الان بمب هسته‌ای نداشت. اون موقع تصمیم بود که به کره شمالی حمله کنند، اما در نهایت این حمله را انجام ندادند و این کشور تبدیل به یک قدرت هسته‌ای شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142611" target="_blank">📅 14:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142610">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
اداره کل هواشناسی استان تهران نسبت به بارش باران در نیمه شمالی و وزش باد شدید در نیمه جنوبی استان همچنین کاهش دما به‌طور میانگین بین ۳ تا ۵ درجه سلسیوس هشدار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/142610" target="_blank">📅 13:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142609">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
شرکت توانیر اعلام کرد: در پی آتش‌سوزی در پست برق شهرقدس که ناشی از فشار و افزایش بار مصرفی رخ داد، بخشی از شبکه برق منطقه دچار اختلال و خاموشی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142609" target="_blank">📅 13:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142608">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/httlNNnQMh5k8Mv_EDCII_2DeajqmXDvvPO1bNmRUUBdPr-56tdGT8QlkLHAZrxa3VLzYLrRbPlYffyGC1iKlAGy-cxh13Ceszn4LRwj6NiuGq3c3RWjCs5G8KsQh2xauInOz4WAM-hLgBBFNREiaN9OUmc6a61uQ_uK4vCDX5BKZh2W8ThNH4ahadmsm73ZQYB1Ou-CJP0wdPiBAeRs27kQVAz0yeEEGgFD193j0K7CiCAb8k-mbXlQRadpdMqbvXFK7257F0ZvSlkKoJwaRgX95aFIhizXaRagpVkuODbcYSXI0tZxrGZtAMXL6EhsSZGvrH5u2_WvUDj0LhKGjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت ایران در هند، در پاسخ به پست ترامپ که تنگه هرمز را جزو قلمرو آمریکا خوانده بود، کالیفرنیا را جزو خاک ایران اعلام کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142608" target="_blank">📅 13:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142607">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ناتو: آماده دفاع از همه کشورهای عضو در برابر هرگونه تهدید ایران هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142607" target="_blank">📅 13:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142606">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbzYmjRhDPev8h9mL2e5Ma8LYNFs3w4o8QJWjopZUKto4JNZKNEaWXQqD7srTFUA9KSCtKs-agB6fxOo7N3xNJrosTOMXAo_Ti2blE6z5UbZ4wXGjjmm6BlQeWzhAoihbk1K4ei_77w886ygtoS4wkbtTwVE5ii8lgjBeDve5UKylkonxRm0e7JcTLuEUUjl5EJEpitg96y0jCmbfdiyJowotC8AGBcjYUS9dCkbXfKqIhkYfGzjA1TxMjLGU4NNdQuKeJT1mo2pj6QxtVjyzPPHgCmgYNMhrjlwm21BnqmWxbiy-a3lXWnOYpxl9lYMIR5c6zo_fO1PyKD-GBT7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار رئیس کمیسیون امنیت ملی به فرانسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142606" target="_blank">📅 13:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142605">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjjFmdrG-4TaX5eIjfE8EZ-BdqMSWr76epjbCu9bAeOejQSn_0EXN0MR72-4_2k0X2sIRQiSptgsqHFyQyYviHJnkXbf4bsauksQnB7VD0IJxAVAcycVDUPztwBvitJWCq_zFFVBc6TFvXUTZEJ4ca-WhUPKBXFOcOBa6JuQpmbNly3vm6HeozAoGkGKWNllGbQIHivi2gwe2gWgxWH-Rt29VuDK1x5dt2Lwgu0x3HwwveJHKwn8qS5AUPUP9bPZ1S-nQadawjWYcdS8tZoO08ziNjwd9EKlbdhNvFf02vqIPKxz6UDajhnSFZ0Q0C3wvijJKRIF91Yke2BuAhMKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غیبت ملانیا از ترس ایران ۲۵ روزه شد!
🔴
تا این هفته، ملانیا ترامپ پس از غیبت در دو رویداد مهم در واشنگتن دی‌سی، به مدت ۲۵ روز در انظار عمومی ظاهر نشده است.
🔴
این غیبت پس از آن صورت گرفت که سرویس مخفی آمریکا اعلام کرد ایران ویدیویی منتشر کرده است که ملانیا را هدف قرار می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142605" target="_blank">📅 13:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142604">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ایرانسل: شایعه کسر چندبرابری حجم اینترنت بین‌الملل صحت نداره؛ ضریب ۲.۷ مربوط به تخفیف ترافیک داخلیه و مصرف اینترنت طبق تعرفه‌های مصوب رگولاتوری محاسبه می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/142604" target="_blank">📅 13:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142603">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
رئیس اتحادیه کسب‌وکارهای مجازی: حدود دو هفته است که مجدداً صدور مجوز پلتفرم‌های آنلاین طلا متوقف شده است. قرار نیست نظارت مانع فعالیت کسب‌وکارها شود
🔴
باید میان بانک مرکزی، اتحادیه و سایر نهادهای نظارتی تقسیم کار شفافی در این حوزه انجام شود.
🔴
معتقدیم باید چارچوب‌ها به‌ صورت شفاف مشخص شود تا کسب‌وکارها بدانند چه نهادی مسئول چه بخشی است و فعالیت آنها در چه چارچوبی باید انجام شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142603" target="_blank">📅 13:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142602">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qz4AI2CqtXzC8B_bt9Gn0vy1mZnQ7_lPNwo__lng9mIISCNebrGZfx_nz0qZjlBduao1hqbt-yXBgl2OaA8m3S9JXPNTwY5E-PClsjZadmDEyTV0Xqx1mO8uI2OMONlmQqWLqfTq0sBF7Wvv3KNvdEoL0BEOPVlLMnxOYc9w4uBgRZ6l9izx4M-A3a4DACARzL8rJj0hdec0D4DnS3vP0NEOsJaSkx3hkl23hfvv3qwiVH_DhRgleVAcNLS7ja0wyRvneOgN8PIBYU4R1XBAYtWRDSG8EeldoZSui71R8larkutXLtmZrv9UifOcqkz6gPH_8198zZo5qJx0K4D7hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار محمدباقر قالیباف با رئیس جمهور عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142602" target="_blank">📅 13:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142601">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
وال استریت ژورنال: مقام‌های عرب می‌گویند ما «بین ایران و آمریکا گیر افتاده‌ایم»
🔴
آن‌ها معتقدند ایران در نهایت به افزایش فشار اقتصادی، واکنش نظامی نشان خواهد داد، در نتیجه، جنگ دوباره می‌تواند شدت بگیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142601" target="_blank">📅 13:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142600">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
بلومبرگ گزارش داده دو نفتکش غول‌پیکر مرتبط با چین در میانه افزایش خطرات کشتیرانی در تنگه هرمز، مسیر خود را تغییر داده‌اند
🔴
نفتکش «سی ۵» که حامل نفت عراق بود، پس از حرکت به‌سوی هرمز تغییر مسیر داده و در میانه تنگه لنگر انداخته است. نفتکش «هستیا» نیز پس از ورود به خلیج فارس، مسیرش را برگردانده و از منطقه خارج شده است.
🔴
وقتی نفتکش‌های بزرگ هم ترجیح می‌دهند برگردند، نگرانی از امنیت هرمز دیگر فقط روی کاغذ نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142600" target="_blank">📅 13:03 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142599">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
روسیه و اوکراین ۲۰۶ اسیر جنگی را مبادله کردند
🔴
وزارت دفاع روسیه: ۱۰۳ نظامی روس از قلمرو تحت کنترل رژیم کی‌یف بازگردانده شده و در مقابل ۱۰۳ اسیر اوکراینی تحویل داده شدند.
🔴
براساس اعلام این وزارتخانه، تبادل اسرای جنگی با اوکراین با میانجیگری امارات انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142599" target="_blank">📅 13:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142598">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
نایب رئیس کمیسیون امنیت ملی مجلس:
به زودی یک «معبر جدید» در تنگه هرمز، غیر از مسیر جنوبی، در قالب بیانیه‌ای مشترک با کشور عمان اعلام خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142598" target="_blank">📅 12:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142597">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2424f78cb2.mp4?token=OcNtyTRh4ASyUCUXZRWUd3hsajl9ybBlPKLZRXn-f7f0_VpmHzEjQhWrlDENkGI03HzCMDhLWkN2YW-jPZfEpx5-fAwdm-5t5IlRoviq-0SeE-9bz_94W8nUzxOrE8YmRbGsBddqkjJZN6T0Gdd3BGQz49V7cxOIfSYGLFxERmbrXPlcAkNBcRTLS4qV_R7nDJOPGQBcMdPzyd24gHcukjBPjD3vtaIbLuK_gGeIi0VKFq_DbWk-9fnQJ19P3WY8pijAcUWExNZ4xR9xnPktCIebsok4yqJNkPvftzjxLvfWRZ9pFx8AE8ZZfB4S7ahH30UEiBGvmbMSh_wKL5UAX6Ph_IPNZ2OSO3YalIsQpUBA0eP84-UtDw-2_i6x9lDpVPG4Qt2lS6qA7hVVWMK1ScRI4bOFqeRHR7y24hyTQsI7uhGZ9ZpkUA8kkSUjOhDZf0i0STzemhwx8OLiOzKcfLaFkZ6CRa-JKix55kWFmWYhMQM0y4fUVys6Nv8EEcKPixcwXWDjYiFuvxL90ln-zPu16mIh-mls2kZhCnrS9OxE9TXkfMNK1BduFqBhsqkKOHXN28puLZXhTYM6FAGJ8rFf-91jKQCt6UzsIX6i-F7Cd8BeZ2ISSBwa4oOnjvkfMVWznhC9LFsY8sE74ItJNoWkgjFrYNbVvmURJ4Z5V48" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2424f78cb2.mp4?token=OcNtyTRh4ASyUCUXZRWUd3hsajl9ybBlPKLZRXn-f7f0_VpmHzEjQhWrlDENkGI03HzCMDhLWkN2YW-jPZfEpx5-fAwdm-5t5IlRoviq-0SeE-9bz_94W8nUzxOrE8YmRbGsBddqkjJZN6T0Gdd3BGQz49V7cxOIfSYGLFxERmbrXPlcAkNBcRTLS4qV_R7nDJOPGQBcMdPzyd24gHcukjBPjD3vtaIbLuK_gGeIi0VKFq_DbWk-9fnQJ19P3WY8pijAcUWExNZ4xR9xnPktCIebsok4yqJNkPvftzjxLvfWRZ9pFx8AE8ZZfB4S7ahH30UEiBGvmbMSh_wKL5UAX6Ph_IPNZ2OSO3YalIsQpUBA0eP84-UtDw-2_i6x9lDpVPG4Qt2lS6qA7hVVWMK1ScRI4bOFqeRHR7y24hyTQsI7uhGZ9ZpkUA8kkSUjOhDZf0i0STzemhwx8OLiOzKcfLaFkZ6CRa-JKix55kWFmWYhMQM0y4fUVys6Nv8EEcKPixcwXWDjYiFuvxL90ln-zPu16mIh-mls2kZhCnrS9OxE9TXkfMNK1BduFqBhsqkKOHXN28puLZXhTYM6FAGJ8rFf-91jKQCt6UzsIX6i-F7Cd8BeZ2ISSBwa4oOnjvkfMVWznhC9LFsY8sE74ItJNoWkgjFrYNbVvmURJ4Z5V48" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاسگاه پلیس ترکیه هدف پهپاد قرار گرفت
🔴
طبق گزارش رسانه‌های ترکیه‌ای یک ایستگاه پلیس در استان «ترابزون» که در ساحل دریای سیاه قرار دارد، هدف یک پهپاد قرار گرفت.
🔴
«ترکیه تودی» گزارش کرد که این حادثه دیشب در منطقهٔ آرسین رخ داده و تلفاتی نداشته است. فرماندار ترابزون هم پس‌از بازدید از محل حادثه گفت: «اطلاعات پس‌از تکمیل تحقیقات در مورد منشأ هواپیما ارائه خواهد شد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142597" target="_blank">📅 12:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142596">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: وجود یک رادار پیشرفته ترکیه‌ای در خاک سوریه به آزادی عمل هوایی، نه تنها در سوریه، بلکه در ایران نیز آسیب خواهد زد. حتی هواپیماهایی که تلاش کنند مخفیانه به سمت ایران به پرواز درآیند ممکن است کشف شوند، و این نشان‌دهنده میزان خطر بالقوه در سوریه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/142596" target="_blank">📅 12:49 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142595">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoVgsrLthmV8p2XYHvykFC3q4ps4wPJD-ZO31Mfqh3wsL6Mm7WyDP7voW75I5gJNpe9IEY3l7oCPYZIZSlM0VmgY-utb4rGPl_thr-OLrxBPPjLffiOOCpGPB8fe1fsNCefbzTf7Vv1AIMQH9qC1o4GsEDK3Sjv7zMJmEVwwtNvYuNOefs-7xHF5eBikAShPFrPNg5S1tSGbVYWeUkwiD7aR0U51EYFUrJ4FuzYo2_wRVboZMUeYYLL-0ELLSZmPfZ62pv7vS68vuZxTGNXtG8U2UG-mXQwT460XGPxuQ9WnJjAc85ErLIRZNROesVupw2I0-4SPQcr4IgVl-7kZIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یاسر جبرائیلی، فعال سیاسی: بنزین ۸۷ هزار تومنی در کرمان عملیات فریب بود. بنزین شده لیتری ۳۰ هزار تومن و به زودی اجرایی میشه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142595" target="_blank">📅 12:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142594">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال: تهران عملاً مسیر کشتی‌ها در هرمز را تعیین می‌کند
🔴
آنچه امروز در تنگه هرمز دیده می‌شود، بیش از آنکه نشانه موفقیت محاصره آمریکا باشد، محدودیت قدرت واشنگتن در برابر توان ایران برای مختل‌کردن یکی از حیاتی‌ترین شریان‌های جهان را نشان می‌دهد.
🔴
بر اساس این گزارش، ایران عملاً بر مسیر عبور کشتی‌ها اثر گذاشته و آمریکا میان پاسخ نظامی و خطر گسترش جنگ گرفتار شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142594" target="_blank">📅 12:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142593">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
خوش‌چشم تحلیلگر صداسیما: باید آب‌های فلوریدا رو با مین‌های هوشمند مین‌گذاری کنیم؛ این کار می‌تونه یک حواس‌پرتی استراتژیک بزرگ برای آمریکا ایجاد کنه و واشنگتن رو مجبور کنه بخشی از تمرکز و توان نظامی خودش رو از خاورمیانه به سمت سواحل خودش منتقل کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/142593" target="_blank">📅 12:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142592">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
مدیر شرکت ملی پخش فرآورده‌های نفتی منطقه کرمان از افزایش سهمیه بنزین کارت سوخت شخصی شهروندان استان به ۱۶۰ لیتر از ابتدای شهریورماه خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/142592" target="_blank">📅 12:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142591">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
فارس: ۷.۵ میلیارد دلار ارز نفتی مرتبط با فروش ۴ ماه اول سال در اختیار بانک مرکزی قرار گرفت
🔴
فروش نفت کشور در ۴ ماه اول سال همه مخارج ارزی دولت تا دی‌ماه را پشتیبانی می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142591" target="_blank">📅 12:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142590">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
اکبر رنجبرزاده، عضو کمیسیون صنایع و معادن مجلس: آتش‌بس پس از جنگ‌های اخیر فرصتی طلایی برای بازسازی و نوسازی تجهیزات نظامی بود و اکنون توان دفاعی جمهوری اسلامی به مراتب بالاتر از زمان جنگ ۱۲ روزه شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/142590" target="_blank">📅 12:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142589">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRJQWZMu5HOjodIwHKEkIxMM8vYxL1wLHRYES4jiyG62V48FpBtTap6gpQJqoat6cdYEcqh1CDMsrKz6COYeuygS5Dn-H6C3Igf0MeOubL5SHhoH34_bU_NoWeG1Dzspl8YJ-I_EsyVZgbvU3KoTLZJChf414-kZ3DfwnRZiRYdoFdscu2ok-7EwoZb2UjnOuH8JbTfd8tMjjPAZL6SHXAp7O9Td8SDtdCWbENKpcUTA42lAKa7NNCR7fvsinWB6eFOiCgDSnRPnuXU8b6zVsE7CiolHMHamgSbjOEAEZrjc-Jtce4NGHG1QST4i7IbbxdkKQ2l9PWiaQI1XlEjSZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زاکانی: مردم عزیزمون بالاخره طعم ناب مدیریت انقلابی را خواهند چشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/142589" target="_blank">📅 12:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142588">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">طلای آنلاین نخرید
⁉️
حتما اینجا چک کنید
👇
https://t.me/+S8mMBRHkHmFiMTFk
https://t.me/+S8mMBRHkHmFiMTFk</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/142588" target="_blank">📅 12:11 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142587">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sk0w2U7fHil29SiTrf1Us5atCzlyFh9cnO4oj_kmomOfUbuMG5tN6aywjsKO6GJpT7r7C5BZD_v7hP-AfVlxCLSyzxnnn0W83pvtopV1hQEhdzfkcqegY_v1DFUlj7iHlhVel8mnkT8sxeG9FhRd4CiU6O9cRljGI3dh37jmMVoqlECrNXUJ-wLoXWG4qMLuJxma7p1CWAnAMbHXAbouYiyDviC9w7rHqGgdEJng7ZHlWdGKj7Azq7n_1BvC5fcELR1NpgCqCMUGM1mgP0D8PYRZZFWstbFSriZ4HIhO1gvAxb5ieTytrOl6QgHzt_IVuEXNRgEMBDPR2wIoXySsCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار رئیس ستاد کل نیروهای مسلح: هرگونه کمک و تسهیل‌گری به آمریکا به منزله مشارکت با نیروهای نظامی آمریکاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142587" target="_blank">📅 12:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142586">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
وزارت دفاع امارات: هدف حملات موشکی امروز شناورهای دریایی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/142586" target="_blank">📅 12:05 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142585">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سازمان سنجش: در کنکور امسال ۶۵ درصد خانم‌ها و ۳۵ درصد آقایان شرکت کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142585" target="_blank">📅 12:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142584">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2IUPFlgSMN5va3OT4trWmeaOTMRAqUPyi9hQ2BfyKHr0P6qlukS8BUyfZSPF5meQDo6N-xvc6Nac3H629AuBwQznCGfj4nDZ8x2GRJ2gHOa-zVNkCzCqahApS_PW6rh8Cne5SRVvAtYJvhXDLFBmmx7oKoRSEbcstgIUa92_O3wwjrIeqqbzct1xtz-oNjvVTR-4-YiBea0YiF2OLFlagoU3t1pPfzXa2EfBT3fPupDxlmol2DUFlieiXRB_ZqSwQVt-RsgOwDLz3ZyZiTxrtgDMvt-eirIvQa8FlErKUBl-3odMP3A2t79jWQvG_AEqcxmNdUwPwK_xcfQLhLjPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آنژی نیکسون، نماینده مجلس ایالت فلوریدا، فعال سابق اتحادیه‌ها و عضو سازمان سوسیالیست‌های دموکراتیک آمریکا، با یک پیروزی غیرمنتظره، در انتخابات مقدماتی سنای ایالات متحده از حزب دموکرات در فلوریدا، به پیروزی رسید.
🔴
او الکساندر ویندمن را شکست داد، در حالی که هزینه کمپین او تقریباً ۱۷ برابر کمتر از رقیبش بود. اکنون او در ماه نوامبر با اشلی مودی، نماینده فعلی جمهوری‌خواه، رقابت خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142584" target="_blank">📅 11:56 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142583">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏
👈
مرگ ۱۸ زن موتورسوار در اصفهان در ۴ ماه
‏
🔴
فرمانده انتظامی استان اصفهان از جان باختن ۱۸زن موتورسیکلت‌ سوار در حوادث رانندگی ۴ ماهه امسال خبر داد.
‏
🔴
بر اساس قانون،هیچ یک از شرکت های بیمه، متهعد به پرداخت خسارت مالی و جانی به موتورسوران بدون گواهینامه نیستند و به محض وقوع حادثه، موتورسیکلت متخلفان توسط پلیس توقیف می شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142583" target="_blank">📅 11:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142582">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
جروزالم پست: تام باراک، فرستاده آمریکا، هشدار داد که حمله هوایی اسرائیل به پایگاه هوایی ابوالظهور در نزدیکی ادلب در سوریه می‌توانست به تشدید تنش و رویارویی نظامی مستقیم، احتمالاً با ترکیه، منجر شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142582" target="_blank">📅 11:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142581">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
شبکه CNN به نقل از مقامات ارشد کاخ سفید: در روز های آینده تحریم های بی سابقه و بسیار شدیدی علیه ایران اعمال خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142581" target="_blank">📅 11:28 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142580">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
رئیس سازمان سنجش: از عضویت در کانال‌های خرید و فروش سؤالات کنکور خودداری کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142580" target="_blank">📅 11:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142579">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cee250a30.mp4?token=TC1ZP9GIs6ySFwCjRT8AVJIaHiwrHYag0vY3tDwhARBfF2deKsrh5SU2WMqdJNrWJXwVhhMa3YmRiNZm8YXy0pIodWRC8PCBaipYJjplkpZNBFQPCHbZbfZ-WB0avlERyGobpIk4ng_TkRe3QcW79j7GuWxdrHR53mDtivc3wpomgjAKCpDXZ0qeLwZLZz2LYlhid-m_Il5a27_cPW7mSz6x6GKDNheUdSR5Zx7BCI0DyUd1RBkBBqK35odOKl784geO6Pt7ws4zttp0u8j-Waptc-4LOiftgD7_Ohvzl1AprGnP94g2zYRvws7WXXtKulI0XncUGEogM2Md8yOD7gQhIAOeqQAP60qs0SDcS48cTnQJUNaQjg6GrYJCl8v8VsSxQacjPlHlnrqLh_SlMBQK5OUPqJ148O2X-hHYcg3vblPpLiBNhZ2NU1BWxbz7wf0asHNAi3WxItGpGIwsYv2Fd7ZgFQW5mqime95UmJs6ILIvRpqtt95RxzTFm5CxUPoTDTfzuJugkGqdqczxPzFQWqK46qWdoQS2QL7vw65rQ5uM75KzWfEprXj_7eYxcOI1nofVWLAhSSBQmxeRdv_CJCYASxX_qR1S1DTktos9Be-elQYL3Nbqb-g8YhGSIABBobiZizHxWpBOjqXru-4wWzhY2kdAIVJNHjCj0kc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cee250a30.mp4?token=TC1ZP9GIs6ySFwCjRT8AVJIaHiwrHYag0vY3tDwhARBfF2deKsrh5SU2WMqdJNrWJXwVhhMa3YmRiNZm8YXy0pIodWRC8PCBaipYJjplkpZNBFQPCHbZbfZ-WB0avlERyGobpIk4ng_TkRe3QcW79j7GuWxdrHR53mDtivc3wpomgjAKCpDXZ0qeLwZLZz2LYlhid-m_Il5a27_cPW7mSz6x6GKDNheUdSR5Zx7BCI0DyUd1RBkBBqK35odOKl784geO6Pt7ws4zttp0u8j-Waptc-4LOiftgD7_Ohvzl1AprGnP94g2zYRvws7WXXtKulI0XncUGEogM2Md8yOD7gQhIAOeqQAP60qs0SDcS48cTnQJUNaQjg6GrYJCl8v8VsSxQacjPlHlnrqLh_SlMBQK5OUPqJ148O2X-hHYcg3vblPpLiBNhZ2NU1BWxbz7wf0asHNAi3WxItGpGIwsYv2Fd7ZgFQW5mqime95UmJs6ILIvRpqtt95RxzTFm5CxUPoTDTfzuJugkGqdqczxPzFQWqK46qWdoQS2QL7vw65rQ5uM75KzWfEprXj_7eYxcOI1nofVWLAhSSBQmxeRdv_CJCYASxX_qR1S1DTktos9Be-elQYL3Nbqb-g8YhGSIABBobiZizHxWpBOjqXru-4wWzhY2kdAIVJNHjCj0kc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سموتریچ، وزیر مالی اسرائیل، درباره طرح ترامپ برای غزه: ما هرگز این توافق 20 ماده‌ای را در یک تصمیم دولتی تصویب نکردیم.
🔴
در این طرح، اشاره‌ای به مسیری برای ایجاد یک کشور فلسطینی شده است، که به نظر من فاجعه‌بار خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142579" target="_blank">📅 11:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142578">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۶ امروز وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142578" target="_blank">📅 11:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142577">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏
👈
تحلیل الجزیره: این ترامپ نیست که مانع عبور کشتی‌ها از تنگه هرمز می‌شود، بلکه شرکت‌های بیمه این کار را خواهند کرد
‏
🔴
تا زمانی که تهدید فیزیکی علیه تردد دریایی وجود داشته باشد، این شرکت‌ها از قدرت مالی خود برای جلوگیری از عبور کشتی‌ها استفاده خواهند کرد
‏
🔴
بدون تضمین‌های قاطع مبنی بر اینکه کشتی‌ها از حملات ایران در امان خواهند بود، مالکان حاضر نمی‌شوند که در تنگه تردد کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142577" target="_blank">📅 11:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142576">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وزیر خارجه کره جنوبی: پیام ترامپ که در آن دستور کاهش رزمایش‌های نظامی مشترک داده شده بود، حاوی فشار بر ما جهت مشارکت در جنگ علیه ایران است
🔴
چو هیون، وزیر خارجه کره جنوبی، گفت پیام دونالد ترامپ، رئیس‌جمهور آمریکا، که در آن دستور کاهش رزمایش‌های نظامی مشترک داده شده بود، به نظر می‌رسید حاوی فشاری بر سئول برای مشارکت در جنگ علیه ایران باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142576" target="_blank">📅 11:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142575">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سی‌ان‌ان: ایران بخش قابل توجهی از کنترل بر تنگه هرمز را از دست داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/142575" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142574">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏
👈
انتصابات جدید در قوه قضاییه
‏
🔴
ناصر عتباتی رئیس کل دادگستری استان آذربایجان غربی به عنوان رئیس کل دادگستری استان تهران
‏
🔴
ذبیح الله خداییان رئیس سازمان بازرسی کل کشور به عنوان رئیس حوزه ریاست قوه قضاییه
‏
🔴
سیدعلی کاظمی رئیس پژوهشگاه قوه قضاییه با حفظ سمت به عنوان سخنگوی قوه قضاییه
‏
🔴
اصغر جهانگیر معاون اجتماعی و پیشگیری از وقوع جرم قوه قضاییه به عنوان رئیس سازمان بازرسی کل کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/142574" target="_blank">📅 11:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142573">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
گزارش ها از هدف قرار گرفتن یک فروند کشتی در تنگه باب‌المندب
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/142573" target="_blank">📅 10:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142572">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
الجزیره به نقل از منبع دیپلماتیک سوری:
رد وجود هر گونه توافق امنیتی میان سوریه و اسرائیل؛ ادعا‌های تل‌آویو در این زمینه نادرست است
🔴
دمشق نمی‌تواند وارد توافقی شود که مانع ساخت نهاد‌های غیر نظامی و نظامی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142572" target="_blank">📅 10:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142571">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
آکسیوس گزارش داده حمله اسرائیل به پایگاه هوایی «ابوالظهور» در سوریه، نارضایتی مقام‌های ارشد آمریکایی را به‌دنبال داشته و شکاف میان دولت ترامپ و نتانیاهو را آشکارتر کرده است.
🔴
برخی مقام‌های آمریکایی معتقدند این حمله ممکن است تا حدی تحت تأثیر انتخابات پیش‌روی تل‌آویو در ماه اکتبر بوده باشد؛ آن هم در شرایطی که دمشق در تلاش برای ایجاد سازوکار هماهنگی مورد حمایت آمریکا با اسرائیل بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/142571" target="_blank">📅 10:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142570">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
کانال ۱۲ (عبری): پروازها بین تل‌آویو و مراکش، پس از سه سال وقفه، امروز از سر گرفته می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/142570" target="_blank">📅 10:36 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142569">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سرلشکر عبداللّهی رئیس ستاد کل نیروهای مسلح : کشور های عربی حاشیه خلیج فارس مراقب رفتارشان و استقرار نیروهای آمریکایی در خاک کشورشان باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142569" target="_blank">📅 10:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142568">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
فاکس نیوز به نقل از مقام وزارت جنگ آمریکا: ترامپ بودجه‌ای بیش از یک تریلیون دلار پیشنهاد کرده، زیرا بازسازی ارتش هزینه‌های زیادی دارد
🔴
مدت قرارداد‌های خرید تسلیحات را از ۵ به ۷ سال افزایش داده‌ایم تا امکان بالا رفتن تولید کارخانه‌ها فراهم شود
🔴
طی این ۷ سال، ۱۴ هزار سامانه پاتریوت تولید خواهد شد
🔴
در حال مذاکره با شرکت‌های جدید برای انعقاد قرارداد‌های تولید موشک‌های کروز کم هزینه هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142568" target="_blank">📅 10:29 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142567">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
وال‌استریت ژورنال: ترامپ در دیدار احتمالی با کیم جونگ اون در ماه نوامبر، می‌خواهد اون را برای دست کشیدن از برنامه هسته‌ای کشورش متقاعد کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142567" target="_blank">📅 10:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142566">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfe76fe9dc.mp4?token=CJL7E5HETmXaFCilNA6DA8WS33xYdFSCk4LZUm0bYnhhmgAN-En3lwYvKyRFI21fvO_INovuuTUQXnq9-49sSs5NNiXjSR6hNX3rgWgm2giZatqNGaTEk66zaenSQ3-MvwXZoEXhqBy7fRiWI0cnZ0cR-qlot1zlAMpcagn6a4yfKu5ODdwwtMeiOFYKkweJpD34fOPJw_bWgSNrJu5XAgAvY4Uz09rGgflTWWjZQPZ94VmcZCaLxzb-1MuGadZ_OjqFWYbPNqdoM0qvheANuFBMjws__MkCPTt-ccIxH9URFKDowR8_4KIxkIeskzdzuJ6BWwbBUJ3xdUqQL8Gf-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfe76fe9dc.mp4?token=CJL7E5HETmXaFCilNA6DA8WS33xYdFSCk4LZUm0bYnhhmgAN-En3lwYvKyRFI21fvO_INovuuTUQXnq9-49sSs5NNiXjSR6hNX3rgWgm2giZatqNGaTEk66zaenSQ3-MvwXZoEXhqBy7fRiWI0cnZ0cR-qlot1zlAMpcagn6a4yfKu5ODdwwtMeiOFYKkweJpD34fOPJw_bWgSNrJu5XAgAvY4Uz09rGgflTWWjZQPZ94VmcZCaLxzb-1MuGadZ_OjqFWYbPNqdoM0qvheANuFBMjws__MkCPTt-ccIxH9URFKDowR8_4KIxkIeskzdzuJ6BWwbBUJ3xdUqQL8Gf-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
یوسفی نماینده مجلس: دلیل مصرف 130 میلیون لیتر بنزین در روز، کیفیت پایین خودروی داخلی حتی مدل صفر آن است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/142566" target="_blank">📅 10:16 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142565">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
شاخص کل بورس تهران در دقایق ابتدایی معاملات امروز با افت ۸۰ هزار واحدی به رقم ۵ میلیون و ۸۶۶ هزار واحد کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142565" target="_blank">📅 10:12 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142564">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d1f7c464.mp4?token=HwBZB0mlGd00pvacVBkjGozoLhs1tEKxvuEWMKqNoealUY9ei6ciQILDzD7ErzcmBOvPsjWKR-ngybkDDaztWCR1AvJuvo4AKAaZQfPRDFiSkUedhJ9QBbOny7ojgR4W0YQKCFX66kFJ4D_4YQyQqbe6sS85Lwqa9U_eKGGgDgNRjtBlD60TNlPW5XboBAH6wT5fiXu2GAHVaVJE9JCoGj9v-xUKcjXEbdgp0vV-remRT69xHUPN3JN9xyc-4VYQoTrHvq6HQkf_eHkGnDIXQeKy68VZYcJZUTgTdXdlIfUh16U2kYBCvIENfDHLuX1QPVisRygUUQCSqppOBBFTJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d1f7c464.mp4?token=HwBZB0mlGd00pvacVBkjGozoLhs1tEKxvuEWMKqNoealUY9ei6ciQILDzD7ErzcmBOvPsjWKR-ngybkDDaztWCR1AvJuvo4AKAaZQfPRDFiSkUedhJ9QBbOny7ojgR4W0YQKCFX66kFJ4D_4YQyQqbe6sS85Lwqa9U_eKGGgDgNRjtBlD60TNlPW5XboBAH6wT5fiXu2GAHVaVJE9JCoGj9v-xUKcjXEbdgp0vV-remRT69xHUPN3JN9xyc-4VYQoTrHvq6HQkf_eHkGnDIXQeKy68VZYcJZUTgTdXdlIfUh16U2kYBCvIENfDHLuX1QPVisRygUUQCSqppOBBFTJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برخورد موشک اسپیس‌ایکس با ماه گودال ۱۸ متری ایجاد کرد
🔴
تصاویر ناسا وجود گودالی به قطر حدود ۱۸ متر روی سطح ماه را نشان می‌دهد که گفته می‌شود در پی برخورد بخشی از موشک فالکون ۹ متعلق به شرکت اسپیس‌ایکس با سطح ماه ایجاد شده است.
🔴
این موشک در ژانویه ۲۰۲۵ با هدف انتقال کاوشگر «بلو گوست» و ایستگاه «ریزیلیِنس» به فضا پرتاب شد، اما مرحله دوم آن به دلیل کمبود سوخت نتوانست به زمین بازگردد.
🔴
مرحله دوم موشک در نهایت با سرعتی حدود 9 هزار کیلومتر بر ساعت با سطح ماه برخورد کرد و گودالی به قطر حدود ۱۸ متر بر جای گذاشت. تصاویر ناسا این عارضه را پس از برخورد ثبت کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/142564" target="_blank">📅 10:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142563">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4t1OYzSmbH-aIPDSs3bQOEKgn-xw6eF8Om0v5uh3c6z43Vm0idV6feIr0wZWce3uzLNf4BlSYaiI5Oqj-3-JaLrGNPpiGZSLncCjMxQCsU-Rh6u4unRb7Z-4qK2fu18ep7G74j2SnfntYoeWAY7ugXkFfpdnj-usrSDrkgCOf81UH_kHrfCqWzR3FLlMUa7Ico5PSCfyLfFivPHStiAcyvEjyc4OMedDqh69NwVsyLKe24iNZK4nXypMLW9v_SU7jNjOfD23E-FwK1jHLTsMS8BI_fYlD5fsO0cTjrDBIKX0OBNNpfYvCbcZU781RFOA_vF_A3wDEoY8HDoFnpuHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکس رنگی شده، از شیراز؛ سال ۱۹۱۱ میلادی، هم‌زمان با پادشاهی احمدشاه قاجار
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/142563" target="_blank">📅 10:00 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142562">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d4b1d33fe.mp4?token=eUe9s-x0AavWmnotdRYXh8YK2lAojtTQxjzBZUmlTP9M3MKKjrHFlDh-BHm5h7o26yUEk59FjT3kkOaY1zIh_7edbUCIB7egs0mhAzyL3tUBzTXEdauxUdvu4mvAxHuwVUp_gRl4DvtUBaG37CJSdY541Tp1rcwbT4e0NXZhD4JcN_jl3Sx_sFznmrDstGCLfN3AlITeAcX5lkVoH6IlA8sW4gI9kVrS-AM1xxTiT1qSyn2OMksf4NZ9vqMk9yHJ9MLeI-wN0zL9PbVlAlDZyUIivZwxzU0gwmqfU7-cxZivcjZX8MgbFgBpKkTr8sSucp7ZbmX2UTykbMMNQZpaLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d4b1d33fe.mp4?token=eUe9s-x0AavWmnotdRYXh8YK2lAojtTQxjzBZUmlTP9M3MKKjrHFlDh-BHm5h7o26yUEk59FjT3kkOaY1zIh_7edbUCIB7egs0mhAzyL3tUBzTXEdauxUdvu4mvAxHuwVUp_gRl4DvtUBaG37CJSdY541Tp1rcwbT4e0NXZhD4JcN_jl3Sx_sFznmrDstGCLfN3AlITeAcX5lkVoH6IlA8sW4gI9kVrS-AM1xxTiT1qSyn2OMksf4NZ9vqMk9yHJ9MLeI-wN0zL9PbVlAlDZyUIivZwxzU0gwmqfU7-cxZivcjZX8MgbFgBpKkTr8sSucp7ZbmX2UTykbMMNQZpaLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک شرکت چینی از ربات انسان‌نمای پرسرعت «سوپرمن» رونمایی کرده که می‌تواند ۲ متر به‌صورت ایستاده بپرد و به سرعت ۱۲.۶۶ متر بر ثانیه، معادل حدود ۴۵ کیلومتر بر ساعت، برسد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/142562" target="_blank">📅 09:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142561">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4b5a92c64.mp4?token=bT02B86t_om2bxT9VcT-R3D3zAMXgwnNmLNT3NG53wseRNOhsZM-HUcJQDG60MtYurxsVzaKySiVV29BuGMJK4Fo1Pp-9lVkqN1n5-7oRgZebVfUpTYuuhoJM3gajAmG4mJhND75Q8V9AVGaHELSnyyR7_0A9yRVtP4jTRqoOTalHO0o0HhRysq2UtXnNbf63diLvBGt6nT4_hFU6_otKnsiKmZ4isWrJZanCC1bros35SJx7aUQQyzz710uTsp1gwAcQYBfJ49PHescQLr8_facHtE86fbyTSSssiv5mrIaR8jrMXyfGv09QhmmuKkH3XhiG8__wV2sutKOqIn4Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4b5a92c64.mp4?token=bT02B86t_om2bxT9VcT-R3D3zAMXgwnNmLNT3NG53wseRNOhsZM-HUcJQDG60MtYurxsVzaKySiVV29BuGMJK4Fo1Pp-9lVkqN1n5-7oRgZebVfUpTYuuhoJM3gajAmG4mJhND75Q8V9AVGaHELSnyyR7_0A9yRVtP4jTRqoOTalHO0o0HhRysq2UtXnNbf63diLvBGt6nT4_hFU6_otKnsiKmZ4isWrJZanCC1bros35SJx7aUQQyzz710uTsp1gwAcQYBfJ49PHescQLr8_facHtE86fbyTSSssiv5mrIaR8jrMXyfGv09QhmmuKkH3XhiG8__wV2sutKOqIn4Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای، آلودگی آب را در نزدیکی سواحل عمان نشان می‌دهند. این آلودگی ناشی از نشت نفت از یک نفتکش حامل حدود یک میلیون بشکه نفت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/142561" target="_blank">📅 09:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142560">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
فایننشال تایمز: ایران در حال بررسی این گزینه است که در صورت تشدید جنگ توسط ترامپ، به اهداف نظامی آمریکا در اروپا حمله کند.
🔴
منابعی که به حکومت نزدیک هستند، مدعی‌اند که نیروهای ایرانی در حال ارزیابی امکان حمله به تاسیسات در کشورهای جنوب شرقی مانند بلغارستان هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/142560" target="_blank">📅 09:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142559">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0wlpcZoeBmeUG5RfzYHL0RJRMDfKCeDqaskdjelPr0L-iSzWY38BZ2Ss3ORw-Cz29vXq6nAjATT-oiSXKWwbfFYy-H3ZrXZ3ESOmMkISfNDJq8_UC0ddBvMHOxfR5IyQvUuiPpAAnHew_2UltxOb9yxsUEW1nvHIckrsEPMOPVy6cIpkkeaNRYLijszPIPGadP3xgE9ZZnm9eAaO9ViqXUw6Od2-LtVn2LaOK4qpTOjiomODv_4lJ16Epdwa-t-68KUoro-mQRWB2c8_zSFv5Qj1BMCcs-UkmNwxSTyB3atI8XDKelNE1IzLlgjGajgM7bmBsoYzMDi2HacZsSjqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: تعرفه‌های ۵۰ درصدی علیه کانادا را که قرار بود فردا صبح اجرا شود، برای سه روز به حالت تعلیق درآوردم، چون کانادا و آمریکا با نهایی شدن اسناد، به توافق رسیده‌اند!
🔴
خط لوله بزرگ کی‌استون ایکس‌ال که سال‌ها پیش توسط جو بایدن خواب‌آلود کشته شد، شاید دوباره از قبر زنده شود! از توجه شما به این موضوع متشکرم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/142559" target="_blank">📅 09:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142558">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Th7iyfQbTALKYxuD1lBRYGNkVVxEtT5tmzYdcbErGomrogtdmfLP8pGvnvBLEp9KiqLI09rPYfdrX4jAsoqJhpqPyd4FukNT3INuQAq_WnlaWaZUe6mhe-3ZGYQUBED4C3kGYHsxlLk0bPczbANLd5av1AaVK7RL3OOscTbxfvIyL8sL47XYZXegfg6cgcR28n5IGRBRaV-CvHUOV3I7yJxfTIFiTEbr8LLGOjRObAn4SDYV4Nsut7qOsUq7dL4tuYbhFFEvbJ9KXtxpXn7icf966TYl6oEaMAa308529dQuBoclq8xxp4hPDmQPKdFcEQzKdsacWrtvrkmBizAPYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف وارد بغداد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/142558" target="_blank">📅 09:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142557">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec90dc737.mp4?token=ZUff5dRQdBAsqMSRm0cuHDWH2QQeuho34x7458dZkuVHgUi9Mc39i8Bg67yy-dS1IHWZH42ZcoD0avQjv2JTwG0amGHEfBNl51Csa2wOca5zCe1fcs_0oPN4garUW2dG0wKnzIu0UH8vXjhvLZ-cl6wDcMbk5NvIVRp6vIv9IS0WejdoebaKnFXzV-eGzbF8l_P4ydAkcyYpap7vbP4P5Dkl4bfs7LMSedkt-APbyg8Eu8QHVPUklFBsUMFnPwYwlq-gcQRbwxPwwo_mcmwlv4ni1QJ4A5owPWJSAg3xohe4zTRCvht_hhwVJv3vNScEsfpjH_rLF30gTlRRifD7sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec90dc737.mp4?token=ZUff5dRQdBAsqMSRm0cuHDWH2QQeuho34x7458dZkuVHgUi9Mc39i8Bg67yy-dS1IHWZH42ZcoD0avQjv2JTwG0amGHEfBNl51Csa2wOca5zCe1fcs_0oPN4garUW2dG0wKnzIu0UH8vXjhvLZ-cl6wDcMbk5NvIVRp6vIv9IS0WejdoebaKnFXzV-eGzbF8l_P4ydAkcyYpap7vbP4P5Dkl4bfs7LMSedkt-APbyg8Eu8QHVPUklFBsUMFnPwYwlq-gcQRbwxPwwo_mcmwlv4ni1QJ4A5owPWJSAg3xohe4zTRCvht_hhwVJv3vNScEsfpjH_rLF30gTlRRifD7sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواشناسی: به نظر می‌رسد از جمعه به‌بعد تهران دمای ۳۸ درجه به خود نبیند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142557" target="_blank">📅 09:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142556">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
قالیباف پیش از سفر به عراق: روابط دوجانبه بغداد و تهران در تحولات منطقه، بسیار مهم و اساسی است
🔴
سفر مذکور با توجه به اینکه بعد از پیروزی ایران در جنگ ۴۰ روزه انجام می‌شود، خیلی اهمیت دارد
🔴
بدون شک ما در آینده منطقه شاهد نظم جدیدی خواهیم بود
🔴
این سفر می‌تواند زمینه‌ساز نگاه و فرصتی که پیش روی ماست، باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142556" target="_blank">📅 09:14 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142555">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
یک مقام آمریکایی به "اکسیوس" گفت:
دولت ترامپ از سوریه خواسته است که پس از حملات هوایی اسرائیل، خویشتن‌داری نشان دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/142555" target="_blank">📅 09:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-142554">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
سفیر ایران در روسیه: اوکراین هنوز بابت حمله به کشتی ایرانی در دریای خزر، غرامت پرداخت نکرده
🔴
تهران و کی‌یف در حال حاضر درباره پرداخت غرامت مذاکره می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/142554" target="_blank">📅 09:03 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
