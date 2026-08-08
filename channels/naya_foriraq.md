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
<img src="https://cdn4.telesco.pe/file/d_8R-ECs3KXHGqtJ_xlJ8oF14lKYpU_z2vP7JwtYQ_9VvWtANCORhsSBR2QmQ2jiQsSQb4G7f3RiqArY4IoVTJPYnBxrmRcPF8_ywlvs0xMkt1jJJBcsuPRKMt5o2MN7TEp17OHQ_pwmFndqCDQuLfkt7WvqsWAEYvFcgpvPbrFLDBCmSqje_LG_t390Ox3PP76mySfGLDgBJP629fH8QH3cQmqBOhcqSO1hopr7A53tynH7ga2LJC8Vzond_AO22djZYrekxcv1Ki7s89HsJC9tlUkbjc8-Q2ao_tHxZMO2R3J_vPg0DhRJd3SYTLS6h98lt1UNpAfpLs0gnT4zRA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 273K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 23:48:14</div>
<hr>

<div class="tg-post" id="msg-87313">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇶
الشيخ اكرم الكعبي: فالصواريخ لا ترد إلا بالصواريخ، والنار لا تقابل إلا بالنار.</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/naya_foriraq/87313" target="_blank">📅 23:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87312">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdvXXAVH4-8lv9aWEK_XoklOQqbgJQ7bTIyeSdHIUxa6qM13XTYEYfsQcEre9ZVzekGdnZSaj4lBVNb9uu9qfV92EoQAgeNkJfIK-8YV8EA-Iyb7wi0c439h5E_4BFheRtitNWvomAjlr5mGDo3oW8-3mKdqaaTr3N8JXh9kbX2MF2J2zrtVSt41XOdR-gzKVcnEvExaaTlACvV6d-vevjDnytAuGI4AzAhBk9oCB2Vf7R_UBKuRZVLhH0x7RbH3YfGCtVUVOSvP-AbwjCM81Ebw0TPA0T0sHQVNDKnv_4hrN-L4An0i69JL7yFQk-prfSYP6Q2I65UlsQqzQ5gTHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معك يا أبا علي
قائد أركان المقاومة العراقية البطلة</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/naya_foriraq/87312" target="_blank">📅 23:43 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87311">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118fa7dac6.mp4?token=rYepw5kxtXmwbpFq0Mmw90eJetut_-1qK2w3rKTYaVHnq1ukn_SSK6e4wIG2fsFwF4dWNnkO67SvtnunBcaJesmoBo0SpqkS1TAQ_FFhn-jD-U0t3G8Ct95V5mQqo4rr72dZiNXXEZQGpv-uNpQvez0CiuKs4I8mkZlObccfsw1eC_LRsK-CmQOm2ppCeYek6K2k5eFgj2Pj02MbcKCmMLAD8CR6zEMepwNilutDWuXDHCG-goQpGnZFPzsdapplG6eK6Z4ZyTTFZ3p1PSZOlssuN6Rj5Xgc-oFqRcERXDXjJRrtMXkCXPBSRLs9sC7nCyooGE-ODaqQyTwdTTCwkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118fa7dac6.mp4?token=rYepw5kxtXmwbpFq0Mmw90eJetut_-1qK2w3rKTYaVHnq1ukn_SSK6e4wIG2fsFwF4dWNnkO67SvtnunBcaJesmoBo0SpqkS1TAQ_FFhn-jD-U0t3G8Ct95V5mQqo4rr72dZiNXXEZQGpv-uNpQvez0CiuKs4I8mkZlObccfsw1eC_LRsK-CmQOm2ppCeYek6K2k5eFgj2Pj02MbcKCmMLAD8CR6zEMepwNilutDWuXDHCG-goQpGnZFPzsdapplG6eK6Z4ZyTTFZ3p1PSZOlssuN6Rj5Xgc-oFqRcERXDXjJRrtMXkCXPBSRLs9sC7nCyooGE-ODaqQyTwdTTCwkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اكرم قائدنا الكلف</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/naya_foriraq/87311" target="_blank">📅 23:41 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87310">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/87310" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
عاشت المقاومة العراقية البطلة وسلاحها الموجه نحو الاحتلال</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/naya_foriraq/87310" target="_blank">📅 23:39 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87309">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇶
الشيخ اكرم الكعبي: فالصواريخ لا ترد إلا بالصواريخ، والنار لا تقابل إلا بالنار.</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/naya_foriraq/87309" target="_blank">📅 23:39 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87308">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LONvTWp1Y7kpu_-x24X80rINMolQAnO-WglqCs0ZcxzSs02O1izfBNRYG22VtmjlAgbzIXExfDd_glg2c0jUYH2d_F_5Uxtb4dY5nY6Q9DwMU8eGqadd0mt9m8C-AZAaXtog3FmkmkY9TFd7RRfz-P0gRSm2iiSuDI_OqFMnPuqq4MPzyZVJYWG6ofq77enGCSR4dXKHuq_V-4vzt_y5lTzjQeqAWs8QLmtoTYHwkXAuwnhlQXXqa7L-dioxT-c41jdySVw3_zzrXdWrN84bmBjGLongx0qGn85ItvVauRCcuXiDGyAjcAdowc-AUpRz5ZPiI43PEMrqI615g392lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الشيخ اكرم الكعبي:
فالصواريخ لا ترد إلا بالصواريخ، والنار لا تقابل إلا بالنار.</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/naya_foriraq/87308" target="_blank">📅 23:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87307">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇾🇪
مرتزقة السعودية في اليمن:
انصار الله يجددون استهداف مدينة مأرب.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/87307" target="_blank">📅 22:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87305">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t8iE4YaT7gee7JrVfFrfp4UBpZKgyaWd88BNXnk2ipK9dFDk8f6T1j--h8n1Ck0zNSxdUvLaiAItN8Sx0AkBHtPfxUHhqvv5_4yuqrl_6q9cah0kox3K_sTrIuSyUB8WLjPaESv8FI13VahgWwZZYLyDO5HExYUu4v5yQM4eThCbCbcZX6MOLdonVYYnvp_DM2-af4sbTot1DyH8T5qrd46V6VNlYGn4QcyisGunIhXBaI2u4z1ASxQoDiyENPg_LVtcRh5GBMLgXajbXw1_x1e6XhJJ6TZ5SQiEh_xf5rBG5v8S4OBJxHmx9wqSvv1Ubvi6NBjJ78HDHN4I6-usRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SZYc6yicTFy5eu6y8brfByIo-Ic9iMtnDSdH4tilJFFpMDM2dv1PkEnrnVj1Oq3mlScqoJvXexH5iUPNtZqplNot600Si3d9XqKT88PWtHwX-5xUAD0r4ohO4T_OUl6gkh8FBD2jJEG3KdrG1n1fH2QDNFaurQktWyrxTABqi7KuMy8XoIDML15NINKysaez20LTrVXndVhYk7p74Pzo6eWFR6pDRDtldr1vr6vA3z3kwO_cr88w0LKG96PxF-sTDBfWxRLjVwBLexvJUPOaOZkv22XnTqA8Ij2xrtmQ4vlcditJihbRYsA8NtXgjARIySmXsKxzzFCOGgerCmJx-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
انقلاب صهريج نفط في منطقة الحرية بالعاصمة بغداد مما ادى الى احتراقه.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/87305" target="_blank">📅 21:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87304">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzpeUP5FZ3Obuz5zP7I2govg8VRlacF8VjBv2CyUvcFr72_B5fNey_pudbUj-RlL5UJJ3I95RQA3nA1tF6J3VOFficS0qROMARMGEyp4A8srWkyqMY_ZKcZGG-m46gHFJQ7dFTH9DZRqS3uc2tGMzTx8M-A3l2qAnm3_zqIUne1v6ZzP127yRtuQCqfgg2OXl_BwiC_0f_qYB9Z5sEUcFh8AaOsW_ShdIJNOgyeB85H7e7Jb-keD5-VWScgNY_2AKPbV8BlGUS9CAB0cFKc1ORRILtHRgNkfs5YU83UYnaFX8ciiyPhbw34ss6XHkPlifS5WHFRwhk2JbtWtnEY6zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
حشدٌ … يحمي حدودَ الوطن .</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/87304" target="_blank">📅 20:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87302">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a735eda5eb.mp4?token=VAovY1UrSusDbidd3A0BmTahxliFGPjdT4nhQy2t_UoJTS1YEq_Rl9Mzi-7zJ0siPKZqW29m_pqxSc4VxnDatRDzWVlrlg47atrCkMxYchxCHQf3Zz1rbt_fPu41amk2kK81mgzK8IfhEiAKh5dgdf_bbUzZIpqVxA5XO6J-FhYbrJa-DsPluRbvQy8Ir2DXnm8Ru3Iu6i0RG_SfDhsEQHl9splIP6BOEREOj8LTYvGP7lANURhZ5Sduhs37JgPs9lOt1hml5PfQiXckAobEgDiJecSJIOK_AcvxYGGsUsJRss98NEh7SOPDgPqpDRBi7W9RdBGodKxYaHmOccwiMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a735eda5eb.mp4?token=VAovY1UrSusDbidd3A0BmTahxliFGPjdT4nhQy2t_UoJTS1YEq_Rl9Mzi-7zJ0siPKZqW29m_pqxSc4VxnDatRDzWVlrlg47atrCkMxYchxCHQf3Zz1rbt_fPu41amk2kK81mgzK8IfhEiAKh5dgdf_bbUzZIpqVxA5XO6J-FhYbrJa-DsPluRbvQy8Ir2DXnm8Ru3Iu6i0RG_SfDhsEQHl9splIP6BOEREOj8LTYvGP7lANURhZ5Sduhs37JgPs9lOt1hml5PfQiXckAobEgDiJecSJIOK_AcvxYGGsUsJRss98NEh7SOPDgPqpDRBi7W9RdBGodKxYaHmOccwiMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انقلاب صهريج نفط في منطقة الحرية بالعاصمة بغداد مما ادى الى احتراقه.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/87302" target="_blank">📅 19:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87301">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ab4e142d.mp4?token=s7lLuf30ZswMoQVLY-sRKU-r3sQIBGyTCxs65pMgVMBQIzsPRt7kPTwpmqezD6swYTZoT_dmqw-c7SCg0KG44Zr-kgtIk4fdLrqLk6GOMEmEQPJbU-6V-6fzYRtL0D5v477_BKQvkpdCOGdY7Mm3sIYM9iMlJ74k9Ibq-Lne6nIIs32D7-bkAaNRVprBfMGKeFAz2oLByOSbm9bKDZR_HQqt-3spuZSmqfj5r6JhLrLQEtb2mmQ0akIWZSctorgGPMQokQYJ1-vQJiWLLCi8c83hD9kZOMnRa7A7yGB7duo1qEPewqchfDyOb6KYdvGcWuT1RX74lVS6r6EZZsSIhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ab4e142d.mp4?token=s7lLuf30ZswMoQVLY-sRKU-r3sQIBGyTCxs65pMgVMBQIzsPRt7kPTwpmqezD6swYTZoT_dmqw-c7SCg0KG44Zr-kgtIk4fdLrqLk6GOMEmEQPJbU-6V-6fzYRtL0D5v477_BKQvkpdCOGdY7Mm3sIYM9iMlJ74k9Ibq-Lne6nIIs32D7-bkAaNRVprBfMGKeFAz2oLByOSbm9bKDZR_HQqt-3spuZSmqfj5r6JhLrLQEtb2mmQ0akIWZSctorgGPMQokQYJ1-vQJiWLLCi8c83hD9kZOMnRa7A7yGB7duo1qEPewqchfDyOb6KYdvGcWuT1RX74lVS6r6EZZsSIhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انقلاب صهريج نفط في منطقة الحرية بالعاصمة بغداد مما ادى الى احتراقه.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/87301" target="_blank">📅 19:57 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87300">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇶
إلقاء القبض على السياسي أحمد الجبوري أبو مازن بتهم فساد في بغداد.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/87300" target="_blank">📅 19:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87299">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇷
🇮🇶
فضیلت آن است که دشمنان نیز به آن گواهی دهند.
صدام حسین دربارهٔ جنگ تحمیلی علیه جمهوری اسلامی ایران سخن می‌گوید و بیان می‌کند که ایرانی‌ها به‌خاطر حوادث کویت و تحریم و محاصرهٔ عراق، از گرفتاری او خوشحال نشدند و شماتتش نکردند:
«آن‌ها کینه و دشمنی به دل نگرفتند و از وضعیت ما ابراز خوشحالی و شماتت نکردند؛ بلکه با وجود هشت سال جنگی که با آن‌ها داشتیم، خواهان همکاری هستند؛ و این‌ها از صفات مؤمنان است!»</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/87299" target="_blank">📅 19:39 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87298">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52f5abbbce.mp4?token=UTdu0fXBW2QlQCmPSONyUhxWMav7GiXArgl1pm2M7aDvmm3gIiim5NyXVFap2sWGaKxZWNbxqMd1Ur7l6uHYQQRCg9IfTJ9984TRdeBviIUgnmj2_O8zTCXgW1LDIs5U2mCqj5kWK0FKyV6LmF9CS8yNrOb0N1RjPlTF24p0CGigppXmYISe5GRPDftBY-tNNPAa-CqMsPyzb4SKH9S746B3yolKj1QehBwVIzuMEqF8IwjGB0HS72GjFXwaK-FwrxEiIGWLqmTbD1Y0zjv8hB6iv9ovgr7NiQhIMISRyLOIlypNm0m4YlKnW2vIpLEtPdHSXc2mJs3nWH_9Q-rKuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52f5abbbce.mp4?token=UTdu0fXBW2QlQCmPSONyUhxWMav7GiXArgl1pm2M7aDvmm3gIiim5NyXVFap2sWGaKxZWNbxqMd1Ur7l6uHYQQRCg9IfTJ9984TRdeBviIUgnmj2_O8zTCXgW1LDIs5U2mCqj5kWK0FKyV6LmF9CS8yNrOb0N1RjPlTF24p0CGigppXmYISe5GRPDftBY-tNNPAa-CqMsPyzb4SKH9S746B3yolKj1QehBwVIzuMEqF8IwjGB0HS72GjFXwaK-FwrxEiIGWLqmTbD1Y0zjv8hB6iv9ovgr7NiQhIMISRyLOIlypNm0m4YlKnW2vIpLEtPdHSXc2mJs3nWH_9Q-rKuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏
فانس
: الإيرانيون يتألمون ويريدون إنهاء الأمر، إيران أبلغتنا بأنها ستسمح بأقصى حد لتدفق النفط عبر هرمز لكن لا نثق بها.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87298" target="_blank">📅 17:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87297">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇷
🇺🇸
امريكا تنهار من الداخل بسبب ايران
إعلام أمريكي : ‏ عائلات 5000 بحار على متن حاملة الطائرات الأمريكية أبراهام لينكولن واجهت وزير البحرية الأمريكية هونغ كاو بسبب مزاعم نقص الغذاء وتلوث المياه وإرهاق الطاقم.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87297" target="_blank">📅 17:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87296">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvEKdzc-3hJbGgTqCUGTxzRXtWSCyXsYPdcOVTU0-ohmxC7JAVFoQisJxsx5DxMqnrkcqaTKa2LX9CKtDiUZIu8MDwvM5iR-dIrhIMtqZ4va-fMGhofE8KJPbz5AoARD2_ja6kbhI7YBtuukROUXjFJY3FqioIXpbPrAdUS2d1yvl94ObNKTUKdUyX0nq3PUXCFvIjNQRT0zh1d7IKwTIpLLmLve9WyXuQ_nWGKUAGYvmIEtKRznuZq2LM20q-YC_29ERZTEUTWw2UtRkm6a47OeMfg84AIK_nf4EhpzV_atdnjw4NV_yFqJDAt-gWeyxLQf_jc-thEVE2O8THluIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
محمد باقر ذو القدر، الأمين العام للمجلس الأعلى للأمن القومي الايراني:
طالما أن الولايات المتحدة لم تصحح سلوكها، فإن مضيق هرمز لن يفتح. المجلس الأعلى للأمن القومي لن يتزحزح عن موقفه، سواء في الحرب أو في المفاوضات.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/87296" target="_blank">📅 17:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87294">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MTWBSMVtWc99nad9vTXVseiB46UhPHbHYt9iM6lUzPUSTOOd_r50SrW5zhlwcEccl5RAn-nfD_nH-94TKwom5FMhRcYyfdgfES4u9TeRCvdcvUgygYeDw-bueCZ-2NlaG4VB2d7gtOTXWGNI0q6FI-wicjZX_JgvAWHjxIycpyq12PL0mgiElRinrrao-N_6aO7Nri0bJGrZHeAIDn_1InXUMN8ZPK6dzolc0BspXmtwN640v0zYuDISQyM26iK2CIiaj8vQZy2l1TMcQztO0_NOePyN4ENWS1_HzWOuKh9qOVV6Th35LhXQiw0ObvIh6GxiGVJu_I2jHdR_0bdNQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WjDgq9x3tkZz-NQMzYxnW-2SsxUha3vuINAhC7JKYyPZHJPaPRBbb_LpzQ2YFGmN0uWK-3sKbBpLNjY1nFvQH6dd4t_a4Zf8INGiH4lZEe7c4k5rshfKJY-m-3lj3lKVCXIG-9qxgEl5YWUCIX3-qEKjCSgBGVd-t9vbYV-7xbfFpkz0jrj5ytrgXdx4fCGbOM8JALN2EZqeIBb-slDNhsnwJvO3BxPUl6Vhair3pXlYb6jXivg2PKHFMzKT1EaZWdD9nsfvUymxgivBdHT59Nqr7rekPWByvHdLgoS8CjVNzM9aPefQ6XuOGBBoIEgWdgJaghnSnros1BylSHp49w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">علي فالح الزيدي يستقبل رئيس جهاز الاستخبارات العامة السعودي</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/87294" target="_blank">📅 17:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87293">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حادثة على بعد 18 ميلًا بحريًا شرق مدينة خصب، في سلطنة عمان.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/87293" target="_blank">📅 16:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87292">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFh837UU_yuiXx5sCXnBUjD9GlTI6vIHFw6nvPOfWSqlA2sszbUW_k63vW4Z9SSReWZLBlwXb_86pwtqiPi5ZUoOboKHQf6ChNqYxaZY7bVQStHuzhgi5SbNM3513XFpgJGMKUPftCK2Oqczzf3Ft_GIIQd0CH7rsK-QEcvVe7NVIJeJkJzVVrwEgMUPZl2u2-k0TH9k22pWSdxEZZHI3_xfXXzmHRMu99wbOnXZseYihv8qgd473ldgJhKo_OB1CAJViFIk5rh39pOE5mBeefPWDpNmb3IUPaF9Yb7A0KULKddTGrSoDFJUllDnLH3o93FfcO7Ded5Sf_6hAOi7dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/87292" target="_blank">📅 16:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87291">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/87291" target="_blank">📅 16:39 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87286">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o2ZgE0AZ4kqI2j6uLEWJVKOHfV2tEku1Myum-3sUL3sdGzBLob55SazN04JkR0WX3ASDEw0gruetAh7_or_X7o7L_BFmzqdfZ-juyWJf5T9o-HJPbZhBku2Wyc8HUXmrnA_YnqFUDULCS7sNTAEpP7MT4kRDID7-0HYvS8jHCKgvmcgwdfEe6nOlOREjJlrXrUw8P5QzHlznbrqFTE3GWFHjDj0yUVA9QX_DjXAKNA3Dk4sQytYe5YU-igbKhwWIh2ueamv7gnep46VaGL7PXHzQt-LmOpd3sii_vkIsbGdAv2WHd3MJ6nP5Bh0UegJGVSGxv4OiiBbj-W05ocRukQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ApEUgJ-vHApAMvi-Wm_n3I8W2CQiXYyT2Re3tYZKb6kZCbN8WECuyc1cfELfDY7UVEYx7_Zcf1AyJYKgZOtYcm8XNqfYdlFw46ykfDRWVLKIWJMZHk-BgKLWCdFS0L7WUjiZeUW3DmnlqSaR0lruYFFzM9zv4-f9OnvFf0w_sZtaZJPn6xLKdfSckB365Z48eV68x-Vgku-nQSdz8QIaAiNb_YkEN0xBAs1S4UskeDfi5A8Aa7C1xLU64HO8NP6zuad-YInzl7kcXCJio5_mr1Imc-wF0TvLJ3t-NcWlmU7cLLMrWGc19AD0MxF_9gOrbuOgG0k0Of8eXfrIUUvkgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a9gc6xyYwzthmuYhUYtfHitWSat4SwFF3oU-zKAl76YP5WFmEiXbE1jkSd1hsgjXgAPt9RASgpXbQAmhvK68dWmZQ6vr1ptMGk2TYn4CFKVon3zVUJuevw2fiWQOz5W5eDK0g665KSn7y24Wwj_QwaHqBzzjs1P2PSgrv-AVzB5Ur7PO4bH2s9wU7RXDvTaKq46jcKCEfaZPVOKL88FWEDfWVEVRJpoylz4OJDYkswZOMio5uspI6yDknwOSsWg7fws5Yk8VmKshLyub-FDwJpH46XeqODDAjQnT-wGyOBQg5uVbGioUisYA9lyTN2ok_3Lt4U6hxE-d7hZw_VfAzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qlrYreigyMUkpnDAlIHqjAXoDsuVZ1yf6tF_xFrFOu70BGcnp9gW0JPfvI2HgZEAKKlkARQIBHcPkqLwu-EcL5ODPoQ9RWn-F4z9SxHzVo8EmV9sbPznuyCauLGOaOuZfwa4U-TI3js6rMee78CrijNx6ojyFRvRwAb3J-IFT5AGfrdwcTbWLUwYW3-xwERH8Gxy6s3G6vnYLcnD2w83PHSyXceuXngy7cs4sJAy6ZNOA1vunw5JWWnRmh3xn66I4TopqDCDlyzmH-iBqg0LGrsKafiDpkSrR_4JlghvkbiRIl7UcrnXWB7yOSkrY7MAxx_047bbC6XlpmlpSGSSAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">السلاح المنفلت في اقليم كردستان
محمد حاجي محمود رئيس الحزب الاشتراكي الديمقراطي الكردستاني يستعرض بقواته في مدينة حلبجة بالاقليم</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/87286" target="_blank">📅 16:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87285">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سماع دوي انفجار شمالي مدينة مأرب اليمنية وسط أنباء أولية عن سقوط صاروخ اطلقته قوات انصار الله باتجاه المرتزقة</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/87285" target="_blank">📅 15:57 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87284">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇶
رئيس الوزراء العراقي:
يوم 30 أيلول المقبل يمثل الموعد النهائي لانسحاب قوات التحالف من العراق.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/87284" target="_blank">📅 15:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87283">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">قسماً، لن يسقطَ العَلَم.
#هيئة_الحشد_الشعبي
تنشر</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87283" target="_blank">📅 15:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87282">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇶
رئيس الوزراء العراقي يوجه بتعطيل الدوام الرسمي في المؤسسات الرسميّة كافة ليوم الأربعاء المقبل تزامنًا مع ذكرى وفاة الرسول الأكرم محمد صلى الله عليه وعلى آله.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/87282" target="_blank">📅 15:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87281">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇷
وزير الخارجية الايراني عباس عراقجي:
- المفاوضات مع عُمان بشأن الآلية القانونية وإدارة مضيق هرمز، فيما يتعلق بتحديد مسار حركة المرور في مضيق هرمز، جارية، ونحن قريبون جدًا من التوصل إلى اتفاق، لكن فتح مضيق هرمز مرهون بظروف أخرى، منها جبر الأضرار الناجمة عن حالات انتهاك مذكرة تفاهم إسلام آباد من جانب أمريكا.
- خطة فصل حركة المرور السابقة في مضيق هرمز لم تعد مقبولة لدى طهران وهناك حاجة إلى مسار جديد، وهو ما ينطوي بالطبع على تعقيدات فنية وقانونية واسعة.
- نظرًا إلى التعقيدات الفنية والقانونية، نتحدث حاليًا عن مسار مؤقت. وقبل التوصل إلى المسار الجديد، سيتم اعتماد مسار مؤقت ليكون أساسًا للمسار الرئيسي، وفي هذا الصدد جرت مفاوضات بين القوات العسكرية والبحرية في البلدين استنادًا إلى الخرائط الموجودة، ومع الانتهاء من هذه المفاوضات، سيتم تحديد المسار الجديد.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/87281" target="_blank">📅 14:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87280">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇱
اعلام العدو:
اصيب جندي في
الجيش الإسرائيلي
بجروح متوسطة في حادث عملياتي في جنوب لبنان. وتم إجلاؤه لتلقي العلاج، وأُبلغت عائلته..</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87280" target="_blank">📅 14:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87279">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇹🇷
نائب الرئيس التركي يقول ان السعودية ستقدم لهم دعم مالي مقابل الدفاع المشترك.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87279" target="_blank">📅 14:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87278">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔻
السفينة التي تم إستهدافها بالقرب من الساحل العماني في مضيق هرمز هي ناقلة نفط تابعة لشركة أدنوك الإماراتية.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87278" target="_blank">📅 14:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87277">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87277" target="_blank">📅 13:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87276">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87276" target="_blank">📅 13:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87275">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇹🇷
تركيا تحد من حركة السفن في البحر الأسود بعد زيادة الهجمات على سفنها.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/87275" target="_blank">📅 13:52 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87274">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDv6MI8j2rJYRqItWyyA12Ys7PhgmaC_GpxgBnh19_i81EpLFyIYduDakriHjZeh_DpjUcvTvwiCusylz_aeV4bYsXMTqW1_NpxWa1Hy4kslfXWN5Ne77VkzOmNjq-vN3sWuv4Yi6xzp8yRQhzU4Kpr03cNuuv-EnUcrL8YTubG0QoVonIpasnW0mV9jiHb_d6vOrrfYjtyZ0LILfSGcU4-5u5q7ISllZOaiBrr6Yhcq5VqjsCGwIJ9WfYUlUfjaTggwA6z5WUA91qiS_ixjmyzNNC5_TK40q2iU0vLFFxDkZmcr_Xm0CY4LlcnvObhRPjmyau6G-8hNrUmnAz5_hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئيس وزراء اقليم كردستان المنتهية صلاحيته مسرور البرزاني: لا يوجد هناك أي جندي أمريكي متواجدًا في القاعدة الجوية "حرير" منذ أكثر من 10 سنوات.
يبدو ان مايكل سوينتون توفي غرقا في شلال كلي علي بيك
😄</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/87274" target="_blank">📅 13:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87273">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇶
وزارة النفط العراقية: نجحنا في تأمين المنتجات النفطية رغم تحديات الملاحة وأزمة مضيق هرمز</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/87273" target="_blank">📅 12:41 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87272">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رئيس حكومة إقليم كردستان العراق:
ندعم الحكومة العراقية في حصر السلاح بيد القوات النظامية فقط
إقليم كردستان تعرض لأكثر من ألف هجوم بالصواريخ والطائرات المسيرة
الهجمات على الإقليم جاءت مباشرة من إيران أو من داخل العراق عبر بعض المليشيات
لا يوجد أي جنود أمريكيين في قاعدة حرير الجوية منذ عشر سنوات</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87272" target="_blank">📅 12:16 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87271">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmZ9HAVZ9dYhW468zFzTffTe8qxL7M-ccFMm7u0I1BRQlIQlIwdF2PGSLSADSLEr6W6CPEMF59r-ue4XAOgVHqbpkAMBIypFkw3pkGlFVmL4NHk1NVAMHJq6KPlkUXfjmlBwanHtkeZ9VU4EHlCdw2Pp1wJNBYsViyOX99ZCgloRa9jwpF8dMwJzgSZjPJGMBzA4e3gpEFdGzva1GaJn2keWS3Tmum6op3aE3bR7KCHFP-VgL5aNvyt0evFswBaN6rjCJ4nl71v5iMzuEte8uyCwH6LiGnk-yHnVJE68fCKjBB5CJBXxb3IbiwT6i7DkDmxOJuV_IQ5MSsrqz8RDzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
استمرار ارتفاع أسعار النفط حيث وصل سعر برميل النفط الواحد إلى مايقارب 84 دولار.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87271" target="_blank">📅 11:43 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87269">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_ADByzBRMyCol1_KVdgt85XfXOfnVnm8LZ7qxIMCF6Q2piLhOJSKK-csc5xUiw5IUpUmg1EDwwk52T9FNM4HuHXfmQiIBw5mpN8X3muR9Inl2Hwsg009AhxVduejds9b6s4igmVDd1oqR1LTIMkn9b37qfifmTHvH1svl0EgR3WUctzUXNYfY_gYfjw9dTGWrPT8KbpMCOntOoswIviX2nbfkiFg0b9CBX1l8bSvJirsNZK23nsTU5N2AzpJYOkicLVnoQFvL4Tt875jxKI1aa99EGuk4V13kLIljQq5ukCHLSpNfeEpUKzzDDtSXQp4upyKT8aqiCqFXlHV9B-jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd02c3829c.mp4?token=ffdCnuWxcD5uFJo-pobCG0EQ0hj0qojQhA5q63mcZnjZInMjUcss71Vda6sdveIwcs-AvQ58Aai6yPvrz7Bxcb9fXbr8u99X6GJHrByXQ0NokldElduUOBfafGvsQGX-ldWgqUezJoUZvhYG_v-EZTKxs3YpnfsT1KBeSIFPfrcZyyGn6XC_-yW2LgyPPwSbnLo0kTi3nL3c3xdmviajgrq93EC2Po-TJcsKlvFSPRJTc9prb9MtGTBjkFY69UXKZ3zr6pzvvNAgSf0-fZx1wetG3q-CLAzOF8CPYAsMT5ZVD1TSmOEwGGHEj6Amcjd0gzZj-yDaxZIAry14_HraMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd02c3829c.mp4?token=ffdCnuWxcD5uFJo-pobCG0EQ0hj0qojQhA5q63mcZnjZInMjUcss71Vda6sdveIwcs-AvQ58Aai6yPvrz7Bxcb9fXbr8u99X6GJHrByXQ0NokldElduUOBfafGvsQGX-ldWgqUezJoUZvhYG_v-EZTKxs3YpnfsT1KBeSIFPfrcZyyGn6XC_-yW2LgyPPwSbnLo0kTi3nL3c3xdmviajgrq93EC2Po-TJcsKlvFSPRJTc9prb9MtGTBjkFY69UXKZ3zr6pzvvNAgSf0-fZx1wetG3q-CLAzOF8CPYAsMT5ZVD1TSmOEwGGHEj6Amcjd0gzZj-yDaxZIAry14_HraMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇾
انفجار مسيرة على إحدى خزانات مصفاة الزاوية في ليبيا</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87269" target="_blank">📅 11:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87268">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇪🇬
🇮🇶
السلطات المصرية تحقق في شبهة تزوير قسائم ودائع مصرفية بقيمة تقارب مليون دولار تقدم بها لواء عراقي سابق مؤكداً أنها تعود لوالده المودعة في بنك القاهرة عام 2002 ؛ حيث تم التحفظ على اللواء ومحامية عراقية رافقته وتمت المباشرة بفحص المستندات والتحقيق في ملابسات الواقعة.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/87268" target="_blank">📅 10:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87267">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇱
صفارات الإنذار تدوي خشية تسلل مقاومين إلى مستوطنات رام الله.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/87267" target="_blank">📅 10:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87266">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇱🇾
انفجار مسيرة على إحدى خزانات مصفاة الزاوية في ليبيا</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/87266" target="_blank">📅 10:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87265">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇱🇾
انفجار مسيرة على إحدى خزانات مصفاة الزاوية في ليبيا</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/87265" target="_blank">📅 10:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87264">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f352388653.mp4?token=ufAcIrtMwoG7xAVfMInZU8pwROE40a6_mnQ-gQ3UjiUflGXCTgxb930q80_lxZnjtjD07piBYIsFRBuYy3qk3Ts34-mj_tB_x8WB6p6Be4OgwFb2RzYaAt3J5I59nV3NdF2X73pItVohVBvsKPNznq0YUxEF1bxO_eeTgnBfk0yfE3ogwApG8_108kw8VmugQHrzv-8RIok17miCpQddPCC1f-6v26bdiT56jSdThTJuEy5hmEyLid7POPqx8RxdOKVzgjD6hMTpw0NFDyvFBoQRnXvJ_QqaHoyElrsU1vEQkS_62mtB6vcuwNh95zng-jwLXgqKHR45TVU2BnEljw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f352388653.mp4?token=ufAcIrtMwoG7xAVfMInZU8pwROE40a6_mnQ-gQ3UjiUflGXCTgxb930q80_lxZnjtjD07piBYIsFRBuYy3qk3Ts34-mj_tB_x8WB6p6Be4OgwFb2RzYaAt3J5I59nV3NdF2X73pItVohVBvsKPNznq0YUxEF1bxO_eeTgnBfk0yfE3ogwApG8_108kw8VmugQHrzv-8RIok17miCpQddPCC1f-6v26bdiT56jSdThTJuEy5hmEyLid7POPqx8RxdOKVzgjD6hMTpw0NFDyvFBoQRnXvJ_QqaHoyElrsU1vEQkS_62mtB6vcuwNh95zng-jwLXgqKHR45TVU2BnEljw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇮🇱
طيران حربي صهيوني يحلق في أجواء الجنوب اللبناني على علو منخفض ويطلق أجسام مضيئة مجهولة.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/87264" target="_blank">📅 09:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87263">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇸🇾
عصابات الجولاني تدعي: تحييد عنصرين من تنظيم داعش الارهابي كانا يحاولان زرع عبوة ناسفة في السيدة زينب بريف دمشق.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/87263" target="_blank">📅 07:48 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87262">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBr7vRuotfP8Fb31ddITb0QkKJIe6_XdfsuqmDrK6JPKSflzFDkc1oM-ZZ-k_n_0qCpj9IZQr2byRWkhC2c0qJXqRUecMJgE-hK51J-JiMwPYYBnnh0K2-icKD9JR7EW7Ip3WG1SaDD83iH2LEq7Y27CrNJnWfUGiOZqb8WCdRFxHeJjp8tn4DYq9gCWB_j51sR4qHtWjDCQurTfBKqL35gJtj0BXxcZwNEnn3k-U6zcG-GJbhfoS8NUoce3GIvWDBklpgDEthzp-mM9QhkswpzJFwXdCfUl5T9XW5w5Vepl0FuVeGhPRO4CNixdU5n_QjWrNjGtnp3gbwL001szgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
عدة طائرات مدنية عاجزة عن الهبوط في مطار جدة الدولي بالسعودية دون معرفة الأسباب.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/87262" target="_blank">📅 06:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87261">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27d8aaf8f4.mp4?token=hBw8FwHLGiF7_IQgqvxnZn4xg0HVi0LerXAz0qPWLZBkKkSdi6vXsfP1zZ32Ov5QBq5WQ9sAqEi3DO9TIlIbVwNesYLAnufrHuOPr_qoH1F9wVG0Q2Uk_-G0Ufl5GZ4L6BDY-GZvcF2cPIrRoQVCv-W1P7muWREdRo4YgVSRBigG-S8AoBRBaRHnbQRk-VdydbsvoivOPolagkEdPjKX6lWU6lZa5gWCvWGzn9BhtbUgYhQvEaF6rBJOmdqanxYgA-eXbOvX1ZzWwFuD21aGFZs0anG6gzyCnhtDHHxp7w5fCZg03p4LULfAYKgKCVYLgkEEgolNHz1IYln935Cc0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27d8aaf8f4.mp4?token=hBw8FwHLGiF7_IQgqvxnZn4xg0HVi0LerXAz0qPWLZBkKkSdi6vXsfP1zZ32Ov5QBq5WQ9sAqEi3DO9TIlIbVwNesYLAnufrHuOPr_qoH1F9wVG0Q2Uk_-G0Ufl5GZ4L6BDY-GZvcF2cPIrRoQVCv-W1P7muWREdRo4YgVSRBigG-S8AoBRBaRHnbQRk-VdydbsvoivOPolagkEdPjKX6lWU6lZa5gWCvWGzn9BhtbUgYhQvEaF6rBJOmdqanxYgA-eXbOvX1ZzWwFuD21aGFZs0anG6gzyCnhtDHHxp7w5fCZg03p4LULfAYKgKCVYLgkEEgolNHz1IYln935Cc0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
استهداف مقر تابع لإرهابيي الكوملة في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/87261" target="_blank">📅 05:41 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87260">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔻
وول ستريت جورنال :
هيغسيث يسحب التصريح الأمني ​​من وزير القوات الجوية في إدارة بايدن.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/87260" target="_blank">📅 05:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87259">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔻
إشتعال النيران داخل سفينة بالقرب من الساحل العماني في مضيق هرمز بعد إستهدافها أثناء المرور من الممر الجنوبي للمضيق.  "وترامب يؤكد أن المضيق مفتوح
😆
"</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/87259" target="_blank">📅 04:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87258">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔻
استهداف مقر تابع لإرهابيي الكوملة في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/87258" target="_blank">📅 04:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87257">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e351fb75c.mp4?token=oTwsut4ppa8MdLG3rwudz9GYeRGcoV__cuo5W2ANZTbjI4pQZt3dCyGSbY1nNIMgTKOCYPuNb-9BK4r4ywmQlbLY3dM67tGPbUIaU6Rjxwg2cFH89Phs4g9ql_cGPrfPaQOcFaLmyltVtoZq3-3GJjwezmq1_nhEaJHcJE-rh0tf6zCcR9n_zDJbKRXvgmCaY8qJBH48YTpmB6nqq1LuXJOzy_l3uA7CrSvWLp46KvCRdrJJMXuYzY9rMn2V8KVca-IsoAUbvfdM8e07xRZUPA4e9xi3wUiNLbNr5BEVU6fDIDCTMiAbUINLTN1HN0i383a6osjaNRivTZJLrE-tJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e351fb75c.mp4?token=oTwsut4ppa8MdLG3rwudz9GYeRGcoV__cuo5W2ANZTbjI4pQZt3dCyGSbY1nNIMgTKOCYPuNb-9BK4r4ywmQlbLY3dM67tGPbUIaU6Rjxwg2cFH89Phs4g9ql_cGPrfPaQOcFaLmyltVtoZq3-3GJjwezmq1_nhEaJHcJE-rh0tf6zCcR9n_zDJbKRXvgmCaY8qJBH48YTpmB6nqq1LuXJOzy_l3uA7CrSvWLp46KvCRdrJJMXuYzY9rMn2V8KVca-IsoAUbvfdM8e07xRZUPA4e9xi3wUiNLbNr5BEVU6fDIDCTMiAbUINLTN1HN0i383a6osjaNRivTZJLrE-tJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
إشتعال النيران داخل سفينة بالقرب من الساحل العماني في مضيق هرمز بعد إستهدافها أثناء المرور من الممر الجنوبي للمضيق.  "وترامب يؤكد أن المضيق مفتوح
😆
"</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/87257" target="_blank">📅 04:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87256">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مداهمة منزل في منطقة الكاظمية شمال بغداد من قبل هيئة النزاهة يعود لأخ شخصية سياسية معروفة</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/87256" target="_blank">📅 04:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87255">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مداهمة منزل في منطقة الكاظمية شمال بغداد من قبل هيئة النزاهة يعود لأخ شخصية سياسية معروفة</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/87255" target="_blank">📅 03:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87254">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAwOk54PKQKm0mt-7q6MrQMNQDKkCE_4kFg9pwiHINXP-n9-HLBwhdjIFfqjOdJt4ZOxpsx8M-Vxtsy_RzDgkZVwAVcD3qeWNN3qJTyYj9fw-Ene_GptrpsMgy5iaEP1P1iKWmcI2y9QOxkSLUxQaDH97wZZ8x206jwJUfTAc8CbnxNNjNJ9qZMrQNFtWhGoJpuppxYjxzcZ29Mwl9ERAwaAo01zQ51D8_10aIdeKFH9_jwyxox4DXbRSt3qsYOiNA-ZJxELZRh4OFV_qSWvNMQ9a_SXfANdHA0k-AX2wqtXVPDd-GuIOnoBzlKd6nN3wjfH_YK79Ye2FVjpmdZpNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
إشتعال النيران داخل سفينة بالقرب من الساحل العماني في مضيق هرمز بعد إستهدافها أثناء المرور من الممر الجنوبي للمضيق.
"وترامب يؤكد أن المضيق مفتوح
😆
"</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/87254" target="_blank">📅 03:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87253">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce4bbf82a.mp4?token=TKB394r_eUP8iUFFSnjJIxMqPI4trVczJSQXGXLlJHWlAKOf87ehMhzHBJxwI1pOu7IL0hOFwIs6mlajt3R2bqI5oFTz1ew7hj4rU1tIgVMPC1qruu_GLutx5WSuJfKnKKpzZOpTB_kRHu72DBEsPuDDguQOd3YAQ5exTeVFAG-ISvdXKseekSr3xssU33wnFY9hxe_6J_qQIVGqTFrowCF6WPLJyi4Z2FqUbc21eIp6D1rOt2UD_JP_8dTZDTvoC35vn8_pKo96v45EuD41iJjmqS0_hqDBd9YimM8KE82Xa1GZR8tlzRpASCQlVL6LKfUwztYJ_S4xgbDlamKF4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce4bbf82a.mp4?token=TKB394r_eUP8iUFFSnjJIxMqPI4trVczJSQXGXLlJHWlAKOf87ehMhzHBJxwI1pOu7IL0hOFwIs6mlajt3R2bqI5oFTz1ew7hj4rU1tIgVMPC1qruu_GLutx5WSuJfKnKKpzZOpTB_kRHu72DBEsPuDDguQOd3YAQ5exTeVFAG-ISvdXKseekSr3xssU33wnFY9hxe_6J_qQIVGqTFrowCF6WPLJyi4Z2FqUbc21eIp6D1rOt2UD_JP_8dTZDTvoC35vn8_pKo96v45EuD41iJjmqS0_hqDBd9YimM8KE82Xa1GZR8tlzRpASCQlVL6LKfUwztYJ_S4xgbDlamKF4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحن لا نشجّع على الحرب،
ولا نحبّ الحرب،
لكن في كل حادثةٍ أو اعتداءٍ،
نواجهها بكل صلابةٍ وشدّة.
وقد أثبتت التجربة ذلك
🫡
الشهيد الأستاذ والمعلم
قاسم سليماني</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/87253" target="_blank">📅 02:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87252">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d93912779.mp4?token=GRL6DnqIU8L4-q08eeKW_1OBEk6YA8h3-g8ErjCXpf7AYSnpQ7aWHTIQA4oaANanX05qVLcogLmSnpzLvjG9s_NXIx8-OZbDQPOcRsxixLAb7DOI12W7XAhGykszBz2OR8KeANx8xFMwX4mWKkgqqxYKUgyXn55CmbMSedzb6SO7qbuz0k0kOQWeZ8ybVDRdfxaaQVl3oTCzpI_csUn2GrE6JuWcPzUmR9zp5XrU-uYhYb7ZbBXJBnauNPBkaZFTeaMNmudN6Hz7ds6aydSMC1tfZbi2kAJAwFNrJjR2fpobNcPMi2jimLxM5maaOZthDDlK4YxL4I0O2k3qu2xYdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d93912779.mp4?token=GRL6DnqIU8L4-q08eeKW_1OBEk6YA8h3-g8ErjCXpf7AYSnpQ7aWHTIQA4oaANanX05qVLcogLmSnpzLvjG9s_NXIx8-OZbDQPOcRsxixLAb7DOI12W7XAhGykszBz2OR8KeANx8xFMwX4mWKkgqqxYKUgyXn55CmbMSedzb6SO7qbuz0k0kOQWeZ8ybVDRdfxaaQVl3oTCzpI_csUn2GrE6JuWcPzUmR9zp5XrU-uYhYb7ZbBXJBnauNPBkaZFTeaMNmudN6Hz7ds6aydSMC1tfZbi2kAJAwFNrJjR2fpobNcPMi2jimLxM5maaOZthDDlK4YxL4I0O2k3qu2xYdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
إشتباكات عنيفة بين القوات اليمنية ومرتزقة السعودية شمال " الخوخة" غربي اليمن؛ سقوط عشرات القتلى والجرحى في صفوف المرتزقة.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/87252" target="_blank">📅 02:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87251">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lULyKo4XfgumEcMoyjvFbi4fXatjSJeue6vXbbCmPZpollX0G7SPl6zh3AfRkLSA-dbcoB3FdXCA1tsGzozstFKGTe-SJpAnfUulFoXJ5l21QODkPpUdgI-V--1FATy-W6zn5h1VPUDuZyVz0fiX-f9hmSEr-g3HkXboJwJo6l6LOsI-nsqXMI72gwgtYI5mJCewcfEVvDO4SKc3ni3xd5xU8oRmHRRdkXA_zM7ASUbR63IGI3bbzh19TPGzqpEgWd7b65OhFdENo4ZgtDzBY_t6WSieNZ7C_Zp12raM2VdukkD5d9m4IHNDG6CypgoBVa8oHKwfEjk5lFoi4hw01w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترامب:
"قال قاضيان، أحدهما عينه باراك حسين أوباما والآخر جو بايدن النعسان، في حكم بشأن مجمع قاعة الرقص/المجمع العسكري الذي تشتد الحاجة إليه، بما في ذلك مهبط طائرات بدون طيار رئيسي على السطح، إن "كل رئيس هو مستأجر مؤقت ... للبيت الأبيض". لسنا مستأجرين ندفع الإيجار ونقوم بكل ما يفعله المستأجر، بل نحن رؤساء منتخبون من شعب الولايات المتحدة الأمريكية، ولنا حقوق عديدة، منها الحق في إصلاح وتجديد وتأمين وحماية وتجميل أراضي البيت الأبيض، الذي بُني وأُعيد بناؤه، وجُدد مرارًا، ورُمم، وببساطة، أصبح أفضل مرات عديدة منذ عام ١٧٩٢، دون الحاجة إلى إذن من الكونغرس أو أي جهة أخرى. هذا القرار، الذي اتُخذ بعد إنجاز جزء كبير من العمل ودفع تكاليفه، يُشكل تهديدًا للأمن القومي على أعلى مستوى. إنه أيضًا عار وطني. لنجعل أمريكا عظيمة مجددًا!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/87251" target="_blank">📅 02:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87250">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OshOAFwx1KIbvr2FqDhGIZW_uMVdW5GAL_mR-sATdTbnH1lAqG_50ihpuqeJSom6tpRAOa-mNOopEX4ypb9wJkDAKEGJtEoAek1ifO2Mmfk2SAyRS9rhM4GlQKwruDSOp5J62mkoVimXHh8HAD8tAGGfRpwEs8y9TTbw9YwKD7sia_KeA6QKeHDY9Dhqb8hoVPcLUZ4rsHD9KNi7X9QAChnVjLK8soo_b5fCmXtldjNkwhUG9c_LHlujtGjdEyat1eCTD_KmsBExRe0e3kj9XNbcCXCa0b3YT7CDx9exbtZKqDoDyspEnWGsLxP7oa2aCk2powazMC7h_2AInjfsnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ليست دوريات روتينية
يستمر الجيش الاميريكي في عمليات الاستطلاع والدعم اللوجستي في سماء خليج فارس بتصرفات لا توحي بان هناك مفاوضات وحالة هدوء …</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/87250" target="_blank">📅 02:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87249">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c84570fd5.mp4?token=nEu-Zcg0kzbA_Y2wik2eY9Rmw3Gc8M66deJ6D8jBzzFA_2YSnjEWidqZwud8RQm2WzbmWRkeclVl3jpBohl8mWph0aHCkqUMIATBscHV960nXcZmiuOXjzUbT5iExO65lToeNzMP4oXexM0tU87iENQZDV4O5QHpcCDOvyoxbIEZJpain9RU7TzwqZNS510Iflk3gdmMsqV96glXSGZX2oQ_Wl9MN2KtFnppDFpHsYA610hOWgRgg0x1tOBFhXb_szC1Q5aaHns7b_nKaVGU2HM8VLE8npaNP6oLEdx4BXqu_kIpx6244Y_CTZV-GyL6gLGsqe3wS5BM6Tw9TMCOBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c84570fd5.mp4?token=nEu-Zcg0kzbA_Y2wik2eY9Rmw3Gc8M66deJ6D8jBzzFA_2YSnjEWidqZwud8RQm2WzbmWRkeclVl3jpBohl8mWph0aHCkqUMIATBscHV960nXcZmiuOXjzUbT5iExO65lToeNzMP4oXexM0tU87iENQZDV4O5QHpcCDOvyoxbIEZJpain9RU7TzwqZNS510Iflk3gdmMsqV96glXSGZX2oQ_Wl9MN2KtFnppDFpHsYA610hOWgRgg0x1tOBFhXb_szC1Q5aaHns7b_nKaVGU2HM8VLE8npaNP6oLEdx4BXqu_kIpx6244Y_CTZV-GyL6gLGsqe3wS5BM6Tw9TMCOBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الصهيوني:
تم الإبلاغ عن فتحة ظهرت في السياج الأمني في زيكيم، الواقعة بالقرب من قطاع غزة. تم توجيه السكان إلى البقاء داخل منازلهم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/87249" target="_blank">📅 02:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87248">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔻
أي بي سي:
عزل الجنرال شارلز كوستانزا، قائد الفرقة الخامسة المشاة التابعة للجيش الأمريكي في أوروبا، بشكل مفاجئ من منصبه قبل حوالي شهرين من الموعد المحدد لمغادرته.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/87248" target="_blank">📅 01:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87247">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔻
سي إن إن:
الجنرال دان كاين، رئيس هيئة الأركان المشتركة، أوضح بشكل خاص لمسؤولين كبار في إدارة ترامب أن الولايات المتحدة بحاجة إلى "إيجاد مخرج" من الحرب مع إيران، معتقدًا أن الخيارات العسكرية المتاحة لتصعيد الصراع قد تنعكس سلبًا.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/87247" target="_blank">📅 01:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87246">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-ua8icTeG8akzkUH2Asv9eYad93KS0gfWnh_HQoYW2PEK3aV908r71gbHmOB41Cen5edkONeX8wwLVoIw1HNuabk6A73wCq5dMyBGCJQ7BXBA2v-mhyYACu7IHNjCAYN__g_UBU1QLpPNEKB07hFuhNLjNZVL_a50Jv8lTjmairl6qYnIb2E5tsbZyZq07KMGdzAJ5SX9XC34Mpz9QLkpjy2W4ZMFoKVRto1pSkXf_tdCXe2QaAiRYhTgacrs8-7e9xIQtaAtBv-kYt6wATB27a5q2Y0In6x948Vdmg2DWlN8jYYa8gqMgS6aEdt01YI0ARdZ2A3QreUo6bibhhTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
الولائي: إن قرار المقاومة الاسلامية في العراق بالتريث جاء استجابةً لطلبات الإخوة قادة الإطار التنسيقي، وبمقدمتهم الاخ المجاهد ابو حسن العامري والشرفاء من السياسيين المستقلين.
⭕️
الولائي: إن إعادة النظر في توقيتات الرد وحجمه ونوعه لازالت قائمة، وهو واجب عقائدي ووطني يتلهف له المجاهدون وذوو الشهداء والجرحى وغيارى الشعب العراقي.
⭕️
الولائي: على المعنيين استثمار هذه الفسحة لإستعادة حق العراق بما يتناسب مع حجم الضرر الذي لحق بوطننا وشعبنا جراء العدوان الغاشم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/87246" target="_blank">📅 01:16 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87244">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇸🇾
عصابات الجولاني تدعي:
تحييد عنصرين من تنظيم داعش الارهابي كانا يحاولان زرع عبوة ناسفة في السيدة زينب بريف دمشق.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/naya_foriraq/87244" target="_blank">📅 23:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87243">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⁩ ⁩
وليس تكليفنا أن نُجمّل الأخطاء أو نبرّرها. فإن دافع الإنسان عن الموقف الفلاني لمجرّد أنّه صدر من الجهة الّتي ينتمي إليها فهذا يعني أنّه يدافع عن نفسه أكثر ممّا يدافع عن الحقيقة. وهذا ليس عملًا يُبتغى به وجه الله، لأن العمل لله يقتضي أن يكون الحق هو المعيار لا الأشخاص.
يجب أن نُخضع أنفسنا للحق،
لا أن نُخضع الحقَّ لأنفسنا.
⁩ ⁩
زهراء " دامت بركاتها "</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/naya_foriraq/87243" target="_blank">📅 23:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87242">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b3147050c.mp4?token=i0sA0RIwH16_rbGFf2LJ_TfKN5IQf9i40DYWvtoeoPOUVr-G78DBXI36Ty5YUysc6pVzgm-BLXH8RKXcC7BpVReWCEKcqK37CaIXnQJ784adpIRr6Y0iFuuEo3gcBfyBqUzR7XRXnIejJEDpXdecxRt8znG1nnYt7HwxgakwBe9_viuJz-R4LefaALUQaMMapSB37VpuvO1kZhkWkNElLDMOA3uW2GC2KWLpyg3mmpFku-ej677kV7ZtO86vEMqZydMzd_VgizYyr72WkhmLQLBKWzkewSCP_EhA2MrGGQf3jUCqu2zuE4F_3Y1QUphLFwNEBAS-k8aVROTGBWeHzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b3147050c.mp4?token=i0sA0RIwH16_rbGFf2LJ_TfKN5IQf9i40DYWvtoeoPOUVr-G78DBXI36Ty5YUysc6pVzgm-BLXH8RKXcC7BpVReWCEKcqK37CaIXnQJ784adpIRr6Y0iFuuEo3gcBfyBqUzR7XRXnIejJEDpXdecxRt8znG1nnYt7HwxgakwBe9_viuJz-R4LefaALUQaMMapSB37VpuvO1kZhkWkNElLDMOA3uW2GC2KWLpyg3mmpFku-ej677kV7ZtO86vEMqZydMzd_VgizYyr72WkhmLQLBKWzkewSCP_EhA2MrGGQf3jUCqu2zuE4F_3Y1QUphLFwNEBAS-k8aVROTGBWeHzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏
ترامب يلغي مؤتمره الصحفي:
لو أمكنكم المغادرة سريعاً سأكون ممتناً، لأن لدينا حرباً يجب خوضها. هذا عذري للمغادرة مبكراً قليلاً.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/naya_foriraq/87242" target="_blank">📅 22:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87241">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي: ‏هناك تقدم بين سلطنة عمان وإيران بشأن مضيق هرمز، ونتوقع التوصل إلى اتفاق قريباً.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/naya_foriraq/87241" target="_blank">📅 22:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87240">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
‏هناك تقدم بين سلطنة عمان وإيران بشأن مضيق هرمز، ونتوقع التوصل إلى اتفاق قريباً.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/naya_foriraq/87240" target="_blank">📅 22:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87239">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇾🇪
التصعيد بالتصعيد</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/naya_foriraq/87239" target="_blank">📅 22:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87238">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇺🇸
‏
الاعلام الاميركي:
الجيش الأميركي يعتزم شراء أجهزة ليزر مضادة للمسيّرات بقيمة 400 مليون دولار.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/naya_foriraq/87238" target="_blank">📅 22:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87237">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smx7gib2sfMxcjmkeU1ADGnPLV1pjtE1nwiEhJlwx7RR4l-OT79x9uNaoptPY_CApnd6sd2eAt-4w98sKkxdjI5OU0S2p4w0MbBLj7FNpx5X9tuXC590q2DFYaHFZjPbrhPo5QLfC6rWXx79AJoYBl9EW8pGyJtNroZm5TBCKmz7wGFKb2b5ZJwqFLqZvXZL06YN-E1VUcq2ODi5DjleEX6IR51i94xcUhL1clrBynYx18YAtIq8RR1Xs4cdfDcjHjH8IMS9G3O36tR2qDeMaFNE2554_jkhOqsRszV9aHdOoxT1TwJtweyWkfGyyR4P-LQCSPKgd6X70IBtFnuiog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقجي:
أظهرت القوات المسلحة الإيرانية القوية جاهزيتها وقدرتها وقوتها في مواجهة أغلى جيش في العالم.
‏عندما يتحد المسلمون، نستطيع مواجهة كل تحدٍّ من قبل الغرباء الحاقدين وجهاً لوجه.
‏حان الوقت للاعتماد على أنفسنا فقط واحتضان الأخوة الحقيقية.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/naya_foriraq/87237" target="_blank">📅 21:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87236">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/052f59ac5e.mp4?token=lzvW3ZBdAZ6CKfuVrfXh3sKcM0Hvzw2EZxdBgEy4uLOfX6qpjj5qvUaOHnZukdG8O7tEYgnbESTn_jeVC1fY96XMTYleO27eyRiJBRFCmwAftRVhylWNoqkQrihpSpF2ckxZbxQHC9dGwibXX4YUWuYgdZvrskZ69KnoGZ9oZixbRtbj0lRR5L7IoB_qqPq_jGUThJt01Soj_URF_caNvs8kBE5jmUjah_cDtwrMXd9ewGoOyKIC5TrtfQ4qwJ0QsVGNe9NAkw0YSt0U-9RFwZUPQgoAueE0aUUMdjH-sAUXY4fcTtrZJGRUnfpZGuLWn7e2IqRuEhTiZFIPTpsO3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/052f59ac5e.mp4?token=lzvW3ZBdAZ6CKfuVrfXh3sKcM0Hvzw2EZxdBgEy4uLOfX6qpjj5qvUaOHnZukdG8O7tEYgnbESTn_jeVC1fY96XMTYleO27eyRiJBRFCmwAftRVhylWNoqkQrihpSpF2ckxZbxQHC9dGwibXX4YUWuYgdZvrskZ69KnoGZ9oZixbRtbj0lRR5L7IoB_qqPq_jGUThJt01Soj_URF_caNvs8kBE5jmUjah_cDtwrMXd9ewGoOyKIC5TrtfQ4qwJ0QsVGNe9NAkw0YSt0U-9RFwZUPQgoAueE0aUUMdjH-sAUXY4fcTtrZJGRUnfpZGuLWn7e2IqRuEhTiZFIPTpsO3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
إغلاق مطارات أبها الدولي والملك عبدالله بمدينة جازان ومطار نجران الدولي في السعودية وخلو أجوائها من الطيران المدني.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/naya_foriraq/87236" target="_blank">📅 21:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87235">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/87235" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/87235" target="_blank">📅 20:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87234">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">يا ابو جبريل جيب الثار</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/87234" target="_blank">📅 20:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87233">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تجدد القصف الصاروخي لانصار الله على معسكر صحن الجن في مأرب</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/naya_foriraq/87233" target="_blank">📅 20:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87232">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/naya_foriraq/87232" target="_blank">📅 20:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87231">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇾🇪
‏
بيانٌ صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ
‏بسمِ اللهِ الرحمنِ الرحيم
‏قال تعالى: {فَلَا عُدۡوَ ٰ⁠نَ إِلَّا عَلَى ٱلظَّـٰلِمِینَ} صدق اللهُ العظيم
‏إصراراً على مواصلةِ حصارِ شعبِنا، وتصعيداً في العدوانِ على بلدِنا، يواصلُ العدوُّ السعوديُّ تحشيدَ قواتِهِ وتحريضَها ودفعَها إلى أتونِ حربٍ عدوانيةٍ باطلةٍ وخاسرةٍ.
‏وعليهِ.. وبعدَ رصدٍ دقيقٍ لتحركاتِ قواتِهِ ومرتزقتِهِ،فقد تم ضربُ هذه الحشودَ بما معها من المخازنِ والآلياتِ والمعداتِ العسكريةِ في معسكرِ "صحنِ الجنِّ"، وكانت —بفضلِ اللهِ— ضرباتٍ نوعيةً ودقيقةً بعددٍ كبيرٍ من الصواريخِ والطائراتِ المسيرةِ.
‏إنَّ القواتِ المسلحةَ اليمنيةَ ماضيةٌ في مواجهةِ التصعيدِ بالتصعيدِ، وتؤكدُ أنها ستضربُ بشدةٍ أيَّ تحشيدٍ أو قوةٍ يأتي بها العدوُّ السعوديُّ لإبقاءِ الحصارِ مفروضاً على بلدِنا، وتؤكدُ القواتُ المسلحةُ استمرارَها في تثبيتِ معادلتي: "الحصارُ بالحصارِ" و"استهدافُ التحشيداتِ السعوديةِ العدوانيةِ أينما كانت"، ولن تسمحَ بأن تمرَّ المخططاتُ العدوانيةُ على بلدِنا دونَ ردٍّ فوريٍّ وشديدٍ.
‏نجددُ نصيحتَنا للمغررِ بهم والمخدوعينَ من أبناءِ بلدِنا بمغادرةِ معسكراتِ العدوِّ السعوديِّ والعودةِ إلى مناطقِهم قبلَ فواتِ الأوانِ، وندعوهم للمسارعةِ للنجاةِ بأنفسِهم وألا يكونوا وقوداً لجهاتٍ خائنةٍ رهنتْ مصيرَها للخارجِ وهي تتاجرُ بهم وبدمائِهم في سبيلِ مشاريعَ أجنبيةٍ احتلاليةٍ توسعيةٍ على حسابِ أمنِ وسيادةِ واستقلالِ الجمهوريةِ اليمنيةِ.
‏نحيي بإعزازٍ قبائلَ مأربَ الأبيةَ والشرفاءَ الأحرارَ لوقوفِهم إلى جانبِ شعبِهم ضدَّ الاحتلالِ والوصايةِ، ونؤكدُ لهم ولكلِّ قبائلِ اليمنِ أننا إلى جانبِهم ومعَهم لانتزاعِ حقوقِ شعبِنا المحقةِ ورفعِ الحصارِ عنه.
‏واللهُ حسبُنا ونعمَ الوكيلُ، نعمَ المولى ونعمَ النصيرُ.
‏عاشَ اليمنُ حراً عزيزاً مستقلاً،
‏والنصرُ لليمنِ ولكلِّ أحرارِ الأمةِ.
‏صنعاءُ، 24 صفر 1448هـ
‏الموافقُ 7 أغسطس 2026م.
‏صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/naya_foriraq/87231" target="_blank">📅 20:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87230">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بسم الله الرحمن الرحيم (وَلَا تَهِنُوا وَلَا تَحْزَنُوا وَأَنتُمُ الْأَعْلَوْنَ إِن كُنتُم مُّؤْمِنِينَ)  تلبية لنداء الحاج المجاهد (أبو حسن العامري)، وتجاوباً مع المواقف المشرفة من بعض القادة السياسيين الشرفاء، تقرر تأجيل الرد الذي كان مقرراً هذا اليوم، الثالث…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/naya_foriraq/87230" target="_blank">📅 20:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87229">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">علي فالح الزيدي يستقبل رئيس جهاز الاستخبارات العامة السعودي</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/87229" target="_blank">📅 20:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87228">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxgMYEoDndU9n9yrzy6OTf3wG0LLCWVzcUh5QHqij-q4bzpxhjLF-rb6sFEfaj-aegqHLg5hD1-7H7hddpIZv6nR5DWcEVwggIrvisYoqgBSBuunSIA_1Yy-S4n9w14hdEn5UPRs9vOFrw9mOohNesafIbutMJb2wod4yF1aqLAmUjuaCNVZS_UBBgp9GHoJAssOJkBQ_JZ5ooUGdIknkIHnPfodtbq0k57TXeCPeK1nYJFCf2pys1Qdhqm__e4kF1DwH_TC7pagIUZczUZlooEq0Btz1MoyMSdP3TBBYNtnaJwTpxdO45B5o6Ht65mwmMcM1IjEPKHle4aHMmhR0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم (وَلَا تَهِنُوا وَلَا تَحْزَنُوا وَأَنتُمُ الْأَعْلَوْنَ إِن كُنتُم مُّؤْمِنِينَ)  تلبية لنداء الحاج المجاهد (أبو حسن العامري)، وتجاوباً مع المواقف المشرفة من بعض القادة السياسيين الشرفاء، تقرر تأجيل الرد الذي كان مقرراً هذا اليوم، الثالث…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/87228" target="_blank">📅 20:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87227">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">" التأجيل سيد الموقف "</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/87227" target="_blank">📅 19:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87225">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإعلام الحربي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V97MvE2jn00mknTkfs1MWWdDHMpuQhB9U2rgh2fZ5bQzikY7TCGVaTf5WXCJuDn6q2tHRXsGb_EuT1XIN9Y0MytNU7oco0ZBdLF1eviLJUEnxLxCdy7Q4y4DbFC5ICw0M4tqm719N8BZojLJt2koEayOUqIwkTxmav-JmrUqgLeu-SnbN085fhdyYWF66_YIr2H7ORewH6iwbKFFh925RtuVonCK1YfRSuXFBILGAmitoRhrAY4FWNH5n91Dl5JUZsnOrIJVClQtZCNOE0S1zDjvE-A0VO-FLG3wYFjpAmNJxy0eeiyRvRY_TIG1a0vwm-YL-AVMtkkA1pqPSCmQpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
(وَلَا تَهِنُوا وَلَا تَحْزَنُوا وَأَنتُمُ الْأَعْلَوْنَ إِن كُنتُم مُّؤْمِنِينَ)
تلبية لنداء الحاج المجاهد (أبو حسن العامري)، وتجاوباً مع المواقف المشرفة من بعض القادة السياسيين الشرفاء، تقرر تأجيل الرد الذي كان مقرراً هذا اليوم، الثالث والعشرين من شهر صفر الخير.
وإذ نؤكد أن دماء الشهداء الزكية ما كانت ولن تكون سلعة في سوق الموازنات السياسية، فإننا ندعو من أعماهم الكرسي عن صون الدماء والسيادة المنتهكة إلى مراجعة أنفسهم والرجوع لرشدهم.
وليعلم العدو الأمريكي وحلفاؤه في المنطقة أن دماء شهدائنا وجرحانا هي وقود صمودنا، وأن السيادة لن تُسترد بالبيانات الخجولة، بل بقبضات الأوفياء الذين لا يساومون على حرمة الأرض ولا كرامة الشهداء.
المقاومة الإسلامية في العراق
7 آب 2026 ميلادية الموافق لـ
23 صفر 1448 هجرية</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/87225" target="_blank">📅 19:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87224">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇶
سيصدر بعد قليل بيان هام للمقاومة الإسلامية في العراق.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/87224" target="_blank">📅 19:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87223">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇶
سيصدر بعد قليل بيان هام للمقاومة الإسلامية في العراق.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/87223" target="_blank">📅 19:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87222">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇶
سيصدر بعد قليل بيان هام للمقاومة الإسلامية في العراق.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/87222" target="_blank">📅 19:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87221">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انصار الله رجال ابو جبريل يهاجمون بالصواريخ مرتزقة السعودية بمدينة المخأ الساحلية في تعز</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/87221" target="_blank">📅 19:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87220">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇾🇪
وزارة الخارجية اليمنية:
-
أي تكتل إقليمي أو عالمي لن يتمكن من مصادرة حقوق الشعب اليمني المشروعة
-
بدلا من تخبط النظام السعودي بحثا عن حلول للمأزق الذي أوقع نفسه فيه، عليه أن يتجه لإنهاء الحصار وكل الأنشطة العدائية في اليمن
- الأحرى بالنظام السعودي أن يبحث عن تحالفات لإنقاذ الشعب الفلسطيني المظلوم وحماية المسجد الأقصى من العدو الصهيوني
- أي تكتل إسلامي لا يجعل من القضية الفلسطينية ومواجهة العدو الإسرائيلي عنوانه الأبرز فهو يخدم أعداء الأمة، ومحكوم عليه بالفشل
- شراء الولاءات وبعثرة أموال بلاد الحرمين لن يمنح النظام السعودي الحصانة لكل الجرائم التي ارتكبها في اليمن
- الجمهورية اليمنية حسمت أمرها واتخذت قرارها في المضي قداما لانتزاع حقوقها المشروعة كاملة مهما كان حجم التحديات ومستوى تطورات الأحداث
- ما دون الحقوق المشروعة هو الذل والخزي والهوان، وهذا ما لا يقبله اليمنيون على أنفسهم</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/87220" target="_blank">📅 18:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87219">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dk7E75Jd6nXEZAszEBL8fZSByICV3OaGVk19_7gX9ZDKNYVxVeIdFvH7jJt5GRYV5rNU7Y0JE5LNLavy1Pu9PA8bDmBjbfHZhILnZpVBQNoWzobR7pIN96Ko123inbBfGqmx2hGxLJ40vHxC-AgddbUTE0PcYTi-hFSex2aXTfa9fvhUkqflG-QJL-Yqr0ZYCmDlF847M5crKLh7fSJQEf-5KxozAtT_3NunFHOzp0rTHPpEUmKerwNW3Cl5_rDXoL75uasKl45KxIvBl4s8rrKR9WJgUyqTUquvDW8aiPcCE21MtHiQbWOFeKL03LOUQMMVG4I6tgW1Od6wz71_Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Milk him , MBS loves milking</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/87219" target="_blank">📅 18:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87218">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇾🇪
الرئيس اليمني مهدي المشاط: الاتفاقيات لا تسري بأثر رجعي، ومعادلة الحصار بالحصار مستمرة حتى تحقق أهدافها</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/87218" target="_blank">📅 18:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87217">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">انصار الله رجال ابو جبريل يهاجمون بالصواريخ مرتزقة السعودية بمدينة المخأ الساحلية في تعز</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/87217" target="_blank">📅 18:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87216">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇾🇪
الرئيس اليمني مهدي المشاط: الاتفاقيات لا تسري بأثر رجعي، ومعادلة الحصار بالحصار مستمرة حتى تحقق أهدافها</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/87216" target="_blank">📅 18:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87215">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇾🇪
الرئيس اليمني مهدي المشاط:
الاتفاقيات لا تسري بأثر رجعي، ومعادلة الحصار بالحصار مستمرة حتى تحقق أهدافها</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/87215" target="_blank">📅 18:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87214">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نقسم برب العرش خلاق السماء بانعدم الجيش السعودي نعدمه  عيسى الليث…</div>
  <div class="tg-doc-extra">Ahmet Demrak</div>
