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
<img src="https://cdn4.telesco.pe/file/FOJyG5gHHVfU2sXXLbn-Z8PiZmU5QdtWndfd36p40dN8FOcvmuj4w36Hh9Gh8sUit43oWsah-HGNY6i_bjZ6Qca_sHy09VtlKZ-zZ5hIRs4vSdLeHCaQhHEKiBSGlnkdavZhYwGB9q5XQU4FYHZvdB5Mvgi_3Mc_7r5wlfwjsTFVi_xQvgQm2gQ7PD5lp7_Oo6OvWV_UkEksVVdpSJEjju1DIqWW2IqbmDGEsyHhlblFZKBePPdx9emDiqWkZPVPFwwSgp0j_G85SykHS3iY0dI0jXMG7eg3AtHmOizoZVuF1gYLVWhNNeXUWWz7fNtGlfwRph934fRWJYL9IFMcUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 22:20:05</div>
<hr>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=ezFYgq1VMDjVhMjTBLatgSuaowqRgDoBB99DpJiNRKkSPioKCf5Jppep4z5Qy6HsrclIiCMZxbXMIXqrZAahgfzHyYMxgGXmYX03PM5I_3-NTemDtIl_HZRGVwV0M-sg4sHzhQpmWT6InrFAvkmISWgSLUP3M2whRwEmjiu9QKs7cqFjkQh8siFbOF69VQzNZu7YMr758RIseHylzzi0uRgJbfAIqm3rlhVFQMQ2F3sktdIVGXuLSqRQOlFxB8KSxPliMjBk8WQyPLG3yr0tVB-H5wYqZ4ck2D3FZqeohZj-YgKdzCrLzp-VxqQ51J047QwjmdvZszzzjVV_bdNUmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=ezFYgq1VMDjVhMjTBLatgSuaowqRgDoBB99DpJiNRKkSPioKCf5Jppep4z5Qy6HsrclIiCMZxbXMIXqrZAahgfzHyYMxgGXmYX03PM5I_3-NTemDtIl_HZRGVwV0M-sg4sHzhQpmWT6InrFAvkmISWgSLUP3M2whRwEmjiu9QKs7cqFjkQh8siFbOF69VQzNZu7YMr758RIseHylzzi0uRgJbfAIqm3rlhVFQMQ2F3sktdIVGXuLSqRQOlFxB8KSxPliMjBk8WQyPLG3yr0tVB-H5wYqZ4ck2D3FZqeohZj-YgKdzCrLzp-VxqQ51J047QwjmdvZszzzjVV_bdNUmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=tYr9DQzzVhF9xThvGTCxcPuovewN8pWhd2YAiiTXGfEOLYA82-UgvI9VvPos7J5Wg38pj_RcSimE3qnfyN7_Qxeb9TR3D9-49QWk_8T1M2UacXnDMMGKuCvk4W-hDQtbHc1S1x4ry6ABPgtiszxpMrxXUGdDegXYCa5ETD-Wx2vp9-IDNPFe37L5Tkdjyq4dXZTCv6IQ5EVkOAK5RKm0oJSYdBrNUc6EamFjRQ797DKGtjIj8vOae3IBfu_grDiuByzN1vtfgld364M_MZTgb1PO_2i_BLULKKgfmDL1Ro1Sm77nm4VcRNqNe4dgULL_ow3pmSHSTxfQuZJpgsobMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=tYr9DQzzVhF9xThvGTCxcPuovewN8pWhd2YAiiTXGfEOLYA82-UgvI9VvPos7J5Wg38pj_RcSimE3qnfyN7_Qxeb9TR3D9-49QWk_8T1M2UacXnDMMGKuCvk4W-hDQtbHc1S1x4ry6ABPgtiszxpMrxXUGdDegXYCa5ETD-Wx2vp9-IDNPFe37L5Tkdjyq4dXZTCv6IQ5EVkOAK5RKm0oJSYdBrNUc6EamFjRQ797DKGtjIj8vOae3IBfu_grDiuByzN1vtfgld364M_MZTgb1PO_2i_BLULKKgfmDL1Ro1Sm77nm4VcRNqNe4dgULL_ow3pmSHSTxfQuZJpgsobMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=GSqYEwDnDhV5v_z_Xi6L6GWzVouqjr6JOUYDCA8WP39VMYULvMtW90ggmBPWFpk02RwVRHxUU0yxxssFKkO5sKKE0QUwaOVURd9bxAI88bb9xdfv54Ku252LKEEM0tNiwkEvRGy05WreP3CK_tFSdJj75FTmVT1xqJvRa5t9APlGf_NvLQU7P8zdrk0KhAc234Ge72Gb1dLsqXpbp5pFjnDcY7TUA7LlEl30hMLRxvRkz192TlnNkFgWR9DIG_ylz1I_FPVW-tYBrEitIGwZ4TFNZdS2DOBliAt7lmr-h3TdNyRm1TE7lIp2zunD59nZbJ9INPifS6sSuxEhPMpMIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=GSqYEwDnDhV5v_z_Xi6L6GWzVouqjr6JOUYDCA8WP39VMYULvMtW90ggmBPWFpk02RwVRHxUU0yxxssFKkO5sKKE0QUwaOVURd9bxAI88bb9xdfv54Ku252LKEEM0tNiwkEvRGy05WreP3CK_tFSdJj75FTmVT1xqJvRa5t9APlGf_NvLQU7P8zdrk0KhAc234Ge72Gb1dLsqXpbp5pFjnDcY7TUA7LlEl30hMLRxvRkz192TlnNkFgWR9DIG_ylz1I_FPVW-tYBrEitIGwZ4TFNZdS2DOBliAt7lmr-h3TdNyRm1TE7lIp2zunD59nZbJ9INPifS6sSuxEhPMpMIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=WF7LcbinBGMWFTE2OpauLPOMEB7TjHx-uYM9l-q3dOlJKf4a4Ratm-XaXMvinpI0dz0xCR2GkPBh0GAYOeA6ebOzAQVHuU5QEF3p6iDJ--WKiVpi32aAWxuMc1ieEdPknkXnji3Nk3JMsVxL9Ht9zbtLfkHq6T-jqVQa7foo-MGna0uK-i1AqE7buRYh7pIHX-3N4zy0rI2TtoxZt_h90su7LD3msX7t5_suB-W_Y00zv-jr_9Dy_0ztm-kdsW9M_qMd41rJKnKYOO-4bo4rTW0AWdUnmqyzrPWrHl9JyDoiZD1MRryvUWLvS4fAAEDKHy9pn9XA8HyyUpcX-Wrp_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=WF7LcbinBGMWFTE2OpauLPOMEB7TjHx-uYM9l-q3dOlJKf4a4Ratm-XaXMvinpI0dz0xCR2GkPBh0GAYOeA6ebOzAQVHuU5QEF3p6iDJ--WKiVpi32aAWxuMc1ieEdPknkXnji3Nk3JMsVxL9Ht9zbtLfkHq6T-jqVQa7foo-MGna0uK-i1AqE7buRYh7pIHX-3N4zy0rI2TtoxZt_h90su7LD3msX7t5_suB-W_Y00zv-jr_9Dy_0ztm-kdsW9M_qMd41rJKnKYOO-4bo4rTW0AWdUnmqyzrPWrHl9JyDoiZD1MRryvUWLvS4fAAEDKHy9pn9XA8HyyUpcX-Wrp_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0oBrXt_6lCiYrIvM3CWsUTWuxfDUW4J0z6G59N9tqNRK_UYGp16m51FZtVb85CngRTdtkQkv96HPbGJp6-VFaTw36QjDU6vmgfPF7bwS9DaqT7wHmUl54PPGEexsoVKdKAEhE8XOzIqtmUvEehuu6a1haCoq6FFa238Qh8CLYAZBNk19aqUHcXgexFt5nHNplyYrGzAaqJ45lF64dU2zJOOiBkjYcSU77aIpMWm8vZYhSRbu0JlrtBzJYOETnfLUcw-n_4meOttVoNvluKnnc8P6smjncsBDM1hCbB3PTuqkHsMiKKpHVN69nqwEpcgPC9gMTsyZ-Qn2eRoXEJ6QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=ZuSArq9OoO3n6G7QD_08Xw4fg2Oz0U5B6X94PKD_dvNW3v3gAYr33TJD5JPhEkfwzCm6-SzbRwnQ3qJ3iE5YjdEdqHX7VLxnO1UGefWKr5Lx-ASFSzVuawwy2Y4LcpjH5BbCpiqQu2_i_hGaCpSQnt-3-5U-8S33vTp6aMB_3BmmrwKHZKDzXGO1t1UXdujV4uypM_KSqcCzB7jCJsP2oF7zGc95H930qrrB3wF_ms6BbTGcdwFATPQhMHM21N5fqrdA1mde89Hi-3z8Bu351gboHfSzcNFje43G0SkmUO2CDK03-A5WPDoj0op2hKPH5STbLrgcagTGnZT7X50IHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=ZuSArq9OoO3n6G7QD_08Xw4fg2Oz0U5B6X94PKD_dvNW3v3gAYr33TJD5JPhEkfwzCm6-SzbRwnQ3qJ3iE5YjdEdqHX7VLxnO1UGefWKr5Lx-ASFSzVuawwy2Y4LcpjH5BbCpiqQu2_i_hGaCpSQnt-3-5U-8S33vTp6aMB_3BmmrwKHZKDzXGO1t1UXdujV4uypM_KSqcCzB7jCJsP2oF7zGc95H930qrrB3wF_ms6BbTGcdwFATPQhMHM21N5fqrdA1mde89Hi-3z8Bu351gboHfSzcNFje43G0SkmUO2CDK03-A5WPDoj0op2hKPH5STbLrgcagTGnZT7X50IHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=fQkG6mrm29iUQt9ZKrofCJrg5BmIzT7qJH_LgVeN0FsjxZvvQRFrgti-VvYDnvajoPRaKnouPwyaDTR53rQUktdLIikRZXgBo6V2tQjorEs2KR1VMYy4i-bzzRnv97RYojm9gMMYeVrYhGZ4Ve1zJn1r9FJG9JZct7qCzgmrm45bfijljIrV2YlJXv9pxC0hJj8Y2j4dMBEGjnse_joCLXDytJPYJdC3nSAydJsNPZDDOBsRmmVLsPEMTZe7SiYv747_liPHcWt72WVtyonZWo0n8H_KvgJEczEf1ni0Ms5w3bRggWQPHfmR_6jab3jBMbIAH9-juEmVAM2AenU1ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=fQkG6mrm29iUQt9ZKrofCJrg5BmIzT7qJH_LgVeN0FsjxZvvQRFrgti-VvYDnvajoPRaKnouPwyaDTR53rQUktdLIikRZXgBo6V2tQjorEs2KR1VMYy4i-bzzRnv97RYojm9gMMYeVrYhGZ4Ve1zJn1r9FJG9JZct7qCzgmrm45bfijljIrV2YlJXv9pxC0hJj8Y2j4dMBEGjnse_joCLXDytJPYJdC3nSAydJsNPZDDOBsRmmVLsPEMTZe7SiYv747_liPHcWt72WVtyonZWo0n8H_KvgJEczEf1ni0Ms5w3bRggWQPHfmR_6jab3jBMbIAH9-juEmVAM2AenU1ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=pTcoW9i2QHip8fIBXF0dqclcHgCGHO_9pwrL_60RTxkjKz5ecVrysXvtzaCQbNb7bTgbY506rYgay_ZV2siDa7aaunMlZWPoWzYOa66b76XUAA_f-NE35rQHBvyx6Jv7MQsownB0kw8h3xoviclT3PkDECu8w_A9Y09NuHF7eoIRflUwIwy6NZf6dWaZSFj5KcNsreMWqNi4MFeHe2q4k8bt1AuP8wpm0IMw6bOm79k6kXSBJcNCYZj2_WMs8HV48Puq5dMzg5DqY-TMzdqgk9lFHFJHkVRK56zUtrk4eGYGI1FTFHg-3iM7cU8sEOUvnpCDEVVRlFvbA0LT8q_-3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=pTcoW9i2QHip8fIBXF0dqclcHgCGHO_9pwrL_60RTxkjKz5ecVrysXvtzaCQbNb7bTgbY506rYgay_ZV2siDa7aaunMlZWPoWzYOa66b76XUAA_f-NE35rQHBvyx6Jv7MQsownB0kw8h3xoviclT3PkDECu8w_A9Y09NuHF7eoIRflUwIwy6NZf6dWaZSFj5KcNsreMWqNi4MFeHe2q4k8bt1AuP8wpm0IMw6bOm79k6kXSBJcNCYZj2_WMs8HV48Puq5dMzg5DqY-TMzdqgk9lFHFJHkVRK56zUtrk4eGYGI1FTFHg-3iM7cU8sEOUvnpCDEVVRlFvbA0LT8q_-3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=O3qzpMSIHoJMHIbsQdZC3CyJOMG_QfrDSh3kx7XzP4nDnl5fzGlQWz-ILLhw6wtYLwX20nB7xGPstNOYhWa_LGWo2rMt_0l6Dokpunws_M1UXzkELvwcaySJzSLzgltJyH-d22VFBZPKfpjt5SKF1C70FX7zZADKEizL_5c4bXR-tF9f0q9bISY9VG-lmVcYoQRkVehiZsIXkEBG_OnnXN04o77nKFkxjEfVGQmTwpAUT5yhtfJVx5udSj8myuT6kLs0X4SJfEJTa1VSxoxc1LGbk1mLwsZyMwoCDnlaVR80vOhnVKf2pWFvy3j45PjTlRGi-iKkpiUWU6uQbWnJVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=O3qzpMSIHoJMHIbsQdZC3CyJOMG_QfrDSh3kx7XzP4nDnl5fzGlQWz-ILLhw6wtYLwX20nB7xGPstNOYhWa_LGWo2rMt_0l6Dokpunws_M1UXzkELvwcaySJzSLzgltJyH-d22VFBZPKfpjt5SKF1C70FX7zZADKEizL_5c4bXR-tF9f0q9bISY9VG-lmVcYoQRkVehiZsIXkEBG_OnnXN04o77nKFkxjEfVGQmTwpAUT5yhtfJVx5udSj8myuT6kLs0X4SJfEJTa1VSxoxc1LGbk1mLwsZyMwoCDnlaVR80vOhnVKf2pWFvy3j45PjTlRGi-iKkpiUWU6uQbWnJVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grT1IV8p2uZrOz1ma8v9ymcZ8N_fcVPClbus-hnp6_KVfyNPG20yVE5d9eO_JvK7Zl-lV2uz8RBDiRLV8q8vyDT9epBVr8gaberG1Im3FgK2f3QgHYhlo3o-WSTmj8dN0rFt4TXrB8JRiRMOYE2fnhODQCuAfh2PO9ru33VqNJe9qnSaHNVfmkYm6VgTDVnYOwBj5X78A-19xlJrZEoQkk3CLWpCcrj1U3SvOhrb6k3wMwhRd6s2OaZDQOV5E89dM4YwGU2S1p6zMVTNt5xP6o3Z9NiheDLaGg6VkYupWHBbow0JsbF1ZTwFbyVTX34KVyI0JxCURQWwnuQZxhojyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Lp2owU9-4FFKlWjcGiFB40L6gfVxD-paBMQ9NHWBgrp2UYWorNHkV5NeHTqKButK8_DSXhwxKij_f6ZMuBG_9s4EtAT40l_w2u7H0nihQZvo5uONV29OpZ27QTPaqbFDKMDs0hHYbVWC4Ffh2l43kbYYJLSw0ByGVDkoj3r-TkL8E0viPYNUvIb-tO_hHg0ArDo9qU1wxG_JWn20EZwLpQ2AWMhchnQ1X4uxzpJ7F_YTpF8DXua8D47A25cHDFjR9XYaYKQ7m5wd9NfSxhisFe-j4CDoat75igJquR0fylZfEIP7qU4WV4thj7qA5oEKf19lCxlyrya78zDKwJiPTYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Lp2owU9-4FFKlWjcGiFB40L6gfVxD-paBMQ9NHWBgrp2UYWorNHkV5NeHTqKButK8_DSXhwxKij_f6ZMuBG_9s4EtAT40l_w2u7H0nihQZvo5uONV29OpZ27QTPaqbFDKMDs0hHYbVWC4Ffh2l43kbYYJLSw0ByGVDkoj3r-TkL8E0viPYNUvIb-tO_hHg0ArDo9qU1wxG_JWn20EZwLpQ2AWMhchnQ1X4uxzpJ7F_YTpF8DXua8D47A25cHDFjR9XYaYKQ7m5wd9NfSxhisFe-j4CDoat75igJquR0fylZfEIP7qU4WV4thj7qA5oEKf19lCxlyrya78zDKwJiPTYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=SFny1EV0pLB7td35-R4uvuwk0qgez3cPcXiPXNMSMIHjLHSgui_TB-Qg5VDb-Rvze0NSPThdssKA06h9iEBvsm1pK6PZAxKBVhGCBugCJq4zFhlSinoXVW2cvEWuDnPkegaNAqmOcq1MAm_1NRYKlmkMz2zjbPl8v5iRdt8HM6XcuVyOUAuyqOPGPQJAT2v0BEXDS6ZS8ybtDbUgm0HIS4b2UBgRPKnDIM5Y3l-Sp_M9pxmXdC2LcLpQFFIpkFl_9pqi_xNb07sO12kpRJ_0xegyVzIgCVX-t_9F14DyZjAVXzSFtz8Pfksztr8RFqNfMRnrXknkLeZWOCUsRrMd5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=SFny1EV0pLB7td35-R4uvuwk0qgez3cPcXiPXNMSMIHjLHSgui_TB-Qg5VDb-Rvze0NSPThdssKA06h9iEBvsm1pK6PZAxKBVhGCBugCJq4zFhlSinoXVW2cvEWuDnPkegaNAqmOcq1MAm_1NRYKlmkMz2zjbPl8v5iRdt8HM6XcuVyOUAuyqOPGPQJAT2v0BEXDS6ZS8ybtDbUgm0HIS4b2UBgRPKnDIM5Y3l-Sp_M9pxmXdC2LcLpQFFIpkFl_9pqi_xNb07sO12kpRJ_0xegyVzIgCVX-t_9F14DyZjAVXzSFtz8Pfksztr8RFqNfMRnrXknkLeZWOCUsRrMd5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EueTBuooCvwrY2vJWGheBKARvS4U0e4RjQ5XUI3XFJ51_rTa1W6mDVUaZDz_aCvZIf3X7E5GRiSzXDBP1HR3OnoQMJmgSt6Ms3D8tj3cyYBHqBTU8Xs9k9Lv9_nfiIFFPERk9WlkzWzYJGrWR_7ga14EPIbhPaUFLXRh1hIGrz8_Jqk1MI6_0X7HkeZq91rNLJAgiVuH0oY6VahS10My3z7nxxY25S9mRWhxHZ6pOTjH6yWA-68SIIHCSRsVJ6guAUN1WB9q6-NZ7CBCftW8uFd6MNtbPAEVZ47dkaxWhBg28x1JAfSESfOIeyiTcJCHZO0FQJbfJdsveJlk95UJuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-Ar6sCX37U0o1Jnx7--I5kqmQhmoKVALNiwRQdCxsnBbIWAOMNoY7VbEAY-50fgDBq3lRdxg4gHrJnf8_cwE2JzH83JCFk-4NG7qibfNFHubQnEpR-YuAEhFLTSIbDSQNh9f6999H8qxJWIRbOFFRYLB3Xbk-cwZ8xk63cByWi2rPDBQU8dpqXUArPs9ki-o1f-Em1t1E3sQckWN45UV7ExRXvSmGIjovngHv42jV8Mpa-WDolmwN41jqqU_MBoNDk5iXiJwtOpOWouJ1rHmhOaN9a2U7-kZpHI7o1Hy5hE5OYamJyJcROXeiWJz22JHqJOfMF3oTUERXNc39qGQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=FmGZ8kA4GrtqVZmDtevZv-oZbx1YammrBnk0V5KNL7BPibq5t3tlJbe3FXttotwd_LbPJFj0OtQ_NKz1oZ6R5btEsxujqOlsDukKM39-kgtLohUQqV88Z0Wsp39VDpmmlB51AYZZ2I8cxauQEuZsMAAwyzN8AxoiuxAoZKApAlcThJ7mXl3fCPhi8iZWBY8RQX8y3o8lEXUbL7eBh38xuU3cbA14eCb_8O9ySOqbgma7HGQj5BDUgtBjvSzs2diLtGInIsGU_iunGEHDCxbpGI7qOwAt3uS15GGV8edPeVyt1GqxIxSduSXK92tATXEi7mXE6gqi3t5BXpFERw78aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=FmGZ8kA4GrtqVZmDtevZv-oZbx1YammrBnk0V5KNL7BPibq5t3tlJbe3FXttotwd_LbPJFj0OtQ_NKz1oZ6R5btEsxujqOlsDukKM39-kgtLohUQqV88Z0Wsp39VDpmmlB51AYZZ2I8cxauQEuZsMAAwyzN8AxoiuxAoZKApAlcThJ7mXl3fCPhi8iZWBY8RQX8y3o8lEXUbL7eBh38xuU3cbA14eCb_8O9ySOqbgma7HGQj5BDUgtBjvSzs2diLtGInIsGU_iunGEHDCxbpGI7qOwAt3uS15GGV8edPeVyt1GqxIxSduSXK92tATXEi7mXE6gqi3t5BXpFERw78aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmwYwSxLQD1g7BM8MkzCM_QATzx2xcdNZQVFkBwiQ4LsKuGHCfuHV_B7h1SRwcbt6YuF3u5-dtBzf5Yw4vrSJZwGrE-9wycf1gFNOt99gvievyT8jVZsC8Xc0sMozi5Q-rRm3Rj_4jHu7aKQg5CA8bS3qi9l-L1WK6zjyHvEjPvnbx5agOaUaQVzw6Qvt_QcKlXZELC39ivrzrIB973x-E37CkFDib7cq2qM5Z5GmS1h9FwVxZQN2oXyNuM85sZkUhsoZHLgyl1QGjKd46DfyNBG4ffCaRChUAQfxPLtih_aVQzYS_eqrQV2eoxfyxJ-TOOG_0dIvlC5djlzmiNVBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ksbhiu9ABNbem22xPgBXxK-vNPCX2qBofXi_wTOle062TyXvkUfAALebsjFUtOdojiM29hSnM10uAgPzqVnov9a61JAI1n5vHtHmnOBKHSFGw6GyfC87VGe1EgYV_WVhn9nbkn73qSAIlas8n_DfC8B01l4sJy6-a7zJRM_cxi7cN2FXd9EPGhII6cr5kB36Qnar--UaT02PsvRxXzJnltUO1RMtcnM1d-j_bkuKW3Q6cdAo1be9h4fj9PfjDfNsVKWdbfJeYjW1_s2wbBPQYNAYVKUW6a1S6jh7HJLoFK7pR5jhkqMXw5NfNpPZ77EofJmvgZRTveB5Yp1gsYKrQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlW2DA1SrUbLDQh8E6ziP3Ig5ppfRVKw5DeP3GDA0rCkc_V4WqzcqTF9g72XP8lmqLkaX1FreBoZNjFYT1lSFGiBJgIRKKSeFnbBWlHSkS2YiiEo8Tqpg6vAp4mmqIB5r0-UpIDhRdRM411ZBJ1zZIcqYqk5FGXdVBhj_N-knnDiQMyeu7Pr7RNdn-3LyvdH-cYhQOM3vy-5tzCCYEpXoeBrH116ZxJpbRUp0XoTg_ItMt0yYlUNB273l9_59by6itjQ2DyN_Nt57ww4tw_D1ERm0iMgwrUu21O5AMiW5WBCGTcU8xGYk5kSLAP387eGdDLYwQ7Gdbr9ajCpId0TvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=rETAhiMVA2hh7zN8Gs1_2vw1taZN_M6zD9d-SNdw--h2G-HLKYH91TMgiCJ79JnlJn5KoPquGBbmRuU5H1vxwPo-k3MNAcsLzlqEFVpyLiHwufB-aqmSmOhQAXLHrhjq8PXiQkIhukayCirEthOKNOGFi1xrMUiNcK0cvs5kUyDT6jaKEaD-_RxylzEa77UGgWRueF-OiQXh-yS4f8UZyVb-C1AAzgSM_qVUY9lUzDwmAt-fGfqXZDXddjk5uzFGvYYFjRarjDFy-U2USOaSoD4PkSBqfjNb3XEv9cCnsousTflXf_AJxRJPG8Y0cNrwxgsv_aL-Nm1FydYpii4fPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=rETAhiMVA2hh7zN8Gs1_2vw1taZN_M6zD9d-SNdw--h2G-HLKYH91TMgiCJ79JnlJn5KoPquGBbmRuU5H1vxwPo-k3MNAcsLzlqEFVpyLiHwufB-aqmSmOhQAXLHrhjq8PXiQkIhukayCirEthOKNOGFi1xrMUiNcK0cvs5kUyDT6jaKEaD-_RxylzEa77UGgWRueF-OiQXh-yS4f8UZyVb-C1AAzgSM_qVUY9lUzDwmAt-fGfqXZDXddjk5uzFGvYYFjRarjDFy-U2USOaSoD4PkSBqfjNb3XEv9cCnsousTflXf_AJxRJPG8Y0cNrwxgsv_aL-Nm1FydYpii4fPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=JC-oOCrD50DNiNzmvgbTNzkSmBcEkTt5821TOtl0cJtaLWTxSNhOZ4st0iOJ2amJSVAmMlRtbcmX-24-kZegTYixmq_hYtqJjy2oPjmmbVsNQ8sgJNVIlk3uc0Z9OQUPQo8EEt7yOJj1hB-HbglmGxFIB4FjQuo4CSfRNbj8Nci9Eo1tm1nRuz-emyEmrmA-7HiwiwObSUt3CjmssMfjevMooaTi5n2oCcjtHqRhShbkTQvjazPiSD9IdWVfIcHdTruPkKkXvb7Ll62dmXTp3uJmIrI1RWUC1S_Ul7-HekSuUyUf5qeqA__zaYLNVhwnGpd9v-TAD5oVnB_68dwRGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=JC-oOCrD50DNiNzmvgbTNzkSmBcEkTt5821TOtl0cJtaLWTxSNhOZ4st0iOJ2amJSVAmMlRtbcmX-24-kZegTYixmq_hYtqJjy2oPjmmbVsNQ8sgJNVIlk3uc0Z9OQUPQo8EEt7yOJj1hB-HbglmGxFIB4FjQuo4CSfRNbj8Nci9Eo1tm1nRuz-emyEmrmA-7HiwiwObSUt3CjmssMfjevMooaTi5n2oCcjtHqRhShbkTQvjazPiSD9IdWVfIcHdTruPkKkXvb7Ll62dmXTp3uJmIrI1RWUC1S_Ul7-HekSuUyUf5qeqA__zaYLNVhwnGpd9v-TAD5oVnB_68dwRGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=RVSlvgsMTocBKKEgfEgVNMjcvR2p-Q9uU5WurbBcvR9WG63YqVqOLEk-JoNa0tTZ4FBB7Z_Gj7hG1JyBrqyIwQ859ifrcr7ux64pwjS5a7NadapnooJ_ljz9AdACFqdLoYXiadFYIBmHop6olpRpw8v68wNVzYpHN6HhlTE4UocdhOOSdKGYAQ9StkABnQZM8itiLEfz2uPl8CKkbnuCRf8NwsVh7wjUyta9TgabV6RpMiYkX5iyKeoz3-DP9byQn8vr3gwI-4tVdj9Ec6hN7aISjTeMXABW4_cKFc2_DEMniqLf_byKfeDMpjYrC9pvqYdIEBXSC9AJxnHBwV4U5CMOrVpUhEPXT0QEF9yQw6Tvzv6Ve4IG0mHKyk_L0zQ31smfVWWxQS5tIPDML_dIC5RhDQEcamU-9esLeGx_UIaZBqVMQ3z68mAQNxRc77ZJUhHKeBYCCp60inRCN1Ywgw6i7RI-S4vgr9ySou3SEv_qgcFdAhTmdhkAnBLri7xkMv8yHsgP2u0XJn0zetgNhU5Svs2qjorrmJesQWei1RmZzZTaR2FixpUDqMBPBiVb4MP42TNm4_zgE15VRYHzhHVCIwQAATkYxZV9J6W151_4PEmVZCZM3K9xkdwUZGFY-pokg0igYLL329BvijIXWII7YKY2G8kWjxwpIT21CF4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=RVSlvgsMTocBKKEgfEgVNMjcvR2p-Q9uU5WurbBcvR9WG63YqVqOLEk-JoNa0tTZ4FBB7Z_Gj7hG1JyBrqyIwQ859ifrcr7ux64pwjS5a7NadapnooJ_ljz9AdACFqdLoYXiadFYIBmHop6olpRpw8v68wNVzYpHN6HhlTE4UocdhOOSdKGYAQ9StkABnQZM8itiLEfz2uPl8CKkbnuCRf8NwsVh7wjUyta9TgabV6RpMiYkX5iyKeoz3-DP9byQn8vr3gwI-4tVdj9Ec6hN7aISjTeMXABW4_cKFc2_DEMniqLf_byKfeDMpjYrC9pvqYdIEBXSC9AJxnHBwV4U5CMOrVpUhEPXT0QEF9yQw6Tvzv6Ve4IG0mHKyk_L0zQ31smfVWWxQS5tIPDML_dIC5RhDQEcamU-9esLeGx_UIaZBqVMQ3z68mAQNxRc77ZJUhHKeBYCCp60inRCN1Ywgw6i7RI-S4vgr9ySou3SEv_qgcFdAhTmdhkAnBLri7xkMv8yHsgP2u0XJn0zetgNhU5Svs2qjorrmJesQWei1RmZzZTaR2FixpUDqMBPBiVb4MP42TNm4_zgE15VRYHzhHVCIwQAATkYxZV9J6W151_4PEmVZCZM3K9xkdwUZGFY-pokg0igYLL329BvijIXWII7YKY2G8kWjxwpIT21CF4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=Qi9WC6wmyEQ9eSKseXuj_ObrkjWsuxUxbcYW8B2TTlkNMeYVsKCjxLEq8t71CfklSjgmldF6pw1TVbJIbmn3hacO0-9ncI7R0IxfSUa1efAfwtlMbWAxT5eOgu5Pwj0b01Gf2W6U6Di_z99QRIqky2wslYmnF1kW4gz4TRk4r7qF3o12a18hzUM4JjuldPLdDZK_CQR0sYi_ZZ5SCpm7mNOj6N9N-dHJn1Q4e6ImuQZJOVVToqFqjfpuf4RH_VcoMhrsQMRDhkRrOYCXZod5xJR_mmKrymTmb5kfxfSsAm0bVIml4rv2EwCj6FcW3rPYMPpvr477OfmRp1Eo13Y_LSnvEowHQQfRJ51rTlRV-_1VLPkhW5ll7Ua7I1dYlqI4LDxck4MmWhMHf38Q70zLbE-Ps0zZ1eXQwoDDQXlBkTf6Ykx0S4qJ3rDDw72RPzuN6xIbei4dubsizDEwVuCSRkUGv4OSM-tvb2AlCofTMbTSjfes3zILuMZ_jHCUSkJVmVdNmgV7PzwE1M-S9Gh5pbDPUUuIRMkLLPmnecYqZxa_lly7S9u4IiwE3muZo5Tc9pyR-i3fdURW67zACJnkFhzMlaxMktktRKkebZrPzOcfMiadto4UruP8hUG2B6RHtxRDTLAY0BdWzVTfTz0BG50MOm0pr3s7a0avdX5c0Vk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=Qi9WC6wmyEQ9eSKseXuj_ObrkjWsuxUxbcYW8B2TTlkNMeYVsKCjxLEq8t71CfklSjgmldF6pw1TVbJIbmn3hacO0-9ncI7R0IxfSUa1efAfwtlMbWAxT5eOgu5Pwj0b01Gf2W6U6Di_z99QRIqky2wslYmnF1kW4gz4TRk4r7qF3o12a18hzUM4JjuldPLdDZK_CQR0sYi_ZZ5SCpm7mNOj6N9N-dHJn1Q4e6ImuQZJOVVToqFqjfpuf4RH_VcoMhrsQMRDhkRrOYCXZod5xJR_mmKrymTmb5kfxfSsAm0bVIml4rv2EwCj6FcW3rPYMPpvr477OfmRp1Eo13Y_LSnvEowHQQfRJ51rTlRV-_1VLPkhW5ll7Ua7I1dYlqI4LDxck4MmWhMHf38Q70zLbE-Ps0zZ1eXQwoDDQXlBkTf6Ykx0S4qJ3rDDw72RPzuN6xIbei4dubsizDEwVuCSRkUGv4OSM-tvb2AlCofTMbTSjfes3zILuMZ_jHCUSkJVmVdNmgV7PzwE1M-S9Gh5pbDPUUuIRMkLLPmnecYqZxa_lly7S9u4IiwE3muZo5Tc9pyR-i3fdURW67zACJnkFhzMlaxMktktRKkebZrPzOcfMiadto4UruP8hUG2B6RHtxRDTLAY0BdWzVTfTz0BG50MOm0pr3s7a0avdX5c0Vk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=uvvs568QtPkWKWOcpUuIij08NXksRj1hbpmlZhaccWBLFM6nlfaTMJVsN07AceYj_grTc92y0jR8SxDs3BJ5UChPRuiCmnAHbSy_dylx9hQe6qxn7YUNHBJp7WExfVoKs0Swdl8pwlh0-sgpli2lWfPAqV1m1_sBbbIK57QBuVN3DsE37CYLy8T2DHENuEsJHkvrDkaFQftGrOOmvsuuj4BI1AM9kYpfPb4tYuclp_cwC3WitYUT1kIOPRakKBYxBvic6GvByhuolRPiwPxKi1ZfNsOzd2h-fjM1Gf9XUqbdauzIX5HdQN4A7YjhaZaMPvnJQxkcavEMl2hyQjccmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=uvvs568QtPkWKWOcpUuIij08NXksRj1hbpmlZhaccWBLFM6nlfaTMJVsN07AceYj_grTc92y0jR8SxDs3BJ5UChPRuiCmnAHbSy_dylx9hQe6qxn7YUNHBJp7WExfVoKs0Swdl8pwlh0-sgpli2lWfPAqV1m1_sBbbIK57QBuVN3DsE37CYLy8T2DHENuEsJHkvrDkaFQftGrOOmvsuuj4BI1AM9kYpfPb4tYuclp_cwC3WitYUT1kIOPRakKBYxBvic6GvByhuolRPiwPxKi1ZfNsOzd2h-fjM1Gf9XUqbdauzIX5HdQN4A7YjhaZaMPvnJQxkcavEMl2hyQjccmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTF3R5zQTkP99Sp9BXl4jNlBES3C_yqYJBm_qNrv2pIP3sOJMmJa8LUriT9BaiT5BaYR1c4LIwLBq71_IHX4B3k0JJid-itdhPlzvjLWyZ1-5ueWXsFlV7KGrYECnB4ohWnmXYGH6qfrrUxytCd0QKgMSKBroBGNp3Q2ZKyMMwJeqxXroELNtegpjASFMwKIoidw9luPQCh6sp8V4K0McCi3yhibblpDZ9DVBkX_E7aUJ3DMH8UcChoPGUZ0vv-FL7-Ly06Go--jXydk4BB5AxuPQ8F4SNkPdWUFE3NwYDlJ4z-ivAmgyTSEkRUrZ2_SA9ZiQuVTNPJ4s7ExEzm5uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=OWfk56R64j6A579cPnjLQSYthMvgfGwvAkQ6F07VLt26w2S26VWs5vsrg1w_5BngHQJvV7UqKghWWeKeCKg035aR0pL4xyuxzqGnRJRBJWJvZUhFyMVGJLNAWpCsY3umjBCQXpwFOskVzmLog_sYoR_rKGaseU2dpqwzAJrD-Gdm4fNoGE-ioBXnca19ao8ctVMtZteGMUSmSG2ZODLzbUAO7vRYqYIidGjxmUWtgcr3wp8UAsnBEaCyxYmif-VjZh9HWCB20kaCOS6gzXywheBHe4fMT-zhCqBFi9mNxr0Gtkoul2gBdI_BgykTp369ISeDowI_qtdLx2_qQ5c1pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=OWfk56R64j6A579cPnjLQSYthMvgfGwvAkQ6F07VLt26w2S26VWs5vsrg1w_5BngHQJvV7UqKghWWeKeCKg035aR0pL4xyuxzqGnRJRBJWJvZUhFyMVGJLNAWpCsY3umjBCQXpwFOskVzmLog_sYoR_rKGaseU2dpqwzAJrD-Gdm4fNoGE-ioBXnca19ao8ctVMtZteGMUSmSG2ZODLzbUAO7vRYqYIidGjxmUWtgcr3wp8UAsnBEaCyxYmif-VjZh9HWCB20kaCOS6gzXywheBHe4fMT-zhCqBFi9mNxr0Gtkoul2gBdI_BgykTp369ISeDowI_qtdLx2_qQ5c1pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=FKiGol33oCTQ3ePr8P39KydWAc6f5gWii2UzdBwVoIRom1wHM5AJTGg9Tjzi5aszJCd8_ZAnUMrymTMGBFU8jUOt8_fVQ8uHOMNCXxuJoPylpXaGDbpSLK1TcpC3IOGX8LCwMCJQQrRyRIR8r7lRhICApdnl9gsbHTpq5D06jy1WkWAwpPSceOpuiFkKKPGm8swmuNBE8l56gzwkpZTFttdh-KWvR4rJW3zKOVv6pxrE1bJzfuRjuCumEDt1br8Af8vmh4PiGbHOEVUXHE6TNfcsHb3jXvDVdNNUU2opdhzOkc4SLh9eUckRwVLOPB7IPG1btTJqEeYs32_cbuu2Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=FKiGol33oCTQ3ePr8P39KydWAc6f5gWii2UzdBwVoIRom1wHM5AJTGg9Tjzi5aszJCd8_ZAnUMrymTMGBFU8jUOt8_fVQ8uHOMNCXxuJoPylpXaGDbpSLK1TcpC3IOGX8LCwMCJQQrRyRIR8r7lRhICApdnl9gsbHTpq5D06jy1WkWAwpPSceOpuiFkKKPGm8swmuNBE8l56gzwkpZTFttdh-KWvR4rJW3zKOVv6pxrE1bJzfuRjuCumEDt1br8Af8vmh4PiGbHOEVUXHE6TNfcsHb3jXvDVdNNUU2opdhzOkc4SLh9eUckRwVLOPB7IPG1btTJqEeYs32_cbuu2Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jjsx7ErA9P4qWx_NI2RwS-aa-aTWkxCigOfHwYR9piu5-EocS2WBrgctNTLC7zhT65PuDWl9HZliYw3Yai4GeurXAcxx1ecEuAPaMjix3eUTLoQnDSJZA__xXFbr4dNh7RkaZXQceh99vjYdtJL604LP2kisAV0PVDbLqHc4PXf6Ky0a6tK3u5_X67sMBN35Y5F29Gc4sNKPASUeG0gPLi4N4TpW8QzPphNtbpcuygZ5qBnQPvY6TM8RGG-H6_gNnRfxE7KFJhf7x5N3AUM2qqlAx_Urh5I-7mnObR9dBxMBBtHpsDhqil9Qmyuxf1b-wVpLu3enMebfNhA99Jug7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SX2mFQ5xIYGTP_83fhwXTaMsO7mm7uDPYFmTertbqlSGG6aLrBkoKEsqooL2xnbU-_fMN3okU1_6xGL4-32Zjdyvpx_KIq5A76B49u49a2pXLu_ZuVyVFACovAmy6Tmvdf_b6QEvYQDSCazCrNTdBkIFAQwMporRdMs5ZMGy3_bBrm68pgwubj_QME_V62e7nKoIZchMDirk5qL8mf_NWbf1H_GDseD2pmvlA4uSLX8wxynm-h1W-6WALQa1E6-mmXEkj4-Soihdf8RwSiie-GWmJp-Wpns3bTRF6HYWALvfnXCLbfy3_IbqQqfQwnSlsuB_7GVFsFAP88ksqn2v5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbaRWFc8sLeAuO4JjzSrzSWdjD1XNY5uURpYUUw2aBM_xTNMgUYPHeW65KcsdAuLi3UTu6IYJ_y-1YVxqYsG8yuT1NQrZczNcihBDgX7TzHmc0170naIViRxRl2ri3ikQlQy778neGWkUdSKFh2HHOoyd9WUfJxK5IvIh7yUMMv_7zWJv4hBvthhX486RPAUZPqjcB--Y_rpkS9QP10BlhAJqZLXodpNI1RJabirHRXZpBIpFjjrR2hXaVu6PIS-iA2VIAQopkxBT2FSAuVTrRnFC2kQIAdD7TeM3GVBHADcJS3pAzhYz5F4pZhIykXZEohlTDL2EVlOj_bA_Odr4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVFohCK3ci7H8Y5QnQf-nrBxgoujUgBvuqXVchXxZ1CWD_glx3thqnVTQdUrpj2JjqQzRVJkT5EVXH2pPapKQ5rewXi1V-oF1_DmFwz6qYgwk7SoNl9JvRlmrKOgmQbsVBBECMnXiHxlCYarD8Cfxi9K_5VOZMFE5itxmHHO9233q1ELrGClw72y_JtPU60Hf_DooN0DfF5nB-WAj_HHnVaQ1iFVCHm9e82x459EbGRXS43vvdenZxatYDI1GgfPNMn-ohkGy3wrQaWQ2aOZbYzQ6kx8ANbD2Tsrxx-WM-YNMHUgM6LFFMh7D40VefTSo7uXghuM-gYXqrnlSlws4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8L4XiyL8s9z33d0j3PpBoSlJ4KJSZH4gy9CmGFKxb42i3-OLbTy336sdt-EOeuCZOoQu9ApotjDyS20fZM3BENZqwhlpYpcj4igRyTW4c4rdOqvlcRR_K0N3ZiZ4O5yp2XRVkcBtlH6tP5HxF9I1A98vLL3EQjm4HCV-MZgdLXXOFtHum1_je56oPs4cTJX_5oinxF_GncsSLtvWkHq1XTmFZ2eXF7xcMCsaRBLiOh5n3ocH0csGXHHHQP8_mQjVtpPmH29xQrRtAJlhQQCBkWNpVnsYu07Ewv9LFaEOMwfiZQtTnMib30B0cc7nxNdf7SqB4qy9OXWWDPXgTkwng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYahaMcSxRhmDPpdACyqSAqVMBRoBl4r8kw_oyhFGqT54vWwSr_zTm60PoWggvr7CJujHX0YDvW943gU0CXkGyw2QjS2Vq3WqXSFKieQ7C3bS2ip7q1Ry96B5kKXj5b-Shu3BwCwj4GKURC22b55n5teBiSwAX_4XatINvOTLe2OxrjnUmcYcq3PPwmjhxK_QmzXF3-jmqthqrqK4cSSHNrIMfOslULTrQLwtnZ0v4DH-UNvFCH_vm-8uL4q0Px9igiycuqRmhmKtbQxRT7-_E6WgwF8fO1F-svX4QA88hlVzNU5Fc5l6Kleng9smUMLVYn2hhM978zgGZHwFDtq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFCncvsnlIFY_ZZWxjSvKcCXCaQD1Cs9TZnW_DyKNKxVHq3gT58Vkt5jaLTNyEsB0QuZep9BqlGCnrbBk_z5UlNE6xvaneCukVsuZFG_yl-IVrb4dOgiSbXWgAfsMWum9ouQfoi9ySffQCOpT9CMj11Qv7zfynHOUU50exB3cCOXsNkQSuXDgbtOnfFw_gXY3WsISNs0gl9FkS-KfJoJrQzIr2XQi7jo7nte4jQN0r9qmv8aolBWBPhZNOQ9R-kYsnLWo18OSr4T_VVnj-jpx6KShIEyVtCGYKF8VLO0AWAbgCvWtgIQ6HPgsRr6qwnz7yEHNBy3oedAe7esN9aqfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/npebOxhcWMJdm2oT9kTj0YbN3ZdD39QQVoF7DYDkPCFeI5gK-6CAyAInjeU_kWbZXHymylQbyJbW_AncqPze-9Pa2zudnJewSIGxmrnuKZf7ASoSYXefA-FztvjHrHVfAIhrelQUSHyWhhC_bBBsjf4Sv8DIVBUjvMyoQ_0zy99YdnbjqgKOfhs4Q_WqwHqqukV7xcMT5uWBDXIDVTMz7Vso-4VY3APT0tTGMLWA6jI3JhGs0v28QEAfClKLL6qklD5Iyx7U6ZcoSvUUavcQzzNexO5uUa7mfdIgOJPMyDJmP2i0SF4xRMdaGZuuIi_eoS7gJ_mbVvMNH_KVF7332A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dwH076-AYyvX6YJ8cDFUHfk23Op5FPxuHpave_csuzENad_cRMw3ea3N3VVygGF6j-RTGzss_3AQiflYaL4h5_cB5i_5ZcyxlohvdQasO_utchzw5mTElZB4i8_vVSZCr0lbEZIdEDonMBw-ZnEIvOo5Ae909qA93666D6GVJ4nkVlEjhGkfyiDdBtSfA_bmg65M8sSW-zX2qNngHC3PBZ-SEXuU0z03jHl_AtYlQ2Io3_r0tHvaNva6epYs5ukfiuSQIv1c3_35DVJQCoUnEbboas9g9mwFoEsPjgBucI-6pSoJeKTQF6zCww7LLzZ_JNyw_sWViXq0qICgC_MUiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTf93Adi-MiL5RQK68mBjts9xcxijRY4twUzxSCxZbCMZZVXcNYmRDe0A_A17qnMLjd2qdnFRaY1cJ-KkaUOjV53QKL-V_ckSHFeWK9SACRQ7N3c9ujUX-oEc0dnC8gj0fez5Vat5c4nGK89LNmJtq76a5tNEZcSGJaS-Vx-S7aXpmlKk9-Gn22ZfA6L9Iyj-P5kaZJOQ67LFJQa7ItiXxZvJnHBNHA8-7MRTYLVy2qb6vMUrZ3svX09Gz-SHHZFrWKtN8-YRGQFajzDJCDo6YiogVlfy1iF2nMsOggE6VYyssPeaouWI9Ho-EWlGu5uduSUqT8_H4IFvkiV4pqirA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=ALreyFGZf_hNxQUdHafqGuNg6OPSJkCIFly2Vjtvq5m5xhzlAhxuGriL504wM-PiG2tC57Lcvdf3WOsGE6pl4zXhmtZy5Ki15in6yYhFuZEmCC8jXB8R-8elK3LpAZ7OdQ2NDRCv2qSgU3Pt7gKh1vicpAntcp1Lk7gnU7THyNio1soBdwoh60z5AgeDUGwiO598kyxf_dmI-5WHHG4ploqrPIS1j1o4IpcVJChheM1KOG88o48YfwNUdxhlku5YVR-gm7zGq0l_zOG1gCU3JOxIqmo8MftxKcP5rUjmf7Dosg-IjRqiT56w4zbUmR_HuvaCDJ3Q92ph5pRy6dqVcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=ALreyFGZf_hNxQUdHafqGuNg6OPSJkCIFly2Vjtvq5m5xhzlAhxuGriL504wM-PiG2tC57Lcvdf3WOsGE6pl4zXhmtZy5Ki15in6yYhFuZEmCC8jXB8R-8elK3LpAZ7OdQ2NDRCv2qSgU3Pt7gKh1vicpAntcp1Lk7gnU7THyNio1soBdwoh60z5AgeDUGwiO598kyxf_dmI-5WHHG4ploqrPIS1j1o4IpcVJChheM1KOG88o48YfwNUdxhlku5YVR-gm7zGq0l_zOG1gCU3JOxIqmo8MftxKcP5rUjmf7Dosg-IjRqiT56w4zbUmR_HuvaCDJ3Q92ph5pRy6dqVcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AR2D42YACD1KXbtTaoNFV9j4v94XAAgXnG1ybs51KfYOotYKSFh1zOyLaGIKp80cVPtJAj6XjJtLyNK5rip9vCFjaiuTPhWbhpzR3ggYgkA4BimUslWn5QCgKOQfVar2KG-w_01kEqkk9XZZQOS-1eayAVEjG0QI5BVgfi7xEcAqfO2xNVr_qgqdeb9PbraBarp8XqW8-A8JmFE9qZk16BryitYN93ip24GgJ_cLzpKEBA7hriEgY_vUayNKun7gYSFYygr17bRXJkXdwfw5yq1OdYY2C0uUR-ixrmvNaDtAwPGDzK-26vsg9Ia4Khozq9MV0DkjkgeTBGo6NQy_9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILwodMbR0n_-CSU61stV27dABcL8mMz7n5p4YonGGNfhVMJthCgCAKuej_lc9yodl2ZKEKYWgleEM27DTiKNOHoR1KIsgQOK1xkog4Ne3Lm8YhkJ4V0__Q43HQIyC9AE_DR7wvokVJYL2kIvVsZvM_N2DXwGAN-GpGchNQOpzDUG34lyJAdi4H2t-uCL-zsICuxYoM5QIykVJ6UTJx2DDY_pJiViyPwA1YBkmVSrxNGotKzvBnq2kxtk5Nxb6N6OnrkQNRN1ibUlJGPVtQ0lPY06wB6_HN6DmmUnfwRgteVCa17FIs9fDJ5VQVJcWWQkSjuvPJDRTYPswZgZCRqdHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=plN3jQNK8zoilNEYhdu976Tz_WyheVbSsXUdVga1uiUpCWt4FmcTbYi-6NBW0zGEhMCuzBUEtjkui-eS_1kxRBTW3AUtiD3YMyft3luFdKGjsRVJUkPlTER_a8MnEU1nxNfFMi5k_dW7OqpdHtDdlpIfPDWplQRITp1UlAWpDHRLC-LHQyc1USGB-y7FYNQmhhEI_4XAAnTuZEcys5crd8et9Fz8uZIi7QmeAkBBrVCINFzu_fRNjOaIHeyryxMLiFntGAmS06OiMmeBGH9Di75sSVPA6xWCkyhUicX1zgXK41TL2MwwWPW8pxn7Ke9Ejm0uP48cv2jPpnGEKgA5bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=plN3jQNK8zoilNEYhdu976Tz_WyheVbSsXUdVga1uiUpCWt4FmcTbYi-6NBW0zGEhMCuzBUEtjkui-eS_1kxRBTW3AUtiD3YMyft3luFdKGjsRVJUkPlTER_a8MnEU1nxNfFMi5k_dW7OqpdHtDdlpIfPDWplQRITp1UlAWpDHRLC-LHQyc1USGB-y7FYNQmhhEI_4XAAnTuZEcys5crd8et9Fz8uZIi7QmeAkBBrVCINFzu_fRNjOaIHeyryxMLiFntGAmS06OiMmeBGH9Di75sSVPA6xWCkyhUicX1zgXK41TL2MwwWPW8pxn7Ke9Ejm0uP48cv2jPpnGEKgA5bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=Al3HWXyGK-BxBdNjBRz-3n56wdt0T78qPzhzDsXhLAjWW8SyKeM34iPzdqLWJWi72VXJcGHyyMzvaHzv4eQ5_SiLhJhzjNv79JYbh7go__qiJGyAbwEFMoQ4TKzwPS2HuJGukmtSUDmjxRCm7KMdhWLjInN7Ns2FcxB8meOPtBl2tfk6kTiPtbf-xoHERgbTaUADTfMy2i6RVoS3kt-Qj_uIsMO-O2i0_EwOkgQTKQMn9PMzKEeeYQbkHNZurP7FUGXM8XsHKtSsu00FuwEFZoSo76v5AMa9xVYLwYNzah8a5Y9OS9PH0VxIyY08kO6ZlqQlAVgKlPVAwJJqvXdVWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=Al3HWXyGK-BxBdNjBRz-3n56wdt0T78qPzhzDsXhLAjWW8SyKeM34iPzdqLWJWi72VXJcGHyyMzvaHzv4eQ5_SiLhJhzjNv79JYbh7go__qiJGyAbwEFMoQ4TKzwPS2HuJGukmtSUDmjxRCm7KMdhWLjInN7Ns2FcxB8meOPtBl2tfk6kTiPtbf-xoHERgbTaUADTfMy2i6RVoS3kt-Qj_uIsMO-O2i0_EwOkgQTKQMn9PMzKEeeYQbkHNZurP7FUGXM8XsHKtSsu00FuwEFZoSo76v5AMa9xVYLwYNzah8a5Y9OS9PH0VxIyY08kO6ZlqQlAVgKlPVAwJJqvXdVWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCCFDAEkYGMi2uXnCTJxpu7Uzs_wZl0h3YiVQrck57NymzjraYTz1qBhydjwha9rAy8sXtDTFUJFZo5cf1okw5RdLoOeTJ4nCh4psg3nR4UCRErRiIH2zDW4wAg5uVSw9XstoPx_QqdS1Xst6vlIeQGHxng5lmy2cGVU2LKfQc5rNueZcIgPsrnB0lmlDbs2lPN4sNNUs0Q2AEnuplA1K1b00ZoZgC8M3lP9jDFSlfqusoLpllkJPjotL6ouYqzmSrmTr7BTDInkfRyPmSZQpQdmksoxQCchuLCgtHV54_sXR7T4sKNnNrmRP7eiapOqnfphQSU_uVvwXAhxzix0zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbmZgR4PYMdugebZJMx6lN3fBqNi_ydlmA6GvLYr_y1SdcRMmcLVqj8UnkyOiZx1xK-ujU458xAiwtBO3ibs6m3sYhcHDusiC5tkwy5Eg28ryPjvmxxAYSIN1wGjjDRGil6SJhOKTrgVB-ctK9QAxgk1falojao6_saAW_VEj5Co-XvvenOX-kzeauJvzxsWPZAkbz7uRCn0f7m5QBBe2-fIzfQ1cO7nE284GLtRcduNv05SRkyzCHwZ9V1-mi0VQDmX4whrmc_gSU_wL0PP_eImXM3Dpp33BJesCvwO9LnIyChEXHVJIMz5tOuI19vv3w9bny0-mRsbseSbFew1lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSMj5M9e0XxTeregT9as-ABNTda7cvGQh5xhcDbgTU6uJP9q-HpZrEwGfAB91GhKJdJTiL7th7YjIEfUYidHFXe4Obw_ShQ4Nwr-Fx2_21YgBFbIW4yqRfWPZiq4Wu5HcltrmolcxwwnFZ5RYB2YYaLa2ydWOwt6RkG2ykV2Vj_BGxHc-pJT4f0QIdD9__MySOP9MqAmzhg6GELppcp0PK8UB24HHUPKIJl6kWlIPt145rgtblDMvpOBTRgxmNov0IwgZ2lSU2xRlfMu6r7f6eYizbwfxets1EKrr3tgtoFSgSpWOBQwei3UBuy4Ef5Gz-y7Pl3D3FOOhZ0BFc3MUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDxz18HCpJOnsZ5S23aXiW95ILYAW_p1DiCzL-Vs3C1wAnPqv8DysEMPiYxWegCGpY3t3A4vDjwkQeMmoWemNhtb1tB4YiFXVrEwVLZ1DUEEDODIwQp3KkSggzmOSLIh2HPkATDeCVv5bMY4ZBLAIVBWc9lEPUWfOavuM-paBbWgMZgAEClDx6IvhocM0aj2SsVV6tyd5ab9qgKcqEi5zYeSaV0w4yESnn1epeDoC3V_RcbEIPCP4YbnK0dXfrek6zcwG1-a09RWUdRb52NdB0WOSBcfw-AsLM-mQSm49EI7496fYYtT1BZurtdZy9MsbUsygr3TrE8gWO1_NjF1CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGDqKhvnyLViTEATpffhhbBnz6CvYg0iteOPIHHxEgf4ykVXBrq_uHo8gwrc73CcYRLSB2dDh2HFZB_WdHnMMdr6VMeUmgjE6r_EaNb3NhhYHWGnD9_b820ypYSURoacYtxHypdUHPBPDEeyTGXuMKm8LWjnS4goS9sAu3QgsrYktEBWrCHUjDCCr1rChyPORjpQgSXxs_iH_I8dzfu1UkeYC9K8XIDofGN7MSmTbGlj37hgymVM4N35GXR8uM4XqpBV0mkuKal2zwetXzX_mXMnC-NlwmXUJ4gVEn75xGI_pP7CAtdRzVF6eDAAOZP-SqQEseeesoYRd6lOo2jU2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lALpMo6YMnIuX5FKkjnc5JTmESitCr0LWxld1O7lEaKBfKuZhXJYzH84jmSn673yk2eUO1UGhKvJY_FDnECUv1b9io5f03VPZJhOQqB-b60t82PXvapmZ9qNXF3y6Mk1FgAKDKDUxPM9iYL9jSu0UWX-zFhfNLKQcon3COngFoqdM4Doj6n2KaJi289_GJAraURraE1BWW0U1QTDBSBnBS8V_P6wb-xlt_kp957E2le8Kq2gvaXP3Nw-bzZaE2YHJU2sLw6Dcchd6gswrjoa1YpSkYbGJqmrVKNSUcbapGyeiHL0MaSr8vprVatMwbwx33rGtjDI6nxaQ2_cXbbgpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEj75jFvHMIPc4GeqA32OphKVT7UGTvRjUnHVc_jxkileXB_rlm_KLmoUxnqPxyZ8_g9girKN9ixP6fPQ8H_Ou_laVL8nTPb0L66zXsjIE3zvdApYFWM0IEYZV1zqW1vyy5W9LbnUxvQgt0gWT9Nhb4pwK1GEU-_GTXf2BXohnYHmaUy5C_kXYn5tM7Yi29qikUS3Y5H8-izxYVXUmkr0jJTDKpNKRHqwYrfwGKbH2iK4SmVhJL6FtNtX15PTKsJq8ilbkENWybIyB0zc0prkBMdqdQpqECve3j2rMHLIyYyJL-DmutcP0pQEzYrSSIFTH8szBsHpUv_OU2YLOGSwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWFdSllK721o5NOLSOhTcf--wastqXA3284MKIdqPFaLHoEhtDuutzF9leKOL-shHdaW2eVX-O0SidRBKYVS-xMin9NIwGOA5Yel_phU4ElP_3kTEbnWSkU_7QaUCjk-CnpOyZkiab15FgQ3ux_gv7IncD5NGC01f0qAqHBVwZ8Rjok5lCqpvNhBz6FfREJs9hquww-udBC_zCyZE8IczK_ZooVx96zz80zKKoZLyNO8K10WEK3y8q1Z6c_EtXPqgH0-4CIfkeU3laS_OG7MYMVhDQ5VMvE1UdgPjgW39LPl_K8jYW07nb6D3niebuvkPtWE5TOqdVsf5c_ZF9uDuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=icNKHZptmMCXLT-rBHm0UcPrC6dhFm-RA441jIn3kJqpE7j3lznPmbZtKZcgOq88oyCr-mTZUEA-sieXGmvQMDWeJN_6jt--DWDZuKMAe4MU4ZrdS7JT4cIj4Y2wXapGXvXbl_z_lO88zls0UUjVoXY1CIKMis8e3F3atuo_i_aB9K5fTcvkIr84LypJ_nWVxoLEBG-39nzKWjblqRqxfUTyryzYjVX5E_NyUdxAC41ozEw5o96kdI0q07GDoz7bOsjKthpTRsso0ObhvUt2iykWt2w4ub-8RASgFrPaKMUId7O_daptbAC_SAU-eFipJLwfztIn6_YOjlpdeKOitg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=icNKHZptmMCXLT-rBHm0UcPrC6dhFm-RA441jIn3kJqpE7j3lznPmbZtKZcgOq88oyCr-mTZUEA-sieXGmvQMDWeJN_6jt--DWDZuKMAe4MU4ZrdS7JT4cIj4Y2wXapGXvXbl_z_lO88zls0UUjVoXY1CIKMis8e3F3atuo_i_aB9K5fTcvkIr84LypJ_nWVxoLEBG-39nzKWjblqRqxfUTyryzYjVX5E_NyUdxAC41ozEw5o96kdI0q07GDoz7bOsjKthpTRsso0ObhvUt2iykWt2w4ub-8RASgFrPaKMUId7O_daptbAC_SAU-eFipJLwfztIn6_YOjlpdeKOitg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZdOOXe5pleg27yV9Zjg3UHUFNGDQj9Y9A9hurOANF4P477D_sUHHGQ7yWeiRtaCnOt0OuTH98-s3jCWvjOfoZKRBWJArhik9nC2_INL3vEuOp3MoXOMr74xM0fvO6fKJ0nC1GJKm84_4JWVX18Gvzz4PklirGO578vr3o5K6EPfPxmiBDhsvboseeV2iX2uBjE13fLiamnBQyocP0Al8i2Je4-AIr5IrbwpYsHTGMh9Uj1TUIgrFkJIY8civmR0nkZGYGCf9_091p9Efhb8Crj9XcKREAsXb5-EKx0umhWy4roakIMJW9vdpwwvIPhJdNTa-amvZXRMBQU5gqEWUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=R0yJ8iCl7VCmKAxbPPig2XlVhUjesKPosgMk3tGHBL0XfzxalnvWXqnpMbHwW6cS8vO6SuhSmWX8EBkArfPDfT66t950jbA89niTf6iE4889zr-Rhp2HPDcRX5uJnT3zq14vogeLykL2oBy78YHyUg_3TNUCo0Q-ZFtzoxgL8ZoHW7r_ck4L30_BpiQGV03bi5o0L3VWTjQHiKa_NvEK6-tJ5CVp8bSSTVXH6qW6uy4IwwAkX7xSAFyKHei34pCIccMma-deqe8EzlHvOQC7aGzO7sPV-2SMSXbm8t05zWeU6RfEa5wv0bRWGPBUu27NMGdejCtAKZWmCzHByP97RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=R0yJ8iCl7VCmKAxbPPig2XlVhUjesKPosgMk3tGHBL0XfzxalnvWXqnpMbHwW6cS8vO6SuhSmWX8EBkArfPDfT66t950jbA89niTf6iE4889zr-Rhp2HPDcRX5uJnT3zq14vogeLykL2oBy78YHyUg_3TNUCo0Q-ZFtzoxgL8ZoHW7r_ck4L30_BpiQGV03bi5o0L3VWTjQHiKa_NvEK6-tJ5CVp8bSSTVXH6qW6uy4IwwAkX7xSAFyKHei34pCIccMma-deqe8EzlHvOQC7aGzO7sPV-2SMSXbm8t05zWeU6RfEa5wv0bRWGPBUu27NMGdejCtAKZWmCzHByP97RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=dqtJsSl6C45mILJVwTBWhbrrY36ZvvomIpK5q2McLGWlOyhAClCg7zJY7RdA0vkoHQhH_kvdMsqkBlOutW7rGcpUAMaxrv04caE30nb20cBzGCK_9_Re1YC_PU0efEnWBockE7iq-KUco1SwE05B-d8mj2fXf_ZYDpD_-Z4mI5ToVDDMRX4QrYQRMGsuf8JEjCV0N-wcYfPmV-NGFINtzxUgjoIdZ2bloCn0CZ1FN0KWlZB3BOKkt61KYSOLOVS0u7kYFWxqmrfVBilByeMxuoJg2C9RMNTwOLyA2XSHPK_z3MPtdWGO8TwNCeLOW3UcaadkyhFMFisjt62NzD8yLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=dqtJsSl6C45mILJVwTBWhbrrY36ZvvomIpK5q2McLGWlOyhAClCg7zJY7RdA0vkoHQhH_kvdMsqkBlOutW7rGcpUAMaxrv04caE30nb20cBzGCK_9_Re1YC_PU0efEnWBockE7iq-KUco1SwE05B-d8mj2fXf_ZYDpD_-Z4mI5ToVDDMRX4QrYQRMGsuf8JEjCV0N-wcYfPmV-NGFINtzxUgjoIdZ2bloCn0CZ1FN0KWlZB3BOKkt61KYSOLOVS0u7kYFWxqmrfVBilByeMxuoJg2C9RMNTwOLyA2XSHPK_z3MPtdWGO8TwNCeLOW3UcaadkyhFMFisjt62NzD8yLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMQ6VpwgyC-k4HVe1LvZSg8JtZpWUAhLeFgTCnTlajDeig4xQMMGjabq6rsdB49JFu_eS86IkTCAzv6epJQP5djV1H096rOHWYF039k5d9c3ZdBhlR01MH8hR3fLs1UbYm8E_ZsHA02X9t4vazGYxfgOEC92wOS5oaLoEKMz0YxNihAlrxrZRzaF-ClWmJwqZIXrECBw2im3bTI6lCP1cnnniolLXjB1aECy4ilGAvrV7zmm1vBBrmystASVSdbSK43IIQDWLcVjCxUoHMcMwyzZbkOsQDXfDB7pT55jORMTguzW5pynr9AM80TvXmsIgQtyf9TqinDF6I33asbB7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJsHo7ii23ao9z5JxJxoR3rMHl4yxUSvfajnmwsew-pJB6hmZRqG0Xf9lV2sJJnq3KGI3xn1K5SqtAFgCABsiT8jbJa_ZFuWzHlMgWpqZv8_V0nKZcrJLqopiNP_8ogcIvf95msLMxtnptbFsfiVfN2O-qQVRlzpzyKVRznVxiLHd7Fi9WFc0jr0J1mz0mN_BAqXJVVqz5W68BTxMBFopK4hkTDxQBCzLLta1l7SCEvRrsqR9nhuPhVlynjLB844I75CuTBhLQ3ytPDPDDBn_YxJ9c5J0t8Vxu2wCX_hBWe7E-6ejjXSx3n0Fo7f-Dfx8VfsJ_r3Qb2mSFqPts7y9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با افتخار می‌گفت ما مشت
و سنگ فلسطینی‌ها رو به موشک تبدیل کردیم!
همون موشک‌ها و ۷ اکتبر،
قدس رو که آزاد نکرد هیچ!
غزه رو که نابود کرد هیچ!
مخفیگاه حسن نصرالا رو که تبدیل به یک چاه
با عمق ۱۰۰ متری کرد هیچ!
بیت رهبری رو که شخم زد هیچ!
رهبر فعلی ج‌ا رو که از ترس جان
به غیبت کبری فرستاد هیچ!
حالا بادبادک هم نمی‌تونن دستشون بگیرن!
اینها همه پیروزی‌‌ان!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
اسکات بسنت، وزیر خزانه‌داری آمریکا :
‏
🔺
امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است.
کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
‏
🔺
خطاب به رهبران جهان می‌گویم؛ امروز زمان انتخاب است، یا آمریکا و یا جمهوری اسلامی.
‏
🔺
هر کشوری که با ایران تجارت کند، خود نیز منزوی خواهد شد. هر کسی که تصمیم بگیرد با ما همکاری کند، سود خواهد برد.
‏
🔺
به عنوان مثال تمام شعب بانک «ملی» باید تعطیل شوند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=vW-N5PGm268DuZAszdkwuAQSRtPXLMoDnYaRSjL9by3tjE4wjF3y0jr16eoSivbQNkwaMst8RFQ-xc2rk32iohZpwvIowpugy3xYmaSGZYWghSAqLNZMVzCwSxhT4lk0OuTUTtuzXHIQFOwU--LCoOCY6jdYont77qSuATLWlbTrBhzvO4Ng6YmuqlG_T2Pnq9OERhzlsDKYWdSxT6RBKXUdIAp_8aACIsJoQBgid0_BnRNixNGViI8japqqoKDhfb2nApSRwReR9M3_UqEm5ZmuW_s6TOb4XozJf9K3aUYZKjKAPLOMGx6kwCz_EB8NvWNB8n0v9STn2oWzmWOj9LifUnua7c2cRYdXkGTsS0dpy90K8RIkmbzJFt7Ma8VqBOzl3gY2A_jYipv1PY6F4fpNHnMs765hDE0z9ZyMndXn4RRgpBiAjmHqifJ434DJbz1AZ-CfXKmNdZAfZ3JV75u21jSAAcTXoo39zW14Xy1JxWgkG8CpjisuQ2AqDY5e4WdlRRFBHz_RV0B7TQ38V2Q48Hvdihe9kP4v_1333jDhbinNf0xvFe7IPpMjAwJtzwdxxJ0jbdLgkW3UbQ9jt4yezZ0_JZEXI8G2_DY1CAzRwKnjQbt9wJPath-lBI9io1cBfE-JaUI_8DLP8UlXmnajHOO8Uq1GNm1AsD8sGUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=vW-N5PGm268DuZAszdkwuAQSRtPXLMoDnYaRSjL9by3tjE4wjF3y0jr16eoSivbQNkwaMst8RFQ-xc2rk32iohZpwvIowpugy3xYmaSGZYWghSAqLNZMVzCwSxhT4lk0OuTUTtuzXHIQFOwU--LCoOCY6jdYont77qSuATLWlbTrBhzvO4Ng6YmuqlG_T2Pnq9OERhzlsDKYWdSxT6RBKXUdIAp_8aACIsJoQBgid0_BnRNixNGViI8japqqoKDhfb2nApSRwReR9M3_UqEm5ZmuW_s6TOb4XozJf9K3aUYZKjKAPLOMGx6kwCz_EB8NvWNB8n0v9STn2oWzmWOj9LifUnua7c2cRYdXkGTsS0dpy90K8RIkmbzJFt7Ma8VqBOzl3gY2A_jYipv1PY6F4fpNHnMs765hDE0z9ZyMndXn4RRgpBiAjmHqifJ434DJbz1AZ-CfXKmNdZAfZ3JV75u21jSAAcTXoo39zW14Xy1JxWgkG8CpjisuQ2AqDY5e4WdlRRFBHz_RV0B7TQ38V2Q48Hvdihe9kP4v_1333jDhbinNf0xvFe7IPpMjAwJtzwdxxJ0jbdLgkW3UbQ9jt4yezZ0_JZEXI8G2_DY1CAzRwKnjQbt9wJPath-lBI9io1cBfE-JaUI_8DLP8UlXmnajHOO8Uq1GNm1AsD8sGUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUht_5cCsX7OO6nRVIhjai1bMCT3OjZKo5S4TEOC8KIf3CiFbrK1eNjwWXdjzcZFRBGmEHu5hwJhBgR-C2I4ecDpx7vTF0uGrZHQ8Rpj9RhsK_H6airtB4KqQudXiSG3Wb6tfkQFcX96_G0EBf0WDmm005rW4GtYfdxjeZosSWJymSGKufId6Nmeu-Vkdla9yul4SPtMkmCeUaFsAD19q7w0eQuV5fBeQE0Ke4uW2FCsuqy6JbhX8RRbLnBDvt7Gt4aB_dEo11zeY3a_lyXShfDEP-9-LtgDvmN-qaZn__9ywpacf8YVtxsTaZV-FjD2jlrH1Jf7odWuWQiraZCl2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=FxZTkrzuDc2OWnNV3OxIyDFPBbPh5LisgQg-semzUIhltLoPBxL4JEbIfJRzCJvAudOVHWepNvmZaGyuoPLmdBJKqzVVcg2Q180yWK2zrKhfm56584eANYYrYSLgKL6qyaP4J29jDzVb8EKEg2sigmc_jX5S9UFoRYOSk6gFgAXeomQ4Squ1w9FflTEZ3kahXQ73FseucuVVvAiHeDj3ySM3vI0vUZ6OTGPqFy-aJbfg6agTkS-mTJYrCO4mQJBpxj0MxGm4hhbjCvQKITKU5LKW0fdndjA2xa4Rm81ahlkOIY3bGYkOhh7nHvJ97jUednOEFGwOploKFEikzE1iZjCsMOyECfrvIOWqE93GXB30y7r-Zb_gvWqrnXeznxBWp89792bESuZyCSEutKiR_8j8Yiy4K-z2ZfVg5GMHl633ZUIYW6WLJEOPdwAJ5W6qW_SSaIP9AVZomm0Dex5f7Db0FqsSzHIGjby8ARLAwCuG1QXV3_wOKPzvVtcO5oMoykSTrRo9RGp3nWgesI2HvjnxLmylzcMnpcgK_PVz-HBe33azSdlh8xZy4kpYpYQA2mtEn8BRCJO7WRolgU2Vp_LZbNcpuwjFzDgtiyWW2EJb3lQWnHHquKf83Vehu3uVkRyyxAOLpdxaHzdybiS6lj3HRYYyd9fRuIviRvc1pPY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=FxZTkrzuDc2OWnNV3OxIyDFPBbPh5LisgQg-semzUIhltLoPBxL4JEbIfJRzCJvAudOVHWepNvmZaGyuoPLmdBJKqzVVcg2Q180yWK2zrKhfm56584eANYYrYSLgKL6qyaP4J29jDzVb8EKEg2sigmc_jX5S9UFoRYOSk6gFgAXeomQ4Squ1w9FflTEZ3kahXQ73FseucuVVvAiHeDj3ySM3vI0vUZ6OTGPqFy-aJbfg6agTkS-mTJYrCO4mQJBpxj0MxGm4hhbjCvQKITKU5LKW0fdndjA2xa4Rm81ahlkOIY3bGYkOhh7nHvJ97jUednOEFGwOploKFEikzE1iZjCsMOyECfrvIOWqE93GXB30y7r-Zb_gvWqrnXeznxBWp89792bESuZyCSEutKiR_8j8Yiy4K-z2ZfVg5GMHl633ZUIYW6WLJEOPdwAJ5W6qW_SSaIP9AVZomm0Dex5f7Db0FqsSzHIGjby8ARLAwCuG1QXV3_wOKPzvVtcO5oMoykSTrRo9RGp3nWgesI2HvjnxLmylzcMnpcgK_PVz-HBe33azSdlh8xZy4kpYpYQA2mtEn8BRCJO7WRolgU2Vp_LZbNcpuwjFzDgtiyWW2EJb3lQWnHHquKf83Vehu3uVkRyyxAOLpdxaHzdybiS6lj3HRYYyd9fRuIviRvc1pPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLDe2E0HQySsrn6R0l_0CkIDqsYknNueHLSOdiAXUdGANw8V9tAKc6LpJj2FEycEXScOKtdTnt0sGHH-abV5ufC9aU5nygekBDw1rfKAGp2lz4i_QacwykY6hWUkkyUk8svkJg2aGnVnRwizrAsNsOZdxtRfZNh0W7XcPZA7g6zhCdnSfFtdyjLsAGQNxl4ttNShuITQ4p8SA1avC7Q3aUC8USs3SUIsH4W4OqEktZyVxK-33gPX8a523TdOfZvMlKheZA-zpff0aAi_30bprYgBtzAaHiTe43Y3971X8o20cIofXO9l2i7eH-cAN4dPADmdNYNx0zgq6hGutziEYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hz23ObDMy1dAItEYEJdZPVtxVarSwrcBv9csIQwu_EFkeAdmNDZKUGqp4x3XNoAnwrLsPWrLBYBbIwO7kKuUkBxktF7JxQabvRExDZZ0-CT_7EXzUsj-MpFHrZYeZyBpPx5WvfDTCRLvGb5N0Gdq9wxp7qasGp43XJUYQrdE6ezz8T8ADkTxgLRh-0wqgW7kJsEqbvKc7sZ3pyC4P6KSTAU301oJtrj_--7eHPUDQQ0DWNej2KY6BmPCs8XonLSyNOUf1_Bu9Sqtx2Tu0RuZG5wTyYaetPnLDDKGqz8XeORdGgvvsgepfxX19bLjiQWP6QHDnNdo85hv5zE8iGbF5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SO6oz2ypmfdT1mydHWwuW-nyfU-VNYtE1N6KC-3LpILa2Xf7tyhJg2QiLjKnQUPAiWVv-4OtrbU-f1jmcaaPq6CTKL3ZnJ23gNp53T9oqnVoNved-BjwYbD2Z6au_B55UuptBcUz8nkCPNXFvd5kudt3--TZT2HvCz86N7VqRAVN08KkojC8IkOduUpArTx6KaExFtH9Q7ss3Rpj1VKXJ_baY3S840Bv2TPwnZG__PnUtvHXqYg37Gf04ge9lTfvEZEvvDDjynuhoeHFh1DjYdZh2XeVN4YzyumSx1gaOtuCeEY9_-s93Dr7MYaCTBJKttBAZgCcW-p6BXGiFY8AcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHwlTM-aa00J8ZBxpMvhJw5ZShvSInWzDPXnioraUCKEsMpH9U993o_11ioBsfQzNbfj8ybjbRLX-IzA0WQx9kOci00DBWHwN-dZ_P79GM6gmrcPMMkZElcFkBuY_p4ISY6halZAbYvrMa1Yiq3EOW_x3t-onb4p4Is-_dbdxJvIFr5AX3y0QckacEGa10Qpq87o01cATI4w5mb2tHEkZjCYi9FESbGIxqpsAIbs7pC1ULdmSInVa_CfNKPBE0NDpKMRwPZP4Ko2_3HRl6s3RL48MY9JrB87TWRmiB_b-lwN_42STFhW2d6QMZCf6QlnNyvZ_5HOZlnKEQQTK1p8Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwr5-NZfY4MpJ2tqz4lqjY38iBwjhTDESZfNhBq5zsdeexh08uYBvUphQbZAHQtLGOHior_CHX_qNsvgD2MKipTwaOSTAYvTCJSwV3KyY7aQ196j440mMU7qAh215ZogZPjxdzS0V3NQBH9hVCaDMQivD6Aqxhe6FxCAp5VhZw4dtPwwvMDcpNwiFcDKYguqhHMJsEEANhGR-kAZsx0ZQjeymIdqxBLA7VMMyp-T7bRESu-cv-j2utGSEw8O2bh9FAMvpui4tNZzS3V4IvpDGStYtBfGUqDNFB2NnD5-6DREHjAZXSWCELxOwrmxHXzTeZaVy3jSQPmfQ3fdjeAaAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtnxqKfvZV3cx3LS3vngfoltkvTq7aU1Ydxdkgz2yE21Ru3j_Sjj3wPA556Bf3EnoIE1Ep-XVbdaPUqClJQ0cGWS5JqkbEIUqgDi_gKZz69WZurWpCqjh2jqeMYeII2k2HtZBXYlpAP-gX39kI1KifbqQ7fdkmC1ONZiHHEujRZrKPGT1QiQTf3Y0YpY5frBSBtjaEU0_KQRo8g1lAvac1e1ZEihF54S1WLcMV5-I1b9jUbfWdkD0PjMcAN-lyOzXeQPA-RHTEUUJ9mPMtQZPOSv9J5IMdHVxRLvKI0pPBY-RVK33xXoMu-m-rJLotU9nZNdPW3z32ZOnhLbw3AuKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwvzu7X23lgVjzIzRU-RucVj7VKSfSX1pRGnT0gHoMSUiWJ8klcT_MSUwtekPF1V_G7SdDbzS98kbRf7XLJex-L-h1bo9l3LN64AtFCfjI_0XM9wsvR-0Zr8xkB8_iQur70goC93Drw1xhjUADfVNgSrzqiDAd9My8wKOrfxXLGc9eD_p2GFgAwfi7X05FB3lbr7ygsX2wOMj8OCj4JOukyLhBblLChdaTuvoI_9u7GRGOkpQpxDp1XVOllqz7IkCEZXPASsqmuN4Qr7Ndk3AU-NEKj8tIe4kO3OXIMa27pGqjRKRRuWjrt_Xcjg-HqHSliqyIUHjzlXbHf70DmoNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkziGop9xvu5C2KBIghJIkvbUBmHlzSOO815Ta6HXURszo6dCbnuiEnx9mJB_DnV8IzR1OckWejb25IKYpT1syKnKErd09fd1FiSkIAG9bWC2B9OaH2_tKN_d_mo05c3RZ0pcVViM67jvg8y_WgzzASg1ao6LjYMegwUa_cN6iz54XyHnRl8QQjiVURhwGj-40mKBr9mGM5oHn7nN5DEmL4GmjEZXT7CHLb78sR3adHPa9RBP_-qq--18Dnrjs9cWaW7MfunozUbUX6D7i-QDhWQ909tRl23M3n5Cc9NXa-SPxXRvKOUFKNmODdc8BGCQ0fVnJvzGkp_zkIDeHx4AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tT0Ry-siaaHacl2wom7ve7QfIiSNhR_j7bSbKIVUiNz10be6h1ZEd0Il-mJTOlvwQXQV4l5VsC1lstOzBae3TFOSIA-IcP9TMy3m_wycGaT7FKYIPhyJA2pkqR-ZN-xH0UPB94hSbfkPaVWJAGGLbonKYh0Q6slO0HU8CTuXSVk-yy6SKMPm_wXfcv4Rc497JT5WbqlVBdKVEx2omujMmZwuNTkmYiBwvRjf2CtpBCZftCU9JBD9xLnXFJEtqNw7Iq5ssmcBioj-Akg0iyQn0g4lwWmBRFXA9pf2c8IQPrR-YC10RiWNgtHi10bbnt1SIWEUsRP1Rdw1uho1eSaHKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXKqk0BZsN55XVXrqy4anD3SBDAAaFYQ8fWqG2zgzFCt2Hjt7rtBe8MypOGvc56J24e9hNBkfBE3YaOxqDU_I6lYc2aXKnWvgVDADq85l-uURBmBl7KWRxUwbDxCrHiDTwn8KvTeTzqYsCFYhTSxVtPp1pX84iNq4oGgwkrEXrtnH1ZCMoW7CtyetghE9xaDwzMwK4VzZaEmmIbsIOKR_O4JGpAOEc_3IXN8gEoZXF-CIULe0nrU5KOefO14OPIC1SDLQthN9kU2eSTx3neObQ-xyBJa8fwOvayssVoLvcz3Hlv2JZhziCp2Tydgyp47aHx6B2fJuzFGWECUUTFpYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ds0NandyaF_CEmDh1y7nFHToTygL73Teg5h2cpiMrqDn0yKb1j2wvcjHicoY7YrjPsrGVC1dvWDeICV_HKfxnY4PmEKQrkMzclQX_c3tOD2zpei32JVYm7o4jQFjwTK76i3LXqod67UzOYD1vPvhFjOdWJW3ZEWENMIr7Ims-WBnONiA30Q5InvFbovLtN4p9Ya_eJ0nWfxkMnxmfBZFh3qmSbiUZhuuzoIka9RrIo9PJ8c-n1jrpWlgDSHDQis51iP0FoA3C4uZ3wkgrm_2iRTjbdJFjqG_Px0FLuD3t1X8xGgMPgAsXQZLzOzEy7VMYNvjpu4ExJT751pJ_hG7bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
