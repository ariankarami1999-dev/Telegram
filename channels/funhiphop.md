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
<img src="https://cdn4.telesco.pe/file/v0hZe25SdQvc3ExeX_cQFDLjjvyMlVkRW2xuD-QpV3MtXfPZbZITGBOb2WUTfYSP8hrevWFyn13F174I0xRwqOsx-9nzUCsfuyJoSuW6_RJvzErUdRbSYgRyvTRKqyapulg-f7lskrOZhE1mxcNw3Tuo0qqkDuboQrY2ircj6nfqSI33p91q5JlwuTiDVSjiGUERQHY1JgEJQ9pIhfmNu_3pGRV_vqAsYKem4GUB-SXJdA4LWZL5-JsHgJvEDRr0wwsFk_DJfQO45-kIvT7Ov5kzrLt11figKT9A5tyqCnbEQC39QQ_VarzSL9bQxkvl1Y7RMYlHydyYGkiy9ToOhA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 244K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 18:02:50</div>
<hr>

<div class="tg-post" id="msg-83611">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/913c6eb0b8.mp4?token=ocyCjYBHDDKV5I7WUaEFRCTnkHRkVZ_CHUgSPQlYTAWT5I-l_cYMz9GZH6Ys0KiLLmkBtmVT1f8CdhU_OY-O-D3Zu3mrjpeIF3y9WjvzuycmY0R_Pa4d6YVOwcSi43kDWizozL9sxa4_G-Gd4mVM4pSCmFoick3FAttvdaj_8GJw1o7A9u-U2aZqjXV6f6Nrn-Qiaz74NmFdLu3tmdI3hf31b5KeyTCrgb8zEHnrpupEKEgv7wu5a9O_0Zlj2vcZqgF6_CDyQRMUpemLl95Q2XjCS3RMRTOARJ2MTds8PaFo1UF3jGEIK_E5I1xXemcVG_W6Ee5CXJD7rFiDAKNujg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/913c6eb0b8.mp4?token=ocyCjYBHDDKV5I7WUaEFRCTnkHRkVZ_CHUgSPQlYTAWT5I-l_cYMz9GZH6Ys0KiLLmkBtmVT1f8CdhU_OY-O-D3Zu3mrjpeIF3y9WjvzuycmY0R_Pa4d6YVOwcSi43kDWizozL9sxa4_G-Gd4mVM4pSCmFoick3FAttvdaj_8GJw1o7A9u-U2aZqjXV6f6Nrn-Qiaz74NmFdLu3tmdI3hf31b5KeyTCrgb8zEHnrpupEKEgv7wu5a9O_0Zlj2vcZqgF6_CDyQRMUpemLl95Q2XjCS3RMRTOARJ2MTds8PaFo1UF3jGEIK_E5I1xXemcVG_W6Ee5CXJD7rFiDAKNujg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشکل ژنتیکیه فکر کنم حاجی زود قضاوت کردیم
پ‌ن: داداش علی گرامیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/funhiphop/83611" target="_blank">📅 17:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83610">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مالکیت و مدیریت باشگاه چلسی به یک تاجر ایرانی الاصل به نام بهداد اقبالی انتقال یافت  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/funhiphop/83610" target="_blank">📅 17:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83608">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مالکیت و مدیریت باشگاه چلسی به یک تاجر ایرانی الاصل به نام بهداد اقبالی انتقال یافت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/funhiphop/83608" target="_blank">📅 17:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83607">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tITBcwkphnLq5lfxbOpt9cs_DEBN1ZLfCfPgGzYv9q2DhdDJIqbPSxJU7oyu4KXoCuXwzYdX9Hf7J9M7yjCmkYHMAXybF2OVPt2f3F32FdEsfaq2a5cM7uocdMNcASyw3BCiOZfxb2v2GqvyrVhxMKy5pwBlEESVLtbg40egTMTgRlBkbqmK_qNnxjNWUPOK_j3W5XLDY4C6ZMxiKbmLsNxu2QksV_WCrzjdmc_vMTCiza5vYhcvNWFOC_PpWDTyycl0yCgDg1Mblg5rimUkBLuu-1Q0-bmIvLBTn9oNV0jBegJsTECUes1gF_tHeq4AAFOu7GS4e41VEGmE0tZi0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewReleased
🆕
🗣
Artist: Young Lean & Metro Boomin & Future & Travis Scott & Mogan Wallen &…..
📋
Title: GTA VI
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/funhiphop/83607" target="_blank">📅 16:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83606">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">📶
منبع کانفیگ های رایگان
📶
🎁
هرروز کانفیگ رایگان میزارن
🎁
جوین شو عشق و حال کن
⬇️
⬇️
🕺
▶️
▶️
▶️
@SpookVPN
◀️
◀️
◀️
▶️
▶️
▶️
@SpookVPN
◀️
◀️
◀️</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/funhiphop/83606" target="_blank">📅 16:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83600">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8162c9ca6.mp4?token=e-0Bq6sy8AS3VYW6Y3A3EV0Sm3evGyULBRjjYZS1hHux84qJH48I6c4yNuyjorifrP_OLAWHLQ_LMONXJddMByQHkiG_O0ULSj0Ldc59T1quDaO-DNOCSD6q6E_uvn1TkGYsQluBw1yQOURSGP_ictVFKFKh9ny57sPIbie-W0wlGtuAPsVkml32Fk03_hhV3_ZmBU5Q8qS07fWXdMPKgSIBTXInNM_4H2cBncFxFqNFcXe3ZVb6FC7xy1yQfZTlMIig1IetT1398bb-eYVsa23075e3DP0Ah0XrITGyIb0bdE8gz0tQCU-quvUYrbkve5gkUsBMd0Soy2eNzShaBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8162c9ca6.mp4?token=e-0Bq6sy8AS3VYW6Y3A3EV0Sm3evGyULBRjjYZS1hHux84qJH48I6c4yNuyjorifrP_OLAWHLQ_LMONXJddMByQHkiG_O0ULSj0Ldc59T1quDaO-DNOCSD6q6E_uvn1TkGYsQluBw1yQOURSGP_ictVFKFKh9ny57sPIbie-W0wlGtuAPsVkml32Fk03_hhV3_ZmBU5Q8qS07fWXdMPKgSIBTXInNM_4H2cBncFxFqNFcXe3ZVb6FC7xy1yQfZTlMIig1IetT1398bb-eYVsa23075e3DP0Ah0XrITGyIb0bdE8gz0tQCU-quvUYrbkve5gkUsBMd0Soy2eNzShaBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسنوپ داگو بردن عروسی براش سامی بیگی گذاشتن  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/funhiphop/83600" target="_blank">📅 15:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83599">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa121b5449.mp4?token=AQo1FaBnVUdZ2uYU_q3FrDxGXV46N-4T0Ft6yCFCaPY1aTKWol_QgQeJCkXi5YXrwHm2W8yclf9mYxvkD4jtclOq2yqVl7pAm4Z5BdErKvcbwdGA7PJdB42eUagy0hDV4bCk3bsiAuLWDtYcRlVvGEbOg5nMSDFAswzNElz2JNzJAK1CN_4_7FGsb--uE4BFDlLi8pXOqDFkQJ5DaUei_UqcjPf1lfWj83u8XvdGOYgXqvyqWSC2nkRX3CuAxczW1dUFwiAF7sst5nf54EqUDgXcqb7GNIyQSuiuTqm_vD5IrOzINLIJvZOkEKuyJvPYaLn6DwDaxqFv_Wlx_l6ZJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa121b5449.mp4?token=AQo1FaBnVUdZ2uYU_q3FrDxGXV46N-4T0Ft6yCFCaPY1aTKWol_QgQeJCkXi5YXrwHm2W8yclf9mYxvkD4jtclOq2yqVl7pAm4Z5BdErKvcbwdGA7PJdB42eUagy0hDV4bCk3bsiAuLWDtYcRlVvGEbOg5nMSDFAswzNElz2JNzJAK1CN_4_7FGsb--uE4BFDlLi8pXOqDFkQJ5DaUei_UqcjPf1lfWj83u8XvdGOYgXqvyqWSC2nkRX3CuAxczW1dUFwiAF7sst5nf54EqUDgXcqb7GNIyQSuiuTqm_vD5IrOzINLIJvZOkEKuyJvPYaLn6DwDaxqFv_Wlx_l6ZJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسنوپ داگو بردن عروسی براش سامی بیگی گذاشتن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/funhiphop/83599" target="_blank">📅 15:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83597">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eyIR0SdYgF92ReTZB_VpWBRnM1TDxPxLGqtZgfWmtqrTi3r6abruDJ0DmIPccN_MMKr61YhRavUjdlQKTk2HKjozcUotDxLzFWnQJuRQYeI5mDfH7Jko_CjLA5jH4PAuQUITUBMzqpC__QbMOQC__idehfte_TzihhWxowBrwkU_qhshNTE2bGfLVkimKicuXAye7lS9sot6rEouljkCArtrA7eyECx8iFvVh2Mk6J1BE_W9m6PaTebGiRvan6klI46sRPFZzlgp1Br_Y-Xui-KAfjOO_venWbWzVIiNNdfTiuKQOY2YpvsVIfzd4Ku_8CKUk1psJMkl3SKj_3IE2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ts2Qlnl8RD8n_EWMXVkhTg1hTdpywh0LD_2w5Ul2DAOC8T2IJQ7fy5GxnPA_MAJDbIFNrN7A6l2UaNJvxYhsbFxXzK3ik1RPg-b2K-lBo3-tiISz03tPsxc8k4e-LXi7eOD4fKu9XRodqJeHyIjZEV4AmrblxTUWxzGZcUnDVLgmuvFyq57uIpDeGvWCJvfwvJtFV063F4a1MF8ydCTzafHWlCig85PlV6gWF-0OBV-3_0-pnxkAmittZKUMSG0oTBeTQ3XEek1sqw_LqWzNYTfP8b3Qy5Vg7CgtI4Ksn3VhM1-Mhc7Prah1nrX-iZfvqsNGxmNWGq1cvx-Vtdkm_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استر و پارتنرش تو فیلم جدیدش کم مونده دیگه برا مارکتینگ فیلم جدیدشون پورن بدن ییرون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/83597" target="_blank">📅 12:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83596">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqh7XleFP8FZdDRKPFQSw31bb1P-R7yCgBESAgHRp8UBYQqpNtU9CgFT-ucyprUt8k-7fwYI7JqwsecNf-bpV2Wz_39ytdFK6MhVJ6ZjOX2SoehHlGmgc9e0PKKnMHK4QZ7sh4YmJ3bNeB3L_EgAUkpRojJ5c-hUCcqQQpnWHwUDKqyUVOrR2PTztGZYIQS16nFN3HBmJ_kg85EJCFhlCa6X3MAmCDnGMMPLLbUv04aNk0I_ynNxCxCYHMhhf362e_7y670GizUq5XE2CbwJRxkrm13s3e-M4yM_5YVV-tIqxRfYR62lSsXgQVPE8ZB7w7Q_h_BRlaAvQO87KE6QDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی رضا پیشرو از ویناک نپرسیده واقعا صورتی بود یا نه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/83596" target="_blank">📅 12:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83595">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNEcZmoTaXl8X1IWyty3D9IwbsiJAmQgmfHwrtg6Z0j4L6ITyZXCHqN8xcMP0cSNcB8lmg53PKJ6Jeq8OoRraF5ze54V8qYPQOohqXDuwiOC0Y8BpSdQDs5FNWEQXG8puiRMB8jiKwXc2hwT53tK9pYkvo4bvvEQeAJj5P96E0f59nl1Rr_9RR4TTMgwrQ_WwWx8c_4VR9HamS32JFoKmAt7SPvJ9wiLV6zWhWCizzIQh1ymJ3vZu76XS-2hZYUU3SeFeORvC0b4UZ_2oBHIyheLJBwNtiIjOLfsV2nhoBTvC6sagBRtfmPaMQcb8eF1T-Px4OHnInJyXpQhdY-iKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازیگر ترک پیشکسوت که قطعا بچگیاتون تو ماهواره دیدینش هم به جمع فوت فتیشا پیوست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/83595" target="_blank">📅 12:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83594">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Esd5bjyIhLZcZ1J_DJjH8YS2ybQCBWlFfDOKyElBm-CIRIt3rMzH2EMe6eNLC2gticYVZDKumbxRhMv3I9_RSTffHMWh8ue1HvVsqzUdaIneldytDxXcwLNH6hcqB8FHLzJfLmUYBInWjjZIff7te7fQf6nVCXqesx4YVka5-ZRjjrD5vWj3LuGngiSUneLgcmzFH5KE9JDvpKI1OrWKRoCoJooWB9n4VM7Zx8hLKiL8sdGe6bXmTCJG1CkZF6WjjFlthGwt727o_hV407PHsEg6Uqo2L-DkdC5jRH6HglSkljbhMvgWKvL5cyCoFSRtl1QyCB3qpbB6ugcKJ6rtXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
رئال سوسیداد - بورنموث
⏰
ساعت ۲۲:۳۰
🌎
📲
یوونتوس - ان ای سی نایمخن
😀
ساعت ۲۲:۳۰
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R26
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/83594" target="_blank">📅 12:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83593">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f8e0a26f.mp4?token=Q6sAgZRjZy-aVB37IuZAGQffxvaKbbqYyiIQ-QfcQ-qIN1f6n2TYZQ1pxfTMRfI_Q9Bv4IbMP9fmldOWbj80L0uzh4336vaHcCERsDfN4DIDxMeRC-H6lEwl2Pid4ChHkR4vKUz6JAg37keRWQzoNwLtBJhJmjfBuKJq2uW17BkgfKH-9j7gqMdcByDddxy707PBF_xOVCH5wI2meVt1iE8IxPW0Gnac2MQK9Qc5tvOoPlSluWyVAXxIfC-voM-KFa30YQGqBW_wKTG0WEISrFoRhN8sKmIrJHbGePRPgLapgNG4VB4fwt3XV6bq-Pbh7PKhbBMywI8NIGADGj03Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f8e0a26f.mp4?token=Q6sAgZRjZy-aVB37IuZAGQffxvaKbbqYyiIQ-QfcQ-qIN1f6n2TYZQ1pxfTMRfI_Q9Bv4IbMP9fmldOWbj80L0uzh4336vaHcCERsDfN4DIDxMeRC-H6lEwl2Pid4ChHkR4vKUz6JAg37keRWQzoNwLtBJhJmjfBuKJq2uW17BkgfKH-9j7gqMdcByDddxy707PBF_xOVCH5wI2meVt1iE8IxPW0Gnac2MQK9Qc5tvOoPlSluWyVAXxIfC-voM-KFa30YQGqBW_wKTG0WEISrFoRhN8sKmIrJHbGePRPgLapgNG4VB4fwt3XV6bq-Pbh7PKhbBMywI8NIGADGj03Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید بیگ شگی که رفته کنسرت ابی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/83593" target="_blank">📅 10:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83592">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCvZiUVmchn6YDDdPUpyQVJfmiyXO8nH9aF-zBfczUcXnpNtSHyFH1rvsA02PcFFbmPDymVt7vWM5WDGadVjBD4D6UuEPf-Xzw8AV9HsxZp9mavYTdQrH2jwIXLfVku9wJEOFYpWvx6dVpyn42qcgPpr784vX6g8naG3YYJMkkINBjjZOcXw6-YaQQWw9v9pYzsv_EwfIXC-kEez4uvOQEU0p9afAjvXs38oteq82EWcwEIt2sDvLdgdOcfX7_V5WZQTs3Fe8_hjAvMm5mk7e2C0sdu0Ic75-kdNGn1kF3URJXkfECFBYS2lkDNvL_vXqpkI_BnDimnCNS3tQ3uK5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا کریم؟
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/83592" target="_blank">📅 09:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83591">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">از باگ های تلگرام حامله ام
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/83591" target="_blank">📅 08:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83590">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">صبح دختر خانوم های عزیز بخیر، پسرا ایشالا بلند نمیشن از خواب.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/83590" target="_blank">📅 08:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83588">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QkDrhnx0WwRKxENMRZ1G8k3lgW3cp0RLg-nPw7mHZZmE59ikuPIeJLe9RsKBHYbIBMVq5zr-IkZJYvMsRJD62rilygoHiqK999G79KY5vZEUCdfNuNFy30yR5lbGWCeCWgjXVimI3TpD-IGMWpYSJlkY9d7sr_Mj6qfS-3e9Ltb9y-3koRhjVNzUoW6w5YhH2nh1oHDLhMZuJSHtkhRcqV9-YUC_EAezCjBQb1XH3lraZRzqVoqvNH7_fZnOkYG_Ku2nhL_Tw-gUntUu2TgQq8NrmZ3wIGieukRKrsg5JrJSx169lkwLeEDvZB_0T0ZHQHwKa7phoGscbwteTtkEHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a5F__3kuTumwcix85PjMVZpOsyKdIO8NnPJJgBpJsw08am6Y4z605AykI5n7n0PjyTRjiA2fNgsO2sGkg91R_vNGklk3xX5TP0PL1rFbeR3yVpDRN0jrcdb1_e5p6oCFT1eXR2Ywicf7Q6wAH4tIAIk8RkqRP1cJoLHcmkybSOt8ROG-rV1hTwe5MQbEEEBp1EUfBTBmxXmUqcN1PFkGTcJ-DVfN4EN-VdZJq3if6jX6zbyYP8o2VEcPO9L14Z4V2JMX3cikBBGpvUwGqjnuI4VwRSxT0nEVa13_capRLg6gSPGGCpDN06CsK92i29fERzUuV6AXGnMO-xlAoqi8Rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">علی ضیا و زیدش تو ایتالیا شکار شدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83588" target="_blank">📅 03:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83587">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ببینید دوستان من الان ۵ تومنو کردم ۶۰ تومن، ولی این تا نهایت یه هفته همش بگا میره چون تجربه همینو ثابت کرده، بت رو برا سرگرمی بزنید نه درامد زایی که بگا میرید  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83587" target="_blank">📅 01:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83586">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sv8Tv6wPxS4qfqI9d53lBHRZIiOEj0Ygb5jqSAkflMMHU2ZaPVCTN6-EJ1yQyj8funbTlqkxQ90m4_uMazmGqrj5yIOURbXtIGvPc5Sw3gyh1PaZ5XZU2rMHyls2rtEn5J7mZxyLTfxV_Rgh6O14ot0UZnk5CIlm4ik-pAH5wq7myAz592FWw4YkiNq_J44AtBcyBmWPpOBit3YKB58kGEEWYrzs7tonOBdPcQw-DpzDlYAwzC44AZ2IR947vSzKZ-ABRlkEJHnnZuJzbFoHgQr6gYx-S_A3hP0vh7CNfNgWE8Znsy2yhoiANA6kh6QOrrLECuzE3CXMZ-D7KB1cJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببینید دوستان من الان ۵ تومنو کردم ۶۰ تومن، ولی این تا نهایت یه هفته همش بگا میره چون تجربه همینو ثابت کرده، بت رو برا سرگرمی بزنید نه درامد زایی که بگا میرید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83586" target="_blank">📅 01:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83585">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f056dbed7e.mp4?token=JWKVSmG8K1IMIdycUqF7D5bxFiKutcuopWCEjQz0EgTX3eqYwv79gdZSe7i8gOeL9BGsnSqwm7XXdIPEq01kkfYgjpQQjguqyobh_b6FugpLNMT-sqKlEUpS3SRhNDVNYM82f-d5aDLu62ZWhprEiQOTGaZw2wClXomB7MSdljjGus2U31-W8t1FiaId-wywD4tS1uIY7lrlQoNgTfJtqoITzABmDkQsc1wT0jd1lxou8poUjUIPm5oKVw5S5saZciTvj9FbUZduWAOtj_jD8bOlpqJbVXJKsS6_Y4NZYNdJvhIf-gtDG3yiO0LAMUvAZBpGmvJocvYW9i3zSwmtfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f056dbed7e.mp4?token=JWKVSmG8K1IMIdycUqF7D5bxFiKutcuopWCEjQz0EgTX3eqYwv79gdZSe7i8gOeL9BGsnSqwm7XXdIPEq01kkfYgjpQQjguqyobh_b6FugpLNMT-sqKlEUpS3SRhNDVNYM82f-d5aDLu62ZWhprEiQOTGaZw2wClXomB7MSdljjGus2U31-W8t1FiaId-wywD4tS1uIY7lrlQoNgTfJtqoITzABmDkQsc1wT0jd1lxou8poUjUIPm5oKVw5S5saZciTvj9FbUZduWAOtj_jD8bOlpqJbVXJKsS6_Y4NZYNdJvhIf-gtDG3yiO0LAMUvAZBpGmvJocvYW9i3zSwmtfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجوری که عملکرد بارسا رو میبینم بهتره باخت فنی بدیم حداقل ۵ تا نمی‌خوریم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83585" target="_blank">📅 01:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83584">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عاشق منچستر شدم، هربار میزنم رو‌ حریفش نا امیدم نمیکنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83584" target="_blank">📅 01:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83583">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یه تحقیق کنید ببینید ادیمی رو تو بچگی همزمان زلاتان و مسی باهم نمالیدن؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83583" target="_blank">📅 01:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83580">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فلیک کسکش از ۵ بکش بیرون شبا تو خوابم میاد   @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83580" target="_blank">📅 00:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83579">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فلیک کسکش از ۵ بکش بیرون شبا تو خوابم میاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83579" target="_blank">📅 00:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83578">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">منچستر فنا واقعا بدبختن</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83578" target="_blank">📅 23:59 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83577">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کانسلو رو بیارید جا رضایی چه موشکایی ول میده</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83577" target="_blank">📅 23:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83576">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یکی به فلیک بگه داداش زندگی رو نمیخواد اونقدا هم سخت بگیری یکم شل کن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83576" target="_blank">📅 23:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83575">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">جا پوتک بودم ربکا رو میاوردم تو موزیک ویدیو دیس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83575" target="_blank">📅 23:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83574">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پوتک و آرتا چرا متوقف نمیشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83574" target="_blank">📅 23:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83573">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اون موقع هایی که آداما ترائوره به خودش روغن میمالید میومد تو زمین باید دنیا متوقف میشد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83573" target="_blank">📅 22:16 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83572">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اقا اول تست کن بعد خرید کن!
گیگی فقط 3 هزار کانفیگ پر سرعت
🫆
شارژ حساب کمتر ۱ دقیقه
✅
@NetingVpnBot
@NetingVpnBot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83572" target="_blank">📅 22:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83571">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کشور های ترکیه گرجستان و عمان اعلام کردن که از ۳۰ شهریور به بعد تمام پرواز های ایران به این کشور ها و پرواز های خودشون به ایران ممنوع میشه (پرواز های ماهان ایر هم امروز به ترکیه کنسل شدن)  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83571" target="_blank">📅 21:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83570">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کشور های ترکیه گرجستان و عمان اعلام کردن که از ۳۰ شهریور به بعد تمام پرواز های ایران به این کشور ها و پرواز های خودشون به ایران ممنوع میشه
(پرواز های ماهان ایر هم امروز به ترکیه کنسل شدن)
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83570" target="_blank">📅 21:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83569">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اینا مگه تا یه ساعت پیش به هم ناموسی نمی‌دادن؟
چرا الان دارن با هم رفیق می‌شن؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83569" target="_blank">📅 21:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83568">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پوتک پری روز گفت من جواب دیس آرتا رو نمیدم کوروش دیس بده جواب میدم
واکنش وانتونز چی بود؟ این حرفو قبول کردن و کوروش رو اوردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83568" target="_blank">📅 21:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83567">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پدر عجب چیزی داده</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83567" target="_blank">📅 21:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83566">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حاجی تهه ویس ببینید چجوری با خجالت کیرو میگه</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/83566" target="_blank">📅 21:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83565">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">از بیف تلخون و پارسالیپ رسیدیم به بیف این دو تا یتیمچه
عجب پسرفتی کردیم پسر
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83565" target="_blank">📅 20:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83564">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">آرتا درمورد رابطه پوتک و نسل چهار و خلسه:
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83564" target="_blank">📅 20:09 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83563">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حاجی این بدبخت اعتماد به نفس درگیری نداره، تو ویس فحش میده با خجالت فحش میده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83563" target="_blank">📅 19:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83561">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPooriaPutaK</strong></div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83561" target="_blank">📅 19:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83560">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPooriaPutaK</strong></div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83560" target="_blank">📅 19:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83559">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stnYS5R1UvXBa_-EyWAe1f7ofArgQWc4XnYe2oBULaMMbsuG_NT7LYe5pqe_84qtElDytmCtBEG2AW1KR_m7oNVC1Zol2eIFmeUOO5IaSbfE3O0H3NYE261Iz-b1J7jz6-7YTu-XEHxnA5BKEQise4Wy8Smljj1RlBXdrzlqg9JMFxAl97Lbg0doNpgQOkvavaeksspRhn69_QSSOJeTcm1oKeNka7M91_byekiDrIhSzWRSXXuBByMd1Q8snWem4wCoYcOyy32MraphnOXMOGh-Y7VI3D4DM3aouo3VZYQTJfL3RlXTffhZkkubuLFihp0oFMZkInMQWvPfmVxovw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورو خدا یکیتون این بیفو گردن بگیره یا آرتا کص میگه یا کوروش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83559" target="_blank">📅 19:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83558">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i97Q3Um2is8P8l2gv4sezJm1qk0CEjClUxU-i6csM1rcaiuhXdFRT9uFwjmsIVS9Eu4TU-SpW9CQaw4ysHrx4OayPOoTqIIex-uQKx3oZQHGJjm8kjCqueTlWqrJj0_I1ctGJH92pbcsiKLmYK8OCDqlpNKHQovDJEsu_Ak9WQ4VFcifnZWn2TqszSbhjeWsKRbrnvvyew6Yqx8j_hGuXiVS_2HtRvgBtj6FP5nGQKetecjSNSku5Qmy7YF0TlgDiSuxX2HOLmV-uTv_BjhpPSTF3dO5UmACFUZqAumCdDoWIpucLiSGI_lsq4clToIQje69hB5J5bx-F0uZwdMYww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتک فردا قراره دیس‌بک بده به وانتونز
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83558" target="_blank">📅 19:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83557">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83557" target="_blank">📅 19:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83556">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4SO6ixubzIh1D9wjb4HdRN7-1deizRb3gw9WULyyehA5D0hHqdzX1WgBjJ6udJeIhSmJCoygfBGECKGNI8ay23rlpI6TaQlaprkL3oYWzPbV0oUGnOZYjfcqY2qm5I25pzYUayi6cdnkoIyQGVIbexuOsbqT6AectdXtdouUNtHvrgEncqHhaHOy7s_qNPh2wihDwpsGQKmH_ba6FLyLs6FmtmBPe-L_U_BrvjzO10UXd0yBk9QNq26KXbLJmjMtXO6TC3sX-YdTDWDztDuCpiqe-GxrGVJ1UwQwK3e6GPsSCJf3E9SOqe8SqAb--L5xbKx5UguR8XcQvw9HEUAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
25g
🅰
🛒
ورود به سایت
👇
✅
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83556" target="_blank">📅 19:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83555">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حمایت از هیچکس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/83555" target="_blank">📅 19:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83554">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آرتا و پوتک یه لحظه متوقف شید پدر ترک داده</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83554" target="_blank">📅 18:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83551">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ek2Gu3M57__aZx5aCDZfCI-hcP8lSGP6RHz4FVVbRTUCT0U6JXPGZ2mmCdwPfL2Mx8LhNFSSXIehclqn5_Pu1NyBVxsAvPgcjG3DviDseiJvJ6LisQ5rkLtP609dPgrdr5U9ey87vZ6TqiLwX6DQntsZcbhclnXoQ4F2G7owVX0ZeREcGoYmzrKOODZ5DETnu89RuBcYbJhK6e6dSWumCSp2xTKyqItmkpe_fzyzKkF_2yQb6cTFaB30NA7XHE6SEECv6KRorfXuTX4j6p1CpYvCnUEzeQo9iz93aH7kwmiHuJCGuw2MqZvA37JoATKBZVsZQZpafegTMZQefW3DJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6b4163f9.mp4?token=gd_us1m07qpUfOdZ6XXxOzOZbjUtM2qqJ7_aQwbldBFrcZg7tseH6EmmOMWsOmcTk4YLvqNibCmiOdw9tciiHGSp2MzfCIerRulxmcOgMRAxVxyObco5qTbZksnx1TMhinm25i5U371tczq_5y-U5GMC04srB-kBFeh6rqImc_LKa22SB-Y8uRKoIljC--0D-meUYZPErX2K5d1jPEPjlaO_toqT3mikptHxRHVioqFBYq8x6jtEe9lYKAqHbEtZd4IIz_jS7CjF4IWCMp2MxVRWHyDzB7M4HJETA-RZuCs2kXRjQt7vebtTN-IPMHy6MEGoL-9yXeC3zh1bsPJKwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6b4163f9.mp4?token=gd_us1m07qpUfOdZ6XXxOzOZbjUtM2qqJ7_aQwbldBFrcZg7tseH6EmmOMWsOmcTk4YLvqNibCmiOdw9tciiHGSp2MzfCIerRulxmcOgMRAxVxyObco5qTbZksnx1TMhinm25i5U371tczq_5y-U5GMC04srB-kBFeh6rqImc_LKa22SB-Y8uRKoIljC--0D-meUYZPErX2K5d1jPEPjlaO_toqT3mikptHxRHVioqFBYq8x6jtEe9lYKAqHbEtZd4IIz_jS7CjF4IWCMp2MxVRWHyDzB7M4HJETA-RZuCs2kXRjQt7vebtTN-IPMHy6MEGoL-9yXeC3zh1bsPJKwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیس ترک جدید کوروش نجفی به پوریا عرب به نام "پسر کوچک" منتشر شد.  SoundCloud  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/funhiphop/83551" target="_blank">📅 18:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83550">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مستی ناگهانی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83550" target="_blank">📅 18:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83549">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دیس ترک جدید کوروش نجفی به پوریا عرب به نام "پسر کوچک" منتشر شد.  SoundCloud  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83549" target="_blank">📅 17:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83548">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دیس ترک جدید کوروش نجفی به پوریا عرب به نام "پسر کوچک" منتشر شد.  SoundCloud  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83548" target="_blank">📅 17:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83547">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_A6E9pQVz0U2lBRq3HenTpIX52CnKCQwGAe3qkXZ6ZxxAchefza0UgIhNM7FsOhOuIvld56xrMPOF9o0gwy383-susWX4hMYcm-kCwcKpcnDPef3P9QHRaUmOYhnrcqI8y-RwcWFj2Yo0f_n-li6eQZkx63X3whkgXbfNb8AxQM9Smle9h77BV3803abZBmcKXxUVjW3CcfK-09DumhFbyGve88N3ZV3EESxHPCu9xxJGeyVHoOiUe4Wmnkmwph9nA8q7wQnDNPStwyIYzL0gkxK49bLLXp51gDNMv-nFr1hlrOfpRIyW2HFrhumd68sS0sRjVHw3i9lwZ-Y9bZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید کوروش نجفی به پوریا عرب به نام "پسر کوچک" منتشر شد.
SoundCloud
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83547" target="_blank">📅 17:26 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83546">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بسه دیگه گاییدید پوتکو
کوروش 7 دقیقه دیس داده بهش
😂</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83546" target="_blank">📅 17:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83545">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKljqFP8BbFaBNZ0GFEpSMkYvHBI2vAfHhUFdlHTJvt1pLPZ4uZkMsA6kUqEpEDLjO4yvBFKauOerNrWNVspoxuhhRwqbzbodb-TrrBeHTaEZ13YxiMuE9IbfRR4SC_HehESDBTiVuvU04hCP8O_RwvctHIac4pvh8dshcT0Rkp3Fc1nWdSh7Ts300VjNsQww71NZYgR-jh8jidUZNuji-3_YiM_4qQWMTOgAWYWtvsGpvjlr7oer-t3Ct65LHoJDQ1msvxKW1hGAQpB0cM8y4s-Niw82FJMdOwWU6fVWvB_Wu6DLMhiTiMkKK-qmx0z0Q6XB9vwIpoH9t1OUGDDlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر کی این تبلیغو انداخته رو چنل حلالش باشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83545" target="_blank">📅 16:04 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83544">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">به بلایی که خط حمله بارسا میخواد سر این دفاع های رئال بیاره فکر میکنم، تنو بدنم میلرزه</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83544" target="_blank">📅 15:41 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83541">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پولدار شدی ایرانی
کالابرگ قراره ۳۰۰ هزارتومن بیشتر بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83541" target="_blank">📅 13:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83540">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mi19_w0arWr-USCi1y5cgQc-vKyiHbOWeQfJT3WXrCiJxHQ6l1aJBIEV8yjl0qQuDlg-XncJvGSfUZ-X1kMeHwnIb7vLwQPVBvCRjGCTWqTF0dpluFB-issVooTzAqmlOGBitYNuihqpghLGX7C4W5G3HYYmWv99sPVPLrTGGqXxbPnlSY9ZS56sY3ODC0Jxs2IEJ993di6jdUhoTh-IPOYAHIGaJ-re9TjTdwOLRA6pQyXTV-bBEmSHLk-JSn8XLFuXYAXOfB5FO7giDolNPSde0Bx0HzgTtltOuW_zKp84xJxilqfHBkt4HNIdfsQ_PFThnFyjUiHJdApzGSQ7_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی منتظرم ببینم کصکش نبودنشو چطوری قراره ثابت کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83540" target="_blank">📅 13:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83539">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5ontiJSxtTHl7s7S1ADIHPFogDb4Tazz8J0S1Sk9MsbYPvfKE6BSMYyIKrT-2OoEHUCMoBQdCG98MD8eWdYK6JWQClvL1_2hMSlm8MRu-eAXyQbB37JmwXWeR7z-dVNc7NcV78k7BliWkwUgOzAKUG_NVgx9nK53sPVMWgZBLh14mPJxFQSjd2vMMLEaPunVbz2XDXcM7GHgj-ASH-1e9HqIEsWc1EOc8LQpgICoSsYmyBNoXBdJFcXFz8NHlOR6b8NQNiI6kYnnl4cWa8kYjEYfJpY8w-Gj1VPLOrq50pzQvDT0uSo4HXkW3IUmwFIVFzdQoeYeXJ9GNpD5TyxmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتک الان در همچین شرایطی با آرتا قرار داره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83539" target="_blank">📅 13:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83538">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Spinner</div>
  <div class="tg-doc-extra">KVIRO</div>
