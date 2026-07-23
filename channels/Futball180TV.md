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
<p>@Futball180TV • 👥 540K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 11:27:00</div>
<hr>

<div class="tg-post" id="msg-101628">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lyt0d-_L6C-mapZoWnLjEv_zUdsE4R6ouxtKa0W-3z-gpwnTms6ct97d2UTvAwEK1tcO3enI1--dGLbcjfeECqvofps6Iy0mwOfaWpMLprigsZL0pEvylO7xXyBYTyfE4dAfme7OsGAezLT5BZ2BUHCcnPKpyuNTg5l2GmFXigdOaUGyfz-wQzBKQjIJRviXE-C-35QIt_0uXkrnh4W4xf6wy1j-19K676cHLeC8lvKrApnCTMj3woMdvkfTbFowoULd5QT-6Gqvmh23xXH62WamBvRmrrho5vdFN3jpHJfiCpvZfE7HglRybaJTKHJ5e1pzxEmVdzDgNsrFSC65nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🇦🇷
اسکواد احتمالی آرژانتین در جام‌جهانی بعدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/101628" target="_blank">📅 11:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101627">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LT_eFdm72l0lDVzw7nqmggVL4Sd5uMCwchlMXu4znszUaqXhOO0huZkmO8gRzXoT_gRlCQdn_r40TJhWDKI94ZlqPtipvS7JvhOfWJ3LnKJSwts3Y9IkIglzdM2_pWmgeJ6gPhg_J99B7iys_Lz8vBGKAa-7md1dcHspP7mMasrxcnYZASbRebX0DufYrp00wiGSNCt5sgS6njF7v6UOEuQdGf6t_5J0HvZtFrbb4EU95GBnBtDTPUVwIFEAZsCoCaeUihYeMDuttUPRVySMA9K1_5YT8sRfGA3dpQlScfde7VXQ_ShopIMifHmRUQUEBs4WYmLDrrjyE-0Pe82gJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ نیمار بعد حذف برزیل از جام خیلی افسرده بنظر میرسه
- نیمار :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/101627" target="_blank">📅 11:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101626">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBrI-Ze5fOWwFtY6qfxsWI9C-uFBchttRDRIr_C0g9lwbQtmzxAaKI0jIt_dZ3WVYJW68ZnkWpyf9e1yjiqKcsjNZfmF7piZqZc_BpX91wyoD75gS7-IYTWR_VjJgIS8UM8Bk33OJw0C4tR6VXFD5MlNbo3abIJF-h_QNsRIvMY0rnWEbn9f9Q7iPw0NBogRnRZsIj7gTASbj-cVJnB45NHkILLNCJeMDGKOf_8v7y8B1UT5e_r_6G2GSoH4A1MobA9iQ2QnC2ha24adDRY_833XCT7ogiS9YmhR5neMJo-1Y5u1K_3NlYXpSsCuZx7JcclzOxFpDd3LqWzI1rfQJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
😢
خانم‌شکیرا و چنتا از اساطیر NBA
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/Futball180TV/101626" target="_blank">📅 11:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101625">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuWdiwMDrh7zpU6uCZTWJdexgp69So8RZjjUSGtsOkSs7zsRA8DiOhtmBeie4nUDNoF_z9Y97s1_qdFBHMd2WIMJd2can0C8XWMjTqAhTMowemqh17a2F0pFdWchZ5Ox_CJStQ5Vc_58qVN3Grde0EeXiE0AdhNQxnRmpemZGjyb5gMlyulGzNgvYYEjv-DqmPVbb1Y_dRw6k03yU5fFGE8M97HD2XTLJfsH3Urqn7p0zq0r04iTJ8f-oazlXyyVM1VNvWsz15NYhGUxeP7BqCkaFxO0157h8Muhhv6y297o4Ln6Aa08VAXc4if0l6Q8_dDpfGHeVMeimdBPv_qs1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚽️
لکیپ: انریکه و پاریس تا 2030 برای تمدید قرارداد به توافق رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/Futball180TV/101625" target="_blank">📅 10:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101624">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/Futball180TV/101624" target="_blank">📅 10:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101623">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/Futball180TV/101623" target="_blank">📅 10:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101622">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/101622" target="_blank">📅 10:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101621">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101621" target="_blank">📅 10:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101620">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBnkEy5wgbBu1Yoz1HJbbH2BV0L6U6npaueS_9SLljXhol0vKx459pwVlnxReP_YtmYR1gMu_FuNW1P8IF6Rcp54qZVvmIagGKFFm1mThqLtPDv8uwzzXo5VwbIjj4iFalCVeYOiydhyKNWs_b48jAp7YgmxlLq6T7vpXhSzVrofIqVpb7mjHTQC8pvC1Lg4Jw1UKjZ5wqLgrG58XeKQOaiwHc06wPsyqFYxZUPJsh7_SFcLfWCKis8U0MktTBd036CL9kHFxzcygfHHUGyAseBWyMXkxxEM3-UY6-Gg5wevVX8nWNDrX4PqouapDNkW0d-8m_mP8qvWdXMXI4kvAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
استوری رسول خادم برای عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/101620" target="_blank">📅 09:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101619">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/101619" target="_blank">📅 09:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101618">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/101618" target="_blank">📅 09:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101617">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101617" target="_blank">📅 04:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101616">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/101616" target="_blank">📅 02:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101615">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsAXcR-s_olgEOWnNWf-OKCBCqSG6U6YNWdRuueK0oLPslTLrQY3aQrY6R0dTv7poMG9zfaSd5R_Wsuzw4XanyPPq9L5E5Uvz5ba0PvUHgwGoGMljfwrHIsJ6HTapN1lbtjBdvbcCXXc8Ix9H26TFf5O9aioAWo6X66oHgWlhqyyTBRKPLIC0BidupI12VxiITKBJRnbFgXfmTdRbFsXs_RLetAmSJrX8RV81DoJoLdApYSjk_pQGHm2y3ntX1WjKiJz9vbGK3I2bT8lrwuJAEpr2kSRewOl-VjU_benDmUe2ls9rHDgsfkmBQtsioJPIAaFEXRk_bxLkeZvEofS1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
منچسترسیتی درخواست اولیه 100 میلیون یورو برای فروش رودری داشته. با توجه به مدت‌کم باقی‌مانده تا پایان قرارداد این بازیکن، رئال‌مادرید می‌تواند با رقمی کمتر ستاره اسپانیا را جذب کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/101615" target="_blank">📅 01:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101614">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNzb0TmAJITfMIfkVoRGtFp5GYAAgJwjwRBKbsMuHWKJCUZgNAE062O_GIVyGWGHe-653BgrngkIcs7VUt5EvJTcYSZQyKfABjBBN8Fq6EnZ50uIydOrOlNwxbdhp244D0SSqUAnWhK85mNp9xcOS4ZhnM4J5vgUFcI4-v670shQwdzbTA_uOQKuTJ5_kz5qJ7AuKFMQdMA-hNqw_wf693IkdAWqBIyZxFH7nXiJL20wdhACWaIppB3ludi1g1HDIaFCQxqnR5FqPouRr7c_cVPZe094a3DduP0AkSfUAS4_-qan2aBQ3ieKitTA5VIu7yS-DQy0U1XLAmLPjGizIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
منچسترسیتی درخواست اولیه 100 میلیون یورو برای فروش رودری داشته. با توجه به مدت‌کم باقی‌مانده تا پایان قرارداد این بازیکن، رئال‌مادرید می‌تواند با رقمی کمتر ستاره اسپانیا را جذب کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/101614" target="_blank">📅 01:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101613">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzpDWBjsu4wttz-l8MdcBMOH6PbfronuR_YfcP6jNwe-frab7qEG6SfLpU3lWz44jxH5CyCOFYMB_0rPvNb2wYPgkKjQGwaGkORNoneVuRKpKcXcKniovXCbo946PdYRqQQ-cYAmv-6l_e1OU_BhVT83BNBv9rez5Wl0mgv2COUsBDNuaY39940DMiylt6AGCJA5NTcW-DUT01rUas2tD4ZbXjmXLh_UfZhVkzH2oRdGAvxBbOkIyd7ILYlJTfNmlnbQeGHpWNzXmV-T9SgQJc0MtSXS2cKBCtydx82PCtUwbkiHe3lloHbiOsW4NZPVx0WY42LLoUhkO1PABjAswg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوید بکهام از تبلیغات تو جام جهانی 22 میلیون دلار درامد داشت و شکیرا 17.5 میلیون دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101613" target="_blank">📅 01:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101612">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krGP69CagstrhK3_rpQY2fd-zVrvnrAREuO8xp2CKbgn2vfFA0dFMBLk8bEJ-q2OrT5LO-RJ8Xcp83M_eEfJEL9e3hdg41GFhhLLjWj3kEP9hGGeHpWrL6NXSKtrj8hAyICIguRL_mImWy_3dnZEwUdLU4Ubaw9K8AOZPVmw7diZCqqIFK7AhjS4zg-xfMoZHnx__64L-1qtvttlSAzRWU4e422GSAVj6uuwTAeWtv930AH0ics4KyiyB_25j5PTKZyC4P4u-AJ6i1RKZE1uqSxtq_NmT1XpMoFeKMAwrp5lkC0jTt7cA5mZqShl7Kmn9au9TBvFu4zDCnphaM9Eqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط 3 بازیکن فعال حال حاضر فوتبال این افتخارات رو دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101612" target="_blank">📅 01:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101611">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101611" target="_blank">📅 01:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101610">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NfHClRqUXn5ljKMEKvbdTa0G2fT2dgOb9nKfeo0T20qnSLXwHcLC2Apc8wiPXCG6QG5g9QG0HzEVdibI7kIWQ5TPPa0SIuB4tXeM_SUKolAKJBYKTjwHCz7ZKFkDl5SldBbVH9Jp3p_hTPmkDDmMrl34g_k0LqeypoYZv090T5xSmNxuJRsckSL508szl4Z_Br8KkfvcJP4fGCY-X6BoCbQCPAna2b1a8YVub_GyNhPSc0KslfyiyFfBl82sbEeVwpqubPZVm8SobLx7vbLvJXGGc-C4cnAHQQEmb6vKhvZUo2XT1NJdPy40vE_phtAib9XAZRhxLOuqm-taY7PBTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
کیت‌لورفته جدید رئال‌مادرید که قراره فردا رسما رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101610" target="_blank">📅 01:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101609">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
⚪️
فووووری از پپه آلوارز: رودری با قراردادی 4 ساله به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/101609" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101608">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEJgF-00RqzjhmIKZP4yr21nVZ384l-0_hz7tNe3jFB-tTbgsHTllZJtSP08yuQx2mkDwZowhSHHuxrguNAYeCy4p49PzOfNqyf2RxjzTbDJHmI16bA56FUSJuyj2O2nOWh51HtdNkw9gXX1WE7MfXVRJwczR-yHfkqIp5wctVShIKnfHNNW4GRbNkYoy6ICSQtnSeW8jJeTY0MnxAP9Mbv7rDbfjsn32tOe3Xy7WbXJJQx3wnaR6Wqz_7ulTBligs6lJdqafkN0F1KuYV-aOopI7YuWdr_0gTwkdO8X0NBGArD6nScwWyTVgMUo3Ahves3Gv8BWZQKj8EDnznbozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
والنتین بارکو با قراردادی به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101608" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101607">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
▶️
👤
حمایت‌جمعی از مردم فارسی زبان آفریقایی از عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101607" target="_blank">📅 00:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101606">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی؛ باشگاه آرسنال رسماً اعلام کرد که با کریستوس تزولیس، وینگر یونانی، از باشگاه کلوب بروژ قرارداد بسته است. مبلغ این انتقال ۴۰ میلیون یورو است و قرارداد او برای پنج فصل اعتبار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101606" target="_blank">📅 00:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101605">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GVerz-TBpR7RioqH4lldukGhwu9ku7FocDka7LR91bG0OySzpIB4JLi42yWGahYoQvsnSA0uqeVD03-UQ6yDSeIZ5Kf8hKreiGY_EVv7M2E-AW5Dx9ShxO214fJOwZ5GeQ_f8WZD8nStjUQJNI-pLUYHQsketZHTr5ZxGlLL_8Jsz7TEslS8TaevgW2AvfRfzw-vgHuQ4QqbPz5ZxPdwFFHQrjpNUydOqqLWZN4cwViemPBpzgb4YUvaopySD71obA92WCX8HZ91a2EppThnIyoTkMJgQBDaXPnpELaZzTY5mKublcL-HntMEBudkrzGD9YJbnd_4N5X83iD-T23xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ باشگاه آرسنال رسماً اعلام کرد که با کریستوس تزولیس، وینگر یونانی، از باشگاه کلوب بروژ قرارداد بسته است. مبلغ این انتقال ۴۰ میلیون یورو است و قرارداد او برای پنج فصل اعتبار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/101605" target="_blank">📅 00:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101604">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcPiwY9YYwsesXe9j95MOtaqc-RJo37WvlL4PpTZA-2YH1qNixE_weyEVU3YgoSTpjFiuxs7A8uukqf5XREVonCALXyWxXYNBwUfw5gzT2mBUUka1crVUEkzF6Y-w2AiVLY2Sez-dgg6MLNZM3X1KmDPNFFH1tLPMyDmU_q_iNGOUyA-k_G6QLeUftAkp4KZ4F_8pIXXvxC16tXuIgqCihmRTW-Gx6V-zy0ZYKaC2VRtlqPLAkiNvoIlULad0gU9qxWUuu_uond5HB9Sk7m7BPHuBLe0vfyDqJNYDFTw2cr5eZkfnGochNgIkBDIN3KgxAcew0Lc8kLhQwaZtQnpWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
ده‌مسابقه برتر جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101604" target="_blank">📅 00:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101603">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jTkUzluyAThA6QEEXr0KH_qCeRVoRYDkViAuxkCmC68wl93d-J7k6KAj5QcunmdsiSyKopCqJjmp4CHHpQLB0qaIGQ1vXNyuFmfCQqG7zcVBULQMpLXpf3cUtEJONq_ygHxuBwjkHoDMoy0lWarRn3Jsvir5aY2aBAbW9Hmhhm04cHl0PCiMv_qgazyWXxYb8uQOu_Q31cJSioLB0mp_MH25N7ZzgQWjWCezRO-vij2sgMVIfX9KvA81OlsMbRCSDkIPu0WAJCejl3A12L9IRhy0-dv7ctpvr_3cEDmMS3l7p85GxhWwEjrrH9dOKlKAWjVBA5U18WKG8Lpeu-n9LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بیانیه آرسنال: ویلیام‌سالیبا به دلیل آسیب‌دیدگی در ناحیه کمر برای مدت طولانی قادر به بازی نخواهد بود، اما تحت درمان قرار خواهد گرفت و جراحی برای او ضروری نیست. او فیزیوتراپی خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/101603" target="_blank">📅 23:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101602">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KxAV821xSUTs-UGxsL7dpvieAhExp-Ws_KTkCPacvouFavZPNmKOhfwqZwbEOlfU6hPY0icobBk5FbydLiTbOENBwVp8F8xa5Vcj8Uigoqg22tsvl81egG9nu0uWJ9BeltN6J9Q7c1nZenwwIZ1cL9jZ0z97-DWbKz1wDdumqLG7ve3cLHIDleMx9Q9Y3ZNscIf2WQqaiHhDMFoxi3RUb9SAGwNY9hhpzAV0h-SSCbcM9EE3TVo_vwlR3Pz9L2SCuC5UZWb8AfLuUYJX5Uqil7eKhmER-heZ5aA0OnWuCIJv6K9y5-pWvRp11U3u4KBllP94NAe1FAGEsxlW515VeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
توصیه‌مهم صداوسیما به مردم ایران؛ فقط کاش تجهیزات هم تحویل مردم بدن تا خوب بزنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/101602" target="_blank">📅 23:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101601">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGAuIJ3M5B-JgrH_3CAICG8fFI04GDI7Zu_IEOEE7Q_nTkt7fG-42OhKlNcMw6fNFZ5kWcpoIWbu3RtV6QUlp4bx1LoQmg5Gug-DlW752fOWhjiLTOzR6-mO9Boi2PoAwKpIB9aZSW4SkMvLjca_sgiBxJLIhdXyLpE6nBoh7GI6TayRvIDv8mZZFft-GP_FFlriv7TLPYLmGXbpXMSW_oEITUaQ_PAWG-ROUzZtdpd10oKJznWJ21VKefDDlBJKdWMo0VzYAu4cKF0DjVWHuTkUn3ly2o0VI3c17XgfR44OSU_oiaiezJV3_4RhdyQxlZRkXQOtCKL4Xj4O4Rcmkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
🔝
ستاره‌های حاضر در لیگ MLS آمریکا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/101601" target="_blank">📅 23:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101600">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbgumHywUy70wC_bO2ZVUVTbrJDTkodd8wxnZv4LxGuQttTr1ITOCehcKzN0VKqyHvWD-9NAGK9JiYHBBlmCKtiXtHXT_eJY0zSChRBhrGKeodBLIn-EyJ3qWHgmcrbgYweZUSbENzhSU66LMsbPlmjG_JEAkCQh9XVSjrhyKVeGLbTS1sci25uMFxKze0FbC7xstD-albKY2dF7f6E7u9n5oG0cod6rgsZ_4_KW8lYDOicnwbVjRq5_X18z7xswDVy_9PZavKgC06An-A3mcjt5fWAqKYdNQUYSrfsb0RwnZMRwByr14APcg8NH9OZZsNN-eLRdp1P2cZVmRU9VCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فووووری از پپه آلوارز:
رودری با قراردادی 4 ساله به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/101600" target="_blank">📅 22:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101599">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYdIvgI2Rs5dWzHrWXB03Gq52jd73TUEpu0gacLNqExdyXlx7P-LuoGWHRGrqXOunCExu6WTaciCT2W30bQgHNnwma3cGFIvU2EtD6gJaRpNZMbQH3JpeHUxPlJJnMgWevw85i1ZB4cPzfoWhJrFaPU0IWfjyYaCMZqMUFl6bGnfl3KhsP_CkaqjTnSbimmrTM254Vxy7g6-T4qrUwgMXAlpXeQC137Korjrw8PdYKPt31rmc4zG4_kzeKBOvqdFGEQgITGEyeNRSiLAi1JfwD2GDYYT6O69shXIKmgM8BVffdMaG7715Irdweeec8eIw11VVWSX5gE4dhnbtMn05A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فووووری از بیلد آلمان: کیلیان امباپه به فلورنتینو پرز اطلاع داده که موفق شده مایکل اولیسه را برای پیوستن به رئال مادرید متقاعد کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/101599" target="_blank">📅 22:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101598">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJBgW1j2FkXXsNdO3toeS569FtVQtt756Imht6csytsc2Gi5wWGbRf_D5JYQXO1uIlfKoI8cYe_t6p9LDxFczwrvlY1UhaB9OfSdMcEKVR3pTlNp65AzGCze5DjOShTT278ljeRk2M_Pg8KasF_S862qJQSW-8NmQR-qQ0tMlHQ-onVap-u6pJI_IrAnegcpssBQptczlC2wbjOKP1Rx9YceelS_9j1saddkdrGrQFcpvDl-4QDwrRcY6_wSoKfaOd1rntHagqON0u5_V8-m4EZXBy1laNPUT4tmbLwzvguc-o5D3bTU2zUHodZRu9bm0ZDcw98ohHV3S40DLPb6Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکلی که وینیسیوس این روزا باهاش سروکله میزنه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101598" target="_blank">📅 22:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101597">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpuI5fC9tMalj-E456SJIu6G7lCEkqMzbXZqlkbQj63HwMlXlBkvPP4jYTTp6n3XkV-3ZFp8tL4DpqfN0GdUd_12z2Kjo9K1UGLe5fBq08VX9RZDVX1lHJeS-Ujl4g5C3ZSwGX8H5od4fn5fn1tmmu8hNfGM9DX81r1pbubg4LSDaXgd4EKUqY0mVzxfZfsCDfI75Enb7Fohm1CxNI3v-Cb05BVEAnmRWkOJVqGFZAeNG-QbVj59W63dJL6dRE1KPKvaGNUjsKpO_faUdBQejX58J0MUenDNlbauCu_lQK0a59VlPwQse80ga_csKdsuMn1E_JXumVWrrVCmcrjMTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فابیو کاناوارو:
اگر من بعد از قهرمانی در جام جهانی و کسب عنوان قهرمانی لیگ، توپ طلا را بردم، چرا پائو کوبارسی نتونه این کار رو انجام بده؟ به نظر من، کوبارسی فصل و جام جهانی حتی بهتری نسبت به چیزی که من در سال ۲۰۰۶ داشتم، پشت سر گذاشته. فکر میکنم او بیش از هر کسی شایسته بردن توپ طلاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/101597" target="_blank">📅 22:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101596">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QR4KxT1KPoSzzsMvHkGjby-8UcdIzFKPEYQj9A-rKq0DRlptww24o7hZhVpS1bxPLaaoCKPePewccqc2mCm1tBjNib86xOQnFrfxd_T8cmiKji7-lLumOZuRaNfYbzbMCFIysCWr-Z87hxlbpXbFSbw1koO-UTdIjz9cBwVRYj0gihas_ZY4m11eckyS8tVinGJVnKjLVNx-NczMFbCpqFIJnbJXupuACEmDN_2Go2_2nGDTZku8QHlb5I7qEjIO1fEafAPtcx5XhLCyI235ibM253PvwsZfd3-Hx1qJi8wE5KjZPEChdGEQ0-ekCc9-44JjwrAhKRZzWg5yVIYXqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🗞
رومانو: سامرویل ستاره وستهم با مبلغ ۵۵ میلیون یورو راهی الهلال شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101596" target="_blank">📅 21:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101595">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN23a62WMQrZQeGRlt-dticzIUqDy7Cc-jfvo7mZ_B1pIYJc9GdSeP6J-puqiQcOAj8dLd38ixVmrVeCkDE3qo0PptUn-8eGCZNQhijzp9dWhlrLv9aPJdyXON5Dl8N3x1L_K3iBeqquPwAUyEG2XYKIo3CI_PJ7O3meB-vLH1auVIRqpyeM3_Y2LURFKr6lcYfRHTRqKlk1u4z_UrVyPAAPhDqH85Cw6kbHIJT3TzV5S9UY-TiuE68oEJGCMvgyN_QN6zQ9GdrEkq6ii4-czxtKB3GiY96S3iTZnBZ_6IP5lcF72EB1oN59P8u5xu1D0T6Zwj7NFhCGffY84s0Pkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
لامین یامال ناخواسته بعد از فینال جام جهانی یه تبلیغ خفن برای یه برند لباس جور کرد! او چند بار توی بازی پیراهنش رو بالا زد و لوگوی برند آلمانی 6PM رو جلوی چشم حدود یک میلیارد بیننده نشون داد؛ اتفاقی که باعث شد شورت‌های این برند خیلی زود بعد از فینال کاملاً فروش بره.
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/101595" target="_blank">📅 21:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101594">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101594" target="_blank">📅 21:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101593">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
#فوووووری
؛ دیلی‌میل: نیکو ویلیامز ستاره تیم‌ملی اسپانیا پس از تعطیلات احتمال بسیار زیاد از بیلبائو جدا میشه. آرسنال از مشتریان جدی این بازیکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/101593" target="_blank">📅 21:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101592">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/101592" target="_blank">📅 21:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101591">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jc4NnRrTdlKE-dFRh3pertCs5RBht0tQdoC_-kuvHbcjT3IeRTLqKVbqFTGvjqSLzgWyiFIHUZz3chi933zW7axkClz-gHK5ZqKBFsVXa1JfMPZOvP4VQG5I1nxibA10OPdV6lZaurOytqeyKOd1fCMqK7-0XZR9WEKmemu-8HFgO3A1PHnObAtVu-oc4GUVKMf3FPHHm19p1ilMDOI8cDVo2XU5glD0akrflStpt7P_TC14IOAgmhuGFOLMthJx0iLPgpAv3DP-TnhMHALrZGPlhB6DXURlgp3vbmwm4pyqDhk4HTKPMgINduQtjQeMDGdaSmgO4R72GykHr6WoOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ یه پستی رو گذاشت که توش نوشته : پس از کشته شدن سربازان امریکایی، ترامپ به سنتکام دستور «دروازه جهنم رو باز کنید» و حمله به ایران رو آغاز کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/101591" target="_blank">📅 20:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101590">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsM1MUvrqwNdYulM0FlDXzRZqX9bKxoedcKJMDuQnZSeqX_uE-kefedSwbn2VX-sqGirI32mEjW7oKHqNHdvJF9DHYDbSnYFLmeyC8brUY2blarmqtldUhAMBTJLsAX2drgNTAcIGjvaRaeiIg2Do76K9EKWrfKUm0o2cOxICk_EKWrBeh5cE3XkD-aWjrKxGA8NuuHS-ZutHO0S0aA4fnlVfgWElwNalxM6JPCSn0kqfimn9kpaRsFtcBE5EIbd7IdHCWpPWGqEtCElgqKMYUuI9RfFIZNGCTx9EaD_LalQa7mzfiiqJVo9pAR26rAKlAfX5MBdAwOyYldQfmHSWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
کنفدراسیون فوتبال آفریقا اعلام کرد که این مسابقات از سال ۲۰۲۷ با حضور ۲۸ تیم برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/101590" target="_blank">📅 20:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101588">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101588" target="_blank">📅 20:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101586">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101586" target="_blank">📅 20:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101585">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IettCqTYuu4HaEux2BIcO9iEfYYqHtHkh464g5hrjhD2U1qUUTQ8EvRHB8urB06UQp876V1gc-xmpf1GrD3IFKCUhyBCcr92M0lPXila9soRC118M4QRUwK-3v-LQcaV2A1_OpsJczhkjUGVhIPgqossZo98Br_IZAnKtcuEHnGPd89pXENI1fUA794cusEw-tnL2pnJhrDS9lWQc0ec60jIOZw2TE0b0lvzONxAQ6XO71glIgasaske5in6iU4xrhUuNovci3k2LbHytjPfP7pTCN5GZir1o4Lq0nCuuyRULCztC4NLqPR8tKzzP0jVt-CfxLcWHTbnw4qRBrh-1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کاسمیرو در انتقالی آزاد با قراردادی تا سال 2029 به اینترمیامی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101585" target="_blank">📅 19:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101584">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ansNckYq26VBoZCWkYD_9JqqmyOyXpBnAZaW4JmaIoZOYFmOGgcWgDTwQdq-als-LjosutiBQMlN_2TFFp_lurTfInnjuKdvJa3H9yESGlGII_Wx6f3xYbnwptjPeLx9y-Tc-KkWH2u1LNcpLMI4biKAEk83uyxpPRYcEvwyP2jlzg3sPCssjbU0X9KajtJsSzduqtcAWD6zKBkAgRXT6i2K2fzEKsDiE9h9pnMmB2KvY4JM1X5TGfVU9bcBqW01S6GNjDw4WYGbpdupLiUfTHJRyVzyEGCSIkovnuCEPjFdXYdKLOURgPclBIRunck6xpJMgUAy0g-_BhIvoTt4QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: گارناچو با عقد قراردادی قرضی راهی استون‌ویلا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101584" target="_blank">📅 19:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101583">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101583" target="_blank">📅 19:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101582">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5lREVv1eyZKLsiO4n7a03lqoeHCeLDWuMojF-ILCcXGfpVIYyTEsRgDCKTk1vssw8qvlWSJpQX9OnzEGGvDZXCXc9W0ATGMJnSJjpc0zrNQbNJ9gXbmFC-mr0qph9p1NQT7FOBDINyY5Ufh8sVp9c5T2PylQEb7o6aXnmvDfwaMkEz74FkpAZjtNAEZsm7exzsvu6IwjCR07WDVHEY35ilXnYnMMIBWWF5yBG7ZVGMqzgRLSn_jsTrB2zcIHqU_VMRSHT4T9gNh3g-0cz83HrMr9B4n8TL6vGBMFeWB9jR1237MZzBvpgm2wOT5yWFCJdpPkr0cSd9VkJDq2ak1YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏امباپه در این فصل آقای گل لالیگا، چمپیونزلیگ و جام جهانی شد و در نهایت هیچ جامی برنده نشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/101582" target="_blank">📅 19:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101581">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/723401c013.mp4?token=cvNEqpQy-FpBc3bH26FRVGkEYx2z0eywtr_w6R6C99s3Ds0pyd82_mc5k6XhwT-tE0BP-KHjCXUxz3YuWCjJLhJjq3xWwVjAHjvZAMFlyDwWeqXeaJHxa0EqmrEl5XDGElWbvGzkRrRlAmHqN9cx5ARdKV7_D4dlgzFAoqR5yvMMg7bCg76Cgt164FLchXY7Y66v1i1y6mdaCKtBe7S9Z89IX-9rJiwRRqv1aBtzgDf7ayV1OxJuui-lhNkvYm6kVvKZZ80w7G-AuNlF82cr1wKpDAbs5KAYs6MsEaF4R-pW6prRFsiouGbrEMiihusiE3nKfAg4yE2xClhzlMgn3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/723401c013.mp4?token=cvNEqpQy-FpBc3bH26FRVGkEYx2z0eywtr_w6R6C99s3Ds0pyd82_mc5k6XhwT-tE0BP-KHjCXUxz3YuWCjJLhJjq3xWwVjAHjvZAMFlyDwWeqXeaJHxa0EqmrEl5XDGElWbvGzkRrRlAmHqN9cx5ARdKV7_D4dlgzFAoqR5yvMMg7bCg76Cgt164FLchXY7Y66v1i1y6mdaCKtBe7S9Z89IX-9rJiwRRqv1aBtzgDf7ayV1OxJuui-lhNkvYm6kVvKZZ80w7G-AuNlF82cr1wKpDAbs5KAYs6MsEaF4R-pW6prRFsiouGbrEMiihusiE3nKfAg4yE2xClhzlMgn3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
علی‌قلی‌زاده: در عمل جراحی رباطی که داشتم، از یک‌عضو جسد برای پیوند استفاده شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101581" target="_blank">📅 19:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101580">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4n9VrHt5KrXYCJbepE_JJacGtdbsbfhOBe_A_zHw1skSXPuYdTG5RSbjysv4jnyqky6HVOhtmyqCMkTibzWaNqyzczqRFlbcjZWFLXPLie4tD2qof3Wfn1tQlPeMCioh5YlFdE1hQXnvYMbiN03YiYPryiEKAfMCrrLvaIIkfRGrrM-uWHexl4xZ1EEVTKk7LeNbtWYesxKVNwdF26vQ6kwtGK1NBwmrwpC6oS28yv5YiSLGaBJeKZvQ03VNzC3w5E9j3fIe5tl3LETWkgw5bJ02a1yTO-9m14eeUIWapUcBxamy34Y4EsIcT72V6vve8F3Sivi5yJdrxdlYmI0xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پزشکیان:
دستور ویژه دادم که سایت عادل فردوسی‌پور از فیلتر خارج بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101580" target="_blank">📅 19:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101579">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfkX-Aq3lPTjJEE0QJpHhE0K5C5YllIfx20sEne0XxBAZegfgZH05cAoh55fGBmAwR50bQfixpjQBan09TIErZaWBB71geRBew6h1lbmrsx6toFEtBUu9mmbVGkXnLnNmEprLjCawFZoLZgJLDUhBpVz7t80aFPn6PzEQNMQMLikzq7dvhlGAyDQ6hxMLy9q9s67IUyZ4aLuRzQOtAp5iOVxydXGyoQRTnnAwVrIv_Tla7kH9P3CN7wO2WzbhkPYdmfeTV0wL3IuJnNjX77KYwh1omSmlBUTzdoMVJTiVWexcRtNFKez-EkoB7hAXtIpC_cmCIN_ognMVbn3rp0FDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاد بولی از زمان اومدنش به چلسی 291 میلیون پوند برای بازیکنای آکادمی منچسترسیتی هزینه کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101579" target="_blank">📅 19:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101578">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2ZIrEtOyoOmhs6rhwWQUdTMulmZnb5RjjpAmJveWqXQm6sr5Phl2Z7hWxLmLrFybKXNR_vQjSUNr1ZmwlqoZuwH9pWwPWTsw_dWpax6IxiWraOAtbC2GnH-8811FM7nZq2FY3Q2caoj4UqXskF7wUtNQt-kN-Z0j38dIZ4IkLeffcvxXlxIRQB_meM7ZfoLMIG9jdiLdtCBQD-DQ7WTkFFjN8ht-EDCD1h3LttodNUV5d3ieFNLVQnicg0fEHehSriOWi9dPzuwnyWIka_uQePWLvGVNiqcIBr6h4nNF1MXG10QnVSy4HngwPnaV2AbTq_WxZJUGwTkHaUr8UxYnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101578" target="_blank">📅 19:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101577">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab44dc23d.mp4?token=J-DPDvgdT5Izj9KBZKT3TREe_dAkR8ZI1O6l_5pQfhHdW1F37zgh3z2eg5JF7RjSeLHbSvDdzhqVdkgiqgEbKa8vxlgAQu2fDTpITF9SDcPoU6i0SugsM9LgxNVVjv39wyYxuetDbI58YUAPmEBeI1ThdvGGVuNa3QaRS5f89W9QzZTv2EyYi4uUSqccZqKIx1Y7ROsztJA_l2a-pMxrGAZAAzwMANKHRZgjRNgAD3Kzt2lKIDeisb0VZU0k9H4ARAHJATD890XjtKGVVLpd9oijVQRnvWjCHSFpKKXJ5NP1qnwGHKJtL1u0yiEXntYNR9-iU3udf3SK1z6uI88Y3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab44dc23d.mp4?token=J-DPDvgdT5Izj9KBZKT3TREe_dAkR8ZI1O6l_5pQfhHdW1F37zgh3z2eg5JF7RjSeLHbSvDdzhqVdkgiqgEbKa8vxlgAQu2fDTpITF9SDcPoU6i0SugsM9LgxNVVjv39wyYxuetDbI58YUAPmEBeI1ThdvGGVuNa3QaRS5f89W9QzZTv2EyYi4uUSqccZqKIx1Y7ROsztJA_l2a-pMxrGAZAAzwMANKHRZgjRNgAD3Kzt2lKIDeisb0VZU0k9H4ARAHJATD890XjtKGVVLpd9oijVQRnvWjCHSFpKKXJ5NP1qnwGHKJtL1u0yiEXntYNR9-iU3udf3SK1z6uI88Y3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
دیس سیدجلال‌حسینی به محمدحسین میثاقی و عادل فردوسی‌پور: یادشون رفته از کیروش حمایت می‌کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101577" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101576">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0c61d3ee9.mp4?token=OEvXiN5cl5euQCq1mRVMCTHal4ydAywkheg6Hg3-yaLABoPMTM3JtAaTSJtBQJ7spEAlhsDSTtD-c5osUPipxFll4knQ1RmRTvuqocLvNtqgDzpscQESIeOsEzOAV-YD4u57LfCDs5Qrba3j-gqGlTccR3LV-ZPplW6dHOPc9XMvg0mJbvP06oUEpxLXrEKL7eHwiQzuIP4Muck9R07vQRXDyDjnVCZKIs085eWBeJxL8Naf-K39YqMGRkQNmfjffZfXTyPfmj4zAHCuURoFBK5_21b9J2CyfeMZj9ERF7yll1pWEoMk2JLgsINzhoKD5meVlZo_6psyD_Co3LH0AA-ZB5AYnLzaH7rt1KrHn-miuUxIJaMSZ0We486JqdK21ZOEtFa2IC9SfrBqCILbIYIAX0RRlNnNFDUmESnu4AtRCpunLQ1NIBejfrkxPvt4jj-epEAacyCOQP3oF1Wj4ZXZaSaacfjtkhOaSr9mp7CLfOsc5OZde_oy5W4jdnrD5GDahUuAJuGkimmyYlkcTtouKtaHbyZ6Fr8t2yxZRU1PgF95zPsKia3ZrxbTlqn8pEUxoo82wITMpuM33t0oO4jHxqeRJ9w2pBRHRUVKY_pYFp5p-7pNo4cpRGY_QVtsQFmPIJnJ-kel7xPm9EJ9lizzdrDrsYw4Y9OImb4ZZzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0c61d3ee9.mp4?token=OEvXiN5cl5euQCq1mRVMCTHal4ydAywkheg6Hg3-yaLABoPMTM3JtAaTSJtBQJ7spEAlhsDSTtD-c5osUPipxFll4knQ1RmRTvuqocLvNtqgDzpscQESIeOsEzOAV-YD4u57LfCDs5Qrba3j-gqGlTccR3LV-ZPplW6dHOPc9XMvg0mJbvP06oUEpxLXrEKL7eHwiQzuIP4Muck9R07vQRXDyDjnVCZKIs085eWBeJxL8Naf-K39YqMGRkQNmfjffZfXTyPfmj4zAHCuURoFBK5_21b9J2CyfeMZj9ERF7yll1pWEoMk2JLgsINzhoKD5meVlZo_6psyD_Co3LH0AA-ZB5AYnLzaH7rt1KrHn-miuUxIJaMSZ0We486JqdK21ZOEtFa2IC9SfrBqCILbIYIAX0RRlNnNFDUmESnu4AtRCpunLQ1NIBejfrkxPvt4jj-epEAacyCOQP3oF1Wj4ZXZaSaacfjtkhOaSr9mp7CLfOsc5OZde_oy5W4jdnrD5GDahUuAJuGkimmyYlkcTtouKtaHbyZ6Fr8t2yxZRU1PgF95zPsKia3ZrxbTlqn8pEUxoo82wITMpuM33t0oO4jHxqeRJ9w2pBRHRUVKY_pYFp5p-7pNo4cpRGY_QVtsQFmPIJnJ-kel7xPm9EJ9lizzdrDrsYw4Y9OImb4ZZzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
قدرت شوت‌زنی اسطوره‌رونالدو که اگر‌توپ گل نمیشد قطعا بازیکن مصدوم میشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101576" target="_blank">📅 18:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101575">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/641d875577.mp4?token=Y1B8W4gDKf28M8qOVZzvEdzoiLBSpMuADiZ4yDb3Y3bn2921gkvcAdKMsa2OV0yKvDMMinBubj7hIKPUM7c761yZJlEBIPewbgUbUFqMat-DzmpAfBfEezievu6nqT_KxI3jHhGgKFhX-R2pqP4ea7_cSOkJeP7bHeYkTk7PE_0FwHI5ht_uASYH4C24awpl1oHLPLDQPtcWIQNKasTFxcKIcFl24IPSV-cpWvdkoOZk6myJiq1haYkB7aPR7ggAbfJ3HW5RfUmh9fxZNuHewnl1zE6ebIdGmEeeUyZQqrNgsPiKpowbEwd6qoFOfoLDS-SjwcuzWh-gNUW7mBlTTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/641d875577.mp4?token=Y1B8W4gDKf28M8qOVZzvEdzoiLBSpMuADiZ4yDb3Y3bn2921gkvcAdKMsa2OV0yKvDMMinBubj7hIKPUM7c761yZJlEBIPewbgUbUFqMat-DzmpAfBfEezievu6nqT_KxI3jHhGgKFhX-R2pqP4ea7_cSOkJeP7bHeYkTk7PE_0FwHI5ht_uASYH4C24awpl1oHLPLDQPtcWIQNKasTFxcKIcFl24IPSV-cpWvdkoOZk6myJiq1haYkB7aPR7ggAbfJ3HW5RfUmh9fxZNuHewnl1zE6ebIdGmEeeUyZQqrNgsPiKpowbEwd6qoFOfoLDS-SjwcuzWh-gNUW7mBlTTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
علی‌ قلی‌زاده‌: کل خانواده‌ام استقلالیه ولی من عاشق پرسپولیسم؛ خیلی دوست دارم در پرسپولیس بازی کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101575" target="_blank">📅 18:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101574">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdff7389ce.mp4?token=fQMUS9iQYTINA2slQ334sJ87KSuGv-ITmHMd2gyxtYRYMGsBIC83Ma7sltg-5m-RNyKk4QpY4HOvTfxtYL5Fr8bluxgQV2_MQTeoKjzzQxwQjwfR8unP7hTJLBnnDnToTuuZpNMoRDGPMDEZom9Wuc81hkFOxEUTUeoHIwIatoHXwIH5NkZmrL3XHnu97SEfQe7xZBCY7aGZ8MUsxbsobk7wJpibpjRhGh2s0uU4FQ9KMEE5sU3B1WseOtSCztUTVVmWhDEmsf-Sz-Iw7BjaUYIlTLhpFM5giHidAdwWEtNGfnjOmcqIFOzt0FC7WJ9quZSuQNcGE8W6Yz5IP5z9Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdff7389ce.mp4?token=fQMUS9iQYTINA2slQ334sJ87KSuGv-ITmHMd2gyxtYRYMGsBIC83Ma7sltg-5m-RNyKk4QpY4HOvTfxtYL5Fr8bluxgQV2_MQTeoKjzzQxwQjwfR8unP7hTJLBnnDnToTuuZpNMoRDGPMDEZom9Wuc81hkFOxEUTUeoHIwIatoHXwIH5NkZmrL3XHnu97SEfQe7xZBCY7aGZ8MUsxbsobk7wJpibpjRhGh2s0uU4FQ9KMEE5sU3B1WseOtSCztUTVVmWhDEmsf-Sz-Iw7BjaUYIlTLhpFM5giHidAdwWEtNGfnjOmcqIFOzt0FC7WJ9quZSuQNcGE8W6Yz5IP5z9Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
جواب عادل فردوسی‌پور به حرف‌های اخیر قلعه‌نویی: بودجه یک‌فصل تولید برنامه من از پاداش سرمربی تیم‌ملی قطعا کمتره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101574" target="_blank">📅 18:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101573">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDSXiHCNHselNAe_1cGEMrGF8dkPfQF43M-Y4I-K09iJwGvnxNCP-i8qjwIyBypUBaHZdYvRZ0U7pSq42jxRj6UElaSV_p4KBReY202hOOyqiD-fZO1S5A4-2cW-9veyvXX0Dlls_yxd1eJYJ100g1aHzwa00UdYF_uMhOX_7EE9AHFK42oAiTs2hdKA_tFTcC5Fpm9oH8d9UBCPxez9E6bk5Hn_DuefYk6a_ZJRmeh_KlptfmywUJ8TlL0bQqICJPzZTj2nSo3tCDDJlKa0Svbk-1qLoEjxjV0Sxoj6_-5oNgL8f4FfrVSGb9B4AAzA3FPVfNMDW1i497kQmOyADg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
👀
فدراسیون بین‌المللی تاریخ و آمار فوتبال (IFFHS) به صورت رسمی لئو مسی را به عنوان بهترین بازیکن جام جهانی ۲۰۲۶ معرفی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101573" target="_blank">📅 18:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101572">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f420d24855.mp4?token=X-hGiuHc3Vqswcp6eZlN_8PHl82nGryOzNGTcrwvapwzewXU87PubKY8F9oeFS3UGpgAzm5niLZQXk7-8xPsMvzN8Pq0pJnOOArY5yRDxXZCM21rFz0kCosSgr7ll79tMbTaGrtey6_XoewKB8nbANQXDyMZpiuaCb59mKM8nbd4JOKUGJOB0U2Kn2rLi-RotzmgI2PGYIlQWY9ZCWImHTeGa8G7LRo91iVk-GgJOcMmwaxh4t19zs9YtlI1zZ4bZU127sJmLNIQV3YqjTdoY7gLq1W1HXZL_ZdQgquedh6F5EnBLkbn0XBLUDqn9FBG7wxod1vPJHTupJ1fL_dWYykoPluOTkMZ8w4_Ui75Ln3aRYUMkZHabebwuK5vIcYv_s3KWX_4v2m1hvLYExtot8PafBm37exqNcHPpqukK28jdwYe4_2RhJu70wPpUCGNhki1KxvzkqQnpHeySFVX-XMn_5fuVpkX5iC3MtlMZnM01imBx5TPc-xq43sNFaCnIeGYBIazHR5lgkP-W1XnDJ-faWEH0fT9hiKPEacecHNMfhRWFD-_5ChfEIi3tg303nio7JARx373F_pofMzAgU_aHtVd-kYSVQZ6VcQX12j0536bsjrBOedD_BtFIpfkoI-fLFB7eBA5J7pTYsa8EEA2QN0oX0R18pb81Zc6oYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f420d24855.mp4?token=X-hGiuHc3Vqswcp6eZlN_8PHl82nGryOzNGTcrwvapwzewXU87PubKY8F9oeFS3UGpgAzm5niLZQXk7-8xPsMvzN8Pq0pJnOOArY5yRDxXZCM21rFz0kCosSgr7ll79tMbTaGrtey6_XoewKB8nbANQXDyMZpiuaCb59mKM8nbd4JOKUGJOB0U2Kn2rLi-RotzmgI2PGYIlQWY9ZCWImHTeGa8G7LRo91iVk-GgJOcMmwaxh4t19zs9YtlI1zZ4bZU127sJmLNIQV3YqjTdoY7gLq1W1HXZL_ZdQgquedh6F5EnBLkbn0XBLUDqn9FBG7wxod1vPJHTupJ1fL_dWYykoPluOTkMZ8w4_Ui75Ln3aRYUMkZHabebwuK5vIcYv_s3KWX_4v2m1hvLYExtot8PafBm37exqNcHPpqukK28jdwYe4_2RhJu70wPpUCGNhki1KxvzkqQnpHeySFVX-XMn_5fuVpkX5iC3MtlMZnM01imBx5TPc-xq43sNFaCnIeGYBIazHR5lgkP-W1XnDJ-faWEH0fT9hiKPEacecHNMfhRWFD-_5ChfEIi3tg303nio7JARx373F_pofMzAgU_aHtVd-kYSVQZ6VcQX12j0536bsjrBOedD_BtFIpfkoI-fLFB7eBA5J7pTYsa8EEA2QN0oX0R18pb81Zc6oYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
وقتی صحبت از کارما میشه منظور چیه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101572" target="_blank">📅 18:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101571">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CY_sKteO_GIJdb0JsDS759bK9ve-acZH1oy-GGW2YHjDqRE-NlXo0jBGyHJjupSvrX1HD2Z3StgL3o87M2WEB6EA5wB2yhnWLQP26eSWDON1jGJr5PvFlHyoDBpclAwVd8VbrjaSxRYBkB1v0iQT9HJhvwRKcaiSJk6TPQvwOn9YXsgdIb6hZ1ltToODOrlg6cbVIqGo6qdxyloGOqqVdQmlqgnsD5hXIYRUlUjYiSlqYY1ICBsvJW6E-fifXxEz0PS9D25jRNSWa8m71mHmsGwtwrjix5B3GYKQR9rFw2FMBJ9ofgPt9MINqfnDSWUJrP0HrbvK1vwKYeOEer1ynQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول و آرسنال درحال رقابت شدید برای جذب بردلی‌بارکولا هستند. حداقل رقم پیشنهادی به پاری‌سن‌ژرمن حدود ۱۰۰ میلیون یورو تخمین زده شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101571" target="_blank">📅 17:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101570">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb17487185.mp4?token=K65ZFoaSLPL5VVFUAi2yd6m4xqBQOGcRu-47ziExwNfRHMpuSPxzevKkrhpwdAVjOrfsP32qLBvXKLVBr-0pLCMsnsqwrKqcgTyHTa4rAI-E3_tp9m_5ibFI1W0ikYgfmptO-f1yKpYWV9NTWUW1W0X_3RJH7QpMWZg-PoAFDrRe8zexVrc8w9Y1yPwiReMMrH0I9ZuC1FMGcLEMgHOZoLUPKWgDxC_PkOsO-GnBwX1dLpJKQDtzbzHuZ_uUKTCUKf4ZAYAbAV2OZ-2yxA5cn3jH6HoBkKQaYvkG0atYqTzn8_7ul74zrLXA9NxhNdCJ6OwIStnBsJKku18t51sWEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb17487185.mp4?token=K65ZFoaSLPL5VVFUAi2yd6m4xqBQOGcRu-47ziExwNfRHMpuSPxzevKkrhpwdAVjOrfsP32qLBvXKLVBr-0pLCMsnsqwrKqcgTyHTa4rAI-E3_tp9m_5ibFI1W0ikYgfmptO-f1yKpYWV9NTWUW1W0X_3RJH7QpMWZg-PoAFDrRe8zexVrc8w9Y1yPwiReMMrH0I9ZuC1FMGcLEMgHOZoLUPKWgDxC_PkOsO-GnBwX1dLpJKQDtzbzHuZ_uUKTCUKf4ZAYAbAV2OZ-2yxA5cn3jH6HoBkKQaYvkG0atYqTzn8_7ul74zrLXA9NxhNdCJ6OwIStnBsJKku18t51sWEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت‌سوزهای اسطوره فران‌تورس ستاره فعلی اسپانیا در فصل گذشته برای بارسلونا
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101570" target="_blank">📅 17:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101569">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea79a8c03.mp4?token=Xf1riJsJfvHyrseNjwAa4crzaUTelNts0oTOXQE5qgIBxp4pw7fLe2uzr39-6w3wFRNaJuixUDVywdWIQk9Ixr913UaqXkbnvQVWn_fNyN7qNJtHFjEnq3ebuoQ0C0S6oiNiP4jU9vrBzkT0YsIkTVSxUqyAJoEnGbPdqx3R8RMNJgcW3WAHihThnc0RSaHQrgKsRhRXHy_nK7BP0_LcLC87DHlexp4bKfi4X4JfPmbkXufaBZ0HK87bBvMQSO070nAYttNwnBKipASSF49OoyYf85s2eYagKdEzFRSH5BQCQGfjMhBzHZdXJ1mnC_HO2DqZldaDNhbk8neIArtluQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea79a8c03.mp4?token=Xf1riJsJfvHyrseNjwAa4crzaUTelNts0oTOXQE5qgIBxp4pw7fLe2uzr39-6w3wFRNaJuixUDVywdWIQk9Ixr913UaqXkbnvQVWn_fNyN7qNJtHFjEnq3ebuoQ0C0S6oiNiP4jU9vrBzkT0YsIkTVSxUqyAJoEnGbPdqx3R8RMNJgcW3WAHihThnc0RSaHQrgKsRhRXHy_nK7BP0_LcLC87DHlexp4bKfi4X4JfPmbkXufaBZ0HK87bBvMQSO070nAYttNwnBKipASSF49OoyYf85s2eYagKdEzFRSH5BQCQGfjMhBzHZdXJ1mnC_HO2DqZldaDNhbk8neIArtluQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
دسته‌گل استاد فران‌تورس در حین حمل مینی کاپ اهدایی جام‌جهانی از سوی فیفا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101569" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101568">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8X3oPuD-JOi123iFE_6WNOZXhZ96ccVtDHUTk44_7j4S6g6OOBLevbhR4pWcydCqTIuhP3G1vjxKWLoMDdFZJe_xAlZPaTkf0nC7p3s6eatDoC9tthBY-8C0fzNgys0B7NSpNNBrSeviwQUqoBw2Tl5rYCyQgoZVWfH9w5XrG83ItZ7-le7EpkBQmnK2diFopB-iB5pikw1KYt_Di6dfl7pOhg-Op9EoCecagOAYCVL8ACWhbKSAPgaa6gN6xKGqEwLeQpD0D-ZANil3y2v2Mh9w4le_BUqax7gRi_AWC5IU7FN-sb1YGX_ePxrpPAdS0FjHN5PKAsRBORmKKrDoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب منتخب جام‌جهانی از نگاه فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101568" target="_blank">📅 17:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101567">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38a17a2eb.mp4?token=ERAvo72M2FE8nbTErnDw28NMc6cu1I0UNF1EeJqSVxTXxoLLufYzWmYmAeoAdfqH1wmBgzlpiIUeL5QoOnLZn2ttbHx-l52QJfjhaGpwe2wm_8J30Zi7O3xTFGLeVw_oCLpZZAOwLpunnYY0tNC374Y7azugcEEdMWhNj5VwYyaxsMTFcOJp5XX-Amn6md1bbeRED036dNHreerzo7om05y21x0EqrLsVw-G9v8yJbyHhIDMwaFDbHdZ7FdBbEwgmz-KuA4S7XhBCBqsP7aIhKo3BBav6TpYRTHHh1OBsidkBF2RwpYYIvUyCbM7jW_HYBTK9h2NmJ5lHmtBy3bqUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38a17a2eb.mp4?token=ERAvo72M2FE8nbTErnDw28NMc6cu1I0UNF1EeJqSVxTXxoLLufYzWmYmAeoAdfqH1wmBgzlpiIUeL5QoOnLZn2ttbHx-l52QJfjhaGpwe2wm_8J30Zi7O3xTFGLeVw_oCLpZZAOwLpunnYY0tNC374Y7azugcEEdMWhNj5VwYyaxsMTFcOJp5XX-Amn6md1bbeRED036dNHreerzo7om05y21x0EqrLsVw-G9v8yJbyHhIDMwaFDbHdZ7FdBbEwgmz-KuA4S7XhBCBqsP7aIhKo3BBav6TpYRTHHh1OBsidkBF2RwpYYIvUyCbM7jW_HYBTK9h2NmJ5lHmtBy3bqUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
✔️
پیش‌بینی پپ در مورد شرایط رودری در مهر ماه ۱۴۰۴ که در ۲۸ تیر ۱۴۰۵ به حقیقت پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101567" target="_blank">📅 17:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101566">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be9c5de5c5.mp4?token=c_7EnTaFyMi3n8iqdYvBQcHSfxK7s84JTeGODL9szAqyv5DFZrIqK9h6npdOoOXoiDepXXPc-LfNzuoFsDT67N1HNAIOg9THN9apOH9YLbPIaTAKkPlabI0N5_FSLOVjk0wQdFDwJtAgJAGaet3O5O3zZ7wlTcV8Vempi_UohEhubZuur1GwVEkA1_TMpsqSsIt_aWDnSpi2gzTibumZ3ZbCyVQxMVzhEY5x11zAfY3UHTfcAp2cDFc05O4RNoN9e8MrfHKyiVWKDrPK_z5t_xWM0ao_86silveRyUOaFC1iE-dy5WtkGTV8P02NAMC3X1mK-sNbLNMI68PGp_B8C7s_Xxa4in1b4whwUmD0I-TGIdj3LN4lssZ70edPCHGY_PGhhL-0JBXiz8dGPWXkHbLuCSz7Aeq3zI0SBXPKFjGgOevsi8Yi-74w38sW958YvUhdovCZUcqhaZDbsq8uZhbAUklHT9IWoLdyTGncd9E03huL-3EoOuyQGandJ3lXtlWjrhD0sholrWn1F5r__R8bx1gkjjnV0S85zPmeSbYm3yTX2zWQhaBY9qC2jsEq-UK5W2W8CRSr5ZTMBUEElpMDBMOhjQzDYE4GGauAaveotcc96wELPsA2AlcWz4I2MDO5VCu7I8jdXC6p7LK62meCyENuw0dPhhYPGNRJJtM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be9c5de5c5.mp4?token=c_7EnTaFyMi3n8iqdYvBQcHSfxK7s84JTeGODL9szAqyv5DFZrIqK9h6npdOoOXoiDepXXPc-LfNzuoFsDT67N1HNAIOg9THN9apOH9YLbPIaTAKkPlabI0N5_FSLOVjk0wQdFDwJtAgJAGaet3O5O3zZ7wlTcV8Vempi_UohEhubZuur1GwVEkA1_TMpsqSsIt_aWDnSpi2gzTibumZ3ZbCyVQxMVzhEY5x11zAfY3UHTfcAp2cDFc05O4RNoN9e8MrfHKyiVWKDrPK_z5t_xWM0ao_86silveRyUOaFC1iE-dy5WtkGTV8P02NAMC3X1mK-sNbLNMI68PGp_B8C7s_Xxa4in1b4whwUmD0I-TGIdj3LN4lssZ70edPCHGY_PGhhL-0JBXiz8dGPWXkHbLuCSz7Aeq3zI0SBXPKFjGgOevsi8Yi-74w38sW958YvUhdovCZUcqhaZDbsq8uZhbAUklHT9IWoLdyTGncd9E03huL-3EoOuyQGandJ3lXtlWjrhD0sholrWn1F5r__R8bx1gkjjnV0S85zPmeSbYm3yTX2zWQhaBY9qC2jsEq-UK5W2W8CRSr5ZTMBUEElpMDBMOhjQzDYE4GGauAaveotcc96wELPsA2AlcWz4I2MDO5VCu7I8jdXC6p7LK62meCyENuw0dPhhYPGNRJJtM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمود شهریاری چه اجرایی کرد
😂
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101566" target="_blank">📅 16:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101565">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESoAeKjKSMzxA8p1LJLTrc6megQaia5rKxjojBTYBeFA-nju1Slsn6zagVf1fiqEFpqIf7weZue04nmTiA-ElHem7hYdCshjZAFsRnwqMSWqk2HVUedtHuXbtETb3Ehl1J3H9X63TW9dLED30Jxa7XwUYdG-w4pzU8aGYLLQrNLgghvjd3d3Avdi7wzW2RnBb2X-XCqLeVPo1vgXbDdJQ1TXvGTrlRSW2wjldAQ6IbPASUPpqoBhdWyyvMGxq0D7E3n_fhGCz1_42ZekuaLgJVDk5Tjq9RFZ3ZGMq_YuICt1q-dIsdVqvqGJmYLQ_tFiN90yaUY7MO6cXVejutRIBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ: از این به بعد، هر زمان که جمهوری اسلامی ایران در تنگه هرمز به یک کشتی شلیک کند، چه با موشک، چه با پهپاد یا هر وسیله یا سلاح دیگری، ایالات متحده یک پل یا نیروگاه را بمباران و نابود خواهد کرد، از جمله آن‌هایی که در کنار یا در شهر پایتخت تهران قرار دارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101565" target="_blank">📅 16:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101564">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🎙
🚨
حمایت جالب رضا‌رشیدپور از فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101564" target="_blank">📅 16:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101563">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318ac55e88.mp4?token=CN699ZVLOYaw6Vgp1wvuvMUgSVkct-uH37kw2_gpkBtVj840Qr_EJn3VNbts59iVGHcU1ohlpAsSFI--S6ijhFX_qzGasEgFxRBS-1Iv9Y1vleAmDh2NCI1PyUwQmf7ZIcohbdPk36INqETRaio-gR7DMM4MLrCcd4_YCi758NBpkVUmPA7YIAo7ongKRz7tD7yLiI0iKh6WwvTsfQfSFaXkupj6fqpXmUEqANpFZzEZEp-I4wxIM99hxlbjbndz6HjxWsnee5SSK3zShmljaul4ckyRhI4ryC8ueW1CaMEPT1Bux2QXT0l3wzATmpHu7Zc28x623sFAP7Gz_S6uGKzymD4Sbo63dcFp4cc0O7xMXVljth6tjBos1Z1cHm1XEwcinTkU5EUTSdLtict-NVfKZ-teI9UUVw8gAXs6rnRddP2xoknh16_UcEHJankNzPwKemLTn-vP1zsZ0uR00dGyCrr7WfUWOk8dLvx6PfFa7L9NqpOsqnCGwBTPxQqokMGEf3iVWVgsmOiJKXdtr3yCbRFmYMOPHgMmYvs9qLLmpJEphvUhFZ--n-Y9UMCqY-N6NRFqkTzuLD_FKS-7BpQqAmF8laL-7uDT7SytSRz9aXfgeigkP08k5fRhvE-6yDTGMbHW7N82_HTlBsyw9FMy6Gpf2vAV4VfC3oDbgNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318ac55e88.mp4?token=CN699ZVLOYaw6Vgp1wvuvMUgSVkct-uH37kw2_gpkBtVj840Qr_EJn3VNbts59iVGHcU1ohlpAsSFI--S6ijhFX_qzGasEgFxRBS-1Iv9Y1vleAmDh2NCI1PyUwQmf7ZIcohbdPk36INqETRaio-gR7DMM4MLrCcd4_YCi758NBpkVUmPA7YIAo7ongKRz7tD7yLiI0iKh6WwvTsfQfSFaXkupj6fqpXmUEqANpFZzEZEp-I4wxIM99hxlbjbndz6HjxWsnee5SSK3zShmljaul4ckyRhI4ryC8ueW1CaMEPT1Bux2QXT0l3wzATmpHu7Zc28x623sFAP7Gz_S6uGKzymD4Sbo63dcFp4cc0O7xMXVljth6tjBos1Z1cHm1XEwcinTkU5EUTSdLtict-NVfKZ-teI9UUVw8gAXs6rnRddP2xoknh16_UcEHJankNzPwKemLTn-vP1zsZ0uR00dGyCrr7WfUWOk8dLvx6PfFa7L9NqpOsqnCGwBTPxQqokMGEf3iVWVgsmOiJKXdtr3yCbRFmYMOPHgMmYvs9qLLmpJEphvUhFZ--n-Y9UMCqY-N6NRFqkTzuLD_FKS-7BpQqAmF8laL-7uDT7SytSRz9aXfgeigkP08k5fRhvE-6yDTGMbHW7N82_HTlBsyw9FMy6Gpf2vAV4VfC3oDbgNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
آنالیز بازی پائو کوبارسی ستاره تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101563" target="_blank">📅 16:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101562">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‼️
🎙
کنایه علی علیپور به علیرضا بیرانوند به خودم اجازه نمی دهم درباره علی دایی و کریم باقری حرف بزنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/101562" target="_blank">📅 16:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101561">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🏆
🇪🇸
رسانه‌های اسپانیایی با وجود قهرمانی صحنه‌ها مشکوک داوری فینال رو منتشر کردند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101561" target="_blank">📅 15:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101560">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H93atli_-7jEVc2DushFtxvCuIdC7iXAEmciBPL_RSO-cWOZociDTb8qZCU00VccG9wbNQ2NZO30Wa0I7AU0lD1yvlmcICt6fVl_tuhX9GD7P8KM-zqLxsYkilbJChwu8CPi4YYm27tGiRPqHuhm5jWxu5HAqWCV3U1Q7ZYYiGnullS-iuYeDpijMGSxKu8ofTPprYQccoc0b1tzUBJp3GjVadMeJ219IUDh7GXeGbEF6wQUpaaivaSQ7ovZf4bJQ1aOo5AlkMZGxheTyUCkQUFtp7hxHkyRzil5nZp6dCxmFg8oMJsgCazdaIEZh4Pka1xVpdgDZRj9OrQUW1JxTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
منچسترسیتی قرارداد فیل فودن را تا سال 2030 تمدید کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101560" target="_blank">📅 15:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101559">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e21d92126a.mp4?token=fPQw-Jszb7tiDR9yBi1W9iJml1jVfeggwuJzfjyLPYv76IdfwOG82rVKpiA9M8iTWR5gx1HmXZNTrs6s0UWa49VfsP_5JVmz4Ku5BEgFmJ4o0rdYL67OUw_eTE7TySFFyLE75zeST-V5E5LeH-x-X4g1wmuAMBTikKiSc3Oa36b3L_-R-g3MgcIOHXJbOPQhc-yHYoVCjRrSP6S1bAvhl1x8USkKS7OZ9_DBJ2XIIu0XK_MMYV3j3WH3LQjrlIo90erpWuTLtc1F9xAzwB3zGJMGIH_2fAnVR7iijIY3nNRbLff1td_kxqfyOeMP1hj9l-n_YT0WqF579z2QiLuMm2TTa2fVtiMnDWcc_Ki3uLJ3qrTqFSMRCyhLIRfnRnfyHu5S186z4jUGs0qNJvRoKopfWZoY_VQXNf-Z0iimYQnSbKoS0uzJHX8QWFmWSis3HyZwVtvp76cAgdljbqO_lLytkzPdpLiNQebyUeqAe-UU_GZEDkwJmMvfwdDyjPalcLl5vDr1E--8GkNOZpXy7fJ2OJ0EBxGZqb65_5FcGZmUPVDMy1BPlXHYsMNgcU2s6Y5YLXIMXJSQD3HRL4Dcf9e7MDSepOqXKC2asVfnPMuCWZtlxqesvdg1Rj1A527uVX3InEOsPy_-v6aLAgfpPyz4wByl9nd1c6-OmmAGnNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e21d92126a.mp4?token=fPQw-Jszb7tiDR9yBi1W9iJml1jVfeggwuJzfjyLPYv76IdfwOG82rVKpiA9M8iTWR5gx1HmXZNTrs6s0UWa49VfsP_5JVmz4Ku5BEgFmJ4o0rdYL67OUw_eTE7TySFFyLE75zeST-V5E5LeH-x-X4g1wmuAMBTikKiSc3Oa36b3L_-R-g3MgcIOHXJbOPQhc-yHYoVCjRrSP6S1bAvhl1x8USkKS7OZ9_DBJ2XIIu0XK_MMYV3j3WH3LQjrlIo90erpWuTLtc1F9xAzwB3zGJMGIH_2fAnVR7iijIY3nNRbLff1td_kxqfyOeMP1hj9l-n_YT0WqF579z2QiLuMm2TTa2fVtiMnDWcc_Ki3uLJ3qrTqFSMRCyhLIRfnRnfyHu5S186z4jUGs0qNJvRoKopfWZoY_VQXNf-Z0iimYQnSbKoS0uzJHX8QWFmWSis3HyZwVtvp76cAgdljbqO_lLytkzPdpLiNQebyUeqAe-UU_GZEDkwJmMvfwdDyjPalcLl5vDr1E--8GkNOZpXy7fJ2OJ0EBxGZqb65_5FcGZmUPVDMy1BPlXHYsMNgcU2s6Y5YLXIMXJSQD3HRL4Dcf9e7MDSepOqXKC2asVfnPMuCWZtlxqesvdg1Rj1A527uVX3InEOsPy_-v6aLAgfpPyz4wByl9nd1c6-OmmAGnNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇦🇷
رفتار عجیب بازیکنان آرژانتین در صحنه اخراج انزو فرناندز که وایرال شده !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/101559" target="_blank">📅 15:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101558">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f9401eccd.mp4?token=ArhIdGFHU3oo6pLxadUl07Z-PBqG-MmBLF_C637O7khGzOSUFXVW1LktLntFJ0QxuzVXkCS1EVxfFPPWDvyjRD-ruNlt7goak-z8Qm18bhGOlO0NehYBxtfcPNP7FPvdnZpYIUXGxz7RnDs73_ohKgxrXOs65MXGgr2jkeDQIykiJ_PEowZZzrgOROF_FEjGFCfa_T7pnJAYIhf-sQCTkOSOF6lTaHo3qW1Wrg-ff-QJfhaJGNyoaVkXOb_Mj5yzAuOX_VVf9sx7cD3y3Ejtj_SCFpOkx55qTEM1e2mPOvbBi8eI7cmxOvS6xqnQYlIi2TdrFGlYd0s9SLBWaU55wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f9401eccd.mp4?token=ArhIdGFHU3oo6pLxadUl07Z-PBqG-MmBLF_C637O7khGzOSUFXVW1LktLntFJ0QxuzVXkCS1EVxfFPPWDvyjRD-ruNlt7goak-z8Qm18bhGOlO0NehYBxtfcPNP7FPvdnZpYIUXGxz7RnDs73_ohKgxrXOs65MXGgr2jkeDQIykiJ_PEowZZzrgOROF_FEjGFCfa_T7pnJAYIhf-sQCTkOSOF6lTaHo3qW1Wrg-ff-QJfhaJGNyoaVkXOb_Mj5yzAuOX_VVf9sx7cD3y3Ejtj_SCFpOkx55qTEM1e2mPOvbBi8eI7cmxOvS6xqnQYlIi2TdrFGlYd0s9SLBWaU55wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
علیرضا نیکبخت جواب بیرانوند رو به زیباترین شکل ممکن داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101558" target="_blank">📅 15:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101557">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzb6ffEqw91vdCrlgDVFPZlf1tB750bXB_8DvI80x_LvbwAdRCgvqjtKYm8NV1SuZVMqakfU0qX90jCp54uE1dPy13k-_GUkmguWHHQxd1_kMHZPWTQLni328fwiSUOmcxbvr-HRmVxMum5B9onFFsMHo8pQIH3Zyjs3897WCoJ6tsXwZyclgVQ0-EM6ppz3s2mXh32hG8ZBWkaBsjxSfH5fLCwNBu3emw0aFLIaVtEYpCVNcXhJCkrNFPGvoiZDKzZSOwR_UPtnIffYsBYsiZmNvgldpsA9oUKpZ7tHeZV2Y5JhM0fRcrWDaVNWLVTrAZyRrxCplHAmmUn6-Jpaug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بازیکنانی که در این فصل، در بین پنج لیگ برتر اروپا، در تمام مسابقات بیشترین گل و پاس گل رو دادن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101557" target="_blank">📅 14:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101556">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a761e81f7f.mp4?token=nZPtaaZwZO3wC7LeSKeXkwk_lDt3-GzbJqWJL9C9Mz0D3s7H7Ml7KEeiylJ_sxQ9r5s52c7OnJUd6sDl7G_3GHX1ys4FRoSsYxp9Ry-ec-6OvwEsCHT5VOW6pZSvyNcP8Rt_fsedieIsWA_svly8z7s07i8dkjzbL1KS2WWhvh-PyXI7EIMQR3y0pYRW3HrWGSPpP7wY7DruCGZNmk4hErPDWT73C1UMAZt0YO9Ju8QDrxofMSei33HT9fXZY36Q5pMiUp4wHswcoS08UM-Vjf3WdAmc3A6uMisraDq3mHtA_e1mh5lINXHqowKPI4nWgMaPrQztQPpucZYJ_vP1PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a761e81f7f.mp4?token=nZPtaaZwZO3wC7LeSKeXkwk_lDt3-GzbJqWJL9C9Mz0D3s7H7Ml7KEeiylJ_sxQ9r5s52c7OnJUd6sDl7G_3GHX1ys4FRoSsYxp9Ry-ec-6OvwEsCHT5VOW6pZSvyNcP8Rt_fsedieIsWA_svly8z7s07i8dkjzbL1KS2WWhvh-PyXI7EIMQR3y0pYRW3HrWGSPpP7wY7DruCGZNmk4hErPDWT73C1UMAZt0YO9Ju8QDrxofMSei33HT9fXZY36Q5pMiUp4wHswcoS08UM-Vjf3WdAmc3A6uMisraDq3mHtA_e1mh5lINXHqowKPI4nWgMaPrQztQPpucZYJ_vP1PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سگی که شباهت عجیبی به مارک کوکوریا داره و حسابی وایرال شده
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/101556" target="_blank">📅 14:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101554">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fi9uEWrqJYSxHivtpTyzj5P38F1ZcDEGIR9EFB9kq-POiEXKu-aUr_TAmLnWlgusWUZOfkXhoMEfA87Strn6Gh1g_pDfY-mQRiF0lWEygocxeyYZDxhb7dk4uaAC6mCKTmNMsx1YgATKD-167v6fOrMEK2C7wmrJXVUARzYYexmu6NEyStr88Gdjwtw5yLO1ygZiDNChNxawiAGdO00rGvQxLy0vrXiMZPWc6o2d_6zTyn_0dJGD1wZxGQ4ZvNhzoZJopukU9rF5HaK-V-x9zTGqIat_vEs3317BBYH8iLYNCrEEm4-0ONZG5_mYD9wtZ3mA6JpCbLfQAa8mJTIvAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/npfyKaZl1emvfgEuqmcfxNGTcPZ_n5fTQVxiAyIsS1dx_g0wiToXOUd3JQpUrffloi8xg7oXMIV0SxnA0MJqDS10BYTc91ZTv_jOWT6GHYoHQZ2IfR0X6eLcpW1-WH1HlodECWhmWwuzqpWfT38IgqbnAmreWDi5rQBFBDt_2KM0N526trqoMFVY8ick0FbpunSLrp-i7a1ieHeS6gkHLfsJF-OeRDxtCW5VRMq1kRLRfNermVw-wrU4kgke3C-Ihy0T818RreWe0cCSydswvi0XFH_2HNB6Xl8CTlGoU_zl0PfyvqW8b0OpJUXOyj1NJwHkGH7Tjx2ISewnkYOACA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
خوان مونفورت، عکاس عکس معروف مسی و یامال:
من به خدا اعتقادی ندارم، اما این عکس نگاه من به زندگی رو عوض کرد. انگار همه‌چیز از قبل نوشته شده بود. هیچکس حتی در یک فیلم سینمایی هم چنین داستانی رو باور نمیکنه! هیچ توضیح منطقی یا علمی واسش وجود نداره. یکی به بهترین بازیکن تاریخ فوتبال تبدیل شد و دیگری حالا داره جای پای اونو در بارسلونا دنبال میکنه و در ۱۹ سالگی هم قهرمان جهان شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101554" target="_blank">📅 14:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101553">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAx77uJuRolcYtYKKilB4nAYBRUNosG00NRZQweQuOxq_OIhltMr1gYD-8B6ZNRLODu4CobINj99fuBanS32v_DCPp15R13xnw0amJ9QSzejAEWZVkHclR36hvuSphhPM_mZ_B9mJSJV67WH6C7UCKBRX4bqSqBN-Vb3pXtTkDLBWab8LZwFeFfq1EVCxijBRqzF0kgEdHD9qn2DnE2Fvk5FocafWvm6rjCRbxnHCkkXSwwXLQYlNu-mxEptuIAVjE7n793QL6LQIRdT0bRqZ-zOZmTA6b9c51WqFsh_oJgFElLyDxHy6_-c6eGxmZq4kLPEKpokgklNM1j_h5YwSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیمار دوباره در برزیل جنجال به پا کرد!
باشگاه سانتوس اعلام کرد نیمار به‌جای سفر با تیم برای دیدار کوپاسودامریکانا، در برزیل ماند تا روی آمادگی بدنی‌اش کار کند. اما ساعاتی بعد، او در یک تورنمنت پوکر با مبلغ بالا در سائوپائولو دیده شد! این اتفاق باعث شد خیلی از هواداران شدیدا از او عصبانی شوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101553" target="_blank">📅 14:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101552">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isstbaNfl6x2A1lTPyK2B5k3dCTyd4Nh_cXI5OH0UMzfwceggbHDu5dGxqNIyhh9bd7s_YJxXrLxJwZsXyI-SaOBGieScDc4n2zq_GG8LTfYs3A3fK79hTB1dPWztrEC9-Dl_ecBJNwTdb16cDxhfHtPyWb6YRcfU7KbU5QovqxWDmlUKEY7e1Kyaj6JIlPaUO5WT6-k11bXgcAJzGXVIO6APMuJn-n6ZKph-0aA6WugoIotwgHGtUFRQH4TukYjbkNk78IzHWnRVjQvLAuAzEcVP4jjHpoQObYJMty3IMaTjdcvuRDB8sgNNQz-1p37bRVAjzp86tlD43E3JV3clQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔥
الکس فرگوسن: "بعد از اینکه ایتالیا جام جهانی ۲۰۰۶ را برد و یوونتوس به سری B سقوط کرد، من مطمئن بودم که او یوونتوس را ترک خواهد کرد. بازیکنی مانند او در سری B بازی نمی‌کند. در آن زمان، رئال مادرید نیز به او علاقه‌مند بود، و با توجه به مشکلاتی که یوونتوس در آن زمان داشت، تصور می‌کردم که یک رقابت جدی بین منچستریونایتد و رئال مادرید برای جذب او وجود داشته باشد.
🔹
بعد از اینکه پیشنهاد خود را ارائه کردم، پاسخ او بسیار تکان‌دهنده بود. او به من گفت: "آقای فرگوسن، شما قبلاً با من صحبت کرده‌اید و من به شما احترام زیادی می‌گذارم، اما یوونتوس در حال حاضر شرایط سختی را تجربه می‌کند و وظیفه من این است که در اینجا بمانم. یوونتوس در بحران است و من کاپیتان این تیم هستم. آیا انتظار دارید که من آن‌ها را ترک کنم؟"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101552" target="_blank">📅 14:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101551">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d88e870288.mp4?token=gNy8BFAeVYJ2mzIpI4CNXPI17ACg63SajR7oPeoYSG6nsgToIh-7UnbyXRDY2PcHiG27DTVh9Ws2rapsyAaV6FSw9sJOnt5qQ_ODDsCZMd-_Jeq4jTW5lAMKk_tLGNpUjhhgvRv5wH9cpbdLZMa5WfJHWlkdu5wqMV52ckw3oy3XQ_LQmYD-vzqf9J-FSr4KjhJydUYC-3L0cQ6TBBYFcHxX9s47XX_U0bQEpYCYYFNLk4SnwOXN74YVzxvScMolM3J0AB4eOC_HV8NbcrvBcN8WI-hb76qOU7EXkxpFVjibTZq5IVI9MO3b8A0quOBN3L9iwruIII-PFXAUyy0EdjfM622W47czxtBOx061nqUzuh6Y27lXCwv9A9we5Mji0V0bMCKLOfxjgVFFp_UMtV4qsINQS8owMIP3BjRAeDC3VmLJl0rbMPTnCZTLxCslVAslj-G68xo0wpB86ZX2G1G2G-5u2lplFdZIp-UcV9Cpwmple881HSa0PpKboTP5VPGBMq1PpZ5EJjo5LgP7_vcgkZbD2PvRBcEQICJtfhU2Dj6FdvL-qE92n6usYfS9LmUF7IQEAIt_Y6ShTtX1dBoJYJE2N-YN7H7XvJ7oz5_-zH-0odf0nigeq1IxqmzrA1FwVtTdt_VrFrmVzOjYwDjmIsu4YgGGR2JstCdFXpo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d88e870288.mp4?token=gNy8BFAeVYJ2mzIpI4CNXPI17ACg63SajR7oPeoYSG6nsgToIh-7UnbyXRDY2PcHiG27DTVh9Ws2rapsyAaV6FSw9sJOnt5qQ_ODDsCZMd-_Jeq4jTW5lAMKk_tLGNpUjhhgvRv5wH9cpbdLZMa5WfJHWlkdu5wqMV52ckw3oy3XQ_LQmYD-vzqf9J-FSr4KjhJydUYC-3L0cQ6TBBYFcHxX9s47XX_U0bQEpYCYYFNLk4SnwOXN74YVzxvScMolM3J0AB4eOC_HV8NbcrvBcN8WI-hb76qOU7EXkxpFVjibTZq5IVI9MO3b8A0quOBN3L9iwruIII-PFXAUyy0EdjfM622W47czxtBOx061nqUzuh6Y27lXCwv9A9we5Mji0V0bMCKLOfxjgVFFp_UMtV4qsINQS8owMIP3BjRAeDC3VmLJl0rbMPTnCZTLxCslVAslj-G68xo0wpB86ZX2G1G2G-5u2lplFdZIp-UcV9Cpwmple881HSa0PpKboTP5VPGBMq1PpZ5EJjo5LgP7_vcgkZbD2PvRBcEQICJtfhU2Dj6FdvL-qE92n6usYfS9LmUF7IQEAIt_Y6ShTtX1dBoJYJE2N-YN7H7XvJ7oz5_-zH-0odf0nigeq1IxqmzrA1FwVtTdt_VrFrmVzOjYwDjmIsu4YgGGR2JstCdFXpo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
📊
نمره‌دهی به لیونل‌مسی در بازی فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101551" target="_blank">📅 14:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101550">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c3187f185.mp4?token=uwpObV-bCLsju9zZJSFy9gnVbqdYE0A9xzOopmPcgZIlH1quBcF8Xy9EJ76NEcLflHt3xpny1t-gg9bXC6I8qkhW5ZRM7LbBF5CDbTF_ZGtJuDGveBCcTkyX0jzCLbRwTb5Wcz1vX9nNXWliTJn3XbNSCVzC8Wq1Ix6Q2KBoWZDoaNVsa4pDa6GMvEa6YJAaysC1q1QYbfS3e9FhqesDjImDyzT3nY55Qlv02qgCBchMermC7AkjbkqdjrvmpYA8EGR27EJbBtLDCcQo-KT8h_nI7k9coeapVrANWypg7WDacW8p-uSd_otgH5gC2p0ys7iQ43jmeTkyTI8WJoawVzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c3187f185.mp4?token=uwpObV-bCLsju9zZJSFy9gnVbqdYE0A9xzOopmPcgZIlH1quBcF8Xy9EJ76NEcLflHt3xpny1t-gg9bXC6I8qkhW5ZRM7LbBF5CDbTF_ZGtJuDGveBCcTkyX0jzCLbRwTb5Wcz1vX9nNXWliTJn3XbNSCVzC8Wq1Ix6Q2KBoWZDoaNVsa4pDa6GMvEa6YJAaysC1q1QYbfS3e9FhqesDjImDyzT3nY55Qlv02qgCBchMermC7AkjbkqdjrvmpYA8EGR27EJbBtLDCcQo-KT8h_nI7k9coeapVrANWypg7WDacW8p-uSd_otgH5gC2p0ys7iQ43jmeTkyTI8WJoawVzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت‌های مجتبی‌پوربخش علیه میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101550" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101549">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c0345d2fb.mp4?token=gxXljRxfGSubTQB54z-MwfN2EnBwW_ebi9R9ivGpFPXKrga-CioSf-RPbSjioCcbdn13KAKcB3bKtWIwn79_oiPHfXggrYctMUvlfno9MTeBmWYZCcWMfLDXRiVBMn3fCKme3VebUg88zApXe3oEF8XDpbSS5eiXJzkTO1BDEeOYdKOcIOdDPDWGLK96_iLFH6fX4vYVTpiZ0WuYViOqegHZKghlsB10MnvwE1UU_rgc39RmPCLbPhTO5GY6VJVqrfmFMlt8aN8z8TBNX5py8DA41ZLyHa51Iou7d-Ow2n-QCg1n5GbLA5U2bCBh7Sc6oIeDP-E2s-4VcQVk3MOSuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c0345d2fb.mp4?token=gxXljRxfGSubTQB54z-MwfN2EnBwW_ebi9R9ivGpFPXKrga-CioSf-RPbSjioCcbdn13KAKcB3bKtWIwn79_oiPHfXggrYctMUvlfno9MTeBmWYZCcWMfLDXRiVBMn3fCKme3VebUg88zApXe3oEF8XDpbSS5eiXJzkTO1BDEeOYdKOcIOdDPDWGLK96_iLFH6fX4vYVTpiZ0WuYViOqegHZKghlsB10MnvwE1UU_rgc39RmPCLbPhTO5GY6VJVqrfmFMlt8aN8z8TBNX5py8DA41ZLyHa51Iou7d-Ow2n-QCg1n5GbLA5U2bCBh7Sc6oIeDP-E2s-4VcQVk3MOSuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
خاطره بامزه علی دایی از معلم زبان خود و کریم باقری در دوران حضور در بیلفلد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101549" target="_blank">📅 13:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101548">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbd74933b1.mp4?token=tBUpeenojh7YCSvRiBDrtQFuRFHFhDC5f0vB93BXbvfoHpT5voP5h-hp87b6gP4A4zFrK4EhnqDIq1vvn8TppVokQLiB3pqFW6Z5X15N5froFRP-suCIrVLFhm_CJMIsp1Bje4gUq3fuga4tCUltiNXd2AtAoH9Ev5c_sbB7-nitaUQTdpItERsvkWMJB4kmgI0G0MXRWPGvijsEMlsx3O8HOm0RX43VYQNRHyY74u0IRziFvWkNB-Jgvayz0_5ikD1Yge4kv8oNd4rh0VzR77owVV0iJ3i5xBR6cY5ih7tNu_hcC4xjZbK_rT1UtRUxXmoKDz8RJGu8yA1aE6QjCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbd74933b1.mp4?token=tBUpeenojh7YCSvRiBDrtQFuRFHFhDC5f0vB93BXbvfoHpT5voP5h-hp87b6gP4A4zFrK4EhnqDIq1vvn8TppVokQLiB3pqFW6Z5X15N5froFRP-suCIrVLFhm_CJMIsp1Bje4gUq3fuga4tCUltiNXd2AtAoH9Ev5c_sbB7-nitaUQTdpItERsvkWMJB4kmgI0G0MXRWPGvijsEMlsx3O8HOm0RX43VYQNRHyY74u0IRziFvWkNB-Jgvayz0_5ikD1Yge4kv8oNd4rh0VzR77owVV0iJ3i5xBR6cY5ih7tNu_hcC4xjZbK_rT1UtRUxXmoKDz8RJGu8yA1aE6QjCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وضعیت رئال مادرید در این روزها.
🧐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101548" target="_blank">📅 13:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101547">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiMGEyjvmFniWqBwDbP9xFVz3gNrt9OGETcI5SPkQ5_LdAYAxxIxHi0eDo-Uj7F3ROARlt-wXdkFvmwq7pLVST7RLA2H1vBLsTKXjKXYhWqigrdIXdQFagAQsiG5etBFgzMyfwOYyXg0ERXdpmOW_82SGRjzJOrp7es7JlgG7CtPQSHIdZj2m2wiT5lEQVnBiHEO4WbrcjP_ZZlDlLRXSX9GuytrwJPYqA3fM983qvXb6WQp2u59j3MRIU8mYSNjUVXR_IAbcFZei7W531sZ-BXKdUf5wMteKU9VquB7XKgTazxNtf8xBxwMRFc48S6plRuk3lxnvRVnmYjR5AttAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
وینیسیوس و زیدش بعد عمل زیبایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101547" target="_blank">📅 12:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101546">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1e8799b7.mp4?token=XzSO8Vu3N9ThjqnuVBbGiuNPkBVb5LgUXjwIhi4A_91ohz2_wT7qGoKQzytdrW6pKpraFDUCt1BxoRI_UQSZEexe0jY2fes0vls1fAeWj50H1RA4D3bIFutrd4enL9Le8NTR6sAgT0ImPpFs4ZbsWLX-pWekkw-RGxRb7XthiAYH2qpH2qv_0EWew3hQPsnX5DOpGfzEnAN6zrePj_aezFSomdyltloTqhipEe8OzJk_9yj5JpW0hXra2DbrhDeyjN_FjFhb9HfL-mdiJmA3DDPC1aqT6Zll1unVF6mvczqHKLwFAnoxrB0bsJnVgLdKya_vuHh0yyi0luQNCsfFaniNblBAjS4cWI3RreYKwz4yOcsnxnd-tW1fi0dwiwz1VHNvKPiL25LnUlT6p0XmvLXT8LYSjqiDalSecSIZmo7j7WN9-mKW-uQowunr2deAYfFVzXY-lXPoUowRp8FY1tFpKaX793lMdXn3_OE631bwEcUARbswhSrsm9WetTmRL_FbP45H5N4mC671BZbq90bZPfzaMwLQpuIcyBYO5_fca7I61jv6Z1HTucI1PKFIzUHY4DmOOr87s7d0dOwtbgkcRZEoWSgTXL5T7JTuFyh0mrUfQfXZhOmuPPZGBiUYpBA51TOjUMyWZ0Il1JG4aIv2zb_sZE1QfjlDW9B3DNk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1e8799b7.mp4?token=XzSO8Vu3N9ThjqnuVBbGiuNPkBVb5LgUXjwIhi4A_91ohz2_wT7qGoKQzytdrW6pKpraFDUCt1BxoRI_UQSZEexe0jY2fes0vls1fAeWj50H1RA4D3bIFutrd4enL9Le8NTR6sAgT0ImPpFs4ZbsWLX-pWekkw-RGxRb7XthiAYH2qpH2qv_0EWew3hQPsnX5DOpGfzEnAN6zrePj_aezFSomdyltloTqhipEe8OzJk_9yj5JpW0hXra2DbrhDeyjN_FjFhb9HfL-mdiJmA3DDPC1aqT6Zll1unVF6mvczqHKLwFAnoxrB0bsJnVgLdKya_vuHh0yyi0luQNCsfFaniNblBAjS4cWI3RreYKwz4yOcsnxnd-tW1fi0dwiwz1VHNvKPiL25LnUlT6p0XmvLXT8LYSjqiDalSecSIZmo7j7WN9-mKW-uQowunr2deAYfFVzXY-lXPoUowRp8FY1tFpKaX793lMdXn3_OE631bwEcUARbswhSrsm9WetTmRL_FbP45H5N4mC671BZbq90bZPfzaMwLQpuIcyBYO5_fca7I61jv6Z1HTucI1PKFIzUHY4DmOOr87s7d0dOwtbgkcRZEoWSgTXL5T7JTuFyh0mrUfQfXZhOmuPPZGBiUYpBA51TOjUMyWZ0Il1JG4aIv2zb_sZE1QfjlDW9B3DNk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇴
استقبال از ادهم‌مخادمه داور اردنی(داور چهارم) فینال جام‌جهانی در بدو ورود به کشورش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101546" target="_blank">📅 12:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101545">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sttStQe162y2nzz4FnXYAG6b1AOLASD1Q_xRR5ZEhBXPpQnQgKevTpDTbXvyCRJS03XIJYQlK0xU_m_wk-uS7IrAb93uV4r8yv2vptAf8rRbRv4Aa5pVkgSNxhYbLBDWItgGvhA3SN83UA7AL8CeWI-SItRqnwSA1EMNyDZsoI_C0s-PoMly5yt8YrD5Z5uqBTGUgmB3vh8MGIHIm6khARz2O5u2ZvKFb47_ZP7xE6-CNznhlNFfqkFQiK995Ph-csMwS1wrKrRsrHxFXhb-lof9kfNBR9N5YyuY-1lqtRRd8JP1HK5CqxX5PDaeWUr6DidWhXZrXnOeAd_PsX6uXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
۶ تیم قطعی صعود کرده به جام‌جهانی ۲۰۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101545" target="_blank">📅 12:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101544">
<div class="tg-post-header">📌 پیام #19</div>
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

