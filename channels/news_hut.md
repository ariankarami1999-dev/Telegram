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
<img src="https://cdn4.telesco.pe/file/Dg0WRgoEdKlhP7PkANmk30b2tUpDP2uTWXcP_2g0PQTAYNGRLZ7wxRcxfFbDvfL1GQKUek1aiZLQ5k0KGbIZEt6qHlKI7LMcIQBpHpQQc33iAykfZdNp_RbMrFsK8bDl7zaxL00WKL1Zn0DWsZKxfIjvq3uddGLuQu34st6Ht89nbr8_HRYSR5cexZ0ysWLKSXxR8XjqF62fPMobkncO3UbPIjStevrr2E3c6DJrarmNqfVPMC8dcQjjvWMK_3td4_rNaadVH5_rzqctO5bIz8PAoBqU9JvcSDfDoDk7VqjqIwvXIAxZpF60KdXmKKOCtk2bGMXo3qxiDWne47L4Wg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 106K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 21:02:41</div>
<hr>

<div class="tg-post" id="msg-71961">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C646lXkvnREq2QbN2wWtYp_zS6VFw0hPV8QahfngKx0WzH1H_573ATD0oJkVQPXJ-5EtWsBNOl-WRAY2EtlJEHV8Jb8OrKayKtLgYpUKG7VwQxFq2aUpfi8WLTWcCx7jeJOwrEsBuLfrrauwrw_wMNaGMVw0-8nG5_0ovjrL5-lnoNcnU2jJILS0ldoUyLnA0mQSINW-MU9hsPCk4AORaxexzIQo7MRmwfPF579vAZEtDmBQPvTobltmjbYFWZFcWQ45jn7bGnA3sV9g1CHhNKubnGRWnxu1GLlqknvdp4hBhCTZzAReB7OWvTDgs5z10732m8LlCZNx-zee_Tm4Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/news_hut/71961" target="_blank">📅 20:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71959">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10eceadf6.mp4?token=e5WPSkHxLlq6At_iAHddtvY71HYFbxmIqiI5Tgx1Ei1vzogR2mHlRoTwYqN3XaUZaVKHECD4yzk_baY9NN7M4bLU-7606oTairYwdG8bCN8WFbdhh8rfMBtxxDoeTm1yzjlydEOGiy6njVwXJaTmgvbQ_ec5fQiwEqzCz3qGZCvVB4tg9_vD7YoNlb7pM07VL5Z456ChhDL4tb1yvoi7_UJReuRdHE6oy6-OnuuDPxY2O2ZtHMi5Ffw_zykNFCojXQ_XjAVDyabjbPCpjDqro-no3DvqN4uLwok3gW_ESXC58ytlVLeAb-TKGstLy0DqWEOPzp5m5_-pzZJlrt-g0yP-AvOWiG3aUvXxZjX4AfoGb-_351UHymyPkyG-fVO6KtIjronfLv9v-fupH7oPXmFCqL3xGdhBp4_sCtrHry28pDv0Q0Qzk4YlAg-uSbAo370sS7Zm8ve6GOAmJ2A6gi4OsW1PvQ6pgYDZRxUj8mWxHj-rx_L0iLC7V3AIupomzG5OSY0baRqQp6v4ngVY6xt3qI1hVqRrPZ3HYdCsC67wTs1W1WaBflFNd2oQhN3jHWXniQLCNJCg4fr8YshYPhwwLtecsGGrYA9PxFHOnJuDC2ATQ2xHRmf-unuovUceJ5Q-pgDqDin4dFuhFpvmsvPHlQv3pft7gkXM-tn8mVM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10eceadf6.mp4?token=e5WPSkHxLlq6At_iAHddtvY71HYFbxmIqiI5Tgx1Ei1vzogR2mHlRoTwYqN3XaUZaVKHECD4yzk_baY9NN7M4bLU-7606oTairYwdG8bCN8WFbdhh8rfMBtxxDoeTm1yzjlydEOGiy6njVwXJaTmgvbQ_ec5fQiwEqzCz3qGZCvVB4tg9_vD7YoNlb7pM07VL5Z456ChhDL4tb1yvoi7_UJReuRdHE6oy6-OnuuDPxY2O2ZtHMi5Ffw_zykNFCojXQ_XjAVDyabjbPCpjDqro-no3DvqN4uLwok3gW_ESXC58ytlVLeAb-TKGstLy0DqWEOPzp5m5_-pzZJlrt-g0yP-AvOWiG3aUvXxZjX4AfoGb-_351UHymyPkyG-fVO6KtIjronfLv9v-fupH7oPXmFCqL3xGdhBp4_sCtrHry28pDv0Q0Qzk4YlAg-uSbAo370sS7Zm8ve6GOAmJ2A6gi4OsW1PvQ6pgYDZRxUj8mWxHj-rx_L0iLC7V3AIupomzG5OSY0baRqQp6v4ngVY6xt3qI1hVqRrPZ3HYdCsC67wTs1W1WaBflFNd2oQhN3jHWXniQLCNJCg4fr8YshYPhwwLtecsGGrYA9PxFHOnJuDC2ATQ2xHRmf-unuovUceJ5Q-pgDqDin4dFuhFpvmsvPHlQv3pft7gkXM-tn8mVM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشتی «لوچینگ یوان‌یو ۱۰۸» با پرچم چین و یک کشتی باری با پرچم پاناما در نزدیکی سواحل سنگاپور با یکدیگر برخورد کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/news_hut/71959" target="_blank">📅 20:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71958">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d61320a9.mp4?token=YHHZ_WUWtzqpfo1t4EhQG2iex8A2sIvAk-NIa0aEiW3ifCioJl7-v8bgKyFAgJqvXRFm79xHkjatETUmbS8Xjic4XfGpI25nX027cB67Z4y-iqUaVs7T6zT8o4nFkTFiTze9vMUEY2HgcMCDDMM6tOJf6gUFf_4yfYS6D0knUvTIri8PpJqPyk6EQ7pcXzxgk7s8jsEBwmLdgdGvguH11P0ItFYY0kXTRFlLIDxO1Rq12FGaXKrLPTrIxl-PJgNW752nGY6p1ZwN59fbgM4cZSVYtHKRZi4kSx52KDVY1buaGzhZfJ83MFQyI8ImSLgioVgEob5EGatvPddxHl7TUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d61320a9.mp4?token=YHHZ_WUWtzqpfo1t4EhQG2iex8A2sIvAk-NIa0aEiW3ifCioJl7-v8bgKyFAgJqvXRFm79xHkjatETUmbS8Xjic4XfGpI25nX027cB67Z4y-iqUaVs7T6zT8o4nFkTFiTze9vMUEY2HgcMCDDMM6tOJf6gUFf_4yfYS6D0knUvTIri8PpJqPyk6EQ7pcXzxgk7s8jsEBwmLdgdGvguH11P0ItFYY0kXTRFlLIDxO1Rq12FGaXKrLPTrIxl-PJgNW752nGY6p1ZwN59fbgM4cZSVYtHKRZi4kSx52KDVY1buaGzhZfJ83MFQyI8ImSLgioVgEob5EGatvPddxHl7TUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک هموطن به مایک جانسون رئیس مجلس نمایندگان آمریکا:
لطفا کار مربوط به ایران را تمام کنید
۸۰ میلیون ایرانی منتظر شما هستند
مایک جانسون:
میدونم ، قطعا و علامت پیروزی
✌🏻
@News_Hut</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/news_hut/71958" target="_blank">📅 19:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71957">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b0937658f.mp4?token=OzGoPDj98vrRzy5L9-S9ohXmlZz4VPUbMOMPIbpsV1uK1k96jWdJzmXRj0WY_r4v_RV-zz5nD5MqdXzNwdDc7aghr23HYrs-4T8DL9kqB7Ay9Hm8sqzHLBgM0QwR2s564NG7RLCU0XRSnC29T4GAPQHgHoliPw6KdyVXak6tTNUo6CHaeR4ZBat_VShxFyAQDn-yXBfJovGRIlPHOP1IYkItECsbJSyHPhyFgzYgrubBQyN3fp9-Fkxxz2qcVBpCJ-7y4MhexP0u_RMMtG6VQrE5geonHvaJOwoVPmMOmnBlZDDdLdDE9uPWbJS6nyHZnxH2KO8t5irZo--6_1s4Mm-VRpXzZM5LZvXTSumZsVchx32ynCpBxFJvySTxtSa9GCru94ukN3dG_lQSR-VqLCgYHW8ifCD4RgWbZxUEq_7D12CMGsOCvepu2zNC08DKm6OaQx0UmUEQsOp7AJwHe5k7AHC_Heula37hVjKn4Xxx5Dgy6mxStIlSepOdvimVQXJtC_sLpPvrBZFI6WgSWpB2rLANBVPo5HEgVRxUPpeq2_x0SCC_bNj9BzL-OWtCdjxKa6h_fmWlOE_fdi8YhxfiWYlqCZrsjkaaQbrK6f3J8SYuqEutkYCDfu9P9FMXmHnhbnPmOoz7mNNwPElpg3ID1cYUO88lO8QWLuIlzT8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b0937658f.mp4?token=OzGoPDj98vrRzy5L9-S9ohXmlZz4VPUbMOMPIbpsV1uK1k96jWdJzmXRj0WY_r4v_RV-zz5nD5MqdXzNwdDc7aghr23HYrs-4T8DL9kqB7Ay9Hm8sqzHLBgM0QwR2s564NG7RLCU0XRSnC29T4GAPQHgHoliPw6KdyVXak6tTNUo6CHaeR4ZBat_VShxFyAQDn-yXBfJovGRIlPHOP1IYkItECsbJSyHPhyFgzYgrubBQyN3fp9-Fkxxz2qcVBpCJ-7y4MhexP0u_RMMtG6VQrE5geonHvaJOwoVPmMOmnBlZDDdLdDE9uPWbJS6nyHZnxH2KO8t5irZo--6_1s4Mm-VRpXzZM5LZvXTSumZsVchx32ynCpBxFJvySTxtSa9GCru94ukN3dG_lQSR-VqLCgYHW8ifCD4RgWbZxUEq_7D12CMGsOCvepu2zNC08DKm6OaQx0UmUEQsOp7AJwHe5k7AHC_Heula37hVjKn4Xxx5Dgy6mxStIlSepOdvimVQXJtC_sLpPvrBZFI6WgSWpB2rLANBVPo5HEgVRxUPpeq2_x0SCC_bNj9BzL-OWtCdjxKa6h_fmWlOE_fdi8YhxfiWYlqCZrsjkaaQbrK6f3J8SYuqEutkYCDfu9P9FMXmHnhbnPmOoz7mNNwPElpg3ID1cYUO88lO8QWLuIlzT8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش، یک موشک رهگیر پدافند هوایی اوکراین در حومه کی‌یف موفق به اصابت به پهپاد جت‌سوز روسی «گران-۵» (Geran-5) نشد و این پهپاد لحظاتی بعد به هدف برخورد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/71957" target="_blank">📅 18:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71954">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12842b3342.mp4?token=YDSovQHnlPCwZkz6q4pNALB0BlGdh7sa1WMlgfiES7wtynH_L8taV2qeci1drSvWZyKebfy6GFWe0W_dHfRszkrmof7hZiZhw_2GxjmyYTBcr2LlmH--eLjOFwlEMlH2DMeK2VnISLKatuDVReLgeokFETZ1ub-Wj_ddW5CtlvmfwC3Bp_PXzONC2WAXF0we8vEEEsqfRD5BApgNxckaxcxa264foLAGFTYfKS3CE-SbBStjuCQFNjIfcFUNXpGbYNGgZcXBqVmXVUHtP4zOTu1Tr6BnyR8101rHfWPglnM8Fb8I0y-WRVS3UEBn-NJ5mt6rLpQ4SEC9cnInTxY6wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12842b3342.mp4?token=YDSovQHnlPCwZkz6q4pNALB0BlGdh7sa1WMlgfiES7wtynH_L8taV2qeci1drSvWZyKebfy6GFWe0W_dHfRszkrmof7hZiZhw_2GxjmyYTBcr2LlmH--eLjOFwlEMlH2DMeK2VnISLKatuDVReLgeokFETZ1ub-Wj_ddW5CtlvmfwC3Bp_PXzONC2WAXF0we8vEEEsqfRD5BApgNxckaxcxa264foLAGFTYfKS3CE-SbBStjuCQFNjIfcFUNXpGbYNGgZcXBqVmXVUHtP4zOTu1Tr6BnyR8101rHfWPglnM8Fb8I0y-WRVS3UEBn-NJ5mt6rLpQ4SEC9cnInTxY6wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به گزارش رویترز، سامانه‌های پدافند هوایی در اربیل (واقع در اقلیم کردستان عراق) یک پهپاد را در نزدیکی فرودگاه اربیل سرنگون کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/71954" target="_blank">📅 18:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71953">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی:
دخل و خرج زندگی مردم آمریکا با هم نمی‌خواند و آمریکایی‌ها در مسائل داخلی به جان هم افتاده‌اند
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/71953" target="_blank">📅 18:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71952">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71952" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/71952" target="_blank">📅 18:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71951">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXNg0f7PiuyHQk6vuSmcUNfc_nGY-x9TZlK-qeknxZ4-Hn2jvdwjbckGKjPs8pbaWvDPum2nf7Yv8AB-2r3iPy5psk_hbsJ_HptvuoCae4hMufGgvH3_NH8zWAu5fOKZD-76IZ_iAXf76J72Hjep1VNe7Hm7bDMHNZPzq_plcFdOzMU0McRr4JVDMTjR3zVhqFTARjB89y-BzLoyfFiIyOY7zWSiS-4nWhLDyI24r4EufdHkK_gA7KxutxX79M_g7M7ZuJuPwdX52v55-77sHM5wq0Yp7Lqkn45iKFTR9zn4pnsaMRQto3BafWrxQ3bbUvfyR0DohZSYotYT3pw2Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/71951" target="_blank">📅 18:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71950">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ea24117fc.mp4?token=EkcGwG1jW3i-Z6rbPlQM5hrE9HN6PmXS_sfpHqtx0cYkB6qqO21AJv52WMgJv3cpuKEO7MXvc7IABRzsJikmmY5S9PyNe5YeLoirR6gzN_tSe5UoQ4p3MABIOyfFk_yct6uVNJg3Io3vGrS5HA7sveFnF_HIJkoRJ7X_ESE9i-YP-4JkFFuUeq3JCZEP8UEZ8MknUlBBofFES-07tTKA9dtvIerX_oUP4yRlH2PmDk9YnNhWf-RFvrb_636p8EzCL7Fy47U4yNU3zz5g7xSEVfPip7yvOo0O3doqVa1jD0iHj2bjCdnXXe_vcYuRY1Eq4D0rYwvlPGZ3P34zaaUulw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ea24117fc.mp4?token=EkcGwG1jW3i-Z6rbPlQM5hrE9HN6PmXS_sfpHqtx0cYkB6qqO21AJv52WMgJv3cpuKEO7MXvc7IABRzsJikmmY5S9PyNe5YeLoirR6gzN_tSe5UoQ4p3MABIOyfFk_yct6uVNJg3Io3vGrS5HA7sveFnF_HIJkoRJ7X_ESE9i-YP-4JkFFuUeq3JCZEP8UEZ8MknUlBBofFES-07tTKA9dtvIerX_oUP4yRlH2PmDk9YnNhWf-RFvrb_636p8EzCL7Fy47U4yNU3zz5g7xSEVfPip7yvOo0O3doqVa1jD0iHj2bjCdnXXe_vcYuRY1Eq4D0rYwvlPGZ3P34zaaUulw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
برخی از مقامات ایرانی همچون موش‌ها پنهان شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/71950" target="_blank">📅 17:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71949">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ درباره ایران:  در «مرحله تصمیم‌گیری» هستم و در آینده‌ای نه چندان دور، اتفاقات بسیار بزرگی رخ خواهد داد.  گزینه‌ها عبارتند از: نابودی کامل ایران، رها کردن آن‌ها تا از نظر اقتصادی بپوسند، یا دستیابی به توافق.  بهتر است درست رفتار کنند!  @News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/71949" target="_blank">📅 17:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71948">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0471fa6ac.mp4?token=SKolgHdKNnYmfvNhjk6ZRPP5OPPjZNTxhZopeuooi2EB81-cq2b_ezMUtl1i9oXiuZEKBOf_nGP7_eHWtPeo1uCQObm_CAs-j6VS0hn11NyYcArovr-wpnhEMmdMyzJDLF77aEjmoCXYfGaQAnpl6PFP-WvL1HosMFgn4Alk8S65PguTy8-HCPT6ER_UEvACLlM5FLHTr9TNqX9QHGiXfLV7I-FtQbBqAWWB7We1dCQJYl6WQF9FAPR2qPjd-HfnUEtNWNpOUBC339stOxpW887by4lsxmy721rraWimbotfcCEgfEuaioCxSooRb8BlJrtM7sWUrqDA9foxd7gD8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0471fa6ac.mp4?token=SKolgHdKNnYmfvNhjk6ZRPP5OPPjZNTxhZopeuooi2EB81-cq2b_ezMUtl1i9oXiuZEKBOf_nGP7_eHWtPeo1uCQObm_CAs-j6VS0hn11NyYcArovr-wpnhEMmdMyzJDLF77aEjmoCXYfGaQAnpl6PFP-WvL1HosMFgn4Alk8S65PguTy8-HCPT6ER_UEvACLlM5FLHTr9TNqX9QHGiXfLV7I-FtQbBqAWWB7We1dCQJYl6WQF9FAPR2qPjd-HfnUEtNWNpOUBC339stOxpW887by4lsxmy721rraWimbotfcCEgfEuaioCxSooRb8BlJrtM7sWUrqDA9foxd7gD8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس نیوز به نقل از ترامپ:
ترامپ می‌گوید «احتمالاً» برای دیدار با مسعود پزشکیان، رئیس‌جمهور ایران، در حاشیه مجمع عمومی سازمان ملل آمادگی دارد
😂
پزشکیان هفته آینده در نیویورک خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/71948" target="_blank">📅 17:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71947">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6e65f0569.mp4?token=pITFxTs2aGCbyhCbLh9x3XovmVvNg7dKuiDQsKgsnKc1bpQllL2UR71IDcGt9Qdt7W9EotI8rtKbdKNHAnmCF_ap7SBeB0cvIfieJeDwdRntydKsz83sa-QowA4SwP_soGo-ILCingEJex6TVJUk-1Yvq6_Um96vomdKKg7J561UUkUcuWevrjvz813bss4YQznaOVT8g6dEO5zE_RhPytyjZVa7nE9AIoUxZi8ImgtN_5IL8690Ya13ceCVEMY7NpeV1ZNt7KEePDNI0intHN-ef-ALDhyazXrN6eWgkShKMrvRQTHTOLMru4991YF_vKGBhrhlRh6oPCYqJGFA-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6e65f0569.mp4?token=pITFxTs2aGCbyhCbLh9x3XovmVvNg7dKuiDQsKgsnKc1bpQllL2UR71IDcGt9Qdt7W9EotI8rtKbdKNHAnmCF_ap7SBeB0cvIfieJeDwdRntydKsz83sa-QowA4SwP_soGo-ILCingEJex6TVJUk-1Yvq6_Um96vomdKKg7J561UUkUcuWevrjvz813bss4YQznaOVT8g6dEO5zE_RhPytyjZVa7nE9AIoUxZi8ImgtN_5IL8690Ya13ceCVEMY7NpeV1ZNt7KEePDNI0intHN-ef-ALDhyazXrN6eWgkShKMrvRQTHTOLMru4991YF_vKGBhrhlRh6oPCYqJGFA-YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
در «مرحله تصمیم‌گیری» هستم و در آینده‌ای نه چندان دور، اتفاقات بسیار بزرگی رخ خواهد داد.
گزینه‌ها عبارتند از: نابودی کامل ایران، رها کردن آن‌ها تا از نظر اقتصادی بپوسند، یا دستیابی به توافق.
بهتر است درست رفتار کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/71947" target="_blank">📅 17:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71946">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3687d7bcf.mp4?token=qLwIUsvPymQIVqMeP77A6QHMzKO58kVdmdwVwAvEahWmLK8lnRmXrs2Iag0dRqMu4WL1ZCDTSDxo4djuK38M53Ng6tH57ZuviurvpHDX5NMHgSHeGh4me7y4h_USnboY1IEfPTfANKoY9xbSMxT-R91N_EUHC-AfeeG6SzG1Yl04RARp2pUzyTS00O1L4yCmODxYdrO45Ij6OHO9ViG2MkXymIUwi-GlY7imYhY4Bg44MXHzPKAR22mKJWs1jrklGN8TLcjMYSoxDZx5V01HFTn2jjFrtNXt3RAHt2mwClojxNug7oHH2wYvwfFQ86AerB5nGUpX1A5GOfmgGi5OJTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3687d7bcf.mp4?token=qLwIUsvPymQIVqMeP77A6QHMzKO58kVdmdwVwAvEahWmLK8lnRmXrs2Iag0dRqMu4WL1ZCDTSDxo4djuK38M53Ng6tH57ZuviurvpHDX5NMHgSHeGh4me7y4h_USnboY1IEfPTfANKoY9xbSMxT-R91N_EUHC-AfeeG6SzG1Yl04RARp2pUzyTS00O1L4yCmODxYdrO45Ij6OHO9ViG2MkXymIUwi-GlY7imYhY4Bg44MXHzPKAR22mKJWs1jrklGN8TLcjMYSoxDZx5V01HFTn2jjFrtNXt3RAHt2mwClojxNug7oHH2wYvwfFQ86AerB5nGUpX1A5GOfmgGi5OJTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهراب قاسم‌خانی نویسنده سریال پاورچین :
تو سریال یه اصطلاحی بین مهران مدیری و سحر زکریا ( نقش زن و شوهر ) بود که درباره " کوه رفتن " به هم میگفتن؛
مثلا زکریا به مدیری میگفت بیا بریم کوه، یا میگفت تو اوایل ازدواجمون بیشتر میومدی کوه،
ولی اصلا موضوع کوه نبود و داشتن درباره رابطه‌شون صحبت میکردن.
بعد از 5,6 قسمت مسئولان صداوسیما متوجه شدن و دیگه اجازه ندادن این دیالوگ تو سریال رد و بدل بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/71946" target="_blank">📅 17:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71945">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/152e7c05de.mp4?token=vgyGv5E_b3phTBtrCHAhylLzJB3w2icZgiaCzMArL8bbrJM4n77TyXSpbSr9eWlJG3We3lvgwQFUQcA-vtIh52JYh9N2LDVM0J_Rm_zgvjKZFOGzifyxz0YdpbzTXWKie83APdtno11hvDE8xFoEkrxsw-VLyiddD2yQjVWGzn90F0s9n8E0_prPNdIPARZ1PXzK7RqLxzuu0FJvRu45i7-qD_WEF5sGpjGf0zfIRCUhfwtGHzSaciThbcHUH379AuQSnID56Dm-6UMB-6y7lvXyJSIMzIE9mAYh9nNRGBbc9Ip82wFqlibqPZvSAkY1icGj-mhzJyeG4s5C60H4H4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/152e7c05de.mp4?token=vgyGv5E_b3phTBtrCHAhylLzJB3w2icZgiaCzMArL8bbrJM4n77TyXSpbSr9eWlJG3We3lvgwQFUQcA-vtIh52JYh9N2LDVM0J_Rm_zgvjKZFOGzifyxz0YdpbzTXWKie83APdtno11hvDE8xFoEkrxsw-VLyiddD2yQjVWGzn90F0s9n8E0_prPNdIPARZ1PXzK7RqLxzuu0FJvRu45i7-qD_WEF5sGpjGf0zfIRCUhfwtGHzSaciThbcHUH379AuQSnID56Dm-6UMB-6y7lvXyJSIMzIE9mAYh9nNRGBbc9Ip82wFqlibqPZvSAkY1icGj-mhzJyeG4s5C60H4H4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی :
100 میلیون بشکه نفت تو مملکت گم شده !
کسی که مسئول نظارت رو این موارد بود بهم گفته که 100 میلیون بشکه نفت رو نمیدونیم چی شده. نه تو دریا ریخته شده، نه امریکا تحریمش کرده و نه دزدای دریایی دزدیدنش.
به نیروی مسلح، قرارگاه فلان‌جا، نیروی انتظامی و ستاد کل چه ربطی داره که همشون دارن نفت میفروشن؟
اطلاعاتی نباید نفت بفروشه؛
اطلاعاتی سواد و فهمش رو نداره، درک نمیکنه. اطلاعاتی‌ای که 50 میلیون حقوق میگیره، میلیارد دلار، ترانزکشن، بیمه، حمل و نقل و این چیزها رو نمیفهمه.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/71945" target="_blank">📅 16:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71944">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1367899db.mp4?token=ZCWXrDVBOtwqQtsLOGhvLNjF7PRW9993APlb7hJDlEOyGoC3KPCqEX_Rj1NMC9EC5mevckeQG0aERwJV7bUy9lUaql5eb4ZUg0nuHayQH5y8juoyhxFXag8jIks9UWmmTQliJ05gHjW3TfDpC_vn7GtJbI_LhvhFNZMHx2IuuhlY2xHu8daDgGusHNz4K30lohvmp7LmvrkE0luIuNe65qWIE-Z-Q3QPXKIHXGCUqVE9Q94BRigXAJSoML-FP402igLATrB5PiPGrSGIRi872Cn_-usu-aeNjZXDuFDYSnxlTdixNpEqm_XOdLsMJ0WsvJARzrHb1Kdflz0GH59Z_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1367899db.mp4?token=ZCWXrDVBOtwqQtsLOGhvLNjF7PRW9993APlb7hJDlEOyGoC3KPCqEX_Rj1NMC9EC5mevckeQG0aERwJV7bUy9lUaql5eb4ZUg0nuHayQH5y8juoyhxFXag8jIks9UWmmTQliJ05gHjW3TfDpC_vn7GtJbI_LhvhFNZMHx2IuuhlY2xHu8daDgGusHNz4K30lohvmp7LmvrkE0luIuNe65qWIE-Z-Q3QPXKIHXGCUqVE9Q94BRigXAJSoML-FP402igLATrB5PiPGrSGIRi872Cn_-usu-aeNjZXDuFDYSnxlTdixNpEqm_XOdLsMJ0WsvJARzrHb1Kdflz0GH59Z_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساجده سلیمانی، مجری شبکه یک:
آقای جبلی میگن ۷۰ درصد مردم صداوسیما رو دنبال میکنن
والا من ۵ سال تو شبکه یک مجری بودم وقتی میرفتم بیرون جز یه مشت پیرمرد و پیرزن که صبح برای نماز بلند میشدن و تلویزیون میدیدن دیگه کسی منو نمیشناخت.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/71944" target="_blank">📅 16:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71941">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc55859ee.mp4?token=LDCLqHK6YbTvv78GLfhl7khkWrX2mzMxIcu-Yf5DT5T22mr0Vc5OVBbbBqw-zf71vKxw5sHYFP39hdAu71sIXQytI3UK-mNMMdqWeo7Ywk2xgYjvf7IT-g1UnyyBb07wavDNnqdqhHCcp_AFxPQXSNfkOLAcqdUu-MXmCz4BeItMgn2rPveLMzmpuE9o4AumpY1zleu6Fnl5U-JwQ7BOd2kdexHHr8BPRvTNTdqn7jRNYNzX8k7411j970CCWgWx3nrfq8qx0_W8i9lI0awnyp26ldUq6qmiWDnkkas14wVvZ_6AGA0hQOigdF2oHn6wdLTvfMZ3BVhiQi1CbhQUUQMWlUfDvbdQOIAwbOdL8pe7sNXp72VF9W0TfVZrBTwu1U5sHHxLHkBnxM6qnxmc74scDsS_2M0iYFxsH_4_q9jIBQBRHCO-B_y8mlyUkJvDxEOrpGJBDn3IXrql1Kq_MTdZfAq750Cbm8NHlYV_thsb3pr49O59FlR9estBM2d1rev9z9kLwWYZQgzJfpgEKGRvqxFGSTmHSFV5xx1Gh6AmSCJ8Nc0TDa5ebbviRQI-9LJ85L6Ruggu07m_EUZVBvUeLeft3SILHlh7Q6o_A2RoLARh5ti24vWHEyqT0-rSHUdng0iNAbfRqvFoa5Ab9dxikQQin_mL_VD9cxkaaXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc55859ee.mp4?token=LDCLqHK6YbTvv78GLfhl7khkWrX2mzMxIcu-Yf5DT5T22mr0Vc5OVBbbBqw-zf71vKxw5sHYFP39hdAu71sIXQytI3UK-mNMMdqWeo7Ywk2xgYjvf7IT-g1UnyyBb07wavDNnqdqhHCcp_AFxPQXSNfkOLAcqdUu-MXmCz4BeItMgn2rPveLMzmpuE9o4AumpY1zleu6Fnl5U-JwQ7BOd2kdexHHr8BPRvTNTdqn7jRNYNzX8k7411j970CCWgWx3nrfq8qx0_W8i9lI0awnyp26ldUq6qmiWDnkkas14wVvZ_6AGA0hQOigdF2oHn6wdLTvfMZ3BVhiQi1CbhQUUQMWlUfDvbdQOIAwbOdL8pe7sNXp72VF9W0TfVZrBTwu1U5sHHxLHkBnxM6qnxmc74scDsS_2M0iYFxsH_4_q9jIBQBRHCO-B_y8mlyUkJvDxEOrpGJBDn3IXrql1Kq_MTdZfAq750Cbm8NHlYV_thsb3pr49O59FlR9estBM2d1rev9z9kLwWYZQgzJfpgEKGRvqxFGSTmHSFV5xx1Gh6AmSCJ8Nc0TDa5ebbviRQI-9LJ85L6Ruggu07m_EUZVBvUeLeft3SILHlh7Q6o_A2RoLARh5ti24vWHEyqT0-rSHUdng0iNAbfRqvFoa5Ab9dxikQQin_mL_VD9cxkaaXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حمله گسترده پهپادی اوکراین به پالایشگاه کاپوتنیا در مسکو، روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/71941" target="_blank">📅 15:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71940">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8ac28a42.mp4?token=JXYMiOm_hz9pYwvKfZWzrGv6TRstQd9h30iZh1zdr_a8BPV7KiDfCq3SmBNRiuVC3YHjpYY6QiWovXG6NtHgn6aE_f2kwh2ME5BgATT2gb6ExfmrTJuLFhJJXlxcYpG2irCO2ha6eq4-tAljRB1DTWbHN-InC3HC4IgfotTfH8HPA1NCuqaXc62pv7FOfejHJnA8CuehAz7m9srM56jXL0PgQCDqnVfAhHJDdQ7ij1U8g8qMqTo_un4VqwzpSTB41dZjyuhbBKhoqwsz9M28lZjKKQqLCymqwFHM-2rPKlrUK9m8_0dePuYOU-aJBRQ1glBdqOQTUaq4VDW_h0Et2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8ac28a42.mp4?token=JXYMiOm_hz9pYwvKfZWzrGv6TRstQd9h30iZh1zdr_a8BPV7KiDfCq3SmBNRiuVC3YHjpYY6QiWovXG6NtHgn6aE_f2kwh2ME5BgATT2gb6ExfmrTJuLFhJJXlxcYpG2irCO2ha6eq4-tAljRB1DTWbHN-InC3HC4IgfotTfH8HPA1NCuqaXc62pv7FOfejHJnA8CuehAz7m9srM56jXL0PgQCDqnVfAhHJDdQ7ij1U8g8qMqTo_un4VqwzpSTB41dZjyuhbBKhoqwsz9M28lZjKKQqLCymqwFHM-2rPKlrUK9m8_0dePuYOU-aJBRQ1glBdqOQTUaq4VDW_h0Et2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میانگین آی‌کیو یمنی‌ها:
یه حوثی پین نارنجک رو کشید واسه اینکه نشون بده خدا باهاشه و نتیجه شد این.
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/71940" target="_blank">📅 15:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71939">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">قرارگاه خاتم الانبیا:
هرگونه حمله به ایران، منجر به حملات «مداوم، مؤثر و دردناک» به تمامی پایگاه‌ها و منافع آمریکا در منطقه، «بدون هیچ‌گونه محدودیتی» خواهد شد.
کشورهای منطقه‌ای که با تجاوز آمریکا همراهی کنند، شریک این حمله محسوب شده و نباید انتظار خویشتن‌داری ایران را داشته باشند.
بر اساس اطلاعات دریافتی آمریکا با چراغ سبز متحدان منطقه‌ای خود و بر اساس هماهنگی‌های صورت‌گرفته در یک نشست اروپایی، در حال برنامه‌ریزی اقداماتی جدید علیه ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71939" target="_blank">📅 14:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71938">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abf3ef96ed.mp4?token=UR34cLh5fPhQzzifOsqwpXF8OVGuFIXaH2Q5fg18a6sfVDdPFYcrZnyLfq0FYQtOhatA6UN2I3K7z0UPexCKmd4svkwdYFIxCKljl5hfovPPQDGr9gbSIMEuj0fwS-GHaYkUyXvZ0dcUu05brnPRQEuJDXQrQhdmnYkyf7vvg9lL6-1fbSTG5v90xce2DqGQlMuPRCdkQPSGVWRE2nkp2EuwvOafrXK6VsGEBIIf3DVfAsfu2aotaih2MYoVyeHzYI3QeRyBEhlbgh73bYC7U4gdmGEDXIq7kuUOPSr0PthA-wVitkNlvmSi_o_aLP-Dn8PzdWI6deYCVvmFBCWZmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abf3ef96ed.mp4?token=UR34cLh5fPhQzzifOsqwpXF8OVGuFIXaH2Q5fg18a6sfVDdPFYcrZnyLfq0FYQtOhatA6UN2I3K7z0UPexCKmd4svkwdYFIxCKljl5hfovPPQDGr9gbSIMEuj0fwS-GHaYkUyXvZ0dcUu05brnPRQEuJDXQrQhdmnYkyf7vvg9lL6-1fbSTG5v90xce2DqGQlMuPRCdkQPSGVWRE2nkp2EuwvOafrXK6VsGEBIIf3DVfAsfu2aotaih2MYoVyeHzYI3QeRyBEhlbgh73bYC7U4gdmGEDXIq7kuUOPSr0PthA-wVitkNlvmSi_o_aLP-Dn8PzdWI6deYCVvmFBCWZmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نجمه امینی، دانشجوی ۲۳ ساله و بازداشت شده در جریان انقلاب ملی در مشهد که او را محکوم به اعدام کرده‌اند، در تماسی تلفنی از زندان وکیل‌آباد مشهد از همه مردم خواست تا صدای او باشند.
درود به مردم عزیز ایران، حکم اعدام من صادر شده، لطفا صدای من باشین، من یه جوونم با کلی آرزو.
تروخدا فقط صدای منو نشنوین، اونو نشر بدین و صدای من باشین، من بی گناهم.
شاید این آخرین صدایی باشه که از من میشنوین چون شاید دیگه نتونم حرف بزنم، ولی تنها امیدم ایران آباد و آزاده.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71938" target="_blank">📅 13:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71937">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4daecc7856.mp4?token=KE8Lsk5-ukOvTllLwKubW1OZayzc--2lXiFZfhKyk6i1wr5DirpkOT0bZYEVPbjkOrwNTbata4iWU2rv95fwtrrXLGKwTYuVoidNf4Qr51OwYQeQz4uoDQ9AZgtBQ1y_pfkiglkHjWWFv86rapmqQTLB5Z85vQ42sdpVtK93-eZG5AOT1-6K_lb2S_bhBwTb0xYVffLCtR3UpmdT4OlvhEXuy9M13pqHkeSVS1aYe5XpW3c_1HvwWWhNdYUs4kJQLvsIA8fnexzzeBtg82fAiSAc3iX1aT8AhYqCU09YZ9TivapgIvCH3skFBJSJUWMCrxEeGw4QmbfO7yMssQSFug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4daecc7856.mp4?token=KE8Lsk5-ukOvTllLwKubW1OZayzc--2lXiFZfhKyk6i1wr5DirpkOT0bZYEVPbjkOrwNTbata4iWU2rv95fwtrrXLGKwTYuVoidNf4Qr51OwYQeQz4uoDQ9AZgtBQ1y_pfkiglkHjWWFv86rapmqQTLB5Z85vQ42sdpVtK93-eZG5AOT1-6K_lb2S_bhBwTb0xYVffLCtR3UpmdT4OlvhEXuy9M13pqHkeSVS1aYe5XpW3c_1HvwWWhNdYUs4kJQLvsIA8fnexzzeBtg82fAiSAc3iX1aT8AhYqCU09YZ9TivapgIvCH3skFBJSJUWMCrxEeGw4QmbfO7yMssQSFug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
اسرائیلی‌ها تونل‌های خالی در لبنان را برای اهداف تبلیغاتی و نمایش انتخاباتی منفجر کردند. آن‌ها عکس و فیلم گرفتند و گفتند: «ببینید نتانیاهو چقدر قدرتمند است.»
همه این‌ها تبلیغات است و همگی به انتخابات مربوط می‌شود.
اما کار ما مبتنی بر اصول است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/71937" target="_blank">📅 12:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71936">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ea49a57b9.mp4?token=k9Do49Ijhk0--B1-RUriYBDnAjkaDJAdvUzTB_ejW-d5VU66veCD5AfZ6y0RymZAKvW_F7-cV0F-6GGtkhleLvVvyrR5If24oG8Bkbhplim9L7PRlhfA7WI30vdPkJd0-4Wj2Txv2JyBnMnxvEYoEckVVz-J23q0H8KUGjbLjV-GuU2lY_fOvoccO_ESjAE4vDlG927qnLxZUTGTPMhxnA0r_Uut2Biiof1B2mSHXAWF9RORnyG50osQTgU6XGzfyeWw7meY-43f3zvh-8v-VGq7lqn7wU0_SIct0dk5hSK_Wyz4vW06uQVsvwXPoLlws-clSOrjPTQDRYtVx3479g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ea49a57b9.mp4?token=k9Do49Ijhk0--B1-RUriYBDnAjkaDJAdvUzTB_ejW-d5VU66veCD5AfZ6y0RymZAKvW_F7-cV0F-6GGtkhleLvVvyrR5If24oG8Bkbhplim9L7PRlhfA7WI30vdPkJd0-4Wj2Txv2JyBnMnxvEYoEckVVz-J23q0H8KUGjbLjV-GuU2lY_fOvoccO_ESjAE4vDlG927qnLxZUTGTPMhxnA0r_Uut2Biiof1B2mSHXAWF9RORnyG50osQTgU6XGzfyeWw7meY-43f3zvh-8v-VGq7lqn7wU0_SIct0dk5hSK_Wyz4vW06uQVsvwXPoLlws-clSOrjPTQDRYtVx3479g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضایی:
پرسش من از مقامات عرب این است: اگر ایران مقاومت نمی‌کرد و ناچار به تسلیم می‌شد، آیا اسرائیل امروز به عربستان سعودی حمله نمی‌کرد؟ آیا اسرائیل تا دمشق پیشروی نمی‌کرد؟ آیا اسرائیل به عراق حمله نمی‌کرد؟
ما در اینجا شهید دادیم و از کشورهای عربی دفاع کردیم. اگر بینی آمریکا و اسرائیل را در اینجا، در ایران، به خاک نمی‌مالیدیم و اگر آن‌ها در ایران احساس پیروزی می‌کردند، دیگر کسی در منطقه باقی نمی‌ماند که بتواند در برابرشان بایستد.
اسرائیل به تمام کشورهای عربی حمله می‌کرد و آمریکا نیز از آن حمایت می‌نمود. ما مقاومت کردیم — بله، ما از کشور خودمان دفاع کردیم — اما دفاع ما به نفع کشورهای عربی نیز تمام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/71936" target="_blank">📅 12:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71935">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c2df1caeb.mp4?token=tSUb_Cnmc-mreUU3jBoSvbdh2RvHgXT6zBUJ8tUrgcwJje4bnNzJ6GzhaSQAIP4N1_9bx2cDd-yGs6WeVNe6oBT1KdBNTT5gOsDWkcRUOjt1_OZ7wCNwihlvDTXxd-bSKkMob5dtezPphawAihKu6IpvjmVoOQnexnNI3oVtqRG1JhiIpLbErpqTsxp4__vxmCa-aVon4bbFjf43am1DqlLc8iSLB1yjU8SQKrKrxRXzitGos03_mqatrwq-1KB1wXSfMKC1rQGlJZmXW8nR979IwGYq2q2WG3Bhz5RCG9Jvf-rm0YBlym0C3v4Yr2bEUsAtOlMkcKDnMmof-4N7eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c2df1caeb.mp4?token=tSUb_Cnmc-mreUU3jBoSvbdh2RvHgXT6zBUJ8tUrgcwJje4bnNzJ6GzhaSQAIP4N1_9bx2cDd-yGs6WeVNe6oBT1KdBNTT5gOsDWkcRUOjt1_OZ7wCNwihlvDTXxd-bSKkMob5dtezPphawAihKu6IpvjmVoOQnexnNI3oVtqRG1JhiIpLbErpqTsxp4__vxmCa-aVon4bbFjf43am1DqlLc8iSLB1yjU8SQKrKrxRXzitGos03_mqatrwq-1KB1wXSfMKC1rQGlJZmXW8nR979IwGYq2q2WG3Bhz5RCG9Jvf-rm0YBlym0C3v4Yr2bEUsAtOlMkcKDnMmof-4N7eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
آمریکا و ترامپ خواهند رفت. همه می‌دانند که اقتصاد آمریکا در واقعیت، در مسیر فروپاشی قرار دارد. آمریکا طی ۱۰ سال آینده، دیگر آن کشوری نخواهد بود که امروز هست.
اما ما و کشورهای عربی باقی خواهیم ماند. ما خودمان باید وضعیت منطقه را سامان دهیم. ما باید امنیت خلیج فارس را برقرار کنیم، پیمانی برای همکاری اقتصادی شکل دهیم و در منطقه با یکدیگر دوست باشیم.
ما یک خانواده هستیم؛ خانواده خلیج فارس. ما هشت کشوریم و باید بر بازسازی و توسعه اقتصادی تمرکز کنیم، با یکدیگر همکاری داشته باشیم، در سرمایه‌گذاری‌های هم مشارکت کنیم و حتی به سمت ایجاد واحد پولی مشترک و بازار مشترک واحد حرکت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/71935" target="_blank">📅 12:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71934">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed047a6e6.mp4?token=Bt0sTAuViGrihMm0mZJrSAA8Hhq7Yf3M4Ouq4QEFnyG8Ocgxa-eKN0EfnZ9phH5cWHXYyacU0npdzQTvQ4dvFxpisN3GUhHtw54aZRlZ3HWK9ffdQjmhTP3oVr8Z9if7pjU5EZOBQkJR0xFTgwQunmtiGs-IIzkwrzefp7mFDlXRlarM0A0IO-sGg57fsEuFbwZUCXCMcYuKDeVaO1zqjah-EoIlg1bLaQ-MU_2RTugfs0-or4OqFKZzsi0BrE9L0IzNFLS1DYnHR_NUzV9GiIYSz6_970LsVckXOANBbSSBjRvtft5qekZ_NdQAjjrfq8X040OnPGub-K8iwls1XE0u2YYdST_CytxCnCyhR1M5hUjAcsShNYOhFcG-4vRAdlRYm7iflafBKAeU_KthDdZ5HPouNJ5aHI9fTRF1wsqT6wXFGEy1gJGngYVnWK0tflILpuuuqbsxnGo3B-8mFri9gVVN-D66HEW9bSoUHBD-_OKwr-SsNwRjZCbYh_R9UvPkCG1ZuFUP24eAMK-4hlLr2tSpo11kC2yaHTChm2ts_yp2yptLEgDNFm-LsRWYFgnaOJFuS0KnmmAO1BZdASsVRh0Nx4Vk2CHXK_U3QwYBS4MCLBRz0B6StkcYUJyc9N0OXHZe1FixxmheseiZ-dg8LUFOFhxh643hn6DqoRs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed047a6e6.mp4?token=Bt0sTAuViGrihMm0mZJrSAA8Hhq7Yf3M4Ouq4QEFnyG8Ocgxa-eKN0EfnZ9phH5cWHXYyacU0npdzQTvQ4dvFxpisN3GUhHtw54aZRlZ3HWK9ffdQjmhTP3oVr8Z9if7pjU5EZOBQkJR0xFTgwQunmtiGs-IIzkwrzefp7mFDlXRlarM0A0IO-sGg57fsEuFbwZUCXCMcYuKDeVaO1zqjah-EoIlg1bLaQ-MU_2RTugfs0-or4OqFKZzsi0BrE9L0IzNFLS1DYnHR_NUzV9GiIYSz6_970LsVckXOANBbSSBjRvtft5qekZ_NdQAjjrfq8X040OnPGub-K8iwls1XE0u2YYdST_CytxCnCyhR1M5hUjAcsShNYOhFcG-4vRAdlRYm7iflafBKAeU_KthDdZ5HPouNJ5aHI9fTRF1wsqT6wXFGEy1gJGngYVnWK0tflILpuuuqbsxnGo3B-8mFri9gVVN-D66HEW9bSoUHBD-_OKwr-SsNwRjZCbYh_R9UvPkCG1ZuFUP24eAMK-4hlLr2tSpo11kC2yaHTChm2ts_yp2yptLEgDNFm-LsRWYFgnaOJFuS0KnmmAO1BZdASsVRh0Nx4Vk2CHXK_U3QwYBS4MCLBRz0B6StkcYUJyc9N0OXHZe1FixxmheseiZ-dg8LUFOFhxh643hn6DqoRs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
اگر آمریکایی‌ها جدی هستند، بگذارند سربازانشان بیایند و وارد ایران شوند. چرا وارد نمی‌شوند؟
در جنگ‌ها، این نیروهای زمینی هستند که همیشه حرف آخر را می‌زنند.
چرا لشکر‌های هوابرد نمی‌آیند؟ چرا نیروهای زمینی آمریکا وارد ایران نمی‌شوند؟ چرا فقط از آسمان بمباران می‌کنند و سپس می‌روند؟
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/71934" target="_blank">📅 12:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71933">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4920ecc6.mp4?token=uYrDa-5ybL72c9vioz6KyQ4KLTxAYQkGgxFreX_Bqq6ViEogJ93ldzPPHhIn8MBiETFtn8_sR2zH5lF55IGOsiAr1W6qFiZvEkkERF9FuVGqG1Vqs0vUF4BoZt3pgfNZ05qI-Qxru82ZEH6Wn5UVpGQjPKwHMr-O9G0W2ps1UbRdlZjpKW7DXP6g-Q6vsxVxWZMYy0yFXOk06qOpOO5Fo3ryfJWD5PUfEmhtIy05Dmt9mNcThVTfEGoMIXB5-Jg0dEWJNWSkeT318YSEl9LmY2ANy99HCrLj9UTKiZquNgpNt0gAqJD7xn22KvwmYyqTEYwFojk8Dvft7SEmtaVp4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4920ecc6.mp4?token=uYrDa-5ybL72c9vioz6KyQ4KLTxAYQkGgxFreX_Bqq6ViEogJ93ldzPPHhIn8MBiETFtn8_sR2zH5lF55IGOsiAr1W6qFiZvEkkERF9FuVGqG1Vqs0vUF4BoZt3pgfNZ05qI-Qxru82ZEH6Wn5UVpGQjPKwHMr-O9G0W2ps1UbRdlZjpKW7DXP6g-Q6vsxVxWZMYy0yFXOk06qOpOO5Fo3ryfJWD5PUfEmhtIy05Dmt9mNcThVTfEGoMIXB5-Jg0dEWJNWSkeT318YSEl9LmY2ANy99HCrLj9UTKiZquNgpNt0gAqJD7xn22KvwmYyqTEYwFojk8Dvft7SEmtaVp4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی:
اگر جنگی دوباره آغاز شود، کشتی‌های آمریکا — مگر اینکه اقیانوس هند را ترک کنند — در هر کجای این اقیانوس که باشند، هدف حمله قرار خواهند گرفت. ما به این توانمندی‌ها دست یافته‌ایم.
ما سرعت موشک‌های هایپرسونیک (مافوق صوت) خود را از ۶ ماخ به ۱۰ ماخ افزایش داده‌ایم.
همچنین سامانه‌های جنگ الکترونیک خود را توسعه داده و پدافند هوایی‌مان را ارتقا بخشیده‌ایم؛ علاوه بر این، تدابیر دیگری نیز داریم که در زمان مناسب از آن‌ها استفاده خواهیم کرد.
بنابراین، ما کاملاً آماده‌ایم. اگر آمریکا جنگی را آغاز کند، با نیرویی بیشتر و ضرباتی پرتعدادتر و دردناک‌تر با آن مقابله خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/71933" target="_blank">📅 12:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71932">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71932" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/71932" target="_blank">📅 12:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71931">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GG9Y09ZIWgZWTZDNwETQgOvG6OrCdJMIeEK-IQWwqaRfkLuOC4UOXJzov11BwMJeLEvIgRyq2pFh9IpiIJki81vv13T_5KB3CGPR42GL-QuhueK9NHFdsNGExZxZR4fVVMszbTfDIfTQft4JOkYAhu0tt_N6Ek2-l5e05tXseHwO6xKFTY-iMLcJSmeqLAOPmwZiZt15G-o7wbZUi3gLY7x-pVf_7wf0bWnUUYv1TQwpn6MdY3sTpSU8qocXnF4qXSwUO-sZ2jgVU5gcZjABMAThNiOgSR4oOpgyagjp_fHKLwoOpaUXXKVd0c_Xcoj96bsl8DLJNNah3ZTFq20chQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
رویارویی غول‌های مادرید!
🦖
نبرد هیجان انگیز رئال مادرید
🆚
اتلتیکو مادرید را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ رویارویی اخیر دو تیم:
رئال مادرید: ۳ برد، ۲ شکست و ۹ گل زده
اتلتیکو مادرید: ۲ برد، ۳ شکست و ۱۰ کل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/71931" target="_blank">📅 12:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71930">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2e9358bf.mp4?token=q2VsNaz74pO7EKW7bwMJ8UX0jvT0bb6OgP_vNXgP-9uz2zAEEtBa0Hv7rI5NPRrjdnE7gz1w-_L-D0_UjkwUCSaZZ2-kkZaUqfuhmTzn5T3z4Y9VtWGmS3h78rO0aAu_2VT4DzcKaWYfQHw9BcNNDtSMUE-G8kF7wGgCe2DMmVxTc-n_5ku0ZBr9VFN3SXYO9pi2FmnHbg5LDNAJVHUGzkeqn1hldwMwm_am8UmORTITRrc7VLu6r5Mxioc9ADo7CryziQucp_PBFFXxuholqe2lptPaGYm_kR2T3rreXIOF8SCGv5v9hqGQXUaDg-ZhrNwPXFCnp-LwRYpUeyBj5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2e9358bf.mp4?token=q2VsNaz74pO7EKW7bwMJ8UX0jvT0bb6OgP_vNXgP-9uz2zAEEtBa0Hv7rI5NPRrjdnE7gz1w-_L-D0_UjkwUCSaZZ2-kkZaUqfuhmTzn5T3z4Y9VtWGmS3h78rO0aAu_2VT4DzcKaWYfQHw9BcNNDtSMUE-G8kF7wGgCe2DMmVxTc-n_5ku0ZBr9VFN3SXYO9pi2FmnHbg5LDNAJVHUGzkeqn1hldwMwm_am8UmORTITRrc7VLu6r5Mxioc9ADo7CryziQucp_PBFFXxuholqe2lptPaGYm_kR2T3rreXIOF8SCGv5v9hqGQXUaDg-ZhrNwPXFCnp-LwRYpUeyBj5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لیلی فلیپس پورن استار آمریکایی، موقع انجام کار‌ نیک راهی بیمارستان شد.
امروز در حین تلاش برای شکستن رکورد بیشترین تعداد سکس تو ۲۴ ساعت، دقایقی بعد از آغاز عملیات یکی از مردایی که باهاش رابطه داشت پاشید تو صورتش و بیناییش بشدت به مشکل خورد و راهی بیمارستان شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71930" target="_blank">📅 11:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71929">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/146935a692.mp4?token=A3lUX98AQxlYl-VyJ0FWt9FoVA8XDIIYy2Jtkkzv_FkvOU9NzoMoWcyJNzSosarsukTXbQr6g64Scr9vJHO_6DcxVJRnnWWqQBrbgLlcnWnRYrXQgjpm3iNUCIdXGnu2fJO5SM1cJ30ljZ0tAk95gb0J8MeWXmlv2XsDklRYh11m65-7wazJVtGA2csckl2DYGXnz-IQvVkMA446BoY1Ydm5lK9ngGYm8FJFa-YfINkoSkpfa0jaayjZU-7nNRt8SIcGcyhJN8UUR-ZC1ETuYRzCr848pTtVCMxtvVe4UIdf697YW73JulnO3Ms8liE-LYmPLr1yteDHO9zWs4oSsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/146935a692.mp4?token=A3lUX98AQxlYl-VyJ0FWt9FoVA8XDIIYy2Jtkkzv_FkvOU9NzoMoWcyJNzSosarsukTXbQr6g64Scr9vJHO_6DcxVJRnnWWqQBrbgLlcnWnRYrXQgjpm3iNUCIdXGnu2fJO5SM1cJ30ljZ0tAk95gb0J8MeWXmlv2XsDklRYh11m65-7wazJVtGA2csckl2DYGXnz-IQvVkMA446BoY1Ydm5lK9ngGYm8FJFa-YfINkoSkpfa0jaayjZU-7nNRt8SIcGcyhJN8UUR-ZC1ETuYRzCr848pTtVCMxtvVe4UIdf697YW73JulnO3Ms8liE-LYmPLr1yteDHO9zWs4oSsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوکراین شب گذشته یکی از بزرگترین حملات پهپادی خود را علیه مسکو انجام داد.
روسیه مدعی است که بیش از ۱۶۰۰ پهپاد، از جمله ۴۵۰ پهپادِ عازمِ مسکو، سرنگون شده‌اند.
این حملات به پالایشگاه نفت «کاپوتنیا» (بزرگترین پالایشگاه مسکو) و ساختمان‌های مسکونی اصابت کرد که منجر به کشته شدن دو نفر در منطقه مسکو و تخلیه ۴۰۰ نفر از ساکنان شد.
محدودیت‌های پروازی در فرودگاه‌های مسکو اعمال شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/71929" target="_blank">📅 11:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71926">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7f510c35.mp4?token=qYwHfe-b9bj4eIMLEtbJfQ3D9NXxdVOnh-bE-fqmBxBEBlgOKZYfVTmlfsm1De2M2xO5f9ngONF1ikGpFtPIJ1cwPGMNCl4mxedwRAgi3Py71eKCY4RuS_o50J1VxMzAXwADqznvPpwC4XEOpXXgXIdfQwbthHGge4ut_cCDibcPfy4eXkwP2uA5KDEGOM-hVwCoCr0ef2z95mkhT4R2Lvh9SqspMRUi41xTRcUEmk96RXLVLqT1dJtPCQZjvsoN-EHaAL5YUdm7_BCoIIFG3NV37ZOJ9eIWdR-tHEvDTa5ywQjBaH8eNXVDNka2hBqZwA00XtYCBquC3B48489Xrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7f510c35.mp4?token=qYwHfe-b9bj4eIMLEtbJfQ3D9NXxdVOnh-bE-fqmBxBEBlgOKZYfVTmlfsm1De2M2xO5f9ngONF1ikGpFtPIJ1cwPGMNCl4mxedwRAgi3Py71eKCY4RuS_o50J1VxMzAXwADqznvPpwC4XEOpXXgXIdfQwbthHGge4ut_cCDibcPfy4eXkwP2uA5KDEGOM-hVwCoCr0ef2z95mkhT4R2Lvh9SqspMRUi41xTRcUEmk96RXLVLqT1dJtPCQZjvsoN-EHaAL5YUdm7_BCoIIFG3NV37ZOJ9eIWdR-tHEvDTa5ywQjBaH8eNXVDNka2hBqZwA00XtYCBquC3B48489Xrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارت امور خارجه آمریکا با توجه به تحولات منطقه، هشداری امنیتی برای آمریکایی‌های ساکن خاورمیانه در خصوص احتمال بسته شدن حریم هوایی صادر کرده است.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71926" target="_blank">📅 10:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71925">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شاهزاده رضا پهلوی:
با توجه به شرایط جدید، تاکتیک‌ها و روش‌های اجرایی مخالفان جمهوری اسلامی تغییر کرده، اما هدف همچنان سرنگونی جمهوری اسلامی و دستیابی به ایرانی آزاد و آباد است.
«ما امروز با تجربه‌تر و مصمم‌تر از هر زمان دیگری هستیم. هدف ما مشخص است، سرنگونی جمهوری اسلامی و رسیدن به یک ایران آزاد و آباد.»
ایشان گفتند: «چهار اصل کلیدی ما مشخص است:
حفظ تمامیت ارضی ایران
جدایی دین از حکومت
آزادی‌های فردی و برابری همه شهروندان در قانون
حق ملت در مشخص کردن شکل آینده حاکمیت ایران از طریق صندوق رای آزاد و منصفانه
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71925" target="_blank">📅 09:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71924">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eacbff262.mp4?token=t7h1bIK-dhsyu-aIf4G8KLCT-_1cMP5VvJd19nkmzZtmLbwflCw0bf-2_Irxjnqi5iUT0q7Fs6AlKFRKiJ8j9sC_wDcACikdhzYUDVLq1IL_SKXOIVfMNSHrGKVK-l5fHdC4bOnwso7qNBAHkPKAB5c5HMvHa5F5LVymmJrxvpVmyBQfiPeAciLwq8whYbqbNZ5jvG6NWc7BBeEBBuYtEYyEKCfZe3Knf5LzD_haFNlw8flqwsLh2t67ebNlZXy6rucXxI3vPWhnm-nSux9XyaAcyTlDvgvPrTWKJx745U48qSOgOF_eG_Kmvic8rQ4F-M_YpeM8wySKCSjUr6TGjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eacbff262.mp4?token=t7h1bIK-dhsyu-aIf4G8KLCT-_1cMP5VvJd19nkmzZtmLbwflCw0bf-2_Irxjnqi5iUT0q7Fs6AlKFRKiJ8j9sC_wDcACikdhzYUDVLq1IL_SKXOIVfMNSHrGKVK-l5fHdC4bOnwso7qNBAHkPKAB5c5HMvHa5F5LVymmJrxvpVmyBQfiPeAciLwq8whYbqbNZ5jvG6NWc7BBeEBBuYtEYyEKCfZe3Knf5LzD_haFNlw8flqwsLh2t67ebNlZXy6rucXxI3vPWhnm-nSux9XyaAcyTlDvgvPrTWKJx745U48qSOgOF_eG_Kmvic8rQ4F-M_YpeM8wySKCSjUr6TGjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی:مجتبی مفقود است و اگر هم زنده باشد در تاریکی زیرزمین جرأت آن را ندارد که حتی صدایی از خود منتشر کند :))
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71924" target="_blank">📅 09:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71923">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d403914707.mp4?token=GljWs2qeT4vAj1HhxTmDgVCjCHDTrojhTBvN7EzS83LYuLbMPHE44DaDK4b-RQLkboNVCd-DGJS2HlHDcxOxHFbupxiRc0KDNS-POglX2EyQT4JRQB-742Cq_ewJp9Zg58ADSJFruIyDGOtqVwn7off_8TEgvMREQemIhAzMEp6GaBtlYCevozQnHrbDua_BaVNjVsqGUN-_TWpPKQ3MH8WUzYRP5OwBb7RNJZaZ_AWdqjRBY1WHZICIPh1K7SvKmdqCoBYCFrktjOHMwstAXwxT9tCnn4KEKpbzAsZYgQEMXvrZS-oTGP_IGFpGNMrZmN88idwllh9atVi5DWN4UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d403914707.mp4?token=GljWs2qeT4vAj1HhxTmDgVCjCHDTrojhTBvN7EzS83LYuLbMPHE44DaDK4b-RQLkboNVCd-DGJS2HlHDcxOxHFbupxiRc0KDNS-POglX2EyQT4JRQB-742Cq_ewJp9Zg58ADSJFruIyDGOtqVwn7off_8TEgvMREQemIhAzMEp6GaBtlYCevozQnHrbDua_BaVNjVsqGUN-_TWpPKQ3MH8WUzYRP5OwBb7RNJZaZ_AWdqjRBY1WHZICIPh1K7SvKmdqCoBYCFrktjOHMwstAXwxT9tCnn4KEKpbzAsZYgQEMXvrZS-oTGP_IGFpGNMrZmN88idwllh9atVi5DWN4UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده‌ رضا پهلوی:
«امروز این (جاویدشاه) یک شعار است .
یک شعار پشتیبانی و من از صمیم قلب سپاس گزارم.
کاری بکنیم که اون روزی که صندوق رای در تهران برقرار شد تبدیل  به رای بشه , نه یک شعار .»
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71923" target="_blank">📅 09:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71922">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71922" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71922" target="_blank">📅 01:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71921">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHeS3P_wRgrCaWBEqZMoacZntZmjFBK9zr59sBicYbXC8tGUlFeE-u-S1Nl_6lppCyOxRPR90W1SpcksIg6laQrx5aQVmkRIAZ5xmV-KLBY54JfPX7Yn_AzsU3JnpS8hli7PohHcVQ-R_fXCRJZ5xwTXGegObcgKyou4NC-8SiYLDAL12iB8t-kntEVgDKdzss-x0DLWFzngyTGkf2SyRL1dzrfZqHOfx9BT_b2yYyl4uKbGE0BoC-7SvZ4V7MCnNLh-oc50u1sH8kEecjaZySJ_jUoZRvKV-qkFTIzSNZRTpvjE7js4sEkGaTpxlcR71sxTdnM-qkX3UMVJ7YN4Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه‌ای و تجربه‌ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71921" target="_blank">📅 01:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71920">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gigVU7XLXJHztD72M6wF91JNHRgKrArmlCZALXaSKQa7XHwMPJbVkqTLNfs0H2PTMv_gaUKt_0eBrNVXhjcaO6FEz3WSnx4msXsLntB9_pPtddjDFCGugWnhJrrWHB9XF75cq26VbAwuHHDNWvo6Ytm5im9-J7mkBt68c2BiaYquMCwaEgmFn6iouiieMpAxPQg9A46zUEmPyYFtnGTHGwiet_CNT725ZstHT9WTfVGiym3F9CrJswUA_z2HsUQPHzzd174ff_E6NZgZcb3V_vg-CMchA48e1zuBIyqBcq2RpNhyH9Ojo6Y6C_QlRfZSPHpHtXNTVBwUZHir_O28uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه آمریکا با توجه به تحولات منطقه، هشداری امنیتی برای آمریکایی‌های ساکن خاورمیانه در خصوص احتمال بسته شدن حریم هوایی صادر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71920" target="_blank">📅 01:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71919">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">هشدار جدید آمریکا برای شهروندانش در خاورمیانه:
بر اساس آخرین اطلاعات منتشرشده، عربستان سعودی، بحرین، کویت و قطر در سطح «۳؛ تجدیدنظر در سفر» قرار دارند.
آمریکا در مورد عربستان نسبت به خطر حملات پهپادی و موشکی، درگیری مسلحانه و تهدیدهای تروریستی هشدار داده است.
در بحرین نیز آمریکا به تهدید حملات پهپادی و موشکی و اختلال در پروازهای تجاری اشاره کرده و سفر به این کشور را در سطح «تجدیدنظر در سفر» قرار داده است.
هشدار آمریکا درباره کویت نیز همچنان در سطح ۳ قرار دارد و از تهدید درگیری مسلحانه و حملات پهپادی و موشکی به‌عنوان عوامل اصلی این هشدار نام برده شده است.
در قطر نیز وزارت خارجه آمریکا نسبت به تهدید ناشی از درگیری مسلحانه، اختلال در پروازها و خطرات مرتبط با وضعیت امنیتی منطقه هشدار داده و از شهروندان خود خواسته برای احتمال تشدید شرایط آماده باشند.
در همین حال، لبنان در سطح بالاتری از هشدار قرار دارد و وزارت خارجه آمریکا از شهروندانش خواسته به لبنان سفر نکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71919" target="_blank">📅 01:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71915">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PbpnHCJgInShYfewehV62I_DfkYr5P9N5kG0zG-JaD5GmtbwfvMzxKkuTZvX_vgrvhmCFPMWHjR1jqXtBrPhvw0vsvApX4POmH4Rl0ToZq-8wEF_fvji_2HpTIJisdE6p8Qs-aSU5TmmYik5xb9zVUf-OjV4Lxx968vBGt46Nc_szVeUfojuE9JrMnSJlzKGZXvRQGphkNtp3g6SIlYg6DGqQQlhq_Tde-MzjPpg_Dfw9AsjJv0_feGTw6v2gtJI7ZZ0MLt56f2xpBf9jggRZnH3ghSyP3oxef6ILhTzRpvAJyGTaMQbHdEl5dCKgDM1zZQuaMwFDDZqWSKlAvxlPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7ac25f2861.mp4?token=Fh7iGM197WUTJ2N_Jp_mehW5IPJv0hPHajmf90cLdSBbGlCMxcjNpkbk8GfsNqZhApHQjOqo7KCuP1YLJRbnuWI2i_4O_BF1_x2yyI0x6fjWqfEwOuG2eP1pfYWD7LXb6o_4zpXeLdEvD0qp0b0SwjX_SIv4v78nMO9zgZv2i4xqRFXins0zx5utxXIwpx-Bn0dX9Yv77Xd2Z1II5vGJ88EHCirhmyJC8spRhoPkHvq-wne41ggb5smiuIJeQs5CSHelcSNR4-HXRUMLxDpQyrghSqTOIl8BUapqdfb1i7FqFzGZymB5RWMbRLP8-XazB1EY0ivxMDb80tY9BYnDYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7ac25f2861.mp4?token=Fh7iGM197WUTJ2N_Jp_mehW5IPJv0hPHajmf90cLdSBbGlCMxcjNpkbk8GfsNqZhApHQjOqo7KCuP1YLJRbnuWI2i_4O_BF1_x2yyI0x6fjWqfEwOuG2eP1pfYWD7LXb6o_4zpXeLdEvD0qp0b0SwjX_SIv4v78nMO9zgZv2i4xqRFXins0zx5utxXIwpx-Bn0dX9Yv77Xd2Z1II5vGJ88EHCirhmyJC8spRhoPkHvq-wne41ggb5smiuIJeQs5CSHelcSNR4-HXRUMLxDpQyrghSqTOIl8BUapqdfb1i7FqFzGZymB5RWMbRLP8-XazB1EY0ivxMDb80tY9BYnDYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور شاهزاده رضا پهلوی در مراسم بزرگداشت کوروش بزرگ در تورنتو کانادا و استقبال فوق‌العاده مردم از ایشان.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71915" target="_blank">📅 01:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71914">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5YYOrQmrXqLGnAgBu7YGSBD0Qpdk52zeQES0Uwanrpocv1Ubc4kz3tJX8_uAEjrZw0T25z4AkJPNdCqj8g457U0opCINPFsUyPbVCAcO5f87plnPtdneEwVw7Lwo5u9nb4sCAIzgQLFDJ4DXpPyfRrrTJWVaXf31-H0X6Mo9Sk9FIQquBKgNjViEmYNTqiuP0YeCINq5g4YtV0vNHFz2ckeEDKf5Cy1U0sUJ4COFukzMPJss2lbwkZWdNHXecLoB2mcPhQ-dEPrZHIvzDUYMTDKpdP0Bi3lp_WZ8qWXoZS2R7my4PGFxRboBejby9qQeUQE7gktzjvVhnc2z1zVXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:
ایران هفت شرط را برای آغاز هرگونه مذاکره به دولت آمریکا اعلام کرده است.
پیام تهران روشن و صریح است؛ اگر واشنگتن می‌خواهد از باتلاقی که خود برای خویش ایجاد کرده رهایی یابد و از گرفتارتر شدن در آن پرهیز کند، چاره‌ای جز پذیرش حقوق و شروط ایران ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71914" target="_blank">📅 00:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71913">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/654a3cad3e.mp4?token=uNsHMVuI9U6JNXG7uXWM4xFs7fF-iw_GhWmHENNJBEh4XRGiVuSK0nsq3bCDhqtMvB9GNFSeY84mgMo4GiqoUVt3wsMAM44sVFbJOeBURCL4tZumYtCXmqYXQoV7_xHk1fKoQ0KlzE8R_YXAAUC5Z-DwOXiIyPlPlE-Z65wnDDDPSb1eBjD2cMDK1EuHaxftFKynJYy22rdSdSiS_ma-UO9HeeKdD0MGmygpCuC3WggZqkUDlDGVfDWIXbq0ZNtqMoDnedg7KDtjeIXeIPeRxK-Wot8Ui1l4-R7kmMgnBVtzNYpR_0CyowlyirMJrKEdws64A9YZUtLWEoyfwXfgl2eOh5xhXNSWHhvaws6rMhKoo_SNL6cYubKkS2ByaYSv4VjmXoqnMMpe2T1ixlZ3QIMYBGVTSeYVcsi79poBo_MVK6PC_Jyy5vLdAT_DiNRiZbxu5X3Nunmc9CEkgRb097dbm79_pyJJdJjRqUR4b8eqPU70aWSodAHYRkOKbSjjIHyUe69OY_X7lWltHIgFguLxpV9MZz-Y8X9vw6lRnN9WXOOgkO5x2T8tAdeaWrUlw5Q4pFt5Pz3PPz4iV0ZRqocW5Ug_qEHrtiaF5UQUSEkJaD_827223afFtBkJswNDFkVTN6HST0UUx79EMkQrE1DTcNunIdoRsPGghp3S9nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/654a3cad3e.mp4?token=uNsHMVuI9U6JNXG7uXWM4xFs7fF-iw_GhWmHENNJBEh4XRGiVuSK0nsq3bCDhqtMvB9GNFSeY84mgMo4GiqoUVt3wsMAM44sVFbJOeBURCL4tZumYtCXmqYXQoV7_xHk1fKoQ0KlzE8R_YXAAUC5Z-DwOXiIyPlPlE-Z65wnDDDPSb1eBjD2cMDK1EuHaxftFKynJYy22rdSdSiS_ma-UO9HeeKdD0MGmygpCuC3WggZqkUDlDGVfDWIXbq0ZNtqMoDnedg7KDtjeIXeIPeRxK-Wot8Ui1l4-R7kmMgnBVtzNYpR_0CyowlyirMJrKEdws64A9YZUtLWEoyfwXfgl2eOh5xhXNSWHhvaws6rMhKoo_SNL6cYubKkS2ByaYSv4VjmXoqnMMpe2T1ixlZ3QIMYBGVTSeYVcsi79poBo_MVK6PC_Jyy5vLdAT_DiNRiZbxu5X3Nunmc9CEkgRb097dbm79_pyJJdJjRqUR4b8eqPU70aWSodAHYRkOKbSjjIHyUe69OY_X7lWltHIgFguLxpV9MZz-Y8X9vw6lRnN9WXOOgkO5x2T8tAdeaWrUlw5Q4pFt5Pz3PPz4iV0ZRqocW5Ug_qEHrtiaF5UQUSEkJaD_827223afFtBkJswNDFkVTN6HST0UUx79EMkQrE1DTcNunIdoRsPGghp3S9nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پورن‌استار ایرانی ملقب به «شیر ایرانی» با شروع بسم الله و کشیدن علامت صلیب توبه کرد :
خدایا منو ببخش و از این آتیش جهنم دورم کن بعد این همه گناهی که کردم
بدترین انسان نیستم ولی بهترین انسان هم نیستم به همه میگم خوبی بکنن کارای مثبت بکنن
دنیا خرابه جنگ زیاده سختی زیاده اصلا سختی دنیا زیاد شده و سختی عمر اعصاب آدما رو خراب کرده
خدایا نه فقط من بلکه همه آدمای دنیا رو از آتیش جهنم دور کن
الله اکبر خدایا منو ببخش خدایا دنیا رو جای خوبی بکن خدایا جنگ ها رو تموم بکن
خدایا منو نجات بده نزدیک خودت بکن میخام آدم خوبی بشم خواهرام و برادرام هم میخام بهت نزدیک بشن الحمدلله
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71913" target="_blank">📅 23:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71912">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrpZKOFgdGBv-2FYFNG7xH0drBTG5n8wfpYFl7d_TKgIrHRGJva4DTT9BPzM3-ExFjro8qGiTbizxr1MjDGCcDZbCnHeZuUaj5y63MXAvrYeLYBX07nEh58_PIOr5J72xs6ztooeAkICCORef-f1WOY-7mAly68axwXUFVh0zef_PBaR8WoardaLxBIQVemuqSQmGOIujRnCeMnuZOnVkArhyH_yRYucGfHymPM6Qhzzi4BTg5UM97dkMjHCdYMR-NGlFxeD84-5_IvYGxgDLiFKoqV9Uhlb6FhMMeHQofhjYCftihzco5r_7tAchj1KtIShTfiRvORjrSGM1e5kBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بعد دیدن این عکس دستور حسینیه شدن کاخ سفید رو صادر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71912" target="_blank">📅 23:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71911">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtiqDnafEcGE2505gG4H53rouSt_dV1eGoqje6en--Ukha-_2ZWtxAxvd9l2HXwTk9z3GZDLP_Ewf3tnGyOtUKhjvgxaryBVB_TkIYW9Y7uL9fULBSw0M0vGcI8E3BugkdUyx0KqaWla3iNkHtpcjvJFUaHiqqZhAn_z5QHlTeeUxI-GHsztgOgUzzmW9Gulg5c5kNKTz32PDWi6Zdy01BcYzhKpbDLNaowX7W7rQkXfzmD2bQK7H6qPFi-D9jSRx-65M-1YvJkGXEa9tVdr_dMr76T3w2hNba6Y6M_VezF1360LlZjrOeTLxdji3gKc__qUBODBlk5FRGHnxHQQRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه سی‌ان‌ان اعلام کرد که روز شنبه به دلیل ممنوعیت اعمال‌شده از سوی ترامپ، از ورود خبرنگارانش به محوطه کاخ سفید جلوگیری شده است؛ این شبکه اقدام مذکور را «تعرضی غیرقانونی» به حقوق خود ذیل متمم اول قانون اساسی توصیف کرد.
سی‌ان‌ان با تأکید بر اینکه «قاطعانه از تیم خود در کاخ سفید حمایت می‌کند»، اظهار داشت: «ما از انجام وظیفه خود در پاسخگو نگه داشتن دولت و سایر نهادهای عمومی، باز نخواهیم ایستاد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71911" target="_blank">📅 22:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71910">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411c3a472b.mp4?token=BshRjWiSn2zmMh_YM7SLevQ37Tstjr_80GNGdsPHFL7vHGxgcVsn6LY75HiqB03g9EZ_mrh8a4chw0O4-wfF_RqKq2maPtJifJkGwO-jCofb_tpXWb-obfWE9O44a-R_ADF7MH-Hs4KZNeNVUpesEoPd8UzbR7u-ec4v-8yBzrXPJ80ljLSlTsgMJ0pKvwtDu9XlevvpT6aORQYOl70qjWtcC29ruqor6xHu2jnWwl7LBo59Yw7bFrkp-OrbUQvpPCPK3McHy0iS1Chs9UOBIQRFwo2ppWKbVZ9lpFDrhrtkQJpmL1fdt5qDXM3npWUzu-4NNWBYrUR2O1Th-_IqGpKL1JybQ9w_TqHSCRcvPdC4p-UgR0RGWEa_7Yol6uERIrkFECmZ7O5G0NRlQ29pi0z0Nn3UQyLwUBMUg_qJ98aYOODl1d_Ul6c9ELIaZEZMPhcKUR8daU8ZuidoHPsOE3_aMak_VvmJn2qhTgfWuTuXnwNnEgok2yp_eZBXYEBRVdB0NskmbKfNejpnhCj7VOWZy_VGYgVxKyzhzveK2FD3e7LxUcohtBZBVU_9zstIgPKKnYhm5aFh60t8h9Zzzd8AIGIZvuj5Pxd6JOxu-1iQ-XKx7id_pKhp5AcKJ33A2r5CYINSHcttWIVtB0jT412x1QtFuf7C5DsYLpRhYtI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411c3a472b.mp4?token=BshRjWiSn2zmMh_YM7SLevQ37Tstjr_80GNGdsPHFL7vHGxgcVsn6LY75HiqB03g9EZ_mrh8a4chw0O4-wfF_RqKq2maPtJifJkGwO-jCofb_tpXWb-obfWE9O44a-R_ADF7MH-Hs4KZNeNVUpesEoPd8UzbR7u-ec4v-8yBzrXPJ80ljLSlTsgMJ0pKvwtDu9XlevvpT6aORQYOl70qjWtcC29ruqor6xHu2jnWwl7LBo59Yw7bFrkp-OrbUQvpPCPK3McHy0iS1Chs9UOBIQRFwo2ppWKbVZ9lpFDrhrtkQJpmL1fdt5qDXM3npWUzu-4NNWBYrUR2O1Th-_IqGpKL1JybQ9w_TqHSCRcvPdC4p-UgR0RGWEa_7Yol6uERIrkFECmZ7O5G0NRlQ29pi0z0Nn3UQyLwUBMUg_qJ98aYOODl1d_Ul6c9ELIaZEZMPhcKUR8daU8ZuidoHPsOE3_aMak_VvmJn2qhTgfWuTuXnwNnEgok2yp_eZBXYEBRVdB0NskmbKfNejpnhCj7VOWZy_VGYgVxKyzhzveK2FD3e7LxUcohtBZBVU_9zstIgPKKnYhm5aFh60t8h9Zzzd8AIGIZvuj5Pxd6JOxu-1iQ-XKx7id_pKhp5AcKJ33A2r5CYINSHcttWIVtB0jT412x1QtFuf7C5DsYLpRhYtI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب حامیان حکومت تو تجمعات شبانه شهر بابلِ استان مازندران داشتن دورهم «کلاغ پر» بازی میکردن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71910" target="_blank">📅 21:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71909">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZN-S1x2I07jWr6c1wKqKy-IgQxX3SGZYz-ZCrQA0pon_S-UvDAdcrxmEvKiC3pc4SbNPRT2ree4N0F0Lf3mbRTzcSgzTMw-cCkh6ArBDGDgBkvj7GXBY250rNiWYrHbnzggfftRjayGiM2chket9AB6VGBQj6tREJ99Winw5qyQS4L6D8v6a2nYo3c9ddEoepkEe-908qEPcHyfPfA7wi58e_O0UAmhHGCez05u-CVFMteKmg3wHp0XTEzJGH1PnWLtb7pyput3IQhkjsrYZxgLXLoDpfpYExJSnWlto7dmcAcsrzB53_CPjI3q9qlVwF_ThRoBzsRY6nG-dtj3flw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:نام فعلی هوش مصنوعی چرته و از رأی‌دهندگان می‌پرسه که آیا نام «هوش مصنوعی» باید به «هوش برتر»، «هوش فوق‌العاده» یا «هوش متعالی» تغییر کنه یا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71909" target="_blank">📅 21:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71908">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50e52af4f.mp4?token=TgJ_uX84S3pdJqULA_b07YUAQUQ57B1yS_IyHbo9xtd6bMl7fRr_HGKCBbTWZgb3zoRUMHAJES6A_Ct0gQmAo29K4BRRzArk2iRDLffSJIQ09sIPN-AG76HIvykGPCvM2hWJ3_gDJyxgpJKmyCYEDB5PsiPL5omQFeETY7k4jioLtJnfc1Bk8-pvhtEApZNg807cwVsvmkEyXi89J41eBz4hxU_kkAYnQCd4HXTWhzZ5HpClZODSv6v9G_ryOOwUjJBvKgPW-VBmj8_wog3hIfeYMrMzqPTTTQA5IWjNWgHBRdoDO9dh_g8lLjmZ1sAryTTD0npBtwUOKUIDsfj4hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50e52af4f.mp4?token=TgJ_uX84S3pdJqULA_b07YUAQUQ57B1yS_IyHbo9xtd6bMl7fRr_HGKCBbTWZgb3zoRUMHAJES6A_Ct0gQmAo29K4BRRzArk2iRDLffSJIQ09sIPN-AG76HIvykGPCvM2hWJ3_gDJyxgpJKmyCYEDB5PsiPL5omQFeETY7k4jioLtJnfc1Bk8-pvhtEApZNg807cwVsvmkEyXi89J41eBz4hxU_kkAYnQCd4HXTWhzZ5HpClZODSv6v9G_ryOOwUjJBvKgPW-VBmj8_wog3hIfeYMrMzqPTTTQA5IWjNWgHBRdoDO9dh_g8lLjmZ1sAryTTD0npBtwUOKUIDsfj4hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تست اکتان بنزین در عربستان …
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71908" target="_blank">📅 20:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71907">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-hKgAcZ73iAJ7k3Z4Qu7IcbK0KvEKclSY2xZx1YR2XNHPRycxq7_Z4PDYVs5oce_zw7TS4jlW8nwHEu_JXvSbdYl49og5fh1X8RfH0IJQqCkZcEMyecEooqv5JjekjkTccy38mXbgkUnerbh7u3nti_sZXmd-nL6_x_YUOT0KCKOEqfYamipurCHUHNl7wQqNG6G_twEX7CO7ph7wCQWiGP7jt2jMpD5H6ybnxvnhhFoYtB0u3ZdkEd596SXV2LEsW9Et6cJG7MdpbVuXcTClu8CGZn3k8P1MtyKsJi5L8jq7Ngemf0RB_CGC_CQ04hfRFJp6P0Zxjkirw02O_H6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان هواشناسی: طبق پیش‌بینی‌های فصلی، بارش پاییز امسال در مجموع فراتر از نرمال خواهد بود؛ تمرکز بیشتر بارش‌ها نیز در غرب، جنوب‌غرب، دامنه‌های زاگرس و بخش‌هایی از البرز پیش‌بینی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71907" target="_blank">📅 19:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71906">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی ایران، در گفتگو با شبکه الجزیره اظهار داشت که دونالد ترامپ، رئیس‌جمهور آمریکا، در ارزیابی خود نسبت به ایران «دچار اشتباه محاسباتی» شده است؛ وی همچنین بنیامین نتانیاهو، نخست‌وزیر اسرائیل، را به تحریک برای آغاز جنگ متهم کرد.
رضایی با بیان اینکه تهران «برای یک جنگ قاطع» آمادگی دارد، هشدار داد که هرگونه حمله بیشتر، با پاسخ‌های شدیدتر علیه پایگاه‌ها و منافع آمریکا در سراسر منطقه مواجه خواهد شد.
وی خاطرنشان کرد که ایران نقاط ضعف ارتش آمریکا را می‌شناسد و برای مقابله با حملات هوایی این کشور آمادگی بهتری دارد؛ ضمن آنکه اخیراً یک موشک ضدکشتی را در نزدیکی یک ناو هواپیمابر آمریکایی آزمایش کرده است.
او همچنین افزود که ایران به این نتیجه رسیده است که پس از خروج آمریکا از یک تفاهم‌نامه، باید راهبرد خود را در قبال واشنگتن تغییر دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71906" target="_blank">📅 19:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71905">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">رضایی، دبیر شورای امنیت ملی:
رایزنی‌ها با میانجی‌های قطری و پاکستانی ادامه دارد و ما شرایط خود را برای مذاکره به آن‌ها اعلام کرده‌ایم.
ما با میانجی قطری در تماس هستیم؛ او شرایط ما را برای توقف جنگ به واشنگتن منتقل کرده است و ما منتظر پاسخ ترامپ به این شرایط هستیم.
شرایط ما عبارتند از: پایان دادن به جنگ در تمام جبهه‌ها، آزادسازی منابع مالی بلوکه‌شده و پایان دادن به محاصره دریایی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71905" target="_blank">📅 19:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71904">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOIMawGXOkVFoQ4A7rNueZDfqBhWpJOmPDbeTlWlo8sbIcODejG-kRiIsHSn5ChO_dmW-3Z9pv9cLGAQ7uOhfvifESVeUbHkJGZDFCR1CIvuiFwKG9eYs1oAQf0uvrtpNW4RzgE440wk4A5DyP7XBXUNr2wxxtRvyutiWiICboo3ed0cZqfJwtEfQrlExQwwWf7HN1zvdY8k7FcSCD5hzbZ2VbqG2C0_TQfMZI8yb07GIk9JOuC9fyn-7wrCcQFQP1Gk_0XPwxl5_kbJ-G2D1nxl9gAaE__G95qHz-05gH08iUyGHevxjjBVWbSs8WGAWDutoGE6-PaKQ9Vr71cyuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی در گفتگو با الجزیره: اقدامات آمریکا و اسرائیل ممکن است ایران را به سمت خروج از «پیمان منع گسترش سلاح‌های هسته‌ای» (NPT) سوق دهد.
رضایی گفت که ایران هنوز تصمیمی برای خروج از این پیمان نگرفته و افزود که این تصمیم به اقدامات آتی واشنگتن بستگی خواهد داشت.
وی تأکید کرد که ایران همچنان به فتوای رهبر فقید انقلاب اسلامی مبنی بر ممنوعیت سلاح‌های هسته‌ای پایبند است و دکترین هسته‌ای خود را تغییر نداده، اما «نمی‌دانیم در آینده چه پیش خواهد آمد.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71904" target="_blank">📅 19:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71903">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7703ac3568.mp4?token=O_szPMHAGW1z8nE_GSabKF1fMrulXPNdLrSexdk5xan_lOs5aOO2BNi7VgQHVDXyiTqguIDL_QigRV13rWnIafJROJ1ojGHteyH2uPPg1VDItQklrzBVQseZ0A0Ka2jwEu2xmi0PqZfGnl4lgylKmvLd17jCetKYec2-xPYjU2RvsLtpD0TZNUP5aKjfeYoRz1m3yFlr-TJ0_P2on6hNP0N_o0Bxnlq6QeEqnTJYEo8gSRaunkHvQlwY4UjKIu1LSPSk4O7EXu8Lu0r0lj8GwZ0HKhORRCNcUU-JN2so1qQfWuhh8nhQkkm1-v50BM0PNPFQ2nuge-Yn8WW3l0MyRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7703ac3568.mp4?token=O_szPMHAGW1z8nE_GSabKF1fMrulXPNdLrSexdk5xan_lOs5aOO2BNi7VgQHVDXyiTqguIDL_QigRV13rWnIafJROJ1ojGHteyH2uPPg1VDItQklrzBVQseZ0A0Ka2jwEu2xmi0PqZfGnl4lgylKmvLd17jCetKYec2-xPYjU2RvsLtpD0TZNUP5aKjfeYoRz1m3yFlr-TJ0_P2on6hNP0N_o0Bxnlq6QeEqnTJYEo8gSRaunkHvQlwY4UjKIu1LSPSk4O7EXu8Lu0r0lj8GwZ0HKhORRCNcUU-JN2so1qQfWuhh8nhQkkm1-v50BM0PNPFQ2nuge-Yn8WW3l0MyRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: کنگره در چه مقطعی وارد عمل شده و به مسئله جنگ با ایران می‌پردازد؟
رئیس مجلس، جانسون: ببینید، دولت این وضعیت را یک جنگِ در جریان نمی‌داند؛ و واقعاً هم چنین نیست. آن‌ها در تلاش برای به سرانجام رساندن یک عملیات هستند — عملیات «خشم حماسی» (Epic Fury) که موفقیتی عظیم بود.
به گمانم در حال حاضر نیازی نیست دموکرات‌های لیبرالِ مارکسیست در کنگره بخواهند به فرمانده کل قوا دیکته کنند که با ارتش چه کار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71903" target="_blank">📅 18:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71901">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75801e50d0.mp4?token=gl0xw3fy7-FEIgsM10zBb-mM6eDZDLV0wL4HEqV3GNWqYT4DuY9USR407NAPvDs3iMaAoY30n892tJLx-9hKn9y9Y6zYg4jEaQZcLHkwF2b2pv9Wblut06Ujd6G5vdJ1dJtXx0bJh-7MKGOEsvKjvJjkG6eaBHC4dkn7F0aWIdcd3B4due8JTpmyv4YWZRCUkafHrH0CljI5dXs-SkoVTCRgZQTL1MnTW2hdXEp9jmZ_kkIWi0KWmvvQqCW3QljTnhzn0N5_AIAOePgit7gjHL_Kt_3hOMR5NFLixD2obBONeYeR8veEq7b4OfFpyEJOnYGYQhKiLdDURe-bJ1Sb9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75801e50d0.mp4?token=gl0xw3fy7-FEIgsM10zBb-mM6eDZDLV0wL4HEqV3GNWqYT4DuY9USR407NAPvDs3iMaAoY30n892tJLx-9hKn9y9Y6zYg4jEaQZcLHkwF2b2pv9Wblut06Ujd6G5vdJ1dJtXx0bJh-7MKGOEsvKjvJjkG6eaBHC4dkn7F0aWIdcd3B4due8JTpmyv4YWZRCUkafHrH0CljI5dXs-SkoVTCRgZQTL1MnTW2hdXEp9jmZ_kkIWi0KWmvvQqCW3QljTnhzn0N5_AIAOePgit7gjHL_Kt_3hOMR5NFLixD2obBONeYeR8veEq7b4OfFpyEJOnYGYQhKiLdDURe-bJ1Sb9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای اسرائیلی به تخریب خانه‌ها در «میس‌الجبل» و «المنصوری» در جنوب لبنان ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71901" target="_blank">📅 18:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71900">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8be83e9c35.mp4?token=YLdtOHXJrk_TzGKI814U-H0JkdJGuCBMf09ezmfVmu9S8znkm5sCcKm8_4xYJUJgY25knh3WsRoUX2YOL2F40zYBW-9kzegqjxh4SxSG0TSeO2QnQrbCf8xHYBRSglFWrsR430qd27V3QLDOiztmgzYcslzhctNmJlMLpdVqUJ5CMHdVWGSrECs41q7I5qWGdFc3Cz89XmS4cYnRA87czHjSF3qVoT7lna7Nx8z6_vWyDLEsrYAlYlMP_521QGuzrgXNJxqfoNIscQp-iuPrzqNJyj8WDpGIy_x2mVFgedUyYXNBT3pBVw1uuh6rs6Pn6jI60SG2UJqk2fHkFOKgcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8be83e9c35.mp4?token=YLdtOHXJrk_TzGKI814U-H0JkdJGuCBMf09ezmfVmu9S8znkm5sCcKm8_4xYJUJgY25knh3WsRoUX2YOL2F40zYBW-9kzegqjxh4SxSG0TSeO2QnQrbCf8xHYBRSglFWrsR430qd27V3QLDOiztmgzYcslzhctNmJlMLpdVqUJ5CMHdVWGSrECs41q7I5qWGdFc3Cz89XmS4cYnRA87czHjSF3qVoT7lna7Nx8z6_vWyDLEsrYAlYlMP_521QGuzrgXNJxqfoNIscQp-iuPrzqNJyj8WDpGIy_x2mVFgedUyYXNBT3pBVw1uuh6rs6Pn6jI60SG2UJqk2fHkFOKgcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ، در حال انجام تمرینات بدنی صبحگاهی با «سپاه دانشجویان افسری» دانشگاه تگزاس ای‌اندام (Texas A&M) است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71900" target="_blank">📅 17:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71899">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دریاسالار برد کوپر، فرمانده سنتکام:
بیش از یک میلیارد بشکه نفت خام از سوی شرکای ما در خلیج فارس از طریق تنگه هرمز ارسال شده، در حالی که ایران به لطف محاصره آهنین ما، حتی یک بشکه هم صادر نکرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71899" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71898">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71898" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/71898" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71897">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMHN4o5W2k7ZZtc-aH3qqIAwj7TmOBq6XEuopN4KRAQctHZqFbeEEwN_Iyyg4sZi9nYdEmJcH17Ig2JiMBPFyqUIULmKde2mc8o_JS27c2C37qi0qG7ioL2Jm4VwMs44dd1fe452nXyGHBP6DoJ2ElMBBRBrH9WB0TtaarRc0Q6OBXYH2Sl2036jyhf4PNPdS0SRiqwOPxBgpcxdDCT7vIFa0tTT7NXF2-qv4u9dImzDNqoMcyafZLl9d7FUio5mmUAt84LeRBrTGAfElbnodjHXltKAkgERh-3e_IFsdih1ZOgcYmUmUk0EzE_nRN4EWAdPKAP5VD9YXDD6z3p4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان‌انگیز  بارسلونا
🆚
سویا
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
بارسلونا: ۵ برد و ۲۵ گل زده
سویا: ۳ برد، ۱ تساوی، ۱ شکست و ۷ کل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71897" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71896">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7687234b2e.mp4?token=emg_VqNTTNDX1jgrMqAX19eUKSikocvF6TQo6RiD66QFrJcrEPpEZ2W_bwvbolEq5Czv5B3S8ZmzVo_c77E10CJbLL0cElyKV6mwIFgF0SdDeLWWrZPZkYYSa4CoDGgpc704oZUmezV5yIC1ycvlogcNPIiAKbael3lD1W2Lz9OG7fLZuzSm2crQ3kPqwpER22BCfsxsEJMbCdv_vXX9AAbFrKEtHHfZwAGFDhO_ZtjtA7u8zXxWLrlULgmtGjPv_TDmpipAbtabd_HL8IOoan8TFCHyew8SZvWW-rxVQsJarIVMmOptkaw_3va_XwrNNtJuD2GyPQhQgMBRm9uVvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7687234b2e.mp4?token=emg_VqNTTNDX1jgrMqAX19eUKSikocvF6TQo6RiD66QFrJcrEPpEZ2W_bwvbolEq5Czv5B3S8ZmzVo_c77E10CJbLL0cElyKV6mwIFgF0SdDeLWWrZPZkYYSa4CoDGgpc704oZUmezV5yIC1ycvlogcNPIiAKbael3lD1W2Lz9OG7fLZuzSm2crQ3kPqwpER22BCfsxsEJMbCdv_vXX9AAbFrKEtHHfZwAGFDhO_ZtjtA7u8zXxWLrlULgmtGjPv_TDmpipAbtabd_HL8IOoan8TFCHyew8SZvWW-rxVQsJarIVMmOptkaw_3va_XwrNNtJuD2GyPQhQgMBRm9uVvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رژه ده‌ها هزار نفری جانفداهای عراقی در حمایت از صدام حسین دو ماه قبل از سقوط رژیم عراق (۱۵ بهمن ۱۳۸۱)
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71896" target="_blank">📅 17:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71895">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f42ac1c41.mp4?token=Ie8MqLEEnlaA0gXaoQ9lP00-qb-1NIoxsYUadeLDnWpboFAPdl0c0UXwMpno8u7n5evOFe4qjKwEpBAg7U1-2IfWaYyGZzQxExVYXrKeDZJYHTODAY4Vbt8TXiePVRo5ORs_btF-tLhdhMaTrn629ckad6YQozcol_tmqFV8UdKygiKybpjc1IFTdvtDC0HW2dSMCHIqWGsp1fkrFoPqOrkVmCBZ9aAfNIfamPc2xTR3wtLibdZkbL8lz_0S9x3FIx9x0LWzHTSpIo-4kprfveBOxtdPZJg_QpErA-gtcpAsOG2bT-lKsMlV41o4F-dDT-xSLs8H3GME_rDx1a3HGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f42ac1c41.mp4?token=Ie8MqLEEnlaA0gXaoQ9lP00-qb-1NIoxsYUadeLDnWpboFAPdl0c0UXwMpno8u7n5evOFe4qjKwEpBAg7U1-2IfWaYyGZzQxExVYXrKeDZJYHTODAY4Vbt8TXiePVRo5ORs_btF-tLhdhMaTrn629ckad6YQozcol_tmqFV8UdKygiKybpjc1IFTdvtDC0HW2dSMCHIqWGsp1fkrFoPqOrkVmCBZ9aAfNIfamPc2xTR3wtLibdZkbL8lz_0S9x3FIx9x0LWzHTSpIo-4kprfveBOxtdPZJg_QpErA-gtcpAsOG2bT-lKsMlV41o4F-dDT-xSLs8H3GME_rDx1a3HGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه آخوند تو صداوسیما :
اگر یک
قو
با
لک لک
ازدواج کنه بچشون
«قلک»
می‌شه
اگر یه
دارکوب
با
بلدرچین
ازدواج کنه بچشون
«دارچین»
می‌شه
اگر یه
مارمولک
با
لاک پشت
ازدواج کنه، بچه‌دار نمی‌شن براشون دعا کنین
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71895" target="_blank">📅 17:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71894">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBdi86CCep8XoSBfNqnkNv9ZALV7PTyMqmjbxrBdc5r9nDQdsU-NdTGFzsvFb_FauWzNxGA2qJBeLpB2huFvcPTaqzt2Z79Evv9VxaQRPSjrBTdlxL5GU9V8iCFRSRWHeWjlGaJymYqrjoXzajyAwBJmkx1Ev_HR5-mF74VegayXwbaeM-mB8-JSBy_-b170hbB-AFEHH73NR-NvQhGwf5RYR8ZfFQ6sueGKFMgVW653UCBaeH--xkwUigvvowV6PFa51fD-Vn8NCCcYldt9MBzeqRudnTaZobNtubZ3GM4QUVTVMzoyWn3YwFBuyVhoUTY5vHZuYUUqCnk21wXUNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنتاگون روز جمعه ششمین مجموعه از اسناد مربوط به UAP/UFO (پدیده‌های هوایی ناشناس/اشیای پرنده ناشناس) را منتشر کرد که شامل ۷۱ پرونده مربوط به بازه زمانی ۱۹۵۲ تا ۲۰۲۵ است.
این مجموعه شامل ۵۵ فایل PDF، ۱۵ ویدیو و یک فایل صوتی است که ۶۴ مورد از این ۷۱ پرونده، حاوی بخش‌های سانسورشده (حذف‌شده) هستند.
در میان این اسناد، سوابقی از یک برنامه نظامی وجود دارد که پژوهش‌هایی را درباره موضوعات غیرمتعارف — از جمله پیشرانه‌های «وارپ» (warp drives)، کرم‌چاله‌ها و گزارش‌های مربوط به آسیب‌های وارده به پژوهشگران در پی برخوردهای احتمالی با وسایل پرنده ناشناس — سفارش داده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71894" target="_blank">📅 16:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71893">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=PSY1yUez36LDyKcgNq-3gYtubOGMzYM7nzVMN_jcsAUrEPqHoM7eg00twg1jtq5nFiOKfyqhOGs9MDqgNALZONjJwx9wFlCEOU-Y1NqiO191EoHPWF_4xK5jldIr48fxWVF1iC1E2e612nSnQeGxDnVZtMqh0MJ1Ndg5kcMqJt7sO4YLrJrqyASPVQ_FlbX5uMjadJIZzg0xmYI9LVy6eMk-zganOF2ZDknTNr0-SgJyt7Bsvt9wq7SYrFXeX6hYmfQW4JzPstGJFuo-o6uTvm6yGEE5iMerxo3Jyexq3Z5FmxRE3VsMEInMvXhSeD2gcoJVWBpM90-91S9gKXlD6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=PSY1yUez36LDyKcgNq-3gYtubOGMzYM7nzVMN_jcsAUrEPqHoM7eg00twg1jtq5nFiOKfyqhOGs9MDqgNALZONjJwx9wFlCEOU-Y1NqiO191EoHPWF_4xK5jldIr48fxWVF1iC1E2e612nSnQeGxDnVZtMqh0MJ1Ndg5kcMqJt7sO4YLrJrqyASPVQ_FlbX5uMjadJIZzg0xmYI9LVy6eMk-zganOF2ZDknTNr0-SgJyt7Bsvt9wq7SYrFXeX6hYmfQW4JzPstGJFuo-o6uTvm6yGEE5iMerxo3Jyexq3Z5FmxRE3VsMEInMvXhSeD2gcoJVWBpM90-91S9gKXlD6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی روزنامه‌نگار و فعال رسانه‌ای:
هنوز مشخص نشده که موشک رو کی شلیک کرد (به کشتی‌های عربستان و قطر) و توافق رو بهم زد!
وقتی رئیس جمهور تو عراق بود، وقتی رئیس مجلس تو مشهد بود، وقتی پیکر رو هوا بود؛ یه عده خودسرانه موشک زدن.
کشور داشت آزادانه نفت می‌فروخت و پولش رو می‌گرفت ولی یه عده بی‌دلیل به دوتا کشتی تجاری موشک زدن.
چرا؟ چون میخواستن شبکه فروش نفت‌ خودشون رو حفظ کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71893" target="_blank">📅 16:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71888">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U0QNap5Bawws4r9Sz-huEZB8fUBKjAi2JX1gXOCzxRtA5j4fKoxjFOmIrjszWEzLY6eHxktzWG7oQ4gbbHIo-1d3jpG-LEJzB2Lya9RR3cWFvO1dbz-iW868nmNqk53lGIaz5lpaffEHw5_7xAgGC7JWCSwf9MGufYkKsltvGv0t64bvy-zokygL4NTooX5n8Niebo1KQa_1JMgGyrdC9siymwZNoVFmRMn8NKMhuFo-zgvjOMwin_VyZfzC5gYNXX-9cqexsEsJwWOmcAfIgSovH-A9UARG9AwUTIJoF3Q7XIwolL-aGg5Qs4p7NWOGyenv7BSV0Kz1SjxiQXUCTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FvEl8RvLpnvtL7eFAQ_6TzPIjmrZLO481Kl-nwftCxWo7lwtFl-hNdDMU8oV2v9a2t3btGIZOlgDA6WZmXCGq7CKaT42iJoTsYU3tRTPjt4KZuvfJWDFc69-Ep1Jm7_48K43SyFnDxicCgqiKe32ZxwksxpKbmdC3kM0hLHel4e_VrN9U2I1K_4yXrZoOzpFsQSzJ16RYXI50JrEdaxg340olvrHvjEakCKBVofw_ELYf9SKGyzx1IHHj8ZP4iLJO66gRcnL56F76tJ7CkbVUpADd4WXX86t8ZtrwUXGzp6HigTHtMNe4fraiTqL4dj47P4lKIqm9pjYGXQC6qam3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BOxSm4fg1_Iiw07blKm37Jfz0xpL9wpiIiTjVKjGLhIYqtfzmkgBKqoqAGQwGbUj3z5xBiu_uCRA6eBCttwGLEprW4W4tVMF0bPErtB1mXrXPhfzaPBg_ZYbPo3F2oQ2-NlzZTbZBzpvuLZWlfk0Q708MxwU1On5k35ZJH6a-2wmlfIkZEpdOIU-KHMXVPGBOf5cDigtuuoGRS7IN5pv_1q4JChg7xTkrRfKg61cPsmkE6LM3iE4H-tCZPEv6yvCM5wdfQHn_nefkgceNObmRj3qr6iHHyo-c6YclWL1YH93aIdB3j7B8dlljU0CTBArmRy-uIp74-5lJb0hhBObpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iwALWvDLHJGkfs5-sVTrzA-OqNGhkaGPv50HkqHX4aFquvbt98shSjUL8BntBo4d1XBSJF8yF7ushi91CguGnK0BS7QuQUJnJPnhLBflgfAezWOqqIZEjug5xkxxjCqG7qbo_cfKtiWscbhcNr3y2eboUipAvGBD7CCS_Mt1Ax9Xny6UQEs4zpXIpzyqzjS81QVRYbvLyIyAajblGwwalXAB2C4qUxCmrMcb47IhvIIMeToZWmWBAlWaxAmYZYH6VmcQ_nKVVDbv8PnxrS2-gJy1BcEO3QwSLdK5KiOpgdPhsHO56_D4Zf5IqlDLGfzMq8zoHOLLWCGghZHyOdqaQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IVurmZK1bodGk5aDY4Yc6WUIjU_bydxorGTwceGzIwqsy8_-Om_oH21H5HD1ZvZAeV4Co48uC9SqZBVJGIuuU-NQABPSZ24cGKGZHu_ZaM3bRhFphyd5njHZDrN_72jH3djmPjIvw6NAVq87bnmnPOMtTbCfIvyP3b_3RzN52s7RkaGUBlXexdhXUsm0__xa-FKafS2bVQRs_rIveRMZ4RSKaHefJQTkeTjfUi8TLAyCiL9yiBUeKCOvQD9At4xPgqMtdFOhMr6v09BTFz4dJLH_9mjTza9AJutXTb8tjUqd72m6w5sTaa29oBOoysXJ9Hvr12ecE0OFiSma9gXWkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه «میداس نیوز» (Meidas News) پنج عکس منتشر کرده است که پیامدهای حمله ایران به یک پایگاه آمریکایی در کویت را نشان می‌دهند.
در این گزارش نام دقیق پایگاه ذکر نشده، اما من آن را به عنوان «کمپ عارف‌جان» (Camp Arifjan) متعلق به ارتش ایالات متحده شناسایی کرده‌ام.
تصاویر حاکی از وارد آمدن خسارات سنگین به یک انبار، محوطه بالگردها، یک پناهگاه مستحکم (که برای اسکان نیروهای آمریکایی در شرایط حمله در نظر گرفته شده بود)، یک ساختمان چندطبقه و یک ساختمان پشتیبانی دیگر است که همگی در کمپ عریفجان واقع شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71888" target="_blank">📅 15:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71885">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ayk49iIlNRL_DjXrDgcpEm6uafffELMUiJJwitCpfzfWnzngL26enU_7T2eLp9Miv1P0xHLu_cVCe9Zo_qdSf5x6gg8QPnvu-36o1T-9TEI472NQNeQccihjw4z-qcZXiIH0BWAwkoOTlKRF2nvRHPgXKJKo9_7wuCf4rm7RGHx4KbtwfreORk6KoK8f12KAgiyPu5bqJOKsev9lYQ4YDCW7qNgNDbwmsSRg8uJaAzXZuxW6Xyzd-MMRVsmybGjdmg_X7oviEZY5nikLMLfQRQNtCr3-nXsK9TTMle_ZxwbWtEj9YWffF42uJKWuf6fvy8eozoieAxgIONwt_QAb6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CAm_1asv7IQ6veuCpvQqbVjFs_aKw-EET_1fdC6AUqm6qaEnFlygcwdZFcwgaOJLBWhKIA2Aw5zuPllz24NG3QVGPwdXGEWG4faYM3HaRBjYiJHoMWV8O93SrOz4CjwJDX7sH0aO092esljzjBedJsSse-xUt0ElkOW6QZgceRCt6uF4SMdf0iZecBiAX_bU5pbYxhS1O2W6Kqrk1WdeDmD-hscZEdPdLUhKisxvTxeNQdotiFudM4kGUwHqF5R3ENGxISGpoHJV9IkKFO6XQijtROZ7z7keZ0CCjkKDH-9SzJ9eFkZdfefiMyuVu3uTxn_O5FQC7rkPfLo-4lABOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bXgrclQolLy3mfBuGk-EYOmrH-zKF5yarZHYHKcGJsLjh81AJp0vNbm2ffgLSBAwBiYbgsV5u0C5mMfEYxJfZf9qFYKJ_oVP2dvg7COsREDIZLipoLOyfT0QIlu6XEeSlrr4XhSvj1g7QXsJeWQV3yc1OaBob-V8SLKKTJNPL9LaAfD0PBNnM-UBhB0OWty5cqwYUl3CwfJF_0aNjokk6BOC59Oncl2Y2X0xC6qxRfP-J0fVTF3dguqC58n9Bck1i8jCI79Advrb45i2K9KAUOOj60SLXn85CmtSQQTfaG0fG-fwacD856Y-TtIbEwOgYlHqxWlVO0XVrJVSUwgc3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انفجارهای پیاپی در نزدیکی فرودگاه بین‌المللی ملک خالد در ریاض
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71885" target="_blank">📅 14:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71884">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/974e7b2cdf.mp4?token=mnMem0F_OyX0jKi04QJElC4Ey6xx3H64JfChyQSBMUb4GJN72I0WV81ne9TJnsfzfCYlGHo4glPa1f7hR3LLuDHL5tjZdLh_6d-YBBpTmC_RCNqhhh2BrwvOgiyWsQ0mUoOxoh5fJzyhy5bJtUnz9keatmQZ-jBhGvgpEUlurPxxCCAxSNKmK1gYA8MoZTNHh9WuHgwPQz3mUh7TK2FB8qwiYjnbIT-M1xI1oAvSd8LRJvChpHHbApd4tpsI0Cjy68OdY-AByz-cim2xbHUL0udaJDzZ83UEX8SzCnJ8UvlEqN8m0RRW4ymyF0-GEakSAUpIHdWouoOWuKjApXrmww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/974e7b2cdf.mp4?token=mnMem0F_OyX0jKi04QJElC4Ey6xx3H64JfChyQSBMUb4GJN72I0WV81ne9TJnsfzfCYlGHo4glPa1f7hR3LLuDHL5tjZdLh_6d-YBBpTmC_RCNqhhh2BrwvOgiyWsQ0mUoOxoh5fJzyhy5bJtUnz9keatmQZ-jBhGvgpEUlurPxxCCAxSNKmK1gYA8MoZTNHh9WuHgwPQz3mUh7TK2FB8qwiYjnbIT-M1xI1oAvSd8LRJvChpHHbApd4tpsI0Cjy68OdY-AByz-cim2xbHUL0udaJDzZ83UEX8SzCnJ8UvlEqN8m0RRW4ymyF0-GEakSAUpIHdWouoOWuKjApXrmww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف سوال پرسیده: سخت‌ترین قسمت پسر بودن چیه؟
جوابا جالب و دردناک بود:
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71884" target="_blank">📅 14:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71880">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e492d945.mp4?token=eAnrdXUKlBTmMkEKYSBWAnHM0Sp1ZhWjVwwBvcppKa18qu1b9qiQ1U-b6r2VN3bl6ixu1t93jGXtiWgQNwMN5JwTS9cbO32H_9G4y00H5wkNyZ6QvxKYhX_bhfjCIuTu3CoAtadVxX39EA2hfFLWXHtyntQgyM7Ef1MJw8UDxIlBV5aD0QqkUa_xUpUHMi5nfdlbgjZabo6KZYMxbkNhC1cmZAK8RtRaLORNEAZ8z7B5gerUkQQhviqYpb-TGxj2NA5pfEwnRDms71GLlgbcH_3VWsmEpbvCMcVbHApSeOkUPndcAVEZilAqNhqMj869rD91WkL8zMsbpgF0ZLvGzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e492d945.mp4?token=eAnrdXUKlBTmMkEKYSBWAnHM0Sp1ZhWjVwwBvcppKa18qu1b9qiQ1U-b6r2VN3bl6ixu1t93jGXtiWgQNwMN5JwTS9cbO32H_9G4y00H5wkNyZ6QvxKYhX_bhfjCIuTu3CoAtadVxX39EA2hfFLWXHtyntQgyM7Ef1MJw8UDxIlBV5aD0QqkUa_xUpUHMi5nfdlbgjZabo6KZYMxbkNhC1cmZAK8RtRaLORNEAZ8z7B5gerUkQQhviqYpb-TGxj2NA5pfEwnRDms71GLlgbcH_3VWsmEpbvCMcVbHApSeOkUPndcAVEZilAqNhqMj869rD91WkL8zMsbpgF0ZLvGzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای امنیتی پاکستان عملیاتی را علیه یک هسته تروریستی — که گفته می‌شود متشکل از شبه‌نظامیان «تی‌تی‌پی» (TTP) است — در منطقه «کوهات» واقع در استان خیبر پختونخوا آغاز کردند.
در پی حملات بمب‌گذاری روز گذشته علیه مسجد شهر، شبه‌نظامیان مسلح یک مقر پلیس را به تصرف خود درآوردند که منجر به درگیری‌ای ۲۰ ساعته شد.
نیروهای پاکستانی اکنون این مقر را به‌طور کامل پاکسازی کرده و تمامی شبه‌نظامیان را از پای درآورده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71880" target="_blank">📅 14:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71879">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6895254ca3.mp4?token=iKIE_REoU7tcm1sKOkynPMMgO86I4WoMy4S914-DVSDuLbvFPjq7U5ykU4oxQ3fr6RnIDISJBtmPYni3Zvcf-O7_ifKdq_Z372nBiYIceIzDbqDocMNWOpOiNBVEeXi6kwVeAnqPcAYyPRS6yx9LuqqHXMR_ugRYLiKHurB6-KO3GPzeEDsKTP7Im8G97R8zFbSDBmF2ZtE0uB0fF2JeZ2WOwLcNaH5rTTmtDfj9zbs8NqPNp-H_wS-tfESuCLClU_HcaTKFa1747hu8xYYh2hpIxf6_PEYlXDucI56tAA9-E4rNMPI5H8TZdHL3kPuT8JVm7Lx41i1nDTt2G3f32g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6895254ca3.mp4?token=iKIE_REoU7tcm1sKOkynPMMgO86I4WoMy4S914-DVSDuLbvFPjq7U5ykU4oxQ3fr6RnIDISJBtmPYni3Zvcf-O7_ifKdq_Z372nBiYIceIzDbqDocMNWOpOiNBVEeXi6kwVeAnqPcAYyPRS6yx9LuqqHXMR_ugRYLiKHurB6-KO3GPzeEDsKTP7Im8G97R8zFbSDBmF2ZtE0uB0fF2JeZ2WOwLcNaH5rTTmtDfj9zbs8NqPNp-H_wS-tfESuCLClU_HcaTKFa1747hu8xYYh2hpIxf6_PEYlXDucI56tAA9-E4rNMPI5H8TZdHL3kPuT8JVm7Lx41i1nDTt2G3f32g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبیله‌ای در جنگل‌های آمازون که با دنیای بیرون تماسی نداشته، از هوا فیلم‌برداری شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71879" target="_blank">📅 13:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71878">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe570c529.mp4?token=Ku4oE0IKjwXvZHB-J3mBhCXmaQRvRrKa1FoMCEp8yvDLvXpIJQaOVs9CW_fIKI_uMD41JbWjtjLBSQ9e9ZGxM30DfQbdEpxdeuS_p7HKqnmo-mFqF9wyoBCq77XqBBiDGvWawMvlV_xmJxcIq-spmgV2Y3SoZtGQCrRMX2QKrKCNIWs2gXeH7OED2TT3nKIwSYhf2h3S2Fw1m8s2GxYa3vEGCFyyNc3fLP9j_0y3OWRA72zCPlPbBlNq1bWmL3z2esNUHNzj4nn33OE97XJTSFQUyCKR_Cwoc3ThxuvfB-Qw2hZ-Pnp7io7qwHDTRzxHKimYit3CZVz8RuzzKR79RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe570c529.mp4?token=Ku4oE0IKjwXvZHB-J3mBhCXmaQRvRrKa1FoMCEp8yvDLvXpIJQaOVs9CW_fIKI_uMD41JbWjtjLBSQ9e9ZGxM30DfQbdEpxdeuS_p7HKqnmo-mFqF9wyoBCq77XqBBiDGvWawMvlV_xmJxcIq-spmgV2Y3SoZtGQCrRMX2QKrKCNIWs2gXeH7OED2TT3nKIwSYhf2h3S2Fw1m8s2GxYa3vEGCFyyNc3fLP9j_0y3OWRA72zCPlPbBlNq1bWmL3z2esNUHNzj4nn33OE97XJTSFQUyCKR_Cwoc3ThxuvfB-Qw2hZ-Pnp7io7qwHDTRzxHKimYit3CZVz8RuzzKR79RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیبی می‌نوازد:
«نصرالله کجاست؟ بعد از من تکرار کنید: حذف شد!»
جمعیت: «حذف شد!»
بیبی: «سنوار کجاست؟»
جمعیت: «حذف شد!»
بیبی: «هنیه کجاست؟»
جمعیت: «حذف شد!»
بیبی: «با خامنه‌ای چه کار کردیم؟»
جمعیت: «حذف شد!»
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71878" target="_blank">📅 13:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71877">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71877" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71877" target="_blank">📅 13:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71876">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQcwpfhPzZzGuEkjJs1H8xbDl4lKXtCshL6FbX9WWjeowNwmDAgEcKN_RPjj2IEfVVsI3sA9Z7IOQacoGio-KPz90QnRYWUP3PgzcfcDfV2pRKM0fDHjXi63r__kcr9VIclD24G8KGr39ySrHU3JwLQ4R-_JDL5iII2IYQkf9fsNvCuxGzIuzUJ2fu4RYu-HxUbaOt1seu8ug5mh3aqPvFus4THFDYdu7BpsHKOhKvnQfPSejg9AudgQ0jWD8obehL6kMSpIvbMdYrGmDtUnqs8_2RnyzU-Av8eQWHL8Js3EgYo2ygk1256F1gtRnX510v_an2-yhcahdq7lxA3s5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
استون ویلا
🆚
تاتنهام
آرسنال
🆚
برایتون
بارسلونا
🆚
سویا
دورتموند
🆚
اشتوتگارت
اینتر
🆚
رم
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71876" target="_blank">📅 13:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71875">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e25ecc6de4.mp4?token=GyGBx33iFBhkzU9DULaTpLSMP0RKmrh4UI6yHOTUWVPmKLy8A4wWbIxPjGHfytVkluX8XipptyHrge7kMQRxLLmcIzRLLBsLFun5zHQ5vvmYWwPHyElHI7yHtvzCHNWgY-5-XSfY9V1xB7Cr6JPxyfhiWEiMM2llCQvfzbOjGHLAHddh7fQy4HQdOyk9vA8eADLO35uR_VasX7u_RFuLwxsNJp9YDo2IgZGnV1Gfe0myZnllS-8SN0_w1Okc4XlYKXOKpQkonB9LnnhDcIocSGyjlbAyI4MGNmQY8xWwh_1OXGxcLi_a5ogdaHorvS0dexSb5s17xt3Kqvtd9utWS786eGkmv76d_L8paG0fS75-TVL1lMKQksDEXR76irWHjj0mkwSd7Ls3Y8KUBFs6FUz9HSuJpAoxTCeBKx4oP1VIrdzPCnKqg57DdUPVAOHjGTYgKyd0hFV-mDqKHrekIHiWL2gPFc7ylL0iVYUGtCNYEncHQe4r9O1K2BpmIdB7D35iRVmguZLmUBMNneZdLW3Sgzy1GcxOhvgpoDg4fH4n_qy2SoHQaya2QW1HW0Bmh5whBF3jKOrnaLLX6TNOEW3Xju8VZdS5fe8TcNkkQPQsrJ33yDKUFVHqbKLj9hJic1FfOgNxsHcg71v3zgaOmvC0eigppM5y90ccHU9NE3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e25ecc6de4.mp4?token=GyGBx33iFBhkzU9DULaTpLSMP0RKmrh4UI6yHOTUWVPmKLy8A4wWbIxPjGHfytVkluX8XipptyHrge7kMQRxLLmcIzRLLBsLFun5zHQ5vvmYWwPHyElHI7yHtvzCHNWgY-5-XSfY9V1xB7Cr6JPxyfhiWEiMM2llCQvfzbOjGHLAHddh7fQy4HQdOyk9vA8eADLO35uR_VasX7u_RFuLwxsNJp9YDo2IgZGnV1Gfe0myZnllS-8SN0_w1Okc4XlYKXOKpQkonB9LnnhDcIocSGyjlbAyI4MGNmQY8xWwh_1OXGxcLi_a5ogdaHorvS0dexSb5s17xt3Kqvtd9utWS786eGkmv76d_L8paG0fS75-TVL1lMKQksDEXR76irWHjj0mkwSd7Ls3Y8KUBFs6FUz9HSuJpAoxTCeBKx4oP1VIrdzPCnKqg57DdUPVAOHjGTYgKyd0hFV-mDqKHrekIHiWL2gPFc7ylL0iVYUGtCNYEncHQe4r9O1K2BpmIdB7D35iRVmguZLmUBMNneZdLW3Sgzy1GcxOhvgpoDg4fH4n_qy2SoHQaya2QW1HW0Bmh5whBF3jKOrnaLLX6TNOEW3Xju8VZdS5fe8TcNkkQPQsrJ33yDKUFVHqbKLj9hJic1FfOgNxsHcg71v3zgaOmvC0eigppM5y90ccHU9NE3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنری کیسینجر و توضیح سه مسیر تاریخی ایران:
دولت–ملت
امپراتوری
ایدئولوژی خمینی.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71875" target="_blank">📅 12:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71874">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beaae9822a.mp4?token=I96AEaqtQbM7AOAY0kL--xdmRpK5sPcwMEloIllWhr9Nb4XKS5vXaAfsbBfH4K_qoi6jcqd83EbQ7H0_77XFwy_yegkoQvz4UYA2HvL1tZjXI4slU8YR9zE4CHbDBbv4PW3Bqh4-mxuhf1iD3ZoMCyVfu-tq1fEhQhfYc3dBL7cYVSY0b509Q2dd-hfjNsjE5vwKKngereINlVKSN8rwCz-fxm0jwzt7LI-mIBm_Bwy4Q6uBbtcE_pVuffxu0X7m0PI7b-oL85wEceGTXfhBNgS7f-w8misWV7WbZyuFy60VmmY9bkhdQTvh5-hfBWsrvED38DCoTbwCpMw1fNWcIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beaae9822a.mp4?token=I96AEaqtQbM7AOAY0kL--xdmRpK5sPcwMEloIllWhr9Nb4XKS5vXaAfsbBfH4K_qoi6jcqd83EbQ7H0_77XFwy_yegkoQvz4UYA2HvL1tZjXI4slU8YR9zE4CHbDBbv4PW3Bqh4-mxuhf1iD3ZoMCyVfu-tq1fEhQhfYc3dBL7cYVSY0b509Q2dd-hfjNsjE5vwKKngereINlVKSN8rwCz-fxm0jwzt7LI-mIBm_Bwy4Q6uBbtcE_pVuffxu0X7m0PI7b-oL85wEceGTXfhBNgS7f-w8misWV7WbZyuFy60VmmY9bkhdQTvh5-hfBWsrvED38DCoTbwCpMw1fNWcIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تئاترهای مملکت این روزا تو وضعیت عجیبی قرار گرفتن؛ گویا شوخی های جنسی برای تئاتر ها آنلاک شده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71874" target="_blank">📅 12:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71873">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77deac1aa1.mp4?token=l7M3_0FYUm7EEU2y7FIzam_X3MDUZP9_-IUkjGzi5YxRh6O_cqPPIETeqHjnRYWovcO4NImBmuZHTkzBHxZiC1bJMz7Gtwu45cHRpVkl29EeinrFcpkm9xXx6kkG4027z3YYdc2t_lpPv_99w2iJV_uEfaHv8PFdvan31joAah3Gng1ilzj7g0M6R--zHhilExtDJSjJR_7FJu6_qCx5k5NM2fUn0mk77RKOcXSWw-10eqgvhfTdGzo6QI1X9I64YQKZODX7fVWH4xTsuOCclUKjur3Wx079eT9lvnZkr1rDzd5ltfwBGUj83xmvvczXziQlTSLFr728KLXj2uP4fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77deac1aa1.mp4?token=l7M3_0FYUm7EEU2y7FIzam_X3MDUZP9_-IUkjGzi5YxRh6O_cqPPIETeqHjnRYWovcO4NImBmuZHTkzBHxZiC1bJMz7Gtwu45cHRpVkl29EeinrFcpkm9xXx6kkG4027z3YYdc2t_lpPv_99w2iJV_uEfaHv8PFdvan31joAah3Gng1ilzj7g0M6R--zHhilExtDJSjJR_7FJu6_qCx5k5NM2fUn0mk77RKOcXSWw-10eqgvhfTdGzo6QI1X9I64YQKZODX7fVWH4xTsuOCclUKjur3Wx079eT9lvnZkr1rDzd5ltfwBGUj83xmvvczXziQlTSLFr728KLXj2uP4fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه شغلی در کانادا هست به اسم آتش‌بان. طرف باید فصل تابستان رو در کابینی بالای کوه بگذرونه و هر وقت آتش‌سوزی جنگلی دید گزارش کنه. عمیقا حس میکنم من میتونم خیلی تو این شغل موفق باشم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71873" target="_blank">📅 11:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71872">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d090aca4d2.mp4?token=CANhHgsFqoxateChdVgvPmilImD5NDbM95NME5xEmO4YjcyKYaSR_uF6G7M01T4OU91JsQ3F6p3W1BODxhCuugZp6fm4LUONAfGEiHNTnckg9GTH68JuhcETbbgJkbyWshGCofFERR_adYU5CgcDge80qjAQeQzPgaausrTD7LJ7vy2XuFs_Hroyyn_gQK_sb3idCEVKvR2HdaQklq1nC4eIwZILXjUF4KrnVvb6muYWeU051u7gYVHeQlYtMOpfbJ74i1k1kMYalVGGmmNY5g_t_W67SvY25McAxVFUWg7fPQDbZR5WudCo_5hnQk3dG2EcUwnD342WB37b1IeC7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d090aca4d2.mp4?token=CANhHgsFqoxateChdVgvPmilImD5NDbM95NME5xEmO4YjcyKYaSR_uF6G7M01T4OU91JsQ3F6p3W1BODxhCuugZp6fm4LUONAfGEiHNTnckg9GTH68JuhcETbbgJkbyWshGCofFERR_adYU5CgcDge80qjAQeQzPgaausrTD7LJ7vy2XuFs_Hroyyn_gQK_sb3idCEVKvR2HdaQklq1nC4eIwZILXjUF4KrnVvb6muYWeU051u7gYVHeQlYtMOpfbJ74i1k1kMYalVGGmmNY5g_t_W67SvY25McAxVFUWg7fPQDbZR5WudCo_5hnQk3dG2EcUwnD342WB37b1IeC7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رائفی‌پور:
رهبر شهید به رئیسی گفتند چرا به امیر تتلو نزدیک‌تر نشدی
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71872" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71871">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/400c93a6ac.mp4?token=LQm7xfjwRz1gKJSoJI3A_Bhjsa0y-tYfw5hLR-xG7_4ehcsymyCLHH4EhBvhVTjrq3rW9M7iPXQ5rm2D0Rwl36V-6OCTvnwVRb1R8OOXMm0CvYaVvYa24hitZq2sqc4OpgI16wm1nZ9-Pq2zmOBFd0BGb_5EhofNA71hsyDdgU0TIVz7zj3tVOubpRWH8t-UlGPEC2scCYfnJIWg3SqW6q8368Z8fF1JWBYKl55cagt-zA444PuM-FgQiTTSdIPbvhQQeoljAZ_AKuD_cRQzUUwaZ4RoyxFNXGZyRx4ye35teBNaLPv1xrfwzh00QvFiDFZYmaFSRb_DwtWeKTKcXA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/400c93a6ac.mp4?token=LQm7xfjwRz1gKJSoJI3A_Bhjsa0y-tYfw5hLR-xG7_4ehcsymyCLHH4EhBvhVTjrq3rW9M7iPXQ5rm2D0Rwl36V-6OCTvnwVRb1R8OOXMm0CvYaVvYa24hitZq2sqc4OpgI16wm1nZ9-Pq2zmOBFd0BGb_5EhofNA71hsyDdgU0TIVz7zj3tVOubpRWH8t-UlGPEC2scCYfnJIWg3SqW6q8368Z8fF1JWBYKl55cagt-zA444PuM-FgQiTTSdIPbvhQQeoljAZ_AKuD_cRQzUUwaZ4RoyxFNXGZyRx4ye35teBNaLPv1xrfwzh00QvFiDFZYmaFSRb_DwtWeKTKcXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پورن استار معروف ایرانی ملقب به «شیر ایرانی» با انتشار این ویدیو اعلام کرده که مسلمون شده و از خدا طلب بخشش کرده :
کاری به هیچی ندارم ، چرا وقتی میگه بسم‌الله ، با دستاش صلیب میکشه
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71871" target="_blank">📅 10:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71870">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40d28238ee.mp4?token=E3e82t9QEIt-BesKRn52ZK6qeDfKJLOfr9xSv9xtQH4ivWRCzVYTxkjq2x1nI7xO0x-fG2k1BXkL-QJYb5yg6WVxWJGjt4yMANXcuqns_ZZ36vquJ3Owm5TeX7kDtIqHZiAJuE_vzWtfLivGDxY3i-63XXupNv7tGoMRO-Tr_GM3DSmwtxT6otiQyiaEOLW8vMJrIu0Ju-NdpQO8AElU76mR7VrR04OOBEW9r7qmX_ixINipp90FAmp2F6uMa_sqBp8g_jiNMWn2wiOYfA820ZD4-uOagKSUQsToB6LZrLSubBGkxdDCtjQnjppyaAb67bxy2KtatjM8aW8na7WGXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40d28238ee.mp4?token=E3e82t9QEIt-BesKRn52ZK6qeDfKJLOfr9xSv9xtQH4ivWRCzVYTxkjq2x1nI7xO0x-fG2k1BXkL-QJYb5yg6WVxWJGjt4yMANXcuqns_ZZ36vquJ3Owm5TeX7kDtIqHZiAJuE_vzWtfLivGDxY3i-63XXupNv7tGoMRO-Tr_GM3DSmwtxT6otiQyiaEOLW8vMJrIu0Ju-NdpQO8AElU76mR7VrR04OOBEW9r7qmX_ixINipp90FAmp2F6uMa_sqBp8g_jiNMWn2wiOYfA820ZD4-uOagKSUQsToB6LZrLSubBGkxdDCtjQnjppyaAb67bxy2KtatjM8aW8na7WGXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو اسلامشهر ی موتوری خیلی ریلکس و بدون پوشوندن صورتش میاد گوشی ی دختر جوونو به زور ازش میگیره و فرار میکنه :
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71870" target="_blank">📅 10:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71866">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6655905e8b.mp4?token=ltQDcIeTmVaPsPRhdeV72mqmJlwAbgL7YdtbIQQtYRrcDve4DLYtoha1NkN01cqhHS8g_MVM25azg8Y6lhMob4tZTEdnvxt2wO-UmRr8kw3Yw9gzNCgmQ6OGyKBXSD7ciPRr0RSqdG1Hi8yQdrD4af4P5p4p8gOH3kd2QWyDigitglQJ-O46C9uV07ZmaG-uTDkMaCE7Kn8wQQFAdhRtJK4KI-7msExfJ_zVtZp3IPqmVsmSDEtCS6o3TsImPstLofHdlXp0UuVM8mBdHUWRUd8tuMr1i1BqcNprlmJpXepZ1uLQs41XUa_8Yg0BkLBwrsSMhIp1xlPLQw6meSszug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6655905e8b.mp4?token=ltQDcIeTmVaPsPRhdeV72mqmJlwAbgL7YdtbIQQtYRrcDve4DLYtoha1NkN01cqhHS8g_MVM25azg8Y6lhMob4tZTEdnvxt2wO-UmRr8kw3Yw9gzNCgmQ6OGyKBXSD7ciPRr0RSqdG1Hi8yQdrD4af4P5p4p8gOH3kd2QWyDigitglQJ-O46C9uV07ZmaG-uTDkMaCE7Kn8wQQFAdhRtJK4KI-7msExfJ_zVtZp3IPqmVsmSDEtCS6o3TsImPstLofHdlXp0UuVM8mBdHUWRUd8tuMr1i1BqcNprlmJpXepZ1uLQs41XUa_8Yg0BkLBwrsSMhIp1xlPLQw6meSszug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید باورتون نشه ولی ایشون دختر نیست و یه فمبوی(پسر) ایرانیه که خیلیا روش کراش زدن و توی تله‌اش افتادن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71866" target="_blank">📅 09:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71865">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbf20c1179.mp4?token=JiI0R4okYhuWlxCv5mxCDvFMAJMX6Dft1_lG2-8cumUVSmA21meJXh-md66I3EKhbD8Pf4p0ZJgqBbOoFsDnMptNX3yH7oxIyG0fGBCL67Q51UP2fv8bwZIbFYg7BCaC43x-vTYsqjNg1xVwHpkHXkybewpV-JI9fXjO4rOADth4KQArje8a4xt_-snJ_mg2LwGGcJhm4MHoTANFa2GWux4dSr7HyxWEfrGIcKfIlmvSoATzeNKyRiABjpnCGV3TNnH0a_ISoiRdDBp1cTEkZhqV7fx4PmCZJz8emZrFkKXYFDJ9Fbyi1O4xU03hAyhpYZGrqvV6D4IICipN6gxaz3h0-W5mhQkqT69R8jPU3RvBAeASvcUs_6i45kHiqtU49yaKgcj7UWpmj8gW9wH4f1Ujv_c1LGeJVmSMj4rUog5xUCVM6NDJFVAYY0zUPYP0BW8yMsr-oiHCjZaPULyZGSj0rG5dgPTVzsAVQdM9FCOfdzUI2V0Bihj04eaUCzpsJqBMZJwytH5rlLKHvld4YB1EP1KrX1o6m72JGeL0BytItac0_G5TzE7V8ljsMcj_jM3CdIm9KynVs-Hx1_LZQhn6Q1RM4ellJJq51n1OPX2IMHFQUeCFIdhOYW2Q081RUAkX8z9ccgT4D2L70Mp0ZCotCyRRoRDNTZmApgTRTFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbf20c1179.mp4?token=JiI0R4okYhuWlxCv5mxCDvFMAJMX6Dft1_lG2-8cumUVSmA21meJXh-md66I3EKhbD8Pf4p0ZJgqBbOoFsDnMptNX3yH7oxIyG0fGBCL67Q51UP2fv8bwZIbFYg7BCaC43x-vTYsqjNg1xVwHpkHXkybewpV-JI9fXjO4rOADth4KQArje8a4xt_-snJ_mg2LwGGcJhm4MHoTANFa2GWux4dSr7HyxWEfrGIcKfIlmvSoATzeNKyRiABjpnCGV3TNnH0a_ISoiRdDBp1cTEkZhqV7fx4PmCZJz8emZrFkKXYFDJ9Fbyi1O4xU03hAyhpYZGrqvV6D4IICipN6gxaz3h0-W5mhQkqT69R8jPU3RvBAeASvcUs_6i45kHiqtU49yaKgcj7UWpmj8gW9wH4f1Ujv_c1LGeJVmSMj4rUog5xUCVM6NDJFVAYY0zUPYP0BW8yMsr-oiHCjZaPULyZGSj0rG5dgPTVzsAVQdM9FCOfdzUI2V0Bihj04eaUCzpsJqBMZJwytH5rlLKHvld4YB1EP1KrX1o6m72JGeL0BytItac0_G5TzE7V8ljsMcj_jM3CdIm9KynVs-Hx1_LZQhn6Q1RM4ellJJq51n1OPX2IMHFQUeCFIdhOYW2Q081RUAkX8z9ccgT4D2L70Mp0ZCotCyRRoRDNTZmApgTRTFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«آیا خواهان جناح چپ هستید؟ (جمعیت: نه!)
آیا خواهان جناح راست هستید؟ (جمعیت: بله!)»
«آیا خواهان تشکیل کشور فلسطین هستید؟ (جمعیت: نه!)
آیا خواهان کشوری یهودی هستید؟ (جمعیت: بله!)»
«آیا می‌خواهید تسلیم شوید؟ (جمعیت: نه!)
آیا می‌خواهید بجنگید؟ (جمعیت: بله!)»
«این جوهره‌ی این انتخابات است: یا چپ، یا راست.»
ما در جناح راست هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71865" target="_blank">📅 08:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71864">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🦖
اینجا فقط ضری ب‌ها نیستن که می‌درخشن...
🦖
چندتا Star آماده‌ست برای کسایی که توی قرعه‌کشی شرکت کردن. شاید قرعه به اسم تو بخوره؛ امتحان کردنش که هزینه‌ای نداره!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71864" target="_blank">📅 01:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71863">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/news_hut/71863" target="_blank">📅 01:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71862">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">#فوری؛دونالد ترامپ، رئیس‌جمهور، «قانون لیندزی او. گراهام برای اعمال تحریم علیه روسیه و ایران (مصوب ۲۰۲۶)» را امضا و به قانون تبدیل کرد.  این قانون، تحریم‌های قانونی، تعرفه‌ها و ممنوعیت‌های اعمال‌شده علیه روسیه را گسترش می‌دهد و تحریم‌های موجود علیه ایران را…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71862" target="_blank">📅 01:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71861">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxWaWDKwK6oaVMom3xn-v7rA51tOio3R1Zkc8lxhiB67JMcA_VIHkE_HmspeC_Xkid1rsKIjGbman0XROfkNqJ82sp4VGf24zZ-ZVm9lrbH2Bl_ONQ_HGlA6yj0pbPLmAuHDlxrrtPjDJXqWFx4qh2Hqo1GIPv-VeM73V8Wt1JJpM5_OHFfHfsf4XWYM4WZv4ubowPS4_ob88H7UMEt6Sls4dezYanihhfK-sua-6zl_viCFAJP_KLoL473TghSabcytPjGsQ8QgZM0z4KoU5EWuxEpyo_60m3936-L1BoIrtwTn2dH8t0LUt0j-YJXSy8V_cMJ9tw6rcxhtp-_hDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛دونالد ترامپ، رئیس‌جمهور، «قانون لیندزی او. گراهام برای اعمال تحریم علیه روسیه و ایران (مصوب ۲۰۲۶)» را امضا و به قانون تبدیل کرد.
این قانون، تحریم‌های قانونی، تعرفه‌ها و ممنوعیت‌های اعمال‌شده علیه روسیه را گسترش می‌دهد و تحریم‌های موجود علیه ایران را تمدید می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71861" target="_blank">📅 01:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71860">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ اعلام کرد که ایالات متحده با دانمارک و گرینلند به توافقی دست یافته است که بر اساس آن، واشنگتن اختیار دائمی در خصوص الزامات امنیتی آمریکا در گرینلند خواهد داشت، در حالی که گرینلند همچنان تحت حاکمیت دانمارک باقی می‌ماند.  ترامپ این توافق را توافقی با «عمر…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71860" target="_blank">📅 01:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71859">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZccaxoFxza4FjYvNePJ3QKSopHDLvHy0n2SLtUzRd6ZnA4UGyZeE1uHntqfcJHIH65xdlweUtfGB0WMctuBBLSQRmaUVih9iuze3q_ECyIKhM28og0AoWT1jt-dSNyfNpUIY-W52rqvosTND9-bo1L_8pgOZxPLQGY-X1mfSRlwruUv59RsUuQC2fT0dlAJsH5IlUBF4mY6nukP5mlPCgeOQ9-UM439A1b-92Ndhfcnvo5lLrHT9Kg3fJlJK3HBYgwSFRxFIVZLuZHwO7Jk646ApPjwTDXgeERsl3mjRqaLPhltuiM0Xwi6atlaQQIoxUx1KkcIt2h3oltepQrsNRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اعلام کرد که ایالات متحده با دانمارک و گرینلند به توافقی دست یافته است که بر اساس آن، واشنگتن اختیار دائمی در خصوص الزامات امنیتی آمریکا در گرینلند خواهد داشت، در حالی که گرینلند همچنان تحت حاکمیت دانمارک باقی می‌ماند.
ترامپ این توافق را توافقی با «عمر نامحدود» و «بدون تاریخ انقضا» توصیف کرد و اظهار داشت که ایالات متحده قادر خواهد بود اقداماتی را که برای دفاع از گرینلند و آمریکا ضروری می‌داند، انجام دهد.
وی همچنین تأکید کرد که هیچ‌یک از دشمنان ایالات متحده اجازه نخواهند داشت بدون تأیید آمریکا، در گرینلند حضور نظامی داشته باشند، پایگاهی دایر کنند یا سرمایه‌گذاری‌های حساسی انجام دهند.
او می‌گوید این توافق برای ایالات متحده «هیچ هزینه‌ای» در بر نخواهد داشت و واشنگتن بلافاصله روند گسترش حضور نظامی خود در گرینلند را آغاز کرده و در زمینه ساخت‌وساز و توسعه با مردم گرینلند همکاری خواهد کرد.
ترامپ این توافق را «تاریخی» و «تحقق یک رویا برای ایالات متحده» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71859" target="_blank">📅 01:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71855">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ddIY6NwXpZoAMLbRwrdMeQ1G4PpEYIvCnwhJi2E5EJyErsneh4HMWIYcdL9pNsFo4iC8FesMAJfWrH8Ek5M2N5kP_0k2A29QiCQ1CweJW5pIPZIFG0fdkODw1yHO1l5icQESVU1BcktbFTmMuO5zyGbkv0eZbAia0yUIj-OGzckU8c1RM7HO9_ECui03Xfe0EFtaB60XoTzoFQw191zahna__dK78qu6-p9LLoWWFAI9FVIRxWHX1mVMqipovxAul5XHAOuie2l1K8xcaAWZ_5gepkzM94tKvlirtUpbzZiENfpCUOUoTh1l2U6Axryep1Fz-Vh0bX2af2E480yehA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OJr5hOl83_M6YMMtWBHQxO6q-cWUhmRw-4s0svPeGJ5mstBVJVoxf3X-Wgpox1DoipzUfeIgpVjMwt3Ya8KfGEzTJg8IFq3Pgvqp8M4ds5UoXzY6sZKtlaCkXy2C7-krmLZtYdrliD6YxPgPK9TqKz19HN33rous596ACKntE_cBWuWyhSjc13DoXh-UpWIB-kL5Kjv_nvtKZ8hs3RyjkyMjto6sIC_uI8uucl-eC3adnjD808EgKuVgYpTCA2PwAp5fhzFpQ51SrEqanETIalxUB9XBB9WuNZgHl2dzB5g7DNvayyKjrlXhgEYf8fnEZy7GAwKFAfwBVC5hidQzfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gvWfhGIJjbGejTP4hTRuZHZULNRzgvvsPPdQdbo_1EjnPA1xX4_pxqe5x52Ivo3-6Mv8tMlZELMFuHz0xdVrLvC9jxGSU7254p5HJiARuhRUib3MRLnDN8KaSnqsIHZ6dXISpovnkVxXBy9iThCM3J1EgDx61AxYB85HFewlNTWJE7xpW_bEJG814kZ-LIUDmovP277Cg0GdKmRYg9_sIXjzRqHifpUXxDGMaVS89u8DVEV5_LYOSvIPrTgkoqoUO-kFpXXC8nwGQ9ojWFiAWLlGQJXUn1ZXXdpnYwY3RYabE0doaPkBuzIg3WRtrf17A09XtVhskIQCwyeagrefBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lA5zxzOoHhTLTXo9RZzhBavGgg0X3Jg9Fdjxw0PlSzge4jfAqU1wMO80yWZYsTPWXewN6Q_XFl5im4AgQCQf6NHH-DuA0Wi1ssj6_iBK4-kDWYpSUMpbcfrHe62CEQ-F0Vp_BXJMOcCJRPFwM7TzRdQ_vNyv2f4CelLLqN-uj2opCCmgiiRcqy3wi1mchtQpqCDk90binE1YxODI_uyuEmTaJ46A_ZQFr96Xhj0LTpB5wslhTHFuf-qVigDAxsAUp9PwwKwe3qcoUI1bdmIQGT6LvbMYWb_qk2GNStmaHGf_f1uYtN6uzbAoTGnYlBuMTnOnsl3xOpUg7k8WSPHr9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سنتکام:
تفنگداران دریایی ایالات متحده، وابسته به «یازدهمین یگان اعزامی تفنگداران دریایی» مستقر در ناو «یو‌اس‌اس باکسر» (LHD 4)، هم‌زمان با حرکت این کشتی در دریای عرب، به تمرین هنرهای رزمی می‌پردازند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71855" target="_blank">📅 00:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71854">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4866c3cddb.mp4?token=uYb-jInxVmis9-H5lQM3AX2u-9qGV4D667iXEs9-Yfg08skuGSkJDePcEy-a8cdD5GbEC5gFUmSTAw9Xl-GEqVnr9W0DBhpg_JqqypyJIXSNgSQzkdhLsRV53zemCNfFnB-MeAjW6KJWwZJhV-6OO-FGYyebGwVizxIZ4obcXkh-mTzdZmt3sig1sSS42bApmyjpO6sVxaG2n_A_ncVxA9d5341bOZVAQOHP685-14hKnhtpEirJM1WAbMK_QzV9B2nYpaU0noENoXaWySpq85_uaZgjjcF5d14A3pw01-uv9uxUIKSxGMec_lBpnDKeMwk5hYpk1CMLehP5GhXTUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4866c3cddb.mp4?token=uYb-jInxVmis9-H5lQM3AX2u-9qGV4D667iXEs9-Yfg08skuGSkJDePcEy-a8cdD5GbEC5gFUmSTAw9Xl-GEqVnr9W0DBhpg_JqqypyJIXSNgSQzkdhLsRV53zemCNfFnB-MeAjW6KJWwZJhV-6OO-FGYyebGwVizxIZ4obcXkh-mTzdZmt3sig1sSS42bApmyjpO6sVxaG2n_A_ncVxA9d5341bOZVAQOHP685-14hKnhtpEirJM1WAbMK_QzV9B2nYpaU0noENoXaWySpq85_uaZgjjcF5d14A3pw01-uv9uxUIKSxGMec_lBpnDKeMwk5hYpk1CMLehP5GhXTUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آزادی مطبوعات در متمم اول قانون اساسی تضمین شده است.
ترامپ: ممنون که این را به من گفتید.
خبرنگار: آیا سعی دارید با ارعاب، مانع از انجام وظیفه مطبوعات شوید؟
ترامپ: نه، نه، نه. من از مطبوعاتِ غیرصادقی مثل شما خوشم نمی‌آید. به نظرم شما افتضاح هستید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71854" target="_blank">📅 00:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71851">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c6db95143.mp4?token=hO3RSWuA5yUQmjBE9DO6aOSrxue-21LdkBQvEHA_Ru7xSv-vCtvcuHdqB2Jub-OJ6dpsW_9oNKg0FyVKR6cfW7mTAgYI5H7OjLtCNKpWzyvASJQ8AG8UQS1qd0shcJ8huX2RoaUgpOHeHz1gUUkE2X3OVwPbcaYFulg33PKZkis0GzXYuqqhRw8zbuUQ0b-VWzAyINjmRdlUnRYolTpX8-O5KBsLElCTPZAqFfYHFpQPrQW5iF3IpQYkA_6uTVOWJkQb2-e6gfBOmZTp4duxZx3vjeTd-ZLlvwls2XacxquN0K7SvElbUm9XMO8RFnKRNnVY8V2kTWIhsANw4B1coQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c6db95143.mp4?token=hO3RSWuA5yUQmjBE9DO6aOSrxue-21LdkBQvEHA_Ru7xSv-vCtvcuHdqB2Jub-OJ6dpsW_9oNKg0FyVKR6cfW7mTAgYI5H7OjLtCNKpWzyvASJQ8AG8UQS1qd0shcJ8huX2RoaUgpOHeHz1gUUkE2X3OVwPbcaYFulg33PKZkis0GzXYuqqhRw8zbuUQ0b-VWzAyINjmRdlUnRYolTpX8-O5KBsLElCTPZAqFfYHFpQPrQW5iF3IpQYkA_6uTVOWJkQb2-e6gfBOmZTp4duxZx3vjeTd-ZLlvwls2XacxquN0K7SvElbUm9XMO8RFnKRNnVY8V2kTWIhsANw4B1coQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
اگر قرار بود رأی‌گیری‌ای میان «کاهش قیمت بنزین» و «اجازه دادن به ایران برای دستیابی به سلاح هسته‌ای» برگزار شود، نتیجه آن یک پیروزی قاطع و چشمگیر می‌بود.
مردم نمی‌خواهند ایران سلاح هسته‌ای داشته باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71851" target="_blank">📅 00:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71848">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MJi6n9NXkLD1cLiweXUywjlexVN2xnQSCJlBW_xYHR26eicRI4nh8kOtqLxLhw-FqIILy3JvxuTj3UlqEPiMhRtphD6r7UEemByOuD_d-fiaL8RGGVLX54J88oDWuVDBWI8_Im5jMUKhs4i8ogB4EzLOqa524SDt8jmbZLnAlVOC7ZHn87-IQHz6Qkh5kvzSVUEYuPi7JKK0gbx2cUonpoXbAhxVQCxra2jvQW48LWynBVapUg7pu6AhGKfd_o2lwJCq7Dep7aQLPM83qlqBKAXhxnk8-8Lh9rYO4-uDJenk_SwJ-zZ6Wij-YuPLFTr8a7jD3UZxidzB02Q4mJ_IRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VvdtPSjjq5Afip65EUr41HqEmiiDw6Qc6JYs-vvIgavHI3CtHW4dC8pjHpzqj6QDjBBBBrREWwnMQiluPPiXxE6K6VcNRCle_5n_TZjSIpiolQySneecOnFpDfI4qDWWIG46CORIy1CpaEGEZWK-RckfBVrfy8Bay66OhiBNNDNHfoqbEmB4CCeqP3N4Eq4IPx95joDZdZ7u6sTSqCs8T1pzXN6hV_xSDhGiG2MwnrcaguOQWixHeJ_Le3_BTo0gzhm23tM2T5T3hqgnPW2gU4aUasPMcNRN6GLAyh9689TJzDSlpiyeliZZw69nXc3HnUz5rLkasbQ4zIKzflzhpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eON10xuq3XaEcNmji1BmoKHOGesQmfCp4rubPGrkWI-1aHNGlZXrlc_-HezfbG7tPRdNsj5ne6_KNIoZ6bBZngCk5d_LXyRJC3ZwN0zxWa2PSyPd91X0_VFgHC3B9xGmD-_4S_bpv9veJV8NFgcqB1isBiAyODKwuTImq56n0LbN2Y86If9CKYBp1tee3EAxwrPK97OzqChSq-dMTVonQe8sDDkOSGZhnqqVjYNctkHuZxj74PZzgmfHIQR-I3i__QDg8Lq7UD8qzU5cUNZfnBwH2yGyHgwVuOPZ6l8syPvlKxHZHEwga-_e1Vgu0Y8JZwnxCBPghQuMPFALQDIXXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گردان های بانوان جانفدا تو همایش امروز:
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71848" target="_blank">📅 23:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71847">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7102741190.mp4?token=UXV7EyZeZbN7gENggLAOoRZFibMfQ_v1zPCCTTnlisJbHffqzGNPFlq4pTvEQhT3nfNMpVNy8PsBaxXpjDza4wko7zCLM1es_vAGEQMkNmtBw41H1oWwVDFV-un7NV6EhNnjci2oE_9tnaBY4ThFebV_78zv8z4GBYnufIlFZbbTtz-uLpb1lptB_1A8hZv4IQGclDtLxRAUXBQ0-VpYr0DHa62Q1qG0F5djISm_cU83R2F8CgqT_XJzWRAKSkLF5NEs6fsaNXUF99qNMn6dd2_MPqQngURZyZfG29zEA-z5i8o-mtVb8Fu0hGMqCJXP_LDCfaSnEYb_AZ3IJJvBMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7102741190.mp4?token=UXV7EyZeZbN7gENggLAOoRZFibMfQ_v1zPCCTTnlisJbHffqzGNPFlq4pTvEQhT3nfNMpVNy8PsBaxXpjDza4wko7zCLM1es_vAGEQMkNmtBw41H1oWwVDFV-un7NV6EhNnjci2oE_9tnaBY4ThFebV_78zv8z4GBYnufIlFZbbTtz-uLpb1lptB_1A8hZv4IQGclDtLxRAUXBQ0-VpYr0DHa62Q1qG0F5djISm_cU83R2F8CgqT_XJzWRAKSkLF5NEs6fsaNXUF99qNMn6dd2_MPqQngURZyZfG29zEA-z5i8o-mtVb8Fu0hGMqCJXP_LDCfaSnEYb_AZ3IJJvBMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این خانم تو بخش پذیرش یه مطب کار میکنه. حالا به یه بیماری برخورد کرده که یه فامیلی شاهکار داره و باید از بلندگو صداش کنه:
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71847" target="_blank">📅 23:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71846">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=syWRo7AhW6Bgpu4xlM6YWswxtiWhzSbUrG_BgWWDVOapgSlhk5n1TFjhZPJufBsutZ77RUv_odjxltsa-HtiL0xn_I4x0xYOGqoZkLZhCsTPqcucgHZaiEq1OwRPGh3S64BXm0GMG7fc7kQFvJlKfctNdAo4TO9KAkmYV_gXuKK2N3mM0PzUScZpTXQVph-KL95Ty6bzFtn6SSVWHLqh6nDRa4ly1iN9RwnKP9xWMHmyN2wcwy6P9i4DqzeKXFl154M2kz3ghKw_UlRqZcKeN7zY9gVhugMsxO83skRwUX6yPsqFLiPwD1uTCVlNH8TcovpcXc75gX7vqDq51KmgCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=syWRo7AhW6Bgpu4xlM6YWswxtiWhzSbUrG_BgWWDVOapgSlhk5n1TFjhZPJufBsutZ77RUv_odjxltsa-HtiL0xn_I4x0xYOGqoZkLZhCsTPqcucgHZaiEq1OwRPGh3S64BXm0GMG7fc7kQFvJlKfctNdAo4TO9KAkmYV_gXuKK2N3mM0PzUScZpTXQVph-KL95Ty6bzFtn6SSVWHLqh6nDRa4ly1iN9RwnKP9xWMHmyN2wcwy6P9i4DqzeKXFl154M2kz3ghKw_UlRqZcKeN7zY9gVhugMsxO83skRwUX6yPsqFLiPwD1uTCVlNH8TcovpcXc75gX7vqDq51KmgCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکات عجیب مجری شبکه‌سه برای توضیح عملی دفع سنگ‌کلیه در برنامه زنده!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71846" target="_blank">📅 22:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71845">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46fca26fda.mp4?token=eoSdsAbSWNZg2qN46Reln45f6EqVQkR6O-HE8S9Kq15xYLI71K8Sca1gDhCvfIFYwpBZNirlaBMXtqk9AScaR017EAjQB3q7_58Nh48P1A4xsASgk1GHM_tM4GegoqSehe6HMyigwQbuMINDO5W3o0J6gN5PGLLSqMeI0KG9ZsF0miJBKc-caiET-HB2mcpkE82BRKazq3Hr36_SJL0lcGnNaPMRb6g-xB_zPcYY2L9O4C2D55gbl-KetwUXnZV9VtR5x_MbRqslSqc5R_jy97Fl3RDnNlq2nAJuUlNIRialbiDURHhY7dCAcrL38ZETodp_SgjNF3QcOQFc0ZYIDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46fca26fda.mp4?token=eoSdsAbSWNZg2qN46Reln45f6EqVQkR6O-HE8S9Kq15xYLI71K8Sca1gDhCvfIFYwpBZNirlaBMXtqk9AScaR017EAjQB3q7_58Nh48P1A4xsASgk1GHM_tM4GegoqSehe6HMyigwQbuMINDO5W3o0J6gN5PGLLSqMeI0KG9ZsF0miJBKc-caiET-HB2mcpkE82BRKazq3Hr36_SJL0lcGnNaPMRb6g-xB_zPcYY2L9O4C2D55gbl-KetwUXnZV9VtR5x_MbRqslSqc5R_jy97Fl3RDnNlq2nAJuUlNIRialbiDURHhY7dCAcrL38ZETodp_SgjNF3QcOQFc0ZYIDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته شده بعد از انتشار این کلیپ، ترامپ از ترس ۳ روزه رفته تو اتاق درو بسته و فقط داره می‌خنده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71845" target="_blank">📅 21:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71844">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vmIY47CgAkEY0b4CW85BQbSfWgA9LgEjY1PtrxaWOYHkkuXa1iL8vgy5Zx8QgRvU2gcZbqtBoTxaRedrazrqsUys6baIscyxkIy7j1dZvCCV1KWzBFdvwDa02Djba1RblHWix5AvUl2inLq7CMRLZ6IXZmBo6uZXdklcv-P6YO5N-v_6qNcKnQyQbW2flvix8odE5omh6Qr-YbA25TZJLzHGwIUU6tdy5OzrEfp_9oS2NSijGY4ge0ga_un48zXfyxiwGAo4hifVZpIOQqFPD-2JrEAL6t6MgAzmbV2ULixjezOxf6Lz6iIiXigCksgu0zcsedI9xCkZQFL182_eRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز September 18، روزِ عشق اوله
❤️
این روز بهانه‌ای برای یادآوری و زنده کردن خاطرات نخستین تجربه عاشقی در زندگی است.
به عشق اول و آخر زندگیت تبریک بگو و این پست رو بفرست براش
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71844" target="_blank">📅 21:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71843">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نیروهای «ارتش ملی یمن» (تحت حمایت عربستان) تصاویری از انهدام ۹ دستگاه خودروی نظامی حوثی‌ها (انصارالله) با استفاده از موشک‌های ضدزره (ATGM) در جبهه غربی مأرب منتشر کردند و مدعی شدند که تمامی سرنشینان این خودروها کشته شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71843" target="_blank">📅 20:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71842">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y53n_ShW7Ne1ctv7tFivRNHZxepEeF5CnMdRGfUzsZz2MvNvSZCV4WpUuelMqNflQG4tm1EOAja0wYFQB1_JuAbQkjmVyzGZadoS8rUenzoWHwjM4M6CgOjUAeEUtc_0OPMQgXW49hMQY--7rmzPNoN8fXGgoAmlY7tVSMEohCgU3fzIfKmSSHNrwoCryTaQ1PCPAmHLioAC9hF11pfKHOss6x0vlUF2GI8CF96Ksb_s1SL4xMJVAE3i2bvtB-00PczcDl34dDelgP85kE9OQbeirguMFwI2GKxH_v5Dap3hfPVt7uyxzQkETZGvUQwmn9JRzPMcVMNpiBasUpilxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در پاسخ به پرسش شبکه «نیوزنیشن» درباره اظهارات اخیرش مبنی بر اینکه احتمال «نابودی» ایران را بررسی می‌کرده است، گفت: «باید دید چه پیش می‌آید.»
ترامپ اظهار داشت که ایران در حال حاضر خواهان توافق است و افزود: «اگر توافق، توافق درستی نباشد، حتی به آن فکر هم نمی‌کنم. اما در حال حاضر، آن‌ها می‌خواهند توافق کنند، چرا که در همه زمینه‌ها در حال باختن هستند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71842" target="_blank">📅 20:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71841">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ به «نیوزنیشن»: آمریکا با حوثی‌ها در حال گفتگو است.
حوثی‌ها نیز مایل به دستیابی به توافق هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71841" target="_blank">📅 20:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71839">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429ba373cd.mp4?token=DzA_0AijTeWQq2uTky5WF-C48vN5FfuTD2irS55m9dWQrofpaqzVsHTZGzVWi22ofDJNc-WUlHnoRX0kMcW3L_YDd8sNQVY6BTzzQMnV363d-APiMVFl7WbcbdZQWuDXY7v2ZOzubxnKOw1b_83-24L6tSbdfoT1Fp7M0E8HSpVM0rxx8prM7U7MoENXIXoazMIFvhKykBOMYB5ohb5XagEu7t0sbYDaDuq7ROnfcly3yWCGqgtez8EVIsQdBVCuNJDI87tVk00ZSlqnMKuptXYW2Z2eUAHwN40cdPF5UNIi-zY6cg_f6ERHlvxZNn-gArzukJYvB6QLuI61FtfPVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429ba373cd.mp4?token=DzA_0AijTeWQq2uTky5WF-C48vN5FfuTD2irS55m9dWQrofpaqzVsHTZGzVWi22ofDJNc-WUlHnoRX0kMcW3L_YDd8sNQVY6BTzzQMnV363d-APiMVFl7WbcbdZQWuDXY7v2ZOzubxnKOw1b_83-24L6tSbdfoT1Fp7M0E8HSpVM0rxx8prM7U7MoENXIXoazMIFvhKykBOMYB5ohb5XagEu7t0sbYDaDuq7ROnfcly3yWCGqgtez8EVIsQdBVCuNJDI87tVk00ZSlqnMKuptXYW2Z2eUAHwN40cdPF5UNIi-zY6cg_f6ERHlvxZNn-gArzukJYvB6QLuI61FtfPVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی روزنامه‌نگار و فعال رسانه‌ای:
ما انگلیسی‌ها رو از ایران خارج کردیم ولی الان کشور افتاده دست چندتا بچه اطلاعاتی!
تشکیل مافیای فروش نفت هم از دوره روحانی و توسط زنگنه (شیخ الوزرا و وزیر نفت سابق) شروع شد.
درحال حاضر چهارنفر دارن نفت ایران رو میفروشن [حسین شمخانی، روح‌الله رضوی (دامادِ سخنگوی جریان پایداری)، علی بایندریان و محمد‌هادی مومنین].
پسر شمخانی(حسین) تو این چند سال، بالای 30 میلیارد دلار یعنی چندین برابر ثروت ترامپ فقط نفت فروخته!!
این چهارتا فقط تو فروش اخیر نفت ایران، 1.5 میلیارد دلار پول به جیب زدن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71839" target="_blank">📅 19:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71838">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1uW7xJiBqHyGJeHWu-PoNC_mABd7mLjEQmnJjJ-of2W5fpqUTODLtOPLzZM2xe8XyU4PZx-z9KKyG-bYJj0dmapAs9_mG9aJYH2Q43fjbnWaMIjv2HKhDrX1W0jN2SZuARORIXhQ4dfgnovGtOeyCsr44uh9pHRK4rqd0GQsRoR4nRaPQzDd3pJZMxk-4XVaKM-cofc_fODR-IeHUFsrfrk6zJvPXsJ1CpA8F2xXPVSTkOddDCxC9edkv3YRCA5j7JqutkDuHHYI3jdlehAGFV0pBjKb6-l8d7c5fqcxk1t5FJ3KKC97_R3bdgk49Bsd15E0kZj-nF1FDuSBfvxxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب تلگرام در پلتفرم ایکس این تصویرو از ایلان‌ماسک منتشر کرده و نوشته:
ثروت کاذب:
🛩️
💰
🏎️
ثروت واقعی:ممه‌های ۸۵ ایلان ماسک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71838" target="_blank">📅 18:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71837">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/915a75db7b.mp4?token=ZqTtpyOsYG3c5VHOHM5_lni70fplah0gKl8DpTF4G_4UIPFdSLd3K8GkjVgPar4U_V39RqrIlOnkdDHV6IwzVp_EqXX13_hu0AtuT31XWIpEE79kIqw-BywSEXGxC-TP4a00jMTf_wTX6W0d3f8fftHxOiJ-68s-eG57ksUIohZpo5a2QzbUDyB7crCa7X1vkUQco6xMmPGd-VLbq4UpHPFpDHuvcBhvGQPK7YyJY9VqwHE8GdZSKBTb7q-6a16ZO-L8EQty6_auydz4CNMwdIGOoDAGrhO7X1-Lt9vmRDkqt6BGvXp5O-oqOJpYA6cuGiEG7KzmX3NkF2MW03sOTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/915a75db7b.mp4?token=ZqTtpyOsYG3c5VHOHM5_lni70fplah0gKl8DpTF4G_4UIPFdSLd3K8GkjVgPar4U_V39RqrIlOnkdDHV6IwzVp_EqXX13_hu0AtuT31XWIpEE79kIqw-BywSEXGxC-TP4a00jMTf_wTX6W0d3f8fftHxOiJ-68s-eG57ksUIohZpo5a2QzbUDyB7crCa7X1vkUQco6xMmPGd-VLbq4UpHPFpDHuvcBhvGQPK7YyJY9VqwHE8GdZSKBTb7q-6a16ZO-L8EQty6_auydz4CNMwdIGOoDAGrhO7X1-Lt9vmRDkqt6BGvXp5O-oqOJpYA6cuGiEG7KzmX3NkF2MW03sOTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس نمایندگان آمریکا «قانون لیندزی او. گراهام برای تحریم روسیه و ایران (مصوب ۲۰۲۶)» را با ۲۶۲ رأی موافق در برابر ۱۵۹ رأی مخالف تصویب کرد و این مصوبه را برای امضا نزد رئیس‌جمهور ترامپ فرستاد.
این لایحه «ناوگان سایه» روسیه را هدف تحریم قرار می‌دهد، اعمال تعرفه‌هایی تا سقف ۱۰۰ درصد بر پنج خریدار بزرگ محصولات انرژی روسیه را مجاز می‌سازد و «قانون تحریم‌های ایران (مصوب ۱۹۹۶)» را تمدید می‌کند؛ این موارد در کنار سایر اقداماتی است که روسیه و ایران را هدف قرار داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71837" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71836">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71836" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71836" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71835">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMHEVexqEL8yeqGgmvXIe13b2sCa1lePCjdJQWjkLjHiESKJ_DE3eKKaV4JLlDvefYJkxcGOnhz3DDSE-z7kMOLbpjirytC9uq4PZOSoVZIRl_LKBFSmGDN75y6_0W0JX_71Iw9AlHJ_uJesqoKt0YsQd8c4PBPYVLGe48OAFSQyk4RwjseKlfioJ3hpxxQW9zeRlS9h4eMWWj3qQe04hzxYygu-Btz6hI1r3lw1Voo5KmxMq8RkX7ztcSHdtxwJ2w-lclTOAEkP-YwBqKpXfWzYh-zp-Amha74Cw90k2jC06P_EFnRsUN6xKlZpel2LRNnlGdErgmB4C6yPJr4jsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71835" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71834">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b71f8c82b6.mp4?token=OyLb88AjFwuXW6-p7bMe4w2M-erllC2VK0j1r9sY45uOI28Y0RoasNF8ytG_C99SvztMtIgY610nzqKI9QPvSAJM6IvkitB9rFERIQsM1e-o281oyeueg9PY5eiAnHXDpE6LYaJWYybqxFSa1QvcDbJML_EP48lDdOGhHnPUmAvvEldE4DeLnWSRZY2Qq4tEyb7DxdPMr_blVGSRuDGPGGjOEgWV-pxttbxfmSLFzY82-jrbtG_SflucTgNn0MDhi0CsFfFVO9jZ2kPnd0qmztSROxRqjrxQuApd7rDtELFYR1UDtV8nvMnWHATzM8KXDAsjy4mgDfPXp3Iq0gITVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b71f8c82b6.mp4?token=OyLb88AjFwuXW6-p7bMe4w2M-erllC2VK0j1r9sY45uOI28Y0RoasNF8ytG_C99SvztMtIgY610nzqKI9QPvSAJM6IvkitB9rFERIQsM1e-o281oyeueg9PY5eiAnHXDpE6LYaJWYybqxFSa1QvcDbJML_EP48lDdOGhHnPUmAvvEldE4DeLnWSRZY2Qq4tEyb7DxdPMr_blVGSRuDGPGGjOEgWV-pxttbxfmSLFzY82-jrbtG_SflucTgNn0MDhi0CsFfFVO9jZ2kPnd0qmztSROxRqjrxQuApd7rDtELFYR1UDtV8nvMnWHATzM8KXDAsjy4mgDfPXp3Iq0gITVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
این جانفدا‌ها چجوری میتونن به دولت کمک کنن؟
پزشکیان:
ما باید کاری بکنیم که چرخ کارخونه‌ها بچرخه. برای این کار باید مصرف گازمون رو کنترل کنیم، بنزین رو کنترل کنیم. با همون حمل و نقل عمومی بیاییم بالا تا بتونیم دشمن رو ناامید کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71834" target="_blank">📅 18:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71830">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fefe1a2487.mp4?token=jISjJcP77xV4tSEP7uXlUke8_DHMvL9Ve5bahpXJ7QRIWyfP58H3P1c_W0g611NSPd3-7iUHMRAjXxUxbq3WmKQea4-XoFIzQ3VJ1E7eU3Yms2JRPSN0yz3IwPmpA96kJ4-mI7F3LjMe1sggcdejJou-SO2ixN0XAT7R2d24u9uKFqFkyxnrNC9lbvYj2byZtdrOJa8Kd3EuV5NldV4jAHFBfjXPT2JrqMAtsXFlzihW7hE2Jl5mKKncw__nuptY45xvSHvVh7aIzorMqhfNJDKlXeab-iEUrz17CRP2ZxNbXxzP0RSrK7WQc6601QhoZ0j27qi2P8crNi7kB978Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fefe1a2487.mp4?token=jISjJcP77xV4tSEP7uXlUke8_DHMvL9Ve5bahpXJ7QRIWyfP58H3P1c_W0g611NSPd3-7iUHMRAjXxUxbq3WmKQea4-XoFIzQ3VJ1E7eU3Yms2JRPSN0yz3IwPmpA96kJ4-mI7F3LjMe1sggcdejJou-SO2ixN0XAT7R2d24u9uKFqFkyxnrNC9lbvYj2byZtdrOJa8Kd3EuV5NldV4jAHFBfjXPT2JrqMAtsXFlzihW7hE2Jl5mKKncw__nuptY45xvSHvVh7aIzorMqhfNJDKlXeab-iEUrz17CRP2ZxNbXxzP0RSrK7WQc6601QhoZ0j27qi2P8crNi7kB978Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسجدی در شهر کوهات، واقع در ایالت خیبر پختونخوا پاکستان، هدف حمله یک بمب‌گذار انتحاری قرار گرفت که در پی آن بیش از ۱۰ نفر کشته و بیش از ۹ تن دیگر زخمی شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71830" target="_blank">📅 17:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71829">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دقایقی قبل صدای دو انفجار از سمت تنگه‌هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71829" target="_blank">📅 17:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71827">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ارتش اسرائیل روز پنج‌شنبه اعلام کرد که نیروی دریایی اسرائیل و یونان دو هفته پیش یک رزمایش دریایی مشترک در دریای مدیترانه برگزار کردند.
این رزمایش با مشارکت دو ناو موشک‌انداز اسرائیلی و دو ناوچه یونانی انجام شد و بر تقویت هماهنگی عملیاتی میان نیروهای دریایی دو کشور تمرکز داشت.
شناورهای حاضر در این رزمایش، سناریوهای متعددی از جمله اجرای پروتکل‌های اضطراری و همچنین شناسایی و مقابله با تهدیدات دریایی را تمرین کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71827" target="_blank">📅 17:01 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