</div>
<a href="https://t.me/funhiphop/83538" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83538" target="_blank">📅 13:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83537">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EV4oM1sXvV6pgd9tElhDwRhrR_uXbkly9urSYTOBr7NaWifxOQmNCiUT9w37pfFYJIHBymtgvvMVar46CIe_Iot-jbZdpMSOSsz6FLKK4p8bXvQ5dw695f_VrP8uDmEc-ismmuiA0duF3sO5w3KdtUdz9-wr76cp9dsIgwpBbZjv1AsULt4xfl1nuuJeAyVSYQRmlCSATvDMOpWx1_f8FbDmSfCEqcyR52Prtm7GgnbQle_5J37hmt5xVgfVlyjhkraxQe_V_lm783_maiHGCY3jHEUlYWBJ8zY5d3nveTZFe6ngq2BBPZ0-o0XX6NPR_J5zYUOX5bOlA9uOFPQa4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید "کای‌رو" به نام "Spinner" منتشر شد
SoundCloud</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/funhiphop/83537" target="_blank">📅 13:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83536">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">#NewAlbum Released
🆕
🗣
Artist: Drake
📋
Title: FOMO
🛑
Featured: Yeat, Don toliver, Ella Langley..  @GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83536" target="_blank">📅 12:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83535">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAHnsGSlZMuRJbJ5YSHaYAEUKWnL3u8PeoX-SQJaYloFpUFrYBYFGvaWSNRSWFX7nIaCg5q4ZQg3mubMLGhfo_Jpn9Wa1gfxXurhDD9VforDSR6S49v0ndc1wcOyoDxURlEzUOoh03DKu855jrJ9Q49roU5nA521NuVzWVGJr8NdX6TiEGPOJhHaZ0qEkuVLqAWpNaUPqByZvlzHNzsRYQ7_VtTJOJvgB3Imn3Nzk9y8qg6i3_rCtpiX_VuVd4H8MKOcSSN3-Z2D3E2_rCbGxI482llYwP-dyCThRzwSTgBbe4R7FvNMe4lduv2bG9701T7DBSUQZJxA2vrsqB-T_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NewAlbum
Released
🆕
🗣
Artist:
Drake
📋
Title:
FOMO
🛑
Featured: Yeat, Don toliver, Ella Langley..
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83535" target="_blank">📅 12:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83534">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یسری شات دیگه هم از مهدیار پخش کردن که محتواش اینه که مهدیار مخ آیدا شاکرمی خواهر نیکا شاکرمی رو زده و بعد یه مددت ولش کرده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83534" target="_blank">📅 11:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83533">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یسری شات دیگه هم از مهدیار پخش کردن که محتواش اینه که مهدیار مخ آیدا شاکرمی خواهر نیکا شاکرمی رو زده و بعد یه مددت ولش کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83533" target="_blank">📅 10:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83532">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GT6J1MnSYd85TjYOabhFHBe2xJP1McN33MfkBSF4nS8eij2rpHp5AD_6jxfNjMTENTtCKrwXLoaWrzYYgd0t3k7TZSW7hfDS-WpfdMVCGwitD2qW1NKQ47ItgjX-3kbxj6JNE8rWwkYiC46oPpg8SSPeDm7jfe2h6-LRI7hGyJ_N4uUrHsg17MDfHEuUa0G0Jg5P1wf4YrTvmKD7CVY8CWy0v5KCeNPDiQcCXIftQHCLz85hRnOUbpdIGJbWhzkVGZE1USpQaw85TsTfeMkQBsBtICynfSyB3_VNHuQIVmE0_vhZ3EOEEk-xMnkcLxIxLOTnT9OLVU8O5k6nfJKZaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کرینج بازیو بس کنید ندید پدیدا بعد از سال ها یکی دیستون کرد حالا گاییدید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83532" target="_blank">📅 10:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83531">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">با من از صبر صحبت نکن من برا هر شوت سوباسا ۵ هفته صبر میکردم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83531" target="_blank">📅 10:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83528">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bIDQFymZrAgj8rsfxFQKwAM1QDXmGageRNwfjeea1lUU1QfhlqjkNu8HFPebWa5zWu4esG7PozavXBgeoH0BH4Be4t68Niu_qGFGwoZP2JQamejg7e0kn01XsI7LVwZVbxMJndlbBYjIuJ3KDOZs6NBOLTjOVt_T9Sk4hd4MZaRdYAnmgRE9I7u29CJrHMD8dvsE8cLXr3k21uRiDoeOxiC_XsAmYgMNpOuXqv_twiu6zMG0wxCceIYf4XicWxJZg4ZOY-VuFxOlW0Ks4gz0-qs9CBptITRMNDhR81fYxa8ayvz7Uv9ByCrxO---jNUFaxi2L6gP0v_ukju9a-dHlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LVgNXNJ3zscnU9WTwHuTNgEUg8zXCNg5XfL9Kb_XqkaSPzmLNG4u0B1QLIcBgKuLM1nHvhrXuyFib-ZPE0j0ERLskMGBYJCwFVaOhbMZ-STuyq_o29CKAVJ0RrUCkm4OFVtLY8PI5n_L0t3m0uahzS9UZQi62oivN3MFFOKFVtC9jvoa2telPf7VRg3VrTDahlD9V1aTpbwbg1xHfyLUQcJRQwfOFtt0SCg1AsNu2DmSw1y5YgeqR7yk1riTXcow8hwG96DvujCeivUpjXCylC_FwkWe6Y7DjiX7OSqI6JT1dpIZJ-UOL6LVMsUEX_U7ptKHsaHYvK1q6vwc9s01FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UqGiXee4LRB9mya4MXDI32t7WKo-QraCWm0fvgkKvMe12jyGdM-yKcFRPd-Wp9Mmd8Xmw-gOe5pSMEe2Mm8JfrcEaz08S6YqtriK76VHQb16jqYqsJTWkC0VE7okA0OTbiDI7mkK0kIAtgGBuyLsAxdIgCN95C_Gt3nyb3-wp1YF1YsVSYHH2qS2zGFVx6plL46kLp7iv1fbRpAdUPfMuojX2dVr2gA15vmw3jmTD8PZtoo7oBZYoxO_KIMlySmMHPY9pBXhYrL1O-4NVIs6L744SmhSd7QVE98XC3pH6UvCGis0AKJrlcibvvAh3gJSosYVF2erO8er85mmQUDBew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شات های جدید شکیرا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83528" target="_blank">📅 09:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83527">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyRy0YlO-v96i2HNNoof0Ljg2zhrz67aUGHWBivaL9oxgqJNNgtawZpag2fYLDO_qU5b2vgzkueOKQXKTl6uTx2oJWyRZCoQzEmk7gMP0RSKO_FiE5uWwbK15agtkvU_VPC62QiaCVgC2ud5p-42WdwJQQPV-sRkCIHM4byY6YT-DuSTuo8BjGY8pvXJYQiemGbqNrTmZ3NkX3tyzkV7EaWeOwpsoMPKrEmfAP2aWUh0NMNvVoFbq0xTKnCVqAF_qd_Ogxzk55A2zx3V7gmLZl1dRmWEtgiNsIgGMS7mW_Sr2uM5TNNF4WJ1OM76icwrLWjdy8UFUG_3rPWWJcrsyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
اتلتیکو مادرید - اوساسونا
⏰
ساعت ۲۰:۳۰
🌎
📲
لوانته - اتلتیک بیلبائو
😀
ساعت ۲۳:۰۰
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R25
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83527" target="_blank">📅 09:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83526">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">این قیمتا هودی، سویشرت و دورس جدیه؟ یا دارن شوخی ای چیزی میکنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83526" target="_blank">📅 08:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83525">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ددی آرتا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83525" target="_blank">📅 07:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83523">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ببینید دوستان بیف تو رپ طبیعیه، حالا یا ایکس(وانتونز) یا ایگرگ(پوتک) میزنه ولی تقسیم(کچی بیتز) حرومزاده اس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83523" target="_blank">📅 06:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83522">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">لاشی دو دقیقه دیس داده ۱ دقیقه و ۵۰ ثانیه اش رو داره حرف میزنه ۱۰ ثانیه هم خونده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83522" target="_blank">📅 05:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83521">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دیس ترک جدید آرتا به پوتک به نام "شکایتی" ریلیز شد.  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83521" target="_blank">📅 05:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83520">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXR01Am2K_e4twLvtgutTauNJCzAVrdevX51OvIVO_XHq-HPa6pzunkXO_3ktwUhRQv1pt8N1iELjHIduTFsxNEzKUALrzqQyBStukYNFVsgR2XgVSxRKNGWgJhaI1Fd9HjYdJPLb0lXYd2zqTCRSBsuXyOOnrWz4z2BglOVek6t5JZaP5aungz5S1_qFJI-HN3oZid9dX3KmiMWQqOkBpL90T8A9UZJsndt4sUk1JL_MQYp-CvxXMDDpAqxIfvIB987EiXJFtHrvn8lnt4YyOLEX8_kVRA30F0sksQQtfAr7AQDePhiOxPvSKpl1I1D20hzUxUGxZf_JXlvSpBrGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید آرتا به پوتک به نام "شکایتی" ریلیز شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83520" target="_blank">📅 05:55 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83519">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBx--7mfcgrKIWEZdEDPZL2H2HNF_r5-bo2BYGW7g5uJhaEwLL8jr3QzaUrZkLx75xKBn4FD36UxYq20JgilWi-vM0ec5s9i_FnDDn3wxIw9jGJ0hqz2LU2OyjN0rmM6M3Gf_vRceDHeNalLXjPMWs5LyFAhl7Z96eKnl3_u_YjoxMbg6cM747DJmYuP9kiu2agsmUEQd7UOtiw-Zh66fga4MtGyESVDNKFl-ZnsDiLCae8dVUs-_8eouQXKc0ike4SWhONWopMoGmy9FMGjlrgWt9-e6bYYgEAYRTHHS8shkjNH4KzGksjWJdKExUNP03StuwpUopiHDogvytl3TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوری و ویناک رفتن تو جلد آرتا، جواب دیس قبلی رو نگرفته میخواد بعدیو بده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83519" target="_blank">📅 05:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83517">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e27bc926be.mp4?token=F9-YZkway5WO-IlFYrxjOPvQbARblmF7j6sLvScPffVyo23lf01vJq0xk01FwMsKXSm5LQp9Q8m-Qpiz-vZ56mhoK3hvzfi3F8xIBxnYt7R4j4yTL3PoUK6zu0ovf0at_mpWuCitlD4sfBCKfzhMAxUc0Qwe4iQDi060gZ7D8SkWeSYQDP8SAglhlhiR7MYVXq00WANYuDnjTCPc1b76o6PcHKljxnlOQjzc74ZdVKOrnaGnK1jwBvhSHQHqrqCD3s8lVmTSHQBIDxTXnKUHpL9rzMYmEuduywIB9CoGFkPV2wfRatSEsm4c05C3Fvmh3xw8V7Rbzt8Fk8-EwG9mgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e27bc926be.mp4?token=F9-YZkway5WO-IlFYrxjOPvQbARblmF7j6sLvScPffVyo23lf01vJq0xk01FwMsKXSm5LQp9Q8m-Qpiz-vZ56mhoK3hvzfi3F8xIBxnYt7R4j4yTL3PoUK6zu0ovf0at_mpWuCitlD4sfBCKfzhMAxUc0Qwe4iQDi060gZ7D8SkWeSYQDP8SAglhlhiR7MYVXq00WANYuDnjTCPc1b76o6PcHKljxnlOQjzc74ZdVKOrnaGnK1jwBvhSHQHqrqCD3s8lVmTSHQBIDxTXnKUHpL9rzMYmEuduywIB9CoGFkPV2wfRatSEsm4c05C3Fvmh3xw8V7Rbzt8Fk8-EwG9mgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو قدیمی‌ای که آرتا میرحسینی از پوریا عرب بازنشر کرده و ویس‌های جدیدش خطاب به وی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83517" target="_blank">📅 04:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83516">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">جنگنده های اسرائیلی امروز چندین بار تمرین‌های شبیه‌سازی‌شده‌ای را بر فراز ایران انجام دادند، و در برخی مواقع حتی وارد فضای هوایی شمال غربی ایران شدند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83516" target="_blank">📅 02:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83515">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjAwdeeuk6R_FktWiJLSUYCsBaDy0E51yywj15zD-_J6xL2alFTbqoQ4sRMocBbJZ6nL6WVm0E8gL86gSomPH5Om83fgDz1kP1BZEUw4VH_asAk7xZQFK_eajT-PhNGR-XCjlM8Jl406zGyUt8T6nZFWQvZWCK7g1pJ-DE79nHZ97oxxGb43rRayn0SzgrJC6AU4nxEIraoDDkpHZa1CG5EXhxEdIDbVbcA6x_qhw1h51KZvp0KlxewC0aBuWtKTSiNBjeSkggYjEylJspgKJTl38CEoOAh91bpqIJfodE0L8MgJYhCFGv71bDjgwfzbX8wQyBc88xFCap2laF-L7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد رپرایی که تو این کنسرت حسین تی ام، بیگ شگی، تیم بکس و... حضور داشتن بیشتر از شنونده هاس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83515" target="_blank">📅 02:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83514">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08141ed2a0.mp4?token=QMtfQXfGJDnXMitL5pFq8cB9zuHlqbhcXSMCg_wG5x6s7U-kiDOuSdVKJZUwXZjj6XSs-oqrFq4Ur2GNSY_WaoPlQ_uTBid-eoUr30LuBQ5eegCrkHc686rF3bcgVrmP1PR9eBC1Gu8A7yHKsbM32HJx5Xj_AXFeUsuqAIbxN481d91mQBJM22z9q9LPgZW6sGDksh_s5p1g44fLDjuuKNv0eHNp9bH5W5GL8F3H0pF7K6THnOz3eUoF8fEvuQlZ2cSj68jN0FkIoABoPvkzjxzjpp9JxbpMmH2nb6H6LbAXjszJb2yxvSds9eIYvCheaKfG07x4nKsf9ZcEhdJT3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08141ed2a0.mp4?token=QMtfQXfGJDnXMitL5pFq8cB9zuHlqbhcXSMCg_wG5x6s7U-kiDOuSdVKJZUwXZjj6XSs-oqrFq4Ur2GNSY_WaoPlQ_uTBid-eoUr30LuBQ5eegCrkHc686rF3bcgVrmP1PR9eBC1Gu8A7yHKsbM32HJx5Xj_AXFeUsuqAIbxN481d91mQBJM22z9q9LPgZW6sGDksh_s5p1g44fLDjuuKNv0eHNp9bH5W5GL8F3H0pF7K6THnOz3eUoF8fEvuQlZ2cSj68jN0FkIoABoPvkzjxzjpp9JxbpMmH2nb6H6LbAXjszJb2yxvSds9eIYvCheaKfG07x4nKsf9ZcEhdJT3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسام سهرابی بلاگر شده و ۸۱۹۲۹۹۱ بار از جاهایی که کونش گذاشتن ریلز طنز دراورده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83514" target="_blank">📅 01:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83513">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">این فلیکو اخراج کنید ناموسا، ۷ گل زده اش تو بازی هم حتی ضریب خوبی نمیده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83513" target="_blank">📅 01:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83512">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi)</strong></div>
<div class="tg-text">آمار امروز:
🔴
1.49
🟢
1.78
🔴
2
🟢
2
🟢
1.8
🟢
1.34
🟢
3.89
🟢
1.67
🟢
1.44
🟢
1.35
🟢
1.4
🟢
1.6
🔴
1.9
🔴
1.46
🟢
1.24
🟢
1.8
🟢
1.2
🟢
1.3
🟢
1.3
🟢
1.3
🔴
1.3
🟢
1.41
🟢
1.85
🟢
1.5
🟢
1.3
🟢
1.5
22وین
5لوز
https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83512" target="_blank">📅 01:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83511">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بخواب بارسایی رئال برد</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83511" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83510">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8X3xLjqwjzBxRXj84Cj__rsVaD_9AgdypeyCwrBeyB8dtXCvkTLTgk9CDIRG-POPzveb4kFH6ycM-GdlqjcbG96yckKCSelB-7TAjw17m4kCpU5SDzCJS0k6XnjK0MHluQAGKTagjS3dRPzpy9kqTnllNmdDnH4AcJHYP_j5zkJ83hmGhW49GVHy2evGezaR-HyFvrrUMePRqNXA-HYJwRfUcss6WyKmWhrcdeE03nFXWsJkPdmThm5sOhkYpepQaDvTJHXS9AFAhE-T7O1aG7soJCvl29VhqUDODfdSrKYdxnVVVDQ_insIs28Z2IkPvFDD8YGYpiNSGIBAT85Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقت خداحافظی با بارساس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/83510" target="_blank">📅 00:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83509">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3Yc98PwNUNL_o8EcSivbnI7HxyiCZ4_3el5B1qGGaSAniDGGq6nH-lJa1MvAYPveTEPC4IKB1R3TG-NN5AamNMoTxea9fl4ZwOH5HExIAFslXC8fG_C8r_eBGwZTmkEbWJzULwto89s00hbvfshiC-suPc-ek4ZPNwWRcSifw93NYqXFMr3N0nHvKms6iKBtGWgneNsk49Ows6CvmplF9qJK9RJR_TEPNAGNdFMbMTUZDBF5Uv3pbWqn1n0E75VMXIfNlp6hzY-ZTSCNjAS3ElXewuibk8Sg72NLZkXUEnpJ7Do5M3Nhsp1MLvRiam4aiQ3oVU0UVbPtHTPGeZHTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که دوران قطعی اینترنت خیلی فراگیر شد اطلاعات کاربرانش در دارک وب، به فروش گذاشت، این اپلیکیشن اطلاعات حساس مثل کارت بانکی و ولت و پسورد و… رو از گوشی کاربران جمع آوری کرد و برای فروش گذاشت  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/83509" target="_blank">📅 23:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83505">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a69179260d.mp4?token=jZZekMTKH20CPqBZ5HOhSYO-eLR3ECq-gGJ-l_PJnKRue2NF4Fk0Dxpub815xeaPPHdUSmozPKnJ4f8C8OKzxMgSWNqlVvIYezHZID49DMDQ1s2jHDhj5ZTScG6BmwhCcttb9XaAjN_cpJt6hasMM3F9NTD0KkgNjGjvJ7WKwtGAl_kyrsm6b8xwTQDNnOyApntRd36dToMktKe9_JmVKAnECyxVFtjyHjKz7VzrfotOB1GfRJTmS4xZQ81gQ7Drdy8aoe1JbLT3tV6HXQwQuTfr2peyNiRrGoQjpOt4btzTqbptJ9pB-tYFrLwqox1nKQICOcwe0aIwlIYQvKH_vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a69179260d.mp4?token=jZZekMTKH20CPqBZ5HOhSYO-eLR3ECq-gGJ-l_PJnKRue2NF4Fk0Dxpub815xeaPPHdUSmozPKnJ4f8C8OKzxMgSWNqlVvIYezHZID49DMDQ1s2jHDhj5ZTScG6BmwhCcttb9XaAjN_cpJt6hasMM3F9NTD0KkgNjGjvJ7WKwtGAl_kyrsm6b8xwTQDNnOyApntRd36dToMktKe9_JmVKAnECyxVFtjyHjKz7VzrfotOB1GfRJTmS4xZQ81gQ7Drdy8aoe1JbLT3tV6HXQwQuTfr2peyNiRrGoQjpOt4btzTqbptJ9pB-tYFrLwqox1nKQICOcwe0aIwlIYQvKH_vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی ایران حاجی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83505" target="_blank">📅 22:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83504">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بیف اصلی شروع شد باز
تو تنگه هرمز صدای انفجار گزارش شده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83504" target="_blank">📅 21:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83503">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خدایا گوه خوردیم درگیری بین پوتکو آرتا رو پوشش دادیم بس کنید توروخدا</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83503" target="_blank">📅 21:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83502">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">انقد نگید چرا بازی پرسپولیس شروع نمیشه کصنمکا
با تایم تیمای شرق آسیا بازی میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83502" target="_blank">📅 20:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83501">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تیمای عربستانی تو لیگ قهرمانان آسیا جنده شدن</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/83501" target="_blank">📅 20:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83500">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpnPmIAayCLeFKU2KbqELXzkSud_mxehwTYwlD9PFP4pFonU450rkRbExbF-Md9poUasRQVBqKVMlZfE1Jatpa0fR7erFwKpPX3pINmX_3QseN-_51i0FAKe-5ZFu48pJxsK2tgcaLTPx63X3Nb1Rr3qca9z9KpwIFjqFA0_bzBUtucKh0sJemNT1IpKE05v6KvOT1arujyjrYcNRgItlqYBQHlexFIjHzPP0DT9xCSinZsuhjguK3YUMI60GaRepn8OUdhTb2pZGYeE3vR3oqQTmo9k-RdJJO3MZgv1ztsz1Y2A-gktFrOgwIyXTf5mpy0Kjc3bdchJwVYO0g02nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم همینطور واقعا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/83500" target="_blank">📅 20:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83499">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فیلترشکن JumpJump که دوران قطعی اینترنت خیلی فراگیر شد اطلاعات کاربرانش در دارک وب، به فروش گذاشت، این اپلیکیشن اطلاعات حساس مثل کارت بانکی و ولت و پسورد و… رو از گوشی کاربران جمع آوری کرد و برای فروش گذاشت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83499" target="_blank">📅 19:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83498">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5VG1nGocqZpuqEUBk2U8V8TXA-dJBz5Zv4NCRG-pLyAPA0R2Q2psq2ITLSwNFPOIx5r9KFBo-Ji76JtaVbdzrH8LzdtRV16F8yN6HsndJdxNOHCPKEgD8R9za6DyV3RFWN2HotNzjEaU-GM6drD-cplT27H7gS2oSxJh85xyVg1v-1zNF_JRw2l27Yd4RPzIHJmCqtDfMotz9aW4fnUqoYJfFtLLuN9iAbcAF2Ip53HX3bK3vX-2QY2ZQ9uWHv8OzA0fDu2D4qKbpylSLzREYUSMLlSekbyBv-1wUvHkIv3uWkAbMmZseL7lWl_rMtp-z-ICfKveijbIUz1HL5b0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا حالا هیچ کصخلی از دید به قیمت دلار نگاه نکرده بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83498" target="_blank">📅 18:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83497">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83497" target="_blank">📅 18:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83495">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYTedKgmo8X0XT4GyVyqikD7XjP_kB2dNY0OiJ1RWCOHh8g35FWZ7ap8isOczErpEh_-Oj1FOy1lVwqYm8DnJeSjrJrhFwtYB4uE5z5esbM4kZHqrnrzHI_6AuGIeqtbP6hK0N9KDn0zzN92nBn4yv-SaZ55yioQlibIg9iPL0wDMEzNaqUk04rfSTUE_w4eQuAteQu_9yl2yrMFnDwX5Ee-9XvUZGF7J-Bqp2HjX-4tJlv6AzfqQls46XmhN836rTpFFqr3E_dt6jdsOGJGiXL22Hf-FbYdOEMy-WiUEBmWJQWnEQ0MALJYbCe6xy4pxvIJ6DbsG3BR2ZfUKLxaGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلبان آمریکایی که از ایران نجات پیدا کرد پرسیدن چی بهت انگیزه داد که با دست و کمر شکسته؛ ۲ کیلومتر راه بری و خودتو به بالای کوه برسونی تا نجات پیدا کنی؟! گفته تنها انگیزم بود که نمیخواستم سر از صداوسیمای ایران در بیارم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83495" target="_blank">📅 17:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83494">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/959d87b013.mp4?token=jllA-kEZ2UvDDICu9MhW4UQESrc1YqNBOLDi13w-WsE4zalgdlD2ixnDvxREUEVptu2268QhSAIkum1wqf3SJozIDKtrCh6lSLYZ5KBCRuRN1tDK6mTDbBycHTnwXchdZO0JxkUewv5yiGKTJnb0aGDohKKComX6cLaUEFe_8Eu1FJ-g04LndagcncHvUrrMCJSIUZMOEVL7R5ukT5bCmxlAR8Y_CJ2TXY09ZRdZ19GfIRpqgB9qGvqYRKhb3oKHm588UfBKxG1_hMetSal_YN5F4nSc8d24oiHR_ekD2dLNG7fNxuHsI4iILxIsqOAFaF3p1dvMWqa61qEwhMY5_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/959d87b013.mp4?token=jllA-kEZ2UvDDICu9MhW4UQESrc1YqNBOLDi13w-WsE4zalgdlD2ixnDvxREUEVptu2268QhSAIkum1wqf3SJozIDKtrCh6lSLYZ5KBCRuRN1tDK6mTDbBycHTnwXchdZO0JxkUewv5yiGKTJnb0aGDohKKComX6cLaUEFe_8Eu1FJ-g04LndagcncHvUrrMCJSIUZMOEVL7R5ukT5bCmxlAR8Y_CJ2TXY09ZRdZ19GfIRpqgB9qGvqYRKhb3oKHm588UfBKxG1_hMetSal_YN5F4nSc8d24oiHR_ekD2dLNG7fNxuHsI4iILxIsqOAFaF3p1dvMWqa61qEwhMY5_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیپ‌هاپولوژیست بالاخره ترک کرده.
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83494" target="_blank">📅 17:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83493">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcIlbKnADqev2CoNMsmDOfWExIsqjJw_rBCvPeUVPjQv8wLnyx7bsTsQg48THJiLOrVVWSbGMolT-BmKbcCWPQJJJc-Oj-vp8y_-URrEfp56JfmkXnl-DuYHJyNVi6Rte2_N4P_2ksHq2nlrkcI2xTrMy4lLyl82qcOvvSeX5s1YzcCqlIh5LKk6hyLs2ghaGJF9ZUb3AXUnkNKw8zWZpSsu3D0Ij8akLhj5UggfpFI9DyNpgcZ1vpW1wDQ4y9-_atLRZM1gI8MyCkI2TgQMbqlMpj9RxarpidMy5JW2UDHlLnoQj-0a-zug825nxYMTlWro9m3IQp6mBOoAxksMFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83493" target="_blank">📅 15:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83492">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فینال سی ال ۲۰۲۹ قراره تو نیوکمپ برگزار بشه و بلاخره بعد چندین سال بارسایی ها قراره جام رو ببینن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83492" target="_blank">📅 14:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83491">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خداروشکر حداقل وسط این همه بدبختی طرفدار دنیای کشتی‌کج نیستم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83491" target="_blank">📅 14:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83489">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrOdHr5YeVvUdhmHrhtUa-Iw_3j3HRZQgEHmfI44RcbgV4Yp7wnmKCbGIxcXpofdG5-lYtKBirkAtOAPibtDKRzejHuO_BnyJrTyWlBKYv-Cj0MH5djO-vteB99wxaFg-sEi1Oi8oZeTotYEPWg-32JXpNHD1e1Gx-T5TtXcwvV3vb862OSrjbM2CPkDo6VUNRcMTgTnIO01O0Swh-njliDhpQk4LMmu1dWMIW6hMph9ODstbu0ywFiFtYmo039Iu7K7ehzeDCJEiivG-5HaEht2VlI6YEtwrJ-xpMhel695OgIOAflGtYxvYIzhIM3vW3pFsFHVR5ylgYlGmgxXbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادش بخیر دهه هشتاد حاجی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83489" target="_blank">📅 13:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83488">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">هشدار شلیک موشک تو مکه به صدا درومده، فکر کنم حوثی ها یادشون رفته خودشونم مسلمونن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83488" target="_blank">📅 13:01 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
