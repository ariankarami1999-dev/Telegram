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
<img src="https://cdn5.telesco.pe/file/rd1PQJJYcNCsoz5lOXocl4dAccTnGEqHfpNqOsrkGScXw75XQRQ-O5_BhcZue26wfzTRioG5A3Ry8bnMmsatOGJpACUe-35mBVK6w6Z8mlc6O5ImEGdWfa_YvJ7NdgPp63ekynj7uTDdF3zVFZV5rTQn6qInKlVvkUfOpF4lQhwqnBXfmocbqLijaWSU7KaUzXN3iQkNRLwhEOwf_rU5Jipz2NW56O0khWMmVEFE4Tu09Xx605zDTfgf30bUkB6MXMixt304RBnHaZA67jQz2cXLuGiLLUNb9Kj9MoHzSO2Phuy60Dwf-u7tvZiwxjHAbtgjOrLqjAEsYyD6ELiFig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 487K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 22:11:08</div>
<hr>

<div class="tg-post" id="msg-103019">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09c6195c5.mp4?token=L_Vn8V8511hQUEth6V_p4k7Yx16OvAoxhftaJIXRoarj5PB8cxUwuHPu9s2dm4tZMv-WuPd0fwlvKx37hEHOKocEnmPZXM6gmHmKJMAh59-PiiL_Qtg-iZ-IlalyFJzaUB8p7T2B2zlhMSxzopsTRO0GsSNFe4Aiq9uMpqzSWZa_QZcCgmXNZkDc4VFPzkR0PzLtkvRE7OgnSxFa9058L4C18gayDlrrFPZAEgjcSx-4vui0pgpqkY6_hrRYR0yh2UNqoaCo8OLiEGS_YFJbgGioVOT1Q0o1tIoEsOgKHJ9iBa9n8brlIDgCR4Z28_jwEllaaRfhVTDpTRqDcb2JsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09c6195c5.mp4?token=L_Vn8V8511hQUEth6V_p4k7Yx16OvAoxhftaJIXRoarj5PB8cxUwuHPu9s2dm4tZMv-WuPd0fwlvKx37hEHOKocEnmPZXM6gmHmKJMAh59-PiiL_Qtg-iZ-IlalyFJzaUB8p7T2B2zlhMSxzopsTRO0GsSNFe4Aiq9uMpqzSWZa_QZcCgmXNZkDc4VFPzkR0PzLtkvRE7OgnSxFa9058L4C18gayDlrrFPZAEgjcSx-4vui0pgpqkY6_hrRYR0yh2UNqoaCo8OLiEGS_YFJbgGioVOT1Q0o1tIoEsOgKHJ9iBa9n8brlIDgCR4Z28_jwEllaaRfhVTDpTRqDcb2JsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
جلل‌الخالق؛ اختراع جالب دهه نودی رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/Futball180TV/103019" target="_blank">📅 22:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103018">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">6 شب و 6 برد پشت هم
✅
من به پول هیچکدومتون نیاز ندارم و قرار نیست چیزی بهتون بفروشم  آماری رو رقم زدم که حتی تازه وارد هم میفهمه این آمار کار هرکس نیست
🚀
g16 https://t.me/+5fvta-uF4QA3ZDY0 https://t.me/+5fvta-uF4QA3ZDY0</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/Futball180TV/103018" target="_blank">📅 22:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103017">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ncp17sQ89n-bK_jqVTXn9gSlmGkrz3HmHfv2MfyAZn-xaVU6W3G1Oi0XjPUAlBr2B554RmXKd8sf4ymcNNdC_dImEyysoIB-V1ngpWnrsj7EA4nJcISXYSoGvCnkABRe7lRuB8PCQy6Ftb2xgeplt9-UaCCv2Xg5dYsFH02OoVy8pp2eneKrHxONpViHiE0f7SglDt15oq1TxvVWuOguiY67Qg72SDVfTjo5TM3rIBi6pUxU1GiA_63cudhctJ-6CK_xrFsnIzmnRpGKPsIeiInyp4OnTPbFVpJ6K_gWwFXiJEZpK4sm_1CA2EmyMC4ExNmQWSPpfw05D5FlEALJIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">6 شب و 6 برد پشت هم
✅
من به پول هیچکدومتون نیاز ندارم و قرار نیست چیزی بهتون بفروشم
آماری رو رقم زدم که حتی تازه وارد هم میفهمه این آمار کار هرکس نیست
🚀
g16
https://t.me/+5fvta-uF4QA3ZDY0
https://t.me/+5fvta-uF4QA3ZDY0</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/Futball180TV/103017" target="_blank">📅 22:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103016">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0EqRYZqqwzOoqPr5Ci6lW-otxcneqF7oU-u3jwh9sIJxO6y7IJvUmlUZiYCKCBBN_2sXtYFQTBUHhLP07nRDCxFpGnW2Ov9RO8BNTdPcFX2QlJQuAZLeX-__fRFyFFpbyjzePlMnuF3kscof4JJkBsKnIfZ9bnQj2hwByw4Z-A4HOHOsi-dYPkAWuVpXy6mXQBrk5MYpFvNpA3RaCgJxFIBSKYLv5AFH6kq6KlGoU8eW8yTOfYW29iz8zFfDe9-twZeRcypP-cvXTxL7z7V6Tg1zR4FyMB6Ne6lQakrwWe1GTEuzh415PNo_D4WSSmWETAkLY6dQZ1z-xGfYRP5YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوپینگ با ما چه کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/Futball180TV/103016" target="_blank">📅 22:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103013">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nndNR2eOhx610itFlYMZXkHreP46eHIGRSyx0U7pwQ6ZJH4l_uXxqXdO7yUC9xcs5-eIa_13UGZ60S9zGzYv8ksLfG_kL5kacfxgrk1Nb-5CS2CtKndO_84Y1a-y4SqctFav7Jy69-ukdz8ifBtd5IFvHUwmnb2L0vWOlJ0AoabY9PBkHGZrPeBDc3hzZ9CTjFusjKAodsUSHF3ddUsk3VZHGiWfrc80TBzMRDC6FGl4oiqqrm-GydWU4veGawWmXxTQHe-kxawKkeo5KK15DRNvYuTC0-7QcK_z0du6_dh1hF5CtHZLxXH4v4aTKap_pFNTaVeX9Mk8wl64pn8b7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/utMP8LXUuHuKi1T5Tp58JOMet8Bz8nLHRI-hsW5pHbY8M0WxBe3BQJXV1eDkiS-r3pyww2E9_NSgK2hfqQx3dBl3QwTgdgxtdqBJh6gOItQqWQ6wDzwpPCo-MP7B4yyzaPtXo6O1zADuP1HGbeJa_E9rH0sZzYDNNBRJwoybBSfQ5kCA_c3Ld5YkdQIqc6_qYH1ST1oyoNIOr0KN3XtEBAaWAmLgfBqc0j8z4IMXfBHBWDSZv5-Hi2fRpeZZ592SdeuwoytG5QA5vGs2ocXiq_sJaGDUPDAzZJFmSUBQmp3inVP4EQAYzBUN4l9SddpqCpqmelxmAsgGtlF1MXCBKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzF-NA8ynDHNJ3nKSh98tatDT57mvgI1njE64JabyJnpjZBE7id3Wc48eQnAgD0SIPjaTuEMxs4qKzk58rfQ6yC89B9lvxwPS6kXyI1AAGLdgHlnxCAn5Rfgm22XG5WSN7IoIrXiMjiU628T-ASx3nmZ-GauxissE7OLhxm-OIxQAoKL2Op9WD-UOk5byrzQuxkxKaF6Q5YPPEHT-_2NgJcFu2RbT1-os16cpulCbRp0qu6_0PN26AHxdhcgV34gl-do63pua9mUMaAbP53pw3VO9lBn-bJUc3Casuw6L-_5-dHcSisO6nyqG6Y3xrze_C9ticUCU8InG2HGS9ZPUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚪️
اولین حضور دیومانده تو تمرینات رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/Futball180TV/103013" target="_blank">📅 21:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103012">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcuxpmzIfjOp6lvbP7ARaPV0ZLvrpXaxzKVK7O7QeIw7oVXgFI_3OdhhN2KAFLKqfsIGN3dhIS1J0Kc79eF3mLwCDcqml0gYJBkRT-6b9efCQjDpGUay1doc1sNE67E2GcLuHJuQO8b7lYHWLLqKiA9TO07_sioOyk7SuwMtqDy7d6dIyIWpVF-lj2KJEHeBAvr2pYR9UNMoPqbEbBkSzYoXf7lmcbScC59m2sF8uSyPBEEumkXForzDdbdZiDPEtNULNurhYK8IB7T7JrcoozIb9NBW5Gy-j6NXMwNfGsn3YDILzooMLiqvXkzRb1KMATCjWC_g0q8bjNGOt_kqlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: رولی گلر مارسی با عقد قراردادی دو ساله به سیتی‌پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/103012" target="_blank">📅 20:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103011">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQoIpY9ThSgFgkv4v5rNjIP1jP3OM28mmiZGEYIO0dB5nOEZlfcFgFQ5RH5i_VCYrjEvN-U0UWIXeMpb-pTDoXaDA-LNDhqikeIjRiRIVcHOwsq0O7SIqKqIVKAITZNLA0VPsiEPXnmmlb1z8VYPnckkgKQwIaha-9RRcBi9WhNIKyu67dhPqk8gxzyKB2zRiovJnfnTIKdXUGoVGSYFPuuArKFte9InUOHA0fYpCTMr1AqMjDS-zoGJK0YMlUQKMKpQfsZ55Vwil5b1RnsHn_JOgg1rLrQUwTn7MWHUmsyKJVNBkQUt9_Tls6NSFAgyIxvRYjWCtDesyZltb13_TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
ژائو کانسلو در تمرینات الهلال؛ مذاکرات با بارسا جهت انتقال دائمی به کاتالان‌ها ادامه داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/103011" target="_blank">📅 20:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103010">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVx_E5uaAOpbMPfzQegfvt-cgC4_GA8LZH61amkvPRliG2atGD-uhzTmckXLZW-iOw8B743oMPJUxOVFdQuUzqrOBK-Fa74KhOhEfwIa4xO4-ktbLTsdwWAyMpXdeYYhgA1hfxiqQoUbi6m08xLlPXZvUC425t20vj_0KvwxEXMwTrU1-kQ6fXEBvmn9y2DnOo0hFIqltUC2v9HYpQYqcgHORNLS2ESVzITEgh-i5_8If7mazXxFqGOBeKkosX9LsnqWeODmUFQ6tx1Vani3FCcej7xnd5wZgGokWoBlGnmA2U4UPfDoVVz8I2pBdDIzx6ruLw-6v5zNe6Z7O_BEsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جناب مالدینی بهتره یه تست DNA از پسرت بگیری:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/103010" target="_blank">📅 20:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103009">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwQ32IpzeT6ta27DDOMe1ijUYjJicRA5hoptJ5SE44cLZcsP9Crcs-D01eYDru58aMe-REoxUeMUpO08nLc7j1jKGsbx1mEtnXZpd524cfijg-z_sFQZ_2EUaetFy6xD3sK5e4Cs3rsRRHy_7cMJSYInfIQXAbvJa2dfedqOCvcOKadGgAYcrHxCPgdTegazyM-dLzuePE7q-42rLzmHDD5FhSk4Pp2BRQYtRWTl3-gpqn1VrNAyJaHnbTazrHn1S16I7gIrtRWTSbhw2_fjIaOeR37HAGSznSZw4r_niHC-Zjfap1mDcEYKTh-tdnUIYI9f853Nx6wBUosFu-WJ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚠️
🔵
سهراب بختیاری‌زاده فاز گواردیولا گرفته و تو شرایط کمبود بازیکنی که داره، گفته که اندونگ رو هیچ‌جوره نمیخوام چون جو تیم رو بهم میریزه! از طرفی گفته آدان ۴۰ ساله رو برای نیمکت‌نشینی میخوام و تا نیم‌فصل که پنجره نقل‌وانتقالات بسته‌هست، باید برگرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/103009" target="_blank">📅 20:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103008">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c04a9f891.mp4?token=ET8qXqQmFfEDqw3_dTi6MT_6p8bb7yejT_3aTntiHjoiED5BKGh3bEDrImO0yQF3pAEH4kDT9KpCeTQQnsbfZG0D_9QUV7EkeI7lHiNSCmOnMz8nDH_wrdxruOnENXOG4WHnQMZ5wjdYdAGYnDSMzCU-OPfdpHA0HMoZuTC8jlbEPSomrQX5ZfOFbj-En81rcJSqxa0-NNQjgP3J6_0OgCGer873gsVyegOk-JACSYoLD2aLUb6PewUL0jIOImIOdmIwO0k27QBiIOm3okP3soG6OY2-UIIRvAlejLNdqvmq4guq9dAaC1-f9xGYP79Hi_jtGv3QGwtdU7Ch736TpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c04a9f891.mp4?token=ET8qXqQmFfEDqw3_dTi6MT_6p8bb7yejT_3aTntiHjoiED5BKGh3bEDrImO0yQF3pAEH4kDT9KpCeTQQnsbfZG0D_9QUV7EkeI7lHiNSCmOnMz8nDH_wrdxruOnENXOG4WHnQMZ5wjdYdAGYnDSMzCU-OPfdpHA0HMoZuTC8jlbEPSomrQX5ZfOFbj-En81rcJSqxa0-NNQjgP3J6_0OgCGer873gsVyegOk-JACSYoLD2aLUb6PewUL0jIOImIOdmIwO0k27QBiIOm3okP3soG6OY2-UIIRvAlejLNdqvmq4guq9dAaC1-f9xGYP79Hi_jtGv3QGwtdU7Ch736TpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
پیشنهاد اولیه بارسا برای خرید رودری بسیار پایین از حد انتظار بوده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/103008" target="_blank">📅 19:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103007">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/445575d6e4.mp4?token=EZeIvsRKwWIdCVOMQ6-MnX52yxXn_OLs_vKnaF86uJJkgEZloVvopeYdOh3YkZNLYYl8MIHx8aAYxm2eIlW72ikuH7wkpkSchGFZK3fMOsLH_QOTQyF4QSxhLa2rhvNDYHfl9c2EA22ab9bLhihXkNyYpet4HekQ7qMoyLjjFmP3UYGqpSSUQQQsqx_xy2rBUZx6C6uW7krh-XX1mcZqL88ns7nhLfbFpKbj8N5YnbCKGL4cFxbQee2mWC69zeO00WYeSUpJvD69Q9fFELX87JOmV_vmEWUK_WkHb8S27DvQwR_uGNOTExHPden8NDhVbe5e7yZ0rb_qtkUEwBuLOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/445575d6e4.mp4?token=EZeIvsRKwWIdCVOMQ6-MnX52yxXn_OLs_vKnaF86uJJkgEZloVvopeYdOh3YkZNLYYl8MIHx8aAYxm2eIlW72ikuH7wkpkSchGFZK3fMOsLH_QOTQyF4QSxhLa2rhvNDYHfl9c2EA22ab9bLhihXkNyYpet4HekQ7qMoyLjjFmP3UYGqpSSUQQQsqx_xy2rBUZx6C6uW7krh-XX1mcZqL88ns7nhLfbFpKbj8N5YnbCKGL4cFxbQee2mWC69zeO00WYeSUpJvD69Q9fFELX87JOmV_vmEWUK_WkHb8S27DvQwR_uGNOTExHPden8NDhVbe5e7yZ0rb_qtkUEwBuLOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشق‌و‌نوش لامین‌یامال در ایام تعطیلات در کلمبیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/103007" target="_blank">📅 19:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103006">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSS3CU6yaXOwhHamKAcASjy-r8Rr1iYc0Q5kVY8sV4qWYWdfz7-XvNs3zGXRyNWfrj7q_GRbgtfoLjFCRPtms8lGzFrcijILO33sRB_STXrUX-OEY_ms-MWUlX-1JpmIBcYf4st55Z6WlXR6ttdtU8A9e7Mo-hc6Ri28Gx096DWyCz8L3k0sUPUBQULDQBi2XCere8fVJNlJttl1qoF7IM5SZE7c8pkJMX-EdIUVDLDFWGMRRcRZ-k_Yujw4ADcO6bu0yETVGCJRQHzo_WoA8MX4SirMghovHrzH60Ok_nG25KiL86PN0GD_DFuLiBI30eANH-1h37sYBuj1XbTrnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚠️
دقایقی‌پیش سه‌کشور عربستان، پاکستان و ترکیه پیمان دفاعی سه‌جانبه امضا کردند که شکلی که هر کشوری مورد حمله قرار بگیرد، دو کشور دیگر حق دخالت و حمایت مستقیم را دارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/103006" target="_blank">📅 19:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103005">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpecby5haGTOuMEBnsXdI2oEqPn7utEUgETM8XlTML5TEv5DuHFnTx92s2k3-ozL03uA1lMEYhKeLEtq9fSUMA1CdPRFt2hEVafPsi6YGCFnvClHVZaQXx3MypB36lfnXmo005pmMxK2WSKmvF47m2UTqYxDgVpBWTx3w7CN6VmvyvgZ-45r6_OQ7AQUYrN5VSkZPqqdewUrtMgLbkYDWB8GZqb4Nz3VZl3e5E94lL6N2PglqfHHeG8c-zOezhvpUIEesIKRMb4K7H5fJae84tNgHmNiG5SVYr5Kg_QjGVh5gKWoyLajuOqJWNz3RMrQQwES9_rv5L1z2mCJ2ZKFvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین دریبل ثبت‌شده در فصل‌گذشته اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/103005" target="_blank">📅 19:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103004">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsK72Y-NXfT8ChQ1vfmzrqgAxfg09r9Nh1BVP2BzG_VhHoswGTQcGhtuqhVMzIkXTRxGY2N-Jf9XseyaIXCiDWKpxmsvaYbMWuFksyPZgKm_5LvodNassimLIfVSXa5KwfcgfzrEdUVoLQ1CPO-0N4dLsnEGREMaaaCnyFIKo_txfnycz_Ahn_dXHkmcazb933_ynPL9aFsHKw4KQB4klcAXgBJkqEzrXlXUK4vZBoxPnAhK1R58VV-bkDP9uuGSaFHpAlZhoN-0ER8kJ07tyzxiDNH3k6InxINg-9qRVZo9PFIQtJkqO82H-5qMHjhWfGvk8elC6zboR36ZbsPfag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
خوشحالی بعد از اولین گلت چجوریه ؟
🎙
دیومانده:
به این شکل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/103004" target="_blank">📅 19:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103003">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f1a08e29c.mp4?token=biRpzamYN_Xtrn6AoOwv79uIUDXK1rWiV8Hj4EsZF4tSspgNBJYpEchEa6M-15ar75411_JcKVXhmbUJysFdM3-APbZ93tX_BfnlwXASyvU3ogKmMY9C-TvoNGV9-9taAvt3Ol0hrZAH6Ud4XSakzX3XsJmBPl0QiIbphmQLPhAXt3ozN0sDrKcCLdzW9xPmwbcRbZm_PfvLNGn04Z7KhuoxS7_m_5LR78N9MHOQUmzk3NxsnW5HHxGK4ioeqsff07XYys7FgchQA5_03sKBspQ7L14xHM2jUx-xz_shWGGuVDBg_Ggn2hMfC8X5JssgrXwo-E2DhFADGL5o0zv3wQTE2zEo2hsWtdKcQ8uoN5xlYKNHOvxmvzkTKYIxgYTc9KxAy8t5p0hoK4L7LulpoQD7vj-d0Itgjm7LFxUexnYsFvzQiSYHVVozIYJobXU_MWPMeIvZ0ljlllRveiv2PeFiz8f8iPnIN0NWzyCmItn0PGv29KyOTlbzrX0ar-5G9gGi1xxAamcn5k6z2QqF5RNH3PJqnZzGLuWYt8-PxGSclnL1K-JP3xGCJVD-hNYoei2AdX6Y90DjYem1KqPl8v9rcMDSmww9TohvFmPbqQxECl1fCYdvFhmeTYezP52O2T2NoN_0uKUIs6lMaA8ZSqDrtY1_rhdSZHasBfGqGxk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f1a08e29c.mp4?token=biRpzamYN_Xtrn6AoOwv79uIUDXK1rWiV8Hj4EsZF4tSspgNBJYpEchEa6M-15ar75411_JcKVXhmbUJysFdM3-APbZ93tX_BfnlwXASyvU3ogKmMY9C-TvoNGV9-9taAvt3Ol0hrZAH6Ud4XSakzX3XsJmBPl0QiIbphmQLPhAXt3ozN0sDrKcCLdzW9xPmwbcRbZm_PfvLNGn04Z7KhuoxS7_m_5LR78N9MHOQUmzk3NxsnW5HHxGK4ioeqsff07XYys7FgchQA5_03sKBspQ7L14xHM2jUx-xz_shWGGuVDBg_Ggn2hMfC8X5JssgrXwo-E2DhFADGL5o0zv3wQTE2zEo2hsWtdKcQ8uoN5xlYKNHOvxmvzkTKYIxgYTc9KxAy8t5p0hoK4L7LulpoQD7vj-d0Itgjm7LFxUexnYsFvzQiSYHVVozIYJobXU_MWPMeIvZ0ljlllRveiv2PeFiz8f8iPnIN0NWzyCmItn0PGv29KyOTlbzrX0ar-5G9gGi1xxAamcn5k6z2QqF5RNH3PJqnZzGLuWYt8-PxGSclnL1K-JP3xGCJVD-hNYoei2AdX6Y90DjYem1KqPl8v9rcMDSmww9TohvFmPbqQxECl1fCYdvFhmeTYezP52O2T2NoN_0uKUIs6lMaA8ZSqDrtY1_rhdSZHasBfGqGxk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
صحبت‌های روز گذشته پدر زنده‌یاد مسعود ذات‌پرور بر سر مزار این قهرمان و اسطوره ملی و میهنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/103003" target="_blank">📅 18:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103002">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1cf973482.mp4?token=Y_d2ls-InIgCKj6D2Zptc62h4qoPyPFzzSLJWNVpoQMmIFu0IEJAxuxs_nlwEbFMj56N1tAEyce0g_nQ8XGAIWNxTfPtZJMCdsYpJ-ir_iVQy4twG5TPo7vy-Q7_dZOceIxoF52yF4gjhg2UjL9npp0C69agrtOS4NeMthUk4Y2BtqfilKksXuw-iAzwYjAfkjhsZb93-l73LSaDq2MTbwGSpfSEHcL95XAgGda-_4GkgB3tbsPKr0lqVLwtULNAlGIWkx4LYooZFxmIoSX8TTZ7H7O7qEfDpPl0UBbUTGeXFI3a1fopmh0C1vge9DFAohzPEIDeYTwrA0Sybbf5xCbFl9yyGo0N7IcXxZut6xrWwCMwa4WLj-i7vNPDGjlnvfM7J9sA4fYVYp_7_sh3Pdsf2AGJz8CttOJz4-u7cXP80g71ZPg2D3p5b814J6u2u-mGoF1Lt5bEAu2R1rwQXu8Wodwc0S3DVqkX17-dk3hKKxSlla_atM9OLSnfNsB7tqQnB4pbVseGPFAFj9tK6xH-f6XDiK1-v0dzgknZZZ-H2HelxhkffscNCg8qROkwpqBVZFxX8VrZ94bbP3_zbYqSgIN7YfgBgYeIpxCwhi-ZGoOtu5MKZHVKXPMDH-FznizEkW6DyKg328N_0Vx06R-QovUjgGc-QWL28T6vTVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1cf973482.mp4?token=Y_d2ls-InIgCKj6D2Zptc62h4qoPyPFzzSLJWNVpoQMmIFu0IEJAxuxs_nlwEbFMj56N1tAEyce0g_nQ8XGAIWNxTfPtZJMCdsYpJ-ir_iVQy4twG5TPo7vy-Q7_dZOceIxoF52yF4gjhg2UjL9npp0C69agrtOS4NeMthUk4Y2BtqfilKksXuw-iAzwYjAfkjhsZb93-l73LSaDq2MTbwGSpfSEHcL95XAgGda-_4GkgB3tbsPKr0lqVLwtULNAlGIWkx4LYooZFxmIoSX8TTZ7H7O7qEfDpPl0UBbUTGeXFI3a1fopmh0C1vge9DFAohzPEIDeYTwrA0Sybbf5xCbFl9yyGo0N7IcXxZut6xrWwCMwa4WLj-i7vNPDGjlnvfM7J9sA4fYVYp_7_sh3Pdsf2AGJz8CttOJz4-u7cXP80g71ZPg2D3p5b814J6u2u-mGoF1Lt5bEAu2R1rwQXu8Wodwc0S3DVqkX17-dk3hKKxSlla_atM9OLSnfNsB7tqQnB4pbVseGPFAFj9tK6xH-f6XDiK1-v0dzgknZZZ-H2HelxhkffscNCg8qROkwpqBVZFxX8VrZ94bbP3_zbYqSgIN7YfgBgYeIpxCwhi-ZGoOtu5MKZHVKXPMDH-FznizEkW6DyKg328N_0Vx06R-QovUjgGc-QWL28T6vTVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
تو مسابقه مردان آهنین دیشب نزدیک بود دوتا بازیکن با همدیگه سر یه چیز کسشر دعواشون بشه که بخیر گذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/103002" target="_blank">📅 18:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102999">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GL0Hd3gOoXxIp3ZKnA2YB1nYPufECzG5KkJOMkT77AyAnbt2LKUYKNz-RiKQaNXhWJTPBJPOqNjojeEwZTMmvSfKjnMYnRhiRP2vE6d2UWmBVdizGKbg-xgKkbJMdgrOHRt2KGLTE52FYQ6t_v-RntBqpihogr1b_MS7nBFl05RA386306Ze-h0UHZv8OvYqJFWPXLMDqKEKatt1cx2XZn3NVKcVVs8fLme9CUnOp7jtWDM9eRGIX7qah44DEVHzIOS2VMwgwcYhSlZlFFZuKVOYTlZ_P-Ylo-ljhkvyMbKHtByLVJrQmXdbal7LtjneGyPnGSJAd4SjRYS8fpjjXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oWSe-wPZ6xXjy6P0wuKKaYiCdanBA0IAFkwB0QeliMTcIMDYHvxrz6yTDtac3gB6akI6Hs3KXLQzt7ZUQVoOT4eQBybuGnDcxf4YRJRUvp1uMjD0JS1WZEA_Z8WZdQmd7LbUqZYf-Y6OFQcmODxUH_AP_2SiIFOybYLSexnaWJUrGwx7sjr9wdKRf0yYeT_Tt0rOmyPMe20e9mddg5-Ft57cw2T6nu_FQ1XgZd_mucP9pyNQfbTPfxI7Irck4RM9vZNNjInkCLS9ckMAaGNBUYXIItTgep8Wt5W0fWYsb2ytWRq-HtjBt23ts542x_ziWLDDL3b3kUDJC3i9JPu7GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WMB3KisPyQu8xYIlf0mMKRyY8kR0fytcyAZiF8wdMgzB-_EeFdod2Hd8QSJLymwLSiHwEou7vrRnfQEaQtghitaUM10b8GIceOBp47IQOdd7SquimSEpoXvtJRikAOg1NFB0-fyJ53KmuD4oAm24pjCH8IwhnPB_3SC1TVC0PJ_XD264S-sttYREa5EPyvJsVYzL_72ZLZd3HxDyjhtR8L-NQghOKpbb3q-4uP6grfOkIG3XHK6-y-DZ8BdsNa8UTYLwtFVVOHynFkuPLoKoYRoxWx02OPbIxCnzMuzKdZDEwi4GX4nYojXw53sdpPxIMysIGSWZQmRqWPVB7RWVoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فران تورس لاشی که چند وقته میگن گی هست برای اینکه خودشو ثابت کنه اکس ژائو فلیکس هم تیمی سابقش رو فالو کرده و پستاشو لایک میکنه. جالبه بدونید طرف سه بار به فلیکس خیانت کرد
‼️
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/102999" target="_blank">📅 18:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102996">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mBgapaOaGtG1eM8UOKUMmaZFINBXxnuV3c7ipx0u5oVHFHIFriD_J4XaOgt2CX3d0O3RJ-9hW0FNbAX3h9I3dOqvjCUadE5pivtOQrBFNr3GtauUG4eXmziIHW6lvavtGmF6wPGjHPLOhioOIik9ZgUd7kvEswSLhXzigybDXBIoHrIi4r-VxpJOZtrgIT984zHYtsRKQq23h3WT57LfPUdyoocD7871FkN2r3NPX2pUIzBn57CUNGZLTC2bZFvthv_FiuKY3dKkG0A3ktMyRaXCEIFHXrBGHu2VCdNYT8QGzYTSGBighL0KjFYjGBCS8y1NtFlAVcKFIUjQjeaPOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/byG-6E_DjEx782N_P4gxbgRpNpPQelw4-KNo-HJ8qYS4dG1u5tmsCZkS0bqJCvCiNZBjvWEoNYb7xnN0iRuzyzPWXqpd0R26SpSl72eRcHxKzpqZwd2eTSTJB6kmfpSMNb3sWDS40rFHyu4Fux4dVcsp0QjL890Ne81Yq4fUdj7eVykzPafcPfXYyKyjQEooJYjCgiqlO2pZRXdFxa9zJR4EEuMskZFfrp7GHRTNYMQDImaC1PONZQLkUbZF2tupHMhlA1J12cMVC2kBQlerUW0eIWvnzYxJ4ieJLO3NyHrN1WakkGIQOfIeD43wz5emMeNEYP-T_EbSYUpxQ1SVTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WvKSyds0qk3afQchL5rG7EUTZ0CTC1YT7Fb9jTTrb6fG3JZaSb4SHaOsFwlmi6rhJkbnh4AoxqGNLIE6bbNZA5j1ovxbRxCyLGnS4UILHWb9uuMUhs9JVJT_GAsxGuzsAewDi885wcTd225G38E_j73i65ZHfkFiZ_KKoEwyaVo1HYnIFZ7T3RR4JKCdIPpnIW8A3PgtBAs9k6KvvO-byqF1FJyzxEB2PJ1uTu5g1RohY9hRKqBQhfN909V4Bm3poxZ3Uw9iX65Xw0TCjUxSfPGbqK2LOzZnCUfmMVSxnDeGfxUy5klMpU7iqXIvxwKtbyppl3M37aD7Rs8F9aAkow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فران تورس لاشی که چند وقته میگن گی هست برای اینکه خودشو ثابت کنه اکس ژائو فلیکس هم تیمی سابقش رو فالو کرده و پستاشو لایک میکنه. جالبه بدونید طرف سه بار به فلیکس خیانت کرد
‼️
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102996" target="_blank">📅 18:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102995">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q3QFHfBb23W3o_29-pcBnN1XEOnGSUDqU2Gfbzp1nsaOBteN3NLhNj-oREUOLt-WeTbcF-yMaz0yPPRhw4Pt3GwCGGJRFGhh-a6zX6nOXXUtvOTwWUW4B3QyzZfPYRrVD56b_R7OgVJm2paIA5IERTulnVOrcJfuFJ_JkjZZ_aEQyr0Jf89R9oJF4M_UY70HDiiJaqObZsEQYaJSDM_9f0O4ASIsI9DEl2ThaVTPtxJhgOQ5XZhDUq2eHPjtWnhF2WBlGjHNA4pQ8PyCucDNYmjszYbYSggxNcdSOZ0gFzKsLXQ552YfhIS0iyK_Fsa7cnTmTeWLpw8H5B4D1HTJeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیومانده در تست های پزشکی رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102995" target="_blank">📅 18:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102994">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇪🇸
❌
#فوووووری
از رومانو: رونی باردغجی‌ بازیکن جوان بارسلونا که در فصل‌گذشته معمولا ذخیره لامین‌یامال بود، به صورت قرضی از کاتالان‌ها جدا خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102994" target="_blank">📅 17:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102993">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOwpflDIYXSiIAczLWOqj0V3lUrYDpnIeLdT_0E2m-7BG5gVPd4_YOy0A2evpK_Rdw2fxtI-uOZXi69wWbCRN1qw2LeL6oj4Xr8AUlU-LB60Kv4CVuJ7nOzUV2gpNr6jyAKt4g3uxd0B41iMVR87MvQa1hXdYUf3bTpdsnGfHr18jkNZPbWQgYOTuTszCDC9hblg8SQBSY0T2bqtbGuJPiIYH0EJgxan5aCEKhUr94dEwWbXtzM4BkYTzKFLCmyazlj0P8KNd61LBCbohnSL3ZbVonUtfkFw8IbwAos21Y_6SQzR5Phgp1h5LzH5GsHCpOfUc2aI2Gp0gECB8qpU1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔥
🔥
🔥
✅
بنظر باید تا اواخر امشب شاهد خبر HERE WE GO رودری باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102993" target="_blank">📅 17:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102992">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txei8WbWxE2RDmmzJ7UfdIKj60PdyzicHmXVPs1pzYIAhBJGtS2eQcYA9yglA7WUlvfM0nosk3y9itIO31L_fGqr7XJSZKDaMInWq3sgVHlBZHb6Gu5q_4BvkiV2PXQr25mG7z6aSxos2m7tYW5DaoiQyfzBcglFVRMVL534DSo-MmqEL5grq2xmp_icsJGVsH2KwQYGeVYLxt3dQm0UJXAfaVbzK6qTtFkB42i7yvzceMh60mQeHIe-zBavrk6WQbk3tCcisDS2qfHTk8499wvPe0QpBX2anVEO9xPPTzCZeZZ9rXLvvAXm2g4sJZO0rHrtq-83Ul7uNMkU66WadQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔥
#فوووووری
#تکمیلی
از RAC1:
🔻
رودری روز ۱۲ آگوست(چهارشنبه) زیر نظر هانسی‌فلیک تمرین خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102992" target="_blank">📅 17:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102991">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
از RAC1: رودری با مبلغ ۵۰ میلیون یورو به بارسلونا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102991" target="_blank">📅 17:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102990">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb0d57e90.mp4?token=k_NPgWEjrIyVb7leHviwiR5l5wnsXcxCghNyhf1e62YtuiaY3-8yJ3RW8a4arzhQKvgsq2pPxM8HjC5pOxqMFygCuU6BJLavv0yU3srr9FbYAg04UMawGyoX_Z7CmkGo6tGFYhf0G4Gl17xDndwZ5njBg3_3JG7qrnEPINzbpl5kdaQJXfrr-L5Ji9E5PLPiFIrVXOIyl6KfkEbeguMj7BpEGzj-wyExap-JWrEZKsPSW9SLHeQI2hUWnDeZNjFvxbR44m9z9uFxi3zAnif80j9uJDX4QpX5umNuUQtEXJTKRoa0xYaiy4KF_TkSlLicd78HuoD9t92tjseB_DGGDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb0d57e90.mp4?token=k_NPgWEjrIyVb7leHviwiR5l5wnsXcxCghNyhf1e62YtuiaY3-8yJ3RW8a4arzhQKvgsq2pPxM8HjC5pOxqMFygCuU6BJLavv0yU3srr9FbYAg04UMawGyoX_Z7CmkGo6tGFYhf0G4Gl17xDndwZ5njBg3_3JG7qrnEPINzbpl5kdaQJXfrr-L5Ji9E5PLPiFIrVXOIyl6KfkEbeguMj7BpEGzj-wyExap-JWrEZKsPSW9SLHeQI2hUWnDeZNjFvxbR44m9z9uFxi3zAnif80j9uJDX4QpX5umNuUQtEXJTKRoa0xYaiy4KF_TkSlLicd78HuoD9t92tjseB_DGGDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادارای رئال: اون دو هفته ای که ما با رودری به توافق رسیده بودیم و وینی هم تو راه آرسنال بود
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102990" target="_blank">📅 17:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102989">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d4f569888.mp4?token=jSumUgipvAtA3njLdI3murKirOY1SuEcUvvvmteSUXYOBOiLWaRA25tdVsweUaNzCEm6iYyc0LuZnnAWqCOoBOekJqOkP_5OCMvu4i_3ynP_Mx4J8evX-r7yO8VHC2iAZtQSvGPYQZ2H3H777MqMRpRsZ9FNp-QiQxHjLrp31Hmf64S95J10-k3E31KxWJe1u4jmjdZdaBOiND26Dxk5CRhrMqUKP0uAAHOMNhBkNqi6nub89iOOaqvX8HyXwwaM4Rz2h-XPwVwxMY76HA1cFbJUU21Mk0AkNtnhjC1BDmbL3R1ImYS56jvzAq3UpSGh3epV4LWEjPKjelbJT5Jw3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d4f569888.mp4?token=jSumUgipvAtA3njLdI3murKirOY1SuEcUvvvmteSUXYOBOiLWaRA25tdVsweUaNzCEm6iYyc0LuZnnAWqCOoBOekJqOkP_5OCMvu4i_3ynP_Mx4J8evX-r7yO8VHC2iAZtQSvGPYQZ2H3H777MqMRpRsZ9FNp-QiQxHjLrp31Hmf64S95J10-k3E31KxWJe1u4jmjdZdaBOiND26Dxk5CRhrMqUKP0uAAHOMNhBkNqi6nub89iOOaqvX8HyXwwaM4Rz2h-XPwVwxMY76HA1cFbJUU21Mk0AkNtnhjC1BDmbL3R1ImYS56jvzAq3UpSGh3epV4LWEjPKjelbJT5Jw3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
مسابقه مردان آهنین و فرامرز خودنگاه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102989" target="_blank">📅 17:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102988">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwlG3VCsMAu5m88ubns_MEi8UBW80xcvNu7kEh3tBx5iagZ2iowGUFM3ceXaUjDgxzVSJrzHEEWaXfqvc3emLUKia2Fv0uxtugbokORIXRTnIGV-Tdsv8aBkX6i6SreblizdEFSpwoe9wzsjAYmfQBOglexgvApw9YHeBJAe2n43-iWygQY67w8sEO5eXVEvs9O_BYX8PyOuhCDFvG_PRSkJavZQMk1QAvCuZmmgMgSg6BoemA3zJYsDkfBiUEnPDCwL985WObs2Ch076Ty0rYBD1zsQXhowwU5dPhUnGA1iuqXu7GLwEnOY8771YvQ8M8VtS-XukmFSs3WVF5nY5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🎙
اورنشتین: بارسا پیشنهاد ۴۵ میلیون یورویی برای خرید رودری ارائه داده؛ درخواست سیتی برای رودری ۸۰ میلیون یوروئه.
📰
رومانو: بارسا حاضر به بیشتر کردن مبلغ پیشنهادی خودشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102988" target="_blank">📅 16:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102987">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af1dce844.mp4?token=T_8QwxpFQz5bMnY60GOdVbDXuMDC2smyumxkiKbsHg9EdWU4Xa9K-32nfkQVjNQqciO9BP1CDIg9S-WbOUpXUSSyMottQ0T5zh2f8m-NJMJF8IBXgBmHZX-WdjTxdCyMdW3q-ZVl2VadZEeiqPhAa8z3KW_G-4sW6yP_mPFvUYZ_OCSmKtz4EZc8xHnH2SqH3ovr6J6rPU9d47qpcOnH8zays0nZ8zQe3FZrgRS8qib9JSpheBh6n9b_ebg6zkTwVaDq768Va_5sdtAxadnqlJmDkSKEWvX5swb7a2RDh2Wh2oQqbN7RpaaxkIMBr9uAqJALFUAOU-PZJ7Pj3-hTnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af1dce844.mp4?token=T_8QwxpFQz5bMnY60GOdVbDXuMDC2smyumxkiKbsHg9EdWU4Xa9K-32nfkQVjNQqciO9BP1CDIg9S-WbOUpXUSSyMottQ0T5zh2f8m-NJMJF8IBXgBmHZX-WdjTxdCyMdW3q-ZVl2VadZEeiqPhAa8z3KW_G-4sW6yP_mPFvUYZ_OCSmKtz4EZc8xHnH2SqH3ovr6J6rPU9d47qpcOnH8zays0nZ8zQe3FZrgRS8qib9JSpheBh6n9b_ebg6zkTwVaDq768Va_5sdtAxadnqlJmDkSKEWvX5swb7a2RDh2Wh2oQqbN7RpaaxkIMBr9uAqJALFUAOU-PZJ7Pj3-hTnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثرات گرما روی رفتار مردم
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102987" target="_blank">📅 16:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102986">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f76aa6acf7.mp4?token=HtDj0fPbrSkOpckrIIJh5evjnKu4rsAssetTmAjFnfkB7q1vlRZamQEN22TUqC2BNhl_NhhvTWa7MDITyOtLAoOy6vnmSPrlT5X9tm0qlEcV1_X6rvxMCu7RsoEDKFEFbip1LqHy3bMcwQ7nrL49aP_WoMDxRFbFBE0h3Rj_4IbQFQbI8FXYb99EsrJWiNYYFrl-d-3P74rtSieJ7aJrl73kmIWbF6gA5dzXIMdxJk-uGlmKmSF1FFM5gyZMpWrqajRkNo017h8q6Q3aVIRIdbPPMEFVaEjrmPBhGLqZQY6mmrsbN61m7epO1dzqh0hvDGSXSQ9LCpLgSqwfUT64qK5fgMYiEitsIO3v3pr-k7a3Exo1zlbfLle_wi5FfK8Hj7QsjLdAj0gJO4RbVksYhpxbimOoFuZDewIKC-zfVzj-OARWlf5pgqMniiyEPmLbAyvGc_Sqh5a3cZ7EbQOwqR3BCUcEft-a7GGvp5odbn3BDerVncgponUv2keHpFE2HFTzB0bf7GeoEkBrDN8-VNw8ZBD8vZtst2xw4k-UChjslk0v3sPwCxRW5BkjPNoKPwc-LSaDR4V5y7MNeW2ZrCowqTo4OVHTladraOYSLSkz64xc2ynIyQ_17karbnvyaGcEbFX1sJORbbsfJ3fbxmyD6kVgZ6L19NZIjzEUn1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f76aa6acf7.mp4?token=HtDj0fPbrSkOpckrIIJh5evjnKu4rsAssetTmAjFnfkB7q1vlRZamQEN22TUqC2BNhl_NhhvTWa7MDITyOtLAoOy6vnmSPrlT5X9tm0qlEcV1_X6rvxMCu7RsoEDKFEFbip1LqHy3bMcwQ7nrL49aP_WoMDxRFbFBE0h3Rj_4IbQFQbI8FXYb99EsrJWiNYYFrl-d-3P74rtSieJ7aJrl73kmIWbF6gA5dzXIMdxJk-uGlmKmSF1FFM5gyZMpWrqajRkNo017h8q6Q3aVIRIdbPPMEFVaEjrmPBhGLqZQY6mmrsbN61m7epO1dzqh0hvDGSXSQ9LCpLgSqwfUT64qK5fgMYiEitsIO3v3pr-k7a3Exo1zlbfLle_wi5FfK8Hj7QsjLdAj0gJO4RbVksYhpxbimOoFuZDewIKC-zfVzj-OARWlf5pgqMniiyEPmLbAyvGc_Sqh5a3cZ7EbQOwqR3BCUcEft-a7GGvp5odbn3BDerVncgponUv2keHpFE2HFTzB0bf7GeoEkBrDN8-VNw8ZBD8vZtst2xw4k-UChjslk0v3sPwCxRW5BkjPNoKPwc-LSaDR4V5y7MNeW2ZrCowqTo4OVHTladraOYSLSkz64xc2ynIyQ_17karbnvyaGcEbFX1sJORbbsfJ3fbxmyD6kVgZ6L19NZIjzEUn1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
وقتی صحبت از خایه میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102986" target="_blank">📅 16:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102985">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/283f5eb6fd.mp4?token=smX2TLoj01e-0CKypcVrYh3WYv1j0gN3ShsCCVw44mEXjamVoicWHaIseWo5gXRudjKAPZQFnOUPB1XbgqjgeswOhsFty_MEDgry8bTqEtR8jBbi_H61Xxfvw1ii2ZN2jFIc8e2pIVoKhIXpytb5GimHO3TzgCeK4EWhlA9I-mx5BrAUKBsgymTYPJyv1w2iW-4zcqq3sRzbtSxrHF5qZ4cElck5P0hOO0SJpGI6SuV09cjWeMmEGwFTU5xP4ufz-o6j1wRcLRrPDcM1V4gk92V5ss2FT0cL9AmgukL50gTTHAJCe1IO_gJAf-cwqS8AyOGqQQSfL5JxjoDGt1E5aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/283f5eb6fd.mp4?token=smX2TLoj01e-0CKypcVrYh3WYv1j0gN3ShsCCVw44mEXjamVoicWHaIseWo5gXRudjKAPZQFnOUPB1XbgqjgeswOhsFty_MEDgry8bTqEtR8jBbi_H61Xxfvw1ii2ZN2jFIc8e2pIVoKhIXpytb5GimHO3TzgCeK4EWhlA9I-mx5BrAUKBsgymTYPJyv1w2iW-4zcqq3sRzbtSxrHF5qZ4cElck5P0hOO0SJpGI6SuV09cjWeMmEGwFTU5xP4ufz-o6j1wRcLRrPDcM1V4gk92V5ss2FT0cL9AmgukL50gTTHAJCe1IO_gJAf-cwqS8AyOGqQQSfL5JxjoDGt1E5aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
گذاشت همه چیو رونالدو انتخاب کنه
#احترام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102985" target="_blank">📅 16:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102984">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQvWhnqjR__0thO0ti9NPHn3Txewzff9xJwIaT1LTcyfXLezaGqvhPha42vRYxXh9g9OyMjZ6qgZYPFF0nr04hxMJCqxN-tPJmk5ZKpJNlWsLfOztnejjmJSC06f5F9G3kQePC1I67vZB3VcVWTNOotBGwxYl4wmt-aE1ZraObiyu6OCShhnk0AYfh4qtM_AcsuyHbxXtw5tRvYKMj-WsEJ4c5mdgJCo69M8VqyRKlgg7v3pQZZv2LJgTJvPyNH77k9E8g5alWn_qbcUkQrTSoySxBI5PuZUaQbdbjVQki5TGS_yo6mm4m5pgTy39nqVci5JJPnlz3_9z0C_YLhLMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فابریزیو رومانو:
منچسترسیتی به توافق با لیل بر سر ایوب بوعدی نزدیک شده است.
این معامله در حال نهایی شدن است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102984" target="_blank">📅 15:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102983">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d314b187ae.mp4?token=AgUQJkZ44AZJw7dQwtJoRHzK_M-OJUNT8yuWCLgK6XAPp4zrhSiWmudkbxg0hBKe-mIQi1m37IS8QKzFdBdJf2uooIkRhUHVTzAzkhdbUQnc8xvEi7KWSd_Xq8N9jeX_NlPBu6ohU2sQFp9TNZmga08WRdpwxOFOfKGgKJTXgTUnPDLNo43GGK8DcKZxxgYxo193wtRwTxjVnctJ3pyijPQwNidNRtPzn4ViIshPN1rNmlwpyJ7ldgFpJNlYhLlgt4AD1gxdc3R0n3hNb0piajrGk5uC7snmOvMWO6u0e1yQV_9d7j6SdgLFgIJSl-ME2aHEI9J_sVSd4mcdSVl0kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d314b187ae.mp4?token=AgUQJkZ44AZJw7dQwtJoRHzK_M-OJUNT8yuWCLgK6XAPp4zrhSiWmudkbxg0hBKe-mIQi1m37IS8QKzFdBdJf2uooIkRhUHVTzAzkhdbUQnc8xvEi7KWSd_Xq8N9jeX_NlPBu6ohU2sQFp9TNZmga08WRdpwxOFOfKGgKJTXgTUnPDLNo43GGK8DcKZxxgYxo193wtRwTxjVnctJ3pyijPQwNidNRtPzn4ViIshPN1rNmlwpyJ7ldgFpJNlYhLlgt4AD1gxdc3R0n3hNb0piajrGk5uC7snmOvMWO6u0e1yQV_9d7j6SdgLFgIJSl-ME2aHEI9J_sVSd4mcdSVl0kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسابقات جذاب دو امدادی المپیک ۲۰۱۲ با قهرمانی کشور جامائیکا و رهبری اوسین‌بولت افسانه‌ای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102983" target="_blank">📅 15:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102982">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dced5ae01f.mp4?token=uFGxgI5IpeBD35ZGcmjJmoZc6z07pgqArtuWLLpCGqeXMkmD53XhgPPMKYgRCuiN_Q18sciGktz6pR2Txg3A3OE6VQQ58gSyydshyswd4LZsDk5kq2hgF75hcEstLe9Lsoze_qbmeopEoVxYHme_46oNDY7UZbiugYChmAE1lYTVCqoFZYYO_dMi0rDU0NBVfiUQGTvlc9GVmYlduMddfCCwL2b23IRhbEzAV91TbxRJVeA8hfXJz6rUqWgbLj7seBU4VKGoGfthsAAyyOjEQDg2ocQbjE3aeAm0Cd2uM3xVDw9cxoXiFO5gNJR7RJraLQZ5dK2k-CImyQb42DYRTrxu4qenVvPxSmGqYSIXG0JIaY1QtaJcwJhF6S-4oWLrfaJLHXsiHZqmHOcxH2JJeO2kIzaOCCdkuHjfMMUZMrWZjJofTXhOaxH3Cka8hq-_L6nx6uvuRL6uyibI65UuOAiLBL-NTqt3xOa9_S67o5131s2B-BbPP0Kkzok_6pA9r-1Mm_tp1KwEri6qpJ2UkW26EkgcUCA4WHZw0uaLRTw2Z7JUWubajOFR_2yxiOmsD5c28kakERUy90nfJjZixOBEmfUjeoHC6xwOh7JF1Z66wge54VJGEL_CW-QLnYEYSdprrelgAgPeopZharmFmk8PVAxHlzzcpgyHR6_GudI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dced5ae01f.mp4?token=uFGxgI5IpeBD35ZGcmjJmoZc6z07pgqArtuWLLpCGqeXMkmD53XhgPPMKYgRCuiN_Q18sciGktz6pR2Txg3A3OE6VQQ58gSyydshyswd4LZsDk5kq2hgF75hcEstLe9Lsoze_qbmeopEoVxYHme_46oNDY7UZbiugYChmAE1lYTVCqoFZYYO_dMi0rDU0NBVfiUQGTvlc9GVmYlduMddfCCwL2b23IRhbEzAV91TbxRJVeA8hfXJz6rUqWgbLj7seBU4VKGoGfthsAAyyOjEQDg2ocQbjE3aeAm0Cd2uM3xVDw9cxoXiFO5gNJR7RJraLQZ5dK2k-CImyQb42DYRTrxu4qenVvPxSmGqYSIXG0JIaY1QtaJcwJhF6S-4oWLrfaJLHXsiHZqmHOcxH2JJeO2kIzaOCCdkuHjfMMUZMrWZjJofTXhOaxH3Cka8hq-_L6nx6uvuRL6uyibI65UuOAiLBL-NTqt3xOa9_S67o5131s2B-BbPP0Kkzok_6pA9r-1Mm_tp1KwEri6qpJ2UkW26EkgcUCA4WHZw0uaLRTw2Z7JUWubajOFR_2yxiOmsD5c28kakERUy90nfJjZixOBEmfUjeoHC6xwOh7JF1Z66wge54VJGEL_CW-QLnYEYSdprrelgAgPeopZharmFmk8PVAxHlzzcpgyHR6_GudI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
روایت سبزی‌فروش اوکراینی از حمله پهپاد روسی که جون سالم به در برده!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102982" target="_blank">📅 15:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102981">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a246a820de.mp4?token=gb1BUSu2CpKgTt0b1Q4sRmVQBe0JVb2pM5kpxiRKlWNVSBZQZbe-2mMoKRvkD4beuGhjrpY7CEnsq2GzERS9Yh4u328tx6LI7SFeVoElL2RFAr5hUaIInRAeCiUmPwoeBLDV9y8q4Id4Pg4qwO5ubZdJcDL-sx05_IY9cZ7tEHfZ2nNsVVirEsWEvBn4EytQbO8gOttrN01oyfUgLFwFMEkNipsPxchlXQed0-pBxIqV_6NAIrC45JH85CDAqIU6F9bqgPzdsf6HUxC3gTOCCpzymoCP89H9nGY-cRezPUxiLj_DVGwNDpYGparvyu_5MB8TNHxUi3ZK5TcEIL-YhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a246a820de.mp4?token=gb1BUSu2CpKgTt0b1Q4sRmVQBe0JVb2pM5kpxiRKlWNVSBZQZbe-2mMoKRvkD4beuGhjrpY7CEnsq2GzERS9Yh4u328tx6LI7SFeVoElL2RFAr5hUaIInRAeCiUmPwoeBLDV9y8q4Id4Pg4qwO5ubZdJcDL-sx05_IY9cZ7tEHfZ2nNsVVirEsWEvBn4EytQbO8gOttrN01oyfUgLFwFMEkNipsPxchlXQed0-pBxIqV_6NAIrC45JH85CDAqIU6F9bqgPzdsf6HUxC3gTOCCpzymoCP89H9nGY-cRezPUxiLj_DVGwNDpYGparvyu_5MB8TNHxUi3ZK5TcEIL-YhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇹🇷
جو پشم‌ریزون در مراسم معارفه محمد صلاح در ترکیه؛ کشور‌های همسایه ما دارن تو آرزوهای ایرانی زندگی میکنن...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102981" target="_blank">📅 14:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102980">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892883543d.mp4?token=hDuqdjNlQ_W-6LIfN57UBEvSbQ-X4L4tHoQgezKDH3o0FtXrXQg2ibiB6euSD_8DugQboq0iL78cNmXlyreZuvcXGnfulFXFeub0ABZ_-jvwt6GrmnSV44Y3VKzfcd4LAro0NEfEg1r4hMTeGEk4ouTe3DiW-g4uZxNKRXXnSd8w3lsamQYxgsR5uu4jvn8fGbEGrqhr1a5foKoWdECSzyMSWo0XGDnRhdXzGb9FRaUIoJv73OyFy893LKZqqPBgaYsWFmpDYKk0FMQ-9s0cK_ZpcL4Bt3APAkxpz5n6veyxjZAOkuLZz3qwo1doqzZW9456MpPP3TycOjeceNtiq4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892883543d.mp4?token=hDuqdjNlQ_W-6LIfN57UBEvSbQ-X4L4tHoQgezKDH3o0FtXrXQg2ibiB6euSD_8DugQboq0iL78cNmXlyreZuvcXGnfulFXFeub0ABZ_-jvwt6GrmnSV44Y3VKzfcd4LAro0NEfEg1r4hMTeGEk4ouTe3DiW-g4uZxNKRXXnSd8w3lsamQYxgsR5uu4jvn8fGbEGrqhr1a5foKoWdECSzyMSWo0XGDnRhdXzGb9FRaUIoJv73OyFy893LKZqqPBgaYsWFmpDYKk0FMQ-9s0cK_ZpcL4Bt3APAkxpz5n6veyxjZAOkuLZz3qwo1doqzZW9456MpPP3TycOjeceNtiq4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💎
سرخیو راموس: فراتر از یک مدافع.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102980" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102979">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A_lHqq54_D-GR97YQ7yowx4F3FdJ0V5V1nnC3IG3Hee-2tFGOxf6qIAAf0GoTXqaCsLzyCghWY_S_AxeHMNyq0oWapqaQRCpm_rK5sLh3Z6FCk3-_NvdPsq5nFzpoEwFOCvL_TrdrJ1F2FrNAtH4Z06CyeMhAJFAVYrJYUYulnV_2ZEbIHXvcoml63C0DxHMt9aPkzRtSHeU5shBpIQEeHZRS6VQOKQ8qHEJJ46w1OGy-jmhIeTLAPOGxtrKJAVlGTHmuZp8S2rYafrIaVdxpPjfREf3zoKPxK_9c3mB0vzNjOlKer8RQa2VcPBZbk5fFB_U3acXBq9egRqxXl7_VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری
از جرارد رومرو: روز دوشنبه قراره یه خبر بمب راجب خولیان آلوارز بگم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102979" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102978">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXjJ5jzl7lftBp3yjd1H4HsKAjUIDTco9glOvKY989OCFsH1Z3uRbY_TppGckd5Sf-vxrqNfvcUZEzojPmiJwVoBgRvRqJecRhYcMONS-VrYw02TCLHBvVybX-pK-GG-rbsWl6ErYTWOypWKiqGiPF5EpJYtqV9g9dlebkTe0q1mQoN9bvAI7fs-vHTopaOs4sjKOA7YfVDfMCyhVIPcuvO__oMMsGngxQ8kgs7i-Z0BS9hZKN4ogrE0xlb0J8sOD9XnwqD_2ghYpW_jb635oyrPIUkII2PaJKW8e8Gnv7A9MaPfnM-wpKpO8YZVp53JTsfT3vAfziGwchFUeFjb6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
مارکا:
نقل و انتقالات تابستانی رئال به پایان رسید و رئال مادرید معتقده که ترکیب تیم ۹۵ درصد تکمیل شده. تنها استثنا، پیشنهاد بسیار نجومی برای یکی از بازیکناست در لحظات پایانی تغییراتی ایجاد کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102978" target="_blank">📅 14:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102977">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5d0Q5p6W6M8mFVyQf-7aWolE031BMb_9lnTzanAI7FEw7QhqxAMBDHHAsBzmMTIftvNHmnX14zDhGThFGI5OodB3ZL6Ga7e4Dd-CZVtMYELYBJYAqb0noHHIuQ56GWsyA5AOJlCMk9phoFoDbOFRvs4ZuJo-CxSCW3rLmK2VMHDS8HIm-p5OBrizPMIZJ3E8E3qg6cTHt9aO50STDc0xi3F9H0cIhPD-ha4dn4oJydW-y4J2Hvkg8dkLEtrcNG1Gp60VhEOjzpcNkBJ5NGs8fB_LWtUZwt4bN-vi0fHpSgP39oMCGuGmDloAazepDUbNL4ZW5oGik4kjU86bBIfSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رومین مولینا:
آرژانتین، جیبوتی و مکزیک از جمله فدراسیون‌های فوتبالی هستن که از جیانی اینفانتینو حمایت میکنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102977" target="_blank">📅 14:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102976">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlXT3fcPMNQAQbqRwG8QE-xnWAhu4oVXTW_pFLN_ULQdKn6tekmP7eRJe6HFXeAItci_Z-yZbyn8XnivFf0-bfF2I-lXzhkAe6zwGCh6yddcycxh6gY72Wx2i1CxoqZeRtGHM2G9o_Hq-FfcpqJVPHNq_OlD5Su9Pcv8Qi1PFU0TpmG0Nro3mBVUoPcJPJJfL9e_vL9aC7KL6Mr9tcbONC8GtspsTIFQ-BRjYwaHpMQr7mIRx4FXSCayyWhprsXv6d5NaBJfUIap2SvdGHLSVJSTzMxD_apq-TikHe0rEOctLm9yK0RXHBdpOZ6TsvxZi9MxSF-f6YDVMDRCyTPagA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
برخی از ستارگان فصل‌آینده سوپرلیگ ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102976" target="_blank">📅 13:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102975">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cw9noE2Oud44fNMJzK6qONXpwAdJj3yd9EeqNs_YZriLM3GX4JqxdSQncZlsCjpSHysfjk-xy2CoOY5h-MDs5ey-1lvztloRNPuHxIFsYYfCoUGOraxXPbY6_pqEKXxFxnkr11t-MdUIej8FxG7P9M-dVChoCTwBaD9vEApxWCikeJrx-2JI8pZ08fdZ3DcfFkHNcw3z5CnVuWtvVc_V-SYTHLvWKF-Nj7s_xgXnONw4s7WRNpSghkCe1lqpzWcGme8iyZ989tcJ9OqBKxJ8fRg-mnuo50JgP2wVqh6TpZHHr3B3qEcVzTq1mZjzgT4yU4HuJh4pW0VCMQ2-_ePKyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
اسطوره موسی جنپو، وینگر فصل گذشته استقلال به پانتولیکوس، تیم یازدهم سوپرلیگ یونان در فصل گذشته پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102975" target="_blank">📅 13:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102974">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6I3sAdykoC3s50xVCDZyn7QUa3pxR3O3qtg3me129UBBUno40zDMtiVY3xDywi2CjhyLmJgRCdQafR-DDcIgdf91ULxeSkVL4Xa_A2kepOQzjVVU0rxk8MeOJFl3R6dtCsQwbUOZOVVG_qMkT4yS7MlKOx3RlolZ2VlJYN8KdZp7WdzsbyRBo3TXXGIbhm7Y4hnGoOQMSixXikJLs49kuvMRL_uQx7Pp7Wu7jLqe6TZwAfW7bs0husxyv0EyE2PU_a1AwVdqhiHdx56EttVJmSRaFf3YwLuKZnpgjvp6lA0XKw_yzISMapIZdXslanmQTtjn0U4-QWr4oeod3q_bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
لیورپول برای جذب بردلی بارکولا به توافق اولیه دست یافت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102974" target="_blank">📅 13:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102973">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa95494b3c.mp4?token=B9MDUn_TrkCuhy-Y9bB2i5jCrSlCTOyHcxDK0QTRatQdVoYk3fcgoRRIu4XUDkQWEXwc38SI2j24VBit3W0sJscx6O6QiTcq-M0gcI-P9pWgMGzjKeHLohJmoEWQM2BzcW8TL8uys9MDvEWNreejGXnUTzJ-52Gmg2rZotgBUriKt-53y8Wq_ghC2JTFN6CEUyApbiRhUF3r8ffDNLvJ9Lg5brT-ntzL7KS2BcLvg6PAnk7FqqCFHX8UF61oKIFQACAyXHmHqUgH0F05wxVnfqXJiph3ryiumN8NaQrlDT35olURYIxfy9WZuXoKrT_BTX1ZOHcJgGStfLF-O3eEOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa95494b3c.mp4?token=B9MDUn_TrkCuhy-Y9bB2i5jCrSlCTOyHcxDK0QTRatQdVoYk3fcgoRRIu4XUDkQWEXwc38SI2j24VBit3W0sJscx6O6QiTcq-M0gcI-P9pWgMGzjKeHLohJmoEWQM2BzcW8TL8uys9MDvEWNreejGXnUTzJ-52Gmg2rZotgBUriKt-53y8Wq_ghC2JTFN6CEUyApbiRhUF3r8ffDNLvJ9Lg5brT-ntzL7KS2BcLvg6PAnk7FqqCFHX8UF61oKIFQACAyXHmHqUgH0F05wxVnfqXJiph3ryiumN8NaQrlDT35olURYIxfy9WZuXoKrT_BTX1ZOHcJgGStfLF-O3eEOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💰
این شما و این گرونترین خرید تاریخ باشگاه رئال مادرید: یان دیومانده.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102973" target="_blank">📅 13:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102972">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4YQ_GKZkijnrCoNTaTTcZBQa47JYOU-F714i_y7-xY6l5EB4LfCB5GFonpj8q6pRrbOgS0wGjWfuM194OTtl_VA14G47UTMad-N9MAua43KTRZw5NnIdIa1ehXPNQG0plEDZlXrSBhC2qobZeMl8N-U766Lgwav5BG98j2OLrrzeSqzG4xaGAJsWht4O0FrXqUR_uOwpGJaajKMdGA-F4aH-bSq4_95OoZVRGNRogL7xIAej3xEKYVn_U9KkbHqPF45KR3V6C3Cy3XxMifdmXIZA0-kKNqvv6bIPou_3UN3snf6nmKem_WPQyf6wCiVzF0xENk9SGayMycN4zxo3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔴
تتوی گابریل ماگالایش از جام پریمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102972" target="_blank">📅 13:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102971">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWNRZow_fsA-IW4H6pjFzLHHXwQnuKMJS81MEDAh8WQNNL64_RmGkeFhSnIR3yjCk9jgl5d077NYR4bE4uQg0vVYaOntoNzWYvnUQq76zY-SFwBcnsyQ3tXv3bmA6i5N2mx16xqSGjDMgFBXF6UniDAGvSSRYrD1x7H95zkx2Vq1AnXkRxHmQy2oLIWhQbU4TBBKt3tEFfVzEGn734znUmrxrUYaew-xboWQ2Ktw_ivq6OkXKjiegjg8baJcYQ6w_Zd4BhkdIH1F918ZaukSbBBr30UTrZ5HUrRetvN3kG4oqCfK46AK-tgaK67cMgZdM5ZfnLt-WrRiUa5q9kCGQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔵
دی‌مارتزیو:
اولین انتخاب مارسکا برای پر کردن جای رودری، انزو فرناندزه. سرمربی سیتی میخواد دوباره با هافبک آرژانتینی چلسی کار کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102971" target="_blank">📅 13:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102970">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lvjxk8gMvOyRH_q8ikdASt1k9C9HeQunytA9Efn40Gl3q1I5-utzsa8mlI3d8yrfM9eVlkeDK4unQfL1rdy20SMHbxrsRPDqvP9GYISsMPpwZG_0L2meRrLrgox5wvMZcIm_j91ISLPL-WgvvPUZ19v_AL5CzIiXKo_rmavC9Xtc6LPdMeqtrdwSbx2KBmOKZhxM1j2FewJ1humtjF07UCG2uLeSXDPYTx7LAMd64qDfrYoJyPuOYhOhtjRn07IzrQi6nP8x_t9vwtRRhdlyncKXug_-HD0o5eMTMjKvanCpURwhFYTmd_EiED9YWnZHAhAKKRg9Wqv0DadtPJBt0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
⚽️
بایندر سنگربان منچستریونایتد با عقد قراردادی قرضی راهی سلتاویگو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102970" target="_blank">📅 13:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102969">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXcM-eXQI9GEDAeN2TJBr0HwG_IRxBHbFm61u_3zVkIgvZirpixMO_STE8t0dcvx2AXuZloU0xFTRaKrzklmQzcRjvSGmE824XFGjzHVPbjU46HtrDhbV6b9jpuPqnfz_ZR5L4LsAKtCR_dHEZvhX_rjsiDbeyf9dGvQ4tK9yJlpyMpT518XKZ5AhNmbmUBnIw8JXQlJJJzwm4xq298tyiMO0bH7pLefzWy2SRnlWpHuxjf7CU8aEPZgWF8s44pZ-PQNjcrBMJrypSbhJE8JYr6a47Vb194GAF3zceEyXsxRGKjC1HamPIXUYmhPgH2ScRPdvuTaJYxiw6xy4f5sbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇹🇷
🇪🇸
#فوووووری
از آلفردو مارتینز: مسابقات سوپرکاپ اسپانیا در هفته اول فوریه ۲۰۲۷ به میزبانی استانبول برگزار میشه و برخلاف دوره‌های قبل، این‌بار خبری از برگزاری مسابقات در عربستان نخواهد بود
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102969" target="_blank">📅 13:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102968">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/102968" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
r16
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102968" target="_blank">📅 13:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102967">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIOwFq6jLMqx8xZkobvRG_GdEaCdcHkDkJiDj9rL2dr95yw_a_DIAkcXcIZpe-DXlxpyIZpB7ciWq31RLvcBg25gWVY2GqtQ3X5_FvmCq_Pf4RApP0e1l7JaZbpj1KlG2sbQ7oeyUQZ4J8fnyfATXKJMuuiPHkn42oKVIu4Bh4R5g-8SQkMOYratvkDccfjlPmitdwZ9ZTth7a0nSKowIsnluoEFzbQQMtEsrvvAe4pQLq2y0f6YqOalDPkLSz3rEMNqKrarWWJ7yOL1_yX99gJJuVYLOweaPK2LzrYbEVidbT3WgjmqCTDgqIviO1MbQjmx32n3xb9F-aFU1KLn_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r16
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/102967" target="_blank">📅 13:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102965">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RWNd9mSCIvtEZplcStHf0pyQPKaGjnZvVv8NAPBUuKt7plWtOptSa1-ZBqXYk5CeH9qPadQjmtlUWTmaYrFSB2hyTj0q4oj3motjUceL0jr1fOzezmAd80vFWS_3EfZL6rvqZgstR0o5JYubvZo_EPGQZixnrnBpuRkM_VyJv5741KAkwTLB4y84gHG9yOXDqeCjrVYkd1yp5e95Ju_dfSz5rCxqXQ-0oXQBYQO1vPMjnJWyqjwKuQL0AlWr9wDcS2851S9vVOfn5qA9YMdkeUzApC5k4jVxC0rj-64xh1Omz6kIZAvos5SDtNayvuu4vkpjqxIUmPiejmkp17ausg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RXazBTkSSx9PxSCur3H5Vq9snEucFC2Rmnb3c8CbjKgWy4u9ZgZroAPfiG1R2C7mizWduclLxMlLZHpIgyKwFkpgbRRoAkGjfseQLEBP7tP4kSiPN-m4oABWfuc_WBkgx235Pkk-9W8fF-eKwuJ3IA8C-JREFSRYhaOhgdC7PrOWSys9JNHD5dEHrBnPvTtxuNFCmtZHEnOBnGwlseCI_4OGy2ghwv_l_nsWndNSwsQgBzgurEJbazb-8LN5L5elLFSqB6ZwUaq9kkFsK9Ydl_NOwyHPx_0wQTdJz2HkkK4fhIKN1Gzn_mEEENlbkDAY54W2nyOTLJ4zge-jFDxXYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الکلاسیکو فصل بعد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102965" target="_blank">📅 12:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102963">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YcmlqKSgo6u0yYwYEFoNMpTuShMv2WLK_6VL8GWG4QBDUvvaCP8jHTHA-7WZJ5TklrgIgKxKuE-UfXWp9mRJWNe7HPFydxHnnBGBlwoGj9vMOzNR6hTPCI6YEzks4oR4Fja2csMGcs0o768JvDDyrhsn99RROsaf2l3Sn3vDwnodBDv3A0vutLrRcvyn6UllGmjHMlZH4jBfC8ZVVDZQEabegTyhTo0YdivFKYNTynCMcNJuREXEkgwr1JwPGSLJDl2ELemA_9239m0NHmK-731j75oWo-woxtCEDVwpalBsJwXfMp_2_-Ki_ips_rgjJc5_iAQ2t0Mi5G61WDjMPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CxOqWSCGajvsXHgYuEnOTtnCyvskb0MuGGnO7lSw1NhJtWUqFo7RR7RbD9WFlaA_kppScJqNBQDRWNbhBZfx32zA2hKQN5lR-PTQOifx8CJ6Eeey04zz34dnBm3kTTwG-5ytSbw29Q6MljyO51ds70rQSxrf5pjFojykDQD28vzECDv5KJ_nvD0wVXKLQcE7QUjnnhZThI_g5t1ENNTIiMm7Su9cTUYUAkSNZjUjl5pjPh5iE0KZuMBvHlQUe7f3DHJcsUYsnqbOW6o3QusxtAm4VxZnAZ7RITmpQOrsk6wJds_PaHzPIAUYAfS3MR1NosXtvEUdmC801FlLaHGeqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
⚪️
تونی کروس:
اگه کریستیانو رونالدو هیچ‌وقت از رئال مادرید نمی‌رفت، پنج بار پشت سر هم قهرمان لیگ قهرمانان اروپا می‌شدیم. واقعا هیچ تیمی حریفمون نبود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102963" target="_blank">📅 12:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102962">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74542a373d.mp4?token=NYNU9D4gsMjSaIOoJEzBVOuceAbdmXXTBCB0eLM4WsLjxqj1VvF05crO8OyTBIGYVsFsHS4PbBwdteJwrXGvCLzFYSVkRj41qeGyRY7Oo3Vtqe57FIhnpYCFazIZP9BJxborElQNfNU3KUmGW8dKCYjjApvHWHxy5vwE3Tl_lvP8V01WnI2gbP4cpCsuzcnycJ6Ghscoa9Dt5FPrOdkM8ASR952oGX4ASB3beqjDdz7UoNAxr6SXK7VF7KDxINtZPJ62OlXh69ca9v6AbPtQDBZmMUFIFX0jc2x3mxGr1BmhQOjeHGACORn4C6WG-oKUMEUtf-oTyJgUXQz4KfZELA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74542a373d.mp4?token=NYNU9D4gsMjSaIOoJEzBVOuceAbdmXXTBCB0eLM4WsLjxqj1VvF05crO8OyTBIGYVsFsHS4PbBwdteJwrXGvCLzFYSVkRj41qeGyRY7Oo3Vtqe57FIhnpYCFazIZP9BJxborElQNfNU3KUmGW8dKCYjjApvHWHxy5vwE3Tl_lvP8V01WnI2gbP4cpCsuzcnycJ6Ghscoa9Dt5FPrOdkM8ASR952oGX4ASB3beqjDdz7UoNAxr6SXK7VF7KDxINtZPJ62OlXh69ca9v6AbPtQDBZmMUFIFX0jc2x3mxGr1BmhQOjeHGACORn4C6WG-oKUMEUtf-oTyJgUXQz4KfZELA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
دوتا سرباز روسیه‌ای با چوب تونستن پهپاد انتحاری اوکراین رو منهدم کنن
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102962" target="_blank">📅 12:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102961">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZqaV5u9zu8OzRtdHo7AArEIOuWXsqTVreFbxauuVQZJkcqf-4h50H5Tq4nO7_iBzVwHtis4Ad5ywaiaHcx05t14nqlUm0qPiiL3a3RBAx0f77w6s9azFD-9ww4dLgU-wAw8mKBU2AysTge4pFzqYIv8kQo9fGXyiIFbIebVvzjxmGYZPO54LoWryg_VKP2gPzDW4bpzNuu3zZyS2X3ivAY1RuCZRJGzBoduBCkROvNygm1b_V43qLxDAEaCS_Fy08cYkQwCKYj67tbeMX7fCvt9xzNPuBlWT7JU1M9pwGCPnINng6Xa4SzmvRJx8N1cbGGouDQGyTSRM49y-UEbRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تفاوت پاداش قهرمانی تو سری آ و پاداش صعود به لیگ برتر انگلیس.
💵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102961" target="_blank">📅 12:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102960">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSoU-8JvDgNsUtJ_ML8VGcLB5so8v9Ln6BURvJfdrXNrxIQUsNyqvUNDAXhv1_mQaQ6MbkQOcG2jgUNyd6tmZCzEJX4AlMf98NgBDWVqBL0IBh5CdZogT1D-FLnCcWRHDvGBZhzQfLLBqw01Af9Ieyiq9YPe2lGD9yfyPzrvt1-3PdG28TMW8p31rnGVdfxTfa7fdzrdmKAlfk3cMn54xme3W8DG_M19dHi9AgzSAdUevBn1j0AP4H7Awz69gRtSEh-bcW0VZv5iDXEIljVEgEP0AgZJajinMpHN8MwT-vduPO5fXQEQxhBEOvbcZkDm7mIvlvmj6NcSogdPpJBTWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمار اگه تو فوتبال به جایی که حقش بود نرسید ولی زندگیو برده‌...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102960" target="_blank">📅 12:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102959">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e300ebd1f.mp4?token=J8tHPWV2pCh-z7r83HtxOi_Bg4MA2nSGddpkH9oSB64Hkcl5GCa4EFEi9F0au6KNv82ESnXIvlZzrQyinbTJYck-wmVp9CThgfFkG9AUv0rcZUvUwi-0xSYA5YKoVmDeFDZG4NjK2oIps_C0iTaIOCTTpzZznU5aD1WKJ_sagw4CsKINorhPSv_Ffru1Q-VtPeXGtGR21xiUNwiuGnoymi05txC2lcIA8-QkMGkUV-7GYNgK3Av_r_qEa0NhAjKv78IIr55neSsHzJ3okoxNC-g0iEHeeMjorfWOghko5XV21KgAo45uRBJ3IAd7ZSZTWd2vh0pxgn5lXNu57wEroQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e300ebd1f.mp4?token=J8tHPWV2pCh-z7r83HtxOi_Bg4MA2nSGddpkH9oSB64Hkcl5GCa4EFEi9F0au6KNv82ESnXIvlZzrQyinbTJYck-wmVp9CThgfFkG9AUv0rcZUvUwi-0xSYA5YKoVmDeFDZG4NjK2oIps_C0iTaIOCTTpzZznU5aD1WKJ_sagw4CsKINorhPSv_Ffru1Q-VtPeXGtGR21xiUNwiuGnoymi05txC2lcIA8-QkMGkUV-7GYNgK3Av_r_qEa0NhAjKv78IIr55neSsHzJ3okoxNC-g0iEHeeMjorfWOghko5XV21KgAo45uRBJ3IAd7ZSZTWd2vh0pxgn5lXNu57wEroQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤯
👀
یک زن ۹۷ ساله بریتانیایی با ایستادن روی بال هواپیما، بار دیگر نام خود را در کتاب رکوردهای جهانی گینس ثبت کرد. بتی برومج که پیش از این نیز عنوان مسن‌ترین بال‌پیمای زن جهان را در اختیار داشت، با این اقدام شجاعانه موفق شد رکورد قبلی خود را ارتقا دهد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102959" target="_blank">📅 12:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102958">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de05a2b317.mp4?token=t9uqhDCX10HCi3JlCjUB80jTePEbsZKPf79ZTIeRUgIjtLQL6G-m_ybjgF-uSoyZ86aWpY3lnojbE19IyWXxU_omcPS6D7S8_cYjDrVcdt3D80jUC2IKTEew6VUe67fYDOKH9s8CJhAMF4zqyQ7gXZ6ekM0YODG-ZYF8f1d6ktopuH7PEjlNRBEnm-4q5WYtbZLPbALaDYZMoD5BQlKHWVxI_fZ4pLeOZCZALOpAZ0keSdoAZHU353KVGwz9m-fW-nuupWU_RlMK0qaHkobe8-u-TFuvEaniFTU6ytrz1EYv36Sf8ZEZSxBoMkjq4itJAVqYRtYW5_4mXn5eqvXMmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de05a2b317.mp4?token=t9uqhDCX10HCi3JlCjUB80jTePEbsZKPf79ZTIeRUgIjtLQL6G-m_ybjgF-uSoyZ86aWpY3lnojbE19IyWXxU_omcPS6D7S8_cYjDrVcdt3D80jUC2IKTEew6VUe67fYDOKH9s8CJhAMF4zqyQ7gXZ6ekM0YODG-ZYF8f1d6ktopuH7PEjlNRBEnm-4q5WYtbZLPbALaDYZMoD5BQlKHWVxI_fZ4pLeOZCZALOpAZ0keSdoAZHU353KVGwz9m-fW-nuupWU_RlMK0qaHkobe8-u-TFuvEaniFTU6ytrz1EYv36Sf8ZEZSxBoMkjq4itJAVqYRtYW5_4mXn5eqvXMmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
🇪🇸
بارساییا بهش Welcome بگن یا زوده؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102958" target="_blank">📅 11:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102956">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iZLkEu0XgxogEOqQtm-Nguk1KzZq3bN3_PRTynqJimGkSBaU6El5ureJE5D_eFa7TKPAW2WIW-aaEMc9gn7gap6ahhHt3MWyV9RwPsoYpP7JzLlsosXIIjVjczXw_5qqPSQDx2SPZDQM7JTo_0LXCxfHSf_tWqn6HWlx7vUTLxU5hWWgOzqS-IhV3TfogwCzXCl1v0LUQKWD3ddln01V6IEyDOsMiJ3O0MkoVyhzx6V4EnxvSIOQ2Ce-t8itGd49_Rb4wNY854mdSf6aDHiUSDceWsukATCZr-eLKtHTW7nSbVyDCGMjHsu5-PFQn48Hn88Y5Y190bp3uILx5syRnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FUZcYRn7hCiktplYpcWNEqj5hhvFYUXT6G7ccCH9b2AxQYDF3v3RHPEP5KTmc7vr-A00BNMOHpYajCbOP2ZZa8ZO7knA_4O7NT7czVMmETy9rjepX5UUAoLVOPlA7FNoah1KwOP-qpTJ6XWfY-YLCyd25ii7KiPFTH7FS8Ll5UG8aLtIPTymQFVFkLfv5VGdADmD6r3ZrRw9ceCxg2FmpnCs5OU0ISGmyYaarE4O2da_HoFAvqi_DlBUp646eBFDYLt7oavUxdk1RCIFgwC9uy2pUt-m9eGrtYL4jpNvlihkCUPd2sjk0aAHl0vVf7VeTEcf1iCcJ-FEY9wphiSLzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
از کیت سوم و خوشگل میلان رونمایی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102956" target="_blank">📅 11:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102952">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IHWAxygjn1NmAryKjbNOREmOHkZ798uQTx3vk7cXGaCslUTA5fp6GQisUOlKFXulMeZwYYshcJHBePdfVhmJLpNxVxlCUyO1Lltf1dNONEc4HHh8Aj53N-dRTboPpTNNixvdvkIw7qakPgaaxWGxVM0cSD7oeyLP31DADvTUU_QRvr-aaCkxPHE2q7XaOu-Lg_Y_0TB4Eh0maBv97suU29kt55zh04GcT5rVJTAlY6rpsNHm9R5vFLuAlmePuRGu6RltJF727t-oCQdKGz-FMRladvx7RI_VZU76pDrmaH_2OKEDLf3gAZ5gzYwKQMZUhiTDqvyyomWPdzYogN2f-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oROB_nlJ_vUCWLCunm9Xg3AaZUxtezJFCaJ0c_DKphLnZ6dBTO45Fz9pq5o18_ovD2av8cTtLvi-iELqm8Vd1xc9Yy-u23OF6b7c3fzgfDYS1-5aj5HRYUv3Cu7shvvBie1fJxrdQjmXXydLg12MbpxHcqLdPEIIlkU6gxIsxnSwhclhnFvLjxOTKuL9-OgiBewBebkGjRM9yT5Ls6QAHISyQxzkE22aXF9gitvk9IeEUqaDCzxgPWiBIt3CXOMZ5yrXuDDkjHEZA3F5u7oInEBDvrN-QtFaeD__grD_0gYhSK5ZrlTnkQH0LIYdkfExjwvd8WWJ_AnfD_WukQAiMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iuYEVpJ3n07y83NXJfe47s8cTQWquWija3As7suItLwAewFAWttmg8z0gjgcSzJhug881UTkbN3f1pgW6bJArCOqQR4i4DON4zvEdoxXeKs9Zd38eP-cadOujOdnbJMS1hIQ0zqdrRy2p9IMJZnrgbh2BGsZ-cXzWHPEoJ21tdsSLf8bRShpIiVKf3rtf7zr3778M-WC8olvG9wG-Sk1zw3wYkr0dEpIOYHBZASSBpMuvXq-TRmhPbbj4aiONPahRK1UA7W3Z4GPd-bzqRjMNaMwlPlesjyc4_m6QHsu72tpV6UIwftJWiDbQWOdH4KzL_6dEK-XnkGgmSP4imZTtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/USCUHjqwtvlefgwzP0WpK-dpvl6iwesm327r5IR8z8H04JrkIbRwU-KtHK4vhW-gaWMWerijZWsUm5PFXCcREHMnOV3reuheGm7rXifpnmDyZvYyjaKXlgnAHLXIuGZRxlxjW5airnnC21p85QMFMfeEG5K__qlXPyxLknIRsK11kCtKVpGbI4psRQvz-DUlg6406FGy5okfw_pxl_DMudDvtxlrj-XaMfBxCG6erWTW9ILHYgD6nNiqkJF9u6Tky_TY_BANE_h8HoYVH_wvXh-yQR7CUX876Uio_cKcPGBMetvcUcI2SpxB8xDOeoQA64_nUbnnbRk2k3kHbbzGxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
کیت سوم زیبای یوونتوس در فصل ۲۷-۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102952" target="_blank">📅 11:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102951">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0147f7deb0.mp4?token=doPQVgaDPI9lECmp-V20bSKcm6MbOwsZ1HSTzQugn4y7w6oxWLQfXOcrVvSVYt_PZ3m5bFKhTEbnlo_PkcVlFKL9HntkkZf4aOvFBFdrup7j9HdDnkJiRRYNQbE-DtBO-PtLLD_0ST7-7rh1oyT6iqgPJwM3puRG7JGnTexavPHFwRSIri1FMlae7Ki-MLTvRSh_UHczvTX43N0X2zD3zmNkDC7Yf476MPmwwBDQvcQrnWCoyJ3QIXgr4-in48DRyvljaLLZuWgNezDSlVy1LczPPSqalyim2UHV4jlknELuf-P_sbh1a_YBD-E-rcax-Fs8EoVMqjqZffWbmp4anw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0147f7deb0.mp4?token=doPQVgaDPI9lECmp-V20bSKcm6MbOwsZ1HSTzQugn4y7w6oxWLQfXOcrVvSVYt_PZ3m5bFKhTEbnlo_PkcVlFKL9HntkkZf4aOvFBFdrup7j9HdDnkJiRRYNQbE-DtBO-PtLLD_0ST7-7rh1oyT6iqgPJwM3puRG7JGnTexavPHFwRSIri1FMlae7Ki-MLTvRSh_UHczvTX43N0X2zD3zmNkDC7Yf476MPmwwBDQvcQrnWCoyJ3QIXgr4-in48DRyvljaLLZuWgNezDSlVy1LczPPSqalyim2UHV4jlknELuf-P_sbh1a_YBD-E-rcax-Fs8EoVMqjqZffWbmp4anw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
زیباترین گل‌های لیونل‌مسی‌که برنده پوشکاش نشدند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102951" target="_blank">📅 11:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102950">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/897207ee53.mp4?token=Bb06jF62FVmRUr3DkcAPa7osHegxWIdanF1RBPWcGObgDvkQg05ElU2Eja-EuXAl9qCAorHCkaaaLTpzNZXB2NP43zF1gki676kic_M4rd6K4jGWxHpiEj5Ibg52r7iKk0TWBLOXOmZLc0WycQni1otL3Rtsh7XEP-cGCJctJcsxDf-RR9Aap7BoK4LpCbd_uIuUQ9bRKSuDbeo55mrvFm1gtjwM9A3T413_km5T0Ali14lgu-pTIWLf3lcjs9Lj74ZHBm70B1gwLhe-7XPU7HCnr_Ryy3bRZD37RVJYJYR91hhqUGYXR_fSLit0VyJtgfiFX9axOrb_P3wxm7peuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/897207ee53.mp4?token=Bb06jF62FVmRUr3DkcAPa7osHegxWIdanF1RBPWcGObgDvkQg05ElU2Eja-EuXAl9qCAorHCkaaaLTpzNZXB2NP43zF1gki676kic_M4rd6K4jGWxHpiEj5Ibg52r7iKk0TWBLOXOmZLc0WycQni1otL3Rtsh7XEP-cGCJctJcsxDf-RR9Aap7BoK4LpCbd_uIuUQ9bRKSuDbeo55mrvFm1gtjwM9A3T413_km5T0Ali14lgu-pTIWLf3lcjs9Lj74ZHBm70B1gwLhe-7XPU7HCnr_Ryy3bRZD37RVJYJYR91hhqUGYXR_fSLit0VyJtgfiFX9axOrb_P3wxm7peuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥶
یک ورزشکار دبیرستانی در آمریکا در آخرین مانع مسابقه دوومیدانی زمین خورد اما سپس با یک حرکت شگفت‌انگیز به خط پایان رسید!
🤯
🏃‍♀️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102950" target="_blank">📅 11:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102949">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c054d35c9e.mp4?token=um5yPzPmpNWy2B-XkKzzeBRUeEhhFLX5TDCwIl6eKP810LxwbYyedO36yDR8n9uyMBgjGcZbiLDiJFHPHdPJvJxR0uV7XTtxqRH8Cf9h0MpDjR37q-nRfiLRsvYgV1nOr2ens5_lGHmKduezykM_y5wJJ16Ce6jE4HOFZPIVnyA2nXziZ3XSvFocNTK6Em5GXFPcbtkSAzFkakuQ2eIZPHw5FA18j2iVHiQ79ZfTzl91F9uhBOXy_fIicawTIYULZnDkBd1TnpopbHQ-9Xbxq6H0u0Yy5N7siW2Bdigin2NYY0Fo2dYpvRO6wrwpA9ABWRP8GbKGU-gfzvP93tx_mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c054d35c9e.mp4?token=um5yPzPmpNWy2B-XkKzzeBRUeEhhFLX5TDCwIl6eKP810LxwbYyedO36yDR8n9uyMBgjGcZbiLDiJFHPHdPJvJxR0uV7XTtxqRH8Cf9h0MpDjR37q-nRfiLRsvYgV1nOr2ens5_lGHmKduezykM_y5wJJ16Ce6jE4HOFZPIVnyA2nXziZ3XSvFocNTK6Em5GXFPcbtkSAzFkakuQ2eIZPHw5FA18j2iVHiQ79ZfTzl91F9uhBOXy_fIicawTIYULZnDkBd1TnpopbHQ-9Xbxq6H0u0Yy5N7siW2Bdigin2NYY0Fo2dYpvRO6wrwpA9ABWRP8GbKGU-gfzvP93tx_mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔝
▶️
عبدالله موحد کسی که واژه‌ی پهلوان بسیار برازنده‌ی او بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102949" target="_blank">📅 10:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102948">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3Nj5eYo-r_khJrLuxUDLMpaekCbaq-t1NPR7m86YE_oPOryQ3iBjLj2B-6uGl9oVX5ioXv81eiiHfO1bB7VxkKxwHVtizemm8bmdHeUn7tySe8J_zHFKzKGY60-19WgGvp2b6Dqc3wBIOOBK1O3d33d3vZqw_6A23fuSrm1vqE-AbbJOe5Pqho7sCBvaUCQy77yP_k6S5LW1DrbQc2XFkIN88Ez4ql42zeDbf2QZ4jEA4LVhFx9Cb9_X_waNMReRqqsbn_O4-WZR7EBzt1JOgKZWODJmaxZ1enoQ0OD0ExPo-YPVg0BrBDSBrUEqy6vTdyjV_VwHSieTXTRNZSJow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیکولا شیرا:
قرارداد رودری با بارسلونا پس از توافق با شرایط شخصی تا سال 2030 اعتبار دارد.
دستمزد رودری 15 میلیون یورو خواهد بود.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102948" target="_blank">📅 10:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102947">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f949a9e24.mp4?token=Y_RHBkj-zz-CpjEZ0FMJGd9-I52AEsN2S4-U_TUu_aNEKlPqcxeRiQKJp4BO29gBhbZUeiU4vvJfmtaLkkBoB6AiujKNz4whnD-J9J5l0byxUEzdPbzDqDTU2su2MNVihbsZr3Fw-l2DaM2AufDcbzVzkapMfFxS2dCB6jkrZTC57RSwHXdaUIUagM9PL9iV_odYYlMK2YsbEzTPP6UQ5qGPfSwf9dkmSCE3qpV5zhxE1lNEtbAvIU2-QguJt4HXZl-8EmMu7RTfViFZu-4hJTorangM2LuHP4iNMdywAf24i_CMbxqjLK3M01oD6n01I-46JXTw_6dXDvR1zCuS-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f949a9e24.mp4?token=Y_RHBkj-zz-CpjEZ0FMJGd9-I52AEsN2S4-U_TUu_aNEKlPqcxeRiQKJp4BO29gBhbZUeiU4vvJfmtaLkkBoB6AiujKNz4whnD-J9J5l0byxUEzdPbzDqDTU2su2MNVihbsZr3Fw-l2DaM2AufDcbzVzkapMfFxS2dCB6jkrZTC57RSwHXdaUIUagM9PL9iV_odYYlMK2YsbEzTPP6UQ5qGPfSwf9dkmSCE3qpV5zhxE1lNEtbAvIU2-QguJt4HXZl-8EmMu7RTfViFZu-4hJTorangM2LuHP4iNMdywAf24i_CMbxqjLK3M01oD6n01I-46JXTw_6dXDvR1zCuS-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات کیه‌لینی از طرز دفاع ایتالیایی
🇮🇹
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102947" target="_blank">📅 10:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102946">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6a2b88eb.mp4?token=cI2LV4g6JrKwUyy6-BmeblZRMZMHvOiZR1aTR0VvT8V2mz8-dtzmyrkTwmBAL9InMOW96xNiR3DCUsYMLISt47D9bBCQO4qPTVIH_Biy55LHrxs1hDPhLkLMW-NIAm6tgQ7orSvYfcd3HSKiVz2flSsVzV1yZKGrIyMLT0dVy5ZauVlmU6BH2BCa1XyIwqpThCVJbXt7FjDukNH5ZC5XOJxCperrVGgA3BZ9m0gj3q3A85NuOyJaBF8bUTB9Bkh1vgfxxQ5p38xOTULqwrsEy6Tb2oTXdZvGcbV5n795EBZmW_glPp9FBTyBNsKGgqILSqvve0sw7fWFkBMinybfJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6a2b88eb.mp4?token=cI2LV4g6JrKwUyy6-BmeblZRMZMHvOiZR1aTR0VvT8V2mz8-dtzmyrkTwmBAL9InMOW96xNiR3DCUsYMLISt47D9bBCQO4qPTVIH_Biy55LHrxs1hDPhLkLMW-NIAm6tgQ7orSvYfcd3HSKiVz2flSsVzV1yZKGrIyMLT0dVy5ZauVlmU6BH2BCa1XyIwqpThCVJbXt7FjDukNH5ZC5XOJxCperrVGgA3BZ9m0gj3q3A85NuOyJaBF8bUTB9Bkh1vgfxxQ5p38xOTULqwrsEy6Tb2oTXdZvGcbV5n795EBZmW_glPp9FBTyBNsKGgqILSqvve0sw7fWFkBMinybfJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
جوری که رودری تیم جدیدشو انتخاب کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102946" target="_blank">📅 09:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102945">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdea72d125.mp4?token=s6AwGHlX1ZQnNucich3QFPyc5Hy15qU4-gKO8NjAlVRjeOlgegt6Dmu0ofSWyZcYBLt-2zeEjUxNWhRW5o0dUkGEKCd6pn6zSSLmRqKRnxK29Xo6xnjqH2a9qKm_TnoucYPd8YRKr5xQHphRTXQ1kKz3TzjI7qG25aVHoTyqt7GNfNbsioQ71jpaCUrAkKHQs2Qv2u22uROfzVTXzCYMF-2nasxyhfsaazcLg-9dLvijlQl6kMQosWhxndsx4qyztudAIaMFMSnWAuecZ1lovR40WrSfeaGtLT8tdDJpMI694ddbjrFZ62ogLjODPS_vsHS7tO1MqNm1XoDn-YyeWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdea72d125.mp4?token=s6AwGHlX1ZQnNucich3QFPyc5Hy15qU4-gKO8NjAlVRjeOlgegt6Dmu0ofSWyZcYBLt-2zeEjUxNWhRW5o0dUkGEKCd6pn6zSSLmRqKRnxK29Xo6xnjqH2a9qKm_TnoucYPd8YRKr5xQHphRTXQ1kKz3TzjI7qG25aVHoTyqt7GNfNbsioQ71jpaCUrAkKHQs2Qv2u22uROfzVTXzCYMF-2nasxyhfsaazcLg-9dLvijlQl6kMQosWhxndsx4qyztudAIaMFMSnWAuecZ1lovR40WrSfeaGtLT8tdDJpMI694ddbjrFZ62ogLjODPS_vsHS7tO1MqNm1XoDn-YyeWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
بهترين آسيايى تاريخ فوتبال؟
👀
يكى از آندرريتد ترين بازيكنايي كه ديدم. با اين که هميشه تاتنهام رو دوست داشتم ولى سون و حتى كين حيف شدن و اون طوری كه بايد ديده نشدن
🥲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102945" target="_blank">📅 09:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102944">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCAjK_4DkY39ayJyiq8vgzWIAzbcuQdtfCwPnt4qxsMBOeSGGYGAa-yk4cwFBdl5bw4uvnLdXoL6GloRbHKfpKQJRamlF_6trnl6HCl7oXlfK5UqAoUl6Z3Wz8RcbfZtXY_K2SWEwMYbo2paonwGKLRnWUISM-JrVhlERqg5Tbhaqzczr3cFw2QJP4i_q1Gz7P_49egtyBd8oMSPcn97HibigOnlFRfTf7vXdSiPrF-kW1ymaSzYdFiUOKyMoCVIm_H4zSGHzWjwT-aE9h952KRPtjZNH--RQLbpHI9dEvu7gLW0DZSCSh1OXqlFX5UUzjcAJfdlW4cSADu6tcjVjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پله اسطوره برزیل، در 4 بازی بجای دروازه بان بازی کرد. تو اون سالها اگه گلر مصدوم یا اخراج می‌شد اجازه تعویض داده نمیشد و یه بازیکن تو زمین باید جاشو می‌گرفت. این اتفاق چهار بار برای اسطوره فقید برزیلی ها افتاد و تو هیچ بازی گل نخورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102944" target="_blank">📅 09:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102943">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab63e40e3.mp4?token=ih2leyCxvu9Mg162mntY_p4uejgKMUNbpN0VQGsoiUH51F8iC7LWPgMIxhOTt__V4Agc6-_cf7V7HoSHrisPXTmxh1uxseuUsmOFUAMNRDnWEwwvjFP6A1nJ-RyAxZGAzB9h_bKw1rPgZfhKyLIFOV5CuHemBw5WR0bDc__oQIbdpFPt8Z2Ap0Un21_kXB3YW3XLqza9cSTePTqBl4xbe3Tq8foaq0ED6d7x7FPQG4ysStY45CiCxK2BMqWMrbOmeGGhEzM3h_t0enkTOuLfWCbZA48tDNrmwmIu2W-JbeTsCRAcD5bCxwz2e5R3KdtCWdWdsKdbpPUuQCCqmH-j9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab63e40e3.mp4?token=ih2leyCxvu9Mg162mntY_p4uejgKMUNbpN0VQGsoiUH51F8iC7LWPgMIxhOTt__V4Agc6-_cf7V7HoSHrisPXTmxh1uxseuUsmOFUAMNRDnWEwwvjFP6A1nJ-RyAxZGAzB9h_bKw1rPgZfhKyLIFOV5CuHemBw5WR0bDc__oQIbdpFPt8Z2Ap0Un21_kXB3YW3XLqza9cSTePTqBl4xbe3Tq8foaq0ED6d7x7FPQG4ysStY45CiCxK2BMqWMrbOmeGGhEzM3h_t0enkTOuLfWCbZA48tDNrmwmIu2W-JbeTsCRAcD5bCxwz2e5R3KdtCWdWdsKdbpPUuQCCqmH-j9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🇹🇷
محمد صلاح در مراسم معارفه امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102943" target="_blank">📅 02:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102942">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPRkTbraFsaRFYXZdbvy__qHHzQbwnelnBwhgaJODvUPNP8nTZ0pQqQSdsIDQ_Qc6S_NeKRhKvSU7wPR7Vd0Ffq1UZbzzjbavbGN3oNjUljWOktireUhOBNdsLc-udmPGNDqlqGNZaiKVtJZ3M3opnGD_YSatcgIFtBmkJRYPSTxb2Svb04HbX-mDK-qgQamroEz5liOLXGGm6DEq4aeCWqxcq86o4jHPeDN1TR0CyUibN7x9rBi34_tKaMl-516XvnF2t5UaCVijXWAgB2UCRcTXJAtyXK9Lrdo_6_Ldw1EicP3x1Mao8T4BSdDppXxsASq8UVISztcsOgle5L_Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
فوووووری از فابریزیو رومانو: توافق بین رودری و باشگاه بارسلونا بر سر شرایط شخصی صورت گرفت. مذاکرات بین بارسلونا و منچسترسیتی به زودی آغاز خواهد شد تا این انتقال در سریع‌ترین زمان ممکن نهایی شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102942" target="_blank">📅 02:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102941">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMZfRKCiBpqJJ0RbScWMGrq-xkW6Iri4Zp-YNnjH5yavLs_ybqdilDSjrzMtoslYvFRqU_sVhza1p9cbjoSQeBG1NnUumTh-OYAqdzayTuMuaP_h5TwPExYKSsXduo-ZSr7mGx6gfUzRDVoU-N1fS7YbxsxUqkPZpbmcCJUknF5UGpY3WYE0y8v8atg_U8rg8vmCL6EZyacqNdYSigWQn2R_sBtuM_bn7BnkhvRFCJbKg93wxNLt_Rkay1R12YxSUMxVcf77lHlyIS0wuNkMnEJCqbrdYN0okIik9xEiuAojGZD3yOgwnrKP75hmEfYG0FjFROKyIZ0Ay4Hb8E4J8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
⚽️
رومانو: ناپولی بدنبال عقد قرارداد با گابریل ژسوس هست اما آرسنال این بازیکن رو قرضی نمیده و میخواد با دریافت پول به صورت قطعی بفروشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102941" target="_blank">📅 01:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102940">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5d0e59f4a.mp4?token=F7-uQzlf2arSDR7bFarlMh-n01ZR3JNnfX_w4nj-tOWL25-bNbTKHYAdMUmDf9z7wVeZtzG-8OYySODn5HTfrY7g3h2-9LRXdCGwzZPkQ_JbZi8YjKIoIrlFPG7pqb5YSQNShb8Oy3Sa969MRF5pooMo6Cs_GZX1k2zlBfPse7Xt6kC3L747X7jwh-Br1RKQh6KwG6IHVdHHQA5omOlBTW8TscFLlg7Vm8lpEeF3TzdRQw_tRMeSuX0lz40-nHJilNW8p2pbdEhCFITtmrhpuAS9kgfDJw-nJI1N3CH6BGNs0vdzZNR37l1ruD4DnfNRfxsBXZ3a2r7FUw-uAfEqww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5d0e59f4a.mp4?token=F7-uQzlf2arSDR7bFarlMh-n01ZR3JNnfX_w4nj-tOWL25-bNbTKHYAdMUmDf9z7wVeZtzG-8OYySODn5HTfrY7g3h2-9LRXdCGwzZPkQ_JbZi8YjKIoIrlFPG7pqb5YSQNShb8Oy3Sa969MRF5pooMo6Cs_GZX1k2zlBfPse7Xt6kC3L747X7jwh-Br1RKQh6KwG6IHVdHHQA5omOlBTW8TscFLlg7Vm8lpEeF3TzdRQw_tRMeSuX0lz40-nHJilNW8p2pbdEhCFITtmrhpuAS9kgfDJw-nJI1N3CH6BGNs0vdzZNR37l1ruD4DnfNRfxsBXZ3a2r7FUw-uAfEqww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
کل‌کل پرزیدنت پزشکیان و مجری برنامه :)
پزشکیان:ما بچه که بودیم پنکه نداشتیم
مجری: آخه آذربایجان خنکه
پزشکیان: من تو زابل خدمت میکردم
مجری: آخه شما میگی وقتی بچه بودم
پزشکیان: من تو زابل خدمت میکردم و پنکه‌ام نداشتم، حالا چی میگی؟ :)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102940" target="_blank">📅 01:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102939">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22707bce2.mp4?token=EJvLz6azUOpOZrvUUJgSvtKM6zYWJwdOMMwZ_06J11cH1sGgF8A-7JrGLujlsMBcRsr5RxIEf0P9Ew66S8N9_qk7ci61Hj241YPpeCMB93yErXJguS97R36LBRY5dV7w8vl7PYz1kJWn5UTO5GHVcK5sNY1nhm5xwlCa5JylAYpEvQOlzOR5EwNNQ2GyFIJtn7DsIa3SRFZSpBxhUg4ut5n-v7cLab3fBsx4OcY7boC7_eLwCbB8qiNFR-77_cN-OOaVb5OjC4qBCG3-fwCUayvBOHG_sYqwsPD2L5bfUfIW1sz2oN9OJbVKYnFd5jj-E6wiH0c0d4QIE-74ihSTTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22707bce2.mp4?token=EJvLz6azUOpOZrvUUJgSvtKM6zYWJwdOMMwZ_06J11cH1sGgF8A-7JrGLujlsMBcRsr5RxIEf0P9Ew66S8N9_qk7ci61Hj241YPpeCMB93yErXJguS97R36LBRY5dV7w8vl7PYz1kJWn5UTO5GHVcK5sNY1nhm5xwlCa5JylAYpEvQOlzOR5EwNNQ2GyFIJtn7DsIa3SRFZSpBxhUg4ut5n-v7cLab3fBsx4OcY7boC7_eLwCbB8qiNFR-77_cN-OOaVb5OjC4qBCG3-fwCUayvBOHG_sYqwsPD2L5bfUfIW1sz2oN9OJbVKYnFd5jj-E6wiH0c0d4QIE-74ihSTTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
⚽️
جو پرشور هواداران فیورنتینا در استقبال از ماستانتانو ستاره جدید این‌تیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102939" target="_blank">📅 01:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102938">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">😐
آقا یعنی رو دست فوتبال بد اولترا توی کانال‌های فان ورزشی تلگرام نمیاد
😂
😂
😂
@Futball_Bad_ultra @Futball_Bad_ultra</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102938" target="_blank">📅 01:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102937">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bjZzkkUxqpYu3FfhzWxF6nMWzVOSAnr6zr8VfPIxZa33xYX4gwFlggrRiSO0u0P-9eJzNsgxbW-rQsuCYT4OBIuGj8vXLwtmLqcdMZPp3DsftJzFG2gmLLYZZQfFEz5VDvE3Bqk034kmPomk258nbM8kHeu9SAwx1gbI0tosFakPDKiXqteucA_DcFtZ6C08mc-etiHtuljJzvDqgQK4TN-t2_t26OIZSifHynvTXJFZMoZCoFZIp4nbXdZghTkXdhYNP4fvS7KCOZrhLqZo7SolKaSsHr2oMRqCQpw2VRfUOl4qVjzxtAEG93i1XjIia9Md_L5wO473tGsqokMUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
آقا یعنی رو دست فوتبال بد اولترا توی کانال‌های فان ورزشی تلگرام نمیاد
😂
😂
😂
@Futball_Bad_ultra
@Futball_Bad_ultra</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102937" target="_blank">📅 01:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102936">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UraRbGbS6d3BRTXghYGys9Cq8xNyyM1cjlVCYwWt_cdA23plwJLirRReIjQFRu4KBRfmnvNWgsoel1AQN0q_hrpciF3RKqSL_Xscr2RYK_fNv-cksWDz5MDeSKgIOmJ1qBLEj6cPe5zpJ6P3fmS30GGzMl_DXsHwskz7oUytjakgwV03XMdT3TenF0BdGbi83wSfXnSp6Y4I53y3ip18UywmfguYSrOv74WPco_bH7Co8uWSRMnMf7HQaXWN8n6QTM0UIkA7F124d5pvBKLhfoVKu7tZOJPbthYVVonOVXhL1axcXsVWipPg0UdelVhN9zd1p0xqpeNUDKoN-WJXyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
پپ چاواریا از رایو وایکانو به چلسی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102936" target="_blank">📅 00:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102935">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TombMm5dysHl3AjF3VxqS8tppv7WU0adaI8WClhZczF3lURybUBF9EzWESbtTW2_ujywdH8nYoH03lGdM1UsWTBcccgLQ0IK_N9iu7kQcc_Vh6mGPT0J_uFw6sM_XVRxbvoxP1r5HtyLkUx-MckdPrRQwCMaUSkIiRHCHz98kZXykR7mcZPiR_AF0Kmlck5q56dkW1lDPGNp7DXhs5GlA0ozpButIDKr3IzVaOeOqk2vtIFnqJ3gcmt1EOFOmglqHIJTe0aW72MCpgSMGXYQ16F2TpPQtMCJyXcYtXuwrvNz9CrWjRC0xBQYXcSHA9qr4xzno-sWJICIuGuzaz7Syg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
📰
فابریزیو رومانو:
🔺
رئال مادرید هفته پیش اوکی داده بود که حاضره ۵۰ میلیون یورو واسه رودری بده، اما سیگنال‌هایی که الان از سمت رئال میاد نشون می‌ده اونا رودری رو دیگه دور از دسترس می‌بینن! چون رودری چراغ سبز رو به بارسلونا داده، برای اولين بار درها رو به روی بارسا باز کرده و حتی با هانسی فلیک و دکو حرف زده. دکو داره سخت تلاش می‌کنه تا این انتقال جفت‌وجور بشه و الان همه‌چی آماده‌ست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102935" target="_blank">📅 00:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102934">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZspS7QNSL-bkDmwHvQLg7_64vrKqt2nx59jdRqC9FJ_DYRgY75BPwJc8HgvZlXAR6M4mwzheooa3T13aC013cI6oLj-MZjSE7DBGEYsKx-UliC2hsl2Pm8RCZhkmgq_elr2AT54K7LYH4SIA1PaO5BU7FlcTS2zYkKZ4Ji4KiqNYR007OYTluVuNpIiL3deItjBJUUHxIrvxzlB7DyS1-sYQk34_4iwU-YBiAZo1dVB8aJ0pw_9KOemlgaGXdLGG8CsrXFr1gFN6ugb4zXN_NDlA_Ib6aH8WIav2MJSJM4OhnhvhPFZShD-9IQ6BqrIk_Xhi9B5Ndbq8SVLcWBHePg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
از ورونیکا بروناتی: کریستین رومرو ستاره خط‌دفاع آرژانتین در آستانه توافق و حضور در اتلتیکومادرید قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102934" target="_blank">📅 00:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102933">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxZpzh7MMsbEkdkfOofuSbRGPlOC8zb0DS3pz11P71bCC767oiDNmZase0_-SRCCQfX9HfUmsYOmHuL_MRgK1OIMa6KtHaaUqoPH2QdPq2admgH5yoKI6i6LLAqeqORl3UEi-9tNkGUJgXi6_nVGdEmrLgRTSzzhatbHhcpEfTkiG8oicj4XA890aOmTOzDXzqrmoBQk73pwCvb47afxLhCdqg2AZbHoNGX326yJP5hqLshuJzca1oePVR7GJ-2vGyF0lL8BLtLtdAh1kVRo3bA3rVYEZIVMKd-CfGdi6W0u0hlvxeD0dtxG-2eCIG-EX15tAbfws_aRYhQg62ofFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
❌
گاستون‌ایدول خبرنگار مطرح آرژانتین: آلوارز هفته‌آینده به تمرینات اتلتیکو برمیگرده و خبری از اعتصاب نیست. اتلتیکو هرگز این بازیکن رو برای فروش نمیذاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102933" target="_blank">📅 00:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102930">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuN-r57rS6l56s0m4c1Ew9njiKGy_jutiA635qo4IToz8I_64sBKh-vkNNAvjegF9l3kDdnSBbYnANXJG928UEEPkVqd9luqc-JFzkNhAkTP2Xe7KkC4CY0F197eA5Cj9iuAqYC5_fIQST9tlurhzs8UpQwS6OfNivtQtSf9v1RiXD2lXHrRDb_Xepe8IpVBwxhSEgT6oD9l3BEOsv4gUPZOKWdt01EkVsSrFff6nc-Er1F0NHkSQtJD7JUtIUM3T_GEesKv7IluKtt8Hi_g6e4VM2n8j4bC5-VhMuxX3aWChB42epZ9ro4m_Vd8RCHBTfjeL3jwaoJvJv6M2jwxgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
باشگاه هایی که بیشترین هزینه رو تو فصل 2026/27 داشتن؛ طبق معمول چلسی در صدر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102930" target="_blank">📅 23:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102929">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhUG2Wdrwa9jzJax7FN8PP8ckpIFwvkevRyyBNa_60s7zUNpMkD5DXgAzL1Vhzv7p4Uf8yFViwKAAkAuku_mFRbajmQi2Op3LxuHNNSq98EMX0X8xip7fE-qQz8zmoCW3p41kmLjsxCRXyVVRDA45rxTlzWJoUl4d5JBhthaLML8b3s8DOO5oaHEjzk99tZEnA0qL1OxUum_jntZUyUADClML6lzX2cTEa59TRJ0m2YSprKThyUo5WzHNLKoXD5Lykq-GYh1U3YDxhtFhoO65DdHU4pN1M9knJESOigU0KjEsxwp4JKprYfGrhttDa_hX9vil4-fo9RLcZh-bulXqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
ال ناسیونال: تیاگو مسی از همین نوامبر به لاماسیا اضافه میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102929" target="_blank">📅 23:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102928">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzKyYcFS-ydQODAJCDHFsXnChlpokBCAjjfJp6tdTvogZj50NOU9L47thPDo0lZfbjKENg5h8wCsFsql0XzeeHoPc27EtdyeDydNmliZm57G0nZbjYTGlR5rWTQQWTS4dANmQvTI2tVX2ulXUEUFopVlEG48bZRhsSzFD_AqFLsiGmvhk1GO164zeb_UZxN1KyJDbxKtfXvJH4SS7G3nWfwmvOh5K-8BdvMak_ksQnOH0Br3tTmY4aoAWTYWI88469l1ABg3CjeNXdb3MSgq8bpc8KZgWQ5iRG3_cvtH-fCSWFOwhn4W6das5oeS1nJFea170hJQtZqlgo2JdfNGKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرف تو آرایشگاه داره موهاشو کوتاه میکنه بعد جرارد رومرو بنگی زنگ زده ازش در مورد رودری سوال میپرسه
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102928" target="_blank">📅 22:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102927">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqu9wJui-jZlYChx1QnCSA9E8BiLvbNCRgaS-Y3vM51zaD8KPmcQZH2XNjhZJaza4kXpqrt8IOT19UIw533kBpRGHa9e_LNsAD5S5fhujXxoBdl0Gmn6eYgqd__kI6sHbs9xtg-SXgcM3e9K1yfNqHuBVIgy-Aex2uzTaTUQIdFxP_YrajE-pxDVGwpj4wFUv8hI0XXWeL0st-g_qCdhLgQx2sjoFCWUuNAjBGC8OsqCmbhoyzkmUfCsIrzAWoH3Ptw58SY97Ya6kEhbWuUUidbE_I34Ecl44cgbWmWxrg-inZgfwGeEhcH9OTAiIncUP7S1_x6ILEfhN6viuo41lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
⚽️
فابینیو رسما از الاتحاد عربستان جدا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102927" target="_blank">📅 22:49 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102926">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0t-ltLoGK1PSN9htPbI0wcE-Mayuyl30SHRaEFHi-TBupCuvZ-SkCbZDKbEMezssnR22dHfVP7nj_7lOeuO6upePQ8OWx9ziLoEYOh9ATIovI3A1G-oq9TgcNJF7Lm_rAXrFq2PgE3VUBamTU_3BLvKCtPYxT7psNOqpEVeP5fPvJ6OnKKwpC7rJeKYgaTLxecfXoGAq6T1GCU0E3tERorOoWRpfnp1-6hab6YYfjfNYE29wB-OYFXb32wHXdlhKzsTYqsnV0yDfw_uFuMeN8nYAjpk6LVn2Y8CGKOZtXaBnMMmR4kZS2-G9vr7kSri2-1MOm2Old96vFr8E9kRNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات از تمرینات امروز ترابزون اسپور.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102926" target="_blank">📅 22:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102925">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-8aS-jkpzneV_7wCJkquVqL3UKR6L4wa4BZDS4vKyWtDBvNeXLWAj9jj8eQMQOYGwe-MrD4swcPPoKwLus59ES6DuYnTETnd_yrb0Sj5Ob6xG3T9gZIxQkYgG7J4jU64J8465_groojznsrvedPd8iCzfXQJsrn_CxuoUVwGybUYpUkilOKn9Nisoz2EZ5f9uxdimoA1sJN84oaU7qBf9JxNxu2KOTozycKXacizi7lHvsC5IwFoRByzAxOZBHg6TdDbvx3nFm5U0vErwQ-bgyuaGPhoW_P5sfFo3oCz2RMc2C-ngq2uA0YC0PYwELuXN29X0C-D5_Q2LVpESr9Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
‼️
وینیسیوس در اقدامی ایرانی طور تمامی پست‌های صفحه اینستاگرام خودش رو حذف کرد و عکس پروفایلش رو هم برداشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102925" target="_blank">📅 21:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102924">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_TNw9L6pKt16_PBQsuz0lbRytXVKOseUcHOayEvyrxfx7fsVbC1s1sXgJqOJRY4eDWJUJVvm1oFC8cWDaHQGYT23I-eHt1Ki9c8sENhjtsfjReAxVteszhYmhmaCb8G2rw1rCUa3Fw5XVOR3YFCNE1UCPgPXqWoAxSvBEmWzYF4mdit97_K9ZUUXDkD7yIcwAj9uWPlOdwql4e79dqFasgXICovdAGI_0uPS8Iinv4SGys_0u1_RazgSo6GmQubk_bgr5-KnJio6YMY39A_IcJpzeWg9TTdw33Fmvj4YM79dDFdgxSQoJlRCBl7Jlys7sVdgB8rLh-NOC4vyKgn3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
شاهکار رئال مادرید تو این تابستون
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102924" target="_blank">📅 21:18 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102923">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIfmbWYlHk6TY3VN-XhWoZp7T-esvdCRqVpG8hOW86OlqHXHpdddyNZB3MQf4-5FwMXztYygGwqFTNdVcoBY9ez4su9X3G028jynRgwxCT1Ya2lqzCLeu1R2VRU5nJv7y8DZtDukY-tusLm5Bh-YmE_PygPLYe-Mb6zGrjkKMxAmdEYsr1VSmWJc5jQhDgljekXQnAayKo1WyHNIX1xBO6tsAX36boNoEJ6gHtXs5teXDwZF_koLTDO1afX3CYTAXwsHDXMSASCsggQAixGp0fYZMqXfDGe1J1vjj0so7riJNwHYzOkJ4L4K6hUftGM0rIAH0hvgKZ9MLZi6V1Cukg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔵
تیم‌فوتبال استقلال در آخرین بازی پیش‌فصل خود با دبل سحرخیزان و تک‌گل آسانی مقابل استقلال خوزستان به برتری رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102923" target="_blank">📅 20:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102921">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dj8HCYpoTiptzTMglWuK47wGHZKW5m5DgXI2QxtOgB9uObz7vmzdn4bdjfRf92UJEWyN5PkCDtppIbyoBCAxUoAlt1K3xqyApGPgJo7ulyeNE8Q-hDOtrkt3iBhDdVRjS_kJ18H3cG28FYYCx-yoAgK4vRHlilbH-Vop_XX4iuOF5ZVv5TTwkyqqylYZNIpIVRY0tjoTGQi_XHOx3U2y1xngPb01OqSFDhQPwyBw5K_e4VBOOD0lsie85yi9Vl1bwT-nwy6-s-wXh52aV2QkEiEpazM7fYQe5wuZH_TzNHlDj81mGrZibU4ihYCAlUsrDcYMv-92EXVwuo8A7mJXog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوووووری از رومانو: وینیسیوس جونیور رسما تا 2032 با رئال مادرید تمدید کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102921" target="_blank">📅 20:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102920">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZ0ZfAuDXXD1L6eRR5189-pnC867SFeH6m7sFyOTQAgIqKWd4EovDTxtiaWFGcu0GaAccQvk9QOX_WI14evmk6Fz5S8R6IgdRGqiqDirg7S9Rp7UBOSFOIRWagE4MGLBncn1w4oyHjibolEtWcS91GYmqxObTRwPS7QCxm-lM2gywq4eqK7229miSKBtpRofjuKmscwCQvNpQxEuC92IyOD-aHkiM7ab5j_Fl999APqJF5I1-QVlcLSt3sfn-Pfe84l_buZ_kMaFAvxAU8LkKFpT5r1HOJ-49986N_6zxcL3F-aRbyAiq35-XC1M9-bXxhmhUSGdheKmmZIlI4kpUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
#فوووووری
و
#رسمیییییی
؛ مگنوس آکلیوش با عقد قراردادی از موناکو به پاری‌سن‌ژرمن پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102920" target="_blank">📅 20:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102919">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U08p9JKPjjR9BaF4VzahCZc9qsviFKn-b6GFgxlT0VifsB5Q8WvUTh1loRACR7sa7NsSzsAHSJpmGp9o6lYybDvgOpMMso_1-t0OL6zh4V0gjy9Ou3Q4XkF5Rwdjgc0TnRNV9vWx9pmo4L4vjSUM7xZDBKRz_AKLV797cbodudok5BSudmvfIO1cFOaMaZtLHUgjd0kna-CumbXogXgcCS2k5wOzlwPOfNwA9mR2_gJCq2AJZTwyM64ulm6xL93hM0GSlxyLGVF8OKk-ypaR-rr-3qOs_6pPqMR8UqdGyOzjxoTYjSg6J2tIInPMo5hHhoxal1_Bcu3Qf5q4z3P7ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👀
🤯
خط‌‌هافبک فصل‌آینده بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102919" target="_blank">📅 20:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102918">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiKQkFc6cBOZnrOmom4MbVXn7rQ4M3C4VIozz5B8jwkgAgLuopFWDhmWfjI8Z2IUtIjPzERQvlGEcbdSDDyMwuNDjmpVRw1uPHxDycAm-oDVpaNY13qT3obo5komUf278qy7nIKVFr3K_QVxJ4xZAM-7GPAgqCk9LDbs35kOwGU1TPffrHxhuH6dyHinDFpSQw4CnXyHdPqVzCy396amBB_hTgt2f8XRz2YtidagbFfdFN0OfetqhwB_5Hdzrgh4hLNBkj8LUJQOFrJriEJeH1ibL_RQy-Dwy55sMwjI8ARdh8RCtlGFoAuL24hGEFoMfPmahMbB4Qb7q80eyPeUbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشرفت یعنی ساپینتو که تو ۱ سال از سرمربیگری عارف غلامی رسیده به سرمربیگری داوید لوئیز
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102918" target="_blank">📅 20:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102917">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHpppqBY75zl_H4ikneZ-0zLcwcW-TCzrpP5sy_GzD0-VAn5zHJrTfLLqr3550t7m-5SPbW67G_vwtfmUk8rL-lHe7UvbCGmJnHL3e3BfcFTjYY02F0SzLTUyIIVCcBzyM-6yEEF0yRFzT816yd8-teVuvpRAa-EiveLLsWTmLl1crh_FguIzRaq-g9Ljkaja-RvFx1xuhdi6jPXt1o9m_kIlmaCtgPOHdH0XfqhkJdiQIle0kecAmnbKGErB4IXZkZtnEQMMgmp47c7IN4_wNggCTotIn-i9iSS2YGBoS3iKtxwF3ic-16UcwfeVPQq2E4-F-xjIUeQMZwNvS9R_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
‼️
هافبک های فعلی اسکواد رئال مادرید؛ عملا چند تاشون فقط لیستو پر کردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102917" target="_blank">📅 20:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102916">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRjUUsAo0LRaE29sH81CfeQulUrgzT3CF1kCBSNJy4cIRcwj_07DH8x9t6rtkISOrFXRWHgJlU_NBq4ySd2o9BHmT3YTXMtCS3zo72K10HYmX29smErzeP3fu850DgQ4N1UtHdDEE1vltASmBP-SX9NW25pZeAxSuv4gB6nVdJkXMid75raDaGbYGlZxdFsh47MTcyZQR6XskGTv0hw1YfYBY_NkIJkFKI8vWbMH1-cE_gQNl3OkzPWGDThnO0tpDXUwBNHAufdi1s7zp5FTBYu3aA9cUPga7jReWL_JDgdDkwwN_XcZfUhdiHLMuEHhOBHmfo_ULgUNF-C6kHMbVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری
خوزه‌فلیکس‌دیاز:
🔺
🇪🇸
قرارداد رودری با بارسلونا به مدت ۴ فصل و با دستمزد ۳۰ میلیون یورویی خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102916" target="_blank">📅 19:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102915">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLy4KYY31I-ArqjrVwCsppHEXO6N8JOo3YX-23fSjh23j_d76FwAK8fkWv1pEwg5wqaxrFBS2_C3TVsvymAwK-jgDdVOMezBV_3yHVAHawhgcI5RYb9rqzXVZiFG9qN55w0kL5LIwin4Q-LMq3SCwt0q8Zqqu1AuhyRuHOH86vba2Lp010VzRTT371ducvkfmDzYgKsjoelcz2OYSZK3McceVSYxI-Xp7u72uOlgUj7N6YTF4TUdb6dDgSKEXyud2fb4iTTIvw4XG-A58V-Hc9OyIpUHNImN_ZUzU3gTHTwEySSTlMMfZqOEgRCJYHr2xhrBOOklzj8sgNN-9Q6sFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
دافید ایبانز: آلوارز هفته دیگه با سیمئونه جلسه میذاره تا رسماً بهش بگه که میخواد از تیم بره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102915" target="_blank">📅 19:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102914">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pX49YDWZtgKpdhP9hpTtFmqbPrqNXVpCqOYsM7r1aprHNZECj6WDkFwTXpC1gLeiClEFtgI3M-vczcde4EuTlN-QDtoSjsrsImjWDJT9d8zQmfAIKe4JeSKSA-o36pwfkwGGNA9eXKClezYdlVBhO8xBEOSUbX29h9ONXFvkTwU3a4vh7JEOcPu8EoWpbYWamLhEIcDvy8trFrBK2MoEvxsZr3TMbqScRMRf2klLqdwWYUZkV-YKgv-k0zM0S3uW2wDXd-7VXsVqvxeJZTCWiguHRjqOo4n8W83sl90EvFDcGjD1DMLSY-boqFiDtveam7h121-3zhoqmAGpB1mXJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💸
دستمزد محمد صلاح در ترابزون اسپور:
🔺
هر فصل 10 میلیون یورو دستمزد
🔺
هر فصل 7 میلیون یورو پاداش
🔺
20 درصد درآمد حاصل از فروش پیراهن‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102914" target="_blank">📅 19:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102913">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuCDm_mcu2waDrJy8v4DBEIxG48i6g0vTPQdIRNiFwTOeWRp2hDNTdUnEKz2EdCwHnr0nfPIe18IaYNwUpeocCD1lyjOiKk9yRUj3YvAWnrZc6yeBt8PsdccW0xKi3ZzUKU_feVwuqIXFwNtPuVFNwuLimGcit5Wz58QEGGyKfTrbx0Qqr9GnAcwLb6RaEP9ouGVY5seN_Vr9h7W4iT0QZKAyVmQGPhFt-X6RWjZfotXObReugvGbkjp0BgSfP71E85rYbqCAkEJbrtAHmLQinJRRxdnNCz76-4Ia8tEhoCsFTT9eHSIScl02Bcm5A8Womo_dwCBrmdq3Yf94omK4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
😐
دیس‌بک ممد رضا گلزار به رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102913" target="_blank">📅 19:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102912">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vlb4LiUG6aXVybOdxpziWoCwz6r6HfYQeH2Sq8AWOwMYJUj9ze6OBNQcrC_-rO0-R9T_ptrp2lyf3c_FncUAz80q5UdBEBZqH3GCn4GTzwCBW3Q-aNZK-VCK0ryzbzCbjMZ-4o0sWN6CQ_5GBPRJEYQB9O3pd2YovPG9QMvrSbc6QOKsamrj8DIWxnBe3UgqLRl_s78h4pGQQUx-mAfR5Ub_1nZBr2ML76hkN5FcT2HpvpB3lNlihPrGHVcO0KH1hrMYdKj-CCDXb5cuO181Hqi2UWsMuUOtX_S7zeWOtjw1XYQm1rXy3H9I4pO1Q2kzgcrSnGfQE4kiEtV5wgQN6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
#فوووووری
؛
🔻
خوزه‌فلیکس‌دیاز: رودری رسما به پیشنهاد رئال‌مادرید پاسخ منفی داد و اعلام کرد که خواهان حضور در تیمی‌ست که سبکی مشابه پپ‌گواردیولا داشته باشد و بارسلونا بهترین انتخاب وی خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102912" target="_blank">📅 19:26 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102909">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d1HPUEzPMkpsgYA_kWPIrKbw1QoduBlC2gmGb75T170MFHZTzKiwK0Gspd-RPsr06kldR4UNogT3Qp7O5iZtOTFRTClSDExkHJfaOgIM9WYX3fWey_dO79JWeUzt5gvBYujX9n3qwB8Tm3SAyBNJYuc7Y9kZ-JL5lq7yJUopmMEMmEMIoB6fvNIqCx2LPu_7_CJKw0E8dSOnxhWyNzVIkZL49dJwUPTNHmjt5moAWG2_29L6s95brMY5ScuwQCtXrH-WSU-BYWysx7kqDWvjmETuA0BsDoUeIr4MJ91q9U8QIAxwfFoSgYHrLazr6I4U-h8JHhOHs1tI3yhaKWjyRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQTWvc4qEMbFbIzI0kLURC9ZDB-eLn8CJYvlCSGEf2EqdrcD5dUDk_V8_yBNC5QpsutBBSRH5JPXpGvLojYxOvnkBiIVF1Wxi82f51mDYtRb0EnKBfdIXZEZATrbv_wr7lJFDehh3HB18560mcBRR5NzNV-iRTml_P85jwkmHlU4tEbQe7Rvx3oHjSD1zuev3rEPNMjz9k4zrgg5WAwaY7RcA-WW9hhsvOI1wFrL4Y68wHFaJTQvTO2XJmHlSJzyZE7RoMWuBsZiGTEEFMrfa-1ckW-GnLjK00i_jc3OH78zr9Q2DbP_e6wfoSqqvkC5l56hU4YdSb1DPq-cIWtdng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
شکار لحظه ها از امباپه و استر اکسپوزیتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102909" target="_blank">📅 19:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102908">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4e56c5aab7.mp4?token=hBG25i0xPmXHFE2KtU3ovnaBl3MNlRvj14M_5WyRq-uxfTXYPQBSjIkpJ-_ajIud5UmhoNbBpoIjHnadKC2LF121sezDvRRI00RavHRYjipamw8JsLZfmB26dr7PjjbSCz4XizCHbcZ87LolE_qiJYg6_Eh2oSbO2Ct2QH1tP35u9gqktPZPZUF9gDnxqw_32xgiypDE1ilDIxBSbRYwYK3bpzbzFk3-_vBAL27NcvO4DefPh0fV40UJY2rcJnWZB5ykCdDBK58uJhwVGmHOcaucSsxUSj7XViOx9KnXUCJDDqBm0lbmC_Lsn259b7He8XNsw44ion80zmKwhJVGEw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4e56c5aab7.mp4?token=hBG25i0xPmXHFE2KtU3ovnaBl3MNlRvj14M_5WyRq-uxfTXYPQBSjIkpJ-_ajIud5UmhoNbBpoIjHnadKC2LF121sezDvRRI00RavHRYjipamw8JsLZfmB26dr7PjjbSCz4XizCHbcZ87LolE_qiJYg6_Eh2oSbO2Ct2QH1tP35u9gqktPZPZUF9gDnxqw_32xgiypDE1ilDIxBSbRYwYK3bpzbzFk3-_vBAL27NcvO4DefPh0fV40UJY2rcJnWZB5ykCdDBK58uJhwVGmHOcaucSsxUSj7XViOx9KnXUCJDDqBm0lbmC_Lsn259b7He8XNsw44ion80zmKwhJVGEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🤯
کصخل‌بازیای جرارد رومرو خبرنگار بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102908" target="_blank">📅 19:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102907">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e118ce024.mp4?token=R3vMw27R3-SeMaJ37pYWJ43XECNliYmQe0ZTWvuM0SOxk6mqykAHIKxbQ2fcr81bkl7u1WWpPNwkHgzFWJBjfd2yq5yJyD7B_h5LqhxcRw1ZRTBIoYMTqt--rrLxgqYxwOXlv0lkCFDQytM-hjw7naWaRmUd3D4jcCdtyrMcPnqVyAFO4PXGicUCji4ga5-1iqiOXSmMvKU4RK70xZACQ2vKn8-AlmettU9JxeJLPJGgwD0ij6epCdPO5OMpNwkl3GysvwbawDXS8kLqraCKh9ONCEk26mme3ylWqJMWlBRJZpySyKKoyREIIJ-pL1Jzr2IY0pgTujWSOLjUGHZVUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e118ce024.mp4?token=R3vMw27R3-SeMaJ37pYWJ43XECNliYmQe0ZTWvuM0SOxk6mqykAHIKxbQ2fcr81bkl7u1WWpPNwkHgzFWJBjfd2yq5yJyD7B_h5LqhxcRw1ZRTBIoYMTqt--rrLxgqYxwOXlv0lkCFDQytM-hjw7naWaRmUd3D4jcCdtyrMcPnqVyAFO4PXGicUCji4ga5-1iqiOXSmMvKU4RK70xZACQ2vKn8-AlmettU9JxeJLPJGgwD0ij6epCdPO5OMpNwkl3GysvwbawDXS8kLqraCKh9ONCEk26mme3ylWqJMWlBRJZpySyKKoyREIIJ-pL1Jzr2IY0pgTujWSOLjUGHZVUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح فوتبال کشور اندونزی رو ببینیم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102907" target="_blank">📅 19:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102906">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXu6tkJPjg7_av773oeV5xbU6JQu_vLVIVUXy6Otsm3-Co0H6wUMoYTTMb9CpJrRN1bIgw73BH-_Ot_GWjyPFXhre-tpj5QB_SLbrZUkg0y7SwRMUcCnIx7uiJgOub82ouljBl5psRBkj1_Qc1zpD1YeRozvc82Inrt2BOVh9oUtA-V9tohE29ASfbsvF-lexwzOJhIDYOeU7ZTc1LWyyn1oA_zglIxSIchFItu9R-wxQsQPFc2rgXxo1W-Moehf_JpGY3ZbgumS6qaHHXr5CCiLWi4TAT_msRQDc-U3Ao52lnMjsOww5i3L3AclousrVeF7FCx4zo8JJV06ZX8-mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
دیومانده گران قیمت ترین خرید رئال در پست وینگر راست از زمان بیل شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102906" target="_blank">📅 18:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102903">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlGA1kdujnfABs8QZPUNGiiytw03ERHtScTZspogw2mZ9M3bG8RFREYGHRMarvyiBvF0SdePz6brs8TiG8mz21ds5REqLUUdN_UPf11-F5Ocl58exL25vZUL3fH6bhTm5octvoeucURsbp2ufBU-bDYjyXF0EtOLdtnq1StX-Pwflzg6ymN7VmoixE5Xuxd6j5G4sevYSxbNe-VjFZvLvAJDZPfpa6mCJDDiVCXX1zYaXLEDXenGPSfq6aKCxgTeM6nUvf8XILB7go5C0zOTWaae967KhjUlyW3kKXaPIvoDNMcGO13UWkVNVpzxwoXGoIcLoY3HSIl8ySL9XDpC9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇪🇸
🇪🇸
فابریزیو رومانو: رئال مادرید داشت روی انتقال رودری کار می‌کرد و فشار می‌آورد، اما بارسلونا با قدرت وارد صحنه شد و حالا کاملاً در آستانه نهایی کردن این انتقاله‌!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102903" target="_blank">📅 18:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102902">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🗞
🔥
🇪🇸
#فوووووری از رومانو: فلیک شخصا با دکو تماس گرفته و گفته که تا آخر هفته قرارداد رودری رو باید نهایی و تمام‌شده کنی. دکو هم راهی مادرید شده تا با ایجنت رودری مذاکره مستقیم داشته باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102902" target="_blank">📅 18:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102901">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siQMKiNlDXFcCQMyyz3JQtbmX58PCiuQesG0IIlGKIIIVKR-p2J1RGpqmCxgPPgaI_oiWJcYQZfuqlHCLfXf8oa7YFHCRC1KByZGXAWYiq0bqLaoMJqWlCS6RR3DFP9HUsX2Joic9xYPp-YdXQ2eT7mB7noupZJ5GQmgak9j9yIhNNaM9IipkyFoWB04N_Rmhj4WeIJLF9JvVgNGEIOIMNYOWppku4UY0y5bb5xTUbPVS90APB1XZwRTdrJQ7m5Gv32313eK_OvGVMDqvN8fMYfzZrJjzlnbBiCURFCk0iSMesfbg9gBcXTRCZN49X4kwx594FWfJHqNBbsM2IuLpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🔥
🇪🇸
#فوووووری
از رومانو: فلیک شخصا با دکو تماس گرفته و گفته که تا آخر هفته قرارداد رودری رو باید نهایی و تمام‌شده کنی. دکو هم راهی مادرید شده تا با ایجنت رودری مذاکره مستقیم داشته باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102901" target="_blank">📅 18:41 · 15 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
