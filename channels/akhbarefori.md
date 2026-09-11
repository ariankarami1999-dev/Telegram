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
<img src="https://cdn4.telesco.pe/file/PvhePQbDwlmvTt6lD6Eoj88CkRUaojBHP4hmNUDqrZX0aUfDJ-_sCcjwFVNgstue2JXS-af4FWDkviMDnnWmHIY_iRyU6QkqiLKR_yvzNXZ71oz6-nERdoL1IzNqZh-9qTG8X7r5WSTBK4_i3B-Z-cy7ZPPassBiUVDxlmYitNbiV9mFknLJZKq4hWuIBkd32JH7ic9BCZbkjm5S2-KuQPzaZ0NtYVAE1ujdVHql83dA2fznMe4OTS7pET7CseVDuWH1kUk8FcW3ZrpjKHbaF9Tum8NvmD0GV6viddBHmAXy9Mfse32r0a-EeZd15t6595P37RSuL2_-i7DzimaX5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.26M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 09:45:45</div>
<hr>

<div class="tg-post" id="msg-688937">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/469234ffb1.mp4?token=U8-tWbMvfzU_suHf7sToelBGjTsWFAsRNk5mkZ7H041W1x08mH0ni-LkJO-j_PXWGaTYRaIRPcek_25IARYWsKE2nkrsMt-e1VgxuBvjcLXeObI53fMIYLi6Zf2TjAgaDTlzux3CsM9y3jPbqNDH98suPAw9fMQWlartHk2JxQV1YZq2Zz7RWr0wCTADzz4AGQx_ldvKuCUnzGbRIoKUoCfvYXVnuT4KNXw-E47AmmAGkFskgNr9pcmctz-LiAcsHbhk-14M3ndZCesbcfZq4dYfoSrWWOmcirMGr5D3UenCMMUs7b_sHMZ5LLOekgmv32OyJtMOge2OYgH_WQwfoLVpOFdNuXXyzeXE3OCM81JkOuuZNosfTk2e7wTd28MchYZYVGqDicdWmtPixUFb_ozQgYf6NSv9Jp-_SKvt33E6kaLhXx0R9Zf25tS50zmWfedrlsCXnKnDOY--RD8t8Igd3Wdmu-4zbGBSLQzIIZ_l32AORSDc2fXqqrDe3DGSqss-pV7Xd2bi9Gz7d5gukygkzgm9NGRg-25uNcFcFL5f_WbIJtBnPGdEC-w5DxlDJ9BZc1EhOXJwQPeuw5bKgsMOVwfgXqxwcBrFtNeRUhqA8mUFouZkaZVQbVf8yrBXj9EE7Np-TMUtVXbI3bdiJTR2PIXH5dfIZx7koh43Iuc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/469234ffb1.mp4?token=U8-tWbMvfzU_suHf7sToelBGjTsWFAsRNk5mkZ7H041W1x08mH0ni-LkJO-j_PXWGaTYRaIRPcek_25IARYWsKE2nkrsMt-e1VgxuBvjcLXeObI53fMIYLi6Zf2TjAgaDTlzux3CsM9y3jPbqNDH98suPAw9fMQWlartHk2JxQV1YZq2Zz7RWr0wCTADzz4AGQx_ldvKuCUnzGbRIoKUoCfvYXVnuT4KNXw-E47AmmAGkFskgNr9pcmctz-LiAcsHbhk-14M3ndZCesbcfZq4dYfoSrWWOmcirMGr5D3UenCMMUs7b_sHMZ5LLOekgmv32OyJtMOge2OYgH_WQwfoLVpOFdNuXXyzeXE3OCM81JkOuuZNosfTk2e7wTd28MchYZYVGqDicdWmtPixUFb_ozQgYf6NSv9Jp-_SKvt33E6kaLhXx0R9Zf25tS50zmWfedrlsCXnKnDOY--RD8t8Igd3Wdmu-4zbGBSLQzIIZ_l32AORSDc2fXqqrDe3DGSqss-pV7Xd2bi9Gz7d5gukygkzgm9NGRg-25uNcFcFL5f_WbIJtBnPGdEC-w5DxlDJ9BZc1EhOXJwQPeuw5bKgsMOVwfgXqxwcBrFtNeRUhqA8mUFouZkaZVQbVf8yrBXj9EE7Np-TMUtVXbI3bdiJTR2PIXH5dfIZx7koh43Iuc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سنگ کلیه چطور به‌وجود می‌آید؟
مهم‌ترین عوامل را بشناسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/akhbarefori/688937" target="_blank">📅 09:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688927">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pnfp_SiJ9QTuVn-YXeIeT6SnuQbIpqOeGYC6HBubqX8yucaJyH4JUmam1SK5stpNJMU3P2EXztXNuPoqoYbnt9sQMhbiZPc-eRSBdBqiMx8AgUUSuLVnOUlFY1N32GbIHqk9RHItlCfa5tyME5--qW6Ol38xl1dlgvw6QQ4tN0nVYFmko5HZLOh7q27gCT0TE4gUqWXJBfEHLh9Nc52fegjI9_YBOvfIgNXO4pcT-PuvJ_iUqQlq7niwg3-ZJtAPegwYg1pzue_ypdEeeMPxkrq-8S7ZvJtTD9pqLuK7YP5xI0sbOcux8nwHKSeL4yD959bpZizKjg0-YC5AR9wAwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LcGQ44Rr-oY3_maI-DjWrDDMikBNq1-63IDqB7l-hv9-ulkwzL2V9AsZf4FODTvmE5mZmoE0trgFYYZVmZyUxduT7mHklm06Z1GUXgUAS9lnp9YE3YhHuRu4zILGH6FCSgMNMB1_XcxFujsHE81bJMh-iGIMTbQRR59ba2S0FcDRPtsn8zq1Z1u5Y7vxOwbr2TH2dFjv0hQT8YmBq4wrz-d8lojvSDMoNE2XWNF99tiNDYfRhXLaOHu-9ZS2TMogGh4wulSdGORMKPrW-YgCTvLsQAgQ5a-UcYXcj4K-nLHEVo0a6tJtkdsBZzHLxkhTJEUnbToHKYKACkL4MbRzGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GrmXGmI6Wwfuyg1T314l-3GnyBPlXocieiC5wvmqVKnVXHlg1g0GujqzFo0SNFq2VKNNaI4QFHJsPwB7Hp1_2MJj7TOcImRp0qKWIG5zSA5bLbvYAdbphxAreu6D7Z_WFhmKDkDiKtRc5j9Cr8u8evt29gQmjCXalpDRREm_yC8Y-Kauos_3VBeVAJYKEEkg2n2q6hdHYVrzszg4Sc_OwyRL55V2UlfczAzhyltFPHSlS_93GSA0jRiDzV2xKkHtDGmoSe3IT6f6KoL4v_On8iYRLXAsXI1dHZXiHzF6BRDo2VjCrD71gV7wprNv21U133_FQIYEap3oueicPomK6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bddv7sT27vz_bh3D7lmEzVy8fItLUc_2voBSqtL_xXHghV9LpcG_mNT9-YFI4FiMDEOAPfKxzj4WYmcuf476ltR0eedCRre5SC1VZG1XkHl0D63bwLcW-tWfT56Z3JYPwc3WDhQHxpPZ4CC0mwycL2jSqkHNYysmx27FQj3dI9sF7dP8PwDP4QKo2KwZZO47_4D3aaU5gBud5-9BUZPDQYGN-VUnFt_uvR4VxKgyvkRxebEW7irHWETCk19kqtBVqG_01cdzrYCbr1Il9nqzraXjBGXiSYVsIXCXneh1swYqg7jesqNszwk32_BquejmCuYyEZoDkJeNF_SsoZhJcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8OdSrUYQYyNuB3M3ZoW_MwZKAkfrCLs-9jjUY6nIfSs_jL7zj--vXlj59oagIGYLJbilvtKslQG6-E-p4-7VEcZNNiC6KBTLP68rV2bBkV-knyWa07DUVIOiuDokz40POgCUkxRw8TWEpW1f2oR1SI99fyz0w1oYn3w4XssZQ5nEwxk8NymCPtGUOgP5N3nJN5b6eer3RrnEoU4V5j93QWhlGp_UnNLsfgNT901w9x3YCFArSd915C88SO7flhXQNH9NO1Guph4RR8jZj5rSquujXvKk7NUSiJme-kzyYryOoFNAIeY6k_dBpyxT6dPqtBWXx7EKktxFT5ckzF9Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mviliLIsc5OCscXegVgWPQpVYB-YGwjMflmJw_42qx-bC8vt-D1sM2feamSSs8bD2_7seS2IEAAkjDYJj6tkvy4iaoIf7MdtzkQNOo8-qFCV--YTbGmdsdxm7lrbUg_L1kJiN1tv_8w4PX7XYduqcV__baldXEZvycco8pQcxWKPeFnaeABcDxAnufUmcAiDgnR7WADqC-dCd49fjzAe8XflR5XvYwGMuVT3vkSnrdCpJ5i9ybOGlW9bsRWpGi0vmtVj03Ds8KdV62bFwgZljLzD6ILlcaKdhSj6vVxWC2nbQJri9EzVq-17tO1eheTU6vZXUtvKVd3I59NMkH4H9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMoeUMAMaPHSMnrz3RYFiUWAR0XQYPkKH6tFGwccWIONBV5zR_TtV5WIP7Plc1iDDvofG-iBPBmj13jbhIl2NbfsuZDJnyWcEdfnruki-tkCzfFkH59Z8gw7XNqKfrO4ebUcZqSElgTFyHUJEPkATVMnV4rHOvuxqMDV1Tag6c0PgfKMJXKKyPpa6V6Rkp9mErwnU9lS76xPzfFu-eJX-q44QUw7kuurlGG_EtFkgFwOZ3De1IclKLqEzvk57GbrzhnJJDHJLKlTGbbHrHGRjHbyNhgfkl6FsWt2LJjh4bSR7OqdjFeXHMCBWr4og9gkBzMitNQs8Pu-NeEdJI6SEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I_ISQ_ji3HYqOWqe3haPYdkIbfyks8-72Ss6QkRAz25_nfTwmrwNTe9HNYMmENv0lbR8iYxy78ZgBTeFQcFI2W122pE9XWdN5XIcx0BpXEfF4QMVlaTlTpYnEMx9ZmoPANy9vl8z6an_QqC77SrL2cnRcQCVqKkcgP9bekiY1Nlvrb4lvVB1jFaJQ2aABSbD1-Kavu_Gc7Xi2llJTtQcYNKne2xzcVS9smns9qP1j_tRhelplgSKpYuWYeuZah52T270dWOwtyxmjSZz2SsUxcxzunq5WOPYsgSTfnaDNrf7GRL-5t4D0ljALiQNMvUnc2fq3HitVEjNGL0OTj0dqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CGQaUqowfFvBc-VDarPCB5LidLtT1oAuLS2OGVi5nc2SJn5T6SGnSHcmNbI4PjZAh1mdq_MhUshf9kVJ62IY8qplQX50vdUsWDEARbiV95clMzRmTiyJJsYSQTMvJLWSMNeS69lHy8gBVrlUsJZgaFd8BFHi_xGOQrJLryOTaWdQGEhcLVXnsIBdI3gf3T1uSj9c5RG5SZStXNwHVTzKxKkLODPOxL6Tr9ykeXuIxKCqQfVilifOncLaKegtd3JOleC2LE3REMioq56KNdrX4yy0p9qZkFp3OgZQcKVQR_-vYORafZnHuTrtaWZxqN1l7dbjY_QAKHU6ZX6qKDuXxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YwPyeeWcIlkI2F6b5VzqEssTNBLw2cpmE43VEzl8YyXFF5fx4lK9WFI1ZOaTJBdhRcsK0OT26cQeantanYJelUUseRfz9rU4eNLp1eADnT_Hdb2JXLMWB1rd98PblM7pQD2ZmS4sbdjazS0_MqnMt_dTHinPFlGVIJD-YcS1TRYSZjA6ARGVeyYV51HDsFB6v5S2EQpoLF3e7aFoC75-q2a2JD57lMafpkQ5APUUXLhT3J4rTSv0TLB7gcIw42-WehW-7rwY9qPEt9jJcSK_w4tpLL6V9hCuPXWs8tpxs4o44DER09fvVg5foVBQn19srlu2wcpsurD7Ca5Rf_3NUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چالش‌های شروع سال تحصیلی
🔹
انعکاسِ مشکلات و دغدغه‌های  مخاطبین الوفوری برای شروع سال تحصیلی جدید.
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/688927" target="_blank">📅 09:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688926">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
رئیس سازمان سنجش: نتایج اولیه کنکور اوایل مهر اعلام می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/688926" target="_blank">📅 09:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688925">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ادعای آکسیوس: محمدبن‌سلمان از ترامپ خواست مقرهای نیروهای مسلح یمن را هدف قرار دهد/ ترامپ این درخواست را رد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/akhbarefori/688925" target="_blank">📅 09:21 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688924">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
رئیس‌جمهور به‌منظور شرکت در اجلاس بریکس عازم هند شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/akhbarefori/688924" target="_blank">📅 09:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688923">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
گوگل اپلیکیشن جمینای را برای ویندوز منتشر کرد
🔹
اپلیکیشن بومی جمینای امکان دسترسی سریع‌تر به ابزارهای هوش مصنوعی گوگل را فراهم می‌کند و پس از عرضه نسخه مک، اکنون برای کاربران ویندوز ۱۰ و ۱۱ نیز در دسترس قرار گرفته است.
🔹
کاربران می‌توانند با فشردن هم‌زمان کلیدهای Alt + Space در هر زمان، جمینای را روی پنجره یا کاری که درحال انجام آن هستند باز کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/akhbarefori/688923" target="_blank">📅 09:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688922">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7LxH98NySFbCVfXxT4IXthT3zRDJCJiixgZB_5bPL8Hb6rcuccfg2YpCC53bF93o378mBtVDAzHwRffcU7aku2BYM_UGJYXLmo9YdKbY2c10siMm_cjBCx6FizzJA2srUkLGWuXTgIWZLx8g_6SJsJ3LyZ0iANIWtHjkLTi9ocVNTaU4LgOzE9fqHF4OiX9UKXQ_JXXl-p9hAMEU4un36vMJCRk4BpBYw8dyMFBEMl1hMLz-jZWoxgUD_hAq0-guYfGoHDqh1PnmR6PZ-LkZHkEFUKn_0IkuQpOAKdAwt1eR67v58uC0CW9D5jdMq9-fOkNJqrnzr_rH9K8J5Bs8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری بی‌نظیر از شاهین آبی با ترکیب رنگی خیره‌کننده
😍
🔹
برای ست کردن رنگ لباس‌هاتون از طبیعت الگو بگیرید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/688922" target="_blank">📅 09:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688921">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
آموزش‌وپرورش مازندران: در سیلاب اخیر ۶۶ مدرسه و مرکز آموزشی این استان دچار خسارت شدند که رقمی معادل ۴۵ میلیارد تومان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/688921" target="_blank">📅 09:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688920">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: ضریب ۲.۷ برابری برای اینترنت خارجی باعث گران‌تر شدن اینترنت شده است
علی جعفری‌آذر، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
ضعف یا نبود پوشش اینترنت و تلفن همراه در شهرها، روستاها و جاده‌ها، عدم تمدید یا بازگشت هزینه بسته‌های اینترنتی در دوران جنگ توسط اپراتورها و محاسبه ۲.۷ برابری مصرف اینترنت خارجی و نیم‌بها نبودن اینترنت داخلی باعث گران‌تر شدن اینترنت برای کاربران شده و توضیحات وزیر ارتباطات نتوانست نمایندگان را قانع کند و مجلس به او کارت زرد داد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/688920" target="_blank">📅 09:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688919">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdaaa3818e.mp4?token=RFqLJvfGC49671rlvzJXFecS1L4__fS-U6Q1dcR_NDRB-l5_eROg-73dzrBlVrgVeda0JD4vmu5kcYc5XvecHOOPo7gWN_u9i-Ng0DhsN655fpGUllJzQwcOBIVOU-QSMTG5t1tYifBJ1qkKklrt49tyquGctfySCYqRiS-yzJes3XymbDZuUAHhdpQ2ilhHur-f_CSb0eW4xPi_v3HX4IQ6SoArQP3fIVkxv1o0Us1FVJbmj_azu0Kqw5YU8DUCsJwXqZkQKeu-kJfz3YBnOye2sVXZzIFuC_Tlm8-NhL9MHrfTDEKnIT6nCDYajRk3NGVIS_0xc7gLA4Vb6EyK1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdaaa3818e.mp4?token=RFqLJvfGC49671rlvzJXFecS1L4__fS-U6Q1dcR_NDRB-l5_eROg-73dzrBlVrgVeda0JD4vmu5kcYc5XvecHOOPo7gWN_u9i-Ng0DhsN655fpGUllJzQwcOBIVOU-QSMTG5t1tYifBJ1qkKklrt49tyquGctfySCYqRiS-yzJes3XymbDZuUAHhdpQ2ilhHur-f_CSb0eW4xPi_v3HX4IQ6SoArQP3fIVkxv1o0Us1FVJbmj_azu0Kqw5YU8DUCsJwXqZkQKeu-kJfz3YBnOye2sVXZzIFuC_Tlm8-NhL9MHrfTDEKnIT6nCDYajRk3NGVIS_0xc7gLA4Vb6EyK1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: اگر ایران سلاح هسته‌ای داشت، ما با آن‌ها تماس می‌گرفتیم و می‌گفتیم: «آقایان، آیا امکان دارد که با هم ملاقات کنیم؟»
🔹
ما با آن‌ها به شکل بسیار متفاوتی برخورد می‌کردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/688919" target="_blank">📅 08:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688918">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b35ee08b5.mp4?token=MXiJasV7pzN285EAqIVuKQJQFH54yIjkgKe1TT1wBm4z75OKRiZcMZG8Kho2rguBaw7PmpyVy6Orq4HLNiLYV1U-Ky9S0yzsKAgPq1a0BbZsD6NeOq5xo-9PqmOiZsejsDMoyTKc7g-5C8ilinXSaohztBp07fq45Sqgb92DDUl9Z58qUKud3N0Zihq6yYcsjOy_zthwihq75ti-VY7tytPPRN7-JF2bmGS4pCIedC183mc8rejDRMvMiWK93d9S-n2sSc4d7DuqW5mJzKKWqu7fpGLp0KSjwI1ty8Q0T5kEsIF2Zw2y5BqE-IbrgCml2cUTmg48YT90D3BiGxG3Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b35ee08b5.mp4?token=MXiJasV7pzN285EAqIVuKQJQFH54yIjkgKe1TT1wBm4z75OKRiZcMZG8Kho2rguBaw7PmpyVy6Orq4HLNiLYV1U-Ky9S0yzsKAgPq1a0BbZsD6NeOq5xo-9PqmOiZsejsDMoyTKc7g-5C8ilinXSaohztBp07fq45Sqgb92DDUl9Z58qUKud3N0Zihq6yYcsjOy_zthwihq75ti-VY7tytPPRN7-JF2bmGS4pCIedC183mc8rejDRMvMiWK93d9S-n2sSc4d7DuqW5mJzKKWqu7fpGLp0KSjwI1ty8Q0T5kEsIF2Zw2y5BqE-IbrgCml2cUTmg48YT90D3BiGxG3Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ درباره پایان جنگ ایران:
من نمی‌خواهم بگویم دقیقاً چه زمانی، اما فکر می‌کنم این اتفاق درست بعد از انتخابات رخ خواهد داد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/688918" target="_blank">📅 08:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688917">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b53bb0ad15.mp4?token=eJGjVqlLryMB3d_SJjNNvbFd0RFXbyzrKXG4vGQHpUVtKztgY1XM2udMF0Z34vvldwCHVt603Zpo3yA7KjkmsI_QsWsJa6P4JThahaDnSWILkZ5ZqIzGOFcXWOUy9C5JyTClSQKS7staZl0lXJq_JoecjKyHuPm2H2ezYNTieX-DSY9QvdnH18wSbCKY8T7ecVfMtn6NhVSzShhTlSLiPF-knActB_g9AbOWUOgEwa49GBS_vA5qHRBJ2xcA9W-APlDPnHX-qY9a6Z5P2A0B4aY7ngYAcgFI0NQ4N41rYXx4EyUUHog4WBWmjCgDkclHWIK5yBMCfnJ7V5orJ16pqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b53bb0ad15.mp4?token=eJGjVqlLryMB3d_SJjNNvbFd0RFXbyzrKXG4vGQHpUVtKztgY1XM2udMF0Z34vvldwCHVt603Zpo3yA7KjkmsI_QsWsJa6P4JThahaDnSWILkZ5ZqIzGOFcXWOUy9C5JyTClSQKS7staZl0lXJq_JoecjKyHuPm2H2ezYNTieX-DSY9QvdnH18wSbCKY8T7ecVfMtn6NhVSzShhTlSLiPF-knActB_g9AbOWUOgEwa49GBS_vA5qHRBJ2xcA9W-APlDPnHX-qY9a6Z5P2A0B4aY7ngYAcgFI0NQ4N41rYXx4EyUUHog4WBWmjCgDkclHWIK5yBMCfnJ7V5orJ16pqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار فاکس‌نیوز: همه می‌گویند اگر می‌خواهید وارد ایران شوید، به طور کامل وارد شوید. فقط وارد شوید و آن‌ها را از بین ببرید
🔹
ترامپ: خب، شاید من این کار را انجام ندهم، چون انتخابات در راه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/688917" target="_blank">📅 08:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688916">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
رئیس‌جمهور به‌منظور شرکت در اجلاس بریکس عازم هند شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/688916" target="_blank">📅 08:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688915">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
قیمت نفت به ۱۱۰ دلار رسید
🔹
قیمت معاملات آتی نفت خام برنت در جریان معاملات شبانه با جهشی نزدیک به ۶ درصد به ۱۰۹.۹۷ دلار در هر بشکه رسید که بالاترین سطح آن در چهار ماه گذشته محسوب می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/688915" target="_blank">📅 08:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688914">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJX9RnM2r6uccL_hXKEENMmvC2KG6N8MVFoR5QvSBjUXVpVtWfEqZ1hOnqIFYhVFJTl1arEt_TUAQ5xOE0t70XBRHDM-yXIpiM1hwdmEQZsmcUSMnBs-sQipQehvQweea3-kSB5SC4n4lAhVvIzpRMD0qP8mZ02xEdLDJDu9byhkra5OXtT7zubTfkuQ5ywM6ZW3Ndj7J8Gn7lawmPhyuQ2uoQH73k-l-gaT8aKLacQcPSjeIFl1d2EXPW1uq-kZw-odkSiIfy1-Bc1aZdtxBQRcTMnRy1jWZJssDqD0JdQH7bd6qwxeGOWyZKGHD92kDWBvnJItPTxIn23qdt-yew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در واکنش به تهدید عربستان برای بمباران شدید بندر المخا، محمد الفرح، عضو انصارالله، منطقه نفتی رأس‌تنوره را تهدید کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/688914" target="_blank">📅 08:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688913">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b1f0f285.mp4?token=guhFgI4jy2q5GaRGjQbO4mhtuW0htbEuUou4G-YReW4UEsjEecz_-3pisc_e2qOr78uiBtYX_QntEIAQXSZxd7y9haQhdvd_kj2NB17614Tl7Nr8Y3Wgr09c2aNHrrfWbBZOdm03sf2byh5rX7qd2ZwJL3u6W8apUCIIOrykOPerAZ9FvSbG0h2b9Hz0wGsq-GNX5Vs1XJP-DV_JeQH6iFfx6Uw2fcsY-v4rbvB8Is7umZjHeDjKVm7khy4-YdI9O4_F8GPy6MU5t3pCmiwt779j3ksD8MzYNs7s3JT7qW4GJrJMMzh8sITabnUCttQ53nd8tEBGLjEy3FO-85IGUhK8B4P2cy42fpHOEfzSs9TZByFOinQJtMpGnI10ns60MCT9iQGjDOLClKUodxofblQYdQ7inKoDTijXwcEFCwtn2mZqvMwPcUXzFPCHQnj8AnVBf8E1HdVZf51oE7GXfSizWO2qz8c0zVkO1wuzTsq9S8cTk1O7naxsZ5cUGOaKku6bZlTt8MpiXGMtuYGQkstRhPm5pJBkNhvQTFng6CuLPKJ9zLPObE6H28VttByVNgNssx-AeLdNxzB2JuWeeZ4Z_1ah0DnfIUGxbTu9uqmIsE5Rnz0MFrKH8nuPYUCbow6gkyeRcn5dNqeUIxivPCqPW9wcE6p9u_PUntkJaxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b1f0f285.mp4?token=guhFgI4jy2q5GaRGjQbO4mhtuW0htbEuUou4G-YReW4UEsjEecz_-3pisc_e2qOr78uiBtYX_QntEIAQXSZxd7y9haQhdvd_kj2NB17614Tl7Nr8Y3Wgr09c2aNHrrfWbBZOdm03sf2byh5rX7qd2ZwJL3u6W8apUCIIOrykOPerAZ9FvSbG0h2b9Hz0wGsq-GNX5Vs1XJP-DV_JeQH6iFfx6Uw2fcsY-v4rbvB8Is7umZjHeDjKVm7khy4-YdI9O4_F8GPy6MU5t3pCmiwt779j3ksD8MzYNs7s3JT7qW4GJrJMMzh8sITabnUCttQ53nd8tEBGLjEy3FO-85IGUhK8B4P2cy42fpHOEfzSs9TZByFOinQJtMpGnI10ns60MCT9iQGjDOLClKUodxofblQYdQ7inKoDTijXwcEFCwtn2mZqvMwPcUXzFPCHQnj8AnVBf8E1HdVZf51oE7GXfSizWO2qz8c0zVkO1wuzTsq9S8cTk1O7naxsZ5cUGOaKku6bZlTt8MpiXGMtuYGQkstRhPm5pJBkNhvQTFng6CuLPKJ9zLPObE6H28VttByVNgNssx-AeLdNxzB2JuWeeZ4Z_1ah0DnfIUGxbTu9uqmIsE5Rnz0MFrKH8nuPYUCbow6gkyeRcn5dNqeUIxivPCqPW9wcE6p9u_PUntkJaxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۲۵ سال پیش، ۱۱ سپتامبر، روزی که آمریکا از طرف یک عرب اهل عربستان سعودی که در پاکستان مخفی شده بود مورد حمله قرار گرفت و بعد تصمیم گرفت برای تلافی به عراق و افغانستان حمله کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/688913" target="_blank">📅 08:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688912">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a870a1584b.mp4?token=Y9dRJSnlKL6SrQkx5a96pXUTpqxgWrz8M75G357MSEDq57vJQOA1tBXNxdc4ObwuBNavuco6gJXG2antptZxsP3SrXNlHN-PJP9hvDbGOmAvEGC1FQVaJHm08MobMd-L0mHHBN7u7NxMG78LE1mcQkn1k-K1nYyHWfGh2D0zB587aVnSDKDUiv9ulIIpPdn94JY7ZlsxCmLSiVjBK8V-VRaTyofbbQ4q-pT406JTf-yZvMu0fcNLoMuhYgOHhAvxbEGN45QT9s5Uzkos98Ihs7AX0y0kHqgVCFqXvKHCJz3-UWCXFIlXk8KNtrXiOqxJYc3TVRQnurIISMBSybTtDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a870a1584b.mp4?token=Y9dRJSnlKL6SrQkx5a96pXUTpqxgWrz8M75G357MSEDq57vJQOA1tBXNxdc4ObwuBNavuco6gJXG2antptZxsP3SrXNlHN-PJP9hvDbGOmAvEGC1FQVaJHm08MobMd-L0mHHBN7u7NxMG78LE1mcQkn1k-K1nYyHWfGh2D0zB587aVnSDKDUiv9ulIIpPdn94JY7ZlsxCmLSiVjBK8V-VRaTyofbbQ4q-pT406JTf-yZvMu0fcNLoMuhYgOHhAvxbEGN45QT9s5Uzkos98Ihs7AX0y0kHqgVCFqXvKHCJz3-UWCXFIlXk8KNtrXiOqxJYc3TVRQnurIISMBSybTtDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله راکتی به منطقه سبز بغداد در سال ۲۰۰۷
🔹
در ۲۲ مارس ۲۰۰۷ (۲ فروردین ۱۳۸۶) در منطقه سبز بغداد، در جریان یک کنفرانس خبری، چند راکت به نزدیکی محل نشست شلیک شد و یکی از آنها حدود ۵۰ متر با محل حضور بان‌کی‌مون دبیرکل وقت سازمان ملل فاصله داشت. وحشت بانکی‌مون و خونسردی نوری المالکی برای بسیاری در زمان خود قابل توجه بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/688912" target="_blank">📅 08:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688911">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4XCUWlpBAQ9r8w_s3VKj6h_VkgTQrW5hgE2oy93u2drHn5HadbaS268KnEVEvv3JGpHkAlNThQ2g-Hoh5-ODTf3_Ek5WMx9kq83vE3gaaA_aPktSQcOjjMFTS8e_iTYr_E6OfgTV4FkR4gpyIdshUMTCyCVhd70iBrLuBUihalOLjUp1dzvHGGjJy1dD3QHOR6wzy_t9UIt5fv2Z6xczQqoPikKW9gnzUg7bRnSAk_YNDO6LLdB3K1HYTN26DMlDSEWf4Qi-28klF_XflQWxx4fwbuNAwRZWsV16qvock5hqtzZPFcESt7mNXqMaW3P5gn-sHcCMM7ljfsd1RRRzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نتانیاهو: بزرگترین تونل ساخت ایران در خارج از این کشور را نابود کردیم، سال نو مبارک
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/688911" target="_blank">📅 08:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688910">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31074ae524.mp4?token=kS4fivwJfotHn64tPkVM0bAvAJp4TOMEfvlX0WIenfPTeiE-E1ly593aPvPt773nCnWPBVG_2b7dxvCMqtWA3gyF_ec_R2VoDjOtD6kkqo6aXciPmJwIYohFVN_8C_jk4m5bVWSYuoyH_nWQHJb5E5Vyb8_0-qmjrJ9Pne7OJTBdPbwcp3SAQ-H-IOWf0eM9Du4ieow1OWuA3DhXmPv9od5lKbTaijQGNJqKyd-usQNwYzfHuofUbEe3PhXY1gjbL2wj0N0F5KAMsvJNeVkYy0S_Fl_tXpcrhP7VIcLAlO0Jtk49n1mlVZxotOxFAL1i2_OlQ7yiU0U8qBFocFibng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31074ae524.mp4?token=kS4fivwJfotHn64tPkVM0bAvAJp4TOMEfvlX0WIenfPTeiE-E1ly593aPvPt773nCnWPBVG_2b7dxvCMqtWA3gyF_ec_R2VoDjOtD6kkqo6aXciPmJwIYohFVN_8C_jk4m5bVWSYuoyH_nWQHJb5E5Vyb8_0-qmjrJ9Pne7OJTBdPbwcp3SAQ-H-IOWf0eM9Du4ieow1OWuA3DhXmPv9od5lKbTaijQGNJqKyd-usQNwYzfHuofUbEe3PhXY1gjbL2wj0N0F5KAMsvJNeVkYy0S_Fl_tXpcrhP7VIcLAlO0Jtk49n1mlVZxotOxFAL1i2_OlQ7yiU0U8qBFocFibng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادامه گرافه‌گویی ترامپ: ایرانی‌ها به سختی می‌توانند به جنگ ادامه دهند و در تنگنای عمیقی قرار دارند
🔹
آن‌ها همیشه مقداری موشک دارند، توانایی موشکی ایران در حد زیادی نابود شده است
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/688910" target="_blank">📅 08:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688909">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
شوک به رئیس فیفا؛ فرانسه پشت اینفانتینو را خالی کرد
🔹
فدراسیون فوتبال فرانسه در اقدامی بی‌سابقه و پس از بررسی‌های گسترده، حمایت رسمی خود را از نامزدی جیانی اینفانتینو برای ریاست مجدد فیفا لغو کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/688909" target="_blank">📅 08:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688908">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWRO6MIG5CAbo222ymB8xN6eZDgqW_3LSl62KstNusAUtaqmnfkAQ4GZ681X58w14PF7WsqpsKi36XsFa0Dgnjz7HV96A0SdsVlKvXirMSJEb3HM9s36YWypqLlj60p6PA_O0k6RcpEimAhz8qxTWVeb4kG3_GBc25Ju6midYSJg3KyerczcIsNYcinoWvhSKBvsyojzughbskAQXmbJr8d9eQ-pg2aAKp4daPjANhDulupeLtlw_QaS7jJV6zhuZtYx1J4hlK66eqcDnOvj3EqL918KYr0hF6Tual2l0rPNi_o0CxEoGiLMW1bVm2JAwruf5cHK1RtK5g0uv7pgvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش عراقچی به اعتراف مقام آمریکایی؛ مردم آمریکا نباید هزینه جنگ‌های اسرائیل را بپردازند
وزیر خارجه:
🔹
صراحت «هانگ کائو»، سرپرست وزارت نیروی دریایی آمریکا، جای تشکر دارد. او درست می‌گوید، نیروهای مسلح قدرتمند ما واقعاً «ستاد ناوگان پنجم آمریکا در بحرین را با خاک یکسان کردند»؛ همان‌ کاری که با دیگر پایگاه‌های پشتیبان تجاوز آمریکا هم انجام دادند. مردم آمریکا واقعا نباید هزینه جنگ‌های اسرائیل را بپردازند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/688908" target="_blank">📅 08:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688907">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ادعای وال‌استریت‌ژورنال: ایران در چندین مکان زیرزمینی، در حال مونتاژ موشک‌های سوخت مایع و جامد است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/688907" target="_blank">📅 08:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688906">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlzaaWQosgx22IwxPMKgEo3NHZUp4oy_BU5YW7jh3zROENXzior9j5DbaxzK9-M2l6i9PFCHv6AjuxrSBR5mrEHPQsX7ysigb16uykmeKXl94nFeYO1SSfc95QG-815NY7yEiSepaPpWfw8fRnzARt1c5iN1JQH6f2b93dkP3R2-iKFvaZQPZffSwWWhgN1WtSGzIa0yyDznkTjCmfq5NL7Wm9bfegCTCd5qAf717-nLoZCBLgu8nTx_UAWaJnQiUrtPM_LwHe3Ez2qdG8YMzTsPnfhaDS89q_vm0eu6huCqNqmktQVacd9vBxJzBJG-wKwkTrIHvVQjE4OzwblwpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آتش‌سوزی بزرگ در خط لوله نفت شرق به غرب عربستان
🔹
منابع غیررسمی از احتمال حمله موشکی یا پهپادی به یکی از مسیرهای انتقال نفت عربستان خبر داده‌اند؛ حمله‌ای که به دنبال آن آتش‌سوزی شدیدی در نزدیکی شهر مدینه رخ داده و دود غلیظی در آسمان این منطقه دیده شده است.
🔹
تصاویر و داده‌های ماهواره‌ای نشان می‌دهد یک کانون حرارتی بزرگ برای چندین ساعت در این محدوده فعال بوده است.
🔹
منابع رسمی یمنی تا این لحظه بیانیه رسمی در این باره صادر نکرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/688906" target="_blank">📅 08:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688905">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WP7dKBPK0RS48Eoryomkf62idenL85etrM-oulSUAZ4jN6ieIQ449W5A5Be2GaGG7kjj2nWFYfrJx5qRRzFa8TXTXDD2GRQ_FyIU613vZFDwDI1dsaKi97whU5npLEiL9rz47OOgU4iNdHFT11mY3S9LPbJps_2lt6iEHSGrakM5WbjLnpEAjo68ra7sv7jMOx_7fgA97hYLKK4Ks2iAvN6qrp8W_PbDQSS2itUxBHzSkTw82ckueBPSd8OE0Lps0ClCu0YBrnDoFD6OS-6HT2fmi21XdSmsqUmylxeExMJUkg2oLHP_mM2at9laARp81lbJYeys7R8BViqVlyg1aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ونس ترامپ را دور زد؛ مستقیم از فرماندهان ارتش آمریکا، ارزیابی از جنگ گرفت
ادعای نیویورک‌تایمز:
🔹
معاون رئیس‌جمهور آمریکا، در اقدامی غیرمعمول و به‌صورت خصوصی خواستار ارزیابی‌های مستقیم و بدون فیلتر از فرماندهان نظامی آمریکا درباره جنگ ایران شد، و آنچه شنید بسیار نگران‌کننده‌تر از پیام عمومی دولت بود.
🔹
فرماندهان هشدار دادند که این جنگ ذخایر حیاتی تسلیحات آمریکا، به‌ویژه رهگیرهای پاتریوت و موشک‌های دوربرد را تخلیه می‌کند و در عین حال ممکن است توانایی آمریکا برای بازدارندگی چین، روسیه و کره شمالی را تضعیف کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/688905" target="_blank">📅 08:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688904">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
امروز آخرین مهلت انتخاب رشته داوطلبان آزمون ارشد دانشگاه آزاد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/688904" target="_blank">📅 08:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688902">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yg3uea0bdmnN4_c8vMxmwEQraHO1BsmYWLFOnfLwh3k3L5-LGd9PORyUofzFfr5y-9D1PKyqyD_1qBOQPDq53Q7c8iinkBfvFT2Z9zC3iL7yNVG5mndtLvCQ0ZzMx8yk5U-W7AcGiQVXarHOhvebTOgrncNfzIE21q6_WR4xzTrvquYEkFS1uSKBGfU5r5huTEQkEAdIVN6k2AEBKbuvZtcOV2lRQ_iE0XPdraHLxGqeu1kyS47PayAVdJnNUQcNlwaKd2R9gguRqllB1LlkkMiirXVNvrEQlof0jl4y-Pn0C1YjIY67OJdwPsDffs1Sg5SmWlIWjcDrOVQvB-MNHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QtFJ1DiqGyFTTQPSjnipJPTUImNEU5m42PKjy5GzevB3CK9pqI-CG8SCUaRJhRSqYBMgZW7Zx7JLroTuSwUduDDdpgsOcZACAvNqdLj9Nn45rIuKjpmSmZxau8MZxk0NsFkHyIdVZbJlyKnsV9oj0WuPCq6QkRsXW1wTShk2cYr56EbMUVAu9oi6pKD7VggV0lOAiH1rKl1aIHfn8FwIDgvpW4GtEG5ueDp54LVXjzdjVLYZqlynr4eK6iwnLTn2UOtE5IuecmgS56Qv3_RrMFDGg5brthx0qk1hBpV1TF0m9YLWUizNf_Y2aP39nAahVMQyy-chutP_WCEz5SQW5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
♦️
اصابت پر تعداد موشک‌های ایرانی در پایگاه موفق السلطی اردن از زاویه دیگر، همزمان با شلیک دهها موشک پدافندی
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/688902" target="_blank">📅 08:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688901">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WiwO7oUCACx4olEtr5kx0OXi0tpCyx28sAvWkZBhNAJZC_dWqOyoI1ifA5VR0DNYBK3Kf2BqbejnNHYH-O3F2r0wdZAg998wszSF5xuyfLkPB_NAx49nHmCd3OeWeqnWI_J51dcQJFFy8gwFxEHt37nkao3eXZe2TC4vpyiiK9BOgB8fSvsQsybbHja2mH0wuAwasmIjlj7EjOCt164tzuKwciINIyjqNR5V48bsRv5nbXCynD-WuZFHVI-nM5IU2WbCnf5Q_eXL85_ZQDf9BuILKxsXZM05wqa6mvkH6-84TqAD4tWzGfNiYBbohYZ0oczlQHXSsbVsEz5TW__1zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۲۰ شهریور ماه
۲۹ ربیع‌الأول ۱۴۴۸
۱۱ سپتامبر ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/688901" target="_blank">📅 08:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688900">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1VXge4sT4BTivmHZNYbnd1QnIU3_MnXehtkh8vUzx89EfMv29SfPOxowPRPaYNF_HUXkh1bIzksS0FujhBESm8ym3Whj4HGrH0cxRQb0jZdqfj7lx6KzyIPU8zPAlFTgWBDFbvh-r_sU0yzVqUD767jUjxDwAnC1mgKVXQ5GxUWOCx42bAtG4iJClP13tDmWqt_rBWSWeKjtsqHNiR-LfE2mVSwswe9MlVZVJc71YqqGYvFr6qUqi8fjL09m4QRoNHMzHXHqBgPAeUdKVw46wAFc7SeYPM6QtQSpMVI-p-V5hq9S66H1S0qTqTcldt-wtP82D__O-_BMTLVlf5gmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۰
کانال خبری و بیش از ۵ میلیون مخاطب!
😳
🔥
یه پکیج تبلیغاتی ویژه برای پاییز آماده کردیم
با شرایطی که شاید انتظارش رو نداشته باشی...
🍂
📩
جزئیات و قیمت؟
فقط کلمه «پاییز» رو پیوی بفرست
👇🏻
@S3eti_01</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/688900" target="_blank">📅 00:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688899">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tdsmhcikq3UD-StqrR7Z0ZgfO7ocbjGHmxscOyBesf979RLAeQF7ZOqrk1Bba4hDKXvgDClYNUsO-5QKhVST4EomQa7-9DegpWmy07UlPKM1-iXraMGXh_iBn3_-0izmCUyZY7BDiQ2-uuPUk9uHZbIVZCkrXm-kXuwawkB-hgaDdZXgWwdnrr9f1ZGQ8yVlqT6f1zN70N15ajv8bc6pKvS9txDp_VFT9zM-U-akW0E0egnqfbFmZ2KcQ1S3YY15nv-GZS97OBZMzr67diuyqP5zSnx4XBaAkz_tLgxi78jvEgWe9Sfo6GndclFpwIOviUk0PTC67dddXZ1v6TtxYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ست راحتی مردانه سوییشرت شلوار مدل Mpower
✅
جنس پلی‌استر باکیفیت و سبک
✅
مناسب هوای خنک بهاری
✅
فری‌سایز (مناسب L و XL)
✅
تنخور راحت و خوش‌فرم
🔴
قیمت فقط برای امروز  1,198,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/51861/180124/</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/688899" target="_blank">📅 00:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688898">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiU_lpS25OMRZt7SWCvxOYwkak2x0iR_8dnHD01ExGobXmkISeTEkcibiGvbVu4rQ_9QB3twNAvZcGbSKFaqiw7c5wxdy7P5QLj3Ju5o48jauY3yat5uBiLF8n57ojAc4evs7rWEc52MJl8hXSG0WtTOTUWJT__yebNDgeZWn93PfwGoyKd6UyIOV_PyLZtSWw4sF72uL4uz16kDSttyw0He-_gfafwcJ5CD5fDsrZsbIaSMMT0LfeghNUkkPcEFc05qwz8dE5b6RdJOs6BxUSaVdOMbJA7zhmaKb0pzNS6Vp62Fl8mBR7BmkYRWN88cq1J5WnLeMjx0Yv9wd60lMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حدادعادل: رهبر انقلاب با قوت مشغول کار هستند
/ جماران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/688898" target="_blank">📅 00:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688897">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
اظهارات
خداداد عزیزی علیه فدراسیون فوتبال: فدراسیون پول آپدیت VAR های لیگ را نداده و اصلاً خط آفساید کار نمی‌کند و نمی‌توانند سر صحنه‌های آفساید خط‌کشی کنند و تنها با عکس تشخیص می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/688897" target="_blank">📅 00:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688896">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8ee5a7ac3.mp4?token=NmRLrUVf6K-Nd96xO-mQ6MIlQG8eXx0wwXDJ3qP-j2YYC-eHUGHe0hGM8il-M5FkJS6uJiy05f7dDwtj6FRJeLvrZakK-Jx6kT9VisYH5TGGGePHo3hZ6_Wbxi1dtnovbtsg0T1RaOby85F08jmiKoOs7It-CSdu52eFnswtdazNPKJb-Mi8MKr-ABvmO7CcK-lbRcBOwVWvROFHltZiJCW6tEFVHKphzlRSAIGyNdwhf_tpBkj0hdm60c7AfTu39VS97lqVBsSZivEc2-C8CAeke80OEe8q-Q8YhYfhbbiuJxkyWNX8P97KdL0x1U4wZ93yB56h0-7z-be6U3ge5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8ee5a7ac3.mp4?token=NmRLrUVf6K-Nd96xO-mQ6MIlQG8eXx0wwXDJ3qP-j2YYC-eHUGHe0hGM8il-M5FkJS6uJiy05f7dDwtj6FRJeLvrZakK-Jx6kT9VisYH5TGGGePHo3hZ6_Wbxi1dtnovbtsg0T1RaOby85F08jmiKoOs7It-CSdu52eFnswtdazNPKJb-Mi8MKr-ABvmO7CcK-lbRcBOwVWvROFHltZiJCW6tEFVHKphzlRSAIGyNdwhf_tpBkj0hdm60c7AfTu39VS97lqVBsSZivEc2-C8CAeke80OEe8q-Q8YhYfhbbiuJxkyWNX8P97KdL0x1U4wZ93yB56h0-7z-be6U3ge5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تد کروز، سناتور و سیاستمدار آمریکایی درباره هوش مصنوعی: ترجیح می‌دهم ربات‌های قاتل آمریکایی باشند تا ربات‌های قاتل چینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/akhbarefori/688896" target="_blank">📅 00:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688895">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIfhuU2DyeSG3f2da_ZpRLLMFQfjU5fhMruLb8b_XwJ9TrNgQyicACt_rsOYFnHrU-8kfwVMB0njrQpRGp9JWhB54Yfa6mn13W25aarcnb4s0a7ONMRH8We3PPfBudfJdEDde3M0U1BliDo-qB4VpuM-D3UDEqffaFtw-v3p8TOPR8T5Iupb-eVQ_TL1QAKOqJUeYqiRAoRvALzN4yTk6_kdy_NXxMvBUxvUcGl3fkU-LKL_X61Sq8yevt_FKMIWDY9D4f46s3vH1gXN9qITZCItDuq63TtgQv2Z_Bft6D5Sp6bhkPTtO5-6k0brGnm_k2U_h_5yjE2Xm61zZqSfPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فتح‌المندب
🔹
رسانه‌ها از تسلط ارتش و نیروهای انصارالله یمن بر جزایر راهبردی زُقر و حُنیش بزرگ و کوچک در نزدیکی تنگه باب‌المندب خبر داده‌اند. این تحولات در حالی رخ می‌دهد که پیشروی حوثی‌ها در امتداد نوار ساحلی دریای سرخ مسیرهای انتقال انرژی را با چالش رو‌به رو کرده است. تحولات ژئوپلیتیکی اخیر در منطقه بر بازار جهانی انرژی هم به شدت اثر گذاشته و قیمت نفت امروز به حدود ۱۰۵ دلار در هر بشکه رسیده است.
🔹
هشتصدوپنجاه‌وهفتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/688895" target="_blank">📅 00:17 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688894">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTt5ziltUVSijss_W59d5SSjrTmRnf2ug5oomqf25YUeza1aJ3W0qsooPSbpQK3iBuuEO7H1oO_mv0xov6f-1lotSzA8RGHRva4tztwPhcj3bVHY4OzNPIIXW4kC3FcBdGHv1jpi8R0IG-l8cXi4LLrSYuNcdAQ_q1v7C3f_lD-UuMzWhTLls26TYHECfnCLdc4ICTRUAjux-0SEjNJdS4Objm4QGTzFaYCitSts7biSl3xXxN32xXXHdgrJPtk9SHMXf9m9Xaxa-cGvt2ZSaph7Evi-5bg0PltgNbQzhJRpcrB1fXJSVtdMJU8ptxqMF66P-heB6dpxsAOgA7JDuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت به ۱۰۸ دلار رسید!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/688894" target="_blank">📅 00:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688893">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
عراقچی و فرمانده ارتش پاکستان تلفنی درباره تشدید تنش‌ها و ناامنی منطقه و پیامدهای آن برای صلح و ثبات گفت‌وگو کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/688893" target="_blank">📅 00:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688892">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7bc4849a2.mp4?token=XhXOr4RdBzDwAFfTyQREV6zJx6ikIMfAS_SHT-oKAoSgGW5f3HE5roCdaO1r5INZ8k0rNbsy1gtk1uq1Yor6hK-3eA2fonA8_OukI-dnft8GZKyHoyi8itnyDZycS7WNPCxCXBz0KOpbbw3JknUmZ6LF3Pc60VtQgSErSnwe3f0SA_arVCSlQDk0U4qSdO1VFbGYqfnXvWCj8DgQCvW4ewf20T75sALmqOwkR-bvhH-FdGVZPmQcV0KUKr8YOTzRcaSDS4L_QomW7WQjaTO_75DZAP6LP32-7fnuVZiBzC9rXJ3nSDOvTJP-pfjo0Ct4JO_TRLw4Puck2VBq6Auq0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7bc4849a2.mp4?token=XhXOr4RdBzDwAFfTyQREV6zJx6ikIMfAS_SHT-oKAoSgGW5f3HE5roCdaO1r5INZ8k0rNbsy1gtk1uq1Yor6hK-3eA2fonA8_OukI-dnft8GZKyHoyi8itnyDZycS7WNPCxCXBz0KOpbbw3JknUmZ6LF3Pc60VtQgSErSnwe3f0SA_arVCSlQDk0U4qSdO1VFbGYqfnXvWCj8DgQCvW4ewf20T75sALmqOwkR-bvhH-FdGVZPmQcV0KUKr8YOTzRcaSDS4L_QomW7WQjaTO_75DZAP6LP32-7fnuVZiBzC9rXJ3nSDOvTJP-pfjo0Ct4JO_TRLw4Puck2VBq6Auq0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحقیقات هاروارد درباره محیط: اگر برای رشد باید ساکت باشی، آن‌جا جای تو نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/688892" target="_blank">📅 00:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688891">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
سازمان عملیات دریایی انگلیس: گزارش‌هایی مبنی بر وقوع حادثه‌ای برای دو کشتی در فاصله ۴ مایلی دریایی غرب شهر خصب در کشور عمان دریافت شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/688891" target="_blank">📅 00:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688890">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
درگیری ۶ استان با سیلاب/
سخنگوی هلال احمر:
۵۶۷ نفر حادثه دیدند
مجتبی خالدی، سخنگوی هلال احمر در
#گفتگو
با خبرفوری:
🔹
در ۲۴ ساعت گذشته، بارش‌های شدید و سیلاب در ۶ استان ایلام، مازندران، گلستان، سیستان‌وبلوچستان، کرمان و هرمزگان، ۵۶۷ نفر را دچار حادثه کرد.
🔹
بیشترین شهرستان‌های درگیر لاهیجان، رشت، کیاسر و فومن در گیلان و قائمشهر، ساری و نور در مازندران و بندرگز، کردکوی و گرگان در گلستان گزارش شده است.
🔹
نیروهای امدادی تاکنون به ۴۰۷ نفر امدادرسانی کردند وهمچنین۱۶۴ نفر اسکان اضطراری داده شده و ۴۵ نفر به مناطق امن منتقل شدند و  ورود به مناطق مرتفع استان‌های درگیر تا اطلاع ثانوی ممنوع است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/688890" target="_blank">📅 00:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688889">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5chEC6aCjbAdKJfTbC-jdtD_Ra-ebBTid4DMrtwNPQfkl0B2-wB2oMaKHveKwSxBob79ZXX4pFVz3WmuO819RoQDH-2U5hqEGptMHdkU7ZFLOQcU-rFAFf119wXOsG9TIe6Rz-FmVnu1H988wrAIN52w9JM1o3ciG7yN2XY7NxpkbzI0oSrcNAM_A19czfizoyXTebz0DKg8exsygkFNAVuCnInZpgNPseRdt8Mo5RZuIdCi1XLhhA8LZuVD4h3vXk2tU9ytPYhkp7Shg0lVcEYqLKdau-daI4dURLC3pHpL3uNL-IH8BHupjD5wmBHyWVGDvcELmfTbG6YXgrqqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/688889" target="_blank">📅 00:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688888">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
رهبر شهید انقلاب اسلامی در چنین روزهایی در ۱۸ شهریور ۱۳۹۴: رژیم صهیونیستی ۲۵ سال آینده را نخواهد دید
🔹
حضرت آیت‌الله سیدمجتبی خامنه‌ای رهبر معظم انقلاب اسلامی: رژیم متزلزل صهیونی و غدّه‌ی سرطانی اسرائیل نیز به مراحل پایانی عمر منحوس خود نزدیک شده و به فضل الهی و مطابق با سخن قاطع و آینده‌نگر ده سال قبل رهبر عظیم‌الشأن شهید قدس‌الله نفسه‌الزّکیّه، بیست‌ و پنج سال بعد از آن تاریخ را نخواهد دید، ان‌شاءالله. ۱۴۰۵/۳/۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/688888" target="_blank">📅 23:56 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688887">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
به‌صدا درآمدن آژیرهای خطر در شهرهای ابها و خمیس مشیط عربستان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/688887" target="_blank">📅 23:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688886">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25951e5e50.mp4?token=oAAijKBoOPLWBLq0zfT7Ya7mce2-M4j06Uo8vwVTpZKNHZKURvPmafh8YACuaW2DezJg_Cd4Kx4vom2kOJ3jH0DDhPe97QU1w019QeQAEnCpy-KezVcwWS8PJMJhhanHZcv6Imm54h521qj_1KNE4yG6WCJJvg_ov85vpbaK9iQBzwi63euz4oSGcU5G5MzuI3Kzplb_Jy0qeOLM3ok3xzI6mX2xzYS0h4f06uO509EetQbNpT3Xy4_PhM75f2Q7WPaYziR81WaaPhADONlRaNnVtFxaXztCJS7AlyQZn0erEHS3fnBqHMsLo2NNpQ-fjXEEfCuYouSn34SK4289qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25951e5e50.mp4?token=oAAijKBoOPLWBLq0zfT7Ya7mce2-M4j06Uo8vwVTpZKNHZKURvPmafh8YACuaW2DezJg_Cd4Kx4vom2kOJ3jH0DDhPe97QU1w019QeQAEnCpy-KezVcwWS8PJMJhhanHZcv6Imm54h521qj_1KNE4yG6WCJJvg_ov85vpbaK9iQBzwi63euz4oSGcU5G5MzuI3Kzplb_Jy0qeOLM3ok3xzI6mX2xzYS0h4f06uO509EetQbNpT3Xy4_PhM75f2Q7WPaYziR81WaaPhADONlRaNnVtFxaXztCJS7AlyQZn0erEHS3fnBqHMsLo2NNpQ-fjXEEfCuYouSn34SK4289qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بال‌های کفشدوزک؛ یک شاهکار مهندسی طبیعت
🐞
✨
🔹
طراحی تاشونده بال‌ها، الهام‌بخش ساخت سازه‌های بازشونده در فناوری و فضا شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/688886" target="_blank">📅 23:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688885">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
۵۴ روز تا انتخابات میان‌دوره‌ای آمریکا؛ فشار اقتصادی بر ترامپ افزایش یافته
🔹
قیمت بنزین به ۴.۲۷ دلار و گازوئیل به ۵.۹۷ دلار در هر گالن رسیده و نفت برنت نیز از ۱۰۶ دلار عبور کرده است.
🔹
هم‌زمان، دموکرات‌ها در نظرسنجی‌های ۷ ایالت از ۹ ایالت رقابتی سنا پیشتازند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/688885" target="_blank">📅 23:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688884">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAArQIt7CoVJNBsTt1i9tzsqNxAVumR8PtYX92Tj-B1pCvnjrq7S-_IiOqeMjItBjsSVdenE9QhBN89OV-q2mo3MgRVACSSUDxoFo_9aGUx3LKjvM8SxhPeCJpmKanJiQmWe6mrByU61gi_Xs8frhp2qboY1UsXteI2L6Z_-QoQp4D-vfIH34mO-sRoNXK9GfwX0EWbMoW6IfNexxFhm_DI-YR0Hq93hyDvvMQvlgi4pbqzjNFQaRXQk2FV6AKY9wagFdKfncXTxXtsEcx79KZAHKV_QcXfdV1Ji2aJVVxvxZvspAlbJBANiBtQ71L_B2WdditYNxa5CPeoTWjX4qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
پک رضوی؛ چهار تکه با معنویتِ یکجا…
همراه با حالِ خوبِ مشهد و هدیه‌ای مبارک از آستان حضرت رضا (ع). پک رضوی مجموعه‌ای ارزشمند و دلنشین از یادگارهای متبرک است تا عطر و حس‌وحالِ صحن و سرای رضوی را در هر لحظه همراه شما کند.
این پک شامل اقلام زیر است:
🧱
مهر تربت مشهدالرضا (ع)
📿
تسبیح سنگی رضوی (سوغات مشهد)
🌹
عطر متبرک روضه منوره (۲۰ میل)
📿
گردنبند طرح ایران امام رضا (ع)
💰
جمع کل به صورت تکی:
۱,۶۳۱,۰۰۰ تومان
✨
قیمت ویژه پک رضوی:
۱,۳۷۵,۰۰۰ تومان
📩
جهت ثبت سفارش این هدیه ارزشمند:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/688884" target="_blank">📅 23:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688883">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00287ee93d.mp4?token=knCQPWxBeBdRbtYyOxAnuhfPNZZCKVJi4fdhh1FVgy4H-ae6rDQbbmeGDK7d-iMP17yutr_vz0UZvXY2hYrz55CtejKfGSuxfpmz-lP0-Ie3NgiigWEsZcsz6cLUMb8wuMXMCU3gblX9I5rFnx5I6HpA8k_RGoaJmRoUfFcKLxNtbKOjKIEc1sBv2CpkzKAnv-oM38Jm5D8Sva0GBEsoVcIzQOLIrDQUE2FsU_bXGlvrqpCH9fdg9NPV6cT6D0gXJrMRs-EAETfu02mKDl9tUxNdxYdV_RfYErPdz9bfaX79nDfmjvWiUgamBCqJJZ43G6v9t9OUK20DWMIEj6gETwDjvHFJXQBYE1mVTSAJkz66_T8i1wQJlrN83TiMTEa37GAq0YKS9AxpFjQhgTGRgUgzPuDo3tuXX53NKpEPW3k8ZDGVXiFAteFuXmeK26jmv5JdXwyHd7PSDlEsrxKMoZtegfE9PUWXhO3LPysXUFhvYOwOwedtbNTbUnjAcwDfQK2a1K-1T-gwIxz4PJ0WozSYnuykc_8XlbjkW_zXEeSLo9avFgL_eY2V0HUCXiL_yF7_p-CB-tIc3ewD6gYIaQ__ISXGacEMPg66tN573pqAKA2GgKy1BX4S-oolbJ7aPsIrBb8TrpiIfUrbnMPW-QgmkacO0RXrVk12Z0B6Dr8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00287ee93d.mp4?token=knCQPWxBeBdRbtYyOxAnuhfPNZZCKVJi4fdhh1FVgy4H-ae6rDQbbmeGDK7d-iMP17yutr_vz0UZvXY2hYrz55CtejKfGSuxfpmz-lP0-Ie3NgiigWEsZcsz6cLUMb8wuMXMCU3gblX9I5rFnx5I6HpA8k_RGoaJmRoUfFcKLxNtbKOjKIEc1sBv2CpkzKAnv-oM38Jm5D8Sva0GBEsoVcIzQOLIrDQUE2FsU_bXGlvrqpCH9fdg9NPV6cT6D0gXJrMRs-EAETfu02mKDl9tUxNdxYdV_RfYErPdz9bfaX79nDfmjvWiUgamBCqJJZ43G6v9t9OUK20DWMIEj6gETwDjvHFJXQBYE1mVTSAJkz66_T8i1wQJlrN83TiMTEa37GAq0YKS9AxpFjQhgTGRgUgzPuDo3tuXX53NKpEPW3k8ZDGVXiFAteFuXmeK26jmv5JdXwyHd7PSDlEsrxKMoZtegfE9PUWXhO3LPysXUFhvYOwOwedtbNTbUnjAcwDfQK2a1K-1T-gwIxz4PJ0WozSYnuykc_8XlbjkW_zXEeSLo9avFgL_eY2V0HUCXiL_yF7_p-CB-tIc3ewD6gYIaQ__ISXGacEMPg66tN573pqAKA2GgKy1BX4S-oolbJ7aPsIrBb8TrpiIfUrbnMPW-QgmkacO0RXrVk12Z0B6Dr8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱۲۰ مگاوات انرژی پاک و تجدیدپذیر برقابی به شبکه برق کشور تزریق می‌شود
🔹
چهار واحد نیروگاه برق‌آبی چم‌شیر در مجموع به ظرفیت ۱۲۰ مگاوات به همت شرکت توسعه منابع آب و نیروی ایران در آستانه بهره‌برداری رسمی قرار دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/688883" target="_blank">📅 23:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688882">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa6dbcd73c.mp4?token=TMa5Sj14OU9RjEazu8GEcFaK36Hn4MBMGIta9_k5XvIN3piW3zFpplccE9bB9QNzSBi1_UYJ5eR1EGkFDljTa_GIvcZnNMpWmFJ5pBmUS9bxChgvlZkQaPDwQAl3N5pwkOuxLKIx7OALz5C6BG8K_3P3_TsYafcokcZPm4ZYig-UUclQ9UIWWx6AUFF0Gh7uHiglTS6rRA2xGLhMwWasShx1Tldz8xb9f4332QQnXDakRXcEQJOpCIhi988TeOH2MTlFzQkiM1ntpHY11bqxlbCqcRCu5clfEUgMmJXUaHjnyQW6DTUfc74OAh7BvK9B4z-Mtey6wqPrbuKJOAbqoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa6dbcd73c.mp4?token=TMa5Sj14OU9RjEazu8GEcFaK36Hn4MBMGIta9_k5XvIN3piW3zFpplccE9bB9QNzSBi1_UYJ5eR1EGkFDljTa_GIvcZnNMpWmFJ5pBmUS9bxChgvlZkQaPDwQAl3N5pwkOuxLKIx7OALz5C6BG8K_3P3_TsYafcokcZPm4ZYig-UUclQ9UIWWx6AUFF0Gh7uHiglTS6rRA2xGLhMwWasShx1Tldz8xb9f4332QQnXDakRXcEQJOpCIhi988TeOH2MTlFzQkiM1ntpHY11bqxlbCqcRCu5clfEUgMmJXUaHjnyQW6DTUfc74OAh7BvK9B4z-Mtey6wqPrbuKJOAbqoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جاهایی روی زمین که انگار واقعی نیستند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/688882" target="_blank">📅 23:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688881">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
سازمان رسانه‌ای رژیم صهیونیستی از برگزاری دور جدید مذاکرات اسرائیل با لبنان در روزهای سه‌شنبه و چهارشنبه در شهر «رم» خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/688881" target="_blank">📅 23:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688879">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قیمت روغن نباتی حدود ۳۸۰ درصد افزایش یافت
علیرضا شریفی، دبیر انجمن صنایع روغن نباتی در
#گفتگو
با خبرفوری:
🔹
قیمت مصرف‌کننده روغن نباتی نسبت به قبل از حذف ارز ترجیحی در دی ماه، به‌طور متوسط حدود ۳۸۰ درصد افزایش یافته است.
🔹
این افزایش قیمت باعث شد که قاچاق تقریباً از بین برود و مصرف خانوار، صنف و صنعت نیز کاهش یابد.
🔹
تولید در ۵ ماهه نخست سال جاری نیز حدود ۸۲۵ هزار تن بوده که نسبت به مدت مشابه در سال قبل، ۱۳ درصد کاهش یافته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/688879" target="_blank">📅 23:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688878">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
نرخ بازدهی اوراق قرضه ۳۰ ساله خزانه‌داری آمریکا به ۵.۳۶ درصد رسید که بالاترین سطح از زمان بحران مالی ۲۰۰۷ است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/688878" target="_blank">📅 23:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688877">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
باب المندب آزاد شد / پیش‌روی انصارالله یمن همزمان با عقب‌نشینی مزدوران وابسته به سعودی
👇
khabarfoori.com/fa/tiny/news-3244248
🔹
همسر خود را در خیابان بزنید، نه پلیس مداخله می کند و نه اورژانس اجتماعی
👇
khabarfoori.com/fa/tiny/news-3243509
🔹
انفجار ۱۱۰۰ تن مواد منفجره در جنوب لبنان/ انهدام تونل‌های زیرزمینی حزب‌الله توسط اسرائیل
👇
khabarfoori.com/fa/tiny/news-3244277
🔹
روستایی در چین که در آن مردم، فارسی حرف می‌زنند | راز ایرانیِ یک آبادی دورافتاده
👇
khabarfoori.com/fa/tiny/news-3244234
🔹
ملانیا بالاخره درباره دستیار بلوند ترامپ سکوتش را شکست
👇
khabarfoori.com/fa/tiny/news-3244182
🔹
صفحه ویژه اخبار پربازدید وبسایت خبرفوری را اینجا کلیک کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/688877" target="_blank">📅 23:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688876">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72408cebae.mp4?token=hkTuvuQMyVf7MAGwGZY6kLXbmcnpzYv5QN1_PzSUnGbs83jyVLRZVKkw30EVUf505LrO5SgHiW7-eZvXy5zKhmbpOwn4EDXXRz0MbKTLKShQCDlPTT2usQyBUHsCzEZx3Ka4rnza_LNLuiKhhZ5rYNn6P9TtKBaWKlTLWWRrDoaJFKxo3JaNId8u7zAsovR5eV6XRMQ6-2Vq5Zyg2z3H_uMi94sEJd6_y2o5uhRtHfJa-B2x4BCWKh0JOAiN3-NftWEyEAYXqmoY7naJbcw4cHnXcU7pIDTZ8vc-dV8BDtgCOReTN6uThy8lBAveqy7OfxTKvFOPTR-1fbD8ZZG3QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72408cebae.mp4?token=hkTuvuQMyVf7MAGwGZY6kLXbmcnpzYv5QN1_PzSUnGbs83jyVLRZVKkw30EVUf505LrO5SgHiW7-eZvXy5zKhmbpOwn4EDXXRz0MbKTLKShQCDlPTT2usQyBUHsCzEZx3Ka4rnza_LNLuiKhhZ5rYNn6P9TtKBaWKlTLWWRrDoaJFKxo3JaNId8u7zAsovR5eV6XRMQ6-2Vq5Zyg2z3H_uMi94sEJd6_y2o5uhRtHfJa-B2x4BCWKh0JOAiN3-NftWEyEAYXqmoY7naJbcw4cHnXcU7pIDTZ8vc-dV8BDtgCOReTN6uThy8lBAveqy7OfxTKvFOPTR-1fbD8ZZG3QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلیپی از صحبت‌های شنیدنی رهبر انصارالله، همزمان با پیروزی‌ها و پیش‌روی نیروهای یمنی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/688876" target="_blank">📅 23:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688874">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30729b4967.mp4?token=rS6t2WjAtTYS4HTGoC3iL1d7Assxt0GogTmPhxbuP4N4SFzqMDxDCviBdUE_PIbxy8DYzbUKyrTCsABFWhB8FVbifmt0Iyl6Qc-lpBaajJO5HsLeBMg0NVB_zsSTTrxT3Ldbajh_REBbfTUIJ14nJGVE4dseUEq_2EiDngTGDH6e_QnOmw27pJztL-glKz1AYf5BJl9XEfxqiSHgh_l0uf4WIXFucdxCvtF619soP5ZYAYQUYoPPl31EM4V0m_ogfnLpyHEdaW2psEz4rh-JZvojoIT5bMkcJp6g5Z1abMJ1Sd6EdqFZW2Ubgrghv57jcEge0ProHt061zrZFK17hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30729b4967.mp4?token=rS6t2WjAtTYS4HTGoC3iL1d7Assxt0GogTmPhxbuP4N4SFzqMDxDCviBdUE_PIbxy8DYzbUKyrTCsABFWhB8FVbifmt0Iyl6Qc-lpBaajJO5HsLeBMg0NVB_zsSTTrxT3Ldbajh_REBbfTUIJ14nJGVE4dseUEq_2EiDngTGDH6e_QnOmw27pJztL-glKz1AYf5BJl9XEfxqiSHgh_l0uf4WIXFucdxCvtF619soP5ZYAYQUYoPPl31EM4V0m_ogfnLpyHEdaW2psEz4rh-JZvojoIT5bMkcJp6g5Z1abMJ1Sd6EdqFZW2Ubgrghv57jcEge0ProHt061zrZFK17hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
بازسازی جنگ احد و نبرد خیره‌کننده حضرت علی علیه السلام
@Heyate_gharar</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/akhbarefori/688874" target="_blank">📅 23:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ادعای یک مقام آمریکایی در گفت‌وگو با شبکه ۱۳ عبری: ایران در حال برنامه‌ریزی برای انجام یک حمله گسترده علیه رژیم صهیونیستی‌ است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/688873" target="_blank">📅 23:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688872">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
وزارت خزانه داری دولت تروریستی آمریکا در ادامه اقدامات خصمانه علیه ایران از اعمال تحریم‌های جدید انچه مرتبط با ایران خوانده، خبر داد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/688872" target="_blank">📅 22:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688871">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
سیاست ارزی جدید بانک مرکزی در مسیر تسهیل تجارت خارجی؛ بررسی صحت گزارش فایننشیال تایمز
🔹
فایننشیال تایمز در گزارش اخیر خود، تغییرات سیاست‌های ارزی بانک مرکزی ایران را در روزهای پس از محاصره اقتصادی بررسی کرده و آن را حرکتی در جهت تسهیل بازگشت ارز و حفظ جریان تجارت خارجی توصیف کرده است. بررسی رفتار سیاست‌گذار ارزی نیز نشان می‌دهد که در ماه‌های اخیر تغییرات اساسی در روند مدیریت ارزی کشور رخ داده است.
🔹
فایننشیال تایمز به تازگی در گزارشی، تغییرات در سیاست‌های ارزی بانک مرکزی را در روزهای بعد از محاصره اقتصادی بررسی کرده است. این روزنامه با اشاره به تلاش بانک مرکزی ایران برای حفظ جریان تجارت خارجی و مقابله با وضعیت محاصره اقتصادی، توضیح داده است که در گذشته، صادرکنندگان ایرانی مکلف بودند بخش عمده عواید صادراتی خود را برگردانند و در مرکز مبادله ارز و طلای ایران با نرخ پایین‌تر از بازار عرضه کنند؛ اما تغییرات اخیر را حرکتی به سمتی توصیف می‌کند که فعال اقتصادی امکان بیشتری برای مبادله ارز در بازار گسترده متشکل از بانک‌ها و صرافی‌ها و با نرخ‌های نزدیک‌تر به بازار داشته باشد و صادرکننده هم بتواند از عواید صادراتی خود به صورت مستقیم برای تأمین واردات استفاده کند.
🔹
نکته قابل توجه این گزارش آن است که مجموعه سیاست‌های ارزی اخیر را در جهت رفع بخشی از ناکارآمدی ترتیبات قبلی و مقابله با وضعیت نامطلوب فعلی از طریق تسهیل بازگشت منابع و استمرار تجارت خارجی تحلیل کرده است.
🔹
این گزارش اشاره کرده است که در رویه جدید، بازرگانان می‌توانند ارز خارجی را در بازار آزاد مبادله کنند یا مستقیما از عواید صادراتی خود برای تأمین مالی واردات استفاده کنند و نیازی به عبور از سیستم رسمی ارزی ندارند. همچنین این گزارش مدعی شده است که بانک مرکزی ایران در ماه‌های اخیر و با حفظ سکوت، بازرگانان را تشویق کرده است تا برای بازگرداندن سرمایه‌های خود از هر وسیله‌ای که لازم است استفاده کنند.
🔹
البته بانک مرکزی هنوز واکنشی نسبت به این گزارش نداشته است و نمی‌توان ادعاهای این گزارش را تأیید یا رد کرد؛ اما بررسی رفتار سیاست‌گذار ارزی نشان می‌دهد که در ماه‌های اخیر تغییرات اساسی در روند مدیریت ارزی کشور اتفاق افتاده است و بنظر می‌رسد برخی گزاره‌ها در گزارش فایننشیال تایمز صحت داشته باشد.
🔹
حذف ارز ترجیحی؛ نخستین تغییر اساسی
اولین تغییر اساسی، حذف ارز ترجیحی در اواخر دی‌ماه سال گذشته بود. بانک مرکزی با این اقدام، بستری را فراهم آورد که صادرکنندگان بتوانند ارزهای صادراتی خود را با نرخی بالاتر و نزدیک به بازار آزاد عرضه کنند. این تصمیم بانک مرکزی صادرکنندگان را به بازگشت ارز حاصل از صادرات تشویق کرد.
افزایش محسوس بازگشت ارز پس از اصلاح سیاست‌ها
🔹
یکی از دلایل اصلی بانک مرکزی برای این تصمیم، افزایش نرخ عدم بازگشت ارز در سال‌های اخیر بود. طبق اعلام چند روز پیش دستیار ارزی رییس کل بانک مرکزی، درصد تعهدات سررسیدشده ایفاشده که در سال ۱۴۰۰ به ۹۱ درصد رسیده بود، از سال ۱۴۰۱ روند کاهشی داشته و در سال ۱۴۰۵ به ۵۲ درصد رسید. یکی از دلایل اصلی کاهش نرخ بازگشت ارز از سال ۱۴۰۱، اعمال نرخ‌های دستوری ارز و عدم جذابیت و عدم سهولت بازگشت ارز از مسیرهای تعیین‌شده بود.
مقایسه وضعیت بازگشت ارز قبل و بعد از ۱۵ دی ۱۴۰۴ نشان می‌دهد که بعد از اصلاح سیاست‌های ارزی، روند بازگشت ارز به صورت محسوسی افزایش یافته است؛ به نحوی که درصد بازگشت ارز به صادرات که در سال ۱۴۰۴ معادل ۶۸ درصد بود، در ۵ ماه ابتدای سال ۱۴۰۵ به ۱۱۷ درصد رسیده است.
رویکرد جدید بانک مرکزی در حوزه سیاست ارزی علاوه بر اینکه بر روند بازگشت ارز اثر مثبت داشته است، مدیریت بهینه‌تر منابع ارزی را نیز به همراه داشته است. همانگونه که رئیس کل بانک مرکزی اخیرا در صحبت‌های خود عنوان کرده است که از ابتدای سال ۱۴۰۵ و در دوران بعد از جنگ رمضان از ناحیه اصلاح سیاست‌های ارزی بیش از ۴.۵ میلیارد دلار به ذخایر ارزی کشور افزوده شده است.
🔹
روش های جدید بانک مرکزی برای رفع تعهد ارزی صادرکنندگان
بانک مرکزی اخیراً از یک اقدام جدید دیگر خود نیز خبر داد که بیشتر تأییدکننده گزارش فایننشیال تایمز است. سیاستگذار پولی و ارزی در این خبر اعلام کرده است که صادرکنندگانی که از تاریخ ارزیابی پروانه صادراتی آن‌ها بیش از ۱۵ ماه نگذشته، می‌توانند با ارائه اظهارنامه گمرکی ورود اسکناس، ارز خود را در نمادهای اسکناس بازار ارز تجاری مرکز مبادله ارز و طلای ایران بفروشند و همچنین صادرکنندگانی که از ارزیابی پروانه آن‌ها بیش از ۱۵ ماه گذشته نیز می‌توانند ارز صادراتی خود را به بانک مرکزی با عاملیت موسسات اعتباری و به نرخ خرید حواله ETS  عرضه کنند.
🔹
عرضه ارز از سوی صادرکنندگان با نرخ خرید حواله ETS یعنی صادرکنندگان این امکان را خواهند داشت که ارز خود را با حداقل فاصله از نرخ بازار آزاد به صورت رسمی عرضه کنند و رفع تعهد ارزی داشته باشند.
🔹
تصمیمات اخیر بانک مرکزی در حوزه سیاست‌های ارزی نشان می‌دهد که سیاست‌گذار ارزی در رویکرد جدید خود تلاش دارد که در شرایط محاصره اقتصاد و جنگ نظامی، جریان تجارت خارجی را از طریق تشویق صادرکنندگان به بازگشت ارز و ارائه راهکارهای قانونی برای ورود ارز به کشور حفظ کند. مسئله‌ای که با بخشی از گزاره‌های موجود در گزارش فایننشیال تایمز همخوانی داشته و می‌تواند آن را تائید کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/688871" target="_blank">📅 22:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688870">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c128be865.mp4?token=ryLS98lm-q1jl-EuMy4ZRXWx5CVlnkXEJzmRsGHEFnoJCD-GMOEpbZsCIzcCc7mEocMF4EboYVaMkLP5eT3ymlK8xqfgQZAbDkN8KqruUIA93-8jdD4QYWNjZemgwY9kHTl0ldNZziAaaIWPetyQkP7PSeyDSACQcGjoZyI7GRIwZZMGJOPWMb05OEDUzBBU1Fw8IkdtXFGZHmLO9C1ai0wjKwwOSf8ovOFjd-tomO9_-VgsqhlRhpHhKsSKEmRIc2EBoBm-ctEhav74bbi70W0Fewsd3Hn0zjLj_cwK1EpOjLzaUJWOuWFcXaUdMJjHvBBLyKQjLzHA828X9dz21A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c128be865.mp4?token=ryLS98lm-q1jl-EuMy4ZRXWx5CVlnkXEJzmRsGHEFnoJCD-GMOEpbZsCIzcCc7mEocMF4EboYVaMkLP5eT3ymlK8xqfgQZAbDkN8KqruUIA93-8jdD4QYWNjZemgwY9kHTl0ldNZziAaaIWPetyQkP7PSeyDSACQcGjoZyI7GRIwZZMGJOPWMb05OEDUzBBU1Fw8IkdtXFGZHmLO9C1ai0wjKwwOSf8ovOFjd-tomO9_-VgsqhlRhpHhKsSKEmRIc2EBoBm-ctEhav74bbi70W0Fewsd3Hn0zjLj_cwK1EpOjLzaUJWOuWFcXaUdMJjHvBBLyKQjLzHA828X9dz21A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در پی اقدام ارتش اسرائیل برای انفجار تونل‌های علی الطاهر، یک زمین لرزه خفیف در لبنان حس شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/688870" target="_blank">📅 22:56 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688869">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای سفر محرمانه هیئت ایرانی به امارات در مرداد ماه، صحت ندارد
علی احمدی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
اینکه هیئت ایرانی به‌صورت محرمانه در مرداد به امارات سفر کرده واقعیت ندارد، ایران چیزی برای مخفی کردن ندارد و اگر هیئتی به امارات برود، اعلام می‌کند.
🔹
میانجی‌های مصر، قطر، پاکستان، عمان، ترکیه و اخیراً روسیه همگی می‌خواهند جنگ به پایان برسد و خیلی از کشورها به این نتیجه رسیده‌اند که باید ایران را راضی کنند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/688869" target="_blank">📅 22:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688866">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
سی‌ان‌ان: بیش از ۱۰۰ مشاور نظامی آمریکا برای پشتیبانی از عملیات عربستان علیه یمن در این کشور مستقر شده‌اند؛ این نیروها در زمینه اطلاعات و هدف‌گیری به افسران سعودی کمک می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/688866" target="_blank">📅 22:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688865">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
به‌صدا درآمدن آژیرهای خطر در شهرهای ابها و خمیس مشیط عربستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/688865" target="_blank">📅 22:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688864">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajIm3_MEqyFdlkggkK2eViUhKmVahm6x52eHZIlDXfsgtELvfsZvYilhY6bMBvYyQ3trAxj3YVmvdKK6qOkN--xWr7e6W4w3JdO0HZm6jl_9gdVAFSHtUf5XkaP6y3h96xZzVhdz8DcIwwOAfcPAuQC-5XVyumR0emHUb0Y9_Q5og77DVk2MAjZj6tKO9pE3ViwMQkyTAN_ifftYrHhGewAVjueCnWINC2ZZgltZwAIa9ToHgSwniP9hPjySENsVk8ElXtB8ymwq98_qMigbhDLk4ciK7Wb3QKTiuq15gaFfGZ13ZdG0uWt8ZSXxYA0HtXAiZ5VK_S5XIjVMIe-AqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای جدید ترامپ: هیچ هواپیمای نظامی آمریکایی در حمله ایران به پایگاه هوایی در اردن آسیب ندیده است
🔹
در حالی ترامپ این ادعا را مطرح می‌کند که شبکه خبری سی‌بی‌اس آمریکا از خسارت گسترده به تجهیزات نظامی این کشور در جریان حمله موشکی ایران به پایگاه هوایی «موفق…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/akhbarefori/688864" target="_blank">📅 22:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688863">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-q_Aw86tQz6a_RS3n8tXQaUJJEIFB6-IwwaczU7d6jcb9G7VON5kb8jAo97c_1VuXRYYofARfXahpJa1bDfHGGTbcjWUrdHgCFy1n29hO_2Ae6y6PRtU0Q5yDT-bPpXeCCirweTc3Ffz-lLdtNR6Rvk5PBOz98fow7tJoimVN-NsQzTVCWtfOREqY0pOqtGfuDpIFjRzjNuYbl6ihR9gSrpJolY_L8XB6rw8AXXiJ2x6y7Est2ZBJi7HJpgj3lF6mnJ-PYod8M6T9NaxeYahDSVC_AI9UG1ovEQMgQayYezFMb-1MD0CfqrEBbJp_eNGXVw4_oA1f6Rzrd2JbKV6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
برای خرید بیمه ثالث موتور؛ بیمه، بازار داره!
من خیلی با موتورم راحتم، ولی قبل از سوار شدن، دو تا چیزی که اول خریدم:
یه کلاه خوب و یه بیمه خوب!
ما موتورسوارها وقت برامون مهمه؛ پس رفتم سراغ
بیمه‌بازار
:
✅
شرکت‌ها رو یک‌جا
مقایسه
کردم
✅
بهترین قیمت
رو انتخاب کردم
✅
بیمه‌م رو با
صدور فوری
، همون لحظه خریدم
👈
برای خرید آنلاین بیمه موتور وارد شو
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/688863" target="_blank">📅 22:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688862">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Af0qS21SzTkwkXsIMGhYw5ziKjujtTdLgXR9YN-xwgkhTMw1qrmP6z_x1oSCzHPhg-4bks9KAiMMhWf1KOzJozY4h0p2WncpyI00LekNLvdqKs1SLcdcNVPRD2_T_NTMK9W7nxClFqvRp9_gQwDnmRnMwtdR-f-8Caz1Hly5IhGU8gfyHsbqPQiJEolgXP7W4CRGY-unmqHuR_D0wiUEs_1q4wSoUJxc3AMId9cAaCYuAEzz5jKqRJRB8IKuhJMRxfE5JVDQJWJi7ThApoHKQlC_my6ylkldxDTxwU--X5iemPkoXlnQWcK7UTEfdt0x_R2RWLdABeiJ3dQNkBkpfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه تو گوگل و ترب دیده نشی، یه بخش مهم از مشتری‌هات رو از دست می‌دی.
اینستاگرام برای جذب عالیه
👌
اما وقتی کنارش سایت داشته باشی، از چند مسیر مختلف می‌تونی مشتری بگیری.
با میکسین می‌تونی یه سایت حرفه‌ای، متصل به گوگل و ترب داشته باشی.
برای راه‌اندازی، سایت و یا دریافت مشاوره رایگان کلیک کن.</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/688862" target="_blank">📅 22:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688860">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8f629792.mp4?token=R-r_u5aF-xnXJFNZlzVbTO_8EBmT0ztwECFLKN_4gxMYdw67QYbqbsw0OnOeovowzswPp8LKeXH8DPvIGmuI6mIRwtUThmgWVJijxl3eZtKPGgx5Pa05Xgk5CkDfm_wCDiC4WCiK6XVGbwgBIkJp14yf_RO04SJoge1A5D4_vAoXTk8VGjxJqLuCtSgfJa6nx8c27MnLxfeJBmexhyMunMZgjswl0ujXUgERSbRQezHEQa_Uz5tMFBN88QiRbYCz9Wz4fe81vkb-p1JsdtKDHWkJeODGSpA0D62Io3wD99Qo4x2xdbDzepsoz5cBLFmgEz1MxkhfX42AgQj0AMe7Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8f629792.mp4?token=R-r_u5aF-xnXJFNZlzVbTO_8EBmT0ztwECFLKN_4gxMYdw67QYbqbsw0OnOeovowzswPp8LKeXH8DPvIGmuI6mIRwtUThmgWVJijxl3eZtKPGgx5Pa05Xgk5CkDfm_wCDiC4WCiK6XVGbwgBIkJp14yf_RO04SJoge1A5D4_vAoXTk8VGjxJqLuCtSgfJa6nx8c27MnLxfeJBmexhyMunMZgjswl0ujXUgERSbRQezHEQa_Uz5tMFBN88QiRbYCz9Wz4fe81vkb-p1JsdtKDHWkJeODGSpA0D62Io3wD99Qo4x2xdbDzepsoz5cBLFmgEz1MxkhfX42AgQj0AMe7Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیلاری کلینتون: می‌دانید، آدم باید از خودش بپرسد: خب، امروز کجا ایستاده‌ایم؟
🔹
این ما هستیم که داریم ایران را تقویت می‌کنیم؛ آیا از آنچه طی ۲۵ سال گذشته انجام داده‌ایم، هیچ درسی نگرفته‌ایم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/688860" target="_blank">📅 22:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688859">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e56a97930.mp4?token=EJwHTAqM60z4zMS9fUwyn_ZOmUvADfLXDj4aC8mEOmDR_2BcQ8n14z1NXZ6Wks86X6zhtNH4z3F_IHDgtXSX5uH26mWdal0XcdhStQiZe10zCO02AjQm3d6cA3cievZ2D2FCW-eoBeRXo9ezWSN_ZBAD9KMgWTo7kdFRymX07aZRV_Z57r4OWcr1Wak69_FxyxzhTa3SlvUGJ1SdBgzB2Y06pZnxwgNiNhUqVgZMcWGqgDDsBdj2sofAIgHtJYTGUZIx-SVhnUcmHE5l_k4QrRSTHvpwUEyFMfAy8Y9gi-7VMhQwLkGzR8IQf_6TEQ_E8i-l8JA6IO2fueFqN73gTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e56a97930.mp4?token=EJwHTAqM60z4zMS9fUwyn_ZOmUvADfLXDj4aC8mEOmDR_2BcQ8n14z1NXZ6Wks86X6zhtNH4z3F_IHDgtXSX5uH26mWdal0XcdhStQiZe10zCO02AjQm3d6cA3cievZ2D2FCW-eoBeRXo9ezWSN_ZBAD9KMgWTo7kdFRymX07aZRV_Z57r4OWcr1Wak69_FxyxzhTa3SlvUGJ1SdBgzB2Y06pZnxwgNiNhUqVgZMcWGqgDDsBdj2sofAIgHtJYTGUZIx-SVhnUcmHE5l_k4QrRSTHvpwUEyFMfAy8Y9gi-7VMhQwLkGzR8IQf_6TEQ_E8i-l8JA6IO2fueFqN73gTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی دیگر از انفجار در ارتفاعات علی‌الطاهر لبنان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/688859" target="_blank">📅 22:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688858">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
در پی اقدام ارتش اسرائیل برای انفجار تونل‌های علی الطاهر، یک زمین لرزه خفیف در لبنان حس شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/688858" target="_blank">📅 22:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688857">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
وزارت خزانه داری دولت تروریستی آمریکا در ادامه اقدامات خصمانه علیه ایران از اعمال تحریم‌های جدید انچه مرتبط با ایران خوانده، خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/688857" target="_blank">📅 22:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688856">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ارتش اسرائیل اعلام کرد برای از بین بردن زیرساخت‌های تونلی در زیر منطقه «تپه علی طاهر» در جنوب لبنان، بیش از ۱۱۰۰ تُن مواد منفجره به کار گرفته شده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/688856" target="_blank">📅 22:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688854">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrUWnZ716Z5dOaE3hSw9jxjAKI8Y_WqHFadWsy7N2FKsC2I9Tpk8YYgrKOPTnnosymOrNUL2fqtK4TKitFoJYPAv6fkIRSO9CO06o2f4TTvPqGn-g0LXToT2EJvDDgA1t1wek_Zpebbpzq3Vks4z0XhJUVqNCIrM3g6ImseUhee9kHX1NJ2rxEDkm6ejWiDXxi3UAM5v3dzLvv4ysLkitXFTTCMdy5YYfbd-rSe-K_eDV21pmMW7lUlHgfhItsSfJPGpyqVh7aZUxvhT7dKlZ1uvbmsQtSzDk7mMmYJGUVIkI2oW4z9fBKrHt83UtxgoyOqMiq3gLF4_N7Q9squD5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرفوری / تنگه باب المندب به تسخیر رزمندگان یمن درآمد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/688854" target="_blank">📅 22:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688852">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ارتش اسرائیل اعلام کرد برای از بین بردن زیرساخت‌های تونلی در زیر منطقه «تپه علی طاهر» در جنوب لبنان، بیش از ۱۱۰۰ تُن مواد منفجره به کار گرفته شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/688852" target="_blank">📅 22:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688851">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
حملات رژیم صهیونیستی به ارتفاعات علی الطاهر
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/688851" target="_blank">📅 22:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688846">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa60631d07.mp4?token=HP6rP2rC1qCYIcbo4YCB_AoFjhOoRP_Q1XRIAZ6FrCvIQzMmXX9FNBMWu5few_DmjL2awwkWWJ8luDhtzf2G8oq3VzrtwrzGZ-KZYVWCENdL_DDePWOcivULVhqM9vuHArpysX6Vb12hbzguYtFPc1xbCw40gIPwDuXRLOSVKXP9TLBKTdHsIRCJbsVYskIGAiHmYatoJ7aGM2UM06Wqx-ryq42eNruEcciK_lLZN33FxNXoSrF6VJAH_RbICJnh7PflLxJ7aL2bysxaYJyQUWK80eCeuJDI1qBS6kzNItlTtbtMwoLAjsBh0_H0fuxKwFIPTLVEKIh3l6AZE2gVHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa60631d07.mp4?token=HP6rP2rC1qCYIcbo4YCB_AoFjhOoRP_Q1XRIAZ6FrCvIQzMmXX9FNBMWu5few_DmjL2awwkWWJ8luDhtzf2G8oq3VzrtwrzGZ-KZYVWCENdL_DDePWOcivULVhqM9vuHArpysX6Vb12hbzguYtFPc1xbCw40gIPwDuXRLOSVKXP9TLBKTdHsIRCJbsVYskIGAiHmYatoJ7aGM2UM06Wqx-ryq42eNruEcciK_lLZN33FxNXoSrF6VJAH_RbICJnh7PflLxJ7aL2bysxaYJyQUWK80eCeuJDI1qBS6kzNItlTtbtMwoLAjsBh0_H0fuxKwFIPTLVEKIh3l6AZE2gVHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات رژیم صهیونیستی به ارتفاعات علی الطاهر
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/688846" target="_blank">📅 22:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688842">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
هر شهر، بخشی از یک روایت ملی‌‌ست...
۹۸ سال کنار ایران
🇮🇷
🔹
کردستان
صدای ایران؛ سرزمینی که باید آن‌ را شنید
و باید آن ‌را دید... در مهربانی مردمی که ریشه در این خاک دارند.
#اعتماد_می‌ماند
#۹۸سال_کنار_ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/688842" target="_blank">📅 21:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688841">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3838521fd3.mp4?token=sHnuYMxvPG1e5n2BiqKjjl6oPmIIxnLG_kTnvirYz1H1RCo_6jSjL8HQdWGbuSnkDf8F4mAJJnl-jKdJEvn7rSKWIX2a-IqeIfT4iwucu_zYRYxkvXIG5TDy978IPZxyC7mpG-f3SzBXix7IyN4fHwO7DijiYdeSg_oguDHP5r4NnYPP1Qico9b88oaIWAycgYIxVVO3Un2l2L7GxybKhRRw5KrE7BcZJlZBQYt_4VsBuxjlakFSp9z4j0G0BFOYGtiPhTJdpPOqMogQY3gfSkXqVUIvh1udKtrlS89hzu28sfbwpebemtHTEUjVsxgAUCBihn65zO7NIh2vUjpcBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3838521fd3.mp4?token=sHnuYMxvPG1e5n2BiqKjjl6oPmIIxnLG_kTnvirYz1H1RCo_6jSjL8HQdWGbuSnkDf8F4mAJJnl-jKdJEvn7rSKWIX2a-IqeIfT4iwucu_zYRYxkvXIG5TDy978IPZxyC7mpG-f3SzBXix7IyN4fHwO7DijiYdeSg_oguDHP5r4NnYPP1Qico9b88oaIWAycgYIxVVO3Un2l2L7GxybKhRRw5KrE7BcZJlZBQYt_4VsBuxjlakFSp9z4j0G0BFOYGtiPhTJdpPOqMogQY3gfSkXqVUIvh1udKtrlS89hzu28sfbwpebemtHTEUjVsxgAUCBihn65zO7NIh2vUjpcBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سازمان رادیو و تلویزیون رژیم صهیونیستی: ارتش اسرائیل امشب تونل‌ها و زیرساخت‌های موجود در ارتفاعات «علی‌الطاهر» در جنوب لبنان را منفجر خواهد کرد/ فارس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/akhbarefori/688841" target="_blank">📅 21:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688840">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
گزافه‌گویی نتانیاهو: ایران بار دیگر تلاش می‌کند تا به سلاح‌های هسته‌ای دست یابد، اما این اتفاق نخواهد افتاد/ نیروهای ما عملیات خود را در تپه علی الطاهر در جنوب لبنان آغاز کرده‌اند #Demon
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/688840" target="_blank">📅 21:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688838">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خبرفوری
pinned «
‼️
خبرفوری / تنگه باب المندب به تسخیر رزمندگان یمن درآمد
📲
🇮🇷
✊
@AkhbareFori
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/688838" target="_blank">📅 21:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688837">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1e7Op67R2r15f_VXGjOOFDGAya2U7Gor8-WhIDwqCkJW-kKhwPznQC4ZXk_AMIeptEAgvs0bEpxfTPSnNPTIxBM5swc5zVw7ABsgRmXNw_bvjpNVKaPKT1kZxbpHzgfF67PPllXIRCkQ_s5RZrEuO6klb7bghtvEfgUhdIIV5-KVRmiUN8SAkpyVnWR4ozfHdN__af-DqINOvJLbgrwPQECSaKTHFC1YAwGkN8LwOGv23KJvzzQth6xdohY4kvQey2qgnwi0B4I6qYfW9PIHC0CVqzkNvqOxrRTwNWwI62hs41IKi7LLAWa7CmRLSwkSpbrufmYKmfN2YR7S7wHkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای مجید شاکری، چهره نزدیک به رئیس مجلس: فروش نفت ایران رکورد سال قبل و همچنین کشورهای همسایه را زده است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/688837" target="_blank">📅 21:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688836">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
پزشکیان فردا به هند سفر می‌کند
🔹
رئیس‌جمهور، فردا برای شرکت در هجدهمین نشست سران کشورهای عضو بریکس به دهلی‌نو سفر می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/akhbarefori/688836" target="_blank">📅 21:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688835">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
الجزایر روابط با امارات را قطع کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/688835" target="_blank">📅 21:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688834">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db9287fd29.mp4?token=tW_YFSUTnSCHk_HBa_z1KP3ElM5OlAqoJFxl24-Mg6snj_pHU-8k9rPBvxx8evIRyuCOMO1rCjMAk-Djfh_4paX2gxdg9Deu7TQEW8LRz9wtXZIBGUW9yOSFb19ykct5bzElxPxHa3J4qSiOAhxpye0U07zrhIkMnhSVZXD1cwIJ7dnTse8P_RzT_iK4TSNmJQDNsJtndt7KovOgOES2MfB31eyjA0vbejw0Yx5bnxY4PGI28y7Ip3XfmHjQI_EgBQRaCSdZzmi9EgFCkxp6OualnSJHRZnSZmIBGfyckLy6sZFf1cPXwyX8NYZcMTn77SZ9DE387hnJlyrt1EUdkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db9287fd29.mp4?token=tW_YFSUTnSCHk_HBa_z1KP3ElM5OlAqoJFxl24-Mg6snj_pHU-8k9rPBvxx8evIRyuCOMO1rCjMAk-Djfh_4paX2gxdg9Deu7TQEW8LRz9wtXZIBGUW9yOSFb19ykct5bzElxPxHa3J4qSiOAhxpye0U07zrhIkMnhSVZXD1cwIJ7dnTse8P_RzT_iK4TSNmJQDNsJtndt7KovOgOES2MfB31eyjA0vbejw0Yx5bnxY4PGI28y7Ip3XfmHjQI_EgBQRaCSdZzmi9EgFCkxp6OualnSJHRZnSZmIBGfyckLy6sZFf1cPXwyX8NYZcMTn77SZ9DE387hnJlyrt1EUdkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه‌گویی نتانیاهو: ایران بار دیگر تلاش می‌کند تا به سلاح‌های هسته‌ای دست یابد، اما این اتفاق نخواهد افتاد/ نیروهای ما عملیات خود را در تپه علی الطاهر در جنوب لبنان آغاز کرده‌اند
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/688834" target="_blank">📅 21:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688833">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HP7K_zD5yVPpgmlP4PKOvKFT84Cm0R4xmV-4yjbFPhRW9to19zoogB-edx4SS3j2xkZudru2YUkdP8ykhunkdikUgx7FqLqIQAWn65J82mQ-0kTEImNVbWNX7TjxO9mKokks7UPHVS36ssPEkMbVg3vuttblY62KSJ16miJwcX1NbGSU6-To73yi247IIP48MU2H72OKihSrIlGfh34BX7ROQUXGVdahSBrb-KXhYnuAci2m1pWObgqTzciOmOPrymNaujo6j3ImP_mGM-rSVbn5kohkMIHWMQ31oO_T_qb1Vj0ro_boJbi0MnFaZ7gVt-5H5oYHnl7599kGoiBQuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تایید برنامه جلسه امروز شورای امنیت برای بررسی برنامه هسته ای ایران با وجود مخالفت چین و روسیه
🔹
۱۱ تایید
🔹
۲ مخالف (روسیه و چین)
🔹
۲ ممتنع
🔹
این رای گیری صرفا برای تعیین برنامه امروز شورای امنیت و تایید بررسی برنامه هسته ای ایران صورت گرفت و رای به پیش نویس…</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/688833" target="_blank">📅 21:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688832">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49629bf6e5.mp4?token=TmyGFqukrJBosTBCNNIJ8gFNnU419weqVuhz0E6koPAcYSIxIkrr4ek1i7X4uZQffnzFilFY2J6jR35XmzQNDUxwLGVzgua6MsWwBY6T-BW1ABXi6pwSgQ7OlcdwIDxCozIfBdy0wLQ4rZuZG57KwFY2ed4cyh2VZGYSXJTSJFKMY76UBkpiq0-j7o9lRmRICjNXJb8B0hyPvV7iIMczPFyaYzhnmAPgmnnj5MGgHub14fh_1q8BF0NhNIAWSzckYfHISmv5edHfY9TTKfHGNXiuz9SFlO2sDamNAqwV5x-TKBY0ja6KQ_BnS-ei1quIxp91QK_T_SNREV0x1GBJPByM_npHSffdWWKb6yStx9-f68JmnSKlF1oNtKRe8-P7wKXG5DxIl8SrxNgWBGrsEemjfIG9edspUtu_mPuTvMu0qtKaYNE0G0sB3yZMtV2RyUCjq3QoHm1NJ1HNrovqWSfZEXhH3OKR3VF3mrhx_IeuxZmfNM33cPz2NN3-siHhOqbiIBV43HJ2oRi0yFOxk8AAbfF2NwZNB2FFrjnq27OBt2K_CRnO2qhdnR5cYiCeuNpV1ook71VLMDMQwLIsXy415bkKts_tjYO5JhFIexUdCMeLgr6U2TtfLci-PxLSvSvxGTLI2hKMsDcTOjQh-6-AM0_FxGOaDanRZ6O8A88" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49629bf6e5.mp4?token=TmyGFqukrJBosTBCNNIJ8gFNnU419weqVuhz0E6koPAcYSIxIkrr4ek1i7X4uZQffnzFilFY2J6jR35XmzQNDUxwLGVzgua6MsWwBY6T-BW1ABXi6pwSgQ7OlcdwIDxCozIfBdy0wLQ4rZuZG57KwFY2ed4cyh2VZGYSXJTSJFKMY76UBkpiq0-j7o9lRmRICjNXJb8B0hyPvV7iIMczPFyaYzhnmAPgmnnj5MGgHub14fh_1q8BF0NhNIAWSzckYfHISmv5edHfY9TTKfHGNXiuz9SFlO2sDamNAqwV5x-TKBY0ja6KQ_BnS-ei1quIxp91QK_T_SNREV0x1GBJPByM_npHSffdWWKb6yStx9-f68JmnSKlF1oNtKRe8-P7wKXG5DxIl8SrxNgWBGrsEemjfIG9edspUtu_mPuTvMu0qtKaYNE0G0sB3yZMtV2RyUCjq3QoHm1NJ1HNrovqWSfZEXhH3OKR3VF3mrhx_IeuxZmfNM33cPz2NN3-siHhOqbiIBV43HJ2oRi0yFOxk8AAbfF2NwZNB2FFrjnq27OBt2K_CRnO2qhdnR5cYiCeuNpV1ook71VLMDMQwLIsXy415bkKts_tjYO5JhFIexUdCMeLgr6U2TtfLci-PxLSvSvxGTLI2hKMsDcTOjQh-6-AM0_FxGOaDanRZ6O8A88" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش صداوسیما: بهترین برنج را کیلویی ۴۷۰ تا ۵۵۰ هزار تومان بخرید؛ گرانتر نخرید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/akhbarefori/688832" target="_blank">📅 21:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688831">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7ggwsNu2eN5CK7zZOwcxnFkA16gERCjE3hTw49GdAj03inFKy-OWSzhYcSgDiUUbaWvN9A66m4wabC74IJeJcICodD8PuIFNaE2EJnEiqjvosqpv5vkrtgqGFF82Z699J-cdou1HQB7REjrXPT4MEK4gvJJ3mf-vcNjChs0ERPo9g_OCYI3qjAXjXmhKCW1QX-hN12XGZwfGkM7TnTWOEZDckhz8F-SVPN0N21FvXvwLgJlsryLeMD9g4PDH97kEp0f6yV9ALRtcIdH7J5CurRR723ifU3W-DlZFDu6Sw9GeVTIdgRkHJbSSt4m410_g5QwVf-N0EHFfQiI11aT9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تبلیغ سازمان مدیریت بحران کشور در فیلترشکن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/688831" target="_blank">📅 21:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688830">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ادعای رویترز: ریاض از تشدید تنش با انصارالله پرهیز می‌کند و فعلا بیشتر به پشتیبانی لجستیکی، تسلیحاتی و اطلاعاتی بسنده کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/688830" target="_blank">📅 21:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688826">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L-PSkUDFfj32rxdMd8FXRfaDB0WwvtBzL9wTHQhy2dedPoSuwDgxo7y3fVRu34xzKHD6mj12OBHB0jqVJ8cXWI5jLniP6J8Ifov0UKKX6nq4iFY3AXHOllB4HQ7GXILCwgGCGVvD4SXjwWDJ67AmIV8YqCE3HJrxJbLWpHrh_Cb8-AI2rLLOWtXQ333LPxqcwikXpYTgtFXmN5jRst3bcUyewzDWGZY8_XTZdUbRE5DG4Dsf4dKughzuuBrRnP1FA37SHNTDbowaw6byIvL1doHQEBky0uwLSQG4Za9Dimbe9Lhqt14z3nySfs6dVsZ1DKApGSIxROHNgl5omxbvGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WA7PgtWoKMCwWOSOUORY4RIOSPQaEUN-gVT2o80rB8ojswBNIlQDZfDeHa5YjWIm0nVeiGbsHPIgOyQXfxazadazhRB0Ab3gh-WTOF6yRTQxzqt0PAESIpetVXisjKDg5VZXGeTCazTp-VuPaCiF6o8pE7VNdPEXMlhOSzQ8LCVjMGxz_8LaxfRmrCi5MxZjtbGa22hEb6TM4fAhEbR8RcIWPjPkTTM2netUc3168Ty954y0j7s8eO6nb0U0vvmutLUtyMJfSek_ktlETKI8tuX2xWByaxJQUI6V0pUNZeK75KPUetLIXAqB5zSHJVTq6XcQKwNXpG2OIWG36JgONw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pX2EICWY2udl72qGFneH__va5sDlD7e96yGS_dac21kGz-P8lSgtTo3AD477A4f79uCHjh-NQdNajE3Vqa_yj-X6cA2q_i6s_DCM7rM3KqtWiBuIr0PbRpzjs6_LFUhWjp8s1Lgwibskf6k78VqJLcFXJEi916OpS-QVTFMH6wTx3dlt_lCdAwACBVMSGB7hBNpsrbX7X_KG_FDm9qGZnw4F6dNa7iMD4QuCkdNxz9irqLW2pL9tSx44TIqS5JL6M3u1VAI3Px752ayTox95EP--HyNqDqs_h8QK1cnueAUWoUZajEwhdADfqI93oVmgvgyhMVgrNqD6RwbxvuEX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/crjOnEKz6FJFacd2zf9xepRQISoOpQBMmSuzZLW31dT6r7pNDMayo_FoktoV_lzu_n9uGhyirInrb-zpmdLsglbE8vyiNmyBk0QIApF91SOCzOPBH2_uKbYB6b-Ym1veAde48JK6Oruioa7ROxLfn86eid9_V9SLQnrOzfMorLapqxSEZ3HX22KLdevuD51SnPVBneOZcNZwn9ESk2JL0RkPILKe8p4-w-U5pvP47yOyGymR0towefh2giLnwerqL1bkvcd8qjY01WSNrgT9GNSVRVYsHx4ChXW5z-wu8Y6ermXDtFC_cm5nqZ82KPBwtuZO1R-Y3sILU3CbORJunQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از پهپاد سرنگون شده سعودی در آسمان یمن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/688826" target="_blank">📅 21:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688825">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOQbqpG2WxAdexrKOl1i94H0e2xPhIZw4e2lhcd8RBMJuXFn_lvpzkrPBvWTG5gHe8OlwJsptAD4YzFHjw0YegeXspRxwFbui0QU-9XgpwCwlSFQkSro9nfzXHzoJvI-qevQtPBw_m3QOHbnR72tFLUNTP1jQmSy2Cn1ovWI-KOYkm0jEWjybiIjmhqZ_NafqBhFmgIc6qZrr7sqiR3_cpAMKe7IHHUbanh6mGxy3E9bi8eJgSF2Ii2OMHTDKLYdTAMMv9mxq86jQIY-a271n85sLMkubhPuXRauSwe5kJmBZ0IAUd_bfPGct69fasR5h4Rou4pe6VKnP7nN4uyVIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ پولپاشی کرد: اگر در انتخابات پیروزی شویم به هر بزرگسال آمریکایی ۵ هزار دلار می‌دهم
🔹
مجری فاکس نیوز: ۵۰۰۰ دلار برای هر شهروند برای هر رای؟ یعنی ۱.۳ تریلیون دلار. رئیس‌جمهور در حال رشوه دادن به رأی‌دهندگان است و کشور را ورشکسته می‌کند.
🔹
ونس: رئیس جمهور…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/688825" target="_blank">📅 20:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688824">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dS40-AEzkPJls86wmy9vDrXRhyMAxw9C0JM5nYZIrWbyuQiOxvaxkNwz1iVjxD9KCDgsGNDj7_lKvvKCYS-App5LhEmKgkCpxHw94a8Xk464k833tQsq-q-L4d-EvO_5d1tOFtJyTB0hPSG31Y1UqQ4CSJbKebJmHRMlLEhCF2BfxZdEhJ3Pxs-fYsxZSwQQVSJcOZATJurlO0NQWM94zLm8GgLOuQLg_BbDYiIwaOHluSLDeKkizzw7oVVKGnMIDev1hjZKvwhI1oZsRuMvJFD8BNdE-rWd8CScGsgwSr8oXVPv3M2k_rJI7u4CW3IHd_LWFQcfvxnTDaumRue7uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آسانی از روی نقطهٔ پنالتی استقلال را پیش انداخت
🔹
استقلال ۱ - ۰ پیکان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/688824" target="_blank">📅 20:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688823">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQkgsgiNqyeKtXcs7c32rcyNMBOIlNk8nj1cocoRCfK-cidg08Z7NxU__iWRXoSFJjOgLoixbf950tRdFMs0zNfU-C1Q5vib_GoJKomCgNdRrmy6gEKSD8ytA98f2l_-GeKv2ThoWux0L6kKOByrwciCMz_8PsYcZi11Xwj1wu2bYnUUAYocBB9h1HpwfzcTkM3s78Ks_xxKQK6A1q1FK3HwmckX0WMyT5RdHRoLgA2zXytlpSjtjuLbhJp86HQh425moXOTCxDNS_HxinAvi7gwpe6y5YrTms3rMT833uAL5q9vTlLRE0TshmW2cPFI8680zKZAUpapzADFmuCUEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چند ترفند کاربردی اما ساده
🤯
#ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/688823" target="_blank">📅 20:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688822">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: ایران تولید موشک‌های بالستیک را از سر گرفته است
🔹
به گفته مقام‌های آمریکایی و خاورمیانه‌ای، ایران با استفاده از قطعات ذخیره‌شده، در تأسیسات زیرزمینی مشغول مونتاژ موشک‌های بالستیک است.
🔹
فعالیت‌هایی در چند تأسیسات از جمله مجموعه موشکی خجیر گزارش شده و ایران در حال ایجاد نقاط جدید مونتاژ زیرزمینی نیز هست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/688822" target="_blank">📅 20:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688820">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خبرفوری
pinned «
♦️
نیروی دریایی سپاه: یک فروند شناور بدون‌سرنشین (شمپاد)، با شماره بدنه ۵۸۳۸ و از نوع «سیل‌درون»، در ورودی تنگه هرمز مورد اصابت قرار گرفت و در اجرای مأموریت خود ناکام ماند
🇮🇷
✊
@AkhbareFori | Link
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/688820" target="_blank">📅 20:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688819">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a73d1b9a6.mp4?token=LjkyrzB2YpcjzLD8LwHK_yhVxrwtjQJp2L-erThJaerevn93xhXZanbnW2G6mbYv13FJJoLGZmswDgo2JTAf1z8MwV0YVHiAEDk9L_tvq8Sp0Bh1ek1DvSCx2ZS-_aOBO4HEH6wkqIoH5vaSvy7s67XcDyGEjwjK0DHmJO4FJnqQRIDds2D0dePxpx91pmAvn-KiSUkRuRvON2xVC7gWNMAtHY92I6sJCwCxWhq4SjfrDF6vQMqXlSb75kys7zWOshIiXHUck4XP0KVzCMUHkIC-EXtGQGv0xVlWmOcLJfu6lln31mBxqy7ni8PB9IsU_Vbt8A36fRqOzEe8vinF0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a73d1b9a6.mp4?token=LjkyrzB2YpcjzLD8LwHK_yhVxrwtjQJp2L-erThJaerevn93xhXZanbnW2G6mbYv13FJJoLGZmswDgo2JTAf1z8MwV0YVHiAEDk9L_tvq8Sp0Bh1ek1DvSCx2ZS-_aOBO4HEH6wkqIoH5vaSvy7s67XcDyGEjwjK0DHmJO4FJnqQRIDds2D0dePxpx91pmAvn-KiSUkRuRvON2xVC7gWNMAtHY92I6sJCwCxWhq4SjfrDF6vQMqXlSb75kys7zWOshIiXHUck4XP0KVzCMUHkIC-EXtGQGv0xVlWmOcLJfu6lln31mBxqy7ni8PB9IsU_Vbt8A36fRqOzEe8vinF0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آسانی از روی نقطهٔ پنالتی استقلال را پیش انداخت
🔹
استقلال ۱ - ۰ پیکان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/688819" target="_blank">📅 20:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688818">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ایران به ۹ جنگنده آمریکایی در اردن آسیب وارد کرد/«سی‌بی‌اس» گزارش داد در پی حمله به پایگاه موفق‌السلطی، ۹ هواپیمای نظامی آمریکا هدف قرار گرفته و آسیب دیده‌اند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/688818" target="_blank">📅 20:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688816">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
انهدام Saildrone آمریکایی در تنگه هرمز توسط نیروی دریایی سپاه
🔹
نیروی دریایی سپاه یک فروند شناور سطحی بدون‌سرنشین آمریکایی از نوع Saildrone Explorer را در محدوده تنگه هرمز هدف قرار داده است.
🔹
باید بدانید که Saildrone Explorer یک USV حدوداً ۷ متری و مداومت‌بالاست که برای مأموریت‌های شناسایی، مراقبت و آگاهی محیطی دریایی (MDA) به دوربین‌ها، سامانه‌های ارتباطی و حسگرهای مختلف مجهز می‌شود. این شناور پیش از این در منطقه توسط ناوگان پنجم نیروی دریایی آمریکا و Task Force 59 به‌کار گرفته می‌شد؛ یگانی که مرکز فعالیت آن در بحرین قرار داشت و مأمور توسعه شبکه شناورهای بدون‌سرنشین و هوش مصنوعی نیروی دریایی آمریکا بود.
🔹
پایگاه دریایی آمریکا در بحرین در جریان جنگ هدف حملات ایران قرار گرفت و از رده خارج شد! اکنون Saildrone توسط یگان مستقر در محور خصب عمان استفاده می شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/688816" target="_blank">📅 20:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688814">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cqepock_Rg18rrY2i6aOTguipPuuR1oEszFuiUmZBwXPk804A0DdZ8aiy011Rg09DX1VXNext6l3OBqixfWLnlt9sJlQtszN8_ycAYdBlWD22Fdm-uw_qjYUY1V0rwAUCUP-d4ruGwWLnudOdVY-EYqzHd6QCmS3qS-G7s-aqB3dOKK5CJTErTOJMQfgP3kjm8qbhKEDSBF8If3viov687w9_b2uodaU0orC5WAUTtPzfsBte7RZ2zGLO89hc2Tg4qym-vA_OoVWCDkIxpcA4zPCkBgGyiUdWha1QdCIBPyfDXjsFGrSD8-DM6RO2yPfMOBzIIS-L5K5XkqYzI2Bxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5800849858.mp4?token=kisHjy4nN7_TgPSfLtGgMgjRPVZwQ_tA8aw3yBEBTou_szG6zHGtRDtE8WWtCenPCkvEO6EoZ34wanNxi6nPJB_A-h2I1vz6QyNv3ZXYAhKnOyMUGZ_rugE3RnZUTccfFjEFQ-gEjdqleQZpCxuYxJhsLLlwEV1OiF6MLgGhtYkUfw3XX-Nyq1DrG9AscAENp5aAAuaK_1E-4Wqoe8V3sR-UtnLPV0qU3yCZEVDKdjY_mgZ2PWD73jrFQbzXX1FtyksfSvItAKKjVR8T8Bi_m5ICVvdEPDTLA_C4wDEHpKlGOauQ1iO5vEyCrmTWaQKxK6zDQS24SuJBwzbadUZBKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5800849858.mp4?token=kisHjy4nN7_TgPSfLtGgMgjRPVZwQ_tA8aw3yBEBTou_szG6zHGtRDtE8WWtCenPCkvEO6EoZ34wanNxi6nPJB_A-h2I1vz6QyNv3ZXYAhKnOyMUGZ_rugE3RnZUTccfFjEFQ-gEjdqleQZpCxuYxJhsLLlwEV1OiF6MLgGhtYkUfw3XX-Nyq1DrG9AscAENp5aAAuaK_1E-4Wqoe8V3sR-UtnLPV0qU3yCZEVDKdjY_mgZ2PWD73jrFQbzXX1FtyksfSvItAKKjVR8T8Bi_m5ICVvdEPDTLA_C4wDEHpKlGOauQ1iO5vEyCrmTWaQKxK6zDQS24SuJBwzbadUZBKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروی دریایی سپاه: یک فروند شناور بدون‌سرنشین (شمپاد)، با شماره بدنه ۵۸۳۸ و از نوع «سیل‌درون»، در ورودی تنگه هرمز مورد اصابت قرار گرفت و در اجرای مأموریت خود ناکام ماند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/688814" target="_blank">📅 20:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688813">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
نیروی دریایی سپاه: یک فروند شناور بدون‌سرنشین (شمپاد)، با شماره بدنه ۵۸۳۸ و از نوع «سیل‌درون»، در ورودی تنگه هرمز مورد اصابت قرار گرفت و در اجرای مأموریت خود ناکام ماند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/688813" target="_blank">📅 20:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688812">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zn_h7em29E3aqMKckjfoztL_iqstyHmrITyz8x5u4z198bnBFseWLylHqsbBOCz7d5QeZfygWJ66JLthQE_yS3kFNlXEAULxKHJouYZIbw03joa9ef6BhbSXFVVLgKna83J6xguPmT5fPvjj7782n6KfOdpX9nKhaaRubfU5V1b8qT7dy0jlEfzXdDAFUgG2quwP-uqNJ6HBidDnOfqK1p3Hc89tX43sgNhPrGJfwD4YgiiFTIgR4_j_qVTZxzinnwh631hjQWy0MTLnPEdglx8bJNqkJZRI0ltmphSWcYZXE2zTHKi4ktPFohQUxTqIaf4Bey5QBXkD9EELFCKYZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: مداخله‌های مالی و یا حتی دروغ‌های خزانه‌داری آمریکا دیگر تاثیری در مهار قیمت نفت ندارد
رئیس مجلس:
🔹
اگر دنبال یک راهنمایی برای آیندهٔ بازار نفت می‌گردید و مقامات اقتصادی دولت آمریکا چیزی نمی‌گویند، بیایید به آینده نگاهی بیندازیم: وزارت خزانه داری برای کنترل قیمت نفت زرادخانهٔ ابزارهای بی‌اثر خودش را (از قبیل دروغ‌پردازی با آکسیوس، مداخله در بازار، آزاد سازی ذخایر و…)خالی خواهد کرد ولی اثری در کاهش قیمت ندارد. این نمودار را ببینید ولی وانمود کنید که نمی‌دانید مرحلهٔ بعدی چیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/688812" target="_blank">📅 20:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688811">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lT5GPiCi6RonlURR0g61OPB-MDtQFsDoXNsQAKvfOtZptEfMYabKMWREb1m_A029ntLwUqz-ZO52ww74G-PiAJMaQNaewSEh1DpzGasYNevnjYN73YueJbj0QDeQ2JqAmEExDRkT3JFpnb2HD1cFVUKufjNYc6_zTT6zlheXseQu7Ef4z2XjNAPbl_rV96io5lJLHWM2YQV_78gxHGINBS8G7V8M4rtHMHrzWgdYRvf4QJeYFKzZmJ5inoxkEQ0Sr7SNeJwhOBM5djm6Ta-CRfAtmXCHRRvOTeKHVUOW-b39h60OaPQUr_DBA_AWHVUzlF1XgMRqo9xByHXLM04OMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مسکن‌های رایج و کاربردهای آن‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/688811" target="_blank">📅 20:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688810">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
نماینده چین: ایران به تعهدات عدم اشاعه پایبند است؛ ایران عضو ان‌پی‌تی است و از حق استفاده صلح‌آمیز انرژی هسته‌ای برخوردار است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/688810" target="_blank">📅 20:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688809">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">14-2 Ane Manaee (1404-01-30)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/688809" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه چهاردهم؛ بخش دوم
حجت‌الاسلام امینی‌خواه:
🔹
مرز انگیزه‌های دشمنی، از حسادت و رقابت تا جنایت؛ ..و وعده‌ حتمی عذاب الهی برای براندازان! [00:00]
🔹
کشتن ناقه‌ صالح، مصداق سنت الهی در زدنِ ضربه ناگهانی در اوج امنیت و بی خبری! [08:07]
🔹
معکوس شدن نقشه‌های دشمنان از یکسو، تکفیر خطاها و پیروزی مؤمنین از سویی!.. به شرط «ایمان و عمل صالح» [09:40]
🔹
معیار اصلی قرآن در تفکیکِ "حسنات" از "سیـّئات"؛ تناسب با مسیر بندگیست [13:51]
🔹
پذیرش و تبعیت از وحی و ولایت؛ رمز تکفیر سیّئات..و این یعنی «ایمان و عمل صالح» [21:08]
🔹
وحدانیت و نبوت ریشه همه "حقیقت" است، مستقیم یا غیرمستقیم [26:50]
🔹
"نصرت خاص الهی" سهم باورمندان واقعی به "ما نُزِّلَ عَلی محمّد" است، نه مؤمنان نیم‌بند با ایمان ظاهری و سنتی! [30:42]
🔹
راز شکست‌ناپذیری جامعه قرآن باور؛ حذف پندارهای باطل از جان جامعه است و اتصال به حق ناب [35:12]
🔹
«مدرسه تعالی»، تجربه‌ای زنده از نصرت الهی در طوفان بحران‌ها، برای متمسّکین به حق و باورهای مومنانه [40:28]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/akhbarefori/688809" target="_blank">📅 20:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688808">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
شعرخوانی جدید میثم مطیعی علیه حسن روحانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/688808" target="_blank">📅 20:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688807">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
روسیه در شورای امنیت: اجازه بازگشت تحریم‌ها علیه ایران را نخواهیم داد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/688807" target="_blank">📅 20:02 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
