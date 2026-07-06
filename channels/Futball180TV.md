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
<img src="https://cdn5.telesco.pe/file/fSsmYNny0YvDsYuPTvA9evFABbDAKoMe0NNYiteGpzD4vzJ2WtJZHB2ijmL0rsudSE8z7bdM865l7teX2WoYorq3mo5zhOFYQu_D3gh4rD3yL5n4nmuW3CCHsLYZiCyddUC4GvExwwI1fmRVxXCPg6pw6xh5f7xOVc_iwmyAs3ZGtqPyWDdGYG021WH7Wqj4uzqAB43CFtvLYN5vN3slkyscJrBMChMGAI-krAD3Wjqn4Itvyh42WT2QKya7w1QozpKZGEZozHzRfZEGv8LJg_KqUJRdDvnFvfiLOHvv6zJw-loQCqMMD6Kv_UnWQ2GjxwnAWkPS3ibE1un0i1wenQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 631K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 03:28:57</div>
<hr>

<div class="tg-post" id="msg-98468">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-7EctLHKMrfK6909jqf3gF0P5ZHSOGR0_xgC0-M_PEL2-hA2FXPFndlILt0kU6xUNW1rodpTuxovdMRm7U46ToVug79Iemq82mfeGizNNA9nAJYHCacpOIsxDFv2gVy_vmsBgscWXbIoFRc68BQLl8byLJ-6SmfnP-m8OGcAbF1Ehj-V5C-UcyyulDxrgWMwSqfz5ratSqX3SVZE9fthtDQAEETXy0tvddxK9H2Vdm2hvYKSyoR4T7WkpErsJwLjq60r2FzbNXOivJ183JY2P2DZMP7mZgoWvCT0r9tP4TjKY2HFyT9j465UtplN2kp98McfGhKC_S4AKFd3wWGSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار نیمار در تیم ملی برزیل:
130 بازی
80 گل
58 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/Futball180TV/98468" target="_blank">📅 03:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98466">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M4f7f1DvwBJ0L7ZT9XyNNj5sRtGEMA3q5Wvsu2GJLQ2TOrJS1BW-8oQ9tWDdmYbkWqaFwSpiOivuoejWBckkbQ8ZbvDrYGEdgZWybX7AWYP1gsijNKyryr2ScnN1oWx1Of8O93YCGbF8Er_2o7Jg7TOEGbH61amM9OeHcw7HmtkLa74rXnyHW4g33TnOtHieVMF22yuyJM2Ojtr2M2qlq6QfuS4S7dIaY7gfPsuOlUvqfxHIjtlN5caLqF9TUhB2PFsKnNHVMcO7iHEvJ3Uq89FUXiR31feP-h6P-0jrOHgh0h5dVoBP7UxEJAJhbMZHO0CiEwtxzBM2IlardnI--g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BdGFC7v0MMU8F32boCSMYpJXLlmfG6ou3_Bbu-Qzap-KWJmwWWvJkpmolqtvF5ETl1CLh0WY07Tu4bt-xvdbMlRzKmtFoq4zna574315nlclbJ2TyMkMwGzaanhWU6gdtN8RbDsvKFg8dxIAfZH_wGIvQEoqDzvbPzm7sZ8w1C9W-rwYcg6FeEdfsT-3L2mtHBSkwIAV4fOFU1mqCBcxM2nFWx1bDodWACDIaue261Ai1thFQB7wGSWyWQqflOlw7_yi5xEWCc9NqpZyvgndql-BbkVpVsT7-Vwpr0YM5q4jg7siBNWWAjRPJ3nk9mn4ywucwCEkRsoL-W0H1w2g6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
نیمار رسما از بازیهای ملی خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/Futball180TV/98466" target="_blank">📅 03:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98465">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c1d5df3d.mp4?token=CffiBmt09DH2nhUlhnB_d9gfOAs-Cdwx29oGR81INIrsoujT7uWVdI7LYqtmR92DpNVwRDiPJvbdwA3StREsKDmbyQLzK4tB4c1NknLsgCJDm_I3snCo6Q2-_QVkWdj6PPxLWZa2NkoKzD6d6lvXa1oHrnub_IGJNrljcxJDD0fUj4yNU5HMKJPQoDu1w7Agi_tWlDcqz_mcWiISi8-qhhvnL6JKJz5TvgaRHKVSFoWoix7k8_1a5aMX4sKVI9tF-Dfxf3NtX3SFVCiIOVl8OWDrer3oeD9UsbPMQgON9xVRYrc-xEf8C2GOhLvhR5D-eQPYkGKXlcYCFX5XMkXPpFmLfhUOe6pEu4RomSyazNOxC3kGoA-_6EJRzLJYF4w-c0fCHTaGLhVusmYHeq8dmbgnpqXWBdIgujUKI-SWeLZrDbz291ZbhjYEQku0Ux4iCOUVCsuQXsE8rb_KZ4DFcPkJnMxCDSgORXGc-Y8IAr5ybj9n7yqidRYZNSskQQCmuytGti9-MEiaY0jcz5LtNvtDzrsjFLAWI8oLAOM-mH9_37nT1pEGZQOMxoP_PkzjqSnH19wKR1TzNHObEmyKRJeenHBAY533vInrHmcSWsz2Cnb9cg5FfclXOa8mPoKyZ8UkfiutGeLbx4zU_TCqNG3CEarcj7oNbxXEL9KYWVk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c1d5df3d.mp4?token=CffiBmt09DH2nhUlhnB_d9gfOAs-Cdwx29oGR81INIrsoujT7uWVdI7LYqtmR92DpNVwRDiPJvbdwA3StREsKDmbyQLzK4tB4c1NknLsgCJDm_I3snCo6Q2-_QVkWdj6PPxLWZa2NkoKzD6d6lvXa1oHrnub_IGJNrljcxJDD0fUj4yNU5HMKJPQoDu1w7Agi_tWlDcqz_mcWiISi8-qhhvnL6JKJz5TvgaRHKVSFoWoix7k8_1a5aMX4sKVI9tF-Dfxf3NtX3SFVCiIOVl8OWDrer3oeD9UsbPMQgON9xVRYrc-xEf8C2GOhLvhR5D-eQPYkGKXlcYCFX5XMkXPpFmLfhUOe6pEu4RomSyazNOxC3kGoA-_6EJRzLJYF4w-c0fCHTaGLhVusmYHeq8dmbgnpqXWBdIgujUKI-SWeLZrDbz291ZbhjYEQku0Ux4iCOUVCsuQXsE8rb_KZ4DFcPkJnMxCDSgORXGc-Y8IAr5ybj9n7yqidRYZNSskQQCmuytGti9-MEiaY0jcz5LtNvtDzrsjFLAWI8oLAOM-mH9_37nT1pEGZQOMxoP_PkzjqSnH19wKR1TzNHObEmyKRJeenHBAY533vInrHmcSWsz2Cnb9cg5FfclXOa8mPoKyZ8UkfiutGeLbx4zU_TCqNG3CEarcj7oNbxXEL9KYWVk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت چمدون بازیکنای ژاپن با بازیکنای قلعه نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/Futball180TV/98465" target="_blank">📅 02:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98464">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/Futball180TV/98464" target="_blank">📅 02:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98463">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G4pCn0SYZqRMdDsTeuWXT1fV3yZ24y8zXyjyFw1cUKm0c2XkINlKt-amYMD1LUI0oJFbdFYcJ_IuU8TY4JfAwIoiqdDIM0Hiuj71LvNDc74U-mnGoORFEfcMGdTAnpHNFZxnQI5dHNiP3HVr2qRWQLJCdW5Im16dk2y1kDKqlr6Kirgy5wbBUBQwRPCfc79KSXhKL0uN_qHBdFjOZOiBbOFP1Q-r9VHTNkGV6GkQvLefoNheQ9z9UtK2ncQkyhHgMgauGjMCie3-_UZJ0cKfAscya-BeNcVsyx164oROBvxqBuR0b3CxhysGkH841O-iSLJrzVNssOTylufntQV9OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/Futball180TV/98463" target="_blank">📅 02:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98462">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/324c5044d0.mp4?token=ZouXi6U5L70BJF2f6YeNeN2qhLK2PjvXroDrDRTtx7BCVYsn8nxIr9JrZjBnF_h5ui8Lv0h_FZ1C7dfsIuRA95U8i1x73q08XKAu9CVPxqTRqWYAQwP3pMD54yP0qFmOcjRe2gxM6PTcPkZknXxmT9FY9YuE2lJ-frL-M8A23XFTZMkU_m7gFmeL8tpnMTSG_KaWT-gj6gZFJYaP9xr_fLHhmmVs8Wukrc0iFeDYnfXHc_CSIgbooneJRPoeUA6L1c9prb7oOLR12Zl1zPM62e79UfAsahjbchqAu9XcKItqIH8PTwj7OoPIbL80jo_nPDRWL5JBN7KwrR0ICNY5cw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/324c5044d0.mp4?token=ZouXi6U5L70BJF2f6YeNeN2qhLK2PjvXroDrDRTtx7BCVYsn8nxIr9JrZjBnF_h5ui8Lv0h_FZ1C7dfsIuRA95U8i1x73q08XKAu9CVPxqTRqWYAQwP3pMD54yP0qFmOcjRe2gxM6PTcPkZknXxmT9FY9YuE2lJ-frL-M8A23XFTZMkU_m7gFmeL8tpnMTSG_KaWT-gj6gZFJYaP9xr_fLHhmmVs8Wukrc0iFeDYnfXHc_CSIgbooneJRPoeUA6L1c9prb7oOLR12Zl1zPM62e79UfAsahjbchqAu9XcKItqIH8PTwj7OoPIbL80jo_nPDRWL5JBN7KwrR0ICNY5cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت کارلتو آدامس  بعد حذف مقابل وایکینگ ها
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/Futball180TV/98462" target="_blank">📅 02:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98461">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/J46_TbQLwDtYZ3gWuInTmloOowUgc4Dk0nHjErw7uixPe6hMs-FCxeeGV2y2jPTeEyyuxkTGoPmytC4r1s7oTokx6IlTc3TCxS1c1pmBAtWe2elVZUDL8LECZaOMXzNV_tBUQ_UEGwqh4GEsENgjBpeawQXiCJToyGmtFAVpqxW6nNzd3pV2Ltcj1VoHdiUa-G44H-jy9RH0gSvOV5PdUg07TTpKOUbESpdqz_W8gL1W7PCwbuIN2ohvNgXP93fNDxehgDlWEOlJvLBGri1J-5dH3AdOEsv1rhxkuIfPTsEM2NP9jeL8iCn6W3-QbokPzqA4AVi5HJRRiBiqFqQCkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمار: تلاش خودمو کردم، خیلی تلاش کردم. دیگه الان همه چی تموم شد. از اینجا شروع کردم و همینجا هم تمومش کردم.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/Futball180TV/98461" target="_blank">📅 02:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98460">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ad834c16.mp4?token=IoYan5ph3PS8cqhtROAFPioQaVpgfew1_51jfDzzkFxalRdS1zolhVgH89IBOWBV9uLjneEKaCkh6XH2hlxJXK19mPMgpqQVLjl-dpggNE4N0aibBjggqSK_69__f-Z7pajb-COq8K6w-bK16Q5wcBblu2dr6XZZWFKnyp7gHcP7EJesGJ8MeLJC2a6TQ2GwYMS374SU9olskJDiyQvBJDPINzFRvOHyjHLypOJdZ3V27cSU6xUIqZ8AyG9q9cWVzyBMQULrKwFk8jMI4VidG9yhCPFL-reMDBukjjyhaCaeHUjeldOeoDOLQWEtMbbWXZ7v5NnC6a68PVDPzIF-Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ad834c16.mp4?token=IoYan5ph3PS8cqhtROAFPioQaVpgfew1_51jfDzzkFxalRdS1zolhVgH89IBOWBV9uLjneEKaCkh6XH2hlxJXK19mPMgpqQVLjl-dpggNE4N0aibBjggqSK_69__f-Z7pajb-COq8K6w-bK16Q5wcBblu2dr6XZZWFKnyp7gHcP7EJesGJ8MeLJC2a6TQ2GwYMS374SU9olskJDiyQvBJDPINzFRvOHyjHLypOJdZ3V27cSU6xUIqZ8AyG9q9cWVzyBMQULrKwFk8jMI4VidG9yhCPFL-reMDBukjjyhaCaeHUjeldOeoDOLQWEtMbbWXZ7v5NnC6a68PVDPzIF-Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صد حذفه داداش
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/Futball180TV/98460" target="_blank">📅 02:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98459">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
بازی مکزیک مقابل انگلیس یک ساعت به تعویق افتاد.
این بازی از ساعت 4:30 شروع خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/Futball180TV/98459" target="_blank">📅 02:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98458">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
نیمار رسما از بازیهای ملی خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/Futball180TV/98458" target="_blank">📅 02:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98457">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-poll">
<h4>📊 نظرتونه یه ۳۰۰۰ دلارو بت بزنیم روی برد انگلیس ؟</h4>
<ul>
<li>✓ نه بابا ریسکه</li>
<li>✓ بزن کون لق پول</li>
</ul>
</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/98457" target="_blank">📅 02:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98456">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بازیکنای فرانسه بازی برزیل و نروژ رو به این شکل نگاه کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/Futball180TV/98456" target="_blank">📅 02:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98455">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umC3mhEdeebFppQ4sfoZUcCEoq4qqwv0RxveROTFrGswMia2Ms6bFVpYh_904lMKG5OqWpsDheH3ozqdAz5D0Z47bX1WLSuHCSAaZXkyvmWQ5yf0eHyXJVW24cI_HmpDz-ZQtaqPue2rTpCUL8YFOpHAkifKO7M4iwPVGPfuDW3S5f_FlL6Y51dMJki6VqjpsQ5oxLBT2Jjoi8jk1KzzmZYx7LXkC7ASf0mj0XN2HQY2DQCq1rvAXZpMVMCu5oCgnYTFFlBKS6JgEiwVxuSQveCj92J3s6CuiGrsTvJAkPMiy3N184InknuuFFdBMu8evntZHpDzeMLde-1Nbco-bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای فرانسه بازی برزیل و نروژ رو به این شکل نگاه کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/Futball180TV/98455" target="_blank">📅 02:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98454">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/sUnaqevAiN6JFKmKsg_7HT5xF5vzgmfJfm0fDT9z0wnwbxpTgfdd1k0JydLDnba8k3EEQT8azi0eo5vrhKhfsXeX-tvVODotvGkTUjqP873SUxx3m-lge5Vpsenk9q2UO0qpAi2_GuN2JAsbFtod_dWcEzoLHfFkmiuhPxdnIUc6qfhDo6WQas9owcstAcdlvXJVAo_7T5whcSw3HSgamLbN9-cYoZeWkDnQfzCVB3GxyoAFDk9zfg_l7fg0nXuEYwcEYtdAgrA0396MPMrRtuwNxCdTve1sUxKi6l90lcaypg_oPpK-ykLL_unRfDnHT_ZqkAty2_Bae_Ryuzc-Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش تو وقتی باختی که پول رو به فوتبال ترجیح دادی این گریه ها دیگه فایده یی ندارن
الانم برو با پولات حال کن فوتبالو ولکن
سال ۲۰۱۵ بود عشق میکردم با بازی هات بیشتر از مسی منتظر بازیت بودم ولی بدجور هم بارسلونا رو داغون کردی هم فوتبال خودتو
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98454" target="_blank">📅 02:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98453">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGAhCvDEJO8OQaI0nCZHwVRjnsLK1GVovEj_cAKxZaHm0FotiU47w_ePx3kBjxW8lBafxois-6vlIlN2TC2klBRpCfLDkNWSvADFcepGN1Ftn1rRdyzUKD4An6oTXbpnfSbUHNDq-sTMKbXrr7mgAWF4ahtsfzIyu32zpTAKT54ZypdhJ1CVC-O8a69OpCry1TuT_x8KnQ_mMfVXVXbGA2larSIs2SR6O4h2V9UpnioEiVyzIa_1jXcqWMMLz-4QGxLHmmJpaEGiVFuZTQjm5_6JNivzwNiL0Cai9d_1TeYh-kERD9hT8j0F-8DAWDBb7etp2nvuRAw-i1v_KrWpAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب انگلیس مقابل مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/98453" target="_blank">📅 02:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98452">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLWkEemdUIHsYxbHPLrz9QLM-nFn9e9-INF13dilyr00MG7yRJCHrRrWDZc5dD00lr6PwmsYBh4d5AT5vBjShS72x2vD_dRjAhihkHiNbciAyEat41Ekj6ZejxV5YIY7njrCwIiu5BLgw2ZEm60CVokrz7C_7RE796CFoDhlS4dU_qhtEC8Nl6j8KTFFpFNHC3hsNY0KmOUT4qh0t4AfDDVjDpWradW-d5opftGym7kcqmUOokgK0Uzlg0CCcFMLQgUe6g0Tw5vA71lvDgcpRDHlsup0e2k0xWneGIw5-cPshXzWFshaQGofWL5RU1fY2nOO_N16mfRLNwy71xVpaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برزیل برای اولین بار از جام جهانی 1990 قبل از مرحله یک چهارم نهایی از جام حذف شد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/98452" target="_blank">📅 02:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98451">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mutdz7vU5OmuH86XDfAoXLUqz1lNVxbKUnnx_3wORjiWgBRLYfULHJMv0e7OdB_4mJuhTvFD5ofkrXxNsGbpiFc1QEecrqHCGHCkb_C34R8NuVkcHGSEqcNWCiOOuFRT2_7uTKvHWPDYJEdfEAvdWyqU5sPl_vJx1Axo_rh4nKijkat7fkzpIaRqGRiKW4COVSDMj9PXC9Fp1qOL8x5cRmi8Ab71MvalikEeZQgux89pZLrQEumy4beyzhwCVmfpfak00KuEhXT7FhOfdpCT-tqEFilOzN06S0mYG3_KoDegnDjyFDOISv5r2d6GcsKRv8o_nbcDC1EWpkX5_pDvuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بهترین گلزنان تاریخ برزیل در جام جهانی:
رونالدو نازاریو 15 گل
پله 12 گل
نیمار 9 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/98451" target="_blank">📅 02:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98450">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtdjR-w3KmLpeE-wmcaQNV-UfJJTBfjdAswL386C7IaPMEMY3-QC3FfFO9Aq59VlirfZ9dhJQpv3bG9TMCujArjo3722_HXmfnXLJTTNIJUAVfYy6YCKaCCbF1CBMByT3zBAbn1-RM1dtyZO2ippo6A6Xz7H_F8f6MD3bcon8ipP6VoCqYJh3cr6HISFpTQi0a4_Jd9nxmLMD2OmPE3aw3N9vX4ZPHTAI78dfY8zDBEjMDO71uUK9fzfPLLPbabcBymythJInFaqevTuQihaJs9ovAjFONi3x4tqrXDD8tAuchBysqNUDPPN8gcJKs0J9aTxZofwk6DKf43F9KVVPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سه بازیکن تا اینجای جام جهانی برای اولین بار در تاریخ حداقل 7 گل به ثمر رساندند:
کیلیان امباپه
لیونل مسی
ارلینگ هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/98450" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98449">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بعد این برزیل دیگه هرکی بیاد دروغه
💔
🇧🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/98449" target="_blank">📅 01:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98448">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c013a9378b.mp4?token=f93aXFBSJBOV9qO-U0f2uI880ey8i-hDrQ5ypMSyU234t8wO16NHAUzdBoBDy30sIrpBwnrStF_jZgGaWNPNw3z691tatEk7wtlhqqMx5Bviq76Hweog7hgz5K0VrAlkE0zLZ4VR67YHgOjg48X2E73EsTd8ShY61DE8eOS3yOogLF78ctzoMcBXL1b_501xM5vG6mNuM9sSxyWmm6bh04LEfTGLoXLOg6OGh3BA6YrDDWNo1Z5yMyA2rTIMUG6WiYAtxM6r6iaC3mMX0llHlSruobkWtvA38XpwifAy1-PtjS3Ro4Yhi_JaclecGSrsd272tU5k5LeEj13kLFLbVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c013a9378b.mp4?token=f93aXFBSJBOV9qO-U0f2uI880ey8i-hDrQ5ypMSyU234t8wO16NHAUzdBoBDy30sIrpBwnrStF_jZgGaWNPNw3z691tatEk7wtlhqqMx5Bviq76Hweog7hgz5K0VrAlkE0zLZ4VR67YHgOjg48X2E73EsTd8ShY61DE8eOS3yOogLF78ctzoMcBXL1b_501xM5vG6mNuM9sSxyWmm6bh04LEfTGLoXLOg6OGh3BA6YrDDWNo1Z5yMyA2rTIMUG6WiYAtxM6r6iaC3mMX0llHlSruobkWtvA38XpwifAy1-PtjS3Ro4Yhi_JaclecGSrsd272tU5k5LeEj13kLFLbVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇳🇴
جشن وایکینگی نروژی ها پس از شکست برزیل در جام جهانی 2026 به رهبری ارلینگ هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/98448" target="_blank">📅 01:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98447">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMYC_yvSu4wSl-r-AAeNRamm_RA3m7-eVvz5LaKfUcF1ItiRSClAXDzGMwTAxKQUFAlmq4QhFtRJOxSrRMj9q4z8hfvNPUbIRm8hmWT8r8pKmnDmVqq_BqF5fxzXjPoRb5SUwY76AUPWvmZmabWDjjRdYs_A_dQkK9Urqs4wJNTK3bLRYY0mbDg3KXrwS3vUPib_N1SPGnM_7958x67L9OvGyrgkgITCtc7XTreiErY8pi2Flhunsm5l5GuozXmbBJEW1P0ydZdyTTqElDUBFLTFLS1Qca_Xe1FLfbIhL1-L7UdeFrWYtpITBFLDa3MBu7AVrRJuFsyFxTpIuHKcTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد این برزیل دیگه هرکی بیاد دروغه
💔
🇧🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/98447" target="_blank">📅 01:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98446">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wi79VyBJumMqNOREL86ebk9URB0GF1ChGOVowHyRXfwPte2rVIbr52goKnl7a0ZN1pyPcD4N6npXydPFcU77pcILkHo89Q6Q1QwYXJgNe7DMhuOScdQGoQA2GjZ5BkM0icMq6fJWBp8dHzYB9m3Aaxk02lmeG-4y_GIj-Ft4vJ8_8iF4XtbffE07cDodhZKemcHQT4YkEZAWA4-it-FCJDC7yr7wo6BYxG6EN9pHVzjhT6PLEhJmKxZXXlQxGsN_dmi0MmSbSEbptiUqHhV_LjBfwed9abxCFD5TICLff2mlwTjJFPZ6mSO1XpQQoLlkaOZ6IVYgCiuIytMdRn_hlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🇳🇴
تیم ملی نروژ برای دومین بار در تاریخ، برزیل را در جام جهانی شکست داد.
‏
✅
پیروزی 2-1 در سال 2026 میلادی
‏
✅
پیروزی 2-1 در سال 1998 میلادی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/98446" target="_blank">📅 01:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98445">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVIQ79gE8A3JZrv-VGI1em0WPE6SNK017cnPmzr7sItp99_NyLxAaCpTuvUGyvoulFrG9kebYlNj7ECJFN1_-_1G0_MSzZsq3-PYvZDMe5DVw_rYyLAeDkxad2bCns2OYaspstr7Ubel71TpMFR2NlPxpuRXf-LkGP7Y_HzcgyUFd5NedsbMDjA0TGbeIjcJ9GlhjPhjGzhzIjftIB8BlzkmS3YkBregAh6ZSBfXluRUa_YB2znviOV1U8ADGuuJlKivr0M8IoithJygufJ0L9Fl9n83mRYICnVxhxUBRZBH4Wf5oPYVpsJY4OrglUrPKJo51CEUG4cj7lByYr3pFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
یک‌قلب تقدیم به بهترین بازیکن برزیل در جام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/98445" target="_blank">📅 01:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98442">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vqZjFY_GaRwfan9IHXQoIDixzyMbE7zfHausWdm79g5NuexVP-kyxs_HJiwuKUl82qYxLi2BvpmYGlliOMXtY6dj22vFpbSup42rsZQGnbVOMzSc8kvwS8teQd8rgevtt8gHJcPf9YTTaSZevGNT0A4edFefs5O_yNzx9xojWTvt_HsAw3hMslOpvGuHz1dJXaXfZcEQI96-Sdhc4qcM8rQtJIPbWMOMhmhMQeTTr78MI311xEhculdVHzlehxLZNMRBra_-PuoXBK-UFuOzzAUjwAU7KaUNvvecsithV7Z2Ei7G50C1dxoAydHwC_S-Ve-cSSgbM3oI19djS6nu7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ICRAvmCwCm6MY2gF5aQyiTl7vUJF2cgSDq-sHgdHSPorYVWs93iqixwGmleV6QL9LKeucimzK0TE1EPOoq3ZmWAFdIWJQaE2Ti_gotQR26COmaHkO_RvKnhwisyTrjpSm5NBZN793a8ugv9Hsy2R0tFlUY6G-HapLdaWk9NwDM11KVTxP9nvWVw4-cYl-D7OPeaI5lsRPRLxyINEBy41p3l7fARep_KvnxOMAxb2mf6HEyk7SFgdmiF0axg5fbbf_T7k_DlM9rET8As1Z1jCetT2TthTsOZ0gfYm6LE8Cfy4J0l8WgJ0iKc8OcVK5x9SMWU1dWiEXt4St_QOJCrbTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CA07XYdCnCFgLALyyTtgKFmfVucoReUGcner3sTU9pCTGtpcbmfSZAAJiLh4s35t5ZL-r9BTscJDfKD2MZKwL4NMfRHSMrlFPt0AlM-oW1WQTJl2VGZsSLBMxAJ8vh4cnaFVgzPHF0fJw8WD9eZ1PL9QMBjrKWtjnb9vd-b1XKJo4z0XvsiiR_ed0O8PJtyOqr12aWGvob4GuHyMGYBbTsCl7N7olxdBYHMtMGJ76kCy5sg7wmq4pDPNaIoFZJFXP9kcBew4aHjyuhpDtWtGr3b5IiVWW5vBeQENTX2j0JyLKrklVoXi5Fs1PtVPb2UE3BhlkeZRi9Rjd9Yk6wucHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اشکهای بی پایان نیمار پس از حذف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/98442" target="_blank">📅 01:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98441">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sluJFwf6xR_vfUnSDTFeuLp5ksO2zFgTNZWDHC8vtZr1qI5-mG0z-idUXKNyVC6wknCsU7P_TdeFb6PyUz_XghiDEzSQOhf6utByDStZAVHYmlzGjiSBHs0PP54rrjlMm2ipAvh5rwJayKuVrQsB7AmntelfpPmkLtsv1txfziBlj_gTa51VG9jBCFFKeZx3zX-jnXLvl1rUIJC6qPGKEEtwRM8jh2OB7eGKtnWpEugJy4PnvfYmvDflnJb5vYQD3hyc4pgI9ktseIwjM8yCqpTnq69AQJQJimeGpvt10OyLDolSuaxgmRvd-Aq0nkDcLIdXNP9pFtb47Si6CeEnHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
دلداری آنچلوتی به وینیسیوس بعد بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/98441" target="_blank">📅 01:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98440">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49f5d9db70.mp4?token=l40EHo1SGGft18tIR7cPQXNhcYknjnYoo_zebivjb67zaR540TMstfCAQArcAyGaAMmVqhoe3yTHyrZ_SPnZ0DPiDVt4H6pQrXHjW5rhg26HV95DFC3pAjPeDxhQH2g0ZjzpN_YZsjNy5F8cXjzHfgvUadFUJwE9grAqgoqnIwkERhszP9E9Fh9P8urLTKpc4sDrzPm0aU5kIR6DL5c2vT-P9yaKcNWxsJ-0WhCWF42SY0GrqniB3o8tgWSIxFfo9KkNhR2fYwoV2q2Zt7QEJ3cFO2fIrGxIMPdqLruocx3M7rEEuoi2dIcrrYgzOUSY45G9HigkvLOwJknrPJgRAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49f5d9db70.mp4?token=l40EHo1SGGft18tIR7cPQXNhcYknjnYoo_zebivjb67zaR540TMstfCAQArcAyGaAMmVqhoe3yTHyrZ_SPnZ0DPiDVt4H6pQrXHjW5rhg26HV95DFC3pAjPeDxhQH2g0ZjzpN_YZsjNy5F8cXjzHfgvUadFUJwE9grAqgoqnIwkERhszP9E9Fh9P8urLTKpc4sDrzPm0aU5kIR6DL5c2vT-P9yaKcNWxsJ-0WhCWF42SY0GrqniB3o8tgWSIxFfo9KkNhR2fYwoV2q2Zt7QEJ3cFO2fIrGxIMPdqLruocx3M7rEEuoi2dIcrrYgzOUSY45G9HigkvLOwJknrPJgRAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارگردان تلویزیونی در حال نشون دادن گریه کردن مردم برزیل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/98440" target="_blank">📅 01:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98439">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1db9df5a1c.mp4?token=oWUoH5D0WiqZGgSDTI35b02ihNmocin5D0IESGG7Qi-fOoVKZ7Aay84N3d340-7eWEUJJY50Ig-ULut0GryV-2W7lxXDEERO1H7UJXIm5lPSdko-MfP7lHA5n_Tq14tZnAX_iP0fQcU_qfVKJcTkpLfZtm5PZodJ6-hXTRBFYScjsBaSucnQB0OIZPX_WOB7Sjt1HzR7QOt-NY9cqb66ZIj1mozVL_58Ft9azWiHcZCsD53QsAaLAojHFWapnszN3E6-jxqpDYPVau5DnMFdwq_SJKU0qoAKcs3et7H7yYXeHa8A3M65PQLqMIcaNUkpzh0mWyYxcfAOcls6bixxYCUdK-IFJRG8wXthE7uyZWY90j2LFYBsg-plH_ROKBoZ6httrdPQYvVX0XCeY67xVOVcfvgEgqj6Dwcj4iKBc844Kh2wT2Oa-keWb57fq_vqd1WOnQSwPdKno_Fz1OCTJUJNnezGeH0U3SoMQhfZIUpzFwFGG2UbZL3ikdKA73sMb7YBYwAlrcR-oyRNQP2NX4_teY7SwKbtllByx8MrZVDsNdIq5FBMPraAYW0lpOQYzs6dcb1qTEeRtNsgJjQRJTX_MDbORxTdyJkKkN7NOQP9vZJr9SsZxZQg2mm2oag6C8Qnu8oULskPBizSVQjNUlE1cOyfO8Co1WRD-xx2TZk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1db9df5a1c.mp4?token=oWUoH5D0WiqZGgSDTI35b02ihNmocin5D0IESGG7Qi-fOoVKZ7Aay84N3d340-7eWEUJJY50Ig-ULut0GryV-2W7lxXDEERO1H7UJXIm5lPSdko-MfP7lHA5n_Tq14tZnAX_iP0fQcU_qfVKJcTkpLfZtm5PZodJ6-hXTRBFYScjsBaSucnQB0OIZPX_WOB7Sjt1HzR7QOt-NY9cqb66ZIj1mozVL_58Ft9azWiHcZCsD53QsAaLAojHFWapnszN3E6-jxqpDYPVau5DnMFdwq_SJKU0qoAKcs3et7H7yYXeHa8A3M65PQLqMIcaNUkpzh0mWyYxcfAOcls6bixxYCUdK-IFJRG8wXthE7uyZWY90j2LFYBsg-plH_ROKBoZ6httrdPQYvVX0XCeY67xVOVcfvgEgqj6Dwcj4iKBc844Kh2wT2Oa-keWb57fq_vqd1WOnQSwPdKno_Fz1OCTJUJNnezGeH0U3SoMQhfZIUpzFwFGG2UbZL3ikdKA73sMb7YBYwAlrcR-oyRNQP2NX4_teY7SwKbtllByx8MrZVDsNdIq5FBMPraAYW0lpOQYzs6dcb1qTEeRtNsgJjQRJTX_MDbORxTdyJkKkN7NOQP9vZJr9SsZxZQg2mm2oag6C8Qnu8oULskPBizSVQjNUlE1cOyfO8Co1WRD-xx2TZk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇧🇷
گریه‌های شدید نیمار پس از پایان بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/98439" target="_blank">📅 01:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98438">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dszh8nVlzgi1B0IYIUtKiSt5UbRFLjXRdLgG9VdkrY9tq6b7i4qWt2a2EmBMIP4sZLDHiCTOpFZQHq4FUl26M_mq0OVHjJWWV9p5iiwfVtp2H3qCOFtrD4uLD7FKHCpVN9oKM09LZhlErIZ3-K_CbuA-ZPPHy4_SvW-kofsxx2kCFml68ZAeW4CfKeLGotXBZhanAh6R4fE1KvX-6YWlaVEYDutr0lHUyuNOOEwMOPqsX0Mf_vP3MTPGD3zTT8R9PU9Fckx4wdYrN1sySbc-n_69beLF-rZKVyeeoBvJy2bPGzuCg0Pb0G1D5DDTRrs5KajxSsg_rgPl2dS22gI1YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
😍
وینیسیوس حالا میتونه با خیال راحت از تعطیلات تابستونی در سواحل برزیل لذت ببره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/98438" target="_blank">📅 01:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98437">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iyk51ltE6PTen8o7d1kUr1JD2QaHIFrryimoR5ERB6LTECZ8ZiCRgnMlpPerz_OBNJ1IZNNvSAYTok6qJW7_iTGsUOg77Sd12pHVufJaJo-4xDutIodLYdkS0Sj776yN9GumGnGGqrMESaMU1wihWXFsTf_uyD8rBW3Xpmv4L1Tzk0ClV5_ow0p3_myXtYbVXwpw5uQxGbmRBz5gW3n4e-3ewsZ-JlURWnzCWfuUoalM-cFwBu_6DgKuaOKTnmPBNx_4t-I2HzvowamO7FbDHHTK4epyyUNGtc3ECHQ3xs2cfWySxf2Hdgma-_CSToIwJAXEo7kfH_uvYK-m_QlHzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏وقتی میخوام یه کار خوب انجام بدم
نتیجه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/98437" target="_blank">📅 01:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98436">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🔥
📊
ارلینگ هالند مقابل برزیل
✅
— ۲ گل
✅
— ۲ پاس منجر به موقعیت گل
✅
— ۳ شوت به سمت دروازه
✅
— ۳ مشارکت دفاعی
✅
— ۳ نبرد هوایی موفق از ۳
✅
— امتیاز ۹.۰ از
📊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/98436" target="_blank">📅 01:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98434">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/naoDcYar2aWGAp0I8uBI0hCCnAqG-Mvap0aoDEA99V3lQA_nu1MkYekKdM5DYw8GgBir0v8vDhgLTMAPs9Jbc2elvK5eVpTHHF4lz0-hE1oTOo-jvRohk33U_oROB4Trin5ZBVwvw6EIiiYPm0oLBsPtw86Rq8nNWB0Hrs-2hTKsFr23tB459d86bDJzyR3AhQz-trZiYmYX2i_vqF9J0WlIvvgGPSl8UpIb_IxaLC3m75Ko4Z8PkQCzg1qKVB5R47D2lnQWBYF18NW4ar395PSXcg0lUGk3hmQC8Z8JK1bgk-2sgB66lRhMVdfkfntcZKLeBCXSwWZ3oMr0rgISAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZP4KxnRXicsiItS59B_NaXxeQdKl_1AC23YnUK0Po1ORyxY97Z5JU_sq4HykcsC5ANup16gNhg-xnC4LKj5ex8CBEzeLfxeW2jpcSEv__ACMAgWmqFhnGnM8aeucgSNhIZKO7EFDIYDWzfZwLSRi1Of7jrHlQ26gS2qurwGDFH4kOk9si1PVQc5D7rEm1pzcoy-DauTcokzdrixVAalGScXgvCX2a3BWLwaUwyjuWps5LOg59H65olC7yRQcnGiB29CxAltMPCRPMpmzfD3Cg1MTr9vGQtsZJZvWKj6LYBCSbJR34EsLJCAwZm6DnCDT86zn4HLo7-pp6XRsk6QVAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از لحاظ شباهت
🥶
🇳🇴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/98434" target="_blank">📅 01:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98433">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mt-j_-VuRcrJ2eY5Xjsfx6cK5fAh8aJjvSMUhY_9KmY0ixke7QWtGz5VCkyxS5L6gb2pPHUskXGEZIyNnzRpS-J-b3OkbaTq3-t62ek2EeSu8FrJDiv8D1RQi4laHWBytyTJfV_IXSRP1BrmQl3mxbNmX5bYqD7zuarcUAKgJfH0WLIlnWJMlUQpAIwPrbiU1uusBvdAKzCJ7-4h1_qHVmh4lPYmEfp1578bgOqgDlBXKYk99WT4NxxrSMZG0UDezxjUnihHBWrkMWHYhbxZtoYagYC0_s0EK5S0COXopaJcCZhtcJQLg4AieZxlWXLZ8r_SNdK-xQ3Za0WLXDZJqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | وایکینگ‌ها فاتح نبرد بزرگ؛ برزیل از جام جهانی کنار رفت!
🇳🇴
نروژ
😀
-
😃
برزیل
🇧🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/98433" target="_blank">📅 01:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98432">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/853652307d.mp4?token=fQTE8qD8_kUuCVnnIb2iafLQs1PX41uJEubS8BIoipbC6Jo8KqRU-9cBayKWxmCseq7dt2D3x0_ekQsq77Z01iUzUcmI8OBe_QMQi8MamEQwUrOiGJ7e0RAUFqMB5qQFDX_Fa3BxXzbE9lsRaiyTFrdddgJULfj8-cUDtnXxasNNHAuMOka23bQd-fETUi1kX2oVGsP-TUwb9NuRpxzQLmXBPMBXkfBXsREr6keVGxCeinwZ6T_b_ibinNoPChkM7VRixT-R7aE2YLT0u3lsld0l0Vi3XCm5rs0vE74_XqDgG2mQ7W0qDaFa-P0R0LJ1e-vDaMa6LVnGEDiZTTPYKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/853652307d.mp4?token=fQTE8qD8_kUuCVnnIb2iafLQs1PX41uJEubS8BIoipbC6Jo8KqRU-9cBayKWxmCseq7dt2D3x0_ekQsq77Z01iUzUcmI8OBe_QMQi8MamEQwUrOiGJ7e0RAUFqMB5qQFDX_Fa3BxXzbE9lsRaiyTFrdddgJULfj8-cUDtnXxasNNHAuMOka23bQd-fETUi1kX2oVGsP-TUwb9NuRpxzQLmXBPMBXkfBXsREr6keVGxCeinwZ6T_b_ibinNoPChkM7VRixT-R7aE2YLT0u3lsld0l0Vi3XCm5rs0vE74_XqDgG2mQ7W0qDaFa-P0R0LJ1e-vDaMa6LVnGEDiZTTPYKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇧🇷
گل‌اول برزیل توسط نیمار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/98432" target="_blank">📅 01:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98431">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گللللل برزیل</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/98431" target="_blank">📅 01:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98430">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گل شد</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/98430" target="_blank">📅 01:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98429">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نیمار پشت توپ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/98429" target="_blank">📅 01:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98427">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پنالتیییی برای برزیل</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/98427" target="_blank">📅 01:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98426">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🔥
❌
خلص و تمت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/98426" target="_blank">📅 01:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98425">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFYqlQx6CpQQ8Rv_X336e1_prBjTJ7rOmQmfNZQSNWqluAUVEnjq8z1fqGs1rddsyceEnBu7CDzCqGcWeZsUtL62A1u7PQLBArFRo5CTZKOdInvtJCdwMRaeRxiaEhCzyBVMD4OIKjWmGShXfZsTZWa5FVWS_pxgRgO9QMmtqmsqRuXaGbbSoSe5hakBTskSk3k-pGVKLBVeHBtE5HKMeTFrerhDq6xoM6OtoIcgWn_IYym0FF_RZOa_80x0WRTR50NJQwIStcVEMGUSIHZF-FitGWuepz7-880vL3DcYIEmCVJbCBXYxsBfzRSS5acrYxYkg5f6rgSGjMiqgd7Feg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
❌
خلص و تمت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/98425" target="_blank">📅 01:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98423">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uiP76dklPE7SIMyYyER8bBWeM_ZDO5uGAw44VVZHOOx6XkDd4FOdSWoXjjnat1vgzVTCrvlecnEmPzKmRJhnZExBLSw3ygjzdQmpWiZphdtdJjWkkTDO6UiyKKy1MdejmPNmOa-mwISuBggQjwOdJeJj8xxndTGwiQ5O4qpQ68ktOfPQZPnHfazBTwzL2XhXKNbov8cq4Sh9d2ZrOzo_RB0h4hit_m5D42cncZt04m2NO7rZKVDSm1tNeYcfSzBjcBnO9vYRemSQ5gz8j9WSD3PljOJsu3ExiW6SEfbXnOpMPLgsGgix7bviZkht9htE80lLSdYTmHTjEdKKbuqwXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QmMH64jefY5KToAzPEhECTwOxdA7lirXuZa9CEnz9RWsdjm_Su3UTM2vNmJ1jCcTwuyY86NHPKT4kHiydnFi2EUO_kNt2-S3JFXaLXA94vdZrD__IT55gi6OvB2GWAXbWRsu_ayRoSTSmY50jk3rJfJAcHh6tTpb3ad_ml1BraeiaqRYwLvpDJwLR5PeLfSldXgnbLMKQZRjCt1wpcT0Inkx5ZEVf8DfFfgbVI7t6gzFWfbzfMmSyB3-dfC8TEbteD2QK1uotYKHorAyqYU5QVNsscfKVQ31-OxRRkEd3AMrj2nazVvCvW2yqs8tNRR2X1OSiSfq9BT67zghODAebw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👋
👋
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/98423" target="_blank">📅 01:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98422">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuG1LxbSHh10pxBC2db5nznY2jRMex8zWKgYpOcT1Nq0J7LZklBIV8-UDDdfv_5UsPFf8slJkcJHFwUTG4Kj5SQU-IekhyiZ22utPqIDeV8U8rzbdNADVndFo9YZV2cmgOiaZeVq1kkZK32bMmcmaF-rgQ_SyQQdbIgfgZQ5a9Tvs1142L9ievdYwbCjD6tT0lHuwzeYZoeXmMSQCO6Asumah9KiYzS2eFgX6TtP9QHnuPgnjHzpDJw8XjRSg6EFAuZ5CnR7Lpo5YITzL4oerU3gXY9q0efRuTvs6ZaAoV30a_W4ANMNUD5ab0kEzWVyi_8Xjjc2xfztH2hj2jit3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا برسه به دادت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/98422" target="_blank">📅 01:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98421">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0jwZEsDlfbnZlZOSCJZ8qDO1ABda9TL1nhkWgXUT85I4dmxmA8pARFqxUAkAAI5oG8Nb01uZlTUYF6-L7xdmbIrfZjImgyn_z3xqjio-eKoEEnYqK_uZ0OnBG2-a8vh2unAKu2HT3hwzwRXXQMj-Ki1eIOw9UMsz9GhGWGSV6mri7OrypkpchLblXZ8OG_Q9NIU9Jf4Sfl6Lpm8prL1Fz6tSpt9-vRgJSDeG__51BPhjqlOaQLsKEUjgPg_RVclEvnR-MSc_dK4IUzSaOkyhXiC4enLmPNmUUU7MIM8lD6xnsuLkE8nN1IsYNjD7aZJaXSe9thJCvf8aIsNjODROA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">AUUUURRRRRAAAA
🥶
🥶
🥶
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/98421" target="_blank">📅 01:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98420">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تیمی که ژائو پدرو بهترین بازیکن فصل چلسی رو دعوت نکنه و بجاش یه کصخل که از هرجا دلش میخاد شوت میزنه رو دعوت کنه ازین بهتر نمیشه
برزیل پررررررررر</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/98420" target="_blank">📅 01:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98419">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a0f2e0732b.mp4?token=loHdFh-d3Oy10gU7Az9AksMOqICuz7ukc88-57VPhN19VBgDIHdHCOf9qFef0s9f5R-Fx9qJ3M7twY_K9s_7prk3oWPMH7buhYSSzFNxSgrrUU3tdtKoNMKayXkWtB6T4-tSFyxcdnnpevQxp0wgiO0Sv6XrcQrxq0jUP14pp-SAlQaq_96TJKUmmdydjKtA2GVmTNT9geJ4Qxsy2wVESnM-Zlaferfq-Tzn09DH3QbMu_DcrUYVidM_rLohEtl377zdw4GoPwnkCxA8YFLGqowHRQMyg72rjk0gnYG--j5xO0B6V-1ToLUk17cY-zKXhdhy0aS_62231_WQiRMs3w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a0f2e0732b.mp4?token=loHdFh-d3Oy10gU7Az9AksMOqICuz7ukc88-57VPhN19VBgDIHdHCOf9qFef0s9f5R-Fx9qJ3M7twY_K9s_7prk3oWPMH7buhYSSzFNxSgrrUU3tdtKoNMKayXkWtB6T4-tSFyxcdnnpevQxp0wgiO0Sv6XrcQrxq0jUP14pp-SAlQaq_96TJKUmmdydjKtA2GVmTNT9geJ4Qxsy2wVESnM-Zlaferfq-Tzn09DH3QbMu_DcrUYVidM_rLohEtl377zdw4GoPwnkCxA8YFLGqowHRQMyg72rjk0gnYG--j5xO0B6V-1ToLUk17cY-zKXhdhy0aS_62231_WQiRMs3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
🇳🇴
گل‌دوم نروژ توسط ارلینگ‌هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/98419" target="_blank">📅 01:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98418">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🍑
🍑
🍑
🍑
🍑
🍑
🍑
هالندددددد</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/98418" target="_blank">📅 01:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98417">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پرزیلللللللللللل پررررررررر</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/98417" target="_blank">📅 01:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98416">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">برزیللللل پررررررررر</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/98416" target="_blank">📅 01:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98415">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">هالند گاییییییییییید
🔥</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/98415" target="_blank">📅 01:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98414">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">عشققققق میکنم با دیدن بازی هالللندددددددددد</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/98414" target="_blank">📅 01:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98413">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">هالندددددددددد</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/98413" target="_blank">📅 01:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98412">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">پشماممممممممم
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/98412" target="_blank">📅 01:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98411">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بای بای کارلتو</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/98411" target="_blank">📅 01:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98410">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تمامممممممم</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/98410" target="_blank">📅 01:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98409">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یا خدااااااااا
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/98409" target="_blank">📅 01:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98408">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دومییییییییببی</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/98408" target="_blank">📅 01:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98407">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نروژژزززز</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/98407" target="_blank">📅 01:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98406">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گلگلگلگلگلگاگا</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/98406" target="_blank">📅 01:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98405">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tc_coRpdDAyl_FsJQ0kJO-j5o0j9cL6nDhnwH-58g9-1gJXHttXnqeXEcVcu6inlg_fh-WmF7gTZrHbOA12GBIwzZm6QZkr3ihp_xE6uymNWGRuLg5EgAq4uNSl10ORVBIp0sTw8FbzWuOKYxShjIj822ZPVUi2Woc6Z8c-GubCj8sVDodssXBig9XM-VppztDvGiO4xFXwG0c91FynrCydvQTbb4i-w6pmlY9Sxeb_NVjTpkPhE5wke2xWKwqzGNJC9egASecwPzfIhCmH71dRiaua4yWB_vt-6aSczFMkjSQKRy-ykxmMij5PH86Q7VIYAuxaOVWx-0O7DOgq6JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
رقابت برای کسب کفش طلای جام‌جهانی همچنان پرقدرت ادامه داره:
🇫🇷
7 گل - کیلیان امباپه
🇦🇷
7 گل - لیونل مسی
🇳🇴
6 گل - ارلینگ هالند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
5 گل - هری کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/98405" target="_blank">📅 01:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98404">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">برزیل خیلی فشار میاره</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/98404" target="_blank">📅 01:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98403">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6cU1nYQ7vq_7810jJepFBp23_48umWzsJIliNdlvVa7BobC98AR1aovVHJYdNu8kjyH4_GSwInjBMMKymGULQoRIVOMMb4kJRsdc6vXkGfIyWoyMedYk_rot42QxP0xQAnwbiMYnE0tAhsjkEywaCqG7B09cWE3fFR6UBddoWpwCXLVPY7YDNyMXLeZvcMeRJZvIpB0zppBObCIayRL9kCu7Hutgm9q-O8Ql1hoR_b7uprL2j-oQJsEZICRdO8VUzVxq7PC6m_7557iiQ0lQhUjDlsm3-w4lIT6uQpWSxf59wFL31Sk7fA0Rx49_O7Gzl1cWeSKrCLVr37bfWq34Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمتر این گابریل رو انگولک کن آقای هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/98403" target="_blank">📅 01:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98402">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">واااااای چییییی گل نشد</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/98402" target="_blank">📅 01:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98401">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/698b2b9218.mp4?token=ohgx7GBGGNj0oYMdT4NLaWmkMYjyJ6pdVUxpMDWQkuxyuNjYeKgvgtqA5m8B3DQRVT1_7sa2iVdinWLjzhk9DZHeJ7fU6fFRQeHHe_Ay9UqczLRtoxquhK3ofrVRPYvG4Isruxg8JH5O3dEfwMmGEvV-wGckydOASj-DpQMnAc1qSwZk5-upLGfJznvgIb5SY48NYGQzq0kkskMskTbntRNxdguq3t7s6Fq-J1fnWhn9iNHQMvqXDwtkuhVmIZZVgZxsRUbCCbgAAKOWKpbSiNGw7F36Mn7D_ta3-0WZYRR5IV8P5yG6gDVRq5ZzGKqOkgB-AJiWJAT6w-EoRhX6wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/698b2b9218.mp4?token=ohgx7GBGGNj0oYMdT4NLaWmkMYjyJ6pdVUxpMDWQkuxyuNjYeKgvgtqA5m8B3DQRVT1_7sa2iVdinWLjzhk9DZHeJ7fU6fFRQeHHe_Ay9UqczLRtoxquhK3ofrVRPYvG4Isruxg8JH5O3dEfwMmGEvV-wGckydOASj-DpQMnAc1qSwZk5-upLGfJznvgIb5SY48NYGQzq0kkskMskTbntRNxdguq3t7s6Fq-J1fnWhn9iNHQMvqXDwtkuhVmIZZVgZxsRUbCCbgAAKOWKpbSiNGw7F36Mn7D_ta3-0WZYRR5IV8P5yG6gDVRq5ZzGKqOkgB-AJiWJAT6w-EoRhX6wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
گل اول نروژ به برزیل توسط هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/98401" target="_blank">📅 01:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98400">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">برزیییییلللللللل پرررررررررر</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/98400" target="_blank">📅 01:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98399">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">برزیللللل پرررررررر</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/98399" target="_blank">📅 01:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98398">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">هالنددددددددد</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/98398" target="_blank">📅 01:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98397">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گللللللللللللل نروژژووو</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/98397" target="_blank">📅 01:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98395">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نیمااااااررررر اومدددد
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/98395" target="_blank">📅 00:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98394">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G672myeAEWNBgrehHAIjzQsLAgD99Zga15DwpMPr4LpRiqROo-h-UvgYDNdMq3WlaN2Lt07_U8N7FT3xfu4_rJ6H_cZxdymqyWTBFL6JH8TZEraV2wTMyVOZIhaYGxBRvfyR7rrCe1ZKcsgWLf4SAllNzgZ1s-_wBFGfyMGLNftL6W_-IGYVAr7vT-MS22P_xDPH6SA7g9NBEZ4wFzhpRUkwNBrx5K49N9KjSliNQ3BspGNft2ID2NJtaj8TyP0thRZpTu6njdYxEA-x0_7uLLuD2YRb0VUljfW9Zcrt4QdtsSYGHUXSxlWRDIaUM7NRPLN-eF4KZ9d2vmnlY_10ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اندریک از بازیای بعدی: مهاجمای تیم مصدوم شدن میتونم بازی کنم؟
🔻
واکنش آنچلوتی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/98394" target="_blank">📅 00:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98393">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گلر نروژ واقعا عالیه</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/98393" target="_blank">📅 00:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98391">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qr0rl0ittwmc5tuWd0USpGVksVSQrA4soZaiRq9hKMImUx6LVB_bkaTUciZX3rXbngfu5VsoJ_C2QZJjH4U0RcrbtGXi0spC15TA3N5a8nXxu6YeUEG6nAA-HN1EaHeyjNuKC83aBynbczo-5kOV5Ug-LuBddUlQw-iJyvasxmXX6Unwq5ghczJ4sPv38c3fwyBl_r_MiGTq_-nNa7y69nN82PrgIehRjkVVAlQ0J_5pFODDwKFeOcctbu40y4VcvIHemO20udlvH_7DhVfJ4b4mYQXEQjSc27o893BfnOr5e6_IjAGgGViN5HzoqhwvQcj8FjKCjpKJhdEER_DmXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Anxgm7Ftu_TwJRT6ah__jh-Sjot3GoaRTSbA_J5xKDUIYcfOh7iTNm-kLB3mGXjYyU11-PxBAspVpf4qrzYIp-yc0KkzI0-UOeN17EcsSEq0PVbr3HCQC_e0JJhmYxJhzq-F51Z3npPY-6pdegvyK6UCBJucWOqu34gnQXgcLOOYxxN-yXFVroNUlpx7gdZHwc8hsy6T6LuTUl9HWAB18ajqgeuHXUlE5whbLt3ilVupqN8zzS8UALb38VNJ3eV0enjskguoK02P_0RX-cZQE6s30Oihl7fJMFUFyD61_-9FMh8uqiMv03Gw4inB_3SyV70JUqEMx76d48eFPyxnUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عجب تک به تکیو رید اندریک
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/98391" target="_blank">📅 00:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98390">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اندریک واقعا ته خندس</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/98390" target="_blank">📅 00:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98389">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">این چه شوتی بود پدرسگ</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/98389" target="_blank">📅 00:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98387">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r113skapO1s-QSiSKRWKjybIMm-oo5pMMo6W_Eq-7OtedQ8M5iWC8HV4c1G4hXBYcdXHoUaM7nYpWEWhZ8Fq_761M6p2faHNyPFnIkU3h0_0lpO9f15ekVAFcSa8Q6y2DCYVCLP6x3scZvFAhX5R6Mdal4BVWmosBY7gvEgefnbNTUnaLGk6cBZiTlZZ7M-pclk1jwdbLEFMiw6-Jd8oXGQstoo35UBaCpJg0GPNvvB9DWffbVcxDFk-u8sgcpp7ZBC3vHmH9LEf3U8QSlhBG0evsKHgqJRmuy7td4FpHdp3dZ9zyiRFL6siu1lt5dWlB_TXucbsXIDfEK9DRqv8RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MYqx7TNFy7C4vxf-NQUeA7ngckJSqbnW17wg2siqgj0WdoVZAJfOmdB1mvC59c_F3dfNjRKebd4gzrFBC4SzzfPxjp6knUMCC3gNGWIxiVEg-u8B__Vj5JP-aKN0JfgneaqweafEdOs4PIsGp1W1gX4VhnS4-AJGWKOypK0N1pCtzlutwLiMnQse__qzsGZ2jzsZ9chSST62tATumtPBbasGwHIi4SHotruRu4sdwSfUgOYFfEzasY4jxDgigIi9QguaI8YRIjd7XqgWp5B5DkP7kwAaot2w0TppMGc1QZHfiOE-_2kHHycTCGk3GtsAb_lChvs8A45WgxgS16qP2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سمت راست : 150 هزار پوند در هفته
سمت چپ: بدون تیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/98387" target="_blank">📅 00:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98386">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">عجب کسخلی بودی و هستی</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/98386" target="_blank">📅 00:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98385">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وااااااای چیووووو رید</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/98385" target="_blank">📅 00:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98384">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اندریک اومد کارو دربیاره</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/98384" target="_blank">📅 00:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98381">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lGBxTpLjgh3Jn1EKjo4wdSIjKvG9kHLrAukVmXzTsrqAgBRZanTcjnwaCKOaoiq6TcinPvsiJhPzT9TK-fpl77V4BpQJce0ftIGD3Et1DSw7Fp0449CLo36W1kvZVOa6LaeRz0nNwr4K1tkFn6p8rIw_6mCQ8i8nHUIkFqMGwBVvD59rVsKg9HrEoArbFbDDtggsTJFdwAGMEvUsBnjvb9t8dzipbUjyHmbGhBpjonsIoAZIgPFs9fiN-31_TRhYjfnlg9aNBeKqNx3SvMJ7FF9qFesDO3CfaFsI5p9fyB1APWSpvqSPpgv_Zz52txCWh_qwKfBfzNaT2H76Q_02Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YLSRNHUeg44fFcFXTmZcNKwcrsBDJzsEOkRwcjdVKVXcPMnhe9rDtBUO_RIxYsd0159EaUA6ImKxBs9RK3rknlfFZNzF4QBak4Ks_FeFN3_MIkJGzzRstE9j4wnxp9WHqLxJyUFhGHWLo4-Fspeo2qk39YYy_GwymAv32hsJEU7ImL6vcYOqryIOJR5BzxkaVmKfPZmFIHHFJjWbjlzHv61uWnQQPpoPp_L6LuiOmSHuHlopGwqoeleS40ScWgqSK4HDEFvKf3_6o1jIPcUZk2O--K48IGxishBtDRJqyOJYgJFNKJztEcif1sHOSQkU9-my5dZ2nkg9lRh4EdUoow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pcbhWcIOZSdOn0dk4S8M8bLT50XIhHOWfjsMaYhlnC11hjGEik21q2MqHlSjdsiANy3kWw8nv0szoJroA71TpY1aL5WiuG0CyGfxclO7O7SyaiSO1RVmpeSDL-3r4PQ8ezgFd1n0_ICmckkZtQfxMNrdCNyiGRnOf4hrUmtyiIFoT_2RkYIHaHxOYDpgwqJT751y-j8fQGxKUeaWO2q0El8Jyqh7lqQ3chgf_v5qKXaG9St0aSg5Stz-r8qVwf4Il9QdgUvfD5J3rs4ea93Ltu-67cClrtMOk_IipB8TstTw8wN9ItemCDWi2o4ywjSIIUpM8kg2FzC1oLepdA35Hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز افتتاحیه فیلم اودیسه نولان در لندن بود و بازیگرای فیلم قبل از بازی امشب انگلیس و مکزیک با کیت تیم‌ملی انگلیس که پشتش اسم شخصیت‌هاشون نوشته بود عکس گرفتن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/98381" target="_blank">📅 00:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98380">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بریم سراغ نیمه دوم</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/98380" target="_blank">📅 00:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98379">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پایان نیمه اول
🇧🇷
برزیل 0 -
🇳🇴
نروژ 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/98379" target="_blank">📅 00:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98378">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پشمام چه توپی رو گرفت آلیسون</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/98378" target="_blank">📅 00:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98377">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igZtKM_QDsAuBzOLw0jyOSLlGFHB9UxEQ8gla2yTPvOyDtWnXUuEDfG5AuwcZS7k4zNKsHpWYYAhZB7OlruDzXm6VgRHOSdhbhFcHyoN6NfsnGerKS8VcawGpuqojhuFBTC6JiEp0lcUcYNk8vWuYzFlnump39azamd1Go_GqzwwOhqiUHYXPi_HU4uyDzjSmuBJZJPdOsIyZp1Aj3flUvtY01LZAQFX8b438fP-g_cUo3kNspBVtyBRz3u0cqS8J2bG9d-hjBb7r4iOYsG8SHlLcjLqj_sn_ZsfsKOx4BDB81gbkDWXaRq4IhPaYe4a8LK0EpYGaRA-Tyd3aLz5oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو ببین
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/98377" target="_blank">📅 00:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98376">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8883504b8d.mp4?token=Z-WH33FYhrivVir4UvgcaCqEvTElH5opXQEYdazP_d8Znw8XpcgD3NMs5GEVUffnfuAdkqu-M7o1dsurDzSYGVrwAMKwgw7FMfKMVLzRwVKRmpc8w_o82JY_x1VXSvKNrc1FJIUT1xrLEqdOTrzvRjI7bJUGC1me1ma0_6lq5PFzgsCn3yttHjPhq_v3TFWywizBXVJ4PNwDYyKd9-ha4Wg2mMXMjHu1YTr4ZJ4UF5l3aUBpTfzNsGqsN4JOCWK994HLZaXRfMDylOeIpycr8N4ZJBgEVoKtP5Pix_T4ujs6V0XN9apvKJSocabxzxHxSDeYdRkyzlCDVQ6N2DAUuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8883504b8d.mp4?token=Z-WH33FYhrivVir4UvgcaCqEvTElH5opXQEYdazP_d8Znw8XpcgD3NMs5GEVUffnfuAdkqu-M7o1dsurDzSYGVrwAMKwgw7FMfKMVLzRwVKRmpc8w_o82JY_x1VXSvKNrc1FJIUT1xrLEqdOTrzvRjI7bJUGC1me1ma0_6lq5PFzgsCn3yttHjPhq_v3TFWywizBXVJ4PNwDYyKd9-ha4Wg2mMXMjHu1YTr4ZJ4UF5l3aUBpTfzNsGqsN4JOCWK994HLZaXRfMDylOeIpycr8N4ZJBgEVoKtP5Pix_T4ujs6V0XN9apvKJSocabxzxHxSDeYdRkyzlCDVQ6N2DAUuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تارتار: قطعا در ترکیب پرسپولیس تغییرات باید ایجاد شود/ به بازیکنان جنجگو و پرتلاش نیاز دارم و از هفته اول یک تیم دونده و سختکوش را به زمین می‌فرستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/98376" target="_blank">📅 00:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98375">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdfvVJeYs9fh72NYYPxQlOvnOawBwq_hD_7RY3eRRlqImXPBVRl7ISg7WtT4MUcl3j61nLMm9XvKArJLdpLhN8rYPTh7vPqe_U6r9hShS1Ensakr4boCDNF32mcLtUZ_zC0BVkqMM0xh13yEBG54LzXGDdbytnfWIO9oM2IXu0qzNYkFfOGWjjjT620Ci-9lPQ-PRlwdG3WawiTIg_CB0WUkPD5CN4M2o40pIUXhrzxg1OxuE2ksE-XNBU2x9IFBH2W-Mg7vjoOqT1Oqq8UUtrajbFpFo1sZoH6-wGxcRXdFBJw4eLSNNQEN9NawgK2d-hWRwYuwUTBJSw4luBtxzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برزیل تو 40 سال اخیر جام‌جهانی در جریان بازی هیچ پنالتی‌ای رو خراب نکرده بود. در تاریخ جام جهانی برزیل فقط 4 پنالتیو تو جریان بازی نتونسته گل کنه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/98375" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98374">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دلتونو به این خوش کردید که کونیا برا برزیل گل بزنن؟</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/98374" target="_blank">📅 23:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98373">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بریم برا آب درنگ</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/98373" target="_blank">📅 23:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98372">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRjlns5fjocBhXr76mdifeIAq1uN5Z-Le44B0QES83gx79d4QHpJNRfWGuO2LyT1XNUODfjSsAVTxIdhN1zvM-P1t0VfJTQ9jz0HQ-xODkxuysSuWhXG5PytMKQiXTSB9hwNHKW3N1gog0vNGKfkzvuEmdkXTal64Hm-cntmFS67UoEdtePQK5thYDAeQ3-I13PFMjy3fDhRdPBAlMr-_5AAN2xQuTxO6_p6ol8ES9ocWrf6FbarSTNjEhk83fyeF4SmH4u4yh2ppgZIKs4_EJiXsOS3qupp2RVgDtcyUvcfMFur4IsKB4HrumKbomcY2jSI9evWUjK-HK7MFVWCcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنری که هوادارای برزیل از اون میم معروف که جدیدا ترند شده آوردن ورزشگاه
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/98372" target="_blank">📅 23:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98371">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjRCOtwCSc-rDBE1F7FndqC468UGOtdO618mL3V3pcpsDIcreo-ydEdukwT81JjoKk14v2npi_hEwB192j_LORgCwsyaU6HbM-OJgkXvvtmWYuZAkx-Clv6KqDGMhwWqYBnpmtGTCo7sqjkJFd3YXXnF05zY4gAz8fscPAt-sfwuXm_Py4vg3PhTxnuo5eiibQtrL3jeNWGNY3mD0otOGzjteXGdAISZ-6o2oM-W9UqVXzCJbWRhhfjm5jDvT3XZ3OBVxlvzEqkw1wuych1qD5qPBt76civTOYEkxaTozxBqNFlL4G5OlwV6zpjZEQwfttAWZe4b2QZ2NYqVjnLj-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنالتی که گیمارش خراب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/98371" target="_blank">📅 23:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98370">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/84350ae9cb.mp4?token=Nb7hPtYuVzRNxhfEbM953yepdxo4_RsTnTAKDDsE9p-Sn-WRxw53SZweERSqOhgvX4AoyIHVgN3cVkNvsXPwI5lj55CWJ61PWUeRnKghSfrN8w5b20QmieloN4c0LHujINLIy8B1bBMXhuzj2MxtYI6etscIp1F90uflQbrDn3OwKk67O9_glJKSSx4fU0MuvODRLgXUJH_AEQ8iHwpRSDtiuRfa8ehxylPSK-SWXJckcdFm4fBiaXsSDVBa9bptP-S7tcyReiqghDl7MG2nm2Lmhb0N_bOLXH3jxELvhqR8_RSR0p1PGSW_ZUA2SALj69kYOPaEz_wCCvZpJDbgWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/84350ae9cb.mp4?token=Nb7hPtYuVzRNxhfEbM953yepdxo4_RsTnTAKDDsE9p-Sn-WRxw53SZweERSqOhgvX4AoyIHVgN3cVkNvsXPwI5lj55CWJ61PWUeRnKghSfrN8w5b20QmieloN4c0LHujINLIy8B1bBMXhuzj2MxtYI6etscIp1F90uflQbrDn3OwKk67O9_glJKSSx4fU0MuvODRLgXUJH_AEQ8iHwpRSDtiuRfa8ehxylPSK-SWXJckcdFm4fBiaXsSDVBa9bptP-S7tcyReiqghDl7MG2nm2Lmhb0N_bOLXH3jxELvhqR8_RSR0p1PGSW_ZUA2SALj69kYOPaEz_wCCvZpJDbgWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنالتی که گیمارش خراب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/98370" target="_blank">📅 23:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98369">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رییییییدددددد گیمارش</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/98369" target="_blank">📅 23:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98368">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خراب کردددد</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/98368" target="_blank">📅 23:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98367">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گیمارش پشت توپ</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/98367" target="_blank">📅 23:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98366">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پنالتییییی واسه برزیل</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/98366" target="_blank">📅 23:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98365">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خودش رفت ببینه</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/98365" target="_blank">📅 23:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98364">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پنالتیی نگرفت</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/98364" target="_blank">📅 23:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98363">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miMDrKIDEcL_Rc7Zr-b8zL9YkXByDB3ZQ979R4PO6E6GTSodHZ-ADLfquWxYx7hY2m18gdnHQcY3cMAbn1A1mIkRSAj_PsBK_HMOsls9gzRixSq7pTyHHcclrTpQ8EvEweA89qLzSZJBaJhkPC4FuQSEJDo-TiCWJtcrJ-lJIr6___36rPC-cv1GskzK_bjgE91nrOjZjNVpE42HChXWfCVZm1mHPferJqt4I4KDoS3tsq3mTHOLxNxzwaxV_68aku_PdFhtbZuKqKWzTghXgtQP5gOn5pbORUJoXrC5KPPeKRLVo8uBBddZecPg3H3kvrdC0fjG-Ql-gzTzdV8KEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو ببین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/98363" target="_blank">📅 23:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98362">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ee365e6e16.mp4?token=GDuJF7Jb_H5WSuvXRD1TSViGNAe9cQF1c7x7jLGVdv5RgGkNvnq_hz8XNmTrmlf4ix-RGOIZioL9nwEms5WyYswzT44JglX35scXBpfpnqw0UIaKK7CocN8ixqU5lRzStx6fio_kwQkKYI3J1BXWpjBv3zLH6gVer2-3pZNa2X38G_sLBtz4OxcSUX2J4i4BcOBnZ83lHcgpPaLNurTJk7mZWpm6hw5xVfA6t1gLg5k0kaDu_g9uAO8a62rHNzOwSjHrrLM8QKUjONspuoauyewSb60wPDxLYQ-yOZUHijc8NiAaVsnCO5HatZ2x_2JdeNc9yWwXRgF6wj8ro4309Utn8xzyqIPXNKt18Duc1yCLf6KBnh7miZV1iy7tsWkYXtfm52WVUrBAeU1PZlQ-Utm8-jCXPPwQrxRPySyJxhTUvMLPmQ9TL-iHxrpSSd8R6Mqcxys9gPt-LTEt15cImaRDpM7s5yp1Dc9hqj0UqMaft_rfxrSEfyCEu_aTqYEF_s3YaP2gcMCZXKoEWZtNJuWYe9YsPRj82qu6vWjcMkhuKufblc4_2RHermLDkjwmlBFfO54l8XmP1XHvvRT6JKslox82WTYB8i6nmMgbFRBe3FkQCMh9iE_QO7ZLPH7-1E23A22wkW88kWoGHN3ygxcwu-vLDAOxiahAdLYiA3k" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ee365e6e16.mp4?token=GDuJF7Jb_H5WSuvXRD1TSViGNAe9cQF1c7x7jLGVdv5RgGkNvnq_hz8XNmTrmlf4ix-RGOIZioL9nwEms5WyYswzT44JglX35scXBpfpnqw0UIaKK7CocN8ixqU5lRzStx6fio_kwQkKYI3J1BXWpjBv3zLH6gVer2-3pZNa2X38G_sLBtz4OxcSUX2J4i4BcOBnZ83lHcgpPaLNurTJk7mZWpm6hw5xVfA6t1gLg5k0kaDu_g9uAO8a62rHNzOwSjHrrLM8QKUjONspuoauyewSb60wPDxLYQ-yOZUHijc8NiAaVsnCO5HatZ2x_2JdeNc9yWwXRgF6wj8ro4309Utn8xzyqIPXNKt18Duc1yCLf6KBnh7miZV1iy7tsWkYXtfm52WVUrBAeU1PZlQ-Utm8-jCXPPwQrxRPySyJxhTUvMLPmQ9TL-iHxrpSSd8R6Mqcxys9gPt-LTEt15cImaRDpM7s5yp1Dc9hqj0UqMaft_rfxrSEfyCEu_aTqYEF_s3YaP2gcMCZXKoEWZtNJuWYe9YsPRj82qu6vWjcMkhuKufblc4_2RHermLDkjwmlBFfO54l8XmP1XHvvRT6JKslox82WTYB8i6nmMgbFRBe3FkQCMh9iE_QO7ZLPH7-1E23A22wkW88kWoGHN3ygxcwu-vLDAOxiahAdLYiA3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تارتار: از کودکی هوادار پرسپولیس بوده‌ام و به عنوان یک سرباز تمام تلاشم را می‌کنم که پرسپولیس موفق شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/98362" target="_blank">📅 23:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98361">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آفساید شد</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/98361" target="_blank">📅 23:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98358">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گلللللللللللل اول نروژ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/98358" target="_blank">📅 23:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98357">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بریییییم سراغ بازی جذاب برزیل و نروژ
🔥</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/98357" target="_blank">📅 23:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98356">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jF_SbUUXvAj4GH1Yi9xcCqfTXJU7BNNUwWZDAmBn8JybkbH17OWu7f2mSUs7r7HAsJ7IwiL0Tar1rtpOI1vA-k9e2gugukP9WVMepjvWlg6mUAW36MgCd5jCeUYW6bZj0D8ZRNC9I-AYB4tIoGwCsaljad_Be7vFRfeCXVeWP-pSzljPy94FlZiFWDPdynFwlqRyQGrYLOgALKF8e5G7GAiVndEssLq_079pMYSP3070sLhwfMLN5Eyagd7qwBzCJNNoCChPHvd7BgaixOZrA3Y_has3HL4ajQ1VMRWZOO58JkYmN6D0SjFYh163Aw-nxQnc9B823ysM_ENYAC3cig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پدر ارلینگ هالند:
شاید روزی انتقال هالند به رئال مادرید اتفاق بیفتد.
چه کسی دوست ندارد برای بهترین تیم جهان بازی کند؟‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/98356" target="_blank">📅 23:13 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
