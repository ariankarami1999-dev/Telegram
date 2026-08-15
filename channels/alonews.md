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
<img src="https://cdn4.telesco.pe/file/KpebWi3jpUVCimGycKlS_HxOxJKDa8hBP1YHkL9Jfol61RhAAff9XI3AQ1RgSg4_ctR2S--424UtHzSjKOalZxVdKMCmWro5iDkjlG4ScG-MumznVo99Dl1mJZcDp47GS5Dp-5PvKkOGNmzR_84vqAUPxN7hG7GtJZdCNZ0wc8YW5gPkM9KFxl4E0H9Eou0nixA-eBu9bmKBdZDIw-h_4rPCbDNiqKoRJkqOH3Z08nLw8PhIc3YNawXnE6ia3Xz44Sq9MbpHh_fiZNBSnMmgHy5CIqbl-dN4kq9S7fMZFlvTKyEGnfuFz0Rg2BZe_Cm8TGOEWGT4JAfKgXqBW_ukxQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 964K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 14:15:05</div>
<hr>

<div class="tg-post" id="msg-141814">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e91310e606.mp4?token=isjOnfPGxCCG2fOZ8it095cOAArK0Z_GTN-chH2RmtbQJeCbv6_myeBHE9iJnWv1biIbBlZsljoxfPGaZa3o3XJdegfEmmO3PELSUuFMIKsk8d6Myzn_j3Z70RHHISMMIujLvBw7Aqaaom7QrkKQA1rG7hz8fnl7defFHTykbQcZILT4nYGx3ZxG5dkrXaa4UYqC2x3VmITiGBv57lAU8Tbv6h3BsSKu_e5TpCCRpCMm2owNFZcZVIixLFMfisq2dDVfwc7nLYn6sIzVh5NGbehoVhbX6Ft4eb30Dc0kZLo3VpbfBiC45wkG5C51VVmMX-t29CsltGK9E9XxfP9EY4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e91310e606.mp4?token=isjOnfPGxCCG2fOZ8it095cOAArK0Z_GTN-chH2RmtbQJeCbv6_myeBHE9iJnWv1biIbBlZsljoxfPGaZa3o3XJdegfEmmO3PELSUuFMIKsk8d6Myzn_j3Z70RHHISMMIujLvBw7Aqaaom7QrkKQA1rG7hz8fnl7defFHTykbQcZILT4nYGx3ZxG5dkrXaa4UYqC2x3VmITiGBv57lAU8Tbv6h3BsSKu_e5TpCCRpCMm2owNFZcZVIixLFMfisq2dDVfwc7nLYn6sIzVh5NGbehoVhbX6Ft4eb30Dc0kZLo3VpbfBiC45wkG5C51VVmMX-t29CsltGK9E9XxfP9EY4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اعتراف میکنن که به مردم معترض شلیک کردن.
🔴
چطور تا دیروز میگفتید تروریست ها حمله کردن که؟!
🤔
حرام زاده بودن از صاف بارز طرفداران رژیم هستش.
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/alonews/141814" target="_blank">📅 14:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141813">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
فوری / حمله گسترده جنگنده های سعودی به مواضع حوثی ها در یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/141813" target="_blank">📅 13:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141812">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
یگان مبارزه با تروریسم عراق از دستگیری یک تروریست تکفیری طی عملیات امنیتی در استان الانبار در غرب این کشور(در نزدیکی مرزهای سوریه) خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/141812" target="_blank">📅 13:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141811">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb8e792f1.mp4?token=eVHtdQD-wn5trlBGvyhg_hmpMaW3kH8D0N_drQc0hDG0F3D4n3ccaqvTwhVSAv2-hPbQ5UTJPkF-xQBb3uKfKJu5XH80oAoEd8AdOD8JoplTUECwZhgVOXXy5tuSZHDHbhzf03vyYwdZQZ41OQI6RHPS3DFwRZAdAuU1WCXNj2qsueIX2AZgk3JhEN_UFDEqJ8ZqzVg4XyF-IzJ1VBuMY99bIUYP8n5oDtnQEYt7WUuYTQLihLLvL0rfZK0_WO6POwpzGhP-UMQ-t3r5XVslcm-4e5IS151zNg_8vvOGeQZiL7RmvNTJ38-muHplm4yQvIF6DyQaD0zYtGz4ie2TRYqeOYHO9bupBKjefMoVlqy8I8KPneYGN1q-3W_-2KWAKBM0z2IcpUNLznT8FIipduceAf_9z_gMfp11cIfgH0p9oPUBQO7IqI7_ju4PBSOrH1d8wciT53VFvZaUHOl47gg3WXRz-irlEDo8xicePUYsCwVpWL81bKe_WAmaTsOgCwHVRHxjZP8Gk7qtV99Kd3R--ngu96YazGXGrETKihnBI33G-_EyWfZMoE1E-o791G2logaQT6aPcBXiEOg8t2TD52NA1MqHxBkxCLgrm5ik3V59Y3juffIhM4yg2eeeF1Etf3NTUDlsTleozDHh7RdZKAovs3nhBh6l-_JkoKo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb8e792f1.mp4?token=eVHtdQD-wn5trlBGvyhg_hmpMaW3kH8D0N_drQc0hDG0F3D4n3ccaqvTwhVSAv2-hPbQ5UTJPkF-xQBb3uKfKJu5XH80oAoEd8AdOD8JoplTUECwZhgVOXXy5tuSZHDHbhzf03vyYwdZQZ41OQI6RHPS3DFwRZAdAuU1WCXNj2qsueIX2AZgk3JhEN_UFDEqJ8ZqzVg4XyF-IzJ1VBuMY99bIUYP8n5oDtnQEYt7WUuYTQLihLLvL0rfZK0_WO6POwpzGhP-UMQ-t3r5XVslcm-4e5IS151zNg_8vvOGeQZiL7RmvNTJ38-muHplm4yQvIF6DyQaD0zYtGz4ie2TRYqeOYHO9bupBKjefMoVlqy8I8KPneYGN1q-3W_-2KWAKBM0z2IcpUNLznT8FIipduceAf_9z_gMfp11cIfgH0p9oPUBQO7IqI7_ju4PBSOrH1d8wciT53VFvZaUHOl47gg3WXRz-irlEDo8xicePUYsCwVpWL81bKe_WAmaTsOgCwHVRHxjZP8Gk7qtV99Kd3R--ngu96YazGXGrETKihnBI33G-_EyWfZMoE1E-o791G2logaQT6aPcBXiEOg8t2TD52NA1MqHxBkxCLgrm5ik3V59Y3juffIhM4yg2eeeF1Etf3NTUDlsTleozDHh7RdZKAovs3nhBh6l-_JkoKo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش
‌سوزی گسترده در اسپانیا به نزدیکی خانه‌ها رسید
🔴
آتش سوزی گسترده در اسپانیا به‌سرعت در حال گسترش است و شعله‌های آن به مناطق مسکونی نزدیک شده است.
🔴
نیروهای آتش‌نشانی با بسیج گسترده تجهیزات و نیروها تلاش می‌کنند از پیشروی آتش و رسیدن آن به خانه‌ها جلوگیری کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/141811" target="_blank">📅 13:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141807">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izoLff5csVzcPUvNYIKKdyKLxYaKdSiUt6rCwp6ERaXIfu7hzormNbAfWYcId7u35LVoiGdtdsQHrzsHTNEo8DV667k5Y0ooznQ9fQ5u8bB-C_nxeIVmk5Tx0rx6H67aBIzDkUTGtEl-kfcdtaxumIJvqN8q3TtL3FVlAg8MRHrxiBC5riVV_gi4wF4g_iVrjcM2G3wIguEadzr8idaDryV0qadACRZGKagOd2j6fjCvzNST5XAhc3CPgkDVb0pkfxyd1U3Rmv5jl36YwGO3w21DyJvU4edzhmM2AoKd-FFSdVgF2rBXCGQkzX_HFrYAVHYxjcoCqMW1tM6TitG02A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/596d386743.mp4?token=ZN9T2gmxkA3okN1kwv0ANLCaEdpfSde06iZvOVUqhpqkUmthI7TzKN-X_CHlZECryk9J6tAH2fu3wDehoF9M0wrdiq276YAr6xLIaZzwFCGhPWgD4kehjCaIxDRw9MxmZ46ome_ddJieAiH8rIncGmmfJeaL1IdpTqH_GUKMTmFMpnBPz2hVecfnZ-EObn0naCKPmusJ4igh2z0gG0pEG5bbFLBV5uc4Wny9Y2FolcBGX0StfvFRUZcCrWiqTod8g5S1wpfoyUosLfO328ntvC9rNwnxPDCHmkr-LIHNcMCRbki07pie9zXOMp1FVUAUrQBJcyseVh7Vom2qoUWYag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/596d386743.mp4?token=ZN9T2gmxkA3okN1kwv0ANLCaEdpfSde06iZvOVUqhpqkUmthI7TzKN-X_CHlZECryk9J6tAH2fu3wDehoF9M0wrdiq276YAr6xLIaZzwFCGhPWgD4kehjCaIxDRw9MxmZ46ome_ddJieAiH8rIncGmmfJeaL1IdpTqH_GUKMTmFMpnBPz2hVecfnZ-EObn0naCKPmusJ4igh2z0gG0pEG5bbFLBV5uc4Wny9Y2FolcBGX0StfvFRUZcCrWiqTod8g5S1wpfoyUosLfO328ntvC9rNwnxPDCHmkr-LIHNcMCRbki07pie9zXOMp1FVUAUrQBJcyseVh7Vom2qoUWYag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت عجیب جنوب لبنان در پی حملات امروز اسراییل
🔴
لبنانیا دارن از جنوب لبنان به سمت شمال فرار میکنند
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/141807" target="_blank">📅 13:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141806">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/368619c5a2.mp4?token=RYdcVv1s41JOe6sIMc8bui8RDUQz17x14ZklGTkG8meZVPEQGRNWFg3LcgslC54mAanWuxheXNB8lzMam7mry1MBsV1JOxYN-OgdgIiuY9E0S9OozCeATZFd08OrcQIYPOZSL_j5f9N-Tnb2VPbu3J3X9t2pIqDYncf-pTdcfWQLx3TwUeROJtXDWO54w092bG-UHoJRYvtmBEh7vJNkd0rxCVlUU5iEi39JHpFzLKSQg4fqABue1KB_2mx_vLtSMYI_qsVp2IDZsApRymnQ6HckDbfTWPUL2o9utUgafP5HdfFXI0ZBbvuOJpwj3O9mZt5pd8pM4luXu642GVYLkYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/368619c5a2.mp4?token=RYdcVv1s41JOe6sIMc8bui8RDUQz17x14ZklGTkG8meZVPEQGRNWFg3LcgslC54mAanWuxheXNB8lzMam7mry1MBsV1JOxYN-OgdgIiuY9E0S9OozCeATZFd08OrcQIYPOZSL_j5f9N-Tnb2VPbu3J3X9t2pIqDYncf-pTdcfWQLx3TwUeROJtXDWO54w092bG-UHoJRYvtmBEh7vJNkd0rxCVlUU5iEi39JHpFzLKSQg4fqABue1KB_2mx_vLtSMYI_qsVp2IDZsApRymnQ6HckDbfTWPUL2o9utUgafP5HdfFXI0ZBbvuOJpwj3O9mZt5pd8pM4luXu642GVYLkYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اعتراف عجیب مجری صدا و سیمای جمهوری اسلامی: حتی به ما هم دسترسی به آرشیو های پهلوی رو نمیدن
🤔
خاندان ایران ساز پهلوی
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/141806" target="_blank">📅 13:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141805">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/titEr8fwJjRnVzRSg1_wGUqWZRU-P-i3M6RxBQu_D-pkoej_lf1G4Suxhkp-uIzbZYf4I5xtYRDSiG130yIZ1vpDgdUY2Kq_D7Sf9nNkD2vmJRai421naznF_kuBydFILP6v8c6GPjNPOtzgsDkW2I3J3a0hAZWjMcb1OdZ1-Hj1P1k118JLbKS-HvdowpBDtRI7aFkeW6_0OLCosz5OM17L-D1mxZPvmA3su85XZnMWyuCjiaX0tfKafzYiI02lABm1DOqEgOSp0TZ4XqmYejtflzcENxJhuypXWHtLl78-V_ipVy1TaNN_4Z4RO_SR7YerhC5-n3eSZPiwZKj6zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تریتا پارسی: به نظر می‌رسد احتمال آغاز دور سوم این جنگ احمقانه بیش از پیش افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/141805" target="_blank">📅 13:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141804">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
طالبان خواهان از سر گیری رابطه با آمریکا است ، وزیر خارجه طالبان گفته است که دیگر دوران جنگ تمام شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/141804" target="_blank">📅 13:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141803">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
تحلیل الجزیره: آمریکا نتوانسته کنترل خود بر تنگه هرمز را تحمیل کند
🔴
بازگشت این کشور به تهدید‌های اقتصادی علیه تهران، نشان دهنده شکست گزینه نظامی است
🔴
ایران همچنان چندین اهرم در اختیار دارد که تنگه هرمز تنها یکی از آن‌ها است
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/141803" target="_blank">📅 13:33 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141802">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
اژه‌ای، رییس قوه‌قضاییه :اراجیف ترامپ درباره تنگه هرمز ناشی از توهمات این فرد سبک‌مغزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/141802" target="_blank">📅 13:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141801">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e629cfdde.mp4?token=vkUlGYM8U1smh_5g-aFKg0lgrTAOARrjNmA3PULBcTzzQ83amWV74aWXhvVgbCqliOl2AsQLhmwAbERV1dKvmhd81GccuTDtlQNr6XFgPpokoeNoCRaVG3JUwh4-inot9yPLkUXb-42ltsjoptl6EVRmsTMDx7NVM-jiPlibFNZGAFE1ryH6FhStDzfRw0V-2W2M7rGLPu-rq1jCpfvsx1JAbeZjuD2is45g90fszN5piUgNYQuzOD7-JP540HCdrMCsYfoWB0QSy9EtjXuL1jTXagvvCSY1zScO3mZUy3Z7DT5Yxa9XB_L4M773tujNCXLA8kdwI-7bIpGweugmsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e629cfdde.mp4?token=vkUlGYM8U1smh_5g-aFKg0lgrTAOARrjNmA3PULBcTzzQ83amWV74aWXhvVgbCqliOl2AsQLhmwAbERV1dKvmhd81GccuTDtlQNr6XFgPpokoeNoCRaVG3JUwh4-inot9yPLkUXb-42ltsjoptl6EVRmsTMDx7NVM-jiPlibFNZGAFE1ryH6FhStDzfRw0V-2W2M7rGLPu-rq1jCpfvsx1JAbeZjuD2is45g90fszN5piUgNYQuzOD7-JP540HCdrMCsYfoWB0QSy9EtjXuL1jTXagvvCSY1zScO3mZUy3Z7DT5Yxa9XB_L4M773tujNCXLA8kdwI-7bIpGweugmsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری که پیامدها بعد از حمله اسرائیل را در شهر دیر الزهرانی در جنوب لبنان که خارج از «کمربند امنیتی» است، نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/141801" target="_blank">📅 13:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141800">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
چین با حدود ۳.۵ تریلیون دلار ذخایر ارزی، در صدر کشورهای جهان قرار دارد.
🔴
ژاپن با فاصله قابل توجه در جایگاه دوم قرار گرفته و میزان ذخایر ارزی چین تقریباً سه برابر ذخایر این کشور است.
🔴
این اختلاف نشان می‌دهد چین همچنان بزرگ‌ترین ذخایر ارزی خارجی جهان را در اختیار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/141800" target="_blank">📅 13:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141799">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mu4lu34iKLXtT1DjhU23M1I0HcpBK3af1ve8SHgx27H5W6xCKO1gJpVmQ0WK06Gm2fEaY7QUGSWh_h4xZ396MFD_CzYfK-BOSTUYK8kLH1wiy0P9W2uZgGX4DNba8rGttanqNTGOpq70Y2ul1-tSxTwkfwgT2VLujZBviYhV7-UFGzMk0nTqZZB91PQ3gF1SoRExwkGSGog8JI9b8cwqKxCr6uKHzsYOF35bb56_kdwWxh-UxylDx5OecuCUmexLH2-phP70mcn-QRqEKqUi23sxdzJsc1BLdMim867tQJ8Wr-0A7ADKZ-yDXqpk8ZWQRu7UcahNp5S-iUAIrvYv8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نشریه ژاپنی : پزشکیان در تماس با نخست وزیر ژاپن به وی اطمینان داده است ایران از کشتی های ژاپنی عبوری از تنگه هرمز هرگز عوارض نخواهد گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/141799" target="_blank">📅 13:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141798">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
الجزیره: جنگ آمریکا و اسرائیل علیه ایران احتمالاً وارد مرحله «بن‌بست» خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/141798" target="_blank">📅 13:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141797">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
تصاویری از پرواز و فرود جنگنده های اف۱۸ و اف۳۵ روی ناو هواپیمابر امریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/141797" target="_blank">📅 13:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141796">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOITZ56OxiasI9KbQys1jG0G3aTT3pisFXEjWLSvWbeLMi3I94Ei9phISh2yPtWtxQU4ASmJTAD6RO8Cw6Vg6ZtFClCLY5u3XMwA4RU6GhewKcWu_xLL_ub1YA3N0y4hRcwWyYgfwBHspwJseYmbDoesFDrES5uo15XwhRhkqVMiPF4RMT5fUSsyPBRDCKFSDB29Ris7e3qGZkVM94HBHYvrTM5OGyYmZ80DC7eUVm0hAcPnqscRAIINkpTHzWR6eWGLE8iZoRiKbyDvNa5vsC2ets7I53d7llyhwA3L1B0UjWme3ItxaKjAKnDc3WtGKyH_3VLJCT_lpvVuFnaNNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
بارزانی: در طول جنگ علیه ایران، کاملاً بی‌طرف ماندیم / مانع از آن شدیم که اقلیم کردستان به سکویی جهت ایجاد مشکل برای ایران تبدیل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/141796" target="_blank">📅 13:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141795">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
عوستاد خوش چشم: شروع مجدد درگیری محتمل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/141795" target="_blank">📅 12:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141794">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وزارت اطلاعات اعلام کرد در پرونده دو دیپلمات فرانسوی بازداشت‌شده در ایران، نشانه‌هایی از نقش سفیر سابق فرانسه دیده می‌شود و پاریس باید در این‌باره پاسخگو باشد.
🔴
این وزارتخانه تأکید کرده ایران اجازه نمی‌دهد میهمانان دیپلماتیک از جایگاه خود برای اقدامات مداخله‌جویانه استفاده کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/141794" target="_blank">📅 12:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141793">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
قیمت دلار آزاد به ۱۸۷ هزار تومان رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/141793" target="_blank">📅 12:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141792">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
رویترز: رئیس‌جمهور کره جنوبی خواستار گفتگو با کره شمالی برای کاهش تنش و جایگزینی آتش‌بس جنگ کره با یک رژیم صلح رسمی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/141792" target="_blank">📅 12:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141791">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
سه بمب‌افکن استراتژیک Tu-22M3 روسیه از پایگاه نظامی اولنیا به پرواز درآمدند؛ احتمالاً برای انجام حملات علیه اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/141791" target="_blank">📅 12:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141790">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPccfOWKlehrcDOB8OOutZZy4jolaGmSbBTwyxYnywWU7TQdkDpx1ULCcQwDHqRX60xLu_P8oKdyZ_3RdXpj8FQDB0yTTjOHk4wHhCzStmChD0WfAPvXQlWRfEQd_gwtb4l09l7JR9MRSCs4IJ_r0dimLszwIp8h5kM8p5pZElRYyN9LMDhbMN0DmtxaqVnQVFaMpliC8aI1PFEPaY9M8-IvxIT8Y2lL1sVeTpsZhylsuOLiAgSaAkwuZbItzojOC5FDLPASkzgtWlq4VlD5ojelCuH5H0O4DrYtkALcFzitSyTeainM2zBYk4MnWxiE2eyLIow9MPokAYEBr5uG5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هزینه جدید کارواش خودرو در ۱۴۰۵ / روشویی تا ۶۰۰ هزار تومان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/141790" target="_blank">📅 12:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141787">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qZd0qnF8Flv_KApoDm8OpP0eKe4FuMsoTs29gWEwBatL_77rx4xIzS5gddWk42YSC17uOnwS8YDO20--DQMKWE8wd72PN8vIPFN_nJ1zGaySoSsszgxNsseHsfKbPhcXtL3WSsG_q1qrELkFRJUZAXfP5oR507g2Z-4VCveeym10slGHRYa6amp7CF-sF8x2RbV627UxsLREyZaubQm_HKRE56flwukOrFF37ANRQljzMCm1bzrfYi1zeuZNqBtnATAmD8fYwNgiW5U1rZQc8CDoZNNAHXEKsq2d_qn7xZ1fHT5pmlTf1-b6j4K8V9S3vT2zcB1z9zSnuWZVUHtkhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BMTgnENhkkF1wgssoti5toK8SJ6TZYE8yqhiNe5oZUZSjssdXPubP4eHGy5NT9jFOkna34Ex0iLm707hPmEFqSwjppph3Imq7gQUJ4KYeHiIwUrDjGjQD4izW2_fYRGC3MrIp8BdQjFC2IjPThtBQI7jgIaq-V1XZkprDcggSQIcmiXPSvbcIZfxhreAALLjCa_5EK7UAmIc6ZXSggdn6T6EqlcFuJQ8ZWJVW4QyUMOGjtW_7uhZ7pPObbhpfcoqIgogD9kkPj6DyFtJE9n5ISxIcMdtrxg8KfNM3mDskdmQ6ci8X3ZXZEQFl9DCDilxEHYX5bXJu_DiMtUax2pkcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKFJ5EvopFIe5AZ2Yr2CDOCUnQ07gOviv6MPq0Cn7SekdkaAOmKkPgpBetcPljj1cymk_9o00GU42OrNuufpdWc8D9IHIpbFSsJBVlZb-thTqzoEZhxyOvlfY4rkp2svl3wolLS436Fh45fbcOSZEQaElJDocWC8Mvv8OD4Nu9fsdwjIrm3ECBR_fx7H6I2MKgPrWTMXpzcRLh7cMRvq0b79H_U9_GzrJqCG_CpC6A9jlCoysm1p6OKy1FHeX7G03wz2nbCXn2zkpdIwcVmPgd9UVO__EV_kY0jbhAaqA7ydoBO442lYVXE4ti8J3b0bcWoDg0ycFiK_HF-G_Qtt1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ، چند عکس تولیدشده توسط هوش مصنوعی از خود و جورج واشنگتن را در سالن جدید کاخ سفید منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/141787" target="_blank">📅 12:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141786">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czSa-dsVNCcHenJS-zuQj27cyu4KMxrYa320g6z5RhPONyMDSfVBsKfdBPxJcTJg640q0iBfAUTzN1NRi2pGa5pCifwL3Ob7srE2voBXOtwUt9YDjwMfhefykb7gvNRRmqCHk0ZrDxV6wutPnZxn9uBzYBAMawYKYq2kV5vhTuz7ldIJPGGWw0i_TDqpI4bBCfFNIl63BSBGtllcDGpiTzzUKUzcX1IYgNXX_EyMdWnrJqp8mB6kQI6Dr98KoMHIqXy-U6go9MvYJG32n-kMmGX8smeOr_5McoD6GhL31XeX_qSPzCk8s2L5YLMmPila-fjk7waVt4zcVEvI525R9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابوالفظل اقبالی از نزدیکان جلیلی: انقدر وضع حجاب خرابه همه مردها تحریک میشن حتی خود من
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/141786" target="_blank">📅 12:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141785">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره :
@khabar
◀️</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/141785" target="_blank">📅 12:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141784">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سلمانی» معاون سرمایه انسانی سازمان اداری و استخدامی کشور: بر اساس اعلام وزارت نیرو تا ۱۵ شهریور امسال ساعت کاری ادارات از ۷ صبح تا ۱۳ بعدازظهر تعیین شده است و بعد از آن در صورت درخواست دستگاه‌ها، تغییر ساعت اعمال خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/141784" target="_blank">📅 12:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141783">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ارتش اسرائیل: به حزب الله اجازه نخواهیم داد که به نیروها و شهروندان ما حمله کند و به از بین بردن تهدیدها ادامه خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/141783" target="_blank">📅 11:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141782">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/953b386e17.mp4?token=T_OO4UQbnWRNlNs93bzva5grFR3HqmjnnPQHRMHlxIxCuBaPbeVblLStto5F0i26mLUR06x2ZKj1EPzMDcnJGD6vAvFrD5z5zRFO0LruFvQeCHruX0sgcoQbtrRMeGwI-2sTUlJup7xzNO8O-5YGtuHgc8F_65AUmPmQIuazjVDUxbjPCstNzoUtOfyyavmR-t4qporMkc9Yb7y_pAUvL7eYKhk5zSizsp3BYps1X4GSls-0NuA2F6g7IQLlmA9FmBdW_zjrA6exCL1JNvAIKz7YfC-pUDCdjaPWwt7W1GckTEgTo7tI--J_-SwU3136J5eY6iI3loHs8U72l7h1gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/953b386e17.mp4?token=T_OO4UQbnWRNlNs93bzva5grFR3HqmjnnPQHRMHlxIxCuBaPbeVblLStto5F0i26mLUR06x2ZKj1EPzMDcnJGD6vAvFrD5z5zRFO0LruFvQeCHruX0sgcoQbtrRMeGwI-2sTUlJup7xzNO8O-5YGtuHgc8F_65AUmPmQIuazjVDUxbjPCstNzoUtOfyyavmR-t4qporMkc9Yb7y_pAUvL7eYKhk5zSizsp3BYps1X4GSls-0NuA2F6g7IQLlmA9FmBdW_zjrA6exCL1JNvAIKz7YfC-pUDCdjaPWwt7W1GckTEgTo7tI--J_-SwU3136J5eY6iI3loHs8U72l7h1gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف
:
تو آخرین حمله به ضاحیه، مذاکرات رو متوقف کردم و گفتم اگه اسرائیل جواب بده
🔴
کل منطقه رو می‌زنیم، همون شب محاصره رو برداشتند
🔴
وقتی ترامپ هم درباره باز شدن همزمان محاصره و تنگه توییت زد
🔴
تهدید کردیم اگه حرفش رو اصلاح نکنه حمله می‌کنیم؛ ترامپ هم پستش رو اصلاح کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/141782" target="_blank">📅 11:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141781">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c188240e7e.mp4?token=Ut4gugewPmvgK04EUOuxQoiFOsvp-is1O1zV6L3kLYFN7bQw-g2Z21XsaNM0y3oCuN7EI-FMcytS1B8gb-J68MOo25fEv4eLT_QVyGJdWiHFcHfdPOZytjg0yz3BUvk4geKakO96L0QiBB_hHutWN2E6n6qUmniQUIe3xumvdpkSBlgNiUIC0ckmVmL7uYqb4ridFvA2AlKCQDlBnKGy4dtii4LxGpVhVwjvcz9tNvM0wZtJw_PTwEEpqcT3hHMRV0IcklHa9kB7PPGHgkM-D6KrQP2UtY_s5qY21TaAxU1QMXzr5I9OlK3cBmOpRjKsUpPF2e8V_vNhmAVeDoNJyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c188240e7e.mp4?token=Ut4gugewPmvgK04EUOuxQoiFOsvp-is1O1zV6L3kLYFN7bQw-g2Z21XsaNM0y3oCuN7EI-FMcytS1B8gb-J68MOo25fEv4eLT_QVyGJdWiHFcHfdPOZytjg0yz3BUvk4geKakO96L0QiBB_hHutWN2E6n6qUmniQUIe3xumvdpkSBlgNiUIC0ckmVmL7uYqb4ridFvA2AlKCQDlBnKGy4dtii4LxGpVhVwjvcz9tNvM0wZtJw_PTwEEpqcT3hHMRV0IcklHa9kB7PPGHgkM-D6KrQP2UtY_s5qY21TaAxU1QMXzr5I9OlK3cBmOpRjKsUpPF2e8V_vNhmAVeDoNJyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف
:
در تفاهم نامه، آمریکا می‌خواست ایران از موضوع موشکی، هسته‌ای جبهه مقاومت و تنگه کوتاه بیاد
🔴
اما ترامپ در نهایت به‌رسمیت‌شناختن جبهه مقاومت رو امضا کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/141781" target="_blank">📅 11:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141780">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
منابع یمنی از حملات توپخانه‌ای ارتش سعودی به شهرستان «الظاهر» در استان صعده خبر دادند.
‏
🔴
همزمان حملات راکتی از سوی خاک عربستان به سمت منطقه «بنی صیاح» در شهرستان مرزی «زارح» گزارش شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/141780" target="_blank">📅 11:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141779">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrG2PAWGhBKk16k0VserA684I7YQiCwK6RozE2URqTn8Y9iNfFbiDL6g81BAt6DyOw9tEywWzvMVDOt78UWxCUispk6BKN6Y6-IipZDmix4IBPt9xiLRmAgWQDw1-ySjPqWceVz43qk1pqJaWbpb-6Iew-A9JYwHAP3vi0GCv1Im8lo65v_Q5L8u3YwzMypOQQXaCbwRtre-isOL_-grVS8YzTbo4Uspk74-EF1hVeotuMGNm-_pp4C2bJiruC0hIQtHI5ZPZ7sniADnzUPouvmufekWaWGhvkQz5tPJvDK2gQD3IuWUDprdTo7ciEmbOyNrgI31ZZD9WpIlRi3GYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از اپل می‌خواهد که از خرید تراشه‌های حافظه از چین خودداری کند، زیرا افزایش تقاضا از مراکز داده هوش مصنوعی باعث کمبود جهانی و افزایش قیمت‌ها شده است، بر اساس گزارش وال‌استریت ژورنال.
🔴
اپل در حال آزمایش تراشه‌های تولید شده توسط شرکت‌های چینی CXMT و YMTC است، اما اعلام کرده است که باید "تمام گزینه‌ها" را در نظر بگیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/141779" target="_blank">📅 11:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141778">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2JGP2vrnpzCY0z1B2UjG1EbGOL6h0-uma_ClddT4DikfqBSYpwhXGmty53gE4bknnVkC_5bNTryI5CgLDCxdU9e-RKJ6BTwEZdjWbABx978eB5xs3knAqRB5OvIieW30zdA8LML5GqIydMkBEMw768YDlyT9fB-DrMIh156EOD2KEaN64JUb_Y_SbIgw_qtEXMub03DDIdllr26K9ZOvM8kax4Yx9mwTA9uA1XIkAWVMTm679ClYd_laTSh41p3ug6kssyzh9t_0qgcWRoL2nJR0XBKIxFJMduquCtiTv0e_J_aJ7pe1QkbPcAAkCeCxVRjDo3UA2fjL8QWxyH1qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق شبکه اجتماعی Truth Social
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/141778" target="_blank">📅 11:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141777">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNOffuOJc8UK1C7mJO-nMMGPx3RZTYrrwTQ0fIzJo09ztD87-09tWqLntVZCZqUnjw-ot3uEXYA1k6ubh34b1FEsTgP57HDMvLCZH8aOqhHGs4NO6b-twhkX-NdHBNSms73oZ_8lSRPj9U9ixAPrqu43ENhhBJI4dWv5zasn_Dk4iuS8-fAAH6rbs7zNeTXf42-y_iToPLr2ivrBNFmvRhlfvA3Vd7D7sLHZN_7SbKCk6j_j-sHml7aWBN202jaZ9oKSlx7o6r5WU4iRTOAtt73M4A3k2a-6xNO3RpEb9Hal8peggz213eAAfiCqvzP4VJYLAQExV0h_mqXz2xvi7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نشریه NYT : حمله ایران تو روزهای ابتدایی جنگ به پایگاه دریایی آمریکا تو بحرین
🔴
این مرکز مهم لجستیکی رو از کار انداخت و نیروی دریایی آمریکا مجبور شد، تدارکاتش رو از جزیره دیه‌گو گارسیا تأمین کنه
🔴
مسیری حدود ۲۲۰۰ مایل دورتر از ناوهای آمریکایی نزدیک ایران
🔴
این مسیر طولانی‌تر باعث کمبود و فشار بیشتر روی ناو هواپیمابر آبراهام لینکلن شده
🔴
۵ هزار ملوان این ناو تقریباً ۹ ماهه در دریا هستن و هنوز وارد بندر آزادی نشدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/141777" target="_blank">📅 11:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141776">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ملیکا همت‌زاده، دختر ۱۳ساله از روستای دسکِ بنت استان سیستان و بلوچستان، پنجشنبه دچار عقرب‌گزیدگی شد
🔴
به گفته اهالی: به‌دلیل نبود امکانات درمانی کافی در روستا،با خودروی شخصی به نیک‌شهر برده شد
🔴
تأخیر پزشک در نیکشهر و سپس اعلام نبود امکانات کافی و لزوم انتقال به مرکز دیگر،روند درمان را طولانی و ملیکا جان باخت...
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/141776" target="_blank">📅 11:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141775">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
کپلر: روز جمعه تنها دو کشتی از تنگه هرمز عبور کرد؛ هیچ محموله نفت خامی نیز مشاهده نشد
🔴
کپلر، بر اساس تحلیلی که انجام داده است اعلام کرد روز جمعه تنها دو کشتی از تنگه هرمز عبور کردند و هیچ محموله نفت خامی نیز مشاهده نشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/141775" target="_blank">📅 11:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141774">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
حاجی‌بابایی: مجلس می‌تواند با رعایت پروتکل‌ها حضوری شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/141774" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141773">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=m5bxirfv7FAiPB1Auw43-JZocQlrSD_PpGDiroeAoaeEE4Gr_cotVCrx0G4RwteXgWo6qQ2IlR9dlYTGHe9ozNCrdwuG33D3W-eNwCXq13EfBO1GGSce8GoDVVxtfokZFZtmXatBTdZunyG3-JnwKF6Xk0WXaQGpHFdKmpy-tGcSEayynkdjWz38Q2EiUzYaq58z7nqFh7PejGxlxiSEkcdOhje5WZz01SP1Z1bY1iwvCs-f47mSj3uH3TScsWaHSc73yc-FVyUBuDokR8zMYnqf8PfORvjH4ntX-Fxk1HnaMhzjcpldmKuUTlqMYL86AEPiTs_WbnWbd1AOO8XdDYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbc04a175.mp4?token=m5bxirfv7FAiPB1Auw43-JZocQlrSD_PpGDiroeAoaeEE4Gr_cotVCrx0G4RwteXgWo6qQ2IlR9dlYTGHe9ozNCrdwuG33D3W-eNwCXq13EfBO1GGSce8GoDVVxtfokZFZtmXatBTdZunyG3-JnwKF6Xk0WXaQGpHFdKmpy-tGcSEayynkdjWz38Q2EiUzYaq58z7nqFh7PejGxlxiSEkcdOhje5WZz01SP1Z1bY1iwvCs-f47mSj3uH3TScsWaHSc73yc-FVyUBuDokR8zMYnqf8PfORvjH4ntX-Fxk1HnaMhzjcpldmKuUTlqMYL86AEPiTs_WbnWbd1AOO8XdDYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش اسنپ از وسایل جامونده تو اسنپ تو سال۱۴۰۴: ۲۶۱ هزار کارت بانکی، ۱۷۸ هزار کیف، ۱۳۷ هزار موبایل، یه کنسول PS5، لباس عروس، ۲۷ هزار ایرپاد، یه نوزاد شیر خواره!
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/141773" target="_blank">📅 11:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141772">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
وال استریت ژورنال: جنگ ترامپ علیه ایران به مسابقه تاب آوری اقتصادی رسیده
🔴
ترامپ تحریم‌ها و محاصره علیه ایران را تشدید کرده در حالی که تهران روی این حساب باز کرده که قیمت بالای نفت، واشنگتن را مجبور به کوتاه آمدن خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/141772" target="_blank">📅 11:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141771">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GE1kL1hMGM4jOlcLxY9slFlx8fWfeRO53eQKPom708C1Tn4FF9MqzumZWppBryjfvwvWcsutuKpY1sZU9vfgCVjlRT3OSWxD2mkqnQLUsbZ_mIFrKfdCFjGN4Vp8L3ZaqjMixzc7hTEdPHJFD8vxPmXI5A352EcubNB950MkQ1ZMe5U-RSnlYzgRaicBqLYEHOkc20GpPHMfTR4hWo8-juowriuweSebAKlNVz_nKxDLfuclrCBYBnjPb3WgF3AuNyETm1k1vM78fK6Ipg2K04ZlHcHmP5VIY0zumzRip9C5IjtaMrJI6Bz7NNp7_efAhqqmRuZuyWcRXl04PNEg3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقایسه آمارهای سال ۲۰۲۴ نشان می‌دهد ایرانی‌ها به طور متوسط هفته‌ای ۴۶.۳ ساعت کار می‌کنند؛ رقمی که ایران را در میان ۱۷۰ کشور جهان در رتبه دهم قرار داده و افسانه کم‌کاری ایرانی‌ها را رد می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/141771" target="_blank">📅 10:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141770">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0azIXMuNwyBe01MywSivaY7MCBlJe9nTS6-vz_ep2Nx5nsCON2sT7syRkUDxGVfRhCi37huBGFJiRT6Ftt91qeJ_dpW81jExbsvv3Ed1YHwkxl4L4lZVo2NzaOpjlzt3EC6GnmAT51rlXy9buOxAyUwAYbYdFDLC0OEDG7iYKgBstVPWYNFpPq3uee2Az7PieCjiyTPfvB5u81JE4L9RzMqpyf8zTs6CHzZAS0NZctoQQhMcd7l8s4rYQEt0KgQPAjJtdVMcZmZr6ieiN_vNHA__pnPCJ95jK6IG57SDq-EklHdJcI2ulDCkxQry9meAT9B1OhguUrk_9RFQXn7hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسماعیل بقائی، سخنگوی وزارت امور خارجه: این فراز از رمان برادران کاراموزوف نوشته داستایوسکی به درستی وضعیتی که سامانه حکمرانی و سیاست خارجی آمریکا در ارتباط با منطقه و ایران به دلیل اتکای افراطی بر دروغ به آن دچار شده است را توضیح می‌دهد:
🔴
کسی که به خویشتن دروغ می‌گوید و دروغ خود را باور می‌کند، سرانجام به جایی می‌رسد که دیگر حقیقت را، چه در وجود خویش و چه در جهان پیرامونش، از دروغ تشخیص نمی‌دهد و آنگاه هرگونه احترام به خود و دیگران را از دست می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/141770" target="_blank">📅 10:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141769">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zq-Mbo0XA7hlI8Xu69RBvmiIzmfwrvTE8CQ5Sb50jJjIRymoBKQiDcv7vfSgpHVjKNfstCc8GI4_8EWKxrAV0uXgOt6oDUsZDA7mL3ip65OHcKUQYlnuk5VeJk4R9HLTm-b1xhhbRrQ1u39E2skfNNVDbXIExHYpQtNVAYIBcFYb5qHvaSbPWRA-hhVSvpisi1C8-RJS_5NkrjC27T4ZMDDNCdiQ6HyjoZQfOXRxcQ8iAT3hT-KyAFSvPoIXdRfISeQRQCL1z3FM_97lF44R7bNoHQUIS_XrtVXXknuRAgz-lWGb2P5V_fKGUcUq9bRj3Vm-hh4ayV-exTHoJpyGOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک پهپاد اسرائیلی یک وسیله انفجاری را در ارتفاعات علی الطاهر در جنوب لبنان رها کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/141769" target="_blank">📅 10:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141768">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
احمد وحیدی، فرمانده کل سپاه پاسداران : رزمندگان ایرانی در شرایط بسیار سخت، مسلح‌ترین ارتش تاریخ جهان را به زانو در آوردند. انشالله به زودی با پایان دادن به درد‌ها و رنج‌های مردم منطقه، جهان برای طلوع خورشید عظمای ولایت، از همیشه آماده‌تر خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/141768" target="_blank">📅 10:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141767">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
روسیه: انبار حاوی سوخت نیروهای مسلح اوکراین در بندر یوژنی را هدف قرار دادیم
🔴
وزارت دفاع روسیه: نیروهای مسلح روسیه انبار حاوی سوخت و روان‌کننده‌های مورد نیاز نیروهای مسلح اوکراین در بندر یوژنی را مورد هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/141767" target="_blank">📅 10:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141766">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
قیمت نفت صعودی شد
🔴
قیمت نفت خام در معاملات روز جمعه بازار جهانی، به دلیل حملات به نفتکش‌ها و عدم پیشرفت در توافق صلح میان ایران و آمریکا، بیش از یک دلار در هر بشکه افزایش یافت و رشد هفتگی چشمگیری را ثبت کرد.
🔴
قیمت نفت برنت با یک دلار و ۴۵ سنت یا ۱.۶۷ درصد افزایش، در ۸۸ دلار و ۵۲ سنت در هر بشکه بسته شد. قیمت نفت خام وست تگزاس اینترمدیت آمریکا با یک دلار و ۱۵ سنت یا ۱.۴۲ درصد افزایش، در ۸۲ دلار و ۴۰ سنت در هر بشکه بسته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/141766" target="_blank">📅 10:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141765">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴ امروز وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/141765" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141764">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏
👈
اهواز ۵۱ درجه‌ای می‌شود!
‏
🔴
رئیس مرکز ملی پیش‌بینی وضع هوا: اهواز با دمای ۵۱ درجه سانتیگراد طی دو روز آینده گرم‌ترین مرکز استان کشور خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/141764" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141763">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-46Bu1ZIBOCa9ptv5yasMJlaQ0jQMEYEEIRzw5VhjfXtD3oxIksA2wgSirnNw4WUKRvd06AfNj5DwzKOApCW5gA5C7WbLHepMnMwKukcxDCwl4jUeBm0A_vCXA8rCJZJKUZMzJMcAPZ0ktVAZK6fWUqyRv7xH_ahKO8XtmEjnm2Qsu3mU-iJNT4yHIAmjPoZrcHQFvCS5zAb5u2-UZ41YnjQdiudv_5i7YVpdBqQYDdmQsuG4dr3tZImwcsiKquW-xxSvitigsINlSgRSEwPwmKfz0l9EqNEoeahJ07J979o6dpYx2dqxSd-GewVVXh6BzHhbXiEc9lKY-Tzy01Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
فرمانده نیروی عملیات ویژه سنتکام در خاورمیانه تغییر کرد
‏
🔴
فرماندهی مرکزی آمریکا، سنتکام، اعلام کرده است فرمانده نیروی عملیات ویژه این نهاد تغییر کرده و دریادار توماس دانوان جایگزین سرلشکر جاسپر جفرز شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/141763" target="_blank">📅 10:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141762">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
حمله به نفتکش شرکت «ادنوک» امارات در تنگه هرمز
🔴
شرکت ادنوک امارات تأیید کرد که یکی از کشتی‌های این شرکت هنگام عبور از تنگه هرمز هدف حمله قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/141762" target="_blank">📅 09:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141761">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
حادثه دریایی در نزدیکی تنگه هرمز
🔴
گزارش‌های رسانه‌ای از وقوع حادثه دریایی در نزدیکی تنگه هرمز خبر می‌دهند.
🔴
سازمان تجارت دریایی بریتانیا: گزارشی درباره اصابت یک پرتابه ناشناس به یک کشتی باربری در تنگه هرمز دریافت شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141761" target="_blank">📅 09:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141760">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1bb640dd0.mp4?token=J_diY08OlLyvM866L7XZT19uOyny12lmrQb_brunHdA0CZudYJ5GDb9118ZY7mTJfD7veOgkfo9fn42JsKPtPX5Egft8L08nuC564JQgXctdYS06ML4wKkvNWFymHK3T-9JLi_njiulMr6_IKMcmm2aR5hlfktSzN1Vvuokqci7ryTVrZKMpJOA13D3mKGK0ZrY46ATQzRQ9szul0emC20wUXu2Ffi8mqW7c-ggHEngM67EoAKSljCVVDrnD8hbyq5pIzuBkVwTPh70njylxhHJbq0g4-nHpzta13nHz5fMMOFxTcKOzv0Pg8YVtzwb3in59O_t23mu2Xz5ceCWrAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1bb640dd0.mp4?token=J_diY08OlLyvM866L7XZT19uOyny12lmrQb_brunHdA0CZudYJ5GDb9118ZY7mTJfD7veOgkfo9fn42JsKPtPX5Egft8L08nuC564JQgXctdYS06ML4wKkvNWFymHK3T-9JLi_njiulMr6_IKMcmm2aR5hlfktSzN1Vvuokqci7ryTVrZKMpJOA13D3mKGK0ZrY46ATQzRQ9szul0emC20wUXu2Ffi8mqW7c-ggHEngM67EoAKSljCVVDrnD8hbyq5pIzuBkVwTPh70njylxhHJbq0g4-nHpzta13nHz5fMMOFxTcKOzv0Pg8YVtzwb3in59O_t23mu2Xz5ceCWrAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلزله‌ای به قدرت 7.7 ریشتر سواحل اندونزی را لرزاند! ساختمان‌های آسیب‌دیده در جزیره فلورس، اندونزی. گزارش‌های محلی حاکی از تخریب چندین ساختمان در این جزیره است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141760" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141759">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/449d6fd03a.mp4?token=I753F18c-joQT9jnfWmRmBjMY8JG_9CC9IxeAKmgVXOCmyN49KKm-78cWDRNnlWeyu0tYTM7Y3fXlfkT34lS8MjyFxP0FA_nVhu_ib2tTxQ-d9Md-KJACY66zjhhpWKRPGmAc3KXDRtd2Stq3e43q7PHwyF86QC2DiFacj4VcwD7etWFSeEE94hJ9fl8kgIUZCrlrjF2JiU-FJQCTP9bUkvnCbsLvNAEf7lOmr6K19iIHsSTxdGwGcdCosbzGQN6Qo10arSRZVe1huRMZTgoWQhoAuBtQqHXI7o3dJ-cMQjwYyfz6QGm8pmX617clMJLmUumzMBd1xNdpSWVziirMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/449d6fd03a.mp4?token=I753F18c-joQT9jnfWmRmBjMY8JG_9CC9IxeAKmgVXOCmyN49KKm-78cWDRNnlWeyu0tYTM7Y3fXlfkT34lS8MjyFxP0FA_nVhu_ib2tTxQ-d9Md-KJACY66zjhhpWKRPGmAc3KXDRtd2Stq3e43q7PHwyF86QC2DiFacj4VcwD7etWFSeEE94hJ9fl8kgIUZCrlrjF2JiU-FJQCTP9bUkvnCbsLvNAEf7lOmr6K19iIHsSTxdGwGcdCosbzGQN6Qo10arSRZVe1huRMZTgoWQhoAuBtQqHXI7o3dJ-cMQjwYyfz6QGm8pmX617clMJLmUumzMBd1xNdpSWVziirMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحنه‌هایی از ویرانی در پی حمله هوایی نیروی هوایی اسرائیل به عینسار در جنوب لبنان.
🔴
فیلم‌ها همچنین نشان می‌دهند که گروه‌های داوطلب نجات انجمن راهنمایان ریسالا اسلامی جنبش أمل، حزب سیاسی شیعه لبنان، در حال تلاش برای یافتن لبنانی‌های احتمالی زیر آوار هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/141759" target="_blank">📅 09:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141758">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEAEKMONJQwngzEVRU8sIlud3XPAim6XtvHmrqKa7v0_SBzUOgJ9Zg8QGpCHMRapn7g8CvnxfTXRTl-vlAW6jFB3IVDwO0G1HIB7qknHev46GvtpM7vehTcl4cDrXcELXOz_B2eKDdSAuYQJMSbGkGa7OdrWcEj8jgwpOtbs19Lp4rwFQazk3wtYdTKBpAcSBcbd88i7DJfWpD21JmzLfuUWRnEbdD_8Hj6J1zlbRhIJqdvMWcjFHM4K-K_zTYYe47x1gfd3QPHmElN-zZh3RDmlycyGbe1z7C_kV2DGrYYJyaVH4xcChpbL3Ikxo-OXJWzsL7LC-5-ELmPMciylFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکس از حمله اسرائیل در نزدیکی قلعه قلعه معس
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/141758" target="_blank">📅 09:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141757">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7e6980068.mp4?token=d9vnGhyINUsSydm4BegJ-4KwQrX3SA91EHbCznq-czAuJXVrakyi93rZAOdiPr2Ox3i8Z_JOln-Ml2VesFMeEbsFIPMGmIZBemfa6H-4g4ax37sB5C0knolP33CzWiDoUFJsthimJaMIwQfDFC6DEBoEB520411bmlINpcroTa2MKzVI5sgQJQv6bEEkgOKib5rF9m_GyZYOheqxN26lGatCZuBFYQv5iymrBSLwBbGMqaOip8HEkiiIbqsNISHcvA7qW5P0Z3tkwWzJZb0HZtiISJTNXhpQTp-YBP46Jqs2a52IhBFgVeOtRlBSsAoZ8DSLX-i2m_qCIFkj_KYUFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7e6980068.mp4?token=d9vnGhyINUsSydm4BegJ-4KwQrX3SA91EHbCznq-czAuJXVrakyi93rZAOdiPr2Ox3i8Z_JOln-Ml2VesFMeEbsFIPMGmIZBemfa6H-4g4ax37sB5C0knolP33CzWiDoUFJsthimJaMIwQfDFC6DEBoEB520411bmlINpcroTa2MKzVI5sgQJQv6bEEkgOKib5rF9m_GyZYOheqxN26lGatCZuBFYQv5iymrBSLwBbGMqaOip8HEkiiIbqsNISHcvA7qW5P0Z3tkwWzJZb0HZtiISJTNXhpQTp-YBP46Jqs2a52IhBFgVeOtRlBSsAoZ8DSLX-i2m_qCIFkj_KYUFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در منطقه علی الطاهر در جنوب لبنان درگیری‌هایی گزارش شده است.
🔴
به نظر می‌رسد عملیات نفوذی اسرائیلی در حال انجام است. این اقدامی است که اسرائیلی‌ها مدت‌هاست به دنبال انجام آن بوده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/141757" target="_blank">📅 09:09 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141756">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
رئیس پلیس امنیت اقتصادی تهران بزرگ:بیش از ۶۸ هزار لیتر فرآورده نفتی خارج از شبکه توزیع در یک کارگاه غیرمجاز کشف شد.
‏
🔴
ارزش سوخت کشف‌شده بیش از ۴۶ میلیارد ریال برآورد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/141756" target="_blank">📅 09:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141755">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
مدیرکل فرودگاه‌های هرمزگان: پروازهای فرودگاه بین‌المللی بندرعباس از امروز  در مسیرهای تهران، مشهد و اصفهان از سر گرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/141755" target="_blank">📅 08:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141754">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
دولت انگلیس در پی خشکسالی شدید و افزایش خطر آتش‌سوزی، برای میلیون‌ها شهروند در سراسر این کشور هشدار اضطراری ارسال کرد؛ اقدامی که در تاریخ انگلیس بی‌سابقه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/141754" target="_blank">📅 08:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141753">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2I3vNHXKWHcAdvGv6Ms5htD64kP7fyczbhUyc-zfRql7fDV3sRLeaLzcWSjUA6ZdK0mi2LYZzhp__k04QJs5k3eEr3W66QtVIGfG1gTMGwCsij1C0G3lvWrBDObTyoo9ys_vn2DwuLCmkfwR_N_Uk3QQRGglPsgE12rbFGBG7p5z1zohjwaL-yokvwUT47-F7PwYwKJbsiYT8mMNTNnpHTmTB3O20b-t98pfya55FOiCfTemeTb14hzQ7BRLtBnoRSFn37RKOZBQNRgiu3wFoHGnxnWNKPsM1Gr_7z_CGHNaBZanD4216_VwQ-am6kWYXBocPG6vL5Cn5CLQsuLMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه یدیوت آحرونوت گزارش داد که اسرائیل همچنان منتظر مجوز نهایی از ترامپ برای تصرف تپه علی الطاهر است، این پایگاه زیرزمینی استراتژیک حزب‌الله که گفته می‌شود ده‌ها جنگجو در آن محاصره شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141753" target="_blank">📅 08:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141752">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از یک مقام ارشد کاخ سفید: ترامپ در سخنرانی خود در مورد اعلام تنگه هرمز به عنوان بخشی از خاک آمریکا شوخی می‌کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141752" target="_blank">📅 08:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141751">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
فوری / زمین‌لرزه‌ای به بزرگی ۷.۴ درجه در مقیاس ریشتر اندونزی را به لرزه درآورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/141751" target="_blank">📅 08:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141750">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
نیویورک‌تایمز: مشکل تأمین و تدارکات ناو آبراهام لینکلن پس از آن آغاز شد که ایران، به پایگاه نیروی دریایی آمریکا در بحرین آسیب شدیدی وارد کرد و یک مرکز لجستیکی مهم را از کار انداخت
🔴
سپس پنتاگون مرکز تأمین و پشتیبانی منطقه‌ای خود را به دیه‌گو گارسیا منتقل کرد که ۳۵۴۰ کیلومتر از ناو‌های آمریکایی فعال در دریای عمان، فاصله دارد
🔴
این طولانی‌تر شدن مسیر، به مشکلات لجستیکی ناو‌های هواپیمابر دامن زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/141750" target="_blank">📅 08:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141749">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87e3beeae8.mp4?token=MhNAa9gcQb1jHjVa2lhw71CfDfDP-p3v3CVCAQ0pK978ZHqkNqfuNn3Vqb863lNyk183wTzhan-ObxVu3QrKqQxDCiv1ppSUEgAnU-FkGn-KdTUIA48jJhJPsmoCt8V_zx7kBOWb2DyxTLx6ZK2rYjoZG9G5m51WiE8xgkoHLNZMAPsTNLfSb6zi9c4c5-NnIaeHSl8uT2hHwIUXii4j-syAPRZFd0BcYBgoa9A7RuDDJviBNx79uldYtcWtmaIaSRIWwPIvPkvaBpfQK7Guv99Wa9UIagKBWMjD685afbRLaNHrJrHmV8-h-UfEMDo040U51Ep3xhSKlkYlLMRv8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87e3beeae8.mp4?token=MhNAa9gcQb1jHjVa2lhw71CfDfDP-p3v3CVCAQ0pK978ZHqkNqfuNn3Vqb863lNyk183wTzhan-ObxVu3QrKqQxDCiv1ppSUEgAnU-FkGn-KdTUIA48jJhJPsmoCt8V_zx7kBOWb2DyxTLx6ZK2rYjoZG9G5m51WiE8xgkoHLNZMAPsTNLfSb6zi9c4c5-NnIaeHSl8uT2hHwIUXii4j-syAPRZFd0BcYBgoa9A7RuDDJviBNx79uldYtcWtmaIaSRIWwPIvPkvaBpfQK7Guv99Wa9UIagKBWMjD685afbRLaNHrJrHmV8-h-UfEMDo040U51Ep3xhSKlkYlLMRv8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تمسخر ایرانی‌ها توسط یک عراقی
‼️
🔴
یه عراقی با ماشینش اومده ایران، و همه با حسرت بهش نگاه میکنن و فیلم میگیرن.
اونم می‌خنده و این ویدیو رو منتشر کرده و حالا در سطح جهان همه میگن ایرانیا ماشین ندیده‌ان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/alonews/141749" target="_blank">📅 01:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141748">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aW7Ruw01sZO8JKmFd1kXtLFgkMx3wTe0N2cW0tkm4J-BzAqILjNAN_aEiSB98hSoDQaONlHZNxHXZ98mEQ_7nWIhTihfL6KbPK7Se1OvIY2nEJYcJz8lCEH2jhfyMi-xwScoBJw2J2_VFMBFfnh14meppkh5otsj3HlLroRfJFfA0fFbKw8nAjLnnsiQqWmCfmFr8b4rTcz4KJ_IZ8uWcWaqH2DLjxPihGICFH6zenA--z7fqJPSEnuCp-GQF99Y2EDF8qfMS4mLCWR7lvL9HfAS9i6yaQwpwi8Q3K4ihk-yt0pkJ-25BLQtDvwMHsjWmsPayxtyw6g0FDY1M1wPwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هادی چوپان: به لطف مسئولین عزیز و زحمتکشمون یه بلوار به نامم شد و آرزوی من محقق شد
🔴
دست مسئولین رو میبوسم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/141748" target="_blank">📅 01:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141747">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ: میتونیم تو ۱روز ایران رو نابود کنیم اما این کار رو نکردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/141747" target="_blank">📅 01:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141746">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGa0bxktUELrd2AI-5tfVwdbyxyerG9CysG6prD_hOiQL9RYIHguAZ7YJ3d0bVUbEXA7tdKTDE6xCYmi_gpuSGyiApBUhYxqrzfa66PYicnIi12lIojo8-GuJ3jLA4gf76XGME31ctEnliASfQmEtdoY9MhhzbJNeBbY_i_BfIZjBo8HvzLR3vz1NvdZru0uBkpm5-mPcMlHfjCOvWyjkShMs5dykmLcrBHfJ2jHsl83c-em6_0y8kZUNv3pPQ0aCcVoA1tMyAD_OBwvSXQn9HS6Tk9cU8jfViQ5Ije22V6Au2YnmlkrCdx4eWPjQ4rm6SFPFrxZhkw33MjrRfGoTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
بلومبرگ:
دولت ترامپ در حال آماده‌سازی "اقدامات اقتصادی بی‌سابقه" علیه ایران است، به منظور وادار کردن این کشور به توافق قبل از انتخابات میان‌دوره‌ای نوامبر!
🔴
این اقدام همچنین نشان می‌دهد که ترامپ به جای بازگشت به حملات نظامی در ایران، به فشار اقتصادی و دیپلماسی اولویت می‌دهد، با وجود فشارهایی از سوی برخی مقامات ارشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/141746" target="_blank">📅 01:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141745">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
کاخ سفید:
تمدید آتش‌بس با ایران هنوز قطعی نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/141745" target="_blank">📅 01:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141743">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3081852fbc.mp4?token=j5Ty0DVGVqFZe5w54BB86UONeuqCFneLPn0qpWUwtn-0lU-xrQEUgaJlYbHs3GC4imXdGcfXbOyG_lag0NqpSA_6o9GYkIkVzssGUiqhuaSWrUjsqKOeWXm8vJEi-NUm51tr9NvoNBK9zWOccZ2fD1ntrbD_H_TnnETcPWyxoPR40U9mjvFwflLdS1e7DjeqyAuFluQl4KK1jrDeajEYOyOvJ1F4Ck6hHF7rUZOUKpeGgYO5jZygJpZmpAkEi0DLNJ58Nyike9G0NycrS-LshCsVbGyNp3er56KC7QSPLkbc5FqJ1m6plAz-DDWDgnszRF_0jntHNLFd9Robv2T8MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3081852fbc.mp4?token=j5Ty0DVGVqFZe5w54BB86UONeuqCFneLPn0qpWUwtn-0lU-xrQEUgaJlYbHs3GC4imXdGcfXbOyG_lag0NqpSA_6o9GYkIkVzssGUiqhuaSWrUjsqKOeWXm8vJEi-NUm51tr9NvoNBK9zWOccZ2fD1ntrbD_H_TnnETcPWyxoPR40U9mjvFwflLdS1e7DjeqyAuFluQl4KK1jrDeajEYOyOvJ1F4Ck6hHF7rUZOUKpeGgYO5jZygJpZmpAkEi0DLNJ58Nyike9G0NycrS-LshCsVbGyNp3er56KC7QSPLkbc5FqJ1m6plAz-DDWDgnszRF_0jntHNLFd9Robv2T8MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدون شرح
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/141743" target="_blank">📅 00:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141742">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری بریزید اینجا
👇
https://t.me/+nCexQYLuuONhYzg0
https://t.me/+nCexQYLuuONhYzg0</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/141742" target="_blank">📅 00:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141741">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
عراقچی:
آنچه در یادداشت تفاهم اسلام‌آباد آمده «خاتمه جنگ» بوده و نه آتش‌بس
🔴
آمریکا این یادداشت تفاهم را نقض کرد و درگیری‌ها مجدداً آغاز شد
🔴
بنایراین چیزی به عنوان آتش‌بس ۶۰ روزه که نیازمند تمدید باشد وجود نداشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/141741" target="_blank">📅 00:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141740">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrlHHXDPgFqu-W7nzjfAAdMaYRM3sEmEd7U877gPi3JoU5odCTHJ14iPLHBeQAzBX3qNTOIEUwwzrHo-58DZy6pnMxtwhJZd1pHpMMCRNbAUMJ_GsAxRcFjziavg5ROYo5IEMyaHfdbXyYuVLbIBW88JxPubSbMVNYrH5f4NEwhxmyAOXTbwZ1IaOqL79bXTVPTCLbB2sRlqK0og6MIRARjiDlNNUUsiYZ_QGf3rI92_G12h-d4r0MFQvVcSwhvsPwn7ZeSZp9sGYywz4Zdo3p5NW0JCAbs_CXlyQtgu0MjkaA7H2P7TJmo-0NL6r07GrLEXK-MfsFNfnkGu2F-2LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: پول نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/141740" target="_blank">📅 00:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141739">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0wDAnWsRF9HhOWchoNsrVhsKqsPvynbPpdwQb0GCYf0Ul4uWBZZ4Afq9qpxVeZkaccmXEmsg11OsY_BJVs2DETdM53WoxfCabNvvlFoyGdc1Si9fZPvp6Qwxv4sFxFpyU48HDPm-jFOYKoJ8k-3BWphX7r_him5e2Qpm-hF2CBfc2hTwqRjANAF30psma3xH4HiPd8qdEGvQKdn1A9Heze-KTMQZ00t4He6hvA-y6p9vWyK18-CUchBYNAAiHZkNzs_gKamwEoqCpSk5_jvX_5O1QVzAvg1gSuM1-3W-gNZSA6wdQofIZfCJb5AhcG2-jCFvbSMev0lgm1DpqbY-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احسان حسینی، خبرنگار حوزه انرژی: اصلا بنزینی نیست که بتوانیم وارد کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/141739" target="_blank">📅 00:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141738">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38c6a0d4c.mp4?token=BSXWTt7u7wlgji48gZZ9O3bN_hQ9MR67pAHWvE3WuSaEE6O0X99rOMd7epumq31z6vCirSYWR9C91eyCMkgksDvJNeMzBX27NaUoch07oOjOoQ7dwcW6Af549dXXd0mCpZtpY3SZ6NZp7GsuRRKDaRHEJrG8LYfigMWva7H7ITX7XTJBawKCLLQZsvKQr7sbg6MTuHNd8cSyKQ_bx-1c_rOwzHDgS8Blu4cGwneXPLxfG_7bkJWlfOq8Rl2PhkPf9xffnWwgh70ouY_bUEIJWvfW4LpX6DZ7a9st1T9Gvm8sm1VPXw9kA7od7xHHjFy9VrZsR2g_eb-96W4oqPfJcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38c6a0d4c.mp4?token=BSXWTt7u7wlgji48gZZ9O3bN_hQ9MR67pAHWvE3WuSaEE6O0X99rOMd7epumq31z6vCirSYWR9C91eyCMkgksDvJNeMzBX27NaUoch07oOjOoQ7dwcW6Af549dXXd0mCpZtpY3SZ6NZp7GsuRRKDaRHEJrG8LYfigMWva7H7ITX7XTJBawKCLLQZsvKQr7sbg6MTuHNd8cSyKQ_bx-1c_rOwzHDgS8Blu4cGwneXPLxfG_7bkJWlfOq8Rl2PhkPf9xffnWwgh70ouY_bUEIJWvfW4LpX6DZ7a9st1T9Gvm8sm1VPXw9kA7od7xHHjFy9VrZsR2g_eb-96W4oqPfJcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : آمریکا بازگشته است، و بزرگ‌ترین پیروزی‌های ما هنوز در راه هستند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/141738" target="_blank">📅 00:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141737">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e572186d.mp4?token=PS_3bLpXGYYvIc2-jkr4_OIvFjIm971xZwHVkvel17KJpoyQNeVyQ_xuRTi-Wzl9efsLUDv0hIXiegmaiLgjAs0KPDxOdhv7k6FkRmWrQe-c8Vh3MA4FyGtY86uL_Eh61vkgzpn03CRxOos0eMTg03E8njd1YCxC3ucr7JDEIK9a6XaAsOlztXrXhUTwiB_y7hml1Gjz6zpLsDfnPHQYCFBkEolr3DarHsrGmwSa5cZAUdKhksz5TMOPtCl9e_e2EY0eZaUH--x2ApivGs8Jkk_yMWjdBRffRa9A63iSW5kPMWq-XhNaziJbHMn7jb731U4mng1GmPUMAnkWax3G2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e572186d.mp4?token=PS_3bLpXGYYvIc2-jkr4_OIvFjIm971xZwHVkvel17KJpoyQNeVyQ_xuRTi-Wzl9efsLUDv0hIXiegmaiLgjAs0KPDxOdhv7k6FkRmWrQe-c8Vh3MA4FyGtY86uL_Eh61vkgzpn03CRxOos0eMTg03E8njd1YCxC3ucr7JDEIK9a6XaAsOlztXrXhUTwiB_y7hml1Gjz6zpLsDfnPHQYCFBkEolr3DarHsrGmwSa5cZAUdKhksz5TMOPtCl9e_e2EY0eZaUH--x2ApivGs8Jkk_yMWjdBRffRa9A63iSW5kPMWq-XhNaziJbHMn7jb731U4mng1GmPUMAnkWax3G2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره ایران گفت: «یکی از مشکلات در ایران این است که کسی وجود ندارد که بتوان با او مذاکره کرد؛ این یک مشکل است.»
🔴
او در ادامه گفت: «ایران تنها کشور جهان است که در آن هیچ‌کس نمی‌خواهد رئیس‌جمهور شود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/141737" target="_blank">📅 00:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141736">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ترامپ: ایران ۲۱۲ هواپیما داشت؛ همه آن‌ها از بین رفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/141736" target="_blank">📅 00:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141735">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d715d521d6.mp4?token=MxM7et8q22wwwDhe8dbyRX0eEyWyrpb2TvHHgbLQz56GJKWyc36yubXPSlOpv1zEyAD-gWjKKXoSi4kgBa_YKDbiYMMCk3qkusV5yiUDwSwkfAM8IOtnKCGfDaPHodHFuthtY4Z0UlECU5td9VEMSB3RyUc9sU-lR40sjDUphgItOcL3o3lRShvJxVDa61lJH2D9905VGLkWKIAbl0rZsJgd17U0Zv1hJjRwol6jVQbiMeWflDgglRO8tByDji4OC1SuMvYGWFSWjR4nYXvEgIA1YVC6Diu1IN6LdvYGAUHtqFJ_4bpjO8hgwcw8EsmL_VHap2wvUtV-YnlLwIaCRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d715d521d6.mp4?token=MxM7et8q22wwwDhe8dbyRX0eEyWyrpb2TvHHgbLQz56GJKWyc36yubXPSlOpv1zEyAD-gWjKKXoSi4kgBa_YKDbiYMMCk3qkusV5yiUDwSwkfAM8IOtnKCGfDaPHodHFuthtY4Z0UlECU5td9VEMSB3RyUc9sU-lR40sjDUphgItOcL3o3lRShvJxVDa61lJH2D9905VGLkWKIAbl0rZsJgd17U0Zv1hJjRwol6jVQbiMeWflDgglRO8tByDji4OC1SuMvYGWFSWjR4nYXvEgIA1YVC6Diu1IN6LdvYGAUHtqFJ_4bpjO8hgwcw8EsmL_VHap2wvUtV-YnlLwIaCRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: هیچ‌کس نمی‌داند چقدر در ایران موفق بوده‌ایم؛ خود ایران می‌داند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/141735" target="_blank">📅 23:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141734">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ : وقتی کشورها به کمک نیاز دارن، با آمریکا تماس می‌گیرند
🔴
من همیشه بهشون کمک نمی‌کنم، چون بعضی وقت‌ها رفتار خوبی با ما نداشتند
🔴
البته ناتو هم همیشه کنار ما نبوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/141734" target="_blank">📅 23:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141733">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8265299e.mp4?token=PVmIZEMT4FHLkztehfttypcqwRpqMXnzC8r9wJymgRFWFMXDtgRPI939h313zUmRtGcqEOzgMv_N-2SDUC_9rJEP4YlW_n0mrq5z0bzdgTWRwFIcuNafWYrF8_nFPw03DNtqtdF_EQEXJLlUH8PVSfwhbW_qAIEj8_nRp4ekElzl6AIfqLzRimwBJJgkSuXIDGc7vgGhqxgNRhw_BHN6-6LvSqAKsFelKxcGxjpZKNEy8OfD9L-ROiu7WR287gJVuUoJ5TDfdz0LODEI06vW0AAEfD87TrQ95aRkJgyHHz6P0rJAVIqALXFRFvpBCs5Q3QUJoK00HWIX6qijc-jDBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8265299e.mp4?token=PVmIZEMT4FHLkztehfttypcqwRpqMXnzC8r9wJymgRFWFMXDtgRPI939h313zUmRtGcqEOzgMv_N-2SDUC_9rJEP4YlW_n0mrq5z0bzdgTWRwFIcuNafWYrF8_nFPw03DNtqtdF_EQEXJLlUH8PVSfwhbW_qAIEj8_nRp4ekElzl6AIfqLzRimwBJJgkSuXIDGc7vgGhqxgNRhw_BHN6-6LvSqAKsFelKxcGxjpZKNEy8OfD9L-ROiu7WR287gJVuUoJ5TDfdz0LODEI06vW0AAEfD87TrQ95aRkJgyHHz6P0rJAVIqALXFRFvpBCs5Q3QUJoK00HWIX6qijc-jDBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد درگیری قبلی با ونزوئلا:
«ونزوئلا یک جنگ یک روزه بود. و اکنون ما با آن‌ها عالی کار می‌کنیم. ما میلیون‌ها و میلیون‌ها بشکه نفت گرفته‌ایم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/141733" target="_blank">📅 23:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141732">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
بر اساس گزارش نشریه پولیتیکو، به نقل از یک مقام کاخ سفید؛ هنوز هیچ تمدید قریب‌الوقوعی برای آتش‌بس بین آمریکا و ایران وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/141732" target="_blank">📅 23:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141731">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ
:
چاک شومر کاملاً فلسطینی شده
🔴
دنبال لباس فلسطینی می‌گردم که براش بفرستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/141731" target="_blank">📅 23:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141730">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ: اقدامات ما در قبال ایران خدمت بزرگی به جهان است
🔴
دونالد ترامپ درباره اقدامات آمریکا در قبال ایران گفت: «کاری که ما انجام می‌دهیم، خدمت بزرگی به جهان است؛ نه فقط به خودمان، بلکه به تمام جهان.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/141730" target="_blank">📅 23:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141729">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
ترامپ درباره ایران: «وقتی مجبور می‌شوید کمی بیشتر برای بنزین‌تان پول بپردازید، من هرگز عذرخواهی نخواهم کرد. من کار درست را انجام دادم.
🔴
[ایران] نباید سلاح هسته‌ای داشته باشد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/141729" target="_blank">📅 23:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141728">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
فوری / ترامپ: در صورت هرگونه حمله از سوی ایران، با قدرتی صد برابر بیشتر پاسخ خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/141728" target="_blank">📅 23:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141727">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
پزشکیان: گرونیا طبیعیه، درآمد نداریم، نفت هم نمیتونیم بفروشیم.
🔴
اما عرزشی معتقده پیروزه جنگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/141727" target="_blank">📅 23:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141726">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/907acfd306.mp4?token=J3xizQ4ihPtbGkOFTRYx6h09-IMZBf-Yy3MMHLk43rc33kWZJk6rg6BI0wbSUs4ByYmKuh0PmFScWd5qKTpaxs2o_HBJ0eme8tg5UGQra4-Bl7IoOaYRjH-Ytb9U7AnlclCVuvrmxHFwp72e7gZwj7jjhqQOnWpydlyKPnqvcitUTVc1ci37Jllf-cnQjCXF3X7MWUQTwj5nG1pQxADpDnRcWHcyxNPVdx2652m1zm5XSXcQJdw085C3Jw6athKgtkjKs2K0O0LqeVgSBsZaYG4ugFW79-MwopbYsLdWiTLktTyXHnYUwiQlmEePKDfZ4_jWj6T_vsxHf8HFg1XnpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/907acfd306.mp4?token=J3xizQ4ihPtbGkOFTRYx6h09-IMZBf-Yy3MMHLk43rc33kWZJk6rg6BI0wbSUs4ByYmKuh0PmFScWd5qKTpaxs2o_HBJ0eme8tg5UGQra4-Bl7IoOaYRjH-Ytb9U7AnlclCVuvrmxHFwp72e7gZwj7jjhqQOnWpydlyKPnqvcitUTVc1ci37Jllf-cnQjCXF3X7MWUQTwj5nG1pQxADpDnRcWHcyxNPVdx2652m1zm5XSXcQJdw085C3Jw6athKgtkjKs2K0O0LqeVgSBsZaYG4ugFW79-MwopbYsLdWiTLktTyXHnYUwiQlmEePKDfZ4_jWj6T_vsxHf8HFg1XnpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما ۱۹.۲ تریلیون دلار برای سرمایه‌گذاری در کشورمان داریم. می‌دانید دلیلش چیست؟ تعرفه‌ها.
🔴
ما با تعرفه‌ها، ثروت زیادی به دست می‌آوریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/141726" target="_blank">📅 23:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141725">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ترامپ: به زودی تنگه هرمز را قلمرو آمریکا اعلام خواهم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/141725" target="_blank">📅 23:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141724">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ae2e03e6b.mp4?token=CvyK8uksxa4G7YYfVxfPFKmrUJ3vFQzg3uVQ4SsdICwcUuljzMJib6xummw-v4KDtB3E4LF_2Jiuln-eCdL9cDGFTLyUJnLwrP7RnoLax4KWwmpFGWX5-VPZVwAXNzCa-kMjThQkjjGqtH2plIHFHPaT6BTYjeaAtaeUwUjM4RAopOYo0_WeuHU0kqTu8LuEzSXlx2uXplmRYfzPZ4bekrw5WMTsQdx5iLb8_4_-GgLbVjy2ihCZ81M6umOeqOiHBKmBwQPCur3GXWOXXhNf-DECHbdby3lyPGx-Aa08pDnqqdQ6LDUbqffG_xFpC0lO6FD_njDwh2dFN8D-zYNFhkvVKluyC9JRg3XW0SsNPMN585sABHWosg2SQ0pcykLKUoY0YdRRi87ZQOFTXmPJrZBWSrAveeqzEnjfGoaZmYdBOsals-XHrPgvg4f_UL_LLdxkWX955HZ5IkjaIxwGj-d1HmP6xfy5DFNT6bHfjrJ6oIjmDkW-0_5kVqhXLjr_i8T-JtMhh8hQLDt2DSD8ekELgkbRCLB0ZN0zM4yTPorOJOgJyiq4auVto_LRJERMFtb_JugenJ1LkK-DsrHEsa4g9C6sfOTQppebby13V1bRUiIeMYcAxbJzKG5R82qpnmMFMMO5vMleWZsteASvtaYGVFuDqcGD7Ccn3R2RsjU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ae2e03e6b.mp4?token=CvyK8uksxa4G7YYfVxfPFKmrUJ3vFQzg3uVQ4SsdICwcUuljzMJib6xummw-v4KDtB3E4LF_2Jiuln-eCdL9cDGFTLyUJnLwrP7RnoLax4KWwmpFGWX5-VPZVwAXNzCa-kMjThQkjjGqtH2plIHFHPaT6BTYjeaAtaeUwUjM4RAopOYo0_WeuHU0kqTu8LuEzSXlx2uXplmRYfzPZ4bekrw5WMTsQdx5iLb8_4_-GgLbVjy2ihCZ81M6umOeqOiHBKmBwQPCur3GXWOXXhNf-DECHbdby3lyPGx-Aa08pDnqqdQ6LDUbqffG_xFpC0lO6FD_njDwh2dFN8D-zYNFhkvVKluyC9JRg3XW0SsNPMN585sABHWosg2SQ0pcykLKUoY0YdRRi87ZQOFTXmPJrZBWSrAveeqzEnjfGoaZmYdBOsals-XHrPgvg4f_UL_LLdxkWX955HZ5IkjaIxwGj-d1HmP6xfy5DFNT6bHfjrJ6oIjmDkW-0_5kVqhXLjr_i8T-JtMhh8hQLDt2DSD8ekELgkbRCLB0ZN0zM4yTPorOJOgJyiq4auVto_LRJERMFtb_JugenJ1LkK-DsrHEsa4g9C6sfOTQppebby13V1bRUiIeMYcAxbJzKG5R82qpnmMFMMO5vMleWZsteASvtaYGVFuDqcGD7Ccn3R2RsjU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور: در عرض ۲.۵ سال، فردی انتخاب خواهد شد.
🔴
لطفاً یک چیز را به خاطر داشته باشید: ترامپ کسی بود که این کار را انجام داد.
🔴
این کارخانه‌ها همگی دوباره راه‌اندازی خواهند شد و آن‌ها خواهند گفت که چقدر باهوش هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/141724" target="_blank">📅 23:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141723">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e62055fa68.mp4?token=caOoagcbsDVCckmRFx7kXRxBtylonK-Eo_oOjDWa14x3feuo6B1uvihegiz1B0ve6d3YwBYTR9tPkaG_XvXI_4nQAHhyPFxKjxSiT1oaKOw_Tx3EqeTAhXKn0Oiox3ABo1lmIsj0gjT9-VryfIVUxzgkDmFzdhRevZDFAX6hozmdTuHKX8e6aqv0p7AxtBezaxZ5JZIrQXZdFR_vej1fmuxLEbTqeuwBtD3n_t-MB8pA0H4aGb_A3AwXRNXFDPqXOB_Yel47WQbrD9Q0vZOc9--O0AMsFSoRE4mJ0-kRUyF3cXmI0VpG2sn0gx1Il7do945cl4boBzcg8ZZlIRF_Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e62055fa68.mp4?token=caOoagcbsDVCckmRFx7kXRxBtylonK-Eo_oOjDWa14x3feuo6B1uvihegiz1B0ve6d3YwBYTR9tPkaG_XvXI_4nQAHhyPFxKjxSiT1oaKOw_Tx3EqeTAhXKn0Oiox3ABo1lmIsj0gjT9-VryfIVUxzgkDmFzdhRevZDFAX6hozmdTuHKX8e6aqv0p7AxtBezaxZ5JZIrQXZdFR_vej1fmuxLEbTqeuwBtD3n_t-MB8pA0H4aGb_A3AwXRNXFDPqXOB_Yel47WQbrD9Q0vZOc9--O0AMsFSoRE4mJ0-kRUyF3cXmI0VpG2sn0gx1Il7do945cl4boBzcg8ZZlIRF_Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شوخی ترامپ: فکر می‌کنم باید دوباره کامالا هریس را نامزد کنند؛ او نامزد فوق‌العاده‌ای بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/141723" target="_blank">📅 23:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141722">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f438219c.mp4?token=JAynmoQPz8bLx2D2dzHsxJD95cWkAJHlJXdl2Dvj7ZE23ReTfIIJ7aOFCtq7T_Y17eqBH834ie9mCm40nkM50NARcBphg9_oBAfKySeqaLmnzPCGu5FTmUC0GMVKZ6XJfGaM_P2nxD4T7FLGcrAxv4oA-kI1F3OqTqrQ4YVps0G4AKMU-Gi_oorOvrc_zFMw2lcK03GfIifxyfJnItkA2piPnPuDMY2ErroTvJ-HpBC6T3in5D4naBuRrntAbUCjOWW2AFgQ8V8Oe5AOIeWjNv1ILCkJqeXyfWtvj-8lgkNMx1gk7R28VDs85XbqSRMRsYvQaPbwzQLZBj3cRWiUqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f438219c.mp4?token=JAynmoQPz8bLx2D2dzHsxJD95cWkAJHlJXdl2Dvj7ZE23ReTfIIJ7aOFCtq7T_Y17eqBH834ie9mCm40nkM50NARcBphg9_oBAfKySeqaLmnzPCGu5FTmUC0GMVKZ6XJfGaM_P2nxD4T7FLGcrAxv4oA-kI1F3OqTqrQ4YVps0G4AKMU-Gi_oorOvrc_zFMw2lcK03GfIifxyfJnItkA2piPnPuDMY2ErroTvJ-HpBC6T3in5D4naBuRrntAbUCjOWW2AFgQ8V8Oe5AOIeWjNv1ILCkJqeXyfWtvj-8lgkNMx1gk7R28VDs85XbqSRMRsYvQaPbwzQLZBj3cRWiUqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: دغدغۀ من معیشت مردم است و نمی‌توانم نسبت به آن بی‌تفاوت باشم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/141722" target="_blank">📅 23:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141721">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c2eb2723.mp4?token=WfHpcU1-hJPZpebJzWhM--CrOiRu7H-BKeqOBOOdQ3D-QKRRFW5ZW7rIx4Z4xp4NsegxdqwVwwJIUMOSaiNLbQuy3faACfv1_Wu67e-Pz77okGdopUYnG8bzRPF1rFSc1W0lMhF5TLzdFnDGf4th16q2c0JzSa91HiO_pgHOGdPUo_cxk9ZG8muPR2MejH7k_d7adWzlSFxsBXbUqVMyHJALaJIZ7WiAOaC330La5EOkOnArTbFNlKh6Y0-qydRPEEHd5ph5c3xG3a2tVCATjxy0NGZ25NB0-iGGvTV-nk8saqPD-5Vqtf35qXG8kH71kC38jOplzjvrD4K_oALztw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c2eb2723.mp4?token=WfHpcU1-hJPZpebJzWhM--CrOiRu7H-BKeqOBOOdQ3D-QKRRFW5ZW7rIx4Z4xp4NsegxdqwVwwJIUMOSaiNLbQuy3faACfv1_Wu67e-Pz77okGdopUYnG8bzRPF1rFSc1W0lMhF5TLzdFnDGf4th16q2c0JzSa91HiO_pgHOGdPUo_cxk9ZG8muPR2MejH7k_d7adWzlSFxsBXbUqVMyHJALaJIZ7WiAOaC330La5EOkOnArTbFNlKh6Y0-qydRPEEHd5ph5c3xG3a2tVCATjxy0NGZ25NB0-iGGvTV-nk8saqPD-5Vqtf35qXG8kH71kC38jOplzjvrD4K_oALztw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد نخواستن اینکه نیویورک به دلیل جرم ها سقوط کند: «ما اجازه نمی‌دهیم این اتفاق برای نیویورک، ایالت نیویورک بیفتد. و به همین دلیل است که باید بروس را به سمت بیاوریم.
باید او را آنجا بیاوریم. هیچ‌جا حمله کمونیستی به جامعه آمریکایی واضح‌تر از اینجا در ایالت نیویورک نیست.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/141721" target="_blank">📅 23:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141720">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ed040a20e.mp4?token=COdhxNeiFNV-6Ji-2qU_iXw12EGJSGSvGCVC3OQYXDkrx6M0eVvH9bKu0RQLd9skZSebF1pcQw0UjIxYd8VNCby2CLQif1M_zRqpXVo0utXitiaQXhIdLp_vDJ8U055M1rXUOSg5tM83ShbnCDCuav5J5RZYggkq9S7D4t_VZjH-jZMATwpLQEOrCYXuaRINH9OtZTYMmMLvnDVCYi5904mrVGqDQm6m_tU6ME7bJVpX69KKfoR1nwAXtEh9MteYfm8Qqv7VyU3YMSYqf2zoYGQkpl5lWy7cCoxboSzITrjTcLwo780E3jsRNfUxjDzOJ-CcxCvFwp4iHsEPHaVrzlCURb77DuvtFM_x1CO4Qq-Wwj1e7HC6D33tQJnal4XGjGAFArq8yHciXIa9Me52_pvn_W4tI-PUkGYmwUyY05FpL_u7upcdtIoziazlS_WLIgvEdJSvPXX_MpLQPEfEcqnkeUZodMOwcBs4shlZnGY5YpjlSLJgypSfEYgsBnF-RYfrorK9_KkY8mTnxjA0HKSgWi3dM-vKkpLjknZpdtbmpCUDukUj4E5Yz_JCgnRVWz0MGDmLuG7keI49sPYIzldJ5ZhYo0jr7-Px9X5N7O67Gud1rLiD_4JNHgObKtklKxDG-2RLvoWrMk4bMJtuGxMQX8m-5PRNBAQA6t_gjEk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ed040a20e.mp4?token=COdhxNeiFNV-6Ji-2qU_iXw12EGJSGSvGCVC3OQYXDkrx6M0eVvH9bKu0RQLd9skZSebF1pcQw0UjIxYd8VNCby2CLQif1M_zRqpXVo0utXitiaQXhIdLp_vDJ8U055M1rXUOSg5tM83ShbnCDCuav5J5RZYggkq9S7D4t_VZjH-jZMATwpLQEOrCYXuaRINH9OtZTYMmMLvnDVCYi5904mrVGqDQm6m_tU6ME7bJVpX69KKfoR1nwAXtEh9MteYfm8Qqv7VyU3YMSYqf2zoYGQkpl5lWy7cCoxboSzITrjTcLwo780E3jsRNfUxjDzOJ-CcxCvFwp4iHsEPHaVrzlCURb77DuvtFM_x1CO4Qq-Wwj1e7HC6D33tQJnal4XGjGAFArq8yHciXIa9Me52_pvn_W4tI-PUkGYmwUyY05FpL_u7upcdtIoziazlS_WLIgvEdJSvPXX_MpLQPEfEcqnkeUZodMOwcBs4shlZnGY5YpjlSLJgypSfEYgsBnF-RYfrorK9_KkY8mTnxjA0HKSgWi3dM-vKkpLjknZpdtbmpCUDukUj4E5Yz_JCgnRVWz0MGDmLuG7keI49sPYIzldJ5ZhYo0jr7-Px9X5N7O67Gud1rLiD_4JNHgObKtklKxDG-2RLvoWrMk4bMJtuGxMQX8m-5PRNBAQA6t_gjEk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ:
تا این هفته، نه نفر از ده نفر از لیست متهمان فراری اف‌بی‌آی دستگیر شده‌اند.
🔴
این یک رکورد تقریبی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/141720" target="_blank">📅 23:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141719">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a10222396.mp4?token=F1De4N-HZHc1-TB6__XQhJfKl7wBiHdObwp8Vi8GPQoNEmLpwwBniwY3cZ0mTnTPm3seM7w7Jxdt4NkjCFcCcRzbsqlh3_MUiq3Q7e1EvBEa7CzBzAbT9mqBktBg120l070T-MXfGqSRPziFnUAUL4wWdhfHzz9NggiquwbOu2hkCVPllNB1S9dVesBuYPVbfOqLCbfpWuzwRAT4UBlFG46odYsmfjEbgHU8qIOGKNCcgLgr68bOEttpNehdgGk-K_EBJJSLuN2wezqgdlGC-tklWbi32CXdTcJAWF0xbKVhUyHnF4PDZZbSw0g8MuhrdlIY_5QQEOTmqTOu7gRqNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a10222396.mp4?token=F1De4N-HZHc1-TB6__XQhJfKl7wBiHdObwp8Vi8GPQoNEmLpwwBniwY3cZ0mTnTPm3seM7w7Jxdt4NkjCFcCcRzbsqlh3_MUiq3Q7e1EvBEa7CzBzAbT9mqBktBg120l070T-MXfGqSRPziFnUAUL4wWdhfHzz9NggiquwbOu2hkCVPllNB1S9dVesBuYPVbfOqLCbfpWuzwRAT4UBlFG46odYsmfjEbgHU8qIOGKNCcgLgr68bOEttpNehdgGk-K_EBJJSLuN2wezqgdlGC-tklWbi32CXdTcJAWF0xbKVhUyHnF4PDZZbSw0g8MuhrdlIY_5QQEOTmqTOu7gRqNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان
:
بارها گفتم و باز هم می‌گم؛ من هیچ‌وقت در برابر رهبر نمی‌ایستم
🔴
این حرف رو فقط برای شعار نمی‌زنم
🔴
چون برای من اتحاد از خیلی چیزهای دیگه مهم‌تره. اگه اتحاد از بین بره، قدرت هم فرو می‌ریزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/141719" target="_blank">📅 23:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141718">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ترامپ : ما نماینده کل جهان هستیم، هیچ کشوری مثل ایالات متحده وجود نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/141718" target="_blank">📅 23:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141717">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترامپ
:
کسی اینجا هست که طرفدار قطع بودجه پلیس باشه؟ اگه هم باشه، جرئت نمی‌کنه بگه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/141717" target="_blank">📅 23:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141716">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: ما یک ضربه اقتصادی قوی به ایران وارد خواهیم کرد و برایم مهم نیست که این قبل از انتخابات میان‌دوره‌ای باشد یا نه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/141716" target="_blank">📅 23:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141715">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ff8a9360.mp4?token=HerTz8zS-P0PCHmi_c5v6YAHDW9TJAE1aCf9an1t0nE_nSS0bvQVWKFn41pcrV1yA9pyO-ipZvf5uV9Nzoq80y28JunhMwvJEMudaNjbgJgIRlkrQp1RIklyTsc8kWH6rq-KXFoQvz176mOquJKpYDzGsPjlf_mEv19MEaTl4rwJPppX9VaC1SmNc2Jah8SQCIEQSMVLx18_XaYi_dRtCbu8crj4iygf-B09AfPR6b26XqsJ65lTLTAYyAGKw3xLjpDa-pzLNMTo4ueHlmQJnRUr6RzXwH-_ymf85OJmDYIEbZcxqlTl81-Cjscob7BIAtZm6HZzKSRxSdcQ_Vod6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ff8a9360.mp4?token=HerTz8zS-P0PCHmi_c5v6YAHDW9TJAE1aCf9an1t0nE_nSS0bvQVWKFn41pcrV1yA9pyO-ipZvf5uV9Nzoq80y28JunhMwvJEMudaNjbgJgIRlkrQp1RIklyTsc8kWH6rq-KXFoQvz176mOquJKpYDzGsPjlf_mEv19MEaTl4rwJPppX9VaC1SmNc2Jah8SQCIEQSMVLx18_XaYi_dRtCbu8crj4iygf-B09AfPR6b26XqsJ65lTLTAYyAGKw3xLjpDa-pzLNMTo4ueHlmQJnRUr6RzXwH-_ymf85OJmDYIEbZcxqlTl81-Cjscob7BIAtZm6HZzKSRxSdcQ_Vod6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، درباره وضعیت فعالیت‌های مجرمانه در ایالات متحده پیش از ریاست‌جمهوری خود: «و در چهار سال گذشته قبل از اینکه من کشور را ترک کنم، کشور ما توسط مجرمان خشونت‌پیشه غرق شده بود. منظورم این است که به یاد دارید چند سال پیش چقدر وضعیت بد بود؟ درست است؟ واقعاً بد بود. باند‌های خارجی، اراذل وحشی همراه با بایدن.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/141715" target="_blank">📅 23:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141714">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
حمله هوایی اسرائیل به المنصوری در جنوب لبنان انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/141714" target="_blank">📅 22:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141713">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
العربیه به نقل از یک منبع نظامی یمن: حوثی ها با ۴۴ پهپاد و ۶ قایق بمب گذاری شده، بندر المخا را مورد حمله قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/141713" target="_blank">📅 22:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141712">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
صحنه‌های ویدیویی شامگاه جمعه 23 مرداد حریق در بندر المخا یمن ناشی از حملات موشکی بالستیک شبه‌نظامی حوثی‌ به زیرساخت‌های این بندرگاه را نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/141712" target="_blank">📅 22:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141711">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوری /  آکسیوس: کاخ سفید بدون اطلاع نتانیاهو در حال برقراری ارتباط با اپوزیسیون اسرائیل است
🔴
آکسیوس به نقل از منابع آگاه گزارش داد، در بحبوحه کاهش محبوبیت نتانیاهو، دولت ترامپ برای جلوگیری از به خطر افتادن ابتکارات خاورمیانه‎ای خود، شروع به برقراری تماس‌های مخفیانه با رهبران اپوزیسیون اسرائیلی کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/141711" target="_blank">📅 22:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141710">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
در دومین حادثه ریلی از نوع خود ظرف شبانه‌روز گذشته در بریتانیا، جمعه 23 مرداد، یک قطار مسافربری در نزدیکی «ویکفورد» در «اسکس» از ریل خارج شد. روز قبل از آن بر اثر واژگون شدن قطار در «لویس» 20 نفر زخمی شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/141710" target="_blank">📅 22:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141709">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ds9u1-HE5SCjK1FOayCwHLuyYvBIO18TiZjVA7FA1swOw5fFnlC-u_RG-qweLJmEZ2Q_D5t5FVxzXlwUCykmWf6IGvhB59A-rmX_AUdd0gWAirc3miINsPwNOwhaSRGVn4LFcoXozZAqBwJArEl_cpSzPxVUBJfUJajif6r1Op9FVsPv8Wcn6j7M4nDgyKj5PFP4Dc-sQjB0fwkPQvTxgtVN4ejGeDAbhsLxxOoLsDxzKNtAbg3yz9VL5izI0032iaBy9jngqyx50tJSjkr9nX1Ua67532-t_gn4KdBc6054Ni1uEdJng9FSnITP3Hn_rXo0VGvftmwTE62CChfXCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با پول یه ماست پرچربِ امروز،
۱۰ سال پیش میشد خرج خورد و خوراک خونواده رو برای یه ماه داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/141709" target="_blank">📅 22:25 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