<div class="tg-post" id="msg-101543">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUEyDw94DkAkbBs07CtPcaO2ph6IQ-kxpQqrok2-BqYwG4cIC4huGbYI0066bS9WKO0jvqVaM9BHmZhjuvrIMJzny3Az8EqKrk9R-hSRBA0fTkQzTOduolLswKMzdarDvlSzVyWTluEU5tb6-pBHT2xpwwSEp6XI83VBXTK8NRpG6DmDQ9cP5QZHvUZXchTag_jrsjla8togneJxH7IL5fZeVlLSLRd2jWRIppAs7xzftzTP5j4pvx5fc9SLBpOl-P477e8Eyp1W_9701bjPSvIWbVXDGDSa2X0fXMfIA7RPon8bNwIkpPFV7-TWBoo7HqrUOqCIhcVbYL01Dr0X8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBET
💎
🇪🇺
لیگ قهرمانان اروپا
⏰
شروع بازی ساعت 20:30
🎁
100% هدیه ورزشی ویژه اولین واریز
💰
محاسبه نرخ دلار با قیمت 2.200.000 ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101543" target="_blank">📅 12:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101541">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbcad2324d.mp4?token=G6ClUfF5T2BUSu6ehT7SrrgAlJrMoIW2pnE_jleD2SC7-ExEVIXHSXwT-me6ukPKhMCXjJgmtHAINi0aJPcNaaaVRxTSTPEr0HaL9qEagT3C0DamrPk-uXnUEHH-n4stX6BDYkPNhpFC64bv3XQC3dwJ4fd2iPFzT2kEQg_GF42yDa3eN_cky6An2l8IEmyckP-rwdagAPd7det99_Fs8Uuk3sW12xm5s1NuJZpuHgFD091U3NNRgWptSsLKL4qhvaV62XtqHByOMibPTi9hdM26QgPAchTrQr5wXGI5I155qG9-S6tow1SLzOiWIH3dckwkrFxkG1sjylY4egiOyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbcad2324d.mp4?token=G6ClUfF5T2BUSu6ehT7SrrgAlJrMoIW2pnE_jleD2SC7-ExEVIXHSXwT-me6ukPKhMCXjJgmtHAINi0aJPcNaaaVRxTSTPEr0HaL9qEagT3C0DamrPk-uXnUEHH-n4stX6BDYkPNhpFC64bv3XQC3dwJ4fd2iPFzT2kEQg_GF42yDa3eN_cky6An2l8IEmyckP-rwdagAPd7det99_Fs8Uuk3sW12xm5s1NuJZpuHgFD091U3NNRgWptSsLKL4qhvaV62XtqHByOMibPTi9hdM26QgPAchTrQr5wXGI5I155qG9-S6tow1SLzOiWIH3dckwkrFxkG1sjylY4egiOyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بازی‌های افتتاحیه جام‌جهانی ۲۰۳۰ به میزبانی سه کشور آرژانتین، اروگوئه و پاراگوئه برگزار میشه و سایر بازی‌ها در مراکش، اسپانیا و پرتغال خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101541" target="_blank">📅 12:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101540">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cde737c1a.mp4?token=lgZO2BCeXyZJix1sCpMmqsn1zn3vQHjyxhU59MnoF_SMj6GjfHFT9--8hz9xFoZiCBGtEOphwG2ljwOLRWA4O9wmsvDiFvnN8_2_Z0bkZya2eRs4qomPFMh8lYk8bi1e4MdBTc_ucFj_H8Sqf0Ys1LoK1h4MZdsXgm2OoSuWxvz6iSFUZnYLe0HiHRGi0nfqz75R21aQu4HU-76509NxSv9QXLfDrF6QSrHcUC4pU_cqM50G30FWv8USMTXeJ5OmGa2xmL4P125_Qpsvnu7O4BughESWKJDOai0N_pBWnKInbllewzLmczCQ6FGR6aK_-QkC5YlGYeNzt8gn7pchag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cde737c1a.mp4?token=lgZO2BCeXyZJix1sCpMmqsn1zn3vQHjyxhU59MnoF_SMj6GjfHFT9--8hz9xFoZiCBGtEOphwG2ljwOLRWA4O9wmsvDiFvnN8_2_Z0bkZya2eRs4qomPFMh8lYk8bi1e4MdBTc_ucFj_H8Sqf0Ys1LoK1h4MZdsXgm2OoSuWxvz6iSFUZnYLe0HiHRGi0nfqz75R21aQu4HU-76509NxSv9QXLfDrF6QSrHcUC4pU_cqM50G30FWv8USMTXeJ5OmGa2xmL4P125_Qpsvnu7O4BughESWKJDOai0N_pBWnKInbllewzLmczCQ6FGR6aK_-QkC5YlGYeNzt8gn7pchag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
علیرضا جهانبخش: به فردوسی‌پور قول دادم که لباس محمدصلاح رو براش بگیرم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101540" target="_blank">📅 11:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101539">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRAtGgbaVLtZ12uFj7l894AQqpZR715Y4ij2RPqjKRO8yDQo6VsrEvD3vQcjKhu0MvRVUiyAKoZ-XgPeWUV67Fs17qs1xe-7XWEBLRqe6b95ozfsVQKwM8RSlh5w6aOjDUWHmdaXfDLOde6yIxiPKP3pml9BK6UEXjT2yyvK3_6dwRXMQVjrP_TSp49EpAl9c01D4FRlDcX_J87hevNDhIuvAeJaEHJL0aeuE77j9GobfnW1u3g3NyRKjsK0_nESDgzOmyEjuM6sqbaPcPVaFuw75GDQfuS7OgCYzSDV-3wC962ak5OCmLh4O8NbV8syhVUfYJH6Wt7LUzayqOA5cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم منچستریونایتد در فصل‌آینده مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101539" target="_blank">📅 11:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101538">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLns4cg7P1kiXu_hgQmQ_dwVK_k7531fhlgnY1luuP-d8WXAKpZJgyNenqyCDUjnQpxeVFJM19gvogJfMlzLnMqq9jXk4cy4UdLaihQBI3S8AzpKRo-v5k5ETHxJl1OVVhlVXBVEOHxM7T_oTjmLqCKq3VcvkAS5xrthQL0SkYHF7P0i7iRa9Lzd8LsSnJndJb8SFcPgAXx5OTlWbkwU6fjPVMs2ZYJ5-ud9-htVo46c7H7lTyl_s8cBlrPs1TvqjrCrx-78ZbjYPYruq3QES9eHtLhU-bSjT-96J7fQ_cu27uh3qjnCVmvkUJowu2oTw5iKPnW4Krj-C09zvr3fVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حمایت یحیی گل‌محمدی از عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101538" target="_blank">📅 11:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101536">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/330d45af26.mp4?token=KQH4KgbJuIzF5-4_FODJ5PWcTsItwejKboFeQenvYC6L-6OFCbn8eWvgm2hHi2m1op1DrxBkA_3XJ9skd1jcdMVVBsEMCN3osWzMgJp6TVnN2AczOT-QOMNF2t2iSvrVZ8hI1d_ScrpLSBL6UzpWT_TpIZBebieU_AXicDkJjKGckUKhGNFRRFOdDQ3N3H2Kd2_uZp5aYep7LmAPlCjxyXW3d0YlGqXhUog5o_lfoFefh8FDOO_1od5QemXFdBy3n5gadhbYk48XpYJSF5R70vQrTitNzLa0WLm8PHPWGFVGUfogecX0qPLlWt1g6pzoNPdRj41YKjRmxdltFfWL4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/330d45af26.mp4?token=KQH4KgbJuIzF5-4_FODJ5PWcTsItwejKboFeQenvYC6L-6OFCbn8eWvgm2hHi2m1op1DrxBkA_3XJ9skd1jcdMVVBsEMCN3osWzMgJp6TVnN2AczOT-QOMNF2t2iSvrVZ8hI1d_ScrpLSBL6UzpWT_TpIZBebieU_AXicDkJjKGckUKhGNFRRFOdDQ3N3H2Kd2_uZp5aYep7LmAPlCjxyXW3d0YlGqXhUog5o_lfoFefh8FDOO_1od5QemXFdBy3n5gadhbYk48XpYJSF5R70vQrTitNzLa0WLm8PHPWGFVGUfogecX0qPLlWt1g6pzoNPdRj41YKjRmxdltFfWL4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تمامی قهرمانان جام‌جهانی در یک ویدیو جالب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101536" target="_blank">📅 11:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101535">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41b3828f7c.mp4?token=e-_63VUpbCRtk3Ld3sCE9Tr6jcr4iinm7XqJ9DYFfr7gAmvnRHxSi8YQcUZqF1H9Voa_S7dtjd45bTvHxG-BB-PxCmleDuI9HOuLtNwD-EajRtyxYoW5L4tUwBWx3hu8IfntvSpWECjTEqd6CXbg6t5IdbedeRb244hZgRyopdtwdaqKUUv3ouQ0gWtjRTbXR1r3bPIagibtC89hcfQmbkdJAMiypFwOQGYNFNpIL94nFeon-OYzAR_uMuzGlH3yPZGVJ3n-shXhXvN3ahsvbQnoNghhCiMh1j2j7dteST8TN_wCWZBHU3QLmKpbGwAd_xO2Eb4HCVtgpDhahTN-GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41b3828f7c.mp4?token=e-_63VUpbCRtk3Ld3sCE9Tr6jcr4iinm7XqJ9DYFfr7gAmvnRHxSi8YQcUZqF1H9Voa_S7dtjd45bTvHxG-BB-PxCmleDuI9HOuLtNwD-EajRtyxYoW5L4tUwBWx3hu8IfntvSpWECjTEqd6CXbg6t5IdbedeRb244hZgRyopdtwdaqKUUv3ouQ0gWtjRTbXR1r3bPIagibtC89hcfQmbkdJAMiypFwOQGYNFNpIL94nFeon-OYzAR_uMuzGlH3yPZGVJ3n-shXhXvN3ahsvbQnoNghhCiMh1j2j7dteST8TN_wCWZBHU3QLmKpbGwAd_xO2Eb4HCVtgpDhahTN-GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی پول نظرتو عوض می‌کنه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101535" target="_blank">📅 10:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101533">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/191f51b3e1.mp4?token=ULecOzpAZq_FVYQhsje5i3wfHCKYlsBspEmPnRyv5LGLnuS0Ka1i6PFTlWDn81eJVmTSvQKGdFfHKmHFg_0X-2NgkbeYqFD1d9qGM__98FjXAvPFxP3yE3PmJDNsiRuUjOPDSXTGLlLxPxsBch6E2SesXZVLqtFZWNqmUKvTI__lYe_bx3PMsO96qcuGlcim-_x5OAePYHRlOKLkMvZ2ycFJMOj4iqFE57ePYRbUTF6jUIuukP5lD-BpUjkud_E68HU3ToNqBWxs5pVRJ4ch0EN9H4CYS1_AQkXlfjxkrkd8_CMHSuvmI39KR0sceFTExqCixU3AZzzNED2fYb9xQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/191f51b3e1.mp4?token=ULecOzpAZq_FVYQhsje5i3wfHCKYlsBspEmPnRyv5LGLnuS0Ka1i6PFTlWDn81eJVmTSvQKGdFfHKmHFg_0X-2NgkbeYqFD1d9qGM__98FjXAvPFxP3yE3PmJDNsiRuUjOPDSXTGLlLxPxsBch6E2SesXZVLqtFZWNqmUKvTI__lYe_bx3PMsO96qcuGlcim-_x5OAePYHRlOKLkMvZ2ycFJMOj4iqFE57ePYRbUTF6jUIuukP5lD-BpUjkud_E68HU3ToNqBWxs5pVRJ4ch0EN9H4CYS1_AQkXlfjxkrkd8_CMHSuvmI39KR0sceFTExqCixU3AZzzNED2fYb9xQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
یه سری ویدیو قدیمی از قبل آشنایی یامال با اینس گارسیا دوست دختر فعلیش داره پخش میشه که توش اینس وقتی یامال با نیکی نیکول بود تو لایو گفته:
‼️
🔻
اگه یامال یه میلیونر یا یک فوتبالیست نبود، نیکی نیکول حتی دو بار به اون نگاه نمیکرد!
﻿
‼️
🔻
همچنین ازش پرسیدن: «لمینه یامال یا امباپه؟»... گفت: «بلینگهام»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/101533" target="_blank">📅 10:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101532">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">😂
😂
😂
تفریحات جدید اسپید بعد جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101532" target="_blank">📅 10:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101531">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d084b6a5a.mp4?token=mPllSvLFNcQHpxDFbF_OO7ntxjssHUdVbrIWKJ1JYv8yizn6lz0E4f5D4o0kZOm6XQJBWPrKS3mHw0OpVP4KdwYdYmLP5dKaZ8FgasQhtYr79FJ7EYTDHdJcPXcnAzmGWSKT_MbFYECt7MTxBfihvvXZNWxlmP3xu0QW4WL-bkbqPR5CeVnMjNaNqWex5ahZ6_I-wWxfX6p9Ur6CRjzKKS11FtkY3eKzzcQQ1S2K9Ank6T8OXHDY2oz92f1LvrjzPCKRD0lRhs-_knktZhRMsHDRcML70wF9HCh2bNiOkEY8f2SV54ZtQAF0nRSncOV8CzeeQRPntYKyTvQm7xnAwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d084b6a5a.mp4?token=mPllSvLFNcQHpxDFbF_OO7ntxjssHUdVbrIWKJ1JYv8yizn6lz0E4f5D4o0kZOm6XQJBWPrKS3mHw0OpVP4KdwYdYmLP5dKaZ8FgasQhtYr79FJ7EYTDHdJcPXcnAzmGWSKT_MbFYECt7MTxBfihvvXZNWxlmP3xu0QW4WL-bkbqPR5CeVnMjNaNqWex5ahZ6_I-wWxfX6p9Ur6CRjzKKS11FtkY3eKzzcQQ1S2K9Ank6T8OXHDY2oz92f1LvrjzPCKRD0lRhs-_knktZhRMsHDRcML70wF9HCh2bNiOkEY8f2SV54ZtQAF0nRSncOV8CzeeQRPntYKyTvQm7xnAwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یادی‌کنیم از سوال خبرنگار صداوسیما از لیونل‌مسی که بنده‌خدا اصلا ایران رو‌ نمیشناخت :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/101531" target="_blank">📅 10:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101530">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZV1-VykbB0P9O88efbENcDY_Q91J4SXbV6J-HSmMu9LgMewv1kJOaoh0zmt10dtjiUPZ2Gf9xv3yEZaTS0dEThhc50f96-FQPPBzTCnVZhZK6fDtcAkxwriz83_jkHyf9IHCrdCuqQwunuFpGJAH6u0MdVmF3VL4GuOa59PLEH-Vb5dXQqjXCweydNLJVCQixuwloT7OmDdeVPPMqqKaJDIvaEiw3qtkvAC4Zqlrw0Zb5LxpQyfQ8LUs8wyKHXvapcScJZpHDt7ZrX6JWK4B-o6kD_wejOxCFebVahgUvdeQuYe2WcGqVXTtWWZpDEQ_NYAOfs-fKqB01yPhAD-Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📅
🏆
شش سال پیش، در همچین روزی لیورپول برای اولین بار پس از 30 سال قهرمان لیگ برتر انگلیس شد.
🎙
یورگن کلوپ: "این دستاورد بسیار فراتر از آن چیزی است که من تصور می‌کردم باشد."
🎙
جوردن هندرسون: "من بسیار خوشحالم که این عنوان را برای استیون (جرارد) به دست آوردم."
🎙
اندی رابرتسون: "ما 13 هفته منتظر ماندیم، اما هواداران ما 30 سال صبر کردند. این مدت کوتاهی در مقایسه با زمانی است که آن‌ها تحمل کردند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/101530" target="_blank">📅 09:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101529">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZB2t6pXg_cjgS0bSUVS4UHvM0qzuuSy2YS0_Gu5ij8gw-MqUzL8OkvMqCJhu2ID2dJflIhS7vn2bmXbEIt2S1OWQ0vPsiPgHTZtTfPibT5pFlaF1mvLZJtj9uOczyC0pIJnh8Z6W2c6PE6dfGlbMsWBgvFbMp-rGshu3i6-RzGqsESIR9uKXVb08PEcFVq7-YdgvmuMKCtVRCgibrGCDfuU7f48g4ug_EtcscXLis4RkyY-9tvmHbjkZUICFzdwtWkFYOA2INiVOYLjpt12d08upWk8LDYJHTe9oFlI41l3Kfc2qAI5R44sR8uKljQMohNQzgzKYjUPZv22bAsjSXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو
🚨
🚨
🚨
🇧🇪
🔻
مارک فان بومل به عنوان سرمربی تیم ملی بلژیک انتخاب شد.
𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101529" target="_blank">📅 09:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101528">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8781c60fd.mp4?token=rIgP0mbj_gheNDVaQV9UwMzU9P5zSHCjNDRN6_xPiOGuCLUF8QO6Yay8zbKus2H9D5FxGBM-2g82oj5vEi6sVSssIlzH3nuEA5_y6VLTStFz1bO11vXts9yYI9ZK8uB676i5Y7YczcgoErYC6xJU4BdTsx8E3rVrhia56STSbcfQeIaPVItb5Z7gzazKuGDtkWPDMq7Uhherkxuz1YI77EzP6vJyXoc0_E1i_d6E3xPkD2lMVncCC5DCqMC_R3-OeAjPdEqUH8TZLA6B0ViqAqKkxS5cG8556aLheuIfCztTXExOe0n05bsy3I_gZg-oVF1s88A1zrWOwL3v5_HwKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8781c60fd.mp4?token=rIgP0mbj_gheNDVaQV9UwMzU9P5zSHCjNDRN6_xPiOGuCLUF8QO6Yay8zbKus2H9D5FxGBM-2g82oj5vEi6sVSssIlzH3nuEA5_y6VLTStFz1bO11vXts9yYI9ZK8uB676i5Y7YczcgoErYC6xJU4BdTsx8E3rVrhia56STSbcfQeIaPVItb5Z7gzazKuGDtkWPDMq7Uhherkxuz1YI77EzP6vJyXoc0_E1i_d6E3xPkD2lMVncCC5DCqMC_R3-OeAjPdEqUH8TZLA6B0ViqAqKkxS5cG8556aLheuIfCztTXExOe0n05bsy3I_gZg-oVF1s88A1zrWOwL3v5_HwKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
فینال‌باز واقعی آرژانتین در کنار لیونل‌مسی فقط یکی بود اونم دیماریا که واقعا نبودش امسال حس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101528" target="_blank">📅 09:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101527">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d9304f085.mp4?token=iPtMxzUS-ZpvuQFi8ZEZqimvJlO17f4_CKNNWOYBcFdko2M1RG1tN4ZWeHBUNgrwyNsBFudtwTO_W6ZbxSbp1kUndhMSVry8t2sU0xgNCbUH-qhjgJfEdzdUJ7NvI9qvEhHt8QqnYQCuZO4EnJDRTSzpRcEp_D2mYlFQMLyx2OgC1EPVe04HKAXGopPO9QzswPev750szadr_7bW62xcFSTme2VOrFK-vMCCvgE0B9129-WXpzBNt0FWjWpjp2AsvJhBToi7HrpPZDDCPh6QN0Xp5KtdAsu6qqHKs0k1jGL3X5d9Kve32EhMJdeP6jLbR9mKXsxvmSBOiMmDDZ45nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d9304f085.mp4?token=iPtMxzUS-ZpvuQFi8ZEZqimvJlO17f4_CKNNWOYBcFdko2M1RG1tN4ZWeHBUNgrwyNsBFudtwTO_W6ZbxSbp1kUndhMSVry8t2sU0xgNCbUH-qhjgJfEdzdUJ7NvI9qvEhHt8QqnYQCuZO4EnJDRTSzpRcEp_D2mYlFQMLyx2OgC1EPVe04HKAXGopPO9QzswPev750szadr_7bW62xcFSTme2VOrFK-vMCCvgE0B9129-WXpzBNt0FWjWpjp2AsvJhBToi7HrpPZDDCPh6QN0Xp5KtdAsu6qqHKs0k1jGL3X5d9Kve32EhMJdeP6jLbR9mKXsxvmSBOiMmDDZ45nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😔
پیام استاد وحید قلیچ به دونالد ترامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/101527" target="_blank">📅 09:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101526">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXhqpgFUR36F4bIDA6r-VZR2__WmLQf12qszHXLSEisjMTim3y8eAPhcdOpCOvp-WXpGoRdBqJOlmLp_rh_xh9IKeLicGdKkNcecB4Fk3NxRbeInFijD2Is1fwFgF4bpM0upSsbTvITpvmS7vbz2T5peWbJPtTd8BauWwS-hWHFqfH-bVgVrhdLD0ySJ63Z6XD44IIJ8g4jXxt1wlPEx82pyHDUOh6aX8k_uO1vVICZovvFJG9SDKWbaa40BZXU0MjEnwoW_i2fgsf1bB_lDI_BWU96X8Yl59HQr9-a4kl_uk-BRTrU1-_ULaGoHobG6E_2oj5TqJEW08bVgPxBfrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
مارک کلینمن:
🔻
جف بزوس، بنیانگذار آمازون و چهارمین فرد ثروتمند جهان، برای پیوستن به ائتلافی به رهبری آمیت بهاتیا دعوت شده است؛ این ائتلاف در حال مذاکره برای خرید بخشی از باشگاه لیورپول است.
💣
💣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101526" target="_blank">📅 09:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101525">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab5d3c4f61.mp4?token=vANdbn2THZNGeyxx5YhsVXrwj_Z3nUsk98bWQfINyVNal0-JgPYKfbVJdJsWtmi7D9NvsvDsH-OMBQsL-SuyZmWo_feGIuq8-_G65gCfN-U2mgzOsBjJ_CRfTdDuqGPKZiO6YTQcZMi5zRnsiam7PzS9L6dRc8J4K7BGVTyQAPdV6RtxZU0O_MTTIKmY4HUAjfMvyCEnkcPUMlaEt6-gRKO82gAwdWlmEGqQJQDkYM-uHv7IkZPvY04x-esRMOu-Y2ylc0teuLgBIxhq9c1_HbZ-EzsUqzsTOIchrFOJlUBMot-wTbA6aM5DPEVNPRKKZBXrorJb-8kVaQcFIJJhVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab5d3c4f61.mp4?token=vANdbn2THZNGeyxx5YhsVXrwj_Z3nUsk98bWQfINyVNal0-JgPYKfbVJdJsWtmi7D9NvsvDsH-OMBQsL-SuyZmWo_feGIuq8-_G65gCfN-U2mgzOsBjJ_CRfTdDuqGPKZiO6YTQcZMi5zRnsiam7PzS9L6dRc8J4K7BGVTyQAPdV6RtxZU0O_MTTIKmY4HUAjfMvyCEnkcPUMlaEt6-gRKO82gAwdWlmEGqQJQDkYM-uHv7IkZPvY04x-esRMOu-Y2ylc0teuLgBIxhq9c1_HbZ-EzsUqzsTOIchrFOJlUBMot-wTbA6aM5DPEVNPRKKZBXrorJb-8kVaQcFIJJhVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
روایت امیر قلعه‌نویی از دیدار با یک آیت‌الله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101525" target="_blank">📅 09:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101524">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfGuHwcTzEZaeMBJ4kQGbxnD0XbkT9KGUUiFrt0B8ix0cvXjXvfJ1bCLgN4NcvRqAT6axqGlXj9SQnpWnSp6cpZy639aJVc85GbTf6W5CxNPsdiMV8UlyOEYKLrhSiGwqvOlPOGVzaKjcO63IZ148t7UEJ2D5FSekX6-VByZq6OLqw-b21MX5CqVvEqp4E96NPnlwo4l3dC63OIEwSkFZGzdKjf0kvsJBrSBlqjjw_6isaQFquZV6Nvphk5CrRDm2a1DHCSahO7cy5UG_-ByoBI3-LcGORKILUecg7TJaWQY-zQA2XAPuwPXSujkbvJiL5yh_e-OBLHW2afF6FQORQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر شاهکاری یه کپی بی ارزش هم داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101524" target="_blank">📅 08:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101523">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xs88gfD9LM4rcImh7Tl9Tt_gjIaicY_fMn0T1hDLIy6c3yWqrqMvRep_InQX_-1xCEkNJYnUyiIo-DRVpNanEw6_6WK3Fun3MxUbc_q9TA9vw_vTaUzc0P7CF5-HbwFkNbVVCIxqrOHSB02XSiEWcfO_5KzC8j5ObTREzPnlTt1_J7fEUm7YMGnQnxOTsCWgKoNfU4FIfgQb82rgSA-DrlbjRVHMs9xmubFPVtgbJGm-eOF3tAXEZKy69TZJ7zOxaYdVh8rYuQZLZH8jPV16BYFTYtUF8mzvqpXCDn1-5m1MFKcdeTdO2bEvCasEnAri1c9UiufAM9pq6sW4wt3ixA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
👏
دیگه قرار نیست بعد دیدنش بفهمیم که 4 سال از زندگی گذشته و اوچوای دوست داشتنی بالاخره از فوتبال خداحافظی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/101523" target="_blank">📅 08:40 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
