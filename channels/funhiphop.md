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
<img src="https://cdn4.telesco.pe/file/o_lRHE93BO-BlXU0ssO8OVadZk5JJ1iT6FJx8IG_jDOxv6BrHMN_IKNS3M4PVHLrhC_ii9g3fHJQsaU0mz-3na3bmzBg8v27AXbi_sWrSuXYqP6kbgaUdwlCyypdZldJdH46Uf0tHdIcNAB1oj1lxMQFtDlfikZyqhFXr8f_RfX3kzvclz0ghXR9PjlvOG6jXBgVokiKxeCi1dh0-Zhs9I8NOWJF4c-Bi-J0MTHHMRwgLG_5_mUtp9QObz8vz_g-vq3-IWufFmoE-C8x16VeKvtpv_OTi9SyFwS3VK5COuUovUFxrgPMFD9HwKqLmDcuj_JcwKk_S85TBj9lGutaCQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 205K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 18:01:49</div>
<hr>

<div class="tg-post" id="msg-81069">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ: از این به بعد، هر زمان که جمهوری اسلامی ایران در تنگه هرمز به یک کشتی شلیک کند، چه با موشک، چه با پهپاد یا هر وسیله یا سلاح دیگری، ایالات متحده یک پل یا نیروگاه را بمباران و نابود خواهد کرد، از جمله آن‌هایی که در کنار یا در شهر پایتخت تهران قرار دارند.…</div>
<div class="tg-footer">👁️ 623 · <a href="https://t.me/funhiphop/81069" target="_blank">📅 18:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81068">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">توافق قطعی شد اکسیوس:  ترامپ در حال بررسی از سرگیری عملیات نظامی گسترده در ایران است، که احتمالاً شامل عملیات مشترک گسترده با اسرائیل خواهد بود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/funhiphop/81068" target="_blank">📅 17:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81067">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">توافق قطعی شد
اکسیوس:
ترامپ در حال بررسی از سرگیری عملیات نظامی گسترده در ایران است، که احتمالاً شامل عملیات مشترک گسترده با اسرائیل خواهد بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/funhiphop/81067" target="_blank">📅 17:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81064">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kUB2q1zVHuCBYxSxcvDsIei4v3da_Oq3wElQ9IaAI7PsKkp4Qg5m_KpjpmgYyTgvwnFb-0A7_ZGLyQJeOcu4csPNITRNlE-A0uGEXaiecfxGr1upcbKvT0DZdxNdwrnLyn1nEKJgUvO9M4_I6WKNHKzQ0E8Ou5ZWVX4bnZjg0fZz7IfS9xBMH603PIl9zwNhEdgjIZKwwk4IT8hHoKkw8aKvTrZnBXJvytt5U8dI-RjGYjzbWmqbP32GemCIE8YTs0Fmn-ysXn7ZSba0ifYfeCuJC6fd39Yij7atMUj-xBPGGVTkL3QZY1SOqKpcRVz1URb51agL4SHVBHykc3cSIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pu3zu6qMbxZ8y1n8Z2nSiqznOE2HqxwP3eLdvGjhoMMYQ55vezxVolmAcqPsqW5sfgvVB0HFSJEHqdvBo821eGZfYayx_TZEuuOh7BQkBEzmcDMxNQ-QPGv8wptSNFGE5ZEBe0644_KoQoPNN0ncIQo0JF6bnuJXzzEiIqgoLOuxUEApWv1vf5u8gW8SxoJITO1ufY9qmSG87ftQVUxKY3tyNB4881JRe6xBGUEdaAtBCUgu_P3iqRmRSXL6k2Ra831Ze4uy6c5V4c3MsqsZnXSRnitx_zX5R3ahJsZ_rdcq6ptEzvqYRKxyOElwvBeFI5a21YWWWkexrdVntMrjJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SKWzvz6W_1OweKhgiZIZ2ku5HoKSXc62B-ZjgNw0xoyCAl7NIF4zqU2WSNzLJmJoTEZ8vRIO3Pdz0yGEYON0N1kr3Rutm3kKYU7vO7qLWAYL_xgeNqxJt27Tgo-mNv558o7UsamIZa4UfN39JqYxrU3eajf5cNo1ZUwuYFfF4EmeMujbVEp6r4N2UK1UJ-FAUVX5rkcSEOpG4vvsGfqsX8yNGRDluyr4FWJkeEa0RFV0b_ecOzXI5N1Qk9IaG-CeiaFSAOKJFznl6KkqiIZsTxwi5S3jtqU_QNVeYHNqba0mxP9_hMqns2XXBPK7Eajri2ubRXnnbd2vcpgRE6oEwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا ک بحث عادل داغه چنتا شات قشنگ ازش ببینید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/funhiphop/81064" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81060">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دلم برا رها وانتونز زیبا تنگ شده، چرا عکس جدید از خودش منتشر نمیکنه؟ شنیده بودم این اواخر ترکیه زیاد طوفان می‌شده امیدوارم باد نبرده باشتش.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/funhiphop/81060" target="_blank">📅 17:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81059">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دلم برا رها وانتونز زیبا تنگ شده، چرا عکس جدید از خودش منتشر نمیکنه؟
شنیده بودم این اواخر ترکیه زیاد طوفان می‌شده امیدوارم باد نبرده باشتش.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/funhiphop/81059" target="_blank">📅 16:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81058">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ: از این به بعد، هر زمان که جمهوری اسلامی ایران در تنگه هرمز به یک کشتی شلیک کند، چه با موشک، چه با پهپاد یا هر وسیله یا سلاح دیگری، ایالات متحده یک پل یا نیروگاه را بمباران و نابود خواهد کرد، از جمله آن‌هایی که در کنار یا در شهر پایتخت تهران قرار دارند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/funhiphop/81058" target="_blank">📅 16:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81057">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">این یعنی تعویق؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/funhiphop/81057" target="_blank">📅 16:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81056">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLIlrjEZB0kyn0htyMTFUvRxAQW-CWgksqLwd1WPNXv4b2bhC0fTyP_LPrkm25JoIw8gg2F_5QW7OMJu4KM_lJT46qlDOutG8q_qclria_eivRX3fMl_lqNx3QEOoTPA-gDOCbL34F8HD9VOR-6Mlt22G2vbtjn1fa7eOuZ4HLDQdPuimdHTjEUm2e8LX6t92F7fkq6HkLyZD5Om_BnEpTbppM6MBG-A937FGgn3jQsIsQuBmW7GWxbGQya78ksk7p_ezCmQk96p4e6N6o1DQIO-v7EjDrNzZ0RR_BPVMKbkNbFnzn-SFfynEYCgg1MJLMbFTHTo60CZvyaZ-U6IOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس گرفت رو فردوسی پور
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/81056" target="_blank">📅 15:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81055">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">داریوش بالاخره ترک کرد، شات جدید داریوش بعد خروج از کمپ.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/81055" target="_blank">📅 15:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81054">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCdp2pqY_NhZY40ddFZpRMZLpwiLX53zdVOeQvGSLfXOXj863jGWsosb1aoUFlbOWulo4RzqdisTObXZ8StOW0G7FVs_VSf4Og6sSJBoupfMTaaql4-LJIisQzvIZJXFyKai043CJxlUsDuo7kGP92mJa5Qs0Mo-legHP5fgj9QgxtzQ5n37pT-dDEndeDe7aPyUT8KV41BZOJDqNsREN-x1eLkIhouPHhuTVvFy0E53bIcngRl-aW_ohKf4lUd_OEni1OOX3ehYLMp-agbyBspQ6XU7_1NroaTb3Gs3VKExS1ZktgI5sFVdmjlnYK9wGE2BldBKtctl6npFqDxxQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریوش بالاخره ترک کرد، شات جدید داریوش بعد خروج از کمپ.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/81054" target="_blank">📅 15:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81053">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سپاه: اگر تجاوزات ادامه یابد، آماده عملیات پشیمان‌ کننده‌ ای می‌شویم که اعلام عزای عمومی در آمریکا را به دنبال خواهد داشت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/81053" target="_blank">📅 14:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81052">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">امتحانتون چطور بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/81052" target="_blank">📅 14:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81051">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">توضیحات مراد ویسی در مورد فالو کردن عراقچی
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/81051" target="_blank">📅 13:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81050">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ببخشید چه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/81050" target="_blank">📅 13:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81049">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">لیونل مسی بعد ناکامی تو جام جهانی اینفانتینو رو آنفالو کرد دلیلشم به خودش مربوطه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/81049" target="_blank">📅 13:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81048">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhzX-q4EIoNJ_S5hvA_Xm14xQKut_t5LCof4TcXvWkTYGL-zhpmwMNFdQd_3NwpLEfUwCWO4LTQj0i8jWu_jV1QJQybZb0TegxGumo9EiDCElu6DyNpCFptiTCSXSZ4LuMiIQNdDVmUZ5bq1ZniumCzU6_UDMJ-vZKCnChKab-LA1-LeOwrtlgc8_XhBAc1Rvs983zx8sq7QW1dECpjtRZBuF53BmaiRk8VtgQdBnlpSx0g45r5uheJWIjNJeFBVa99OHkmIo6xsVkhhX3IeO1vsjX7GiSoJsuISD96RA7TUbm8HyuNgs7vRaeAFLlV8VTI8vBqi6-DtJjbj1dobYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا من در سطحی نیستم که راجب این موجودات نازنین نظر بدم ولی ناموسا سینک جای بچه نگه داشتن نیست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/81048" target="_blank">📅 12:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81047">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcrVq4XaNLm6M2jjbPvcDldvj7OaQYp_GLDf2-SbYCx6qK4fMgnSrCT369EE0e5QfljJ1J7N5O-MVMPFnU6bIIID1jGYpX_HE-MDGy-E2RnWk5mJZdJ2GKNokbJNxfe8AS2alf9q-Abj3Y1936sY4bLkjJSYXaY1am-CripptiyO-yMxfF7BOGATgLmXuqOSCrz_M31O08sOep6zs0l4XD0hfwSbPPLErass9CPjLEN5j6yVtK1txqBjj9E-E9CzJEVyuFC7bL_7rVRB_HqwWfy47FSGw1A9tXcd5HvxC6YiuM9_VcqrVy0wwTjC19GsnHL8R7Es8i2O2DZOLwdXNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
هوش مصنوعی را وارد پیش‌بینی‌های خود کنید
🎲
🔥
دستیار هوشمند بت‌فوروارد با بررسی داده‌ها، آمار و اطلاعات مسابقات، مسیر تحلیل را برای شما سریع‌ و ساده‌تر می‌کند تا انتخاب‌های خود را با دید دقیق‌تری ثبت کنید.
🎯
تحلیل مسابقات با کمک هوش مصنوعی
📊
بررسی آمار و داده‌های مهم بازی
💬
گفت‌وگو با AI و دریافت تحلیل حرفه‌ای
🛠
ساخت پیش‌بینی با ابزار پیش‌بینی‌ساز
⚡️
ثبت انتخاب‌ها تنها با یک کلیک
👍
هیجان پیش‌بینی ورزشی، این‌بار در کنار قدرت هوش مصنوعی
⏩
مسابقات را بررسی و تحلیل کنید و پیش‌بینی خود را هوشمندانه‌تر ثبت کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r31
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/81047" target="_blank">📅 12:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81046">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سجاد شاهی این پول ویناک چیشد</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/81046" target="_blank">📅 12:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81045">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">قبل اون قضیه نجات خلبانا میگفتن نیرو های آمریکایی خایه ورود به ایران ندارن بیان سلاخی میشن و فلان
الان میگن خایه اومدن دارن ولی خایه موندن ندارن، بمونن سلاخی میشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/81045" target="_blank">📅 11:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81044">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ویناک چند روزه به دکی نگفته پول منو بده دارم نگرانش میشم</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/81044" target="_blank">📅 11:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81043">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سپاه صبح ها نمیزاره عربا بخوابن آمریکا شبا نمیزاره ما بخوابیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81043" target="_blank">📅 11:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81042">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تو دنیایی که ملت با سهراب ام‌جی لاتیشو پر میکنن دیگه این که فران تورس جام جهانی داره و رونالدو نه چیز عجیبی نیست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81042" target="_blank">📅 10:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81041">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">زهران ممدانی میخواسته نتانیاهو رو تو نیویورک بازداشت کنه.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81041" target="_blank">📅 09:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81038">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">زهران ممدانی میخواسته نتانیاهو رو تو نیویورک بازداشت کنه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81038" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81037">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">همین بین که شماها مثل سگ استرس امتحان دارید رفتم سنگک گرفتم دارم املت میخورم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81037" target="_blank">📅 07:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81036">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ولی بیدار کردن پدافندا الکی نبود، حس میکنم امروز صب یه تیزر از اتفاقات فردا بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81036" target="_blank">📅 07:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81035">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سنتکام اعلام کرد عملیات امشبش تموم شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81035" target="_blank">📅 04:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81029">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تسنیم: دشمن اومده رو آسمون تهران ولی جایی رو نزده و فقط صدای پدافند میاد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81029" target="_blank">📅 03:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81028">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دانش آموزا بگیرید بخوابید فردا امتحانا برقراره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81028" target="_blank">📅 03:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81027">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نصف این گزارش های انفجاری که میزنن فیکه، تا الان پنج تا انفجار برای شرق تهران زدن ولی هنوز خبری جز صدای پدافند نشده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81027" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81026">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Ginza</div>
  <div class="tg-doc-extra">J Balvin</div>
