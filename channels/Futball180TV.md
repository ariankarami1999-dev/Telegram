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
<img src="https://cdn5.telesco.pe/file/PWwb8sLpbgY0ZCNmZQLYm9Zam3CDDTGTgSh341yY00As8IFeXc6Yz9kjw5PFeDoH0cPDDlDtyh0ATYIOUffxHGM8t1B_6FtOKz1dyC7PT8JRLj6euAFG1xQVFpkM30LbnEdVI7VljHokLPFTyhQWMsZzL4z--roudc2rmR1jTVvzaJKc6HjbX_d3ePqCWvp36MaaCOmpBlk4qXzWXZhurtzXp_nfiP9xXfgSIF38tHfxV_jESyY-3PuSEPayEwAcTupwZBiw6z4rPuaH0qkwe9cM8SkxwXr2khVWdUNDBc0vnvP0shln7v-omG2DzjFs89dUres9r3_EiCpxqx7CMA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 539K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 13:47:57</div>
<hr>

<div class="tg-post" id="msg-101649">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNm20_BFAwrUPw3tRY6UKH1IvQWBQo-CbpVT6GeXhqs1bNv4irF6X3HeackwGlx6rEzkWi4ckJt8Hv9QjG1FXDTocet5nMQ21KNnfP6eoef8bx1kvGIDDpziZNBshUl4YbC-bcYbwYHZDeFSI3JVI-dE_Iwx88YSRvdSERUsRyyO9bS6BSnK_9YNEGycZEa3f8uUVvWkgPPs4Ogi-TTWO5e2ZsCN9vUdyRBT0ZA5ZX9sAtMYygDJN-hF4LqPb67yM-rkSZOiYo4tQd4mMz7SM86dlOC9SrEhNIP3Jz3pR_bjNROt0hiiUBBZvmpT6s1KLtN3d_DlAJNFBYSLfFu2fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
⚽️
#فوووووری
از مارکا: انریکه در روزهای اخیر با فران‌تورس تماس گرفته و پروژه آینده تیمش با حضور این بازیکن رو توضیح داده. قراره تورس نظر نهایی خودش رو بزودی اعلام کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 304 · <a href="https://t.me/Futball180TV/101649" target="_blank">📅 13:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101648">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f57cc284b.mp4?token=n1dGlXSyxY50yVbXOffz3Q05Gvx05T6sn7fwxxZ0Po768Gv6-5mzzWbp4wqCK-iARp3rmu22eGhca1N2LYfXBdOdIfH21whX_WyTgXjzPwgiE2etjcJ87bODdAXFadx6qJDuNZCF7LrF7ZdXHdXvweQlFX5EVAAyjO1OM_FJG9v5DtO_PqbVT_PoyJemX7XhR-BV7SekJR_wyEsyZq1hHTTidaBrIbbNKrFUeBYCYmRYLk4s6FeLkoCg-5DeBs-GbGWgA4v4kxA85pUY-2Zr_9aIFgPXMWyeBmMq6jPts9Dy-Xz1esEVs5Hw1XXN1sumf9GMLcFk3TW7LfilvWAM4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f57cc284b.mp4?token=n1dGlXSyxY50yVbXOffz3Q05Gvx05T6sn7fwxxZ0Po768Gv6-5mzzWbp4wqCK-iARp3rmu22eGhca1N2LYfXBdOdIfH21whX_WyTgXjzPwgiE2etjcJ87bODdAXFadx6qJDuNZCF7LrF7ZdXHdXvweQlFX5EVAAyjO1OM_FJG9v5DtO_PqbVT_PoyJemX7XhR-BV7SekJR_wyEsyZq1hHTTidaBrIbbNKrFUeBYCYmRYLk4s6FeLkoCg-5DeBs-GbGWgA4v4kxA85pUY-2Zr_9aIFgPXMWyeBmMq6jPts9Dy-Xz1esEVs5Hw1XXN1sumf9GMLcFk3TW7LfilvWAM4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سیدجلال‌حسینی: بدترین خاطره دوران فوتبالم بازی معروف با اولسان‌هیوندای کره‌جنوبی است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/Futball180TV/101648" target="_blank">📅 13:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101647">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b841d71bb3.mp4?token=hKuIO07qLHFg8KO6y-7hP4XcE3fn_CyuJglrRolcgrlbmEhQZVdSQjLOYBdMvAYeZG6Zl9Aoo7ZcD_prkPWrqAf-Mtmva7onvzxCd5EoWFIrYeNKnAQqRV_ljojixDkGZKe08aBDMFUDwh4Iz8AzDlV1YZWOBzdXj6v0VW7SuzJyignW6B4bWiMKPa_EsnzkjbLB3qbbSoEmZZuDhaHXwqygzFULZff46QIlUDT2hdMU87GZ5smMnXntJEL5Osfo2FRqeV2RsA3NZT5hw3FZVZ12yzfG54WTz8667_cBQNDsZPx_a1l7OgdHTerCQc4yCc7XSv0bWLWz8jxviKFdUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b841d71bb3.mp4?token=hKuIO07qLHFg8KO6y-7hP4XcE3fn_CyuJglrRolcgrlbmEhQZVdSQjLOYBdMvAYeZG6Zl9Aoo7ZcD_prkPWrqAf-Mtmva7onvzxCd5EoWFIrYeNKnAQqRV_ljojixDkGZKe08aBDMFUDwh4Iz8AzDlV1YZWOBzdXj6v0VW7SuzJyignW6B4bWiMKPa_EsnzkjbLB3qbbSoEmZZuDhaHXwqygzFULZff46QIlUDT2hdMU87GZ5smMnXntJEL5Osfo2FRqeV2RsA3NZT5hw3FZVZ12yzfG54WTz8667_cBQNDsZPx_a1l7OgdHTerCQc4yCc7XSv0bWLWz8jxviKFdUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
کریم‌آدیمی برای عقد قرارداد رسمی با باشگاه بارسلونا راهی دفاتر نیوکمپ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/Futball180TV/101647" target="_blank">📅 13:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101646">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c225ae4bf.mp4?token=U4UK2__64f870EtCsEaLgnagzyPmSZhx6PWCDA_5aXp8q6fLk0ehpQmBOVmlrMKoqGlrZiHgvlYgAhCqfGQURurHYmGHj001-c4WHmwmThDEyYMNQiynFNoRkWPEWSI-D63tlMASgIdc7A-oadMgvXds5otFWLVPvmhHQTVE8bhOVzQkPMEdUAH1GLC_PFiXBLu7zBHZ_kU1a_77_rrAUgBWCNtm5MIG5AVhfcxyQ_wp4t6rhx2PwSxbBxNK9QZ_7zQ1G0RhlNRIEvJj7lsd5RNzmUu7he9zZPcW6DUo5lkprny-4sPyJGLcWYRkDTyg-g6T09NtMxGcVxG0gigvp4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c225ae4bf.mp4?token=U4UK2__64f870EtCsEaLgnagzyPmSZhx6PWCDA_5aXp8q6fLk0ehpQmBOVmlrMKoqGlrZiHgvlYgAhCqfGQURurHYmGHj001-c4WHmwmThDEyYMNQiynFNoRkWPEWSI-D63tlMASgIdc7A-oadMgvXds5otFWLVPvmhHQTVE8bhOVzQkPMEdUAH1GLC_PFiXBLu7zBHZ_kU1a_77_rrAUgBWCNtm5MIG5AVhfcxyQ_wp4t6rhx2PwSxbBxNK9QZ_7zQ1G0RhlNRIEvJj7lsd5RNzmUu7he9zZPcW6DUo5lkprny-4sPyJGLcWYRkDTyg-g6T09NtMxGcVxG0gigvp4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
یادی‌کنیم از دوران درخشان سادیو‌مانه سنگالی در ایام حضورش در لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/Futball180TV/101646" target="_blank">📅 13:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101645">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UB-0gjFjI39iLKz523C12fUEA89C9firbZ7I3TJdx1h96MdjIQx80cDCH3LzuTZv1GMeu2AjppCEYxSxKyIZZgXM1M8q4AGASEGnxO5ojdJ1ZhBSI11DAqDlYRTsKMx14Qeb7H-mD8fcv0RRRv3sHh68Sw4AH8o0JCqfsi1UOiPstR-tB3XnGTk4SDIh-wwmsSFXRS3k9618L9fWEcBN-DawKtSbVacUWCaCq_7tTHt7m1bAGLho4axCgd_dgswLDJxzTTJe7PgEsejjT02I6XBcFrvv7TjkG6mfE8zYaq89eSBleAaqU_NsH7ji6KY3sp96fh9VepDD64pWdWRdnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/Futball180TV/101645" target="_blank">📅 13:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101644">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZzkipYEJdDbZu9DNq4hyDw0wR-fkemTVt0aZDbfll-6L7X4N2sCJtSAKRvVV3Mx2w81H2_6QDnGNzxjfxI15O5aXlHUGtfSU6shqD_YsjJvH91nq4nwDZpNoLF4smRCaVv3eGzpikV4lk3kfgRsbpfrMnY3KZO92m_BZQ4PJZT1JbamlxSzV2HPmBfT-QmdekRHdveJ6SVhbv4k9hWDBwfFEQqA6laP8aAJd28XBwAU38MOKKYCZed5ujrLecLsxk0tfulfSMgmrtxvQ4LZmh4RIz6uD8uitjmWfCX-lZT4IW5XCgRA1Jayf3T-0ESzxt7H-1gkJiLWcZ11OtCaBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
مارکا: رئال‌مادرید فارغ از جذب رودری، تمام تلاش خودشو برای جذب اولیسه به کار میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/Futball180TV/101644" target="_blank">📅 13:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101643">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2BluY_gfOjyfl102Gr26qBniqJa0rl7a-yns9Qt2Heqd_4ETewu6uDcP5RL4bvgtdN7gNlc_BrvYLOUq6bhdHMVUQGBMXY1MZd2OM0QbEZevMTyhvCIRto0ks8m4ybGwpE5f5Hri0m9JXIylqmqw-Hl-yQJhltzRonrIAZGXaEif5-eL29kRCInAMjuV8gEPbxIpNM1oNpF0Hy404YDqwfnyrnqHEcAhgcGNBGj2a7AiCgm8zY-TCZU9EKV_4x3bkWvGDOuGTuzxfNgQ-gNGa8QtXskOse_78RcHOoshRlE4y90H8odabjDLDlkWrmRZKDygmj8vyvEucy5u4KxqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
مارکا: رئال‌مادرید فارغ از جذب رودری، تمام تلاش خودشو برای جذب اولیسه به کار میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/Futball180TV/101643" target="_blank">📅 13:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101642">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c46077059.mp4?token=iW8KNdKeyjip4w_FVUQeqGB8VBwCnXq26sFT-4ppfGPrzNgACL0bhanqEGNcjWGn77lZ9HVMuBWYB-iKk_k_g1Lr-SSz6gSjwg_a5zVJQGvWt42XFyvUaRJp5e3aYUP0t2NyLB8A2Nt4d3kUkjqfRNzuKqhnHfagCexlJYuBLFiabbWVK8yeJ1u814c85UXbZJl1oOCBD5cHCcnJOoAfAdVTJehcNbpsCRdxKQs3syadx3bfQzWbLs_vPvIAteBt1aJznmvowZEavhJmBmIkaY71wksjXyyEBaBbku5uVmGW2osK4_MEKM3eUJ4B-wKKCGSgrZLyAjAz7MMyYifuyEgaWPPUALuboqV07fHFpYkg6Qo3cq1IM4T7bGOuyZggm0iyBQEsMQDUr3ljTzB1e7hHyhJMYaEkvJbHDy1wvKst4cG9jhfXAmtSsy8nsAwWwvt8AcZOJRYgBnlyFOFh3vH_IPOvf_74jUJ9ak_Gpevr0XsnohAmMhIA_AeyVbGN-11IoWccNrnI1LBf0T6CQ3HnzjMaV77teheOvqs8lbkdeqT8MqRuWVmFM_-APefnb1dFJzApArkIo4bC4TgSkhQ9p7OLMB4oE00jKDH29THUHCNNar2oLpVxQEn6jhiXS8RfPq3xapQIvvXZRsoFkCcQSkcpHOXhkx525pppzwY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c46077059.mp4?token=iW8KNdKeyjip4w_FVUQeqGB8VBwCnXq26sFT-4ppfGPrzNgACL0bhanqEGNcjWGn77lZ9HVMuBWYB-iKk_k_g1Lr-SSz6gSjwg_a5zVJQGvWt42XFyvUaRJp5e3aYUP0t2NyLB8A2Nt4d3kUkjqfRNzuKqhnHfagCexlJYuBLFiabbWVK8yeJ1u814c85UXbZJl1oOCBD5cHCcnJOoAfAdVTJehcNbpsCRdxKQs3syadx3bfQzWbLs_vPvIAteBt1aJznmvowZEavhJmBmIkaY71wksjXyyEBaBbku5uVmGW2osK4_MEKM3eUJ4B-wKKCGSgrZLyAjAz7MMyYifuyEgaWPPUALuboqV07fHFpYkg6Qo3cq1IM4T7bGOuyZggm0iyBQEsMQDUr3ljTzB1e7hHyhJMYaEkvJbHDy1wvKst4cG9jhfXAmtSsy8nsAwWwvt8AcZOJRYgBnlyFOFh3vH_IPOvf_74jUJ9ak_Gpevr0XsnohAmMhIA_AeyVbGN-11IoWccNrnI1LBf0T6CQ3HnzjMaV77teheOvqs8lbkdeqT8MqRuWVmFM_-APefnb1dFJzApArkIo4bC4TgSkhQ9p7OLMB4oE00jKDH29THUHCNNar2oLpVxQEn6jhiXS8RfPq3xapQIvvXZRsoFkCcQSkcpHOXhkx525pppzwY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
▶️
هنر استپ‌ و گلزنی از برخی ستارگان فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/Futball180TV/101642" target="_blank">📅 13:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101641">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQTQDCu8aQ7zuakpbUfXhCdFY630mx3T3ZH65N2na0qIuah-jP822Sg92Cg1PB3ka3JrKp9YrO3c2ASwBNe8vm5ipDmG6nYvvbDe_9N9_SVieyivkjlGYJKtDRYVKKUzRV7BdVU2hgpqShYBFieiuMDM4meuIoqOL2-D84XLs-UMHd6SyF5Ko5jlG3CHkVTu1e1ZibFbZ-X1lugSQNST7beeuV8MMaq3gCmkorvfd8l7yOM6knAO_DHKvg0_9Qr4anGLpoj9NXs0_BgKaMxrwB567Bolo1O2kEaTCCq7ztot1aYMJJEzQhqdbPrIIjV_n774vuj0UZI92V-Ici7mkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
باشگاه بارسلونا در صورت عدم جذب آلوارز، داروین نونیز مهاجم الهلال را زیر نظر دارد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/Futball180TV/101641" target="_blank">📅 12:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101640">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1YpMlAmcb2NTfC5Yj4ilbI8_iJx9dqH0osWatlmZoAw56x9ZEpNi-g0txXhyujO3PdIP0tgJGECG2YG2F_cxO2c2ChfZfSDpi9WrgU6I2IsU_qhGSgw1fa-q4uAXPIoTc7y2YA7OIxYhQI81s7lqMuRKTkxpdbTEPd06cYccn0cXutFa65leidiYMxyp-X12y__gt83Lb4mInda3_Q8ddEN7nOs9sF-tdTQ3mim3hyYS1_O5rEOfWFzcpW18s-KlRFw5FuD8l20x1iUcCATu9T4RA1YBs48E9m_NJoPhXI1I-QA7ybLE-jITcyNa5QFTT4LTj16LU7ZXbBA5K_9-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
😢
خانم‌شکیرا و چنتا از اساطیر NBA
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/Futball180TV/101640" target="_blank">📅 12:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101639">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8fa0ff87b.mp4?token=MKTI8OAOR_1UmdjBIn-UDl8L9Vd7H9QuGyf7W7FCPw7yU5AflqcY9jFJCiduj0GycCv_iKHbrag5gjlvBdLNujkWcl8kTm4CHsiA2NyzfJpDMhOmUt5WMZxkc9NEfx588_Ol4Ed7WnLEcI3_D5vOHZcqjJrt4dJTllyf-sQKSl_9sxqrCT9hmlSbKVDxwNWtERZmnNqByHX7-5Wga0vDpOTvhRdxolDGJ6DjlkovWGCYDYZSTEilasGkxR4rELYO-PLOZ0iPwhYSmVvAVVMn_DFnsYJyuojZ39lrA9FhMLXAOQdb_Cy5o7n4ez_RWhKlKhFJ3P7KX23PKYr1YnFB8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8fa0ff87b.mp4?token=MKTI8OAOR_1UmdjBIn-UDl8L9Vd7H9QuGyf7W7FCPw7yU5AflqcY9jFJCiduj0GycCv_iKHbrag5gjlvBdLNujkWcl8kTm4CHsiA2NyzfJpDMhOmUt5WMZxkc9NEfx588_Ol4Ed7WnLEcI3_D5vOHZcqjJrt4dJTllyf-sQKSl_9sxqrCT9hmlSbKVDxwNWtERZmnNqByHX7-5Wga0vDpOTvhRdxolDGJ6DjlkovWGCYDYZSTEilasGkxR4rELYO-PLOZ0iPwhYSmVvAVVMn_DFnsYJyuojZ39lrA9FhMLXAOQdb_Cy5o7n4ez_RWhKlKhFJ3P7KX23PKYr1YnFB8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
سید جلال حسینی: اشتباه کردم همه زندگیم رو برای فوتبال گذاشتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/Futball180TV/101639" target="_blank">📅 12:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101638">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoaHS77mjbLzAqc3yRMAKZs5MfxFh_Snb8vfUutjG7sapZ_JQ18JeLJlcbmYAKAcDQzzuFxmPCjP77hKiz8bwlTTiGMG2Pd-zCu03HdN-wyQdr0AgMLrMImLUcQbK4bYRRlmsI4_fJXJHWq_QpoQebEfig6MjfRat8lm0pfHXEWzcAuOsm9FMKPt1Qnn4fuuUUmpcHjEYOwmxGSiM62YdYieQq4UZkCW-yY336e_3cviaarXmgvQJV0j_K_uc-HMw4avZ597wJhn5xbtN9jqiM2o2JfV0FRAHUbZ6YiAnU3B6_ut0OrGI5A3i8oXK7fz-YPs_srln9Bn406GcciOJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📰
بیلد‌آلمان: آرسنال حاضر است برای جذب دیامانده ستاره ساحل‌عاج مبلغ ۱۰۰ میلیون یورو پرداخت کند اما این بازیکن خواستار حضور در پاری‌سن‌ژرمن شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/101638" target="_blank">📅 12:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101637">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e657d4048f.mp4?token=HtdMqQ1S46hWzVepHLJHG5jCBDmJ3iasMxkboArj4NEEQ58MVz3-tqd2c3bMquyXtd1j-3ItIVm9MU4o1UOhr0HZYU4W-Atvm9BaRlddlqInzNOJRZkiMO70-yoaihMO_Z1-vUJB5xXwWMxWAT_o3Iw76A3TsRVTFtj9K0mMe2zaIxzMz6UAkZnEO9vd024m4NPjU4CYN1vvFiOVZtEcynYMtBclwhCO3HtR4jIcjuc-7uP9QTUx26rkS5dHcS0d5awRzZLC3l7lMjlnMvk2XJsss2CeCnvBb-ul-RLhYjFqRm2hd0hNMSFnT6ovrvILfjH8gYrjSVJJ477Ge7m6H1-uTSBZQG1l2fUcvP4PWiRUVtCUYJMizUmPk7txe6lbXafDxQUFrxIxmmMrihOYcwq_OKHJmnLqeyJpV4e_8q8tRUToOD7nyjK11HlhPy2p7O3FKsOGj1uklS9LKTHRUnKTsMR9oCHHHxf0jwUxKD14tsUWjjI5E1bPWM3tSyd4PW-XpUrfc3wQ5KY3pGWEyOBAGT0x14KwWoAK9iqzi-lq2Ii9DUOeUgiZ0At8AEPsbTcHVt24d7TPfsR-WAQhKNOSw0X6L1knlWvKIc8eIza8ksjeebCRB9XL7D5NOihzz2x6nMWxDTAtrdDBoHZ2T9hJCM_KRaC2SrhsAJmP188" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e657d4048f.mp4?token=HtdMqQ1S46hWzVepHLJHG5jCBDmJ3iasMxkboArj4NEEQ58MVz3-tqd2c3bMquyXtd1j-3ItIVm9MU4o1UOhr0HZYU4W-Atvm9BaRlddlqInzNOJRZkiMO70-yoaihMO_Z1-vUJB5xXwWMxWAT_o3Iw76A3TsRVTFtj9K0mMe2zaIxzMz6UAkZnEO9vd024m4NPjU4CYN1vvFiOVZtEcynYMtBclwhCO3HtR4jIcjuc-7uP9QTUx26rkS5dHcS0d5awRzZLC3l7lMjlnMvk2XJsss2CeCnvBb-ul-RLhYjFqRm2hd0hNMSFnT6ovrvILfjH8gYrjSVJJ477Ge7m6H1-uTSBZQG1l2fUcvP4PWiRUVtCUYJMizUmPk7txe6lbXafDxQUFrxIxmmMrihOYcwq_OKHJmnLqeyJpV4e_8q8tRUToOD7nyjK11HlhPy2p7O3FKsOGj1uklS9LKTHRUnKTsMR9oCHHHxf0jwUxKD14tsUWjjI5E1bPWM3tSyd4PW-XpUrfc3wQ5KY3pGWEyOBAGT0x14KwWoAK9iqzi-lq2Ii9DUOeUgiZ0At8AEPsbTcHVt24d7TPfsR-WAQhKNOSw0X6L1knlWvKIc8eIza8ksjeebCRB9XL7D5NOihzz2x6nMWxDTAtrdDBoHZ2T9hJCM_KRaC2SrhsAJmP188" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
▶️
عادل و جاودانی؛ دو مجری، دهه‌ها داستان!
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/101637" target="_blank">📅 12:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101636">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJMZCH7caBcKfXO54NeZIaUyGFNfJ1KRoyhvFldhH4-nhIJjTPkcQ-bChmwxoPuqPDIPXHBjVGUQt-mWnit3Mrp2RdUctotc7AZC_ceBuVfVXxVU4DKfm9Wtlwvy46YpDC-j8ziirow9Wm01tL2Feo4Pa1RrcKWQGEo7V5GNTUCnEuZXo28C7i_Wos1aTXRZHtt6YOPY1bWe6Xeml25YSAcQ1XNn32arg5FtKBcHqqyRCCrOoPq_wC41Em7kea84JltVk_z_tP1NOkHN0kitNnauM5crrpCcqc0IlIZyKB-cS-kAM2PFnv3aT--L3Sfcl2EJMft5zy24Yr8zysZRjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مایکل اولیسه پس از تعطیلاتش باید به دنبال خانه جدیدی در مونیخ باشد. او از سپتامبر ۲۰۲۴ ویلای ژروم بواتنگ در گرونوالد را اجاره کرده. بواتنگ اکنون می‌خواهد ملک لوکس خود را بفروشد، بنابراین اولیسه باید تا پایان ماه اوت از آنجا نقل مکان کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/101636" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101632">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v3DTjE_NpgnrSWErLrDpTiOdVc5GeTcVSLGT3AT67c9Wag7VAi-KmskcA3bIRKMUufKPUQ4gkJ6yG3oUvWb_oTcQ-Rtd5Yqorf_gpp688yb4ZNdGj-n4HWInXJkNMrWeY_ZpS8vFyPXOStH1PnL7qWEg55CK7Ib6qRZYpW7m5Fewl7_iKKpfIi8pn0_WYvxNGeVd_WF-JPvrAO9_bMO0wNN8C3pOjkSdklWK9RpZQnVmoC7fXypL4CnNYJO2Yz0g4cxnr12VlsBR6C32N_luO4mH1-Kvc6pQ82c_gGFckZ8klct2dzUbnWs3HA_juorJgxD_ItUCCUiTMskDBw_llw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aHn5aOL8pXiX3xG5A6LP3N9F1p7n4ueCvHKHHHSdo_xFg1rpMlFYFswE3E0JskNbRrT-qUAJGtDNqVmfWUz6kcMz3ry1RYPldS0rGfO62_PIJlcxLTxc3m22O9hfS0PS7iJtHD4OVu633GsaKxgvYIAFwkqSM9wNncTpY2R4yNTaFGvBx1hTGPs4NknXO_e2w2D95dxvTYDs1djPozhmOxkbTH5FWHrMMzaX0lXLlImzhUiR4xbhS3Onix3iOOqjNtDxWOc5PXPAnvdP8pbSdrGAQikNtoM-WGFzNp7UX82dEsBD9p3lcflLK3vLU7wpagqN9vSXZ867uUwcSmJzkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cEyjgrm9o5IGmIyl5Uxa_2jdBd46HMvF419gztY5n1iiCWJfcKQgWSpVahnjNb7T-ur5kTWl-yA3RvktA56up_bLekV8yxerOli39fWOFDTm9BuC1A24C2uMeFYeEhXjJHGw67EkaGoCh3sN1oGeRTpWdMtXJNcYRJXOWkElqs1RefpnzQzcETo8zGpDOi6eD5hCR0Z7ByQGiNTwNSOtUsu-XJhx9PwKyd4JBx9iNQjCb-_m1HcZq-lJUnnNl17L0xsLDxSOC-QcXTeO5N9X1cJoZtNwD-frPALLAnQMjGQEu_p_SzT8dYvGydKghTFaE7LXEfG8zjh0hHWREnsrqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G3VNxD6xFHK9uGfoiFnJHXbCjn2KYaLh98bSbwLVAw-dPgzBD6eDGCT5pTvUi-w5iKpHD4ehTFWu7RT9zfrVhGIXmKoDvwQ109ga7YBr139ib2eKa57PATqbsmoy_qR9xWRgW7c97igun7FJF9k5L3WfFbTyRooglep4WuhE_AsYKRUPPgAPf36h_L7j6kQTW0e6_KiQ42pWg50KSTOwKMq91YKtzB95p_vichwChX3khQd_yF-5TbExW2uyuoglpGCWnQzNTAWWXQiX5VaF9ILkdVpVbKlcdi-oHJ_twOIUeCSsbHZT4YMiHWEu8hLvSJE8mpTpxyFZl1o6NJM4Gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇸
کیت‌لورفته جدید رئال‌مادرید که قراره فردا رسما رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/101632" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101631">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsKyoqlWRxZf6A6WsqKLY79ChaiDquHD39QOxmIxMOzktVHN-Uv6zCX339QjMLgf_lLdBokRhJDEHkM46z0e3pSnKxt6L1GxuzFwhXWyZdT8UO7G7yqyXSb2bsT6q15F6-YAsEEHWUyqJtQ0pHFdGkizpSNXVQ6U2MbZA5_Vztpw8XrR69GBNHjEDBIvqunYTAEsUASrlXFazlRhMeEQGEx24sS6in00sFO81ppwZNnHLKvOaKIQLntFRqJpMdetG3Cd5an0iDa3VnSCxkjwTYEFtjXWCKR5p5N1evmZMID-jxImp1ZqN1aw4NzskMwtcDVXU9kyQuHGyF5oBLwE7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
هواداران آرژانتین بعد از شکست مقابل اسپانیا در فینال جام جهانی 2026، یک دادخواست برای تکرار بازی فینال راه‌اندازی کرده‌اند. تا امروز بیش از 61 هزار و 500 نفر این درخواست را امضا کرده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101631" target="_blank">📅 11:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101630">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W66tuXdqWeUDlZg_bwj6uGKJG340pdvjqSvgnl1Wjv-StwTDM3hQTjcxBI4KE73IhAJYctr-O3EdfSfXQpiSKCHRV07ffoWlNkNlh9V0n65XrZdPVgadKHo53cFGv1RlEchk37P7fe50hk9KbmI3Tx0jG-u5quZT06g_WJlAnjYvikSkgb7k9jwxjUQIWkETMq06ypdUTlFIAezrXEZi69gtl85zxzhQylImcAHjiw8t7S4f2IoBLVmli9Jqtd6qqbfLWVm_NWB-cSS05KCdA7jDgYh0az0BJUvC5B0yi-w5d2sv_AWpo7bAkGVDry46qfWuhoX1AVTdMNXhwNgnhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
❌
لاگاتزتا: پپ‌گواردیولا پیشنهاد تیم‌ملی ایتالیا برای نشستن روی نیمکت را رد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/101630" target="_blank">📅 11:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101629">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fde3785bf.mp4?token=eaIqlV4Zhr8Cxo8Et0SFkfOGX8BpSg6pjZmWlsazWHUP3E2fWb4qQqb369ibiu5Ea1ffUUYR8WiDd0YlPobietqnFfe-bnn5ZTT-9FKqW5o7bDtdq_86lg8t_oCp9iATnlEYzTmZ9azQ4gji9biYLv6nfvLuF0kbK48GVq2BMeEV4EK9fgJce1fxbe0rzjsX0DzfYAkRN4WTpn2LpgeU9kQufPAzUXdwnREzhs4Tep9oINuLxrXucQ1ERu6QkzUAA5bHc_toRfclAkadnEnp6Ik5YIuYBFG-2LH-6b5oi6ga63sCmKjKIpU5QUTAwqoK9LQxI35Yi8Sljh36QlBeTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fde3785bf.mp4?token=eaIqlV4Zhr8Cxo8Et0SFkfOGX8BpSg6pjZmWlsazWHUP3E2fWb4qQqb369ibiu5Ea1ffUUYR8WiDd0YlPobietqnFfe-bnn5ZTT-9FKqW5o7bDtdq_86lg8t_oCp9iATnlEYzTmZ9azQ4gji9biYLv6nfvLuF0kbK48GVq2BMeEV4EK9fgJce1fxbe0rzjsX0DzfYAkRN4WTpn2LpgeU9kQufPAzUXdwnREzhs4Tep9oINuLxrXucQ1ERu6QkzUAA5bHc_toRfclAkadnEnp6Ik5YIuYBFG-2LH-6b5oi6ga63sCmKjKIpU5QUTAwqoK9LQxI35Yi8Sljh36QlBeTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
📊
▶️
آنالیز‌بازی رودری ستاره تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/101629" target="_blank">📅 11:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101628">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lyt0d-_L6C-mapZoWnLjEv_zUdsE4R6ouxtKa0W-3z-gpwnTms6ct97d2UTvAwEK1tcO3enI1--dGLbcjfeECqvofps6Iy0mwOfaWpMLprigsZL0pEvylO7xXyBYTyfE4dAfme7OsGAezLT5BZ2BUHCcnPKpyuNTg5l2GmFXigdOaUGyfz-wQzBKQjIJRviXE-C-35QIt_0uXkrnh4W4xf6wy1j-19K676cHLeC8lvKrApnCTMj3woMdvkfTbFowoULd5QT-6Gqvmh23xXH62WamBvRmrrho5vdFN3jpHJfiCpvZfE7HglRybaJTKHJ5e1pzxEmVdzDgNsrFSC65nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🇦🇷
اسکواد احتمالی آرژانتین در جام‌جهانی بعدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/101628" target="_blank">📅 11:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101627">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LT_eFdm72l0lDVzw7nqmggVL4Sd5uMCwchlMXu4znszUaqXhOO0huZkmO8gRzXoT_gRlCQdn_r40TJhWDKI94ZlqPtipvS7JvhOfWJ3LnKJSwts3Y9IkIglzdM2_pWmgeJ6gPhg_J99B7iys_Lz8vBGKAa-7md1dcHspP7mMasrxcnYZASbRebX0DufYrp00wiGSNCt5sgS6njF7v6UOEuQdGf6t_5J0HvZtFrbb4EU95GBnBtDTPUVwIFEAZsCoCaeUihYeMDuttUPRVySMA9K1_5YT8sRfGA3dpQlScfde7VXQ_ShopIMifHmRUQUEBs4WYmLDrrjyE-0Pe82gJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ نیمار بعد حذف برزیل از جام خیلی افسرده بنظر میرسه
- نیمار :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/101627" target="_blank">📅 11:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101626">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBrI-Ze5fOWwFtY6qfxsWI9C-uFBchttRDRIr_C0g9lwbQtmzxAaKI0jIt_dZ3WVYJW68ZnkWpyf9e1yjiqKcsjNZfmF7piZqZc_BpX91wyoD75gS7-IYTWR_VjJgIS8UM8Bk33OJw0C4tR6VXFD5MlNbo3abIJF-h_QNsRIvMY0rnWEbn9f9Q7iPw0NBogRnRZsIj7gTASbj-cVJnB45NHkILLNCJeMDGKOf_8v7y8B1UT5e_r_6G2GSoH4A1MobA9iQ2QnC2ha24adDRY_833XCT7ogiS9YmhR5neMJo-1Y5u1K_3NlYXpSsCuZx7JcclzOxFpDd3LqWzI1rfQJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
😢
خانم‌شکیرا و چنتا از اساطیر NBA
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101626" target="_blank">📅 11:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101625">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuWdiwMDrh7zpU6uCZTWJdexgp69So8RZjjUSGtsOkSs7zsRA8DiOhtmBeie4nUDNoF_z9Y97s1_qdFBHMd2WIMJd2can0C8XWMjTqAhTMowemqh17a2F0pFdWchZ5Ox_CJStQ5Vc_58qVN3Grde0EeXiE0AdhNQxnRmpemZGjyb5gMlyulGzNgvYYEjv-DqmPVbb1Y_dRw6k03yU5fFGE8M97HD2XTLJfsH3Urqn7p0zq0r04iTJ8f-oazlXyyVM1VNvWsz15NYhGUxeP7BqCkaFxO0157h8Muhhv6y297o4Ln6Aa08VAXc4if0l6Q8_dDpfGHeVMeimdBPv_qs1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚽️
لکیپ: انریکه و پاریس تا 2030 برای تمدید قرارداد به توافق رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/101625" target="_blank">📅 10:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101624">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9443946ca4.mp4?token=AiX2X8oV0jy_OWehVauyTIchDNYPMZbwDh6Y8CLHQpJ45CxBAzb1_ig8z94D9Nhk6VR5pU3wZFhld5vmHfcdRRCp6eydedDpxdn-i1yMGUjK0uBBdEZSrikfxQRZ4vOGbVVJbOCcy4z4SsIKHOqdRk2TbD-zVIhUzr6uKYT-6MWxLiCUH4RpZnHkCAWcrgXd6DHdiW1J0mytsbHoJlaC47g3x0ZBcxmG4xRa2FeXjZ1Tmn4Z82Fi0XeMh7NSkvpXe3veM9IdI3-mCO6ZZRE4gni_spVFdNenzM45crv65bzJ0IfaKSlEkg9_Qrv57u14lJ2yUbgz0tkrmFbLZ_IDLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9443946ca4.mp4?token=AiX2X8oV0jy_OWehVauyTIchDNYPMZbwDh6Y8CLHQpJ45CxBAzb1_ig8z94D9Nhk6VR5pU3wZFhld5vmHfcdRRCp6eydedDpxdn-i1yMGUjK0uBBdEZSrikfxQRZ4vOGbVVJbOCcy4z4SsIKHOqdRk2TbD-zVIhUzr6uKYT-6MWxLiCUH4RpZnHkCAWcrgXd6DHdiW1J0mytsbHoJlaC47g3x0ZBcxmG4xRa2FeXjZ1Tmn4Z82Fi0XeMh7NSkvpXe3veM9IdI3-mCO6ZZRE4gni_spVFdNenzM45crv65bzJ0IfaKSlEkg9_Qrv57u14lJ2yUbgz0tkrmFbLZ_IDLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
سید جلال: حسین‌ماهینی واقعا بازیکن‌نفهمی بود. همیشه منو عصبی میکرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/101624" target="_blank">📅 10:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101623">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/509c49999b.mp4?token=gwEVFSpld8jmNOpcRHP4CqgfXDGMbk9le0nwsGYyNPibFz80nH1jO6mzqEoc5_l7tX2-rq_WoXW0u0I9xzZdk9czIVeeLy8QXSd4UmyxjImbr-adqsiYgRmBb_ANqohw8hPjJXgfAJArX_hut8qVMiqGRtIkM8VKy0BOXYh8qzv7NBa1l1qMj4trFtYjd2Ng47Bqt_edM2zIZuk1Iyjqe-gurdEyDqgTe2S_rggSnH2LGVIYiFlgqD5ejV1-iisjRz9QhNvh4iNQCh-wXNMjxeopknG93m7SyegJP-R3yPyLR2AEaGQ8LlaR5s5KQFCHPr1Soh9Dyk8x2n8Vsy4xTk5WQcowGUvMExe-qEeXHMrx-ZJOTGQT3tCrfxISaWYWF5AJfBA4pp8fnwUEs-VcqTFXC1l1ojuG1c4HZsIwoIfv6n_eknlakR0XiYnmoylPsHAWm6QjabEBAHlRzmIIT6BF3_ALoGFjqzOVPOGJPzQ9FmIRvyt0i-pD857qW4NGYpJKYAXC2dRMMYOnT1Dare-pn4vUAqGVbuvbBCgRo0bkaNNKmy8WbqZHkZgVjqmDyiof24igxNEI7U2uced9RDfTYL5ZvqgntJwTrRygGfSnNk4-SpcXFENYBv59evZmEF3P6kjietHDhAtHhRzVwHzjH7TEdi8NJzTfMK_cGHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/509c49999b.mp4?token=gwEVFSpld8jmNOpcRHP4CqgfXDGMbk9le0nwsGYyNPibFz80nH1jO6mzqEoc5_l7tX2-rq_WoXW0u0I9xzZdk9czIVeeLy8QXSd4UmyxjImbr-adqsiYgRmBb_ANqohw8hPjJXgfAJArX_hut8qVMiqGRtIkM8VKy0BOXYh8qzv7NBa1l1qMj4trFtYjd2Ng47Bqt_edM2zIZuk1Iyjqe-gurdEyDqgTe2S_rggSnH2LGVIYiFlgqD5ejV1-iisjRz9QhNvh4iNQCh-wXNMjxeopknG93m7SyegJP-R3yPyLR2AEaGQ8LlaR5s5KQFCHPr1Soh9Dyk8x2n8Vsy4xTk5WQcowGUvMExe-qEeXHMrx-ZJOTGQT3tCrfxISaWYWF5AJfBA4pp8fnwUEs-VcqTFXC1l1ojuG1c4HZsIwoIfv6n_eknlakR0XiYnmoylPsHAWm6QjabEBAHlRzmIIT6BF3_ALoGFjqzOVPOGJPzQ9FmIRvyt0i-pD857qW4NGYpJKYAXC2dRMMYOnT1Dare-pn4vUAqGVbuvbBCgRo0bkaNNKmy8WbqZHkZgVjqmDyiof24igxNEI7U2uced9RDfTYL5ZvqgntJwTrRygGfSnNk4-SpcXFENYBv59evZmEF3P6kjietHDhAtHhRzVwHzjH7TEdi8NJzTfMK_cGHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
به‌بهانه صحبت‌های اخیر قلعه‌نویی؛ یادی‌کنیم از روزی که مایلی‌کهن با شدیدترین الفاظ علیه سرمربی فعلی تیم‌منتخب ایران صحبت و افشاگری کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/101623" target="_blank">📅 10:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101622">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1802ff2c96.mp4?token=BhGlMe6MO0ffIHMO3vRdqAsWVuczUC-T3YH3quIlrP46GoKuEvopt8dH8pV4ycZe9Yw-r1Eg0ZUSRnBW9NvPHh7B9pXLCTHusW2HmX0-dSsqy2S3WTr6c_wIGpi4CrjRZYP6kaTHYFm9-sVLDbqfp_1FcMuP3UGM_Bss8PDYxspaPTXN65-Bd5YFrkBMDRmliHKROpCd1IbmyVdq-rM7Wya9kYfZAP22GM3HoTeVrpUQ62-51EDfQhnCCm0f_ZDxbjTwR-Hgp-K5K6xuItLfRlTr63TXgz7RD3byv3YOIJfmhTrlbV1QxjzaSkw6oTeowVrqsqdYMWTfMc_oaP0klg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1802ff2c96.mp4?token=BhGlMe6MO0ffIHMO3vRdqAsWVuczUC-T3YH3quIlrP46GoKuEvopt8dH8pV4ycZe9Yw-r1Eg0ZUSRnBW9NvPHh7B9pXLCTHusW2HmX0-dSsqy2S3WTr6c_wIGpi4CrjRZYP6kaTHYFm9-sVLDbqfp_1FcMuP3UGM_Bss8PDYxspaPTXN65-Bd5YFrkBMDRmliHKROpCd1IbmyVdq-rM7Wya9kYfZAP22GM3HoTeVrpUQ62-51EDfQhnCCm0f_ZDxbjTwR-Hgp-K5K6xuItLfRlTr63TXgz7RD3byv3YOIJfmhTrlbV1QxjzaSkw6oTeowVrqsqdYMWTfMc_oaP0klg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
مهدی قایدی:
۲ سال دیگر قراردادم تمام میشود، اگر آن موقع استقلال من را خواست، برمی‌گردم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/101622" target="_blank">📅 10:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101621">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db54c4d205.mp4?token=q1hNUa0cUUJce11OTLHe3TmjqI1oPRKDpvjT4AaD8HPH-JWxxhtDtOJvF7lZxeLLqwNbGL8alT2dfxivFkxa3X6lD62n5ldJu0Japeo3eNsqCraURA7uji65HN5Bj3OOqP-SVN0EJg5VgROu25dIsDW7R_3nXYBmfeXy615eAV36Xo4ZC48ZS8RXalKzldk3tXhCCDGufr0xjcwRcsvBQIEfryji3_rAE2VqAaT9mOQsA62TGeCnUxGxPZ7VakM-CTmmBAv025EmQXdHL1biMSlsFP3-KZ_C-WbCWMC92K26XrcPi69HzlyBUj1i29BGmjRclEXvMrGBTRBfSymnTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db54c4d205.mp4?token=q1hNUa0cUUJce11OTLHe3TmjqI1oPRKDpvjT4AaD8HPH-JWxxhtDtOJvF7lZxeLLqwNbGL8alT2dfxivFkxa3X6lD62n5ldJu0Japeo3eNsqCraURA7uji65HN5Bj3OOqP-SVN0EJg5VgROu25dIsDW7R_3nXYBmfeXy615eAV36Xo4ZC48ZS8RXalKzldk3tXhCCDGufr0xjcwRcsvBQIEfryji3_rAE2VqAaT9mOQsA62TGeCnUxGxPZ7VakM-CTmmBAv025EmQXdHL1biMSlsFP3-KZ_C-WbCWMC92K26XrcPi69HzlyBUj1i29BGmjRclEXvMrGBTRBfSymnTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
سیدجلال: بیرانوند رو مخ‌ترین همبازی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101621" target="_blank">📅 10:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101620">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBnkEy5wgbBu1Yoz1HJbbH2BV0L6U6npaueS_9SLljXhol0vKx459pwVlnxReP_YtmYR1gMu_FuNW1P8IF6Rcp54qZVvmIagGKFFm1mThqLtPDv8uwzzXo5VwbIjj4iFalCVeYOiydhyKNWs_b48jAp7YgmxlLq6T7vpXhSzVrofIqVpb7mjHTQC8pvC1Lg4Jw1UKjZ5wqLgrG58XeKQOaiwHc06wPsyqFYxZUPJsh7_SFcLfWCKis8U0MktTBd036CL9kHFxzcygfHHUGyAseBWyMXkxxEM3-UY6-Gg5wevVX8nWNDrX4PqouapDNkW0d-8m_mP8qvWdXMXI4kvAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
استوری رسول خادم برای عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101620" target="_blank">📅 09:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101619">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46845c1eb0.mp4?token=sLJUDgc0of-IKVqDrbCPdHR5rGI_oS3DL51My0D9HNJOf8V8m4IWYpeeYbE7MgI9jWAusGll9eMI-W5SH36jSNtHadm7Ny4yGZe_mKP6PSDOEeHu51dCDTu4AKL0r20EFgIw7rjsNXZZZfDjSe98I7u203Iz7xUH3eSrCuNkoigZGhPfV7zkuXwGsc6WeCIhDMYAheSL7uTHX5xyYIIoFGx8Gt9qNbVqXDQD-A2sDakXySBOB6zbzFxDbHYQWVrG5ZHiX7IZuEmbTg6wrcf7nejungBHUCybJyeOLoz0k8a3XR8NNm2nqcwcHVAx2mcJ3dNEQGPxzWMPhdPABozQXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46845c1eb0.mp4?token=sLJUDgc0of-IKVqDrbCPdHR5rGI_oS3DL51My0D9HNJOf8V8m4IWYpeeYbE7MgI9jWAusGll9eMI-W5SH36jSNtHadm7Ny4yGZe_mKP6PSDOEeHu51dCDTu4AKL0r20EFgIw7rjsNXZZZfDjSe98I7u203Iz7xUH3eSrCuNkoigZGhPfV7zkuXwGsc6WeCIhDMYAheSL7uTHX5xyYIIoFGx8Gt9qNbVqXDQD-A2sDakXySBOB6zbzFxDbHYQWVrG5ZHiX7IZuEmbTg6wrcf7nejungBHUCybJyeOLoz0k8a3XR8NNm2nqcwcHVAx2mcJ3dNEQGPxzWMPhdPABozQXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
صحبت‌های جالب علی‌قلی‌زاده بازیکن تیم‌ملی درباره همسرش که فوتبالیست هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101619" target="_blank">📅 09:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101618">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ae48d98ae.mp4?token=cD7tmMVgfzIOghJiwWnaLrnVlTVOeVTB9vUSu875p65svDIXgavCOi0OzeDh_kNUyZrCPJB48eL2PYPLE8jHw2kL-Kzd2ic184GifTa2b8MR9kOqMX7r2kW6h6Y3ckzPfvluD52YTGS6GnMaNGH4xdSCCfBDz2RHOH1rNlSFAytl2iz77LaPU2q2dMuKbyvoEx-v30jaLsHIA0LUA5Jf66WHP2IX8vqPsNEpdkSMaBEVRycTQaW5gyeMPeegCoQowObC_mLCvOifxDS4kURC5VumAdPVkeeS7HXXOPWNdUnkxW3S51kAquF4ZJmkz2qqvzNbFycdZdzTLATG7DhnJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ae48d98ae.mp4?token=cD7tmMVgfzIOghJiwWnaLrnVlTVOeVTB9vUSu875p65svDIXgavCOi0OzeDh_kNUyZrCPJB48eL2PYPLE8jHw2kL-Kzd2ic184GifTa2b8MR9kOqMX7r2kW6h6Y3ckzPfvluD52YTGS6GnMaNGH4xdSCCfBDz2RHOH1rNlSFAytl2iz77LaPU2q2dMuKbyvoEx-v30jaLsHIA0LUA5Jf66WHP2IX8vqPsNEpdkSMaBEVRycTQaW5gyeMPeegCoQowObC_mLCvOifxDS4kURC5VumAdPVkeeS7HXXOPWNdUnkxW3S51kAquF4ZJmkz2qqvzNbFycdZdzTLATG7DhnJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
سیدجلال‌حسینی اسطوره پرسپولیس: رپر مورد علاقم تتلو هست. بعضی وقتا هم شایع!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101618" target="_blank">📅 09:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101617">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRA1i6EiRCtohnJSDyV3DVwmFW-2R4B7bLnoZoWlvgSG8zeleTVghG0pIuRPO-DVFvNvjmWpIe4vJrcY6RrPR_eclVfuxbxvGh_GxQ5gyHWJ7x-Vh37YkYWZVOsyyxm8Tg9Xdv0ESzcO_dGVXWsRRAfmcUzliYroh-Ut_7e7iXMS5Qx0qtxhfHMgSUOyltScoRDkKWV-DCCD5OVHZneBsGC8pfqeqlfwRoaWYWD07lSXO1vmUWPWcxhhEOrkHpkar65GyGhV8I2wKVi2xBDJRWJ5l5SgYcZ-lxBemj6mLt2WU2ECSaTFWr--nIrs_Qg72mHgQ3RoWWoZwfT20FWwpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو
🚨
🚨
🚨
🔵
⚪️
منچستر سیتی احتمالا مبلغ زیادی رو برای انتقال رودری به رئال‌مادرید درخواست خواهد کرد. حتی اگر فلورنتینو پِرز موافقت کند، باید دید که آیا این انتقال از نظر مالی برای رئال مادرید امکان‌پذیر است یا خیر.
🔹
🔺
رودری هنوز قراردادش را با منچسترسیتی تمدید نکرده است، زیرا منتظر پیشنهادی از رئال مادرید است.
💣
💣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/101617" target="_blank">📅 04:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101616">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2512ad65.mp4?token=jYhDaeQLDFmxk34XHVLKtkUuqdyiHqw9Uk_J8j8ZMcN4cgRx3LEwNhR8uggh-RosFZgDdr6OPabLYJ89NWzjkFjSlxdtTZRGAFPk1JLZhnNywqWTenc66JUz1qvY4c0yLB4YBe_QnQlWgBDXaIeb5lTZynPRyCVGoGmpMgrEVJ3iIvEnCLLqSqSZAk5GqLOQ6d93NLVB0xDRFxkmFnKA3IChUTL28LG4hQrBq70jtWdwxWGHbNUo-mlGaHRc5U17t67GSk8gE8oJh1ZCh8A-eztQM0XWadV08L9s-tq_BTB37UlRzHI4XOUOA-baqRwwtUrNgJwla4CU748FRHhpjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2512ad65.mp4?token=jYhDaeQLDFmxk34XHVLKtkUuqdyiHqw9Uk_J8j8ZMcN4cgRx3LEwNhR8uggh-RosFZgDdr6OPabLYJ89NWzjkFjSlxdtTZRGAFPk1JLZhnNywqWTenc66JUz1qvY4c0yLB4YBe_QnQlWgBDXaIeb5lTZynPRyCVGoGmpMgrEVJ3iIvEnCLLqSqSZAk5GqLOQ6d93NLVB0xDRFxkmFnKA3IChUTL28LG4hQrBq70jtWdwxWGHbNUo-mlGaHRc5U17t67GSk8gE8oJh1ZCh8A-eztQM0XWadV08L9s-tq_BTB37UlRzHI4XOUOA-baqRwwtUrNgJwla4CU748FRHhpjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
⚽️
خاطره مهدی قایدی: بیرانوند خیلی خسیسه. یه روز زنگ زد بستنی آوردن خوردیم و خودش رفت، گفتیم چرا حساب نمیکنی گفت فقط دعوت کردم نگفتم حساب میکنم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/101616" target="_blank">📅 02:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101615">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsAXcR-s_olgEOWnNWf-OKCBCqSG6U6YNWdRuueK0oLPslTLrQY3aQrY6R0dTv7poMG9zfaSd5R_Wsuzw4XanyPPq9L5E5Uvz5ba0PvUHgwGoGMljfwrHIsJ6HTapN1lbtjBdvbcCXXc8Ix9H26TFf5O9aioAWo6X66oHgWlhqyyTBRKPLIC0BidupI12VxiITKBJRnbFgXfmTdRbFsXs_RLetAmSJrX8RV81DoJoLdApYSjk_pQGHm2y3ntX1WjKiJz9vbGK3I2bT8lrwuJAEpr2kSRewOl-VjU_benDmUe2ls9rHDgsfkmBQtsioJPIAaFEXRk_bxLkeZvEofS1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
منچسترسیتی درخواست اولیه 100 میلیون یورو برای فروش رودری داشته. با توجه به مدت‌کم باقی‌مانده تا پایان قرارداد این بازیکن، رئال‌مادرید می‌تواند با رقمی کمتر ستاره اسپانیا را جذب کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/101615" target="_blank">📅 01:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101614">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNzb0TmAJITfMIfkVoRGtFp5GYAAgJwjwRBKbsMuHWKJCUZgNAE062O_GIVyGWGHe-653BgrngkIcs7VUt5EvJTcYSZQyKfABjBBN8Fq6EnZ50uIydOrOlNwxbdhp244D0SSqUAnWhK85mNp9xcOS4ZhnM4J5vgUFcI4-v670shQwdzbTA_uOQKuTJ5_kz5qJ7AuKFMQdMA-hNqw_wf693IkdAWqBIyZxFH7nXiJL20wdhACWaIppB3ludi1g1HDIaFCQxqnR5FqPouRr7c_cVPZe094a3DduP0AkSfUAS4_-qan2aBQ3ieKitTA5VIu7yS-DQy0U1XLAmLPjGizIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
منچسترسیتی درخواست اولیه 100 میلیون یورو برای فروش رودری داشته. با توجه به مدت‌کم باقی‌مانده تا پایان قرارداد این بازیکن، رئال‌مادرید می‌تواند با رقمی کمتر ستاره اسپانیا را جذب کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/101614" target="_blank">📅 01:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101613">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzpDWBjsu4wttz-l8MdcBMOH6PbfronuR_YfcP6jNwe-frab7qEG6SfLpU3lWz44jxH5CyCOFYMB_0rPvNb2wYPgkKjQGwaGkORNoneVuRKpKcXcKniovXCbo946PdYRqQQ-cYAmv-6l_e1OU_BhVT83BNBv9rez5Wl0mgv2COUsBDNuaY39940DMiylt6AGCJA5NTcW-DUT01rUas2tD4ZbXjmXLh_UfZhVkzH2oRdGAvxBbOkIyd7ILYlJTfNmlnbQeGHpWNzXmV-T9SgQJc0MtSXS2cKBCtydx82PCtUwbkiHe3lloHbiOsW4NZPVx0WY42LLoUhkO1PABjAswg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوید بکهام از تبلیغات تو جام جهانی 22 میلیون دلار درامد داشت و شکیرا 17.5 میلیون دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/101613" target="_blank">📅 01:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101612">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krGP69CagstrhK3_rpQY2fd-zVrvnrAREuO8xp2CKbgn2vfFA0dFMBLk8bEJ-q2OrT5LO-RJ8Xcp83M_eEfJEL9e3hdg41GFhhLLjWj3kEP9hGGeHpWrL6NXSKtrj8hAyICIguRL_mImWy_3dnZEwUdLU4Ubaw9K8AOZPVmw7diZCqqIFK7AhjS4zg-xfMoZHnx__64L-1qtvttlSAzRWU4e422GSAVj6uuwTAeWtv930AH0ics4KyiyB_25j5PTKZyC4P4u-AJ6i1RKZE1uqSxtq_NmT1XpMoFeKMAwrp5lkC0jTt7cA5mZqShl7Kmn9au9TBvFu4zDCnphaM9Eqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط 3 بازیکن فعال حال حاضر فوتبال این افتخارات رو دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/101612" target="_blank">📅 01:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101611">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FK0f2y_l-H4Jedv-TNh95OaJvLNk5ugsKkUnK1d2_Pl4JDsnPQTyDOZg1ki9nDv-uEu-LBfFXBjf2CaZPYyS5JSWuj0-UsSc_Bm51ri-sm36_57gYaBfrq7LKd3PQ3XfJ2fmdOzMk14-MlZO-UtCEf7LdvN7Ci0O0K61VFeK9btHW3KwfRNvq0QiY_pvfP3sgeFgbc9nIky9jUsUDy-441kavsIIpSV1R56lQVRdO64-LPPvdT7756dEJcGk6JCK7tNCembXCYEaPYJUfM2u5MNCYSmJ8IXJKRW8uS6gZp6uESrm-9tsBUtjve0UdgLdUEbhXDu-Gs0Abkx6GfDZ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/101611" target="_blank">📅 01:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101610">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NfHClRqUXn5ljKMEKvbdTa0G2fT2dgOb9nKfeo0T20qnSLXwHcLC2Apc8wiPXCG6QG5g9QG0HzEVdibI7kIWQ5TPPa0SIuB4tXeM_SUKolAKJBYKTjwHCz7ZKFkDl5SldBbVH9Jp3p_hTPmkDDmMrl34g_k0LqeypoYZv090T5xSmNxuJRsckSL508szl4Z_Br8KkfvcJP4fGCY-X6BoCbQCPAna2b1a8YVub_GyNhPSc0KslfyiyFfBl82sbEeVwpqubPZVm8SobLx7vbLvJXGGc-C4cnAHQQEmb6vKhvZUo2XT1NJdPy40vE_phtAib9XAZRhxLOuqm-taY7PBTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
کیت‌لورفته جدید رئال‌مادرید که قراره فردا رسما رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/101610" target="_blank">📅 01:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101609">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
⚪️
فووووری از پپه آلوارز: رودری با قراردادی 4 ساله به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/101609" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101608">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEJgF-00RqzjhmIKZP4yr21nVZ384l-0_hz7tNe3jFB-tTbgsHTllZJtSP08yuQx2mkDwZowhSHHuxrguNAYeCy4p49PzOfNqyf2RxjzTbDJHmI16bA56FUSJuyj2O2nOWh51HtdNkw9gXX1WE7MfXVRJwczR-yHfkqIp5wctVShIKnfHNNW4GRbNkYoy6ICSQtnSeW8jJeTY0MnxAP9Mbv7rDbfjsn32tOe3Xy7WbXJJQx3wnaR6Wqz_7ulTBligs6lJdqafkN0F1KuYV-aOopI7YuWdr_0gTwkdO8X0NBGArD6nScwWyTVgMUo3Ahves3Gv8BWZQKj8EDnznbozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
والنتین بارکو با قراردادی به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/101608" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101607">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‼️
▶️
👤
حمایت‌جمعی از مردم فارسی زبان آفریقایی از عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/101607" target="_blank">📅 00:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101606">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی؛ باشگاه آرسنال رسماً اعلام کرد که با کریستوس تزولیس، وینگر یونانی، از باشگاه کلوب بروژ قرارداد بسته است. مبلغ این انتقال ۴۰ میلیون یورو است و قرارداد او برای پنج فصل اعتبار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/101606" target="_blank">📅 00:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101605">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GVerz-TBpR7RioqH4lldukGhwu9ku7FocDka7LR91bG0OySzpIB4JLi42yWGahYoQvsnSA0uqeVD03-UQ6yDSeIZ5Kf8hKreiGY_EVv7M2E-AW5Dx9ShxO214fJOwZ5GeQ_f8WZD8nStjUQJNI-pLUYHQsketZHTr5ZxGlLL_8Jsz7TEslS8TaevgW2AvfRfzw-vgHuQ4QqbPz5ZxPdwFFHQrjpNUydOqqLWZN4cwViemPBpzgb4YUvaopySD71obA92WCX8HZ91a2EppThnIyoTkMJgQBDaXPnpELaZzTY5mKublcL-HntMEBudkrzGD9YJbnd_4N5X83iD-T23xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ باشگاه آرسنال رسماً اعلام کرد که با کریستوس تزولیس، وینگر یونانی، از باشگاه کلوب بروژ قرارداد بسته است. مبلغ این انتقال ۴۰ میلیون یورو است و قرارداد او برای پنج فصل اعتبار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/101605" target="_blank">📅 00:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101604">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcPiwY9YYwsesXe9j95MOtaqc-RJo37WvlL4PpTZA-2YH1qNixE_weyEVU3YgoSTpjFiuxs7A8uukqf5XREVonCALXyWxXYNBwUfw5gzT2mBUUka1crVUEkzF6Y-w2AiVLY2Sez-dgg6MLNZM3X1KmDPNFFH1tLPMyDmU_q_iNGOUyA-k_G6QLeUftAkp4KZ4F_8pIXXvxC16tXuIgqCihmRTW-Gx6V-zy0ZYKaC2VRtlqPLAkiNvoIlULad0gU9qxWUuu_uond5HB9Sk7m7BPHuBLe0vfyDqJNYDFTw2cr5eZkfnGochNgIkBDIN3KgxAcew0Lc8kLhQwaZtQnpWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
ده‌مسابقه برتر جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/101604" target="_blank">📅 00:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101603">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jTkUzluyAThA6QEEXr0KH_qCeRVoRYDkViAuxkCmC68wl93d-J7k6KAj5QcunmdsiSyKopCqJjmp4CHHpQLB0qaIGQ1vXNyuFmfCQqG7zcVBULQMpLXpf3cUtEJONq_ygHxuBwjkHoDMoy0lWarRn3Jsvir5aY2aBAbW9Hmhhm04cHl0PCiMv_qgazyWXxYb8uQOu_Q31cJSioLB0mp_MH25N7ZzgQWjWCezRO-vij2sgMVIfX9KvA81OlsMbRCSDkIPu0WAJCejl3A12L9IRhy0-dv7ctpvr_3cEDmMS3l7p85GxhWwEjrrH9dOKlKAWjVBA5U18WKG8Lpeu-n9LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بیانیه آرسنال: ویلیام‌سالیبا به دلیل آسیب‌دیدگی در ناحیه کمر برای مدت طولانی قادر به بازی نخواهد بود، اما تحت درمان قرار خواهد گرفت و جراحی برای او ضروری نیست. او فیزیوتراپی خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101603" target="_blank">📅 23:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101602">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxAV821xSUTs-UGxsL7dpvieAhExp-Ws_KTkCPacvouFavZPNmKOhfwqZwbEOlfU6hPY0icobBk5FbydLiTbOENBwVp8F8xa5Vcj8Uigoqg22tsvl81egG9nu0uWJ9BeltN6J9Q7c1nZenwwIZ1cL9jZ0z97-DWbKz1wDdumqLG7ve3cLHIDleMx9Q9Y3ZNscIf2WQqaiHhDMFoxi3RUb9SAGwNY9hhpzAV0h-SSCbcM9EE3TVo_vwlR3Pz9L2SCuC5UZWb8AfLuUYJX5Uqil7eKhmER-heZ5aA0OnWuCIJv6K9y5-pWvRp11U3u4KBllP94NAe1FAGEsxlW515VeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
توصیه‌مهم صداوسیما به مردم ایران؛ فقط کاش تجهیزات هم تحویل مردم بدن تا خوب بزنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/101602" target="_blank">📅 23:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101601">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGAuIJ3M5B-JgrH_3CAICG8fFI04GDI7Zu_IEOEE7Q_nTkt7fG-42OhKlNcMw6fNFZ5kWcpoIWbu3RtV6QUlp4bx1LoQmg5Gug-DlW752fOWhjiLTOzR6-mO9Boi2PoAwKpIB9aZSW4SkMvLjca_sgiBxJLIhdXyLpE6nBoh7GI6TayRvIDv8mZZFft-GP_FFlriv7TLPYLmGXbpXMSW_oEITUaQ_PAWG-ROUzZtdpd10oKJznWJ21VKefDDlBJKdWMo0VzYAu4cKF0DjVWHuTkUn3ly2o0VI3c17XgfR44OSU_oiaiezJV3_4RhdyQxlZRkXQOtCKL4Xj4O4Rcmkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
🔝
ستاره‌های حاضر در لیگ MLS آمریکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/101601" target="_blank">📅 23:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101600">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbgumHywUy70wC_bO2ZVUVTbrJDTkodd8wxnZv4LxGuQttTr1ITOCehcKzN0VKqyHvWD-9NAGK9JiYHBBlmCKtiXtHXT_eJY0zSChRBhrGKeodBLIn-EyJ3qWHgmcrbgYweZUSbENzhSU66LMsbPlmjG_JEAkCQh9XVSjrhyKVeGLbTS1sci25uMFxKze0FbC7xstD-albKY2dF7f6E7u9n5oG0cod6rgsZ_4_KW8lYDOicnwbVjRq5_X18z7xswDVy_9PZavKgC06An-A3mcjt5fWAqKYdNQUYSrfsb0RwnZMRwByr14APcg8NH9OZZsNN-eLRdp1P2cZVmRU9VCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فووووری از پپه آلوارز:
رودری با قراردادی 4 ساله به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/101600" target="_blank">📅 22:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101599">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYdIvgI2Rs5dWzHrWXB03Gq52jd73TUEpu0gacLNqExdyXlx7P-LuoGWHRGrqXOunCExu6WTaciCT2W30bQgHNnwma3cGFIvU2EtD6gJaRpNZMbQH3JpeHUxPlJJnMgWevw85i1ZB4cPzfoWhJrFaPU0IWfjyYaCMZqMUFl6bGnfl3KhsP_CkaqjTnSbimmrTM254Vxy7g6-T4qrUwgMXAlpXeQC137Korjrw8PdYKPt31rmc4zG4_kzeKBOvqdFGEQgITGEyeNRSiLAi1JfwD2GDYYT6O69shXIKmgM8BVffdMaG7715Irdweeec8eIw11VVWSX5gE4dhnbtMn05A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فووووری از بیلد آلمان: کیلیان امباپه به فلورنتینو پرز اطلاع داده که موفق شده مایکل اولیسه را برای پیوستن به رئال مادرید متقاعد کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/101599" target="_blank">📅 22:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101598">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJBgW1j2FkXXsNdO3toeS569FtVQtt756Imht6csytsc2Gi5wWGbRf_D5JYQXO1uIlfKoI8cYe_t6p9LDxFczwrvlY1UhaB9OfSdMcEKVR3pTlNp65AzGCze5DjOShTT278ljeRk2M_Pg8KasF_S862qJQSW-8NmQR-qQ0tMlHQ-onVap-u6pJI_IrAnegcpssBQptczlC2wbjOKP1Rx9YceelS_9j1saddkdrGrQFcpvDl-4QDwrRcY6_wSoKfaOd1rntHagqON0u5_V8-m4EZXBy1laNPUT4tmbLwzvguc-o5D3bTU2zUHodZRu9bm0ZDcw98ohHV3S40DLPb6Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکلی که وینیسیوس این روزا باهاش سروکله میزنه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101598" target="_blank">📅 22:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101597">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpuI5fC9tMalj-E456SJIu6G7lCEkqMzbXZqlkbQj63HwMlXlBkvPP4jYTTp6n3XkV-3ZFp8tL4DpqfN0GdUd_12z2Kjo9K1UGLe5fBq08VX9RZDVX1lHJeS-Ujl4g5C3ZSwGX8H5od4fn5fn1tmmu8hNfGM9DX81r1pbubg4LSDaXgd4EKUqY0mVzxfZfsCDfI75Enb7Fohm1CxNI3v-Cb05BVEAnmRWkOJVqGFZAeNG-QbVj59W63dJL6dRE1KPKvaGNUjsKpO_faUdBQejX58J0MUenDNlbauCu_lQK0a59VlPwQse80ga_csKdsuMn1E_JXumVWrrVCmcrjMTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فابیو کاناوارو:
اگر من بعد از قهرمانی در جام جهانی و کسب عنوان قهرمانی لیگ، توپ طلا را بردم، چرا پائو کوبارسی نتونه این کار رو انجام بده؟ به نظر من، کوبارسی فصل و جام جهانی حتی بهتری نسبت به چیزی که من در سال ۲۰۰۶ داشتم، پشت سر گذاشته. فکر میکنم او بیش از هر کسی شایسته بردن توپ طلاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/101597" target="_blank">📅 22:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101596">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QR4KxT1KPoSzzsMvHkGjby-8UcdIzFKPEYQj9A-rKq0DRlptww24o7hZhVpS1bxPLaaoCKPePewccqc2mCm1tBjNib86xOQnFrfxd_T8cmiKji7-lLumOZuRaNfYbzbMCFIysCWr-Z87hxlbpXbFSbw1koO-UTdIjz9cBwVRYj0gihas_ZY4m11eckyS8tVinGJVnKjLVNx-NczMFbCpqFIJnbJXupuACEmDN_2Go2_2nGDTZku8QHlb5I7qEjIO1fEafAPtcx5XhLCyI235ibM253PvwsZfd3-Hx1qJi8wE5KjZPEChdGEQ0-ekCc9-44JjwrAhKRZzWg5yVIYXqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🗞
رومانو: سامرویل ستاره وستهم با مبلغ ۵۵ میلیون یورو راهی الهلال شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/101596" target="_blank">📅 21:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101595">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN23a62WMQrZQeGRlt-dticzIUqDy7Cc-jfvo7mZ_B1pIYJc9GdSeP6J-puqiQcOAj8dLd38ixVmrVeCkDE3qo0PptUn-8eGCZNQhijzp9dWhlrLv9aPJdyXON5Dl8N3x1L_K3iBeqquPwAUyEG2XYKIo3CI_PJ7O3meB-vLH1auVIRqpyeM3_Y2LURFKr6lcYfRHTRqKlk1u4z_UrVyPAAPhDqH85Cw6kbHIJT3TzV5S9UY-TiuE68oEJGCMvgyN_QN6zQ9GdrEkq6ii4-czxtKB3GiY96S3iTZnBZ_6IP5lcF72EB1oN59P8u5xu1D0T6Zwj7NFhCGffY84s0Pkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
لامین یامال ناخواسته بعد از فینال جام جهانی یه تبلیغ خفن برای یه برند لباس جور کرد! او چند بار توی بازی پیراهنش رو بالا زد و لوگوی برند آلمانی 6PM رو جلوی چشم حدود یک میلیارد بیننده نشون داد؛ اتفاقی که باعث شد شورت‌های این برند خیلی زود بعد از فینال کاملاً فروش بره.
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101595" target="_blank">📅 21:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101594">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBwG3h-pPC6BmkPBsiZdl2FSP031rTtc5UsO7dyVyDjdkkkoAYDV7YROIJEoOuVGwAjFles258JGTnUDgbKXkd5bGOGMW6x4tzQNEYNDeoiecfB0WiWilp7Kcq99x4PGl86B6jWQ9Muxf2mffWzV7N6jZmeenTnwTtJSRO1UjTetJ85R9TXnHgSnB5aOCjkRb7RF7CFn6OD5oIrJwqk5kKTNEip0Qv2J6o8lJ-eSbxQUE1aAYIIBmQTXc1hWb6_5FZveldZibJ23W3Nrs2fpwEICfXgAXC0wQn1kEDRYCLLD1fG-Lw_qGEXIpDtqrHx8dzqzy4IpMOCS2dM42v9MOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶۰ سال بعد، او انجامش داد!
✅
📊
کیلیان امباپه حالا:
⚽️
🥇
آقای گل جام جهانی ۲۰۲۶
⚽️
🥇
آقای گل لیگ قهرمانان اروپا ۲۰۲۵/۲۶
⚽️
🥇
آقای گل لیگ داخلی در فصل ۲۰۲۵/۲۶
تنها اوزه‌بیو
🇵🇹
پیش از این موفق شده بود در یک فصل، آقای گل هر سه رقابت باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101594" target="_blank">📅 21:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101593">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
#فوووووری
؛ دیلی‌میل: نیکو ویلیامز ستاره تیم‌ملی اسپانیا پس از تعطیلات احتمال بسیار زیاد از بیلبائو جدا میشه. آرسنال از مشتریان جدی این بازیکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/101593" target="_blank">📅 21:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101592">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76aa3864d3.mp4?token=TZuxHIgSJ334bfiW_VzB_vKZdgHnGpZwunRK-cpaTRrUmuqC1KIEmpNJ35CwkytHEIjZQRPGsvtfq1aMOUr8lR-U0n68BGz1C09Z5OsCXAkY_ImZSiBhsvQN531ShfZ1B0Jj9yNYdVUDcD6-s8hULEkz0KbW7ZplKSEbHu72RW4xwFbGHMlTZvde-67ANcUD3kWEk2pVRIqWBdZvUISH6QtDRJqwXr9y5lDRjMj40GWZjq1MG25WB9t-0fBps5wLyGQnVQu9VuHHcRuh6gh6o39EBHqbXVWLoDJV2AAf3dIFT0tn6ljbeyJI8TYCknff63qywgBhgHr37rGXGYJvVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76aa3864d3.mp4?token=TZuxHIgSJ334bfiW_VzB_vKZdgHnGpZwunRK-cpaTRrUmuqC1KIEmpNJ35CwkytHEIjZQRPGsvtfq1aMOUr8lR-U0n68BGz1C09Z5OsCXAkY_ImZSiBhsvQN531ShfZ1B0Jj9yNYdVUDcD6-s8hULEkz0KbW7ZplKSEbHu72RW4xwFbGHMlTZvde-67ANcUD3kWEk2pVRIqWBdZvUISH6QtDRJqwXr9y5lDRjMj40GWZjq1MG25WB9t-0fBps5wLyGQnVQu9VuHHcRuh6gh6o39EBHqbXVWLoDJV2AAf3dIFT0tn6ljbeyJI8TYCknff63qywgBhgHr37rGXGYJvVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
در اتفاقی عجیب، امروز تو پلی آف صعود به پرمیرلیگ مملکت مس رفسنجان تو زمین حاضر نشد و صنعت نفت آبادان با پیروزی 3_0 صعود کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101592" target="_blank">📅 21:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101591">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jc4NnRrTdlKE-dFRh3pertCs5RBht0tQdoC_-kuvHbcjT3IeRTLqKVbqFTGvjqSLzgWyiFIHUZz3chi933zW7axkClz-gHK5ZqKBFsVXa1JfMPZOvP4VQG5I1nxibA10OPdV6lZaurOytqeyKOd1fCMqK7-0XZR9WEKmemu-8HFgO3A1PHnObAtVu-oc4GUVKMf3FPHHm19p1ilMDOI8cDVo2XU5glD0akrflStpt7P_TC14IOAgmhuGFOLMthJx0iLPgpAv3DP-TnhMHALrZGPlhB6DXURlgp3vbmwm4pyqDhk4HTKPMgINduQtjQeMDGdaSmgO4R72GykHr6WoOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ یه پستی رو گذاشت که توش نوشته : پس از کشته شدن سربازان امریکایی، ترامپ به سنتکام دستور «دروازه جهنم رو باز کنید» و حمله به ایران رو آغاز کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101591" target="_blank">📅 20:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101590">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsM1MUvrqwNdYulM0FlDXzRZqX9bKxoedcKJMDuQnZSeqX_uE-kefedSwbn2VX-sqGirI32mEjW7oKHqNHdvJF9DHYDbSnYFLmeyC8brUY2blarmqtldUhAMBTJLsAX2drgNTAcIGjvaRaeiIg2Do76K9EKWrfKUm0o2cOxICk_EKWrBeh5cE3XkD-aWjrKxGA8NuuHS-ZutHO0S0aA4fnlVfgWElwNalxM6JPCSn0kqfimn9kpaRsFtcBE5EIbd7IdHCWpPWGqEtCElgqKMYUuI9RfFIZNGCTx9EaD_LalQa7mzfiiqJVo9pAR26rAKlAfX5MBdAwOyYldQfmHSWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
کنفدراسیون فوتبال آفریقا اعلام کرد که این مسابقات از سال ۲۰۲۷ با حضور ۲۸ تیم برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/101590" target="_blank">📅 20:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101588">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M7kI006o_Gym61vywfFUzrDVLW0U04dapd3aRlwTtJZrlSzwi8QftqCf1KHMx04x_MG_nCGkR6dHWqO6hCf1dY4CfoDjSdmnwshA0rmYeBE5DDEvgWM9pwHvTVxxaKN4qh0EUUiUysLUWtvO3OcGD25VOoMttJorpLhyWPiyZJeMEWFKkAjS34MVIf_8Sg6WYQpy8XPkd1awdrITt-LxDGgnrgyX9coZqedemRkp0hpsC5gEdCPsKRYGiQm_bnG_aEPBVVdXfTpm1e5k3V0a7vORtWeLcxxkt5Tumd1DcrP6uDQbejrRn7gOjihT60eIGAqOEvNDHcoFoYqbGjpmFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f8v480p-zRu2csLq_Mna6mtHqIX5VL5dH7wzH4wjv3XABvy6ezXNrQANwMI73Rl5crjjYpduEqOiMZolsqxGzkGPrq6bS5rz6klCYk1q1ETspdlHNn25yp4TyMNVo6SH3d0RTpa_4EtyRz_R4aRz3R8wXQaFcxo8WZkW5pjgwtmX78KPv2di3MqZhPzRkiEzFa7kKtHzKTPoVfH2ffG22AX4JbqTXQBn9b1fewr2mh1YKsQLTWTh2teCzLBDpqNOWc2JCA4mNx9TsaN5JrHpN1IoRMC3glqjqtl7msqXLy70ETyplZFFe5OI_iFlAqR48sVaWKtVZdrV2xkiZjiZTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کاور رسمی نسخه استاندارد FC27
🔺
تریلر بازی فردا 23 جولای منتشر میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101588" target="_blank">📅 20:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101586">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxM-VV3CH0A6Cbf1ynzbHx2IG9CPuiTNRJlqHgWFWeNBOVa-VbrbL9zsLcCgux-yyO4gcMwyN2mBt6AU67f9tNpsWa9l72upHL-7vNB1ZTuqH5fmpxXrEGwe2iwn63W8_ZSwxg6FV-NdU9JJhYZ5dEUo8hbjv1EsihbYgXwCNoOHDVeit0Rw87Qpmm9Mdz-YLvGGUxmmKj7u8oM_zzFBPdhUseJHUXZYQUj4m-QXckgaZzk_CX1r_D-yAzibrslE_fEHLz3tHJqVedzgun-exeoSmAvBO_OtDqY2slP4x6jaIx1gek4rAZZ9ooMLAjmZIqBrVIbaa3n7VaAfYJcvng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6db999500.mp4?token=VzbfJshAGBzgjmb5n_WiNS8do9knFCdOBicPmrhc_Utn-Vm-bCmT-rfKcO1Nlpc2gV21d53h6_gMBfZIwj_cqjNsvtV9p_kX6QmBfuORxNwWiQt67gsDCkngFgqd3fidqzGohLHBZkAjx-VS5wwslX6qF1j0jFSI4i51j38Le6M07YwJFr6bj2-QR4aSbGYsOmu3F2MJpKguQSxb3adhKjCr1CjaRtH6qdqQs6LViEfm8KW7pan5S_FR9PTyhfWYdtxac0A30x8YnLl0EqU0ysLYJw7lq_PYnyj0zL_NNh7fnC1iyv8S0_yJ82bFHrGkDIIZkDVcfezydb_rS7vffw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6db999500.mp4?token=VzbfJshAGBzgjmb5n_WiNS8do9knFCdOBicPmrhc_Utn-Vm-bCmT-rfKcO1Nlpc2gV21d53h6_gMBfZIwj_cqjNsvtV9p_kX6QmBfuORxNwWiQt67gsDCkngFgqd3fidqzGohLHBZkAjx-VS5wwslX6qF1j0jFSI4i51j38Le6M07YwJFr6bj2-QR4aSbGYsOmu3F2MJpKguQSxb3adhKjCr1CjaRtH6qdqQs6LViEfm8KW7pan5S_FR9PTyhfWYdtxac0A30x8YnLl0EqU0ysLYJw7lq_PYnyj0zL_NNh7fnC1iyv8S0_yJ82bFHrGkDIIZkDVcfezydb_rS7vffw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📅
🔴
24 سال پیش در چنین‌روزی ریو فردیناند یکی از بهترین مدافعان تاریخ پریمیر لیگ به منچستریونایتد پیوست و با 30 میلیون پوند، گران‌ترین بازیکن تاریخ منچستر یونایتد شد.
🏟️
455 بازی
⛔️
203 بازی بدون گل خورده
✅
🔻
پرمیرلیگ [x6]
🔥
🔻
جام اتحادیه انگلیس [x2]
🚀
🔻
سوپرجام انگلیس [x4]
🔵
🔻
لیگ قهرمانان اروپا [x1]
✔️
🔻
جام باشگاه‌های جهان [x1]
🥇
🔻
عضو تیم منتخب فصل پرمیرلیگ [x6]
🥇
🔻
عضو تیم منتخب فصل فیفا [x1]
🥇
🔻
بازیکن فصل 1997/98 وستهم
🥇
🔻
عضو تالار مشاهیر فوتبال انگلیس
🥇
🔻
عضو تالار مشاهیر پرمیرلیگ
🎙
🔻
مایکل کریک:
به‌طور خلاصه، بهترین مدافع میانی‌ای که تا به حال دیده‌ام.
🎙
🔻
کریستیانو رونالدو:
واسه من افتخار بزرگیه که با یکی از بهترین مدافعان تاریخ همبازی بودم. فوتبال و شخصیت او داخل و خارج از زمین بی نظیر بوده. واقعاً خوش شانس بودم که کنار او بازی کردم نه مقابلش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/101586" target="_blank">📅 20:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101585">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IettCqTYuu4HaEux2BIcO9iEfYYqHtHkh464g5hrjhD2U1qUUTQ8EvRHB8urB06UQp876V1gc-xmpf1GrD3IFKCUhyBCcr92M0lPXila9soRC118M4QRUwK-3v-LQcaV2A1_OpsJczhkjUGVhIPgqossZo98Br_IZAnKtcuEHnGPd89pXENI1fUA794cusEw-tnL2pnJhrDS9lWQc0ec60jIOZw2TE0b0lvzONxAQ6XO71glIgasaske5in6iU4xrhUuNovci3k2LbHytjPfP7pTCN5GZir1o4Lq0nCuuyRULCztC4NLqPR8tKzzP0jVt-CfxLcWHTbnw4qRBrh-1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کاسمیرو در انتقالی آزاد با قراردادی تا سال 2029 به اینترمیامی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101585" target="_blank">📅 19:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101584">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ansNckYq26VBoZCWkYD_9JqqmyOyXpBnAZaW4JmaIoZOYFmOGgcWgDTwQdq-als-LjosutiBQMlN_2TFFp_lurTfInnjuKdvJa3H9yESGlGII_Wx6f3xYbnwptjPeLx9y-Tc-KkWH2u1LNcpLMI4biKAEk83uyxpPRYcEvwyP2jlzg3sPCssjbU0X9KajtJsSzduqtcAWD6zKBkAgRXT6i2K2fzEKsDiE9h9pnMmB2KvY4JM1X5TGfVU9bcBqW01S6GNjDw4WYGbpdupLiUfTHJRyVzyEGCSIkovnuCEPjFdXYdKLOURgPclBIRunck6xpJMgUAy0g-_BhIvoTt4QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: گارناچو با عقد قراردادی قرضی راهی استون‌ویلا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101584" target="_blank">📅 19:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101583">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b963f629b0.mp4?token=fJNwhHhp-UZ-ZF4htG7ieqD0QKYLT-yVh6NdFCmhffjwVJGV1Kp8HPLb3QgU3q0rOce9cAyt9JS28dbXoArYyFmBfZSGkCIwvmSIiGiizpYa_HHBBRo2NNU1jMXShhewS5a1yJM_-lubEK5hhUfK-LYEafNm7V-w1U02iRrqP_zT2fbXX407CTyij58Z_wcUp5KHbLlpB8vbp9_Hhr8Oc2gBNtcUK9BcbaexMWu5gUZwAASd64QLL92OhppwkuVErr1TwhuLgNmvRp5TVzwaqjY1hgqbK8iw01wh3HvRP0VZ-xqnM1iG8F96LE4doe6s3LkBcJkHFhPIX-J-wstyRI1gAjJLyUDEV72P0YFhPFRVeAzldia79kRQaZzTeGknrzpBSyD1A-9exmXCtkPoslypz3bUYNLCblGG34NO3vXMs-R_Yh7CiDSmfkhtZI8UOacllux4ZMvNu13sLmaDaxhUInilmbI-GrwHGeFq8NHmWBnRN-9XwH-VqiC7NmOsfIgPU4_6yxipZzPqa2XknsRbBE7DsAZrUAjf74jNHXXue9XWBTdIVK-M9pyL6z-mjk5V-x-qaq91ONyABaWCVDLPjpXmRqfK39_e8P7zSl-Ps_kPfDvqc-6x94otxHGgrd2Kun55DNVvVX0Ua07H9RrZoiI0pwoqcS9S4iVZz5E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b963f629b0.mp4?token=fJNwhHhp-UZ-ZF4htG7ieqD0QKYLT-yVh6NdFCmhffjwVJGV1Kp8HPLb3QgU3q0rOce9cAyt9JS28dbXoArYyFmBfZSGkCIwvmSIiGiizpYa_HHBBRo2NNU1jMXShhewS5a1yJM_-lubEK5hhUfK-LYEafNm7V-w1U02iRrqP_zT2fbXX407CTyij58Z_wcUp5KHbLlpB8vbp9_Hhr8Oc2gBNtcUK9BcbaexMWu5gUZwAASd64QLL92OhppwkuVErr1TwhuLgNmvRp5TVzwaqjY1hgqbK8iw01wh3HvRP0VZ-xqnM1iG8F96LE4doe6s3LkBcJkHFhPIX-J-wstyRI1gAjJLyUDEV72P0YFhPFRVeAzldia79kRQaZzTeGknrzpBSyD1A-9exmXCtkPoslypz3bUYNLCblGG34NO3vXMs-R_Yh7CiDSmfkhtZI8UOacllux4ZMvNu13sLmaDaxhUInilmbI-GrwHGeFq8NHmWBnRN-9XwH-VqiC7NmOsfIgPU4_6yxipZzPqa2XknsRbBE7DsAZrUAjf74jNHXXue9XWBTdIVK-M9pyL6z-mjk5V-x-qaq91ONyABaWCVDLPjpXmRqfK39_e8P7zSl-Ps_kPfDvqc-6x94otxHGgrd2Kun55DNVvVX0Ua07H9RrZoiI0pwoqcS9S4iVZz5E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
میلاد کرمی: بخاطر چند میلیون پول بیشتر تصمیم گرفتم یه حرکت وحشتناک بزنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101583" target="_blank">📅 19:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101582">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wg2V3IwsQUDztxSWLMSZ0149FdSq3_hWUJHpG44I5f3JWVBE2kUuRwkQXqbgp2leU2w4oWcaJ3HvllC-HrNDHPm1Oi946PG9gsRXCQ1noZl9GoNflPxNyHtaU70Izs3nd0DRy9vAejFyGwSnEaBqdJmWiBDNjTnfHF5qM1sWD_YxJIS2Wx_uYcI_x2Kgqs-iWHxfYfjp-fl4OL0t_klpmUxGOI0o4hxEBDE2ElZWBhyfQKfBB31KwQER0JH1T9W04WEJXB9fGQoLXo1YjWGBn4eLBnGwsIQk1Uqh3idJQlyRCqw3xUW5DMyG8fUOi-2ZRuVs7vFMwDcHIMyr0fgjsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏امباپه در این فصل آقای گل لالیگا، چمپیونزلیگ و جام جهانی شد و در نهایت هیچ جامی برنده نشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101582" target="_blank">📅 19:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101581">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/723401c013.mp4?token=AvPR6QSu_pKjREslsAsp-YL1pPkQYPnPOgUgqiGACnV8cG3rmAEsUSJRd9284x3S3TkD_9wmv42Jwo3eA-Bs3UBLlYTbJBCWCzCOEHgl12ZRphGEIr8n34Fb49ZZJdKcvpxOlgPYgYKsKhVzoIa5x_4V7MNqfDlM9UH11ekNK9dQFo_mzsPjUea4yDfpMV1D2RNnf_ITzwBijwBsgiYJsO_jMKGgq3MmlFmM0bz6eqtJFKXRRnqaFxuneFFBv0pwDcSYJdwLtYNbVQL0YSaAZm7TiArCLAyv565ptpp7fRqioPaOGtkmPA6Q-Td4_gIXrMcxrMa2KElfx_Plx8uR-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/723401c013.mp4?token=AvPR6QSu_pKjREslsAsp-YL1pPkQYPnPOgUgqiGACnV8cG3rmAEsUSJRd9284x3S3TkD_9wmv42Jwo3eA-Bs3UBLlYTbJBCWCzCOEHgl12ZRphGEIr8n34Fb49ZZJdKcvpxOlgPYgYKsKhVzoIa5x_4V7MNqfDlM9UH11ekNK9dQFo_mzsPjUea4yDfpMV1D2RNnf_ITzwBijwBsgiYJsO_jMKGgq3MmlFmM0bz6eqtJFKXRRnqaFxuneFFBv0pwDcSYJdwLtYNbVQL0YSaAZm7TiArCLAyv565ptpp7fRqioPaOGtkmPA6Q-Td4_gIXrMcxrMa2KElfx_Plx8uR-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
علی‌قلی‌زاده: در عمل جراحی رباطی که داشتم، از یک‌عضو جسد برای پیوند استفاده شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101581" target="_blank">📅 19:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101580">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOPDetbxkmm55LrLCUBLxGO_Fx_p692g0rnPctcDFQYecu2kSH3OUDive-zZVbwm3gayzlxrHuITRO0peIBiFVRq1UNp4G6VYS032HFRPbFUt022pOxiIKnp_spHhjBZgw_xEGjbsZ-a1eZsiWvC4FeumpuOTjw6zZOkKKhz5VeD-dY-fbta9_EoeXj1euFxmLfzsWfXepAgG3sM74emoAkKEXAQ4rMKD-dXRnFdlcsUWHYZ-zS418mo_76PEAlBjW0s7EU3LaftZCegquP5Uo2k2yJCEGr3PP_4eWYmzSsRS2YI1QsFMwVQ_pMtywRvpy89lV6zUL1Qwk8e_kI17Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پزشکیان:
دستور ویژه دادم که سایت عادل فردوسی‌پور از فیلتر خارج بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101580" target="_blank">📅 19:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101579">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d838DzKni0_4RDUJWSbc1Z6ErwFc-nGxkxfsV6EauygPyBz1200myemE7gdZoUdrvbl4wIjq08VHeg4Ix_s6Aw6hWJZFa2FbNLCwbi0jkuuYRnBHRf--Xi-Hvizw2Ld0p9lTSAlAz_NkQfbye8-bpzgB-EyCzmHmC4_n3-u47PxgdnssaGTIc4Qhp2S0NVRVijZzKdAphpz2hh0ZSuzlA69JtieaP8GnjnWSGcq7WnrjvOhDXYkF54UcCbKBNR6VVzP4fckMTLjfaagqlfhL9JAY0913Y70XNBFepdtrEyXUU2crgTx4FHW5hP6G5aDec2gWehpud1Ij3qIInTNdbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاد بولی از زمان اومدنش به چلسی 291 میلیون پوند برای بازیکنای آکادمی منچسترسیتی هزینه کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101579" target="_blank">📅 19:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101578">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNEIfS8qg8gdALF6czHSbDmn7iFzN9BC1MDNI_rYxGCEcv0jS-uGpoPayXml1HCTlVOdx_SYYz5lecvfiZXEye2X_s4cMED_Z9T4uhN4LUgMsdP3NpgrMUDpvIElQiK4XdgMZGnPKR-pm2bQmffy3hd_J0V-KVrnuMD5hPPh4FTbQcJMB6XCGSfS6sf8SMrBlCEF2WIwurlbFbXInHzw_yK1Pd-hUm1ryjBjqBdOKYcGUGPLibLNIw-cBFjH1EcooEKu0LsZBFtqU7MlDlEHwEdbasCkPbdO66RnevG7qExnky2M99UANprjn8lBbsa7tJ3QJNku-AHZDH5DsCwVWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101578" target="_blank">📅 19:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101577">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab44dc23d.mp4?token=gYRqykFk0wGFQITTX9DvzU4Rchm8FdhidDbx_UBx-nZGfpyjwSsoA1hIi6I1N6I62igoM86U3M5D-cXCoko4-3sPlv-WD_rI0EQtGAGEbbiB7JDY4qzdGAtk4FLOAADKYjpJ2eTjpVKo76Hmc7A-Xg8RW-irN8kkDkIcfSLSdP5I9qANLIDSl1hEJ9Cm2O_lqzqZBwxCnlAJT_0IqFMN5ogJdTiy-U2WWgnfdunQPFL_6CiqYq_A2kPYuMkzabTUc07vasI85u9HfbObN7EG8i-fMsOQD-DYvihGq7ZJjY9Sq-BrqKJBZAMLc1I2UUkn2aLTRYdmkdKWRlsyXNc77A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab44dc23d.mp4?token=gYRqykFk0wGFQITTX9DvzU4Rchm8FdhidDbx_UBx-nZGfpyjwSsoA1hIi6I1N6I62igoM86U3M5D-cXCoko4-3sPlv-WD_rI0EQtGAGEbbiB7JDY4qzdGAtk4FLOAADKYjpJ2eTjpVKo76Hmc7A-Xg8RW-irN8kkDkIcfSLSdP5I9qANLIDSl1hEJ9Cm2O_lqzqZBwxCnlAJT_0IqFMN5ogJdTiy-U2WWgnfdunQPFL_6CiqYq_A2kPYuMkzabTUc07vasI85u9HfbObN7EG8i-fMsOQD-DYvihGq7ZJjY9Sq-BrqKJBZAMLc1I2UUkn2aLTRYdmkdKWRlsyXNc77A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
دیس سیدجلال‌حسینی به محمدحسین میثاقی و عادل فردوسی‌پور: یادشون رفته از کیروش حمایت می‌کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101577" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101576">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c61d3ee9.mp4?token=tetgNOiPlOb2DsAesrxelN5sWTkKVc5izy49YwHc4siRK9Cg31LQu3r3FsIaQYTLtuQFSMavWu_tdtIrd9Y-NLa9k4Aw0BnAz3R23piWWwFjgiGEI4LVWgL9DoHSkkf70CeOOE7oixQ4jbWjzQvozCAG8eylbO-2-hJrn4ex5po6gDTJ3RsSSm97A-1AC5fksN7K2NGT3pdCyURvCnAVqHR9PhEZUEb_JxyGrwXXj7AXPSH5U65w9N-jwSVGUS4j0qS3H-yg3NkRjaa_gaugNcYkVQf4Qm8sqt-z67vtexlQgAyiMdxpiyyefZ4uoGJdSAWvE0d6d021tnw2rWB6Fqme_7tG3KwVY4e90ipHpOVGA2y3o4FWCFQWnbD0YcOpOi3hZxrneTw9d3BjSNRvL6qpUHecA7Q-3p0f4gfJWA4nTRHsS_zURmZJGEOGRrlRWEdhdWi3_V5bib07h6hqhXUqUEx1DBP3mmqBnNIyjIsSEaicnPVvTiW-3L579bRVCYgdgA47P42L-GPpypdhQqle2K8B1u2AbhtBgTcaDCx0eO4BPZkieuV_fyVfIydd6yGY7ffpyFn5qBwtu9JPd10ZHjmStiiDYBLug05uuZwrqj0FwLpnYZKp7ylJwBXHe_99XQzdEwsAadGUQqKlvqI2alIiwauaq9ijiZ8NzP4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c61d3ee9.mp4?token=tetgNOiPlOb2DsAesrxelN5sWTkKVc5izy49YwHc4siRK9Cg31LQu3r3FsIaQYTLtuQFSMavWu_tdtIrd9Y-NLa9k4Aw0BnAz3R23piWWwFjgiGEI4LVWgL9DoHSkkf70CeOOE7oixQ4jbWjzQvozCAG8eylbO-2-hJrn4ex5po6gDTJ3RsSSm97A-1AC5fksN7K2NGT3pdCyURvCnAVqHR9PhEZUEb_JxyGrwXXj7AXPSH5U65w9N-jwSVGUS4j0qS3H-yg3NkRjaa_gaugNcYkVQf4Qm8sqt-z67vtexlQgAyiMdxpiyyefZ4uoGJdSAWvE0d6d021tnw2rWB6Fqme_7tG3KwVY4e90ipHpOVGA2y3o4FWCFQWnbD0YcOpOi3hZxrneTw9d3BjSNRvL6qpUHecA7Q-3p0f4gfJWA4nTRHsS_zURmZJGEOGRrlRWEdhdWi3_V5bib07h6hqhXUqUEx1DBP3mmqBnNIyjIsSEaicnPVvTiW-3L579bRVCYgdgA47P42L-GPpypdhQqle2K8B1u2AbhtBgTcaDCx0eO4BPZkieuV_fyVfIydd6yGY7ffpyFn5qBwtu9JPd10ZHjmStiiDYBLug05uuZwrqj0FwLpnYZKp7ylJwBXHe_99XQzdEwsAadGUQqKlvqI2alIiwauaq9ijiZ8NzP4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
قدرت شوت‌زنی اسطوره‌رونالدو که اگر‌توپ گل نمیشد قطعا بازیکن مصدوم میشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101576" target="_blank">📅 18:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101575">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/641d875577.mp4?token=B1eAHQM4sTn8udmJNTrr2bHfjFVgzczBX4JXihmaIzlvzj60jqp54cnTPkNrLABjP3YK-HAQcREyEQZwdceKKaCAzdr-kmwwgXv7wMi7BnkeD_A1KVCh-hWhVK1jxQBgv-NmclKv3ot_8SoUFTqze2XBXjdIuxtsG_l8OjGHixoEX7sQppbGTIqrpW-BWYGR4TLonJj8Ogj94w4N0JdsCvApykvBRVpEvthf9fMfH83w8lE-aSJRLG0hOj5MVR8rOIFkmMTqTTQeaTH-pbrQfcaamAHPENk5RRdS37ffAGgXyrRixwsb5miHoWwNRWPQNFm6Bjhg1HA3iSXJWfvggQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/641d875577.mp4?token=B1eAHQM4sTn8udmJNTrr2bHfjFVgzczBX4JXihmaIzlvzj60jqp54cnTPkNrLABjP3YK-HAQcREyEQZwdceKKaCAzdr-kmwwgXv7wMi7BnkeD_A1KVCh-hWhVK1jxQBgv-NmclKv3ot_8SoUFTqze2XBXjdIuxtsG_l8OjGHixoEX7sQppbGTIqrpW-BWYGR4TLonJj8Ogj94w4N0JdsCvApykvBRVpEvthf9fMfH83w8lE-aSJRLG0hOj5MVR8rOIFkmMTqTTQeaTH-pbrQfcaamAHPENk5RRdS37ffAGgXyrRixwsb5miHoWwNRWPQNFm6Bjhg1HA3iSXJWfvggQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
علی‌ قلی‌زاده‌: کل خانواده‌ام استقلالیه ولی من عاشق پرسپولیسم؛ خیلی دوست دارم در پرسپولیس بازی کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101575" target="_blank">📅 18:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101574">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdff7389ce.mp4?token=EAbS3qpSDQtUB8mo0KA6Z0j8fnbmC0MiEvtwk2FspR9RXp0yhb9f_a6DO6607rD3_iP3JWk72hoeK9YT6ihbZ5fqAHnqSReixbmfKy7sF9RBnVMVg45vyxJsndZhlcNCT-qrvQStgvTamEoX85GRY5pqU76wlodk--tpzy7B1z-_4HFslTioXujMfZp5-6S2aFdybIIgIHTsakcgrPW8oVuNAWTI29YhVMVyA7v8L6H1Q8tiPAgr1AXTA2UxCgKVTTPdJZelhH56qwleJO9AjKIk6Y0kPGJqCZ-cJr3jTB6-9G3GIMRNrddWyUwwkDaifQihK2Mjfzv_8LIqVzXufg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdff7389ce.mp4?token=EAbS3qpSDQtUB8mo0KA6Z0j8fnbmC0MiEvtwk2FspR9RXp0yhb9f_a6DO6607rD3_iP3JWk72hoeK9YT6ihbZ5fqAHnqSReixbmfKy7sF9RBnVMVg45vyxJsndZhlcNCT-qrvQStgvTamEoX85GRY5pqU76wlodk--tpzy7B1z-_4HFslTioXujMfZp5-6S2aFdybIIgIHTsakcgrPW8oVuNAWTI29YhVMVyA7v8L6H1Q8tiPAgr1AXTA2UxCgKVTTPdJZelhH56qwleJO9AjKIk6Y0kPGJqCZ-cJr3jTB6-9G3GIMRNrddWyUwwkDaifQihK2Mjfzv_8LIqVzXufg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
جواب عادل فردوسی‌پور به حرف‌های اخیر قلعه‌نویی: بودجه یک‌فصل تولید برنامه من از پاداش سرمربی تیم‌ملی قطعا کمتره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101574" target="_blank">📅 18:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101573">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAsTI2cpylmcBMXNr_iiX__brwLTl2uc1QH3V9764dt5xSJ6ZwCSWa_xrmxb22vAStBVQ6d6ozkQwC-PdbCmuJ9uCiImykB5G_9GIhTAUGvNT_BpDzh_73ILnRJOrroiq2kdcNqU2mJakcmyV-Hs5yY35LF4hxQfOpbYjKDZojXeY71Jz44cCCrFaykcXgxGWo8kjSdchjCLmD3W_fATe6u6V8nOwvebNF7f1dPtuj80lwoI5nKeplnK5tJh38uo_jtw4_b2UqaYsY7t42EpU7w4H6SsT56zi5AGwUY8s2QJesjiCTPyqf_LnHBc32b5yAXw1eTWkYW5vx6sZWVLaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
👀
فدراسیون بین‌المللی تاریخ و آمار فوتبال (IFFHS) به صورت رسمی لئو مسی را به عنوان بهترین بازیکن جام جهانی ۲۰۲۶ معرفی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101573" target="_blank">📅 18:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101572">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f420d24855.mp4?token=TpFnpUEX1UT2cNQcr32oUJh3y50Zw2_oCfxZ33kcnb8Sra9Zxf5puooYwwne_2TJI9jFdUTS9cC80S8OtNmWLFmIBpkt2eEB-V6s0EUxHihDIilx4gK0iz_ZQaVTo4oyuTRh6qiZyqWUo53t84iJ6M9TUpU89S-6LvilD3SnvajaQe-dB1RzAFhmgNhbpc-JoFamsW7QWe1G8-TEHfAosuRXHPZq_zIfdU2GDaLRxpGffK6-GsbBQXWmGVFkW4i75ucYhN35vxHK-aWjukTs9skiXu7QTbOWKfRT1vqJ0gOOw7a9r7yNpaEBojch28GbcOkz7qBqMg_t5IaOc6kKJToB9fhKebLkPtn-zibeH92owy89rVfxQ7LZklmHC8tzdoqVYM3EM7fvV4CGZnFhFXBV06BykBl7Yz5BRmKXTShgshabvTuUBnPcreScyr7K8fzVArgKcvUjzaKkgLSFV8kzNzrseLRfz2DoBnRdOlFSLWbjq3OLbzQt7SKU3WJW_WSS4Kt0Errva12QoUMf5Er8ymL4V6bpEZsqt3r3aoDsDzzLI0ksz63h18bjosS3qaDu3_F8-tAt6rKpavB-16bgu-0hi4Ra4RiRs4dArDZ79Jt7ZqSSuCtnmbN3sw33fSCda_dD5e4JZzQlFZt8QVd0DernsyVdDg2dHi9dZ9E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f420d24855.mp4?token=TpFnpUEX1UT2cNQcr32oUJh3y50Zw2_oCfxZ33kcnb8Sra9Zxf5puooYwwne_2TJI9jFdUTS9cC80S8OtNmWLFmIBpkt2eEB-V6s0EUxHihDIilx4gK0iz_ZQaVTo4oyuTRh6qiZyqWUo53t84iJ6M9TUpU89S-6LvilD3SnvajaQe-dB1RzAFhmgNhbpc-JoFamsW7QWe1G8-TEHfAosuRXHPZq_zIfdU2GDaLRxpGffK6-GsbBQXWmGVFkW4i75ucYhN35vxHK-aWjukTs9skiXu7QTbOWKfRT1vqJ0gOOw7a9r7yNpaEBojch28GbcOkz7qBqMg_t5IaOc6kKJToB9fhKebLkPtn-zibeH92owy89rVfxQ7LZklmHC8tzdoqVYM3EM7fvV4CGZnFhFXBV06BykBl7Yz5BRmKXTShgshabvTuUBnPcreScyr7K8fzVArgKcvUjzaKkgLSFV8kzNzrseLRfz2DoBnRdOlFSLWbjq3OLbzQt7SKU3WJW_WSS4Kt0Errva12QoUMf5Er8ymL4V6bpEZsqt3r3aoDsDzzLI0ksz63h18bjosS3qaDu3_F8-tAt6rKpavB-16bgu-0hi4Ra4RiRs4dArDZ79Jt7ZqSSuCtnmbN3sw33fSCda_dD5e4JZzQlFZt8QVd0DernsyVdDg2dHi9dZ9E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
وقتی صحبت از کارما میشه منظور چیه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101572" target="_blank">📅 18:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101571">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMb1DtwuxRexnivDJVA47gz-yhFLy6aoL_Ewn8AZDmwOhYy-Z6zFQbJDgYFaPtbsLYAERHdfwsbiVJmapOOkBBGag7qPLDVphLyO7fJflx3q9m-strZ2ndNyppk0wodRW_i22Sf7_bgCnEemcE6wCO5poWHwd0LJ2ZMpicsjXQV8HRuJ9br2gm0hDEucIKaosB1XZOQF4gknPBKcDts2sFLBrL4MguXY_QXn2bjupI3lhc0uGrqGRx46B4q6WLWO5wdUbHRkuKN20ZB9f-ei-_D4YgB0BYw6dPPh9Sb0KKLwxdd9q6ITw0jyKllUJvF-TxZ8cwISYCSb9otqduairA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول و آرسنال درحال رقابت شدید برای جذب بردلی‌بارکولا هستند. حداقل رقم پیشنهادی به پاری‌سن‌ژرمن حدود ۱۰۰ میلیون یورو تخمین زده شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101571" target="_blank">📅 17:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101570">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb17487185.mp4?token=nFa0LcBeWbBNu46tBTsODHOnZIJl_yGOA0Uy53qLZdb9VzHm730rcUxsgL-6IvqGrxVgvCnT37qkCLT47T6NYJRZ8YsIE4TTYvvMFLpUVnw7iZ4PZ9X6JbZZOFgj1Lwe72XoRoD5bo54kYv2QPqoW0c1kI8W3tp_SzyUjXaEZsatV023XkKtawlASbtIrfq4ERDfkrFW4AVIkgeohRPYi7xfzv_aFm3kOejp9Ux7FjPD-WwCJakpPWJG821PlHiZ1PMNzze83rO3U43hmo9GB7_KSHjHCxXcjDT6rqocFlBDwe-8tM3dGMrjtKCU1J6b0m3CE54y-VyWptczyLi7Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb17487185.mp4?token=nFa0LcBeWbBNu46tBTsODHOnZIJl_yGOA0Uy53qLZdb9VzHm730rcUxsgL-6IvqGrxVgvCnT37qkCLT47T6NYJRZ8YsIE4TTYvvMFLpUVnw7iZ4PZ9X6JbZZOFgj1Lwe72XoRoD5bo54kYv2QPqoW0c1kI8W3tp_SzyUjXaEZsatV023XkKtawlASbtIrfq4ERDfkrFW4AVIkgeohRPYi7xfzv_aFm3kOejp9Ux7FjPD-WwCJakpPWJG821PlHiZ1PMNzze83rO3U43hmo9GB7_KSHjHCxXcjDT6rqocFlBDwe-8tM3dGMrjtKCU1J6b0m3CE54y-VyWptczyLi7Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت‌سوزهای اسطوره فران‌تورس ستاره فعلی اسپانیا در فصل گذشته برای بارسلونا
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101570" target="_blank">📅 17:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101569">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea79a8c03.mp4?token=mXVl4H0xfrS-XE7jQWYNfBBCodiDgcMFHiR9yjULqUK5J-l5R4x2N-9keWWe_sVAT47p5JxPLQ0U5xs1rPqSHsF-5BnDLADS9alkr3nlXpvy-yGfrc3zVRnbeTKYMlN4y3xNFow0xpoIV52CI_wLaR7iCxchD8ZaresbsL9jfL4hwkDB8eetXByxi5JcLBP938lstkwo63ucVgZj1st3krt7v8Hk9e_B-qAibhH8REhizwrLegkwt9SGMvT3KiY5bcgdwTtmdnS22U3DEMgsrIcEbgNV1Bg_hjCgfovmoLz6jckD_6OdgFyNPVFHyfZTMAJpG2vDKAZ4FwCSh6eVgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea79a8c03.mp4?token=mXVl4H0xfrS-XE7jQWYNfBBCodiDgcMFHiR9yjULqUK5J-l5R4x2N-9keWWe_sVAT47p5JxPLQ0U5xs1rPqSHsF-5BnDLADS9alkr3nlXpvy-yGfrc3zVRnbeTKYMlN4y3xNFow0xpoIV52CI_wLaR7iCxchD8ZaresbsL9jfL4hwkDB8eetXByxi5JcLBP938lstkwo63ucVgZj1st3krt7v8Hk9e_B-qAibhH8REhizwrLegkwt9SGMvT3KiY5bcgdwTtmdnS22U3DEMgsrIcEbgNV1Bg_hjCgfovmoLz6jckD_6OdgFyNPVFHyfZTMAJpG2vDKAZ4FwCSh6eVgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
دسته‌گل استاد فران‌تورس در حین حمل مینی کاپ اهدایی جام‌جهانی از سوی فیفا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101569" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101568">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nh-0CQup4_EttELq7AvR8ZOenLPLDRKz-NxoG2srcqScfJjbkot0dkgAdcBfSuOBZGJxcR7eDjjp-B0VF7n2dpQgWA9FUS5HfWdn41elXQmI4t7rJfeljb-OHJbQ2onyjgU8mzTCGmzcMn9Mg6niP4Eqb-sIZ1Wul3Pg3CMyq2eK7QKoSvREdy_c-teJ5BxrXxGMHk8AhBWw58WAlRJaVUCplzXPQ0Ycfw7FheDkMhtz3OtqnUli73nRk8FGi_kzNvmpefGr5e3N_HRHqV0KpVIsMw3etVIsgIESZiBoU80gNZjLUJyqPL1Sxf34t7N1gr9qQKxr7HoEprsVrFhZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب منتخب جام‌جهانی از نگاه فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101568" target="_blank">📅 17:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101567">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38a17a2eb.mp4?token=uwhIare450-MyW2lsppEulvEOF4NgvJz0fB3RGB_BL0WwP2g_cAlfOx-XIOxseIX5A2WkYARJmbFQCHN4cOnAPDaUKzcWfUS6WfXc0j44GHQ6u63JtZYsSwvmvZHYJA85RYgU3LG00O3oWfMSbiH6yBO30f7v7nCE8boHbXOVxnbtQ1WbtgeQ6XHNxRCYgGvGS_-WdaHm0DPKGRrhEtYLZ1KM1xToVzcDaY4iuZUbtq7YkFn7jJjGz3b9DmGLqDkbsj86_QCDgxiCFrBxb5URAx7yqhrTeOKqEeEqPaZ1HvFBrO2wUZrfdqXhtqlL-LySSOEMdQVk4kcAIa82cf47g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38a17a2eb.mp4?token=uwhIare450-MyW2lsppEulvEOF4NgvJz0fB3RGB_BL0WwP2g_cAlfOx-XIOxseIX5A2WkYARJmbFQCHN4cOnAPDaUKzcWfUS6WfXc0j44GHQ6u63JtZYsSwvmvZHYJA85RYgU3LG00O3oWfMSbiH6yBO30f7v7nCE8boHbXOVxnbtQ1WbtgeQ6XHNxRCYgGvGS_-WdaHm0DPKGRrhEtYLZ1KM1xToVzcDaY4iuZUbtq7YkFn7jJjGz3b9DmGLqDkbsj86_QCDgxiCFrBxb5URAx7yqhrTeOKqEeEqPaZ1HvFBrO2wUZrfdqXhtqlL-LySSOEMdQVk4kcAIa82cf47g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
✔️
پیش‌بینی پپ در مورد شرایط رودری در مهر ماه ۱۴۰۴ که در ۲۸ تیر ۱۴۰۵ به حقیقت پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101567" target="_blank">📅 17:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101566">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be9c5de5c5.mp4?token=Pp-KOLS6-A9h0RmtI6tKJqrzWWRfI_H2VHLVdt6UiuM2MvfXjCgkua_DqJOxSIQljaSjqE_-rzeCUWkkPa-WWkZstXr1EeXZV4gKGnW7B_tgAP1-Ji9M50lbMAZ5TIjNce17i6oYK-6EygvIZnDUDcL_VoNUYWEI4nk9IFjQ8rByPLz-SZyv3sJCMqsaTSgC0rXaZrdt6maMyzljD1UNLEwLLp7G9hDQs6ML4-6cmO2FtXuwYY4E7LnIikymNIiE0hVTPIZf2sG8RIInjbRRybpHsrViR5sARupZVuQztAAG_2vRTAorL7UvsOUeO2eUVCFEuEaGEr1HLGuskoLnMSmIECWoCXxAbNbZrjL6FY52pLLFiQNmk2nqm0Dxn8diGmfXeQZoVJkh9dtaFx53g5_Egg6tEFbWcBHAmRzk6_4MO6ae7Vqn-_e-Ra6t3ooeTR9_MYVRnhf9SRTg_i3-qEoeT4Z8jacR_OyKRDaiM4vvpEolL-YCGpeT_LZ41K-MDeKNFHQfADq0lgcwweMP7vekY33kz_yET6PkiVM9VOusYo7eZ0-IRQeoYmq99b2eZqqXgsrSpCdVjLi8XocqccvA9Hc3pvqIQOu3E9Z7yCT8EOI_0XKu-JyJ3V3-PQDtpxq_PFGk3SaryvOffZP9jDQOOBvNMpw7oMg7if7NUYE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be9c5de5c5.mp4?token=Pp-KOLS6-A9h0RmtI6tKJqrzWWRfI_H2VHLVdt6UiuM2MvfXjCgkua_DqJOxSIQljaSjqE_-rzeCUWkkPa-WWkZstXr1EeXZV4gKGnW7B_tgAP1-Ji9M50lbMAZ5TIjNce17i6oYK-6EygvIZnDUDcL_VoNUYWEI4nk9IFjQ8rByPLz-SZyv3sJCMqsaTSgC0rXaZrdt6maMyzljD1UNLEwLLp7G9hDQs6ML4-6cmO2FtXuwYY4E7LnIikymNIiE0hVTPIZf2sG8RIInjbRRybpHsrViR5sARupZVuQztAAG_2vRTAorL7UvsOUeO2eUVCFEuEaGEr1HLGuskoLnMSmIECWoCXxAbNbZrjL6FY52pLLFiQNmk2nqm0Dxn8diGmfXeQZoVJkh9dtaFx53g5_Egg6tEFbWcBHAmRzk6_4MO6ae7Vqn-_e-Ra6t3ooeTR9_MYVRnhf9SRTg_i3-qEoeT4Z8jacR_OyKRDaiM4vvpEolL-YCGpeT_LZ41K-MDeKNFHQfADq0lgcwweMP7vekY33kz_yET6PkiVM9VOusYo7eZ0-IRQeoYmq99b2eZqqXgsrSpCdVjLi8XocqccvA9Hc3pvqIQOu3E9Z7yCT8EOI_0XKu-JyJ3V3-PQDtpxq_PFGk3SaryvOffZP9jDQOOBvNMpw7oMg7if7NUYE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمود شهریاری چه اجرایی کرد
😂
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101566" target="_blank">📅 16:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101565">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVpQidIBnvOfaKFfrehR3kkeDxzRmB5heRvhhHKoghtWIRL3RYHgCZ3Z1sbHWwKNNhQuT7StoPvmlD6LzVdMYPf2P4UNf7gM0y5Gt5Xvx9EqUm9uZqIOOUlynY3IoctitG33dItwaeqP5mk4P8nCI6gaAVd3-5KQNruQA75rvIu3QJo3gFmIC5VEX0D5uuJmd76O8hqKkIxGUVwULniGy-JPfrgeHaFvFZJ9MqT-J2G3UJHwZTP_DvvREMbxqV2k9F4lAAG95ETyYMyouymx2EHodlzqJm19D_0AEmRitBIxSQWMWW8RjuKpMuN_QHo7F-a4r8OxaJWT0JBQ_to4Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ: از این به بعد، هر زمان که جمهوری اسلامی ایران در تنگه هرمز به یک کشتی شلیک کند، چه با موشک، چه با پهپاد یا هر وسیله یا سلاح دیگری، ایالات متحده یک پل یا نیروگاه را بمباران و نابود خواهد کرد، از جمله آن‌هایی که در کنار یا در شهر پایتخت تهران قرار دارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101565" target="_blank">📅 16:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101564">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🎙
🚨
حمایت جالب رضا‌رشیدپور از فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101564" target="_blank">📅 16:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101563">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318ac55e88.mp4?token=l9F4-UXz3Coi3PtfsdRC6o01ecNcd_oUMB_pC1lx_vNtH3G7UizG6QvHIC6ebfzkuvkv7A-pyVtMc-Ry56NUKWs0z9fSIVXl6SV8zBBwsvnHNij0SsWelHJdaB8sko4aRWK-SEvB651apLyI1Ln6uI6a5KW66zgLfWOJafR_5XUAUwsOJyz_zCpSgq1PVt1LZhAivi2ChZ-gcifqnDwG4eBNF0WWY_su0knATtXizskKeV1Ya0nLs_VvtcNkD_m2mtJcPYn2xVvUlKg-0VIdfucr2GnRrbPqGfQhJDlof8jRGthV8W9970wyn_WBdT0hn6YFxuKgBWyfjKaFVzt_lHUKrtFcQNLU_hHPaM0Tm8HCU9yXHgj4Wg7n2z9boVhNgc_aSrBiIXkEticPEiPXHPISemyFxP4odontK7zzbc0LxC0Zy1a3CSRS9hK7CMdOmbimMYKUgAMzffEMYwbBMFviKBWwFncKOK-9pL7HEanz1AJ4xVGxBs1aggqsBqWjwXo9v9aagcfPen_jirAFEOc0-nl1LPiwkstbl32GHaSixTvKF_u9TxowVh5NAgZZhMLz6jZNiknoQ7xaazb0H0QH64qEC46-7VeNi-1gYr8TfbRHpzkMiWu_X8iuPlrnvN7gezBHIpZKsobv2pKZyceCM4WMi2L89VcH8TXBA3s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318ac55e88.mp4?token=l9F4-UXz3Coi3PtfsdRC6o01ecNcd_oUMB_pC1lx_vNtH3G7UizG6QvHIC6ebfzkuvkv7A-pyVtMc-Ry56NUKWs0z9fSIVXl6SV8zBBwsvnHNij0SsWelHJdaB8sko4aRWK-SEvB651apLyI1Ln6uI6a5KW66zgLfWOJafR_5XUAUwsOJyz_zCpSgq1PVt1LZhAivi2ChZ-gcifqnDwG4eBNF0WWY_su0knATtXizskKeV1Ya0nLs_VvtcNkD_m2mtJcPYn2xVvUlKg-0VIdfucr2GnRrbPqGfQhJDlof8jRGthV8W9970wyn_WBdT0hn6YFxuKgBWyfjKaFVzt_lHUKrtFcQNLU_hHPaM0Tm8HCU9yXHgj4Wg7n2z9boVhNgc_aSrBiIXkEticPEiPXHPISemyFxP4odontK7zzbc0LxC0Zy1a3CSRS9hK7CMdOmbimMYKUgAMzffEMYwbBMFviKBWwFncKOK-9pL7HEanz1AJ4xVGxBs1aggqsBqWjwXo9v9aagcfPen_jirAFEOc0-nl1LPiwkstbl32GHaSixTvKF_u9TxowVh5NAgZZhMLz6jZNiknoQ7xaazb0H0QH64qEC46-7VeNi-1gYr8TfbRHpzkMiWu_X8iuPlrnvN7gezBHIpZKsobv2pKZyceCM4WMi2L89VcH8TXBA3s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
آنالیز بازی پائو کوبارسی ستاره تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101563" target="_blank">📅 16:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101562">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‼️
🎙
کنایه علی علیپور به علیرضا بیرانوند به خودم اجازه نمی دهم درباره علی دایی و کریم باقری حرف بزنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101562" target="_blank">📅 16:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101561">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🏆
🇪🇸
رسانه‌های اسپانیایی با وجود قهرمانی صحنه‌ها مشکوک داوری فینال رو منتشر کردند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101561" target="_blank">📅 15:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101560">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BV43LdwafVBBwFwcGYBmaDYgOv-_azMyI9JuArAAx0-BsMIPXO7TMV6wr9-Ta0vCG9IE_2MG26IiRZ9FBh28he4zzbJlLfe4cMBIaCxXpl5dw_tZIC_1fKDtyN-QKLORo5y_L_HqvhYQtZt30lcolW-xvUMmZI2EB9F9NMjh8D7lCNH_NfbTAGNjZCLOhtuXTlMlFohHf0fiU0NuI6sZHAiQ8XThWS4gaax5DX4Hcg39HDQIP9ESkVd24Znfo-Q8PIc-FP1JE317IYlc5mq9zClkNIxkHewZ085wsMaAN5NcKIxZo6uQ0FBfn-oK_uXv313CxlNUg4cgDd2oVc26VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
منچسترسیتی قرارداد فیل فودن را تا سال 2030 تمدید کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101560" target="_blank">📅 15:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101559">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e21d92126a.mp4?token=fPQw-Jszb7tiDR9yBi1W9iJml1jVfeggwuJzfjyLPYv76IdfwOG82rVKpiA9M8iTWR5gx1HmXZNTrs6s0UWa49VfsP_5JVmz4Ku5BEgFmJ4o0rdYL67OUw_eTE7TySFFyLE75zeST-V5E5LeH-x-X4g1wmuAMBTikKiSc3Oa36b3L_-R-g3MgcIOHXJbOPQhc-yHYoVCjRrSP6S1bAvhl1x8USkKS7OZ9_DBJ2XIIu0XK_MMYV3j3WH3LQjrlIo90erpWuTLtc1F9xAzwB3zGJMGIH_2fAnVR7iijIY3nNRbLff1td_kxqfyOeMP1hj9l-n_YT0WqF579z2QiLuMmwuQcuVilwn2nA5FBkuDOrF3KuBNMCXGq4m4t2WZxVQ4ye4HThQ-I-UF_phlvLxVbMGesA5c49jPgRKHk5sfvj7wc1P2x_sESqCpXIuAIjGq2-IvpXz9RLaBUCh4JBR3pMQg6ffSFM5EIAlUUaB4KzGgm4o3iHjinwu54IFyjc0KMXTZACq5tqplcEVPBnDLAakC1T6hIqFT2jG_q7pBsn6DWH7hVWf3Wrwg3HME7u4aVIdmfJhqfoKA9rXOuhFVs_34Vle67YVPo3UaE_19N5GnrJ2FQ7zqYU4jKvEGbej0lzTWcbQIYiwTRi4WXVtzGA1i_hK0jXYP0xBc8Oq32q0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e21d92126a.mp4?token=fPQw-Jszb7tiDR9yBi1W9iJml1jVfeggwuJzfjyLPYv76IdfwOG82rVKpiA9M8iTWR5gx1HmXZNTrs6s0UWa49VfsP_5JVmz4Ku5BEgFmJ4o0rdYL67OUw_eTE7TySFFyLE75zeST-V5E5LeH-x-X4g1wmuAMBTikKiSc3Oa36b3L_-R-g3MgcIOHXJbOPQhc-yHYoVCjRrSP6S1bAvhl1x8USkKS7OZ9_DBJ2XIIu0XK_MMYV3j3WH3LQjrlIo90erpWuTLtc1F9xAzwB3zGJMGIH_2fAnVR7iijIY3nNRbLff1td_kxqfyOeMP1hj9l-n_YT0WqF579z2QiLuMmwuQcuVilwn2nA5FBkuDOrF3KuBNMCXGq4m4t2WZxVQ4ye4HThQ-I-UF_phlvLxVbMGesA5c49jPgRKHk5sfvj7wc1P2x_sESqCpXIuAIjGq2-IvpXz9RLaBUCh4JBR3pMQg6ffSFM5EIAlUUaB4KzGgm4o3iHjinwu54IFyjc0KMXTZACq5tqplcEVPBnDLAakC1T6hIqFT2jG_q7pBsn6DWH7hVWf3Wrwg3HME7u4aVIdmfJhqfoKA9rXOuhFVs_34Vle67YVPo3UaE_19N5GnrJ2FQ7zqYU4jKvEGbej0lzTWcbQIYiwTRi4WXVtzGA1i_hK0jXYP0xBc8Oq32q0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇦🇷
رفتار عجیب بازیکنان آرژانتین در صحنه اخراج انزو فرناندز که وایرال شده !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/101559" target="_blank">📅 15:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101558">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f9401eccd.mp4?token=k67maHBCeWrtgBj4l6UWOqbUTPBYHlt0EPe2SXCsBsxNq7nu561dAaONujKQcpSWRJSA2qiZ61IxJjpMHW-jD4f_slKJIGwNRp17V3a2lMdx2OwTsxtPV_lAci5QEnRjOSEvQ8nxUFQ4iA95Bmc8WJ7bT9azBThXtr4XnNZTBOcI1HDExLWnTxXn7bfzCdd820OV9mTmWnh_d2dBj1klkLWnbh21NtedQ58PmMyxlLGjffLlvxD5JyCyz3T1ArKqCECBqwSBrgZLhwk_9YVNhqyoLmmILpaoRudreZ__8pSF08KT1IrdC7ukfKjq85WlwZvgpl5isVaiBYZtL6m80Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f9401eccd.mp4?token=k67maHBCeWrtgBj4l6UWOqbUTPBYHlt0EPe2SXCsBsxNq7nu561dAaONujKQcpSWRJSA2qiZ61IxJjpMHW-jD4f_slKJIGwNRp17V3a2lMdx2OwTsxtPV_lAci5QEnRjOSEvQ8nxUFQ4iA95Bmc8WJ7bT9azBThXtr4XnNZTBOcI1HDExLWnTxXn7bfzCdd820OV9mTmWnh_d2dBj1klkLWnbh21NtedQ58PmMyxlLGjffLlvxD5JyCyz3T1ArKqCECBqwSBrgZLhwk_9YVNhqyoLmmILpaoRudreZ__8pSF08KT1IrdC7ukfKjq85WlwZvgpl5isVaiBYZtL6m80Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
علیرضا نیکبخت جواب بیرانوند رو به زیباترین شکل ممکن داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101558" target="_blank">📅 15:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101557">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxNGPORT2zEGcLrCWHZrij7OUsDFaRM2vixzsHeI7F97x-0tilQDq7Ev_FTEG6XRgB_Zz7GecScU3MwZTkj7uklAp-7ty7-W5_85afXEAljXIyax5DiZWCU0N4yj_siiYKC-S7KqhsXLLDfmlCtv7joTvJ1PmvvBFk6pfbCJn_Tl6wrVhv0MhjWnpsVFoxf-6QffVWIE-g03W34nfycCPznSz3Xhm_C6r_J73zh_6UhMcEIE_QplW1jWtgGblorwl1LIt9wuTfPVTbUlLr6WzQgajeYrJpwlX4JuYyeQHqXWV3GRNfFcGrV7EeAhc4oOITH4E8_SNQ1U5csYUAmiOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بازیکنانی که در این فصل، در بین پنج لیگ برتر اروپا، در تمام مسابقات بیشترین گل و پاس گل رو دادن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101557" target="_blank">📅 14:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101556">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a761e81f7f.mp4?token=C450HGppWstL3TxuNA8_0PItPo9bOXurqieh3_95CFZFy6C7dcT7y3Niw4GGQrffIJ3KX3HNY72nP9IkcERW13Cg-w5tbCpHqfCsgS6rLDY0cJGadhXSRe3ZiiUnbmHoyPadM1WPOb9kK5agZjFytfyb8l1yh0wt6Fo4Og5dfeSuYhmDG5RxXG1EjknAu5t-C3iNr_kVrSqt2ZJmkUHHoWKIa9Mn4PE2ecMWwWU9zR_NrLnBwVv82GeN_1-vbp0zg_bJO-YnLGXF4QNp0Y4Gv-SFZwVpnfdOhPkAg6QtYDMBkwf0H0bz27fLeNApcuM_-REeIx2P45G9ZJUr2627kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a761e81f7f.mp4?token=C450HGppWstL3TxuNA8_0PItPo9bOXurqieh3_95CFZFy6C7dcT7y3Niw4GGQrffIJ3KX3HNY72nP9IkcERW13Cg-w5tbCpHqfCsgS6rLDY0cJGadhXSRe3ZiiUnbmHoyPadM1WPOb9kK5agZjFytfyb8l1yh0wt6Fo4Og5dfeSuYhmDG5RxXG1EjknAu5t-C3iNr_kVrSqt2ZJmkUHHoWKIa9Mn4PE2ecMWwWU9zR_NrLnBwVv82GeN_1-vbp0zg_bJO-YnLGXF4QNp0Y4Gv-SFZwVpnfdOhPkAg6QtYDMBkwf0H0bz27fLeNApcuM_-REeIx2P45G9ZJUr2627kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سگی که شباهت عجیبی به مارک کوکوریا داره و حسابی وایرال شده
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101556" target="_blank">📅 14:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101554">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VKjtUX6UOi-3ZeH23abvAhdBvsUkAGd6TjgAQcYJhn6MbEidlHgFdvU0LXYNf3rFl7uqyWhb5bKs_dioBYhAq8L352BwFb7PRtXShlVeiLD8orq1VPXM0X7r9MtrUvBuALRt82xpVdrISj5oSdU_AKyEqogKZAED_vjTMJ8qvPa4BO0_0h1s5JhDl-nzMPUZ3uuWMRRwfnkqJ_DqlO1Ka5x_oEbjGxtmBcvkO6YMSkVywMpAlHLwFQ8xrl2bpkwcdDvAQaEICqaXZWxtucJoRei0konH8QaxSN7-I1JsHl4y_u-WkUV5Scj052WHKkqaWxNgULHORt-JW9sqCtojCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lSrAtNHC6y94tpTgnDP-U8dHGKKnmzwlXq8xKOMYHB2FLSNWyIkE18-hqYAGWdSwVyWFdUwEBo5_0EBDT__yBm-pEAd5em6-cD8p15RrlZZvkhmj40WP4DkiwDO7opk5O7YC-Jan-VL4eEYWs-YmVJJ6qpSm8DYBL-reGyXYHuqxXjMGaa2w49TnwECTXe-wN0P33zNXIIE1-jdJUmTo7gYRLQvJFiobNoQxHinxNIaTb6k6V47z5b_j8N_YMGf4GcMN3NRvNuVtam8M-a6oJCxix2Dm9sx5CnkpGxifsw9wqQgbkdU6w5F_sII03M637EWZ0aU_zWFxduKm64bJ5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
خوان مونفورت، عکاس عکس معروف مسی و یامال:
من به خدا اعتقادی ندارم، اما این عکس نگاه من به زندگی رو عوض کرد. انگار همه‌چیز از قبل نوشته شده بود. هیچکس حتی در یک فیلم سینمایی هم چنین داستانی رو باور نمیکنه! هیچ توضیح منطقی یا علمی واسش وجود نداره. یکی به بهترین بازیکن تاریخ فوتبال تبدیل شد و دیگری حالا داره جای پای اونو در بارسلونا دنبال میکنه و در ۱۹ سالگی هم قهرمان جهان شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101554" target="_blank">📅 14:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101553">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgQwPGzBoEz-m9DIii7QxpCurOc1OAQy5khpXcla34LzPR5j_f3tY3pWyCU3t6zitiDUl_WIO28pRperhJkRGgaQa-qguLyCrxAGb9YUq65onsqAidnXI3vtgg-NH9XP2Z7J52ujBYi-HLjR1ETGIMkYUmICKb20bg6hoNlgfIsr3IWZYjhJy7AGB-KA2veK6v7vL78H2tygsACDgA765IHL-lNYVI2xZiGUO3_cloxk1egbhkU31JOGkXbXE2uHUMKvs8iSM37TLav8lKDY36AI7iKz58urVI4UjXw5H0x9k9gZwrME5V49kgJXXbx6K0zxtSwKoQNF3xDgRpa6XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیمار دوباره در برزیل جنجال به پا کرد!
باشگاه سانتوس اعلام کرد نیمار به‌جای سفر با تیم برای دیدار کوپاسودامریکانا، در برزیل ماند تا روی آمادگی بدنی‌اش کار کند. اما ساعاتی بعد، او در یک تورنمنت پوکر با مبلغ بالا در سائوپائولو دیده شد! این اتفاق باعث شد خیلی از هواداران شدیدا از او عصبانی شوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101553" target="_blank">📅 14:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101552">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnJQEoexCjK8M6XDW_pezwsQsjrBhHmzB1-Eej0twL-xAuAwoyMBmqar5UamiSK4cfqJio5W3VoUNfuXlGEt2qFdoPPlJCghbAXmF8XFjowsqwaX3SbND4947pKI7mPJbQxMDXXXKWdijlDd7VVPfGV-lsqCAl3W1eu-QOyplwf4ij2tPSLHzhnBjXiYdmh0qPITAfRbdP7uugzRBVRMwUdG7TBNybzCAlfImPV66LmVzP9LQQZyy2fqVlyxHc8LEqVO32EwOLmCgwIwyc2GyAepOZFU0YCRDO7541k83s1b77sr5VoTqMakewYr_jYAqWt8WvlIkmOs5kuqr94U6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔥
الکس فرگوسن: "بعد از اینکه ایتالیا جام جهانی ۲۰۰۶ را برد و یوونتوس به سری B سقوط کرد، من مطمئن بودم که او یوونتوس را ترک خواهد کرد. بازیکنی مانند او در سری B بازی نمی‌کند. در آن زمان، رئال مادرید نیز به او علاقه‌مند بود، و با توجه به مشکلاتی که یوونتوس در آن زمان داشت، تصور می‌کردم که یک رقابت جدی بین منچستریونایتد و رئال مادرید برای جذب او وجود داشته باشد.
🔹
بعد از اینکه پیشنهاد خود را ارائه کردم، پاسخ او بسیار تکان‌دهنده بود. او به من گفت: "آقای فرگوسن، شما قبلاً با من صحبت کرده‌اید و من به شما احترام زیادی می‌گذارم، اما یوونتوس در حال حاضر شرایط سختی را تجربه می‌کند و وظیفه من این است که در اینجا بمانم. یوونتوس در بحران است و من کاپیتان این تیم هستم. آیا انتظار دارید که من آن‌ها را ترک کنم؟"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101552" target="_blank">📅 14:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101551">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d88e870288.mp4?token=cYewEbzhyepwMDHuRufpB-yTpCv5RmFeBVFo3I_IgATmYETC9Y66gSyZvK8RRqvOnPhkFu76S0-OvAp57osSaAv2q6-MoAc-6ZBiQ0iG9qFAlQNq1ywcOgdXksr5pvlCdFo096aR2HJ3BBnPnUEHN_LZUhgA0jdI_Bv9O5DpK-QjX_GXYxJvESqP6_8djuubfBMiXlx45iYokS5udN_f9UNaTitBbN5hFGmBadtZgy0ysMChxso5J5E8qT6O-JOnPmQbn9qVRKQ-8XkzHSM_2y5GKe_pmQ5X6Cuxgd6V9w-DyjuN5se8rgysuJw-1anug9icnMMgbqtbrrfQ-1SJz25Pk2_zXmkVL7VPkDJeEWjDBVfo5ql7fcmFRsY4_qfr0gKGmgIck0i9eDtpJzdBoMayXy9pJRPSXsGM4zeAB6QzhMmk_ID4XjQsXGS2s3L608CTKGIybXRDJvpVwzeaWUKcbDi7UEs_dJqPzoVCLsdTB5uRdGQ8gyv2KkhgwvbCwP-P7fpXSPjJu-znj2ARzylyWlcj_uInOMwFLmoIayfletveC9sjDfg5Cj3JGGmNbMDubIfTMzwolVlUVwtXOE45eFqycUoaQqEW7Gqs91jqcuTkEpG8vDmA418lbOpYsdvN0XGCAdy2bZB4jsIU8DgUMyoa4DPqKpyBI1sIxAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d88e870288.mp4?token=cYewEbzhyepwMDHuRufpB-yTpCv5RmFeBVFo3I_IgATmYETC9Y66gSyZvK8RRqvOnPhkFu76S0-OvAp57osSaAv2q6-MoAc-6ZBiQ0iG9qFAlQNq1ywcOgdXksr5pvlCdFo096aR2HJ3BBnPnUEHN_LZUhgA0jdI_Bv9O5DpK-QjX_GXYxJvESqP6_8djuubfBMiXlx45iYokS5udN_f9UNaTitBbN5hFGmBadtZgy0ysMChxso5J5E8qT6O-JOnPmQbn9qVRKQ-8XkzHSM_2y5GKe_pmQ5X6Cuxgd6V9w-DyjuN5se8rgysuJw-1anug9icnMMgbqtbrrfQ-1SJz25Pk2_zXmkVL7VPkDJeEWjDBVfo5ql7fcmFRsY4_qfr0gKGmgIck0i9eDtpJzdBoMayXy9pJRPSXsGM4zeAB6QzhMmk_ID4XjQsXGS2s3L608CTKGIybXRDJvpVwzeaWUKcbDi7UEs_dJqPzoVCLsdTB5uRdGQ8gyv2KkhgwvbCwP-P7fpXSPjJu-znj2ARzylyWlcj_uInOMwFLmoIayfletveC9sjDfg5Cj3JGGmNbMDubIfTMzwolVlUVwtXOE45eFqycUoaQqEW7Gqs91jqcuTkEpG8vDmA418lbOpYsdvN0XGCAdy2bZB4jsIU8DgUMyoa4DPqKpyBI1sIxAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
📊
نمره‌دهی به لیونل‌مسی در بازی فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101551" target="_blank">📅 14:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101550">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c3187f185.mp4?token=fORmQm7EAwnaXM2vC33bLmNX6gF5DilpoOYQhQDocDAN23WGgZfAOCkKoQ4kInsz3P8jDemm1JZOqJi9iUu3ZWyogsIvcnDG7PTHlDGxZqa8CRcaCuZ-h7od69Rx7LvJ41KdidA64I6K_Hg9mRqG1_0Naoudg-pnuOHtoCRA_Uj-mbP1oRGrAkUybkn_nAcH3Cjyx_FTfaSthjbGo2j8LHFwULhMqKhyYe-_OD4-CKKRuCTifrg16sBIIDXU2NujWn1fpuZpG8XdsCfrc-nnZFgxtk_RUyce4nQG1PuA3vVTWxhEZ1rRGbwu4IokM3AUUR54pwJqE9ytxoMSLZNv-Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c3187f185.mp4?token=fORmQm7EAwnaXM2vC33bLmNX6gF5DilpoOYQhQDocDAN23WGgZfAOCkKoQ4kInsz3P8jDemm1JZOqJi9iUu3ZWyogsIvcnDG7PTHlDGxZqa8CRcaCuZ-h7od69Rx7LvJ41KdidA64I6K_Hg9mRqG1_0Naoudg-pnuOHtoCRA_Uj-mbP1oRGrAkUybkn_nAcH3Cjyx_FTfaSthjbGo2j8LHFwULhMqKhyYe-_OD4-CKKRuCTifrg16sBIIDXU2NujWn1fpuZpG8XdsCfrc-nnZFgxtk_RUyce4nQG1PuA3vVTWxhEZ1rRGbwu4IokM3AUUR54pwJqE9ytxoMSLZNv-Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت‌های مجتبی‌پوربخش علیه میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101550" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101549">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c0345d2fb.mp4?token=S-S5dZcVxNEJuX14HWiHit-wUHNgdDT0fZsjrmheUCkh0EDxKLnHBwDFWituKPJ4kbaXu6N4GDSjVPzeXQ2T1fRS3S_FngOAo7e4M5OD0imNY8XIGEeDtHGAqZrSDnd1MqNzLeVWQqM0GK6yNSpVNwZ49bArc9BmMV5-WhiaWfgDSdVYEOj2_2MPGurmp5owzPIrUWwUzo6MilL_7cVG7a2c7ue1PWExMcizruvVw9um7zlWBDYylTaXFwoOFx7eBUh9GK5jLySFiF2SS1-M6zSe_oWK8H-ae13LQVWzpFeGGzURR-OhAI_dtJbyM58bOdbcheDjXm5LLXUlwSoRug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c0345d2fb.mp4?token=S-S5dZcVxNEJuX14HWiHit-wUHNgdDT0fZsjrmheUCkh0EDxKLnHBwDFWituKPJ4kbaXu6N4GDSjVPzeXQ2T1fRS3S_FngOAo7e4M5OD0imNY8XIGEeDtHGAqZrSDnd1MqNzLeVWQqM0GK6yNSpVNwZ49bArc9BmMV5-WhiaWfgDSdVYEOj2_2MPGurmp5owzPIrUWwUzo6MilL_7cVG7a2c7ue1PWExMcizruvVw9um7zlWBDYylTaXFwoOFx7eBUh9GK5jLySFiF2SS1-M6zSe_oWK8H-ae13LQVWzpFeGGzURR-OhAI_dtJbyM58bOdbcheDjXm5LLXUlwSoRug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
خاطره بامزه علی دایی از معلم زبان خود و کریم باقری در دوران حضور در بیلفلد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101549" target="_blank">📅 13:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101548">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbd74933b1.mp4?token=OtWgqCjXJOzx9Xqpv9Ac4lXFnzvCMfNIT97I4kIRZhbheKDQdMqp4EZP1FfRJ5mSnFdDa4hdJo2lhb_l_j86a7dpXyuTyBME_xCL1S41rK5U8KvPh9eqUEP6ZBEIe3kcIsOZfymFRV5vlBKsYO1haJpdOrcw5ITO-u9t4vTHZEn4-TYmS-ecphhH0EGRx-oVLzldkDAeJ_3gAwMqcX8v0x9jhJpH7MiIcWFFQI9MGc-8wmxU472Yw2ybE6X9cT2ztmsFMTM_BPaQZOy_Li8H-Ko4Btfq_VBR-OIyAZJipnzsefFMgcc772puwGjdBs4qMf_35q-xPnK_EVPfxu7IQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbd74933b1.mp4?token=OtWgqCjXJOzx9Xqpv9Ac4lXFnzvCMfNIT97I4kIRZhbheKDQdMqp4EZP1FfRJ5mSnFdDa4hdJo2lhb_l_j86a7dpXyuTyBME_xCL1S41rK5U8KvPh9eqUEP6ZBEIe3kcIsOZfymFRV5vlBKsYO1haJpdOrcw5ITO-u9t4vTHZEn4-TYmS-ecphhH0EGRx-oVLzldkDAeJ_3gAwMqcX8v0x9jhJpH7MiIcWFFQI9MGc-8wmxU472Yw2ybE6X9cT2ztmsFMTM_BPaQZOy_Li8H-Ko4Btfq_VBR-OIyAZJipnzsefFMgcc772puwGjdBs4qMf_35q-xPnK_EVPfxu7IQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت رئال مادرید در این روزها.
🧐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101548" target="_blank">📅 13:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101547">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVz10ERkeCYTMMvdMxzL8kAMYM7ygvP8KGUV5MfzOawXiA0WELwPbhRsANY6R1J38vCUxRz6hveffKhVljoLn8DboKxdUATg1jyRpDJpvgcT5WRJEVtPpFnPKIDt9YxHsdJEAKhF0VykvnzyIMI43X_tVt6WFBXrgHQZRJkgWopN4jyBUEA2Gn7gBZh_hyBTdVIa7MpT9pbOGIYBHLlmF44vDGaUyGkg2BMAspUrE55rYBjt7_uiSeNAo1c_TY2hV8wOpYk5D_jPOBz3oQaQUpX6sZtBWAJWF6esxGvfMShf9eldwJwKyg7mVNiyOzPSx-dgXkIprOnxu8yLU2W9Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
وینیسیوس و زیدش بعد عمل زیبایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101547" target="_blank">📅 12:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101546">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1e8799b7.mp4?token=k006BUIvCWBnrgS2fFY8jWyk8XSDoxcCuNUq3ZWYEwyWMLLKzOblKj8M2wr7BLK0zSjWKNN3SQBd-ZWg4znmkaLAi9-dw9DhhNUzpo9tLL00js3i5hLGqBTJTG41v-J-ld-dJNXeUGiBXFFKjhamHXywIopt32tQoaDG6MCspnqx4X1KbGSaIIeSvo-KizJlZ0AJ0EZgUcxfuLjCe7_miQ_-3R1e7yauCwOez6kg1SKnsR8VIA8ppgk9li8ZqsgOJbswvjAu-A7dXtaoZ1BDfhsLvIfJK9uqKjl1uNmkp50UwT7-Yf-G6lM8dfaLyj3obJf8foTjoI88Nu06rmtG4Wt5rSYNIRLd5OANBzhc3qTtOpxjvVPolO-9Pwxu5AiqfJe3KWiklXPNv2vrIpiDloK4bBUnc1RndGz7xCezc33hK2eEhgx55hHpXaZgDR8ZrbnvX_XkpMHLrxASuPtB2dwG5ZH0FyfAOGpD1cZkYXeIbvi3debudvY6YZ-CqDCiKxRKmDuFL3B2a7Am00hlU-n6lfU53D_Nr2J0pBAv_oZ0os9Cc8IBXRSgJnuEcm3v8gvweAD2TQAYeVBOuNu-re7NqTS_UczU7Jh2q1NBgm1cg1ODn0DlCPvmuS27ZAzTnHZiW5Jf0qzhdfmiv-rjef55u55tO82JbgoUXkcwTJI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1e8799b7.mp4?token=k006BUIvCWBnrgS2fFY8jWyk8XSDoxcCuNUq3ZWYEwyWMLLKzOblKj8M2wr7BLK0zSjWKNN3SQBd-ZWg4znmkaLAi9-dw9DhhNUzpo9tLL00js3i5hLGqBTJTG41v-J-ld-dJNXeUGiBXFFKjhamHXywIopt32tQoaDG6MCspnqx4X1KbGSaIIeSvo-KizJlZ0AJ0EZgUcxfuLjCe7_miQ_-3R1e7yauCwOez6kg1SKnsR8VIA8ppgk9li8ZqsgOJbswvjAu-A7dXtaoZ1BDfhsLvIfJK9uqKjl1uNmkp50UwT7-Yf-G6lM8dfaLyj3obJf8foTjoI88Nu06rmtG4Wt5rSYNIRLd5OANBzhc3qTtOpxjvVPolO-9Pwxu5AiqfJe3KWiklXPNv2vrIpiDloK4bBUnc1RndGz7xCezc33hK2eEhgx55hHpXaZgDR8ZrbnvX_XkpMHLrxASuPtB2dwG5ZH0FyfAOGpD1cZkYXeIbvi3debudvY6YZ-CqDCiKxRKmDuFL3B2a7Am00hlU-n6lfU53D_Nr2J0pBAv_oZ0os9Cc8IBXRSgJnuEcm3v8gvweAD2TQAYeVBOuNu-re7NqTS_UczU7Jh2q1NBgm1cg1ODn0DlCPvmuS27ZAzTnHZiW5Jf0qzhdfmiv-rjef55u55tO82JbgoUXkcwTJI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇴
استقبال از ادهم‌مخادمه داور اردنی(داور چهارم) فینال جام‌جهانی در بدو ورود به کشورش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101546" target="_blank">📅 12:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101545">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nabo6jYs3Oq-4GYTzu8joVfr-7_6-yabgb10RLiR_yN-8ZaoyQC7iCgpLFSW2i2e0VlygWXQKTFWHi8q4oIQmX-ZiETyaGKQthhY88lHSwOBgdGyxAyhKYYyuti89P74h43dHqmqsp26z6Sh8NnvGdd3L_T2Ei1NXXp8qgYH1D91lMaINsgRvETRHS1_sHSwcnCwG0A3uJsCUK_qXxbgrzmc9lx1Oxgt23N89IOy3Eke-t3z7KxOU5IzFxirf2ibz5t1UjqClcKYde1QdnPazGx1oEQd58t0O9kHPEWdkqBqn2zfJCv2NSBj_E2-IWmdIWILWrei4NkC_D1Zxxtd1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
۶ تیم قطعی صعود کرده به جام‌جهانی ۲۰۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101545" target="_blank">📅 12:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101544">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
💵
پرداخت آسان و سریع با تمامی روش‌های پرداختی
📣
30% فریبت ورزشی برای واریزهای کریپتوباکس (ارز دیجیتال اتوماتیک)
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101544" target="_blank">📅 12:21 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
