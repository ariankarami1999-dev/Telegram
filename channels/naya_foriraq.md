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
<img src="https://cdn4.telesco.pe/file/oO-Io2zz8vx2YQ3OGKIx_zt-LEDfmTadNxBwh_mhw_v0TjrF3JLb7wFBAFxQ1g4pSIvzY4G2caYkNEc_aXuRM-t-Gyw8tDpLER34bkp8pPhhbayimLRqrNrzg61ShwaWl4GFPyQqgE9yg0o-Q3k5MKdHOW3EP0sOJTynjpxj6YXeJmuoFdoIowAei8_4FD-5YydbLauPkqDLmTY_9Np3J7KY1Ad_MNQQudNyKhI3eDzJFkGtn1ATnTENWl-sv9Oc4MdTIcNsaKR0dqMpF6irl_SFPblooVZrA3iFfx_lYQIWsKLFX60RebdvVUa-ufPbwo-UuG1C9yqnmAP--A3YqA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 02:58:56</div>
<hr>

<div class="tg-post" id="msg-81001">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd7aa532cd.mp4?token=Asa23_131JWVg4RnrVo_zHJwWsILHfJ4_5fPmczO7m99bK1Bi71j6D9X4Ux8Nhj5seqlN9eJ6Pb3tTcZAUq2mMHLJdBoV8XYB2LELe5r4Mm33v2xxcjbVfO9A70jn37X0RqGMGARXzt5atKhzde5DseKIl_Fdis5MQi-pNpgJz5wLQ03pAG9_LEwENr4Uz7q2ieHTLFb7okc2hW3eLulFWZDL_E9QxNxDYss-XbvOey-eqbsJdJixwD5Q7_dhEoJ2sQRV6hv9pLRcue1BfAaTUcJc2FF6wqvE2iPAhIia2YkoIy6DINbvSfwmVV_Fd_7E3A7X7dZ9XNge7ls990SSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd7aa532cd.mp4?token=Asa23_131JWVg4RnrVo_zHJwWsILHfJ4_5fPmczO7m99bK1Bi71j6D9X4Ux8Nhj5seqlN9eJ6Pb3tTcZAUq2mMHLJdBoV8XYB2LELe5r4Mm33v2xxcjbVfO9A70jn37X0RqGMGARXzt5atKhzde5DseKIl_Fdis5MQi-pNpgJz5wLQ03pAG9_LEwENr4Uz7q2ieHTLFb7okc2hW3eLulFWZDL_E9QxNxDYss-XbvOey-eqbsJdJixwD5Q7_dhEoJ2sQRV6hv9pLRcue1BfAaTUcJc2FF6wqvE2iPAhIia2YkoIy6DINbvSfwmVV_Fd_7E3A7X7dZ9XNge7ls990SSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
بعدسة نايا |
المواكب العراقية في طهران تستنفر لخدمة مشيعي قائد الثورة الشهيد</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/naya_foriraq/81001" target="_blank">📅 01:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81000">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eda2a08b1.mp4?token=KuYU4_KsFrS_FC1wC-9pTMS1UEU6iEj2Dg1rMnFU3n1B3uW8w74mH9CeAxVBFX_zmAqimM2RspHCBfvtQqkRr_NUaCJAOQ9v5R2UpKiyYb33-G7zfInrmi2pgPGfZzkrLpB_E6NGVRtK1q7YLX2WdlTYNnLhg1F1d__SpxDhJICSd8TaUToHYWg1LAz8ttSIJniWl3m6RTueAG5WCk632pweIhYHsgZcdbwRa5Sluc8EbrdZZ6yIp-cBNK6-0cxx4zbMrU8Zj9RXeMzptH99_rkqQ_pmdQmjGcntNC8M9_a_GoGeppZf7jm7dFrUPlzpB9fWObSGkYSzVHjY35SG2oERG5Wz8MRhI71tW5jseFbKWcVFYriQOzeITyTwCLXf1l4qPf3ykol6XpMI6Ypz_qrRndytPTkOeB6MnezxpA9pw260mkRK8P8S-v06Qhw8ptWfRKoixr7_bgTyqz_OL--Ehqzrd5kRzy5zh3W1pMli4_w9UEwSAzS8CputAeLVabQx99wOz7XyztNcajlUMwMpSJTzwUWVMpOqmpLf7ZiKOxbldIp0IU1-zM3YuTFOywh-MmD29fFbonW58M1SobcDdGiEsmI7YnJS94rLsnHA3ltHKCkX3zdYQciRAu4oYnsmHKl02xmhStFIvyq3kdlJsx2eqD7eLt9r-GuDC0s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eda2a08b1.mp4?token=KuYU4_KsFrS_FC1wC-9pTMS1UEU6iEj2Dg1rMnFU3n1B3uW8w74mH9CeAxVBFX_zmAqimM2RspHCBfvtQqkRr_NUaCJAOQ9v5R2UpKiyYb33-G7zfInrmi2pgPGfZzkrLpB_E6NGVRtK1q7YLX2WdlTYNnLhg1F1d__SpxDhJICSd8TaUToHYWg1LAz8ttSIJniWl3m6RTueAG5WCk632pweIhYHsgZcdbwRa5Sluc8EbrdZZ6yIp-cBNK6-0cxx4zbMrU8Zj9RXeMzptH99_rkqQ_pmdQmjGcntNC8M9_a_GoGeppZf7jm7dFrUPlzpB9fWObSGkYSzVHjY35SG2oERG5Wz8MRhI71tW5jseFbKWcVFYriQOzeITyTwCLXf1l4qPf3ykol6XpMI6Ypz_qrRndytPTkOeB6MnezxpA9pw260mkRK8P8S-v06Qhw8ptWfRKoixr7_bgTyqz_OL--Ehqzrd5kRzy5zh3W1pMli4_w9UEwSAzS8CputAeLVabQx99wOz7XyztNcajlUMwMpSJTzwUWVMpOqmpLf7ZiKOxbldIp0IU1-zM3YuTFOywh-MmD29fFbonW58M1SobcDdGiEsmI7YnJS94rLsnHA3ltHKCkX3zdYQciRAu4oYnsmHKl02xmhStFIvyq3kdlJsx2eqD7eLt9r-GuDC0s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بعدسة نايا | حشود غفيرة تتوافد عبر المترو باتجاه مصلى الإمام الخميني للمشاركة في مراسم تشييع السيّد الولي</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/naya_foriraq/81000" target="_blank">📅 01:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80999">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a596566298.mp4?token=JgOdpAWveN89A_VLnUvtPE6dXVzYu2D_1U4IOJQDWQdGwKs1syJoXxOx3W6nYnkwYGFZ6f7-SUpJWtiH8OM-xmgTZHuLV28koKS3P4BaOEROu2-Hf3e4INMWrgBsiiRJ4i2esnHSmGjdhM3ujqwJs2_Gh13-RmlhTJYfA0phC9Pd7gzCOD7adOk7DtVfdyIzF8OJnCdi7MlC5t78HEwoqJjn1rdurnFpVrnNl2a34EVhUDnmoFv3iw21DYoLsg6x1ftPVi6CuxwJh7UNlbG4KQQ3NEmRaHAJerpC82rCg6PtpaOUY5UOXTZjOnloTzqyoUnJV4qj5ATPRxb0Xni_Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a596566298.mp4?token=JgOdpAWveN89A_VLnUvtPE6dXVzYu2D_1U4IOJQDWQdGwKs1syJoXxOx3W6nYnkwYGFZ6f7-SUpJWtiH8OM-xmgTZHuLV28koKS3P4BaOEROu2-Hf3e4INMWrgBsiiRJ4i2esnHSmGjdhM3ujqwJs2_Gh13-RmlhTJYfA0phC9Pd7gzCOD7adOk7DtVfdyIzF8OJnCdi7MlC5t78HEwoqJjn1rdurnFpVrnNl2a34EVhUDnmoFv3iw21DYoLsg6x1ftPVi6CuxwJh7UNlbG4KQQ3NEmRaHAJerpC82rCg6PtpaOUY5UOXTZjOnloTzqyoUnJV4qj5ATPRxb0Xni_Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
"ياعلي مدد"..
توتر امني تشهده مدينة السلمية في ريف حماه الشرقي بعد قيام عصابات الجولاني باختطاف عدد من ابناء الطائفة العلوية.</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/naya_foriraq/80999" target="_blank">📅 01:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80995">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5noxvQSX4FYhTFdcyzJAfNsI1-hwIAYKOhKg03u3tsW-0R9s4bEl0e7bR7w70jwA7yuYqenDISLE5vFSk3YS6QZ_5aQKWF4UmUU2zmfbxNTpNs68YZJq0TvYmgQ64qUsnrZWPbxTxYcW4OdD1RJjHghnEvAoTLlR2cQGEWZK0CfGeEoNtLrFE8zvAaWPCyZ505bYQfLGWbJMOOfsZtpCDDtmfJ1YC-wvdinp3d9Sxc578-tS9v0ZiZ9WOAC9vBq65YozrxSubHuPuH1pPUUryBHd-N2_D1x9OgC2TH8N5Sr8Mqg6LuoWLs8ge24r0X_ocY7MdEtiRGElPS5tNc7cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ac2ad5e5.mp4?token=LuW-9ZrT0ohE-wwGQ4sMxGGBFe2UZWeZE4qCAsNuCu8XovnVXNY5zE1kBuhJw0QEz-e3iH8--yk4Pp6hoDjLYynwFY3Q3YY1M9kuLlaubm_uy6HC14XuhFWODfXcFqYgn82lkdocJDIGaSWUED3-fuxAo92edzo3FQKcq4ysi6mx-KeUZhok1jKmWzkgdJp0P0ZJxoL1u9NlTaMzdZErtLEqMeYy5A_oj83Dj1nPnn0cflanyPhMd8bfJSjWkW6uwMLXGdFhwOhFo1Nsmw47AoCmUH0x1IOzVYfpBkOkvUFLRpqfo-9juqb1sLkqLVgtqLJiu0rxDYbUS-4Q7gTYig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ac2ad5e5.mp4?token=LuW-9ZrT0ohE-wwGQ4sMxGGBFe2UZWeZE4qCAsNuCu8XovnVXNY5zE1kBuhJw0QEz-e3iH8--yk4Pp6hoDjLYynwFY3Q3YY1M9kuLlaubm_uy6HC14XuhFWODfXcFqYgn82lkdocJDIGaSWUED3-fuxAo92edzo3FQKcq4ysi6mx-KeUZhok1jKmWzkgdJp0P0ZJxoL1u9NlTaMzdZErtLEqMeYy5A_oj83Dj1nPnn0cflanyPhMd8bfJSjWkW6uwMLXGdFhwOhFo1Nsmw47AoCmUH0x1IOzVYfpBkOkvUFLRpqfo-9juqb1sLkqLVgtqLJiu0rxDYbUS-4Q7gTYig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بعدسة نايا |
حشود غفيرة تتوافد عبر المترو باتجاه مصلى الإمام الخميني للمشاركة في مراسم تشييع السيّد الولي</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/naya_foriraq/80995" target="_blank">📅 00:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80994">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c808640a81.mp4?token=XHE7XWMv8wkovYNbVcKgvP38bH20spcGm97cBPLYypBpS3XMV6UiiWR4m4AzAHy7x2in60Bu_Eia9Y_0fj3Azyj3qedNELOoiYEakan6H1xflrvnDDxP6R8IHeeusc4oBH55PbhgygcLvdHf6wvkHdmvt27-x1f-FJEEzHVOJF_lNIQ9ud1evhxf4Dsw0tzOagWVbR__bfMTHn5uuux5lgvp5NDvCmqkaZqUc0tvuhwPl_zjD_CE8OVSieLEYtDb6baW6z42IeFldBU_y9-M4n6BxrEc6fH-E8-lo4UiAaKyDEG3iAErP8judWgw7pkWPUFKi3WSvVq84mrNmoxhuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c808640a81.mp4?token=XHE7XWMv8wkovYNbVcKgvP38bH20spcGm97cBPLYypBpS3XMV6UiiWR4m4AzAHy7x2in60Bu_Eia9Y_0fj3Azyj3qedNELOoiYEakan6H1xflrvnDDxP6R8IHeeusc4oBH55PbhgygcLvdHf6wvkHdmvt27-x1f-FJEEzHVOJF_lNIQ9ud1evhxf4Dsw0tzOagWVbR__bfMTHn5uuux5lgvp5NDvCmqkaZqUc0tvuhwPl_zjD_CE8OVSieLEYtDb6baW6z42IeFldBU_y9-M4n6BxrEc6fH-E8-lo4UiAaKyDEG3iAErP8judWgw7pkWPUFKi3WSvVq84mrNmoxhuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
وفود جماهيرية من حركة انصار الله اليمنية تشارك في مراسم توديع قائد الثورة الشهيد</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/naya_foriraq/80994" target="_blank">📅 00:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80993">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e739239b93.mp4?token=KyXk9ioEZ8ijZlFlWmcu7ePlsygdS1OhxYyTWgbIqiYbwpkxIu_lq-IhMigmrBFYQ-gytacAvy1MslZDrGk4VUI5PCyElfevX-s7TbT4KSsWRxxBZeRaDQ_e74NODIHSFvnq6eJwhu0k2lC-BCf0nbG7lu5zizMlxE4nlmiVZXXub5E1Cras9hv2JOlR96ojT-jt6N7EIKkkt_gvSgsAV5-EQiV0Uzt_DgKG01XXwUb3EJZSODClzYL78eec67NX_lsj9SD_3M3Rn6qmi91hFmTrTuhnol2DTlzAE9jbvuEiMJQPjx4_klL_fgVmoe-zzHxisCkOVPAYz-cA_idz4zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e739239b93.mp4?token=KyXk9ioEZ8ijZlFlWmcu7ePlsygdS1OhxYyTWgbIqiYbwpkxIu_lq-IhMigmrBFYQ-gytacAvy1MslZDrGk4VUI5PCyElfevX-s7TbT4KSsWRxxBZeRaDQ_e74NODIHSFvnq6eJwhu0k2lC-BCf0nbG7lu5zizMlxE4nlmiVZXXub5E1Cras9hv2JOlR96ojT-jt6N7EIKkkt_gvSgsAV5-EQiV0Uzt_DgKG01XXwUb3EJZSODClzYL78eec67NX_lsj9SD_3M3Rn6qmi91hFmTrTuhnol2DTlzAE9jbvuEiMJQPjx4_klL_fgVmoe-zzHxisCkOVPAYz-cA_idz4zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فتح ابواب جديدة في مصلى الإمام الخميني بسبب توافد حشود غفيرة</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/naya_foriraq/80993" target="_blank">📅 00:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80991">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40d71ccc51.mp4?token=CWJNLzJZ9-PihTg7XiFXJD4Q9aMqOi4bGpMqNcE0tAAXQPH5u6LNA-wRWZTxBJP99pfxpUJshVanEq6gorlrJolgQo2SIInc6VY-39xNs2CNROv5Evp9-VQzfVjNwo3Wwcplzf5B1ZAbpjs21VvE0CAain2_HW_vJSoSl4Fpusn2pUfii7R7zLyZR5PERCVuQMzIT8PyD-CxzkXK9tkjfFRd8EaJzZaUtZ8qiveOrJL93L4-uu8hFoKy43Fl1p7lodIBqKvIOfKt-dlRrlR_Tqb0fB9ACRRtvyLSYegrHaucc8UZOIbMU_BR-JxlkcDCi67-7onkxfCW9b-Pgr8hlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40d71ccc51.mp4?token=CWJNLzJZ9-PihTg7XiFXJD4Q9aMqOi4bGpMqNcE0tAAXQPH5u6LNA-wRWZTxBJP99pfxpUJshVanEq6gorlrJolgQo2SIInc6VY-39xNs2CNROv5Evp9-VQzfVjNwo3Wwcplzf5B1ZAbpjs21VvE0CAain2_HW_vJSoSl4Fpusn2pUfii7R7zLyZR5PERCVuQMzIT8PyD-CxzkXK9tkjfFRd8EaJzZaUtZ8qiveOrJL93L4-uu8hFoKy43Fl1p7lodIBqKvIOfKt-dlRrlR_Tqb0fB9ACRRtvyLSYegrHaucc8UZOIbMU_BR-JxlkcDCi67-7onkxfCW9b-Pgr8hlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عصابات كردية تعتدي على العلم العراقي في محافظة اربيل بالتزامن مع قيام الجيش التركي بتعذيب شباب اكراد داخل الاقليم وتهجيره للمواطنين الاكراد من منازلهم وتجريفه للغابات واقامة المعسكرات.</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/naya_foriraq/80991" target="_blank">📅 00:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80990">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🌟
مجلس الوزراء العراقي يقرر إضافة (25) ألف برميل من النفط الخام إلى الاتفاقية العراقية الصينية وفتح حساب لها لضمان سد وتسديد الالتزامات المالية للجانب العراقي للمحافظة على موقف العراق الائتماني واستمرار تمويل المشروعات من الجانب الصيني</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/naya_foriraq/80990" target="_blank">📅 00:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80986">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2Cc1gbAd8eboz-hkqBhQQOVJi2F29R4FIVqStPSHdC_AEUoxIlTOCY9PlbiD1mPZPzCHnBOLFpY2I7McsXeYbHA9yMaDWLsLsECjyK3Or5cvkc0asb9OS1ax_OkTeOwZZb7bGeIEH3BrF0tdmq5GB_K4wpMpZF-3F7F7fXxU4uOKS_ccl_XNaA7i5_jv-P_oCz70qtjQkqVIakinzLkXG2BYVfMD1joBHbkLFK0o1ZudqVOJq3YnrWD5wgi1WTjlwO1cubPyGl4jwfiu7V_2cc8enaiXHzi8KpZqLA247xmQD-QAuc2YsMG7kA0fdIt04DJSN4ntr_yzv1tRmYG_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8b91b0b8e.mp4?token=sv9Cv-bv7AhF2PiCesjgdEMJDMjevqajalWEpgvk83Qlkx3nSioHR88W0c-qiKib8EqGXhxsMGIfIYW4_NC_-lX5FKCfIlKLHx5CQHlFPE2J3Q-lmhghnuQ4Vav1Z8JGUq_MKmG9CaBIMQVmJUSPvYvpLCZv3DwU7VQMSB5npu-6rgSwLcP6FnQdXPR14WOQmfKnYJnMQyjBnOdlvQ5qwS7o2Mehhw2NfMPGVN2CzAsrOU2CBEn6wd30h4ZRXOjRiA72NyIfjR4QQhIp1v_xdtZfWsHgpmFUQ68fvIHyvESSjaXi9oXw-hUEFa_rFV70n7m0iMyWVHVwvpaGpvhsDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8b91b0b8e.mp4?token=sv9Cv-bv7AhF2PiCesjgdEMJDMjevqajalWEpgvk83Qlkx3nSioHR88W0c-qiKib8EqGXhxsMGIfIYW4_NC_-lX5FKCfIlKLHx5CQHlFPE2J3Q-lmhghnuQ4Vav1Z8JGUq_MKmG9CaBIMQVmJUSPvYvpLCZv3DwU7VQMSB5npu-6rgSwLcP6FnQdXPR14WOQmfKnYJnMQyjBnOdlvQ5qwS7o2Mehhw2NfMPGVN2CzAsrOU2CBEn6wd30h4ZRXOjRiA72NyIfjR4QQhIp1v_xdtZfWsHgpmFUQ68fvIHyvESSjaXi9oXw-hUEFa_rFV70n7m0iMyWVHVwvpaGpvhsDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بعدسة نايا |
حشود مليونية تواصل القاء نظرة الوداع على قائد الثورة الشهيد في طهران.</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/naya_foriraq/80986" target="_blank">📅 23:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80985">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🌟
محافظة المثنى تعلن تعطيل الدوام الرسمي يوم الأربعاء المقبل لإفساح المجال أمام أبناء المحافظة للمشاركة في تشييع الجثمان الطاهر لآية الله العظمى سماحة السيد الشهيد علي الخامنئي (رضوان الله عليه)</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/naya_foriraq/80985" target="_blank">📅 23:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80984">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇾🇪
عضو المكتب السياسي لأنصار الله محمد الفرح:
إصرار السعودية على تجرع الخسارة يدل على أن قرارها ليس بيدها وأنها مدفوعة ولا تراعي مصالح شعبها ولا تهتم لأمنها وطموحها، السعودية تبدد أموالها في شراء التافهين في اليمن ولبنان وتراهن على شخصيات لا تملك وزناً ولا احتراماً وتريد أدوات ومرتزقة</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/80984" target="_blank">📅 23:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80983">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">طلب_العشائر_والقبائل_العراقية_تشييع_جثمان_قائد_الثورة_الشهيد_بالعراق.pdf</div>
  <div class="tg-doc-extra">5.1 MB</div>