</div>
<a href="https://t.me/funhiphop/81026" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کوبارسی اینو بعد قهرمان جهان شدنش گوش میداد من وسط بمباران
@Funhiphop
| Erfan</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81026" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81025">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انگار پوفیلا میترکه</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81025" target="_blank">📅 03:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81024">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromZahra</strong></div>
<div class="tg-text">انگار پوفیلا میترکه</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81024" target="_blank">📅 03:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81023">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پس خبری نیست، جنگنده اومده بود پدافند فعال نمیشد.
@Funhiphop
| Erfan</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81023" target="_blank">📅 03:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81022">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">صدا پدافند در شرق تهران.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81022" target="_blank">📅 03:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81021">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شبای خاورمیانه واقعا ی حال دیگه ای داره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81021" target="_blank">📅 03:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81020">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">شین: انفجارهای عظیم (حداقل ۵ انفجار) در مجتمع پارچین، شرق تهران
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81020" target="_blank">📅 03:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81019">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38b1c9a3f5.mp4?token=tXGrbc2fscYFku5yW40rWBposkbcq76JTkApm3kgwNi0Om0GV7VM1Mzx2VkfGljLCZVaRsnX0AuQXJ8usEsc8BXIUEWlQHfXk3Y8Wkv16Q3KSFvD1iVQoZzr_b53mu4T0raj_16sw1PzUarAgyQjZ66iP1hOg1Ef-8kmbVcC7UMCk5ZNeysrtSzR-oVgxMpVSnDnlM7VnGH3WW5-PwV2ASw5apGuTZkNgli4iQbz9ITaLPUk4BWrSva5gqhUAjUljD2mLQ6o0ys6SJw8EqPTbtrKPaipcyRRpM3PJ-5-Fpk2utC4We6QxhtcK2bBp4dVl1oqu5533jHbARWItlMhooWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38b1c9a3f5.mp4?token=tXGrbc2fscYFku5yW40rWBposkbcq76JTkApm3kgwNi0Om0GV7VM1Mzx2VkfGljLCZVaRsnX0AuQXJ8usEsc8BXIUEWlQHfXk3Y8Wkv16Q3KSFvD1iVQoZzr_b53mu4T0raj_16sw1PzUarAgyQjZ66iP1hOg1Ef-8kmbVcC7UMCk5ZNeysrtSzR-oVgxMpVSnDnlM7VnGH3WW5-PwV2ASw5apGuTZkNgli4iQbz9ITaLPUk4BWrSva5gqhUAjUljD2mLQ6o0ys6SJw8EqPTbtrKPaipcyRRpM3PJ-5-Fpk2utC4We6QxhtcK2bBp4dVl1oqu5533jHbARWItlMhooWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پالایشگاه بیدبلند،ماهشهر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81019" target="_blank">📅 03:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81018">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سنتکام:
نیروهای سنتکام از ساعت ۷ عصر به وقت شرق آمریکا (۰۲:۳۰ بامداد به وقت تهران) برای یازدهمین شب متوالی حمله به اهداف نظامی در ایران را آغاز کردند، با هدف تضعیف توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/81018" target="_blank">📅 03:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81017">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60f68ed4a.mp4?token=DsARYu7iAvhjSUWp9Sy3xpDovGrTVDCLl3Voeun5Hy98y781_FYFPVzm0uyvY3OB6bjQ206kbY0bAh1gSdcKXnJp4ludtrwEn0ZMvnxFZDnmaQIRAXjoUOPWgXcFap7hxVzgrGArfUehakfw0ht8ypr-LCx1WYyJxeQkJIFMjVs4y3EHiS5E8Yodpr0FQBAlb-qBldLwix5Wz1U2jevJiZRfdZeCpkRGjdQfmQp-kEK4DedNOYhc_lK7qt_sNNe0_z8nhknFdO6ZJUdO8hpiHjMOo7MkcwGIgmcqsKm4jMp0sMuDCevqiV10jy4qZ6hN_UGc7jMd4ZoPCjKlSMTzuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60f68ed4a.mp4?token=DsARYu7iAvhjSUWp9Sy3xpDovGrTVDCLl3Voeun5Hy98y781_FYFPVzm0uyvY3OB6bjQ206kbY0bAh1gSdcKXnJp4ludtrwEn0ZMvnxFZDnmaQIRAXjoUOPWgXcFap7hxVzgrGArfUehakfw0ht8ypr-LCx1WYyJxeQkJIFMjVs4y3EHiS5E8Yodpr0FQBAlb-qBldLwix5Wz1U2jevJiZRfdZeCpkRGjdQfmQp-kEK4DedNOYhc_lK7qt_sNNe0_z8nhknFdO6ZJUdO8hpiHjMOo7MkcwGIgmcqsKm4jMp0sMuDCevqiV10jy4qZ6hN_UGc7jMd4ZoPCjKlSMTzuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریز
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/81017" target="_blank">📅 03:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81016">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انفجار مهیب در بانه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/81016" target="_blank">📅 03:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81015">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">فعالیت پدافند هوایی در سوهانک
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/81015" target="_blank">📅 03:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81014">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1366210ff4.mp4?token=IwjHdJYXkZwDSBk7a1FqeP5FIYWtPxKTEwE0LWRi6go3tyq5cOpex7rQzPkCXwlDVlKtaJNraSsF_S9e_uUCQxp0_zH14NDd4DFQuIiRl97fbhstzUwVWc8jtKY-qydf4SpBGC-hPG3c2X_V_rEwbu7GLZx6IGmVTVALpAvSuQIy8I34ndNWbp6Q2UGMBelSZTkF-DHExetPoJ0N5snoxrYmX4J80zWbBx_fUB1UeiGGv9fWZm9BdhxVzx6FWGwbufOT5l7G2VddV04q7Cf4_CpUWNdOBRzEsToVrnKtD-D30trouTm8vZzHp6pipRBpZpPOn6ozMcvPKleIvbTYDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1366210ff4.mp4?token=IwjHdJYXkZwDSBk7a1FqeP5FIYWtPxKTEwE0LWRi6go3tyq5cOpex7rQzPkCXwlDVlKtaJNraSsF_S9e_uUCQxp0_zH14NDd4DFQuIiRl97fbhstzUwVWc8jtKY-qydf4SpBGC-hPG3c2X_V_rEwbu7GLZx6IGmVTVALpAvSuQIy8I34ndNWbp6Q2UGMBelSZTkF-DHExetPoJ0N5snoxrYmX4J80zWbBx_fUB1UeiGGv9fWZm9BdhxVzx6FWGwbufOT5l7G2VddV04q7Cf4_CpUWNdOBRzEsToVrnKtD-D30trouTm8vZzHp6pipRBpZpPOn6ozMcvPKleIvbTYDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهبهان
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/81014" target="_blank">📅 02:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81013">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تایید نشده انفجار تو نارمک  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/81013" target="_blank">📅 02:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81012">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">۵ انفجار مهیب دیگر در بهبهان
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/81012" target="_blank">📅 02:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81011">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">شین: ۶ انفجار در بندر ماهشهر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/81011" target="_blank">📅 02:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81010">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">چندین انفجار تو تبریز
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/81010" target="_blank">📅 02:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81009">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نت شمام کیری شده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81009" target="_blank">📅 02:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81008">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تایید نشده
انفجار تو نارمک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81008" target="_blank">📅 02:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81007">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">به گزارش نیویورک پست، دونالد ترامپ، رئیس‌جمهور آمریکا، خواسته است که جیانی اینفانتینو، رئیس فدراسیون بین‌المللی فوتبال (فیفا)، به عنوان دبیرکل بعدی سازمان ملل متحد منصوب شود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81007" target="_blank">📅 01:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81006">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">حالتون چطوره؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81006" target="_blank">📅 01:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81005">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">چرا باید یه کوه اسمش کلنگ باشه</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81005" target="_blank">📅 00:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81004">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اقا جدی انگار تو کلنگ خبریه
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): آمریکای جنایتکار مراکز هسته‌ای و حساس ایران اسلامی را تهدید به حمله نموده است
-اعلام می‌گردد چنانچه ارتش متجاوز و تروریست آن کشور وارد چنین مرحله‌ای بشود، آن را به عنوان توسعه جنگ در منطقه می‌دانیم و همه منافع آمریکا، هم پیمانان و حامیان آن کشور یاغی و شرور، هدف هجوم قدرتمند نیروهای مسلح جمهوری اسلامی ایران قرار خواهند گرفت
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81004" target="_blank">📅 00:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81003">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">به سیکتیر (۳۱ تیر) آخرین روز ماه تیر رسیدیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81003" target="_blank">📅 00:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81002">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">افتخاری دیگر برای ایران و ایرانی، بستنی سنتی زعفرونی ایرانی مناسب برای افرادی که ضعف رون دارن، بهترین دسر سرد جهان شد. در ادامه هم فالوده و آب هویج بستنی به ترتیب رنک نه و بیست و یک جهان رو گرفتن.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81002" target="_blank">📅 23:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81001">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HuyTJrJizQzq6Eeoatd07MB7ORHeX10dnxX5lEwQJGq8QO7KJ0etpFwifP1Vz4zaNvVABNW7KV8vmjTMOwORP6-XRhK-A9p-BW7lS_UQAfrdDLKWqEgB5-Oa4I75YwlOMoVypzdJaDU9KUS6SMv27bSeRV8zaRBarYZ_s29Y_rILJhUCyb4uDBiDhs5e_aBBirtSE1rzdOrMqvIIZdcdq55U4kWVKD4Ils334CI_G5tHK7HkpH1l4GHdbnogn9-wOj_zJoTt74UlbO9GSb3IJ1GvF270DhM4sxIvi3wiTCjO-vCyoGIZDSblGAp_0wt9HO6cbXydrLZBVSiRe2pTqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۵  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81001" target="_blank">📅 23:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80999">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jGc01HxN_LZGe5IBIGVr-bC7x6TdnUhUidBsN2N8B1TmMGI5gekOnTB76A2nz9ST5fOxJrJWOnkOWdW5wYdXULhWMEniQuE_l5hALgIamn74MhLTSG_62B13yocP1w7Pa5j1bv5qgRCS1ijKtp8rZ86lmdp0bzfuTeaesfSEwePagsKt3rzFxLKv3tTdMGq4g45kGybWY4kvCjUhFlvudWmNa7wmuaW7Cn9o_BkeIlG4gGffZjxGjVhwXT1E2G4UomW31-9yGca9zk-7W9OAQTi_hEzJC2gyyK76pz4oeWZSTgKepzdP9ntTEQ8tMKVaXilxlZi3xsbLHvmThs_r8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dJChc5nz3HEI3GrLoxdRiWqIO6LsMHOAryHZPvzpbmn_xf2_X2cSS_wvEWoWSPGcsL4xMja1waVL95nRZTGPLuKaFMbod0ffrb-GAODh_6KJoZQGnWHNgfk8LcUmwH7zDu5GLAT3ZAn9z1YJ7n0aD502qEGHdFNt3QAqVl6kKxLMgPQH7WTu5L2hnm29xgHKWqKcfoilWa8TZgZ2Y07xHEZAlmfBCALwMIqs43NZfuac2r4xUQ0aR3A7SA5LKrFp3a3bYxU_jyniaCWclZXMbHBE0lhiAo68pT6_5U5XZchHyViTKwzvy1SZfTfJy5A4-1m10WqDFsSlhXZ88fot_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">افتخاری دیگر برای ایران و ایرانی، بستنی سنتی زعفرونی ایرانی مناسب برای افرادی که ضعف رون دارن، بهترین دسر سرد جهان شد.
در ادامه هم فالوده و آب هویج بستنی به ترتیب رنک نه و بیست و یک جهان رو گرفتن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80999" target="_blank">📅 22:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80998">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">جدی این یکی بخدا عی ماخارنا ماخارنا بعضی رسانه ها میگن سپاه سفارت اسرائیلو تو بحرین زده  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80998" target="_blank">📅 22:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80997">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">هشتمین روز اعتصاب غذای گسترده زندانیان در قرلحصار در اعتراض به اعدامها هم سپری شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80997" target="_blank">📅 22:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80996">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">این دفعه بخدا عی ماخارنا ماخارنا ماخارنا  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80996" target="_blank">📅 21:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80994">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uae8e3oQTMjAuqsi84pBZdJ_FF0Y02ocRi2pAUBTUpv9aQYyARs4YXK9Z4bKZtVinazRNiqbNGuzxFxHY8emgrplwMDsGygDw2-WsERqP9775G5c3pSbUwhpkiYr_d6fmRo40X9Lzs32nb4ZNbyTGNODFr09OjnMjcAjZNS0QneSSRTLRYqiRyejroCTcFSnBqFnh0bM0VN7QC6qCJ_9bHKUtcZfZzqZT215T81XeaN9yH-Yj8AyTYis8P4ZxhATCVIX_E_H6JHT6yYMfaq2YvGHhikgGYdj03RALku4QUXfm-qAgqJHwSPUI2aer1nFg4V_WkANb8ABOZq44bqKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxEVjGVAVtj3yFxsTuG77cXulPT6sy_LQz_ni8BecNIG7X2L6YPutFDAT8fUSxx1uDQd7NxxB0Im2CrgZ1qvK81RKXI0bGJCXny4sLMTRSDnssprW_q1OFTZCOVRA4GC_2UWeFhyN0JFqh5hXPe2smnVGnq1zAPbhiL7G5PFJb6OPJZ7VU_oATfeGa3WBC3QfXhE6IFxfLKaTZzzbXINxO2SsG18VgMnqW33I81WiSrrk2oOrG5LMnZ331SS_AfME31QOXZ3AQsfZu9BvYCadc8nPxe7ezGC_yr_6pVEGV6u4jct2eyvOC74JlALGqjk0ZEk5B9zRbL_macmn9tViA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وینی چرا این شکلی شده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80994" target="_blank">📅 21:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80993">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ گفته تاسیسات هسته ای ایران تو کوه کلنگ رو میخواد بمبارون کنه، برای بمبارون کردن این تاسیسات حداقل چیزی حدود ۱۲ تا بمب سنگرشکن لازمه، خارکصه میخواد چیکار کنه خدا میدونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80993" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80992">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بمب افکن های B1 آمریکا از بریتانیا بلند شدن به سمت مقصد نامعلوم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/80992" target="_blank">📅 21:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80991">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W88BRXIu8tDQCD5N_80hC5ht82QxU_JeytO71Hgj1jNIT4Lf_ReWzx2ojurvkQTkIhsgvDceh4IztVms7GhV99_Dqj3V8d5BXGUQFdb-W21Tgs3n7hpjDnC8ZsSv7jM6VCbTqEEflxGIK-aA6MGBVmkiSVfZyeYKCvjlS-jCZVnIDCvtyQ32vbykFPsI4af0yaHc8THQgniUuCDdShlwm_r_BXb4Dt5ttDmfEFXnGdY_yvQkgaT0LdD1bU5uYQQiuVXm48QMADFoRTLk4WxcUvTA70wuZ3F2qv7XnXyN6n8flJzXN2udmFZYFuhHVOmo1Wn8nZiNdHiviCr4GGtIYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80991" target="_blank">📅 20:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80989">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AzoRugX4yVVCeFABHfpUeYursX8Wanyaaeu3s3nAODErKWMHxtqU1XUSCZvAqvuqczrEMTmzKl1llBVUvC2H3JkEWnf1FY7k2MxKcVTHQlus7h90do4IJ_aB-GrCbjdr4myEh0eH0T3GtRO1f13Q5dY9VsIJ9NHvV3JkJxdJm8aGr-eCRuINAr7W8LdJwf17z92n1560CtDPn7V_S-6UboITDibMEn_vNsNmkyFOJUYJZro1VMdqX1OMB0NUa_FAXQ6xSXHDuletgwih27tbf5j8WUr4YK7p0tBtMC16qEr26PS5cdtyGkOGxjTftIiulp4s7NHZwEdNMGyp9KoLcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Os_zQKZZBskWSD2uYNK7sBJoDU_AZmrxedV9ipOkmGHB1bjx0MWAV2tujdpP5x_uVOMjgxrtj2IKOxMGue8ZK43tfQi6MXl7CjVmioyPmVwT0exxsUmodfMzje6NgwVOMVYi7Sdvk_e4b-mT5lJTWTM5y0F2P8UitpAmNcU-8irZlPJPuVzHEsMjK-rgP4HgxIO7Cd_lprysC3hD74eKVx2CftBX7KjmfFnpP7GEwSeD2AXcQkYKOwAzXf1L__DJ1CW1d64N1LxAuLItqLAgPnFo4MHq1cP8anqe4F6TdJt2kmB3XKaIjaPPqI7vxj9bIU2N5LGPUrx_9CfnfNfrAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به گزارش خبرگزاری verse خانمی انگلیسی که با خودش ازدواج کرده بود، از خودش طلاق گرفت چون تو رابطه به توافق نرسید و احساس تنهایی میکرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/80989" target="_blank">📅 20:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80988">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc36a1a784.mp4?token=ky4WQ6Iq7IheDN0Y6fYLZkTuKtlAF3oYFVM9vw1TrOI9BWIzHhHb4ENfk1BJmL-rr5Jqx0uDbEvFWKJ8e2p-ek6s2Z7NGAFAUeLoFAYJLF7ZLDZ-FGJpixwJMDIsDMIl-t3G5XWLlHanh4xYkU0q1otWzhhib8RsDLBmK-wR0XtMy1gvksUbgOjfejGpYr-Sk0kXynDUqq-ZDrqwA7Aynzmk_TlxQmLwPCpg4RTWKD28odUObOf9ab3jqDFlhqaX-Z4M9sM3frdmZqnttUrmgKF0dFn7tT-3j0sZTG5ECyg2IpeuI3IAwMKjpKxGAqLp_vr68FSWQJ7qIYzmWQCF3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc36a1a784.mp4?token=ky4WQ6Iq7IheDN0Y6fYLZkTuKtlAF3oYFVM9vw1TrOI9BWIzHhHb4ENfk1BJmL-rr5Jqx0uDbEvFWKJ8e2p-ek6s2Z7NGAFAUeLoFAYJLF7ZLDZ-FGJpixwJMDIsDMIl-t3G5XWLlHanh4xYkU0q1otWzhhib8RsDLBmK-wR0XtMy1gvksUbgOjfejGpYr-Sk0kXynDUqq-ZDrqwA7Aynzmk_TlxQmLwPCpg4RTWKD28odUObOf9ab3jqDFlhqaX-Z4M9sM3frdmZqnttUrmgKF0dFn7tT-3j0sZTG5ECyg2IpeuI3IAwMKjpKxGAqLp_vr68FSWQJ7qIYzmWQCF3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید دکی.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80988" target="_blank">📅 19:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80987">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🗣️
تعرفه سرویس‌های Retro  پلن نامحدود
1️⃣
ماهه :
🌀
1 کاربره |  99  هزار تومان ‌
🌀
2 کاربره | 149 هزار تومان
🌀
3 کاربره | 199 هزار تومان  پلن حجمی
1️⃣
ماهه اقتصادی :
🌀
10 گیگ | 30 هزار تومان
🌀
20 گیگ | 50 هزار تومان
🌀
30 گیگ | 75 هزار تومان
🌀
50 گیگ | 110…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80987" target="_blank">📅 19:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80986">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRetro Channel</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-vdwNIt-6MQLxRKv2r_K8iKBVA2oDV71r-baUCDr-GzQyLXF-o7ADBAS7jnfcBsQXfc3czPsBWAAmOa8fKa5MoGMLy0K3STj_-MZIgHlTND_DOAlBWgwJV7A3aKBhrUq17OgKb6vF-PtU3BBLRbeMqBG79EpKo3b2q9_UBBgmB8Clc5pLC8IeB1N4ZKUYsIqSsjW3gyh6E9oawE9PZL7qICo4ylLZlCOcUMmrbyj2auZz8X7PmZVNQzt9vDZTwgQOqrK3oT5NuZ6NATG4Wous9WD8W-Xxe9WmhvF7DDeZVDOY9xbCo_7yw7XTTfIBdZFo3n_ajIh4GcJpCuud9pbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣️
تعرفه سرویس‌های Retro
پلن نامحدود
1️⃣
ماهه :
🌀
1 کاربره |  99  هزار تومان
‌
🌀
2 کاربره |
149 هزار تومان
🌀
3 کاربره |
199 هزار تومان
پلن حجمی
1️⃣
ماهه اقتصادی :
🌀
10 گیگ | 30 هزار تومان
🌀
20 گیگ | 50 هزار تومان
🌀
30 گیگ | 75 هزار تومان
🌀
50 گیگ | 110 هزار تومان
🌀
100 گیگ | 175 هزار تومان
پلن حجمی
1️⃣
ماهه VIP :
🌀
5 گیگ | 35 هزار تومان
🌀
10 گیگ | 60 هزار تومان
🌀
20 گیگ | 100 هزار تومان
🌀
50 گیگ | 200 هزار تومان
🌀
100 گیگ | 350 هزار تومان
تمامی پلن ها دارای تست رایگان میباشند.
⚡
پلن های حجمی بدون محدود کاربر هستند.
♾
مولتی لوکیشن
💸
پشتیبانی
7️⃣
/
4️⃣
2️⃣
🏪
⭐
با تهیه یک اشتراک Retro، به اینترنت آزاد و بدون محدودیت دسترسی خواهید داشت.
⭐
خرید
|
کانال
|
پشتیبانی</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/80986" target="_blank">📅 19:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80983">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A6fUx6C6P1YRioI0R4W3Xh3Sxa5fSsXxcgFuY2iEfrqXxCZ9jc1QoY6Q5DQbgAzqPnmPcE8Hq_Xt39nQ8qI4zCrOEsrXB6EwsxZtwKQoBHkaYl0-PRuih7so9L44DwFz4AFw46BmUB1IZ3Y1d01EY_kfLQLk-veYZkufic_7sY8W1J9hczPnu-H55m1yDQ0I0bFyVNe4l9kOfftWw2MCeiG9JWR1XQS5a1vzRiokIfQwPWu7NGyL8NnYWpzL67BJallpmJ_Qnh75GU2Myu0IG0cRN4P4jwLalZbKQY2UbFq8rDBeP30EZR_y6LIbt7YmbYG6N4ZOHwxQw-mIzoTUHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WLMsbXw31UkSOM-7L3zT5WnVxpoUl4YaIJz2yfdAd9-XFXL_uTif2H5VbY36trc4VA5UiU1-xbNSP-nKPhvWtTbYXM_f19M825ltm4uAsGH5iqT2-ZSpDQt2Mq2wFCoDFS8d6kvq9y8jmHUyik56uL3QzSJeA82U4qc1e1ynGFlV6LJynYQI1FbsyQq07DYDbcYXML_0C42t1_m4ONQQcOEFbZU3e4X75S2oB5IXZEV3JGeL2pkNzNGIUBT0g8pBF5GjHtKAvbMwFejlV79Jk93XZCAuGTTH_IBZcJ4p0a1V_uM6hR9LXj_e_hEjMvRQ0KynY6z9RYFXHqMizGap7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J7R_IShUSbUdBmDZy8sNAtTUlhzwCadATSrS5QRx4dW3pIgQHhOmSKcaRK_U7ZI5lHQhyt_FTOZ8yB_eMcZwQhBPZkYudGpw_aqdHeLHb9ia7FmuwA1Vp7Rch5sQLf-ZQaKLor4q6xDPUM83Oz_qb7qQtA2WjXTkXou0piKfYy-ovpKbj2wgC6n0Kb1lBvP19SI93oe9CMbnFT0yGX1IUDA6vOZUJJnjeyyzBWGP3Wxp4vu_wh6apqlQ4dX4vmrTmLV2cSaXj81Akm6x7OlwftmubG_h0vBzBaTlqYmgG9GExGjlz85n5q5al2m_bnqRsetf5DYgyT-eUj13terjfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فعلا عکسا ربکا رو ببیند تا من برم و برگردم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80983" target="_blank">📅 19:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80982">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4221f89e3c.mp4?token=pOw5YkBMKJLsnHphdwJSn1hd482TW5Hx27TGVzk3VcC8pTIboE49gJqCyUA6yohQyGR11P8E4R2_L-auQRJbM_Ze3hMGLgLHtfbaYxy-BBY_DJgZS_WWYFDqfF5kwBu1Hs_LnWtHhwKqhso6mPt7ny2LGgbc04MuD2w1lTBws3uQjDlYPilPYEp3zVAjQ0aAceUhx_omgQjEmBrqjrFZnsiWbZn_V2l62lKPx4jz72Ts4lD7UmkVQLbwh1jSOG_AbFjL5gUkkxl7gzO4Km59hOmW6_Tcx2ULrhMT2qtBMmN3H7ynyWiap40JyYCsPK60Zv4buEcYwr171O-2gEu3UVtH9CKnRwVmJDO4ONZ4XjzLEZreEGseTM266wnIoNVV9TC3i33JalhjX3XKTnGFAleQLdHYOYd6w7nbnPycVCwC3JDhC0gPopxgA-RuB0rv9oJkIY0Z3fYkzwaCU7lKN71PUDfRxg4N6jzFsyff9eo2WgPzVD15d66N2Fayl7J9akEq-9Ev02LTjsFKpWjilCS40rvhQ0Obdi3SHhfsw8hIiNxAKv72W70CbJPdrWWtgCeiz7AZHdxHD6yWg-ULK_gc7NObG1FmVQER-ZCcISYN02k0kgVyIXY7N0WeX5LNGQTjVbw4VcN6T1lo99DW6WJpuhOp1l4ycVryl5whjfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4221f89e3c.mp4?token=pOw5YkBMKJLsnHphdwJSn1hd482TW5Hx27TGVzk3VcC8pTIboE49gJqCyUA6yohQyGR11P8E4R2_L-auQRJbM_Ze3hMGLgLHtfbaYxy-BBY_DJgZS_WWYFDqfF5kwBu1Hs_LnWtHhwKqhso6mPt7ny2LGgbc04MuD2w1lTBws3uQjDlYPilPYEp3zVAjQ0aAceUhx_omgQjEmBrqjrFZnsiWbZn_V2l62lKPx4jz72Ts4lD7UmkVQLbwh1jSOG_AbFjL5gUkkxl7gzO4Km59hOmW6_Tcx2ULrhMT2qtBMmN3H7ynyWiap40JyYCsPK60Zv4buEcYwr171O-2gEu3UVtH9CKnRwVmJDO4ONZ4XjzLEZreEGseTM266wnIoNVV9TC3i33JalhjX3XKTnGFAleQLdHYOYd6w7nbnPycVCwC3JDhC0gPopxgA-RuB0rv9oJkIY0Z3fYkzwaCU7lKN71PUDfRxg4N6jzFsyff9eo2WgPzVD15d66N2Fayl7J9akEq-9Ev02LTjsFKpWjilCS40rvhQ0Obdi3SHhfsw8hIiNxAKv72W70CbJPdrWWtgCeiz7AZHdxHD6yWg-ULK_gc7NObG1FmVQER-ZCcISYN02k0kgVyIXY7N0WeX5LNGQTjVbw4VcN6T1lo99DW6WJpuhOp1l4ycVryl5whjfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید دکی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/80982" target="_blank">📅 19:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80981">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZMRyeRgTLUSSjbTJ3Ynw5wgHZLytkZ-fqgBWS18mvsskpicrQiMQzurxdhL8ZB3B6tUPoN2GlLS17yPea6cCMTXL9YP3Pnv_c-1ny2mwmqLqMEf2u6B6R__UHXIHhglvfPyN9R7_ZzL1mJ-Qf4VhclwRr6nQlfjaEavBVaJabtKOB7G7T-J9VK5xUwKWbvwmqKBu0-4lfgP34_JW-YHm9nrhIwANF1gsKtNmrUsbLrxoMJGVGwoR0PzrEqoUWNl7tYcaRBAVLwp2nAuHucDO0e_upvgvsIDzWoUattSe0SWrBeuPLK8DDaBnDXHLdB23JtL4De15YfHnQJWd1KlVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی جبهه مقاومت شعبه اروپا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80981" target="_blank">📅 19:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80980">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rckGBgp0ep7hgLjQ_9p3Wr5chK_sFFWdlHsVbOPfD3VDKIucbOokbeLcX2qJUX1A3hQYKFSHeXdiQRtgFUUcoazfVf8IrXRFbAu6VGjvq25K5lyGHdtZ7W8vMIBDHigBbbbuwf0gH3kOlJpZWSpU3yy1adHwlL7e_872AG-ZruL-vNEv1XF3IAx0jZNWbtmeFksPOUXVwqqFwT9EWSy6wZxVj_lh2HCl9TWCuqCpFZpkEPidpCgFwPjQRbsL6HmteMa27SJA7MWDPjZN8hBGWexe-aNXM8YDRSZEsyyA_cAJ7GQyrBj1sgytURvLgEXGlHignBzWXOb4wvgDJRnVaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
مجموع جوایز پنج هزار دلاری بلک‌جک زنده
🃏
🔥
با ثبت پیش‌بینی حداقل ۵۰٫۰۰۰ ریالی در بازی بلک‌جک زنده جایگاهتان را در تورنمنت ارتقا دهید و سهم بیشتری را از مجموع جوایز ۵ هزار دلاری بت فوروارد دریافت کنید. در صورتی که جزو ۵۰ نفر برتر تورنمنت باشید بر اساس رتبه تا سقف ۲۰ میلیون ریال هدیه نقدی به شما تعلق خواهد گرفت.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/BLN
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g30
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/80980" target="_blank">📅 19:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80978">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b79960724.mp4?token=HoaVQ13HFBGV8491SBFf4OAkSKcus-sagYnHrSOk2zQ9SQn0rwJdpDX2VNkanfS9TWqZJ_yKIvWzukx8vwQNxjyVSfHBSzltN3QR8CPSzPBziaAdblR5Pm5blJuYOUOjBo3KvKcQ8f50ib4HT8uOE7hr5SaVVG1meGVSO1OUhn2aE6bVRMiRHkdfgL2PAqgKPMwRMzgxb46gilmdfu55mRX2_borr23cmA7ZowkJ3YUnVHwdSAmI9v5XsjBtcBfjq31-9-Rml6czsNgluNWUPo3aL4X1Ga8VEdO5u4OTar9o3s98iazdkxOtMxHtI85ZJvcMYbOjxlbjQ3RqBQZ72A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b79960724.mp4?token=HoaVQ13HFBGV8491SBFf4OAkSKcus-sagYnHrSOk2zQ9SQn0rwJdpDX2VNkanfS9TWqZJ_yKIvWzukx8vwQNxjyVSfHBSzltN3QR8CPSzPBziaAdblR5Pm5blJuYOUOjBo3KvKcQ8f50ib4HT8uOE7hr5SaVVG1meGVSO1OUhn2aE6bVRMiRHkdfgL2PAqgKPMwRMzgxb46gilmdfu55mRX2_borr23cmA7ZowkJ3YUnVHwdSAmI9v5XsjBtcBfjq31-9-Rml6czsNgluNWUPo3aL4X1Ga8VEdO5u4OTar9o3s98iazdkxOtMxHtI85ZJvcMYbOjxlbjQ3RqBQZ72A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو جشن قهرمانی اسپانیا یرمی پینو رو اینطوری معرفی کردند:
قبلنا بهش میگفتند کریس رونالدو ولی فرقشون اینه که پینو جام جهانی برده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/80978" target="_blank">📅 18:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80977">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](𝙼𝚎𝚑𝚍𝚒)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPy-b2MDhr_W2MS9H2am4uhzmAhDMEF4v4hD_LhGFpQIPK6NzlAUVo3KRJv-Mau7R_QaXrwnHvo3bOq6PdIb9fdRYFnPOSbS5fGsLoGKH4gBJkopYrWCQQdldDhMKeOKA03EaEaGJNcexy1HLPdHuU1mA7HQA5jjzUZtFyFxjTZqcInt-AkaMbeqVg_y9vjuvXCsTR4BG3iSbJ5H0Le7BmbnGDw6FhqXfPZRdsOw1VBIMIkhpDzLz59h-WHf3GyxjLpZC4KHsXi0AVHiT8PEd2G2Dw4pix9SpHh2EDOk2fiZdjcGI3d7tuR73X_NvbvRbhSXqSYWqG1Q-xGfznvVkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حریف نبود</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80977" target="_blank">📅 18:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80975">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بگردید کارنامه منو تو چنل پیدا کنید، قبل امتحانا یسر نگاش کنید امید به زندگی بگیرید</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80975" target="_blank">📅 18:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80974">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">امتحاناتون چطور میگذره؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80974" target="_blank">📅 18:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80970">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خب دیگه چخبر</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80970" target="_blank">📅 17:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80965">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آمریکا یچیزی حدود ۱۰۰ تا سوخت رسان تو اسرائیل جا داده، این تعداد سوخت رسان میتونه ۲۰۰ تا ۶۰۰ تا جنگنده رو ساپورت کنه، معلوم نیست چه گوهی میخوان بخورن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80965" target="_blank">📅 17:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80964">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">آمریکا یچیزی حدود ۱۰۰ تا سوخت رسان تو اسرائیل جا داده، این تعداد سوخت رسان میتونه ۲۰۰ تا ۶۰۰ تا جنگنده رو ساپورت کنه، معلوم نیست چه گوهی میخوان بخورن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80964" target="_blank">📅 17:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80963">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">عادل با شرف
❤️</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80963" target="_blank">📅 17:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80962">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ما کی باشیم نظر بدیم اصلا، ولش کن</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80962" target="_blank">📅 17:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80961">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دعوای عادل و صداسیما دعوا خانوادگیه، دخالت نکنیم بهتره.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80961" target="_blank">📅 17:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80960">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جنوبیا نگران جنگ نباشید احلام بجاتون موهیتو خورد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80960" target="_blank">📅 16:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80959">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKAjCWHBcgkVORgtRYX1Adqvg2F-JLmpQLsXvLns0m0oO4WCEx2j2I0IleM9lTC3jQpAO0Yun_TYfmT3blqHvBVBKMHJZulNSUoNr63Qt_H3kWAEUm3onFvN_HcDE29xrfpavBtYSVi5f-qgpg_BGXdxXKHWs0jltQWFi229qWBj6iPg3YDdIUCMZAwVWtkA47evJtm9qcdqslOmePz-mKbTTqJFx4nKJ8XkUFqlrb0UAkQ7EjTGWOgyES11dy9EoOXnZF7GHQpCRCwqdzM5S7VS8cbENA19UQM5nhzG9O5TZjozHytQPU8tM0V8r5ctelCJdlJ-V5t3dxLITNP44w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنوبیا نگران جنگ نباشید احلام بجاتون موهیتو خورد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80959" target="_blank">📅 16:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80958">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzPeBkmpRzxItcM0RopEjOkQe_XGUs3jtXQtLk4wQxNYAheySHffQWFwzk7-EfGic7idAkGe-oeHwzL9h4dJnT8SNw57aUNYHL-48jITthDAc0WmwZ3WB2Td2JzptqZLhJLo3Yeq_xEEEC5r4KvUEEf00p4LrtBl2JmtOTL2aZxPQ80PdIeuwEKPrXknzNuvCsOMY0qbxxiL_yhmqgGkmHB5iZZoSjsAMlQDTVl2oDEZcd9IA2rxK1ta4NudkgQ_ew7X72zCktiJ2JJxN1jdDDKFQpLcI6RRWYXiKgiRoWzkYPA6n1-g075O9g8BvLcqOX59UdaYaMBR1K4qOpayCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانم ناجی و تتویی که خیلی وقت پیش از چشماش زد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80958" target="_blank">📅 16:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80957">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">انقدر هوا گرمه که هر روز از دیروز آدم پخته تری میشم.
پروکسی | پروکسی
پروکسی | پروکسی | پروکسی
پروکسی | پروکسی | پروکسی
پروکسی | پروکسی | پروکسی
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80957" target="_blank">📅 16:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80955">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دعوای عادل و صداسیما دعوا خانوادگیه، دخالت نکنیم بهتره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/80955" target="_blank">📅 15:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80954">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بارسا لاپورتو گرفت</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80954" target="_blank">📅 15:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80953">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">جرزوالم پست: ترامپ پیشنهاد قطر و پاکستان برای آتش بس ده روز با ایران را رد کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/80953" target="_blank">📅 15:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80952">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سپاه عکس بسیجی جان بر کف فران تورس و همچین میمون فلسطینی رو چسبوند به پهپاد شاهد و بعد شلیک کرد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/80952" target="_blank">📅 14:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80951">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dbc0a853b.mp4?token=A40wQ35oBlHtGC7x-DmT3VwDrWbzOhYhMIxLC96bQ9va5i84hgPvTsgIa6pRAFECk4dS6eIgIDetPEYLkhYw0hyUguBkHG9BT31Zh_sJCjEej7kkQTcJx-4nxH1pk3F6A_YrQf7iNxqF5Y25hod007FzDqdFX2xyR-lM2Mt1bX6K7PgVu1E_MenoqPw0F6cpI0mEPPGZjR2RIS2WRvkPV86vKWDSj5XJvBaSwYihGFpvn2CA0Wcs1efeN26ZgcHeXpftCQsrTS37SylCV0nFmx3k2VoqPjiE-0vkP8nLo6pZOXLXptdngD8StxYtM6R5tMS-tO6cgPGpWLEQYhtLkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dbc0a853b.mp4?token=A40wQ35oBlHtGC7x-DmT3VwDrWbzOhYhMIxLC96bQ9va5i84hgPvTsgIa6pRAFECk4dS6eIgIDetPEYLkhYw0hyUguBkHG9BT31Zh_sJCjEej7kkQTcJx-4nxH1pk3F6A_YrQf7iNxqF5Y25hod007FzDqdFX2xyR-lM2Mt1bX6K7PgVu1E_MenoqPw0F6cpI0mEPPGZjR2RIS2WRvkPV86vKWDSj5XJvBaSwYihGFpvn2CA0Wcs1efeN26ZgcHeXpftCQsrTS37SylCV0nFmx3k2VoqPjiE-0vkP8nLo6pZOXLXptdngD8StxYtM6R5tMS-tO6cgPGpWLEQYhtLkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه عکس بسیجی جان بر کف فران تورس و همچین میمون فلسطینی رو چسبوند به پهپاد شاهد و بعد شلیک کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/80951" target="_blank">📅 14:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80950">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">قاطی "همون همیشگی" امشب یه همون همیشگی دیگه هم هست و اون "اطرافِ نیروگاه هسته ای بوشهره" که دوباره زدنش  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/80950" target="_blank">📅 14:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80949">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ببخشید چه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/80949" target="_blank">📅 13:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80948">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ببخشید چه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/80948" target="_blank">📅 13:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80947">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTlzikI5pgmxDM8OcaZ0ohrQckeKetccDGmwaP_GvnQWB9iXz8dhs2kIC3IA7llQmCUqN_Jwi_B_IorUPLOw8lL2xN7fceEtq2R5RcF0B3y5V8SFxotg1UdmoPnmOrBbykH9963KcCL-uv8mXOUvXwvnQLg2jV-5CXTvvQ3S0_ypWTciQ0pNTt_EmV3Y3ibBDZgKbBLRgGCRDVDiJzQFkVcMp34PtqBmnVfNTRDdu-01-dVyvqqx1lgQ5HH8NZTsdMbnC63XsoXVnMPrL4MKSkVtuaka4gPMXc_egOf5jeXE-o7JVlaguW-mTrBRo2-OC4LWe0T5A0eRzH-S-HYTOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید چه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/80947" target="_blank">📅 13:18 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80946">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">شات جدید یاس.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/80946" target="_blank">📅 13:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80945">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شات جدید یاس.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/80945" target="_blank">📅 12:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80944">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGloriø</strong></div>
<div class="tg-text">رنگ پوست رو میخوای چیکار کنی داداش؟</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/80944" target="_blank">📅 11:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80943">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usaDeTX07gvndVm-pRV6BLXT38CkCpHtEYpN9_P2XvcNLkE1khR3xDvFoZblTPHxJVN_cKjazHPr7HsHBJg9RXf3omU04uNCto1u-6FxSzM-uhUymEIceKEl5U0lkmEr0JJu8EjHJEEOKJq7RxJz5gJE6JQXwH1lba8O0qFM77VXphPTo932MkbIvEbOf5emBmlKcV-s_Iva-P8LxLZnd252WaZF53vWAFoCozemwqtYJfLYrqyNAU1rxKBxqZA-gx1YdiqBxh96Vp-3IJOxg29oZqcYavo6quZJctUHkEA0TtuAmeqW3UdGBSKYV2LIdorZY7WBbUc6lRiYCvn_hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچی، فقط همینو بگم وینیسیوس رفته عمل زیبایی انجام داده.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/80943" target="_blank">📅 10:55 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
