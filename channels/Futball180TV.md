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
<img src="https://cdn5.telesco.pe/file/gw7Tg4_vfh-B8uR4AuNRTXYvezKa7no1Vc46KaIG3kxTHJeIMgmWahIZbJQrE2LrNyISWBvQM6L3bzJYkm6n-Xaka59Ah6VotXaLl0z2VBU2S52btaUi6Gk7ELruInhWbAHF3hv-N7Iy1ToqhNzs5Xqf5mdhPeHXMlBqZQbWOvXb88pRJbAVFR-2tZP6Wiq79WDm-0HP9q-iXl1u-QhDOn7XhS0b3u7GAe5_4jLy2yfjSx78G2NcEu8AbAFEM2HZG8aDrJ1h91plFZp8SbNw9g4u7qecxGpuwV94SOjZLUEZ4GwYf6AVOlFSlpQrUCAXJchwX_bv_v4LeHq6a7f9tw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 420K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 15:05:25</div>
<hr>

<div class="tg-post" id="msg-106119">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61ab051ddf.mp4?token=CCeGIBLbkZ0NAOvoufiwEV6HPaUXynGn1cm8JcvpM5WTxFb63jjz4XOZJx0xY8F-VbsVAxjWLWPN0T_OvwWX514xRT43HQf_GJ4ZygW7cgUTBYX4XvXC0nobzbWwyj8_Y7ImFUol1vjkJSrDZ4Hi2DNvKD5SVYRFiSXETRZ87T0PiSEbvf76sioConQMH-Qk0DAPblthIDB69V9JEEVra3Bx8DRBWuqR8gcsuJCEaCHW87gzqYMlgMZzilZ9DbTuF-BTP5Xgm0NAC9YAaOECCCL7D3kQXEPlqiluNhoXC98cjSOp22hxKBOU1RFsU78MZWmnHHI5nWXS6lHu80gfkR83sp21m2heTZKfUwJc2fih63lwAg8NCQ6HoJgHzvJnOFLE0zcBTzt_xmbu9ibJDjI2DvqrGoTHJrW4ECLkGzZZp1k8Y19S11keFxURl-Z-j-lo_5fYPbHLY_wNxxC5SFmD8BBBoYRkc15a-VOEuHqUeJGFkyJbICL5ymguMFumsW0tPL4QM2pxfniiExaWppOTBFJxKzKEYmpamRQmt92D_pB7uOKpXuk8uOi_BxSYE4lYNmsf-1W0c9YtXk6R6WC97WQsGcgdzDj6hfOM39VIyf5qZngfuGUWbCjIOS8xXXF2s0_wGbPJycY3Ph8v5a8gqMZGBX49BQmtzSAeER8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61ab051ddf.mp4?token=CCeGIBLbkZ0NAOvoufiwEV6HPaUXynGn1cm8JcvpM5WTxFb63jjz4XOZJx0xY8F-VbsVAxjWLWPN0T_OvwWX514xRT43HQf_GJ4ZygW7cgUTBYX4XvXC0nobzbWwyj8_Y7ImFUol1vjkJSrDZ4Hi2DNvKD5SVYRFiSXETRZ87T0PiSEbvf76sioConQMH-Qk0DAPblthIDB69V9JEEVra3Bx8DRBWuqR8gcsuJCEaCHW87gzqYMlgMZzilZ9DbTuF-BTP5Xgm0NAC9YAaOECCCL7D3kQXEPlqiluNhoXC98cjSOp22hxKBOU1RFsU78MZWmnHHI5nWXS6lHu80gfkR83sp21m2heTZKfUwJc2fih63lwAg8NCQ6HoJgHzvJnOFLE0zcBTzt_xmbu9ibJDjI2DvqrGoTHJrW4ECLkGzZZp1k8Y19S11keFxURl-Z-j-lo_5fYPbHLY_wNxxC5SFmD8BBBoYRkc15a-VOEuHqUeJGFkyJbICL5ymguMFumsW0tPL4QM2pxfniiExaWppOTBFJxKzKEYmpamRQmt92D_pB7uOKpXuk8uOi_BxSYE4lYNmsf-1W0c9YtXk6R6WC97WQsGcgdzDj6hfOM39VIyf5qZngfuGUWbCjIOS8xXXF2s0_wGbPJycY3Ph8v5a8gqMZGBX49BQmtzSAeER8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
پشت‌پرده جنجال‌های اخیر امید عالیشاه در تبریز؛ خصومتی که سال‌هاست ادامه دارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/Futball180TV/106119" target="_blank">📅 14:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106118">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcc99cf37e.mp4?token=T_kRMoW5lxJ5dGDei0hH0jbwr3hSYgXTYZPZgIR8tLJV52LVyJFv8Bpe5pMLdOzFBFWoxB_cyq4rtglElTxOEi-r7SwgQGg0-SvJI0wr-zR2t_GIV30SZwUskIcT_MWk4alimkNfmEEllcrciSPPAMPrkihF4tDQOGtuhKphA0fwSzKqQiWXn558IfLWRh54-ShIW9fMMVeyDr02PxRF5hzidHPQ3y2sFannTVQfre9ESOsWeypi0GUX0UbEHs2adJeR55GvjU2JOnOe3ppTHqAOol42qu0r0Kkl1fN2E2YNdtxafQOpd5AcR5Ff_OVIdTR9VUfwBfUCThLF1MRjYq-HYxcedaqRxBaPYucLYzOxruDrCIq5bMwJDJAI_m46bQ8bOW9Ls5mrgRLtwtvmYSZJzyDLfGlinPb1j2PPFMu6XPlX5Jg7mT9NcHYViTcl4GA0ckMsaOhraynYLdnTkor_DtUEbBOxF-EkZAE_15dRuCx52-JPSx_Ez3V67PocyBEq_JUXk7NOFsePsdnmZU5t6B_R33QafguROIkBokE3x_wnxLw1_uemmcR2qd3NOlThOq3UKqPZZNKfmCUb2oPnpJJU268BK2gV3lqfu3tTSoZ_4fWiYRkTitP7SFkXFzXhNgVZWyn88QdzqnSOiR94KlI6KSghefTVBolZ8Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcc99cf37e.mp4?token=T_kRMoW5lxJ5dGDei0hH0jbwr3hSYgXTYZPZgIR8tLJV52LVyJFv8Bpe5pMLdOzFBFWoxB_cyq4rtglElTxOEi-r7SwgQGg0-SvJI0wr-zR2t_GIV30SZwUskIcT_MWk4alimkNfmEEllcrciSPPAMPrkihF4tDQOGtuhKphA0fwSzKqQiWXn558IfLWRh54-ShIW9fMMVeyDr02PxRF5hzidHPQ3y2sFannTVQfre9ESOsWeypi0GUX0UbEHs2adJeR55GvjU2JOnOe3ppTHqAOol42qu0r0Kkl1fN2E2YNdtxafQOpd5AcR5Ff_OVIdTR9VUfwBfUCThLF1MRjYq-HYxcedaqRxBaPYucLYzOxruDrCIq5bMwJDJAI_m46bQ8bOW9Ls5mrgRLtwtvmYSZJzyDLfGlinPb1j2PPFMu6XPlX5Jg7mT9NcHYViTcl4GA0ckMsaOhraynYLdnTkor_DtUEbBOxF-EkZAE_15dRuCx52-JPSx_Ez3V67PocyBEq_JUXk7NOFsePsdnmZU5t6B_R33QafguROIkBokE3x_wnxLw1_uemmcR2qd3NOlThOq3UKqPZZNKfmCUb2oPnpJJU268BK2gV3lqfu3tTSoZ_4fWiYRkTitP7SFkXFzXhNgVZWyn88QdzqnSOiR94KlI6KSghefTVBolZ8Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✅
🍏
توضیحات بسیار کاربردی برای آشنایی با آپشن‌های سه‌مدل جدید آیفون 18
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/Futball180TV/106118" target="_blank">📅 14:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106117">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f226d46bbd.mp4?token=gp56subNeCnTlMdD1IuEIpudpmqylmpRXpzkSyBwiN3tghx-yW5JR7xY4TzBJI6gFp2q6OWoXmYBM7U21h0Ky66HGLU36KywZxYM-hsThTRVAe_EjuqU7RoaO2VDUGh3pdarhidhHEzukBYopXZhV52rvSLX53EyLwYktze17i-z55GYhOBTgVAMAfh1eOwfmW9MYo_7O8X1isKQQnh7OcumGUuGLjlbnwi0ADIbPvTeoThvF3Nnomg3t0giIhb_VF5WJvn3nEC4INcNoh7FDUvVqwVqv1uMZHJJdo2Kokh1CrfmYGJeOEAOcasZJunnxsesiGW2ORfysPQ6KGgfSYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f226d46bbd.mp4?token=gp56subNeCnTlMdD1IuEIpudpmqylmpRXpzkSyBwiN3tghx-yW5JR7xY4TzBJI6gFp2q6OWoXmYBM7U21h0Ky66HGLU36KywZxYM-hsThTRVAe_EjuqU7RoaO2VDUGh3pdarhidhHEzukBYopXZhV52rvSLX53EyLwYktze17i-z55GYhOBTgVAMAfh1eOwfmW9MYo_7O8X1isKQQnh7OcumGUuGLjlbnwi0ADIbPvTeoThvF3Nnomg3t0giIhb_VF5WJvn3nEC4INcNoh7FDUvVqwVqv1uMZHJJdo2Kokh1CrfmYGJeOEAOcasZJunnxsesiGW2ORfysPQ6KGgfSYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
تشویق وایکینگ‌ها در قلب قزوین :))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/Futball180TV/106117" target="_blank">📅 14:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106116">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faf79d5ef7.mp4?token=SUMWtA1jZ2EbSbkTxEeICrA7OIGUvayIue6TlObRksZwBJiWDlqso2PXc8HVj-UkGljHO-KsBAFm8o04WU63hbcxiSvKxSVSyfyxLQ9w0m8JBXR3VIsyXPyKvanrpSQpk2RxXv8HXtrPdTY7XNLcGONQIVp0nbrUzx-J9TPMauojKiIaEVSim5KBNX6xWT7KYE3xl7A2PX3FlS5MXAPbOJpuDx7I2GJcZrQy7OrVFJ8WJYN_dq-OCprsGhXmP3SiCTAnBgmFapFr8ES-ANmmc_vHT88F_2d-KLDUl6y8Nb7g35hLnN3OOD7uj1y--Wes-rX3SNJYMrLJuVvz1SHMOHcPXAvHHH9tV_Mdq3gOzx6eGi0hQD83Rhc6Nw03Dx9_HzpX00n-acOlWH8VJxUf1gluEWCK4K1e9_o4NHnjFk55Jh4QnozUDFLuvRZSdiWGDAhZNSpTJdxmq18TaFn9JHuzky_9sNrx--EJoQ2z9dsk9QvJD1thL-ASD6lk2TkuTbB7VQC86oR6po5huYrcfjJh9VyRz6BDa7yyOkM-hGPduudNChQP98qh2-0hwGoxm2AmS10sHtssFuoN816MuLsciksPcf5-nMJIbQRhCocgEpdPKlwZOLkQO0nnLapIDorZ9QA-2zeeZ0AJlgt7hG8ydU0vli3ij4nwDNFGdgc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faf79d5ef7.mp4?token=SUMWtA1jZ2EbSbkTxEeICrA7OIGUvayIue6TlObRksZwBJiWDlqso2PXc8HVj-UkGljHO-KsBAFm8o04WU63hbcxiSvKxSVSyfyxLQ9w0m8JBXR3VIsyXPyKvanrpSQpk2RxXv8HXtrPdTY7XNLcGONQIVp0nbrUzx-J9TPMauojKiIaEVSim5KBNX6xWT7KYE3xl7A2PX3FlS5MXAPbOJpuDx7I2GJcZrQy7OrVFJ8WJYN_dq-OCprsGhXmP3SiCTAnBgmFapFr8ES-ANmmc_vHT88F_2d-KLDUl6y8Nb7g35hLnN3OOD7uj1y--Wes-rX3SNJYMrLJuVvz1SHMOHcPXAvHHH9tV_Mdq3gOzx6eGi0hQD83Rhc6Nw03Dx9_HzpX00n-acOlWH8VJxUf1gluEWCK4K1e9_o4NHnjFk55Jh4QnozUDFLuvRZSdiWGDAhZNSpTJdxmq18TaFn9JHuzky_9sNrx--EJoQ2z9dsk9QvJD1thL-ASD6lk2TkuTbB7VQC86oR6po5huYrcfjJh9VyRz6BDa7yyOkM-hGPduudNChQP98qh2-0hwGoxm2AmS10sHtssFuoN816MuLsciksPcf5-nMJIbQRhCocgEpdPKlwZOLkQO0nnLapIDorZ9QA-2zeeZ0AJlgt7hG8ydU0vli3ij4nwDNFGdgc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
قدرت نمایی رئیس جمهوری مغولستان با وزنه!
رئیس جمهوری ۵۸ ساله مغولستان، هنگام بازدید از یک واحد نظامی، ۱۰۰ کیلوگرم وزنه را به مدت ۲۰ تکرار پرس سینه زد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/Futball180TV/106116" target="_blank">📅 13:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106115">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaea95c3de.mp4?token=c3BZQI39-3dl3gkXv9odradvXTNYln3VRf28H83bA9pqh1Lw2r5gSYb5xw_RwqdyO6n3ei22IV0IpkGS5A1AubPD3yfguEYes7u9ULtPMJIxv4ReVrXHCVYiS0XW3z5NZyMxoQIigiPG-q36HjTkpZnX3WcF_b3_nZN4O58nl49KNMm_tKJvHlNA0jaTCvuCfIvK_Fde_OcgP0BYE-IOD9lUqXUEn5tzoSqt3b2u-24Smg3GIjHquWz2yJ3aUwSKmk_S9WICAp7GRYGH7duZ2o-LTUV2Gpt3Hpf8hfTXAiqGH6iGDMuhEEvCHYGajhb0fLDyE4mAoDB3jhwm9KRzug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaea95c3de.mp4?token=c3BZQI39-3dl3gkXv9odradvXTNYln3VRf28H83bA9pqh1Lw2r5gSYb5xw_RwqdyO6n3ei22IV0IpkGS5A1AubPD3yfguEYes7u9ULtPMJIxv4ReVrXHCVYiS0XW3z5NZyMxoQIigiPG-q36HjTkpZnX3WcF_b3_nZN4O58nl49KNMm_tKJvHlNA0jaTCvuCfIvK_Fde_OcgP0BYE-IOD9lUqXUEn5tzoSqt3b2u-24Smg3GIjHquWz2yJ3aUwSKmk_S9WICAp7GRYGH7duZ2o-LTUV2Gpt3Hpf8hfTXAiqGH6iGDMuhEEvCHYGajhb0fLDyE4mAoDB3jhwm9KRzug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد ایوب‌بوعدی در نخستین بازی سیتیزن‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/Futball180TV/106115" target="_blank">📅 13:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106114">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
✅
🇮🇷
بیانیه باشگاه پرسپولیس: از سوی باشگاه ما هیچ درخواستی برای لغو بازی با خیبر خرم‌آباد وجود نداشته و آمادگی لازم برای تقابل با این تیم در روز یکشنبه را داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/Futball180TV/106114" target="_blank">📅 13:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106113">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da7a59d4f1.mp4?token=kla2MvKD-MkLdUvXTaA67RYqomVfyrVuis_rGVRw13JYW1mdPJETrUkS7YviAvxHhXxpEiQ-RD_-1b7eWwB8pnddlg-b2QhYIs5VHh6KtsmUAJG7msYXFCi77E_f3WEZ_EgJ3rMXZtksoQoSj6qkXjFQRdbQJ-b-SZbXdpsT9BFXP-qh7v3QSE-clktghh_S7O1DVyxh_Lj7879LdmYXOV9naAXgz_PhZFX9smS5yuitEMdZPedRaimRqu7bkGrcCNgUV8i86XvuJOp4PHHI7dtHjS72MtWXslgwlmRwInks9r71jZr-PaWBK3oymcaHDPmqm98o7USd0sXps-8d2HBLcWgzBDJIQFukvHVqWfZ6KdXD6B8NrFuxHPzdpRN-uWPNVnZjCqwDrJpZySiSX2_y63wsW8vBjNbPSRvfIE_50yjvqkLhbFkSWs_NbrZj8XsosXQZJ35P0C35YxJa1j1inO4fcshNY0hxAuaMJZv6Z4fMmsKooYvxCMxIG6xqcpYM14lWuHSIkVtTHpkSRfvE3M3QoGH4tLpwcmC-vY4Mrc31D8Frv_Hzn28tlsfXhCY2vk4A7nFmM2PMhaqEUIAEL1hfbQpyijg3UisWvgVV-mTlQXGpwhrBWe5MZZDQq7w1_Pk6s_ZkqDAA1CESt-1oD1TtJmuGAqH8PGGNqa4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da7a59d4f1.mp4?token=kla2MvKD-MkLdUvXTaA67RYqomVfyrVuis_rGVRw13JYW1mdPJETrUkS7YviAvxHhXxpEiQ-RD_-1b7eWwB8pnddlg-b2QhYIs5VHh6KtsmUAJG7msYXFCi77E_f3WEZ_EgJ3rMXZtksoQoSj6qkXjFQRdbQJ-b-SZbXdpsT9BFXP-qh7v3QSE-clktghh_S7O1DVyxh_Lj7879LdmYXOV9naAXgz_PhZFX9smS5yuitEMdZPedRaimRqu7bkGrcCNgUV8i86XvuJOp4PHHI7dtHjS72MtWXslgwlmRwInks9r71jZr-PaWBK3oymcaHDPmqm98o7USd0sXps-8d2HBLcWgzBDJIQFukvHVqWfZ6KdXD6B8NrFuxHPzdpRN-uWPNVnZjCqwDrJpZySiSX2_y63wsW8vBjNbPSRvfIE_50yjvqkLhbFkSWs_NbrZj8XsosXQZJ35P0C35YxJa1j1inO4fcshNY0hxAuaMJZv6Z4fMmsKooYvxCMxIG6xqcpYM14lWuHSIkVtTHpkSRfvE3M3QoGH4tLpwcmC-vY4Mrc31D8Frv_Hzn28tlsfXhCY2vk4A7nFmM2PMhaqEUIAEL1hfbQpyijg3UisWvgVV-mTlQXGpwhrBWe5MZZDQq7w1_Pk6s_ZkqDAA1CESt-1oD1TtJmuGAqH8PGGNqa4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
سرگیجه جذاب و سخت این‌فصل کارشناسان برای انتخاب مناسب‌ترین گزینه برای بردن توپ طلا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/Futball180TV/106113" target="_blank">📅 13:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106112">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
⭕️
🇮🇷
با توجه به حضور سه بازیکن پرسپولیس در اردوی تیم‌ملی امید، احتمالا دیدار سرخ‌پوشان مقابل خیبر خرم‌آباد لغو خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/Futball180TV/106112" target="_blank">📅 12:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106111">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkrUsS1qVoxGq3pg68fTDrmyUng3qYTs0gI7OcOS9trQJB1vrvmF29zl9n0fcA294wb6OkL9-t4ogRXIO_6h6U282qPfyhG7duDRZdLkSNg89T31YycCROFaoqM1uY432B3awd2SQNIRAIYS9lXe9kCqN6tlB6x5M2KQTneKj0VWQ3-Wbn07LiaktK786tq7U0aUnKPjiqYCvZfZSXMyQWfuS7l-GGFqobvfuKUQ-TvfiWqi3k3RlC3Q1IHgYfrUUCZCd7zVGJOyF4TFDYi_29foeVVeKMzoK-ttvn4wt4I8DQJxFQYosKOvGCLEoW_DIyNWbMhE1FkZognn6-vX7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⁉️
با پول پژو ۲۰۷ در ایران در کشورهای مختلف چه ماشینی میشه خرید؟
🇦🇪
امارات: لکسوس ۲۰۱۶ تا ۲۰۱۸
🇩🇪
آلمان: بی ام و سری ۳- ۲۰۱۵ تا ۲۰۱۷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/106111" target="_blank">📅 12:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106110">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
‼️
⚔️
کل‌کل و دعوای دیشب رودریگو دی پائول با روبرت لواندوفسکی در لیگ‌آمریکا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/106110" target="_blank">📅 12:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106109">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72b9052ac6.mp4?token=ZRP_A7Q7jp8MzRA3DJAUENduaO9qRoESCCmm3cdaKs7idx7dflzDg0iqsimMbBz2gEWO3AcsRvUo_3_3duQbIKA5CE2pUZrqpRGVFVKHNGoHFUhpdcs_cxmBnBsdHrusTgHtNfjDsomc28noCP9OVhY1m-803McgDT4cVU7ELa38kOkZo2zlia1gnv9iZPkyXfx-WY5GMG-voc5Baj_9XW9PyMT67sHhkUb5ttT9TpkCZ-g7c87887MAKpICxR75JTWL1pOlebA5UYBLl66Jv2bjnGymiB0Oc2pSAHhzkHEkMzDDvh2y_Bk1NXra4PCFJpPpDruOO-Zd2eyKLYDYcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72b9052ac6.mp4?token=ZRP_A7Q7jp8MzRA3DJAUENduaO9qRoESCCmm3cdaKs7idx7dflzDg0iqsimMbBz2gEWO3AcsRvUo_3_3duQbIKA5CE2pUZrqpRGVFVKHNGoHFUhpdcs_cxmBnBsdHrusTgHtNfjDsomc28noCP9OVhY1m-803McgDT4cVU7ELa38kOkZo2zlia1gnv9iZPkyXfx-WY5GMG-voc5Baj_9XW9PyMT67sHhkUb5ttT9TpkCZ-g7c87887MAKpICxR75JTWL1pOlebA5UYBLl66Jv2bjnGymiB0Oc2pSAHhzkHEkMzDDvh2y_Bk1NXra4PCFJpPpDruOO-Zd2eyKLYDYcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
کنایه‌سنگین مهدی مهدوی‌کیا ستاره سابق ایران در مصاحبه جدیدش به عادل فردوسی‌پور
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/106109" target="_blank">📅 11:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106108">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff5f3cdb2.mp4?token=lmzHot7iuUDCZp9sT_2J9i098y1dzwzWzv2WC_VpipvNLS8vYrqoN7cT6A3MAaM5WfuksZiU8c21xGJ6M7xq8arUUK4Nl5VBg8K6i1Y0o6Kmxg124ihLJVgMtGwR9H7f97yLSut2WeVbMlAPuY6bWjZG6OBwTKIAh7VaZJEzx2Jm89q4pt-0IUgFJ0pZDwqCb488wsR3XF4jeJc2SDKzyJJ5EB-zyuEjqN7NQf6sfSFbR5FqIQlHJGLW1piSofT_-6rgA-ZCasqyC1zSb_3rwjXJ6BBFH8lKGghWQXEywXXD8yzf2MGTjpj3U-p3g9PzQY7bRMrqov776eAaFDlZjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff5f3cdb2.mp4?token=lmzHot7iuUDCZp9sT_2J9i098y1dzwzWzv2WC_VpipvNLS8vYrqoN7cT6A3MAaM5WfuksZiU8c21xGJ6M7xq8arUUK4Nl5VBg8K6i1Y0o6Kmxg124ihLJVgMtGwR9H7f97yLSut2WeVbMlAPuY6bWjZG6OBwTKIAh7VaZJEzx2Jm89q4pt-0IUgFJ0pZDwqCb488wsR3XF4jeJc2SDKzyJJ5EB-zyuEjqN7NQf6sfSFbR5FqIQlHJGLW1piSofT_-6rgA-ZCasqyC1zSb_3rwjXJ6BBFH8lKGghWQXEywXXD8yzf2MGTjpj3U-p3g9PzQY7bRMrqov776eAaFDlZjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
لواندوفسکی بعد جدا شدن از بارسلونا تو لیگ آمریکا هم هربازی داره گل‌میزنه و چه گلایی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/106108" target="_blank">📅 11:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106107">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c9d287e7a.mp4?token=VbbmeUpa-nTqiKAJwSxMLo2vxqgePTPe5igjYukKcrkLSAECOK_j6oO3RBiiFAM2e5pTy-TMmwK2TEQZRP5lV2MnwFGRib7uDZ_tY4Glc9myNU_5NOdunjgprdCZX-D1g5dgBjQZ1b40WJjs1g0VaXtZOKqYFnwp6nRplhzf834ZDMl503sIVe9qlNRTTHA-wg9y3Yf6YQDau8RGwAtHYxRS1MXR5OduTU3alksnvRv8CENxsSeY3kypgOsaSiHBKhnOshO3yEgqcIRRSkXZNugKFPTWJRpUZS7WahKnygrjfuP8NsiA9iZF6da7vKdWZKzdfSmKuAGsYaDVRMRotQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c9d287e7a.mp4?token=VbbmeUpa-nTqiKAJwSxMLo2vxqgePTPe5igjYukKcrkLSAECOK_j6oO3RBiiFAM2e5pTy-TMmwK2TEQZRP5lV2MnwFGRib7uDZ_tY4Glc9myNU_5NOdunjgprdCZX-D1g5dgBjQZ1b40WJjs1g0VaXtZOKqYFnwp6nRplhzf834ZDMl503sIVe9qlNRTTHA-wg9y3Yf6YQDau8RGwAtHYxRS1MXR5OduTU3alksnvRv8CENxsSeY3kypgOsaSiHBKhnOshO3yEgqcIRRSkXZNugKFPTWJRpUZS7WahKnygrjfuP8NsiA9iZF6da7vKdWZKzdfSmKuAGsYaDVRMRotQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
شفاف‌سازی عادل فردوسی‌پور از ویدیو جنجالی که به بوسیدن دست وزیر مرتبط بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/106107" target="_blank">📅 11:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106106">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106106" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/106106" target="_blank">📅 11:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106105">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJwU3YDSARQlmj6hS6mvRTmuj48sFrM51VpBlCDjHNNLCCYtjE-jwmdHTgVr0x3URCh1RtvHJ-EUrEoVxl1EG6H14rYOBIao7ep6I-8iOAzP2wyCWh77PthbOgzA2Aebf7VpsoSqS7QMhdYmIMF8p3ireAypBZVXE39Fg9rGfggeuGdL8Rxf9mfv8IlJYkvq00QhSRSxeVG5M0NWpzb7E_8mPaJNS0KYgOYdVd1Ld7n7j0NP-DzpHcNZlypIQRsaroXu6Hp1mFZGWPGewAOsCAEKoTiCxgqdkVEnPd_4v9uTq_ugLUKL3lv6IDtQfoTdz5ef65XEJO_IkY3SBSes9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پیکان
🆚
استقلال
⚽️
رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم
در ۵ بازی اخیر :
⚽️
پیکان : ۲ برد، ۲ تساوی، ۱ شکست
⚽️
استقلال : ۲ برد، ۳ تساوی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/106105" target="_blank">📅 11:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106104">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evVjjYFYtZ_sx5jZv4i1tEkKCPG2_7wualG-CiPAJmJg-6e0AcF5SJ21FyhPcswEYqgWfX6wOSQ2-EC93Kv0lTQ71WDsGHt3-AtWG-J714nQgAj3iTQkSgJT3Bx9fuQ0ndQawkQ3DWsdtJTbFGk2O3FES1RmnNyhoKSMmxr4z3fsOIQr3hTA_9Pso8AaL-DgIPUMKS4K4FB1q5hjhgWG0q7GAYcYRgTA0jyqUIuZnmyRhGu3iWMgOsQieWeRER_OeUUcEJP2NKt_Yr5YqDeQf-KaKnGlXqbEKQ2UP3nOvsn2NhkqQrihOlaV6N9KbdvMrpOp8veTVv3JF7qLGl-Vcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
تیم‌منتخب غایبان لیست توپ‌طلا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/106104" target="_blank">📅 11:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106103">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d1619d9ae.mp4?token=WQSrG3HZGHjMgrs7BcwTLTXbaL1H2YN3D1qJS3nNBNQ7aMYkdxT9IdKWzCaP36m8CJ2BhhFWFX9r9Qr8DKqV7qmUHEahz6upqmxEHUL9LCe4A1cPugWz3Gf3IEpJQp7vutjOqvysSdvukt75XUjy-mA9dzAa0_dM1_Y2GCOBDIna-x7WKIMnXMc_EhmX6bfyLafAzprO0RRMmWuf-WedXRRg6h4Izv8pN02daQrl3SlYhSnj96DM4yREFg3HSCRqwYU1CThNQ186XR71iX0V2ofwfdUnlopgWvY9WRqfxTH8S3_PKIlpxjG_Z9sqhvKPhztysPGL2BMnt37eXxFJWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d1619d9ae.mp4?token=WQSrG3HZGHjMgrs7BcwTLTXbaL1H2YN3D1qJS3nNBNQ7aMYkdxT9IdKWzCaP36m8CJ2BhhFWFX9r9Qr8DKqV7qmUHEahz6upqmxEHUL9LCe4A1cPugWz3Gf3IEpJQp7vutjOqvysSdvukt75XUjy-mA9dzAa0_dM1_Y2GCOBDIna-x7WKIMnXMc_EhmX6bfyLafAzprO0RRMmWuf-WedXRRg6h4Izv8pN02daQrl3SlYhSnj96DM4yREFg3HSCRqwYU1CThNQ186XR71iX0V2ofwfdUnlopgWvY9WRqfxTH8S3_PKIlpxjG_Z9sqhvKPhztysPGL2BMnt37eXxFJWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🤯
رکورد لیفت دنیا شکسته شد...
۵۱۱ کیلو رکورد از یک جوان ۲۰ ساله مکزیکی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/106103" target="_blank">📅 10:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106102">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef0e259b6.mp4?token=Rty7cTZ1fUx94NP6f9-lrKAA5nH0yPBrn2B0dWR46JuD_tC9NNX1jJisFEPVXuxTCNBgsIG_YCTrU3861ofoS4FQngN1cl-RUkdqAUcWQV59riWdbL3D874tGqIk0IEsc7ECPTXIYs4cK6EXvu9BhY7Os0x3freEX77Mep0TjdlXqfyaqeXxJVqgLfvXry6TzzXUCc-5m0FhQDqUVyQrs5CtToNh6Je1lIOxfWUKppKqLzTbNJNZNEfDBZATj9-2pfDi55X1WknDmivfSxrcG26-rIMhC9WaBTBoMqWltEc4fGKSsjmdPXYZDO4MO-sxlobSmlmzuddAMfxwTx1REA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef0e259b6.mp4?token=Rty7cTZ1fUx94NP6f9-lrKAA5nH0yPBrn2B0dWR46JuD_tC9NNX1jJisFEPVXuxTCNBgsIG_YCTrU3861ofoS4FQngN1cl-RUkdqAUcWQV59riWdbL3D874tGqIk0IEsc7ECPTXIYs4cK6EXvu9BhY7Os0x3freEX77Mep0TjdlXqfyaqeXxJVqgLfvXry6TzzXUCc-5m0FhQDqUVyQrs5CtToNh6Je1lIOxfWUKppKqLzTbNJNZNEfDBZATj9-2pfDi55X1WknDmivfSxrcG26-rIMhC9WaBTBoMqWltEc4fGKSsjmdPXYZDO4MO-sxlobSmlmzuddAMfxwTx1REA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔻
🎙
ماجرای ازدواج محمد پروین با آناهیتا درگاهی عمه دنیس‌درگاهی مهاجم تیم‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/106102" target="_blank">📅 10:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106101">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa9e4c6ba5.mp4?token=bb1twOLZjJwV0OSg_E901SqXgj-2xM2NgDOqrXsSBeMHXkwMlR8lJTHNwbMdudj_jcrbqXMp7PLEBD_jkJ39IpmQh3sWq4c9pq674yUrrAK597UyIesFuv8g1LVTMk4LRTdBDUxNm-gSh_0lH3b0mJUXwT65mJRsuN_MgHol8TaHSA6k3znLJ3rHfqcKczvkWAXsz2PD73Wa2KzjLo3_WL9My6fCQUXLlpc1rZQl0AC4DoipDzrk9ZycD60WlG9WsRkzPikmhRuEKY7cyJlRmw89Fck3TsnyFFPGVTJR3s3RDtD0tiVUoOZ0ZJkp5-ltj6Npix0ONZR7aI0ilWVm8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa9e4c6ba5.mp4?token=bb1twOLZjJwV0OSg_E901SqXgj-2xM2NgDOqrXsSBeMHXkwMlR8lJTHNwbMdudj_jcrbqXMp7PLEBD_jkJ39IpmQh3sWq4c9pq674yUrrAK597UyIesFuv8g1LVTMk4LRTdBDUxNm-gSh_0lH3b0mJUXwT65mJRsuN_MgHol8TaHSA6k3znLJ3rHfqcKczvkWAXsz2PD73Wa2KzjLo3_WL9My6fCQUXLlpc1rZQl0AC4DoipDzrk9ZycD60WlG9WsRkzPikmhRuEKY7cyJlRmw89Fck3TsnyFFPGVTJR3s3RDtD0tiVUoOZ0ZJkp5-ltj6Npix0ONZR7aI0ilWVm8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
▶️
ریما رامین‌‌فر بازیگر معروف سریال پایتخت و پسرش روی فرش‌قرمز جشنواره فیلم ونیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/106101" target="_blank">📅 10:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106100">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/710d093c91.mp4?token=UZ5midjJsOxEVJdezhpDY85DcQrIMOO-uQ7bD_b3xV3CMt_CnpAqO_kFQfg6hTTfXP-JR8t0Gpo8q8o9X0I-nJNGcXGFkfP8izhbLyyVmaInDFJHurf7EE4MLscxioZ0BGQfjztiJr1etfmu6uawx1-NpwokV2971LoxwxEQcTSO5TvtcqF51ktV_-0xcE8Kj-MHfAGZdVJAj6kY1BuAyy-5YY9nNjbKIHtyyvjhRq12wJ_525TN_UezEWPa9H1PlYBUCLp943r8SG5VrnH5C0jwCR13mPSgIx9SNrBppLrPl4rRdPMTtb0jn2Ym6PVCOCIzj0PmoP2iBcg5gf-qqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/710d093c91.mp4?token=UZ5midjJsOxEVJdezhpDY85DcQrIMOO-uQ7bD_b3xV3CMt_CnpAqO_kFQfg6hTTfXP-JR8t0Gpo8q8o9X0I-nJNGcXGFkfP8izhbLyyVmaInDFJHurf7EE4MLscxioZ0BGQfjztiJr1etfmu6uawx1-NpwokV2971LoxwxEQcTSO5TvtcqF51ktV_-0xcE8Kj-MHfAGZdVJAj6kY1BuAyy-5YY9nNjbKIHtyyvjhRq12wJ_525TN_UezEWPa9H1PlYBUCLp943r8SG5VrnH5C0jwCR13mPSgIx9SNrBppLrPl4rRdPMTtb0jn2Ym6PVCOCIzj0PmoP2iBcg5gf-qqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇮🇷
هوادار جذاب و خوشکل تیم فولاد خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/106100" target="_blank">📅 09:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106099">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe421b6527.mp4?token=gujOmd4ip2VwRoFZdcMH9bVoS7X9YD40L1zqpc8OiFgqlJtavnBmbFfKOE6-cXCT22qHUH3c1HrRN15SPKyyVI1Sa2lwAMXP3tXUifPQB_MM6ytoo70h3ajw8RVKB0G2tm9Xw6x2hE5g8DbqpzypBFGVzwN5be_yjGjm6HdWiUu7H6j1vvd7yV9fBnj3fx_Vdyw_S5sQjXQxzcES_03MBPDZ4G3s2FWwb7P86LoqbMqChTDvm1tAZPaxYsKw93yvybTIt8QRdT7XkLumnKGC3c3CWJ176h3buscuuk-VLMLBBieIupKoxTSATh2_Cyewzcw1vebXRK6j63qrqRD5vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe421b6527.mp4?token=gujOmd4ip2VwRoFZdcMH9bVoS7X9YD40L1zqpc8OiFgqlJtavnBmbFfKOE6-cXCT22qHUH3c1HrRN15SPKyyVI1Sa2lwAMXP3tXUifPQB_MM6ytoo70h3ajw8RVKB0G2tm9Xw6x2hE5g8DbqpzypBFGVzwN5be_yjGjm6HdWiUu7H6j1vvd7yV9fBnj3fx_Vdyw_S5sQjXQxzcES_03MBPDZ4G3s2FWwb7P86LoqbMqChTDvm1tAZPaxYsKw93yvybTIt8QRdT7XkLumnKGC3c3CWJ176h3buscuuk-VLMLBBieIupKoxTSATh2_Cyewzcw1vebXRK6j63qrqRD5vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
داماد سابق علی پروین: بعد ۶ سال جدایی هنوز لادن پروین رو دوست دارم!
🔻
لادن پروین رو خیلی دوست داشتم الانم خیلی دوسش دارم. لادن سوگلی خانواده‌ بود، دليل طلاقمون قماربازی من بود. چندین فرش ابریشم زیرپامون رو تو این راه به فنا دادم و ماشین بی‌ام‌و که داشتم رفت.. لادن هیج تقصری نداشت خودم مقصر اصلی این جدایی بودم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/106099" target="_blank">📅 09:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106098">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36609cb5e6.mp4?token=WnyA0R-bD2SIMnOgJqd4dqgwaYcycfabnthVbYzG0s18KuYLQOyKEvn8oZWXnFHBJIErF_m04P1_0t0EpCGSnf0G1hPluco1VPAHqJZFmlUvZOCJ4T0Q5zsK3t_qq5eXzHpkIsQ3ZFpcJ7GWq5A0tiBLBVZlQLXvYCMqicwWh_UCaPWzfIoerfkWjYUWQz6aO18TmNk6qONYupwxLkTgaF4ByAzaG009Rp-mrDKo3OMJV_u0A96WuMkO1S8_SLCpjr7qdsc15oGmbJ4JzFdpBEB0ZIeAZa8cyUstcySoj0VJPrPFfRtjFQ6TjaZ6MFC5AIdMcdQu6IH7fCPpuAIqCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36609cb5e6.mp4?token=WnyA0R-bD2SIMnOgJqd4dqgwaYcycfabnthVbYzG0s18KuYLQOyKEvn8oZWXnFHBJIErF_m04P1_0t0EpCGSnf0G1hPluco1VPAHqJZFmlUvZOCJ4T0Q5zsK3t_qq5eXzHpkIsQ3ZFpcJ7GWq5A0tiBLBVZlQLXvYCMqicwWh_UCaPWzfIoerfkWjYUWQz6aO18TmNk6qONYupwxLkTgaF4ByAzaG009Rp-mrDKo3OMJV_u0A96WuMkO1S8_SLCpjr7qdsc15oGmbJ4JzFdpBEB0ZIeAZa8cyUstcySoj0VJPrPFfRtjFQ6TjaZ6MFC5AIdMcdQu6IH7fCPpuAIqCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥲
🇮🇷
🇮🇷
بدشانسی دختر کوچولوی یزدی در حاشیه بازی چادرملو مقابل شمس‌آذر قزوین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106098" target="_blank">📅 09:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106094">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lpxlU_OTZ4CQzMAQXy_TN0-7RYO9-MYR5chu7oYtw18wb7EwKcqF0XXbQMrTtFg2o32hPnYoUhZ8Apay-BdHKtDAm6uHkGRF0RzKjElwZOcs8lwZp3Mwq3yQJ4N9vfE70zMJ35k3EkcBvn0SDGT8XgKzcbvseTe0EMQmx4izNAEGOPpZeaQ4xlGYsaoTN7K7dteWVqm0tl0Iaws3bgS_WsiWR7TXuG4mESp_Ig23Zw5F-wtAS4VbqjcsAjGFov6FL-oX_UaOv_APPppPO7HB-jU2w8Byj3Ujs5_ntfS05zr5Ni7zM93_lVCqG9eWVGwf-OtBWdzPsSriMhb2N0lA4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mUCZLZWLjPGbONFXv9JC1gER8qusld9tCxFBJqEAZqBmGQoigUSaCV42B_PenGSPJU37ZbCAfbywT2SOBIieuaokqig5pFg8Hdkrg5WnJ8HC94mnvgqp6tFO58YN76NaS3gqCzi-f6aAKfsylbFTbPk6Y4vpCDjzBj8RPYFuzmoCjtC1DOnSJg3lIQoetYgK7-iLZc7GtmB2aMm2C1r5LV9jDH7cDtct4Y_RzSv5Kv3jjUvKGZZlX5PwHvAioPBukkwkpQcdQ6l2gz7Fg4DtgCBvlml-DexWC_IkC0kdWAoVVZzh7QDqZs9kkY49YbZz-jiJW6rQFsJN6x1gRAAGag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r582HoISCC_fkU4tNNN9e-Q52gLYOl08UawjeH0zhc7aM_k5ePcfNoU56KTB7qOEnlL11yn9rMEmzEaqGvT2Wse7teM0GsqbLaeaOuPC4eHU16Y2i4gqSlY4n51gLKXpUC--CXDUbvoaBtOI3J72WQa8agXzNLcJ2K7dMkmA970NCx-t55xsD86kVym8SVj_PE5Y6d9fpbr2DK_l46JuTU_UwGhzIf_06QUzLzmCUUxHLIYJNm1WXTFLbvRPN5GzFGaWtlnEFV6VMBuWM4_sbwdkGFHmUGyobB8yIC0xhGMr_Ny8MomiehasePFImlPhFJTWAJ3-FM3y2Gc6vCf0iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rzGwwyW3xb2RP19sKNeUOH_ak5SxgSHMnM3gHmIaGqLo1kj8-ywm5vXopBMi-9Cuzakx7EYMX03a8JC8y5Re4IpyI9pIEfJIgrymxcPf61mvDkFgAP2NFv9l3UakFk_qK98_DF6nonNPZVotm7SpPtKq8BJ9nKqtcsASrx2_IaZotKlk5T4JMy9eJKT34swwuzwj9FepQmzSPQKI3XRTo0R1AnweS5wLx3G6wx567zfNCBbdIwIP7pXltlbpo1PvCxy_154GQky7KK2zrJHWv52ztrgU4HQb5msw0pVRqyG3k15MEwatlpLSISVYwAON4ybl3sylMnzvA2Pi4EFN5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇮🇷
دختر پرسپولیسی حاضر در بازی ذوب‌آهن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106094" target="_blank">📅 08:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106093">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106093" target="_blank">📅 01:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106092">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EF1S_zMmaRQztozob56FaSImAyTf7MjUYVEcuJXDFxNHAOTSxdyF1dv9gARp-lrF5k6bwCViQq5c_CbJgOFulsczLUqSnAWrM-vsYkAcYSVUWfPpQmLEtCOxgrt0RiqD7ilHvOsM2CbS7a34NOHc4nc9oqFqbdDPLz6QztzfwtDVSiLGTNNGyUXb6jibsyrWa7N2q75EULe6_TgejI0yoNgoT6M9ZWJfsNazRqZbSGoMo2XP_X1QfwLA41UZWOaFGZcYkf5kRS7gNAK0bELqur5OgIgvfA1mU0rt9vc5gFZMpaOTrcnl9ADRbngBovzPg3waH8k07huRlcRyolAeFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106092" target="_blank">📅 01:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106091">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106091" target="_blank">📅 01:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106090">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/970c991132.mp4?token=KVmBL4K1R8sD2sHXxrM1h63g1LzQZoojdHfHPsVt95iSJRGQbxCxkpy0Rs3SFBaGKJIqRhNGPp7orhQv3F9yuMT_YLd9ZfdTm08sWYRmZ95EhpDuW-Ox-TnQJ9Zyj3lfVTb5w-XinRM5rBhqtYBVqdlYchLar3ZA0m5FSC1XMLKbo5ygABbWckHXqhUGH5pYhsOXp4TejJ_g4wouKCC7dxU15z_FhWdIY18EunWUEbW2BnCe8gmW6XnGXiBrqkwDvfRwVZ9yISAxgJOzGVWKQDkHCTrFw3Z49jfEwXRK4Iyc3ms4ygdRdv4VcJ3wfLgOYDDMG357n8jEg7Zr5-fBPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/970c991132.mp4?token=KVmBL4K1R8sD2sHXxrM1h63g1LzQZoojdHfHPsVt95iSJRGQbxCxkpy0Rs3SFBaGKJIqRhNGPp7orhQv3F9yuMT_YLd9ZfdTm08sWYRmZ95EhpDuW-Ox-TnQJ9Zyj3lfVTb5w-XinRM5rBhqtYBVqdlYchLar3ZA0m5FSC1XMLKbo5ygABbWckHXqhUGH5pYhsOXp4TejJ_g4wouKCC7dxU15z_FhWdIY18EunWUEbW2BnCe8gmW6XnGXiBrqkwDvfRwVZ9yISAxgJOzGVWKQDkHCTrFw3Z49jfEwXRK4Iyc3ms4ygdRdv4VcJ3wfLgOYDDMG357n8jEg7Zr5-fBPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤔
🖤
ایرانی بیا که یه حسرت جدید به حسرت‌های بیشمار زندگیمون اضافه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106090" target="_blank">📅 01:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106089">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9d64db334.mp4?token=s_4Khgm1lMl8ry4JPJr0NXLYkPiE3I878HHccrebDL7hbV_ShdmlnGdRUy_JxkQr4piYsfmYL1BGVczejDQnOSi3hnBFwG4ud_qSCEQyvQu1CqFdjxqwf0Vwdi_6AhMPuC35EKTuqpHz1vShxNVLjbBVN1Hyvs9gKz_QML-eTYuKDrB9IUVAIzoto7rstFAz2ywab8Mp028ic6OcmuLAnzVLPxirRDmPG3oeBun4jqEwyNTrJWOwDxs8bDyL5uCGmkUAM6T7VkIRBKJA26POKH4RyUAo_9DJG0cyhW5QlK4OoB0k6TxsVGxrMv46UHwn5sl6t2xjrNbknPK0gRiVRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9d64db334.mp4?token=s_4Khgm1lMl8ry4JPJr0NXLYkPiE3I878HHccrebDL7hbV_ShdmlnGdRUy_JxkQr4piYsfmYL1BGVczejDQnOSi3hnBFwG4ud_qSCEQyvQu1CqFdjxqwf0Vwdi_6AhMPuC35EKTuqpHz1vShxNVLjbBVN1Hyvs9gKz_QML-eTYuKDrB9IUVAIzoto7rstFAz2ywab8Mp028ic6OcmuLAnzVLPxirRDmPG3oeBun4jqEwyNTrJWOwDxs8bDyL5uCGmkUAM6T7VkIRBKJA26POKH4RyUAo_9DJG0cyhW5QlK4OoB0k6TxsVGxrMv46UHwn5sl6t2xjrNbknPK0gRiVRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لامین‌یامال
❌
لیونل‌مسی
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106089" target="_blank">📅 01:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106088">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
⭕️
🇺🇸
رسانه‌های مملکت: آمریکا ساعاتی‌پیش به مناطقی از سیریک حمله کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106088" target="_blank">📅 01:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106087">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaKvwo_hwxgR3oIuzZ3HVx74FyTD7G1fjTCWmeoSZciTcMITkeKd_3kBReO1n0jJMfYWNyn81jbrSdQfzMbYvedV7bd6Fpd8WGSlWfeik9dS7gb8lsLkHqV8qTlxGO6MwGjbl4Rk-ET3G1D6QC2U2fSZcct6Iz7uwNgJ21tCfcnlONJblTo6rG90hNCBfayARVuBrck4KEFpO3PFjG_qa_hDCm7LDLMYAPDRWzafueb3t900U6Qj15ERjYYldsq8yLkxEHsG-SQVqw1Mgy-5rNJYmSYV6Ib26_PDMzWAOSe4Ei4GnGlbYJnmPk2Drpsx-9hdbCxJ0CWJKbzZX-MTTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🐐
🇫🇷
آمار فران‌تورس در بازی امشب تیمش
:
🔺
15 پاس موفق از 16 پاس. 6 شوت. 3 گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106087" target="_blank">📅 01:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106086">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-Tz6-zxrP-vLJjA3ZDmvCtJ0fCJe_oGvmEeqGkMMlrRZ5ewOyrMDrP12Xc-IGTPbYrr0HbyAbhrCgXKxKWWcor5Bq7gu0wF_OZvVyVMkKBzelceKUOYnz64GgFz4bJPE38suUO9Y8j3SkY7-pnXqPf3u_ButG5GRtZQ--ZvyS2mq4VhfywXbH4SOVunZyLzd7LcgN4OCzs_iXWqBpyUzVQkopuXg6mPTp4Vuq1-ytDm-L4sR_eoPH6uFSYklEWZgWmgbbg--tuYUOVUKUw1Fmk-Q98AG79C7wGQHlRPsgPvZ84tAUQuylmFyEz4P5ElwEezJ_fvKlUG98CquT9x3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برای اولین بار در تاریخ، آرسنال موفق به ثبت ۱۶ بازی شکست‌ناپذیری پیاپی در لیگ‌قهرمانان شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106086" target="_blank">📅 00:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106085">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
دیدار ذوب‌آهن و سپاهان از هفته هفتم لیگ برتر که قرار بود روز شنبه برگزار شود، لغو شد. دلیل این تصمیم حضور بازیکنان سپاهان در اردوی تیم امید برای شرکت در بازی‌های آسیایی ناگویا است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/106085" target="_blank">📅 00:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106084">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LF5IzU1znFccvGbUrdpTFBCFairgVWlB4PCHtymSxnX_s6xv1ssvLScm_hiBJRUALfCkxI5aOvNJv_yyo-yqsEJDRPp7be4QtxK8gMNwRAqVTN-OeN4-QHG_U0BNJILA_SnkqqwEGXd7rlcBIHrONavYp1jfNYT86VcL2Uxvr6r4wH4L9SJyF9ZOr4VLxuPv29-uGkGETnOFAOUYvumr6ufDLVZtcp_pZE7rZrwpyF3cVRvSjCDs37uqkDWBw6AYBZ40uHNkufWybj-B75CN260Ip0Sngzsm8UAmRBZbSnDj6eisrRIaDgNjDj5YW2F-yoS_sGGITT7oTDo3j5HAKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
📊
نتایج روز دوم از هفته‌اول مسابقات لیگ‌قهرمانان اروپا به شرح زیر است:
🇪🇸
بارسلونا
5️⃣
-
1️⃣
فاینورد
🇳🇱
🇩🇪
اشتوتگارت
3️⃣
-
1️⃣
وایکینگ
🇳🇴
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
2️⃣
-
1️⃣
اتلتیکومادرید
🇪🇸
🇫🇷
پاری‌سن‌ژرمن‌
6️⃣
-
1️⃣
اسلوان
🇸🇰
🇵🇹
اسپورتینگ
3️⃣
-
1️⃣
گالاتاسرای
🇹🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
1️⃣
-
0️⃣
ناپولی
🇮🇹
…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106084" target="_blank">📅 00:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106083">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZ2CPXt5XjRWZ5fiefZXmf_3QvY7g0VrwFN1vdlOFCJAAcJcjYHQyOacN3bQWu_7YSHUVoyaobBzcyeaGLc_GWkKfky3fkBfHTkBFp1G33GIUcHot5rIQmmsZVKhUoAENNvKoQD7cmUcX_zQsgQ5zK-gMiEFar0P_tNc88f3ML1zktXOBYObgt_QUzQZ6knjSFHGCQKq4AqGVvSSoX8o9BjxQ9NVpQnKrYhj-6W63_DNQerdBr8Y5v03WL0HveY4VbFB2l8Na5Z-S1XNw0GPBuB4nL3js51Q8y5TAqXmlRC5Kc-b0Qxzems-BKSn3fP4pmKjV1K2aU8QTY2VQlsj_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
📊
نتایج روز دوم از هفته‌اول مسابقات لیگ‌قهرمانان اروپا به شرح زیر است
:
🇪🇸
بارسلونا
5️⃣
-
1️⃣
فاینورد
🇳🇱
🇩🇪
اشتوتگارت
3️⃣
-
1️⃣
وایکینگ
🇳🇴
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
2️⃣
-
1️⃣
اتلتیکومادرید
🇪🇸
🇫🇷
پاری‌سن‌ژرمن‌
6️⃣
-
1️⃣
اسلوان
🇸🇰
🇵🇹
اسپورتینگ
3️⃣
-
1️⃣
گالاتاسرای
🇹🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
1️⃣
-
0️⃣
ناپولی
🇮🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106083" target="_blank">📅 00:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106082">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/af7ad02b07.mp4?token=Gx7hZ7WlChIFfruoHxG0xuIUVcbkeLr916jL0gzstLUu06P6Uynr0aQchOHKBzgzT7-StYW7PS3hSXfqDKNm09-MGCMq0qr6FG8duXsbz7PxssF338N6LIZEXj-l9NBncK0h6l4fTMrQ4zEV9xugHwWCsG3GeRdFBDL3iQUFeoaBq1noBdwskONnwCfZ5Enbbx3P-4emEcZODzdinLGn38WW_3xAmeevdJ0F2MQYKYUXQQY8EXbjP9y5wGGeApCfk7htDJk5jdAwdRXw1lPv6BMSLKb0Jzr7Ig_oh51qIF53XAlx8fmXtd3ngZ_CeV0iOY0thY21OMeFvEL8vPkUoaXH1oyX37MtXXDVGtd3dQgu5u5rV0FXIBdZ0Hxg58bjRWNzq1NCkUVTR1gPYHnkGEu1QpaZsOEtvA2Ph3bVyORYf1Eu7UyiGvE7CeUZrVu_8EUrBqRB-6cv7ga8hz-bYho_h0to8xmGPLofQihA3PvFrgDUrglNcs30SebUdPsEw4eH3nlKsJqgqPZHMJYC9sV-2ZifRbqC1R2l2SbftaPgCZJns5aDbAJFCExhAFG0B_n0iptVeroCh2FuBYaR4s2LlxktQ_1AIzK356MSeG5P_Rv__Dr4apSzC4oAahPTPPDb0XPSotTPmIhKShzZJ4LFOkCsaNncZTgPOoVOiUU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/af7ad02b07.mp4?token=Gx7hZ7WlChIFfruoHxG0xuIUVcbkeLr916jL0gzstLUu06P6Uynr0aQchOHKBzgzT7-StYW7PS3hSXfqDKNm09-MGCMq0qr6FG8duXsbz7PxssF338N6LIZEXj-l9NBncK0h6l4fTMrQ4zEV9xugHwWCsG3GeRdFBDL3iQUFeoaBq1noBdwskONnwCfZ5Enbbx3P-4emEcZODzdinLGn38WW_3xAmeevdJ0F2MQYKYUXQQY8EXbjP9y5wGGeApCfk7htDJk5jdAwdRXw1lPv6BMSLKb0Jzr7Ig_oh51qIF53XAlx8fmXtd3ngZ_CeV0iOY0thY21OMeFvEL8vPkUoaXH1oyX37MtXXDVGtd3dQgu5u5rV0FXIBdZ0Hxg58bjRWNzq1NCkUVTR1gPYHnkGEu1QpaZsOEtvA2Ph3bVyORYf1Eu7UyiGvE7CeUZrVu_8EUrBqRB-6cv7ga8hz-bYho_h0to8xmGPLofQihA3PvFrgDUrglNcs30SebUdPsEw4eH3nlKsJqgqPZHMJYC9sV-2ZifRbqC1R2l2SbftaPgCZJns5aDbAJFCExhAFG0B_n0iptVeroCh2FuBYaR4s2LlxktQ_1AIzK356MSeG5P_Rv__Dr4apSzC4oAahPTPPDb0XPSotTPmIhKShzZJ4LFOkCsaNncZTgPOoVOiUU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌پیروزی بخش آرسنال به ناپولی توسط اودگارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106082" target="_blank">📅 00:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106081">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0e2d644ee4.mp4?token=LyALZsqDpKAU9zV1cEYi5HxgHXTmhqYU1od_NHJ6anBilYZKFlI9DCt-GwBrFNkSQqmoO3MAvsBOvKA_EQLfdwE4b1PP64q0EsM1ONs8JX5rxEof1mdsRC7aZvxTaqmbbybhR1q4GOE9Hf0L2yfQP7DhHck4Q9cO270rwJK-cYfBvfPMgowUI74ocddXM8MOsOVgeu_1XyHMl1IhjNziVfOoOr6Qhmef3KdM3Ru72B7bV2I8sg0Q0qACp6sWW3hUR7UZFE49pc0myBVbjcLp6dqtqWv9OnZ5S7tfZjW1mZAWw38Z9iSq9ydJiTPE5pRZLqwF-HwWMzkGbGtmeUyf8A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0e2d644ee4.mp4?token=LyALZsqDpKAU9zV1cEYi5HxgHXTmhqYU1od_NHJ6anBilYZKFlI9DCt-GwBrFNkSQqmoO3MAvsBOvKA_EQLfdwE4b1PP64q0EsM1ONs8JX5rxEof1mdsRC7aZvxTaqmbbybhR1q4GOE9Hf0L2yfQP7DhHck4Q9cO270rwJK-cYfBvfPMgowUI74ocddXM8MOsOVgeu_1XyHMl1IhjNziVfOoOr6Qhmef3KdM3Ru72B7bV2I8sg0Q0qACp6sWW3hUR7UZFE49pc0myBVbjcLp6dqtqWv9OnZ5S7tfZjW1mZAWw38Z9iSq9ydJiTPE5pRZLqwF-HwWMzkGbGtmeUyf8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇪🇺
الله اکبررررررررر سوپرگل اسپورتینگ رو ببینید پشماممممم چی زدددددددددددد
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106081" target="_blank">📅 00:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106080">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106080" target="_blank">📅 23:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106079">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106079" target="_blank">📅 23:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106078">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hG65tcEt6jm4Qnv-pjpCfOYg0pElJpQCY7M-pr3-WBsgrBrZ5ftxVB_BxkbbKI7S-7IJ-Fb24F90zzkyE8p52ba23WYF0J_hCE6x8bDLapUdctBjHL_gsUUuOc7Y3z6WrjBU32Ui6xJKurr3JvBSHsFVWZFs5A2uACnkUw4Hsbkybr_o-Z9nOBZ2c3I0SDwsfS0KVJliNbSLBgTBoE963l9N5gUx6vAGBnBLgjKgfb-xpfmHXRmUzHDgtAwBngP1MGyystuWpBUrR1DzjJqJ7ISmlIpar8y1L6GYLTqtMHTN-iw_UXxaxJZOlbofrPwKiKbealuDt0eIgkUiZRg25g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
▶️
🇪🇺
📊</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106078" target="_blank">📅 23:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106077">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فران تورس خارکوسه هتریکککککک کرده برای پارس</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106077" target="_blank">📅 23:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106076">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b4804a9f6.mp4?token=pyKW8XksKeZuviKMF128_gT6my6bB3qxIQd9EIUNoBaiGuvnKhDbQyVhnOKBZ264A_PIEybJH-GbhVG_pegnncVqMEtBDRbB3Q1ifEYa2jrCWD6P2BdIFIPYvx2rSHGvtUmaKMqHNyNIGStgwDYL0Moux3Uzxu3Slc_ibnANTK9IF5yJA1PoEfykEjlnouyO2-uaysCLy2qkinWTXg9LRnmcWnfIiY4vx3cbORL3AeNuBq7WePRhTXzJC2Md6FiM4yAA23UWZ9jaArNoep_UFh9aCku2x_QFXpLr9Th6ChqqySCXr9uqTEofhfdC9908-s7QyncQEvWtyVGASQe1Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b4804a9f6.mp4?token=pyKW8XksKeZuviKMF128_gT6my6bB3qxIQd9EIUNoBaiGuvnKhDbQyVhnOKBZ264A_PIEybJH-GbhVG_pegnncVqMEtBDRbB3Q1ifEYa2jrCWD6P2BdIFIPYvx2rSHGvtUmaKMqHNyNIGStgwDYL0Moux3Uzxu3Slc_ibnANTK9IF5yJA1PoEfykEjlnouyO2-uaysCLy2qkinWTXg9LRnmcWnfIiY4vx3cbORL3AeNuBq7WePRhTXzJC2Md6FiM4yAA23UWZ9jaArNoep_UFh9aCku2x_QFXpLr9Th6ChqqySCXr9uqTEofhfdC9908-s7QyncQEvWtyVGASQe1Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم لیورپول توسط مک‌آلیستر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106076" target="_blank">📅 23:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106075">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپووووووپوول دومییییییییییی</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106075" target="_blank">📅 23:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106074">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
مک آلیستررررررررررر</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106074" target="_blank">📅 23:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106073">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گلگلگلگلگلگلگگلگلگل</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106073" target="_blank">📅 23:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106072">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVwrvd47kLt5w8ZMUKFJnDYFQuFU1ry9XMlCQjOrQeCGsIFIn8lWcWMuH3dTDquEiRMNfzDHsRoMjAIxGviPaB2sF9ZxsUJNz9XMpnqcEb0him78pyBcxusenedg2-Y59IqmVAKytPOCXeWIFmdNHnmpX4P3dXTK0BWRm9vhs4K-vFhTGojeFyJ0BUzTE_HFtl3GpzL3I_jiqGb-9hQsc0LNgeLXCxjrlMLdoQKWIrqUaVN7X8o2qNvaakD20zBeKhfwWajoCQOXiveCnm_SV3R_dVFfrRjLaTCUf5Pbpph-tV0FbJ_gMydeWwc4d_SKsP-dr7VIqZSE_gcltbEnWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
نیمه‌دوم مسابقات با این نتایج آغاز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106072" target="_blank">📅 23:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106071">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPgUbDnNtMk6eOa1YLwhUe0E5XpHoIge77DymfzpojspqsVEcqT_WdhhfqDYTSDaCRUwn8uKpMpOv4GHvU2ZS1Z80d-N9sJFAkYgNbIGbhtC3eIWS6jUCrZfbcwSD3q1avWHDlGTyQ_W_T2ZmypvcmefMxtkoFWi8_qWxbeGoMgGjMQVsQJXJsCfRAlfanPungF3Hb2RzWTrSxZPK0XO5YMkwHFksy_OtGbc4Mo2w-ExyQzdPbWPNMdwedXtaOKWkb7faA_A09BiAFh3K453R9NuA9Svj7NhPXEDl1YTqGPjT98vkML5aswFkZJpcWLkxT0tJKyOYvzgCX_JJXx0sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
دیدار ذوب‌آهن و سپاهان از هفته هفتم لیگ برتر که قرار بود روز شنبه برگزار شود، لغو شد. دلیل این تصمیم حضور بازیکنان سپاهان در اردوی تیم امید برای شرکت در بازی‌های آسیایی ناگویا است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106071" target="_blank">📅 23:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106070">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64577d8800.mp4?token=CHbshMNoArjM7JFOzGNVJq0xw7yZfPKqDmAJXFYu2XR96D-uTdUvy2ABXrXZNiPhenmY8pqmhtEqKxS4yRH9xTGw5GXlD722gdx1m-M-rkaTryy0WOT_QRdDNBkyxuWuwXsOl7hhGufxLXaSybQYPkAkv0tiqdNCuvI9uqUaKX3-2-C3XuPNEOlWQpH2vdgV3xHmr62c6K9N-oTo2InxkRqkWIYj7WSm4sO6FCUoPxFftbJG5UuFEHrSZA3aS_D0t16GDzo96ok2WbcDeZdMffA3J4zxFXlXuOg6c1omlaL-bkgR06kVFgnFab1hYiWKkwNfK1HoNHKI9S2uIIjOpg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64577d8800.mp4?token=CHbshMNoArjM7JFOzGNVJq0xw7yZfPKqDmAJXFYu2XR96D-uTdUvy2ABXrXZNiPhenmY8pqmhtEqKxS4yRH9xTGw5GXlD722gdx1m-M-rkaTryy0WOT_QRdDNBkyxuWuwXsOl7hhGufxLXaSybQYPkAkv0tiqdNCuvI9uqUaKX3-2-C3XuPNEOlWQpH2vdgV3xHmr62c6K9N-oTo2InxkRqkWIYj7WSm4sO6FCUoPxFftbJG5UuFEHrSZA3aS_D0t16GDzo96ok2WbcDeZdMffA3J4zxFXlXuOg6c1omlaL-bkgR06kVFgnFab1hYiWKkwNfK1HoNHKI9S2uIIjOpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول لیورپول به اتلتیکو توسط سوبوسلای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106070" target="_blank">📅 23:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106069">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ارائوخو پاس گل داد
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106069" target="_blank">📅 23:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106068">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سوبوسلایییییییییییییییی</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106068" target="_blank">📅 23:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106067">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">لیورپول زدددددددد</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106067" target="_blank">📅 23:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106066">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106066" target="_blank">📅 23:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106065">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2sc5Nz4o8fRo4nuoy8BHbTLWABvUm5tct1hgpuQFGDApRy6sdLZdXMC34BCy3hXvazC2Cd6M08h5lb-s-P1mxaV5Ozph9jetWtiC_kbPGfpMFJeSiPq1okrbCVqt5_ubqXU9KOiZiZ-H-I5ZsR6j7fiajZs064nXxdc_ZQQv4LEMba9QaNYmIs8CfjwJisd1wH2SrMPARq6YONBBuv7qayK0-MQj7duc4dHojqYGtHeiD2oF-S7t9J0VbX5DAgWyJr7XRrSVO0FQbqpxy2uas6lVTKNnH1Cb5mP2b7YvwSrb_wCus36yFsDXcsgOrgH0n5TQ4oPtNs9Dl-rE5XSxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚡️
🔴
از آیفون 18 رونمایی شد.   چهار رنگ آبی، آلبالویی، مشکی و نقره‌ای.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106065" target="_blank">📅 23:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106063">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64d71d9562.mp4?token=eZDeLMvJ488eoL5ubhm1tZi3pA0fFF95WxEbrCm6S0LykljfLFBX9MqYDPGATUcPEFeKaNjQBrvdTTk1TUSB7-wCbgzX_Y171Bi-lYcAT9W7ykQQLrFUU86PB1fvf3hCj9v-qcjnw34722_DO2Jb9ZqMz-lK1B25UywYJ4UIlLlSo_00FCLNc9S7vfyqy3SJoUSfh-2ge4SDu4Bo7xbtoiWHFxINImj8SbAzawM-THaHbLz-SWn0dwAKJeJ3znLXpN3s14YDX6VCrwTUSa-ThYLvV4KUmdx9gK_wTCrTjRKbsDf4AP4PgVReA6XJmkPN61bV0cE3Jv6FOM0z9zYQlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64d71d9562.mp4?token=eZDeLMvJ488eoL5ubhm1tZi3pA0fFF95WxEbrCm6S0LykljfLFBX9MqYDPGATUcPEFeKaNjQBrvdTTk1TUSB7-wCbgzX_Y171Bi-lYcAT9W7ykQQLrFUU86PB1fvf3hCj9v-qcjnw34722_DO2Jb9ZqMz-lK1B25UywYJ4UIlLlSo_00FCLNc9S7vfyqy3SJoUSfh-2ge4SDu4Bo7xbtoiWHFxINImj8SbAzawM-THaHbLz-SWn0dwAKJeJ3znLXpN3s14YDX6VCrwTUSa-ThYLvV4KUmdx9gK_wTCrTjRKbsDf4AP4PgVReA6XJmkPN61bV0cE3Jv6FOM0z9zYQlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
گل‌اول اتلتیکو توسط مارکوس یورنته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106063" target="_blank">📅 22:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106062">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پاس کل از آلوارز</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106062" target="_blank">📅 22:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106061">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یورنتههههههههه</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106061" target="_blank">📅 22:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106060">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اتلتیکومادرید زددددددددد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106060" target="_blank">📅 22:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106059">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گلگلگلگگلگلگلگلگگلگاگا</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106059" target="_blank">📅 22:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106058">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbLixAHHRlKfiiWDL7WcDXkPeN7wPn5onbAjgV1ZoYX-fmNzFryfee5cEgkUdI0eLq21MMfdLMo0jzJzcUn4vCervM5kYCg5gelQXGj0T9MqiIyrCmRfoxjM4fuiVkAiFOWulu4jrztiaJaT91QhL4k60mpuSnkz1Wstm16f4W2lP55zaKk2tS1BujN57Tl4rid_mv9InfJW7jv815CHD-YVhgTGGqN7pS6HtGOQ7TjjoIOD6lpce2bzKVYNnDzmtEi26Uvld90QIxQw7Cni7IC9AWnjUITu_gSyNmZtUFuBEbpGjtQa3wWAhYML9bfKb2hnFPb4VToaTEbao3C-Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🇪🇸
🇪🇸
لب خوانی صحبت های رودری در جریان دیدار بارسلونا مقابل والنسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106058" target="_blank">📅 22:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106057">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M62OZa4eFvILn47yGQfx73Xz2ao81zAey-GIRYBkDfstKGW5Pd60Gqz8tbxIbM_YIBPo9_GuTUj-mAhC3isHcmlJN3MOhH3XgIK8gIQKcP0qe36xA0gtvKdfTg-KS5qrhoE0t_8Ej7P4ApY5YdLV84aMfUK6fdE4Z-HzwW_hfjvJKZOxucG5xQwhxDYSzSlqA0b-yOtnMbrs4DFur97ut33R9ck-6i9AMxFro9b8GJngfHcKlQg6KF70sQ2N2xM-YqLOsOInxpReakCWtnCIdn2Qe33Sf8q3g7warfEXUihZTVp7CcneMraScVPYkEsM7QLGvNPR8LlC5zylC1TuAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇺
هفته‌اول لیگ‌قهرمانان اروپا؛ معرفی قربانی جدید تجاوزهای بارسلونا؛ فاینورد در نیوکمپ تحقیر شد؛ رافینیا و یامال مجددا درخشیدند
🇪🇸
بارسلونا
5️⃣
-
1️⃣
فاینورد
🇳🇱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106057" target="_blank">📅 22:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106056">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dcba68c3d.mp4?token=NwFYOcwVskO7aA_OU-tFjzB68dPUgnuAhmfWB4ZU3RNDFU1vFSuvJ462so3FXFMjlexiqs_biRiuCZMtK74HuMJggCn56ZJnTmmPcfZ1Rp3PqwXkriKMK31EClMBT21jJP7I3aMp2KS3CDQc_9MLgO4JWkFOlRkej-i6gfzkoJHVYaAzktHyqp4FGhcpNrOdT__QjFeCM6-zxYnCS9F9laFJTRAPeJhW4m5m5wNxsG_eH81O2FVHy6uoNGfldpevAAYZwjLTJZ8gZQ7KepkpYWsiCKRtaoIUq4t7uSJo5KJOopWxj8HEvW3YnCZ3S-scU6ESjnJYjLsId0AQvgkWew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dcba68c3d.mp4?token=NwFYOcwVskO7aA_OU-tFjzB68dPUgnuAhmfWB4ZU3RNDFU1vFSuvJ462so3FXFMjlexiqs_biRiuCZMtK74HuMJggCn56ZJnTmmPcfZ1Rp3PqwXkriKMK31EClMBT21jJP7I3aMp2KS3CDQc_9MLgO4JWkFOlRkej-i6gfzkoJHVYaAzktHyqp4FGhcpNrOdT__QjFeCM6-zxYnCS9F9laFJTRAPeJhW4m5m5wNxsG_eH81O2FVHy6uoNGfldpevAAYZwjLTJZ8gZQ7KepkpYWsiCKRtaoIUq4t7uSJo5KJOopWxj8HEvW3YnCZ3S-scU6ESjnJYjLsId0AQvgkWew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: حملات بیشتری در تنگه‌هرمز از سوی ما رقم خواهد خورد. فقط کمی صبور باشید
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106056" target="_blank">📅 22:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106055">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siYKcX0gVdj-KtqI6uj7k6BDhQNY-EwVOIWfH_6K3smAMbfWgE8NBEOBQhfq5f43Sf8dKIShQR1omJcXqWmOqs6ThaYGM5BKPqcZ1Nr7TXD8ytBk5EJTCjadQkIf_w2-a2V9L7RGLLt6KGjI1ErjVcdZ_kpX_BTVl3BTE3cTljuhyugi-0Huji_2bi8vSZaV02b8eM1TcertCIuWHvmBm9h8rWJ0GIz3wjo7hT6NtHM1NWwLC9HjnSfNttfgwXbo3LeeMnmjFNiKvlEivQ5zZzMvoUh9yeKiTLZocQJjfGZSauuzUluBE9ve4IYYsTHLLQC8BgWkptkpXFpV4mygYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇺
هفته‌اول لیگ‌قهرمانان اروپا؛ معرفی قربانی جدید تجاوزهای بارسلونا؛ فاینورد در نیوکمپ تحقیر شد؛ رافینیا و یامال مجددا درخشیدند
🇪🇸
بارسلونا
5️⃣
-
1️⃣
فاینورد
🇳🇱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106055" target="_blank">📅 22:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106054">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcGQ6nzWy8yWO_lxaxbQ1Hg5s9Qj_jwbZGbkqTNGFBhg_HuBr14EQxuC_NN9dgOP3xddX4NID7Yt7BCDll46vGjl07CXZWFJnGit2J6IRBtUZ7-Xkh6EzNfeUUSVqJMFJx5RboIidkGZJhCNGHuOUSLbgSI53m-QWG5vEivlfaH-YeeiNJF2SdkwpOQKWkd0t_kh93m-kW0GdCXI9zbVQRJc-L2qaVWA6dcAQOpxOZB7_T4zRLV4CUw-9MKFVlvWhUAE6vjdxr1LoGCAQ8KEzu5UC6PGvfPz-yY-F-Nnn9WN_prLG0KwdPCwM46Yp-Z8ieQfFeU1yCQAYPhpaImVTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇺
هفته‌اول لیگ‌قهرمانان اروپا؛ معرفی قربانی جدید تجاوزهای بارسلونا؛ فاینورد در نیوکمپ تحقیر شد؛ رافینیا و یامال مجددا درخشیدند
🇪🇸
بارسلونا
5️⃣
-
1️⃣
فاینورد
🇳🇱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106054" target="_blank">📅 22:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106053">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0430c92c86.mp4?token=cc6brR8zAktXvzetBjR3rlgZQ90_5iCqpu4FXTuhhrvd_etQ9IFOzgppRFHALJ2nKo7YrgVxVacs7U-Ve84trrk_aNTPNgbI2ySaCmOlttSBNUPPyDrbyY2sP8al1rCfVJYZRLJzaW7IzkJ6S2DJcl6fD9kFz-XlOPqDSqEDoGeBQKTmAWQXMfTO_SjkicHhrZQkJC116i3o2FU_zAqxFmBvx3E2AeLed9r1i5s08K4oA8y4qhVXEXcVHjZ2aqPYqndzoUEH9HIHJBl6ktNZUyga7uj-C78bEtMupyurh5nDWdK70l4PkVHiCqJ_qFVbnXsEb81pCxNVPltEl2p1zwTtO3nP5ViqS_eWoCQSHyEh79yheMefd9EX56c3oPKWBIvE25Zs4_iydYcCzGQeLsQftWft9lHg1IH_fO6JF-5DHhkpSGZEsvxDJiRGopX_PqHOQXhmyw7wwxTWNV0Vyi_LqojPOi-VnH1BxwdRQf-yI6YyhSEdZTOHiwbiFXXPWQvjhH3KnIHHqZBwykJs8LjSHlCxJw8GV7Dw4Hm9_-X-mpJGSaOuc7S6HkV2Aazjo7AcML7DnIM5jjORj6_j3X9afWaiScFlHor7HeWkNoYQqti5JQo7myt95ABedHL90dE1hARUv3wt-LGsoOgWuY6PLcHmhsxM4zIJTLAez8A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0430c92c86.mp4?token=cc6brR8zAktXvzetBjR3rlgZQ90_5iCqpu4FXTuhhrvd_etQ9IFOzgppRFHALJ2nKo7YrgVxVacs7U-Ve84trrk_aNTPNgbI2ySaCmOlttSBNUPPyDrbyY2sP8al1rCfVJYZRLJzaW7IzkJ6S2DJcl6fD9kFz-XlOPqDSqEDoGeBQKTmAWQXMfTO_SjkicHhrZQkJC116i3o2FU_zAqxFmBvx3E2AeLed9r1i5s08K4oA8y4qhVXEXcVHjZ2aqPYqndzoUEH9HIHJBl6ktNZUyga7uj-C78bEtMupyurh5nDWdK70l4PkVHiCqJ_qFVbnXsEb81pCxNVPltEl2p1zwTtO3nP5ViqS_eWoCQSHyEh79yheMefd9EX56c3oPKWBIvE25Zs4_iydYcCzGQeLsQftWft9lHg1IH_fO6JF-5DHhkpSGZEsvxDJiRGopX_PqHOQXhmyw7wwxTWNV0Vyi_LqojPOi-VnH1BxwdRQf-yI6YyhSEdZTOHiwbiFXXPWQvjhH3KnIHHqZBwykJs8LjSHlCxJw8GV7Dw4Hm9_-X-mpJGSaOuc7S6HkV2Aazjo7AcML7DnIM5jjORj6_j3X9afWaiScFlHor7HeWkNoYQqti5JQo7myt95ABedHL90dE1hARUv3wt-LGsoOgWuY6PLcHmhsxM4zIJTLAez8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
گل‌پنجم بارسلونا توسط گابریل‌ژسوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106053" target="_blank">📅 22:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106052">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گابریل ژسوس
😂
😂
😂
😂
😂
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106052" target="_blank">📅 22:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106051">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پنجممییییییی بارساااااا</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106051" target="_blank">📅 22:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106050">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گلگلگلگگلگلگلگلگلگ</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106050" target="_blank">📅 22:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106049">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e47209925e.mp4?token=Fy0oqAH1VO9foaQfOzhxms81XdwVqo0_eef4iTzxnpGCc2iMKGFApwC-6U-LZf84WZuMg7TAXSQZ2DS1rsNdRKL3vmR7HRLqZVTFPd4B5hghQQ5yQyTCZCRWnzuBYeVjZVRo_Q_IEc0SZm_L580KT-D5aaMpZ42g6-pmhtKr-pyyxucdq1XtUDiNGqC9JNTGChWfGy7gT-OsAbrgZlcao1B30aF1M9zRILZQvvmrAq1t15GbiVFYQ835kBZWXbXQlT9RLDXGC26A0ax6-L12CkHglxfxo-_lLb4czSWtWJJxEfq8YDemw9wbTantCh08nSvk-KL1fUUzgdt5WYWDz0OZ0HYZcFRK3kI-baVKbflq7g4B6HA3ze7OXBeL9tzrpKhZ9p_tPLX60802bN81rmi3YjWysl0_GbSqALpZ5HrVNrpwWm95MFjCY9MXHa3rakq8Bg7eqLyUtdxtcPDpUMWSVvaofrk_RHcpEAPx0G_qgTs3mG-F9MTv-qwDm9eDU4lZhE7gXM9yqYMPNzEK7W43WCnvkCiXSJVpv9QgUMPEl068miy1yLqM1M859x_if4ursUSxkNIwC4fFSbQe4zU1M7-061tR-qXAmyQgtPpDC9jrDw0-g-LbMEwKU7PRxtPiHThtWLKcLsiAKFcCxG-9A_EfQztGfJ9P-HJ1S-I" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e47209925e.mp4?token=Fy0oqAH1VO9foaQfOzhxms81XdwVqo0_eef4iTzxnpGCc2iMKGFApwC-6U-LZf84WZuMg7TAXSQZ2DS1rsNdRKL3vmR7HRLqZVTFPd4B5hghQQ5yQyTCZCRWnzuBYeVjZVRo_Q_IEc0SZm_L580KT-D5aaMpZ42g6-pmhtKr-pyyxucdq1XtUDiNGqC9JNTGChWfGy7gT-OsAbrgZlcao1B30aF1M9zRILZQvvmrAq1t15GbiVFYQ835kBZWXbXQlT9RLDXGC26A0ax6-L12CkHglxfxo-_lLb4czSWtWJJxEfq8YDemw9wbTantCh08nSvk-KL1fUUzgdt5WYWDz0OZ0HYZcFRK3kI-baVKbflq7g4B6HA3ze7OXBeL9tzrpKhZ9p_tPLX60802bN81rmi3YjWysl0_GbSqALpZ5HrVNrpwWm95MFjCY9MXHa3rakq8Bg7eqLyUtdxtcPDpUMWSVvaofrk_RHcpEAPx0G_qgTs3mG-F9MTv-qwDm9eDU4lZhE7gXM9yqYMPNzEK7W43WCnvkCiXSJVpv9QgUMPEl068miy1yLqM1M859x_if4ursUSxkNIwC4fFSbQe4zU1M7-061tR-qXAmyQgtPpDC9jrDw0-g-LbMEwKU7PRxtPiHThtWLKcLsiAKFcCxG-9A_EfQztGfJ9P-HJ1S-I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
گل‌اول فاینورد به بارسلونا دقیقه ۸۲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106049" target="_blank">📅 21:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106048">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cbc91a214.mp4?token=AnOqd8IcSpvxgiETr0_9_6q9b6EIw-kDK4v49I3N8bCFZuvG_IaDTwhmal6utpG-drf3EYZq8g03sov2PN7pGrr4Y_zlM0186PlGDFdIqtJoT8MJ606-wh5UWVZ9Gbh73e5OWLxlqdPWR_5HG3lubQxkRCiTBR3cn0yYs2dnDl71CJx2IXxjkl0wRElvu9zcWHqS8GJa7L9vyeO3zUWptN4vUzlr1T7VOUuAPdyjt3dzn7KVTblzRuy3Ypa5S5zwMzkacXDBUbnURaaNt3WNaTN9akb-1RZsfD7fqp2UFVT4dz3kv2KwHp7f8TqTyQvw0ia7b3wiHbUNlO9GQmXNdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cbc91a214.mp4?token=AnOqd8IcSpvxgiETr0_9_6q9b6EIw-kDK4v49I3N8bCFZuvG_IaDTwhmal6utpG-drf3EYZq8g03sov2PN7pGrr4Y_zlM0186PlGDFdIqtJoT8MJ606-wh5UWVZ9Gbh73e5OWLxlqdPWR_5HG3lubQxkRCiTBR3cn0yYs2dnDl71CJx2IXxjkl0wRElvu9zcWHqS8GJa7L9vyeO3zUWptN4vUzlr1T7VOUuAPdyjt3dzn7KVTblzRuy3Ypa5S5zwMzkacXDBUbnURaaNt3WNaTN9akb-1RZsfD7fqp2UFVT4dz3kv2KwHp7f8TqTyQvw0ia7b3wiHbUNlO9GQmXNdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🐐
گل‌شماره ۹۷۹ اسطوره کریس‌رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106048" target="_blank">📅 21:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106047">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فاینورد بالاخره یکی زدددد</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/106047" target="_blank">📅 21:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106046">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گگلللگللگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106046" target="_blank">📅 21:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106045">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/064c2da039.mp4?token=KyNUc2i9zW0bRzPl83FTw17od59UHJi6ymU6-kSbYmDjMsgU_e3vDicuk9fNbMw5dKe1u60IvNQE17G3VYgEmEVAF5bKSA3AVWyHSlLGqBXuKWc7P9QXVo_hEShxwK5vphfgdsL_BIAeeTXcbUkHI15nHRB3kT7RGn304vn2g-OPK2CIA2RgQJgoiXRBH2-g42vQmS9yRk-wsF4Ag1T-KyLY7Rqqvpw552EmZ-cyICEsWfs5JV8xXcSOzPtHddHynXNhPIKWbIa9ym3pM6KEwuXrMhCQfA_2E-z7rVjpUQVtY-fU36yscJHIqkr9PWFPC0RsBi3tLhpHEhkbquXIHw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/064c2da039.mp4?token=KyNUc2i9zW0bRzPl83FTw17od59UHJi6ymU6-kSbYmDjMsgU_e3vDicuk9fNbMw5dKe1u60IvNQE17G3VYgEmEVAF5bKSA3AVWyHSlLGqBXuKWc7P9QXVo_hEShxwK5vphfgdsL_BIAeeTXcbUkHI15nHRB3kT7RGn304vn2g-OPK2CIA2RgQJgoiXRBH2-g42vQmS9yRk-wsF4Ag1T-KyLY7Rqqvpw552EmZ-cyICEsWfs5JV8xXcSOzPtHddHynXNhPIKWbIa9ym3pM6KEwuXrMhCQfA_2E-z7rVjpUQVtY-fU36yscJHIqkr9PWFPC0RsBi3tLhpHEhkbquXIHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل‌چهارم و تماشایی لامین‌یامال مقابل فاینورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106045" target="_blank">📅 21:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106044">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سوپرررررررر کاشته تماشایی لامین‌یامال</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106044" target="_blank">📅 21:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106043">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گلگلگلگلگلگللگلگلگل</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/106043" target="_blank">📅 21:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106042">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
🇮🇷
👤
برانکو ایوانکوویچ: بزودی برای تماشای یکی از بازی‌های پرسپولیس به ایران می‌آیم و عشق و علاقه خودم را به این تیم بزرگ و تماشاگرانش تقدیم میکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106042" target="_blank">📅 21:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106041">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sk-9JGeZreaTcFmJ2q6xaMJG6G0WMVCB6Grdu8VYJRG3y-opfgHAkmddkiJcdWkFhRWo7MhSGk3loH8zUXV_wuHYnUp3VEZHr7SctAWJpqhPxbsbPCBAPfr1uNmjdQIbmwJfcQvjg6O9Hi0ekNy6i2fx0d82vTL1WjP4tzKAF7re1ijW_Xetqiu485ZsHABmv73_WNoC35kvm8zmhgJDtAAjvZpZ9ou2-G4pulWQzNto-PFkZthOv6F9LcnaCO9JdjwpofUIzaNwu1tq2gmr7dAtc3hAqaiIKB3-ofwmQwtLAqLMlYxH_KkyPNe9hrgWrHM3z37WWpXq0zwHulr6tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
❌
گل فاینورد آفساید اعلام شد</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106041" target="_blank">📅 21:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106040">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇳🇱
گل‌اول فاینورد به بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/106040" target="_blank">📅 21:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106039">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/890fd0d430.mp4?token=gpVf3xiDiOsoGgtyKtc0ZftMIU9mYHM9rBZPz_GWikcsaJtJkiBzFYkEBVercBLTqieNMJB7CbArvw204k2ghLh0Vlke1ET9GWZaoo3VRbIS3-qkDBZ6A6oG87joGtLTSkviVaMfSK18hibs9-Hu9UgK1F_ZLnOQRLs1YOejYva-b-fLtavCRFXHsWnFuc30h4Fh2RraTFVW7kHcS6FQv0-Ljq-PUlqMaVKA7OyFjkUoJdavJ2WuhWZCa9iytHiHc_yR3smeYXS_vXK5UpUGa8AB3PzfQ17EKSnaXUja7El9oxqBZdsLY-ovUUfejIMBDip63Ft3oyBte1cwPXQCDaL9mywGSjFYJSxZy_04le3wQfFaxmXJfubAOVeminY1tMqw8GtIh5plP9IgSv1KOdVHhjq6bs8MhS_ZJHycqAOJ7KvR0mYGe40jVtdOIeFRr-eml59AEg2eUAWB0lUS8eUjogrL-rZOppTDoVyNBKYl-x_IiYJZXP6fDv0oZBoSFAZTpcmThpsrJVSMo8h-9Tgxp5gHJ2qqk8iXnzSoCA76swDwkRkPcQDxuAFOPHR4k4CO8P-3KMh5G3lqVSqo5na03uLUQL7f0ESyhBJ1O8bmkaTovZv6Xx3ctR1pIKHGQF-9BKySbto1RFtN58rTDWwpmDpY21ZAra80-YU8hlg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/890fd0d430.mp4?token=gpVf3xiDiOsoGgtyKtc0ZftMIU9mYHM9rBZPz_GWikcsaJtJkiBzFYkEBVercBLTqieNMJB7CbArvw204k2ghLh0Vlke1ET9GWZaoo3VRbIS3-qkDBZ6A6oG87joGtLTSkviVaMfSK18hibs9-Hu9UgK1F_ZLnOQRLs1YOejYva-b-fLtavCRFXHsWnFuc30h4Fh2RraTFVW7kHcS6FQv0-Ljq-PUlqMaVKA7OyFjkUoJdavJ2WuhWZCa9iytHiHc_yR3smeYXS_vXK5UpUGa8AB3PzfQ17EKSnaXUja7El9oxqBZdsLY-ovUUfejIMBDip63Ft3oyBte1cwPXQCDaL9mywGSjFYJSxZy_04le3wQfFaxmXJfubAOVeminY1tMqw8GtIh5plP9IgSv1KOdVHhjq6bs8MhS_ZJHycqAOJ7KvR0mYGe40jVtdOIeFRr-eml59AEg2eUAWB0lUS8eUjogrL-rZOppTDoVyNBKYl-x_IiYJZXP6fDv0oZBoSFAZTpcmThpsrJVSMo8h-9Tgxp5gHJ2qqk8iXnzSoCA76swDwkRkPcQDxuAFOPHR4k4CO8P-3KMh5G3lqVSqo5na03uLUQL7f0ESyhBJ1O8bmkaTovZv6Xx3ctR1pIKHGQF-9BKySbto1RFtN58rTDWwpmDpY21ZAra80-YU8hlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
گل‌اول فاینورد به بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106039" target="_blank">📅 21:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106038">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گلگلگلگلگگلگلل اول فاینوردددددددد</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/106038" target="_blank">📅 21:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106037">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d0ecaa5ad9.mp4?token=VagbBsNU4hTaWyebwcn6-Uf-xPtsNj-SjLlo6GaSJpD2gF-zysgYoQ-PirhPDolrJQuiKpxBtPlgiMGilUlyaWEhgTPJJXXEAQvIU3ju3tp2KC037j_GfDA_j_V5dbUtffe8Ce6xOQ6CAoupxPpOKo4GpehwS5USwxmqIRdibVSxCFWu-_lg6Us4Febetbx_vz68cgjQQjsw9hFp3DAAiNj9fy8ua4NFQT70l8xCT5fBjfRjD3mYqa3H0rphGJv9bgszuglLuj8AgVoVQc2cgRcPfInXfmYSvNsdwaWoCLlfju0_LM9BErWuwV6-ptqlzEGbGCTxKv2BdsP0OjR51A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d0ecaa5ad9.mp4?token=VagbBsNU4hTaWyebwcn6-Uf-xPtsNj-SjLlo6GaSJpD2gF-zysgYoQ-PirhPDolrJQuiKpxBtPlgiMGilUlyaWEhgTPJJXXEAQvIU3ju3tp2KC037j_GfDA_j_V5dbUtffe8Ce6xOQ6CAoupxPpOKo4GpehwS5USwxmqIRdibVSxCFWu-_lg6Us4Febetbx_vz68cgjQQjsw9hFp3DAAiNj9fy8ua4NFQT70l8xCT5fBjfRjD3mYqa3H0rphGJv9bgszuglLuj8AgVoVQc2cgRcPfInXfmYSvNsdwaWoCLlfju0_LM9BErWuwV6-ptqlzEGbGCTxKv2BdsP0OjR51A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
گل‌سوم بارسا روی پاس محشر پدری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/106037" target="_blank">📅 21:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106036">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پدری چه سوپر پاس گلی دادددددد
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/106036" target="_blank">📅 21:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106035">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">رافینیاااااااا دبل کردددددددد</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/106035" target="_blank">📅 21:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106034">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گلگلگگلگلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/106034" target="_blank">📅 21:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106033">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUqaXpTfshmg8f79G17NFjC7fto6evSQjc1PRf-J8GA84pToIU_fkjPqxxPrwF7kZp3tKc3mXztib9CoNKEiya6li5pU6iuBQ6gs1nkswIDlFvbJ_UhxG9K1WGg9ERuhzIDmnp77nlA_PZHEhfKACUIRfNP8U2ZEtaBsyCWQAdEBE2YgaaZPi9AOowJS7wcAcr8S95A0spOIN84svtLOh9MGz8kSfXnDTk1w-mCMgznQXAKCcp17VWftV8Y-afC6hJPzthj1EFYZ42MxQ3fI6GYyN8sNW-lCGP06i9VUHpRbmOcDaEciCBZgcewsCwqg8Srh49aWMRnMHk07bVMOmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚡️
🔴
از آیفون 18 رونمایی شد.
چهار رنگ آبی، آلبالویی، مشکی و نقره‌ای.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106033" target="_blank">📅 21:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106032">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhChPXF3bs1KBBhD93tYEGyEZKfLEvoC4CkUaQJGPEY-iw1xnfO1VFev0hiKIwJJ9HcsKTe3AmnUQstjTsM5M_2G0TWsVDfvbKEY4ecyg54P0snWn2O9rCDgcGFRkvxk5g2G4JW-DU1W84DPagvmy8IREDj1Ryin3iuGSiwL1glku1_Q1Xkrx_0vuZRyOdB8cZU-mguu5kyARTAPLTCPrYFfvnW3rm8Eg4bopmqsE3XVbIe8OkH5KtOZC_SM4FCa2q8N4q4epu5AxypzJGVWcuxsgQi_wpPSuJZcVn9Zy2ZbgjKTTeoyo3Hz9OghpmV03yuo-3hIJmUC4uEtvjznyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
ترکیب لیورپول و اتلتیکومادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/106032" target="_blank">📅 21:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106031">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dO_FEGu_gOfDEJDFm6u0MHIF9tvFn6ZunfS7vxQfgg4NQ1khh8S_OQ6sPfVbwae338KDqZPgHHS4SLiHcVkdRi3FHkTGE40ZSkOQZ2Lcwt-pF6BolitQ3uNZdsIMqKSiSgdEtbTtHDVz7fz4Q7gI5GAaTd1j2AQotYHQ1HPL-NBd0SSxhq14oiFBdSDXfnZBs7G7eWfaOxHN6fy-BUPjED4Fe9EgWaXeZR4Sf9EOXU2rxJmjSmg9b1EuMkdi4b0N8lGjbii-GOkvrRieqZ_7wnwPHf982BFkrTgfNhJPBBJoO9JNHc2ZZQtWjw6tCg09r9FpBXSDm_vnJ_2AYELabw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇮🇹
ترکیب تیم‌های ناپولی و آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/106031" target="_blank">📅 21:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106030">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0aFcENMJHx6Qyojh2K5NGQfNUpq3F2QKV_3WavnI9pReHOsMvyYDEnivzmwmU5yxMXNESG3M8ko0CWfp5d9XHOeI6Tk5TabhFfXHFzAQxa5IaW3SKVpxRUZDvqm8o8cW9yP7eR92yh7cEV-VXk9kLYQF_KitlmN2XlDNS5tAs3aD_W4NPzGa3gBbXUuX_3kya_FD6UDi8Qeh3yZijuO2ZrvtiADKDJ4HcoA5s3eThm_TVvngQ-UvK6FONlL5IEF-Hf0CYZsQ_3OyRtOkvif8ZYtHyy1GvVAFPw5YMUzmSgNqOmvmHMq4p1Q3nF0oYyZf0oZdN9AffpSLfJocRWfMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
پوستر باشگاه پیکان برای بازی با استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/106030" target="_blank">📅 21:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106029">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c8eea35c2d.mp4?token=UWVGbsyfibnPod5FZxCrHy_CSiusqMfaEs8jBfHB1reE1t6loR-b0ezs80eAraXxlsOjdsOGbXW_2vZCJGgUyCUSd7qDo7MC4T69asb4snzpoWignXrE4yvJJwiL3mviOkqv-GK5Htxylf7GYVTG7zrlz6Kp4QNk7qxsAF80iZrNOo8J8Y9ss7KYXoUXX52w6l1aOkAoH2qsTTnnh3cDWQsX1NTHAEp8OwWgQzaDI1sIKSJERtUCXcxDIxZPV2oIDejkrEYDQWqtBuOMD4CYt76OBCZ13_fq0Bl1547Ogqmr8MOXBSWaDwnO3K2ysjyFNw1BsThwVHHDMGCeBzcnGopWCeUvaWrqSeK-JxIf5rCijk_HlVu5PQ8TabLiH9dd6QvY8ybVOAEAg-iFAbYDsGhzRO-5fscuiygFXN4-nnWn2wImbAsIYIF1TXiX2IOIf05Eko3oXNzWcKwXFYLWVXQmvucOhq85nk6I7tX6idBimxURXOo3zZS5y-5QO-oUTgF0XQM9FgfplE0qXCkTgpdiIoRwKwrUGj9HvqeqmQSqZhFsNIJGs3f6D9fI4o2cWlH7OgrlQJwgW1GCqpUy0P2HpLJdFrIsqZgNJj3I5hi3F0xiT1bWmJIHo30qTXvUPhgitomUOycECZJD-Yh1h-WTLq2SmTGvF-oVmlIzcJ0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c8eea35c2d.mp4?token=UWVGbsyfibnPod5FZxCrHy_CSiusqMfaEs8jBfHB1reE1t6loR-b0ezs80eAraXxlsOjdsOGbXW_2vZCJGgUyCUSd7qDo7MC4T69asb4snzpoWignXrE4yvJJwiL3mviOkqv-GK5Htxylf7GYVTG7zrlz6Kp4QNk7qxsAF80iZrNOo8J8Y9ss7KYXoUXX52w6l1aOkAoH2qsTTnnh3cDWQsX1NTHAEp8OwWgQzaDI1sIKSJERtUCXcxDIxZPV2oIDejkrEYDQWqtBuOMD4CYt76OBCZ13_fq0Bl1547Ogqmr8MOXBSWaDwnO3K2ysjyFNw1BsThwVHHDMGCeBzcnGopWCeUvaWrqSeK-JxIf5rCijk_HlVu5PQ8TabLiH9dd6QvY8ybVOAEAg-iFAbYDsGhzRO-5fscuiygFXN4-nnWn2wImbAsIYIF1TXiX2IOIf05Eko3oXNzWcKwXFYLWVXQmvucOhq85nk6I7tX6idBimxURXOo3zZS5y-5QO-oUTgF0XQM9FgfplE0qXCkTgpdiIoRwKwrUGj9HvqeqmQSqZhFsNIJGs3f6D9fI4o2cWlH7OgrlQJwgW1GCqpUy0P2HpLJdFrIsqZgNJj3I5hi3F0xiT1bWmJIHo30qTXvUPhgitomUOycECZJD-Yh1h-WTLq2SmTGvF-oVmlIzcJ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
سوپرررررررگل کریم‌آدیمی مقابل فاینورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106029" target="_blank">📅 20:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106028">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlNTgCyxX3gAaAiSevtQhBGlkAQ-x1fPLxQfD0HXhAAAl8IVZf0YEtQrCfqAVe2zJ_0Sv39N_7J97VcrcPWWA-7q-dt8Ikpxd1CpEsb1E98WRaEqclVxJJe6DKMad2r8FmoZvVFSYpvznphxlO5U4fIMRtzEoOGQz-ndNoa37lbgNFr4VZR_g9EPdLDM_vgQwUsewTSz_tfWPG94_vtPa11svKGBvS2SGAN4NdFruKKVkSTKN8an6_1Zz93DY4hIgpGEefKYwDOojCmpivTHqLH94oRDXftuSwKWN1X9K3cBgVxIRtjAqqrbTHlIsNkLk3XFlkhoovW9YKU8ielkIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شادی بعد گل کریم آدیمی
😐
🔥
😐
🔥
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106028" target="_blank">📅 20:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106027">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سوپرگلگلگلگلگلگلگگلگل کریمممممم آدیمی
😐
😐
😐
😐
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106027" target="_blank">📅 20:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106026">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گلگلگلگگلگلگغگلگغگلگلگ</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106026" target="_blank">📅 20:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106025">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6q0WlEMQdiDIbX6prcp3amUD_okc6dw3WaS5btUMfopM39NZRg7Z4B2wE5g1n8q_tDCyrdu9X8NH-Ke6f8PDrxRIzbboCWkS_FRLoWF7fbaQkaPPCmA9_aw2vOxfshDp8RK4Ot2MxAPIyBLyx0rylHKgjonWzSZem7jISgCaIA6MRVBQyB_HmdkRNkf7HddtXbRL70vgoPA_FEuiYM5XcUf8OUD7VncntpIWbEoBVIE0nknF41FMCXNTQ6lj-l49b1gio_IXavriN5w9EbqIXeSTJ47icJM1XEEd3tx0GJY9XY-volsTR4GAQvmH_GBV61Ufs2GqVlEfbQpwoay8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلووووووو ببینیددددددد ناموسا
😐
😐
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106025" target="_blank">📅 20:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106024">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f1f0f0fa3.mp4?token=fS8h1OjuJ3cPxw5N8JLtoSpgpxQKDiV5o90O6QgtUF5AQ9G6_-CCqqilUwD2zVra6-Azl-NNWg1FF13Qmt5XYpwc4DwrAzFpjxi9_S8q7rROf7LnOFC1X6f3PjWFNOahGM6h7ryWMm42TX0GADHLkuiKhtlpNKM-QpZpxwyV33vfamtwsZ7GckIIsjR6T3TZAc_9ZTW7zM7LKzMrOTkCQKCn2E795sJq-0tfuKuowlP9_jxFOVa98J2whlp5msw2Anu5MdCv_dUxG8GW-I6UMEdP1t8cAxVwTc6ESujIEPen3iorLNbUo-moqFpEPrGNC-f6tny4_6hw-YjLSjpLpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f1f0f0fa3.mp4?token=fS8h1OjuJ3cPxw5N8JLtoSpgpxQKDiV5o90O6QgtUF5AQ9G6_-CCqqilUwD2zVra6-Azl-NNWg1FF13Qmt5XYpwc4DwrAzFpjxi9_S8q7rROf7LnOFC1X6f3PjWFNOahGM6h7ryWMm42TX0GADHLkuiKhtlpNKM-QpZpxwyV33vfamtwsZ7GckIIsjR6T3TZAc_9ZTW7zM7LKzMrOTkCQKCn2E795sJq-0tfuKuowlP9_jxFOVa98J2whlp5msw2Anu5MdCv_dUxG8GW-I6UMEdP1t8cAxVwTc6ESujIEPen3iorLNbUo-moqFpEPrGNC-f6tny4_6hw-YjLSjpLpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلووووووو ببینیددددددد ناموسا
😐
😐
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106024" target="_blank">📅 20:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106023">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGQAL6QTR2ApEX0ka5gLxO2cASoG8a8lubLXgbLY1jmmagxzGm8Yt-eBp5eApJfO2qQz0dYeCCv5AG8-9V5wEhMjiHCqpKQQu5j_WplXZh2Q425clCv_o0pWG-zfbH3q7-iRW2ZRFmX7rIpwf-C0UbidaydCJUPNnnXv6BrFcI-9dlXl8WZy24PPQL4FkU_aKl8ZSO0Gz2qNQG7rcpXT_HfunNMVm5RmrRpB-m9i1qcon0VCL_rzNbHy9iumMEuZOf6FcsJ-kME4GG3CRtIyFS88QGsQXFBWnkW5fvJUShu0wHvUGQqoftpnZyQnKQ8rO6J1tN3E7JxaxBCuyHtCwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلایی که سر مدافعان فاینورد آورد
😐
😐
😐
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106023" target="_blank">📅 20:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106022">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اینا چرا این فصل اینقدر وحشین رحمی به هیچ تیمی ندارن
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106022" target="_blank">📅 20:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106021">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">عجب سوپرگلیییییی زدددددددددد</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106021" target="_blank">📅 20:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106020">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رافینیااااااااااا</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106020" target="_blank">📅 20:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106019">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بارسلونا زددددددددذ</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106019" target="_blank">📅 20:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106018">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گلگلگلگلگگلگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106018" target="_blank">📅 20:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106017">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aeda36fbc.mp4?token=X3WKJMpXM9kxBY4naYCu9770cMuvERF_T0WeiSu_BN7O__h1sPUdDUciNEon3T1aoQY9a27nRz3l4G63EYYm0GfuS_G56UqlRbqBIVQssrRVflzdvbDjDwRAB61B9rJM174Y0OAFuMuXPmWXrqauMlumv-45Jrvil5Uvvm_LAPA6V3Mq4y3yvCTCIeo9TaCc1qYVB24iG-YrwR33XWsHnm1GRYoagJNKljRWBNdpx6t1gSvWF7kuGE08tl0yqPzkurop6ED7m37ESGlMFeptXpmqEdZRg8-8ET6O-6oZjxFWUYOEc_t-O9ZocXMhQjwryhD3Ek8AbtnYWlY960sXcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aeda36fbc.mp4?token=X3WKJMpXM9kxBY4naYCu9770cMuvERF_T0WeiSu_BN7O__h1sPUdDUciNEon3T1aoQY9a27nRz3l4G63EYYm0GfuS_G56UqlRbqBIVQssrRVflzdvbDjDwRAB61B9rJM174Y0OAFuMuXPmWXrqauMlumv-45Jrvil5Uvvm_LAPA6V3Mq4y3yvCTCIeo9TaCc1qYVB24iG-YrwR33XWsHnm1GRYoagJNKljRWBNdpx6t1gSvWF7kuGE08tl0yqPzkurop6ED7m37ESGlMFeptXpmqEdZRg8-8ET6O-6oZjxFWUYOEc_t-O9ZocXMhQjwryhD3Ek8AbtnYWlY960sXcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
باشگاه سپاهان از طرح جذاب توسعه استادیوم نقش‌جهان اصفهان رونمایی کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106017" target="_blank">📅 20:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106016">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8t7eq05kP9pcKbvRwI2Sis2L1ruGLr9KvR1PsrvKpi4XPIAqDjpUM23xrhZMB7OXC9gEQvY_U8iJR6sm94LXDgV230ecmSspnsgbKs_Fqp_g0x67Ky77InLltiz4GfSF520bwgJZdZH3vlr-sjz8_oLjah4Kvh7-tKeaPeWQyAyBOwSLKmwL7IzT7WteIENquTbp9Kkbdcp4S1pPNmnnLWhOVciuNMmT7ByNFwd4ju50SplrcOuLe6rqxeC5LmXPdTrM1ynidZbR_X_qQXuLLaCkkBDHVGichCldGV4GQDMyRLu036HOrWa6RIrzgu6HsRvZFi3fhjdbh3s88xg8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
📱
استوری صالح‌حردانی بازیکن مغضوب استقلال برای دیدار فردای تیمش مقابل پیکان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106016" target="_blank">📅 20:13 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