</div>
<a href="https://t.me/naya_foriraq/80983" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#بالوثائق_للتأريخ
🇮🇶
🇮🇷
العشائر والقبائل العراقية تقدمت بطلب رسمي إلى قائد الثورة الإسلامية السيد مجتبى الخامنئي لإقامة مراسيم تشييع جثمان والده الشهيد السيد علي الخامنئي (رضوان الله عليه) على أرض العراق العظيم؛ وتعاهده على مواصلة السير على نهج الإمام الشهيد والتمسك بالمقاومة.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/80983" target="_blank">📅 23:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80982">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdQxI0niwbEyMZzBgMIp5P7TryWq_hNp2gBsBEXH4yyJof4f50CYtED-4zKcZCKffCg0X4EngBEyx6sEF4K3Ri008F33zMwOETdVvi5pHlLHqYP3wjH_y-MDQoJGlQnMHzvIOeb2y9ZuUrW1fqhHkfINBulEVCSkkQIgQrOA9mdWyXPP0YsV-4xJehIBcGuE-BPUKCaz_hKlteSlJYliAV4cd38Tcn5G7KG09fbVaotidL9Krp5035EXtnXuUmOxOmzSS67sB-SPnQU9nO9yi-mir2gW5z1vTgEaGxU6RT7mapvVs-SbONdxNKLxrdcrtMPalJybs4fR6mVh0ey6Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
تعلم أوروبا أنه عندما تستقبل مجرمين من العالم الثالث، فإنك تصبح دولة من العالم الثالث. يحدث ذلك بسرعة، في غمضة عين. تم انتخابي في الوقت المناسب!!!</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/80982" target="_blank">📅 22:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80981">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇲🇦
المغرب تتأهل الى ربع نهائي كأس العالم بعد فوزها على كندا بـ3 اهداف مقابل لا شيء</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/80981" target="_blank">📅 22:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80980">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldMaYMV6YxjCbz7artujpRgpK9IVTbL0d2MKJ8RG5sQVdeBhkFoG-PIMPp6pI6ya2RWF9adZd49BR1FthY6WFAF4S0sFoOBn8-B8H4LZ-dRVU0-yl12VkJAk6WKqWf8uLULw8iTdLOI85Aae2oSdamNT2max79cFBEqoZi46mbOlXDyj9Sv_3esCMlcILb1pHQkGbzqVlUUHXwohhzkQrAe8L7Kl1FVzsfMKIkqrsQZWkZAqE0YX2E0opOc6KSygeHC9V_6e_YYwLVPHzg2JuFYLOeCnWG8LbxyVbxAe3WlLdVzvYx_tP4i14jsvg3hNcHuuRUmbXLQP_K5ZLszmbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني عباس عراقجي:
‏يسرّ إيران أنها استقبلت ممثلين من أكثر من سبعين دولة ممن اختاروا المشاركة في تكريم قائدنا الأعلى الشهيد، آية الله العظمى خامنئي، ومن بينهم إخواننا العرب الأوفياء. ‏وسيظل هذا الإحياء التاريخي ذكرى خالدة في مسيرة علاقاتنا المشتركة.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/80980" target="_blank">📅 22:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80979">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMBS0yqLlFH_oHgCzPhp1jn_SMwte8usRU7iaN4BiBcl3y8Ws9UQ3dm4LIs1_ocsAWdrqykyzasLkN3xQZAyTKfxp4PqZOvQh417u6bFpBcAAa5L45XmC2zk0nk_hdoWrTZ5HC6PQiE8fYeZUTeEj4lHknPZLUIYniK-CQYkteuYtJ7lddjTouFe8FBXNGP8aI8WWRqCSFQb_3dOzFJLmWRsN2AYbXWiCkpcE6XrfNLgEApwqVofyNPCF9zH5aj9qCiNq3j7T7xtB7vVW1JrK0HffotnqZgtCGheQtd_Yq_euC2-LBR1dFTTzDZNaPsER6J3QMYtyJMKxcLKIqTgPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
بعد اغلاق ايران الممر الذي وافقت عليه الولايات المتحدة لعبور مضيق هرمز.. عدة طائرات تكتيكية تابعة لسلاح الجو الأمريكي تحلق فوق خليج فارس:
‏- طائرة إنذار مبكر محمول جواً من طراز E-3B عدد 1
‏- 6 طائرات تزويد وقود من طراز KC-135R
‏- طائرتان للتزود بالوقود من طراز KC-46A</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/80979" target="_blank">📅 22:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80978">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a987a11e90.mp4?token=HMHdQD27hRwsBRxbds956Zfv3TBDQCSft7cM-r-_0Gr_fbYAeT1PDNgs5CDFXe9noH2Lu-FPs1bKoo1I9J_VLpd7fPZihBUoMuEECpvBaba27lGOC7iDByWUXklP4L2DkMVEUacvPQO5aEKtKESiEc0cN4-jpiKNyK9HpXIku4u2VKH4H2GVeKeLfyAO7Pp3G_gGJdFA8uiBRLEafJRSDGcgTy4lgxkpgcVKLLH2iM0Y6vXuBUmXUDqpKhtLfYcKm8hjtiX7qgMCmAvDlzsgZsgVjkx58meLEGkN-Ou8V1g0MkLGeOeRGwHuCPSkcLqXuZTLsab7n6G-3C62mz45Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a987a11e90.mp4?token=HMHdQD27hRwsBRxbds956Zfv3TBDQCSft7cM-r-_0Gr_fbYAeT1PDNgs5CDFXe9noH2Lu-FPs1bKoo1I9J_VLpd7fPZihBUoMuEECpvBaba27lGOC7iDByWUXklP4L2DkMVEUacvPQO5aEKtKESiEc0cN4-jpiKNyK9HpXIku4u2VKH4H2GVeKeLfyAO7Pp3G_gGJdFA8uiBRLEafJRSDGcgTy4lgxkpgcVKLLH2iM0Y6vXuBUmXUDqpKhtLfYcKm8hjtiX7qgMCmAvDlzsgZsgVjkx58meLEGkN-Ou8V1g0MkLGeOeRGwHuCPSkcLqXuZTLsab7n6G-3C62mz45Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الحشود المليونية في طهران تطالب بالثأر</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/80978" target="_blank">📅 22:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80977">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
وفقًا لتقديرات الجيش، يوجد حتى الآن نحو 1,200 عنصر مسلح جنوب نهر الليطاني.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/80977" target="_blank">📅 21:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80975">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">⭐️
خوفا من رد فعل إيران.. إعلام العدو:
نتنياهو طلب تأجيل العملية بمنطقة علي الطاهر جنوبي لبنان بطلب من ترامب.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/80975" target="_blank">📅 21:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80974">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7783221b7.mp4?token=Q9mH8zUTPUG6OjTiFzmIrgbT7DFhvmiBFQMjgCznNjM0NI12yG4TCDYjeZYezldZvANmpOrROfULWVnop1HR3TitszkYcWDmfGx5kg4vp9UCu3PAdjGHGK-xnoh8sHOx3oWfUm2xxJ5jalHDud8pBlYE6OYWlYbBxWxsaddaAcTJE3odej6Lu8a1WipPhD3-8dsvwmXqo6wtIUaajehGvYyP-YFTOnZBUcKl7WjPyTagrXZSj-l0NLMFvbQVGVH-Wqb3xfKJxufzeq0d9R_g2H_OwIOMeOG0mbBbqS2M9cKYe2mLjLHh4DzkjzGKYsFNryTfZvhWoegRM-l4JwC96UTcq7y1R9-m34zZX6ojxIdx_W9psb1iYAM8hj3l4C4uoea7KkYKOhUmSZbTUhdKDVG0GtA9I9dc9vX_VCfc-u370hILfQd9Go6Kbm9NApHvNY6eETTmJZIRXiQVr_QS2WAzr1mkDMvBxJeGeATRwQLEUYkqmf-fG4kS4-ZL1JgLmDGDsYXW60JWsl4MzH6YC_I-WT0y905mRZ5ndNxn_CGqNmfwZqDOyqAzRlAvZOv7TISHU2DJQqXbOBsrUnGPEYRgP3Ff25UPKkLJP8KNLIUc8E1VGwxUtsQp-_lxIgDoRVj792_qX6iBKOIUONuoKxKBOuRo5cSQdOwInu7JbFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7783221b7.mp4?token=Q9mH8zUTPUG6OjTiFzmIrgbT7DFhvmiBFQMjgCznNjM0NI12yG4TCDYjeZYezldZvANmpOrROfULWVnop1HR3TitszkYcWDmfGx5kg4vp9UCu3PAdjGHGK-xnoh8sHOx3oWfUm2xxJ5jalHDud8pBlYE6OYWlYbBxWxsaddaAcTJE3odej6Lu8a1WipPhD3-8dsvwmXqo6wtIUaajehGvYyP-YFTOnZBUcKl7WjPyTagrXZSj-l0NLMFvbQVGVH-Wqb3xfKJxufzeq0d9R_g2H_OwIOMeOG0mbBbqS2M9cKYe2mLjLHh4DzkjzGKYsFNryTfZvhWoegRM-l4JwC96UTcq7y1R9-m34zZX6ojxIdx_W9psb1iYAM8hj3l4C4uoea7KkYKOhUmSZbTUhdKDVG0GtA9I9dc9vX_VCfc-u370hILfQd9Go6Kbm9NApHvNY6eETTmJZIRXiQVr_QS2WAzr1mkDMvBxJeGeATRwQLEUYkqmf-fG4kS4-ZL1JgLmDGDsYXW60JWsl4MzH6YC_I-WT0y905mRZ5ndNxn_CGqNmfwZqDOyqAzRlAvZOv7TISHU2DJQqXbOBsrUnGPEYRgP3Ff25UPKkLJP8KNLIUc8E1VGwxUtsQp-_lxIgDoRVj792_qX6iBKOIUONuoKxKBOuRo5cSQdOwInu7JbFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
استمرار تدفق الحشود إلى مصلى الإمام الخميني في العاصمة طهران لوداع قائد الثورة الشهيد.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/80974" target="_blank">📅 21:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80973">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حضور القادة التاريخيين للمقاومة في مراسم وداع قائد الأمة الشهيد
من الإمام موسى الصدر إلى نيلسون مانديلا وغيرهما…
أحرار العالم في خيمة الحسين ع
#قوموا_لله</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/80973" target="_blank">📅 21:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80972">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddef9fba30.mp4?token=P-Op3RA6oSWJ_ibXNxEnIgS__ULxt_SwUxeM0qbuv7MHTUFoZvS3ahp6W8yGAQbb0k0BzXAI5ursM2i4kQfMv-YwXkjhzaT2YUJoJPqOToJH9mLunNNybxRXRSBv1QlQflMchLdx6tNh8WmKVVeLcaRUvewUrZd-Z_tTUEjd3maBSFUWC9mVMbY22IiR1xMctlvwRxwqYpuLbqCCb0g95qA2ViYJ8kKjZOPMNDNhjG9wlEDCvqz8NQPucJKSzKU_9hOuLejiVOJZn8zeA10ZduADcsrKcgogWjfoeMFHl14b-Ea1Y4XKGb_evWiORwQiRQ1HtwP1Us-o0OGJdYYTeQ3Myo0tXPZ-WQu31AwHNKtOL6QEGnVGdmUHXUElEXCsa8E8rFBwaCFjNSQ6qufshEaEMJglR_tubUFPuHkdoZyliYJPxMeAT3jmAfaaHVTlHCCyIP_KhL8xVMVkl7RClTdwCpJ7S5_yip3PKyEJd83BlGNtA0rC843gE0RqPT3INMJWUWlaLuYXK7VSjkhQcghPZd7bzHm5jXx7hucd6s-mmWcSLheTb6WGDIj2qiTEUqE8waMm6RjVcxX-eYD6GPywAfm0ld4yHTT_h9P6yZKu3BvfaqepNwh-ZQjSgGhW27aJKK_j0DqxueO7Vqcihy9ep9MbuFzGOmoCNU15iOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddef9fba30.mp4?token=P-Op3RA6oSWJ_ibXNxEnIgS__ULxt_SwUxeM0qbuv7MHTUFoZvS3ahp6W8yGAQbb0k0BzXAI5ursM2i4kQfMv-YwXkjhzaT2YUJoJPqOToJH9mLunNNybxRXRSBv1QlQflMchLdx6tNh8WmKVVeLcaRUvewUrZd-Z_tTUEjd3maBSFUWC9mVMbY22IiR1xMctlvwRxwqYpuLbqCCb0g95qA2ViYJ8kKjZOPMNDNhjG9wlEDCvqz8NQPucJKSzKU_9hOuLejiVOJZn8zeA10ZduADcsrKcgogWjfoeMFHl14b-Ea1Y4XKGb_evWiORwQiRQ1HtwP1Us-o0OGJdYYTeQ3Myo0tXPZ-WQu31AwHNKtOL6QEGnVGdmUHXUElEXCsa8E8rFBwaCFjNSQ6qufshEaEMJglR_tubUFPuHkdoZyliYJPxMeAT3jmAfaaHVTlHCCyIP_KhL8xVMVkl7RClTdwCpJ7S5_yip3PKyEJd83BlGNtA0rC843gE0RqPT3INMJWUWlaLuYXK7VSjkhQcghPZd7bzHm5jXx7hucd6s-mmWcSLheTb6WGDIj2qiTEUqE8waMm6RjVcxX-eYD6GPywAfm0ld4yHTT_h9P6yZKu3BvfaqepNwh-ZQjSgGhW27aJKK_j0DqxueO7Vqcihy9ep9MbuFzGOmoCNU15iOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
قصف جوي مجهول يستهدف حدود بردي بمحافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/80972" target="_blank">📅 20:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80971">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51c217e1cd.mp4?token=lkSpLab03IHxFKzvBcslWgpHM8gAQ32j0fvQdaZn-qT8lYWXiWLHc17iago6H7BQiVzGLQU_HHhJg2Rz6sVByOM3RCUUQkJ6UNOLJ7LtCxdHnHgtn3B5ExLvixbYr13KJzhEyJ2lCSI8Hrj6gXMmPAEXpt6xVyRxG2cRJFlXO2HsjJVn5bj5O8RyG8s7Zap2g6o1kH4bK0sm8WkBdP3Jc6GGiCy9kIGcLvFEAhn_zCaIBGHVIriK493UzV4EcAyHKjsE0Oaq5EumXyZKmVNsozO6dHzSJAyII9R_wN9rgusW7W287jrFh7e6CNIdFK7sd7iiIcUvmf7i3U4TlDUPy0TZ7V7fY1u33kXOZjxv29pchiaHgdyZwUwZ5K-tTVxq4sOM2dP_954lJYGtDjytxC0IWbpAp5sAYvELmZDJ6m-bLbYUkQjvZQihtufPBI3KsUfy7SdlIHcGRXfBuUjYfUSQsH_UeYppk7KbtOAuuCb4HkAo6AzACdyNG-QwdbqObmZIwP1cVURKlUgFgl4gwhu10pEL3SJ493zZG5JF73XMwb6KEcB3cnfQ2YYuHogrB7pfYOaa4w_M_7kcTSvMCx4Ttzh7cmxauRivaf1htO9hvb3-L7OUEpU55fXK7PAfBrXEnAZKvZPqOVXwr6Mdjgj8XKerKvhKRzpXzcId9-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51c217e1cd.mp4?token=lkSpLab03IHxFKzvBcslWgpHM8gAQ32j0fvQdaZn-qT8lYWXiWLHc17iago6H7BQiVzGLQU_HHhJg2Rz6sVByOM3RCUUQkJ6UNOLJ7LtCxdHnHgtn3B5ExLvixbYr13KJzhEyJ2lCSI8Hrj6gXMmPAEXpt6xVyRxG2cRJFlXO2HsjJVn5bj5O8RyG8s7Zap2g6o1kH4bK0sm8WkBdP3Jc6GGiCy9kIGcLvFEAhn_zCaIBGHVIriK493UzV4EcAyHKjsE0Oaq5EumXyZKmVNsozO6dHzSJAyII9R_wN9rgusW7W287jrFh7e6CNIdFK7sd7iiIcUvmf7i3U4TlDUPy0TZ7V7fY1u33kXOZjxv29pchiaHgdyZwUwZ5K-tTVxq4sOM2dP_954lJYGtDjytxC0IWbpAp5sAYvELmZDJ6m-bLbYUkQjvZQihtufPBI3KsUfy7SdlIHcGRXfBuUjYfUSQsH_UeYppk7KbtOAuuCb4HkAo6AzACdyNG-QwdbqObmZIwP1cVURKlUgFgl4gwhu10pEL3SJ493zZG5JF73XMwb6KEcB3cnfQ2YYuHogrB7pfYOaa4w_M_7kcTSvMCx4Ttzh7cmxauRivaf1htO9hvb3-L7OUEpU55fXK7PAfBrXEnAZKvZPqOVXwr6Mdjgj8XKerKvhKRzpXzcId9-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الحشود المؤمنية المشاركة في مراسيم توديع إمام الأمة تقيم صلاة المغرب والعشاء في مصلى العاصمة طهران.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/80971" target="_blank">📅 20:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80970">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🌟
المجرم ترامب: أتابع مراسم تشييع خامنئي وبإمكاننا القضاء على الجميع لكن لن يبقى أحد للتفاوض معه.  نحن والإيرانيون قررنا أخذ استراحة لمدة أسبوع من المحادثات إلى حين انتهاء مراسم التشييع.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/80970" target="_blank">📅 20:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80969">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🌟
المجرم ترامب:
أتابع مراسم تشييع خامنئي وبإمكاننا القضاء على الجميع لكن لن يبقى أحد للتفاوض معه.
نحن والإيرانيون قررنا أخذ استراحة لمدة أسبوع من المحادثات إلى حين انتهاء مراسم التشييع.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/80969" target="_blank">📅 20:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80968">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇶
محافظة ميسان تعلن تعطيل الدوام الرسمي يومي الأربعاء والخميس وذلك لإتاحة الفرصة أمام المواطنين للمشاركة في تشييع الشهيد السيد علي الخامنئي رضوان الله عليه.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/80968" target="_blank">📅 20:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80967">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5e0993873.mp4?token=bVkqWzMTqMYbfO6ZvkTscA-afhrz1tw610BD4bnRGlH_jTVWc_jbw8ZHPDNpB_zIta_a3mWZ1HRFb7EmLkjGSGsZpiRSfdxiAcLMlveUfsENRgp-YA6tlJplO665sKUFPr9DOE2jSIl50QCdTZPhhAarFNisu8wRjWtt7nV9hcXMKT3zbIVJYbmsG42Fsu4Q6h8EHwhWT9VIZy0gall7oi7BmPfmE09DQb4EfWilTFXR7dNmBqwPL6CsJdF2DlXvmAC31SvCXNoEKdttzkIuF3lGGc8Ylwoe8AYJI1V77q53_MIkFYejho-hu294DZH3U6IZ2hEg9D73VHMfhLECkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5e0993873.mp4?token=bVkqWzMTqMYbfO6ZvkTscA-afhrz1tw610BD4bnRGlH_jTVWc_jbw8ZHPDNpB_zIta_a3mWZ1HRFb7EmLkjGSGsZpiRSfdxiAcLMlveUfsENRgp-YA6tlJplO665sKUFPr9DOE2jSIl50QCdTZPhhAarFNisu8wRjWtt7nV9hcXMKT3zbIVJYbmsG42Fsu4Q6h8EHwhWT9VIZy0gall7oi7BmPfmE09DQb4EfWilTFXR7dNmBqwPL6CsJdF2DlXvmAC31SvCXNoEKdttzkIuF3lGGc8Ylwoe8AYJI1V77q53_MIkFYejho-hu294DZH3U6IZ2hEg9D73VHMfhLECkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الحشود المؤمنية المشاركة في مراسيم توديع إمام الأمة تقيم صلاة المغرب والعشاء في مصلى العاصمة طهران.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/80967" target="_blank">📅 20:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80966">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427bde8bb7.mp4?token=lXfBMIVd98vD53x8V4AH6flllvfcxR9p248sY2H6Rc-a2qDC48Yalf-PATNzPoSaRwJLO9AudCFqFCMr7aCcJzSCVXjEXM11OpaRtBMHR7Yha6oF_Ry_Ncg9Kw2aJB-30YJYign66cVu8RLr9YilIwF7AutMnkxzb4gP8HcgKr6Xwg4vsJq_tpzSSuU5QTiWCYU9dci_uRT3LYJjvesLRJO-_k3dmd3LICMmvMqrPLEi6cviMpN-AymeX0_5Fng57gnqwyB7R0xwlPXgdk-Hu4RijwHbtjhg5nBekknzHbj-RWMqYyre8QHqMDyAF2V5IYqx0QK8Uz-tf0AFHqthbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427bde8bb7.mp4?token=lXfBMIVd98vD53x8V4AH6flllvfcxR9p248sY2H6Rc-a2qDC48Yalf-PATNzPoSaRwJLO9AudCFqFCMr7aCcJzSCVXjEXM11OpaRtBMHR7Yha6oF_Ry_Ncg9Kw2aJB-30YJYign66cVu8RLr9YilIwF7AutMnkxzb4gP8HcgKr6Xwg4vsJq_tpzSSuU5QTiWCYU9dci_uRT3LYJjvesLRJO-_k3dmd3LICMmvMqrPLEi6cviMpN-AymeX0_5Fng57gnqwyB7R0xwlPXgdk-Hu4RijwHbtjhg5nBekknzHbj-RWMqYyre8QHqMDyAF2V5IYqx0QK8Uz-tf0AFHqthbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای خامنه‌ای خداحافظ
السيد الخامنئي… وداعًا</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/80966" target="_blank">📅 20:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80965">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSWWGr9PxXr49QmH0klpFruivVkWtJ7eTrFzUXy_G-Hv-fE3Rso3rZkl7KY604Hzz8DQGjuYpv60NuzLGtq_xJ_w9pyxAb6ZxrfD1GB6ONx2TA6PdmbmREKzCcGEzLo30zjGBfKyRlBA-Q4QQFoqzUVVSYbPF_CTNFbfCbxHkwTFcXbNZyKqk15rOh0LVtkuAeX5WWhjhsUBltUt9L31jvKEBIbA3jWj2rB__wcjiWodRm39h6Tph4huHEpY0EqtC9l_pEnjNGX1EQLGw_IqHyytos1Hd55_XIthAAL18AITGw-0Mm2Z9rSZgVtx_7Z6Uy4NS3-CheIRr5uLlS9-tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الأمين العام لحركة أنصار الله الأوفياء الشيخ حيدر الغراوي يدعو إلى المشاركة في تشييع جثمان قائد الثورة الإسلامية الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/80965" target="_blank">📅 20:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80964">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني مسعود بزشكيان:
نحن المسلمون لن ننحني أمام الظلم والطغيان.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/80964" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80963">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e792efbf43.mp4?token=bggZY-D4FwXOrwRc1J0YSI9zEA_hYTfGD580vuZGzK4Hrgn0zjXUvOOBPh1Ib2cnuKtGd1AhL7ddUEFS-qZBTOWJfiQsHbZ_5HTo0Q64g1ActnrngG1-waA7JVsI56drWusxgmf1Fc7uTYwcUak3LdLkfNRmDSwbC0wHT59_qOs8fCL-Hf_6CmYsk29qMQnaYPYrt-XX4CyieW9dqIimBGRDGF8mB1qgRfntPnfttQPlY8ivxnevGObFZcjV-P7QEuC5LdVCF2PdHzZAQMDPDeWW9_YGfsjlHyaM0MhvQ13E1dgUq2eC5NOxoxNHkP73T1eo1wmNYhQ18PZ1uNyQ-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e792efbf43.mp4?token=bggZY-D4FwXOrwRc1J0YSI9zEA_hYTfGD580vuZGzK4Hrgn0zjXUvOOBPh1Ib2cnuKtGd1AhL7ddUEFS-qZBTOWJfiQsHbZ_5HTo0Q64g1ActnrngG1-waA7JVsI56drWusxgmf1Fc7uTYwcUak3LdLkfNRmDSwbC0wHT59_qOs8fCL-Hf_6CmYsk29qMQnaYPYrt-XX4CyieW9dqIimBGRDGF8mB1qgRfntPnfttQPlY8ivxnevGObFZcjV-P7QEuC5LdVCF2PdHzZAQMDPDeWW9_YGfsjlHyaM0MhvQ13E1dgUq2eC5NOxoxNHkP73T1eo1wmNYhQ18PZ1uNyQ-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
قصف جوي مجهول يستهدف حدود بردي بمحافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/80963" target="_blank">📅 19:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80959">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef85f6290f.mp4?token=gZLv5xSg8olEzE0UkMBEbyhVdmkOQClXAaKBUi3n1p-Vom43oPjToGh79CiLZfTd360xW4VQE3cC6q5AYYrRRaK0h8eFtMjzOkHcVHm3wRh_D-uLQhaFwryKp3hLvwR60Qt6eTxpHXEIvuOOkvtmeDie_SZ4C7wXk2EC7xQo60MmugkYvQqYUlEQHfg-SQI6C-VS5yqOrBIrsRRkqcwwFArvrNQYdJtS7RrMTFWbksyhpFBHLIgXDBpwFllcfwHT_Tfb2IOu1SHpcHrHn47AwEtY46I0fAp8PjXW0OY1X04w1KkayWy6FsOSUI2ceZluwY7uY0jU9Y5U-y8cuwbZ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef85f6290f.mp4?token=gZLv5xSg8olEzE0UkMBEbyhVdmkOQClXAaKBUi3n1p-Vom43oPjToGh79CiLZfTd360xW4VQE3cC6q5AYYrRRaK0h8eFtMjzOkHcVHm3wRh_D-uLQhaFwryKp3hLvwR60Qt6eTxpHXEIvuOOkvtmeDie_SZ4C7wXk2EC7xQo60MmugkYvQqYUlEQHfg-SQI6C-VS5yqOrBIrsRRkqcwwFArvrNQYdJtS7RrMTFWbksyhpFBHLIgXDBpwFllcfwHT_Tfb2IOu1SHpcHrHn47AwEtY46I0fAp8PjXW0OY1X04w1KkayWy6FsOSUI2ceZluwY7uY0jU9Y5U-y8cuwbZ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
آلافُ المعزّين يكتظّون في المصلّى بانتظار انطلاق مراسم التشييع.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/80959" target="_blank">📅 19:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80958">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHFSofMZzOTwYVODctsFn3amzS9yxQRMjlohOVcf6YKRFJSVIhbzfSX8CpPbV0t_1fpa3S6FXu9RynnuNqtq3btyBsncCf20R_rty6FLsKIYMUjnlaPzNnOV37bDrEpIssJ94QoxViEyqhD6j4fbVuMDlA1E4qgsCgeYMvO5mt_jKDhVm12JDqND9fDr3GHLfJuQbcGS_Vl55vT3dByWJ2gvKEfIv7nZWpIVFGBAnlqrAFbC7gcTyYlkQO_p26nPvXBG8hj3WLRS0pk8WoKgZJoLzchum1zZzMTeaBQmswq4zZyiw9wYNxv4SrU1_1XQjaa_AnalRmzn9ODLNv019g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
قصف جوي مجهول يستهدف حدود بردي بمحافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/80958" target="_blank">📅 19:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80957">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔻
‏سفير إيران في الصين:
بكين ستحصل على تسهيلات في مضيق هرمز.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/80957" target="_blank">📅 19:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80956">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔻
مفوضية حقوق الإنسان في محافظة البصرة تناشد الجهات المعنية بالتدخل العاجل لإنقاذ عراقيات عالقات في الكويت بعد سحب جنسيتهن مؤكدة أنهن بلا هوية أو مستمسكات ما فاقم أوضاعهن الإنسانية وحرم بعضهن من الحصول على الخدمات الصحية الأساسية.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/80956" target="_blank">📅 18:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80955">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDfq_WFhS_ECdhlA5cfhj4hgfCU6oL4wgwN3GdtVSvW2Bv3z35e7PXXBFp-Oy5MeQ8ilCgheRicCY2-G1SROl79qe3UnX8kvJqU3j9Jp4M1nCcNOU2taFuERXG9Me16cAUToZ8esipnE-UW9XracDxdeLW24yOEXJmjhOE4hoaKCyKSfQ9qFkakuQ0-IwQNzf08EVH-lCe-eocjJIo6akGGRbA1T7uMRltaHVjq52YRyZV6JV1fMiA9WYLbLTx7uH3cgCyMX02KnlsZb6pyB5nYFcqpBFEVhNOhk_kVUNytHy94u7fSW3YjsVeNEcsJInaEa8syFViBJs_fu5Ercjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
آلافُ المعزّين يكتظّون في المصلّى بانتظار انطلاق مراسم التشييع.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/80955" target="_blank">📅 18:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80954">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔻
أردوغان
: يجب عدم السماح للحكومة الإسرائيلية الحالية بأن تفشي رائحة البارود والدماء في منطقتنا مرة أخرى</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/80954" target="_blank">📅 17:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80953">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqOl-US87Abm8duuql7z1LH7u9Uvd-lSvewVU355zMo4DUVJYfcr5WFCxfSTruC9EkGnilfOnwYg6pyJyDx9kV-qKEkvVTC0ydIfD-15PS_1eLYW7BNcwpAnV56LQ97eiutxKqw8dk0RAfZp1n3O3Cx2Sz56b7f894zGfMQT6sArxccioXAzGU0ZZzZBTLjdZKzUSjIhNqPLUbY8pwskf11kCgh9uC5TXu2tTjkle5qi6hFdPSF0ivBz8eXIl-x37sSkYJ3M36B5DP_kY2rx9Ko0U2F-pBflT1SeoO_oDbezMk49HFOoKqpc5ZUAJFfUr5i2opLXZpcRxEwW_JSd5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
في غضون ساعات قليلة، أغلق الحرس الثوري الإيراني الممر الملاحي المدعوم من الولايات المتحدة تماماً، لا تعبر أي سفينة تجارية المياه العمانية لعبور المضيق.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/80953" target="_blank">📅 17:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80952">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721fa47854.mp4?token=Jz77bC5kckI_7V5kQzrkcJd_T8leyHVVXCpfeAcMeeCWAeqVzfSUqPnjJaIo5il2eK4BVlSHbIqdVSSQWa5A06VivpQ36g-NsXJ_gshBbxt_L7SC0owg-ekiuhimTXHTjxuUizwyVF3wXMevW5ZXfxq4pFTOjeTlbXiW94ItnnnUp5FNJXLWnGVmhoZWckQS_IP8X_wJOTHkrgdEmGpfJkRfOP5bI1eITshuc0dR4iSObPOVuv0RTlmw4c44HbH6TRM92jyRXEsRodYakerLfjSPLR6w55sIuN0i0qq45tHwsQ8cVOlmSuR3xZmk-7qgQlnF15D8K3QGZXkD5n99tJxIhgHRVM8z0rBGofpgMTd9YhxU-dv2cVrJtOS0j-IBMiQkNH5ZJ9G7tVlCnmSd6BZt3MMd6hfq3bR9FdBPh95Qb6QiDh_q6QsgeVg78ArrJ3AXaA34bJ01y31GRqLkueFKwIWnl-LBwvD4v9zPNmjjrQTu-KGoGXqSSI4_9X4r36HLZDQMJr9Yp_VaB_Icbf2spzHXvK6OrE4mzewyJ87BvVue3cg719QEt2EThdygdyqL4_oIXpjvppAp-Ma7vKPBKyWMEAvbEfgggOmwHksbnJM99H6La6OyT5nWUTUgclJNozOnn_AWtydik7tlDKomOsJyJ-X1bvbSNEh05es" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721fa47854.mp4?token=Jz77bC5kckI_7V5kQzrkcJd_T8leyHVVXCpfeAcMeeCWAeqVzfSUqPnjJaIo5il2eK4BVlSHbIqdVSSQWa5A06VivpQ36g-NsXJ_gshBbxt_L7SC0owg-ekiuhimTXHTjxuUizwyVF3wXMevW5ZXfxq4pFTOjeTlbXiW94ItnnnUp5FNJXLWnGVmhoZWckQS_IP8X_wJOTHkrgdEmGpfJkRfOP5bI1eITshuc0dR4iSObPOVuv0RTlmw4c44HbH6TRM92jyRXEsRodYakerLfjSPLR6w55sIuN0i0qq45tHwsQ8cVOlmSuR3xZmk-7qgQlnF15D8K3QGZXkD5n99tJxIhgHRVM8z0rBGofpgMTd9YhxU-dv2cVrJtOS0j-IBMiQkNH5ZJ9G7tVlCnmSd6BZt3MMd6hfq3bR9FdBPh95Qb6QiDh_q6QsgeVg78ArrJ3AXaA34bJ01y31GRqLkueFKwIWnl-LBwvD4v9zPNmjjrQTu-KGoGXqSSI4_9X4r36HLZDQMJr9Yp_VaB_Icbf2spzHXvK6OrE4mzewyJ87BvVue3cg719QEt2EThdygdyqL4_oIXpjvppAp-Ma7vKPBKyWMEAvbEfgggOmwHksbnJM99H6La6OyT5nWUTUgclJNozOnn_AWtydik7tlDKomOsJyJ-X1bvbSNEh05es" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">٨ تمّوز... موعدُ أطفالِ العراقِ للوفاءِ للسيدِ القائدِ الشهيد...
بعدَ سبعينَ عاماً من الشوق.
إرفع قبضة يَدَكَ | أَنشِدْ قُوموا لله | وَاحْمِلْ رايَتَكَ
🚩
🚩
🚩
#قوموا_لله</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/80952" target="_blank">📅 17:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80949">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce101f4641.mp4?token=IJq5sFIDSypAEnJD5ZEhv4Ilm4eCNM-s08lVx7pjBImElgPBrqV6pQHOq2IEXlKlggwowl42vmsVBaxiIzrZhd4OTgg9xlFwx8fA1Tt7pjAImLWOe1Qbr31rDdg2hvOwrH8TgW-L5XDKhzJXX6h-WVjAvzuGtQug-gQnZMdfzp-HkVOlvDKQAYwgMpIO791SMXPZ6mD094b-7m3_hF5BBdYmDUZL_jcBCdSizUy5Q_VLeanjEmSm7h_75Vl86_BqW_88aaSGtPi7h1PCA0LEVV1hhe9JlKdT3MfQmYW5pb6SVHGA-_W1_MiPuY2-0qyzy5vobc-yGuS7nWJoCaLU4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce101f4641.mp4?token=IJq5sFIDSypAEnJD5ZEhv4Ilm4eCNM-s08lVx7pjBImElgPBrqV6pQHOq2IEXlKlggwowl42vmsVBaxiIzrZhd4OTgg9xlFwx8fA1Tt7pjAImLWOe1Qbr31rDdg2hvOwrH8TgW-L5XDKhzJXX6h-WVjAvzuGtQug-gQnZMdfzp-HkVOlvDKQAYwgMpIO791SMXPZ6mD094b-7m3_hF5BBdYmDUZL_jcBCdSizUy5Q_VLeanjEmSm7h_75Vl86_BqW_88aaSGtPi7h1PCA0LEVV1hhe9JlKdT3MfQmYW5pb6SVHGA-_W1_MiPuY2-0qyzy5vobc-yGuS7nWJoCaLU4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
كل بقعةٍ في إيران تهتف الموت للأميركان.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/80949" target="_blank">📅 17:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80947">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tckCTWEWiHUb2CL_9L4qHctX7kyu-p-hm96oz06aFH42U9h6T1yyszerZ7R1J807LpzTPb6fXipPNE9dXEmGmt4wFQhlXhRhKy1yOTBn2jHp6GngqQOWYW1gtlKVH2Fqd8H5mYb3JIbODXUQH0HTBGVCEsrD4TQIaKm-hZoRTIhe4HtJEN-Q4nm4lyV-pTC_l6IfDbsKdS5R60UfHcy8BQVxfXC4yfPz6U8ZncFLixUViRHjRMBgfddswf1I2A5BJWa4nF03IUJI2z6F8uPTYhJEtaGzQChLL0VzBpYSFGjHIE5JdfOEm8KlYhJ7TCAXDYXxvi5FUcF2L41vpDXYXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
الإرهابي الذي قتل خلال الإشتباكات مع القوات الأمنية العراقية في كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/80947" target="_blank">📅 16:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80946">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔻
أعلنت وزارة العدل العراقية استرداد أكثر من 25 مليون دولار من أموال العراق المنهوبة خلال العامين الماضيين، مؤكدةً مواصلة إجراءاتها القضائية لاستعادة الأموال والأصول المهربة في الخارج.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/80946" target="_blank">📅 15:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80945">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPLQv02PFDmzElnSV9xDXXd0KHoWkwBZSAfTtEKC9q2cXKx2ecYumt03612joH51jOgsWp-ACmDzF-wA4xYsrhcbM1ynkR0d1cylzuIV9zHHc217H1pSn5xXoDbvUF-eTutCH-ziNjQBA7IA1GGUGdNM9LFZ-UZJGtMIM_rTG1BZ8pk7srLZrnQKlK0s4xS2ICu9CG5pH_Qdfc-CdSxdfvXshhx9gxLBJI7o8mJuohiHsapTDk8KwVMMpivq-mMg1CR6F8dt_GfSCl6WFbki7_Uc5R8aFoLcB8djgcQdfZDzE-CT0CZdntuG4AaHXzqNWizq86HL_Rc3IAtv7KcmmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
القوات الامنية العراقية تطيح بتاجر  للمخدرات بحوزته 14 ألف حبة كبتاجون في بغداد</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/80945" target="_blank">📅 15:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80944">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0532608c1e.mp4?token=KNDBbpBXl1V_7DQIjzl81TIaYnCL84EDTltauCKheSdk6Dbi_RW5QFklRsZ1axUGTWuEbEV16g7ih1E2xNfhaixPQSS38w044cyvtI-rb8cmzJAP3fteWZ6CteAJTn1rRxK7F_0UCWHPL-kDnJZsxKeChrZcMG7UT5SY5skRhh_2677S_59gcBC2uf-KpVNvsoVrs1E5OHFDnAUlWVw2sQ6pCBh_-tEgpJxokIkLMas3BCBr45-nhPzLfH_yHAWaMKfWAsrX8LQmWdv538qmT7auTiNzodosvJLeAH_ZiGCOTCkB-W7CtnjXwDjs-92FfMwpgcN-2-QM-BqqXo5Qnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0532608c1e.mp4?token=KNDBbpBXl1V_7DQIjzl81TIaYnCL84EDTltauCKheSdk6Dbi_RW5QFklRsZ1axUGTWuEbEV16g7ih1E2xNfhaixPQSS38w044cyvtI-rb8cmzJAP3fteWZ6CteAJTn1rRxK7F_0UCWHPL-kDnJZsxKeChrZcMG7UT5SY5skRhh_2677S_59gcBC2uf-KpVNvsoVrs1E5OHFDnAUlWVw2sQ6pCBh_-tEgpJxokIkLMas3BCBr45-nhPzLfH_yHAWaMKfWAsrX8LQmWdv538qmT7auTiNzodosvJLeAH_ZiGCOTCkB-W7CtnjXwDjs-92FfMwpgcN-2-QM-BqqXo5Qnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
كل بقعةٍ في إيران تهتف الموت للأميركان.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/80944" target="_blank">📅 14:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80943">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نايا - NAYA
pinned «
جمهورنا العزيز..  القناة الوحيدة المعترف بها من اللجنة الإعلامية العليا بخصوص التشيع المركزي هي على الرابط أدناه   https://t.me/KhameneiMediaIQ
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/80943" target="_blank">📅 13:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80942">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">جمهورنا العزيز..
القناة الوحيدة المعترف بها من اللجنة الإعلامية العليا بخصوص التشيع المركزي هي على الرابط أدناه
https://t.me/KhameneiMediaIQ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/80942" target="_blank">📅 13:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80941">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇷
المتحدث باسم الدفاع المدني الإيراني:
لم يتم الإبلاغ عن أي حوادث حتى الآن خلال مراسم وداع السيد القائد الشهيد.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/80941" target="_blank">📅 13:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80940">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔻
سيقيم صلاة الجنازة على جثمان الإمام الخامنئي في طهران آیة الله سبحاني (حفظه‌الله) ؛ في قم: آیة الله مکارم الشیرازي(حفظه‌الله) وفي مشهد آیة الله نوري الهمداني(حفظه‌الله).</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/80940" target="_blank">📅 13:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80937">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lygn6Gpft4LY3PeEYLERmRv8bLdlU_GTq0dESAAll3-h6JjKxtewraDm-yaegCUntzbBeg80J3pPLo9iPNyAO-Y1hwNuxmdKJCqM28HFLmLKygD43ziGtK3RGIDEHB4OVa-WXqk-Ummviw-zDnXmU6ODVyYqguvg69lbbT79L6M8BIXE2iTLOf2Ce271E5AiWL2iM6zraEQIYHNqirp1cuhVLuwDjbW4nhqEMAhhuQwId80aOINEz3oq-dtVoK5qH5KB-c3csdAQqR7_c_I50L7W8rA4LW2VvJuQIwXZr4W1ic7tiAtvnJ5_lnmk0-zhd4mVKAi6siuvI7wFpSzT4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffdff87be6.mp4?token=lmrIYrwIZpLSInJAAygbwV0rcZEhZexiJ5EEeJKk6OWRD6qVJ1aLnXT4UMA7iuHXxr8y5PNPgFx9Dw88mv12NkF1tyn4OljI_4FhLuGhkssLhUOXhlObL0kJcLKXuAmre4rDZbl2R1sgfC8exqT7s6MVKhThXtvrzi3q2O-d5ta1HVowLoLum1IYUXkLNsHFJHvqdILQ2CXearbRQ_JGa-CxIT8g6lA5Meso9lulZ06NlaNv6C18e4IIKi-4_DfjR2WW7zAxAGVjG3wglxcMdMTCQ_kXppKH3o-seXSmZp-Uj--pSYckqL7sqV7P1RCIkZ_pc_HpSq9z1kwN4XiUWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffdff87be6.mp4?token=lmrIYrwIZpLSInJAAygbwV0rcZEhZexiJ5EEeJKk6OWRD6qVJ1aLnXT4UMA7iuHXxr8y5PNPgFx9Dw88mv12NkF1tyn4OljI_4FhLuGhkssLhUOXhlObL0kJcLKXuAmre4rDZbl2R1sgfC8exqT7s6MVKhThXtvrzi3q2O-d5ta1HVowLoLum1IYUXkLNsHFJHvqdILQ2CXearbRQ_JGa-CxIT8g6lA5Meso9lulZ06NlaNv6C18e4IIKi-4_DfjR2WW7zAxAGVjG3wglxcMdMTCQ_kXppKH3o-seXSmZp-Uj--pSYckqL7sqV7P1RCIkZ_pc_HpSq9z1kwN4XiUWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇮🇷
في العاصمة الإيرانية، قام المنظمون الروس بإقامة خيمة خاصة لاستقبال جميع المواطنين والضيوف من روسيا، الذين جاءوا لتوديع الشهيد الإمام خامنئي وأفراد عائلته.
على القماش الأبيض للخيمة، مكتوب باللغتين الفارسية والروسية: "الأتباع المحبون للشهيد من روسيا".</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/80937" target="_blank">📅 12:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80936">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M45Q-7SEEwMskZTXi5zJOHVX177pkEpqd9DZy_hqySM2WHV44uP-jcs2AHcn9_5J3j56BRku-_5wOqLMuTVJm_UKCoFOXI8B8Ej9ffshr45H8x3Q4_SoqjbaHZPIuFk8lsMWoSCEHYdrAVs8YL14xmIHmC3QsJktiHRJMEdg-kJMVujTDuothLLH4APurXjdhTIG5t45dmTwRq5nevEm8jSi1L3Cpt0x6601aoiAA-7cwjnUsg84H4eXUcdKCJqrWYHeepkWwKXEKraGOtWoaWl3M52CHe5D7vxDjBa7KbCw6oMf9kBMGyquBMHpM5VNloDJyt4DV_u4CQxpehUtmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏رئيس العراق : بعد الانتهاء من ملف الفساد سنتجه إلى "سلاح الفصائل والملف الأمني مع تركيا"</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/80936" target="_blank">📅 12:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80935">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇶
معاون رئيس أركان هيئة الحشد الشعبي لشؤون العمليات، ياسر حسين العيساوي:
اكتمال الاستعدادات التنظيمية الخاصة بمراسم تشييع آية الله العظمى السيد الشهيد علي الخامنئي (قدس سره)، والمقرر إقامتها يوم الأربعاء المقبل في محافظتي النجف الأشرف وكربلاء المقدسة.
الخطط شملت محافظتي النجف الأشرف وكربلاء المقدسة، وجرى إعدادها بالتنسيق بين تشكيلات الحشد والقوات الأمنية والجهات المعنية، إلى جانب وضع خطط تنظيمية وخدمية بديلة لضمان انسيابية مراسم التشييع، والاستعدادات تعكس مستوى عالياً من الجاهزية والإمكانات المسخرة لإنجاح المناسبة.
مراسم التشييع تمثل رسالة وفاء لدماء الشهداء الذين ارتقوا جراء العدوان الصهيو-أميركي.
العراق يتشرف باحتضان هذه المناسبة واستقبال المشاركين فيها، لما يمثله الشهيد السيد علي الخامنئي من مكانة دينية وإسلامية كبيرة.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/80935" target="_blank">📅 12:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80934">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8fo5ThK6gn2jEHcSoyXkvXORE4tdmTY4i9robs08zkTv4LWMjDDk2fFMiVSgI1D6XBph3p6uxvzHhzFFZrBeYIEjtkPO2VTsmcNit7srdZNuFfiMOh8GIi1ZY50-kUMyMfHYw71_eLUKnnKRyFcq8qKQbBGdEpK5Dc9gfR1OXEKl4NU5a0Qz_WWIXZxhbRU9nbbtb3A593yEBWK9JT0AUqa2zyBVlvzU60E5ygQ0tCA-F7wEElUFkzl8C8LcfEEEuMbPPzizTKenm79BHbF42YvLuRpf4lkMbm2oypMoJ_vY8zCNoXcxf8ClPo-6c8-c-iuRr0dAu_6XN6zGWQo2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
إشتباكات بين القوات الامنية العراقية وعناصر تنظيم داعsh الإرهابي في محافظة كركوك شمالي العراق؛ مقتل إرهابي كحصيلة أولية.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/80934" target="_blank">📅 12:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80933">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zt8HTY4JijYmVmuRRkCmIpw9QNfhUC1nZO1d9L6-belWdJ5rybUmD3dxEJvLN7hkx3jczQaUhgPSSqsSrK6QzLsqufzEtHDJlfuS8WY1lNRydsUqbfXvul57_1Es-NYMXjVZy2BpwxcJKqmhro2JX8KsMYAz6i1sOEL9rOu4I9ofs9DiNcYJ7uY-V00mX8UNnWbATAKreXFXTmRhwwBXpPZuOAD6EFv7imW8BbmeyVdwXAb7hN0J0t6u6Zfm6osgM9XyZiKziCV_rJCV2Np_xI6zD8EW6OlXOEGsgwVkxquxncUXr7nGdQVZTJ1Et_vLQiwYURZir1F5O6c1m5Mh-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
هيئة الحشد الشعبي:
عمليات الفرات الأوسط بالحشد تعقد اجتماعًا لاستكمال خطة مراسم تشييع الشهيد السيد الخامنئي (قدس سره).</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/80933" target="_blank">📅 12:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80932">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">المرثية التاريخية للشاعر الفلسطيني البارز تميم البرغوثي في رثاء قائد الثورة الإسلامية الشهيد.
#قوموا_لله</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/80932" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80931">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15cbaa4687.mp4?token=BvQsUjQzrzxWiPz3PRs4I1T9YnFkYg7Ul0rlAEnOm0ikA9s1WdFsuZ2T_7qKPtLtr0h9PlZ4biM4WX5KBcz7pME9iAhTNjxXXphPq_ZM40eiHZ80l5oUOpyWm1xfvR3_czJD36C94ueMxmDbkrUNRoe31xRV_AL-Df3cWFeXSB4J-q5Hd-XZOz2qKEYN_J7ocbDqde8PrYqq50UPvoyNM2kp0SYjokP15XVrXBnIC2wTj9LEwE4LD4Y-ZhhNg6ctZ1i6apqIarW6YSGZsP15FNsH5MbFcUrcKALF2ORdDG1khZkIi8VijU1IYsxnmoqPVm7v9jHc6484MKLIm_uu4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15cbaa4687.mp4?token=BvQsUjQzrzxWiPz3PRs4I1T9YnFkYg7Ul0rlAEnOm0ikA9s1WdFsuZ2T_7qKPtLtr0h9PlZ4biM4WX5KBcz7pME9iAhTNjxXXphPq_ZM40eiHZ80l5oUOpyWm1xfvR3_czJD36C94ueMxmDbkrUNRoe31xRV_AL-Df3cWFeXSB4J-q5Hd-XZOz2qKEYN_J7ocbDqde8PrYqq50UPvoyNM2kp0SYjokP15XVrXBnIC2wTj9LEwE4LD4Y-ZhhNg6ctZ1i6apqIarW6YSGZsP15FNsH5MbFcUrcKALF2ORdDG1khZkIi8VijU1IYsxnmoqPVm7v9jHc6484MKLIm_uu4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
في حادثة أخرى.. عصابات داعsh الإرهابية تقدم على إختطاف مواطن في منطقة التون كوبري بمحافظة كركوك شمالي العراق، وتقتاده الى جهة مجهولة.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/80931" target="_blank">📅 12:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80930">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⭐️
إشتباكات بين القوات الامنية العراقية وعناصر تنظيم داعsh الإرهابي في محافظة كركوك شمالي العراق؛ مقتل إرهابي كحصيلة أولية.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/80930" target="_blank">📅 11:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80929">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⭐️
رئيس الوزراء العراقي "علي الزيدي":
سنعالج ملف الفصائل المسلحة بطريقة حكيمة ومقاربة عراقية تضمن منع إراقة الدماء.
‏أميركا شريك استراتيجي والعراق يقرر علاقاته وفق مصالحه الوطنية.
‏العراق سيقيّم احتياجاته الأمنية بعد انتهاء مهمة التحالف الدولي.‏
العراق سيحدد ما إذا كان سيعقد اتفاقيات أو مذكرات تفاهم مع أميركا أو غيرها.‏
سنعالج الملفات الأمنية العالقة مع تركيا وإيران وفي مقدمتها "حزب العمال وسنجار".</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/80929" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80928">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔻
جانب أخر من التشييع الرمزي لقائد الثورة الإسلامية، في نيجيريا.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/80928" target="_blank">📅 11:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80923">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rN7WwXkL9S_QxFA3fWrC8UWzJBoK8e1LMlqbfjC4Yh9zwKvIA5EIJ2CFxi2GEMsZDzfBm4LWYzzojYrr6E9YiXOGWJldiwxIB-GsIfO4skv-7czjf0tsHCpgQgQ_gdu9u6mphqShiTFeIIkMeh2CIX8-lCqWy-9qES75WFlnWJkI4XjihhfXck9RAeLL9u2cYFJ4vVbMvx3TySUENX4_RnP8b_TwgUB04SCb19lG86CLcMc1GGt1_xMo94gbKQmJQEuP1HBpXMY4TQaca96OvTqyksjFZ__9jeVv7ySNA_UcXcqFr5bMtTXzjrJxrr5U4w1gbxbT4W5AsAsePncAlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FxdYW80rybzMVadlHErks1HPsDro8pRS278QzZMcsT4VLGnhPkEWOS-mwibGQUsXfWP9_Fcu_bLfUX56PAqdFKOnkQGWleN9PdKcdPoyOekJCE56omyEmPzfRYoxIr4Qb-eg6X8gs-XhQkSF4u94wg8BGSOscPxVMejlJG2d0R6jU3B3X3XvydUhwKaaFERSzpXfygieJnOvR1OIHOHIB4_oQxe4YvY_cuGkgKb717n8uZO-DymTHB0AutkTq8sWtEbOOZBxwoZFGup-FEPoakeh5x4Ga8Ag5X22XObtf_gEloQTgTcdrAWnNta_TlZzLEAAJ0n4jNFuQVUfL9IEww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zvd2Z7LFug3xtDMEBWtMPUHuG8DOcEZWbVSyUBSIM9HjUl1rWa_408WoseO6inpuRLdTmhwZ4CuVVBxA9DgALwaxfJtTLDgfwC1kiQR2EJMaLNUcKmMvukNcYlhZdNBJOS2wYnf3A-W8BcKGVOc5gF9EQTj1jd8_GgwFZS1Qdyv0888pCdw691jnmgqzhCbXO_cIQR9VSzdXT2P5TJdsNs4ogSPxrr-hFLbQmcn5psFFegpkAV3_6-udTNHDIUdS7peK02bwe3EaMC6RVpl3OJFRD7uWj3S3kx23BJHdgQ6plUEqTuYjAgr_xyMN8WqzZ205DSMWgP05FzuDezD7-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fg2RaBPfs61eyI2d3wb-S36ZsQxHoWfxPhYwAs1d7vD4iqwezeVYck2w6ulvdg4mTEKVmm24mVe39zJo98tZRsKXl7e5zI36zZIA-pVAnLkD6-5nAiP31QxvbLZOzVFH0xqb6nqSdOJuuYQqrP1A8vP-7mmunu4dNZ7P-WCuC4NAEi2qgnPojlND-UrTy98vxI3q_kqD6sQp2-uBECznbbZa7yY9tzgC-nup77K63FLaMI0IuSwEsotyOJpoSXgz4Sjv3qoA8BHVLcGNqQv5_lPjQ5jtX6qE-dZRu0NZtywwI6TlzjLZLakb7QymWWRyu6cso9GGFHQKyQCRj14H4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f68d37552a.mp4?token=kWN00JUbNCFSUbRFO4KwYZrCWLcymoQOGm-nRp3pAd16RvHkkRZ8M61RVirhbAWT1GX-UZadOap4UigIw84iUZbHLG6HLH6h1hwkG7HfIc8Bz_H6c55apMBB9uI3dkPTUyZfw8s9OEen2Tgxqyx3R7CHDFAbJCOcZ-UZPvkMkzmo4S7TwVUUXBdTMZvzeTkYAYYvll2Y5uPhRCavs8yh3eOAlQwZ9T8r93Ijrag54LH26slYNr57RuEsvwN3-XQKrEm4y1S8e-NQCA2z_velnLMzSB3BQaFrO1o-cQPMn9tFLq334SZk5rpir-2g0Q-YWVo_Y9DJB4atC9qNj3FaNYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f68d37552a.mp4?token=kWN00JUbNCFSUbRFO4KwYZrCWLcymoQOGm-nRp3pAd16RvHkkRZ8M61RVirhbAWT1GX-UZadOap4UigIw84iUZbHLG6HLH6h1hwkG7HfIc8Bz_H6c55apMBB9uI3dkPTUyZfw8s9OEen2Tgxqyx3R7CHDFAbJCOcZ-UZPvkMkzmo4S7TwVUUXBdTMZvzeTkYAYYvll2Y5uPhRCavs8yh3eOAlQwZ9T8r93Ijrag54LH26slYNr57RuEsvwN3-XQKrEm4y1S8e-NQCA2z_velnLMzSB3BQaFrO1o-cQPMn9tFLq334SZk5rpir-2g0Q-YWVo_Y9DJB4atC9qNj3FaNYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">على طريقة خدمة زوار الإمام الحسين.. المواكب الحسينية تقدم الخدمات للمشاركين في مراسيم توديع قائد الثورة الإسلامية بالعاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/80923" target="_blank">📅 11:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80922">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsEQPDQM0ntULBupv9Pe2Wvdf9KkqFeRkZFrpuEdYn0l1t0cAPdTh1ES2j3iiS9mmU080KSl4m9qMLC2fN3qJvjCBp9zJ_kY13Dm_7nIcgl1i1IyF45p1wGWrromfkRkOXGWwjVvkLaFqR9M805TOOfFqrQuZDN289U7L26YxL6S8k7mBj_8CuiTDSHVaPovlPngiTPX9w3_a-KC8VD77aN_5qdjnwFgL7LK4do3akk38dhHT73vUP8-HciYvpMvJIIlvjzrGBoLyDoKvxr9WTnAFS1798bZed3W-RrCkkQdrOls5JHAn5S1Ym586FUtqN4fMx7BGM0_TSY5k595zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
إرهابيي ماتسمى "وحدات حماية شرق كردستان" الإنفصالية تعلن عن هوية عناصرها الذين تم قتلهم على أيدي القوات الأمنية الإيرانية في مدينة مهاباد بالقرب من الحدود الإيرانية العراقية.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/80922" target="_blank">📅 11:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80921">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⭐️
إشتباكات بين القوات الامنية العراقية وعناصر تنظيم داعsh الإرهابي في محافظة كركوك شمالي العراق؛ مقتل إرهابي كحصيلة أولية.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/80921" target="_blank">📅 11:25 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80920">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇷
غدا الساعة 6 صباحاً بتوقيت طهران ستقام صلاة الجنازة على جثمان الشهيد المجاهد الإمام الخامنئي والشهداء من عائلته في مصلى الإمام الخميني.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/80920" target="_blank">📅 10:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80919">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQcc45SXv7IUsqPYrmFezZU7sbW1NqdWcZD0G6IVHeQxVK1a3m3SfwpE-dx5zJWgvTfkx65eLjUI-9a-hZGNHLoqlcuFwqiVF9NN0y4mXjbqJy5pGcPT1NosKXCHNdGUA19WXOKY2-SlwdWQ7BxINd7o609hGGzN6E1hvHiVVcEH_jtyS__BE4PpFZH0IY0wuNTensKzXRbLeQqmhkCqsImF8X_5_B-4fVfiEzWgevZnpDzNA6_v1_gOp3RsVTLk7WspEcV1LBWNsJ3IGfaWiWGBV7V9oNA_OHvGCvcsnypaukGshedKDQLwxBo1QJQj8l1L5lsNsr0hk-ro-iDdQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لازالت الجموع الغفيرة تتدفق نحو مصلى الإمام الخميني في العاصمة الإيرانية طهران للمشاركة في توديع جثمان قائد الثورة الإسلامية.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/80919" target="_blank">📅 10:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80918">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15fb197939.mp4?token=RTyLaMmjqFwPWXBbSPYPHc5aplwr5lFJWHRTcDSGl8R3Rgp_5KJraLrsQj0FYcQStW31h6E4YKdzNZDoBNHGkpbOBWfCkFRlJzIVhSNz5R6zS-U8yvtHQk6nh3mcSYdquOxx5FuPTxuTijgN5zWBxdrV353AYG24bKN1dYfubmsqU5hYBroXixFKofZAxkRKC0qqmZYzQ460rpsCX1qrjudGnOKS-i3kK5LPZYYBY77GyaGu0wc_tqAk51rDDOoTUj0XhHeFfgRiM-dmv1Y0w4PMgASQWOybZot4bJ2jeIRXQZW9mYJspbSlABG-cQd0Pc0ZJKulS7mgxxi7Rx1_1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15fb197939.mp4?token=RTyLaMmjqFwPWXBbSPYPHc5aplwr5lFJWHRTcDSGl8R3Rgp_5KJraLrsQj0FYcQStW31h6E4YKdzNZDoBNHGkpbOBWfCkFRlJzIVhSNz5R6zS-U8yvtHQk6nh3mcSYdquOxx5FuPTxuTijgN5zWBxdrV353AYG24bKN1dYfubmsqU5hYBroXixFKofZAxkRKC0qqmZYzQ460rpsCX1qrjudGnOKS-i3kK5LPZYYBY77GyaGu0wc_tqAk51rDDOoTUj0XhHeFfgRiM-dmv1Y0w4PMgASQWOybZot4bJ2jeIRXQZW9mYJspbSlABG-cQd0Pc0ZJKulS7mgxxi7Rx1_1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"الموت لأمريكا"</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/80918" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80917">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/368ae0ed53.mp4?token=BAvxkWefFFknb5XY5U-4FefcsdDwI7lC5cCwgTM8sl2Ybys6qhiDOJ62io419eIH95uTSulmhG_dk749icRPrKoTSeWkpDn-SDoX-PJNcQzeBen-lD36IpbGF4kOcw65UpGV8oQbbLBg0vRN0N1YTeyrda58bwc4COrVWs4HBT0J67ywPU24THqPzIYbgFvE7kqVMQq_VZfKF8GQS-q62ndddYFz5CoEijyL7cJgDapnGvn8mVzU6z_O_5pnu-T4mvWrjR-tTdQ4TBoIWLARAndL1dscGRRAfBxyhiMVEdeO2MSELMfmOPiSiG7WT3_oIDm9z_V206HOxdLu_xttAWhTXGylE-B1Z2Yg5qR-jMutA1gU8GUeLJFeea_glMt7LT6vTBXWIZ66UHp6u3-hvU5bX4XYXA7z4MWSuUsYq72bPwuk8rWXSnxZlun_LFUN9j8lpFqQKVOW0U89KL80pM5daPzTjbIgQteyp2KyLbX_gCJdTIUWLNIHnogm6G80q9soYMV4CzF9bhsrSSJAe-tXzGQQ8c_WhMEPitInAlVAAgjjpm9zGRrXxPoAzuzdmeFfqjwOhKZMmD0NAuAvyIx393YU7ot1vJvjUvYEV89Ll1VLSS59uAhJUDzY4kETtJ4fR4qXWCar6ttjOxFlRbD5RoKYF-Fr2EoPFX6rum0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/368ae0ed53.mp4?token=BAvxkWefFFknb5XY5U-4FefcsdDwI7lC5cCwgTM8sl2Ybys6qhiDOJ62io419eIH95uTSulmhG_dk749icRPrKoTSeWkpDn-SDoX-PJNcQzeBen-lD36IpbGF4kOcw65UpGV8oQbbLBg0vRN0N1YTeyrda58bwc4COrVWs4HBT0J67ywPU24THqPzIYbgFvE7kqVMQq_VZfKF8GQS-q62ndddYFz5CoEijyL7cJgDapnGvn8mVzU6z_O_5pnu-T4mvWrjR-tTdQ4TBoIWLARAndL1dscGRRAfBxyhiMVEdeO2MSELMfmOPiSiG7WT3_oIDm9z_V206HOxdLu_xttAWhTXGylE-B1Z2Yg5qR-jMutA1gU8GUeLJFeea_glMt7LT6vTBXWIZ66UHp6u3-hvU5bX4XYXA7z4MWSuUsYq72bPwuk8rWXSnxZlun_LFUN9j8lpFqQKVOW0U89KL80pM5daPzTjbIgQteyp2KyLbX_gCJdTIUWLNIHnogm6G80q9soYMV4CzF9bhsrSSJAe-tXzGQQ8c_WhMEPitInAlVAAgjjpm9zGRrXxPoAzuzdmeFfqjwOhKZMmD0NAuAvyIx393YU7ot1vJvjUvYEV89Ll1VLSS59uAhJUDzY4kETtJ4fR4qXWCar6ttjOxFlRbD5RoKYF-Fr2EoPFX6rum0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"الموت لأمريكا"</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/80917" target="_blank">📅 09:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80915">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQp8zC6qU6uC-0rwUAbw_XNYJh6Z5mBq9OLMrhR9yGwf0XIuxkVw0tDnolARI1TrlY_QXDCGq3uY-Hmeka0nbdFffhgOCEtEGaHTsKLoBoplWLrTBmRTKRSIXYKFVPSzKV7ajLNrEcpoemyBhQ5LFV_kou3L9f1GaPh6RLsYqwXg7WnBKaZj4Gn8bQcBxQrzlQGQQPOwJ9ZHreSu6dzEUpIoIIVqGADsgQ9mnb8LsM8F5YEgEDTTzOkk48CtL6ZNqmO706elm_f6-zXn94OpopuMHZqbIMPpmXQSd_UD7PK71kWSVdT4LgU98bgQHCpE79qsR3rSIa7okidUaNvbEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bnyhv4HzgBQJWocLuX-rZLTqne2n7qn1uMAnChLWMFVjmMTx_NhhQ6Zvjc4oifN4nvCm-UDv6hcHQ2fZTm_HRQQlnVjAKFYWVXYqo6xQMt9ubTzVwSWaq_FpaC6i5zvA80LhtJldimU3-ZjMOhuM31rVNcdyTPP98WH1109F0f-XIfYSaaq-uYgaSNbCtc8eoh3ACVLRbRtD514sIuJFIUFhegl09YgCrfCUSOpcR1TtfYGHKQYZrTnVgAgW0Yo5BkNo5Kfi-_QNywcLB56LsKy5w2elvfgrX1CjSkD_-d1suWndS9u-P-ZKvALwCRzW8Ex-pRdJnCfe_BDGBqQ35Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭐️
من مصلى الإمام الخميني في طهران.. محور العزة والمقاومة يودِّع قائده الحكيم الشجاع الشهيد.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/80915" target="_blank">📅 09:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80911">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wArc8cdY96xha2QB_rWpF4TNCxeWpmkQyyXaXAMlkzF93-PJQjFNGyHSjpKwh2PZQ93Fr3Bz-tfVbAuzh6Bg8knFerZfkTK1yZiQutr3-mIe7i2fVkg3wAnj2UaWG1tVX2mGIWWSgR8M0ZbPqM0LSN1odko20aC-HOuNvqWVLv29QrkMuFleB-CVxAMCSNxeKZknMVoj2-wZDmNM5tK2K3WTntAFBU7H9CWQTdPxsGi30JhhcT1QOvY28G8rPYBHe4qC5UPh5yNW-gDq259rzRfB5Iosmx1E4E6SjSJoNGvU-gDw3BK7eoCxBsjTgPFhpT1msgc4x486JhGRt7yd7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GeLvZlAinEDObsrYU9hekdfexlLzVtrTFG6757txE6-nVM6iJR3X2jh5G1CDfc4ieZxiFotPvJyYHVNzHbPBey-TJXhVmbaXOjyYfQ3__9pI5PD1EP2FGClBg5S9t8JHpVgovpeGWnzuXpAR_jL6rDUo22ciz6vfwPkLq2DW9x8ktLAfgPKY87dMFnErtpA8cfEkesWlRstFFVV1NdAe7rRfCqgU1MSGxAIT8O-i8Vel2M5mCJPR5PlF7mOUvzFjTnD-9Vjs6wA37uxFiQxyCS1StIQrm_rnACGgDvbHsqd2Vdnpvu-R1qyQ4l8Sz-rcTlcpR2twUCEmTcZWkMHnVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bwFTKZ4n1HuOY6HpiOilkWQIGhLT6kJtWnfRyB3VttN4z8MaEya_OA2qjnl2BTH7UlfD8_A0WlwXgzUcoxXwXLEfjLsyD7pFyyMrobZ7jWhgyHte32awcgxwvJx-l74BC4ul1hXzRNwyYVhsuSVY8ZqDBp0O0rlzwEq7oZ5GqHd1TYv6xQJDbkswDnTkHI6h2NSOQ8PMQ7ZOm-RWw-6mRtx5RAR7QFfLA1wW5_Sh1ZKzn7cmfk-m4Gx_D3SJlUtKJuLA6YQbJMK1ZQBPw-bXm9lLlYIV3Oe6D9oreT4ZgCxl-aP8OYHqCm8cJta7CRWc7P_iZ7VwXZHwzOGjMUgCsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i1zBWIywvP93y9ZQz-9Y_Q8TQAgA5eD2pmLd1trvV-sm-3SezdROnIJUXLaZ6M9cuoAlKIx9BF5vezsN5HSkF2XXJ3FI83P-C2x3s8akM0dtm1I-2l3GD93wGR1CF6Y4iHtAEdZ7TUIkJLeFR7hOj2MZjnKC8Swp8Bn_HJagt_-akvFWy10Il3Fq9aKMO5vQg05lZAtFKW8FUb1beXhhOk83Z7ABe3NgwgtXpuvDJHh4vopc6lFKyjLfdVrKA_VbofDJmoSQoac4aVm9r86rIYTxiAVgCGSDu-ibAlgJ7fMZxZAwCjecLR-VWbfSJPlwNSqisXzZUmXcQItVzDIIUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">أقيم في نيجيريا مراسم رمزية لتشييع جثمان قائد الثورة الإسلامية الإمام الشهيد السيد علي الخامنئي رضوان الله عليه.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/80911" target="_blank">📅 08:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80910">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a2ba6faf1.mp4?token=EnTrA8AbFoC2HOxXjTNcWxRHpqkGLH0s1J4Yc0U28LdldjQDwNbMD1hvgxLok2U_nV-r_ZOcUDoCiXz5erFmWfyYztM1r4CQWM9QGSdTaIxYcEsZ5a1OMpW3vRssj8hD_SudEG-Y0NJH0U1MOTa51HVcGRV_O6ZnV7lzRbt2U293W-lHpriV8vhgLn5TyF5dOy66z2TIKcP20H1PnPFeB8O4aAuog2g70ZPJAV2pzXuZisO6hWGgL_sKw-Oy0S7arZlcHcw_49tHiqGyTumtTYxFmnc6ub-UmIadxdMFrnW8l8aysoR5qJUmeKHyDryy3XdimATEXCMH2b80AVtLVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a2ba6faf1.mp4?token=EnTrA8AbFoC2HOxXjTNcWxRHpqkGLH0s1J4Yc0U28LdldjQDwNbMD1hvgxLok2U_nV-r_ZOcUDoCiXz5erFmWfyYztM1r4CQWM9QGSdTaIxYcEsZ5a1OMpW3vRssj8hD_SudEG-Y0NJH0U1MOTa51HVcGRV_O6ZnV7lzRbt2U293W-lHpriV8vhgLn5TyF5dOy66z2TIKcP20H1PnPFeB8O4aAuog2g70ZPJAV2pzXuZisO6hWGgL_sKw-Oy0S7arZlcHcw_49tHiqGyTumtTYxFmnc6ub-UmIadxdMFrnW8l8aysoR5qJUmeKHyDryy3XdimATEXCMH2b80AVtLVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الحشود الغاضبة في مصلى الإمام الخميني تطالب بالإقتصاص من الرئيس الأمريكي المجرم ترامب.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/80910" target="_blank">📅 08:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80909">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQeNLOtgUuyfQHnSe3HxbmQzwP9H-g84ASb11Dsgyy_lDwwlcdtJ_7i_7iYoOEEySw4NsWM8plJs6Gg1Msi8Uw0tDufby4CtqGAbmtdniRJft9jK1Et_9ISrFpwmTSeLZpQJFQLKNp2WSPOtyTxt4bDsFvZBVnFGa0Uq3usA3Zr57747eE-xmGf6M0T0zkVQ2BlWY4z1Pe6YYaAu8uKuP5Ca_cFfmUzjyWbUmqw-9g7CMkqMeo4LcMhuI0ClWRS1S47w_68RqmwNbkRH6dcgYcP25fNhEFBw_gk9LjHTzW7ztzTPNTTYin1VdmjeLwrFiJiri9d9uUP31SlO9eJyLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجموع الغفيرة في مصلى الإمام الخميني بالعاصمة طهران تنادي بالثأر لإمام الأمة الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/80909" target="_blank">📅 08:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80908">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/211d83b2cb.mp4?token=YLz4R5dq9uiEmIOQFOY2YiA-58VNdHSvtQO5ItiInHzM4MQQ0TARAL_b29EoSQKMGzPD2bYQqOEL8ASsLtiiO7WEpYzn8xfIygRZx1VA_P1NHsrk8tSWjq8Kpj2kgmYIiEOCHGyb2yZ3s2uAbGNYtSUMoG6sLUu7O0VEazStQX2qKgyFnUK_VdPGnaBpDGNNkZUX5q6ShTW2uQKm2QA8qRu3MXWC2IQzHoxcr14NAxWp9C8fppJaaBCjT2AJdFbCDmb-bV4_SaxzjKzsIRvmo3NtyGVoPfptta2GKj7bge7aObfIZ1Qr2F7f7SxkRmj4xo2l7QhUg-dS6tf2uWiNsIrDQwWn1E5YLmKD0JuQuZ7ZqxYu8V4LNcap8JkFA2AAhGJOCZ_vw2TIMZKHEHuCgrVNX1dygiyCRtVOPi3BAon6u41JIx79YM5xMtsN-FFfgfFdO7xGHz5bweuuFYrNZbyI9b0jiZqsffRVm7oC5C_Bs0WkzbeHRxyRg0JsmcmthWalO-RV5Q2nqDgUkmJN8Jd8nrvqZmlaDCCdNOt7DKoMfMNPAW9MHWwtb4384I4wUMyd36F7qK1nwTpZOxAhkDEVUUsxsmeCPcGvctkHS_lJTMo_2kLoOlqEZiY4I_ItM7B1rvcAGDaGxcfte3JxtMI3RqVZ6IQBauPx0NFmd8o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/211d83b2cb.mp4?token=YLz4R5dq9uiEmIOQFOY2YiA-58VNdHSvtQO5ItiInHzM4MQQ0TARAL_b29EoSQKMGzPD2bYQqOEL8ASsLtiiO7WEpYzn8xfIygRZx1VA_P1NHsrk8tSWjq8Kpj2kgmYIiEOCHGyb2yZ3s2uAbGNYtSUMoG6sLUu7O0VEazStQX2qKgyFnUK_VdPGnaBpDGNNkZUX5q6ShTW2uQKm2QA8qRu3MXWC2IQzHoxcr14NAxWp9C8fppJaaBCjT2AJdFbCDmb-bV4_SaxzjKzsIRvmo3NtyGVoPfptta2GKj7bge7aObfIZ1Qr2F7f7SxkRmj4xo2l7QhUg-dS6tf2uWiNsIrDQwWn1E5YLmKD0JuQuZ7ZqxYu8V4LNcap8JkFA2AAhGJOCZ_vw2TIMZKHEHuCgrVNX1dygiyCRtVOPi3BAon6u41JIx79YM5xMtsN-FFfgfFdO7xGHz5bweuuFYrNZbyI9b0jiZqsffRVm7oC5C_Bs0WkzbeHRxyRg0JsmcmthWalO-RV5Q2nqDgUkmJN8Jd8nrvqZmlaDCCdNOt7DKoMfMNPAW9MHWwtb4384I4wUMyd36F7qK1nwTpZOxAhkDEVUUsxsmeCPcGvctkHS_lJTMo_2kLoOlqEZiY4I_ItM7B1rvcAGDaGxcfte3JxtMI3RqVZ6IQBauPx0NFmd8o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجموع الغفيرة في مصلى الإمام الخميني بالعاصمة طهران تنادي بالثأر لإمام الأمة الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/80908" target="_blank">📅 08:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80907">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f580f185a.mp4?token=ptL-RfXdg2smLrJBNZ4E1AYBp4uhPc33axi83b0IRlsjOuUqSvrkXXYreL_kMuyXMNbqwqFHG_uCWAyZLM0CTvO4gCbKtA0OXQQI1JABsLKoYYUn0-uD0CbKaOuxB79NCiANMFTyMCZaPolLnS3FTD5IsETV1WPaqCU62A7KiwasH9Eqoxc4wR7XFBkl7WM1PIRI0DR6570StKe1q_qZahd_G-p03epCZGY1b9hlCXTQaTlYWKNadbgNH1ShYbzZ3Ifk0UOycuYeHIKg5nOyeBYR6FSITyKm-JZ6N37VMA1BSwAhYUhhlrJeKE4Ah7F5e73fctyLznweZpk3lW9Pbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f580f185a.mp4?token=ptL-RfXdg2smLrJBNZ4E1AYBp4uhPc33axi83b0IRlsjOuUqSvrkXXYreL_kMuyXMNbqwqFHG_uCWAyZLM0CTvO4gCbKtA0OXQQI1JABsLKoYYUn0-uD0CbKaOuxB79NCiANMFTyMCZaPolLnS3FTD5IsETV1WPaqCU62A7KiwasH9Eqoxc4wR7XFBkl7WM1PIRI0DR6570StKe1q_qZahd_G-p03epCZGY1b9hlCXTQaTlYWKNadbgNH1ShYbzZ3Ifk0UOycuYeHIKg5nOyeBYR6FSITyKm-JZ6N37VMA1BSwAhYUhhlrJeKE4Ah7F5e73fctyLznweZpk3lW9Pbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجواء حزينة تخيم على مصلى الإمام الخميني خلال توديع جثمان الإمام الخامنئي الشهيد.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/80907" target="_blank">📅 07:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80906">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59c23d54d.mp4?token=cCM9Lmuk6lZKIAxHPRWYN90Jn4PO2AL1fho-yQHgKdNuDdtC6i3WGf-nNcVeddklQ-NIUTIi0T0i-h15CfMur3_9zL9pB4-wyRqOFZRYnY0ZyOo5z-x9FZO6naE7cmVpJc66bo6kyWdP87IK7CU4JNjQmsz1xM2nuqSKYIiOkbWyFY7XmnMwWBClVfq-CVDL6g--oHTitd3ooY_dmafc1nOr5I3-J5JcmU-vM0XY6g6qh-RxQNWAeZVtjy2SkCqs0m-aZMNiKeFmgH5hiDFEcXcoCWs-OcG2XH3Ir3ol6Zcz61IRSPmXjJ6Vv7nn23PzP3bCKwITaauhssj7KAepYLQ11AVvU1FAsov3uwUSmVrM_ya95UiLhWV9AnrQxs1JEDL4Lz-zJ4L6WK5WxuBIosl629_cIOYSPzU0oOO6qa0r69JZpliltmUZx6IE0iRmNDS1k_mz45ef7Cx39AwQGV6PUn3LcFUUpEH4Jr0QCOsrSLQDCEHqCng95dNECVjayKvMfk0dC3P-XZCjNgUiDiy-QikVDS5uOgO8e9SnrBt85QMm991mhgO510sf-WEFM26E9DpkAWfB2XlhbQJYOan8JmwpD3n-OjW3uwPaqD7GQmQFLkeBV2A_3FHisrE0GPPHWZ9lmpb6nXcGTmpzBO0FvBbDj2G3Kc6ZROuLaXo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59c23d54d.mp4?token=cCM9Lmuk6lZKIAxHPRWYN90Jn4PO2AL1fho-yQHgKdNuDdtC6i3WGf-nNcVeddklQ-NIUTIi0T0i-h15CfMur3_9zL9pB4-wyRqOFZRYnY0ZyOo5z-x9FZO6naE7cmVpJc66bo6kyWdP87IK7CU4JNjQmsz1xM2nuqSKYIiOkbWyFY7XmnMwWBClVfq-CVDL6g--oHTitd3ooY_dmafc1nOr5I3-J5JcmU-vM0XY6g6qh-RxQNWAeZVtjy2SkCqs0m-aZMNiKeFmgH5hiDFEcXcoCWs-OcG2XH3Ir3ol6Zcz61IRSPmXjJ6Vv7nn23PzP3bCKwITaauhssj7KAepYLQ11AVvU1FAsov3uwUSmVrM_ya95UiLhWV9AnrQxs1JEDL4Lz-zJ4L6WK5WxuBIosl629_cIOYSPzU0oOO6qa0r69JZpliltmUZx6IE0iRmNDS1k_mz45ef7Cx39AwQGV6PUn3LcFUUpEH4Jr0QCOsrSLQDCEHqCng95dNECVjayKvMfk0dC3P-XZCjNgUiDiy-QikVDS5uOgO8e9SnrBt85QMm991mhgO510sf-WEFM26E9DpkAWfB2XlhbQJYOan8JmwpD3n-OjW3uwPaqD7GQmQFLkeBV2A_3FHisrE0GPPHWZ9lmpb6nXcGTmpzBO0FvBbDj2G3Kc6ZROuLaXo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدء مراسم وداع الجماهير بوضع نعش القائد الشهيد السيد علي الخامنئي وأفراد أسرته على منصة الوداع في مصلى الإمام الخميني بطهران.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/80906" target="_blank">📅 07:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80905">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b0629f1b9.mp4?token=uYB1WkHzCrkF-SAhREKFRSDnyCitIwbDFsF990CUsA_280tpKdsQUhbv1F50AZalVSsOP58Y4bhFHUiHD-T_wBIT2eeRfKbOQwSYseTUU1GdyJDKvyGIQouAzPIP3vRE2N_0rNHBuwRppfhjBBuEXIZu2wX4aCs0NNYMfK3NaNQWAhLI4ibp6ugoKim_YZyQCW_p00wo2qIYvoH96tfmtsbdBJzWCLTcBdLH9t4z7QwhQLYlXG8RBViJEb4E-OZqhSNJ835SYtnbnPoh78E4yTcYWeEvxE6-eSZIBGaqKIlRn_GY7eabblTESMfyBdondWEHHR30kAmRJyIJQ-CJ1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b0629f1b9.mp4?token=uYB1WkHzCrkF-SAhREKFRSDnyCitIwbDFsF990CUsA_280tpKdsQUhbv1F50AZalVSsOP58Y4bhFHUiHD-T_wBIT2eeRfKbOQwSYseTUU1GdyJDKvyGIQouAzPIP3vRE2N_0rNHBuwRppfhjBBuEXIZu2wX4aCs0NNYMfK3NaNQWAhLI4ibp6ugoKim_YZyQCW_p00wo2qIYvoH96tfmtsbdBJzWCLTcBdLH9t4z7QwhQLYlXG8RBViJEb4E-OZqhSNJ835SYtnbnPoh78E4yTcYWeEvxE6-eSZIBGaqKIlRn_GY7eabblTESMfyBdondWEHHR30kAmRJyIJQ-CJ1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ای پسر فاطمه منتظر تو هستیم.. مصلى الإمام الخميني في العاصمة طهران يعج بالحشود المعزية.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/80905" target="_blank">📅 07:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80904">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5b973972.mp4?token=awtI9Fx87Jx0YEHEpiWrWXuDB8my7a2jfONwVS-_810gUEhbSDz_2WxYP8r22MMHYfbM6o79-edN-qlTG2i7-YFQ5qWdTxueTxiWlSa1qTLZE58X9mM49L3peRItbImWpQGv_ovQhMS87G4QB7S7CIRL87HDevZPXQ0DKbDNyYuGqaPGHqDJkUTNa9ZbZryqYx4DxmcvRroQlJLRWBkZfbGu9VJ0DDfMSlqx8KmByHXm1RqE45kqv-ZrBPg_RKEIJ34Y8GN50Dsdj4X5xqTiHKdb7zOki7vv-RCJ28YgSI0GdU79gKEmCfDWDBd5lyhKRZNHnmf765QJzgZRfcF94A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5b973972.mp4?token=awtI9Fx87Jx0YEHEpiWrWXuDB8my7a2jfONwVS-_810gUEhbSDz_2WxYP8r22MMHYfbM6o79-edN-qlTG2i7-YFQ5qWdTxueTxiWlSa1qTLZE58X9mM49L3peRItbImWpQGv_ovQhMS87G4QB7S7CIRL87HDevZPXQ0DKbDNyYuGqaPGHqDJkUTNa9ZbZryqYx4DxmcvRroQlJLRWBkZfbGu9VJ0DDfMSlqx8KmByHXm1RqE45kqv-ZrBPg_RKEIJ34Y8GN50Dsdj4X5xqTiHKdb7zOki7vv-RCJ28YgSI0GdU79gKEmCfDWDBd5lyhKRZNHnmf765QJzgZRfcF94A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عَزف النشيد الوطني للجمهورية الإسلامية الإيرانية في مصلى الإمام الخميني.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/80904" target="_blank">📅 07:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80903">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c94673ef37.mp4?token=ElVALooMBrVQqUhIwpdXV2scX0p-zk99I_qEtODRLwExZZEaJUkRiMm88bJbLwAEk4oEpSDF8BaDqQQMNgbCehkvpybVvedzHjdcJB6m-CwBknSIK6L4CA69Ob0BjS7h8qxhCuOnv7EZpT2A6TBvNHCjGQAv3iv06D6FJjYv4ToiyZ_PMQufP1oOeGvT9Jv54ClG1w-G7XzWCuyObEOxcje1qRzkbOD14_psbHvnSvWz5gUo6Kx-IrUkXi-QfLnohTKyLe3fU-mCUdcEM4WLXIfq7TLZDD8hQ3my8OPKuIs21lutyWt7jauN8EE8wlvIqgLnHkkY49Gp5TMst0nAbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c94673ef37.mp4?token=ElVALooMBrVQqUhIwpdXV2scX0p-zk99I_qEtODRLwExZZEaJUkRiMm88bJbLwAEk4oEpSDF8BaDqQQMNgbCehkvpybVvedzHjdcJB6m-CwBknSIK6L4CA69Ob0BjS7h8qxhCuOnv7EZpT2A6TBvNHCjGQAv3iv06D6FJjYv4ToiyZ_PMQufP1oOeGvT9Jv54ClG1w-G7XzWCuyObEOxcje1qRzkbOD14_psbHvnSvWz5gUo6Kx-IrUkXi-QfLnohTKyLe3fU-mCUdcEM4WLXIfq7TLZDD8hQ3my8OPKuIs21lutyWt7jauN8EE8wlvIqgLnHkkY49Gp5TMst0nAbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
من مصلى الإمام الخميني في طهران.. محور العزة والمقاومة يودِّع قائده الحكيم الشجاع الشهيد.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/80903" target="_blank">📅 07:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80902">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLyk42Q3ujGadbNCtega1PxforQF15boooVpFsiuCbbBuTqxcGpUj6c67XGaZ_SZG2OTZrVJUvE6W2GdAGrZMzXn36MHbii49L1Tu2hlDx-2ZGo2PiRoKeI-jlckX0pp7G_B4f-ukPa_l1P5jx6S5n_P97y_bxQ24kduXPblY4uNZQWLzDTVuhcaC6p3qfOWKQi8Po_xlfEa-t7ppGMN3ZvkDPxwvkMQjWwzOuh5UNdmV7Bi8OmxcZOFwPv8AEwc9tUrmJlbru5OHvSIueqv0ziXIfGqSGO5P-B-Vl7VZgU-3RXOXzd9a-wZLmdQ49OzYyiCXefE5gMGQFzTr-ImMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
إيران والعراق، لايمكن الفراق.. العلم العراقي يرفرف في مصلى العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/80902" target="_blank">📅 07:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80901">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TH5m5hTmOmpH9OVHfpU_N1LitpDbBuP_FCneNZjMW1onsdGdoSE1g8ERzKoJAMOWJJhNvBz0aAqYzkESb5I77b5J3FDl7LzvtlN0jLuBTsQ3p2C3eSK3wsKxBtJbQCLyrIMZ2gWa92P9nqko7EiVQSlQsyuWLLvdszQiMrb9gUQYn1mcj6hg82rCf72pTeC96b4u6-lkGGYCHOLkJ458iXFjpZsWvMWRliaBiNgQCAiI1ZOTy66A2BxGl_p9PzVlOosLq25ii8svP3CS49xABkzR3k9C69bnRDV3_M4oHkmFKaNmBKQbxc7A9Tc8yCUWxI2sxfcMA6NnVhD966Vq3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
پرچم سرخ انتقام.. راية "يالثارات الحسين" ترفع على قبة مصلى العاصمة طهران.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/80901" target="_blank">📅 07:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80900">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd46b31465.mp4?token=qoa7PxA8nZtc2LH0HOl1RwudKPvHjRYkSagyb8koV6YYf0gt_DP_x1tX7edIivjt1mrpTFgrd3EMM7f243V3nIt57mJBGCsOhnomXcFJ6xs4SP7guCAH8ugwdUXfoZURg5d9Sq22gkjhs7EpO4nqB9Kr6KGvAXrocT5pmerC8htX7ChNL0GgJXuDJrjI3Wapu8O0uxCITQ0v68CFuUXItPME27FvTVbPDG9cey6rqtQL4nddLtK3HBX9D4vyYALDHU6jvp7dDfcO5UjwOaoCsIWAEyZZMGAphtD175wHBsehM-PH5Yp6OujkJZORJ8nWX-czsodpTsKtmpLWCztl_aFOEG75RTujNhDhnE62WrlSMqrme2JzcaRPGHvaVQUmTymQG0RxH6MK0Gxdt94GXScnzqN0ipnPljDVQYO3Icuc5t1D12_n7yJkLL1S6lZYjBWxt5beiQ6lUA8-Z-Sv0k8LXQsSwROTvlSJ_jDL4KS72-os1U523BrBQQPYsxVQ0JDATB1_CaQnmVHopQMCeL5ODwMmY2c_2jn6xFwhcEtwbV6py45ao_Jfq58Bk8Ev9TTfcwVbVTL0RnMIJyWTgS8QgWUDy4XIuJWcP3s0IEN2IUVMXRoehi7w3gj4X7yXgcDD3qGWLccrmZdaR3zxv7CwJSxZAcmXXAwVShfbQBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd46b31465.mp4?token=qoa7PxA8nZtc2LH0HOl1RwudKPvHjRYkSagyb8koV6YYf0gt_DP_x1tX7edIivjt1mrpTFgrd3EMM7f243V3nIt57mJBGCsOhnomXcFJ6xs4SP7guCAH8ugwdUXfoZURg5d9Sq22gkjhs7EpO4nqB9Kr6KGvAXrocT5pmerC8htX7ChNL0GgJXuDJrjI3Wapu8O0uxCITQ0v68CFuUXItPME27FvTVbPDG9cey6rqtQL4nddLtK3HBX9D4vyYALDHU6jvp7dDfcO5UjwOaoCsIWAEyZZMGAphtD175wHBsehM-PH5Yp6OujkJZORJ8nWX-czsodpTsKtmpLWCztl_aFOEG75RTujNhDhnE62WrlSMqrme2JzcaRPGHvaVQUmTymQG0RxH6MK0Gxdt94GXScnzqN0ipnPljDVQYO3Icuc5t1D12_n7yJkLL1S6lZYjBWxt5beiQ6lUA8-Z-Sv0k8LXQsSwROTvlSJ_jDL4KS72-os1U523BrBQQPYsxVQ0JDATB1_CaQnmVHopQMCeL5ODwMmY2c_2jn6xFwhcEtwbV6py45ao_Jfq58Bk8Ev9TTfcwVbVTL0RnMIJyWTgS8QgWUDy4XIuJWcP3s0IEN2IUVMXRoehi7w3gj4X7yXgcDD3qGWLccrmZdaR3zxv7CwJSxZAcmXXAwVShfbQBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
المجرم ترامب:
منحنا إيران مهلة أسبوع لوقف العمليات لإقامة مراسم جنازة من منطلق لطفنا.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/80900" target="_blank">📅 07:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80899">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d8b978849.mp4?token=u94kRCfeKK65Sq4avY3Y8mcXlkqvoeCy5yYFWNPP6uiaU_P58AMENR-jii0beZpg7jM_yXnyvjHRsECAIeHjPtojVXQ2_sk7iYDeeEzK0-4AXm6VPi9f4JpkZ5p-5FIxnas5DfmF3kPaVHxfMjl2t4rtC55yRrGwap7M8MRLIoH5sLQw_PpZGNz2PmdP5WfHUBLzkGm40xqLdgYWVerZuG0-YPc6eo7So1GAZqtAeGsOXZocYkin8S0RevRHImt-DMITlbtl0QHLT1kKuUEL9WGRtvoGothoxQarr1qBWBNjxjc8O5Liru94VCVIxEIbpexfhdbc3HKNg85tqck7KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d8b978849.mp4?token=u94kRCfeKK65Sq4avY3Y8mcXlkqvoeCy5yYFWNPP6uiaU_P58AMENR-jii0beZpg7jM_yXnyvjHRsECAIeHjPtojVXQ2_sk7iYDeeEzK0-4AXm6VPi9f4JpkZ5p-5FIxnas5DfmF3kPaVHxfMjl2t4rtC55yRrGwap7M8MRLIoH5sLQw_PpZGNz2PmdP5WfHUBLzkGm40xqLdgYWVerZuG0-YPc6eo7So1GAZqtAeGsOXZocYkin8S0RevRHImt-DMITlbtl0QHLT1kKuUEL9WGRtvoGothoxQarr1qBWBNjxjc8O5Liru94VCVIxEIbpexfhdbc3HKNg85tqck7KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رايات "يالثارات الحسين" ترفرف في مصلى العاصمة طهران.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/80899" target="_blank">📅 06:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80898">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/350b75f432.mp4?token=nNyP14cbzMtRvUZM7zEQSO7cavTjJ-MHCTMm21gwMbu9bGuo2Z37bYNmRi20wfV_sHctC7DjGg-S0OLoRwE8WubWuwhwNHH9DedrkqSnhLlwiwqYs5wbrPwpS94aXgLyI_7HbqmN9uifCcM8AU3g1Mlb-sXI0nCY7BUcTzDAP7qq6crtIXrlkNLbkR8xV-kRbbcKz-M02OCY6ZQ6sAKkXUTLYmXXgXcAJ0GjOkonPywwNo6JQnjuT538madGUOdJ8esfZ1hgowLysVdkxT2e4y87vPU9GRBHsc1L6jTYV48QdKWmBwex8WIETyz3LKce4g529lrrl0b8LMkj0iKS3FF2oz5SvS_a70jjSocYstUh-XOQ5RnvSVvL-ZjWRl0-NGfsjAwMMruXJeA9TywuxWskjBmpb4dwXG1gXBnQxWbPN_yt8ta6sY2tjpo1FqYvseK_JT8VsM27j_e0duYh0LCOklyrLWH230UEYYVFXAPd2EqK48PiEk_ez7taHw3DV3a6Uu_I7wh_Wgk6FBknp5nYyOXUjvpSyZ2wh3uUcWFmnaWzZ0Ssm9CzzEPEmKXbousV3OUGHsDEeVfE6_gY8GZVLdoTIkgfikI7haIaLqKj_72mNnc6veYE2K4WvGhJ4vWw0WlhQ4w9ycEudYZqirO--Lkqs0EW0FO8nXdlN58" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/350b75f432.mp4?token=nNyP14cbzMtRvUZM7zEQSO7cavTjJ-MHCTMm21gwMbu9bGuo2Z37bYNmRi20wfV_sHctC7DjGg-S0OLoRwE8WubWuwhwNHH9DedrkqSnhLlwiwqYs5wbrPwpS94aXgLyI_7HbqmN9uifCcM8AU3g1Mlb-sXI0nCY7BUcTzDAP7qq6crtIXrlkNLbkR8xV-kRbbcKz-M02OCY6ZQ6sAKkXUTLYmXXgXcAJ0GjOkonPywwNo6JQnjuT538madGUOdJ8esfZ1hgowLysVdkxT2e4y87vPU9GRBHsc1L6jTYV48QdKWmBwex8WIETyz3LKce4g529lrrl0b8LMkj0iKS3FF2oz5SvS_a70jjSocYstUh-XOQ5RnvSVvL-ZjWRl0-NGfsjAwMMruXJeA9TywuxWskjBmpb4dwXG1gXBnQxWbPN_yt8ta6sY2tjpo1FqYvseK_JT8VsM27j_e0duYh0LCOklyrLWH230UEYYVFXAPd2EqK48PiEk_ez7taHw3DV3a6Uu_I7wh_Wgk6FBknp5nYyOXUjvpSyZ2wh3uUcWFmnaWzZ0Ssm9CzzEPEmKXbousV3OUGHsDEeVfE6_gY8GZVLdoTIkgfikI7haIaLqKj_72mNnc6veYE2K4WvGhJ4vWw0WlhQ4w9ycEudYZqirO--Lkqs0EW0FO8nXdlN58" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مصلى طهران شارف على الإمتلاء قبيل بدء مراسيم صلاة الجنازة وتشييع جثمان الطاهر لقائد الثورة الإسلامية.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/80898" target="_blank">📅 06:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80895">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rK4RgX9WsEnIFL9Psb7MGaoV7kYs2AcL6r2-FwtnXv1ErlHxZAu0cv4L102QaZNQ9nyRPNBP_q7n65LuhYo5tIkCHCQIGViCfJzoYYa5V0ILLN3beJPqoZe57c6sXZoqRzH2NELzqg5CcoCvXpb69JldqAYMxH0TLgJVT39syLLXZaB55L8o1RQJ4DLzG0ddJDFEVTxsdcIRf3ckEiKnKF0K--RzaDVm7dDx3m5HKC_SYmi72sjrpnL2S6_fr6q5amMVpwnzW7sz57gTzGVJoWOiT10MC6QNXXZMNn8YacoFUzQyId26IbG-w2jaLoRxyuK5D4yFBF2tMLd5w_rynA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/apWznZjM3N6BgP_7w0DOaAMaCDrrzQVn2lEDdI6omroNLThDTVUT8nv-ppcd8Mjzq1Bobjf_Fs8Fg6yAymcc9NQvVX86gn0xN5h8yggEqNpxjI5ztxPQA2-asJL2oZrk8CwKfiJnv8U32_Zaoz4devoV8yZ1JGqjlYNl83bMbAq4SVECGenOyb5TF9oV-IvnSbd1xA4Te-bp9l5BjGfXZqIgfSweKAMztwmfsM0wgZe-YzMLn4-pIjI4mBzFZadkEB04-ekJhXI2JMtGUYWX9ewBDURU_viOmYA7uZsLQfVJVqCmNfcgg-N1X1L3TKcRS-ONrTwmPn-qGSzoZNoSIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4136e83b6.mp4?token=f4ppaSqowp2swRG_90G2qN4seR_gxEWtVtWWKNW5Y5FSm9Lafd3OFTtF05-0KxjJaHSdfyq46CwmHMTQ4HDtGGw3l1h7JAW_KIsAi5a7fOZEW15lQMDbWqGNGbvNkqbEOQL4t5I2bdU4-JxohkaAd_8vJJYwz3gLFAAqRW0ppSKdfOIVFCIu4T8JwyNcq4h0Lmgs6fa1Kpv7xEHL2kGFKuyY2A9BeO6G-ea4Gp8FkxeyRk1UvP5W4kHhD37oIGFiAcsOyqZGYx2EHa0y5iVVBxGpMyjezRicbGNTprjZwpoW1RWSRDBW6V854pPYjqoQnpypcEDzjMCH4GD7u6ZgWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4136e83b6.mp4?token=f4ppaSqowp2swRG_90G2qN4seR_gxEWtVtWWKNW5Y5FSm9Lafd3OFTtF05-0KxjJaHSdfyq46CwmHMTQ4HDtGGw3l1h7JAW_KIsAi5a7fOZEW15lQMDbWqGNGbvNkqbEOQL4t5I2bdU4-JxohkaAd_8vJJYwz3gLFAAqRW0ppSKdfOIVFCIu4T8JwyNcq4h0Lmgs6fa1Kpv7xEHL2kGFKuyY2A9BeO6G-ea4Gp8FkxeyRk1UvP5W4kHhD37oIGFiAcsOyqZGYx2EHa0y5iVVBxGpMyjezRicbGNTprjZwpoW1RWSRDBW6V854pPYjqoQnpypcEDzjMCH4GD7u6ZgWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
إيران والعراق، لايمكن الفراق.. العلم العراقي يرفرف في مصلى العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/80895" target="_blank">📅 06:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80894">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/on7JrDdBpfkuYBYWCqljsLP0fLuBkVAGdM4uKbp294C-hPmyURux47s2T4cqNRT9whsw9AkJr2ACHKauxXBJTQ-G8AzK3F9_gS4ZBPmRoEoKQRQkzTLn6YYAMn6bbBcsqVI6viQavhcv9-mchIvaw1zk6dhQd1iopASocc-CWp-klh8_aMOOvJAE73ipLJ_y6ma8wE7TtBn8JdU6dZ77atakTIfFa4PwsMPLZo6gTwqDRfS-w0WjghD99C1PpLYl9-HHc6PcF6Jp1nRAgEJ3nqnUOAvQse8xktZmoKHR2CDu4xbmZ6MV0uuJ6sXY-O6ntahMobic2AYcYiZvvkrnhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الآلاف من عشاق الإمام الشهيد يستعدون لإقامة صلاة الجنازة وتشييع الجثمان الطاهر في مصلى العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/80894" target="_blank">📅 05:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80893">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d4462b1d.mp4?token=I3-qFEjM7QLxCgsSz3NnLQ0bg4cDRwAFFRJhF4qzybQI5AogXZE4tdBXx-Sa1o9g8Ncy_JTrCcwyfgLcAKF3cecOzvl-2ROC_byvvNVa9bNFy3IJ_81GQGmoNP_mcAyMj8GAekcXD1yuiH7QixUuO2ap7w-MvkIHSZlzI1t6mXLee1H_YwIFg1jsH9JYe1NMq-bBM9a48qMgqhRxy5rdzGP-AJLalCDHV3wyiffbir7aGTcTAipNHQVRvsrZoAZSCFqxA7S7Z_OYUmKlLzbh8sAQm7T0Z7_CumHMRae3vAeJ4bFRcGt_kYocPq6EOZIvuBz9Trv1Kr93Z0wVj_hwrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d4462b1d.mp4?token=I3-qFEjM7QLxCgsSz3NnLQ0bg4cDRwAFFRJhF4qzybQI5AogXZE4tdBXx-Sa1o9g8Ncy_JTrCcwyfgLcAKF3cecOzvl-2ROC_byvvNVa9bNFy3IJ_81GQGmoNP_mcAyMj8GAekcXD1yuiH7QixUuO2ap7w-MvkIHSZlzI1t6mXLee1H_YwIFg1jsH9JYe1NMq-bBM9a48qMgqhRxy5rdzGP-AJLalCDHV3wyiffbir7aGTcTAipNHQVRvsrZoAZSCFqxA7S7Z_OYUmKlLzbh8sAQm7T0Z7_CumHMRae3vAeJ4bFRcGt_kYocPq6EOZIvuBz9Trv1Kr93Z0wVj_hwrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الآلاف من عشاق الإمام الشهيد يستعدون لإقامة صلاة الجنازة وتشييع الجثمان الطاهر في مصلى العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/naya_foriraq/80893" target="_blank">📅 05:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80892">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9d564211.mp4?token=SPQhhH4MzYcula9DzW941zJnNfCi6p13Pf14fA7AfpeyzOJSeDjQCuAL-XWqj1RLfhfvRkjtdHedoCo8L7r3k5-paeRIzAWpuXw3RVZbY5yj1W9KES2v_idmrqn_KDRSmzSyU4UCTPmpJ6HWLxS-BWubC3_cwH88NlyniB0k1qGdiX8MPJTGm_60lFXnS_q9xKjTb0m-vG-vx3SyKbbuXEtqb4ijjpIWVLyYPxdvhJQsp-lUbo2F6t-hKEXJ8tzgvyJXoP_Zgmjajrh5XgcAQuYqkFnOFXmWYgUiuzFe4S0zZWxATFDUk9OMIYcMAi2gNBgqhTOhxWwH-ZuwswOCLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9d564211.mp4?token=SPQhhH4MzYcula9DzW941zJnNfCi6p13Pf14fA7AfpeyzOJSeDjQCuAL-XWqj1RLfhfvRkjtdHedoCo8L7r3k5-paeRIzAWpuXw3RVZbY5yj1W9KES2v_idmrqn_KDRSmzSyU4UCTPmpJ6HWLxS-BWubC3_cwH88NlyniB0k1qGdiX8MPJTGm_60lFXnS_q9xKjTb0m-vG-vx3SyKbbuXEtqb4ijjpIWVLyYPxdvhJQsp-lUbo2F6t-hKEXJ8tzgvyJXoP_Zgmjajrh5XgcAQuYqkFnOFXmWYgUiuzFe4S0zZWxATFDUk9OMIYcMAi2gNBgqhTOhxWwH-ZuwswOCLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مباشر من مصلى العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/80892" target="_blank">📅 05:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80891">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XC93TGgKQWytpruGGnJ4EQ8ccLHfGAsq_3M0F7CxniiT688rfuGSUpQuYyGa5fHiRLFxNC69797jJtQYDj9HEjxRk7tBergj0Up0zwbioVkEaZXErAizYKpi7CnhFIYA-eG3vF-JwGH8VroOk_erxADgCbj62F1h9Lhj-jdx5rV2equPlToLsBlrfQU5BRhBNL3gcsz4PYXaZOLX4L1WQNlmNKIBbPpNAok32lE3UkXAFA0T1PMeQWLlLB64kV4sLPVjRUG9w6duSQb6_JafNgEiwFJuduzGw6YDHwJuk-Y-Z-gTlIuWhO6CEt-26uJvuC6Wka7uO49t6bgOZ4vzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رايات "يالثارات الحسين" ترفرف في مصلى العاصمة طهران.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/80891" target="_blank">📅 05:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80890">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rr7XN25VNsbCuAqVRtZT1S2b0RpM38wWfnq08AGtznbuf4VuhaoPkcF14O-dfcGu1iB3rQL88BRgA0NcthbHK2pzIQbGDscl1LNbeTqVZD90KYsKLjeenCCtRJBw2NpFwLeUG_GM91wFFeMH78ZVHeeyGCcMj5U3njBF11uZGFlKUcJ5azmhh9zKcawe9q_hkkgi1rPcTbh6wDbMuV38lTWd_ioG8GjlHynZ-Rnzb_QnN4axbqzUAxW7Kn-BpCLCK6Abvc1BRGiJB03LU1jQ3NjjkgzRae9RHegWPW888IP3S94g1MBd5CVm30znxyYrzhFGQ2k4tbRIj6XC7q1Yxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعة ويبدء الحدث الأكبر.. الحشود المعزية تستمر في التوجه نحو مصلى طهران.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/80890" target="_blank">📅 05:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80889">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b7d3170cd.mp4?token=ENLRCZPWWAyYQHhA2USeK_ITu4c-yg9dbVzC9Evh3EgVY3d1a-HBY_mOcHDjgbG4jKr2aICefoLVpnMkqiuZ-Ws13FRkB4xqKyAsL3Mpqn59pNNNbe9jm0XEX3Q-LUKGs_oBjqLpGiK8DIBqVnP3gQbZuyiA8YGZNjXtgUSU4m9WdlsA2qlGu_MTIe34FJJk55iXP0mMfN_5H48twNrs05WmKw6zQR6bQ91CssSEV2r8Ok7suHOTH2xxernU4gg04CHj4a_dvaWrp8oYMV6AoFyz1DMxc9Yu3mGcVzVVtqFsBzEpodBB7euUVozLPdTHU7WSZJD91pSeoqVz44NsSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b7d3170cd.mp4?token=ENLRCZPWWAyYQHhA2USeK_ITu4c-yg9dbVzC9Evh3EgVY3d1a-HBY_mOcHDjgbG4jKr2aICefoLVpnMkqiuZ-Ws13FRkB4xqKyAsL3Mpqn59pNNNbe9jm0XEX3Q-LUKGs_oBjqLpGiK8DIBqVnP3gQbZuyiA8YGZNjXtgUSU4m9WdlsA2qlGu_MTIe34FJJk55iXP0mMfN_5H48twNrs05WmKw6zQR6bQ91CssSEV2r8Ok7suHOTH2xxernU4gg04CHj4a_dvaWrp8oYMV6AoFyz1DMxc9Yu3mGcVzVVtqFsBzEpodBB7euUVozLPdTHU7WSZJD91pSeoqVz44NsSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار "الموت لأمريكا" يرتفع من مصلى طهران قبيل بدء مراسيم تشييع إمام الأمة.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/80889" target="_blank">📅 04:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80888">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/724637f597.mp4?token=Kxjsyk9wdtOp3__OcUdeFVi5hAcQV02tYB8rPI7eMT6sRXSQXRxsM6ef6DSNqxre6SxdFAKGANScmldrcfQdgpyUV5UB1NFaqyH2ul4LCIL2AT_sCTd0r6owJJMIC3ZjLdz1qhx7SvtVjL73NgI-K7cXCqxCUl5kwMs3hZEoa_5TTzC0RlPniXYqMNuGmab9kaU9EQdJzwzgEIyqwPifcotdnhIldTgvc3OYlj-2ztwQP4H7MZiCqzDfRWjuXtSLMXRvGnCNC0FZBhVxawtm_-YcLnwEEo58AxoL-vRiw1fD6Go7HsxUtRR9V2kDeuy1sOiZwebzZQpG0aHoatLDyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/724637f597.mp4?token=Kxjsyk9wdtOp3__OcUdeFVi5hAcQV02tYB8rPI7eMT6sRXSQXRxsM6ef6DSNqxre6SxdFAKGANScmldrcfQdgpyUV5UB1NFaqyH2ul4LCIL2AT_sCTd0r6owJJMIC3ZjLdz1qhx7SvtVjL73NgI-K7cXCqxCUl5kwMs3hZEoa_5TTzC0RlPniXYqMNuGmab9kaU9EQdJzwzgEIyqwPifcotdnhIldTgvc3OYlj-2ztwQP4H7MZiCqzDfRWjuXtSLMXRvGnCNC0FZBhVxawtm_-YcLnwEEo58AxoL-vRiw1fD6Go7HsxUtRR9V2kDeuy1sOiZwebzZQpG0aHoatLDyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنا مصلى طهران حيث ينتظر العالم أجمع بدء مراسيم تشييع الإمام القائد الشهيد السيد علي الخامنئي رضوان الله عليه.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/80888" target="_blank">📅 04:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80887">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqnqK4L_xmIIe1e2k0ND_dk0QC5C3aihScPXKk4Xi-jODOkeYUu7JyoAxCtyqHrBb5nCNgg6q9-vqrxqpT3rUjUkS_zMBZUxgK0Du-OQOWuzstMTSKbhwDXvt_ehEuqSMDZ_eb71DvUX12U8dT7FvyIh-6g5hYNwdsUb3zZun4O8ynnvfCXDATIy02Ut-tVLUlw2YMmOpp313JQu9OphXe-20PcXerzMHm-k_d-NxHle2CMK1-2tLXs2HCT-kZMSw5l5gg8yzyrkn6shtqFKslq54fcFTth5H43yPRKs0YmxkhrmzWI9sk05-iZld_4vE2EzzxPAf6v05GR9a07f2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرق میکنه با خانوادت شهید شی یا با خانوادت فرار کنی.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/80887" target="_blank">📅 04:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80886">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6baa49ce.mp4?token=ZBYmVsaTQDexXJ4yas9OYIHXRiVJDgPAeUuYyhCkm3U8wMMU74zd9DOCB9WXUceB49X-W8r_-SA-RuzFkyg5bXGtwU183ivK38Wl5YRxbJTz4WYXVe2pYx8P9VR_xjfm5ppEC68Xee1ZCT9WAPRsLGdUSRYJMF0REpE5OCJUfnO33Rxqk1qcN7Euup7OMMdUnSHuHZX-hxD-L8De-Ns8YS7wNltcag0sk6kGK16IjB2T4DJxTWhRCXnFzMG64ccbJ6sbZ1pOl7_Qeb25aZqDwz1JzkLcmkt0JoRqxqliIwBdqRGbW2hE2hYOZ6H4RnUw4awOSfp_4BJ10lbS6UgdDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6baa49ce.mp4?token=ZBYmVsaTQDexXJ4yas9OYIHXRiVJDgPAeUuYyhCkm3U8wMMU74zd9DOCB9WXUceB49X-W8r_-SA-RuzFkyg5bXGtwU183ivK38Wl5YRxbJTz4WYXVe2pYx8P9VR_xjfm5ppEC68Xee1ZCT9WAPRsLGdUSRYJMF0REpE5OCJUfnO33Rxqk1qcN7Euup7OMMdUnSHuHZX-hxD-L8De-Ns8YS7wNltcag0sk6kGK16IjB2T4DJxTWhRCXnFzMG64ccbJ6sbZ1pOl7_Qeb25aZqDwz1JzkLcmkt0JoRqxqliIwBdqRGbW2hE2hYOZ6H4RnUw4awOSfp_4BJ10lbS6UgdDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فتح الأبواب الشمالية لمصلى طهران.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/80886" target="_blank">📅 04:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80885">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔻
توافدت جموع غفيرة من مختلف الإثنيات والقوميات والاعراق إلى المصلى للمشاركة في تشييع الإمام الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/80885" target="_blank">📅 04:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80884">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfeuDo9RqMX-3oFw4pKQPjkdSUmqu5pTk6-drhNJC9ZgmQyB4YsJ_HAlJx6-KpcI9d60BB5cSFo97Z5z6BpqXYH_DxAVB8ofC14vrNJmq8u8r338RH5JfIos-8XA7cBCdbZgKx2JzBxoNta-iryWKJhzAZeKbnZ0zBuwX-wYFfN7H8Fu6tW6D2ESMyokMYfjLYwzzB3ejlo_9t_TYVnmeqzYsnVyRlK9bZtMhEJeVetPCI_15T5CeOb5Y14m22q3w_iZ5HXXDuYrWI6xe0xVCorUlV1smlCQCc2xP6Yext7XKZe7ZLuGb-0KyL6nNPNcPZl_2Oa7KNt6P-jeDClRvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بدأت جموع المعزّين بالتوافد إلى المصلى.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/80884" target="_blank">📅 04:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80883">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83e25fbbbe.mp4?token=VXZOF5vwMfG-RaEnRlothDny7ufpTmdczQCnXreVjTAacZzBHwXP1iAr8t81FDfvOZT6pFHzZsYZqoPL07lnkzQfBSng3DpdZuxoHulG4crlTJkwykW9ZHFKeWct7rxREUJMvx_OC163pzLIdll2leUVAdhrfmNtUP7MCKR28UAapc1-DIZySlMGFpmil9YqhRyE_OjU2bPYiBNA8tO2XAZlnZSbbG2VVmAy-TAK5EpsfgroLhXJXt36ayLpqFdl6q26G6TKP5DJkC6ixS_cRCEKym6NFLYbQip_S9Gjhm2Ucc_6o2l0im6cmjAzrcFt0iME-CidMxSNONZX_8qhFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83e25fbbbe.mp4?token=VXZOF5vwMfG-RaEnRlothDny7ufpTmdczQCnXreVjTAacZzBHwXP1iAr8t81FDfvOZT6pFHzZsYZqoPL07lnkzQfBSng3DpdZuxoHulG4crlTJkwykW9ZHFKeWct7rxREUJMvx_OC163pzLIdll2leUVAdhrfmNtUP7MCKR28UAapc1-DIZySlMGFpmil9YqhRyE_OjU2bPYiBNA8tO2XAZlnZSbbG2VVmAy-TAK5EpsfgroLhXJXt36ayLpqFdl6q26G6TKP5DJkC6ixS_cRCEKym6NFLYbQip_S9Gjhm2Ucc_6o2l0im6cmjAzrcFt0iME-CidMxSNONZX_8qhFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
إزالة الأرصفة الجانبية ومحطات النقل والحواجز المؤقتة بالكامل، لتوسعة الطريق وجعله سالكًا لاستقبال مواكب التشييع.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/80883" target="_blank">📅 03:49 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80882">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orMTZYn9JM_LddLfKjYVMDcBRWsfS31gIMxxRIDWTNSCXaUEU1fL9Mvuv9q9_0Q1UoTxK2Sle4aao1pNRjEfmMubXb1hNGs51iNrGDHKXEUa23ebJD9Pn9YUf5YJKYzoudqPGQePDXXgBX1rKJFLTMFXwJ5aIfhFGcxPlfvZPxxF_UCBFD-ZOa-3p0NBDNFITigDBGHxI0nAaj2cl-AJElS3XCUST-hGNgjsNijeZ8F-ybx_OmWLC-eYh7FLI_ZBXtF3qk0ckjX3HY2iZwRv1mLM2R7Tw6glHOcgCOHp3RajIyCCIQUSnQT5p0t_ind20MPSjTxYbyrVLDblNNrb4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
من المصلى توافد المعزّين بانتظار مراسم تشييع السيد القائد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/80882" target="_blank">📅 03:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80881">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11361885ff.mp4?token=W2zWnV38ERu9EKVJiFppPXCOQuP_F2wJKKOjiRpT3Jx80GIIqH1spjysZMeqfbWLBSR0E6VhS5vGEOto8II7B4CY22vJjYKFw6N-4bQR8MLrGXF2ff0DCb421Ds_eIxIRv3PPifL9H-8i6RxuExbmkl-_MGAvPQgxrOkZRQNVK-uJKcO2ph6dCUoGtkF2L_dO7gyyKwPxBBNAdNhrEykV1nn0bqXg_GIETe6tEIAb8SO-aXCqATEYrYT451kaYt5lbkahR3rCcihE_6ip5xf7U0E0V7WfY_y9kKZaxqDqSdtumPguvEBprQLBOGVnCvdZCYiMk_Goolb2HHwaEtKdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11361885ff.mp4?token=W2zWnV38ERu9EKVJiFppPXCOQuP_F2wJKKOjiRpT3Jx80GIIqH1spjysZMeqfbWLBSR0E6VhS5vGEOto8II7B4CY22vJjYKFw6N-4bQR8MLrGXF2ff0DCb421Ds_eIxIRv3PPifL9H-8i6RxuExbmkl-_MGAvPQgxrOkZRQNVK-uJKcO2ph6dCUoGtkF2L_dO7gyyKwPxBBNAdNhrEykV1nn0bqXg_GIETe6tEIAb8SO-aXCqATEYrYT451kaYt5lbkahR3rCcihE_6ip5xf7U0E0V7WfY_y9kKZaxqDqSdtumPguvEBprQLBOGVnCvdZCYiMk_Goolb2HHwaEtKdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
أجواء مصلى طهران، قبل ساعات من بدء مراسم وداع قائد الأمة.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/80881" target="_blank">📅 03:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80880">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/80880" target="_blank">📅 03:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80879">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfwWTiKLtuB4nsmrLV3Vq_TPvmRYbrpLLBLoLjSAsanAcUuhLfE-56ciOc2EEKWCRjVnTBjDuI7pIDF-rJm2mHYysgFOPTNTp3dAy3Rogc1cqyzmvrYjgG9N3Yxy6qYxhDoC8cdcRRVnfbf7fWCBN0R3Tq8MnYdkzENVCxkij89MZrsQr7xQElUihyGXqUfw3svyLx-iCXchlpovoAtsCbusOc2dwurVPU3pAb3i5ftf3Vfa2buIw3Q9wjFW_W2gC5b3lqPrSeqOzXPYLhCda1xCaVpBwS0s7RDu6tKIUQ0u6BpV4snCPMyVyPdKEAvhA2ZbUZNF4lP7WsCClCuBgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ج
مهورنا الكريم ؛؛
🔻
لغرض التواصل معنا ونقل مشاكلكم وارسال الاخبار والمواد الصورية والفديوات ، سنكون على مدار الساعة معكم نجيبكم.
للمراسلة
@Nayaforiraq_bot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/80879" target="_blank">📅 03:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80878">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d3b269ce8.mp4?token=Ki4v_6NPCFhNukSQXRYCas-ffgUVWzl-deU9kFoqzoG-oYwagsmIRMnJTuWUURiTgt1MXfjmcMkYmpJZxsVl8YStXKcErLGXY93kLc0Tks8eHxiYPAVWAVxruqDuNi3h-fbma4j7xgqx0_9jwvYlP_O7idiU_ZhMKPm1UW30i9dycP40SYOMFXLA7_7E5Z8ldkm6OyQBAfHND8SztFvE_zDLM0VoX92SayXMDm8hsZ8bq75bheXvewnPZzLyv09dHu0V2DftoFlFI2SwmpRp_h0aCIep-GTKJfKfeGcUpN7qc0gTwz9hkvCXsLJYTbGHD4SMbOPSS8o29ecSXfzA4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d3b269ce8.mp4?token=Ki4v_6NPCFhNukSQXRYCas-ffgUVWzl-deU9kFoqzoG-oYwagsmIRMnJTuWUURiTgt1MXfjmcMkYmpJZxsVl8YStXKcErLGXY93kLc0Tks8eHxiYPAVWAVxruqDuNi3h-fbma4j7xgqx0_9jwvYlP_O7idiU_ZhMKPm1UW30i9dycP40SYOMFXLA7_7E5Z8ldkm6OyQBAfHND8SztFvE_zDLM0VoX92SayXMDm8hsZ8bq75bheXvewnPZzLyv09dHu0V2DftoFlFI2SwmpRp_h0aCIep-GTKJfKfeGcUpN7qc0gTwz9hkvCXsLJYTbGHD4SMbOPSS8o29ecSXfzA4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
ثأرك جمرةٌ في قلوب المؤمنين لن تنطفئ وذكراك ستبقى حاضرةً في الوجدان يستلهم منها الأحرار معاني الصبر والثبات كجدك الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/80878" target="_blank">📅 02:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80877">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114b80e11f.mp4?token=oToVOhwWfIRLj8dSh6wRSzyfH-eLQcpYkx4i-bCq87VzUZe7MFJym5Gk23f5VvURU3MDIN1XNZdg__zLe3DKae3YFnPNRO1fQAgMF5-Ao8YhFuP4yfoUcOgpXTtjG--p6nTAcXLGn7jm_kUlRAe99ELyDQPZoP3--28N5199Swrqs2Cu4ukjuhF71F7x28BMH1kO0qly0GadL6uNHbJk1YAhFNvSoZcLUiDusuZG6Buo52dU2gVyZoRymKjYg0xol8FUxNiLkv8T2suD6hYRv5-zE_T2n-cD-ruPepwDrm5cmQzWmThCh3rE74mKQj_QRve_OCq9229L36iVqtb90g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114b80e11f.mp4?token=oToVOhwWfIRLj8dSh6wRSzyfH-eLQcpYkx4i-bCq87VzUZe7MFJym5Gk23f5VvURU3MDIN1XNZdg__zLe3DKae3YFnPNRO1fQAgMF5-Ao8YhFuP4yfoUcOgpXTtjG--p6nTAcXLGn7jm_kUlRAe99ELyDQPZoP3--28N5199Swrqs2Cu4ukjuhF71F7x28BMH1kO0qly0GadL6uNHbJk1YAhFNvSoZcLUiDusuZG6Buo52dU2gVyZoRymKjYg0xol8FUxNiLkv8T2suD6hYRv5-zE_T2n-cD-ruPepwDrm5cmQzWmThCh3rE74mKQj_QRve_OCq9229L36iVqtb90g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
ثأرك جمرةٌ في قلوب المؤمنين لن تنطفئ وذكراك ستبقى حاضرةً في الوجدان يستلهم منها الأحرار معاني الصبر والثبات كجدك الحسين (عليه السلام).</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/80877" target="_blank">📅 02:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80876">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50a191d7a6.mp4?token=l2ZI5F_Q4cc_bmpnO0Fxqj2EnyTa9Y7UhffkbN0tSoOHDu6KnRQxYvffoTabogIs_u1B4ZcJ6xQDYpNbk9n1Inc30dNqAGzBV6iNeNg3siT02Rim77YtSD0fgJcIqXiBWFWGcA_KUfAWb0qeKHdo3MOYq-_2bp3M991E6m8502KDc6kWcfH7GptT1HlTfyawLApQYAIW69L5LxZoxo8k7GcVzCYAw4bCuSp182RmDznI39gtEueC1AqnWrjYUmp7DLXzBVXFkZdYeuSJtqtfYHUI2bxo1ZbuhGuiMb8iZgWpoPuUYPFjiyzu4fy3THR-5_oQtldG0K--ttgm0xx0eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50a191d7a6.mp4?token=l2ZI5F_Q4cc_bmpnO0Fxqj2EnyTa9Y7UhffkbN0tSoOHDu6KnRQxYvffoTabogIs_u1B4ZcJ6xQDYpNbk9n1Inc30dNqAGzBV6iNeNg3siT02Rim77YtSD0fgJcIqXiBWFWGcA_KUfAWb0qeKHdo3MOYq-_2bp3M991E6m8502KDc6kWcfH7GptT1HlTfyawLApQYAIW69L5LxZoxo8k7GcVzCYAw4bCuSp182RmDznI39gtEueC1AqnWrjYUmp7DLXzBVXFkZdYeuSJtqtfYHUI2bxo1ZbuhGuiMb8iZgWpoPuUYPFjiyzu4fy3THR-5_oQtldG0K--ttgm0xx0eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصورٌ كان يوثّق مراسم العزاء على السيد الولي في مصلى طهران اليوم لم يتمالك نفسه فترك الكاميرا وانهمر بالبكاء تأثرًا برحيل امامنا السيد الولي.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/80876" target="_blank">📅 01:40 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
