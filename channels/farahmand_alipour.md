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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 19:02:49</div>
<hr>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=kSQCEhRh1ln1qKpmztV0lYzalOb7m2qcV7JWw_TCmElhsvxoM75VasjhfwP7N7u8gHWwVwM0c9nGjSDkgQ3imV_G1M8cj-L1lMYveviE2vJeJFzUHtbis7kz0Dam0yXy9O_Sfvrr5DdBqaxha6Cqa91tZbcqjusafpiG0OXNcXfsIJYYSC1tXQUUh4YjM_K_ZvH3Fi45sY84kTJji5bDN3TYHR7Y4oazuz7v1K-7hhNDhRffzISZB8fUwQuIFhCkjumtjn9G0YOEFWESav8KMQdcQMYk0n3XaCUPJXEvSG1LtYpaZgnHXeunXNKJvCJYLpTN16TPOx5rnd2xkUdL1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=kSQCEhRh1ln1qKpmztV0lYzalOb7m2qcV7JWw_TCmElhsvxoM75VasjhfwP7N7u8gHWwVwM0c9nGjSDkgQ3imV_G1M8cj-L1lMYveviE2vJeJFzUHtbis7kz0Dam0yXy9O_Sfvrr5DdBqaxha6Cqa91tZbcqjusafpiG0OXNcXfsIJYYSC1tXQUUh4YjM_K_ZvH3Fi45sY84kTJji5bDN3TYHR7Y4oazuz7v1K-7hhNDhRffzISZB8fUwQuIFhCkjumtjn9G0YOEFWESav8KMQdcQMYk0n3XaCUPJXEvSG1LtYpaZgnHXeunXNKJvCJYLpTN16TPOx5rnd2xkUdL1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BNsFe1SHmULH0j95rxoDh53L96Jmj7tkp0F-FXLr5B_1IEBWgpAgJAKl2bIfSb4wJfakpxnR6wt1BG5D-SrH94n_QGa5RtkCjsOJKGCSzZ1UTzZv10jGXOIU649p1JIAJy6SBGx332rZcuTquzsJiXf9BiJVkJxQJBO9dx-85oZTq3lD-vUa_S9AuoTfyCq1pYFpIN9IJFH-Q6-QapNuqc3nFLHgihriXwqJM85n4jDa0C3pT03vAm4sB-wYPhWuh7XhXDu4DTdvk0QevdITH2XXYk_7iM3Me-4_s9yWAIiikxYLLxcWXK8moQmOfq447qEh6NTfxCT1ce2L15Pfrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N5_jB_jzFw_Ylt-DQnBsFwwJKTbInid8C9MARXI6XRu0bHtgJlDTMREJNSR3otEUREpoMvowgycOx8ahfMkioKyneBnRtgm1upyZmlFcC59VsDR5Cu-OVY9cZbg3MIW5b0r7s0xUaHeHwJFMjPQafv8VyJxIuFc06UOoasoRZyHwrXLMBeUaVdaGquF-ospQJ-FNIbVsKtiXyd3dcexFpOkTvpJD8NSnwvxQxonz5sgLs1vJm2RENWx43Eg3WOEZm7mhwUF2xHoiDTXAUEjH4enYa4Le2UP39D9YA3HTp6_GXIcNAMnwpU0JUgh8KAEkZJQ_ZdU81STa70zeHinMyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=ErnU24aFpGsgUu0i8WuUKGaUVzc7FbEk6DU4BXP-Vkpbt0sJOVwm3l65QMC0RENmjgTQfA4uNFLHxNY8KnOr0mPhGprkXO9uJPSQtKoojMwM992qgq3sZQav_0a6Uz4MC6huLuuB_kuIgoFlhC7y5D_CTqFZFK21BVl9JMKCkbJdmL0YMA3MgtBZCv38uMLPCRv8NrY9IAObCNWo-qDvDNxdK853vHn-G0hKy55O45EoKmXBsbNfQgYuIW0SuLwMrRsohzqte7BQ_3RBkARFBNUfEaesT4E9v-i4Vu0utb3SP4BjmKvO52tUC_gNqsLmdO6e6Tj2vl3TJKrEl6Lcwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=ErnU24aFpGsgUu0i8WuUKGaUVzc7FbEk6DU4BXP-Vkpbt0sJOVwm3l65QMC0RENmjgTQfA4uNFLHxNY8KnOr0mPhGprkXO9uJPSQtKoojMwM992qgq3sZQav_0a6Uz4MC6huLuuB_kuIgoFlhC7y5D_CTqFZFK21BVl9JMKCkbJdmL0YMA3MgtBZCv38uMLPCRv8NrY9IAObCNWo-qDvDNxdK853vHn-G0hKy55O45EoKmXBsbNfQgYuIW0SuLwMrRsohzqte7BQ_3RBkARFBNUfEaesT4E9v-i4Vu0utb3SP4BjmKvO52tUC_gNqsLmdO6e6Tj2vl3TJKrEl6Lcwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulFwHCGGyfqQyPD_ucwApTjIybhWCF-pMBxwvm_wLcfT4CIeCyiqwa8m7LVFOYt_xhLWN8__mBZjDyMLG2BQzWuBtlbcZTyXr2mmC87Uj2WXSjXBubG2buNSWuqzgliv-OBJUX3PHnvf8ChRmOFXK9pqNRIwX93Od-_0r77r29kKS3DsyZyaQc7STghZUNCF21sNYrDPby73EpxlyFHFApHGjSJf5eGhE-GTg2thVzzjjvEXtsNfSjacYZl1g7PhotsMuRGCEQxIi2oXOCDfdENZYoOfmBe0TCi8e7GVCRgds0tU2vc1z_MathCMLQywDGyiOMhSxzVLi6jKFQgnog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0L0NnhLMjyZE_jmq8E9IH5yCp80Ie0huEwqoQa3m5BM3Bkbg0cP7Udseq0SrJUsBH0syBNtbNx3eBCr-mQl8n6LyxE0TgVmPZ-3T1Z0k2fiEgV4OmZ-XObX8MLPja6eAF-vpo4StLzlbqyau3UY5B4iKOtEWgBmeD5svvJLMrJvpm74GJrmA3aOWuXByt_WVNNqL7A7mB06sWhht5BAgxnJ6XpXv9GNsDh9GwUmmApYy2KK31zjcSlUW8rMsRH2Qg2bbUp2ZOh9y_8NGx06pOi4fPyfj30a9g7Q8xuZS6y9ISGapGtv_L_sxnGK0-tvjcdg_JGA3TDnOhJ6iFBPKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fk3iPEtD-csJgtTCl3tnKEfJpWyqL_xDhiG1OkHknZ4dgKeZJWCSFKxVKzrIMvBgRQWMILZ7VuKWOp1a9nwoltU7-nJiZg-9Vm-AaPWRvdi8y_esfoabfLwP3ZKz-XUrRIV-A1RNq5ya6YYPkVQGeYPY2iz1EkuSceY_DNPpH2DKc82kUupOsf0SYUHK8czjWTrSP2poh8n6br-ESne0KqpC243_lHthinu1bDXrdFT6IYfyT-qMYTVdqI7_IOVbEk1R8qTk6DhpA04nDwN-iROah83u69_VSaU3HZ8lPjkSWWJLdw2FAvlxrExQ_DbzcHBnByxsJVuWNZ3dsuOelQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=Z8S5BNgY7KD7oSTxQ8y5B6Bs8wtFP1imQ6wpcpDJ3c8k3AwpazJzYidVSNLxXxU49SOmO_RkflhInl58-MHB5DmS8gzNgdgvIJCy1dl9e_9Ye4wlxgTTJLcow-_DHFds616F30yTCYBblr78le5rYb08a77LbA2q2jINUTzJJvEhmifPBb2BXCfkBotMhwsjA2wRB2NcyLXoO2By1afbEhcSCxPoqpVcKto-iL72VpsI_AmWNRYsMubzICIlMeISuW8bf1MWmsMFb11cc9DzdFHiQRQpDYQWWv5zPs2GpCnqTdt2TcqlaLz8V2zwVoRB4E7BI-IgoCjUZl0BuQ4xCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=Z8S5BNgY7KD7oSTxQ8y5B6Bs8wtFP1imQ6wpcpDJ3c8k3AwpazJzYidVSNLxXxU49SOmO_RkflhInl58-MHB5DmS8gzNgdgvIJCy1dl9e_9Ye4wlxgTTJLcow-_DHFds616F30yTCYBblr78le5rYb08a77LbA2q2jINUTzJJvEhmifPBb2BXCfkBotMhwsjA2wRB2NcyLXoO2By1afbEhcSCxPoqpVcKto-iL72VpsI_AmWNRYsMubzICIlMeISuW8bf1MWmsMFb11cc9DzdFHiQRQpDYQWWv5zPs2GpCnqTdt2TcqlaLz8V2zwVoRB4E7BI-IgoCjUZl0BuQ4xCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=XJhTjEzo0BoeVd1cqitpeyDKBuELN3Suk0sh46FCz_InDPdrxvCUF3Kd5f4E3ZM4AjJxFgB1UUGAdjTgLvWuFNrxyyeZpLZ1s2l3jYTGw3pgrOfPLStyYO4j5SMdhOZ8THnOWxw5gaS4p-XTXUm8Zc8VmQpDmX5XGcCrsjcOQ48-4-qqH9kgADurqJHfnZDiuPYbkTDWlzPw960g3JqQ9d_H8Citu3LKzkyyBakZzau5YQlcWlcAcxSMPeeHrVTw_o91KaR8gJteNoEEXXOa-4AMxIznb6DYlwxEeruiq2966ChSGezFSRELTRztHLypnSgZgdE4V06vWlVjTpy0eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=XJhTjEzo0BoeVd1cqitpeyDKBuELN3Suk0sh46FCz_InDPdrxvCUF3Kd5f4E3ZM4AjJxFgB1UUGAdjTgLvWuFNrxyyeZpLZ1s2l3jYTGw3pgrOfPLStyYO4j5SMdhOZ8THnOWxw5gaS4p-XTXUm8Zc8VmQpDmX5XGcCrsjcOQ48-4-qqH9kgADurqJHfnZDiuPYbkTDWlzPw960g3JqQ9d_H8Citu3LKzkyyBakZzau5YQlcWlcAcxSMPeeHrVTw_o91KaR8gJteNoEEXXOa-4AMxIznb6DYlwxEeruiq2966ChSGezFSRELTRztHLypnSgZgdE4V06vWlVjTpy0eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=bpvFMmoe71E4AAnuL3lKrX0yzNVNMrbp7KOhC4Zjc9VBBP-kJC9an35jjdpZUZM_2Ek_eXuKG5NBtgAIrzoplC-36tLMOOysMEvzmWzuM7IMAGZwijUosFGjjDsLufL0d7drVBo48IddqURHP6_GVH3lrn-5dCuvI98ULEFnxIRtDbQe-wO3y7dHYMBjGpXuveu1TA4uau4IKPJW8eYI9PgbodLOHOi2YwKcUG2Zt-zrEfo1HAVgOKvbBC6Xg62rIVW8WZbmVhS707B6dQ9oY60mGXuKKoqj32bm-41FWcIv-JIwoQiNYRx205QK92lSK2rz6FFgus5XwngpqBugeQfg1GlcRjOsWk9QLcoi9AsMZE-A9-x5k_NSui1V036pGOYksk-7j6QtoTqBJBm-ZXVnoclE4IHcxwjgVzfaAP-RUuhKIHwlhenVqj8qVEGwm2OCs6U_vTmo4YltZ7rprzQZPK8h14N9GywJWniokKyo7rym4VpVHjthIh8V5MKa4fPyTPXwAorbxRsJ2vB1HpS3OhtMmeDfpQwR4tNgSl7OPTe-kBKUKiWnRgDqTVw32yoPUDhuN9xUHtZOKOYLo0n3lHLQS8DmAnZ3pcY4Ws7CDCTioJ6liGEZVnZ59fjbgrxlgaLafwJgdnoUsK6tfe9r3kvL17iHiHR4dlwoUnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=bpvFMmoe71E4AAnuL3lKrX0yzNVNMrbp7KOhC4Zjc9VBBP-kJC9an35jjdpZUZM_2Ek_eXuKG5NBtgAIrzoplC-36tLMOOysMEvzmWzuM7IMAGZwijUosFGjjDsLufL0d7drVBo48IddqURHP6_GVH3lrn-5dCuvI98ULEFnxIRtDbQe-wO3y7dHYMBjGpXuveu1TA4uau4IKPJW8eYI9PgbodLOHOi2YwKcUG2Zt-zrEfo1HAVgOKvbBC6Xg62rIVW8WZbmVhS707B6dQ9oY60mGXuKKoqj32bm-41FWcIv-JIwoQiNYRx205QK92lSK2rz6FFgus5XwngpqBugeQfg1GlcRjOsWk9QLcoi9AsMZE-A9-x5k_NSui1V036pGOYksk-7j6QtoTqBJBm-ZXVnoclE4IHcxwjgVzfaAP-RUuhKIHwlhenVqj8qVEGwm2OCs6U_vTmo4YltZ7rprzQZPK8h14N9GywJWniokKyo7rym4VpVHjthIh8V5MKa4fPyTPXwAorbxRsJ2vB1HpS3OhtMmeDfpQwR4tNgSl7OPTe-kBKUKiWnRgDqTVw32yoPUDhuN9xUHtZOKOYLo0n3lHLQS8DmAnZ3pcY4Ws7CDCTioJ6liGEZVnZ59fjbgrxlgaLafwJgdnoUsK6tfe9r3kvL17iHiHR4dlwoUnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=cUrTWIW9OZE7RVW4pyy55_c5PrZ2zbCs0BsHRp-5K34ttrVV4HekA9DNnhT4l0YWBHTfcvN2Htq5hWnbzC7tJzvmNjYaZX5UNTrSGa-622-l2Yak2pLQuVkrZQlpPhCoe38IlDpchlLA6S7FDvCAhDgjWIXTCVDunSrWQ7Tn5mhEDE9a2rf1GNGr8VfZlnJGDKeYhOnOUT6TC5gmTsiPmir6molgLzIBcnxXXZpTcxvdjV_LHbXw0NArjQr7ie4zuje878G5ehhDLJgIBYNAQER-twxPcVj-Vxk7Zfdr4uXoC3WUCJ90udM9gntM0vhwb_tho5mYSmXqNjD_geDLpzR4_nmXb3MxMpjjL-BERy5Rmd_8oxwxy-okU_7MNudzMoxo4_SPoRU54qxQOOoqv1vIvwlZxVtC0fycRnPEsxT8QLPYwgLkdz02pVKGG2cjajGVQwk283yy3PLNokHxQrThFD2lnsBPqDFlwNWANLEJDvlvjC-S9cNsWbmXjobZehiV6RVq7mgpYgnTWsZKbm5ivK5aArtZDVPFth5H5VIdpdLnJ36ixEbAAOfvSFdnoSdSo-b9dMWcwmoOQzNS-AWekxAir-YyrMZQ087DS8Mc7MKOhYiG90JEAlC6812mzGho8cZn4_oCwJoqLL8CE1y0MiGCQYRKdk8gSDwpwKI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=cUrTWIW9OZE7RVW4pyy55_c5PrZ2zbCs0BsHRp-5K34ttrVV4HekA9DNnhT4l0YWBHTfcvN2Htq5hWnbzC7tJzvmNjYaZX5UNTrSGa-622-l2Yak2pLQuVkrZQlpPhCoe38IlDpchlLA6S7FDvCAhDgjWIXTCVDunSrWQ7Tn5mhEDE9a2rf1GNGr8VfZlnJGDKeYhOnOUT6TC5gmTsiPmir6molgLzIBcnxXXZpTcxvdjV_LHbXw0NArjQr7ie4zuje878G5ehhDLJgIBYNAQER-twxPcVj-Vxk7Zfdr4uXoC3WUCJ90udM9gntM0vhwb_tho5mYSmXqNjD_geDLpzR4_nmXb3MxMpjjL-BERy5Rmd_8oxwxy-okU_7MNudzMoxo4_SPoRU54qxQOOoqv1vIvwlZxVtC0fycRnPEsxT8QLPYwgLkdz02pVKGG2cjajGVQwk283yy3PLNokHxQrThFD2lnsBPqDFlwNWANLEJDvlvjC-S9cNsWbmXjobZehiV6RVq7mgpYgnTWsZKbm5ivK5aArtZDVPFth5H5VIdpdLnJ36ixEbAAOfvSFdnoSdSo-b9dMWcwmoOQzNS-AWekxAir-YyrMZQ087DS8Mc7MKOhYiG90JEAlC6812mzGho8cZn4_oCwJoqLL8CE1y0MiGCQYRKdk8gSDwpwKI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=tSw6G2TtyMGzJEB1vrZ5BkxuI2Hh9TZe1qHn0nIHU58hjNnDVa3IZIJyKm-1i1tvzzPOBrOmk4BNZY0YiHFKO3h-Hday8Vl-6MaLCbdvADox9VjrD1X0ky9wiTU-OMjBC_G2AEtlVFMOeTAUvxNheELcV7Xpf0mewVjghJWovtM8kiH25i2fnFT8CVlnCkHoP9VCqpqO-SRPC7DRl1FYnl48uz5sxBYLveEyNuWTK1VqVViGBo3lhJi_GQC8nNslrp7XxmpItrNboDzV2k746n1D9uSCw-WFNlLxWWjfKOThst2-csnmuCp4Rm9EFtxFDdYWOv3nwE23CbkzCM7fqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=tSw6G2TtyMGzJEB1vrZ5BkxuI2Hh9TZe1qHn0nIHU58hjNnDVa3IZIJyKm-1i1tvzzPOBrOmk4BNZY0YiHFKO3h-Hday8Vl-6MaLCbdvADox9VjrD1X0ky9wiTU-OMjBC_G2AEtlVFMOeTAUvxNheELcV7Xpf0mewVjghJWovtM8kiH25i2fnFT8CVlnCkHoP9VCqpqO-SRPC7DRl1FYnl48uz5sxBYLveEyNuWTK1VqVViGBo3lhJi_GQC8nNslrp7XxmpItrNboDzV2k746n1D9uSCw-WFNlLxWWjfKOThst2-csnmuCp4Rm9EFtxFDdYWOv3nwE23CbkzCM7fqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y00S2A0R4qFwwsARFC9RCZ-xTQGK-_UHxpTZZX7i6isTYxJElfshrOHQbxKETAMdnYgudApcEG5yqZAaa0cZIbBIAE9cnmY_HhUsQpNkgCG1fk9BXX9PiC0ojjj6jOp_PHhZDcZFq6NYNiMUx-fycAsaJ6PpQWNb1QmOsEtLp2NALxgNe9IvMgPmzEAtU_x-b6RnAFeKb7lTDWAoxhVH9dU_UCh_Tq5fmCbcyJO7BB3WowfflafeBFmHsbRi6Ag0_Ijel5V_fyhD571LlhS9c66qhowtp8UEDbO2_70NHz3xe6QropDKKlpbX6CAPTMEYds8pM-7ItA_tei_wI_BeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=ik2cgOnUmgAwAOezvnGLFv2cV7PilTylx4ii1VQaAw_W6dWb1Kpu4o7C5fZtYbV9HEVYnLI9qh4TxVpK1zJcuwCnNolQlYKzXlJHts7GdbvqpPiEipqVd7r_ZpSoMocCL7R_LSYj_jZJGhKMLEG8p_nBMzN4TA5-fpC6fuX55C86iqnaKWXsquOPp0ZCenvNQLrThh1M7Aok1Lc7thvzivCRfjyDT4JEikgHmo5-95YIwMKkyp2S3es2C-YdiCRvkSNtgBlb7B9AnRYCPtURJy1YhChIreMbcxNSMOqg5zpMfsNlqfUVIs4FUefN9TJLmVQpJJi9JEERgbn2vErQgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=ik2cgOnUmgAwAOezvnGLFv2cV7PilTylx4ii1VQaAw_W6dWb1Kpu4o7C5fZtYbV9HEVYnLI9qh4TxVpK1zJcuwCnNolQlYKzXlJHts7GdbvqpPiEipqVd7r_ZpSoMocCL7R_LSYj_jZJGhKMLEG8p_nBMzN4TA5-fpC6fuX55C86iqnaKWXsquOPp0ZCenvNQLrThh1M7Aok1Lc7thvzivCRfjyDT4JEikgHmo5-95YIwMKkyp2S3es2C-YdiCRvkSNtgBlb7B9AnRYCPtURJy1YhChIreMbcxNSMOqg5zpMfsNlqfUVIs4FUefN9TJLmVQpJJi9JEERgbn2vErQgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=b8Q1dlz2DEb4_m5zK_5w1H-8r8LzAGDbwWFDN3H51F7lrRQJ1zeDetiTq55Qv7V4IriewGoGz4goq4p1hKzdK82mo18GCi7iO6qGxfX6zRybK1rpNJrN8lb2x2pum319qFk-tFGa5fbJv7VZCNeAN9HUJYD3CMVysw2P-O6ms9LQ7VCOy7pdcqfCqkQd6JA-T-kzIoOOmKwsV6Lli_ulmzDcM8D_iBnf3zbAQRJBB-yfHlo8JIgQe3-7yyxDzFcjzXaK1YDnHuBh70ehIIj3Znz2BM7X5xD6xqE2WmnsXZV_JEp8x5fm09KAyt3ydh9aDHYu7GPTNpB9XDkGWXVScA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=b8Q1dlz2DEb4_m5zK_5w1H-8r8LzAGDbwWFDN3H51F7lrRQJ1zeDetiTq55Qv7V4IriewGoGz4goq4p1hKzdK82mo18GCi7iO6qGxfX6zRybK1rpNJrN8lb2x2pum319qFk-tFGa5fbJv7VZCNeAN9HUJYD3CMVysw2P-O6ms9LQ7VCOy7pdcqfCqkQd6JA-T-kzIoOOmKwsV6Lli_ulmzDcM8D_iBnf3zbAQRJBB-yfHlo8JIgQe3-7yyxDzFcjzXaK1YDnHuBh70ehIIj3Znz2BM7X5xD6xqE2WmnsXZV_JEp8x5fm09KAyt3ydh9aDHYu7GPTNpB9XDkGWXVScA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUqGbQVIm1WfA8dTRaHUKRLpxAzOQvcss2-AiAyvzwEv6wyrO0I9Bv9TyCIZBsHTo1Z5O0AvRMj8UCLgztqMGMOt4yoTDH-8MdUT3iW5iKWwNl1Jj5jvMnLu0MOmVBoUcKOJjEQrTKlXI5EbfbDKxY4haang6vS6PsKv5nrt43QjfTyHULERxRJfYVKrWQ_Nq50VeFAejWt5bTG2IMyvgT2KdNXqcMXGwJ3MFqAyn8xbQm6jARDnRRKH3aCamWF3zD9sBJbb6aTVMODpjgB3gWdAuUjXb_FCaMzeTozP02Qr6SkQZch6Ju9LQ4mL_9UhQPTzEEEwr6_WlxRfzuc2jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbFp-D-8NvIa_cpqEpFOey2XuZ_JTnFUfg0kHTEAHV7ytxCb3_i7ADwd12AjD1euZ8Xa3a1pyZT3j7dnpOl4QmcHTyi6aE0xppvUakAsxt9fXZMYGf8yJtBA9iqnvFfyVVPqNy26xhTDkAWGc34AEfv4D7qwldoTK_ukuXkqWjWSSdLzuSQsM94Z6tQfXWfXC-8rLO9GK401Et7pshfj1wOeS1jtheBFQme0vev_kz1CDECSCabR1z2xqO05qxAT5mnVdsxrj1nrlUQFBqDFe5TSHCKWI90hh7m_UsGBmKdH5CwV8vyvXtVSJRtybLs-gVrcsCrZDFoItM9kBDp12w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8J1FGo3E5SkCAqNpyT7aNFO3oeW-rQx0Z9AJyetjL7miw-0WGO3cyV4SDrMIr2rXCGm0luGFMbveBWn6KuEUX8c3xnP9AwdMOdWa4J6kg8MEndlSZeCIqvk8-WR3rNHUbOZjLv6UdclZxi0b9N6l70LwhgPOo7pqYHIDCTL_MbYf1xGelDO4h1OUtLUrhL2grprU77JGVZ8Xsyz8vcQR7FHVBZ-VV2dQ80p-fVXeArp5uvM8QHuPE9eexNDp78VrIjrZPE46zhfLXwIS-YSkg3lRbaiX79sASqg9pPWwPioE4qqFK0B5RM-FvXGtRs_mbKqTAdckewcj9v7dI0_Jw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qj-EFLkmvZbNQh3YbqgRvGlJA7O5ezPzOhZ3Wn8tEikwXCp3IgZUIe0GedmcBkCVarEQpSAuJwCHaxfLxOSdKMMJ-OmOKhyHTh0ORdeQJtGghgzotMjerhxvsDsvbvZsn1R4JfhkzRfOffXkVAfonokQK0TmVRbdbCe1glz16NPbRH_PQhyt62hPklTnL6XEuhemMgzBmt8euxtkaVYT6uZSCn_BqVi5IW8CroCZel6mYtGMEVzvjPt-UpGaqKJfXxoiEohlPs5RaNcO_-khg_FlzGMB2rclvQX2hfDpEWR0qJ5jq_i4QBvw40p0uPaaZ0z2UQhE_vcuMAZvXn551Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKJkeI8C1axKMecqxYGeHokeesK_P4mT1K3p3G1koWLcINVfKs_rd1KrzYdNXrS3H60zvlHuPFGXk2J_MbtHaRL3f0evRpRtEy6W_lPpllilXzrUMAT5C7jMDyi2sfJWopFBIj0KLHHy0LVMSeDKR9Ruwcg3cWiuphnY6tnArSxdXopp_H6sbI90F0RAqsff0Xt8zMIJdOJgIDupJs8O31hzchS1_sFMN7mKjmfTzHSUkfHNVY4DR3dlcllJsOdk46tJYaC4MPFcMkDLSsiXW5wY8g9V93c1Z5WhNo9pbhxm890q2KZyxXyRCqQNcS7P6fac7MRz7djm2KqLPq9QuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJE9xSIndpkfTAC6jcjNQ3nEftrV2gvaXdgmm4tLQYD1KIvPUArll3ihbbqmwhEoGV3UZzLHfPpAGi0z5r5ibSrPrHfhtaB1rp5LhaCvl7hqVh2Qfk1D0W7VWfpvTaNfHPq5K5EmsNtY_5GnNacq1o2DRwQoAJ7aTGVmrEofiOAz7By_hlmPDpeG5XGw1sAO7_Punv94KznGs0KHUJT9FVwh5hWaHSjqtJS5ciAV37H5N8LT5_oV65MJmD9aWi3p5Hkb7H8dTNKSVbGEz0rvQETkfLEZ4F_lY2O3KyI-YpsZLZ8yQ7KOUH9n_xdlpXRJ8zOCW4_ZnS1rdXL2xMIwuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-QNcNoc9TUp1M7a3Uxbe5w1L5h8SKIG51eLwXnmZ5GC3sEOw0r2aZHtTjNbxaxWeOlZIn6XSRTHJQxadZMHzF6pA9jl3saINDlQeXq-PQLWytqz_Q5mBh4twIJlOzoFjCvgJlVtyb2PGMoK8KSzojIsso1EeIO2FJISrv-W5B_EbRNe1RhosoGKb_L3p20uLQPUWLn3Ie5m2HD-ItZBNJ41Dkiza2X2A5rNJC3-faWjdQsL1O8ueU98PwQ4jXbO1LxPlN4ZOTr-pZBI-4RiN4EMnUMTEHxsN0iOYsHvKktXj5iz2VGKRFMZdDIFWxcYnTdHjzjoD7hrQlrPfJz-DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pFHWoFU8Kpi0Luib0u2zm2LADBCLynpAXR7ZathugoTKScx_Q4lwwE4oL5a_HgY_N2Napt1Al-FzoROd1N4VzV4HMNN24eszCmo-JgfrSyeVTyZ9ochGGJgmfXntTx6mHR53bRygqS1H50rnMTOzjhdeqwTqDSHeydZhU9H2sgI1xu_UcJoz2Td7w6ruw8u24GaqKM4V8z8TtrfzErsgYmvdGmt27ox_wyH2Gj0IG_qvi6S17K6f2hmlnbeK2OoOG_8AqYZsqnM-0ctzr5Rpms2Af1uTbj8KrqPWNMcVAaVmthzJ9iejww8M3r1MMO2sb8ngwMpRTJ9lZSpK4n9nHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tnHOuZ2H9cGMh1TrXHF8ysJbXzxoBkCb8WyH4ixjE5k4newMNnWFnCJuzrB70uLZ3wz7P6afrv1c01vDlLtZ2XUzaEmuxJxUkhPlM4Fqt_ANd6fsvqty9Yf0JaIS_ItqJSaM8NEO0cb_FidCVaZ-v1zSt0sL7L-i3L74f_aZHh1r5bLETmtrN2cfmO7lcvDcbYh1bWOmcAD0mJzsxkbLVkJrrCorGRgT0lX3FDJiOb2TyqF1rLKBNy0CCv3Gx2YzjLL8eXuG9CE5dL8Sway5vFUU7Z-XIKiMax0xb7Ri9TxSxoTHwkNcLnb_68wNfVu2AdyPdJnYD5L18hA55KftRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qMiN2xYyXQ6PwYApXam_TtsNxLVAMAiAYK0uKvLQ6Sssk0KzcSAle2gcJ4tauSPucIi1PK4AtKPD0U-OCskcwUdbPQ_shUdchmMIuv6YaV36Mj5wJfHIoGeACN14Ww9_bMxsrF9T2XHkbAHE9-XW6DZwgAp1lunSbD8lc4V93JI9htXEVe7GxeuiaPE7itaxARUH-MvT_BWEhGPpjfgpdgVfL99YJ7VoxQg0CYVFQKne65pouflXNIaFb1W19DGB3sR6XCzgV3WxMgcxhqwiDswwTWTD08FquYeeNxOv1pk2nt_rW8etBLriwBE_pxx7Oz7OOmuTaWcWzsTVr6caAw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=nQWVg0z6egt1dLiWbkR80D7OMH8CYctenQkCKwfMHgTbybWzPrJ7IoHfwnOrXfLBHHMjKQ-XxqqPPEl5vPTyMq41FFgnLD0ISEDRV7L2rGCLy3Ve83t9bp2ebDOsA-t-mKILiPrOkQfsll4qVovBKd-cLpFRot4nRU63yBYbZnf2PAZ7McFPWHm5cnLksze4ZCGLr2zfFyJqic-zQ8ipYopF7h0YE0ciF3SC2KGewp3Aus8S4FSmTqgmOEW5USMBjdSdUNn2YmlK8QpUBeAZq6JpL_KJEsJy7VYX1thxIq49uvoyc9zaDj3xHREobbgCG3hWIqRKQjxWqxeiJjVM7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=nQWVg0z6egt1dLiWbkR80D7OMH8CYctenQkCKwfMHgTbybWzPrJ7IoHfwnOrXfLBHHMjKQ-XxqqPPEl5vPTyMq41FFgnLD0ISEDRV7L2rGCLy3Ve83t9bp2ebDOsA-t-mKILiPrOkQfsll4qVovBKd-cLpFRot4nRU63yBYbZnf2PAZ7McFPWHm5cnLksze4ZCGLr2zfFyJqic-zQ8ipYopF7h0YE0ciF3SC2KGewp3Aus8S4FSmTqgmOEW5USMBjdSdUNn2YmlK8QpUBeAZq6JpL_KJEsJy7VYX1thxIq49uvoyc9zaDj3xHREobbgCG3hWIqRKQjxWqxeiJjVM7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDIS8YxE1kdi1h_bcbIclXNFrG-oJTaoYj6phkYCpoJBWB0X7aWIeM9_lCMTxqU7RdomHNgkawzXReKrwb1HlTkJvzolX1SLOJDf2pu5KL1QH0mqPmsswC3G0ha61kOsU64XbMi7HO-DUrpPRNuEiGO4S0eAciz9mS8D_wNOcRkY_ci4q0IvXUpCba0aA-bMNcgKE5tXj_sMnKkh4wYVKk6jHqV8gYrcrAx4_rtamVWdsUCl4AB7vrOT3CaW4qWOTVpDdR6kTZ_aL4lolT9GhKe5aJJ1FbHC0Tk_oGtyaInPbe39LYT3_oh0ETGOkTZxm1DrpYMq4srkCyRc-ZvFgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCxd7DyqIfScryX1G7477PEMgtNLt3e-wRD3I3eKnPGkcqzSvM-l9MOPII53p5v6a4SChu-Bzw4lghdpS2SNeyKm_s0bVVqnq1bHfPTWwV9vfTQN3iDWC-XPaxsAJvr1hXrlO_ppXTmKEZZyQIfawTZcGtXc-XsLkoeD0YE4pvE-y-mFtQeyVHdzOCZMUEgQX2XJPphRVfiQCT1TJBDqpurjw4u2kPGKiCmNL5HAej9sNxT_NTBt-pmkLZl4-lCTaVsZJtc31y780rYvE5l7VT76p3SSO2wG3p1Iy-oLH-g91jU1qRKZpEK_v3j_Kszy-3qv9bDVmbZqrapCEVfzZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=iX6XElm8CjjwdVyRENxijCNvZzuc9KtN0bGW8z_5-tV-3PnCI4T6LqKBm9KgYCHV3TIFGjlGr_lnPVttyWrwGX83JRpgPb6Hv51DOO407I6AQAElQujfeq0VqCsoRnXlec7CIh-HTkdzWX0L41v2q_IqjFG6TsmkHTeu2X5ucWvKnwB89RtYSlIwJKUxP78m25tLzHSwCZtOBeE84hgUBJOLH2KWJVZjHjFR7cv1HjbUyL8MVmaMquh0LFIWQgdzkhS-7J1U5P2Gg1IFvidCC3Rpxpb8kI5NGmOzQaGJBAHfYcmWMRDoYUb3Lq5xdywhugQRbZAjRMcwsBh-d-1mbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=iX6XElm8CjjwdVyRENxijCNvZzuc9KtN0bGW8z_5-tV-3PnCI4T6LqKBm9KgYCHV3TIFGjlGr_lnPVttyWrwGX83JRpgPb6Hv51DOO407I6AQAElQujfeq0VqCsoRnXlec7CIh-HTkdzWX0L41v2q_IqjFG6TsmkHTeu2X5ucWvKnwB89RtYSlIwJKUxP78m25tLzHSwCZtOBeE84hgUBJOLH2KWJVZjHjFR7cv1HjbUyL8MVmaMquh0LFIWQgdzkhS-7J1U5P2Gg1IFvidCC3Rpxpb8kI5NGmOzQaGJBAHfYcmWMRDoYUb3Lq5xdywhugQRbZAjRMcwsBh-d-1mbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=Qu7KrkBszNodqFsaSsDBKLaiDqhxJoW95LatHMYtlL8OXDZeWoxHXKz0UNeFHHMUmWhSTxx2_xJGuN_ky2Lf5v8GOPdDJqCbKy0GDVmKhRCHBYuobSMQ05IO_Tly9Vh_IYRN77-tCc0Mv3SRW2e0wpWgRcvMARWB0MnzHjfSkCeim1FhcanVhppKw3QykuBo8h-eLcUw9I7wpSM4zK7LZr83glu8GLXTmJGrihC3wfOzCPgqIML9eqHsJYVGXHuTJLRQpcA2c7Wf6EsL6_sCIYq2kdEobnXsnX7YSA6YYqAX9mVfIGHy3xYs2xc9jxiM25UyQaPZ5wg7dS7I1-WnvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=Qu7KrkBszNodqFsaSsDBKLaiDqhxJoW95LatHMYtlL8OXDZeWoxHXKz0UNeFHHMUmWhSTxx2_xJGuN_ky2Lf5v8GOPdDJqCbKy0GDVmKhRCHBYuobSMQ05IO_Tly9Vh_IYRN77-tCc0Mv3SRW2e0wpWgRcvMARWB0MnzHjfSkCeim1FhcanVhppKw3QykuBo8h-eLcUw9I7wpSM4zK7LZr83glu8GLXTmJGrihC3wfOzCPgqIML9eqHsJYVGXHuTJLRQpcA2c7Wf6EsL6_sCIYq2kdEobnXsnX7YSA6YYqAX9mVfIGHy3xYs2xc9jxiM25UyQaPZ5wg7dS7I1-WnvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0lt3HQmUqqTq1MTGfCs01B3bqJRy_aklt_DnRGgmTE69Jj3dUl5OMKEteVXV7EN-6HnnJJfxoosAttcHQLRMFlMB2xQP3V2VZntisrpYgVUA3j2a7O_RdZzH7Ja7ff3RLqz1eH8I81qvKu8tcm18fHgwCQXb3Z0uJEWp_VhTx6TyVtD930p7BY9gDiX9HTuEWbgQk0tzNKojdvVcQrhO-Sg_N1SYTy1HGXWnSY2rTLKuK-EauDbsbyysJV4wxLaOuLc3kkrcw1YSGblCJGE6mv6npXJYlZSEZ1n3IM9Bp-fIUTPA3fLmFvRkAvX3v7l7Da95JYsiEnumGsH4qts6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZ54CS1ioRVkeBev4ggYUHR9E9yIhxLBcFhqgXImHp5QDoP8hdcgzILWFim3_akRtUY2ZdR6HSprjojGl3CrB2NSFDmtyNINaKR-qFOkeL8hcrY0OpUR2mlMVaOPpgmLM_TZGB_rwp4rqcU0X1XuCwc6qXqlD4DFHzLmcot0IzcPK_oqQwQXxBIjoru238wkzQdf9-xgoSLbO5EfB01G1_juh407LXKoMt5sDgtqKutkKBqcREbnJp61Mqxzkh7taTV8lf_WxpEbrDFH3xs77qYg9-3jtU29g0eIEqtM58pivU6pdZRs4sXsqm-geWf-YNZWo8qbKgJWpP2r1lQIcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZWnjICZo4Z6a7CVFEgGm4hCwy_ahTR8jyUrV1NlFNJuMupvybgpsjytkxMO_wk2R1GgwmcZ5WQ7ED0c4zop0MDuYU0Vqr8z8Vyog2a_ocDpM4tjCry4po6-FPEicLVK240SriWAkeQUEyDh2QI3-sB3JTVrNbOkK2WjYoz6UlLTJGEfC7FDkyDSls0CTDXPoU9Plhbwl11hmN5aql4LAjtMmAgnL2staPuTqPoVDp7mylvFp3fKpAAu0VrMmqjFSg6d-Ih8hzCBD3O4W7fsnndWR31gQ1EKRPEKWtp2zUPZVoePbE_8y9bJlGFtrRmIf3whU1egzTvaz6nFq_gT6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDiwiAKHI5-ly3UU9fpT_SYaRyBROyiZh5LGFMCGMUjfpWIGz1MY6NDKWBngHZ7nX-gsqP2MbzyOezBeZgKrrK53QvgfX3Cme47D97_6JJ-_UWFp4LGdY0v4LflZN8PFR4uwC7YavoblDqtg3MYVO2fVxxbt50ljj7hV4DZb_Cio2hACdHeFlNvM6B608yAH7DBtwyGl4X2SANb3zIcM43T0KosT_RVSnD9cM6MUncRu_kuMw1mbEK9opdw4JMbl8Q8EslfywfCdSOMRKb4mpx_z3or1Tjj7yAYuT6DyGmh-URnRPUBbPEvxMkbzxS4MBSsXRDtD_fX3aP-HIM6IQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2-IF2B3612vfPhfm-80lWci7_7xzYTqe2xoyLlWqorq1EZB4Z9UaBhryWOQHqrK-keLXQX-sxrvLcY5iPoBembpKjBGovVxfib8A3YEQY1okaMzibNqsYAgjzaMPDsz2bgDfZFya_arpNoIaGmunyU0TO0m2FpB_C3V5Eg9J7oeg-kFxXBysc4-3dje6dxKu567uEWbtZ4nR-0ToSDTtqA_ItJTBXL2EBUcBvTmBNiZIps7UDcvj7KC4Xn600QfFZ1V3BosRV5IIQ_o3NC6F12Zc46dSTgBskNm49hdBATy18DJ-E3n9v4v8udvLXmfDuGKDptjIqMKroIM4McTNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9TSb8_aVxWjprYaXt97eU_Ns6PmU9o7Si4CbEBR4Nq14MsMlzCVxGl7gl8lpKjX8_6WqAfjEKeHBMOYIrxeoMku6ph2bbetxhUBCRj-Q19Ztt98J1497gGcLq4SL7ljz6JeMxSxFW5la4fNaJAnm-v6IUEXgpj7JFU4EaLLyi_LcLyqbCB1Hl_vm09RYUYU8drwbRc7le_-8uz0_HaM-00wIUV7AThuWVOTA5OkY1IICgSYRyk4CvYHB_DPiMf1fMzRaw1E8SWCqPKVokhQkkL53kvlvyST-_RWwVHHi9Q09wHW3IxfIpkL6NWiP3SRNMTVGxwitWNIZdrcNs5BOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPAb7szRBLnevtKXxS-nFUVhF3fe1U_PpU4FDCA-z7TihnIdBV-77nw3PAmdFmHEw5GQoPLXjJoGIqa7fz37UnUdN5VPz-JZUU3uAN2H2bI9d_fwrcBIX_2lPRSS6hh_QfHIcAan-K-rKlot9Ip_FYJbgEtDs1K2btV00NPHcYtmFHrRZZfDZ4WuS6MtXRRONdOnnF9hAQlMIsBzmPbzx-WFuxG-Zadxb1YdIgijWva7FoP8o1X3ZZPJs1TRKPJGgA5Ms7nknUAFpdW6F9R4d-7pHLjj8_1iekKGtNs-ff2yzLdC6raeNoAkagoBBC96GI49UQMz19eNty3tw22zeA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=F-it3zpLOimHZfJn36uNWm_jK7Mevace9O54rI792T-MGmS0aXr5baydmapdYYY8bQ9Z15SEm-SLDJSh-akRrQDKTyS9d5tn0z3ultWmIPgQN2QaSx5ZXr4Dn1Tm2hT-VIyuarki6lPcmzsatqwlMFc-EFbT2x7Bn3ky985n8ZRZjR_O59GWh1GRfUHz0FlJMdIEXiUqLTMxA93E_XEJSUGlL0UeG7rnbV__OWfnNH46Q7C76lPDtSJRjixRLTEB7gs0E3hE3bvE_tEOSp5F69QBqtmHxFTZUDGEqKyNrtfeR2eI7dC1k6xbpXCZgTQiQn0wp8EWGMcZQkwlrbO4_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=F-it3zpLOimHZfJn36uNWm_jK7Mevace9O54rI792T-MGmS0aXr5baydmapdYYY8bQ9Z15SEm-SLDJSh-akRrQDKTyS9d5tn0z3ultWmIPgQN2QaSx5ZXr4Dn1Tm2hT-VIyuarki6lPcmzsatqwlMFc-EFbT2x7Bn3ky985n8ZRZjR_O59GWh1GRfUHz0FlJMdIEXiUqLTMxA93E_XEJSUGlL0UeG7rnbV__OWfnNH46Q7C76lPDtSJRjixRLTEB7gs0E3hE3bvE_tEOSp5F69QBqtmHxFTZUDGEqKyNrtfeR2eI7dC1k6xbpXCZgTQiQn0wp8EWGMcZQkwlrbO4_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgiHPf5r1JLLRnR4w7kcTVU-PQvhv_XSWQWdSfAHFkUDctuLwPsk00PcqS090qFeW0UX8cp0yhFddAdDI2EFLrQVVsPxKcUJP0k40s1hb3DsgHkV0aP2cap7MuPlUGtxEP0pPW3R0SxfDsuEEZh6SiXHU9skTBi9LzDgE3tDpJrJv3hlCt9E5mZL5hX2nn_QtJIKTk-a1i6QvyjZY8wSU1gWldgub-WxJeRDOq5khnwUzJ6bo2kT-zgeRM1GMFH5wgZeD2yfRiUT5sb_FM-HZNfZxDY_K0XXyoSwe-XLjUc53a4VgpeTmpnqMyoLl1WLWjC7v_qDjgKMZlrEtQ8m-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=aw8Y47o9gvGOXGgX7hnS1XA9u_jiTJT5PfnbaBtzJ5cdSLfw5PZZ8Qia8w3mfTeZkFB8vCczz0036o3B9L5M8pdUYhS-oB29qQcl6nht0wl7FI3otBvQ2n69_pK6jPcu-InQDMMfPk7yX6q-7C0BBYbMTbJThX3delRR64m0BzPiqfiVqwFDQ1KoI3iyFHSN2SHdvkZPlGo2995jT7Gv2md8AjUOcqf_Z5myTEMtmnskU0LDp-qPM-1ZXFBgmF2Hpa2CthUJFpuDmdLBRe_fc7YjNNYYU6f32eQXJAl_1dPFCfw5PSHaMi52gzDY_Seh_EYSbzOtkTxpW1ofq70HEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=aw8Y47o9gvGOXGgX7hnS1XA9u_jiTJT5PfnbaBtzJ5cdSLfw5PZZ8Qia8w3mfTeZkFB8vCczz0036o3B9L5M8pdUYhS-oB29qQcl6nht0wl7FI3otBvQ2n69_pK6jPcu-InQDMMfPk7yX6q-7C0BBYbMTbJThX3delRR64m0BzPiqfiVqwFDQ1KoI3iyFHSN2SHdvkZPlGo2995jT7Gv2md8AjUOcqf_Z5myTEMtmnskU0LDp-qPM-1ZXFBgmF2Hpa2CthUJFpuDmdLBRe_fc7YjNNYYU6f32eQXJAl_1dPFCfw5PSHaMi52gzDY_Seh_EYSbzOtkTxpW1ofq70HEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=WSL4CRicKtWtDy-YJqw_vbBtsHxk1NWHqSg5jDIVHPsKw7i8yJBE1ayjUdbm1IojaFBqM6Vb3gLbi8u4JsCRRJJiL_9hnvi4IRiHX95YcGWBrTKaH4PTpMPAeMolvZC1KeGFjpp9JFrZFivtZdCQI2_3bi_602JFtgFWO1GXfcUoUiS4DtpFIRy1YrCOhNrTY7F4HBxXFwA0Fc5PFT9Y3TLlZp2hDOWa3jgJtq5rbSiEyy2toKmIPJZPc7cViCXRjTgnrSnpYiPxyPAIKca5RhNBiSB1JiFkUlq6wxSxJxtfZdj3tpVk0csj754RjCqDHKX74SnmEqZT8wPIvmoDUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=WSL4CRicKtWtDy-YJqw_vbBtsHxk1NWHqSg5jDIVHPsKw7i8yJBE1ayjUdbm1IojaFBqM6Vb3gLbi8u4JsCRRJJiL_9hnvi4IRiHX95YcGWBrTKaH4PTpMPAeMolvZC1KeGFjpp9JFrZFivtZdCQI2_3bi_602JFtgFWO1GXfcUoUiS4DtpFIRy1YrCOhNrTY7F4HBxXFwA0Fc5PFT9Y3TLlZp2hDOWa3jgJtq5rbSiEyy2toKmIPJZPc7cViCXRjTgnrSnpYiPxyPAIKca5RhNBiSB1JiFkUlq6wxSxJxtfZdj3tpVk0csj754RjCqDHKX74SnmEqZT8wPIvmoDUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIe6hc3tK3yRKvjz3EDJAdER22fjebrawWynrNMOflaor08laNNUDEYq7whi9GP0JB4Yh0mxON5RU1QECRNZiuOB7NSwBEvCrtcUSvgMAT4BcVQ8ZKxr_n-9JKdH9ezHghjQgs-usCTIdJPd-jwrs6FLueWeVpzkvcuJDkRAXdaXlwouJL5ajcWURV4g6NvRrURV0uir7WsuaPq0Dh4ddhDH3w7ax9FjjU33rLqflZlSqn_hWL2WQr6BidUb6Gx1Pwp1YZhtDpfmmoTwHhcc6KVOzPkA0XVGMhAJ8BPQ9AodYO5NdXZp96cMnu33Y9SRIGaRhx20qSpYVZTRAxIIBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VT4iS9iLjQBkneNAhdOjkcjlGSewwzbTRa3rkjij8B1JLlTOxw9KxLso1m2WF5ZmLZdCQ0FTDf-otNelL7aPkkR8c9vx1nFZolKAyTHnG-qHAxluGOYgBYtfNaTdm7a__CJoPexzIki7fy_KRlAxAQU2kUV12fnJAerzK6Q24iY7NzvNNd6I2F7WDdE8DvXqG_6IA2e_IoV0xG3lXh5dxODEjgyEeZ5G0mw9315SSSmLqD93YSN3qId71eOvqTjkVkgoYrpQCqCOwqYcgst6hLQoYEBD07LTKIwzLs4WtjWwDqpNYX-ABBkV7bjsC8KpaVgYpRzRmeaelzaxFEHSPQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=t7h-IUaQ1xWaWCTeEi2b1wWLsurzB4H34VZCrBg5J3_uKx3Si9Yxh3xQ5yM1qERGzBOJuBWIttRtVWLgP2WbMLxy8hxLBRpPB02U0fLUFfy7S4yECSydXaVLPSkfIVQWc_l9TGePM7KmS-ZL7oVIJUS25Ogj-01PBeJSHOmLH_g5chMQmw_l34fVBujMBV0E2GzITXAGyufutPAAxSkihaCXugfe6ld5BP1eMRF1_Fa-YtGJ_7SL2SFEWOAxvkqwU5YsLyoKqitblfeZT72spT5U742DMDHuZeidqNl6UTURjFpqOlDbADHiF_yubgU45CGMnwD4o8EZSi_f6LVHjgYQwb7dhmMHbaSszeKu-RGb2Ek0FZggB66EdPTuVuj68Q0O1oa2CMR-qq4IkzuFnY6VosQRvUI7lQviqJkKV8BItz-71VvrxiCzd_JJ9JqHbn1VFFnX3sboyIDfEudY1ArEYzUF6ihoukbMeEqlIK4RjObEY4hH_wdxYE4Ba2H-sSW7X1DqlVPLFqR7I9byztfJ8cDAUBgiqs0d4BPE7OOOFCd8efw0yaEkwigaNrD0nBsCowI1-Pul3AR8oenVkdbzKaiZvWh5oTI2C0hxbwqdCoDAn719hDdNOAvh_ed8ikYcr0h4_B5qgyPfWiJa3cQ4i3q0cYprs7ujnOkk7iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=t7h-IUaQ1xWaWCTeEi2b1wWLsurzB4H34VZCrBg5J3_uKx3Si9Yxh3xQ5yM1qERGzBOJuBWIttRtVWLgP2WbMLxy8hxLBRpPB02U0fLUFfy7S4yECSydXaVLPSkfIVQWc_l9TGePM7KmS-ZL7oVIJUS25Ogj-01PBeJSHOmLH_g5chMQmw_l34fVBujMBV0E2GzITXAGyufutPAAxSkihaCXugfe6ld5BP1eMRF1_Fa-YtGJ_7SL2SFEWOAxvkqwU5YsLyoKqitblfeZT72spT5U742DMDHuZeidqNl6UTURjFpqOlDbADHiF_yubgU45CGMnwD4o8EZSi_f6LVHjgYQwb7dhmMHbaSszeKu-RGb2Ek0FZggB66EdPTuVuj68Q0O1oa2CMR-qq4IkzuFnY6VosQRvUI7lQviqJkKV8BItz-71VvrxiCzd_JJ9JqHbn1VFFnX3sboyIDfEudY1ArEYzUF6ihoukbMeEqlIK4RjObEY4hH_wdxYE4Ba2H-sSW7X1DqlVPLFqR7I9byztfJ8cDAUBgiqs0d4BPE7OOOFCd8efw0yaEkwigaNrD0nBsCowI1-Pul3AR8oenVkdbzKaiZvWh5oTI2C0hxbwqdCoDAn719hDdNOAvh_ed8ikYcr0h4_B5qgyPfWiJa3cQ4i3q0cYprs7ujnOkk7iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gt_dEsqeaCdiUpXkqOs-YxqMnPMAmL78RLCT-24Ef9qlt-SvrI4lLQkA1onOMAesoVb8hTkEP3mjZ4sjZK148mRsj8sNFofDs3thtX95Gk2G9rbHWR5XVUQMEY0SHJA7GRNKZw9OxwEgBjH3GDWJpotmMVSvbuiugDE1DD9mXuETSM2kM7Q0Su80dAun7GbOOoeS18vleVGN3bIxjCVrwWaRIq_-LFO1LKq18hnoGYMY-Qz5yOjvwJ9x31zB_78fDufrEmSiiu2u59mDgUafKe4W2z0I4dbuVSHZYSKmXHU-N4JGy8v_xh6nzLnfryqezX2udYWdu7oeqfygK7rocw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=Dnl6WmSKDpMYLsjU9HoRMCO8htl_tMjlJd24xDQc9Wlu5p-S0Z9_rEGh-6jXWVx_i1Q6MOU0IWniQZizg9AxeftJL65mUGn4LiKlnK4OOfSN8y6l5uXzt7NM7dKBDwGprkkjAb-dhhFtEzlPBmi-OUsuk6XOpa_rH1O6U6tleDbw0FDRxEkFyLLxhg2il_xRSBwHFRNurTvu24PZ_uk0mu3T1dhEEuFQzY1kmLosM4IWiBKI_eOJ3LaY7pUMSvrpTBYB0UGdkz0fuEEfv3BukfnWLxCUhigIlK35SzcsUZE2hqLLg6BZNN41BMS1ezZwBc2tJbh3WsEa4zXuI-tra7QHvEhxNBOAepTBQQh3mFcDncEg1bHTGnZjFzZl8kbO3z6-pvl0ZF_gZuS-JMATUr55Wl6rJ3EJog5LAQ_9FzWMrpebGUyKQukNJW1MPS583p0fc_Qv8JGez8Qk0cH5ixGeKqGzFxq3Dkc7ERygZCgYlfRlnae9SkUwI0BGEFJp__d9BsCRk9QosEwjSctzPuW6MtqTssGjBafIgvth4a9feNhJnMqIOomtZUdJNPH2zAS8Qfg0D3Z_AJr7i57-byDKICdHXnFQLntH0lDklKFUpLY6YYlVp18OcuMrSOJaVbrJfzqeNSGGjDOvapXtSFUmcahCTqfA0xQfbSfXGSo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=Dnl6WmSKDpMYLsjU9HoRMCO8htl_tMjlJd24xDQc9Wlu5p-S0Z9_rEGh-6jXWVx_i1Q6MOU0IWniQZizg9AxeftJL65mUGn4LiKlnK4OOfSN8y6l5uXzt7NM7dKBDwGprkkjAb-dhhFtEzlPBmi-OUsuk6XOpa_rH1O6U6tleDbw0FDRxEkFyLLxhg2il_xRSBwHFRNurTvu24PZ_uk0mu3T1dhEEuFQzY1kmLosM4IWiBKI_eOJ3LaY7pUMSvrpTBYB0UGdkz0fuEEfv3BukfnWLxCUhigIlK35SzcsUZE2hqLLg6BZNN41BMS1ezZwBc2tJbh3WsEa4zXuI-tra7QHvEhxNBOAepTBQQh3mFcDncEg1bHTGnZjFzZl8kbO3z6-pvl0ZF_gZuS-JMATUr55Wl6rJ3EJog5LAQ_9FzWMrpebGUyKQukNJW1MPS583p0fc_Qv8JGez8Qk0cH5ixGeKqGzFxq3Dkc7ERygZCgYlfRlnae9SkUwI0BGEFJp__d9BsCRk9QosEwjSctzPuW6MtqTssGjBafIgvth4a9feNhJnMqIOomtZUdJNPH2zAS8Qfg0D3Z_AJr7i57-byDKICdHXnFQLntH0lDklKFUpLY6YYlVp18OcuMrSOJaVbrJfzqeNSGGjDOvapXtSFUmcahCTqfA0xQfbSfXGSo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L10HmtJTNL2wTApQlOOzoPW8RysOHiZwKnqj8PLXRdJENJJkLkdZP_5KHL7v6bb6NqrOyGphiUTeWceICI1_fpyK6W_AjctclsUE7uM8oMWL9kHJPrDNXJfkRxHeZK2GIK1lXPORqEu4KL3_3yty8e4CX6duZpz1Zj9ohrUXz2UDPlx1HFp_xkBVTLAuTgc_J763u8Nr--OcuN9wO4A1RuPoJ1VHGwAXwCzSqigMz5FH59f0NQORVIJOp0U5C8jzSw37qHgwB0a-hffokhvJlJm7Z7yd2_kfDYLThMaA9eU9OfSCdqgxVeUR_CowKtODzqP1VCFiodzH9Fa0z_DpMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5RUUlD_T4nwxaTInRbfiu-Di8Q1ccPe-A23Gd2soDIAvkovsEskw4Vf2-sCeSXofFuJN8cgKhJaK3Pp3uP198mUquLwsaTlWVqXWtJzMKozfiaJDtNMRHW6BhQ_tIT398NunXJ6V8aGg835XwvC_5LAiDV7z3ZX_m-uDaqyGcjOcA9K3TRDU9JYeVrXg8GYICh5QP208D-Lr_7UNZ6zbwUVypIvtTgoJZDPRvCZcOBDPqTYAcXBPrbEnfFOgHulu075zokjkYzW2c-eB_ZSuGsJZj-G2qT7Ori_cJ95Or5Fs6QP_iMAqvudeUNtrsgP5Q-H41tXPEwirkBqGuosyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaBftmFFFOpazUBYv9FGU6FoPhRAK97VMZ_OPpAjRmBtBuFXEm7klyjgzhnaJ-gSd86z3q_YMkrqLeda4i2Gzngg1FJUAnOm6O-JKBGEFU0l9Q5Tfg5uP3NrQXX2WIiYHfN-wfFQXQv4LSk9913U3V_D9GELJvHKZ8adPdv4QePNRcXr-cUal7jjzOvXrS1HYebqWD1l4_yZ-SHTYSFmu_E8FgSkmIu8IhO8XZAzYA5qLs086CP0P84-TI8dd6v31Zk8h2VLgXuNkrp8dWE3AfXaECBMjEX34JQjeTjL_tGIq61pOLIy7ndWotqNxQEwXdDiEwX5V20mwGaH5ThBKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzamcfdL5BYd_2_uv-Sihfr33DnXGq-dXdDnCj25gkuhKyW6-sI93TqNlRQDnLFNgBsMH5cG7YTjQfLDgKciRnGccIv-Xxc1erzzDiGbaXLUTdp3NUMal4P24-8TRqrH894mTGQH1vR4CE6FvMUcZY3yU7BxW1ugYJV6Ahhptw-u5QMlYI9m6SfAefUEKvVc2AsbhSAuLHRpXIPRHomQMAVY5GqVrFUGNh8p1q7a6H-TPFsyXmLXSpssSWr8W42jRIl2VUohdPg_vUnjwPoIDA72AomGjlgFKyw99Zfh8jT2Cqr8IAS71eSJfu0V0QCFiKzqFpWII9EQn708tqiBGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cb4kyDMytkCj-Cb_zt42qx0_44XR6gFhawxfCp-gJpIbZa7AJUvJ4CHKNUtzvOEqARjayG-JaBZoK5bprWuKw8rfU-U3lVsbN-Kp8gLCU9bMiMuHeLc40FpK_vvHGeuHXzSc8sfii_fgAO3BzNqXiYBxuxNA2p8fA2_WhWWzdoDh24Nmbb20GwuRVgJPPD_5NefJUDzN9NKczVpTDYq4OE1KJw6sUT6pt0pNiDmVmKRGK8Qn6fX1YNy1BljxFR8Nple5_lvo0Y1SsyM0XGb2ruW0xjU7qQB_IqJpfFmYXUNu45MA1TyBPZ21NUCOZoJUvgKNaHqqFSTgB3wC39GiFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlF3e2NcQB61arDunBKd2_c7aigu8EvytAzrSNgUbmLTR_JJgKu7ymAW_Io8GkmZIK1cmpSHqOc5hMVyQdV1gZirhjpQ09qTFPQhuVlBB93bQLRmRz3ekjL0NC_ZtmjJLkrgY8orP4Ffk8FgVi45w9qLE05wJqU3_NrV9jkE6fn-pyJO6Sj9_VqAKjJWijEgvHUY-8plIiUvsl2KZGq23Ou1eqlOiyposwZVH0LZLw9CrOII0M-Q7Yl0bPZStoPINgjfWjytyCIgDsoYwMp4oF7SIA6jjYAUVuJ5V_FG6REmAkAnXuvpNXg5nxTXeqHc8JLQq6A3xXEbc2Pm7Orm2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWcARv70ysVuTFs5podjsu1M4zjHJHXb-3nJlbdbN8b4fSiAhA-qKC4RIeoRLnTLuPKhpKMEOjjFhQltsXot6qMVS84eIMWhMzyEqTqN4_qkMWvokchFh1oRDuM7PbxbENDou-Ld_7XF7Yu22N5wE18M_04It7FFbE7J-964PxAxS-8E6koZ8787QM2T2jC0e1dDEt2F6VT47GVe9QFPN9t9hJlqpi49TbifHH6slW2c-XnZTM1PqigvECf4JH00RNDgExrGe4qVMBkE-YDxlvo0RODEB6gHOocxNXSTe9h0hS5CzL8H78GtnLN8_rn_SZMoguVH6FcenYBuB2WEvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HN3QP9vVB2m6AQ_597VLqzBqLBEnbS0YlV1nRzEuST9oKhiKoR_rzX7KxNpQEItU5f6F7Hk8C_ftuepv4uSh2YOFGdPd2uvSnQ0b3fqTq-VLM8MVVfRmDmYKs2VtQeandwMPyKIN5uyXTOfTbQaU1SA8_Vz-iwa-aeXYF8Fk-DxciIcNoul-d-qnfMnyIWcrRwBg6Ww2K9GPVoBr50YsMqP6k5X_hgynR-LtIyeFNstFsRfWZ4Pz1uPPd53I1M7pbI_gQgwyz-kN6Fy4LSm9apEeCo9WvsmiLNfeRWaUHbFST7PfpcDrPsCqz7_nL66zq7OlfcfX65tTMFY6Zdf6MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeDNc8dq5vvsd7V1U9H3uU6tnRIj4NkgylT0yuHqX-qTsiQ8_8Np9un3Hrxbucp6aXBsSdyrgTBbLQYGsQ-qFqJ1_VFoBwssp4SAq8tAExotvJSc-ny-i6slJ6MzzTuTj5Hk7RXDIC50kCri2h_-LqJGef_oFblsIyXF_41ydNNUAcZZ7l5nodnhyCPJraeZ8qYgjGNmONacdWCqAXn27U5GOjIfoa5suLwd07UEG4wjY8efSV24fAaSx4tXdiXBqTbjxcVYQtSUnih1MPXLEhKPWjDbg1kC8GvJZ1tQWxx3jAxTi_yHKU85YnX974TtbHthpMm0wBGY-90FkKV0Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6YndW4Xua-CWMH3OdF2srK2JN_2nRAxX2_PbqCve4eK3fn4eaKmLqpW6ysE0ScbbV0P2jrOVc5MkqjSVArUIgarnxEV999qJLpi3prXefkL5nKL1iDFBoZgMX4StyHr_Lk8DAQ-XwFpZGDDdBMNVBDGKtqXTI3QmEFeS1vbCWKITyshunc1--CjcqLScS02B4hPuECPS_fud_EdHz8p9twkgbga7inh3AujAhXx796fdXJ-pQsF2Gb6vthZyNNMqAJxm-lxI-NSu3X07ERVMU_sB6PZtn2vcLO9PaDeEsW5_cJvp1OAIOXCRh6jVo9Ckn-MRpZ-vUjyqBtUWxl7iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcqLgWfh9CMJJH3D4iMLG4w4sqmn0WXditupI4fOIU5c3s-0YjvlapkZb3gdvVwkZlfy5m0QsRwIjzBQJfUlJaxqeL0xxnB9l-kVy0JdBn6FjVoA_UI_PWlI2tMWvJuLhri7nnTHJBHrZzDpCXN2mnxPJErgtpcQtlYCJvKdk5yQZx8z8ce3DqnPDSFhWb9uR451b9p_BCd6AD_JI8sUkdSJKwMmVHwZqpH81wufGEH-T1QfJ-u19aN0pVp0ErMJhR610UJmN-pT67RYcv7QI-5SoGG30kk2Iq0ypW5T7Getxb2QfVnI3tDnHfE-15UaIzb2oJH0BLPClR3aQ3_lpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