</div>
<a href="https://t.me/naya_foriraq/87214" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نقسم برب العرش
#شاركها</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/naya_foriraq/87214" target="_blank">📅 18:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87213">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HB5XcqQEd4djhN_Rjx1_fpk3R5x8uTkL1pWVcsMU-MJhOKldiElC-cUV-YTTZHNph-ohoK-xuX6-o8wsm2xJb7mYlG4QgW_ae-7GhzVq_CZVm8mbolFyOm1C0mVebzLTeftZQNtoNWFVU58wwNuEAcGq8X_bj2SXmlDgTniU3aUnm1hu1U2Ah2waS6TIdsIaihEIcyuAHRHFwEp8zYk_J288ZPKdRRDmegmTi1qlmXBzZEe5RCt3DdoeWSJ9VXQFEsnuA9KBIVA_6aZbUPyV_CqNJLNqPEEAFL0hbkJSQfuLMPYniXFB6leFOZ1400X-ML6xBIZ0NpCu0sQbBEi3Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بين عطوة الكلداني وفديو عطوة العامري
قصة عن أمة يراد لها ان تكون مسلوبة الإرادة ، فلا تتعجب بان تتجرا الكويت بقتل صياد عراقي ولا تتفاجئ ان يتجرأ الجولاني عليك بقادم الأيام ؛ ايران لم ثبت معادلة الردع بتهديدات الشهيد سلامي الشفوية رضوان الله عليه ، فمن ثبت معادلتها امام العالم ودويلات عرب الخليج هو الخيبر شكن وفتاح ١١٠ هذا وليعلم من يريد ان يستسلم للحرب المفروضة من ال سعود على العراق ان تكلفة الاستسلام اعلى من تكلفة المواجهة ..
يالثارات العراق
🇮🇶</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/87213" target="_blank">📅 18:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87212">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1GhxJLsnGpLOdVo0SoVLysTV4G-E4qtAxrhUalG4kPk1QxhQqzzJxv0i8923fVlxC1VemsU_38W5c4iZ6mS8-SGYXPp3feyfEAJaio40yziA3Pgy8BNrhCuZfEyQY7iSjtmk-xVdkW7cgALMv30WgRD_jcVqhx9CLBGGPS3ovF2yHczuX1BdF7has_l7rqdpFPcObBiaNHOnqKNdVDYew185qqH7ovPQfg27pkmlYPx0Hi_qy4R-dJC0tIV_vOBaNLo_RioVGqbjCjnRC-Qc1AkPljbwEDQc9b3iSvWoR-CifGu6YeiY4BIdGo2nK2J7nDtlno5RaEM3aKGD8JXRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السعودية والكويت تقدمان مذكرة احتجاج جديدة لدى الامم المتحدة ضد خارطة المجالات البحرية العراقية وطالبوا بسحب الخارطة و قوائم الاحداثيات و تؤكد السعودية والكويت بان هذه الخارطة تسبب تداعيات جسيمة بالعلاقة مع العراق ، والسبب هو للاستحواذ على حقول النفط والغاز…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/87212" target="_blank">📅 17:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87211">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🌟
🇺🇸
‏محكمة الاستئناف الأمريكية تقرر ايقاف مشروع ترامب لانشاء قاعة الرقص في البيت الأبيض بكلفة 400 مليون دولار</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/87211" target="_blank">📅 17:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87210">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇦🇪
شركة أدنوك الاماراتية:
تعرضت 15 سفينة تابعة لنا للهجوم منذ بداية النزاع.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/87210" target="_blank">📅 17:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87209">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇺🇸
وزير الخزانة الامريكي:
أعتقد أنه قريبًا، ربما حتى اليوم أو غدًا، سنشهد اتفاقًا، ووقف إطلاق نار لمدة تتراوح بين 30 و 60 يومًا، وستُفتح الممرات المائية.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/87209" target="_blank">📅 17:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87208">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3686bd868d.mp4?token=R1neYWBcyOCkWYa96aORAXYGWsW85eyyon5rP29Skvff8TpeXWsy_ISesc_wvgWQW31uU-6kqNbmQ5bOeNEplrHOkc4v7uv-MPxhP0VOz0DsVECr6W551QOPL8Li_qi3ITvRkGf9VBI1uxp9fdzhG1dHA8Ans_GXADNdaXTTt0mEXU-GnoYIJxl6eqzT-xHCJgESwQrnTo-18ujpxNZ0wopZTZJmpiKo91mYXP8xijp3C_J5zWcULLdbRZvbfpjZ85B953UUjj04ENK-pzc59o3nRRxEeeN2n28wvKw8cqnPcwA78ngI8tBZcAy7BXSvY8PTvDxq4PjLKV-4vS0a6I9lkfK6B2lXyKLhwKfzWVYvFpuwTsAo3l0_cs4y8pVyD9KxEzJjlniJCmCYMUR-WjByp-bgUlXqyGTYdCARKs11FMUV21xfBtqypFn0diQGDwQytUqTkraGSPrOiV1-blCBVruQsI5OsJ2Pdcg9M7HzoPTA1yApzsbjjLIYVgXbNkPGda_Dzgt2xTInjdqQOxvGbX00RwwG9Bvv7pQs0JlyQiTJ3furLyMiXsocKy3O5dFO7oRPaVPL0tWWQF3z-5qqttEh2-cQnzkeNnKO3-cgiCGorx-m6QSpKElcT-IzfL7c2JD6HrK0nTzipgpr-krGHxNehVn8U6e86yNeZkM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3686bd868d.mp4?token=R1neYWBcyOCkWYa96aORAXYGWsW85eyyon5rP29Skvff8TpeXWsy_ISesc_wvgWQW31uU-6kqNbmQ5bOeNEplrHOkc4v7uv-MPxhP0VOz0DsVECr6W551QOPL8Li_qi3ITvRkGf9VBI1uxp9fdzhG1dHA8Ans_GXADNdaXTTt0mEXU-GnoYIJxl6eqzT-xHCJgESwQrnTo-18ujpxNZ0wopZTZJmpiKo91mYXP8xijp3C_J5zWcULLdbRZvbfpjZ85B953UUjj04ENK-pzc59o3nRRxEeeN2n28wvKw8cqnPcwA78ngI8tBZcAy7BXSvY8PTvDxq4PjLKV-4vS0a6I9lkfK6B2lXyKLhwKfzWVYvFpuwTsAo3l0_cs4y8pVyD9KxEzJjlniJCmCYMUR-WjByp-bgUlXqyGTYdCARKs11FMUV21xfBtqypFn0diQGDwQytUqTkraGSPrOiV1-blCBVruQsI5OsJ2Pdcg9M7HzoPTA1yApzsbjjLIYVgXbNkPGda_Dzgt2xTInjdqQOxvGbX00RwwG9Bvv7pQs0JlyQiTJ3furLyMiXsocKy3O5dFO7oRPaVPL0tWWQF3z-5qqttEh2-cQnzkeNnKO3-cgiCGorx-m6QSpKElcT-IzfL7c2JD6HrK0nTzipgpr-krGHxNehVn8U6e86yNeZkM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇰
انفجارات تهز عاصمة سلوفاكيا وتصاعد لاعمدة الدخان</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/87208" target="_blank">📅 17:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87207">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇳
🌟
وكالة رويترز:
شركة ريلاينس إندستريز الهندية حجزت ناقلة عملاقة لنقل مليوني برميل من خام البصرة.. الشركة دفعت ما بين 23 و25 مليون دولار لاستئجار الناقلة أي نحو 12 ضعف السعر المعتاد قبل الحرب مقارنة بنحو مليوني دولار فقط عندما كانت أسعار الشحن تتراوح بين 0.8 و0.9 من السعر القياسي. الناقلة ستوفرها شركة "سينوكور" الكورية الجنوبية وهي واحدة من عدد محدود من شركات الشحن التي لا تزال ترسل ناقلاتها عبر المضيق، رغم تزايد المخاطر التي تواجه السفن التجارية.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/87207" target="_blank">📅 17:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87206">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇶
وزارة الداخلية العراقية:
الأجهزة المختصة رصدت خلال الفترة الأخيرة ارتفاعاً في معدل الشائعات والعمليات النفسية التي تستهدف إثارة الرعب والقلق بين المواطنين، الجهات التي تقف وراء هذه الحملات تعتمد على نشر الأخبار المفبركة والمقاطع القديمة والمعلومات المضللة عبر مواقع التواصل الاجتماعي، في محاولة للتأثير على الأمن المجتمعي وإرباك الرأي العام، أن هذه المحاولات لن تنجح في ظل الوعي المتزايد لدى المواطنين وسرعة تعامل المؤسسات الأمنية والإعلامية مع ما يتم تداوله.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/87206" target="_blank">📅 15:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87205">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTKa_2CKJWmFMujQlxMwiCN4XxNTgK1v77qawsgcbR9izZUwrPZ0qmBRTkPWLkDSFQdgzLkgLQErRKcpqe9-siD0bHeMBzwXkSKPJoVrvAeed4fgKiqKci2wCYkvJFW_yFeIknxgwEkI9nAjGtjyWgIn8w51F9khZP_KiagqbgxRH8E1pydOMStA4X7zpe5J73sbwy2uM5lqi3570Ze4bHW9OeZAfvdnFp8K9KxantuvXgNcVsL_D5egOSsL41wNsyYCDd1XqsG3BJC-RYiGMgruhRRLAY_vsU50JYcMMEhxJ4LeO_XE3oQgoW4N_dB-CYokZDa0vKcsxCTUPEzAZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو لجنة الأمن القومي في البرلمان الإيراني إبراهيم رضائي:
ينبغي للسعوديين أن يدركوا أن اتفاقية ورقية مع تركيا وباكستان لن تجلب لهم الأمن، تماماً كما أن سنوات من الاستغلال الامريكي الأحادي الجانب لم تجلب لكم الأمن. أصلحوا الأمر حتى لا تضطروا إلى التوسل للحصول على الحماية من الآخرين.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/87205" target="_blank">📅 15:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87204">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇶
هيئة الإعلام والاتصالات العراقية:
لا وكيل رسمي لستارلنك في العراق وكل من يدّعي ذلك يواجه المساءلة القانونية.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/87204" target="_blank">📅 15:07 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
