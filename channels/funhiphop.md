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
<img src="https://cdn4.telesco.pe/file/ImXOoy79bOdOpAhF1nTXZMOTZXc_aitYHg8fqFdznL61eilCyYsGEESDXRpbook16VDm5dI_OPKCik5olOWkFTSiUtF0yzxDi4T84WHMWo4qRn65h0lhnuguR3i2seyBcE2UJYNSHZYRRtJ2dAFsGlSx07JK5Wd4fzoi_IovvRBRzf8OpysV36MsEadMUzpglZde3TDlkLnF3aizPEGAedb31320BmzpIuU35Dl0jE2yQDeUX5K_nPjZNI9dbPS3x_85ftF5ynwBP8L1Ht-DFVuwtKbm_M5vq6_n2oFSpwRGKzco3b5o_mdHF1Wz5EZyy2eD5XIYIhBhuQ0eg5bcVw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 267K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 03:30:25</div>
<hr>

<div class="tg-post" id="msg-84688">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hp_qqoZos2FSUyoCO8ZYdSkZ2km3mVIV0f44-NS-vVDFtQM-rQqdbzu84ddX-hfuk-F1I2ANP14-K8MVbwikLesYxffyu5V2Fep-e2NgAVjRAR_o0h81Z8s3aHNpNAn_0l0BLZmTJe0hRrL1PNkPDvLHECQ-iwE5cmg0twvOmw2LFWNZCZ15FB6a_D6jGKFBJw4fUbn31PBlj8jOsv2b2Mpq3030U0xJUNqcROnQDP3-X1RigwD3It9wutw6jRVqtKGDgskQ6FR3yEwaWnmhMh9NebopV75iXE0mRwDAMNhXufAiG2Bt_Jdt6E_oH-0d6QPkn25USGdvhbnoPBDZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دم هرکی اینو ساخته گرم یه ماه بود از تهه دل نخندیده بودم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/funhiphop/84688" target="_blank">📅 01:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84687">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJtbqiyHTR2XOmtxkgwzp3CI-fyevt-LsXufhwgk0DWcAlZEbyluC_n8jAytRG9OsUX4Q8HmsOEEl2k-ajxp7mplclFNJiqdIbOW8oATxO7teSajWKBj_il1ibhpR6NfjXen6-3_Bngu4tdCeSpPk_P1_qK6chuI-grhyGhFLHToBk2cPx3LEt8qoSt3P8VD0NGXqh2f3oiIUqrWdgTykyJ2NarGWbG13Wlp8jIjGinqrMXYvhMLYy-XSOaJ3UVS3o9GFgbPpFUFRAJrPkihzhNvRwf2kTNpGoxK7zZn36MQ28Q-rASoNGjdXQHgYy_0ji6lWs1-a2UEWv99Pi-j1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیرم واس دلت دادا
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/funhiphop/84687" target="_blank">📅 01:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84686">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">داور کسکش فقط به من کارت نداد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/funhiphop/84686" target="_blank">📅 00:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84685">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b32a1ac263.mp4?token=cpSeOdt6cYb1rBZvwMdVAiUa1Jp5X8GmVNdnBpPEk3BOJG7MTsBmpy-kS6w63AJ0PNPOsSyidGRaPQQAPM8xaf2tWgme7zIO6yVy_x7l9amHqqtWSKsrxgvKfMli-hByDdVgbxdsz5yYqUY8cQobp3b8xBMU2-0xhMWvRwAsk48TclQN2AQWx_gyS9xkZnlGJsP5pKuXMvvNeuo5TzhUQAiC7jBCnbaaUXW9GeEPJUS2-L8LaRJ9l4NdNW8NhiP8QNTfaDa5CpMrXf2W4IiFMuzD9RbvoWgNG5iKtmdOpCyVvVxZGehPAka3mJa5O_mZjwFuBjEXpdnFW6FSmzOjF5Pf7rde7c7bLakYDXwf6vU601Dp7lLlQV2_VCjxFJITm4S5uAVGplrg4AX3bAyrirACHdwGR2DRmIxGOkAnMSMCqPemtNZUQ4RA1GcWTmyY9CJiDBXNzcbijQ-TQxYmdvCikk1JAti50iAszsKxvWoyDTixAJOEUaeHbMvQZLvxF0I3D335t8TguYBeu-lyNi12_qJIt90nVdufKrlokYY0b2uuZh1Hi7mrV97LuiWD6x2pHrzOin4rhpgpuuDSn2cb3MoGFkpswTD_QM8J9WUttTtubvVzQJzfFw5ahVy6ISFbiJJD-vV55GJ2bPu_aytilR3RUNTBRwjyP6aP5_M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b32a1ac263.mp4?token=cpSeOdt6cYb1rBZvwMdVAiUa1Jp5X8GmVNdnBpPEk3BOJG7MTsBmpy-kS6w63AJ0PNPOsSyidGRaPQQAPM8xaf2tWgme7zIO6yVy_x7l9amHqqtWSKsrxgvKfMli-hByDdVgbxdsz5yYqUY8cQobp3b8xBMU2-0xhMWvRwAsk48TclQN2AQWx_gyS9xkZnlGJsP5pKuXMvvNeuo5TzhUQAiC7jBCnbaaUXW9GeEPJUS2-L8LaRJ9l4NdNW8NhiP8QNTfaDa5CpMrXf2W4IiFMuzD9RbvoWgNG5iKtmdOpCyVvVxZGehPAka3mJa5O_mZjwFuBjEXpdnFW6FSmzOjF5Pf7rde7c7bLakYDXwf6vU601Dp7lLlQV2_VCjxFJITm4S5uAVGplrg4AX3bAyrirACHdwGR2DRmIxGOkAnMSMCqPemtNZUQ4RA1GcWTmyY9CJiDBXNzcbijQ-TQxYmdvCikk1JAti50iAszsKxvWoyDTixAJOEUaeHbMvQZLvxF0I3D335t8TguYBeu-lyNi12_qJIt90nVdufKrlokYY0b2uuZh1Hi7mrV97LuiWD6x2pHrzOin4rhpgpuuDSn2cb3MoGFkpswTD_QM8J9WUttTtubvVzQJzfFw5ahVy6ISFbiJJD-vV55GJ2bPu_aytilR3RUNTBRwjyP6aP5_M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
این فوق العادس پسر. من میتونم کسشر ترین حرف‌ها رو بزنم، و شما تشویق می‌کنید.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/funhiphop/84685" target="_blank">📅 00:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84684">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مورینیو رو
😂
😂
@FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/funhiphop/84684" target="_blank">📅 00:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84683">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مورینیو رو
😂
😂
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/funhiphop/84683" target="_blank">📅 00:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84681">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m9XjxeD5QwgdZDVuXSLQIhB-1_WBbmPXO9gj3-lKBtYhXFGRodbMuzylTpr8f8HR1ZBafWP_rtgPhSke_vdd--fnC7M8-DrGD67-D-56syY7KvaPzc8wxf6PxEWudr1U7CsSRdDtoBsZ6BraSG8UIqKFIIndcwfN5PwWmyC6JkffnWBSzgj8bgfSmEB8RzYS2CPSfP25fM9idPUOzsuVlWBR9csKkTHiA80qQK13lP-mm9TFQzKccbFXfFJzWaTAg_XLqQTahWK6RlDS5V4p1hwR88-5KH2e900rvguh1PVttN3Amr_1Gnkqzu5QyVb7zIP9rXdQPexsHrdtQ0YhPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fliGJEG1L-6K2DGNVtfHoy0Ht6UhHWx6wguFTScKZd-GxyzVhRWp9dox1_VmKGMoRQcqobEMa_9aECL7uipbTGC42u6Qd41JByoToH_Y_fESoaUpJnZG1Op5K-2rEAuCn4CXCSqAxz31HHvUD_9TOdQBgxrmWkDPea_aR__KVyKBGp4aDjdDtnzjSHDQJlvuU2111U28O3TBEdR4bL27Bvs7VXtVFT3RPVrTC5RT-AoV61jVN2SSfSvNv1hZncTYrpzdu3vkbOR3cUNR_VfTyiy7ZRdBwkDtG2zUrH0PZPlwD0HaZapSxh5RZqbIwK2ldxY6nq9npxO726qTYsjNaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با پاسپورت شمرون به ۱۹۵ تا کشور میشه سفر کرد؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/84681" target="_blank">📅 23:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84677">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iizZ0yTFdfnWqq1iEQFQdsrxF5yHf2pXCS8Rt8pY1ctXSfQIuxEapY0WNI4bbOe2BiWns2f-zoLB2VQ1sGw7MBTr4VHgspQcqEJdLo8okZ3R_YoCzeb3VVRDgErJAJzr3PJCBakr8tMbs_5Bb2jKM2PFvcPVgf0PSZeku339TdRAV8B9OjbEtRf-vG32Rk1En-9RLjzUfIPI_7C1xVLVmQ4C3_EjeiKpHRvxoEzW9Xz3qJPLxlmnv5LnTlocIUtOdv6XMy1hhPC6bTzrXxNC3UYZ4pEikGC37sXSdkedukCw8i0WMd_PCCdbSOfURuaw5_2WEBSau4F90TtEBNQqRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bucuMaHf9c0Y00Wk5FeHMhLKVshGvjFseNmsTS0l1TUC-6GsqnPPJsqC1QjfMKRT9AeGIP-tyKkV7ra88mgQfQ74o8P-UYGmTBZVsic9PastAaeLu32L1p-dyiSu7bvqxIOLKE8rwThscqSlymnJl1yxIwUHXOu1hjS9NO0s4pnep7nkDc69ov71IE4So2WZnRGQu3gYZdcvMdv5tC1c2A3wLhx6L_GPvNgLWbpxiWiIY5odQmC5ts9iizngF4Rj7Lsypu9GIBwVQ8ZXRxesWLgqdTaVvm3hjW3Fwe_skFolhVNiWCtLsU6U4OTbCKw8p-CNkOqZjoOMepVZUr_Vbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MgWWVD3SYaRQclvQVyuIej1RBjjgEoR10PUiaEe6f7b9hc3c_113XwjxKtAYkSmJg_Pm18lmTaWYu4osg0bJw0kpGhAm7MNzvWMW7NRxXRhgaTMdU33fRST5qr3W8x3uEm2syd3GeDAcEnRnYuMJeg7pHw9xK1k5WkwLNOEBMQJpfPTOelP8loCL_1SwptOmvo3Ha8UDcl5yZzL5mpDUXMF3Ed7-ZAFsMl-YwZhoDhM_AJo4Kn4_r36LnwhLi4QgXAC68Bax_CETNuJFFJozLoDvYl-VxLCEdCE0Fk0T7Bn3CoWRWka2LVpH9Sf8GmcjlW7VU-jDz7glcPxhXdh25w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPdFVSjOW_m2ojb4RnsHSgbdMTTLQjnMVNyv6TNkkYppLhOlAYCmSS-6KcTM6tY22I-tbrWD2k_o7Mt2fUq_pc4hIl1O_QStBDZlGYpxrOozwQle2xsKCM2tw0-qTYoOUfdn71wwFAurvi_Iy9tgxBuztuvJDukqlA65nEEj0rLk4Xy6WACbkJERv5TCPamSZsIkWprkOjjriDzq6qO_Ivg-9YxdvfBSeSgswaV8zEZ2DrtBZcOtOOYrOed2BpOa9iYwkXU_rKECQ5-KpQxEbMemvOlWMIus2v1NuDkGAGlb6PxwWoFzsG3HRz-mXuYUMhQgBb1JyY1i7WcP3VsMUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بسیجی‌ها امروز با پرچم فلسطین رفتن دم در سفارت فرانسه که به سرکوب خشونت آمیز اعتراضات تو فرانسه اعتراض کنن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/84677" target="_blank">📅 22:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84676">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd88d22e31.mp4?token=mCSYx6v3MWt7EXq4mwmETzSWp9FPaDt0jqVhhcLYYGGTz0-Et5NfTvnuo1-e6D8Pv8RMM5u6vPaVUFqBLKvEEhlDxugCY41ZiT4uIciSB7nNOoC4ikMc7xmloDixp2e04Cu0p87uVGOpjhs_WHH44dWNcZRRSZunkPTSCcoSAuXa-kjYryL8SuxNiiIbVHM6crZ4SKqeNl7jAyR0uNidPNqxmKPsehrgLKtB0J3827xhGauh8HKcWyrXM7kkbNIHXw7j5z61cddYiJH3rHnp88YjfGo18BPnteip6YnVKMxeSmTXG5sBycvz083xnMBHNKrYBhdMcpfygDDuwWQUjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd88d22e31.mp4?token=mCSYx6v3MWt7EXq4mwmETzSWp9FPaDt0jqVhhcLYYGGTz0-Et5NfTvnuo1-e6D8Pv8RMM5u6vPaVUFqBLKvEEhlDxugCY41ZiT4uIciSB7nNOoC4ikMc7xmloDixp2e04Cu0p87uVGOpjhs_WHH44dWNcZRRSZunkPTSCcoSAuXa-kjYryL8SuxNiiIbVHM6crZ4SKqeNl7jAyR0uNidPNqxmKPsehrgLKtB0J3827xhGauh8HKcWyrXM7kkbNIHXw7j5z61cddYiJH3rHnp88YjfGo18BPnteip6YnVKMxeSmTXG5sBycvz083xnMBHNKrYBhdMcpfygDDuwWQUjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمسه میگه به خدا من بادیگارد ندارم چرا به من فحش میدید
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/84676" target="_blank">📅 22:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84675">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SS0kR7gqPXRb3GRcBW2UAKNum3-3mMyfdDi_mbgArlNhqAI7EB_upzP4vc5TQiVLaPp_2t64sZvuC_g8AdP_iIyu2F-VYINI3pSZcvjwIHouRsvSRVkqRJTu8fRH_gVJUZVa1tDSQNwr2sCI3s9YNcfGFhbsS6TvzHJ6Yq6tdVyETCos9JGD_Yo82ay19nCZSlt_sh2tQYjEVixQEYST42M8j20vm9fvBUua7N_6R8Ab-aaIjvllKOxLm4u1XQiaZN0URA1Q75r4xy6FQfQ0RJUmPoz99AJKEviyh3PHZS3x5Rbgk6IkVj-RIntyQQotlBz1yX5L6USKwBwQD_yN7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاره شدم.
بعد از اون کامنتای مردم، اسطوره نوید برگشت به تیجی گفت شما اسطوره و مرجع تقلید منید و افتخار می‌کنم که باهاتون تو یه خاک نفس می‌کشم؛
تیجی هم اد استوری کرد نوشت پرچمت بالاس
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/84675" target="_blank">📅 21:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84674">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Talangor</div>
  <div class="tg-doc-extra">The Creator & Lickel</div>
</div>
<a href="https://t.me/funhiphop/84674" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام تلنگر منتشر شد
🆔️
@Amircreatorrr
🆔️
@Rapkadeh_official
®
🎶</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/84674" target="_blank">📅 21:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84673">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKVvUOM3OkQoKERB4259ECKRuuc-Z-25iJ5CsIJGJeSjPqgGyoypMG-N2hm6CAjg_lhcj3hvgE7dr2d3TCcRodu7bELI5ofYxkylcOiYODWENtZoUVx3RD2m6OfvusFioko1yLDDrAOQqGQR8zzbcqce--zpWw_6xYv_gWMaLLpEYolJsrLIRWKyVsuenfApggJUHZ6EwZbJrJSB6wUYkyUuM9OvX_4-1NdLsc-lGtjv3FVZUFxsBccOkN7GSHnx4NmmZIFQcQCvCvStv9x0JH3SSKcajIy0WZ5Mm_ugeMtMbpbS3g0K0Y0Ib5pfbwXehgeG9NWjR651E7qkRpGHIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام تلنگر منتشر شد
🆔️
@Amircreatorrr
📥
Download
نظر شما درباره این ترک ؟
عالی
👍
خوب
🔥
متوسط
❤️
ضعیف
👎
🆔️
@Rapkadeh_official
®
🎶</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/84673" target="_blank">📅 21:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84672">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25eadd38c3.mp4?token=otwJFC3hbnGjk72XUW1KpHu9fWKlrhfdxJLdsn50GHaj5DhtW-MumR_QCM0XOjaM0u9gTL0CDcY7TmVnPZGbKGsx0eQuWx1rsq6keM3ZoCzhT80taTMlfZZPReFqjRQm7Fozv4pC2LrBIzwlkzlsbsST4u8A491p88PvOgUeAvF4zyUVfYalkXwdwap61KGCSLC_bcK7DZU81KCEEk-wTGCgQVOAkTKcLTNrsBTHEeai_kgmWU64l09kuvbHvFHcthAse3lHwABVF2VZ5S9ChjP5vbva3gpOHeEERRhxkSrQFKfj89ms8POzmV7pyAlXNMkzBiNBG8WJZAVwhz_CGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25eadd38c3.mp4?token=otwJFC3hbnGjk72XUW1KpHu9fWKlrhfdxJLdsn50GHaj5DhtW-MumR_QCM0XOjaM0u9gTL0CDcY7TmVnPZGbKGsx0eQuWx1rsq6keM3ZoCzhT80taTMlfZZPReFqjRQm7Fozv4pC2LrBIzwlkzlsbsST4u8A491p88PvOgUeAvF4zyUVfYalkXwdwap61KGCSLC_bcK7DZU81KCEEk-wTGCgQVOAkTKcLTNrsBTHEeai_kgmWU64l09kuvbHvFHcthAse3lHwABVF2VZ5S9ChjP5vbva3gpOHeEERRhxkSrQFKfj89ms8POzmV7pyAlXNMkzBiNBG8WJZAVwhz_CGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببین عرفان جان میدونم ضرورتی نداره من الان این پستو بزارم، ولی تورو خدا برای یک بارم شده یچی بخون بشه گوش داد، من خیلی دوستت دارم ولی واقعا نمیشه گوشت داد، لطفا لطفا
🙏
🫀
🌱
🌹
✨
🌟
⭐️
🔥
🌈
☀️
🌨
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/84672" target="_blank">📅 20:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84671">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
ترامپ درباره اوکراین:
«پیشنهاد می‌کنم اوکراین رهبر جدیدی انتخاب کند که بتواند به توافق برسد.
-به دلایلی، زلنسکی هیچ‌وقت به توافق نمی‌رسد.»
بابا یکی جلوی این کصکشو بگیره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/84671" target="_blank">📅 20:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84670">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وضعیت فرودگاه ریاض  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/84670" target="_blank">📅 20:23 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84669">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQeHlnZgp3pOk3w-NwqK1V3UqnKsIQpJLLh7i4MEJkog_Pj_pZbCdje1d9xgLJ9Q_ye-ZY8pEuXw4moagM8qM1xbZ5c90P1khC2JM_nZ4B29O8TliKy3JL3H-yV_tkwaqVjJMNXTibf0_JlbpsTOS0Hg8Pgpiv3sf8pvHQ0n03ImZnIiOJiNuKcZyiuihi09Q0kknGYFw04RaQa9lFawz_MhgAwyTzZL4po-QneymEFOW-9WOcxTUhz7akBKvr9Q8pa5We8vLUjfTZHGvet43s2PFYddTr_bW-flOyiRW6NDZbdhEWbfs8Tconjqy0YLj308EM5KVwsL_QVS4UzRaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت فرودگاه ریاض
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/84669" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84668">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/84668" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84667">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4_KF_1Cpbf9ryVBPAUbm-xXkEH_ochs0rg441D6WT-F0Xe6Vjh7ugrwwkUh9f7Q6IlvZuwRbAEB8aUj1Xy8FL5De70Xq4fikRofZoVppfXSxrRAscEanYXDvDj7CkqH8DFuaY-iql7eT3fNkgxmNlq1yRBZhJtPjnBoXn2JOOHAgx3nRR4ookX3pdBjy-pr4j90GwoEMh8pZcvJEb1_bCxls1q1wKs-ffRaomSZnxP3cJby8XFpLT8zwe7xNlpg501rFdIParJKHz0sZ-pFrdODwDiFmsiF1OBpZcLrwzQMtOBEzNYALCzTuaa3KtXEyciuWGMJAPYf3gfFGAdFBg.jpg" alt="photo" loading="lazy"/></div>
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
G18
🅰
🛒
ورود به سایت
👇
✅
https://ieoruyxtsud.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/84667" target="_blank">📅 20:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84665">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aae2137c8.mp4?token=bwY4Q5QbPv7y-Q-lCyoyCP29qj20S3iAOM9qezuyTqUwAxSqBdnt7Zl1u0Q2WtOZhSc2sdAm05X1X3oDZ6wIHe-ws0q4SctbpAfAeHy3ML7AUsUOBRdG0UHU1XRTBUhU2bppGfaqC0CnLToMPnYOtV5RQWHXSYLJ0zt1TF0LNu857qwkWMgOAZjEhUceVK7RmULiyHUbIdzY162Tj1S1PQmQN7BL3yWNLq88pTiFAVqL7fNVIFKbtETsAAK5zOeF-rs3qUDE3WvHS7rI6jpHWfCcxzmfAkvNNcQjAAzJ2nUoVNmFWFgefdv0iy9Dphjufw6fbVmg1SSfNdgL7Om4-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aae2137c8.mp4?token=bwY4Q5QbPv7y-Q-lCyoyCP29qj20S3iAOM9qezuyTqUwAxSqBdnt7Zl1u0Q2WtOZhSc2sdAm05X1X3oDZ6wIHe-ws0q4SctbpAfAeHy3ML7AUsUOBRdG0UHU1XRTBUhU2bppGfaqC0CnLToMPnYOtV5RQWHXSYLJ0zt1TF0LNu857qwkWMgOAZjEhUceVK7RmULiyHUbIdzY162Tj1S1PQmQN7BL3yWNLq88pTiFAVqL7fNVIFKbtETsAAK5zOeF-rs3qUDE3WvHS7rI6jpHWfCcxzmfAkvNNcQjAAzJ2nUoVNmFWFgefdv0iy9Dphjufw6fbVmg1SSfNdgL7Om4-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/84665" target="_blank">📅 20:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84664">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">امین تیجی جن زده شده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/84664" target="_blank">📅 19:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84663">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">چرا حس میکنم هوا دلش میخواد سرد بشه ولی روش نمیشه</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/84663" target="_blank">📅 19:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84661">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W0auDhlBKpCSS8xMlpt8o3hXiVKqBf_lhwM0jkC-Tclx23-jbyjLwDuFL8WZ9uBKuOJwyGa8mDdO-ht6-Ij8LPig_ENUMfUurCLL986XdNlf_fBmG1KfYEjcclNzbW2yAT7BwOPG7g4mvfqh76ktqw9TPvnPZY5c13ZunZQd0g13kmji_5ssOq04EOBQEPqh3JCfdQjFdbyOVLgFzaJGWchRQo8tfYLYAD0D28MUIM5Psk5TmDgu4pkGZ-bNJHiTtcIuPqQ6s2O3DwLXhcUCV8PrMIQesCUDCKMZ0TV6S51FvJUKcazldtjD6INGMyxZ6WEFBQNCnhZ3L3-PCkO5dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EYWJlJvKwmdjsBeIBJHGcb4PdMtx_itttvKd95LPhQa9WixVKRwPA_S4bujl9gadi1Yc6wV0r-abNyDit8ITMRLK1gI8_qRVk20sSSRV5tLITxbKJ2IfcX6uGstJS4U1RKpMK9R2GiIF41PDhs3KtQxTR4FFq-CLZr03vGFLDzk4JVt3grpTYR5MaiYsNiM2v3roe0op-gpeCxsUUO6eEZSyYtHzcBDFCAImThPQH8pwweZ_O0-bIDw8yNE4Jcb3eGp1lid5XT-CyOut4anLy4VvwfPphh9vahwY3gTBIDCkiJkjo7MqqJJKb7Pum701LLszz4YzATXBAo7-_f656w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریستیانو رونالدو موقتاً از تیم ملی پرتغال محروم شد!
فدراسیون فوتبال پرتغال بعد از جدایی جنجالی رونالدو از اردوی تیم ملی، تصمیم گرفته فعلاً این ستاره رو محروم کنه.
کمیته انضباطی هم رسماً پرونده رونالدو رو باز کرده و قراره به‌صورت فوری به این ماجرا رسیدگی کنه.
هنوز تصمیم نهایی درباره مدت محرومیت رونالدو گرفته نشده و مشخص نیست تا چه زمانی از حضور تو تیم ملی محرومه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84661" target="_blank">📅 16:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84660">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کاش آرتا و هیچکس یه فیت بدن، هم فنای آرتا کف و خون قاطی میکنن صدای اگزوز خاوری هیچکسو بشنون هم فنای هیچکس کصخلشون در میره صدای اوب دار آرتا رو گوش بدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84660" target="_blank">📅 15:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84658">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k7MMwzQz9udyJNao2ZKFoPKd8UhBpEmlRHSxRvSRMU5zAVquc79OPE3iGoNYBPJAdsP-fgZpxEglvw_8GwMyPOA9fEnfyJYuarU8p4N8IjvDzbvvcDe5cugD3yNaGe-bpLOy5s6HdgXbIgDd6H9OOK0r88IyZIHDrMXM67XS2GszcDJ2A_0a_38STYfw45_0wMuSHsmOrr30pkuMto0gfmGM4YVvxPV8gSGxAkiK-WOco5ANg3e6xvw7oJ2S2ndV_nO1pLpo7ZpQsVmZFKvxKrRsVmAvuXo2yamvYqqY_5AN182WhEO2e9mqYiGF-ZZpe3i33eA0J9cmCRyZi3zhJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qBxToaprXhieGXyyJ6lBOp8DAveeEnJqwA7vZmtSr78q28XtAa5txi1Q9InuiLJyOlnLb3GVAfvfop8ZWBt6WUZuglEhoL6UPOczIWbbvMlaep917_3B55kjCjVYpaFQ77_NubwgynEnvpREOpnkq9GECvlADe-1d2_38EtAUTzrxpOZZ_dkUWmuBTmRO05qizBIA0wW7WfQYiOtVYgFLXhSD9w84pbLZXeJe6J9Do92q2P3RqbjXN740V1Ho3_AFHBY_j0RLEWcGD8-GTNszEzoHrP7F7mANXhzskCFlPTCaTmLuwfy6VtDzGmZNHr6SXJFH4JMCfnIygbk__N1Rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سوتیدا، ملکه تایلند برای نخستین بار پرواز انفرادی خود را با هدایت یک جنگنده گریپن در استان سورات تانی در جنوب این کشور با موفقیت انجام داد.
وی همچنین خلبان بوئینگ 737  هم می باشد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84658" target="_blank">📅 13:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84657">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حصین جان جوس ورد از اون دنیا هنوز داره آلبوم میده، این یاد کیریو بده کونکش پیر شدیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84657" target="_blank">📅 12:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84656">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">در این دوره از تاریخ که ما شاهد امپراتوری آمریکا در دنیا هستیم و دیگه بریتانیای کبیر و شوروی سابقی وجود نداره، هنوز عده ای وجود دارن که کلش آف کلنز بازی میکنن، منم جزو اون عده ام، کسی کلن فعال داره؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84656" target="_blank">📅 11:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84655">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ:
ما گرینلند رو با قیمت مناسب به دست آوردیم: صفر دلار!
کصکش املاکی
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84655" target="_blank">📅 11:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84654">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwZIW4lKty3V5DurT893RuepAnPlJ5I-9p1N2Mt7TahAK32uoUdZcqhKbCuk-uU5LkcSgnSZpFmY3cN2RNqjoBFxC5ZYcQjFHLPnjs0owqcpSjj9c73g58Ad_-hqvZWvWdWHAiRvVSWwNQeDw09w60hCD0sfuztsoozPZabhFT611ezmhDWvrDfyWdqUtIxVDjr8GVY2INiHyZhK0nB4vgwYW8hI5dgT0WGIHpUa8EHWP5vMx4a-PCKkAlLtYxnPfLvv_2iAAtcW_ljrNDhKaJweIteh9xmXROAKJ6vrOEj3GDVqkXdVsRXIirDWuC9CAgvp378o7eVFX1GuqjqNPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من میدونم تا مدت ها قراره اکسپلورم با این تصاویر گاییده شه، فقط بگید چقدر طول میکشه، میخوام بدونم تا کی اینستارو باز نکنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84654" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84653">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/84653" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84652">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfOD7ZBbcCQV6KXzW55UDmqKL9LfYdrTKBsR_o_0jv7Uuxy76caywj33bCDbIxzYtJ2t29bG86PkCW95yAGEumc1Gcbs7uDncYb-VhsBjwIljSHFeu-x2rqeUOyV9r_fYkvyfWTfo7pPrI4FfItA__lhurqiQPfPGjsP21iCtv8PvzTYZv0cLNg0efG6dliCAC1a6HUnTJvi7KuCCbPlGgTFzSQMz6NOxJs4yVzX8qohdo4A1MS0-TtZDWiisvVciZxfNL0Tl8A-K6e6D70LcnU25pUb98grbEAPn-JbxXDdrif-BjmNGBwTeO8CBoBYKofkkxBN2LEtZ3ujc2cI1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
چلسی  - بورنموث
🌎
ساعت ۱۷:۳۰
⚽️
منچستر یونایتد  - تاتنهام
🌎
ساعت ۲۰:۰۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r18
🔗
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84652" target="_blank">📅 11:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84651">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4795cf2815.mp4?token=XHg3LDqG7iUymRpjw1jh9bDX-NZOvCODcrmlOk2cVvzrs_pVAwqZzfy5Rqo6fsUw7an_bk3--Y6a02fsTRB0N23KYY70kuQFMYf6_heneL-oLk3id_dc1ln-jBe-l5y-MY5i1_lg-NUUFIckftBfbJq-mIHLEL3DEi6sd4d-V2dh61LVm9-1N3Gd9MBcRXEMig90bHHjhCVPC6IP0Q3oLxJ9jtSfgc40RZC7zChBngmtAEPZ5RsAZMZk4ndl2K5au9tSlLQtWKxaFIRSA3h5od1gXddR5ovWy0dPVJhgbfEw3YTKttoXADbkUCs1rEmv2LUvjtS-PY_T7FSEq_uVKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4795cf2815.mp4?token=XHg3LDqG7iUymRpjw1jh9bDX-NZOvCODcrmlOk2cVvzrs_pVAwqZzfy5Rqo6fsUw7an_bk3--Y6a02fsTRB0N23KYY70kuQFMYf6_heneL-oLk3id_dc1ln-jBe-l5y-MY5i1_lg-NUUFIckftBfbJq-mIHLEL3DEi6sd4d-V2dh61LVm9-1N3Gd9MBcRXEMig90bHHjhCVPC6IP0Q3oLxJ9jtSfgc40RZC7zChBngmtAEPZ5RsAZMZk4ndl2K5au9tSlLQtWKxaFIRSA3h5od1gXddR5ovWy0dPVJhgbfEw3YTKttoXADbkUCs1rEmv2LUvjtS-PY_T7FSEq_uVKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداوکیلی ۵ سال پیش به یکی میگفتی پیشرو و هیچکس رو قراره یه روز کنار تهی و ۰۲۱کید و آرتا تو یه کنسرت ببینی فکر میکرد مواد زدی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84651" target="_blank">📅 09:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84650">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258be0442c.mp4?token=NoJdfns9zNgoAsEJZ73YLBvUyjr1QPcIhVB7Ew9TH1YeLmpBq2TLCPwy1Cq0_z2c1Xy1TlShyLK0eIhD1zQ2i7ol4RjSKmoQYOwP41nLCOdcZBNCuVRSPhuwPzTR2MJZeSaa3XDfURJMoaV82shPDEwz-hBf2b2zkctsqGFFcHrb6iUfashOhksnCEcErZyfAUGDHZxf8tPH9UjeGTro2PbJwHR8YAxyXTWdYDHw3J3Cw84obKORdyj5fFJ4mU9JTBjEWCJyh2w7xhnwtP3yfCnsuVhZ24EIUK51dbfmP9SDPIl3cLbBE6DDNFVvg5p5bcj-_PvnEhshviTNHUF2fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258be0442c.mp4?token=NoJdfns9zNgoAsEJZ73YLBvUyjr1QPcIhVB7Ew9TH1YeLmpBq2TLCPwy1Cq0_z2c1Xy1TlShyLK0eIhD1zQ2i7ol4RjSKmoQYOwP41nLCOdcZBNCuVRSPhuwPzTR2MJZeSaa3XDfURJMoaV82shPDEwz-hBf2b2zkctsqGFFcHrb6iUfashOhksnCEcErZyfAUGDHZxf8tPH9UjeGTro2PbJwHR8YAxyXTWdYDHw3J3Cw84obKORdyj5fFJ4mU9JTBjEWCJyh2w7xhnwtP3yfCnsuVhZ24EIUK51dbfmP9SDPIl3cLbBE6DDNFVvg5p5bcj-_PvnEhshviTNHUF2fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درمورد جنگ ایران:
آنها یا همه چیز را به ما خواهند داد، یا دیگر وجود نخواهند داشت، آنها این را می‌دانند.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84650" target="_blank">📅 05:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84649">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تو تنگه بزن بزنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84649" target="_blank">📅 01:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84648">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اوه اوه
روسیه تا ۷ اوریل سال ۲۰۲۷ توسط امریکا معافیت تحریمی گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/84648" target="_blank">📅 00:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84647">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhTIol7WxiWmDrifXpbw1WW95DSkYRgV6arDb4masigCHzBYktZ8KP-_1eSZtAqkD8Mj1yIdYq37VaQQqslhhSBLqVMBiso4mrc6grPOwLh1vtYfCL1FxPa5yZVAo070mbX1SgcEvfbIfIyHEw6gIYSLqqTaHaICMQvi-YSdl6m3Xc_LRcMCewGTk9B477WV9NMrnH3z2egDO6NNiKPU4LMDT-v8qEfYYUIPw4IUo4qYYCqA8bJ04E1vNx7xqSm8_aYUhjn3hxeqVV33MSTXbQ__tvm0exR76FbZjLitNu6fWfe8gG0FDtszxZHtjbzgFFbqWR-I9cC3hL2N1jqc_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هی داره یکی بهشون اضافه میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/84647" target="_blank">📅 23:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84646">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uio-bG79phUKW3Mys5cMFRQkYJwPPuXIoL5spimFDeaR1QrFcdfUTe7i1So3xvjMls84Sg4soO9hz_lN9uwGwNW4mMprrt0FKHK_rIRWtZa3kBDhMCifyenhqmdVHEdwsYqepqINFqpQcE21WXA3tQ6puIuu8f30CqwwKS4rSNYJOf0wLB5JAgLgwSxdehR4KXILpiTj1DOUdkH0sOLNrSkJOW2I-R7lGlN08qD4Nc-dJ2MxfvtUq92kjq2BxdVvKWKwjQKYGwnWr3_gMP4Hptm26bSpZCxxP7g7b-vB4UVCPn48mWF6Bjt5q3nWMwVMgUk4Sk3-EBetyJuv4y7ErQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان فعلا پست ندارم اینو داشته باشید تا بعد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/84646" target="_blank">📅 20:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84642">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pwvdskOYyTLggz36EEzWB-Z0KZzSNBmI4H0qVU7vz8qMOLE88kXEkF5-1jzQ3NpqZAoMaVvVpb5BvBXnaPPjnWBRyGwI-cjscNOsLAnrOPcQl9pTAfKj15E6EDfZbJKvywtrTRj-L5faZXqOuSp65lUGAL2QdgSQvBMM8W_Ogu3zTEY5VF5zGOBVP8nEph89tzqI32mW51yJVq4Xl98GglxjP0k1_r-uzRg2Jx3at7HxtNny6ZA8gZGPELs_znKn4zWy0g3EWCjgvBLrK1cnXMLTrquDFtjjQvnfBhGT-BbmXyA3EjC5sPfC7vYI_qt-5KLz_2JAEhQ0wOuovW-D4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tXa-a82WYdzHzJfV-9EbqPcNbDqjWsZUezCduCtoPmMffKY0pDHIzbMOxBobcIWi_36YfHIXq5UdMw_mwUrS8cZAF5dM4RFzIIfLvPzQ_tOCiE0kEinUc5O_zA0H40vMEEIqtW_hiIQZxsczLiexXfczvXtn5wsluOV5Z3b4xRHGgjfczEopQU8OrxmzwxxOW4Ngl8UywRPN-gJJujwCg4HKLv8nh4Hit6E7JnCa6VyuvsMzwKD0gni2cx8K7jeepSNo__jHQ1ayV4YX6s0ENr-06UkewzViij1CxKPZz1PXjR3mOKImzPaQ-6-bEjP3e-NgKz-7N8ylkCM6cEWgEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J1b7qRsQ3sSBkfduzprv-VHa6EVFnSRxNdgloXAtHEKUF_AbNbKQLn8WjYqfGqLGDfoT0bTgrMChW-6gnt4nn5H2daNY3RPTxoxUlGqZ-yg0ikRVGaH6NIYqhV5b3KvKyhW66LzQw2vlWPl5eWjGw7MHV3NxATIl9DwI7YNn3voAljgi1JdPzzIvWhNJZBEZerI6s7wStyoSOBFi61L-9ca4TMXH7_REhcWGFHDRxmjqSh2yAEFjfr77JjPuXcIv4IZokomh93rkCxURI4CAZgl_3oeqg9vSzXdHfZYDmpXiPZ9YQTP31eGtVd-WoZ-vcH2MEWAMyf3meAq4zpIlFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v22yKUA-NOa5-_586HGgs5bYMga11XnBo-3bTiK-vX_G-CF9TC-iCt2bmfQy6dv16clfPBrAzRiMGWzghn6hRtdknQ0JgIWDgNEVjmhFXlEXOcQ8H1NqVPKYiwQaC_0PfX8QZp3A-mB-EeHth4w68dRqdpDMJTyQvwrNM3SXvx3xj01XpA8wNIy9A7rmUBFxsuLsm_kdutyoX56vb1FIrdMF9YOUgfAOaNLhpK4aLbJI05E2q8rcb5vhrxQZedNA8v0_f3AkRbtvPB0fXGb-5ORU7keLtExA4XR9t9wfXN0iNq5d8W9cwYsvz6yrYUiNuHLIKaXp4k7rb7phjYU9wQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همزمان با ماه کامل بر فراز آرامگاه کوروش بزرگ، این اثر هنری زیبا خلق شد:
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84642" target="_blank">📅 20:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84641">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZl6K8cc5Bz_K-AwjY8x35Hw3oMLt3jX7HKya_bJ8sowDX5oETttIvdR74VRedD_rXEoFdjRgYXQpHfoK3lPyxqVygRd3qKqwhqPQukDVzJfCJFLi0qTIUCRI16vHDLGih-r5WfW4UGmApInInd7otf9A-nCIdKOFjulX8pHQn2qLHiXFNaTlXZ1RCzqj7xUaXGR-i9EgETU90-YAQ9rjdiA65i4CBIkyhNkSCEDj-rTBTUqi9cOmew_hpWGj9zUfeOcvJAto39DCkpmiagS6fck1lPpQj7Iw_lxT2at_RU4JnyujtEKw7R7fQT6ZvOaAmELe4HZRAmlMkx_u2o7zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چجوری مصرفمون از خود افغانستان بالا تره؟
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84641" target="_blank">📅 20:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84640">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4nGCjklb1jYnbWSZw8e2i-mLGiVr7bioqpDdI85zNDw6lXp8417YtCQuBecsVfuJF2KWl5sxK7_zDLzu79M8KSeI0v8nQWhddUyFzgUl1f_W6l1D_ZWSNySGZbVNNWSYaUdvabUBu28RSNJizk8HsxsxRl1AzT3NjCF5RjXXC_iybxX8nacm6fr9g4ZxuXQpipm2w-1Kp1lg32vSzBSeF7_0m2qi_E2bVecPn5j9LAbZidpbTXFtjRUsoEdI3s4EDa6QvmdTIsMNHv9Z0aNn0ajNiJe1BGLzdhBpPwvvC0rQ9l8s1TbeZkn534Z1qL7TqT-818dMH9CM_7G7liylg.jpg" alt="photo" loading="lazy"/></div>
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
G17
🅰
🛒
ورود به سایت
👇
✅
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84640" target="_blank">📅 20:28 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84639">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDQE8ACHBkkrFdPzpFm4zPFry8-hoPzsCjlGFaPAQMzSy-Z_qbtAUaDJCqm786DB3F18SmSqdGkbgtGRna-3itO07G9CEGZLjrYbQWlnoM_pn8TXVsEQPak8bvfW6N3yVcxh2zbA3Iwu08CBk9h4UmLKUObWJloCnkux02iNMSV0jjMFRoc2gdXxWhzzHYyOrSQGQ_7QBQIZE-9joVTZqyEe_r-EPQIvYZKwvt0jV0LiCrBkUxnYIldQAfrxXiyUBx4vOkSt1Ydei5iDeQQovPNuYQlPlhW9PJofyoSgjF-dYHRMPuqLK1KBbY3jzE4E56c0Cc4G1b670b61DqEWrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا خودت رحم کن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84639" target="_blank">📅 19:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84638">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fg2nIHY8fNs2v5qzfqQyNl10TGdmmqm_M6h2oUvMGWHyhzVvRHJJQ_8XUWaTRfXn1V3-i3EbeIiuEnu6kBfaGeiWvPD6JuK9XCf_zhY6W2wRXg-N3eZy0wUUlwStbaL9m71sKv_B8KoDkmk7AtnecpdjvFEKhGEbgDz5lOxXnkqoXEw7AdeYiA6ebOD5eIaD5h5sEX2vRpWTP4cHT6HZ_dWrm3dhyC6nuKE5_ujDmyrbAbNoGtZofYN2Duu9CilAXvnb19B78S5tDN4Wj4yV_MfRWuYkXTclU8UM8vQjcq41j-EnykItrUnxfCvrZZztr3lO02k3WAJtZSdYrZAuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجیب ترین چیزی که امروز دیدم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84638" target="_blank">📅 19:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84637">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دولت آمریکا در حال رایزنی با پاکستان و ترکیه برای بستن تمام مسیرهای زمینی ورود و خروج از ایرانه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84637" target="_blank">📅 17:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84636">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خدابنده‌لو چقد شبیه رودری بازی میکنه</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84636" target="_blank">📅 17:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84635">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گزارش‌های اولیه از کشته‌شدن معاون اجتماعی انتظامی استان در پی انفجار مین کنار جاده‌ای علیه خودروی نیروهای انتظامی در منطقه چشمه‌زیارت زاهدان حکایت دارد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84635" target="_blank">📅 16:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84634">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">میرسلیم، عضو مجمع تشخیص مصلحت نظام : تیبا در سطح ماشینای معروف خارجیه و به راحتی می‌تونه باهاشون رقابت کنه.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84634" target="_blank">📅 16:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84633">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84633" target="_blank">📅 15:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84632">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بچه‌ رضا پیشرو یک ماه دیر به دنیا میاد، ازش اجاره میگیره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/84632" target="_blank">📅 14:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84631">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVeohXm1nZvxYqWjIfWjFbX1yjqb4fM6TRMX7fobxeuYF55zS2FmHkFmnjNFQB0qK2xY1sHcMhOfH12rgYWDsW9xsQCL11I_K4Zsq-8tMucydzu549gDtJgaG_9STlTYFPRMkqbWvbkXYLx0JvXvRvVRMb7ExC8hdsAjujlipi1JpQUGtXAUrZ76J0ZzQJQUXnC9KjHcmZ5P29eT_Q8rmNyQdxP1mgqQRI8YjG0Yg4rlZhpC156RWtG3IIp9EcQBXfNwZT2aF5Ybp2cpj87LWdb2Un4I2iU_vcqx22AfW6tyTecjFRv-UjVn-omm7RBkyoMy7xLrZAnHdbN7gQ4GIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا حاج اقا
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/84631" target="_blank">📅 13:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84630">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سر همین اصلا به مشکل خوردن، پیشرو زنگ زده بود به هیچکس گفته بود داداش مالزی کنسرت دارم، هیچکس گفته بود خوش بگذره داداش</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84630" target="_blank">📅 12:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84629">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سر همین اصلا به مشکل خوردن، پیشرو زنگ زده بود به هیچکس گفته بود داداش مالزی کنسرت دارم، هیچکس گفته بود خوش بگذره داداش</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84629" target="_blank">📅 12:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84628">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">من اینو صب دیدم سریع رد کردم گفتم ای آیه</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84628" target="_blank">📅 12:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84627">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromᴀᴍɪɴ.</strong></div>
<div class="tg-text">من اینو صب دیدم سریع رد کردم گفتم ای آیه</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84627" target="_blank">📅 12:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84626">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQZe-phb73PUWPR8p8v7P56W_PTMDCplyxv9OF42zYOY-4vzOdVFzROjZBo_-vOPXpgDDFmddvD_7PSUrNb8dbZopgklanMEpfcx8gx9_WPAdXuX9baO_eN5dJPbbqtSIpGyR1-00PcexbHGDx2Zg8WC5zGHNVG4Pz-rYA6eZtEhfJVIls6TAaGiLoX5Q0XvwbyiJ4OyFPpF7pMWEBqRmj0ZQd8rUdB7dg66QKyhvi95Zzz-3GtWiF4k09J9qpKcBmnmxgbAOkU6cDQO5vq-5gyIt3_Aen6HLWwFdQiRzVp070DgN7FT6TU16XFSpSOWXLRO-6Bl47pG7V8NH4u5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا فک کن فیت بدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84626" target="_blank">📅 12:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84625">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">هالند و امباپه تعویض بشن بین سیتی و رئال جفتشون بهترین تیمای جهان میشن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84625" target="_blank">📅 11:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84624">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWHcTkAPTKAEUmAO4LpVoVxz9Tly8Lh8tCaBJx5Vb4_1KuH7zzLFgBLgCW0Vssfl1A4JJiRHIAbvCktjxYmWk6r7pvFE1-D1uNwDjN-fpGCLn6a78TQXbKh0y2Qt5RJZYHArF7FAtf19-t9RBcLcCP9SRN7QlbHrbISgvicztrk4hC72fHldbV5ZEXKMxQVoKXoZJ5gBVdrAuZL1G8XtT2M8o6sg6ftnuhLcBzzHytEoB-gSXdDbKcKH7mksEEzjWqNaqwmvpT7qPBZe9pP_O_FaOOSLaSxzm5d9c1F3gHF2lG7vl1SFWptwL1_Q9jUNxvCy3B5eQOHy1c-0yntMPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس داستانای کیلیان دیکتاتور حقیقت داره پسر
آاس :
امباپه توی رئال هیچ رفیق صمیمی‌ای نداره و اون توی رختکن رئال احساس غریبه بودن میکنه. با بلینگهام بینشون یه جور تنش و سردی وجود داره، با وینیسیوس هم رفیق نیست و با بقیه بازیکنا هم رابطه‌شون بیشتر در حد کار و فوتبال حرفه‌ایه. حتی از بازیکنایی که قبلاً باهاشون صمیمی بود هم کم‌کم داره فاصله میگیره، کلا تو تیم کسی با امباپه حال نمیکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84624" target="_blank">📅 11:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84623">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9NTy17yxCWcH4ZmCN5QraxijmQuVOmhoO1zTVW-aMPtRFMcdn9MNeX0K5rC3NPPrydclpSWsL9ZH81r1JPO1-xnvN7mxKD3IzoN5FEt4g-0TC2auU1EG6Ov8PJcQSk2bPMVmciPVXSnK42lRFNwkOUlSwqS_ANWcgIZizPFgEoT2b6gvP_0RAm5CbaHeIx0eVxBCpzFbNPiAuiTI_JstehQfS_-DSGb8sW1RGiyBs9KGrOxD2RKU3zEpdLezTazUG8_eqTYcAzBxNG7-WLSZrnXLB3wEpQiZ59ElMvy8ao2qfbnSAishuii2V65IHRKN6XtLPFbPtl4Pc061cBX4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مستند تک قسمته ۲ دقیقه ای(یک دقیقش تبلیغاته)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84623" target="_blank">📅 11:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84622">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">عراقچی پالس های مثبت از مذاکره با آمریکا داده، شیشه هاتونو ضربدری چسب بزنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84622" target="_blank">📅 10:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84621">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ویچرت؛ تحلیلگر معروف آمریکا در توییترش: اسرائیل دقیقا قبل از‌ انتخابات آمریکا به ایران حمله میکند. این پست رو‌ ذخیره کنید.
پ.ن: این یه بارم گفته بود آمریکا لحظات آخر جنگ ۴۰ روزه میخواسته به ایران بمب اتم بزنه که ایران میفهمه و مذاکره کردن رو میپذیره، قبل از شروع جنگ ۱۲ روزه ام میگفت دیر یا زود یه جنگی بین ایران و اسرائیل اتفاق میوفته
پ.ن۲: آیزنکوت رقیب نتانیاهو در انتخابات اسرائیل هم دقیقا همچین حرفی زده دیشب
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84621" target="_blank">📅 10:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84620">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">من جای تهی بودم دیسای قدیمی پیشرو و هیچکس به هم دیگه رو جلوشون پلی میکردم و از واکنشاشون فیلم میگرفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84620" target="_blank">📅 09:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84619">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfWqcn6NPvyaZhgynERqdX0ZzGN9HS-d2r3v77OVfxhJNII9okO50Yq8YEPi_nAI5i4Xyj9QLRbX9x_efSNTHnNtzQ97NlnbJ3D6ikfogIWMTVRpURtGIl3If4nSggo39aQig-6M0LF46ijdAdGEEJLeADbqnS8hu-tBQBp9K4W97gOJIs6hvWeR3kJXOq-ilG88EchPwN2w57jqy3kJM9UNE8SnSo6uzQ8iMw22eczbUKf3M6lWYw1lr0x0uzfoeB00Af3hM4Gr7x25ZprHcSt1sRAI-P60W6FUDGdHOYQWy4lY8XFNMEfulPEEK3aiQkTdh9OQG2_ytXj_xZpS1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی کیر تو روزی که با این تصویر شروع شه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84619" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84618">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84618" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84617">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tps1ZCeoI9Tr-VnXwBW2YRyWn_fLlkS6lq2cf6dlVNB96LNPXtqM04b3ZjKR5-T8JQrwwF6u7H5rmzUCC1fd9ey6cEz1ehRwDsSiXAI2ZHE5zze2wlsRxejqX8lYnBV62VVOwd-akjMIRjUsn__e_Zby1Dam7RWAPOyCrFg75CuwXPjXZ8cl-f_7sgeBdv9fNyBn9IKGvakgGeZPO7be-hUPR_K8H6jCYAvxNs-OtSY3GKJmauqmAntLVyzjNEP-rX87mPEEbRTs7Z7g9pH_FBrx5rOkf55Nq5EiQpA_7giuWn369zb1y6gDbaxou0lZ1-5PsgpnZuUJAGhk5fFssw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
پرسپولیس - صنعت نفت ابادان
🌎
ساعت 17:00
⚽️
چادرملو اردکان  - خیبر خرم‌آباد
🌎
ساعت 16:45
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r17
🔗
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84617" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84616">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=KXv7OnO4zM6RLB6-nNGjVy_NGqar0hWDPEQ0VJw8cqbYDFFrJ4JdQPKqHdqlA4U1mSTAF0PiLypB5seJEA0xgFVl47OBtVNq1FR2PtFMNjc3kcxO2mcJojQYmCGvT2iDbhebcZtEI2YaVgP-0uKn2CJ-MYylIdiwiNy2dMeIcNrbX-v4Mg7N54XsVu6P9lBHDJPVQRkT8dFXONHWetA6TKtuDMuZwM0TXdZKKPmcZdDY7f8PgVht4hqB_Pr9-l19TcaGqE9kpsmIP99KJr3AIHtnDOA1ZvDcjod1Qn8PFtF_eD1TYHuJnpWjEFRhzEuY_UbTsz4DtsMB1X-OGKSKJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=KXv7OnO4zM6RLB6-nNGjVy_NGqar0hWDPEQ0VJw8cqbYDFFrJ4JdQPKqHdqlA4U1mSTAF0PiLypB5seJEA0xgFVl47OBtVNq1FR2PtFMNjc3kcxO2mcJojQYmCGvT2iDbhebcZtEI2YaVgP-0uKn2CJ-MYylIdiwiNy2dMeIcNrbX-v4Mg7N54XsVu6P9lBHDJPVQRkT8dFXONHWetA6TKtuDMuZwM0TXdZKKPmcZdDY7f8PgVht4hqB_Pr9-l19TcaGqE9kpsmIP99KJr3AIHtnDOA1ZvDcjod1Qn8PFtF_eD1TYHuJnpWjEFRhzEuY_UbTsz4DtsMB1X-OGKSKJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو و تهی رفتن لندن که سروش هیچکس رو از نزدیک زیارت کنن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/84616" target="_blank">📅 02:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84615">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVhHUvoV-txipgjTkXOOnckyIrZRXsz2UnaNB9GUgzqBByH-y3ElIqwzuq30Dlo7QE_MXUBV6QasovEXoQwB0ADSYkKo939W1vCSYkNPsegwo59IvYpO-HuVWRzaQnUfMJd-VDWPZQy1_Ie_3WRxWreImijuOL-JYqqlwB6IHbug2LJhP88Ujt_aNtuhuWZttYcd1_smQXW5sE9zHs6XvxbmYeXK3-KTs--HjcMeMHe1qM-zAzBGbvhMdd649IMqce7XwjsR83Ft-bsF08xRqHq2fdsCzN4R41eisjSvt4EqgMhim_aA5VADdc4SVujCC9ERSlgIWVv50_TPdjoLjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز شیوع طاعون تایید نشده؛ تو ایران شروع کردن ماسکش رو میفروشن.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/84615" target="_blank">📅 00:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84614">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سپاه به اربیل عراق حمله کرد، احتمالا هدف مقر کرد ها بوده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/funhiphop/84614" target="_blank">📅 23:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84613">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اجرای جدید هیپهاپولوژیست
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/84613" target="_blank">📅 22:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84612">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16fa565c7.mp4?token=XRFRNtMkmJ2T0AJQlKBhx1IX3RyNm8pJaQA-23vDMXgiGd_eHoKdl6VWq_-Hf3cWHrXBrRQOuZpn0fF2If2Ou4lUyn9rFDxEEbbP-d1V2vXKmkDa4sHsHH9rtrJGqKREa0HMzPGxNkDOYOdkKYMpdrVhOFtkUK18j5gkoyCoCjxBudyfjmzR52r7Naj90XQoBe0lAV4I9iZ02TqoyD1hid3Zc6IA9hqG5YwwNioEwZBe12sW9o9lAnLI9jymzOaEFdNitiSiF1XdpETHvMJS64AE7zM2p01J7ZM3RHanyaE-Q6jH7bcYy-o622WiPKVx-yhg3CwI80qn7qo9d6yJEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16fa565c7.mp4?token=XRFRNtMkmJ2T0AJQlKBhx1IX3RyNm8pJaQA-23vDMXgiGd_eHoKdl6VWq_-Hf3cWHrXBrRQOuZpn0fF2If2Ou4lUyn9rFDxEEbbP-d1V2vXKmkDa4sHsHH9rtrJGqKREa0HMzPGxNkDOYOdkKYMpdrVhOFtkUK18j5gkoyCoCjxBudyfjmzR52r7Naj90XQoBe0lAV4I9iZ02TqoyD1hid3Zc6IA9hqG5YwwNioEwZBe12sW9o9lAnLI9jymzOaEFdNitiSiF1XdpETHvMJS64AE7zM2p01J7ZM3RHanyaE-Q6jH7bcYy-o622WiPKVx-yhg3CwI80qn7qo9d6yJEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوجی انانوبی بازیکن بسکتبال+۲۱۰ سانتی نیویورک نیکس رفته دایرکت یه دختر ۱۲۰ سانتی و میگه بیا ببرمت نیویورک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/84612" target="_blank">📅 22:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84611">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49025c86d2.mp4?token=irl1zDB0T3zvMtjQo0bBolxXWIDIVS1xYmgqCMRQgsKDbX59dc31egR8uADEBRoKkTFPfPIlQUMQbfDZpzIFmKsBePWwLgsDM8glo2_y3Hu9NLogLDocRI5QT4PAvmzECMLmXpwxxPYb8LOXmkY-OezxNzbI5yHRNFoJGxudgOLmznExtBWEYlQP9koPgmgwVVPPF5Ec6CQYfNfjeF_eQUQ0DGrD_8B0TG_VvrmgzFtAzQ7cSXxCEIm4ACsqIL5L_ura3LYRZ_POuXcN-HgWqYbbUO5m-leNRhcoTkvKhVejV6X9KJVAFOBHeABFzL0p6CinxQL0NKz0XW0jyZG9kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49025c86d2.mp4?token=irl1zDB0T3zvMtjQo0bBolxXWIDIVS1xYmgqCMRQgsKDbX59dc31egR8uADEBRoKkTFPfPIlQUMQbfDZpzIFmKsBePWwLgsDM8glo2_y3Hu9NLogLDocRI5QT4PAvmzECMLmXpwxxPYb8LOXmkY-OezxNzbI5yHRNFoJGxudgOLmznExtBWEYlQP9koPgmgwVVPPF5Ec6CQYfNfjeF_eQUQ0DGrD_8B0TG_VvrmgzFtAzQ7cSXxCEIm4ACsqIL5L_ura3LYRZ_POuXcN-HgWqYbbUO5m-leNRhcoTkvKhVejV6X9KJVAFOBHeABFzL0p6CinxQL0NKz0XW0jyZG9kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرقت غذا تو یکی از فست فودی های کشور:
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/84611" target="_blank">📅 21:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84610">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f08a78a31e.mp4?token=Oc6q9kwl_rxdjuasQj_MEaxlU_cqcu2loK50u859oW1XNDWAfbBskdoQLbiXzssJuEGaGDNfnb6BvznD7t-FDpcfZk3JC4_XIKw5bDPJjAFFDVtOoIaMN2MHTBEj9rD6HyTMWrcdF6Jp4rDIWCjf25CPu6MBmGIeNjPTa7-7oE-Glrp0eMNPI7urOiAWr6Oc3KG1qrZIxgkcoOxGjoWVzYKTS1fGyya71ClpzrgvP6jK5FwlaD1VbywFBK5Pswo4x6ROfEl9ZxlHeGdAmAC4BFOgrhqB01BkIl1laE94jEzvXCfx34kOuhuk7DS85xr9yrQJz9HaVgy-MtQ3ipg6RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f08a78a31e.mp4?token=Oc6q9kwl_rxdjuasQj_MEaxlU_cqcu2loK50u859oW1XNDWAfbBskdoQLbiXzssJuEGaGDNfnb6BvznD7t-FDpcfZk3JC4_XIKw5bDPJjAFFDVtOoIaMN2MHTBEj9rD6HyTMWrcdF6Jp4rDIWCjf25CPu6MBmGIeNjPTa7-7oE-Glrp0eMNPI7urOiAWr6Oc3KG1qrZIxgkcoOxGjoWVzYKTS1fGyya71ClpzrgvP6jK5FwlaD1VbywFBK5Pswo4x6ROfEl9ZxlHeGdAmAC4BFOgrhqB01BkIl1laE94jEzvXCfx34kOuhuk7DS85xr9yrQJz9HaVgy-MtQ3ipg6RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من هیچ کاری به این که رئیس بانک مرکزی ایران به وزیر خزانه داری آمریکا سه روز وقت میده و این که دقیقا برای چی وقت میده ندارم.
ولی چرا میگه ۳ روز بعد با دست ۴ نشون میده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84610" target="_blank">📅 21:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84609">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d8dc7bfe.mp4?token=KYNKrCzklQ26wxj4fhNA9qKexZsbK88zvQFFuzIAVjw57HuNIHMIwyfzo5Bd24rA__9JBqh2aII9spfQCNRMaITOoKtpE4yJUfcfhnrYGR44vBEYxKwluAHVMLmMMx9yocAQpgH9VmRsD4ex8E-1qZT_FK0nD60fKOk6jhZAmjpErJw7Y29_p51EWZtjIFZENrj53ByaGydshD_mBqEvj756qBnXt69iscgCVf01q2qHnwQwNFjQ2unjlzu-nKMtQMOUexr0JsqF73ZJDgLAwC9DqlygEcZsnWuyhll_Kmx79VwISLpzf5sn420iSyHooCUtSfvJYLEE2uhYQAQwUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d8dc7bfe.mp4?token=KYNKrCzklQ26wxj4fhNA9qKexZsbK88zvQFFuzIAVjw57HuNIHMIwyfzo5Bd24rA__9JBqh2aII9spfQCNRMaITOoKtpE4yJUfcfhnrYGR44vBEYxKwluAHVMLmMMx9yocAQpgH9VmRsD4ex8E-1qZT_FK0nD60fKOk6jhZAmjpErJw7Y29_p51EWZtjIFZENrj53ByaGydshD_mBqEvj756qBnXt69iscgCVf01q2qHnwQwNFjQ2unjlzu-nKMtQMOUexr0JsqF73ZJDgLAwC9DqlygEcZsnWuyhll_Kmx79VwISLpzf5sn420iSyHooCUtSfvJYLEE2uhYQAQwUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد.
از این به بعد در سراسر کشور، با خانم‌های بی‌حجاب برخورد و براشون جرم ثبت میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/84609" target="_blank">📅 20:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84607">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6f2ajyiwCGt__iMQV3QIK07o5hk5j0hicei1SlgPEH3WQWfEBI8lQuvRc1E4X9j8WJrzZ9ooMTquQ0MDysjC47h9P7pHPIr_v9EzTVpBBI-g7nxlUqA9Ppzoe0nPZQ4ZCKDt0DyTfnjI2m-F0O70KufLEbrg5ujNsHQEnKjqZCfI2CbIt4Lc4FvCVGWFmKQ8HPlan30iP3qA2umuiEaQ-UQ38XrPMs1L8nLQd-Tc6ZTd4GpxzPRgprOqqEpUYFHcNNO89wCMD_7l3UrWWpNULSvABF_81fd7S5aGvluw6Nd5sCLSeqvjJkSWPcO_n-yUJRKNrChFHluKBIkniM9sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان پاشید یه جوری شیشه‌هاتون رو چسب بزنید که ذخایر چسب کشور تموم شه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84607" target="_blank">📅 20:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84606">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBpWIQCcPMKW3QbQoVdtOZWpIMzJG_MlQslK-3W7PDSVFIBbxzq_jsmVJt34_L7hM4kIwxLa3RXDQBMp6raL52G-Q5KFkzgoZHh6oHWf6RTZFt4Zh4imoduYSCrZnB5npNKv3_6HFd7M1JgokyRpeHLti43QgdXJxEVQCvHVZOZQF1zK7v40JfhRTPUQRhCrHqTUu0cqaY9hg3klHL1q5Mbk2GfWkoyinzUpgVgyiaf-ctMCbUwuJSzUUiN_tP8god9YuXUdVEZiIQ3ZmyGoPiaTcUMBewoCc8asb1AkaM-NF2X37vO-1SkPY_Upi-afOxwO8r5FVHHhLGPpsXw99g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خخخ
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84606" target="_blank">📅 20:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84604">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quNbaqU2FBTBL6Xstmaxg6XbWlCEDE8m7zK88AHAyNWIN-bZMJd7G9yBIRonM0hPxz_KD7BiLnh8_UegDAmgbzgCkBY4C9TPxKQuVs2rDztWCijAbl0G-No6DSjBN1jMGMN2iiuHBMfCVqTTugh30exzfmG_-xTA6-R1jLK2PQOcg6o28aGS4BbYo7Wn1wXqb0pEA1nwapB5-k-58NbqAH_N1N_GA2-q6DmXXv9_C0WkZTocixAtMExIQu9_h60a1DhbV7Hiqacn1HgUmG4mQEm4NswkYJJjinkaRUKxb52ZQjsaCuH4B_dzW0hBeOJMYcqTFeoPqQyHqeCfeqGe2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توماج صالحی با رپر بسیجی‌ای که شبا تو تجمعات اجرا می‌کنه درگیر شده.
(به نظرم رپره داره حق پسر ایرانمون رو می‌خوره
💔
)
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84604" target="_blank">📅 19:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84602">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ebbea01a.mp4?token=i7S-WU4v6noS5CObpktHhVKeF_X0yeBQ__qy3yS33c7YzkD4BBBuVoTI2l2BYfhGQOpnb2zKvAD8upEBGC5-bpy5u9w_zBJNo1pKoC5NAHOjrztOy1PYxwlRj5egLFU-ZJgl_TcNJ9GljgfcUB2r2tSmlv14OtH16kz_06lf3Ny68-03UQBiJczphFppkkV-oWUrPZ3tghGVOawfSDeCS1NriZQrjbEX3fIzCdUwkA2XeejrnDQGu8xj-vvbeCBoHeXsmHoRW25Agx_mVRkEnY6x1CZbantJCXYF92Qz3Unaz-XUBUTEezrQyD3g_UbcKq8cDjxqbpWF4QI72Om_nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ebbea01a.mp4?token=i7S-WU4v6noS5CObpktHhVKeF_X0yeBQ__qy3yS33c7YzkD4BBBuVoTI2l2BYfhGQOpnb2zKvAD8upEBGC5-bpy5u9w_zBJNo1pKoC5NAHOjrztOy1PYxwlRj5egLFU-ZJgl_TcNJ9GljgfcUB2r2tSmlv14OtH16kz_06lf3Ny68-03UQBiJczphFppkkV-oWUrPZ3tghGVOawfSDeCS1NriZQrjbEX3fIzCdUwkA2XeejrnDQGu8xj-vvbeCBoHeXsmHoRW25Agx_mVRkEnY6x1CZbantJCXYF92Qz3Unaz-XUBUTEezrQyD3g_UbcKq8cDjxqbpWF4QI72Om_nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی رشت رعد و برق جوری میخوره به دکل برق فشار قوی انگار که زدن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84602" target="_blank">📅 19:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84601">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد!
از این به بعد در سراسر کشور، با خانمای بی‌حجاب برخورد و براشون جرم ثبت میشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84601" target="_blank">📅 18:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84600">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">هوا الان یجوریه که همه تو خیابون فکر میکنن شخصیت اصلی داستانن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/84600" target="_blank">📅 17:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84599">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حالا من که میگم استقلال یکی زده به تراکتور، ولی ناموسا فوتبال ایران دیدن نداره</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/84599" target="_blank">📅 17:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84597">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">محسن زنگنه: قراره 110 هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/84597" target="_blank">📅 16:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84596">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">محسن زنگنه: قراره 110 هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84596" target="_blank">📅 16:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84595">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmV-rqWjKggMoqmqgwZpr_lV1tRWAQZ54H4OWjcCAbVYjP3NTnNs7LcAmtRYclh4qeoxp2rlcM9rhNZrPGYZPh3CSsFE7ct2vU6aGi-wki_HxuMtXtxURJ_Ki6abMAgFg1Q_a4Lfe5lScvSct6ZstE-OTsPrs5tulYGR0H4tPXeh7hYgffB5XtI9POgJB8yRYXZFi5ZN1nhd6yJRdK1sA41BNOIgQbfKU5__KhRwxHd4caevr1tNUSflO-_t7rHEw3xq2_qU82PxGyElsvTEZDEDkTp9RVR1s771AGpyI-_6xL2MMehaSg1_GgPLHehXCwgN7CdtSSZD0pep9WZskA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر دلو فوت کرده
خدابیامرزه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84595" target="_blank">📅 15:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84593">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJ9x2fitrQ0WcBdMe3D8WTfNJF8L_2_WPDovrKtXyJOWG5TJWVfAcFsjDb5oCRiwECrQneT6HU7SI6UT0iaXM2MVm1k0SSZih5ecX5J38qElhas_R2wVoARjqpvxKa24rUGKUKf_d1VPoMR3Bd7lHyydsN4t7cHrLkKRpRU2l45F-A1ErPBEEbukxun87M1ijEdK0tpdyMvCP_Mml38yN_X1UT3CjP3qqWeprLXOzyyLzhex10dZb5Y5iQ_IDltHtVO7YSSvpqTJ2bkPrjcnVL02Xa2KSOeqPK02ioJ9HENRqJvIwVkUjyG87I8NjEm7HxJ87BVJ0zEm21RqVDJYtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T1_eneOjXyyPaGBSbgTtotDQhPIHhBeZNNNgSiYQ4EtFYW18F55BpE3aetXr7RailUyxnTp2w9gmTwmM1jzf1nmN2ciC49dCIIXTA31iuZRu2Bl2VnoEIgi1GtcYakfocDfu8hXY7LBYKi9ZVHzboMCg_y_UtrmeDjMKEvR7X5OvVxEn6BOZDtyDmdH9h-pBAWm5fNqWQR2rgoZd7YzZ7kTcifp4TodpZ5J58912o-zSfaVmxHqXSRc9vzay7Ahe8kpkmiH7tLxfJHCiBp7HaOkPVRWvps6hjJNK__DYDnfUq4oyHMGVgKA-TQ4QKK7VkpScMBJQUnoAPAkHUxX8CA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشتی ریدی که
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84593" target="_blank">📅 15:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84592">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مجری صداوسیما:
گاو که دلار نمی‌خورد، پس چرا شیر گران می‌شود؟
کارشناس:
اتفاقاً گاوها هم دلار می‌خورند
عالیه پسر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84592" target="_blank">📅 15:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84591">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cac1e3571f.mp4?token=Z3vv0SoizIKW4LVKlHrvW_4kKR-_5sHxHGF0rMOFfbjd-6_XWEVraTMNv7jjKc9Wwj71RV2ezaC8mepBvmZiP_y5C3L50tzslvRYf6ZsxgyF6nGfFzoyvNZt-IRh4SapFqL_vlxJEqh82ReG_w-S8WlpgacIDs7IhDYiM4lkxU_SAP8Gj_2Z9dUYCkKgbbvf_mCCvNgnqsQqljRfE9EX7XvXnvXqepAsCrVjBRM-T5bgCT44RVtxMyJoqBIV93DG8Piue_nV5yStpxRuqgUXMAsInRT0kNPAJWwgnTaPc3HERV0jV0PIeS9VGL4wuxLX8oH5rvLhy22eBjl16fGEFg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cac1e3571f.mp4?token=Z3vv0SoizIKW4LVKlHrvW_4kKR-_5sHxHGF0rMOFfbjd-6_XWEVraTMNv7jjKc9Wwj71RV2ezaC8mepBvmZiP_y5C3L50tzslvRYf6ZsxgyF6nGfFzoyvNZt-IRh4SapFqL_vlxJEqh82ReG_w-S8WlpgacIDs7IhDYiM4lkxU_SAP8Gj_2Z9dUYCkKgbbvf_mCCvNgnqsQqljRfE9EX7XvXnvXqepAsCrVjBRM-T5bgCT44RVtxMyJoqBIV93DG8Piue_nV5yStpxRuqgUXMAsInRT0kNPAJWwgnTaPc3HERV0jV0PIeS9VGL4wuxLX8oH5rvLhy22eBjl16fGEFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز، ۱۶ مهر؛ روز بزرگداشت داریوش بزرگ، شاهنشاهی که نامش با شکوه و اقتدار ایران هخامنشی گره خورده
👑
داریوش بزرگ در سال ۵۲۲ پیش از میلاد به تخت نشست؛ در حالی که شاهنشاهی هخامنشی درگیر شورش‌های گسترده‌ای از ماد و بابل تا پارس، ایلام و ارمنستان بود. او طبق کتیبه بیستون، طی ۱۹ نبرد مدعیان سلطنت و شورشیان رو شکست داد و دوباره یکپارچگی شاهنشاهی رو برقرار کرد.
در دوران داریوش بزرگ، قلمرو هخامنشی از شرق تا حوالی دره سند و از غرب تا تراکیه و بخش‌هایی از بالکان گسترش پیدا کرد. او همچنین فرمان ساخت تخت‌جمشید رو صادر کرد؛ یکی از ماندگارترین نمادهای تمدن ایران باستان.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84591" target="_blank">📅 14:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84590">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نیویورک تایمز:
پاکستان به کمپین نظامی عربستان سعودی علیه حوثی‌ها در یمن پیوسته است.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84590" target="_blank">📅 13:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84589">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خیلی دوس دارم صبحتونو با درو دافایی که تو اینستا دابسمش میگیرن شروع کنم ولی اکسپلورم کلا شده کچالویی که باباش داره مسافرت و بهش پول داده تا ۲ سال دیگه برگرده ببینه با پول چیکار کرده</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84589" target="_blank">📅 12:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84588">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UR7Cm4BRUGEWICIUYYwAseb1HrNEfpWUKWQBQwbUytUazOKwORZIO1Vn0nTMf0FnxSE0y3rPXCUx0kJnCnINfZkXr5qQr3SMjauyNcviiRyM6wvNaY04oNueErhHUmcjOKl208NbNY4YYeDsqP0TW3m2fsNIRTm52lN3qEGvozpzoVpxh8hTVCNAz66owXSi7K6dUHk2Uz1y1wOpBC_TjAXoj_nCEb6kvXpJ4g0igMKlmf63RdYGxVEBBP-8fqdHlwZithhY9mlyeCFDGS0Kup0TH3xPf7oUkeupO4CsIzQg3tD0zEQemh7tE3kYy8E9uAQ3C6lT-iTmyxgh9WzI4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84588" target="_blank">📅 12:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84585">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خیلیا تو بندر صدای انفجار شنیدن حالا معلوم نیست چی ترکیده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84585" target="_blank">📅 09:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84584">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وحید جان بیدار شو، زدن</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84584" target="_blank">📅 09:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84583">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4894c49154.mp4?token=fMM1UqRnSnjvlIh62a3rV5Q9glyxL3pwJ5uOoOzBwh4NBdgKfjAGipWQkdmHUDMuDLfnLYCjxwP6DAcBrhNAi_-UaYQuFSjoEPV6UjpMcN1nEleXQE2tNrJKrBKG_cpVuyRrK06BqMdmA-iLmkelF_BN8WsZiKCNjqrpfiMbWq27P3CCbRlnuVRIqfzutLgSyg9zqS8wWiuDFkh2k8OtaY2rtLpdsSYP2wqc9efFgMVPjcLRbSGu_ELBP0FxYTmvixnzee054fAINufEvsg0vj2H0xrUxFVPPNwLjQauT-I9-37cuTMhpxN7HYHvg5_WGzCfWx4TehdMFMnpqg_ABA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4894c49154.mp4?token=fMM1UqRnSnjvlIh62a3rV5Q9glyxL3pwJ5uOoOzBwh4NBdgKfjAGipWQkdmHUDMuDLfnLYCjxwP6DAcBrhNAi_-UaYQuFSjoEPV6UjpMcN1nEleXQE2tNrJKrBKG_cpVuyRrK06BqMdmA-iLmkelF_BN8WsZiKCNjqrpfiMbWq27P3CCbRlnuVRIqfzutLgSyg9zqS8wWiuDFkh2k8OtaY2rtLpdsSYP2wqc9efFgMVPjcLRbSGu_ELBP0FxYTmvixnzee054fAINufEvsg0vj2H0xrUxFVPPNwLjQauT-I9-37cuTMhpxN7HYHvg5_WGzCfWx4TehdMFMnpqg_ABA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">+ آقای زنوزی پولاشو از کجا اورده؟
- آذربایجان ستار خان و باقرخان داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/84583" target="_blank">📅 09:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84582">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKOJvjQOzFaybxoHCbqX_1g7d3436DogB79gTZKaM-4r3nzUH_LaKBB6dM1rhq_sPKQxWiINnYWEV49iUODfKz1D0-_880PAxemj8vzds2MVJIUTzdVfyx70QopNxdVkiAujxcM47evjMWpamBkPbzma8QYBLrjyGZU-6NMSoxpAbrrGHPqwIE-kg94AL2GMZiEoXi_B_8ejAR9NUoC3u5wb83W7bwNDPcQt4AGKWbPPikl9y7Q6qxyIW3PUcoBYkEeiwnQXMmKKXR3A30W6zJb1fsW7kz-Eictmz7cwCz6x9Xe298KNd1Fb9eZ_MYp5CbpXwcqmH2Cq4T1ib3nayA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاوه گویی رسانه‌ی جعلی آکسیوس:
مقامات جنایتکار پنتاگون به سنت‌کام دستور دادن تا آماده بشن برای حمله‌ی مجدد به خاک مقدس جمهوری اسلامی ایران قبل از انتخابات میان‌دوره‌ای آمریکا.
همچنین دو مقام اسرائیلی گفتند که احتمال حمله‌ی پیش‌دستانه‌ی سپاه بسیار بالاست، زیرا آنها دوبار دچار غافلگیری شده‌اند و دوست ندارند این غافلگیر شدن برای بار سوم هم اتفاق بیافتد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/84582" target="_blank">📅 03:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84581">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یه ۶ تا ترک کنسلی و انریلیز از تیجی لیک شده، اگه علاقه به گوش دادنش دارید چنل آرشیو گذاشتم برید گوش بدید  Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/84581" target="_blank">📅 01:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84580">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">یه ۶ تا ترک کنسلی و انریلیز از تیجی لیک شده، اگه علاقه به گوش دادنش دارید چنل آرشیو گذاشتم برید گوش بدید
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/84580" target="_blank">📅 00:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84579">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دوستان زیاد دنبال موضوع فعالیت این چنل نباشید، هرچیزی جالب باشه یا حتی جالب نباشه رو میزاریم ما
هدف ما راحتی شماست که مجبور نباشید چندتا چنل جوین باشید</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/84579" target="_blank">📅 00:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84578">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رسما جنگ زمینیه
افراد مسلح ناشناس با شلیک راکت آرپی‌جی و تیراندازی با سلاح‌های سبک و نیمه‌سنگین، مقر فرماندهی انتظامی جالق در شهرستان گلشن را هدف قرار دادند.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/funhiphop/84578" target="_blank">📅 00:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84576">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015c4e30e6.mp4?token=s1oQSsSF5pSffUywAnY86p6T6rZDWccuEbCJTeVwC42UH8ts5Hu565uiocBsgO2EjCOtd0lWoPpZ6ZrTnnFHE932DNBfox7DHEQKHIBGSNzVzDdR4VTlCawldPIN7PufOn4HaBdtaUOL1KF9gT6vFh33QAt-6Ld2_mg9RWl4V_cJxyYPJCGTZ_3MsiG_SyOidzbPb2Ihhz4xq9x3J0V4F4XCNfUIGyF2nI1Zq0BYF1BJQNrIJPL86TRTScriWcAOy_4fnuVB3Eurfts3ktfDGBQPv3YJTaKysf3Uj3oWMPm4fRdEpyZ0rJEVDTcdamgruu6YBkGQ_GNfGBJU29lltA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015c4e30e6.mp4?token=s1oQSsSF5pSffUywAnY86p6T6rZDWccuEbCJTeVwC42UH8ts5Hu565uiocBsgO2EjCOtd0lWoPpZ6ZrTnnFHE932DNBfox7DHEQKHIBGSNzVzDdR4VTlCawldPIN7PufOn4HaBdtaUOL1KF9gT6vFh33QAt-6Ld2_mg9RWl4V_cJxyYPJCGTZ_3MsiG_SyOidzbPb2Ihhz4xq9x3J0V4F4XCNfUIGyF2nI1Zq0BYF1BJQNrIJPL86TRTScriWcAOy_4fnuVB3Eurfts3ktfDGBQPv3YJTaKysf3Uj3oWMPm4fRdEpyZ0rJEVDTcdamgruu6YBkGQ_GNfGBJU29lltA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی قیاسی رو با تیر متوقف کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/funhiphop/84576" target="_blank">📅 23:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84574">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ptj2oZvzWUcj9PtRxZv2kuQgltz8JLQJ2lxhluMoFkGAzPxgzRfHG80xMp3UU8yEIU2TYwO5F_zpJE7aYIoTAs9A8UkYlrA3R-KrwZDHY58hh2s4m1GEWe2mB7T6AwQ4yzu7cSMIUEZ5B_jN4yi3NRAHGnZYXemtxRFUUgjEax6Lpy-fCUj6_TNJRi5OnHk3eEauFXiI7GXWhUshrDS_1UVYyoxq-mJi8G3kFxUx2rq5Ch_6hvw12i16ZMgLq-sr23ThSBUX10vpNJnlldThODOBco4vzJEWGhs7nYB_K4Wvhp9kTLLLcBUCtsC-krV0RXRx9Y0ai-Mf5rypoTiFWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Efksikglxja61iUtI1QEIt7_NXlTWCUtMZAzIZy0U4wTzyR7YQDZzHnThag5wuEB8-vj6GklICOchuq0go4sMK46ygPe956chIhxsVfHpluddmwdFpw5eJ4XO-PCRRcb9OdMrEFHLCUtpt4Z-TpLTxS2dCOXF3qkV1Zv3vs3ubmDMVaguMm8sySidvqdbbxRG_p0gauOVnRkeGbWf_SQiql05Mg8l-auRDsfD64erGaX1LhPHCtWuP5YvtfsE97JkHX78dlTY_6RVfw2Xx8Hw--brRlyr30--XBzr7CWpajt-g8SePnoP-v-TqRsboJ3Nsb4zx3rDmWWQmRzSsOqqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاگان و ادرویت دوباره افتادن به جون هم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/84574" target="_blank">📅 23:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84573">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐒𝐡𝐚𝐲𝐚𝐧</strong></div>
<div class="tg-text">بلندگو هاشون خوب نبوده</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84573" target="_blank">📅 23:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84572">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3a994e34.mp4?token=BZrkRV_l5AcUnrmk2o4yW-cFgke6vK5XHJWkyWaTiCZ_zLq1MvB9HRH5FUBYMB3JcYZebFCR4oant9IE9AzKcZYlRp4BVoN5n8McTTWZpcvgWHzpg3jSlRq-pg8M3i-WKjGChPAIlB0bcVYBEwfHs9a4U566j5BfbYNRE4-mrW_6m26wC_f-6I153aaCX2wjzSPRjDII1p8EWXxUTqhgjKRjpRCnyxzbdUPyrwZ6vgaV_QewQ64xZ3ybhUO-J4PEtOFBZvHyge_9I0vdsBQRk8DvB-TRCX0dnlQEN0y-qP0zYGxv49ydJM_VLdPWNptmls-93YYk5mPN18BA5PYgcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3a994e34.mp4?token=BZrkRV_l5AcUnrmk2o4yW-cFgke6vK5XHJWkyWaTiCZ_zLq1MvB9HRH5FUBYMB3JcYZebFCR4oant9IE9AzKcZYlRp4BVoN5n8McTTWZpcvgWHzpg3jSlRq-pg8M3i-WKjGChPAIlB0bcVYBEwfHs9a4U566j5BfbYNRE4-mrW_6m26wC_f-6I153aaCX2wjzSPRjDII1p8EWXxUTqhgjKRjpRCnyxzbdUPyrwZ6vgaV_QewQ64xZ3ybhUO-J4PEtOFBZvHyge_9I0vdsBQRk8DvB-TRCX0dnlQEN0y-qP0zYGxv49ydJM_VLdPWNptmls-93YYk5mPN18BA5PYgcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میا خانوم انگار تو کنسرتش خراب کاری کرده و خوب نخونده، ولی خب به کسی مربوط نیست ایشون هرکاری کنه درسته.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/84572" target="_blank">📅 23:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84571">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d35a289765.mp4?token=hTIphwLdLeZTZQb4gKyVODNh4gVB70ECIB6apr9Gw21db8Us29tem_9brq7uz8iakT7AAZ1GsH7515XBtnLbuI8pfujUAWhRAtiCXVEsvNGI40IGyibq_7zfXiM4HV8RHIZtpAsNPzZSzV47Dt2jIZBlF_hopOjp5OGi4cYjK5QFx2PDYTZnfTSq72vNNqclGmhHdUTi9U-Q-PZCZGx8FZY9ci6OaulCvujr5-ZkUEMuyFO8CA3rIwCXjs04S72-lN8JDBynWkhR4_k-V175vsTDebeu3SgWXneEiiPNygzyANibsevk_xi6rtSrAZeoiCAvG_5mDD8y-Vuljdziqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d35a289765.mp4?token=hTIphwLdLeZTZQb4gKyVODNh4gVB70ECIB6apr9Gw21db8Us29tem_9brq7uz8iakT7AAZ1GsH7515XBtnLbuI8pfujUAWhRAtiCXVEsvNGI40IGyibq_7zfXiM4HV8RHIZtpAsNPzZSzV47Dt2jIZBlF_hopOjp5OGi4cYjK5QFx2PDYTZnfTSq72vNNqclGmhHdUTi9U-Q-PZCZGx8FZY9ci6OaulCvujr5-ZkUEMuyFO8CA3rIwCXjs04S72-lN8JDBynWkhR4_k-V175vsTDebeu3SgWXneEiiPNygzyANibsevk_xi6rtSrAZeoiCAvG_5mDD8y-Vuljdziqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلوت کنید آقای سامان ویلسونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84571" target="_blank">📅 22:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84568">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwB0mdTscUrWC5dCgKWmLFsjdqR_3FeXoJ7CBhPu4lYQb0hseq8R93ED1eqSwO_77EvyQyTpRIsxzFG9EcfmcPlJdJOT-hRlZjXxYo8gmJUIi0TDRLOYQwikcHQK0xJGGX_qD9j-ZDIg4eKE_8NAGTbDm3HYDhOSOZB6wVo8s6QJsjYHGGg_J4-KWwAQL0HRRRbCtfVpFfiOVMVPt_8OX6RTbDUkjMObG6pd50a36muqlFfORflwtWkLCFyfRyYuFFJkzbujAYkFp4TRUtCnRXDg1SzG4E3FkpyimO_sI0exVH2bnK9kfgi3GJAZu9uC0ylLrDQPfNxLw1udncDl4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت رونالدو برای مسی: لئو، سال‌های زیادی از کشورت دفاع کردی و تاریخی ساختی که برای همیشه ماندگار خواهد بود. بابت تمام چیزهایی که با آرژانتین به دست آوردی، نهایت احترام رو برات قائلم. یه بغل گرم...
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84568" target="_blank">📅 21:42 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
